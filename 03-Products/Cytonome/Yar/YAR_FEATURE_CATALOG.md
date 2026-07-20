# Yar Feature Catalog (consolidated, canonical)

> **Status**: Active
> **Date**: 2026-07-19
> **Author**: @shahin
> **Audience**: engineers, stakeholders
> **Tags**: `yar`, `product`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

**Date:** 2026-07-19 · **Status:** canonical front door for all Yar features · **Supersedes:** the 05-31 feature master and all pre-v4 comparisons.
**Integrates:** the "Yar specs execution plan" session (16 specs, promoted to `docs/03-Products/Cytonome/Yar/spec/`), the v4 feature comparison + prioritization, the feature-naming convention, and the "Cytonome research consolidation" benchmark package.
**Reading time:** ~6 minutes. **If you only read one thing:** the Wave 1 table in §4 (the 25 wedge features being built first).

**Hierarchy:** This catalog is organized by build wave; for the domain hierarchy (6 domains, 19 clusters, 69 features) see research/FEATURE-HIERARCHY.md and research/features.json.

## 1. Scope

69 features, F01-F69, across 6 neurodivergent functional domains, plus 2 infrastructure modules (privacy boundary, crisis detection) that gate the rest. Sensor-science features are flagged for the Cytoscope project (§7). This catalog is the single index; each feature's depth lives in its spec.

## 2. Domain and naming legend

**ND functional domains:** AEF = Attention/Executive Function; ERM = Emotion Regulation/Mood; SCI = Social/Communication/Interaction; SPR = Sensory/Processing; CTO = Cognition/Thought Organization; SMI = Self-Monitoring/Insight.

**Three naming layers per feature:** affirming public label (user-facing), psychological construct tag (internal), domain code (above). **CU-1..CU-8** mark 20 features anchored to 8 named, defensible capability clusters, plus 21 additional features with no direct competitor equivalent (CSP sensor system, social tracker, adaptive personas, personal-KG NER, capture-everywhere, conversational mind-mapping, templated transformation, self-report instruments).

## 3. Prioritization (IPS) and waves

**IPS (Impact Priority Score, max 70)** = AI_Fit (0-20) + Desirability (0-20) + WedgeFit x5 + DR x5 + MoatBonus (0 or 5). **Wave 1 was founder-elevated (v1.1):** 9 mind-mapping/capture features moved up from Wave 2, raising Wave 1 from 16 to 25. Waves: 0 = safety/sensor infra, 1 = wedge, 2 = moat, 3 = sensor/hardware/research.

## 4. The features by wave

### Infrastructure (7, build first; everything depends on these)

| ID | Feature | Domain | CU | IPS |
|---|---|---|---|---|
| F18 | Safety / consent layer | ERM, SMI | | gate |
| F19 | On-device AI runtime (Gemma 4 E4B) | ERM, SMI | | 63 |
| F52 | Local knowledge store | CTO | | 40 |
| F50 | Web annotation layer | CTO | | 36 |
| F51 | Schema translation | CTO | | 36 |
| F67 | Long-term personal memory (PeT recall) | CTO | | n/s* |
| F68 | Cross-device sync | CTO | | n/s* |

*n/s = added 2026-07-19, post-matrix, not yet IPS-scored; placed in Infrastructure because every agent and wave depends on them (see `research/DEPENDENCY-GRAPH.md`).

Plus two off-catalog infra modules: **privacy-boundary schema** and **crisis-detection module** (separate build stories; gate F18/F27/F28/F36/F42/F56).

### Wave 0 (sensor + safety substrate)

| ID | Feature | Domain | CU | IPS |
|---|---|---|---|---|
| F12 | Open sensor layer (CSP) | SMI | CU-1 | 48 |
| F55 | Custom tracking axes | SMI | CU-1 | 43 |

### Wave 1 (25 wedge features, founder-elevated)

| ID | Feature | Domain | CU | IPS |
|---|---|---|---|---|
| F05 | Energy / mood map | ERM, SMI | | 69 |
| F07 | Flexible plan with backup | AEF, ERM | | 68 |
| F27 | Rest-day support (safety-gated) | ERM | | 67 |
| F44 | Streaks that honor rest | ERM | | 67 |
| F06 | Focus companion / body doubling | AEF | | 66 |
| F11 | Companion style / voice | ERM | | 64 |
| F54 | Voice mood awareness (in progress) | ERM | | 64 |
| F57 | Adaptive companion / trust | ERM, SCI | CU-3 | 64 |
| F53 | Morning check-in | ERM, SMI | | 63 |
| F17 | Private space before planning | ERM | | 62 |
| F39 | Gentle nudges | SMI | | 59 |
| F13 | Voice-grown thought map (founder priority) | CTO, AEF | CU-6 | 59 |
| F01 | Voice capture | AEF | | 58 |
| F02 | Task creation from speech | AEF | | 58 |
| F03 | Task structuring | AEF | | 58 |
| F04 | Task scheduling | AEF | | 58 |
| F58 | Personal NER | CTO | CU-4 | 53 |
| F60 | Conversational thought map | CTO | CU-6 | 53 |
| F32 | Stray-thought capture | AEF | | 52 |
| F08 | Mood tag | ERM | | 52 |
| F59 | Capture from anywhere (Cytomark) | AEF | CU-5 | 51 |
| F14 | Thought placement | CTO | | 49 |
| F31 | Map reviewer | CTO | CU-6 | 48 |
| F15 | Spatial map view | CTO | | 48 |
| F16 | Open export | CTO | | 48 |

### Wave 2 (28 moat features, incl. 2 added 2026-07-18 and 2 added 2026-07-19)

| ID | Feature | Domain | CU | IPS |
|---|---|---|---|---|
| F24 | AI morning plan (with interactive collaborative refinement) | AEF | | 53 |
| F33 | Personal vocabulary | CTO | CU-4 | 53 |
| F20 | Focus mode | AEF | | 51 |
| F48 | Gentle reset (safety-gated) | ERM | | 51 |
| F36 | Co-planning (safety-gated) | SCI | | 50 |
| F49 | Week as a story | ERM | | 50 |
| F29 | Companion learns style | ERM | | 49 |
| F34 | Map-to-doc transform | CTO | CU-7 | 49 |
| F61 | Document templates | CTO | CU-7 | 49 |
| F25 | Tone check-in | SCI | | 48 |
| F41 | All-in-one app | | | 48 |
| F42 | Two-way communication bridge (safety-gated) | SCI | CU-2 | 48 |
| F43 | Wellbeing dashboard | SMI | | 48 |
| F45 | Mood-matched companion | ERM | CU-3 | 48 |
| F09 | Notes | CTO | | 47 |
| F10 | Search | CTO | | 47 |
| F21 | Pause | AEF | | 47 |
| F22 | Break | AEF | | 47 |
| F26 | Floating reminder | AEF | | 47 |
| F28 | MCP connections (safety-gated) | | | 47 |
| F38 | No-penalty plan change | AEF | | 47 |
| F23 | Read-aloud | SPR | | 46 |
| F35 | Energy check before yes | AEF | | 46 |
| F37 | Transition cues | SPR | | 44 |

**F24 scope extension (2026-07-19):** F24 now explicitly includes interactive collaborative refinement of the daily plan: the person and the agent iterate on the plan together (reusing F60's conversational-iteration pattern) instead of a single-pass suggestion. See `yar-product-spec.md` and `prompts/daily-anchor-planner.md`.

#### Added 2026-07-18

Not yet scored in the v4 comparison matrix (post-matrix additions per D-E).

| ID | Feature | Domain / cluster | Status | Gated | Description |
|---|---|---|---|---|---|
| F63 | Invisible-disability advocacy mode | SCI / Communication coaching | planned | yes | During depressive or anxious periods, Yar helps explain your situation, needs, and what to expect to partners or colleagues, on your terms, so you are not misunderstood when you cannot perform as usual. Closes the founder-narrative "advocates for you" gap. |
| F64 | Personal compass (gentle goals) | AEF / Day planning & flexible plans | planned | no | Non-pressuring direction: gentle goals you steer by, never a performance bar. Reframes the Leantime "Goals" pattern into Yar's no-shame model. |

#### Added 2026-07-19

Not yet scored in the v4 comparison matrix (post-matrix additions per `research/FEATURE-VERIFICATION.md`).

| ID | Feature | Domain / cluster | Status | Gated | Description |
|---|---|---|---|---|---|
| F65 | Focus & adherence guardian | AEF / Focus, body-doubling & breaks | planned | yes | With your permission across chosen apps, nudges you back to the agreed plan when you drift, at an authority level you set from gentle reminder to blocking distractions. Gated on the privacy-boundary schema. |
| F66 | Ask & summarize your captures | CTO / Capture, documents & transforms | planned | no | Ask questions across your captures and get grounded summaries from your own knowledge. Usable against F52's local store on day one; quality upgrades once F67 lands. |

### Wave 3 (7 sensor / hardware / research)

| ID | Feature | Domain | CU | IPS | Note |
|---|---|---|---|---|---|
| F62 | Opt-in self-assessments (safety-gated) | SMI | CU-8 | 48 | clinical instruments (Cytoscope science) |
| F56 | Social connections / mood (safety-gated) | SCI | CU-2 | 43 | |
| F30 | Wearable connection | SMI | | 41 | CSP adapter Yar-side; biosignal science Cytoscope |
| F40 | Voice wellbeing signals (research) | ERM | | 37 | **Cytoscope** (SER, no clinical validation yet) |
| F47 | Untangling parallel thoughts (research) | CTO | | 37 | |
| F46 | Brain sensor layer (future) | SMI | CU-1 | 27 | **Cytoscope** (hardware) |
| F69 | Meeting-mode diarization | AEF | | n/s | added 2026-07-19 (reverses the D-E deferral); consent-gated plus multi-party consent-law counsel review |

## 5. Feature-to-spec map

- **SPEC-CSP:** F12, F55, F30, F46
- **SPEC-sensor-physiological:** F30
- **SPEC-sensor-speech-mentalstate:** F54, F40 (DistilHuBERT SER)
- **SPEC-sensor-social-interaction:** F56, F42
- **SPEC-neurobehavioral-axes:** axis substrate for all features
- **SPEC-personas-voice:** F11, F29, F45, F57 (Kokoro TTS)
- **SPEC-multi-agent:** F13, F14, F15, F31, F60 (3-agent loop), F18
- **SPEC-edge-ai-hybrid:** F19 (Gemma 4 E4B)
- **SPEC-storage-engine / SPEC-sync-protocol:** F52, F16, F68
- **SPEC-petkg-longmemory:** F67, F66 (PeT temporal knowledge graph + long-term recall)
- **SPEC-meeting-diarization:** F69 (consent-first; internal use now, counsel review before public release)
- **SPEC-transcriber-agent / SPEC-proofreading-agent / SPEC-mindmapping-agent:** worker-level detail under SPEC-multi-agent (F01, F13-F15, F31, F33, F58, F60)
- **SPEC-cactus-routing:** simple local-vs-cloud model selection for all agents (Cactus removed 2026-07-19; with SPEC-edge-ai-hybrid)
- **SPEC-browser-extension:** F50, F59 (WADM + Memex parity)
- **SPEC-multiplatform-delivery:** F41 delivery architecture (org interface templates)
- **MODULE-crisis-detection + privacy-boundary-spec:** gate F18, F27, F28, F36, F42, F56

## 6. Status

The 14 formal specs plus 15 ADHD variants are written and promoted to `docs/03-Products/Cytonome/Yar/spec/` (canonical). This catalog is the index over them. The Cytonome research consolidation produced a benchmark package (`.../Yar/benchmark/`): SQLite wins at 10k rows, FalkorDB at 100k, SurrealDB PATCH10; cytomem stays on Neo4j with a full-text index and HybridRetriever. Storage-engine spec stays draft until the SurrealDB v3.1.5 retest.

## 7. Cytoscope split (sensor-science leaves Yar)

Per the voice-as-sensor rule, the sensing science moves to the Cytoscope project; Yar keeps the consumption and UX. **Pure Cytoscope:** F40 (voice wellbeing SER), F46 (brain sensor hardware). **Shared (science to Cytoscope, in-app surface stays Yar):** F30 (wearable biosignal validation), F54 (DistilHuBERT model artifacts), F62 (clinical instruments). Voice-as-persona (F11, F29, F45, F57; SPEC-personas-voice) stays Yar.

## 8. Open integration deltas (status as of 2026-07-19)

1. INCORPORATION_MAP gaps: benchmark numbers into `SPEC-storage-engine` DONE (v0.2 active); CapLiteGuard into `SPEC-multi-agent` DONE (v0.2, 2026-07-19); cytos KG schema into `SPEC-CSP` still OPEN.
2. `consolidation_2026-06-21/` dir retired DONE (removed; git history retains it).
3. Spec ADHD twins: policy changed 2026-07-16, twins retired; the ADHD navigation surface is now the master-index twin `README.adhd.md` (2026-07-19).
4. Hand F40/F46 (and the science side of F30/F54/F62) to the Cytoscope project: still OPEN.
5. Stale 05-31 master and pre-v4 comparisons retired DONE.
