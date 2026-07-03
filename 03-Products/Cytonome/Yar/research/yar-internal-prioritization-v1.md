# Yar Internal Feature Prioritization v1

**Date:** 2026-06-21
**Version:** v1.1 (2026-06-21): founder-priority elevation of the mindmapping and capture clusters.
**Author:** Cytognosis Foundation
**Classification:** INTERNAL ONLY. Do not share with external partners or funders without explicit approval.

---

## 1. Scoring Model

**IPS (Integrated Priority Score)** = AI_Fit + Desirability + (WedgeFit x 5) + (DependencyReadiness x 5) + MoatBonus

| Component | Range | Definition |
|---|---|---|
| **AI_Fit** | 0-20 | AI_Leverage + Differentiation + ND_Impact + Feasibility (each 0-5) |
| **Desirability** | 0-20 | If Chen et al. (2026) speed-dating median exists: median x 4, capped at 20. Otherwise: ND_Impact x 3, marked "(proxy)", capped at 15. |
| **WedgeFit** | 0-3 | 3 = core daily-companion loop, 2 = strongly supports loop, 1 = adjacent or power-user, 0 = future hardware or sensor research |
| **DependencyReadiness** | 0-2 | 2 = buildable now, 1 = depends on a near-term prerequisite we are building, 0 = depends on far prerequisite (Cytoscope hardware or unbuilt research models) |
| **MoatBonus** | 0 or 5 | +5 if Cytognosis_Unique is Yes or Partial (any form); else 0 |

**Multipliers:** WedgeFit and DependencyReadiness are each multiplied by 5 before summing. Maximum possible IPS is 20 + 20 + 15 + 10 + 5 = 70.

---

## 2. Build-Wave Summary

| Wave | Count | What it is | Gating logic |
|---|---|---|---|
| **In-progress / Infra (under build, not complete)** | 5 | Enabling infrastructure in progress (F18, F19, F50, F51, F52) | No build action; scores recorded for reference |
| **Wave 0** | 2 + 2 notes | Safety gates and sensor foundations (F12, F55 in CSV; Privacy boundary schema and Crisis detection module NOT in CSV) | Must complete before Wave 1 can begin; F12 unblocks all sensor adapters; privacy-boundary schema and crisis-detection module are prerequisite infrastructure not yet represented as standalone features, create them before Wave 1 |
| **Wave 1** | 25 | Wedge core: the YC daily-companion MVP loop | WedgeFit = 3 AND buildable now; includes F01 (in progress) and F54 (in progress); founder-priority mindmapping and capture cluster elevated here |
| **Wave 2** | 24 | Moat depth: defensible differentiators and experience depth | Planned, WedgeFit 1 or 2, not in Wave 0/1/3; several safety-gated items require Wave 0 review |
| **Wave 3** | 6 | Sensors and research: wearable, vocal biomarker, connectomic, social exposome, clinical instruments | Hardware-dependent or research-stage; Mindstrong caveat applies to F40 (vocal biomarker): Mindstrong's failure shows voice biomarkers require clinical validation before any inference claim |

The founder-priority elevation moved 9 features from Wave 2 into Wave 1, raising the Wave 1 count from 16 to 25 and reducing Wave 2 from 33 to 24.

**Wave 0 note (critical):** The two CRITICAL safety infrastructure items are NOT in the 62-feature CSV. Create standalone stories for:
1. **Privacy boundary schema** (gates all data-sharing features; see safety-spec draft 2026-06-21)
2. **Crisis detection module** (gates all therapy-adjacent features; see crisis-detection-spec draft 2026-06-21)

These must be reviewed and approved before any SafetyGated=Y feature ships.

---

## 2b. Founder-Priority Track

The founder personally prioritizes two capability clusters above the model's wedge-first default: the interactive linear and nonlinear mindmapping tool and the capture-everywhere capability. These are now an explicit prioritization variable (Founder_Priority column in the CSV).

### Cluster A: Interactive Mindmapping (CU-6)

**Core features** (build within Wave 1):

| ID | Feature |
|---|---|
| F13 | Voice-grown thought map |
| F14 | Thought placement assistant |
| F15 | Spatial thought map view |
| F60 | Conversational thought map |
| F31 | Thought map reviewer |

**Support features** (build within Wave 1 to directly enable the mindmapping experience):

| ID | Feature |
|---|---|
| F58 | Names and terms you use |
| F16 | Your data in your own tools |
| F32 | Stray thought capture |
| F34 | Map to document transform (Wave 2, founder fast-follow) |
| F61 | Thought to document templates (Wave 2, founder fast-follow) |

### Cluster B: Capture Everywhere (CU-5)

| ID | Feature | Founder_Priority |
|---|---|---|
| F59 | Capture from anywhere (Cytomark Chrome extension) | Core |
| F50 | Highlight and link on any page (in progress) | Support |

### Recommended build order for this track

1. F59 Capture from anywhere and F50 Highlight and link on any page (the annotation layer is in progress; finalize Cytomark spec and ship the extension)
2. F01 Voice brain dump (already in Wave 1 and in progress) and F32 Stray thought capture (now Wave 1; quick-capture anywhere without breaking focus)
3. F58 Names and terms you use (NER layer that makes all transcription and capture accurate)
4. F13 Voice-grown thought map (the mindmap core; everything below depends on this)
5. F14 Thought placement assistant and F15 Spatial thought map view (placer and canvas view, build together as the map UI)
6. F60 Conversational thought map (chat-style entry loop into the map)
7. F31 Thought map reviewer (AI-guided re-organization; depends on a populated map)
8. F34 Map to document transform and F61 Thought to document templates (Wave 2 fast-follow; document export layer)

### Tradeoff

This track enriches the first build well beyond the minimal daily-companion MVP. The original Wave 1 was scoped to the wedge core (voice capture, task management, Brain Weather, persona). Adding the full mindmapping and capture-everywhere cluster to Wave 1 is a deliberate founder decision, not a model recommendation. Teams should plan for a larger Wave 1 scope and sequence the mindmap features after the wedge core is stable but within the same build cycle.

F47 (Untangling parallel thoughts) is explicitly excluded from this elevation. It remains a Wave 3 research item requiring an NLP source-separation model not yet built.

---

## 3. Feature Tables by Wave

### In-progress / Infra (under build, not complete) (5 features)

Correction 2026-06-21: these items were previously labeled Built from doc claims; they are in progress at best. The storage engine and cross-node sync are open decisions, tracked in SPEC-storage-engine.md, SPEC-sync-protocol.md, and STORAGE_BENCHMARK_TRACKER.md.

| ID | Feature | IPS | AI_Fit | Desirability | WedgeFit | DR | MoatBonus | SafetyGated |
|---|---|---|---|---|---|---|---|---|
| F18 | Safety and consent layer (CAP) | 64 | 19 | 15 | 3 | 2 | 5 | N |
| F19 | On-device private AI | 63 | 18 | 15 | 3 | 2 | 5 | N |
| F52 | Private local knowledge store | 40 | 15 | 15 | 0 | 2 | 0 | N |
| F50 | Highlight and link on any page | 36 | 14 | 12 | 0 | 2 | 0 | N |
| F51 | Open schema translation layer | 36 | 14 | 12 | 0 | 2 | 0 | N |

---

### Wave 0: Foundations and Safety (2 CSV features)

| ID | Feature | IPS | AI_Fit | Desirability | WedgeFit | DR | MoatBonus | SafetyGated |
|---|---|---|---|---|---|---|---|---|
| F12 | Open sensor connection layer (CSP) | 48 | 16 | 12 | 1 | 2 | 5 | N |
| F55 | Your custom tracking axes | 43 | 16 | 12 | 1 | 1 | 5 | N |

**Also required in Wave 0 (not in CSV):** Privacy boundary schema, Crisis detection module.

---

### Wave 1: Wedge Core (25 features, sorted by IPS descending)

| ID | Feature | IPS | AI_Fit | Desirability | WedgeFit | DR | MoatBonus | SafetyGated |
|---|---|---|---|---|---|---|---|---|
| F05 | Your energy and mood map | 69 | 19 | 20 | 3 | 2 | 5 | N |
| F07 | Flexible plan with a backup track | 68 | 18 | 20 | 3 | 2 | 5 | N |
| F27 | Rest day support | 67 | 19 | 18 | 3 | 2 | 5 | **Y** |
| F44 | Streaks that honor rest days | 67 | 17 | 20 | 3 | 2 | 5 | N |
| F06 | Focus companion and body doubling | 66 | 18 | 18 | 3 | 2 | 5 | N |
| F11 | Companion style and voice | 64 | 19 | 15 | 3 | 2 | 5 | N |
| F54 | Voice mood awareness | 64 | 19 | 15 | 3 | 2 | 5 | N |
| F57 | Adaptive companion that builds trust | 64 | 19 | 15 | 3 | 2 | 5 | N |
| F53 | Mood-anchored morning check-in | 63 | 18 | 15 | 3 | 2 | 5 | N |
| F17 | Private space before planning | 62 | 17 | 15 | 3 | 2 | 5 | N |
| F39 | Personalized gentle nudges | 59 | 17 | 12 | 3 | 2 | 5 | N |
| F01 | Voice brain dump | 58 | 18 | 15 | 3 | 2 | 0 | N |
| F02 | Brain dump to action plan | 58 | 18 | 15 | 3 | 2 | 0 | N |
| F03 | Tasks from your words | 58 | 18 | 15 | 3 | 2 | 0 | N |
| F04 | Right-sized task breakdown | 58 | 18 | 15 | 3 | 2 | 0 | N |
| F08 | Mood tag on tasks | 52 | 15 | 12 | 3 | 2 | 0 | N |
| F13 | Voice-grown thought map | 59 | 19 | 15 | 2 | 2 | 5 | N |
| F58 | Names and terms you use | 53 | 18 | 15 | 1 | 2 | 5 | N |
| F60 | Conversational thought map | 53 | 18 | 15 | 1 | 2 | 5 | N |
| F32 | Stray thought capture | 52 | 17 | 15 | 1 | 2 | 5 | N |
| F59 | Capture from anywhere | 51 | 16 | 15 | 2 | 1 | 5 | N |
| F14 | Thought placement assistant | 49 | 17 | 12 | 1 | 2 | 5 | N |
| F31 | Thought map reviewer | 48 | 18 | 15 | 1 | 1 | 5 | N |
| F15 | Spatial thought map view | 48 | 16 | 12 | 1 | 2 | 5 | N |
| F16 | Your data in your own tools | 48 | 16 | 12 | 1 | 2 | 5 | N |

**Wave 1 note:** F27 (Rest day support) is safety-gated. It may be built in Wave 1 but must not ship to users until Wave 0 safety gates (crisis detection module) are reviewed and approved.

---

### Wave 2: Moat Depth (24 features, sorted by IPS descending)

| ID | Feature | IPS | AI_Fit | Desirability | WedgeFit | DR | MoatBonus | SafetyGated |
|---|---|---|---|---|---|---|---|---|
| F24 | AI morning plan | 53 | 18 | 15 | 2 | 2 | 0 | N |
| F33 | Your personal vocabulary | 53 | 16 | 12 | 2 | 2 | 5 | N |
| F20 | Single-task focus mode | 51 | 16 | 15 | 2 | 2 | 0 | N |
| F48 | Gentle reset after a hard day | 51 | 19 | 12 | 1 | 2 | 5 | **Y** |
| F36 | Co-planning with a trusted person | 50 | 18 | 12 | 1 | 2 | 5 | **Y** |
| F49 | Your week as a story | 50 | 18 | 12 | 1 | 2 | 5 | N |
| F29 | Companion that learns your style | 49 | 19 | 15 | 1 | 1 | 5 | N |
| F34 | Map to document transform | 49 | 19 | 15 | 1 | 1 | 5 | N |
| F61 | Thought to document templates | 49 | 19 | 15 | 1 | 1 | 5 | N |
| F25 | Pre-send tone check-in | 48 | 18 | 15 | 1 | 2 | 0 | N |
| F41 | All-in-one ND support app | 48 | 18 | 15 | 1 | 1 | 5 | N |
| F42 | Two-way communication bridge | 48 | 18 | 15 | 1 | 1 | 5 | **Y** |
| F43 | Layered wellbeing dashboard | 48 | 18 | 15 | 1 | 1 | 5 | N |
| F45 | Mood-matched companion | 48 | 18 | 15 | 1 | 1 | 5 | N |
| F09 | Structured note types | 47 | 15 | 12 | 2 | 2 | 0 | N |
| F10 | Saved smart searches | 47 | 15 | 12 | 2 | 2 | 0 | N |
| F21 | Graceful activity pause | 47 | 15 | 12 | 2 | 2 | 0 | N |
| F22 | Gentle break prompts | 47 | 15 | 12 | 2 | 2 | 0 | N |
| F26 | Floating task reminder | 47 | 15 | 12 | 2 | 2 | 0 | N |
| F28 | Open data connections (MCP) | 47 | 15 | 12 | 2 | 2 | 0 | **Y** |
| F38 | No-penalty plan change | 47 | 17 | 10 | 1 | 2 | 5 | N |
| F23 | Read-aloud with highlighting | 46 | 16 | 15 | 1 | 2 | 0 | N |
| F35 | Energy check before saying yes | 46 | 18 | 8 | 1 | 2 | 5 | N |
| F37 | Gentle context change cues | 44 | 16 | 8 | 1 | 2 | 5 | N |

**Wave 2 note on F32:** IPS=52 places it above many Wave 2 features; build it early in Wave 2 alongside voice capture extensions.

---

### Wave 3: Sensors and Research (6 features, sorted by IPS descending)

| ID | Feature | IPS | AI_Fit | Desirability | WedgeFit | DR | MoatBonus | SafetyGated |
|---|---|---|---|---|---|---|---|---|
| F30 | Wearable sensor connection | 41 | 16 | 15 | 0 | 1 | 5 | N |
| F56 | Social connections and your mood | 43 | 18 | 15 | 0 | 1 | 5 | **Y** |
| F62 | Opt-in self-assessment tools | 48 | 18 | 15 | 0 | 2 | 5 | **Y** |
| F40 | Voice wellbeing signals (research) | 37 | 17 | 15 | 0 | 0 | 5 | **Y** |
| F47 | Untangling parallel thoughts | 37 | 17 | 15 | 0 | 0 | 5 | N |
| F46 | Brain sensor connection layer | 27 | 13 | 9 | 0 | 0 | 5 | N |

**Mindstrong caveat (F40):** Mindstrong Health's failure (2022) demonstrates that passive voice biomarkers for mental health require rigorous prospective clinical validation before any inference claim. F40 must not make any mood-inference assertion based on voice until a validated pipeline with IRB-approved data collection is in place. Frame as "research signals" not "indicators."

---

## 4. Top 12 to Build First

Ordered by wave and IPS. Items marked [SAFETY-GATED] must pass Wave 0 safety review before shipping to users.

1. **F12 - Open sensor connection layer (CSP)** | IPS 48 | Wave 0 | Foundation protocol; unblocks all sensor adapters (F30, F55); build first.
2. **F55 - Your custom tracking axes** | IPS 43 | Wave 0 | Sensor ontology layer; build alongside F12 as a unit.
3. **F05 - Your energy and mood map** | IPS 69 | Wave 1 | Highest IPS feature; Brain Weather is the defining Yar differentiator and YC demo anchor.
4. **F07 - Flexible plan with a backup track** | IPS 68 | Wave 1 | Dual-track planning with Chen validation 5.0; builds user trust in the companion loop.
5. **F44 - Streaks that honor rest days** | IPS 67 | Wave 1 | Chen validation 5.0; reframes motivation for ND users; quick to build on top of mood data.
6. **F27 - Rest day support** | IPS 67 | Wave 1 [SAFETY-GATED] | Strong Chen validation (4.5) and unique; build in Wave 1 but hold release until crisis-detection module is approved.
7. **F06 - Focus companion and body doubling** | IPS 66 | Wave 1 | Clinically validated ADHD intervention; unique; strong Chen validation (4.5).
8. **F11 - Companion style and voice** | IPS 64 | Wave 1 | Base persona prerequisite for F29, F45, and F57; must ship before persona-adaptation features.
9. **F54 - Voice mood awareness** | IPS 64 | Wave 1 | Already in progress; real-time mood inference from voice; core differentiator.
10. **F57 - Adaptive companion that builds trust** | IPS 64 | Wave 1 | Capstone of the persona system; ships alongside F11.
11. **F53 - Mood-anchored morning check-in** | IPS 63 | Wave 1 | Daily ritual anchor; validates against C2 design principle; pairs with F05.
12. **F13 - Voice-grown thought map** | IPS 59 | Wave 2 | Highest-IPS Wave 2 feature; brainmap is the second major product surface; begin as soon as Wave 1 voice loop is stable.

---

## 5. Conflicts and Judgment Calls

### High-IPS features held back by wave assignment

| ID | Feature | IPS | Why held back |
|---|---|---|---|
| F27 | Rest day support | 67 | Wave 1 build but safety-gated (therapy-adjacent burnout detection); cannot ship until Wave 0 crisis-detection module approved |
| F62 | Opt-in self-assessment tools | 48 | Raw IPS is higher than some Wave 2 items (47) but Wave 3 because clinical instruments require safety-gate review and CAP extension; data-collection validity is a prerequisite |
| F56 | Social connections and your mood | 43 | Wave 3 despite high AI-fit (18) because social-data linkage is safety-gated and requires sensor infrastructure not yet built |
| F40 | Voice wellbeing signals (research) | 37 | DR=0 (HuBERT validation pipeline not built); Wave 3 despite unique status and high AI-fit; Mindstrong caveat applies |

### Features where Chen desirability diverges from ND_Impact proxy

| ID | Feature | Chen Desirability | Proxy Desirability | Implication |
|---|---|---|---|---|
| F35 | Energy check before saying yes | 8 (C4 median 2.0) | 15 | Users rate this lower than ND researchers expect; deprioritize within Wave 2 |
| F37 | Gentle context change cues | 8 (C7 median 2.0) | 12 | Lower user pull than expected; nice-to-have in Wave 2, not urgent |
| F38 | No-penalty plan change | 10 (C9 median 2.5) | 15 | Moderate validation; build later in Wave 2 |
| F05 | Your energy and mood map | 20 (C8 median 5.0) | 15 | Users rate this higher than the ND_Impact proxy; confirms Brain Weather as top priority |
| F07 | Flexible plan with a backup track | 20 (C3 median 5.0) | 15 | Same; dual-track planning is more desirable than the proxy alone would suggest |
| F44 | Streaks that honor rest days | 20 (C3 median 5.0) | 15 | Same Chen study item as F07; rest-honoring streaks have exceptional user pull |

### DependencyReadiness conflicts

- **F57** (Adaptive companion that builds trust): assigned WedgeFit=3 and Wave 1, but technically adapts on top of F11 base personas. Both F11 and F57 are Wave 1; build them together as a unit rather than sequentially.
- **F31, F34, F61** (brainmap-dependent features): DR=1 but placed in Wave 2 correctly; do not begin these until F13 (voice-grown thought map) has shipped and populated data.
- **F43** (Layered wellbeing dashboard): DR=1 because it requires F05 Brain Weather data to be meaningful. Build the dashboard shell in Wave 2 but delay data population until F05 is running in production.

---

## 6. What Changed vs. Priority_draft

The Priority_draft field from the source CSV uses a P1/P2/P3/Infra scheme. Differences between IPS-derived wave assignments and Priority_draft are noted below.

### Features promoted by IPS model vs. Priority_draft

| ID | Feature | Priority_draft | IPS Wave | Reason for promotion |
|---|---|---|---|---|
| F39 | Personalized gentle nudges | P1 | Wave 1 | Confirmed; WedgeFit=3 and Chen validation (3.0) align with P1 |
| F17 | Private space before planning | P1 | Wave 1 | Confirmed; WedgeFit=3 and unique moat justify Wave 1 |
| F55 | Your custom tracking axes | P2 | Wave 0 | Promoted: CSP-layer infrastructure must precede any sensor adapter; P2 underestimated its foundational role |
| F13 | Voice-grown thought map | P2 | Wave 2 (top) | IPS=59 makes it the highest-priority Wave 2 item; Priority_draft did not capture the multiplicative wedge value |

### Features demoted by IPS model vs. Priority_draft

| ID | Feature | Priority_draft | IPS Wave | Reason for demotion |
|---|---|---|---|---|
| F35 | Energy check before saying yes | P2 | Wave 2 (lower priority) | Chen median 2.0 is significantly below ND_Impact proxy; real user desirability is lower than draft assumed |
| F37 | Gentle context change cues | P2 | Wave 2 (lower priority) | Chen median 2.0; deprioritized within Wave 2 relative to brainmap and capture features |
| F36 | Co-planning with a trusted person | P2 | Wave 2 (safety-gated) | P2 did not account for safety gate; must pass privacy-boundary review before shipping |
| F62 | Opt-in self-assessment tools | P3 | Wave 3 (confirmed) | Priority_draft correctly called P3; IPS model agrees due to safety gate and clinical complexity |
| F28 | Open data connections (MCP) | P2 | Wave 2 (safety-gated) | MCP exposes user data externally; P2 did not flag safety requirement |
| F48 | Gentle reset after a hard day | P2 | Wave 2 (safety-gated) | Therapy-adjacent; P2 did not flag safety gate needed |

### Summary of net changes

- **4 features promoted** (F55 most significantly, from P2 to Wave 0)
- **6 features retained at same tier** with safety flags added (F27, F28, F36, F42, F48, F62)
- **3 features deprioritized within their wave** based on Chen desirability evidence (F35, F37, F38)
- **No features dropped entirely**; all 62 remain in the model with assigned waves

---

*Generated 2026-06-21. Recompute when any of the following change: Chen et al. (2026) median scores, Cytognosis_Unique status of any feature, CSP or Cytomark spec completion status, or Wave 0 safety-gate approval status.*
