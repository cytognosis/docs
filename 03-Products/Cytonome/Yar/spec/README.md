> **Status**: Active
> **Date**: 2026-07-17
> **Author**: @mohammadi (research agent)
> **Audience**: engineers, stakeholders
> **Tags**: `yar`, `spec`, `index`

# Yar Spec Index

**BLUF:** This folder holds Yar's 14 formal engineering specs plus 6 storage/safety session artifacts from 2026-07-16 and 2 supporting guides. Two specs are `active` (data-sovereignty, storage-engine); the rest are `draft` pending build; the two safety modules and the new safety checkpoint are `design-final` but deferred post-YC. The `adhd/` easy-read twins that used to sit here were archived 2026-07-16 (see `../_archive/cleanup_2026-07-16/adhd-twins/spec/`); `adhd/` is now an empty placeholder, not a live section.

[Up: Yar master index](../README.md)

## Core specs

| File | Purpose | Status | Date |
|---|---|---|---|
| [SPEC-CSP.md](./SPEC-CSP.md) | Cytonome Sensor Protocol — universal sensor adapter, "MCP for sensors" | draft | 2026-06-21 |
| [SPEC-data-sovereignty.md](./SPEC-data-sovereignty.md) | Data ownership, export, and residency guarantees | active | 2026-07-06 |
| [SPEC-edge-ai-hybrid.md](./SPEC-edge-ai-hybrid.md) | On-device / cloud hybrid inference split | draft | 2026-06-22 |
| [SPEC-multi-agent.md](./SPEC-multi-agent.md) | Three-agent brainmap loop (placer, reviser, side-thread) | draft | 2026-06-21 |
| [SPEC-neurobehavioral-axes.md](./SPEC-neurobehavioral-axes.md) | Dimensional neurobehavioral axis substrate | draft | 2026-06-22 |
| [SPEC-personas-voice.md](./SPEC-personas-voice.md) | Adaptive persona, relationship stance, on-device TTS (Kokoro) | draft | 2026-06-22 |
| [SPEC-sensor-menstrual.md](./SPEC-sensor-menstrual.md) | Menstrual/reproductive-cycle sensing (Cytoscope-owned science) | draft | 2026-06-22 |
| [SPEC-sensor-physiological.md](./SPEC-sensor-physiological.md) | Physiological/passive-sensing modalities (Cytoscope-owned science) | draft | 2026-06-22 |
| [SPEC-sensor-social-interaction.md](./SPEC-sensor-social-interaction.md) | Temporal social-interaction sensing (Cytoscope-owned science) | draft | 2026-06-22 |
| [SPEC-sensor-speech-mentalstate.md](./SPEC-sensor-speech-mentalstate.md) | Speech mental-state sensor (Cytoscope-owned science) | draft | 2026-06-22 |
| [SPEC-storage-engine.md](./SPEC-storage-engine.md) | Storage engine decision: SQLite wins 10k rows, FalkorDB wins 100k | active | 2026-06-21 |
| [SPEC-sync-protocol.md](./SPEC-sync-protocol.md) | Op-log sync protocol across devices | draft | 2026-06-21 |

## Safety and governance (session artifacts, 2026-07-16)

| File | Purpose | Status | Date |
|---|---|---|---|
| [privacy-boundary-spec.md](./privacy-boundary-spec.md) | Privacy boundary rulebook; hard limits on what leaves the device | design-final (deferred post-YC) | revised 2026-07-16 |
| [MODULE-crisis-detection.md](./MODULE-crisis-detection.md) | Crisis-detection check; depends on privacy-boundary-spec | design-final (deferred post-YC) | revised 2026-07-16 |
| [SAFETY-CHECKPOINT_2026-07-16.md](./SAFETY-CHECKPOINT_2026-07-16.md) | Checkpoint closing both safety pieces for post-YC resume | design-final (deferred post-YC) | 2026-07-16 |

See each file's own "Related documents" footer for the cross-link chain between these three.

## Storage and sync (session artifacts, 2026-07-16)

| File | Purpose | Status | Date |
|---|---|---|---|
| [ANYSYNC-FIT-ASSESSMENT_2026-07-16.md](./ANYSYNC-FIT-ASSESSMENT_2026-07-16.md) | Any-Sync fit assessment against SPEC-sync-protocol and SPEC-storage-engine | assessment | 2026-07-16 |
| [STORAGE_BENCHMARK_TRACKER.md](./STORAGE_BENCHMARK_TRACKER.md) | Living master status table for all storage engines and sync options; open decisions O-1 through O-8 | draft (refreshed) | 2026-07-16 |

Full benchmark evidence for these decisions lives in [`../benchmark/`](../benchmark/README.md) — see especially `SURREALDB-PATCH11-VERDICT_2026-07-16.md` and `SURREALDB-RETEST-REPORT_2026-07-16.md`.

## Supporting guides

| File | Purpose | Status | Date |
|---|---|---|---|
| [STORAGE-ENGINE-RECOMMENDATION.md](./STORAGE-ENGINE-RECOMMENDATION.md) | Storage engine recommendation for Yar v0.1 | Active | 2026-07-10 |
| [SurrealDB-tuning-and-graphrag-guide.md](./SurrealDB-tuning-and-graphrag-guide.md) | Troubleshooting T1-T12, SCHEMAFULL schema, FTS/HNSW index syntax, GraphRAG query patterns | Draft | 2026-06-21 |
| [SurrealDB-advanced-optimization-and-versions.md](./SurrealDB-advanced-optimization-and-versions.md) | Version changelog 3.1.0-3.1.5, max-performance checklist, PATCH11 docker-compose changes | Draft | 2026-06-22 |
| [YAR-CLIENT-EVAL.md](./YAR-CLIENT-EVAL.md) | Evaluation of the `yar-code-20260705-2354` client against these specs | Active | 2026-07-10 |

## Archive placeholder

`adhd/` is an empty directory. The easy-read spec twins that used to live here were archived 2026-07-16 to `../_archive/cleanup_2026-07-16/adhd-twins/spec/`. Treat the core specs above as the current source; the archive is historical only.

## Cross-links

- Feature-to-spec map: [`../yar-product-spec.md`](../yar-product-spec.md) Section 7.
- Benchmark evidence for storage decisions: [`../benchmark/README.md`](../benchmark/README.md).
- Research chain (framework/AnySync assessments): [`../research/README.md`](../research/README.md).
- CAP code path (engineering): `~/repos/cytognosis/yar_revisions/yar-code-20260705-2354/backend/cap/`.
