> **Status**: Active
> **Date**: 2026-06-14
> **Author**: @mohammadi
> **Audience**: engineers
> **Tags**: `cap`, `cytoplex`, `spec`

# CAP v0.1 Production-Candidate Status

**Package:** `cap-protocol` / `cytognosis_cap_v01_production_candidate`
**Status:** production-candidate research package, not externally audited stable standard
**Core positioning:** CAP v1 is the **Control Authority Protocol**, a supervisory control plane and semantic enforcement layer. The current package preserves a v0.1 Control Authority Profile subset and includes partial v1 migration for the gRPC reference path and independent HTTP/JSON path; it is not a standalone transport, tool-calling, policy, identity, audit database, workflow engine, clinical-correctness system, or full v1 runtime.

## Implemented in this package

- Canonical implementation under `src/cap_protocol/`.
- Reference implementation at `src/cap_protocol/bindings/grpc_reference` over `grpc/protobuf-reference-binding/cap-envelope-v1`; `reference_grpc/` is a wrapper.
- Second independent implementation at `src/cap_protocol/bindings/http_json` over `http/json-independent-binding/cap-envelope-v1`; `second_http/` is a wrapper with retained v0.1 compatibility helpers.
- Local third implementation interop adapter at `third_impl/go_cap_adapter`, written in Go with standard-library dependencies, validates shared CAP v1 CAPEnvelope/JCS/signature fixtures and reports pass/fail by fixture ID.
- Shared compatibility CAP Core artifacts: v0.1 `Directive`, `GuardDecision`, `RefusalMessage`, `ExecutionReport`, `DecisionRecord`, `EvidenceRef`, and `AuthorityChain`.
- Active gRPC v1 artifacts: `CAPEnvelope`, `Directive`, `GuardDecision`, `InterruptDecision`, `RefusalMessage`, `ExecutionReport`, `EvidenceRef`, `AuthorityChain`, `PrivacyBoundary`, and `OperationalConstraints`.
- Active HTTP/JSON v1 artifacts: `CAPEnvelope`, `EvidenceRef`, `Directive`, `GuardDecision`, `InterruptDecision`, `RefusalMessage`, `ExecutionReport`, `AuthorityChain`, `PrivacyBoundary`, and `OperationalConstraints`.
- Decomposed Controller reference service: `ControllerService` forms signed Directive envelopes from intents, delegates policy to Guard/PDP evaluators, routes through `SessionRouter`, emits optional observability events, and documents the combined gRPC `CAPCenter` as v0.1 legacy compatibility.
- CAP-Med v0.1 profile constraints: non-diagnostic output boundary, clinical-output blocking, and raw-transcript-upload blocking remain compatibility evidence.
- CAP-Med v1 runtime-profile fixture: `cap_protocol.profiles.cap_med` uses signed `CAPEnvelope`, structured `PrivacyBoundary`, closed `OperationalConstraints`, unified `Capability`, `Directive`, `EvidenceRef`, and `InterruptDecision` objects while keeping CAP-Med constraints under `profile_constraints.cap-med/v1` and metadata under `profile_extensions.cap-med/v1`; tests and V1-C05 conformance cover Local PEP raw-transcript minimization and Supervisor Gateway overreach refusal.
- MCP constrained invocation demo and forbidden-tool refusal fixture.
- A2A metadata carriage demo.
- Live local MCP/A2A substrate interop scaffold: MCP `tools/call` and `resources/read` route through Edge PEP before handler execution, and A2A message delivery requires CAPEnvelope carriage plus AgentCard CAP extension advertisement.
- Reference live model-stream adapter: local scripted chunks, and optional Ollama chunks when supplied by a caller, route through the Local PEP sliding lookahead buffer with 250 ms/50 token defaults, deterministic semantic slow-path classification, pull-side backpressure, abort propagation, pre-display safe substitution, CLI/WebSocket-style safe abort replacement UX, CLI/WebSocket-style correction-frame replacement/annotation UX, Android/iOS native abort and correction contracts, and audit/provenance frame links.
- Local NER redaction pipeline: `LocalPEP.prepare_supervisor_context(...)` substitutes raw transcript/audio into local EvidenceRefs, then runs local-only redaction before Supervisor Gateway backend access. The deterministic fallback covers person, location, date, email, phone, SSN, medical, financial, credit-card, and IP-address categories, while `LocalModelNERRedactor` allows caller-supplied local model spans without remote egress.
- Embedding-only Supervisor egress: `LocalPEP.prepare_supervisor_context(...)` can encode text and voice sources locally and send only embeddings, aggregate dimensions, safety flags, evidence refs, provenance refs, recipient-binding metadata, and minimization metadata to the Supervisor Gateway. Raw transcript/audio remain local, and recipients are checked against the active PrivacyBoundary.
- Retention TTL deletion: `PrivacyBoundary.retention` drives raw local backing-content expiry for Local PEP evidence refs and Evidence Registry blobs. Expired backing content is deleted by deterministic GC, while deletion audit/provenance records retain hashes, refs, expiry/deletion timestamps, and `raw_content_logged=false` without retaining raw evidence.
- Mobile separately privileged proxy Local PEP scaffold: Android `CapLocalPepProxyService` and iOS `CapLocalPepProxyExtension` contracts, route-control metadata, manifest-shaped helpers, and smoke checks for direct user output, network, raw-data egress, local-tool, and missing OS-route bypass attempts. Native mobile project wiring and device evidence remain open.
- Attested isolated Local PEP registration scaffold: Control Plane challenge/response registration verifies deterministic detached-JWS test attestations, binds registration to SPIFFE workload identity and Local PEP version, rejects missing, expired, replayed, mismatched, untrusted, or debuggable attestations, and publishes Local PEP capability metadata only after verification. Real Play Integrity, App Attest, Secure Enclave, and TPM quote verifier integrations remain open.
- Machine-checkable lifecycle FSM and profile-inheritance scaffold: envelope, directive, interrupt, execution, evidence, audit, and provenance transitions are validated by `cap_protocol.runtime.lifecycle`; profile composition is deterministic, monotonic, and refuses Core lifecycle/interrupt overrides in `cap_protocol.profiles.inheritance`.
- Local latency/mobile-resource benchmark artifacts: `cap-run-v1-benchmarks` publishes p50/p95 latency, CPU-time, memory, streaming-delay, and mobile proxy-path measurements under `docs/benchmarks/`. These are local Python microbenchmarks, not native mobile telemetry or measured battery drain.
- OpenTelemetry `cap.*` semantic attributes and reference collector config.
- Signed audit-operation scaffold with external key-custody hooks, retention/access metadata, replication retry/backpressure, and audit-as-delivery-precondition gating.
- Sigstore/Rekor-style transparency scaffold for release and AuthorityChainStep DSSE/in-toto attestations, with local Rekor-compatible signed entry timestamps and Merkle inclusion-proof bundles that verify offline.
- W3C PROV-JSONLD local store scaffold with queryable session, evidence, authority, and interrupt lineage.
- W3C PROV mapping.
- Temporal-style workflow-engine composition sample showing signed CAP envelope receipt, Edge PEP verification, Session Router delivery, retry-triggered `InterruptDecision`, and final `ExecutionReport` emission with workflow/session/trace history links.
- JSON Schema artifacts for the CAP message primitives.
- Independent fixture-based conformance package.
- Deterministic adversarial fixtures.
- SPIFFE SVID workload identities on selected v1 envelope and AuthorityChain verification paths.
- Istio/Linkerd-style service-mesh composition scaffold where the mesh owns mTLS/SPIFFE identity and CAP Edge PEP remains an application sidecar for CAPEnvelope, policy, privacy, and authority validation.
- Runtime-generated local mTLS certificates under ignored runtime output, labeled as non-production localhost fallback transport; package verification checks that no source private key material is included.
- Ed25519 detached-JWS verification.
- DSSE signed envelopes.
- in-toto-style attestation statements.
- Hash-chain append-only audit store.
- One-command local, Colab, and Modal-compatible runner.

## Latest local runner output

The latest successful local deterministic run was regenerated at `2026-05-22T12:53:22Z` and produced:

- `overall_pass: true`
- reference implementation pass
- HTTP/JSON implementation pass
- production-hardening pass
- 28/28 implementation conformance checks per executable binding
- 33/33 production-hardening and independent conformance checks
- `final_output/CAP_FINAL_SUMMARY.json`
- `final_output/production_hardening/CAP_PRODUCTION_HARDENING_REPORT.json`
- `docs/benchmarks/cap_v1_latency_mobile_budget.json`
- `docs/benchmarks/cap_v1_latency_mobile_budget.md`

These are local structural/conformance results, not external verification or a stable security audit.

## Execution modes

- Deterministic structural/conformance mode is the default and uses local mock model behavior.
- Optional real-model mode is requested with `--use-real-separate-e2b`; dependencies and model access are installed manually.
- `--require-real-model` makes model-load failure fatal instead of falling back to deterministic mode.

## Remaining external gates before stable public release

The following are outside the scope of this self-contained runner and should not be claimed as complete:

1. Independent third-party security review.
2. Production key-management integration such as KMS/HSM. A custody and operations plan now exists at `docs/kms_hsm/README.md`, but deployment-owned KMS/HSM evidence remains required.
3. Organization-specific OPA/Cedar policy deployment. A deployment guide now exists at `docs/policy_deployment/README.md`, but organization-owned policies, runtimes, promotion evidence, and rollback evidence remain required.
4. External MCP server and live multi-organization MCP/A2A interoperability testing. A partner run plan and report template now exist at `docs/mcp_a2a_interop/README.md`, but external partner evidence beyond the local Go fixture adapter and local substrate scaffold remains required.
5. Empirical semantic-quality evaluation for the target application domain. A harness, rubric, report template, and synthetic onboarding fixtures now exist at `docs/domain_semantic_quality/README.md`, but qualified external expert review remains required.
6. CAP-Med or other regulated-profile review. A review packet now exists at `docs/regulated_profile_review/README.md`, but qualified external profile review and gate evidence remain required.
7. Deployment-representative latency/resource evaluation, including native mobile/device telemetry and measured battery drain.

## Release gate position

See `CAP_RELEASE_GATES.md` for the full gate taxonomy. The short form is:

- `v0.1-production-candidate` is the current executable package label.
- `v1-architecture-documented` is supported by the current docs and partial scaffolding.
- `v1-implemented-runtime`, `v0.1-stable`, and `v1-stable` are not supported labels yet.

The main blockers to `v1-implemented-runtime` are production Local PEP and Edge PEP deployment paths, native Android/iOS project wiring and device/instrumented bypass evidence, real platform attestation verifier integrations for Play Integrity, App Attest, Secure Enclave, and TPM quote paths, native/mobile performance telemetry and measured battery drain, production SPIRE/service-mesh SVID sourcing, deployed local/central PDP services, production Policy Registry hardening/deployment, production Controller rollout, production Supervisor Gateway rollout, production Session Router deployment, production Human Review portal/workflow rollout, deployed Temporal/LangGraph workflow integration, external MCP/A2A interoperability beyond local fixture validation, production model-provider rollout and shipping native UI wrappers around the reference live stream adapter, organization-selected semantic model-judge rollout, production local NER and embedding model rollout with redaction/privacy/quality evaluation, production offline signed policy bundle operations, production Capability/Evidence/Agent/Tool registry hardening/deployment, durable scheduled retention-job operations, production observability exporter/collector integration, production PROV graph/document store deployment, deployed KMS/HSM-backed warrant and audit key custody, external Sigstore/Rekor transparency publication, transparency/replication services, deployed revocation operations, and full v1 conformance certification.

## Correct claim

> CAP v1 architecture is documented and partially scaffolded as the Control Authority Protocol. This repository currently provides a v0.1 production-candidate Control Authority Profile subset with two executable local bindings, migrated gRPC and HTTP/JSON CAPEnvelope hot paths, a local Go third-implementation interop adapter, a decomposed Controller reference service, structured in-process privacy PDP, local NER redaction, embedding-only egress, retention TTL deletion checks on selected PEP/registry paths, machine-checkable lifecycle/profile-inheritance rules, CAP-Med v1 runtime-profile evidence, CAP-SWE non-medical profile evidence, local latency/mobile-resource benchmark artifacts, SPIFFE SVID identity-binding checks, deterministic service-mesh, live MCP/A2A substrate, workflow-engine, and transparency-log composition scaffolding, Biscuit-backed AuthorityChain warrant scaffolding, shared conformance fixtures, a release-blocking deterministic scaffold conformance gate for V1-C01 through V1-C15, production-hardening checks, signed authority artifacts, and optional real-model execution support. It is not a complete CAP v1 runtime and is not yet an externally audited stable public standard.
