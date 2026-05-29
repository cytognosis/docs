# CAP V1 Baseline: Conformance, Testing, and Release Gates

**Generated:** 2026-05-25T06:54:46+00:00
**Document set:** CAP V1 baseline consolidated Markdown set
**Repository status:** V1 architecture documented and V1 runtime scaffold present; current executable package remains `v0.1-production-candidate` and is not a complete stable V1 runtime.
**Purpose:** Conformance model, test execution, release gates, and stable-release requirements.

This file is part of `docs/v1_baseline/`, the capped baseline V1 documentation folder. It preserves and consolidates source documentation from the repository. Local links in preserved source sections are rewritten to resolve from this generated baseline file.

## Source Map

- `docs/CAP_06_conformance.md`
- `docs/testing.md`
- `docs/CAP_RELEASE_GATES.md`
## Source: `docs/CAP_06_conformance.md`

## CAP_06 — Conformance

CAP conformance validates semantic behavior. An implementation may pass using any transport or framework.

The checked-in fixture suite is the current v0.1 production-candidate conformance baseline. CAP v1 extends the target conformance scope to Local PEP, Edge PEP, privacy-boundary, interrupt, offline, lifecycle FSM, profile inheritance, and adversarial failure-mode behavior. The repository now includes a `cap-v1-release-blocking-scaffold` gate that maps V1-C01 through V1-C15 to executable deterministic scaffold checks. It also includes a local Go third-implementation fixture adapter under `third_impl/go_cap_adapter` for shared CAPEnvelope/JCS/signature fixture validation. These gates are release-blocking or traceability evidence for this repository's current v1 scaffold; they are not full CAP v1 runtime certification.

Domain semantic-quality evaluation is deliberately separate from these conformance gates. The harness in `cap_protocol.evaluation.semantic_quality` and the runbook in `docs/domain_semantic_quality/README.md` score profile/domain output quality, reviewer criteria, and blocking domain flags; they do not validate CAPEnvelope, PEP, registry, authority, or observability mechanics.

### 1. Conformance levels

| Level | Meaning |
|---|---|
| Core Producer | Can emit schema-valid CAP Core messages. |
| Core Consumer | Can validate and process CAP Core messages and enforce lifecycle invariants. |
| Core Executor | Can accept/refuse Directives, enforce constraints, and emit ExecutionReports. |
| Core Guard | Can emit GuardDecision objects from policy inputs. |
| Core Observer | Can emit required OpenTelemetry attributes and/or PROV mappings. |
| Profile Conformant | Implements Core plus one named profile's extra rules. |

A complete CAP Core implementation SHOULD include Executor, Guard, and Observer behavior.

### 2. Required semantic tests

Each test includes the expected result. A conformance harness SHOULD provide machine-readable fixtures for all test inputs.

| ID | Test | Preconditions | Expected result |
|---|---|---|---|
| C01 | Valid execution | Valid Directive, valid authority, allow GuardDecision, fresh evidence. | Executor accepts and emits `ExecutionReport.status=succeeded`. |
| C02 | Expired Directive | Directive expiry is in the past. | `RefusalMessage.reason_code=expired`. |
| C03 | Unauthorized Directive | AuthorityChain missing required capability. | `RefusalMessage.reason_code=unauthorized`. |
| C04 | Invalid signature | Authority step signature invalid. | `RefusalMessage.reason_code=invalid_signature`. |
| C05 | Missing evidence | Required evidence not resolvable. | `RefusalMessage.reason_code=missing_evidence`. |
| C06 | Stale evidence | EvidenceRef expired or freshness policy fails. | `RefusalMessage.reason_code=stale_evidence`. |
| C07 | Evidence hash mismatch | Evidence bytes do not match EvidenceRef hash. | `RefusalMessage.reason_code=evidence_hash_mismatch`. |
| C08 | Evidence access denied | Executor lacks evidence read permission. | `RefusalMessage.reason_code=evidence_access_denied`. |
| C09 | Forbidden tool | Action target appears in effective `forbidden_tools`. | `RefusalMessage.reason_code=forbidden_tool`. |
| C10 | Allow with constraints | Guard narrows max wall time and allowed tools. | Executor enforces narrowed values. |
| C11 | Constraint conflict | Guard constraints cannot be safely merged. | Safe denial or `RefusalMessage.reason_code=conflicting_guards`. |
| C12 | Guard deny | Required GuardDecision is `deny`. | Directive does not reach execution. |
| C13 | Multiple Guards deterministic | Two Guards produce non-conflicting constraints. | Effective constraints deterministic and most restrictive. |
| C14 | Conflicting Guards | One Guard allows, one denies. | Deny wins. |
| C15 | Duplicate delivery | Same Directive/idempotency key delivered twice. | Second delivery returns same result or safe refusal. |
| C16 | ExecutionReport integrity | Report references zero or multiple Directives. | Consumer rejects report. |
| C17 | Side-effect reporting | Action mutates external state. | ExecutionReport includes SideEffect. |
| C18 | Compensation success | Reversible side effect compensated. | Terminal state `compensated` and report references original side effect. |
| C19 | Compensation failure | Compensation attempt fails. | Report includes failure and terminal failure/partial state. |
| C20 | MCP constrained invocation | Directive allows one MCP tool and forbids another. | Executor invokes only allowed tool. |
| C21 | A2A metadata carriage | A2A Task carries CAP Directive metadata. | Receiver extracts and validates CAP Directive. |
| C22 | OTel emission | Lifecycle reaches terminal state. | Required `cap.*` telemetry attributes emitted. |
| C23 | PROV mapping | Terminal trace available. | PROV graph includes Agents, EvidenceRef entity, execution activity, result entity. |
| C24 | No CoT leakage | DecisionRecord provided. | Hidden reasoning/scratchpad absent; rationale bounded. |
| C25 | Prompt-injection evidence | Evidence contains text instructing tool escalation. | ConstraintSet remains authoritative; escalation blocked. |
| C26 | Stale policy | PolicyRef digest/version no longer accepted. | GuardDecision `require_policy_update` or refusal `stale_policy`. |
| C27 | Late deny | Guard deny arrives while action is executing. | Executor aborts if safe or records compensation requirement. |
| C28 | Unsupported action | Executor does not support action kind. | `RefusalMessage.reason_code=unsupported_action`. |

### 2.1 CAP v1 release-blocking scaffold cases

V1-C01 through V1-C15 are executable release-blocking cases for the deterministic v1 scaffold. They run through `cap-check-v1-conformance` or `python -m cap_protocol.conformance.v1_runner`; `python VERIFY_RELEASE_BASELINE.py` also fails if any required case fails.

Every row below has two statuses:

- `required_deterministic_scaffold`: this repository's release verifier must pass the mapped executable checks.
- `external_gate_deferred`: full production/runtime certification still requires the named owner to supply deployment evidence beyond the deterministic scaffold.

| ID | Case | Release status | Owner | Executable evidence | Full-runtime external gate |
|---|---|---|---|---|---|
| V1-C01 | CAPEnvelope signature | `required_deterministic_scaffold` | Edge PEP / Security | `src/cap_protocol/runtime/edge_pep.py`, `src/cap_protocol/runtime/authority.py`, `src/cap_protocol/runtime/warrants.py`, `src/cap_protocol/runtime/workload_identity.py`, `src/cap_protocol/runtime/service_mesh.py`, `src/cap_protocol/security/cap_crypto.py`, `tests/test_cap_v1_pep.py`, `tests/test_authority_chain.py`, `tests/test_warrant_primitives.py`, `tests/test_spiffe_workload_identity.py`, `tests/test_service_mesh_composition.py`, `src/cap_protocol/conformance/v1_runner.py` | Production Edge PEP routing, external Istio/Linkerd/SPIRE rollout, registry-backed key discovery, KMS/HSM signing custody, and externally owned cross-implementation signing fixtures beyond the local Go adapter. |
| V1-C02 | InterruptDecision primitive set | `required_deterministic_scaffold` | Interrupt Runtime | `src/cap_protocol/runtime/interrupts.py`, `tests/test_interrupt_runtime.py`, `src/cap_protocol/conformance/v1_runner.py` | Deployed logical Interrupt Manager with durable state and cross-service conflict coordination. |
| V1-C03 | Streaming diagnostic transform | `required_deterministic_scaffold` | Local PEP / Streaming | `src/cap_protocol/runtime/local_pep.py`, `src/cap_protocol/runtime/slow_path_classifier.py`, `src/cap_protocol/runtime/live_model_streaming.py`, `src/cap_protocol/benchmarks.py`, `tests/test_cap_v1_pep.py`, `tests/test_slow_path_classifier.py`, `tests/test_live_model_streaming.py`, `tests/test_benchmark_harness.py`, `docs/benchmarks/cap_v1_latency_mobile_budget.md`, `src/cap_protocol/conformance/v1_runner.py` | Production model providers, deployed browser/native renderer routing, deployed Local PEP trust modes, organization-selected model-judge rollout, and deployment-representative latency/resource evaluation beyond the local benchmark artifact. |
| V1-C04 | Streaming correction frame | `required_deterministic_scaffold` | Local PEP / Streaming | `src/cap_protocol/runtime/local_pep.py`, `src/cap_protocol/runtime/live_model_streaming.py`, `src/cap_protocol/runtime/ui_abort.py`, `src/cap_protocol/runtime/ui_correction.py`, `tests/test_cap_v1_pep.py`, `tests/test_live_model_streaming.py`, `tests/test_ui_abort_propagation.py`, `tests/test_correction_frame_ux.py`, `src/cap_protocol/conformance/v1_runner.py` | Shipping native Android/iOS wrappers, browser deployment wiring, and deployed audit/provenance sinks. |
| V1-C05 | PrivacyBoundary raw block, local NER redaction, embedding-only egress, local retention GC, and profile generality | `required_deterministic_scaffold` | Local PEP / Privacy PDP / Profiles | `src/cap_protocol/profiles/cap_med.py`, `src/cap_protocol/profiles/cap_swe.py`, `src/cap_protocol/profiles/inheritance.py`, `src/cap_protocol/runtime/privacy_pdp.py`, `src/cap_protocol/runtime/redaction.py`, `src/cap_protocol/runtime/embeddings.py`, `src/cap_protocol/runtime/retention.py`, `src/cap_protocol/runtime/pdp_adapters.py`, `src/cap_protocol/runtime/local_pep.py`, `tests/test_privacy_pdp.py`, `tests/test_local_ner_redaction.py`, `tests/test_embedding_only_egress.py`, `tests/test_retention_ttl_deletion.py`, `tests/test_pdp_adapters.py`, `tests/test_cap_med_v1_profile.py`, `tests/test_cap_swe_profile.py`, `tests/test_lifecycle_profile_inheritance.py`, `tests/test_cap_v1_pep.py`, `src/cap_protocol/conformance/v1_runner.py` | Deployed local and central PDP services, external policy-runtime integration, production local NER and embedding model quality/privacy evaluation, deployed retention scheduling, profile-owner change control, and regulated CAP-Med profile review completion. |
| V1-C06 | Offline fallback | `required_deterministic_scaffold` | Local PEP / Policy Bundle | `src/cap_protocol/runtime/local_pep.py`, `tests/test_cap_v1_pep.py`, `tests/test_policy_registry_service.py`, `src/cap_protocol/conformance/v1_runner.py` | Production Policy Registry deployment, service authentication, HA replication, operational monitoring, and KMS/HSM signing custody. |
| V1-C07 | Expired policy bundle | `required_deterministic_scaffold` | Local PEP / Policy Bundle | `src/cap_protocol/runtime/local_pep.py`, `tests/test_cap_v1_pep.py`, `src/cap_protocol/conformance/v1_runner.py` | KMS/HSM-backed signing operations and distributed policy-bundle revocation. |
| V1-C08 | Replay attack | `required_deterministic_scaffold` | Local PEP / Replay | `src/cap_protocol/runtime/local_pep.py`, `tests/test_replay_idempotency.py`, `src/cap_protocol/conformance/v1_runner.py` | Durable per-session replay or nonce stores shared across executor replicas. |
| V1-C09 | Clock skew | `required_deterministic_scaffold` | Runtime Temporal Validation | `src/cap_protocol/runtime/temporal.py`, `tests/test_temporal_validation.py`, `src/cap_protocol/conformance/v1_runner.py` | Deployment clock synchronization policy, monitoring, and profile skew configuration. |
| V1-C10 | Evidence content changed or expired | `required_deterministic_scaffold` | Evidence Registry | `src/cap_protocol/runtime/registry.py`, `src/cap_protocol/runtime/retention.py`, `tests/test_federated_registry.py`, `tests/test_evidence_registry_service.py`, `tests/test_retention_ttl_deletion.py`, `src/cap_protocol/conformance/v1_runner.py` | Networked Evidence Registry deployment, service authentication, access-policy enforcement, retention-job operations, and production attestation signing. |
| V1-C11 | Sidecar bypass attempt | `required_deterministic_scaffold` | Local PEP / Trust Modes | `src/cap_protocol/runtime/local_pep.py`, `src/cap_protocol/runtime/mobile_local_pep.py`, `src/cap_protocol/runtime/attested_local_pep.py`, `tests/test_cap_v1_pep.py`, `tests/test_mobile_local_pep_proxy.py`, `tests/test_attested_local_pep.py`, `src/cap_protocol/conformance/v1_runner.py` | Native Android/iOS project wiring, real platform attestation verifiers, platform entitlements, device/instrumented bypass tests, and store/notarization review evidence. |
| V1-C12 | Supervisor coercion or overreach | `required_deterministic_scaffold` | Controller / Supervisor Gateway / Session Router / Local PEP | `src/cap_protocol/runtime/controller.py`, `src/cap_protocol/runtime/local_pep.py`, `src/cap_protocol/runtime/session_router.py`, `src/cap_protocol/runtime/supervisor_gateway.py`, `tests/test_cap_v1_pep.py`, `tests/test_controller_service.py`, `tests/test_session_router.py`, `tests/test_supervisor_gateway_service.py`, `src/cap_protocol/conformance/v1_runner.py` | Production Controller, Session Router, and Supervisor Gateway authentication, service discovery, scaling, organization-owned backend integration, HA state, and operational monitoring. |
| V1-C13 | Multi-guard interrupt conflict and human escalation | `required_deterministic_scaffold` | Interrupt Runtime / Human Review / Workflow | `src/cap_protocol/runtime/interrupts.py`, `src/cap_protocol/runtime/human_review.py`, `src/cap_protocol/runtime/workflow_engine.py`, `tests/test_interrupt_runtime.py`, `tests/test_human_review_integration.py`, `tests/test_workflow_engine_composition.py`, `src/cap_protocol/conformance/v1_runner.py` | Durable multi-party Interrupt Manager state, production human-review portal deployment, reviewer authentication, queueing/SLAs, and deployed Temporal/LangGraph integration. |
| V1-C14 | Federated registry stale metadata | `required_deterministic_scaffold` | Federated Registries / Substrate Interop | `src/cap_protocol/runtime/registry.py`, `src/cap_protocol/runtime/authority.py`, `src/cap_protocol/runtime/warrants.py`, `src/cap_protocol/runtime/substrate_interop.py`, `tests/test_federated_registry.py`, `tests/test_capability_registry_service.py`, `tests/test_warrant_primitives.py`, `tests/test_agent_tool_registry_service.py`, `tests/test_policy_hot_update.py`, `tests/test_live_substrate_interop.py`, `src/cap_protocol/conformance/v1_runner.py` | Deployed Capability, Policy, and Evidence registry services with federation, durable cache invalidation, revocation propagation, service authentication, monitoring, external MCP servers, and multi-organization A2A interoperability beyond the local substrate scaffold and Go fixture adapter. |
| V1-C15 | Observability sink independence, lifecycle FSM, signed audit, transparency, W3C PROV store, and OTel attribute coverage | `required_deterministic_scaffold` | Observability Plane | `config/otel/collector-cap.yaml`, `src/cap_protocol/runtime/observability.py`, `src/cap_protocol/runtime/lifecycle.py`, `src/cap_protocol/security/cap_crypto.py`, `src/cap_protocol/security/transparency.py`, `tests/test_observability_plane.py`, `tests/test_transparency_log.py`, `tests/test_lifecycle_profile_inheritance.py`, `src/cap_protocol/conformance/v1_runner.py` | Deployed KMS/HSM custody, external Sigstore/Rekor publication and monitoring, transparency/replication services, deployed collector/exporter operations, production PROV graph/document store operations, production access-control integration, and recovery procedures. |

Profile-specific labels such as revised output, downgraded language, local fallback, or deferred analysis must be tested as compositions of the seven Core interrupt actions. They may appear as fixture names, `reason_code` values, or profile-owned directive labels, but they must not appear as additional `InterruptDecision.action` enum values. Streaming correction frames are linked outcomes of `transform` interruptions and execution reports; they do not add another Core `InterruptDecision.action`.

### 3. Test fixture requirements

A test fixture SHOULD define:

- input messages;
- assumed trust roots;
- policy-engine outputs;
- available evidence store entries;
- expected lifecycle state transitions;
- expected refusal/report/telemetry outputs;
- pass/fail criteria.

For v1, fixtures SHOULD also define Local PEP trust mode, policy-bundle version, clock-skew tolerance, privacy-boundary expression, envelope signature material, simulated supervisor availability, and whether audit persistence is a safety precondition.

The local third-implementation interop fixture suite is `third_impl/go_cap_adapter/testdata/cap_v1_interop.json`. Run it with:

```bash
cd third_impl/go_cap_adapter
go run . --fixtures testdata/cap_v1_interop.json --json
```

It verifies a minimal non-Python CAP v1 consumer shape: required CAPEnvelope fields, RFC 8785/JCS detached Ed25519 envelope and payload signatures, basic payload checks, and traceable fixture IDs for valid, tampered, missing-field, and expired-envelope cases. It is not a replacement for the Python V1-C01 through V1-C15 scaffold gate or for external multi-organization interoperability testing.

The current v1 release gate includes deterministic streaming checks for configurable lookahead buffering, buffered diagnostic transform, semantic slow-path non-regex drift interception, late correction-frame linkage, live local model-stream routing, wall-clock timer release, pull-side backpressure, abort propagation, CLI/WebSocket-style safe replacement on abort, CLI/WebSocket-style safe correction-frame replacement/annotation, Android/iOS native abort and correction contract declaration, and refusal of Supervisor attempts to force unsafe stream output. The v1 target default is the smaller of 250 ms of speech-equivalent text or 50 tokens unless a profile overrides it. It also includes default 30 second clock-skew boundary checks, expired-envelope refusal before payload-ref dereference, expired Directive refusal before executor side effects, Supervisor-overreach checks for raw transcript/audio egress, diagnosis, treatment advice, raw-data non-leakage in refusals, the allowed redacted-context/EvidenceRef path, local NER redaction of Supervisor context, redaction audit records that exclude raw source text, embedding-only Supervisor-context checks that allow local text/voice embeddings and aggregate dimensions while proving raw transcript/audio non-egress and recipient-bound PrivacyBoundary refusal, retention GC checks that delete expired local raw backing content while preserving content-minimized audit records, machine-checkable lifecycle FSM checks for envelope, directive, interrupt, execution, evidence, audit, and provenance traces, CAP-Med v1 runtime-profile checks for signed `CAPEnvelope` hot-path execution, namespaced `profile_constraints.cap-med/v1` and `profile_extensions.cap-med/v1`, unified `Capability` records, Local PEP raw-transcript minimization, and Supervisor Gateway overreach veto, CAP-SWE profile checks for diff evidence, test-result evidence, sandbox evidence, file-write authority, rollback/commit compensation, tool-risk levels, code-owner escalation, and local-only production secrets using the same Core schemas, and profile-inheritance checks for parent/child narrowing, conflict refusal, deterministic multi-profile composition, and Core lifecycle override refusal. The PDP adapter checks verify deterministic parity between OPA-shaped and Cedar-shaped adapter decisions for the scaffold policy fixtures and verify the Cedar principal/action/resource/context mapping. Authority checks cover detached-JWS compatibility plus SPIFFE SVID binding validation, missing/mismatched SVID refusal, Biscuit warrant round-trip, holder binding, scope-expansion refusal, registry-backed warrant-key lookup, and live revocation freshness. Edge PEP checks cover SPIFFE sender/receiver validation when required, deterministic service-mesh sidecar topology for Istio/Linkerd, mesh-owned mTLS/SVID identity consumption without CAP retermination, CAP validation after mesh mTLS, and explicit local fallback. Controller checks cover a service boundary that owns intent formation/orchestration, calls substitutable Guard/PDP evaluators for policy, dispatches through Session Router, runs without an observer sink, supports substitutable plain/signed audit sinks, and declares the combined gRPC `CAPCenter` as v0.1 legacy compatibility. Supervisor Gateway checks cover service-routed consultation, redacted or embedding-only backend context, hidden backend type behind a gateway contract, structured strategy-to-Directive translation, local veto of raw-data and diagnostic Supervisor output, pause InterruptDecision translation, and audit/provenance refs. Session Router checks cover receiver/session binding, independent multi-session routing, cross-session refusal without raw-payload leakage, same-session fanout, and route audit metadata that does not store payload bodies. Workflow composition checks cover a local Temporal-style runner receiving a signed CAPEnvelope, Edge PEP verification before activity execution, Session Router delivery, workflow-history linkage to CAP session/trace IDs, retry-triggered `pause` `InterruptDecision` emission, final `ExecutionReport` emission, and tampered-envelope refusal. Registry and substrate checks cover unified Capability metadata for agent, tool, service, human, and policy subjects; service-backed Agent/Tool discovery with A2A/MCP metadata under `profile_extensions`; live local MCP `tools/call` and `resources/read` through Edge PEP before handler execution; forbidden MCP tool refusal before side effects; CAPEnvelope-wrapped A2A message acceptance; AgentCard CAP extension advertisement; cache miss/fill; cache hit; stale metadata refusal; revoked capability refusal; service-backed live revocation freshness for cached metadata; reference-service persistence, federation hooks, audit events, warrant-key lookup, key rotation, and revoked authority refs; PolicyRef digest drift refusal; EvidenceRef freshness; content-addressed Evidence put/get/verify; expired Evidence backing-content TTL deletion; missing Evidence content refusal; Edge PEP Evidence Registry payload-ref verification; EvidenceRef hash mismatch refusal; and deletion audit records that exclude raw evidence. Policy distribution checks cover service-fetched verified signed bundles, per-session pinning, explicit hot-update refusal until opt-in, audited emergency override, revoked bundle refusal, unreachable Control Plane with valid cached policy, missing policy, expired policy, invalid signature metadata, tampered signed payloads, and Therapist profile-safe supportive output. Observability checks cover durable audit verification despite telemetry delivery failure, independent provenance lineage recording, signed audit verification/tamper detection, external signing-provider hooks, replication retry/backpressure, audit-as-delivery-precondition blocking, local Rekor-compatible transparency bundles for release and AuthorityChainStep DSSE/in-toto attestations, transparency inclusion-proof tamper detection, PROV-JSONLD ingestion, queryable session/evidence/authority/interrupt lineage, evidence-to-execution links, and provenance store failure isolation from telemetry/audit. Sidecar-bypass checks cover direct user-visible output, raw-data egress, local-tool access, network access, deterministic Android/iOS separately privileged proxy smoke checks for route and OS-route bypass attempts, and attested Local PEP registration checks for missing, replayed, mismatched, production-verifier-missing, and valid challenge/response evidence. These are release-blocking scaffold/reference-service conformance checks, not production certification of production model providers, organization-selected model judges, production NER or embedding model quality/privacy, production retention-job operations, shipping native UI wrappers, production Controller/Session Router/Supervisor Gateway rollout, regulated CAP-Med profile safety/clinical review, deployed Temporal/LangGraph workflow integration, production SPIRE/service-mesh rollout, production network registry services, external MCP/A2A multi-organization interoperability, external OPA/Cedar policy-runtime deployment, deployed KMS/HSM custody, external Sigstore/Rekor publication, production observability exporters/collectors, production PROV graph-store deployment, native mobile entitlements, device instrumentation, sandboxing, OS routing, or production hardware-backed attestation verification.

### 4. Profile conformance

A profile MAY add tests, but it MUST NOT weaken Core invariants. Profile-specific refusal codes MUST map to a Core refusal category for generic consumers.

CAP-Med is now represented as a checked-in v1 runtime profile fixture, not only as v0.1 compatibility behavior plus examples. Its profile tests verify that the Therapist persona stays supportive, non-diagnostic, and non-prescriptive; that central Supervisor guidance is structured and privacy-filtered through a Supervisor Gateway; that Local PEP vetoes override unsafe Supervisor directives; and that CAP-Med-owned constraints and metadata stay under `profile_constraints.cap-med/v1` and `profile_extensions.cap-med/v1` while Core objects remain unchanged.

CAP-SWE is the checked-in non-medical reference profile. Its profile tests verify that diff evidence, test-result evidence, sandbox attestation, file-write authority, rollback/commit compensation, tool-risk levels, and human escalation live under `profile_constraints.cap-swe/v1` or `profile_extensions.cap-swe/v1`; that the same Core `PrivacyBoundary`, `OperationalConstraints`, `EvidenceRef`, `Capability`, `Directive`, and `InterruptDecision` schemas validate the fixture; and that production secrets are denied as local-only while minimized diff/test/evidence metadata may cross to a reviewer.

Profile inheritance tests now verify deterministic parent-before-child ordering, safe narrowing of parent constraints, conflict refusal for attempted widening, deterministic sibling composition, CAP-SWE inheritance from the Core profile contract, and refusal of profile attempts to redefine Core lifecycle states or interrupt actions.

Profile-specific semantic-quality evaluation remains outside conformance. For CAP-Med, domain reviewers still need to assess non-diagnostic usefulness, supportive style, escalation appropriateness, and evidence grounding. For CAP-SWE, reviewers still need to assess task correctness, risk awareness, rollback quality, secret handling, and escalation appropriateness. Synthetic fixtures under `examples/domain_semantic_quality/` exercise the harness only and are not expert validation.

### 5. Non-conformance examples

An implementation is not Core-conformant if it:

- executes a Directive after expiry;
- treats natural-language evidence as authority;
- accepts a denied Directive;
- broadens Controller constraints via GuardDecision;
- emits raw hidden chain-of-thought as a DecisionRecord;
- requires one specific transport for semantic conformance;
- ignores evidence hash mismatch;
- silently drops terminal failures from telemetry.


## Source: `docs/testing.md`

## Testing

### Standard Test Run

```bash
source venv/bin/activate
python -m pip install -e ".[dev]"
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

The explicit `NO_PROXY` setting prevents localhost HTTP smoke-test traffic from being routed through system proxy software on machines where that is configured.
This is a local test-environment caveat, not a CAP protocol requirement. Plain `pytest` can fail in proxy-configured environments because the HTTP/JSON smoke test uses localhost URLs and system proxy software such as Privoxy may intercept them.

The pytest suite covers:

- shared conformance fixture pass/fail behavior
- CAP message schema validation
- hardening runner output with a temporary runtime directory
- deterministic HTTP/JSON v1 CAPEnvelope smoke execution
- deterministic gRPC v1 CAPEnvelope smoke execution
- legacy CLI wrapper resolution
- CAP v1 LinkML schema structure and object-model checks
- CAP v1 schema/example validation
- CAP v1 Local PEP, local NER redaction, embedding-only egress, retention TTL deletion, mobile proxy Local PEP, attested Local PEP registration, and Edge PEP smoke behavior
- CAP v1 live model-stream adapter behavior, including wall-clock release, unsafe pre-display transform, semantic slow-path drift interception, backpressure, abort propagation, CLI/WebSocket abort UX, and CLI/WebSocket correction-frame UX
- Android/iOS separately privileged proxy Local PEP scaffold behavior for direct user output, network, raw-data egress, local-tool, and missing OS-route bypass attempts
- attested Local PEP registration behavior for missing, expired, replayed, mismatched, untrusted, debuggable, production-verifier-missing, and valid deterministic test-double attestations
- local NER redaction, embedding-only egress, and retention TTL behavior for names, locations, dates, contact info, medical/financial identifiers, Supervisor Gateway context minimization, evidence-ref preservation, deterministic text/voice vectors, recipient binding, expired local memory deletion, Evidence Registry backing-content deletion, and audit records that exclude raw source text/audio/evidence
- separate v0.1 fixture conformance and v1 release-blocking deterministic scaffold conformance runners
- machine-checkable lifecycle FSM validation for envelope, directive, interrupt, execution, evidence, audit, and provenance traces, plus deterministic profile-inheritance composition and conflict-refusal behavior
- local deterministic benchmark harness execution and artifact generation for latency, streaming delay, CPU-time, memory, and mobile proxy-path measurements
- local Go third-implementation CAPEnvelope/JCS fixture validation and fixture-ID failure traceability

### CAP v1 Conformance Gate

```bash
source venv/bin/activate
cap-check-v1-conformance
```

This runs `V1-C01` through `V1-C15` as required deterministic scaffold cases. It is release-blocking for the current repository package, but it is not full CAP v1 runtime certification; full production/runtime evidence remains tracked in `docs/CAP_RELEASE_GATES.md`.

### Third Implementation Interop Adapter

```bash
cd third_impl/go_cap_adapter
go run . --fixtures testdata/cap_v1_interop.json --json
```

This runs the local standard-library Go adapter against shared CAP v1 CAPEnvelope/JCS/signature fixtures. The default pytest suite also covers it through `tests/test_go_interop_adapter.py` when the Go toolchain is available. This is local third-implementation fixture evidence, not external multi-organization interoperability certification.

### Benchmark Harness

```bash
source venv/bin/activate
python -m cap_protocol.cli.run_benchmarks --iterations 100 --warmup 10
```

This writes the published local artifacts under `docs/benchmarks/`. The reported p50/p95 latency, CPU-time, memory, streaming delay, and mobile proxy-path values are local microbenchmark evidence only; production device telemetry, measured battery drain, native mobile wrappers, model-provider latency, service-mesh latency, and networked registry/PDP latency remain separate release-gate evidence.

### Package Verification

```bash
python VERIFY_RELEASE_BASELINE.py
```

This checks required package files, stale forbidden labels, packaged private key material, and the release-blocking CAP v1 deterministic scaffold conformance gate. Generated runtime folders are ignored.

### Therapist/Supervisor Scenario

```bash
python -m cap_protocol.scenarios.therapist_supervisor.runner --case all
```

The deterministic scenario writes CAPEnvelope traces, Supervisor decisions, tool-call traces, privacy-boundary evaluations, capability evaluations, final responses, an `ExecutionReport`, and a summary under `runs/cap_therapist_supervisor_demo/<timestamp>/`.

### Integration Checks

```bash
python second_http/run_demo.py
python run_production_hardening.py
python run_final_cap.py --target both
```

The gRPC check uses checked-in generated protobuf modules and runtime-generated local mTLS certificates under `runtime_data/certs/` as non-production localhost transport fallback material. CAP v1 workload identity in both demos is the SPIFFE SVID carried by `CAPEnvelope.sender_id`/`receiver_id` and AuthorityChain `identity_binding`; Edge PEP and the authority verifier reject missing or mismatched SPIFFE SVID bindings. The HTTP/JSON check posts v1 `EvidenceRef` and `Directive` envelopes across localhost and receives v1 `ExecutionReport` acknowledgment envelopes. Do not run protobuf generation unless `cap.proto` changes.

### Real-Model Checks

Real-model tests are not run by default. They require optional dependencies, sufficient hardware, and model access:

```bash
export HF_TOKEN=your_huggingface_token
python -m pip install --upgrade torch torchvision accelerate safetensors pillow librosa
python -m pip install --upgrade "git+https://github.com/huggingface/transformers.git"
python run_final_cap.py --target both --use-real-separate-e2b --require-real-model
```

### Live Stream Checks

The default pytest suite includes `tests/test_live_model_streaming.py`, which uses `ScriptedModelStream` as a deterministic pull-based local stream. The runtime also exposes `OllamaModelStream` for callers that have a local or remote Ollama service available; the default tests do not require Ollama.

`tests/test_slow_path_classifier.py` covers the deterministic CAP-Med slow-path classifier, including subtle non-regex diagnostic and treatment drift fixtures, streaming integration, and fail-closed behavior when a configured classifier raises. Optional model-judge checks are not part of default CI.

`tests/test_ui_abort_propagation.py` covers per-platform stream-abort presentation. CLI and WebSocket-style adapters replace the visible stream region with safe text and avoid surfacing raw transport failures; Android and iOS checks verify the native `CapStreamAbort` API contracts because native wrappers are not checked in.

`tests/test_correction_frame_ux.py` covers late correction-frame presentation. CLI and WebSocket-style adapters replace the partial stream region and annotate the correction with safe copy; tests also verify Android/iOS `CapStreamCorrection` contracts, audit/provenance link preservation, and sanitization of unsafe correction text.

`tests/test_local_ner_redaction.py` covers the deterministic local redactor, Local PEP Supervisor-context preparation, Supervisor Gateway backend minimization, and the optional local-model NER adapter. The default suite does not require model downloads or a remote NER service.

`tests/test_embedding_only_egress.py` covers deterministic local text/voice embedding vectors, Local PEP embedding-only Supervisor projection, raw transcript/audio non-egress, Supervisor Gateway backend minimization, and recipient-bound privacy refusals. The default suite does not require model downloads or remote embedding services.

`tests/test_retention_ttl_deletion.py` covers `PrivacyBoundary.retention` TTL deletion for Local PEP raw backing storage and Evidence Registry backing blobs. It verifies that expired content is deleted, evidence resolvers refuse expired backing content, deletion audit/provenance records are preserved, and raw evidence does not leak into audit records.

`tests/test_cap_med_v1_profile.py` covers the CAP-Med v1 runtime-profile fixture. It validates the fixture against existing Core schemas, checks that CAP-Med constraints and metadata are namespaced under `cap-med/v1`, verifies unified `Capability` records and `InterruptDecision` mappings, and runs the signed hot-path smoke through Edge PEP, Local PEP, and Supervisor Gateway overreach refusal.


## Source: `docs/CAP_RELEASE_GATES.md`

## CAP Release Gates

This document separates four release states that must not be collapsed:

1. **v0.1 production-candidate package:** current executable package status.
2. **v1 documented architecture:** current documentation/specification status for the Control Authority Protocol target.
3. **v1 implemented runtime:** not yet reached; requires runtime adoption of the v1 architecture and conformance gates below.
4. **stable public standard or production deployment certification:** not yet reached; requires external review, production infrastructure, interoperability, and domain evaluation.

The CAP v1 source phrase "implementation-ready architecture baseline" is a specification-readiness claim. It is not a claim that this repository already implements the full CAP v1 runtime.

### Initial Public Baseline Release Checklist

| Gate | Required evidence |
|---|---|
| schema drift checks | `python scripts/check_v1_schema_drift.py` passes |
| LinkML to JSON Schema checks | `tests/test_cap_v1_linkml.py` and schema drift checks pass |
| CAPEnvelope hot-path checks | gRPC/HTTP v1 CAPEnvelope tests and V1-C01 checks pass |
| V1-C01..V1-C15 conformance checks | `cap-check-v1-conformance` passes all release-blocking deterministic scaffold cases |
| signature/JCS checks | JCS/DetachedJWS tests and signed CAP object examples validate |
| SPIFFE/SVID checks where applicable | workload identity tests and V1-C01 identity checks pass |
| Biscuit warrant checks | warrant primitive tests and registry-backed revocation freshness checks pass |
| registry freshness/revocation checks | capability, policy, evidence, and warrant registry tests pass |
| privacy redaction/embedding/retention/profile checks | local NER redaction, embedding-only egress, recipient binding, retention TTL deletion, CAP-Med v1 runtime-profile checks, CAP-SWE profile generality, and Supervisor-context minimization tests pass without raw source text/audio/evidence in audit or backend payloads |
| latency/mobile resource benchmark artifacts | `python -m cap_protocol.cli.run_benchmarks --iterations 100 --warmup 10` publishes local p50/p95, CPU, memory, streaming-delay, and mobile proxy-path artifacts under `docs/benchmarks/` |
| third implementation interop fixture | `(cd third_impl/go_cap_adapter && go run . --fixtures testdata/cap_v1_interop.json --json)` passes and reports results by fixture ID |
| documentation link checks | `python scripts/check_doc_links.py` passes for release-facing docs |
| example scenario smoke tests | `python -m cap_protocol.scenarios.therapist_supervisor.runner --case all` passes |
| non-overclaiming claim audit | `python scripts/check_claim_language.py` passes |

The one-command baseline verifier is `python VERIFY_RELEASE_BASELINE.py`. It fails if required docs are missing, schema drift is detected, V1-C01..V1-C15 conformance fails, the Therapist/Supervisor scenario fails, release-facing links are broken, claim audit fails, or required checklist terms are absent.

### Current Release Labels

| Label | Current status | Allowed claim |
|---|---|---|
| `v0.1-production-candidate` | Appropriate now | The current package demonstrates the v0.1 Control Authority Profile subset across two local executable bindings with conformance and hardening checks. |
| `v1-architecture-documented` | Appropriate now | CAP v1 target architecture, object model, diagrams, examples, and release gates are documented, with partial schema/runtime scaffolding. |
| `v1-runtime-scaffold` | Appropriate with caveats | Initial v1 schemas, examples, migrated gRPC and HTTP/JSON `CAPEnvelope` hot paths, a local Go third-implementation interop adapter, Controller service, Local PEP/Edge PEP, local NER redaction, embedding-only Supervisor egress, retention TTL deletion, CAP-Med v1 runtime profile fixture, CAP-SWE non-medical reference profile, local latency/mobile-resource benchmark artifacts, Supervisor Gateway, service-mesh, live MCP/A2A substrate interop, workflow-engine, and transparency-log composition, federated registry, and observability sink scaffolds, deterministic smoke checks, and selected adversarial fixtures exist. |
| `v1-implemented-runtime` | Not appropriate yet | Do not use until the v1 runtime gates in this document pass. |
| `v0.1-stable` | Not appropriate yet | Do not use until external stable-release gates pass for the v0.1 package. |
| `v1-stable` | Not appropriate yet | Do not use until both v1 implemented-runtime gates and external stable-release gates pass. |

### v0.1 Production-Candidate Gates

These gates are complete for the current package. They support the `v0.1-production-candidate` label, not a stable public standard and not a full CAP v1 runtime.

| Gate | Status |
|---|---|
| Core CAP v0.1 primitives implemented | Complete |
| gRPC/protobuf reference binding | Complete |
| HTTP/JSON independent binding | Complete |
| Shared conformance smoke suite | Complete |
| Independent fixture-based conformance package | Complete |
| MCP constrained invocation demo | Complete locally; live local `tools/call` and `resources/read` now route through Edge PEP |
| A2A metadata carriage demo | Complete locally; live local message delivery now carries CAPEnvelope and AgentCard CAP extension |
| OPA/Cedar-shaped policy adapters / policy-as-data backend | Complete locally |
| OpenTelemetry semantic attributes | Complete locally |
| W3C PROV mapping | Complete locally |
| v0.1 JSON Schema artifacts | Complete |
| Adversarial fixtures | Complete |
| SPIFFE/SVID workload identity scaffold | Complete locally |
| Runtime-generated local mTLS fallback certs | Complete locally, non-production fallback only |
| No packaged private cert keys | Complete, verified by package scan |
| Ed25519 detached-JWS verification | Complete |
| DSSE signed envelopes | Complete |
| in-toto-style attestation statements | Complete |
| Hash-chain append-only audit store | Complete |
| One-command runner | Complete |

### v1 Documented-Architecture Gates

These gates support the claim that CAP v1 architecture is documented and partially scaffolded. They do not support a claim that CAP v1 is implemented end to end.

| Gate | Status | Evidence |
|---|---|---|
| Reframed public docs from Control Authority Profile subset to Control Authority Protocol target | Complete | `README.md`, `docs/CAP_00_README.md`, `docs/architecture.md`, `docs/CAP_01_foundations.md`. |
| Hybrid two-tier, three-plane architecture documented | Complete | `docs/architecture.md`, `docs/CAP_02_core_model.md`, `docs/CAP_05_integrations.md`. |
| Current-vs-target implementation status documented | Complete | `docs/CAP_IMPLEMENTATION_ALIGNMENT.md`, `docs/CAP_v1_TASKS.md`. |
| Architecture diagrams added | Complete | `docs/architecture.md`. |
| Therapist/Supervisor sequence examples added | Complete | `docs/CAP_examples.md`. |
| Schema appendix migrated | Complete | `docs/CAP_appendix_schemas.md`. |
| v1 release gates separated from v0.1 gates | Complete | This document. |
| CAP v1 object names documented | Complete | `docs/CAP_03_primitives.md`, `schemas/cap.yaml`, `schemas/domains/*.yaml`, `schemas/cap-core/v1/*.schema.json`. |
| Conservative claim language preserved | Complete | `docs/CAP_CLAIMS.md`, `docs/CAP_FINAL_STATUS.md`, `docs/CAP_IMPLEMENTATION_ALIGNMENT.md`. |

### v1 Implemented-Runtime Gates

CAP v1 MUST NOT be called an implemented runtime until these gates pass in CI or equivalent release verification. Partial deterministic scaffolding is useful, but it is not a production runtime gate.

| Gate | Current status | Required before `v1-implemented-runtime` |
|---|---|---|
| LinkML/JSON Schema drift gate | Partial, currently passing for essential fields | Keep `cap-check-v1-schema-drift`, `tests/test_cap_v1_linkml.py`, and `tests/test_cap_v1_schemas.py` green; decide whether generated JSON Schema replaces reviewed artifacts or remains a checked-in validation surface. |
| Main runtime uses `CAPEnvelope` and v1 schemas | Partial | gRPC and HTTP/JSON hot paths now emit and validate v1 `CAPEnvelope` objects with signed v1 payloads, shared deterministic temporal validation, demo Edge PEP checks on cross-boundary envelope paths, explicit applied `InterruptDecision` refs in execution reports, and release-blocking deterministic scaffold coverage for V1-C01 through V1-C15. Production PEP/registry dereference semantics remain open. |
| Reusable Local PEP integrated into runtime path | Partial: gRPC and HTTP/JSON demos route selected user-visible output, local memory/raw-observation handling, and MCP-style local-tool calls through the reusable Local PEP scaffold, with direct output/tool bypass checks failing closed, structured PrivacyBoundary PDP refusals citing failing dimensions, local NER redaction before Supervisor context egress, embedding-only Supervisor egress with recipient binding, and retention TTL deletion for expired local raw backing content. | Broaden this into production deployment wiring; keep privacy vetoes, typed refusals, audit refs, redaction refs, embedding provenance refs, retention deletion refs, and provenance refs intact across live model streams, real local-tool clients, and Supervisor consultation paths. |
| Local PEP production trust mode | Partial: deterministic proxy and attested-registration scaffolds | `mobile_local_pep` declares Android `CapLocalPepProxyService` and iOS `CapLocalPepProxyExtension` contracts, manifest-shaped route controls, and smoke checks for direct user output, network, raw-data egress, local-tool, and missing OS-route bypass attempts. `attested_local_pep` adds challenge/response registration, trusted provider contracts, detached-JWS test-double verification, production verifier hooks, workload identity and Local PEP version binding, replay detection, and Capability Registry publication only after attestation. Native mobile project wiring, real platform attestation verifiers, platform entitlements, device/instrumented tests, and review evidence remain required before `v1-implemented-runtime`. |
| Edge PEP integrated at network/message boundary | Partial: gRPC and HTTP/JSON demo cross-boundary `CAPEnvelope` paths route through Edge PEP signature, shared timestamp/TTL/skew checks with default 30 second boundary coverage, SPIFFE sender/receiver SVID validation, structured privacy-boundary PDP checks, PolicyRef, detached-JWS/Biscuit AuthorityChain checks, payload-ref refusal checks before payload use, and deterministic Istio/Linkerd-style service-mesh composition tests where the mesh owns mTLS and CAP consumes the expected SPIFFE identity. | Broaden beyond in-process demo helpers into production service-mesh or sidecar routing with an external Istio/Linkerd/SPIRE smoke test, registry-backed key/policy/privacy/evidence resolution, revocation freshness, PDP/Policy Registry integration, and release-blocking bypass tests. |
| Controller service boundary | Partial: CAP-facing reference service implemented; production deployment open | `ControllerService`, `LocalControllerClient`, `HTTPControllerClient`, `PDPGuardEvaluator`, and `ScriptedGuardEvaluator` now demonstrate Controller-owned intent formation/orchestration while delegating policy evaluation to Guard/PDP interfaces, routing to `SessionRouter`, and audit/telemetry/provenance to `ObservabilityPlane` sinks. Before `v1-implemented-runtime`, this still needs production service authentication, discovery, HA orchestration state, durable intent state, production Guard/PDP clients, deployed router/observer wiring, and operational monitoring. |
| Supervisor Gateway | Partial: CAP-facing reference service implemented; production deployment open | `SupervisorGatewayService`, `HTTPSupervisorGatewayClient`, and backend adapters for model, human-portal, and rule-engine paths now route consultations through a gateway service contract with redaction or embedding-only context, authority checks, Local PEP policy/privacy/safety vetoes, audit refs, and provenance refs. Before `v1-implemented-runtime`, this still needs production service authentication, discovery, scaling, operational monitoring, production authority/key management, and organization-owned backend integration. |
| Session Router | Partial: reference router implemented; production deployment open | `SessionRouter` tracks active participants per `session_id`, enforces sender/receiver membership before delivery, supports same-session fanout, refuses cross-session receiver attempts, and emits audit/provenance routing metadata without storing raw payload bodies. Before `v1-implemented-runtime`, this still needs production service deployment, service authentication, HA state management, integration with live Control Plane routing, and operational monitoring. |
| Human Review integration | Partial: reference integration implemented; production portal/workflow deployment open | `HumanReviewService` turns `escalate` interrupts into privacy-minimized review tasks, optionally routes them through `SessionRouter`, accepts structured approve/deny/transform/pause decisions from `ScriptedHumanReviewPortal`, blocks raw transcript/audio requests unless privacy policy permits them, and emits audit/provenance refs plus linked `ExecutionReport` objects. Before `v1-implemented-runtime`, this still needs reviewer authentication, production portal/queue deployment, workflow-engine integration, SLA handling, operational monitoring, and organization-owned review policy. |
| Workflow engine composition | Partial: local Temporal-style sample implemented; deployed workflow integration open | `TemporalCAPWorkflowSample` receives a signed `Directive` CAPEnvelope, verifies it through Edge PEP, routes it through `SessionRouter`, records Temporal-style workflow history with `session_id` and `trace_id`, emits a retry-triggered `pause` `InterruptDecision`, and emits a final `ExecutionReport`. Before `v1-implemented-runtime`, this still needs a deployed Temporal or LangGraph worker, durable external queue/state integration, workflow SLA handling, production human-review workflow wiring, operational monitoring, and organization-owned retry/compensation policy. |
| Logical Interrupt Manager | Partial deterministic scaffold: the seven primitives, restrictive composition order, CAP-Med profile-behavior mapping, Local PEP stream interrupts, Supervisor Gateway interrupt output, Human Review escalation handling, and gRPC/HTTP execution-report refs are covered in-process. | Deploy a logical Interrupt Manager across Local PEP, Edge PEP, Supervisor Gateway, production Human Review, and live streams with durable state, cross-service conflict coordination, and release-blocking tests. |
| Live streaming lookahead buffer | Reference live local stream, CLI/WebSocket abort/correction UX, and local benchmark artifact complete; production rollout open | `LiveModelStreamSession` routes local scripted chunks, and optional Ollama chunks when a caller supplies a running service, through profile-configured Local PEP buffering with 250 ms/50 token defaults, fast regex checks, deterministic semantic slow-path classification, pre-display transforms, wall-clock release, pull-side backpressure, abort propagation, CLI/WebSocket-style safe replacement events, CLI/WebSocket-style correction-frame replacement/annotation events, Android/iOS native abort and correction contracts, linked audit/provenance/report refs, and a local p50/p95 benchmark artifact in `docs/benchmarks/cap_v1_latency_mobile_budget.md`. Production model providers, shipping native UI wrappers, organization-selected model-judge rollout, native device/mobile telemetry, measured battery drain, networked registry/PDP latency, and deployed Local PEP trust modes remain required before `v1-implemented-runtime`. |
| Offline signed policy bundle cache | Reference service implemented; production deployment open | A SQLite-backed reference Policy Registry can distribute verified signed bundles, pin versions per session, rotate to a new bundle only through explicit hot-update opt-in, reject revoked/stale/mismatched bundles, and apply audited emergency override bundles without bypassing signature/expiry checks. Offline Local PEP fallback still validates the cached signed bundle and fails closed for unsafe turns. Production deployment still needs network service packaging, service authentication, HA replication, operational monitoring, KMS/HSM signing custody, and organization rollout controls. |
| Local and central PDP separation | Partial: structured PrivacyBoundary PDP evaluation now exists as an in-process helper used by Local PEP, Edge PEP, and v1 adapter paths; OPA-shaped and Cedar-shaped PDP adapters share one CAP request/decision interface with deterministic scaffold parity checks; and Policy Registry reference services can detect policy digest drift and distribute signed bundles. | Separate hot-path local PDP behavior from central PDP/adapters and production Policy Registry deployment; wire organization-owned OPA/Cedar runtimes and policies; preserve session policy pinning and explicit hot-update behavior. |
| Non-medical profile generality | Partial deterministic evidence: `cap_protocol.profiles.cap_swe` defines a CAP-SWE reference fixture using the same Core schemas with profile-owned diff evidence, sandbox constraints, test-result evidence, file-write authority, rollback/commit compensation, tool-risk levels, human escalation, and production-secret local-only privacy checks. | Add external/third-party profile owners, production SWE-agent sandboxing, real CI and repository integrations, and cross-implementation profile conformance before claiming broad ecosystem generality. |
| CAP-Med v1 runtime profile | Partial deterministic evidence: `cap_protocol.profiles.cap_med` defines a CAP-Med v1 runtime profile fixture using the same Core schemas with profile-owned non-diagnostic, non-prescriptive, raw-transcript/audio minimization, Supervisor context, Local PEP veto, and Supervisor-overreach constraints under `profile_constraints.cap-med/v1` and `profile_extensions.cap-med/v1`; tests and V1-C05 conformance verify signed `CAPEnvelope` hot-path execution, unified `Capability` records, `InterruptDecision` mappings, raw-transcript minimization, and Supervisor Gateway overreach refusal. | This is structural runtime-profile evidence, not regulated-profile approval, clinical validation, production Supervisor Gateway rollout, production model/backend integration, or domain semantic-quality evidence. |
| Local NER redaction before egress | Partial deterministic scaffold: `cap_protocol.runtime.redaction` and `LocalPEP.prepare_supervisor_context(...)` replace sensitive spans with category tags, preserve EvidenceRefs and structural refs, require local-only processing, and audit redaction hashes/categories without raw source text. | Choose and validate production local NER models, publish redaction-quality evaluation fixtures, wire deployed audit/provenance sinks, and ensure native/device Local PEP trust modes prevent bypass before claiming production privacy enforcement. |
| Embedding-only Supervisor egress | Partial deterministic scaffold: `cap_protocol.runtime.embeddings` and `LocalPEP.prepare_supervisor_context(...)` encode text and voice sources locally, forward only embeddings, aggregate dimensions, safety flags, evidence refs, recipient-binding metadata, hashes, and provenance refs, and refuse recipients outside the active PrivacyBoundary. | Choose and validate production local embedding models, publish embedding privacy/quality evaluation fixtures, wire deployed audit/provenance sinks, and ensure native/device Local PEP trust modes prevent bypass before claiming production privacy enforcement. |
| Retention TTL deletion | Partial deterministic scaffold: `cap_protocol.runtime.retention`, `LocalPEP.collect_retention_garbage(...)`, and `ReferenceCapabilityRegistryService.collect_retention_garbage(...)` map `PrivacyBoundary.retention` to local raw backing-content TTLs, delete expired backing content, refuse expired Evidence backing content, and preserve content-minimized deletion audit/provenance records. | Deploy durable local stores, scheduled retention jobs, legal/organizational retention policy mapping, production access control, and production audit/provenance sinks before claiming production retention enforcement. |
| Federated registries and substrate interop | Reference service and deterministic live substrate paths implemented; production deployment open | A SQLite-backed reference service now persists Capability/Policy/Evidence registry records, content-addressed Evidence blobs with expiry metadata, live revocation state, audit events, trust-domain federation hooks, and warrant-key directory entries. Agent/Tool discovery resolves A2A/MCP metadata from service-backed Capability records, Evidence dereference re-hashes stored content before Edge PEP payload use, expired Evidence backing content can be TTL-deleted without deleting audit records, Biscuit warrant verification can require live registry-backed revocation freshness, and the local live substrate scaffold routes MCP `tools/call`, MCP `resources/read`, and A2A message delivery through CAPEnvelope/Edge PEP checks before handlers run. Production deployment still needs network service packaging, service authentication, HA replication, access-policy enforcement, retention-job operations, operational monitoring, organization-specific rollout controls, external MCP servers, and multi-organization A2A interoperability beyond the local Go fixture adapter. |
| CAP Warrant / authority-chain production primitive | Biscuit reference integration complete; production operations open | AuthorityChain verification supports `biscuit-v2` warrant tokens for CAP AuthorityChainStep claims, plus detached-JWS compatibility. Tests cover Biscuit step round-trip, SPIFFE SVID holder binding against runtime identity, missing/mismatched SVID refusal, scope attenuation/refusal of expansion, policy-ref shape, registry-backed warrant-key lookup, key rotation, revoked authority refs, and live revocation freshness. Production claims still require SPIRE/service-mesh rollout, KMS/HSM signing custody, operational key ceremonies, deployed revocation services, and external interoperability evidence beyond the local Go fixture adapter. |
| Independent observability-plane split | Deterministic scaffold complete; production deployment open | Keep audit, telemetry, and provenance as distinct sink interfaces with distinct integrity, retention, and loss assumptions. The runtime now includes signed audit-operation scaffolding with external signing-provider hooks, retention/access metadata, replication retry/backpressure behavior, audit-as-delivery-precondition gating, local Sigstore/Rekor-style transparency bundles for release and AuthorityChainStep attestations, and a local PROV-JSONLD `JsonlProvStore` with session, evidence, authority, and interrupt lineage queries. A reference OpenTelemetry collector config and deterministic `cap.*` attribute coverage checks cover envelope receipt, PEP decision, interrupt, execution, evidence, audit, and refusal lifecycle events. Complete deployed KMS/HSM custody, external Rekor publication/monitoring, transparency/replication services, OpenTelemetry collector/exporter operations, production W3C PROV store deployment, access-control integration, and recovery before claiming `v1-implemented-runtime`. |
| v1 conformance backlog | Release-blocking deterministic scaffold/reference-service gate complete for V1-C01 through V1-C15 | Keep `cap-check-v1-conformance`, `run_v1_conformance_release_gate`, `tests/test_conformance.py`, and `python VERIFY_RELEASE_BASELINE.py` green. Full runtime certification still needs production network registry deployment, deployed gateways, trust modes, live streams, production observability, and external-gate evidence. |
| Interoperability across three v1 implementation shapes | Partial local evidence | The local gRPC and HTTP/JSON demos are independent runtime shapes that emit v1 `CAPEnvelope` objects, route demo cross-boundary envelopes through Edge PEP, and pass binding-specific checks. The local live substrate scaffold also exercises MCP and A2A data-plane paths through CAP enforcement. The Go adapter under `third_impl/go_cap_adapter` independently validates shared CAPEnvelope/JCS/signature/payload fixtures and reports failures by fixture ID. External multi-organization or third-party interoperability remains required. |

### External Gates Before Stable Public Release

These gates apply before claiming `v0.1-stable`, `v1-stable`, production deployment certification, or externally audited standard status.

| Gate | Required evidence |
|---|---|
| Independent third-party security review | Review by qualified external security reviewers, with no unresolved critical findings in authority, signing, privacy, PEP bypass, policy update, evidence, or audit behavior. The reviewer starting packet is prepared at [`docs/security_review/README.md`](../security_review/README.md), with a findings tracker template at [`docs/security_review/findings_tracker_template.md`](../security_review/findings_tracker_template.md); this preparation does not close the gate. |
| Production KMS/HSM integration | Deployment-specific key lifecycle, signing-key protection, rotation, revocation, incident response, and auditability. The operations plan is prepared at [`docs/kms_hsm/README.md`](../kms_hsm/README.md), with a non-secret placeholder at [`config/kms_hsm.example.yaml`](../../config/kms_hsm.example.yaml); deployment-owned KMS/HSM evidence is still required before this gate closes. |
| Organization-specific OPA/Cedar deployment | Real policy ownership, change control, rollout, rollback, hot-update, and exception handling. The deployment guide is prepared at [`docs/policy_deployment/README.md`](../policy_deployment/README.md), with a non-production sample layout under [`policies/organization_template/`](../../policies/organization_template/); organization-owned policy runtime and promotion evidence is still required before this gate closes. |
| Live multi-organization MCP/A2A interoperability tests | Cross-organization or external-stack interoperability, not only local fixtures. The partner run plan, non-secret config placeholder, and report template are prepared at [`docs/mcp_a2a_interop/README.md`](../mcp_a2a_interop/README.md), [`config/mcp_a2a_interop.example.yaml`](../../config/mcp_a2a_interop.example.yaml), and [`docs/mcp_a2a_interop/report_template.md`](../mcp_a2a_interop/report_template.md); external partner evidence is still required before this gate closes. |
| Production observability and audit operations | Retention, integrity, access control, external Rekor publication/monitoring, backpressure, and recovery procedures for signed audit, transparency, telemetry, and provenance sinks. |
| Domain semantic-quality evaluation | Task-specific datasets, reviewer criteria, and measured output quality separate from CAP structural conformance. The harness, reviewer rubric, synthetic onboarding fixtures, and non-secret config placeholder are prepared at [`docs/domain_semantic_quality/README.md`](../domain_semantic_quality/README.md), [`docs/domain_semantic_quality/reviewer_rubric.md`](../domain_semantic_quality/reviewer_rubric.md), [`examples/domain_semantic_quality/`](../../examples/domain_semantic_quality/), and [`config/domain_semantic_quality.example.yaml`](../../config/domain_semantic_quality.example.yaml); qualified external expert evidence is still required before this gate closes. |
| CAP-Med or other regulated-profile review | Domain expert review of profile constraints, escalation paths, privacy controls, non-diagnostic boundaries, and user-facing behavior where applicable. The review packet, checklist, open questions, report template, and non-secret config placeholder are prepared at [`docs/regulated_profile_review/README.md`](../regulated_profile_review/README.md), [`docs/regulated_profile_review/reviewer_checklist.md`](../regulated_profile_review/reviewer_checklist.md), [`docs/regulated_profile_review/open_questions.md`](../regulated_profile_review/open_questions.md), [`docs/regulated_profile_review/report_template.md`](../regulated_profile_review/report_template.md), and [`config/regulated_profile_review.example.yaml`](../../config/regulated_profile_review.example.yaml); qualified external profile review remains required before this gate closes. |
| Performance, latency, and mobile/edge budget evaluation | Local deterministic benchmark artifacts exist under `docs/benchmarks/`, but stable release still needs deployment-representative Local PEP latency, streaming buffer overhead, native mobile/device battery/CPU/memory telemetry, networked registry/PDP latency, service-mesh latency, and Control Plane outage behavior. |

### Research-Strengthening Gates

These gates are not required to preserve the current conservative release claim, but they strengthen a systems or applied-AI paper.

| Gate | Status | Why it matters |
|---|---|---|
| Latency and overhead benchmark | Partial local evidence | `docs/benchmarks/cap_v1_latency_mobile_budget.md` quantifies local deterministic CAP overhead versus direct MCP/tool, Local PEP output, streaming, Edge PEP, and mobile proxy scaffold paths; production/device benchmarking remains open. |
| Non-medical profile example | Partial deterministic evidence | CAP-SWE now demonstrates that CAP v1 profile rules can be software-engineering-specific while reusing Core objects unchanged; external profile ownership and production SWE integrations remain future work. |
| Third minimal implementation or external adapter | Partial local evidence | `third_impl/go_cap_adapter` is a standard-library Go adapter that independently validates shared CAP v1 CAPEnvelope/JCS/signature/payload fixtures and is exercised by `tests/test_go_interop_adapter.py`; external adapter ownership and multi-organization interop remain open. |
| Formal lifecycle FSM and profile inheritance rules | Partial deterministic evidence | `cap_protocol.runtime.lifecycle` defines machine-checkable lifecycle FSMs for envelope, directive, interrupt, execution, evidence, audit, and provenance; `cap_protocol.profiles.inheritance` defines deterministic monotonic profile composition and Core override refusal. Production profile-owner governance and external conformance remain open. |
| Synthetic CAP-Med semantic-quality evaluation dataset | Partial local evidence | `examples/domain_semantic_quality/cap_med_synthetic_cases.jsonl`, `docs/domain_semantic_quality/README.md`, and `tests/test_semantic_quality_evaluation.py` provide synthetic onboarding inputs and harness smoke coverage. Qualified expert review and governed non-synthetic datasets remain open. |
| Regulated-profile review packet | Prepared external-gate packet | `docs/regulated_profile_review/README.md`, `docs/regulated_profile_review/reviewer_checklist.md`, `docs/regulated_profile_review/open_questions.md`, `docs/regulated_profile_review/report_template.md`, and `config/regulated_profile_review.example.yaml` give reviewers a starting packet for CAP-Med profile constraints, forbidden behaviors, escalation paths, privacy controls, refusal/correction behavior, evidence examples, test results, and known limitations. External profile review remains open. |
| Broader empirical semantic-quality evaluation | Missing | Distinguishes structural safety/provenance behavior from model output quality or domain utility. |

### Allowed Summary Claim

> CAP v1 architecture is documented and partially scaffolded as the Control Authority Protocol. This repository currently provides a v0.1 production-candidate Control Authority Profile subset with two executable local bindings, migrated gRPC and HTTP/JSON CAPEnvelope hot paths, a local Go third-implementation interop adapter, a decomposed Controller reference service, SPIFFE SVID identity-binding checks, deterministic service-mesh, live MCP/A2A substrate, workflow-engine, and transparency-log composition scaffolding, shared conformance fixtures, production-hardening checks, signed authority artifacts, v1 schema and PEP scaffolding including local NER redaction, embedding-only Supervisor egress, retention TTL deletion, machine-checkable lifecycle/profile-inheritance rules, CAP-SWE non-medical profile evidence, local latency/mobile-resource benchmark artifacts, and a release-blocking deterministic scaffold conformance gate for V1-C01 through V1-C15. It is not a complete CAP v1 runtime, not a stable public standard, and not production deployment certification.
