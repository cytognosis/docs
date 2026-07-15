# Regulated-Profile Review Packet

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: engineers
> **Tags**: `engineering`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

This packet prepares CAP-Med, and future regulated profiles, for external domain review. It is a reviewer starting point, not evidence that regulatory, clinical, safety, or domain approval has happened.

CAP-Med is used here as the primary example because it is the motivating regulated profile in this repository. The same packet shape can be reused for other regulated profiles by replacing the profile constraints, forbidden behaviors, evidence examples, and reviewer roster.

## Review Objective

Review whether the CAP-Med profile behavior is clearly bounded, privacy-preserving, non-diagnostic, non-prescriptive, and appropriately escalated when safety or policy concerns appear.

This review is separate from:

- structural CAP conformance, which is checked by `cap-check-v1-conformance`;
- domain semantic-quality scoring, which is prepared under [domain_semantic_quality](../quality/README.md);
- independent security review, which is prepared under [security_review](../security/security_review.md);
- organization policy deployment, which is prepared under [policy_deployment](../../infrastructure/policy-deployment/README.md).

## Scope

In scope:

- CAP-Med profile constraints and extension placement.
- Therapist/interviewer output boundaries.
- Supervisor Gateway authority separation and Local PEP veto behavior.
- Human Review escalation behavior.
- Privacy controls for raw transcript/audio, redaction, embedding-only egress, retention, audit, and reviewer visibility.
- User-facing refusal and correction behavior.
- Evidence examples and deterministic test evidence.
- Known limitations and open review questions.

Out of scope:

- claiming clinical efficacy, clinical safety, regulated-profile approval, or regulatory clearance;
- reviewing a deployed clinical product;
- approving production model providers, clinical workflows, or organization-specific policies;
- replacing a qualified domain, legal, privacy, or security review.

## Reviewer Starting Map

| Area | Primary docs | Evidence to inspect |
|---|---|---|
| Profile architecture | CAP_07_profiles_roadmap.md (target archived/removed), CAP_03_primitives.md (target archived/removed) | Confirm CAP-Med rules stay under `profile_constraints.cap-med/v1` and `profile_extensions.cap-med/v1`, not CAP Core. |
| CAP-Med fixture | [cap_med.py](../../src/cap_protocol/profiles/cap_med.py), [test_cap_med_v1_profile.py](../../tests/test_cap_med_v1_profile.py) | Confirm Core schemas are reused and CAP-Med constraints are profile-owned. |
| Local PEP boundaries | [local_pep.py](../../src/cap_protocol/runtime/local_pep.py), [test_cap_v1_pep.py](../../tests/test_cap_v1_pep.py) | Confirm raw-data, diagnosis, treatment-advice, and unsafe stream paths are vetoed or transformed. |
| Supervisor Gateway | [supervisor_gateway.py](../../src/cap_protocol/runtime/supervisor_gateway.py), [test_supervisor_gateway_service.py](../../tests/test_supervisor_gateway_service.py) | Confirm Supervisor authority role, gateway endpoint, and backend engine remain distinct, and raw context is withheld from backends. |
| Human Review | [human_review.py](../../src/cap_protocol/runtime/human_review.py), [test_human_review_integration.py](../../tests/test_human_review_integration.py) | Confirm safety escalation can route to human review without raw transcript leakage. |
| Semantic-quality harness | [domain_semantic_quality](../quality/README.md), [synthetic cases](../../examples/domain_semantic_quality/) | Confirm synthetic examples are labeled as onboarding evidence only. |
| Release gates | CAP_RELEASE_GATES.md (target archived/removed), CAP_FINAL_STATUS.md (target archived/removed), CAP_CLAIMS.md (target archived/removed) | Confirm regulated-profile review remains an external gate. |

## Profile Constraints

The CAP-Med v1 runtime-profile fixture declares these constraints under `OperationalConstraints.profile_constraints.cap-med/v1`:

| Constraint | Expected behavior |
|---|---|
| `non_diagnostic_required` | The Therapist/interviewer must not diagnose or imply a diagnosis. |
| `non_prescriptive_required` | The system must not prescribe treatment, medication, or clinical action. |
| `clinical_output_forbidden` | Clinical labels, diagnoses, and treatment claims are forbidden in profile-owned output. |
| `raw_transcript_upload_forbidden` | Raw transcript upload is forbidden by default. |
| `raw_audio_upload_forbidden` | Raw audio upload is forbidden by default. |
| `supervisor_context_redacted_by_default` | Supervisor context uses redacted context, EvidenceRefs, or embedding-only payloads by default. |
| `local_pep_veto_required` | Local PEP can refuse Supervisor or backend output that violates local policy. |
| `supervisor_overreach_veto_required` | Supervisor overreach cannot bypass Local PEP privacy, non-diagnostic, or safety rules. |
| `psychological_test_results_are_screening_only` | Profile examples must not present screening outputs as diagnostic results. |

Reviewers should confirm the constraints are understandable, sufficiently narrow, and aligned with the intended domain scope.

## Forbidden Behaviors

The profile should refuse, transform, pause, escalate, or reroute these behaviors:

| Behavior | Expected CAP handling | Evidence |
|---|---|---|
| Diagnostic label or disease claim | Transform before user display or refuse Supervisor directive. | `tests/test_cap_v1_pep.py`, `tests/test_slow_path_classifier.py` |
| Treatment plan, medication advice, or prescriptive clinical instruction | Transform before user display or refuse Supervisor directive. | `tests/test_cap_v1_pep.py`, `tests/test_live_model_streaming.py` |
| Raw transcript/audio egress to Supervisor or backend | Replace with local EvidenceRefs, redacted context, or embedding-only payload; refuse raw egress. | `tests/test_cap_v1_pep.py`, `tests/test_supervisor_gateway_service.py` |
| Supervisor request for raw data, diagnosis, or treatment advice | Local PEP veto with typed refusal. | `tests/test_cap_v1_pep.py`, `tests/test_supervisor_gateway_service.py` |
| Unsafe late stream content | Emit correction frame and linked audit/report refs without quoting unsafe content. | `tests/test_correction_frame_ux.py` |
| Safety concern requiring human judgment | Escalate to Human Review with minimized context. | `tests/test_human_review_integration.py` |

## Escalation Rules

CAP-Med profile behavior maps profile labels onto Core `InterruptDecision.action` values:

| Profile situation | Core action | Review focus |
|---|---|---|
| Diagnostic or treatment drift before display | `transform` | Replacement content must remain supportive and non-diagnostic. |
| Uncertain or sensitive Supervisor review needed | `pause` | User-facing behavior should be safe during pause. |
| Safety or policy exception requires qualified review | `escalate` | Human Review request must be minimized and auditable. |
| Reviewer or code-owner style routing for profile exception | `reroute` | Recipient must be authorized and privacy-bounded. |
| Raw-data or policy overreach | `deny` | Refusal must be typed and must not leak raw content. |
| Safe supportive next question under constraints | `allow` or `constrain` | Output remains inside profile constraints. |

Reviewers should check whether these mappings are sufficient for the intended regulated use case and whether additional escalation triggers are needed.

## Privacy Controls

CAP-Med uses the structured `PrivacyBoundary` dimensions as reviewable policy facts:

| Privacy dimension | CAP-Med expectation |
|---|---|
| Classification | Behavioral-health, raw transcript/audio, redacted transcript, embeddings, dimension vectors, safety flags, and EvidenceRefs are distinguished. |
| Movement | Raw transcript/audio are local-only by default. |
| Transformation | Redaction is required before Supervisor context; embedding-only egress is allowed only when policy permits it. |
| Retention | Raw backing content has TTL-driven deletion in the deterministic scaffold; audit retention is separate. |
| Logging | Shared audit/provenance records must use hashes, ids, refs, and `raw_content_logged=false`. |
| Audit visibility | Reviewer and auditor visibility must be bounded by policy. |
| Allowed recipients | Supervisor Gateway, Human Review, and other recipients must be explicit. |
| Raw-data egress | Raw transcript and raw audio egress are denied by default. |
| Minimization | EvidenceRefs, redacted summaries, embeddings, and aggregate dimensions are preferred over raw content. |

Reviewers should identify any missing privacy controls for the intended jurisdiction, user population, and deployment environment.

## User-Facing Refusals and Corrections

The current deterministic scaffold uses typed refusals and safe replacement/correction behavior:

| Situation | Expected user-facing behavior |
|---|---|
| Diagnosis request | Decline diagnosis and continue with bounded supportive reflection where appropriate. |
| Treatment-advice request | Decline prescriptive guidance and route to appropriate human/professional context where appropriate. |
| Raw-data request from Supervisor/backend | Do not expose raw content; return typed privacy refusal internally. |
| Unsafe buffered stream | Replace before display with safe non-diagnostic text. |
| Unsafe late stream | Emit correction frame without quoting unsafe original text. |
| Safety concern | Escalate or pause according to profile policy with minimal necessary content. |

Domain reviewers should assess whether the wording is acceptable, whether escalation language is appropriate, and whether any user-facing refusal could be misleading, overconfident, or insufficiently supportive.

## Evidence Examples

Reviewers can inspect these concrete evidence shapes:

| Evidence type | Repository example |
|---|---|
| CAP-Med `PrivacyBoundary` | `cap_med_reference_profile_fixture()["privacy_boundary"]` |
| CAP-Med `OperationalConstraints` | `cap_med_reference_profile_fixture()["operational_constraints"]` |
| CAP-Med `Directive` and `CAPEnvelope` | `cap_med_reference_profile_fixture()` |
| CAP-Med `Capability` records | `cap_med_capabilities()` |
| CAP-Med `EvidenceRef` records | `cap_med_evidence_refs()` |
| CAP-Med interrupt mappings | `cap_med_profile_interrupts(...)` |
| Synthetic semantic-quality cases | `examples/domain_semantic_quality/cap_med_synthetic_cases.jsonl` |

These are deterministic fixtures and examples. They are review inputs, not approval evidence by themselves.

## Suggested Verification Commands

Run from the repository root:

```bash
source venv/bin/activate
pytest tests/test_cap_med_v1_profile.py tests/test_supervisor_gateway_service.py tests/test_human_review_integration.py tests/test_semantic_quality_evaluation.py
python scripts/check_doc_links.py
python scripts/check_claim_language.py
```

Optional broader profile/PEP sampling:

```bash
source venv/bin/activate
pytest tests/test_cap_v1_pep.py tests/test_slow_path_classifier.py tests/test_live_model_streaming.py tests/test_correction_frame_ux.py
```

## Known Limitations

- The packet does not establish regulated-profile approval, clinical safety, clinical efficacy, or regulatory clearance.
- CAP-Med examples remain non-diagnostic and non-prescriptive; they are not a medical-device workflow.
- Synthetic semantic-quality cases are onboarding fixtures only.
- Production Supervisor Gateway rollout, backend integration, reviewer authentication, Human Review portal deployment, audit/provenance operations, KMS/HSM custody, organization policy deployment, and external security review remain separate gates.
- Native mobile trust modes, device/instrumented evidence, model-provider behavior, and deployment-specific privacy/legal review remain external.
- Domain experts still need to decide whether the profile constraints, escalation paths, refusal copy, and privacy rules are adequate for the intended use.

## Reviewer Workflow

1. Read this packet and [reviewer_checklist.md](reviewer_checklist.md).
2. Inspect the CAP-Med fixture, Local PEP, Supervisor Gateway, Human Review, and synthetic semantic-quality artifacts listed above.
3. Run or request the suggested verification commands.
4. Record findings, open questions, required wording changes, and gate impact in [report_template.md](report_template.md).
5. Resolve or explicitly carry any blocking findings before release-gate language changes.

## Closure Rule

The regulated-profile review gate can close only when:

- qualified domain experts or profile owners complete the review;
- reviewer qualifications, scope, independence, and conflicts are recorded;
- profile constraints, forbidden behaviors, escalation paths, privacy controls, refusal/correction copy, evidence examples, and limitations are reviewed;
- blocking findings are resolved or carried as explicit release blockers;
- structural CAP conformance, semantic-quality scoring, security review, and organization policy deployment remain separately reported.
