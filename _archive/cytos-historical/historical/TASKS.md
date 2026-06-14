# Cytos Task List

> Last updated: 2026-05-12 | Phase: P2 — Semantic Infrastructure

## Status Legend

| Symbol | Meaning |
|--------|---------|
| ✅ | Complete |
| 🔄 | In progress |
| ⬜ | Not started |
| ❌ | Blocked |

---

## Phase P0: Foundation ✅

| ID | Task | Status |
|----|------|--------|
| P0.1 | UMLS 2026AA RRF ingestion | ✅ |
| P0.2 | SNOMED CT RF2 parsing (INT + US) | ✅ |
| P0.3 | 37 OBO/OWL ontologies via Pronto | ✅ |
| P0.4 | UniProt XML streaming (868K proteins) | ✅ |
| P0.5 | DuckDB KGBuilder implementation | ✅ |
| P0.6 | KGX TSV format + BioLink categories | ✅ |
| P0.7 | Semantic overlay (TUI→BioLink mapping) | ✅ |

## Phase P1: External KG Integration ✅

| ID | Task | Status | Nodes | Edges |
|----|------|--------|------:|------:|
| P1.1 | Monarch Initiative | ✅ | 1,379,605 | 15,356,321 |
| P1.2 | PrimeKG | ✅ | 129,312 | 8,100,498 |
| P1.3 | Open Targets 25.03 | ✅ | 125,360 | 465,572 |
| P1.4 | PKG2.0 (scholarly) | ✅ | 1,480,795 | 34,565,345 |
| P1.5 | PlaNet (clinical trials) | ✅ | 184,861 | 3,765,506 |
| P1.6 | UniChem xrefs | ✅ | 0 | 10,000,000 |
| P1.7 | Ensembl 115 xrefs | ✅ | 0 | 1,645,953 |
| P1.8 | Monarch SSSOM | ✅ | 0 | 1,262,397 |
| P1.9 | Topic areas (AIO+CSO+ROADMAP) | ✅ | 15,715 | 54,692 |

## Phase P1b: Infrastructure ✅

| ID | Task | Status |
|----|------|--------|
| P1b.1 | Neo4j 2026.04.0 deployment | ✅ |
| P1b.2 | DVC pipeline (10 stages) | ✅ |
| P1b.3 | Dagster orchestration | ✅ |
| P1b.4 | RO-Crate provenance | ✅ |
| P1b.5 | pytest integrity suite (33 tests) | ✅ |
| P1b.6 | Data lake (13 canonical directories) | ✅ |

## Phase P1c: HRA Integration ✅

| ID | Task | Status |
|----|------|--------|
| P1c.1 | CCF Ontology ingestion (ccf.owl) | ✅ |
| P1c.2 | 9,493 HRA nodes + 26,444 edges | ✅ |
| P1c.3 | 3,481 spatial placements (Parquet) | ✅ |
| P1c.4 | LinkML hra.yaml schema [provisional] | ✅ |

---

## Phase P2: Semantic Infrastructure 🔄

### P2a: Architecture Design ✅

| ID | Task | Status |
|----|------|--------|
| P2a.1 | Define Three Constituent Graphs (Ontology/Catalog/Observation) | ✅ |
| P2a.2 | Sensor → Assay → Schema → Location model | ✅ |
| P2a.3 | FAIR Data Access Layer design | ✅ |
| P2a.4 | Interaction Taxonomy (MI ontology alignment) | ✅ |
| P2a.5 | Classification Layer design (UMLS STN, MeSH, BioLink) | ✅ |
| P2a.6 | Entity type audit (42 canonical types) | ✅ |
| P2a.7 | Clinical Trial dual-graph resolution | ✅ |
| P2a.8 | Genome/Variant dual-graph resolution | ✅ |
| P2a.9 | Device hierarchy (Device → MedicalDevice + Sensor) | ✅ |
| P2a.10 | Behavior split (NeurobehavioralPhenotype + BehavioralAssessment) | ✅ |
| P2a.11 | CellLine full schema (CLO + Cellosaurus) | ✅ |
| P2a.12 | Exposure entity hierarchy (ECTO + ExO + ENVO) | ✅ |
| P2a.13 | HRA Ontology Graph integration design | ✅ |

### Phase A: Data Lake Cleanup ✅

| ID | Task | Status | Verification |
|----|------|--------|-------------|
| A.1 | Create archive directory | ✅ | `/01-ontologies/archive/` created |
| A.2 | Move legacy subdirs to archive | ✅ | 7 dirs archived (biomedical, clinical, neuro, singlecell, environmental, experimental, latest) |
| A.3 | Create flat `/owl/` directory | ✅ | 72 OWL files |
| A.4 | Create `/mappings/` directory | ✅ | Directory exists |
| A.5 | Deduplicate OWL files into `/owl/` | ✅ | 72 files (49 from latest + 23 extras) |
| A.6 | Validate structure | ✅ | archive/, owl/, mappings/, registry.yaml |

### Phase B: Registry Creation ✅

| ID | Task | Status | Verification |
|----|------|--------|-------------|
| B.1 | Create registry YAML schema | ✅ | schema_version 1.0.0 |
| B.2 | Register 50+ resources | ✅ | 51 resources |
| B.3 | Annotate entity types per ontology | ✅ | All types covered |
| B.4 | Add version tracking | ✅ | version_installed field |
| B.5 | Cross-reference to constituent graph | ✅ | All have `graph: ontology` |
| B.6 | Commit registry to repo | ✅ | At datasets/01-ontologies/registry.yaml |

### Phase C: Entity Reclassification ✅

| ID | Task | Nodes | Status | Verification |
|----|------|------:|--------|-------------|
| C.1 | TUI-based reclassification | 44,844 | ✅ | 20 transition types |
| C.2 | Agent → Organization | 3,420 | ✅ | cytos:Organization in Neo4j |
| C.3 | IndividualOrganism → OccupationalRole | 7,449 | ✅ | cytos_OccupationalRole in Neo4j |
| C.4 | Population rename | 10,197 | ✅ | cytos_PopulationGroup in Neo4j |
| C.5 | QuantityValue → MeasurementUnit | 5,725 | ✅ | cytos_MeasurementUnit in Neo4j |
| C.6 | Behavior → NeurobehavioralPhenotype | 1,274 | ✅ | cytos_NeurobehavioralPhenotype in Neo4j |
| C.7 | Behavior → SocialDeterminant | 1,306 | ✅ | cytos_SocialDeterminant in Neo4j |
| C.8 | NamedThing reduction | 66,582 | ✅ | Down from 77,649 (14% reduction) |
| C.9 | Run pytest suite | — | ✅ | 55 passed, 14 pre-existing |

### Phase D: Schema Implementation ✅ (9/13)

| ID | Task | File | Status | Verification |
|----|------|------|--------|-------------|
| D.1 | cellline.yaml (CLO+Cellosaurus) | `schemas/domains/cellline.yaml` | ✅ | 1 class, 19 slots, 2 enums |
| D.2 | device.yaml (Device hierarchy) | `schemas/domains/device.yaml` | ✅ | 4 classes, 16 slots, 2 enums |
| D.3 | behavior.yaml (NBO+DSM-5+PHQ-9) | `schemas/domains/behavior.yaml` | ✅ | 3 classes, 14 slots, 2 enums |
| D.4 | exposure.yaml (ECTO+ExO+ENVO) | `schemas/domains/exposure.yaml` | ✅ | 1 class, 6 slots, 2 enums |
| D.5 | geography.yaml (GAZ+ISO 3166) | `schemas/domains/geography.yaml` | ✅ | 1 class, 6 slots, 1 enum |
| D.6 | measurement.yaml (UO+QUDT) | `schemas/domains/measurement.yaml` | ✅ | 1 class, 5 slots |
| D.7 | population.yaml (OMB+GAZ) | `schemas/domains/population.yaml` | ✅ | 1 class, 3 slots |
| D.8 | agent.yaml (ROR+Schema.org) | `schemas/domains/agent.yaml` | ✅ | 2 classes, 6 slots |
| D.9 | Update clinical.yaml (OMOP) | `schemas/domains/clinical.yaml` | ⬜ | Deferred to P3 |
| D.10 | Update hra.yaml (coordinates) | `schemas/domains/hra.yaml` | ⬜ | Deferred to P3 |
| D.11 | Update variant.yaml (dual-graph) | `schemas/domains/variant.yaml` | ⬜ | Deferred to P3 |
| D.12 | dataset.yaml (FAIR fields) | `schemas/domains/dataset.yaml` | ✅ | 1 class, 17 slots |
| D.13 | Update cytos.yaml master import | `schemas/cytos.yaml` | ⬜ | Deferred to P3 |

### Phase E: Evidence Typing ✅ (partial)

| ID | Task | Edges | Status | Verification |
|----|------|------:|--------|-------------|
| E.1 | Edge decomposition module | — | ✅ | `evidence_typing.py` created |
| E.2 | Decompose related_to via MRREL | 15,287,266 | ✅ | 2,452,364 decomposed (16%) |
| E.3 | New predicates from decomposition | — | ✅ | 8 new predicates (closeMatch, subclass_of, etc.) |
| E.4 | Evidence metadata schema | — | ✅ | SOURCE_TO_EVIDENCE dict (18 sources) |
| E.5 | Remaining related_to | 12,834,902 | 🔄 | RO-type needs RELA analysis |
| E.6 | Validate typed edges | — | ✅ | Distribution confirmed |

### Phase F: Ontology Manager ✅

| ID | Task | File | Status | Verification |
|----|------|------|--------|-------------|
| F.1 | Registry loader | `ontology/registry.py` | ✅ | Loads 51 resources |
| F.2 | Fetcher | `ontology/fetcher.py` | ✅ | HTTP + OBO→OWL conversion |
| F.3 | Validator | `ontology/validator.py` | ✅ | ROBOT-based validation |
| F.4 | Reasoner | `ontology/reasoner.py` | ⬜ | Deferred to P3 |
| F.5 | Converter | `ontology/converter.py` | ⬜ | Deferred to P3 |
| F.6 | CLI | `ontology/cli.py` | ✅ | status, list, fetch, validate, fetch-all |
| F.7 | Tests | `tests/test_ontology.py` | ⬜ | Deferred to P3 |

### Phase G: Neo4j Update ✅

| ID | Task | Status | Verification |
|----|------|--------|-------------|
| G.1 | Reclassified nodes.tsv | ✅ | 44,844 nodes reclassified |
| G.2 | Export to Neo4j CSV | ✅ | 10.2M nodes, 77.9M edges |
| G.3 | Bulk import to Neo4j | ✅ | 9.2M nodes, 52.4M rels (1m 51s) |
| G.4 | Verify node counts | ✅ | NamedThing = 38,817 (< 50K ✅) |
| G.5 | Verify new labels | ✅ | 6 cytos_ labels present |
| G.6 | Verify decomposed edges | ✅ | related_to reduced 16% |
| G.7 | Run full test suite | ✅ | 55 passed, 14 pre-existing failures |

### Phase H: Documentation Sync ✅

| ID | Task | Status |
|----|------|--------|
| H.1 | Update design/README.md | ✅ |
| H.2 | Update design/ARCHITECTURE.md | ✅ |
| H.3 | Update design/SCHEMAS.md | ✅ |
| H.4 | Update design/ROADMAP.md | ✅ |
| H.5 | Update design/TASKS.md | ✅ |
| H.6 | Update design/HRA_INTEGRATION.md | ✅ |
| H.7 | Create design/EXECUTION_PLAN.md | ✅ |
| H.8 | Create design/AUTOMATION.md | ✅ |

---

## Summary

| Phase | Tasks | Complete | Remaining |
|-------|------:|--------:|----------:|
| P0 Foundation | 7 | 7 | 0 |
| P1 External KGs | 9 | 9 | 0 |
| P1b Infrastructure | 6 | 6 | 0 |
| P1c HRA | 4 | 4 | 0 |
| P2a Architecture | 13 | 13 | 0 |
| A Data Cleanup | 6 | 6 | 0 |
| B Registry | 6 | 6 | 0 |
| C Reclassification | 9 | 9 | 0 |
| D Schemas | 13 | 9 | 4 |
| E Evidence Typing | 6 | 5 | 1 |
| F Ontology Manager | 7 | 4 | 3 |
| G Neo4j Update | 7 | 7 | 0 |
| H Documentation | 8 | 8 | 0 |
| **Total** | **101** | **93** | **8** |
