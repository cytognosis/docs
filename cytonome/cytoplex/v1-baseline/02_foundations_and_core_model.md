# CAP V1 Baseline: Foundations and Core Model

**Generated:** 2026-05-25T06:54:46+00:00
**Document set:** CAP V1 baseline consolidated Markdown set
**Repository status:** V1 architecture documented and V1 runtime scaffold present; current executable package remains `v0.1-production-candidate` and is not a complete stable V1 runtime.
**Purpose:** Problem statement, scope boundaries, roles, envelope model, lifecycle, constraints, and authority checks.

This file is part of `docs/v1_baseline/`, the capped baseline V1 documentation folder. It preserves and consolidates source documentation from the repository. Local links in preserved source sections are rewritten to resolve from this generated baseline file.

## Source Map

- `docs/CAP_01_foundations.md`
- `docs/CAP_02_core_model.md`
## Source: `docs/CAP_01_foundations.md`

## CAP_01 — Foundations

### 1. Problem statement

Modern agent systems have rapidly standardized important boundaries:

- MCP standardizes how a host/client interacts with tools, resources, and prompts.
- A2A standardizes peer-agent discovery, messages, tasks, artifacts, and transport bindings.
- Workflow frameworks provide state machines, durable execution, retries, checkpoints, and human approval tasks.
- Observability stacks provide traces, logs, metrics, and provenance graphs.
- Policy engines provide machine-evaluable authorization and governance decisions.

A gap remains: **runtime supervisory control across the component that decides, the component that acts, the component that enforces local policy, and the infrastructure that records evidence and provenance**.

Without a typed supervisory layer, authority is usually hidden in orchestration code, prompts, or middleware. The Executor often cannot determine whether a request was approved by the right authority, whether required evidence is fresh, whether the request is still valid, or whether a policy decision narrowed the action. Local enforcement points often cannot prove why an output was allowed, transformed, interrupted, or refused. Refusals are often strings or exceptions rather than structured, auditable protocol events.

CAP exists to make this control boundary explicit and portable.

### 2. Core thesis

CAP v1 is a **supervisory control plane and runtime governance protocol**. It defines how Controllers, Supervisors, Guards, PDPs, PEPs, Executors, Observers, and registries compose without replacing the lower-level systems they ride on. CAP owns supervisory semantics: authority, evidence, privacy boundaries, interruption, refusal, execution reporting, audit, and provenance.

The repository implementation is the smaller CAP v0.1 production-candidate subset. It proves the Controller-to-Executor authority boundary and should be treated as implementation evidence, not as the full v1 architecture.

### 2.1 Architecture shape

CAP v1 uses a hybrid **two-tier** architecture:

- **Local tier:** Local PEPs run near agents, tools, local memory, and user surfaces. They enforce hot-path privacy, redaction, typed refusal, offline fallback, and streaming interruption before user-visible output or local-tool access crosses the local boundary.
- **Federated tier:** a decomposed central Control Plane coordinates Controller, Supervisor Gateway, Session Router, logical Interrupt Manager, PDP adapters, and Human Review integration. Edge PEPs enforce CAP envelopes at service, agent, and tool network boundaries. Federated Agent, Tool, Capability, Policy, and Evidence registries distribute metadata and signed bundles without becoming one monolithic Control Plane service.

CAP v1 also separates three **planes**:

- **Data plane:** A2A, MCP, HTTP, gRPC, WebSocket, and local IPC traffic governed by CAP but not owned by CAP.
- **Control plane:** `CAPEnvelope`, `Directive`, `GuardDecision`, `InterruptDecision`, `RefusalMessage`, and `ExecutionReport` traffic used for synchronous authority, interruption, refusal, and reporting semantics.
- **Observability plane:** signed audit records, OpenTelemetry telemetry, and W3C PROV graphs emitted to independent sinks. Observability receives lifecycle facts from CAP components, but it is not the synchronous policy or interruption path.

The current v0.1 Center/Edge demos are simplified demonstrations of the authority boundary. A v1 Controller reference service now separates Controller-owned intent formation/orchestration from Guard/PDP policy evaluation, Session Router delivery, and observability sinks, while the old combined Center remains a legacy compatibility path. This is still not a complete decomposed production Control Plane: full Local PEP trust modes, production model-provider rollout, shipping native UI wrappers around the reference live adapter, organization-selected semantic model-judge rollout, production policy-bundle distribution, production network registry deployment, production observability exporter/collector integration, and live Control Plane service wiring remain tracked in `CAP_v1_TASKS.md`.

CAP Core is deliberately small:

1. A Controller creates a `Directive`.
2. One or more Guards evaluate the Directive and emit `GuardDecision` objects.
3. A Local PEP or Edge PEP enforces the decision at the user, tool, or network boundary.
4. The Directive is dispatched only if the required GuardDecision set permits dispatch.
5. The Executor validates authority, policy, evidence, freshness, capability, and constraints.
6. The enforcement point can allow, deny, transform, constrain, pause, escalate, or reroute through the v1 interrupt semantics.
7. The Executor either emits `RefusalMessage` or executes and emits `ExecutionReport`.
8. Observers map state transitions to signed audit records, OpenTelemetry, and W3C PROV.

CAP gives structure to **authorization and accountability**, not cognition itself.

### 3. CAP guarantees and non-guarantees

#### CAP guarantees, if implemented correctly

- A Directive can be validated against explicit constraints.
- An Executor can refuse with typed, machine-actionable reason codes.
- Guard decisions can block, narrow, or escalate a Directive.
- Evidence and policy references can be attached to the decision boundary.
- Observers can reconstruct the structural lifecycle of an action.
- Hidden chain-of-thought is not required to audit structural behavior.

#### CAP does not guarantee

- The Controller's reasoning is correct.
- The Guard's policy is complete or safe.
- The Executor is honest if fully compromised.
- External tools return correct or non-poisoned data.
- LLM outputs can be replayed bit-for-bit.
- A CAP-conformant system is automatically safe, compliant, or clinically/financially valid.

CAP provides **structural accountability**, not semantic infallibility.

### 4. Relationship to MCP

CAP does not define tool schemas or tool invocation. A CAP `Directive.action` may reference an MCP tool identifier or MCP resource, but the Executor uses MCP to list tools, call tools, access resources, and receive results. CAP constrains **whether and how** the Executor is allowed to use that tool.

CAP adds authority context around MCP calls:

```text
CAP Directive -> Executor authorization boundary -> MCP tools/call -> CAP ExecutionReport
```

### 5. Relationship to A2A

CAP does not define peer-agent discovery, generic delegation, or task lifecycle. A2A Tasks can carry CAP metadata when a delegated task requires Controller-to-Executor authority semantics.

CAP adds semantic restrictions to A2A work units:

```text
A2A Task = durable cross-agent work container
CAP Directive = authority payload inside or referenced by the task
```

### 6. Relationship to policy engines

CAP does not define quorum, weighted voting, safety veto, policy veto, or human-required algorithms in Core. Those are policy decisions.

CAP carries `PolicyRef` and `GuardDecision`; engines such as OPA/Rego or Cedar evaluate policy. A Guard is the CAP-facing adapter that converts a policy decision into a portable CAP object.

### 7. Relationship to observability and provenance

CAP does not define an audit store or custom hash chain. It defines semantic events that can be emitted as OpenTelemetry spans/events and mapped into W3C PROV.

- OpenTelemetry answers operational questions: latency, errors, lifecycle state transitions.
- W3C PROV answers provenance questions: which agents, activities, plans, evidence, and generated entities participated.
- in-toto/DSSE/SLSA/transparency logs answer tamper-evidence and attestation questions.

In CAP v1, audit, telemetry, and provenance are a separate observability plane. They have different latency, retention, integrity, and backpressure properties and should not be folded into the synchronous Control Plane.

### 8. Relationship to workflow frameworks

CAP does not replace LangGraph, Temporal, Microsoft Agent Framework, CrewAI, AutoGen, or Semantic Kernel. Those frameworks own orchestration, retries, local state, human workflow, persistence, and internal graph execution.

CAP messages can be emitted **by** workflow nodes or across framework boundaries when independent components must interoperate.

### 9. Novelty claim

CAP is novel only in its narrow composition:

> A portable supervisory control plane for agentic systems that combines local enforcement, central supervision, cryptographic authority, evidence references, privacy boundaries, streaming interruption, structured refusals, execution reports, and lifecycle observability without replacing existing transports, tool protocols, identity systems, policy engines, or workflow engines.

CAP is not novel as a transport, discovery mechanism, policy engine, audit system, or workflow runtime; those belong outside CAP Core.

### 10. Therapist/Supervisor scenario

The default motivating scenario uses a mobile **Therapist** persona as the local interviewer. This is a profile/scenario label only, not CAP Core and not a clinical authority claim. It does not permit diagnosis, treatment advice, prescription, or claims of clinical validity.

The central/main **Supervisor** provides strategy, higher-order review, and structured directives through a Supervisor Gateway. CAP v1 separates three meanings that older drafts overloaded:

- the Supervisor authority role that may issue or approve directives;
- the Supervisor Gateway service endpoint that validates and mediates supervisor output;
- the model, human, or rule engine used behind that gateway.

The Local PEP can refuse Supervisor directives that violate local policy, privacy, jurisdiction, evidence, non-diagnostic, non-prescriptive, or safety constraints.

### Normative and Informative References

CAP is designed to compose with existing standards rather than replace them. The following references are informative unless a profile explicitly makes one normative:

- Model Context Protocol specification: https://modelcontextprotocol.io/specification/2025-06-18/basic/index
- MCP tools: https://modelcontextprotocol.io/specification/2025-06-18/server/tools
- MCP resources: https://modelcontextprotocol.io/specification/2025-06-18/server/resources
- A2A core specification: https://agent2agent.info/specification/core/
- A2A core concepts: https://agent2agent.info/docs/concepts/
- Open Policy Agent / Rego: https://www.openpolicyagent.org/docs/policy-language
- SPIFFE concepts and SVID: https://spiffe.io/docs/latest/spiffe-about/spiffe-concepts/
- SPIRE concepts: https://spiffe.io/docs/latest/spire-about/spire-concepts/
- OpenTelemetry semantic conventions: https://opentelemetry.io/docs/concepts/semantic-conventions/
- OpenTelemetry trace semantic conventions: https://opentelemetry.io/docs/specs/semconv/general/trace/
- W3C PROV-O Recommendation: https://www.w3.org/TR/prov-o/


### 11. Novelty and paper positioning

CAP's novelty must be stated narrowly. CAP is not novel as a transport, tool-calling mechanism, identity system, audit store, or generic agent-discovery protocol. Those layers are delegated to existing infrastructure.

CAP is novel as a **supervisory control-authority protocol** for agentic systems. Its contribution is the explicit, typed boundary between intent, enforcement, execution, and observation:

- a `Controller` cannot merely prompt an action; it must issue a bounded `Directive`;
- a `Guard` can allow, deny, narrow, or escalate the proposed action;
- a Local PEP or Edge PEP can enforce a policy result before the action crosses a trust boundary;
- an `Executor` must validate authority, evidence, policy, freshness, and constraints before acting;
- an `Executor` can return a typed `RefusalMessage` instead of a free-form error;
- every execution result is connected to evidence, side effects, and provenance.

For Cytognosis/Neuroverse, the domain-specific novelty is stronger: CAP becomes a profile for non-diagnostic psychometric assessment, signed assessment configurations, privacy-preserving edge-to-supervisor handoff, and reproducible phenotype-generation traces. The profile should therefore focus on psychometric session state, non-diagnostic guard policies, evidence minimization, and phenotype provenance rather than communication plumbing.

#### Defensible paper claim

A defensible paper claim is:

> We define and evaluate a Control Authority Protocol for evidence-bound, privacy-preserving, non-diagnostic psychometric agent systems. The protocol composes with MCP for tools, A2A for external agent tasks, OPA/Cedar for policy, and OpenTelemetry/W3C PROV for observability and provenance.

A weak claim to avoid is:

> We introduce a new universal protocol for agent communication.


## Source: `docs/CAP_02_core_model.md`

## CAP_02 — Core Model

### 1. Core roles

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

#### Legacy-role mapping

Older CAP drafts used eleven roles. In v0.1-candidate these become specializations:

| Older role | v0.1-candidate mapping |
|---|---|
| PlannerAgent, ReasonerAgent, CriticAgent | Controller specialization or internal orchestration role. |
| SafetyAgent, PolicyAgent, PrivacyAgent | Guard specialization or external policy decision point. |
| InterfaceAgent, ExecutionAgent | Executor specialization. |
| MemoryAgent | Evidence/memory infrastructure, not a Core role. |
| AuditorAgent | Observer or observability infrastructure. |
| HumanReviewer | External workflow actor; may produce an authority step or policy decision through an application workflow. |

### 2. Envelope

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

#### Placement rules

- Constraints belong in the `Directive.payload.constraints`, not in the envelope.
- Evidence references belong in the payload that uses or produces evidence.
- In v1 `CAPEnvelope`, `policy_refs` are required boundary metadata; payload-specific policy references still belong in objects such as `Directive`, `GuardDecision`, or `ExecutionReport`.
- Authority MUST NOT be inferred from `sender_id` alone. Authority requires identity, capability, scope, policy, freshness, and attestation.

### 3. Lifecycle finite-state machines

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

### 4. Lifecycle invariants

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

### 5. Effective constraint merge

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

### 6. Guard conflict resolution

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

### 7. Authority verification overview

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

### 8. v1 tiers, planes, and enforcement points

CAP v1 has two deployment tiers and three logical planes. The local tier contains Local PEPs near agents, tools, local memory, and user surfaces. The federated tier contains the decomposed Control Plane, Edge PEPs, PDP adapters, Human Review integration, and independently deployable Capability, Policy, and Evidence registries.

The data plane is ordinary A2A, MCP, HTTP, gRPC, WebSocket, and local IPC traffic carrying CAP metadata or payload references. The control plane carries `CAPEnvelope`, `Directive`, `GuardDecision`, `InterruptDecision`, `RefusalMessage`, and `ExecutionReport` objects. The observability plane carries signed audit records, OpenTelemetry telemetry, and W3C PROV graphs to separate sinks; it should not be required for every hot-path policy decision unless a profile explicitly makes audit persistence a precondition.

See `architecture.md#architecture-diagrams` for the visual target topology and the current-vs-target status captions.

### 9. v1 runtime lanes and enforcement points

CAP v1 uses three runtime lanes:

| Lane | Location | Purpose |
|---|---|---|
| Fast lane | Local PEP | Local policy, redaction, evidence-reference substitution, and low-latency output gates. |
| Control lane | Control Plane and Supervisor Gateway | Supervisor consultation, cross-cutting policy, routing, and interrupt coordination. |
| Analysis lane | Async specialists and observability sinks | Non-blocking scoring, trend analysis, telemetry, audit, and provenance export. |

The motivating Therapist/Supervisor scenario is a profile example, not CAP Core. It uses the fast lane for non-diagnostic, non-prescriptive output filtering and local privacy enforcement. Sensitive or uncertain turns can pause into the control lane for central Supervisor review through a Supervisor Gateway. Longer-running specialist analysis stays asynchronous and can constrain future turns rather than blocking the current one. The Local PEP remains the final local veto for Supervisor directives that violate privacy, non-diagnostic, jurisdiction, or safety policy.

### 10. v1 implementation status

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
