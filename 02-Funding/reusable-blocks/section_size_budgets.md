# Section Size Budgets

> **Status**: Active
> **Date**: 2026-07-16
> **Author**: Shahin Mohammadi
> **Tags**: `funding`, `slot-library`

## BLUF

**ARPA-H Mission Office Solution Summary is the best-sourced precedent: official limit is 6 pages** (verified twice, from two different template sources), with an internal 5-page working budget and a 2,300-word, 7-part Heilmeier breakdown that the shipped PsychIGoR SS matched closely (2,354 realized words). Most other funders publish an artifact-level page limit only, with **no official per-section split**; those get the reusable default proportion guideline below and are marked TBD until we verify against the live solicitation. This file recovers the PsychIGoR page-budget work that was lost after the reorg.

---

## 1. Important correction: the "5 pages" figure

Two independent, verified source documents state the **official ARPA-H Mission Office ISO Solution Summary limit is six (6) pages**, not five:

- `DOCS/02-Funding/reusable-blocks/raw-source/arpah_appendix_a_solution_summary.md`: "Solution Summaries have a limit of **six (6) pages**. Citations do not count toward the six-page limit."
- `cytos/data/staged/grants/arpah/templates/arpah_solution_summary_template.yaml` (Amend-2, machine-readable): `page_limit: 6`, exclusions = `citations`, `cover_page`, `sub_awardee_table`.
- `cytos/data/staged/grants/arpah/programs/evident/ta1_3/appendix_a_-_solutions_summary_template_v2.md` (EVIDENT TA1-3): "Solution Summaries are limited to six pages, exclusive of a cover page and References."

The **"5 pages" figure is an internal working budget**, not a solicitation rule. It appears in two places:
- `DOCS/02-Funding/reusable-blocks/slot-library/funders/arpah_mission_office.yaml` sets `page_limit: 5` on the `appendix_a` artifact (a deliberate buffer under the real 6-page cap).
- The shipped submission doc itself (`IGoR_Solution_Summary_SUBMISSION_2026-06-19.md`, line 10) states as a build target: "Sections 1 to 4 fit within 5 pages; cover/profile, Section 5 (BOE), and Section 6 (References) are excluded from the page limit."

**Recommendation:** keep using 5 pages as our internal drafting target (safety margin), but cite 6 pages as the verified solicitation limit whenever a compliance question comes up.

---

## 2. Master per-funder table

| Funder | Artifact | Total limit | Included slots | Per-slot size budget | Source / verified |
|---|---|---|---|---|---|
| ARPA-H Mission Office ISO | Solution Summary (Appendix A) | **6 pages** official (5 pages internal target) | U01-U08, U09.1, U11, U13, U14, U16, U17 (see Section 3) | See Section 3 word-budget table (2,300 words / 7 headings) | Verified, 3 source docs agree on 6 pages |
| ARPA-H Mission Office ISO | Full Technical & Management Proposal | 20 pages | U01-U04, U07, U08, U11, U17-U20 | Not sub-divided in solicitation | Verified page limit (`arpah_mission_office.yaml`); per-section split TBD verify from solicitation |
| ARPA-H Mission Office ISO | Technology Development Document (TDD) | No stated page limit | U15, U16, U18.3, U20.2 | TBD verify from solicitation | Page limit not found in raw-source or staged templates |
| ARPA-H Mission Office ISO | Cost Proposal | N/A (xlsx, 9 sections) | U06, A01, A03, U16.2-.3 | N/A (spreadsheet, not page-gated) | Verified format from `arpah_mission_office.yaml` |
| NIH R01 | Specific Aims | **1 page** | U01, U04, U08.1 | Whole page, no sub-split (NIH convention) | Verified, standard NIH page limit, confirmed in `nih_r01.yaml` |
| NIH R01 | Research Strategy | **12 pages** | Significance (U02, U04), Innovation (U03.1, U03.3), Approach (U03.2/.4/.5, U05, U07, U08) | Convention: roughly 1p Significance, 1p Innovation, 10p Approach; not in our files | `nih_r01.yaml` notes this is "guessed from framework_catalog," page limit reflects FY2026 standard, re-verify before use |
| NSF Tech Labs | RFI Response | **10 pages** | Q1-Q7 (org overview through meta-feedback) | Not sub-divided; 15 sub-questions across 10 pages implies roughly 0.65 pages/question average | `nsf_tech_labs.yaml` notes structure is "guessed", TBD verify against live RFI text |
| DOE Genesis Mission | Project Abstract | **1 page** | U01, U04.1, U04.3 | Whole page | Verified in `doe_genesis.yaml` |
| DOE Genesis Mission | Project Narrative | **15 pages** | Section1 Significance, Section2 Innovation/Approach, Section3 Technical Approach & Milestones, Section4 Team, Section5 Go/No-Go, Section6 Risk | Not sub-divided per section | Verified page limit in `doe_genesis.yaml`; per-section split TBD verify from solicitation |
| DOE Genesis Mission | Data Management Plan | **2 pages** | U12.1-.5, U15.3 | Whole allotment | Verified in `doe_genesis.yaml` |
| Astera Residency | Application (web form) | No page limit; **Q1 capped at 300 characters** | Q1-Q8 | Q1 = 300 chars (verified, `astera_residency.yaml`); Q2-Q8 open text, TBD verify from live form | Partially verified (char cap only) |
| Brains Accelerator | Application (web form) | TBD verify from solicitation | B1-B7, Program Leadership Readiness, Vision for Impact, References | TBD, no char/word caps recorded in `brains_accelerator.yaml` | Not verified |
| Foresight Nodes | Application (web form) | No page limit; **F15 "bold thesis" capped at 350 characters** | F1-F39 | F15 = 350 chars (verified, `foresight_nodes.yaml`); other fields TBD verify from live form | Partially verified (char cap only) |
| Google.org AI Impact Challenge | Online Application Form | TBD verify from solicitation | Q1-Q53 (16 grouped sections) | TBD, no char/word caps recorded in `google_impact_challenge.yaml` | Not verified |
| YC Nonprofit | Application (web form) | No page limit; **YC9 "tagline" capped at 50 characters** | YC1-YC38 | YC9 = 50 chars (verified, `yc_nonprofit.yaml`); other fields TBD verify from live form | Partially verified (char cap only) |
| Heilmeier Catechism | Internal Narrative (baseline, not a real funder) | No limit (internal review format) | Q1-Q8 (= U01-U08) | `word_limit: null`, deliberately unconstrained | N/A, internal baseline, not a submission artifact |

---

## 3. ARPA-H Mission Office Solution Summary, internal word budget (7-heading Heilmeier breakdown)

This is the internal slot-planning budget from `slot-library/funders/arpah_mission_office.yaml`, used to plan content before drafting into the 5 official template sections (Concept Summary / Innovation and Impact / Proposed Work / Team Org / BOE).

| # | Heading (internal Heilmeier label) | Slots | Word budget | % of 2,300-word total |
|---|---|---|---:|---:|
| 1 | Program fit, what are you trying to do? | U01, U09.1 | 400 | 17.4% |
| 2 | How is it done today, and what are the limits of current practice? | U02 | 400 | 17.4% |
| 3 | What is new, and what are the quantitative metrics? | U03, U08.1 | 500 | 21.7% |
| 4 | Who cares? If successful, what difference will it make? | U04, U13.1, U13.2, U17.1, U17.4 | 300 | 13.0% |
| 5 | Risks | U05, U14.2, U16.1, U16.6 | 300 | 13.0% |
| 6 | Team / key personnel | U11.1, U11.2, U11.4 | 200 | 8.7% |
| 7 | Budget synopsis | U06.1, U06.2 | 200 | 8.7% |
| | **Total** | | **2,300** | **100%** |

**Note on structure:** these 7 headings are an internal Heilmeier-question relabeling used for slot planning; they are not the literal headers in the official template, which has 5 numbered sections (Concept Summary, Innovation and Impact, Proposed Work, Team Organization and Capabilities, Basis of Estimate). Map heading 1 into Concept Summary; headings 2-3 mostly into Innovation and Impact; heading 3 (metrics/approach) and elements of 4-5 into Proposed Work; heading 6 into Team Org; heading 7 into the BOE narrative lead-in.

---

## 4. Realized PsychIGoR Solution Summary, actual word counts (2026-06-19 submission)

Pulled directly from `IGoR_Solution_Summary_SUBMISSION_2026-06-19.md` (sections 1-4 only; cover, BOE, and References are excluded from the page limit per the doc's own build note):

| Official section | Realized words | % of realized total (2,354 words) |
|---|---:|---:|
| 1. Concept Summary | 262 | 11.1% |
| 2. Innovation and Impact | 704 | 29.9% |
| 3. Proposed Work | 982 | 41.7% |
| 4. Team Organization and Capabilities | 406 | 17.2% |
| **Total (sections 1-4)** | **2,354** | **100%** |

**Validation:** the realized total (2,354 words) lands almost exactly on the internal 2,300-word budget from Section 3, confirming the budget was a workable target. The realized split skews more weight into "Proposed Work" (41.7% vs. an implied ~35-40% under the 7-heading mapping) and less into Concept Summary, consistent with ARPA-H reviewers wanting depth on technical approach over scene-setting. **Use the Section 3 proportions as the starting allocation, then shift 5-8 points from Concept Summary toward Proposed Work** if the technical approach needs more room.

---

## 5. Default proportion guideline, reusable for any 5-page Heilmeier-style Solution Summary

For a new 5-page Heilmeier-style SS (any funder, when no official per-section split exists), start from the ARPA-H-derived proportions and round to clean planning numbers:

| Content block | Heilmeier question(s) | Target share of page budget | Pages (of 5) |
|---|---|---:|---:|
| Concept / program fit | Q1 | ~15% | 0.75 |
| State of the art & limits | Q2 | ~15% | 0.75 |
| Novelty + quantitative metrics | Q3 | ~25% | 1.25 |
| Who cares / impact | Q4 | ~13% | 0.65 |
| Risks | Q5 | ~13% | 0.65 |
| Team / key personnel | (extension) | ~9% | 0.45 |
| Budget synopsis | Q6 (light touch) | ~9% | 0.45 |
| **Total** | | **~100%** | **~5.0** |

This guideline is a starting allocation, not a rule; adjust per funder emphasis (for example, Foresight Nodes weights safety/differential risk more heavily; Google.org weights beneficiaries/equity and measurement more heavily; see `funder_values_view.md` for per-funder emphasis).

---

## 6. Open TBDs (verify before next use)

- NIH R01 Research Strategy per-section split (Significance/Innovation/Approach) inside the 12-page limit; no official split on file, `nih_r01.yaml` self-flags this as "guessed."
- NSF Tech Labs per-question length inside the 10-page RFI response; self-flagged as "guessed" in `nsf_tech_labs.yaml`.
- DOE Genesis Project Narrative per-section split inside 15 pages; page limit is verified, sub-split is not.
- Brains Accelerator and Google.org Impact Challenge; no page/word/char caps recorded anywhere in the slot library, both need a live-form check.
- ARPA-H TDD and Cost Proposal; no page limit found, likely uncapped or capped only by practicality (xlsx / narrative-lite).
