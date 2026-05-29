# Cytos Roadmap

> Last updated: 2026-05-12 | KG: **10.7M nodes × 118.5M edges**

## Completed Phases

### P0: Foundation (✅ Complete)
- UMLS 2026AA RRF ingestion (8.7M nodes, 43.3M edges)
- SNOMED CT INT+US RF2 parsing
- 37 OBO/OWL ontologies via Pronto pipeline
- UniProt XML streaming (868K proteins)
- DuckDB-based KGBuilder
- KGX TSV format
- BioLink Model category mapping (53 categories)

### P1: External KG Integration (✅ Complete)
- Monarch Initiative (1.38M nodes, 15.4M edges)
- PrimeKG (129K nodes, 8.1M edges)
- Open Targets Platform 25.03 (125K nodes, 466K edges)
- PKG2.0 scholarly layer (1.48M nodes, 34.6M edges)
- PlaNet clinical trial layer (185K nodes, 3.77M edges)
- UniChem chemical cross-references (10M edges)
- Ensembl release 115 gene ID mappings (1.65M edges)
- Monarch SSSOM mappings (1.26M edges)
- Topic areas (AIO+CSO+ROADMAP, 15.7K nodes)

### P1b: Infrastructure (✅ Complete)
- Neo4j 2026.04.0 deployment (80.7M relationships)
- DVC pipeline (10 stages)
- Dagster orchestration (5 assets, 3 jobs)
- RO-Crate provenance (9 sources, 17 artifacts)
- pytest integrity suite (33/33 passing)
- Data lake organization (13 canonical directories)

### P1c: HRA Integration (✅ Complete)
- CCF Ontology ingestion (9,493 nodes, 26,444 edges)
- 3,481 spatial placements (3D coordinates)
- 41 organ ASCT+B tables
- SpatialEntity and SpatialPlacement schemas

## Current: P2 — Semantic Infrastructure (🔄 In Progress)

### P2a: Architecture (✅ Designed)
- Three Constituent Graphs: Ontology Graph, Catalog Graph, Observation Graph
- Sensor → Assay → Schema → Location model (Cytoscope backbone)
- FAIR Data Access Layer (metadata vs. data separation)
- Interaction Taxonomy (MI ontology alignment)
- Classification Layer (UMLS STN, BioLink, MeSH)
- Entity type audit and reclassification plan

### P2b: Data Lake Cleanup (⬜ Phase A)
- Archive legacy ontology directories
- Create flat `owl/` + `mappings/` structure
- Build `registry.yaml` (single source of truth for 50+ resources)

### P2c: Entity Reclassification (⬜ Phase C)
- Reclassify NamedThing (297K → <50K)
- Reclassify InformationContentEntity (598K → <180K)
- Split/rename: Agent→Organization, IndividualOrganism→OccupationalRole, Behavior→NeurobehavioralPhenotype

### P2d: Schema Implementation (⬜ Phase D)
- 8 new schemas: cellline, device, behavior, exposure, geography, measurement, population, agent
- 4 updated schemas: clinical (OMOP), hra (coordinates), variant (dual-graph), dataset (FAIR)

### P2e: Evidence Typing (⬜ Phase E)
- MI ontology alignment for `interacts_with` (6.1M edges)
- Decompose `related_to` (17.6M edges)
- Add evidence metadata to all Observation Graph edges

### P2f: Ontology Manager (⬜ Phase F)
- `cytos.ontology` module: registry, fetcher, validator, reasoner, converter
- CLI: `cytos ontology fetch/validate/reason/convert`

## Future: P3 — AI Featurization

| Priority | Task | Dependencies |
|----------|------|-------------|
| P3a | Graph embedding (TransE/RotatE) on typed edges | P2e (evidence typing) |
| P3b | Node feature matrix (ontology + expression) | P2d (schemas) |
| P3c | Sensor data featurization (CellxGene, NWB) | P2d (Sensor schema) |
| P3d | Multi-modal embedding alignment | P3a + P3b + P3c |

## Future: P4 — Platform Integration

| Priority | Task | Dependencies |
|----------|------|-------------|
| P4a | Cytoverse health coordinate system | P3d (embeddings) |
| P4b | Cytoscope sensor data ingestion | P2f (ontology manager) |
| P4c | Cytonome on-device inference | P4a + P4b |
| P4d | Patient-specific CCF registration | P1c (HRA) + P4b |

## Priority Matrix

```
                    Urgency
              HIGH          LOW
         ┌──────────┬──────────┐
   HIGH  │ P2b,P2c  │ P3a,P3b  │
Impact   │ Cleanup  │ Embeddings│
         ├──────────┼──────────┤
   LOW   │ P2e      │ P4c,P4d  │
         │ Evidence │ On-device │
         └──────────┴──────────┘
```
