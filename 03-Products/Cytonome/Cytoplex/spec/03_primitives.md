> **Status**: Active
> **Date**: 2026-06-14
> **Author**: @mohammadi
> **Audience**: engineers
> **Tags**: `cap`, `cytoplex`, `spec`

# CAP_03 — Primitives

The current package defines seven shared artifacts: five envelope payload artifacts plus two core structures used by those payloads. CAP v1 keeps the successful subset but expands the target Core object model to support the hybrid supervisory architecture.

Current implemented payload artifacts:

- `Directive`
- `GuardDecision`
- `RefusalMessage`
- `ExecutionReport`
- optional `DecisionRecord`

Current implemented support structures include `EvidenceRef`, `AuthorityChainStep`, `PolicyRef`, `ConstraintSet`, and `SideEffect`.

CAP v1 target Core objects are `CAPEnvelope`, `Directive`, `GuardDecision`, `InterruptDecision`, `RefusalMessage`, `ExecutionReport`, `EvidenceRef`, `AuthorityChain`, `PolicyRef`, `PrivacyBoundary`, `Capability`, and `OperationalConstraints`. `SupervisorDirective`, human-review payloads, psychometric strategy fields, and domain-specific constraints belong in profiles, not Core.

These primitives flow across different parts of the hybrid architecture. `CAPEnvelope`, `Directive`, `GuardDecision`, `InterruptDecision`, `RefusalMessage`, and `ExecutionReport` are control-plane objects used by Local PEPs, Edge PEPs, Controllers, Supervisor Gateways, PDP adapters, and Executors. `EvidenceRef`, `AuthorityChain`, `PolicyRef`, `PrivacyBoundary`, `Capability`, and `OperationalConstraints` bind those control messages to federated registries, policy decisions, and local enforcement. Observability-plane outputs are derived from these primitives as signed audit records, OpenTelemetry telemetry, and W3C PROV graphs; they are not separate CAP Core transports or workflow records.

## 1. Directive

A `Directive` is a scoped authorization request from a Controller to an Executor.

### Required fields

| Field | Type | Semantics |
|---|---|---|
| `directive_id` | string | Unique Directive identifier. |
| `directive_type` | enum | `execute`, `observe`, `compensate`, or `wait`. |
| `action` | object | The target operation reference. Does not define tool schema. |
| `constraints` | `ConstraintSet` | Operational bounds. |
| `authority_chain` | `AuthorityChainStep[]` | Authority steps supporting the Directive. |
| `policy_refs` | `PolicyRef[]` | Policies that govern the Directive. |
| `expiry` | timestamp | Time after which the Directive MUST NOT be acted on. |
| `reversibility` | enum | `reversible`, `partial`, or `irreversible`. |

### Recommended fields

| Field | Type | Semantics |
|---|---|---|
| `evidence_required` | `EvidenceRef[]` | Evidence required before dispatch/execution. |
| `side_effect_expectations` | `SideEffect[]` | Expected external mutations. |
| `compensation_hint` | string/object | Suggested rollback/compensation instruction. |
| `idempotency_key` | string | Duplicate delivery protection. |
| `expected_report_schema` | object/string | Schema URI or embedded schema for ExecutionReport validation. |

### Action object

CAP does not define tool schemas. `action` references external capabilities:

```json
{
  "kind": "mcp_tool",
  "target": "mcp://github/tools/read_issue",
  "operation": "tools/call",
  "arguments_ref": "cas://sha256/9b..."
}
```

Other `kind` values MAY include `a2a_task`, `http_operation`, `robot_actuation`, `ui_render`, or profile-defined namespaces.

## 2. GuardDecision

A `GuardDecision` is the CAP representation of a policy/safety/privacy/compliance decision.

### Required fields

| Field | Type | Semantics |
|---|---|---|
| `decision_id` | string | Unique decision id. |
| `guarded_message_id` | string | Message or Directive being evaluated. |
| `guard_identity` | string | Guard workload/agent identity. |
| `guard_capability` | string | Capability claim used by the Guard. |
| `decision` | enum | See below. |
| `policy_refs` | `PolicyRef[]` | Policies evaluated. |
| `expires_at` | timestamp | Decision validity window. |

### Supported decisions

| Decision | Blocking? | Meaning |
|---|---:|---|
| `allow` | no | Directive may proceed under original constraints. |
| `deny` | yes | Directive MUST NOT dispatch or execute. |
| `allow_with_constraints` | no, if merge succeeds | Directive may proceed only under stricter constraints. |
| `require_more_evidence` | yes | Controller must provide additional evidence. |
| `require_human_review` | yes | External workflow must produce authority/policy decision. |
| `require_policy_update` | yes | Policy reference is stale, missing, or insufficient. |
| `advisory_warning` | no | Warning must be recorded; does not block by itself. |

CAP v1 keeps `GuardDecision` as a policy-evaluation result and adds a distinct `InterruptDecision` for runtime control of an envelope or stream. This avoids overloading `GuardDecision` with both policy conclusion and streaming action semantics.

### Additional fields

| Field | Type | Semantics |
|---|---|---|
| `severity` | enum | `block`, `warn`, `audit`. |
| `constraints_added` | `ConstraintSet` | Additional narrowing constraints. |
| `evidence_required` | `EvidenceRef[]` | Required missing evidence. |
| `override_policy_ref` | `PolicyRef` | Policy defining who/what may override. |
| `resolution_strategy` | string/object | Profile-defined conflict resolution. |
| `attestation_ref` | object | DSSE/COSE/JOSE/in-toto reference. |

### Guard conflict rules

- `deny` overrides `allow`.
- `allow_with_constraints` narrows `allow`.
- `require_human_review` blocks until external workflow returns a valid authority or policy decision.
- `advisory_warning` does not block but MUST be emitted as telemetry.
- Expired Guard decisions MUST NOT authorize execution.
- If multiple Guards conflict and no valid resolution strategy exists, the Directive MUST be safely denied.

## 3. RefusalMessage

A `RefusalMessage` is emitted when an Executor structurally rejects a Directive or message.

### Required fields

| Field | Type | Semantics |
|---|---|---|
| `refusal_id` | string | Unique refusal id. |
| `refused_message_id` | string | Message being refused. |
| `refused_by` | string | Executor identity. |
| `reason_code` | enum | Machine-actionable refusal reason. |
| `reason_detail` | string | Safe diagnostic detail. |
| `retryable` | boolean | Whether retry may succeed after remediation. |

### Reason codes

| Code | Meaning |
|---|---|
| `unauthorized` | Missing/invalid authority. |
| `expired` | Directive or GuardDecision expired. |
| `missing_evidence` | Required evidence absent or unresolvable. |
| `forbidden_tool` | Requested tool forbidden by effective constraints. |
| `policy_denied` | Policy denied the action. |
| `safety_denied` | Safety policy denied the action. |
| `privacy_denied` | Privacy policy denied the action. |
| `unsupported_action` | Executor cannot perform requested action type. |
| `insufficient_capability` | Executor lacks required capability. |
| `resource_exhausted` | Budget/time/capacity exhausted. |
| `invalid_signature` | Signature/attestation verification failed. |
| `stale_policy` | Policy reference is stale or no longer accepted. |
| `stale_evidence` | Evidence expired or freshness policy failed. |
| `evidence_access_denied` | Executor is not authorized to read evidence. |
| `evidence_hash_mismatch` | Evidence hash does not match reference. |
| `action_no_longer_reversible` | Required compensation window has closed. |
| `conflicting_guards` | Guard decisions could not be reconciled safely. |

### Optional fields

- `safe_alternatives`: machine-readable alternative actions.
- `remediation_options`: steps needed to make the Directive acceptable.
- `required_policy_or_evidence`: references to missing policy/evidence.
- `trace_ref`: OpenTelemetry trace id.

## 4. ExecutionReport

An `ExecutionReport` records the result of an accepted Directive.

CAP v1 treats `ExecutionReport` as two logical portions: an audit-grade portion that is signed, durable, and content-minimized, and a telemetry-grade portion that can be sampled and optimized for operations. The current schema keeps them in one payload for the v0.1 package.

### Required fields

| Field | Type | Semantics |
|---|---|---|
| `report_id` | string | Unique report id. |
| `directive_id` | string | Exactly one Directive id. |
| `status` | enum | Terminal execution status. |
| `completed_at` | timestamp | Completion time. |

### Status values

- `succeeded`
- `partially_succeeded`
- `failed`
- `aborted`
- `compensated`

### Recommended fields

| Field | Type | Semantics |
|---|---|---|
| `observations` | object[] | Bounded observations; not hidden reasoning. |
| `evidence_produced` | `EvidenceRef[]` | New evidence artifacts. |
| `side_effects` | `SideEffect[]` | External mutations. |
| `metrics` | object | Time/cost/tool-call metrics. |
| `errors` | object[] | Structured errors. |
| `tool_result_refs` | string[] | External tool result references, e.g. MCP results. |
| `compensation_status` | object | Compensation/rollback result. |
| `policy_decision_refs` | string[] | Guard/policy decisions relied upon. |
| `trace_ref` | string | OpenTelemetry trace id. |

## 5. DecisionRecord optional artifact

A `DecisionRecord` is a provenance artifact, not a required hot-path message. It is used to record the safe, structured rationale for a Controller or Guard decision.

A DecisionRecord MUST NOT contain hidden chain-of-thought, raw scratchpad text, or unbounded free-form reasoning.

### Fields

- `decision_id`
- `decision_question`
- `selected_option`
- `alternatives_considered`
- `evidence_used`
- `policy_refs`
- `uncertainty_summary`
- `known_limitations`
- `non_cot_rationale_summary`
- `created_at`
- `decider_id`
- `trace_ref`

## 6. Core data structures

The implementation and schemas treat `EvidenceRef` and `AuthorityChainStep` arrays as core validation targets, not as informal documentation-only fields.

### AuthorityChainStep

Authority is not a role label. It is the conjunction of identity, capability, scope, policy, time, and attestation. CAP v1 grounds this in cryptographic capability warrants: attenuating, holder-bound, offline-verifiable tokens built on primitives such as Biscuit, Tenuo, or Macaroons, with identity binding through SPIFFE SVIDs, X.509, OIDC, or profile-selected equivalents.

`AuthorityChain` required fields:

- `chain_id`
- `warrant_format`
- `steps`

`AuthorityChainStep` required fields:

- `step_id`
- `delegator`
- `delegatee`
- `identity_binding`
- `capability`
- `scope`
- `policy_ref`
- `issued_at`
- `expires_at`
- `revocation_ref`
- `delegation_constraints`
- `signature`

Recommended fields:

- `root_trust_domain` on the chain
- `not_before`
- `previous_step_hash` when ordered chaining is used

The `warrant_format` is profile-selected. CAP Core can carry detached-JWS, DSSE, COSE, JOSE, in-toto, Biscuit, Tenuo, Macaroon, or equivalent warrant metadata, but it does not mandate one primitive. Whatever primitive is selected must bind holder identity, capability, scope, policy, expiry, revocation metadata, delegation constraints, and the signed step payload.

### EvidenceRef

EvidenceRef is a typed, immutable or versioned reference to evidence.

Fields:

- `uri`
- `hash`
- `media_type`
- `size_bytes`
- `created_at`
- `expires_at`
- `freshness_policy`
- `producer_identity`
- `confidentiality_label`
- `access_policy_ref`
- `redaction_ref`
- `provenance_ref`
- `attestation_ref`

CAP v1 adds an explicit target field, `freshness_protocol`, to say how freshness is verified, not only what freshness policy is required.

The reference Evidence Registry stores deterministic content-addressed blobs keyed by `cas://sha256/...`, publishes matching Evidence Registry metadata, attaches reference attestation metadata under `attestation_ref`, stores `expires_at` for the backing blob, and emits a provenance reference suitable for observability-plane projection. Retention GC can delete expired backing content while preserving content-minimized audit/provenance records. Production profiles still need deployment-specific access policy, retention-job operations, and attestation-signing rules.

### PolicyRef

Fields:

- `policy_id`
- `engine`
- `version`
- `digest`
- `uri`
- `entrypoint`
- `evaluated_at`
- `decision_ref`

### Capability

`Capability` is the CAP v1 target metadata object for agents, tools, services, humans, and policy subjects. It is the object a Capability Registry resolves when a PEP, Controller, or Executor needs to determine which operations a subject can perform.

Required fields:

| Field | Semantics |
|---|---|
| `capability_id` | Stable capability record identifier. |
| `kind` | Required discriminator: `agent`, `tool`, `service`, `human`, or `policy`. |
| `subject_id` | Stable identity or URI for the subject. |
| `operations` | Non-empty list of authorized or advertised operations. |

Optional fields:

| Field | Semantics |
|---|---|
| `endpoint` | Local, service, SPIFFE, A2A, MCP, or equivalent reference used to reach the subject. |
| `risk_level` | Risk label interpreted by profiles and policies. |
| `policy_refs` | Policy references governing use, discovery, or delegation. |
| `profile_extensions` | Namespaced metadata owned by integrations or profiles. A2A AgentCard references and MCP server/tool/input-schema metadata belong here rather than as Core peers of `kind` or `operations`. |

CAP Core requires one shape for all capability subjects. It does not define separate top-level `a2a` or `mcp` fields, and it does not redefine external AgentCard, MCP server, MCP tool, or MCP schema objects.

The current runtime registry scaffold enforces that same shape for agent, tool, service, human, and policy-subject registrations. Kind-specific registry views are compatibility adapters only: they normalize legacy `agent_id` or `tool_id` metadata into `Capability` records and preserve non-Core details under `profile_extensions`.

### ConstraintSet

`ConstraintSet` is the v0.1 compatibility shape used by retained legacy HTTP/JSON helpers and legacy gRPC compatibility fixtures. It remains intentionally open in the v0.1 schema so compatibility payloads continue to validate; the active gRPC and HTTP/JSON demos use v1 `OperationalConstraints` inside `Directive.payload.constraints`.

Fields:

- `allowed_tools`
- `forbidden_tools`
- `max_wall_time_ms`
- `max_tool_calls`
- `max_cost`
- `scope_tags`
- `network_egress`
- `data_access`
- `requires_human_confirmation`

CAP v1 splits this into Core `OperationalConstraints` plus profile-specific constraints. Operational constraints cover generic limits such as allowed tools, forbidden tools, maximum wall time, maximum tool calls, cost/budget, data-access scope, reversibility, side-effect limits, network egress, and freshness limits. Profile-specific constraints cover domain rules such as non-diagnostic response style, psychometric scoring, medical thresholds, or escalation thresholds, and belong under `profile_constraints` or the containing object's `profile_extensions`.

The v0.1 `requires_human_confirmation` key is a compatibility field, not a top-level CAP v1 Core `OperationalConstraints` field. In CAP v1, profile-specific human confirmation requirements belong under a namespaced profile constraint such as `profile_constraints.cap-med/v1.requires_human_confirmation`; policy-driven human review is represented by `GuardDecision.require_human_review` and the resulting authority or policy decision.

The v1 `OperationalConstraints` schema is closed to top-level profile-only or legacy fields. For example, `non_diagnostic_required` and `requires_human_confirmation` are valid under `profile_constraints.cap-med/v1`, not as Core constraint peers of `allowed_tools` or `budget`.

### SideEffect

Fields:

- `resource_uri`
- `mutation_type`
- `occurred_at`
- `reversibility`
- `reversible_until`
- `compensation_hint`
- `compensation_action_ref`
- `attestation_ref`

## 7. InterruptDecision target primitive

`InterruptDecision` is a CAP v1 target primitive with a checked-in schema, examples, deterministic runtime composition helpers, and demo binding integration. It controls an active envelope, directive, or stream. The retained v0.1 compatibility helpers still use their legacy guard/refusal shapes; the migrated gRPC and HTTP/JSON demos now emit explicit `InterruptDecision` envelopes for applied runtime control.

Required target fields:

- `interrupt_id`
- `target_envelope_id`
- `target_stream_id` when acting on streaming output
- `action`
- `reason_code`
- `policy_refs`
- `issuer`
- `issued_at`
- `expires_at`
- `payload_directive_ref` when a transform, escalation, or reroute requires follow-up authority
- `signature`

The v1 primitive actions are:

| Action | Semantics |
|---|---|
| `allow` | Proceed unchanged. |
| `deny` | Stop and emit a typed refusal. |
| `transform` | Substitute or rewrite output under an authorized follow-up directive. |
| `constrain` | Proceed only under narrower constraints. |
| `pause` | Hold execution until a bounded resolution event. |
| `escalate` | Transfer the decision to supervisor, human, or peer guard; resolves through `pause`. |
| `reroute` | Emit a new envelope or directive addressed to a different agent or tool. |

Composition is restrictive by default: `deny` wins over `pause`/`escalate`, which wins over `transform`, which wins over `constrain`, which wins over `allow`. Conflicting transforms escalate to a bounded pause. The deterministic runtime helper in `src/cap_protocol/runtime/interrupts.py` implements this order, merges compatible `constrain` decisions by narrowing constraints, and denies contradictory constraint intersections.

Profile-specific behavior maps onto these seven primitives rather than extending the Core action enum. Profile shorthand names may appear in narrative text, policy labels, `reason_code` values, or profile-owned directive templates, but they MUST NOT be serialized as additional `InterruptDecision.action` values. A CAP-Med "downgrade language" or "downgraded language" label is a `transform` with profile-owned replacement content or a payload directive. A "revise output", "revised output", or "revise question" label is a profile `Directive` plus a `transform` or `constrain` decision. A "local fallback" or offline-fallback label is deployment-mode policy, usually expressed as `allow`, `deny`, or `constrain` under cached local policy. Deferred analysis is scheduling or routing behavior represented by `pause`, `escalate`, or `reroute`. Late streaming correction is a correction frame and `ExecutionReport` status linked to the original `InterruptDecision`; it is not an `InterruptDecision.action` value.

The CAP-Med helper API `cap_med_profile_interrupts(...)` maps profile shorthand such as `diagnostic_transform`, `supportive_constraints`, `supervisor_pause`, `safety_escalation`, `reroute_to_human_review`, and `privacy_overreach_deny` onto the seven Core actions. Profile-owned interrupt metadata is carried under `profile_extensions.cap-med/v1`. `compose_cap_med_interrupts(...)` applies the same restrictive composition order for profile-local decisions.

Normative streaming terminology: a `lookahead buffer` is the Local PEP-held portion of an outgoing stream that has not yet reached a user surface; a `sliding lookahead buffer` is a lookahead buffer that releases safe prefixes while retaining a bounded suffix for continued evaluation; `configurable lookahead` means a profile or deployment can set the token, character, or time window, with the CAP v1 target default remaining the smaller of 250 ms of speech-equivalent text or 50 tokens unless a profile overrides it. A `buffered transform` is a `transform` `InterruptDecision` applied while unsafe candidate content is still inside the lookahead buffer, before user-visible delivery. An `abort` stops further delivery or execution of an active stream, envelope, or directive after a `deny` or other blocking decision and must preserve audit/report linkage for any already-started work. A `correction frame` is a safe, linked user-visible correction emitted only after partial emission has already occurred; it references the original stream, partial-emission audit ref, correction audit ref, `InterruptDecision`, provenance ref, and `ExecutionReport`, and it is not an `InterruptDecision.action` value. Correction-frame UI copy must not quote the unsafe original stream text; clients should replace the affected partial region and may annotate it with a short safe notice.

Streaming output is intercepted at the Local PEP before user-visible delivery. If unsafe content is detected inside the lookahead buffer, the Local PEP applies a buffered transform or another pre-display `constrain`, `pause`, `escalate`, or `deny` decision. If unsafe content is detected after partial emission, the Local PEP emits a correction frame instead of treating the event as a pre-display transform. The current reference runtime models chunk-level configurable lookahead, fast regex checks, deterministic semantic slow-path classification for non-regex CAP-Med drift, buffered transform, abort/refusal, correction-frame linkage, a wall-clock `tick()` path, a live pull-based model-stream adapter with deterministic backpressure and abort propagation, CLI/WebSocket-style abort replacement contracts, and CLI/WebSocket-style correction-frame replacement/annotation contracts. Production model-provider rollout, shipping native UI wrappers, organization-selected model-judge rollout, and deployed Interrupt Manager coordination remain v1 runtime migration work.

## 8. PrivacyBoundary target primitive

`PrivacyBoundary` is a CAP v1 target primitive with an initial checked-in schema and examples. It replaces flat privacy labels with a structured policy expression evaluated by the PDP and enforced by the Local PEP or Edge PEP.

The normative CAP v1 model has nine first-class privacy dimensions. `boundary_id` identifies the boundary and `policy_refs` cites policy material; neither is counted as a privacy dimension.

The nine first-class dimensions are:

- classification: what kind of data is being handled;
- movement: where the data may move;
- transformation: which redaction, summarization, or feature extraction is required;
- retention: how long local backing content, references, and audit records may persist;
- logging: whether content, references, hashes, or only structural metadata may be logged;
- audit visibility: which actors may inspect the audit record;
- allowed recipients: which identities may receive transformed or referenced data;
- raw-data egress: explicit `raw_transcript` and `raw_audio` booleans plus any profile-owned exceptions;
- minimization: redaction requirements, evidence-reference substitution, and allowed summary fields.

For the Therapist/Supervisor scenario, raw transcripts and raw audio stay local by default. The central/main Supervisor receives redacted context, evidence references, safety flags, dimension vectors, or policy-allowed local text/voice embeddings unless profile policy explicitly authorizes narrower exceptions. Embedding-only egress is still a minimization transform: source text/audio remain local, while hashes, provenance refs, encoder metadata, aggregate dimensions, and recipient-binding metadata can cross the boundary when the active PrivacyBoundary allows it.

The current runtime maps `PrivacyBoundary.retention.raw_local_ttl_seconds` to `local-evidence://` backing storage and Evidence Registry backing blobs. Expired raw backing content is deleted by retention GC; audit/provenance records are retained separately with hashes, refs, and deletion metadata but without raw content.

The current deterministic runtime scaffold evaluates this structured model through `src/cap_protocol/runtime/privacy_pdp.py`. The evaluator treats Core `OperationalConstraints` as a closed shape, normalizes known profile-only fields such as CAP-Med non-diagnostic and human-confirmation requirements under `profile_constraints`, and returns privacy refusals with the failing boundary dimension such as `raw_data_egress.raw_transcript`, `movement.allowed_cross_boundary`, `allowed_recipients`, or `minimization.allowed_summary_fields`. Local PEP, Edge PEP, and the v1 OPA/Cedar-shaped adapter paths use this helper for privacy decisions. This is still an in-process deterministic PDP scaffold, not a deployed PDP service or Policy Registry integration.
