# Consolidated Sensor Documentation and Semantic Alignment

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: engineers
> **Tags**: `engineering`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

## Goal

Consolidate all sensor-related documentation scattered across Yar (product), Cytos (schemas), and archived neuro-pheno research into a coherent, cross-linked system. Then create a dedicated semantic alignment specification for the four target standards (SOSA/SSN, IEEE 1752/Open mHealth, FHIR R5, AWARE) with concrete implementation steps.

## Current State: What Exists

The sensor documentation is substantial but fragmented across three distinct locations with overlapping content and no cross-references between them.

### Location 1: `docs/cytonome/yar/sensors/` (Production docs, 4,427 lines)

| File | Lines | Content |
|---|---|---|
| [README.md](file:///home/mohammadi/repos/cytognosis/docs/cytonome/yar/sensors/README.md) | 59 | Index of sensor docs, TL;DR recommended stack |
| [unified-sensor-report.md](file:///home/mohammadi/repos/cytognosis/docs/cytonome/yar/sensors/unified-sensor-report.md) | 716 | Master consolidated report: body, sensors, data, models in one thread |
| [sensor-taxonomy.md](file:///home/mohammadi/repos/cytognosis/docs/cytonome/yar/sensors/sensor-taxonomy.md) | 442 | Full sensor taxonomy with IEEE 1752 and Open mHealth coverage |
| [sensor-architecture.md](file:///home/mohammadi/repos/cytognosis/docs/cytonome/yar/sensors/sensor-architecture.md) | 379 | Pluggable sensor framework (Pydantic Protocol, SensorDescriptor, Voice Emotion Sensor 0 reference implementation) |
| [interop-standards.md](file:///home/mohammadi/repos/cytognosis/docs/cytonome/yar/sensors/interop-standards.md) | 284 | Cross-standard interop with IEEE 1752 and Open mHealth focus |
| [universal-sensor-schema-vault.md](file:///home/mohammadi/repos/cytognosis/docs/cytonome/yar/sensors/universal-sensor-schema-vault.md) | 1,458 | Comprehensive vault copy with full schema details |
| [data-formats.md](file:///home/mohammadi/repos/cytognosis/docs/cytonome/yar/sensors/data-formats.md) | 254 | Data storage format recommendations |
| [human-body-systems.md](file:///home/mohammadi/repos/cytognosis/docs/cytonome/yar/sensors/human-body-systems.md) | 219 | HRA and human body ontology integration |
| [ml-models.md](file:///home/mohammadi/repos/cytognosis/docs/cytonome/yar/sensors/ml-models.md) | 226 | ML model manifest and IO contracts |

### Location 2: `cytos/schemas/domains/sensor/` (LinkML schemas, 3,986 lines)

| File | Lines | Content |
|---|---|---|
| [core/core.yaml](file:///home/mohammadi/repos/cytognosis/cytos/schemas/domains/sensor/core/core.yaml) | 1,460 | Core spine: Subject, Device, Sensor, Channel, Platform, Deployment, Session, Observation, Result, Stream, UnitValue, TimeFrame |
| [core/selfreport.yaml](file:///home/mohammadi/repos/cytognosis/cytos/schemas/domains/sensor/core/selfreport.yaml) | 198 | SurveyInstrument, SurveyResponse, ESMPrompt |
| [core/context.yaml](file:///home/mohammadi/repos/cytognosis/cytos/schemas/domains/sensor/core/context.yaml) | 255 | Mobile context: Location, Screen, App, Notification, Communication events |
| [profiles/profile_sosa.yaml](file:///home/mohammadi/repos/cytognosis/cytos/schemas/domains/sensor/profiles/profile_sosa.yaml) | 79 | SOSA/SSN class/slot URI bindings |
| [profiles/profile_ieee1752.yaml](file:///home/mohammadi/repos/cytognosis/cytos/schemas/domains/sensor/profiles/profile_ieee1752.yaml) | 351 | IEEE 1752.1 / Open mHealth body-schema mirror |
| [profiles/profile_fhir.yaml](file:///home/mohammadi/repos/cytognosis/cytos/schemas/domains/sensor/profiles/profile_fhir.yaml) | 264 | FHIR R5 Observation/Device/DeviceMetric/DeviceUsage |
| [profiles/profile_aware.yaml](file:///home/mohammadi/repos/cytognosis/cytos/schemas/domains/sensor/profiles/profile_aware.yaml) | 232 | AWARE framework smartphone sensors |
| [profiles/profile_bt_ghs.yaml](file:///home/mohammadi/repos/cytognosis/cytos/schemas/domains/sensor/profiles/profile_bt_ghs.yaml) | 198 | Bluetooth GHS + IEEE 11073 |
| [profiles/profile_mcphases.yaml](file:///home/mohammadi/repos/cytognosis/cytos/schemas/domains/sensor/profiles/profile_mcphases.yaml) | 566 | Test-case profile: PhysioNet mcPHASES dataset |
| [vendors/*.yaml](file:///home/mohammadi/repos/cytognosis/cytos/schemas/domains/sensor/vendors/) | 383 | Vendor adapters: Cytoscope, Fitbit, Dexcom, Mira, Oura |
| [README.md](file:///home/mohammadi/repos/cytognosis/cytos/schemas/domains/sensor/README.md) | 75 | Schema architecture overview |

### Location 3: `archive/neuro-pheno/design_draft/schemas/research/` (Research docs, 1,581 lines)

| File | Lines | Content |
|---|---|---|
| [sensors.md](file:///home/mohammadi/repos/cytognosis/archive/neuro-pheno/design_draft/schemas/research/sensors.md) | 226 | Phenotypic measurement schemas research: OBI, BAO, EFO, UCUM, LOINC, sampling regimes, AssayManifest |
| [interop.md](file:///home/mohammadi/repos/cytognosis/archive/neuro-pheno/design_draft/schemas/research/interop.md) | 234 | How models, sensors, and data compose: match function, ontology backbone, bridge schemas |
| [linkml_kg_playbook/07_sosa_ssn_to_linkml.md](file:///home/mohammadi/repos/cytognosis/archive/neuro-pheno/design_draft/schemas/research/linkml_kg_playbook/07_sosa_ssn_to_linkml.md) | 217 | SOSA/SSN → LinkML conversion walkthrough (CytoSensor, CytoObservation) |
| [sssom_tooling_for_cytognosis.md](file:///home/mohammadi/repos/cytognosis/archive/neuro-pheno/design_draft/schemas/research/sssom_tooling_for_cytognosis.md) | 505 | SSSOM cross-ontology mapping for the scholarly KG |
| [data.md](file:///home/mohammadi/repos/cytognosis/archive/neuro-pheno/design_draft/schemas/research/data.md) | 254 | Data storage research |
| [linkml_kg_playbook/02_schema_landscape.md](file:///home/mohammadi/repos/cytognosis/archive/neuro-pheno/design_draft/schemas/research/linkml_kg_playbook/02_schema_landscape.md) | 145 | Schema landscape survey |

### Location 4: Yar Product Docs (Sensor references, scattered)

| File | Sensor Content |
|---|---|
| [product-implementation.md](file:///home/mohammadi/repos/cytognosis/docs/cytonome/yar/product-implementation.md) Phase 7 (lines 419-489) | USAP: SensorAdapter Protocol, SensorDescriptor, 6 sensor classes, plug-and-play UX |
| [adhd-paper-synthesis.md](file:///home/mohammadi/repos/cytognosis/docs/cytonome/yar/research/adhd-paper-synthesis.md) §8.9 | Sensor Integration features #44-47 (USAP, wearables, brain connectomic, environmental) |
| [yar-unified-feature-comparison-v3.md](file:///home/mohammadi/repos/cytognosis/docs/cytonome/yar/research/yar-unified-feature-comparison-v3.md) | USAP in Priority 3 features, Big Gap section |
| [cytonome-master-reference.md](file:///home/mohammadi/repos/cytognosis/docs/cytonome/yar/cytonome-master-reference.md) | Paralinguistic sensor pipeline references |

---

## Problems to Solve

### 1. Fragmentation
Three separate locations with no cross-references. A developer looking at the Yar USAP Phase 7 has no idea that 1,460-line LinkML schemas already exist in `cytos/`. A researcher reading `archive/neuro-pheno/` doesn't know the schemas were built.

### 2. Yar USAP vs. Cytos Schema Divergence
The Yar product-implementation.md defines a `SensorAdapter(Protocol)` + `SensorDescriptor(BaseModel)` that is a simplified subset of the actual `cytos/schemas/domains/sensor/` architecture. They need alignment.

### 3. Semantic Alignment Not Documented
The cytos schemas have profile files for SOSA, FHIR, IEEE 1752, and AWARE, but no documentation explains the crosswalk logic, mapping gaps, or semantic alignment strategy between them.

### 4. Missing SSSOM Integration
The SSSOM tooling doc exists in the archive but isn't connected to the sensor schema alignment. SSSOM is the right tool for formalizing the crosswalks between SOSA, FHIR, IEEE 1752, and AWARE.

---

## Proposed Changes

### Component 1: Master Consolidated Sensor Document

#### [NEW] `docs/cytonome/yar/sensors/consolidated-sensor-reference.md`

A single master reference that:
- Replaces the current `README.md` as the entry point
- Summarizes the architecture across all three locations
- Cross-links every file with clickable paths
- Maps the Yar USAP to the Cytos schema spine
- Includes the semantic alignment specification
- Provides the implementation roadmap

#### [MODIFY] `docs/cytonome/yar/sensors/README.md`

Update to point to the consolidated reference as the canonical entry point.

---

### Component 2: Semantic Alignment Specification

#### [NEW] `docs/cytonome/yar/sensors/semantic-alignment.md`

The core deliverable: a detailed specification for aligning SOSA/SSN, IEEE 1752, FHIR, and AWARE through the Cytos LinkML spine.

Contents:
1. **Schema-by-schema concept mapping table** (SOSA Observation ↔ IEEE 1752 data-point ↔ FHIR Observation ↔ AWARE sensor row)
2. **Property-level crosswalk** (sosa:madeBySensor ↔ fhir:Device ↔ ieee1752:header.source ↔ aware:device_id)
3. **Temporal alignment** (SOSA phenomenonTime ↔ IEEE 1752 TimeFrame ↔ FHIR effectiveDateTime ↔ AWARE timestamp)
4. **Unit alignment** (UCUM canonical, with QUDT/UO/MDC bridges)
5. **SSSOM mapping sets** for each crosswalk (machine-readable TSV)
6. **Gap analysis** per standard
7. **LinkML slot_uri alignment table** showing how each cytos slot maps to each standard

---

### Component 3: Yar USAP Alignment

#### [MODIFY] `docs/cytonome/yar/product-implementation.md` Phase 7

Add cross-references to the Cytos schema library and sensor docs. Update the `SensorAdapter` Protocol to note it is the Yar-facing facade over the full Cytos schema.

---

### Component 4: Cross-Linking

Update these docs with cross-links:
- `docs/cytonome/yar/sensors/README.md` → link to Yar USAP, ADHD synthesis, cytos schemas
- `docs/cytonome/yar/product-implementation.md` Phase 7 → link to sensor docs and cytos schemas
- `docs/cytonome/yar/research/adhd-paper-synthesis.md` §8.9 → link to sensor docs
- `docs/cytonome/yar/research/yar-unified-feature-comparison-v3.md` → link to sensor docs
- `cytos/schemas/domains/sensor/README.md` → link to sensor docs

---

## Open Questions

> [!IMPORTANT]
> **Q1**: Should the consolidated sensor reference live at `docs/cytonome/yar/sensors/consolidated-sensor-reference.md` alongside the existing docs, or should it replace `unified-sensor-report.md` as the new unified report?

> [!IMPORTANT]
> **Q2**: The Yar `SensorAdapter(Protocol)` in product-implementation.md is a simplified Pydantic interface. The Cytos `core.yaml` has a 1,460-line LinkML schema with 40+ classes. Should the Yar doc reference the full Cytos schema directly, or keep the simplified interface as the "Yar-facing facade" and note the full schema underneath?

> [!IMPORTANT]
> **Q3**: Do you want the SSSOM crosswalk mapping sets generated as actual `.tsv` files in the repo (machine-readable), or documented inline as markdown tables?

> [!IMPORTANT]
> **Q4**: The `archive/neuro-pheno/` research docs are thorough but live in the archive. Should we copy key content forward into the active `docs/cytonome/yar/sensors/` tree, or leave the archive in place and just add cross-links?

---

## Verification Plan

### Automated Tests
```bash
# Validate all LinkML sensor schemas still lint clean
cd cytos/schemas/domains/sensor
linkml-lint core/core.yaml
linkml-lint profiles/profile_sosa.yaml
linkml-lint profiles/profile_ieee1752.yaml
linkml-lint profiles/profile_fhir.yaml
linkml-lint profiles/profile_aware.yaml

# Validate example still passes
linkml-validate -s profiles/profile_mcphases.yaml -C SensorDataset examples/mcphases_example.yaml
```

### Manual Verification
- All cross-links resolve to correct files
- No broken file references
- Semantic alignment table covers all 4 standards
- Yar USAP references match cytos schema spine
