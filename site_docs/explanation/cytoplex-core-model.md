# CAP_02 — Core Model

## 1. Core roles

The current v0.1 package implements four functional roles. Roles are semantic responsibilities, not deployment units. A single process MAY implement multiple roles, but every CAP message MUST identify the capability under which it acts.

| Role | Core responsibility | Examples outside Core |
|---|---|---|
| `Controller` | Forms intent and issues `Directive` objects. | Planner, reasoner, supervisor, orchestrator node. |
| `Guard` | Evaluates Directives and emits `GuardDecision` objects. | Safety policy adapter, privacy gate, compliance engine, OPA sidecar. |
| `Executor` | Accepts, refuses, or executes Directives under constraints. | Tool runner, browser actor, robot actor, API caller, UI renderer. |
| `Observer` | Emits telemetry/provenance from CAP lifecycle events. | OTel collector, PROV exporter, audit dashboard. |

CAP v1 keeps these roles but adds explicit deployment and enforcement roles around them:

| v1 role or component | Responsibility |
|---|---|
| `Local PEP` | Enforces hot-path local policy, privacy, refusal, offline fallback, and streaming gates before user-visible output. |
| `Edge PEP` | Enforces CAP envelopes at process, host, service, agent, or tool network boundaries. |
| `Decomposed Control Plane` | Coordinates Controller, Supervisor Gateway, Session Router, logical Interrupt Manager, PDP adapters, and Human Review integration without absorbing registries or observability sinks into one process. |
| `Supervisor Gateway` | Mediates structured supervisor output, validates authority scope, and applies privacy filtering before supervisor consultation. |
| `PDP` | Evaluates OPA, Cedar, or equivalent policy locally and centrally. |
| `Session Router` | Tracks active session participants and routing decisions without owning raw session content. |
| `Federated Registries` | Capability, Policy, and Evidence registries provide independently cacheable metadata and signed bundles; agent, tool, service, human, and policy-subject records use the unified Capability shape. |
| `Observability Plane` | Receives signed audit records, OpenTelemetry telemetry, and W3C PROV independently of synchronous control traffic. |

The Supervisor is not a single CAP component. CAP v1 separates the Supervisor authority role, the Supervisor Gateway endpoint, and the model/human/rule engine behind that endpoint.

`Capability` is the v1 target metadata object for agent, tool, service, human, and policy subjects. It uses one shared structure and a required `kind` discriminator instead of separate Core shapes for agents, tools, services, humans, and policies.

Required v1 `Capability` fields:

| Field | Semantics |
|---|---|
| `capability_id` | Stable identifier for this capability record. |
| `kind` | Subject discriminator: `agent`, `tool`, `service`, `human`, or `policy`. |
| `subject_id` | Stable identity or URI for the subject that holds or exposes the capability. |
| `operations` | Non-empty list of operations this capability authorizes or advertises. |

Optional v1 `Capability` fields:

| Field | Semantics |
|---|---|
| `endpoint` | Transport or local reference used to reach the subject, such as a local URI, SPIFFE URI, MCP URI, or service endpoint. |
| `risk_level` | Profile- or deployment-defined risk label used by policy and registry decisions. |
| `policy_refs` | Policies governing use, discovery, or delegation of the capability. |
| `profile_extensions` | Namespaced integration/profile metadata. A2A AgentCard pointers and MCP server/tool/schema details belong here, not as CAP Core fields. |

Federated Capability Registries resolve these records by `capability_id`, check metadata freshness/version/digest, and authorize requested operations against the `operations` list. Registry entries may cache A2A or MCP metadata in `profile_extensions`, but CAP does not redefine AgentCard, MCP server, MCP tool, or MCP input-schema formats.

The current deterministic Python registry scaffold stores agent, tool, service, human, and policy-subject registrations as the same closed `Capability` metadata shape. `AgentRegistry`, `ToolRegistry`, `ServiceRegistry`, `HumanRegistry`, and `PolicySubjectRegistry` remain compatibility views for callers that want a kind-specific registry, but their stored metadata is normalized to `Capability` with a fixed `kind`; the central `CapabilityRegistry` can resolve and authorize all five subject kinds directly.

### Legacy-role mapping

Older CAP drafts used eleven roles. In v0.1-candidate these become specializations:

| Older role | v0.1-candidate mapping |
|---|---|
| PlannerAgent, ReasonerAgent, CriticAgent | Controller specialization or internal orchestration role. |
| SafetyAgent, PolicyAgent, PrivacyAgent | Guard specialization or external policy decision point. |
| InterfaceAgent, ExecutionAgent | Executor specialization. |
| MemoryAgent | Evidence/memory infrastructure, not a Core role. |
| AuditorAgent | Observer or observability infrastructure. |
| HumanReviewer | External workflow actor; may produce an authority step or policy decision through an application workflow. |

## 2. Envelope

Every CAP object MAY be carried directly or embedded inside another protocol such as A2A. When serialized by the current package, it uses this v0.1 envelope.

| Field | Required | Semantics |
|---|---:|---|
| `cap_version` | yes | CAP profile version, e.g. `0.1`. |
| `message_id` | yes | Globally unique message identifier. ULID or UUID recommended. |
| `message_type` | yes | One of `Directive`, `GuardDecision`, `RefusalMessage`, `ExecutionReport`, `DecisionRecord`. |
| `session_id` | recommended | Stable interaction/session identifier. |
| `task_id` | recommended | Task/work item identifier. MAY map to A2A Task id. |
| `correlation_id` | optional | Cross-message correlation id. |
| `created_at` | yes | RFC 3339 timestamp. |
| `expiry` | conditional | Required for `Directive` and `GuardDecision`; optional otherwise. |
| `sender_id` | yes | Stable agent/workload identity URI. |
| `receiver_id` | optional | Required for unicast; absent for broadcast telemetry. |
| `sender_capability` | recommended | Capability claim under which the sender acts. |
| `receiver_capability` | optional | Expected receiver capability. |
| `payload` | yes | The CAP primitive payload. |
| `attestation_ref` | optional | DSSE/COSE/JOSE/in-toto reference or embedded object. |
| `trace_context` | optional | W3C Trace Context fields. |
| `profile_extensions` | optional | Namespaced profile-specific extension object. |

CAP v1 renames this concept to `CAPEnvelope` and tightens the target verification model. The checked-in v1 LinkML and JSON Schema artifacts define target scaffolding for `CAPEnvelope`; the gRPC reference demo and independent HTTP/JSON demo now use v1 `CAPEnvelope` plus v1 Core payload objects on their active hot paths. The v1 `CAPEnvelope` required fields are:

- `cap_version`, `envelope_id`, `session_id`, `trace_id`, `sender_id`, `receiver_id`, `message_kind`, exactly one of `payload_ref` or `payload`, `authority_chain_ref`, `policy_refs`, `privacy_boundary_ref`, `timestamp`, `ttl_ms`, and `signature`;
- canonicalization before signing, with the current signing decision summarized in `CAP_04_security_trust_evidence.md`;
- sender signature verification before cross-trust-boundary processing;
- privacy-boundary validation before payload dereference or user-visible delivery.

### Placement rules

- Constraints belong in the `Directive.payload.constraints`, not in the envelope.
- Evidence references belong in the payload that uses or produces evidence.
- In v1 `CAPEnvelope`, `policy_refs` are required boundary metadata; payload-specific policy references still belong in objects such as `Directive`, `GuardDecision`, or `ExecutionReport`.
- Authority MUST NOT be inferred from `sender_id` alone. Authority requires identity, capability, scope, policy, freshness, and attestation.

## 3. Lifecycle finite-state machines

CAP v1 now has machine-checkable lifecycle finite-state machines in `cap_protocol.runtime.lifecycle`. The runtime scaffold covers the envelope, directive, interrupt, execution, evidence, audit, and provenance domains; conformance calls the same definitions instead of relying only on prose. The table below is the human-readable Directive projection of that executable model.

A Directive has one lifecycle. Multiple messages may refer to it, but implementations MUST maintain a single effective state per `directive_id`.

| From state | To state | Trigger/event | Actor | Required validation | Terminal |
|---|---|---|---|---|---:|
| `null` | `proposed` | Directive drafted | Controller | Schema valid; expiry in future; idempotency key not conflicting. | no |
| `proposed` | `under_guard_review` | Guard review requested | Controller or runtime | PolicyRef resolvable; evidence refs syntactically valid. | no |
| `under_guard_review` | `approved` | Required GuardDecision set allows dispatch | Guard/runtime | Decisions unexpired; no deny; constraints merge valid. | no |
| `under_guard_review` | `denied` | Any required GuardDecision is `deny`, or conflict cannot be resolved | Guard/runtime | Denial reason recorded. | yes |
| `under_guard_review` | `proposed` | Guard requires more evidence or modification | Controller/runtime | Missing evidence/remediation attached. | no |
| `approved` | `dispatched` | Controller sends to Executor | Controller | Effective constraints and authority chain attached. | no |
| `dispatched` | `accepted` | Executor accepts | Executor | Authority, evidence, policy, capability, expiry, and constraints verified. | no |
| `dispatched` | `refused` | Executor emits RefusalMessage | Executor | Refusal reason maps to closed enum. | yes |
| `accepted` | `executing` | First external action begins | Executor | No expiry; no active deny; idempotency checked. | no |
| `executing` | `succeeded` | Execution completed | Executor | ExecutionReport valid; evidence/side effects recorded. | yes |
| `executing` | `partially_succeeded` | Partial completion | Executor | Report includes incomplete steps and side effects. | yes |
| `executing` | `failed` | Execution failed | Executor | Error object included. | yes |
| `executing` | `aborted` | Execution stopped before completion | Executor/runtime/Guard | Abort reason and side effects recorded. | yes |
| `succeeded` or `partially_succeeded` | `compensated` | Reversal/compensation completed | Executor/runtime | Compensation result recorded. | yes |
| any non-terminal | `expired` | Expiry passes before terminal state | Runtime | Expiry timestamp verified. | yes |

The executable lifecycle domains use these initial and terminal states:

| Domain | Initial state | Terminal states |
|---|---|---|
| `envelope` | `created` | `accepted`, `refused`, `expired` |
| `directive` | `proposed` | `denied`, `refused`, `succeeded`, `partially_succeeded`, `failed`, `aborted`, `compensated`, `expired` |
| `interrupt` | `issued` | `applied`, `superseded`, `refused`, `expired` |
| `execution` | `not_started` | `succeeded`, `partially_succeeded`, `failed`, `aborted`, `compensated` |
| `evidence` | `referenced` | `accepted`, `refused`, `expired` |
| `audit` | `pending` | `replicated`, `retained`, `failed` |
| `provenance` | `pending` | `queryable`, `failed` |

Allowed transitions are explicit. Unknown states, skipped precondition states, and terminal-to-non-terminal resumes fail validation. Compensation is modeled as an explicit terminal-to-terminal transition from `succeeded` or `partially_succeeded` to `compensated`, preserving the invariant that terminal states never resume active execution.

## 4. Lifecycle invariants

A CAP Core implementation MUST enforce these invariants:

1. No external execution without a valid, unexpired `Directive`.
2. No execution when any required, unexpired `GuardDecision` is `deny`.
3. `allow_with_constraints` MUST strictly narrow or preserve Controller constraints. It MUST NOT broaden them.
4. Every `ExecutionReport` MUST reference exactly one `Directive`.
5. Every `RefusalMessage` MUST reference exactly one refused message, normally a `Directive`.
6. Duplicate `Directive` delivery MUST be idempotent or safely refused.
7. A terminal Directive state MUST NOT transition to a non-terminal state.
8. Required evidence MUST be available, authorized, fresh, and hash-valid before execution.
9. A late Guard denial after execution has started MUST abort execution if possible; if not possible, it MUST trigger compensation if compensation is available and policy requires it.
10. Observability events MUST be emitted for all terminal states.

## 5. Effective constraint merge

The retained v0.1 compatibility helpers carry an open `ConstraintSet` object inside `Directive.payload.constraints`. CAP v1 narrows that shape into Core `OperationalConstraints` plus namespaced profile constraints. v0.1 compatibility remains in the v0.1 schemas and fixtures; migrated gRPC and HTTP/JSON hot paths use `OperationalConstraints`.

The Executor acts on the **effective constraints**, computed from:

```text
effective_constraints = intersection(Directive.constraints, all GuardDecision.constraints_added)
```

If two constraints cannot be intersected safely, the result is denial. Examples:

| Constraint type | Merge rule |
|---|---|
| `allowed_tools` | Intersection. |
| `forbidden_tools` | Union. |
| `max_wall_time_ms` | Minimum. |
| `max_tool_calls` | Minimum. |
| `max_cost` | Minimum. |
| `budget` | Minimum. |
| `network_egress` | Intersection/most restrictive. |
| `data_access_scope` | Intersection/most restrictive. |

Profile-specific constraints, such as non-diagnostic style, psychometric scoring, medical thresholds, escalation thresholds, or human confirmation requirements, MUST NOT become top-level Core fields. They belong under `profile_constraints` in an `OperationalConstraints` object or under the containing object's `profile_extensions`. A policy-driven human review block is represented by `GuardDecision.require_human_review`, not by adding `requires_human_confirmation` to Core `OperationalConstraints`.

## 6. Guard conflict resolution

Default conflict behavior is conservative.

| Situation | Default result |
|---|---|
| Any required Guard returns `deny` | Deny. |
| Required GuardDecision expired | Treat as absent; deny or require revalidation. |
| `allow` + `allow_with_constraints` | Allow with narrowed constraints. |
| `require_more_evidence` and no evidence supplied | Return to `proposed`; no dispatch. |
| `require_human_review` | Block until external workflow produces a valid authority or policy decision. |
| Only `advisory_warning` | Does not block, but MUST emit telemetry. |
| Conflicting non-deny decisions without resolution strategy | Deny safely. |

Profiles MAY define more specific conflict-resolution policies, but Core implementations MUST have a safe-deny fallback.

## 7. Authority verification overview

Authority is an explicit warrant chain, not a role label or a trusted `sender_id`. Before execution, the PEP or Executor verifies:

1. The Directive schema is valid.
2. The Directive has not expired.
3. Required Guard decisions are present and valid.
4. The resolved `AuthorityChain` declares its `warrant_format` and every step carries `delegator`, `delegatee`, `identity_binding`, `capability`, `scope`, `policy_ref`, `issued_at`, `expires_at`, `revocation_ref`, `delegation_constraints`, and `signature`.
5. The final delegatee is holder-bound to the sender or actor identity, for example by SPIFFE SVID, X.509, OIDC, DID, or a profile-selected equivalent.
6. Capability and scope cover the requested action/resource/tool.
7. Delegated steps attenuate scope and constraints monotonically.
8. Expiry, not-before, revocation, and policy metadata are acceptable for the decision class.
9. Signatures, DSSE/COSE/JOSE/in-toto attestations, or profile-selected capability warrants verify offline where the active profile requires offline verification.
10. Evidence references are resolvable, authorized, fresh, and hash-valid.
11. Effective constraints allow the requested action.

Failure at any step yields `RefusalMessage`.

## 8. v1 tiers, planes, and enforcement points

CAP v1 has two deployment tiers and three logical planes. The local tier contains Local PEPs near agents, tools, local memory, and user surfaces. The federated tier contains the decomposed Control Plane, Edge PEPs, PDP adapters, Human Review integration, and independently deployable Capability, Policy, and Evidence registries.

The data plane is ordinary A2A, MCP, HTTP, gRPC, WebSocket, and local IPC traffic carrying CAP metadata or payload references. The control plane carries `CAPEnvelope`, `Directive`, `GuardDecision`, `InterruptDecision`, `RefusalMessage`, and `ExecutionReport` objects. The observability plane carries signed audit records, OpenTelemetry telemetry, and W3C PROV graphs to separate sinks; it should not be required for every hot-path policy decision unless a profile explicitly makes audit persistence a precondition.

See `architecture.md#architecture-diagrams` for the visual target topology and the current-vs-target status captions.

## 9. v1 runtime lanes and enforcement points

CAP v1 uses three runtime lanes:

| Lane | Location | Purpose |
|---|---|---|
| Fast lane | Local PEP | Local policy, redaction, evidence-reference substitution, and low-latency output gates. |
| Control lane | Control Plane and Supervisor Gateway | Supervisor consultation, cross-cutting policy, routing, and interrupt coordination. |
| Analysis lane | Async specialists and observability sinks | Non-blocking scoring, trend analysis, telemetry, audit, and provenance export. |

The motivating Therapist/Supervisor scenario is a profile example, not CAP Core. It uses the fast lane for non-diagnostic, non-prescriptive output filtering and local privacy enforcement. Sensitive or uncertain turns can pause into the control lane for central Supervisor review through a Supervisor Gateway. Longer-running specialist analysis stays asynchronous and can constrain future turns rather than blocking the current one. The Local PEP remains the final local veto for Supervisor directives that violate privacy, non-diagnostic, jurisdiction, or safety policy.

## 10. v1 implementation status

Current implementation evidence:

- Controller, Guard, Executor, and Observer flows exist in gRPC and HTTP/JSON bindings, and a v1 `ControllerService` now separates Controller-owned intent formation/orchestration from injected Guard/PDP evaluation, `SessionRouter` delivery, and observability sinks.
- Directives, GuardDecisions, RefusalMessages, ExecutionReports, EvidenceRefs, and AuthorityChainSteps are represented.
- CAP-Med profile constraints demonstrate non-diagnostic and non-prescriptive Therapist/interviewer behavior, raw-transcript minimization, and Local PEP veto of unsafe Supervisor directives. The v1 runtime-profile fixture keeps those rules under `profile_constraints.cap-med/v1` and `profile_extensions.cap-med/v1` while reusing CAP Core objects unchanged.

Open v1 gaps:

- Local PEP and Edge PEP now exist as minimal reusable runtime scaffolds and are wired into selected gRPC/HTTP v1 demo paths; production deployment and trust modes remain open.
- The old gRPC `CAPCenter` still combines Controller, Guard, and Observer as a preserved v0.1 legacy compatibility path; production Controller deployment, production Guard/PDP clients, router discovery, observer pipelines, HA state, and live Control Plane service wiring remain open.
- `CAPEnvelope`, `InterruptDecision`, structured `PrivacyBoundary`, `Capability`, and `OperationalConstraints` now have initial v1 LinkML authoring schemas, JSON Schema artifacts, examples, migrated gRPC/HTTP hot-path coverage, and deterministic in-process privacy PDP evaluation; retained v0.1 helpers still preserve the legacy message shapes for compatibility.
- Streaming transform/correction behavior exists as Local PEP reference scaffolding with configurable lookahead metadata, deterministic semantic slow-path classification, wall-clock release, a pull-based live model-stream adapter for local scripted chunks or optional Ollama chunks, and CLI/WebSocket-style abort replacement contracts. Shipping native UI wrappers, production provider rollout, organization-selected model-judge rollout, and deployed stream control remain open.
- Federated Capability, Policy, and Evidence registries now have deterministic runtime clients plus SQLite-backed reference services. Capability views cover agent, tool, service, human, and policy subjects; agent/tool demo discovery resolves A2A and MCP metadata from service-backed Capability records; Evidence Registry storage can put/get/verify content-addressed blobs with attestation metadata and delete expired backing content while preserving content-minimized audit records. Production network deployment, service authentication, HA replication, scheduled retention operations, and access-policy enforcement remain open.
- Independent observability-plane sink scaffolding now exists for durable/tamper-evident audit, signed audit operations, lossy/sampled telemetry, and queryable W3C PROV-JSONLD lineage; production exporter/collector/PROV-store deployment and v0.1 demo wiring remain migration tasks.
