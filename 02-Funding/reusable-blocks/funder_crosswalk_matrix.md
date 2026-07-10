# Funder Crosswalk Matrix

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: leadership, grant team
> **Tags**: `funding`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

**Status:** Authoritative reference. Pairs every funder question with its universal slot(s) and every universal slot with its funder obligations.
**Purpose:** Reverse rendering — given a funder, know which slots to assemble; given a slot, know which funders will consume it.
**Source of truth:** `canonical/funders/*.yaml` (forward) and `canonical/slots/*.md` frontmatter `funder_hooks` (forward). This file is the reader-friendly aggregation.
**Version:** 1.0 (2026-04-23)

---

## Part 1 — Slot × Funder matrix (at-a-glance)

Each row is a universal slot; each column is a funder. A filled cell shows the *funder-specific section or question ID* this slot populates in that funder; an empty cell means this slot is not explicitly required by that funder (author content may still be volunteered if strategically useful).

Legend: funder columns are abbreviated — full names in §Part 3.

### Heilmeier core (U01–U08)

| Slot | Heilmeier | NIH R01 | NSF TL | ARPA-H | DOE Gen | Astera | Brains | Foresight | Google.org | YC |
|------|-----------|---------|--------|--------|---------|--------|--------|-----------|-----------|-----|
| U01 Objective | Q1 | Specific Aims §1 | Q3a.i | App A §1 · Exec Sum | Project Abstract · Narrative §1 | Q1 | B1 | F14·F15 | Q11·Q12·Q16a | YC8·YC9·YC13·YC27 |
| U02 SOTA & limits | Q2 | Significance | Q3a.i (implicit) | App A §2 · Tech Approach | Narrative §1 Significance | Q4 | B2 | F16 | Q16b·Q16c | YC24·YC25 |
| U03 Novelty & approach | Q3 | Innovation · Approach | Q3a.i·Q3a.ii | App A §3 · Tech Approach | Narrative §2·§3 | Q2 | B3 | F16 | Q17a–d·Q20·Q21·Q22·Q28 | YC13·YC29·YC32 |
| U04 Stakes & beneficiaries | Q4 | Significance | Q6 (impact) | App A §4 | Narrative §1·§5 | Q4·Q5 | B4·B5 | F19 | Q18a·Q18c·Q19c | YC24 |
| U05 Risks | Q5 | Approach (alt. strategies) | — | App A §5 · Tech Approach | Narrative §6 | — | B6 | F17 | Q29 | — |
| U06 Cost | Q6 | SF-424 R&R Budget | Q4e | Cost Proposal · App A §Budget | SF-424 · Budget Justification | Q2 (budget line) | — | F27–F30·F31 | Q37–Q42 | YC26·YC30 |
| U07 Schedule | Q7 | Approach (timeline) | Q4b (phases) | Tech Approach · Mgmt Plan | Narrative §3 (milestones) | Q2 (timeline) | — | F18 | Q43–Q47 | YC30 |
| U08 Exams & gates | Q8 | Approach (benchmarks) | — | App A §3 · Tech Approach | Narrative §3·§5 | — | B5·B6 | F18 | Q19a·Q19b·Q19c·Q28 | — |

### Extensions (U09–U20)

| Slot | Heilmeier | NIH R01 | NSF TL | ARPA-H | DOE Gen | Astera | Brains | Foresight | Google.org | YC |
|------|-----------|---------|--------|--------|---------|--------|--------|-----------|-----------|-----|
| U09 Opportunity-space | — | — | Q3a.i·Q6 | App A §1 · Tech Approach | Narrative §1 | — | Vision for Impact | — | — | — |
| U10 Why-not-academia/VC | — | — | Q2·Q3a.i | — | — | Q6 | B7 | — | — | — |
| U11 Team fit | — | Investigators · Environment | Q3a.ii·Q3a.iii·Q3b | App A §Team · Tech Mgmt | Narrative §4 · Biosketches | Q3·Q5·Q6 | Prog Ldrshp Readiness | F9·F10·F11 | Q25·Q26·Q27·Q30 | YC1–YC7 |
| U12 Open science | — | DMP | Q4c (openness) | — | DMP | Q8 | — | F20 | Q13·Q24 | — |
| U13 Equity / access | — | — | — | App A §4 | — | — | — | — | Q18a·Q18b | — |
| U14 Responsible AI | — | — | — | App A §5 | — | — | — | F17 | Q23 | — |
| U15 IP & data | — | — | Q4c | TDD · App A §5 | DMP | — | — | F32–F34 | Q22 (data) | — |
| U16 Regulatory / biosecurity | — | Human Subjects · DURC | — | App A §5 · Cost §HSR/AR · TDD | Compliance appendices | — | — | — | — | YC31 |
| U17 End-user / adoption | — | — | Q3a.iv-v · Q6 | Tech Mgmt §TransPractice | Narrative §5 | Q5 | B4 | — | Q35 (deployment) | YC16–YC21·YC24·YC27 |
| U18 Translation-to-Mission | — | — | Q3a.iv-v · Q6 | Tech Mgmt §TransPractice · TDD | Narrative §5 | — | — | — | — | YC26 |
| U19 Sustainability / sunset | — | — | — | Tech Mgmt §Sustainability | Narrative §4·§5 | — | — | F19 | Q32·Q33·Q34a·Q34b·Q35 | YC26 |
| U20 Partnerships | — | — | Q3a.iv·Q3a.v·Q5 | Tech Mgmt §Partnerships · TDD | Narrative §4 | — | — | F10·F11·F25 | Q31a–e (×5) | YC23 |

### Administrative (A01–A05)

| Slot | NIH R01 | NSF TL | ARPA-H | DOE Gen | Astera | Brains | Foresight | Google.org | YC |
|------|---------|--------|--------|---------|--------|--------|-----------|-----------|-----|
| A01 Org identity | SF-424 R&R (cover) | Q1 | Cost §Entity | SF-424 · Title Page | Residency form | Basic info | F1–F8 | Q1–Q6 | YC14·YC15·YC33–YC36 |
| A02 POC | SF-424 R&R | Q1 | Cost §POC | SF-424 · Cover | Residency form | Basic info | F1–F8 | Q8·Q9·Q10 | (implicit) |
| A03 Eligibility / compliance | R&R Other | Q3b | Cost §Compliance · Admin & National Policy | Compliance appendices | — | — | F35–F39 | Q48–Q53 | YC33–YC36 |
| A04 Supplementary artifacts | Biosketches · Letters of Support | — | Letters of Support | Biosketches · Bibliography · DMP | Video · Resume | References | F11·F20 | — | YC10·YC11·YC12 |
| A05 Intake meta | — | — | — | — | "How did you hear" | — | F35·F36·F38 | Q7 | YC37·YC38 |

**Reading the matrix:**
- An empty cell is permission to *omit* the slot, not prohibition. For slots like U10, U12, U13, and U14 where Cytognosis values are strong, volunteer content even if the funder doesn't ask (add as an appendix or inside `U04 Stakes`).
- Multiple cells per row are expected — the same universal content is re-cut to different funders' length and structural demands.
- Where a cell lists more than one funder question, that slot fills more than one prompt in that funder's form (e.g., U01 populates *every* Google.org title/topic/focus question).

---

## Part 2 — Per-funder detail tables (funder Q → slot)

These are the authoritative one-to-one mappings. If the Part 1 matrix conflicts with Part 2, trust Part 2.

### 2.1 Heilmeier (universal baseline)

| Heilmeier Q | Question | → Universal slot(s) |
|---|---|---|
| Q1 | What are you trying to do (no jargon)? | U01 |
| Q2 | How is it done today; limits? | U02 |
| Q3 | What is new; why will it succeed? | U03 |
| Q4 | Who cares; what difference? | U04 |
| Q5 | What are the risks? | U05 |
| Q6 | How much will it cost? | U06 |
| Q7 | How long will it take? | U07 |
| Q8 | Mid-term and final exams? | U08 |

### 2.2 NIH R01 Research Strategy

| Section | → Universal slot(s) |
|---|---|
| Cover · SF-424 R&R | A01 · A02 |
| Specific Aims (1 p) | U01 · U03.1 · U04.1 · U08.1 |
| Research Strategy §Significance | U02 · U04 |
| Research Strategy §Innovation | U03 |
| Research Strategy §Approach (design + alt. strategies + rigor + timeline + benchmarks) | U03 · U05 · U07 · U08 |
| Investigators & Environment | U11 · A01 |
| Biosketches | A04 · U11.2 |
| Budget (R&R Budget + Justification) | U06 · A01 |
| Data Management & Sharing Plan | U12 · U15.3 |
| Human Subjects / Vertebrate Animals | U16.2 · U16.3 |
| Resource Sharing (DURC, foreign) | U15.5 · U16.4 |
| Bibliography | A04 |
| Letters of Support | A04 |
| Current & Pending | A03 · U20.5 |

### 2.3 NSF Tech Labs RFI

| RFI Q | → Universal slot(s) |
|---|---|
| Q1 (org overview) | A01 · U11.2 |
| Q2 (comparative advantage) | U10.3 · U10.4 |
| Q3a.i (mission clarity) | U01.2 · U09.1 · U10.3 |
| Q3a.ii (team qualifications) | U11.2 |
| Q3a.iii (leadership continuity) | U11.6 · U19.2 |
| Q3a.iv / Q3a.v (partnerships) | U20.3 · U20.5 |
| Q3b.i / Q3b.ii (ecosystem fit) | U11.4 · U11.6 |
| Q4a (eligibility) | U11.6 |
| Q4b (phases / timing) | U07.2 |
| Q4c (IP & openness) | U15.2 · U12.2 |
| Q4d (sustainability) | U11.6 · U19.2 |
| Q4e (funding level & scale) | U06.1 · U06.5 |
| Q5 (novel partnerships) | U20.3 |
| Q6 (beneficiary of NSF Tech Labs) | U04.4 · U09.1 |
| Q7 (RFI feedback) | — (meta, out-of-slot) |

### 2.4 ARPA-H Mission Office ISO

| Artifact → Section | → Universal slot(s) |
|---|---|
| Appendix A §1 Program fit | U01 · U09.1 |
| Appendix A §2 How is it done today | U02 |
| Appendix A §3 Novelty + quantitative metrics | U03 · U08.1 |
| Appendix A §4 Who cares | U04 · U13.1 · U13.2 · U17.1 · U17.4 |
| Appendix A §5 Risks | U05 · U14.2 · U16.1 · U16.6 |
| Appendix A §Team | U11.1 · U11.2 · U11.4 |
| Appendix A §Budget synopsis | U06.1 · U06.2 |
| Tech & Mgmt Proposal §Executive Summary | U01 · U04 · U08.1 |
| Tech & Mgmt Proposal §Technical Approach | U02 · U03 · U08 |
| Tech & Mgmt Proposal §Management Plan & Phases | U07 · U08.2 |
| Tech & Mgmt Proposal §Team | U11 |
| Tech & Mgmt Proposal §Transition-to-Practice | U17.2 · U17.5 · U17.6 · U18 |
| Tech & Mgmt Proposal §Partnerships | U20.1 · U20.3 |
| Tech & Mgmt Proposal §Sustainability | U19.1 |
| TDD §IP & Data | U15.1 · U15.2 · U15.3 · U15.5 |
| TDD §Dual-Use / Biosecurity | U16.4 · U16.5 |
| TDD §Consortium Governance | U20.2 |
| TDD §Translation IP | U18.3 |
| Cost Proposal §Budget | U06.1 · U06.2 · U06.3 · U06.4 |
| Cost Proposal §Compliance | A01 · A03 |
| Cost Proposal §HSR / AR | U16.2 · U16.3 |
| Letters of Support | A04.5 |

### 2.5 DOE Genesis Mission (Focus Area 2)

| Artifact | → Universal slot(s) |
|---|---|
| Project Abstract (1 p) | U01 |
| Title Page + SF-424 + budget pages | A01 · A02 · A03 · U06 |
| Project Narrative §1 Significance | U02 · U04 · U09.1 · U09.2 |
| Project Narrative §2 Innovation / Approach | U03 |
| Project Narrative §3 Technical approach & milestones | U03.2 · U07 · U08 |
| Project Narrative §4 Team & management | U11 · U20 |
| Project Narrative §5 Go/no-go + outcomes + sustainability | U08.2 · U04.4 · U17.5 · U18.1 · U19.1 · U19.5 |
| Project Narrative §6 Risk & mitigation | U05 |
| Biosketches | A04 · U11 |
| Facilities & equipment | U11.4 |
| Data Management Plan | U12 · U15.3 |
| Bibliography | A04 |
| Budget justification | U06.2 · U06.3 |
| Current & pending | A03 · U20.5 |

### 2.6 Astera Residency

| Q | → Universal slot(s) |
|---|---|
| "How did you hear" | A05 |
| Q1 (300-char pitch) | U01.1 · U01.2 |
| Q2 (plan + budget line + timing) | U03.2 · U06.2 · U07.3 |
| Q3 (who-are-you) | U11.1 · U11.2 · U11.3 · U03.4 |
| Q4 (why it matters / why now) | U02.1 · U02.2 · U04.2 |
| Q5 (non-legible accomplishments) | U04.1 · U17.1 · U17.3 · U11.3 |
| Q6 (why Astera vs. academia/VC) | U10.1 · U10.2 · U10.3 |
| Q7 (scope / phasing / anti-goals) | U09.4 · U07.2 |
| Q8 (openness commitments) | U12.1 · U12.2 · U12.4 |
| Video + resume | A04 |

### 2.7 Brains Accelerator

| Section | → Universal slot(s) |
|---|---|
| Basic info | A01 · A02 |
| B1 (thesis) | U01.1 · U01.2 |
| B2 (SOTA / limits) | U02.1 · U02.2 |
| B3 (novelty / why now) | U03.1 · U03.3 |
| B4 (beneficiaries / adoption) | U04.1 · U17.1 |
| B5 (reach / unlock) | U04.3 · U04.4 |
| B6 (risks / mitigations) | U05.4 · U05.5 |
| B7 (why not traditional) | U10.1 · U10.2 · U10.3 |
| Program Leadership Readiness | U11.1 · U11.2 · U11.4 |
| Vision for Impact | U04.4 · U09.1 |
| References | A04 |

### 2.8 Foresight AI for Safety & Science Nodes

| F-code | → Universal slot(s) |
|---|---|
| F1–F8 (basic + POC) | A01 · A02 |
| F9 (track record) | U11.2 |
| F10 (team) | U11.4 · U20.1 |
| F11 (references) | A04 |
| F12 (ask + how-did-you-hear) | U06.1 · A05 |
| F13 (focus area) | U01.2 |
| F14 (project title) | U01.4 |
| F15 (350-char elevator) | U01.1 · U01.2 |
| F16 (today's limits + what's new) | U02.1 · U02.2 · U03.1 · U03.3 · U04.4 |
| F17 (differential safety) | U14.5 · U14.2 |
| F18 (phasing + exams) | U07.2 · U07.3 · U08.2 |
| F19 (sustainability / sunset) | U19.5 · U04.3 |
| F20 (open science) | A04 (publications · code · data links) |
| F21–F26 (node residency requests) | U06.2 · U20.2 |
| F27–F30 (budget) | U06.1 · U06.2 · U06.3 |
| F31 (ambitious vs. moderate) | U06.5 |
| F32–F34 (edge / privacy / compute) | U06.2 · U15.4 |
| F35–F39 (compliance / intake meta) | A03 · A05 |

### 2.9 Google.org AI Impact Challenge

| Q | → Universal slot(s) |
|---|---|
| Q1–Q10 (org + POC + intake) | A01 · A02 · A05 |
| Q11 (title) | U01.4 |
| Q12 (topic) | U01.2 |
| Q13 (open-source outputs) | U12.1 · U12.2 |
| Q14 (geography) | U13.1 |
| Q15 (project stage / TRL) | U03.4 |
| Q16a (plain-language objective) | U01.2 |
| Q16b (current landscape) | U02.1 · U02.2 |
| Q16c (why hasn't it been solved) | U02.2 · U03.1 |
| Q17a (novel idea) | U03.1 |
| Q17b (technical approach) | U03.2 |
| Q17c (prior evidence) | U03.4 |
| Q17d (why it matters now) | U03.3 · U04.4 |
| Q18a (target population) | U04.1 · U13.1 |
| Q18b (beneficiary voice) | U13.3 |
| Q18c (magnitude / reach) | U04.3 |
| Q19a (success metric) | U08.1 |
| Q19b (failure indicators) | U05.4 · U08.3 |
| Q19c (baseline vs. change) | U08.4 |
| Q20 (data & tools) | U03.2 |
| Q21 (why now) | U03.1 · U03.3 |
| Q22 (data governance) | U03.2 · U15.3 |
| Q23 (AI Principles compliance) | U14.2 · U14.4 |
| Q24 (open-source plan) | U12.2 |
| Q25 (ecosystem partners) | U11.5 · U20.3 |
| Q26 (team) | U10.4 · U11.1 · U11.2 |
| Q27 (AI maturity) | U11.4 |
| Q28 (feasibility evidence) | U03.4 · U08.1 |
| Q29 (risks) | U05.1 · U05.2 · U05.3 · U05.5 |
| Q30 (key roles) | U11.4 · U11.5 |
| Q31a–e ×5 (partner details) | U20.1 |
| Q32 (scaling) | U19.5 |
| Q33 (governance for scale) | U11.5 · U19.2 |
| Q34a (post-grant funding) | U19.1 |
| Q34b (technical sustainability) | U19.3 |
| Q35 (adoption / deployment) | U12.3 · U17.5 |
| Q36 (convening / community) | U11.2 · U20.4 |
| Q37 (total ask) | U06.1 |
| Q38–Q42 (budget breakdown) | U06.2 · U06.3 |
| Q43–Q47 (schedule / milestones) | U07.2 · U07.3 · U08.2 |
| Q48–Q53 (compliance / due diligence) | A03 |

### 2.10 Y Combinator Nonprofit

| Q | → Universal slot(s) |
|---|---|
| YC1 (founder track record) | U11.2 |
| YC2 (non-legible accomplishments) | U11.3 |
| YC3 (things you didn't put on resume) | U11.3 |
| YC4 (education / credentials) | U11.2 |
| YC5 (prior companies / projects) | U11.2 |
| YC6 (co-founder relationship) | U11.4 |
| YC7 (gaps in team) | U11.5 |
| YC8 (company/project name) | U01.4 |
| YC9 (50-char tagline) | U01.3 |
| YC10–YC12 (demo + video + links) | A04 |
| YC13 (what does your nonprofit do) | U01.2 · U03.2 |
| YC14–YC15 (legal status / location) | A01 |
| YC16–YC21 (progress · launched · revenue · beneficiaries) | U03.4 · U17.3 |
| YC22 (re-application diff) | — (meta, out-of-slot) |
| YC23 (prior funder referrals) | U20.5 |
| YC24 (mission + beneficiaries + obsession) | U02.2 · U04.1 · U11.1 |
| YC25 (competition / why not them) | U02.1 · U10.4 |
| YC26 (sustainability / revenue) | U18.1 · U19.1 |
| YC27 (condensed one-liner) | U01.2 |
| YC28 (alternatives considered) | U09.4 |
| YC29 (primary innovation) | U03.1 · U03.2 |
| YC30 (milestones / funding trajectory) | U07.2 · U07.3 · U06.5 |
| YC31 (regulatory path) | U16.1 · U06.3 · U07.3 |
| YC32 (unique insight) | U03.4 |
| YC33–YC36 (compliance / foreign ties) | A01 · A03 |
| YC37–YC38 (how did you hear / intake) | A05 |

---

## Part 3 — Funder abbreviation key

| Abbrev | Full name | `funder_id` in canonical/ |
|---|---|---|
| Heilmeier | DARPA Heilmeier Catechism | `heilmeier` |
| NIH R01 | NIH Research Project Grant R01 | `nih_r01` |
| NSF TL | NSF Tech Labs (RFI 2026) | `nsf_tech_labs` |
| ARPA-H | ARPA-H Mission Office ISO | `arpah_mission_office` |
| DOE Gen | DOE Genesis Mission (Focus Area 2) | `doe_genesis` |
| Astera | Astera Institute Residency | `astera_residency` |
| Brains | Brains Accelerator | `brains_accelerator` |
| Foresight | Foresight Institute AI for Safety & Science Nodes | `foresight_nodes` |
| Google.org | Google.org AI Impact Challenge | `google_impact_challenge` |
| YC | Y Combinator Nonprofit Program | `yc_nonprofit` |

---

## Part 4 — Coverage diagnostics (auto-derivable)

These sanity checks should run automatically against the manifest — listed here so an author can reason about coverage without running the script.

### Slots universally required (every funder)
- **U01 Objective** — 10/10 funders
- **U03 Novelty & approach** — 10/10
- **U04 Stakes & beneficiaries** — 10/10
- **U11 Team fit** — 10/10
- **A01 Org identity** — 9/9 real funders (Heilmeier has no submission)
- **A02 POC** — 9/9

### Slots under-required (≤ 3 funders explicitly prompt)
- **U13 Equity / access** — 2/10 (ARPA-H, Google)
- **U14 Responsible AI** — 3/10 (Foresight, Google, ARPA-H)
- **U10 Why-not-academia/VC** — 3/10 (Astera, Brains, NSF TL)

These are the slots Cytognosis should volunteer content for even when not asked, because they are strategic differentiators.

### Slots only appearing in administrative / one funder
- None currently — every slot is used by ≥2 funders.

### Orphan funder questions (not yet mapped)
- NIH R01 "Simplified Review Framework" factors (Importance / Rigor / Expertise) — these re-grouping labels are covered by existing slots but not called out as sections. Add to `nih_r01.yaml` as meta-tags when NIH publishes a template matching the new framework.
- YC22 (re-application diff) and NSF TL Q7 (RFI feedback) — meta questions that do not fit any slot. Leave unmapped.

---

## Part 5 — Usage

**Given a new funder opportunity:**
1. Identify every prompt / section / form field in the solicitation.
2. Walk Part 2 to see if an existing funder file covers a similar shape you can fork.
3. Map each prompt to slot(s) using Part 1 as the menu.
4. Write `canonical/funders/<new_funder>.yaml` with artifacts, sections, and slot lists.
5. Add the funder to the manifest and run the validator.
6. Render.

**Given a slot you're about to author:**
1. Find the slot's row in Part 1 — see every funder that will consume this content.
2. Read the intersecting Part 2 rows for each funder column — see the exact prompt wording.
3. Author once in `canonical/slots/<id>_*.md` — make sure the content works against *every* funder prompt it maps to.
4. Length-trim happens at render time; author at the longest funder limit, not the shortest.

---

*Authored 2026-04-23. Auto-derivable from `canonical/funders/*.yaml` and `canonical/slots/*.md` — this file is currently the hand-maintained reference but will be regenerated from source of truth once a validator is written.*
