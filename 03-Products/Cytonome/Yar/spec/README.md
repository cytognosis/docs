> **Status**: Active
> **Date**: 2026-07-19
> **Author**: @mohammadi (research agent)
> **Audience**: engineers, stakeholders
> **Tags**: `yar`, `spec`, `index`

# Yar Spec Index

**BLUF:** This folder holds Yar's 20 formal core engineering specs (12 pre-existing plus the 8-spec Wave 0 suite added or updated 2026-07-19), 2 safety/governance specs, 6 storage/safety session artifacts, and 2 supporting guides. The Wave 0 suite and its three companion updates were founder-approved and promoted to `active` on 2026-07-19, joining data-sovereignty and storage-engine; the two safety modules stay `design-final`, deferred post-YC. The `adhd/` easy-read twins were retired 2026-07-16 and now live only in git history.

[Up: Yar master index](../README.md)

## Core specs

| File | Purpose | Status | Date |
|---|---|---|---|
| [SPEC-CSP.md](./SPEC-CSP.md) | Cytonome Sensor Protocol: universal sensor adapter, "MCP for sensors" | draft | 2026-06-21 |
| [SPEC-data-sovereignty.md](./SPEC-data-sovereignty.md) | Data ownership, export, and residency guarantees | active | 2026-07-06 |
| [SPEC-edge-ai-hybrid.md](./SPEC-edge-ai-hybrid.md) | On-device / cloud hybrid inference split | draft | 2026-06-22 |
| [SPEC-multi-agent.md](./SPEC-multi-agent.md) | Supervisor-worker orchestration; canonical agent naming (Supervisor, Interviewer, Transcriber, Proofreader, Mind-mapper) | active | 2026-07-19 |
| [SPEC-neurobehavioral-axes.md](./SPEC-neurobehavioral-axes.md) | Dimensional neurobehavioral axis substrate | draft | 2026-06-22 |
| [SPEC-personas-voice.md](./SPEC-personas-voice.md) | Adaptive persona, relationship stance, on-device TTS (Kokoro); one persona on the Interviewer, workers voiceless | active | 2026-07-19 |
| [SPEC-sensor-menstrual.md](./SPEC-sensor-menstrual.md) | Menstrual/reproductive-cycle sensing (Cytoscope-owned science) | draft | 2026-06-22 |
| [SPEC-sensor-physiological.md](./SPEC-sensor-physiological.md) | Physiological/passive-sensing modalities (Cytoscope-owned science) | draft | 2026-06-22 |
| [SPEC-sensor-social-interaction.md](./SPEC-sensor-social-interaction.md) | Temporal social-interaction sensing (Cytoscope-owned science) | draft | 2026-06-22 |
| [SPEC-sensor-speech-mentalstate.md](./SPEC-sensor-speech-mentalstate.md) | Speech mental-state sensor (Cytoscope-owned science) | draft | 2026-06-22 |
| [SPEC-storage-engine.md](./SPEC-storage-engine.md) | Storage engine decision: SQLite wins 10k rows, FalkorDB wins 100k | active | 2026-06-21 |
| [SPEC-sync-protocol.md](./SPEC-sync-protocol.md) | Cross-device sync (F68); O-1 resolved: any-sync transport-only, Yar reducer authoritative, Loro CRDT lib | active | 2026-07-19 |

## Wave 0 spec suite (added 2026-07-19)

Dependency-ordered per `../research/SPECS-INVENTORY.md`. All were founder-approved and promoted to `active` on 2026-07-19; each carries its own open-questions section with recommendations.

| File | Purpose | Feature anchors |
|---|---|---|
| [SPEC-petkg-longmemory.md](./SPEC-petkg-longmemory.md) | PeT (Personal Temporal knowledge graph) + long-term memory: bitemporal facts on SQLite/FalkorDB; cytomem schema convergence | F67, F66 |
| [SPEC-cactus-routing.md](./SPEC-cactus-routing.md) | Model routing: simple local-vs-cloud selection (Cactus removed per founder decision 2026-07-19; filename kept for link stability); Gemma 4 Apache-2.0 confirmed | all agents |
| [SPEC-transcriber-agent.md](./SPEC-transcriber-agent.md) | Dictation STT worker: whisper.cpp/WhisperKit edge, faster-whisper server; raw audio device-only; speaker_hint seam for F69 | F01, F02, F03, F13 |
| [SPEC-proofreading-agent.md](./SPEC-proofreading-agent.md) | Proofreader worker: gazetteer, GLiNER/spaCy, Instructor tiers; DSPy offline-only; dual CAP gates | F33, F58, F09 seam |
| [SPEC-mindmapping-agent.md](./SPEC-mindmapping-agent.md) | Mind-mapper worker (flagship): LLM placement + conservatism contract; conservative structure revision | F13, F14, F15, F31, F60 |
| [SPEC-browser-extension.md](./SPEC-browser-extension.md) | MV3 side-panel extension: WADM annotation, Memex parity checklist, paired localhost handoff | F50, F59, F16 |
| [SPEC-multiplatform-delivery.md](./SPEC-multiplatform-delivery.md) | Thin adoption of the org interface templates; Tauri v2 on phone and desktop (founder-decided 2026-07-19) | F41 delivery |
| [SPEC-meeting-diarization.md](./SPEC-meeting-diarization.md) | Botless meeting diarization: pyannote/diart/FluidAudio stack; consent-first UX; Phase 0 internal use now, counsel review gates public release only | F69 (phased) |

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

Full benchmark evidence for these decisions lives in [`../benchmark/`](../benchmark/README.md); see especially `SURREALDB-PATCH11-VERDICT_2026-07-16.md` and `SURREALDB-RETEST-REPORT_2026-07-16.md`.

## Supporting guides

| File | Purpose | Status | Date |
|---|---|---|---|
| [STORAGE-ENGINE-RECOMMENDATION.md](./STORAGE-ENGINE-RECOMMENDATION.md) | Storage engine recommendation for Yar v0.1 | Active | 2026-07-10 |
| [SurrealDB-tuning-and-graphrag-guide.md](./SurrealDB-tuning-and-graphrag-guide.md) | Troubleshooting T1-T12, SCHEMAFULL schema, FTS/HNSW index syntax, GraphRAG query patterns | Draft | 2026-06-21 |
| [SurrealDB-advanced-optimization-and-versions.md](./SurrealDB-advanced-optimization-and-versions.md) | Version changelog 3.1.0-3.1.5, max-performance checklist, PATCH11 docker-compose changes | Draft | 2026-06-22 |
| [YAR-CLIENT-EVAL.md](./YAR-CLIENT-EVAL.md) | Evaluation of the Tauri reference client (the `yar-code-20260705-2354` snapshot, since promoted to the canonical `~/repos/cytognosis/Yar`) against these specs | Active | 2026-07-10 |

## Retired content

The easy-read ADHD spec twins were retired 2026-07-16; the on-disk `_archive/` was later removed. Both are retrievable from git history. Treat the core specs above as the current source.

## Cross-links

- Feature-to-spec map: [`../yar-product-spec.md`](../yar-product-spec.md) Section 7.
- Benchmark evidence for storage decisions: [`../benchmark/README.md`](../benchmark/README.md).
- Research chain (framework/AnySync assessments): [`../research/README.md`](../research/README.md).
- CAP code path (engineering): `~/repos/cytognosis/Yar/backend/cap/` (canonical repo; formerly the `yar-code-20260705-2354` snapshot).
