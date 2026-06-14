# Cytos Implementation Plan

> Status: **Phase 1-2 complete (including RO-Crate integration), Phase 3 ready to begin**
> Pipeline stack: **Kedro + DVC + MLflow + Dagster + RO-Crate** (confirmed)

## Completed Work

### Phase 1: Design Doc Review & Pipeline Decision ✅

| Task | Status |
|------|--------|
| Read all 4 design docs (58KB + 11KB + 10KB + 15KB = 94KB) | ✅ |
| Read linkml_kg_playbook README (10KB, 22-chapter overview) | ✅ |
| Research Kedro, DVC, Dagster, ZenML, MLflow, Prefect | ✅ |
| Pipeline tool recommendation artifact written | ✅ |
| Research RO-Crate ecosystem (spec v1.2, WRROC, Five Safes, ro-crate-py) | ✅ |
| RO-Crate integration plan artifact written | ✅ |

**Decision**: Kedro + DVC + MLflow + Dagster + RO-Crate (provenance packaging). See:
- [pipeline_tool_recommendation.md](file:///home/mohammadi/.gemini/antigravity/brain/cd6537fc-9f66-43c5-80fd-f9d2c8fe6893/artifacts/pipeline_tool_recommendation.md)
- [rocrate_integration_plan.md](file:///home/mohammadi/.gemini/antigravity/brain/cd6537fc-9f66-43c5-80fd-f9d2c8fe6893/artifacts/rocrate_integration_plan.md)

### Phase 2: Cytocast Profile Update & Package Scaffold ✅

| Task | Status | File |
|------|--------|------|
| Updated `profiles/cytos.yaml` (pipeline_framework, kedro_pipelines, capabilities) | ✅ | [cytos.yaml](file:///home/mohammadi/repos/cytognosis/cytocast/profiles/cytos.yaml) |
| Created cytos package at `/home/mohammadi/repos/cytognosis/cytos/` | ✅ | — |
| `pyproject.toml` with full dependency spec + extras | ✅ | [pyproject.toml](file:///home/mohammadi/repos/cytognosis/cytos/pyproject.toml) |
| `src/cytos/__init__.py` + `__main__.py` | ✅ | — |
| CLI with all 14 command groups (480 lines) | ✅ | [cli/main.py](file:///home/mohammadi/repos/cytognosis/cytos/src/cytos/cli/main.py) |
| SourceDescriptor + ProvenanceHeader + CohortDefinition + ModelCard models | ✅ | [descriptor.py](file:///home/mohammadi/repos/cytognosis/cytos/src/cytos/sources/descriptor.py) |
| Source registry (load/list/fetch/doctor) | ✅ | [registry.py](file:///home/mohammadi/repos/cytognosis/cytos/src/cytos/sources/registry.py) |
| HTTP fetcher with rate limiting | ✅ | [http.py](file:///home/mohammadi/repos/cytognosis/cytos/src/cytos/sources/http.py) |
| Path constants (all repo dirs) | ✅ | [paths.py](file:///home/mohammadi/repos/cytognosis/cytos/src/cytos/utils/paths.py) |
| IO utilities (atomic write, SHA-256, YAML/JSON) | ✅ | [io.py](file:///home/mohammadi/repos/cytognosis/cytos/src/cytos/utils/io.py) |
| Kedro Data Catalog (all stage IO contracts) | ✅ | [catalog.yml](file:///home/mohammadi/repos/cytognosis/cytos/conf/base/catalog.yml) |
| Kedro parameters (release, cohort, modalities) | ✅ | [parameters.yml](file:///home/mohammadi/repos/cytognosis/cytos/conf/base/parameters.yml) |
| Kedro settings + pipeline registry | ✅ | [settings.py](file:///home/mohammadi/repos/cytognosis/cytos/src/cytos/settings.py), [pipeline_registry.py](file:///home/mohammadi/repos/cytognosis/cytos/src/cytos/pipeline_registry.py) |
| Data engineering pipeline (7 nodes) | ✅ | [data_engineering/pipeline.py](file:///home/mohammadi/repos/cytognosis/cytos/src/cytos/pipelines/data_engineering/pipeline.py) |
| Modeling pipeline (5 nodes) | ✅ | [modeling/pipeline.py](file:///home/mohammadi/repos/cytognosis/cytos/src/cytos/pipelines/modeling/pipeline.py) |
| Publishing pipeline (2 nodes) | ✅ | [publishing/pipeline.py](file:///home/mohammadi/repos/cytognosis/cytos/src/cytos/pipelines/publishing/pipeline.py) |
| Noxfile with 30+ sessions | ✅ | [noxfile.py](file:///home/mohammadi/repos/cytognosis/cytos/noxfile.py) |
| 11 source descriptor YAMLs | ✅ | [configs/sources/](file:///home/mohammadi/repos/cytognosis/cytos/configs/sources/) |
| LinkML master schema (cytos.yaml) + core types | ✅ | [schemas/](file:///home/mohammadi/repos/cytognosis/cytos/schemas/) |
| 13 domain schema stubs | ✅ | [schemas/domains/](file:///home/mohammadi/repos/cytognosis/cytos/schemas/domains/) |
| Policy: VERSION_POLICY, source_licenses, Rego gates | ✅ | [policy/](file:///home/mohammadi/repos/cytognosis/cytos/policy/) |
| Training recipe (PoE-VAE pilot) | ✅ | [poe_vae_pilot.yaml](file:///home/mohammadi/repos/cytognosis/cytos/configs/training/recipes/poe_vae_pilot.yaml) |
| README with pipeline DAG and CLI surface | ✅ | [README.md](file:///home/mohammadi/repos/cytognosis/cytos/README.md) |
| .gitignore | ✅ | — |
| Unit tests for SourceDescriptor | ✅ | [test_sources.py](file:///home/mohammadi/repos/cytognosis/cytos/tests/unit/test_sources.py) |
| 40+ `__init__.py` files for all modules | ✅ | — |
| RO-Crate publishing module (Process/Workflow/Provenance Run Crate) | ✅ | [rocrate.py](file:///home/mohammadi/repos/cytognosis/cytos/src/cytos/publish/rocrate.py) |
| RO-Crate unit tests | ✅ | [test_rocrate.py](file:///home/mohammadi/repos/cytognosis/cytos/tests/unit/test_rocrate.py) |
| `rocrate>=0.12` in core deps, `runcrate>=0.6` in extras | ✅ | [pyproject.toml](file:///home/mohammadi/repos/cytognosis/cytos/pyproject.toml) |
| Profile updated with RO-Crate capabilities + WRROC profiles | ✅ | [cytos.yaml](file:///home/mohammadi/repos/cytognosis/cytocast/profiles/cytos.yaml) |
| CLI: `cytos publish rocrate`, `cytos publish workflowhub` commands | ✅ | [cli/main.py](file:///home/mohammadi/repos/cytognosis/cytos/src/cytos/cli/main.py) |

**Total files created: ~100**

---

## Remaining Work

### Phase 3: Schema Authoring ✅

Fleshed out all 13 domain schema stubs with full LinkML classes, enums, and
ontology-aligned attributes. **2,565 total lines** across 13 domain schemas.

| Schema | Playbook Ch. | Key Classes | Lines | Status |
|--------|-------------|-------------|-------|--------|
| `anatomy.yaml` | 04, 09 | AnatomicalEntity, Tissue, CellType, Organ, BiologicalSample | 142 | ✅ |
| `disease.yaml` | 04, 05 | Disease, PhenotypicFeature, DiagnosticCriteria, GeneToDiseaseAssociation | 177 | ✅ |
| `gene.yaml` | 06 | Gene, Transcript, Protein, GeneExpression | 209 | ✅ |
| `variant.yaml` | 07 | SequenceVariant, Haplotype, Genotype, VariantToDiseaseAssociation | 193 | ✅ |
| `drug.yaml` | 06, 11 | ChemicalEntity, Drug, DrugExposure, ChemicalToGeneAssociation | 212 | ✅ |
| `phenotype.yaml` | 04, 16 | Phenotype, PhenotypicQuality, PhenotypeAssociation, ClinicalProfile | 143 | ✅ |
| `expression.yaml` | 09, 18 | ExpressionDataset, SingleCellExperiment, CellMetadataRow, CytoCellMetadataRow, AnnDataSet | 223 | ✅ |
| `pathway.yaml` | 06 | Pathway, BiologicalProcess, MolecularFunction, CellularComponent, GeneToPathwayAssociation | 133 | ✅ |
| `biothings.yaml` | 06 | BioThingsAPI, DDESchema, APIEndpoint | 141 | ✅ |
| `ga4gh.yaml` | 07 | VRSVariation, Phenopacket, PhenopacketPhenotypicFeature, PhenopacketDisease, PedigreeNode, BeaconQuery | 252 | ✅ |
| `publication.yaml` | 12 | Publication, Author, Journal, Institution, Citation | 226 | ✅ |
| `sensor.yaml` | 08 | Sensor, Observation, FeatureOfInterest, ObservableProperty, Procedure, Platform | 233 | ✅ |
| `nwb.yaml` | 10 | NWBFile, NWBSubject, TimeSeries, ElectricalSeries, Electrode, ElectrodeGroup, SpikeUnit, Stimulus | 281 | ✅ |

### Phase 4: Per-Source Ingest Modules ✅

Implemented all 7 parsers (full production code) and 10 linkmlize modules
(3 full + 7 stubs with BaseLinkMLizer interface). **21 files, 2,082 lines**.

| Module | Playbook Ch. | Implementation | Status |
|--------|-------------|----------------|--------|
| `parsers/rdf.py` | 03, 08 | rdflib + pyld, class/property extraction, JSON-LD framing | ✅ |
| `parsers/jsonschema.py` | 06, 07 | YAML/JSON, `$ref` resolution, type mapping | ✅ |
| `parsers/rrf.py` | 05 | DuckDB-based MRCONSO/MRREL/MRSTY/MRDEF views | ✅ |
| `parsers/parquet.py` | 11 | PyArrow streaming, predicate pushdown, schema introspection | ✅ |
| `parsers/bibtex.py` | 12 | bibtexparser with LaTeX cleanup, entry normalization | ✅ |
| `parsers/owl.py` | 05 | pronto (OBO) + owlready2 (OWL), auto-detect | ✅ |
| `parsers/hdmf.py` | 10 | NamespaceCatalog walker, group/dataset extraction | ✅ |
| `linkmlize/base.py` | — | Abstract base class with Parquet/YAML/provenance helpers | ✅ |
| `linkmlize/cellxgene.py` | 09 | Full: obs → CellMetadataRow Parquet + dataset metadata | ✅ |
| `linkmlize/opentargets.py` | 11 | Full: targets/diseases/drugs → Gene/Disease/Drug Parquet | ✅ |
| `linkmlize/openalex.py` | 12 | Full: Works → Publication/Author Parquet + BibTeX path | ✅ |
| `linkmlize/schema_org.py` | 03 | Stub (BaseLinkMLizer interface) | 🔲 |
| `linkmlize/biolink.py` | 04 | Stub | 🔲 |
| `linkmlize/umls.py` | 05 | Stub | 🔲 |
| `linkmlize/biothings.py` | 06 | Stub | 🔲 |
| `linkmlize/ga4gh.py` | 07 | Stub | 🔲 |
| `linkmlize/sosa.py` | 08 | Stub | 🔲 |
| `linkmlize/nwb.py` | 10 | Stub | 🔲 |


### Phase 5: KG + Harmonize Modules

| Module | Status |
|--------|--------|
| `harmonize/oak.py` — OAK adapter wrappers | ⬜ |
| `harmonize/sssom.py` — SSSOM set algebra | ⬜ |
| `harmonize/tiered_resolver.py` — tiered entity resolution | ⬜ |
| `harmonize/curies.py` — prefix policy | ⬜ |
| `kg/biocypher/adapters/base.py` — adapter base class | ⬜ |
| `kg/biocypher/ontology_graft.py` — head/tail grafts | ⬜ |
| `kg/biocypher/runner.py` — BioCypher execution | ⬜ |
| `kg/koza/source_scaffold.py` — Koza config generator | ⬜ |
| `kg/koza/runner.py` — Koza execution | ⬜ |
| `kg/merge.py` — KGX merge bridge | ⬜ |
| `kg/storage/neo4j.py`, `duckdb.py`, etc. | ⬜ |

### Phase 6: Modeling Stack

| Module | Status |
|--------|--------|
| `features/modalities/*.py` — 5 modality featurizers | ⬜ |
| `models/encoders/*.py` — 7 encoder types | ⬜ |
| `models/fusion/*.py` — 7 fusion strategies | ⬜ |
| `models/ot/*.py` — 5 OT modules | ⬜ |
| `train/lightning/trainer.py` — Lightning wrapper | ⬜ |
| `train/mlflow.py` — MLflow integration | ⬜ |
| `evaluate/integration/scib.py`, `cka.py`, etc. | ⬜ |
| `publish/snapshot.py` — versioned bundler | ⬜ |
| `rag/*.py` — optional LLM layer | ⬜ |

### Phase 7: CI/CD + Production

| Task | Status |
|------|--------|
| `.github/workflows/ci.yaml` | ⬜ |
| `.github/workflows/kg-build.yaml` | ⬜ |
| `.github/workflows/pretrain.yaml` | ⬜ |
| `Dockerfile` + `docker-compose.yml` | ⬜ |
| `mkdocs.yml` + docs site | ⬜ |
| DVC remote configuration | ⬜ |
| MLflow server deployment | ⬜ |

---

## Priority Order

1. **Phase 3**: Schema authoring (unblocks all downstream work)
2. **Phase 4**: Parsers + linkmlize (enables first data flow)
3. **Phase 5**: KG build (enables first KG snapshot)
4. **Phase 6**: Modeling stack (enables first training run)
5. **Phase 7**: CI/CD (enables production deployment)

> [!TIP]
> Pipeline stack confirmed: **Kedro + DVC + MLflow + Dagster + RO-Crate**.
> RO-Crate integration is complete at the code level.
> Ready to proceed with Phase 3 (schema authoring) immediately.
