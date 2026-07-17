# Grants & Applications Consolidation, Living Log (2026-07-16)

> **Status:** Active · **Owner:** Shahin Mohammadi (with Claude) · **Backup tag:** `pre-grants-consolidation-2026-07-16` @ `dc3dfd9` (docs repo)
> This is the single "where are we" doc for the grants/applications consolidation program. Companion docs in this folder: `MASTER_CONSOLIDATION_PLAN_2026-07-16.md`, `01_ASSET_INVENTORY.md`, `00_PRIOR_WORK_SYNTHESIS.md`.

**If you only read one thing:** the phase table and the commit ledger below.

## Guardrails in force

- Backup before destructive actions (tag set); archive over delete; never delete unique content; md5 before removing any duplicate.
- Commit in logical chunks as **Shahin Mohammadi <mohammadi@cytognosis.org>**; stage explicit paths, never `git add -A`.
- Do not touch IGoR Google Docs programmatically. No PI salary figure. No private dollar target. Voice: no "revolutionary / breakthrough / cure"; never "Substrate"; CAP is Cytoplex; Neuroverse off small pilots.
- **Connector caveat:** the Monday connector needs re-authorization (non-interactive session cannot run OAuth), so the Phase 6 Monday board sync is deferred to Shahin.

## Systems of record (verified 2026-07-16)

| Asset | Canonical home |
|---|---|
| Prose funding docs | `docs/02-Funding/` (repo `~/repos/cytognosis/docs`, branch `main`) |
| Standardization (slots, funders, manifest) authoring home | `docs/02-Funding/reusable-blocks/` |
| Render engine + code-consumed schema copy | `cytos/src/cytos/scholarly/funding/` |
| Raw parsed solicitations | `cytos/data/staged/grants/` |
| Primary tables / curated data | `~/datasets/cytognosis/` (git + DVC) |
| Science / ontology backbone for biotyping | `datasets/ontologies/{clinical-instruments,rdoc,neuromondo,disease}/`, `datasets/science-platform/` |
| Live memory / index | cytomem (Neo4j) |

## Phase status

| Phase | Name | Status |
|---|---|---|
| 0 | Setup (synthesis + ground truth + plan) | Done |
| 1 | Discover & classify (incl. cytos + datasets) | Done |
| 2 | Verify & backup (tag + validation) | In progress |
| 3 | Taxonomy freeze + fold orphan duplicates | Pending |
| 4 | Standardization: sizes + values + canonical/sync + bug fixes | Pending |
| 5 | Previous applications: per-app records + registry rebuild | In progress |
| 6 | Funding opps: eligibility axes + EU/UK + entity memo | Pending |
| 7 | Precision-psych 1-pager / SS / proposal (draft) | Pending |
| 8 | Biotyping dossier index + figure spec | Pending |
| 9 | READMEs / INDEX / branch note / memory | Pending |

## Commit ledger

| # | Commit subject | Phase | Hash |
|---|---|---|---|
| 0 | (safety tag `pre-grants-consolidation-2026-07-16`) | 2 | dc3dfd9 |

## Open items for Shahin

- Trigger Monday board sync once the connector is re-authorized (Phase 6 output is Monday-ready CSV).
- Confirm the three Verify-flagged statuses if Gmail check is inconclusive.
- Entity decision (Madhvi partner vs UK/EU branch): review the Phase 6 memo, decide with counsel.
