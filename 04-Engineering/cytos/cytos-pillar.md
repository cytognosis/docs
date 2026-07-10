# Cytos pillar — technical reference

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: engineers
> **Tags**: `engineering`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

> **Variants**: Technical (this doc) - Readable (cytos-pillar.md in Obsidian vault: 04-Engineering/cytos/) - Agent (cytos-pillar_prompt.md)

> **Status:** Active · **Date:** 2026-07-01 · **Audience:** Engineering (canonical) · **Pillar:** Cytoverse

**BLUF:** Cytos is the Cytognosis engineering substrate under the Cytoverse pillar. It defines the platform's data model as LinkML schemas, ingests source data under DVC, constructs a knowledge graph (GenomeKG and the scholarly KG), and exposes typed artifacts (Pydantic, JSON Schema, OWL, SHACL, SQL, GraphQL) generated from those schemas. This document is the precise, complete engineering reference; the readable and agent variants sit beside it.

## Scope and boundary

Cytos owns the **platform and engineering code** and the **Cytoverse product framing**. The science-foundation narrative (BDNF axes, factorized-PRS, bipolar geometry, micro-to-meso bridge) belongs to **Neuroverse** (`05-Research/neuroverse`) and is linked, not authored, from Cytos docs. The interface repo `cytoexplorer` is part of the pillar identity but is not restructured in this consolidation wave.

## Repository layout (`~/repos/cytognosis/cytos`)

| Path | Role | Git status |
|---|---|---|
| `schemas/*.yaml` (67 files: `cytos.yaml`, `core.yaml`, `domains/*.yaml`) | LinkML source of truth; codegen inputs | Tracked; large validation enums are DVC-managed |
| `src/cytos/` | Python package: schema, KG, datasets, models, scholarly | Tracked |
| `src/cytos/schema/generated/genomics.py` | Hand-crafted Pydantic models (LinkML PydanticGenerator bug workaround) | Tracked, labeled exception |
| `artifacts/{pydantic,docs,graphql,sql,jsonschema,owl,shacl}/` | Codegen outputs | Gitignored; empty until generated |
| `dist/schemas/` | Codegen distribution | Gitignored |
| `data/**` (44G) | Source and processed data | DVC-managed; only `*.dvc`, `manifest.yaml`, `*.provenance.json` tracked |
| `noxfile.py` | Task sessions incl. `schema_generate` | Tracked |

## Schema-to-artifact pipeline

The LinkML schemas in `schemas/` are the single source of truth. All typed artifacts are regenerated from them:

```bash
cd ~/repos/cytognosis/cytos && nox -s schema_generate   # == uv run cytos schema generate all
```

Invariants:

1. Artifacts are never edited by hand; edit the schema, then regenerate.
2. Artifacts are never committed; they are gitignored and reproducible.
3. The only hand-maintained generated file is `genomics.py`, tracked and labeled because the LinkML Pydantic generator has a cross-schema sort bug on the current import graph.
4. Data blobs never enter git; DVC pointers plus provenance sidecars do.

## Knowledge graph and data stores

GenomeKG covers genes, variants, GWAS associations, and eQTLs, built from ingested sources (GWAS Catalog, PGC, Open Targets, Monarch, Ensembl). The scholarly KG (schema `scholarly-kg-v0.4.0.yaml`) covers bibliographic resources, workflows, protocols, instruments, and their relationships, aligned with Biolink, OpenAlex, SemOpenAlex, and NCATS Translator. Persistence spans Neo4j (graph), SurrealDB (status: see `databases/SURREALDB.md`), and TileDB plus modality-specific stores for omics counts, genotypes, and signals (`data-stores.md`).

## Sensing schema

`sensing-schema/` specifies how models, sensors, and data compose into a matchable system: a universal sensor architecture, a sensor and phenotypic-assay taxonomy grounded in SOSA/SSN, and a semantic-alignment crosswalk across SOSA/SSN, IEEE 1752, FHIR, and AWARE through the Cytos LinkML spine. `unified-sensor-report.md` is the consolidated reference.

## Canonical documents

See `README.md` in this layer for the full doc map. The load-bearing set is `architecture.md` (v4.0 kernel reference), `module-map.md`, `cytos-neuros-separation.md`, `data-lifecycle-architecture.md`, the `schemas-ontologies/` corpus (LinkML playbook, resource schemas, scholarly KG v0.4.0), and the `sensing-schema/` set.

## Consolidation state

Superseded docs are in `_archive/` with forward links (two `architecture-overview` copies, `module-map-v2`, `scholarly-kg` v0.3.0). Open provenance questions (in-repo `cytos/docs/` overlap; four neuros-boundary docs) are logged in the resume kit and deferred to Wave 2. Full non-doc accounting is in `~/Claude/Projects/Cytos/00-CONSOLIDATION/DATA-MANIFEST.md`.
