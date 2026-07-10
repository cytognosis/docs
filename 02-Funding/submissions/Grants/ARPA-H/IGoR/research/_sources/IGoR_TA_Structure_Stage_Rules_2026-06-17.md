# IGoR TA Structure and Participation Rules — Source Extraction
**Date:** 2026-06-17
**Sources read:**
- Appendix A: Program and Technical Description (ARPA-H-SOL-26-155, 20 pages, PDF + extracted text)
- Appendix B: Solution Summary Format and Instructions (Amendment 01, extracted text)
- Appendix C: Proposal Format, Instructions, and Evaluation (extracted text)
- Appendix C.1: Technical & Management Proposal (extracted text)
- ISO Main Document (extracted text)

All quotes are verbatim unless noted; page/line numbers reference the pdftotext-extracted `/tmp/appendix_a.txt` line count or the source file for other documents.

---

## 1. TA DEFINITIONS

### TA1: Comprehensive Disease Models
**Official definition line (Appendix A, §4.1.1, lines 157–166):**
> "TA1 will develop digital twins that encode causal biological relationships across time and length scales. These models will integrate literature, experimental data, and expert knowledge from many subﬁelds into a single representation. The models will empower researchers to interpret new data and formulate hypotheses in the context of everything that is known about a disease, rather than through the lens of a narrow subﬁeld."

**Deliverables / scope:** Disease model architecture (languages, schemas, ontologies); automated ingestion of TA4 experimental data; knowledge gap identification. Models must be: Modular, Mechanistic, Multiscale, Verifiable.

**Out of scope for TA1:** Training new LLMs from scratch; purely correlational models; non-human disease models (except as informative).

---

### TA2: New Science Engine
**Official definition line (Appendix A, §4.1.2, lines 217–223):**
> "TA2 will develop an orchestration layer, a 'New Science Engine,' that plans, veriﬁes, and explains scientiﬁc workﬂows. This is the reasoning core of the IGoR system: it leverages frontier models, synthesizes literature and mechanistic models from TA1 to ﬁnd knowledge gaps, surfaces conceptually adjacent knowledge, and proposes optimal experiments. The proposed experiments would be unconstrained by any single researcher's prior knowledge or local resources."

**Deliverables / scope:** Hypothesis generation, experiment design (Obj. 1); explainability and human researcher interface (Obj. 2). TA2 is "the principal interface for the researcher." Must demonstrate mechanistic grounding (via TA1), multi-modal experimental design (via TA3), and distributed execution (via TA4).

**Out of scope for TA2:** Pre-training new LLMs; irreversible resource commitments without researcher approval; replacing rather than augmenting human researchers.

---

### TA3: Interoperable Experimental Procedures
**Official definition line (Appendix A, §4.1.3, lines 284–289):**
> "Once a hypothesis has been selected, the next step is to generate clear procedures for executing experiments and to identify the optimal laboratory to which it will be assigned. This addresses a current infrastructure gap: today, transferring an experiment from one laboratory to another requires extensive negotiation, protocol adaptation, and troubleshooting. TA3 will make this transfer as straightforward as sending a data ﬁle."

**Deliverables / scope:** Layered protocol architecture (Intent / Protocols / Calibration / Hardware abstractions); open standards development via RFC process and bake-offs; interoperability with IV&V partner; engagement with external standards bodies. Must accommodate at least 3 distinct experimental modalities.

**Out of scope for TA3:** Closed/proprietary protocol systems; protocol development for vertebrate animals or clinical trials.

---

### TA4: Experiment Marketplace
**Official definition line (Appendix A, §4.1.4, lines 362–368):**
> "TA4 will make ordering a validated experiment as routine as querying a database. TA4 will create a network of validated laboratories, such as cloud labs, core facilities, CROs, and independent research labs, that can execute standardized TA3 protocols and return high-quality data and metadata. The marketplace will enable researchers to request experiments from any qualiﬁed laboratory in the network, receive results in a standardized format, and have those results automatically ingested into TA1 disease models."

**Deliverables / scope:** Validated and reproducible experimentation (QC, cell lines, reference materials, concordance); marketplace operations (interfaces, laboratory capability manifests, onboarding infrastructure). Phase I: cultured cells. Phase II: multicellular systems. Phase III: unified cross-team marketplace.

**Out of scope for TA4:** Vertebrate/higher invertebrate animal experiments (except limited cases outside the marketplace per §3); human clinical trials; experiments that don't return TA1-compatible data.

---

## 2. PROGRAM / AWARD STRUCTURE

### Critical finding: ONE integrated proposal covers ALL FOUR TAs.
**Appendix A, §5.1 (lines 432–453) — verbatim:**
> "To be responsive to this solicitation, proposals must address all four TAs (TA1, TA2, TA3, & TA4). **Proposals not addressing all four TAs will not be reviewed.**"

> "Each proposal team is expected to include performers with the expertise and capabilities to address all four TAs. This may involve a single organization with breadth across all areas or, more likely, a team of organizations, each contributing expertise in one or more TAs. A single team member may cover more than one TA."

> "**Proposers must submit a single proposal led by one Principal Investigator under a single prime performer that addresses program Phase I, Phase II, and Phase III.**"

**ISO Main Document, §2 (lines 110–113):**
> "IGoR is a 5-year, 3-phase program. **ARPA-H anticipates awarding to approximately three multidisciplinary teams, each addressing all four components.**"

**Appendix C, §1.1(a) (conforming submission checklist):**
> "The submission includes the requirement to **address all four Technical Areas and all three Phases in the proposal.**"

**Conclusion:** IGoR is NOT a per-TA solicitation. Every proposal must span TA1 through TA4, led by one PI at one prime. ARPA-H expects ~3 awards.

---

## 3. TEAMING REQUIREMENTS AND PREFERENCES BY TA

### All TAs — team composition
**Appendix A, §5.1 (lines 445–452):**
> "Each proposal team is expected to include performers with the expertise and capabilities to address all four TAs. This may involve a single organization with breadth across all areas or, more likely, a team of organizations, each contributing expertise in one or more TAs. A single team member may cover more than one TA. Proposers must describe how their team is organized, how the TA responsibilities are distributed, and how the team will coordinate across TAs to ensure closed-loop operation. Team formation is the sole responsibility of the proposing teams."

### TA4 — minimum 2 laboratories (hard requirement)
**Appendix A, §4.1.4 (lines 413–420):**
> "**Each team must include at least two TA4 laboratories.** In Phase I, reproducibility and concordance metrics will be assessed within each team's own laboratories. In Phase II, teams will begin cross-team experimentation: laboratories from each team must demonstrate the ability to execute experiments requested by another team's TA2 engine, using a common TA3 protocol standard."

### Required named roles (three distinct roles, all TAs)
**Appendix A, §5.5 (lines 829–848) — Project Management section:**

**Role 1 — Principal Investigator (PI):**
> "Proposers must submit a single proposal led by **one Principal Investigator** under a single prime performer." (§5.1)

**Role 2 — Project Manager:**
> "Proposals should identify the individual responsible for day-to-day project management, cross-team integration, delivery tracking, dependency management, and reporting. This individual should have project management expertise, experience managing large multi-team efforts, and a suitable level of effort to manage the project."

**Role 3 — Software Architect (distinct from PI and PM):**
> "Additionally, the proposal should name the individual responsible for interface design, cross-team interoperability, and architectural consistency. This individual should have demonstrated experience building systems that interoperate with external partners (e.g., open-source infrastructure, protocol implementations, API-ﬁrst platforms). **This 'software architect' role is distinct from the PI and Project Manager.** Proposers should describe how this role will exercise architectural authority over implementation decisions, especially those accelerated by AI coding tools."

**Integration leads:**
> "The person or people directly leading integration should be identiﬁed as well as the hours they will dedicate to integration each year."

### Disease area
**Appendix A, §3 (lines 125–140):**
> "Teams will propose their own complex area of human disease... By Phase III, teams must extend their approach to a related disease area." (Teams choose their own disease; no stated preference for disease diversity across proposals.)

---

## 4. CROSS-TA AND MULTI-PROPOSAL PARTICIPATION

### Organization appearing on multiple proposals — sub-performer level only, with ARPA-H overlap review
**Appendix A, §5.1 (lines 434–444) — the ONLY explicit cross-proposal rule:**
> "**An organization may serve as a sub-performer under multiple proposals.** If ARPA-H selects two or more proposals in which the same sub-performer is proposed to perform work under the same Technical Area, ARPA-H reserves the sole right to determine whether the proposed efforts are substantially distinct or whether a material overlap exists. In the event ARPA-H determines that such an overlap exists, ARPA-H may, at its discretion, (i) fund the overlapping work only once, or (ii) require the sub-performer to elect the project in which it will participate."

**Key implication:** An organization can be a sub-performer on multiple proposals, but if selected on more than one and doing overlapping work in the same TA, ARPA-H may force an election or fund the work only once. There is NO stated prohibition on being a sub-performer on multiple proposals.

### Individual (PI / Key Personnel) appearing on multiple proposals
**SILENT.** The solicitation contains no explicit rule stating that an individual PI or key personnel member may or may not appear on more than one proposal. The sub-performer overlap rule above applies at the organization level only.

### Prime performer appearing on multiple proposals
**Implicit prohibition by structure.** Each proposal requires "one Principal Investigator under a single prime performer." The overlap/election rule references "sub-performer," strongly implying the drafters contemplated organizations serving as prime on one proposal and sub on another — but no rule explicitly prohibits a single prime from submitting multiple distinct proposals. This is AMBIGUOUS.

### Cross-TA OCI / separation rules
**SILENT on structural TA-level separation.** There is no stated rule that an organization leading TA3 cannot also participate in TA1, or that an "integrating" TA role creates an OCI against a data-generation role. However, the general OCI disclosure requirement applies (see below).

### OCI — general disclosure required
**Appendix C, §3.5:**
> "Through submission of a proposal, the proposer is required to identify and disclose all facts relevant to a potential OCI involving the proposer, its organization, and/or any proposed team member (proposed sub-awardee). Along with the OCI disclosure, the proposer must submit an OCI mitigation plan..."

**Appendix C, §3.6 — ARPA-H Support Services OCI:**
> "ARPA-H restricts Performers from concurrently providing professional support services... to ARPA-H office(s)... the proposer must affirm whether it or any proposed team member (proposed sub-awardee, etc.) is providing professional support services to any ARPA-H office(s) under: (1) a current award or subaward; or (2) a past award or subaward that ended within one calendar year prior to the proposal's submission date."

---

## 5. STAGE DIFFERENCES: SOLUTION SUMMARY vs. FULL PROPOSAL vs. AWARD

### Stage 1 — Solution Summary (due 2026-06-25)
**ISO Main §4.1–4.3 (lines 196–229):**
> "Non-Gated Solution Summary processes involve: Step 1: Submit Solution Summary through the Solutions site. Step 2: Potential proposers are provided feedback encouraging or discouraging the submission of a proposal. **Step 3: Submit Proposals (Potential proposers may submit proposals, regardless of whether encouraged in Step 2).**"

**Content requirements (Appendix B):** Cover page with prime organization, key personnel (name/email/organization), sub-awardee/team member table (organization name + technical POC only — no detailed roles), 5-page narrative covering: Concept Summary, Innovation and Impact, Proposed Work, Team Organization and Capabilities, BOE. UEI not required at this stage ("If already registered, not required at Solution Summary stage").

**Team locking at SS stage:** Sub-awardees are listed by organization name and technical POC. No TA responsibility breakdown is required; no PM/architect named explicitly. The 5-page narrative asks for team organization and key personnel skills in 1-2 sentences each.

**Gantt chart (Appendix C.1, referenced in section heading):** "As Applicable to the proposed TA or TAs" — this language appears in the full proposal (C.1), not the SS. At SS stage the work plan is narrative only.

### Stage 2 — Full Proposal (due 2026-08-06)
**Content requirements (Appendix C.1):** 40-page Technical & Management Proposal. Must include:
- PI identified; team organization with roles and responsibilities
- Named PM with level of effort
- Named software architect (distinct from PI and PM)
- Hours dedicated to integration per year
- Task Description Document (TDD, unlimited pages)
- Price Proposal + Spreadsheet
- Biosketches for all key personnel (NIH format acceptable)
- OCI disclosure and mitigation plan
- Gantt chart (not in page limit)
- SAM.gov UEI required at proposal submission

**Appendix C, §1.1(a) — conforming submission requires:**
> "The submission includes the requirement to address all four Technical Areas and all three Phases in the proposal."
> "The proposer's concept has not received funding or been selected for award negotiations for another funding opportunity (whether from ARPA-H or another government agency)."

**Team finalization:** The full proposal must name all sub-awardees with organization type (for-profit/nonprofit/academia), technical POC, and telephone/email. No explicit statement that the team can be revised between SS and proposal, but the SS is non-binding feedback only.

### Stage 3 — Award
**Appendix A, §5.5 (lines 870–879):**
> "Initially, teams will operate as self-contained units. By Phase III, cross-team collaboration will be required, and APA language will be included in awards to facilitate the open exchange of information."

**ISO §4.4 (lines 253–256):**
> "After completing a Solution Summary review, ARPA-H will notify each proposer whether it is 'encouraged' to or 'discouraged' from submitting a proposal."

**Appendix C, §2.3(a):**
> "The government reserves the right to select for negotiation all, some, one, or none of the proposals received in response to this ISO. In the event the government desires to award only portions of a proposal, negotiations will commence upon selection notification."

**Appendix C, §1.2 (notice of selection):**
> "This notification may indicate that only a part of the effort has been selected for negotiation and may request a revised proposal for only those selected portions, if not apparent through the delineation of proposed tasks."

---

## 6. GOVERNMENT-FURNISHED RESOURCES, CONSORTIUM FORMATION, AND DOWN-SELECT

### Government-Furnished Property
**Appendix C, §3.11:**
> "**Government-furnished property/equipment/information is not expected to be provided to performers.**"

### IV&V — government-contracted, separate from performer teams
**Appendix A, §5.4 (lines 738–758):**
> "ARPA-H will contract with one or more qualiﬁed organizations to provide independent veriﬁcation and validation across the IGoR program." Covers TA1 (mechanistic models) and TA3/TA4 (experimental infrastructure). "**Performers do not need to budget for IV&V partners,** but proposals and budgets should account for the effort required to collaborate with them..."

### Down-select between phases
**Appendix A, §5.3 (lines 494–498):**
> "These represent minimum requirements and serve to bound the scope of the effort while affording maximal ﬂexibility, creativity, and innovation... **Achievement of all metrics, as agreed to by ARPA-H, is the basis for continuation to subsequent phases.**"

Down-select is milestone-gated per phase (18-month Phase I, 18-month Phase II, 24-month Phase III). ARPA-H does not describe an explicit down-select across proposals between phases — continuation within a given award depends on milestone achievement.

### Associate Performer Agreements (APAs)
**Appendix A, §5.5 (lines 871–879):**
> "Associate Performer Agreements (APAs) are agreements between performer teams on a program that establish the terms for sharing information, data, and materials... **APA language will be included in awards** to facilitate the open exchange of information. Each performer will work with other performers to develop an APA that speciﬁes the types of information that will be freely shared across teams."

APAs are required at award; they are not a pre-proposal teaming device. They govern cross-team data sharing (especially TA3 standards, TA4 cross-team lab execution) in Phases II–III.

### Cross-team collaboration expectations (mandatory, not optional)
**Appendix A, §5.5 (lines 849–869):**
> "All performer teams are expected to interact and work collaboratively with other teams in developing methods, technologies, and tools... In particular: Phase I: Domain-Driven Design workshop (program milestone); Phases I–II: TA3 standards working groups (bake-offs, RFC); Phases II–III: cross-team lab execution; Phase III: connect-a-thon."

---

## WHAT THE SOLICITATION IS SILENT OR AMBIGUOUS ABOUT

1. **Individual PI / key personnel on multiple proposals:** The solicitation explicitly addresses organization-level overlap (sub-performer election rule) but is **completely silent** on whether a named individual (PI, key personnel, co-investigator) may appear on more than one IGoR proposal simultaneously. There is no prohibition and no guidance.

2. **Prime organization submitting multiple proposals:** The overlap/election rule specifically says "sub-performer." The solicitation does not explicitly prohibit a single prime from leading more than one IGoR proposal, though the intent of "one PI under a single prime" per proposal strongly implies one proposal per team configuration. **Ambiguous.**

3. **TA-level OCI / structural separation rules:** No rule prohibits an organization contributing to TA3 (protocol standards) from also contributing to TA1 (disease models) within the same team or across teams. The IV&V partner is the only entity with an explicit structural separation (ARPA-H-contracted, outside performer teams). **Silent on cross-TA OCI within the program.**

4. **Teaming finalization deadline:** The solicitation does not state that the team listed in the Solution Summary must be the final team in the Full Proposal. Teams can presumably change personnel between SS and proposal, but this is **not addressed explicitly**.

5. **Whether "encouraged" SS feedback gates proposal submission:** ISO §4.1 states proposals may be submitted "regardless of whether encouraged in Step 2." Whether a discouraged submission can still be selected is not stated. **Ambiguous on practical effect.**

6. **Sub-performer election timing:** If ARPA-H selects two proposals with the same sub-performer in the same TA, the election rule applies. The solicitation does not specify when this determination is made (at selection, during negotiation, at award). **Timing not specified.**

7. **Minimum number of labs for TA1/TA2/TA3:** Only TA4 has an explicit minimum (2 laboratories). TAs 1, 2, and 3 have no stated minimum number of performers or institutions. **Silent.**

8. **Prime organization eligibility on multiple proposals simultaneously:** No rule explicitly prevents an organization from submitting as prime on one proposal and sub-performer on another, or as sub-performer on two proposals simultaneously (beyond the TA-overlap election rule if both are selected).
