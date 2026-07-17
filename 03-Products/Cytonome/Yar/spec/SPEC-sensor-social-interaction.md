---
spec_id: SPEC-sensor-social-interaction
version: "0.1"
status: draft
domain: sensor-social-interaction
owner: Shahin Mohammadi
created: 2026-06-22
last_updated: 2026-06-22
depends_on: [SPEC-CSP, SPEC-storage-engine, SPEC-sensor-physiological]
implements: [CSP]
---

# SPEC-sensor-social-interaction: Temporal Social-Interaction Sensing

> **Reading options:** An ADHD-friendly progressive-disclosure rendering is generated from this file. The hand-maintained ADHD twin (`spec/adhd/SPEC-sensor-social-interaction_adhd.md`) was retired 2026-07-16; see `_archive/cleanup_2026-07-16/adhd-twins/`.

> **Status**: Draft
> **Date**: 2026-06-22
> **Author**: Cytognosis Foundation
> **Audience**: engineers
> **Tags**: `yar`, `cytonome`, `csp`, `sensor`, `social-interaction`, `social-rhythm`, `aware`, `digital-phenotyping`
> **Related:** [SPEC-CSP](./SPEC-CSP.md); [SPEC-sensor-physiological](./SPEC-sensor-physiological.md); privacy boundary at `Cytoplex/spec/privacy-boundary-spec.md`; storage engine at `./SPEC-storage-engine.md`

---

**Reading time**: ~14 minutes.
**If you only read one thing**: Section 4 (CSP binding and LinkML classes) and Section 5 (social-rhythm modeling). This spec extends the AWARE communication and Bluetooth co-presence primitives from SPEC-sensor-physiological into a dedicated social-interaction adapter layer with derived rhythm metrics, diversity indices, and mood/energy contextual covariates.

**BLUF**: Social withdrawal and social rhythm disruption are established behavioral markers for mood disorders, bipolar disorder, and neurodivergent presentations. Yar passively captures the rhythm and quantity of social contact (not content) from AWARE communication logs, Bluetooth co-presence, and location overlap. Derived metrics (social-rhythm regularity, interaction diversity, co-presence index) feed mood and energy axes as contextual covariates. All contact identifiers are pseudonymized on-device; no contact graph leaves the device.

> **Implementation status**: Design-only, not yet implemented. No social-interaction sensor adapter code was found in any Cytognosis repo at the time of the June 2026 codebase sweep (see INCORPORATION_MAP.md §8, SPEC-sensor-social-interaction row). The AWARE communication and Bluetooth primitives this spec extends (`AWARECommunicationObservation`, `AWAREBluetoothObservation`) are likewise design-only in SPEC-sensor-physiological. The SQLite-backed storage pattern (`Yar/src/yar/storage/sqlite_store.py`) and the CapLiteGuard privacy gate (`Yar/src/cap/guard.py`) are implemented and will serve as the foundation for this adapter's on-device event log and consent enforcement respectively.

---

## 1. Purpose and Scope

This spec is the formal modality-level binding for social-interaction sensing in Yar. It imports and extends the AWARE communication and proximity primitives defined in [SPEC-sensor-physiological](./SPEC-sensor-physiological.md) Section 4.2, and it defines the derived layer that converts raw interaction events into clinically meaningful rhythm metrics.

### 1.1 What This Sensor Captures

| Signal class | Examples | CSP tier |
|---|---|---|
| **Communication event metadata** | Call duration, call direction, SMS count | `boundary_derived` (hashed contact, scalar metrics) |
| **Bluetooth co-presence** | Device-detected peer count over time, RSSI-based proximity duration | `boundary_derived` (hashed addresses, duration scalars) |
| **Interaction timing regularity** | Time-of-day distribution of calls, weekly rhythm deviation | `boundary_derived` |
| **Contact diversity** | Count of unique hashed contacts over a window | `boundary_derived` |
| **Social rhythm index** | Composite regularity score derived on-device | `boundary_derived` |
| **Co-presence sessions** | Duration of Bluetooth-inferred proximity events with any device | `boundary_derived` |

### 1.2 What This Sensor Does NOT Capture

The following are strictly outside the scope of this spec and are prohibited at the schema level:

- Call or message **content** of any kind.
- Message text, subject lines, or notification text (hashing at the `NotificationEvent` layer already enforces this in SPEC-sensor-physiological).
- **Identity** of contacts: names, phone numbers, and contact-book entries never appear in persisted fields. Only stable, salted, per-device SHA-256 hashes are permitted.
- **Contact graph egress**: the set of hashed contacts, and any structure derived from it (frequency matrix, contact pairs, network topology), never leaves the device under any consent scope.
- Inference about **who** the user is with or communicating with.
- Eavesdropping, ambient audio, or any acoustic signal. This spec is metadata-only.

These prohibitions are enforced at the schema field level, at the CAP PEP, and in the CrossBoundarySignal classifications in Section 6.

### 1.3 Clinical and Behavioral Rationale

**Social zeitgeber theory** proposes that social contacts and routines entrain circadian rhythms. Disruption of these cues can dis-entrain circadian timing, increasing risk of mood episodes (Frank et al., 1994; Grandin et al., 2006). The **Social Rhythm Metric (SRM)**, originally a clinician-administered diary instrument (Monk et al., 1991), quantifies how regularly a person performs daily activities including social contacts. Lower SRM scores correlate with increased mood-episode risk in bipolar disorder (Monk et al., 1991; Ehlers et al., 1993).

Passive smartphone sensing can approximate the SRM from communication metadata and co-presence signals. A 2016 study (Canzian et al., JAMIA) demonstrated that passively-sensed communication frequency, location, and non-stationary duration predicted SRM scores with RMSE of 1.40 (range 0-7), and that classifiers achieved 0.85 precision and 0.86 recall for distinguishing stable from unstable states.

A 2018 smartphone-based SRM study (Faurholt-Jepsen et al., PMC) validated the feasibility of app-based social rhythm tracking in bipolar disorder, showing significant correlations between app-logged SRM and clinical ratings.

For ADHD and autism presentations, routine regularity (including social routine) is a meaningful behavioral dimension. Social withdrawal is also a documented feature of depressive episodes and autistic burnout that passive sensing can detect weeks before clinical presentation (Onnela and Rauch, 2016; Mohr et al., 2017).

---

## 2. Source Primitives

This spec does not redefine AWARE primitives. It references and extends the classes already bound in SPEC-sensor-physiological Section 4.2.

### 2.1 AWARE Primitives Used (Reference Only)

| Primitive | Defined in | Social-interaction role |
|---|---|---|
| `AWARECommunicationObservation` (extends `CommunicationEvent`) | SPEC-sensor-physiological §4.2 | Per-event call/SMS metadata: duration, direction, `contact_hash` |
| `AWAREBluetoothObservation` | SPEC-sensor-physiological §4.2 | Per-scan Bluetooth peer detection: `device_address_hash`, RSSI |
| `AWARELocationObservation` (extends `LocationFix`) | SPEC-sensor-physiological §4.2 | Co-location inference (on-device only; raw coords never cross boundary) |
| `AWAREScreenObservation` (extends `ScreenEvent`) | SPEC-sensor-physiological §4.2 | Screen-on timing used to gate communication event windows |
| `AWAREActivityObservation` (extends `ActivityRecognitionEvent`) | SPEC-sensor-physiological §4.2 | Activity context for social events (e.g., "in vehicle" during call) |

These classes are consumed as input events by the social-interaction aggregation pipeline. They are not re-emitted; only derived `SocialInteractionObservation` subclasses enter the CSP op-log under this spec.

### 2.2 AWARE Adapter IDs in Use

| Adapter ID | Scope |
|---|---|
| `org.cytognosis.yar.aware.communication` | Call/SMS metadata |
| `org.cytognosis.yar.aware.bluetooth` | Co-presence proximity |
| `org.cytognosis.yar.aware.location` | Co-location (on-device only) |

These adapters are registered and governed under SPEC-sensor-physiological. This spec adds a **derived-observation layer** on top of them using the adapter ID `org.cytognosis.yar.social_interaction`.

---

## 3. Adapter Inventory

A single social-interaction adapter aggregates the AWARE primitives listed above into derived observations. It does not poll hardware directly; it subscribes to the AWARE event bus via the `AWAREAggregatorMixin` pattern.

| Adapter ID | CSP Adapter Class | Maturity | Privacy Tier | Feature Refs |
|---|---|---|---|---|
| `org.cytognosis.yar.social_interaction` | `passive_digital_phenotyping` | Research | `boundary_derived` (derived scalars, counts); `on_device_only` (contact hashes, graph structure) | CSP §6.5 |

**SensorDescriptor (normative YAML):**

```yaml
adapter_id: org.cytognosis.yar.social_interaction
display_name: "Social Interaction Patterns"
adapter_class: passive_digital_phenotyping
maturity: research
modalities: [social_engagement, behavioral_regularity]
axes_produced:
  - yar.social.call_volume_daily
  - yar.social.call_duration_total_daily
  - yar.social.sms_volume_daily
  - yar.social.outgoing_ratio
  - yar.social.contact_diversity_7d
  - yar.social.copresence_duration_daily
  - yar.social.copresence_peer_count_daily
  - yar.social.social_rhythm_score
  - yar.social.social_rhythm_deviation
  - yar.social.interaction_timing_entropy
  - yar.social.social_contact_index
  - yar.social.social_withdrawal_flag
privacy_tier: boundary_derived   # derived scalars only; hashes and graph structure are on_device_only
requires_consent: [aware.communication, aware.bluetooth, social.derived]
schema_ref: "cytos/schemas/domains/sensor/vendors/vendor_social_interaction.yaml"
implementation_ref: "04-Engineering/yar/sensors/implementing-aware.md"
upstream_adapters:
  - org.cytognosis.yar.aware.communication
  - org.cytognosis.yar.aware.bluetooth
  - org.cytognosis.yar.aware.location
```

---

## 4. CSP Binding and LinkML Classes

### 4.1 Inheritance Chain

```
sosa:Observation
  └── CSPObservation                                  (SPEC-CSP §4.1)
        └── PhysiologicalObservation                 (SPEC-sensor-physiological §3.3)
              └── PassiveDigitalPhenotypingObservation (SPEC-sensor-physiological §4.2)
                    └── SocialInteractionObservation  (THIS SPEC §4.2)
                          ├── CommunicationSummaryObs  (§4.3)
                          ├── CoPresenceSessionObs     (§4.4)
                          ├── SocialRhythmMetricObs    (§4.5)
                          └── SocialContactSummaryObs  (§4.6)
```

All classes inherit `CSPObservation` fields: `observation_id`, `adapter_id`, `axis_ref`, `timestamp`, `result`, `provenance`, `consent_ref`, `privacy_tier`, `unit`, `quality_flags`.

### 4.2 SocialInteractionObservation Base Class

```yaml
# LinkML (normative field names; inherits all PhysiologicalObservation fields)
classes:
  SocialInteractionObservation:
    is_a: PassiveDigitalPhenotypingObservation
    description: >-
      Base class for all social-interaction-derived observations.
      Captures temporal and quantitative patterns of social contact without
      content, identity, or contact-graph structure. All contact identifiers
      are pseudonymized on-device before this class is instantiated.
    attributes:
      window_start:
        range: datetime
        required: true
        description: Start of the aggregation window (UTC).
      window_end:
        range: datetime
        required: true
        description: End of the aggregation window (UTC).
      window_type:
        range: WindowTypeEnum
        required: true
        description: >-
          Granularity of the aggregation window.
          # WindowTypeEnum: hourly | daily | rolling_7d | rolling_30d
      contact_diversity_hash_count:
        range: integer
        description: >-
          Count of unique contact_hash values observed in the window.
          This count is on_device_only; it is used in derived metrics but
          is not emitted as a boundary_derived field directly.
          The derived ContactDiversityObs carries only the count scalar.
      social_context_flags:
        range: SocialContextFlagEnum
        multivalued: true
        description: >-
          Non-diagnostic behavioral flags set on this observation.
          # SocialContextFlagEnum: reduced_call_volume | elevated_call_volume |
          # irregular_timing | low_contact_diversity | high_copresence |
          # low_copresence | rhythm_disruption | baseline_insufficient
```

### 4.3 CommunicationSummaryObs

Aggregates per-event `CommunicationEvent` primitives into windowed summaries. Emitted once per `window_type` per adapter run.

```yaml
classes:
  CommunicationSummaryObs:
    is_a: SocialInteractionObservation
    description: >-
      Windowed summary of call and SMS event metadata. All contact
      identifiers are excluded; only aggregate counts and durations appear.
    attributes:
      call_count:
        range: integer
        description: Total call events (incoming + outgoing + missed) in window.
      call_duration_total_s:
        range: float
        description: Total duration of completed calls in seconds.
      call_duration_mean_s:
        range: float
        description: Mean duration of completed calls in seconds.
      incoming_call_count:
        range: integer
      outgoing_call_count:
        range: integer
      missed_call_count:
        range: integer
      sms_count:
        range: integer
        description: Total SMS/MMS events (sent + received) in window.
      outgoing_ratio:
        range: float
        description: >-
          Fraction of total communication events that are outgoing.
          Range 0.0-1.0. A proxy for social initiative.
      call_timing_hours:
        range: float
        multivalued: true
        description: >-
          Hour-of-day (0-23, float for sub-hour precision) for each call event.
          Used for on-device rhythm modeling only; this list is on_device_only.
          The derived interaction_timing_entropy scalar is boundary_derived.
```

**Privacy invariant:** `call_timing_hours` is `on_device_only` (raw timing list). Only the derived `interaction_timing_entropy` scalar crosses the boundary.

### 4.4 CoPresenceSessionObs

Derived from Bluetooth scan events. A co-presence session is a contiguous window during which one or more Bluetooth peers are detected within RSSI threshold, interpreted as physical proximity.

```yaml
classes:
  CoPresenceSessionObs:
    is_a: SocialInteractionObservation
    description: >-
      A proximity-inferred co-presence session derived from Bluetooth
      scan events. Captures duration and peer count only. Device addresses
      are hashed and never included in boundary_derived fields.
    attributes:
      session_duration_s:
        range: float
        description: Duration of the inferred co-presence session in seconds.
      max_peer_count:
        range: integer
        description: >-
          Maximum number of simultaneously detected Bluetooth peers
          during the session. Peers are hashed devices; count is the
          boundary-crossable scalar.
      mean_rssi_dbm:
        range: float
        description: >-
          Mean RSSI (dBm) of all detected peers during the session.
          Proxy for physical proximity distance.
      rssi_threshold_dbm:
        range: float
        description: RSSI threshold used to define proximity (default -75 dBm).
      inferred_setting:
        range: InferredSettingEnum
        description: >-
          On-device contextual inference of the social setting (heuristic only).
          # InferredSettingEnum: home_network | commute | public_space |
          # office_network | unknown
          Derived from WiFi network hash match against known networks;
          never discloses raw location or network identity.
```

**Privacy invariant:** Peer device addresses are not included in this class. `max_peer_count` is the only peer-related boundary-derived field. `inferred_setting` uses WiFi hash matching against a user-defined local mapping; the mapping stays on-device.

### 4.5 SocialRhythmMetricObs

The core rhythm-regularity observation. Computed on-device over a rolling window. Based on the Social Rhythm Metric (SRM; Monk et al., 1991) and its passive-sensing approximation (Canzian et al., 2016).

```yaml
classes:
  SocialRhythmMetricObs:
    is_a: SocialInteractionObservation
    description: >-
      On-device approximation of social rhythm regularity derived from
      communication timing and co-presence patterns. Provides the
      primary contextual covariate for mood and energy axes.
    attributes:
      srm_score:
        range: float
        description: >-
          Social rhythm regularity score (0.0-7.0 scale, matching the
          clinical SRM range). Higher scores indicate greater regularity.
          Derived from call timing entropy, daily interaction window
          consistency, and co-presence session timing.
      srm_deviation:
        range: float
        description: >-
          Deviation of the current srm_score from the user's rolling
          28-day baseline. Positive values indicate above-baseline regularity;
          negative values indicate reduced regularity relative to baseline.
          Expressed in SRM units.
      baseline_window_days:
        range: integer
        description: Length of the rolling baseline window in days (default 28).
      baseline_sufficient:
        range: boolean
        description: >-
          True if the baseline window contains enough data to compute a
          reliable baseline (at least 7 days of valid observations).
          Set to false during onboarding or after data gaps.
      interaction_timing_entropy:
        range: float
        description: >-
          Shannon entropy (bits) of the hourly distribution of communication
          events over the window. Low entropy = concentrated at regular times
          (high rhythm); high entropy = scattered across hours (low rhythm).
      social_rhythm_trend:
        range: SocialRhythmTrendEnum
        description: >-
          Direction of srm_deviation over the past 7 days.
          # SocialRhythmTrendEnum: increasing | stable | decreasing | insufficient_data
      circadian_anchor_hour:
        range: float
        description: >-
          Hour-of-day (0-23 float) of the modal first daily social contact.
          Proxy for the social circadian anchor point. Used in downstream
          circadian alignment analysis; forward-reference SPEC-neurobehavioral-axes.md.
```

### 4.6 SocialContactSummaryObs

A daily roll-up that combines `CommunicationSummaryObs` and `CoPresenceSessionObs` into a single composite observation suitable for axis population and rhythm modeling.

```yaml
classes:
  SocialContactSummaryObs:
    is_a: SocialInteractionObservation
    description: >-
      Daily composite summary combining communication and co-presence
      signals into a single axis-compatible observation.
    attributes:
      social_contact_index:
        range: float
        description: >-
          Composite social contact intensity score (0.0-1.0). Derived from
          normalized call volume, call duration, SMS volume, and co-presence
          duration. Higher values indicate more social contact relative to
          the user's baseline. Normalized against a 28-day rolling baseline.
      contact_diversity_index:
        range: float
        description: >-
          Diversity of social contacts in the window (0.0-1.0). Derived from
          the count of unique hashed contact identifiers, normalized against
          the user's rolling baseline. The raw hash-count is on_device_only;
          only this normalized scalar is boundary_derived.
      copresence_duration_daily_s:
        range: float
        description: Total co-presence session duration (seconds) in the window.
      copresence_peer_count_max:
        range: integer
        description: Maximum peer count observed in any single session during the window.
      communication_active_hours:
        range: integer
        description: >-
          Count of distinct clock hours containing at least one communication
          event. Proxy for the breadth of daily social engagement time.
      withdrawal_signal:
        range: WithdrawalSignalEnum
        description: >-
          Non-diagnostic signal indicating whether social contact is
          meaningfully below the user's baseline. Never uses clinical or
          diagnostic terminology in user-visible labels.
          # WithdrawalSignalEnum:
          #   none: within baseline range
          #   mild_reduction: 20-40% below 28d rolling mean
          #   moderate_reduction: 40-60% below 28d rolling mean
          #   marked_reduction: >60% below 28d rolling mean
          #   baseline_insufficient: not enough history to compute
```

**Affirming language note:** `WithdrawalSignalEnum` values are phrased as relative changes from personal baseline, not clinical states. User-visible labels are "slightly less social contact than usual," "less social contact than usual," and "notably less social contact than usual." Never "abnormal," "isolated," or "social withdrawal" as a user-facing label.

---

## 5. Axis Registry

All axes produced by this spec are registered as CSP built-in axes (namespace `yar.social.*`). Default tier is `boundary_derived` unless marked `on_device_only`.

| axis_id | axis_label | domain | value_type | unit | Biolink |
|---|---|---|---|---|---|
| `yar.social.call_volume_daily` | Daily call count | social_engagement | continuous | {count} | biolink:PhenotypicFeature |
| `yar.social.call_duration_total_daily` | Total call duration (daily) | social_engagement | continuous | s | biolink:PhenotypicFeature |
| `yar.social.sms_volume_daily` | Daily message count | social_engagement | continuous | {count} | biolink:PhenotypicFeature |
| `yar.social.outgoing_ratio` | Outgoing communication ratio | social_engagement | continuous | {ratio} | biolink:PhenotypicFeature |
| `yar.social.contact_diversity_7d` | Contact diversity (7-day) | social_engagement | continuous | {score} | biolink:PhenotypicFeature |
| `yar.social.copresence_duration_daily` | Daily co-presence duration | social_engagement | continuous | s | biolink:PhenotypicFeature |
| `yar.social.copresence_peer_count_daily` | Daily co-presence peer count | social_engagement | continuous | {count} | — |
| `yar.social.social_rhythm_score` | Social rhythm regularity | behavioral_regularity | continuous | {score} | biolink:PhenotypicFeature |
| `yar.social.social_rhythm_deviation` | Social rhythm deviation from baseline | behavioral_regularity | continuous | {delta} | biolink:PhenotypicFeature |
| `yar.social.interaction_timing_entropy` | Interaction timing entropy | behavioral_regularity | continuous | bits | — |
| `yar.social.social_contact_index` | Social contact index | social_engagement | continuous | {score} | biolink:PhenotypicFeature |
| `yar.social.social_withdrawal_flag` | Reduced social contact signal | social_engagement | categorical | — | biolink:PhenotypicFeature |

**Affirming language note:** `yar.social.social_withdrawal_flag` axis label in the user interface is "Social contact pattern" with values described as "within your usual range," "somewhat less than usual," "less than usual," and "notably less than usual." The axis ID uses technical nomenclature for internal routing only.

### 5a. Axis Registry Alignment

The table below maps each social-interaction axis to the canonical 63-axis registry name and EQ dimension facet (source: PSYCH_AXES_SYNTHESIS.md Section 5.3). Social axes are primarily contextual covariates; their EQ dimension role is noted in the "Axis role" column.

| axis_id | Canonical 63-axis registry name | Category | EQ dimension facet (OBA/ICF anchor) | Factor grouping | Axis role |
|---|---|---|---|---|---|
| `yar.social.call_volume_daily` | Social Motivation/Attachment | Social | ICF d750 (informal social relationships); RDoC Social Processes/Affiliation | Social/Interpersonal | Primary driver of `mood.anhedonia_signal` (deficit pole) |
| `yar.social.call_duration_total_daily` | Social Motivation/Attachment | Social | ICF d750; OBA social contact duration trait | Social/Interpersonal | Primary driver of `mood.anhedonia_signal`; supersedes deprecated `yar.aware.call_duration_daily` |
| `yar.social.sms_volume_daily` | Social Motivation/Attachment | Social | ICF d750 | Social/Interpersonal | Supporting driver of `mood.anhedonia_signal` |
| `yar.social.outgoing_ratio` | Approach/Reward Seeking | Behavioral | ICF b1301 (motivation); RDoC Positive Valence / Approach Motivation | Positive Affect/Reward | Proxy for social initiative / approach motivation |
| `yar.social.contact_diversity_7d` | Social Cognition/Theory of Mind + Social Motivation/Attachment | Social | ICF d750 + d760 (family relationships, broad) | Social/Interpersonal | Supporting driver of `mood.anhedonia_signal` |
| `yar.social.copresence_duration_daily` | Social Motivation/Attachment | Social | ICF d750; physical co-presence as social contact form | Social/Interpersonal | Supporting driver of `mood.anhedonia_signal` |
| `yar.social.copresence_peer_count_daily` | Social Motivation/Attachment | Social | ICF d750 (peer count proxy) | Social/Interpersonal | Environmental context for social contact intensity |
| `yar.social.social_rhythm_score` | Circadian Rhythm + Sleep Onset/Maintenance | Sleep | ICF b134 (sleep functions) + d750; Social Rhythm Metric theory (SRM; Monk et al. 1991) | Sleep/Arousal/Circadian | Type-7 (mistiming) deviation detector; covariate for whole Mood axis |
| `yar.social.social_rhythm_deviation` | Circadian Rhythm | Sleep | Same as `social_rhythm_score`; deviation magnitude | Sleep/Arousal/Circadian | Type-7 deviation magnitude covariate for `mood.activation` |
| `yar.social.interaction_timing_entropy` | Habit/Automaticity | Behavioral | ICF b147 (behavioral regularity) + d750 timing | Social/Interpersonal | Input to SRM scoring; not a direct axis driver |
| `yar.social.social_contact_index` | Social Motivation/Attachment + Anhedonia/Diminished Interest | Social + Emotional | ICF d750; RDoC Social Processes/Affiliation | Social/Interpersonal | Primary covariate for `mood.anhedonia_signal`; composite of volume and duration |
| `yar.social.social_withdrawal_flag` | Avoidance/Withdrawal | Behavioral | ICF b1301 (motivation deficit); RDoC Negative Valence / Social Withdrawal | Negative Affect | Non-diagnostic flag; secondary signal for crisis-detection module |

*Source: PSYCH_AXES_SYNTHESIS.md §3.1 (63-axis inventory) and §5.3 (social rhythm/withdrawal sensor EQ mapping).*

---

## 6. Social Rhythm Modeling

### 6.1 On-Device Computation Pipeline

The social rhythm model runs entirely on-device. No raw events, contact hashes, or timing lists are transmitted at any stage. The pipeline consists of three passes per aggregation cycle.

**Pass 1: Event ingestion (event-driven)**

The adapter subscribes to the `AWARECommunicationObservation` and `AWAREBluetoothObservation` event streams via the Yar sensor bus. Each arriving event is appended to a rolling 30-day on-device event log (SQLite, encrypted at rest). Contact hashes are already irreversible at this stage (SHA-256 with per-device salt, enforced by SPEC-sensor-physiological REQ-AWARE-001). Timing metadata (hour-of-day, day-of-week) is extracted and appended to a separate timing table.

**Pass 2: Session detection (hourly batch)**

```
Co-presence session detection:
  Input: AWAREBluetoothObservation stream
  Algorithm:
    1. Cluster Bluetooth scan events by time (gap threshold: 15 min).
    2. A session starts when ≥1 non-self device (hashed address) is
       detected with RSSI ≥ rssi_threshold_dbm (default -75 dBm).
    3. Session ends when no qualifying device appears for 15 min.
    4. Output: CoPresenceSessionObs (duration, max_peer_count,
       mean_rssi; no device addresses).

Communication window detection:
  Input: AWARECommunicationObservation stream
  Algorithm:
    1. Group events by day and clock-hour.
    2. Count unique hashed contacts per day (stored on-device only).
    3. Compute outgoing_ratio = outgoing_events / total_events.
    4. Output: CommunicationSummaryObs per daily window.
```

**Pass 3: Rhythm scoring (daily batch)**

```
Interaction timing entropy:
  H = -Σ p(h) * log2(p(h))   for each clock-hour h with ≥1 event
  where p(h) = fraction of total events occurring in hour h.
  Lower entropy = more regular timing.

SRM score approximation:
  srm_score = 7.0 * (1 - normalize(H))
  Normalized against user's 28-day entropy baseline.
  Maps H=0 (perfectly regular) → srm_score=7.0
  Maps H=max_observed → srm_score=0.0

srm_deviation:
  srm_deviation = srm_score - rolling_28d_mean(srm_score)

social_contact_index:
  sci = weighted_mean(
    w1 * norm(call_duration_total_daily),
    w2 * norm(call_volume_daily),
    w3 * norm(sms_volume_daily),
    w4 * norm(copresence_duration_daily)
  )
  Default weights: w1=0.4, w2=0.2, w3=0.1, w4=0.3
  Normalized against user's 28-day rolling mean per signal.
  All norms use a sigmoid transform capped at [0.0, 1.0].
```

Weights are user-configurable within the adapter config. The weight schema is defined in `AdapterConfig.social_interaction_weights`.

### 6.2 Baseline Bootstrapping

During onboarding (first 28 days), `baseline_sufficient = false` on all `SocialRhythmMetricObs` observations. The user interface surfaces this as "still building your personal rhythm baseline" rather than a zero or error state. The `social_withdrawal_flag` axis is set to `withdrawal_signal: baseline_insufficient` until the baseline stabilizes.

The minimum viable baseline is 7 days of valid daily observations (days with `quality_flags` containing `insufficient_data` do not count). Once the 7-day minimum is met, `baseline_sufficient` transitions to `true` and deviation metrics become active, even if the full 28-day window is not yet populated.

### 6.3 Social Rhythm as a Contextual Covariate

`SocialRhythmMetricObs` observations are contextual covariates for the mood and energy axes defined in the forthcoming `SPEC-neurobehavioral-axes.md`. The relationship is:

```
mood_axis_context = {
  ...,
  social_rhythm_score: yar.social.social_rhythm_score,
  social_rhythm_deviation: yar.social.social_rhythm_deviation,
  social_contact_index: yar.social.social_contact_index,
}
```

The social rhythm covariate is not a direct input to the mood score; it is a contextual signal that the neurobehavioral axis model (SPEC-neurobehavioral-axes.md) uses to calibrate interpretation of mood/energy observations. A user with sustained low `social_rhythm_score` whose self-reported mood also drops receives a different contextual annotation than a user whose rhythm is stable.

This forward-reference is deliberately non-prescriptive. The exact integration mechanism is assigned to SPEC-neurobehavioral-axes.md.

### 6.4 ND-Relevant Signal Flags

`SocialInteractionObservation.nd_signal_flags` (inherited from `PhysiologicalObservation`) carries these values when triggered:

| Flag (NDSignalFlagEnum) | Condition | ND relevance |
|---|---|---|
| `social_withdrawal` | `withdrawal_signal` ∈ {`moderate_reduction`, `marked_reduction`} for ≥3 consecutive days | Depression, autistic burnout, ADHD avoidance |
| `behavioral_routine_disruption` | `srm_deviation` < −1.5 for ≥2 consecutive days | Circadian dysregulation, mood prodrome |
| `low_contact_diversity` | `contact_diversity_index` < 0.2 relative to baseline for ≥5 days | Social isolation proxy; sensitive to depression and burnout |

These flags are `boundary_derived` and never carry diagnostic labels. They are inputs to the crisis-detection module hook (see `MODULE-crisis-detection.md`) only when combined with co-occurring safety signals from instrument observations.

---

## 7. Privacy and Governance

### 7.1 Third-Party Privacy

Communication and co-presence data inherently implicates **third parties** — the people the user contacts or is proximate to. These individuals have not consented to data collection by Yar. This spec addresses their privacy through the following invariants, which are non-negotiable and enforced at the schema level:

| Invariant | Enforcement mechanism |
|---|---|
| **Metadata only**: no content, text, subject, or call audio is recorded | `CommunicationEvent.contact_hash` schema enforces; `AWARECommunicationObservation` forbids content fields |
| **Contact identifier pseudonymization**: all phone numbers and contact IDs are SHA-256 hashed with a per-device, per-study salt before any persistence | SPEC-sensor-physiological REQ-AWARE-001; enforced in `PrivacyGate.hash_identifier()` |
| **No contact graph egress**: the set of contact hashes, contact pairs, or any relationship structure never crosses the privacy boundary | CrossBoundarySignal classification `on_device_only` for all hash-set fields; CAP PEP enforced |
| **No identity inference**: Yar does not attempt to re-identify contact hashes, match them to address-book entries, or cross-reference them across sessions | Schema prohibition; model inference is forbidden on hash fields |
| **Bluetooth address pseudonymization**: Bluetooth device addresses are SHA-256 hashed before any persistence | `AWAREBluetoothObservation.device_address_hash`; enforced in AWARE adapter |
| **Peer count only crosses boundary**: from co-presence sessions, only the scalar peer count (an integer) crosses the boundary | CrossBoundarySignal for `CoPresenceSessionObs`: `max_peer_count` is `boundary_derived`; `device_address_hash` set is `on_device_only` |

### 7.2 CrossBoundarySignal Classifications

Per `privacy-boundary-spec.md` Section 3 and `Cytoplex/spec/03_primitives.md`.

| Signal | Privacy tier | CAP primitive | Notes |
|---|---|---|---|
| `CommunicationSummaryObs` aggregate scalars (counts, durations, ratios) | `boundary_derived` | `Directive` scope `aware.communication` + `social.derived` | Contact hashes excluded |
| `call_timing_hours` list | `on_device_only` | N/A | Raw timing list; used only for on-device entropy computation |
| `contact_hash` values (any set or list) | `on_device_only` | N/A | Never crosses boundary under any consent scope |
| `CoPresenceSessionObs.max_peer_count`, `session_duration_s` | `boundary_derived` | `Directive` scope `aware.bluetooth` + `social.derived` | Device addresses excluded |
| `CoPresenceSessionObs.device_address_hash` (any set) | `on_device_only` | N/A | Bluetooth hash set is a contact-graph proxy; never crosses |
| `SocialRhythmMetricObs` scalars (srm_score, srm_deviation, interaction_timing_entropy) | `boundary_derived` | `Directive` scope `social.derived` | Fully derived; no raw event data |
| `SocialContactSummaryObs.social_contact_index`, `contact_diversity_index`, `withdrawal_signal` | `boundary_derived` | `Directive` scope `social.derived` | Normalized scalars and enum; no raw data |
| `inferred_setting` | `boundary_derived` | `Directive` scope `social.derived` | Heuristic categorical; WiFi hash mapping stays on-device |

### 7.3 Consent Scope Controlled Vocabulary

This spec adds the following consent scopes to the vocabulary established in SPEC-sensor-physiological Section 5.3:

| Scope name | Adapter | Data covered |
|---|---|---|
| `social.derived` | `org.cytognosis.yar.social_interaction` | All derived social-interaction scalars, rhythm scores, and composite indices |
| `aware.communication` | `org.cytognosis.yar.aware.communication` | Communication metadata (already defined in SPEC-sensor-physiological; listed here for completeness) |
| `aware.bluetooth` | `org.cytognosis.yar.aware.bluetooth` | Bluetooth co-presence data (already defined; listed for completeness) |

The `social.derived` scope is distinct from `aware.communication` and `aware.bluetooth`. A user who revokes `social.derived` stops the rhythm modeling pipeline but does not affect raw AWARE ingestion (which continues under their respective scopes). Revoking `aware.communication` or `aware.bluetooth` stops the corresponding raw adapter and, as a consequence, stops the derived social pipeline.

### 7.4 Consent and Retention

- **Default-deny**: all three scopes default to off at install. The user must opt in explicitly to each scope.
- **Granular revocation**: each scope is independently revocable per CSP lifecycle rule (PB-8); stopping within one session.
- **On-device retention**: the raw communication event log (SQLite, encrypted) retains 30 days by default. The derived observation log (op-log) retains per the SPEC-storage-engine.md retention policy. Both are purged immediately on revocation of `aware.communication` or `social.derived` respectively.
- **Third-party data**: upon revocation, all on-device contact hashes and peer-address hashes are also purged, since these represent data about third parties collected under the user's consent on their behalf.

---

## 8. Storage: CRDT Op-Log Representation

All observations from this spec are CRDT `append` operations on the op-log (L2, per SPEC-storage-engine.md). No observation from this spec is ever a direct graph write.

### 8.1 CommunicationSummaryObs Op-Log Example

```yaml
op_id: "crdt:op/social-comm-summary-20260622T000000Z"
op_type: append
vector_clock: {...}        # Loro/any-sync CRDT vector clock
payload_type: CommunicationSummaryObs
payload:
  observation_id: "social-comm-summary-20260622T000000Z"
  adapter_id: "org.cytognosis.yar.social_interaction"
  axis_ref:
    axis_id: yar.social.call_duration_total_daily
    axis_label: "Total call duration (daily)"
    domain: social_engagement
    value_type: continuous
    unit: s
    biolink_class: biolink:PhenotypicFeature
  timestamp: "2026-06-22T00:00:00Z"
  window_start: "2026-06-21T00:00:00Z"
  window_end: "2026-06-21T23:59:59Z"
  window_type: daily
  result:
    scalar: 840.0           # 14 minutes of calls
  provenance:
    source_device: "pixel9-abc"
    collection_method: passive
    raw_data_location: "/on-device/aware/communication/20260621.db"
  consent_ref: "consent:grant/aware.communication/xyz"
  privacy_tier: boundary_derived
  unit: s
  quality_flags: []
  call_count: 3
  incoming_call_count: 1
  outgoing_call_count: 2
  missed_call_count: 0
  sms_count: 12
  outgoing_ratio: 0.67
  # call_timing_hours omitted: on_device_only, not serialized to op-log
```

### 8.2 SocialRhythmMetricObs Op-Log Example

```yaml
op_id: "crdt:op/social-srm-20260622T000000Z"
op_type: append
vector_clock: {...}
payload_type: SocialRhythmMetricObs
payload:
  observation_id: "social-srm-20260622T000000Z"
  adapter_id: "org.cytognosis.yar.social_interaction"
  axis_ref:
    axis_id: yar.social.social_rhythm_score
    axis_label: "Social rhythm regularity"
    domain: behavioral_regularity
    value_type: continuous
    unit: "{score}"
    biolink_class: biolink:PhenotypicFeature
  timestamp: "2026-06-22T00:00:00Z"
  window_start: "2026-06-15T00:00:00Z"    # rolling 7-day for rhythm
  window_end: "2026-06-21T23:59:59Z"
  window_type: rolling_7d
  result:
    scalar: 4.2             # SRM-equivalent score (0-7 scale)
  srm_deviation: -0.8       # 0.8 units below 28-day baseline
  baseline_window_days: 28
  baseline_sufficient: true
  interaction_timing_entropy: 2.14   # bits
  social_rhythm_trend: decreasing
  circadian_anchor_hour: 9.5         # modal first contact at ~9:30 AM
  consent_ref: "consent:grant/social.derived/abc"
  privacy_tier: boundary_derived
  unit: "{score}"
  quality_flags: []
  social_context_flags: [rhythm_disruption]
```

### 8.3 SocialContactSummaryObs Op-Log Example

```yaml
op_id: "crdt:op/social-contact-summary-20260622T000000Z"
op_type: append
vector_clock: {...}
payload_type: SocialContactSummaryObs
payload:
  observation_id: "social-contact-summary-20260622T000000Z"
  adapter_id: "org.cytognosis.yar.social_interaction"
  axis_ref:
    axis_id: yar.social.social_contact_index
    axis_label: "Social contact index"
    domain: social_engagement
    value_type: continuous
    unit: "{score}"
    biolink_class: biolink:PhenotypicFeature
  timestamp: "2026-06-22T00:00:00Z"
  window_start: "2026-06-21T00:00:00Z"
  window_end: "2026-06-21T23:59:59Z"
  window_type: daily
  result:
    scalar: 0.34            # 34% of user's typical contact intensity
  social_contact_index: 0.34
  contact_diversity_index: 0.41
  copresence_duration_daily_s: 3600.0   # 1 hour of inferred proximity
  copresence_peer_count_max: 3
  communication_active_hours: 4
  withdrawal_signal: mild_reduction
  consent_ref: "consent:grant/social.derived/abc"
  privacy_tier: boundary_derived
  unit: "{score}"
  quality_flags: []
  nd_signal_flags: []
  social_context_flags: [reduced_call_volume]
```

---

## 9. Conformance and Acceptance Criteria

### 9.1 All Social-Interaction Observations

- **REQ-SOC-001**: The system shall reject any `SocialInteractionObservation` that includes a raw phone number, contact name, email address, or any un-hashed contact identifier in any field.
- **REQ-SOC-002**: The system shall reject any `SocialInteractionObservation` that includes a set or list of contact hashes as a boundary-crossable field. The `contact_diversity_hash_count` field is an integer count only and is `on_device_only`; the `contact_diversity_index` scalar is the only boundary-crossable derivative.
- **REQ-SOC-003**: The system shall not serialize `call_timing_hours` to any network-bound buffer. This field is `on_device_only` and is used solely for on-device entropy computation.
- **REQ-SOC-004**: The system shall write every accepted `SocialInteractionObservation` to the CRDT op-log as an `append` operation before acknowledging acceptance.
- **REQ-SOC-005**: When any of the three consent scopes (`aware.communication`, `aware.bluetooth`, `social.derived`) is withdrawn, the system shall stop accepting observations from the affected pipeline within one session and shall purge the corresponding on-device raw event log within 24 hours.

### 9.2 Communication Summary

- **REQ-COMM-001**: The system shall produce exactly one `CommunicationSummaryObs` per daily window per active adapter session, even if the call count is zero (emitting a `quality_flag: no_data_in_window` observation).
- **REQ-COMM-002**: The `outgoing_ratio` field shall be `null` (not 0.0) when `call_count + sms_count = 0` to distinguish an active-zero window from a no-data window.
- **REQ-COMM-003**: The system shall enforce that `incoming_call_count + outgoing_call_count + missed_call_count = call_count`. A mismatch shall set `quality_flag: schema_validation_error`.

### 9.3 Co-Presence Session

- **REQ-COP-001**: The system shall not include any Bluetooth device address hash in any boundary-derived field of `CoPresenceSessionObs`. Device hashes are inputs to session detection only and are not persisted in the op-log.
- **REQ-COP-002**: The system shall apply the RSSI threshold at session detection time. Sessions with all detected peers below the threshold (default -75 dBm) shall not be recorded.
- **REQ-COP-003**: The `inferred_setting` field shall use only on-device WiFi hash comparisons against a user-defined network map. It shall not derive inferences from GPS coordinates or named locations.

### 9.4 Social Rhythm Modeling

- **REQ-SRM-001**: When `baseline_sufficient = false`, the system shall set `srm_deviation = null` and `social_rhythm_trend = insufficient_data`. It shall not impute a deviation from incomplete data.
- **REQ-SRM-002**: The system shall compute the SRM score using only the on-device timing table and co-presence session log. It shall not transmit intermediate timing data to any external service.
- **REQ-SRM-003**: The system shall emit `SocialRhythmMetricObs` observations daily. If the input window has fewer than 3 days of valid communication events, the system shall set `quality_flag: insufficient_data` and set `srm_score = null`.
- **REQ-SRM-004**: The `social_withdrawal` ND signal flag shall be set only when `withdrawal_signal` has been `moderate_reduction` or `marked_reduction` for 3 or more consecutive days and `baseline_sufficient = true`. It shall not be set based on a single-day observation.
- **REQ-SRM-005**: No user-visible label, notification, or Yar message shall describe the user's social interaction using diagnostic or pathologizing language. Permissible phrasing: "you've had a bit less social contact than usual this week." Prohibited: "social isolation," "social withdrawal," "low social functioning," or any diagnostic framing.

### 9.5 Data Quality

- **REQ-DQ-001**: Airplane mode or device-off periods exceeding 4 hours shall be flagged with `quality_flag: sensor_offline` on observations that span the gap. Rhythm scores computed from windows containing sensor-offline gaps of > 8 hours shall be downweighted or set to `null`.
- **REQ-DQ-002**: The system shall distinguish between "zero social events observed" and "sensor offline." A `call_count = 0` observation with no `sensor_offline` flag is a valid data point representing a genuinely low-contact day.

---

## 10. Open Questions

| # | Question | Current leaning | Blocker |
|---|---|---|---|
| O-1 | RSSI proximity threshold for co-presence session detection (-75 dBm default) | Calibrate from AWARE literature; may need per-device or per-environment adjustment | Empirical validation; assign to pilot study |
| O-2 | SRM score computation weight scheme (w1-w4 in `social_contact_index`) | Default weights derived from Canzian et al. 2016; make user-configurable but with defensible defaults | Needs pilot calibration; documented in adapter config |
| O-3 | Contact diversity normalization: should the 28-day baseline be per-week-day (accounting for weekday/weekend social variation)? | Weekday-stratified baseline preferred for mood-disorder use case (SRM theory calls for regularity, not volume) | Algorithm design; assign to SPEC-neurobehavioral-axes.md |
| O-4 | Co-presence inference using WiFi (same SSID hash) vs. Bluetooth-only | Bluetooth-only preferred for fewer false positives; WiFi can augment for confirmed-home sessions | Evaluate in pilot; Bluetooth is the primary signal |
| O-5 | Should `inferred_setting` be surfaced as boundary_derived or kept on_device_only? | Keep `on_device_only` until the inference is validated as reliably non-identifying | Privacy-first default; revisit in v0.2 |
| O-6 | Integration with location entropy (`yar.aware.location_entropy`) for improved SRM approximation | Literature supports adding location entropy to improve RMSE; add as optional secondary input once location-entropy axis is stable | Depends on location-entropy on-device compute (SPEC-sensor-physiological O-7) |
| O-7 | Minimum viable Bluetooth scan rate for co-presence session detection | Current SPEC-sensor-physiological default is every 5 min (0.003 Hz); may need 1-2 min for session-boundary detection accuracy | Battery impact analysis; trade-off with co-presence temporal resolution |
| O-8 | Menstrual cycle interaction: social rhythm disruption is documented across the cycle. Should `SocialRhythmMetricObs` link to menstrual phase from SPEC-sensor-menstrual.md? | Yes; add a `menstrual_phase_context` field as an optional forward-link once SPEC-sensor-menstrual.md is published | Depends on SPEC-sensor-menstrual.md |
| O-9 | Voice/VoIP call detection: AWARE `CommunicationEvent` captures cellular calls; VoIP (WhatsApp, Signal, FaceTime) requires separate adapter hooks | Flag as coverage gap; VoIP calls are a growing fraction of social contact, especially for ND individuals | Platform API access; escalate to SPEC-sensor-speech-mentalstate.md as a coordination point |
| O-10 | Cross-adapter aggregation when both `yar.aware.call_duration_daily` (from SPEC-sensor-physiological) and `yar.social.call_duration_total_daily` (this spec) write to semantically overlapping axes | Resolve naming: physiological spec's `yar.aware.call_duration_daily` may be superseded by this spec's axis once social-interaction adapter is mature | Assign to axis registry cleanup in v0.2; for now, both coexist with different `adapter_id` provenance |

---

## 11. References

1. **Monk TH et al.** (1991). The Social Rhythm Metric: An Instrument for Quantifying the Daily Rhythms of Life. *Journal of Nervous and Mental Disease*, 179(2), 98-103. [Foundational SRM instrument.]

2. **Frank E, Kupfer DJ, Ehlers CL, Monk TH et al.** (1994). Interpersonal and social rhythm therapy for bipolar disorder: integrating interpersonal and behavioral approaches. *Behavior Therapist*, 17(4), 143-149. [Social zeitgeber and IPSRT basis.]

3. **Grandin LD, Alloy LB, Abramson LY** (2006). The social zeitgeber theory, circadian rhythms, and mood disorders: review and evaluation. *Clinical Psychology Review*, 26(6), 679-694. [Social zeitgeber theory review.] https://doi.org/10.1016/j.cpr.2006.07.001

4. **Canzian L, Musolesi M** (2016). Trajectories of depression: unobtrusive monitoring of depressive states by means of smartphone mobility traces analysis. *Proc. ACM UbiComp*, 1. [RMSE 1.40 SRM passive sensing result, referenced in JAMIA 2016 study context.]

5. **Canzian et al., JAMIA 2016.** Automatic detection of social rhythms in bipolar disorder. *Journal of the American Medical Informatics Association*, 23(3), 538–543. https://academic.oup.com/jamia/article/23/3/538/2909018 [Precision 0.85, recall 0.86 for stable/unstable state classification; RMSE 1.40 on SRM prediction.]

6. **Faurholt-Jepsen M et al.** (2018). Development and Evaluation of a Smartphone-Based Measure of Social Rhythms for Bipolar Disorder. *JMIR Mental Health*. https://pmc.ncbi.nlm.nih.gov/articles/PMC6155452/ [Smartphone-based SRM validation in bipolar disorder.]

7. **Tienoven TP, Minnen J** (2014). Calculating the Social Rhythm Metric (SRM) and Examining Its Use in IPSRT. https://pubmed.ncbi.nlm.nih.gov/25379281/ [SRM computation methodology for healthy populations.]

8. **Jacobson NC, Bhattacharya S** (2024). Digital phenotyping for monitoring mental disorders: Systematic review. *PMC*. https://pmc.ncbi.nlm.nih.gov/articles/PMC10753422/ [Systematic review of passive sensing for mood and anxiety.]

9. **JMIR 2025.** Passive Sensing for Mental Health Monitoring Using Machine Learning With Wearables and Smartphones: Scoping Review. https://www.jmir.org/2025/1/e77066 [Scoping review of 42 studies, 2015-2025.]

10. **Saeb S et al.** (2019). Identifying Behavioral Phenotypes of Loneliness and Social Isolation with Passive Sensing. *PMC*. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6685126/ [Bluetooth, location, and call logs as social isolation markers.]

---

## 12. Cross-References

| Document | Relationship |
|---|---|
| `Yar/spec/SPEC-CSP.md` | Anchor protocol; adapter lifecycle, schema types, CAP governance, privacy tiers |
| `Yar/spec/SPEC-sensor-physiological.md` | Defines AWARE primitive classes this spec extends; Section 4.2 defines `AWARECommunicationObservation`, `AWAREBluetoothObservation`, `AWARELocationObservation` |
| `Cytoplex/spec/privacy-boundary-spec.md` | Privacy tier classification, CrossBoundarySignal schema; PB-1 through PB-10 apply |
| `Cytoplex/spec/03_primitives.md` | CAP primitive types: `Directive`, `GuardDecision`, `DecisionRecord` |
| `Yar/spec/SPEC-storage-engine.md` | CRDT op-log (L2); op-log entry format |
| `Yar/spec/SPEC-sync-protocol.md` | L2 CRDT replication; L6 consent layer |
| `04-Engineering/yar/sensors/implementing-aware.md` | AWARE adapter implementation; `AWARECommunicationObservation` and `AWAREBluetoothObservation` implementation detail (Sections 3.5, 3.6) |
| `MODULE-crisis-detection.md` | Social withdrawal flags may contribute as secondary signals; crisis module governs response |
| `SPEC-neurobehavioral-axes.md` (planned) | Forward-reference: social rhythm score and deviation as contextual covariates for mood and energy axes |
| `SPEC-sensor-menstrual.md` (planned) | Open item O-8: menstrual phase as social-rhythm covariate |
| `SPEC-sensor-speech-mentalstate.md` (planned) | Open item O-9: VoIP call detection coordination |
