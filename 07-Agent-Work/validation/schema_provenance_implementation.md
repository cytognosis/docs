# Schema, Provenance & Manifest Implementation Report

> **Date**: 2026-05-12 | **KG**: 5,813,739 nodes × 47,892,082 edges

## 1. Data Manifest (`data/manifest.yaml`)

Centralized source-of-truth for all data sources, replacing hardcoded paths.

```
data/manifest.yaml          ← URI templates with ${ENV_VAR} expansion
src/cytos/kg/source_resolver.py  ← Resolves manifest URIs → concrete paths
```

**Key features**:
- `${CYTOS_DATA_ROOT}` / `${CYTOS_RAW_ROOT}` env-var templates
- To move data to GCP: set `CYTOS_DATA_ROOT=gs://cytognosis-data/neuro-pheno`
- Version + license + release date tracked per source
- Checksum verification on all Parquet files

## 2. Provenance System

### Per-file sidecars (`.provenance.yaml`)
Generated for all 52 UMLS + 8 SNOMED Parquet files via `SourceResolver.generate_all_sidecars()`.

```yaml
# Example: MRCONSO.parquet.provenance.yaml
source: umls
source_version: 2026AA
release_date: '2026-05-01'
license_class: controlled
sha256: f5bf89d001459f55...
file_size_bytes: 720380031
transform_step: parquet_conversion
retrieval_date: '2026-05-12'
agent: cytos
manifest_path: data/manifest.yaml
```

### Run history (append-only)
Each KG build appends a timestamped log:
```
data/provenance/runs/run_20260512T052059Z.yaml
data/provenance/last_run.yaml  ← convenience pointer
```

### SSSOM mapping provenance
Preserved via `mapping_set_id` + `provided_by` fields in edge records. Every CUI→CODE link and SSSOM mapping retains its source vocabulary (SAB).

## 3. Provisional LinkML Schemas

| Schema | Classes | Enums | Node Coverage |
|--------|---------|-------|------:|
| [clinical.yaml](file:///home/mohammadi/repos/cytognosis/cytos/schemas/domains/clinical.yaml) | ClinicalFinding, ClinicalAttribute, ClinicalProcedure, MedicalDevice | 2 | 1.3M |
| [taxonomy.yaml](file:///home/mohammadi/repos/cytognosis/cytos/schemas/domains/taxonomy.yaml) | OrganismTaxon | 1 | 812K |
| [environment.yaml](file:///home/mohammadi/repos/cytognosis/cytos/schemas/domains/environment.yaml) | EnvironmentalFeature, ExperimentalFactor, CellLine | 1 | 609K |
| [semantic_network.yaml](file:///home/mohammadi/repos/cytognosis/cytos/schemas/domains/semantic_network.yaml) | SemanticType, SemanticRelation, SemanticTypeAssignment | 1 | 181 |
| [information.yaml](file:///home/mohammadi/repos/cytognosis/cytos/schemas/domains/information.yaml) | InformationEntity, NucleicAcidEntity, BiologicalActivity, BehavioralEntity | 1 | 579K |

**Total**: 19 new classes, 6 new enums, covering 3.3M previously unschematized nodes.

All schemas:
- Are marked `PROVISIONAL` with `[provisional]` field annotations
- Import `../core` for `CytosEntity` / `CytosAssociation` base classes
- Include UMLS CUI + SNOMED ID + semantic type attributes
- Are registered in [cytos.yaml](file:///home/mohammadi/repos/cytognosis/cytos/schemas/cytos.yaml) master imports

## 4. PredicateEnum (core.yaml)

All 53 edge predicates now have formal schema definitions in [core.yaml](file:///home/mohammadi/repos/cytognosis/cytos/schemas/core.yaml), grouped by:
- Hierarchy (subclass_of, superclass_of, isa, part_of)
- Mapping (skos:exactMatch)
- Semantic Network (affects, causes, treats, prevents, location_of, ...)
- SNOMED-specific (has_finding_site, has_associated_morphology, has_causative_agent)

## 5. Files Created/Modified

| File | Action |
|------|--------|
| `data/manifest.yaml` | **Created** — central data source manifest |
| `src/cytos/kg/source_resolver.py` | **Created** — URI resolution + provenance generator |
| `src/cytos/kg/builder.py` | **Modified** — uses SourceResolver, logs run provenance |
| `schemas/domains/clinical.yaml` | **Created** — provisional |
| `schemas/domains/taxonomy.yaml` | **Created** — provisional |
| `schemas/domains/environment.yaml` | **Created** — provisional |
| `schemas/domains/semantic_network.yaml` | **Created** — provisional |
| `schemas/domains/information.yaml` | **Created** — provisional |
| `schemas/core.yaml` | **Modified** — added PredicateEnum |
| `schemas/cytos.yaml` | **Modified** — added 5 new domain imports |
| `neuro-pheno/data/UMLS/*.provenance.yaml` | **Created** — 52 sidecars |

## 6. Reproducibility Guarantees

| Concern | Solution |
|---------|----------|
| **Path portability** | `${CYTOS_DATA_ROOT}` env-var, no hardcoded paths |
| **GCP migration** | Change env-var; resolver supports any path prefix |
| **Version pinning** | `manifest.yaml` records exact version per source |
| **Checksum integrity** | SHA-256 in every `.provenance.yaml` sidecar |
| **Run history** | Append-only `runs/run_{timestamp}.yaml` |
| **New release adaptation** | Update `version` + `release_date` in manifest, re-run pipeline |
| **BioCypher/Koza integration** | Schema classes use `class_uri: biolink:*` for direct mapping |
