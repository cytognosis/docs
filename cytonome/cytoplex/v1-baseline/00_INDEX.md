# CAP V1 Baseline Documentation Index

**Generated:** 2026-05-25T06:54:46+00:00
**Folder:** `docs/v1_baseline/`
**Document count:** 18 Markdown files including this index.
**Cap requested:** maximum 20 Markdown documents.

This folder is the consolidated baseline V1 documentation set for the repository. It gathers the current public docs, status/claims language, schemas, examples, implementation alignment, development notes, and prompt archive into a capped Markdown-only set.

## What this release contains

| Area | Status |
|---|---|
| CAP V1 architecture baseline | documented |
| 11 Core schemas | implemented |
| gRPC + HTTP/JSON bindings on V1 CAPEnvelope | implemented |
| V1-C01..V1-C15 conformance | release-blocking |
| 15-case Therapist/Supervisor scenario | implemented |
| federated registries | reference service |
| Biscuit-v2 warrants, SPIFFE SVID, RFC 8785 JCS | scaffold + tests |
| Phase 3 capabilities | deterministic scaffolds |
| Phase 4 readiness packets | readiness packets |
| production deployment certification | not claimed |

## What this release is not

- not a complete production runtime
- not a clinical product
- not externally security-reviewed; packet is ready, execution pending
- not a stable public standard

## Current Status

- CAP V1 is documented as the Control Authority Protocol target architecture.
- This repository contains a V1 runtime scaffold and selected V1 hot paths.
- The executable package label remains `v0.1-production-candidate`.
- The repository must not be described as a complete CAP V1 runtime, a stable public standard, or production deployment certification.

## Documents

- [`01_status_overview_and_claims.md`](./01_status_overview_and_claims.md)
- [`02_foundations_and_core_model.md`](./02_foundations_and_core_model.md)
- [`03_architecture.md`](./03_architecture.md)
- [`04_primitives.md`](./04_primitives.md)
- [`05_security_trust_and_threat_model.md`](./05_security_trust_and_threat_model.md)
- [`06_integrations_api_and_bindings.md`](./06_integrations_api_and_bindings.md)
- [`07_conformance_testing_and_release_gates.md`](./07_conformance_testing_and_release_gates.md)
- [`08_schema_appendix.md`](./08_schema_appendix.md)
- [`09_examples.md`](./09_examples.md)
- [`10_profiles_roadmap_and_backlog.md`](./10_profiles_roadmap_and_backlog.md)
- [`11_implementation_alignment.md`](./11_implementation_alignment.md)
- [`12_supervisor_and_research_positioning.md`](./12_supervisor_and_research_positioning.md)
- [`13_development_and_operations.md`](./13_development_and_operations.md)
- [`14_changelog_and_references.md`](./14_changelog_and_references.md)
- [`15_done_prompt_archive.md`](./15_done_prompt_archive.md)
- [`16_open_prompt_archive.md`](./16_open_prompt_archive.md)
- [`17_repository_artifact_inventory.md`](./17_repository_artifact_inventory.md)

## Reading path by role

| Role | Start with |
|---|---|
| new readers | [`01_status_overview_and_claims.md`](./01_status_overview_and_claims.md), then [`03_architecture.md`](./03_architecture.md) |
| implementers | [`03_architecture.md`](./03_architecture.md), [`04_primitives.md`](./04_primitives.md), [`11_implementation_alignment.md`](./11_implementation_alignment.md) |
| security reviewers | [`05_security_trust_and_threat_model.md`](./05_security_trust_and_threat_model.md), then `../security_review/README.md` |
| conformance reviewers | [`07_conformance_testing_and_release_gates.md`](./07_conformance_testing_and_release_gates.md), then [`08_schema_appendix.md`](./08_schema_appendix.md) |
| Phase 3 scaffold reviewers | [`10_profiles_roadmap_and_backlog.md`](./10_profiles_roadmap_and_backlog.md), [`11_implementation_alignment.md`](./11_implementation_alignment.md) |
| Phase 4 readiness reviewers | `../security_review/README.md`, `../kms_hsm/README.md`, `../mcp_a2a_interop/README.md`, `../domain_semantic_quality/README.md`, `../regulated_profile_review/README.md` |
| release reviewers | this index, [`17_repository_artifact_inventory.md`](./17_repository_artifact_inventory.md), `../../VERIFY_RELEASE_BASELINE.py` |

## Verification Commands

From the repository root:

```bash
pip install -e ".[dev]"
cap-check-v1-schema-drift
cap-check-v1-conformance
NO_PROXY=127.0.0.1,localhost no_proxy=127.0.0.1,localhost pytest -q
python -m cap_protocol.scenarios.therapist_supervisor.runner --case all
python VERIFY_RELEASE_BASELINE.py
```
