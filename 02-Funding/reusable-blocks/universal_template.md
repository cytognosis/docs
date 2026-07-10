# Universal Grant/Application Template (Cytognosis)

**Purpose.** A harmonized, funder-agnostic superset of sections that every Cytognosis grant, application, or proposal can be assembled from. Authored content lives once in canonical slots (U01…U22 + A01…A05); each funder's template is a *sink* that selects, reorders, and length-limits a subset of those slots. Funders compose their schemas via group inheritance (see [`canonical/groups.yaml`](canonical/groups.yaml) and `canonical_template_format.md` §13).

**Companion docs:**
- [`funder_metadata.md`](funder_metadata.md) — F-series funder-metadata fields (F01–F38), the schema for the *opportunity itself* (deadline, instrument, indirect-cost rule, strategic connections, sub-programs, etc.). Drives the Monday `Funding Opportunities` board.
- [`canonical/groups.yaml`](canonical/groups.yaml) — group bundles (six U-groups, four A-groups, eight F-groups) and eleven composition presets (one per `funder_kind`).
- [`canonical/CHANGELOG.md`](canonical/CHANGELOG.md) — schema version history (current: manifest v1.2, groups v1.0).

**Design principles**
1. **Heilmeier-first spine.** U01–U08 reproduce the DARPA Heilmeier Catechism in order; every proposal answers them even when the target funder doesn't explicitly ask.
2. **Extensions as named blocks.** U09–U20 are the 12 recurring extensions from the framework catalog — each maps to a concrete prompt somewhere across existing funders.
3. **Stable slot IDs.** `U01` … `U20` are the addressable content keys. Sub-slots use `U03.2`, `U03.3`, etc. Content authored once under a slot is reusable.
4. **Limits belong to the sink, not the slot.** A slot has canonical content; word/char/page limits are applied at render time by the funder-specific template (e.g., Google's 75-word problem vs. Astera's 1000-char problem).
5. **Every prompt in the extracted apps/grants maps to ≥1 slot.** The mapping table at the end is authoritative; if a new funder prompt has no target slot, add a new slot rather than force-fit.

---

## Part A — Universal sections

### Heilmeier core (U01–U08)

#### U01 — Objective, in plain language
**Asks:** What are you trying to do? Articulate objectives using absolutely no jargon.
**Sub-slots:**
- `U01.1` Bold one-sentence thesis (Gates-style opener, ≤30 words)
- `U01.2` Plain-language objective (no jargon, college-freshman readable)
- `U01.3` Short tagline (≤50 chars, for YC-style compact forms)
- `U01.4` Project title / company name
**Source funders:** Heilmeier Q1 · Astera Q1 · Brains B1 · Foresight F14/F15 · Google Q11/Q16.a · YC YC8/YC9/YC13 · ARPA-H Appendix A §1 · NSF Tech Labs RFI Q3a.i · DoE Genesis Project Abstract.

#### U02 — State of the art & its limits
**Asks:** How is it done today, and what are the limits of current practice?
**Sub-slots:**
- `U02.1` Current-practice narrative (citations, SOTA reference points)
- `U02.2` Gaps / bottlenecks / failure modes of SOTA
- `U02.3` Why the gap persists (structural, not just "no one has tried")
**Source funders:** Heilmeier Q2 · Brains B2 · Foresight F16 (today's-limits clause) · Google Q16.b · Astera Q4 · NIH Significance · ARPA-H Appendix A §2 · DoE Genesis Narrative §1.

#### U03 — Novelty & approach
**Asks:** What is new in your approach, and why do you think it will be successful?
**Sub-slots:**
- `U03.1` Core insight / thesis of novelty
- `U03.2` Technical approach (tools, models, methods, data, hardware)
- `U03.3` Why it will work now (enabling conditions, "why now")
- `U03.4` Evidence of feasibility (pilots, prelim data, literature, PoC)
- `U03.5` Alternative strategies & fallback plans (NIH-style contingencies)
**Source funders:** Heilmeier Q3 · Brains B3 · Foresight F16 (what's-new clause) · Google Q17.a/b/c/d, Q20, Q21, Q28 · Astera Q2 · NIH Innovation/Approach · ARPA-H Appendix A §3 · DoE Genesis Narrative §2/§3 · NSF Tech Labs RFI Q3a.i/ii.

#### U04 — Stakes & beneficiaries
**Asks:** Who cares? If successful, what difference will it make?
**Sub-slots:**
- `U04.1` Beneficiary populations / end-users (who + how many)
- `U04.2` Mechanism of benefit (why lives/practice/field change)
- `U04.3` Magnitude & reach (ambition; numbers where possible)
- `U04.4` Downstream / unlock scenarios (what becomes possible)
**Source funders:** Heilmeier Q4 · Brains B4/B5 · Foresight F19 · Google Q18.a/c, Q19.c · Astera Q4/Q5 · YC YC24 · NSF Broader Impacts · ARPA-H Appendix A §4 · DoE Genesis Narrative §4.

#### U05 — Risks
**Asks:** What are the risks?
**Sub-slots:**
- `U05.1` Technical risks
- `U05.2` Programmatic / execution risks (staffing, dependencies, logistics)
- `U05.3` Policy / regulatory / ethical risks
- `U05.4` Failure-mode narrative (why it could fail, most likely reasons)
- `U05.5` Mitigation plan per risk
**Source funders:** Heilmeier Q5 · Brains B6 · Foresight F17 (safety-first differential) · Google Q29 · ARPA-H Appendix A §5 · DoE Genesis Narrative §6 · NIH contingencies.

#### U06 — Cost
**Asks:** How much will it cost?
**Sub-slots:**
- `U06.1` Total ask (USD) and period
- `U06.2` Budget categories (personnel / compute / equipment / partners / overhead)
- `U06.3` Per-category justification
- `U06.4` Cost share / matching funds
- `U06.5` Phased / tiered budget (ambitious vs. moderate; option A/B)
**Source funders:** Heilmeier Q6 · Google Q37–Q42 · Foresight F27–F30, F31 · YC YC26/YC30 · ARPA-H Cost Proposal (9 sections) · DoE Genesis SF-424 + Budget Justification · NSF Tech Labs Phase 0/1/2 funding levels.

#### U07 — Schedule
**Asks:** How long will it take?
**Sub-slots:**
- `U07.1` Start/end dates and period of performance
- `U07.2` Phased structure (Phase 0 / 1 / 2 or equivalent)
- `U07.3` Milestones with dates
- `U07.4` Dependencies and critical path
**Source funders:** Heilmeier Q7 · Google Q43–Q47 · Foresight F18 · YC YC30 · ARPA-H Technical & Management §Phases · DoE Genesis §Timeline · NSF Tech Labs Phase 0 (9 mo) + Phase 1 (24 mo) + Phase 2 (24+).

#### U08 — Mid-term & final exams (quantitative go/no-go)
**Asks:** What are the mid-term and final "exams" to check for success?
**Sub-slots:**
- `U08.1` Quantitative success metrics (numeric, ambitious — 4×, 100× style)
- `U08.2` Go/no-go decision gates per phase
- `U08.3` Negative signals / failure indicators
- `U08.4` Baseline vs. expected change
**Source funders:** Heilmeier Q8 · Google Q19.a/b/c · Foresight F18 · Brains B5/B6 · ARPA-H Appendix A §3 (quantitative metrics) · DoE Genesis Narrative §3/§5 · ARPA-E Performance Period Goals · Wellcome Leap 3-yr milestones.

---

### Extension blocks (U09–U20)

#### U09 — Bold thesis & opportunity-space framing
**Asks:** Why is this space consequential, under-explored, and ripe for a new bet? Why now?
**Sub-slots:**
- `U09.1` Opportunity-space thesis (ARIA triple: consequential · under-explored · ripe)
- `U09.2` "Why now" — enabling conditions (tech, data, regulatory, cultural)
- `U09.3` Uniqueness · Impact · Magic (Media Lab 3-sentence gut-check)
- `U09.4` Anti-goals — what this program will *not* do
**Source funders:** ARIA Opportunity Space · Gates Grand Challenges (unconventional approach) · Media Lab · Brains (implicit, via coordinated-program framing).

#### U10 — Why-not-academia / why-not-for-profit / why-Cytognosis (org-form fit)
**Asks:** Why does this need an FRO / independent nonprofit / DARPA-shaped bet — not a PI, not a startup?
**Sub-slots:**
- `U10.1` Why not a standard academic lab / PI
- `U10.2` Why not a VC-backed startup
- `U10.3` Why this form (FRO / 501(c)(3) + PBC Helix / coordinated research program)
- `U10.4` What Cytognosis can do that alternatives can't
**Source funders:** Astera Q6 (explicit) · Brains B7 (explicit) · FRO template · Speculative Technologies · NSF Tech Labs RFI Q2 (comparative advantage) · Convergent Research FRO pitch.

#### U11 — Team & founder fit
**Asks:** Why this team, now? Obsession, track record, non-legible expertise, diversity.
**Sub-slots:**
- `U11.1` Founder / PI obsession & origin story (how long, why you)
- `U11.2` Track record (publications, prior builds, prior funding outcomes)
- `U11.3` Non-legible accomplishments (Astera Q5 style)
- `U11.4` Key team members / roles / expertise (Google-style: role + expertise, no names)
- `U11.5` Hiring plan / gaps to fill
- `U11.6` Governance / advisors / scientific board
**Source funders:** Astera Q3/Q5/Q6 · Brains "Program Leadership Readiness" · YC YC1–YC7 · Foresight F9/F10/F11 · NIH Investigators/Environment · Google Q26/Q30 · NSF Tech Labs Q3a.ii/iii · Schmidt personal statement.

#### U12 — Open science & openness commitments
**Asks:** What outputs are released as public goods, under what licenses, and what tradeoffs do you anticipate?
**Sub-slots:**
- `U12.1` Output inventory (publications, datasets, software, models, hardware designs, SOPs)
- `U12.2` Licensing plan (CC-BY/CC0 · Apache/MIT · OpenRAIL · etc.)
- `U12.3` Release cadence and channels
- `U12.4` Openness tradeoffs (safety holds, embargoes, privacy, competitive concerns)
- `U12.5` FAIR / reproducibility commitments (data standards, ontologies, containers)
**Source funders:** Astera Q8 (required) · Google Q13/Q24 (required) · Foresight (preferred) · FRO template · Horizon Europe dissemination/open-access · Media Lab permissionless-innovation · NSF Tech Labs (strategic objective 2: outcomes beyond papers).

#### U13 — Equity, accessibility, workforce
**Asks:** Who benefits, who is excluded, how do you centre beneficiary voices, how does workforce participation happen?
**Sub-slots:**
- `U13.1` Target populations / geographies / socioeconomic reach
- `U13.2` Affordability & access plan (cost-to-user, low-resource deployment)
- `U13.3` Beneficiary-voice mechanism (co-design, advisory boards, feedback loops)
- `U13.4` Workforce / training / broadening participation
- `U13.5` Unintended-exclusion audit
**Source funders:** Google Q18.a/b · NSF Broader Impacts · ARPA-H equity/access block · Horizon Europe Impact · Gates Grand Challenges · Cytognosis values memo.

#### U14 — Responsible AI / AI safety
**Asks:** What are the AI-specific risks (dual-use, alignment, evaluation, privacy), and how are they mitigated?
**Sub-slots:**
- `U14.1` AI system description (models, capabilities, deployment surface)
- `U14.2` Dual-use & misuse analysis (adversarial, privacy, amplification)
- `U14.3` Evaluation & red-teaming plan
- `U14.4` Alignment with Google AI Principles / NIST AI RMF / EU AI Act as applicable
- `U14.5` Differential safety advancement (Foresight F17 style)
- `U14.6` Model/data governance (access control, auditing, update policy)
**Source funders:** Foresight F17 (first-class) · Google Q23 · ARPA-H (emerging) · NSF Tech Labs (responsible innovation) · Horizon Europe ethics self-assessment · Cytognosis values memo.

#### U15 — IP & data governance
**Asks:** Who owns what, who can use it, what is open, what is restricted?
**Sub-slots:**
- `U15.1` Background IP inventory
- `U15.2` Foreground IP plan (what is created, who holds title, how licensed)
- `U15.3` Data governance (consent, custody, retention, re-use)
- `U15.4` Privacy architecture (de-identification, federation, edge-compute)
- `U15.5` Export control / research-security posture (CHIPS & Science Act, MFTRP)
**Source funders:** ARPA-E T2M IP · SBIR IP rights · Wellcome Leap standard FA · Horizon Europe exploitation · FRO open-by-default · NSF Tech Labs RFI Q4c · ARPA-H TDD.

#### U16 — Regulatory, dual-use & biosecurity
**Asks:** What regulatory, ethics, and dual-use/biosecurity reviews apply, and what is the plan?
**Sub-slots:**
- `U16.1` FDA / SaMD / IVD pathway (if applicable)
- `U16.2` IRB / human subjects plan (consent, enrollment, DSMB)
- `U16.3` Animal use / IACUC (if applicable)
- `U16.4` Dual-use research of concern (DURC, P3CO, gain-of-function)
- `U16.5` Biosecurity screening for synthetic biology outputs
- `U16.6` Ethics self-assessment (Horizon Europe style)
**Source funders:** ARPA-H regulatory/ethics · NIH human-subjects, DURC · Horizon Europe ethics · YC YC31 · DoE Genesis compliance appendices · ARPA-H Cost Proposal §HSR/AR.

#### U17 — End-user narrative / adoption / transition-to-practice
**Asks:** Who picks this up, how do they use it, what is the switching cost, and how does the technology transition after the grant?
**Sub-slots:**
- `U17.1` Customer / user segment (who, where, buying process)
- `U17.2` Future-press-release / PR-FAQ (Amazon style)
- `U17.3` Adoption story — first 10 users, first 100, first 10k
- `U17.4` Switching cost vs. status quo
- `U17.5` Transition-to-practice plan (who operates it after award)
- `U17.6` Commercialization strategy (if applicable; SBIR-style)
**Source funders:** Amazon PR-FAQ · Lean Canvas · YC YC24–YC26 · ARPA-H transition-to-practice · SBIR commercialization · NSF Tech Labs strategic objectives 2 & 4 · DoE Genesis Narrative §4.

#### U18 — Translation-to-Mission plan (Market · Manufacturing · IP · Funding)
**Asks:** ARPA-E-style four-question framework adapted for nonprofit bio+AI.
**Sub-slots:**
- `U18.1` Mission: what real-world value must exist for adoption to occur
- `U18.2` Production: can it be produced/deployed cost-effectively at scale
- `U18.3` IP: how secured / licensed / openly released (references U15.2)
- `U18.4` Funding: post-grant sustainability (references U19)
- `U18.5` TEA / LCA analog (cost-per-insight, impact-per-$) where relevant
**Source funders:** ARPA-E T2M · SBIR Phase III · ARPA-H commercialization · DoE Genesis §Transition · Wellcome Leap transition.

#### U19 — Sustainability / transition / sunset
**Asks:** How does this continue (or wind down) after the grant period?
**Sub-slots:**
- `U19.1` Post-grant funding strategy (next funders, revenue model, endowment)
- `U19.2` Operating-entity continuity (who runs it, where it lives)
- `U19.3` Technical sustainability (maintenance, cloud costs, data hosting)
- `U19.4` Sunset plan — if it doesn't continue, how are outputs preserved as public goods
- `U19.5` Scalability levers (geographic, sectoral, user-growth, policy)
**Source funders:** FRO sunset · Horizon Europe exploitation · ARPA-E T2M funding · SBIR Phase III · Google Q32/Q34.a/Q34.b/Q35 · Foresight F19 · YC YC26.

#### U20 — Partnerships, ecosystem, consortium
**Asks:** Who else is in the circle, and how does the coordination work?
**Sub-slots:**
- `U20.1` Strategic partners (name, website, role, relationship status)
- `U20.2` Consortium governance (PD model, RFP flow, IP defaults)
- `U20.3` Industry / philanthropy engagement
- `U20.4` Community & convening (workshops, seminars, open calls)
- `U20.5` Prior funder relationships & referrals
**Source funders:** Google Q31.a–e × 5 · Foresight F10/F11/F25 · NSF Tech Labs RFI Q3a.iv/v, Q5 · ARPA-H teaming/TDD · Wellcome Leap consortium · Speculative Technologies block-diagram consortia.

---

## Part B — Administrative & conditional sections (A01–A05)

Not proposal content per se, but present in most funders.

| ID | Slot | Typical contents | Source funders |
|---|---|---|---|
| A01 | Organizational identity | Legal name, EIN, classification, year founded, budget, FTE, website, socials | Google I, Foresight About You, YC Equity, ARPA-H admin, DoE SF-424, NSF Tech Labs Q1 |
| A02 | Points of contact | Primary & secondary POC, timezone, English fluency | Google Q8/Q9/Q10, Foresight F1/F2, DoE cover |
| A03 | Eligibility / compliance | Government ties, sanctioned-country dealings, prior SBIR, foreign influence | Google Q48–Q53, YC YC33–YC35, DoE compliance, ARPA-H research security |
| A04 | Supplementary artifacts | Video (2-min), resume, demo URL, bibliographies, letters of support | Astera video, YC YC11, Foresight F4, ARPA-H letters, DoE biosketches |
| A05 | Intake meta | How did you hear, consent to share, expedited review, batch preference | Google Q7, Foresight F38/F35/F36, YC YC37/YC38 |

---

## Part C — Master mapping table

Every prompt extracted in `extracted_questions_applications.md` and `extracted_grants.md` mapped to the universal slot(s) it occupies. Read as: *"this funder's question writes content into these slot(s)"*.

### C.1 Google.org Impact Challenge

| Funder Q | → Universal slot(s) |
|---|---|
| Q1–Q10 (org + POC + intake) | A01 · A02 · A05 |
| Q11 (title) | U01.4 |
| Q12 (topic) | U01.2 (categorization) |
| Q13 (open-source outputs) | U12.1 · U12.2 |
| Q14 (geography) | U13.1 |
| Q15 (project stage) | U03.4 (TRL/feasibility) |
| Q16.a | U01.2 |
| Q16.b | U02.1 · U02.2 |
| Q16.c | U02.2 · U03.1 |
| Q17.a | U03.1 |
| Q17.b | U03.2 |
| Q17.c | U03.4 |
| Q17.d | U03.3 · U04.4 |
| Q18.a | U04.1 · U13.1 |
| Q18.b | U13.3 |
| Q18.c | U04.3 |
| Q19.a | U08.1 |
| Q19.b | U05.4 · U08.3 |
| Q19.c | U08.4 |
| Q20 | U03.2 |
| Q21 | U03.1 · U03.3 |
| Q22 | U03.2 · U15.3 |
| Q23 | U14.2 · U14.4 |
| Q24 | U12.2 |
| Q25 | U11.5 · U20.3 |
| Q26 | U10.4 · U11.1 · U11.2 |
| Q27 (AI Maturity) | U11.4 |
| Q28 | U03.4 · U08.1 |
| Q29 | U05.1 · U05.2 · U05.3 · U05.5 |
| Q30 | U11.4 · U11.5 |
| Q31.a–e ×5 | U20.1 |
| Q32 | U19.5 |
| Q33 | U11.5 · U19.2 |
| Q34.a | U19.1 |
| Q34.b | U19.3 |
| Q35 | U12.3 · U17.5 |
| Q36 | U11.2 · U20.4 |
| Q37 | U06.1 |
| Q38–Q42 | U06.2 · U06.3 |
| Q43–Q47 | U07.2 · U07.3 · U08.2 |
| Q48–Q53 | A03 |

### C.2 Astera Residency

| Funder Q | → Universal slot(s) |
|---|---|
| "How did you hear" | A05 |
| Q1 (300 char) | U01.1 · U01.2 |
| Q2 | U03.2 · U06.2 · U07.3 |
| Q3 | U11.1 · U11.2 · U11.3 · U03.4 |
| Q4 | U02.1 · U02.2 · U04.2 |
| Q5 | U04.1 · U17.1 · U17.3 |
| Q6 | U10.1 · U10.2 · U10.3 |
| Q7 | U09.4 (in-scope/out-of-scope = anti-goals) · U07.2 |
| Q8 | U12.1 · U12.2 · U12.4 |
| Video + resume | A04 |

### C.3 Brains Accelerator

| Funder Q | → Universal slot(s) |
|---|---|
| Basic info | A01 · A02 |
| B1 | U01.1 · U01.2 |
| B2 | U02.1 · U02.2 |
| B3 | U03.1 · U03.3 |
| B4 | U04.1 · U17.1 |
| B5 | U04.3 · U04.4 |
| B6 | U05.4 · U05.5 |
| B7 (why-not-traditional) | U10.1 · U10.2 · U10.3 |
| Program Leadership Readiness | U11.1 · U11.2 · U11.4 |
| Vision for Impact | U04.4 · U09.1 |
| References | A04 |

### C.4 Foresight AI for Safety & Science Nodes

| Funder Q | → Universal slot(s) |
|---|---|
| F1–F8 | A01 · A02 |
| F9 | U11.2 |
| F10 | U11.4 · U20.1 |
| F11 | A04 |
| F12 | U06.1 · A05 |
| F13 | U01.2 (focus-area tag) |
| F14 | U01.4 |
| F15 (350 char) | U01.1 · U01.2 |
| F16 | U02.1 · U02.2 · U03.1 · U03.3 · U04.4 |
| F17 | U14.5 · U14.2 |
| F18 | U07.2 · U07.3 · U08.2 |
| F19 | U19.5 · U04.3 |
| F20 | A04 |
| F21–F26 | U06.2 · U20.2 (node residency requests) |
| F27–F30 | U06.1 · U06.2 · U06.3 |
| F31 (ambitious/moderate) | U06.5 |
| F32–F34 | U06.2 · U15.4 (edge/private compute governance) |
| F35–F39 | A03 · A05 |

### C.5 Y Combinator

| Funder Q | → Universal slot(s) |
|---|---|
| YC1 | U11.2 |
| YC2 | U11.3 |
| YC3 | U11.3 |
| YC4 | U11.2 |
| YC5 | U11.2 |
| YC6 | U11.4 |
| YC7 | U11.5 |
| YC8 | U01.4 |
| YC9 (50 char) | U01.3 |
| YC10–YC12 | A04 |
| YC13 | U01.2 · U03.2 |
| YC14–YC15 | A01 |
| YC16–YC21 | U03.4 · U17.3 |
| YC22 | meta (re-application diff) — out-of-slot |
| YC23 | U20.5 |
| YC24 | U02.2 · U04.1 · U11.1 |
| YC25 | U02.1 · U10.4 |
| YC26 | U18.1 · U19.1 |
| YC27 | U01.2 |
| YC28 | (alternatives-considered) → U09.4 |
| YC29 | U03.1 · U03.2 |
| YC30 | U07.2 · U07.3 · U06.5 |
| YC31 | U16.1 · U06.3 · U07.3 |
| YC32 | U03.4 |
| YC33–YC36 | A01 · A03 |
| YC37–YC38 | A05 |

### C.6 NSF Tech Labs RFI

| RFI Q | → Universal slot(s) |
|---|---|
| Q1 (org overview) | A01 · U11.2 |
| Q2 (comparative advantage) | U10.3 · U10.4 |
| Q3a.i | U01.2 · U09.1 · U10.3 |
| Q3a.ii | U11.2 |
| Q3a.iii | U11.6 · U19.2 |
| Q3a.iv / Q3a.v | U20.3 · U20.5 |
| Q3b.i / Q3b.ii | U11.4 · U11.6 (ecosystem view) |
| Q4a | U11.6 (eligibility design feedback) |
| Q4b | U07.2 |
| Q4c | U15.2 · U12.2 |
| Q4d | U11.6 · U19.2 |
| Q4e | U06.1 · U06.5 |
| Q5 | U20.3 |
| Q6 | U04.4 · U09.1 |
| Q7 | meta-feedback — out-of-slot |

### C.7 ARPA-H Mission Office ISO — Solution Summary (Appendix A) + Full Proposal

| Appendix A section | → Universal slot(s) |
|---|---|
| §1 Program fit / what are you trying to do | U01 · U09 |
| §2 How is it done today / limits | U02 |
| §3 Novelty + quantitative metrics | U03 · U08.1 |
| §4 Who cares / stakes | U04 · U13 · U17 |
| §5 Risks | U05 · U14 · U16 |
| Team / key personnel | U11 |
| Budget synopsis | U06 |
| Full Technical & Management Proposal (20 p) | all Heilmeier slots + U11 + U15 + U16 + U17 + U20 |
| TDD | U15 · U16.4 · U20.2 |
| Cost Proposal (9 sections) | U06 in depth · A01 · A03 |

### C.8 DoE Genesis Mission (Focus Area 2)

| Phase I artifact | → Universal slot(s) |
|---|---|
| Project Abstract (1 p) | U01 |
| Title Page + SF-424 + budget pages | A01 · A02 · A03 · U06 |
| Project Narrative §1 Significance | U02 · U04 |
| §2 Innovation / Approach | U03 |
| §3 Technical approach & milestones | U03.2 · U07 · U08 |
| §4 Team & management | U11 · U20 |
| §5 Go/no-go + outcomes | U08.2 · U04.4 |
| §6 Risk & mitigation | U05 |
| Biosketches | A04 · U11 |
| Facilities & equipment | U11.4 (environment) |
| Data management plan | U12 · U15.3 |
| Bibliography | A04 |
| Budget justification | U06.2 · U06.3 |
| Current & pending | A03 · U20.5 |

---

## Part D — Slot coverage heatmap (which funders use which slots)

| Slot | Google | Astera | Brains | Foresight | YC | NSF Tech Labs | ARPA-H | DoE Genesis |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| U01 Objective (plain) | ● | ● | ● | ● | ● | ● | ● | ● |
| U02 SOTA & limits | ● | ● | ● | ● | ● | ○ | ● | ● |
| U03 Novelty & approach | ● | ● | ● | ● | ● | ● | ● | ● |
| U04 Stakes | ● | ● | ● | ● | ● | ● | ● | ● |
| U05 Risks | ● | ○ | ● | ● | ○ | ○ | ● | ● |
| U06 Cost | ● | ● | ○ | ● | ● | ● | ● | ● |
| U07 Schedule | ● | ● | ○ | ● | ● | ● | ● | ● |
| U08 Exams / go-no-go | ● | ○ | ● | ● | ○ | ○ | ● | ● |
| U09 Bold thesis / why-now | ○ | ○ | ● | ○ | ○ | ● | ● | ● |
| U10 Why-not-academia/VC | ○ | ● | ● | ○ | ○ | ● | ○ | ○ |
| U11 Team fit | ● | ● | ● | ● | ● | ● | ● | ● |
| U12 Open science | ● | ● | ○ | ● | ○ | ● | ○ | ● |
| U13 Equity / access | ● | ○ | ○ | ○ | ○ | ○ | ● | ○ |
| U14 Responsible AI | ● | ○ | ○ | ● | ○ | ○ | ● | ○ |
| U15 IP & data | ● | ○ | ○ | ● | ○ | ● | ● | ● |
| U16 Regulatory / biosecurity | ○ | ○ | ○ | ○ | ● | ○ | ● | ● |
| U17 End-user / adoption | ● | ● | ● | ○ | ● | ● | ● | ● |
| U18 Translation-to-Mission | ○ | ○ | ○ | ○ | ● | ● | ● | ● |
| U19 Sustainability / sunset | ● | ○ | ○ | ● | ● | ○ | ● | ● |
| U20 Partnerships | ● | ○ | ○ | ● | ○ | ● | ● | ● |

`●` = explicitly required/prompted · `○` = implicit or not prompted.

**Implications:**
- **U01, U03, U04, U11 are required by every funder** — these are the "spine of the spine."
- **U08 (go/no-go metrics) and U12 (open science) are gated extensions** — required by research funders (ARPA-H, DoE, Google, Foresight), optional for accelerators (YC, Brains).
- **U10 (FRO-fit) is only explicit in Astera, Brains, NSF Tech Labs** — yet is the strongest differentiator for Cytognosis; we should author it once and include it by default even when not asked.
- **U13 (equity), U14 (responsible AI), U16 (biosecurity)** are funder-conditional but values-critical for Cytognosis — author them once, include by default, trim in length-constrained sinks.
- **U18 (Translation-to-Mission) + U19 (sustainability)** are the weakest coverage — actively weak in Astera/Brains, which is where Cytognosis should be most intentional about volunteering the content.

---

## Part E — Cytognosis-specific default content hooks

These are the slot → Cytognosis-specific canonical-content anchors that all sinks should reference (content lives in the operational docs, not here):

| Slot | Cytognosis anchor |
|---|---|
| U01.1 bold thesis | "GPS for Health" elevator — Cytoverse + Cytoscope + Cytonome |
| U01.2 plain-language objective | From-reactive-to-proactive healthspan narrative (Mission statement) |
| U03.1 novelty | Four-layer hybrid (Three Horizons · OGSM · Hoshin · OKRs) + meso/micro/macro triple |
| U04.1 beneficiaries | Neuro first indication · transdiagnostic-autoimmune (UK) second |
| U07.2 phases | H1 R&D (Y1–5) · H2 Clinical & Commercial (Y5–10) · H3 Globalization (Y10–15) |
| U10.3 org form | 501(c)(3) Foundation + PBC Helix — see Helix paper |
| U11.6 governance | Bylaws v2 · Scientific Advisory Board roster |
| U12 openness | FAIR by default · LinkML/Biolink/RO-Crate stack · Cytognosis Open Science Policy |
| U14 responsible AI | Edge-first Cytonome architecture · federated/decentralized storage · quantum-safe plan |
| U15.3 data governance | Consent model · Cytonome sensor-plug-in protocol · Delphi collaboration |
| U16.1 regulatory | SaMD/IVD pathway per clinical axis · IRB partners |
| U19.1 sustainability | Grant portfolio + PBC revenue reinvestment |

---

*Authored 2026-04-22. Feeds: `framework_catalog.md`, `extracted_questions_applications.md`, `extracted_grants.md`. Downstream consumers: `templates/02_original_order/`, `templates/03_harmonized_order/`, `templates/04_engine_templates/`, `templates/05_content_extracted/`.*
