---
spec_id: SPEC-sensor-physiological
version: "0.1"
status: draft
domain: sensor-physiological
owner: Shahin Mohammadi
created: 2026-06-22
last_updated: 2026-06-22
depends_on: [SPEC-CSP, SPEC-storage-engine]
implements: [CSP]
---

# SPEC-sensor-physiological: Physiological and Passive-Sensing Modalities

> **Reading options:** An ADHD-friendly progressive-disclosure rendering is generated from this file. The hand-maintained ADHD twin (`spec/adhd/SPEC-sensor-physiological_adhd.md`) was retired 2026-07-16; see `_archive/cleanup_2026-07-16/adhd-twins/`.

> **Status**: Draft
> **Date**: 2026-06-22
> **Author**: Cytognosis Foundation
> **Audience**: engineers
> **Tags**: `yar`, `cytonome`, `csp`, `sensor`, `wearables`, `aware`, `instruments`
> **Related:** [SPEC-CSP](./SPEC-CSP.md); privacy boundary at `Cytoplex/spec/privacy-boundary-spec.md`; storage engine at `./SPEC-storage-engine.md`

---

**Reading time**: ~15 minutes.
**If you only read one thing**: Section 3 (CSP binding). Every modality defined here must satisfy the CSP adapter lifecycle and schema contract. This spec narrows and extends CSP for three adapter classes: physiological wearables (Oura, Fitbit), AWARE passive smartphone sensing, and clinical/EMA instruments.

**BLUF**: This spec consolidates wearable, passive-sensing, and validated-instrument adapters under the CSP schema. Every signal is formally bound to a `CSPObservation`, every boundary crossing is classified as a `CrossBoundarySignal`, and every observation enters the system as a CRDT operation on the op-log, not a direct write.

> **Implementation status**: Design-only, not yet implemented. No Oura, Fitbit, HealthKit, or AWARE wearable/passive-sensing adapter code was found in any Cytognosis repo at the time of the June 2026 codebase sweep (see INCORPORATION_MAP.md §8, SPEC-sensor-physiological row). The CSP SensorDescriptor schema referenced here (`04-Engineering/cytos/sensing-schema/`) does not yet exist as a LinkML artifact. The voice-affect and CAP guard implementations in `Yar/src/` (distilhubert-ser ONNX pipeline, CapLiteGuard) demonstrate the on-device sensing infrastructure pattern; wearable adapters will follow the same pattern once the CSP schema is scaffolded.

---

## 1. Purpose and Scope

This spec is the formal modality-level complement to [SPEC-CSP](./SPEC-CSP.md). CSP defines the protocol skeleton; this document fills it in for three concrete adapter classes.

**In scope:**

- Physiological wearables: Oura Ring (Cloud API v2), Fitbit Web API, and the Apple HealthKit stub
- AWARE passive smartphone sensing: all 25 sensor classes in `profile_aware.yaml`, including ESM triggers
- Validated clinical/EMA instruments: PHQ-9/2, GAD-7/2, ASRS v1.1, WFIRS, BRIEF-A (licensed), PSQI, and AWARE ESM micro-surveys

**Out of scope:** voice and speech signals (see planned `SPEC-sensor-speech-mentalstate.md`), social-interaction signal aggregation (see planned `SPEC-sensor-social-interaction.md`), Cytoscope and future biosensors (CSP Section 6.6), and model inference internals.

**Canonical naming reminder:** the protocol is CSP (Cytonome Sensor Protocol; formerly USAP/UBAP). Do not use the deprecated aliases in new code comments, schema references, or documentation.

---

## 2. Scope and Modality Inventory

The table below lists every sensor source covered by this spec. Each row is a CSP sensor source with a declared adapter class, maturity, and privacy tier.

| Sensor Source | Adapter ID | CSP Adapter Class | Maturity | Privacy Tier | Feature Refs |
|---|---|---|---|---|---|
| Oura Ring Cloud API v2 | `org.cytognosis.yar.oura` | Physiological Wearable | Beta | `boundary_derived` (summaries), `on_device_only` (raw PPG/HRV waveforms) | F30 |
| Fitbit Web API | `org.cytognosis.yar.fitbit` | Physiological Wearable | Beta | `boundary_derived` (summaries), `on_device_only` (raw intraday waveforms) | F30 |
| Apple HealthKit | `org.cytognosis.yar.healthkit` | Physiological Wearable | Future (schema stub) | `boundary_derived` | F30 |
| AWARE Accelerometer | `org.cytognosis.yar.aware.accelerometer` | AWARE Passive | Beta | `on_device_only` (raw), `boundary_derived` (derived stats) | — |
| AWARE Gyroscope | `org.cytognosis.yar.aware.gyroscope` | AWARE Passive | Beta | `on_device_only` | — |
| AWARE Magnetometer | `org.cytognosis.yar.aware.magnetometer` | AWARE Passive | Beta | `on_device_only` | — |
| AWARE Activity Recognition | `org.cytognosis.yar.aware.activity` | AWARE Passive | Beta | `boundary_derived` | — |
| AWARE Light | `org.cytognosis.yar.aware.light` | AWARE Passive | Beta | `boundary_derived` | — |
| AWARE Barometer | `org.cytognosis.yar.aware.barometer` | AWARE Passive | Beta | `boundary_derived` | — |
| AWARE Location | `org.cytognosis.yar.aware.location` | AWARE Passive | Beta | `on_device_only` (raw coordinates); `boundary_derived` (location-entropy scalar) | — |
| AWARE Screen | `org.cytognosis.yar.aware.screen` | AWARE Passive | Beta | `boundary_derived` | — |
| AWARE Applications | `org.cytognosis.yar.aware.applications` | AWARE Passive | Beta | `boundary_derived` (app-category dwell); `on_device_only` (package names) | — |
| AWARE Notifications | `org.cytognosis.yar.aware.notifications` | AWARE Passive | Beta | `boundary_derived` (counts, hashed source) | — |
| AWARE Keyboard | `org.cytognosis.yar.aware.keyboard` | AWARE Passive | Beta | `boundary_derived` (counts only, never keystrokes) | — |
| AWARE Touch | `org.cytognosis.yar.aware.touch` | AWARE Passive | Beta | `boundary_derived` | — |
| AWARE Communication | `org.cytognosis.yar.aware.communication` | AWARE Passive | Beta | `boundary_derived` (hashed contacts, duration); `on_device_only` (raw identifiers) | — |
| AWARE WiFi | `org.cytognosis.yar.aware.wifi` | AWARE Passive | Beta | `boundary_derived` (hashed SSID/BSSID) | — |
| AWARE Bluetooth | `org.cytognosis.yar.aware.bluetooth` | AWARE Passive | Beta | `boundary_derived` (hashed addresses) | — |
| AWARE Battery | `org.cytognosis.yar.aware.battery` | AWARE Passive | Beta | `boundary_derived` | — |
| AWARE Network | `org.cytognosis.yar.aware.network` | AWARE Passive | Beta | `boundary_derived` | — |
| AWARE ESM / EMA | `org.cytognosis.yar.aware.esm` | AWARE ESM | Beta | `clinician_gated` (clinical scores); `boundary_derived` (symptom-severity summaries) | F62 |
| PHQ-9 / PHQ-2 | `org.cytognosis.yar.instrument.phq` | Validated Instrument | Beta | `clinician_gated` (item responses); `boundary_derived` (total score) | F62 |
| GAD-7 / GAD-2 | `org.cytognosis.yar.instrument.gad` | Validated Instrument | Beta | `clinician_gated` (item responses); `boundary_derived` (total score) | F62 |
| ASRS v1.1 | `org.cytognosis.yar.instrument.asrs` | Validated Instrument | Beta | `clinician_gated` (item responses); `boundary_derived` (subscale scores) | F62 |
| WFIRS | `org.cytognosis.yar.instrument.wfirs` | Validated Instrument | Beta | `clinician_gated` | F62 |
| BRIEF-A (licensed) | `org.cytognosis.yar.instrument.briefa` | Validated Instrument | Beta | `clinician_gated` | F62 |
| PSQI | `org.cytognosis.yar.instrument.psqi` | Validated Instrument | Beta | `clinician_gated` (item responses); `boundary_derived` (global score, component scores) | F62 |

---

## 3. CSP Binding

### 3.1 Adapter Class to CSP Section Mapping

| This spec's adapter class | CSP Section | SensorDescriptor.adapter_class value |
|---|---|---|
| Physiological Wearable | CSP Section 6.3 | `physiological_wearable` |
| AWARE Passive | CSP Section 6.5 (partial) | `passive_digital_phenotyping` |
| AWARE ESM | CSP Section 6.1 (self-report) + 6.2 (instrument) | `ecological_momentary_assessment` |
| Validated Instrument | CSP Section 6.2 | `validated_instrument` |

### 3.2 LinkML Class Hierarchy

All classes defined in this spec extend the cytos sensing-schema base classes from `04-Engineering/cytos/sensing-schema/` and the CSP schema from SPEC-CSP. The inheritance chain is:

```
sosa:Observation
  └── CSPObservation                          (SPEC-CSP Section 4.1)
        ├── PhysiologicalObservation          (this spec, §3.3)
        │     ├── WearableVitalObservation    (§4.1)
        │     │     ├── OuraHeartRateObs
        │     │     ├── OuraHRVObs
        │     │     ├── OuraSleepSessionObs
        │     │     ├── OuraSkinTempObs
        │     │     ├── OuraActivityDayObs
        │     │     ├── OuraReadinessObs
        │     │     ├── OuraSpO2Obs
        │     │     ├── OuraStressObs
        │     │     ├── FitbitHeartRateObs
        │     │     ├── FitbitHRVObs
        │     │     ├── FitbitSleepSessionObs
        │     │     ├── FitbitStepsObs
        │     │     ├── FitbitActivityMinutesObs
        │     │     ├── FitbitActiveZoneMinutesObs
        │     │     ├── FitbitStressScoreObs
        │     │     ├── FitbitSkinTempObs
        │     │     ├── FitbitSpO2Obs
        │     │     ├── FitbitRespiratoryRateObs
        │     │     └── FitbitVO2MaxObs
        │     └── PassiveDigitalPhenotypingObservation   (§4.2)
        │           ├── AWAREIMUObservation               (accel/gyro/mag/linear accel/rotation/gravity)
        │           ├── AWAREActivityObservation          (extends ActivityRecognitionEvent)
        │           ├── AWAREEnvironmentalObservation     (light/baro/temp/proximity)
        │           ├── AWARELocationObservation          (extends LocationFix)
        │           ├── AWAREScreenObservation            (extends ScreenEvent)
        │           ├── AWAREAppObservation               (extends AppForegroundEvent)
        │           ├── AWARENotificationObservation      (extends NotificationEvent)
        │           ├── AWAREKeyboardObservation          (extends KeyboardEvent)
        │           ├── AWARETouchObservation             (extends TouchEvent)
        │           ├── AWARECommunicationObservation     (extends CommunicationEvent)
        │           ├── AWARENetworkObservation           (extends NetworkEvent)
        │           ├── AWAREWifiObservation
        │           ├── AWAREBluetoothObservation
        │           └── AWAREBatteryObservation           (extends BatteryEvent)
        └── InstrumentObservation                         (§4.3)
              ├── SurveyResponse                          (from cytos/selfreport.yaml)
              └── ESMSurveyResponse                       (extends SurveyResponse with trigger metadata)
```

### 3.3 PhysiologicalObservation Base Class

```yaml
# LinkML (normative field names; inherits all CSPObservation fields)
classes:
  PhysiologicalObservation:
    is_a: CSPObservation
    description: >-
      Base class for all physiological and passive-sensing observations.
      Adds vendor context, sampling provenance, and ND-relevant derived fields.
    attributes:
      vendor:
        range: VendorEnum
        required: true       # oura | fitbit | healthkit | aware | instrument
      collection_epoch:
        range: CollectionEpochEnum
                             # realtime | intraday | daily_summary | event_driven
      nd_signal_flags:
        range: NDSignalFlagEnum
        multivalued: true    # see §4.4 ND-relevant derived features
      biolink_class:
        range: string        # e.g. biolink:PhenotypicFeature for behaviorally-relevant axes
```

### 3.4 Axis Registry: Built-in Axes Produced by This Spec

These axes are registered as CSP built-in axes (namespace `yar.*`). All axes below are `boundary_derived` by default unless marked `on_device_only`.

| axis_id | axis_label | domain | value_type | unit | LOINC/code | Biolink |
|---|---|---|---|---|---|---|
| `yar.physio.heart_rate` | Heart rate | cardiovascular | continuous | /min | 8867-4 | biolink:PhenotypicFeature |
| `yar.physio.resting_heart_rate` | Resting heart rate | cardiovascular | continuous | /min | 40443-4 | biolink:PhenotypicFeature |
| `yar.physio.hrv_rmssd` | HRV (RMSSD) | autonomic_regulation | continuous | ms | 80404-7 | biolink:PhenotypicFeature |
| `yar.physio.hrv_lf` | HRV LF power | autonomic_regulation | continuous | ms² | sensor:hrv-lf-power | — |
| `yar.physio.hrv_hf` | HRV HF power | autonomic_regulation | continuous | ms² | sensor:hrv-hf-power | — |
| `yar.physio.sleep_efficiency` | Sleep efficiency | sleep_quality | continuous | % | 93832-4 | biolink:PhenotypicFeature |
| `yar.physio.sleep_deep_duration` | Deep sleep duration | sleep_quality | continuous | s | 93831-6 | — |
| `yar.physio.sleep_rem_duration` | REM duration | sleep_quality | continuous | s | 93829-0 | — |
| `yar.physio.sleep_latency` | Sleep onset latency | sleep_quality | continuous | s | — | — |
| `yar.physio.spo2` | Blood oxygen saturation | respiratory | continuous | % | 59408-5 | biolink:PhenotypicFeature |
| `yar.physio.respiratory_rate` | Respiratory rate | respiratory | continuous | /min | 9279-1 | — |
| `yar.physio.skin_temp_deviation` | Skin temperature deviation | thermoregulation | continuous | Cel | 61008-9 | — |
| `yar.physio.step_count` | Daily step count | activity | continuous | {steps} | 55423-8 | — |
| `yar.physio.active_zone_minutes` | Active zone minutes | activity | continuous | min | 68516-4 | — |
| `yar.physio.readiness_score` | Daily readiness | capacity_estimate | continuous | {score} | sensor:oura-readiness | — |
| `yar.physio.stress_score` | Stress management score | autonomic_regulation | continuous | {score} | sensor:fitbit-stress | — |
| `yar.physio.vo2_max` | VO2 max | cardiovascular_fitness | continuous | mL/kg/min | 60842-2 | — |
| `yar.aware.activity_state` | Physical activity state | activity | categorical | — | — | — |
| `yar.aware.screen_unlock_rate` | Screen unlock rate | digital_behavior | continuous | /h | — | biolink:PhenotypicFeature |
| `yar.aware.app_switch_rate` | App switching rate | digital_behavior | continuous | /h | — | biolink:PhenotypicFeature |
| `yar.aware.location_entropy` | Location entropy | behavioral_regularity | continuous | bits | — | biolink:PhenotypicFeature |
| `yar.aware.notification_rate` | Notification rate | cognitive_load_proxy | continuous | /h | — | — |
| `yar.aware.ambient_light` | Ambient light | environmental | continuous | lx | — | — |
| `yar.aware.call_duration_daily` | Daily call duration (**DEPRECATED** — superseded by `yar.social.call_duration_total_daily` in SPEC-sensor-social-interaction.md; use the canonical social axis for all new code) | social_engagement | continuous | s | — | biolink:PhenotypicFeature |
| `yar.instrument.phq9_score` | Depression severity (PHQ-9) | mood_distress | continuous | {score} | 44261-6 | biolink:PhenotypicFeature |
| `yar.instrument.gad7_score` | Anxiety severity (GAD-7) | anxiety_arousal | continuous | {score} | 70274-6 | biolink:PhenotypicFeature |
| `yar.instrument.asrs_parta_score` | Attention difficulty screen (ASRS-A) | attention_regulation | continuous | {score} | 73633-9 | biolink:PhenotypicFeature |
| `yar.instrument.psqi_global` | Sleep quality index (PSQI) | sleep_quality | continuous | {score} | 95653-4 | biolink:PhenotypicFeature |

**Affirming language note:** axis labels are named for experienced states, not diagnostic categories. "Attention difficulty screen" rather than "ADHD symptom score." Severity outputs use the controlled vocabulary `low | moderate | elevated | high`; never "abnormal" or "pathological."

**Deprecation note:** `yar.aware.call_duration_daily` is DEPRECATED. It is superseded by `yar.social.call_duration_total_daily`, defined in SPEC-sensor-social-interaction.md and registered under the social-interaction adapter (`org.cytognosis.yar.social_interaction`). New code must use `yar.social.call_duration_total_daily`. The deprecated axis remains in the registry for legacy read compatibility until the social-interaction adapter reaches stable maturity; write new observations to the canonical axis only.

### 3.4a Axis Registry Alignment

The table below maps each physiological/AWARE axis to the canonical 63-axis registry name and EQ dimension facet (source: PSYCH_AXES_SYNTHESIS.md Section 5.2). "N/A" indicates axes that are environmental or device-context signals without a direct EQ neurobehavioral dimension (they feed derived features rather than axis scores directly).

| axis_id | Canonical 63-axis registry name | Category | EQ dimension facet (OBA/ICF anchor) | Factor grouping |
|---|---|---|---|---|
| `yar.physio.hrv_rmssd` | Autonomic Arousal | Somatic | ICF b4301 (heart rate functions, adjacent); autonomic-cardiac regulation / vagal tone | Somatic/Physiological |
| `yar.physio.sleep_efficiency` | Sleep Quality/Architecture | Sleep | ICF b1342 (sleep continuity) | Sleep/Arousal/Circadian |
| `yar.physio.sleep_deep_duration` | Sleep Quality/Architecture | Sleep | ICF b1340 sub (deep sleep amount) | Sleep/Arousal/Circadian |
| `yar.physio.sleep_rem_duration` | Sleep Onset/Maintenance | Sleep | ICF b1344 (sleep cycle, REM amount) | Sleep/Arousal/Circadian |
| `yar.physio.sleep_latency` | Sleep Onset/Maintenance | Sleep | ICF b1341 (sleep onset latency) | Sleep/Arousal/Circadian |
| `yar.physio.spo2` | Cardiovascular Symptoms | Somatic | ICF b4402 (oxygen-carrying capacity) | Somatic/Physiological |
| `yar.physio.step_count` | Psychomotor Activity | Behavioral | ICF b147 (psychomotor functions) | Somatic/Physiological |
| `yar.physio.skin_temp_deviation` | Circadian Rhythm | Sleep | OBA skin temperature variability; type-7 mistiming signal | Sleep/Arousal/Circadian |
| `yar.physio.readiness_score` | Fatigue/Energy | Somatic | OBA recovery/readiness composite | Somatic/Physiological |
| `yar.physio.heart_rate` | Cardiovascular Symptoms | Somatic | ICF b410 (heart functions) | Somatic/Physiological |
| `yar.physio.resting_heart_rate` | Autonomic Arousal | Somatic | ICF b410 + b4301 | Somatic/Physiological |
| `yar.physio.hrv_lf` | Autonomic Arousal | Somatic | ICF b4301 (LF spectral power, sympathetic tone) | Somatic/Physiological |
| `yar.physio.hrv_hf` | Autonomic Arousal | Somatic | ICF b4301 (HF spectral power, parasympathetic tone) | Somatic/Physiological |
| `yar.physio.respiratory_rate` | Respiratory Symptoms | Somatic | ICF b440 (respiration functions) | Somatic/Physiological |
| `yar.physio.stress_score` | Autonomic Arousal + Distress/Stress Response | Somatic + Emotional | OBA stress composite | Somatic/Physiological |
| `yar.physio.vo2_max` | Fatigue/Energy | Somatic | OBA cardiorespiratory fitness | Somatic/Physiological |
| `yar.physio.active_zone_minutes` | Psychomotor Activity | Behavioral | ICF b147 (active energy expenditure) | Somatic/Physiological |
| `yar.aware.screen_unlock_rate` | Attention (Selective/Divided) | Cognitive | ICF b140 (attention functions) — digital proxy | Cognitive Control |
| `yar.aware.app_switch_rate` | Cognitive Flexibility | Cognitive | ICF b1643 (mental flexibility) — digital proxy | Cognitive Control |
| `yar.aware.location_entropy` | Habit/Automaticity + Psychomotor Activity | Behavioral | ICF b147 + d460 (moving around in different locations) | Somatic/Physiological |
| `yar.aware.notification_rate` | Attention (Sustained) | Cognitive | ICF b140 (attention functions) — interrupt load proxy | Cognitive Control |
| `yar.aware.ambient_light` | Circadian Rhythm | Sleep | OBA light exposure; circadian phase anchor | Sleep/Arousal/Circadian |
| `yar.aware.call_duration_daily` | Social Motivation/Attachment | Social | ICF d750 (informal social relationships) **DEPRECATED** — use `yar.social.call_duration_total_daily` | Social/Interpersonal |
| `yar.aware.activity_state` | Psychomotor Activity | Behavioral | ICF b147 (psychomotor functions) | Somatic/Physiological |
| `yar.instrument.phq9_score` | Sadness/Depressed Mood + Anhedonia/Diminished Interest | Emotional | ICF b152 (emotional functions); RDoC Negative Valence Systems | Negative Affect |
| `yar.instrument.gad7_score` | Anxiety/Worry + Fear/Acute Threat Response | Emotional | ICF b152; RDoC Negative Valence / Potential Threat | Negative Affect |
| `yar.instrument.asrs_parta_score` | Attention (Sustained) + Impulse Control/Inhibition | Cognitive + Behavioral | ICF b140 + b164 (higher-level cognitive functions) | Cognitive Control |
| `yar.instrument.psqi_global` | Sleep Quality/Architecture + Sleep Onset/Maintenance | Sleep | ICF b134 (sleep functions) | Sleep/Arousal/Circadian |

*Source: PSYCH_AXES_SYNTHESIS.md §3.1 (63-axis inventory) and §5.1 (physiological sensor EQ mapping).*

---

## 4. Per-Modality Sections

### 4.1 Physiological Wearables

#### 4.1.1 Oura Ring

**Data source:** Oura Cloud API v2 (`https://api.ouraring.com/v2/usercollection/`)

**Authentication:** OAuth2 Authorization Code with scope separation per data type (`daily`, `heartrate`, `sleep`, `personal`). Each scope maps to a distinct `ConsentScope` in the CSP consent model.

**Ingestion adapter:** `OuraSensorAdapter` (Python, aiohttp, tenacity retry). Polling strategy: daily summaries batched once per day; heart rate every 5 minutes; webhook subscriptions for event-driven updates.

**Sampling/cadence:**

| Oura signal | Cadence | Raw data location |
|---|---|---|
| Heart rate | 5-min intervals | `on_device_only` PPG waveform; interval average is `boundary_derived` |
| HRV (RMSSD) | 5-min during sleep | same |
| Sleep stages | Per 5-min epoch | stage string stored on-device; stage durations are `boundary_derived` |
| Daily activity | Daily summary | `boundary_derived` |
| Daily readiness | Daily summary | `boundary_derived` |
| Skin temperature deviation | Daily (nightly) | `boundary_derived` |
| SpO2 (daily avg/min/max) | Daily summary | `boundary_derived` |
| Daily stress | Daily summary | `boundary_derived` |

**FHIR mapping (normative LOINC codes):**

| Signal | LOINC | UCUM unit | CSP class |
|---|---|---|---|
| Heart rate | 8867-4 | /min | `OuraHeartRateObs` |
| HRV RMSSD | 80404-7 | ms | `OuraHRVObs` |
| Sleep duration | 93832-4 | s | `OuraSleepSessionObs` (compound: deep 93831-6, light 93830-8, REM 93829-0, awake 93828-2) |
| Skin temp deviation | 61008-9 | Cel | `OuraSkinTempObs` |
| Step count | 55423-8 | {steps} | `OuraActivityDayObs` |
| SpO2 | 59408-5 | % | `OuraSpO2Obs` |
| Readiness score | sensor:oura-readiness | {score} | `OuraReadinessObs` |

**ND-relevant derived features:** See Section 4.4.

**SensorDescriptor (normative YAML):**

```yaml
adapter_id: org.cytognosis.yar.oura
display_name: "Oura Ring"
adapter_class: physiological_wearable
maturity: beta
modalities: [cardiovascular, sleep, activity, thermoregulation, respiratory]
axes_produced:
  - yar.physio.heart_rate
  - yar.physio.hrv_rmssd
  - yar.physio.sleep_efficiency
  - yar.physio.sleep_deep_duration
  - yar.physio.sleep_rem_duration
  - yar.physio.sleep_latency
  - yar.physio.spo2
  - yar.physio.skin_temp_deviation
  - yar.physio.step_count
  - yar.physio.readiness_score
  - yar.physio.stress_score
privacy_tier: boundary_derived        # summaries; raw waveforms are on_device_only
requires_consent: [oura.sleep, oura.heartrate, oura.activity, oura.temperature]
schema_ref: "cytos/schemas/domains/sensor/vendors/vendor_oura.yaml"
implementation_ref: "04-Engineering/yar/sensors/implementing-wearables.md"
```

#### 4.1.2 Fitbit

**Data source:** Fitbit Web API (`https://api.fitbit.com/`)

**Authentication:** OAuth2 Authorization Code with PKCE (required since 2023). Scopes: `activity`, `heartrate`, `sleep`, `temperature`, `respiratory_rate`, `oxygen_saturation`. Each scope is a separate `ConsentScope`.

**Ingestion adapter:** `FitbitSensorAdapter` (Python, aiohttp, `FitbitTokenManager` for automatic refresh). Rate limit: 150 requests per hour per user. Strategy: batch daily summaries first, then fill intraday data within remaining quota. Intraday access (1-second HR, 1-minute steps) requires special API approval.

**Sampling/cadence:**

| Fitbit signal | Cadence | Intraday? | Privacy tier |
|---|---|---|---|
| Heart rate summary | Daily | No | `boundary_derived` |
| Heart rate intraday | 1-second resolution | Yes (special approval) | `on_device_only` |
| HRV (RMSSD, LF, HF) | 5-min during sleep | No | `boundary_derived` |
| Sleep stages | 30-second epochs | No | `boundary_derived` (durations); `on_device_only` (epoch string) |
| Steps summary | Daily | No | `boundary_derived` |
| Steps intraday | 1-minute | Yes | `on_device_only` |
| Active zone minutes | Daily | No | `boundary_derived` |
| Skin temperature | Nightly | No | `boundary_derived` |
| SpO2 | Nightly | No | `boundary_derived` |
| Respiratory rate | Per sleep stage | No | `boundary_derived` |
| Stress/VO2 Max | Daily | No | `boundary_derived` |

**Fitbit HRV advantage over Oura:** Fitbit provides RMSSD plus LF and HF spectral power components, enabling autonomic nervous system balance metrics. The `FitbitHRVObs` class carries all three components as a `CompoundResult`.

**FHIR mapping (normative LOINC codes):**

| Signal | LOINC | UCUM unit | CSP class |
|---|---|---|---|
| Heart rate | 8867-4 | /min | `FitbitHeartRateObs` |
| Resting heart rate | 40443-4 | /min | `FitbitHeartRateObs` |
| HRV RMSSD | 80404-7 | ms | `FitbitHRVObs` |
| Sleep duration | 93832-4 | s | `FitbitSleepSessionObs` |
| Steps | 55423-8 | {steps} | `FitbitStepsObs` |
| Moderate activity | 68516-4 | min | `FitbitActivityMinutesObs` |
| Vigorous activity | 68515-6 | min | `FitbitActivityMinutesObs` |
| Skin temperature | 61008-9 | Cel | `FitbitSkinTempObs` |
| SpO2 | 59408-5 | % | `FitbitSpO2Obs` |
| Respiratory rate | 9279-1 | /min | `FitbitRespiratoryRateObs` |
| VO2 max | 60842-2 | mL/kg/min | `FitbitVO2MaxObs` |

**SensorDescriptor (normative YAML):**

```yaml
adapter_id: org.cytognosis.yar.fitbit
display_name: "Fitbit"
adapter_class: physiological_wearable
maturity: beta
modalities: [cardiovascular, sleep, activity, thermoregulation, respiratory, cardiovascular_fitness]
axes_produced:
  - yar.physio.heart_rate
  - yar.physio.resting_heart_rate
  - yar.physio.hrv_rmssd
  - yar.physio.hrv_lf
  - yar.physio.hrv_hf
  - yar.physio.sleep_efficiency
  - yar.physio.sleep_deep_duration
  - yar.physio.sleep_rem_duration
  - yar.physio.spo2
  - yar.physio.respiratory_rate
  - yar.physio.skin_temp_deviation
  - yar.physio.step_count
  - yar.physio.active_zone_minutes
  - yar.physio.stress_score
  - yar.physio.vo2_max
privacy_tier: boundary_derived
requires_consent: [fitbit.heartrate, fitbit.sleep, fitbit.activity, fitbit.temperature, fitbit.respiratory_rate, fitbit.oxygen_saturation]
schema_ref: "cytos/schemas/domains/sensor/vendors/vendor_fitbit.yaml"
implementation_ref: "04-Engineering/yar/sensors/implementing-wearables.md"
```

#### 4.1.3 Apple HealthKit (stub)

Schema stub only. Full implementation is blocked on confirming Apple's FHIR R4/R5 export API stability (CSP Open item O-2). Adapter ID: `org.cytognosis.yar.healthkit`. Modality coverage is expected to match Oura plus add menstrual cycle data (see planned `SPEC-sensor-menstrual.md`).

#### 4.1.4 Cross-Vendor Normalization

When the same axis is produced by multiple adapters (for example, `yar.physio.hrv_rmssd` from both Oura and Fitbit), the cross-adapter aggregation semantics apply. Decision on merging strategy (last-write, weighted average, or federated score) is deferred to `SPEC-neurobehavioral-axes.md` (CSP Open item O-8). Until resolved, each adapter writes independently to the same axis, and the read layer surfaces the most recent value with `adapter_id` as provenance.

---

### 4.2 AWARE Passive Smartphone Sensing

**Data source:** AWARE (Advanced Wearable and Ambient Recognition Engine) Android/iOS framework. Variant support: both AWARE full (plugin-based) and AWARE-Light (simplified sensor manager). The adapter normalizes differences at ingestion.

**Ingestion modes:** batch CSV export, direct SQLite file ingestion, or AWARE API real-time stream. All three paths pass through the `AWARETransformer` before CAP.

**Core privacy invariants** (enforced at schema level, not configuration):

- All phone numbers, contact identifiers, WiFi SSIDs, BSSID, and Bluetooth device addresses are irreversibly SHA-256 hashed with a per-device salt before any persistence.
- Notification text is hashed; raw content is never stored.
- Keyboard events record counts only (`key_count`, `backspace_count`); raw keystrokes are never recorded.
- Raw GPS coordinates are `on_device_only`. The only boundary-crossable location signal is the derived scalar `yar.aware.location_entropy`.

**Sensor group overview:**

| Group | AWARE sensors | Privacy level | Key ND signal |
|---|---|---|---|
| IMU | Accelerometer, Gyroscope, Magnetometer, Linear Acceleration, Rotation, Gravity | `contextual` (raw = `on_device_only`) | Fidgeting, device manipulation |
| Activity | Activity Recognition | `behavioral` | Sedentary bouts, hyperfocus detection |
| Environmental | Light, Barometer, Temperature, Proximity | `contextual` | Circadian light exposure, altitude |
| Location | Location (GPS/network/fused) | `behavioral` (`on_device_only` for raw) | Routine regularity, location entropy |
| Digital behavior | Screen, Applications, Notifications, Keyboard, Touch | `behavioral` | Attentional fragmentation, doomscrolling |
| Communication | Communication (call/SMS metadata), Telephony | `behavioral` (all IDs hashed) | Social rhythm |
| Device state | Battery, Network, WiFi, Bluetooth | `contextual` (IDs hashed) | Usage intensity proxy |
| ESM | AWARE ESM plugin | `health` | Momentary subjective state |

**Sampling rates:**

| Sensor group | Default rate | Low-power rate |
|---|---|---|
| IMU (accel, gyro, mag) | 5 Hz | 1 Hz |
| Environmental (light, baro) | 0.1 Hz (every 10 s) | 0.017 Hz (every 60 s) |
| Location | 0.003 Hz (every 5 min) | 0.0006 Hz (every 30 min) |
| Activity recognition | 0.017 Hz (every 60 s) | 0.003 Hz (every 5 min) |
| Screen / App / Comm / Touch / Keyboard | Event-driven | Event-driven |
| Battery / Network / WiFi / Bluetooth | 0.017 Hz or event-driven | 0.003 Hz |

**Battery optimization requirements:** adaptive sampling (reduce IMU when activity = still for >5 min), batched 30–60 s SQLite writes, duty cycling of GPS and WiFi scan during sleep hours.

**Linking AWARE classes to CSP:**

```yaml
# LinkML sketch — normative class names
classes:
  AWAREIMUObservation:
    is_a: PhysiologicalObservation
    mixins: [AWAREObservationMixin]
    description: Three-axis inertial measurement unit sample (accel/gyro/mag/linear/rotation/gravity).
    attributes:
      imu_type: { range: IMUTypeEnum, required: true }   # accelerometer | gyroscope | magnetometer | linear_accel | rotation | gravity
      x_value:  { range: float }    # m/s², rad/s, or µT depending on imu_type
      y_value:  { range: float }
      z_value:  { range: float }
      accuracy: { range: integer }  # Android sensor accuracy constant

  AWAREActivityObservation:
    is_a: ActivityRecognitionEvent   # from cytos/context.yaml
    mixins: [AWAREObservationMixin, PhysiologicalObservation]
    # Adds no new fields; inherits activity + confidence from ActivityRecognitionEvent

  AWAREEnvironmentalObservation:
    is_a: PhysiologicalObservation
    mixins: [AWAREObservationMixin]
    attributes:
      env_type:   { range: EnvSensorTypeEnum, required: true }  # light | barometer | temperature | proximity
      scalar_value: { range: float }
      unit:       { range: string }   # lx | hPa | Cel | boolean

  AWARELocationObservation:
    is_a: LocationFix                # from cytos/context.yaml
    mixins: [AWAREObservationMixin, PhysiologicalObservation]
    # LocationFix provides latitude, longitude, altitude, speed, accuracy, provider
    # Raw coordinates are privacy_tier: on_device_only (enforced at PEP)

  AWAREScreenObservation:
    is_a: ScreenEvent               # from cytos/context.yaml
    mixins: [AWAREObservationMixin, PhysiologicalObservation]

  AWAREAppObservation:
    is_a: AppForegroundEvent        # from cytos/context.yaml
    mixins: [AWAREObservationMixin, PhysiologicalObservation]

  AWARENotificationObservation:
    is_a: NotificationEvent         # from cytos/context.yaml
    mixins: [AWAREObservationMixin, PhysiologicalObservation]
    # text_hash is enforced by NotificationEvent; raw text is forbidden

  AWAREKeyboardObservation:
    is_a: KeyboardEvent             # from cytos/context.yaml
    mixins: [AWAREObservationMixin, PhysiologicalObservation]
    # key_count + backspace_count only; raw keystrokes are schema-prohibited

  AWARETouchObservation:
    is_a: TouchEvent                # from cytos/context.yaml
    mixins: [AWAREObservationMixin, PhysiologicalObservation]

  AWARECommunicationObservation:
    is_a: CommunicationEvent        # from cytos/context.yaml
    mixins: [AWAREObservationMixin, PhysiologicalObservation]
    # contact_hash is enforced; raw phone numbers are schema-prohibited

  AWARENetworkObservation:
    is_a: NetworkEvent              # from cytos/context.yaml
    mixins: [AWAREObservationMixin, PhysiologicalObservation]
    # ssid_hash is enforced

  AWAREWifiObservation:
    is_a: PhysiologicalObservation
    mixins: [AWAREObservationMixin]
    attributes:
      ssid_hash:   { range: string }
      bssid_hash:  { range: string }
      rssi_dbm:    { range: integer }
      frequency_mhz: { range: integer }

  AWAREBluetoothObservation:
    is_a: PhysiologicalObservation
    mixins: [AWAREObservationMixin]
    attributes:
      device_address_hash: { range: string }
      rssi_dbm: { range: integer }

  AWAREBatteryObservation:
    is_a: BatteryEvent              # from cytos/context.yaml
    mixins: [AWAREObservationMixin, PhysiologicalObservation]
```

**AWARE-specific SensorDescriptor fields** (addition for all AWARE adapters):

```yaml
# Extension mixin for AWARESensorDescriptor
classes:
  AWARESensorDescriptor:
    is_a: SensorDescriptor
    attributes:
      aware_variant:   { range: AWAREVariantEnum }   # full | light
      aware_plugin_id: { range: string }             # e.g. "com.aware.plugin.screen"
      hash_salt_ref:   { range: string }             # reference to on-device salt store; never the salt itself
```

---

### 4.3 Clinical and EMA Instruments

#### 4.3.1 Instrument-as-Sensor Model

A validated questionnaire is a CSP sensor. The `SurveyInstrument` (extending `Procedure` in cytos/selfreport.yaml) is the adapter descriptor analog. The `SurveyResponse` (extending `Observation`) is the `CSPObservation`. A completed `SurveyItemAnswer` (extending `ResultComponent`) is the `CSPResult` component.

This is not a metaphor: the CSP adapter lifecycle applies unchanged. An instrument adapter must pass through `discover`, `connect(consent_ref)`, `configure`, `observe`, and `disconnect`.

```yaml
# LinkML — instrument observation hierarchy
classes:
  InstrumentObservation:
    is_a: CSPObservation
    description: >-
      Wraps a SurveyResponse as a first-class CSP observation. The
      survey_response field contains the full structured result;
      result.scalar contains the total score for axis routing.
    attributes:
      instrument_id:    { range: string, required: true }  # e.g. "phq-9"
      survey_response:  { range: SurveyResponse, required: true }
      safety_flag:      { range: boolean }   # true if crisis-relevant item elevated
      # Inherits axis_ref, consent_ref, privacy_tier, etc. from CSPObservation

  ESMSurveyResponse:
    is_a: SurveyResponse
    description: SurveyResponse with AWARE ESM trigger metadata.
    attributes:
      trigger:            { range: ESMTriggerEnum }
      trigger_definition: { range: string }
      response_latency_s: { range: float }   # seconds from prompt to completion
```

**Privacy rules for instruments:**

- Raw item responses: `clinician_gated`. They cross the boundary only when a clinician integration is active and consented (BAA required).
- Total and subscale scores: `boundary_derived`. These may cross the boundary under standard consent.
- Any item flagging safety concern (PHQ-9 item 9, or any direct suicidal ideation screen): `clinician_gated` regardless of overall score. This also fires the crisis-detection hook (see `MODULE-crisis-detection.md`).

#### 4.3.2 Instrument Catalog Binding

| Instrument | LOINC Panel | CSP axis populated | Safety flag |
|---|---|---|---|
| PHQ-9 | 44249-1 | `yar.instrument.phq9_score` | Item 9 > 0 |
| PHQ-2 (screen) | 55757-9 | `yar.instrument.phq9_score` (partial) | No; triggers full PHQ-9 |
| GAD-7 | 69737-5 | `yar.instrument.gad7_score` | No (see crisis module for acute anxiety) |
| GAD-2 (screen) | 69725-0 | `yar.instrument.gad7_score` (partial) | No; triggers full GAD-7 |
| ASRS v1.1 | 73633-9 | `yar.instrument.asrs_parta_score` | No |
| WFIRS | — | user-defined domain axes | No |
| BRIEF-A (licensed) | — | user-defined executive function axes | No |
| PSQI | 95653-4 | `yar.instrument.psqi_global` | No |
| AWARE ESM (custom) | — | user-defined or standard axes | Depends on item content |

**Adaptive screening logic (built into adapter, not user-visible):**

- PHQ-2 score ≥ 3 automatically schedules full PHQ-9 at next ESM window.
- GAD-2 score ≥ 3 automatically schedules full GAD-7 at next ESM window.
- ASRS Part A screener: positive result (≥ 4 shaded items) flags for consideration of ASRS Part B in next scheduled session.

#### 4.3.3 ESM Trigger Types

| Trigger | `ESMTriggerEnum` value | Typical use |
|---|---|---|
| Fixed schedule | `scheduled` | Morning check-in, evening review |
| Random within window | `random_within_window` | EMA bias reduction |
| Location entry/exit | `location_based` | Context-specific assessments |
| Activity transition | `activity_based` | Post-exercise mood capture |
| Sensor threshold | `sensor_threshold` | Elevated screen time, poor sleep signal |
| App event | `app_event` | Post-social-media reflection |
| User initiated | `user_initiated` | On-demand self-report |

---

### 4.4 ND-Relevant Derived Features

These features are derived on-device from raw sensor signals. They are `boundary_derived` and map to registered CSP axes. They carry direct clinical and behavioral relevance for neurodivergent individuals.

| Derived feature | Source signals | axis_id | ND relevance |
|---|---|---|---|
| **Circadian stability score** | Sleep onset time variability, first screen-on time, ambient light morning exposure | user.circadian_stability | ADHD circadian phase delay tracking |
| **Autonomic regulation index** | HRV RMSSD 7-day trend, HRV HF/LF ratio | `yar.physio.hrv_rmssd` + `yar.physio.hrv_hf` | Vagal tone, executive function readiness |
| **Sleep architecture quality** | Deep sleep %, REM %, sleep latency, SpO2 during sleep | `yar.physio.sleep_efficiency` + `yar.physio.sleep_deep_duration` | ADHD sleep fragmentation detection |
| **Attentional fragmentation index** | Screen unlock rate, app switch rate, notification rate | `yar.aware.screen_unlock_rate` + `yar.aware.app_switch_rate` | Proxy for attentional instability |
| **Behavioral routine regularity** | Location entropy, activity state consistency, sleep-wake consistency | `yar.aware.location_entropy` | Autism/ADHD routine tracking |
| **Social rhythm metric** | Call duration, contact diversity (hashed), communication timing | `yar.aware.call_duration_daily` (**DEPRECATED** — use `yar.social.call_duration_total_daily` from SPEC-sensor-social-interaction.md) | Mood disorder social rhythm therapy support |
| **Physical capacity estimate** | Step count trend, active zone minutes, readiness score | `yar.physio.readiness_score` + `yar.physio.step_count` | Activity-capacity correlation for executive load |
| **Light-circadian alignment** | Ambient light lux at morning/evening + screen-on patterns | `yar.aware.ambient_light` | Circadian rhythm disruption flag |

**NDSignalFlagEnum values:** `hyperfocus_candidate | attentional_fragmentation | circadian_misalignment | elevated_autonomic_load | low_sleep_efficiency | social_withdrawal | behavioral_routine_disruption`. These flags are set on the `PhysiologicalObservation.nd_signal_flags` field. They are `boundary_derived` and never carry diagnostic labels.

---

## 5. Privacy and Governance

### 5.1 CrossBoundarySignal Classification

Every axis produced by this spec is a `CrossBoundarySignal`. The classification follows `privacy-boundary-spec.md` Section 3.

| Signal category | Privacy tier | What may cross | CAP primitive |
|---|---|---|---|
| Wearable daily summaries (HR, HRV, sleep scores, steps) | `boundary_derived` | Scalar values and coded results | `Directive` with scope `wearable.summary.read` |
| Wearable raw waveforms (PPG, intraday HR epochs, epoch-level sleep stages) | `on_device_only` | Nothing | N/A |
| AWARE derived scalars (unlock rate, app-switch rate, location entropy) | `boundary_derived` | Scalar values | `Directive` with scope `aware.derived.read` |
| AWARE raw sensor streams (IMU, GPS coordinates, raw app lists) | `on_device_only` | Nothing | N/A |
| AWARE hashed identifiers (contact_hash, ssid_hash, bssid_hash) | `on_device_only` | Nothing (hashes are not portable outside this device) | N/A |
| Instrument total and subscale scores | `boundary_derived` | Scalar scores | `Directive` with scope `instrument.score.read` |
| Instrument raw item responses | `clinician_gated` | Only under active clinician consent + BAA | `Directive` with scope `instrument.item.read`, requires BAA flag |
| Safety-flagged item responses | `clinician_gated` | Only under clinician consent; also triggers crisis module | `Directive` + `GuardDecision` with `safety_flag=true` |

### 5.2 On-Device-First Defaults

All adapters in this spec default to `on_device_only` at install time. The user must explicitly upgrade each data type to `boundary_derived` or `clinician_gated`.

Upgrade flow:
1. User navigates to adapter settings.
2. CAP PEP issues a `Directive` requesting scope upgrade.
3. User confirms; `GuardDecision` is `allow_with_constraints`.
4. `DecisionRecord` is written to the local audit log.
5. Subsequent observations at the upgraded tier are permitted to cross the boundary.

Downgrade (revocation) is immediate and takes effect within one session per CSP lifecycle rule (PB-8).

### 5.3 Consent Scope Controlled Vocabulary

This spec defines the consent scope names for all adapters. These names resolve the open item O-4 from SPEC-CSP for this modality.

| Scope name | Adapter | Data covered |
|---|---|---|
| `oura.sleep` | Oura | Sleep sessions, stages, latency, efficiency |
| `oura.heartrate` | Oura | Heart rate, HRV, readiness |
| `oura.activity` | Oura | Steps, active calories, activity score |
| `oura.temperature` | Oura | Skin temperature deviation |
| `fitbit.heartrate` | Fitbit | Heart rate, HRV (RMSSD/LF/HF), resting HR, stress score |
| `fitbit.sleep` | Fitbit | Sleep sessions, stages, sleep score |
| `fitbit.activity` | Fitbit | Steps, active zone minutes, activity minutes |
| `fitbit.temperature` | Fitbit | Skin/wrist temperature |
| `fitbit.respiratory_rate` | Fitbit | Respiratory rate per sleep stage |
| `fitbit.oxygen_saturation` | Fitbit | SpO2 |
| `aware.motion` | AWARE | Accelerometer, gyroscope, magnetometer (raw = `on_device_only`) |
| `aware.activity` | AWARE | Activity recognition events |
| `aware.environment` | AWARE | Light, barometer, temperature, proximity |
| `aware.location` | AWARE | Location (raw = `on_device_only`; entropy = `boundary_derived`) |
| `aware.screen` | AWARE | Screen state events |
| `aware.applications` | AWARE | App foreground events |
| `aware.communication` | AWARE | Call/SMS metadata (hashed identifiers only) |
| `aware.keyboard` | AWARE | Keystroke counts (never raw keystrokes) |
| `aware.derived` | AWARE | Cross-sensor derived scalars (attentional fragmentation, etc.) |
| `instrument.score.read` | All instruments | Total and subscale scores |
| `instrument.item.read` | All instruments | Raw item responses (requires BAA for clinical instruments) |

---

## 6. Storage: CRDT Op-Log Representation

All observations from this spec are CRDT operations appended to the op-log (Layer 2 of the data fabric per SPEC-storage-engine.md). Adapters do not write directly to the graph index (Layer 4).

### 6.1 Op-Log Entry Format

```yaml
# Normative CRDT op-log entry for a PhysiologicalObservation
op_id: "crdt:op/oura-hrv-20260622T023000Z"
op_type: append            # never update, never delete
vector_clock: {...}        # Loro/any-sync CRDT vector clock (per SPEC-sync-protocol.md)
payload_type: CSPObservation
payload:
  observation_id: "oura-hrv-20260622T023000Z"
  adapter_id: "org.cytognosis.yar.oura"
  axis_ref:
    axis_id: yar.physio.hrv_rmssd
    axis_label: "HRV (RMSSD)"
    domain: autonomic_regulation
    value_type: continuous
    unit: ms
  timestamp: "2026-06-22T02:30:00Z"
  result:
    scalar: 45.2
  provenance:
    source_device: "oura-ring-gen4-abc123"
    collection_method: passive
    raw_data_location: "/on-device/oura/raw/hrv/20260622T0230.bin"
  consent_ref: "consent:grant/oura.heartrate/abc"
  privacy_tier: boundary_derived
  unit: ms
  quality_flags: []
```

### 6.2 AWARE Derived Scalar Example

Raw AWARE IMU samples are `on_device_only` and are summarized into derived scalars before any op-log write.

```yaml
# CRDT op-log entry: attentional fragmentation index (derived from screen + app events)
op_id: "crdt:op/aware-attn-frag-20260622T170000Z"
op_type: append
payload_type: CSPObservation
payload:
  observation_id: "aware-attn-frag-20260622T170000Z"
  adapter_id: "org.cytognosis.yar.aware.screen"
  axis_ref:
    axis_id: yar.aware.screen_unlock_rate
    axis_label: "Screen unlock rate"
    domain: digital_behavior
    value_type: continuous
    unit: /h
  timestamp: "2026-06-22T17:00:00Z"
  result:
    scalar: 14.3     # unlocks per hour, derived from raw screen events
  provenance:
    source_device: "pixel8-abc"
    collection_method: passive
    raw_data_location: "/on-device/aware/screen/20260622.db"
  consent_ref: "consent:grant/aware.screen/xyz"
  privacy_tier: boundary_derived
  unit: /h
  quality_flags: []
```

### 6.3 Instrument Score Example

```yaml
# CRDT op-log entry: PHQ-9 total score
op_id: "crdt:op/phq9-resp-20260622T091500Z"
op_type: append
payload_type: InstrumentObservation
payload:
  observation_id: "phq9-resp-20260622T091500Z"
  adapter_id: "org.cytognosis.yar.instrument.phq"
  axis_ref:
    axis_id: yar.instrument.phq9_score
    axis_label: "Depression severity (PHQ-9)"
    domain: mood_distress
    value_type: continuous
    unit: "{score}"
    biolink_class: biolink:PhenotypicFeature
  timestamp: "2026-06-22T09:15:00Z"
  result:
    scalar: 14.0
    coded_value: "loinc:44261-6"
  consent_ref: "consent:grant/instrument.score.read/abc"
  privacy_tier: boundary_derived    # total score; item responses remain clinician_gated
  instrument_id: "phq-9"
  safety_flag: false
  quality_flags: []
  # Raw item responses stored separately at clinician_gated tier; referenced not embedded
  survey_response:
    id: "sensor:response/phq9/20260622T091500Z"
    privacy_tier: clinician_gated
    raw_data_location: "/on-device/instruments/phq9/resp-20260622.json"
```

---

## 7. Conformance and Acceptance Criteria

The following EARS-style requirements govern all adapters defined in this spec. Requirements are organized by adapter class.

### 7.1 All Adapters

- **REQ-PHYS-001**: The system shall reject any `PhysiologicalObservation` that does not carry an active `consent_ref` matching the adapter's declared consent scopes.
- **REQ-PHYS-002**: The system shall write every accepted `PhysiologicalObservation` to the CRDT op-log as an `append` operation before acknowledging acceptance to the adapter.
- **REQ-PHYS-003**: The system shall enforce `on_device_only` privacy tier at the CAP PEP: raw PPG waveforms, raw IMU samples, raw GPS coordinates, and raw notification text must never be serialized to any network-bound buffer.
- **REQ-PHYS-004**: When a consent grant is withdrawn, the system shall stop accepting observations from the affected adapter within one session and shall not queue pending observations.
- **REQ-PHYS-005**: The system shall record a `DecisionRecord` in the local audit log for every consent check, regardless of outcome.

### 7.2 Wearable Adapters

- **REQ-WEAR-001**: The Oura adapter shall poll daily summaries no more than once per hour and shall use webhook callbacks for event-driven updates when available.
- **REQ-WEAR-002**: The Fitbit adapter shall enforce the 150-requests-per-hour rate limit with a 5-request safety buffer and shall wait for the rate limit reset rather than dropping observations silently.
- **REQ-WEAR-003**: When both Oura and Fitbit are connected, the system shall write both observations to the same axis and tag each with its source `adapter_id` in `CSPProvenance.source_device`.
- **REQ-WEAR-004**: Raw waveform data (PPG, intraday heart rate below 5-minute resolution) shall be referenced by `waveform_ref` to an encrypted on-device blob. The blob shall never be serialized as an inline field on the op-log entry.

### 7.3 AWARE Passive Adapters

- **REQ-AWARE-001**: The AWARE adapter shall hash all contact identifiers, SSIDs, BSSIDs, and Bluetooth device addresses with SHA-256 and a per-device salt before persisting any observation. Unhashed identifiers shall not appear in any persisted field.
- **REQ-AWARE-002**: The keyboard adapter shall record counts only (`key_count`, `backspace_count`). The system shall reject any observation that includes raw keystroke content.
- **REQ-AWARE-003**: Raw GPS coordinates in `AWARELocationObservation` shall be `privacy_tier: on_device_only`. The only boundary-crossable location signal shall be derived scalars (location entropy) on separately registered axes.
- **REQ-AWARE-004**: When activity recognition reports "still" for 5 or more consecutive minutes, IMU sampling rates shall reduce to the low-power schedule automatically.
- **REQ-AWARE-005**: The system shall not transmit any AWARE-derived observation that includes a `waveform_ref` or a raw AWARE SQLite table reference in a network-bound payload.

### 7.4 Instrument Adapters

- **REQ-INST-001**: The system shall store raw item responses at `privacy_tier: clinician_gated`. Total and subscale scores shall be stored at `privacy_tier: boundary_derived`. These must not be co-mingled in a single `CSPObservation` payload.
- **REQ-INST-002**: When PHQ-9 item 9 returns a value > 0, the system shall set `InstrumentObservation.safety_flag = true` and shall invoke the crisis-detection module hook within the same session.
- **REQ-INST-003**: The PHQ-2 and GAD-2 screening adapters shall schedule the full PHQ-9 or GAD-7 at the next available ESM window when the screening threshold is met (PHQ-2 ≥ 3; GAD-2 ≥ 3).
- **REQ-INST-004**: BRIEF-A and CAARS (proprietary instruments) shall require an active licensing verification token in the adapter `configure` phase. Connection shall fail if the token is absent or expired.
- **REQ-INST-005**: ESM prompts shall honor the `expiration_seconds` field: if the user does not respond within the expiration window, the adapter shall emit a `quality_flag: response_expired` observation rather than a missing observation.

---

## 8. Open Questions and Future Modalities

| # | Question | Current leaning | Blocker |
|---|---|---|---|
| O-1 | Cross-vendor HRV axis aggregation (Oura RMSSD vs. Fitbit RMSSD: same axis or separate?) | Single axis `yar.physio.hrv_rmssd` with `adapter_id` provenance; aggregation logic deferred | Resolve in `SPEC-neurobehavioral-axes.md` (CSP O-8) |
| O-2 | Apple HealthKit adapter schema finalization | Implement once HealthKit FHIR export API is confirmed stable; scope to include menstrual data | Apple API stability; coordinate with `SPEC-sensor-menstrual.md` |
| O-3 | Encrypted on-device blob store for raw waveforms (`waveform_ref`) | iroh-blobs (Loro+Iroh path) or any-sync-filenode; decision follows SPEC-sync-protocol.md O-1 and O-4 | Sync protocol decision |
| O-4 | OMOP CDM mapping for instrument scores | Add alongside the clinician-path scope (BAA pathway) | Legal posture decision on HIPAA; assign to clinician integration spec |
| O-5 | Dexcom CGM adapter (continuous glucose) | Schema stub exists (`vendor_dexcom.yaml`); high value for metabolic-mood correlation | Not prioritized until menstrual + metabolic track opens |
| O-6 | Mira fertility adapter | Schema stub exists (`vendor_mira.yaml`); coordinate with `SPEC-sensor-menstrual.md` | Blocked on menstrual spec |
| O-7 | Location-entropy computation: server-side vs. on-device | On-device preferred (raw GPS never leaves); requires on-device entropy library | Engineering effort estimate needed |
| O-8 | CAARS and BRIEF-A licensing token infrastructure | Define a license-token service; could be lightweight API check or embedded JWT | Legal; PAR/MHS licensing terms |
| O-9 | AWARE-Light vs. AWARE Full feature parity at ingestion | Normalize at adapter level; no schema difference | Engineering implementation detail |
| O-10 | Consent scope granularity for AWARE ESM triggers | Single `aware.esm` scope vs. per-trigger-type scope | Depends on final consent UX design |

---

## 9. Cross-References

| Document | Relationship |
|---|---|
| `Yar/spec/SPEC-CSP.md` | Anchor protocol; all adapter classes, lifecycle phases, and schema types defined there apply here |
| `Cytoplex/spec/privacy-boundary-spec.md` | Privacy tier classification and CrossBoundarySignal schema; PB-1 through PB-10 apply |
| `Cytoplex/spec/03_primitives.md` | CAP primitive types: `Directive`, `GuardDecision`, `DecisionRecord` |
| `Yar/spec/SPEC-storage-engine.md` | CRDT op-log (L2); graph index (L4); op-log entry format |
| `Yar/spec/SPEC-sync-protocol.md` | L2 CRDT replication; L6 consent layer |
| `04-Engineering/cytos/sensing-schema/unified-sensor-report.md` | Authoritative Cytos LinkML schema; vendor profiles |
| `04-Engineering/yar/sensors/implementing-wearables.md` | Oura and Fitbit implementation detail (API, Python adapter code, LOINC codes) |
| `04-Engineering/yar/sensors/implementing-aware.md` | AWARE adapter implementation (Python, SQLite, privacy gate) |
| `04-Engineering/yar/sensors/implementing-health-instruments.md` | Full instrument item text, scoring algorithms, FHIR LOINC codes |
| `MODULE-crisis-detection.md` | Crisis-detection module; triggered by `InstrumentObservation.safety_flag = true` |
| `SPEC-sensor-speech-mentalstate.md` (planned) | Extends CSP for voice signals; companion spec |
| `SPEC-sensor-menstrual.md` (planned) | Extends CSP for menstrual and fertility signals; includes HealthKit scope |
| `SPEC-sensor-social-interaction.md` (planned) | Extends AWARE communication/location primitives for social rhythm |
| `SPEC-neurobehavioral-axes.md` (planned) | Defines how CSP axis outputs from this spec combine into longitudinal neurobehavioral axis scores |
