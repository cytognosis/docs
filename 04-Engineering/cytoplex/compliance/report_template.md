# Regulated-Profile Review Report Template

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: engineers
> **Tags**: `engineering`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

Use this template to record an external regulated-profile review. The report should cite evidence and findings, not replace the evidence itself.

## Run Metadata

| Field | Value |
|---|---|
| Report id |  |
| Profile | CAP-Med / other |
| Repository commit or package version |  |
| Review dates |  |
| Review type | initial / retest / limited-scope |
| Gate conclusion | external_review_required / ready_for_gate_review / blocked |
| Report owner |  |

## Reviewer Roster

| Reviewer id | Role | Qualification or profile-owner basis | Independence/conflict notes |
|---|---|---|---|
|  |  |  |  |

## Scope Reviewed

| Area | Evidence refs | Status |
|---|---|---|
| Profile constraints |  |  |
| Forbidden behaviors |  |  |
| Escalation rules |  |  |
| Privacy controls |  |  |
| User-facing refusals/corrections |  |  |
| Evidence examples |  |  |
| Test results |  |  |
| Known limitations |  |  |

## Checklist Summary

| Checklist section | Pass | Needs revision | Blocked | Notes |
|---|---:|---:|---:|---|
| Profile scope |  |  |  |  |
| Forbidden behaviors |  |  |  |  |
| Escalation and Human Review |  |  |  |  |
| Privacy and audit |  |  |  |  |
| Evidence and tests |  |  |  |  |

## Verification

| Command or evidence | Result | Notes |
|---|---|---|
| `pytest tests/test_cap_med_v1_profile.py tests/test_supervisor_gateway_service.py tests/test_human_review_integration.py tests/test_semantic_quality_evaluation.py` |  |  |
| `python scripts/check_doc_links.py` |  |  |
| `python scripts/check_claim_language.py` |  |  |

## Findings

| Finding id | Severity | Description | Owner | Status | Retest evidence |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

## Open Questions

| Question id | Question | Owner | Resolution needed before gate closure? |
|---|---|---|---|
|  |  |  |  |

## Gate Conclusion

State exactly one conclusion:

- `external_review_required`: packet prepared, but review is not complete.
- `blocked`: review found unresolved blocking issues.
- `ready_for_gate_review`: qualified reviewers completed the scoped review, no blocking findings remain, and separate security, semantic-quality, policy, and production evidence requirements are still tracked independently.

Sign-off:

| Reviewer or owner | Role | Date | Notes |
|---|---|---|---|
|  |  |  |  |
