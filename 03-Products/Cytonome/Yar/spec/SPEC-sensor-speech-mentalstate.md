---
spec_id: SPEC-sensor-speech-mentalstate
version: "0.1"
status: draft
domain: sensor-speech-mentalstate
owner: Shahin Mohammadi
created: 2026-06-22
last_updated: 2026-06-22
depends_on: [SPEC-CSP, SPEC-storage-engine]
implements: [CSP]
---

# SPEC-sensor-speech-mentalstate: Speech Mental-State Sensor

> **Reading options:** An ADHD-friendly progressive-disclosure rendering is generated from this file. The hand-maintained ADHD twin (`spec/adhd/SPEC-sensor-speech-mentalstate_adhd.md`) was retired 2026-07-16; see `_archive/cleanup_2026-07-16/adhd-twins/`.

> **Status**: Draft
> **Date**: 2026-06-22
> **Author**: Cytognosis Foundation
> **Audience**: engineers
> **Tags**: `yar`, `cytonome`, `csp`, `sensor`, `speech`, `mental-state`, `paralinguistic`
> **Related**: [SPEC-CSP](./SPEC-CSP.md); privacy boundary at `Cytoplex/spec/privacy-boundary-spec.md`; crisis detection at `./MODULE-crisis-detection.md`

---

## Implementation Status

**Partially implemented (v0.1 backend).** The core data models are live in `Yar/src/yar/models/voice_affect.py`: `VoiceAffectConstants`, `VoiceAffectSignal`, `VoiceAffectPolicy`, `VoiceAffectEvent`, and related types are production-ready Pydantic models. The `EmotionTrackerService` and `RawAffectObservation` pipeline are implemented in `Yar/src/yar/core/affect/tracker.py`. The Flutter/Dart mobile sidecar is implemented at `Yar/apps/mobile/lib/src/affect/voice_affect_models.dart` and `onnx_distilhubert_ser_inference.dart`.

**Not yet implemented:** the full CSP adapter lifecycle (`connect()`/`disconnect()`/consent gate), the openSMILE eGeMAPSv02 extraction pipeline described in Section 4.3.1, the `SessionVocalProfile` aggregation step, CRDT op-log integration for axis observations, and the CAP PEP boundary enforcement at the CrossBoundarySignal layer. The `SensorDescriptor` LinkML class cited in Section 2.1 does not yet exist in any repo. Do not treat any section describing these flows as describing existing behavior.

**VoiceAffectPolicy** (`Yar/src/yar/models/voice_affect.py`) is the governing consent and retention model for this sensor. Its fields (`raw_audio_stored: false`, `diagnostic_use_allowed: false`, `user_facing_emotion_label_allowed: false`, `on_device_only: true`, `retention_policy: "ephemeral"`) are normative for all implementations. The backend rejects events that violate any of these constraints.

---

**Reading time**: ~14 minutes.
**If you only read one thing**: Section 3 (signal taxonomy) and Section 4 (inference pipeline). The sensor produces quantified acoustic and paralinguistic features from the user's voice. It never stores raw audio, never transmits audio off-device, and never labels users with clinical diagnoses. Every emitted signal is a CSP-conformant observation bound to a named tracking axis.

**BLUF**: The speech mental-state sensor is an on-device CSP adapter that runs alongside Yar's voice layer. It captures audio, applies voice activity detection, extracts acoustic and prosodic features using HuBERT and openSMILE eGeMAPSv02, and infers mid-level mental-state dimensions (arousal, valence, cognitive load, distress signal level). Raw audio is ephemeral and never persisted. Derived features are stored as CRDT op-log entries. Every signal that could leave the device is a declared `CrossBoundarySignal` subject to CAP PEP evaluation and active user consent.

---

## 1. Purpose and Scope

### 1.1 What This Sensor Does

The speech mental-state sensor extracts clinically relevant, quantified paralinguistic features from the user's voice during Yar sessions. It operates as a passive, background CSP adapter. It does not transcribe speech, generate responses, or control Yar's spoken output; those are the domain of the voice model adapter (see `04-Engineering/yar/research/voice_model_deep_evaluation.md` Section 5).

**Capabilities:**

- Voice activity detection (VAD) to gate feature extraction to user speech segments.
- Per-utterance prosodic and acoustic feature extraction (pitch, energy, speech rate, pause structure, jitter, shimmer, harmonic-to-noise ratio).
- Per-utterance disfluency counting (filled pauses, false starts, repetitions).
- Non-speech event detection (sighs, laughter, breathing patterns).
- Utterance-level mental-state inference: arousal, valence, cognitive load estimate, distress signal level.
- Session-level aggregation into a `SessionVocalProfile`.
- Longitudinal baseline tracking per user for personalized trend detection.
- Crisis-detection signal feed per `MODULE-crisis-detection.md`.

### 1.2 What This Sensor Does NOT Do

| Out of scope | Where it lives instead |
|---|---|
| Speech recognition / transcription | Voice model adapter (Gemma 4 cascade) |
| Yar's spoken output, TTS, or voice persona | `SPEC-personas-voice.md` (planned Batch 3) |
| Clinical diagnosis of any condition | Out of scope for all Yar sensors; user-facing output is dimensional, not diagnostic |
| Covert recording (recording without active, informed consent) | Prohibited. Consent gate enforced at `connect()` per SPEC-CSP Section 5.3 |
| Raw audio storage of any kind | Prohibited. Audio is ephemeral; only derived features are persisted |
| Raw audio transmission off-device | Prohibited. CAP PEP enforces `on_device_only` at the raw-audio boundary |
| Biometric voice identification or speaker verification | Out of scope; this sensor measures state, not identity |
| Any user-facing output using diagnostic labels | Prohibited per Section 9 and CSP Section 9 affirming-language policy |

### 1.3 Position in the Stack

This adapter is one of two independent voice-layer sensors (per `voice_model_deep_evaluation.md` Section 5). It runs in parallel with the speech/dialogue sensor and shares the same audio input from the VAD stage.

```
Audio In (microphone)
      |
   [VAD]
   /       \
[Dialogue sensor]    [Speech mental-state sensor]   <-- THIS SPEC
(transcription,       (paralinguistic features,
 ASR, TTS control)    mental-state inference)
      |                      |
[CSP adapter: voice.speech.gemma]   [CSP adapter: voice.mentalstate.v0]
      |                      |
      +----------+-----------+
                 |
          [CAP PEP boundary check]
                 |
          [CRDT op-log (L2)]
```

---

## 2. Adapter Registration

### 2.1 SensorDescriptor

```yaml
# Normative field values for this adapter's SensorDescriptor
adapter_id:       org.cytognosis.yar.voice.mentalstate.v0
display_name:     "Voice wellbeing signals"
adapter_class:    SpeechMentalState
maturity:         research
modalities:       [voice]
privacy_tier:     on_device_only          # raw audio and raw feature vectors
axes_produced:
  - yar.voice.arousal
  - yar.voice.valence
  - yar.voice.cognitive_load
  - yar.voice.distress_signal
  - yar.voice.speech_rate
  - yar.voice.pause_index
  - yar.voice.vocal_affect_index
  - yar.voice.energy_in_voice
requires_consent:
  - consent.voice.mental_state_sensing    # user must grant this scope explicitly
schema_ref:       "cytos/schemas/domains/sensor/voice/mentalstate_v0.yaml"
implementation_ref: "yar/sensors/mentalstate/"
```

### 2.2 Consent Scope

The adapter requires the scope `consent.voice.mental_state_sensing`. This scope is distinct from any consent for recording, transcription, or cloud processing. The consent UI must present:

1. What is being sensed (prosodic features, not the words).
2. Where data is stored (on-device only, under user control).
3. What derived signals may optionally cross the boundary (summary scalars only, with a second explicit consent).
4. How to revoke (adapter disconnects within one session; no residual feature data retained beyond the user's configured retention window).

### 2.3 VoiceAffect Constants: Backend vs Mobile Divergence (D2)

The `VoiceAffectConstants` class is defined in both tiers. The values differ and the divergence is currently **unresolved** — it may be intentional tier tuning or drift. Engineers implementing this spec must be aware of both sets.

Source files:
- Python backend: `Yar/src/yar/models/voice_affect.py` (`VoiceAffectConstants`)
- Flutter/Dart mobile: `Yar/apps/mobile/lib/src/affect/voice_affect_models.dart` (`VoiceAffectConstants`)

| Constant | Python backend | Dart mobile | Notes |
|---|---|---|---|
| `HOP_MS` | 250 ms | 1500 ms | 6x difference. Mobile may use a longer hop to reduce CPU and battery load; backend runs on server hardware with no such constraint. **To reconcile.** |
| `TTL_MS` | 120,000 ms (2 min) | 10,000 ms (10 sec) | 12x difference. Mobile discards affect state much faster, shrinking cross-turn context. **To reconcile.** |
| `CONFIDENCE_FLOOR` | 0.45 | 0.25 | Mobile accepts lower-confidence predictions; may reduce false negatives at cost of precision. **To reconcile.** |
| `MIN_SPEECH_MS` | 800 ms | 1000 ms | Minor; mobile requires a slightly longer utterance before processing. |
| `DEFAULT_MODEL_ID` | `distilhubert-ser-onnx` | `distilhubert-ser-int8-onnx` | Quantized INT8 variant on mobile for memory footprint. Intentional. |
| `HISTORY_FOR_TREND` | 4 observations | 3 observations | Minor; mobile uses a shorter trend window. |

**Status: to reconcile.** The `HOP_MS`, `TTL_MS`, and `CONFIDENCE_FLOOR` differences are large enough to produce meaningfully different runtime behavior between tiers. The spec cannot be normative on these constants until they are either confirmed as intentional tier tuning (with a documented rationale per tier) or corrected to shared values. Assign a reconciliation task before this adapter advances from Research to Beta maturity.

### 2.4 VoiceAffectPolicy as the Governing Consent Model

`VoiceAffectPolicy` (defined in `Yar/src/yar/models/voice_affect.py`) is the **implemented** consent and retention attestation model for this sensor. Its normative defaults are:

```python
raw_audio_stored: bool = False           # raw audio never persisted
diagnostic_use_allowed: bool = False     # no diagnostic inference permitted
user_facing_emotion_label_allowed: bool = False  # labels not surfaced to users
on_device_only: bool = True              # data stays on device
retention_policy: str = "ephemeral"     # affect state is ephemeral
```

The backend enforces these constraints today: it rejects any `VoiceAffectEvent` where `raw_audio_stored`, `diagnostic_use_allowed`, or `user_facing_emotion_label_allowed` is `True`. These are not aspirational requirements; they are enforced at the API boundary. All future implementations of this adapter's consent layer must conform to this schema, not replace it.

---

## 3. Signal Taxonomy

The taxonomy has three tiers: **raw acoustic/prosodic features** (utterance-level, always `on_device_only`), **mid-level mental-state dimensions** (utterance and session-level, `on_device_only` for raw vectors, `boundary_derived` for summary scalars under consent), and **CSP axis observations** (what is actually emitted to the data layer).

### 3.1 Raw Acoustic and Prosodic Features (Tier 1)

These features are extracted per utterance. They are intermediate computational artifacts and are not stored as CSP observations. They feed the mental-state inference layer (Section 4.3). Their privacy tier is `on_device_only`; they must not appear in any `CSPResult` field that could cross the boundary.

| Feature group | Feature | Unit | Extractor | Clinical relevance |
|---|---|---|---|---|
| **Pitch** | Pitch mean | Hz | openSMILE eGeMAPSv02 | Flat/monotone: low arousal, possible low-mood episode |
| | Pitch std dev | Hz | openSMILE | High variability: elevated arousal or anxiety |
| | Pitch range | Hz | openSMILE | Reduced range: potential cognitive fatigue |
| | F0 contour | list[float] | openSMILE | Shape of pitch curve over utterance |
| **Energy** | RMS energy mean | dB | openSMILE | Low energy: fatigue or low-mood state |
| | Energy range | dB | openSMILE | Flat energy: reduced affective expression |
| **Rate** | Speech rate | syl/sec | openSMILE | Elevated rate: high arousal or pressured speech |
| | Articulation rate | syl/sec | openSMILE | Excludes silence; separates pausing from speaking pace |
| **Pauses** | Pre-utterance pause | ms | VAD timestamp delta | Extended pause: cognitive load or processing difficulty |
| | Within-utterance pause count | count | VAD | Fragmented thought, cognitive load indicator |
| | Within-utterance pause duration | ms | VAD | Prolonged silence mid-utterance |
| | Response latency | ms | Turn-taking delta | Slow response: cognitive load; fast response: impulsivity signal |
| **Vocal quality** | Jitter | % | openSMILE | Elevated jitter: vocal tension, fatigue, or stress |
| | Shimmer | dB | openSMILE | Elevated shimmer: vocal tension |
| | HNR | dB | openSMILE | Low HNR (high noise): fatigue, laryngeal tension |
| | Spectral centroid | Hz | openSMILE | Vocal brightness proxy |
| | Formants F1-F4 | Hz | openSMILE | Articulation quality indicators |
| **Disfluency** | Filled pauses | count | ASR + post-processing | Elevated count: cognitive load in ADHD-relevant contexts |
| | False starts | count | ASR + post-processing | Executive function indicator |
| | Repetitions | count | ASR + post-processing | Working-memory or anxiety signal |
| **Non-speech** | Sigh events | count | VAD + classifier | Fatigue, frustration, emotional regulation |
| | Laughter events | count | VAD + classifier | Positive affect, engagement |
| | Breathing pattern | rate, depth | VAD + classifier | Stress, anxiety, physiological arousal |

### 3.2 Mid-Level Mental-State Dimensions (Tier 2)

These are inferred from Tier 1 features using the on-device model pipeline (Section 4.3). Each dimension maps directly to a CSP axis.

| Dimension | Description | Range | Model source | CSP axis |
|---|---|---|---|---|
| **Arousal** | Activation level: calm to activated | 0.0 to 1.0 | HuBERT SER (dimensional head) | `yar.voice.arousal` |
| **Valence** | Affective polarity: low to high | -1.0 to 1.0 | HuBERT SER (dimensional head) | `yar.voice.valence` |
| **Cognitive load estimate** | Inferred mental effort | ordinal: low, moderate, elevated, high | Rule-based fusion (filled-pause rate + response latency + speech rate deviation from baseline) | `yar.voice.cognitive_load` |
| **Distress signal level** | Composite indicator combining arousal, valence, vocal quality degradation, and non-speech events | ordinal: minimal, mild, moderate, elevated | Fusion model (Section 4.3.3) | `yar.voice.distress_signal` |
| **Speech rate** | Utterance-level articulation rate | syl/sec (float) | openSMILE direct | `yar.voice.speech_rate` |
| **Pause index** | Normalized ratio of pause time to total utterance time | 0.0 to 1.0 | Derived from VAD output | `yar.voice.pause_index` |
| **Vocal affect index** | Composite prosodic expressiveness score | 0.0 to 1.0 | Derived from pitch range, energy range, speech rate variability | `yar.voice.vocal_affect_index` |
| **Energy in voice** | Session-level mean RMS relative to user baseline | float (z-score vs baseline) | openSMILE + longitudinal baseline | `yar.voice.energy_in_voice` |

**Affirming language rule**: no dimension label exposed to users uses "normal," "abnormal," or any diagnostic-adjacent term. The user-visible representation of `distress_signal=elevated` is "your voice is showing elevated distress signals today," not any clinical label.

### 3.3 CSP Axis Definitions

Each axis produced by this adapter is registered in the CSP axis registry. The definitions below are normative `AxisRef` instances.

```yaml
# cytos/schemas/domains/sensor/voice/mentalstate_axes.yaml (normative)

axes:
  - axis_id: yar.voice.arousal
    axis_label: "Vocal arousal level"
    domain: emotional_regulation
    value_type: continuous
    range_min: 0.0
    range_max: 1.0
    unit: null
    biolink_class: biolink:PhenotypicFeature
    boundary_eligible: true          # scalar summary may cross boundary under consent

  - axis_id: yar.voice.valence
    axis_label: "Vocal affective tone"
    domain: emotional_regulation
    value_type: continuous
    range_min: -1.0
    range_max: 1.0
    unit: null
    biolink_class: biolink:PhenotypicFeature
    boundary_eligible: true

  - axis_id: yar.voice.cognitive_load
    axis_label: "Cognitive load estimate"
    domain: cognitive_state
    value_type: ordinal
    enum_values: [low, moderate, elevated, high]
    unit: null
    biolink_class: biolink:PhenotypicFeature
    boundary_eligible: true

  - axis_id: yar.voice.distress_signal
    axis_label: "Vocal distress signal"
    domain: emotional_regulation
    value_type: ordinal
    enum_values: [minimal, mild, moderate, elevated]
    unit: null
    biolink_class: biolink:PhenotypicFeature
    boundary_eligible: true
    crisis_feed: true                # signals feed MODULE-crisis-detection.md

  - axis_id: yar.voice.speech_rate
    axis_label: "Speech rate"
    domain: cognitive_state
    value_type: continuous
    range_min: 0.0
    range_max: 15.0
    unit: syl/sec
    biolink_class: null
    boundary_eligible: false         # raw rate is biometric-adjacent; summarized only

  - axis_id: yar.voice.pause_index
    axis_label: "Pause pattern index"
    domain: cognitive_state
    value_type: continuous
    range_min: 0.0
    range_max: 1.0
    unit: null
    biolink_class: null
    boundary_eligible: false

  - axis_id: yar.voice.vocal_affect_index
    axis_label: "Vocal affect expressiveness"
    domain: emotional_regulation
    value_type: continuous
    range_min: 0.0
    range_max: 1.0
    unit: null
    biolink_class: biolink:PhenotypicFeature
    boundary_eligible: true

  - axis_id: yar.voice.energy_in_voice
    axis_label: "Energy in voice"
    domain: energy_regulation
    value_type: continuous
    unit: "z-score"
    biolink_class: null
    boundary_eligible: true
```

### 3.4 LinkML Class Hierarchy

These classes extend the Cytos sensing-schema base classes (`core.yaml`) and are SOSA-aligned.

```yaml
# cytos/schemas/domains/sensor/voice/mentalstate_v0.yaml (normative)

imports:
  - ../../core/core.yaml
  - ../../../profiles/profile_sosa.yaml

prefixes:
  yar_voice: https://schema.cytognosis.org/yar/voice/
  biolink: https://w3id.org/biolink/vocab/
  sosa: http://www.w3.org/ns/sosa/
  loinc: http://loinc.org/

classes:

  SpeechMentalStateSensor:
    is_a: Sensor          # from core.yaml; SOSA-aligned
    description: >
      CSP adapter that extracts paralinguistic features from user speech
      and infers mid-level mental-state dimensions. Never stores raw audio.
    class_uri: yar_voice:SpeechMentalStateSensor

  VocalBiomarkerFrame:
    is_a: sosa:Observation
    description: >
      Per-utterance vocal biomarker record. Covers one VAD-bounded user speech
      segment (~250ms analysis window). Privacy tier: on_device_only.
      Never transmitted. Source of truth for session aggregation.
    class_uri: yar_voice:VocalBiomarkerFrame
    attributes:
      utterance_id:        { range: string, required: true, identifier: true }
      session_id:          { range: string, required: true }
      timestamp:           { range: datetime, required: true }
      # Prosodic (Tier 1 features — on_device_only)
      pitch_mean_hz:       { range: float }
      pitch_std_hz:        { range: float }
      pitch_range_hz:      { range: float }
      pitch_contour:       { range: float, multivalued: true }
      speech_rate_syl_sec: { range: float }
      articulation_rate:   { range: float }
      # Temporal
      pre_utterance_pause_ms:   { range: float }
      response_latency_ms:      { range: float }
      within_utterance_pauses:  { range: PauseEvent, multivalued: true }
      # Disfluency
      filled_pause_count:  { range: integer }
      false_start_count:   { range: integer }
      repetition_count:    { range: integer }
      # Vocal quality
      jitter_percent:      { range: float }
      shimmer_db:          { range: float }
      hnr_db:              { range: float }
      spectral_centroid_hz: { range: float }
      formant_frequencies: { range: float, multivalued: true }
      # Emotion (Tier 2 — inferred; on_device_only at utterance level)
      arousal:             { range: float }
      valence:             { range: float }
      dominance:           { range: float }
      emotion_categorical: { range: EmotionCategoricalEnum }
      emotion_confidence:  { range: float }
      # Non-speech
      non_speech_events:   { range: NonSpeechEvent, multivalued: true }

  PauseEvent:
    description: Single pause event within an utterance.
    class_uri: yar_voice:PauseEvent
    attributes:
      position_ms:  { range: float, required: true }
      duration_ms:  { range: float, required: true }
      pause_type:   { range: PauseTypeEnum, required: true }

  NonSpeechEvent:
    description: >
      A non-speech acoustic event detected within or between utterances.
      Never contains user speech content.
    class_uri: yar_voice:NonSpeechEvent
    attributes:
      timestamp_ms: { range: float, required: true }
      event_type:   { range: NonSpeechEventTypeEnum, required: true }
      duration_ms:  { range: float, required: true }
      intensity:    { range: float }   # 0.0 to 1.0

  SessionVocalProfile:
    is_a: sosa:Observation
    description: >
      Per-session aggregate derived from all VocalBiomarkerFrames in that session.
      Serves as the CRDT-persisted summary. Raw frame data is not persisted beyond
      the user's configured retention window.
    class_uri: yar_voice:SessionVocalProfile
    attributes:
      session_id:               { range: string, required: true, identifier: true }
      session_date:             { range: date, required: true }
      duration_minutes:         { range: float }
      # Prosodic aggregates
      avg_pitch_hz:             { range: float }
      pitch_variability_cv:     { range: float }   # coefficient of variation
      avg_speech_rate:          { range: float }
      speech_rate_variability:  { range: float }
      # Emotion arc
      dominant_emotion:         { range: EmotionCategoricalEnum }
      emotion_volatility:       { range: float }
      arousal_mean:             { range: float }
      arousal_trend:            { range: TrendEnum }
      valence_mean:             { range: float }
      valence_trend:            { range: TrendEnum }
      # Engagement
      avg_response_latency_ms:  { range: float }
      response_latency_trend:   { range: TrendEnum }
      avg_turn_duration_sec:    { range: float }
      turn_duration_trend:      { range: TrendEnum }
      # Cognitive load
      filled_pause_rate:        { range: float }   # per minute
      cognitive_load_estimate:  { range: CognitiveLoadEnum }
      distress_signal_level:    { range: DistressSignalEnum }
      # ND-relevant derived metrics (on_device_only)
      adhd_vocal_markers:       { range: ADHDAVocalMarkers }
      asd_vocal_markers:        { range: ASDVocalMarkers }

  ADHDAVocalMarkers:
    description: >
      ADHD-relevant vocal pattern indicators derived from session data.
      User-visible labels are dimensional and affirming, not diagnostic.
      Privacy tier: on_device_only.
    class_uri: yar_voice:ADHDAVocalMarkers
    attributes:
      speech_rate_variability_zscore:  { range: float }
      topic_coherence_score:           { range: float }   # semantic similarity across turns
      impulsive_response_count:        { range: integer } # responses < 200ms after Yar
      tangential_shift_count:          { range: integer }
      hyperfocus_episode_count:        { range: integer } # sustained engagement > 5 min
      energy_trajectory:               { range: TrendEnum }

  ASDVocalMarkers:
    description: >
      ASD-relevant vocal pattern indicators derived from session data.
      User-visible labels are dimensional and affirming, not diagnostic.
      Privacy tier: on_device_only.
    class_uri: yar_voice:ASDVocalMarkers
    attributes:
      prosodic_range_score:           { range: float }   # normalized to user baseline
      emotional_expression_range:     { range: float }
      turn_taking_regularity:         { range: float }
      social_script_adherence:        { range: float }

enums:
  EmotionCategoricalEnum:
    permissible_values:
      anger: {}
      sadness: {}
      fear: {}
      joy: {}
      neutral: {}
      surprise: {}
      disgust: {}

  PauseTypeEnum:
    permissible_values:
      silent: {}
      filled: {}
      breath: {}

  NonSpeechEventTypeEnum:
    permissible_values:
      sigh: {}
      laugh: {}
      cry: {}
      breath: {}
      cough: {}
      hmm: {}
      other: {}

  TrendEnum:
    permissible_values:
      decreasing: {}
      stable: {}
      increasing: {}
      variable: {}

  CognitiveLoadEnum:
    permissible_values:
      low: {}
      moderate: {}
      elevated: {}
      high: {}

  DistressSignalEnum:
    permissible_values:
      minimal: {}
      mild: {}
      moderate: {}
      elevated: {}
```

### 3.5 Neurobehavioral Axis Alignment

The axes produced by this adapter correspond to specific dimensions in the Cytognosis 63-axis canonical neurobehavioral registry. Source: `consolidation_2026-06-21/_research/PSYCH_AXES_SYNTHESIS.md` (Section 5.2, "Speech Mental-State Sensor").

| Adapter axis | Canonical registry axis | Registry category | EQ dimension facet (ICF/OBA) |
|---|---|---|---|
| `yar.voice.valence` | Pleasure/Positive Affect + Sadness/Depressed Mood | Emotional | Affective valence / hedonic tone (MFOEM hedonic valence); primary driver of `mood.valence` |
| `yar.voice.arousal` | Arousal/Wakefulness + Autonomic Arousal | Sleep + Somatic | Emotional arousal / affective activation (MFOEM arousal); drives `mood.activation` and supports `thought.rate` |
| `yar.voice.speech_rate` | Speech/Communication + Psychomotor Activity | Behavioral | Verbal output / speech rate (ICF b1671); primary driver of `thought.rate` |
| `yar.voice.pause_index` | Language/Verbal + Reasoning/Abstraction | Cognitive | Thought organization / verbal fluency (ICF b160 + b1671); primary driver of `thought.organization` |
| `yar.voice.cognitive_load` | Executive Function/Cognitive Control + Working Memory | Cognitive | Executive and working-memory load (ICF b164 + b144); supports `thought.organization` and `cognitive.working_memory` |
| `yar.voice.distress_signal` | Emotional Lability/Dysregulation + Distress/Stress Response | Emotional | Affective regulation threshold (ICF b1521); primary driver of `mood.irritability`; feeds crisis detection |
| `yar.voice.vocal_affect_index` | Anger/Irritability (blunted pole) + Pleasure/Positive Affect | Emotional | Prosodic expressiveness / affective range (ICF b1522); primary driver of `mood.anhedonia_signal` |
| `yar.voice.energy_in_voice` | Fatigue/Energy + Speech/Communication | Somatic + Behavioral | Vocal energy / speech amplitude (ICF b1671 sub); supports `thought.rate` |

These axes feed the higher-level Yar neurobehavioral axis scores defined in `SPEC-neurobehavioral-axes.md`. The axis IDs used here (`yar.voice.*`) are the sensor-layer identifiers; the registry canonical names are for ontology cross-referencing.

---

## 4. Inference Pipeline

### 4.1 Overview

```
Microphone
    |
  [VAD]  ← WebRTC VAD or Silero VAD; gates all downstream processing
    |
[Audio buffer: ephemeral, in-memory only]
    |
    +----> [openSMILE eGeMAPSv02] ──────────────┐
    |      (pitch, energy, rate, jitter,          |
    |       shimmer, HNR, pauses, MFCCs)          |
    |                                             |
    +----> [Non-speech classifier]                |
    |      (sigh, laugh, breath detection)        v
    |                                    [Feature fusion buffer]
    +----> [HuBERT-large SER head]  ────>         |
           (arousal, valence, dominance,           |
            emotion categorical)                  |
                                                  v
                                   [Mental-state inference layer]
                                   (cognitive load, distress signal,
                                    vocal affect index, energy z-score)
                                                  |
                                                  v
                                   [VocalBiomarkerFrame: on_device_only]
                                                  |
                                   [Session aggregation (batch, post-utterance)]
                                                  |
                                                  v
                                   [SessionVocalProfile]
                                                  |
                                   [CSP observation emit → CRDT op-log]
                                   (axes: arousal, valence, cognitive_load,
                                    distress_signal, speech_rate, pause_index,
                                    vocal_affect_index, energy_in_voice)
                                                  |
                                   [CAP PEP boundary check]
                                    (on_device_only axes: never cross)
                                    (boundary_derived axes: cross only
                                     under active consent)
                                                  |
                                   [MODULE-crisis-detection.md feed]
                                   (distress_signal axis only)
```

**Key invariant**: raw audio never exits the VAD-to-feature-extraction stage. The `audio buffer` is an in-memory ring buffer. It is overwritten after feature extraction; it is never flushed to disk, logged, or referenced in any CSP observation.

### 4.2 Voice Activity Detection

**Model**: WebRTC VAD (primary, lowest latency), with Silero VAD as the higher-accuracy option for research-tier deployments.

**Behavior:**
- VAD segments the audio stream into speech segments and silence/non-speech intervals.
- Each speech segment maps to one or more `VocalBiomarkerFrame` instances (sliding windows of approximately 250 ms with 50% overlap).
- Silence intervals are characterized for pause analysis; they are not stored as audio.
- Non-speech events (sighs, laughter, breathing) detected within silence intervals are logged as `NonSpeechEvent` records (event type, duration, intensity only, never audio).

**Latency budget**: VAD must complete within 20 ms of segment boundary. This gates the start of downstream processing.

### 4.3 Feature Extraction

#### 4.3.1 openSMILE eGeMAPSv02

**Configuration:** `eGeMAPSv02` functional feature set. Produces 88 features per analysis window. Running in streaming mode with 250 ms frames and 125 ms hop.

**Selected features emitted** (subset of 88 used downstream):

| Feature name | openSMILE key | Notes |
|---|---|---|
| Pitch mean | `F0semitoneFrom27.5Hz_sma3nz` mean | Converted to Hz post-extraction |
| Pitch std dev | `F0semitoneFrom27.5Hz_sma3nz` stddev | |
| Jitter | `jitterLocal_sma3nz` mean | Cycle-to-cycle F0 variation |
| Shimmer | `shimmerLocaldB_sma3nz` mean | Amplitude variation |
| HNR | `HNRdBACF_sma3nz` mean | Harmonic-to-noise ratio |
| Spectral centroid | `spectralCentroid_sma3` mean | |
| Speech rate | Derived from syllable count / duration | Post-processing from VAD timestamps |
| Loudness | `Loudness_sma3` mean and range | Perceptual loudness proxy for energy |

**Latency target**: 40 ms per frame on a mobile A-class chip (A15 Bionic or equivalent Snapdragon). This target was validated in the voice model evaluation (`voice_model_deep_evaluation.md` Section 4.2, "Real-time (~10ms)" for openSMILE on desktop; mobile headroom of 4x applied).

#### 4.3.2 HuBERT Speech Emotion Recognition

**Model**: `HuBERT-large` with a fine-tuned SER (Speech Emotion Recognition) head trained on IEMOCAP. Quantized to INT8 for on-device deployment.

**Outputs per utterance:**
- `emotion_categorical`: one of {anger, sadness, fear, joy, neutral, surprise, disgust}
- `emotion_confidence`: float (0.0 to 1.0)
- `arousal`, `valence`, `dominance`: dimensional continuous values (circumplex model)

**Language note**: HuBERT's paralinguistic representation is largely language-independent. Prosodic features encode acoustic properties that carry emotional signal across languages. This is validated in the voice model evaluation: "HuBERT + openSMILE: **All languages** — Paralinguistic features are acoustic, not linguistic."

**Latency target**: 50 ms per utterance on a mobile A-class chip. Model footprint: approximately 150 MB INT8 (from HuBERT-large 316M parameters at FP32; INT8 quantization reduces by ~75%).

**Alternative for footprint-constrained devices**: `HuBERT-base` INT8 (~45 MB) with reduced accuracy; or `wav2vec 2.0 base` with SER head. Model selection is an open decision (see Section 8, OQ-1).

#### 4.3.3 Mental-State Inference Layer

This layer fuses Tier 1 features and HuBERT outputs into the four primary Tier 2 dimensions that drive CSP axis observations.

**Cognitive load estimate** (rule-based fusion):

| Signal | Weight | Threshold for elevated |
|---|---|---|
| Filled pause rate (per min) | Primary | > 6 filled pauses/min vs user baseline |
| Response latency (ms) | Secondary | > 2 std devs above user baseline |
| Speech rate deviation | Secondary | > 1.5 std devs above or below baseline |
| False start count | Tertiary | > 3 per utterance |

The ordinal output (`low`, `moderate`, `elevated`, `high`) is derived by counting how many signals are in their elevated range. This rule-based approach is chosen for interpretability and auditability at Research maturity. A learned fusion model is an open decision (OQ-3).

**Distress signal level** (composite):

| Input | Contribution |
|---|---|
| `arousal` (high) and `valence` (low) simultaneously | Strong indicator |
| `jitter` > baseline + 2 SD | Moderate indicator |
| `shimmer` > baseline + 2 SD | Moderate indicator |
| `HNR` < baseline - 2 SD | Moderate indicator |
| Sigh event rate (per min) | Moderate indicator |
| `emotion_categorical` in {anger, sadness, fear} with high confidence | Moderate indicator |

The distress signal level feeds `MODULE-crisis-detection.md` directly. When `distress_signal=elevated` is emitted, the crisis detection module evaluates additional context and may escalate per its own logic. This sensor does not make escalation decisions; it only produces the signal.

**Vocal affect index** (composite):

```
vocal_affect_index = weighted_mean([
    norm(pitch_range_hz),          # pitch expressiveness
    norm(energy_range_db),         # energy expressiveness
    norm(speech_rate_variability), # rhythmic variety
    (1 - jitter_percent / 5.0)    # penalize excessive perturbation
])
```

All components are normalized [0, 1] against the user's rolling 30-day baseline.

**Energy in voice** (longitudinal z-score):

```
energy_in_voice = (session_avg_loudness - user_30d_mean_loudness)
                  / user_30d_std_loudness
```

A value of -2.0 means "substantially lower energy than your typical voice," rendered to the user as "your voice energy is lower than usual today."

### 4.4 Session Aggregation

After each session, a background task aggregates all `VocalBiomarkerFrame` records into a `SessionVocalProfile`. This runs post-session, not in real time.

**Steps:**

1. Load all `VocalBiomarkerFrame` records from the session's in-memory buffer (or short-lived on-device store if session exceeded buffer length).
2. Compute aggregate statistics (means, variabilities, trends) per feature group.
3. Compute ND-relevant derived markers (`ADHDAVocalMarkers`, `ASDVocalMarkers`) if the user has opted into these modules.
4. Emit one CSP observation per axis using `SessionVocalProfile` values as the result.
5. Write each observation to the CRDT op-log (Section 6).
6. Discard all `VocalBiomarkerFrame` records per the retention policy (Section 5.5).

### 4.5 Longitudinal Baseline

Accurate personalized inference requires a per-user baseline. The baseline is established over the first 14 sessions (approximately two weeks of daily use) and updated on a rolling 30-day window thereafter.

| Parameter | Baseline period | Update cadence |
|---|---|---|
| Pitch mean and variability | 14 sessions | Rolling 30-day |
| Speech rate mean and variability | 14 sessions | Rolling 30-day |
| Loudness mean and std dev | 14 sessions | Rolling 30-day |
| Response latency mean and std dev | 14 sessions | Rolling 30-day |
| Filled pause rate | 14 sessions | Rolling 30-day |

**Before the baseline is established**: all z-score computations use population-level norms from the eGeMAPSv02 reference distribution. Outputs during this period carry the `quality_flag: pre_baseline` in the CSP observation. Users see a UI indicator: "Your voice patterns are still being learned."

**No inference of ND-specific markers before the baseline is complete.** `ADHDAVocalMarkers` and `ASDVocalMarkers` are set to null until session 14.

### 4.6 On-Device Model Constraints

| Constraint | Target | Notes |
|---|---|---|
| VAD latency | < 20 ms | Per segment boundary |
| openSMILE frame latency | < 40 ms | Per 250 ms frame |
| HuBERT utterance latency | < 50 ms | End-to-end per utterance |
| Peak memory (combined) | < 300 MB | openSMILE + HuBERT INT8 + buffers |
| Battery impact | < 3% per hour | Measured on iPhone 14-class device |
| Model update | Over-the-air, user-consented | Model files are code assets, not user data |

---

## 5. Privacy and Governance

### 5.1 On-Device-Only Processing

Raw audio is the highest-sensitivity possible signal class. No raw audio leaves the `audio buffer` stage under any circumstances. The CAP PEP enforces this at the observation emit boundary.

**Data class assignments:**

| Data artifact | Privacy tier | May cross boundary? |
|---|---|---|
| Raw audio (in-memory ring buffer) | `on_device_only` | Never |
| `VocalBiomarkerFrame` (per-utterance features) | `on_device_only` | Never |
| `ADHDAVocalMarkers`, `ASDVocalMarkers` | `on_device_only` | Never |
| `SessionVocalProfile` (session aggregate) | `on_device_only` (raw) | Never as a record |
| Scalar axis values (arousal, valence, etc.) | `boundary_derived` | Only with active `consent.voice.mental_state_sensing` and only the scalar value, not the session record |
| Ordinal axis values (cognitive_load, distress_signal) | `boundary_derived` | Same conditions |
| `speech_rate` (axis) | `on_device_only` | Never; biometric-adjacent |
| `pause_index` (axis) | `on_device_only` | Never; biometric-adjacent |

### 5.2 CrossBoundarySignal Declarations

The following axes are declared as `CrossBoundarySignal` per `Cytoplex/spec/03_primitives.md` and `06_conformance.md`. Any observation on these axes that is emitted with `privacy_tier: boundary_derived` is subject to CAP PEP evaluation before it may enter any cross-boundary data flow.

```yaml
# CrossBoundarySignal declarations (normative)
cross_boundary_signals:
  - signal_id: yar.voice.arousal.session_mean
    source_axis: yar.voice.arousal
    aggregation: session_mean
    data_type: float
    range: [0.0, 1.0]
    consent_scope_required: consent.voice.mental_state_sensing
    pep_policy_ref: cap/policies/voice_mentalstate_v0.rego

  - signal_id: yar.voice.valence.session_mean
    source_axis: yar.voice.valence
    aggregation: session_mean
    data_type: float
    range: [-1.0, 1.0]
    consent_scope_required: consent.voice.mental_state_sensing
    pep_policy_ref: cap/policies/voice_mentalstate_v0.rego

  - signal_id: yar.voice.cognitive_load.session_mode
    source_axis: yar.voice.cognitive_load
    aggregation: session_mode
    data_type: ordinal
    consent_scope_required: consent.voice.mental_state_sensing
    pep_policy_ref: cap/policies/voice_mentalstate_v0.rego

  - signal_id: yar.voice.distress_signal.session_max
    source_axis: yar.voice.distress_signal
    aggregation: session_max
    data_type: ordinal
    consent_scope_required: consent.voice.mental_state_sensing
    pep_policy_ref: cap/policies/voice_mentalstate_v0.rego

  - signal_id: yar.voice.vocal_affect_index.session_mean
    source_axis: yar.voice.vocal_affect_index
    aggregation: session_mean
    data_type: float
    range: [0.0, 1.0]
    consent_scope_required: consent.voice.mental_state_sensing
    pep_policy_ref: cap/policies/voice_mentalstate_v0.rego

  - signal_id: yar.voice.energy_in_voice.session_mean
    source_axis: yar.voice.energy_in_voice
    aggregation: session_mean
    data_type: float
    consent_scope_required: consent.voice.mental_state_sensing
    pep_policy_ref: cap/policies/voice_mentalstate_v0.rego
```

### 5.3 Consent Model

This adapter requires `consent.voice.mental_state_sensing`. This is a standalone scope, separate from consent for transcription or any other voice capability. Consent is required before the adapter can call `connect()`.

**Consent UI must disclose:**

1. Acoustic features (how you speak) are analyzed; your words are not processed by this sensor.
2. All feature data is stored on your device only.
3. You can turn this sensor off at any time. Past data is deleted within 24 hours of deactivation.
4. Summary signals (arousal level, distress signal, cognitive load, affective tone, vocal affect expressiveness, vocal energy) may be shared with Yar's supervisor model to personalize your experience. This sharing requires separate confirmation.
5. Your voice patterns are never used to identify you to any third party.

**Consent revocation** per SPEC-CSP Section 5.3: adapter stops emitting within one session. Pending observations in the queue are dropped. The retention timer for stored features starts immediately on revocation.

### 5.4 CAP Authorization Flow

1. Adapter calls `connect(consent_ref="consent.voice.mental_state_sensing::<grant_id>")`.
2. CSP layer issues a `Directive` to CAP PEP for the adapter's declared scopes.
3. CAP Guard evaluates against `cap/policies/voice_mentalstate_v0.rego`.
4. On `allow`: adapter transitions to `connected`. A `DecisionRecord` is written to the local audit log.
5. On `deny`: adapter cannot emit observations. Error is surfaced to the Yar settings UI.

### 5.5 Retention Policy

| Data artifact | Default retention | User-configurable range |
|---|---|---|
| Raw audio (in-memory buffer) | Overwritten immediately after feature extraction | Not configurable; always ephemeral |
| `VocalBiomarkerFrame` (per-utterance) | 7 days | 1 to 30 days |
| `SessionVocalProfile` | 365 days | 30 to unlimited |
| Longitudinal baseline data | Until user deletes | Always user-deletable |
| CSP axis observations in op-log | Per SPEC-storage-engine.md retention rules | Inherits op-log policy |

**On consent revocation or sensor disconnection**: all `VocalBiomarkerFrame` records and `SessionVocalProfile` records are queued for deletion. Deletion completes within 24 hours. CSP axis observations already written to the op-log are retained per the op-log retention policy (they no longer contain the source frames, only scalar summaries).

### 5.6 Crisis Detection Feed

When `distress_signal=elevated` is emitted by the mental-state inference layer, the CSP observation is routed to `MODULE-crisis-detection.md` before reaching the CRDT op-log. The crisis detection module evaluates the signal in context and applies its own escalation logic. This sensor does not make escalation decisions. It produces a signal; the module acts on it.

**The crisis detection feed is subject to the same consent scope** (`consent.voice.mental_state_sensing`). If the user has not consented to this sensor, no crisis signals are generated from this modality.

---

## 6. Storage: CRDT Op-Log Representation

All persisted data from this adapter enters the system as CRDT operations on the op-log (L2), per SPEC-storage-engine.md. The adapter never writes directly to the graph engine (L4).

### 6.1 Op-Log Entry Structure

Each CSP axis observation from this adapter becomes one CRDT op-log entry. The entry structure follows the `CSPObservation` schema from SPEC-CSP Section 4.1.

```yaml
# Example op-log entry (normative structure)
observation_id: obs_voice_20260622T143500Z_arousal_0e3f
adapter_id:     org.cytognosis.yar.voice.mentalstate.v0
axis_ref:
  axis_id:     yar.voice.arousal
  axis_label:  "Vocal arousal level"
  domain:      emotional_regulation
  value_type:  continuous
timestamp:     2026-06-22T14:35:00.000Z
result:
  scalar:      0.72           # session mean arousal
  coded_value: null
  waveform_ref: null          # never set by this adapter; raw audio not retained
  text_summary: null          # never set; no raw content
provenance:
  source_device: "iPhone:A15-Bionic"
  model_version: "hubert-large-ser-iemocap-int8-v0.3:opensmile-egemapsv02-2.4.0"
  collection_method: inferred
  raw_data_location: null     # no raw data location; audio was ephemeral
consent_ref:   "consent.voice.mental_state_sensing::grant_abc123"
privacy_tier:  boundary_derived
unit:          null
quality_flags: []             # or [pre_baseline] if session < 14
```

**Invariants:**
- `result.waveform_ref` is always null for this adapter. Raw audio is never stored as a blob.
- `result.text_summary` is always null. No text derived from transcription may appear here.
- `provenance.raw_data_location` is always null. Audio is ephemeral.

### 6.2 Session Profile Op-Log Entry

The `SessionVocalProfile` is stored as a structured CRDT record separate from per-axis observations. It holds the full aggregate feature set and is never transmitted.

```yaml
# SessionVocalProfile op-log entry
record_type:   SessionVocalProfile
record_id:     svp_20260622_session_0e3f
privacy_tier:  on_device_only
session_id:    session_0e3f
session_date:  2026-06-22
duration_minutes: 24.5
avg_pitch_hz:  195.3
pitch_variability_cv: 0.14
# ... (full profile fields per Section 3.4 schema)
adhd_vocal_markers:
  speech_rate_variability_zscore: 1.3
  # ...
asd_vocal_markers:
  prosodic_range_score: 0.61
  # ...
```

### 6.3 CRDT Semantics

Axis observations use **last-write-wins (LWW)** semantics per session. If the session aggregation runs twice (for example, after a retry), the second write supersedes the first using the CRDT timestamp. `SessionVocalProfile` records use LWW keyed on `session_id`.

**No merge conflict is possible** for a single-device deployment. For multi-device scenarios (future, per SPEC-sync-protocol.md), LWW is the correct policy: the device that ran the session holds the authoritative profile.

---

## 7. Conformance and Acceptance Criteria

The system shall satisfy all of the following criteria before this adapter advances from Research to Beta maturity.

### 7.1 Privacy

- **[SHALL-P1]** The system shall never write any raw audio data to disk or any persistent store.
- **[SHALL-P2]** The system shall never include raw audio in any CSP observation, op-log entry, or cross-boundary data structure.
- **[SHALL-P3]** The system shall refuse to call `connect()` if no active `consent.voice.mental_state_sensing` grant is present.
- **[SHALL-P4]** The system shall stop emitting observations within the current session when the consent grant is revoked.
- **[SHALL-P5]** The system shall complete deletion of all `VocalBiomarkerFrame` and `SessionVocalProfile` records within 24 hours of consent revocation or adapter disconnection.
- **[SHALL-P6]** The system shall classify `speech_rate` and `pause_index` axis observations as `on_device_only` and shall not emit them via any `CrossBoundarySignal` pathway.

### 7.2 Functional

- **[SHALL-F1]** The system shall extract all Tier 1 features listed in Section 3.1 from each VAD-bounded utterance exceeding 500 ms.
- **[SHALL-F2]** The system shall infer arousal and valence dimensions for each utterance exceeding 500 ms with confidence ≥ 0.4.
- **[SHALL-F3]** The system shall produce a `SessionVocalProfile` for any session with ≥ 3 utterances.
- **[SHALL-F4]** The system shall mark all axis observations with `quality_flag: pre_baseline` until 14 sessions have been completed.
- **[SHALL-F5]** The system shall route any `distress_signal=elevated` observation to `MODULE-crisis-detection.md` before writing to the op-log.
- **[SHALL-F6]** The system shall support multilingual audio input without language-detection gating (paralinguistic features are extracted regardless of language).

### 7.3 Performance

- **[SHALL-PERF1]** VAD shall complete within 20 ms of each segment boundary.
- **[SHALL-PERF2]** openSMILE feature extraction shall complete within 40 ms per 250 ms frame.
- **[SHALL-PERF3]** HuBERT SER inference shall complete within 50 ms per utterance.
- **[SHALL-PERF4]** Combined peak memory usage (all components) shall not exceed 300 MB.
- **[SHALL-PERF5]** Battery consumption shall not exceed 3% per hour of active sensing on a device with ≥ 80% battery health.

### 7.4 Affirming Language

- **[SHALL-L1]** No user-visible axis label, observation summary, notification payload, or trend description shall use the terms "normal," "abnormal," "pathological," or any clinical diagnosis name.
- **[SHALL-L2]** The distress signal axis shall be presented to users as "vocal distress signals," never as a diagnosis or risk score.
- **[SHALL-L3]** Cognitive load labels shall use the controlled vocabulary: low, moderate, elevated, high. Never "impaired," "deficient," or equivalent.
- **[SHALL-L4]** ND-specific derived markers (`ADHDAVocalMarkers`, `ASDVocalMarkers`) shall not appear in any user-facing display by name. If surfaced, they shall appear as dimensional patterns (e.g., "speech rhythm variety," "response timing patterns").

---

## 8. Open Questions

| # | Question | Current leaning | Blocker | Priority |
|---|---|---|---|---|
| **OQ-1** | On-device SER model selection: HuBERT-large INT8 (~150 MB) vs HuBERT-base INT8 (~45 MB) vs wav2vec 2.0 base | HuBERT-large if memory budget allows; base as fallback | Benchmark on iPhone 14 and Pixel 8 to confirm memory and latency targets | High (blocks Phase 1 implementation) |
| **OQ-2** | Validation of distress signal composite against a clinical anchor (e.g., PHQ-9 trajectory, GAD-7) | Correlate `distress_signal` with validated self-report (SPEC-sensor-physiological `SurveyInstrument` axis) in pilot study | Requires IRB (North Star) and 30+ session longitudinal dataset | High (required for Research→Beta promotion) |
| **OQ-3** | Cognitive load estimate: rule-based fusion (current) vs learned fusion model | Rule-based now for interpretability and auditability; learned model in Phase 2 | Training data; labeling protocol | Medium |
| **OQ-4** | Multilingual prosody calibration: do eGeMAPSv02 norms transfer across language families? | Likely yes for arousal/valence; speech rate and pause norms may differ | Empirical validation across 3+ language families in pilot | Medium |
| **OQ-5** | VAD model: WebRTC VAD vs Silero VAD | Silero VAD preferred for accuracy; WebRTC for lowest latency | Benchmark on-device; assess false-positive rate in noisy environments | Medium |
| **OQ-6** | VocalBiomarkerFrame retention: should frames be persisted at all, or always derived and discarded? | Retain for 7 days (default) to support retroactive session profile correction; always ephemeral option if privacy preference demands it | User research on willingness to retain utterance-level frames | Low |
| **OQ-7** | ASD vocal markers: `social_script_adherence` and `literal_interpretation_flags` require ASR output as input. Does this create a coupling dependency on the dialogue sensor? | Yes; these two fields are conditionally populated only when the dialogue adapter is also active and produces a transcript | Cross-adapter dependency design; assign to SPEC-neurobehavioral-axes.md | Low |
| **OQ-8** | ElevenLabs audio isolation as a pre-processing stage: would cloud-based noise removal improve extraction quality in noisy environments? | Only if on-device alternative (e.g., RNNoise) is insufficient; never as a default given privacy-first posture | Audio quality benchmarks in simulated noise environments | Low |

---

## 9. Cross-References

| Document | Relationship |
|---|---|
| `Yar/spec/SPEC-CSP.md` | Parent protocol; all lifecycle phases, consent model, op-log integration, and privacy tier taxonomy apply |
| `Yar/spec/MODULE-crisis-detection.md` | Consumer of `distress_signal=elevated` observations from this adapter |
| `Yar/spec/SPEC-storage-engine.md` | Op-log layer where CSP observations are written as CRDT entries |
| `Yar/spec/SPEC-sync-protocol.md` | CRDT replication layer; multi-device sync semantics for `SessionVocalProfile` |
| `Cytoplex/spec/03_primitives.md` | CAP primitive types: Directive, GuardDecision, DecisionRecord |
| `Cytoplex/spec/privacy-boundary-spec.md` | CrossBoundarySignal classification; PB-1 through PB-10 apply |
| `Cytoplex/spec/06_conformance.md` | CrossBoundarySignal conformance requirements |
| `04-Engineering/yar/research/voice_model_deep_evaluation.md` | Primary source for VocalBiomarkerFrame schema, model selection, and nonverbal feature taxonomy |
| `04-Engineering/yar/research/elevenlabs_evaluation.md` | STT and audio isolation capability reference |
| `04-Engineering/cytos/sensing-schema/unified-sensor-report.md` | Cytos schema tree structure; HuBERT and openSMILE as reference extractors (Section 4) |
| `04-Engineering/cytos/sensing-schema/sensor-architecture.md` | Base SensorDescriptor and SensorModality definitions |
| `SPEC-sensor-physiological.md` (planned) | `SurveyInstrument` axis outputs that will be used for distress signal validation (OQ-2) |
| `SPEC-neurobehavioral-axes.md` (planned) | Will define how voice mental-state axes combine with other sensors into longitudinal neurobehavioral axis scores |
