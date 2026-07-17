# Grants Asset Inventory — 2026-07-16

**Reading time:** about 12 minutes. **Read-only recon; nothing was moved, edited, or deleted.**

**If you only read one thing:** the reorg mostly worked. The slot-library (`02-Funding/reusable-blocks/slot-library/`) is a real, working canonical system, and IGoR already has a good archive precedent (`_archive/2026-07-14_harmonize/`). The main risks are three **orphaned root-level duplicates** (Astera, Google-impact, Foresight), a **wrong funder count (17 vs actual 10)** baked into two status docs, and a **confirmed-missing** page-budget/Heilmeier guide from 2026-06-23.

**Scope covered:** `docs/02-Funding` (511 files), `docs/01-Strategy` (tracks/partnerships/planning/archive subset), `docs/05-Research` (biotyping/psychiatry subset). Branch checked out was `main`, not `reorg/universal-taxonomy-2026-06-12` (see note at bottom).

---

## A) Canonical set, by area

### Area 1 — Standardization / templates / schemas

| Path | Purpose | Last commit |
|---|---|---|
| `02-Funding/reusable-blocks/slot-library/INDEX.md` | Master orientation map for the whole canonical template system | 2026-07-15 |
| `02-Funding/reusable-blocks/slot-library/README.md` | Quick orientation, directory layout | 2026-07-15 |
| `02-Funding/reusable-blocks/slot-library/CHANGELOG.md` | v1.0 to v1.2 schema history | 2026-07-09 |
| `02-Funding/reusable-blocks/slot-library/manifest.yaml` | **Authoritative** slot/funder/F-field registry, v1.2 | 2026-07-09 |
| `02-Funding/reusable-blocks/slot-library/groups.yaml` | U/A/F group + preset composition system | 2026-07-09 |
| `02-Funding/reusable-blocks/canonical_template_format.md` | File-format spec, YAML schema, ID conventions | 2026-07-09 |
| `02-Funding/reusable-blocks/universal_template.md` | Human-readable slot definitions + per-funder Q-to-slot mapping | 2026-07-09 |
| `02-Funding/reusable-blocks/funder_crosswalk_matrix.md` | Slot x funder matrix, authoritative | 2026-07-09 |
| `02-Funding/reusable-blocks/funder_metadata.md` | F01-F38 field reference (funder-side metadata) | 2026-07-15 |
| `02-Funding/reusable-blocks/slot-library/slots/` (27 files: A01-A05, U01-U22) | Reusable proposal-content blocks | 2026-07-09, mixed authored/stub |
| `02-Funding/reusable-blocks/slot-library/funders/` (**10** yaml files) | Per-funder config: heilmeier, nih_r01, nsf_tech_labs, arpah_mission_office, doe_genesis, astera_residency, brains_accelerator, foresight_nodes, google_impact_challenge, yc_nonprofit | 2026-07-09 |
| `02-Funding/reusable-blocks/slot-library/opportunity_mapping.yaml` + `.csv` + `opportunity_mapping_index.md` | Master 71-opportunity mapping (all F-fields, slot requirements) | 2026-07-09 |
| `02-Funding/reusable-blocks/slot-library/research/` (funding_opps_inventory.md, research_summary.md, `profiles/` x71) | Per-opportunity research profiles feeding the schema | 2026-07-09 |
| `02-Funding/reusable-blocks/slot-library/proposals/astera_2026/` | Worked example: proposal-specific slot overrides (U01, U03, U10) | 2026-07-09/07-15 |
| `02-Funding/simple/README.md` | 1-minute plain-language companion; correctly points to slot-library as system of record | 2026-07-10 |
| `02-Funding/README.md` | Top hub doc, links everything below | 2026-07-09 (has stale figures, see Ledger B6-B7) |

### Area 2 — Previous applications

| Path | Purpose | Last commit |
|---|---|---|
| `02-Funding/submissions/INDEX.md` | Master submissions index | 2026-07-09 (**stale**, see Ledger B5) |
| `02-Funding/submissions/Applications/` (Anthropic, AWS, Biswas, CoefficientGiving x2, EA, ElevenLabs, Foresight, Lilly, YC) | Small grants / credits / accelerators, each with dated `archive/` | 2026-07-09, various |
| `02-Funding/submissions/Grants/ARPA-H/IGoR/` (full_proposal, solution_summary, research, partnerships, materials, figures) | Active flagship application; most recently touched grant in the repo | 2026-07-14/15 |
| `02-Funding/submissions/Grants/ARPA-H/HSF/ARPA-H_HSF_Solution_Summary.md` | Draft, secondary ARPA-H track | 2026-07-09 |
| `02-Funding/submissions/Grants/Google/` (working md + `original/all_materials/` submitted package + `original/archive/`) | Google.org Impact Challenge | 2026-07-09 |
| `02-Funding/submissions/Grants/NSF/X-labs/` (Phase 0 draft, SYNTHESIS.md, `materials/processed/` solicitation extraction) | NSF X-Labs / Psychoscope | 2026-07-09 |
| `02-Funding/YC/submissions/` (7 files: ARCHITECTURE, EVALUATION, LIMITATIONS, PROJECT_OVERVIEW, ROADMAP, SAFETY_AND_TRUST, VIDEO_STORYBOARD) | YC supporting content blocks (product-side), separate from the application form itself | 2026-07-09 |
| `02-Funding/submissions/_support/Human_Subjects_Readiness_FWA_IRB_SMART_2026-06-01.md` | Cross-grant human-subjects compliance status (North Star IRB, FWA #372195) | 2026-06-01/07-09 |

### Area 3 — Status / registry

| Path | Purpose | Last commit |
|---|---|---|
| `02-Funding/status/submission-registry.md` | **Canonical** funder-by-funder status table; explicitly supersedes `gdrive-funding-index.md` | 2026-07-15 |
| `02-Funding/status/component_status.md` | Pipeline/schema build-status matrix | 2026-07-09 (**stale figure**, see Ledger B6) |
| `02-Funding/architecture/pipeline_architecture.md` | End-to-end pipeline diagram | 2026-07-09 |
| `02-Funding/plans/implementation_plan.md` | Phased plan, status "Proposed" | 2026-07-09 |
| `02-Funding/testing/testing_strategy.md` | Testing plan, status "Proposed" | 2026-07-09 |
| `02-Funding/strategy/grant-alignment-map.md` + `_prompt.md` | Framing rule (technical + agent-brief variant) | 2026-07-09 |

### Area 4 — Funding opportunities

| Path | Purpose | Last commit |
|---|---|---|
| `02-Funding/INDEX_funding_opportunities_2026-06-12.md` | Root funding-opportunity index | 2026-07-09 |
| `02-Funding/Cytognosis_Strategy_and_Grant_Alignment_Map_2026-06-11.md` | Strategy/alignment map | 2026-07-09 |
| `02-Funding/_DRIVE_PLAN_Three_Grants_2026-06-12.md` | Active drive plan (verify title still matches current grant count) | 2026-07-09 |
| `02-Funding/grant-deep-research.md` | **Canonical** deep-research doc | 2026-07-09 |
| `02-Funding/NIMH_BRAIN_RFA-MH-26-140_summary_and_materials.md` | NIH TMM R01 vehicle | 2026-07-09 |
| `02-Funding/Compute_Credits_Applications_Anthropic_NAIRR_Cohere.md` | Compute-credit strategy | 2026-07-09 |
| `02-Funding/funding-opportunities/` (8 active files: Coefficient/EA research, Reprioritization, Individual Runway Shortlist, PAC Advocacy Companion, Verifiability-vs-CognitiveLiberty framing, NIH BRAIN/OneMind plan, dashboard html, funnel xlsx) | Funder-specific strategy docs | 2026-07-09 |
| `02-Funding/reusable-blocks/slot-library/research/profiles/` (71 files, incl. `aria-uk-full-programmes.md`, `aria-uk-opportunity-seeds.md`, `horizon-europe-cluster-1-health.md`, `wellcome-trust-discovery-awards.md`) | Full researched-opportunity set, including EU/UK (see Gap D3) | 2026-07-09 |

### Area 5 — Precision-psychiatry proposal materials

| Path | Purpose | Last commit |
|---|---|---|
| `02-Funding/submissions/astera/Astera_Round2_Response.md` | Astera Residency Round 2, Neuroverse framing | 2026-07-09 (**denied per memory; orphaned, see Ledger B3**) |
| `02-Funding/submissions/google-impact/Google_Impact_Revised.md` | Google.org Impact Challenge, "Revised v4," Neuroverse framing | 2026-07-09 (**orphaned, see Ledger B4**) |
| `02-Funding/submissions/Grants/Google/original/all_materials/` | The actual **submitted** Google.org package (md+docx) | 2026-07-09 |
| `02-Funding/reusable-blocks/slot-library/proposals/astera_2026/` | Slot-override worked example for Astera | 2026-07-09/07-15 |
| `02-Funding/NIMH_BRAIN_RFA-MH-26-140_summary_and_materials.md` | NIH precision-psychiatry RFA vehicle | 2026-07-09 |

No standalone precision-psychiatry **1-pager** exists separate from the two full narrative responses above (contrast with IGoR, which has a dedicated one-pager system). See Gap D5.

### Area 6 — Science / biotyping

| Path | Purpose | Last commit |
|---|---|---|
| `05-Research/foundational/disease-biotypes/diseases/BIOTYPES_CHEATSHEET_v2.md` | Biotyping quick reference | 2026-07-15 |
| `05-Research/foundational/disease-biotypes/molecular-cellular-biotypes.md` | Molecular/cellular biotype survey | 2026-07-09 |
| `05-Research/foundational/disease-biotypes/multiscale-biomarkers.md` | Multiscale biomarker survey | 2026-07-09 |
| `05-Research/foundational/dimensional/BDNF_TrkB_Neuroplasticity_Axes_Dossier_2026-06-03.md` | Keystone science: BDNF/TrkB dimensional axes (bipolar PoC) | 2026-07-09 |
| `05-Research/foundational/dimensional/psych-axes-synthesis.md` (+ ADHD companion in `dimensional/simple/`) | Dimensional-axes synthesis | 2026-07-09 |
| `05-Research/cytoverse/genomics/Genomic_Factorization_and_MultiTrait_PRS_Landscape_2026-06-07.md` | Factorized-PRS landscape (crown-jewel IP area) | 2026-07-09 |
| `05-Research/neuroverse/` (14 files: README, action-plan, datasets-cohorts, fmri-methods-review, infrastructure, master-dataset-curation, multimodal-coembedding x3, neurobehavioral-phenotype-feature-space x2, etc.) | Direct science backing for Astera/Google-Impact/Neuroverse proposals | 2026-07-09 |

---

## B) Duplicates and superseded ledger

| Path | Duplicate-of | MD5 match | Recommended action |
|---|---|---|---|
| `02-Funding/architecture/deep_research_report.md` | `02-Funding/grant-deep-research.md` | **No** (a613... vs 41e7...) — expected, because the file **already self-declares SUPERSEDED** and its current content is just a pointer stub, not the original text | Already handled correctly. No action. |
| `02-Funding/foresight/foresight-cytonome-2026-submit.md` (269 lines, dated 2026-06-14, **pre-reorg**) | `02-Funding/submissions/Applications/Foresight/Foresight_Cytonome_2026_SUBMIT.md` (263 lines, touched 2026-07-09 during reorg, has plaintext companion + own `archive/`) | Not tested (line counts differ) | Archive dated, keep the Applications/Foresight/ copy as canonical. |
| `02-Funding/submissions/astera/Astera_Round2_Response.md` | **N/A — no second copy exists anywhere.** Corrects the brief's hypothesis: there is no `Applications/Astera/` or `Grants/Astera/` "home." This is an orphan, not a true duplicate. | N/A | Astera was denied (per memory) and is **absent from `status/submission-registry.md`**. Archive dated; it is not tracked as active anywhere. |
| `02-Funding/submissions/google-impact/Google_Impact_Revised.md` (259 lines, "v4," 2026-07-09 15:02) | `02-Funding/submissions/Grants/Google/Google_org_Impact_Challenge_AI_for_Science.md` (257 lines, 07-09 22:50) **and** `Grants/Google/original/all_materials/...md` (256 lines, the actual **submitted** package, 07-09 22:50) | Not identical (line counts differ 259/257/256) | Google's real "home" is `Grants/Google/` (large-grant category), not `Applications/`. Do a 5-minute human diff first ("v4" naming suggests it may be a later, unmerged revision, not junk) before archiving. |
| `02-Funding/submissions/INDEX.md` (dated 2026-06-12; describes IGoR as versioned `v1/v2/v3` folders) | Superseded in practice by `status/submission-registry.md` (2026-07-15) and by the actual current IGoR folder layout (`full_proposal/`, `solution_summary/`, `research/`, `partnerships/`, `materials/`, `figures/`, no more v1/v2/v3) | N/A (structural, not byte-level) | Rewrite to match current structure, or add a "SUPERSEDED, see status/submission-registry.md" banner (same pattern already used on `gdrive-funding-index.md`). |
| `02-Funding/README.md` **and** `02-Funding/status/component_status.md` | Each other (both say "17 funder-profile files") | N/A | **Both wrong.** Actual count on disk is **10** (`slot-library/funders/*.yaml`). Neither file was touched in the 2026-07-15 refresh pass that fixed `slot-library/INDEX.md` (which correctly says "10 modeled"), `slot-library/README.md`, `funder_metadata.md`, and `submission-registry.md`. Fix the figure in both. |
| `02-Funding/README.md` source-code links (`../../src/cytos/scholarly/grants/*.py`) | N/A | N/A | **Broken path.** `src/cytos/scholarly/grants/` does not exist at that location; the sibling repo folder is `cytos/src/cytos/scholarly/` (one directory prefix different). Fix links or verify the code's real location before trusting the "Production" status claims in README/component_status. |
| `02-Funding/archive/Cytognosis_Status_Dashboard_2026-06-01.html` vs `02-Funding/_archive/opportunities-README.md` | Each other, structurally (two differently-named archive dirs at the same root level, one file each) | N/A | Consolidate to one `_archive/` naming convention (matches the underscore-prefix pattern already used inside IGoR). Move the dashboard html into `_archive/` with a dated subfolder. |
| `02-Funding/submissions/Grants/ARPA-H/IGoR/_consolidation_2026-06-19/` (8 process docs + notes/) | Superseded by current `full_proposal/` (C1-C4) and `solution_summary/`, exactly like the drafts already moved into `_archive/2026-07-14_harmonize/` | N/A | Same treatment: archive into a dated folder. This directory is the one piece of the 07-14 harmonize pass that got missed. |
| `02-Funding/submissions/Grants/ARPA-H/IGoR/PsychIGoR_Solution_Summary_SUBMISSION_2026-06-19_branded.docx` (loose at IGoR root) | Sibling files in `solution_summary/` | Not tested | Relocate into `solution_summary/` to colocate with its build system (build.py, sections/, template/). |

---

## C) Obsolete list (already archived correctly; no action needed, listed for completeness)

- `01-Strategy/archive/` — 5 files (FRESH_PROJECT_KICKOFF_PROMPT, MASTER_PLAN_AND_CONSOLIDATION_PROGRAM, STAGE1_ARCHIVE_TRIAGE, STAGE4_META_STRATEGY_TAXONOMY, cytomem_FIXES_FOR_ANTIGRAVITY), all 2026-06-03.
- `02-Funding/funding-opportunities/archive/` — 4 files (ACTION_TRACKER, Strategy_Master, compass_artifact export, funding_strategy_v2_update).
- `02-Funding/submissions/Applications/{Biswas,EA,Foresight,YC}/archive/` — prior-cycle drafts, correctly versioned away (YC alone has 2: Spring 2026, Winter 2025).
- `02-Funding/submissions/Grants/ARPA-H/IGoR/_archive/2026-07-14_harmonize/` — 21 files. **This is the best-practice model**: dated folder, `_archived-2026-07-14` suffix on every filename. Reuse this exact pattern for every other archive move in this doc.
- `02-Funding/submissions/Grants/Google/original/archive/` — 1 older draft, correctly archived.
- `02-Funding/reusable-blocks/raw-source/_ARCHIVED.md` — self-declared archived marker.
- `02-Funding/architecture/deep_research_report.md` — self-declared SUPERSEDED stub, pointer intact and correct.
- `02-Funding/submissions/astera/Astera_Round2_Response.md` — denied; not archived yet (see Ledger).

---

## D) Gaps

**D1. PsychIGoR "proposal_craft" materials — CONFIRMED MISSING.**
Memory references a 2026-06-23 package (`proposal_craft_2026-06-23/`: Heilmeier-to-healthcare guide, ARPA-H SS page-budget architecture, IGoR SS ISO-mapping punch-list). Checked and **not found** in: `02-Funding`, `01-Strategy`, `05-Research`, the `Claude/Projects/Grants` working folder, or a filename search of the Obsidian vault. No "16-block Heilmeier" library exists either (the slot system uses 27 U/A slots, of which U01-U08 map to Heilmeier core). Likely lost in an ephemeral session. Recommend checking Google Drive/chat history before rebuilding from `materials/markdown/APPENDIX_B_Solution_Summary_Format_and_Instructions.md` + `funders/heilmeier.yaml`.

**D2. Consolidated per-funder VALUES view — MISSING.**
No single document joins $-ask, fit-score (F10), insider-connection (F31), and live status in one row per funder. The pieces exist separately: status lives in `status/submission-registry.md`; scoring/connections live in `opportunity_mapping.yaml` (71 rows, machine-readable, not a human dashboard). Recommend generating one view by joining these two sources.

**D3. EU/UK opportunity rows + configs — PARTIAL.**
Rows exist: ARIA (UK) Full Programmes, ARIA (UK) Opportunity Seeds, Horizon Europe Cluster 1 Health, Wellcome Trust Discovery Awards, all present in `opportunity_mapping.yaml`/`.csv`/`_index.md` with full research profiles. **Configs do not exist**: all four show `canonical_funder_ref: null`, and none of the 10 `funders/*.yaml` files cover them. None of these four are on the current Active Funders priority list either, so this may be intentional deprioritization rather than an oversight worth fixing today.

**D4. Nonprofit-vs-for-profit eligibility tag — MISSING.**
No F-field (F01-F38) encodes organization-type eligibility. Closest proxies are F25 `residency_required`, F37 `academic_affiliation_required`, and a `nonprofit_discount` salary preset (compensation modeling only, not an eligibility gate). Separately: the YC funder-kind is literally named **`yc_nonprofit`**, which contradicts the actual strategy (YC S26 = for-profit PBC, per memory). Recommend adding an explicit `entity_type_eligibility` field and auditing the `yc_nonprofit` naming/logic.

**D5. Precision-psychiatry 1-pager — MISSING.**
Full narrative responses exist (Astera, Google Impact) but no short-form 1-pager, unlike IGoR which has a dedicated `partnerships/onepagers/` system. Worth building for warm-intro outreach (e.g., Smoller/Jordan per the network map).

---

## E) Recommended archive moves (checklist — NOT executed)

- [ ] Archive `submissions/astera/Astera_Round2_Response.md` to a dated `submissions/_archive/` folder (denied, untracked).
- [ ] Diff `submissions/google-impact/Google_Impact_Revised.md` against `Grants/Google/original/all_materials/` first, then archive whichever is not canonical.
- [ ] Archive `02-Funding/foresight/foresight-cytonome-2026-submit.md` (pre-reorg leftover; canonical copy lives in `Applications/Foresight/`).
- [ ] Consolidate `02-Funding/archive/` and `02-Funding/_archive/` into one `_archive/` convention.
- [ ] Archive `submissions/Grants/ARPA-H/IGoR/_consolidation_2026-06-19/` into IGoR's existing `_archive/` (same dated pattern as `2026-07-14_harmonize/`).
- [ ] Rewrite or banner-flag `submissions/INDEX.md` as superseded by `status/submission-registry.md`.
- [ ] Fix the "17 funder profiles" figure in both `02-Funding/README.md` and `status/component_status.md` (actual = 10).
- [ ] Fix broken source-code links in `02-Funding/README.md` (wrong relative path to the `cytos/` sibling repo).
- [ ] Relocate the loose `PsychIGoR_Solution_Summary_SUBMISSION_2026-06-19_branded.docx` into IGoR's `solution_summary/`.
- [ ] Decide whether to rebuild the missing `proposal_craft` Heilmeier/page-budget guide (Gap D1), after checking Drive/chat history.

---

## Notes on scope

- **Branch**: repo was on `main`, not `reorg/universal-taxonomy-2026-06-12` as the project CLAUDE.md states. Worth confirming whether that branch already merged.
- **Google Drive index**: read `02-Funding/gdrive-funding-index.md` per instructions (not crawled). It is dated 2026-06-14 and is **explicitly superseded** by `status/submission-registry.md`'s own text for status purposes; its Drive-URL mapping content may still be useful but its referenced docs-repo paths (`01-strategy/funding/...` lowercase) predate the current `01-Strategy` structure.
- **Obsidian vault**: only a filename-level check was run (per "note only" instructions), specifically for `proposal_craft`. No hits. Deeper vault content was not read.
- **05-Research**: `foundational/` alone holds 152 files; only the canonical/master documents directly fed into proposals are listed in Area 6. The remainder (disease-specific deep dives, connectomics, behavioral instruments) was not individually classified, consistent with "grant-relevant only" scoping.
- Everything in this document was read, not changed. No files were moved, archived, or deleted.
