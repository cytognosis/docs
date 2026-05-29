# CAP V1 Baseline: Integrations, API, and Bindings

**Generated:** 2026-05-25T06:54:46+00:00
**Document set:** CAP V1 baseline consolidated Markdown set
**Repository status:** V1 architecture documented and V1 runtime scaffold present; current executable package remains `v0.1-production-candidate` and is not a complete stable V1 runtime.
**Purpose:** Integration model for A2A, MCP, OPA/Cedar, OpenTelemetry, W3C PROV, gRPC, and HTTP/JSON bindings.

This file is part of `docs/v1_baseline/`, the capped baseline V1 documentation folder. It preserves and consolidates source documentation from the repository. Local links in preserved source sections are rewritten to resolve from this generated baseline file.

## Source Map

- `docs/CAP_05_integrations.md`
- `docs/policy_deployment/README.md`
- `docs/mcp_a2a_interop/README.md`
- `docs/api.md`
- `reference_grpc/README.md`
- `second_http/README.md`
- `src/cap_protocol/bindings/grpc_reference/README.md`
- `src/cap_protocol/bindings/http_json/README.md`
## Source: `docs/CAP_05_integrations.md`

## CAP_05 — Integrations

CAP is designed to compose with other systems. This file defines recommended mappings. Unless a profile says otherwise, these mappings are informative, not mandatory.

CAP v1 is transport-independent and framework-independent. It uses the surrounding stack as three planes:

- **Data plane:** A2A, MCP, HTTP, gRPC, WebSocket, and local IPC carry agent, tool, and user traffic governed by CAP enforcement points.
- **Control plane:** CAP-specific `CAPEnvelope`, `Directive`, `GuardDecision`, `InterruptDecision`, `RefusalMessage`, and `ExecutionReport` objects carry synchronous authority, interruption, refusal, and reporting semantics.
- **Observability plane:** signed audit records, OpenTelemetry telemetry, and W3C PROV graphs leave through independent sinks. Integrations must not make telemetry or provenance export part of every hot-path Control Plane decision unless a profile explicitly requires audit persistence before delivery.

The architecture diagrams in `architecture.md#architecture-diagrams` show where these integration planes meet Local PEPs, Edge PEPs, PDPs, registries, and observability sinks.

When an integration carries an `InterruptDecision`, the serialized `action` value MUST be one of `allow`, `deny`, `transform`, `constrain`, `pause`, `escalate`, or `reroute`. Integration or profile labels such as downgraded language, revised output, local fallback, or deferred analysis belong in `reason_code`, `payload_directive_ref`, profile metadata, or test names; they are shorthand for Core-action compositions, not enum extensions.

### CAP v1 Capability Shape For Integrations

CAP v1 uses one `Capability` shape for agents, tools, services, humans, and policy subjects. The required fields are `capability_id`, `kind`, `subject_id`, and a non-empty `operations` list. The optional fields are `endpoint`, `risk_level`, `policy_refs`, and `profile_extensions`.

Integration-specific discovery metadata remains in `profile_extensions`. A2A AgentCard references belong under an A2A-owned extension key, and MCP server/tool/input-schema details belong under an MCP-owned extension key. CAP registries use the Core fields to resolve, cache, version, digest-check, and authorize operations, while preserving extension metadata for the integration that owns it.

The checked-in v1 examples cover all five `kind` values: agent, tool, service, human, and policy. The current deterministic registry scaffold validates the same closed shape and rejects top-level integration metadata such as `a2a` or `mcp`; those keys must sit under `Capability.profile_extensions`.

### 1. CAP over A2A

A2A owns peer-agent discovery, Agent Cards, messages, tasks, artifacts, and transport bindings. CAP metadata MAY be embedded in or referenced from A2A `Task`, `Message`, or `Part` objects.

#### Recommended mapping

| A2A concept | CAP mapping |
|---|---|
| AgentCard | Advertise CAP support, supported profiles, capabilities, and required extensions. |
| Task | Durable work container that may carry a CAP Directive. |
| Message | May carry CAP envelope or reference CAP payload. |
| Part | Atomic content part containing CAP JSON or a reference to it. |
| Artifact | May become an EvidenceRef or tool/result reference in ExecutionReport. |
| Task canceled/failed | Map to RefusalMessage or ExecutionReport status depending on lifecycle stage. |

#### CAP metadata location

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

### 2. CAP with MCP

MCP owns tool/resource/prompt access. CAP only authorizes and constrains an Executor's MCP interaction.

#### Flow

```text
Controller -> Directive(action.kind=mcp_tool, action.target=mcp://server/tool)
Guard -> GuardDecision(allow_with_constraints)
Executor -> verify Directive + effective constraints
Executor -> MCP tools/call
Executor -> ExecutionReport(tool_result_refs + evidence_produced)
```

#### Mapping

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

### 3. CAP with OPA/Rego or Cedar

CAP does not define policy logic. Guards adapt CAP objects into policy-engine inputs and turn engine outputs into `GuardDecision`.

The current repository exposes both adapters through one PDP interface. The OPA/Rego path emits an OPA-shaped input document; the Cedar path emits a Cedar-shaped authorization request with `principal`, `action`, `resource`, and `context`. Both deterministic scaffold adapters reuse the same CAP privacy and operational-constraint evaluation so the included conformance fixtures produce equivalent allow/deny/human-review decisions. This is portability evidence for the CAP adapter boundary, not an organization-specific production OPA or Cedar deployment.

#### OPA-style input example

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

#### Cedar authorization request mapping

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

#### GuardDecision output shape

```json
{
  "decision": "allow_with_constraints",
  "constraints_added": { "max_wall_time_ms": 2000 },
  "evidence_required": [],
  "reason": "Write access allowed only in sandbox workspace."
}
```

### 4. Observability plane: OpenTelemetry semantic conventions

CAP Observers SHOULD emit spans or span events with these attributes.

#### Required attributes

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

#### Recommended attributes

| Attribute | Description |
|---|---|
| `cap.policy.refs` | Stable policy references, preferably digests or ids. |
| `cap.evidence.refs` | Evidence ids/hashes, not raw evidence contents. |
| `cap.profile.namespaces` | Active profile namespaces. |
| `cap.execution.status` | ExecutionReport status. |
| `cap.compensation.status` | Compensation outcome. |
| `cap.constraint.merge.result` | `narrowed`, `unchanged`, or `conflict`. |

#### Lifecycle event names

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

#### Sink responsibility split

CAP implementations SHOULD keep observability sinks separate even when they share an event source:

| Sink | Primary purpose | Integrity and retention assumption |
|---|---|---|
| Audit | Durable accountability and compliance evidence. | Tamper-evident or signed, retention-oriented, and optionally a delivery precondition when a profile requires audit persistence before user-visible delivery. |
| Telemetry | Operational traces, metrics, and debugging signals. | May be sampled, lossy, short-retention, and unavailable without invalidating audit integrity. |
| Provenance | Structural lineage between agents, evidence, activities, and generated results. | Preserves graph relationships and may be persisted independently of operational telemetry delivery. |

The repository includes a deterministic scaffold in `cap_protocol.runtime.observability` that models this split. It includes `SignedAuditSink`, which signs audit operations over the next hash-chain sequence and previous-chain hash with an external signing-provider interface, records retention/access metadata, exposes replication/export retry hooks, and lets profiles require audit confirmation before user-visible delivery. It also includes `W3CProvenanceSink` and a local `JsonlProvStore` that ingests PROV-JSONLD documents and supports queryable session, evidence, authority, and interrupt lineage without storing raw sensitive evidence or hidden chain-of-thought. The scaffold also includes a reference OpenTelemetry collector fixture at `config/otel/collector-cap.yaml` and tests that require `cap.*` attribute coverage across envelope receipt, PEP decision, interrupt, execution, evidence, audit, and refusal events. Production deployments still need deployed KMS/HSM custody, transparency/replication services, collector/exporter operations, production PROV store deployment, access-control integration, recovery procedures, and operational runbooks.

### 5. Observability plane: W3C PROV mapping

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

### 6. DSSE / in-toto / SLSA / transparency logs

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

### 7. Workflow engine composition

Workflow engines own durable orchestration, activity retry, timers, local workflow state, and human workflow queues. CAP owns the supervisory control objects that move through those workflows. A workflow activity may receive a `CAPEnvelope`, call an Edge PEP or Local PEP to verify it, route it through a Session Router, emit `InterruptDecision` during pause/retry/escalation, and emit `ExecutionReport` on terminal completion. The workflow history should link `session_id`, `trace_id`, envelope ids, and emitted report/interrupt refs without storing raw sensitive payload bodies.

The current repository chooses Temporal for the deterministic composition sample because Temporal's workflow-history and activity-retry model maps cleanly to CAP lifecycle events. The sample is runnable without the `temporalio` dependency:

```bash
source venv/bin/activate
python -m cap_protocol.runtime.workflow_engine
```

That local runner is a Temporal-style scaffold, not a deployed Temporal worker. It records `WorkflowExecutionStarted`, CAP envelope receipt/verification/routing, a retryable activity failure, a `pause` `InterruptDecision` for the scheduled retry, and a final signed `ExecutionReport`. A tampered input envelope is refused before activity execution. Production Temporal or LangGraph integration should replace only the local runner/history implementation; CAP envelope verification, PolicyRef/PrivacyBoundary checks, authority validation, interrupts, refusals, execution reports, and observability semantics remain CAP-owned.

### 8. Optional direct serialization

CAP Core does not mandate one transport. Direct serialization options MAY include:

- HTTP/JSON for simple integrations.
- gRPC/protobuf for internal high-throughput systems.
- WebSocket/SSE for streaming session updates.
- Message queues for asynchronous control loops.

Conformance tests target semantic behavior, not a specific transport. The gRPC and HTTP/JSON demos now carry v1 `CAPEnvelope` objects on their active hot paths while retaining v0.1 compatibility fixtures. Neither demo yet implements the full v1 decomposed Control Plane, production network registry deployment, Local PEP trust modes, Edge PEP service-boundary enforcement, or production observability exporter/collector integration tracked in `CAP_v1_TASKS.md`.

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


## Source: `docs/policy_deployment/README.md`

## Organization OPA/Cedar Policy Deployment Guide

This guide prepares organizations to replace the repository's deterministic OPA-shaped and Cedar-shaped policy scaffolds with owned policy runtimes, policy bundles, promotion controls, and operational evidence. It does not deploy production OPA or Cedar, and it does not close the organization-specific policy deployment gate in [CAP_RELEASE_GATES.md](../CAP_RELEASE_GATES.md).

The checked-in policies and adapter tests are local scaffold evidence. They are not production policy, not a regulated-profile approval, and not a substitute for organization-owned policy review.

### Scope

This guide covers:

- policy ownership and approval responsibilities;
- OPA/Rego and Cedar deployment choices;
- CAP PDP adapter request/decision contracts;
- Policy Registry and signed policy-bundle promotion;
- environment separation;
- rollout, rollback, hot update, emergency override, and exception handling;
- test promotion and evidence needed before a deployment can claim organization-specific policy readiness.

It does not define the organization's policy semantics, legal obligations, clinical/domain rules, cloud IAM, or runtime hosting platform.

### Existing CAP Policy Interfaces

| Surface | Current repo hook | Production expectation |
|---|---|---|
| CAP request shape | `CAPPolicyRequest` in `cap_protocol.runtime.pdp_adapters` | Organization-owned adapters should preserve subject, action, resource, context, constraints, evidence refs, policy refs, privacy boundary, and profile namespace. |
| OPA-shaped input | `opa_input(request)` | Real OPA/Rego policies should consume the same content-minimized input shape or a versioned superset. |
| Cedar-shaped request | `cedar_authorization_request(request)` | Real Cedar policies should preserve CAP principal/action/resource/context mapping and avoid raw evidence contents. |
| PDP decision shape | `PDPDecision` | Real adapters must return allow/deny/human-review decisions, reasons, constraints deltas, policy ids, runtime metadata, and fail-closed runtime availability. |
| Policy bundles | `PolicyBundle`, `OfflinePolicyBundleCache`, `ReferencePolicyRegistryService` in `cap_protocol.runtime.local_pep` | Production deployments must distribute signed bundles through an authenticated Policy Registry with session pinning, expiry, revocation, and audited hot-update behavior. |
| Guard conversion | gRPC `evaluate_policy_to_guard(...)` and HTTP `opa_policy_to_guard(...)` | Real policy decisions must still become CAP `GuardDecision` objects and must not bypass Local PEP or Edge PEP checks. |

### Ownership Model

Every production policy set should have named owners:

| Role | Responsibility |
|---|---|
| Policy owner | Owns policy intent, risk appetite, profile constraints, and approval to promote. |
| Domain reviewer | Reviews domain-specific behavior, for example CAP-Med non-diagnostic or CAP-SWE repository-write constraints. |
| Security reviewer | Reviews authority, privacy, data access, policy update, and emergency override impact. |
| Runtime owner | Operates OPA/Cedar services, adapters, registry clients, and availability monitoring. |
| Release owner | Signs and promotes bundles, manages staged rollout, and coordinates rollback. |
| Audit owner | Verifies policy evaluation, promotion, hot update, emergency override, and exception records. |

No single person or service should be able to write policy, approve it, sign the bundle, deploy it, and approve emergency override for high-risk profiles.

### Environment Separation

Use separate policy assets, signing keys, registries, and PDP endpoints per environment:

| Environment | Purpose | Requirements |
|---|---|---|
| `dev` | Policy authoring and adapter development. | Synthetic data only; no production signer; deterministic fixtures allowed. |
| `test` | Automated parity and negative tests. | Signed test bundles; production-like CAP input shapes; no production data. |
| `staging` | Deployment rehearsal and canary validation. | Staging KMS/HSM keys, staging Policy Registry, staged revocation source, production-like OPA/Cedar runtime. |
| `prod` | Organization-approved enforcement. | Production signer, production Policy Registry, monitored PDP runtime, live revocation, audit export, rollback path. |

Policy IDs, bundle IDs, digest refs, and PDP endpoints should include environment or trust-domain metadata so a non-production bundle cannot be silently used in production.

### Sample Layout

A non-production sample layout is checked in under [policies/organization_template](../../policies/organization_template/):

```text
policies/organization_template/
  README.md
  bundles/policy-bundle.manifest.example.json
  cedar/cap_policy.cedar
  opa/cap_policy.rego
  tests/policy_cases.example.jsonl
```

Organizations should copy the shape into their own repository or controlled policy workspace. Do not edit the template into production policy in this repository.

### Change Control

Minimum change-control fields:

- policy id, owner, profile namespace, engine, and entry point;
- reason for change and risk classification;
- affected CAP roles, actions, resources, PrivacyBoundary dimensions, and PolicyRefs;
- test evidence and reviewer approvals;
- signed bundle id, version, digest, expiry, and revocation ref;
- rollout plan, rollback plan, and monitoring checks;
- exception or emergency override criteria.

Policy changes should be reviewed as code and promoted only after deterministic CAP tests, engine-specific tests, negative/adversarial cases, and signature verification pass.

### Test Promotion

Before promotion from one environment to the next, run at least:

```bash
source venv/bin/activate
pytest tests/test_pdp_adapters.py tests/test_policy_registry_service.py tests/test_policy_hot_update.py
cap-check-v1-conformance
```

Deployment-owned policy repositories should add:

- OPA unit tests for Rego packages and entrypoints.
- Cedar schema validation and authorization tests.
- CAP parity fixtures proving equivalent allow/deny/human-review behavior where both OPA and Cedar are claimed.
- Negative tests for forbidden tools, raw-data egress, stale policy, unknown policy id, digest mismatch, expired bundle, revoked bundle, and runtime unavailable.
- Profile-specific tests for CAP-Med, CAP-SWE, or organization-owned profiles.
- Canary tests against staging PDP endpoints and staging Policy Registry.

Promotion should fail closed if an external runtime is required but unavailable, mirroring `CedarPolicyAdapter(require_external_runtime=True)`.

### Rollout

Recommended rollout:

1. Publish the signed bundle as `candidate` in the target environment Policy Registry.
2. Run staging/canary CAP traces using the exact `policy_id`, `version`, and `digest`.
3. Activate the bundle for new sessions only.
4. Keep existing sessions pinned to their current bundle unless the profile explicitly allows hot update.
5. Monitor refusals, `stale_policy`, `require_policy_update`, `privacy_denied`, PDP latency, runtime unavailability, and emergency override counters.
6. Expand rollout by trust domain, profile, service, or user cohort.
7. Record rollout evidence in audit/provenance and release notes.

### Rollback

Rollback must be preplanned before promotion:

- keep the last known-good bundle active and verifiable;
- disable new sessions from receiving the bad bundle;
- revoke the bad bundle in the Policy Registry;
- force hot update only when the profile and incident response approve it;
- record affected sessions and policy refs;
- add regression tests for the failure before re-promoting.

Existing sessions should remain pinned unless the risk of staying pinned is higher than the risk of forced update.

### Hot Updates

CAP treats hot update as explicit. A Local PEP or Executor must not silently authorize a directive when its `PolicyRef.version` or `PolicyRef.digest` disagrees with the active signed bundle.

Production hot update requires:

- profile-level permission for hot update;
- signed target bundle with valid expiry and revocation state;
- Policy Registry audit event;
- session pin update record;
- reason code and approval ref;
- verifier behavior for stale in-flight directives.

If the hot update cannot be proven, return `stale_policy` or the Guard/PDP equivalent `require_policy_update`.

### Emergency Override And Exceptions

Emergency override must be narrower than ordinary policy relaxation:

- dual approval for high-risk profiles;
- signed emergency bundle with short expiry;
- clear scope, affected identities, and affected actions;
- mandatory audit and post-incident review;
- automatic rollback or expiry;
- refusal if signature, digest, expiry, or revocation metadata is invalid.

Exceptions should be modeled as policy data with owner, expiry, reason, scope, and audit refs, not as code paths that bypass PDP, Local PEP, Edge PEP, or Policy Registry checks.

### Deployment Evidence Checklist

The organization-specific OPA/Cedar deployment gate remains open until a deployment organization supplies:

- policy ownership matrix and approval workflow;
- environment topology and endpoint separation;
- OPA/Rego and/or Cedar policy repository with tests;
- CAP adapter mapping and versioned request schemas;
- signed policy-bundle generation and verification evidence;
- Policy Registry publication, revocation, session pinning, hot-update, and rollback evidence;
- emergency override process and last drill or tabletop evidence;
- PDP runtime monitoring, latency, availability, and fail-closed behavior;
- audit export showing policy evaluation and promotion events without raw sensitive evidence;
- evidence that sample policies in this repository are not used as production policy.

### External Gate Status

This guide is preparation evidence only. The external gate remains open until a real organization supplies owned policies, real OPA/Cedar runtime deployment evidence, signed bundle operations, and operational review artifacts.


## Source: `docs/mcp_a2a_interop/README.md`

## Multi-Organization MCP/A2A Interop Plan

This package prepares the external live MCP/A2A interoperability gate. It is a runbook and evidence format for partner organizations. It does not close the gate by itself: local simulation and repository-maintainer-only execution remain local evidence.

The release-gate status is tracked in [CAP_RELEASE_GATES.md](../CAP_RELEASE_GATES.md). Integration mappings are described in [CAP_05_integrations.md](../CAP_05_integrations.md).

### Objective

Demonstrate that CAPEnvelope authority, policy, privacy, evidence, and refusal semantics survive real cross-organization MCP and A2A operation.

The minimum run uses two separately controlled organizations:

| Role | Responsibility | Required owner |
|---|---|---|
| Organization A controller | Issues signed CAPEnvelope directives and publishes controller identity metadata. | Partner A security or platform owner |
| Organization A registries | Provides policy, capability, evidence, revocation, and warrant-key references used by A. | Partner A registry owner |
| Organization B MCP server | Hosts at least one allowed MCP `tools/call`, one allowed MCP `resources/read`, and one forbidden tool target. | Partner B agent/tool owner |
| Organization B A2A agent | Publishes AgentCard CAP extension metadata and receives CAPEnvelope-wrapped A2A messages. | Partner B agent/tool owner |
| Independent observer | Records transcript hashes, decision results, log extracts, and report sign-off. | Jointly agreed reviewer |

Optional third or fourth organizations can add another controller, another MCP server, or an A2A peer with a different trust root. More organizations strengthen the evidence, but two independent owners are the minimum external run.

### Existing Local Harness

The repository already has a deterministic local harness:

- [substrate_interop.py](../../src/cap_protocol/runtime/substrate_interop.py) builds in-process MCP and A2A peers.
- [test_live_substrate_interop.py](../../tests/test_live_substrate_interop.py) checks MCP `tools/call`, MCP `resources/read`, forbidden-tool refusal before handler execution, A2A CAPEnvelope carriage, AgentCard CAP extension metadata, and tampered-envelope refusal.
- [go_cap_adapter](../../third_impl/go_cap_adapter) validates shared CAPEnvelope/JCS/signature fixtures in Go, but it does not host MCP or A2A services.

Run the local simulation from the repository root:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest tests/test_live_substrate_interop.py tests/test_go_interop_adapter.py
```

Local simulation is useful for partner onboarding and fixture debugging. It is not external multi-organization evidence.

### Partner Setup

Each organization should prepare a short environment sheet before the live run:

| Field | Required content |
|---|---|
| Organization id | Stable display name and trust-domain URI. |
| Contact owners | Security, registry, platform, and tool/agent owners. |
| Runtime stack | MCP server/runtime, A2A implementation, CAP adapter version, deployment environment. |
| CAP version | Supported CAP version and profile names. |
| Identity system | SPIFFE, OIDC, X.509, DID, or other identity used at the service boundary. |
| Network path | Ingress URL or service name, mTLS or token-auth shape, firewall allowlist owner. |
| Privacy boundary | Raw-data egress rules, logging policy, retention policy, allowed recipients. |
| Report owner | Person who can sign off that the run used organization-owned systems. |

Use [config/mcp_a2a_interop.example.yaml](../../config/mcp_a2a_interop.example.yaml) as a non-secret checklist. Do not store real tokens, private keys, credentials, account ids, or partner-confidential endpoints in the repository.

### Trust Roots

Before test execution, partners exchange or agree on these non-secret trust anchors:

| Trust item | Required evidence |
|---|---|
| Workload identity root | SPIFFE trust bundle, OIDC issuer/JWKS URL, X.509 CA bundle, or equivalent root reference. |
| CAP signing keys | Public key ids, algorithm, key-use metadata, rotation owner, and validity window. |
| Authority/warrant root | AuthorityChain root, warrant-key directory, revocation reference, and attenuation rules. |
| Policy root | Policy Registry base URL or bundle location, policy id, version, digest, and entry point. |
| Capability root | Capability Registry base URL or exported record set for AgentCard, MCP tools, and MCP resources. |
| Evidence root | Evidence Registry base URL or content-addressed storage root with hash verification. |
| Time source | NTP or equivalent clock source and allowed skew. |

The run should fail closed if any required trust root is missing, expired, revoked, or mismatched.

### Registry Setup

Each external run needs registry records for the exact live endpoints under test:

| Registry | Minimum records |
|---|---|
| Capability Registry | A2A agent capability, MCP tool capability, MCP resource capability, controller/service capability. |
| Policy Registry | Signed policy bundle or immutable policy record with digest, version, entry point, and environment. |
| Evidence Registry | Test EvidenceRefs with content hashes, freshness policy, media type, size, access policy ref, and expiry. |
| Warrant/key registry | CAP signing public keys, AuthorityChain or warrant keys, revocation state, and rotation metadata. |

Registry records should be exported as evidence refs or hashes in the final report. Raw evidence content should not be copied into the report.

### Fixtures

Create one fixture bundle per partner run. The fixture bundle should include:

| Fixture | Required fields |
|---|---|
| CAPEnvelope directive | `envelope_id`, `session_id`, `trace_id`, sender, receiver, message kind, policy refs, privacy boundary ref, authority chain ref, timestamp, TTL, and signature. |
| MCP tool descriptor | Server URI, tool URI/name, input schema hash, operation `tools/call`, risk level, and CAP constraints. |
| MCP resource descriptor | Server URI, resource URI/name, media type, operation `resources/read`, and CAP constraints. |
| A2A AgentCard | Agent URL, CAP extension URI, supported CAP version, supported message types, and envelope-required flag. |
| EvidenceRef set | URI, hash, media type, size, expiry, freshness policy, access policy ref, and provenance ref. |
| PolicyRef set | Policy id, engine, version, digest, URI, and entry point. |
| PrivacyBoundary | Classification, movement, transformation, retention, logging, audit visibility, raw-data egress, minimization, and allowed recipients. |

Use content-addressed references and hashes for fixtures whenever possible. Keep raw transcripts, raw audio, hidden reasoning, credentials, private keys, and sensitive partner data out of fixture files.

### Required Test Cases

The live run should include these pass and fail cases. Additional partner-specific cases can be appended.

| ID | Flow | Expected result |
|---|---|---|
| INT-MCP-01 | Org A sends signed CAPEnvelope directive to Org B MCP `tools/call` for an allowed tool. | Allowed; handler executes; ExecutionReport includes tool result refs and Edge PEP decision evidence. |
| INT-MCP-02 | Org A sends signed CAPEnvelope directive to Org B MCP `resources/read` for an allowed resource. | Allowed; resource handler executes; response returns EvidenceRefs, not raw sensitive content. |
| INT-MCP-03 | Org A requests a forbidden MCP tool target. | Refused before handler execution; refusal reason identifies forbidden target or policy denial. |
| INT-MCP-04 | CAPEnvelope signature is tampered after signing. | Refused before payload use or handler execution. |
| INT-MCP-05 | PolicyRef digest or version does not match the pinned registry record. | Refused before handler execution. |
| INT-MCP-06 | EvidenceRef hash mismatches backing content or evidence is expired. | Refused before evidence influences execution. |
| INT-A2A-01 | Org A sends an A2A message whose part carries `application/cap-envelope+json`. | Allowed; receiver verifies CAPEnvelope and records accepted message id. |
| INT-A2A-02 | Org B AgentCard advertises CAP v1 support and envelope-required metadata. | AgentCard metadata resolves through registry or live discovery and matches the report. |
| INT-A2A-03 | A2A receiver id or trust domain does not match the signed CAPEnvelope. | Refused before message delivery. |
| INT-A2A-04 | A2A message omits required CAPEnvelope carriage. | Refused or not accepted as CAP-governed traffic. |
| INT-PRIV-01 | Fixture attempts raw transcript, raw audio, or unrestricted result egress across the boundary. | Refused or transformed according to PrivacyBoundary; raw content is absent from logs. |
| INT-REPLAY-01 | A previously accepted directive is replayed with the same idempotency key. | Duplicate side effect is prevented and outcome is auditable. |
| INT-OBS-01 | Audit, telemetry, and provenance sinks receive content-minimized events for allowed and refused flows. | Report includes event ids or hashes without raw sensitive content. |

### Logging and Privacy Rules

Logs and reports should include:

- envelope ids, session ids, trace ids, partner ids, timestamps, and decision status;
- policy ids, policy digests, capability ids, evidence hashes, authority/warrant refs, and key ids;
- handler-executed booleans for every allow/refusal path;
- audit, telemetry, and provenance event ids or hashes;
- redaction/minimization metadata and `raw_content_logged=false` where applicable.

Logs and reports must not include:

- private keys, tokens, credentials, bearer headers, or partner secrets;
- raw transcript/audio, raw sensitive evidence, hidden reasoning, unsafe partial output, or matched redaction spans;
- unredacted endpoint internals that a partner marks confidential.

Partner organizations should retain their own raw operational logs under their governance controls. The shared report should contain hashes, ids, and summaries sufficient to reproduce the gate conclusion without leaking protected content.

### Report Format

Use [report_template.md](../mcp_a2a_interop/report_template.md) for the external evidence report. A valid report includes:

- partner organization identities and sign-off owners;
- trust roots and registry records used for the run;
- fixture manifest hashes;
- pass/fail matrix for every required test case;
- selected log/audit/provenance references;
- privacy review notes;
- open findings and retest status;
- explicit gate conclusion.

The conclusion must distinguish:

- local simulation only;
- live external-stack test by one organization;
- live multi-organization test by at least two independent organizations.

Only the third category can support closing the live multi-organization MCP/A2A gate.

### Local Simulation Mode

Use local simulation before inviting partners:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest tests/test_live_substrate_interop.py
```

Optional companion check:

```bash
source venv/bin/activate
pytest tests/test_go_interop_adapter.py
```

Record local simulation output in the report only as onboarding evidence. Mark the gate conclusion as `external_evidence_required` unless two independent organizations ran live MCP/A2A endpoints or equivalent external stacks.

### Closure Rule

The live multi-organization MCP/A2A gate can close only when:

- at least two independent organizations execute the required MCP and A2A cases against live or deployment-representative endpoints;
- trust roots, registries, policies, warrants, and EvidenceRefs are organization-owned or organization-approved for the run;
- every required fail-closed case refuses before handler execution or message delivery;
- logs and reports are content-minimized and reviewed for privacy leakage;
- any blocking findings have fixes or documented mitigations and retest evidence;
- release docs are updated without claiming more than the evidence supports.


## Source: `docs/api.md`

## API

### CLI

- `cap-run-final --target both`: run selected bindings and hardening checks.
- `cap-run-hardening`: run schema, policy, signature, attestation, fixture, and audit checks.
- `cap-verify-package`: verify required package files and detect forbidden stale labels or packaged private key material.
- `cap-verify-release-baseline`: run the baseline release verifier.
- `cap-check-v1-schema-drift`: compare CAP v1 LinkML authoring schemas with checked-in v1 JSON Schema artifacts and fail on essential drift. Without reinstalling entry points, run `python scripts/check_v1_schema_drift.py`.
- `cap-run-therapist-supervisor-demo --case all`: run the deterministic Therapist/Supervisor/Psych Results Tool scenario.
- `cap-run-v1-benchmarks --iterations 100 --warmup 10`: regenerate local deterministic latency and mobile-resource benchmark artifacts under `docs/benchmarks/`.

Compatibility commands:

- `python run_final_cap.py --target both`
- `python run_production_hardening.py`
- `python VERIFY_RELEASE_BASELINE.py`
- `python -m cap_protocol.scenarios.therapist_supervisor.runner --case all`
- `python -m cap_protocol.cli.run_benchmarks --iterations 100 --warmup 10`
- `python reference_grpc/run_demo.py`
- `python second_http/run_demo.py`
- `(cd third_impl/go_cap_adapter && go run . --fixtures testdata/cap_v1_interop.json --json)`

### Core Modules

- `cap_protocol.bindings.grpc_reference.cap_v1_core`: active gRPC v1 `CAPEnvelope` builders and executor-side directive validation.
- `cap_protocol.bindings.grpc_reference.cap_core`: v0.1 compatibility builders used by legacy fixture conformance and hardening tests.
- `cap_protocol.bindings.grpc_reference.cap_profile_med`: CAP-Med profile state, redaction, dimension extraction, and guard validation.
- `cap_protocol.bindings.http_json.cap_v1_types`: active HTTP/JSON v1 `CAPEnvelope` builders and executor-side directive validation.
- `cap_protocol.bindings.http_json.validators_v1`: active HTTP/JSON v1 schema and executor acceptance checks.
- `cap_protocol.bindings.http_json.cap_types`: v0.1 compatibility HTTP/JSON CAP primitive builders.
- `cap_protocol.bindings.http_json.validators`: v0.1 compatibility schema and executor acceptance checks.
- `cap_protocol.conformance.runner`: shared fixture conformance and CAP message schema validation.
- `cap_protocol.conformance.v1_runner`: smoke checks for implemented CAP v1 scaffolding; not a full v1 certification.
- `cap_protocol.benchmarks`: local deterministic CAP v1 benchmark harness for direct MCP/tool versus CAP-mediated execution, Edge PEP verification, Local PEP output gating, stream gating, and Android/iOS proxy scaffold paths. It reports p50/p95 latency, CPU-time proxy units, tracemalloc peak memory, streaming delay, and benchmark caveats.
- `cap_protocol.runtime.lifecycle`: machine-checkable lifecycle FSM definitions for envelope, directive, interrupt, execution, evidence, audit, and provenance states, with transition/trace validators and V1 conformance checks for illegal transitions.
- `cap_protocol.profiles.cap_med`: CAP-Med v1 runtime-profile reference fixture. It builds a structured `PrivacyBoundary`, closed `OperationalConstraints` with `profile_constraints.cap-med/v1`, unified `Capability` records, redacted `EvidenceRef` records, a signed-envelope hot-path smoke check through Edge PEP, Local PEP, and Supervisor Gateway, and deterministic profile conformance checks.
- `cap_protocol.profiles.inheritance`: deterministic profile inheritance and composition rules for parent-before-child ordering, constraint narrowing, conflict refusal, Core override protection, and CAP-SWE/Core profile composition.
- `cap_protocol.hardening.policy_engine`: portable policy-as-data evaluator with optional OPA hook.
- `cap_protocol.hardening.audit_store`: append-only hash-chain JSONL audit store.
- `cap_protocol.runtime.local_pep`: reusable CAP v1 Local PEP scaffold for deterministic typed refusals, Therapist/Supervisor privacy minimization, raw evidence-reference substitution with retention TTL metadata, local retention garbage collection, local NER redaction, embedding-only Supervisor egress, supervisor-overreach vetoes, service-backed signed policy-bundle fetch, offline policy-bundle cache fallback, output gating, and configurable streaming lookahead checks. It includes `ReferencePolicyRegistryService` for signed bundle distribution, per-session pinning, explicit hot update, revocation refusal, and audited emergency override modeling.
- `cap_protocol.runtime.retention`: shared deterministic retention helpers for `PrivacyBoundary.retention`, including raw local TTL defaults, audit-retention TTL defaults, expiry checks, audit-retained-until calculation, and content-minimized deletion records.
- `cap_protocol.runtime.redaction`: local-only NER redaction helpers for Supervisor and cross-boundary context minimization. `DeterministicLocalNERRedactor` is the dependency-free CI fallback for person, location, date, email, phone, SSN, medical, financial, credit-card, and IP-address tags; `LocalModelNERRedactor` adapts caller-supplied local NER providers while retaining deterministic fallback coverage; `redact_payload_for_supervisor(...)` preserves evidence refs and structural metadata while emitting audit-safe redaction summaries without raw source text.
- `cap_protocol.runtime.embeddings`: local-only text and voice embedding interfaces for Supervisor minimization. `DeterministicTextEmbeddingEncoder` and `DeterministicVoiceEmbeddingEncoder` provide fixed CI vectors without model downloads; `build_embedding_only_supervisor_payload(...)` projects raw transcript/audio sources into embeddings, aggregate dimensions, evidence refs, provenance refs, recipient-binding metadata, and `raw_content_logged=false` minimization summaries without forwarding raw text/audio.
- `cap_protocol.runtime.attested_local_pep`: deterministic attested isolated Local PEP registration scaffold. It defines challenge/response payloads, trusted provider contracts for deterministic TEE, Android Play Integrity, Apple App Attest, Secure Enclave, and TPM quote paths, detached-JWS test-double verification, production verifier hooks, replay detection, workload identity and Local PEP version binding, and a Control Plane registrar that refuses missing, expired, replayed, mismatched, untrusted, or production-verifier-missing attestations before Capability Registry publication.
- `cap_protocol.runtime.live_model_streaming`: reference live model-stream adapter. `LiveModelStreamSession` pulls chunks from `ScriptedModelStream` or optional stdlib `OllamaModelStream`, feeds them through `LocalPEP.open_stream_gate(...)`, releases safe buffered text on the 250 ms/50 token default window, pauses model pulls under sink backpressure, propagates abort signals to the source, and emits user-visible frames with audit/provenance refs without logging raw unsafe chunks.
- `cap_protocol.runtime.mobile_local_pep`: deterministic Android/iOS separately privileged proxy Local PEP scaffold. It declares `CapLocalPepProxyService` and `CapLocalPepProxyExtension` contracts, platform route controls, reproducible smoke checks for direct user output, network, raw-data egress, and local-tool bypass attempts, and manifest-shaped Android/iOS native wiring metadata. Native projects, platform entitlements, and device instrumentation remain external.
- `cap_protocol.runtime.ui_abort`: client-surface abort propagation contracts and local presentation adapters. It defines CLI and WebSocket-style replacement behavior for terminal stream aborts and transforms, plus precise Android and iOS `CapStreamAbort` contracts for native wrappers that are not implemented in this repository.
- `cap_protocol.runtime.ui_correction`: client-surface correction-frame UX contracts and local presentation adapters. It defines safe correction-frame semantics, CLI and WebSocket-style partial-region replacement plus safe annotation behavior, Android and iOS `CapStreamCorrection` contracts for native wrappers, and helpers that preserve partial-emission, original-audit, correction-audit, interrupt, execution-report, and provenance links without echoing unsafe original text.
- `cap_protocol.runtime.slow_path_classifier`: CAP-Med semantic slow-path classifier interface and local runtimes. `DeterministicCapMedSlowPathClassifier` provides CI-safe non-regex clinical-drift detection without model downloads; `OllamaSemanticClassifier` is an optional stdlib HTTP model-as-judge adapter for caller-supplied local Ollama models.
- `cap_protocol.runtime.edge_pep`: reusable CAP v1 Edge PEP scaffold for signed CAPEnvelope validation, TTL/skew checks, configured boundary PolicyRef checks, optional resolved AuthorityChain verification, privacy-boundary checks, and payload-ref privacy dereference hooks.
- `cap_protocol.runtime.controller`: decomposed CAP v1 Controller reference service. `ControllerService` forms signed `Directive` CAPEnvelopes from `ControllerIntent` objects and orchestrates subordinate boundaries only: `PDPGuardEvaluator` or another Guard evaluator owns policy decisions, `SessionRouter` owns routing, and optional `ObservabilityPlane` sinks own audit/telemetry/provenance. `LocalControllerClient`, `HTTPControllerClient`, and `start_controller_http_service` provide local and standard-library HTTP/JSON service boundaries; `legacy_center_compatibility_report` documents the preserved v0.1 combined Center mode.
- `cap_protocol.runtime.pdp_adapters`: deterministic CAP PDP adapter interface with `CAPPolicyRequest`, `PDPDecision`, `OPAPolicyAdapter`, and `CedarPolicyAdapter`. It maps CAP directives into OPA-shaped inputs or Cedar principal/action/resource/context authorization requests and marks the optional external Cedar runtime availability in decision metadata.
- `cap_protocol.runtime.warrants`: Biscuit-backed CAP AuthorityChainStep warrant helpers. `encode_biscuit_authority_step` turns a CAP step into a `biscuit-v2` holder-bound token, while `verify_biscuit_authority_step` decodes the canonical claims and enforces holder/capability/scope caveats before `verify_authority_chain` checks policy refs, expiry, attenuation, and revocation.
- `cap_protocol.runtime.observability`: deterministic CAP v1 observability-plane sink scaffold with separate audit, telemetry, and provenance sink interfaces, hash-chain audit durability/verification, signed audit operations through `SignedAuditSink`, external audit signing-provider hooks for caller-supplied or KMS/HSM-backed custody, retention/access metadata, replication retry/backpressure hooks, optional audit-as-delivery-precondition gating, lossy sampled telemetry behavior, independent provenance lineage recording, W3C PROV-JSONLD conversion through `W3CProvenanceSink`, queryable local `JsonlProvStore` lineage for session/evidence/authority/interrupt refs, OpenTelemetry `cap.*` attribute normalization, lifecycle attribute validation helpers, and a reference collector config path at `config/otel/collector-cap.yaml`.
- `cap_protocol.runtime.registry`: CAP v1 registry service interfaces, a SQLite-backed reference service, and cache-aware runtime clients. `CapabilityRegistry` is the unified registration surface for agent, tool, service, human, and policy subjects; kind-specific Agent/Tool/Service/Human/PolicySubject views normalize to the same `Capability` shape. Policy and Evidence registries add policy drift and evidence hash/freshness checks. The reference service persists registry records, audit events, revocation state, trust-domain federation routes, content-addressed Evidence blobs with `expires_at`, TTL garbage collection for expired backing content, and Ed25519 warrant-key directory entries; `ServiceBackedKeyRegistry` lets authority verification resolve active warrant keys and fail closed after key revocation or rotation.
- `cap_protocol.runtime.session_router`: CAP v1 Session Router reference component for the decomposed Control Plane. `SessionRouter` registers active participants per `session_id`, routes CAPEnvelope-like control messages only when sender and receiver are active participants in that session, supports atomic same-session fanout, refuses cross-session delivery attempts, and records audit/provenance route metadata without storing raw `payload` bodies.
- `cap_protocol.runtime.human_review`: CAP v1 Human Review reference integration. `HumanReviewService` turns `escalate` `InterruptDecision` payloads into Local PEP-minimized `HumanReviewRequest` tasks, optionally routes them through `SessionRouter`, calls a `HumanReviewPortal` stub, accepts structured approve/deny/transform/pause decisions, blocks portal requests for raw transcript/audio unless the active privacy policy permits them, and emits linked audit/provenance refs plus an `ExecutionReport`.
- `cap_protocol.runtime.workflow_engine`: Temporal-style workflow-engine composition sample. `TemporalCAPWorkflowSample` receives a signed `Directive` CAPEnvelope, verifies it through Edge PEP, routes it through `SessionRouter`, records workflow history linked to CAP `session_id` and `trace_id`, emits a retry-triggered `pause` `InterruptDecision`, emits a final `ExecutionReport`, and refuses tampered envelopes before activity execution. Run it with `python -m cap_protocol.runtime.workflow_engine`; it does not require `temporalio`.
- `cap_protocol.runtime.supervisor_gateway`: CAP v1 Supervisor Gateway enforcement core plus a CAP-facing reference service boundary. `SupervisorGatewayService` exposes a stable consultation contract, `HTTPSupervisorGatewayClient` and `LocalSupervisorGatewayClient` route calls through that contract, and `ModelSupervisorBackend`, `HumanPortalSupervisorBackend`, and `RuleEngineSupervisorBackend` sit behind the same backend interface. The service receives only Local PEP-minimized consultation context, including embedding-only payloads when requested and policy-allowed, translates structured backend output into `Directive` or `InterruptDecision` payloads, applies authority and Local PEP policy/privacy/safety vetoes, and emits audit/provenance refs.
- `cap_protocol.runtime.substrate_interop`: deterministic live MCP/A2A substrate interop scaffold. `LiveMCPServer` routes signed CAPEnvelope `Directive` payloads for MCP `tools/call` and `resources/read` through Edge PEP and service-backed MCP Capability discovery before invoking handlers, refuses forbidden tools before side effects, and emits `ExecutionReport` evidence refs. `LiveA2AAgent` advertises CAP v1 support in its AgentCard extension and accepts only A2A messages carrying an `application/cap-envelope+json` part that verifies through Edge PEP.
- `cap_protocol.runtime.workload_identity`: SPIFFE SVID parsing and validation helpers used by Edge PEP and AuthorityChain holder-binding checks.
- `cap_protocol.runtime.service_mesh`: deterministic Istio/Linkerd-style service-mesh composition helpers. It builds expected Kubernetes SPIFFE IDs, deployment manifests and labels for an application plus CAP Edge PEP sidecar beside an injected mesh sidecar, validates that mesh mTLS is consumed rather than reterminated by CAP, and provides an Edge PEP factory plus explicit local fallback topology for tests.
- `cap_protocol.schema.linkml`: LinkML authoring helpers and v1 LinkML/JSON Schema drift checks for the umbrella/core/domain schema structure.
- `cap_protocol.security.cap_crypto`: Ed25519 key material, detached signature verification, DSSE envelopes, and attestation helpers.
- `cap_protocol.security.transparency`: Sigstore/Rekor-style transparency-log scaffold. `LocalRekorTransparencyLog` publishes DSSE/in-toto release and AuthorityChainStep attestations into deterministic Rekor-compatible bundles with signed entry timestamps and Merkle inclusion proofs; `verify_transparency_bundle` verifies the bundle offline without calling external Rekor.
- `cap_protocol.security.cert_manager`: runtime-generated local mTLS certificates for non-production gRPC localhost fallback transport.

### Data Artifacts

- Compatibility implementation JSON schemas: `schemas/cap-core/v0.1/*.schema.json` and `schemas/cap-med/v0.1/*.schema.json`
- CAP v1 LinkML authoring schemas: `schemas/cap.yaml`, `schemas/core.yaml`, and `schemas/domains/*.yaml`
- Initial CAP v1 target schemas and examples: `schemas/cap-core/v1/*.schema.json` and `examples/cap-core/v1/*.json`
- Policies: `policies/cap_core_policy.json` and `policies/cap_med_policy.json`
- Fixtures: `src/cap_protocol/conformance/fixtures/adversarial.jsonl`
- Third implementation interop fixture suite: `third_impl/go_cap_adapter/testdata/cap_v1_interop.json`
- Authority-chain schema: `schemas/cap-core/v0.1/authority-chain-step.schema.json`
- Local benchmark artifacts: `docs/benchmarks/cap_v1_latency_mobile_budget.json` and `docs/benchmarks/cap_v1_latency_mobile_budget.md`

### Import Example

```python
from cap_protocol.bindings.grpc_reference.cap_v1_core import directive, evidence_ref
from cap_protocol.bindings.grpc_reference.schema_validation import validate_envelope

profile_ext = {
    "cap-med/v1": {
        "non_diagnostic_required": True,
        "non_prescriptive_required": True,
        "clinical_output_forbidden": True,
        "raw_transcript_upload_forbidden": True,
    }
}
evidence = evidence_ref(
    uri="cas://sha256/example",
    content="redacted evidence",
    media_type="application/json",
    producer_identity="spiffe://cytognosis.local/executor/example",
)
message = directive(
    session_id="session-example",
    directive_id="dir-example",
    question="What feels important to understand first?",
    section_id="opening_boundary",
    dimension_id="values_goals",
    evidence_required=[evidence],
    profile_ext=profile_ext,
)
assert validate_envelope(message)[0] is True
```


## Source: `reference_grpc/README.md`

## gRPC Reference Binding Wrapper

The implementation moved to `src/cap_protocol/bindings/grpc_reference`.

The wrapper now runs the migrated gRPC reference hot path, which carries v1 `CAPEnvelope` JSON over the checked-in gRPC/protobuf stream. v0.1 gRPC builders remain available only as compatibility fixtures inside the package.

Use either command:

```bash
python reference_grpc/run_demo.py
python -m cap_protocol.bindings.grpc_reference.run_demo
```


## Source: `second_http/README.md`

## HTTP/JSON Binding Wrapper

The implementation moved to `src/cap_protocol/bindings/http_json`. The active path now emits v1 `CAPEnvelope` JSON over HTTP; legacy v0.1 HTTP helpers remain available in that package for compatibility tests.

Use either command:

```bash
python second_http/run_demo.py
python -m cap_protocol.bindings.http_json.run_demo
```


## Source: `src/cap_protocol/bindings/grpc_reference/README.md`

## gRPC Reference Binding

This binding is the active CAP v1 hot-path migration for the local gRPC demo. The protobuf stream still carries generic JSON CAP payloads, but those payloads are now v1 `CAPEnvelope` objects with v1 `Directive`, `GuardDecision`, `InterruptDecision`, `RefusalMessage`, and `ExecutionReport` payloads.

The older v0.1 builders remain in `cap_core.py` for compatibility fixtures, hardening checks, and legacy schema tests. They are not used by the active gRPC demo path.

### Split files

- `cap_v1_core.py` - v1 CAPEnvelope and payload builders plus executor validation.
- `cap_core.py` - v0.1 compatibility builders and validation.
- `cap_profile_med.py` - non-diagnostic psychology profile state.
- `center_server.py` - Center as simplified Controller + Guard + Observer.
- `edge_client.py` - Edge as Executor.
- `conformance_v1.py` - gRPC v1 binding smoke checks.
- `conformance.py` and `*_legacy.py` adapters - v0.1 compatibility conformance path.
- `schema_validation.py` - v1 JSON Schema validation for gRPC CAPEnvelope traces.
- `run_demo.py` - local test runner.

### Strict Guard Semantics

```text
Unsafe/generic/bad Edge proposal
-> CAPEnvelope(GuardDecision deny) for original Edge proposal
-> Controller creates safe revised CAPEnvelope(Directive)
-> CAPEnvelope(GuardDecision allow_with_constraints) for revised Directive
-> Executor accepts/executes
-> CAPEnvelope(ExecutionReport)
-> CAPEnvelope(InterruptDecision pause) when the demo stop condition is met
```

### Run deterministic

```bash
python -m cap_protocol.bindings.grpc_reference.run_demo
```

Expected PASS checks include:

```text
PASS - cap_schema_validation_passed
PASS - cap_mcp_execution_demo_passed
PASS - cap_mcp_forbidden_tool_refused
PASS - cap_a2a_metadata_carriage_passed
PASS - cap_opa_policy_adapter_demo_passed
PASS - cap_otel_required_attributes_emitted
PASS - cap_prov_graph_exported
PASS - cap_conformance_smoke_passed
PASS - edge_pep_cross_boundary_enforced
PASS - edge_pep_verified_before_payload_use
PASS - edge_pep_refusal_matrix_passed
PASS - runtime_interrupts_linked
```

### Status

This is not a complete CAP v1 runtime. The gRPC binding now validates its CAP messages against `schemas/cap-core/v1/cap-envelope.schema.json` and the corresponding v1 payload schemas, selected user-output/local-tool paths route through the reusable Local PEP scaffold, demo cross-boundary CAP envelopes route through the reusable Edge PEP before payload use, structured privacy checks use the in-process PrivacyBoundary PDP helper, execution reports link to applied `InterruptDecision` refs, and the repository-level V1-C01 through V1-C15 deterministic scaffold gate is release-blocking. Production Edge PEP service-mesh deployment, registry-backed dereference, deployed local/central PDP services, production Local PEP trust modes, production Interrupt Manager deployment, and production key management remain separate tasks.


## Source: `src/cap_protocol/bindings/http_json/README.md`

## Cytognosis CAP v1 — Second Independent HTTP/JSON Implementation

This package is a second, intentionally separate implementation shape for the CAP demo. Its active HTTP/JSON hot path now uses CAP v1 `CAPEnvelope` objects and v1 Core payload objects while preserving the older v0.1 modules as compatibility evidence.

It does **not** use the previous gRPC/protobuf reference runtime. It uses:

- Python stdlib `ThreadingHTTPServer`
- JSON `CAPEnvelope` messages over HTTP
- independent v1 primitive builders in `cap_v1_types.py`
- independent v1 validation logic in `validators_v1.py`
- independent profile guard in `cap_profile_runtime.py`
- reusable Local PEP mediation for selected user-visible output, raw local observation handling, and MCP-style local-tool simulation
- reusable Edge PEP mediation for demo cross-boundary CAPEnvelope verification before payload use
- structured PrivacyBoundary PDP evaluation through the reusable in-process privacy helper
- explicit applied `InterruptDecision` refs on execution reports

The goal is to demonstrate that CAP control semantics can run over a transport-independent HTTP/JSON binding. The retained `cap_types.py`, `validators.py`, `integrations.py`, and `conformance.py` files remain v0.1 compatibility helpers.

### Run deterministic

```python
%cd /root
!rm -rf cytognosis_cap_v1_second_impl_http
!unzip -o cytognosis_cap_v1_second_impl_http.zip
%cd /root/cytognosis_cap_v1_second_impl_http
!python run_demo.py
```

### Run with two real separate E2B models

```python
!python run_demo.py --use-real-separate-e2b --require-real-model
```

### Expected checks

```text
PASS — second_independent_implementation
PASS — http_json_binding
PASS — cap_core_semantics_enabled
PASS — strict_guard_semantics
PASS — original_bad_proposal_denied
PASS — safe_revised_directive_allowed
PASS — cap_schema_validation_passed
PASS — cap_http_cross_boundary_schema_validation_passed
PASS — cap_conformance_smoke_passed
PASS — cap_mcp_execution_demo_passed
PASS — cap_mcp_forbidden_tool_refused
PASS — cap_a2a_metadata_carriage_passed
PASS — cap_opa_policy_adapter_demo_passed
PASS — cap_otel_required_attributes_emitted
PASS — cap_prov_graph_exported
PASS — local_pep_user_output_enforced
PASS — local_pep_local_tool_enforced
PASS — local_pep_bypass_refused
PASS — local_pep_audit_provenance_linked
PASS — edge_pep_cross_boundary_enforced
PASS — edge_pep_verified_before_payload_use
PASS — edge_pep_refusal_matrix_passed
PASS — runtime_interrupts_linked
PASS — models_are_not_shared
PASS — raw_transcripts_local_only
PASS — idempotency_duplicate_detected
PASS — stop_condition_met

FINAL RESULT: PASS
```


### v2 patch

This version renames `profile.py` to `cap_profile_runtime.py`.

Reason: a local file named `profile.py` shadows Python's standard-library `profile` module.
`torch` / `transformers` import `cProfile`, which imports stdlib `profile`; if the local file wins,
real-model mode fails with:

```text
AttributeError: module 'profile' has no attribute 'run'
```

So v2 avoids that namespace collision.
