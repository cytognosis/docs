> **Status**: Active
> **Date**: 2026-07-19
> **Author**: @mohammadi
> **Audience**: engineers and reviewers
> **Tags**: `yar`, `research`, `index`

# Yar Research Index (product-facing)

This directory holds **product-facing** feature research and planning. Tool and technology evaluations (the `EVAL-<topic>.md` set) live in `04-Engineering/yar/research/` (one canonical home since 2026-07-01).

[Up: Yar master index](../README.md)

## The canonical feature chain (read in this order)

| # | File | Role |
|---|------|------|
| 1 | [`features.json`](./features.json) | **Machine-readable source of truth**: 6 domains, 19 clusters, 69 features, status + gated flags |
| 2 | [`FEATURE-HIERARCHY.md`](./FEATURE-HIERARCHY.md) | Human-readable hierarchy (v6): the 3-level tree, cluster rationale, status rollup |
| 3 | [`../YAR_FEATURE_CATALOG.md`](../YAR_FEATURE_CATALOG.md) | Canonical front door: 69 features by build wave, IPS scores, feature-to-spec map |
| 4 | [`yar-unified-feature-comparison-v4.md`](./yar-unified-feature-comparison-v4.md) | The scored evidence base (competitor comparison + AI-Fit); F63-F69 are post-matrix additions |
| 5 | [`yar-feature-hierarchy.csv`](./yar-feature-hierarchy.csv) | Flat CSV of the hierarchy (for tooling) |

Interactive views: [`../assets/viz/yar-feature-tree.html`](../assets/viz/yar-feature-tree.html) plus the two SVGs beside it.

## Wave 0 planning suite (2026-07-19)

Produced with the Wave 0 spec suite; each carries a spec-refresh addendum with the founder decisions of 2026-07-19.

| File | Description |
|------|-------------|
| [`FEATURE-VERIFICATION.md`](./FEATURE-VERIFICATION.md) | Verification of 8 proposed capabilities against the taxonomy; confirmed gaps F65-F69 |
| [`SPECS-INVENTORY.md`](./SPECS-INVENTORY.md) | The 22-file spec inventory and the dependency-ordered build list the Wave 0 suite followed |
| [`EFFORT-ESTIMATES.md`](./EFFORT-ESTIMATES.md) | Per-component effort (revised total about 146-270 eng-weeks after the spec suite) |
| [`DEPENDENCY-GRAPH.md`](./DEPENDENCY-GRAPH.md) | 22-node task DAG: foundations, gates, pipeline, layered features |
| [`YAR-WAVE-ROADMAP.md`](./YAR-WAVE-ROADMAP.md) | Consolidated roadmap: waves, quarterly timeline, team scenarios |
| [`CODING-AGENT-PRODUCTIVITY.md`](./CODING-AGENT-PRODUCTIVITY.md) | Cited coding-agent productivity multipliers behind the timeline scenarios |

## Feature research and naming

| File | Description |
|------|-------------|
| [`yar-feature-research-FINAL_2026-07-16.md`](./yar-feature-research-FINAL_2026-07-16.md) | Founder-facing consolidation of the v4 comparison, prioritization, naming, and salvage map |
| [`yar-feature-research-FINAL-simplified_2026-07-16.md`](./yar-feature-research-FINAL-simplified_2026-07-16.md) | Plain-language companion to FINAL |
| [`yar-internal-prioritization-v1.md`](./yar-internal-prioritization-v1.md) | IPS scoring and wave assignment (v1.1 founder-elevated Wave 1) |
| [`yar-feature-naming-convention.md`](./yar-feature-naming-convention.md) | Three-layer feature naming convention (affirming label, construct tag, domain code) |
| [`yar-feature-catalog-public.md`](./yar-feature-catalog-public.md) | Community-facing feature labels (feedback instrument) |
| [`yar-feature-feedback.html`](./yar-feature-feedback.html) | The feedback instrument page (pairs with the public catalog and the website voting dashboard) |
| [`COMPS-MASTER-TABLE.md`](./COMPS-MASTER-TABLE.md) | Comp-by-comp coverage map across the 47 evaluated tools |

## Decision records (historical, kept on purpose)

| File | Decision it records |
|------|---------------------|
| [`CANONICAL-EDITS-SPEC.md`](./CANONICAL-EDITS-SPEC.md) | Decisions A-G (2026-07-18): ND-only identity, F63/F64, CSP naming, fully free |
| [`yar-salvage-reconciliation-map_2026-07-16.md`](./yar-salvage-reconciliation-map_2026-07-16.md) | Repo A vs Repo B: port nothing from legacy before the YC deadline |

Removed 2026-07-19 (superseded, retrievable from git history): `yar-framework-assessment_2026-07-16.md` (recommended Flutter + flutter_rust_bridge; overruled by the founder decision for Tauri v2 on phone and desktop, recorded in `../spec/SPEC-multiplatform-delivery.md`).

## Promoted references

| File | What it is |
|------|-----------|
| [`INCORPORATION_MAP.md`](./INCORPORATION_MAP.md) | Spec-integration gap map (see `../YAR_FEATURE_CATALOG.md` Section 8 for current status) |
| [`SURREALDB_CODE_AUDIT.md`](./SURREALDB_CODE_AUDIT.md) | SurrealDB code audit (context for `../spec/SPEC-storage-engine.md`) |
| [`persona_profiler_frameworks_reference.md`](./persona_profiler_frameworks_reference.md) | Frameworks and standards behind `persona_profiler_schema.yaml` and `../spec/SPEC-personas-voice.md` |
| [`persona_profiler_schema.yaml`](./persona_profiler_schema.yaml) | LinkML schema for the persona profiler |

## Data pointers

The feature/prioritization CSV tables live in the datasets tree at `https://github.com/cytognosis/datasets/tree/main/cytognosis/yar/data` (see [`../DATA-MOVED.md`](../DATA-MOVED.md)). Superseded comparisons (pre-v4, v3) and the retired ADHD twins live in git history (the on-disk `_archive/` was retired).

## Related

- Specs: [`../spec/README.md`](../spec/README.md)
- Benchmarks: [`../benchmark/README.md`](../benchmark/README.md)
- Tool evaluations: `04-Engineering/yar/research/`
- Canonical code repo: `https://github.com/cytognosis/Yar`
