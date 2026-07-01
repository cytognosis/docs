> **Status**: Draft
> **Date**: 2026-06-22
> **Author**: Cytognosis Foundation
> **Audience**: engineers
> **Tags**: `yar`, `consolidation`, `code-sweep`, `incorporation`, `divergence`

# INCORPORATION MAP — Yar Spec Suite vs Codebase

**BLUF**: Seven Cytognosis repos contain implemented artifacts that should be stitched into the Yar spec suite. The most urgent gaps are: the benchmark numbers from `yar_supervisor_reproducible_benchmark_package` are not yet cited in SPEC-storage-engine, the Yar-resident `cap/` package implements a CAP-Lite guard that diverges architecturally from what SPEC-multi-agent describes, and the `cytos` KG schema (SOSA/Biolink sensing graph) is entirely absent from SPEC-CSP.

---

## 1. Repo: `Yar/`

**Maturity**: Implemented (Python backend) + Partial (Flutter/Dart mobile). Tests passing per `__pycache__` evidence. Core FastAPI backend callable via `yar serve`.

### 1.1 Python backend (`Yar/src/yar/`)

| Module path | What it is |
|---|---|
| `src/yar/models/voice_affect.py` | Pydantic models: `AffectState`, `AffectTrend`, `VoiceAffectSignal`, `VoiceAffectPolicy`, `VoiceAffectEvent`, `VoiceAffectContextHint`, `VoiceAffectFeatureFlags`, `VoiceAffectConstants` |
| `src/yar/models/yar_object.py` | `YarObject`, `YarObjectType` (17-type enum: Note/Task/Idea/Project/Person/Paper/Webpage/Decision/Reflection/MessageDraft/Author/Dataset/Code/Method/Model/Annotation/Collection/Concept), `ObjectUpdateRequest` |
| `src/yar/models/voice.py` | `VoiceIntentType`, `VoiceIntent`, `CAPMobileDirective`, `VoiceTurnRequest`, `VoiceSuggestedAction` |
| `src/yar/models/planning.py` | `PersonaMode` (5-mode enum: assistant/buddy/guardian/coach/quiet), `PersonaSettings`, `DailyAnchor`, `DailyPlan` |
| `src/yar/models/wadm.py` | W3C Web Annotation Data Model: `WADMAnnotation`, `WADMBody`, `WADMTarget`, `TextQuoteSelector`, `TextPositionSelector`, `AnnotationCaptureRequest`, `AnnotationCaptureResponse` |
| `src/yar/storage/graph_store.py` | Abstract `GraphStore` interface (12 methods): create/list/get/search/update/delete objects, create/delete/list links, get object detail, register/list schemas |
| `src/yar/storage/sqlite_store.py` | `SQLiteGraphStore` (concrete) — tables: `objects`, `links`, `captures`, `execution_reports`, `schemas`, `anytype_write_plans` |
| `src/yar/core/affect/tracker.py` | `EmotionTrackerService` + `RawAffectObservation` (dataclass) — EMA smoothing + state mapping + trend detection pipeline |
| `src/yar/core/model_router.py` | `ModelRouterConfig` (provider: `ollama_cli`, default model: `gemma4:e4b`), `StubObjectRouter` |
| `src/yar/api/routes_persona.py` | REST endpoints: `GET /persona`, `PATCH /persona`, `GET /persona/modes` |
| `src/yar/integrations/linkml_loader.py` | LinkML schema loader wired to schema registry |
| `src/yar/integrations/anytype/` | Full Anytype MCP adapter (adapter, client, config, mapper, schema_mapper) |

### 1.2 Standalone `cap/` package (`Yar/src/cap/`)

This is a standalone Python package (not a sub-module of `yar`). `yar.cap` bridges to it via re-exports.

| File | What it contains |
|---|---|
| `src/cap/guard.py` | `CapLiteGuard` — deterministic safety/privacy gate. Runs before any model inference. Evaluates: crisis terms (multilingual: English + Farsi), diagnosis terms, treatment advice patterns, intent signals, raw-data sharing. Crisis message: redirects to 1480 (Iran Social Emergency) + findahelpline.com. |
| `src/cap/models.py` | `GuardDecision`, `GuardDecisionValue` |
| `src/cap/primitives.py` | CAP primitive building blocks |
| `src/cap/protocols.py` | `CaptureProtocol`, `WriteOperationProtocol`, `WritePlanProtocol` |
| `src/cap/data/cap_core_policy.json` | Core CAP policy JSON |
| `src/cap/data/cap_med_policy.json` | Medical-domain CAP policy JSON |

### 1.3 Flutter/Dart mobile (`Yar/apps/mobile/`)

| File | What it is |
|---|---|
| `lib/src/affect/voice_affect_models.dart` | Dart mirrors of Python voice-affect models — `AffectState`, `AffectTrend`, `VoiceAffectSignal`, `VoiceAffectPolicy`, `VoiceAffectEvent`, `VoiceAffectContextHint`, `VoiceAffectEventAck` + constants (`VoiceAffectConstants`) |
| `lib/src/affect/onnx_distilhubert_ser_inference.dart` | On-device SER inference via DistilHuBERT ONNX (`distilhubert-ser-int8-onnx`, `distilhubert-ser-onnx`) — arousal/valence output |
| `lib/src/services/gemma_edge_intent_service.dart` | `GemmaEdgeIntentService` — on-device Gemma 4 E4B intent inference via `flutter_gemma`, chat with `temperature: 0.1`, `topK: 16`, `topP: 0.8` |
| `lib/src/affect/affect_inference.dart` | ONNX inference pipeline for affect |
| `lib/src/audio/microphone_audio_capture_service.dart` | Microphone capture |
| `lib/src/audio/voice_input_service.dart` | Voice input pipeline |

**Key constant divergence (backend vs mobile)**: `VoiceAffectConstants.HOP_MS` = 250 ms (Python backend) vs 1500 ms (Dart mobile). `MIN_SPEECH_MS` = 800 ms (Python) vs 1000 ms (Dart). `TTL_MS` = 120,000 ms (Python) vs 10,000 ms (Dart). `CONFIDENCE_FLOOR` = 0.45 (Python) vs 0.25 (Dart). Model ID: `distilhubert-ser-onnx` (Python) vs `distilhubert-ser-int8-onnx` (Dart).

---

## 2. Repo: `cytoplex/`

**Maturity**: Implemented. Full CAP v1 Python library with gRPC + HTTP/JSON bindings, conformance test suite, benchmarks, and LinkML schema.

### 2.1 Source layout

| Path | What it is |
|---|---|
| `src/cytoplex/runtime/` | Full runtime: `controller.py`, `edge_pep.py`, `mobile_local_pep.py`, `attested_local_pep.py`, `privacy_pdp.py`, `warrants.py`, `retention.py`, `interrupts.py`, `live_model_streaming.py`, `service_mesh.py`, `session_router.py`, `slow_path_classifier.py`, `supervisor_gateway.py`, `workflow_engine.py`, `human_review.py`, `observability.py`, `temporal.py`, `workload_identity.py` |
| `src/cytoplex/security/` | `cap_crypto.py` (canonicalization + signing), `cert_manager.py`, `transparency.py` |
| `src/cytoplex/hardening/` | `policy_engine.py`, `audit_store.py` |
| `src/cytoplex/profiles/cap_med.py` | Medical-domain CAP profile |
| `src/cytoplex/profiles/cap_swe.py` | Software-engineering CAP profile |
| `src/cytoplex/profiles/inheritance.py` | Profile inheritance logic |
| `src/cytoplex/scenarios/therapist_supervisor/` | Complete therapist+supervisor reference scenario: `therapist_agent.py`, `supervisor_agent.py`, `cap_controller.py`, `policies.py`, `psych_results_tool.py`, `transport.py` |
| `src/cytoplex/bindings/grpc_reference/` | gRPC binding (proto + generated Python + adapters): `cap.proto`, `cap_core.py`, `cap_v1_core.py`, `mcp_adapter.py`, `a2a_adapter.py`, `policy_adapter.py`, `telemetry_prov.py`, `schema_validation.py` |
| `src/cytoplex/bindings/http_json/` | HTTP/JSON binding: `cap_v1_types.py`, `http_runtime.py`, `integrations_v1.py`, `validators_v1.py`, `conformance_v1.py` |
| `src/cytoplex/conformance/v1_runner.py` | Conformance test suite including adversarial fixtures |

### 2.2 Schemas

| Path | What it is |
|---|---|
| `schemas/cap.yaml` | Root LinkML schema — imports all domain schemas, defines `CAPSchemaBundle` container |
| `schemas/core.yaml` | Core CAP LinkML types |
| `schemas/domains/authority.yaml` | Authority chain types |
| `schemas/domains/capability.yaml` | `Capability` type |
| `schemas/domains/constraints.yaml` | `OperationalConstraints` |
| `schemas/domains/control.yaml` | `GuardDecision`, `InterruptDecision`, `CAPEnvelope`, `Directive` |
| `schemas/domains/evidence.yaml` | `EvidenceRef`, `ExecutionReport` |
| `schemas/domains/privacy.yaml` | `PrivacyBoundary`, `PrivacyBoundaryDimension` |
| `schemas/domains/profiles.yaml` | Profile definition types |

### 2.3 Policies (JSON)

| Path | What it contains |
|---|---|
| `policies/cap_core_policy.json` | Core CAP policy rules |
| `policies/cap_med_policy.json` | Medical-domain policy rules (overlaps with `cap/data/cap_med_policy.json` in Yar) |

### 2.4 CAP latency budget

The benchmark file at `cytoplex/docs/benchmarks/cap_v1_latency_mobile_budget.json` has been moved to `~/repos/cytognosis/docs/cytonome/cytoplex/benchmarks/cap_v1_latency_mobile_budget.json` (per the stub left in the repo). The docs location was not yet populated at sweep time.

---

## 3. Repo: `cytos/`

**Maturity**: Implemented (KG + genomics + sensing layers). Source layout: `src/cytos/{assets,atlases,cli,datasets,db,genomics,kg,scholarly,services,sources,tagging,validate}`.

### 3.1 BioCypher KG schema (sensing-relevant)

| File | Contents |
|---|---|
| `src/cytos/kg/biocypher/schema_config.yaml` | Biolink-mapped node types: `dataset`, `sequence_variant`, `gene`, `disease`, `cell_type`, `anatomical_entity`, `phenotypic_feature`, `drug`, `protein`, `publication`, `organism_taxon`; edge types: `gene_to_disease_association`, `variant_to_disease_association`, `variant_to_gene_association`, `has_phenotype`, `has_cell_type`, `located_in`, `measured_by` (with `cytos:measured_by` predicate linking to `device`). Uses Biolink 4.x (alignment parquet at `data/normalized/biolink/4.x/CytosBiolinkAlignment.parquet`). |

### 3.2 Archive: SurrealDB adapter

| File | What it contains |
|---|---|
| `archive/surrealdb/schema.py` | SurrealDB schema — legacy, superseded by SQLite stack |
| `archive/surrealdb/client.py` | SurrealDB client — archived |

### 3.3 Active DB adapters

- `src/cytos/db/neo4j/` — Neo4j client + converter
- `src/cytos/db/surrealdb/` — SurrealDB KG store (active, not archived — different from `archive/surrealdb/`)
- `src/cytos/db/soma/` — TileDB-SOMA adapter for single-cell data
- `src/cytos/db/neuro_store/` — Neuro-phenotype store (atlas + harmonize + ingest)
- `src/cytos/db/vcf_store/` — VCF/genomic variant store

### 3.4 Sensing-adjacent schemas

The `configs/sources/sosa_ssn.yaml` and `configs/sources/nwb_core.yaml` files declare SOSA/SSN and NWB as registered schema sources for the cytos pipeline. These are directly relevant to the CSP sensor schema design.

---

## 4. Repo: `cytocast/`

**Maturity**: Implemented (project scaffolding + profile schema).

### 4.1 Key artifact

| File | What it is |
|---|---|
| `profiles/schema/profile_schema.linkml.yaml` | `ProfileManifest` LinkML schema — slots: `id`, `name`, `description`, `project_type`, `project_language`, `dependency_manager`, `environment_strategy`, `compute_backend`, `agents` (`ProfileAgents`: defaults, optional, workflows, metadata). This is a project-scaffold profile, NOT a Yar persona profile. |

**Note**: cytocast is a project-template/copier system. It does not contain Yar user-facing persona definitions. The "profile schema" here governs software project manifests, not conversation personas.

---

## 5. Repo: `yar_supervisor_reproducible_benchmark_package`

**Maturity**: Complete benchmark package with reference results. This is the canonical empirical source for SPEC-storage-engine and SPEC-sync-protocol.

### 5.1 DB benchmark results (PATCH10, verified)

**Winner at 10k workload**: SQLite (score 3.05), then FalkorDB (5.53), then SurrealDB tuned (8.35).
**Winner at 100k workload**: FalkorDB (4.26), then SQLite (5.49), then SurrealDB tuned (9.37).

**PATCH10 p50 latency comparison (10k, RocksDB + HNSW) — ms:**

| operation | falkordb | sqlite | surrealdb_tuned |
|---|---|---|---|
| lexical_search | 0.349 | 0.132 | 3.555 |
| hybrid_rrf | 3.244 | 2.289 | 5.923 |
| vector_search | 2.894 | 2.229 | 2.722 |
| memory_packet | 2.134 | 2.135 | 8.374 |
| task_lookup | 0.573 | 0.579 | 46.003 |
| depth2_context | 0.453 | 0.021 | 2.584 |
| depth3_context | 0.492 | 0.025 | 4.458 |
| project_decisions | 0.435 | 5.102 | 0.732 |
| incremental_write | 4.014 | 0.268 | 6.259 |
| cold_open | 0.783 | 12.432 | 63.654 |

**Decision captured in `reports/Yar_Data_Fabric_Supervisor_Brief_EN.md`:**
- Phone/Laptop MVP: SQLite + FTS5 + sqlite-vec
- Server graph projection: FalkorDB
- SurrealDB: priority GraphRAG projection candidate (not MVP default)
- Sync: Yar op-log / CRDT state (not DB files); MVP = `central_oplog_pull_since_seq`

### 5.2 Sync benchmark edge-case coverage

**Result: 12/12 edge cases passed.**

Covered: idempotency (duplicate_replay, partial_crash_resume), delivery ordering (out_of_order_chunks), chunking/backpressure (chunk_limit_many_small_ops), device lifecycle (new_device_bootstrap, device_reinstall_new_actor), conflict/tombstone (delete_update_race_delete/update_wins), deterministic tie-breaking (same_lamport_tie_break), partition healing (network_partition_bridge), blob/encrypted DAG (star_hub_blob_archive), anti-pattern guard (snapshot_badness_guard).

Not yet covered by executable adapter: real any-sync cluster latency, real Iroh blob transfer, real Loro/Yjs/Automerge document adapters against Yar object schema, mobile OS background limits, encrypted key rotation, malicious peer / Byzantine validation.

---

## 6. Repo: `cytomem/`

**Maturity**: Implemented. Neo4j graph memory engine + MCP server + CLI. Live at bolt://localhost:7687 (7,322 artifacts, 14 repos).

### 6.1 Key artifacts

| File | What it contains |
|---|---|
| `src/cytomem/models.py` | `AssetKind` enum (14 kinds: Component/Environment/Docker/Schema/Skill/Dataset/Model/Paper/Code/Workflow/Document/Plan/Decision/AgentSession), `LifecycleStage` enum (8 stages: draft/described/built/tested/published/archived/stale/superseded), `ArtifactType` enum |
| `src/cytomem/graph/client.py` | Neo4j graph client |
| `src/cytomem/graph/episodes.py` | Episode/memory graph management |
| `src/cytomem/graph/queries.py` | Cypher queries for memory retrieval |
| `src/cytomem/graph/local_embedder.py` | Local embedding for semantic search |
| `src/cytomem/mcp/server.py` | MCP server (tools: cytomem_recall, cytomem_task_add/update/delete/list, cytomem_backlog_*, cytomem_link_*) |
| `configs/tracks.yaml` | Track taxonomy: cytoverse / cytonome / cytoscope / toolchain / operational / research + overlays |

---

## 7. Repo: `neuro-pheno/`

**Maturity**: Empty or deleted at sweep time. No files found. Likely merged elsewhere.

---

## 8. Spec-to-Artifact Master Table

| Spec | Concrete artifacts to incorporate | Divergence / Risk flag |
|---|---|---|
| **SPEC-multi-agent** | `Yar/src/cap/guard.py` (CapLiteGuard — the actual on-device gate); `cytoplex/src/cytoplex/scenarios/therapist_supervisor/` (reference scenario matching the therapist+supervisor model); `cytoplex/src/cytoplex/bindings/grpc_reference/cap.proto` (gRPC wire schema); `cytoplex/src/cytoplex/runtime/mobile_local_pep.py` (mobile PEP implementation) | **DIVERGENCE**: The `Yar/src/cap/` package is a **standalone deterministic term-matching guard**, not the full supervisor-worker topology the spec describes. Spec Section 2 defines a `GemmaEdgeIntentService` (Gemma 4 E4B) + a 26B MoE supervisor. The actual mobile code has the Gemma edge service (`apps/mobile/lib/src/services/gemma_edge_intent_service.dart`) but uses `GemmaRouterStub` as the server-side fallback in tests, not a live supervisor. The `StubObjectRouter` in `model_router.py` defaults to `gemma4:e4b` but only as CLI stub. No supervisor agent is wired up yet. |
| **SPEC-CSP** | `cytos/configs/sources/sosa_ssn.yaml` (SOSA/SSN as registered source schema); `cytos/kg/biocypher/schema_config.yaml` (cytos KG schema with `cytos:measured_by` edge and `device` node type, directly relevant to sensor-to-dataset links); `Yar/src/yar/models/voice_affect.py` (VoiceAffectPolicy — the most complete privacy-attestation model in the codebase, should be the reference model for CSP consent attestation) | **DIVERGENCE**: SPEC-CSP references `04-Engineering/cytos/sensing-schema/unified-sensor-report.md` but no SOSA/SSN schema is implemented in Yar itself. The cytos source-schema configs (`sosa_ssn.yaml`, `nwb_core.yaml`) are declared but not imported into any Yar adapter. CSP spec assumes a `SensorDescriptor` LinkML class; this does not exist yet in any repo. |
| **SPEC-storage-engine** | `yar_supervisor_reproducible_benchmark_package/reference_results/surreal_tuned_patch10_final_comparison.md` (all p50 latency numbers, decision scores); `reports/Yar_Data_Fabric_Supervisor_Brief_EN.md` (final architecture decision); `sync_benchmark/EDGE_COVERAGE.md` (12/12 pass matrix); `Yar/src/yar/storage/sqlite_store.py` (live schema: objects/links/captures/execution_reports/schemas tables); `Yar/src/yar/storage/graph_store.py` (abstract `GraphStore` interface) | **DIVERGENCE**: SPEC-storage-engine mentions `LadybugDB` as a front-runner alongside SQLite and SurrealDB. The benchmark package does NOT include a LadybugDB result. The definitive decision in the benchmark report is SQLite (10k) + FalkorDB (100k/server); LadybugDB appears only in the spec, not in measured results. Spec should either cite LadybugDB pending-benchmark status or remove it from the front-runner pair. |
| **SPEC-sync-protocol** | `sync_benchmark/EDGE_COVERAGE.md` (12/12 edge-case matrix with gap list); `sync_benchmark/yar_sync_edge_bench.py` (executable benchmark harness); `reports/Yar_Data_Fabric_Supervisor_Brief_EN.md` (sync phase table: MVP=central_oplog_pull_since_seq, local-first=p2p_version_vector_delta, blob=any-sync/Iroh) | No major divergence found but real Iroh/Loro/Automerge adapters not yet wired. |
| **SPEC-edge-ai-hybrid** | `Yar/apps/mobile/lib/src/services/gemma_edge_intent_service.dart` (actual GemmaEdgeIntentService with temperature/topK/topP params — temperature:0.1, topK:16, topP:0.8); `Yar/apps/mobile/lib/src/affect/onnx_distilhubert_ser_inference.dart` (on-device SER inference, confirmed model: `distilhubert-ser-int8-onnx`); `cytoplex/src/cytoplex/runtime/mobile_local_pep.py` (mobile-tier CAP PEP) | **DIVERGENCE**: Spec says edge-tier latency target is under 200ms per op. The `VoiceAffectConstants` constants differ between backend and mobile: backend `HOP_MS=250ms`, mobile `HOP_MS=1500ms`. Backend `TTL_MS=120,000ms`, mobile `TTL_MS=10,000ms`. These are not annotated as intentional tier differences in either codebase. Spec also references CAP latency budget JSON but the file has been moved and the docs destination was not populated at sweep time. |
| **SPEC-personas-voice** | `Yar/src/yar/models/planning.py` (`PersonaMode` enum: assistant/buddy/guardian/coach/quiet, `PersonaSettings`, `DailyPlan`); `Yar/src/yar/api/routes_persona.py` (live REST API: GET/PATCH /persona, GET /persona/modes); `Yar/apps/mobile/lib/src/services/gemma_edge_intent_service.dart` (`generateAssistantReply` with `persona` and `affectPromptAddition` params) | **DIVERGENCE**: The spec defines a rich `PersonaConfig` LinkML class. The implementation uses a simple `PersonaMode` StrEnum with 5 modes. The implemented modes (assistant/buddy/guardian/coach/quiet) partially overlap the spec's persona system but the spec adds ND-tuned personas (focus, rest, crisis) not present in the enum. ElevenLabs integration is spec-designed but not yet implemented — the mobile uses `flutter_gemma` TTS, not ElevenLabs. Kokoro is implemented (`src/yar/core/tts/kokoro_english.py`) and matches the fallback design. |
| **SPEC-sensor-speech-mentalstate** | `Yar/src/yar/models/voice_affect.py` (full pydantic model suite, `DEFAULT_MODEL_ID="distilhubert-ser-onnx"`); `Yar/src/yar/core/affect/tracker.py` (`EmotionTrackerService`, `RawAffectObservation`); `Yar/apps/mobile/lib/src/affect/onnx_distilhubert_ser_inference.dart` (on-device ONNX inference pipeline); `Yar/apps/mobile/lib/src/affect/affect_model_installer.dart` (model download and install) | Maturity divergence only: desktop backend uses `distilhubert-ser-onnx`; mobile uses `distilhubert-ser-int8-onnx` (quantized). Neither the spec nor the code documents this as intentional — should be explicit. |
| **SPEC-multi-agent (CAP)** | `cytoplex/schemas/cap.yaml` + all `schemas/domains/*.yaml` (7 domain schemas: authority/capability/constraints/control/evidence/privacy/profiles); `cytoplex/policies/cap_core_policy.json`, `cap_med_policy.json`; `cytoplex/src/cytoplex/conformance/fixtures/adversarial.jsonl` (adversarial test cases) | Both `Yar/src/cap/data/cap_med_policy.json` and `cytoplex/policies/cap_med_policy.json` exist. Verify they are synchronized; no indication they are auto-generated from the same source. |
| **SPEC-neurobehavioral-axes** | `cytomem/configs/tracks.yaml` (track taxonomy: cytoverse/cytonome/cytoscope/toolchain/operational/research — neurobehavioral tracks live in cytonome); `cytos/data/gwas/pgc/*.tsv.gz` (PGC GWAS data for 14 disorders including BIP/MDD/SCZ/ADHD/ASD/ANX/PTSD) | No neurobehavioral axis scoring implementation found in any repo. The spec is design-only; no code bridge yet. |
| **SPEC-sensor-physiological** | No physiological sensor (Oura/wearable) adapter found in any repo. `Yar/apps/mobile/lib/src/audio/` covers voice; no Fitbit/Oura integration code exists. CSP SensorDescriptor is not yet implemented. | Design-only; no code to incorporate. |
| **SPEC-sensor-menstrual** | No menstrual sensor code found. | Design-only; no code to incorporate. |
| **SPEC-sensor-social-interaction** | No social-interaction (call log, proximity) sensor adapter code found. | Design-only; no code to incorporate. |

---

## 9. Highest-Value Incorporations (Top 8)

1. **DB benchmark numbers into SPEC-storage-engine** — `yar_supervisor_reproducible_benchmark_package/reference_results/surreal_tuned_patch10_final_comparison.md` contains the definitive p50 latency table and weighted scores; paste the PATCH10 comparison table into SPEC-storage-engine Section 3 to replace any placeholder language and nail the decision.

2. **Sync edge-case pass matrix into SPEC-sync-protocol** — `sync_benchmark/EDGE_COVERAGE.md` shows 12/12 pass with a named gap list; add as a normative table in SPEC-sync-protocol to define the minimum sync conformance bar.

3. **`VoiceAffectPolicy` as the CSP consent-attestation reference model** — `Yar/src/yar/models/voice_affect.py` contains the most complete privacy-policy model (5 fields: `raw_audio_stored`, `diagnostic_use_allowed`, `user_facing_emotion_label_allowed`, `on_device_only`, `retention_policy: ephemeral`). SPEC-CSP's consent-attestation section should cite or align to this schema rather than defining independently.

4. **`cap/guard.py` (CapLiteGuard) into SPEC-multi-agent** — the actual on-device safety gate is a deterministic term-matching guard, not an LLM-based evaluator. SPEC-multi-agent should describe this accurately, including the multilingual crisis terms (English + Farsi) and the crisis-support message format.

5. **`cytos/kg/biocypher/schema_config.yaml` into SPEC-CSP** — the `cytos:measured_by` predicate and `device` node type is the existing KG hook for connecting sensors to datasets. SPEC-CSP Section 5 (data schema) should reference this as the upstream semantic anchor for CSP observations.

6. **Gemma edge inference params into SPEC-edge-ai-hybrid** — `gemma_edge_intent_service.dart` has measured inference parameters (`temperature: 0.1`, `topK: 16`, `topP: 0.8`, `ModelType.gemmaIt`); these belong in SPEC-edge-ai-hybrid Section 3 as the normative on-device inference configuration.

7. **`PersonaMode` enum + Kokoro TTS implementation into SPEC-personas-voice** — the 5-mode enum (assistant/buddy/guardian/coach/quiet) is live and tested via `routes_persona.py`. Kokoro is implemented at `src/yar/core/tts/kokoro_english.py`. SPEC-personas-voice Section 5 should reconcile its richer persona model against the implemented enum and note ElevenLabs as planned, Kokoro as current.

8. **cytoplex `cap_med` profile + therapist scenario into SPEC-multi-agent** — `cytoplex/src/cytoplex/profiles/cap_med.py` and `scenarios/therapist_supervisor/` are the closest working reference for the Yar supervisor-therapist model. SPEC-multi-agent Section 3 (authority chain) and Section 6 (worked example) should cite these as the reference implementation.

---

## 10. Three Most Important Divergences

### D1: CapLiteGuard vs SPEC-multi-agent supervisor model

**What the spec says**: Section 2 describes a supervisor-worker topology with a 26B MoE supervisor and Gemma E4B workers communicating via CAP Directive envelopes.

**What exists**: `Yar/src/cap/guard.py` implements a **deterministic term-matching gate** that classifies crisis/diagnosis/treatment terms. There is no supervisor agent wired up in the backend. The `StubObjectRouter` in `core/model_router.py` has `fallback_to_stub: bool = False` and defaults to `ollama_cli` with `gemma4:e4b`. The `GemmaEdgeIntentService` on mobile performs local intent inference but routes to the Yar backend HTTP API, not to a supervisor. The full supervisor-worker split is spec-designed, not yet implemented.

**Risk**: Spec reviewers and engineers may believe the multi-agent system is further along than it is. The guard is production-ready; the supervisor is not.

### D2: VoiceAffectConstants diverge between Dart and Python

**What exists**: Three constants diverge between the backend (`voice_affect.py`) and mobile (`voice_affect_models.dart`): `HOP_MS` (250 vs 1500), `TTL_MS` (120,000 vs 10,000), `CONFIDENCE_FLOOR` (0.45 vs 0.25). Model ID also diverges (`distilhubert-ser-onnx` vs `distilhubert-ser-int8-onnx`).

**Risk**: If SPEC-sensor-speech-mentalstate cites these constants, it will be inconsistent. The divergence is either intentional (mobile needs longer hops to conserve battery, shorter TTL for privacy) or a drift bug. Either way it must be documented or reconciled before the spec can be normative.

### D3: LadybugDB cited in SPEC-storage-engine but absent from benchmark package

**What the spec says**: SPEC-storage-engine Section 3 lists LadybugDB as a front-runner alongside SQLite.

**What exists**: The `yar_supervisor_reproducible_benchmark_package` contains benchmarks for SQLite, FalkorDB, and SurrealDB (tuned and untuned). There are no LadybugDB results. The final decision in `Yar_Data_Fabric_Supervisor_Brief_EN.md` makes no mention of LadybugDB.

**Risk**: The spec presents an untested engine as a co-equal candidate. This could lead engineers to implement a LadybugDB path that has no empirical backing. The spec should either note "LadybugDB: pending benchmark, not yet measured" or remove it from front-runner status.
