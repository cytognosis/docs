# Cytos (Cytoverse engineering platform) — layer index

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: engineers
> **Tags**: `engineering`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

> **Status:** Active · **Date:** 2026-07-01 · **Pillar:** Cytoverse (The Map) · **Owner:** Cytos consolidation agent · **Reading time:** ~4 min

**If you only read one thing:** This layer is the canonical home for **Cytos engineering and platform** docs. Cytos is the data-and-modeling substrate: LinkML schemas, DVC-managed ingestion, knowledge-graph construction (GenomeKG), multimodal modeling, and the sensing schema. The code lives in `~/repos/cytognosis/cytos`; the schema outputs in `cytos/artifacts/` are **generated** and gitignored (regenerate with `nox -s schema_generate`). Research narrative (the science foundation) belongs to **Neuroverse** (`05-Research/neuroverse`), not here.

## What Cytos is

| | |
|---|---|
| **Identity** | The Map: the engineering platform under the Cytoverse pillar |
| **Code repo** | `~/repos/cytognosis/cytos` (LinkML schemas, KG, models, DVC data) |
| **Sibling repo** | `~/repos/cytognosis/cytoexplorer` (interface layer; not restructured this wave) |
| **Boundary** | Cytos owns platform/engineering code; **Neuroverse** owns Research and the science foundation. The Cytoverse product framing lives in `03-Products/Cytoverse`. |

## Canonical doc map

| Topic | Canonical file | Notes |
|---|---|---|
| System architecture | `architecture.md` | v4.0 kernel reference; **supersedes** the two archived `architecture-overview` files |
| Module inventory | `module-map.md` | `src/cytos/` module table; `-v2` duplicate archived |
| Cytos/Neuros split | `cytos-neuros-separation.md` | Boundary + migration playbook (module-level) |
| Data lifecycle | `data-lifecycle-architecture.md` | Ingestion → KG → export; DVC/FAIR |
| Data stores | `data-stores.md`, `databases/{NEO4J,SURREALDB}.md`, `data-lake/INVENTORY.md` | Modality-specific stores + graph DBs |
| Genomics | `genomic-atlas.md`, `genomic-standards.md`, `genomekg/*` | Gene → variant → GWAS → eQTL → PRS |
| Schemas + ontologies | `schemas-ontologies/` | LinkML playbook (22 ch.), resource-schemas, scholarly-kg **v0.4.0** (v0.3.0 archived), software-metadata |
| Sensing schema | `sensing-schema/` | Sensor architecture, taxonomy, semantic alignment, unified-sensor-report |
| Experiments | `experiment-management-architecture.md`, `experiment-orchestration-research.md`, `experiment-management-interface.md` | Tracking + orchestration analysis |
| Decisions | `adrs/ADR-001-*.md` | Architecture decision records |
| Pillar orientation | `cytos-pillar.{technical,readable,agent}.md` | Three-variant entry doc (readable mirrored to Obsidian) |

## Schema artifacts (generated, not source)

The `cytos/artifacts/{pydantic,docs,graphql,sql,jsonschema,owl,shacl}/` trees and `dist/schemas/` are **codegen outputs** from the LinkML sources in `cytos/schemas/*.yaml`. They are gitignored and regenerated on demand:

```bash
cd ~/repos/cytognosis/cytos && nox -s schema_generate   # == uv run cytos schema generate all
```

The canonical **source** of those artifacts is the schema set: `cytos/schemas/{cytos,core}.yaml` + `schemas/domains/*.yaml` (30+), documented here under `schemas-ontologies/`. Exception: `src/cytos/schema/generated/genomics.py` is **hand-crafted** (not codegen) and git-tracked with a label. Full accounting: `~/Claude/Projects/Cytos/00-CONSOLIDATION/DATA-MANIFEST.md`.

## Consolidation notes (2026-07-01)

- **Archived** (see `_archive/`, each with a `SUPERSEDED` forward link): `architecture-overview.md`, `architecture-overview-v2.md`, `module-map-v2.md`, `scholarly-kg.yaml` (v0.3.0).
- **Flagged for Wave 2** (not moved this wave): four docs touching the neuros boundary (`brain-atlas.md`, `sensing-schema/data-formats.md`, `sensing-schema/sensor-taxonomy.md`, `schemas-ontologies/biotools-schema-edam-research.md`); and the in-repo `cytos/docs/` overlap with this layer. See the resume kit `OPEN_QUESTIONS.md` (Q6, Q7).
