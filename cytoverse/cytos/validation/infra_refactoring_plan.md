# Infrastructure Refactoring Session Report

> 2026-05-12 | Phases completed: Neo4j, Git, Schema Mapping, Pipeline Setup

---

## ✅ Completed

### 1. Neo4j Cleanup & Fresh Install

| Action | Details |
|--------|---------|
| Old versions removed | 3.5.35, 4.4.40 (OLS4), 2025.03.0 (old KG) — freed **264GB** |
| New install | **Neo4j 2026.04.0** Community (latest stable) |
| Config | 8GB heap, 16GB pagecache, auth disabled, bolt:7687, http:7474 |
| KG loaded | **9,225,808 nodes, 52,399,886 relationships** (2m 10s import) |
| Database size | 6.7GB on disk |
| Disk freed | From 100% → 70% (1.1TB free) |

### 2. Git Commits (3 commits)

```
ec79722 feat: add Dagster pipeline definitions for KG build
5346dea feat: add Neo4j converter, BibTeX IO, and DVC pipeline stages
6702cbd feat: add KG schemas, DVC pipeline, and data engineering scripts
```

### 3. External KG Schema Mapping (6 KGs)

All mapped to BioLink, exported as independent artifacts. NOT imported yet.

| KG | Nodes | Edges | Compatibility | Key Types |
|----|------:|------:|--------------|-----------|
| PrimeKG | - | 8.1M | HIGH | 10 entity, 30 relation types |
| Monarch | 1.38M | 15.36M | PERFECT | Native BioLink/KGX |
| PheKnowLator | - | ~156GB RDF | HIGH | Gene, Protein, Variant, Chemical |
| PlaNet | - | 240M triples | MEDIUM | 26 relation types (UMLS/MeSH) |
| CKG | - | ~50+ types | HIGH | 26 node, 35+ edge types (proteomics) |
| Open Targets | - | 23GB Parquet | HIGH | Target, Disease, Drug, Evidence |

Full details: [external_kg_schema_mapping.md](file:///home/mohammadi/.gemini/antigravity/brain/cd6537fc-9f66-43c5-80fd-f9d2c8fe6893/artifacts/external_kg_schema_mapping.md)

### 4. Pipeline Infrastructure

| Component | Status |
|-----------|--------|
| **Dagster** | Installed, 5 assets defined (quality, ingest, scholarly, export) |
| **DVC** | Tracking `data/kg/*.tsv` with sidecar `.dvc` files |
| **RO-Crate** | `ro-crate-metadata.json` for provenance |
| **Neo4j** | 2026.04.0 with `cytos` database loaded |

### 5. Topic Area Evaluation

| Ontology | Decision | Use Case |
|----------|----------|----------|
| AIO (AI Ontology) | ✅ Import | ML model annotation |
| CSO 3.5 (CS Ontology) | ✅ Import | Paper topic annotation |
| ROADMAP | ✅ Import | Project/investigation topics |
| NCIT | ⚠️ Skip | Already in KG via UMLS |
| Annett-O | ❌ Skip | Too narrow |

### 6. Data Organization Proposal

Full proposal: [data_lake_organization.md](file:///home/mohammadi/.gemini/antigravity/brain/cd6537fc-9f66-43c5-80fd-f9d2c8fe6893/artifacts/data_lake_organization.md)

---

## Pipeline Scripts (Production-ready)

| Script | Purpose | Status |
|--------|---------|--------|
| [convert_to_neo4j.py](file:///home/mohammadi/repos/cytognosis/cytos/src/cytos/pipelines/data_engineering/convert_to_neo4j.py) | KGX→Neo4j CSV | ✅ CLI + logging |
| [bibtex_io.py](file:///home/mohammadi/repos/cytognosis/cytos/src/cytos/pipelines/data_engineering/bibtex_io.py) | BibTeX import/export | ✅ CLI |
| [parse_uniprot.py](file:///home/mohammadi/repos/cytognosis/cytos/src/cytos/pipelines/data_engineering/parse_uniprot.py) | UniProt XML→KGX | ✅ SAX streaming |
| [dagster_definitions.py](file:///home/mohammadi/repos/cytognosis/cytos/src/cytos/pipelines/dagster_definitions.py) | Dagster pipeline | ✅ 5 assets, 3 jobs |

---

## ⬜ Remaining Work (Priority Order)

### P0: Data Organization ✅ COMPLETED

- [x] Execute data lake restructuring (13 numbered directories, symlink-based migration)
- [x] Update all path references in `params.yaml` (canonical 0X-prefixed paths)
- [x] Initialize DVC tracking for datasets directory
- [x] Create data lake README.md with structure documentation
- [x] Backward-compatible symlinks verified for all 9 legacy paths

### P1: External KG Ingestion
- [ ] Ingest Monarch KG (already in KGX format, direct merge)
- [ ] Parse PrimeKG CSV to KGX
- [ ] Parse PlaNet entity dictionary to KGX
- [ ] Clone + parse CKG
- [ ] Parse Open Targets Parquet to KGX

### P2: Schema Finalization
- [ ] Compare all entity/relationship types across 6 KGs
- [ ] Identify gaps in Cytos LinkML schema
- [ ] Iterate schema until all KGs map cleanly
- [ ] Add License type to each ingested source

### P3: Identifier Standardization
- [ ] Update UniChem database
- [ ] Build Ensembl → HGNC → NCBI Gene → UniProt ID mapping table
- [ ] Build PubChem CID → CHEBI → DrugBank mapping table
- [ ] Add SMILES support for chemical entities

### P4: Pipeline Robustification
- [ ] Add tests for all pipeline scripts (pytest)
- [ ] Add type hints to all modules (mypy)
- [ ] Set up Dagster webserver as containerized service
- [ ] Add GCS remote for DVC

### P5: Topic Areas + Scholarly KG Enhancement
- [ ] Ingest AIO, CSO 3.5, ROADMAP as ontology nodes
- [ ] Link to Paper nodes via topic annotations
- [ ] Add OpenAlex metadata to scholarly KG

### P6: Variant Pipeline (Phase E)
- [ ] VRS schema implementation
- [ ] Pan-UKBB GWAS catalog ingestion
- [ ] PsychENCODE genotype harmonization

### P7: Neuro-specific (Phase K)
- [ ] BIDS/NWB schema integration
- [ ] NeuroKG integration
