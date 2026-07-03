> **Status**: Input pack for Opus spec drafting session
> **Date**: 2026-06-21
> **Author**: Sonnet ingestion subagent (read-only research pass)
> **Audience**: Opus parent agent writing two safety specs
> **Purpose**: Compiled source material for (1) Privacy-Boundary Schema spec and (2) Crisis-Detection Subsystem spec

---

# SPEC INPUT PACK: Privacy Boundary Schema + Crisis Detection Subsystem

Reading time: ~12 minutes. If you only read one section: read Section 1 (privacy schema) and Section 3 (crisis detection) before writing anything.

---

## 0. Document Map

| Section | Content |
|---------|---------|
| 1 | Privacy-boundary schema: verbatim field definitions, what exists, what is missing |
| 2 | CAP enforcement model: PEP/PDP/PAP/PIP, CAP-Lite, how a schema plugs in |
| 3 | Crisis detection: all current architecture, signals, escalation, build status |
| 4 | Cytomark and annotation context: F50 WADM, F59 capture-anywhere, memex |
| 5 | Template section structures (four templates, pick the right one) |
| 6 | Naming and safety constraints to honor |
| 7 | Policy decisions the parent must flag, not decide |

---

## 1. Privacy-Boundary Schema

### 1.1 What Exists (Verbatim)

Source: `docs/03-Products/Cytonome/Yar/cytonome-master-reference.md` Section 4.2.

The heading in that document reads: **"4.2 Privacy Boundary Schema (Must-Draft)"**

The exact two-column table reproduced verbatim:

| Crosses to supervisor | Never crosses |
|---|---|
| `stress_signal(level, timestamp)` | Raw audio |
| `topic_shift(from, to, timestamp)` | Transcripts |
| `user_disengaged(timestamp, severity)` | Raw feature vectors |
| `session_phase`, `mood_arc` | Free-text from user |
| Structured guidance hints | Audio fragments |
| Supervisor interrupt signals | PHI identifiers |

Framing sentence from the source (verbatim): "Everything above the boundary stays on-device. The schema defines exactly what crosses."

This is the entirety of the formal schema content in that document. No field types, retention TTLs, provenance fields, or serialization format are specified. No separate artifact file exists.

### 1.2 Data Classes Referenced Elsewhere in the Codebase

From `cap-protocol-assessment.md` and the feature master, these named data types exist but are unspecified as of 2026-06-21:

| Type Name | Where Referenced | Status |
|-----------|-----------------|--------|
| `VocalBiomarkerFrame` | cytonome-master-reference.md gap #14 | Named only; no schema |
| `GuardDecision` | `Yar/src/cap/models.py` (Pydantic) | Implemented |
| `GuardDecisionValue` | same | Implemented |
| `CaptureProtocol` | `cap/protocols.py` structural type | Implemented (structural type, not a data frame) |
| `WriteOperationProtocol` | same | Implemented |
| `WritePlanProtocol` | same | Implemented |
| `VoiceIntent` | Routes and ARCHITECTURE.md | Referenced; schema not found in docs |

The six "Crosses to supervisor" fields in the verbatim table above are signal envelopes, not typed schemas. No serialization spec (JSON, protobuf, LinkML) has been found for them.

### 1.3 Retention and Boundary Rules (Assembled from Multiple Sources)

These rules are stated in prose across several documents, not in a single schema artifact:

- Raw audio: never leaves device, never crosses the privacy boundary, even to local supervisor.
- Transcripts: never cross the boundary; on-device episodic memory only.
- Free-text from user: never crosses the boundary.
- PHI identifiers: never cross; PII/PHI redaction engine exists in Cytoplex (`runtime/redaction.py`, `Scaffold` status).
- Derived signals (stress level, topic shift, mood arc): may cross with explicit session token.
- External writes to Anytype or any external store: require explicit user confirmation before any write; plan-before-confirm pattern is enforced by CAP-Lite.
- Consent granularity: per data type, per purpose, per recipient (patient-safety-architecture.md consent architecture section).
- Consent revocation: revocation propagates to derived-data deletion (Tier 3 substrate).
- Data retention: `retention.py` module exists in Cytoplex runtime, scaffold status; configurable TTL and deletion checks.
- Post-quantum: by M48, all persistent storage uses NIST PQC (CRYSTALS-Kyber / Dilithium / SHA-3).

### 1.4 Four-Tier Compute Boundary Summary

From `patient-safety-architecture.md`:

| Tier | Description | What leaves this tier |
|------|-------------|----------------------|
| T1 Perception (phone) | On-device LLM, S2S voice, crisis detection, episodic memory | Only opt-in derived signals, not raw audio or transcripts |
| T2 Local compute (personal node) | Long-term semantic memory, causal recommendation, sensor aggregation | Encrypted, anonymized embeddings only, with granular consent |
| T3 Distributed substrate (community) | Decentralized shards, federated learning | Aggregated, DP-bounded, post-quantum encrypted gradient updates |
| T4 Cytognosis central | Foundation training cluster | Model updates pushed back open to T1 and T2 |

The boundary between T1 and T2 is exactly what the privacy-boundary schema must govern for Yar's phone-to-supervisor signal channel.

### 1.5 What Is Missing (Critical Gaps)

These items are confirmed absent in all scanned docs:

1. Formal field type definitions for the six crossing signals (no JSON Schema, no LinkML, no protobuf).
2. Retention TTL values for any signal type.
3. Serialization format specification (envelope structure, version field, timestamp format, session token binding).
4. A schema registry entry or artifact file at any path in the repo.
5. Audit log schema for boundary-crossing events.
6. `VocalBiomarkerFrame` schema (named in gaps list, priority HIGH).
7. Any spec for `VoiceIntent` payload structure.

---

## 2. CAP Enforcement Model

### 2.1 Four-Point Architecture (PEP / PDP / PAP / PIP)

CAP's architecture is a Policy Enforcement Point / Policy Decision Point pattern. The canonical source is `cytoplex-tech.md` and `cytoplex-readme.md`.

**PEP (Policy Enforcement Point):** Intercepts every model call or agent action before execution. Three implementations exist:
- `local_pep.py`: full on-device enforcement (Production status).
- `edge_pep.py`: lightweight for constrained environments (Production).
- `attested_local_pep.py`: hardware-attested (Scaffold).
- `mobile_local_pep.py`: on-device for constrained resources (Scaffold).

**PDP (Policy Decision Point):** Evaluates policy and returns a decision for the PEP to execute.
- `privacy_pdp.py`: privacy-specific evaluation (Production).
- `pdp_adapters.py`: pluggable PDP backends (Production).

**PAP (Policy Administration Point):** Not named as "PAP" in the Cytoplex codebase. The closest equivalent is the `PolicyEngine` in `hardening/policy_engine.py` (Production-hardening status) plus the policy-as-data JSON files in `policies/` (`cap_core_policy.json`, `cap_med_policy.json`). The LinkML schemas in `schemas/` are the authoring layer for policy rules.

**PIP (Policy Information Point):** Not named as "PIP" in the Cytoplex codebase. Authority and capability metadata lives in `runtime/registry.py` (the Authority Registry). The `warrants.py` module manages Biscuit-v2 authorization tokens.

### 2.2 CAP-Lite (What It Enforces in Yar)

Source: `cap-protocol-assessment.md` Section 3.2.

`CapLiteGuard` (class in `Yar/src/cap/guard.py`, 757 lines, 29.7 KB) implements six boundary categories in priority order:

1. **Crisis detection** (highest priority, immediate deny) - see Section 3 below.
2. **Diagnosis boundary**: 22 terms in English and Farsi. Action: deny with forbidden action `diagnosis`.
3. **Treatment boundary**: medication changes, prescription, therapeutic interventions. Action: deny.
4. **Diagnostic claim boundary**: asserting facts about user mental state. Action: deny.
5. **Intent and risk boundary**: statements of intent to harm, risk disclosures. Action: deny.
6. **Raw-data sharing boundary**: blocks any attempt to share raw user data externally without plan-confirm. Action: deny or downgrade to `allow_with_constraints`.

The five public methods:
- `evaluate(capture, candidate_objects, target_external_write)`: capture-level safety evaluation, checks all six boundaries in priority order (crisis first), returns `GuardDecision` with full audit trail.
- `validate_external_write(operation_or_plan)`: validates Anytype write operations.
- `validate_local_object_update(values)`: checks local object mutations for boundary-violating content.
- `validate_local_link(...)`: link creation validation.
- (A fifth method exists for edge cases; not detailed in available docs.)

`GuardDecision` returns one of: `allow`, `allow_with_constraints`, `deny`.

### 2.3 How a Schema or Subsystem Plugs Into CAP

From the `cap-protocol-assessment.md` integration pattern (Section 4.4, verbatim):

> "Every Yar operation follows a consistent pattern:
> 1. Instantiate `CapLiteGuard()` (lightweight, no state)
> 2. Call the appropriate `evaluate()` or `validate_*()` method
> 3. Check `guard_decision` for `allow`, `allow_with_constraints`, or `deny`
> 4. If denied: return the `refusal_message` to the user, log the `decision_record`
> 5. If allowed: apply `constraints` and proceed, include `execution_report` in audit"

A new subsystem (such as a crisis-detection module or a privacy-boundary enforcer) plugs into CAP either:
- As a guard rule inside `CapLiteGuard` (highest priority rules, checked first), which is the current pattern for crisis detection.
- As a standalone PEP that wraps all signal egress (appropriate for the privacy-boundary schema as a boundary gate at the T1-to-T2 channel).

The six Yar source files that already instantiate `CapLiteGuard` are: `routes_communication.py`, `routes_anytype.py`, `routes_cap.py`, `routes_objects.py`, `routes_voice.py`, `core/coordinator.py`, `core/interactive_assistant.py`, `core/voice_service.py`.

A new privacy-boundary enforcer should hook into the egress path in `routes_voice.py` and `core/voice_service.py` since those are the signal sources that currently cross (or could cross) the boundary.

---

## 3. Crisis Detection

### 3.1 What Is Architecture-Designed (Not Built)

From the Technology Readiness Matrix in `cytonome-master-reference.md` (verbatim row):

| Component | Research | Prototype | MVP | Production | Notes |
|---|---|---|---|---|---|
| Crisis detection | CHECKMARK | NOT DONE | NOT DONE | NOT DONE | **Architecture designed** |

Status as of 2026-06-21: design only. No prototype, no MVP, no production.

### 3.2 Current Implementation in CAP-Lite

A partial implementation exists inside `CapLiteGuard.evaluate()` as the highest-priority boundary check. From `cap-protocol-assessment.md` (verbatim):

**Crisis Detection (highest priority, immediate deny)**
- **Terms**: 22 crisis terms in English and Farsi ("end my life", "kill myself", "suicidal", "خودکشی", "می‌خوام بمیرم", etc.)
- **Action**: Immediate deny with `refer_to_human_support` directive
- **Response**: Provides crisis hotline numbers (Iran: 1480, International: findahelpline.com)
- **Constraint**: `no_object_write`, `refer_to_human_support`

This is term-matching only, embedded in the guard rule layer. It is not a standalone module; it is not architecture-separate from the general policy gate.

### 3.3 Intended Architecture (from patient-safety-architecture.md)

From `patient-safety-architecture.md` Section "Crisis-detection module" (verbatim):

> "The crisis-detection module is the only mode in which the navigator is allowed to override user-controlled flows. It is hard-coded, ships before any participant exposure, and is reviewed by clinical advisors on every release."

Behavior on crisis detection (verbatim from that document):

- "Surface 988 Suicide and Crisis Lifeline and Crisis Text Line in-app, in plain language, with one-tap call or message."
- "If the user has opted in to clinician alerting, send a structured alert to the clinician with the minimum information needed for response."
- "Log the detection event in the user's memory with a clear, non-stigmatizing description."
- "Continue conversation in a supportive, non-clinical mode that does not pretend to be a therapist."

Threshold policy (verbatim): "The detection threshold is intentionally biased toward over-detection: a false alarm is acceptable; a missed crisis is not. Clinical advisors set and review the threshold."

From `app-design.md`: the coach "routes any crisis indication immediately to the crisis-detection module."

From the Tier 1 architecture description in `patient-safety-architecture.md`: "the hard-coded crisis-detection module that surfaces 988 Suicide and Crisis Lifeline plus Crisis Text Line on detection, with optional clinician alerting" is listed as a Tier 1 phone-resident component alongside the on-device LLM.

### 3.4 Planned Spec Documentation Structure

From `cap-protocol-assessment.md` Section 3 (the planned guard-rules directory structure), a `crisis-detection.md` file is listed under `guard-rules/` as a planned spec document. That file does not yet exist.

### 3.5 Gap Summary (Four Bullets)

- The crisis-detection module is architecture-designed only; no prototype or MVP exists; only a 22-term keyword match embedded inside `CapLiteGuard` stands between the user and unguarded crisis content.
- The intended architecture requires a standalone hard-coded module (separate from the general policy gate) that overrides user-controlled flows and is reviewed by clinical advisors on every release, but neither the module nor the review process exist.
- Escalation behavior is defined in prose (988/Crisis Text Line surfacing, optional clinician alert, non-stigmatizing log, supportive non-clinical continuation) but no signal taxonomy, escalation tiers, or multi-signal fusion architecture exists.
- The detection threshold policy commits to over-detection bias and clinical advisor review, but no threshold values, no sensitivity/specificity targets, and no test dataset or evaluation protocol are specified anywhere in the scanned docs.

---

## 4. Cytomark and Annotation Context

### 4.1 Cytomark Identity

- **Product name**: Cytomark. Browser extension product name for Yar. Chrome/Firefox MV3. Not started.
- **Priority**: HIGH gap (gap #8 in cytonome-master-reference.md).
- **Rationale** (verbatim from `yar-product-implementation.md`): "The browser extension may be the most important interface. People spend enormous time in browsers. Contextual capture where cognition already happens is more valuable than a separate app switch."
- **Feature ID**: F59 "Capture-anywhere" (covers phone, desktop, Chrome extension, on-page annotation).

### 4.2 F50: WADM Annotation Model

- **Feature ID**: F50, listed as "Built (MVP)" in the feature table.
- **Standard**: W3C Web Annotation Data Model.
- **Current capability** (from `ARCHITECTURE.md`): "Transforms webpage highlight payloads into W3C Web Annotation Data Model-compatible Annotation and Webpage objects, then stores them through the same coordinator path."
- **Current limitation** (from `LIMITATIONS.md` verbatim): "Current support covers webpage-style text selections. PDF anchoring, DOM ranges, Hypothesis import, and Memex import are roadmap items."
- **Implementation reference**: `WADM Annotation Adapter` in the Yar backend, exposed as a route via `ARCHITECTURE.md`.
- **Fields used** (from `VIDEO_STORYBOARD.md`): "body, target, selector, motivation, and tags."
- **Memex reference**: Memex import is explicitly listed as a roadmap item alongside Hypothesis import. No further detail in scanned docs.

### 4.3 F59: Capture-Anywhere

- **Feature ID**: F59, "Capture-anywhere." Planned, no prototype.
- **Competitor reference**: Saner AI extension (score: 6/10).
- **Cluster**: CU-5 in the consolidated inventory ("Capture-anywhere: phone, desktop, Chrome extension, on-page annotation").
- **Relation to Cytomark**: F59 is the functional requirement; Cytomark is the product expression of it in the browser.

### 4.4 Hypothesis Extension and Memex

No standalone spec for Hypothesis or Memex integration exists in the scanned docs. Both are listed as WADM limitation/roadmap items. The hypothesis-extension mention in the prompt likely refers to the Hypothesis web annotation service (hypothes.is), not a biological hypothesis. The relevant integration path is the WADM Annotation Adapter, which would need an import adapter for Hypothesis/Memex annotation formats.

---

## 5. Template Section Structures

All four templates are in `/home/mohammadi/repos/cytognosis/cytoskills/skills/cytognosis/cytognosis-doc/references/`.

### 5.1 module-spec-template.md

**Best for**: a single module with a public API. Sections (in order):

1. Header (Package, Status, Date, Owner, LoC, Test Coverage)
2. Purpose (one paragraph: what problem, why it exists)
3. Architecture (Mermaid diagram: inputs, outputs, dependencies, side effects; Dependencies table)
4. Public API (per-function: signature, parameter table, Returns, Raises, Example; per-class: field table)
5. Configuration (env vars, config keys, secrets)
6. Error Handling (error | cause | resolution table)
7. Performance (latency, throughput, scaling)
8. Known Limitations (numbered list)
9. Changelog (date | change | author table)
10. Related Documents (ADR, RFC, related specs)

Quality checklist: every public function documented; all env vars listed; errors have causes and resolutions; at least one Mermaid diagram; Purpose is specific; Dependencies list is complete.

### 5.2 platform-design-template.md

**Best for**: platform-level architecture documents covering the full scope of a product or system. Sections (in order):

1. Vision and Context (Problem Statement, Mission, Key Differentiators table, Success Metrics table)
2. Current State Audit (Existing Systems table, Technical Debt table)
3. Architecture (System Context C4 diagram, Component Architecture diagram, Data Flow, API Surface table)
4. Compute Architecture (Tier table)
5. Storage Architecture (Store | Technology | Data Type | Retention table)
6. Data Lifecycle (Stage | Tools | SLA table)
7. Tool Stack (Category | Tool | Version | Purpose table)
8. Security Architecture (Layer | Controls table)
9. Observability (Signal | Tool | Retention table)
10. Roadmap (Phase | Timeline | Deliverables table)
11. Decision Log (number | Decision | Date | Rationale table)
12. References (ADRs, Related docs, External specs)

### 5.3 requirements-template.md (EARS notation)

**Best for**: formal requirements documents with EARS (Easy Approach to Requirements Syntax) notation. Sections (in order):

1. Feature Overview (2-3 sentences: feature, problem, scope boundary)
2. User Stories (US-NNN: As a role, I want to action, so that benefit)
3. Requirements (EARS patterns: WHEN / WHILE / WHERE / IF-THEN THE SYSTEM SHALL; each REQ has Acceptance Criteria, Priority, Linked Design)
4. Non-Functional Requirements (ID | Category | Requirement | Target table)
5. Unchanged Behavior (CAUTION block: what must not change)
6. Traceability Matrix (Requirement | Design Section | Task/Issue | Test Case)

EARS syntax patterns (verbatim from template):
- `WHEN [trigger event or condition], THE SYSTEM SHALL [observable system response]`
- `WHILE [state], THE SYSTEM SHALL [behavior]`
- `WHERE [condition], THE SYSTEM SHALL [action]`
- `IF [condition], THEN THE SYSTEM SHALL [response]`

### 5.4 sensor-spec-template.md (measurement spec)

**Best for**: sensors, instruments, assays, or any measurement system. Follows SOSA/SSN ontology patterns. Sections (in order):

1. Identity (Name, SOSA class, short description, domain, target measurand, measurement context)
2. Observable Properties (Property | SOSA/QUDT Term | Unit UCUM | Range | Resolution table)
3. Protocol (Preparation, Measurement Protocol, Quality Control table)
4. Hardware/Platform (Component | Specification table: Instrument, Manufacturer, Model, Software version, Consumables, Calibration)
5. Data Contract (Output Format field table, File Format, Metadata Requirements table)
6. Interoperability (Ontology Mapping, Integration Points)
7. Performance Characteristics (Sensitivity, Specificity, Detection limit, Quantification limit, Dynamic range, Throughput, Turnaround time, Cost per sample)
8. Regulatory/Compliance
9. References (Publications, Protocols, Related specifications)

---

## 6. Naming and Safety Constraints to Honor

These are standing rules from memory and the canonical docs. The spec author must honor all of them.

| Rule | Constraint |
|------|-----------|
| CSP is canonical | The sensor protocol is "CSP" (Cytonome Sensor Protocol). "USAP" is the engineering alias. Do not introduce a third name. |
| Never "Substrate" | Retired term. Use "layer", "foundation", or "protocol" instead. The codebase still has `substrate_interop.py`; flag for rename but do not use the term in new docs. |
| No diagnosis or treatment claims | CAP-Lite enforces this. Specs must not imply or enable diagnostic or treatment output from Yar. Persona schema `non_diagnostic: true` and `no_treatment_recommendations: true`. |
| Augmentation not replacement | Yar augments cognitive function; it is not a therapy replacement and must not be framed as one. Crisis detection routes to human support, not to Yar handling the crisis. |
| No raw data sharing | Raw audio, transcripts, raw feature vectors, and free-text never cross the privacy boundary. This is a hard constraint, not a preference. |
| Explicit write confirmation | Every external write requires explicit user confirmation (plan-before-confirm pattern). CAP-Lite enforces. |
| Controller-Authority Protocol | Full name of CAP. Not "Cytonome Assurance Protocol" (stale) and not "Control Authority Protocol" (cytoplex-readme.md uses this; cytonome-track.md uses "Controller-Authority" as canonical; use the canonical form). |
| Identity safe | Yar must never become a masking engine. Persona schema `identity_safe: true`. This applies to crisis detection: the module must not tell a user their crisis reaction is "wrong" or mask it. |
| Over-detection bias | Crisis detection threshold is explicitly biased toward false positives. Any spec that sets sensitivity/specificity targets must respect this stated policy. |
| Clinical advisor review gate | Crisis detection module must be reviewed by clinical advisors on every release. This is a stated release gate, not a preference. |

---

## 7. Policy Decisions the Parent Must Flag (Not Decide)

These require a human decision or clinical/legal input. The parent Opus agent should raise these as explicit flags in the spec, not silently resolve them.

1. **Crisis signal taxonomy**: Which signals (beyond the current 22 keyword terms) should trigger crisis detection? Linguistic signals only, or also paralinguistic (vocal biomarker thresholds)? This requires clinical advisor input and should not be resolved by the spec author alone.

2. **Clinician alerting opt-in mechanics**: The patient-safety-architecture says "if the user has opted in to clinician alerting." No consent flow, UI flow, or data minimization spec for that alerting exists. HIPAA implications if any PHI crosses to a clinician channel. Flag for Duane Valz (counsel) and a benefits/compliance specialist.

3. **Crisis hotline localization**: Current CAP-Lite hardcodes Iran (1480) and findahelpline.com. The patient-safety-architecture says 988 and Crisis Text Line (US-focused). These two source documents differ. Which set of hotlines is canonical for the Yar launch market? This requires a product decision.

4. **Retention TTL for crisis detection events**: The patient-safety-architecture says "Log the detection event in the user's memory with a clear, non-stigmatizing description." How long does that log persist? Is it user-deletable? Is there a minimum retention floor for safety audit purposes? This intersects with HIPAA and state mental health privacy laws. Flag for counsel.

5. **Threshold values for over-detection policy**: "Clinical advisors set and review the threshold" is stated, but no clinical advisors are yet formally attached to Yar (the IRB is with North Star, not Cytognosis directly). Who sets the initial threshold before clinical advisors are contracted? Flag for Shahin.

6. **Privacy-boundary schema formal format**: Should the schema be LinkML (matching the rest of CAP schemas), JSON Schema only, or protobuf? The choice affects how it integrates with the Cytoplex schema registry and the gRPC/HTTP bindings. This is an engineering decision that has downstream compatibility implications.

7. **PAP (Policy Administration Point) gap**: The Cytoplex architecture does not name or implement a PAP. If the privacy-boundary spec requires a PAP (a layer that allows policy rules to be updated without redeployment), this is a new architectural component, not a small addition. Flag for a design decision before specifying it.

---

## 8. Source Files Read for This Pack

| File | Status |
|------|--------|
| `docs/03-Products/Cytonome/Yar/cytonome-master-reference.md` | Read OK |
| `docs/03-Products/Cytonome/Yar/consolidation_2026-06-21/_ingestion/A_canonical_product.md` | Read OK |
| `docs/03-Products/Cytonome/Cytoplex/cytoplex-readme.md` | Read OK |
| `docs/03-Products/Cytonome/Cytoplex/steering/cytoplex-tech.md` | Read OK |
| `docs/03-Products/Cytonome/Cytoplex/steering/cytoplex-product.md` | Read OK |
| `docs/03-Products/Cytonome/Cytoplex/steering/cytoplex-structure.md` | Read OK |
| `docs/03-Products/Cytonome/patient-safety-architecture.md` | Read OK |
| `docs/04-Engineering/cytoplex/research/cap-protocol-assessment.md` | Searched (not fully read; crisis and guard rule sections extracted) |
| `docs/03-Products/Cytonome/navigation-recommendations.md` | Searched (crisis escalation row extracted) |
| `docs/03-Products/Cytonome/app-design.md` | Searched (crisis routing line extracted) |
| `docs/02-Funding/foresight/foresight-cytonome-2026-submit.md` | Searched (crisis detection milestone extracted) |
| `docs/03-Products/Cytonome/Yar/consolidation_2026-06-21/_synthesis/CONSOLIDATED_INVENTORY.md` | Read (F50, F59, CU-5 rows extracted) |
| `cytoskills/skills/cytognosis/cytognosis-doc/references/module-spec-template.md` | Read OK |
| `cytoskills/skills/cytognosis/cytognosis-doc/references/platform-design-template.md` | Read OK |
| `cytoskills/skills/cytognosis/cytognosis-doc/references/requirements-template.md` | Read OK |
| `cytoskills/skills/cytognosis/cytognosis-doc/references/sensor-spec-template.md` | Read OK |

### Missing files (paths given in the task that did not resolve to readable content)

None of the six primary source files were missing. All resolved and were read. The `cap-protocol-assessment.md` file exists at `docs/04-Engineering/cytoplex/research/cap-protocol-assessment.md` (not under `docs/03-Products`); it was found by search, not given in the task path list.
