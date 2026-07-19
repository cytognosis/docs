---
spec_id: SPEC-neurobehavioral-axes
version: "0.2"
status: draft
domain: neurobehavioral-axes
owner: Shahin Mohammadi
created: 2026-06-22
last_updated: 2026-06-22
depends_on: [SPEC-CSP, SPEC-storage-engine, SPEC-sensor-physiological, SPEC-sensor-speech-mentalstate, SPEC-sensor-social-interaction, SPEC-sensor-menstrual]
implements: [CSP]
---

# SPEC-neurobehavioral-axes: Dimensional Neurobehavioral Axes

> **Reading options:** An ADHD-friendly progressive-disclosure rendering is generated from this file. The hand-maintained ADHD twin (`spec/adhd/SPEC-neurobehavioral-axes_adhd.md`) was retired 2026-07-16; see `_archive/cleanup_2026-07-16/adhd-twins/`.

> **Status**: Draft
> **Date**: 2026-06-22
> **Author**: Cytognosis Foundation
> **Audience**: engineers, researchers
> **Tags**: `yar`, `cytonome`, `csp`, `neurobehavioral`, `axes`, `dimensional`, `crdt`, `linkml`, `EQ-model`, `PATO`, `OBA`, `RDoC`, `HiTOP`, `ontology`
> **Related:** [SPEC-CSP](./SPEC-CSP.md); [SPEC-sensor-physiological](./SPEC-sensor-physiological.md); [SPEC-sensor-speech-mentalstate](./SPEC-sensor-speech-mentalstate.md); [SPEC-sensor-social-interaction](./SPEC-sensor-social-interaction.md); [SPEC-sensor-menstrual](./SPEC-sensor-menstrual.md); privacy boundary at `Cytoplex/spec/privacy-boundary-spec.md`; crisis detection at `MODULE-crisis-detection.md`; EQ model synthesis at `Yar/consolidation_2026-06-21/_research/PSYCH_AXES_SYNTHESIS.md`

---

**Reading time**: ~22 minutes.

**If you only read one thing**: Section 4 (sensor-to-axis mapping table) and Section 5 (score computation). The three neurobehavioral axes (Mood, Thought, Cognitive) are high-level groupings over dimensional, continuous neurobehavioral sub-dimensions. All scores are interpreted relative to each user's personal baseline — never against a population normal, never as a diagnostic label.

**BLUF**: This spec is the integration layer above all sensor specs. It defines the three canonical neurobehavioral axes, their sub-dimensions, the LinkML schema that represents them, the mapping from every sensor output to its contributing axis, an on-device score computation model, and a CRDT longitudinal state model for tracking axes over time. The formal theoretical basis is the Entity-Quality (EQ) dimension+direction model: every sub-dimension is a sign-free bearer (dimension facet) paired with a typed deviation (direction facet). Axis scores are derived health inferences — the most sensitive output Yar produces — and are governed accordingly under Cytoplex and the privacy boundary. Optional genomic priors may inform per-person axis baselines (specified separately under controlled access; out of scope for this spec).

---

## 1. Purpose and Scope

This spec integrates the outputs of Yar's sensor layer into three dimensional neurobehavioral axes that are the primary interface through which users understand their longitudinal patterns. The sensor specs (SPEC-sensor-physiological, SPEC-sensor-speech-mentalstate, SPEC-sensor-social-interaction, SPEC-sensor-menstrual) each produce named CSP axis observations. Those observations are inputs to this spec's aggregation and scoring layer.

**In scope:**

- Conceptual model for the three axes and their sub-dimensions, grounded in the EQ dimension+direction formalism.
- Canonical axis vocabulary: the 63-axis Cytognosis neurobehavioral registry and the 8-type deviation typology.
- LinkML schema: `AxisDefinition`, `AxisScore`, `SubDimensionScore`, `DeviationTypeEnum`, the canonical axis registry.
- Sensor-to-axis mapping: which sensor output contributes to which axis and sub-dimension, with role (primary, supporting, covariate), and which facet (dimension vs. direction) each sensor output populates.
- On-device score computation: baseline, normalization, trend detection, confidence, missing-modality handling.
- Longitudinal CRDT state model: how axis tracks are stored, updated, and queried over time.
- Privacy, governance, and Cytoplex conformance for axis scores.
- Axis-ID collision resolution across sensor specs.
- Conformance criteria and open decisions.

**Out of scope:** per-sensor inference pipelines (covered in each sensor spec), crisis escalation logic (MODULE-crisis-detection.md), the sync protocol for cross-device axis track replication (SPEC-sync-protocol.md), and the genomic prior layer (out of scope for this spec; noted abstractly where relevant).

**Canonical name reminder:** the protocol is CSP (Cytonome Sensor Protocol; formerly USAP/UBAP); do not use the deprecated aliases in new code or documentation.

---

## 2. Conceptual Model

### 2.1 Why Dimensional, Not Categorical

Mental health is not a binary state. Mood, thought patterns, and cognitive function are continuous dimensions that every person moves along throughout their life. The categorical approach (diagnosis present / absent) hides within-person variation, discards the structure that makes behavioral tracking useful, and attaches stigma to normal fluctuation.

Yar's dimensional model treats each axis as a continuous personal trajectory. A user's **Mood activation** today is not "normal" or "abnormal"; it is higher or lower than their own recent baseline, moving in a direction that may or may not be meaningful in context. This framing is:

- **Clinically grounded**: dimensional models are the dominant framework in contemporary biological psychiatry (Insel, 2014; Cuthbert and Insel, 2013; Allsopp et al., 2019). Kotov et al.'s Hierarchical Taxonomy of Psychopathology (HiTOP, 2017) is the most complete operationalization of this framework.
- **ND-affirming**: neurodivergent users show greater within-person variability than neurotypical populations. A categorical "normal" is especially inapplicable here.
- **Safe**: continuous, baseline-relative outputs cannot be directly mapped to a specific diagnostic label, reducing misuse risk.

**EQ formalism.** Each sub-dimension is formally a **dimension** (entity/bearer) in the Entity-Quality (EQ) sense: a sign-free neurobehavioral function whose value can move in either direction relative to the user's baseline. The direction of movement is captured separately as a **deviation facet**, enabling continuous, bidirectional monitoring without pre-coordinating direction into the axis name.

```
neurobehavioral_feature = Dimension (bearer/entity) + Deviation (signed quality)
```

- **Dimension**: the bare, sign-free neurobehavioral axis. Sourced from OBA, ICF Body-Function b-codes, RDoC constructs, and Cognitive Atlas.
- **Deviation**: the direction and type of change relative to the user's baseline. Sourced from PATO and the 8-type typology in §2.6.

A clinical term such as "anhedonia" is a **materialized view**: `hedonic capacity` (dimension) + `decreased` (deviation, PATO:0000911). Pre-coordinated HPO and SNOMED IDs are retained as convenience labels and EHR bridges, not as the primary axis representation. Axis definitions are dimensional and do not correspond to DSM-5-TR or ICD-11 categories. Mapping to those systems is available only via the research-track ontology bridge and is never surfaced to users.

The formal EQ model and canonical axis vocabulary are detailed in the companion synthesis document: `Yar/consolidation_2026-06-21/_research/PSYCH_AXES_SYNTHESIS.md`.

### 2.2 The Three Axes

Yar's dimensional model uses three primary behavioral axes. **Mood, Thought, and Cognitive are high-level groupings over EQ sub-dimensions, not the axis bearers themselves.** Each groups a set of EQ dimensions that share a common neurobiological substrate. The BDNF/TrkB neuroplasticity mechanism explains within-person covariation across these sub-dimensions and their sensitivity to neuroplastogenic treatments (including evidence from a bipolar proof-of-concept on McLean published data with Mt Sinai validation). BDNF/TrkB is not the source of the axis taxonomy; the axis vocabulary is derived from OBA, ICF, RDoC, and HiTOP as detailed in the synthesis reference.

| Axis | Core question | Biological grounding | EQ grouping |
|---|---|---|---|
| **Mood** | How does the user's emotional and energetic state vary over time? | BDNF/TrkB modulation of limbic circuits; estrogen-dopamine coupling; HRV as autonomic-emotional index | Negative Affect + Positive Affect/Reward factors; Sleep/Arousal/Circadian as covariate |
| **Thought** | How does the user's cognitive-linguistic processing style vary? | Prefrontal-striatal circuits; dopamine-norepinephrine balance; speech organization and rate as behavioral readouts | Language/Communication + Psychosis/Reality Testing factors (at non-clinical levels) |
| **Cognitive** | How does the user's executive and attentional capacity vary? | Prefrontal cortex; working memory load; circadian regulation of executive function | Cognitive Control + Memory/Learning factors; Somatic/Physiological as covariate |

These axes are explicitly **NOT** diagnostic categories. The Mood axis is not a measure of a mood disorder. The Thought axis is not a measure of thought disorder. The Cognitive axis is not a measure of cognitive impairment. They are dimensional windows into normal variation, anchored to each person's own baseline.

### 2.3 Sub-Dimensions

Each axis has sub-dimensions that provide finer resolution and enable targeted interpretation. Sub-dimensions are scored on the same continuous, baseline-relative scale as the parent axis.

**Mood axis sub-dimensions:**

| Sub-dimension | Description | Sensor grounding | EQ dimension (OBA/ICF) | RDoC construct | HiTOP node |
|---|---|---|---|---|---|
| `mood.valence` | Affective polarity: low to high hedonic tone | Voice valence, self-report mood, PHQ-9 trajectory | ICF b1522 (range of emotion) | Positive Valence Systems / Reward Responsiveness | Internalizing / Distress |
| `mood.activation` | Energy and arousal level | HRV, voice arousal, sleep quality, activity level, social rhythm | ICF b1300 (energy level) + b147 (psychomotor) | Arousal and Regulatory Systems | Internalizing / Distress |
| `mood.irritability` | Reactivity and emotional threshold | Voice distress signal, response latency, app-switch rate proxy | ICF b1521 (regulation of emotion) | Negative Valence / Frustrative Nonreward | Internalizing / Distress / Anxiousness |
| `mood.anhedonia_signal` | Engagement and interest level | Social contact index, activity, vocal affect index | ICF b1301 (motivation) + b1522 | Positive Valence / Reward Responsiveness | Detachment / Social Anhedonia |

**Thought axis sub-dimensions:**

| Sub-dimension | Description | Sensor grounding | EQ dimension (OBA/ICF) | RDoC construct | HiTOP node |
|---|---|---|---|---|---|
| `thought.rate` | Speed of verbal-ideational processing; slowed vs. racing | Speech rate, response latency, vocal affect index | ICF b1600 (pace of thought) + b1671 (expression of language) | Cognitive Systems / Language | Language/Communication |
| `thought.organization` | Coherence and linearity of expressed thought | Pause index, disfluency counts (from SessionVocalProfile) | ICF b1601 (form of thought) + b1671 | Cognitive Systems / Language | Language/Communication |
| `thought.pressure` | Urgency and compulsion in speech production | Speech rate + filled pause composite, app-switch rate | ICF b1600 + b1671 (pace + output urgency, compound) | Cognitive Systems / Language | Thought Disorder / Disorganization |

**Cognitive axis sub-dimensions:**

| Sub-dimension | Description | Sensor grounding | EQ dimension (OBA/ICF) | RDoC construct | HiTOP node |
|---|---|---|---|---|---|
| `cognitive.attention` | Attentional stability and focus capacity | Attentional fragmentation index, ASRS score, app-switch rate, screen-unlock rate | ICF b140 (attention functions) | Cognitive Systems / Attention | Disinhibited Externalizing / Attentional Dysregulation |
| `cognitive.working_memory` | Short-term information-holding capacity | BRIEF-A score, vocal cognitive load estimate, response latency | ICF b144 (memory) + b1640 (abstraction/WM sub) | Cognitive Systems / Working Memory | Cognitive Control |
| `cognitive.processing_speed` | Speed of information processing | Voice response latency, speech rate deviation, PHQ-9 item 6 (psychomotor proxy) | ICF b147 (psychomotor functions) | Cognitive Systems | Cognitive Control |
| `cognitive.executive` | Planning, initiation, and inhibition capacity | BRIEF-A, WFIRS, circadian stability, sleep architecture quality | ICF b164 (higher-level cognitive: b1641 planning, b1643 flexibility, b1644 insight, b1645 judgment) | Cognitive Systems / Cognitive Control | Cognitive Control |

### 2.4 EQ Dimension Grounding: Sub-Dimension to Registry Reconciliation

The 11 Yar sub-dimensions are a focused subset of the 63-axis Cytognosis neurobehavioral registry (§2.5), selected for sensor coverage in the current Yar sensor stack. The table below reconciles the Yar `yar.axis.*` IDs to the registry.

| Yar sub-dimension ID | Registry canonical axis(es) | Registry category | Registry factor grouping |
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

**ID-management rule**: `yar.axis.*` IDs are the Yar-internal identifiers. The `eq_dimension_id` field (§3.3) holds the OBA/ICF CURIE as the canonical bearer reference. An optional `registry_axes` list field in `NeurobehavioralSubDimension` may enumerate the corresponding registry axis names for documentation.

### 2.5 Canonical Axis Vocabulary and Registry

The authoritative Cytognosis neurobehavioral axis vocabulary is the 63-axis unified registry at:

```
Documents/drafts/Science/psych/archive/neuro_onto/task5_unified_axes.csv
```

RDoC harmonization cross-references are at:

```
Documents/drafts/Science/psych/RDoC_harmonization/
```

The ontology crosswalk columns in the registry are: `Canonical_Axis`, `Category`, `RDoC_Behaviors`, `Test_Axes`, `HP` (HPO CURIE), `MFOEM`, `MF`, `CogAt` (Cognitive Atlas), `NBO`, `SYMP`, `SNOMED`. The dimension-direction model (Part 3) adds: `OBA` (dimension bearer), `PATO` (quality/direction), `ICF_b_code`, and `SNOMED_Interprets` / `SNOMED_HasInterpretation` for the clinical bridge.

**The three Yar axes and 11 sub-dimensions are a focused subset of this registry. Future sub-dimensions should be drawn from the registry before new dimensions are coined.**

The 63 canonical axes, grouped by category:

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

**Behavioral (7 axes)**:
22. Impulse Control/Inhibition
23. Psychomotor Activity
24. Motor Control/Coordination
25. Habit/Automaticity
26. Avoidance/Withdrawal
27. Approach/Reward Seeking
28. Speech/Communication

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

The 13 higher-level factor groupings (from `task6_behavioral_factors.csv`) and their mapping to Yar's three axes:

| Factor | Maps primarily to |
|---|---|
| 1. Negative Affect | Mood |
| 2. Positive Affect/Reward | Mood |
| 3. Cognitive Control | Cognitive |
| 4. Memory/Learning | Cognitive |
| 5. Social/Interpersonal | Mood (anhedonia) |
| 6. Language/Communication | Thought |
| 7. Perceptual/Sensory | (out of scope, current sensor stack) |
| 8. Somatic/Physiological | Cognitive (covariate) |
| 9. Sleep/Arousal/Circadian | Mood (activation covariate) |
| 10. Psychosis/Reality Testing | Thought (at non-clinical levels) |
| 11. Trauma/PTSD | (out of scope, current sensor stack) |
| 12. Substance/Disinhibition | (out of scope, current sensor stack) |
| 13. Personality/Trait | (research track) |

### 2.6 Deviation Typology: 8-Type Vocabulary

Every axis score (the z-score scalar) carries an implicit direction facet. A positive z-score = excess or hyperfunction on that dimension; a negative z-score = deficit or hypofunction. The 8-type typology adds semantic precision for crisis detection thresholds (§9.4), trend interpretation (§5.4), and the `direction_facet_type` field (§3.4).

| # | Type | Definition | Psychiatric exemplars | PATO anchor | SNOMED qualifier |
|---|---|---|---|---|---|
| 1 | **deficit / hypofunction** | Level below personal baseline range | Anhedonia, avolition, blunted affect, hypoarousal, cognitive slowing, social withdrawal | PATO:0000911 (decreased amount/rate) | 1250004 Decreased |
| 2 | **excess / hyperfunction** | Level above personal baseline range | Elevated mood, pressured speech, hyperactivity, hypersomnia, hyperarousal | PATO:0001563 (increased amount/rate) | 35105006 Increased |
| 3 | **absence / loss** | Complete loss (limit of deficit) | Mutism, akinesia, total avolition | PATO:0000462 absent | 2667000 Absent |
| 4 | **distortion / qualitative aberration** | Function runs but yields qualitatively altered output | Delusional content, perceptual distortion, thought derailment | PATO:0000460 abnormal (qualitative) | 263654008 Abnormal |
| 5 | **release / false generation** | Output generated with no normal input (Jacksonian positive) | Hallucinations, intrusive thoughts, flashbacks, compulsive urges | PATO:0000467 present (context-inappropriate) | 52101004 Present |
| 6 | **dysregulation / lability** | Abnormal variability rather than a fixed shift | Affective lability, mood instability, impulsivity | PATO:0001303 fluctuating | 25153009 Labile |
| 7 | **mistiming / dyssynchrony** | Temporal or phase disturbance | Delayed sleep phase, circadian misalignment, diurnal mood variation | PATO delayed/early/abnormal-duration qualities | Temporal-context qualifiers |
| 8 | **context_decoupling / inappropriateness** | Normal-magnitude function mismatched to context | Incongruent affect, fear without threat, situational vs. free-floating anxiety | PATO:0000460 abnormal (relational) | 263654008 Abnormal + finding-context |
| — | **neutral** | Score within [-0.5, +0.5] stable range | At baseline | — | — |

**Sensor-inferability notes:**

- Types 1-3 (**magnitude family**): the axis z-score sign directly encodes these. Negative z-score stable = type 1 or 3; positive z-score stable = type 2.
- Types 4-5 (**quality family**, i.e., classic "positive symptoms"): not directly inferrable from current passive sensors alone. Sustained excess on Thought/Perception sub-dimensions is a signal; reserved for clinical-track integration.
- Types 6-8 (**dynamics family**): invisible to a single cross-sectional score but detectable longitudinally. Type 6 = high `std(axis_scores[-7:])` (maps to `trend = "variable"`). Type 7 = circadian disruption via `yar.social.circadian_anchor_hour` and `yar.repro.phase_covariate`. Type 8 requires external stressor context annotation; outside current sensor scope.

The deviation typology grounds this model in Hughlings Jackson's (1884) positive/negative distinction, carried into psychiatry by Crow's Type I/II (1980) and operationalized by Andreasen's SAPS/SANS.

### 2.7 Baseline-Relative Interpretation

All axis and sub-dimension scores are expressed relative to the user's own rolling baseline. A score of 0.0 means "at your typical level." A score of +1.0 means "one standard deviation above your baseline." A score of -2.0 means "two standard deviations below your baseline." Raw sensor values are never surfaced as user-facing scores.

User-visible language never uses "above normal" or "below normal." It uses "higher than your usual," "lower than your usual," or "in your typical range." This is not a policy preference; it is a technical requirement that must be enforced at every output layer.

**Baseline establishment**: a minimum of 14 days of valid daily observations are required before baseline-relative scoring is active. During onboarding, all axis scores carry `quality_flag: pre_baseline`. The user sees a UI indicator that their patterns are still being learned.

---

## 3. Axis Schema: LinkML Classes

### 3.1 Class Hierarchy Overview

```
biolink:PhenotypicFeature
  └── NeurobehavioralAxisDefinition      (§3.2) — static registry entry
        └── NeurobehavioralSubDimension  (§3.3) — sub-dimension definition

sosa:Observation
  └── CSPObservation                     (SPEC-CSP §4.1)
        └── AxisScoreObservation         (§3.4) — per-axis computed score
              └── SubDimensionScoreObs   (§3.5) — per-sub-dimension score

crdt:OpLog                               (SPEC-storage-engine.md)
  └── AxisTrackRecord                    (§6.2) — longitudinal track entry
```

All classes inherit from the Cytos sensing-schema base classes (`04-Engineering/cytos/sensing-schema/`) and align with SOSA/SSN where applicable. `NeurobehavioralAxisDefinition` extends `biolink:PhenotypicFeature` because all three axes are behavioral phenotypes with biological grounding.

### 3.2 NeurobehavioralAxisDefinition

This class defines an entry in the axis registry. It is a static configuration artifact, not an observation. Each axis has exactly one `NeurobehavioralAxisDefinition`.

```yaml
# LinkML (normative field names)
classes:
  NeurobehavioralAxisDefinition:
    is_a: biolink:PhenotypicFeature
    description: >-
      Defines one of Yar's three canonical neurobehavioral tracking axes.
      A dimensional, continuous behavioral phenotype anchored to the user's
      personal baseline. Never a diagnostic category.
      Mood, Thought, and Cognitive are high-level groupings over EQ
      sub-dimensions, not the axis bearers themselves.
    class_uri: yar_axes:NeurobehavioralAxisDefinition
    attributes:
      axis_id:
        range: string
        required: true
        identifier: true
        description: >-
          Canonical axis identifier. Namespace: yar.axis.*
          Reserved: yar.axis.mood | yar.axis.thought | yar.axis.cognitive
      axis_label:
        range: string
        required: true
        description: User-visible axis name. No diagnostic terminology.
      biolink_class:
        range: string
        equals_string: "biolink:PhenotypicFeature"
      sub_dimensions:
        range: NeurobehavioralSubDimension
        multivalued: true
        required: true
      score_range_min:
        range: float
        equals_number: -4.0          # z-score floor; values beyond cap here
      score_range_max:
        range: float
        equals_number: 4.0           # z-score ceiling
      baseline_window_days:
        range: integer
        equals_number: 30            # rolling 30-day baseline
      baseline_min_days:
        range: integer
        equals_number: 14            # minimum before baseline scoring activates
      crisis_feed:
        range: boolean
        description: >-
          True if sustained adverse movement on this axis feeds MODULE-crisis-detection.md.
          All three axes set this to true.
      privacy_tier:
        range: PrivacyTierEnum
        description: >-
          Axis scores are boundary_derived by default. Clinician-gated
          if a BAA integration is active and the user has consented.
      factor_groupings:
        range: string
        multivalued: true
        description: >-
          Higher-level factor groupings from the 13-factor registry
          (task6_behavioral_factors.csv) that this axis groups over.
          E.g., ["Negative Affect", "Positive Affect/Reward"] for mood.
```

### 3.3 NeurobehavioralSubDimension

```yaml
classes:
  NeurobehavioralSubDimension:
    is_a: biolink:PhenotypicFeature
    description: >-
      A finer-resolution EQ dimension within a neurobehavioral axis grouping.
      Each sub-dimension is a sign-free neurobehavioral bearer (dimension facet)
      whose deviation from the user's baseline is tracked continuously.
      Scored on the same z-score scale as the parent axis.
    class_uri: yar_axes:NeurobehavioralSubDimension
    attributes:
      subdim_id:
        range: string
        required: true
        identifier: true
        description: "e.g. yar.axis.mood.valence"
      parent_axis_id:
        range: string
        required: true
        description: "e.g. yar.axis.mood"
      subdim_label:
        range: string
        required: true
      eq_dimension_id:
        range: string
        description: >-
          OBA identifier (preferred) or ICF b-code for the sign-free bearer
          dimension this sub-dimension tracks. E.g., "OBA:VB0003199" or "b1522".
          Source: PSYCH_AXES_SYNTHESIS.md §3.1 and the dimension-direction
          model (Part 3) at Documents/drafts/Science/psych/
          neurobehavioral-dimension-direction-model.md.
      pato_quality_id:
        range: string
        description: >-
          PATO quality class for the deviation type most commonly observed on
          this sub-dimension. One of the 8-type typology in §2.6.
          E.g., "PATO:0000911" (decreased amount, for deficit-type sub-dimensions).
      registry_axes:
        range: string
        multivalued: true
        description: >-
          Corresponding canonical axis names from the 63-axis registry
          (task5_unified_axes.csv). For documentation and cross-referencing.
      primary_sensor_axes:
        range: AxisRef              # from SPEC-CSP §4.2
        multivalued: true
        description: >-
          Sensor axes that are primary inputs to this sub-dimension score.
          These populate the DIMENSION facet (the continuous scalar value
          on the bearer dimension) via z-score normalization.
      supporting_sensor_axes:
        range: AxisRef
        multivalued: true
        description: >-
          Sensor axes that support but do not drive this sub-dimension.
          Also populate the dimension facet at lower weight.
      covariate_axes:
        range: AxisRef
        multivalued: true
        description: >-
          Sensor axes that condition interpretation of this sub-dimension
          but are not direct inputs to the score (e.g. menstrual phase).
          These annotate the deviation facet's interpretation context.
      aggregation_method:
        range: AggregationMethodEnum
        description: >-
          How primary sensor inputs are fused. weighted_mean is default.
          # AggregationMethodEnum: weighted_mean | max | min | rule_based
      minimum_inputs_required:
        range: integer
        description: >-
          Minimum number of primary sensor axes that must have valid
          recent observations for this sub-dimension to be scored.
          If fewer are available, the sub-dimension is set to null.
```

### 3.4 AxisScoreObservation

The primary output of this spec. One `AxisScoreObservation` is written to the op-log per axis per scoring cycle (daily by default).

```yaml
classes:
  AxisScoreObservation:
    is_a: CSPObservation
    description: >-
      Computed score for one of the three neurobehavioral axes.
      A derived health inference — the most sensitive output Yar produces.
      Always expressed relative to the user's personal baseline (z-score).
      Never surfaced as a diagnostic value.
    class_uri: yar_axes:AxisScoreObservation
    attributes:
      axis_id:
        range: string
        required: true            # yar.axis.mood | yar.axis.thought | yar.axis.cognitive
      score:
        range: float
        required: true
        description: >-
          Z-score relative to the user's rolling 30-day baseline.
          Range capped at [-4.0, 4.0]. Positive = above user's typical level;
          negative = below user's typical level.
      score_confidence:
        range: ConfidenceEnum
        required: true
        # low | medium | high
        description: >-
          Confidence in the score given the number of contributing
          sensor modalities and observation quality.
      sub_dimension_scores:
        range: SubDimensionScoreObs
        multivalued: true
        description: Per-sub-dimension breakdown scores.
      contributing_sensor_axes:
        range: AxisRef
        multivalued: true
        description: List of sensor axes that contributed to this score.
      missing_modalities:
        range: string
        multivalued: true
        description: Sensor axes expected but not available in this cycle.
      cycle_window_start:
        range: datetime
        required: true
      cycle_window_end:
        range: datetime
        required: true
      covariate_context:
        range: AxisCovariateContext
        description: Contextual covariate values at scoring time.
      trend:
        range: TrendEnum
        description: >-
          Direction of change relative to the prior 7-day window.
          # TrendEnum: improving | stable | declining | variable | insufficient_data
      trend_magnitude:
        range: float
        description: Magnitude of change in z-score units over the trend window.
      direction_facet_type:
        range: DeviationTypeEnum
        description: >-
          Semantically typed deviation direction for this score cycle.
          Derived from score sign and trend (see Appendix A for derivation rules).
          # DeviationTypeEnum values: deficit | excess | absence | distortion |
          #   release | dysregulation | mistiming | context_decoupling | neutral
          # deficit = score < -0.5 AND trend stable/declining AND std(7d) <= 1.5
          # excess  = score > +0.5 AND trend stable/improving AND std(7d) <= 1.5
          # absence = score < -3.0 AND trend = declining (limit of deficit)
          # dysregulation = std(axis_scores[-7:]) > 1.5 (trend = variable)
          # mistiming = circadian_anchor_hour deviation > 1.5h (via covariate_context)
          # neutral = score in [-0.5, +0.5]
          # distortion, release, context_decoupling: not inferrable from current
          #   sensors alone; reserved for clinical-track integration.
      # Inherits: observation_id, adapter_id, axis_ref, timestamp, result,
      #   provenance, consent_ref, privacy_tier, unit, quality_flags from CSPObservation
      # result.scalar carries the primary score value
      # privacy_tier: boundary_derived (default); clinician_gated under BAA

  DeviationTypeEnum:
    description: >-
      8-type deviation typology for the direction facet of axis score observations.
      Maps to PATO quality classes and SNOMED qualifier values per §2.6.
      Source: PSYCH_AXES_SYNTHESIS.md §4 and the dimension-direction model
      (Part 3) §4.
    permissible_values:
      deficit:
        description: Level below personal baseline range. PATO:0000911.
      excess:
        description: Level above personal baseline range. PATO:0001563.
      absence:
        description: Complete loss (limit of deficit). PATO:0000462.
      distortion:
        description: >-
          Qualitative aberration; function runs but yields altered output.
          PATO:0000460 (abnormal, qualitative). Not inferrable from current sensors.
      release:
        description: >-
          False generation; output without normal input (Jacksonian positive).
          PATO:0000467. Not inferrable from current sensors.
      dysregulation:
        description: >-
          Abnormal variability rather than fixed shift. PATO:0001303 (fluctuating).
          Detected via std(7d) > 1.5.
      mistiming:
        description: >-
          Temporal/phase disturbance. PATO delayed/early/abnormal-duration qualities.
          Detected via circadian_anchor_hour deviation > 1.5h.
      context_decoupling:
        description: >-
          Normal-magnitude function mismatched to context. Requires external
          stressor annotation; not inferrable from current sensors.
      neutral:
        description: Score within [-0.5, +0.5] stable range; at baseline.

  AxisCovariateContext:
    description: >-
      Contextual covariate values that condition axis score interpretation.
      These are not inputs to the score computation; they are annotations
      that help interpret the deviation facet in context.
    class_uri: yar_axes:AxisCovariateContext
    attributes:
      cycle_phase:
        range: CyclePhaseEnum       # from SPEC-sensor-menstrual §4.5; null if unknown/not consented
        description: >-
          Menstrual cycle phase at scoring time (optional covariate).
          Available only under reproductive_cycle.phase_covariate consent.
          Luteal phase shifts the normative midpoint for mood activation,
          executive function, working memory, and irritability threshold.
      social_rhythm_score:
        range: float                # yar.social.social_rhythm_score value at scoring time
      social_rhythm_deviation:
        range: float                # yar.social.social_rhythm_deviation value
      sleep_efficiency:
        range: float                # yar.physio.sleep_efficiency from most recent sleep session
      hrv_rmssd_zscore:
        range: float                # HRV relative to user baseline

  SubDimensionScoreObs:
    is_a: sosa:Observation
    description: Per-sub-dimension score component of an AxisScoreObservation.
    class_uri: yar_axes:SubDimensionScoreObs
    attributes:
      subdim_id:
        range: string
        required: true
      score:
        range: float               # z-score, same scale as parent axis
      confidence:
        range: ConfidenceEnum
      contributing_axes:
        range: AxisRef
        multivalued: true
      quality_flags:
        range: QualityFlagEnum
        multivalued: true
```

### 3.5 Canonical Axis Registry

The canonical registry entries are normative. All three axes are registered at system initialization. No axis in this namespace may be redefined by user-defined axes (the `yar.axis.*` prefix is reserved, per SPEC-CSP §7.3).

```yaml
# cytos/schemas/domains/neurobehavioral/axis_registry.yaml (normative)

axes:
  - axis_id: yar.axis.mood
    axis_label: "Mood and Energy"
    biolink_class: biolink:PhenotypicFeature
    privacy_tier: boundary_derived
    crisis_feed: true
    score_range_min: -4.0
    score_range_max: 4.0
    baseline_window_days: 30
    baseline_min_days: 14
    factor_groupings: ["Negative Affect", "Positive Affect/Reward", "Sleep/Arousal/Circadian"]
    sub_dimensions:
      - yar.axis.mood.valence
      - yar.axis.mood.activation
      - yar.axis.mood.irritability
      - yar.axis.mood.anhedonia_signal

  - axis_id: yar.axis.thought
    axis_label: "Thought Patterns"
    biolink_class: biolink:PhenotypicFeature
    privacy_tier: boundary_derived
    crisis_feed: true
    score_range_min: -4.0
    score_range_max: 4.0
    baseline_window_days: 30
    baseline_min_days: 14
    factor_groupings: ["Language/Communication", "Psychosis/Reality Testing"]
    sub_dimensions:
      - yar.axis.thought.rate
      - yar.axis.thought.organization
      - yar.axis.thought.pressure

  - axis_id: yar.axis.cognitive
    axis_label: "Cognitive Capacity"
    biolink_class: biolink:PhenotypicFeature
    privacy_tier: boundary_derived
    crisis_feed: true
    score_range_min: -4.0
    score_range_max: 4.0
    baseline_window_days: 30
    baseline_min_days: 14
    factor_groupings: ["Cognitive Control", "Memory/Learning", "Somatic/Physiological"]
    sub_dimensions:
      - yar.axis.cognitive.attention
      - yar.axis.cognitive.working_memory
      - yar.axis.cognitive.processing_speed
      - yar.axis.cognitive.executive
```

---

## 4. Sensor-to-Axis Mapping

### 4.1 Axis-ID Collision Resolution

A collision exists between two sensor specs that write to semantically overlapping axes:

| Collision | Source spec | axis_id used | Resolution |
|---|---|---|---|
| Daily call duration | SPEC-sensor-physiological (§3.4) | `yar.aware.call_duration_daily` | **Superseded** by SPEC-sensor-social-interaction |
| Daily call duration | SPEC-sensor-social-interaction (§5) | `yar.social.call_duration_total_daily` | **Canonical**: use `yar.social.call_duration_total_daily` |

The resolution: `yar.aware.call_duration_daily` (from SPEC-sensor-physiological) is a provisional axis ID that was registered before the social-interaction spec existed. Once `org.cytognosis.yar.social_interaction` is active, it produces `yar.social.call_duration_total_daily` as the authoritative daily call duration metric. `yar.aware.call_duration_daily` remains in the registry for backward compatibility but is marked `deprecated: true` and should not be used in new axis mappings. Both coexist in the op-log with distinct `adapter_id` provenance; the neurobehavioral-axes scoring layer reads only `yar.social.call_duration_total_daily` for axis computation.

**Action for sensor-physiological spec v0.2**: mark `yar.aware.call_duration_daily` as `deprecated: true` in the axis registry and add a migration note directing consumers to `yar.social.call_duration_total_daily`.

### 4.2 Sensor-to-Axis Mapping Table

**Role definitions:**
- **Primary**: this sensor axis is a direct, weighted input to the target axis or sub-dimension score. It populates the **dimension facet** (the continuous scalar bearing) via z-score normalization.
- **Supporting**: contributes at a lower weight; increases confidence but does not drive the score. Also populates the dimension facet.
- **Covariate**: annotates the **deviation facet interpretation context**; does not enter the score computation. Conditions how the direction type is interpreted (e.g., menstrual phase shifts the normative midpoint, affecting which deviation type a given score maps to).

On-device change-detection populates the **direction facet** (`direction_facet_type`) via the derivation rules in Appendix A, using the score value and trend computed from all contributing sensors. No individual sensor directly emits a direction type; the direction facet is always derived from the aggregated score.

| Sensor axis_id | Source spec | Target axis / sub-dimension | Role | Rationale |
|---|---|---|---|---|
| `yar.voice.valence` | speech-mentalstate | `yar.axis.mood.valence` | **Primary** | Acoustic affective polarity is the highest-signal per-session mood indicator |
| `yar.instrument.phq9_score` | physiological (instrument) | `yar.axis.mood.valence` | **Primary** | Validated, weekly-resolution depression severity |
| `yar.physio.hrv_rmssd` | physiological (Oura/Fitbit) | `yar.axis.mood.activation` | **Primary** | Autonomic regulation directly modulates emotional activation (ICF b4301 adjacent) |
| `yar.voice.arousal` | speech-mentalstate | `yar.axis.mood.activation` | **Primary** | Vocal activation is a real-time energy readout (MFOEM arousal dimension) |
| `yar.physio.sleep_efficiency` | physiological | `yar.axis.mood.activation` | **Primary** | Sleep continuity (ICF b1342) is a primary predictor of next-day energy and mood |
| `yar.physio.sleep_deep_duration` | physiological | `yar.axis.mood.activation` | **Supporting** | Deep sleep (ICF b1340 sub) specifically modulates emotional regulation |
| `yar.physio.step_count` | physiological | `yar.axis.mood.activation` | **Supporting** | Physical activity / psychomotor activity (ICF b147); low activity is a depression signal |
| `yar.social.social_rhythm_score` | social-interaction | `yar.axis.mood.activation` | **Supporting** | Social rhythm regularity (ICF d750 + SRM theory); type 7 mistiming is most meaningful direction |
| `yar.social.social_contact_index` | social-interaction | `yar.axis.mood.anhedonia_signal` | **Primary** | Affiliative motivation (ICF d750, RDoC Social Processes); type 1 deficit = withdrawal |
| `yar.voice.vocal_affect_index` | speech-mentalstate | `yar.axis.mood.anhedonia_signal` | **Primary** | Prosodic expressiveness (ICF b1522); type 1 deficit = blunted prosody |
| `yar.physio.readiness_score` | physiological (Oura) | `yar.axis.mood.activation` | **Supporting** | Composite recovery integrates sleep, HRV, temperature into energy estimate |
| `yar.physio.skin_temp_deviation` | physiological | `yar.axis.mood.activation` | **Supporting** | Thermoregulation covariate; type 7 mistiming for circadian temperature rhythm |
| `yar.instrument.gad7_score` | physiological (instrument) | `yar.axis.mood.irritability` | **Primary** | Anxiety severity indexes emotional reactivity threshold (ICF b1521) |
| `yar.voice.distress_signal` | speech-mentalstate | `yar.axis.mood.irritability` | **Primary** | Vocal distress composite (ICF b1521); type 6 dysregulation or type 8 context-decoupling; feeds crisis detection independently |
| `yar.aware.app_switch_rate` | physiological (AWARE) | `yar.axis.mood.irritability` | **Supporting** | Elevated app switching as proxy for restlessness and reactivity |
| `yar.social.social_withdrawal_flag` | social-interaction | `yar.axis.mood.anhedonia_signal` | **Primary** | Type 1 deficit (binary threshold); complements continuous social contact index |
| `yar.repro.phase_covariate` | menstrual | `yar.axis.mood` (whole axis) | **Covariate** | Luteal phase shifts normative midpoint; conditions deviation facet interpretation |
| `yar.social.social_rhythm_deviation` | social-interaction | `yar.axis.mood` (whole axis) | **Covariate** | Social rhythm deviation contextualizes mood; type 7 mistiming annotation |
| `yar.voice.speech_rate` | speech-mentalstate | `yar.axis.thought.rate` | **Primary** | Articulation rate deviation from baseline (ICF b1671); type 1 deficit = slowed, type 2 excess = pressured |
| `yar.voice.arousal` | speech-mentalstate | `yar.axis.thought.rate` | **Supporting** | High arousal co-occurs with elevated thought rate |
| `yar.voice.pause_index` | speech-mentalstate | `yar.axis.thought.organization` | **Primary** | Fragmented pauses index disorganized thought (ICF b1601 + b1671); type 4/6 |
| `yar.voice.energy_in_voice` | speech-mentalstate | `yar.axis.thought.rate` | **Supporting** | Low vocal energy co-occurs with slowed thought patterns |
| `yar.voice.cognitive_load` | speech-mentalstate | `yar.axis.thought.organization` | **Supporting** | High cognitive load (ICF b164 + b144) degrades organizational fluency |
| `yar.voice.vocal_affect_index` | speech-mentalstate | `yar.axis.thought.pressure` | **Supporting** | Reduced prosodic range accompanies pressured speech |
| `yar.aware.app_switch_rate` | physiological (AWARE) | `yar.axis.thought.pressure` | **Supporting** | Rapid attention shifts correlate with pressured ideation |
| `yar.aware.screen_unlock_rate` | physiological (AWARE) | `yar.axis.thought.pressure` | **Supporting** | Compulsive device checking as a thought-pressure behavioral readout |
| `yar.instrument.asrs_parta_score` | physiological (instrument) | `yar.axis.cognitive.attention` | **Primary** | ASRS is the validated attention-difficulty screen in this population (ICF b140) |
| `yar.aware.screen_unlock_rate` | physiological (AWARE) | `yar.axis.cognitive.attention` | **Primary** | Attentional fragmentation proxy via passive sensing |
| `yar.aware.app_switch_rate` | physiological (AWARE) | `yar.axis.cognitive.attention` | **Primary** | App-switching rate is the most direct passive behavioral attention signal (ICF b140) |
| `yar.voice.cognitive_load` | speech-mentalstate | `yar.axis.cognitive.attention` | **Supporting** | Cognitive load estimate from speech; corroborates attentional burden |
| `yar.aware.notification_rate` | physiological (AWARE) | `yar.axis.cognitive.attention` | **Supporting** | High notification rate fragments attention; also causally upstream |
| `yar.instrument.psqi_global` | physiological (instrument) | `yar.axis.cognitive.attention` | **Supporting** | Poor sleep quality degrades next-day attention; weekly cadence |
| `yar.instrument.briefa` | physiological (instrument) | `yar.axis.cognitive.working_memory` | **Primary** | BRIEF-A subscale directly indexes working memory (ICF b144 + b1640) |
| `yar.voice.cognitive_load` | speech-mentalstate | `yar.axis.cognitive.working_memory` | **Primary** | High cognitive load in speech production is a working-memory readout |
| `yar.physio.sleep_rem_duration` | physiological | `yar.axis.cognitive.working_memory` | **Supporting** | REM sleep (ICF b1344) is critical for memory consolidation |
| `yar.physio.hrv_rmssd` | physiological | `yar.axis.cognitive.executive` | **Supporting** | Vagal tone correlates with prefrontal executive function readiness |
| `yar.instrument.wfirs` | physiological (instrument) | `yar.axis.cognitive.executive` | **Primary** | WFIRS measures functional impairment linked to executive deficits (ICF b164) |
| `yar.physio.readiness_score` | physiological (Oura) | `yar.axis.cognitive.executive` | **Supporting** | Readiness is a composite of recovery metrics that predict cognitive capacity |
| `yar.aware.location_entropy` | physiological (AWARE) | `yar.axis.cognitive.executive` | **Supporting** | Low location entropy (rigid routine) or high entropy (disorganized) both signal executive strain |
| `yar.physio.spo2` | physiological | `yar.axis.cognitive.processing_speed` | **Supporting** | Low SpO2 during sleep impairs next-day processing speed (ICF b4402) |
| `yar.physio.hrv_rmssd` | physiological | `yar.axis.cognitive.processing_speed` | **Supporting** | Autonomic regulation correlates with cognitive processing speed |
| `yar.social.circadian_anchor_hour` | social-interaction (SocialRhythmMetricObs) | `yar.axis.cognitive.executive` | **Covariate** | Social circadian anchor (ICF b134, RDoC Arousal/Circadian); type 7 mistiming when anchor shifts |
| `yar.repro.phase_covariate` | menstrual | `yar.axis.cognitive` (whole axis) | **Covariate** | Luteal-phase dopamine depletion reduces executive function and working memory; conditions deviation facet |
| `yar.physio.sleep_efficiency` | physiological | `yar.axis.cognitive.processing_speed` | **Primary** | Sleep efficiency (ICF b1342) is the strongest daily predictor of processing speed |

### 4.3 Notes on Sensor Coverage

- **Speech sensor is Research maturity**: `yar.voice.*` axes carry `quality_flag: research_maturity` until the speech-mentalstate adapter advances to Beta. The axis model must handle their absence gracefully (see §5.5).
- **Social-interaction sensor is Research maturity**: same handling applies to `yar.social.*` axes.
- **Instrument scores are periodic**: PHQ-9, GAD-7, ASRS, BRIEF-A, and WFIRS are weekly or bi-weekly observations. The scoring layer must carry instrument scores forward for up to 14 days before flagging `quality_flag: stale_instrument_score`.
- **Menstrual phase covariate is opt-in**: `yar.repro.phase_covariate` requires `reproductive_cycle.phase_covariate` consent. Its absence does not degrade axis scores; it merely reduces covariate annotation richness. When present, it conditions the deviation facet interpretation (luteal phase shifts the normative midpoint for several sub-dimensions).

---

## 5. Score Computation

### 5.1 Overview

Score computation runs on-device, daily, in a background task after sensor inputs for the scoring cycle are available. The computation pipeline is stateless per invocation: it reads from the op-log, computes, and writes a new `AxisScoreObservation`. It does not modify prior observations.

```
[Op-log query: sensor axes for scoring window]
          |
[Baseline lookup: user's 30-day rolling stats per sensor axis]
          |
[Per-sensor normalization: (observed - baseline_mean) / baseline_std]
          |             ← populates DIMENSION facet for each contributing sensor
[Sub-dimension aggregation: weighted mean of normalized primary inputs]
          |
[Axis aggregation: weighted mean of sub-dimension scores]
          |
[Confidence estimation: based on available modalities]
          |
[Trend computation: compare to prior 7-day mean]
          |
[Direction facet derivation: score + trend -> DeviationTypeEnum]
          |             ← populates DIRECTION facet (see Appendix A)
[Covariate context assembly: cycle phase, social rhythm, sleep]
          |
[AxisScoreObservation: write to op-log → Cytoplex PEP boundary check]
```

### 5.2 Baseline and Normalization

**Per-sensor normalization**: each contributing sensor axis value is normalized to a z-score relative to that sensor's 30-day rolling statistics stored for this user.

```
sensor_zscore = (observed_value - user_30d_mean) / user_30d_std
```

If `user_30d_std < 0.01` (near-zero variance, e.g., sensor stuck at a constant value), the normalization substitutes population-level standard deviation from the sensor spec's reference distribution. This situation is flagged with `quality_flag: low_sensor_variance`.

**Sub-dimension aggregation**: a weighted mean of normalized primary sensor inputs.

```
subdim_score = weighted_mean(
    [sensor_zscore_i * weight_i for sensor_i in primary_inputs
     if sensor_i is available in scoring window]
)
```

Default weights are uniform within a sub-dimension (equal weighting of all primary inputs). Weights are configurable at the adapter-config level and are stored as CRDT-versioned configuration records.

**Axis aggregation**: a simple mean of sub-dimension scores with all sub-dimensions weighted equally by default.

```
axis_score = mean([subdim_score_j for subdim_j in sub_dimensions
                   if subdim_j is scoreable])
```

If fewer than `minimum_scoreable_subdims` sub-dimensions are scoreable, the axis score is null (not imputed) and carries `quality_flag: insufficient_sub_dimensions`.

### 5.3 Confidence Estimation

Confidence is determined by the number and quality of contributing sensor modalities.

| Confidence level | Condition |
|---|---|
| `high` | Three or more primary sensor axes contributed; no `pre_baseline` or `stale_instrument_score` flags |
| `medium` | Two primary sensor axes contributed, or three or more with a stale instrument flag |
| `low` | Only one primary sensor axis contributed; or baseline is not yet established (`pre_baseline`) |
| `insufficient` | Fewer than `minimum_inputs_required` primary axes available; score is null |

Confidence is surfaced to users as a visual indicator on the axis card, not as a numeric value. The user-visible vocabulary is "high confidence," "some data gaps today," and "limited data today." Never numerical confidence scores in user-facing UI.

### 5.4 Trend Detection

Trend is computed by comparing the current score to the rolling 7-day mean of prior axis scores.

```
trend_magnitude = axis_score - rolling_7d_mean(axis_score)

trend = "declining"   if trend_magnitude < -0.5
trend = "stable"      if -0.5 <= trend_magnitude <= 0.5
trend = "improving"   if trend_magnitude > 0.5
trend = "variable"    if std(axis_scores[-7:]) > 1.5
trend = "insufficient_data" if fewer than 5 valid scores in past 7 days
```

The `TrendEnum` values map to deviation types: `declining` = type-1 (deficit) movement; `variable` = type-6 (dysregulation); `improving` = type-2 (excess) or return toward neutral. See Appendix A for the full derivation rules.

Trend direction labels ("improving" vs. "declining") are used only in the internal representation. User-facing presentation never uses "declining" as a label. Instead, the Brain Weather visualization conveys change through metaphorical visual transitions. Written summaries use "lower than your recent pattern" and "higher than your recent pattern."

### 5.5 Missing-Modality Handling

No single sensor is required. The system must degrade gracefully as sensors become unavailable.

| Scenario | Behavior |
|---|---|
| Voice sensor offline | `yar.voice.*` axes excluded; sub-dimensions relying primarily on voice receive lower confidence; axis score computed from remaining inputs |
| Wearable disconnected | `yar.physio.*` axes excluded; mood activation and cognitive axis lose primary HRV input; quality flag set |
| All instruments overdue (> 14 days) | Instrument axes excluded; `quality_flag: stale_instrument_score` added |
| Social-interaction adapter not connected | `yar.social.*` axes excluded; mood anhedonia signal loses primary input |
| Menstrual covariate absent | `AxisCovariateContext.cycle_phase = null`; covariate column absent from axis score annotation; deviation facet interpretation proceeds without phase conditioning |
| Fewer than `minimum_inputs_required` for a sub-dimension | Sub-dimension score is `null`; not imputed |
| Fewer than 2 non-null sub-dimension scores for an axis | Axis score is `null` for that cycle; not imputed |

The scoring cycle never imputes or interpolates missing axis scores. Nulls propagate. The CRDT op-log captures the null as a valid observation with `quality_flags` explaining why.

### 5.6 Optional Genomic Priors

Optional genomic priors may inform per-person axis baselines (specified separately under controlled access; out of scope for this spec). Where such priors are available and the user has consented, they adjust the initial baseline prior before observational data accumulates. The adjustment mechanism and prior specification are documented separately. This spec makes no assumptions about the existence or structure of such priors.

---

## 6. Longitudinal State: CRDT Op-Log Model

### 6.1 Principles

Axis scores are longitudinal time-series data. Their value lies not in any single observation but in the track they form over weeks and months. The CRDT op-log (Layer 2 per SPEC-storage-engine.md) is the source of truth for this track.

Key invariants:
- Every axis score is an `append` operation on the op-log. Scores are never updated in place.
- Prior axis scores are never modified by re-computation. A new scoring cycle always writes a new observation.
- Baseline statistics (30-day mean and std per sensor axis) are themselves stored as CRDT records, updated daily by the baseline-update pass.
- The graph index (Layer 4) may be rebuilt from the op-log at any time; it is derived, not authoritative.

### 6.2 Axis Track Record

An `AxisTrackRecord` is a daily op-log entry produced by the scoring pipeline for each of the three axes.

```yaml
# Normative CRDT op-log entry for a daily Mood axis score
op_id: "crdt:op/axis-mood-20260622"
op_type: append
vector_clock: {...}            # Loro/any-sync CRDT vector clock
payload_type: AxisScoreObservation
payload:
  observation_id: "axis-mood-20260622"
  adapter_id: "org.cytognosis.yar.neurobehavioral_axes.v0"
  axis_ref:
    axis_id: yar.axis.mood
    axis_label: "Mood and Energy"
    domain: neurobehavioral
    value_type: continuous
    range_min: -4.0
    range_max: 4.0
    biolink_class: biolink:PhenotypicFeature
  timestamp: "2026-06-22T23:59:00Z"     # end of scoring cycle
  result:
    scalar: -0.8                         # 0.8 std below user's 30d baseline
  cycle_window_start: "2026-06-22T00:00:00Z"
  cycle_window_end:   "2026-06-22T23:59:59Z"
  score: -0.8
  score_confidence: medium
  trend: stable
  trend_magnitude: -0.2
  direction_facet_type: deficit          # score < -0.5, trend stable, std(7d) <= 1.5
  contributing_sensor_axes:
    - yar.voice.valence
    - yar.physio.hrv_rmssd
    - yar.physio.sleep_efficiency
    - yar.social.social_contact_index
  missing_modalities:
    - yar.instrument.phq9_score          # overdue; last scored 5 days ago
  covariate_context:
    cycle_phase: luteal
    social_rhythm_score: 4.1
    social_rhythm_deviation: -0.6
    sleep_efficiency: 0.78
    hrv_rmssd_zscore: -0.4
  sub_dimension_scores:
    - subdim_id: yar.axis.mood.valence
      score: -1.1
      confidence: high
      contributing_axes: [yar.voice.valence]
    - subdim_id: yar.axis.mood.activation
      score: -0.7
      confidence: medium
      contributing_axes: [yar.physio.hrv_rmssd, yar.physio.sleep_efficiency]
    - subdim_id: yar.axis.mood.anhedonia_signal
      score: -0.6
      confidence: medium
      contributing_axes: [yar.social.social_contact_index, yar.voice.vocal_affect_index]
    - subdim_id: yar.axis.mood.irritability
      score: null                        # voice distress not available this cycle
      confidence: insufficient
      contributing_axes: []
  provenance:
    source_device: "iPhone:A15-Bionic"
    model_version: "neurobehavioral_axes_scorer-v0.1"
    collection_method: inferred
    raw_data_location: null
  consent_ref: "consent:grant/axis.mood/abc"
  privacy_tier: boundary_derived
  quality_flags:
    - stale_instrument_score              # PHQ-9 overdue
```

### 6.3 Baseline State Record

Baseline statistics are stored as a separate CRDT record type, updated daily.

```yaml
# Normative CRDT baseline state record (updated daily)
record_type: AxisBaselineState
record_id: "baseline-state-yar.physio.hrv_rmssd-20260622"
op_type: lww_register                    # last-write-wins; one per sensor axis per user
payload:
  sensor_axis_id: yar.physio.hrv_rmssd
  window_start: "2026-05-23T00:00:00Z"   # rolling 30-day
  window_end:   "2026-06-22T23:59:59Z"
  observation_count: 28                  # days with valid observations
  mean: 44.7                             # ms
  std: 8.2
  min: 28.3
  max: 61.4
  last_updated: "2026-06-22T23:59:00Z"
  baseline_sufficient: true              # >= 14 days of data
```

### 6.4 CRDT Semantics

| Record type | CRDT semantic | Rationale |
|---|---|---|
| `AxisScoreObservation` | `append` (immutable) | Daily scores are historical facts; never overwrite |
| `AxisBaselineState` | `lww_register` (last-write-wins) keyed on `(sensor_axis_id, date)` | Daily baseline update supersedes the prior day's record |
| `SubDimensionScoreObs` | Embedded in parent `AxisScoreObservation`; inherits `append` | Sub-dimension scores are components of the daily score |
| Axis configuration (weights, window sizes) | `lww_register` keyed on `(axis_id, config_key)` | User preference changes supersede prior settings |

**Multi-device behavior**: axis scoring runs on the primary device (the device that holds the most recent sensor data). On secondary devices, the op-log receives replicated axis scores via SPEC-sync-protocol.md. If scoring runs on two devices in the same cycle (e.g., during a sync gap), both observations are appended and tagged with their source device. The graph query layer surfaces the observation with the higher confidence score for that cycle window.

### 6.5 Example: 7-Day Mood Track Query

```python
# Pseudocode: retrieve 7-day Mood axis track from op-log
mood_track = op_log.query(
    payload_type = "AxisScoreObservation",
    filters = {
        "axis_id": "yar.axis.mood",
        "timestamp": {"gte": seven_days_ago, "lte": now},
    },
    order_by = "timestamp",
    limit = 7
)
# Returns list of AxisScoreObservation records, one per day
# Each record contains score, confidence, trend, direction_facet_type,
# sub_dimension_scores, covariate_context
```

---

## 7. Privacy and Governance

### 7.1 Axis Scores as Derived Health Inferences

Axis scores are the most sensitive data Yar produces. A raw HRV measurement is a physiological observation. An axis score that synthesizes HRV, voice valence, sleep quality, and social rhythm into a single "Mood" trajectory is a derived health inference with diagnostic adjacency. It must be treated accordingly.

**Classification**: all three axis scores are classified as `CrossBoundarySignal` per `privacy-boundary-spec.md` Section 3. Default privacy tier: `boundary_derived`. Under active BAA and clinician-gated consent: `clinician_gated`.

### 7.2 CrossBoundarySignal Declarations

```yaml
# CrossBoundarySignal declarations for neurobehavioral axis scores (normative)
cross_boundary_signals:

  - signal_id: yar.axis.mood.daily_score
    source_axis: yar.axis.mood
    aggregation: daily_score
    data_type: float
    range: [-4.0, 4.0]
    consent_scope_required: axis.mood.read
    pep_policy_ref: cap/policies/neurobehavioral_axes_v0.rego
    crisis_feed: true

  - signal_id: yar.axis.thought.daily_score
    source_axis: yar.axis.thought
    aggregation: daily_score
    data_type: float
    range: [-4.0, 4.0]
    consent_scope_required: axis.thought.read
    pep_policy_ref: cap/policies/neurobehavioral_axes_v0.rego
    crisis_feed: true

  - signal_id: yar.axis.cognitive.daily_score
    source_axis: yar.axis.cognitive
    aggregation: daily_score
    data_type: float
    range: [-4.0, 4.0]
    consent_scope_required: axis.cognitive.read
    pep_policy_ref: cap/policies/neurobehavioral_axes_v0.rego
    crisis_feed: true

  - signal_id: yar.axis.mood.subdim_scores
    source_axis: yar.axis.mood
    aggregation: sub_dimension_breakdown
    data_type: object
    consent_scope_required: axis.mood.subdim.read
    pep_policy_ref: cap/policies/neurobehavioral_axes_v0.rego
    clinician_gated: true       # sub-dimension breakdown requires clinician consent

  - signal_id: yar.axis.thought.subdim_scores
    source_axis: yar.axis.thought
    aggregation: sub_dimension_breakdown
    data_type: object
    consent_scope_required: axis.thought.subdim.read
    pep_policy_ref: cap/policies/neurobehavioral_axes_v0.rego
    clinician_gated: true

  - signal_id: yar.axis.cognitive.subdim_scores
    source_axis: yar.axis.cognitive
    aggregation: sub_dimension_breakdown
    data_type: object
    consent_scope_required: axis.cognitive.subdim.read
    pep_policy_ref: cap/policies/neurobehavioral_axes_v0.rego
    clinician_gated: true
```

**Rule**: sub-dimension scores (e.g., `yar.axis.mood.irritability`) are `clinician_gated` because they carry higher diagnostic specificity than the composite axis score. The composite daily score is `boundary_derived` under standard user consent.

### 7.3 On-Device-First Default

Axis scores are computed on-device and stored on-device by default. The user must explicitly consent to each of the three `axis.*.read` scopes to allow axis scores to participate in cross-boundary features (e.g., Yar's cloud-assisted supervisor model, if that feature is enabled).

**Default at install:** all three axis consent scopes are `off`. The user must opt in.

**Upgrade flow**: same as established in SPEC-sensor-physiological §5.2. User navigates to axis settings, Cytoplex PEP issues a `Directive`, user confirms, `GuardDecision` is `allow_with_constraints`, `DecisionRecord` written to audit log.

### 7.4 Link to Crisis Detection

When any axis score crosses a **sustained adverse movement threshold**, the scoring engine emits a crisis-detection signal to `MODULE-crisis-detection.md`. The crisis detection module applies its own logic and escalation criteria; this spec only produces the signal.

**Threshold for crisis signal**: `axis_score < -2.5` for two or more consecutive days, on any axis. The crisis detection module combines this with voice distress signals, self-report safety flags, and other context before escalating. The `direction_facet_type` value at the time of the threshold crossing (e.g., `deficit` vs. `dysregulation`) is passed to the crisis module as supplementary context for distinguishing sustained deficit from lability-driven dips.

**The axis scorer does not make escalation decisions.** It produces signals; the crisis detection module acts.

### 7.5 Consent Scope Controlled Vocabulary

New consent scopes defined by this spec:

| Scope name | Covers | Privacy tier |
|---|---|---|
| `axis.mood.read` | Daily Mood axis composite score | `boundary_derived` |
| `axis.thought.read` | Daily Thought axis composite score | `boundary_derived` |
| `axis.cognitive.read` | Daily Cognitive axis composite score | `boundary_derived` |
| `axis.mood.subdim.read` | Mood sub-dimension scores | `clinician_gated` |
| `axis.thought.subdim.read` | Thought sub-dimension scores | `clinician_gated` |
| `axis.cognitive.subdim.read` | Cognitive sub-dimension scores | `clinician_gated` |

---

## 8. Affirming Language Policy

Axis scores are the most consequential output Yar surfaces to users. The affirming language policy is more stringent here than in individual sensor specs.

**Required for all user-facing axis outputs:**

- Never describe an axis score as "normal" or "abnormal."
- Never describe an axis score using a diagnostic label (e.g., "depressive episode," "hypomanic," "attention deficit").
- Axis names in user-facing contexts: "Mood and Energy," "Thought Patterns," "Cognitive Capacity." Never "Mood Disorder Axis," "Thought Disorder Index," or any diagnostic-adjacent name.
- Scores below the user's baseline are described as "lower than your usual" or "below your recent pattern." Not "impaired," "declined," or "deficient."
- Scores above the user's baseline are described as "higher than your usual" or "above your recent pattern." Not "elevated" as a clinical euphemism.
- Trend direction: "your [axis] has been a bit lower than usual this week" vs. "your [axis] is declining."
- The Brain Weather metaphor is the primary user-facing representation. Axis scores feed the weather model; they are not surfaced as numeric z-scores.
- Sub-dimension scores are never shown to users in the standard interface. They are available only in a "detailed view" for users who explicitly request it, and only with affirming framing.
- The `direction_facet_type` field is an internal engineering field. It must never be surfaced directly to users in any form.

---

## 9. Conformance and Acceptance Criteria

### 9.1 Axis Schema

- **[SHALL-AX-001]** The system shall maintain exactly three `NeurobehavioralAxisDefinition` records in the axis registry with IDs `yar.axis.mood`, `yar.axis.thought`, and `yar.axis.cognitive`. These records are immutable at runtime; changes require a schema version update.
- **[SHALL-AX-002]** The system shall reject any user-defined axis registration using the `yar.axis.*` prefix. User-defined axes must use the `user.*` prefix per SPEC-CSP §7.3.
- **[SHALL-AX-003]** All `AxisScoreObservation` records shall carry a `consent_ref` matching an active consent grant for the corresponding `axis.*.read` scope.
- **[SHALL-AX-004]** All `NeurobehavioralSubDimension` records in the axis registry shall carry an `eq_dimension_id` referencing an OBA CURIE or ICF b-code. Sub-dimensions without an `eq_dimension_id` are not valid registry entries.

### 9.2 Score Computation

- **[SHALL-SC-001]** The system shall not impute axis scores for cycles where fewer than `minimum_inputs_required` primary sensor axes have valid observations. Null scores shall be written with `quality_flags` explaining the insufficiency.
- **[SHALL-SC-002]** The system shall complete the daily scoring cycle and write `AxisScoreObservation` records to the op-log within one hour of the end of the scoring window (default: midnight local time).
- **[SHALL-SC-003]** Before the baseline is established (fewer than 14 days of valid observations), the system shall write all axis scores with `quality_flag: pre_baseline` and shall not surface z-scores to the user as baseline-relative scores.
- **[SHALL-SC-004]** The system shall carry instrument scores forward for up to 14 days after the last valid observation, applying `quality_flag: stale_instrument_score` on each cycle that uses a carried-forward value.
- **[SHALL-SC-005]** The system shall not use population-level norms in place of personal-baseline z-scores after the baseline is established. Population norms apply only during pre-baseline onboarding.
- **[SHALL-SC-006]** The system shall derive `direction_facet_type` from the aggregated score and trend using the rules in Appendix A. It shall not set `direction_facet_type` to `distortion`, `release`, or `context_decoupling` based on sensor data alone.

### 9.3 CRDT Op-Log

- **[SHALL-CRDT-001]** All `AxisScoreObservation` records shall be written as `append` operations on the CRDT op-log. No update or delete operations are permitted on axis score records.
- **[SHALL-CRDT-002]** Baseline state records (`AxisBaselineState`) shall be written as `lww_register` operations keyed on `(sensor_axis_id, date)`.
- **[SHALL-CRDT-003]** In a multi-device scenario where two devices score the same axis on the same cycle, both observations shall be retained in the op-log with distinct `source_device` provenance. The query layer shall surface the higher-confidence observation.

### 9.4 Privacy

- **[SHALL-PV-001]** The system shall not transmit any `AxisScoreObservation` across the privacy boundary without an active `axis.*.read` consent grant.
- **[SHALL-PV-002]** Sub-dimension scores shall be classified as `clinician_gated` and shall not cross the boundary under standard `axis.*.read` consent. A separate `axis.*.subdim.read` consent scope is required.
- **[SHALL-PV-003]** When an axis score triggers the crisis detection signal (score < -2.5 for two or more consecutive days), the system shall route the signal to `MODULE-crisis-detection.md` before writing the `AxisScoreObservation` to the op-log.
- **[SHALL-PV-004]** Axis scores shall never carry any raw sensor signal value in their payload. They carry z-scores relative to user baselines only.
- **[SHALL-PV-005]** The `AxisCovariateContext.cycle_phase` field shall be populated only when `reproductive_cycle.phase_covariate` consent is active. When absent, the field shall be `null`. The null must not trigger any inference about the user's reproductive status.

### 9.5 Affirming Language

- **[SHALL-LANG-001]** No user-visible label, notification, axis card, or trend description shall use the words "normal," "abnormal," "impaired," "deficient," "pathological," or any clinical diagnosis name.
- **[SHALL-LANG-002]** Numeric z-scores shall not be surfaced in the standard user interface. The Brain Weather metaphor is the canonical user-facing representation.
- **[SHALL-LANG-003]** The user-visible axis labels shall be "Mood and Energy," "Thought Patterns," and "Cognitive Capacity." No other labels are permissible in production user-facing surfaces.
- **[SHALL-LANG-004]** The `direction_facet_type` enum value shall not appear in any user-facing string, label, notification, or log entry visible to the user.

---

## 10. Open Questions

| # | Question | Current leaning | Blocker |
|---|---|---|---|
| O-1 | **Cross-adapter aggregation semantics (CSP O-8):** when multiple adapters write to the same sensor axis (e.g., `yar.physio.hrv_rmssd` from both Oura and Fitbit), which value does the axis scorer use? | Most recent value with highest provenance quality; tag both with `adapter_id`; aggregation = maximum-recency | Define a formal `cross_adapter_merge_policy` field in `AxisBaselineState`; assign to sensor-physiological v0.2 |
| O-2 | **Uniform vs. learned sub-dimension weights:** are equal weights for sub-dimension aggregation adequate, or should weights be learned from longitudinal user data? | Uniform for v0.1 (interpretability and auditability); learned model in v1 if validation data supports it | Requires labeled pilot dataset; IRB pathway (North Star); not before Beta |
| O-3 | **Axis score discretization for user-facing Brain Weather:** how many discrete weather states are needed (continuous vs. 5-class vs. 7-class)? | 5 discrete weather states mapping to z-score bands: clear / partly cloudy / overcast / stormy / unknown | UX design decision; product spec (SPEC-personas-voice.md) must coordinate |
| O-4 | **Trend window length:** 7 days was chosen for sensitivity; longer windows reduce noise but delay detection of state changes. | 7-day for daily Mood/Thought/Cognitive; 14-day for slower-moving Cognitive sub-dimensions | Pilot study; assign to research track |
| O-5 | **Scoring cadence:** daily scoring is the default. Should high-frequency (per-session) axis scores be supported for research use? | Daily for user-facing; per-session for research track when explicitly enabled | Storage implications; assign to SPEC-storage-engine.md for partition design |
| O-6 | **Weekday/weekend stratification for social rhythm covariate:** should `social_rhythm_score` be stratified by weekday vs. weekend before entering the Mood axis covariate context? | Yes, stratification is theoretically justified (SRM theory); add weekday_srm and weekend_srm separately | Algorithm design; coordinate with SPEC-sensor-social-interaction Open item O-3 |
| O-7 | **Axis score sharing with clinicians:** what is the minimum sub-dimension and time-window granularity needed for a clinician integration to be clinically useful? | 7-day trend per sub-dimension + raw daily scores for 90 days; define in clinician-integration spec | Clinician integration spec (not yet drafted); legal and BAA pathway |
| O-8 | **PMDD-aware Mood axis scoring:** should the luteal-phase covariate produce a separate "cycle-adjusted Mood" score in addition to the standard score? | Potentially high value for ADHD/PMDD users; add as an opt-in "cycle-adjusted view" once menstrual phase data has >= 90 days of validation | SPEC-sensor-menstrual O-6; requires pilot data; deferred to v0.2 |
| O-9 | **Crisis detection threshold:** the provisional threshold (score < -2.5 for 2+ consecutive days) is conservative. Calibration against validated clinical outcomes is needed. Should `direction_facet_type` (e.g., `dysregulation` vs. `deficit`) modulate the threshold? | Keep conservative for v0.1; add direction-type-aware threshold variant in Beta; recalibrate using self-report and instrument co-validation | IRB; North Star pilot |
| O-10 | **Axis-ID collision `yar.aware.call_duration_daily` deprecation timeline:** SPEC-sensor-physiological needs a patch to mark this axis deprecated. | Apply in sensor-physiological v0.2; deprecation does not break existing op-log records | Assign to spec maintenance batch |
| O-11 | **`eq_dimension_id` CURIE sourcing:** OBA coverage of neurobehavioral attributes is currently incomplete. For sub-dimensions without an OBA CURIE, should Cytognosis mint provisional CURIEs (EQ-defined, OBA-style) or use ICF b-codes as the canonical bearer? | Use ICF b-code as canonical bearer when OBA CURIE is absent; mint Cytognosis provisional OBA-style CURIEs as OBA coverage grows; track in the 63-axis registry CSV | Assign to ontology curation task; coordinate with cytomem knowledge graph |
| O-12 | **Direction-facet population for types 4, 5, 8 (distortion, release, context-decoupling):** these types are not inferrable from current passive sensors. Should the crisis-detection module be the only consumer authorized to infer them, via instrument items? | Reserve for future clinical-track integration; instrument items (e.g., PANSS-like items in research track) may populate these types under IRB; do not infer from passive sensing alone | Clinical-track spec; IRB pathway |

---

## 11. References

### Internal

| Document | Relationship |
|---|---|
| `Yar/spec/SPEC-CSP.md` | Parent protocol; all CSP types, lifecycle, privacy tiers, and axis registry primitives |
| `Yar/spec/SPEC-sensor-physiological.md` | Source of `yar.physio.*`, `yar.aware.*`, `yar.instrument.*` axes consumed here |
| `Yar/spec/SPEC-sensor-speech-mentalstate.md` | Source of `yar.voice.*` axes consumed here |
| `Yar/spec/SPEC-sensor-social-interaction.md` | Source of `yar.social.*` axes consumed here; social rhythm as covariate |
| `Yar/spec/SPEC-sensor-menstrual.md` | Source of `yar.repro.phase_covariate`; menstrual phase as contextual covariate |
| `Yar/spec/SPEC-storage-engine.md` | CRDT op-log (L2); graph index (L4); op-log entry format and retention |
| `Yar/spec/SPEC-sync-protocol.md` | L2 CRDT replication; multi-device axis track sync |
| `Cytoplex/spec/03_primitives.md` | Cytoplex primitive types: `Directive`, `GuardDecision`, `DecisionRecord` |
| `Cytoplex/spec/privacy-boundary-spec.md` | `CrossBoundarySignal` classification; PB-1 through PB-10 |
| `Cytoplex/spec/06_conformance.md` | `CrossBoundarySignal` conformance requirements |
| `MODULE-crisis-detection.md` | Consumer of axis score crisis signals; governs escalation |
| `04-Engineering/yar/research/adhd-paper-synthesis.md` | ADHD symptom dimensions; Brain Weather Dashboard; mood-adaptive interface requirements |
| `04-Engineering/cytos/sensing-schema/sensor-architecture.md` | Cytos sensor base classes and `SensorDescriptor` |
| `04-Engineering/cytos/sensing-schema/unified-sensor-report.md` | Cytos LinkML schema tree; SOSA/SSN alignment; vendor profiles |
| `Yar/consolidation_2026-06-21/_research/PSYCH_AXES_SYNTHESIS.md` | Formal EQ model adoption, 63-axis registry, 8-type deviation typology, sensor-to-EQ mapping |
| `Documents/drafts/Science/psych/neurobehavioral-dimension-direction-model.md` | Keystone: Part 3 dimension-direction model; PATO/OBA/SNOMED source assessment; full deviation typology |
| `Documents/drafts/Science/psych/cdisc-qrs-feature-space-design.md` | Part 2: six-layer ontology stack; ICF/MF/RDoC/HiTOP/PROMIS layer definitions |
| `Documents/drafts/Science/psych/cdisc-qrs-comprehensive-reference.md` | Part 1: instrument catalogue, LOINC codes, crosswalks |
| `Documents/drafts/Science/psych/archive/neuro_onto/task5_unified_axes.csv` | 63-axis canonical registry; ontology crosswalk columns |
| `Documents/drafts/Science/psych/archive/neuro_onto/task6_behavioral_factors.csv` | 13 higher-level factor groupings |
| `Documents/drafts/Science/psych/RDoC_harmonization/` | 922 RDoC associations × 6 units; `reference_behavior.csv` = full EQ decomposition |

### External

1. **Insel TR et al.** (2010). Research Domain Criteria (RDoC): Toward a new classification framework for research on mental disorders. *American Journal of Psychiatry*, 167(7), 748-751. https://doi.org/10.1176/appi.ajp.2010.09091379 [Dimensional psychiatry basis for the three-axis model.]

2. **Cuthbert BN, Insel TR** (2013). Toward the future of psychiatric diagnosis: the seven pillars of RDoC. *BMC Medicine*, 11, 126. https://doi.org/10.1186/1741-7015-11-126 [RDoC rationale for dimensional behavioral phenotyping.]

3. **Allsopp K et al.** (2019). Heterogeneity in psychiatric diagnostic classification. *Psychiatry Research*, 279, 15-22. https://doi.org/10.1016/j.psychres.2019.07.005 [Evidence against categorical diagnostic boundaries in behavior.]

4. **Robberecht G et al.** (2026). Menstrual Cycle-Related Hormonal Fluctuations in ADHD. *Journal of Clinical Medicine*, 15(1), 121. https://pmc.ncbi.nlm.nih.gov/articles/PMC12786913/ [ADHD + menstrual phase interaction; luteal dopamine depletion.]

5. **Monk TH et al.** (1991). The Social Rhythm Metric. *Journal of Nervous and Mental Disease*, 179(2), 98-103. [Social rhythm as mood covariate; SRM basis.]

6. **Grandin LD et al.** (2006). The social zeitgeber theory, circadian rhythms, and mood disorders. *Clinical Psychology Review*, 26(6), 679-694. https://doi.org/10.1016/j.cpr.2006.07.001 [Social rhythm as mood activation covariate.]

7. **Chen J, Meng Y, Nie K** (2026). Not Just Me and My To-Do List: Understanding Challenges of Task Management for Adults with ADHD and the Need for AI-Augmented Social Scaffolds. arXiv:2603.17258v2. [ADHD dimensional challenge framework; Brain Weather as affirming interface.]

8. **Canzian L, Musolesi M** (JAMIA 2016). Automatic detection of social rhythms in bipolar disorder. *J Am Med Inform Assoc*, 23(3), 538-543. https://academic.oup.com/jamia/article/23/3/538/2909018 [Passive SRM sensing for mood state classification.]

9. **Onnela JP, Rauch SL** (2016). Harnessing Smartphone-Based Digital Phenotyping to Enhance Behavioral and Mental Health. *Neuropsychopharmacology*, 41, 1691-1696. https://doi.org/10.1038/npp.2016.7 [Digital phenotyping as longitudinal behavioral tracking.]

10. **Jacobson NC, Bhattacharya S** (2024). Digital phenotyping for monitoring mental disorders: Systematic review. PMC10753422. https://pmc.ncbi.nlm.nih.gov/articles/PMC10753422/ [Systematic review of passive sensing for behavioral axis tracking.]

11. **Cytognosis Foundation** (2026-05-26). Separating Phenotype from Direction of Change: A Dimension-Deviation Model for the Cytognosis Neurobehavioral Feature Space (Part 3). Internal working document. [Formal basis for the EQ axis model in this spec; PATO/OBA/SNOMED source assessment; 8-type deviation typology.]

12. **Cytognosis Foundation** (2026-05-13). Cytognosis Neurobehavioral Phenotype Feature Space: Design Reference (Part 2). Internal working document. [Six-layer ontology stack; ICF/MF/RDoC/HiTOP/PROMIS layer definitions.]

13. **Cytognosis Foundation** (2026-05-13). CDISC QRS Comprehensive Reference (Part 1). Internal working document. [Instrument catalogue, LOINC codes, crosswalks.]

14. **Mungall CJ et al.** (2017). The Monarch Initiative: an integrative data and analytic platform connecting phenotypes to genotypes across species. *Nucleic Acids Research*, 45(D1), D712-D722. [UPHENO EQ unification basis; same pattern used in this spec's dimension-direction decomposition.]

15. **Kotov R et al.** (2017). The Hierarchical Taxonomy of Psychopathology (HiTOP). *Journal of Abnormal Psychology*, 126(4), 454-477. [HiTOP 6-level hierarchy; DSM bridge referenced in sub-dimension crosswalk; 13-factor groupings in §2.5.]

16. **Geneviève LD et al.** PATO: The Phenotype and Trait Ontology. http://purl.obolibrary.org/obo/pato.owl (CC BY). [Deviation quality vocabulary; anchors for the 8-type typology in §2.6.]

17. **OBA: Ontology of Biological Attributes.** http://purl.obolibrary.org/obo/oba.owl (CC BY). [Sign-free dimension bearer vocabulary; primary source for `eq_dimension_id` field.]

---

## Appendix A: Deviation-Type to Score-State Derivation Rules

The `direction_facet_type` field on `AxisScoreObservation` is derived computationally from the aggregated score, trend, and covariate context. These rules are normative for v0.1.

| `direction_facet_type` | Derivation rule | Notes |
|---|---|---|
| `deficit` | `score < -0.5` AND `trend in [stable, declining]` AND `std(7d) <= 1.5` | Most common; maps to magnitude-family negative direction |
| `excess` | `score > +0.5` AND `trend in [stable, improving]` AND `std(7d) <= 1.5` | Magnitude-family positive direction |
| `absence` | `score < -3.0` AND `trend = declining` | Limit of deficit; triggers crisis-detection signal regardless of day count |
| `dysregulation` | `std(axis_scores[-7:]) > 1.5` (regardless of mean score) | Dynamics family; maps to current `trend = "variable"` |
| `mistiming` | `circadian_anchor_hour deviation > 1.5h` (via `covariate_context.circadian_anchor_hour`) | Dynamics family; detected via social-circadian anchor shift |
| `neutral` | `score in [-0.5, +0.5]` AND `std(7d) <= 1.5` | At baseline; no meaningful deviation |
| `distortion` | Not derivable from current sensors alone | Reserved; requires clinical-track instrument items under IRB |
| `release` | Not derivable from current sensors alone | Reserved; requires clinical-track instrument items under IRB |
| `context_decoupling` | Not derivable from current sensors alone | Reserved; requires external stressor annotation |

**Precedence**: when multiple rules could apply, `absence` takes precedence over `deficit`; `dysregulation` takes precedence over `deficit` or `excess` when `std(7d) > 1.5`; `mistiming` may co-occur with other types and is stored as a secondary annotation in `covariate_context` rather than overwriting the primary `direction_facet_type`.

**Open question O-12**: whether the crisis detection module may assign `distortion`, `release`, or `context_decoupling` from instrument items is deferred pending clinical-track spec.
