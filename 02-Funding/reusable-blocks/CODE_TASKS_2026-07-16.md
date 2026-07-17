# Standardization Engine, Code Tasks (for independent Claude Code instances)

> **Status:** Open · **Date:** 2026-07-16 · **Author:** Shahin Mohammadi · **Rule:** doc/data consolidation is done in Cowork; these CODE/engine tasks run as independent Claude Code sessions. Commit as Shahin Mohammadi; tag before changes; do not touch IGoR Google Docs.

Repos: docs = `~/repos/cytognosis/docs` (authoring source for slot-library data); code = `~/repos/cytognosis/cytos` (`src/cytos/scholarly/funding/`, engine + schema mirror).

1. **Adopt or gate the 6 registry entries.** In the docs manifest (`02-Funding/reusable-blocks/slot-library/manifest.yaml`), reconcile the 6 funders present only in the cytos mirror (`nsf_xlabs`, `nsf_sbir_phase1`, `nsf_sbir_phase2`, `nsf_sbir_phase2b`, `nih_r21`, `arpah_program_iso`): either add matching `funders/*.yaml` or mark the entries `planned: true` so `require_all_funder_files` validation passes. Priority configs to build first: `arpah_program_iso` (precision-psych ISO) and `nsf_xlabs`.
2. **Build new priority funder configs** from the landscape: `primed_ai` (D2M-AIP, Cytognosis-PI-eligible, due 2026-10-19) and `nsf_sch` (NSF 25-542). Map their questions to U/A slots; add section-size limits.
3. **Relabel `yc_nonprofit`** (YC S26 is a for-profit PBC) atomically across the docs manifest, `funders/`, and `opportunity_mapping.{yaml,csv}`; update all references.
4. **Sync docs to cytos and validate.** Copy `slot-library/{manifest.yaml,opportunity_mapping.*,groups.yaml}` into `cytos/src/cytos/scholarly/funding/schemas/`; run `nox -s parse_grants` in cytos; fix the parser if new F-fields or entries break loading. Acceptance: `nox -s parse_grants` green and manifest validation passes.

Each task: backup tag first, commit in logical chunks as Shahin Mohammadi, report a before/after validation result.
