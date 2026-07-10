# Cytonome Sensor Documentation — Yar's Sensing Component

> [!IMPORTANT]
> **TL;DR**: This is Yar's **sensing component**, nested at `docs/cytonome/yar/sensors/`. It defines the **sensor protocol** that lets any sensor (voice, wearables, self-report, future connectomics) plug into Yar as a typed, consent-governed adapter. The protocol is referred to here as **USAP (Universal Sensor Adapter Protocol)**; the Yar master and strategy docs call the same protocol **CSP (Cytonome Sensor Protocol)**. They are the same thing. It is a standalone sensor architecture, integrated as Yar's input layer (Yar master `§4B`) and governed by **CAP** (every adapter needs per-sensor consent; raw data stays on-device by default).

> **Start here**: [Consolidated Sensor Reference](../../cytos/sensing-schema/unified-sensor-report.md)

## Quick Navigation

### Architecture and Standards

| Document | Content |
|---|---|
| [Consolidated Sensor Reference](../../cytos/sensing-schema/unified-sensor-report.md) | **Master reference**: architecture, schema system, standards coverage, vendor profiles, interop stack, roadmap |
| [Semantic Alignment Specification](../../cytos/sensing-schema/semantic-alignment.md) | SOSA/SSN ↔ IEEE 1752 ↔ FHIR ↔ AWARE crosswalk tables, SSSOM integration, gap analysis |
| [Sensor Architecture](sensor-architecture.md) | Runtime sensor protocol, Voice Sensor 0 reference implementation, MindMed AI fusion architecture |
| [Sensor Taxonomy](../../cytos/sensing-schema/sensor-taxonomy.md) | Full sensor taxonomy across micro/meso/macro scales with IEEE 1752 and Open mHealth coverage |
| [Interop Standards](../../cytos/sensing-schema/interop-standards.md) | Cross-standard interop details and data flow patterns |

### Implementation Guides

| Document | Content |
|---|---|
| [Implementing AWARE](implementing-aware.md) | AWARE smartphone sensor data gathering: 25 sensors, ESM/EMA, digital phenotyping for ADHD |
| [Implementing Wearables](implementing-wearables.md) | Oura Ring and Fitbit integration: API mapping, Python adapters, cross-vendor normalization |
| [Implementing Health Instruments](implementing-health-instruments.md) | PHQ-9, GAD-7, ASRS, PSQI, WHO-5: instrument catalog, Cytos schema, FHIR mapping, scoring |

### Data and Models

| Document | Content |
|---|---|
| [Data Formats](../../cytos/sensing-schema/data-formats.md) | Storage format recommendations (AnnData, Zarr, Parquet, TileDB-SOMA) |
| [Human Body Systems](../../cytos/sensing-schema/human-body-systems.md) | Human Reference Atlas (HRA), HuBMAP, CCF Ontology integration |
| [ML Models](ml-models.md) | Model manifest, IO contracts, distributional outputs |

## Schema Location

The Cytos LinkML sensor schemas live at:

```
cytos/schemas/domains/sensor/
├── core/          Core spine (35+ classes, SOSA-aligned)
├── profiles/      Standard alignment (SOSA, IEEE 1752, FHIR, AWARE, BT GHS)
├── vendors/       Device-specific schemas (Oura, Fitbit, Dexcom, Mira, Cytoscope)
└── examples/      Validation examples (mcPHASES dataset)
```

Full schema documentation: [Cytos Sensor Schema README](file:///home/mohammadi/repos/cytognosis/cytos/schemas/domains/sensor/README.md)

## Yar Integration

The Yar product-level sensor integration (USAP: Universal Sensor Adapter Protocol) is defined in:

- [Product Implementation Phase 7](file:///home/mohammadi/repos/cytognosis/docs/cytonome/yar/product-implementation.md) (USAP specification)
- [ADHD Paper Synthesis §8.9](file:///home/mohammadi/repos/cytognosis/docs/cytonome/yar/research/adhd-paper-synthesis.md) (sensor features for ADHD)
- [Feature Comparison v3](file:///home/mohammadi/repos/cytognosis/docs/cytonome/yar/research/yar-unified-feature-comparison-v3.md) (USAP in competitive matrix)

## Research Lineage

Foundational research that informed this architecture (retained in archive for citation purposes):

- [Sensors Research](file:///home/mohammadi/repos/cytognosis/archive/neuro-pheno/design_draft/schemas/research/sensors.md) (ontology survey)
- [Interop Research](file:///home/mohammadi/repos/cytognosis/archive/neuro-pheno/design_draft/schemas/research/interop.md) (match function design)
- [SOSA/SSN to LinkML](file:///home/mohammadi/repos/cytognosis/archive/neuro-pheno/design_draft/schemas/research/linkml_kg_playbook/07_sosa_ssn_to_linkml.md) (conversion walkthrough)
- [SSSOM Tooling](file:///home/mohammadi/repos/cytognosis/archive/neuro-pheno/design_draft/schemas/research/sssom_tooling_for_cytognosis.md) (cross-ontology mapping)
