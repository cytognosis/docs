# Grants & Applications Consolidation, Living Log (2026-07-16)

> **Status:** Complete for this session (follow-ups listed) · **Owner:** Shahin Mohammadi (with Claude) · **Backup tag:** `pre-grants-consolidation-2026-07-16` @ `dc3dfd9`
> Companion docs in this folder: `MASTER_CONSOLIDATION_PLAN_2026-07-16.md`, `01_ASSET_INVENTORY.md`, `00_PRIOR_WORK_SYNTHESIS.md`, `submission-registry.REBUILT.md`.

**If you only read one thing:** the commit ledger and the follow-ups. Everything is version-controlled in `~/repos/cytognosis/docs` on branch `main`, committed as Shahin Mohammadi.

## Guardrails honored

- Safety tag set before writes; archive over delete (3 orphans relocated, none deleted); explicit-path staging, never `git add -A`.
- IGoR Google Docs untouched; no PI salary; impact framed as lives; voice rules kept.
- Monday sync deferred (connector needs re-authorization; non-interactive session cannot run OAuth).

## Systems of record

| Asset | Canonical home |
|---|---|
| Prose funding docs | `docs/02-Funding/` (branch `main`) |
| Standardization authoring source | `docs/02-Funding/reusable-blocks/` (+ `slot-library/`) |
| Render engine + code-consumed schema mirror | `cytos/src/cytos/scholarly/funding/` |
| Raw parsed solicitations | `cytos/data/staged/grants/` |
| Primary tables / curated data | `~/datasets/cytognosis/` (git + DVC) |
| Biotyping / ontology backbone | `datasets/ontologies/{clinical-instruments,...}`, `docs/05-Research/foundational/` |

## Phase status (all complete this session unless noted)

| Phase | Name | Status |
|---|---|---|
| 0 | Setup (synthesis, ground truth, plan) | Done |
| 1 | Discover & classify (docs + cytos + datasets) | Done |
| 2 | Verify & backup (tag) | Done |
| 3 | Fold orphan duplicates | Done (3 relocated) |
| 4 | Standardization: counts, canonical/sync, sizes, values | Done |
| 5 | Per-application records + registry rebuild | Done (17 records + 2 stubs) |
| 6 | Funding opps: eligibility axes + EU/UK + entity memo | Done |
| 7 | Precision-psych 1-pager + ISO/Convergent homes | Done (draft) |
| 8 | Biotyping dossier index + figure spec | Done |
| 9 | READMEs, branch note, log, memory | Done |

## Commit ledger (docs repo, all authored Shahin Mohammadi)

| # | Subject | Hash |
|---|---|---|
| tag | safety tag `pre-grants-consolidation-2026-07-16` | dc3dfd9 |
| 1 | consolidation kickoff (plan, inventory, synthesis, log) | 9d942f1 |
| 2 | rebuild submission registry (verified 2026-07-16 statuses) | 7ffd062 |
| 3 | fold 3 orphan duplicates (archived, pointers) | cf5081b |
| 4 | correct funder-config count to 10 | a47460b |
| 5 | slot-library canonical-source + render-engine + sync doc | e3d5c66 |
| 6 | section-size budgets + per-funder values view | 76c9f6f |
| 7 | biotyping dossier index + figure spec | 16f1040 |
| 8 | eligibility axes + EU/UK funders + entity memo | a8d4fcd |
| 9 | per-application INDEX records | 8df7f7f |
| 10 | precision-psych 1-pager + ISO/Convergent homes | d9bb93b |
| 11 | finalize log + README pointer | (this commit) |

## Follow-ups (not blocking; tracked)

1. **Monday board sync** once the connector is re-authorized (opportunity_mapping.csv is Monday-ready). Shahin to trigger.
2. **Adopt the 6 extra funder registry entries** into the docs manifest, then sync docs to cytos and run `nox -s parse_grants`. Build configs for `arpah_program_iso` and `nsf_xlabs` first.
3. **Relabel `yc_nonprofit`** (YC S26 is a for-profit PBC) as one atomic change across manifest, funders, opportunity_mapping.
4. **Verify 3 statuses via Gmail:** Coefficient Capacity Building, ElevenLabs, Anthropic AI for Science.
5. **Expand the precision-psych 1-pager into the 6-page ISO Solution Summary** using `section_size_budgets.md`; send the Smoller lead-ask.
6. **Ingest into biotyping dossier:** NbN tables into `datasets/treatments/nbn/`, plus the recent ADHD/depression papers, Stanford biotypes page, ADHD DSM blog.
7. **Entity:** review the memo; decide the UK/EU vehicle with Duane Valz and a CPA (recommendation on file: do not form an entity; route via Madhvi/Manchester).
