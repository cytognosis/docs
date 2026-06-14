# Cytos Requirements

> Last updated: 2026-05-12 | Version: 3.0

## 1. Functional Requirements

### FR-OG: Ontology Graph

| ID | Requirement | Status |
|----|------------|--------|
| FR-OG-01 | Ingest 50+ ontologies, vocabularies, and identifier registries from OBO/OWL/RRF/RF2 formats | ✅ |
| FR-OG-02 | Maintain a `registry.yaml` as single source of truth for all semantic resources | ⬜ |
| FR-OG-03 | Support selective update of individual ontologies (by ID, class, or query) | ⬜ |
| FR-OG-04 | Auto-convert OBO to OWL upon download | ⬜ |
| FR-OG-05 | Validate OWL files against EL++ profile using ROBOT | ⬜ |
| FR-OG-06 | Store cross-ontology mappings in SSSOM format | ✅ |
| FR-OG-07 | Integrate HRA CCF as spatial scaffold with 3D coordinates | ✅ |
| FR-OG-08 | Support HRA ASCT+B tables for 41 organs | ✅ |
| FR-OG-09 | Map all ontology entities to BioLink categories (42 canonical types) | 🔄 |
| FR-OG-10 | Propagate UMLS Semantic Network types to ~80% of biomedical nodes | ⬜ |
| FR-OG-11 | Support MeSH tree number assignment for disease/drug/anatomy nodes | ⬜ |

### FR-CG: Catalog Graph

| ID | Requirement | Status |
|----|------------|--------|
| FR-CG-01 | Ingest 1M+ publications from PKG2.0 with citation links | ✅ |
| FR-CG-02 | Ingest 480K+ clinical trial metadata from ClinicalTrials.gov | ✅ |
| FR-CG-03 | Dataset nodes carry FAIR-compliant fields (DCAT, EDAM, RO-Crate) | ⬜ |
| FR-CG-04 | Model nodes link to assay types and data schemas | ⬜ |
| FR-CG-05 | Software nodes follow CodeMeta/CITATION.cff standards | ⬜ |
| FR-CG-06 | Organization nodes link to ROR identifiers | ⬜ |
| FR-CG-07 | Citation subtyping via CiTO ontology (usesMethodIn, usesDataFrom, etc.) | ⬜ |
| FR-CG-08 | Behavioral assessment instruments (PHQ-9, GAD-7) modeled as Catalog artifacts | ⬜ |

### FR-ObG: Observation Graph

| ID | Requirement | Status |
|----|------------|--------|
| FR-ObG-01 | Ingest gene-disease associations from Monarch, PrimeKG, Open Targets | ✅ |
| FR-ObG-02 | Ingest PPI/molecular interactions from multiple databases | ✅ |
| FR-ObG-03 | Subtype `interacts_with` edges with MI ontology evidence metadata | ⬜ |
| FR-ObG-04 | Decompose `related_to` edges into specific predicates | ⬜ |
| FR-ObG-05 | Every Observation edge carries evidence_class, confidence, source_db | ⬜ |
| FR-ObG-06 | Ingest clinical trial observations (eligibility, outcomes) from PlaNet | ✅ |
| FR-ObG-07 | ClinicalFinding nodes align to OMOP CDM Condition domain | ⬜ |
| FR-ObG-08 | ClinicalCase nodes follow GA4GH Phenopackets v2 schema | ⬜ |

### FR-Sensor: Sensor Triple

| ID | Requirement | Status |
|----|------------|--------|
| FR-Sensor-01 | Every measurement maps to Assay (WHAT) × Location (WHERE) × Schema (HOW) | ⬜ |
| FR-Sensor-02 | Schema inheritance follows assay ontology hierarchy | ⬜ |
| FR-Sensor-03 | Device entity type is parent of MedicalDevice, DiagnosticDevice, Sensor | ⬜ |
| FR-Sensor-04 | Sensor measurements map to HRA/UBERON anatomical locations | ⬜ |
| FR-Sensor-05 | Per-assay data constraint schemas (format, dimensions, required fields) | ⬜ |

### FR-Infra: Infrastructure

| ID | Requirement | Status |
|----|------------|--------|
| FR-Infra-01 | Neo4j Community 2026.04.0 with 80M+ relationships | ✅ |
| FR-Infra-02 | DVC pipeline with 10+ reproducible stages | ✅ |
| FR-Infra-03 | Dagster assets for orchestrated builds | ✅ |
| FR-Infra-04 | RO-Crate provenance for all sources and artifacts | ✅ |
| FR-Infra-05 | pytest integrity suite (headers, BioLink, CURIEs, totals) | ✅ |
| FR-Infra-06 | `cytos ontology` CLI for registry-based ontology management | ⬜ |
| FR-Infra-07 | Flat ontology storage with `registry.yaml` metadata layer | ⬜ |

## 2. Non-Functional Requirements

| ID | Requirement | Target |
|----|------------|--------|
| NFR-01 | KG build time (full rebuild) | < 4 hours |
| NFR-02 | Neo4j import time | < 30 minutes |
| NFR-03 | DVC pipeline reproducibility | 100% (deterministic outputs) |
| NFR-04 | Node category coverage | 100% (no uncategorized nodes) |
| NFR-05 | Evidence typing coverage | ≥80% of Observation Graph edges |
| NFR-06 | SSSOM mapping coverage | ≥60% of ontology terms have xrefs |
| NFR-07 | Test pass rate | 100% (0 failures) |
| NFR-08 | Schema validation rate | 100% of entity types have LinkML schema |

## 3. Data Quality Requirements

| ID | Requirement | Metric |
|----|------------|--------|
| DQ-01 | No orphan nodes (every node has ≥1 edge) | orphan_count = 0 |
| DQ-02 | No duplicate nodes (same ID, different categories) | dup_count = 0 |
| DQ-03 | All CURIEs resolve to valid prefixes | invalid_prefix_count = 0 |
| DQ-04 | NamedThing nodes < 5% of total | NamedThing/total < 0.05 |
| DQ-05 | InformationContentEntity < 2% of total | ICE/total < 0.02 |
| DQ-06 | `related_to` edges < 10% of total | related_to/total < 0.10 |
| DQ-07 | HRA spatial placements have valid coordinates | all x,y,z ∈ ℝ |
