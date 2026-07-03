> [!WARNING]
> **Status:** SUPERSEDED · **Date:** 2026-07-01 · Superseded by [architecture.md](../architecture.md).
> Byte-identical to architecture-overview-v2.md; both are v3.0, superseded by architecture.md v4.0. Archived by the Cytos consolidation (`reorg/cytos-2026-07-01`). Retained for history; do not edit.

---

# Cytos Architecture Overview

> v3.0 — Data-only KG construction and genomic infrastructure layer.
> Last updated: 2026-05-22

---

## What Cytos Is (and Is Not)

**Cytos IS:**
- The genomic data ingestion and KG construction layer for Cytognosis
- A multi-backend Knowledge Graph builder (Neo4j + SurrealDB)
- A statistical genetics toolkit (LDGM, graphLD, GWAS pipeline)
- A schema system (LinkML → multi-format generation)
- A scholarly intelligence pipeline

**Cytos IS NOT:**
- A machine learning training framework (stubs only; deferred to v2.x)
- A user-facing application (consumed by Cytoverse, Cytoscope, Cytonome)
- A microservice (it's a Python library + CLI)

---

## Platform Position

```
Cytognosis Platform
├── Cytoverse (The Map)      ← consumes cytos KG
├── Cytoscope (The Sensor)   ← consumes cytos sensor schemas
├── Cytonome (The Navigator) ← consumes cytos embeddings
└── Cytos (The Substrate)    ← THIS PACKAGE
    ├── GenomeKG
    ├── Scholarly KG
    ├── Biomedical KG
    └── Schema System
```

---

## Three Constituent Graphs

Cytos builds a unified biomedical KG composed of three constituent subgraphs:

### 1. Ontology Graph (OG)
Definitional relationships: is_a, part_of, has_part.
Sources: UMLS, SNOMED, 37 OBO ontologies, HRA CCF, UniChem, Ensembl.
Neo4j label examples: Disease, Gene, Protein, ChemicalEntity, AnatomicalEntity.

### 2. Catalog Graph (CG)
Publication and artifact metadata.
Sources: PKG2.0 (scholarly), PlaNet (clinical trials).
Neo4j label examples: Publication, ClinicalTrial, InformationContentEntity.

### 3. Observation Graph (ObG)
Measured associations (experimental evidence).
Sources: Monarch, PrimeKG, Open Targets, GWASHit associations.
Neo4j label examples: GWASHit, Trait (via ASSOCIATED_WITH).

### New: GenomeKG (added May 2026)
Genomic coordinates and variant associations. Overlaid on OG.
Neo4j labels: Gene (extended), Chromosome, GWASHit, Trait, Variant (planned).

---

## System Architecture Diagram

```
External Sources                  Cytos Pipeline                  Outputs
─────────────────                 ──────────────                  ───────
UMLS, SNOMED, OBO    ──► ingest/ ──► kg/ ──► KGX TSV ──► Neo4j 2026.04.0
Monarch, PrimeKG, OT                                   ──► SurrealDB
Scholarly papers     ──► scholarly/                    ──► DVC artifacts
                                                        ──► RO-Crate

GWAS Catalog/PGC     ──► gwas.py  ──► Neo4j GWASHit
GENCODE v47 GTF      ──► reference.py ──► Neo4j Gene + Chromosome
Personal WGS VCF     ──► vcf.py   ──► TileDB-VCF stores
PEC cohort VCF       ──► vcf.py   ──► TileDB-VCF stores
LDGM edgelists       ──► ldgm.py  ──► TileDB sparse Ω arrays + DuckDB

LinkML YAML          ──► schema/  ──► JSON-LD, Pydantic, JSON Schema, SHACL
```

---

## Pipeline Stack

| Layer | Tool | Purpose |
|-------|------|---------|
| Pipeline framework | Kedro | Data catalog + DAG + node composition |
| Data versioning | DVC | Large artifact tracking (dvc.yaml, 10 stages) |
| Experiment tracking | MLflow | Training runs (future use) |
| Orchestration | Dagster | Production scheduling (kedro-dagster) |
| Graph DB (primary) | Neo4j 2026.04.0 | Biomedical KG + GenomeKG |
| Graph DB (secondary) | SurrealDB | Document+graph for clinical/sensor data |
| Array storage | TileDB | VCF genotypes + LDGM precision matrices |
| Local analytics | DuckDB | LDGM block index + KGBuilder intermediate |
| Schema language | LinkML | Source of truth for all data models |

---

## Key Data Flows

### VCF Ingestion Flow
```
Raw VCF → tiledbvcf.Dataset.create_sample() → TileDB-VCF array
                                                     │
                                             query by region/sample
                                                     │
                                         vrs.py → VRS Allele ID
                                                     │
                                         Neo4j Variant node (pending seqrepo)
```

### GWAS Flow
```
GWAS TSV → load_gwas_ssf() → polars DataFrame
               │ auto-detect: GWAS-SSF / harmonized / PGC minimal
               ▼
filter p < 5e-8 → GWASHit rows
               ▼
Neo4j: CREATE GWASHit, Trait → NEAR_GENE links to Gene (±500kb)
```

### LDGM Flow
```
graphLD edgelist + snplist files
               ▼
ldgm.py:ingest_edgelist() → TileDB sparse Ω array
ldgm.py:build_block_index() → DuckDB ld_blocks table
               ▼
interface.py:load_block_precision(block_id) → PrecisionOperator
               ▼
interface.py:align_block_sumstats() → aligned z-scores
               ▼
interface.py:run_graphreml() → heritability estimate
```

---

## All Settled Architecture Decisions

See `docs/architecture/DECISIONS.md` for full detail. Key decisions:

1. **No NPZ** — TileDB for all array storage (language-agnostic)
2. **Data-only scope** — ML models are external consumers; modeling stubs deferred
3. **LinkML as schema truth** — all formats generated, never hand-written
4. **Neo4j owns genomics graph** — SurrealDB for clinical/sensor
5. **graphLD sparse format** — Ω precision matrices, not dense R matrices
6. **GWAS-SSF 1.0 standard** — with auto-detection of PGC/harmonized variants
7. **VRS 2.0 IDs** — for all Variant nodes (requires seqrepo)
8. **HANCESTRO for ancestry** — standardized population labels in LDGM index

---

## Dependency Groups (pyproject.toml)

```toml
[project.optional-dependencies]
genomics = ["tiledb", "tiledbvcf", "duckdb", "graphld", "pysam", "pronto", "networkx"]
ga4gh = ["ga4gh-vrs[extras]", "biocommons.seqrepo"]
graphld = ["graphld @ git+https://github.com/oclb/graphld.git", "scikit-sparse>=0.4"]
vcf = ["tiledbvcf>=0.28"]
schemas = ["linkml>=1.7", "linkml-runtime"]
kg_neo4j = ["neo4j>=5.0"]
kg_surreal = ["surrealdb>=1.0"]
scholarly = ["docling", "marker-pdf", "scispacy", "spacy"]
```
