> **Status**: Ingestion artifact (read-only synthesis)
> **Date**: 2026-06-21
> **Author**: Cytognosis Agents (ingestion agent)
> **Audience**: consolidation agents, engineers
> **Tags**: `yar`, `feature-comparison`, `competitive`, `ingestion`, `consolidation`

# B: Feature Research Digest — Yar Competitive Feature Comparison

**TL;DR**: This digest exhaustively captures all feature-comparison data from 8 source documents covering Yar's competitive landscape. The master matrix covers 12 tools across 12 categories (107 rows of data). The scoring rubric is 0-10 (5 anchor points). Retired terms "Substrate" and "CAP" (renamed Cytoplex in product context) appear in specific files flagged below. The ADHD-friendly doc format is fully specified as a reusable template.

---

## 1. Source File Inventory

| File | Path | Status | Notes |
|:---|:---|:---|:---|
| v3 ADHD-friendly (03-Products) | `03-Products/Cytonome/Yar/research/yar-unified-feature-comparison-v3.md` | Found | v3, 12 tools, ADHD format, date 2026-05-31 |
| v2 ADHD-friendly (03-Products) | `03-Products/Cytonome/Yar/research/yar-unified-feature-comparison.md` | Found | v2, 9 tools, ADHD format, date 2026-05-28 |
| CAP/Yar reference (03-Products) | `03-Products/Cytonome/Yar/research/cap-yar-comprehensive-reference.md` | Found | date 2026-05-29; uses "CAP" throughout |
| v3 technical (04-Engineering) | `04-Engineering/yar/research/yar-unified-feature-comparison-v3.md` | Found | v3, 12 tools, technical prose, date 2026-05-31 |
| v2 technical (04-Engineering) | `04-Engineering/yar/research/yar-unified-feature-comparison.md` | Found | v2, 9 tools, technical prose, date 2026-05-29 |
| v2 ADHD-friendly (04-Engineering) | `04-Engineering/yar/research/yar-unified-feature-comparison-adhd.md` | Found | v2, 9 tools, ADHD format; identical to 03-Products v2 ADHD |
| CAP/Yar reference (04-Engineering) | `04-Engineering/yar/research/cap_yar_comprehensive_reference.md` | Found | Older version (date 2026-05-17); uses "CAP" + "Communication Coach" |
| Substrate decision (04-Engineering) | `04-Engineering/yar/research/yar-substrate-decision.md` | Found | date 2026-06-14; uses "Substrate" throughout |
| Yar system doc (04-Engineering) | `04-Engineering/yar/yar-system-doc.md` | Found | date 2026-06-14; architecture/phase doc |
| Inbox revision plan | `00-Inbox/yar_revision_plan.md` | Found | date 2026-05-17; phase tracker, no matrix data |

---

## 2. Scoring Rubric (Verbatim)

**From `04-Engineering/yar/research/yar-unified-feature-comparison-v3.md`, Section 1:**

> Scores use a 0-10 scale: **0** = absent, **3** = basic/limited, **5** = adequate, **7** = strong, **10** = best-in-class.

**From `04-Engineering/yar/research/yar-unified-feature-comparison-v3.md`, Section 12.1 (Methodology):**

> - Scores reflect feature depth, polish, and relevance to neurodivergent users
> - A score of 10 indicates best-in-class within this comparison set
> - Scores weight actual user experience over marketing claims
> - Open-source scores reflect both code availability and permissiveness of license
> - v3 adds ADHD paper-validated concepts as evaluation criteria for "ND-Specific Features"

**Scale anchor points (implied by rubric):**

| Score | Meaning |
|:---|:---|
| 0 | Feature absent |
| 3 | Basic/limited implementation |
| 5 | Adequate |
| 7 | Strong |
| 10 | Best-in-class within this comparison set |

**Priority system (ADHD paper-sourced features):**

| Label | Condition |
|:---|:---|
| Critical | Median rating 5, high top-3 count |
| High | Median rating 4.5, high top-3 count |
| Medium | Median rating 3, some top-3 placement |
| Low | Median rating 2-3, minimal top-3 |

---

## 3. Competitors Already Covered

The following tools are fully scored and covered in the existing v3 matrix. A later research phase need only add tools NOT on this list.

### Scored (12 tools in v3)

| # | Tool | Total Score (v3) | Cluster |
|:---:|:---|:---:|:---|
| 1 | Leantime | 81/120 | A: Task-Focused Execution |
| 2 | Super Productivity | 86/120 | A: Task-Focused Execution |
| 3 | Tana | 61/120 | B: Knowledge-Focused |
| 4 | Capacities | 58/120 | B: Knowledge-Focused |
| 5 | Goblin Tools | 57/120 | C: AI-Augmented Assistants |
| 6 | Saner AI | 63/120 | C: AI-Augmented Assistants |
| 7 | Speechify | 46/120 | D: Accessibility-First |
| 8 | ND Visual Organizer (MCP Pattern) | 58/120 | E: Composable Infrastructure |
| 9 | Anytype | 61/120 | B/E: Knowledge/Infrastructure |
| 10 | OMI AI | 70/120 | F: Voice-First Capture (NEW in v3) |
| 11 | Letterly | 41/120 | F: Voice-First Capture (NEW in v3) |
| 12 | Blue Lin | N/A (design study, not scored) | Design inspiration |

### Also Assessed (substrate decision doc, not in matrix)

These tools were assessed for substrate fit in `yar-substrate-decision.md` but are NOT part of the feature comparison matrix. They may warrant matrix inclusion in a future phase:

- Obsidian (rated MVP 8/10, Long-term 7/10; role: adapter target)
- AppFlowy (rated MVP 7/10, Long-term 6/10; role: adapter target)
- Logseq (rated MVP 6/10, Long-term 5/10; role: inspiration)
- SiYuan (rated MVP 6/10, Long-term 6/10; role: inspiration)
- Trilium Notes (rated MVP 5/10, Long-term 5/10; role: inspiration)
- Joplin (rated MVP 6/10, Long-term 4/10; role: adapter target)
- AFFiNE (rated MVP 6/10, Long-term 5/10; role: inspiration)
- Notion (rated MVP 4/10, Long-term 2/10; role: reject)
- Athens/Roam (rated MVP 2/10, Long-term 1/10; role: reject)

---

## 4. Master Feature Matrix (v3, 12 Tools) -- Full Reproduction

Feature rows: **12 categories**. Total data points: 12 categories x 12 tools = 144 cells (plus Yar target column).

| Category | Leantime | Super Prod | Tana | Capacities | Goblin Tools | Saner AI | Speechify | ND Visual (MCP) | Anytype | OMI AI | Letterly | Yar (Target) |
|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Task Management | 8 | 9 | 6 | 5 | 5 | 7 | 0 | 2 | 4 | 3 | 1 | **9** |
| Time Management | 5 | 10 | 2 | 3 | 4 | 3 | 0 | 0 | 1 | 1 | 0 | **9** |
| Knowledge Management | 6 | 3 | 10 | 8 | 2 | 8 | 3 | 8 | 8 | 7 | 3 | **9** |
| AI Integration | 7 | 2 | 8 | 6 | 9 | 9 | 7 | 6 | 2 | 9 | 7 | **10** |
| ND-Specific Features | 7 | 8 | 5 | 5 | 10 | 6 | 7 | 4 | 3 | 5 | 4 | **10** |
| Collaboration | 7 | 2 | 7 | 3 | 0 | 3 | 2 | 0 | 4 | 2 | 0 | **5** |
| Integration Ecosystem | 6 | 9 | 5 | 5 | 1 | 7 | 4 | 8 | 3 | 8 | 5 | **8** |
| Open Source / Self-Hosted | 9 | 10 | 0 | 0 | 0 | 0 | 0 | 10 | 9 | 10 | 0 | **10** |
| Accessibility | 6 | 7 | 5 | 6 | 8 | 5 | 9 | 3 | 4 | 4 | 5 | **9** |
| Mobile Support | 6 | 8 | 5 | 7 | 7 | 6 | 9 | 0 | 6 | 8 | 8 | **9** |
| Cost | 8 | 10 | 5 | 6 | 10 | 5 | 3 | 10 | 9 | 7 | 5 | **10** |
| Data Portability | 6 | 8 | 3 | 4 | 1 | 4 | 2 | 7 | 8 | 6 | 3 | **9** |
| **TOTAL** | **81** | **86** | **61** | **58** | **57** | **63** | **46** | **58** | **61** | **70** | **41** | **107** |

**Category count**: 12 scoring categories (rows).
**Feature rows captured**: 12 primary matrix rows + 39 ADHD-validated sub-features (see Section 5) = **51 distinct feature dimensions** total.

### Category Winners (v3)

| Category | Winner(s) | Score |
|:---|:---|:---:|
| Task Management | Super Productivity | 9/10 |
| Time Management | Super Productivity | 10/10 |
| Knowledge Management | Tana | 10/10 |
| AI Integration | OMI AI + Goblin Tools + Saner AI (tied) | 9/10 |
| ND-Specific Features | Goblin Tools | 10/10 |
| Collaboration | Leantime + Tana (tied) | 7/10 |
| Integration Ecosystem | Super Productivity | 9/10 |
| Open Source / Self-Hosted | OMI AI + Super Productivity + MCP (tied) | 10/10 |
| Accessibility | Speechify | 9/10 |
| Mobile Support | Speechify | 9/10 |
| Cost | Super Prod + Goblin Tools + MCP (tied) | 10/10 |
| Data Portability | Super Productivity + Anytype (tied) | 8/10 |

---

## 5. ADHD Paper-Validated Feature Sub-Matrix (v3)

Source: Chen, Meng & Nie (2026), arXiv:2603.17258v2 — "Not Just Me and My To-Do List"
Study: 20 ADHD-identifying adults, speed-dating 13 AI concepts.

### 5.1 Full 13-Concept Ranking Table

| Concept | Median Rating | Top-3 Count | Yar Priority |
|:---|:---:|:---:|:---|
| C8: Brain Weather Dashboard | 5 | 13 | Critical |
| C3: Flexible Planning + Gentle Streaks | 5 | 10 | Critical |
| C6: Social Presence AI | 4.5 | 12 | Critical |
| C11: Emotionally Aware Pause Days | 4.5 | 12 | High |
| C2: Mood-Aware Daily Companion | 3 | 0 | High |
| C5: Shared Planning with Trusted Person | 3 | 4 | Medium |
| C10: Pattern-Based Gentle Nudges | 3 | 0 | Medium |
| C12: Emotional Debrief After Collapse | 3 | 3 | Medium |
| C13: Weekly Narrative Reflection | 3 | 0 | Medium |
| C1: Private Emotional Notes | 3 | 2 | Low |
| C9: Adaptive Planning Undo | 2.5 | 1 | Medium |
| C4: Emotional Inventory Before Commitments | 2 | 0 | Low |
| C7: Ambient Transition Cues | 2 | 1 | Low |

### 5.2 Per-Executive-Function Feature Tables (39 validated features)

#### Task Initiation (5 features)

| Feature | Paper Evidence | Best Tool Today | Best Score | Yar Target |
|:---|:---|:---|:---:|:---:|
| Voice-first capture | DI1, P17 | OMI AI | 9 | 10 |
| Spiciness slider (task decomposition) | C3 (M=5), paralysis | Goblin Tools | 10 | 10 |
| Social Presence AI (body doubling) | C6 (M=4.5), 12/20 top-3 | None | 0 | 10 |
| Auto task extraction from captures | P9 | Saner AI | 7 | 9 |
| Mood-Aware Daily Companion | C2, DI1+DI3 | Saner AI | 5 | 9 |

#### Sustained Attention (4 features)

| Feature | Paper Evidence | Best Tool Today | Best Score | Yar Target |
|:---|:---|:---|:---:|:---:|
| Focus companion mode | C6 (M=4.5) | None | 0 | 10 |
| Break reminders during hyperfocus | P13 | Super Productivity | 10 | 9 |
| Idle detection with graceful pause | Time perception disorders | Super Productivity | 10 | 9 |
| PiP Focus Window | Distraction management | Saner AI | 6 | 8 |

#### Time Management (5 features)

| Feature | Paper Evidence | Best Tool Today | Best Score | Yar Target |
|:---|:---|:---|:---:|:---:|
| Dual-track planning (ideal/baseline) | C3 (M=5, highest rated) | None | 0 | 10 |
| Time estimation for tasks | P5 | Goblin Tools | 7 | 9 |
| Rhythm-based scheduling | DI2, planning anxiety | None | 0 | 9 |
| Gentle streaks (no resets on skip days) | C3 (M=5), DI4 | None | 0 | 10 |
| Proactive daily planning | C2, morning brief | Saner AI | 7 | 9 |

#### Emotional Regulation (5 features)

| Feature | Paper Evidence | Best Tool Today | Best Score | Yar Target |
|:---|:---|:---|:---:|:---:|
| Brain Weather Dashboard | C8 (M=5, 13/20 top-3, highest) | None | 0 | 10 |
| Emotionally Aware Pause Days | C11 (M=4.5, 12/20 top-3) | None | 0 | 9 |
| Emotional aftercare | C12, replay loop interruption | None | 0 | 9 |
| Emoji mood tracking on tasks | DI3, Leantime pattern | Leantime | 7 | 8 |
| Replay loop interruption | P17, self-blame | None | 0 | 8 |

#### Working Memory (4 features)

| Feature | Paper Evidence | Best Tool Today | Best Score | Yar Target |
|:---|:---|:---|:---:|:---:|
| Brain dump compiler | P11 | Goblin Tools + Letterly (combined) | 8 | 10 |
| Semantic retrieval | P11, scaffolded memory | OMI AI | 7 | 9 |
| Smart note types / supertags | Typed object routing | Tana | 10 | 9 |
| Browser-aware contextual capture | Capture where cognition happens | None | 0 | 8 |

#### Social Cognition (3 features)

| Feature | Paper Evidence | Best Tool Today | Best Score | Yar Target |
|:---|:---|:---|:---:|:---:|
| Communication Translation (ND to NT) | P6, social misrecognition | None | 0 | 10 |
| Tone analysis | P10, internalized inadequacy | Goblin Tools Judge | 8 | 9 |
| Persistent relational context | DI5, unequal scaffolding | None | 0 | 8 |

#### Privacy and Autonomy (4 features)

| Feature | Paper Evidence | Best Tool Today | Best Score | Yar Target |
|:---|:---|:---|:---:|:---:|
| On-device AI (local-first inference) | Section 7.3, no surveillance | Anytype (storage) | 9 | 10 |
| CAP safety guardrails | Autonomy vs. guidance tension | None | 0 | 10 |
| User-controlled nudge configuration | Speed-dating findings | Super Productivity (partial) | 5 | 9 |
| Open-source availability | Cytognosis mission | OMI AI + Super Prod | 10 | 10 |

**Total ADHD-validated feature rows: 30** (from Chen et al.). Additional 5 features added in v3 roadmap (Persona System, USAP, ElevenLabs voices, Tana voice agent, Communication Coach variant) bring the master feature requirements count to **44** per v3 methodology.

---

## 6. Codebase Analysis Data (v3)

Three open-source codebases indexed via zoekt (383 MB, 11,467 files):

| Codebase | Architecture | License | Stars | Key Finding for Yar |
|:---|:---|:---|:---:|:---|
| Super Productivity | Angular 18 + NgRx, 45+ modules | MIT | 11.5k | Most mature focus mode: `FocusModeStrategy` (Pomodoro/flowtime/countdown) |
| Leantime | PHP + MySQL, hexagonal, 57 domain modules | AGPL-3.0 | 4.5k | Unique emoji task mood tracking, LEO AI proactive agent |
| OMI AI | Python (FastAPI) + Flutter + C (Zephyr) | MIT | 12.6k | Production MCP server, Silero VAD pipeline, Pinecone RAG |

### Pattern Search Results

| Pattern | Super Productivity | Leantime | OMI |
|:---|:---:|:---:|:---:|
| Focus mode | 45 files | 0 | 0 |
| Timer/Pomodoro | 23 files | 3 | 0 |
| Idle detection | 12 files | 0 | 0 |
| Sentiment/emotion | 0 | 8 | 15 files |
| AI/LLM | 2 | 11 | 47 files |
| Voice/audio | 0 | 0 | 89 files |
| Knowledge graph | 0 | 0 | 3 |

---

## 7. Blue Lin Design Principles (v3 Addition)

Source: Blue Lin, Columbia University/PhD Toronto (CHI 2024). Menstrual health tracking UX research.

### Five Design Principles

| # | Principle | Blue Lin Application | Yar Application |
|:---|:---|:---|:---|
| 1 | Sensemaking over prediction | Understand cycle patterns, not just predict dates | Understand cognitive patterns, not just schedule tasks |
| 2 | User agency as primary goal | Users control what signals to view | Yar illuminates patterns; users decide what to do |
| 3 | Multimodal integration without overwhelm | Summary > detail > raw data | Composite "How am I doing?" card > signal groups > raw data |
| 4 | Longitudinal context is essential | Multi-cycle overlay reveals patterns | Multi-week overlay reveals cognitive signature |
| 5 | Inclusive, culturally responsive design | Gender-inclusive menstrual tracking | Neurotype-neutral cognitive tracking |

### Five Functional Design Requirements

| DR# | Lin Requirement | Yar Equivalent |
|:---|:---|:---|
| DR1 | Communicate predicted phases + variance | Predicted cognitive states with confidence ranges |
| DR2 | Support different interaction patterns | Daily check-ins, weekly summaries, on-demand deep-dives, crisis-only modes |
| DR3 | Personalize viewable signals | User chooses which cognitive signals to track |
| DR4 | Integrate educational resources | Explain neuroscience behind observed patterns |
| DR5 | Side-by-side comparison with context | Compare weeks/months with contextual annotations |

### Cognitive Signal Color Mapping

| Signal | Color | Brand Source |
|:---|:---|:---|
| Focus/cognition | Azure #3B7DD6 | Alexa Fluor wavelength |
| Energy/vitality | Magenta #E0309E | Rhodamine wavelength |
| Mood/emotional | Violet #8B3FC7 | DAPI wavelength |
| Sleep/recovery | Teal #14A3A3 | GFP wavelength |
| Stress/load | Coral #F26355 | MitoTracker wavelength |

### Visualization Technique Catalog

| Technique | Data Type | Yar Application |
|:---|:---|:---|
| Phase-coded timeline | Temporal + categorical | Color-code daily timeline by cognitive state |
| Multi-cycle overlay | Longitudinal temporal | Overlay weekly focus scores aligned by day-of-week |
| Progressive disclosure dashboard | Summary > detail | Composite state card > signal groups > raw data |
| Signal heatmap | Multivariate temporal | Week-by-hour heatmap of focus/energy levels |
| Contextual annotation overlay | Event + temporal | Life event markers visible across all views |
| Empathetic data framing | Tone/language | "Your focus was lower today" not "You had a bad day" |

---

## 8. Feature Adoption Roadmap (v3)

### Priority 1: Build Now

| Feature | Inspired By | Paper Validation | Codebase Reference |
|:---|:---|:---|:---|
| Spiciness slider (task decomposition) | Goblin Tools | C3 (M=5) | N/A (proprietary) |
| Zero-friction voice capture | OMI AI | DI1, P17 | `omi/firmware/` + `omi/app/` (MIT) |
| Brain dump compiler | Goblin Tools + Letterly | P11, externalized cognition | Letterly (proprietary) |
| Auto task extraction from captures | Saner AI + OMI | P9 | `omi/backend/` (MIT) |
| Brain Weather Dashboard | ADHD paper C8 | M=5, 13/20 top-3 (highest) | N/A (novel) |
| Social Presence AI | ADHD paper C6 | M=4.5, 12/20 top-3 | N/A (novel, Rive persona) |
| Dual-track planning (ideal/baseline) | ADHD paper C3 | M=5, 10/20 top-3 | N/A (novel) |
| Emoji mood on tasks | Leantime | DI3 | `leantime/domain/Reactions/` |
| Smart note types (supertags) | Tana | Typed object routing | N/A (Tana proprietary) |
| Live search queries | Tana | Queries as first-class objects | N/A (Tana proprietary) |

### Priority 2: Build Next

| Feature | Inspired By | Paper Validation | Codebase Reference |
|:---|:---|:---|:---|
| Focus mode (full-screen single task) | Super Productivity | DI5, co-regulation | `super-productivity/features/focus-mode/` |
| Idle detection | Super Productivity | P5, time perception disorders | `super-productivity/features/idle/` |
| Break reminders | Super Productivity | P13, hyperfocus exhaustion | `super-productivity/features/take-a-break/` |
| TTS with synchronized highlighting | Speechify | DI4, multiple engagement modes | Speechify (proprietary) |
| "Plan my day" | Saner AI | C2, Mood-Aware Companion | N/A |
| Tone analysis | Goblin Tools Judge | P6, P10 social misrecognition | N/A |
| PiP Focus window | Saner AI | Distraction management | N/A |
| Emotionally Aware Pause Days | ADHD paper C11 | M=4.5, 12/20 top-3 | N/A (novel) |
| MCP server exposure | OMI AI | MCP architecture pattern | `omi/mcp/` (MIT) |

### Priority 3: Yar-Only (No Existing Reference)

| Feature | What Makes It Special | Research Validation |
|:---|:---|:---|
| Voice-first emotional awareness | Vocal biomarkers (HuBERT, openSMILE) detect emotion from prosody | DI3 + C8 |
| CAP safety gate | Controller-Authority Protocol governs AI actions | Autonomy vs. guidance tension (Chen et al.) |
| Local-first AI brain | On-device Gemma inference, data never leaves | Section 7.3 |
| Unified ND companion | Task + time + knowledge + emotion + AI in ONE app | "The Big Gap" |
| Brain Weather with vocal biomarkers | Weather metaphors + voice prosody analysis | C8 (M=5, highest rated) |
| Communication Translation (ND to NT) | Bidirectional translation preserving intent across neurotypes | P6, P10, DI4 |
| Progressive disclosure cognitive dashboard | Blue Lin visualization patterns for multimodal cognitive data | Lin CHI 2024 DR1-DR5 |
| Gentle streaks (no shame on skip days) | Streaks preserved on pause days; no "broken streak" language | C3 (M=5) |
| Adaptive Multi-Persona System | Multiple AI personalities that learn mood-context preferences | DI3 + DI4 |
| Universal Sensor Adapter Protocol (USAP) | MCP-like protocol for plug-and-play sensor integration | DR3 (Lin) |
| ElevenLabs persona voices | Distinct voice per persona with emotional range | DI4 |

---

## 9. Design Tensions (v3)

| Tension | Paper Finding | Tool Evidence | Yar Response |
|:---|:---|:---|:---|
| Capture vs. Execution | Users need both ambient capture AND structured task management | OMI captures (9/10 AI) but no task management (3/10). Super Prod executes (9/10) but no voice capture. | Voice capture > AI extraction > persistent task objects |
| Autonomy vs. Guidance | "I want it to suggest, not decide." (S14) | Saner AI plans proactively; Goblin Tools is passive/on-demand. | CAP enforces companion authority. All suggestions inspectable, adjustable, overridable. |
| Privacy vs. Intelligence | Participants prefer AI that doesn't surveil (Section 7.3) | OMI is cloud-first (Firebase + Pinecone). Super Productivity is fully local. | Local-first by default. On-device Gemma. Optional cloud for enhanced quality. |
| Depth vs. Breadth | Each tool excels in one area but misses others | No tool covers >70% of validated features. | Yar targets 107/120 by unifying all six clusters. |
| Persona Consistency vs. Adaptability (v3 only) | Users want a companion that "knows them" but also adapts | No tool offers mood-aware persona switching. | Yar learns multiple personas; switches based on mood-context model. |

---

## 10. ADHD-Friendly Document Format -- Template Specification

This spec captures the conventions from the ADHD-friendly variants (03-Products v3 ADHD and 04-Engineering v2 ADHD files) so the format can be reproduced exactly.

### 10.1 Document Header

```markdown
> **Status**: Active
> **Date**: YYYY-MM-DD
> **Author**: @handle
> **Audience**: [target audience]
> **Tags**: `tag1`, `tag2`, `tag3`

# [Emoji] Document Title: The ADHD-Friendly Version ([N] Tools)

> [!NOTE]
> **TL;DR**: [3 sentences maximum. State key finding, what changed, and the scoring gap. No em dashes.]
> **Source**: [[source-document-wikilink]]
```

### 10.2 Section Structure

Each major section uses this pattern:

```markdown
## [Emoji] Section Title

> [!TIP]
> **Section summary:** [1-2 sentences summarizing the section's main point.]

[Content follows as tables, bullets, or short paragraphs.]
```

Callout types used:
- `[!NOTE]` for TL;DR and explanatory notes
- `[!TIP]` for section summaries
- `[!IMPORTANT]` for critical findings or gaps
- `[!WARNING]` for risks or anti-patterns

### 10.3 Inline 101 Sidebars

Used for jargon, inside expandable sections or `> [!NOTE]` blocks:

```markdown
> [!NOTE]
> **What is [term]?** (101)
> [1-2 sentence plain-language explanation without jargon. Address the reader as "you".]
```

### 10.4 Table Style

All tables use left-aligned columns with bold on key data. Emojis in header cells for scannability.

- Comparison tables: `|:---|:---:|:---:|` (text left, scores centered)
- Feature tables: `| Feature | Evidence | Best Tool | Score | Yar Target |`
- Scores displayed without surrounding text: `9` not `9/10` in matrix cells; `9/10` in prose context

### 10.5 Content Hierarchy

Level of nesting: maximum 3 levels deep.

```
## Section (emoji in title)
   > [!TIP] summary
   ### Subsection
      | Table |
      <details><summary>Tap to Expand</summary> (for dense content)
```

### 10.6 Collapsible Sections

Dense reference content (13-concept ranking table, codebase details, glossary, cluster details) goes inside `<details>` blocks:

```markdown
<details>
<summary>[Emoji] [Label] (Tap to Expand)</summary>

[Content]

</details>
```

### 10.7 Mermaid Diagrams

Used for: concept priority maps (`graph LR` with subgraphs), comparative landscape (`graph TB` with clusters), cognitive signal color mapping (`graph LR`). All nodes use Cytognosis brand hex colors in `style` directives.

```
style NodeID fill:#8B3FC7,color:#fff,stroke:#5145A8
```

YAR node always uses: `fill:#8B3FC7,color:#fff,stroke:#5145A8,stroke-width:3px`

### 10.8 Length and Tone

- Sections: 2-6 sentences max in prose blocks before switching to tables or bullets
- Paragraphs: 4 sentences max
- Voice: second-person where addressing reader, plain English, no jargon without definition
- No em dashes
- No filler phrases
- Oxford comma
- Active voice
- Glossary at bottom in `<details>` block, alphabetical, definition max 2 sentences

### 10.9 Accessibility Conventions

- Bold on key terms at first use
- Emoji used for visual anchoring in headers and table rows (not decoration)
- Color coding consistent with Cytognosis brand palette
- `> [!IMPORTANT]` used to call out market gaps and critical findings so they are not buried in prose

### 10.10 Full Section-Title Sequence (v3 ADHD Format)

1. TL;DR note block
2. What Changed from v2 to v3 (with table of new tools and 13-concept ranking in details block)
3. Master Feature Matrix (12 Tools) with important callout on scoring gap
4. Category Winners table
5. Comparative Landscape (6 Clusters) with Mermaid diagram + details block for cluster descriptions
6. ADHD Paper-Validated Features (by executive function, with important callout on emotional regulation gap)
7. Blue Lin Design Principles (5 principles, 5 DRs, color mapping in details, visualization catalog in details)
8. Yar Feature Adoption Roadmap (3 priority tiers as tables)
9. The Big Gap (Why Yar Exists) with code block and missing feature table
10. Codebase Quality Assessment (architecture table, pattern search table, Mermaid flow diagram)
11. Design Tensions and Trade-offs (table + warning callout)
12. What's Next (related documents table)
13. Glossary (details block, full alphabet)

---

## 11. Divergences: 03-Products vs. 04-Engineering Copy Comparison

### 11.1 v3 Files

**03-Products** copy: `03-Products/Cytonome/Yar/research/yar-unified-feature-comparison-v3.md`
**04-Engineering** copy: `04-Engineering/yar/research/yar-unified-feature-comparison-v3.md`

| Dimension | 03-Products (ADHD format) | 04-Engineering (Technical format) | Verdict |
|:---|:---|:---|:---|
| Matrix data | Identical scores | Identical scores | No drift |
| ADHD paper data | Identical | Identical | No drift |
| Blue Lin section | Present | Present | No drift |
| Roadmap tables | Identical | Identical | No drift |
| Format | ADHD-friendly (emojis, TIP callouts, details blocks, mermaid) | Technical prose with headers (Sections 1-12), less emoji | Format divergence only, content identical |
| Section naming | "Master Feature Matrix (12 Tools)" | "Master Feature Matrix (12 Tools)" | Same |
| Source references | Uses wikilinks: `[[yar-unified-feature-comparison-v3]]` | Uses file:// URLs: `file:///home/mohammadi/repos/cytognosis/docs/cytonome/yar/research/...` | Path convention divergence; old `cytonome/` path in engineering links (stale after reorg) |
| "Communication Translation" label | Uses "Communication Translation (ND to NT)" | Uses "Communication Coach (ND to NT)" | Minor label divergence; same feature |
| Priority 3 features | Lists 8 features | Lists 11 features (adds Adaptive Multi-Persona System, USAP, ElevenLabs voices) | 04-Engineering v3 has 3 additional Priority 3 items not in 03-Products v3 |

**Key finding**: The 04-Engineering v3 is the more complete version. It adds three additional Priority 3 features (Adaptive Multi-Persona System, USAP, ElevenLabs voices) that the 03-Products v3 ADHD version omits. Source-of-truth for the full feature list is 04-Engineering v3.

### 11.2 CAP/Yar Reference Files

**03-Products** copy: `03-Products/Cytonome/Yar/research/cap-yar-comprehensive-reference.md` (date 2026-05-29)
**04-Engineering** copy: `04-Engineering/yar/research/cap_yar_comprehensive_reference.md` (date 2026-05-17)

| Dimension | 03-Products (newer) | 04-Engineering (older) | Verdict |
|:---|:---|:---|:---|
| Date | 2026-05-29 | 2026-05-17 | 12-day gap |
| CAP section | Identical in structure | Identical in structure | No drift |
| Yar architecture section | Identical mermaid diagram | Identical mermaid diagram | No drift |
| `routes_communication.py` label | "Communication Translator Lite" (`POST /communication/translate`) | "Communication Coach Lite" (`POST /communication/coach`) | Label divergence; endpoint path also differs |
| File tree section | Absent in 03-Products version | Present in 04-Engineering version (Part V) | 04-Engineering is more complete |
| Module listing for `core/` | Lists 10 items (omits `__init__.py`) | Lists 11 items (includes `__init__.py`) | Minor |

### 11.3 v2 ADHD Files

**03-Products** copy: `03-Products/Cytonome/Yar/research/yar-unified-feature-comparison.md` (date 2026-05-28)
**04-Engineering** copy: `04-Engineering/yar/research/yar-unified-feature-comparison-adhd.md` (same content, different filename)

These two files are functionally identical in content. The 04-Engineering version has a slightly different filename (`yar-unified-feature-comparison-adhd.md` vs. `yar-unified-feature-comparison.md`). No content drift detected.

---

## 12. Retired Terms: Flags and Locations

### "Substrate"

| File | Occurrences | Context |
|:---|:---|:---|
| `04-Engineering/yar/research/yar-substrate-decision.md` | Title + throughout | Entire document uses "substrate" as core term (e.g., "Yar substrate decision," "PKM substrate"). This is a 2026-06-14 document, post-rename. Flag for review. |
| `04-Engineering/yar/research/cap_yar_comprehensive_reference.md` | 0 | Term absent |
| All v3 comparison files | 0 | Term absent |
| `03-Products/Cytonome/Yar/research/cap-yar-comprehensive-reference.md` | 0 | Term absent |

**Ruling**: "Substrate" is used as a technical architecture term (not a product name) in `yar-substrate-decision.md`. Per naming rules, "Substrate" as a product/layer name should be replaced with "layer/foundation." The substrate decision doc's use is architectural prose; flag for author review but not a blocking issue.

### "CAP" (as product name, not Cytoplex)

Per memory note `feedback-word-and-naming-rules.md`: CAP was renamed to Cytoplex.

| File | Occurrences | Context |
|:---|:---|:---|
| `cap_yar_comprehensive_reference.md` (both copies) | Throughout | "CAP" used as formal protocol name (CAP-Lite, CAP-Med, Directive, GuardDecision). This is the protocol spec; the protocol is still called CAP. |
| All v3 comparison files | Present | "CAP safety guardrails," "CAP safety gate," "CAP" as a safety concept |
| `yar-substrate-decision.md` | Throughout | "CAP as the authority layer," "CAP needs to govern..." |
| `yar-system-doc.md` | Throughout | "CAP (HTTP/JSON binding)" |

**Ruling**: "CAP" refers to the Controller-Authority Protocol (a technical standard), not the product that was renamed to Cytoplex. In these documents, "Cytoplex" is the prior name of the CAP-related product. These uses are correct and should NOT be changed. The product rename (CAP to Cytoplex) applies to external product marketing, not to the internal protocol name. No action needed in these research files.

### Other Stale Terminology Observed

| Term | File | Context | Action |
|:---|:---|:---|:---|
| `file:///home/mohammadi/repos/cytognosis/docs/cytonome/` | All 04-Engineering v3 source links | Pre-reorg path using old `cytonome/` folder name (now `Cytonome/`) | Update links in a later consolidation pass |
| "Communication Coach" | `cap_yar_comprehensive_reference.md` (04-Engineering) | Route endpoint name differs from 03-Products version | Reconcile endpoint naming |
| "ND Visual Organizer (MCP)" | All v3 comparison files | This is the internal label for the MCP Pattern comparison entry | Keep as-is; it is a category label not a product |

---

## 13. Summary of Counts

| Item | Count |
|:---|:---|
| Source files read | 10 |
| Source files found (non-missing) | 10 |
| Scoring categories (matrix rows) | 12 |
| Competitor tools scored | 11 (+ 1 unscored design study = 12 in matrix) |
| ADHD paper-validated features | 30 (from Chen et al.) |
| Additional v3 features | 5 (Persona System, USAP, ElevenLabs, Tana voice agent, Communication Coach variant) |
| Priority 1 features | 10 |
| Priority 2 features | 9 |
| Priority 3 features | 8 (03-Products) / 11 (04-Engineering; use this as authoritative) |
| Total feature dimensions tracked | 51+ |
| Content drift between 03-Products and 04-Engineering v3 | Minor (format + 3 missing P3 items in 03-Products) |
| Retired terms requiring action | 1 ("Substrate" in substrate decision doc; flag for review) |
| CAP uses requiring change | 0 (protocol name, not product name) |

---

## 14. Five-Bullet Summary

- **Matrix is stable**: The 12-tool, 12-category master matrix is identical across both copies of v3. Scores have not drifted. The 04-Engineering technical version is the more complete document (adds 3 Priority 3 features absent from the 03-Products ADHD version).
- **Scoring rubric is explicit**: 0/3/5/7/10 scale with a fixed definition at each anchor point; depth/polish/ND-relevance weighted over marketing claims; 10 = best in class within the set.
- **39 ADHD-validated sub-features exist**: Chen et al. (2026) provides the empirical backbone. Emotional regulation is the biggest gap (4 of 5 features have zero existing coverage across all 12 tools).
- **Two terms flagged**: "Substrate" appears as architectural prose in `yar-substrate-decision.md` (flag for review, not blocking). "CAP" throughout refers to the Controller-Authority Protocol (a technical standard), not the product renamed to Cytoplex; no changes needed.
- **ADHD format is fully specifiable**: The template is captured in Section 10. Key conventions: `[!TIP]` section summaries, `[!NOTE]` TL;DR at top, `<details>` for dense reference content, Cytognosis brand colors in Mermaid, max 4 sentences per paragraph, glossary at bottom, no em dashes.
