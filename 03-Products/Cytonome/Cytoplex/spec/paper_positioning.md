> **Status**: Active
> **Date**: 2026-06-14
> **Author**: @mohammadi
> **Audience**: engineers
> **Tags**: `cap`, `cytoplex`, `spec`

# CAP Paper Positioning

## 1. Recommended paper framing

CAP should be submitted as a supervisory protocol and systems-architecture contribution, not as a universal agent communication standard or as a fully implemented v1 runtime.

Recommended title:

> CAP: A Control Authority Protocol for Evidence-Bound and Non-Diagnostic Agentic Assessment

Alternative titles:

- A Control Authority Protocol for Privacy-Preserving Psychometric Agent Systems
- Evidence-Bound Agentic Assessment: A Control Authority Protocol for Non-Diagnostic Behavioral Phenotyping
- Guardable, Refusable, and Auditable Agentic Assessment via a Control Authority Protocol

## 2. Thesis

Current agent systems can call tools and delegate tasks, but they often lack a portable, typed supervisory boundary between deciding, enforcing, and acting. CAP v1 defines that boundary as a runtime governance protocol and semantic enforcement layer. In the Cytognosis/Neuroverse setting, the current v0.1 Profile subset specializes that boundary for non-diagnostic psychometric assessment, privacy-preserving edge-to-supervisor handoff, and reproducible phenotype-generation traces.

## 3. Primary contribution claims

1. **Control authority model:** A minimal Controller/Guard/Executor/Observer role model.
2. **Evidence-bound Directive lifecycle:** A finite state machine that prevents execution without valid authority, policy, evidence, freshness, and constraints.
3. **Typed refusal and guard semantics:** Machine-actionable negative outcomes rather than string errors or prompt-only guardrails.
4. **Non-diagnostic assessment profile:** A profile that encodes claim boundaries and blocks diagnostic drift.
5. **Provenance-first phenotype trace:** A mapping from evidence, policy, domain config, and execution to OpenTelemetry and W3C PROV.
6. **Conformance suite:** Semantic and adversarial tests for interoperability and safety-boundary behavior.
7. **Executable production-candidate package:** A gRPC/protobuf reference binding, an independently structured HTTP/JSON binding, a local Go third-implementation CAPEnvelope/JCS fixture adapter, and a production-hardening runner with detached-JWS, DSSE, in-toto-style, adversarial-fixture, and audit-chain checks.

## 4. Non-contributions

The paper must explicitly say CAP does not contribute:

- a new transport;
- a new tool-calling protocol;
- a new agent-discovery protocol;
- a new workflow runtime;
- a new identity/key management system;
- a new clinical data standard;
- a claim of clinical efficacy;
- a claim that this repository already contains a complete CAP v1 runtime.

## 5. Related work positioning

| Existing system | What it solves | Why CAP still exists |
|---|---|---|
| MCP | Tool/resource/prompt access. | CAP governs whether and under what constraints an Executor may invoke tools. |
| A2A | Agent discovery and task lifecycle. | CAP defines asymmetric authority, guard decisions, refusal, and evidence-bound execution. |
| OPA/Rego, Cedar | Policy evaluation. | CAP carries policy decisions into the agent lifecycle and makes them executable by Executors. |
| OpenTelemetry | Observability. | CAP defines agent-control semantic events and required attributes. |
| W3C PROV, RO-Crate | Provenance and research packaging. | CAP defines which provenance artifacts an agentic assessment must emit. |
| FHIR/ReproSchema/Phenopackets | Health and assessment data models. | CAP governs the process that produces, transforms, and exports these artifacts. |
| LangGraph/Temporal | Runtime orchestration and durability. | CAP is portable across runtimes and defines the external authority contract. |

## 6. Suggested paper outline

1. Introduction
2. Background and limitations of MCP/A2A/tool-centric agents
3. Requirements from non-diagnostic psychometric agent systems
4. CAP Core design
5. Cytognosis/Neuroverse profile
6. Implementation
7. Evaluation
8. Threats to validity and limitations
9. Discussion and future work
10. Conclusion

## 7. Evaluation design

### Scenario

A synthetic psychometric assessment session where a local edge agent collects a response, summarizes or redacts it, sends a permitted evidence packet to a supervisor, receives the next question directive, and produces a non-diagnostic phenotype artifact.

### Implemented test conditions

- Valid low-risk directive.
- Expired directive.
- Unauthorized directive.
- Invalid signature.
- Missing evidence.
- Stale evidence.
- Evidence hash mismatch.
- Evidence access denied.
- Forbidden tool.
- Guard deny.
- Guard allow-with-constraints.
- Conflicting guards with deny-wins behavior.
- Prompt-injected evidence.
- Diagnostic-style output request.
- Stale policy.
- Duplicate delivery / idempotency.
- Side-effect reporting and compensation.
- Detached-JWS / DSSE / in-toto-style hardening.
- Revoked-key refusal and tampered-payload rejection.

### Metrics

- refusal correctness;
- guard-decision correctness;
- provenance completeness;
- overhead versus direct execution;
- schema validation pass rate;
- conformance suite pass rate.
- domain semantic-quality scores from qualified reviewers, reported separately from CAP conformance.

The current repository includes a local deterministic benchmark artifact for overhead versus direct execution under `docs/benchmarks/`. Treat it as early systems evidence only; production/provider latency, native mobile telemetry, and measured battery drain remain follow-up evaluation work.

The repository also includes a domain semantic-quality evaluation harness under `docs/domain_semantic_quality/` and `cap_protocol.evaluation.semantic_quality`, with synthetic CAP-Med and CAP-SWE onboarding fixtures under `examples/domain_semantic_quality/`. These fixtures exercise the evaluation workflow; they should not be described as expert validation or evidence of domain efficacy.

The repository includes a regulated-profile review packet under `docs/regulated_profile_review/` for CAP-Med-style constraints, forbidden behaviors, escalation, privacy controls, refusals, evidence examples, tests, known limitations, and reviewer questions. It is review preparation material, not regulatory clearance or clinical approval.

## 8. Expected reviewer concerns and responses

| Concern | Response |
|---|---|
| “Isn’t this just MCP/A2A?” | No. MCP and A2A provide tool and task plumbing; CAP defines authority, guard, refusal, and evidence semantics. |
| “Why not just use LangGraph?” | LangGraph is an implementation runtime; CAP is a portable supervisory protocol layer across runtimes and organizations. |
| “Does this guarantee safety?” | No. It provides structural accountability and enforcement points. Safety still depends on policies, models, data, and human oversight. |
| “Is this clinically validated?” | Not yet, and the paper should not claim clinical efficacy. It evaluates protocol/profile behavior and non-diagnostic boundary enforcement; the regulated-profile packet prepares external profile review but does not close that gate. |
| “Is CAP only medical?” | No. CAP-Med is the motivating regulated profile and now has a deterministic v1 runtime-profile fixture; CAP-SWE provides deterministic non-medical profile evidence for software-engineering agents using the same Core objects. |
| “Why a new protocol layer?” | Because agentic systems need supervisory control semantics not provided by any one existing standard, and domain profiles such as CAP-Med and CAP-SWE need evidence-bound, privacy-preserving, profile-specific constraints with deterministic inheritance and Core override refusal. |

## 9. Submission path

Current recommended path: workshop or systems-position paper with architecture, threat model, two executable bindings plus the local Go fixture adapter, conformance tests, local benchmark artifacts, and hardening results.
Stronger follow-up path: systems paper with deployment-representative latency/provenance benchmarking and live multi-organization interoperability tests.
Best long-term path: applied health-AI paper with a controlled pilot or synthetic user-study workflow, after external security review, regulated-profile review, and technical validation.
