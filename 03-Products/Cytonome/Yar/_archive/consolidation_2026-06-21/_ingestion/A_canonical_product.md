> **Status**: Generated digest — read-only synthesis of source docs
> **Date**: 2026-06-21
> **Author**: Ingestion agent (subagent of Claude Code)
> **Sources**: 14 product docs under `docs/03-Products/Cytonome/`
> **Missing files**: None — all 14 paths resolved successfully

# Cytonome / Yar / Cytoplex — Canonical Product Digest

**Total distinct features captured:** 54

---

## 1. Architecture and Terminology

### How the Three Layers Relate

```
Cytonome (platform pillar / Navigator)
  └── Yar (consumer app — the productized expression of Cytonome)
        ├── Cytoplex / CAP (safety + authority protocol embedded in Yar; also a standalone lib)
        └── CSP / USAP (sensor adapter protocol — the input layer for Yar)
```

- **Cytonome** is the Navigator pillar of the Cytognosis platform. It is not a product; it is the conceptual layer that Yar and the PBC arm operationalize.
- **Yar** is the shippable consumer product. It is the first and currently only product instance of Cytonome.
- **Cytoplex** is the CAP (Controller-Authority Protocol) runtime. It sits inside Yar as a bundled peer subpackage (`src/cap/`) and as a standalone open-source library in the `cytoplex` repo. It is not a user-facing product; it is an enforcement library that wraps every model call.
- **CAP** is the protocol spec (docs `CAP_00` through `CAP_07`); **Cytoplex** is the package name for the implementation. These terms are interchangeable in engineering contexts but must be distinguished from "Substrate" (retired) and from "CAP" the acronym, which stands for Controller-Authority Protocol (the cytoplex-readme also calls it "Control Authority Protocol" — minor inconsistency; Controller-Authority is the canonical form per cytonome-track.md).
- **CSP** (Cytonome Sensor Protocol) and **USAP** (Universal Sensor Adapter Protocol) are the same protocol. CSP is the primary term in the product master; USAP is used in engineering/sensor docs. A single canonical name is a pending decision.

### Controlled Vocabulary in Use

| Term | Meaning | Use |
|------|---------|-----|
| Cytonome | Navigator platform pillar | Platform layer; not a product name to ship |
| Yar | Consumer cognitive companion app | Ship this |
| Cytoplex | CAP runtime package name | Engineering; library name |
| CAP | Controller-Authority Protocol (spec) | Protocol name; use in spec and external docs |
| CSP | Cytonome Sensor Protocol (primary) | Preferred sensor protocol term |
| USAP | Universal Sensor Adapter Protocol (alt) | Engineering alias for CSP; resolve to one name |
| CAP-Lite | Lightweight CAP for mobile / MVP | MVP safety gate |
| Brain Weather | Cognitive-state visualization dashboard | Use verbatim (from ADHD paper vocabulary) |
| Gentle streaks | No-shame streak tracking | Use verbatim |
| Pause days | Burnout-aware pause mechanism | Use verbatim |
| Cytomark | Browser extension product name | Yar surface; not started |
| PBC | For-profit public benefit corporation | Not yet formed; activates at Gate 1 |
| PEP | Policy Enforcement Point | Cytoplex runtime component |
| PDP | Policy Decision Point | Cytoplex runtime component |

### Retired / Forbidden Terms

| Term | Status | Replacement |
|------|--------|-------------|
| **Substrate** | **RETIRED. Never use.** | "layer", "foundation", or "protocol" |
| **CAP** (as product name) | Acceptable only as acronym in protocol context | "Cytoplex" for the package; "CAP" for the spec |
| Cytonome Assurance Protocol | Stale definition (appears in yar-product-implementation.md glossary) | Correct to "Controller-Authority Protocol" |

**Note:** `cytoplex/runtime/substrate_interop.py` still uses "substrate" as a module name in the codebase — this is a code-level inconsistency with the naming rule; flagged for rename.

---

## 2. Feature Inventory

**Scoring scheme (from CSV `yar-feature-prioritization.csv`):**

| Column | Values / Range |
|--------|---------------|
| `Priority` | P1 (build now), P2 (build next), P3 (Yar-only differentiators / research), Infra (infrastructure) |
| `Yar-only` | Yes / No / Partial |
| `Build Status` | Built, In progress, Planned, Research, Future |

No numeric score column exists. The qualitative priority tiers are the only scoring system. The competitive analysis uses a 0-10 per-category scale (tool totals: Yar target 107/120, Super Productivity 86, OMI 70, etc.), but those scores are not stored per-feature in any file.

### Full Feature Table

| # | Feature Name | Description (1-2 lines) | Product Layer | Priority | ND Domain | Yar-only | Build Status | Source |
|---|-------------|------------------------|--------------|----------|-----------|---------|--------------|--------|
| 1 | Zero-friction voice capture | Real-time voice-to-text capture via platform STT; user edits transcript fallback; Milestone 1 end-to-end pipeline shipped | Yar app | P1 | Task initiation / working memory | No (OMI pattern) | In progress (built) | CSV, yar-product-feature-master.md |
| 2 | Brain-dump compiler | Routes messy voice/text dumps through AI to produce structured typed objects | Yar app | P1 | Working memory | No (Goblin+Letterly) | Planned | CSV, yar-product-feature-master.md |
| 3 | Auto task-extraction from captures | Automatically extracts tasks from free-form captures; no manual parsing required | Yar app | P1 | Task initiation | No (Saner+OMI) | Planned | CSV, yar-product-feature-master.md |
| 4 | Spiciness slider (task decomposition) | Adjustable granularity dial for task breakdown; reduces initiation paralysis | Yar app | P1 | Task initiation | No (Goblin) | Planned | CSV, yar-product-feature-master.md |
| 5 | Brain Weather Dashboard | Ambient cognitive-state visualization; displays focus/energy/mood/sleep/stress axes using fluorophore-mapped colors | Yar app | P1 | Emotional regulation / self-awareness | Yes | Planned | CSV, yar-product-feature-master.md |
| 6 | Social Presence AI (focus companion / body-doubling) | An animated Rive companion that provides presence during focused work; digital body-double | Yar app | P1 | Sustained attention | Yes | Planned | CSV, yar-product-feature-master.md |
| 7 | Dual-track planning (ideal vs. baseline) | Maintains two parallel plans: aspirational and energy-adjusted; no shame on fallback | Yar app | P1 | Time management | Yes | Planned | CSV, yar-product-feature-master.md |
| 8 | Emoji mood on tasks | Lightweight mood tagging on individual tasks | Yar app | P1 | Emotional regulation | No (Leantime) | Planned | CSV |
| 9 | Smart note types (supertags) | LinkML-typed objects as first-class structured notes; schema-aware routing | Yar app | P1 | Working memory | No (Tana) | Partial (LinkML typed objects built) | CSV |
| 10 | Live search queries | Queries as first-class saved objects in the KG; retrievable by name | Yar app | P1 | Working memory | No (Tana) | Planned | CSV |
| 11 | Adaptive personas (relationship type + voice) | Companion persona bundles: relationship stance (coach/buddy/guardian/parent/partner), communication tone, ElevenLabs voice; preset library + manual switch | Yar app | P1 | Companion identity / emotional regulation | Yes | Planned | CSV, yar-product-feature-master §4A |
| 12 | Cytonome Sensor Protocol / USAP (universal sensor adapter) | MCP-style open protocol for plugging any sensor into Yar; lifecycle: discover/connect/configure/read-stream/disconnect; CAP governs every adapter | Cytonome platform / Yar infra | P1 | Infrastructure / platform backbone | Yes | Planned | CSV, yar-product-feature-master §4B |
| 13 | Branching brainmap companion (flagship) | Voice-driven living thought-graph: spoken turns are attached to a growing tree by a placer agent; D3-force visualization; KG-mirrored | Yar app | P1 | Working memory / ideation / self-awareness | Yes | Planned | CSV, yar-product-feature-master §4C |
| 14 | Turn-time attachment reasoning (placer agent) | On-device agent that determines the best parent branch for each new thought before placing it | Yar app | P1 | Working memory / ideation | Yes | Planned | CSV |
| 15 | Force-directed brainmap visualization (D3-force) | Spatial, ambient force-directed graph rendering of the thought-tree | Yar app | P1 | Self-awareness / ideation | Yes | Planned | CSV |
| 16 | Personal-KG integration (Obsidian / LogSeq mirror) | Every brainmap node and edge mirrors into a local personal KG with relative links | Yar app | P1 | Knowledge graph | Yes | Planned | CSV |
| 17 | Private Emotional Notes Before Planning | Private mood capture space before planning sessions; never used for scheduling | Yar app | P1 | Emotional regulation | Yes | Planned | CSV, §7A C1 |
| 18 | CAP safety gate (CAP-Lite) | Hard execution boundary: blocks diagnosis/treatment claims; requires explicit user confirmation before external writes; all model output must conform to schema | Cytoplex / Yar infra | P3 | Privacy / autonomy | Yes | Built (CAP-Lite) | CSV, multiple sources |
| 19 | Local-first AI brain (on-device Gemma) | On-device inference via Gemma 4 E2B/E4B (LiteRT / Ollama); raw data never leaves device by default | Cytoplex / Yar infra | P3 | Privacy | Yes | Built | CSV |
| 20 | Focus mode (full-screen single task) | Distraction-free full-screen single-task mode; ported from Super Productivity FocusModeStrategy | Yar app | P2 | Sustained attention | No (Super Productivity) | Planned | CSV |
| 21 | Idle detection (graceful pause) | Detects user inactivity; gracefully pauses timers; no penalty | Yar app | P2 | Time management | No (Super Productivity) | Planned | CSV |
| 22 | Break reminders (hyperfocus guard) | Gentle prompts to break hyperfocus sessions; no alarm tone | Yar app | P2 | Sustained attention | No (Super Productivity) | Planned | CSV |
| 23 | TTS with text highlighting | Text-to-speech output with synchronized word highlighting (Speechify-style) | Yar app | P2 | Accessibility | No (Speechify) | Planned | CSV |
| 24 | Plan my day | AI-generated daily plan based on tasks, energy, and mood signals | Yar app | P2 | Time management | No (Saner) | Planned | CSV |
| 25 | Tone analysis (Goblin Judge) | Analyzes tone of user's text before sending; identifies potential social misreadings | Yar app | P2 | Social cognition | No (Goblin Tools) | Planned | CSV |
| 26 | PiP focus window | Picture-in-picture focus window that persists across other apps | Yar app | P2 | Sustained attention | No (Saner) | Planned | CSV |
| 27 | Emotionally Aware Pause Days | Detects burnout signals and proactively suggests a full pause day; no guilt framing | Yar app | P2 | Emotional regulation | Yes | Planned | CSV, §7A C11 |
| 28 | MCP server exposure | Expose Yar's captured data and KG via an MCP server for third-party integrations | Yar app / Cytonome platform | P2 | Interop / infrastructure | No (OMI pattern) | Planned | CSV |
| 29 | Persona adaptive refinement (auto-tune) | Persona refines itself from interaction signals and mood; no manual configuration required | Yar app | P2 | Companion identity | Yes | Planned | CSV, §4A |
| 30 | CSP wearable adapter (Oura / Apple Watch) | CSP adapter for wearable sensors: HRV, sleep, activity via Oura / Apple HealthKit / Google Fit | Cytonome platform / Yar | P2 | Sensing / infrastructure | Partial | Planned | CSV |
| 31 | Parallel correction + restructuring agent (the reviser) | Background on-device agent that continuously revisits and proposes corrections to brainmap placements; non-punitive | Yar app | P2 | Working memory / ideation | Yes | Planned | CSV, §4C |
| 32 | Side-thread TODO / reminder capture | Parallel agent that captures a stray task or reminder off the main brainmap flow without interrupting thought | Yar app | P2 | Task initiation / working memory | Yes | Planned | CSV |
| 33 | Personal grammar + lexicon learning | Learns user's personal slang, nicknames, and shorthand; applies in capture and prompts | Yar app | P2 | Communication / capture | Yes | Planned | CSV |
| 34 | Brainstorm-to-artifact operations | Deterministic graph-to-document transforms that convert a brainmap subtree into a proposal, paper, or plan | Yar app | P2 | Ideation / executive function | Yes | Planned | CSV |
| 35 | Emotional Inventory Before New Commitments | Energy-check prompt before accepting new tasks; reduces overcommitment | Yar app | P2 | Emotional regulation / time management | Yes | Planned | CSV, §7A C4 |
| 36 | Shared Planning with a Trusted Person | Opt-in co-regulation: share a planning session with a trusted contact; CAP-guarded | Yar app | P2 | Co-regulation / social | Yes | Planned | CSV, §7A C5 |
| 37 | Ambient Transition Cues | Non-verbal, non-alarming signals for focus/context transitions | Yar app | P2 | Sustained attention / transitions | Yes | Planned | CSV, §7A C7 |
| 38 | Adaptive Planning Undo Button | Soft, no-penalty plan rescope; avoids shame spirals from abandoned plans | Yar app | P2 | Time management | Yes | Planned | CSV, §7A C9 |
| 39 | Pattern-Based Gentle Nudges | Detects recurring friction points and surfaces them as gentle, non-judgmental nudges | Yar app | P2 | Self-awareness / time management | Yes | Planned | CSV, §7A C10 |
| 40 | Voice-first emotional awareness (vocal biomarkers) | Extracts emotion from voice using HuBERT-large + openSMILE eGeMAPSv02; feeds Brain Weather | Yar app | P3 | Emotional regulation | Yes | Research | CSV, §4B |
| 41 | Unified ND companion (task+time+knowledge+emotion+AI) | Single app replacing 7-8 ND tool stack; unified context across all cognitive domains | Yar app | P3 | All | Yes | In progress | CSV |
| 42 | ND-NT Communication Translation | Bidirectional translation: user's intent preserved while adapting tone for NT audiences | Yar app | P3 | Social cognition | Yes | Planned (out of MVP scope) | CSV, cytonome-track |
| 43 | Progressive-disclosure cognitive dashboard | Blue Lin CHI-2024-inspired layered dashboard: composite card → signal groups → raw data | Yar app | P3 | Self-awareness | Yes | Planned | CSV |
| 44 | Gentle streaks (no shame on skip days) | Streak tracking that explicitly handles skip days without punishment or reset | Yar app | P3 | Emotional regulation | Yes | Planned | CSV, §7A C3 |
| 45 | Persona mood/context auto-selection | On-device classifier/bandit that learns which persona the user prefers per mood/context/time | Yar app | P3 | Companion identity / self-awareness | Yes | Planned | CSV, §4A |
| 46 | CSP connectomic adapter (Cytoscope / fNIRS) | CSP adapter for future Cytognosis biosensor hardware; brain-connectomic data into Yar | Cytonome platform | P3 | Sensing / infrastructure | Yes | Future | CSV |
| 47 | Thought deconvolution | Separates interleaved, independent ND thought-threads into distinct brainmap branches | Yar app | P3 | Working memory / ideation | Yes | Research | CSV |
| 48 | Emotional Debrief After Task Collapse | Non-judgmental reflection space offered after a task is abandoned | Yar app | P3 | Emotional regulation / reflection | Yes | Planned | CSV, §7A C12 |
| 49 | Weekly Narrative Reflection | Narrates the week as a story rather than as analytics; no graphs | Yar app | P3 | Self-awareness / reflection | Yes | Planned | CSV, §7A C13 |
| 50 | WADM annotation model (W3C WADM) | W3C Web Annotation Data Model for highlight/annotate/link flows on papers and webpages | Yar infra | Infra | Working memory / capture | No | Built (MVP) | CSV |
| 51 | LinkML-to-Anytype schema mapping | Bidirectional schema mapping: LinkML classes/slots → Anytype Types/Properties/Relations | Yar infra | Infra | Knowledge graph | No | Built (MVP) | CSV |
| 52 | Anytype local-first storage | Local-first, E2E-encrypted knowledge graph backend via Anytype MCP; SQLite fallback | Yar infra | Infra | Privacy / data portability | No | In progress | CSV |
| 53 | Mood-Aware Daily Companion (morning check-in) | Persona-driven daily morning check-in anchored to current mood state | Yar app | P1 (via C2) | Companion identity | Yes | Planned | yar-product-feature-master §7A |
| 54 | Affect detection (voice affect route) | Real-time emotional affect analysis from voice input; exposed as `/routes_affect.py` | Yar app | (not in CSV; coded in structure) | Emotional regulation | Yes | In progress (route exists) | yar-structure.md |

---

## 3. Cytoplex (CAP) Feature Inventory

Cytoplex is a protocol library, not an end-user product. Its capabilities appear in the feature table above as "CAP safety gate" (row 18). Below are its distinct technical capabilities as a library.

| Capability | Description | Status |
|-----------|-------------|--------|
| Local PEP (Policy Enforcement Point) | Full on-device enforcement; intercepts every model call | Production |
| Edge PEP | Lightweight enforcement for constrained environments | Production |
| Attested Local PEP | Hardware-attested enforcement | Scaffold |
| Mobile Local PEP | Constrained-resource on-device enforcement | Scaffold |
| Privacy PDP (Policy Decision Point) | Privacy-specific policy evaluation | Production |
| PDP Adapters | Pluggable PDP backend adapters | Production |
| Supervisor Gateway | Gateway for human-in-the-loop supervisor flows | Scaffold |
| Session Router | Session lifecycle routing | Scaffold |
| Workflow Engine | Multi-step CAP-governed workflow execution | Scaffold |
| Audit Store | Cryptographically signed, persistent audit trail | Production (hardening) |
| Policy Engine | Runtime policy evaluation engine | Production (hardening) |
| Biscuit-v2 Warrant Management | Decentralized, attenuable authorization tokens | Scaffold + tests |
| SPIFFE SVID Workload Identity | Workload identity for cross-service calls | Scaffold |
| Detached-JWS / DSSE / JCS signing | Tamper-evident signed execution records | Tests pass |
| CAPMed profile | Medical/clinical domain profile; extends base CAP | Implemented |
| CAPSWE profile | Software engineering domain profile | Implemented |
| Profile inheritance system | Domain profiles extend base via formal inheritance | Implemented |
| gRPC transport binding | Reference gRPC/protobuf binding for CAP envelopes | Production |
| HTTP/JSON transport binding | Independent HTTP/JSON binding | Production |
| Edge PEP bridge | Transport bridge for edge PEP deployments | Production |
| V1 conformance suite (V1-C01..V1-C15) | Full v1 protocol compliance test suite | 15 gates; release-blocking |
| Schema drift detector | CI gate detecting unintended schema changes | Implemented |
| Therapist-supervisor scenario | 15-case reference deployment scenario | Implemented |
| Semantic quality evaluation | Domain semantic-quality evaluation harness | Implemented |
| LinkML CAP schemas | Canonical schema authoring in LinkML; compiled to JSON Schema | Implemented |
| Go third-implementation adapter | Local Go CAP v1 interop fixture adapter | Implemented |
| PII/PHI redaction engine | Redacts sensitive data from model outputs and audit logs | Scaffold |
| Data retention policies | Configurable retention TTL and deletion checks | Scaffold |
| Human-in-the-loop review flows | Structured escalation for human review decisions | Scaffold |
| Streaming interruption | Mid-stream abort and correction protocol primitives | Scaffold |

---

## 4. Positioning and Wedge

**First-app strategy:** Win the daily ND habit with frictionless capture and execution (Tier 1), then layer communication coaching (Tier 2), then longitudinal sensor data and persona depth (Tier 3). This inverts the 1-2 month abandonment curve that kills wearable and health apps.

**Target users (priority order):**
1. ADHD adults (thought loss, executive dysfunction, shame spirals)
2. Autistic adults (communication mismatch, interface unpredictability)
3. Twice-exceptional adults (knowledge without organization)
4. Late-diagnosed adults (decades of half-working coping)
5. ND researchers and students (hyperfocus capture)

**Go-to-market wedge:**
- Distribution: founder's warm queer/trans/nonbinary/ND community; design-partner program (2-minute opt-in); TestFlight beta first.
- Revenue: freemium at $12/month. Free tier: local capture and structure. Paid: cross-device sync, communication translator, deeper KG, longitudinal insights. Later: B2B tier for employer neurodiversity support and university disability offices.
- Entity path: Yar operates as a for-profit Delaware C-corp (YC path); Foundation holds IP and licenses it to the PBC/operating company.
- Competitive claim: the only local-first, voice-first, emotionally-aware, unified ND companion with on-device AI. Feature score 107/120 vs. best competitor at 86 (Super Productivity).

**Wedge thesis:** Capture tools (OMI, Letterly) capture but do nothing with the output. Execution tools (Super Productivity) execute but have no voice, AI, or emotional awareness. Yar unifies: capture to AI extraction to execution to emotional awareness, in a single local-first app.

---

## 5. Competitor Mentions (Named Tools)

| Tool | Category | Scores | What Yar borrows |
|------|---------|--------|-----------------|
| Super Productivity | Task execution (open-source) | 86/120 | FocusModeStrategy, idle detection, break reminders |
| OMI AI | Voice-first capture (MIT) | 70/120 | Voice stack patterns, MCP server exposure, firmware reference |
| Leantime | Task / project (open-source) | 81/120 | Emoji mood on tasks |
| Tana | Knowledge organizer (proprietary) | 61/120 | Supertags, live search queries |
| Capacities | Knowledge organizer | 61/120 | Object-based KG patterns |
| Anytype | Local-first KG (open-source) | 61/120 | Storage backend selected |
| Saner AI | AI assistant | 63/120 | Plan my day, PiP focus, auto-task |
| Goblin Tools | AI assistant (task decomp) | (part of 12-tool set) | Spiciness slider, tone analysis (Judge) |
| Speechify | Accessibility / TTS | (part of 12-tool set) | TTS with highlighting |
| Letterly | Voice brain-dump | (part of 12-tool set) | Brain-dump patterns |
| ND-Visual MCP | Composable ND infra | (part of 12-tool set) | MCP patterns |
| Gemma 4 (Google) | On-device LLM | Selected | Primary on-device model (E2B/E4B) |
| Cactus | Flutter on-device LLM runtime | Evaluate | Hybrid on/cloud routing, NPU accel |
| LiteRT-LM | On-device inference runtime | Selected | Current mobile runtime |
| Ollama | Desktop LLM host | Selected | Supervisor/desktop model host |
| Whisper | ASR | Evaluated | Voice recognition (Parakeet evaluated as replacement) |
| Parakeet TDT-0.6B | ASR | Evaluate | Faster Apache-2.0 Whisper alternative |
| Kokoro 82M | TTS | Selected | Cascaded pipeline TTS |
| Fish Audio S2 Pro | TTS / voice cloning | Evaluate | Per-persona voice quality |
| ElevenLabs Voice Design | TTS / voice design | Selected | Per-persona voices |
| Moshi 7B | Full-duplex S2S | Monitor | Future full-duplex voice |
| Qwen3.5-Omni | S2S | Evaluate | Cloud supervisor voice |
| HuBERT | Vocal biomarker model | Planned | Speech emotion recognition |
| openSMILE | Acoustic feature extraction | Planned | eGeMAPSv02 for prosody |
| Dapr Agents | Distributed agent runtime | Evaluated (not integrated) | Multi-agent orchestration |
| NATS JetStream | Message bus | Evaluated (not integrated) | Sub-ms LAN messaging |
| LiveKit Agents | WebRTC media | Evaluated (not integrated) | Real-time signal layer |
| Google ADK | Agent orchestration | Evaluated | Gemma-native multi-step planning |
| Iroh Documents | Distributed CRDTs | Evaluated (not integrated) | Distributed state sync |
| Rive | Animation | Selected | Persona visual state machine |
| Neo4j | Graph DB | Planned (Cytoverse) | Production KG |
| Anytype (MCP adapter) | Storage | In progress | Bi-directional KG sync |
| Character Card V3 (CCv3) | Persona schema | Reference | Community persona definition standard |
| SillyTavern | Persona frontend | Reference (not adopted) | Hobbyist character card platform |
| NVIDIA PersonaPlex | Full-duplex persona | Monitor | Emotional persona system |

---

## 6. Architecture Gaps (Features Referenced but Underspecified)

| Gap | Severity | Notes |
|-----|---------|-------|
| Privacy boundary schema (formal) | CRITICAL | Must be drafted before any distributed runtime; schema columns defined in cytonome-master-reference.md §4.2 but no artifact exists |
| Crisis detection subsystem | CRITICAL | Specifically required before any therapy-adjacent use; architecture designed, not built |
| Paralinguistic sensor pipeline (full) | HIGH | Architecture documented; not integrated; VocalBiomarkerFrame storage schema needed |
| Vocal biomarker storage (VocalBiomarkerFrame) | HIGH | Schema type named but not specified |
| Communication Coach (bidirectional ND-NT translation) | HIGH | Defined as P3 / planned; no spec beyond description |
| Cytomark browser extension | HIGH | Likely most-used ND interface; not started; no detailed spec |
| CSP / USAP spec v0 (written document) | HIGH | Protocol described; spec doc not yet published |
| Emotional aftercare module | MEDIUM | Named; no spec |
| Persistent relational context (per-person models) | MEDIUM | Named; no spec |
| Graph RAG design | MEDIUM | Named; no design |
| Distributed runtime (Dapr + NATS) | MEDIUM | Evaluated; not integrated |
| Full-duplex S2S voice (Moshi / LFM) | LOW | Evaluated; not scheduled |
| mDNS peer discovery | LOW | Named; not implemented |
| Multi-org CAP interop | LOW | CAP v2 territory |
| CSP/USAP canonical name resolution | LOW | Two names for one protocol; needs a decision |
| "Substrate" rename in codebase | LOW | `substrate_interop.py` still uses forbidden term |
| Cytoplex v1 full runtime | LOW (for consumer Yar) | v0.1 adequate for launch; v1 needed for regulated/clinical |
| Cactus vs. LiteRT-LM evaluation | MEDIUM | Research complete; evaluation not run |
| Parakeet vs. Whisper ASR evaluation | MEDIUM | Research complete; evaluation not run |

---

## 7. Source File Status

| File | Status |
|------|--------|
| `cytonome-track.md` | Read OK |
| `cytonome-track-simplified.md` | Read OK |
| `Cytoplex/cytoplex-readme.md` | Read OK |
| `Cytoplex/steering/cytoplex-tech.md` | Read OK |
| `Cytoplex/steering/cytoplex-product.md` | Read OK |
| `Cytoplex/steering/cytoplex-structure.md` | Read OK |
| `Yar/yar-product-feature-master.md` | Read OK |
| `Yar/yar-master-features-requirements.md` | Read OK (identical content to yar-product-feature-master.md — these are the same doc at two paths; flagged as duplicate) |
| `Yar/yar-product-implementation.md` | Read OK |
| `Yar/cytonome-master-reference.md` | Read OK |
| `Yar/yar-feature-prioritization.csv` | Read OK — 53 rows + header |
| `Yar/steering/yar-product.md` | Read OK |
| `Yar/steering/yar-tech.md` | Read OK |
| `Yar/steering/yar-structure.md` | Read OK |

**Duplicate alert:** `yar-product-feature-master.md` and `yar-master-features-requirements.md` at their respective paths are byte-for-byte identical in content. One path should be removed or symlinked.
