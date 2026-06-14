> **Status**: Active
> **Date**: 2026-06-14
> **Author**: @mohammadi
> **Audience**: engineers
> **Tags**: `cap`, `cytoplex`, `spec`

# CAP_05 — Integrations

CAP is designed to compose with other systems. This file defines recommended mappings. Unless a profile says otherwise, these mappings are informative, not mandatory.

CAP v1 is transport-independent and framework-independent. It uses the surrounding stack as three planes:

- **Data plane:** A2A, MCP, HTTP, gRPC, WebSocket, and local IPC carry agent, tool, and user traffic governed by CAP enforcement points.
- **Control plane:** CAP-specific `CAPEnvelope`, `Directive`, `GuardDecision`, `InterruptDecision`, `RefusalMessage`, and `ExecutionReport` objects carry synchronous authority, interruption, refusal, and reporting semantics.
- **Observability plane:** signed audit records, OpenTelemetry telemetry, and W3C PROV graphs leave through independent sinks. Integrations must not make telemetry or provenance export part of every hot-path Control Plane decision unless a profile explicitly requires audit persistence before delivery.

The architecture diagrams in `architecture.md#architecture-diagrams` show where these integration planes meet Local PEPs, Edge PEPs, PDPs, registries, and observability sinks.

When an integration carries an `InterruptDecision`, the serialized `action` value MUST be one of `allow`, `deny`, `transform`, `constrain`, `pause`, `escalate`, or `reroute`. Integration or profile labels such as downgraded language, revised output, local fallback, or deferred analysis belong in `reason_code`, `payload_directive_ref`, profile metadata, or test names; they are shorthand for Core-action compositions, not enum extensions.

## CAP v1 Capability Shape For Integrations

CAP v1 uses one `Capability` shape for agents, tools, services, humans, and policy subjects. The required fields are `capability_id`, `kind`, `subject_id`, and a non-empty `operations` list. The optional fields are `endpoint`, `risk_level`, `policy_refs`, and `profile_extensions`.

Integration-specific discovery metadata remains in `profile_extensions`. A2A AgentCard references belong under an A2A-owned extension key, and MCP server/tool/input-schema details belong under an MCP-owned extension key. CAP registries use the Core fields to resolve, cache, version, digest-check, and authorize operations, while preserving extension metadata for the integration that owns it.

The checked-in v1 examples cover all five `kind` values: agent, tool, service, human, and policy. The current deterministic registry scaffold validates the same closed shape and rejects top-level integration metadata such as `a2a` or `mcp`; those keys must sit under `Capability.profile_extensions`.

## 1. CAP over A2A

A2A owns peer-agent discovery, Agent Cards, messages, tasks, artifacts, and transport bindings. CAP metadata MAY be embedded in or referenced from A2A `Task`, `Message`, or `Part` objects.

### Recommended mapping

| A2A concept | CAP mapping |
|---|---|
| AgentCard | Advertise CAP support, supported profiles, capabilities, and required extensions. |
| Task | Durable work container that may carry a CAP Directive. |
| Message | May carry CAP envelope or reference CAP payload. |
| Part | Atomic content part containing CAP JSON or a reference to it. |
| Artifact | May become an EvidenceRef or tool/result reference in ExecutionReport. |
| Task canceled/failed | Map to RefusalMessage or ExecutionReport status depending on lifecycle stage. |

### CAP metadata location

Implementations SHOULD avoid inventing a separate discovery descriptor if an A2A AgentCard is already used. A2A AgentCard extension metadata can advertise:

```json
{
  "cap": {
    "version": "0.1",
    "profiles": ["cap-core"],
    "capabilities": ["cap.directive.accept", "cap.refusal.emit", "cap.guard.evaluate"],
    "supported_message_types": ["Directive", "GuardDecision", "ExecutionReport", "RefusalMessage"]
  }
}
```

When mirrored into CAP v1 metadata, A2A-specific AgentCard pointers belong in `Capability.profile_extensions` rather than as CAP Core `Capability` fields. The Core `Capability` object records the subject kind, operations, endpoint, and policy refs; A2A remains the owner of AgentCard shape, discovery, messages, tasks, artifacts, and transport bindings.

The current reference runtime includes a deterministic live A2A substrate path in `cap_protocol.runtime.substrate_interop`: an A2A transport `Message` carries an `application/cap-envelope+json` part, the enclosed CAPEnvelope wraps the A2A message payload, and the receiver verifies signature, SPIFFE receiver identity, PolicyRef, PrivacyBoundary, and AuthorityChain through Edge PEP before accepting the message. The AgentCard extension advertises CAP v1 support and the required envelope behavior. This is local executable interop evidence, not a multi-organization A2A network certification.

## 2. CAP with MCP

MCP owns tool/resource/prompt access. CAP only authorizes and constrains an Executor's MCP interaction.

### Flow

```text
Controller -> Directive(action.kind=mcp_tool, action.target=mcp://server/tool)
Guard -> GuardDecision(allow_with_constraints)
Executor -> verify Directive + effective constraints
Executor -> MCP tools/call
Executor -> ExecutionReport(tool_result_refs + evidence_produced)
```

### Mapping

| MCP concept | CAP mapping |
|---|---|
| Tool name/URI | `Directive.action.target`, `ConstraintSet.allowed_tools`, `ConstraintSet.forbidden_tools`. |
| Tool input schema | Remains MCP-owned; CAP may reference expected input/evidence. |
| Tool result | `ExecutionReport.tool_result_refs` and/or `EvidenceRef`. |
| MCP resource | `EvidenceRef.uri` or `action.target` when the action is resource access. |
| MCP capability negotiation | External; CAP may require negotiated capability before execution. |

When a tool is represented as CAP v1 `Capability` metadata, its `kind` is `tool`, its `subject_id` and `endpoint` may reference an MCP URI, and MCP-specific server, tool, or schema details belong in `Capability.profile_extensions`. CAP preserves that metadata for policy and registry lookup, but MCP remains the owner of tool definitions, input schemas, resource semantics, and invocation protocol.

The current reference runtime also includes a deterministic live MCP substrate path in `cap_protocol.runtime.substrate_interop`: an in-process MCP server accepts signed CAPEnvelope `Directive` payloads for `tools/call` and `resources/read`, runs them through Edge PEP before invoking any handler, discovers MCP descriptors through service-backed `Capability` records, refuses a forbidden tool before side effects, and emits ExecutionReport evidence refs for allowed calls. This replaces metadata-only MCP evidence with a live local server path, while external MCP servers and cross-organization interoperability remain separate release gates.

The third implementation interop adapter under `third_impl/go_cap_adapter` is deliberately narrower: it validates shared CAP v1 CAPEnvelope/JCS/signature fixtures in Go and reports fixture IDs, but it does not host MCP/A2A, HTTP, gRPC, registry, or PEP services.

External partner execution is tracked separately from this local evidence. The multi-organization MCP/A2A plan in `docs/mcp_a2a_interop/README.md` defines partner setup, trust roots, registry records, fixtures, pass/fail cases, logging/privacy rules, local simulation mode, and the evidence report format needed before the external interop gate can close.

## 3. CAP with OPA/Rego or Cedar

CAP does not define policy logic. Guards adapt CAP objects into policy-engine inputs and turn engine outputs into `GuardDecision`.

The current repository exposes both adapters through one PDP interface. The OPA/Rego path emits an OPA-shaped input document; the Cedar path emits a Cedar-shaped authorization request with `principal`, `action`, `resource`, and `context`. Both deterministic scaffold adapters reuse the same CAP privacy and operational-constraint evaluation so the included conformance fixtures produce equivalent allow/deny/human-review decisions. This is portability evidence for the CAP adapter boundary, not an organization-specific production OPA or Cedar deployment.

### OPA-style input example

```json
{
  "subject": "spiffe://example/controller/planner-1",
  "action": "mcp://github/tools/write_file",
  "resource": "repo:example/project",
  "directive": { "directive_id": "dir-001" },
  "constraints": { "max_wall_time_ms": 5000 },
  "evidence": ["cas://sha256/abc..."],
  "policy_refs": ["opa://cap/swe/write_file/v1#sha256:abc..."]
}
```

### Cedar authorization request mapping

| Cedar concept | CAP source |
|---|---|
| `principal.type` | CAP adapter namespace, currently `CAP::Principal`. |
| `principal.id` | Directive payload `subject_id`, then envelope `sender_id`. |
| `action.type` | CAP adapter namespace, currently `CAP::Action`. |
| `action.id` | `Directive.action.operation`, then `action.kind`, then `action.target`. |
| `resource.type` | CAP adapter namespace, currently `CAP::Resource`. |
| `resource.id` | `Directive.action.target`, payload `resource`, payload `recipient_id`, or envelope `receiver_id`. |
| `context.directive_id` | `Directive.directive_id`. |
| `context.session_id` / `context.trace_id` | CAP envelope session and trace identifiers. |
| `context.constraints` | Normalized Core `OperationalConstraints` plus namespaced profile constraints. |
| `context.evidence_refs` | EvidenceRef URIs only, not raw evidence content. |
| `context.policy_refs` | CAP `PolicyRef` metadata used for policy identity, version, digest, and entry point. |

Example Cedar-shaped request:

```json
{
  "principal": {
    "type": "CAP::Principal",
    "id": "spiffe://example/controller/planner-1"
  },
  "action": {
    "type": "CAP::Action",
    "id": "tools/call"
  },
  "resource": {
    "type": "CAP::Resource",
    "id": "mcp://github/tools/write_file"
  },
  "context": {
    "directive_id": "dir-001",
    "session_id": "session-001",
    "trace_id": "trace-001",
    "target": "mcp://github/tools/write_file",
    "constraints": { "max_wall_time_ms": 5000 },
    "evidence_refs": ["cas://sha256/abc..."],
    "policy_refs": [
      {
        "policy_id": "cap-swe-write-file",
        "engine": "cedar",
        "version": "1",
        "digest": "sha256:abc...",
        "uri": "policy://cap/swe/write_file/v1"
      }
    ]
  }
}
```

If a Cedar CLI/runtime is unavailable, the repository's `CedarPolicyAdapter` remains usable through a deterministic Cedar-shaped evaluator and marks `runtime_available=false` in the decision metadata. Deployments that require external Cedar evaluation should configure the adapter to require the runtime and fail closed when it is absent.

Organization-specific deployment guidance is in `docs/policy_deployment/README.md`, and the non-production sample layout is under `policies/organization_template/`. These artifacts show how an organization can own policy repositories, promotion tests, signed bundle metadata, environment separation, rollout, rollback, hot update, and emergency override controls without treating the repository's sample policies as production policy.

### GuardDecision output shape

```json
{
  "decision": "allow_with_constraints",
  "constraints_added": { "max_wall_time_ms": 2000 },
  "evidence_required": [],
  "reason": "Write access allowed only in sandbox workspace."
}
```

## 4. Observability plane: OpenTelemetry semantic conventions

CAP Observers SHOULD emit spans or span events with these attributes.

### Required attributes

| Attribute | Description |
|---|---|
| `cap.version` | CAP version. |
| `cap.message.id` | CAP message id. |
| `cap.message.type` | CAP message type. |
| `cap.session.id` | Session id if available. |
| `cap.task.id` | Task id if available. |
| `cap.directive.id` | Directive id when applicable. |
| `cap.lifecycle.state` | Current Directive lifecycle state. |
| `cap.sender.id` | Sender identity. |
| `cap.receiver.id` | Receiver identity when applicable. |
| `cap.guard.decision` | Guard decision value when applicable. |
| `cap.refusal.reason_code` | Refusal reason when applicable. |
| `cap.authority_chain.hash` | Hash of authority chain representation. |

### Recommended attributes

| Attribute | Description |
|---|---|
| `cap.policy.refs` | Stable policy references, preferably digests or ids. |
| `cap.evidence.refs` | Evidence ids/hashes, not raw evidence contents. |
| `cap.profile.namespaces` | Active profile namespaces. |
| `cap.execution.status` | ExecutionReport status. |
| `cap.compensation.status` | Compensation outcome. |
| `cap.constraint.merge.result` | `narrowed`, `unchanged`, or `conflict`. |

### Lifecycle event names

- `cap.directive.proposed`
- `cap.guard.decision`
- `cap.directive.dispatched`
- `cap.directive.accepted`
- `cap.directive.refused`
- `cap.execution.started`
- `cap.execution.completed`
- `cap.compensation.attempted`
- `cap.directive.terminal`

Telemetry MUST NOT include raw hidden chain-of-thought or sensitive evidence content. OpenTelemetry export belongs to the observability plane; it receives lifecycle facts from Local PEPs, Edge PEPs, Executors, and Control Plane components but does not replace the CAP control plane or PDP.

### Sink responsibility split

CAP implementations SHOULD keep observability sinks separate even when they share an event source:

| Sink | Primary purpose | Integrity and retention assumption |
|---|---|---|
| Audit | Durable accountability and compliance evidence. | Tamper-evident or signed, retention-oriented, and optionally a delivery precondition when a profile requires audit persistence before user-visible delivery. |
| Telemetry | Operational traces, metrics, and debugging signals. | May be sampled, lossy, short-retention, and unavailable without invalidating audit integrity. |
| Provenance | Structural lineage between agents, evidence, activities, and generated results. | Preserves graph relationships and may be persisted independently of operational telemetry delivery. |

The repository includes a deterministic scaffold in `cap_protocol.runtime.observability` that models this split. It includes `SignedAuditSink`, which signs audit operations over the next hash-chain sequence and previous-chain hash with an external signing-provider interface, records retention/access metadata, exposes replication/export retry hooks, and lets profiles require audit confirmation before user-visible delivery. It also includes `W3CProvenanceSink` and a local `JsonlProvStore` that ingests PROV-JSONLD documents and supports queryable session, evidence, authority, and interrupt lineage without storing raw sensitive evidence or hidden chain-of-thought. The scaffold also includes a reference OpenTelemetry collector fixture at `config/otel/collector-cap.yaml` and tests that require `cap.*` attribute coverage across envelope receipt, PEP decision, interrupt, execution, evidence, audit, and refusal events. Production deployments still need deployed KMS/HSM custody, transparency/replication services, collector/exporter operations, production PROV store deployment, access-control integration, recovery procedures, and operational runbooks.

## 5. Observability plane: W3C PROV mapping

| CAP concept | PROV mapping |
|---|---|
| Controller, Executor, Guard, Observer | `prov:Agent` or `prov:SoftwareAgent`. |
| Directive | `prov:Plan`; dispatch/execution may be `prov:Activity`. |
| GuardDecision | `prov:Entity` generated by policy-evaluation `prov:Activity`. |
| ExecutionReport | `prov:Entity` generated by execution `prov:Activity`. |
| EvidenceRef | `prov:Entity`. |
| AuthorityChain | `prov:wasAssociatedWith`, `prov:actedOnBehalfOf`, qualified association/delegation. |
| Evidence consumed | `prov:used`. |
| Evidence produced | `prov:wasGeneratedBy`. |
| Compensation | separate `prov:Activity` linked to original side effect. |

The reference `W3CProvenanceSink` maps CAP observability events into PROV-JSONLD bundles with `prov:Entity`, `prov:Activity`, `prov:SoftwareAgent`, `prov:used`, `prov:wasGeneratedBy`, `prov:wasDerivedFrom`, `prov:wasAssociatedWith`, and `prov:actedOnBehalfOf` relations. `JsonlProvStore` is a local deterministic store for conformance and development workflows; production profiles should replace it with a deployed graph/document store, service authentication, access policy enforcement, retention/deletion controls, backups, and recovery procedures.

## 6. DSSE / in-toto / SLSA / transparency logs

CAP does not define a new signature envelope. Deployments SHOULD use established attestation formats.

Recommended usage:

| CAP object | Attestation recommendation |
|---|---|
| AuthorityChainStep | DSSE/COSE/JOSE signature or in-toto statement. |
| GuardDecision | DSSE/in-toto attestation for high-stakes decisions. |
| Evidence snapshot | Content hash plus optional signed statement. |
| ExecutionReport | Optional attestation for cross-organization workflows. |
| Release artifacts / tool binaries | SLSA/in-toto supply-chain provenance. |

For Sigstore/Rekor, CAP deployments SHOULD log content-minimized attestations rather than raw sensitive payloads. The current deterministic scaffold in `cap_protocol.security.transparency` logs release attestations and AuthorityChainStep attestations as DSSE-wrapped in-toto statements. `LocalRekorTransparencyLog` returns Rekor-compatible bundles with hashedrekord-like entries, signed entry timestamps, Merkle inclusion proofs, and checkpoint metadata. `verify_transparency_bundle` verifies the DSSE attestation, entry body hash, signed entry timestamp, and inclusion proof offline. Production deployments should replace the local log with a real Rekor service, monitor publication failures, and define whether missing transparency inclusion blocks release, authority issuance, or only raises an operational alert.

## 7. Workflow engine composition

Workflow engines own durable orchestration, activity retry, timers, local workflow state, and human workflow queues. CAP owns the supervisory control objects that move through those workflows. A workflow activity may receive a `CAPEnvelope`, call an Edge PEP or Local PEP to verify it, route it through a Session Router, emit `InterruptDecision` during pause/retry/escalation, and emit `ExecutionReport` on terminal completion. The workflow history should link `session_id`, `trace_id`, envelope ids, and emitted report/interrupt refs without storing raw sensitive payload bodies.

The current repository chooses Temporal for the deterministic composition sample because Temporal's workflow-history and activity-retry model maps cleanly to CAP lifecycle events. The sample is runnable without the `temporalio` dependency:

```bash
source venv/bin/activate
python -m cap_protocol.runtime.workflow_engine
```

That local runner is a Temporal-style scaffold, not a deployed Temporal worker. It records `WorkflowExecutionStarted`, CAP envelope receipt/verification/routing, a retryable activity failure, a `pause` `InterruptDecision` for the scheduled retry, and a final signed `ExecutionReport`. A tampered input envelope is refused before activity execution. Production Temporal or LangGraph integration should replace only the local runner/history implementation; CAP envelope verification, PolicyRef/PrivacyBoundary checks, authority validation, interrupts, refusals, execution reports, and observability semantics remain CAP-owned.

## 8. Optional direct serialization

CAP Core does not mandate one transport. Direct serialization options MAY include:

- HTTP/JSON for simple integrations.
- gRPC/protobuf for internal high-throughput systems.
- WebSocket/SSE for streaming session updates.
- Message queues for asynchronous control loops.

Conformance tests target semantic behavior, not a specific transport. The gRPC and HTTP/JSON demos now carry v1 `CAPEnvelope` objects on their active hot paths while retaining v0.1 compatibility fixtures. Neither demo yet implements the full v1 decomposed Control Plane, production network registry deployment, Local PEP trust modes, Edge PEP service-boundary enforcement, or production observability exporter/collector integration tracked in `CAP_v1_TASKS.md`.

## Normative and Informative References

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
