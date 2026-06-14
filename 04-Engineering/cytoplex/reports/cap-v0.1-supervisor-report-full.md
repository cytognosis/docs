> **Status**: Active
> **Date**: 2026-06-14
> **Author**: @mohammadi
> **Audience**: engineers
> **Tags**: `cytoplex`, `cap`, `report`, `v0.1`, `comprehensive`

# Cytognosis CAP v0.1 Production-Candidate
## Comprehensive Supervisor Report

**Prepared by Ali Mohammadi**  
**Date:** May 2026  
**Status:** Production-candidate research package; not externally audited stable release.

# Executive Summary

CAP, the Cognitive Agent Protocol in the project history and now more precisely framed as a Control Authority Profile, is a transport-independent control layer for agentic systems. It defines the typed authority boundary between a Controller that forms or authorizes intent, a Guard that evaluates policy, safety, privacy, and domain constraints, and an Executor that acts only under bounded authority or emits a typed refusal. The current package is a production-candidate research implementation, not merely a concept note.

The central contribution is not another transport, tool-calling mechanism, workflow engine, or agent-discovery protocol. CAP is designed to sit above or beside existing systems such as MCP, A2A, policy engines, observability stacks, and provenance standards. Its role is to make agentic action explicitly authorized, evidence-bound, guardable, refusable, auditable, and profile-constrained.

The current package contains two executable bindings, a conformance suite, integration adapters, and production-hardening checks. The reference implementation uses gRPC/protobuf; the second implementation uses HTTP/JSON with independent primitive builders. Both run the same core semantics. The hardening layer verifies detached signatures, DSSE signed envelopes, in-toto-style attestations, adversarial fixtures, and hash-chain audit logs.

The intended supervisor review question is whether this narrowed framing - CAP as a Control Authority Profile rather than a standalone agent protocol - is academically defensible and whether the current evidence is sufficient for a systems, responsible-AI, or agent-architecture workshop paper.

| Dimension | Current status |
| --- | --- |
| Core framing | Control Authority Profile, not standalone transport/tool/discovery protocol |
| Executable bindings | gRPC/protobuf reference binding and HTTP/JSON independent binding |
| Core semantics | Directive, GuardDecision, RefusalMessage, ExecutionReport, DecisionRecord, EvidenceRef, AuthorityChain |
| Integration coverage | MCP, A2A, OPA-style policy, OpenTelemetry, W3C PROV, DSSE, in-toto-style attestations |
| Conformance | 28/28 implementation checks per executable binding; 33/33 hardening/conformance checks in production-hardening runner |
| Privacy boundary | Raw transcript remains local; center receives redacted/evidence-reference semantics |
| Current maturity | Production-candidate research package; external security review still required |

# 1. Problem and Motivation

Modern agentic systems increasingly separate high-level reasoning from tool execution, distributed task execution, edge inference, remote supervision, and external services. However, many frameworks still treat the boundary between deciding and acting as an implementation detail. Authority is often embedded implicitly in prompts, system messages, tool schemas, or application code. This creates several problems for high-stakes or research-sensitive systems:

- It can be unclear which component authorized an action.
- Policy and safety decisions are often not represented as first-class machine-readable objects.
- Executors may receive broad tool access without an explicit, attenuated authority scope.
- Refusals are often represented as strings or exceptions rather than typed protocol-level outcomes.
- Evidence used to justify an action may be stale, untrusted, over-shared, or detached from provenance.
- Audit traces may record what happened but not the authority chain that made it permissible.

These issues become especially important in Cytognosis because the platform is intended for non-diagnostic mental-health and behavioral phenotype modeling. In this context, the system must support useful assessment intelligence while explicitly avoiding clinical diagnosis, treatment recommendation, or raw sensitive transcript upload. CAP was designed to formalize this control boundary.

# 2. Project Objective

The objective of CAP v0.1 is to define and demonstrate a minimal, reusable authority semantics layer for agentic systems. The layer should be general enough for non-medical agentic systems, while also supporting a domain profile for non-diagnostic psychometric and behavioral assessment workflows.

The project therefore has two simultaneous goals:

- General systems goal: provide a transport-independent control profile for bounded agentic action.
- Cytognosis domain goal: provide a non-diagnostic CAP-Med profile that prevents diagnostic drift, raw transcript leakage, and unsafe clinical-style outputs in psychometric/phenotype workflows.

The package is intentionally framed as a production-candidate research artifact rather than a final standard. It demonstrates executable semantics, conformance, and hardening evidence while clearly identifying the external gates that remain before public stable release.

# 3. CAP Conceptual Model

CAP defines an authority contract between components that form intent and components that act. A CAP trace is expected to answer four questions: who authorized the action, under which constraints and policies it was authorized, which evidence justified or bounded the action, and why the executor accepted, refused, or reported the result.

| Role | Responsibility | Typical location in Cytognosis scenario |
| --- | --- | --- |
| Controller | Forms or approves an intended action and emits a bounded Directive. | Center/supervisor agent or higher-level reasoning service |
| Guard | Evaluates policy, safety, privacy, and domain constraints; emits GuardDecision. | Policy/safety layer attached to the controller or independent guard service |
| Executor | Verifies authority/evidence/constraints and either acts or emits RefusalMessage. | Edge interviewer, tool executor, or local agent |
| Observer | Records telemetry, provenance, decision records, and audit trail. | Tracing/audit/provenance infrastructure |

The key design decision is asymmetric authority. The Controller may propose or authorize actions, but the Executor is not a passive tool. It must verify the authority chain, guard outcome, evidence requirements, freshness constraints, allowed tools, and policy references before execution. If the action is invalid, unsafe, stale, unauthorized, or outside scope, it must refuse in a structured way.

# 4. Core CAP Primitives

CAP Core is intentionally small. It does not attempt to define model routing, tool schemas, long-running workflow persistence, identity issuance, or generic agent discovery. Instead, it defines the minimum set of typed objects needed to make authority and bounded execution explicit.

| Primitive | Purpose | Why it matters |
| --- | --- | --- |
| Directive | A bounded authorization from Controller to Executor. | Turns intent into a scoped, auditable, executable request. |
| GuardDecision | A policy/safety/privacy decision that can allow, deny, narrow, or escalate. | Prevents prompt-only guardrails from being the only safety mechanism. |
| RefusalMessage | A typed machine-actionable refusal from the Executor. | Makes negative outcomes structured and testable instead of string errors. |
| ExecutionReport | A report of completed, failed, aborted, or compensated execution. | Captures side effects, evidence produced, policy refs, and trace refs. |
| DecisionRecord | A non-chain-of-thought decision summary for audit/provenance. | Supports accountability without exposing hidden reasoning. |
| EvidenceRef | A reference to evidence with hash, freshness, producer, access policy, and redaction metadata. | Links execution to bounded evidence without over-sharing raw data. |
| AuthorityChain | A chain of authorized capability claims and scopes. | Prevents implicit prompt authority and supports delegation constraints. |

The most important semantic rule is that a Directive is not executable merely because it exists. It becomes executable only if its authority, constraints, evidence, guard decisions, expiry, and policy references validate under the profile rules.

# 5. Lifecycle and Execution Semantics

A typical CAP flow begins when a Controller drafts a Directive. A Guard evaluates the Directive and returns a GuardDecision. The Controller may then dispatch the original or narrowed Directive. The Executor verifies all requirements before acting. After execution or refusal, the Executor emits a structured report. The Observer maps the trace to telemetry and provenance records.

| Lifecycle step | Expected behavior |
| --- | --- |
| Draft | Controller creates a candidate Directive with target action, constraints, evidence requirements, and authority scope. |
| Guard evaluation | Guard returns allow, allow_with_constraints, deny, or escalate, with policy references and reason code. |
| Dispatch | Only an allowed or properly narrowed Directive is sent to an Executor. |
| Executor verification | Executor checks authority, expiry, signature/attestation, evidence hash/freshness/access, allowed tools, forbidden tools, and guard outcome. |
| Execution or refusal | Executor either performs the bounded action or emits typed refusal. |
| Reporting | Executor reports status, side effects, evidence produced, metrics, policy refs, and trace refs. |
| Observation/provenance | Observer emits OpenTelemetry-style attributes and W3C PROV-style artifacts. |

CAP uses deny-wins semantics: if any required GuardDecision denies the action, execution must be blocked. If a Guard returns allow_with_constraints, the effective Directive must be narrowed rather than expanded. This is important because the Guard must never increase authority beyond the Controller scope.

# 6. Scope: What CAP Is and Is Not

A major refinement in the final package is the narrowed positioning. CAP is not presented as a universal agent protocol. It is a profile that composes with surrounding infrastructure.

| CAP is not | Use or compose with instead | CAP relationship |
| --- | --- | --- |
| Transport protocol | HTTP, gRPC, WebSocket, SSE, NATS, Kafka, MQTT | CAP can be carried over these transports. |
| Tool-calling protocol | MCP | CAP constrains whether and how tools may be invoked. |
| Agent discovery / task lifecycle | A2A | CAP metadata can be carried inside A2A tasks. |
| Policy language | OPA/Rego, Cedar, or equivalent | CAP references and carries policy decisions. |
| Identity system | SPIFFE/SPIRE, DID, OAuth/OIDC, X.509, mTLS | CAP consumes identity and capability claims. |
| Audit/provenance store | OpenTelemetry, W3C PROV, event sourcing, transparency logs | CAP defines what should be emitted and linked. |
| Workflow engine | Temporal, LangGraph, other orchestration runtimes | CAP can be implemented within or across workflow runtimes. |

This distinction is important for novelty and defensibility. CAP is not competing with MCP or A2A. It adds an authority and evidence semantics layer that those systems do not by themselves define.

# 7. Domain Profile: CAP-Med v0.1

The package includes a domain profile referred to as CAP-Med v0.1. Despite the name, the profile is intentionally non-diagnostic. It exists to enforce boundaries relevant to psychometric, behavioral, and phenotype-modeling workflows. It blocks diagnosis, treatment/prescription behavior, and raw transcript upload while preserving enough redacted or structured information for research-oriented assessment intelligence.

| Profile rule | Implementation behavior |
| --- | --- |
| Non-diagnostic required | The system can discuss observations, dimensions, or supportive reflection, but must not label the user with a clinical diagnosis. |
| Clinical output forbidden | Diagnostic and treatment-planning outputs are blocked by policy/guard semantics. |
| Raw transcript upload forbidden | Raw user text is kept local to the edge; center receives redacted summaries, dimension vectors, flags, or evidence references. |
| Safety-aware question quality | Risk-related language must trigger safety/support-aware follow-up rather than generic questioning. |
| Evidence minimization | Only bounded evidence references and redacted observations should appear in cross-agent traces. |

This profile is a concrete demonstration of CAP profiles in general. The same Core could support other profiles, such as robotics, finance, enterprise workflow, education, or scientific data processing, as long as those profiles define their own domain-specific constraints and conformance cases.

# 8. Implementation Package

The final package is named cytognosis_cap_v01_production_candidate. It contains the specification documents, two executable bindings, policy and security components, conformance fixtures, notebooks/scripts for execution, and final review documents.

| Directory or file | Purpose |
| --- | --- |
| docs/ | CAP specification, examples, threat model, paper positioning, supervisor brief, final status, claims, release gates, implementation alignment. |
| reference_grpc/ | Reference implementation over gRPC/protobuf. |
| second_http/ | Second independent implementation over HTTP/JSON with independent primitive builders. |
| cap_conformance/ | Shared conformance runner and fixture-based checks. |
| security/ | Cryptographic support including Ed25519 detached-JWS, DSSE, in-toto-style verification, and runtime certificate handling. |
| hardening/ | Policy engine and hash-chain audit store support. |
| policies/ | Portable policy-as-data definitions for CAP Core and CAP-Med. |
| run_final_cap.py | One-command runner for reference implementation, HTTP implementation, and hardening checks. |
| run_production_hardening.py | Direct runner for hardening-only checks. |
| VERIFY_FINAL_PACKAGE.py | Pre-send verification script that checks required docs, stale labels, private key leakage, and release-gate consistency. |
| Colab/Modal support files | Notebook/script wrappers for running in hosted environments. |

The package verification script has been run successfully. It confirms that required final documents are present, stale demo labels have been removed, private key material is not packaged, and the earlier contradiction around second implementation release status has been removed.

# 9. Two Executable Bindings

A core claim of CAP is that it is transport-independent. The package supports this claim through two executable bindings. The purpose is not merely to duplicate code but to show that the same authority semantics can be exercised in different runtime shapes.

| Binding | Implementation evidence | Design significance |
| --- | --- | --- |
| gRPC/protobuf reference binding | reference_grpc/ with cap.proto, generated bindings, center/edge runtime, conformance, adapters, telemetry/provenance support. | Demonstrates a strongly typed reference transport binding. |
| HTTP/JSON independent binding | second_http/ with independent primitive builders, stdlib HTTP/JSON runtime, validators, integration layer, conformance. | Demonstrates that CAP Core semantics are not tied to gRPC/protobuf. |

The final run summary reports both bindings passing. The reference binding and independent HTTP/JSON binding each pass implementation-level schema validation, conformance smoke tests, MCP integration demo, A2A metadata carriage, OPA-style policy adapter, OpenTelemetry attributes, W3C PROV export, strict guard semantics, raw transcript minimization, idempotency checks, and stop conditions.

# 10. Production-Hardening Layer

Earlier drafts identified security and release-readiness gaps. The current production-candidate package implements several hardening mechanisms directly in the runner. These do not replace an external security review, but they provide concrete artifacts for review.

| Hardening element | Status in package |
| --- | --- |
| Runtime-generated local mTLS certificates | Implemented; no packaged private certificate keys. |
| Ed25519 detached-JWS verification | Implemented and verified. |
| DSSE signed envelopes | Implemented and verified. |
| in-toto-style attestation statements | Implemented and verified. |
| Portable policy-as-data backend | Implemented with optional OPA CLI hook. |
| Formal JSON Schema artifacts | Implemented. |
| Independent fixture-based conformance package | Implemented. |
| Deterministic adversarial fixtures | Implemented and passing. |
| Hash-chain append-only audit store | Implemented and valid in hardening report. |
| Tampered payload rejection | Implemented and passing. |
| Revoked key refusal | Implemented and passing. |

The production-hardening report indicates 33/33 hardening and independent conformance checks passing. It also explicitly states that third-party security review remains external, which is the correct claim boundary.

# 11. Evaluation and Validation Results

The final reported run indicates overall_pass: true, with both executable implementations and the production-hardening layer passing. The real-model run was configured to require real separate model instances for edge and center. The report indicates edge_model_was_real: true, center_model_was_real: true, models_are_shared: false, raw_data_received_by_center: false, and raw_included_in_audit: false.

| Evaluation area | Reported result |
| --- | --- |
| Reference gRPC/protobuf binding | PASS |
| Second HTTP/JSON implementation | PASS |
| Implementation conformance checks | 28/28 per executable binding |
| Production-hardening conformance checks | 33/33 |
| MCP constrained invocation | PASS |
| MCP forbidden tool refusal | PASS |
| A2A metadata carriage | PASS |
| OPA-style policy adapter / policy-as-data | PASS |
| OpenTelemetry cap.* attributes | PASS |
| W3C PROV graph export | PASS |
| Detached-JWS verification | PASS |
| DSSE verification | PASS |
| in-toto-style attestation verification | PASS |
| Hash-chain audit validation | PASS |
| Tampered payload rejection | PASS |
| Revoked key refusal | PASS |

The test scenario exercises a non-diagnostic supportive interview workflow. The edge agent observes local raw text, produces redacted observations and dimensions, proposes questions, and the guard/controller validates or replaces unsafe/generic/misaligned proposals. The final reports show clinical/diagnostic boundary violations, generic question failures, context alignment failures, and risk-safety question failures being blocked or narrowed as intended.

# 12. Conformance Coverage

The conformance suite is designed to test protocol/profile behavior rather than clinical quality. It checks whether implementations enforce authority, evidence, guard, refusal, telemetry, and profile constraints.

| Category | Representative checks |
| --- | --- |
| Valid execution | A valid Directive with evidence and authority can execute. |
| Temporal validity | Expired Directives and stale evidence are refused. |
| Authorization validity | Unauthorized Directives and invalid signatures are refused. |
| Evidence integrity | Missing evidence, hash mismatch, and access-denied evidence are refused. |
| Tool constraints | Forbidden tools and unsupported actions are refused. |
| Guard semantics | Guard deny blocks execution; allow_with_constraints narrows; conflicting guards resolve with deny-wins behavior. |
| Idempotency | Duplicate delivery/retry is detected. |
| Reporting | ExecutionReport integrity, side effects, compensation success/failure are represented. |
| Integrations | MCP invocation, A2A metadata carriage, OpenTelemetry attributes, W3C PROV mapping. |
| Privacy/safety | No hidden chain-of-thought in decision records; prompt injection in evidence blocked. |
| Hardening | DSSE required, detached-JWS verified, revoked key refused, hash-chain audit verifies, adversarial fixtures deterministic. |

This conformance coverage supports the claim that CAP has executable, testable semantics. It does not prove that any particular LLM-generated question is clinically useful, nor does it prove deployment security in a real organization.

# 13. Security, Trust, and Privacy Model

CAP assumes that no single layer is sufficient for safety. It provides structural authority semantics, but it still requires sandboxing, network controls, secure coding, model evaluation, production identity, and human governance where appropriate.

The main trust model is that a Directive must carry enough signed or attestable authority metadata for an Executor to verify scope and constraints before acting. Evidence must be referenced with integrity and freshness metadata. Guard decisions must be explicit and policy-referenced. Execution reports must describe side effects and produced evidence without leaking hidden chain-of-thought or raw sensitive evidence.

| Risk | CAP mitigation | Remaining operational mitigation |
| --- | --- | --- |
| Replay attack | Expiry, idempotency key, message id, and duplicate detection. | Short TTLs, synchronized clocks, replay caches. |
| Confused deputy | AuthorityChain scope and effective constraints. | Downstream per-directive authorization and least privilege. |
| Prompt injection through evidence | Evidence treated as untrusted; constraints parsed outside model context. | Prompt isolation, output validation, evidence sanitization. |
| Raw data leakage | EvidenceRef, redaction refs, confidentiality labels, raw transcript exclusion. | Privacy review, logging controls, redaction tests. |
| Compromised executor | Expected refusal/reporting semantics and audit trails. | Sandboxing, network egress controls, independent monitoring. |
| Compromised guard or broad policy | Multiple guards and deny-wins semantics can be used. | Policy review, guard diversity, key rotation. |
| Hidden chain-of-thought leakage | DecisionRecord uses non-CoT rationale summaries and reports hidden_cot_included=false. | Logging policy and provider-level controls. |

The package correctly avoids claiming that protocol conformance equals safety. CAP conformance means structural correctness of the authority lifecycle under the tested profile and fixtures.

# 14. Relationship to Existing Standards

A central argument for CAP is compositionality. CAP should not replace mature infrastructure. Instead, it specifies the missing authority layer that can be carried through or bound to these infrastructures.

| Existing system | What it provides | CAP contribution |
| --- | --- | --- |
| MCP | Tool, resource, and prompt access. | Determines whether and under what constraints an Executor may invoke tools. |
| A2A | Agent discovery and task lifecycle. | Carries authority, guard, evidence, and refusal metadata for asymmetric control. |
| OPA/Rego or Cedar | Policy evaluation. | Transports policy decisions and constraints into agent execution lifecycle. |
| OpenTelemetry | Observability and traces. | Defines cap.* semantic attributes for authority/evidence/control events. |
| W3C PROV | Provenance graph semantics. | Maps Directives, ExecutionReports, Guards, and DecisionRecords to provenance artifacts. |
| DSSE and in-toto | Signed envelopes and supply-chain attestations. | Attests CAP messages or authority artifacts. |
| FHIR/ReproSchema/Phenopackets | Health or assessment data models. | Governs the process that produces or transforms domain artifacts; does not replace those schemas. |
| LangGraph/Temporal/workflow engines | Runtime orchestration and durability. | Defines portable authority semantics across runtimes. |

This positioning makes the work more defensible: CAP is not an ecosystem replacement, but a missing semantic contract for authority and evidence-bound action.

# 15. Novelty and Research Contribution

The novelty of CAP is the combination of authority semantics, guard semantics, typed refusals, evidence-bound execution, and profile-specific constraints in a small transport-independent layer. Individually, many surrounding components exist: policy engines, tool protocols, traces, provenance graphs, cryptographic attestations, and workflow engines. CAP ties them into the agentic control path.

The most defensible contribution claims are:

- A minimal Controller/Guard/Executor/Observer control-authority model for agentic systems.
- A typed Directive lifecycle that prevents execution without valid authority, policy, evidence, freshness, and constraints.
- GuardDecision and RefusalMessage semantics as first-class machine-readable outcomes.
- EvidenceRef semantics for minimization, integrity, freshness, access policy, and provenance linkage.
- A non-diagnostic CAP-Med profile for psychometric and phenotype-modeling workflows.
- A conformance suite with semantic and adversarial fixtures.
- Two executable bindings plus production-hardening checks showing the profile is not tied to one transport.

The project should avoid claiming that CAP is a universal agent communication standard or a clinically validated mental-health system. The strongest claim is that CAP provides structural accountability and enforcement points for bounded agentic actions, demonstrated in a non-diagnostic assessment setting.

# 16. Claims and Non-Claims

| Supported claim | Evidence |
| --- | --- |
| CAP is a profile, not a transport. | Same semantics exercised over gRPC/protobuf and HTTP/JSON. |
| Controller/Guard/Executor separation is implemented. | Both runtimes emit Directive, GuardDecision, ExecutionReport, and RefusalMessage flows. |
| Guard semantics are enforced. | Deny blocks execution; allow_with_constraints narrows execution. |
| Executors can refuse with typed reasons. | Conformance covers expired, unauthorized, invalid signature, missing evidence, stale evidence, forbidden tool, and policy denied cases. |
| Evidence is integrity- and freshness-bound. | EvidenceRef contains hash, producer, redaction ref, access policy, expiry, and freshness metadata. |
| Raw transcript minimization is represented. | Reports indicate raw transcript excluded from center/audit. |
| CAP composes with existing standards. | Examples cover MCP, A2A, policy, telemetry, provenance, DSSE, and in-toto-style artifacts. |

| Non-claim | Why this matters |
| --- | --- |
| CAP does not guarantee clinical validity. | The current tests are structural and protocol-level, not clinical trials. |
| CAP does not diagnose, treat, or replace professionals. | CAP-Med explicitly enforces non-diagnostic boundaries. |
| CAP does not guarantee model truthfulness or hallucination prevention. | Semantic quality requires separate empirical evaluation. |
| CAP does not replace MCP, A2A, OPA, Cedar, OpenTelemetry, W3C PROV, DSSE, in-toto, FHIR, or workflow engines. | CAP composes with these systems. |
| CAP is not yet an externally audited stable standard. | Third-party security review and production integrations remain external gates. |

# 17. Reproducibility and Execution

The package is designed to be runnable with a small number of commands locally, in Google Colab, or in Modal-like hosted environments. The verification script should be used before sending or reviewing the package.

```bash
unzip cytognosis_cap_v01_production_candidate_final.zip
cd cytognosis_cap_v01_production_candidate
python VERIFY_FINAL_PACKAGE.py
```

A fast mock run can be used for structural verification without real model loading:

```bash
python run_final_cap.py --target both
```

The real-model run requires access to the configured model and sufficient compute/memory. A Hugging Face token is recommended for rate limits and faster downloads:

```bash
export HF_TOKEN=your_huggingface_token
python run_final_cap.py --target both --use-real-separate-e2b --require-real-model
```

The production-hardening runner can be executed separately:

```bash
python run_final_cap.py --hardening-only
# or
python run_production_hardening.py
```

Expected output paths include final_output/CAP_FINAL_SUMMARY.json and final_output/production_hardening/CAP_PRODUCTION_HARDENING_REPORT.json. Runtime artifacts are generated locally and should not include packaged private key material.

# 18. Remaining Work Before Stable Public Release

The remaining work is not ordinary code cleanup. It is mostly external validation and deployment integration. The current package is appropriate as a research production-candidate, but not as a fully audited public standard.

| Remaining gate | Reason it remains |
| --- | --- |
| Independent third-party security review | Must be conducted by reviewers outside the implementation team. |
| Production KMS/HSM integration | Requires deployment-specific key lifecycle, rotation, and hardware/cloud key policy. |
| Organization-specific OPA/Cedar policy deployment | Requires real organizational policies, ownership, approval workflow, and change control. |
| Live multi-organization MCP/A2A interoperability tests | Requires independent external agent stacks or organizations. |
| Domain semantic-quality evaluation | Requires task-specific datasets, human review criteria, and empirical evaluation beyond protocol conformance. |
| Latency and overhead benchmark | Needed for a stronger systems paper; compare CAP-mediated flow with direct execution. |
| Broader profile examples | Needed to show generality beyond CAP-Med, such as finance, robotics, or scientific data agents. |

# 19. Recommended Paper Framing

The best paper framing is not “we built a new agent protocol.” The stronger and more accurate framing is “we define a Control Authority Profile for evidence-bound, guardable, refusable, and auditable agentic action.”

Recommended working title: CAP: A Control Authority Profile for Evidence-Bound and Non-Diagnostic Agentic Assessment.

Alternative titles:

- A Control Authority Profile for Privacy-Preserving Psychometric Agent Systems.
- Evidence-Bound Agentic Assessment: A Control Authority Profile for Non-Diagnostic Behavioral Phenotyping.
- Guardable, Refusable, and Auditable Agentic Assessment via a Control Authority Profile.

A first submission should be a systems-position or workshop paper. It should evaluate structural conformance, authority enforcement, refusal correctness, privacy boundary preservation, and provenance completeness. It should not claim clinical efficacy.

| Paper section | Suggested content |
| --- | --- |
| Introduction | Agentic systems need explicit authority boundaries between deciding and acting. |
| Background | Limitations of tool-centric and task-centric agent protocols. |
| Requirements | Non-diagnostic psychometric/phenotype workflows and privacy-preserving edge supervision. |
| CAP Core | Roles, primitives, lifecycle, and authority/evidence semantics. |
| CAP-Med profile | Non-diagnostic boundary, raw data minimization, safety-aware constraints. |
| Implementation | gRPC/protobuf reference binding, HTTP/JSON independent binding, hardening layer. |
| Evaluation | Conformance suite, adversarial fixtures, hardening checks, integration tests. |
| Limitations | No clinical validation, no guarantee of model truthfulness, external security review pending. |
| Discussion | How CAP composes with MCP, A2A, OPA/Cedar, OTel, W3C PROV, DSSE, and in-toto. |

# 20. Suggested Supervisor Review Questions

The most useful supervisor feedback would be on the conceptual contribution, research framing, and evaluation plan rather than minor code style. Recommended questions to ask the supervisor are:

- Is the narrowed framing of CAP as a Control Authority Profile academically defensible?
- Is the distinction from MCP, A2A, policy engines, workflow engines, and provenance systems clear enough?
- Are the Core primitives minimal, or should any primitive be removed or merged?
- Is CAP-Med a good first profile, or should the first paper emphasize a more general domain first?
- Are the current two bindings and conformance suite enough for a workshop paper?
- What additional evaluation would make this credible as a systems paper?
- Which claims should be weakened before submission to avoid overclaiming?
- Which venue type is most appropriate: responsible AI, agent systems, digital health AI, or distributed systems for AI?

# 21. Recommended Next Steps

The next steps should focus on strengthening research validity, not only adding more features.

| Priority | Action | Rationale |
| --- | --- | --- |
| High | Prepare a concise paper draft using the Control Authority Profile framing. | The implementation is now strong enough to support a research narrative. |
| High | Run an external security review or at least an internal red-team review by someone outside the implementation author. | Stable release requires independent review. |
| High | Create a compact benchmark table: direct execution vs CAP-mediated execution. | Needed for systems credibility. |
| Medium | Add a third minimal implementation or external adapter. | Further supports transport/framework independence. |
| Medium | Add a non-medical profile example. | Strengthens the claim that CAP is general. |
| Medium | Develop a formal specification for the lifecycle FSM and profile inheritance rules. | Improves standardization potential. |
| Medium | Build a synthetic evaluation dataset for CAP-Med semantic quality. | Separates structural conformance from model-output quality. |
| Low | Improve developer documentation and examples. | Useful after core research framing is accepted. |

# 22. Conclusion

CAP v0.1 is now a coherent production-candidate research package. Its strongest contribution is a small, transport-independent authority semantics layer for agentic systems. It makes agentic actions explicitly authorized, evidence-bound, guardable, refusable, and auditable. The current implementation evidence is meaningful: two executable bindings, shared conformance, integration adapters, hardening checks, adversarial fixtures, and verification scripts all support the claim that the design is implementable and testable.

The main caution is that CAP should not be oversold. It does not guarantee clinical validity, model truthfulness, or production deployment security. It is best presented as a systems and architecture contribution that creates enforceable control points around agentic behavior. With the current package, the project appears ready for supervisor review and likely suitable as the basis for a workshop or position paper, provided the paper keeps the claims narrow and the limitations explicit.

# Appendix A - Key Artifacts for Review

| Artifact | Purpose |
| --- | --- |
| docs/CAP_SUPERVISOR_BRIEF_FINAL.md | Short supervisor-ready summary and novelty framing. |
| docs/CAP_FINAL_STATUS.md | Current status, implemented gates, and external gates. |
| docs/CAP_CLAIMS.md | Supported claims and non-claims. |
| docs/CAP_IMPLEMENTATION_ALIGNMENT.md | Mapping from document claims to implementation evidence. |
| docs/CAP_RELEASE_GATES.md | Completed and remaining release gates. |
| docs/CAP_paper_positioning.md | Recommended paper thesis, contribution claims, evaluation design, and reviewer concerns. |
| docs/CAP_threat_model.md | Threat model and residual risk statement. |
| run_final_cap.py | One-command runner for both implementations and hardening. |
| run_production_hardening.py | Direct hardening runner. |
| VERIFY_FINAL_PACKAGE.py | Pre-send verification script. |

# Appendix B - Informative References and Standards

The CAP documents position the work as compositional with, rather than replacement for, the following standards and systems:

- Model Context Protocol (MCP): tool, resource, and prompt access.
- Agent-to-Agent (A2A): agent discovery and task lifecycle.
- OPA/Rego and Cedar: policy evaluation.
- SPIFFE/SPIRE, X.509, and mTLS: workload identity and transport authentication.
- OpenTelemetry: observability and semantic event attributes.
- W3C PROV: provenance graph representation.
- DSSE and in-toto: signed envelopes and attestation patterns.
- FHIR, ReproSchema, and Phenopackets: possible downstream domain-data models rather than CAP replacements.

In the report and future paper, these systems should be described as adjacent infrastructure. CAP should be described as the authority and evidence-bound control profile that composes with them.
