---
spec_id: SPEC-sensor-menstrual
version: "0.1"
status: draft
domain: sensor-menstrual
owner: Shahin Mohammadi
created: 2026-06-22
last_updated: 2026-06-22
depends_on: [SPEC-CSP, SPEC-storage-engine]
implements: [CSP]
---

# SPEC-sensor-menstrual: Menstrual and Reproductive-Cycle Sensing

> **Status**: Draft
> **Date**: 2026-06-22
> **Author**: Cytognosis Foundation
> **Audience**: engineers
> **Tags**: `yar`, `cytonome`, `csp`, `sensor`, `menstrual`, `reproductive-health`, `privacy`
> **Related:** [SPEC-CSP](./SPEC-CSP.md); [SPEC-sensor-physiological](./SPEC-sensor-physiological.md); privacy boundary at `Cytoplex/spec/privacy-boundary-spec.md`; storage at `./SPEC-storage-engine.md`

---

**Reading time**: ~14 minutes.
**If you only read one thing**: Section 6 (Privacy and Governance). Reproductive-cycle data is the highest-sensitivity personal health category in Yar. Every design choice in this spec flows from the principle that the user owns this data absolutely, it stays on-device by default, and no third-party shares are ever permitted.

**BLUF**: This spec binds menstrual and reproductive-cycle sensing to the CSP schema. Cycle-phase data is a meaningful covariate for mood, cognition, and neurodivergent symptom expression, but it is also maximally sensitive under current US law. The spec covers Apple HealthKit and Google Health API sources, manual logging, on-device cycle-phase estimation, and the contextual covariate pathway that feeds neurobehavioral axes, all wrapped in a consent model, CrossBoundarySignal classifications, and explicit safeguards against reproductive-data misuse.

> **Implementation status**: Design-only, not yet implemented. No menstrual-cycle sensor adapter code was found in any Cytognosis repo at the time of the June 2026 codebase sweep (see INCORPORATION_MAP.md §8, SPEC-sensor-menstrual row). A schema stub `vendor_mira.yaml` is referenced in `04-Engineering/cytos/sensing-schema/` but was not found in the codebase at sweep time. The HealthKit reproductive identifiers, Google Health API integration, and the on-device phase estimator are all design-only pending app implementation.

---

## 1. Purpose and Scope

This spec is the formal modality-level complement to [SPEC-CSP](./SPEC-CSP.md) for menstrual and reproductive-cycle signals. CSP defines the protocol skeleton; this document fills it in for one new CSP adapter class: **Reproductive Cycle Sensing**.

### 1.1 Why This Matters

Menstrual cycle phase modulates neurotransmitter levels, mood, cognition, and neurodivergent symptom expression in ways that are measurable and clinically meaningful. Estrogen rises during the follicular phase and promotes dopamine release; as estrogen drops in the late luteal phase, dopamine availability decreases, which is associated with worsening attention difficulties, emotional reactivity, and executive function challenges in people with ADHD (Robberecht et al., 2026; Getinflow.io 2024; ADDitude 2024). **PMDD** (Premenstrual Dysphoric Disorder) co-occurs with ADHD at elevated rates, producing a compounding luteal-phase burden. A recent narrative review documented pronounced attention, impulsivity, and executive function impairments during mid-luteal and pre-menstrual phases in people with ADHD (MDPI/JCM 2026; PMC12786913).

Without cycle-phase as a covariate, Yar's longitudinal mood and cognition axes will show unexplained periodic variance. Anchoring that variance to cycle phase is not optional for accurate behavioral modeling in this user population.

**Inclusive language note:** Throughout this spec, "people who menstruate" is the preferred construction over gendered terms. User-facing copy must reflect this. Cycle variation is described as variation, not deviation from a standard. Labels such as "normal cycle" or "abnormal cycle" are prohibited; use "cycle pattern varies" or "phase estimation paused" instead.

### 1.2 What Is in Scope

- **Cycle-phase estimation**: follicular, ovulatory, luteal, menstrual phases estimated on-device from logged and sensor inputs.
- **Flow logging**: period onset, offset, and relative flow intensity.
- **Symptom logging**: user-reported associated symptoms (cramping, mood, energy, cognitive fog) as structured observations, never free text.
- **Biomarker inputs**: basal body temperature (BBT), ovulation test result, cervical mucus quality, intermenstrual bleeding, as available from HealthKit or manual entry.
- **Fertile-window estimate**: derived on-device; classified `on_device_only` by default given its sensitivity.
- **Cycle-phase covariate axis**: a derived scalar that feeds `SPEC-neurobehavioral-axes.md` as a contextual covariate without exposing underlying reproductive-health observations.

### 1.3 What Is Explicitly Not in Scope

- **Fertility or contraception advice**: Yar does not offer medical guidance on fertility, contraception, or pregnancy. The fertile-window estimate is a behavioral-context covariate, not a contraceptive tool. This must be communicated clearly in the consent flow and app UI.
- **Covert tracking**: no cycle data is collected without explicit, per-session consent. Passive background collection of reproductive-cycle signals is prohibited by this spec.
- **Pregnancy management**: pregnancy detection and monitoring are outside scope. If `HKCategoryTypeIdentifier.pregnancy` is set in HealthKit, Yar will not ingest it and must ignore it at the adapter level.
- **Third-party data sharing**: reproductive-health observations (all tiers) are never shared with any third party, including research pipelines, cloud analytics, or clinician integrations, without a separate, purpose-specific consent act (see Section 6.5).

---

## 2. Data Sources

The table below lists every sensor source and input mode covered by this spec. Each row is a CSP sensor source with declared adapter class, maturity, and privacy tier.

| Source | Adapter ID | Maturity | Privacy Tier | What Is Ingested |
|---|---|---|---|---|
| Apple HealthKit (reproductive) | `org.cytognosis.yar.healthkit.repro` | Beta | `on_device_only` (all reproductive-category observations) | menstrualFlow, basalBodyTemperature, cervicalMucusQuality, ovulationTestResult, intermenstrualBleeding, and newer identifiers (see §3.1) |
| Google Health API (cycle) | `org.cytognosis.yar.googlehealth.cycle` | Beta | `on_device_only` (raw); `boundary_derived` (derived covariate scalar only) | Cycle log entries accessible via Google Health API cycle data types (note: Fitbit Web API deprecated September 2026; see §3.2) |
| Manual user logging | `org.cytognosis.yar.menstrual.log` | Stable | `on_device_only` (raw log); `boundary_derived` (derived covariate scalar only) | User-entered period onset/offset, flow, and symptom checklist |
| On-device cycle-phase estimator | `org.cytognosis.yar.menstrual.estimator` | Beta | `boundary_derived` (phase enum only); `on_device_only` (all inputs) | Derived `CyclePhaseEstimate` from the above sources |

**Privacy tier rationale**: all raw reproductive-cycle observations are `on_device_only`. The sole `boundary_derived` output is the `CyclePhaseEstimate`, and only after explicit user opt-in to covariate sharing. This is stricter than wearable physiological data (SPEC-sensor-physiological) because the legal and personal risk of reproductive-data exposure is categorically higher (see Section 6.1).

---

## 3. Source-Specific Notes

### 3.1 Apple HealthKit Reproductive Identifiers

Apple HealthKit defines the following reproductive and menstrual `HKCategoryTypeIdentifier` values, all category samples (Apple Developer Documentation, 2024-2026):

| HealthKit Identifier | Type | Description | Ingested by Yar? |
|---|---|---|---|
| `menstrualFlow` | Category | Menstrual flow presence and relative volume | Yes |
| `basalBodyTemperature` | Quantity (Cel) | Waking body temperature before activity | Yes |
| `cervicalMucusQuality` | Category | Mucus quality enum (dry, sticky, creamy, watery, eggWhite) | Yes |
| `ovulationTestResult` | Category | LH surge test result (negative, positive, indeterminate, estrogenSurge) | Yes |
| `intermenstrualBleeding` | Category | Spotting event between periods | Yes |
| `infrequentMenstrualCycles` | Category | Cycle duration > 38 days (iOS 16+) | Yes |
| `irregularMenstrualCycles` | Category | Detected cycle irregularity pattern (iOS 16+) | Yes |
| `persistentIntermenstrualBleeding` | Category | Prolonged intermenstrual spotting (iOS 16+) | Yes |
| `prolongedMenstrualPeriods` | Category | Flow lasting > 8 days (iOS 16+) | Yes |
| `pregnancyTestResult` | Category | Home pregnancy test result | No (out of scope; ignored at adapter) |
| `progesteroneTestResult` | Category | Home progesterone test | Yes (luteal confirmation only; ingested as phase input, not exposed raw) |
| `pregnancy` | Category | Pregnancy confirmation | No (out of scope; ignored at adapter) |
| `lactation` | Category | Lactation status | No (out of scope) |
| `sexualActivity` | Category | Sexual activity with/without contraception | No (out of scope) |
| `contraceptive` | Category | Contraceptive method | No (out of scope) |

`basalBodyTemperature` is an `HKQuantityTypeIdentifier` (not category); it uses UCUM `Cel` as unit. All other identifiers above are category samples with associated value enums.

**HealthKit access**: requires `NSHealthShareUsageDescription` and individual `HKSampleType` authorization per identifier. Each identifier maps to a separate `ConsentScope` in Yar's CSP consent model.

### 3.2 Google Health API (formerly Fitbit)

The Fitbit Web API is being deprecated in September 2026; all integrations must migrate to the Google Health API (Google, 2026). The Google Health API includes cycle health data types accessible via OAuth 2.0 and provides cycle log and period data. However, as of 2026, the Google Health API does not expose raw reproductive cycle metrics (BBT, cervical mucus) via API; it surfaces aggregated cycle log and period prediction data only.

**Yar's approach**: ingest cycle log entries (period start/end dates, predicted fertile window) as `MenstrualCycleLogObs`. All reproductive-cycle data from this source is `on_device_only`. Only the derived phase estimate may become `boundary_derived` under explicit consent.

Adapter ID: `org.cytognosis.yar.googlehealth.cycle`. Authentication: Google OAuth 2.0 with the Health API cycle data scope. Rate limits and retry policy follow the pattern established in `SPEC-sensor-physiological.md` for the Fitbit adapter.

### 3.3 Manual User Logging

The manual adapter is a structured self-report form: period onset/offset date, flow level (enumerated), and a symptom checklist (enumerated, never free text). This adapter is always `Stable` because it requires no external API and carries no authentication complexity.

The adapter implements the standard CSP lifecycle: `discover` registers the form, `connect(consent_ref)` activates it, `configure` sets the user's typical cycle length prior (used by the estimator), `observe` captures a single completed log entry, and `disconnect` closes the session.

---

## 4. CSP Binding and LinkML Classes

### 4.1 Adapter Class Declaration

| This spec's adapter class | CSP Section | SensorDescriptor.adapter_class value |
|---|---|---|
| HealthKit reproductive adapter | CSP 6.3 (Physiological Wearables extended) | `reproductive_cycle_sensing` |
| Google Health cycle adapter | CSP 6.3 (extended) | `reproductive_cycle_sensing` |
| Manual log adapter | CSP 6.1 (Self-Report, structured) | `reproductive_cycle_sensing` |
| On-device estimator | CSP 6.3 (derived) | `reproductive_cycle_sensing` |

All adapters share the single class `reproductive_cycle_sensing`. This consolidation reflects the spec's design intent: all reproductive-cycle inputs, regardless of source, feed a unified on-device model and produce observations of the same types.

### 4.2 LinkML Class Hierarchy

```
sosa:Observation
  └── CSPObservation                               (SPEC-CSP §4.1)
        └── ReproductiveCycleObservation           (this spec, §4.3)
              ├── MenstrualCycleLogObs             (§4.4) — period onset, offset, log entry
              ├── MenstrualFlowObs                 (§4.4) — daily flow intensity
              ├── BasalBodyTemperatureObs          (§4.4) — waking BBT
              ├── CervicalMucusQualityObs          (§4.4) — mucus quality enum
              ├── OvulationTestResultObs           (§4.4) — LH/estrogen surge result
              ├── IntermenstrualBleedingObs        (§4.4) — spotting event
              ├── MenstrualSymptomObs              (§4.5) — user-reported associated symptoms
              └── CyclePhaseEstimate               (§4.6) — derived on-device phase enum
```

### 4.3 ReproductiveCycleObservation Base Class

```yaml
# LinkML (normative field names; inherits all CSPObservation fields)
classes:
  ReproductiveCycleObservation:
    is_a: CSPObservation
    description: >-
      Base class for all menstrual and reproductive-cycle observations.
      Maximally-sensitive data category. All raw observations are on_device_only.
      Only CyclePhaseEstimate may be boundary_derived, and only under explicit user opt-in.
    mixins: [ReproductiveSensitivityMixin]
    attributes:
      source_adapter:
        range: ReproductiveCycleSourceEnum
        required: true          # healthkit | google_health | manual | estimator
      cycle_day:
        range: integer          # day within the current cycle (1-indexed); computed on-device
        minimum_value: 1
        maximum_value: 90       # covers longest typical cycles + outliers
      data_entry_mode:
        range: DataEntryModeEnum    # passive (healthkit/google) | active (manual)
        required: true
      # Inherits: observation_id, adapter_id, axis_ref, timestamp, result, provenance,
      #           consent_ref, privacy_tier, unit, quality_flags from CSPObservation

  ReproductiveSensitivityMixin:
    description: >-
      Marker mixin applied to all reproductive-cycle observations.
      Signals to the CAP PEP that these observations require the
      reproductive_cycle consent scope and elevated audit logging.
      No additional fields; existence of the mixin is the signal.
    mixin: true
```

### 4.4 Concrete Observation Classes

```yaml
classes:
  MenstrualCycleLogObs:
    is_a: ReproductiveCycleObservation
    description: A logged cycle event — period start, period end, or a cycle boundary marker.
    attributes:
      event_type:
        range: CycleEventTypeEnum    # period_start | period_end | cycle_start | no_bleed
        required: true
      cycle_length_days:
        range: integer               # estimated cycle length used by the on-device estimator
      # privacy_tier: on_device_only (enforced by ReproductiveSensitivityMixin + PEP)

  MenstrualFlowObs:
    is_a: ReproductiveCycleObservation
    description: A single-day flow intensity observation.
    attributes:
      flow_level:
        range: MenstrualFlowLevelEnum    # none | spotting | light | medium | heavy | very_heavy
        required: true
      # Maps to HKCategoryValueMenstrualFlow (HealthKit) or user selection (manual)
      # privacy_tier: on_device_only

  BasalBodyTemperatureObs:
    is_a: ReproductiveCycleObservation
    description: Waking body temperature before physical activity; a key ovulation signal.
    attributes:
      temperature_cel:
        range: float
        required: true        # UCUM: Cel; HealthKit HKQuantityTypeIdentifier.basalBodyTemperature
      thermometer_type:
        range: BBTThermometerTypeEnum    # basal | standard | wearable_derived
      # privacy_tier: on_device_only

  CervicalMucusQualityObs:
    is_a: ReproductiveCycleObservation
    description: User-observed cervical mucus quality, a fertility signal.
    attributes:
      quality:
        range: CervicalMucusQualityEnum    # dry | sticky | creamy | watery | egg_white | unknown
        required: true
      # Maps to HKCategoryValueCervicalMucusQuality (HealthKit) or manual selection
      # privacy_tier: on_device_only

  OvulationTestResultObs:
    is_a: ReproductiveCycleObservation
    description: Result of a home LH surge or estrogen surge ovulation test.
    attributes:
      test_result:
        range: OvulationTestResultEnum    # negative | lh_surge | estrogen_surge | indeterminate
        required: true
      # Maps to HKCategoryValueOVulationTestResult (HealthKit) or manual entry
      # privacy_tier: on_device_only

  IntermenstrualBleedingObs:
    is_a: ReproductiveCycleObservation
    description: A spotting or bleeding event between expected period windows.
    attributes:
      bleeding_present:
        range: boolean
        required: true
      # privacy_tier: on_device_only

  MenstrualSymptomObs:
    is_a: ReproductiveCycleObservation
    description: >-
      User-reported physical or cognitive symptom associated with the cycle phase.
      Uses a controlled enumeration; free text is prohibited.
    attributes:
      symptom_type:
        range: MenstrualSymptomTypeEnum
        required: true
        # cramping | bloating | headache | fatigue | low_energy | mood_low | mood_irritable
        # mood_elevated | cognitive_fog | hyperfocus | sleep_disruption | appetite_change
        # pain_pelvic | pain_breast | other_physical | other_cognitive
      severity:
        range: SymptomSeverityEnum    # low | moderate | elevated | high
        required: true
      # Free text is schema-prohibited. Symptoms are categorical, never narrative.
      # privacy_tier: on_device_only
```

### 4.5 CyclePhaseEstimate

`CyclePhaseEstimate` is the only observation type in this spec that may become `boundary_derived`. It is a derived output of the on-device estimator (Section 5) and carries no individual biomarker data.

```yaml
classes:
  CyclePhaseEstimate:
    is_a: ReproductiveCycleObservation
    description: >-
      On-device derived estimate of the user's current cycle phase.
      This is the sole output type from this spec that may cross the privacy boundary,
      and only under explicit opt-in consent (scope: reproductive_cycle.phase_covariate).
      It contains no raw biomarker data.
    attributes:
      phase:
        range: CyclePhaseEnum
        required: true           # menstrual | follicular | ovulatory | luteal | unknown
      phase_confidence:
        range: CyclePhaseConfidenceEnum    # low | medium | high
        required: true
      estimated_cycle_day:
        range: integer           # estimated day within cycle; same as cycle_day
      data_inputs_used:
        range: CycleDataInputEnum
        multivalued: true        # which sources informed this estimate
        # period_log | bbt | mucus | ovulation_test | historical_pattern | skin_temp
      days_since_period_start:
        range: integer           # coarse temporal anchor; no raw dates
      biolink_class:
        range: string
        equals_string: "biolink:PhenotypicFeature"
      # privacy_tier: boundary_derived ONLY under reproductive_cycle.phase_covariate consent scope
      # Default at install time: on_device_only
```

### 4.6 Axis Registry: Built-in Axes

These axes are registered as CSP built-in axes (namespace `yar.*`). All axes are `on_device_only` by default. The phase covariate axis may become `boundary_derived` under explicit consent.

| axis_id | axis_label | domain | value_type | unit | LOINC/code | Biolink |
|---|---|---|---|---|---|---|
| `yar.repro.cycle_phase` | Cycle phase estimate | reproductive_cycle | categorical | — | sensor:cycle-phase | biolink:PhenotypicFeature |
| `yar.repro.cycle_day` | Estimated cycle day | reproductive_cycle | continuous | {day} | — | — |
| `yar.repro.menstrual_flow` | Menstrual flow level | reproductive_cycle | ordinal | — | LOINC:49033-4* | — |
| `yar.repro.bbt` | Basal body temperature | reproductive_cycle | continuous | Cel | LOINC:8310-5 | — |
| `yar.repro.cervical_mucus` | Cervical mucus quality | reproductive_cycle | categorical | — | LOINC:10564-3 | — |
| `yar.repro.ovulation_test` | Ovulation test result | reproductive_cycle | categorical | — | — | — |
| `yar.repro.symptom_burden` | Cycle-associated symptom burden | reproductive_cycle | continuous | {score} | — | biolink:PhenotypicFeature |
| `yar.repro.phase_covariate` | Cycle phase (covariate scalar) | contextual_covariate | continuous | {0-3}** | — | biolink:PhenotypicFeature |

\* LOINC 49033-4 does not map precisely to a flow-level categorical; this is the closest panel code (menstrual cycle observation). Verify against loinc.org before implementation.

\*\* The phase covariate encodes phase as an ordinal integer (0=menstrual, 1=follicular, 2=ovulatory, 3=luteal) for downstream model use. This is a derived scalar with no patient-identifiable content.

**FHIR/LOINC mapping table:**

| Signal | LOINC | SNOMED CT | UCUM | FHIR Observation profile |
|---|---|---|---|---|
| Last menstrual period start | 8665-2 | 21840007 | — | `Observation.code = 8665-2` |
| Basal body temperature | 8310-5 | 248595001 | Cel | `Observation.valueQuantity` |
| Cervical mucus volume | 10564-3 | — | mL | `Observation.code = 10564-3` |
| Cycle length (days) | 64700-8 | — | {day} | `Observation.valueQuantity` |
| Menstrual cycle observation | 49033-4* | — | — | `Observation` panel |

FHIR R4 Observation resource is the normative representation. The Australian Base FHIR profile (`au-lastmenstrualperiod`) provides a worked example of `code = 8665-2` with `valueDateTime`. Yar's FHIR mapping follows the same pattern but does not require a FHIR server; LOINC codes are used for semantic alignment only.

### 4.7 Axis Registry Alignment

The table below maps each reproductive-cycle axis to its role in the canonical 63-axis registry (source: PSYCH_AXES_SYNTHESIS.md Sections 5.2 and 5.4). A critical architectural note precedes the table.

**Cycle phase is a COVARIATE, not a neurobehavioral axis.** `yar.repro.phase_covariate` does not appear in the 63-axis registry as a dimension in its own right. It is a normative context modifier that conditions the interpretation of deviation types on existing axes (see PSYCH_AXES_SYNTHESIS.md §5.4). Specifically:

- During the luteal phase, reduced dopamine availability shifts the normative midpoint for Mood activation, executive function, working memory, and irritability threshold. A z-score of -0.8 on `mood.activation` in the luteal phase carries a different interpretation weight than the same score in the follicular phase.
- The covariate is stored in `AxisCovariateContext.cycle_phase` (SPEC-neurobehavioral-axes.md schema) and is used to flag when longitudinal baseline statistics may be phase-confounded.
- No reproductive-cycle axis should be presented to users as a behavioral phenotype or tracking target; the cycle phase contextualizes phenotypes, it does not define one.

The other reproductive axes (`yar.repro.cycle_phase`, `yar.repro.menstrual_flow`, etc.) are health-record signals, not neurobehavioral phenotype axes. They do not map to 63-axis registry entries; they are inputs to the on-device phase estimator.

| axis_id | Registry role | EQ dimension facet / context function | Notes |
|---|---|---|---|
| `yar.repro.phase_covariate` | **Contextual covariate** (not a registry axis) | Type-7 (mistiming) context modifier for `mood.activation`, `cognitive.executive`, `cognitive.working_memory`, `mood.irritability` | Conditions z-score interpretation in luteal phase; forward-reference to SPEC-neurobehavioral-axes.md `AxisCovariateContext.cycle_phase` |
| `yar.repro.cycle_phase` | Health-record signal; estimator output | Phase enum feeding `phase_covariate` | Not a neurobehavioral dimension; on-device only |
| `yar.repro.cycle_day` | Health-record signal | Temporal anchor for phase estimation | Not a neurobehavioral dimension; on-device only |
| `yar.repro.menstrual_flow` | Health-record signal | Flow level input to phase estimator | Not a neurobehavioral dimension; on-device only |
| `yar.repro.bbt` | Health-record signal | Ovulation signal input; also a type-7 (mistiming) thermal marker when combined with `yar.physio.skin_temp_deviation` | Not a neurobehavioral dimension; on-device only |
| `yar.repro.cervical_mucus` | Health-record signal | Ovulation signal input | Not a neurobehavioral dimension; on-device only |
| `yar.repro.ovulation_test` | Health-record signal | Ovulation event pin for phase estimation | Not a neurobehavioral dimension; on-device only |
| `yar.repro.symptom_burden` | Partial overlap with **Fatigue/Energy** (Somatic) and **Distress/Stress Response** (Emotional) | ICF b152 (emotional functions) + b455 (exercise tolerance) for luteal-phase burden; symptom entries as phenomenological inputs | On-device only; feeds `mood.irritability` and `mood.activation` covariate context, not direct axis scoring |

*Source: PSYCH_AXES_SYNTHESIS.md §5.4 (menstrual phase as covariate) and §3.1 (63-axis inventory).*

---

## 5. On-Device Cycle-Phase Modeling

### 5.1 Algorithm Overview

Yar estimates cycle phase entirely on-device. No raw dates, biomarker values, or personally identifiable cycle data are transmitted to any server for modeling.

The on-device estimator uses a **rule-based Bayesian prior updated by user data**:

1. **Prior initialization**: the user enters (or the adapter infers from historical logs) a typical cycle length (default: 28 days) and typical period duration (default: 5 days). These become the prior.
2. **Phase boundary computation**: menstrual phase = days 1 through period_duration; follicular = period_duration+1 through ovulation_day-2; ovulatory = ovulation_day-1 through ovulation_day+1; luteal = ovulation_day+2 through cycle_length. Ovulation day defaults to cycle_length - 14 (standard calendar rule).
3. **Biomarker updating**: BBT rise (>0.2°C above follicular baseline sustained 3 days) shifts ovulation day estimate backward by 1-2 days. Positive LH/ovulation test result pins ovulation day to the test date. Cervical mucus "egg white" quality shifts the ovulatory window estimate forward by 1 day. Each update is weighted by data availability and consistency.
4. **Confidence scoring**: `high` if period start is logged and ≥1 biomarker input is available; `medium` if period start only; `low` if estimated from historical average alone.
5. **Wearable temperature integration**: if Oura or Fitbit skin temperature deviation (`yar.physio.skin_temp_deviation`) is available and the user has consented to cross-sensor correlation, the estimator uses the temperature signal as a BBT proxy. This is an optional enhancement, not a requirement.

**Research grounding**: A 2025 machine learning study (npj Women's Health, 2025; doi referenced below) achieved 87% three-phase accuracy using wearable physiological signals without user input. Yar's algorithm is simpler (rule-based + Bayesian update) but more privacy-preserving. Fully on-device ML phase classification is a future enhancement (see Open Question O-4).

### 5.2 Cycle Phase as a Contextual Covariate

The `CyclePhaseEstimate` feeds the neurobehavioral axes system as a **contextual covariate**, not as a behavioral phenotype. The distinction matters:

- **Contextual covariate**: the phase estimate is a stratification variable that explains variance in other axes (mood, attention, energy) without being a tracking target itself. Cycle phase is NOT one of the 63 canonical neurobehavioral axes. It does not produce a user-visible phenotype score or trend. It is stored in `AxisCovariateContext.cycle_phase` and used by the axis model to condition baseline statistics.
- **Affected axes**: `mood.activation`, `mood.irritability`, `cognitive.executive`, and `cognitive.working_memory` are the primary axes whose z-score interpretation is conditioned by cycle phase (see PSYCH_AXES_SYNTHESIS.md §5.4). A luteal-phase flag shifts the normative midpoint for these dimensions; the same observation carries different weight in follicular vs. luteal context.
- **Forward reference**: `SPEC-neurobehavioral-axes.md` (planned) will define the axis-combination model that incorporates `yar.repro.phase_covariate` as an input. This spec only produces the covariate; it does not perform the integration. See also PSYCH_AXES_SYNTHESIS.md §5.4 for the formal EQ-model rationale for why phase is a covariate and not a dimension.

The covariate output is the `yar.repro.phase_covariate` axis (Section 4.6): an ordinal integer (0-3) representing phase. No cycle day, date, or biomarker value is included in the covariate.

### 5.3 Cycle Irregularity and "Unknown" Phase

Not all users have regular cycles. PCOS, perimenopause, hormonal contraception, and other factors produce irregular or absent cycles. The estimator handles this gracefully:

- If no period has been logged in the last 90 days, `phase = unknown` and `phase_confidence = low`.
- If HealthKit reports `infrequentMenstrualCycles`, `irregularMenstrualCycles`, or `prolongedMenstrualPeriods`, the estimator widens its phase uncertainty window and reduces confidence.
- The `unknown` phase passes through the covariate axis as `null` (not 0). Downstream neurobehavioral-axes models must handle `null` covariate gracefully (impute or stratify separately).

Users are never shown "irregular" or "abnormal" in any user-facing label. Instead, Yar uses affirming, descriptive language: "cycle pattern varies" or "phase estimation paused — no recent data."

---

## 6. Privacy and Governance

### 6.1 Legal-Risk Context

Reproductive-cycle data is among the highest-risk personal health categories in the current US legal landscape. The 2024 HIPAA Privacy Rule amendments that protected reproductive health data were vacated by a federal court in June 2025 (US District Court, Northern District of Texas, 2025; IAPP 2025). State-level protections vary dramatically. The FTC has taken action against period-tracking apps that shared personal data with advertisers (FTC enforcement, 2023-2024). Privacy researchers have documented significant data exposure in consumer cycle-tracking apps (arXiv:2404.05876, 2024).

Yar's position: **this data never leaves the device without the user's explicit, purpose-specific consent, and never reaches any third party under any circumstances.** This is not a policy aspiration; it is an architectural invariant enforced at the CAP PEP level.

### 6.2 Consent Model

All reproductive-cycle adapters require **explicit opt-in consent** as a precondition for the `connect` phase. The default is `denied`.

Consent scopes defined by this spec:

| Scope name | Covers | Privacy tier |
|---|---|---|
| `reproductive_cycle.flow_log` | Period onset/offset, flow level | `on_device_only` |
| `reproductive_cycle.biomarkers` | BBT, cervical mucus, ovulation test, intermenstrual bleeding | `on_device_only` |
| `reproductive_cycle.symptoms` | Symptom log entries | `on_device_only` |
| `reproductive_cycle.healthkit` | HealthKit read access for reproductive identifiers | `on_device_only` |
| `reproductive_cycle.google_health` | Google Health API cycle data read | `on_device_only` |
| `reproductive_cycle.phase_covariate` | Export of `CyclePhaseEstimate` (phase enum only) to neurobehavioral axes | `boundary_derived` (opt-in upgrade from `on_device_only`) |

**Consent rules:**

- Each scope requires a separate, distinct consent act. Bundled consent ("allow Yar to track your health") is prohibited for reproductive-cycle data.
- Consent UI must clearly state: (a) what data is collected, (b) where it is stored (on-device only), (c) that no third parties receive the data, and (d) that consent can be withdrawn at any time with immediate effect.
- The `reproductive_cycle.phase_covariate` scope must explain what the phase covariate is and how it is used, before the user is asked to consent.
- Consent withdrawal takes effect within one session (PB-8). All pending observations are dropped; existing on-device data is retained until the user requests deletion (see Section 6.4).

### 6.3 CrossBoundarySignal Classification

Every axis produced by this spec is classified as a `CrossBoundarySignal`. The classifications are stricter than physiological wearable data.

| Signal | Privacy tier | What may cross the boundary | CAP primitive |
|---|---|---|---|
| Period onset/offset dates | `on_device_only` | Nothing | N/A |
| Menstrual flow level | `on_device_only` | Nothing | N/A |
| BBT readings | `on_device_only` | Nothing | N/A |
| Cervical mucus quality | `on_device_only` | Nothing | N/A |
| Ovulation test results | `on_device_only` | Nothing | N/A |
| Intermenstrual bleeding events | `on_device_only` | Nothing | N/A |
| Symptom log entries | `on_device_only` | Nothing | N/A |
| CyclePhaseEstimate (phase enum only) | `on_device_only` by default; `boundary_derived` under explicit `reproductive_cycle.phase_covariate` consent | Phase enum (0-3), confidence level, no dates or biomarkers | `Directive` with scope `reproductive_cycle.phase_covariate` |
| Fertile window estimate | `on_device_only` permanently | Nothing — fertile window is never boundary_derived | N/A |

**Key invariants enforced at the CAP PEP:**

- The `ReproductiveSensitivityMixin` on every observation class signals elevated audit logging. Every CAP `Directive` and `GuardDecision` for reproductive-cycle data is logged with `sensitivity_level: reproductive` in the local audit chain.
- `CyclePhaseEstimate` observations that include raw cycle day, period dates, or any biomarker value in their payload must be rejected by the PEP, even under `reproductive_cycle.phase_covariate` consent.
- No reproductive-cycle observation may be included in any research export, clinical data request, or data-sharing agreement without a separate consent act, explicitly scoped to that purpose, with a description of the recipient and use.

### 6.4 Retention, Export, and Deletion

- **Retention**: all reproductive-cycle observations are stored in the on-device encrypted op-log. No server-side copy is made.
- **User-controlled export**: the user may export their reproductive-cycle data at any time in a machine-readable format (JSON, CSV). The export includes all raw observations and is delivered to the user's device as a file; it is never transmitted to any server.
- **Deletion**: the user may delete all reproductive-cycle data at any time. Deletion must be irreversible, must cover all observations in the op-log (including CRDT tombstones), and must propagate to any synced nodes under the user's control within the next sync session.
- **No analytics exceptions**: reproductive-cycle data is excluded from any aggregate analytics, even non-identifiable analytics. No counts, rates, or distributions derived from reproductive-cycle data are transmitted.

### 6.5 On-Device-First Default

All reproductive-cycle adapters are `on_device_only` at install time. The upgrade path to `boundary_derived` for `CyclePhaseEstimate` follows the CAP consent upgrade flow (SPEC-CSP §5.2, SPEC-sensor-physiological §5.2), with the additional requirement that the upgrade dialog must be full-screen and explicitly reproductive-health-themed, not embedded in a general permissions flow.

### 6.6 No-Sharing Architectural Invariant

The following rule is non-negotiable and must be verified at each conformance review:

> Reproductive-cycle observation data (any tier, any class defined in this spec) must never appear in: (a) any network-bound payload, (b) any cloud analytics pipeline, (c) any third-party SDK call, (d) any clinician integration payload, or (e) any research data export. The only permitted boundary crossing is the `CyclePhaseEstimate` under explicit `reproductive_cycle.phase_covariate` consent, and even that crossing must carry no dates, biomarker values, or identifying context.

---

## 7. SensorDescriptors (Normative YAML)

```yaml
# HealthKit reproductive adapter
adapter_id: org.cytognosis.yar.healthkit.repro
display_name: "Apple Health (cycle)"
adapter_class: reproductive_cycle_sensing
maturity: beta
modalities: [reproductive_cycle]
axes_produced:
  - yar.repro.cycle_phase
  - yar.repro.cycle_day
  - yar.repro.menstrual_flow
  - yar.repro.bbt
  - yar.repro.cervical_mucus
  - yar.repro.ovulation_test
privacy_tier: on_device_only          # all raw observations; phase covariate upgrades separately
requires_consent:
  - reproductive_cycle.flow_log
  - reproductive_cycle.biomarkers
  - reproductive_cycle.healthkit
schema_ref: "cytos/schemas/domains/sensor/vendors/vendor_healthkit_repro.yaml"
implementation_ref: "04-Engineering/yar/sensors/implementing-healthkit.md"

---
# Google Health API cycle adapter
adapter_id: org.cytognosis.yar.googlehealth.cycle
display_name: "Google Health (cycle)"
adapter_class: reproductive_cycle_sensing
maturity: beta
modalities: [reproductive_cycle]
axes_produced:
  - yar.repro.cycle_phase
  - yar.repro.cycle_day
  - yar.repro.menstrual_flow
privacy_tier: on_device_only
requires_consent:
  - reproductive_cycle.flow_log
  - reproductive_cycle.google_health
schema_ref: "cytos/schemas/domains/sensor/vendors/vendor_googlehealth_cycle.yaml"
implementation_ref: "04-Engineering/yar/sensors/implementing-googlehealth.md"
# NOTE: Fitbit Web API deprecated September 2026. This adapter uses Google Health API exclusively.

---
# Manual logging adapter
adapter_id: org.cytognosis.yar.menstrual.log
display_name: "Cycle log (manual)"
adapter_class: reproductive_cycle_sensing
maturity: stable
modalities: [reproductive_cycle]
axes_produced:
  - yar.repro.cycle_phase
  - yar.repro.cycle_day
  - yar.repro.menstrual_flow
  - yar.repro.bbt
  - yar.repro.cervical_mucus
  - yar.repro.ovulation_test
  - yar.repro.symptom_burden
privacy_tier: on_device_only
requires_consent:
  - reproductive_cycle.flow_log
  - reproductive_cycle.biomarkers
  - reproductive_cycle.symptoms
schema_ref: "cytos/schemas/domains/sensor/core/selfreport.yaml"   # extends SurveyInstrument
implementation_ref: "04-Engineering/yar/sensors/implementing-menstrual-log.md"

---
# On-device phase estimator (produces CyclePhaseEstimate)
adapter_id: org.cytognosis.yar.menstrual.estimator
display_name: "Cycle phase estimator"
adapter_class: reproductive_cycle_sensing
maturity: beta
modalities: [reproductive_cycle]
axes_produced:
  - yar.repro.cycle_phase
  - yar.repro.phase_covariate   # boundary_derived only under phase_covariate consent
privacy_tier: on_device_only          # default; phase_covariate upgrades to boundary_derived
requires_consent:
  - reproductive_cycle.flow_log       # at minimum
  - reproductive_cycle.phase_covariate  # required if covariate is to cross boundary
schema_ref: "cytos/schemas/domains/sensor/vendors/vendor_healthkit_repro.yaml"
implementation_ref: "04-Engineering/yar/sensors/implementing-menstrual-estimator.md"
```

---

## 8. Storage: CRDT Op-Log Examples

All observations are CRDT `append` operations on the op-log (Layer 2, SPEC-storage-engine.md). Reproductive-cycle observations are stored in an isolated op-log partition (see Open Question O-1) with additional access controls.

### 8.1 MenstrualFlowObs Op-Log Entry

```yaml
# CRDT op-log entry: menstrual flow observation (on_device_only)
op_id: "crdt:op/menstrual-flow-20260622"
op_type: append
partition: reproductive_cycle          # isolated partition; elevated access control
vector_clock: {...}
payload_type: MenstrualFlowObs
payload:
  observation_id: "menstrual-flow-20260622"
  adapter_id: "org.cytognosis.yar.menstrual.log"
  axis_ref:
    axis_id: yar.repro.menstrual_flow
    axis_label: "Menstrual flow level"
    domain: reproductive_cycle
    value_type: ordinal
  timestamp: "2026-06-22T08:00:00Z"
  result:
    coded_value: "medium"              # MenstrualFlowLevelEnum value
  provenance:
    source_device: "manual-entry"
    collection_method: active
    raw_data_location: "/on-device/repro/log/20260622.json"
  consent_ref: "consent:grant/reproductive_cycle.flow_log/xyz"
  privacy_tier: on_device_only        # never crosses boundary
  source_adapter: manual
  data_entry_mode: active
  cycle_day: 2
  quality_flags: []
```

### 8.2 CyclePhaseEstimate Op-Log Entry (boundary_derived variant)

```yaml
# CRDT op-log entry: cycle phase estimate (boundary_derived, after explicit opt-in)
op_id: "crdt:op/cycle-phase-est-20260622"
op_type: append
partition: reproductive_cycle
vector_clock: {...}
payload_type: CyclePhaseEstimate
payload:
  observation_id: "cycle-phase-est-20260622"
  adapter_id: "org.cytognosis.yar.menstrual.estimator"
  axis_ref:
    axis_id: yar.repro.phase_covariate
    axis_label: "Cycle phase (covariate scalar)"
    domain: contextual_covariate
    value_type: continuous
    biolink_class: biolink:PhenotypicFeature
  timestamp: "2026-06-22T08:01:00Z"
  result:
    scalar: 0.0                        # 0 = menstrual phase
  provenance:
    source_device: "on-device-estimator-v0.1"
    collection_method: inferred
    raw_data_location: "/on-device/repro/estimates/20260622.json"
  consent_ref: "consent:grant/reproductive_cycle.phase_covariate/abc"
  privacy_tier: boundary_derived       # only because phase_covariate consent is active
  phase: menstrual
  phase_confidence: high
  estimated_cycle_day: 2
  days_since_period_start: 1
  data_inputs_used: [period_log, historical_pattern]
  # No raw dates, biomarker values, or flow data in this payload.
  quality_flags: []
```

### 8.3 MenstrualSymptomObs Op-Log Entry

```yaml
op_id: "crdt:op/symptom-fog-20260622"
op_type: append
partition: reproductive_cycle
payload_type: MenstrualSymptomObs
payload:
  observation_id: "symptom-fog-20260622"
  adapter_id: "org.cytognosis.yar.menstrual.log"
  axis_ref:
    axis_id: yar.repro.symptom_burden
    axis_label: "Cycle-associated symptom burden"
    domain: reproductive_cycle
    value_type: continuous
  timestamp: "2026-06-22T09:00:00Z"
  result:
    coded_value: "cognitive_fog"       # MenstrualSymptomTypeEnum
  provenance:
    source_device: "manual-entry"
    collection_method: active
    raw_data_location: "/on-device/repro/symptoms/20260622.json"
  consent_ref: "consent:grant/reproductive_cycle.symptoms/xyz"
  privacy_tier: on_device_only
  symptom_type: cognitive_fog
  severity: moderate
  data_entry_mode: active
  cycle_day: 2
```

---

## 9. Conformance and Acceptance Criteria

### 9.1 All Reproductive-Cycle Adapters

- **REQ-REPRO-001**: The system shall reject any `ReproductiveCycleObservation` that does not carry an active `consent_ref` matching the `reproductive_cycle.*` scope required by that observation class.
- **REQ-REPRO-002**: The system shall write every accepted reproductive-cycle observation to the `reproductive_cycle` partition of the CRDT op-log as an `append` operation before acknowledging acceptance to the adapter.
- **REQ-REPRO-003**: The system shall enforce `on_device_only` privacy tier at the CAP PEP for all `ReproductiveCycleObservation` subclasses except `CyclePhaseEstimate` under active `reproductive_cycle.phase_covariate` consent.
- **REQ-REPRO-004**: The system shall log every CAP `Directive` and `GuardDecision` for reproductive-cycle observations with `sensitivity_level: reproductive` in the local audit chain.
- **REQ-REPRO-005**: The system shall never include any reproductive-cycle observation in any network-bound payload, analytics pipeline, third-party SDK call, clinician integration, or research export, regardless of consent scope, except for the `CyclePhaseEstimate` under `reproductive_cycle.phase_covariate` consent as specified in this document.
- **REQ-REPRO-006**: When consent for any `reproductive_cycle.*` scope is withdrawn, the system shall stop accepting observations under that scope within one session and shall not queue pending observations.
- **REQ-REPRO-007**: The system shall provide a user-accessible deletion function for all reproductive-cycle data that irreversibly removes all observations (including CRDT tombstones from the isolated partition) and propagates deletion to all synced nodes within the next sync session.
- **REQ-REPRO-008**: The system shall expose a user-accessible export function that produces all reproductive-cycle observations as a user-controlled file delivered to the local device, without any server transmission.

### 9.2 HealthKit and Google Health Adapters

- **REQ-HK-001**: The HealthKit adapter shall request authorization for only the `HKCategoryTypeIdentifier` values listed in Section 3.1 as "Ingested by Yar: Yes". It shall not request authorization for `pregnancy`, `lactation`, `contraceptive`, or `sexualActivity`.
- **REQ-HK-002**: The HealthKit adapter shall not ingest `HKCategoryTypeIdentifier.pregnancyTestResult` or `HKCategoryTypeIdentifier.pregnancy` samples; if encountered in a HealthKit query response, those samples must be silently dropped before any persistence.
- **REQ-GH-001**: The Google Health cycle adapter shall target the Google Health API exclusively. No code path may call the legacy Fitbit Web API after September 2026 deprecation.

### 9.3 On-Device Estimator

- **REQ-EST-001**: The `CyclePhaseEstimate` payload written to the op-log shall not contain raw period dates, BBT values, mucus quality values, ovulation test results, or any data that could identify a specific cycle event. It shall contain only: `phase`, `phase_confidence`, `estimated_cycle_day`, `days_since_period_start`, and `data_inputs_used`.
- **REQ-EST-002**: When `CyclePhaseEstimate.phase = unknown`, the system shall write `null` to the `yar.repro.phase_covariate` axis (not 0 or any other default value) and shall set `phase_confidence = low`.
- **REQ-EST-003**: The on-device estimator shall run entirely in the app process with no network calls. Any update to the estimator model must be a local algorithm update delivered via app update, not a server-side model push.

### 9.4 Manual Logging Adapter

- **REQ-LOG-001**: The manual log adapter shall never accept free-text input for any field. All symptom, flow, mucus, and test result fields are enumeration-constrained at the schema and UI layer.
- **REQ-LOG-002**: The manual log adapter shall present consent UI before accepting the first log entry in each session. If `reproductive_cycle.flow_log` consent is not active, the log form must not be rendered.

### 9.5 Affirming Language

- **REQ-LANG-001**: No user-facing label, axis name, notification, or UI text produced by this spec's adapters shall use the words "normal," "abnormal," "irregular" (as a user-facing label), "regular," or any diagnostic term. Cycle variation is described as "cycle pattern varies" or "phase estimation paused."
- **REQ-LANG-002**: User-facing references to the user's cycle must use inclusive language: "your cycle," "the cycle," or "cycle phase." Gendered terms are not used.
- **REQ-LANG-003**: The severity vocabulary for `MenstrualSymptomObs` uses the CSP controlled vocabulary: `low | moderate | elevated | high`. Never "severe" as a displayable label without clinical qualification.

---

## 10. Open Questions

| # | Question | Current leaning | Blocker |
|---|---|---|---|
| O-1 | Should reproductive-cycle observations be stored in an isolated op-log partition with separate encryption and access control, or in the main op-log with an access-control layer? | Isolated partition strongly preferred given legal risk; adds implementation complexity | SPEC-storage-engine.md must define partition semantics; assign there |
| O-2 | Does the Google Health API expose enough cycle data to be meaningful, or is manual logging the primary path? | Manual log is the primary path; Google Health supplements with period-start/end dates only | Verify Google Health API cycle data types against actual API documentation when access is available |
| O-3 | Should BBT wearable proxy (Oura/Fitbit skin temperature) be enabled by default when the user has a wearable connected, or require explicit opt-in? | Explicit opt-in; cross-sensor correlation of reproductive data requires a clear disclosure | UX design; legal review of cross-sensor data use |
| O-4 | Should the on-device estimator be upgraded to a local ML model (e.g., from the 2025 npj Women's Health study)? | Future enhancement; rule-based is correct for v0.1 | Research into on-device model size vs. accuracy tradeoff; labeled cycle data for validation |
| O-5 | Mira fertility analyzer integration (vendor_mira.yaml stub in cytos) — should it be added to this spec? | Deferred to v0.2; Mira provides quantitative hormone levels (LH, estrogen), which raises additional sensitivity questions | SPEC-sensor-physiological.md Open item O-6; coordinate there |
| O-6 | Should `MenstrualSymptomObs` feed into the PMDD-aware mood axis, or is that entirely the domain of `SPEC-neurobehavioral-axes.md`? | SPEC-neurobehavioral-axes.md owns the integration; this spec only produces the symptom observations | Blocked on neurobehavioral-axes spec (CSP O-8) |
| O-7 | What is the correct op-log deletion semantics for `on_device_only` reproductive-cycle data when the user requests deletion? Standard CRDT tombstoning is not true deletion. | Secure overwrite of the isolated partition's encrypted data store; CRDT tombstones for any synced copies | Sync protocol decision (SPEC-sync-protocol.md) must address physical deletion |
| O-8 | Cross-cycle longitudinal analysis (e.g., detecting cycle-length drift over months): should Yar surface this to the user? | Yes, as a behavioral regularity insight, with affirming language; detail in SPEC-neurobehavioral-axes.md | Out of scope for this spec |

---

## 11. References

1. Robberecht G, et al. "Menstrual Cycle-Related Hormonal Fluctuations in ADHD: Effect on Cognitive Functioning — A Narrative Review." *Journal of Clinical Medicine*, 2026; MDPI doi:10.3390/jcm15010121. PMC12786913. URL: https://pmc.ncbi.nlm.nih.gov/articles/PMC12786913/
2. ADDitude Magazine. "The Menstrual Cycle Impacts ADHD Symptoms in Disparate Ways." URL: https://www.additudemag.com/adhd-and-periods-menstrual-cycle-hormones/
3. Getinflow.io. "PMDD, Estrogen, and Dopamine: How ADHD Is Affected by Severe PMS." 2024. URL: https://www.getinflow.io/post/pmdd-estrogen-dopamine-adhd-affected-by-severe-pms
4. npj Women's Health. "Machine learning-based menstrual phase identification using wearable device data." 2025. URL: https://www.nature.com/articles/s44294-025-00078-8
5. JMIR. "Oura Ring as a Tool for Ovulation Detection: Validation Analysis." 2025. URL: https://www.jmir.org/2025/1/e60667
6. Apple Developer Documentation. "HKCategoryTypeIdentifier — menstrualFlow." URL: https://developer.apple.com/documentation/healthkit/hkcategorytypeidentifier/menstrualflow
7. Apple Developer Documentation. "HKCategoryTypeIdentifier — cervicalMucusQuality." URL: https://developer.apple.com/documentation/healthkit/hkcategorytypeidentifier/cervicalmucusquality
8. Apple Developer Documentation. "HKCategoryTypeIdentifier — ovulationTestResult." URL: https://developer.apple.com/documentation/healthkit/hkcategorytypeidentifier/1615252-ovulationtestresult
9. Apple Developer Documentation. "HKCategoryTypeIdentifier — infrequentMenstrualCycles." URL: https://developer.apple.com/documentation/healthkit/hkcategorytypeidentifier/infrequentmenstrualcycles
10. Apple Developer Documentation. "basalBodyTemperature (HKQuantityTypeIdentifier)." URL: https://developer.apple.com/documentation/healthkit/hkquantitytypeidentifier/1615763-basalbodytemperature
11. Google / Fitbit Community. "Introducing the next phase of the Fitbit Web API." 2026. URL: https://community.fitbit.com/t5/Web-API-Development/Introducing-the-next-phase-of-the-Fitbit-Web-API/td-p/5821061
12. TryTerra. "The complete guide: How the new Google Health API works." 2025-2026. URL: https://tryterra.co/blog/everything-you-need-to-know-about-google-health-new-api
13. LOINC. "8665-2 Last menstrual period start date." URL: https://loinc.org/8665-2
14. LOINC. "10564-3 Cervical mucus [Volume]." URL: https://loinc.org/10564-3/
15. LOINC. "64700-8 Typical menstrual cycle length [PhenX]." URL: https://loinc.org/64700-8
16. HL7 Australia Base FHIR R4. "au-lastmenstrualperiod StructureDefinition." URL: https://hl7.org.au/fhir/4.0.0/StructureDefinition-au-lastmenstrualperiod.html
17. IAPP. "The State of US Reproductive Privacy in 2025: Trends and Operational Considerations." URL: https://iapp.org/news/a/the-state-of-us-reproductive-privacy-in-2025-trends-and-operational-considerations
18. arXiv. "Privacy and Security of Women's Reproductive Health Apps in a Changing Legal Landscape." 2024. URL: https://arxiv.org/pdf/2404.05876
19. US District Court, Northern District of Texas. Order vacating HIPAA Reproductive Health Privacy Rule. June 18, 2025. Reported by: https://www.apaservices.org/practice/business/hipaa/july-2025-court-decision-reproductive-health-privacy-rule
20. HHS.gov. "HIPAA and Reproductive Health." URL: https://www.hhs.gov/hipaa/for-professionals/special-topics/reproductive-health/index.html

---

## 12. Cross-References

| Document | Relationship |
|---|---|
| `Yar/spec/SPEC-CSP.md` | Anchor protocol; adapter lifecycle, `SensorDescriptor`, `CSPObservation`, privacy tiers all defined there |
| `Yar/spec/SPEC-sensor-physiological.md` | Companion spec; CSP binding patterns, CRDT op-log examples, and `CrossBoundarySignal` table style reused here |
| `Cytoplex/spec/privacy-boundary-spec.md` | Privacy tier classification; `CrossBoundarySignal` schema; PB-1 through PB-10 apply |
| `Cytoplex/spec/03_primitives.md` | CAP primitive types: `Directive`, `GuardDecision`, `DecisionRecord` |
| `Yar/spec/SPEC-storage-engine.md` | CRDT op-log (L2); isolated partition semantics (O-1); physical deletion semantics (O-7) |
| `Yar/spec/SPEC-sync-protocol.md` | L2 CRDT replication; physical deletion on sync (O-7) |
| `SPEC-neurobehavioral-axes.md` (planned) | Consumes `yar.repro.phase_covariate` as a contextual covariate for mood/cognition axes |
| `04-Engineering/cytos/sensing-schema/unified-sensor-report.md` | Cytos LinkML schema tree; `vendor_mira.yaml` stub for future Mira integration |
| `04-Engineering/yar/sensors/implementing-healthkit.md` (planned) | HealthKit adapter implementation detail |
| `04-Engineering/yar/sensors/implementing-menstrual-log.md` (planned) | Manual logging adapter implementation detail |
| `04-Engineering/yar/sensors/implementing-menstrual-estimator.md` (planned) | On-device phase estimator implementation detail |
