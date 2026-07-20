---
title: "CAP Protocol Assessment"
date: "2026-05-25"
source: "migrated from org/plans"
category: "product"
status: "current"
tags:
  - cytognosis
  - product
---

# CAP Protocol Assessment

> **Date**: 2026-05-24
> **Author**: Cytognosis Research Agent
> **Status**: Comprehensive analysis of CAP (Control Authority Protocol) implementation, integration, gaps, and rebuild considerations
> **Scope**: CAP standalone repo, Yar integration, previous designs, cytocast rebuild path

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Current Implementation Assessment](#2-current-implementation-assessment)
3. [Yar CAP-Lite Implementation](#3-yar-cap-lite-implementation)
4. [Yar Integration Points](#4-yar-integration-points)
5. [Previous Designs and Evolution](#5-previous-designs-and-evolution)
6. [Schema and Policy Architecture](#6-schema-and-policy-architecture)
7. [Test Coverage Analysis](#7-test-coverage-analysis)
8. [Gaps and Issues](#8-gaps-and-issues)
9. [Docs Reorganization Plan](#9-docs-reorganization-plan)
10. [Cytocast Rebuild Consideration](#10-cytocast-rebuild-consideration)
11. [Migration Roadmap](#11-migration-roadmap)
12. [Appendix: Complete File Inventory](#appendix-complete-file-inventory)

---

## 1. Executive Summary

CAP (Control Authority Protocol) exists in two distinct codebases with fundamentally different architectures:

| Codebase | Package | Version | Purpose |
|---|---|---|---|
| `CAP/` | `cap-protocol` | v0.1.0 | Standalone v1 architecture research package with runtime scaffolds |
| `Yar/src/cap/` | `cap` (embedded) | v0.1 | Production-grade deterministic policy gate for Yar |

The standalone CAP repo (`cap-protocol`) is a massive research artifact: 29 runtime modules, 52 test files, 25 documentation files, 12 JSON schemas (v1), 9 JSON schemas (v0.1), 7 LinkML domain schemas, and multiple transport bindings (gRPC, HTTP/JSON, Go interop). It targets a v1 "Control Authority Protocol" architecture but currently implements a v0.1 production-candidate subset.

The Yar-embedded `cap` package is the production workhorse: 7 focused modules (guard, primitives, models, protocols, policies, constants, plus `__init__`) totaling under 50KB of source. It is a deterministic, zero-network-dependency policy gate that enforces safety, privacy, and consent boundaries via term matching and metadata checks. Every Yar API route runs through `CapLiteGuard` before any model inference.

The two codebases have diverged significantly. The standalone repo evolved into a v1 research architecture while Yar continued using the simpler v0.1 guard. They share no code at runtime; `Yar/src/yar/cap/` is a re-export bridge that imports from the co-located `Yar/src/cap/` package.

### Key Findings

1. **Two separate CAP packages coexist** with no shared runtime code
2. **Yar's CAP-Lite** is mature and production-ready for its scope (757 lines of guard logic)
3. **The standalone CAP repo** is research-quality scaffolding, not a deployable runtime
4. **52 test files** in the standalone repo cover v1 scaffolds that Yar does not use
5. **Documentation is extensive but scattered** across 25+ files in the standalone repo
6. **Cytocast rebuild** is the recommended path forward to unify the two codebases

---

## 2. Current Implementation Assessment

### 2.1 Repository Structure: `CAP/`

The standalone CAP repository at `https://github.com/cytognosis/CAP/` is organized as follows:

```
CAP/
├── src/cap_protocol/               # Main package (v0.1.0)
│   ├── __init__.py                  # Package init, version = "0.1.0"
│   ├── benchmarks.py                # Performance benchmark harness (19.8KB)
│   ├── paths.py                     # Path utilities (1KB)
│   ├── bindings/                    # Transport bindings
│   │   ├── edge_pep_bridge.py       # Edge PEP bridge adapter (9.1KB)
│   │   ├── grpc_reference/          # gRPC reference binding
│   │   └── http_json/               # HTTP/JSON independent binding
│   ├── cli/                         # CLI entry points (7 scripts)
│   │   ├── run_final.py             # Final run script (12.5KB)
│   │   ├── run_hardening.py         # Hardening runner (17.8KB)
│   │   ├── run_benchmarks.py        # Benchmark runner (2.5KB)
│   │   ├── verify_package.py        # Package verification
│   │   ├── verify_release_baseline.py # Release baseline check (7.3KB)
│   │   └── check_v1_schema_drift.py # Schema drift checker
│   ├── conformance/                 # Conformance testing (V1-C01..V1-C15)
│   │   ├── runner.py                # Conformance runner (7.5KB)
│   │   ├── v1_runner.py             # V1 conformance suite (181.8KB!)
│   │   └── fixtures/                # JSONL fixture data
│   ├── hardening/                   # Security hardening utilities
│   │   ├── audit_store.py           # JSONL audit store (3.9KB)
│   │   └── policy_engine.py         # Policy evaluation engine (8.2KB)
│   ├── profiles/                    # Domain profiles
│   │   ├── __init__.py              # Profile exports (2.6KB)
│   │   ├── cap_med.py               # Medical profile (24.9KB)
│   │   ├── cap_swe.py               # Software engineering profile (21.7KB)
│   │   └── inheritance.py           # Profile inheritance system (24.1KB)
│   ├── runtime/                     # Core runtime (29 modules, ~650KB total)
│   │   ├── __init__.py              # Massive re-export index (19.2KB)
│   │   ├── local_pep.py             # Local Policy Enforcement Point (90.1KB!)
│   │   ├── registry.py              # Federated registries (94.6KB!)
│   │   ├── observability.py         # OTel integration (60.5KB)
│   │   ├── supervisor_gateway.py    # Supervisor gateway service (41.1KB)
│   │   ├── substrate_interop.py     # MCP/A2A substrate interop (41.5KB)
│   │   ├── controller.py            # Controller service (27.7KB)
│   │   ├── human_review.py          # Human review workflows (30.5KB)
│   │   ├── attested_local_pep.py    # Attested local PEP (30.2KB)
│   │   ├── workflow_engine.py       # Temporal-style workflow engine (27KB)
│   │   ├── lifecycle.py             # Lifecycle FSM (25.7KB)
│   │   ├── mobile_local_pep.py      # Mobile PEP proxy (20.8KB)
│   │   ├── live_model_streaming.py  # Live model streaming (18KB)
│   │   ├── edge_pep.py              # Edge PEP (18.8KB)
│   │   ├── privacy_pdp.py           # Privacy PDP (17.4KB)
│   │   ├── redaction.py             # NER redaction (17.5KB)
│   │   ├── session_router.py        # Session routing (16.4KB)
│   │   ├── interrupts.py            # Interrupt decisions (16.4KB)
│   │   ├── service_mesh.py          # Service mesh composition (14.1KB)
│   │   ├── embeddings.py            # Embedding-only egress (14.2KB)
│   │   ├── authority.py             # Authority chain (13.1KB)
│   │   ├── ui_correction.py         # UI correction frames (13KB)
│   │   ├── ui_abort.py              # UI abort propagation (12.2KB)
│   │   ├── slow_path_classifier.py  # Semantic slow-path (10.7KB)
│   │   ├── pdp_adapters.py          # OPA/Cedar PDP adapters (10.8KB)
│   │   ├── warrants.py              # Biscuit warrants (9.1KB)
│   │   ├── workload_identity.py     # SPIFFE identity (6.8KB)
│   │   ├── temporal.py              # Temporal validation (5.2KB)
│   │   └── retention.py             # Retention TTL deletion (3KB)
│   ├── scenarios/                   # Reference scenarios
│   │   └── therapist_supervisor/    # 15-case therapist/supervisor demo
│   ├── schema/                      # Schema utilities
│   │   ├── __init__.py              # Schema exports
│   │   └── linkml.py                # LinkML integration (8.8KB)
│   └── security/                    # Security primitives
│       ├── cap_crypto.py            # Ed25519/DSSE signing (14.6KB)
│       ├── cert_manager.py          # Certificate management (4KB)
│       └── transparency.py          # Transparency log (13.7KB)
├── schemas/                         # Schema definitions
│   ├── cap.yaml                     # Umbrella LinkML schema (1.9KB)
│   ├── core.yaml                    # Core types/enums/classes (5.4KB)
│   ├── domains/                     # Domain schema modules (7 YAML files)
│   │   ├── authority.yaml           # Authority chain schemas (3.3KB)
│   │   ├── capability.yaml          # Capability schemas (1.4KB)
│   │   ├── constraints.yaml         # Constraints schemas (1.8KB)
│   │   ├── control.yaml             # Control schemas (8.3KB)
│   │   ├── evidence.yaml            # Evidence schemas (1.6KB)
│   │   ├── privacy.yaml             # Privacy boundary schemas (3.8KB)
│   │   └── profiles.yaml            # Profile schemas (6.4KB)
│   ├── cap-core/v0.1/               # 9 JSON schemas for v0.1
│   └── cap-core/v1/                 # 12 JSON schemas for v1
├── policies/                        # Policy-as-data files
│   ├── cap_core_policy.json         # Core policy rules
│   └── cap_med_policy.json          # Medical profile policy
├── docs/                            # 25 documentation files + 3 subdirectories
├── tests/                           # 52 test files
├── reference_grpc/                  # Legacy gRPC wrapper
├── second_http/                     # Legacy HTTP/JSON wrapper
├── third_impl/go_cap_adapter/       # Go interop adapter
├── examples/cap-core/               # Example scripts
├── scripts/                         # Build and validation scripts (6 files)
├── config/otel/                     # OpenTelemetry configuration
└── pyproject.toml                   # Package metadata
```

### 2.2 Package Configuration

From `pyproject.toml`:

- **Name**: `cap-protocol`
- **Version**: `0.1.0`
- **Python**: `>=3.12`
- **Dependencies**: `biscuit-python>=0.4,<0.5`, `cryptography>=42.0.0`, `grpcio==1.71.2`, `jsonschema>=4.22.0`, `protobuf==5.29.5`
- **Dev dependencies**: `grpcio-tools`, `linkml-runtime`, `pre-commit`, `PyYAML`, `pytest`
- **CLI scripts**: 8 registered entry points (`cap-run-final`, `cap-run-hardening`, `cap-verify-package`, `cap-verify-release-baseline`, `cap-check-v1-schema-drift`, `cap-check-v1-conformance`, `cap-run-v1-benchmarks`, `cap-run-therapist-supervisor-demo`)

### 2.3 Core Runtime Modules

The runtime layer (`src/cap_protocol/runtime/`) exports 660+ symbols. Key classes and components:

| Module | Size | Key Classes/Functions | Purpose |
|---|---|---|---|
| `local_pep.py` | 90KB | `LocalPEP`, `PEPDecision` | Local Policy Enforcement Point, primary hot path |
| `registry.py` | 94KB | `CapabilityRegistry`, `PolicyRegistry`, `EvidenceRegistry`, `AgentToolRegistry` | Federated registry services |
| `observability.py` | 60KB | `CAPOtelEvent`, `validate_cap_otel_events` | OpenTelemetry event generation/validation |
| `supervisor_gateway.py` | 41KB | `SupervisorGatewayService` | Supervisor gateway HTTP service |
| `substrate_interop.py` | 41KB | MCP/A2A substrate interop | Live substrate composition scaffolding |
| `controller.py` | 27KB | `ControllerService`, `ControllerGuardEvaluator` | Controller decomposed service |
| `human_review.py` | 30KB | `HumanReviewService`, `HumanReviewPortal` | Human-in-the-loop review workflows |
| `attested_local_pep.py` | 30KB | Attested PEP registration | Platform attestation for mobile/device |
| `workflow_engine.py` | 27KB | `WorkflowHistoryEvent`, `WorkflowRetryPolicy` | Temporal-style workflow composition |
| `lifecycle.py` | 25KB | Lifecycle FSM, profile inheritance | State machine for CAP lifecycle |
| `privacy_pdp.py` | 17KB | `PrivacyPDPDecision` | 9-dimensional privacy boundary evaluation |
| `redaction.py` | 17KB | Local NER redaction | Pre-Supervisor redaction pipeline |
| `embeddings.py` | 14KB | Embedding-only egress | Privacy-preserving embedding projection |

### 2.4 Transport Bindings

Three independent transport implementations:

1. **gRPC Reference Binding** (`bindings/grpc_reference/`): Protobuf-based binding over v1 `CAPEnvelope`
2. **HTTP/JSON Independent Binding** (`bindings/http_json/`): REST-style binding over v1 `CAPEnvelope`
3. **Go Interop Adapter** (`third_impl/go_cap_adapter/`): Standard-library Go fixture validator for CAPEnvelope/JCS signatures

### 2.5 Profiles

Two domain profiles implemented:

- **CAP-Med** (`profiles/cap_med.py`, 24.9KB): Medical/psychology profile with non-diagnostic constraints, redaction requirements, evidence minimization, clinical-output blocking, and safe question revision
- **CAP-SWE** (`profiles/cap_swe.py`, 21.7KB): Software engineering profile with tool risk levels, file write directives, and code-specific operational constraints
- **Profile Inheritance** (`profiles/inheritance.py`, 24.1KB): Composition system with `ProfileDefinition`, `ProfileCompositionResult`, forbidden core override keys, and risk ordering

---

## 3. Yar CAP-Lite Implementation

### 3.1 Module Structure

The Yar-embedded CAP package at `Yar/src/cap/` contains 7 source files:

| File | Size | Purpose |
|---|---|---|
| `__init__.py` | 2.6KB | Package init with lazy imports for `CapLiteGuard` and `primitives` |
| `guard.py` | 29.7KB | `CapLiteGuard` class, 757 lines of deterministic policy evaluation |
| `primitives.py` | 14.1KB | Factory functions for Directives, Refusals, Reports, Evidence, DecisionRecords |
| `models.py` | 1.5KB | `GuardDecision` and `GuardDecisionValue` Pydantic models |
| `protocols.py` | 1.6KB | `CaptureProtocol`, `WriteOperationProtocol`, `WritePlanProtocol` structural types |
| `policies.py` | 1.2KB | JSON policy loader using `importlib.resources` |
| `constants.py` | 440B | Version, profile namespace, SPIFFE identity URIs |

Plus a `data/` directory containing bundled policy JSON files:
- `cap_core_policy.json` (877B)
- `cap_med_policy.json` (623B)

### 3.2 CapLiteGuard: Guard Rules

The `CapLiteGuard` class implements six categories of deterministic boundary enforcement:

#### Crisis Detection (highest priority, immediate deny)
- **Terms**: 22 crisis terms in English and Farsi ("end my life", "kill myself", "suicidal", "خودکشی", "می‌خوام بمیرم", etc.)
- **Action**: Immediate deny with `refer_to_human_support` directive
- **Response**: Provides crisis hotline numbers (Iran: 1480, International: findahelpline.com)
- **Constraint**: `no_object_write`, `refer_to_human_support`

#### Diagnosis Boundary
- **Terms**: 22 terms in English and Farsi ("diagnose me", "do i have adhd", "تشخیص بده", etc.)
- **Action**: Deny with forbidden action `diagnosis`
- **Refusal**: "Yar cannot provide diagnosis or clinical conclusions."

#### Treatment Boundary
- **Terms**: 13 static terms + 4 compiled regex patterns for treatment advice detection
- **Harmless context filter**: Skips detection for policy descriptions (e.g., "must not recommend treatment")
- **Diagnostic claim patterns**: 2 regex patterns detecting definitive claims ("user has clinical depression")
- **Action**: Deny with forbidden action `medical_treatment_recommendation`

#### Intent Attribution Boundary
- **Terms**: 8 terms ("true intent", "really feels", "secretly feels", etc.)
- **Action**: Deny with forbidden action `claim_another_person_true_intent_or_emotion`

#### Raw Data Sharing Boundary
- **Terms**: 4 terms ("share raw", "send raw", "upload raw", "publish raw")
- **Condition**: Only triggers when `user_confirmed_external_write` is `False`
- **Action**: Deny with forbidden action `raw_data_sharing_without_consent`

#### Health Risk Scoring Boundary
- **Terms**: 4 terms ("health risk score", "risk scoring", "score my health", "health score")
- **Action**: Deny with forbidden action `health_risk_scoring`

### 3.3 Evaluation Methods

The guard exposes five public methods:

1. **`evaluate(capture, candidate_objects, target_external_write)`**: Capture-level safety evaluation. Checks all six boundaries in priority order (crisis first). Returns `GuardDecision` with full audit trail.

2. **`validate_external_write(operation_or_plan)`**: Validates Anytype write operations. Checks action type (`create`/`update`/`delete`), target kind (`object`/`type`/`property`/`relation`), delete-without-id, user confirmation, raw content presence, and health boundary text.

3. **`validate_local_object_update(values)`**: Checks if a local object mutation contains diagnosis, treatment, diagnostic claim, intent, or risk content.

4. **`validate_local_link(source_id, target_id, relation)`**: Validates link creation (safe identifier pattern, no self-links except `related_to`).

5. **`validate_local_relation(relation)`**: Validates relation names match `^[A-Za-z][A-Za-z0-9_]*$`.

### 3.4 Primitives Module

Factory functions produce well-formed CAP v0.1 message dicts:

| Function | Returns |
|---|---|
| `directive()` | CAP Directive with action_kind, target, operation, evidence, scope_tags |
| `refusal_message()` | Typed refusal with reason_code, reason_detail, retryable flag |
| `execution_report()` | Audit record with observations, evidence_produced, side_effects, errors |
| `decision_record()` | Decision audit with question, selected_option, evidence_used, policy_refs |
| `evidence_ref_for_capture()` | Evidence reference with SHA-256 hash, redacted pointer |
| `evidence_ref_for_operation()` | Evidence reference for write operations |
| `constraints_for_context()` | Constraint set with allowed_actions, scope_tags, confirmation state |
| `default_policy_refs()` | Core and med policy references |
| `capabilities_matrix()` | Full CAP capabilities declaration for the Yar instance |

### 3.5 GuardDecision Model

Pydantic model with 15 fields:

```python
class GuardDecision(BaseModel):
    cap_version: str = "0.1"
    decision_id: str                    # UUID
    guarded_message_id: str | None
    guard_identity: str                 # SPIFFE URI
    guard_capability: str               # "cap.guard.evaluate"
    directive: str                      # Action directive
    allowed_actions: list[str]
    forbidden_actions: list[str]
    guard_decision: GuardDecisionValue  # allow | allow_with_constraints | deny
    severity: str                       # "audit" or "block"
    constraints: list[str]
    constraints_added: dict
    policy_refs: list[dict]
    evidence_required: list[dict]
    refusal_reason: str | None
    refusal_message: dict | None
    decision_record: dict | None
    cap_directive: dict | None
    execution_report: dict
```

### 3.6 Protocols (Structural Typing)

Three `@runtime_checkable` Protocol classes define the contracts:

- **`CaptureProtocol`**: `raw_content`, `source_type`, `user_confirmed_external_write`, `capture_id`, `raw_local_only`
- **`WriteOperationProtocol`**: `operation_id`, `action`, `target_kind`, `title`, `type_name`, `properties`, `links`, `external_id`, `dry_run`, `user_confirmed_external_write`
- **`WritePlanProtocol`**: `operations: list[WriteOperationProtocol]`

### 3.7 Policy Definitions

Two JSON policy files define declarative rules:

**Core Policy** (`cap_core_policy.json`):
- `default_decision`: `"deny"` (deny-wins semantics)
- `allowed_message_types`: Directive, GuardDecision, ExecutionReport, RefusalMessage, DecisionRecord
- `required_top_level_fields`: 11 fields (cap_version, message_id, message_type, sender_id, etc.)
- `forbidden_tools`: `edge://diagnosis/label_user`, `edge://treatment/prescribe`, `network://raw_transcript/upload`
- `allowed_data_access`: redacted_transcript, dimension_vector, safety_flags, evidence_refs_only
- `raw_transcript_forbidden`: true
- `clinical_output_forbidden`: true
- `hidden_cot_forbidden`: true

**Med Policy** (`cap_med_policy.json`):
- `non_diagnostic_required`: true
- `non_prescriptive_required`: true
- `clinical_output_forbidden`: true
- `blocked_terms`: 10 terms including prompt injection attempts ("ignore cap", "execute without constraints", "system: ignore")
- `safety_question_must_address`: safe, support, contact, nearby, right now

---

## 4. Yar Integration Points

### 4.1 Bridge Module: `Yar/src/yar/cap/`

The Yar project maintains a bridge module at `Yar/src/yar/cap/` that re-exports all public symbols from the standalone `cap` package. This allows `from yar.cap import ...` imports to continue working:

```python
# Yar/src/yar/cap/__init__.py
"""Yar bridge to the standalone ``cap`` package.

This module re-exports all public symbols from the standalone ``cap``
package so that existing ``from yar.cap import ...`` imports continue
to work without modification.

The canonical implementation lives in ``src/cap/``. This bridge exists
solely for backward compatibility within the Yar codebase.
"""
from cap import (
    CAP_VERSION, CONTROLLER_IDENTITY, EXECUTOR_IDENTITY, GUARD_IDENTITY,
    PROFILE_NS, CapLiteGuard, CaptureProtocol, GuardDecision,
    GuardDecisionValue, WriteOperationProtocol, WritePlanProtocol,
    load_core_policy, load_med_policy, load_policy, primitives,
)
```

Additional bridge files in `yar/cap/`:
- `guard.py`: `from cap.guard import CapLiteGuard`
- `models.py`: `from cap.models import GuardDecision, GuardDecisionValue`
- `policies.py`: `from cap.policies import load_core_policy, load_med_policy, load_policy`
- `constants.py`: `from cap.constants import CAP_VERSION, ...`

### 4.2 API Routes Using CAP

Six Yar source files directly instantiate `CapLiteGuard`:

| File | Usage | Guard Methods Called |
|---|---|---|
| `yar/api/routes_communication.py` | Pre-evaluates captures before processing | `evaluate()` (3 call sites) |
| `yar/api/routes_anytype.py` | Guards Anytype write operations | `evaluate()`, `validate_external_write()` |
| `yar/api/routes_cap.py` | Exposes `/cap/rules`, `/cap/capabilities`, `/cap/audit` | Direct guard introspection |
| `yar/api/routes_objects.py` | Guards object mutations and link creation | `validate_local_object_update()`, `validate_local_link()` |
| `yar/api/routes_voice.py` | Guards voice interaction writes | `validate_external_write()` |
| `yar/core/coordinator.py` | Coordinator holds a guard instance | `self.guard = CapLiteGuard()` |
| `yar/core/interactive_assistant.py` | Interactive assistant holds a guard instance | `self.guard = CapLiteGuard()` |
| `yar/core/voice_service.py` | Voice service holds a guard instance | `self.guard = CapLiteGuard()` |
| `yar/models/guard.py` | Model imports `GuardDecision` | Type reference only |

### 4.3 CAP API Endpoints in Yar

The `routes_cap.py` module exposes three CAP-specific HTTP endpoints:

1. **`GET /cap/rules`**: Returns the complete guard rule set (term dictionaries, matching strategy, policy refs)
2. **`GET /cap/capabilities`**: Returns the CAP capabilities matrix from `primitives.capabilities_matrix()`
3. **`GET /cap/audit`**: Returns capture reports and voice reports from the SQLite store (with configurable limit)

### 4.4 Integration Pattern

Every Yar operation follows a consistent pattern:

1. Instantiate `CapLiteGuard()` (lightweight, no state)
2. Call the appropriate `evaluate()` or `validate_*()` method
3. Check `guard_decision` for `allow`, `allow_with_constraints`, or `deny`
4. If denied: return the `refusal_message` to the user, log the `decision_record`
5. If allowed: apply `constraints` and proceed, include `execution_report` in audit

---

## 5. Previous Designs and Evolution

### 5.1 Yar Documentation References

The Yar docs directory at `Yar/docs/` contains several CAP-related documents:

| Document | Description |
|---|---|
| `architecture/02_cap_comprehensive.md` | "Communication Augmentation Protocol": the schema-first coordination layer |
| `research/cap_yar_comprehensive_reference.md` | Unified reference merging CAP protocol design with Yar implementation |

The early design positioned CAP as a "Communication Augmentation Protocol", a broader schema-first coordination layer for agent-to-agent and agent-to-human messaging. This was later narrowed and reframed.

### 5.2 CAP Naming Evolution

CAP has undergone a naming and scope evolution:

1. **Communication Augmentation Protocol** (original Yar docs): Broad schema-first coordination layer
2. **Control Authority Profile** (v0.1): Narrowed to safety/privacy policy enforcement
3. **Control Authority Protocol** (v1 target): Reframed as a supervisory control plane above existing transports

The current v1 framing is the most defensible: CAP is not a transport, tool-calling, or agent-discovery protocol. It is a supervisory control layer that makes agentic actions explicitly authorized, evidence-bound, privacy-bounded, interruptible, refusable, and auditable.

### 5.3 CAP v1 Architecture Vision

From the standalone repo's `docs/CAP_00_README.md`, the v1 target architecture is hybrid, two-tier, and three-plane:

- **Local tier**: Local PEPs near agents, tools, and user surfaces. Enforce raw-evidence substitution, local retention TTL deletion, NER redaction, embedding-only projection, non-diagnostic output, semantic slow-path checks, typed refusal, offline fallback, and streaming interruption.
- **Remote tier**: Controller, Supervisor, Registries, and observability collectors in a remote trust boundary.
- **Three planes**: Data plane (evidence and actions), Control plane (authority and policy), Observability plane (audit and tracing).

A CAP trace answers four questions: (1) Who authorized this action? (2) What evidence bounds this decision? (3) What privacy boundary applies? (4) Can this be interrupted or refused?

### 5.4 v1 Specification Documents

The standalone repo contains a complete 7-chapter document set:

| Document | Size | Topic |
|---|---|---|
| `CAP_00_README.md` | 12.4KB | Overview, positioning, references |
| `CAP_01_foundations.md` | 12.7KB | Design principles, threat model basis |
| `CAP_02_core_model.md` | 21.3KB | Core object model (CAPEnvelope, typed payloads) |
| `CAP_03_primitives.md` | 24.2KB | Primitive definitions (Directive, GuardDecision, InterruptDecision, etc.) |
| `CAP_04_security_trust_evidence.md` | 30.9KB | Security architecture, trust boundaries, evidence |
| `CAP_05_integrations.md` | 20.4KB | Integration with A2A, MCP, OPA, SPIFFE, OTel |
| `CAP_06_conformance.md` | 26.1KB | Conformance testing (V1-C01..V1-C15) |
| `CAP_07_profiles_roadmap.md` | 18.9KB | Profile system, roadmap, future profiles |

### 5.5 Refactoring History

From `REFACTORING_NOTES.md`:
- Modules moved into `src/cap_protocol`
- Legacy top-level commands preserved as thin wrappers
- Schemas and policies kept as top-level canonical artifacts
- Runtime model dependency installation removed (fail-fast instead)
- Protobuf regeneration moved to `scripts/generate_proto.py`

---

## 6. Schema and Policy Architecture

### 6.1 LinkML Schema System

The v1 schema is authored in LinkML with an umbrella schema (`schemas/cap.yaml`) importing:

- `core.yaml`: Shared types (`Identifier`, `CAPVersion`, `Timestamp`, `SHA256Digest`, `MediaType`, `URIOrReference`), enums (`ReversibilityEnum`, `InterruptTypeEnum`, `ConsentBasis`, `ConfidentialityLabelEnum`, etc.), and abstract base classes (`CAPObject`, `JsonObject`, `Signature`, `ProfileExtensionMap`)
- `domains/authority.yaml`: Authority chain schemas (3.3KB)
- `domains/evidence.yaml`: Evidence reference schemas (1.6KB)
- `domains/privacy.yaml`: 9-dimensional privacy boundary (3.8KB)
- `domains/capability.yaml`: Capability schemas (1.4KB)
- `domains/constraints.yaml`: Operational constraints (1.8KB)
- `domains/control.yaml`: Control objects including CAPEnvelope, Directive, GuardDecision, InterruptDecision, ExecutionReport, RefusalMessage (8.3KB)
- `domains/profiles.yaml`: Profile definition schemas (6.4KB)

### 6.2 JSON Schema Artifacts

Two generations of JSON schemas coexist:

**v0.1 schemas** (`schemas/cap-core/v0.1/`, 9 files):
- `cap-message.schema.json`, `directive.schema.json`, `guard-decision.schema.json`
- `execution-report.schema.json`, `refusal-message.schema.json`
- `decision-record.schema.json`, `evidence-ref.schema.json`
- `authority-chain-step.schema.json`, `policy-ref.schema.json`

**v1 schemas** (`schemas/cap-core/v1/`, 12 files):
- Everything from v0.1 plus: `cap-envelope.schema.json`, `capability.schema.json`
- `interrupt-decision.schema.json`, `operational-constraints.schema.json`
- `privacy-boundary.schema.json`

**v1 additions over v0.1**: CAPEnvelope (typed envelope with routing), InterruptDecision (7 interrupt types), OperationalConstraints (tool/network/data/confirmation limits), PrivacyBoundary (9 dimensions), Capability (capability URIs).

### 6.3 PrivacyBoundary: 9 Dimensions

The v1 PrivacyBoundary schema defines nine first-class privacy dimensions:
1. **Classification**: Confidentiality label
2. **Movement**: Data locality constraints
3. **Transformation**: Required transformations before egress
4. **Retention**: TTL and deletion requirements
5. **Logging**: What gets logged
6. **Audit visibility**: Who can see audit records
7. **Allowed recipients**: Permitted data recipients
8. **Raw-data egress**: Whether raw data can leave the boundary
9. **Minimization**: Data minimization requirements

### 6.4 CAP-Med Policy Schema

The `cap-med` schema (`schemas/cap-med/v0.1/`) extends core with non-diagnostic psychology domain constraints, providing evidence schemas for the medical profile.

---

## 7. Test Coverage Analysis

### 7.1 Standalone CAP Tests

The standalone repo contains 52 test files (`tests/`):

| Test Category | Files | Total Size | Key Tests |
|---|---|---|---|
| **Core runtime** | 15 | ~90KB | `test_cap_v1_pep.py` (56KB!), `test_cap_v1_schemas.py` (16KB), `test_cap_v1_linkml.py` (10KB) |
| **Registry services** | 5 | ~43KB | `test_federated_registry.py` (19.9KB), `test_capability_registry_service.py` (9.3KB), `test_policy_registry_service.py` (10.3KB), `test_evidence_registry_service.py` (8.6KB), `test_agent_tool_registry_service.py` (6.8KB) |
| **Security** | 4 | ~29KB | `test_cap_crypto.py` (6.5KB), `test_evidence_tamper.py` (5.3KB), `test_transparency_log.py` (6.8KB), `test_spiffe_workload_identity.py` (9.4KB) |
| **Transport bindings** | 3 | ~15KB | `test_grpc_reference_v1_binding.py` (5.9KB), `test_http_binding.py` (6.3KB), `test_go_interop_adapter.py` (2.6KB) |
| **Profiles** | 3 | ~20KB | `test_cap_med_v1_profile.py` (5.7KB), `test_cap_swe_profile.py` (6.6KB), `test_lifecycle_profile_inheritance.py` (8.4KB) |
| **Privacy/redaction** | 4 | ~35KB | `test_privacy_pdp.py` (9.6KB), `test_local_ner_redaction.py` (8.3KB), `test_embedding_only_egress.py` (9.1KB), `test_retention_ttl_deletion.py` (6.7KB) |
| **UX/interaction** | 3 | ~17KB | `test_human_review_integration.py` (13KB), `test_correction_frame_ux.py` (5.7KB), `test_ui_abort_propagation.py` (5.6KB) |
| **Infrastructure** | 7 | ~45KB | `test_observability_plane.py` (17.8KB), `test_service_mesh_composition.py` (9.6KB), `test_workflow_engine_composition.py` (5.7KB), `test_controller_service.py` (8KB), `test_supervisor_gateway_service.py` (8.1KB), `test_session_router.py` (5.9KB), `test_pdp_adapters.py` (8.3KB) |
| **Other** | 8 | ~45KB | `test_authority_chain.py`, `test_warrant_primitives.py`, `test_interrupt_runtime.py`, `test_attested_local_pep.py`, `test_mobile_local_pep_proxy.py`, `test_live_model_streaming.py`, `test_live_substrate_interop.py`, `test_slow_path_classifier.py` |
| **Conformance/hardening** | 5 | ~12KB | `test_conformance.py`, `test_hardening.py`, `test_schema_validation.py`, `test_benchmark_harness.py`, `test_temporal_validation.py` |
| **Smoke/release** | 3 | ~8KB | `test_cli_smoke.py`, `test_executor_validation.py`, `test_verify_release_baseline.py`, `test_therapist_supervisor_scenario.py`, `test_replay_idempotency.py`, `test_policy_hot_update.py` |

### 7.2 Conformance Suite (V1-C01..V1-C15)

The `conformance/v1_runner.py` at 181.8KB is the largest single file. It implements 15 release-blocking conformance checks:

- V1-C01 through V1-C15 covering: envelope validation, directive structure, guard decision semantics, interrupt decisions, privacy boundary, authority chain, evidence references, transport binding compliance, profile conformance, and cross-implementation fixture verification.

### 7.3 Yar CAP Test Coverage

Yar's test coverage for CAP is embedded in the Yar test suite (not in the CAP repo). The CAP repo tests validate the standalone `cap-protocol` package, not the Yar-embedded `cap` package directly. There is no shared test harness between the two.

---

## 8. Gaps and Issues

### 8.1 Architectural Gaps

| Gap | Severity | Description |
|---|---|---|
| **Two divergent codebases** | Critical | `cap` (Yar) and `cap-protocol` (standalone) share no runtime code |
| **Package naming collision** | High | Two packages with different names (`cap` vs `cap-protocol`) and different APIs |
| **No shared import path** | High | Yar imports from `cap.*`, standalone from `cap_protocol.*` |
| **v0.1/v1 schema mismatch** | Medium | Yar uses v0.1 primitives; standalone scaffolds v1 objects |
| **No production runtime** | High | The standalone repo is scaffolding/research, not a deployable runtime |

### 8.2 Implementation Gaps (Standalone Repo)

From `docs/CAP_FINAL_STATUS.md` and `docs/architecture.md`:

- **No production key infrastructure**: Ed25519 keys are local-dev; no KMS/HSM-backed warrant key custody
- **No externally owned cross-implementation JCS fixtures**: Go adapter uses local fixtures only
- **No native mobile/device certification**: Attested PEP uses scaffolded attestation, not real platform verifiers
- **No production Controller/Supervisor Gateway**: Reference services, not production deployments
- **No production model-provider rollout**: Live model streaming is optional/local Ollama only
- **No production NER/embedding model rollout**: Local deterministic redaction only
- **No production offline policy-bundle operations**: Signed bundles are scaffolded
- **No production registry hardening/deployment**: Federated registries are in-process
- **No production observability exporter/collector integration**: OTel events are generated but not exported
- **No production PROV graph/document store deployment**: W3C PROV is scaffolded
- **No deployed revocation operations**: Biscuit revocation is scaffolded
- **No external multi-organization interoperability**: Only local Go adapter
- **No expanded adversarial conformance coverage**: Limited adversarial fixtures

### 8.3 Documentation Gaps

| Gap | Description |
|---|---|
| **No integration guide** | No guide for integrating CAP into a new application |
| **No API reference** | `docs/api.md` exists but covers the standalone package, not the Yar-embedded guard |
| **No migration guide** | No documentation for migrating from v0.1 to v1 |
| **Duplicate docs** | Multiple overlapping status documents (`CAP_FINAL_STATUS.md`, `CAP_CLAIMS.md`, `CAP_SUPERVISOR_BRIEF_FINAL.md`) |
| **No Yar-specific docs** | CAP's role in Yar is documented in Yar's docs, not in the CAP repo |
| **No cytocast profile docs** | No documentation for how CAP would be templated via cytocast |

### 8.4 Test Gaps

| Gap | Description |
|---|---|
| **No cross-codebase tests** | No tests verify that Yar's `cap` and standalone `cap-protocol` produce compatible artifacts |
| **Scaffolding-heavy tests** | Many tests verify scaffolded fixtures, not real runtime behavior |
| **No integration tests with real models** | Live model tests are optional and require local Ollama |
| **No performance regression tests** | Benchmarks exist but are not CI-gated |
| **No Yar guard unit tests in CAP repo** | The Yar guard rules are tested only in the Yar repo |

### 8.5 Standalone Package Issues

- **File sizes**: Several files exceed reasonable module sizes (`local_pep.py` 90KB, `registry.py` 94KB, `v1_runner.py` 181KB). These should be decomposed.
- **Monolithic __init__.py**: The runtime `__init__.py` re-exports 660+ symbols, making the API surface unmanageable.
- **Build system**: Uses `setuptools` instead of modern `uv`/`hatch` tooling.
- **Pinned dependencies**: `grpcio==1.71.2` and `protobuf==5.29.5` are pinned to exact versions, creating fragility.
- **Heavy dependencies**: `biscuit-python`, `grpcio`, `protobuf` are required even if only using the policy gate.

---

## 9. Docs Reorganization Plan

### 9.1 Proposed Documentation Structure

```
docs/
├── index.md                        # Landing page, project overview
├── getting-started.md              # Quick start guide for new users
│
├── architecture/
│   ├── overview.md                 # Two-tier, three-plane architecture
│   ├── core-model.md              # CAPEnvelope, typed payloads, routing
│   ├── trust-boundaries.md        # Local/remote tier, trust domains
│   └── diagrams/                  # Architecture diagrams (mermaid sources)
│
├── guard-rules/
│   ├── overview.md                # CapLiteGuard philosophy and design
│   ├── crisis-detection.md        # Crisis terms, response protocol
│   ├── boundary-terms.md          # Diagnosis, treatment, intent, raw-share, risk
│   ├── evaluation-methods.md      # evaluate(), validate_external_write(), etc.
│   └── multilingual-support.md    # Farsi support, non-ASCII matching
│
├── primitives/
│   ├── overview.md                # Primitive taxonomy
│   ├── directive.md               # Directive structure and semantics
│   ├── guard-decision.md          # GuardDecision model and values
│   ├── interrupt-decision.md      # InterruptDecision (v1)
│   ├── refusal-message.md         # RefusalMessage structure
│   ├── execution-report.md        # ExecutionReport for audit
│   ├── evidence-ref.md            # EvidenceRef with SHA-256 hashes
│   ├── decision-record.md         # DecisionRecord for transparency
│   └── authority-chain.md         # AuthorityChain/Biscuit warrants
│
├── policies/
│   ├── overview.md                # Policy-as-data architecture
│   ├── core-policy.md             # cap_core_policy.json reference
│   ├── med-policy.md              # cap_med_policy.json reference
│   └── writing-policies.md        # Guide to creating custom policies
│
├── profiles/
│   ├── overview.md                # Profile system architecture
│   ├── cap-med.md                 # Medical profile specification
│   ├── cap-swe.md                 # Software engineering profile
│   ├── inheritance.md             # Profile composition and inheritance
│   └── creating-profiles.md       # Guide to creating new profiles
│
├── privacy/
│   ├── privacy-boundary.md        # 9-dimensional privacy model
│   ├── redaction.md               # NER redaction pipeline
│   ├── embedding-egress.md        # Embedding-only projection
│   └── retention.md               # TTL deletion and data lifecycle
│
├── integration-guide/
│   ├── quickstart.md              # Minimal integration (5 minutes)
│   ├── yar-integration.md         # How Yar uses CAP (reference implementation)
│   ├── fastapi-integration.md     # Generic FastAPI integration pattern
│   ├── transport-bindings.md      # gRPC, HTTP/JSON, custom bindings
│   └── testing-integration.md     # Testing your CAP integration
│
├── api-reference/
│   ├── cap-lite-guard.md          # CapLiteGuard class API
│   ├── primitives-api.md          # primitives module API
│   ├── models-api.md              # Pydantic model API
│   ├── protocols-api.md           # Protocol types API
│   └── policies-api.md            # Policy loader API
│
├── schemas/
│   ├── overview.md                # Schema architecture (LinkML, JSON Schema)
│   ├── v01-schemas.md             # v0.1 schema reference
│   └── v1-schemas.md              # v1 schema reference
│
├── conformance/
│   ├── overview.md                # Conformance testing philosophy
│   ├── v1-conformance.md          # V1-C01..V1-C15 test descriptions
│   └── running-conformance.md     # How to run conformance tests
│
├── security/
│   ├── threat-model.md            # CAP threat model
│   ├── cryptographic-operations.md # Ed25519, DSSE, JCS
│   ├── transparency-log.md        # Audit transparency
│   └── spiffe-identity.md         # SPIFFE SVID integration
│
├── development/
│   ├── contributing.md            # Contribution guide
│   ├── development-setup.md       # Dev environment setup
│   ├── running-tests.md           # Test execution guide
│   └── release-process.md         # Release gates and process
│
└── reference/
    ├── claims.md                  # What CAP claims and does not claim
    ├── changelog.md               # Version changelog
    ├── roadmap.md                 # v1 migration roadmap
    └── paper-positioning.md       # Academic positioning
```

### 9.2 Documentation Principles

1. **Separate Yar-specific from CAP-generic**: CAP docs should describe the protocol; Yar docs should describe Yar's use of CAP
2. **API reference generated from code**: Use Google-style docstrings (already present) with autodoc tooling
3. **Single source of truth**: Eliminate duplicate status/claims documents
4. **Progressive disclosure**: Getting started → guard rules → primitives → full architecture
5. **Schema-driven**: Link docs to the actual JSON/LinkML schema files

---

## 10. Cytocast Rebuild Consideration

### 10.1 Cytocast Overview

Cytocast (`https://github.com/cytognosis/cytocast`) is the Cytognosis Foundation's Copier-based templating engine. It provides standardized project scaffolding with:

- **Copier templates** for non-destructive updates (`copier update`)
- **Profile system** connecting to Cytoskeleton component graphs
- **Skills integration** from the agents repo
- **Pre-configured tooling**: `uv`, `pixi`, `nox`, `ruff`, `mypy`, `pytest`, MkDocs
- **CI/CD pipelines**: GitHub Actions, MkDocs deployment
- **Component system**: `components.yml` for declaring project components

### 10.2 What a Cytocast-Generated CAP Package Would Look Like

A cytocast rebuild would produce a clean, standards-compliant Python package:

```
cap/
├── pyproject.toml              # uv-managed, ruff/mypy configured
├── src/cap/
│   ├── __init__.py             # Clean public API
│   ├── guard.py                # CapLiteGuard (from Yar's cap/guard.py)
│   ├── primitives.py           # Message factories (from Yar's cap/primitives.py)
│   ├── models.py               # Pydantic models (from Yar's cap/models.py)
│   ├── protocols.py            # Structural typing (from Yar's cap/protocols.py)
│   ├── policies.py             # Policy loader (from Yar's cap/policies.py)
│   ├── constants.py            # Version/identity constants
│   ├── data/                   # Bundled policy JSONs
│   ├── schemas/                # JSON Schema artifacts
│   └── py.typed                # PEP 561 type stub marker
├── tests/
│   ├── conftest.py
│   ├── test_guard.py
│   ├── test_primitives.py
│   ├── test_models.py
│   └── test_policies.py
├── docs/                       # MkDocs site (see Section 9)
├── noxfile.py                  # lint, test, typecheck, docs sessions
├── .github/workflows/          # CI/CD
└── .agents/                    # Skills from agents repo
```

### 10.3 Cytocast Templates Needed

| Template/Component | Purpose |
|---|---|
| **profile**: `cap-protocol` | New cytocast profile for CAP-style governance packages |
| **component**: `guard` | Deterministic policy gate with term matching |
| **component**: `primitives` | CAP message factories |
| **component**: `schemas` | JSON Schema + LinkML schema management |
| **component**: `policies` | Policy-as-data loading and validation |
| **component**: `profiles` | Domain profile system (cap-med, cap-swe) |
| **nox session**: `conformance` | Conformance test runner |
| **nox session**: `schema-drift` | Schema drift detection |

### 10.4 Tests to Preserve

From the current codebases, these tests provide genuine value and should be preserved:

**From Yar's CAP tests (implicit in Yar test suite):**
- Crisis detection with English and Farsi terms
- Diagnosis boundary enforcement
- Treatment boundary with regex patterns and harmless context filtering
- External write validation (action type, target kind, consent, raw content)
- Local object mutation safety checks
- Link and relation validation

**From standalone CAP repo:**
- Schema validation (`test_schema_validation.py`, `test_cap_v1_schemas.py`)
- Authority chain verification (`test_authority_chain.py`)
- Conformance basics (`test_conformance.py`)
- Crypto operations (`test_cap_crypto.py`)
- Profile inheritance (`test_lifecycle_profile_inheritance.py`)

**Tests to NOT preserve (scaffolding-only):**
- Most of the 29 runtime module tests, as they test scaffolded fixtures
- Registry service tests (in-process-only registries)
- Transport binding tests (until real bindings are deployed)
- Mobile/attested PEP tests (until real attestation is available)

### 10.5 Migration Strategy

Phase 1: **Extract Yar CAP-Lite as standalone package via cytocast**
- Generate new `cap` package from cytocast template
- Copy Yar's `src/cap/` modules as the canonical source
- Add comprehensive unit tests (port from Yar test suite)
- Publish as `cytognosis-cap` on PyPI

Phase 2: **Update Yar to depend on the new package**
- Replace `Yar/src/cap/` with a `cytognosis-cap` dependency
- Update `Yar/src/yar/cap/` bridge to import from `cytognosis_cap`
- Verify all API routes continue to work

Phase 3: **Selective v1 feature adoption**
- Add v1 schemas to the new package
- Add profile system (inheritance, cap-med, cap-swe)
- Add privacy boundary model (9 dimensions)
- Gate behind optional extras: `pip install cytognosis-cap[profiles,schemas]`

Phase 4: **Deprecate standalone CAP repo**
- Archive `CAP/` repo as research reference
- Move valuable documentation to the new package
- Keep conformance fixtures for historical traceability

---

## 11. Migration Roadmap

### Phase 1: Foundation (Week 1-2)

- [ ] Create cytocast profile for CAP packages
- [ ] Generate new `cap` package from template
- [ ] Port Yar CAP-Lite modules (guard, primitives, models, protocols, policies, constants)
- [ ] Port and expand unit tests
- [ ] Set up CI/CD (lint, test, typecheck, docs)
- [ ] Configure MkDocs documentation site

### Phase 2: Yar Integration (Week 2-3)

- [ ] Publish `cytognosis-cap` v0.1.0 to internal/PyPI
- [ ] Update Yar `pyproject.toml` to depend on `cytognosis-cap`
- [ ] Update import paths in Yar bridge module
- [ ] Run Yar test suite to verify compatibility
- [ ] Remove `Yar/src/cap/` source files (keep bridge only)

### Phase 3: Schema and Profile Enrichment (Week 3-5)

- [ ] Add JSON Schema v1 artifacts to new package
- [ ] Add LinkML schema source files
- [ ] Port profile system (inheritance, cap-med, cap-swe)
- [ ] Add privacy boundary model
- [ ] Add conformance test framework (subset of V1-C01..C15)
- [ ] Write integration guide documentation

### Phase 4: Advanced Features (Week 5-8)

- [ ] Add configurable guard (allow custom term dictionaries)
- [ ] Add policy engine (beyond static JSON)
- [ ] Add audit store interface
- [ ] Add transport binding abstractions
- [ ] Add observability hooks (OTel event generation)

### Phase 5: Archive and Sunset (Week 8-10)

- [ ] Archive standalone `CAP/` repo
- [ ] Migrate valuable docs to new package
- [ ] Update all org-wide references to point to new package
- [ ] Write migration guide for any external consumers

---

## Appendix: Complete File Inventory

### A.1 Standalone CAP Repo: Source Files (`src/cap_protocol/`)

| Path | Size | Description |
|---|---|---|
| `__init__.py` | 105B | Package init, `__version__ = "0.1.0"` |
| `benchmarks.py` | 19.8KB | Performance benchmark harness |
| `paths.py` | 1KB | Path utilities |
| `bindings/__init__.py` | — | Bindings package |
| `bindings/edge_pep_bridge.py` | 9.1KB | Edge PEP bridge adapter |
| `bindings/grpc_reference/` | — | gRPC reference binding (protobuf) |
| `bindings/http_json/` | — | HTTP/JSON independent binding |
| `cli/__init__.py` | — | CLI package |
| `cli/run_final.py` | 12.5KB | Final run entry point |
| `cli/run_hardening.py` | 17.8KB | Hardening runner |
| `cli/run_benchmarks.py` | 2.5KB | Benchmark runner |
| `cli/verify_package.py` | 265B | Package verification |
| `cli/verify_release_baseline.py` | 7.3KB | Release baseline check |
| `cli/check_v1_schema_drift.py` | 364B | Schema drift checker |
| `conformance/__init__.py` | — | Conformance package |
| `conformance/runner.py` | 7.5KB | Conformance runner |
| `conformance/v1_runner.py` | 181.8KB | Full V1 conformance suite |
| `conformance/fixtures/` | — | JSONL fixture data |
| `hardening/__init__.py` | — | Hardening package |
| `hardening/audit_store.py` | 3.9KB | JSONL audit store |
| `hardening/policy_engine.py` | 8.2KB | Policy evaluation engine |
| `profiles/__init__.py` | 2.6KB | Profile exports |
| `profiles/cap_med.py` | 24.9KB | Medical profile |
| `profiles/cap_swe.py` | 21.7KB | Software engineering profile |
| `profiles/inheritance.py` | 24.1KB | Profile inheritance system |
| `runtime/__init__.py` | 19.2KB | Runtime re-export index (660+ symbols) |
| `runtime/local_pep.py` | 90.1KB | Local Policy Enforcement Point |
| `runtime/registry.py` | 94.6KB | Federated registries |
| `runtime/observability.py` | 60.5KB | OTel integration |
| `runtime/supervisor_gateway.py` | 41.1KB | Supervisor gateway |
| `runtime/substrate_interop.py` | 41.5KB | MCP/A2A substrate interop |
| `runtime/human_review.py` | 30.5KB | Human review workflows |
| `runtime/attested_local_pep.py` | 30.2KB | Attested local PEP |
| `runtime/controller.py` | 27.7KB | Controller service |
| `runtime/workflow_engine.py` | 27KB | Workflow engine |
| `runtime/lifecycle.py` | 25.7KB | Lifecycle FSM |
| `runtime/mobile_local_pep.py` | 20.8KB | Mobile PEP proxy |
| `runtime/live_model_streaming.py` | 18KB | Live model streaming |
| `runtime/edge_pep.py` | 18.8KB | Edge PEP |
| `runtime/privacy_pdp.py` | 17.4KB | Privacy PDP |
| `runtime/redaction.py` | 17.5KB | NER redaction |
| `runtime/session_router.py` | 16.4KB | Session routing |
| `runtime/interrupts.py` | 16.4KB | Interrupt decisions |
| `runtime/service_mesh.py` | 14.1KB | Service mesh composition |
| `runtime/embeddings.py` | 14.2KB | Embedding-only egress |
| `runtime/authority.py` | 13.1KB | Authority chain |
| `runtime/ui_correction.py` | 13KB | UI correction frames |
| `runtime/ui_abort.py` | 12.2KB | UI abort propagation |
| `runtime/slow_path_classifier.py` | 10.7KB | Semantic slow-path |
| `runtime/pdp_adapters.py` | 10.8KB | OPA/Cedar PDP adapters |
| `runtime/warrants.py` | 9.1KB | Biscuit warrants |
| `runtime/workload_identity.py` | 6.8KB | SPIFFE identity |
| `runtime/temporal.py` | 5.2KB | Temporal validation |
| `runtime/retention.py` | 3KB | Retention TTL deletion |
| `scenarios/__init__.py` | 43B | Scenarios package |
| `scenarios/therapist_supervisor/` | — | 15-case therapist/supervisor demo |
| `schema/__init__.py` | 610B | Schema exports |
| `schema/linkml.py` | 8.8KB | LinkML integration |
| `security/__init__.py` | — | Security package |
| `security/cap_crypto.py` | 14.6KB | Ed25519/DSSE signing |
| `security/cert_manager.py` | 4KB | Certificate management |
| `security/transparency.py` | 13.7KB | Transparency log |

### A.2 Standalone CAP Repo: Test Files (`tests/`)

52 test files totaling ~400KB. See Section 7.1 for categorized listing.

### A.3 Standalone CAP Repo: Documentation (`docs/`)

25 documentation files plus 3 subdirectories. See Section 5.4 for the specification document set.

### A.4 Yar CAP-Lite: Source Files (`Yar/src/cap/`)

| Path | Size | Description |
|---|---|---|
| `__init__.py` | 2.6KB | Package init with lazy imports |
| `guard.py` | 29.7KB | CapLiteGuard (757 lines) |
| `primitives.py` | 14.1KB | CAP message factories |
| `models.py` | 1.5KB | GuardDecision Pydantic model |
| `protocols.py` | 1.6KB | Structural typing protocols |
| `policies.py` | 1.2KB | Policy loader |
| `constants.py` | 440B | Version and identity constants |
| `data/cap_core_policy.json` | 877B | Core policy rules |
| `data/cap_med_policy.json` | 623B | Med profile policy |

**Total Yar CAP-Lite**: ~52KB of source code (excluding data files).

### A.5 Yar Bridge Module (`Yar/src/yar/cap/`)

| Path | Description |
|---|---|
| `__init__.py` | Re-exports all 14 public symbols from standalone `cap` package |
| `guard.py` | Re-exports `CapLiteGuard` |
| `models.py` | Re-exports `GuardDecision`, `GuardDecisionValue` |
| `policies.py` | Re-exports `load_core_policy`, `load_med_policy`, `load_policy` |
| `constants.py` | Re-exports version and identity constants |

### A.6 Top-Level CAP Repo Files

| File | Size | Description |
|---|---|---|
| `README.md` | 12KB | Repository documentation |
| `REFACTORING_NOTES.md` | 1.4KB | Migration notes |
| `CHANGELOG.md` | 1KB | Version history |
| `pyproject.toml` | 1.8KB | Package configuration |
| `requirements.txt` | 466B | Production dependencies |
| `requirements-dev.txt` | 111B | Dev dependencies |
| `.pre-commit-config.yaml` | 845B | Pre-commit hooks |
| `.env.example` | 448B | Environment template |
| `modal_app.py` | 633B | Modal deployment script |
| `run_final_cap.py` | 323B | Legacy final runner |
| `run_production_hardening.py` | 327B | Legacy hardening runner |
| `VERIFY_FINAL_PACKAGE.py` | 337B | Legacy package verifier |
| `VERIFY_RELEASE_BASELINE.py` | 337B | Legacy baseline verifier |
| `RUN_CAP_COLAB.sh` | 126B | Colab launcher |
| `CAP_v0.1_Production_Candidate_Supervisor_Report(1).md` | 3.6KB | Supervisor report |
| `CODE_OF_CONDUCT.md` | 4.8KB | Code of conduct |
| `CONTRIBUTING.md` | 872B | Contributing guide |
| `LICENSE` | 10.1KB | Apache 2.0 license |
| `SECURITY.md` | 990B | Security policy |
| `cytognosis_cap_v01_final_colab.ipynb` | 1.2KB | Colab notebook |
| `cytognosis_cap_v01_production_candidate_colab.ipynb` | 1.2KB | Colab notebook |
