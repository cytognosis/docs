> **Status**: Draft
> **Date**: 2026-06-22
> **Author**: Cytognosis Foundation
> **Audience**: engineers, product researchers
> **Tags**: `neurobehavioral-axes`, `EQ-model`, `dimensional-psychiatry`, `yar`, `spec`, `ontology`, `PATO`, `OBA`, `RDoC`, `HiTOP`

# Psych-Axes Corpus Synthesis: Folding the EQ Model into SPEC-neurobehavioral-axes

**BLUF**: Cytognosis has a rich, internally consistent neurobehavioral phenotype corpus (Parts 1-3 of the psych-axes series, plus the RDoC harmonization tables and a 63-axis unified registry) that the current SPEC-neurobehavioral-axes.md was drafted without. This synthesis recommends adopting the Entity-Quality (EQ) dimension+direction model as the formal theoretical basis for Yar's axes, reconciles it with the Mood/Thought/Cognitive framing without disrupting the existing schema, and provides the precise revisions the spec needs.

**Reading time**: ~12 minutes.

---

## 1. What Exists: Corpus Inventory

Four primary documents and six data files. The archived Obsidian copy at `/home/mohammadi/Documents/_archive/old_Obsidian Vault/Science/psych/` mirrors the drafts; do not double-count. The canonical source is `/home/mohammadi/Documents/drafts/Science/psych/`.

| Source | Path | What it contributes |
|---|---|---|
| **Part 3: Dimension-Direction Model** (keystone) | `psych/neurobehavioral-dimension-direction-model.md` | EQ decomposition, 8-type deviation typology, PATO/OBA/SNOMED source assessment, augmented feature tuple |
| **Part 2: Feature Space Design** | `psych/cdisc-qrs-feature-space-design.md` | Six-layer ontology stack (OGMS/ICF/MF/RDoC/HiTOP/PROMIS), per-layer source ratings, DSM/instrument crosswalk strategy |
| **Part 1: CDISC-QRS Reference** | `psych/cdisc-qrs-comprehensive-reference.md` | Instrument catalogue (PHQ-9, GAD-7, PANSS, MADRS, PCL-5, etc.), LOINC codes, SNOMED/HPO mapping per item |
| **RDoC Harmonization** | `psych/RDoC_harmonization/` | 922 RDoC associations × 6 units; `reference_behavior.csv` = full EQ decomposition (entity CURIE + PATO quality + direction_type) for every RDoC behavior unit |
| **Unified Axis Registry** | `archive/neuro_onto/task5_unified_axes.csv` | 63 canonical axes × ontology crosswalk (RDoC, CogAtlas, HP, MFOEM, MF, NBO, SYMP, SNOMED) |
| **Behavioral Factors** | `archive/neuro_onto/task6_behavioral_factors.csv` + `task6_factor_x_axis.csv` | 13 higher-level factor groupings, factor × 63-axis membership matrix |
| **NeuroMONDO Disease Map** | `Science/NeuroMONDO_disease_classification.tsv` | MONDO disorder IDs with DOID/HPO cross-refs for disease-level linkage |
| **DSM/ICD books** | (PDF/large MD files in archive) | Present; not read for this synthesis. Cite by reference only. |

---

## 2. The Adopted Axis Model

### 2.1 Recommendation: Adopt the EQ Dimension+Direction Model

Yar should adopt the **Entity-Quality (EQ) dimension+direction model** (Part 3, 2026-05-26) as the formal theoretical basis for its neurobehavioral axis system. This is the same pattern used across the OBO phenotype world (HPO, MP, ZP via UPHENO) and SNOMED's post-coordination model.

The core formulation:

```
neurobehavioral_feature = Dimension (bearer/entity) + Deviation (signed quality)
```

- **Dimension** (the entity): the bare, sign-free neurobehavioral axis, sourced from OBA, ICF Body-Function b-codes, RDoC constructs, and Cognitive Atlas. Examples: "hedonic capacity," "sleep amount," "psychomotor activity," "speech rate."
- **Deviation** (the PATO-style quality): the direction and type of change relative to the user's baseline. Sourced from PATO and the 8-type deviation typology in Section 3 below.

A clinical term such as "anhedonia" is then a **materialized view**: `hedonic capacity` (dimension) + `decreased` (deviation). Pre-coordinated HPO/SNOMED IDs are retained as convenience labels and EHR bridges, not as the primary axis representation.

**Why this matters for Yar specifically:**
- Yar's sensors emit signed continuous scalars, not binary symptom flags. The EQ model is the correct formal interpretation layer for that data.
- The 8-type deviation vocabulary maps directly onto the on-device change detection logic (Section 6 below).
- The factored representation makes bidirectional DSM items (PHQ-9 items 3, 5, 8) bind once to a dimension and resolve direction from the sensor response, rather than requiring two separate axis entries.

### 2.2 How the EQ Model Reconciles with the Current Spec

The current SPEC-neurobehavioral-axes.md v0.1 uses three top-level axes (Mood, Thought, Cognitive) with 11 named sub-dimensions. This framing is **compatible** with the EQ model and does not need to be replaced. The reconciliation is straightforward:

**Mood, Thought, and Cognitive are high-level GROUPINGS over EQ dimensions, not the axes themselves.**

Each current sub-dimension maps to one (or occasionally two) EQ dimension(s). For example:
- `mood.valence` groups the EQ dimension "hedonic capacity / affective valence" (ICF b152, RDoC Positive Valence Systems)
- `mood.activation` groups "energy/drive" (ICF b1300) and "psychomotor activity" (ICF b147)
- `thought.rate` maps to "speech rate / verbal output" (ICF b1671, RDoC Cognitive Systems/Language)
- `cognitive.attention` maps to "attention functions" (ICF b140, RDoC Cognitive Systems/Attention)

**BDNF/TrkB stays as the neuroplasticity grounding**, not the axis taxonomy. BDNF/TrkB provides the mechanistic explanation for why these dimensions are correlated within a person and why they are modulated by neuroplastogens. It does not provide the axis vocabulary. The EQ model provides the vocabulary.

**Every axis score (the z-score scalar) carries an implicit direction facet.** A positive z-score = excess or hyperfunction on that dimension; a negative z-score = deficit or hypofunction. The 8-type typology adds semantic precision for the SPEC's Open Questions (e.g., distinguishing "dysregulation/lability" from "sustained deficit" for the crisis detection threshold in §9.4).

The net architectural delta is small: add an `eq_dimension_id` field to `NeurobehavioralSubDimension` pointing to the OBA/ICF/RDoC bearer, add a `direction_facet_type` field to `AxisScoreObservation` (or derive it from the score sign + trend), and add a reference table section to the spec. Nothing in the existing schema needs to be removed.

---

## 3. Canonical Axis Registry

The table below is the authoritative Cytognosis axis vocabulary, derived from `task5_unified_axes.csv` (63 axes) and `task6_behavioral_factors.csv` (13 factor groupings). The ontology crosswalk columns available from the CSV are shown in the header row.

**Ontology crosswalk columns available in the registry**:
`Canonical_Axis` | `Category` | `RDoC_Behaviors` | `Test_Axes` | `HP` (HPO CURIE) | `MFOEM` | `MF` | `CogAt` (Cognitive Atlas) | `NBO` | `SYMP` | `SNOMED`

Plus, from the dimension-direction model (Part 3): `OBA` (dimension bearer), `PATO` (quality/direction), `ICF_b_code` (WHO function scaffold), and `SNOMED_Interprets` / `SNOMED_HasInterpretation` (post-coordination for clinical bridge).

### 3.1 Full 63-Axis Inventory by Category

**Emotional (9 axes)**:
1. Fear/Acute Threat Response
2. Anxiety/Worry
3. Sadness/Depressed Mood
4. Anhedonia/Diminished Interest
5. Anger/Irritability
6. Pleasure/Positive Affect
7. Emotional Lability/Dysregulation
8. Distress/Stress Response
9. Guilt/Self-Blame

**Cognitive (11 axes)**:
10. Attention (Sustained)
11. Attention (Selective/Divided)
12. Working Memory
13. Long-Term Memory/Recall
14. Learning/Encoding
15. Executive Function/Cognitive Control
16. Cognitive Flexibility
17. Processing Speed
18. Language/Verbal
19. Reasoning/Abstraction
20. Planning/Goal Management
21. Orientation

**Behavioral (8 axes)**:
22. Impulse Control/Inhibition
23. Psychomotor Activity
24. Motor Control/Coordination
25. Habit/Automaticity
26. Avoidance/Withdrawal
27. Approach/Reward Seeking
28. Speech/Communication
29. Orientation *(duplicate in source; retained in Cognitive category)*

**Social (4 axes)**:
29. Social Cognition/Theory of Mind
30. Social Motivation/Attachment
31. Emotion Recognition
32. Facial Expression/Nonverbal

**Perceptual (5 axes)**:
33. Face/Social Perception
34. Visual Perception
35. Auditory Perception
36. Somatosensory/Interoception
37. Sensory Gating/Filtering

**Somatic (7 axes)**:
38. Pain
39. Fatigue/Energy
40. Gastrointestinal Symptoms
41. Cardiovascular Symptoms
42. Respiratory Symptoms
43. Neurological/Vestibular Symptoms
44. Autonomic Arousal
45. Appetite/Feeding

**Sleep (4 axes)**:
46. Sleep Onset/Maintenance
47. Sleep Quality/Architecture
48. Circadian Rhythm
49. Arousal/Wakefulness

**Psychosis (2 axes)**:
50. Unusual Beliefs/Thought Content
51. Perceptual Aberrations/Hallucinations

**Trauma (3 axes)**:
52. Trauma Re-experiencing
53. Emotional Numbing/Detachment
54. Negative Cognitions (trauma)

**Suicidality (1 axis)**:
55. Suicidal Ideation/Behavior

**Substance (1 axis)**:
56. Substance Use/Misuse

**Motivational (1 axis)**:
57. Motivation/Drive

**Personality (6 axes)**:
58. Extraversion/Social Energy
59. Agreeableness/Prosociality
60. Conscientiousness/Self-regulation
61. Openness/Intellectual Curiosity
62. Honesty-Humility
63. Antagonism/Interpersonal Hostility

### 3.2 The 13 Higher-Level Factor Groupings (from task6_behavioral_factors.csv)

These groupings sit above the 63 canonical axes and correspond to the three Yar high-level axes (Mood, Thought, Cognitive) plus broader coverage:

1. Negative Affect
2. Positive Affect/Reward
3. Cognitive Control
4. Memory/Learning
5. Social/Interpersonal
6. Language/Communication
7. Perceptual/Sensory
8. Somatic/Physiological
9. Sleep/Arousal/Circadian
10. Psychosis/Reality Testing
11. Trauma/PTSD
12. Substance/Disinhibition
13. Personality/Trait

**Mapping to Yar's three axes:**
- **Mood axis** = primarily Negative Affect + Positive Affect/Reward + (Sleep/Arousal/Circadian as covariate)
- **Thought axis** = primarily Language/Communication + Psychosis/Reality Testing (at non-clinical levels)
- **Cognitive axis** = primarily Cognitive Control + Memory/Learning + (Somatic/Physiological as covariate)

---

## 4. Direction/Deviation Vocabulary: The 8-Type Typology

Source: Part 3, Section 4 of the dimension-direction model. Each type has a PATO anchor and SNOMED qualifier. This typology is a Cytognosis editorial layer on top of PATO, not a lookup into any single source.

| # | Type | Definition | Psychiatric exemplars | PATO anchor | SNOMED qualifier |
|---|---|---|---|---|---|
| 1 | **Deficit / hypofunction** | Level below personal baseline range | Anhedonia, avolition, blunted affect, hypoarousal, cognitive slowing, social withdrawal | PATO:0000911 (decreased amount/rate) | 1250004 Decreased |
| 2 | **Excess / hyperfunction** | Level above personal baseline range | Elevated mood, pressured speech, hyperactivity, hypersomnia, hyperarousal | PATO:0001563 (increased amount/rate) | 35105006 Increased |
| 3 | **Absence / loss** | Complete loss (limit of deficit) | Mutism, akinesia, total avolition | PATO:0000462 absent | 2667000 Absent |
| 4 | **Distortion / qualitative aberration** | Function runs but yields qualitatively altered output | Delusional content, perceptual distortion, thought derailment | PATO:0000460 abnormal (qualitative) | 263654008 Abnormal |
| 5 | **Release / false generation** | Output generated with no normal input (Jacksonian "positive") | Hallucinations, intrusive thoughts, flashbacks, compulsive urges, tics | PATO:0000467 present (context-inappropriate) | 52101004 Present |
| 6 | **Dysregulation / lability** | Abnormal variability rather than a fixed shift | Affective lability, mood instability, emotional dysregulation, impulsivity | PATO:0001303 fluctuating | 25153009 Labile |
| 7 | **Mistiming / dyssynchrony** | Temporal or phase disturbance | Delayed sleep phase, circadian misalignment, diurnal mood variation | PATO delayed/early/abnormal-duration qualities | Temporal-context qualifiers |
| 8 | **Context-decoupling / inappropriateness** | Normal-magnitude function mismatched to context | Incongruent affect, fear without threat, situational vs. free-floating anxiety | PATO:0000460 abnormal (relational) | 263654008 Abnormal + finding-context |

**Key groupings for Yar:**
- Types 1-3 are the **magnitude family** (more/less/none): the axis z-score sign directly encodes these. Negative z-score = type 1 or 3; positive = type 2.
- Types 4-5 are the **quality family** (what psychosis researchers call "positive symptoms"): distortion vs. release. Sensors cannot directly detect these, but sustained excess on Thought/Perception sub-dimensions is a signal.
- Types 6-8 are the **dynamics family** (variability, timing, context): invisible to a single cross-sectional score but detectable from the longitudinal track. Type 6 maps to high `std(axis_scores[-7:])` (already in the spec's `trend = "variable"` rule). Type 7 maps to circadian disruption (already tracked via `yar.social.circadian_anchor_hour` and `yar.repro.phase_covariate`). Type 8 requires context annotation (external stressor vs. no stressor) and is outside current sensor scope.

The direction facet is what makes the current spec's `TrendEnum` values semantically precise: `declining` = type-1 movement; `variable` = type-6; `improving` = type-2 or return toward baseline.

---

## 5. Sensor-to-Axis Mapping: EQ-Layer Guidance

This section adds a formal ontology interpretation layer to the sensor mapping already in SPEC-neurobehavioral-axes.md §4.2. It does not change the mapping table; it states what each sensor output is formally populating in the EQ model.

### 5.1 Physiological Sensor (HRV/sleep/activity)

| Sensor axis | EQ dimension facet | EQ deviation facet | OBA/ICF anchor | Notes |
|---|---|---|---|---|
| `yar.physio.hrv_rmssd` | Autonomic-cardiac regulation / vagal tone | Continuous scalar; sign = deficit (decreased) or excess (increased) relative to baseline | ICF b4301 (heart rate functions, adjacent); OBA trait (autonomic reactivity) | Populates **Dimension** of `mood.activation` and `cognitive.executive`; deviation inferred from z-sign |
| `yar.physio.sleep_efficiency` | Sleep continuity (ICF b1342) | Type 1/3 deficit below baseline; type 2 excess (rare oversleeping) | OBA sleep-efficiency trait; ICF b1342 | Primary dimension driver for `mood.activation` and `cognitive.processing_speed` |
| `yar.physio.sleep_deep_duration` | Deep sleep amount (ICF b1340 sub) | Type 1 deficit most clinically relevant | OBA slow-wave sleep amount trait | Supporting dimension for `mood.activation` |
| `yar.physio.sleep_rem_duration` | REM sleep amount (ICF b1344 sleep cycle) | Type 1 deficit impairs memory consolidation | OBA REM sleep amount | Supporting for `cognitive.working_memory` |
| `yar.physio.step_count` | Physical activity / psychomotor activity (ICF b147) | Type 1 deficit = hypoactivity signal | OBA physical activity amount | Supporting for `mood.activation` |
| `yar.physio.skin_temp_deviation` | Thermoregulation (adjacent to circadian phase) | Type 7 mistiming (dysregulated temperature rhythm) | OBA skin temperature variability | Supporting for `mood.activation`; especially relevant in luteal phase (covariate) |
| `yar.physio.readiness_score` | Multi-domain recovery composite | Composite deviation; positive = deficit resolved | OBA recovery/readiness composite | Supporting for `mood.activation` and `cognitive.executive` |
| `yar.physio.spo2` | Oxygen saturation (ICF b4402 oxygen-carrying capacity) | Type 1 deficit below normal (nocturnal hypoxia) | OBA arterial oxygen saturation | Supporting for `cognitive.processing_speed` |

### 5.2 Speech Mental-State Sensor (prosody/arousal/valence/cognitive-load)

| Sensor axis | EQ dimension facet | EQ deviation facet | Notes |
|---|---|---|---|
| `yar.voice.valence` | Affective valence / hedonic tone (MFOEM hedonic valence) | Type 1 deficit = decreased positive affect; sign aligns with RDoC Positive Valence Systems | Primary driver of `mood.valence`; most direct within-session mood signal |
| `yar.voice.arousal` | Emotional arousal / affective activation (MFOEM arousal) | Type 1 = hypoarousal; type 2 = hyperarousal | Drives `mood.activation` and supports `thought.rate` |
| `yar.voice.speech_rate` | Verbal output / speech rate (ICF b1671) | Type 1 deficit = slowed speech (poverty); type 2 excess = pressured speech | Primary driver of `thought.rate`; most direct speech-organization signal |
| `yar.voice.pause_index` | Thought organization / verbal fluency (ICF b160 + b1671) | Type 4/6 distortion or dysregulation = fragmented pauses | Primary driver of `thought.organization` |
| `yar.voice.cognitive_load` | Executive/working memory load (ICF b164 + b144) | Type 1 deficit = high load (resource depletion) | Supports `thought.organization` and primary driver of `cognitive.working_memory` |
| `yar.voice.distress_signal` | Affective regulation / threshold (ICF b1521) | Type 6 dysregulation or type 8 context-decoupling | Primary driver of `mood.irritability`; feeds crisis detection |
| `yar.voice.vocal_affect_index` | Prosodic expressiveness / affective range (ICF b1522) | Type 1 deficit = blunted prosody (anhedonia marker) | Primary driver of `mood.anhedonia_signal`; supports `thought.pressure` |
| `yar.voice.energy_in_voice` | Vocal energy / speech amplitude (ICF b1671 sub) | Type 1 deficit = low vocal energy co-occurring with slowed thought | Supports `thought.rate` |

### 5.3 Social Rhythm / Withdrawal Sensor

| Sensor axis | EQ dimension facet | EQ deviation facet | Notes |
|---|---|---|---|
| `yar.social.social_rhythm_score` | Social rhythm regularity (ICF d750 + SRM theory) | Type 7 mistiming = disrupted social circadian anchor | Supporting driver of `mood.activation`; type 7 is the most meaningful direction type here |
| `yar.social.social_contact_index` | Affiliative motivation / social engagement (ICF d750, RDoC Social Processes/Affiliation) | Type 1 deficit = withdrawal below personal baseline | Primary driver of `mood.anhedonia_signal` |
| `yar.social.social_withdrawal_flag` | Affiliative motivation (same dimension as above) | Type 1 deficit (binary threshold detection) | Primary driver of `mood.anhedonia_signal`; complements continuous index |
| `yar.social.social_rhythm_deviation` | Social rhythm (see above) | Type 7 deviation magnitude | Covariate for whole Mood axis |
| `yar.social.circadian_anchor_hour` | Circadian phase / sleep-wake timing (ICF b134, RDoC Arousal/Circadian Rhythms) | Type 7 mistiming when anchor shifts | Covariate for `cognitive.executive` |

### 5.4 Menstrual Phase as Covariate

`yar.repro.phase_covariate` is not an EQ dimension; it is a **normative context modifier**. It does not enter the axis score computation. Its role is to condition the interpretation of deviation types:

- Luteal phase: reduced dopamine availability shifts the normative midpoint for several dimensions (Mood activation, executive function, working memory, irritability threshold). A z-score of -0.8 on `mood.activation` during luteal phase has a different interpretation weight than the same z-score in follicular phase.
- The SPEC should annotate the covariate context in `AxisCovariateContext.cycle_phase` (already present in the schema) and flag when longitudinal baseline statistics may be phase-confounded.
- The CDISC-QRS reference (Part 1) and PROMIS item banks do not currently stratify by menstrual phase; this is a gap in the external standards that Yar's longitudinal data can help fill.

---

## 6. External Standards: What to Cite in the Spec

The spec must stay dimensional, never diagnostic. The following standards map to specific roles:

| Standard | Role in spec | How to cite |
|---|---|---|
| **RDoC** | Mechanistic dimension source (Layer 3a). Six domains, ~36 constructs/subconstructs provide the biological grounding for each sub-dimension. | Cite per sub-dimension in the `eq_dimension_id` field; e.g., `mood.anhedonia_signal` -> RDoC Positive Valence Systems / Reward Responsiveness. |
| **HiTOP spectra** | Psychometric dimension source (Layer 3b). The 6-level hierarchy (spectra / sub-factors / syndromes / components) is the best DSM bridge without being categorical. | Cite HiTOP node for each sub-dimension; e.g., `mood.valence` -> HiTOP Internalizing / Distress component. Kotov et al. 2017 is the key reference. |
| **CDISC-QRS instruments** | Operational bindings (Layer 5). PHQ-9, GAD-7, ASRS, BRIEF-A, PSQI, WFIRS are already in the spec. MADRS, YMRS, PANSS items are relevant for future clinical-track expansion. | Already referenced in the spec's sensor-to-axis mapping table. Add CDISC QSTESTCD values to the sub-dimension definitions for regulatory interoperability. |
| **PROMIS** | IRT-calibrated subclinical measurement. Positive-pole banks (Positive Affect, Meaning and Purpose) are the normative-range anchor for the Mood axis. | Cite in the `normative_anchor` field of each dimension definition. PROMIS T-score theta is the model for the user's personal baseline distribution. |
| **ICF Body Functions** | WHO-authoritative dimension scaffold. b134 (sleep), b140-b164 (cognitive), b147 (psychomotor), b152 (emotional), b1671 (language/speech). | Cite `icf_code` field in each sub-dimension definition. |
| **OBA + PATO** | Formal EQ ontology (Tier A sources). OBA provides the sign-free dimension bearer; PATO provides the quality/direction vocabulary. Both CC BY. | Add to the spec's References section. Required for the `eq_dimension_id` and `pato_quality_id` fields proposed in Section 7 below. |
| **NeuroMONDO** | Disease-level linkage for the research track. Maps dimensional axis patterns to MONDO disorder IDs via DOID/HPO cross-references. | Cite in the spec only abstractly: "optional disease-level linkage via NeuroMONDO and MONDO disorder ontology is available for the research track and is out of scope for the core Yar product." Do not expose disorder labels to users. |
| **DSM-5-TR / ICD-11** | Reference only. These are categorical systems; the spec explicitly does not use them for axis definition. They are relevant only as bridges for clinician integration (clinician-gated, future). | A single sentence in §1 (Scope): "Axis definitions are dimensional and do not correspond to DSM-5-TR or ICD-11 categories. Mapping to those systems is available only via the research-track ontology bridge and is never surfaced to users." |

---

## 7. Precise Revisions for SPEC-neurobehavioral-axes.md

The following changes are additive. Nothing in the existing v0.1 schema is removed. All additions are clearly delineated as new subsections or new fields.

### 7.1 Section 2.1 (Why Dimensional, Not Categorical) - EXPAND

- Add a paragraph grounding the model in the EQ formalism: "Each axis is formally a **dimension** (entity/bearer) in the EQ sense: a sign-free neurobehavioral function whose value can move in either direction relative to the user's baseline. The direction of movement is captured separately as a **deviation facet**, enabling continuous, bidirectional monitoring without pre-coordinating direction into the axis name."
- Add a sentence linking to PSYCH_AXES_SYNTHESIS.md (this document) as the source of the formal EQ model and canonical axis vocabulary.
- Keep the BDNF/TrkB paragraph; add a sentence: "BDNF/TrkB provides the neuroplasticity mechanism that explains within-person axis covariation and sensitivity to treatment. It is not the source of the axis taxonomy; the axis vocabulary is derived from OBA, ICF, RDoC, and HiTOP as detailed in the synthesis reference."

### 7.2 Section 2.2 (The Three Axes) - ADD subsection 2.2a

Add a new subsection **2.2a EQ dimension grounding** with a table mapping each sub-dimension to its EQ bearer:

```
| Sub-dimension ID | EQ dimension label | OBA/ICF anchor | RDoC construct | HiTOP node |
```

Populate from the mapping in Section 5 of this synthesis. This makes the axis definitions formally computable and cross-referenceable.

### 7.3 Section 3.2 (NeurobehavioralAxisDefinition) - ADD field

Add to the `NeurobehavioralSubDimension` class:

```yaml
eq_dimension_id:
  range: string
  description: >-
    OBA identifier (preferred) or ICF b-code for the sign-free bearer dimension
    this sub-dimension tracks. E.g., "OBA:VB0003199" or "b1522".
    Source: PSYCH_AXES_SYNTHESIS.md §3.1.

pato_quality_id:
  range: string
  description: >-
    PATO quality class for the deviation type most commonly observed on this
    sub-dimension. One of the 8-type typology from PSYCH_AXES_SYNTHESIS.md §4.
    E.g., "PATO:0000911" (decreased amount, for deficit-type sub-dimensions).
```

### 7.4 Section 3.4 (AxisScoreObservation) - ADD field

Add to the `AxisScoreObservation` class:

```yaml
direction_facet_type:
  range: DeviationTypeEnum
  description: >-
    Semantically typed deviation direction for this score cycle.
    Derived from score sign and trend.
    # DeviationTypeEnum: deficit | excess | absence | distortion |
    #   release | dysregulation | mistiming | context_decoupling | neutral
  notes: >-
    Deficit = score < -0.5 stable; excess = score > +0.5 stable;
    dysregulation = std(7d) > 1.5 (maps to current "variable" trend);
    mistiming = circadian_anchor_hour deviation > 1.5h;
    neutral = score within [-0.5, +0.5]. Distortion, release, and
    context_decoupling are not inferrable from current sensors alone;
    reserved for future clinical-track integration.
```

### 7.5 Section 2.3 (Sub-Dimensions) - ADD ontology crosswalk column

Add an `EQ dimension (OBA/ICF)` column to each sub-dimension table:

**Mood sub-dimensions (additions):**
- `mood.valence`: ICF b1522 (range of emotion), RDoC Positive Valence Systems / Reward Responsiveness, HiTOP Internalizing/Distress
- `mood.activation`: ICF b1300 (energy level) + b147 (psychomotor), RDoC Arousal and Regulatory Systems
- `mood.irritability`: ICF b1521 (regulation of emotion), RDoC Negative Valence / Frustrative Nonreward, HiTOP Internalizing/Distress/Anxiousness
- `mood.anhedonia_signal`: ICF b1301 (motivation) + b1522, RDoC Positive Valence / Reward Responsiveness, HiTOP Detachment/Social Anhedonia

**Thought sub-dimensions (additions):**
- `thought.rate`: ICF b1600 (pace of thought) + b1671 (expression of language), RDoC Cognitive Systems/Language
- `thought.organization`: ICF b1601 (form of thought) + b1671, RDoC Cognitive Systems/Language
- `thought.pressure`: ICF b1600 + b1671 (compound: pace + output urgency); HiTOP Thought Disorder/Disorganization

**Cognitive sub-dimensions (additions):**
- `cognitive.attention`: ICF b140 (attention functions), RDoC Cognitive Systems/Attention, HiTOP Disinhibited Externalizing/Attentional Dysregulation
- `cognitive.working_memory`: ICF b144 (memory) + b1640 (abstraction/WM sub), RDoC Cognitive Systems/Working Memory
- `cognitive.processing_speed`: ICF b147 (psychomotor functions), RDoC Cognitive Systems
- `cognitive.executive`: ICF b164 (higher-level cognitive functions: b1641 planning, b1643 flexibility, b1644 insight, b1645 judgment), RDoC Cognitive Systems/Cognitive Control

### 7.6 New Section: Section 2.5 - Canonical Axis Vocabulary Reference

Add a new section **2.5 Canonical Axis Vocabulary and Registry** with:
- A reference to this synthesis document and the task5_unified_axes.csv for the full 63-axis registry.
- A statement: "The three Yar axes and 11 sub-dimensions are a focused subset of the 63-axis Cytognosis neurobehavioral registry, selected for sensor coverage in the current Yar sensor stack. The registry is the authoritative vocabulary source. Future sub-dimensions should be drawn from the registry before new dimensions are coined."
- The 13-factor grouping table (Section 3.2 of this synthesis), showing how Mood/Thought/Cognitive map to the broader factor structure.

### 7.7 Section 11 (References) - ADD external references

Add the following to the External References section:

```
11. Cytognosis Foundation (2026-05-26). Separating Phenotype from Direction of Change:
    A Dimension-Deviation Model for the Cytognosis Neurobehavioral Feature Space (Part 3).
    Internal working document. [Formal basis for the EQ axis model in this spec.]

12. Cytognosis Foundation (2026-05-13). Cytognosis Neurobehavioral Phenotype Feature Space:
    Design Reference (Part 2). Internal working document. [Six-layer ontology stack;
    ICF/MF/RDoC/HiTOP/PROMIS layer definitions.]

13. Cytognosis Foundation (2026-05-13). CDISC QRS Comprehensive Reference (Part 1).
    Internal working document. [Instrument catalogue, LOINC codes, crosswalks.]

14. Mungall CJ et al. (2017). The Monarch Initiative: an integrative data and analytic
    platform connecting phenotypes to genotypes across species. Nucleic Acids Research,
    45(D1), D712-D722. [UPHENO EQ unification basis.]

15. Kotov R et al. (2017). The Hierarchical Taxonomy of Psychopathology (HiTOP).
    Journal of Abnormal Psychology, 126(4), 454-477. [HiTOP 6-level hierarchy;
    DSM bridge referenced in sub-dimension crosswalk.]

16. Geneviève LD et al. PATO: The Phenotype and Trait Ontology.
    http://purl.obolibrary.org/obo/pato.owl (CC BY). [Deviation quality vocabulary.]

17. OBA: Ontology of Biological Attributes.
    http://purl.obolibrary.org/obo/oba.owl (CC BY). [Sign-free dimension bearer vocabulary.]
```

### 7.8 New Appendix: Deviation-Type to Score-State Mapping

Add an appendix (can be a small table) mapping the `DeviationTypeEnum` values to their computational definition in terms of the existing score and trend fields:

| `direction_facet_type` | Derivation rule |
|---|---|
| `deficit` | `score < -0.5` AND `trend in [stable, declining]` AND `std(7d) <= 1.5` |
| `excess` | `score > +0.5` AND `trend in [stable, improving]` AND `std(7d) <= 1.5` |
| `absence` | `score < -3.0` AND `trend = declining` (limit of deficit) |
| `dysregulation` | `std(axis_scores[-7:]) > 1.5` (maps to current `trend = "variable"`) |
| `mistiming` | `circadian_anchor_hour deviation > 1.5h` (via `covariate_context`) |
| `neutral` | `score in [-0.5, +0.5]` |
| `distortion`, `release`, `context_decoupling` | Not inferrable from current sensors; reserved for clinical-track integration |

---

## 8. Axis-ID Reconciliation

The current SPEC uses `yar.axis.*` IDs (e.g., `yar.axis.mood.valence`) for Yar-specific sub-dimensions, and `yar.physio.*`, `yar.voice.*`, `yar.social.*`, `yar.repro.*`, `yar.instrument.*`, `yar.aware.*` for sensor axes.

The 63-axis unified registry uses plain names (e.g., "Sadness/Depressed Mood", "Anhedonia/Diminished Interest"). The bridge between them is the `eq_dimension_id` field proposed in Section 7.3 above.

**Reconciliation table (current spec sub-dimensions to registry axes):**

| Yar sub-dimension ID | Registry canonical axis | Category | Registry factor grouping |
|---|---|---|---|
| `yar.axis.mood.valence` | Sadness/Depressed Mood + Pleasure/Positive Affect | Emotional | Negative Affect + Positive Affect/Reward |
| `yar.axis.mood.activation` | Fatigue/Energy + Arousal/Wakefulness | Somatic + Sleep | Sleep/Arousal/Circadian |
| `yar.axis.mood.irritability` | Anger/Irritability + Emotional Lability/Dysregulation | Emotional | Negative Affect |
| `yar.axis.mood.anhedonia_signal` | Anhedonia/Diminished Interest + Social Motivation/Attachment | Emotional + Social | Negative Affect + Social/Interpersonal |
| `yar.axis.thought.rate` | Speech/Communication + Psychomotor Activity | Behavioral | Language/Communication |
| `yar.axis.thought.organization` | Language/Verbal + Reasoning/Abstraction | Cognitive | Language/Communication |
| `yar.axis.thought.pressure` | Speech/Communication (excess pole) + Impulse Control/Inhibition | Behavioral | Language/Communication |
| `yar.axis.cognitive.attention` | Attention (Sustained) + Attention (Selective/Divided) | Cognitive | Cognitive Control |
| `yar.axis.cognitive.working_memory` | Working Memory | Cognitive | Memory/Learning |
| `yar.axis.cognitive.processing_speed` | Processing Speed + Psychomotor Activity | Cognitive + Behavioral | Cognitive Control |
| `yar.axis.cognitive.executive` | Executive Function/Cognitive Control + Planning/Goal Management | Cognitive | Cognitive Control |

**Recommended ID-management rule**: the `yar.axis.*` IDs remain the Yar-internal identifiers. The `eq_dimension_id` field holds the OBA/ICF CURIE. A separate field `registry_axes` (a list of strings) in `NeurobehavioralSubDimension` can optionally enumerate the corresponding canonical registry axis names for documentation and cross-referencing. This avoids any namespace collision.

---

## 9. What Stays Out of Scope

**Confidential factorized-PRS (genomic) layer**: optional genomic priors exist, are specified separately under controlled access, and are already noted abstractly in SPEC-neurobehavioral-axes.md §5.6. This synthesis adds nothing to that section. Do not detail the TF-region scoring or CREB/SREBP axes in any public-facing spec.

**DSM-5-TR and ICD-11 categorical labels**: the spec must never use these as axis definitions, sub-dimension names, or user-facing labels. They may appear in the `materialized_view` block of the `eq_dimension_id` description (for engineering reference) but never in user-visible outputs or in the normative schema.

---

## 10. Source File Locations (Canonical)

| Document | Canonical path |
|---|---|
| Keystone: dimension-direction model (Part 3) | `/home/mohammadi/Documents/drafts/Science/psych/neurobehavioral-dimension-direction-model.md` |
| Feature space design (Part 2) | `/home/mohammadi/Documents/drafts/Science/psych/cdisc-qrs-feature-space-design.md` |
| CDISC-QRS reference (Part 1) | `/home/mohammadi/Documents/drafts/Science/psych/cdisc-qrs-comprehensive-reference.md` |
| RDoC harmonization | `/home/mohammadi/Documents/drafts/Science/psych/RDoC_harmonization/` |
| Unified axis registry (63 axes) | `/home/mohammadi/Documents/drafts/Science/psych/archive/neuro_onto/task5_unified_axes.csv` |
| Behavioral factor groupings | `/home/mohammadi/Documents/drafts/Science/psych/archive/neuro_onto/task6_behavioral_factors.csv` |
| Factor x axis matrix | `/home/mohammadi/Documents/drafts/Science/psych/archive/neuro_onto/task6_factor_x_axis.csv` |
| RDoC behavior EQ decomposition | `/home/mohammadi/Documents/drafts/Science/psych/RDoC_harmonization/reference_tables/reference_behavior.csv` |
| NeuroMONDO disease map | `/home/mohammadi/Claude/Projects/Science and Platform/NeuroMONDO_disease_classification.tsv` |
| Archive (mirror; do not edit) | `/home/mohammadi/Documents/_archive/old_Obsidian Vault/Science/psych/` |
| Duplicate registry (do not use; superseded by drafts/) | `/home/mohammadi/Claude/Projects/Grants and Applications/task5_unified_axes.csv` |
| Target spec | `/home/mohammadi/repos/cytognosis/docs/03-Products/Cytonome/Yar/spec/SPEC-neurobehavioral-axes.md` |
