# Neo4j — GenomeKG Graph Database

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: engineers
> **Tags**: `engineering`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

> Running at: `bolt://localhost:7687`
> Auth: `neo4j` / `cytognosis2026`
> Version: Neo4j 2026.04.0

---

## Current Graph State (2026-05-22)

### Node Counts

| Label | Count | Properties | Source |
|-------|-------|-----------|--------|
| `Gene` | 233,878 | gene_id, gene_name, chrom, start_bp, end_bp, gene_type, strand, assembly | GENCODE v47 |
| `Chromosome` | 25 | name (chr1..chrY, chrM), assembly, length_bp, refseq_acc | GRCh38 built-in |
| `Trait` | 3 | name, efo_id, mondo_id, pmid, n_cases, n_controls, n_total, ancestry, source | GWAS Catalog |
| `GWASHit` | 19,621 | rsid, chrom, pos, beta, se, pval, trait, source, dataset_id | GWAS Catalog (p<5e-8) |
| `Variant` | **0** | rsid, chrom, pos, ref, alt, vrs_id, so_term | ❌ Not loaded (seqrepo needed) |

Plus pre-existing biomedical KG: ~10.7M nodes (Disease, Gene, Protein, Drug, etc.)

### Edge Counts

| Relationship | Count | From → To | Notes |
|-------------|-------|-----------|-------|
| `LOCATED_ON` | 78,687 | Gene → Chromosome | GENCODE v47 |
| `NEAR_GENE` | 795,297 | GWASHit → Gene | ±500kb window |
| `ASSOCIATED_WITH` | 19,868 | GWASHit → Trait | All GWS hits |
| `TRANSCRIBES` | (many) | Transcript → Gene | GENCODE |
| `PART_OF` | (many) | Exon → Transcript | GENCODE |

### Indexes and Constraints

```cypher
SHOW INDEXES;
-- gene_id_unique (UNIQUE on Gene.gene_id)
-- transcript_id_unique (UNIQUE on Transcript.transcript_id)
-- trait_efo (UNIQUE on Trait.efo_id)
-- trait_name (INDEX on Trait.name)
-- gwas_hit_rsid (INDEX on GWASHit.rsid)
-- gwas_hit_chrom_pos (INDEX on GWASHit.chrom, GWASHit.pos)
-- gwas_hit_pos (INDEX on GWASHit.chrom, GWASHit.pos)
```

---

## Key Queries

```cypher
-- Count nodes by label
MATCH (n) RETURN labels(n)[0] as label, count(n) as count ORDER BY count DESC LIMIT 20;

-- SCZ GWAS hits near TBX1 gene
MATCH (h:GWASHit)-[:ASSOCIATED_WITH]->(t:Trait {name: 'Schizophrenia'})
MATCH (h)-[:NEAR_GENE]->(g:Gene {gene_name: 'TBX1'})
RETURN h.rsid, h.chrom, h.pos, h.pval, h.beta ORDER BY h.pval;

-- All traits and hit counts
MATCH (t:Trait)
OPTIONAL MATCH (h:GWASHit)-[:ASSOCIATED_WITH]->(t)
RETURN t.name, t.efo_id, count(h) as hits ORDER BY hits DESC;

-- Genes with most GWAS hits nearby (MDD)
MATCH (h:GWASHit)-[:ASSOCIATED_WITH]->(t:Trait {name: 'Major Depressive Disorder'})
MATCH (h)-[:NEAR_GENE]->(g:Gene)
RETURN g.gene_name, count(h) as n_hits ORDER BY n_hits DESC LIMIT 20;

-- GENCODE genes on chr22 with coordinates
MATCH (g:Gene)-[:LOCATED_ON]->(c:Chromosome {name: 'chr22'})
WHERE g.gene_id IS NOT NULL
RETURN g.gene_name, g.start_bp, g.end_bp
ORDER BY g.start_bp LIMIT 10;
```

---

## Loading Scripts

| Script | What it loads | Status |
|--------|--------------|--------|
| `src/cytos/genomics/reference.py:reference_to_neo4j()` | GRCh38 chromosomes | ✅ done |
| `src/cytos/genomics/reference.py:load_gencode_to_neo4j()` | GENCODE v47 genes | ✅ done |
| `scripts/ingest_gwas_neo4j.py` | GWAS Catalog traits + hits | ✅ done (3 traits) |
| `src/cytos/genomics/so.py:so_to_neo4j()` | SO term nodes | ⬜ not yet run |
| TBD — Variant loader | SNP Variant nodes from TileDB-VCF | ❌ blocked (seqrepo) |

---

## Connecting from Python

```python
import os
os.environ.setdefault("NEO4J_PASSWORD", "cytognosis2026")

from cytos.db.neo4j.client import get_driver
driver = get_driver()

with driver.session() as session:
    result = session.run("MATCH (t:Trait) RETURN t.name, t.efo_id")
    for row in result:
        print(row["t.name"], row["t.efo_id"])
```

**Environment variables:**
```bash
NEO4J_URI=bolt://localhost:7687
NEO4J_USER=neo4j
NEO4J_PASSWORD=cytognosis2026
```

---

## Planned Additions

1. **Variant nodes** (seqrepo dependency) — SNP nodes with VRS IDs
2. **SO term nodes** — Sequence Ontology class hierarchy
3. **PGC trait nodes** — 14 additional psychiatric GWAS traits
4. **eQTL edges** — `(Variant)-[:REGULATES]->(Gene)` from GTEx/PEC
5. **Haplotype nodes** — common haplotype blocks
