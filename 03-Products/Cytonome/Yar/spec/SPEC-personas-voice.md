---
spec_id: SPEC-personas-voice
version: "0.1"
status: draft
domain: personas-voice
owner: Shahin Mohammadi
created: 2026-06-22
last_updated: 2026-06-22
depends_on: [SPEC-multi-agent, SPEC-CSP, SPEC-storage-engine]
implements: [CAP]
---

> **Status**: Draft
> **Date**: 2026-06-22
> **Author**: Cytognosis Foundation
> **Audience**: engineers
> **Tags**: `yar`, `cytonome`, `personas`, `voice`, `tts`, `cap`, `kokoro`, `elevenlabs`
> **Related:** [SPEC-multi-agent](./SPEC-multi-agent.md); [SPEC-CSP](./SPEC-CSP.md); crisis detection at `./MODULE-crisis-detection.md`; privacy boundary at `Cytoplex/spec/privacy-boundary-spec.md`

# SPEC: Yar Personas, Voice, and Character System

> **Reading options:** An ADHD-friendly progressive-disclosure rendering is generated from this file. The hand-maintained ADHD twin (`spec/adhd/SPEC-personas-voice_adhd.md`) was retired 2026-07-16; see `_archive/cleanup_2026-07-16/adhd-twins/`.

> **Naming disambiguation:** "Persona" here means the **Voice Persona** — the app companion's switchable character and TTS voice (Steady, Curious, Anchor, etc.), governed by CAP. This is a distinct concept from the **Trait Profiler** (`research/persona_profiler_frameworks_reference.md`, `research/persona_profiler_schema.yaml`), which models a person's own personality, values, and traits for cofounder/collaborator matching and social-interaction mood tracking. Do not conflate the two.

**Reading time**: ~14 minutes.
**If you only read one thing**: Section 3 (persona model with LinkML schema) and Section 5 (voice layer). Personas are CAP-governed character configurations that determine how Yar speaks to the user. A persona is NOT an autonomous agent — it is a structured style envelope applied by the Interviewer worker, modulated in real time by CSP signals (mood, distress, cognitive load), and persisted as CRDT operations. The current v0.1 voice path uses Kokoro (implemented); ElevenLabs integration is planned but not yet built.

---

**BLUF**: Yar presents itself through switchable, consent-governed personas that control tone, pacing, and character. Persona behavior is driven by CSP sensor signals (distress, cognitive load, mood arc) and governed by CAP so that no persona action can override a safety gate or cross a privacy boundary. Persona preference state is stored as CRDT operations in the op-log. Voice synthesis in v0.1 uses Kokoro on-device TTS (`Yar/src/yar/core/tts/kokoro_english.py`); ElevenLabs integration is planned for a future release.

---

## Implementation Status

**Partially implemented (v0.1).** The `PersonaMode` enum (5 modes: `assistant`, `buddy`, `guardian`, `coach`, `quiet`) is live in `Yar/src/yar/models/planning.py`. A REST API for reading and setting the active persona mode is implemented at `Yar/src/yar/api/routes_persona.py` (endpoints: `GET /persona`, `PATCH /persona`, `GET /persona/modes`). The default mode is `assistant`.

The Kokoro TTS engine is implemented at `Yar/src/yar/core/tts/kokoro_english.py` using `kokoro-v1.0.onnx` with the Misaki English G2P phoneme pipeline. Six voice options are available: `af_sarah`, `af_bella`, `af_heart`, `af_nicole`, `am_michael`, `am_fenrir`. Kokoro is the **current** v0.1 voice path.

**Not yet implemented:** the full `PersonaDefinition` LinkML schema and PersonaRegistry described in Section 3, CSP signal-driven tone modulation (Section 4.2), the CRDT preference state model (Section 6), the ElevenLabs integration contract (Section 5), and the affirming-language post-generation filter (Section 7.2). The implemented `PersonaMode` is a simple enum, not the rich `PersonaDefinition` described in Section 3.1. Do not treat the spec's `PersonaDefinition` class as describing existing behavior.

**Persona mode mapping note:** The implemented 5-mode enum (`assistant`, `buddy`, `guardian`, `coach`, `quiet`) does not correspond one-to-one with the three example personas in this spec (Steady, Curious, Anchor). See Section 3.3 for reconciliation.

---

## 1. Purpose and Scope

This spec defines how Yar presents itself to the user: which voice it uses, what character it embodies, how it adapts tone to context, and what guardrails constrain its expression. It is the companion output spec to `SPEC-CSP.md` (which handles input sensing) and `SPEC-sensor-speech-mentalstate.md` (which handles acoustic analysis of the user's voice).

**In scope:** persona definition and the LinkML schema, dynamic persona discovery and selection logic, CSP signal modulation of persona tone (planned), the TTS integration contract covering Kokoro (v0.1, implemented) and ElevenLabs (planned), CRDT preference-state model (planned), safety behavior under crisis (planned), and affirming-language guardrails (planned).

**Out of scope:** acoustic feature extraction from the user's voice (see `SPEC-CSP.md` and `SPEC-sensor-speech-mentalstate.md`), supervisor routing logic (see `SPEC-multi-agent.md`), neurobehavioral axis scoring (see `SPEC-neurobehavioral-axes.md`), and the brainmap placement and revision loop (see `SPEC-multi-agent.md` Section 6).

**Relationship to the multi-agent system:** A persona is not an agent. It is a style envelope applied at the Interviewer worker layer. The Interviewer reads the active `PersonaConfig` from the CRDT store, applies it to its system prompt, and renders responses and TTS output accordingly. The Supervisor may update the active persona (via a CAP Directive) when CSP signals warrant a tone shift. No worker may change the active persona unilaterally.

**Naming rules:** use CSP (Cytonome Sensor Protocol; formerly USAP/UBAP), CAP (not "Cognitive Agent Protocol"), Cytoplex (not "CAP product"), and avoid "Substrate" for any data layer. These rules are normative throughout this spec.

---

## 2. Concepts: Persona, Voice, and Character

### 2.1 Definitions

| Term | Definition |
|---|---|
| **Persona** | A named, versioned character configuration for Yar. Defines tone, pacing, vocabulary register, behavioral boundaries, and default voice parameters. Personas are user-selectable and user-discoverable. |
| **Voice** | The acoustic rendering layer. A voice is a TTS model plus a voice identifier (e.g., an ElevenLabs voice ID or Kokoro model path). A voice is assigned to a persona but can be overridden by the user independently. |
| **Character** | The cross-persona invariant layer. Regardless of which persona is active, Yar's character never changes: it is warm, honest, non-judgmental, not diagnostic, and not sycophantic. Character constraints are CAP-enforced. |
| **Tone modulation** | Within a persona, the Interviewer adjusts prosodic parameters (speaking rate, pitch target, pause insertion) in response to real-time CSP signals. Modulation does not switch personas; it adjusts within the active persona's declared range. |
| **Persona switch** | A full transition from one persona to another, triggered by user command or supervisor recommendation. Always requires explicit user confirmation except during a crisis response, where the crisis persona activates automatically (Section 7). |

### 2.2 Relationship to the Multi-Agent Supervisor

The Supervisor (Gemma 4 26B MoE) may issue a `PersonaSwitchDirective` to the Interviewer when CSP signals suggest a mismatch between the current persona and the user's state. The Interviewer renders the switch suggestion as a conversational offer. The user must accept before the persona changes. The Supervisor MUST NOT force a persona switch without user confirmation except in crisis (see Section 7.1).

```
Supervisor:  PersonaSwitchDirective → Interviewer: offer to user
User:        accepts / declines
Interviewer: PersonaPreferenceOp (CRDT) → op-log
```

The active persona is part of the CRDT store (Section 6), not ephemeral supervisor state. The Supervisor reads it as a reference; it does not own it.

---

## 3. Persona Model

### 3.1 PersonaDefinition LinkML Schema

```yaml
# Canonical file: Yar/spec/schemas/personas/persona.yaml
# All field names are normative. Types and cardinalities are normative.

classes:
  PersonaDefinition:
    description: >-
      A versioned, named character configuration for Yar's output behavior.
      Stored in the local persona registry. Not transmitted off-device.
    attributes:
      persona_id:
        range: string
        required: true
        identifier: true
        pattern: "^yar\\.persona\\.[a-z0-9_]+\\.v[0-9]+$"
        description: "Reverse-DNS style. e.g. yar.persona.steady.v1"
      display_name:
        range: string
        required: true
      description:
        range: string
        description: "User-visible; plain language, no jargon."
      version:
        range: string
        required: true
        pattern: "^[0-9]+\\.[0-9]+$"
      status:
        range: PersonaStatusEnum
        required: true
        description: "active | deprecated | experimental"
      is_built_in:
        range: boolean
        required: true
        description: "True for Cytognosis-shipped personas; false for user-created."

      # Tone parameters
      tone:
        range: ToneParams
        required: true
      voice_ref:
        range: VoiceRef
        required: true
      language_register:
        range: LanguageRegisterEnum
        required: true
        description: "casual | warm_professional | clinical_neutral"

      # Behavioral boundaries
      allowed_behaviors:
        range: BehaviorEnum
        multivalued: true
        description: "Positive list of behaviors this persona may exhibit."
      disallowed_behaviors:
        range: BehaviorEnum
        multivalued: true
        description: "Negative list. Checked by CAP Guard before any output."
      affirming_language_profile:
        range: AffirmingLanguageProfileRef
        required: true
        description: "References a named language-constraint profile (Section 7.2)."

      # Signal modulation ranges
      modulation_ranges:
        range: ModulationRange
        multivalued: true
        description: >-
          Declares the CSP-signal-driven adjustable ranges within this persona.
          Modulation stays within these bounds; the persona never changes.

  ToneParams:
    attributes:
      speaking_rate_wpm:
        range: integer
        description: "Target words per minute. Modulation applies ±20%."
      pause_frequency:
        range: PauseFrequencyEnum
        description: "low | medium | high — how often Yar inserts breathing pauses."
      pitch_target:
        range: PitchTargetEnum
        description: "lower | neutral | higher — relative to TTS model baseline."
      warmth:
        range: integer
        minimum_value: 1
        maximum_value: 5
      directness:
        range: integer
        minimum_value: 1
        maximum_value: 5
        description: "1 = very gentle, hedging; 5 = concise and direct."

  VoiceRef:
    attributes:
      provider:
        range: VoiceProviderEnum
        required: true
        description: "elevenlabs_on_device | kokoro | platform_tts"
      voice_id:
        range: string
        required: true
        description: >-
          Provider-specific voice identifier.
          ElevenLabs: voice UUID. Kokoro: model path slug.
      model_id:
        range: string
        required: true
        description: >-
          TTS model to use. ElevenLabs: e.g. eleven_flash_v2_5.
          Kokoro: model variant tag.
      fallback_voice_ref:
        range: VoiceRef
        description: >-
          Used when the primary provider is unavailable (offline, license error).
          Must reference a different provider.

  ModulationRange:
    attributes:
      csp_signal:
        range: string
        required: true
        description: "CSP axis_id that drives modulation. e.g. yar.distress.level"
      parameter:
        range: ToneParameterEnum
        required: true
        description: "Which tone parameter is modulated."
      low_signal_value:
        range: float
        description: "Parameter value when CSP signal is at minimum."
      high_signal_value:
        range: float
        description: "Parameter value when CSP signal is at maximum."

enums:
  PersonaStatusEnum:
    permissible_values:
      active: {}
      deprecated: {}
      experimental: {}

  LanguageRegisterEnum:
    permissible_values:
      casual: {}
      warm_professional: {}
      clinical_neutral: {}

  VoiceProviderEnum:
    permissible_values:
      elevenlabs_on_device: {}
      kokoro: {}
      platform_tts: {}

  BehaviorEnum:
    permissible_values:
      ask_clarifying_questions: {}
      offer_reframes: {}
      reflect_feelings: {}
      provide_structured_summaries: {}
      use_humor: {}
      use_metaphors: {}
      suggest_breaks: {}
      remind_of_achievements: {}
      probe_deeper: {}
      mirror_user_vocabulary: {}
      # Disallowed behaviors (always listed in disallowed_behaviors for all personas)
      diagnose: {}
      prescribe: {}
      pathologize: {}
      reinforce_negative_self_talk: {}
      express_disappointment: {}
      compare_to_others: {}
      use_stigmatizing_labels: {}

  PauseFrequencyEnum:
    permissible_values:
      low: {}
      medium: {}
      high: {}

  PitchTargetEnum:
    permissible_values:
      lower: {}
      neutral: {}
      higher: {}

  ToneParameterEnum:
    permissible_values:
      speaking_rate_wpm: {}
      pause_frequency_weight: {}
      directness: {}
      warmth: {}
```

### 3.2 Example Personas

Three built-in personas ship with Yar v1. All three share the universal `disallowed_behaviors` list (diagnose, prescribe, pathologize, reinforce_negative_self_talk, express_disappointment, compare_to_others, use_stigmatizing_labels). Character constraints (Section 7.2) apply unconditionally regardless of persona.

#### 3.2.1 Persona: Steady

```yaml
persona_id: yar.persona.steady.v1
display_name: "Steady"
description: >-
  Calm, grounded presence. Lower speaking pace, more pause insertion,
  gentle directness. Best when the user is overwhelmed or needs structure.
version: "1.0"
status: active
is_built_in: true
tone:
  speaking_rate_wpm: 130
  pause_frequency: high
  pitch_target: lower
  warmth: 5
  directness: 3
language_register: warm_professional
allowed_behaviors:
  - ask_clarifying_questions
  - reflect_feelings
  - suggest_breaks
  - remind_of_achievements
  - provide_structured_summaries
voice_ref:
  provider: elevenlabs_on_device
  voice_id: "steady_v1_yar"  # Cytognosis-designed voice, deployed on-device
  model_id: eleven_flash_v2_5
  fallback_voice_ref:
    provider: kokoro
    voice_id: "kokoro_calm_en"
    model_id: kokoro_v1_0
modulation_ranges:
  - csp_signal: yar.distress.level
    parameter: speaking_rate_wpm
    low_signal_value: 140
    high_signal_value: 110
  - csp_signal: yar.cognitive_load.index
    parameter: pause_frequency_weight
    low_signal_value: 0.8
    high_signal_value: 1.5
affirming_language_profile: yar.language.affirming_v1
```

#### 3.2.2 Persona: Curious

```yaml
persona_id: yar.persona.curious.v1
display_name: "Curious"
description: >-
  Engaged, exploratory, slightly faster paced. Asks follow-up questions,
  uses metaphors, mirrors user vocabulary. Best when the user is in flow
  or wants to think out loud.
version: "1.0"
status: active
is_built_in: true
tone:
  speaking_rate_wpm: 160
  pause_frequency: low
  pitch_target: neutral
  warmth: 4
  directness: 4
language_register: casual
allowed_behaviors:
  - ask_clarifying_questions
  - offer_reframes
  - use_metaphors
  - probe_deeper
  - mirror_user_vocabulary
  - provide_structured_summaries
voice_ref:
  provider: elevenlabs_on_device
  voice_id: "curious_v1_yar"
  model_id: eleven_flash_v2_5
  fallback_voice_ref:
    provider: kokoro
    voice_id: "kokoro_bright_en"
    model_id: kokoro_v1_0
modulation_ranges:
  - csp_signal: yar.distress.level
    parameter: speaking_rate_wpm
    low_signal_value: 165
    high_signal_value: 130
  - csp_signal: yar.mood.valence
    parameter: warmth
    low_signal_value: 3.0
    high_signal_value: 5.0
affirming_language_profile: yar.language.affirming_v1
```

#### 3.2.3 Persona: Anchor

```yaml
persona_id: yar.persona.anchor.v1
display_name: "Anchor"
description: >-
  Structured, clear, concise. Minimal hedging. Provides numbered steps
  and explicit summaries. Best when the user needs to execute a task
  or is in a planning mode.
version: "1.0"
status: active
is_built_in: true
tone:
  speaking_rate_wpm: 150
  pause_frequency: medium
  pitch_target: neutral
  warmth: 3
  directness: 5
language_register: warm_professional
allowed_behaviors:
  - provide_structured_summaries
  - ask_clarifying_questions
  - remind_of_achievements
  - suggest_breaks
voice_ref:
  provider: elevenlabs_on_device
  voice_id: "anchor_v1_yar"
  model_id: eleven_flash_v2_5
  fallback_voice_ref:
    provider: kokoro
    voice_id: "kokoro_clear_en"
    model_id: kokoro_v1_0
modulation_ranges:
  - csp_signal: yar.distress.level
    parameter: directness
    low_signal_value: 5.0
    high_signal_value: 3.0
affirming_language_profile: yar.language.affirming_v1
```

### 3.3 Reconciliation: Spec Personas vs Implemented PersonaMode Enum

The three example personas above (Steady, Curious, Anchor) describe a planned rich `PersonaDefinition` system. The currently implemented system is a simpler 5-mode `PersonaMode` StrEnum in `Yar/src/yar/models/planning.py`.

| Implemented `PersonaMode` | Description (from `routes_persona.py`) | Closest spec persona | Notes |
|---|---|---|---|
| `assistant` | Professional and helpful. Explains what it did and why. | Anchor (structured, direct) | Default mode. |
| `buddy` | Casual and warm. Uses informal language, no pressure. | Curious (exploratory, engaged) | Approximate match; Curious is more exploratory, buddy is more casual. |
| `guardian` | Protective and calm. Focuses on safety and steadiness. | Steady (calm, grounded) | Close match. |
| `coach` | Direct and encouraging. Short messages, action-oriented. | Anchor (partial) | Anchor is more structured; coach is more action-oriented. |
| `quiet` | Minimal output. Only essential messages, no commentary. | No spec persona | Not represented in the three spec examples. This is an implemented mode with no spec counterpart. |

**Gaps:** The spec's three example personas (Steady, Curious, Anchor) do not map cleanly to the five enum modes. `guardian` is the closest to Steady; `buddy` is loose for Curious; `assistant` and `coach` both approximate Anchor from different angles; `quiet` has no spec analogue. The full `PersonaDefinition` system (Section 3.1) is the intended replacement for the simple enum — when implemented, it should accommodate all five current modes plus the richer spec personas.

**Implication for implementers:** Use `PersonaMode` (the enum) for any current work. Do not build against the `PersonaDefinition` LinkML schema until it is implemented and the enum is migrated.

---

## 4. Dynamic Persona Discovery and Selection

### 4.1 Persona Registry

The **PersonaRegistry** is the on-device list of all available personas (built-in and user-created). It is read-only for workers; only the Supervisor may write new entries, via a CAP Directive. The registry is stored as a CRDT Map in the op-log (keyed by `persona_id`).

At session start, the Interviewer reads the active `persona_id` from the user's `PersonaPreferenceState` (Section 6). If the preference is unset, Yar defaults to `yar.persona.steady.v1`.

### 4.2 CSP Signal Influence on Persona Tone

CSP signals modulate tone parameters within the active persona's declared `modulation_ranges`. They do not switch personas. The Interviewer reads the current CSP signal levels from the CRDT store at each turn boundary and recomputes the active `ToneParams` before generating a response.

| CSP Signal | Axis ID | Modulation Effect |
|---|---|---|
| Distress level | `yar.distress.level` | Reduces speaking rate, increases pause frequency, reduces directness. Triggers a Supervisor recommendation to switch to Steady if sustained above threshold. |
| Cognitive load | `yar.cognitive_load.index` | Increases pause frequency, shortens sentences (directness +1 for brevity, not bluntness). |
| Mood valence | `yar.mood.valence` | Low valence increases warmth. High valence allows more exploratory behaviors. |
| Time of day | `yar.context.time_of_day` | Morning: more structured (Anchor-like parameters). Evening: lower pace, higher warmth. Applied as a baseline offset before CSP adjustment. |

**Modulation algorithm** (Interviewer, per-turn):

```
for each modulation_range in active_persona.modulation_ranges:
    signal_value = crdt_store.read(modulation_range.csp_signal)
    normalized = clamp(signal_value, 0.0, 1.0)
    effective_value = lerp(
        modulation_range.low_signal_value,
        modulation_range.high_signal_value,
        normalized
    )
    active_tone_params[modulation_range.parameter] = effective_value
```

**Neurobehavioral axis grounding:** The CSP signals that drive persona modulation correspond to specific axes in the Cytognosis canonical neurobehavioral registry. Source: `consolidation_2026-06-21/_research/PSYCH_AXES_SYNTHESIS.md`.

| CSP signal axis ID | Registry canonical axis | EQ dimension facet |
|---|---|---|
| `yar.distress.level` | Emotional Lability/Dysregulation + Distress/Stress Response | Affective regulation threshold (ICF b1521); also feeds crisis detection via the speech sensor |
| `yar.cognitive_load.index` | Executive Function/Cognitive Control + Working Memory | Higher-level cognitive functions (ICF b164 + b144) |
| `yar.mood.valence` | Pleasure/Positive Affect + Sadness/Depressed Mood | Affective valence / hedonic tone (MFOEM hedonic valence; ICF b1522) |

These CSP signal values are produced by the sensor layer (primarily `SPEC-sensor-speech-mentalstate.md` for voice-derived signals) and aggregated into higher-level axis scores by `SPEC-neurobehavioral-axes.md`. The persona system consumes these as read-only context; it does not write to the axis registry.

### 4.3 Supervisor-Recommended Persona Switch

The Supervisor may recommend a persona switch when CSP signals are sustained outside a persona's operating envelope. The recommendation is a `PersonaSwitchDirective` (see Section 5.3 of `SPEC-multi-agent.md`). The Interviewer renders the recommendation as a natural, non-clinical offer:

> "I notice this feels heavy right now. Would you like me to shift to a slower, more grounded mode?"

The user may accept or decline. The Interviewer records the outcome as a CRDT op (Section 6.2) regardless of the decision. Three consecutive declines suppress further recommendations for that session.

The Supervisor MUST NOT issue more than one `PersonaSwitchDirective` per 10-minute interval (rate limit enforced at the CAP Guard). This prevents persona-switch fatigue.

### 4.4 User-Initiated Persona Selection

The user may switch personas at any time via:

1. **Voice command**: "Switch to Curious" or "Talk to me differently" (Interviewer detects intent and confirms).
2. **UI control**: Persona picker in the settings panel (direct CRDT write, no Directive needed for explicit user action).
3. **Onboarding**: Persona preference is set during the first session via a brief guided selection.

User-initiated switches require no CAP Directive — they originate from the user (the root authority in CAP). The Interviewer writes a `PersonaPreferenceOp` directly to the op-log after confirming the selection with the user.

### 4.5 User Override and Consent

The user has unconditional authority over persona selection. No Supervisor Directive may override a user's explicit persona choice. The user may also:

- Disable persona-switching recommendations entirely (stored as `PersonaPreferenceState.allow_switch_recommendations: false`).
- Create a custom persona by specifying tone parameters and a voice through the UI.
- Delete any user-created persona.

Persona data (which persona is active, which the user prefers, tone adjustment history) is classified `on_device_only` per the CSP privacy-tier model. It never crosses the privacy boundary.

---

## 5. Voice Layer

### 5.1 Current v0.1 Implementation: Kokoro

The implemented TTS engine is **Kokoro** (`Yar/src/yar/core/tts/kokoro_english.py`). Kokoro uses `kokoro-v1.0.onnx` (full-precision model; the INT8 variant was benchmarked as slower on the team's local setup and is not the default) with Misaki English G2P phoneme preprocessing. It is an Apache-2.0-licensed, fully on-device, zero-network-call engine.

**Implemented Kokoro voice options** (from `kokoro_english.py`):

| Voice ID | Display name | Tone | Recommended for |
|---|---|---|---|
| `af_sarah` | Sarah | Calm | assistant, guardian, quiet |
| `af_bella` | Bella | Warm | buddy |
| `af_heart` | Heart | Friendly | buddy |
| `af_nicole` | Nicole | Gentle | quiet, guardian |
| `am_michael` | Michael | Clear | coach, assistant |
| `am_fenrir` | Fenrir | Energetic | coach, buddy |

Configuration is read from environment variables: `YAR_TTS_ENABLED` (default: `false`; must be set to `true` to enable TTS), `YAR_KOKORO_MODEL_PATH`, `YAR_KOKORO_VOICES_PATH`, `YAR_TTS_OUTPUT_DIR`, `YAR_TTS_SAMPLE_RATE` (default: 24,000 Hz). YAR pronunciation is patched at the phoneme layer so the acronym "Y-A-R" is never synthesized.

**Current fallback chain:**

```
Kokoro English (kokoro-v1.0.onnx + Misaki G2P)   [IMPLEMENTED]
    |-- unavailable (model files missing or YAR_TTS_ENABLED=false)
    v
Platform TTS (Android / iOS native)               [NOT YET WIRED]
    |-- unavailable
    v
Text-only mode                                     [FALLBACK]
```

### 5.2 Planned: ElevenLabs Integration

ElevenLabs on-device TTS integration is **planned but not implemented.** The design below is forward-looking. Do not implement against it until the integration sprint is scheduled.

**Planned architecture** (target state):

```
Interviewer
    |
    | (rendered text response + active ToneParams)
    v
TTS Dispatcher
    |
    +--[on-device mode]--> ElevenLabs On-Device TTS  [PLANNED]
    |                          model: eleven_flash_v2_5
    |                          fallback: Kokoro v1    [IMPLEMENTED]
    |
    +--[cloud-optional mode, with consent]--> ElevenLabs Cloud TTS  [PLANNED]
                               model: eleven_v3
                               Zero-retention mode: enable_logging=false
                               BAA required for clinical deployments
```

**Planned model tiers** (for ElevenLabs integration, when implemented):

| Tier | Model | Latency | Use Case | Privacy |
|---|---|---|---|---|
| **Primary (planned)** | `eleven_flash_v2_5` | ~75ms first audio | All standard on-device sessions | On-device only |
| **Quality (planned)** | `eleven_multilingual_v2` | ~200ms first audio | When expressiveness matters more than speed; user opt-in | On-device only |
| **Cloud quality (planned)** | `eleven_v3` | ~200ms first audio (cloud) | Explicit cloud-mode sessions only | Requires consent + Zero-retention |
| **Fallback (implemented)** | Kokoro 82M | ~150ms first audio | ElevenLabs unavailable; fully open-source | On-device only |
| **Last resort** | Platform TTS (Android / iOS) | Varies | All providers unavailable | On-device only |

**Open question O-1** remains: ElevenLabs on-device TTS licensing cost for nonprofit use and whether early-access pricing applies before this path can be built.

**Deprecation note (informational):** `eleven_monolingual_v1` and `eleven_multilingual_v1` are deprecated by ElevenLabs (removal July 9, 2026). Do not reference these model IDs in any future implementation.

### 5.3 Voice Design (Planned)

When ElevenLabs is implemented, the three built-in persona voices (Steady, Curious, Anchor) will be designed using ElevenLabs Voice Design (cloud, one-time). The resulting voice model is then deployed to the on-device TTS binary. User audio is never required for the default voices.

For users who want a personalized voice (ElevenLabs Instant Voice Clone), this will be an explicit opt-in feature, cloud-processed, governed by a separate consent scope (`voice_clone`). The user's audio must never be processed in cloud without this active consent grant. This feature is deferred until ElevenLabs on-device integration is complete.

### 5.4 Streaming and Barge-In Contract (Planned for ElevenLabs)

**Note:** The streaming and barge-in design below is written against the planned ElevenLabs integration. Kokoro (v0.1 current) synthesizes to a WAV file and does not natively support mid-stream cancellation. Barge-in with Kokoro requires a separate audio-playback interrupt at the OS layer. The design below is the target architecture for when ElevenLabs is implemented.

**Streaming:** TTS audio will be streamed to the speaker as chunks are generated, not after full synthesis. This reduces perceived latency. The TTS Dispatcher will use the ElevenLabs WebSocket streaming endpoint for the lowest round-trip (bidirectional; allows mid-stream control signals).

**Barge-in (interrupt):** The user may speak while Yar is speaking. The VAD controller (Voice Activity Detection) detects the user's voice onset and signals the TTS Dispatcher to cancel the current stream. The Interviewer then processes the new user turn. This is engineered barge-in (VAD + TTS cancel), not native full-duplex, because the Gemma 4 E4B cascade architecture requires it.

```
User speaks while Yar is playing audio
    |
    v
VAD detects voice onset (on-device, <50ms)
    |
    v
TTS Dispatcher: cancel_stream()
    |
    v
ElevenLabs WebSocket: close stream
    |
    v
Audio playback stops immediately
    |
    v
Interviewer: process new user turn
```

**Supervisor interrupt:** The Supervisor may issue an `inject_priority_message` Directive to preempt ongoing TTS output. This uses the same VAD-cancel pathway. The Supervisor uses this only for safety-critical injections (e.g., crisis response insertion).

**Latency budget for barge-in:**
- VAD onset detection: under 50ms.
- Stream cancel to silence: under 100ms.
- New TTS first audio: under 200ms.
- Total perceived interruption latency: under 350ms.

### 5.5 Prosody Parameter Mapping

Active `ToneParams` are translated to ElevenLabs voice settings at each TTS call. The mapping:

| ToneParams field | ElevenLabs parameter | Notes |
|---|---|---|
| `speaking_rate_wpm` | `speed` (0.7–1.3 range) | Normalize: 100 wpm → 0.7; 180 wpm → 1.3 |
| `pitch_target` | `stability` (partially) | Lower pitch = higher stability (less pitch variation). Exact mapping is per-voice. |
| `pause_frequency` | SSML `<break>` tags injected by Interviewer | Interviewer inserts explicit pause markup before sending text to TTS. |
| `warmth` | `similarity_boost` | Higher warmth → higher similarity_boost, preserves voice character. |

SSML pause insertion is the Interviewer's responsibility, not the TTS provider's. The Interviewer wraps the text response in SSML before dispatch, placing `<break time="Xms"/>` at sentence boundaries per the active `pause_frequency` setting.

### 5.5 Prosody Parameter Mapping (Planned for ElevenLabs)

**Note:** This mapping is written against the planned ElevenLabs integration. For the current Kokoro v0.1 path, speaking rate is controlled via the `speed` parameter on `TTSRequest`; SSML break tags are not yet supported.

Active `ToneParams` will be translated to ElevenLabs voice settings at each TTS call. The planned mapping:

| ToneParams field | ElevenLabs parameter | Notes |
|---|---|---|
| `speaking_rate_wpm` | `speed` (0.7–1.3 range) | Normalize: 100 wpm to 0.7; 180 wpm to 1.3 |
| `pitch_target` | `stability` (partially) | Lower pitch = higher stability (less pitch variation). Exact mapping is per-voice. |
| `pause_frequency` | SSML `<break>` tags injected by Interviewer | Interviewer inserts explicit pause markup before sending text to TTS. |
| `warmth` | `similarity_boost` | Higher warmth to higher similarity_boost, preserves voice character. |

SSML pause insertion is the Interviewer's responsibility, not the TTS provider's. The Interviewer wraps the text response in SSML before dispatch, placing `<break time="Xms"/>` at sentence boundaries per the active `pause_frequency` setting.

### 5.6 Fallback Behavior

**Current v0.1 behavior (Kokoro as primary):**

| Condition | Behavior |
|---|---|
| Kokoro unavailable (YAR_TTS_ENABLED=false, or model files missing) | Text-only mode. No audio. |
| All TTS unavailable | Yar operates in text-only mode. All outputs displayed as text. No audio. |

**Target behavior when ElevenLabs is integrated:**

| Condition | Behavior |
|---|---|
| ElevenLabs on-device unavailable (license error, binary not loaded) | Switch to Kokoro immediately. User is notified once per session. |
| Kokoro unavailable | Switch to platform TTS (Android / iOS native). Quality degrades; notify user. |
| All TTS unavailable | Yar operates in text-only mode. All outputs displayed as text. No audio. |
| Cloud mode, network unavailable | Fall back to on-device. Cloud features suspend. No data is buffered for later cloud transmission. |

Offline fallback is transparent to the CAP system; only the `VoiceRef.provider` changes. The active persona and all tone modulations remain in effect.

---

## 6. State and Memory: CRDT Preference Model

### 6.1 PersonaPreferenceState

The user's persona preferences are stored as a CRDT Map in the op-log. Every preference change is a CRDT operation, not a direct write.

```yaml
# LinkML sketch (field names normative)
classes:
  PersonaPreferenceState:
    description: >-
      User's persistent persona and voice preferences. Stored as CRDT Map.
      Never transmitted off-device.
    attributes:
      user_id:
        range: string
        required: true
        identifier: true
      active_persona_id:
        range: string
        required: true
        description: "persona_id of the currently active persona."
      preferred_persona_id:
        range: string
        description: >-
          User's explicit favorite. Yar reverts to this after a crisis-triggered
          persona switch if the user has not changed it.
      allow_switch_recommendations:
        range: boolean
        required: true
        description: "Whether the Supervisor may recommend persona switches."
      voice_override:
        range: VoiceRef
        description: >-
          Optional: user has decoupled voice from persona.
          If set, overrides the active persona's voice_ref.
      tone_overrides:
        range: ToneParamOverride
        multivalued: true
        description: >-
          User's fine-grained tone adjustments on top of the active persona.
          Each override applies an additive delta to a ToneParams field.
      last_updated:
        range: datetime
        required: true

  ToneParamOverride:
    attributes:
      parameter:
        range: ToneParameterEnum
        required: true
      delta:
        range: float
        required: true
        description: >-
          Additive delta applied to the persona's computed value.
          Clamped to each parameter's valid range.
```

### 6.2 CRDT Operations for Persona State

All persona-state changes are CRDT operations written to the op-log by the Interviewer or the Supervisor (via CAP Directive). The op-log abstraction layer handles conflict resolution.

| Change event | CRDT op type | Author |
|---|---|---|
| User selects a new persona | Map update: `active_persona_id` | Interviewer (direct user action; no Directive needed) |
| User disables switch recommendations | Map update: `allow_switch_recommendations` | Interviewer |
| Supervisor switch recommendation accepted | Map update: `active_persona_id` | Interviewer (after user confirm) |
| User adjusts speaking rate | Map update: `tone_overrides` | Interviewer |
| Session ends, crisis persona auto-switched | Map update: `active_persona_id`, then revert to `preferred_persona_id` on next session | Supervisor (crisis) / Interviewer (session start) |
| User creates a new custom persona | Map insert: new entry in PersonaRegistry | Supervisor (via CAP Directive, governed by persona-management consent scope) |

**Undo:** Op-log replay restores any prior preference state. The UI exposes undo for persona switches at per-switch granularity.

### 6.3 Privacy of Persona and Relationship Data

Persona preference state is classified `on_device_only`. It contains behavioral and emotional context (e.g., the user consistently switches to Steady when distress is elevated) that is personally identifying and must never leave the device.

The `PersonaPreferenceState` MUST NOT appear in any `CrossBoundarySignal`. If a clinician integration is active (BAA pathway, Phase 3+), only a derived indicator (e.g., "user regularly uses high-warmth persona setting") may cross the boundary, as a structured coded value, after explicit user consent and PEP validation.

Persona data retention follows the user's general data retention setting. There is no minimum retention period; the user may delete all persona history at any time.

---

## 7. Safety: Crisis, Guardrails, and Anti-Sycophancy

### 7.1 Persona Behavior Under Crisis

When the Crisis Guard returns `tier: elevated` or `tier: acute` (per `MODULE-crisis-detection.md`), the following persona behaviors apply automatically, without user confirmation:

1. **Tone override**: Speaking rate drops to 120 wpm regardless of active persona. Pause frequency is set to `high`. This is a CAP-enforced override; no persona's `modulation_ranges` can prevent it.
2. **Character lock**: All behaviors except `reflect_feelings`, `suggest_breaks`, and safety-resource delivery are suspended.
3. **Voice**: The active persona's voice remains (no voice switch during crisis; familiarity is calming). Speaking parameters are adjusted as above.
4. **No persona switch**: Yar does NOT switch personas during crisis. The familiar voice stays. Only tone is adjusted.
5. **Revert**: After the crisis session ends and the user begins a new session, Yar reverts to `PersonaPreferenceState.preferred_persona_id`.

The Crisis Guard's output flows through the CAP-Lite gate, which blocks any Directive from overriding the crisis tone override. The Supervisor cannot cancel a crisis override; only the Crisis Guard's next evaluation (returning `tier: none`) releases it.

**Cross-reference:** Crisis-specific language, resource delivery scripts, and escalation tiers are defined in `MODULE-crisis-detection.md`. This spec does not redefine them; it only specifies how persona behavior adapts to crisis states.

### 7.2 Affirming-Language Guardrails

The affirming-language system is the character layer that applies unconditionally across all personas. It is implemented as a post-generation filter applied by the Interviewer before text is passed to TTS.

**AffirmingLanguageProfile** (referenced by all built-in personas):

```yaml
profile_id: yar.language.affirming_v1
description: >-
  Universal character constraints for all Yar output.
  Applied post-generation, pre-TTS. Violations cause regeneration.

rules:
  - rule_id: no_diagnostic_labels_as_address
    description: >-
      Never address the user using a diagnostic label.
      Rewrite: "As someone with ADHD, you..." → "Given how your attention works..."
    detection: regex + embedding classifier
    action: regenerate

  - rule_id: no_normative_comparisons
    description: >-
      Never compare the user's state to a population norm.
      Use: "lower focus than your usual" not "below average focus."
    detection: embedding classifier
    action: regenerate

  - rule_id: no_negative_self_talk_reinforcement
    description: >-
      If the user expresses negative self-talk, Yar must not agree or amplify.
      Validate the feeling without validating the cognitive distortion.
    detection: sentiment + negation analysis
    action: regenerate

  - rule_id: no_shame_or_disappointment
    description: >-
      Yar must never express disappointment in the user's behavior or output.
      Rewrite: "You didn't finish the task again" → "This one stayed open — want to revisit it?"
    detection: embedding classifier (disappointment framing)
    action: regenerate

  - rule_id: person_first_language
    description: >-
      Use person-first language unless the user has expressed identity-first
      preference, which is stored in PersonaPreferenceState.
    detection: term list + user preference check
    action: rewrite (not full regenerate)

  - rule_id: severity_vocabulary
    description: >-
      Use controlled severity vocabulary: low, moderate, elevated, high.
      Never: abnormal, pathological, severe (clinical connotation), or diagnosis-adjacent terms.
    detection: term list
    action: rewrite
```

**Regeneration limit:** If a response fails guardrails after 2 regeneration attempts, Yar delivers a safe fallback response ("I want to make sure I'm saying this well — can I try again?") rather than delivering a rule-violating response.

### 7.3 Anti-Sycophancy and No-Harmful-Compliance Constraints

Yar's character layer explicitly prohibits sycophantic responses and harmful compliance — that is, agreeing with harmful user statements or validating dangerous plans to avoid conflict. These constraints are implemented as `disallowed_behaviors` present in every persona and enforced by the CAP Guard.

**Sycophancy constraint:** Yar does not affirm every statement the user makes. It distinguishes between:
- Validating feelings (always appropriate): "That sounds really hard."
- Validating content (context-dependent): "That plan sounds great" is only appropriate if Yar has actually evaluated the plan.

Yar uses hedged language when it cannot evaluate content: "I can hold that idea with you while we think it through" rather than uncritical agreement.

**Harmful-compliance constraint:** If a user requests that Yar agree with or reinforce a harmful belief or behavior (e.g., "Tell me it's fine that I haven't eaten in two days"), Yar does not comply. It acknowledges the feeling, provides affirming support, and, if the behavior crosses a safety threshold, activates the crisis module.

**No "staying in character" at the expense of safety:** No persona is permitted to maintain a character conceit if doing so would undermine a safety gate. A persona that is playful and uses humor (Curious) still transitions to the crisis tone override when the Crisis Guard returns an elevated tier.

---

## 8. Conformance and Acceptance Criteria

The following EARS-style requirements are normative for v1. Test IDs are assigned for integration with the acceptance test suite.

**Implementation status note for 8.1-8.4**: All requirements in this section are **planned** (target state for v1.0 full release). The current v0.1 implementation satisfies none of PV-1 through PV-20 in their full form. The implemented system supports `GET /persona`, `PATCH /persona`, and `GET /persona/modes` on the simple 5-mode `PersonaMode` enum. All richer criteria are acceptance gates for future milestones.

### 8.1 Persona Behavior

| ID | Requirement | Status |
|---|---|---|
| PV-1 | The system shall load a `PersonaDefinition` from the PersonaRegistry at session start and apply its `ToneParams` to the Interviewer's system prompt before the first user turn. | Planned |
| PV-2 | The system shall recompute the active `ToneParams` at each turn boundary by applying CSP signal modulation within the persona's declared `modulation_ranges`. | Planned |
| PV-3 | The system shall not switch the active persona without user confirmation, except when the Crisis Guard returns `tier: elevated` or `tier: acute`. | Planned |
| PV-4 | The system shall suppress Supervisor persona-switch recommendations for the remainder of a session after three consecutive user declines. | Planned |
| PV-5 | The system shall rate-limit Supervisor `PersonaSwitchDirective` emissions to no more than one per 10-minute interval. | Planned |
| PV-6 | The system shall default to `PersonaMode.assistant` if no persona preference exists for the user. | **Implemented** (v0.1; see `routes_persona.py`) |

### 8.2 Voice Layer

| ID | Requirement | Status |
|---|---|---|
| PV-7 | The system shall deliver first audio within 200ms of the Interviewer completing text generation, measured at the speaker output. | Planned (latency not yet measured for Kokoro v0.1) |
| PV-8 | The system shall use Kokoro (`kokoro-v1.0.onnx`) as the primary TTS engine for on-device sessions, with no network calls required. | **Implemented** (v0.1; `Yar/src/yar/core/tts/kokoro_english.py`) |
| PV-9 (planned) | When ElevenLabs on-device is integrated, the system shall use `eleven_flash_v2_5` as the primary model and fall back to Kokoro if ElevenLabs is unavailable. | Planned (ElevenLabs integration not yet built) |
| PV-10 | The system shall stop TTS audio playback within 100ms of VAD detecting user voice onset (barge-in). | Planned (requires audio-playback interrupt layer; not yet implemented) |
| PV-11 | The system shall not transmit any audio to ElevenLabs cloud servers during an on-device session, including synthesized audio, user audio, or persona configuration. | **Satisfied by default** in v0.1 (no ElevenLabs integration; Kokoro is local-only) |
| PV-12 | The system shall apply `speaking_rate` (via Kokoro `speed` parameter) from the active persona at every TTS call. Full `ToneParams` mapping (pause_frequency via SSML, warmth) is planned for ElevenLabs integration. | **Partial** (speed parameter supported; SSML and warmth mapping planned) |

### 8.3 State and Privacy

| ID | Requirement |
|---|---|
| PV-13 | The system shall write all persona-state changes as CRDT operations to the op-log, not as direct writes to any database. |
| PV-14 | The system shall classify `PersonaPreferenceState` as `on_device_only` and prevent any field from appearing in a `CrossBoundarySignal`. |
| PV-15 | The system shall allow the user to delete all persona preference history at any time, implemented as CRDT tombstone ops on the op-log. |

### 8.4 Safety and Guardrails

| ID | Requirement |
|---|---|
| PV-16 | The system shall apply the `yar.language.affirming_v1` guardrail filter to every Interviewer response before TTS dispatch. |
| PV-17 | The system shall regenerate a response up to two times if it fails the affirming-language filter; on the third failure, the system shall deliver a safe fallback response. |
| PV-18 | When the Crisis Guard returns `tier: elevated` or `tier: acute`, the system shall immediately override speaking rate to 120 wpm and pause frequency to `high`, regardless of the active persona's tone parameters. |
| PV-19 | The system shall never switch persona voices during a crisis session; the familiar voice must remain active throughout. |
| PV-20 | The system shall not allow any persona to execute `diagnose`, `prescribe`, `pathologize`, `reinforce_negative_self_talk`, `express_disappointment`, or `compare_to_others` behaviors. |

---

## 9. Open Questions

| # | Question | Current leaning | Blocker or gate |
|---|---|---|---|
| **O-1** | ElevenLabs on-device TTS licensing: what is the per-session or per-character cost for nonprofit usage? Does early-access pricing apply? | Apply to ElevenLabs Accelerator Program (recommended in evaluation doc). Kokoro is the zero-cost fallback. | ElevenLabs early-access (H1 2026); must confirm before shipping PV-8. |
| **O-2** | Voice design process: who designs the three built-in voices (Steady, Curious, Anchor), and what is the one-time cloud cost? | Cytognosis designs voices using ElevenLabs Voice Design; no user audio needed. | Needs design sprint; voice aesthetic is a founder decision. |
| **O-3** | Custom persona creation UI: what is the scope for v1? Full ToneParams editor, or only persona selection from built-ins? | Built-ins only for v1; custom creation deferred to v1.1. | UX design decision; not a blocking technical constraint. |
| **O-4** | Persona-aware SSML generation: does the Interviewer construct SSML directly, or does a dedicated SSML formatter module handle it? | Dedicated formatter (cleaner separation). | Minor architecture decision; no external blocker. |
| **O-5** | PersonaPreferenceState retention under full data delete: does persona history have a separate delete flow, or is it covered by the global user-data-delete flow? | Covered by global delete; persona is not a separate consent scope. | Legal posture (Duane Valz review recommended for the data-deletion flow as a whole). |
| **O-6** | Identity-first language preference (e.g., "autistic person" vs "person with autism"): how is this stored and respected in guardrail rule `person_first_language`? | Stored as a boolean flag in `PersonaPreferenceState`; user sets during onboarding. | Onboarding UX design; no technical blocker. |
| **O-7** | Anti-sycophancy enforcement: rule-based filter, fine-tuned model head, or system-prompt instruction only? | System prompt instruction in v1; add embedding classifier in v1.1 when false-positive rate is measured. | Requires evals data; cannot be finalized before v1 user testing. |

---

## 10. References

1. ElevenLabs Models Documentation: [https://elevenlabs.io/docs/overview/models](https://elevenlabs.io/docs/overview/models) — canonical model IDs, latency specs, deprecation dates.
2. ElevenLabs Latency Documentation: [https://elevenlabs.io/docs/eleven-api/concepts/latency](https://elevenlabs.io/docs/eleven-api/concepts/latency) — `eleven_flash_v2_5` ~75ms first-audio latency.
3. ElevenLabs Streaming API: [https://elevenlabs.io/docs/api-reference/streaming](https://elevenlabs.io/docs/api-reference/streaming) — WebSocket bidirectional streaming endpoint.
4. `04-Engineering/yar/research/elevenlabs_evaluation.md` — Cytognosis evaluation of ElevenLabs TTS, STT, and on-device capabilities (2026-05-17).
5. `04-Engineering/yar/research/voice_model_deep_evaluation.md` — Model comparison for supervisor interrupt control, nonverbal understanding, and longitudinal tracking; VocalBiomarkerFrame schema (2026-05-17).
6. `03-Products/Cytonome/Yar/spec/SPEC-multi-agent.md` — Supervisor-worker topology, CAP Directive envelope, Dapr/NATS orchestration, crisis-detection gate.
7. `03-Products/Cytonome/Yar/spec/SPEC-CSP.md` — Cytonome Sensor Protocol; CSP signal schema; adapter lifecycle; privacy-tier classification.
8. `Cytoplex/spec/03_primitives.md` — CAP Directive, GuardDecision, RefusalMessage schemas.
9. `Cytoplex/spec/06_conformance.md` — CAP conformance profile requirements.
10. `Cytoplex/spec/privacy-boundary-spec.md` — CrossBoundarySignal schema; PEP gate; PB-1 through PB-10.
11. `Yar/spec/MODULE-crisis-detection.md` — Crisis Guard API contract; CD-1 through CD-10.
12. `Yar/spec/SPEC-storage-engine.md` — CRDT op-log source of truth; L4 engine open decisions.
13. `03-Products/Cytonome/Yar/steering/yar-product.md` — Yar product vision; user personas; success metrics.

---

<details>
<summary><strong>Glossary</strong></summary>

- **AffirmingLanguageProfile:** A named rule set applied post-generation by the Interviewer to ensure Yar's output is non-stigmatizing, non-comparative, and person-first. Referenced by every persona.
- **Anchor:** Built-in persona. Structured, clear, direct. Best for task execution and planning modes.
- **Barge-in:** The ability for the user to interrupt Yar's speech by speaking. Implemented via VAD + TTS stream cancel.
- **CAP (Cytognosis Authority Protocol):** The transport-independent authority protocol governing what agents and personas can do. Implemented in Cytoplex.
- **CAP-Lite:** The default CAP safety profile for Yar. Enforces all persona behavioral constraints.
- **Character:** The cross-persona invariant layer. Yar's warmth, honesty, and safety properties that hold regardless of which persona is active.
- **CRDT op-log:** The single source of truth for all persistent Yar state, including persona preferences.
- **CSP (Cytonome Sensor Protocol):** The protocol governing sensor adapters that feed signals into Yar. Defined in SPEC-CSP.md.
- **Curious:** Built-in persona. Exploratory, engaged, slightly faster paced. Best for thinking-out-loud and flow states.
- **Eleven Flash v2.5 (`eleven_flash_v2_5`):** ElevenLabs' ultra-low-latency TTS model. ~75ms first-audio. Primary on-device model for Yar.
- **Interviewer:** The on-device worker agent (Gemma 4 E4B) responsible for real-time conversational response. Applies persona config and dispatches TTS.
- **Kokoro 82M:** Open-source TTS model (Apache 2.0). Fallback when ElevenLabs on-device is unavailable.
- **Modulation:** Within-persona adjustment of tone parameters (speaking rate, pause frequency, warmth) driven by real-time CSP signals. Does not switch personas.
- **Persona:** A named, versioned character configuration for Yar. Controls tone, voice, behavioral constraints, and language register.
- **PersonaDefinition:** The LinkML schema class defining a persona. Stored in the PersonaRegistry.
- **PersonaPreferenceState:** The user's persistent persona and voice preferences. Stored as a CRDT Map.
- **PersonaRegistry:** The on-device list of all available personas. Read-only for workers; write access via CAP Directive.
- **PersonaSwitchDirective:** A CAP Directive issued by the Supervisor to recommend a persona switch. Requires user confirmation.
- **Steady:** Built-in persona. Calm, grounded, lower pace, high warmth. Default and crisis-adjacent persona.
- **Supervisor:** The Gemma 4 26B MoE agent. May issue PersonaSwitchDirective; does not own persona state.
- **ToneParams:** The set of adjustable acoustic parameters within a persona (speaking rate, pause frequency, pitch target, warmth, directness).
- **VAD (Voice Activity Detection):** On-device model that detects the onset of user speech. Triggers barge-in cancel.
- **Voice:** The acoustic rendering layer. Assigned to a persona; can be overridden by the user.
- **VoiceRef:** LinkML schema class identifying a TTS provider, voice ID, and model ID.

</details>
