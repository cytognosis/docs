# Genomic Standards and Protocols

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: engineers
> **Tags**: `engineering`
> **Variants**: Technical (this doc) - Readable (genomic-standards.md in Obsidian vault: 04-Engineering/cytos/) - Agent (n/a)

> Research notes on all external standards used in Cytos GenomeKG.
> Consolidated from multiple Antigravity sessions (b591c0f4, cd6537fc).

---

## GA4GH VRS 2.0 — Variant Representation Specification

**Purpose:** Language-agnostic, globally unique identifiers for genomic variants.

**Spec:** https://vrs.ga4gh.org/en/stable/

### Variant types used in Cytos

| Variant class | VRS type | Trigger |
|--------------|---------|---------|
| SNP / INDEL | `Allele` with `SequenceLocation` | len(ref)==1 and len(alt)==1, or indel |
| Copy number variant | `CopyNumberChange` | `SVTYPE=DEL/DUP/CNV` |
| Structural variant (insertion, translocation) | `Adjacency` | `SVTYPE=INS/BND/INV` |
| Multi-sample frequency | `VariationDescriptor` | cohort-level allele frequency |

### VRS ID computation
VRS IDs are computed as: `ga4gh:VA.<sha512t24u>` where `sha512t24u` is a truncated
SHA-512 digest of the canonical JSON representation. Requires:
1. `seqrepo` — local sequence database for reference allele lookup
2. `ga4gh-vrs` Python package
3. `ga4gh-vrs[extras]` for the translator

**Seqrepo install:**
```bash
pip install biocommons.seqrepo
seqrepo pull -i 2021-01-29   # ~50GB
export SEQREPO_ROOT=~/datasets/04-identifiers/seqrepo
```

### TBX1 SV (Shahin's diagnostic variant)
Located at chr22:19,756,000 (GRCh38). Insertion ~2.5kb.
Sequence in `https://github.com/cytognosis/datasets/tree/main/06-genotype/personal/Shahin/insertion_TBX1.fa`.
VRS class: `Adjacency` with two `SequenceLocation` breakpoints.
Clinical significance: Pathogenic, OMIM 188400 (DiGeorge syndrome / 22q11.2DS).

---

## GWAS-SSF 1.0 — GWAS Summary Statistics Format

**Spec:** https://github.com/EBISPOT/gwas-summary-statistics-standard

### Column mapping (Cytos internal names)
| GWAS-SSF name | Cytos column | Notes |
|--------------|-------------|-------|
| `rsid` | `rsid` | |
| `chromosome` | `chrom` | normalized to `chr1`, `chrX` etc. |
| `base_pair_location` | `pos` | GRCh38 |
| `effect_allele` | `alt` | |
| `other_allele` | `ref` | |
| `beta` | `beta` | log OR for binary traits |
| `standard_error` | `se` | |
| `p_value` | `pval` | |
| `effect_allele_frequency` | `eaf` | |
| `n` | `n` | total sample size |

### Auto-detection logic in `gwas.py`
```
if "hm_rsid" in cols:       # GWAS Catalog harmonized format
    use hm_* columns
elif "OR" in cols:          # PGC minimal format
    beta = log(OR)
else:                       # GWAS-SSF native
    use standard columns
```

### PGC Minimal Format
PGC Psychiatric Genomics Consortium uses a non-standard format:
`CHR | BP | SNP | A1 | A2 | OR | SE | P`
- `A1` = effect allele
- `OR` = odds ratio (convert to beta via `log(OR)`)
- No EAF column

PGC files at `data/gwas/pgc/`:
```
ADHD.tsv.gz   ALCH.tsv.gz   AN.tsv.gz    ANX.tsv.gz
ASD.tsv.gz    BIP.tsv.gz    CANNABIS.tsv.gz  INSOMNIA.tsv.gz
MDD.tsv.gz    OCD.tsv.gz    PTSD.tsv.gz  SCZ.tsv.gz
TOURETTE.tsv.gz  TS.tsv.gz
```

---

## Sequence Ontology (SO)

**Source:** http://www.sequenceontology.org/
**OBO file:** `https://github.com/cytognosis/datasets/tree/main/04-identifiers/ontologies/so.obo`
**Version loaded:** 2.5.3 (latest release)

### Key term accessions

| Term | Accession | Notes |
|------|-----------|-------|
| `sequence_variant` | SO:0001060 | Root of all variant types |
| `SNV` | SO:0001483 | Single nucleotide variant |
| `SNP` | SO:0000694 | Child of SNV (population-level) |
| `substitution` | SO:1000002 | Parent of SNV |
| `insertion` | SO:0000667 | |
| `deletion` | SO:0000159 | |
| `copy_number_variation` | SO:0001019 | CNV |
| `structural_variant` | SO:0001537 | SV root |
| `gene` | SO:0000704 | Gene feature |
| `exon` | SO:0000147 | Exon feature |

### Hierarchy (partial)
```
sequence_variant (SO:0001060)
  └─ substitution (SO:1000002)
       └─ SNV (SO:0001483)
            └─ SNP (SO:0000694)
  └─ structural_variant (SO:0001537)
       └─ copy_number_variation (SO:0001019)
```

### Upstream OBO Bugs (Fixed)
The official SO OBO file from purl.obolibrary.org has two breaking parse errors:
1. `xref: http://www.ncbi.nlm.nih.gov/...` — backslash-colon (`:`) in URL is invalid per RFC3987
2. `PMID: 12345` — space after colon within `def:` xref brackets

Fixed in `so.py:load_so_obo()`:
```python
text = re.sub(r'xref: (https?://[^\n]+)', r'xref: "\1"', text)
text = re.sub(r'PMID: (\d+)', r'PMID:\1', text)
```

---

## HANCESTRO — Human Ancestry Ontology

**Purpose:** Standardized ancestry labels for genetic studies.
**Source:** https://www.ebi.ac.uk/ols4/ontologies/hancestro

### Ancestry mapping used in LDGM DuckDB index

```python
ANCESTRY_CURIE = {
    'EUR': 'HANCESTRO:0005',  # European
    'EAS': 'HANCESTRO:0009',  # East Asian
    'AFR': 'HANCESTRO:0010',  # African
    'AMR': 'HANCESTRO:0013',  # Admixed American
    'CSA': 'HANCESTRO:0006',  # Central/South Asian
    'MID': 'HANCESTRO:0015',  # Middle Eastern
}
```

---

## EFO + MONDO — Trait and Disease Ontologies

Used for `Trait` node properties in Neo4j:
- **EFO** (Experimental Factor Ontology) — GWAS Catalog trait IDs
- **MONDO** (Mondo Disease Ontology) — disease-level IDs

### Trait EFO/MONDO mapping (loaded traits)

| Trait | EFO ID | MONDO ID | PMID |
|-------|--------|----------|------|
| Schizophrenia | EFO_0000692 | MONDO:0005090 | 35396580 |
| Bipolar Disorder | EFO_0000289 | MONDO:0004985 | 21926972 |
| Major Depressive Disorder | EFO_0001663 | MONDO:0002050 | 29892016 |

### PGC traits to add (EFO IDs)

| Trait | EFO ID | MONDO ID |
|-------|--------|----------|
| ADHD | EFO_0003756 | MONDO:0007977 |
| Alcohol use disorder | EFO_0007589 | MONDO:0002473 |
| Anorexia nervosa | EFO_0000421 | MONDO:0011669 |
| Anxiety disorder | EFO_0004274 | MONDO:0005618 |
| Autism spectrum disorder | EFO_0003756 | MONDO:0005258 |
| Cannabis use disorder | EFO_0009312 | MONDO:0002691 |
| Insomnia | EFO_0004698 | MONDO:0011408 |
| OCD | EFO_0004683 | MONDO:0008758 |
| PTSD | EFO_0001358 | MONDO:0012086 |
| Tourette syndrome | EFO_0004243 | MONDO:0007661 |

---

## graphLD / LDGM

**Repo:** https://github.com/oclb/graphld
**Paper:** Eleanora Lindsey et al. 2024, *graphLD: graph linkage disequilibrium for
scalable genetic analysis*
**Install:** `pip install -e third_party/graphld/` (editable, in-repo)

### Key mathematical concepts

| Symbol | Meaning | Notes |
|--------|---------|-------|
| R | LD correlation matrix | Dense, pairwise SNP correlations |
| Ω = R⁻¹ | LD precision matrix | Sparse — most entries exactly 0 |
| LDGM | Graph encoding of Ω | Only non-zero Ω entries stored as edges |
| graphREML | REML heritability using Ω | Scales linearly with #variants |
| BLUP | Best Linear Unbiased Prediction | Polygenic scores using Ω |

### Why LDGM is sparse (important)
LD matrix R is dense (every SNP correlates with every nearby SNP).
The **inverse** Ω is sparse because of the Markov property: distant SNPs are
conditionally independent given intermediate SNPs. LDGM stores only the edges
where Ω_ij ≠ 0, giving O(n) storage vs O(n²) for R.

### LDGM file format
Each ancestry/chromosome is split into LD blocks. Each block has:
- `{block_id}.edgelist.csv` — columns: `i,j,weight` (non-zero Ω entries)
- `{block_id}.snplist.csv` — columns: `site_ids,position` (SNP metadata)

### DuckDB index schema
```sql
CREATE TABLE ld_blocks (
    block_id       TEXT PRIMARY KEY,
    chromosome     TEXT,
    start_bp       INTEGER,
    end_bp         INTEGER,
    n_snps         INTEGER,
    ancestry       TEXT,
    hancestro      TEXT,
    edgelist_path  TEXT,
    snplist_path   TEXT
);
```

---

## TileDB — Array Storage

**Purpose:** Language-agnostic dense/sparse array storage. Used for:
- TileDB-VCF: multi-sample genotype data
- LDGM TileDB: sparse precision matrices (one array per block)
- Tracks: BigWig signal arrays

**Key rule: Never use NPZ.** NPZ is Python-only. TileDB is readable from R, Julia, C++, and any language.

### TileDB-VCF Arrays (vcf stores)
Location: `tiledb/vcf/`
```
Shahin/snp/     → 1 sample, 47 attrs including GT, DP, GQ, AD
Olivia/snp/     → 1 sample (SNP+INDEL)
Olivia/cnv/     → 1 sample (copy number)
Olivia/sv/      → 1 sample (structural variants)
PEC/snp/        → 218 samples (brainSCOPE WGS cohort)
PEC_RNA/snp/    → 226 samples (RNA-derived imputed genotypes)
```

### LDGM TileDB Arrays
Location: `https://github.com/cytognosis/datasets/tree/main/06-genotype/ldgm/tiledb`
Schema: sparse 2D (row=SNP index i, col=SNP index j) + attribute `weight` (Ω_ij)
One TileDB array per block. DuckDB index (`index.duckdb`) maps block_id → TileDB path.

---

## Hail — Large-Scale Genomic Analysis

**Status:** Research/reference only. Not actively used in Cytos yet.

**Relevance:**
- Pan-UKBB uses Hail VDS (Variant Dataset) format — an alternative to TileDB-VCF
- Hail provides a Spark-based distributed computation framework
- If Pan-UKBB data is ingested, will need Hail→TileDB bridge in `graphld/dense.py`

**Key formats:**
- `MatrixTable` (.mt) — Hail's primary format (Spark-based)
- `VariantDataset` (VDS) — sparse representation for large cohorts
- `BlockMatrix` — for dense LD matrix storage

**Decision:** For LDGM, we use the native graphLD sparse format, not Hail. If Pan-UKBB dense LD
matrices are needed, `graphld/dense.py` provides the Hail bridge.

---

## LinkML — Schema Language

**Purpose:** Source of truth for all Cytos data schemas.
All other formats (JSON-LD, Pydantic, JSON Schema, SHACL, OWL) are generated from LinkML YAML.

**Spec:** https://linkml.io/

### Cytos domain schemas (36 total in `schemas/domains/`)
```
agent, anatomy, annotation, behavior, biothings, cellline, clinical, dataset,
device, disease, drug, environment, evidence, exposure, expression, ga4gh,
gene, genomics, geography, hra, measurement, molecular, network, organism,
pathway, phenotype, population, protein, publication, schema_org, sensor/,
sequence, spatial, taxonomy, trial, variant
```

### `schemas/domains/genomics.yaml` structure
15 classes: `GenomicVariant`, `SNP`, `Insertion`, `Deletion`, `StructuralVariant`,
`CopyNumberVariant`, `Haplotype`, `LDBlock`, `GWASSumstat`, `GWASAssociation`,
`SequenceFeature`, `ChromosomeRegion`, `GenomicRegion`, `PangenomePath`, `EQTLAssociation`

5 enums: `VariantType`, `StrandEnum`, `AncestryEnum`, `EvidenceLevel`, `EffectDirection`

4 types: `ChromosomeAccession`, `RSIdentifier`, `VRSIdentifier`, `GeneID`
