---
title: "Cytos Universal Sensor Schema"
date: "2026-05-25"
source: "migrated from org/plans"
category: "research"
status: "current"
tags:
  - cytognosis
  - research
---

# Cytos Universal Sensor Schema

> **Status**: v0.2 (Design Specification)
> **Date**: 2026-05-24
> **Authors**: Cytognosis Foundation
> **Scope**: Comprehensive schema for encoding every health-tracking sensor, from wearables and voice biomarkers to clinical labs and cellular assays, under a single interoperable LinkML standard.

---

## Table of Contents

1. [Current State Inventory](#1-current-state-inventory)
2. [AWARE Schema Status](#2-aware-schema-status)
3. [Design Patterns Established](#3-design-patterns-established)
4. [Gaps and Design Proposals](#4-gaps-and-design-proposals)
5. [Proposed New Profiles](#5-proposed-new-profiles)
6. [PhysioNet mcPHASES Dataset Mapping](#6-physionet-mcphases-dataset-mapping)
7. [Sensor as MCP/Plugin System](#7-sensor-as-mcpplugin-system)
8. [Reference Standards Alignment](#8-reference-standards-alignment)

---

## 1. Current State Inventory

The Cytognosis sensor infrastructure spans three repositories (`cytos`, `Yar`, `org`) and already implements a mature, standards-aligned LinkML schema family. This section catalogs every existing sensor-related schema and code artifact.

### 1.1 cytos/schemas/domains/sensor/ (Primary Schema Family)

The primary sensor schema is a comprehensive LinkML schema family organized into **core**, **profiles**, **vendors**, and **examples**. It represents the most mature component of the Cytos data model.

```
schemas/domains/sensor/
├── sensor.yaml                  Umbrella import (all profiles + vendors)
├── core/
│   ├── core.yaml                Spine: Subject, Device, Sensor, Channel, Platform,
│   │                            Deployment, Session, Observation, ObservationCollection,
│   │                            Result, WaveformResult, Stream, UnitValue, TimeFrame,
│   │                            SystemCapability, CalibrationState, ObservationQuality
│   ├── selfreport.yaml          SurveyInstrument, SurveyResponse, ESMPrompt (IEEE 1752
│   │                            survey + AWARE ESM)
│   └── context.yaml             Mobile context: LocationFix, ScreenEvent, AppForegroundEvent,
│                                NotificationEvent, CommunicationEvent, ActivityRecognitionEvent,
│                                BatteryEvent, NetworkEvent (AWARE pattern, privacy-preserving)
├── profiles/
│   ├── profile_sosa.yaml        W3C SOSA/SSN class/slot URI bindings
│   ├── profile_ieee1752.yaml    IEEE 1752.1 / Open mHealth body-schema mirror
│   ├── profile_fhir.yaml        FHIR R5 Observation/Device/DeviceMetric/DeviceUsage + Vitals
│   ├── profile_bt_ghs.yaml      Bluetooth GHS + IEEE 11073-10206 ACOM semantics
│   ├── profile_aware.yaml       AWARE framework smartphone sensors
│   └── profile_mcphases.yaml    Test-case profile: PhysioNet mcPHASES dataset
├── vendors/
│   ├── vendor_cytoscope.yaml    Cytognosis Cytoscope (placeholder, draft)
│   ├── vendor_fitbit.yaml       Fitbit consumer wearables
│   ├── vendor_dexcom.yaml       Dexcom CGM
│   ├── vendor_mira.yaml         Mira fertility analyzer
│   └── vendor_oura.yaml         Oura Ring (example third-party plug-in)
└── examples/
    └── mcphases_example.yaml    Synthetic mcPHASES participant, validates clean
```

#### 1.1.1 Core Schema (`core/core.yaml`, 1461 lines)

The spine of the universal sensor standard. Defines 35+ classes aligned with W3C SOSA/SSN at the class and slot URI level, IEEE 1752.1 at the semantics level, and FHIR R5 at the clinical interoperability level.

**Entity classes:**

| Class | SOSA/FHIR Alignment | Purpose |
|-------|---------------------|---------|
| `SensorEntity` | Abstract root | Root base for all sensor entities |
| `SensorDataset` | `prov:Bundle` | Tree root container for all sensor data exports |
| `Subject` | `sosa:FeatureOfInterest` | Human or animal participant |
| `FeatureOfInterest` | `sosa:FeatureOfInterest` | Real-world entity being observed |
| `BiologicalSample` | `sosa:Sample` | Biological specimen from a Subject |
| `Device` | `fhir:Device` | Physical artifact hosting Sensors (Fitbit, Dexcom, etc.) |
| `Sensor` | `sosa:Sensor` | Procedure-and-device combo producing Observations |
| `Channel` | `ssn:System` | Single logical data channel of a multi-channel Sensor |
| `Platform` | `sosa:Platform` | Host for Sensors (body, bench, ambient) |
| `Deployment` | `ssn:Deployment` | Act of deploying a Sensor onto a FeatureOfInterest |
| `Session` | `prov:Activity` | Bounded data-collection session with time alignment |
| `Observation` | `sosa:Observation` | Single observation with typed Result |
| `ObservationCollection` | `sosa:ObservationCollection` | Time series or multi-channel groupings |
| `Result` | `sosa:hasResult` | Polymorphic result (scalar, coded, range, compound, waveform, attachment) |
| `ObservableProperty` | `sosa:ObservableProperty` | Property being measured (HR, glucose, mood, PHQ-9 total) |
| `Procedure` | `sosa:Procedure` | Workflow, protocol, or algorithm used to obtain an Observation |
| `Stream` | — | Continuous data stream with blob references |
| `SystemCapability` | `ssn-system:SystemCapability` | Declared capability (accuracy, range, drift) |
| `CalibrationState` | — | Time-indexed calibration state |
| `ObservationQuality` | — | Quality flags and reasons |
| `ObservationHeader` | IEEE 1752.1 header | Universal envelope header (UUID, schema ID, modality) |
| `UnitValue` | `fhir:Quantity` | Scalar quantity with UCUM units |
| `TimeFrame` | IEEE 1752.1 | Point-in-time or interval |

**Key enum types:**

| Enum | Values (count) | Notable entries |
|------|---------------|-----------------|
| `DeviceTypeEnum` | 12 | `consumer_wearable`, `smartphone`, `medical_device`, `self_report_instrument`, `lab_instrument`, `environmental_sensor` |
| `DeviceCategoryEnum` | 14 | `wrist_worn`, `ring`, `patch`, `cgm_transmitter`, `hormone_analyzer`, `handheld_analyzer`, `implantable` |
| `SensorModalityEnum` | 30+ | `ppg`, `accelerometer`, `ecg`, `eda`, `cgm_amperometric`, `hormonal_assay`, `self_report_likert`, `smartphone_context`, `voice_acoustic`, `ai_inference` |
| `PropertyClassEnum` | 11 | `vital_sign`, `hormonal`, `behavioral`, `survey`, `derived_biomarker`, `environmental` |
| `ModalityEnum` | 9 | `sensed`, `self_reported`, `ai_inferred`, `lab_assay`, `clinician_entered` |
| `ResultTypeEnum` | 11 | `scalar`, `coded`, `string`, `boolean`, `integer`, `range`, `ratio`, `compound`, `waveform`, `attachment` |
| `PlatformTypeEnum` | 7 | `body_worn`, `benchtop`, `ambient`, `vehicle`, `room`, `subject_self` |
| `SensorScaleEnum` | 10 | `molecular`, `cellular`, `tissue`, `organ`, `organism`, `population`, `environmental`, `clinical` |

**Custom types defined:**

- `Hertz`: Sampling rate in Hz (xsd:double)
- `Seconds`: Duration in seconds (xsd:double)
- `UCUMCode`: UCUM unit expression (xsd:string)
- `Hex`: Hex-encoded binary for raw GATT/MET round-trip (xsd:hexBinary)
- `Base64`: Base64-encoded binary for waveform blob references (xsd:base64Binary)

#### 1.1.2 Self-Report Schema (`core/selfreport.yaml`, 199 lines)

Self-report and ecological-momentary-assessment (ESM/EMA) extensions aligned with IEEE 1752.1 survey package and AWARE ESM.

| Class | Alignment | Purpose |
|-------|-----------|---------|
| `SurveyInstrument` | `fhir:Questionnaire`, is_a `Procedure` | Named survey instrument (PHQ-9, GAD-7, daily Likert) |
| `SurveyResponse` | `fhir:QuestionnaireResponse`, is_a `Observation` | A completed survey instance |
| `SurveyItemAnswer` | — | Single item answer with typed value |
| `ESMPrompt` | is_a `SurveyInstrument` | EMA prompt with contextual trigger |

**SurveyInstrument attributes:**

- `instrument_local_id`, `instrument_name`, `instrument_version`
- `questionnaire_code` (LOINC)
- `items` (list of `SurveyItem`)
- `scoring_algorithm`, `score_range`, `cutoff_thresholds`
- `administration_mode`, `estimated_minutes`
- `normative_reference`, `validation_reference`

**SurveyAnswerTypeEnum** values (14): `likert`, `visual_analog`, `numeric`, `categorical_single`, `categorical_multiple`, `free_text`, `date`, `time`, `duration`, `unit_value`, `pam_image`, `web`, `attachment`, `boolean`

**ESMTriggerEnum** values (7): `scheduled`, `random_within_window`, `location_based`, `activity_based`, `sensor_threshold`, `app_event`, `user_initiated`

#### 1.1.3 Context Schema (`core/context.yaml`, 256 lines)

Smartphone and ambient-context extensions modeled after AWARE framework's behavioral and contextual sensors.

| Class | Purpose |
|-------|---------|
| `LocationFix` | Geolocation observation (lat, lon, altitude, bearing, speed, accuracy, provider) |
| `ScreenEvent` | Screen on/off/locked/unlocked events |
| `AppForegroundEvent` | App usage tracking (app hash, duration) |
| `NotificationEvent` | Notification metadata (app hash, action) |
| `CommunicationEvent` | Call/SMS events (privacy-preserving hashed contacts) |
| `ActivityRecognitionEvent` | Recognized activities (still, walking, running, biking, in_vehicle) |
| `BatteryEvent` | Battery level, status, plugged state |
| `TouchEvent` | Touch gesture events |
| `KeyboardEvent` | Keyboard interaction metrics |
| `InstallationEvent` | App install/update/uninstall events |
| `NetworkEvent` | Network connectivity events |

All context events inherit from `Observation` and use privacy-preserving design (hashed identifiers, no raw content).

### 1.2 Profiles (6 profiles)

#### profile_sosa.yaml (80 lines)

Binds core classes to W3C SOSA/SSN class and slot URIs. No new classes introduced. Imports only add annotations for lossless RDF round-trip (Turtle, JSON-LD). Includes platform subtypes: `BodyWornPlatform`, `SubjectPlatform`, `BenchtopPlatform`, `AmbientPlatform`.

#### profile_ieee1752.yaml (9180 bytes)

Mirrors IEEE 1752.1 / Open mHealth body schemas. Covers all major health data types:

- Heart rate, blood pressure, body temperature, BMI
- Blood glucose, SpO2, respiratory rate
- Step count, physical activity, calories
- Sleep episode, geoposition
- Ambient light/sound/temperature
- Pain, mood, body weight/height

#### profile_fhir.yaml (265 lines)

Maps to FHIR R5 resources:

| Cytos Class | FHIR R5 Resource |
|-------------|-----------------|
| `FHIRObservation` | `fhir:Observation` (status, code, category, value[x]) |
| `FHIRDevice` | `fhir:Device` |
| `FHIRDeviceMetric` | `fhir:DeviceMetric` |
| `FHIRDeviceUsage` | `fhir:DeviceUsage` |
| `FHIRVitalSignsObservation` | FHIR Vital Signs profile family |
| `FHIRExtension` | `fhir:Extension` (URL + value[x]) |

Enums: `FHIRObservationStatusEnum` (8 values), `FHIRObservationCategoryEnum` (9 values including `vital_signs`, `laboratory`, `survey`, `activity`, `social_history`).

#### profile_bt_ghs.yaml (199 lines)

Aligns with Bluetooth SIG Generic Health Sensor (GHS) profile and IEEE 11073-10206 ACOM:

- `GHSDevice`: BLE device with GATT service UUID, specialization MDC codes
- `GHSObservation`: 9 observation classes (numeric, simple_discrete, string, sample_array, compound_discrete, compound_state_event, compound_numeric, tlv, bundle)
- Measurement-status bitfield, MDC code bindings, ETS clock semantics
- Optional raw-MET round-trip via Hex slot

#### profile_aware.yaml (233 lines)

See [Section 2: AWARE Schema Status](#2-aware-schema-status).

#### profile_mcphases.yaml (567 lines)

Test-case profile mapping every modality and column in the PhysioNet mcPHASES dataset. See [Section 6: PhysioNet mcPHASES Dataset Mapping](#6-physionet-mcphases-dataset-mapping).

### 1.3 Vendor Profiles (5 vendors)

#### vendor_fitbit.yaml (110 lines)

Fitbit consumer wearable profile with 19 Observation subclasses:

| Class | Source |
|-------|--------|
| `FitbitDevice` | Device subclass (consumer_wearable) |
| `FitbitHeartRate` | Continuous HR with vendor confidence |
| `FitbitRestingHeartRate` | Daily resting HR |
| `FitbitHRVDetails` | 5-min HRV during sleep (RMSSD, LF, HF) |
| `FitbitRespiratoryRateSummary` | Per-night breathing rate by sleep stage |
| `FitbitSteps` | Step count |
| `FitbitDistance` | Distance |
| `FitbitAltitude` | Altitude/floors |
| `FitbitCalories` | Calorie expenditure |
| `FitbitActivityMinutes` | Activity intensity buckets |
| `FitbitActiveZoneMinutes` | Heart-rate zone time |
| `FitbitTimeInHRZones` | Time in HR zones |
| `FitbitExerciseSession` | Exercise sessions |
| `FitbitSleepSession` | Sleep sessions with stages |
| `FitbitSleepScore` | Composite sleep score |
| `FitbitStressScore` | Stress management score |
| `FitbitVO2Max` | Demographic VO2 max estimate |
| `FitbitNightlySkinTemperature` | Nightly skin temp summary |
| `FitbitWristTemperatureSample` | Wrist temp delta from baseline |
| `FitbitEstimatedOxygenVariation` | Nocturnal SpO2 variation |

#### vendor_dexcom.yaml (77 lines)

Dexcom CGM profile:

- `DexcomDevice`: Medical device (cgm_transmitter), supports G6/G7/Stelo
- `DexcomGlucoseObservation`: Interstitial glucose with session ID, transmitter ID, trend arrow, rate of change, calibration status, sensor state
- `DexcomTrendEnum`: 9 values (double_up through rate_out_of_range)
- `DexcomSensorStateEnum`: 7 values (ok, warmup, stopped, failed, etc.)

#### vendor_mira.yaml (61 lines)

Mira fertility analyzer profile:

- `MiraDevice`: Diagnostic device (handheld hormone analyzer)
- `MiraHormoneObservation` (abstract): Base with assay lot, test strip ID
- `MiraLHObservation`: Luteinizing hormone (mIU/mL)
- `MiraE3GObservation`: Estrone-3-glucuronide (ng/mL)
- `MiraPDGObservation`: Pregnanediol glucuronide (mcg/mL)
- `MiraCyclePhaseInference`: Inferred menstrual cycle phase

#### vendor_oura.yaml (63 lines)

Oura Ring (Gen 3/4) vendor profile demonstrating third-party plug-in pattern:

- `OuraDevice`: Consumer wearable (ring form factor)
- `OuraHeartRate`, `OuraHRV`, `OuraSkinTemperature`
- `OuraSleepSession`, `OuraSleepStages`
- `OuraActivityDay`, `OuraReadinessScore`
- `OuraCycleInsight`: Menstrual cycle feature

#### vendor_cytoscope.yaml (77 lines, DRAFT)

Cytognosis Cytoscope biosensor (in-development):

- `CytoscopeDevice`: Medical device (patch form factor)
- `CytoscopeAssayChannel`: Assay channel with target analyte (CHEBI/NCIT/HGNC), LOD, readout modality
- `CytoscopeObservation`: Observation with edge-AI inference label
- `CytoscopeFormFactorEnum`: patch, wearable_module, handheld, implantable, benchtop_reader

### 1.4 Registries (`schemas/registries/registries.yaml`, 279 lines)

Instance-level catalog data complementing the type-level profiles:

| Registry Class | Purpose | Key Fields |
|---------------|---------|------------|
| `VendorRegistryEntry` | Vendor catalog | `vendor_id`, `display_name`, `homepage`, `api_base_url`, `auth_method` |
| `DeviceRegistryEntry` | Device model catalog | `device_id`, `vendor_id`, `model_name`, `device_type`, `regulatory_class`, `fda_510k`, `ce_mark` |
| `ObservablePropertyRegistryEntry` | Observable property catalog | `property_id`, LOINC/SNOMED/MDC/HPO codes, `preferred_unit`, `property_class` |
| `UnitRegistryEntry` | Unit catalog | `unit_id`, UCUM code, QUDT/UO/MDC codes |
| `BodySiteRegistryEntry` | Body site catalog | `body_site_id`, UBERON/SNOMED codes, `laterality` |
| `ProcedureRegistryEntry` | Procedure catalog | `procedure_id`, LOINC/SNOMED/OBI/MDC codes |
| `SensorChannelRegistryEntry` | (Device, Channel, ObservableProperty) triple | `channel_id`, `device_id`, `property_id`, `unit_id`, `sampling_rate_hz`, `body_site_id`, `modality` |

### 1.5 Yar Sensor Architecture (Runtime Layer)

The Yar repository contains the runtime implementation of the sensor framework for Cytonome.

#### Sensor Descriptor System (`Yar/docs/architecture/sensor_architecture.md`, 380 lines)

Defines the pluggable sensor framework using Pydantic models:

- **`SensorDescriptor`**: Universal sensor registration with identity, classification, capabilities, output schema, hardware requirements, and dependencies
- **`SensorModality`** enum: `VOICE`, `TEXT`, `IMAGE`, `VIDEO`, `PHYSIOLOGICAL`, `MULTIMODAL`, `ENVIRONMENTAL`
- **`SensorCategory`** enum: `EMOTION`, `COGNITION`, `VITALS`, `SLEEP`, `ACTIVITY`, `SPEECH`, `SOCIAL`, `ENVIRONMENT`
- **`SensorPrivacyLevel`** enum: `BIOMETRIC`, `HEALTH`, `BEHAVIORAL`, `CONTEXTUAL`
- **`ObservationField`**: Output field definition (name, dtype, unit, description, clinical_relevance, range_min/max, enum_values)

#### Sensor Protocol (Interface)

```python
class Sensor(Protocol):
    @property
    def descriptor(self) -> SensorDescriptor: ...
    async def initialize(self) -> None: ...
    async def start(self, session_id: str) -> None: ...
    async def stop(self) -> None: ...
    async def observe(self, raw_input: bytes | None = None) -> SensorObservation: ...
    def stream(self, raw_input_stream: AsyncIterator[bytes]) -> AsyncIterator[SensorObservation]: ...
    async def teardown(self) -> None: ...
```

#### Sensor Registry

```python
class SensorRegistry:
    def list_available(self) -> list[SensorDescriptor]: ...
    def list_active(self) -> list[SensorDescriptor]: ...
    async def connect(self, sensor_id: str) -> None: ...
    async def disconnect(self, sensor_id: str) -> None: ...
    def get_sensor(self, sensor_id: str) -> Sensor: ...
```

#### Voice Emotion Sensor (Instance 0)

The first implemented sensor, combining HuBERT + openSMILE eGeMAPSv02 for paralinguistic analysis. 13 output fields covering categorical emotion, dimensional affect (valence, arousal, dominance), and vocal biomarkers (pitch, jitter, shimmer, HNR, speech rate, pause metrics).

### 1.6 Yar Voice Affect Models (`Yar/src/yar/models/voice_affect.py`, 195 lines)

Production Pydantic models for the voice-affect subsystem:

| Model | Purpose |
|-------|---------|
| `AffectState` (enum) | Coarse emotional state: `NEUTRAL`, `ELEVATED`, `SUBDUED`, `MIXED`, `AGITATED` |
| `AffectTrend` (enum) | Trend direction: `STABLE`, `RISING`, `FALLING`, `VOLATILE` |
| `VoiceAffectSignal` | Single smoothed observation (state, trend, arousal, valence, confidence) |
| `VoiceAffectPolicy` | Privacy attestation (on_device, no_audio_stored, consent_given) |
| `VoiceAffectEvent` | Signal + policy, ready for persistence |
| `VoiceAffectEventEnvelope` | Wire wrapper for HTTP route |
| `VoiceAffectEventAck` | Compact acknowledgement |
| `VoiceAffectStateSnapshot` | Full state for a conversation (GET endpoint) |
| `VoiceAffectContextHint` | Only payload the response-style layer may consume |
| `VoiceAffectFeatureFlags` | Kill switches (emotion_tracking_enabled, context_injection, debug_ui) |
| `VoiceAffectConstants` | Numeric defaults (EMA alpha, window size, confidence floor) |

### 1.7 Clinical Domain Schema (`cytos/schemas/domains/clinical.yaml`, 145 lines)

Provisional LinkML schema for clinical entities from UMLS Metathesaurus and SNOMED CT:

- `ClinicalFinding`: Observation/condition with CUI, SNOMED ID, LOINC code, ICD-10 code, severity
- `ClinicalAttribute`: Measurable clinical parameter (CUI, SNOMED, units, reference range)
- `Procedure`: Clinical procedure with CUI, SNOMED, CPT code, procedure type
- `MedicalDevice`: Medical/research device with CUI, FDA classification, semantic type

### 1.8 NWB Domain Schema (`cytos/schemas/domains/nwb.yaml`, 282 lines)

LinkML mirrors of key HDMF/NWB types for neurophysiology data:

- `NWBFile`: Top-level container (session, subject, acquisition metadata)
- `NWBSubject`: Animal/human subject with species, genotype, weight
- `TimeSeries`: Core time-series with data array, timestamps, sampling rate
- `ElectrodeGroup`: Recording electrode group with location, device
- `SpikeUnit`: Sorted spike unit with quality metrics
- `Stimulus`: Visual, auditory, somatosensory, optogenetic stimuli

### 1.9 Example Instance Data

`examples/mcphases_example.yaml` (245 lines): A synthetic mcPHASES participant demonstrating one row per modality across all sensor types (Fitbit HR, HRV, skin temp, sleep, Dexcom glucose, Mira hormones + self-report). Validates clean against the mcPHASES profile schema.

---

## 2. AWARE Schema Status

The AWARE framework smartphone sensing schemas are **fully implemented** in the Cytos sensor schema. This section details the coverage.

### 2.1 Architecture

AWARE integration uses a two-layer design:

1. **`core/context.yaml`**: Defines generic smartphone context observation classes (LocationFix, ScreenEvent, AppForegroundEvent, etc.) independent of AWARE
2. **`profiles/profile_aware.yaml`**: AWARE-specific profile that subclasses context events with the `AWAREObservationMixin`, adding AWARE-canonical columns (`aware_label`, `aware_accuracy`)

### 2.2 AWARE Device

```yaml
AWAREDevice:
  is_a: Device
  description: An AWARE-managed smartphone or wearable.
  attributes:
    aware_device_uuid:
      range: string
      description: AWARE-assigned device UUID.
    study_id:
      range: string
    aware_micro_endpoint:
      range: uri
```

### 2.3 AWARE Observation Mixin

```yaml
AWAREObservationMixin:
  mixin: true
  description: Mixin adding the canonical AWARE columns.
  attributes:
    aware_label:
      range: string
      description: User-set free-text label for calibration/annotation.
    aware_accuracy:
      range: integer
      description: AWARE sensor accuracy enum (0-3).
```

### 2.4 Complete Sensor Coverage

| AWARE Sensor | Cytos Class | Base Class |
|-------------|-------------|------------|
| Accelerometer | `AWAREAccelerometer` | `Observation` + mixin |
| Gyroscope | `AWAREGyroscope` | `Observation` + mixin |
| Magnetometer | `AWAREMagnetometer` | `Observation` + mixin |
| Gravity | `AWAREGravity` | `Observation` + mixin |
| Light | `AWARELight` | `Observation` + mixin |
| Proximity | `AWAREProximity` | `Observation` + mixin |
| Barometer | `AWAREBarometer` | `Observation` + mixin |
| Temperature | `AWARETemperature` | `Observation` + mixin |
| Location | `AWARELocation` | `LocationFix` + mixin |
| Network | `AWARENetwork` | `NetworkEvent` + mixin |
| WiFi | `AWAREWifi` | `Observation` + mixin (bssid_hash, rssi, frequency) |
| Bluetooth | `AWAREBluetooth` | `Observation` + mixin (device_address_hash, rssi) |
| Screen | `AWAREScreen` | `ScreenEvent` + mixin |
| Telephony | `AWARETelephony` | `Observation` + mixin |
| Applications | `AWAREApplications` | `AppForegroundEvent` + mixin |
| Notifications | `AWARENotifications` | `NotificationEvent` + mixin |
| Communication | `AWARECommunication` | `CommunicationEvent` + mixin |
| Activity Recognition | `AWAREActivityRecognition` | `ActivityRecognitionEvent` + mixin |
| Processor | `AWAREProcessor` | `Observation` + mixin (cpu_load) |
| Battery | `AWAREBattery` | `BatteryEvent` + mixin |
| Installations | `AWAREInstallations` | `InstallationEvent` + mixin |
| Keyboard | `AWAREKeyboard` | `KeyboardEvent` + mixin |
| Touch | `AWARETouch` | `TouchEvent` + mixin |
| Scheduler | `AWAREScheduler` | `Observation` + mixin |
| ESM | `AWAREESM` | `ESMPrompt` + mixin |

### 2.5 Privacy-Preserving Design

All AWARE context classes follow the privacy-by-design principle established in `core/context.yaml`:

- **Contact hashing**: Communication events use `contact_hash` (SHA-256 of phone number), raw identifiers are hashed before persistence
- **App hashing**: App foreground events use `app_package_hash`
- **BSSID hashing**: WiFi events use `bssid_hash`
- **Device address hashing**: Bluetooth events use `device_address_hash`
- **No raw content**: Notification events capture metadata only, not notification content

---

## 3. Design Patterns Established

The existing schema family establishes several architectural patterns that must be followed by all new profiles.

### 3.1 Profile + Registry Pattern

- **Profiles** define type-level extensions (new sensor kinds, observation flavors, vendor-specific fields) as LinkML schemas
- **Registries** hold instance-level catalog data (which vendors exist, which device models, which observable properties with LOINC/SNOMED/MDC codes)
- Profiles describe *kinds*; registries enumerate *instances*
- Most third-party plug-ins ship a small profile (Device + Observation subclasses) plus registry rows

### 3.2 Observation Subclass Pattern

Every sensor type produces observations by subclassing the core `Observation` class:

```yaml
VendorSpecificObservation:
  is_a: Observation
  description: Vendor-specific observation with extra fields.
  attributes:
    vendor_specific_field_1:
      range: float
    vendor_specific_field_2:
      range: string
```

The base `Observation` provides: `header`, `made_by_sensor`, `device`, `deployment`, `session`, `subject`, `observed_property`, `used_procedure`, `phenomenon_time`, `result_time`, `anatomical_site`, `result`, `quality`, `interpretation`, `reference_ranges`.

### 3.3 Device Subclass Pattern

Each vendor defines a Device subclass with fixed `device_type` and `device_category`:

```yaml
VendorDevice:
  is_a: Device
  slot_usage:
    device_type:
      equals_string: consumer_wearable  # or medical_device, etc.
    device_category:
      equals_string: wrist_worn         # or ring, patch, etc.
```

### 3.4 Mixin Pattern (AWARE)

For cross-cutting concerns, use LinkML mixins:

```yaml
CrossCuttingMixin:
  mixin: true
  attributes:
    extra_field:
      range: string

ConcreteObservation:
  is_a: Observation
  mixins:
    - CrossCuttingMixin
```

### 3.5 Result Polymorphism

Results use a typed discriminator (`result_type` enum) to support heterogeneous value types through a single `Result` class:

- `scalar`: `UnitValue` (decimal + UCUM unit)
- `coded`: URI/CURIE reference
- `string`: Free text
- `boolean`: True/false
- `integer`: Whole number
- `range`: Low/high `UnitValue` pair
- `ratio`: Numerator/denominator `UnitValue` pair
- `compound`: List of `ResultComponent` (each with its own code + value)
- `waveform`: `WaveformResult` (blob reference, format, sample rate, channel count)
- `attachment`: `AttachmentResult` (URI, media type, size, hash)

### 3.6 SurveyInstrument-as-Procedure Pattern

Self-report instruments are modeled as `Procedure` subclasses (via `SurveyInstrument`), with completed responses modeled as `Observation` subclasses (via `SurveyResponse`). This aligns with SOSA semantics where a Procedure is the method used to make an Observation.

### 3.7 Standards Cross-Reference Pattern

Every class and slot uses dual-coding:

- `class_uri` points to the most specific standard (e.g., `sosa:Observation`, `fhir:Device`)
- `slot_uri` binds individual fields to standard properties (e.g., `sosa:madeBySensor`, `fhir:Device.serialNumber`)
- `property_codes` on `ObservableProperty` allows multi-coding (LOINC + SNOMED + MDC + HPO)

### 3.8 Privacy-by-Design Pattern

All contextual/behavioral sensors follow:

1. Hash identifiers before persistence (contacts, app packages, BSSIDs)
2. Store metadata only, not raw content
3. Declare `privacy_level` on sensor descriptors
4. Policy attestation objects (e.g., `VoiceAffectPolicy`) require explicit consent flags

---

## 4. Gaps and Design Proposals

### 4.1 Missing Sensor Profiles

| Gap | Priority | Current State | Proposal |
|-----|----------|---------------|----------|
| **Psychiatric Instruments** | P0 | `SurveyInstrument` exists but no concrete instrument profiles (PHQ-9, GAD-7, AUDIT, PCL-5) | Create `profile_psych_instruments.yaml` with concrete classes per instrument |
| **Clinical Labs** | P0 | `clinical.yaml` has `ClinicalFinding` but no lab-specific schema | Create `profile_clinical_labs.yaml` modeling labs as sporadic snapshot sensors |
| **Voice Biomarkers** | P0 | Yar has Pydantic models; no LinkML profile | Create `profile_voice_biomarker.yaml` bridging Yar runtime to Cytos schema |
| **Apple Watch** | P1 | No vendor profile | Create `vendor_apple_watch.yaml` mapping HealthKit data types |
| **Garmin** | P1 | No vendor profile | Create `vendor_garmin.yaml` mapping Garmin Connect data |
| **OMOP CDM** | P2 | No profile | Create `profile_omop.yaml` mapping to OMOP Observation domain |
| **Cellular Assays** | P2 | `vendor_cytoscope.yaml` exists as placeholder | Expand with single-cell RNA-seq, flow cytometry, spatial transcriptomics profiles |

### 4.2 Missing Registry Entries

The registry schema exists but the actual registry data files are not yet populated:

- No `vendors.yaml` instance file with vendor catalog entries
- No `devices.yaml` with device model entries
- No `observable_properties.yaml` with LOINC/SNOMED-coded property entries
- No `body_sites.yaml` with UBERON/SNOMED body site entries
- No `procedures.yaml` with procedure catalog entries

**Proposal**: Generate initial registry population scripts using the mcPHASES dataset as seed data.

### 4.3 Schema-to-Runtime Bridge

The Yar `SensorDescriptor` (Pydantic) and Cytos `Sensor` (LinkML) are semantically equivalent but not formally linked:

| Yar (Runtime) | Cytos (Schema) | Status |
|---------------|----------------|--------|
| `SensorDescriptor.sensor_id` | `Sensor.sensor_local_id` | Semantically equivalent |
| `SensorDescriptor.modality` | `Sensor.sensor_modality` | Different enum values |
| `ObservationField` | `Channel` + `ObservableProperty` | Structural mismatch |
| `SensorObservation` | `Observation` | Same intent, different structure |

**Proposal**: Create a `cytos_bridge.py` module that auto-generates LinkML-valid Cytos instances from Yar runtime objects, and vice versa.

### 4.4 Missing Standard Alignments

| Standard | Coverage Gap |
|----------|-------------|
| **OMOP CDM** | Observation domain mapping for clinical data warehousing |
| **CDISC ODM** | Clinical trial data collection forms |
| **openEHR** | Archetype-based health record semantics |
| **Apple HealthKit** | HealthKit data type mapping (HKQuantityType, HKCategoryType) |
| **Google Health Connect** | Android health data API mapping |

### 4.5 Validation and Testing Gaps

- LinkML validation passes (`linkml-lint`, `gen-json-schema`, `gen-pydantic`, `linkml-validate`) for existing schemas
- No automated CI pipeline for schema validation on commit
- No cross-profile consistency tests (e.g., ensuring a Fitbit observation can also validate as a FHIR Observation)
- No data-driven test suite against real mcPHASES data files

---

## 5. Proposed New Profiles

### 5.1 Psychiatric Instruments Profile (`profile_psych_instruments.yaml`)

Psychiatric screening instruments modeled as concrete `SurveyInstrument` and `SurveyResponse` subclasses. Each instrument specifies items, response options, scoring algorithm, clinical cut-offs, and ontology mappings.

#### 5.1.1 PHQ-9 (Patient Health Questionnaire-9)

```yaml
PHQ9Instrument:
  is_a: SurveyInstrument
  description: >-
    Patient Health Questionnaire-9. Nine-item depression screening tool.
    Scores 0-27. Cut-offs: 5 mild, 10 moderate, 15 moderately severe, 20 severe.
  slot_usage:
    instrument_name:
      equals_string: "PHQ-9"
    questionnaire_code:
      equals_string: "loinc:44249-1"
  attributes:
    phq9_item_1:
      range: integer
      minimum_value: 0
      maximum_value: 3
      description: "Little interest or pleasure in doing things (0=Not at all, 3=Nearly every day)"
    phq9_item_2:
      range: integer
      minimum_value: 0
      maximum_value: 3
      description: "Feeling down, depressed, or hopeless"
    phq9_item_3:
      range: integer
      minimum_value: 0
      maximum_value: 3
      description: "Trouble falling or staying asleep, or sleeping too much"
    phq9_item_4:
      range: integer
      minimum_value: 0
      maximum_value: 3
      description: "Feeling tired or having little energy"
    phq9_item_5:
      range: integer
      minimum_value: 0
      maximum_value: 3
      description: "Poor appetite or overeating"
    phq9_item_6:
      range: integer
      minimum_value: 0
      maximum_value: 3
      description: "Feeling bad about yourself"
    phq9_item_7:
      range: integer
      minimum_value: 0
      maximum_value: 3
      description: "Trouble concentrating on things"
    phq9_item_8:
      range: integer
      minimum_value: 0
      maximum_value: 3
      description: "Moving or speaking so slowly/being fidgety or restless"
    phq9_item_9:
      range: integer
      minimum_value: 0
      maximum_value: 3
      description: "Thoughts of self-harm"
    phq9_total_score:
      range: integer
      minimum_value: 0
      maximum_value: 27
    phq9_severity:
      range: PHQ9SeverityEnum

PHQ9Response:
  is_a: SurveyResponse
  description: A completed PHQ-9 response.
  attributes:
    instrument:
      range: PHQ9Instrument
    items:
      range: SurveyItemAnswer
      multivalued: true
    total_score:
      range: integer
      minimum_value: 0
      maximum_value: 27
    severity:
      range: PHQ9SeverityEnum
```

**Ontology mappings:**
- LOINC: `44249-1` (PHQ-9 total), individual items `44250-9` through `44258-2`
- SNOMED: `720433000` (PHQ-9 score)
- ICD-10: F32.x (Major depressive disorder) when score >= 10
- DSM-5: 296.xx (Major Depressive Disorder)

#### 5.1.2 GAD-7 (Generalized Anxiety Disorder-7)

```yaml
GAD7Instrument:
  is_a: SurveyInstrument
  description: >-
    Generalized Anxiety Disorder 7-item scale. Scores 0-21.
    Cut-offs: 5 mild, 10 moderate, 15 severe.
  slot_usage:
    instrument_name:
      equals_string: "GAD-7"
    questionnaire_code:
      equals_string: "loinc:69737-5"
  attributes:
    gad7_item_1:
      range: integer
      minimum_value: 0
      maximum_value: 3
      description: "Feeling nervous, anxious, or on edge"
    gad7_item_2:
      range: integer
      minimum_value: 0
      maximum_value: 3
      description: "Not being able to stop or control worrying"
    gad7_item_3:
      range: integer
      minimum_value: 0
      maximum_value: 3
      description: "Worrying too much about different things"
    gad7_item_4:
      range: integer
      minimum_value: 0
      maximum_value: 3
      description: "Trouble relaxing"
    gad7_item_5:
      range: integer
      minimum_value: 0
      maximum_value: 3
      description: "Being so restless it is hard to sit still"
    gad7_item_6:
      range: integer
      minimum_value: 0
      maximum_value: 3
      description: "Becoming easily annoyed or irritable"
    gad7_item_7:
      range: integer
      minimum_value: 0
      maximum_value: 3
      description: "Feeling afraid something awful might happen"
    gad7_total_score:
      range: integer
      minimum_value: 0
      maximum_value: 21
    gad7_severity:
      range: GAD7SeverityEnum
```

**Ontology mappings:**
- LOINC: `69737-5` (GAD-7 total)
- SNOMED: `720079009` (GAD-7 score)
- ICD-10: F41.1 (Generalized anxiety disorder)

#### 5.1.3 AUDIT (Alcohol Use Disorders Identification Test)

```yaml
AUDITInstrument:
  is_a: SurveyInstrument
  description: >-
    AUDIT 10-item alcohol screening. Scores 0-40.
    Cut-offs: 8 hazardous, 16 harmful, 20 possible dependence.
  slot_usage:
    instrument_name:
      equals_string: "AUDIT"
    questionnaire_code:
      equals_string: "loinc:72109-2"
```

**Ontology mappings:**
- LOINC: `72109-2` (AUDIT total)
- SNOMED: `713107009` (AUDIT score)
- ICD-10: F10.x (Alcohol use disorders)

#### 5.1.4 PCL-5 (PTSD Checklist for DSM-5)

```yaml
PCL5Instrument:
  is_a: SurveyInstrument
  description: >-
    PCL-5 PTSD screening. 20 items scored 0-4. Total 0-80.
    Cut-off: 31-33 provisional PTSD diagnosis.
  slot_usage:
    instrument_name:
      equals_string: "PCL-5"
```

**Ontology mappings:**
- LOINC: `77857-9` (PCL-5)
- SNOMED: `441836009` (PTSD screening score)
- ICD-10: F43.1 (Post-traumatic stress disorder)
- DSM-5: 309.81

#### 5.1.5 FHIR QuestionnaireResponse Mapping

All psychiatric instruments map to FHIR as follows:

| Cytos Concept | FHIR R5 Resource |
|--------------|------------------|
| `SurveyInstrument` | `Questionnaire` |
| `SurveyItem` | `Questionnaire.item` |
| `SurveyResponse` | `QuestionnaireResponse` |
| `SurveyItemAnswer` | `QuestionnaireResponse.item.answer` |
| Total score | `Observation` with LOINC code |
| Severity level | `Observation.interpretation` |

#### 5.1.6 Scoring Enums

```yaml
PHQ9SeverityEnum:
  permissible_values:
    none: {description: "Score 0-4"}
    mild: {description: "Score 5-9"}
    moderate: {description: "Score 10-14"}
    moderately_severe: {description: "Score 15-19"}
    severe: {description: "Score 20-27"}

GAD7SeverityEnum:
  permissible_values:
    minimal: {description: "Score 0-4"}
    mild: {description: "Score 5-9"}
    moderate: {description: "Score 10-14"}
    severe: {description: "Score 15-21"}

AUDITRiskEnum:
  permissible_values:
    low_risk: {description: "Score 0-7"}
    hazardous: {description: "Score 8-15"}
    harmful: {description: "Score 16-19"}
    possible_dependence: {description: "Score 20-40"}
```

### 5.2 Clinical Labs Profile (`profile_clinical_labs.yaml`)

Clinical laboratory results modeled as "sporadic snapshot sensors" in the universal schema.

#### 5.2.1 Design Rationale

Clinical lab results are sensors in the same way a Fitbit is a sensor, with key differences:

| Property | Wearable Sensor | Clinical Lab Sensor |
|----------|----------------|-------------------|
| Sampling frequency | Continuous (1-5 min) | Sporadic (days to months) |
| Latency | Real-time | Hours to days |
| Location | On-body | External laboratory |
| Result type | Scalar | Scalar + reference ranges + flags |
| Standards | IEEE 11073, BLE GHS | LOINC, FHIR Lab Result |
| Device | Consumer wearable | Lab analyzer instrument |

Both produce `Observation` instances with `UnitValue` results, `reference_ranges`, `interpretation` codes, and provenance metadata.

#### 5.2.2 Proposed Schema

```yaml
LabDevice:
  is_a: Device
  description: A clinical laboratory analyzer or test system.
  slot_usage:
    device_type:
      equals_string: lab_instrument
  attributes:
    clia_number:
      range: string
      description: CLIA certification number for the performing laboratory.
    lab_name:
      range: string
    lab_oid:
      range: string
      description: OID of the performing laboratory.

LabObservation:
  is_a: Observation
  description: >-
    A clinical laboratory result. Sporadic-snapshot sensor producing one
    observation per analyte per specimen per collection event.
  attributes:
    specimen_type:
      range: BiologicalSampleTypeEnum
      description: Type of specimen (blood, urine, CSF, saliva).
    specimen_collected:
      range: datetime
    specimen_received:
      range: datetime
    resulted_at:
      range: datetime
    ordering_provider:
      range: string
    lab_status:
      range: LabStatusEnum

LabPanel:
  is_a: ObservationCollection
  description: >-
    A collection of LabObservations from a single panel order
    (e.g., Basic Metabolic Panel, Comprehensive Metabolic Panel, CBC).
  attributes:
    panel_code:
      range: uriorcurie
      description: LOINC panel code.
    panel_name:
      range: string
```

#### 5.2.3 Common Lab Panels as Observable Properties

| Panel | LOINC Code | Analytes |
|-------|-----------|----------|
| **Basic Metabolic Panel (BMP)** | `51990-0` | Glucose, BUN, Creatinine, Na, K, Cl, CO2, Ca |
| **Comprehensive Metabolic Panel (CMP)** | `24323-8` | BMP + Albumin, Total Protein, ALP, ALT, AST, Bilirubin |
| **Complete Blood Count (CBC)** | `58410-2` | WBC, RBC, Hemoglobin, Hematocrit, Platelets, MCV, MCH, MCHC, RDW |
| **Lipid Panel** | `24331-1` | Total Cholesterol, LDL, HDL, Triglycerides, VLDL |
| **Thyroid Panel** | `24348-5` | TSH, Free T4, Free T3 |
| **HbA1c** | `4548-4` | Glycated hemoglobin |
| **hsCRP** | `30522-7` | High-sensitivity C-reactive protein |

### 5.3 Voice Biomarker Profile (`profile_voice_biomarker.yaml`)

Bridges the Yar runtime voice sensor to the Cytos LinkML schema.

#### 5.3.1 Proposed Schema

```yaml
VoiceBiomarkerSensor:
  is_a: Sensor
  description: >-
    A voice analysis sensor producing acoustic and affective biomarkers
    from speech audio. Modeled after the Yar SensorDescriptor for
    cytonome.voice.emotion.v0.
  slot_usage:
    sensor_modality:
      equals_string: voice_acoustic

VoiceEmotionObservation:
  is_a: Observation
  description: >-
    Per-utterance emotion and vocal biomarker observation from
    HuBERT + openSMILE eGeMAPSv02 analysis.
  attributes:
    emotion_categorical:
      range: EmotionCategoryEnum
    emotion_confidence:
      range: float
      minimum_value: 0.0
      maximum_value: 1.0
    valence:
      range: float
      minimum_value: -1.0
      maximum_value: 1.0
    arousal:
      range: float
      minimum_value: 0.0
      maximum_value: 1.0
    dominance:
      range: float
      minimum_value: 0.0
      maximum_value: 1.0
    pitch_mean_hz:
      range: float
    pitch_std_hz:
      range: float
    speech_rate_syl_sec:
      range: float
    jitter_percent:
      range: float
    shimmer_db:
      range: float
    hnr_db:
      range: float
    pause_count:
      range: integer
    pause_total_ms:
      range: float

VoiceAffectTrendObservation:
  is_a: Observation
  description: >-
    Smoothed affect trend from EMA-windowed voice observations.
    Maps to VoiceAffectSignal from Yar models.
  attributes:
    affect_state:
      range: AffectStateEnum
    affect_trend:
      range: AffectTrendEnum
    arousal_smoothed:
      range: float
    valence_smoothed:
      range: float
    confidence:
      range: float
    window_size:
      range: integer
    ema_alpha:
      range: float
```

#### 5.3.2 Emotion Enums

```yaml
EmotionCategoryEnum:
  description: Categorical emotion labels aligned with Ekman + neutral.
  permissible_values:
    anger: {}
    sadness: {}
    fear: {}
    joy: {}
    neutral: {}
    surprise: {}
    disgust: {}

AffectStateEnum:
  description: Coarse affect state from Yar VoiceAffectSignal.
  permissible_values:
    neutral: {}
    elevated: {}
    subdued: {}
    mixed: {}
    agitated: {}

AffectTrendEnum:
  permissible_values:
    stable: {}
    rising: {}
    falling: {}
    volatile: {}
```

### 5.4 Apple Watch Vendor Profile (`vendor_apple_watch.yaml`)

#### 5.4.1 Proposed Schema

```yaml
AppleWatchDevice:
  is_a: Device
  description: Apple Watch wearable device (Series 7+, SE, Ultra).
  slot_usage:
    device_type:
      equals_string: consumer_wearable
    device_category:
      equals_string: wrist_worn
  attributes:
    healthkit_source_id:
      range: string
      description: HealthKit source bundle identifier.
    watch_series:
      range: string

AppleWatchHeartRate:
  is_a: Observation
  description: Apple Watch continuous heart rate (PPG, optical).
  annotations:
    healthkit_type: HKQuantityTypeIdentifier.heartRate

AppleWatchRestingHeartRate:
  is_a: Observation
  annotations:
    healthkit_type: HKQuantityTypeIdentifier.restingHeartRate

AppleWatchHRV:
  is_a: Observation
  description: Apple Watch HRV (SDNN, measured overnight).
  annotations:
    healthkit_type: HKQuantityTypeIdentifier.heartRateVariabilitySDNN

AppleWatchSpO2:
  is_a: Observation
  description: Apple Watch blood oxygen (overnight, reflectance pulse ox).
  annotations:
    healthkit_type: HKQuantityTypeIdentifier.oxygenSaturation

AppleWatchECG:
  is_a: Observation
  description: Apple Watch single-lead ECG (30s recording).
  annotations:
    healthkit_type: HKElectrocardiogramType

AppleWatchSkinTemperature:
  is_a: Observation
  description: Apple Watch wrist skin temperature (overnight baseline deviation).
  annotations:
    healthkit_type: HKQuantityTypeIdentifier.appleSleepingWristTemperature

AppleWatchSteps:
  is_a: Observation
  annotations:
    healthkit_type: HKQuantityTypeIdentifier.stepCount

AppleWatchSleepSession:
  is_a: Observation
  description: Apple Watch sleep analysis with stages (Core, Deep, REM, Awake).
  annotations:
    healthkit_type: HKCategoryTypeIdentifier.sleepAnalysis

AppleWatchActivitySummary:
  is_a: Observation
  description: Daily activity rings (Move, Exercise, Stand).
  attributes:
    active_energy_burned_kcal:
      range: float
    exercise_minutes:
      range: integer
    stand_hours:
      range: integer

AppleWatchRespiratoryRate:
  is_a: Observation
  annotations:
    healthkit_type: HKQuantityTypeIdentifier.respiratoryRate

AppleWatchNoiseExposure:
  is_a: Observation
  description: Environmental sound level exposure (dB SPL).
  annotations:
    healthkit_type: HKQuantityTypeIdentifier.environmentalAudioExposure

AppleWatchCycleTracking:
  is_a: Observation
  description: Menstrual cycle tracking data.
  annotations:
    healthkit_type: HKCategoryTypeIdentifier.menstrualFlow
```

### 5.5 Garmin Vendor Profile (`vendor_garmin.yaml`)

#### 5.5.1 Proposed Schema

```yaml
GarminDevice:
  is_a: Device
  description: Garmin wearable device (Fenix, Venu, Forerunner, Vivosmart).
  slot_usage:
    device_type:
      equals_string: consumer_wearable
    device_category:
      equals_string: wrist_worn
  attributes:
    garmin_connect_device_id:
      range: string

GarminHeartRate:
  is_a: Observation
  description: Garmin optical heart rate (PPG).

GarminRestingHeartRate:
  is_a: Observation

GarminHRV:
  is_a: Observation
  description: Garmin HRV status (overnight RMSSD with 7-day baseline).

GarminPulseOx:
  is_a: Observation
  description: Garmin Pulse Ox (SpO2) measurement.

GarminSteps:
  is_a: Observation

GarminStress:
  is_a: Observation
  description: Garmin stress score (1-100, derived from HRV).
  attributes:
    stress_level:
      range: integer
      minimum_value: 1
      maximum_value: 100
    stress_qualifier:
      range: GarminStressQualifierEnum

GarminBodyBattery:
  is_a: Observation
  description: Garmin Body Battery energy level (1-100).

GarminSleepSession:
  is_a: Observation
  description: Garmin Advanced Sleep Monitoring with stages.

GarminRespiratoryRate:
  is_a: Observation

GarminActivitySession:
  is_a: Observation
  description: A logged activity/exercise session from Garmin Connect.

GarminVO2Max:
  is_a: Observation
  description: Garmin VO2 max estimate (running or cycling).

GarminTrainingStatus:
  is_a: Observation
  description: Training status (Productive, Peaking, Recovery, Unproductive, Detraining).

GarminStressQualifierEnum:
  permissible_values:
    rest: {}
    low: {}
    medium: {}
    high: {}
    activity: {}
```

---

## 6. PhysioNet mcPHASES Dataset Mapping

The mcPHASES dataset (Mathai et al., 2025; Nature Scientific Data, doi:10.1038/s41597-026-06805-3) is available at `/home/mohammadi/datasets/sensors/physionet` and contains 27 files from 19 data modalities spanning three vendor devices (Fitbit Sense, Dexcom G6, Mira fertility analyzer) plus daily self-report surveys and baseline demographics.

### 6.1 Dataset Summary

| Property | Value |
|----------|-------|
| **Participants** | Menstrual-cycle-tracking individuals |
| **Study intervals** | Jan-Apr 2022 (Interval 1), Jul-Oct 2024 (Interval 2) |
| **Devices** | Fitbit Sense, Dexcom G6, Mira Plus Kit |
| **Join keys** | `id` (participant), `day_in_study` (normalized day index) |
| **Total CSV files** | 19 data files + metadata files |

### 6.2 File-to-Schema Mapping

Every CSV file in the mcPHASES dataset is mapped to a Cytos Observation subclass in `profile_mcphases.yaml`:

| CSV File | Size | Cytos Class | Vendor Profile |
|----------|------|------------|----------------|
| `heart_rate.csv` | 2.0 GB | `FitbitHeartRate` | `vendor_fitbit` |
| `resting_heart_rate.csv` | 704 KB | `FitbitRestingHeartRate` | `vendor_fitbit` |
| `heart_rate_variability_details.csv` | 24.5 MB | `FitbitHRVDetails` | `vendor_fitbit` |
| `respiratory_rate_summary.csv` | 553 KB | `FitbitRespiratoryRateSummary` | `vendor_fitbit` |
| `steps.csv` | 227 MB | `FitbitSteps` | `vendor_fitbit` |
| `distance.csv` | 244 MB | `FitbitDistance` | `vendor_fitbit` |
| `altitude.csv` | 2.8 MB | `FitbitAltitude` | `vendor_fitbit` |
| `calories.csv` | 646 MB | `FitbitCalories` | `vendor_fitbit` |
| `active_minutes.csv` | 163 KB | `FitbitActivityMinutes` | `vendor_fitbit` |
| `active_zone_minutes.csv` | 5.8 MB | `FitbitActiveZoneMinutes` | `vendor_fitbit` |
| `time_in_heart_rate_zones.csv` | 214 KB | `FitbitTimeInHRZones` | `vendor_fitbit` |
| `exercise.csv` | 8.4 MB | `FitbitExerciseSession` | `vendor_fitbit` |
| `sleep.csv` | 54.7 MB | `FitbitSleepSession` | `vendor_fitbit` |
| `sleep_score.csv` | 333 KB | `FitbitSleepScore` | `vendor_fitbit` |
| `stress_score.csv` | 533 KB | `FitbitStressScore` | `vendor_fitbit` |
| `demographic_vo2_max.csv` | 817 KB | `FitbitVO2Max` | `vendor_fitbit` |
| `computed_temperature.csv` | 757 KB | `FitbitNightlySkinTemperature` | `vendor_fitbit` |
| `wrist_temperature.csv` | 317 MB | `FitbitWristTemperatureSample` | `vendor_fitbit` |
| `estimated_oxygen_variation.csv` | 96.8 MB | `FitbitEstimatedOxygenVariation` | `vendor_fitbit` |
| `glucose.csv` | 24.7 MB | `DexcomGlucoseObservation` | `vendor_dexcom` |
| `hormones_and_selfreport.csv` | 696 KB | `McPhasesHormonesAndSelfreport` | `vendor_mira` + selfreport |
| `subject-info.csv` | 3.5 KB | `McPhasesSubject` | core |
| `height_and_weight.csv` | 586 B | `McPhasesHeightWeight` | core |

### 6.3 mcPHASES-Specific Classes

The `profile_mcphases.yaml` (567 lines) defines additional classes specific to the dataset:

- **`McPhasesSubject`**: Subject with `day_in_study`, `study_interval`, `is_weekend`
- **`McPhasesHeightWeight`**: Height and weight baseline
- **`McPhasesCycleAnnotation`**: Researcher-annotated menstrual cycle phase
- **`McPhasesHormonesAndSelfreport`**: Compound observation combining Mira hormones (LH, E3G, PDG) with 12 daily self-report Likert items (cramps, fatigue, sleep issues, mood swings, stress, food cravings, indigestion, bloating, etc.)
- **`McPhasesCyclePhaseEnum`**: `menstrual`, `follicular`, `ovulation`, `luteal`, `late_luteal`, `not_classified`
- **`McPhasesFlowVolumeEnum`**: Self-reported menstrual flow volume Likert
- **`McPhasesFlowColorEnum`**: Self-reported flow color

### 6.4 Validation Status

The mcPHASES profile validates cleanly:

```bash
linkml-lint core/core.yaml                                   # error-clean
gen-json-schema profiles/profile_mcphases.yaml > /tmp/x.json # ~17k lines, clean
gen-pydantic profiles/profile_mcphases.yaml > /tmp/x.py      # 143 classes
linkml-validate -s profiles/profile_mcphases.yaml \
   -C SensorDataset examples/mcphases_example.yaml           # No issues found
```

---

## 7. Sensor as MCP/Plugin System

### 7.1 Architecture Overview

The sensor plugin system follows the Yar `SensorDescriptor` + `Sensor` Protocol pattern, extended with MCP (Model Context Protocol) integration for AI agent interoperability.

```
┌──────────────────────────────────────────────────┐
│                   Cytonome App                    │
│                                                   │
│  ┌─────────────┐  ┌─────────────┐  ┌───────────┐│
│  │  Settings >  │  │  Dashboard  │  │  Agents   ││
│  │   Sensors    │  │  360° View  │  │ Supervisor││
│  └──────┬───────┘  └──────┬──────┘  └─────┬─────┘│
│         │                 │               │       │
│  ┌──────▼─────────────────▼───────────────▼─────┐│
│  │           Sensor Event Bus                    ││
│  └──────┬────────┬────────┬────────┬────────┬───┘│
│         │        │        │        │        │     │
│  ┌──────▼──┐ ┌───▼────┐ ┌▼──────┐ ┌▼──────┐ ┌▼─┐│
│  │  Voice  │ │ Fitbit │ │Dexcom │ │ PHQ-9 │ │...││
│  │ Emotion │ │ Sense  │ │  G7   │ │ Survey│ │   ││
│  │ Sensor  │ │ Plugin │ │Plugin │ │Plugin │ │   ││
│  └─────────┘ └────────┘ └───────┘ └───────┘ └───┘│
└──────────────────────────────────────────────────┘
```

### 7.2 Plugin Interface

Each sensor plugin implements:

1. **`SensorDescriptor`**: Self-describing registration (identity, modality, privacy level, capabilities, output fields, hardware requirements)
2. **`Sensor` Protocol**: Lifecycle methods (`initialize`, `start`, `observe`, `stream`, `stop`, `teardown`)
3. **LinkML Profile**: Schema definition for its Observation subclasses
4. **Registry Entries**: Vendor, device, observable property, and procedure catalog entries

### 7.3 Plugin Discovery and Installation

```
~/.cytonome/plugins/
├── cytonome-voice-emotion/
│   ├── plugin.yaml          # SensorDescriptor
│   ├── sensor.py            # Sensor implementation
│   ├── schema/
│   │   └── profile.yaml     # LinkML profile
│   └── registries/
│       ├── properties.yaml  # ObservableProperty entries
│       └── procedures.yaml  # Procedure entries
├── fitbit-connect/
│   ├── plugin.yaml
│   ├── sensor.py
│   ├── schema/
│   │   └── vendor_fitbit.yaml
│   └── registries/
│       └── devices.yaml
└── dexcom-connect/
    └── ...
```

### 7.4 User Control Flow

1. User opens Settings > Sensors
2. Available plugins are listed as cards with: name, modality icon, privacy level badge, description, required permissions
3. User taps "Connect" on a plugin
4. Plugin calls `initialize()` (loads models, connects to APIs, validates dependencies)
5. Plugin requests any required permissions (microphone, Bluetooth, HealthKit)
6. Plugin starts producing `SensorObservation` instances on the event bus
7. Dashboard aggregates all active sensors into a 360° health view
8. User can disconnect any sensor at any time via the toggle

### 7.5 MCP Integration

Sensor plugins expose an MCP tool interface so AI agents can query sensor data:

```json
{
  "name": "sensor_query",
  "description": "Query observations from a connected sensor",
  "parameters": {
    "sensor_id": "string",
    "time_range": {"start": "datetime", "end": "datetime"},
    "property": "string",
    "aggregation": "mean|median|min|max|last"
  }
}
```

---

## 8. Reference Standards Alignment

### 8.1 Standards Coverage Matrix

| Standard | LinkML Asset | Coverage Level |
|----------|-------------|----------------|
| **W3C SOSA/SSN** (2017, ext-2023) | `profile_sosa.yaml` + all core classes | Full: Sensor, Observation, FeatureOfInterest, ObservableProperty, Procedure, Platform, Sample, Result, ObservationCollection, Deployment, System, SystemCapability. Class/slot URI alignment for lossless RDF round-trip. |
| **IEEE 1752.1 / Open mHealth** | `profile_ieee1752.yaml` + `core/core.yaml` | Full: Header, data-point envelope, data-series envelope, all major body schemas (heart-rate, BP, body-temp, BMI, BG, SpO2, RR, steps, physical-activity, sleep, calories, geoposition, ambient, pain, mood). |
| **HL7 FHIR R5** | `profile_fhir.yaml` | Full: Observation, Device, DeviceMetric, DeviceUsage, Patient, Vital Signs profile family, Extension carrier. |
| **Bluetooth GHS / IEEE 11073-10206** | `profile_bt_ghs.yaml` | Full: All 9 observation classes, measurement-status, MDC code bindings, ETS clock, raw-MET round-trip. |
| **AWARE Framework** | `profile_aware.yaml` + `core/context.yaml` | Full: All 25 smartphone sensors + ESM. Privacy-preserving hashing. |
| **physiodsp** | `WaveformResult`, `Stream`, `Channel`, `ProcessingPipeline` | Partial: (timestamps, values, fs) pattern captured. |
| **Hermes** | `Session`, `Stream`, `DelayEstimate`, `ProcessingPipeline` | Partial: Multi-device session, delay estimates, stream provenance. |
| **OMOP CDM** | Not yet implemented | Gap: Observation domain mapping needed for clinical data warehousing. |
| **Apple HealthKit** | Not yet implemented | Gap: HKQuantityType/HKCategoryType mapping proposed in Section 5.4. |
| **CDISC ODM** | Not yet implemented | Gap: Clinical trial data collection forms. |

### 8.2 Prefix Namespace Registry

The sensor schema uses the following URI prefixes for standards alignment:

| Prefix | URI | Standard |
|--------|-----|----------|
| `sosa:` | `http://www.w3.org/ns/sosa/` | W3C SOSA |
| `ssn:` | `http://www.w3.org/ns/ssn/` | W3C SSN |
| `ssn_system:` | `http://www.w3.org/ns/ssn/systems/` | SSN System Capabilities |
| `fhir:` | `http://hl7.org/fhir/` | HL7 FHIR R5 |
| `loinc:` | `http://loinc.org/` | LOINC |
| `sct:` | `http://snomed.info/sct/` | SNOMED CT |
| `ucum:` | `http://unitsofmeasure.org/` | UCUM |
| `mdc:` | `urn:iso:std:iso:11073:10101:` | IEEE 11073 MDC |
| `omh:` | `https://w3id.org/openmhealth/schemas/` | Open mHealth |
| `prov:` | `http://www.w3.org/ns/prov#` | W3C PROV |
| `qudt:` | `http://qudt.org/schema/qudt/` | QUDT |
| `UBERON:` | `http://purl.obolibrary.org/obo/UBERON_` | Uber-anatomy |
| `CHEBI:` | `http://purl.obolibrary.org/obo/CHEBI_` | ChEBI |
| `OBI:` | `http://purl.obolibrary.org/obo/OBI_` | Ontology for Biomedical Investigations |
| `HP:` | `http://purl.obolibrary.org/obo/HP_` | Human Phenotype Ontology |
| `DUO:` | `http://purl.obolibrary.org/obo/DUO_` | Data Use Ontology |

---

## Appendix A: Cytos-to-Yar Bridge Mapping

| Cytos (LinkML) | Yar (Pydantic Runtime) | Notes |
|----------------|----------------------|-------|
| `Sensor` | `SensorDescriptor` | Cytos is schema-level; Yar is runtime registration |
| `Sensor.sensor_modality` | `SensorDescriptor.modality` | Different enum granularity |
| `Channel` + `ObservableProperty` | `ObservationField` | Cytos separates channel from property; Yar merges them |
| `Observation` | `SensorObservation` | Cytos has full SOSA semantics; Yar has flat dict |
| `Deployment` | Implicit in `SensorRegistry.connect()` | Yar has no explicit deployment model |
| `Session` | `session_id` string | Cytos tracks multi-device co-recording; Yar tracks per-sensor |
| `ObservationQuality` | `confidence` float | Cytos has structured quality flags; Yar has scalar confidence |
| `VoiceAffectSignal` | ← new in Yar | No direct Cytos equivalent; proposed in `profile_voice_biomarker.yaml` |
| `VoiceAffectContextHint` | ← new in Yar | Response-style layer input; maps to a derived `Observation` |

## Appendix B: Implementation Roadmap

| Phase | Deliverables | Timeline |
|-------|-------------|----------|
| **Phase 0** (Complete) | Core schema, SOSA/IEEE/FHIR/GHS/AWARE profiles, Fitbit/Dexcom/Mira/Oura/Cytoscope vendors, mcPHASES profile + example | Done |
| **Phase 1a** | Psychiatric instruments profile (PHQ-9, GAD-7, AUDIT, PCL-5) | 2 weeks |
| **Phase 1b** | Clinical labs profile (BMP, CMP, CBC, Lipid, Thyroid, HbA1c) | 2 weeks |
| **Phase 1c** | Voice biomarker profile (HuBERT + openSMILE, affect trend) | 1 week |
| **Phase 1d** | Apple Watch + Garmin vendor profiles | 1 week |
| **Phase 2a** | Registry population (vendors, devices, properties, body sites, procedures) | 2 weeks |
| **Phase 2b** | Cytos-to-Yar bridge module | 1 week |
| **Phase 2c** | CI/CD validation pipeline + cross-profile consistency tests | 1 week |
| **Phase 3** | OMOP CDM profile, HealthKit/Google Health Connect mapping | 4 weeks |
| **Phase 4** | Cellular assay profiles (scRNA-seq, flow cytometry, spatial transcriptomics) | 8 weeks |
