> [!WARNING]
> **Status:** SUPERSEDED · **Date:** 2026-07-01 · Superseded by [module-map.md](../module-map.md).
> Byte-identical duplicate of module-map.md; module-map.md kept as canonical. Archived by the Cytos consolidation (`reorg/cytos-2026-07-01`). Retained for history; do not edit.

---

# Cytos Module Map

> All `src/cytos/` Python modules, status, and purpose.
> Last audited: 2026-05-22 | Total files: ~170

---

## Status Key
- ✅ Production — tested, committed
- ⚠️ Partial — code exists, gaps noted
- 🔧 Stub — scaffold only, not implemented
- ❌ Deleted — removed in v3 cleanup

---

## `genomics/` — Primary recent work

| Module | Status | Purpose |
|--------|--------|---------|
| `vcf.py` | ✅ | TileDB-VCF wrapper + CRAM functions (open_cram, fetch_reads, cram_coverage, validate_tbx1_insertion) |
| `vrs.py` | ⚠️ | VRS 2.0 Allele/CNV/Adjacency; seqrepo integration blocked |
| `reference.py` | ✅ | GRCh38 chromosome table, GENCODE GTF parser, Neo4j loader |
| `so.py` | ✅ | SO OBO loading (with upstream bug sanitizer), hierarchy queries, Neo4j ingestion |
| `haplotype.py` | ✅ | Phased haplotype storage, KG bridge |
| `regions.py` | ✅ | GenomicRegion CRUD, BED/GFF3/GTF importers |
| `tracks.py` | ✅ | BigWig → TileDB ingestion + positional query |
| `eqtl.py` | ✅ | GTEx + PsychENCODE eQTL loaders; cis-eQTL KG bridge |
| `gwas.py` | ✅ | GWAS-SSF 1.0 + harmonized + PGC format auto-detection; Neo4j writer |
| `pangenome.py` | ✅ | GFA 1.0/2.0 parser, haplotype path representation |
| `phenopacket.py` | ✅ | Phenopackets v2 + PED → KG bridge |
| `munge.py` | ✅ pre-existing | GWAS sumstat munging |
| `sources.py` | ✅ pre-existing | GWAS/genomics source registry |
| `ingest.py` | ✅ pre-existing | Data ingestion orchestration |
| `io.py` | ✅ pre-existing | File I/O utilities |
| `annotate.py` | ✅ pre-existing | Variant annotation |
| `liftover.py` | ✅ pre-existing | hg19→hg38 liftover |
| `regulatory.py` | ✅ pre-existing | Regulatory region annotation |
| `join.py` | ✅ pre-existing | Dataset joining utilities |
| `prs.py` | ✅ pre-existing | Polygenic risk score computation |
| `graphld_bridge.py` | ⚠️ legacy | Original LDGM bridge (predates graphld/ submodule) |
| `graphld/__init__.py` | ✅ | Exports all graphld interface functions |
| `graphld/ldgm.py` | ✅ | LDGM TileDB sparse ingestion + DuckDB indexing |
| `graphld/dense.py` | ✅ | Pan-UKBB dense LD covariance (Hail bridge) |
| `graphld/analysis.py` | ✅ | GWAS-LDGM alignment (align_ldgm_to_sumstats) |
| `graphld/interface.py` | ✅ | Native graphLD library bridge (load_block_precision, align_block_sumstats, run_graphreml, compute_blup_scores) |

---

## `db/` — Database Clients

| Module | Status | Purpose |
|--------|--------|---------|
| `db/__init__.py` | ✅ | Factory: `connect(backend)` |
| `db/neo4j/__init__.py` | ✅ | |
| `db/neo4j/client.py` | ✅ | get_driver() singleton; env: NEO4J_URI/USER/PASSWORD |
| `db/neo4j/convert_to_neo4j.py` | ⚠️ | KGX TSV → Neo4j bulk loader |
| `db/surrealdb/client.py` | ⚠️ | **Bug: missing async context manager** (__aenter__/__aexit__) |
| `db/surrealdb/schema.py` | 🔧 | LinkML → SurrealQL transpiler (not implemented) |
| `db/surrealdb/converter.py` | ⚠️ | KGX → SurrealDB writer |
| `db/surrealdb/query.py` | ⚠️ | Graph query helpers |

---

## `schema/` — Schema System

| Module | Status | Purpose |
|--------|--------|---------|
| `schema/export.py` | ⚠️ | export_schema(), export_all(), push_to_cytoskeleton() — **push pipeline partial** |
| `schema/generator.py` | ❌ missing | **NOT IMPLEMENTED** — planned SchemaGenerator class |
| `schema/__init__.py` | ✅ | |
| `schema/bridges/__init__.py` | ✅ | |
| `schema/generated/genomics.py` | ✅ | Pydantic v2 datamodels for genomics domain (15 classes) |

---

## `scholarly/` — Academic Intelligence (30 modules, pre-existing + recent additions)

Full pipeline: PDF parsing (Docling/Marker/Surya/PyMuPDF/Grobid), scispaCy NER,
author identity/profiling, OpenAlex/Semantic Scholar/ORCID/Zotero APIs,
citation graph, paper profiling, KG integration.

**Recent Additions (Grants & Compilation):**
- `scholarly/compiler.py` (✅) — Pandoc/Quarto markdown-to-PDF/Word compilation interface.
- `scholarly/grants/` (✅) — Grant opportunity ingestion.
  - `parser.py` (✅) — Unified parser for PyMuPDF, `python-docx`, and `openpyxl`. Extracts text, tables, and CriticMarkup highlights.
  - `llm_extraction.py` (✅) — Instructor/Pydantic structured extraction wrapper (Ollama/OpenAI compatible).
  - `harmonizer.py` (✅) — Funder-specific schema (NSF, ARPA-H) mapping into canonical Proposal slots.
  - `generator.py` (✅) — Jinja2 template rendering for standardized Funder proposals.
  - `schemas/` and `templates/` (✅) — YAML declarative schemas and pure Markdown templates for `nsf_xlabs` and `arpah_solution_summary`.

## `kg/` — Knowledge Graph Builder (pre-existing)

DuckDB-based KGBuilder: 860 LOC. Builds KGX TSV from all sources.
`store.py`, `mapper.py`, `reclassify.py`, `semantic_overlay.py`, etc.

---

## `ontology/` — Ontology Manager (pre-existing)

`registry.py`, `fetcher.py`, `validator.py`, `cli.py`
Full CLI: `cytos ontology fetch/validate/reason/convert`

---

## `publish/` — Asset Publishing (pre-existing)

`asset_pipeline.py` — CSO ontology distribution
`rocrate.py` — RO-Crate provenance packaging

---

## `pipelines/` — Orchestration (pre-existing + modified)

Dagster definitions, Kedro data engineering pipeline.
`dagster_definitions.py` — modified (tracked as unstaged change)

---

## Stubs (Deferred to v2.x)

These exist as `__init__.py` stubs only. Not to be implemented in current phase.

| Package | Deferred capability |
|---------|-------------------|
| `features/` | Per-modality feature extraction |
| `models/` | Encoder, fusion, kg_embed architectures |
| `train/` | Lightning + JAX trainers |
| `evaluate/` | Integration, fairness, robustness metrics |
| `rag/` | Graph-RAG inference |

---

## Services (pre-existing)

| Module | Purpose |
|--------|---------|
| `services/cellxgene.py` | CellxGene API client |
| `services/hra.py` | Human Reference Atlas client |
| `services/ontology_mapper.py` | OLS4 + BioPortal mapping |
| `services/rest_apis.py` | Generic REST client |
| `services/single_cell.py` | scRNA-seq data access |
