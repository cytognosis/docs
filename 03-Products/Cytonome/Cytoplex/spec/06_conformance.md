> **Status**: Active
> **Date**: 2026-06-14
> **Author**: @mohammadi
> **Audience**: engineers
> **Tags**: `cap`, `cytoplex`, `spec`

# CAP_06 — Conformance

CAP conformance validates semantic behavior. An implementation may pass using any transport or framework.

The checked-in fixture suite is the current v0.1 production-candidate conformance baseline. CAP v1 extends the target conformance scope to Local PEP, Edge PEP, privacy-boundary, interrupt, offline, lifecycle FSM, profile inheritance, and adversarial failure-mode behavior. The repository now includes a `cap-v1-release-blocking-scaffold` gate that maps V1-C01 through V1-C15 to executable deterministic scaffold checks. It also includes a local Go third-implementation fixture adapter under `third_impl/go_cap_adapter` for shared CAPEnvelope/JCS/signature fixture validation. These gates are release-blocking or traceability evidence for this repository's current v1 scaffold; they are not full CAP v1 runtime certification.

Domain semantic-quality evaluation is deliberately separate from these conformance gates. The harness in `cap_protocol.evaluation.semantic_quality` and the runbook in `docs/domain_semantic_quality/README.md` score profile/domain output quality, reviewer criteria, and blocking domain flags; they do not validate CAPEnvelope, PEP, registry, authority, or observability mechanics.

## 1. Conformance levels

| Level | Meaning |
|---|---|
| Core Producer | Can emit schema-valid CAP Core messages. |
| Core Consumer | Can validate and process CAP Core messages and enforce lifecycle invariants. |
| Core Executor | Can accept/refuse Directives, enforce constraints, and emit ExecutionReports. |
| Core Guard | Can emit GuardDecision objects from policy inputs. |
| Core Observer | Can emit required OpenTelemetry attributes and/or PROV mappings. |
| Profile Conformant | Implements Core plus one named profile's extra rules. |

A complete CAP Core implementation SHOULD include Executor, Guard, and Observer behavior.

## 2. Required semantic tests

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

## 2.1 CAP v1 release-blocking scaffold cases

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

## 3. Test fixture requirements

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

## 4. Profile conformance

A profile MAY add tests, but it MUST NOT weaken Core invariants. Profile-specific refusal codes MUST map to a Core refusal category for generic consumers.

CAP-Med is now represented as a checked-in v1 runtime profile fixture, not only as v0.1 compatibility behavior plus examples. Its profile tests verify that the Therapist persona stays supportive, non-diagnostic, and non-prescriptive; that central Supervisor guidance is structured and privacy-filtered through a Supervisor Gateway; that Local PEP vetoes override unsafe Supervisor directives; and that CAP-Med-owned constraints and metadata stay under `profile_constraints.cap-med/v1` and `profile_extensions.cap-med/v1` while Core objects remain unchanged.

CAP-SWE is the checked-in non-medical reference profile. Its profile tests verify that diff evidence, test-result evidence, sandbox attestation, file-write authority, rollback/commit compensation, tool-risk levels, and human escalation live under `profile_constraints.cap-swe/v1` or `profile_extensions.cap-swe/v1`; that the same Core `PrivacyBoundary`, `OperationalConstraints`, `EvidenceRef`, `Capability`, `Directive`, and `InterruptDecision` schemas validate the fixture; and that production secrets are denied as local-only while minimized diff/test/evidence metadata may cross to a reviewer.

Profile inheritance tests now verify deterministic parent-before-child ordering, safe narrowing of parent constraints, conflict refusal for attempted widening, deterministic sibling composition, CAP-SWE inheritance from the Core profile contract, and refusal of profile attempts to redefine Core lifecycle states or interrupt actions.

Profile-specific semantic-quality evaluation remains outside conformance. For CAP-Med, domain reviewers still need to assess non-diagnostic usefulness, supportive style, escalation appropriateness, and evidence grounding. For CAP-SWE, reviewers still need to assess task correctness, risk awareness, rollback quality, secret handling, and escalation appropriateness. Synthetic fixtures under `examples/domain_semantic_quality/` exercise the harness only and are not expert validation.

## 5. Non-conformance examples

An implementation is not Core-conformant if it:

- executes a Directive after expiry;
- treats natural-language evidence as authority;
- accepts a denied Directive;
- broadens Controller constraints via GuardDecision;
- emits raw hidden chain-of-thought as a DecisionRecord;
- requires one specific transport for semantic conformance;
- ignores evidence hash mismatch;
- silently drops terminal failures from telemetry.
