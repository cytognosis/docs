# Yar Salvage and Reconciliation Map — Repo A (Tauri YC base) vs Repo B (legacy Python/Flutter)

Analysis date: 2026-07-16. YC deadline: 2026-07-27 (11 days out). Scope: analysis only, no code changed in either repo.

**Repo A** = `~/repos/cytognosis/yar_revisions/yar-code-20260705-2354/` (canonical, React/Vite + Tauri + Django, 2 commits, started 2026-07-16).
**Repo B** = `~/repos/cytognosis/Yar/` (legacy, FastAPI + Flutter mobile, last commit 2026-05-29).

## BLUF

Repo A already ships a tested 22-feature slice (29/29 e2e, 34/34 backend tests) and already ported the one piece of Repo B that mattered most: CAP (CapLiteGuard), verbatim, today. Of the four named salvage targets, **none are YC-critical**. Three are architecturally redundant with decisions Repo A already made (TTS tiering, companion tone, capture-from-anywhere groundwork); the fourth (voice-affect SER) is explicitly out of scope for Yar per project rules (it belongs to Cytoscope) and isn't even working in the donor repo. Recommendation: ship the 7/27 slice with zero scope adds from Repo B; queue all four items as post-YC tickets with the port plans below. The only pre-YC action worth taking is a 10-minute disk cleanup of Repo B's 2.1 GB of build artifacts before anyone clones it again.

If you only read one thing: **don't port anything from Repo B before 7/27.** Everything named is either already covered, already superseded by a shipped decision in Repo A, or out of scope for this product per the project's own sensing boundary.

## 1. Salvage items — verdict table

| # | Item | Size in B | Model/deps | A has today | Port difficulty | YC-critical? |
|---|---|---|---|---|---|---|
| 1 | Voice-affect pipeline + ONNX SER | ~1,340 lines (Py: 497 core + 194 models + 148 routes; Dart: 882) | `distilhubert-ser-onnx` — not bundled, no `.onnx` in repo; mobile inference path is **disabled placeholder** (plugin conflict with Kokoro) | F54 "Voice mood awareness" already shipped as an honest placeholder, off by default | L | No — out of scope (Cytoscope owns sensing) |
| 2 | `core/tts/kokoro_english.py` (Kokoro TTS) | 412 lines (+524 lines support: text_processing/chunking/cache/registry) | `kokoro-onnx` pip pkg + `kokoro-v1.0.onnx` + `voices-v1.0.bin` — not bundled, downloaded to `models/kokoro/` | F11 companion voice already shipped: mock WAV + `openai_compat` forwarding to a Kokoro-FastAPI **server**, tested | M (mostly not reusable as-is; architecture mismatch) | No |
| 3 | `linkml_loader.py` + WADM annotation models | 538 + 328 + 68 + 43 + 53 = 1,030 lines | None (pure Python/YAML/Pydantic) | Nothing directly; F59 "Cytomark" (capture from anywhere) is Groundwork only | M | No |
| 4 | 5-mode PersonaMode system | 38 + 44 = 82 lines | None | F11 CompanionTone (4 modes: gentle/steady/cheerful/quiet) already shipped, tested, wired UI→backend→op-log | S (it's a naming decision, not a port) | No |

## 2. Item-by-item detail

### 2.1 Voice-affect pipeline + ONNX speech-emotion recognition (SER)

**Files in B** (all under `src/yar/`, line counts exclude `__pycache__`):

| File | Lines | Role |
|---|---|---|
| `models/voice_affect.py` | 194 | Pydantic wire types: `AffectState`, `AffectTrend`, `VoiceAffectSignal/Event/Policy/ContextHint` |
| `core/affect/tracker.py` | 171 | `EmotionTrackerService` — stateful EMA + trend fold, pure logic, no model code |
| `core/affect/style.py` | 148 | Maps affect state to companion response-style hints; hard bans "the user is angry"-type phrasing |
| `core/affect/mapper.py` | 49 | arousal/valence/confidence → coarse `AffectState` |
| `core/affect/trend.py` | 46 | trend detection over last N smoothed observations |
| `core/affect/smoothing.py` | 43 | EMA smoother |
| `api/routes_affect.py` | 148 | FastAPI routes; refuses any payload claiming raw audio was stored |
| `apps/mobile/lib/src/affect/*.dart` | 882 across 9 files | Flutter sidecar: tracker, EMA, mapper, trend, ONNX inference adapter |

**External dependency reality check**: no `.onnx` files exist anywhere in Repo B (`data/` is empty, no `models/` dir populated). The `DEFAULT_MODEL_ID = "distilhubert-ser-onnx"` is a string constant, not a shipped artifact — it would need separate acquisition/hosting. More importantly, `apps/mobile/lib/src/affect/onnx_distilhubert_ser_inference.dart` is **currently a stub that reports itself unavailable**: comment in the file explains the real Flutter ONNX plugin was dropped because `flutter_onnxruntime` (needed for Kokoro TTS) and the older `onnxruntime` plugin ship incompatible native iOS pods. So the "working SER pipeline" doesn't actually work end-to-end even in the donor repo today — what's salvageable is the orchestration scaffolding (tracker/smoother/mapper/trend), not a functioning sensor.

**What Repo A has today**: `CompanionTone` (`src/domain/yarTypes.ts`) is user-selected, not sensed. F54 in `REQUIREMENTS_COVERAGE.md` is explicitly "Placeholder by design... off by default... never a diagnosis." `IMPLEMENTATION_NOTES.md` repeats the same non-diagnostic language rule independently. The two repos converged on identical safety language without copying from each other.

**Project-rule check**: Yar's own `CLAUDE.md` states: *"Yar CONSUMES sensing; it does not own the sensing science. The sensor-science specs (voice/speech mood, physiological, menstrual, social) belong to the Cytoscope project."* Voice-affect SER is a sensor-science spec. Porting it into Yar's Django backend directly would violate this boundary regardless of YC timing.

**Verdict**: Not YC-critical. Do not port before 7/27 under any circumstance — F54 is already shipped as intended (an honest placeholder) and touching it risks the 29/29 e2e suite for zero user-facing gain in an 11-day window.

**Post-YC port plan** (only once Cytoscope has a working on-device SER adapter): reuse `tracker.py` + `smoothing.py` + `mapper.py` + `trend.py` near-verbatim as pure functions (they have zero framework dependencies) inside Cytoscope, not inside Yar. Yar's only change is to consume a `VoiceAffectContextHint` the same way `assistant/style.py`'s pattern already anticipates — add it as an optional input to `backend/assistant/providers.py`'s tone selection, never surfaced to the UI as a label.

### 2.2 `core/tts/kokoro_english.py` (Kokoro TTS)

**Files in B**: `kokoro_english.py` (412 lines, the in-process ONNX binding), plus shared TTS infra `text_processing.py` (105), `chunking.py` (91), `cache.py` (54), `registry.py` (158), `base.py` (46), `null_provider.py` (36) — 936 lines total in `core/tts/`.

**External deps**: `kokoro-onnx` PyPI package (`pip install kokoro-onnx misaki[en] soundfile`) + `kokoro-v1.0.onnx` + `voices-v1.0.bin`, both env-path-configured (`YAR_KOKORO_MODEL_PATH`, `YAR_KOKORO_VOICES_PATH`), neither committed to the repo — confirmed absent from `find -iname "*.onnx"`.

**What Repo A has today**: `backend/transcribe/tts.py` (104 lines, tested — 34/34 backend tests include TTS). Two providers: `MockTts` (deterministic sine-wave WAV, dependency-free) and `OpenAICompatTts` (forwards to `YAR_TTS_BASE_URL` + `/v1/audio/speech`). `ARCHITECTURE.md`'s AI-runtime-tiers table explicitly names **Kokoro-FastAPI** as the recommended laptop-tier server, spoken to over the OpenAI wire dialect — i.e., Repo A already decided to run Kokoro as a separate process and call it over HTTP, not embed the ONNX runtime inside Django. Repo B's `kokoro_english.py` is the opposite pattern (direct in-process binding), which is why it's mostly not reusable as-is: adopting it would mean walking back an architecture decision already documented and tested in A.

**Verdict**: Not YC-critical. A's TTS story for F11 is shipped and tested; nothing in `NEXT_STEPS.md` calls for embedding Kokoro directly.

**Port plan (post-YC, optional)**: don't port the binding. Two small, genuinely reusable pieces:
- `KOKORO_VOICE_OPTIONS` (the voice-persona table, e.g. `am_fenrir` tagged `recommended_for: ["coach", "buddy"]`) — useful seed data for a future `/api/tts/voices` endpoint once a real Kokoro-FastAPI instance is deployed. Target: extend `backend/transcribe/tts.py` with a static voice catalog.
- `text_processing.py` (TTS-safe text cleaning) and `chunking.py` (long-text splitting) — worth a look if `OpenAICompatTts` needs pre-chunking for long replies later. Target: same file, additive only.

### 2.3 `integrations/linkml_loader.py` + WADM annotation models

**Files in B**: `integrations/linkml_loader.py` (538), `integrations/wadm_adapter.py` (328), `models/wadm.py` (68, W3C Web Annotation Data Model types: `WADMAnnotation`, `TextQuoteSelector`, `TextPositionSelector`), `api/routes_annotations.py` (43), `core/annotation_service.py` (53). Total ~1,030 lines. Companion JSON Schemas: `data/schemas/linkml_anytype_mapping.schema.json`, `capture.schema.json`, `yar_object.schema.json`, `guard_decision.schema.json`. Test coverage exists: `tests/test_linkml_loader.py`, `tests/test_wadm_adapter.py`, `tests/test_annotation_routes.py`.

**External deps**: none beyond stdlib/PyYAML/Pydantic — this is the cleanest, lowest-risk item of the four to actually port when the time comes.

**What Repo A has today**: nothing equivalent. A's knowledge layer is op-log projections (`backend/knowledge/graph.py`), not a schema-driven typed-object store. F59 ("Capture from anywhere" / Cytomark) is listed as Groundwork in `REQUIREMENTS_COVERAGE.md` — the capture source is modeled and rendered, but there's no browser-extension/global-hotkey capture path yet, which is exactly what `wadm_adapter.py` was built to feed (it converts browser highlight/annotation payloads into a capture object).

**Coupling caveat**: in B, `linkml_loader.py` feeds Anytype's payload mapper (`integrations/anytype/_schema_mapper.py`) — it needs decoupling from Anytype before it's useful to A.

**Verdict**: Not YC-critical. F59 groundwork isn't part of the 22-feature tested slice per `IMPLEMENTATION_NOTES.md`'s explicit scope list (F01–F08, F11, F13–F17, F27, F31, F32, F39, F44, F53, F54, F57–F60 as groundwork, not full builds).

**Port plan (post-YC, when browser capture is prioritized)**: target `backend/knowledge/annotations.py` (new). Reuse `models/wadm.py` almost verbatim — `WADMAnnotation`/`TextQuoteSelector`/`TextPositionSelector` are W3C-standard shapes worth keeping intact. Re-target `wadm_adapter.py`'s output from an Anytype write to a `capture.created` op (`source: "cytomark"`, provenance = page URL + selector). Port `linkml_loader.py` near-verbatim, dropping the Anytype-specific `_schema_mapper` glue.

### 2.4 5-mode PersonaMode system

**Files in B**: `models/planning.py` lines 8–18 (`PersonaMode` enum: `assistant`, `buddy`, `guardian`, `coach`, `quiet`), `api/routes_persona.py` (44 lines: `GET/PATCH /persona`, `GET /persona/modes` with human-readable descriptions).

**What Repo A has today**: `CompanionTone` (`gentle` | `steady` | `cheerful` | `quiet`) — F11, **Shipped**, wired through `src/features/settings/SettingsScreen.tsx` → `src/domain/store.ts` → `backend/assistant/providers.py` (`TONE_OPENERS`/`TONE_CLOSERS` dictionaries) → the rule-based and OpenAI-compat companion providers. This is functionally the same feature (a persona/tone axis shaping companion replies) under a different taxonomy. Only `"quiet"` is shared verbatim between the two naming schemes; B's `coach`/`guardian` have no A equivalent, and A's `cheerful` has no B equivalent.

**Verdict**: Not a port task at all — it's a naming reconciliation decision. A's version is shipped, tested end-to-end (UI + backend + op-log + e2e), and functionally complete for the 7/27 slice.

**Recommendation**: keep A's 4-tone system for the 7/27 ship. Do not reopen this pre-deadline — a rename would touch UI copy, the op-log schema (`companionTone` field), backend tone dictionaries, and the e2e suite (currently 29/29 green) for a purely cosmetic change. Post-YC, if product wants B's naming (it may read better against the public feature catalog's naming-layer convention), do a rename-only pass: `CompanionTone` type, `TONE_OPENERS`/`TONE_CLOSERS`, the tone picker UI, and `src/lib/copy.ts`. This is not code salvage from B; B's actual route/enum code isn't reused, just its vocabulary.

## 3. Other findings worth flagging (searched broadly per instructions)

| Finding | Detail | Recommendation |
|---|---|---|
| CAP guard is already ported, verbatim | `backend/cap/{guard,policies,constants,primitives,protocols,models,__init__}.py` in A match `src/cap/*` in B byte-for-byte in line counts (756/42/13/386/59/44/83). Confirmed by A's own git log: `068b10d feat(safety): port CapLiteGuard pre-response gate from legacy Yar repo` (2026-07-16, today). | Done. No further action. |
| A second, stale CAP module exists in B | `src/yar/cap/` (79 lines total: `guard.py` 5 lines, `models.py` 5 lines, etc.) is a much smaller, different, likely-abandoned stub, distinct from the real `src/cap/` that was actually ported. | Flag so nobody accidentally references `yar.cap` instead of the top-level `cap` package during any future salvage pass. Candidate for deletion in B. |
| Anytype PKM integration (~2,250 lines: `adapter.py` 692, `client.py` 388, `setup.py` 235, `_payload_mapper.py` 255, `_schema_mapper.py` 120, `_transport.py` 155, plus smaller helpers) | Legacy integration writing to the third-party Anytype app. A's architecture is self-contained (own op-log + graph projections) and has no Anytype dependency. B's own `docs/reports/02_anytype_refactor.md` and `03_cap_consolidation.md` (already promoted to the docs repo) document this as a past pivot. | Not portable, not needed. Dead weight for cold-store; the historical rationale is already captured in the promoted reports, so nothing is lost by archiving the code. |
| `model_router.py` (620 lines) + `interactive_assistant.py` (312 lines) | B's design for routing between on-device Gemma E2B and cloud models. Conceptually overlaps with A's `src/lib/runtimes.ts` + `backend/assistant/providers.py`, but A's design is simpler and already shipped/tested; B's is unshipped and tied to Anytype/Flutter plumbing. | Reference only for the post-YC on-device LLM work in `NEXT_STEPS.md` item 5 ("On-device runtime (Gemma-class)"). Not a direct port. |
| Prompt drafts (`data/prompts/*.md`) | `object_router.md` and `communication_translator.md` are already promoted to `docs/03-Products/Cytonome/Yar/prompts/`. `daily_anchor_planner.md` does not appear promoted. | Low-priority: promote `daily_anchor_planner.md` if daily-planning prompt engineering becomes relevant post-YC; otherwise leave in B. |
| JSON Schemas (`yar_object.schema.json`, `capture.schema.json`, `guard_decision.schema.json`) | Reference schemas for B's typed-graph-node model — a different paradigm from A's op-log. | Not portable directly; could inform a future JSON-schema validation layer over A's op payloads if that's ever added. Not urgent. |
| Flutter mobile app (`apps/mobile/`) | Full Flutter/Dart codebase. A's mobile story is Tauri v2 iOS/Android init, planned post-desktop per `NEXT_STEPS.md` item 7 — an entirely different framework. | Not code-portable across frameworks. Keep as design reference only (e.g., the EMA/trend math in the Dart affect files mirrors the Python version and could sanity-check a future Rust/TS port). |

## 4. Repo A shipped features vs Repo B feature surface

Mapping `REQUIREMENTS_COVERAGE.md`'s Wave 1 table against what exists (in any form) in Repo B:

| A feature (status in A) | B equivalent | Note |
|---|---|---|
| F01/F02 Voice capture, task from speech (Shipped) | B has `apps/mobile` audio capture + `interactive_assistant.py` | A's server STT (mock/faster-whisper) is a cleaner, already-tested path; no gap |
| F11 Companion style/voice (Shipped) | B's 5-mode PersonaMode + Kokoro TTS | Naming/taxonomy difference only (§2.4); TTS architecture already superseded (§2.2) |
| F54 Voice mood awareness (Placeholder by design) | B's voice-affect/SER pipeline | Intentionally not implemented in A; see §2.1 — also not fully working in B |
| F58 Personal NER (Shipped, lite) | B's `linkml_loader`/schema registry, Anytype `_schema_mapper` | Different paradigm (schema-typed objects vs op-log graph mentions); no direct reuse |
| F59 Capture from anywhere / Cytomark (Groundwork) | B's `wadm_adapter.py` + browser-highlight capture flow | Closest real gap-filler candidate; see §2.3 port plan |
| F60 Conversational thought map (Groundwork→Shipped for chat) | B has no direct equivalent (Anytype write-back is a different UX) | No gap |
| Nothing in A's catalog | B's Anytype PKM sync | Legacy, superseded, no A feature maps to it |
| Nothing in A's catalog | B's `communication_translator.md` / `routes_communication.py` ("rewrite outgoing draft, preserve authentic voice") | Not in A's Wave 1 canonical catalog; worth a look against the CU-1..CU-8 Cytognosis-unique feature list post-YC, but out of scope now |

## 5. Docs in B's `docs/` worth promoting

Most of `docs/` in Repo B is already stub-redirected ("moved to docs repo") from the 2026-05-29 consolidation, and cross-checked against the current canonical tree (`docs/03-Products/Cytonome/Yar/` and `docs/02-Funding/YC/submissions/`):

| B doc | Status |
|---|---|
| `docs/architecture/*`, `docs/planning/mvp/*`, `docs/research/*`, `docs/reports/*` | Already stub-redirected; content confirmed present under the current canonical tree (e.g., `research/yar-unified-feature-comparison-v4.md`, `research/persona_profiler_frameworks_reference.md`). No action needed, though the stub `new_path` values reference a stale flat path scheme (`cytonome/yar/...`) that predates the current `03-Products/Cytonome/Yar/` reorg — cosmetic only, files exist under the new location. |
| `docs/submission/{ARCHITECTURE,EVALUATION,LIMITATIONS,PROJECT_OVERVIEW,ROADMAP,SAFETY_AND_TRUST,VIDEO_STORYBOARD}.md` | Already promoted, confirmed present at `docs/02-Funding/YC/submissions/`. No action needed. |
| `docs/submission/{API_WALKTHROUGH,DEMO_SCRIPT,JUDGES_QUICKSTART,README_SUBMISSION}.md` | **Not promoted, not stubbed.** These are live content but describe an earlier hackathon submission workflow (`cd ~/Documents/Yas`, `venv`) that predates the Tauri pivot and no longer matches Repo A's setup. | Recommend cold-store (archive), not promote — factually superseded. |
| `docs/checkpoint/2026-05-23-pre-antigravity-update/branch-graveyard.md` | Historical branch-deletion log, informational only. | Low priority; fine to leave or archive alongside the rest of `docs/checkpoint/`. |

## 6. Dead weight in B — cold-store decision

| Path | Size | Recommendation |
|---|---|---|
| `build/` | 960 MB | Delete. Build artifact, regenerable. |
| `dist/` | 640 MB | Delete. Build artifact, regenerable. |
| `third_party/` (`leantime` + `super-productivity` full clones, `flutter_kokoro_tts` vendor) | 524 MB | Delete. The two app clones were feature-comparison research aids; findings already captured in the promoted `feature_comparison_leantime_vs_sp.md`. `flutter_kokoro_tts` is vendor code for an abandoned Flutter plugin path. |
| `.venv/` | 76 MB | Delete. Regenerable via `uv sync`. |
| `.mypy_cache/` | 63 MB | Delete. Regenerable. |
| `logs/` | 2.6 MB | Delete. Runtime logs. |
| `.ruff_cache/`, `.pytest_cache/` | ~112 KB combined | Delete. Regenerable. |
| `apps/mobile/android/.gradle/`, iOS build folders | Included in `apps/` 4.6 MB total (small) | Low priority; prune only if `apps/mobile` itself is cold-stored. |

Total immediately reclaimable: **~2.27 GB** (`build` + `dist` + `third_party` + `.venv` + `.mypy_cache` + `logs` + small caches), none of which affects the salvage items above (all four named targets live under `src/yar/` and `apps/mobile/lib/`, which total under 10 MB combined).

## 7. Bottom line for the 7/27 ship

- **Zero scope adds from Repo B.** Every named salvage target is either out of scope (voice-affect/SER — Cytoscope's domain), architecturally superseded by a shipped decision (Kokoro TTS, PersonaMode/CompanionTone), or Groundwork-only in A's own plan (WADM/Cytomark).
- **The one thing that mattered (CAP) is already done**, verbatim, same-day.
- **Post-YC backlog, in priority order**: (1) WADM/linkml for F59 browser capture — cleanest port, real feature gap; (2) Kokoro voice-catalog seed data — small, cosmetic upgrade once Kokoro-FastAPI is deployed; (3) PersonaMode naming reconciliation — product decision, not engineering; (4) voice-affect — blocked on Cytoscope shipping a working SER adapter, and on resolving the ONNX-plugin conflict that currently disables it even in the donor repo.
- **Housekeeping**: reclaim ~2.27 GB from Repo B's build artifacts and vendor clones; archive the four un-promoted hackathon submission docs; note the stale `src/yar/cap/` stub for eventual deletion so it doesn't get confused with the real `src/cap/` that was ported.

---

## Related documents

- [`yar-framework-assessment_2026-07-16.md`](./yar-framework-assessment_2026-07-16.md) -- the companion long-term framework call; read together, this map is short-term (pre-7/27) and the framework assessment is long-term (post-YC).
- [`yar-feature-research-FINAL_2026-07-16.md`](./yar-feature-research-FINAL_2026-07-16.md) -- consolidates this map alongside the v4 comparison and prioritization into one founder reference.
- Repo A (canonical): `~/repos/cytognosis/yar_revisions/yar-code-20260705-2354/` (branches `main`, `feat/sqlite-device-store`); Repo B (legacy) per this map's own path.
