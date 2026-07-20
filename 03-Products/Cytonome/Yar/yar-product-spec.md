# Yar Product Spec (canonical)

> **Status:** Active · **Date:** 2026-07-18 · **Author:** @mohammadi · **Audience:** engineers, stakeholders, funders
> **Variants**: Technical (this doc) - Readable (yar-product-spec.md in Obsidian vault, same filename) - Agent (yar-product-spec_prompt.md)
> **Supersedes:** `yar-product-feature-master.md`, `yar-product-implementation.md`, `cytonome-master-reference.md`, `feature-comparison.md` (all archived with forward links). **Feature index:** `YAR_FEATURE_CATALOG.md` (69 features). **Evidence base:** `research/yar-unified-feature-comparison-v4.md`.
> **Reading time:** about 8 minutes.

**If you only read one thing:** Yar is Cytonome v0.1, a local-first, voice-aware, AI-native cognitive companion built by and for neurodivergent adults. It turns messy voice or text into typed objects in a personal knowledge graph, helps the user plan and execute, and keeps raw data on-device behind a hard safety boundary (CAP). This spec is the single canonical product doc; per-feature depth lives in the 69-feature catalog and the formal specs it maps to.

---

## 1. What Yar is

**Yar (Your AI Representative) is a local-first, voice-aware, AI-native cognitive companion for neurodivergent adults, built by and for neurodivergent people.** It is the consumer-facing expression of Cytognosis's **Cytonome** navigator layer. Yar accepts messy input (voice, text, web context), uses on-device AI to structure it into typed objects in a personal knowledge graph, and helps the user execute, manage time, and stay self-aware. Raw private data stays on-device by default, and a hard safety boundary (**CAP**) blocks diagnosis, treatment, and unconfirmed sharing.

**Who it is for:** neurodivergent adults (ADHD, autistic, AuDHD, and adjacent) for whom continuous tracking and multi-app context-switching fail. Yar is not built for clinicians or developers as target users.

**Wedge thesis:** win the daily habit first (frictionless capture, execution, self-awareness), then layer soft sensors (speech-emotion, patterns) in software, with hardware sensors later. This inverts the one-to-two-month abandonment curve typical of health and wearable apps.

**Relationship to Cytognosis:** Yar is the shippable consumer wedge of the platform, Cytonome productized. It builds a consented, longitudinal, multimodal personal dataset that feeds the broader Cytoverse map, and is structured to sit in the **for-profit PBC arm** post-bifurcation; the open science stays in the Foundation. Three architecture pillars anchor the product: the flagship **branching brainmap companion** (Section 5C), **adaptive personas** (Section 5A), and a **universal sensor protocol, an "MCP for sensors"** (Section 5B).

## 2. Who it is for and the gap it closes

To get through a day, a neurodivergent adult currently stitches together seven or eight apps: task and focus managers, task-breakdown helpers, knowledge organizers, auto-planners, read-aloud tools, ambient voice capture, brain-dump transcription, and a data-ownership store. That is seven or eight logins and seven or eight silos, and the context-switching between them is itself the executive-function problem each claims to solve.

None of them combine cognitive-state visualization (Brain Weather), digital body-doubling, dual-track planning (ideal versus baseline), emotionally aware rest days, a hard safety boundary, neurodivergent-to-neurotypical communication support, and vocal-biomarker emotional awareness. **Yar replaces the stack with one local-first, AI-native, voice-aware, emotionally intelligent companion that keeps data on-device, adapts to the user's brain, and never charges a subscription.** The full scored competitive analysis is in `research/yar-unified-feature-comparison-v4.md`.

## 3. Current build status

The skeleton-first MVP is implemented, and **Product Milestone 1 (Mobile Voice)** proves the first end-to-end mobile voice loop:

```
Flutter mobile voice/text capture
  -> on-device (or backend-edge) VoiceIntent routing
  -> CAP-Lite mobile directive
  -> Yar central coordinator
  -> model router (stub / http_json / Ollama; tested with gemma 4 e4b)
  -> local graph store
  -> typed write plan
  -> explicit user confirmation
  -> guarded external write
```

Mobile is a Flutter app (Status, Voice, Objects, Plan, Settings screens) with platform speech-to-text plus an editable transcript fallback and on-device **Gemma E2B** VoiceIntent via `flutter_gemma`. The backend exposes voice APIs with a deterministic model-router stub as the default test path. **CAP-Lite** is the boundary before model routing and before any external write. Storage is a local graph with a typed write plan and explicit user confirmation. The founder is solo, there are no external users yet, and Yar is positioned as wellness and productivity, not a medical device.

## 3A. Design partners

The founder is embedded in overlapping queer, trans, nonbinary, poly, and neurodivergent communities, which are high mental-health need, underserved, and exactly Yar's population. This is the natural first user base and is already in motion: community members have contributed data unprompted, and a sensor-engineer design partner (Olivia) collaborates on Cytoscope and the CSP sensor protocol. The plan is a small **design-partner program** (a two-minute opt-in) that prioritizes features, pilots Milestone 1, and seeds the consented longitudinal dataset. It is the lowest-cost growth path and the foundation of the wedge.

## 4. Architecture

**Pipeline:** `phone capture -> local coordinator -> Gemma 4 structuring -> CAP-Lite guard -> typed objects -> read/write/link`.

| Layer | Implementation |
|---|---|
| Capture | Flutter app: voice via platform STT plus editable fallback; text; future web/browser context |
| Coordination | Local coordinator service: receives captures, calls Gemma 4 (or mock), produces structured proposals, runs CAP-Lite, executes graph ops, returns reports |
| On-device AI | Gemma 4 family (E2B on mobile, E4B on desktop) via `flutter_gemma` / LiteRT and Ollama; local-first inference, optional cloud for quality (`SPEC-edge-ai-hybrid`) |
| Safety | **CAP / CAP-Lite** (Controller-Authority Protocol): only allowlisted ops execute; no external writes without confirmation; raw captures stay local; model output must conform to schema; diagnosis and treatment claims blocked; uncertain social interpretations must use uncertainty language (`MODULE-crisis-detection`, `privacy-boundary-spec`) |
| Schema | **LinkML** classes and slots mapped to typed store objects (Class to Type, Slot to Property or Relation, Enum to Select, inheritance to template) |
| Storage | Storage-engine under active decision (`SPEC-storage-engine`, DRAFT): the MVP used a local SQLite graph plus an Anytype MCP write path; the storage-engine spec evaluates SurrealDB and is held in DRAFT pending the SurrealDB v3.1.5 retest. Sync is covered by `SPEC-sync-protocol` |
| Annotation | **WADM** (W3C Web Annotation Data Model) for highlight, annotate, and link flows |
| Interop | **MCP** server exposure planned; on-device TTS for personas via **Kokoro** (`SPEC-personas-voice`) |

**On voice technology (reconciliation):** persona voices now use on-device **Kokoro TTS** (`SPEC-personas-voice`), not the earlier ElevenLabs Voice-Design approach; the Yar repo vendors `flutter_kokoro_tts`. ElevenLabs remains only a possible one-time voice-design source, not a runtime dependency.

## 5. The three flagship pillars

### 5A. Adaptive personas (companion identity)

Yar's companion is configurable as a **persona**: a bundle of personality, relationship stance (coach, buddy, guardian, parent, partner), tone and style, and voice (on-device TTS). Three commitments make this neurodivergent-native. **Zero configuration tax:** the persona refines itself from ordinary interaction (explicit feedback plus implicit signals such as engagement, voice-emotion mood-state, time, and task), learning preferences on-device; every adaptation is inspectable, adjustable, and resettable ("suggest, not decide"). **Multiple personas:** a user can keep several. **Mood and context-aware selection:** Yar learns which persona the user prefers in which mood and context and suggests it via a lightweight on-device policy. This operationalizes the ADHD paper's highest-rated companion concepts (Social Presence AI and Mood-Aware Companion). Maps to features F11, F29, F45, F57 and `SPEC-personas-voice`.

### 5B. Cytonome Sensor Protocol (CSP), an "MCP for sensors"

CSP is a **universal sensor adapter protocol**, an MCP-style open interface that lets users and third parties plug any sensor into Cytonome/Yar as easily as adding an integration. The voice-emotion sensor is simply the first CSP adapter. Each adapter declares identity and modality, the typed observations it emits (LinkML schema, so all sensors feed Brain Weather and the graph uniformly), a privacy and data-residency class, consent requirements, sampling cadence, and a `discover -> connect -> configure -> read/stream -> disconnect` lifecycle. **CAP governs every adapter:** raw biometric data stays on-device by default and each sensor is granted or revoked individually. CSP future-proofs Yar for Cytognosis hardware, creates an open ecosystem (Apache 2.0), and unifies every modality into one typed, on-device cognitive picture. Maps to features F12, F55, F30, F46 and `SPEC-CSP`.

> [!NOTE]
> **Naming:** **CSP (Cytonome Sensor Protocol; formerly USAP/UBAP)** is the canonical term. The engineering `sensors/` docs historically used these deprecated names for the same protocol; use CSP going forward.

### 5C. Branching brainmap companion (the flagship)

> [!IMPORTANT]
> **TL;DR:** Yar's flagship is a voice-driven living brainmap. You think out loud; a companion agent grows a self-organizing thought-tree in real time, attaching each idea where it belongs, quietly fixing earlier placements, learning your personal slang, and turning any branch into a proposal, paper, or plan on command. It is the Cytonome navigator pointed at your own mind, a GPS for your thoughts.

You talk; Yar listens, understands your words (including slang and shorthand), and on each turn reasons about where the new thought best attaches in the growing graph, which restructures itself as the bigger picture emerges. It removes the "where does this go?" tax, honors nonlinear associative thinking, repairs earlier placements via a background reviser agent, learns your personal lexicon, deconvolves interleaved threads, captures side TODOs off the main flow, and turns a subtree into a proposal, paper, or plan. The brainmap is a typed (LinkML) thought-graph stored locally; three on-device agent roles run over it (a placer, a reviser, and a side-thread agent), all governed by CAP. Maps to features F13, F14, F15, F31, F60 and `SPEC-multi-agent`. It exists because it is how the founder's own mind works, which is the heart of the by-and-for-neurodivergent thesis.

## 6. Feature catalog (69 features)

The canonical per-feature index is `YAR_FEATURE_CATALOG.md`: **69 features, F01-F69** (62 original; F63 invisible-disability advocacy mode and F64 personal compass added 2026-07-18; F65 focus & adherence guardian, F66 ask & summarize your captures, F67 long-term personal memory, F68 cross-device sync, and F69 meeting-mode diarization added 2026-07-19 per `research/FEATURE-VERIFICATION.md`), across six neurodivergent functional domains, plus two infrastructure modules that gate the rest. Each feature carries three naming layers (affirming public label, psychological construct tag, domain code); **CU-1..CU-8** mark the unique features: 20 features anchored to 8 named, defensible capability clusters, plus 21 additional features with no direct competitor equivalent.

**Domains:** AEF (Attention/Executive Function), ERM (Emotion Regulation/Mood), SCI (Social/Communication/Interaction), SPR (Sensory/Processing), CTO (Cognition/Thought Organization), SMI (Self-Monitoring/Insight).

Features are organized in a 3-level hierarchy (6 domains, 19 clusters, 69 features); see `research/FEATURE-HIERARCHY.md` and `research/features.json`.

**Waves:** 0 = safety and sensor substrate; 1 = wedge (25 founder-elevated features); 2 = moat (28 features, including F65 and F66); 3 = sensor, hardware, and research (7 features, including F69). Seven infrastructure features build first: F18 safety/consent layer, F19 on-device AI runtime (Gemma 4 E4B), F52 local knowledge store, F50 web annotation layer, F51 schema translation, F67 long-term personal memory (the PeT recall layer), F68 cross-device sync; plus the privacy-boundary schema and crisis-detection module.

**Wave 1 (the wedge, build first):** energy/mood map (F05), flexible plan with backup (F07), rest-day support (F27), streaks that honor rest (F44), focus companion / body doubling (F06), companion style/voice (F11), voice mood awareness (F54), adaptive companion/trust (F57), morning check-in (F53), private space before planning (F17), gentle nudges (F39), voice-grown thought map (F13), voice capture (F01), task creation from speech (F02), task structuring (F03), task scheduling (F04), personal NER (F58), conversational thought map (F60), stray-thought capture (F32), mood tag (F08), capture from anywhere (F59), thought placement (F14), map reviewer (F31), spatial map view (F15), open export (F16).

**F24 scope extension (2026-07-19), AI morning plan with interactive collaborative refinement.** F24 is no longer a single-pass suggestion. The agent proposes up to three anchors, then the person and the agent iterate together: the person can push back, swap, resize, reorder, or defer items in plain language, and the agent revises and re-presents until the person confirms the plan. The interaction model reuses F60's conversational-iteration pattern; accepting the first pass unchanged is always a first-class outcome, never a nagged one. Prompt contract: `prompts/daily-anchor-planner.md`.

## 7. Feature-to-spec map

- **`SPEC-CSP`:** F12, F55, F30, F46
- **`SPEC-personas-voice`:** F11, F29, F45, F57 (Kokoro TTS)
- **`SPEC-multi-agent`:** F13, F14, F15, F31, F60 (three-agent loop), F18
- **`SPEC-edge-ai-hybrid`:** F19 (Gemma 4 E4B)
- **`SPEC-storage-engine` / `SPEC-sync-protocol`:** F52, F16, F68 (storage-engine ACTIVE; sync co-designed with storage and the PeT temporal-KG abstractions)
- **`SPEC-petkg-longmemory`:** F67, F66 (PeT temporal knowledge graph + long-term recall)
- **`SPEC-transcriber-agent` / `SPEC-proofreading-agent` / `SPEC-mindmapping-agent`:** worker-level detail under `SPEC-multi-agent` (F01, F13-F15, F31, F33, F58, F60)
- **`SPEC-cactus-routing`:** local/cloud model routing for all agents (with `SPEC-edge-ai-hybrid`)
- **`SPEC-browser-extension`:** F50, F59 (WADM + Memex parity)
- **`SPEC-multiplatform-delivery`:** F41 delivery architecture (org interface templates)
- **`SPEC-meeting-diarization`:** F69 (consent-gated; counsel review of multi-party consent law)
- **`SPEC-neurobehavioral-axes`:** axis substrate for all features
- **`MODULE-crisis-detection` + `privacy-boundary-spec`:** gate F18, F27, F28, F36, F42, F56
- **Sensor-science specs** (`SPEC-sensor-speech-mentalstate`, `-physiological`, `-menstrual`, `-social-interaction`): consumed by F54, F40, F30, F56, F42; the sensing science is owned by the **Cytoscope** project (Section 10).

## 8. Prioritization (IPS) and roadmap

**IPS (Impact Priority Score, max 70)** = AI_Fit (0-20) + Desirability (0-20) + WedgeFit x5 + DR x5 + MoatBonus (0 or 5). Wave 1 was founder-elevated to 25 features by moving nine mind-mapping and capture features up from Wave 2. Near-term roadmap: harden the mobile voice loop and stabilize the write path; ship Brain Weather v0 (manual signals first), spiciness-slider task decomposition, dual-track planning, gentle streaks, and auto task-extraction; ship preset personas with per-persona voice and CSP v0 with the voice adapter as reference; then focus mode, idle and break support, read-aloud, and MCP server exposure. The F24 interactive-refinement loop ships with the daily-plan work, reusing the F60 conversational-iteration pattern.

## 9. North star: the ADHD paper

> [!IMPORTANT]
> **TL;DR:** Chen, Meng, and Nie (2026), "Not Just Me and My To-Do List" (arXiv 2603.17258), is Yar's north star. Its five design implications drive naming, prioritization, and design; its 13 speed-dating concepts (rated by 20 ADHD adults) are the validated feature backlog.

The five design implications and how Yar embodies each: **relational accountability over solo optimization** (body-doubling F06, adaptive personas); **time as rhythm, not grid** (dual-track planning F07, streaks that honor rest F44, pause days F27); **mood-adaptive interfaces to prevent failure spirals** (voice-biomarker awareness feeding Brain Weather, mood-aware persona selection); **affirming neurodivergent cognition** (the branching brainmap as associative representation, ambient Brain Weather metaphors, no-shame language); and **co-regulation as core infrastructure** (focus companion F06, shared planning F36, the design-partner cohort). Use the paper's vocabulary verbatim (Brain Weather, gentle streaks, pause days, ideal versus baseline, body-doubling, co-regulation) so the product, research, and grant narrative speak one language.

## 10. Cytoscope split (sensor science leaves Yar)

Per the voice-as-sensor rule, the sensing science moves to the **Cytoscope** project; Yar keeps the consumption and user experience. **Pure Cytoscope:** F40 (voice wellbeing SER), F46 (brain sensor hardware). **Shared (science to Cytoscope, in-app surface stays Yar):** F30 (wearable biosignal validation), F54 (DistilHuBERT model artifacts), F62 (clinical instruments). **Voice-as-persona stays Yar** (F11, F29, F45, F57; `SPEC-personas-voice`). Yar consumes sensing; it does not own the sensing science. The sensor-science specs remain in place for now; the Cytoscope agent owns their move.

## 11. Safety: CAP / CAP-Lite

The Controller-Authority Protocol is a hard execution boundary, not advice-time guidance. CAP-Lite (MVP) enforces allowlisted operations only, no external writes without explicit confirmation, raw captures local by default, schema-conformant model output, blocked diagnosis and treatment claims, and uncertainty language for social interpretations. This is the productized version of the platform's CAP and is core to Yar's "suggest, not decide" stance. The full CAP protocol lives under `Cytoplex/` (`cap-readme.md`, `spec/`).

## 12. Design principles

Grounded in Blue Lin's health-data-visualization research and the Chen, Meng, and Nie ADHD study: **sensemaking over prediction**; **user agency primary** (Yar illuminates, the user decides); **progressive disclosure** (a composite "how am I doing?" card, then signal groups, then raw data); **longitudinal context**; **inclusive and neurotype-neutral**; and **no shame, ever** (gentle streaks, pause days, self-compassionate framing). Cognitive-signal color mapping uses the Cytognosis fluorophore palette: Focus azure #3B7DD6, Energy magenta #E0309E, Mood violet #8B3FC7, Sleep and recovery teal #14A3A3, Stress and load coral #F26355.

**What Yar is not:** not a therapist, not a diagnostic tool, not a medical device, not a surveillance product, and not a subscription. It reduces the invisible tax of existing in systems not designed for neurodivergent cognition.

## 13. Strategic fit and positioning

The wedge-to-platform flywheel: Yar wins the daily neurodivergent habit, builds a consented longitudinal multimodal dataset, and feeds the Cytoverse map and Cytonome navigator. The open and proprietary split keeps open science and safety primitives in the Foundation (Apache 2.0, CC BY) and the Yar consumer product plus proprietary tracking in the **PBC** arm; this bifurcation also makes the funding story clean and is the basis of the Summer 2026 YC for-profit consumer positioning (see [`cytonome-track.md`](../../../01-Strategy/tracks/CYTONOME_TRACK_2026-06-03.md), canonical home; the `03-Products/Cytonome/cytonome-track.md` copy is a stub pointer as of 2026-07-16). Yar is positioned as wellness and productivity, not a medical device, with CAP enforcing the line. Its durable differentiation is being the only local-first, voice-first, emotionally aware, unified neurodivergent companion with on-device AI and no subscription, built by and for neurodivergent people.

## 14. Founder and advocacy narrative

Yar exists because its founder lives the problem. The branching brainmap exists because it is how the founder's own mind works; Yar's features are accommodations the founder and community need daily. The community are co-designers ("nothing about us without us"), the warmest first user base, and unprompted data contributors. Disclosure is dial-able: central internally, and a deliberate, calibrated asset externally (YC, grants, partners).

## 15. Open questions and risks

- Storage-engine decision is open (`SPEC-storage-engine`, DRAFT) pending the SurrealDB v3.1.5 retest; reconcile the `AsyncSurreal` vs `AsyncSurrealDB` SDK naming at that retest (see `00-CONSOLIDATION/CONFLICTS.md`).
- External write-path stability (a local fallback exists).
- Vocal-biomarker accuracy and on-device cost and latency.
- Holding the "no diagnosis" line while delivering emotional awareness (CAP is the control).
- Retention versus the abandonment curve (the wedge thesis is the bet; partially de-risked by the warm design-partner cohort).
- Solo-founder bandwidth; co-founder search.

## Cross-references

- **Feature index:** `YAR_FEATURE_CATALOG.md` · **Competitive evidence:** `research/yar-unified-feature-comparison-v4.md`
- **Specs:** `spec/` (14 formal specs; the `spec/adhd/` easy-read variants were archived 2026-07-16, see `_archive/cleanup_2026-07-16/adhd-twins/spec/`) · **Safety and protocol:** `Cytoplex/cap-readme.md`, `Cytoplex/spec/`
- **Identity and YC:** [`cytonome-track.md`](../../../01-Strategy/tracks/CYTONOME_TRACK_2026-06-03.md) (canonical; `03-Products/Cytonome/cytonome-track.md` is a stub pointer) · **Engineering:** `04-Engineering/yar/` (sensors, integrations, reports)
