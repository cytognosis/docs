> **Status**: Active
> **Date**: 2026-07-17
> **Author**: @mohammadi (research agent)
> **Audience**: engineers, stakeholders, funders
> **Tags**: `yar`, `cytonome`, `index`, `master`

# Yar Documentation Pillar: Master Index

**BLUF:** Yar (Your AI Representative) is Cytonome v0.1, a local-first, voice-aware cognitive companion built by and for neurodivergent people. This is the master index for every current (non-archive) doc in this pillar, organized by section. Start with [`yar-product-spec.md`](./yar-product-spec.md) for the product, [`YAR_FEATURE_CATALOG.md`](./YAR_FEATURE_CATALOG.md) for the 64-feature index (62 original + F63, F64 added 2026-07-18), and [`submission/README.md`](./submission/README.md) if you're a YC reviewer.

**If you only read one thing:** the product spec, plus this pillar's four section indexes (`research/README.md`, `spec/README.md`, `benchmark/README.md`, `submission/README.md`), each of which cross-links the others.

---

## Identity and product spec

| File | Description |
|---|---|
| [`yar-product-spec.md`](./yar-product-spec.md) | Canonical product spec: what Yar is, architecture, feature catalog, safety, positioning (15 sections) |
| [`yar-product-spec_prompt.md`](./yar-product-spec_prompt.md) | Self-contained agent brief; companion to the product spec for a fresh agent picking up Yar |
| [`YAR_FEATURE_CATALOG.md`](./YAR_FEATURE_CATALOG.md) | Canonical 64-feature index (F01-F64; 62 original + F63, F64 added 2026-07-18), Wave 1 build table, supersedes all pre-v4 comparisons |
| [`INTEGRATION_PLAN.md`](./INTEGRATION_PLAN.md) | Codebase integration plan reconciling this docs pillar with the Yar code repo and Cytoplex |
| [`DATA-MOVED.md`](./DATA-MOVED.md) | Pointer: feature/prioritization CSV tables live in the datasets repo, not here (path corrected 2026-07-17) |
| [`sensor-architecture.md`](./sensor-architecture.md) | ADHD-friendly summary of the sensor architecture layer |
| [`sensor-ecosystem.md`](./sensor-ecosystem.md) | Sensor plug-in ecosystem for CSP (Cytonome Sensor Protocol; formerly USAP/UBAP); see `spec/SPEC-CSP.md` for the engineering-facing equivalent |
| [`simple/README.md`](./simple/README.md) | One-minute plain-language pointer into the technical docs; notes what changed in the 2026-07 consolidation |

## Research (`research/`)

Full index, statuses, and cross-links: **[`research/README.md`](./research/README.md)**.

Covers: the canonical v4 feature comparison and its supporting docs (naming convention, public catalog), the 2026-07-16 session artifacts (FINAL consolidation + simplified twin, framework assessment, salvage-reconciliation map), and promoted references (incorporation map, SurrealDB code audit, persona-profiler framework reference and schema).

**New artifacts (2026-07-18):** [`research/FEATURE-HIERARCHY.md`](./research/FEATURE-HIERARCHY.md) and [`research/features.json`](./research/features.json) (canonical 6-domain, 19-cluster, 64-feature hierarchy), [`research/COMPS-MASTER-TABLE.md`](./research/COMPS-MASTER-TABLE.md) (competitor coverage table), [`research/yar-feature-hierarchy.csv`](./research/yar-feature-hierarchy.csv), and [`assets/viz/yar-feature-tree.html`](./assets/viz/yar-feature-tree.html) (interactive feature-tree visualization).

## Spec (`spec/`)

Full index, statuses, and cross-links: **[`spec/README.md`](./spec/README.md)**.

Covers: 12 core engineering specs (CSP, data-sovereignty, edge-ai-hybrid, multi-agent, neurobehavioral-axes, personas-voice, 4 sensor-science specs, storage-engine, sync-protocol), 3 safety/governance session artifacts (privacy-boundary-spec, MODULE-crisis-detection, SAFETY-CHECKPOINT), 2 storage/sync session artifacts (ANYSYNC-FIT-ASSESSMENT, STORAGE_BENCHMARK_TRACKER), and 4 supporting storage guides. `spec/adhd/` is an empty placeholder (twins archived 2026-07-16).

## Benchmark (`benchmark/`)

Full index and cross-links: **[`benchmark/README.md`](./benchmark/README.md)**.

Covers: benchmark evaluation and results, prompts catalog, cytomem GraphRAG integration, the Antigravity execution runbook, the master drive plan, and the 2026-07-16 SurrealDB PATCH11 verdict and v3.1.5 retest report. External anchor: the reproducible benchmark package (see below).

## Submission (`submission/`)

Full index and cross-links: **[`submission/README.md`](./submission/README.md)**.

11 YC Summer 2026 judge-facing documents (architecture, demo script, evaluation, limitations, safety and trust, roadmap, etc.), last refreshed 2026-07-16 to the Tauri-reality, fully-free model.

## Steering (`steering/`)

| File | Description |
|---|---|
| [`steering/yar-product.md`](./steering/yar-product.md) | Product steering notes (active) |
| [`steering/yar-structure.md`](./steering/yar-structure.md) | Structure steering notes — **superseded 2026-07-16**, see `yar-product-spec.md` and the code repo's `ARCHITECTURE.md`; retained for history |
| [`steering/yar-tech.md`](./steering/yar-tech.md) | Tech steering notes — **superseded 2026-07-16**, same pointer as above; retained for history |

## MVP (`mvp/`) — superseded

> All files below are marked superseded as of 2026-07-16 (see `mvp/README.md`'s own banner). Canonical current state is `yar-product-spec.md` (product) and the code repo's `ARCHITECTURE.md` (engineering). Retained for historical reference, not archived.

| File | Description |
|---|---|
| [`mvp/README.md`](./mvp/README.md) | Index and status of the original Gemma-4-Good MVP package |
| [`mvp/00_CONTEXT_UPDATE.md`](./mvp/00_CONTEXT_UPDATE.md) | What changed based on early feedback and a screenshot review |
| [`mvp/01_UPDATED_MVP_SCOPE.md`](./mvp/01_UPDATED_MVP_SCOPE.md) | Final skeleton-first MVP scope |
| [`mvp/02_ARCHITECTURE_SCOPE.md`](./mvp/02_ARCHITECTURE_SCOPE.md) | Architecture boundary and system layers |
| [`mvp/03_LINKML_ANYTYPE_MAPPING.md`](./mvp/03_LINKML_ANYTYPE_MAPPING.md) | LinkML-to-Anytype type/property/relation mapping |
| [`mvp/04_ENTITY_MODEL.md`](./mvp/04_ENTITY_MODEL.md) | Initial research/personalization entity model |
| [`mvp/05_TASK_LIST.md`](./mvp/05_TASK_LIST.md) | Prioritized build task list |
| [`mvp/06_WADM_ANNOTATION_INTEGRATION.md`](./mvp/06_WADM_ANNOTATION_INTEGRATION.md) | W3C Web Annotation / LinkML / AnnotationStore integration plan |
| [`mvp/07_ARCHITECTURE_DESIGN_PROMPT.md`](./mvp/07_ARCHITECTURE_DESIGN_PROMPT.md) | Copy-paste prompt for generating detailed architecture |
| [`mvp/08_DEMO_FLOW.md`](./mvp/08_DEMO_FLOW.md) | Skeleton-first demo script |
| [`mvp/09_RISKS_AND_ACCEPTANCE_CRITERIA.md`](./mvp/09_RISKS_AND_ACCEPTANCE_CRITERIA.md) | Risks, fallback paths, pass/fail criteria |
| [`mvp/10_CAP_USAGE.md`](./mvp/10_CAP_USAGE.md) | Early CAP usage notes for the MVP |
| [`mvp/11_SETUP_CENTRAL_AND_MOBILE.md`](./mvp/11_SETUP_CENTRAL_AND_MOBILE.md) | macOS/Ubuntu central model setup and iOS/Android install scripts |
| [`mvp/PRODUCT_MILESTONE_1_MOBILE_VOICE.md`](./mvp/PRODUCT_MILESTONE_1_MOBILE_VOICE.md) | Implemented mobile voice architecture, setup, demo script, limitations |

## Sensor ecosystem

`sensor-ecosystem.md` (top level, listed above) is the live document. `sensor-ecosystem/` is an **empty directory** with no tracked files — a stray placeholder, not a duplicate or a broken section. No action taken; flagged here so it isn't mistaken for missing content.

## Prompts (`prompts/`)

| File | Description |
|---|---|
| [`prompts/object-router.md`](./prompts/object-router.md) | Structured capture router prompt |
| [`prompts/communication-translator.md`](./prompts/communication-translator.md) | Neurodivergent-to-neurotypical communication translator prompt |
| [`prompts/daily-anchor-planner.md`](./prompts/daily-anchor-planner.md) | Daily anchor/planning prompt |

## Archive

`_archive/` is excluded from this index (per pillar convention) but not deleted. It contains:

- `_archive/cleanup_2026-07-16/adhd-twins/` — the 15 ADHD-friendly spec/research twins retired 2026-07-16 when the specs were standardized; `research/README.md` and `spec/README.md` both note where each retired reference now points.
- `_archive/cleanup_2026-07-16/surrealdb/` — the three SurrealDB docs merged into `benchmark/SURREALDB-RETEST-REPORT_2026-07-16.md`.
- `_archive/consolidation_2026-06-21/` — the 2026-06-21 consolidation snapshot (ingestion, research, storage, synthesis subfolders); several files were promoted out to `research/` and `spec/` and are noted as such in those indexes.
- `_archive/*.md` (top level) — four retired top-level docs (`cytonome-master-reference.md`, `feature-comparison.md`, `yar-product-feature-master.md`, `yar-product-implementation.md`), all superseded by `yar-product-spec.md` per its own front matter.

## External anchors

| Anchor | Path |
|---|---|
| Yar code repo (canonical) | `~/repos/cytognosis/yar_revisions/yar-code-20260705-2354/` — branches `main` and `feat/sqlite-device-store` |
| CAP code path | `~/repos/cytognosis/yar_revisions/yar-code-20260705-2354/backend/cap/` (CapLiteGuard) |
| Reproducible benchmark package | `~/repos/cytognosis/yar_revisions/yar_supervisor_reproducible_benchmark_package/` |
| Yar feature/prioritization CSVs | `~/datasets/cytognosis/yar/data/` (see `DATA-MOVED.md` for the per-file list and one open gap) |
| Project/author working folder | `~/Claude/Projects/Yar/` (this pillar's durable output is promoted here from; not modified by this index) |
| Cytoplex (CAP protocol spec) | `~/repos/cytognosis/docs/03-Products/Cytonome/Cytoplex/` |
