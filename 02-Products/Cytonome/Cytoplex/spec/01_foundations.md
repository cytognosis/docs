# CAP_01 — Foundations

## 1. Problem statement

Modern agent systems have rapidly standardized important boundaries:

- MCP standardizes how a host/client interacts with tools, resources, and prompts.
- A2A standardizes peer-agent discovery, messages, tasks, artifacts, and transport bindings.
- Workflow frameworks provide state machines, durable execution, retries, checkpoints, and human approval tasks.
- Observability stacks provide traces, logs, metrics, and provenance graphs.
- Policy engines provide machine-evaluable authorization and governance decisions.

A gap remains: **runtime supervisory control across the component that decides, the component that acts, the component that enforces local policy, and the infrastructure that records evidence and provenance**.

Without a typed supervisory layer, authority is usually hidden in orchestration code, prompts, or middleware. The Executor often cannot determine whether a request was approved by the right authority, whether required evidence is fresh, whether the request is still valid, or whether a policy decision narrowed the action. Local enforcement points often cannot prove why an output was allowed, transformed, interrupted, or refused. Refusals are often strings or exceptions rather than structured, auditable protocol events.

CAP exists to make this control boundary explicit and portable.

## 2. Core thesis

CAP v1 is a **supervisory control plane and runtime governance protocol**. It defines how Controllers, Supervisors, Guards, PDPs, PEPs, Executors, Observers, and registries compose without replacing the lower-level systems they ride on. CAP owns supervisory semantics: authority, evidence, privacy boundaries, interruption, refusal, execution reporting, audit, and provenance.

The repository implementation is the smaller CAP v0.1 production-candidate subset. It proves the Controller-to-Executor authority boundary and should be treated as implementation evidence, not as the full v1 architecture.

## 2.1 Architecture shape

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

## 3. CAP guarantees and non-guarantees

### CAP guarantees, if implemented correctly

- A Directive can be validated against explicit constraints.
- An Executor can refuse with typed, machine-actionable reason codes.
- Guard decisions can block, narrow, or escalate a Directive.
- Evidence and policy references can be attached to the decision boundary.
- Observers can reconstruct the structural lifecycle of an action.
- Hidden chain-of-thought is not required to audit structural behavior.

### CAP does not guarantee

- The Controller's reasoning is correct.
- The Guard's policy is complete or safe.
- The Executor is honest if fully compromised.
- External tools return correct or non-poisoned data.
- LLM outputs can be replayed bit-for-bit.
- A CAP-conformant system is automatically safe, compliant, or clinically/financially valid.

CAP provides **structural accountability**, not semantic infallibility.

## 4. Relationship to MCP

CAP does not define tool schemas or tool invocation. A CAP `Directive.action` may reference an MCP tool identifier or MCP resource, but the Executor uses MCP to list tools, call tools, access resources, and receive results. CAP constrains **whether and how** the Executor is allowed to use that tool.

CAP adds authority context around MCP calls:

```text
CAP Directive -> Executor authorization boundary -> MCP tools/call -> CAP ExecutionReport
```

## 5. Relationship to A2A

CAP does not define peer-agent discovery, generic delegation, or task lifecycle. A2A Tasks can carry CAP metadata when a delegated task requires Controller-to-Executor authority semantics.

CAP adds semantic restrictions to A2A work units:

```text
A2A Task = durable cross-agent work container
CAP Directive = authority payload inside or referenced by the task
```

## 6. Relationship to policy engines

CAP does not define quorum, weighted voting, safety veto, policy veto, or human-required algorithms in Core. Those are policy decisions.

CAP carries `PolicyRef` and `GuardDecision`; engines such as OPA/Rego or Cedar evaluate policy. A Guard is the CAP-facing adapter that converts a policy decision into a portable CAP object.

## 7. Relationship to observability and provenance

CAP does not define an audit store or custom hash chain. It defines semantic events that can be emitted as OpenTelemetry spans/events and mapped into W3C PROV.

- OpenTelemetry answers operational questions: latency, errors, lifecycle state transitions.
- W3C PROV answers provenance questions: which agents, activities, plans, evidence, and generated entities participated.
- in-toto/DSSE/SLSA/transparency logs answer tamper-evidence and attestation questions.

In CAP v1, audit, telemetry, and provenance are a separate observability plane. They have different latency, retention, integrity, and backpressure properties and should not be folded into the synchronous Control Plane.

## 8. Relationship to workflow frameworks

CAP does not replace LangGraph, Temporal, Microsoft Agent Framework, CrewAI, AutoGen, or Semantic Kernel. Those frameworks own orchestration, retries, local state, human workflow, persistence, and internal graph execution.

CAP messages can be emitted **by** workflow nodes or across framework boundaries when independent components must interoperate.

## 9. Novelty claim

CAP is novel only in its narrow composition:

> A portable supervisory control plane for agentic systems that combines local enforcement, central supervision, cryptographic authority, evidence references, privacy boundaries, streaming interruption, structured refusals, execution reports, and lifecycle observability without replacing existing transports, tool protocols, identity systems, policy engines, or workflow engines.

CAP is not novel as a transport, discovery mechanism, policy engine, audit system, or workflow runtime; those belong outside CAP Core.

## 10. Therapist/Supervisor scenario

The default motivating scenario uses a mobile **Therapist** persona as the local interviewer. This is a profile/scenario label only, not CAP Core and not a clinical authority claim. It does not permit diagnosis, treatment advice, prescription, or claims of clinical validity.

The central/main **Supervisor** provides strategy, higher-order review, and structured directives through a Supervisor Gateway. CAP v1 separates three meanings that older drafts overloaded:

- the Supervisor authority role that may issue or approve directives;
- the Supervisor Gateway service endpoint that validates and mediates supervisor output;
- the model, human, or rule engine used behind that gateway.

The Local PEP can refuse Supervisor directives that violate local policy, privacy, jurisdiction, evidence, non-diagnostic, non-prescriptive, or safety constraints.

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


## 11. Novelty and paper positioning

CAP's novelty must be stated narrowly. CAP is not novel as a transport, tool-calling mechanism, identity system, audit store, or generic agent-discovery protocol. Those layers are delegated to existing infrastructure.

CAP is novel as a **supervisory control-authority protocol** for agentic systems. Its contribution is the explicit, typed boundary between intent, enforcement, execution, and observation:

- a `Controller` cannot merely prompt an action; it must issue a bounded `Directive`;
- a `Guard` can allow, deny, narrow, or escalate the proposed action;
- a Local PEP or Edge PEP can enforce a policy result before the action crosses a trust boundary;
- an `Executor` must validate authority, evidence, policy, freshness, and constraints before acting;
- an `Executor` can return a typed `RefusalMessage` instead of a free-form error;
- every execution result is connected to evidence, side effects, and provenance.

For Cytognosis/Neuroverse, the domain-specific novelty is stronger: CAP becomes a profile for non-diagnostic psychometric assessment, signed assessment configurations, privacy-preserving edge-to-supervisor handoff, and reproducible phenotype-generation traces. The profile should therefore focus on psychometric session state, non-diagnostic guard policies, evidence minimization, and phenotype provenance rather than communication plumbing.

### Defensible paper claim

A defensible paper claim is:

> We define and evaluate a Control Authority Protocol for evidence-bound, privacy-preserving, non-diagnostic psychometric agent systems. The protocol composes with MCP for tools, A2A for external agent tasks, OPA/Cedar for policy, and OpenTelemetry/W3C PROV for observability and provenance.

A weak claim to avoid is:

> We introduce a new universal protocol for agent communication.
