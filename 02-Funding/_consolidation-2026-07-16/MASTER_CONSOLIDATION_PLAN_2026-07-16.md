# Master Consolidation Plan — Grants & Applications

> **Status:** Active (living plan) · **Date:** 2026-07-16 · **Author:** Shahin Mohammadi (with Claude) · **Audience:** Shahin, grant team · **Tags:** `funding`, `grants`, `consolidation`, `standardization`
> **Variants:** Technical (this doc) · Readable twin (to generate in vault) · Agent (dispatch orders in §9)

## TL;DR (BLUF)

Your grant standardization system is **already ~90% built and mature** (slot-library v1.2 in `docs/02-Funding/reusable-blocks/`), so this program is **verify, reconcile, and finish**, not build from scratch. The stale pieces are the **submission statuses** (registry is dated Jul 1; five decisions have landed since) and three real gaps: **section-size budgets**, a **consolidated per-funder "values" view**, and **EU/UK eligibility + entity strategy**. After those, the payoff is the **precision-psychiatry proposal** (1-pager → Solution Summary → full) for ARPA-H Mission Office ISO and Convergent Research, plus the Jordan Smoller lead-ask 1-pager.

**If you only read one thing:** the phase table in §3 and the reconciled status snapshot in §5.

**Reading time:** ~9 minutes full; ~90 seconds for §3 + §5.

---

## ✅ Already done (so you can see the ground you stand on)

- **Standardization spine built:** 27 slots (Heilmeier U01-U08 + extensions U09-U22 + admin A01-A05), each a real file in `slot-library/slots/`.
- **Funder-metadata schema built:** 38 fields (F01-F38) covering category, stage, deadline, eligibility, review mechanism, strategic connections, sub-programs, and Heilmeier-required flag.
- **Funder-kind engine built:** `funder_kinds` maps each funder type to a slot subset (heavy / medium / light).
- **71 opportunities mapped:** `opportunity_mapping.{yaml,csv}` + 71 research profiles + Monday-loadable CSV.
- **Framework catalog built (18 rubrics):** incl. Heilmeier, NIH R01, NSF, ARPA-H SS, **ARIA (UK)**, **Horizon Europe**, Convergent FRO, YC, Wellcome Leap, SBIR/STTR.
- **10 funder build-configs written:** ARPA-H Mission Office, NIH R01, NSF Tech Labs, DOE Genesis, Astera, Brains, Foresight, Google Impact, YC, Heilmeier.
- **Submissions already foldered:** `submissions/Applications/` and `submissions/Grants/` per funder.
- **IGoR harmonized** to one canonical home (separate plan, `IGoR-CONSOLIDATION-PLAN_2026-07-12.md`), driving to the **Aug 13** full-proposal deadline.
- **Cytos CLI hook exists:** `cytos funding parse --criticmarkup`.

---

## 1. Where everything lives (ground truth, verified 2026-07-16)

| Layer | Location | Contents |
|---|---|---|
| **Canonical docs repo** | `~/repos/cytognosis/docs` (host `cytognosis`, branch `main`) | The source of record for all funding work |
| Standardization layer | `docs/02-Funding/reusable-blocks/` | `canonical_template_format.md` (spec), `universal_template.md`, `framework_catalog.md`, `funder_crosswalk_matrix.md`, `funder_metadata.md`, `slot-library/` |
| Slot library | `.../reusable-blocks/slot-library/` | `slots/` (27), `funders/` (10 yaml), `manifest.yaml` (v1.2), `groups.yaml`, `opportunity_mapping.{yaml,csv}`, `research/profiles/` (71) |
| Funding opportunities research | `docs/02-Funding/funding-opportunities/` | Dashboards, funnel xlsx, reprioritization, Coefficient/EA research, NIH/OneMind plan |
| Submissions (the applications) | `docs/02-Funding/submissions/` | `Applications/` (AWS, Anthropic, Biswas, CoefficientGiving, EA, ElevenLabs, Foresight, Lilly, YC) + `Grants/` (ARPA-H/{HSF,IGoR,outreach}, Google, NSF/X-labs) |
| Status tracking | `docs/02-Funding/status/` | `submission-registry.md` (STALE, dated Jul 1), `component_status.md` |
| Pipeline architecture / automation | `docs/02-Funding/architecture/`, `.../plans/`, `.../testing/` | Pipeline design + implementation + testing strategy |
| Working / active drafts | `~/Claude/Projects/Grants/` (this project) | Thin shortcut layer via `_context/` → docs repo; plans + drafts |
| Google Drive / Docs | Drive `Funding/…`; live Google Docs | Official appendices, submitted PDFs, hand-edited IGoR docs |
| Obsidian vault | `~/Documents/ObsidianVault` | Readable twins; docs-repo symlink |
| Live memory | cytomem (Neo4j) | System of record for facts/decisions |

**Two consolidation working files (this session):** `00_PRIOR_WORK_SYNTHESIS.md` (prior chats) and `01_ASSET_INVENTORY.md` (full classification, complete; corrections below), both in `Grants/_consolidation-2026-07-16/`.

### 1.1 Phase 1 inventory corrections (apply during execution)

| Finding | Detail | Fix in phase |
|---|---|---|
| **3 orphan duplicates** | `submissions/astera/Astera_Round2_Response.md` (true orphan; Astera denied); `submissions/google-impact/Google_Impact_Revised.md` (canonical home = `submissions/Grants/Google/original/all_materials/`); `02-Funding/foresight/foresight-cytonome-2026-submit.md` (canonical = `submissions/Applications/Foresight/`) | 3 (fold + archive dated) |
| **Funder-count bug** | `02-Funding/README.md` and `status/component_status.md` say **17** funder profiles; actual is **10** (`slot-library/INDEX.md` already fixed 2026-07-15) | 4a |
| **Naming bug** | funder-kind/config `yc_nonprofit`, but **YC S26 is a for-profit PBC**; relabel | 4a |
| **Broken links** | `02-Funding/README.md` code links (`../../src/cytos/...`) do not resolve; real code is in the sibling `cytos/` repo | 4e |
| **Missing (confirmed)** | the 2026-06-23 PsychIGoR `proposal_craft` page-budget/Heilmeier guide is absent from repo, Grants, and Obsidian; recover from Google Drive/Docs or reconstruct | 4c |
| **EU/UK config gap** | ARIA (x2), Horizon Europe, Wellcome Trust have research rows but `canonical_funder_ref: null`; no build-configs | 6c |
| **No precision-psych 1-pager** | only full narrative responses exist; none standalone | 7 |
| **Branch drift** | repo is on `main` (reorg branch merged); project `CLAUDE.md` still cites `reorg/universal-taxonomy-2026-06-12` | 3 (update) |
| **Best-practice model** | `submissions/Grants/ARPA-H/IGoR/_archive/2026-07-14_harmonize/` is the archive pattern to replicate for every other funder | 3 |

---

## 2. Coverage map (your request → where it is handled → state)

| Your requested item | Phase | State today |
|---|---|---|
| Schemas/templates; map questions to standard format; Heilmeier; IGoR SS→questions | 4 (Standardization) | **Exists**; verify + extend |
| Standardize "values" + infer relevant values per funder | 4 | **Partial** (crosswalk + F-fields); consolidate into one view |
| Separate templates from content (reusable proposal builder; Cytos; Yar lineage) | 4 | **Exists** (slots vs funder configs vs proposals); document |
| Section proportions/sizes per application (from PsychIGoR SS) | 4 | **Gap**; recover + encode length budgets |
| Previous apps: status, Google Doc link, final markdown, scope→platform, Q→framework | 5 | **Partial**; per-app record schema + fill |
| Status updates + rejection/pending emails | 5 (snapshot in §5) | **Reconciled below**; rebuild registry |
| Funding research consolidation (deadlines, eligibility, stage, amount, values, priority, links) | 6 | **Exists** (71-opp map); refresh + verify |
| EU/UK extension + nonprofit vs for-profit + Madhvi vs UK/EU branch | 6 | **Partial**; add axes + entity memo |
| Guide which to prep next (ARPA-H MO ISO, Convergent, Smoller 1-pager, ARPA-H PD) | 6 → 7 | Prioritized output |
| Precision-psych 1-pager / SS / full proposal (team, gaps, solutions) | 7 | **Build** |
| Unsorted science / biotypes / deliverable figure | 8 | **Build** dossier (2 variants) |

---

## 3. Phases at a glance (the backbone)

| Phase | Name | Output | Depends on | Mode |
|---|---|---|---|---|
| **0** | Setup | Prior-work synthesis + ground truth + this plan | — | ✅ done this session |
| **1** | Discover & classify (read-only) | `01_ASSET_INVENTORY.md`: canonical / duplicate / obsolete + dedup ledger + gaps | 0 | 🔄 running (subagent) |
| **2** | Verify & backup | Validation run + git tag `pre-grants-consolidation-2026-07-16`; false-"done" audit | 1 | main thread |
| **3** | Taxonomy freeze | Confirm canonical grants taxonomy (generalize IGoR model); naming + archive rules | 1-2 | main thread |
| **4** | Standardization: finish | Sizes + values complete; system v1.3; builder + Cytos documented | 2-3 | subagents + synth |
| **5** | Previous applications: consolidate | Per-app records (status, Doc link, FINAL.md, scope-map, Q-map); registry rebuilt | 3-4 | subagents |
| **6** | Funding opps: refresh + extend | 71-opp map refreshed + verified; EU/UK added; entity memo; priority "prep-next" list | 4 | subagents + web |
| **7** | Precision-psych proposal | 1-pager → SS → full for ARPA-H MO ISO + Convergent; Smoller lead-ask 1-pager | 4-6 | synth (Opus/main) |
| **8** | Biotyping / science dossier | 2 variants (ND-friendly + grant/review); universal dimensional map figure | 4 | subagents + synth |

Rule of thumb: **Phases 1-6 make the machine trustworthy and current; Phases 7-8 use it to win the psychiatry funding.**

---

## 4. Phase 4 — Standardization: verify, reconcile, complete

**BLUF:** The system is mature; close four items and cut v1.3.

- **4a. Validate integrity.** Run the slot-library's own validation (`manifest.yaml` → `validation:` rules): all 27 slot files resolve, all 10 funder configs resolve, ID formats pass. Fix any broken hooks.
- **4b. Resolve the "16-block Heilmeier" question.** The prior 16-block library appears to have already become U01-U22. Confirm on disk (Phase 1), archive any stray copy dated, leave a RELOCATED pointer. Do **not** maintain two libraries.
- **4c. Populate section-size budgets (the real gap).** Recover the PsychIGoR page-budget work (`proposal_craft_2026-06-23`, not in repo — search Drive + IGoR submission folder first). Encode per-funder, per-slot length budgets into each `funders/*.yaml` (the `length_enforcement` engine already exists; it just needs the numbers) plus a human-readable **section-proportion table** (which sections are included, and target size, per application type). ARPA-H SS 5-page budget is the seed.
- **4d. Consolidate the per-funder "values" view.** Merge `funder_crosswalk_matrix.md` + `funder_metadata.md` + F07 (focus areas) + F10 (mission alignment) + F29 (review criteria) + F33 (thematic tags) + F38 (score rationale) into **one canonical "what this funder values, and which slots to emphasize" view** per funder. This is the "infer the most relevant values to address" deliverable.
- **4e. Document the reusable proposal builder.** One short doc: slots (reusable content) vs funder configs (selection + order + sizes) vs assembled proposals (outputs), plus the `cytos funding parse` render workflow. Note the lineage to the earlier personal-app/Yar "reusable building" feature so the design intent is on record.

**Output:** standardization system **v1.3** (sizes + values complete, validated), CHANGELOG bumped.

---

## 5. Phase 5 — Previous applications: reconciled status (as of 2026-07-16)

**BLUF:** The registry is stale. Below is the corrected snapshot; Phase 5 rebuilds `submission-registry.md` from it and gives every application a full canonical record.

### 5.1 Status snapshot (verified against your Jul 12-16 updates)

| Program | Recipient / scope | Applied | Status (2026-07-16) | Next / note |
|---|---|---|---|---|
| **ARPA-H IGoR (PsychIGoR)** | Org (Purdue-IPAI prime) | SS Jun 25 | **Pending / Active** | Full proposal **due Aug 13** (own plan) |
| **Google.org Impact: AI for Science** | Org | May 1 | **Pending** | Invitation-only next stage, rolling |
| **Foresight AI for Science & Safety Nodes** | Org | Resubmitted May 31 | **Pending (2nd round)** | R1 declined Apr 14; R2 live |
| NSF X-Labs (Psychoscope) | Org | — | **Missed** (deadline Jul 13) | Herve non-response; re-plan next cycle |
| Grand Challenge: Aging Reimagined (Lilly-Nucleate) | Org | — | **Missed** | Deadline lapsed |
| AWS Imagine | Org (credits) | R1 submitted | **Rejected** Jul 13 | Recipients announced Dec 2026; reapply next year |
| Biswas Fast Grant | Org | Jun 12 | **Rejected** Jul 1 | Reapply window **Dec 16, 2026** |
| Coefficient Career Development & Transition | Individual | Jun 12 | **Rejected** Jul 12 | — |
| Google for Startups Cloud | Org (credits) | May 7 | **Rejected** May 11 | Nonprofit ineligibility after call |
| NVIDIA Inception | Org (credits) | — | **Rejected** (prior) | — |
| qb3 mentorship | Org | — | **Rejected** (prior) | — |
| Coefficient Capacity Building | Org (~$175K) | — | **Verify** | Near-final; confirm not bundled into the CDT rejection |
| EA LTFF | Individual/org (~$75-125K) | — | Near-final (to submit) | Rolling |
| Manifund | Org/individual ($15-30K) | — | No draft | Rolling |
| YC Summer 2026 | PBC | — | Parked | Until Yar is further along |
| ARPA-H HSF / EVIDENT | Org | — | Draft | Rolling |
| NIH TMM (RFA-MH-26-140) | via Purdue/Grama | — | Planned | Oct 2026 cycle |
| Compute credits (Anthropic AI for Science, NAIRR, Cohere) | Org | — | Materials | Verify each; Anthropic "AI for Science" folder = confirm vs Claude Corps |
| ElevenLabs | Org | — | **Verify** | Folder exists, status unknown |

**Decisions I made here (flagged):** Foresight is **Pending (2nd round)**, not declined. Google for Startups Cloud added as **Rejected**. Coefficient **Capacity Building** and **ElevenLabs** and the **Anthropic AI for Science** item are marked **Verify** (I will confirm via Gmail in Phase 5 rather than guess).

### 5.2 Per-application canonical record (schema to fill for each)

Each application folder gets an `INDEX.md` with exactly these fields:

1. **Status** (from 5.1) + decision date + source email/link.
2. **Final Google Doc link(s)** (and note if hand-edited-only, e.g. IGoR).
3. **Final application as `FINAL.md`** (frozen markdown of what was actually submitted).
4. **Scope / proposed solution** = which subset of the Cytognosis platform + neuro application this bid maps to (Cytoverse / Cytoscope / Cytonome-Yar / Neuroverse / Brainscope).
5. **Question → slot map** (funder questions mapped to U/A slots; for submitted apps this largely exists, extend where missing).

Fold the duplicate `submissions/astera/` and `submissions/google-impact/` (repo root) into their `Applications/…` homes; archive dated, never delete.

---

## 6. Phase 6 — Funding opportunities: refresh, extend, prioritize

**BLUF:** Refresh the 71-opp map to today's truth, add the eligibility/entity axes, extend EU/UK, then output a ranked "prep these next" list.

- **6a. Refresh + verify.** Update deadlines, amounts, stage, priority, links across the 71; **web-search-verify every near-term deadline** before asserting (registry itself warns on this).
- **6b. Add eligibility axes to every opportunity.** Two axes, using existing F-fields: **nonprofit vs for-profit eligible** (extend F04/F16), and **US-lead vs requires-UK/EU-lead** (F25/F30/F37 + a new tag). This directly answers "which allow nonprofit vs for-profit."
- **6c. Extend EU/UK.** Add opportunity rows + build-configs for ARIA, Wellcome Trust, Wellcome Leap, UKRI, Horizon Europe, and peers. Frameworks already exist in `framework_catalog.md` (ARIA §5, Horizon Europe §6); this is data + configs, not new research from zero.
- **6d. Entity strategy memo (decision).** Resolve **Madhvi-as-UK/EU-partner vs incorporating a Cytognosis UK/EU branch.** Pull Madhvi's role from `01-Strategy` people/planning docs; assess per-funder whether a partner suffices (US-nonprofit-lead programs: ARIA, Wellcome Leap) vs where a UK/EU legal entity or UK/EU lead is required (Wellcome Trust, UKRI, Horizon Europe). Output a one-page recommendation, flagged for counsel (Duane) on entity mechanics.
- **6e. Extract + map questions for the next priority funders.** For **ARPA-H Mission Office ISO** and **Convergent Research FRO**, gather the live application questions (web + files) and map to slots (feeds Phase 7).

**Output:** refreshed `opportunity_mapping.{yaml,csv}` (+ Monday sync), EU/UK rows + configs, entity memo, and a **priority-ranked prep list** headed by ARPA-H MO ISO + Convergent.

---

## 7. Phase 7 — Precision-psychiatry proposal (the payoff)

**BLUF:** Assemble the 1-pager → Solution Summary → full proposal from the standardized slots, sized and values-tuned per Phases 4/6, for **ARPA-H Mission Office ISO** and **Convergent Research**, plus a **Jordan Smoller lead-ask 1-pager** and an **ARPA-H program-director** outreach 1-pager.

Section build (each drawn from slots + the Phase 8 dossier):

- **Team (U11 + A01/A02).** Shahin's dual identity as **patient + founder**, industry + academia track record, revised CV/biosketch. Public members: long + short + website bios. Use `[rate pending comp finalization]`, never a salary figure.
- **Gaps (U02/U04/U09).** Consolidated general healthcare gaps (treating symptoms not cause; missing trajectory; too late) + neuro-specific gaps (no objective psychiatric diagnostics; masked within-diagnosis heterogeneity; GxE/exposome; ignored dimensional + transdiagnostic structure; treatment failure/resistance) + biotypes across scales + personalized treatment (traditional meds, neuroplastogens, neuromodulation/EVIDENT, plus the recent personalized-lifestyle-trial evidence).
- **Solution (U01/U03/U17/U18).** Platform (Cytognosis general) → Neuro: **Yar**, **Neuroverse**, **Brainscope (with Herve)**; the "digital psychiatric twin" causal-RL framing.

Guardrail: **IGoR Google docs are hand-edited by Shahin — do not touch them programmatically.** This precision-psych proposal is a **distinct submission** (ARPA-H Mission Office ISO ≠ IGoR SOL-26-155); build it in its own home.

---

## 8. Phase 8 — Biotyping / science dossier (feeds Phase 7)

**BLUF:** Consolidate all biotyping research into two variants and produce the signature figure.

- **Consolidate** all scales (molecular/cellular/connectomic/phenotypic), all disorders, nodes **and** edges/subgraphs (connectomics), plus recent inputs (ADHD + depression papers from Jul 11; Stanford biotypes page; ADHD-DSM blog).
- **Two variants:** (1) **educational / ND-friendly** (neuroanatomy, diagrams, tables, simplified) for you; (2) **grant / review-ready** (formal specs, publishable) toward a future review paper.
- **Signature deliverable:** the **universal dimensional map of the human psyche** figure — MDD, BD, SZ (± PTSD, anxiety/autism), phenotypes of the 3-5 leading genomic factors aligned to DSM cross-cutting + HiTOP, with treatments layered by micro (molecular/cellular, incl. neuroplastogens/EVIDENT), meso (connectomic nodes like dlPFC, edges like SAINT, subgraphs like default-mode), and macro (phenotypic/cross-trial) effects.

---

## 9. Dispatch orders (copy-paste ready, max 2 parallel Sonnet subagents)

- **Phase 1 (running):** "Inventory and classify every grant/application/funding asset in `~/repos/cytognosis/docs/02-Funding` (+ grant-relevant `01-Strategy`, `05-Research`); mark canonical/duplicate/superseded/obsolete, detect dupes (md5 for identical), list gaps; READ-ONLY; save `01_ASSET_INVENTORY.md`."
- **Phase 4:** two subagents — (A) validate slot-library + resolve 16-block question + recover PsychIGoR sizes; (B) consolidate per-funder values view.
- **Phase 6:** two subagents — (A) refresh + web-verify the 71 opps + eligibility axes; (B) EU/UK extension + entity memo.
- **Phase 8:** two subagents — (A) molecular/cellular + genomic-factor biotypes; (B) connectomic (node/edge/subgraph) + treatment-mapping.
- **Synthesis (Phases 3, 4e, 7, entity memo):** main thread / Opus.

---

## 10. Guardrails (non-negotiable)

- **Backup before any move:** git tag `pre-grants-consolidation-2026-07-16` before Phase 3+; commit in logical chunks as **Shahin Mohammadi <mohammadi@cytognosis.org>**; visible heads-up before any mass move or history rewrite.
- **Archive over delete; never delete unique content;** hash (md5) before removing any duplicate.
- **Verify against ground truth; trust nothing marked "done"** without disk/Gmail/web confirmation (documented false-"done" pattern in prior program).
- **Do not touch the IGoR Google Docs programmatically** (Shahin hand-edits).
- **No PI salary figure** anywhere; use `[rate pending comp finalization]`. **No private dollar target;** frame impact as lives / life-years, not money.
- **Voice:** authoritative, compassionate, optimistic; never "revolutionary", "breakthrough", "cure", or fear-based. Never the word "Substrate" (use layer/foundation). CAP is **Cytoplex**. **Neuroverse** is the settled neuro-FM brand; keep the flagship brand off small disease-specific pilots.
- **ADHD-friendly twins** for key docs (readable version in the vault).

---

## 11. Open decisions (only three; recommendations given)

1. **Where does this consolidation output live?** → *Recommendation:* build in `Grants/_consolidation-2026-07-16/`, promote finished canonical docs into `docs/02-Funding/` (matches the project's own "working here, canonical in docs home" rule). Proceeding on this unless told otherwise.
2. **Entity strategy (Madhvi vs UK/EU branch)** → decided in Phase 6d as a memo; the *choice* is yours + counsel, I will give a recommendation with rationale, not leave it open.
3. **Verify-flagged statuses** (Coefficient Capacity Building, ElevenLabs, Anthropic AI for Science) → I will confirm via Gmail in Phase 5; no decision needed from you.

---

## 12. Immediate next actions (once you say go)

1. Finish Phase 1 inventory (subagent running); read its `01_ASSET_INVENTORY.md`.
2. Phase 2 backup + validation + false-"done" audit.
3. Rebuild `submission-registry.md` from §5.1 (safe, git-tracked) — the single highest-value quick win.
4. Then proceed Phases 3 → 8 autonomously, reporting at each phase boundary.
