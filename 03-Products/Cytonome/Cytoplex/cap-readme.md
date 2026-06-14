> **Status**: Active
> **Date**: 2026-06-14
> **Author**: @mohammadi
> **Audience**: engineers, stakeholders
> **Tags**: `cytoplex`, `cap`, `overview`

# CAP — Control Authority Protocol

**A supervisory control plane and authority protocol for agentic systems.**

**Architecture target:** v1.0 consolidated baseline
**Implementation status:** v0.1 production-candidate subset
**Status:** Candidate documentation and executable reference package
**Scope:** General-purpose interoperability profile; transport-independent; framework-independent.

**Baseline V1 document set:** `docs/v1_baseline/00_INDEX.md` is the consolidated capped V1 Markdown set generated from the current repository documents, schemas, examples, prompt archive, and artifact inventory.

## What CAP is

CAP v1 defines a **runtime supervisory control plane** for agentic systems: a runtime governance protocol and semantic enforcement layer above existing transports and frameworks. It sits one layer above A2A, MCP, HTTP, gRPC, WebSocket, local IPC, OPA/Cedar, SPIFFE/OIDC/mTLS, OpenTelemetry, W3C PROV, and workflow engines. CAP adds the semantics those layers do not own: explicit authority, evidence references, privacy boundaries, streaming interruption, typed refusal, execution reporting, audit, and provenance.

The checked-in implementation currently exercises the smaller v0.1 Control Authority Profile subset. That subset is still useful: it proves the Controller-to-Executor authority boundary and produces deterministic conformance evidence across two bindings. It should not be read as a complete CAP v1 runtime.

A CAP trace answers four questions that ordinary agent frameworks often leave implicit:

1. **Who authorized this action?**
2. **Under which constraints and policies was it authorized?**
3. **Which evidence justified or bounded the action?**
4. **Why did the Executor accept, refuse, or report the result?**

CAP does this through a small set of typed objects:

- `Directive`: a bounded authorization from a Controller to an Executor.
- `GuardDecision`: a policy/safety/privacy decision that allows, denies, narrows, or escalates a Directive.
- `InterruptDecision`: the v1 target command for allow, deny, transform, constrain, pause, escalate, or reroute behavior.
- `RefusalMessage`: a typed, machine-actionable rejection from an Executor.
- `ExecutionReport`: the bounded result of executing a Directive.
- `EvidenceRef`, `AuthorityChain`, `PolicyRef`, `PrivacyBoundary`, `Capability`, and `OperationalConstraints`: the v1 target support objects for verification, privacy, and profile portability.
- Optional `DecisionRecord`: a non-chain-of-thought provenance artifact explaining a decision at a safe level of abstraction.

CAP does **not** define the transport, tool call, workflow engine, policy language, audit store, or identity system. It defines the semantic layer that lets those systems compose safely.

## CAP v1 architecture target

The v1 architecture is a hybrid two-tier, three-plane system:

- The local tier contains Local PEPs near agents, tools, local memory, and user surfaces. They enforce local privacy, redaction, typed refusal, offline fallback, and streaming interruption before content reaches a user.
- The federated tier contains a decomposed central Control Plane: Controller, Supervisor Gateway, Session Router, logical Interrupt Manager, PDP adapters, and Human Review integration. Edge PEPs sit at network boundaries and inspect CAP envelopes crossing services, agents, or tools.
- The data plane carries A2A, MCP, HTTP, gRPC, WebSocket, and local IPC traffic under CAP enforcement. CAP governs this traffic but is not the data-plane transport.
- The control plane carries `CAPEnvelope`, `Directive`, `GuardDecision`, `InterruptDecision`, `RefusalMessage`, and `ExecutionReport` messages used for synchronous authority and enforcement decisions.
- The observability plane carries signed audit records, OpenTelemetry telemetry, and W3C PROV graphs independently of the control plane. It is not the hot-path policy decision loop.
- PDPs evaluate policy locally and centrally, while Agent, Tool, Capability, Policy, and Evidence registries are independently deployable and cacheable.

The motivating scenario is a profile example, not CAP Core: a mobile **Therapist** persona used as the local interviewer. The Therapist remains supportive, non-diagnostic, non-prescriptive, and privacy-preserving. The main/central **Supervisor** is an authority participant behind a Supervisor Gateway; CAP separates that authority role from the gateway endpoint and from the model, human, or rule engine behind it. Supervisor strategy and review are still subject to Local PEP vetoes for privacy, non-diagnostic, jurisdiction, and safety policy. Current Supervisor context preparation substitutes raw transcript/audio into local EvidenceRefs, applies local-only NER redaction, can project text/voice sources into local embeddings plus aggregate dimensions before gateway backend access, and can delete expired raw backing content according to `PrivacyBoundary.retention` while preserving content-minimized audit/provenance records.

For visual architecture context, see `architecture.md#architecture-diagrams`. Those diagrams are target-topology documentation and include captions that distinguish the v0.1 implemented subset from the v1 migration target.

## Minimal end-to-end flow

```text
Controller drafts Directive
        ↓
Guard evaluates policy and emits GuardDecision
        ↓
Controller dispatches approved/narrowed Directive
        ↓
Executor verifies authority, evidence, policy, freshness, constraints
        ↓
Executor either refuses or executes under bounds
        ↓
Executor emits ExecutionReport with evidence and side effects
        ↓
Observer maps the trace to OpenTelemetry and W3C PROV
```

## What CAP is not

CAP is **not** a standalone end-to-end wire protocol. It composes with existing standards and infrastructure.

| CAP is not | Use instead |
|---|---|
| Transport protocol | HTTP, gRPC, WebSocket, SSE, NATS, Kafka, MQTT, etc. |
| Tool-calling protocol | MCP |
| Peer-agent discovery / generic task lifecycle | A2A |
| Policy language or policy engine | OPA/Rego, Cedar, or equivalent |
| Identity / authentication system | SPIFFE/SPIRE, DID, OAuth/OIDC, X.509, mTLS |
| Audit log or trace store | OpenTelemetry, W3C PROV, event sourcing, transparency logs |
| Workflow engine | Temporal, LangGraph, Microsoft Agent Framework, etc. |
| Supply-chain attestation system | DSSE, in-toto, SLSA, Sigstore/Rekor, or equivalent |

## Strict scope test

A feature belongs in CAP Core only if it expresses a **supervisory control semantic** that cannot be cleanly represented by the surrounding ecosystem: authority, evidence, privacy boundary, interrupt, refusal, execution reporting, or lifecycle observation.

If a feature handles transport retries, agent directory lookup, generic task delegation, generic tool schemas, hash-chained audit storage, workflow checkpointing, key issuance, model routing, or arbitrary voting algorithms, it does **not** belong in CAP Core.

## Reading order

1. `CAP_01_foundations.md` — problem statement, scope, v1 thesis, and relationship to the ecosystem.
2. `CAP_02_core_model.md` — roles, envelope, lifecycle FSM, authority/evidence placement rules.
3. `CAP_03_primitives.md` — primitives and core data structures.
4. `CAP_04_security_trust_evidence.md` — threat model summary, trust assumptions, evidence security, replay semantics.
5. `CAP_05_integrations.md` — mappings to A2A, MCP, OPA/Cedar, OpenTelemetry, W3C PROV, DSSE/in-toto.
6. `CAP_06_conformance.md` — semantic and adversarial conformance tests.
7. `CAP_07_profiles_roadmap.md` — profile model, roadmap, release criteria, risk register.
8. `CAP_appendix_schemas.md` — v0.1 JSON Schema Draft 2020-12 skeletons plus pointers to v1 LinkML/JSON schema artifacts.
9. `CAP_examples.md` — JSON examples and realistic flows.
10. `CAP_threat_model.md` — detailed threat table.
11. `security_review/README.md` — independent security review starting packet; the external review gate remains open until review completion and critical-finding remediation.
12. `kms_hsm/README.md` — production KMS/HSM custody and operations plan; deployment-owned production key evidence remains required.
13. `policy_deployment/README.md` — organization-specific OPA/Cedar policy deployment guide; organization-owned policy evidence remains required.
14. `mcp_a2a_interop/README.md` — multi-organization MCP/A2A interop plan and report template; external partner evidence remains required.
15. `domain_semantic_quality/README.md` — domain semantic-quality evaluation harness, reviewer rubric, and synthetic fixture guidance; external expert evidence remains required.
16. `regulated_profile_review/README.md` — CAP-Med or other regulated-profile review packet; external profile review remains required.
17. `CAP_changelog_from_previous_draft.md` — what changed from the older protocol-shaped draft.
18. `CAP_supervisor_brief.md` — supervisor-ready executive brief, novelty claim, and research framing.
19. `CAP_paper_positioning.md` — paper thesis, contribution claims, evaluation plan, and limitations.
20. `CAP_references.md` — consolidated references and standards links.
21. `CAP_v1_TASKS.md` — gap analysis and implementation backlog for the v1 target architecture.

## Design status

This package is a **v0.1 production-candidate implementation with partial v1 runtime migration** plus **v1 architecture documentation and initial v1 scaffolding**, not a final externally audited standard. The gRPC/protobuf reference binding and independently structured HTTP/JSON binding now carry v1 `CAPEnvelope` objects on their active hot paths; a local Go third-implementation adapter validates shared CAPEnvelope/JCS/signature fixtures; shared fixture conformance and retained legacy helpers remain v0.1 compatibility evidence. Initial v1 schemas, examples, Local PEP, local NER redaction, embedding-only Supervisor egress, retention TTL deletion, machine-checkable lifecycle FSM/profile-inheritance rules, CAP-Med v1 runtime-profile evidence, CAP-SWE non-medical reference profile evidence, local latency/mobile-resource benchmark artifacts, Edge PEP, structured privacy PDP, a decomposed Controller reference service, Supervisor Gateway, service-mesh composition helpers, live local MCP/A2A substrate interop, Temporal-style workflow-engine composition sample, Sigstore/Rekor-style transparency-log scaffold, reference registry services, observability sink scaffolds, and smoke checks exist, including service-backed Agent/Tool discovery, signed policy-bundle distribution, content-addressed Evidence storage with backing-content TTL deletion, signed audit-operation scaffolding, W3C PROV-JSONLD store scaffolding, reference OpenTelemetry lifecycle attribute coverage, and local offline transparency-bundle verification. The Controller service owns intent formation/orchestration and delegates policy evaluation, routing, and observability to injected Guard/PDP, Session Router, and sink interfaces while the old combined Center remains a v0.1 legacy compatibility path. Full CAP v1 runtime migration remains open and is tracked in `CAP_v1_TASKS.md`.

Where the v1 source material calls the architecture an "implementation-ready architecture baseline," read that as a specification baseline ready to guide implementation. It is not a claim that this repository already contains a complete CAP v1 runtime.

See also:

- `CAP_FINAL_STATUS.md`
- `CAP_CLAIMS.md`
- `CAP_RELEASE_GATES.md`
- `CAP_IMPLEMENTATION_ALIGNMENT.md`

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


## Supervisor-facing summary

For supervisor review, start with `CAP_supervisor_brief.md`. The core message is:

> CAP is not proposed as a new transport, tool-calling, or agent-discovery protocol. CAP is proposed as a supervisory Control Authority Protocol: a runtime control layer that makes agentic actions explicitly authorized, evidence-bound, privacy-bounded, interruptible, refusable, and auditable.

The most defensible near-term research contribution is not "a universal agent protocol." It is a structurally testable supervisory control architecture for non-diagnostic, privacy-preserving psychometric agent systems, with reusable general semantics and a Cytognosis/Neuroverse domain profile.
