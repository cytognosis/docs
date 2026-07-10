# GenomeKG — What Was Built, Why, and How

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: leadership
> **Tags**: `strategy`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

> Session: b591c0f4 (May 2026) | 19 commits, 56 tests passing

---

## Purpose

The GenomeKG subsystem makes Cytos the genomic data layer for the Cytognosis platform. It adds:
1. **Personal genome ingestion** (Shahin + Olivia WGS via TileDB-VCF)
2. **Cohort genome ingestion** (PEC 218+226 samples)
3. **LDGM precision matrices** (graphLD-compatible sparse LD for statistical genetics)
4. **GWAS associations** (3 psychiatric traits in Neo4j KG with gene proximity links)
5. **Sequence Ontology** (SO term hierarchy for variant type classification)
6. **VRS 2.0** (GA4GH variant representation standard)

---

## Architecture

```
                 ┌─────────────────────────────────────────┐
                 │           Neo4j GenomeKG                 │
                 │  Chromosome ──► Gene ──► GWASHit → Trait │
                 └────────────────┬────────────────────────┘
                                  │ NEAR_GENE / ASSOCIATED_WITH
          ┌───────────────────────┼───────────────────────┐
          │                       │                       │
    TileDB-VCF              LDGM TileDB              SO DAG
  (variant calls)        (precision matrices)     (NetworkX)
  Shahin/Olivia/PEC      1360 UKBB blocks        2615 terms
```

### Data Flow
```
Raw VCF/CRAM → tiledbvcf ingest → TileDB-VCF arrays
                                          │
                                    query variants
                                          │
                              vrs.py → VRS Allele/SV ID
                                          │
                               (seqrepo) → Neo4j Variant node

GWAS TSV → load_gwas_ssf() → polars DataFrame
                                     │
                          filter p<5e-8
                                     │
                       → Neo4j GWASHit + Trait + NEAR_GENE

LDGM edgelist → ingest_edgelist() → TileDB sparse Ω matrix
                                          │
                              DuckDB index (block_id, chrom, pos)
                                          │
                        graphld.io.load_ldgm() → PrecisionOperator
                                          │
                          align_ldgm_to_sumstats() → z-scores
```

---

## Key Design Choices Explained

### Why TileDB for LDGM (not NPZ)?
**Rule: No NPZ ever.** NPZ is Python-specific — unreadable from R, Julia, C++.
TileDB sparse arrays are language-agnostic (R/Python/Julia/C++ APIs all exist).
Each LDGM block = one TileDB sparse array. DuckDB indexes all 1,360 blocks.

### Why a DuckDB index?
We need to look up "which blocks cover chromosome X, positions A–B?" without
loading all 1,360 TileDB arrays. DuckDB `ld_blocks` table:
```
block_id | chromosome | start_bp | end_bp | n_snps | ancestry | hancestro | edgelist_path | snplist_path
```
Queries are instant (in-memory columnar scan).

### Why ±500kb for NEAR_GENE?
Standard genomic convention for cis-regulatory window. Nearly all eQTL associations
for a gene fall within 500kb of the gene body. Creates interpretable GWASHit → Gene links
without requiring full eQTL data.

### Why is LDGM a precision matrix (Ω) not an LD matrix (R)?
- **R** = LD correlation matrix (dense, pairwise SNP correlations)
- **Ω = R⁻¹** = LD precision matrix (sparse — most entries are exactly zero)
- LDGM exploits this sparsity: only edges with Ω_ij ≠ 0 stored
- Used for: graphREML heritability, BLUP polygenic scores, Gibbs sampling
- Dense R matrices (Pan-UKBB) handled separately in `graphld/dense.py`

### SO OBO upstream bugs
The SO OBO file from `purl.obolibrary.org` has two parse-breaking bugs:
1. `xref:` lines with backslash-colon URLs (invalid IRI per RFC3987)
2. `PMID: 12345` (space after colon) in `def:` xref lists

Fixed in `so.py:load_so_obo()` via two regex subs before passing to pronto.

---

## Module Reference

### `src/cytos/genomics/gwas.py`
- `load_gwas_ssf(path)` — auto-detects format: GWAS-SSF 1.0, harmonized `hm_*`, PGC minimal
- `filter_genome_wide_sig(df, threshold=5e-8)` — filters to GWS hits
- `gwas_to_neo4j(df, trait, source)` — writes ASSOCIATED_WITH (requires Variant nodes)
- `to_gwas_ssf_parquet(df, path)` — exports to GWAS-SSF Parquet

### `src/cytos/genomics/graphld/interface.py`
- `list_blocks(ancestry, chromosome)` — query DuckDB index
- `load_block_precision(block_id)` — returns native graphLD `PrecisionOperator`
- `load_chromosome_blocks(chromosome)` — all blocks for one chrom
- `align_block_sumstats(sumstats, block_id)` — GWAS z-score alignment
- `run_graphreml(sumstats, chromosomes, n_samples)` — heritability estimation
- `compute_blup_scores(sumstats, h2, n_samples)` — polygenic scores

### `src/cytos/genomics/so.py`
- `load_so_obo(path)` → `nx.DiGraph` (sanitizes upstream bugs)
- `get_so_term(dag, accession)` → `SOTerm | None`
- `get_so_children(dag, accession, depth)` → list of descendant accessions
- `get_subtypes` = alias for `get_so_children`
- `is_a(dag, child, parent)` → bool (direct or transitive)
- `iter_variant_terms(dag)` → generator of (accession, name) tuples
- `so_to_neo4j(dag)` → write SO term nodes to Neo4j
- `infer_so_class(ref, alts, svtype)` → SO CURIE for a variant

### `src/cytos/genomics/vcf.py`
- `CytosVCFDataset` — TileDB-VCF wrapper class
- `ingest_vcf(vcf_path, store_uri, sample_ids)` — ingest VCF into TileDB
- `open_cram(cram_path, reference)` — open CRAM via pysam
- `fetch_reads(cram, chrom, start, end)` — iterator over reads
- `cram_coverage(cram_path, regions)` — per-region coverage DataFrame
- `validate_tbx1_insertion(cram_path, insertion_fa)` — TBX1 SV validation

---

## Validated Results

| Validation | Result |
|-----------|--------|
| LDGM block load (chr22 first block) | Shape (4120, 4120) sparse Ω |
| GWAS alignment (SCZ × chr22) | 2,069 / 10,267 SNPs matched (20.2%) |
| Neo4j Trait nodes | 3 (SCZ, BIP, MDD) with EFO/MONDO IDs |
| Neo4j GWASHit nodes | 19,621 at p < 5×10⁻⁸ |
| NEAR_GENE edges | 795,297 (±500kb to GENCODE v47 genes) |
| SO terms loaded | 2,615 terms, 2,510 is_a edges |
| Test suite (genomics) | 56 pass, 4 skip |
| PEC WGS ingested | 218/218 samples |
| PEC RNA ingested | 226/226 samples |
