# Security Review Findings Tracker Template

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: engineers
> **Tags**: `engineering`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

Use this template during an independent security review. It is intentionally empty; filling it out records review evidence but does not by itself close the external review gate in CAP_RELEASE_GATES.md (target archived/removed).

## Review Metadata

| Field | Value |
|---|---|
| Reviewer organization / reviewer names | TBD |
| Review start date | TBD |
| Review end date | TBD |
| Repository commit SHA | TBD |
| Reviewed release labels | `v0.1-production-candidate`, `v1-architecture-documented`, `v1-runtime-scaffold` |
| Packet used | README.md (target archived/removed) |
| Test commands run | TBD |
| Artifacts reviewed | TBD |
| Out-of-scope areas | TBD |

## Severity Definitions

| Severity | Definition | Gate impact |
|---|---|---|
| Critical | Allows unauthorized authority expansion, signature bypass, Local/Edge PEP bypass, raw sensitive-data egress, unsafe policy update authorization, evidence tamper acceptance, audit forgery, or comparable compromise of the core CAP security model. | Blocks the independent security review gate until fixed and retested. |
| High | Materially weakens a security boundary but has a narrower exploit path, requires special preconditions, or affects a scaffold claim rather than a claimed production behavior. | Requires fix, mitigation, or explicit release-gate deferral before any stable-release claim. |
| Medium | Security weakness with limited impact, partial mitigation, or primarily defense-in-depth value. | Track to closure or documented backlog with owner. |
| Low | Documentation, hardening, test coverage, or minor implementation issue with limited direct exploitability. | Track in backlog or fix opportunistically. |
| Informational | Clarification, suggested improvement, or non-security observation. | No release gate impact unless later reclassified. |

## Finding Lifecycle

Allowed statuses:

- `draft`
- `confirmed`
- `fix_in_progress`
- `fixed_awaiting_retest`
- `retested_fixed`
- `accepted_risk`
- `duplicate`
- `not_applicable`

Unresolved critical findings cannot be closed as `accepted_risk` before any future stable-release security-review gate.

## Findings

| ID | Date | Severity | Status | Area | Component / refs | Summary | Impact | Reproduction / evidence | Recommended fix | Owner | Fix PR / commit | Regression tests | Reviewer retest result | Gate impact | Closure date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| SEC-001 | TBD | TBD | draft | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |

## Closure Checklist

Before claiming the independent security review gate is complete:

- All critical findings are `retested_fixed` or reclassified with reviewer agreement.
- High findings have fixes, mitigations, or explicit release-gate deferrals.
- Regression tests were added or existing tests were cited for each fixed finding.
- Documentation and release-gate language were updated for any changed claim status.
- `python scripts/check_claim_language.py` passes.
- `python scripts/check_doc_links.py` passes.
- The final review report is linked from this tracker or from the release-gate evidence record.
