> **Status**: Active
> **Date**: 2026-06-14
> **Author**: @mohammadi
> **Audience**: engineers
> **Tags**: `cap`, `cytoplex`, `spec`

# CAP_07 — Profiles and Roadmap

## 1. Profile architecture

CAP Core is deliberately minimal. Profiles define domain-specific policy, evidence schemas, constraints, and conformance tests without changing Core semantics.

CAP v1 keeps this rule while moving more deployment detail into profile metadata. A profile must declare its Local PEP trust mode, offline behavior, privacy-boundary defaults, interrupt latency budget, audit-persistence requirements, and any supervisor/human escalation obligations.

A profile MAY define:

- additional EvidenceRef media types;
- domain-specific PolicyRef conventions;
- stricter Guard requirements;
- required human/workflow approval before certain authority steps;
- retention/minimization constraints;
- domain-specific side-effect and compensation semantics;
- additional conformance tests.

A profile MUST NOT:

- redefine Directive lifecycle states;
- remove Core refusal codes;
- weaken Core constraint merge rules;
- make raw chain-of-thought auditable content;
- replace MCP, A2A, OTel, PROV, identity, or policy engines;
- require a specific transport as Core conformance.

## 2. Extension mechanism

Profiles SHOULD use namespaced extension objects:

```json
{
  "profile_extensions": {
    "cap-med/v1": {
      "non_diagnostic_required": true,
      "non_prescriptive_required": true,
      "clinical_output_forbidden": true
    }
  }
}
```

When a rule narrows execution resources or budgets in a way that generic CAP machinery can merge, profiles SHOULD place it under `OperationalConstraints.profile_constraints` using the same namespace pattern. Profile-specific safety or domain requirements, such as CAP-Med non-diagnostic style, psychometric scoring, medical thresholds, or escalation thresholds, MUST NOT be promoted to top-level CAP Core `OperationalConstraints` fields.

Generic CAP parsers MUST preserve extension objects for signature integrity but MAY ignore namespaces they do not understand.

## 3. Profile inheritance and composition

Profile inheritance is monotonic. A child profile can narrow a parent profile, add namespaced requirements, or raise risk levels, but it cannot weaken Core or parent requirements. The executable reference rules live in `cap_protocol.profiles.inheritance` and are covered by V1-C05 conformance.

Profile composition is deterministic:

- Parents are applied before children; otherwise profiles sort by `priority` and namespace.
- Core lifecycle states, lifecycle transitions, interrupt actions, PrivacyBoundary dimensions, and Core refusal categories are reserved and cannot be overridden by a profile.
- `allowed_tools`, `network_egress`, and `data_access_scope` compose by intersection; an empty intersection is a conflict.
- `forbidden_tools` composes by union.
- Numeric ceilings such as `max_wall_time_ms`, `max_tool_calls`, `max_cost`, and numeric budgets compose by minimum; a child profile that explicitly raises a parent ceiling is refused as a widening override.
- Required boolean constraints cannot be unset by a child profile.
- Tool-risk levels can only stay the same or move to a stricter risk level in the `low < medium < high < critical` order.
- Unknown scalar conflicts fail closed instead of choosing an arbitrary winner.
- Multi-profile sibling composition produces the same effective constraints regardless of input order.

These rules make CAP-Med, CAP-SWE, and future profiles portable without letting a profile redefine Core semantics.

## 4. Candidate profiles

| Profile | Scope | Examples of profile-specific rules |
|---|---|---|
| CAP-Med | Medical and mental-health workflows | non-diagnostic and non-prescriptive output constraints, FHIR/Questionnaire evidence refs, clinician/human workflow requirements. |
| CAP-SWE | Software engineering agents | diff evidence, sandbox constraints, test-result evidence, file-write authority, rollback/commit compensation, tool-risk levels, and human/code-owner escalation. |
| CAP-Fin | Financial services | funds-movement Guard policies, regulatory PolicyRefs, retention requirements, stricter authority chains. |
| CAP-Edu | Education/tutoring | learner privacy, age-appropriate content, parental/educator workflow approvals. |
| CAP-Rob | Robotics/physical actuation | spatial constraints, millisecond expiry, emergency-stop policy, physical safety Guard decisions. |
| CAP-CS | Customer support | PII minimization, escalation policy, communication side-effect rules. |
| CAP-Sci | Scientific/research workflows | dataset provenance, reproducibility evidence, experiment/run attestations. |

For the current motivating CAP-Med scenario, the local interviewer can be labeled **Therapist** in examples and tests, but this label is profile-specific and must always remain supportive, non-diagnostic, and non-prescriptive. The central/main **Supervisor** is an authority participant behind a Supervisor Gateway, not a single CAP component. CAP separates the Supervisor authority role, the Supervisor Gateway endpoint, and the model, human, or rule engine behind that gateway. The Supervisor provides strategy and safety review; it receives locally redacted context and evidence references by default, or policy-allowed local text/voice embeddings plus aggregate dimensions for embedding-only egress, does not receive raw transcript/audio by default, and cannot bypass Local PEP privacy, non-diagnostic, jurisdiction, or safety vetoes. `cap_protocol.profiles.cap_med` is the checked-in CAP-Med v1 runtime profile fixture: its constraints live under `profile_constraints.cap-med/v1`, its metadata lives under `profile_extensions.cap-med/v1`, and its hot-path smoke uses a signed `CAPEnvelope`, structured `PrivacyBoundary`, unified `Capability` records, `OperationalConstraints`, `InterruptDecision` mappings, Local PEP minimization, and Supervisor Gateway overreach vetoes. Current deterministic Controller, Local PEP, local NER redaction, embedding-only egress, retention TTL deletion, Supervisor Gateway, Session Router, and Human Review fixtures cover Controller/Guard/Observer separation, raw transcript/audio overreach, diagnostic and treatment-advice overreach, structured gateway translation, allowed redacted-context/EvidenceRef paths, embedding-only recipient binding, expired backing-content deletion with audit preservation, routed review tasks, structured review decisions, and raw-data request refusal unless policy permits it. The v0.1 CAP-Med profile constraints remain legacy compatibility evidence. A regulated-profile review packet now exists under `docs/regulated_profile_review/`, but qualified external profile review, production Controller, Supervisor Gateway, and Human Review portal/workflow rollout remain runtime and external-gate backlog.

CAP-SWE is the checked-in non-medical reference profile. It uses the same CAP Core objects and places profile-owned rules under `profile_constraints.cap-swe/v1` and `profile_extensions.cap-swe/v1`. The reference fixture in `cap_protocol.profiles.cap_swe` declares diff evidence, test-result evidence, sandbox attestation, file-write authority, rollback plans, commit compensation, tool-risk levels, and code-owner escalation triggers. Its deterministic conformance checks prove that a minimized software-engineering review payload can cross the active privacy boundary while production secrets remain local-only. This is executable generality evidence for CAP profiles, not production certification of a deployed software-engineering agent.

## 5. Roadmap

### Completed in this production-candidate package

- CAP Core v0.1-candidate markdown package.
- JSON Schema Draft 2020-12 artifacts.
- Initial CAP v1 LinkML authoring schemas using the umbrella/core/domain layout.
- gRPC/protobuf reference binding.
- HTTP/JSON independent binding with independent primitive builders.
- MCP constrained tool-execution example.
- A2A Task metadata carriage example.
- OPA/Cedar-shaped policy adapters and portable policy-as-data backend.
- OpenTelemetry `cap.*` attribute emission and W3C PROV exporter.
- Shared conformance suite and independent fixture package.
- Local Go third-implementation CAPEnvelope/JCS fixture adapter.
- Deterministic adversarial fixtures.
- SPIFFE SVID workload-identity checks, with runtime-generated local mTLS certificates retained only as non-production fallback transport.
- Detached-JWS, DSSE, in-toto-style attestation verification, and local Sigstore/Rekor-style transparency-bundle verification.
- Hash-chain audit store.

### Remaining external gates

- Independent third-party security review.
- Production key-management integration such as KMS/HSM.
- Organization-specific OPA/Cedar policy deployment.
- Live multi-organization MCP/A2A interoperability tests.
- Empirical semantic-quality evaluation for target application tasks. A harness, reviewer rubric, report template, and synthetic onboarding fixtures now exist under `docs/domain_semantic_quality/`, `examples/domain_semantic_quality/`, and `cap_protocol.evaluation.semantic_quality`; qualified domain expert review remains required.
- CAP-Med or other regulated-profile review. A review packet, checklist, open-question list, report template, and non-secret placeholder now exist under `docs/regulated_profile_review/` and `config/regulated_profile_review.example.yaml`; qualified external profile review remains required.
- Deployment-representative latency, resource, and native mobile/device evaluation.

### CAP v1 migration backlog

The v1 migration is tracked in `CAP_v1_TASKS.md`. It is separate from the completed v0.1 production-candidate evidence. Initial v1 LinkML schemas, JSON Schema artifacts/examples, Controller/Local PEP/Edge PEP scaffolds, deterministic Android/iOS mobile proxy Local PEP contracts, deterministic attested Local PEP challenge/response registration, local NER redaction, embedding-only projection, retention TTL deletion before/after Supervisor egress, CAP-SWE non-medical reference profile evidence, formal lifecycle/profile-inheritance scaffold checks, local latency/mobile-resource benchmark artifacts, local Go third-implementation CAPEnvelope/JCS fixture validation, release-blocking deterministic scaffold conformance for V1-C01 through V1-C15, migrated gRPC/HTTP `CAPEnvelope` hot paths, selected executable Local PEP mediation, demo cross-boundary Edge PEP verification, service-backed Agent/Tool discovery, live local MCP/A2A substrate interop, signed policy-bundle distribution, and content-addressed Evidence Registry reference storage now exist, but production PEP/registry/substrate deployment remains on the migration backlog. The main remaining buckets are:

- deterministic generated JSON Schema replacement if reviewed output becomes suitable for the runtime validation path;
- production key infrastructure, externally owned cross-implementation JCS fixtures, KMS/HSM warrant-key custody, external Sigstore/Rekor publication and monitoring, and deployed revocation operations;
- production Edge PEP service-mesh or sidecar wiring, native mobile/device evidence, and real platform attestation verifier rollout for attested Local PEP trust modes;
- production Controller, Supervisor Gateway, and central Control Plane decomposition;
- production stream-provider rollout, organization-selected semantic model-judge rollout or human expert review process, production local NER and embedding model/evaluation rollout, shipping native UI wrappers around the reference live Local PEP lookahead, abort, and correction adapters, and deployment-representative latency/resource/mobile telemetry beyond the local Python benchmark;
- production hardening for signed policy-bundle distribution and revocation;
- deployed federated registry services, external MCP/A2A interoperability beyond the local Go fixture adapter, service authentication, access-policy enforcement, scheduled retention operations, and durable cache semantics;
- full production v1 conformance certification beyond the deterministic scaffold gate.

## 6. Public release criteria

CAP v0.1 SHOULD NOT be called stable until:

1. Two independent implementations pass the same Core conformance fixtures. **Status: complete in this package; a local Go third-implementation fixture adapter also passes the shared CAPEnvelope/JCS fixture suite.**
2. At least one implementation demonstrates CAP + MCP execution. **Status: complete locally, including live local MCP server paths through Edge PEP.**
3. At least one implementation demonstrates CAP-over-A2A metadata carriage. **Status: complete locally, including CAPEnvelope-wrapped A2A message delivery.**
4. OpenTelemetry and PROV mappings are implemented by an Observer. **Status: complete for deterministic reference mappings; production collector/exporter operations remain open.**
5. Schema examples validate under JSON Schema Draft 2020-12. **Status: complete.**
6. Deterministic adversarial fixtures pass. **Status: complete.**
7. Authority-signature, DSSE, in-toto-style attestation, local transparency-bundle, revoked-key, and tamper-rejection checks pass. **Status: complete in the hardening runner.**
8. A security review finds no unresolved critical flaws in authority verification. **Status: external gate remaining.**
9. Production key-management and organization-specific policy deployment are integrated. **Status: external gate remaining.**
10. Documentation clearly states CAP's non-guarantees. **Status: complete.**

CAP v1 SHOULD NOT be called implemented until:

1. Target v1 LinkML schemas exist, JSON Schema artifacts are generated or drift-checked, and examples validate.
2. At least one reusable Local PEP enforces privacy boundaries and streaming interrupts.
3. At least one Edge PEP validates CAPEnvelope signatures at a network boundary.
4. Supervisor Gateway output is structured, authority-checked, and privacy-filtered.
5. Offline fallback behavior is tested with signed policy bundles.
6. Federated registry behavior is represented by services or deterministic stubs. **Status: complete as reference services; production deployment remains open.**
7. V1 conformance backlog cases pass in CI.
8. Documentation distinguishes architecture claims from implementation evidence.

## 7. Risk register

| Risk | Likelihood | Impact | Mitigation |
|---|---:|---:|---|
| Scope creep | High | High | Strict scope test; reject transport/tool/audit/workflow features from Core. |
| Profile bloat | Medium | High | Profiles cannot redefine Core; profile tests must map to Core invariants. |
| Adoption friction | Medium | Medium | Allow local-trust relaxation of message-level attestations where profiles permit. |
| False safety claims | High | High | Document non-guarantees; conformance means structural correctness only. |
| Policy-engine complexity | Medium | Medium | Provide minimal OPA/Cedar examples; keep policy logic outside Core. |
| Signature integration bugs | Medium | High | Use established DSSE/COSE/JOSE libraries; avoid custom canonicalization. |
| Evidence poisoning | High | High | Treat evidence as untrusted; enforce constraints outside model context. |
| Inconsistent implementations | Medium | High | Provide machine-checkable lifecycle/profile rules, schemas, examples, and conformance fixtures. |
| Performance overhead | Medium | Medium | Keep CAP on control path, not high-frequency data path; use the local benchmark artifact as early evidence and require deployment-specific measurement before production claims. |
| Conflict with A2A/MCP | Medium | High | Define CAP as metadata/profile over A2A and authorization boundary around MCP. |
| Sidecar bypass | Medium | High | Require profile-declared Local PEP trust mode; use proxy or attested isolation for high-assurance deployments. |
| Supervisor overreach | Medium | High | Preserve Local PEP veto over raw-data egress, diagnostic output, treatment advice, and jurisdictional policy; allow only redacted context, embedding-only context, and EvidenceRefs by default. |
| Streaming leakage | Medium | High | Implement lookahead buffers, semantic slow-path checks, correction frames, and adversarial stream tests. |
| Policy drift between local and central PDPs | Medium | Medium | Use signed policy bundles, version pinning per session, and explicit hot-update behavior. |



## Paper-readiness plan

CAP can support three paper forms, with increasing empirical strength:

| Paper type | Minimum evidence | Recommended venue style |
|---|---|---|
| Position / architecture paper | Final spec, literature comparison, threat model, and design rationale. | Agent systems, responsible AI, health-AI workshops. |
| Systems paper | Reference implementation, conformance suite, MCP/OPA/OTel integrations, local benchmark artifacts, and security tests. | AI systems, distributed systems for AI, applied AI engineering. |
| Applied psychometric-AI paper | Synthetic or pilot assessment workflow, non-diagnostic guard evaluation, phenotype provenance, privacy handoff case study. | Digital health, mental-health AI, computational psychiatry workshops. |

A first submission should not claim clinical efficacy. It should claim structural accountability and evaluate whether CAP enforces the intended authority, evidence, refusal, and non-diagnostic boundaries.

The semantic-quality harness at `docs/domain_semantic_quality/README.md` can support an applied follow-up by separating reviewer-scored output quality from structural CAP conformance. Its checked-in fixtures are synthetic onboarding examples only; an applied paper still needs qualified domain reviewers and a governed dataset plan.

The regulated-profile review packet at `docs/regulated_profile_review/README.md` can support CAP-Med or similar profile review by collecting constraints, forbidden behaviors, escalation rules, privacy controls, user-facing refusals, evidence examples, test references, known limitations, a reviewer checklist, and open questions. It is preparation material only; external profile review remains open.

### Minimum implementation status

The minimum implementation previously required before public review is now complete in this production-candidate package:

1. Controller-Guard-Executor reference flow. **Complete.**
2. One MCP tool call authorized by a CAP Directive. **Complete, with local live MCP `tools/call` and `resources/read` substrate coverage.**
3. OPA-shaped and Cedar-shaped policy GuardDecision adapters. **Complete locally as deterministic scaffold parity.**
4. EvidenceRef integrity and freshness checks. **Complete.**
5. OpenTelemetry span/event export. **Complete for local/reference attribute coverage.**
6. W3C PROV export for terminal sessions. **Complete.**
7. Conformance tests for expired, unauthorized, missing-evidence, forbidden-tool, guard-deny, and prompt-injection-through-evidence cases. **Complete.**
8. Detached-JWS/DSSE/in-toto-style hardening, revoked-key refusal, tamper rejection, adversarial fixtures, and audit hash-chain verification. **Complete in the hardening runner.**

### Research validation questions

- Does CAP prevent execution without valid authority and evidence?
- Does CAP correctly narrow execution when a Guard returns `allow_with_constraints`?
- Does CAP reject diagnostic-style outputs under a non-diagnostic profile?
- Does CAP preserve enough provenance to reconstruct how a phenotype artifact was produced?
- What latency overhead does CAP add compared with direct MCP/tool execution? **Current package: local deterministic p50/p95 evidence exists under `docs/benchmarks/`, with production/device benchmarking still open.**
- Can independent implementations pass the same conformance suite? **Current package: yes for the two executable local bindings, and the local Go third-implementation adapter passes the shared CAPEnvelope/JCS fixture suite.**
- Can the Therapist persona remain supportive and non-diagnostic when the central Supervisor is unavailable or overreaches?
- Can Local PEP streaming interruption prevent unsafe output before user-visible delivery under realistic latency budgets? **Current package: deterministic stream gating and timer-release benchmark evidence exists; production provider and native UI budgets remain open.**
- Can the same Core objects carry a non-medical CAP-SWE profile with executable diff, test, sandbox, file-write, compensation, tool-risk, and human-escalation evidence?
