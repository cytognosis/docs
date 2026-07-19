> **Status**: Active
> **Date**: 2026-06-21
> **Author**: @shahin (Cytognosis Foundation)
> **Audience**: founders, product, engineering, grant reviewers
> **Tags**: `yar`, `cytonome`, `cytoplex`, `market-research`, `feature-matrix`, `neurodiversity`, `v4`
> **Supersedes**: `yar-unified-feature-comparison-v3.md` (archive on merge)
> **Version note**: v4.2 (2026-06-21): applied affirming, psych-aligned feature naming.

# Yar Unified Feature Comparison and AI-Fit Prioritization (v4)

> **Reading time**: ~20 minutes.
> **If you only read one thing**: the **P1 build list** in Section 9 and the **AI-Fit master matrix** in Section 4. Yar's defensible moat is the cluster of emotional-regulation and adaptive-companion features that no competitor ships, not the task and focus features that several competitors already do well.
> **Reading options:** An ADHD-friendly progressive-disclosure rendering is generated from this file. The hand-maintained ADHD twin (`yar-unified-feature-comparison-v4-adhd.md`) was retired 2026-07-16; see `_archive/cleanup_2026-07-16/adhd-twins/research/`.

---

## 1. Research Objective

**Domain.** Consumer and prosumer tools that support neurodivergent people across attention, mood, social communication, sensory regulation, thought organization, and self-monitoring.

**Key question.** Which Yar features create a defensible, AI-native advantage for neurodivergent users, which features are table stakes that competitors already deliver well, and how should the build sequence follow from that split?

**What is new in v4.** This version unifies four prior research streams, adds three tools and seven personal-knowledge-management comparators that v3 lacked, folds in Cytognosis's eight unique capabilities as first-class rows, and adds an **AI-Fit scoring layer** on top of the existing competitor scores so features can be prioritized by how much artificial intelligence improves them and how crowded the space already is.

**Framing note.** This document groups features by **functional neurodivergence domain**, not by diagnosis. Social communication differences are framed through the double-empathy lens (a two-way translation problem, not a one-way deficit), and all language is person-first and affirming while remaining clinically precise.

---

## 2. Candidate Identification

**Search strategy.** Four research passes: ingestion of all prior Cytonome, Yar, and Cytoplex docs; the v3 scored matrix; deep web research on tools the founder named; and verification of the academic sources.

**Inclusion criteria.** Tools that (a) target one or more neurodivergence domains, (b) ship a real product or peer-reviewed result, and (c) inform a Yar feature decision.

**Exclusion criteria.** Generic productivity suites with no neurodivergence angle, and marketing pages with no shipped product (flagged where they appear).

**Candidate counts.**

| Set | Count |
|---|---|
| Tools fully scored (0-10 per feature, v3 matrix) | 12 |
| Tools assessed as references or comparators (briefs C and D) | 6 |
| Personal-knowledge-management comparators (substrate analysis) | 7 |
| Total named tools represented | 18 |
| Unified features after de-duplication | 62 |
| Of those, anchored to 8 named, defensible capability clusters (D-B) | 20 |
| Additional Cytognosis-unique features with no direct competitor equivalent | 21 |
| Academic sources verified | Chen et al. 2026 (CSCW), Brain.fm Communications Biology 2024, Blue Lin CHI 2024 + IMWUT 2025 |

> **Taxonomy update (2026-07-18):** Two features (F63 invisible-disability advocacy mode, F64 personal compass) were added on 2026-07-18 per decision D-E; they have no competitor equivalent and are not yet scored in this matrix. Current taxonomy total: 64.
>
> **Domain hierarchy** (6 domains, 19 clusters, 64 features): see `FEATURE-HIERARCHY.md` and `features.json` in this folder.

---

## 3. Scoring Methodology

This document uses two scoring layers. The first is carried forward verbatim from v3; the second is new in v4.

### 3.1 Competitor feature score (0-10), carried forward

> Scores use a 0-10 scale: **0** = absent, **3** = basic or limited, **5** = adequate, **7** = strong, **10** = best-in-class within this comparison set. Scores weight actual user experience over marketing claims.

### 3.2 AI-Fit scoring layer (new in v4)

Each feature is rated on five axes, 0 to 5, then combined.

| Axis | 0 means | 5 means |
|---|---|---|
| **AI leverage** | Rule-based; no meaningful AI contribution | AI is the entire mechanism; impossible without machine learning |
| **Prior-AI maturity** | Greenfield; no one has shipped AI here | Mature AI products exist with strong adoption |
| **Differentiation** | Competitors match Cytognosis on this | Cytognosis holds a structural, defensible advantage |
| **Neurodivergent impact** | Marginal to the core experience | Critical to the core value proposition |
| **Feasibility** | Years of R&D or unbuilt hardware | Shippable this build cycle with known tools |

**AI-Fit Score (0-20) = AI leverage + differentiation + neurodivergent impact + feasibility.** Prior-AI maturity is reported separately as a crowdedness signal, not summed, because low maturity is an opportunity (open moat) rather than a penalty.

**How to read the two numbers together.** A high AI-Fit Score with **low** prior-AI maturity is a defensible greenfield moat (build it, own it). A high competitor score with **high** prior-AI maturity is table stakes (adopt or port a known pattern, do not reinvent it).

### 3.3 Priority tiers

| Tier | Rule | Meaning |
|---|---|---|
| **P1** | AI-Fit ≥ 16 and neurodivergent impact ≥ 4, or a table-stakes capture primitive | Build now |
| **P2** | AI-Fit 13 to 17, or strong impact with lower feasibility | Build next |
| **P3** | High impact and high differentiation but low feasibility, or future-dependent | Differentiator and research track |
| **Infra** | Enabling infrastructure under the features above | Foundational, not user-facing |

---

## 4. Master Feature Matrix (AI-Fit, by neurodivergence domain)

Feature names below are the affirming public labels. Internal names and psychological construct tags are in `yar-feature-matrix-v4.csv` and `yar-feature-naming-map.csv`.

Each feature is listed under its primary domain. Full 15-column data, including per-axis AI-fit scores and the "who has tried AI here" notes, lives in `yar-feature-matrix-v4.csv`. Best Competitor shows the strongest tool on that feature with its 0-10 score; **0 means no competitor ships anything equivalent**.

### 4.1 AEF: Attention regulation and executive function

Covers task initiation, sustained attention, working memory, planning, and time management (relevant to ADHD).

| ID | Feature | Yar Status | Best Competitor (0-10) | AI-Fit /20 | Prior-AI /5 | Priority |
|---|---|---|---|:---:|:---:|:---:|
| F01 | Voice brain dump | In progress | Omi AI (9) | 18 | 4 | P1 |
| F02 | Brain dump to action plan | Planned | Goblin Tools (8) | 18 | 4 | P1 |
| F03 | Tasks from your words | Planned | Saner AI (7) | 18 | 4 | P1 |
| F04 | Right-sized task breakdown | Planned | Goblin Tools (10) | 18 | 3 | P1 |
| F06 | Focus companion and body doubling | Planned | None (0) | 18 | 1 | P1 |
| F07 | Flexible plan with a backup track | Planned | None (0) | 18 | 1 | P1 |
| F20 | Single-task focus mode | Planned | Super Productivity (10) | 16 | 4 | P2 |
| F21 | Graceful activity pause | Planned | Super Productivity (10) | 15 | 4 | P2 |
| F22 | Gentle break prompts | Planned | Super Productivity (10) | 15 | 4 | P2 |
| F24 | AI morning plan | Planned | Saner AI (7) | 18 | 3 | P2 |
| F26 | Floating task reminder | Planned | Saner AI (6) | 15 | 3 | P2 |
| F28 | Open data connections (MCP) | Planned | Omi AI (8) | 15 | 3 | P2 |
| F32 | Stray thought capture | Planned | None (0) | 17 | 1 | P2 |
| F41 | All-in-one ND support app | In progress | None (0) | 18 | 1 | P3 |
| F59 | Capture from anywhere | Planned | Saner AI ext. (6) | 16 | 2 | P2 |

### 4.2 ERM: Emotional regulation and mood

Covers mood tracking, burnout detection, shame reduction, and emotional aftercare (relevant to depression, anxiety, and bipolar conditions). **This is Yar's largest open moat: 15 of 18 features have no competitor equivalent.**

| ID | Feature | Yar Status | Best Competitor (0-10) | AI-Fit /20 | Prior-AI /5 | Priority |
|---|---|---|---|:---:|:---:|:---:|
| F05 | Your energy and mood map | Planned | None (0) | 19 | 1 | P1 |
| F08 | Mood tag on tasks | Planned | Leantime (7) | 15 | 3 | P1 |
| F11 | Companion style and voice | Planned | None (0) | 19 | 1 | P1 |
| F17 | Private space before planning | Planned | None (0) | 17 | 1 | P1 |
| F18 | Safety and consent layer (CAP) | In progress | None (0) | 19 | 2 | P3 |
| F19 | On-device private AI | In progress | Anytype storage (9) | 18 | 3 | P3 |
| F27 | Rest day support | Planned | None (0) | 19 | 1 | P2 |
| F29 | Companion that learns your style | Planned | None (0) | 19 | 1 | P2 |
| F35 | Energy check before saying yes | Planned | None (0) | 18 | 1 | P2 |
| F38 | No-penalty plan change | Planned | None (0) | 17 | 1 | P2 |
| F40 | Voice wellbeing signals (research) | Research | None (0) | 17 | 2 | P3 |
| F44 | Streaks that honor rest days | Planned | None (0) | 17 | 1 | P3 |
| F45 | Mood-matched companion | Planned | None (0) | 18 | 1 | P3 |
| F48 | Gentle reset after a hard day | Planned | None (0) | 19 | 1 | P3 |
| F49 | Your week as a story | Planned | None (0) | 18 | 1 | P3 |
| F53 | Mood-anchored morning check-in | Planned | Saner AI (7) | 18 | 2 | P1 |
| F54 | Voice mood awareness | In progress | None (0) | 19 | 2 | P1 |
| F57 | Adaptive companion that builds trust | Planned | None (0) | 19 | 1 | P1 |

### 4.3 SCI: Social communication and interaction

Covers neurodivergent-to-neurotypical translation, tone calibration, co-regulation, and the social exposome (relevant to autism, framed through the double-empathy problem).

| ID | Feature | Yar Status | Best Competitor (0-10) | AI-Fit /20 | Prior-AI /5 | Priority |
|---|---|---|---|:---:|:---:|:---:|
| F25 | Pre-send tone check-in | Planned | Goblin Tools (8) | 18 | 2 | P2 |
| F36 | Co-planning with a trusted person | Planned | None (0) | 18 | 1 | P2 |
| F42 | Two-way communication bridge | Planned | None (0) | 18 | 1 | P3 |
| F56 | Social connections and your mood | Planned | None (0) | 18 | 1 | P2 |

### 4.4 SPR: Sensory processing and regulation

Covers the auditory environment, transition cues, and sensory-gentle signaling.

| ID | Feature | Yar Status | Best Competitor (0-10) | AI-Fit /20 | Prior-AI /5 | Priority |
|---|---|---|---|:---:|:---:|:---:|
| F23 | Read-aloud with highlighting | Planned | Speechify (9) | 16 | 3 | P2 |
| F37 | Gentle context change cues | Planned | None (0) | 16 | 1 | P2 |

### 4.5 CTO: Cognitive style and thought organization

Covers nonlinear ideation, the personal knowledge graph, mind mapping, and schema capture. This is where the **branching brainmap** flagship lives.

| ID | Feature | Yar Status | Best Competitor (0-10) | AI-Fit /20 | Prior-AI /5 | Priority |
|---|---|---|---|:---:|:---:|:---:|
| F09 | Structured note types | Partial | Tana (10) | 15 | 3 | P1 |
| F10 | Saved smart searches | Planned | Tana (10) | 15 | 3 | P1 |
| F13 | Voice-grown thought map | Planned | None (0) | 19 | 1 | P1 |
| F14 | Thought placement assistant | Planned | None (0) | 17 | 1 | P1 |
| F15 | Spatial thought map view | Planned | None (0) | 16 | 1 | P1 |
| F16 | Your data in your own tools | Planned | None (0) | 16 | 2 | P1 |
| F31 | Thought map reviewer | Planned | None (0) | 18 | 1 | P2 |
| F33 | Your personal vocabulary | Planned | None (0) | 16 | 2 | P2 |
| F34 | Map to document transform | Planned | None (0) | 19 | 1 | P2 |
| F47 | Untangling parallel thoughts | Research | None (0) | 17 | 1 | P3 |
| F50 | Highlight and link on any page | In progress | None (0) | 14 | 2 | Infra |
| F51 | Open schema translation layer | In progress | None (0) | 14 | 2 | Infra |
| F52 | Private local knowledge store | Under evaluation | Anytype (9) | 15 | 3 | Infra |

> **Note (2026-06-21):** F50, F51, and F52 were previously labeled Built. Status corrected to In progress or Under evaluation. The storage engine (F52: Anytype vs SurrealDB vs other) and cross-node sync protocol are open decisions, documented in SPEC-storage-engine.md, SPEC-sync-protocol.md, and STORAGE_BENCHMARK_TRACKER.md.

| F58 | Names and terms you use | Planned | Tana (8) | 18 | 2 | P1 |
| F60 | Conversational thought map | Planned | None (0) | 18 | 1 | P1 |
| F61 | Thought to document templates | Planned | None (0) | 19 | 1 | P2 |

### 4.6 SMI: Self-monitoring and interoception

Covers longitudinal self-report, sensor integration, and physiological signal tracking. This is where the **universal sensor system** lives.

| ID | Feature | Yar Status | Best Competitor (0-10) | AI-Fit /20 | Prior-AI /5 | Priority |
|---|---|---|---|:---:|:---:|:---:|
| F12 | Open sensor connection layer (CSP) | Planned | None (0) | 16 | 1 | P1 |
| F30 | Wearable sensor connection | Planned | Omi AI (7) | 16 | 2 | P2 |
| F39 | Personalized gentle nudges | Planned | None (0) | 17 | 1 | P2 |
| F43 | Layered wellbeing dashboard | Planned | None (0) | 18 | 1 | P3 |
| F46 | Brain sensor connection layer | Future | None (0) | 13 | 1 | P3 |
| F55 | Your custom tracking axes | Planned | None (0) | 16 | 1 | P1 |
| F62 | Opt-in self-assessment tools | Planned | None (0) | 18 | 1 | P2 |

---

## 5. Comparative Landscape Analysis

The neurodivergence tool market splits into well-served lanes and one almost-empty lane. Task and focus execution, voice capture, and knowledge graphs each have a clear leader: Super Productivity, Omi AI, and Tana respectively, with Goblin Tools leading neurodivergent-native task UX. No tool covers more than two or three of the six functional domains. Saner AI is the closest to a unified companion, yet it carries no emotional-regulation or interoception layer at all.

The decisive gap is emotional regulation. Fifteen of eighteen emotional-regulation features have zero competitor coverage, and the adaptive-persona and branching-brainmap clusters are entirely greenfield. These are also the highest AI-Fit features, because they depend on on-device inference, mood-state modeling, and multi-agent reasoning that rule-based tools cannot replicate. Where competitors are strong, in focus timers, supertags, and text-to-speech, the work is well understood and largely solved, so Yar should port proven patterns rather than rebuild them.

Yar's defensible position is the unified, emotionally aware, on-device companion spanning all six domains, anchored by the Brain Weather dashboard, adaptive personas, and the branching brainmap. The augmentation framing, assist and never replace care, is both the honest position and the one the Mindstrong failure shows is commercially necessary. The wedge is the ADHD daily-companion experience; the moat is the emotional-regulation and adaptive-companion layer no competitor is building.

## 6. Bullet-Point Summary

- **Strongest contender:** Super Productivity (86/120) for task and focus, fully open-source under MIT, and the pattern source for Yar's focus stack.
- **Emerging trend:** open, composable capture. Omi AI ships an MCP server and pluggable speech-to-text, pointing toward an interoperable sensor and capture layer rather than walled gardens.
- **Underserved need:** emotional regulation and shame-free planning, almost entirely absent across all eighteen tools, and the highest-rated concept cluster in Chen et al. (2026).
- **Licensing risk:** the strongest companion patterns (Tana supertags, Goblin Judge, Saner proactive model) are proprietary, so Yar must adopt the concepts on open foundations (LinkML, on-device models), not copy code.
- **Integration opportunity:** Omi's open MCP and Anytype's local-first encrypted storage are directly adoptable as Yar's capture and storage foundation.

## 7. Candidate Groups

### Leaders (best-in-class in their lane)

| Tool | Lane | Score | Strength | Weakness for ND use |
|---|---|:---:|---|---|
| Super Productivity | Task and focus execution | 86 | Mature focus, idle, break logic; MIT; local | No emotional layer, no AI |
| Omi AI | Voice-first capture | 70 | Open-source, MCP server, pluggable STT, ambient capture | Cloud-first storage; no mood model |
| Tana | Knowledge and schema capture | 61 | Supertags, voice-to-typed-node, live search | Proprietary schema; steep onboarding |
| Goblin Tools | Neurodivergent task UX | 57 | Spiciness slider, unique Judge tone tool | Stateless; no memory or context |

### Contenders

| Tool | Score | Strength | Weakness |
|---|:---:|---|---|
| Leantime | 81 | Project management with emoji mood on tasks; LEO agent | Team-PM framing, not personal companion |
| Saner AI | 63 | Closest to Yar UX; proactive morning plan; ADHD-explicit | No emotional regulation or interoception |
| Anytype | 61 | Local-first, end-to-end encrypted, object model | Storage only; no companion or AI |
| Capacities | 58 | Object-first PKM; daily-note inbox | No proactive surfacing; rate-limited AI |

### Niche, emerging, and reference-only

| Tool | Role | Note |
|---|---|---|
| Speechify | Accessibility (TTS) | Best-in-class read-aloud; pattern to port |
| Letterly | Voice brain-dump | Narrow; single-purpose |
| AFFiNE | Canvas + notes (PKM) | Infinite canvas, ADHD planner templates; strongest open PKM fit |
| Obsidian, Logseq, Notion | PKM comparators | Rich but high setup friction is itself a neurodivergent barrier |
| Brain.fm | Functional audio | One peer-reviewed study; evidence thinner than marketing (see 10.2) |
| Lovable.dev | AI app builder | Mind-map-from-prompt pattern only; not a shipped ND product |
| Mindstrong (defunct) | Digital phenotyping | Cautionary failure case (see 10.1) |
| Blue Lin | Design research | CHI 2024 + IMWUT 2025; design evidence base, not a product (see 10.4) |

### Storage-layer role conclusions (from `yar-substrate-decision.md`)

The substrate decision report (2026-06-14) assessed nine PKM tools against Yar's CAP-governance, privacy, and local-first requirements. The conclusions that directly affect product and engineering decisions:

**Obsidian** (MVP 8/10, long-term 7/10): preferred adapter target. Maximum data ownership, no required account, no app telemetry, official clipper, and mature plugin ecosystem make it the fastest route to local capture and plugin-side CAP orchestration. It does not become the canonical source of truth; Yar's own runtime owns the schema.

**Logseq** (MVP 6/10, long-term 5/10): inspiration only. Strong block-graph semantics and open-source lineage are valuable; however, the ongoing DB-mode transition creates integration risk. Do not depend on it as a storage surface.

**AFFiNE** (MVP 6/10, long-term 5/10): inspiration only. Promising local-first workspace with ADHD planner templates and infinite canvas, but extension points are not yet mature enough for production integration.

**Notion** (MVP 4/10, long-term 2/10): reject. Cloud-first architecture and a trust boundary that sits with Notion rather than with Yar make it structurally incompatible with the CAP promise for mental-health-adjacent data.

**Capacities** (MVP 5/10, long-term 3/10): reject. Capacities explicitly does not use end-to-end encryption, and sync cannot be disabled by the user. Those properties disqualify it for a mental-health-adjacent companion regardless of its object-model strengths.

**Tana** (MVP 6/10, long-term 3/10): adopt the supertag concept, reject as a governed data layer. Tana's supertag schema is proprietary, which means CAP cannot govern the authority model if Yar relies on Tana's schema. A user whose data lives in Tana's schema is subject to Tana's authority, not Yar's. The Input API is useful for adapter experiments only; it must not become the canonical write path.

**Anytype** (MVP 8/10, long-term 6/10): MVP storage backend only. Best existing off-the-shelf match for typed PKG requirements; its localhost Local API and official MCP support are genuinely useful for MVP iteration. Long-term limitations: desktop app uses the Any Source Available License (not MIT/Apache), app-usage analytics cannot be disabled without host blocking, and the API surface is still maturing. Material for the engineering risk register. Any analytics caveat matters for sensitive reflection data.

## 8. Cytognosis Unique-Feature Strategy

Twenty of the sixty-two features are anchored to eight named, defensible capability clusters that define Yar's moat. A further twenty-one features have no direct competitor equivalent but are not yet anchored to a named cluster. Each anchored capability is greenfield (prior-AI maturity 0 to 2), high impact, and high differentiation.

| CU | Capability | Feature IDs | Why it is defensible |
|---|---|---|---|
| CU-1 | Your custom tracking axes | F12, F55, F46 | No competitor has an open, CAP-governed sensor protocol; new health axes become first-class citizens |
| CU-2 | Social connections and your mood | F42, F56 | Links social context causally to mood; Goblin Judge is stateless and one-directional by comparison. The coach triggers before the user sends a message or after a flagged social interaction, and it outputs a gentler rephrase alongside a "how this may land" note for the recipient. |
| CU-3 | Adaptive companion that builds trust | F11, F29, F45, F57 | On-device persona auto-selection by mood and context; no open competitor ships this. During onboarding, the user is offered an optional initial persona choice that they may skip entirely, after which personas adapt implicitly from interaction signals without requiring manual configuration. |
| CU-4 | Names and terms you use | F33, F58 | Entity recognition seeded from the personal knowledge graph; removes the manual-correction burden |
| CU-5 | Capture from anywhere | F59 | Phone, desktop, and a Chrome extension (Cytomark) unified into one knowledge-graph-linked capture layer. Memex (WorldBrain) is the open-source, local-first, account-free web annotation reference pattern: unlike Hypothes.is, which requires an account and routes annotations through a central server, Memex stores annotations locally and does not require cloud sign-in; meeting transcripts are a supported capture type under this surface. |
| CU-6 | Conversational thought map | F13, F14, F15, F31, F60 | Transcriber, placer, and reviser agents grow and reorganize a living thought-graph from speech; novel. Revision tracking keeps a versioned history of map states and a log of placer and reviser decisions, with undo available at any prior state. |
| CU-7 | Thought to document templates | F34, F61 | Deterministic graph-to-artifact transforms (proposal, notes, plan); not summarization |
| CU-8 | Opt-in self-assessment tools | F62 | Validated scales feed Brain Weather as self-report axes under CAP governance. Named example instruments: ASRS v1.1 (ADHD symptoms), PHQ-9 (depression severity), GAD-7 (anxiety severity), BRIEF-A (executive function), and BIS-11 (impulsivity). |

## 9. Prioritized Recommendations

> **If you only read one thing, read this section.**

1. **Build the P1 core first.** Capture (F01 to F04), Your energy and mood map (F05), Companion style and voice and Adaptive companion that builds trust (F11, F57), the Mood-anchored morning check-in and Voice mood awareness (F53, F54), and the brainmap core (F13 to F16, F58, F60). This set is high AI-Fit, high impact, and mostly greenfield.
2. **Port, do not reinvent, the table-stakes lanes.** Focus, idle, and break logic from Super Productivity (MIT); supertags and live search from the Tana pattern; text-to-speech from a Speechify-class cascade; voice capture from Omi. These are solved problems; spend build time elsewhere.
3. **Protect the emotional-regulation cluster as the moat.** Fifteen ERM features are greenfield and define the differentiation; do not let table-stakes work crowd them out.
4. **Adopt open patterns rather than competing on them.** Omi's MCP and pluggable STT, Goblin's Judge tone concept, Tana's schema-governed capture, and Saner's proactive AI-initiated model.
5. **Unblock the two critical safety gaps before shipping any care-adjacent or distributed feature.** The privacy-boundary schema and the crisis-detection subsystem (Section 11) gate therapy-adjacent use.
6. **Resolve naming and de-duplicate.** Adopt CSP as the canonical sensor-protocol name, retire "Substrate" in code, and collapse the duplicate master files.

**P1 build list (23 features):** F01, F02, F03, F04, F06, F07 (attention); F05, F08, F11, F17, F53, F54, F57 (emotion and companion); F09, F10, F13, F14, F15, F16, F58, F60 (thought organization); F12, F55 (sensing).

**Engagement-design mandate (from Blue Lin, Section 10.4):** plan for a week 4 to 6 engagement drop. Shift the experience from daily data entry to periodic confirmation and exception-flagging as the user internalizes patterns; do not read flat mid-period engagement as failure.

## 10. Strategic Insights and Caveats

### 10.1 Mindstrong failure lesson

Mindstrong failed on economics and positioning, not science (Perlis, STAT News, 2023-02-06). Insurance reimbursement was structurally inadequate, consumer willingness to pay did not match stated demand, the tech-replaces-care stance was a fatal error, and passive-sensing efficacy was never validated at scale before scaling. **Lesson for Yar:** the value proposition must not depend on reimbursement, passive biomarkers stay in the research track until validated, and the augmentation framing holds throughout.

### 10.2 Brain.fm evidence caveat

Brain.fm has more peer-reviewed support than most attention-audio competitors, but it rests on one study (Communications Biology, 2024), measured on people with ADHD **symptoms** rather than clinical diagnosis, with no public effect sizes. **Citation rule:** never cite Brain.fm as having robust ADHD evidence; the one-study caveat accompanies any reference to its science.

### 10.3 Chen et al. (2026) attribution rule

Cite Chen, Meng, and Nie (2026), "Not Just Me and My To-Do List," arXiv:2603.17258, accepted to CSCW 2026, for the **social-scaffold and co-regulation framing** and the thirteen design-concept ratings (C1 to C13). The paper does not enumerate thirty validated sub-features; that count is downstream Yar synthesis and must not be attributed directly to the paper.

### 10.4 Blue Lin engagement-curve finding

Blue Lin's IMWUT 2025 field study (20 participants, 100 days) shows engagement follows a learning curve: high early, a sharp decline in weeks 4 to 6 as users internalize patterns, then a late resurgence for new insights. This predicts a churn inflection that Yar must design around, per the mandate in Section 9.

## 10.5 Blue Lin design requirements and visualization patterns

Blue (Georgianna) Lin's CHI 2024 paper ("Functional Design Requirements to Facilitate Menstrual Health Data Exploration") and her IMWUT 2025 longitudinal field study provide the most directly actionable design evidence in the Yar research corpus. The domain is menstrual health, but the structural challenge is identical to cognitive/emotional state tracking: multimodal longitudinal biological signals, high individual variation, and the risk of overwhelm from data without sensemaking support. The full researcher profile and project deep-dive are in `04-Engineering/yar/research/blue-lin-projects-deep-dive.md`.

### Functional design requirements (DR1-DR5)

Five requirements were validated through interviews with 30 participants and two proof-of-concept design probes (Phase-Centric and Signal-Centric views).

| # | Requirement | Cognitive or emotional-state parallel for Yar |
|---|---|---|
| DR1 | Communicate predicted phases and expected symptom variance, not just timing | Communicate predicted cognitive states with confidence ranges: "Your focus typically dips in the afternoon, with moderate variability" |
| DR2 | Support different user interaction patterns (daily check-in, weekly review, episodic deep-dive) | Yar users vary: daily companions, weekly reflectors, and crisis-only users all need the same underlying data presented at different depths |
| DR3 | Personalize which signals are visible; users arrange their own dashboards | Signal selection varies by neurotype: an autistic person may track sensory load and social fatigue where an ADHD person tracks focus and impulsivity |
| DR4 | Integrate educational content contextually, not as a separate help section | Explain why patterns emerge: "Dopamine regulation affects focus differently before and after meals" accessible at the moment of observation |
| DR5 | Enable side-by-side period comparison with contextual annotations | Compare cognitive performance across weeks or months: "Your focus was higher this week; sleep consistency was also higher" |

### Visualization patterns (7 techniques)

| Pattern | Description | Yar application |
|---|---|---|
| Phase-coded timeline | Background color regions mark cognitive-state phases; signal values plotted on top | Color-code daily timelines by focus, transition, rest, and recovery using Cytognosis brand colors |
| Multi-cycle overlay | Multiple weeks aligned by day-of-week or sleep onset, not calendar date | Overlay four weeks of focus scores aligned by wake time; highlight the current week |
| Circular timeline | Cyclical radial view revealing periodicity; reduces "missed day" guilt of linear calendars | Radial circadian view (24-hour clock face) for ultradian and daily cognitive rhythms |
| Signal grouping and custom dashboards | User-defined groups of related signals toggled on and off | "Energy" group: sleep quality plus caffeine plus steps; "Social" group: interaction count plus sensory load |
| Contextual annotation overlay | Life events, medication changes, and stress markers visible across all signal views | Auto-detect context shifts from voice captures (travel, new project, illness) and overlay as event markers |
| Progressive disclosure dashboard | Status indicator, then summary, then signal group detail, then raw data with comparison | Yar default: composite state card; tap for signal group summary; tap again for raw session data |
| Empathetic data framing | Language is neutral and personal-baseline-first, never normative | "Your focus was lower today" not "You had a bad day"; compare to the user's own history, not a neurotypical baseline |

### Three patterns most relevant to Yar

**Unified multimodal view.** Neither Lin's Phase-Centric nor Signal-Centric probe was universally preferred; the effective design lets users switch between both mental models. Yar's Brain Weather dashboard should support a phase-first view (organized by cognitive state period) and a signal-first view (individual axes with phase background overlay), with a persistent toggle between them.

**Paired-hypothesis data entry.** Power users formed hypotheses and tested them against their data ("Is my focus always lower in the afternoon?"). Yar's agent can support this by constructing structured comparisons: focus scores on days with morning exercise versus days without, surfaced as a persistent saved query rather than a one-time report. This pattern grounds F05 (Your energy and mood map), F43 (Layered wellbeing dashboard), and the conversational sensemaking layer of F60 (Conversational thought map).

**Progressive-trust scaffolding (and the circular-vs-linear toggle).** Lin's field study found that users who successfully built self-knowledge compared across time periods rather than analyzing individual data points. The circular timeline reduced guilt about missed days by removing the visual representation of linear streaks. For Yar, this translates to: suppress real-time focus fluctuation (do not show a live score that changes every minute), emphasize trend views, and optionally offer a radial circadian view for users who find linear calendars anxiety-inducing.

## 10.6 Voice-model architecture verdict

The full evaluation is in `04-Engineering/yar/research/voice_model_deep_evaluation.md`. Five candidates were assessed across three capabilities: supervisor interrupt and context injection, nonverbal communication understanding (prosody, hesitation, vocal quality), and longitudinal storage of vocal biomarkers for neuropsychiatric tracking.

### Candidate comparison

| Model | Supervisor control | Nonverbal understanding | Notes |
|---|:---:|:---:|---|
| Moshi 7B | 9/10 | 6/10 | Native full-duplex supervisor channel via dual-stream; MoshiRAG adds retrieval; English-only, CC-BY license |
| Gemma 4 cascade (E4B edge + 26B MoE supervisor) | 7/10 | 4/10 | Structured function-call supervisor interface; 35+ languages; Apache 2.0; recommended for Yar |
| Qwen3.5-Omni | 6/10 | 7/10 | Best native audio reasoning for nonverbal cues; supervisor can only inject between segments |
| LFM2.5-Audio | 5/10 | 3/10 | Interleaved mode has some overlap; no clean supervisor channel |
| Whisper + LLM + Kokoro cascade | 4/10 | 2/10 | Strips nonverbal by design; three-component coordination makes interruption complex |
| HuBERT-large + openSMILE eGeMAPSv02 (parallel sensor) | N/A | 9/10 | Purpose-built quantified sensor; required alongside any base model for neuropsychiatric tracking |

### Verdict

**Recommend the Gemma 4 cascade for Yar across all three evaluation dimensions.** The edge model is Gemma 4 E4B (LiteRT-LM, 35+ languages, Apache 2.0); the supervisor is Gemma 4 26B MoE (Ollama, laptop or cloud). The supervisor sends structured `update_guidance()` and `inject_priority_message()` function calls rather than ad-hoc text injection, which is a genuine architectural advantage for the CAP governance model. TTS is Kokoro 82M with ElevenLabs on-device as the upgrade path.

The HuBERT-large plus openSMILE eGeMAPSv02 parallel sensor is non-negotiable: no base model produces the quantified, clinically comparable prosodic features (jitter, shimmer, F0 contour, response latency) required for longitudinal neuropsychiatric tracking. The two sensors run in parallel and produce independent observation streams.

**Monitor Moshi** for future consideration. Its native full-duplex supervisor channel (score 9/10) and MoshiRAG retrieval augmentation are architecturally superior for supervisor control; however, English-only support and the CC-BY license are disqualifiers for Yar's day-one multilingual and open-source commitments. Revisit when multilingual Moshi variants are released.

This verdict grounds features F01 (Voice brain dump), F40 (Voice wellbeing signals (research)), and F54 (Voice mood awareness).

## 11. Flagged Decisions and Architecture Gaps

| # | Decision or gap | Severity | Recommended action |
|---|---|---|---|
| D1 | Sensor-protocol naming | Low | **CSP (Cytonome Sensor Protocol; formerly USAP/UBAP)** is canonical; the deprecated aliases are not used in new work |
| D2 | Privacy-boundary schema (no artifact) | **Critical** | Create the schema before any distributed-runtime work; block that work on it |
| D3 | Crisis-detection subsystem (not built) | **Critical** | Required before any therapy-adjacent feature reaches users |
| D4 | Duplicate master files (byte-identical) | Low | Designate `yar-product-feature-master.md` canonical; replace the other with a link |
| G1 | "Substrate" term in `substrate_interop.py` | Low | Rename to a layer or protocol term per naming rules |
| G2 | Cytomark browser extension (no spec) | High | Highest-value unbuilt surface; write the spec (see F59) |
| G3 | Vocal-biomarker storage schema (VocalBiomarkerFrame) | High | Specify before the F40 research feature integrates; see `04-Engineering/yar/research/voice_model_deep_evaluation.md` for the full `VocalBiomarkerFrame`, `SessionVocalProfile`, `ADHDVocalMarkers`, and `ASDVocalMarkers` schema definitions |
| G4 | CAP protocol internals reference | Low | See `03-Products/Cytonome/Yar/research/cap-yar-comprehensive-reference.md` for the full CAP primitive lifecycle, 7 primitives, 16 RefusalMessage reason codes, Directive state machine, and routing architecture |

## 12. Methodology Notes

- **Scoring calibration.** Competitor scores carry forward from v3 (0 to 10, user-experience weighted). AI-Fit axes (0 to 5) were assigned per feature from the four research briefs, then summed into the 0-to-20 AI-Fit Score; prior-AI maturity is reported separately as crowdedness.
- **Data sources.** Prior Cytonome, Yar, and Cytoplex docs; the v3 matrix; web research on eighteen named tools; verified academic sources (Chen et al. 2026, Brain.fm 2024, Blue Lin 2024 and 2025).
- **Limitations.** Competitor feature depth is assessed from public materials and may lag private roadmaps. AI-Fit scores are judgment-based and should be revisited as the build progresses. Brain.fm and Mindstrong evidence is explicitly caveated above.
- **Last verified.** 2026-06-21.

---

<details>
<summary><strong>Glossary</strong></summary>

- **Brain Weather:** Yar's ambient cognitive-state dashboard (focus, energy, mood, sleep, stress).
- **Body-doubling:** working alongside a real or simulated presence to sustain attention (feature F06).
- **CAP (Controller-Authority Protocol):** the safety and authority spec governing Yar's AI actions; **CAP-Lite** is the mobile or MVP gate.
- **CSP (Cytonome Sensor Protocol):** the open, CAP-governed protocol for plugging any sensor into Yar.
- **Cytonome:** the navigator platform pillar; Yar is its first consumer application.
- **Cytoplex:** the runtime package that implements CAP.
- **Double-empathy problem:** the framing that neurodivergent-to-neurotypical miscommunication is mutual, not a one-sided deficit.
- **Exposome:** the cumulative environmental and social exposures that influence health and mood.
- **MCP (Model Context Protocol):** an open protocol for connecting tools and data to AI systems.
- **NER (named-entity recognition):** identifying proper nouns and domain terms, here seeded from the personal knowledge graph.
- **Supertags:** typed, schema-bearing tags that turn a note into a structured object (Tana pattern).
- **WADM (Web Annotation Data Model):** the W3C standard for highlights and annotations (feature F50).
- **Yar:** Cytognosis's neurodivergent cognitive-companion app, the first instance of Cytonome.

</details>

