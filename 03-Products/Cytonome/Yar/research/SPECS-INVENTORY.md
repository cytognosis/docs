> **Status**: Active
> **Date**: 2026-07-19
> **Author**: research agent (subagent, Cowork session)
> **Audience**: whoever builds the missing Wave 0 specs next
> **Tags**: `yar`, `spec-inventory`, `wave-0`, `planning`

# Yar Wave 0 — Specs Inventory

**BLUF:** Yar's `spec/` folder holds 22 files (12 core specs, 2 safety/governance specs, 5 storage/safety/eval session artifacts, 2 SurrealDB supporting guides, 1 index). Of the 10 Wave 0 spec areas needed, 3 already exist and need updating (sync protocol, multi-agent, personas), 7 are missing entirely and need new files. Two of those 7 have real prior art elsewhere in the docs tree that should be reused, not re-derived: Cactus model routing has a sketch in Cytoplex CAP research, and proofreading/structured-output has a canonical Instructor + spaCy/scispaCy pattern already documented for Cytos. Start with cross-node sync and the memory layer; they block everything downstream.

**If you only read one thing:** Section 3, the build list. It is ordered by the actual `depends_on` chains already declared in the specs' own frontmatter, not a guess.

---

## 1. Existing Specs (`docs/03-Products/Cytonome/Yar/spec/`)

All 22 files in the directory, read and summarized 2026-07-19.

| File | Scope (1 line) | Status |
|---|---|---|
| `README.md` | Index of the spec folder: core specs, safety/governance specs, storage/sync session artifacts, supporting guides | current |
| `SPEC-CSP.md` | Cytonome Sensor Protocol: universal sensor adapter contract ("MCP for sensors"), 5-phase adapter lifecycle, `SensorDescriptor`/`CrossBoundarySignal` schema | current (design-only, foundational) |
| `SPEC-data-sovereignty.md` | Data ownership/export/residency principles: device-first, server-optional, zero-knowledge relay, export-as-a-right | current (active) |
| `SPEC-edge-ai-hybrid.md` | On-device/cloud hybrid inference routing contract under CAP-Lite; Gemma edge intent + DistilHuBERT-SER implemented, cloud supervisor planned | needs-update (closest existing analog to "Cactus routing"; should absorb that decision once made) |
| `SPEC-multi-agent.md` | Supervisor-worker architecture: Supervisor, Interviewer, Transcriber, Placer, Reviser workers; CAP Directive envelope; brainmap-loop worked example | needs-update (agent naming inconsistent with `YAR-CLIENT-EVAL.md`'s shipped framing and with Wave 0's "transcriber/proofreading/mind-mapping" naming; mostly PLANNED, not built) |
| `SPEC-neurobehavioral-axes.md` | Integration layer combining all sensor outputs into 3 axes (Mood/Thought/Cognitive) via EQ dimension+direction model | current |
| `SPEC-personas-voice.md` | Voice Persona system (character/tone/TTS: Steady, Curious, Anchor, etc.); Kokoro TTS implemented, ElevenLabs planned; explicitly distinct from the "Trait Profiler" | needs-update (confirm/narrow scope note; does not cover per-agent personas) |
| `SPEC-sensor-menstrual.md` | Menstrual/reproductive-cycle sensing (Cytoscope-owned science), design-only | current |
| `SPEC-sensor-physiological.md` | Wearables (Oura/Fitbit), AWARE passive smartphone sensing, clinical instruments; design-only | current |
| `SPEC-sensor-social-interaction.md` | Social-rhythm/co-presence sensing extending the physiological spec; design-only | current |
| `SPEC-sensor-speech-mentalstate.md` | Speech/paralinguistic mental-state sensor; core models partially implemented (`voice_affect.py`, `EmotionTrackerService`) | current |
| `SPEC-storage-engine.md` | Storage engine decision: SQLite+FTS5+sqlite-vec (device, DECIDED), FalkorDB (server, DECIDED); CRDT op-log is sole source of truth; SurrealDB demoted to candidate GraphRAG projection | current (v0.2, ACTIVE, most authoritative doc in the set) |
| `SPEC-sync-protocol.md` | Cross-node sync: CRDT op-log at L2; Loro+Iroh (score 36/45) leaning over any-sync (35/45), neither committed; Solid at L6 for portability | needs-update (decision O-1 still open; this is the spec Wave 0 needs finalized) |
| `privacy-boundary-spec.md` | CAP privacy-boundary schema: data-classification table, `CrossBoundarySignal` schema | current (design-final, deliberately deferred post-YC) |
| `MODULE-crisis-detection.md` | Crisis-detection module: tiered scoring, `CrisisDecision` struct; only the `CapLiteGuard` keyword gate is shipped | current (design-final, deliberately deferred post-YC) |
| `SAFETY-CHECKPOINT_2026-07-16.md` | Resume-from-zero-context checkpoint memo for the safety/crisis workstream (decision D5 record) | current (2026-07-16, reference memo not a spec) |
| `ANYSYNC-FIT-ASSESSMENT_2026-07-16.md` | Licensing/fit assessment of Anytype `any-sync`: MIT server-node repos are clean, ASAL client is out of scope; informs SPEC-sync-protocol | current (2026-07-16) |
| `STORAGE_BENCHMARK_TRACKER.md` | Living master tracker for all storage/sync engine benchmarks; open decisions O-1 through O-8 | current (living document, refreshed 2026-07-16) |
| `STORAGE-ENGINE-RECOMMENDATION.md` | Recommendation memo that moved SPEC-storage-engine from draft to active; flags "Personal KG (cytomem)" as a separate, already-decided, out-of-scope-for-Yar system on Neo4j | current (2026-07-06) |
| `YAR-CLIENT-EVAL.md` | Evaluation of Ali's Tauri/React/Django reference client against the 3-agent design (transcription, revision/tagging, organization-into-KG); recommends adoption as the Wave 1 reference implementation | current, high-relevance cross-reference for multi-agent/transcriber/mind-mapping specs |
| `SurrealDB-tuning-and-graphrag-guide.md` | SurrealDB troubleshooting, configuration, GraphRAG query patterns, phone-vs-desktop profiles | current (narrow scope, contingent on future SurrealDB GraphRAG adoption) |
| `SurrealDB-advanced-optimization-and-versions.md` | Version-tracking companion guide: pin to v3.1.5, switch to `AsyncSurreal` | current (narrow scope, same contingency as above) |

## 2. Needed Specs for Wave 0

| Spec name | Exists? | Supports which Wave 0 feature | Scope to cover | Deep-research required? | Key libraries/standards to evaluate |
|---|---|---|---|---|---|
| **Personas for conversational agents** | update | User-facing companion voice/character | `SPEC-personas-voice.md` covers the single app-facing Voice Persona (Kokoro TTS, 5 modes) well, but does not address whether each worker agent (transcriber, proofreader, mind-mapper) needs its own persona or stays voiceless. Add an explicit scope-boundary note and cross-reference to `SPEC-multi-agent.md` | No | Kokoro (implemented), ElevenLabs (planned) — already identified, no new research needed |
| **Cactus model-routing (local/cloud)** | missing (partial prior art) | Cost/latency/privacy-aware routing across all agents | `docs/04-Engineering/cytoplex/research/cap-comprehensive.md` §5 already sketches "Cactus's hybrid routing concept" as a CAP `RoutingPolicy` model (`privacy_level`, `complexity_threshold`, `latency_budget_ms`, `fallback_on_cloud_unavailable`), flagged as open gap #6 (MEDIUM priority) in `cap-v0.2-revision-plan.md`. No Yar-specific spec formalizes this yet. New spec should adopt that pattern, not re-derive it, and reconcile with `SPEC-edge-ai-hybrid.md`'s existing on-device/cloud split | Partial — routing pattern exists, needs formal evaluation of Cactus itself plus integration with the already-decided Gemma-edge + Ollama-supervisor split | Cactus, existing Gemma 4 E4B/26B MoE, Ollama, LiteRT, flutter_gemma |
| **Cross-node sync: any-sync vs Loro+Iroh** | update | Multi-device sync for all Wave 0 features | `SPEC-sync-protocol.md` + `STORAGE_BENCHMARK_TRACKER.md` + `ANYSYNC-FIT-ASSESSMENT_2026-07-16.md` already carry a scored comparison (Loro+Iroh 36/45 vs any-sync 35/45) and a licensing clearance for any-sync's MIT server nodes. What is missing is the actual decision plus a concrete wire-protocol/ACL/conflict-resolution design, and the "any-sync as transport only, Yar reducer stays authoritative" pattern needs to be locked in | No — research is done; needs decision + design synthesis and a validation prototype | Loro, Iroh, any-sync (MIT server nodes only), Automerge 3.0 (fallback), Solid-OIDC/WebID (L6, already decided in principle) |
| **PeT knowledge graph + long-term memory** | missing | Long-term memory substrate for all agents | Note: the literal term "PeT" does not appear anywhere in the docs tree (grep returned zero hits); confirm what it refers to before starting. `SPEC-storage-engine.md` (ACTIVE) already decided the base substrate (SQLite device / FalkorDB server). The long-term-memory retrieval layer itself is only a one-line open question in `docs/01-Strategy/master-metaplan.md` ("Memory: HippoRAG vs ReMem vs SurrealDB"). Must also reconcile with `STORAGE-ENGINE-RECOMMENDATION.md`'s note that "Personal KG (cytomem)" is a **separate, already-decided, Neo4j-based system explicitly out of scope for Yar** — the new spec must state whether Yar's memory reuses cytomem or is a distinct construct on SQLite/FalkorDB | Yes | HippoRAG (2), ReMem, SurrealDB Spectron (native agent-memory layer, referenced in `STORAGE_BENCHMARK_TRACKER.md` §3.2), FalkorDB, Neo4j (for reconciliation only) |
| **Multi-agent orchestration** | update | Umbrella spec for transcriber + proofreading + mind-mapping loop | `SPEC-multi-agent.md` exists but has 3 different naming schemes across the corpus: README's "placer/reviser/side-thread" brainmap loop, this spec's own 5-role topology (Supervisor/Interviewer/Transcriber/Placer/Reviser), and `YAR-CLIENT-EVAL.md`'s shipped 3-agent framing (transcription / revision-tagging / organization-into-KG). Reconcile all three, update the implementation-status table against the actual shipped Tauri/Django reference client, add Dapr/NATS orchestration detail | No — mostly reconciliation of what already exists and what has already shipped | Existing: Gemma, Ollama, Dapr, NATS, MCP, A2A, CAP Directive envelope |
| **Proofreading / NER / structured-output** | missing (strong prior art) | The "Reviser" worker | Only a role-name stub exists in `SPEC-multi-agent.md`; `YAR-CLIENT-EVAL.md` notes a shipped but simple "personal NER via gazetteer." Critically, `docs/04-Engineering/infrastructure/data-strategy/linkml-kg-playbook/20_structured_extraction.md` already documents a **canonical Cytognosis pattern**: OntoGPT (ontology-grounded) → Instructor/PydanticAI (Pydantic-typed, schema-flexible) → spaCy/scispaCy (high-precision NER fallback), with a worked "LinkML → Pydantic → Instructor" example. The new Yar spec should adapt this tiered pattern rather than re-research it, adding medSpacy and DSPy evaluation (neither appears in the existing doc) plus CAP-Lite/crisis-gate interaction | Partial — reuse the existing tiered pattern; new research needed only for medSpacy, DSPy, and clinical/behavioral-health-specific tuning | spaCy, sciSpacy, medSpacy, Instructor, DSPy, OntoGPT (existing org pattern) |
| **Mind-mapping** | missing | The "Placer" worker | Only a role-name stub exists in `SPEC-multi-agent.md`. `YAR-CLIENT-EVAL.md` confirms a shipped MVP "Thought map (spatial canvas)" frontend plus BM25 + hashing-embedder + RRF hybrid retrieval + n-hop graph expansion server-side. `EVAL-tana.md`/`tana-outliner-deep-dive.md` already researched competitive UX patterns (supertags, live searches, command nodes) directly relevant to structure inference. New spec must define real-time chunking, a clustering algorithm to infer structure, and conservative-revision rules that preserve the user's existing spatial layout instead of constantly reorganizing it | Partial — competitive/UX research done via Tana eval; the chunking/clustering algorithm itself is new research | Incremental/streaming clustering approaches (for example online HDBSCAN, streaming topic models), existing BM25+RRF hybrid retrieval already in the reference client |
| **Transcriber agent** | missing (partial groundwork) | The "Transcriber" worker | Role stub exists in `SPEC-multi-agent.md` (Whisper-compatible on-device STT, PLANNED). `YAR-CLIENT-EVAL.md` confirms server-tier transcription is already shipped (mock + faster-whisper providers, content-hash blob archive); device-tier whisper.cpp/WhisperKit seam is documented but not bundled. `EVAL-voice-models.md`/`voice_model_deep_evaluation.md` already concluded Gemma 4 E4B + HuBERT/openSMILE for the **speech-affect sensor**, which is a different pipeline from dictation/STT. New spec must cover STT model choice for actual transcription (not affect), streaming partial-transcript handling, and the latency budget referenced in `SPEC-edge-ai-hybrid.md` (`cytoplex/benchmarks/cap_v1_latency_mobile_budget.md`) | Partial — voice-affect research exists but does not cover dictation STT specifically; needs its own model/vendor comparison | whisper.cpp, WhisperKit, faster-whisper, cloud STT vendors (comparison needed), OMI's Capture→Structure→Retrieval→Action memory loop (already researched, P0 adoption target per `EVAL-omi-ai.md`) |
| **Browser extension / WADM annotation + Memex parity** | missing (superseded prior doc) | Web capture surface | `docs/03-Products/Cytonome/Yar/mvp/06_WADM_ANNOTATION_INTEGRATION.md` exists but is explicitly marked **SUPERSEDED (2026-07-16)**, pointing to `yar-product-spec.md` and the Tauri reference client's `ARCHITECTURE.md` as current canonical sources; neither lives in `spec/`. It already names Memex and Hypothesis as reference projects and the W3C WADM model (`Annotation = Body + Target + Motivation + Selector + Provenance`); some WADM-inspired endpoints were implemented as of 2026-05-17. The MV3 + side-panel extension itself is one of four locked interface templates in `docs/04-Engineering/interface_and_fabric_design/00_master_architecture.md`. New spec should re-ground the WADM work in current architecture and add a concrete Memex feature-parity checklist | Partial — WADM pattern and reference projects already identified; needs a refreshed gap analysis against current architecture | W3C Web Annotation Data Model, Hypothesis, Memex, MV3 side-panel APIs |
| **Multi-platform delivery / design-system consumption** | missing (thin spec needed; heavy lifting exists org-wide) | Consistent delivery across Yar's phone/desktop/web/extension apps | `docs/04-Engineering/interface_and_fabric_design/00_master_architecture.md`, `01_refactor_brief.md`, and `claude_design_briefs/` (with per-platform delta briefs for desktop/extension/phone/web) already lock the four interface templates (Flutter phone, React 19+Vite+Tailwind+shadcn web, Tauri v2 desktop wrapping the web template, MV3+side-panel extension) at the org level. This is not Yar-specific and lives outside `spec/`. New spec should be a thin adoption/cross-reference document mapping Yar's actual apps (`apps/mobile`, `apps/desktop`, `apps/web`, `apps/extension`) onto these templates and listing only Yar-specific deltas (voice-capture UI, CSP consent screens, crisis-resource screens) | No | Flutter, React 19 + Vite + Tailwind + shadcn, Tauri v2, Manifest V3 side panel, the 4 use-case-profile CSS overlays (`[data-profile=...]`) |

## 3. Build List (dependency order)

Ordered using the `depends_on` chains already declared in the specs' own frontmatter, not a guess. Four tiers; within a tier, order is less critical.

**Tier 1 — foundational, blocks everything downstream**

1. **Cross-node sync** (`SPEC-sync-protocol.md`, UPDATE) — finalize the Loro+Iroh vs any-sync decision (O-1) and add the concrete wire-protocol/ACL design. `SPEC-CSP.md` and `SPEC-multi-agent.md` both list this spec as a direct dependency.
2. **PeT knowledge graph + long-term memory** (NEW) — builds on the already-ACTIVE `SPEC-storage-engine.md`; resolve the HippoRAG/ReMem/Spectron choice and the cytomem/Neo4j reconciliation before any agent starts writing long-term-memory ops.

**Tier 2 — orchestration layer, depends on Tier 1**

3. **Multi-agent orchestration** (`SPEC-multi-agent.md`, UPDATE) — reconcile agent naming and update implementation status. Must land before the three worker-detail specs below so they inherit one consistent naming scheme.
4. **Cactus model-routing** (NEW) — mirrors `SPEC-edge-ai-hybrid.md`'s own dependency list (multi-agent, CSP, storage-engine); formalize the existing Cactus-hybrid-routing sketch from `cap-comprehensive.md` §5 for Yar.

**Tier 3 — the three pipeline workers, in pipeline order, depend on Tier 2**

5. **Transcriber agent** (NEW) — first in the pipeline, captures raw input.
6. **Proofreading / NER / structured-output** (NEW) — consumes the transcript; reuse the existing Instructor/spaCy tiered pattern.
7. **Mind-mapping** (NEW) — consumes proofread/tagged output, organizes it into the KG/memory layer from Tier 1.

**Tier 4 — cross-cutting, lower dependency risk, can run alongside Tier 3**

8. **Personas for conversational agents** (`SPEC-personas-voice.md`, UPDATE) — scope-boundary clarification only.
9. **Browser extension / WADM annotation + Memex parity** (NEW) — refresh the superseded WADM doc against current architecture.
10. **Multi-platform delivery / design-system consumption** (NEW, thin) — lowest research burden; mostly adopting the existing org-wide template system. Good quick win to close out the wave.

---

## Notes for the next session

- **"PeT" is undefined in the docs tree.** Zero grep hits for the literal term across `docs/`. Confirm what it stands for before writing that spec; do not assume it equals `SPEC-storage-engine.md` or `cytomem`.
- **`cytomem` is a separate, already-decided system** (Neo4j, explicitly out of scope for Yar per `STORAGE-ENGINE-RECOMMENDATION.md`). Do not conflate it with Yar's own storage engine or the new long-term-memory spec without an explicit reconciliation statement.
- **Two "missing" specs have real prior art elsewhere in the docs tree**, found only by grepping outside the Yar product folder: Cactus routing in `docs/04-Engineering/cytoplex/research/cap-comprehensive.md` (§5) and `docs/03-Products/Cytonome/Cytoplex/research/cap-v0.2-revision-plan.md`; the Instructor/spaCy/scispaCy structured-extraction pattern in `docs/04-Engineering/infrastructure/data-strategy/linkml-kg-playbook/20_structured_extraction.md`. Both should be adopted, not re-researched from scratch.
- **`docs/04-Engineering/interface_and_fabric_design/`** already carries the org-wide, cross-product answer to "multi-platform delivery." Yar needs only a thin adoption spec, not a new design system.
