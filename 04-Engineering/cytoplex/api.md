> **Status**: Active
> **Date**: 2026-06-14
> **Author**: @mohammadi
> **Audience**: engineers
> **Tags**: `cytoplex`, `cap`, `api`, `reference`

# API

## CLI

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

## Core Modules

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

## Data Artifacts

- Compatibility implementation JSON schemas: `schemas/cap-core/v0.1/*.schema.json` and `schemas/cap-med/v0.1/*.schema.json`
- CAP v1 LinkML authoring schemas: `schemas/cap.yaml`, `schemas/core.yaml`, and `schemas/domains/*.yaml`
- Initial CAP v1 target schemas and examples: `schemas/cap-core/v1/*.schema.json` and `examples/cap-core/v1/*.json`
- Policies: `policies/cap_core_policy.json` and `policies/cap_med_policy.json`
- Fixtures: `src/cap_protocol/conformance/fixtures/adversarial.jsonl`
- Third implementation interop fixture suite: `third_impl/go_cap_adapter/testdata/cap_v1_interop.json`
- Authority-chain schema: `schemas/cap-core/v0.1/authority-chain-step.schema.json`
- Local benchmark artifacts: `docs/benchmarks/cap_v1_latency_mobile_budget.json` and `docs/benchmarks/cap_v1_latency_mobile_budget.md`

## Import Example

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
