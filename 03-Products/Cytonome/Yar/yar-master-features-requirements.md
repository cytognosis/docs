> **Status**: Active
> **Date**: 2026-06-14
> **Author**: @mohammadi
> **Audience**: engineers, stakeholders
> **Tags**: `cytonome`, `features`, `yar`

# Yar — Product, Feature & Implementation Master Reference

**Compiled:** 2026-05-31 · **Status:** canonical consolidated reference (use this going forward)
**Synthesized from** `repos/cytognosis/docs/cytonome/yar/` — anchor: `research/yar-unified-feature-comparison-v3.md`; plus `mvp/01_UPDATED_MVP_SCOPE.md`, `submission/PROJECT_OVERVIEW.md`, and the research/ deep-dives. This is a standalone, portable asset; the repo `docs/cytonome/yar/` remains the dev source of truth.

---

## 1. What Yar is

**Yar is a local-first, voice-aware, AI-native cognitive companion for neurodivergent (ND) adults, built by and for neurodivergent people** — the productized, consumer-facing expression of Cytognosis's **Cytonome** navigator layer. It accepts messy input (voice / text / web context), uses on-device AI to structure it into typed objects in a personal knowledge graph, and helps the user execute, manage time, and stay self-aware — with raw private data staying on-device by default and a hard safety boundary (CAP) blocking diagnosis/treatment/unconfirmed sharing.

**Who it's for:** ND adults (ADHD/autistic/AuDHD and adjacent) for whom continuous tracking and multi-app context-switching fail. **Wedge thesis:** win the *daily habit* first (frictionless capture + execution + self-awareness), then layer "soft sensors" (speech-emotion, patterns) in software, hardware sensors later — inverting the 1–2-month abandonment curve typical of health/wearable apps.

**Relationship to Cytognosis:** Yar is the shippable consumer wedge of the platform — Cytonome (navigator) productized. It builds a consented, longitudinal, multimodal personal dataset that feeds the broader Cytoverse map, and is structured to sit in the **for-profit PBC** arm post-bifurcation (the open science stays in the Foundation). Three architecture features anchor the product: the flagship **branching brainmap companion** (§4C), **adaptive personas** (§4A), and a **universal sensor protocol, "an MCP for sensors"** (§4B). See `StrategicPlanning/` and the funding master.

---

## 2. The Big Gap — why Yar exists

To get through a day, an ND adult currently stitches together **7–8 apps**: Super Productivity (tasks/focus/time) + Goblin Tools (task breakdown/tone) + Tana/Capacities (knowledge) + Saner AI (auto-task/morning plan) + Speechify (listen-don't-read) + OMI (ambient voice capture) + Letterly (brain-dump→text) + Anytype (own your data). That's 7–8 logins and 7–8 silos — and the context-switching between them *is* the executive-function problem they each claim to solve.

And **none** of them have: Brain Weather (cognitive-state visualization), Social Presence AI (digital body-doubling), dual-track planning (ideal vs. baseline), Emotionally Aware Pause Days, CAP safety boundaries, ND↔NT Communication Translation, or vocal-biomarker emotional awareness.

**Yar replaces all of them with one local-first, AI-native, voice-aware, emotionally intelligent companion that keeps data on-device, adapts to the user's brain, and never charges a subscription.** In the 12-tool feature analysis, Yar targets **107/120** vs. Super Productivity 86, OMI 70, Saner 63, Tana/Anytype 61.

---

## 3. Current status — what's actually built (as of 2026-05-17)

The **skeleton-first MVP is implemented**, and **Product Milestone 1 (Mobile Voice)** proves the first real end-to-end mobile voice loop:

```
Flutter mobile voice/text capture
→ on-device (or backend-edge) VoiceIntent routing
→ CAP-Lite mobile directive
→ Yar central coordinator
→ model router (stub / http_json / Ollama; tested with gemma4:e4b)
→ SQLite graph
→ Anytype dry-run write plan
→ explicit user confirmation
→ guarded Anytype MCP write
```

- **Mobile (Flutter, `mobile/`):** Status, Voice, Objects, Anytype Plan, Settings screens; platform STT + editable transcript fallback; on-device **Gemma E2B** `VoiceIntent` via `flutter_gemma`.
- **Backend:** `/voice/*` APIs (voice turns, Anytype plan creation, confirmed write execution, conversation history); deterministic model-router **stub** as default test path; optional Ollama-compatible central routing.
- **Safety:** CAP-Lite is the boundary before model routing **and** before any external write.
- **Storage:** local SQLite graph; **Anytype MCP** write with user confirmation (LinkML-typed objects); SQLite/JSON fallback with an identical adapter interface.
- **Maturity signal:** prior sessions noted 243 passing tests (93 on the safety layer); solo founder; no external users yet; positioned as wellness/productivity (not a medical device, no FDA pathway).

---

## 3A. Design partners & first user base

> [!TIP]
> **Key takeaway**: Yar already has a warm, eager, high-signal first cohort, the founder's own community, which de-risks the hardest part (early retention) and feeds feature prioritization.

The founder is embedded in close, overlapping **queer / trans / nonbinary / poly / neurodivergent** communities, which are high mental-health need, underserved, and exactly Yar's population. This is the natural first user base, and it is already in motion:

- Friends have **sent their whole-genome-sequencing data unprompted**, eager to contribute.
- **Olivia** (software + electrical engineer; wears, uses, and **builds** sensors; the source of our OMI and Letterly findings) is a model **design partner** and a strong **sensor-engineering collaborator** for Cytoscope + the CSP sensor protocol (§4B).
- Many others want to help shape the first-pass feature set or be first users today.

**Plan:** stand up a small **design-partner program** (a 2-minute opt-in, not a recruitment campaign). This cohort prioritizes features (validating Brain Weather, personas, and the first CSP sensors), pilots Milestone 1, and seeds the consented longitudinal dataset. It is the lowest-cost growth path and the foundation of the wedge.

---

## 4. Architecture & implementation

**Pipeline:** `phone capture → desktop/local coordinator → Gemma 4 structuring → CAP-Lite guard → LinkML→Anytype typed objects → read/write/link`.

| Layer | Implementation |
|---|---|
| Capture | Flutter app (voice via platform STT + editable fallback; text; future: web/browser context) |
| Coordination | Local desktop coordinator service: receives captures, calls Gemma 4 (or mock), produces structured object proposals, runs CAP-Lite, executes graph ops, returns reports |
| On-device AI | Gemma 4 family (E2B/E4B) via `flutter_gemma` / LiteRT (mobile) and Ollama (`gemma4:e4b`) (desktop); local-first inference, optional cloud for quality |
| Safety | **CAP / CAP-Lite** (Controller-Authority Protocol): only allowed ops execute; no external writes without confirmation; raw captures stay local; model output must conform to schema; **diagnosis/treatment claims blocked**; uncertain social interpretations must use uncertainty language |
| Schema | **LinkML** classes/slots → **Anytype** Types/Properties/Relations (Class→Type, Slot→Property/Relation, Enum→Select, inheritance→template). Local registry first, then push to Anytype |
| Storage | **Anytype** (local-first, E2E-encrypted, data sovereignty) as the planned backend; SQLite graph as fallback/dev |
| Annotation | **WADM** (W3C Web Annotation Data Model) object model for highlight→annotate→link flows (papers/webpages) |
| Interop | **MCP** server exposure planned (OMI's MCP server is the open reference) |

**Entity types (research space first):** Paper, Author, Dataset, Code, Method (+ Model, Project, Task, Annotation, Collection, Concept).

**Key open-source references mined for patterns:** OMI (MIT full voice stack: firmware+app+backend+MCP), Super Productivity (`FocusModeStrategy`: Pomodoro/flowtime/countdown; idle detection), Leantime (emoji mood tracking), Tana (supertags), Anytype (local-first storage).

---

## 4A. Adaptive personas (companion identity)

Yar's companion is configurable as a **persona** — a bundle of personality/character, **relationship stance** (coach, buddy, guardian, parent, partner, …), communication tone/style, and **voice** (an ElevenLabs Voice-Design voice deployed via on-device TTS). Three commitments make this ND-native, not a gimmick:

1. **Zero configuration tax.** ND users pay a heavy executive-function cost to set up and tune tools, so Yar does **not** require manual persona tuning: the persona **refines itself adaptively from ordinary interaction** — explicit feedback plus implicit signals (engagement, mood-state from the voice-emotion sensor, time/task context) — learning the user's preferences **on-device**. ("Suggest, not decide": every adaptation is inspectable, adjustable, and resettable.)
2. **Multiple personas.** A user can keep several (e.g., a calm *guardian*, an energetic *coach*, a casual *buddy*).
3. **Mood/context-aware selection.** Yar **learns which persona the user prefers in which mood/context** (guardian when overwhelmed/low, coach during planning, buddy for quick capture) and surfaces/suggests it via a lightweight on-device policy keyed on Brain-Weather mood signals, time, and task. Cold-start with sensible defaults; improves with use.

**Why it matters / validation.** Operationalizes the ADHD-paper's highest-rated companion concepts — Social Presence AI / body-doubling (C6) and Mood-Aware Daily Companion (C2) — plus the "no tax / no shame" principle. A companion that *adapts to you* (vs. one you must configure) is the ND-native differentiator.

**Safety (CAP).** Persona learning runs on-device; a persona cannot assert clinical authority or diagnose regardless of stance (CAP blocks this); the user can inspect, edit, switch, or reset any persona and its learned preferences; CAP guards against engagement-maximizing/manipulative optimization.

**Implementation.** Persona = a typed (LinkML) object: `{name, relationship_type, trait/tone params, voice_id (ElevenLabs), prompt template, learned-preference weights}`. Adaptive refinement = on-device preference update from interaction + mood signals. Selection = an on-device classifier/bandit mapping `{mood, context, time, task} → persona`, fully local. Voices via ElevenLabs Voice Design (one-time) → on-device TTS, one voice per persona. UI: a persona library (inspect / edit / disable / reset + manual switch). **Roadmap:** P1 = preset personas + manual switch + per-persona voice; P2 = adaptive refinement from interaction; P3 = learned mood/context auto-selection.

## 4B. Universal Sensor Protocol — "an MCP for sensors" (platform backbone)

The most strategically important addition: a **universal sensor adapter/protocol** — the **Cytonome Sensor Protocol (CSP)**, an MCP-style open interface — that lets users (and third parties) plug *any* sensor into Cytonome/Yar as easily as adding an integration. The voice-emotion sensor is simply the first CSP adapter; CSP turns "each modality is a pluggable sensor the user controls" from a slogan into a concrete, extensible standard.

**What plugs in:** voice (vocal-biomarker emotion); **wearables — Oura, Apple Watch / smartwatches** (HRV, sleep, activity); text/behavior; Cytognosis's own **mood-tracker sensors**; and future **brain-connectomic trackers (Cytoscope / fNIRS)**. CSP is the bridge from the consumer app to the full Cytoverse platform.

**Protocol design (MCP-analogous).** Each sensor adapter declares, via a standard interface: identity/type & modality; the **typed observations/biomarkers it emits** (LinkML schema, so all sensors feed Brain Weather + the knowledge graph uniformly); a **privacy/data-residency class** (on-device-only vs. requires-cloud); consent/permission requirements; sampling cadence; and a `discover → connect → configure → read/stream → disconnect` lifecycle. **CAP governs every adapter:** raw biometric data stays on-device by default; the user grants/revokes each sensor individually; no adapter exfiltrates data without explicit, per-sensor consent.

**Why it matters (most important for us).** (1) Future-proofs Yar for Cytognosis's own hardware (mood tracker, Cytoscope connectomics) with no re-architecture; (2) creates an **open ecosystem** — any organization can build a CSP adapter (Apache 2.0), the same openness pitch we make to partners; (3) unifies every modality into one typed, longitudinal, on-device cognitive picture; (4) keeps privacy guarantees consistent across all inputs.

**Implementation.** Publish the CSP spec (open, Apache 2.0), reusing existing MCP/Anytype patterns (the repo already plans MCP server exposure). Refactor the voice-emotion sensor as the reference CSP adapter; add a wearable adapter (Oura / Apple HealthKit / Google Fit) as the second; ship a "build-your-own-sensor" guide. Each adapter maps raw signals → typed Cytoverse observations. **Roadmap:** P1 = CSP spec v0 + voice adapter (reference); P2 = wearable adapter(s) + third-party adapter guide; P3 = Cytognosis mood-tracker + connectomic (Cytoscope) adapters.

## 4C. Branching Brainmap Companion (the flagship)

> [!IMPORTANT]
> **TL;DR**: Yar's flagship is a voice-driven **living brainmap**. You think out loud, and a companion agent grows a beautiful, self-organizing thought-tree in real time: attaching each new idea where it belongs, quietly fixing earlier mistakes, learning your personal slang, and turning any branch into a proposal, paper, or plan on command. It is the productized Cytonome navigator pointed at your own mind, a GPS for your thoughts.

**The core loop.** You talk. Yar listens, understands your words (including your slang, nicknames, and personal shorthand), and on **each turn reasons carefully about where the new piece best attaches** in the growing graph. The map expands like a tree and **restructures itself adaptively** as the bigger picture becomes clear. You stay in flow; the structure forms around you.

**What makes it ND-native (not just another mind-mapper):**

| Capability | What it does | Why it matters for ND minds |
|---|---|---|
| **Turn-time attachment reasoning** | Each spoken turn, the agent decides the best parent/branch for the new thought before placing it. | Removes the executive-function tax of "where does this go?" that stalls capture. |
| **Adaptive restructuring** | As understanding grows, branches reorganize (split, merge, re-parent) to match the real shape of the idea. | Honors nonlinear, associative thinking instead of forcing a fixed outline. |
| **Parallel correction agent (the reviser)** | A background agent continuously revisits earlier placements and tags, proposing fixes. | Mistakes get repaired without breaking your train of thought. |
| **Personal grammar and lexicon** | Learns your slang, nicknames, and shorthand syntax; tags and gently corrects. | Speaks your language, not a rigid command set. |
| **Thought deconvolution** | Separates interleaved, independent lines of thought into distinct branches. | ND thinking jumps between threads; Yar untangles them for you. |
| **Side-thread capture** | "Add a TODO / reminder" is handled by a parallel agent, off the main flow. | Capture a stray task without losing the thought you were on. |
| **Brainstorm to artifact** | Predefined operations turn a subtree into a proposal, paper, or plan draft. | Closes the gap between divergent ideation and a finished deliverable. |
| **Living visualization** | Force-directed (D3-force) layout: the brainmap as a beautiful, growing tree. | A spatial, ambient representation that affirms cognitive style. |
| **Personal-KG integration** | Every node and edge mirrors into your personal KG (Obsidian / LogSeq), with local, relative links. | Your thinking compounds in a graph you own, on-device. |

**Architecture (how it fits the existing stack).** The brainmap is a **typed (LinkML) thought-graph** stored locally (Anytype / SQLite, the same backend as the rest of Yar). The voice loop is the shipped Milestone 1 capture pipeline. Three on-device agent roles run over the graph: a **placer** (turn-time attachment), a **reviser** (background correction and restructuring), and a **side-thread** agent (TODOs and reminders), all governed by **CAP** (no external writes without confirmation; raw thought stays local; suggest, not decide). "Brainstorm to artifact" operations are deterministic graph-to-document transforms over a selected subtree. Visualization is a D3-force view of the same graph.

**Why it is the flagship.** It is the most vivid expression of every Yar principle at once: local-first and private, voice-first, ND-native, agency-preserving, and KG-backed. It is also the clearest demonstration of **Cytonome as a navigator**: where the platform builds a GPS for human health, the brainmap is a GPS for your own thinking. It is the feature the founder built because **this is how his own mind works**, which is the heart of the by/for-neurodivergent thesis (§9, §13).

**Roadmap.** P1 = voice to brainmap with turn-time placement + D3-force view + KG mirror; P2 = parallel reviser (restructuring and correction) + side-thread TODO capture + personal lexicon; P3 = thought deconvolution + full brainstorm-to-artifact operation set.

**North-star grounding.** Directly serves the ADHD paper's **Affirming Neurodivergent Cognition** (associative, multi-modal representation; §7A implication 4), **Social Presence AI / body-doubling** during thinking (C6), and the spirit of **Adaptive Planning Undo** (C9, the reviser's non-punitive fixes). See §7A.

---

## 5. Feature research & competitive landscape (12-tool)

0–10 per category; Yar target total **107/120** (highest in set). Leaders to learn from: **Super Productivity 86** (tasks/time/focus, open-source), **OMI 70** (voice-first, MIT), **Saner 63**, **Leantime 81**, **Tana/Anytype 61**.

Six market clusters: (A) Task execution engines [Super Productivity, Leantime]; (B) Knowledge organizers [Tana, Capacities, Anytype]; (C) AI assistants [Goblin Tools, Saner]; (D) Accessibility utilities [Speechify]; (E) Composable infrastructure [ND-Visual MCP, Anytype]; (F) **Voice-first capture [OMI, Letterly]**. The defining insight: capture tools (OMI/Letterly) capture beautifully but **do nothing with the captured info**; execution tools (Super Productivity) execute but have **no voice/AI/emotion**. **Yar's wedge is unifying capture → AI extraction → execution → emotional awareness.**

---

## 6. Feature prioritization roadmap

### Priority 1 — build now (paper-validated critical + codebase-informed)
Spiciness slider for task decomposition (Goblin) · zero-friction voice capture (OMI) · brain-dump compiler (Goblin+Letterly) · auto task-extraction from captures (Saner+OMI) · **Brain Weather Dashboard** (ADHD paper C8, highest-rated) · **Social Presence AI / focus companion** (C6) · **dual-track planning, ideal vs. baseline** (C3) · emoji mood on tasks (Leantime) · smart note types / supertags (Tana) · live search queries (Tana).

### Priority 2 — build next
Focus mode (Super Productivity `FocusModeStrategy`) · idle detection · break reminders · TTS with highlighting (Speechify) · "plan my day" (Saner) · tone analysis (Goblin Judge) · PiP focus window · **Emotionally Aware Pause Days** (C11) · MCP server exposure (OMI pattern).

### Priority 3 — Yar-only differentiators (no existing reference)
Voice-first emotional awareness via **vocal biomarkers** (HuBERT/openSMILE prosody) · **CAP safety gate** · **local-first AI brain** (on-device Gemma) · unified ND companion · Brain Weather fed by vocal biomarkers · **ND↔NT Communication Translation** · progressive-disclosure cognitive dashboard (Blue Lin) · **gentle streaks** (no shame on skip days).

*(Full feature×tool matrix and the 39 ADHD-paper-validated requirements are in the companion CSV.)*

---

## 7. Design principles

From **Blue Lin's** health-data-viz research (CHI 2024) + the **Chen, Meng & Nie (2026)** ADHD speed-dating study (20 ADHD adults, 13 concepts):
1. **Sensemaking over prediction** — help users understand cognitive patterns, not just schedule.
2. **User agency primary** — Yar illuminates; the user decides.
3. **Progressive disclosure** — composite "How am I doing?" card → signal groups → raw data.
4. **Longitudinal context** — multi-week overlays reveal a cognitive signature.
5. **Inclusive, neurotype-neutral, culturally responsive.**
6. **No shame, ever** — "Your focus was lower today," not "You had a bad day"; gentle streaks; pause days.

**Cognitive-signal color mapping (Cytognosis brand / fluorophore wavelengths):** Focus = Azure #3B7DD6 · Energy = Magenta #E0309E · Mood = Violet #8B3FC7 · Sleep/recovery = Teal #14A3A3 · Stress/load = Coral #F26355.

---

## 7A. North Star — the ADHD paper's five design implications

> [!IMPORTANT]
> **TL;DR**: Chen, Meng & Nie (2026), "Not Just Me and My To-Do List" (arXiv 2603.17258), is Yar's **north star**. Its **five design implications** drive our naming, prioritization, and design. Its **13 speed-dating concepts** (rated by 20 ADHD adults) are our validated feature backlog. When in doubt about what to build or how to name it, defer to this study.

**The five implications, and how Yar embodies each:**

| # | Design implication (paper) | How Yar embodies it |
|---|---|---|
| 1 | **Relational accountability over solo optimization** | Social Presence AI / body-doubling (C6); adaptive personas as attentive companions (§4A); gentle check-ins, never surveillance. |
| 2 | **Time as rhythm, not grid** | Dual-track ideal vs. baseline planning (C3); gentle streaks that survive skipped days; pause days (C11); energy and mood-aware scheduling. |
| 3 | **Mood-adaptive interfaces to prevent failure spirals** | Vocal-biomarker emotional awareness feeding Brain Weather; mood-aware persona selection (§4A); reduced output framed as self-compassion, not failure. |
| 4 | **Affirming neurodivergent cognition, not pathologizing it** | The **branching brainmap** (§4C) as an associative, nonlinear representation; Brain Weather ambient metaphors ("light fog with patches of clarity"); no-shame language; multiple modes of engagement. |
| 5 | **Co-regulation as core infrastructure** | Social Presence AI focus companion (C6); shared planning with a trusted person (C5); the community design-partner cohort (§3A) as real co-regulation. |

**The 13 concepts, and Yar coverage** (median preference rating from the study in brackets where notable; phases: planning / execution / adaptation / reflection):

| ID | Concept (paper title) | Yar status |
|---|---|---|
| C1 | Private Emotional Notes Before Planning | Planned (private mood capture; never used for scheduling) |
| C2 | Mood-Aware Daily Companion | Core (persona morning check-in, §4A) |
| C3 | Flexible Planning and Gentle Streaks [M=5] | **P1** (dual-track planning + gentle streaks) |
| C4 | Emotional Inventory Before New Commitments | Planned (energy-check prompt on new tasks) |
| C5 | Shared Planning with a Trusted Person | Planned (opt-in; CAP-guarded sharing) |
| C6 | Social Presence AI During Work [M=4.5] | **P1** (focus companion / body-double) |
| C7 | Ambient Transition Cues | P2 (non-verbal focus and transition signals) |
| C8 | Brain-Weather Visualization Dashboard [M=5, highest] | **P1** (flagship dashboard) |
| C9 | Adaptive Planning Undo Button | P1/P2 (soft, no-penalty rescope; also the brainmap reviser) |
| C10 | Pattern-Based Gentle Nudges | P2 (friction-point detection) |
| C11 | Emotionally Aware Pause Days [M=4.5] | P2 (burnout-aware pause suggestion) |
| C12 | Emotional Debrief After Task Collapse | Planned (non-judgmental reflection space) |
| C13 | Weekly Narrative Reflection Instead of Analytics | Planned (narrate the week, not graphs) |

**Naming discipline.** Use the paper's vocabulary verbatim where it exists (**Brain Weather**, **gentle streaks**, **pause days**, **ideal vs. baseline**, **body-doubling**, **co-regulation**), so the product, the research, and the grant narrative all speak one language.

---

## 8. Safety — CAP / CAP-Lite

The Controller-Authority Protocol is a hard execution boundary, not advice-time guidance. CAP-Lite (MVP) enforces: only allowlisted object operations; no external writes without explicit user confirmation; raw captures stay local by default; model output must conform to schema; **diagnosis/treatment claims are blocked**; uncertain social interpretations must use uncertainty language (when communication support is later enabled). This is the productized version of the platform's CAP and is core to Yar's "autonomy vs. guidance" stance ("suggest, not decide").

---

## 9. Strategic fit & positioning

- **Wedge → platform flywheel:** Yar wins the daily ND habit → builds a consented longitudinal multimodal dataset (speech, behavior, patterns) → feeds the Cytoverse map and Cytonome navigator.
- **Open/proprietary split:** open science + safety primitives (Foundation, Apache 2.0/CC BY); Yar consumer product + proprietary tracking → the **PBC** arm. This is the bifurcation that also makes the funding story clean.
- **Not a medical device:** positioned as wellness/productivity (no FDA pathway, no diagnosis) — CAP enforces this.
- **Differentiation vs. the field:** the only local-first, voice-first, emotionally-aware, *unified* ND companion with on-device AI and no subscription.
- **By neurodivergent, for neurodivergent:** Yar is built by an openly ND founder and an ND design-partner community (§3A), not researched from the outside. The people with the highest need are the co-designers, first users, and data contributors. This is an authenticity and trust moat ("nothing about us without us") and the lowest-cost distribution path. See §13.

---

## 10. Roadmap / next milestones (from current skeleton)

1. **Now:** harden the mobile voice loop; stabilize Anytype MCP write; expand entity types beyond research space into personal/task/annotation.
2. **P1 features:** Brain Weather v0 (manual signals first), spiciness-slider task decomposition, dual-track planning, gentle streaks, auto task-extraction; **preset personas + per-persona voice**; **Cytonome Sensor Protocol (CSP) v0 + the voice adapter as reference**.
3. **Then:** focus mode + idle/break (port Super Productivity patterns), TTS, "plan my day," MCP server.
4. **Yar-only:** vocal-biomarker emotional awareness → Brain Weather; Communication Translation; progressive-disclosure dashboard.
5. **Co-founder:** seeking an ND co-founder; solo founder today.

---

## 11. Open questions / risks
- Anytype MCP write stability (fallback exists).
- Vocal-biomarker accuracy + on-device cost/latency.
- Maintaining the "no diagnosis" line while delivering emotional awareness (CAP is the control).
- Retention vs. the abandonment curve (the wedge thesis is the bet; partially de-risked by the warm design-partner cohort, see §3A).
- Solo-founder bandwidth; co-founder search.

## 12. Source index (repo)
`research/yar-unified-feature-comparison-v3.md` (anchor) · `research/{omi-ai,letterly,blue-lin,tana,capacities,adhd-paper-synthesis,codebase-analysis,cap_yar_comprehensive_reference,...}` · `mvp/01_UPDATED_MVP_SCOPE.md` + `mvp/*` · `submission/{PROJECT_OVERVIEW,ARCHITECTURE,ROADMAP,SAFETY_AND_TRUST,EVALUATION,LIMITATIONS}.md` · `product-implementation.md` · `cytonome-master-reference.md` · `yar_revision_plan.md`.

**Component doc sets (now nested under Yar in the repo):**

| Component | Repo path | What it is |
|---|---|---|
| **Cytoplex** | `docs/cytonome/yar/cytoplex/` | The home of **CAP (Controller-Authority Protocol)**: Yar's safety, authority, and coordination component. Standalone spec, integrated as Yar's hard execution boundary (§8). Entry: `cytoplex/README.md`. |
| **Sensors** | `docs/cytonome/yar/sensors/` | The sensing component: the **CSP (Cytonome Sensor Protocol)**, also called **USAP (Universal Sensor Adapter Protocol)** in the engineering docs (same protocol). Standalone sensor architecture + adapters, integrated as Yar's input layer (§4B). Entry: `sensors/README.md`. |

> [!NOTE]
> **Naming note**: **CSP** and **USAP** refer to the same sensor protocol. This master uses **CSP** as the primary term; the `sensors/` doc set uses **USAP**. A single canonical name is a pending decision (see the iteration checkpoint).

---

## 13. Founder and advocacy narrative (by/for neurodivergent)

> [!NOTE]
> **TL;DR**: Yar exists because its founder lives the problem. Shahin is an openly neurodivergent, queer founder who works to break the taboo around mental health and who has a track record of building inclusive structures (diversity groups and HR/DEI planning at insitro). The advocacy is not adjacent to the product; it is the product thesis.

- **Lived experience as design source.** The branching brainmap (§4C) exists because it is how the founder's own mind works. Yar's features are accommodations the founder and community need daily, not abstractions.
- **Community as co-designers.** The founder is embedded in close, overlapping queer / trans / nonbinary / poly / neurodivergent communities (§3A): the warmest first user base, eager design partners, and unprompted data contributors. "Nothing about us without us" is literal here.
- **Taboo-breaking advocacy.** The founder is openly active in normalizing conversations about mental health and neurodivergence. Building in the open, and openly ND, is itself the credibility and reach strategy.
- **Track record of inclusive building.** At insitro, the founder helped lead diversity groups, activities, and HR/DEI planning: evidence of building inclusive structures, not just talking about them.
- **Disclosure is dial-able.** In external materials (YC, grants, partners), the founder controls how much of this to foreground per audience. Internally it is central; externally it is a deliberate, calibrated asset.
