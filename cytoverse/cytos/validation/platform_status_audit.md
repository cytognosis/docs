# Cytos Platform Status Audit

> **Date**: 2026-05-14 | **Audited by**: Codebase inspection

---

## 1. Semantic Knowledge Graph

### Status: ⚠️ Data Exported, Not Loaded into Neo4j

| Metric | Value |
|--------|-------|
| **KG data on disk** | 25 GB |
| **Neo4j nodes CSV** | 10.2M rows (9.7M + 0.5M in exports) |
| **Neo4j edges CSV** | 77.9M rows (60.1M + 17.8M in exports) |
| **Ontology validation enums** | 6 files (CL, EFO, HANCESTRO, MONDO, PATO, UBERON) |
| **SSSOM mappings** | `consolidated.sssom.tsv` (14 MB) |
| **HRA spatial data** | `hra_spatial_placements.parquet` (100 KB) |
| **Neo4j server** | **Not running**. Binary not in PATH. No database directory found. |

### What's Done
- Ontology validation enums generated from OBO sources (CL, EFO, HANCESTRO, MONDO, PATO, UBERON)
- KG node/edge CSVs generated in Neo4j import format (88M total rows)
- SSSOM cross-ontology mappings consolidated
- HRA spatial placements ingested
- `convert_to_neo4j.py` pipeline exists in `pipelines/data_engineering/`
- Neo4j Python driver installed (`neo4j 5.28.4`, `neo4j-graphrag 1.8.0`)

### What's Missing
- **Neo4j 5.x not installed or configured** as a service/container
- CSV data **never imported** into a running Neo4j instance
- No Neo4j schema constraints, indexes, or APOC procedures configured
- No validation that the 88M rows are self-consistent and load cleanly
- Two separate CSV exports (neo4j/ and exports/) may be duplicates or different versions
- Missing ontologies: GO (Gene Ontology), ChEBI, SO (Sequence Ontology), NCBITaxon

---

## 2. Observational Knowledge Graph

### Status: ⚠️ Schemas Defined, No Data Ingested

| Metric | Value |
|--------|-------|
| **Domain LinkML schemas** | 33 files |
| **Total schema lines** | ~175K (mostly ontology enums) |
| **Domain-specific schemas** | anatomy, annotation, behavior, biothings, cellline, clinical, dataset, device, disease, drug, environment, evidence, exposure, expression, ga4gh, gene, geography, hra, information, measurement, nwb, pathway, person, phenotype, population, publication, scholarly, semantic_network, sensor, taxonomy, topic, variant |
| **Schema format** | LinkML (all converted) ✅ |
| **Ingestion adapters** | biothings, cellxgene, ga4gh, nwb, ontology, openalex, opentargets, schema_org, sosa, umls |
| **Data ingested** | **Zero** (adapters exist but no processed output) |

### What's Done
- All 33 domain schemas converted to LinkML ✅
- Cross-domain alignment module (`kg_align.py`) exists
- 10 LinkML-ization adapters written (biothings, cellxgene, ga4gh, nwb, etc.)
- Parsers for BibTeX, HDMF, JSON Schema, OWL, Parquet, RDF, RRF formats
- UMLS vocabulary processor exists

### What's Missing
- **No harmonization test run** across all adapters with a shared schema
- Edge/relationship schemas not documented (only node schemas exist)
- No consolidated "run all ingestion" pipeline
- No validation that adapter outputs conform to domain schemas
- Person/scholarly schemas updated this session but others untouched since May 11-12

---

## 3. Genomics & Neuroimaging Pipeline

### Status: ❌ Schema Only, No Data Pipeline

| Component | Status |
|-----------|--------|
| `variant.yaml` schema | ✅ Exists (GA4GH VRS 2.x aligned) |
| `ga4gh.yaml` schema | ✅ Exists (VRS, Phenopackets, Beacon) |
| `nwb.yaml` schema | ✅ Exists (NWB 2.x neuroimaging) |
| `gene.yaml` schema | ✅ Exists |
| GWAS summary stats ingestion | ❌ **No code exists** |
| WGS data ingestion | ❌ **No code exists** |
| PGC download functions | ❌ **No code exists** |
| GWAS Catalog API functions | ❌ **No code exists** |
| Pan-UKBB download/ingest | ❌ **No code exists** |
| TileDB-VCF storage | ❌ **Installed** (`tiledbvcf 0.40.3`) but **no integration code** |
| Liftover/munging pipeline | ❌ **No code exists** |
| 14 psychiatric GWAS from Nature paper | ❌ **Not downloaded** |

### What's Done
- LinkML schemas for variants (VRS), GA4GH entities, NWB, and genes
- TileDB ecosystem installed: `tiledb 0.36.2`, `tiledbvcf 0.40.3`, `tiledbsoma 2.1.0`
- Schema imports properly chain through `core.yaml`

### What's Missing (Critical)
- **Entire GWAS ingestion pipeline**: No functions to download from PGC, GWAS Catalog, or Pan-UKBB
- **No liftover/munging**: No hg19→hg38 liftover, allele harmonization, or strand alignment
- **No TileDB-VCF writer**: Package installed but zero integration code
- **No WGS/summary stats parser**: No code to parse .vcf.gz, .tsv.gz, or LDSC-format files
- **No download orchestrator**: No code to map KG identifiers → download URLs → fetch → process
- **14 psychiatric GWAS datasets**: Not downloaded, not referenced anywhere in data/

---

## 4. GraphLD

### Status: ⚠️ In-Housed, Partially Configured

| Metric | Value |
|--------|-------|
| **Location** | `third_party/graphld/` |
| **Source code** | 24 Python files, 8,486 total lines |
| **Tests** | 20 test files (cli, simulate, heritability, io, clumping, etc.) |
| **LDGM data** | `metadata.csv` only (972 KB) |
| **Full LDGM precision matrices** | ❌ **Not downloaded** |
| **Data directory** | 26 MB total |

### What's Done
- GraphLD repository fully in-housed under `third_party/graphld/`
- Source code present: simulation, heritability estimation, clumping, score tests, VCF I/O
- LDGM metadata CSV downloaded (maps populations/chromosomes to matrix files)
- Test suite present (20 test files)

### What's Missing
- **LDGM precision matrices not downloaded**: Only the metadata.csv is present. The actual sparse precision matrices (estimated ~50-100 GB for all populations × chromosomes) have not been fetched.
- **Functions not adapted to Cytos formats**: GraphLD reads its own data formats; no bridge code maps between Cytos KG variant schema and GraphLD's internal structures
- **No integration tests**: Tests reference GraphLD's own test data, not Cytos data
- **pyproject.toml not integrated**: GraphLD's dependencies not merged into Cytos's dep graph

---

## 5. BioCypher

### Status: ❌ Scaffolded, Not Functional

| Metric | Value |
|--------|-------|
| **Installed** | `biocypher 0.13.4` ✅ |
| **Bridge adapter** | `biocypher_bridge.py` (172 lines) |
| **BioCypher adapters dir** | Empty (`__init__.py` only, 0 bytes) |
| **BioCypher KG module** | `src/cytos/kg/biocypher/` (scaffold only) |
| **Ontology config** | ❌ No `schema_config.yaml` |
| **Tested sources** | ❌ Zero |
| **Export formats tested** | ❌ Zero |

### What's Done
- BioCypher package installed
- Bridge adapter file exists (172 lines) linking BioCypher to Cytos ingest
- Directory structure scaffolded (`kg/biocypher/adapters/`)

### What's Missing
- **No BioCypher adapters**: The adapters directory is empty (only empty `__init__.py`)
- **No `schema_config.yaml`**: BioCypher requires a YAML ontology config mapping; none exists
- **No ingestion tested**: Zero data sources ingested through BioCypher
- **No export tested**: Neo4j, PostgreSQL, or CSV export not configured or tested
- **Bridge adapter untested**: The 172-line bridge has not been validated against real data

---

## Prioritized Next Steps

Based on the audit, here's the critical path ranked by impact and dependency order:

### P0: Infrastructure Blockers (Must unblock everything else)

| # | Task | Effort | Why Critical |
|---|------|--------|-------------|
| 1 | **Install and configure Neo4j 5.x** (Docker or APT) | 1 hr | All KG queries depend on this |
| 2 | **Import the 88M-row CSV into Neo4j** | 2-4 hr | Validates the entire semantic KG pipeline |
| 3 | **Download LDGM precision matrices** for GraphLD | 2-4 hr | Required before any LD-based analysis |

### P1: Genomics Pipeline (Highest value, zero code exists)

| # | Task | Effort | Why Critical |
|---|------|--------|-------------|
| 4 | **GWAS summary stats ingestion pipeline** (download → parse → harmonize → store) | 8 hr | Core research capability |
| 5 | **PGC/GWAS Catalog/Pan-UKBB download functions** with KG identifier mapping | 6 hr | Data access for psychiatric genomics |
| 6 | **Liftover + allele harmonization** (hg19→hg38, strand flip, A1/A2 normalization) | 4 hr | Prerequisite for any cross-study analysis |
| 7 | **TileDB-VCF writer** for ingested variants | 4 hr | Scalable storage for WGS + summary stats |
| 8 | **Download + ingest 14 psychiatric GWAS** from the Nature paper | 4 hr | First validation of the full pipeline |

### P2: KG Consolidation

| # | Task | Effort | Why Critical |
|---|------|--------|-------------|
| 9 | **Run all 10 LinkML adapters** and validate output against schemas | 4 hr | Proves observational KG pipeline works |
| 10 | **Harmonize edge schemas** (relationships not documented) | 3 hr | Nodes without edges are useless |
| 11 | **GraphLD ↔ Cytos bridge** (variant schema mapping, data format conversion) | 4 hr | Enables LD-aware analyses |
| 12 | **BioCypher schema_config.yaml** + first working adapter | 3 hr | Enables multi-format export |

### P3: Polish and Scale

| # | Task | Effort | Dependencies |
|---|------|--------|-------------|
| 13 | Missing ontologies (GO, ChEBI, SO, NCBITaxon) | 2 hr | Neo4j running |
| 14 | BioCypher multi-source ingestion tests | 4 hr | Item 12 |
| 15 | Pan-UKBB full download orchestration | 8 hr | Items 4-7 |
| 16 | Module specs for all genomics/KG modules | 4 hr | Implementation stable |

---

## Bottom Line

The project has strong **schema infrastructure** (33 LinkML schemas, ontology enums, SSSOM mappings) and **scholarly pipeline** (fully functional), but the **data infrastructure gap is critical**:

- 88M rows of KG data sit in CSV files with **no running Neo4j to query them**
- The entire genomics pipeline (GWAS, PGC, Pan-UKBB, TileDB-VCF) is **schemas only, zero code**
- GraphLD is in-housed but the **LDGM data that makes it useful is not downloaded**
- BioCypher is **installed but non-functional** (empty adapters, no config)

The recommended sequence is: **Neo4j up → GWAS pipeline → GraphLD data → BioCypher adapters**.
