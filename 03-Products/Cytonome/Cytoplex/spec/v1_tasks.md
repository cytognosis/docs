> **Status**: Active
> **Date**: 2026-06-14
> **Author**: @mohammadi
> **Audience**: engineers
> **Tags**: `cap`, `cytoplex`, `spec`, `tasks`

# CAP v1 Documentation Gap Backlog

This backlog tracks the gap between the current CAP v0.1 production-candidate package and the CAP v1 target architecture.

Source priority:

1. `/Users/ali/Downloads/cap_v1_baseline.md` is the authoritative v1 architecture source.
2. `/Users/ali/Downloads/CAP_Architecture_Critical_Review.md` fills missing sections: object model, interrupt semantics, privacy, MVP, roadmap, conformance, and failure modes.
3. `/Users/ali/Downloads/CAP_Final_Architecture_and_Critique_Prompt.md`, `/Users/ali/Downloads/Designing CAP_ Agent Control Plane.md`, and `/Users/ali/Downloads/deep-research-report(8).md` are fallback context only.

This document is a planning artifact. It does not imply that the current schemas or runtime already implement every v1 target.

## Current Status

Completed documentation items:

- DOC-FIX-01 is complete: v0.1 `ConstraintSet.requires_human_confirmation` is documented as compatibility-only, CAP v1 Core `OperationalConstraints` stays closed to top-level human-confirmation fields, and the v1 example/tests use namespaced `profile_constraints`.
- DOC-FIX-02 is complete: CAP v1 `PrivacyBoundary` now consistently uses nine first-class dimensions, with `boundary_id` treated as an identifier and `policy_refs` as supporting metadata; raw transcript/audio egress remains explicit and denied by default in CAP-Med examples.
- DOC-FIX-03 is complete: the streaming lookahead default is consistently documented as the smaller of 250 ms of speech-equivalent text or 50 tokens unless a profile overrides it, and architecture text/diagrams place the buffer inside the Local PEP before user-visible output.
- DOC-FIX-04 is complete: `Capability` required and optional fields are documented inline, A2A AgentCard and MCP server/tool metadata remain in `profile_extensions`, and registry semantics remain tied to `capability_id` plus `operations`.
- DOC-FIX-05 is complete: legacy interrupt vocabulary such as downgraded language, revised output, local fallback, deferred analysis, and streaming correction is explicitly documented as profile shorthand or linked outcomes composed from the seven Core `InterruptDecision.action` values, not enum extensions.
- DOC-FIX-06 is complete: streaming terminology is defined once in the `InterruptDecision` primitive section, including lookahead buffer, sliding lookahead buffer, configurable lookahead, buffered transform, abort, and correction frame; nearby security, examples, architecture, and scaffold comments now refer back to that vocabulary.
- P0-DOC-01 through P0-DOC-05 are complete.
- P2-DOC-01 is complete: `docs/architecture.md` now includes Mermaid diagrams for the v1 target planes, enforcement points, decomposed Control Plane, PDPs, federated registries, observability plane, and current-vs-target implementer path.
- P2-DOC-02 is complete: `docs/CAP_examples.md` now includes redacted Therapist/Supervisor profile sequence examples for safe pass-through, diagnostic transform, supervisor pause with Local PEP veto, self-harm escalation, and offline fallback.
- P2-DOC-03 is complete: `docs/CAP_appendix_schemas.md` now distinguishes current v0.1 schema skeletons from the v1 LinkML authoring layout, checked-in v1 JSON Schema artifacts, examples, compatibility notes, and drift checks.
- P2-DOC-04 is complete: `docs/CAP_RELEASE_GATES.md` now separates v0.1 production-candidate, v1 documented architecture, v1 implemented-runtime, and stable public release gates.
- A task prompt library now exists under `docs/task_prompts/cap_v1/`, with one standalone prompt file per backlog item.

Completed or initially implemented migration items:

- P1-SCHEMA-01 through P1-SCHEMA-06 have initial LinkML authoring schemas under `schemas/cap.yaml`, `schemas/core.yaml`, and `schemas/domains/*.yaml`, plus JSON Schema Draft 2020-12 artifacts and examples under `schemas/cap-core/v1/` and `examples/cap-core/v1/`. `cap-check-v1-schema-drift`, `python scripts/check_v1_schema_drift.py`, and `tests/test_cap_v1_linkml.py` provide the current drift gate.
- P1-SEC-01 documents RFC 8785/JCS as the CAP v1 JSON canonicalization target, keeps v0.1 deterministic JSON signing compatibility labeled in helper metadata, and adds deterministic invalid-signature and payload-tamper coverage for detached JWS, DSSE, and signed CAPEnvelope payload hashes.
- P1-SEC-02 documents the CAP Warrant / AuthorityChain verification algorithm, requires holder identity, capability, scope, policy, expiry, revocation, delegation constraints, and signature metadata in v1 authority steps, and adds deterministic signed AuthorityChain verifier coverage for missing, expired, unsupported, and invalid-signature paths.
- P1-T1 is complete for the gRPC reference binding: `src/cap_protocol/bindings/grpc_reference` now emits v1 `CAPEnvelope` objects with v1 `Directive`, `GuardDecision`, `InterruptDecision`, `RefusalMessage`, and `ExecutionReport` payloads on the active gRPC path, while v0.1 gRPC builders/adapters remain compatibility evidence.
- P1-T2 is complete for the independent HTTP/JSON binding: `src/cap_protocol/bindings/http_json` now emits v1 `CAPEnvelope` objects for HTTP boundary requests and responses with independent v1 `EvidenceRef`, `Directive`, `GuardDecision`, `RefusalMessage`, and `ExecutionReport` builders/validators, while retained v0.1 HTTP helpers remain compatibility evidence.
- P1-T3 is complete for helper-generated v1 signatures: `src/cap_protocol/security/cap_crypto.py` exposes RFC 8785/JCS bytes for v1 detached-JWS and DSSE signing, v1 runtime/binding/conformance signing surfaces label `rfc8785-jcs`, and v0.1 deterministic JSON verification remains compatible under `json-deterministic-sort-keys-v0.1`.
- P1-T4 is complete for executable Local PEP mediation: the gRPC and HTTP/JSON demos route selected user-visible output, local memory/raw-observation handling, and MCP-style local-tool calls through the reusable Local PEP scaffold, link mediated execution reports to audit/provenance refs, and include direct output/tool bypass refusals.
- P1-T5 is complete for demo Edge PEP enforcement: the gRPC and HTTP/JSON demos route cross-boundary `CAPEnvelope` traffic through the reusable Edge PEP before payload use, expose verification-order/report evidence, and include binding-level typed refusal matrices for invalid signature, expired envelope, unknown boundary, revoked authority, and payload-ref dereference refusal.
- P1-T6 is complete for deterministic runtime `InterruptDecision` handling: `src/cap_protocol/runtime/interrupts.py` builds all seven primitive actions, composes conflicts with `deny > pause/escalate > transform > constrain > allow`, maps CAP-Med profile behaviors onto Core actions, and the gRPC/HTTP demos link applied interrupt refs from execution reports.
- P1-T7 is complete for structured privacy PDP evaluation: `src/cap_protocol/runtime/privacy_pdp.py` evaluates the nine `PrivacyBoundary` dimensions, normalizes profile-only constraint fields under `profile_constraints`, and Local PEP, Edge PEP, and v1 policy-adapter paths now cite the failing boundary dimension in privacy refusals.
- P1-T8 is complete for deterministic clock-skew and expiry behavior: `src/cap_protocol/runtime/temporal.py` centralizes the default 30 second skew tolerance and exact expiry checks, and Edge PEP, Local PEP, AuthorityChain verification, policy-bundle checks, registry freshness, EvidenceRef freshness, Supervisor Gateway authority checks, and the gRPC/HTTP v1 validators reuse it.
- P1-T9 is complete for unified Capability registration metadata: schema examples now cover agent, tool, service, human, and policy subject kinds; `CapabilityRegistry` stores and authorizes all five kinds with one closed `Capability` shape; kind-specific registry views normalize legacy agent/tool metadata only as compatibility adapters.
- P1-T10 is complete for release-blocking deterministic scaffold conformance: `src/cap_protocol/conformance/v1_runner.py` maps V1-C01 through V1-C15 to executable required cases with owner, status, evidence links, and explicit full-runtime external-gate reasons; `cap-check-v1-conformance`, `tests/test_conformance.py`, and `python VERIFY_RELEASE_BASELINE.py` fail on required case failures.
- P1-CONF-01 through P1-CONF-04 have deterministic coverage for replay/idempotency, clock-skew/expiry, stale-policy hot update, and evidence tamper. P1-CONF-05 through P1-CONF-08 have deterministic coverage for offline fallback, sidecar bypass, streaming correction, and Supervisor overreach.
- P2-RUNTIME-01 is complete as a reusable deterministic Local PEP scaffold with typed refusals, raw evidence-reference substitution, local privacy/output gates, Supervisor overreach vetoes, offline fallback, and documented production-hardening gaps. P2-RUNTIME-02 is complete as a reusable deterministic Edge PEP scaffold with CAPEnvelope signature/TTL/skew checks, configured boundary PolicyRef checks, resolved AuthorityChain verification, privacy-before-dereference checks, demo gRPC/HTTP cross-boundary routing, and documented registry/PDP integration gaps.
- P2-RUNTIME-03 is complete as a deterministic configurable streaming lookahead scaffold with pre-display transform and late correction-frame behavior. P2-RUNTIME-04 is complete as a deterministic offline policy-bundle cache scaffold with metadata checks, optional detached-JWS signed-payload verification through existing crypto helpers, unreachable-Control-Plane fallback, profile-safe support, and fail-closed sensitive output. P2-RUNTIME-05 is complete as a deterministic Supervisor Gateway stub that privacy-filters consultation context, validates authority scope, separates authority role/gateway/backend engine, translates safe structured output into `Directive` or `InterruptDecision`, and preserves Local PEP veto behavior. P2-RUNTIME-06 is complete as deterministic Capability, Policy, and Evidence registry stubs with kind-specific Capability views, cache hit/miss, version, digest, expiry, trust-domain, stale metadata, revoked capability, policy drift, and evidence hash-mismatch behavior. P2-RUNTIME-07 is complete as deterministic observability-plane sink scaffolding that routes events to separate audit, telemetry, and provenance sinks, keeps audit durable/tamper-evident through the hash-chain store, models telemetry as lossy/sampled/short-retention, preserves provenance lineage, and isolates sink failures from each other.
- P2-T1 is complete as a Capability Registry reference service interface and SQLite-backed implementation: runtime clients preserve cache hit/miss behavior while checking live service-backed revocation freshness, registry records persist across service restarts, trust-domain federation hooks delegate lookups and propagate revocations, audit events are recorded, and `ServiceBackedKeyRegistry` resolves Ed25519 warrant keys for AuthorityChain verification with key-rotation and revoked-authority coverage. KMS/HSM custody, service authentication, network deployment, HA replication, and operational monitoring remain external deployment dependencies.
- P2-T2 is complete as a Policy Registry reference service for signed bundle distribution: Local PEP can fetch verified signed bundles from `ReferencePolicyRegistryService`, sessions pin bundle version/digest by default, explicit hot update rotates a pin, revoked or mismatched bundles fail closed, emergency override bundles are audited and still require valid signature/digest/expiry, and offline fallback continues from the verified local cache. KMS/HSM signing custody, service authentication, network deployment, HA replication, operational monitoring, and organization rollout controls remain external deployment dependencies.
- P2-T3 is complete as service-backed Agent/Tool discovery for deterministic demos: `AgentToolDiscoveryService` registers and looks up A2A AgentCard metadata and MCP tool descriptors through closed `Capability` records with cache hit/miss, stale, unknown, revoked, and trust-domain test coverage. Live multi-organization MCP/A2A interoperability, service authentication, network deployment, HA replication, and monitoring remain external deployment dependencies.
- P2-T4 is complete as a service-backed Evidence Registry reference implementation: the registry can put/get/verify content-addressed Evidence blobs, store media type and size, attach reference attestation/provenance metadata, reject missing or tampered content, and feed Edge PEP payload-ref dereference after privacy-boundary checks. Deterministic retention/deletion coverage is now tracked under P3-T9; production access-policy enforcement, scheduled retention operations, production attestation signing, service authentication, network deployment, HA replication, and monitoring remain external deployment dependencies.
- P2-T5 is complete as a deterministic Cedar PDP adapter scaffold behind the same CAP request/decision interface as the OPA-shaped adapter: `CAPPolicyRequest`, `PDPDecision`, `OPAPolicyAdapter`, and `CedarPolicyAdapter` support equivalent conformance-fixture decisions, the Cedar request maps CAP subject/action/resource/context explicitly, and tests mark the optional external Cedar runtime as skipped when unavailable. Organization-owned Cedar policy authoring, deployment, rollout, and production runtime integration remain external deployment dependencies.
- P2-T6 is complete as a Biscuit warrant reference integration for v1 AuthorityChain steps: `warrant_format=biscuit-v2` encodes canonical CAP step claims into holder-bound Biscuit tokens, the verifier decodes/authorizes them through the same AuthorityChain interface as detached-JWS compatibility steps, and tests cover round-trip, wrong-holder capture refusal, scope-expansion refusal, policy-ref shape, registry-backed warrant-key lookup, key rotation, and live revocation freshness. KMS/HSM custody, service authentication, network deployment, HA replication, operational monitoring, and external interoperability evidence remain external deployment dependencies.
- P2-T7 is complete as a SPIFFE/SVID workload-identity scaffold: `cap_protocol.runtime.workload_identity` parses environment-provided SPIFFE IDs and mounted X.509 SVIDs, Edge PEP can require SPIFFE sender/receiver/runtime identities in the expected trust domain, AuthorityChain and Biscuit-backed warrant verification refuse missing or mismatched SPIFFE SVID holder bindings, and the gRPC/HTTP demos report SPIFFE SVIDs as primary CAP v1 workload identity. Runtime-generated gRPC mTLS certificates remain only a local non-production transport fallback; production SPIRE Workload API/service-mesh rollout remains external deployment work.
- P2-T8 is complete as a Supervisor Gateway reference service boundary: `SupervisorGatewayService` routes consultation requests through a CAP-facing contract, `HTTPSupervisorGatewayClient` exercises the standard-library HTTP/JSON path, and model, human-portal, and rule-engine backend adapters sit behind the same backend interface. The service forwards only Local PEP-minimized context to backends, refuses unredacted raw context flags, preserves AuthorityChain verification and Local PEP policy/privacy/safety vetoes, hides backend type behind the gateway contract, and emits audit/provenance refs. Production service authentication, discovery, scaling, operational monitoring, KMS/HSM custody, and organization-owned backend integrations remain external deployment work.
- P2-T9 is complete as a Session Router reference component: `SessionRouter` registers active participants per session, routes CAPEnvelope-like control messages only when sender and receiver are active in that session, supports same-session fanout and multi-session batches, refuses cross-session receiver attempts, and records audit/provenance route metadata without storing raw `payload` bodies. Production service deployment, service authentication, HA state, live Control Plane integration, and operational monitoring remain external deployment work.
- P2-T10 is complete as a Human Review reference integration: `HumanReviewService` turns `escalate` `InterruptDecision` payloads into Local PEP-minimized `HumanReviewRequest` tasks, can route those tasks through `SessionRouter`, calls a `HumanReviewPortal` stub, accepts structured approve/deny/transform/pause decisions, refuses portal requests for raw transcript/audio unless the active privacy policy permits them, and emits audit/provenance refs plus linked `ExecutionReport` objects. Reviewer authentication, production portal/queue deployment, production workflow integration, SLA handling, operational monitoring, and organization-owned review policy remain external deployment work.
- P2-T11 is complete as a reference OpenTelemetry collector and attribute-coverage scaffold: `config/otel/collector-cap.yaml` provides a production-shaped OTLP receiver/processor/exporter config, `cap_protocol.runtime.observability` normalizes `cap.*` attributes, lifecycle tests cover envelope receipt, PEP decision, interrupt, execution, evidence, audit, and refusal events, and validation fails on missing required attributes. Production collector deployment, exporter credentials, retention, backpressure/retry, access control, recovery, and runtime rollout remain external deployment work.
- P2-T12 is complete as signed audit-operation scaffold coverage: `SignedAuditSink` signs audit operations over content-minimized events, the next hash-chain sequence, previous-chain hash, retention/access metadata, key-custody descriptors, and replication policy; `ObservabilityPlane` can require audit confirmation before user-visible delivery; tests cover signature verification, tamper detection, KMS/HSM provider stub fail-closed behavior, replication retry/backpressure, and telemetry failure isolation. Deployed KMS/HSM custody, transparency/replication services, production access-control integration, recovery runbooks, and runtime rollout remain external deployment work.
- P2-T13 is complete as W3C PROV store wiring: `W3CProvenanceSink` converts CAP observability events into content-minimized PROV-JSONLD bundles, `JsonlProvStore` ingests them locally, and tests/conformance cover queryable session lineage across sessions, evidence-to-execution `prov:wasDerivedFrom` links, authority delegation lineage, interrupt lineage, no raw evidence/hidden chain-of-thought inclusion, and provenance store failure isolation from telemetry and audit. Production PROV graph/document store deployment, access-control integration, backup/recovery, retention/deletion operations, and runtime rollout remain external deployment work.
- P2-T14 is complete as service-mesh composition scaffold coverage: `cap_protocol.runtime.service_mesh` builds Istio/Linkerd-style topology metadata and Kubernetes Deployment manifests for an application container plus CAP Edge PEP sidecar, with mesh proxy injection handled by annotations and mesh-owned mTLS/SPIFFE identity. Tests and conformance verify CAP consumes the expected SPIFFE identity without setting `CAP_SPIFFE_ID` or terminating mesh TLS, while Edge PEP still validates CAPEnvelope signature, PolicyRefs, PrivacyBoundary, AuthorityChain, and local fallback behavior. A live mesh smoke test remains external because it requires an Istio/Linkerd/SPIRE cluster.
- P2-T15 is complete as a Temporal-style workflow-engine composition sample: `cap_protocol.runtime.workflow_engine` runs locally without `temporalio`, receives a signed `Directive` CAPEnvelope, verifies it through Edge PEP, routes it through `SessionRouter`, records workflow history with `workflow_id`, `run_id`, `session_id`, and `trace_id`, emits a retry-triggered `pause` `InterruptDecision`, emits a final `ExecutionReport`, and refuses a tampered envelope before activity execution. Deployed Temporal/LangGraph workers, durable external queue/state integration, workflow SLA handling, production human-review workflow wiring, operational monitoring, and organization-owned retry/compensation policy remain external deployment work.
- P2-T16 is complete as Sigstore/Rekor-style transparency scaffold coverage: `cap_protocol.security.transparency` logs release and AuthorityChainStep DSSE/in-toto attestations into deterministic local Rekor-compatible bundles with signed entry timestamps, Merkle inclusion proofs, checkpoint metadata, and offline verification. Tests, hardening, and V1-C15 conformance cover bundle verification and inclusion-proof tamper detection. External Rekor publication, log monitoring, production key custody, release-blocking publication policy, and cross-organization transparency interoperability remain deployment work.
- P2-T17 is complete as deterministic live MCP/A2A substrate interop coverage: `cap_protocol.runtime.substrate_interop` provides an in-process MCP server that routes signed CAPEnvelope `Directive` payloads for `tools/call` and `resources/read` through Edge PEP and service-backed MCP Capability discovery before invoking handlers, refuses forbidden tools before side effects, returns EvidenceRefs in reports, and provides an A2A peer that advertises CAP v1 support in its AgentCard extension and accepts only CAPEnvelope-wrapped messages after Edge PEP validation. External MCP servers and multi-organization A2A interoperability remain deployment/evidence work.
- P2-T18 is complete as a decomposed Controller reference service boundary: `cap_protocol.runtime.controller` adds `ControllerService`, local and HTTP/JSON clients, a PDP-backed Guard evaluator, a scripted Guard evaluator, signed `Directive` CAPEnvelope formation from Controller intents, Session Router delegation, optional ObservabilityPlane emission, substitutable plain/signed audit sink coverage, and an explicit v0.1 `CAPCenter` legacy compatibility report. Production Controller service authentication, HA orchestration state, durable intent state, production Guard/PDP clients, deployed router/observer wiring, and operational monitoring remain deployment work.
- P3-T1 is complete as reference live model-stream integration. `StreamingLookaheadBuffer` now supports wall-clock `tick()` release and abort handling, while `cap_protocol.runtime.live_model_streaming` feeds pull-based local scripted chunks or optional Ollama chunks through the Local PEP, pauses model pulls under sink backpressure, aborts the source on external cancellation or unsafe transforms, applies pre-cached CAP-Med safe substitution before display, and emits linked audit/provenance frame refs. Production model providers, shipping native UI wrappers, deployment-representative latency/resource evaluation, and deployed Local PEP trust modes remain open.
- P3-T2 is complete as a deterministic semantic slow-path classifier beside fast regex checks. `cap_protocol.runtime.slow_path_classifier` defines the classifier interface, CI-safe CAP-Med fallback, and optional Ollama model-as-judge adapter; Local PEP and live streaming now combine fast and slow unsafe decisions before user-visible delivery. Organization-selected model-judge rollout, deployment-representative latency/resource evaluation, shipping native UI wrappers, and production provider deployment remain open.
- P3-T3 is complete as per-platform abort propagation contracts and local client-surface adapters. `cap_protocol.runtime.ui_abort` maps terminal Local PEP stream decisions to CLI and WebSocket-style safe replacement events, clears/replaces visible stream regions instead of surfacing raw transport failures, and declares precise Android/iOS `CapStreamAbort` contracts for native wrappers not present in this repo. Shipping native SDK wrappers, production browser integration, and production provider rollout remain open.
- P3-T4 is complete as correction-frame UX semantics and local client-surface adapters. `cap_protocol.runtime.ui_correction` maps late Local PEP correction frames to CLI and WebSocket-style partial-region replacement plus safe annotation events, preserves partial-emission, original-audit, correction-audit, interrupt, execution-report, and provenance refs, sanitizes unsafe correction copy, and declares Android/iOS `CapStreamCorrection` contracts for native wrappers not present in this repo. Shipping native SDK wrappers, production browser integration, and production provider rollout remain open.
- P3-T5 is complete as a deterministic Android/iOS separately privileged proxy Local PEP scaffold. `cap_protocol.runtime.mobile_local_pep` declares Android `CapLocalPepProxyService` and iOS `CapLocalPepProxyExtension` contracts, platform route controls, manifest-shaped native metadata, and smoke checks that refuse direct user output, network, raw-data egress, local-tool, and missing-OS-route bypass attempts while preserving Local PEP privacy refusals for mediated raw-data egress. Native mobile project wiring, platform entitlements, device/instrumented tests, attested isolation, and review evidence remain open.
- P3-T6 is complete as deterministic attested isolated Local PEP registration. `cap_protocol.runtime.attested_local_pep` defines challenge/response payloads, trusted provider contracts for deterministic TEE, Android Play Integrity, Apple App Attest, Secure Enclave, and TPM quote paths, detached-JWS test-double verification, production verifier hooks, replay detection, workload identity and Local PEP version binding, and a Control Plane registrar that refuses missing, expired, replayed, mismatched, untrusted, or production-verifier-missing attestations before publishing Local PEP capability metadata. Real platform verifiers, native entitlements, device/instrumented tests, and review evidence remain open.
- P3-T7 is complete as deterministic local NER redaction before Supervisor-context egress. `cap_protocol.runtime.redaction` defines a local-only redaction interface, dependency-free fallback, optional caller-supplied local model adapter, and audit-safe payload summaries; `LocalPEP.prepare_supervisor_context(...)` substitutes raw transcript/audio into local EvidenceRefs before redacting person, location, date, contact, medical, and financial spans into category tags. Production local NER model rollout, redaction-quality evaluation, deployed audit/provenance sinks, and bypass-resistant deployment remain open.
- P3-T8 is complete as deterministic embedding-only Supervisor egress. `cap_protocol.runtime.embeddings` defines local-only text and voice encoder protocols, dependency-free deterministic fallback encoders with fixed CI vectors, payload projection helpers, provenance refs, minimization metadata, and recipient-bound PrivacyBoundary checks; `LocalPEP.prepare_supervisor_context(...)` can send embeddings, aggregate dimensions, safety flags, and evidence refs while keeping raw transcript/audio local. Production local embedding model rollout, privacy/quality evaluation, deployed audit/provenance sinks, and bypass-resistant deployment remain open.
- P3-T9 is complete as deterministic retention TTL deletion. `cap_protocol.runtime.retention` maps `PrivacyBoundary.retention` into raw local and audit-retention TTL metadata; `LocalPEP.collect_retention_garbage(...)` deletes expired raw local backing content for substituted EvidenceRefs; `ReferenceCapabilityRegistryService.collect_retention_garbage(...)` deletes expired Evidence Registry backing blobs; deletion audit/provenance records keep hashes, refs, expiry/deletion timestamps, and `raw_content_logged=false` without raw evidence. Durable distributed stores, scheduled retention jobs, legal/organizational policy mapping, production access control, and deployed audit/provenance sinks remain open.
- P3-T10 is complete as a deterministic CAP-SWE non-medical reference profile. `cap_protocol.profiles.cap_swe` defines profile-owned diff evidence, test-result evidence, sandbox attestation, file-write authority, rollback/commit compensation, tool-risk levels, and code-owner escalation under `profile_constraints.cap-swe/v1` and `profile_extensions.cap-swe/v1`; `SoftwareEngineeringAgentProfile` is documented as a profile contract in LinkML; tests and V1-C05 conformance checks validate the same Core objects with CAP-SWE profile data. Production SWE-agent sandboxing, real CI/repository integrations, external profile owners, and cross-implementation profile conformance remain open.
- P3-T11 is complete as local deterministic latency and mobile-resource benchmark evidence. `cap_protocol.benchmarks` measures direct MCP/tool handling versus CAP-mediated MCP `tools/call`, Edge PEP envelope verification, direct user-output emission versus Local PEP gating, direct stream concatenation versus Local PEP live-stream gating, and Android/iOS proxy scaffold user-output paths. `cap-run-v1-benchmarks` publishes JSON and Markdown artifacts under `docs/benchmarks/` with p50/p95 latency, CPU-time proxy units, tracemalloc peak memory, streaming delay, hardware/environment metadata, and explicit caveats. Production native device telemetry, measured battery drain, service-mesh latency, networked registry/PDP latency, production model-provider latency, and Control Plane outage behavior remain open.
- P3-T12 is complete as local third implementation interop evidence. `third_impl/go_cap_adapter` is a standard-library Go adapter that validates shared CAP v1 fixtures, verifies RFC 8785/JCS detached Ed25519 signatures on envelopes and signed payloads, checks required CAPEnvelope fields and temporal bounds, and reports pass/fail status by fixture ID. `tests/test_go_interop_adapter.py` runs the adapter from pytest and verifies unexpected failures remain traceable. This is local third-implementation fixture evidence, not production runtime or external multi-organization interoperability certification.
- P3-T13 is complete as formal lifecycle FSM and profile inheritance scaffolding. `cap_protocol.runtime.lifecycle` defines machine-checkable FSMs for envelope, directive, interrupt, execution, evidence, audit, and provenance states; `cap_protocol.profiles.inheritance` defines deterministic monotonic profile composition, parent-before-child ordering, conflict refusal for widening overrides, tool-risk strictness, and Core lifecycle/interrupt override refusal. `tests/test_lifecycle_profile_inheritance.py` and V1-C05/V1-C15 conformance cover illegal transitions and profile conflict resolution. Production profile-owner governance and external conformance remain open.
- P3-T14 is complete as CAP-Med v1 runtime-profile migration. `cap_protocol.profiles.cap_med` defines profile-owned non-diagnostic, non-prescriptive, raw-transcript/audio minimization, Supervisor-context, Local PEP veto, and Supervisor-overreach rules under `profile_constraints.cap-med/v1` and `profile_extensions.cap-med/v1`; the profile fixture validates against the same v1 Core `CAPEnvelope`, `PrivacyBoundary`, `OperationalConstraints`, `Capability`, `Directive`, `EvidenceRef`, and `InterruptDecision` schemas. Tests and V1-C05 conformance cover signed hot-path execution through Edge PEP, Local PEP raw-transcript minimization, unified Capability records, Core interrupt-action mapping, and Supervisor Gateway overreach refusal. v0.1 CAP-Med constraints remain legacy compatibility evidence; regulated-profile/domain review remains an external gate.
- P4-T1 is complete as an independent security review preparation packet. `docs/security_review/README.md` lists architecture, trust boundaries, high-risk components, review focus, verification commands, open external gaps, and evidence links; `docs/security_review/findings_tracker_template.md` provides the findings tracker template. The independent third-party security review gate remains open until external review completion and critical-finding remediation.
- P4-T2 is complete as a production KMS/HSM custody and operations plan. `docs/kms_hsm/README.md` documents key roles, custody, rotation, revocation, incident response, auditability, signer interfaces, and deployment-owned evidence; `config/kms_hsm.example.yaml` is a non-secret placeholder shape only. The production KMS/HSM gate remains open until a deployment organization supplies real KMS/HSM evidence.
- P4-T3 is complete as an organization-specific OPA/Cedar deployment guide. `docs/policy_deployment/README.md` documents policy ownership, environment separation, change control, rollout, rollback, hot updates, emergency overrides, test promotion, and deployment evidence; `config/policy_deployment.example.yaml` and `policies/organization_template/` provide non-production placeholders. The organization-specific policy gate remains open until a deployment organization supplies real policy runtime and promotion evidence.
- P4-T4 is complete as a multi-organization MCP/A2A interoperability plan. `docs/mcp_a2a_interop/README.md` defines partner setup, trust roots, registry records, fixtures, required pass/fail cases, logging/privacy constraints, local simulation mode, and gate-closure rules; `docs/mcp_a2a_interop/report_template.md` provides the external evidence report shape; `config/mcp_a2a_interop.example.yaml` is a non-secret placeholder shape only. The live multi-organization interop gate remains open until independent partner organizations run the plan and provide acceptable evidence.
- P4-T5 is complete as a domain semantic-quality evaluation harness. `cap_protocol.evaluation.semantic_quality` aggregates reviewer JSONL scores separately from structural CAP conformance, `docs/domain_semantic_quality/README.md` defines datasets, reviewer criteria, scoring, privacy handling, artifacts, and release-gate rules, `docs/domain_semantic_quality/reviewer_rubric.md` and `docs/domain_semantic_quality/report_template.md` provide reviewer/report templates, `examples/domain_semantic_quality/` provides synthetic onboarding fixtures, and `config/domain_semantic_quality.example.yaml` is a non-secret placeholder shape only. The semantic-quality gate remains open until qualified domain experts or profile owners provide non-synthetic review evidence under the documented privacy rules.
- P4-T6 is complete as a regulated-profile review packet. `docs/regulated_profile_review/README.md` collects CAP-Med profile constraints, forbidden behaviors, escalation rules, privacy controls, user-facing refusals/corrections, evidence examples, test references, and known limitations; `docs/regulated_profile_review/reviewer_checklist.md`, `docs/regulated_profile_review/open_questions.md`, and `docs/regulated_profile_review/report_template.md` provide reviewer workflow artifacts; `config/regulated_profile_review.example.yaml` is a non-secret placeholder shape only. The regulated-profile review gate remains open until qualified external profile reviewers complete the review and accepted evidence is recorded.
- CI/release verification now distinguishes the existing v0.1 fixture conformance from the release-blocking deterministic v1 scaffold gate through `run_v1_conformance_release_gate` and `cap-check-v1-conformance`.

Deterministic scaffold limitations:

- P1-SEC-02 remains a reference-service and Biscuit-token integration, not a production KMS/HSM signing-custody or deployed revocation service implementation.

Still open:

- Production hardening/deployment for Controller, Session Router, Human Review portal/workflow integration, deployed Temporal/LangGraph workflow integration, PDP/Policy/Capability/Evidence Registry services, organization-owned OPA/Cedar policy runtime integration, production-grade Local PEP trust modes, production model-provider rollout and shipping native UI wrappers around the reference live adapter, native/device performance telemetry, measured battery drain, production local NER and embedding model rollout plus quality/privacy evaluation, regulated-profile review evidence, production Supervisor Gateway rollout, organization-owned backend engine integration, external Istio/Linkerd/SPIRE mesh rollout, deployed KMS/HSM audit custody, external Sigstore/Rekor publication and monitoring, transparency/replication services, production PROV graph/document store operations, and production observability exporter/collector operations remain open.
- The gRPC and HTTP/JSON demos use v1 `CAPEnvelope` hot paths plus selected Local PEP, Edge PEP, and service-backed Agent/Tool discovery mediation, but they still do not wire production Local PEP/Edge PEP trust modes, external service-mesh cluster deployment, or live external registry services.
- Full production v1 conformance certification remains open; P1-CONF-01 through P1-CONF-08 and P1-T10 are release-blocking deterministic scaffold/test coverage, not a complete runtime certification.
- Automated LinkML-to-JSON-Schema replacement is not yet wired into runtime validation. The current P1-SCHEMA-06 implementation intentionally uses a CI-friendly drift gate for essential LinkML/JSON Schema alignment while checked-in JSON Schema artifacts remain reviewed manually.

## Task Prompt Library

Each task below has a standalone implementation-ready prompt in `docs/task_prompts/cap_v1/`. These prompts are designed for incremental follow-up work. They restate source priority, current implementation status, files to inspect, implementation scope, acceptance criteria, verification commands, and final-response expectations.

No next-task prompts remain open. `docs/task_prompts/cap_v1/Open/README.md` is retained as the empty open-prompt index, and completed task records live under `docs/task_prompts/cap_v1/Done/`.

Open prompt coverage:

- All P1 hot-path foundation prompts are complete. `P1-T1` through `P1-T10` are recorded under completed prompt evidence.
- All Phase 2 service, registry, and substrate prompts are complete. `P2-T1` through `P2-T18` are recorded under completed prompt evidence.
- All Phase 3 streaming, trust-mode, profile, and evaluation prompts are complete. `P3-T1` through `P3-T14` are recorded under completed prompt evidence.
- All Phase 4 external-gate preparation prompts are complete. `P4-T1` through `P4-T6` are recorded under completed prompt evidence, while external review/evidence gates remain open where documented.

Completed prompt index:

| ID | Prompt file |
|---|---|
| DOC-FIX-01 | `docs/task_prompts/cap_v1/Done/DOC-FIX-01_operationalconstraints_human_confirmation_placement.md` |
| DOC-FIX-02 | `docs/task_prompts/cap_v1/Done/DOC-FIX-02_privacyboundary_dimension_count_alignment.md` |
| DOC-FIX-03 | `docs/task_prompts/cap_v1/Done/DOC-FIX-03_streaming_buffer_default_and_diagram_alignment.md` |
| DOC-FIX-04 | `docs/task_prompts/cap_v1/Done/DOC-FIX-04_capability_shape_inline_documentation.md` |
| DOC-FIX-05 | `docs/task_prompts/cap_v1/Done/DOC-FIX-05_legacy_interrupt_vocabulary_rewrite.md` |
| DOC-FIX-06 | `docs/task_prompts/cap_v1/Done/DOC-FIX-06_normative_streaming_terminology.md` |
| P0-DOC-01 | `docs/task_prompts/cap_v1/Done/P0-DOC-01_reframe_public_docs.md` |
| P0-DOC-02 | `docs/task_prompts/cap_v1/Done/P0-DOC-02_two_tier_three_plane_architecture.md` |
| P0-DOC-03 | `docs/task_prompts/cap_v1/Done/P0-DOC-03_therapist_supervisor_scenario.md` |
| P0-DOC-04 | `docs/task_prompts/cap_v1/Done/P0-DOC-04_current_vs_target_alignment.md` |
| P0-DOC-05 | `docs/task_prompts/cap_v1/Done/P0-DOC-05_localhost_proxy_testing_caveat.md` |
| P1-SCHEMA-01 | `docs/task_prompts/cap_v1/Done/P1-SCHEMA-01_cap_envelope.md` |
| P1-SCHEMA-02 | `docs/task_prompts/cap_v1/Done/P1-SCHEMA-02_interrupt_decision.md` |
| P1-SCHEMA-03 | `docs/task_prompts/cap_v1/Done/P1-SCHEMA-03_privacy_boundary.md` |
| P1-SCHEMA-04 | `docs/task_prompts/cap_v1/Done/P1-SCHEMA-04_operational_constraints.md` |
| P1-SCHEMA-05 | `docs/task_prompts/cap_v1/Done/P1-SCHEMA-05_capability.md` |
| P1-SCHEMA-06 | `docs/task_prompts/cap_v1/Done/P1-SCHEMA-06_linkml_json_schema_generation.md` |
| P1-SEC-01 | `docs/task_prompts/cap_v1/Done/P1-SEC-01_canonicalization_signing.md` |
| P1-SEC-02 | `docs/task_prompts/cap_v1/Done/P1-SEC-02_cap_warrant_authority_chain.md` |
| P1-T1 | `docs/task_prompts/cap_v1/Done/P1-T1_migrate_grpc_reference_binding_to_capenvelope.md` |
| P1-T2 | `docs/task_prompts/cap_v1/Done/P1-T2_migrate_http_json_binding_to_capenvelope.md` |
| P1-T3 | `docs/task_prompts/cap_v1/Done/P1-T3_implement_rfc_8785_jcs_for_v1_signatures.md` |
| P1-T4 | `docs/task_prompts/cap_v1/Done/P1-T4_wire_local_pep_onto_agent_to_user_and_local_tool_paths.md` |
| P1-T5 | `docs/task_prompts/cap_v1/Done/P1-T5_wire_edge_pep_onto_cross_boundary_paths.md` |
| P1-T6 | `docs/task_prompts/cap_v1/Done/P1-T6_implement_runtime_interruptdecision_and_composition_rules.md` |
| P1-T7 | `docs/task_prompts/cap_v1/Done/P1-T7_implement_structured_privacyboundary_pdp_evaluation.md` |
| P1-T8 | `docs/task_prompts/cap_v1/Done/P1-T8_apply_clock_skew_and_expiry_uniformly.md` |
| P1-T9 | `docs/task_prompts/cap_v1/Done/P1-T9_use_capability_as_unified_registration_object.md` |
| P1-T10 | `docs/task_prompts/cap_v1/Done/P1-T10_make_v1_c01_through_v1_c15_release_blocking.md` |
| P1-CONF-01 | `docs/task_prompts/cap_v1/Done/P1-CONF-01_replay_idempotency.md` |
| P1-CONF-02 | `docs/task_prompts/cap_v1/Done/P1-CONF-02_clock_skew_expiry.md` |
| P1-CONF-03 | `docs/task_prompts/cap_v1/Done/P1-CONF-03_stale_policy_hot_update.md` |
| P1-CONF-04 | `docs/task_prompts/cap_v1/Done/P1-CONF-04_evidence_tamper.md` |
| P1-CONF-05 | `docs/task_prompts/cap_v1/Done/P1-CONF-05_offline_fallback.md` |
| P1-CONF-06 | `docs/task_prompts/cap_v1/Done/P1-CONF-06_sidecar_bypass.md` |
| P1-CONF-07 | `docs/task_prompts/cap_v1/Done/P1-CONF-07_streaming_correction.md` |
| P1-CONF-08 | `docs/task_prompts/cap_v1/Done/P1-CONF-08_supervisor_overreach.md` |
| P2-RUNTIME-01 | `docs/task_prompts/cap_v1/Done/P2-RUNTIME-01_local_pep.md` |
| P2-RUNTIME-02 | `docs/task_prompts/cap_v1/Done/P2-RUNTIME-02_edge_pep.md` |
| P2-RUNTIME-03 | `docs/task_prompts/cap_v1/Done/P2-RUNTIME-03_streaming_lookahead_buffer.md` |
| P2-RUNTIME-04 | `docs/task_prompts/cap_v1/Done/P2-RUNTIME-04_offline_policy_bundle_cache.md` |
| P2-RUNTIME-05 | `docs/task_prompts/cap_v1/Done/P2-RUNTIME-05_supervisor_gateway_stub.md` |
| P2-RUNTIME-06 | `docs/task_prompts/cap_v1/Done/P2-RUNTIME-06_federated_registry_stubs.md` |
| P2-RUNTIME-07 | `docs/task_prompts/cap_v1/Done/P2-RUNTIME-07_observability_plane_sinks.md` |
| P2-T1 | `docs/task_prompts/cap_v1/Done/P2-T1_deploy_capability_registry_service.md` |
| P2-T2 | `docs/task_prompts/cap_v1/Done/P2-T2_deploy_policy_registry_and_signed_bundle_distribution.md` |
| P2-T3 | `docs/task_prompts/cap_v1/Done/P2-T3_deploy_agent_and_tool_registry_services.md` |
| P2-T4 | `docs/task_prompts/cap_v1/Done/P2-T4_deploy_evidence_registry.md` |
| P2-T5 | `docs/task_prompts/cap_v1/Done/P2-T5_implement_cedar_pdp_adapter.md` |
| P2-T6 | `docs/task_prompts/cap_v1/Done/P2-T6_integrate_biscuit_or_tenuo_warrant_primitive.md` |
| P2-T7 | `docs/task_prompts/cap_v1/Done/P2-T7_integrate_spiffe_spire_workload_identity.md` |
| P2-T8 | `docs/task_prompts/cap_v1/Done/P2-T8_deploy_supervisor_gateway_service.md` |
| P2-T9 | `docs/task_prompts/cap_v1/Done/P2-T9_implement_session_router.md` |
| P2-T10 | `docs/task_prompts/cap_v1/Done/P2-T10_implement_human_review_integration.md` |
| P2-T11 | `docs/task_prompts/cap_v1/Done/P2-T11_wire_opentelemetry_collector_and_attribute_coverage.md` |
| P2-T12 | `docs/task_prompts/cap_v1/Done/P2-T12_implement_signed_audit_operations.md` |
| P2-T13 | `docs/task_prompts/cap_v1/Done/P2-T13_wire_w3c_prov_store.md` |
| P2-T14 | `docs/task_prompts/cap_v1/Done/P2-T14_implement_service_mesh_composition_test.md` |
| P2-T15 | `docs/task_prompts/cap_v1/Done/P2-T15_implement_workflow_engine_composition_sample.md` |
| P2-T16 | `docs/task_prompts/cap_v1/Done/P2-T16_integrate_sigstore_and_rekor_transparency.md` |
| P2-T17 | `docs/task_prompts/cap_v1/Done/P2-T17_implement_live_mcp_and_a2a_substrate_interop.md` |
| P2-T18 | `docs/task_prompts/cap_v1/Done/P2-T18_split_controller_into_distinct_deployable.md` |
| P3-T1 | `docs/task_prompts/cap_v1/Done/P3-T1_integrate_live_model_streaming.md` |
| P3-T2 | `docs/task_prompts/cap_v1/Done/P3-T2_implement_slow_path_classifier.md` |
| P3-T3 | `docs/task_prompts/cap_v1/Done/P3-T3_implement_ui_abort_propagation_per_platform.md` |
| P3-T4 | `docs/task_prompts/cap_v1/Done/P3-T4_design_and_implement_correction_frame_ux.md` |
| P3-T5 | `docs/task_prompts/cap_v1/Done/P3-T5_implement_mobile_separately_privileged_proxy_local_pep.md` |
| P3-T6 | `docs/task_prompts/cap_v1/Done/P3-T6_implement_attested_isolated_local_pep.md` |
| P3-T7 | `docs/task_prompts/cap_v1/Done/P3-T7_implement_local_ner_redaction_pipeline.md` |
| P3-T8 | `docs/task_prompts/cap_v1/Done/P3-T8_implement_embedding_only_egress.md` |
| P3-T9 | `docs/task_prompts/cap_v1/Done/P3-T9_implement_retention_timers_and_ttl_deletion.md` |
| P3-T10 | `docs/task_prompts/cap_v1/Done/P3-T10_build_cap_swe_non_medical_reference_profile.md` |
| P3-T11 | `docs/task_prompts/cap_v1/Done/P3-T11_benchmark_latency_and_mobile_resource_budget.md` |
| P3-T12 | `docs/task_prompts/cap_v1/Done/P3-T12_build_third_implementation_interop.md` |
| P3-T13 | `docs/task_prompts/cap_v1/Done/P3-T13_formalize_lifecycle_fsm_and_profile_inheritance.md` |
| P3-T14 | `docs/task_prompts/cap_v1/Done/P3-T14_migrate_cap_med_v1_profile_end_to_end.md` |
| P4-T1 | `docs/task_prompts/cap_v1/Done/P4-T1_prepare_independent_security_review_package.md` |
| P4-T2 | `docs/task_prompts/cap_v1/Done/P4-T2_prepare_production_kms_hsm_operations_plan.md` |
| P4-T3 | `docs/task_prompts/cap_v1/Done/P4-T3_prepare_organization_specific_opa_cedar_deployment_guide.md` |
| P4-T4 | `docs/task_prompts/cap_v1/Done/P4-T4_prepare_multi_organization_mcp_a2a_interop_plan.md` |
| P4-T5 | `docs/task_prompts/cap_v1/Done/P4-T5_prepare_domain_semantic_quality_evaluation_harness.md` |
| P4-T6 | `docs/task_prompts/cap_v1/Done/P4-T6_prepare_regulated_profile_review_packet.md` |
| P2-DOC-01 | `docs/task_prompts/cap_v1/Done/P2-DOC-01_architecture_diagrams.md` |
| P2-DOC-02 | `docs/task_prompts/cap_v1/Done/P2-DOC-02_therapist_supervisor_sequences.md` |
| P2-DOC-03 | `docs/task_prompts/cap_v1/Done/P2-DOC-03_schema_appendix_migration.md` |
| P2-DOC-04 | `docs/task_prompts/cap_v1/Done/P2-DOC-04_v1_release_gates.md` |

## Scenario Contract

The motivating test scenario uses **Therapist** as the local interviewer persona and **Supervisor** as the main/central strategy and review role.

The Therapist persona must remain:

- non-diagnostic;
- non-prescriptive;
- privacy-preserving by default;
- subject to Local PEP streaming and privacy enforcement;
- allowed to emit supportive, reflective interview language only inside profile constraints.

The Supervisor:

- issues structured strategy or control directives through a Supervisor Gateway;
- receives redacted context and evidence references by default, or embedding-only context when policy requests it;
- is not allowed to bypass Local PEP privacy, non-diagnostic, jurisdiction, or safety vetoes;
- may be a model, human, or rule engine behind a CAP-facing gateway.

CAP keeps three Supervisor meanings separate:

- the Supervisor authority role that may issue or approve strategy;
- the Supervisor Gateway endpoint that validates, privacy-filters, and mediates supervisor output;
- the model, human, rule engine, or workflow behind the gateway.

## P0 - Documentation Alignment

| ID | Task | Type | Dependencies | Acceptance criteria |
|---|---|---|---|---|
| P0-DOC-01 | Reframe high-level docs from only "Control Authority Profile" to v1 "Control Authority Protocol / Supervisory Control Plane" while preserving current implementation status. | Documentation | None | `README.md`, `CAP_00_README.md`, and `architecture.md` distinguish v1 target architecture from v0.1 implementation evidence. |
| P0-DOC-02 | Document the hybrid two-tier, three-plane architecture. | Documentation | P0-DOC-01 | Docs name Local PEP, Edge PEP, decomposed Control Plane, PDP, federated registries, and independent observability plane. |
| P0-DOC-03 | Add explicit Therapist/Supervisor scenario wording. | Documentation | P0-DOC-01 | Docs state Therapist is a non-diagnostic local interviewer persona and Supervisor is the central/main authority participant behind a gateway. |
| P0-DOC-04 | Document current-vs-target implementation status. | Documentation | P0-DOC-01 | `CAP_IMPLEMENTATION_ALIGNMENT.md` lists v0.1 evidence and v1 gaps without overclaiming. |
| P0-DOC-05 | Record local test environment proxy caveat. | Documentation | None | Backlog or alignment docs mention that this workspace needs `NO_PROXY=127.0.0.1,localhost` for localhost HTTP smoke tests. |

## P1 - v1 Core Object Model

| ID | Task | Type | Dependencies | Acceptance criteria |
|---|---|---|---|---|
| P1-SCHEMA-01 | Define v1 `CAPEnvelope`. | Schema + tests | P0-DOC-02 | Schema includes `envelope_id`, `session_id`, `trace_id`, `sender_id`, `receiver_id`, `message_kind`, `payload` or `payload_ref`, `authority_chain_ref`, `policy_refs`, `privacy_boundary_ref`, `timestamp`, `ttl_ms`, and `signature`; examples validate. |
| P1-SCHEMA-02 | Define v1 `InterruptDecision`. | Schema + runtime + tests | P1-SCHEMA-01 | Schema and fixtures cover `allow`, `deny`, `transform`, `constrain`, `pause`, `escalate`, and `reroute` plus restrictive composition rules. |
| P1-SCHEMA-03 | Define structured `PrivacyBoundary`. | Schema + policy tests | P1-SCHEMA-01 | Boundary supports nine first-class dimensions: classification, movement, transformation, retention, logging, audit visibility, allowed recipients, raw-data egress rules, and minimization; Therapist/Supervisor fixtures block raw transcript/audio egress. |
| P1-SCHEMA-04 | Split `ConstraintSet` into Core `OperationalConstraints` and profile constraints. | Schema + docs + tests | P1-SCHEMA-01 | Generic constraints remain Core; non-diagnostic response style and psychometric strategy move into profile extensions. |
| P1-SCHEMA-05 | Collapse agent/tool capability metadata into a `Capability` object with `kind` discriminator. | Schema + docs | P1-SCHEMA-01 | Agent and Tool capability examples share one structure and preserve A2A/MCP-specific endpoint metadata through extension metadata. |
| P1-SCHEMA-06 | Automate or scaffold LinkML-to-JSON-Schema generation/drift checking. | Schema tooling + CI | P1-SCHEMA-01 through P1-SCHEMA-05 | CI can compare checked-in JSON Schema artifacts against LinkML without changing runtime behavior; drift between LinkML and JSON Schema fails clearly. |
| P1-SEC-01 | Specify canonicalization and signing rules for signed Core objects. | Docs + security tests | P1-SCHEMA-01 | Signed-object docs pick a canonicalization rule, identify signing targets, and include invalid-signature and tamper tests. |
| P1-SEC-02 | Define CAP Warrant binding for authority chains. | Docs + schema + tests | P1-SEC-01 | AuthorityChain steps bind identity, capability, scope, expiry, revocation, and attenuation; docs allow Biscuit, Tenuo, Macaroons, or equivalent profile-selected primitives. |

## P1 - Conformance and Failure Modes

| ID | Task | Type | Dependencies | Acceptance criteria |
|---|---|---|---|---|
| P1-CONF-01 | Add replay and idempotency adversarial tests. | Tests | P1-SCHEMA-01 | Replayed directives cannot trigger duplicate execution. |
| P1-CONF-02 | Add clock-skew and expiry tests. | Tests | P1-SEC-01 | Objects outside profile skew tolerance are refused. |
| P1-CONF-03 | Add stale policy and hot-update tests. | Tests | P1-SCHEMA-03 | Policy version changes are pinned per session or force re-evaluation according to profile. |
| P1-CONF-04 | Add evidence tamper tests. | Tests | Existing EvidenceRef validation | Changed backing content produces `evidence_hash_mismatch`. |
| P1-CONF-05 | Add offline fallback tests. | Tests + runtime | P2-RUNTIME-04 | Local PEP uses cached signed policy bundle; sensitive output fails closed if the bundle is missing, expired, or has invalid signature metadata. |
| P1-CONF-06 | Add sidecar-bypass tests for high-assurance profiles. | Tests + runtime | P2-RUNTIME-01 | Agent cannot reach user, network, or local tools outside the Local PEP path. |
| P1-CONF-07 | Add streaming correction tests. | Tests + runtime | P2-RUNTIME-03 | Buffered unsafe output is transformed before display; late detection emits a correction frame and audit/report linkage. |
| P1-CONF-08 | Add Supervisor overreach tests. | Tests + policy | P1-SCHEMA-03 | Supervisor requests for raw transcripts, raw audio, diagnosis, or treatment advice are vetoed by Local PEP policy. |

## P2 - Runtime Architecture Migration

| ID | Task | Type | Dependencies | Acceptance criteria |
|---|---|---|---|---|
| P2-RUNTIME-01 | Extract reusable Local PEP component. | Runtime + tests | P1-SCHEMA-01, P1-SCHEMA-03 | Local PEP enforces privacy, evidence-reference substitution, refusal, and local output gating for the Therapist persona. |
| P2-RUNTIME-02 | Add Edge PEP component. | Runtime + tests | P1-SCHEMA-01 | Edge PEP validates v1 CAPEnvelope signatures and policy at network/message boundaries. |
| P2-RUNTIME-03 | Implement streaming lookahead buffer. | Runtime + tests | P1-SCHEMA-02 | Local PEP supports profile-configured token/time buffer and correction-frame path. |
| P2-RUNTIME-04 | Implement offline signed policy bundle cache. | Runtime + tests | P1-SEC-01 | Local PEP can operate safely when the Control Plane is unreachable and fails closed when policy material is invalid. |
| P2-RUNTIME-05 | Add Supervisor Gateway stub. | Runtime + tests | P1-SCHEMA-02, P1-SCHEMA-03 | Supervisor output is structured, privacy-filtered, authority-checked, and translated into directives or interrupt decisions. |
| P2-RUNTIME-06 | Add federated registry stubs. | Runtime + tests | P1-SCHEMA-05 | Capability, Policy, and Evidence registry APIs exist as deterministic stubs with cache/version semantics; Capability views cover agent, tool, service, human, and policy subjects. |
| P2-RUNTIME-07 | Split observability plane sinks. | Runtime + docs | Existing OTel/PROV exports | Audit, telemetry, and provenance are emitted through distinct code paths with distinct retention/integrity assumptions. |

## P2 - Documentation and Examples

| ID | Task | Type | Dependencies | Acceptance criteria |
|---|---|---|---|---|
| P2-DOC-01 | Add v1 architecture diagrams. | Documentation | P0-DOC-02 | Diagrams show data, control, and observability planes plus Local PEP, Edge PEP, PDP, registries, Supervisor Gateway, and Human Review. |
| P2-DOC-02 | Add Therapist/Supervisor sequence examples. | Documentation + examples | P1-SCHEMA-02, P1-SCHEMA-03 | Examples cover safe pass-through, diagnostic transform, supervisor pause, self-harm escalation, and offline fallback. |
| P2-DOC-03 | Update schema appendix after migration. | Documentation | P1 schema tasks | Appendix reflects v1 object names and keeps v0.1 compatibility notes where needed. |
| P2-DOC-04 | Update release gates for v1. | Documentation | P1/P2 implementation status | Release gates distinguish v0.1 candidate, v1 documented architecture, and v1 implemented runtime. |

## Test Baseline

Use the repo-local virtual environment:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

Current observed baseline for this workspace after P3-T9: `299 passed, 1 skipped`.

Plain `pytest` can fail in this environment because localhost urllib traffic from the HTTP/JSON smoke test may be routed through system proxy software and return `HTTP Error 500: Internal Privoxy Error`. This is a local testing caveat, not a CAP protocol requirement.
