> **Status**: Active
> **Date**: 2026-06-14
> **Author**: @mohammadi
> **Audience**: engineers
> **Tags**: `cap`, `cytoplex`, `spec`

# CAP Supervisor Brief

**Project:** CAP — Control Authority Protocol
**Context:** Cytognosis / Neuroverse non-diagnostic psychometric agent systems
**Version:** v1 architecture target with v0.1 production-candidate implementation evidence
**Purpose:** Explain the research contribution, novelty, architecture, and next steps without overstating the current package as a complete CAP v1 runtime.

## 1. Executive summary

CAP v1 should be framed as a **Control Authority Protocol**: a supervisory control plane and semantic enforcement layer for agentic systems. The current package implements a narrower v0.1 Control Authority Profile subset; it should not be described as a complete v1 runtime or as a new end-to-end agent transport.

The core idea is to separate **deciding** from **acting** in agentic systems. A Controller forms intent; a Guard evaluates policy, safety, privacy, and evidence requirements; an Executor either acts within constraints or returns a typed refusal. CAP standardizes this boundary through `Directive`, `GuardDecision`, `RefusalMessage`, `ExecutionReport`, `AuthorityChain`, `EvidenceRef`, and `PolicyRef`.

CAP deliberately does **not** replace MCP, A2A, OpenTelemetry, W3C PROV, OPA/Rego, Cedar, SPIFFE, DSSE, FHIR, ReproSchema, Phenopackets, RO-Crate, or workflow runtimes. It composes with them.

## 2. Final position

The defensible position is:

> CAP v1 is a supervisory Control Authority Protocol for agentic systems. Its novelty is the typed, evidence-bound, guardable, refusable, interruptible, privacy-bounded, and auditable boundary between authority sources, enforcement points, and executors that act on the world.

The claim to avoid is:

> CAP is a new universal transport or communication protocol for all agents.

That broader claim is weak because transport, tool calling, agent discovery, policy, identity, provenance, workflow durability, and health-data interchange already have stronger existing standards. CAP composes with those layers instead of replacing them.

## 3. Why CAP is still worth building

CAP is justified if it owns only the semantic gap that existing standards do not cover cleanly:

| Need | Existing layer | Gap CAP fills |
|---|---|---|
| Tool access | MCP | MCP does not define Controller-to-Executor authority semantics. |
| Agent task lifecycle | A2A | A2A does not define asymmetric control authority, evidence-bound refusal, or non-diagnostic guard semantics. |
| Policy evaluation | OPA/Rego, Cedar | Policy engines decide; CAP carries and enforces the decision in the agent lifecycle. |
| Observability/provenance | OpenTelemetry, W3C PROV, RO-Crate | These record provenance; CAP defines which agentic events and evidence links must be recorded. |
| Health/research data | FHIR, ReproSchema, Phenopackets | These represent data; CAP governs the agentic process that produces and validates that data. |

## 4. Novelty

### 4.1 General CAP novelty

CAP is novel in its composition of four control semantics:

1. **Typed authority:** actions require an explicit `AuthorityChain`, not just a prompt or role label.
2. **Guardable intent:** proposed actions can be allowed, denied, narrowed, or escalated by `GuardDecision`.
3. **Typed refusal:** Executors return structured refusal reasons rather than free-form errors.
4. **Evidence-bound execution:** actions must reference concrete evidence with integrity, freshness, access, and provenance metadata.

### 4.2 Cytognosis / Neuroverse novelty

The stronger novelty is domain-specific:

1. **Psychometric temporal state machine:** CAP tracks assessment progression, item order, branching logic, response timing, and evidence lineage rather than only generic task completion.
2. **Signed non-diagnostic boundary:** the profile can encode that assessment outputs must not become diagnosis or treatment recommendations.
3. **Signed assessment playbooks:** psychometric instruments, scoring rules, thresholds, prompts, and policies are versioned and attestable.
4. **Privacy-preserving edge-to-supervisor handoff:** raw behavioral data can remain local while redacted evidence packets or phenotype vectors are shared.
5. **Reproducible phenotype-generation traces:** phenotype artifacts can be traced back to evidence, policies, scoring rules, models, and domain configuration.

## 5. Architecture summary

```text
Controller -> Directive -> Guard -> GuardDecision -> Executor -> ExecutionReport / RefusalMessage
```

Core roles:

- **Controller:** forms intent and issues Directives.
- **Guard:** evaluates the Directive using policy, safety, privacy, and evidence rules.
- **Executor:** executes under bounds or refuses.
- **Observer:** maps lifecycle events to OpenTelemetry and W3C PROV.

Core primitives:

- `Directive`
- `GuardDecision`
- `RefusalMessage`
- `ExecutionReport`
- optional `DecisionRecord`

Core structures:

- `AuthorityChain`
- `EvidenceRef`
- `PolicyRef`
- `ConstraintSet`
- `SideEffect`

## 6. What was removed from the earlier CAP draft

The earlier draft was too close to a full protocol. The revised version removes:

- 11 hardcoded roles;
- 7 hardcoded governance modes;
- mandatory gRPC conformance;
- custom `DelegationRequest`;
- custom `HumanReviewRequest`;
- custom `StateCheckpoint`;
- custom `AuditEvent` and hash-chained audit;
- CAP-specific tool schemas;
- CAP-specific identity/key infrastructure.

These were delegated to A2A, MCP, workflow engines, OpenTelemetry, W3C PROV, DSSE/in-toto, and identity systems.

## 7. Paper opportunity

A paper is feasible if framed correctly.

Recommended title:

> CAP: A Control Authority Protocol for Evidence-Bound and Non-Diagnostic Agentic Assessment

Possible contributions:

1. A Controller/Guard/Executor authority model.
2. Evidence-bound Directive lifecycle.
3. Typed refusal and guard semantics.
4. A non-diagnostic safety profile for psychometric agents.
5. Reproducible phenotype-generation provenance.
6. Reference implementation and conformance suite.

The first paper can be an architecture/position paper. A stronger systems paper requires a small implementation and evaluation.

## 8. Current implementation evidence

The current package implements the v0.1 Control Authority Profile subset and extends it into a production-candidate research package with canonical code under `src/cap_protocol/`. CAP v1 architecture and initial schema/runtime scaffolding are present, but full v1 runtime migration remains open:

1. Controller issues a Directive.
2. Guard evaluates policy and returns `allow`, `allow_with_constraints`, or `deny`.
3. Executor validates authority, evidence, policy, freshness, and constraints.
4. Executor calls an MCP-style tool only if authorized.
5. Executor emits `ExecutionReport` or `RefusalMessage`.
6. Observer exports OpenTelemetry `cap.*` attributes and W3C PROV graph.
7. CAP-Med blocks diagnostic-style outputs and raw-transcript upload attempts.
8. The same semantics are exercised by both a gRPC/protobuf reference binding and an independently structured HTTP/JSON binding; top-level `reference_grpc/` and `second_http/` directories are compatibility wrappers.
9. Production-hardening checks cover detached-JWS verification, DSSE envelopes, in-toto-style attestations, revoked-key refusal, tampered-payload rejection, adversarial fixtures, package-private-key scanning, and hash-chain audit validation.
10. MCP, A2A, OPA-style policy, OpenTelemetry, and W3C PROV evidence is local demo/adapter coverage, not live external interoperability certification.
11. A regulated-profile review packet now exists under `docs/regulated_profile_review/`; it prepares external CAP-Med-style profile review but does not close the review gate.

## 9. Evaluation plan

| Evaluation | Metric / evidence |
|---|---|
| Authority enforcement | Unauthorized, expired, missing-evidence, invalid-signature, and revoked-key Directives are refused. |
| Guard correctness | `deny` blocks and `allow_with_constraints` narrows. |
| Evidence integrity | stale, hash-mismatched, inaccessible, and poisoned evidence is refused or blocked. |
| Non-diagnostic boundary | diagnostic-style Directive/output is blocked by CAP-Med profile policy. |
| Interoperability | MCP and A2A mappings work locally without CAP redefining them; a local Go adapter validates shared CAPEnvelope/JCS fixtures. |
| Observability | required `cap.*` OpenTelemetry attributes and W3C PROV graph are emitted. |
| Hardening | detached-JWS, DSSE, in-toto-style, revoked-key, tamper-rejection, adversarial fixtures, and audit hash-chain checks pass. |
| Overhead | local deterministic latency/mobile-resource benchmark artifacts compare CAP-mediated paths with direct paths; deployment/device evaluation remains future work. |

## 10. Limitations to state explicitly

CAP does not guarantee model truthfulness, hallucination prevention, clinical validity, or clinical safety. It does not diagnose, treat, or replace human judgment. It provides structural accountability, typed authority, evidence linkage, bounded execution, and auditable refusal/execution traces.

The current package is production-candidate and research-grade. It is not yet an externally audited stable public standard.

## 11. Remaining next steps

### Before external release as stable v0.1

- Run independent third-party security review.
- Integrate production key management such as KMS/HSM.
- Deploy organization-specific OPA/Cedar policies under real policy ownership and change control.
- Run external MCP server and live multi-organization MCP/A2A interoperability tests.
- Evaluate semantic question quality and domain-specific safety on representative tasks.
- Complete regulated-profile review using the packet under `docs/regulated_profile_review/`.

### For paper submission

- Use this package as implementation evidence for an architecture/systems paper.
- Report conformance and adversarial fixture results.
- Clearly separate structural safety/provenance claims from clinical or semantic-quality claims.
- Position CAP v1 as a Control Authority Protocol and supervisory control plane, while describing the checked-in runtime as a v0.1 Control Authority Profile subset rather than a new transport protocol or complete v1 implementation.
- Extend the current latency/overhead measurements, lifecycle/profile-inheritance scaffold, CAP-SWE profile evidence, Go fixture adapter, and synthetic semantic-quality harness with external interoperability and qualified expert review for a stronger systems paper.

## 12. Supervisor ask

Feedback requested:

1. Is the framing as a supervisory Control Authority Protocol, with the current runtime clearly scoped to a v0.1 Profile subset, acceptable?
2. Is the implementation evidence sufficient for a workshop/system-position paper?
3. Which remaining evaluation matters most before submission: security review, latency, semantic quality, non-diagnostic safety, or interoperability?
4. Should the first paper emphasize general control-authority semantics or the Cytognosis/CAP-Med psychometric use case?
