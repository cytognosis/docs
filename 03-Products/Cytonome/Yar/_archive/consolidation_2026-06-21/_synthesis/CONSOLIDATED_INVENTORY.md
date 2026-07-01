> **Status**: Synthesis artifact (read-only for Opus parent; do not edit directly)
> **Date**: 2026-06-21
> **Author**: Sonnet synthesis agent
> **Sources**: A_canonical_product.md, B_feature_research.md, C_new_tools_and_papers.md, D_deepen_tools.md
> **Audience**: Opus parent agent (writing final master docs v4)
> **Tags**: `yar`, `consolidation`, `feature-matrix`, `synthesis`, `v4`

# Yar Feature Consolidation v4 — Consolidated Inventory

> [!NOTE]
> **TL;DR**: 62 features unified across 4 ingestion briefs. 28 are Cytognosis-unique (no competitor equivalent). 18 named competitor tools are represented. This file preserves all rubrics, template structures, strategic insights, and flagged decisions the Opus parent needs to write master docs without re-reading source files.

---

## 1. Feature Count and Scope

| Metric | Count |
|--------|-------|
| Total canonical features (post-merge) | 62 |
| Cytognosis-unique rows | 28 |
| Features with competitors | 34 |
| Named competitor tools represented | 18 |
| ND domain tags applied | 6 |
| Features marked as built or in-progress | 8 |
| Features marked as research or future | 5 |

The 62 features span:
- 54 features from A (canonical product digest)
- 8 Cytognosis-unique features added per task spec (CU-1 through CU-8), merged into the table without creating duplicates (several overlap with existing features and are tagged accordingly)

---

## 2. ND Functional Domain Taxonomy (Canonical)

Use these codes exactly in all master docs. The brief C used shorter aliases (ATT/EMO/SOC etc.); the canonical codes below supersede them.

| Code | Full Name | What it covers |
|------|-----------|----------------|
| AEF | Attention regulation and executive function | Task initiation, sustained attention, working memory, planning, time management |
| ERM | Emotional regulation and mood | Mood tracking, burnout detection, shame reduction, emotional aftercare |
| SCI | Social communication and interaction | ND-to-NT translation, tone calibration, co-regulation, social exposome |
| SPR | Sensory processing and regulation | Auditory environment, transition cues, sensory-gentle signals |
| CTO | Cognitive style and thought organization | Nonlinear ideation, knowledge graph, mind mapping, schema capture |
| SMI | Self-monitoring and interoception | Longitudinal self-report, sensor integration, physiological signal tracking |

---

## 3. Cytognosis-Unique Features (CU-1 through CU-8)

These eight capabilities have no competitor equivalent and must appear as first-class rows in the feature matrix. They are tagged Cytognosis_Unique = Yes in the CSV.

| CU# | Feature | Where it maps in CSV |
|-----|---------|----------------------|
| CU-1 | Universal sensor/tracking system (user-extensible health and mental-health axes) | F12 (CSP/USAP), F55 (Universal sensor system), F46 (Cytoscope adapter) |
| CU-2 | Social interaction tracker plus communication coach (exposome-to-mood causal linkage) | F42 (ND-NT Communication Translation), F56 (Social interaction tracker) |
| CU-3 | Adaptive personas (implicitly adapted, mood/mindset-matched, trust-building) | F11, F29, F45, F57 |
| CU-4 | Personal-knowledge plus named-entity recognition for accurate transcription | F33 (Personal grammar/lexicon), F58 (Personal-KG NER) |
| CU-5 | Capture-anywhere (phone, desktop, Chrome extension, on-page annotation) | F59 |
| CU-6 | Conversational mind-mapping with 3-agent loop (transcriber, placer, reviser) | F13, F14, F15, F31, F60 |
| CU-7 | Templated transformation engine (doc/artifact/transcript/mind-map to structured artifacts) | F34, F61 |
| CU-8 | Self-report instruments (personality and validated tests as opt-in psych sensors) | F62 |

---

## 4. Competitor Tools Represented (18 Named)

Scored tools in the v3 master matrix (12 tools, 0-10 per category):

| Tool | Total v3 Score | Cluster | Key Feature Domain |
|------|:--------------:|---------|-------------------|
| Super Productivity | 86/120 | A: Task-Focused Execution | Focus mode, idle detection, break reminders, data portability |
| Leantime | 81/120 | A: Task-Focused Execution | Emoji mood on tasks, LEO AI proactive agent |
| Saner AI | 63/120 | C: AI-Augmented Assistants | Proactive morning plan, ADHD-explicit design, Skai AI |
| Omi AI | 70/120 | F: Voice-First Capture | Ambient capture, open MCP, pluggable STT, 300k+ users |
| Anytype | 61/120 | B/E: Knowledge/Infrastructure | Local-first E2E storage, object model |
| Tana | 61/120 | B: Knowledge-Focused | Supertags, live search, voice-to-graph, 8/10 ND relevance |
| Capacities | 58/120 | B: Knowledge-Focused | Object-first PKM, daily note inbox, 6/10 ND relevance |
| ND Visual Organizer (MCP Pattern) | 58/120 | E: Composable Infrastructure | MCP patterns, open-source |
| Goblin Tools | 57/120 | C: AI-Augmented Assistants | Spiciness slider, Judge tool, 8/10 ND UX purity |
| Speechify | 46/120 | D: Accessibility-First | TTS with highlighting, 9/10 mobile |
| Letterly | 41/120 | F: Voice-First Capture | Voice brain-dump |
| Blue Lin (design study) | N/A | Design inspiration | CHI 2024 + IMWUT 2025 multimodal health UX research |

Additional tools assessed (not in matrix, from substrate decision doc):
Obsidian (6/10 ND), AFFiNE (6/10 ND), Notion (5/10 ND), Logseq (5/10 ND), Lovable.dev (4/10 ND), Brain.fm (6/10 ND), Mindstrong (defunct).

---

## 5. Scoring Rubrics (Verbatim, Carry Forward)

### 5.1 Competitor Feature Score (0-10)

From v3 `04-Engineering/yar/research/yar-unified-feature-comparison-v3.md`, Section 1:

> Scores use a 0-10 scale: **0** = absent, **3** = basic/limited, **5** = adequate, **7** = strong, **10** = best-in-class.

Methodology anchors:
- Scores reflect feature depth, polish, and relevance to neurodivergent users
- A score of 10 indicates best-in-class within this comparison set
- Scores weight actual user experience over marketing claims
- Open-source scores reflect both code availability and license permissiveness
- v3 adds ADHD paper-validated concepts as evaluation criteria for "ND-Specific Features"

| Score | Meaning |
|:-----:|---------|
| 0 | Feature absent |
| 3 | Basic or limited implementation |
| 5 | Adequate |
| 7 | Strong |
| 10 | Best-in-class within this comparison set |

### 5.2 AI-Fit Assessment Rubric (DRAFT, 0-5 each)

These five columns appear in the CSV. All values are DRAFT and should be finalized by the Opus parent.

| Column | 0 means | 5 means |
|--------|---------|---------|
| AI_Leverage | No meaningful AI contribution; rule-based only | AI is the entire mechanism; not possible without ML |
| PriorAI_Maturity | No one has shipped AI here; greenfield | Mature AI products exist with strong user adoption |
| Differentiation | Competitors match Cytognosis on this dimension | Cytognosis has a structural, defensible advantage |
| ND_Impact | Minimal impact on the ND user experience | Critical to the core ND value proposition |
| Feasibility | Requires years of R&D or hardware not yet built | Shippable in the current build cycle with known tools |

### 5.3 ADHD Paper Priority Labels (Chen et al. 2026)

| Label | Condition |
|-------|-----------|
| Critical | Median rating 5; high top-3 count |
| High | Median rating 4.5; high top-3 count |
| Medium | Median rating 3; some top-3 placement |
| Low | Median rating 2-3; minimal top-3 |

---

## 6. Features by Domain Group

### 6.1 AEF: Attention Regulation and Executive Function

| ID | Feature | Yar Status | Best Competitor | Score |
|----|---------|------------|----------------|:-----:|
| F01 | Zero-friction voice capture | In progress | Omi AI | 9 |
| F02 | Brain-dump compiler | Planned | Goblin Tools | 8 |
| F03 | Auto task-extraction from captures | Planned | Saner AI | 7 |
| F04 | Spiciness slider (task decomposition) | Planned | Goblin Tools | 10 |
| F06 | Social Presence AI (focus companion / body-doubling) | Planned | None | 0 |
| F07 | Dual-track planning (ideal vs. baseline) | Planned | None | 0 |
| F13 | Branching brainmap companion (flagship) | Planned | None | 0 |
| F14 | Turn-time attachment reasoning (placer agent) | Planned | None | 0 |
| F15 | Force-directed brainmap visualization | Planned | None | 0 |
| F20 | Focus mode (full-screen single task) | Planned | Super Productivity | 10 |
| F21 | Idle detection (graceful pause) | Planned | Super Productivity | 10 |
| F22 | Break reminders (hyperfocus guard) | Planned | Super Productivity | 10 |
| F24 | Plan my day (AI daily plan) | Planned | Saner AI | 7 |
| F26 | PiP focus window | Planned | Saner AI | 6 |
| F32 | Side-thread TODO / reminder capture | Planned | None | 0 |
| F34 | Brainstorm-to-artifact operations | Planned | None | 0 |
| F41 | Unified ND companion | In progress | None | 0 |
| F53 | Mood-Aware Daily Companion (morning check-in) | Planned | Saner AI | 7 |
| F55 | Universal sensor / tracking system | Planned | None | 0 |
| F58 | Personal-knowledge NER for accurate transcription | Planned | Tana | 8 |
| F59 | Capture-anywhere | Planned | Saner AI (ext.) | 6 |
| F60 | Conversational mind-mapping (3-agent loop) | Planned | None | 0 |
| F61 | Templated transformation engine | Planned | None | 0 |

### 6.2 ERM: Emotional Regulation and Mood

| ID | Feature | Yar Status | Best Competitor | Score |
|----|---------|------------|----------------|:-----:|
| F05 | Brain Weather Dashboard | Planned | None | 0 |
| F07 | Dual-track planning (ideal vs. baseline) | Planned | None | 0 |
| F08 | Emoji mood on tasks | Planned | Leantime | 7 |
| F11 | Adaptive personas (relationship type plus voice) | Planned | None | 0 |
| F17 | Private Emotional Notes Before Planning | Planned | None | 0 |
| F18 | CAP safety gate (CAP-Lite) | Built | None | 0 |
| F19 | Local-first AI brain (on-device Gemma) | Built | Anytype (storage) | 9 |
| F27 | Emotionally Aware Pause Days | Planned | None | 0 |
| F29 | Persona adaptive refinement (auto-tune) | Planned | None | 0 |
| F35 | Emotional Inventory Before New Commitments | Planned | None | 0 |
| F36 | Shared Planning with a Trusted Person | Planned | None | 0 |
| F38 | Adaptive Planning Undo Button | Planned | None | 0 |
| F44 | Gentle streaks (no shame on skip days) | Planned | None | 0 |
| F45 | Persona mood/context auto-selection | Planned | None | 0 |
| F48 | Emotional Debrief After Task Collapse | Planned | None | 0 |
| F49 | Weekly Narrative Reflection | Planned | None | 0 |
| F53 | Mood-Aware Daily Companion | Planned | Saner AI | 7 |
| F54 | Affect detection (voice affect route) | In progress | None | 0 |
| F56 | Social interaction tracker (exposome-to-mood) | Planned | None | 0 |
| F57 | Adaptive personas (implicit mood/mindset matching) | Planned | None | 0 |
| F62 | Self-report instruments (opt-in psych sensors) | Planned | None | 0 |

### 6.3 SCI: Social Communication and Interaction

| ID | Feature | Yar Status | Best Competitor | Score |
|----|---------|------------|----------------|:-----:|
| F25 | Tone analysis (Goblin Judge) | Planned | Goblin Tools | 8 |
| F36 | Shared Planning with a Trusted Person | Planned | None | 0 |
| F42 | ND-NT Communication Translation | Planned | None | 0 |
| F56 | Social interaction tracker and communication coach | Planned | None | 0 |
| F59 | Capture-anywhere | Planned | Saner AI (ext.) | 6 |

### 6.4 SPR: Sensory Processing and Regulation

| ID | Feature | Yar Status | Best Competitor | Score |
|----|---------|------------|----------------|:-----:|
| F23 | TTS with text highlighting | Planned | Speechify | 9 |
| F37 | Ambient Transition Cues | Planned | None | 0 |

### 6.5 CTO: Cognitive Style and Thought Organization

| ID | Feature | Yar Status | Best Competitor | Score |
|----|---------|------------|----------------|:-----:|
| F09 | Smart note types / supertags | Partial | Tana | 10 |
| F10 | Live search queries | Planned | Tana | 10 |
| F13 | Branching brainmap companion | Planned | None | 0 |
| F14 | Turn-time attachment reasoning | Planned | None | 0 |
| F15 | Force-directed brainmap visualization | Planned | None | 0 |
| F16 | Personal-KG integration | Planned | None | 0 |
| F31 | Parallel correction plus restructuring agent | Planned | None | 0 |
| F33 | Personal grammar plus lexicon learning | Planned | None | 0 |
| F34 | Brainstorm-to-artifact operations | Planned | None | 0 |
| F43 | Progressive-disclosure cognitive dashboard | Planned | None | 0 |
| F47 | Thought deconvolution | Research | None | 0 |
| F50 | WADM annotation model (W3C) | Built | None | 0 |
| F51 | LinkML-to-Anytype schema mapping | Built | None | 0 |
| F52 | Anytype local-first storage | In progress | Anytype | 9 |
| F58 | Personal-knowledge NER for accurate transcription | Planned | Tana | 8 |
| F60 | Conversational mind-mapping (3-agent loop) | Planned | None | 0 |
| F61 | Templated transformation engine | Planned | None | 0 |

### 6.6 SMI: Self-Monitoring and Interoception

| ID | Feature | Yar Status | Best Competitor | Score |
|----|---------|------------|----------------|:-----:|
| F05 | Brain Weather Dashboard | Planned | None | 0 |
| F12 | CSP / USAP (universal sensor adapter) | Planned | None | 0 |
| F18 | CAP safety gate | Built | None | 0 |
| F19 | Local-first AI brain | Built | Anytype | 9 |
| F30 | CSP wearable adapter (Oura / Apple Watch) | Planned | Omi AI | 7 |
| F39 | Pattern-Based Gentle Nudges | Planned | None | 0 |
| F40 | Voice-first emotional awareness (vocal biomarkers) | Research | None | 0 |
| F43 | Progressive-disclosure cognitive dashboard | Planned | None | 0 |
| F45 | Persona mood/context auto-selection | Planned | None | 0 |
| F46 | CSP connectomic adapter (Cytoscope / fNIRS) | Future | None | 0 |
| F53 | Mood-Aware Daily Companion | Planned | Saner AI | 7 |
| F54 | Affect detection (voice affect route) | In progress | None | 0 |
| F55 | Universal sensor / tracking system | Planned | None | 0 |
| F57 | Adaptive personas (implicit mood/mindset matching) | Planned | None | 0 |
| F62 | Self-report instruments (opt-in psych sensors) | Planned | None | 0 |

---

## 7. ADHD-Friendly Document Template Structure

From `/home/mohammadi/repos/cytognosis/cytoskills/skills/cytognosis/cytognosis-doc/references/adhd-friendly-template.md`.

**Section sequence (canonical, 8 sections):**

1. Document header with status/date/author/audience/tags blockquote
2. `[!NOTE]` TL;DR block (1-3 sentences; link to canonical source)
3. Overview (2-3 short paragraphs; max 3 sentences each; `[!TIP]` key takeaway)
4. Quick Start (numbered steps; bold commands; max 2 lines per step; `[!TIP]` key takeaway)
5. Core Concept or Feature section (bullets for use cases; `[!NOTE]` 101 sidebar for jargon; `<details>` deep dive for advanced content)
6. Second Concept or Feature section (3-point numbered list; `[!TIP]` key takeaway; `[!NOTE]` jargon sidebar; `<details>` deep dive with option table)
7. Common Pitfalls (bullet list; bold mistake then fix; `[!WARNING]` for most dangerous pitfall)
8. What's Next (2-3 bullets with links; separator `---`)
9. Glossary in `<details>` block (alphabetical; one sentence per term)

**Callout types:**
- `[!NOTE]` for TL;DR, explanatory notes, and 101 jargon definitions
- `[!TIP]` for key takeaways at the end of sections
- `[!WARNING]` for the single most dangerous pitfall
- `[!IMPORTANT]` (from v3 ADHD file): for critical findings and market gaps

**Formatting rules:**
- Max 4 sentences per paragraph (template says 3; v3 practice says 4; use 4)
- Max 3 nesting levels
- Bold key terms on first use
- No em dashes
- Oxford comma
- Active voice
- Emoji in section headers and table rows for visual anchoring (not decoration)
- `<details>` blocks for dense reference content
- Mermaid diagrams for flows and concept maps

**v3 ADHD format 13-section full sequence** (from B digest, for the full comparison document):
1. TL;DR note block
2. What Changed from v2 to v3
3. Master Feature Matrix (12 Tools) with `[!IMPORTANT]` scoring gap callout
4. Category Winners table
5. Comparative Landscape (6 Clusters) with Mermaid diagram and `<details>` cluster descriptions
6. ADHD Paper-Validated Features (by executive function) with `[!IMPORTANT]` emotional regulation gap callout
7. Blue Lin Design Principles (5 principles, 5 DRs, color mapping in `<details>`, visualization catalog in `<details>`)
8. Yar Feature Adoption Roadmap (3 priority tiers as tables)
9. The Big Gap (Why Yar Exists) with code block and missing feature table
10. Codebase Quality Assessment (architecture table, pattern search table, Mermaid flow diagram)
11. Design Tensions and Trade-offs (table and `[!WARNING]` callout)
12. What's Next (related documents table)
13. Glossary (`<details>` block, full alphabet)

**Mermaid color rules:**
- YAR node: `fill:#8B3FC7,color:#fff,stroke:#5145A8,stroke-width:3px`
- Competitor nodes: Cytognosis brand palette
- Diagrams: `graph LR` (landscape/concept) or `graph TB` (cluster/comparative)

---

## 8. Market-Research Template Structure

From `/home/mohammadi/repos/cytognosis/cytoskills/skills/cytognosis/cytognosis-doc/references/market-research-template.md`.

**Section sequence (canonical, 8 sections):**

1. Document header with status/date/author/audience/tags blockquote
2. Research Objective (domain, key question, constraints)
3. Candidate Identification (search strategy, inclusion criteria, exclusion criteria, candidate counts)
4. Master Feature Matrix (0-10 score per feature per tool; average column)
5. Comparative Landscape Analysis (3-paragraph executive summary: landscape state, key differentiators/gaps, implications and positioning)
6. Bullet-Point Summary (5 bullets: strongest contender, emerging trend, underserved need, licensing risk, integration opportunity)
7. Candidate Groups (3-5 groups by capability tier: Leaders, Contenders, Niche/Emerging; per-tool strengths/weaknesses/differentiator; `[!NOTE]` on group placement methodology)
8. Recommendations (numbered; concrete and actionable; state conclusions not options)
9. Methodology Notes (scoring calibration, data sources, limitations, last verified date)

---

## 9. Strategic Insights (Carry Forward Verbatim)

### 9.1 Mindstrong Failure Lesson

Source: Roy Perlis, STAT News (2023-02-06) and STAT April 2023 analysis.

Four causal factors in the Mindstrong failure (not caused by bad science):
1. Insurance reimbursement was structurally inadequate for MH digital tools
2. Consumer willingness to pay did not match stated demand
3. Tech-replaces-care positioning was a fatal error; augmentation framing is safer and more honest
4. The passive sensing science was not validated before scaling; pilot efficacy did not transfer to RCT

**Lesson for Yar:** Consumer MH apps need a value proposition that does not depend on insurance reimbursement. Passive behavioral biomarkers are scientifically promising but not clinically validated at consumer scale. The augmentation (not replacement) framing must be maintained throughout all Yar positioning.

### 9.2 Brain.fm Evidence Caveat

Source: Woods et al. (2024), Communications Biology; Woods et al. (2019), arXiv preprint.

Brain.fm has more peer-reviewed support than most competitors in the attention-music category, but the evidence is limited:
- One peer-reviewed efficacy study exists (Communications Biology 2024, Nature portfolio)
- The ADHD finding is for participants with ADHD *symptoms* (likely screening-based), not clinically diagnosed ADHD in an RCT
- No effect sizes are publicly available in accessible summaries
- The 2019 study is an unreviewed preprint
- The "world's first science-backed, purpose-built focus music for ADHD" marketing overstates what one neuroimaging study with self-reported symptoms demonstrates

**Citation rule:** Do not cite Brain.fm as having robust ADHD evidence. The one-study caveat must accompany any reference to its science.

### 9.3 Chen et al. (2026) Attribution Rule

**Correct citation:** Chen, J., Meng, Y., & Nie, K. (2026). "Not Just Me and My To-Do List": Understanding Challenges of Task Management for Adults with ADHD and the Need for AI-Augmented Social Scaffolds. arXiv:2603.17258 [cs.HC]. Accepted to CSCW 2026.

**What this paper provides:**
- 22 semi-structured interviews (challenge discovery) plus speed-dating study with 20 ADHD-identifying adults evaluating 13 speculative AI design concepts
- Qualitative grounding for social-scaffold and co-regulation feature clusters
- ADHD task management is relationally and affectively co-constructed, not an isolated individual act
- The paper does NOT produce a list of 30 discrete validated sub-features; that count is a downstream Yar synthesis

**Attribution rule:** Cite Chen et al. (2026) for the social-scaffold and co-regulation framing, and for the 13 design concept ratings (C1-C13). Do not attribute a specific sub-feature count directly to this paper without also citing the internal synthesis process.

### 9.4 Blue Lin Week 4-6 Engagement-Drop Churn Risk

Source: Blue Lin IMWUT 2025 (Phase 3 field study, 20 participants, 100 days).

Finding: Engagement follows a learning-curve pattern. There is a sharp mid-study decline (weeks 4-6) as users internalize patterns, followed by a late resurgence for new insights. Users who reach the late phase develop lasting internalized models even after stopping active tracking.

**Churn risk for Yar:** The week 4-6 engagement drop is a predictable churn risk. Design must account for the "patterns internalized" phase by shifting from daily data entry to periodic confirmation and exception flagging. A "simplify view" suggestion triggered at this inflection is one mitigation. Do not treat flat engagement in weeks 4-6 as failure.

### 9.5 Adopt-List (Open-Source / Pattern References)

From A digest and D synthesis. These are tools Yar should adopt patterns from, not compete with:

| Tool | What to adopt | License | Status |
|------|--------------|---------|--------|
| Omi AI | Open MCP server pattern; pluggable STT; open hardware reference | MIT | Adopt open-source patterns; MCP is production-ready |
| Goblin Tools Judge | Tone analysis pattern for social calibration; adapt for mood-report calibration | Proprietary | Adapt UX concept, not code |
| Tana supertag schema-capture | Schema-governed capture model; typed node resolution from voice | Proprietary | Adopt concept; implement via LinkML |
| Saner AI proactive model | AI-initiated check-ins; morning plan plus distributed micro-check-ins | Proprietary | Adopt UX pattern; Yar adds mood/energy layer |

---

## 10. Flagged Decisions (Pending, for Opus Parent)

These four items require an explicit decision before master docs can be finalized. Flag each in the output documents.

| # | Decision | Options | Recommendation |
|---|---------|---------|----------------|
| D1 | CSP vs. USAP canonical name | CSP (primary in product master); USAP (engineering alias) | Pick one name for all docs; recommend CSP as the canonical term and document USAP as the engineering alias |
| D2 | Privacy-boundary schema (missing artifact) | Schema columns are defined in cytonome-master-reference.md §4.2 but no schema artifact exists | Mark as CRITICAL gap; create schema artifact before any distributed runtime work; block distributed runtime on this |
| D3 | Crisis detection subsystem (missing artifact) | Architecture is designed but not built; required before any therapy-adjacent use case is deployed | Mark as CRITICAL gap; must be present before any care-adjacent feature goes to users |
| D4 | Duplicate master files | yar-product-feature-master.md and yar-master-features-requirements.md are byte-for-byte identical at two paths | Remove one path or replace with a symlink; designate yar-product-feature-master.md as canonical |

---

## 11. Architecture Gaps (From A Digest, Severity-Ordered)

| Gap | Severity | Notes |
|-----|---------|-------|
| Privacy boundary schema (formal artifact) | CRITICAL | Schema columns defined in cytonome-master-reference.md §4.2 but no artifact exists; must precede any distributed runtime |
| Crisis detection subsystem | CRITICAL | Architecture designed; not built; required before any therapy-adjacent deployment |
| Paralinguistic sensor pipeline (full integration) | HIGH | Architecture documented; not integrated; VocalBiomarkerFrame storage schema needed |
| Vocal biomarker storage (VocalBiomarkerFrame schema) | HIGH | Type named but not specified |
| Communication Coach bidirectional spec | HIGH | Defined as P3/planned; no spec beyond description |
| Cytomark browser extension (detailed spec) | HIGH | Likely most-used ND interface; not started; no spec |
| CSP / USAP spec v0 (written document) | HIGH | Protocol described; spec doc not yet published |
| Emotional aftercare module spec | MEDIUM | Named; no spec |
| Persistent relational context (per-person models) | MEDIUM | Named; no spec |
| Graph RAG design | MEDIUM | Named; no design |
| Distributed runtime (Dapr + NATS) | MEDIUM | Evaluated; not integrated |
| Cactus vs. LiteRT-LM evaluation | MEDIUM | Research complete; evaluation not run |
| Parakeet vs. Whisper ASR evaluation | MEDIUM | Research complete; evaluation not run |
| Full-duplex S2S voice (Moshi / LFM) | LOW | Evaluated; not scheduled |
| mDNS peer discovery | LOW | Named; not implemented |
| CSP/USAP canonical name resolution | LOW | See D1 above |
| Substrate rename in codebase | LOW | substrate_interop.py still uses forbidden term |

---

## 12. Vocabulary and Naming Rules

**Canonical terms:**

| Term | Meaning | Use |
|------|---------|-----|
| Cytonome | Navigator platform pillar | Platform layer; not a shipping product name |
| Yar | Consumer cognitive companion app | Ship this |
| Cytoplex | CAP runtime package name | Engineering; library name |
| CAP | Controller-Authority Protocol (spec) | Protocol name; use in spec and external docs |
| CSP | Cytonome Sensor Protocol (primary) | Preferred sensor protocol term; USAP is engineering alias |
| CAP-Lite | Lightweight CAP for mobile / MVP | MVP safety gate |
| Brain Weather | Cognitive-state visualization dashboard | Use verbatim |
| Gentle streaks | No-shame streak tracking | Use verbatim |
| Pause days | Burnout-aware pause mechanism | Use verbatim |
| Cytomark | Browser extension product name | Yar surface; not started |
| PEP | Policy Enforcement Point | Cytoplex runtime component |
| PDP | Policy Decision Point | Cytoplex runtime component |

**Retired / forbidden terms:**

| Term | Replacement |
|------|-------------|
| Substrate (as product/layer name) | "layer", "foundation", or "protocol" |
| CAP (as product name) | "Cytoplex" for the package; "CAP" for the spec |
| Cytonome Assurance Protocol | "Controller-Authority Protocol" |
| Communication Coach (as endpoint label in 04-Engineering) | Reconcile to "Communication Translator" or pick one |

---

## 13. New Tools Added in This Synthesis (v4 Additions Beyond v3)

These tools appear in briefs C and D but were not in the v3 matrix. They inform feature design but are not added as full matrix rows because they are not direct competitors.

| Tool | Category | Score | ND domains | Key Yar relevance |
|------|---------|:-----:|------------|------------------|
| Lovable.dev | AI app builder | 4/10 | COG/AEF | Mind-map-from-prompt pattern; low-friction start; not a shipped ND product |
| Brain.fm | Functional audio | 6/10 | AEF/SPR | Auditory regulation reference; one peer-reviewed study; SPR domain input |
| Mindstrong (defunct) | Digital phenotyping + care | N/A | MON/EMO | Passive sensing risk lesson; tech-replaces-care failure |
| Obsidian | Local-first PKM | 6/10 | COG/AEF | Graph view; plugin AI; high setup friction is ND barrier |
| Logseq | Open-source PKM | 5/10 | COG/AEF | Block-level granularity; slower development pace |
| AFFiNE | Open-source canvas + notes | 6/10 | COG/AEF | Infinite canvas; ADHD planner templates; multi-modal |
| Notion | Cloud workspace | 5/10 | COG/AEF | Native AI add-on; high configurability creates setup paralysis |

Tana score revised to 8/10 (from 61/120 in category total) based on D deep-dive findings.
Omi AI score revised to 7/10 (more mature MCP + pluggable STT than previously assessed).
Goblin Tools score confirmed at 8/10 for ND UX purity; Judge tool unique in landscape for SC domain.
Saner AI confirmed as closest existing product to Yar core UX; lacks SI and ER domains entirely.

---

## 14. Blue Lin Design Requirements (Carry Forward)

From D deep-dive (Blue Lin, CHI 2024 + IMWUT 2025). Five functional design requirements for Yar's multimodal dashboard.

| DR# | Requirement | Yar Application |
|-----|------------|----------------|
| DR1 | Predict cognitive phases plus variance | Predicted cognitive states with confidence ranges |
| DR2 | Unified multivariate view | One timeline: mood, energy, sleep, cognitive state; not separate logs |
| DR3 | Personalize viewable signals | User chooses which cognitive axes to track |
| DR4 | Cross-signal comparison | Show relationships between symptoms and physiological data on aligned timescales |
| DR5 | Cross-cycle comparison with context | Compare weeks/months with contextual annotations |

**Cognitive signal color mapping (Cytognosis brand):**

| Signal | Color | Brand Source |
|--------|-------|-------------|
| Focus/cognition | Azure #3B7DD6 | Alexa Fluor wavelength |
| Energy/vitality | Magenta #E0309E | Rhodamine wavelength |
| Mood/emotional | Violet #8B3FC7 | DAPI wavelength |
| Sleep/recovery | Teal #14A3A3 | GFP wavelength |
| Stress/load | Coral #F26355 | MitoTracker wavelength |

---

## 15. Source Files Read

| Brief | File Path | Status |
|-------|----------|--------|
| A | docs/03-Products/Cytonome/Yar/consolidation_2026-06-21/_ingestion/A_canonical_product.md | Read OK |
| B | docs/03-Products/Cytonome/Yar/consolidation_2026-06-21/_ingestion/B_feature_research.md | Read OK |
| C | docs/03-Products/Cytonome/Yar/consolidation_2026-06-21/_research/C_new_tools_and_papers.md | Read OK |
| D | docs/03-Products/Cytonome/Yar/consolidation_2026-06-21/_research/D_deepen_tools.md | Read OK |
| adhd-friendly-template | cytoskills/skills/cytognosis/cytognosis-doc/references/adhd-friendly-template.md | Read OK |
| market-research-template | cytoskills/skills/cytognosis/cytognosis-doc/references/market-research-template.md | Read OK |
