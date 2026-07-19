---
spec_id: SPEC-CSP
version: "0.1"
status: draft
domain: universal-sensor-CSP
owner: Shahin Mohammadi
created: 2026-06-21
last_updated: 2026-06-22
depends_on:
  - Cytoplex/spec/03_primitives.md
  - Cytoplex/spec/privacy-boundary-spec.md
  - Yar/spec/SPEC-storage-engine.md
  - Yar/spec/SPEC-sync-protocol.md
implements:
  - CAP-Lite (Yar default profile)
  - CrossBoundarySignal schema v0
aliases:
  - USAP (Universal Sensor Adapter Protocol) -- deprecated alias; do not use in new writing
  - UBAP (Universal Biosensor Adapter Protocol) -- deprecated alias; do not use in new writing
---

# SPEC-CSP: Cytonome Sensor Protocol

> **Reading options:** An ADHD-friendly progressive-disclosure rendering is generated from this file. The hand-maintained ADHD twin (`spec/adhd/SPEC-CSP_adhd.md`) was retired 2026-07-16; see `_archive/cleanup_2026-07-16/adhd-twins/`.

> **Status**: Draft
> **Date**: 2026-06-22
> **Author**: Cytognosis Foundation
> **Audience**: engineers
> **Tags**: `yar`, `cytonome`, `csp`, `sensor-protocol`, `biocypher`, `sosa`, `consent`
> **Related**: `Cytoplex/spec/03_primitives.md`, `Cytoplex/spec/privacy-boundary-spec.md`, `Yar/spec/SPEC-storage-engine.md`, `Yar/spec/SPEC-sync-protocol.md`, `04-Engineering/cytos/sensing-schema/unified-sensor-report.md`

> **Implementation status**: The `SensorDescriptor` schema, lifecycle phases, and CSP governance model are **design only** (no SensorDescriptor class exists in any repo at time of writing). The voice-affect sensor stack (`Yar/src/yar/models/voice_affect.py`, `Yar/src/yar/core/affect/tracker.py`, `Yar/apps/mobile/lib/src/affect/`) is **implemented** and is the closest working artifact to a CSP-compliant adapter. The Cytos KG hook (`cytos:measured_by` predicate, `device` node type) is **implemented** in `cytos/src/cytos/kg/biocypher/schema_config.yaml`. All other adapter classes are **planned or research-tier**; see Section 6 maturity labels.

---

**Reading time**: ~12 minutes.
**If you only read one thing**: Section 3 (adapter lifecycle) and Section 5 (data schema). CSP is the boundary contract every sensor must satisfy before its output can touch Yar's data layer or cross the privacy boundary.

**BLUF**: CSP (Cytonome Sensor Protocol) is the open, CAP-governed protocol that lets any sensor or signal source plug into Yar. Every adapter must declare a `SensorDescriptor`, pass through the five-phase lifecycle, produce observations that conform to the LinkML/SOSA schema, and reference a consent grant before any data is stored or transmitted. Raw signals stay on-device. Only derived, structured outputs may cross the privacy boundary. User-defined axes become first-class citizens via the extensible axis registry.

---

## 1. Purpose and Scope

CSP defines the contract that any sensor or signal source must satisfy to integrate with Yar. It is an open protocol: any developer, researcher, or third party may implement a CSP-compatible adapter using only this document and the referenced schema files.

**Design goals:**

- **User sovereignty.** No sensor is mandatory. The user connects and disconnects adapters at will. All data stays on-device unless the user explicitly enables a cross-boundary feature.
- **CAP governance.** Every adapter is authorized by CAP. The privacy boundary classifies every observation before it can leave the device. Consent references are required.
- **Semantic interoperability.** Sensor outputs use a shared LinkML/SOSA schema, so observations from an Oura Ring, a voice pipeline, and a user-defined custom axis are all query-compatible at the data layer.
- **Extensibility.** Users and developers may define new tracking axes (F55). Once registered, a custom axis is indistinguishable from a built-in one.

**In scope:** adapter model, lifecycle phases, sensor data schema, CAP governance integration, privacy-boundary interaction, built-in adapter classes, user-extensible axes, and the relationship to per-sensor modality specs.

**Out of scope:** transport security, model inference internals, the clinician alert experience (see `MODULE-crisis-detection.md`), CRDT sync mechanics (see `SPEC-sync-protocol.md`), and the graph query engine (see `SPEC-storage-engine.md`).

**Canonical name:** this protocol is **CSP (Cytonome Sensor Protocol; formerly USAP/UBAP)**. These aliases were used in engineering docs predating this spec. New writing, code comments, and references must use CSP.

---

## 2. Protocol Position in the System Stack

CSP sits at the input boundary of Yar's eight-layer data fabric (from `SPEC-sync-protocol.md`). It feeds the CRDT op-log at L2 and the consent layer at L6.

```
External signals
      |
  [CSP Layer]  <--- THIS SPEC
      |
  CAP PEP (privacy boundary check + consent validation)
      |
  CRDT op-log (L2) -- source of truth per SPEC-storage-engine.md
      |
  Graph index (L4) -- derived, swappable
```

Every observation produced by a CSP adapter becomes a CRDT operation on the op-log. Adapters do not write directly to the graph engine.

---

## 3. Adapter Model and Lifecycle

A CSP adapter is a self-contained module that wraps a single signal source (a hardware sensor, an API, a local model inference pipeline, or a self-report form). It declares its capabilities at registration time and produces typed observations during operation.

### 3.1 SensorDescriptor

Every adapter must register a `SensorDescriptor` before any data flows. This is the identity and capability declaration.

```yaml
# LinkML sketch (field names normative)
classes:
  SensorDescriptor:
    attributes:
      adapter_id:        { range: string, required: true }    # reverse-DNS, e.g. org.cytognosis.yar.oura
      display_name:      { range: string, required: true }    # user-visible label
      adapter_class:     { range: AdapterClassEnum, required: true }
      maturity:          { range: MaturityEnum, required: true }  # stable | beta | research | future
      modalities:        { range: ModalityEnum, multivalued: true }
      axes_produced:     { range: AxisRef, multivalued: true }    # axes this adapter populates
      privacy_tier:      { range: PrivacyTierEnum, required: true }  # on_device_only | boundary_derived | clinician_gated
      requires_consent:  { range: ConsentScopeEnum, multivalued: true }
      schema_ref:        { range: uri, required: true }    # points to the adapter's observation schema
      implementation_ref: { range: uri }                   # optional; source or package reference
```

The `SensorRegistry` holds all registered descriptors. An adapter that is not registered cannot produce observations that the data layer will accept.

### 3.2 Lifecycle Phases

Every CSP adapter passes through exactly five phases. Implementations must expose the corresponding method signatures.

| Phase | Method | Description |
|---|---|---|
| **Discover** | `discover() -> SensorDescriptor` | Adapter announces itself to the registry; returns its descriptor. No data flows yet. Hardware adapters check device availability here. |
| **Connect** | `connect(consent_ref: str) -> ConnectionStatus` | Adapter establishes a link to its signal source and records the consent grant. Connection fails if `consent_ref` is not active or is mismatched to this adapter's required scopes. |
| **Configure** | `configure(config: AdapterConfig) -> ConfigStatus` | Adapter applies user and system configuration: axis mapping, sampling rate, privacy-tier overrides, and Yar integration settings. Configuration may be re-applied at runtime without a full disconnect. |
| **Read or Stream** | `observe() -> Observation` or `stream() -> AsyncIterator[Observation]` | Adapter emits typed observations conforming to the CSP schema. Point-in-time sensors use `observe`; continuous sensors use `stream`. Observations reference the active consent grant at the field level. |
| **Disconnect** | `disconnect() -> None` | Adapter severs its signal source connection, flushes any pending observations, and releases hardware resources. Pending observations that have not been written to the op-log are dropped, not queued. |

State machine:

```
[unregistered]
     |  discover()
  [registered]
     |  connect(consent_ref)
  [connected]
     |  configure(config)
  [configured]
     |  observe() / stream()
  [active]
     |  disconnect()
  [registered]  (returns to registered, not unregistered)
```

If `consent_ref` is withdrawn while the adapter is `active`, the adapter must transition to `connected` and stop emitting observations within one session, consistent with `privacy-boundary-spec.md` PB-8.

---

## 4. Sensor Data Schema

All CSP observations use the Cytos LinkML schema system (`04-Engineering/cytos/sensing-schema/`). The schema is SOSA-aligned: a `Sensor` makes an `Observation` of a `FeatureOfInterest` via a `Procedure`, producing a `Result`.

### 4.1 Core Observation Type

```yaml
# LinkML sketch (normative field names; full schema in cytos/schemas/domains/sensor/core/core.yaml)
classes:
  CSPObservation:
    is_a: sosa:Observation
    attributes:
      observation_id:   { range: string, required: true, identifier: true }
      adapter_id:       { range: string, required: true }    # references SensorDescriptor.adapter_id
      axis_ref:         { range: AxisRef, required: true }   # which tracked axis this populates
      timestamp:        { range: datetime, required: true }  # UTC, millisecond precision
      result:           { range: CSPResult, required: true }
      provenance:       { range: CSPProvenance, required: true }
      consent_ref:      { range: string, required: true }    # active consent grant ID
      privacy_tier:     { range: PrivacyTierEnum, required: true }  # inherited from SensorDescriptor
      unit:             { range: string }                    # UCUM code preferred
      quality_flags:    { range: QualityFlagEnum, multivalued: true }

  CSPResult:
    attributes:
      scalar:        { range: float }
      coded_value:   { range: string }     # SNOMED CT, LOINC, or controlled vocabulary code
      waveform_ref:  { range: string }     # reference to blob in encrypted store (L3)
      text_summary:  { range: string }     # derived, non-PHI summary; never raw transcript

  CSPProvenance:
    attributes:
      source_device:    { range: string }    # hardware or software source identifier
      model_version:    { range: string }    # inference model version if applicable
      collection_method: { range: string }   # passive | active | inferred
      raw_data_location: { range: string }   # on-device path; never transmitted
```

**Key rules:**

- `CSPResult.text_summary` is a derived, non-PHI field. It must never contain raw transcripts, verbatim user input, or identifiable content. Enforce at the PEP per `privacy-boundary-spec.md` Section 3.2.
- `CSPResult.waveform_ref` references an encrypted on-device blob. The blob itself is `privacy_tier: on_device_only` and never crosses the boundary.
- `consent_ref` is required at the observation level, not just at connect time. This enables per-observation consent granularity for adapters that handle multiple consent scopes.

### 4.2 Axis Reference

An `AxisRef` links an observation to a named tracking axis. Axes are registered separately (see Section 6). Both built-in axes and user-defined axes use the same `AxisRef` type.

```yaml
classes:
  AxisRef:
    attributes:
      axis_id:         { range: string, required: true, identifier: true }  # e.g. yar.mood.valence
      axis_label:      { range: string, required: true }   # user-visible
      domain:          { range: AxisDomainEnum, required: true }  # see Section 6
      value_type:      { range: ValueTypeEnum, required: true }   # continuous | ordinal | categorical | event
      range_min:       { range: float }
      range_max:       { range: float }
      unit:            { range: string }
      biolink_class:   { range: string }    # optional Biolink Model alignment
```

Biolink Model alignment: where an axis maps to a biological or clinical entity class, the `biolink_class` field records the alignment (for example, `biolink:PhenotypicFeature` for a behavioral phenotype axis). This is optional but strongly recommended for axes that feed research or grant reporting pipelines.

### 4.3 SOSA and SSN Alignment

CSP extends the W3C SOSA/SSN ontology rather than reinventing observation semantics. The full alignment is in `profile_sosa.yaml` inside the Cytos schema tree. Key namespace prefixes in use:

| Prefix | Namespace |
|---|---|
| `sosa:` | `http://www.w3.org/ns/sosa/` |
| `ssn:` | `http://www.w3.org/ns/ssn/` |
| `ucum:` | `http://unitsofmeasure.org/` |
| `loinc:` | `http://loinc.org/` |
| `DUO:` | `http://purl.obolibrary.org/obo/DUO_` (data use ontology, consent) |
| `cytos:` | Cytognosis internal predicate namespace (see Section 4.4) |

### 4.4 Cytos KG Hook: `cytos:measured_by` and `device` Node Type

The Cytos BioCypher KG schema (`cytos/src/cytos/kg/biocypher/schema_config.yaml`) defines an **implemented** edge type that links sensor-produced datasets to the device that collected them:

```yaml
# From cytos/src/cytos/kg/biocypher/schema_config.yaml (implemented)
measured by:
  is_a: association
  represented_as: edge
  label_in_input: cytos:measured_by
  source: dataset
  target: device
  properties:
    provided_by: str
```

This `cytos:measured_by` predicate is the upstream KG semantic anchor for CSP observations. When a CSP adapter produces an observation that flows into the Cytos KG pipeline, the `CSPObservation.provenance.source_device` field maps to the `device` node, and the resulting dataset record carries the `cytos:measured_by` edge to that device.

CSP adapter implementers who intend their output to participate in the Cytos KG pipeline must ensure:

1. `CSPProvenance.source_device` contains a stable, resolvable device identifier that the Cytos ingest pipeline can resolve to a `device` node.
2. The observation schema uses `cytos:measured_by` to express the sensor-to-dataset link, consistent with the BioCypher alignment at `cytos/src/cytos/kg/biocypher/schema_config.yaml`.
3. SOSA/SSN source configs are declared in `cytos/configs/sources/sosa_ssn.yaml` and `cytos/configs/sources/nwb_core.yaml`; use these as registered schema sources rather than defining independent sensing schemas.

---

## 5. Governance: CAP, Privacy Boundary, and Consent

Every CSP adapter is governed by CAP (Control Authority Protocol, `Cytoplex/spec/`). The relevant CAP profile for Yar's default operation is CAP-Lite.

### 5.1 CAP Authorization

Adapters are not self-authorizing. Before an adapter's observations can enter the CRDT op-log, the CAP Guard must have issued an `allow` or `allow_with_constraints` decision for that adapter's scope. The authorization flow:

1. Adapter calls `connect(consent_ref)`.
2. The CSP layer issues a `Directive` to the CAP PEP requesting authorization for this adapter's declared scopes.
3. The CAP Guard evaluates against the active policy and the user's consent grant.
4. If the decision is `allow` or `allow_with_constraints`, the adapter transitions to `connected`. If `deny`, the connection fails and the adapter cannot emit observations.
5. The `GuardDecision` is stored in the local hash-chain audit log (CAP Layer 5 from `cap-yar-comprehensive-reference.md`).

The CAP primitive types used are `Directive`, `GuardDecision`, and `DecisionRecord` (see `03_primitives.md` for full definitions).

### 5.2 Privacy Boundary Classification

Every adapter declares a `privacy_tier` in its `SensorDescriptor`. The three tiers map directly to the `privacy-boundary-spec.md` data classification:

| Privacy tier | Data class | What may cross the boundary |
|---|---|---|
| `on_device_only` | Section 3.2 (device-local) | Nothing. Raw audio, transcripts, raw feature vectors, free text, PHI. |
| `boundary_derived` | Section 3.1 (crossing allowed under consent) | Derived, structured signals only: scalar levels, coded values, opaque hashes, enums. Never raw content. |
| `clinician_gated` | Section 3.1, restricted scope | Same as `boundary_derived`, but only when a clinician integration is active and consented. Requires BAA pathway. |

The CAP PEP enforces these classifications at observation emit time, consistent with `privacy-boundary-spec.md` requirements PB-1 through PB-10. Any observation that violates its declared tier is dropped, a policy violation is raised, and a non-PHI validation error is logged (PB-3).

### 5.3 Consent Model

CSP uses a reference-based consent model. Consent grants are managed outside CSP (by the consent layer at L6 of the data fabric), and adapters reference them by ID.

Rules:

- **Default-deny.** An adapter without an active `consent_ref` cannot emit observations (PB-4).
- **Scope specificity.** Each adapter type has a declared required consent scope. The `consent_ref` must cover the adapter's scopes. An Oura adapter with a sleep-data consent grant cannot emit activity-data observations under that grant.
- **Revocation.** When consent is withdrawn, the adapter stops emitting within one session (PB-8). Pending observations in the queue are dropped.
- **Audit.** Every consent check generates a `DecisionRecord` in the local audit log.

### 5.4 VoiceAffectPolicy as the Reference Consent-Attestation Model

The most complete privacy-attestation model currently implemented in the codebase is `VoiceAffectPolicy` in `Yar/src/yar/models/voice_affect.py`. CSP signal descriptor authors should align their consent-attestation fields to this model.

`VoiceAffectPolicy` (implemented, Apache-2.0):

| Field | Type | Default | Meaning |
|---|---|---|---|
| `raw_audio_stored` | bool | `False` | Attestation that raw audio is never persisted |
| `diagnostic_use_allowed` | bool | `False` | Whether data may be used for diagnostic inference |
| `user_facing_emotion_label_allowed` | bool | `False` | Whether a labelled emotion state may be shown to the user |
| `on_device_only` | bool | `True` | Whether all processing stays on-device |
| `retention_policy` | str | `"ephemeral"` | Retention class; default is ephemeral (TTL-based, not persisted) |

The backend rejects any `VoiceAffectEvent` where `raw_audio_stored`, `diagnostic_use_allowed`, or `user_facing_emotion_label_allowed` is `True`. This hard-reject pattern is the normative model for CSP adapters: the privacy policy is not advisory; it gates ingestion.

New CSP signal descriptor schemas should include equivalent attestation fields. Where a field does not apply to a non-voice adapter, it may be omitted, but the `on_device_only` and `retention_policy` fields are required for all adapter classes with `privacy_tier: on_device_only`.

The Dart mirror of this model is at `Yar/apps/mobile/lib/src/affect/voice_affect_models.dart`, confirming the policy travels with the event from the mobile sidecar to the backend.

---

## 6. Adapter Classes and Maturity

Adapter classes group sensors by signal type and governance requirements. Each class has a canonical maturity label.

Maturity labels:
- **Stable**: schema finalized, at least one reference implementation shipped.
- **Beta**: schema finalized, reference implementation in progress.
- **Research**: schema draft, inference pipeline under development.
- **Future**: schema planned, no implementation yet.

### 6.1 Subjective Self-Report (Stable)

Point-in-time user-initiated check-ins for mood, energy, focus, and other user-defined states.

**Signal type:** user-entered scalar or categorical value.
**Privacy tier:** `boundary_derived` (only aggregated trajectory, never raw text).
**Axes produced:** mood valence, mood arousal, energy level, focus, custom user axes.
**Key features:** F53 (mood-anchored morning check-in).

These adapters are the simplest CSP implementation: no hardware, no inference model, just a typed form that produces a `CSPObservation` with a coded or scalar `CSPResult`.

### 6.2 Validated Self-Report Instruments (Beta)

Structured administration of validated clinical and research instruments as first-class CSP adapters. Referenced as F62 (opt-in self-assessment tools).

**Signal type:** scored questionnaire response.
**Privacy tier:** `clinician_gated` for instruments with direct diagnostic utility; `boundary_derived` for symptom-severity summaries.
**Named instruments:** ASRS v1.1 (ADHD symptoms), PHQ-9 (depression severity), GAD-7 (anxiety severity), BRIEF-A (executive function), BIS-11 (impulsivity).
**Schema refs:** `cytos/schemas/domains/sensor/core/selfreport.yaml` (`SurveyInstrument`, `SurveyResponse`); FHIR `Questionnaire` and `QuestionnaireResponse` for interoperability.
**Axes produced:** symptom-severity axes per instrument; each maps to a named Yar tracking axis.
**Implementation note:** The per-instrument CAP Directive must specify the instrument name and scoring version. Raw item responses are `on_device_only`. Only total and subscale scores may cross the boundary under `boundary_derived`.

### 6.3 Physiological Wearables (Beta)

Consumer wearable devices accessed via vendor API or Bluetooth. Referenced as F30 (wearable sensor connection).

**Signal type:** physiological time-series and daily summaries.
**Privacy tier:** `boundary_derived` for daily summaries; `on_device_only` for raw PPG/accelerometer waveforms.
**Reference implementations:** Oura Ring (vendor_oura.yaml, 8 Observation subclasses), Fitbit (vendor_fitbit.yaml, 19 Observation subclasses), Apple Watch (HealthKit, schema proposed but not yet implemented).
**Axes produced:** sleep efficiency, HRV, resting heart rate, activity level, step count.
**Consent scope:** per-vendor scope per data type (sleep, activity, temperature, SpO2 are separate scopes).
**Implementation note:** Full implementation guides are in `04-Engineering/yar/sensors/implementing-wearables.md`. That document is an input to the forthcoming `SPEC-sensor-physiological.md`, which will bind these adapters to CSP formally.

### 6.4 Speech and Voice Signals (Research)

Paralinguistic and acoustic features extracted from the user's voice during Yar sessions. Referenced as F40 (voice wellbeing signals) and F54 (voice mood awareness).

**Signal type:** derived acoustic features; never raw audio or transcripts.
**Privacy tier:** `on_device_only` for raw audio and transcripts; `boundary_derived` for derived scalar features.
**Axes produced:** vocal affect index, energy-in-voice, speech rate, pause pattern index.
**Inference stack:** HuBERT and openSMILE are the reference extraction models (from `04-Engineering/cytos/sensing-schema/unified-sensor-report.md` Section 4). Model output is a `VocalBiomarkerFrame` (schema defined in `04-Engineering/yar/research/voice_model_deep_evaluation.md`).
**Key schema types:** `VocalBiomarkerFrame`, `SessionVocalProfile`, `ADHDVocalMarkers`, `ASDVocalMarkers`.
**Maturity caveat:** F40 is Research-tier. The inference pipeline is not shipped. The schema is the gate before implementation may begin. See architecture gap G3 in `yar-unified-feature-comparison-v4.md`.
**Implementation note:** This adapter class will be formally specified in the forthcoming `SPEC-sensor-speech-mentalstate.md`.

### 6.5 Social-Interaction Signals (Research)

Passive sensing of interaction patterns: call duration, proximity events, and social rhythm metrics. Derived from smartphone sensors without capturing message content.

**Signal type:** temporal interaction event counts and durations; no content.
**Privacy tier:** `boundary_derived` for summary statistics; `on_device_only` for any interaction content.
**Axes produced:** social rhythm regularity, interaction frequency, isolation index.
**Reference source:** AWARE Framework (profile_aware.yaml, 25 smartphone sensor classes including privacy-preserving hashed contacts).
**Maturity:** Research. No implementation yet.
**Implementation note:** This adapter class will be formally specified in the forthcoming `SPEC-sensor-social-interaction.md`.

### 6.6 Future Biosensor Adapter (Future)

A forward-looking class for high-fidelity neurophysiological sensors that provide connectomic or brain-state signals. Referenced as F46 (brain sensor connection layer).

**Signal type:** neural, optical, or electrical signals from wearable or implantable biosensors.
**Target devices:** Cytoscope (Cytognosis proprietary), fNIRS headbands, consumer EEG devices.
**Privacy tier:** `on_device_only` for raw signals; `clinician_gated` for derived biomarkers.
**Axes produced:** attention state, cognitive load index, neural circuit state (axes TBD in `SPEC-neurobehavioral-axes.md`).
**Schema refs:** `vendor_cytoscope.yaml` (draft) in the Cytos vendor schema directory.
**Maturity:** Future. The Cytoscope hardware is not shipped. Schema design follows the same SOSA foundation as other adapter classes.
**Implementation note:** This class bridges CSP with the Cytoscope hardware track. Implementation is blocked on Cytoscope hardware availability.

---

## 7. User-Extensible Axes (F55)

CSP treats user-defined tracking axes as first-class citizens. A user or developer may define a new axis, register it in the axis registry, and any adapter that declares it in `axes_produced` can populate it. The axis then appears in the Yar dashboard, query engine, and cross-adapter aggregations alongside all built-in axes.

### 7.1 Axis Registration

```yaml
# LinkML sketch -- UserDefinedAxis is a subclass of AxisRef
classes:
  UserDefinedAxis:
    is_a: AxisRef
    attributes:
      created_by:    { range: string, required: true }     # "user" | "developer" | adapter_id
      created_at:    { range: datetime, required: true }
      description:   { range: string }
      example_values: { range: string, multivalued: true }
      linked_adapter_ids: { range: string, multivalued: true }  # adapters authorized to write this axis
```

### 7.2 Registration Flow

1. User or developer constructs a `UserDefinedAxis` record with a unique `axis_id`, a display label, a domain, and a value type.
2. The axis is submitted to the CSP axis registry via `register_axis(axis: UserDefinedAxis, consent_ref: str)`. CAP issues a `Directive` for the registration action; the Guard checks that the user has an active consent grant for "axis management."
3. On `allow`, the axis is stored as a CRDT operation in the op-log. It becomes immediately queryable.
4. Any adapter whose `SensorDescriptor` lists the new `axis_id` in `axes_produced` will have its observations automatically routed to that axis.

### 7.3 Governance Rules for Custom Axes

- Custom axes are `on_device_only` by default. A user must explicitly upgrade the privacy tier to `boundary_derived` if they want the axis to participate in cross-boundary features.
- Custom axis IDs must use a user-namespaced prefix (for example, `user.<display_name_slug>`) to prevent collision with built-in axes.
- Built-in axes (namespaced `yar.*`) are read-only and cannot be overridden.
- A custom axis may reference a `biolink_class` for research alignment. This is optional but supported.

### 7.4 Example: Custom Energy Crash Axis

A user who wants to track post-meal energy crashes can define:

```yaml
axis_id: user.post_meal_energy_crash
axis_label: "Post-meal energy drop"
domain: energy_regulation
value_type: ordinal
range_min: 0
range_max: 4
unit: null
biolink_class: biolink:PhenotypicFeature
```

This axis is then available to any adapter the user authorizes to populate it, including a self-report adapter, an Oura HRV adapter, or a future continuous-glucose adapter.

---

## 8. Relationship to Per-Sensor Modality Specs

This spec defines the protocol skeleton. Concrete sensor bindings live in per-modality specs that import CSP and specify the adapter implementation in full. Each modality spec follows the same structural template as CSP but narrows to a specific signal class.

| Modality spec | Adapter classes covered | Status | Dependencies |
|---|---|---|---|
| `SPEC-sensor-physiological.md` | Physiological wearables (6.3), Validated self-report instruments (6.2) | Planned (Batch 2a) | This spec (CSP) |
| `SPEC-sensor-speech-mentalstate.md` | Speech and voice signals (6.4) | Planned (Batch 2b) | This spec (CSP) |
| `SPEC-sensor-menstrual.md` | Menstrual cycle tracking (new class) | Planned (Batch 3a) | This spec (CSP) |
| `SPEC-sensor-social-interaction.md` | Social-interaction signals (6.5) | Planned (Batch 3b) | This spec (CSP), SPEC-sensor-physiological.md (AWARE primitives) |

Modality specs must:
- Declare `depends_on: [SPEC-CSP]` in their YAML frontmatter.
- Implement `SensorDescriptor` fully for each named device or pipeline.
- Specify the concrete `axes_produced` set and their `AxisRef` definitions.
- Declare `CrossBoundarySignal` classification per `privacy-boundary-spec.md` for every axis that may leave the device.
- Reference the CRDT op-log mutation pattern per `SPEC-storage-engine.md`.

---

## 9. Affirming Language Policy

Any user-facing content produced by a CSP adapter, including axis labels, observation summaries, and notification payloads, must comply with the affirming language policy defined in `SPEC_CONSOLIDATION_PLAN.md` Section 4f.

Rules:

- Do not use diagnostic labels as user-visible axis identifiers. Axes are named for the experience, not the diagnosis (for example, "attention fluctuation" rather than "ADHD symptom score").
- Do not use "normal" versus "abnormal" for sensor readings. Use specific descriptors: "elevated distress signal," "lower-than-usual sleep efficiency."
- Severity labels use the controlled vocabulary: `low`, `moderate`, `elevated`, `high`. Never "abnormal," "pathological," or diagnosis-adjacent terms.
- Observation quality flags (for example, `insufficient_data`, `sensor_offline`) are non-judgmental technical labels, never personal assessments.

---

## 10. Decided vs Open

### Decided

| Component | Decision |
|---|---|
| Canonical protocol name | CSP (Cytonome Sensor Protocol); see Section 1 for alias history |
| Schema foundation | LinkML with SOSA/SSN alignment; Cytos schema tree is the canonical source |
| Privacy boundary enforcement | CAP PEP validates every observation before op-log write; raw signals stay on-device |
| Consent model | Reference-based; consent_ref required at observation level; default-deny |
| Data layer integration | All observations are CRDT operations on the op-log (not direct graph writes) |
| Adapter lifecycle | Five phases: discover, connect, configure, read/stream, disconnect; state machine is normative |
| Axis extensibility | User-defined axes are first-class; same AxisRef type as built-ins |
| Custom axis namespace | `user.*` prefix for user-defined axes; `yar.*` is reserved and read-only |
| Privacy tiers | Three tiers: on_device_only, boundary_derived, clinician_gated |
| CAP primitives used | Directive, GuardDecision, DecisionRecord (per `03_primitives.md`) |
| Affirming language policy | No diagnostic labels as user-visible identifiers; no "normal/abnormal" |
| SOSA/SSN as observation grammar | Decided (per SPEC-sync-protocol.md Decided table) |

### Open

| # | Decision | Current leaning | Blocker |
|---|---|---|---|
| O-1 | PAP implementation for runtime-updatable adapter policies | Defer to v1 unless modality specs expose a need | Shared with `privacy-boundary-spec.md` O-3; resolve in one place |
| O-2 | Apple HealthKit adapter schema | Implement once HealthKit FHIR export API is confirmed stable | Schema is designed (profile gap noted in unified-sensor-report.md); no engineering work yet |
| O-3 | OMOP CDM profile for clinical data warehousing | Add alongside the clinician-path scope | Needed before any HIPAA pathway with clinical analytics; depends on legal posture decision |
| O-4 | Consent scope vocabulary (controlled list of scope names) | Draft a controlled vocabulary per adapter class during modality spec writing | No canonical list yet; each adapter currently uses ad-hoc scope names |
| O-5 | Encrypted blob store for waveform_ref at L3 | iroh-blobs (Loro+Iroh path) or any-sync-filenode (any-sync path) | Follows SPEC-sync-protocol.md O-1 and O-4; cannot finalize waveform storage until sync protocol is chosen |
| O-6 | VocalBiomarkerFrame schema finalization | Adopt schema from voice_model_deep_evaluation.md; validate against CSPObservation | Blocks F40 implementation; assigned to SPEC-sensor-speech-mentalstate.md |
| O-7 | Cytoscope vendor schema maturity | Promote vendor_cytoscope.yaml from draft to stable when hardware ships | Hardware availability; no engineering action possible before that |
| O-8 | Cross-adapter axis aggregation semantics | Define how observations from multiple adapters targeting the same axis are merged (last-write, weighted average, CRDT counter, or federated score) | Depends on neurobehavioral axes spec; assign to SPEC-neurobehavioral-axes.md |

---

## 11. Cross-References

| Document | Relationship |
|---|---|
| `Cytoplex/spec/03_primitives.md` | CAP primitive types used in adapter authorization (Directive, GuardDecision, DecisionRecord) |
| `Cytoplex/spec/privacy-boundary-spec.md` | Privacy tier classification and CrossBoundarySignal schema; PB-1 through PB-10 apply to all CSP adapters |
| `Yar/spec/SPEC-storage-engine.md` | L4 graph engine; CSP observations enter the system as CRDT op-log entries consumed by L4 |
| `Yar/spec/SPEC-sync-protocol.md` | L2 CRDT op-log replication; L6 consent layer; SOSA/SSN decided in sync spec's Decided table |
| `04-Engineering/cytos/sensing-schema/unified-sensor-report.md` | Authoritative Cytos LinkML schema reference; vendor profiles; standards alignment tables |
| `04-Engineering/yar/sensors/README.md` | Legacy sensor documentation index; references CSP as the current canonical spec |
| `04-Engineering/yar/sensors/implementing-wearables.md` | Oura and Fitbit implementation detail; input to SPEC-sensor-physiological.md |
| `04-Engineering/yar/sensors/implementing-aware.md` | AWARE passive sensing adapter; input to SPEC-sensor-physiological.md and SPEC-sensor-social-interaction.md |
| `04-Engineering/yar/sensors/implementing-health-instruments.md` | Clinical questionnaire adapters; input to SPEC-sensor-physiological.md |
| `04-Engineering/yar/research/voice_model_deep_evaluation.md` | VocalBiomarkerFrame schema; G3 architecture gap; input to SPEC-sensor-speech-mentalstate.md |
| `Yar/research/yar-unified-feature-comparison-v4.md` | Feature IDs F12, F30, F40, F46, F54, F55, F62 and their priority tiers |
| `MODULE-crisis-detection.md` | Crisis-detection module; operates on CSP-derived observations; governed by same CAP primitives |
| `SPEC-neurobehavioral-axes.md` (planned) | Will define how CSP axis outputs combine into longitudinal neurobehavioral axis scores |
