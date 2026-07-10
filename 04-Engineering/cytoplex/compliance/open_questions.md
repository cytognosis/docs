# Regulated-Profile Open Questions

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: engineers
> **Tags**: `engineering`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

These questions should be answered by domain experts, profile owners, privacy/legal reviewers, and deployment owners before a regulated-profile review gate can close.

## CAP-Med Profile Scope

1. Is the "supportive local interviewer" role sufficiently narrow for the intended use?
2. Are any user-facing terms likely to imply therapy, diagnosis, clinical assessment, or treatment?
3. Should the profile distinguish crisis, acute risk, ordinary distress, and non-urgent support with more explicit routing?
4. Which domain expert roles are required for sign-off, and what conflicts of interest are disallowed?

## Non-Diagnostic and Non-Prescriptive Boundaries

1. Are the forbidden behavior examples complete enough for the intended population and jurisdiction?
2. Should additional categories be blocked, such as medication changes, emergency triage instructions, legal advice, or insurance/benefit advice?
3. Are the safe replacement and refusal patterns understandable to users without implying clinical authority?
4. Which outputs require human review even if they do not contain explicit diagnosis or treatment advice?

## Escalation and Human Review

1. Which safety signals require immediate escalation, pause, or reroute?
2. What should the user see while a Human Review request is pending?
3. What information can a human reviewer access by default?
4. Who can approve exceptions to raw transcript/audio access, and how is that approval audited?
5. What are the service-level expectations for review queues in a real deployment?

## Privacy, Data, and Retention

1. Which data classes must remain local for the intended deployment?
2. Are redaction categories sufficient for the user population and expected language coverage?
3. Are embedding-only payloads acceptable for the intended privacy model?
4. What consent or governance reference is required for non-synthetic review datasets?
5. What retention period is appropriate for raw backing content, review notes, audit records, and provenance records?

## Evidence and Evaluation

1. Which synthetic cases are missing from `examples/domain_semantic_quality/`?
2. What expert-authored challenge cases are required before domain review?
3. What semantic-quality criteria and pass thresholds should apply to this profile?
4. Which structural conformance tests are release blockers for this profile?
5. Which findings would block public claims, pilot use, or broader deployment?

## Release Claims

1. What exact claim language is acceptable after review completion?
2. Which claims must remain disallowed even after this review?
3. What documentation must change if the review finds material gaps?
4. How should review findings be retested and archived?
