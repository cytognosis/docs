> **Status**: Active
> **Date**: 2026-07-01
> **Author**: @mohammadi
> **Audience**: engineers and reviewers
> **Tags**: `yar`, `research`, `index`

# Yar Research Index (product-facing)

This directory holds **product-facing** feature research. Tool and technology evaluations (the `EVAL-<topic>.md` set) moved to `04-Engineering/yar/research/` on 2026-07-01 so tool evaluations have one canonical home.

## Canonical product docs

- `../yar-product-spec.md` is the canonical Yar product spec (supersedes the retired feature-master and requirements docs, now in `../_archive/`).
- `../YAR_FEATURE_CATALOG.md` is the canonical 62-feature index.

## Feature comparison (v4)

| File | Description |
|------|-------------|
| `yar-unified-feature-comparison-v4.md` | Formal master: scored 12-tool feature comparison (the evidence base) |
| `yar-feature-catalog-public.md` | Community-facing feature labels (feedback instrument) |
| `yar-feature-naming-convention.md` | Three-layer feature naming convention |

> **ADHD-friendly twin archived (2026-07-16):** `yar-unified-feature-comparison-v4-adhd.md` no longer lives in this folder. It was moved to `../_archive/cleanup_2026-07-16/adhd-twins/research/yar-unified-feature-comparison-v4-adhd.md` in the same pass that archived the other spec ADHD twins. Read the base doc above; the readable framing now lives in `yar-feature-research-FINAL-simplified_2026-07-16.md`, its closer current equivalent.

The underlying data matrix (`yar-feature-matrix-v4.csv`) and the prioritization tables now live in the datasets tree at `~/datasets/cytognosis/yar/data/` (see `../DATA-MOVED.md`; the path there was also corrected 2026-07-17). Superseded comparisons (pre-v4, v3) are in `_archive/`.

## Promoted references

| File | What it is |
|------|-----------|
| [`INCORPORATION_MAP.md`](./INCORPORATION_MAP.md) | Spec-integration gap map (promoted from the retired `consolidation_2026-06-21/` snapshot) |
| [`SURREALDB_CODE_AUDIT.md`](./SURREALDB_CODE_AUDIT.md) | SurrealDB code audit (relevant to `spec/SPEC-storage-engine.md`, ACTIVE) |
| [`persona_profiler_frameworks_reference.md`](./persona_profiler_frameworks_reference.md) | Frameworks, standards, and schema reference behind `persona_profiler_schema.yaml` and `spec/SPEC-personas-voice.md` |
| [`persona_profiler_schema.yaml`](./persona_profiler_schema.yaml) | LinkML schema for the persona profiler, companion to the frameworks reference above |

## Session artifacts (2026-07-16)

| File | Description |
|------|-------------|
| `yar-feature-research-FINAL_2026-07-16.md` | Consolidates the v4 comparison, prioritization v1, naming convention, public catalog, and salvage map into one founder-facing reference (does not replace the sources) |
| `yar-feature-research-FINAL-simplified_2026-07-16.md` | Plain-language companion to FINAL |
| `yar-framework-assessment_2026-07-16.md` | Long-term app framework recommendation (Flutter + flutter_rust_bridge) |
| `yar-salvage-reconciliation-map_2026-07-16.md` | Repo A (Tauri, canonical) vs Repo B (legacy Flutter) salvage analysis ahead of the 7/27 YC deadline |

See each file's own "Related documents" footer for the full cross-link chain.

## Related

- Tool evaluations: `04-Engineering/yar/research/` (`EVAL-<topic>.md` + deep-dive references)
- Prior internal prioritization writeup: `yar-internal-prioritization-v1.md`
- Specs referenced by this research: [`../spec/README.md`](../spec/README.md)
- Storage/benchmark evidence: [`../benchmark/README.md`](../benchmark/README.md)
- Salvage-map source repos: `~/repos/cytognosis/yar_revisions/yar-code-20260705-2354/` (Repo A, `main` + `feat/sqlite-device-store`); legacy Repo B per the salvage map

[Up: Yar master index](../README.md)
