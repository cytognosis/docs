# Yar Product Spec (agent brief)

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: engineers, stakeholders
> **Tags**: `yar`, `product`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

> **Variants**: Agent seed (this doc) - Technical (yar-product-spec.md) - Readable (yar-product-spec.md)

> **Status:** Active · **Date:** 2026-07-01 · Self-contained brief for a fresh agent picking up Yar. Companion to `yar-product-spec.md` (canonical) and `yar-product-spec.readable.md` (ADHD).

## Goal

Yar (Your AI Representative) is **Cytonome v0.1**, a local-first, voice-aware, AI-native cognitive companion built by and for neurodivergent adults. It consumes messy voice or text, structures it with on-device AI into a typed personal knowledge graph, and helps the user plan, execute, and stay self-aware behind a hard safety boundary (CAP). It is the consumer wedge of the Cytognosis platform, destined for the for-profit PBC arm.

## Scope

- **In scope (Yar):** the app, the three pillars (adaptive personas, CSP sensor protocol, branching brainmap), the 62-feature catalog, the app-side sensor surface, CAP-Lite integration.
- **Out of scope (other projects):** sensor science (Cytoscope), the Cytoverse map and cytos schemas (Cytos, Neuroverse), org infrastructure (Infrastructure).

## Decided and done (2026-07-01 consolidation)

- Canonical product spec is `yar-product-spec.md`. It supersedes and absorbs `yar-product-feature-master.md`, `yar-product-implementation.md`, `cytonome-master-reference.md`, and `feature-comparison.md` (archived in `_archive/` with forward links).
- Feature index is `YAR_FEATURE_CATALOG.md` (62 features, F01-F62, six domains, waves, IPS, CU-1..CU-8).
- Tool evaluations consolidated to `04-Engineering/yar/research/` (concise `EVAL-<topic>.md` plus deep-dive references).
- 14 formal specs live in `spec/` with ADHD variants in `spec/adhd/`. Cytoplex (CAP) docs are in `Cytoplex/`.
- Primary tables live in the datasets tree (`~/datasets/cytognosis/products/yar/`).
- Persona voice is on-device Kokoro TTS.

## Open questions and pending work

1. **Storage engine (blocking a spec):** `SPEC-storage-engine` is DRAFT pending the **SurrealDB v3.1.5 retest**. Do not promote it out of DRAFT until the retest passes.
2. **SurrealDB SDK naming:** reconcile `AsyncSurreal` vs `AsyncSurrealDB` to the pinned SDK class at the retest (target `AsyncSurreal`); see `00-CONSOLIDATION/CONFLICTS.md` [CONFLICT-2].
3. **`SPEC-data-sovereignty.md`:** not yet authored. Create it from `SPEC-sync-protocol` §5 (Solid TR ledger) plus post-quantum crypto and encryption-at-rest; add an ADHD variant.
4. **ADHD-variant coverage:** confirm each spec has a `spec/adhd/` twin; `SurrealDB-advanced-optimization-and-versions.md` is missing one.
5. **Spec-integration gaps (`research/INCORPORATION_MAP.md`):** fold benchmark numbers into `SPEC-storage-engine`; reconcile CapLiteGuard in `SPEC-multi-agent`; add the cytos KG schema to `SPEC-CSP`.
6. **Pre-existing stale links:** about 65 `docs/cytonome/yar/...` links need a dedicated repair pass (not caused by this run).
7. **Sensor-science specs** (`SPEC-sensor-*`): the Cytoscope agent owns moving these out of Yar.

## Source-of-truth files

- Canonical spec: `03-Products/Cytonome/Yar/yar-product-spec.md`
- Feature index: `03-Products/Cytonome/Yar/YAR_FEATURE_CATALOG.md`
- Specs: `03-Products/Cytonome/Yar/spec/` (+ `spec/adhd/`)
- Engineering: `04-Engineering/yar/` (sensors, integrations, reports, research)
- Safety/protocol: `03-Products/Cytonome/Cytoplex/` (`cap-readme.md`, `spec/`)
- Consolidation state: `~/Claude/Projects/Yar/00-CONSOLIDATION/` (`STATE.md`, `PHASE4-PLAN.md`, `CONFLICTS.md`, `OPEN_QUESTIONS.md`)

## Success criteria

A change is on-track if it keeps the spec consistent with the 62-feature catalog, honors CAP (local-first, no diagnosis, confirm before external writes), uses the ADHD paper's vocabulary, keeps `SPEC-storage-engine` DRAFT until the retest, and adds an ADHD variant for any new spec.

## Start commands

```bash
# Repos and branch
cd ~/repos/cytognosis/docs && git checkout reorg/yar-2026-07-01
# Read the canonical spec, then the feature catalog
sed -n '1,60p' 03-Products/Cytonome/Yar/yar-product-spec.md
# The Yar app and CAP repos
cd ~/repos/cytognosis/Yar && git checkout reorg/yar-2026-07-01
cd ~/repos/cytognosis/cytoplex && git checkout reorg/yar-2026-07-01
```
