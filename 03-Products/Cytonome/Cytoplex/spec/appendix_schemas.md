> **Status**: Draft
> **Date**: 2026-06-14
> **Author**: @mohammadi
> **Audience**: engineers
> **Tags**: `cap`, `cytoplex`, `spec`

# CAP Appendix — Schemas

This appendix is split into two layers:

1. The v0.1 executable compatibility layer remains available. The inline JSON Schema Draft 2020-12 skeletons below describe the v0.1-candidate message shapes still preserved by legacy compatibility helpers and fixtures; the active gRPC and HTTP/JSON demos have migrated to the checked-in v1 `CAPEnvelope` schema artifacts.
2. The CAP v1 layer is the migration target. Its authoring source is LinkML under `schemas/`, and its checked-in JSON Schema validation artifacts and examples live under `schemas/cap-core/v1/` and `examples/cap-core/v1/`.

The repository therefore contains v1 schema scaffolding and selected migrated hot paths, but the main runtime has not fully migrated to the complete v1 architecture. Do not read the presence of a v1 schema file or one migrated demo path as evidence of production-ready v1 runtime implementation.

## v1 Schema Reading Path

Read the v1 schema artifacts in this order:

1. `schemas/cap.yaml` is the umbrella LinkML schema. It imports the shared core schema and each domain module.
2. `schemas/core.yaml` defines shared LinkML types, reusable classes, and enums: `ReversibilityEnum`, `CapabilityKindEnum`, `DirectiveTypeEnum`, `GuardDecisionEnum`, `InterruptActionEnum`, `MessageKindEnum`, `ExecutionStatusEnum`, `RefusalReasonEnum`, and `ConfidentialityLabelEnum`.
3. `schemas/domains/*.yaml` defines the target object model by domain.
4. `schemas/cap-core/v1/*.schema.json` contains the reviewed JSON Schema artifacts used by tests for concrete validation.
5. `examples/cap-core/v1/*.json` contains minimal examples for the v1 artifacts.

The LinkML layout is the authoring layout. The checked-in JSON Schema files are the executable validation artifacts until automated generation is deterministic and reviewed enough to replace them in the runtime validation path.

The v1 `PrivacyBoundary` dimensional model is nine first-class dimensions: classification, movement, transformation, retention, logging, audit visibility, allowed recipients, raw-data egress, and minimization. `boundary_id` is the identifier and `policy_refs` is supporting metadata. Recipients, raw-egress, and minimization are not optional refinements in the v1 schema; they are required first-class dimensions, with CAP-Med raw transcript and raw audio egress represented as explicit booleans.

## v1 Domain Map

| Domain | LinkML file | v1 objects |
|---|---|---|
| Umbrella | `schemas/cap.yaml` | `CAPSchemaBundle` container for grouped v1 objects. |
| Shared core | `schemas/core.yaml` | shared types, signature metadata, profile extension map, and v1 enums. |
| Control | `schemas/domains/control.yaml` | `CAPEnvelope`, `Directive`, `GuardDecision`, `InterruptDecision`, `RefusalMessage`, `ExecutionReport`, and `DirectiveAction`. |
| Authority | `schemas/domains/authority.yaml` | `PolicyRef`, `AuthorityChain`, `AuthorityChainStep`. |
| Evidence | `schemas/domains/evidence.yaml` | `EvidenceRef`. |
| Privacy | `schemas/domains/privacy.yaml` | `PrivacyBoundary`, `RawDataEgressPolicy`, `MinimizationPolicy`. |
| Capability | `schemas/domains/capability.yaml` | unified `Capability` for agents, tools, services, humans, and policy subjects. |
| Constraints | `schemas/domains/constraints.yaml` | `OperationalConstraints`. |
| Profiles | `schemas/domains/profiles.yaml` | `TherapistSupervisorScenario` and `SoftwareEngineeringAgentProfile`, profile/scenario contracts and not CAP Core. |

## v1 JSON Schema And Example Map

| v1 object | JSON Schema artifact | Example |
|---|---|---|
| `CAPEnvelope` | `schemas/cap-core/v1/cap-envelope.schema.json` | `examples/cap-core/v1/cap-envelope.json` |
| `Directive` | `schemas/cap-core/v1/directive.schema.json` | `examples/cap-core/v1/directive.json` |
| `GuardDecision` | `schemas/cap-core/v1/guard-decision.schema.json` | `examples/cap-core/v1/guard-decision.json` |
| `InterruptDecision` | `schemas/cap-core/v1/interrupt-decision.schema.json` | `examples/cap-core/v1/interrupt-decision.json` |
| `RefusalMessage` | `schemas/cap-core/v1/refusal-message.schema.json` | `examples/cap-core/v1/refusal-message.json` |
| `ExecutionReport` | `schemas/cap-core/v1/execution-report.schema.json` | `examples/cap-core/v1/execution-report.json` |
| `EvidenceRef` | `schemas/cap-core/v1/evidence-ref.schema.json` | `examples/cap-core/v1/evidence-ref.json` |
| `AuthorityChain` | `schemas/cap-core/v1/authority-chain.schema.json` | `examples/cap-core/v1/authority-chain.json` |
| `PolicyRef` | `schemas/cap-core/v1/policy-ref.schema.json` | `examples/cap-core/v1/policy-ref.json` |
| `PrivacyBoundary` | `schemas/cap-core/v1/privacy-boundary.schema.json` | `examples/cap-core/v1/privacy-boundary.json` |
| `Capability` | `schemas/cap-core/v1/capability.schema.json` | `examples/cap-core/v1/capability.json`, `examples/cap-core/v1/capability-tool.json`, `examples/cap-core/v1/capability-service.json`, `examples/cap-core/v1/capability-human.json`, `examples/cap-core/v1/capability-policy.json` |
| `OperationalConstraints` | `schemas/cap-core/v1/operational-constraints.schema.json` | `examples/cap-core/v1/operational-constraints.json` |

## v0.1 Compatibility Notes

The v0.1 schemas remain part of this package because they describe retained compatibility fixtures and legacy helper modules:

- `schemas/cap-core/v0.1/cap-message.schema.json` is the executable v0.1 envelope shape. CAP v1 uses `CAPEnvelope` with `envelope_id`, `trace_id`, `message_kind`, exactly one of `payload` or `payload_ref`, required `authority_chain_ref`, `privacy_boundary_ref`, `ttl_ms`, and signature metadata.
- v0.1 message kinds are `Directive`, `GuardDecision`, `RefusalMessage`, `ExecutionReport`, and `DecisionRecord`. CAP v1 keeps the operational objects and adds target `CAPEnvelope`, `InterruptDecision`, `PrivacyBoundary`, `Capability`, and `OperationalConstraints`. `DecisionRecord` remains a v0.1 compatibility object and must not contain hidden chain-of-thought.
- v0.1 `ConstraintSet` remains intentionally broad for demo compatibility. CAP v1 splits generic limits into `OperationalConstraints` and keeps profile-specific requirements, such as non-diagnostic style and human confirmation requirements, under `profile_constraints` or `profile_extensions`.
- v0.1 `ConstraintSet.requires_human_confirmation` is compatibility-only. CAP v1 Core `OperationalConstraints` MUST NOT use `requires_human_confirmation` as a top-level field; use a namespaced `profile_constraints` entry for profile-specific confirmation obligations, or a `GuardDecision.require_human_review` workflow when a policy decision blocks execution pending review.
- v0.1 authority material is represented as `AuthorityChainStep` arrays inside payloads. CAP v1 models `AuthorityChain` as an ordered chain with identity binding, capability, scope, policy, expiry, revocation metadata, delegation constraints, and signature metadata.
- v0.1 profile namespaces such as `cap-med/v0.1` remain valid for retained compatibility fixtures. CAP v1 CAP-Med runtime-profile examples use `cap-med/v1` extension keys where the profile/scenario is part of the target model.

## Validation And Drift Checks

The v1 JSON Schema examples are validated in `tests/test_cap_v1_schemas.py`. The LinkML authoring schemas load and are compared to the checked-in JSON Schema artifacts in `tests/test_cap_v1_linkml.py`.

The command `python scripts/check_v1_schema_drift.py` compares essential field names, required fields, enum values, simple cardinalities, and numeric minima between the LinkML authoring schemas and the checked-in v1 JSON Schema artifacts. The same check is exposed as `cap-check-v1-schema-drift` after editable installation.

The schemas are not a replacement for conformance tests. Implementations MUST still enforce lifecycle, policy, evidence, privacy-boundary, interruption, refusal, authority-chain, and observability semantics.

## v0.1 Inline Schema Skeletons

The following JSON Schema Draft 2020-12 snippets document the current v0.1-candidate message skeletons. They are kept inline for historical compatibility and quick review; prefer the standalone files under `schemas/cap-core/v0.1/` and `schemas/cap-core/v1/` for executable validation.

Core schemas use `additionalProperties: false` where the v0.1 object is closed. Extension data belongs in `profile_extensions`, whose keys are profile namespaces such as `cap-med/v1` for CAP-Med v1 or `cap-med/v0.1` for retained compatibility fixtures.

## common

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://cap.example/schemas/v0.1/common.json",
  "$defs": {
    "Timestamp": {
      "type": "string",
      "format": "date-time"
    },
    "URI": {
      "type": "string",
      "format": "uri"
    },
    "Identifier": {
      "type": "string",
      "minLength": 1,
      "maxLength": 256
    },
    "Hash": {
      "type": "string",
      "pattern": "^sha256:[a-fA-F0-9]{64}$"
    },
    "AttestationRef": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "kind": {
          "type": "string",
          "enum": [
            "dsse",
            "cose",
            "jose",
            "in_toto",
            "slsa",
            "sigstore",
            "other"
          ]
        },
        "uri": {
          "type": "string"
        },
        "digest": {
          "type": "string"
        },
        "embedded": {
          "type": "object"
        }
      },
      "required": [
        "kind"
      ]
    },
    "TraceContext": {
      "type": "object",
      "additionalProperties": false,
      "properties": {
        "traceparent": {
          "type": "string"
        },
        "tracestate": {
          "type": "string"
        }
      }
    },
    "ProfileExtensions": {
      "type": "object",
      "additionalProperties": {
        "type": "object"
      },
      "propertyNames": {
        "pattern": "^[a-z0-9][a-z0-9_.-]*/v[0-9]+(\\.[0-9]+)?$"
      }
    }
  }
}
```

## Envelope

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://cap.example/schemas/v0.1/Envelope.json",
  "title": "CAP Envelope v0.1",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "cap_version",
    "message_id",
    "message_type",
    "created_at",
    "sender_id",
    "payload"
  ],
  "properties": {
    "cap_version": {
      "const": "0.1"
    },
    "message_id": {
      "type": "string"
    },
    "message_type": {
      "type": "string",
      "enum": [
        "Directive",
        "GuardDecision",
        "RefusalMessage",
        "ExecutionReport",
        "DecisionRecord"
      ]
    },
    "session_id": {
      "type": "string"
    },
    "task_id": {
      "type": "string"
    },
    "correlation_id": {
      "type": "string"
    },
    "created_at": {
      "$ref": "common.json#/$defs/Timestamp"
    },
    "expiry": {
      "$ref": "common.json#/$defs/Timestamp"
    },
    "sender_id": {
      "type": "string"
    },
    "receiver_id": {
      "type": "string"
    },
    "sender_capability": {
      "type": "string"
    },
    "receiver_capability": {
      "type": "string"
    },
    "payload": {
      "type": "object"
    },
    "attestation_ref": {
      "$ref": "common.json#/$defs/AttestationRef"
    },
    "trace_context": {
      "$ref": "common.json#/$defs/TraceContext"
    },
    "profile_extensions": {
      "$ref": "common.json#/$defs/ProfileExtensions"
    }
  },
  "allOf": [
    {
      "if": {
        "properties": {
          "message_type": {
            "const": "Directive"
          }
        }
      },
      "then": {
        "properties": {
          "payload": {
            "$ref": "https://cap.example/schemas/v0.1/Directive.json"
          }
        },
        "required": [
          "expiry"
        ]
      }
    },
    {
      "if": {
        "properties": {
          "message_type": {
            "const": "GuardDecision"
          }
        }
      },
      "then": {
        "properties": {
          "payload": {
            "$ref": "https://cap.example/schemas/v0.1/GuardDecision.json"
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "message_type": {
            "const": "RefusalMessage"
          }
        }
      },
      "then": {
        "properties": {
          "payload": {
            "$ref": "https://cap.example/schemas/v0.1/RefusalMessage.json"
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "message_type": {
            "const": "ExecutionReport"
          }
        }
      },
      "then": {
        "properties": {
          "payload": {
            "$ref": "https://cap.example/schemas/v0.1/ExecutionReport.json"
          }
        }
      }
    },
    {
      "if": {
        "properties": {
          "message_type": {
            "const": "DecisionRecord"
          }
        }
      },
      "then": {
        "properties": {
          "payload": {
            "$ref": "https://cap.example/schemas/v0.1/DecisionRecord.json"
          }
        }
      }
    }
  ]
}
```

## Directive

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://cap.example/schemas/v0.1/Directive.json",
  "title": "CAP Directive v0.1",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "directive_id",
    "directive_type",
    "action",
    "constraints",
    "authority_chain",
    "policy_refs",
    "expiry",
    "reversibility"
  ],
  "properties": {
    "directive_id": {
      "type": "string"
    },
    "directive_type": {
      "type": "string",
      "enum": [
        "execute",
        "observe",
        "compensate",
        "wait"
      ]
    },
    "action": {
      "type": "object",
      "additionalProperties": false,
      "required": [
        "kind",
        "target"
      ],
      "properties": {
        "kind": {
          "type": "string",
          "enum": [
            "mcp_tool",
            "a2a_task",
            "http_operation",
            "robot_actuation",
            "ui_render",
            "profile_defined"
          ]
        },
        "target": {
          "type": "string"
        },
        "operation": {
          "type": "string"
        },
        "arguments_ref": {
          "type": "string"
        },
        "profile_extensions": {
          "$ref": "common.json#/$defs/ProfileExtensions"
        }
      }
    },
    "constraints": {
      "$ref": "https://cap.example/schemas/v0.1/ConstraintSet.json"
    },
    "authority_chain": {
      "type": "array",
      "items": {
        "$ref": "https://cap.example/schemas/v0.1/AuthorityChainStep.json"
      },
      "minItems": 1
    },
    "evidence_required": {
      "type": "array",
      "items": {
        "$ref": "https://cap.example/schemas/v0.1/EvidenceRef.json"
      }
    },
    "policy_refs": {
      "type": "array",
      "items": {
        "$ref": "https://cap.example/schemas/v0.1/PolicyRef.json"
      },
      "minItems": 1
    },
    "expiry": {
      "$ref": "common.json#/$defs/Timestamp"
    },
    "reversibility": {
      "type": "string",
      "enum": [
        "reversible",
        "partial",
        "irreversible"
      ]
    },
    "side_effect_expectations": {
      "type": "array",
      "items": {
        "$ref": "https://cap.example/schemas/v0.1/SideEffect.json"
      }
    },
    "compensation_hint": {
      "type": "string"
    },
    "idempotency_key": {
      "type": "string"
    },
    "expected_report_schema": {
      "type": [
        "object",
        "string"
      ]
    },
    "profile_extensions": {
      "$ref": "common.json#/$defs/ProfileExtensions"
    }
  }
}
```

## GuardDecision

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://cap.example/schemas/v0.1/GuardDecision.json",
  "title": "CAP GuardDecision v0.1",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "decision_id",
    "guarded_message_id",
    "guard_identity",
    "guard_capability",
    "decision",
    "policy_refs",
    "expires_at"
  ],
  "properties": {
    "decision_id": {
      "type": "string"
    },
    "guarded_message_id": {
      "type": "string"
    },
    "guard_identity": {
      "type": "string"
    },
    "guard_capability": {
      "type": "string"
    },
    "decision": {
      "type": "string",
      "enum": [
        "allow",
        "deny",
        "allow_with_constraints",
        "require_more_evidence",
        "require_human_review",
        "require_policy_update",
        "advisory_warning"
      ]
    },
    "severity": {
      "type": "string",
      "enum": [
        "block",
        "warn",
        "audit"
      ]
    },
    "policy_refs": {
      "type": "array",
      "items": {
        "$ref": "https://cap.example/schemas/v0.1/PolicyRef.json"
      },
      "minItems": 1
    },
    "constraints_added": {
      "$ref": "https://cap.example/schemas/v0.1/ConstraintSet.json"
    },
    "evidence_required": {
      "type": "array",
      "items": {
        "$ref": "https://cap.example/schemas/v0.1/EvidenceRef.json"
      }
    },
    "expires_at": {
      "$ref": "common.json#/$defs/Timestamp"
    },
    "override_policy_ref": {
      "$ref": "https://cap.example/schemas/v0.1/PolicyRef.json"
    },
    "resolution_strategy": {
      "type": [
        "string",
        "object"
      ]
    },
    "attestation_ref": {
      "$ref": "common.json#/$defs/AttestationRef"
    },
    "profile_extensions": {
      "$ref": "common.json#/$defs/ProfileExtensions"
    }
  }
}
```

## RefusalMessage

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://cap.example/schemas/v0.1/RefusalMessage.json",
  "title": "CAP RefusalMessage v0.1",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "refusal_id",
    "refused_message_id",
    "refused_by",
    "reason_code",
    "reason_detail",
    "retryable"
  ],
  "properties": {
    "refusal_id": {
      "type": "string"
    },
    "refused_message_id": {
      "type": "string"
    },
    "refused_by": {
      "type": "string"
    },
    "reason_code": {
      "type": "string",
      "enum": [
        "unauthorized",
        "expired",
        "missing_evidence",
        "forbidden_tool",
        "policy_denied",
        "safety_denied",
        "privacy_denied",
        "unsupported_action",
        "insufficient_capability",
        "resource_exhausted",
        "invalid_signature",
        "stale_policy",
        "stale_evidence",
        "evidence_access_denied",
        "evidence_hash_mismatch",
        "action_no_longer_reversible",
        "conflicting_guards"
      ]
    },
    "reason_detail": {
      "type": "string",
      "maxLength": 4096
    },
    "safe_alternatives": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "remediation_options": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "retryable": {
      "type": "boolean"
    },
    "required_policy_or_evidence": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "trace_ref": {
      "type": "string"
    },
    "profile_extensions": {
      "$ref": "common.json#/$defs/ProfileExtensions"
    }
  }
}
```

## ExecutionReport

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://cap.example/schemas/v0.1/ExecutionReport.json",
  "title": "CAP ExecutionReport v0.1",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "report_id",
    "directive_id",
    "status",
    "completed_at"
  ],
  "properties": {
    "report_id": {
      "type": "string"
    },
    "directive_id": {
      "type": "string"
    },
    "status": {
      "type": "string",
      "enum": [
        "succeeded",
        "partially_succeeded",
        "failed",
        "aborted",
        "compensated"
      ]
    },
    "completed_at": {
      "$ref": "common.json#/$defs/Timestamp"
    },
    "observations": {
      "type": "array",
      "items": {
        "type": "object"
      }
    },
    "evidence_produced": {
      "type": "array",
      "items": {
        "$ref": "https://cap.example/schemas/v0.1/EvidenceRef.json"
      }
    },
    "side_effects": {
      "type": "array",
      "items": {
        "$ref": "https://cap.example/schemas/v0.1/SideEffect.json"
      }
    },
    "metrics": {
      "type": "object"
    },
    "errors": {
      "type": "array",
      "items": {
        "type": "object"
      }
    },
    "tool_result_refs": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "compensation_status": {
      "type": "object"
    },
    "policy_decision_refs": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "trace_ref": {
      "type": "string"
    },
    "profile_extensions": {
      "$ref": "common.json#/$defs/ProfileExtensions"
    }
  }
}
```

## DecisionRecord

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://cap.example/schemas/v0.1/DecisionRecord.json",
  "title": "CAP DecisionRecord v0.1",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "decision_id",
    "decision_question",
    "selected_option",
    "created_at",
    "decider_id",
    "non_cot_rationale_summary"
  ],
  "properties": {
    "decision_id": {
      "type": "string"
    },
    "decision_question": {
      "type": "string",
      "maxLength": 2048
    },
    "selected_option": {
      "type": "string"
    },
    "alternatives_considered": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "evidence_used": {
      "type": "array",
      "items": {
        "$ref": "https://cap.example/schemas/v0.1/EvidenceRef.json"
      }
    },
    "policy_refs": {
      "type": "array",
      "items": {
        "$ref": "https://cap.example/schemas/v0.1/PolicyRef.json"
      }
    },
    "uncertainty_summary": {
      "type": "string",
      "maxLength": 2048
    },
    "known_limitations": {
      "type": "array",
      "items": {
        "type": "string"
      }
    },
    "non_cot_rationale_summary": {
      "type": "string",
      "maxLength": 2048
    },
    "created_at": {
      "$ref": "common.json#/$defs/Timestamp"
    },
    "decider_id": {
      "type": "string"
    },
    "trace_ref": {
      "type": "string"
    },
    "profile_extensions": {
      "$ref": "common.json#/$defs/ProfileExtensions"
    }
  }
}
```

## EvidenceRef

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://cap.example/schemas/v0.1/EvidenceRef.json",
  "title": "CAP EvidenceRef v0.1",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "uri",
    "hash",
    "media_type",
    "producer_identity"
  ],
  "properties": {
    "uri": {
      "type": "string"
    },
    "hash": {
      "$ref": "common.json#/$defs/Hash"
    },
    "media_type": {
      "type": "string",
      "minLength": 1
    },
    "size_bytes": {
      "type": "integer",
      "minimum": 0
    },
    "created_at": {
      "$ref": "common.json#/$defs/Timestamp"
    },
    "expires_at": {
      "$ref": "common.json#/$defs/Timestamp"
    },
    "freshness_policy": {
      "type": "string"
    },
    "producer_identity": {
      "type": "string"
    },
    "confidentiality_label": {
      "type": "string",
      "enum": [
        "public",
        "internal",
        "confidential",
        "restricted",
        "secret"
      ]
    },
    "access_policy_ref": {
      "$ref": "https://cap.example/schemas/v0.1/PolicyRef.json"
    },
    "redaction_ref": {
      "type": "string"
    },
    "provenance_ref": {
      "type": "string"
    },
    "attestation_ref": {
      "$ref": "common.json#/$defs/AttestationRef"
    },
    "profile_extensions": {
      "$ref": "common.json#/$defs/ProfileExtensions"
    }
  }
}
```

## PolicyRef

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://cap.example/schemas/v0.1/PolicyRef.json",
  "title": "CAP PolicyRef v0.1",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "policy_id",
    "engine",
    "version"
  ],
  "properties": {
    "policy_id": {
      "type": "string"
    },
    "engine": {
      "type": "string",
      "enum": [
        "opa",
        "cedar",
        "custom",
        "manual",
        "workflow"
      ]
    },
    "version": {
      "type": "string"
    },
    "digest": {
      "type": "string"
    },
    "uri": {
      "type": "string"
    },
    "entrypoint": {
      "type": "string"
    },
    "evaluated_at": {
      "$ref": "common.json#/$defs/Timestamp"
    },
    "decision_ref": {
      "type": "string"
    },
    "profile_extensions": {
      "$ref": "common.json#/$defs/ProfileExtensions"
    }
  }
}
```

## AuthorityChainStep

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://cap.example/schemas/v0.1/AuthorityChainStep.json",
  "title": "CAP AuthorityChainStep v0.1",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "agent_id",
    "capability_claim",
    "authority_scope",
    "approved_at",
    "expires_at",
    "trust_domain"
  ],
  "properties": {
    "agent_id": {
      "type": "string"
    },
    "capability_claim": {
      "type": "string"
    },
    "authority_scope": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "minItems": 1
    },
    "approved_at": {
      "$ref": "common.json#/$defs/Timestamp"
    },
    "expires_at": {
      "$ref": "common.json#/$defs/Timestamp"
    },
    "trust_domain": {
      "type": "string"
    },
    "policy_ref": {
      "$ref": "https://cap.example/schemas/v0.1/PolicyRef.json"
    },
    "previous_step_hash": {
      "$ref": "common.json#/$defs/Hash"
    },
    "signature_ref": {
      "$ref": "common.json#/$defs/AttestationRef"
    },
    "delegation_constraints": {
      "$ref": "https://cap.example/schemas/v0.1/ConstraintSet.json"
    },
    "revocation_ref": {
      "type": "string"
    },
    "profile_extensions": {
      "$ref": "common.json#/$defs/ProfileExtensions"
    }
  }
}
```

## ConstraintSet

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://cap.example/schemas/v0.1/ConstraintSet.json",
  "title": "CAP ConstraintSet v0.1",
  "type": "object",
  "additionalProperties": false,
  "properties": {
    "allowed_tools": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "uniqueItems": true
    },
    "forbidden_tools": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "uniqueItems": true
    },
    "max_wall_time_ms": {
      "type": "integer",
      "minimum": 1
    },
    "max_tool_calls": {
      "type": "integer",
      "minimum": 0
    },
    "max_cost": {
      "type": "number",
      "minimum": 0
    },
    "scope_tags": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "uniqueItems": true
    },
    "network_egress": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "uniqueItems": true
    },
    "data_access": {
      "type": "array",
      "items": {
        "type": "string"
      },
      "uniqueItems": true
    },
    "requires_human_confirmation": {
      "type": "boolean"
    },
    "profile_extensions": {
      "$ref": "common.json#/$defs/ProfileExtensions"
    }
  }
}
```

## SideEffect

```json
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://cap.example/schemas/v0.1/SideEffect.json",
  "title": "CAP SideEffect v0.1",
  "type": "object",
  "additionalProperties": false,
  "required": [
    "resource_uri",
    "mutation_type",
    "occurred_at",
    "reversibility"
  ],
  "properties": {
    "resource_uri": {
      "type": "string"
    },
    "mutation_type": {
      "type": "string",
      "enum": [
        "read",
        "write",
        "delete",
        "send_message",
        "actuate",
        "external_state_change",
        "other"
      ]
    },
    "occurred_at": {
      "$ref": "common.json#/$defs/Timestamp"
    },
    "reversibility": {
      "type": "string",
      "enum": [
        "reversible",
        "partial",
        "irreversible"
      ]
    },
    "reversible_until": {
      "$ref": "common.json#/$defs/Timestamp"
    },
    "compensation_hint": {
      "type": "string"
    },
    "compensation_action_ref": {
      "type": "string"
    },
    "attestation_ref": {
      "$ref": "common.json#/$defs/AttestationRef"
    },
    "profile_extensions": {
      "$ref": "common.json#/$defs/ProfileExtensions"
    }
  }
}
```
