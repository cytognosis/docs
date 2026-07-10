# Regulated-Profile Reviewer Checklist

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: engineers
> **Tags**: `engineering`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

Use this checklist when reviewing CAP-Med or another regulated profile. Mark each item as pass, needs revision, blocked, or out of scope.

## Profile Scope

| Item | Review prompt | Status |
|---|---|---|
| Profile purpose is clear. | Does the profile describe what it does and what it does not do? |  |
| CAP Core boundary is preserved. | Are regulated-domain rules kept in `profile_constraints` or `profile_extensions` rather than Core fields? |  |
| Non-diagnostic boundary is clear. | Does the profile avoid diagnostic labels, disease claims, and clinical determinations? |  |
| Non-prescriptive boundary is clear. | Does the profile avoid treatment plans, medication advice, and prescriptive clinical instructions? |  |
| Screening-only language is clear. | Are psychometric or behavioral outputs framed as screening/reflection, not diagnosis? |  |

## Forbidden Behaviors

| Item | Review prompt | Status |
|---|---|---|
| Diagnosis attempts fail safely. | Are diagnostic requests refused or transformed before user-visible output? |  |
| Treatment advice fails safely. | Are treatment-advice requests refused or transformed before user-visible output? |  |
| Raw transcript/audio egress is blocked. | Does raw data stay local by default and fail closed when requested externally? |  |
| Supervisor overreach is vetoed. | Can Local PEP override unsafe Supervisor or backend output? |  |
| Unsafe stream content is handled. | Are buffered and late-stream unsafe outputs transformed or corrected without unsafe leakage? |  |

## Escalation and Human Review

| Item | Review prompt | Status |
|---|---|---|
| Escalation triggers are sufficient. | Are safety, jurisdiction, and policy-exception triggers defined clearly enough? |  |
| Human Review context is minimized. | Does review receive redacted context, safety flags, and EvidenceRefs rather than raw transcript by default? |  |
| Reviewer authority is bounded. | Are reviewer roles, allowed operations, and audit refs defined? |  |
| User-facing escalation wording is acceptable. | Does escalation language avoid alarm, overclaiming, and unsupported advice? |  |

## Privacy and Audit

| Item | Review prompt | Status |
|---|---|---|
| PrivacyBoundary dimensions are complete. | Are classification, movement, transformation, retention, logging, audit visibility, allowed recipients, raw egress, and minimization covered? |  |
| Redaction happens before egress. | Is redacted context or embedding-only context used before Supervisor/backend access? |  |
| Retention expectations are reviewable. | Are raw backing-content TTL and audit retention treated separately? |  |
| Logs avoid raw sensitive content. | Do reports, audit, telemetry, and provenance avoid raw transcript/audio and hidden reasoning? |  |
| Reviewer visibility is bounded. | Are reviewer/auditor scopes explicit? |  |

## Evidence and Tests

| Item | Review prompt | Status |
|---|---|---|
| Profile fixture is inspectable. | Can reviewers inspect CAP-Med PrivacyBoundary, constraints, directives, capabilities, and EvidenceRefs? |  |
| Test commands are reproducible. | Do the suggested tests pass in the reviewed checkout? |  |
| Synthetic examples are labeled. | Are synthetic semantic-quality fixtures clearly separated from expert evidence? |  |
| Known limitations are complete. | Are missing production, security, policy, privacy, and domain-review items visible? |  |

## Open Questions

Record unresolved questions in [open_questions.md](open_questions.md) or the final review report.
