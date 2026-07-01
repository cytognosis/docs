# Toolchain Platform Overview (technical)

> **Status:** Active · **Date:** 2026-07-01 · **Author:** Toolchain agent · **Audience:** engineering (canonical)

## Scope
The Toolchain pillar provides the reproducibility and capability substrate for all Cytognosis engineering: environment/asset management, project scaffolding, agent-skill management, and a cross-repo memory index. Four repositories compose the pillar.

## Components and interfaces

### cytoskeleton — environment and asset manager
Configuration-as-Code over `uv`. Declarative YAML components compose into environments; resolution is a DAG with recursive parameter resolution, environment inheritance, and lock integrity checks (see `cytoskeleton/architecture.md`). Backends: CPU, CUDA, ROCm (Strix Halo `gfx1151`). A virtual filesystem (VFS) abstracts GCS, local files, Git, Hugging Face Hub, and Zenodo. Assets are versioned via **DVC** to `gs://cytognosis-data-hub/assets`; the repo commits only DVC pointers, `manifest.yaml`, and `*.provenance.json` (blobs never enter git). LinkML schemas (`src/cytoskeleton/schemas/core.yaml`, `docker.yaml`) are source assets, tracked in git.

### cytocast — project scaffolder
Copier-based generator with 14 profile presets and 85 documented features across 19 categories (`cytocast/features/index.md`). It bakes in CI/CD (GitHub Actions, self-hosted runner), a four-tier ruff quality hierarchy, Docker/DevContainer configs, MkDocs+Quarto docs, MLflow/Lightning/Hydra ML tracking, and license selection. Generated projects consume cytoskeleton for environments and vendor cytoskills skills post-generation.

### cytoskills — skill platform
TypeScript/Commander.js CLI (`cyto-skills`) over a two-entity model (Repository layer + Profile layer) with a 13-division, 87-skill taxonomy. Commands cover discovery, classification, judging, profile-based deployment, and agent config. Skills are tagged on two orthogonal axes (see ontology below). CI runs `cyto-skills judge all --root skills/`.

### cytomem — memory and index
Cross-repo index and provenance spine (the deduplication oracle), with `DEPENDS_ON` / `SUPERSEDES` / `MIGRATED_TO` edges. Local store at `cytomem/.cytomem/`. Two registries in `cytomem/configs/`: `tracks.yaml` (pillar to repo map) and `doc_sources.yaml` (non-repo folders to ingest). cytomem is rebuilt once, as a terminal job, from consolidated truth.

## Composition flow
`cytocast` scaffolds a project; the project resolves environments and assets through `cytoskeleton`; it vendors capabilities from `cytoskills`; `cytomem` indexes the resulting docs and code across all repos. The ontology tags every skill so routing and capability search are well-defined.

## Skill-tagging ontology (SHARED-BLUEPRINT Section 10)
Two SKOS vocabularies in `cytoskeleton/ontologies/`:
- **Axis A (`cyto-se-usecase.ttl`):** SWEBOK v4-derived use-case concepts (`cyto:se/*`), each with GitHub-Topic aliases and, where verified, a Wikidata `skos:closeMatch`; plus an 8-value task-intent enumeration.
- **Axis B (`cyto-org-function.ttl`):** APQC PCF v7.4 functions (`apqc:pcf:*`) typed `archimate:BusinessFunction`, plus a `cyto:science/*` local extension.
A skill declares at least one axis. The CI gate (`validate_skill_tags.py`, workflow `skill-tags.yml`) fails any skill missing both axes or referencing a concept absent from the vocabularies. Pin the ontology version (`1.0.0`) in downstream consumers.

## Data and generated artifacts
Per SHARED-BLUEPRINT Section 16: source data to the Data Hub via DVC; generated trees (`.venv`, `dist`, `site`, `node_modules`, `packages/*/dist`) gitignored and regenerated on demand; document renders derived from Markdown source. The cytos `.gitignore` DVC carve-out model is propagated to cytocast and cytoskeleton (cytoplex and Yar pending, see the Toolchain project artifacts).

## Invariants
- One canonical home per artifact; cross-cutting docs here, repo-internal docs in each repo.
- No blobs over ~10 MB in git.
- cytomem is not patched mid-consolidation; it is rebuilt terminally.
- Ontology versions are pinned; taxonomy changes never silently retag existing skills.

## Source-of-truth files
`cytoskeleton/ontologies/*.ttl`, `cytomem/configs/{tracks,doc_sources}.yaml`, `04-Engineering/standards/*`, `04-Engineering/decisions/*`, and the Toolchain project `00-CONSOLIDATION/`.
