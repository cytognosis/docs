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
| `yar-unified-feature-comparison-v4-adhd.md` | ADHD-friendly twin of the formal master |
| `yar-feature-catalog-public.md` | Community-facing feature labels (feedback instrument) |
| `yar-feature-naming-convention.md` | Three-layer feature naming convention |

The underlying data matrix (`yar-feature-matrix-v4.csv`) and the prioritization tables now live in the datasets tree at `~/datasets/cytognosis/products/yar/` (see `../DATA-MOVED.md`). Superseded comparisons (pre-v4, v3) are in `_archive/`.

## Promoted references

| File | What it is |
|------|-----------|
| `INCORPORATION_MAP.md` | Spec-integration gap map (promoted from the retired `consolidation_2026-06-21/` snapshot) |
| `SURREALDB_CODE_AUDIT.md` | SurrealDB code audit (relevant to `spec/SPEC-storage-engine.md`, DRAFT) |

## Related

- Tool evaluations: `04-Engineering/yar/research/` (`EVAL-<topic>.md` + deep-dive references)
- Prior internal prioritization writeup: `yar-internal-prioritization-v1.md`
