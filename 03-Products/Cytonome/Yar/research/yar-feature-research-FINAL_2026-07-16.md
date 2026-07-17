> **Status**: Active
> **Date**: 2026-07-16
> **Author**: @shahin (Cytognosis Foundation), consolidated by research agent
> **Audience**: founder (prioritization), product, engineering, grant reviewers
> **Tags**: `yar`, `cytonome`, `feature-matrix`, `neurodiversity`, `final`, `2026-07-16`
> **Consolidates**: `yar-unified-feature-comparison-v4.md` (v4.2), `yar-internal-prioritization-v1.md` (v1.1), `yar-feature-naming-convention.md`, `yar-feature-catalog-public.md`, `yar-salvage-reconciliation-map_2026-07-16.md`, `REQUIREMENTS_COVERAGE.md` (Repo A, 2026-07-05)
> **Does not modify**: any of the five source documents above remain the system of record for their own detail; this file is the single merged reference for founder prioritization.

# Yar Feature Research: Final Consolidated Reference (2026-07-16)

## BLUF

All 62 features (F01-F62) are reconciled into one table below, with build wave, priority score, competitor coverage, research backing, moat status, and real shipped/not-shipped status from the Tauri codebase. **22 features are shipped and tested today** (29/29 e2e, 34/34 backend), 4 are partial or groundwork, 1 is an intentional placeholder, and 35 are not started. Eight features are safety-gated and cannot ship to users until the crisis-detection module and privacy-boundary schema (both still unwritten) are approved. Three genuine conflicts were found across the source documents and are resolved explicitly in Section 9. Five open decisions need your call; they are listed in Section 8.

**If you only read one thing:** Section 8 (what is open) and the master table's Safety-Gated column.

---

## 1. The six-domain ontology

Yar organizes all 62 features under six functional neurodivergence domains, not by diagnosis. A feature lives in the domain of the cognitive or emotional function it primarily supports, regardless of which condition it is most associated with.

**AEF - Attention regulation and executive function.** Task initiation, sustained attention, working memory, planning, and time management. Most relevant to ADHD. 15 features.

**ERM - Emotional regulation and mood.** Mood tracking, burnout support, shame reduction, and emotional aftercare. Most relevant to depression, anxiety, and bipolar conditions. 18 features, and Yar's largest open competitive gap: 15 of 18 have no competitor equivalent at all.

**SCI - Social communication and interaction.** Neurodivergent-to-neurotypical translation, tone calibration, co-regulation, and the social exposome, framed through the double-empathy lens (miscommunication is mutual, not a one-sided deficit). Most relevant to autism. 4 features.

**SPR - Sensory processing and regulation.** The auditory environment, transition cues, and sensory-gentle signaling. 2 features.

**CTO - Cognitive style and thought organization.** Nonlinear ideation, the personal knowledge graph, mind mapping, and schema capture. Home of the branching-brainmap flagship. 16 features.

**SMI - Self-monitoring and interoception.** Longitudinal self-report, sensor integration, and physiological signal tracking. Home of the universal sensor system. 7 features.

15 + 18 + 4 + 2 + 16 + 7 = **62. Confirmed, all features accounted for.**

---

## 2. The CU moat summary

Twenty of the 62 features are anchored to eight named, defensible capability clusters (CU-1 through CU-8). Each is greenfield (little or no prior AI product has shipped it) and each is judged high-impact and high-differentiation in the source research.

| CU | Capability | Feature IDs | Why it is defensible |
|---|---|---|---|
| CU-1 | Your custom tracking axes | F12, F46, F55 | Open, CAP-governed sensor protocol; no competitor has one |
| CU-2 | Social connections and your mood | F42, F56 | Causally links social context to mood, both directions; competitors (Goblin Judge) are stateless and one-way |
| CU-3 | Adaptive companion that builds trust | F11, F29, F45, F57 | On-device persona auto-selection by mood and context; no open competitor ships this |
| CU-4 | Names and terms you use | F33, F58 | Entity recognition seeded from the personal knowledge graph |
| CU-5 | Capture from anywhere | F59 | Phone, desktop, and Chrome extension unified into one capture layer; Memex (WorldBrain) is the closest open reference pattern |
| CU-6 | Conversational thought map | F13, F14, F15, F31, F60 | Transcriber, placer, and reviser agents grow a living thought-graph from speech; novel |
| CU-7 | Thought to document templates | F34, F61 | Deterministic graph-to-artifact transforms, not summarization |
| CU-8 | Opt-in self-assessment tools | F62 | Validated instruments (ASRS, PHQ-9, GAD-7, BRIEF-A, BIS-11) feed Brain Weather under CAP governance |

**A data-quality flag on the "28 unique features" claim:** see Section 9, Conflict 1. The master table below marks each feature's CU status as either a `CU-n` anchor or `Unique (unlabeled)` where the source matrix scores it 0-against-all-competitors but it was not folded into a named cluster. Do not quote "28" externally until you resolve which count you want to stand behind (see Section 8).

---

## 3. Wave structure summary

Waves come from the Integrated Priority Score (IPS) model in `yar-internal-prioritization-v1.md`, **with your founder override for the mindmapping and capture-everywhere clusters already applied.** That override moved 9 features from Wave 2 into Wave 1, so Wave 1 is intentionally larger than a minimal daily-companion MVP would need.

| Wave | Count | What it is |
|---|---|---|
| Infra (in progress) | 5 | Enabling infrastructure: F18, F19, F50, F51, F52 |
| Wave 0 | 2 | Safety and sensor foundations: F12, F55 (plus two non-CSV prerequisites, see Section 8) |
| Wave 1 | 25 | Wedge core plus your elevated mindmap and capture cluster |
| Wave 2 | 24 | Moat depth: differentiators and experience depth |
| Wave 3 | 6 | Sensors and research: wearable, vocal biomarker, connectomic, social exposome, clinical instruments |

5 + 2 + 25 + 24 + 6 = **62. Confirmed.**

---

## 4. Master feature table

Columns: **ID** - **Feature** (affirming public label) - **Construct tag** (psych/neurobehavioral construct; ✓ = confirmed against the naming-convention doc's worked examples, all others are this document's best-fit derivation and should be spot-checked before use in diagnostics-facing work) - **Wave** - **IPS** (0-70 scale) - **Best competitor** (0-10, tool named, 0 = none found) - **CU** - **Research/tool backing** (see legend) - **Implementation status** (from `REQUIREMENTS_COVERAGE.md`, Repo A, verified 2026-07-05) - **Safety-gated**.

**Backing legend:** `CHEN(Cx, m)` = Chen et al. 2026 (arXiv:2603.17258, CSCW), design-concept Cx, participant median m/5. `LIN` = Blue Lin CHI 2024 + IMWUT 2025 design requirements. `VOICE` = voice-model architecture verdict, Section 10.6 of the v4 comparison. `MINDSTRONG` = Mindstrong failure caveat (Perlis, STAT News 2023); research-only framing required. `PATTERN(tool)` = adopt the interaction pattern from a named competitor; not an academic citation. `CU-n` = backed by the CU-n rationale in Section 2 above. `PROXY` = no direct paper or named pattern found; scored only by the internal ND-impact proxy. Where `PROXY` appears with no other tag, that is a genuine research-backing gap, not an omission.

### 4.1 AEF - Attention regulation and executive function

| ID | Feature | Construct tag | Wave | IPS | Best competitor | CU | Backing | Status | Safety-gated |
|---|---|---|---|---|---|---|---|---|---|
| F01 | Voice brain dump | Working memory offload | 1 | 58 | Omi AI (9) | - | PATTERN(Omi AI), VOICE | Shipped (server STT) | N |
| F02 | Brain dump to action plan | Executive function: planning | 1 | 58 | Goblin Tools (8) | - | PATTERN(Goblin Tools) | Shipped | N |
| F03 | Tasks from your words | Executive function: task initiation | 1 | 58 | Saner AI (7) | - | PATTERN(Saner AI) | Shipped | N |
| F04 | Right-sized task breakdown | Executive function: task initiation ✓ | 1 | 58 | Goblin Tools (10) | - | PATTERN(Goblin Tools) | Shipped (gentle form) | N |
| F06 | Focus companion and body doubling | Sustained attention / co-regulation | 1 | 66 | None (0) | Unique (unlabeled) | CHEN(-, 4.5), clinically validated body-doubling literature (general) | Shipped | N |
| F07 | Flexible plan with a backup track | Executive function: cognitive flexibility | 1 | 68 | None (0) | Unique (unlabeled) | CHEN(C3, 5.0) | Shipped (dual-track) | N |
| F20 | Single-task focus mode | Sustained attention | 2 | 51 | Super Productivity (10) | - | PATTERN(Super Productivity) | Not started | N |
| F21 | Graceful activity pause | Prospective memory / task resumption | 2 | 47 | Super Productivity (10) | - | PATTERN(Super Productivity) | Not started | N |
| F22 | Gentle break prompts | Effort self-regulation | 2 | 47 | Super Productivity (10) | - | PATTERN(Super Productivity) | Not started | N |
| F24 | AI morning plan | Executive function: planning | 2 | 53 | Saner AI (7) | - | PATTERN(Saner AI) | Not started | N |
| F26 | Floating task reminder | Prospective memory | 2 | 47 | Saner AI (6) | - | PATTERN(Saner AI) | Not started | N |
| F28 | Open data connections (MCP) | To confirm (infra) | 2 | 47 | Omi AI (8) | - | PATTERN(Omi AI); PROXY (gap: no ND-specific citation) | Not started | **Y** |
| F32 | Stray thought capture | Working memory offload | 1 | 52 | None (0) | Unique (unlabeled) | PROXY (gap) | Shipped | N |
| F41 | All-in-one ND support app | To confirm (product framing, not a construct) | 2 | 48 | None (0) | Unique (unlabeled) | PROXY (gap) | Not started | N |
| F59 | Capture from anywhere | Working memory offload / capture | 1 | 51 | Saner AI ext. (6) | CU-5 | CU-5 (Memex/WorldBrain reference pattern) | Groundwork | N |

### 4.2 ERM - Emotional regulation and mood

| ID | Feature | Construct tag | Wave | IPS | Best competitor | CU | Backing | Status | Safety-gated |
|---|---|---|---|---|---|---|---|---|---|
| F05 | Your energy and mood map | Interoception / affect monitoring | 1 | 69 | None (0) | Unique (unlabeled) | CHEN(C8, 5.0), LIN | Shipped | N |
| F08 | Mood tag on tasks | Affect labeling | 1 | 52 | Leantime (7) | - | PATTERN(Leantime) | Shipped | N |
| F11 | Companion style and voice | Attachment / co-regulation preference | 1 | 64 | None (0) | CU-3 | CU-3 | Shipped (text tones + TTS) | N |
| F17 | Private space before planning | Emotional regulation: pre-processing | 1 | 62 | None (0) | Unique (unlabeled) | PROXY (gap) | Shipped | N |
| F18 | Safety and consent layer (CAP) | Safety / trust (infra) | Infra | 64 | None (0) | - | CAP protocol spec (not academic) | Shipped (UI + native mirror) | N |
| F19 | On-device private AI | Trust / privacy (infra) | Infra | 63 | Anytype storage (9) | - | Substrate decision report, Section 7 of v4 | Not started | N |
| F27 | Rest day support | Emotional regulation: self-compassion | 1 | 67 | None (0) | Unique (unlabeled) | CHEN(-, 4.5); MINDSTRONG caveat (burnout framing) | Shipped | **Y** |
| F29 | Companion that learns your style | Adaptive co-regulation | 2 | 49 | None (0) | CU-3 | CU-3 | Not started | N |
| F35 | Energy check before saying yes | Interoception, boundary-setting | 2 | 46 | None (0) | Unique (unlabeled) | CHEN(C4, 2.0) - rated lower by users than the ND-impact proxy assumed | Not started | N |
| F38 | No-penalty plan change | Cognitive flexibility, self-compassion | 2 | 47 | None (0) | Unique (unlabeled) | CHEN(C9, 2.5) | Not started | N |
| F40 | Voice wellbeing signals (research) | Affect recognition (research-stage) | 3 | 37 | None (0) | Unique (unlabeled) | VOICE; MINDSTRONG caveat (no inference claims until validated) | Not started | **Y** |
| F44 | Streaks that honor rest days | Motivation / self-compassion | 1 | 67 | None (0) | Unique (unlabeled) | CHEN(C3, 5.0) | Shipped | N |
| F45 | Mood-matched companion | Affect-adaptive response | 2 | 48 | None (0) | CU-3 | CU-3 | Not started | N |
| F48 | Gentle reset after a hard day | Emotional regulation, self-compassion ✓ | 2 | 51 | None (0) | Unique (unlabeled) | PROXY (gap) | Not started | **Y** |
| F49 | Your week as a story | Narrative reflection / metacognition | 2 | 50 | None (0) | Unique (unlabeled) | PROXY (gap) | Not started | N |
| F53 | Mood-anchored morning check-in | Affect check-in / metacognition | 1 | 63 | Saner AI (7) | - | CHEN (validates against design principle C2) | Shipped | N |
| F54 | Voice mood awareness | Affect recognition ✓ | 1 | 64 | None (0) | Unique (unlabeled) | VOICE | Placeholder by design (off by default, non-diagnostic) | N |
| F57 | Adaptive companion that builds trust | Trust-building / co-regulation | 1 | 64 | None (0) | CU-3 | CU-3 | Groundwork | N |

### 4.3 SCI - Social communication and interaction

| ID | Feature | Construct tag | Wave | IPS | Best competitor | CU | Backing | Status | Safety-gated |
|---|---|---|---|---|---|---|---|---|---|
| F25 | Pre-send tone check-in | Social pragmatics | 2 | 48 | Goblin Tools (8) | - | PATTERN(Goblin Tools) | Not started | N |
| F36 | Co-planning with a trusted person | Social scaffolding | 2 | 50 | None (0) | Unique (unlabeled) | PROXY (gap) | Not started | **Y** |
| F42 | Two-way communication bridge | Social pragmatics (double empathy) ✓ | 2 | 48 | None (0) | CU-2 | CU-2 | Not started | **Y** |
| F56 | Social connections and your mood | Social exposome / affect linkage | 3 | 43 | None (0) | CU-2 | CU-2 | Not started | **Y** |

### 4.4 SPR - Sensory processing and regulation

| ID | Feature | Construct tag | Wave | IPS | Best competitor | CU | Backing | Status | Safety-gated |
|---|---|---|---|---|---|---|---|---|---|
| F23 | Read-aloud with highlighting | Sensory accessibility / reading support | 2 | 46 | Speechify (9) | - | PATTERN(Speechify) | Not started | N |
| F37 | Gentle context change cues | Sensory transition support | 2 | 44 | None (0) | Unique (unlabeled) | CHEN(C7, 2.0) - rated lower by users than the ND-impact proxy assumed | Not started | N |

### 4.5 CTO - Cognitive style and thought organization

| ID | Feature | Construct tag | Wave | IPS | Best competitor | CU | Backing | Status | Safety-gated |
|---|---|---|---|---|---|---|---|---|---|
| F09 | Structured note types | Metacognition / schema organization | 2 | 47 | Tana (10) | - | PATTERN(Tana) | Partial (types exist) | N |
| F10 | Saved smart searches | Working memory support | 2 | 47 | Tana (10) | - | PATTERN(Tana) | Not started | N |
| F13 | Voice-grown thought map | Nonlinear ideation | 1 | 59 | None (0) | CU-6 | CU-6 | Groundwork (needs AI runtime) | N |
| F14 | Thought placement assistant | Cognitive flexibility, schema organization | 1 | 49 | None (0) | CU-6 | CU-6 | Shipped | N |
| F15 | Spatial thought map view | Spatial cognition | 1 | 48 | None (0) | CU-6 | CU-6 | Shipped | N |
| F16 | Your data in your own tools | Data autonomy (infra) | 1 | 48 | None (0) | Unique (unlabeled) | PROXY (gap) | Shipped (JSON + Markdown export) | N |
| F31 | Thought map reviewer | Metacognition | 1 | 48 | None (0) | CU-6 | CU-6 | Shipped (heuristic; generative later) | N |
| F33 | Your personal vocabulary | Language personalization | 2 | 53 | None (0) | CU-4 | CU-4 | Not started | N |
| F34 | Map to document transform | Executive function: synthesis | 2 | 49 | None (0) | CU-7 | CU-7 | Not started | N |
| F47 | Untangling parallel thoughts | Thought organization, cognitive flexibility ✓ | 3 | 37 | None (0) | Unique (unlabeled) | PROXY (gap); explicitly excluded from founder mindmap elevation, needs unbuilt NLP source-separation model | Not started | N |
| F50 | Highlight and link on any page | Capture / annotation (infra) | Infra | 36 | None (0) | Unique (unlabeled) | W3C WADM standard (technical, not ND-research) | Not started | N |
| F51 | Open schema translation layer | Infra | Infra | 36 | None (0) | Unique (unlabeled) | PROXY (infra) | Not started | N |
| F52 | Private local knowledge store | Infra | Infra | 40 | Anytype (9) | - | Substrate decision report, Section 7 of v4 | Shipped (op-log + projections + search; SQLite/FTS5 next) | N |
| F58 | Names and terms you use | Entity recognition / personalization | 1 | 53 | Tana (8) | CU-4 | CU-4 | Shipped (lite, gazetteer NER) | N |
| F60 | Conversational thought map | Nonlinear ideation, dialogic cognition | 1 | 53 | None (0) | CU-6 | CU-6, LIN (sensemaking layer) | Partial (chat side shipped via GraphRAG; map-editing by conversation is groundwork) | N |
| F61 | Thought to document templates | Executive function: synthesis | 2 | 49 | None (0) | CU-7 | CU-7 | Not started | N |

### 4.6 SMI - Self-monitoring and interoception

| ID | Feature | Construct tag | Wave | IPS | Best competitor | CU | Backing | Status | Safety-gated |
|---|---|---|---|---|---|---|---|---|---|
| F12 | Open sensor connection layer (CSP) | Infra | 0 | 48 | None (0) | CU-1 | CU-1 | Not started | N |
| F30 | Wearable sensor connection | Interoception, physiological awareness | 2 | 41 | Omi AI (7) | - | PATTERN(Omi AI); MINDSTRONG caveat (passive sensing) | Not started | N |
| F39 | Personalized gentle nudges | Behavioral activation | 1 | 59 | None (0) | Unique (unlabeled) | PROXY (gap) | Shipped | N |
| F43 | Layered wellbeing dashboard | Metacognition, self-monitoring | 2 | 48 | None (0) | Unique (unlabeled) | LIN | Not started | N |
| F46 | Brain sensor connection layer | Interoception (future research) | 3 | 27 | None (0) | CU-1 | CU-1; MINDSTRONG caveat (unvalidated future hardware) | Not started | N |
| F55 | Your custom tracking axes | Self-monitoring personalization | 0 | 43 | None (0) | CU-1 | CU-1 | Not started | N |
| F62 | Opt-in self-assessment tools | Standardized self-report (ADHD, depression, anxiety, EF, impulsivity) | 3 | 48 | None (0) | CU-8 | CU-8 (ASRS, PHQ-9, GAD-7, BRIEF-A, BIS-11) | Not started | **Y** |

**Row count check:** AEF 15 + ERM 18 + SCI 4 + SPR 2 + CTO 16 + SMI 7 = **62 rows, matching the 62-feature catalog exactly.**

---

## 5. Implementation status summary

From `REQUIREMENTS_COVERAGE.md` (Repo A, `yar-code-20260705-2354`, verified 2026-07-05) cross-checked against the salvage map (2026-07-16):

| Status | Count | Features |
|---|---|---|
| Shipped | 22 | F01-F08, F11, F14-F18, F27, F31, F32, F39, F44, F52, F53, F58 |
| Partial | 2 | F09 (types exist, not full), F60 (chat side shipped, map-editing groundwork) |
| Groundwork | 3 | F13, F57, F59 |
| Placeholder by design | 1 | F54 (intentionally off by default; "never a diagnosis"; the sensing science itself belongs to Cytoscope, not Yar) |
| Not started | 34 | all remaining IDs |

22 + 2 + 3 + 1 + 34 = **62. Confirmed.** This matches the salvage map's independent claim of "a tested 22-feature slice (29/29 e2e, 34/34 backend tests)" exactly, which is a good cross-validation signal between the two source documents.

---

## 6. Safety-gated features (8)

Eight features cannot ship to users until two prerequisite pieces of infrastructure exist and are reviewed: the **crisis-detection module** and the **privacy-boundary schema**. Neither exists as a built artifact today (Section 8, item 2).

| ID | Feature | Why it is gated |
|---|---|---|
| F27 | Rest day support | Therapy-adjacent burnout framing |
| F28 | Open data connections (MCP) | Exposes user data to external tools |
| F36 | Co-planning with a trusted person | Third-party data visibility |
| F40 | Voice wellbeing signals (research) | Passive biomarker inference; Mindstrong caveat applies directly |
| F42 | Two-way communication bridge | Third-party message content |
| F48 | Gentle reset after a hard day | Therapy-adjacent debrief |
| F56 | Social connections and your mood | Social-data linkage requires sensor infrastructure not yet built |
| F62 | Opt-in self-assessment tools | Clinical instruments (ASRS, PHQ-9, GAD-7, BRIEF-A, BIS-11) require data-collection validity review |

None of these are blocked on anything except the two prerequisite infrastructure pieces; all eight are otherwise buildable now.

---

## 7. Table-stakes vs. moat: the one-paragraph strategic read

Focus and time-management execution, voice capture, and knowledge graphs each already have a strong, well-understood leader (Super Productivity, Omi AI, Tana respectively). Yar should port those interaction patterns, not reinvent them; that is most of the `PATTERN(tool)` rows above. The moat is emotional regulation (15 of 18 ERM features have zero competitor coverage) and the adaptive-persona and branching-brainmap clusters, which are entirely greenfield. Spend build effort disproportionately on the `Unique` and `CU-n` rows; treat the `PATTERN` rows as fast, low-risk ports.

---

## 8. For founder prioritization: what is open

These are the calls only you can make. Each is stated as a recommendation with rationale, per standing practice; proceeding on the recommendation unless you say otherwise.

1. **Crisis-detection module and privacy-boundary schema are both unbuilt and gate 8 features (Section 6).** Recommendation: treat writing both specs as the next infrastructure priority after the YC submission (7/27), since none of the 8 gated features are on the critical path to that deadline. Confirm this sequencing or tell me to pull one forward.

2. **The founder-priority mindmap and capture-everywhere elevation (9 features moved Wave 2 to Wave 1) substantially enlarges Wave 1 scope, and the YC deadline is 11 days out as of 2026-07-16.** Three of those nine (F13, F57, F59) are still groundwork, not shipped. Recommendation: hold the elevation as-is for the roadmap, but do not treat the un-shipped groundwork items as YC-demo blockers; the salvage map already confirms zero scope needs to be pulled in from the legacy repo to hit 7/27. Confirm you're comfortable presenting the 22-feature shipped slice as the YC demo, with the mindmap cluster framed as "in active build," rather than delaying for full mindmap completion.

3. **The "28 Cytognosis-unique features" claim in the v4 comparison doc does not match the matrix's own data** (see Section 9, Conflict 1: the raw count of zero-competitor-score rows is 41, and the named CU-1-through-8 clusters anchor only 20). Recommendation: use "20 features anchored to 8 named, defensible capability clusters, plus 21 additional features with no direct competitor equivalent" as the accurate, defensible framing for investor and grant materials going forward, retiring the "28" figure. Confirm or give me your preferred framing.

4. **Naming reconciliation between the shipped 4-tone `CompanionTone` system (gentle/steady/cheerful/quiet) and the public feature catalog's affirming-label convention.** The salvage map recommends keeping the shipped 4-tone system through YC and revisiting naming post-YC only if desired. Recommendation: accept as stated; this is purely cosmetic and touches UI copy, the op-log schema, and the e2e suite if reopened. Confirm you don't want to touch this before 7/27.

5. **Construct-tag completeness.** Only 5 of 62 construct tags (F04, F42, F47, F48, F54) are drawn directly from the naming-convention doc's worked examples; the remaining 57 are this document's best-fit derivation, marked without a checkmark in Section 4. Recommendation: treat these as provisional until product/research reviews them, since they will matter once Yar's neurobehavioral-axis diagnostics work begins. No action needed before YC; flag for the next research pass.

---

## 9. Conflicts found across sources, and how they were resolved

**Conflict 1 - the "28 unique features" count vs. the matrix data.** `yar-unified-feature-comparison-v4.md` Section 8 states "twenty-eight of the sixty-two features have no competitor equivalent," anchored by CU-1 through CU-8. Counting best-competitor-score rows directly in the same document's Section 4 matrix yields 41 features scored 0 (no competitor), and the CU-1-through-8 clusters themselves anchor only 20 features (two of which, F58 and F59, actually carry nonzero competitor scores of 8 and 6). None of 28, 41, or 20 match each other. Resolution used in this document: report both the CU-anchored count (20) and the raw zero-competitor-score count (41) transparently in Section 4's `CU` column (`CU-n` vs `Unique (unlabeled)`), and flag the discrepancy for your decision in Section 8, item 3, rather than silently picking one number.

**Conflict 2 - wave assignment vs. the older P1/P2/P3/Infra priority tier.** The v4 comparison doc's AI-Fit-based P1 list contains 23 features; the newer IPS-based Wave 1 (with your founder override) contains 25, and the two schemes disagree on where F12 and F55 belong (P1 in v4, but Wave 0 under IPS, because they gate all sensor adapters). Resolution: this document uses **Wave** (IPS-based, founder override applied) as canonical throughout, per your instruction, and does not carry the older P1-P3 tier forward as a column, since `yar-internal-prioritization-v1.md` Section 6 already documents the promotions and demotions between the two schemes in full. If you need the old P-tier for a specific feature, it's in the v4 source doc.

**Conflict 3 - F52 (private local knowledge store) status.** The v4 comparison doc (dated 2026-06-21) lists F52 as "Under evaluation" pending a SQLite-vs-FalkorDB-vs-Anytype-vs-SurrealDB storage decision. `REQUIREMENTS_COVERAGE.md` (2026-07-05) reports F52 as **Shipped**: an op-log-plus-projections architecture, with SQLite/FTS5 as the next projection, and explicitly no Anytype dependency. Resolution: this document reports F52 as Shipped, reflecting the more recent, code-verified source; the storage-engine benchmarking work referenced in `SPEC-storage-engine.md` and `STORAGE_BENCHMARK_TRACKER.md` continues at the projection layer (e.g., FalkorDB for scale) but no longer blocks the foundational architecture choice, which has already been made and shipped.

---

## 10. Honest gaps

- **Research backing is thin outside the ERM domain's headline items.** Only 9 features carry an explicit Chen et al. (2026) participant-desirability citation (F05, F06, F07, F27, F35, F37, F38, F44, F53); three carry Blue Lin design-requirement backing (F05, F43, F60); three carry the voice-model architecture verdict (F01, F40, F54). The remaining ~40 features are backed only by the internal ND-impact proxy score, a named competitor pattern to port, or a CU-cluster rationale, none of which is peer-reviewed evidence of desirability. This is marked `PROXY` throughout Section 4 rather than glossed over.
- **Brain.fm's evidence caveat (one study, symptom-level not diagnosis-level, no public effect sizes) is a citation-hygiene rule for any future audio-focus feature, not a per-feature backing item today**, since no current F-ID is Brain.fm-derived; flagging it here so it isn't lost.
- **Construct tags are 92% derived, not sourced** (57 of 62; see Section 8, item 5).
- **The two CRITICAL safety-gate prerequisites (crisis-detection module, privacy-boundary schema) have no artifact yet**, only draft-stage mentions in the source docs. They are infrastructure, not one of the 62 features, and are not tracked in this table; do not let that omission read as "resolved."

---

## Sources

- `yar-unified-feature-comparison-v4.md` (v4.2, 2026-06-21) - master feature matrix, AI-Fit scoring, CU rationale, academic backing
- `yar-internal-prioritization-v1.md` (v1.1, 2026-06-21) - IPS scores, wave assignments, founder-priority override, safety gates
- `yar-feature-naming-convention.md` (2026-06-21) - dual-label rule, worked construct-tag examples
- `yar-feature-catalog-public.md` (2026-06-21 draft) - plain-language domain groupings, affirming one-line descriptions
- `yar-salvage-reconciliation-map_2026-07-16.md` - implementation-status cross-check, YC-timeline context
- `REQUIREMENTS_COVERAGE.md` (Repo A `yar-code-20260705-2354`, 2026-07-05) - ground-truth shipped/groundwork/placeholder status

---

## Related documents

- [`yar-feature-research-FINAL-simplified_2026-07-16.md`](./yar-feature-research-FINAL-simplified_2026-07-16.md) -- plain-language companion to this doc.
- [`yar-unified-feature-comparison-v4.md`](./yar-unified-feature-comparison-v4.md), [`yar-internal-prioritization-v1.md`](./yar-internal-prioritization-v1.md), [`yar-feature-naming-convention.md`](./yar-feature-naming-convention.md), [`yar-feature-catalog-public.md`](./yar-feature-catalog-public.md) -- the five sources this doc consolidates without replacing.
- [`yar-salvage-reconciliation-map_2026-07-16.md`](./yar-salvage-reconciliation-map_2026-07-16.md) -- the salvage analysis folded into this consolidation.
- [`../YAR_FEATURE_CATALOG.md`](../YAR_FEATURE_CATALOG.md) -- the canonical 62-feature index this research supports.
