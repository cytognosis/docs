# Domain Semantic-Quality Evaluation Report Template

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: engineers
> **Tags**: `engineering`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

Use this template for human-readable evaluation reports. Attach the harness JSON report as a machine-readable artifact.

## Run Metadata

| Field | Value |
|---|---|
| Report id |  |
| Profile |  |
| Domain |  |
| Dataset tier | synthetic onboarding / expert-authored challenge set / consent-governed pilot data |
| Harness command |  |
| CAP structural conformance report | separate artifact ref |
| Gate conclusion | external_expert_evidence_required / ready_for_gate_review / blocked |
| Report owner |  |

## Dataset Manifest

| Case set | Case count | Synthetic count | Consent/governance refs | Source hash refs |
|---|---:|---:|---|---|
|  |  |  |  |  |

## Reviewer Roster

| Reviewer id | Role | Qualification or profile-owner basis | Independence/conflict notes |
|---|---|---|---|
|  |  |  |  |

## Criteria and Thresholds

| Criterion | Passing threshold | Required reviewers | Blocking flags |
|---|---:|---:|---|
|  |  |  |  |

## Aggregate Results

| Status | Count |
|---|---:|
| pass |  |
| needs_review |  |
| needs_revision |  |
| blocked |  |

## Case Results

| Case id | Review count | Status | Low criteria | Blocking flags | Retest needed |
|---|---:|---|---|---|---|
|  |  |  |  |  |  |

## Privacy Review

| Check | Result | Evidence |
|---|---|---|
| Shared cases exclude raw transcript/audio, raw sensitive evidence, hidden reasoning, and credentials. |  |  |
| Non-synthetic cases include consent or governance refs. |  |  |
| Reviewer notes avoid raw sensitive spans. |  |  |
| Dataset and report retention are documented. |  |  |

## Findings and Retest

| Finding id | Severity | Description | Owner | Status | Retest evidence |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

## Gate Conclusion

State exactly one conclusion:

- `external_expert_evidence_required`: synthetic-only run, incomplete reviewer depth, or no qualified domain expert review.
- `blocked`: a required criterion failed, a blocking flag is unresolved, or privacy review failed.
- `ready_for_gate_review`: qualified reviewers completed the plan, no blocking findings remain, and structural CAP conformance is reported separately.

Sign-off:

| Reviewer or owner | Role | Date | Notes |
|---|---|---|---|
|  |  |  |  |
