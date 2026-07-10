# Independent Security Review Packet

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: engineers
> **Tags**: `engineering`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

This packet prepares CAP for independent third-party security review. It is a reviewer starting point, not evidence that the review has happened.

The external review gate remains open until qualified external reviewers complete the review and any critical findings in authority, signing, privacy, PEP bypass, policy update, evidence, or audit behavior are resolved. The supported status labels remain those listed in [CAP_RELEASE_GATES.md](../CAP_RELEASE_GATES.md).

## Review Objective

Review whether the current repository evidence supports the conservative claims in [CAP_CLAIMS.md](../CAP_CLAIMS.md), and identify security issues that would block any future stable-release or production-deployment claim.

The review should focus on the current executable and documented surfaces:

- v0.1 production-candidate compatibility evidence.
- CAP v1 architecture documentation and deterministic runtime scaffold evidence.
- v1 CAPEnvelope hot paths in the gRPC and HTTP/JSON reference bindings.
- Local PEP, Edge PEP, PrivacyBoundary, authority-chain, evidence, policy, audit, registry, and observability scaffolds.
- The stated gaps that still require deployment-specific or external evidence.

Out of scope for this packet: claiming CAP v1 as a complete runtime, stable public standard, production deployment certification, clinical validation, or completed external audit.

## Reviewer Starting Map

| Area | Primary docs | Evidence to inspect |
|---|---|---|
| Release status and gate language | [CAP_RELEASE_GATES.md](../CAP_RELEASE_GATES.md), [CAP_FINAL_STATUS.md](../CAP_FINAL_STATUS.md), [CAP_CLAIMS.md](../CAP_CLAIMS.md) | Confirm the review gate is still open and no docs overclaim review completion. |
| Architecture and trust boundaries | [architecture.md](../architecture.md), [CAP_00_README.md](../CAP_00_README.md), [CAP_IMPLEMENTATION_ALIGNMENT.md](../CAP_IMPLEMENTATION_ALIGNMENT.md) | Verify the two-tier, three-plane target and current scaffold/production boundaries are clearly separated. |
| Threat model | [CAP_threat_model.md](../CAP_threat_model.md), [CAP_04_security_trust_evidence.md](../CAP_04_security_trust_evidence.md) | Validate threats, mitigations, and residual gaps for compromised components, replay, key compromise, PEP bypass, and privacy leakage. |
| Production key custody | [KMS/HSM operations plan](../kms_hsm/README.md), [config placeholder](../../config/kms_hsm.example.yaml) | Confirm local/demo keys remain non-production and deployment-owned key custody evidence is still required. |
| Organization policy deployment | [OPA/Cedar deployment guide](../policy_deployment/README.md), [sample policy layout](../../policies/organization_template/), [config placeholder](../../config/policy_deployment.example.yaml) | Confirm sample policies are not treated as production policy and organization-owned promotion evidence is still required. |
| Multi-organization MCP/A2A interop | [interop plan](../mcp_a2a_interop/README.md), [report template](../mcp_a2a_interop/report_template.md), [config placeholder](../../config/mcp_a2a_interop.example.yaml) | Confirm local simulation and external partner evidence are separated, and shared reports do not include raw sensitive content or secrets. |
| Domain semantic-quality evaluation | [evaluation harness](../domain_semantic_quality/README.md), [rubric](../quality/reviewer_rubric.md), [config placeholder](../../config/domain_semantic_quality.example.yaml) | Confirm semantic-quality evidence is separated from structural conformance and synthetic scores are not represented as expert validation. |
| Regulated-profile review | [regulated-profile packet](../regulated_profile_review/README.md), [checklist](../compliance/reviewer_checklist.md), [config placeholder](../../config/regulated_profile_review.example.yaml) | Confirm CAP-Med profile review remains external and the packet does not claim regulatory clearance or clinical approval. |
| Conformance and testing | [CAP_06_conformance.md](../CAP_06_conformance.md), [testing.md](../testing.md) | Run or sample the release-blocking deterministic scaffold checks and targeted security tests. |
| Security reporting | [SECURITY.md](../../SECURITY.md) | Confirm vulnerability handling and scope language match the release status. |
| Findings tracking | [findings_tracker_template.md](findings_tracker_template.md) | Use the tracker to record findings, owners, fixes, retests, and gate impact. |

## Architecture Summary

CAP v1 is documented as a supervisory control plane and semantic enforcement layer above existing transports, policy engines, identity systems, observability stacks, and workflow engines. The current repository provides deterministic scaffolds and selected hot paths; it is not a complete deployed runtime.

The high-level topology is:

- Local tier: local agents, user surfaces, local tools, local memory, Local PEP, and local PDP.
- Federated tier: Edge PEP, decomposed Control Plane, Supervisor Gateway, Session Router, PDP adapters, Human Review integration, registries, and remote agents/tools.
- Observability plane: signed audit, telemetry, provenance, and transparency evidence kept distinct from hot-path policy decisions.

Reviewers should check that data-plane traffic crossing local, network, agent, tool, and registry boundaries is mediated by the correct PEP assumptions before payload use or user-visible delivery.

## Trust Boundaries

| Boundary | Expected enforcement | Current evidence | Review questions |
|---|---|---|---|
| Local agent to user surface | Local PEP output gate, streaming lookahead, abort/correction semantics | [local_pep.py](../../src/cap_protocol/runtime/local_pep.py), [live_model_streaming.py](../../src/cap_protocol/runtime/live_model_streaming.py), [ui_abort.py](../../src/cap_protocol/runtime/ui_abort.py), [ui_correction.py](../../src/cap_protocol/runtime/ui_correction.py) | Can any user-visible path bypass Local PEP in the current bindings or scenarios? Are unsafe partial outputs handled before and after emission? |
| Local agent to raw local evidence, tools, and network | Local PEP privacy checks, evidence-reference substitution, proxy/attestation contracts | [mobile_local_pep.py](../../src/cap_protocol/runtime/mobile_local_pep.py), [attested_local_pep.py](../../src/cap_protocol/runtime/attested_local_pep.py), [tests/test_mobile_local_pep_proxy.py](../../tests/test_mobile_local_pep_proxy.py), [tests/test_attested_local_pep.py](../../tests/test_attested_local_pep.py) | Are trusted-library, separately privileged proxy, and attested-isolated modes scoped honestly? Are bypass tests sufficient for scaffold claims? |
| Local tier to federated tier | CAPEnvelope validation, signature/time checks, authority, policy, privacy-before-dereference | [edge_pep.py](../../src/cap_protocol/runtime/edge_pep.py), [authority.py](../../src/cap_protocol/runtime/authority.py), [tests/test_cap_v1_pep.py](../../tests/test_cap_v1_pep.py), [tests/test_authority_chain.py](../../tests/test_authority_chain.py) | Does verification order prevent payload-ref or raw payload use before signature, time, authority, policy, and privacy checks? |
| Authority and signing material | RFC 8785/JCS signatures, detached JWS, DSSE/in-toto, Biscuit warrants, revocation freshness | [cap_crypto.py](../../src/cap_protocol/security/cap_crypto.py), [warrants.py](../../src/cap_protocol/runtime/warrants.py), [transparency.py](../../src/cap_protocol/security/transparency.py), [tests/test_cap_crypto.py](../../tests/test_cap_crypto.py), [tests/test_warrant_primitives.py](../../tests/test_warrant_primitives.py) | Are canonical payloads unambiguous? Are holder bindings, attenuation, expiry, and revocation checks fail-closed? |
| Policy update and PDP decisions | Signed policy bundle pinning, explicit hot update, OPA/Cedar adapter parity, privacy PDP dimensions | [local_pep.py](../../src/cap_protocol/runtime/local_pep.py), [pdp_adapters.py](../../src/cap_protocol/runtime/pdp_adapters.py), [privacy_pdp.py](../../src/cap_protocol/runtime/privacy_pdp.py), [tests/test_policy_registry_service.py](../../tests/test_policy_registry_service.py), [tests/test_pdp_adapters.py](../../tests/test_pdp_adapters.py) | Can stale or mismatched policy material authorize a directive? Are emergency overrides auditable and still signature checked? |
| Evidence and registry dereference | EvidenceRef hash/freshness/access checks, content-addressed blobs, TTL deletion | [registry.py](../../src/cap_protocol/runtime/registry.py), [retention.py](../../src/cap_protocol/runtime/retention.py), [tests/test_evidence_registry_service.py](../../tests/test_evidence_registry_service.py), [tests/test_evidence_tamper.py](../../tests/test_evidence_tamper.py), [tests/test_retention_ttl_deletion.py](../../tests/test_retention_ttl_deletion.py) | Are evidence blobs re-hashed on dereference? Can expired or tampered evidence influence execution? |
| Supervisor and human review | Gateway-mediated context minimization, session routing, human escalation contracts | [supervisor_gateway.py](../../src/cap_protocol/runtime/supervisor_gateway.py), [session_router.py](../../src/cap_protocol/runtime/session_router.py), [human_review.py](../../src/cap_protocol/runtime/human_review.py), [workflow_engine.py](../../src/cap_protocol/runtime/workflow_engine.py) | Can Supervisor output overreach Local PEP vetoes? Are session boundaries and human review decisions auditable and privacy-minimized? |
| Observability and audit | Distinct audit, telemetry, provenance, signed audit operations, local transparency bundles | [observability.py](../../src/cap_protocol/runtime/observability.py), [audit_store.py](../../src/cap_protocol/hardening/audit_store.py), [collector-cap.yaml](../../config/otel/collector-cap.yaml), [tests/test_observability_plane.py](../../tests/test_observability_plane.py), [tests/test_transparency_log.py](../../tests/test_transparency_log.py) | Can telemetry failure suppress audit? Are audit records content-minimized and tamper-evident? |

## High-Risk Component Map

| Component | Why high risk | Key tests |
|---|---|---|
| Edge PEP and CAPEnvelope verification | First network/message boundary before payload use. | [tests/test_cap_v1_pep.py](../../tests/test_cap_v1_pep.py), [tests/test_grpc_reference_v1_binding.py](../../tests/test_grpc_reference_v1_binding.py), [tests/test_http_binding.py](../../tests/test_http_binding.py), [tests/test_service_mesh_composition.py](../../tests/test_service_mesh_composition.py) |
| Local PEP trust modes | Primary bypass-resistance claim for user output, local tools, network, and raw data. | [tests/test_cap_v1_pep.py](../../tests/test_cap_v1_pep.py), [tests/test_mobile_local_pep_proxy.py](../../tests/test_mobile_local_pep_proxy.py), [tests/test_attested_local_pep.py](../../tests/test_attested_local_pep.py) |
| AuthorityChain, warrants, SPIFFE binding, and signatures | Controls delegation, holder binding, scope attenuation, replay windows, and invalid signature refusal. | [tests/test_authority_chain.py](../../tests/test_authority_chain.py), [tests/test_warrant_primitives.py](../../tests/test_warrant_primitives.py), [tests/test_spiffe_workload_identity.py](../../tests/test_spiffe_workload_identity.py), [tests/test_cap_crypto.py](../../tests/test_cap_crypto.py) |
| PrivacyBoundary, redaction, embedding-only egress, and retention | Controls raw transcript/audio minimization and sensitive local evidence handling. | [tests/test_privacy_pdp.py](../../tests/test_privacy_pdp.py), [tests/test_local_ner_redaction.py](../../tests/test_local_ner_redaction.py), [tests/test_embedding_only_egress.py](../../tests/test_embedding_only_egress.py), [tests/test_retention_ttl_deletion.py](../../tests/test_retention_ttl_deletion.py) |
| Policy Registry and policy hot update | Stale policy or unsafe override could authorize behavior outside session assumptions. | [tests/test_policy_registry_service.py](../../tests/test_policy_registry_service.py), [tests/test_policy_hot_update.py](../../tests/test_policy_hot_update.py), [tests/test_pdp_adapters.py](../../tests/test_pdp_adapters.py) |
| Evidence Registry and payload-ref dereference | Evidence integrity/freshness controls can fail open if dereference order is wrong. | [tests/test_evidence_registry_service.py](../../tests/test_evidence_registry_service.py), [tests/test_federated_registry.py](../../tests/test_federated_registry.py), [tests/test_evidence_tamper.py](../../tests/test_evidence_tamper.py) |
| Audit, provenance, and transparency scaffolds | Review evidence depends on content-minimized, tamper-evident records and failure isolation. | [tests/test_observability_plane.py](../../tests/test_observability_plane.py), [tests/test_transparency_log.py](../../tests/test_transparency_log.py), [tests/test_hardening.py](../../tests/test_hardening.py) |
| Supervisor Gateway, Session Router, Human Review, workflow composition | Central authority paths can coerce unsafe output or leak private context if boundaries are weak. | [tests/test_supervisor_gateway_service.py](../../tests/test_supervisor_gateway_service.py), [tests/test_session_router.py](../../tests/test_session_router.py), [tests/test_human_review_integration.py](../../tests/test_human_review_integration.py), [tests/test_workflow_engine_composition.py](../../tests/test_workflow_engine_composition.py) |
| Live substrate interop and Go fixture adapter | External protocol integration and cross-implementation parsing are common confusion points. | [tests/test_live_substrate_interop.py](../../tests/test_live_substrate_interop.py), [tests/test_go_interop_adapter.py](../../tests/test_go_interop_adapter.py) |

## Suggested Verification Commands

Run Python commands from the repository root with the project virtual environment active:

```bash
source venv/bin/activate
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest
```

Targeted commands for review sampling:

```bash
source venv/bin/activate
python scripts/check_v1_schema_drift.py
cap-check-v1-conformance
python VERIFY_RELEASE_BASELINE.py
python scripts/check_doc_links.py
python scripts/check_claim_language.py
python run_production_hardening.py
python -m cap_protocol.scenarios.therapist_supervisor.runner --case all
python -m cap_protocol.cli.run_benchmarks --iterations 100 --warmup 10
```

Third-implementation fixture check:

```bash
cd third_impl/go_cap_adapter
go run . --fixtures testdata/cap_v1_interop.json --json
```

Reviewer-selected targeted tests:

```bash
source venv/bin/activate
pytest tests/test_cap_crypto.py tests/test_authority_chain.py tests/test_warrant_primitives.py
pytest tests/test_cap_v1_pep.py tests/test_privacy_pdp.py tests/test_policy_registry_service.py
pytest tests/test_evidence_registry_service.py tests/test_evidence_tamper.py tests/test_observability_plane.py
pytest tests/test_mobile_local_pep_proxy.py tests/test_attested_local_pep.py
```

## Expected Reviewer Focus

Reviewers are expected to probe:

- Verification order at Edge PEP and Local PEP boundaries.
- Authority-chain attenuation, holder binding, revocation, and expiry behavior.
- Canonicalization and signature metadata ambiguity across JSON, envelope, and warrant paths.
- Replay and clock-skew behavior for envelopes, directives, policies, authority steps, and evidence.
- Whether policy bundle pinning, hot update, and emergency override modes can fail open.
- Evidence dereference safety, hash mismatch handling, TTL deletion, and refusal content minimization.
- PrivacyBoundary enforcement for raw transcript/audio, redaction-before-egress, embedding-only egress, retention, and allowed recipients.
- Local PEP bypass assumptions, especially the difference between in-process tests, separately privileged proxy plans, and attested isolated mode.
- Supervisor Gateway overreach, session routing isolation, human review privacy, and workflow retry behavior.
- Audit/provenance integrity and whether logs can leak raw evidence, hidden chain-of-thought, unsafe partial output, or sensitive spans.
- Claim language consistency across release docs, baseline docs, README, and SECURITY scope.

## Open External Gaps

The following remain open even after this packet is prepared:

- Independent third-party security review completion and critical-finding remediation.
- Production KMS/HSM custody for signing, audit, warrants, transparency, rotation, and revocation.
- Production SPIRE/service-mesh rollout and external mesh smoke tests.
- Native Android/iOS project wiring, platform entitlements, device or instrumented bypass tests, and real platform attestation verifiers.
- Deployed Local PEP, Edge PEP, PDP, Policy Registry, Capability Registry, Evidence Registry, Controller, Supervisor Gateway, Session Router, Human Review, workflow, audit, telemetry, provenance, and transparency services.
- External MCP/A2A interoperability beyond local substrate scaffolds and the local Go fixture adapter.
- Production local NER and embedding model selection plus redaction/privacy/quality evaluation fixtures.
- Regulated CAP-Med profile review completion, clinical/domain semantic-quality evaluation, and organization-owned policy review.
- Deployment-representative latency, mobile CPU/memory/battery, networked registry/PDP, service-mesh, and outage behavior measurements.

## Review Closure Rule

The security-review gate in [CAP_RELEASE_GATES.md](../CAP_RELEASE_GATES.md) can close only after:

- external reviewers complete the scoped review;
- findings are recorded in a tracker derived from [findings_tracker_template.md](findings_tracker_template.md);
- no critical findings remain unresolved in authority, signing, privacy, PEP bypass, policy update, evidence, or audit behavior;
- fixes have regression tests or documented operational mitigations;
- release docs and claim-language checks are updated to reflect the result without overclaiming.
