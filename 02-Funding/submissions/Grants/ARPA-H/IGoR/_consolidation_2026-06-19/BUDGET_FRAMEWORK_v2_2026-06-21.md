# IGoR Budget Framework v2.2 (2026-06-21)

**Status:** Planning framework for review by Shahin + Ananth; exact figures and F&A finalize in the C4 workbook. Built bottom-up, NOT force-fit to $50M. Roles aligned to Shahin + Matt's 2026-06-21 structure (below). Total ~**$43M**.

**BLUF (3 sentences):** Aligned to the canonical team map: Purdue leads TA1 (Grama + Anne co-lead) AND the TA2 engine (Grama), Cytognosis leads the TA1 disease model and the TA1-to-TA2 hypothesis generation (Shahin), SIFT owns TA2-TA3 + TA3 + TA3-TA4 (Dan), and TA4 has an academic arm (Tegtmeyer) and an industry arm (Cellanome). **Matt is TA4-academic lead AND a TA1 disease-modeling contributor** (he stated disease modeling is where he fits). Purdue's computational line is raised to ~$6.5M (it covers TA1 + the TA2 engine + Purdue's ~57% F&A, so it should not be below SIFT), making Purdue the largest performer at ~$12.5M.

---

## 0. Canonical team / role structure (Shahin + Matt, 2026-06-21) — authoritative

| Scope | Org / lead | Notes |
|---|---|---|
| Lead organization (prime) | Purdue IPAI; PI Ananth Grama | |
| Project Manager | Patricia Purcell | Cytognosis hire |
| Software Engineer / Architect | TBD | Cytognosis hire |
| **TA1** (mechanistic disease model + data-generation framing) | Purdue IPAI (Lead Grama, co-Lead Anne Carpenter) + Cytognosis (Lead Shahin) | Anne is TA1 co-lead (computational morphology), not a separate org |
| **TA1-TA2** (TA1-model-grounded hypothesis generation) | Cytognosis (Lead Shahin) | |
| **TA2** (experiment-design engine) | Co-led: Purdue IPAI (Grama) + Cytognosis (Shahin); optional Phylo later | Both orgs co-lead TA1 and TA2 |
| **TA2-TA3** (incl. user interface) | SIFT (Lead Dan Bryce, Advisor Robert Goldman) | |
| **TA3** | SIFT (Lead Dan Bryce, Advisor Robert Goldman) | |
| **TA3-TA4** | SIFT (Lead Dan) + TA4 partners | |
| **TA4 academic arm** | Purdue (Lead Matthew Tegtmeyer) | iPSC-neuron wet-lab + multimodal readouts; Matt ALSO contributes to TA1 disease modeling |
| **TA4 industry arm** | Cellanome (Lead: TBD) | R3200 |
| **TA4 sequencing/cloud (optional)** | Illumina (Lead James Han, co-Lead Michael Mehan) | PCX-partnership framing: NovaSeq, DRAGEN, ICA; optional/in-kind |
| **TA4-TA1** (data back to the model) | Purdue (Grama, co-Lead Anne) + Cytognosis (Shahin) | |

Refinements vs prior docs (updated 2026-06-21): (a) **TA1 AND TA2 are both co-led by Purdue (Grama) + Cytognosis (Shahin)** — option to add Phylo on TA2 before final submission, or keep a Purdue-engine / Cytognosis-hypothesis split; decide before submission; (b) **Matt spans TA4-academic + TA1 disease modeling**; (c) **TA4-academic is Matt's Purdue department (Biomedical Engineering / neuroscience), NOT IPAI** (IPAI is the AI institute carrying TA1/TA2 computational; confirm Matt's exact dept). Describe contributions by scope/work, not bare TA labels. **Broad/Carpenter collaboration confirmed (acknowledge, no subaward):** Anne Carpenter co-authored NeuroPainting with Matt; cite the Broad Imaging Platform / Cell Painting collaboration as a methodological foundation and team strength. Open: Cellanome TA4-industry lead name; Matt's exact Purdue department.

---

## 1. Restructured performer table (planning 5-yr, fully loaded; finalize in C4)

| Performer / line | 5-yr | ~$/yr | Basis / notes |
|---|---|---|---|
| **Purdue/IPAI — computational (TA1 + TA2 engine)** | ~$6.5M | ~$1.3M | Grama (PI), Anne Carpenter (TA1 co-lead, morphology), 2-3 PhD students, 2 research engineers (TA1/TA2 systems + engine dev), disease-modeling postdoc; **Purdue ~57% F&A** inflates the total. Range $6-7M; should not be below SIFT. |
| **Purdue (Tegtmeyer lab, non-IPAI dept) — TA4-academic** | ~$6.0M | ~$1.2M | Tegtmeyer (lead; also TA1 disease-modeling effort) in his Purdue department (Biomedical Eng / neuroscience, NOT IPAI), iPSC-neuron postdoc, assay-methods PhD, lab tech, 1-2 RAs; Phase I equipment ~$1.4M; wet-lab materials. **May move host if Matt relocates; keep separable.** |
| **= Purdue total (prime)** | **~$12.5M** | **~$2.5M/yr** | Largest line, as the prime should be; 2-3+ RAs/students, likely more. |
| **Cytognosis (TA1 model + TA1-TA2 hypothesis)** | **~$9.5M** | **~$1.9M/yr** | Shahin + Cytognosis-hired PM + SWE + ~5 ML/comp-bio (see §2). Market Bay-Area rates; low 15% de minimis F&A; shared compute moved out. |
| **SIFT (TA2-TA3 + TA3 + TA3-TA4)** | **$7.0M** | ~$1.4M/yr | Dan's real cost (24,204 hrs; DL $4.09M, indirect $2.20M, travel $69.7K, fee $0.64M). |
| **Cellanome (TA4-industry)** | **~$6.0M** | ~$1.2M/yr | R3200 RENT-and-we-run base case (§3); confirm with a quote. |
| **Shared program compute (GPU/cloud; TA1 + TA2)** | ~$2.5M | | Program line serving the model + engine (not loaded onto one org). |
| **TA4 sequencing (service/CRO line)** | ~$2.0M | | scRNA-seq + Perturb-seq; NovaSeq X+ ~$2,050/1.25B-read lane; CRO subaward w/ quote. Illumina optional in-kind. |
| **McLean / HMS** | $0.7M | | Ruzicka clinical + data governance (minor sub; floor n/a). |
| **Duane Valz — legal/IP** | ~$0.2M | | nonprofit rate x scoped hours (§4). |
| **Cross-team / integration / reserve** | ~$2.5M | | DDD workshop, bake-offs, connect-a-thon, ~6% reserve. |
| **Phylo / Illumina (as partners)** | dropped | | Phylo not budgeted; Illumina optional in-kind only. |
| **TOTAL (planning)** | **~$43M** | | Bottom-up; Purdue largest; each main org ~$1.2-2.5M/yr. |

### What was going on with "Purdue TA1 too low" (now fixed)

I had Purdue computational at $4.5M because I (a) under-counted headcount and (b) treated TA2 as Cytognosis-led. Correcting both: **Purdue leads TA1 computational AND the TA2 experiment-design engine**, staffed by Grama + Anne + 2-3 PhD students + 2 research engineers + a disease-modeling postdoc, and Purdue's **~57% F&A** roughly multiplies the direct base by 1.57. That lands ~$6.5M (range $6-7M), correctly above SIFT.

### Why Cytognosis (~$9.5M) is fair, not inflated

Deepest technical core (TA1 disease model + TA1-TA2 hypothesis generation); Bay-Area senior ML salaries run ~2-3x academic, but Cytognosis bills only **15% de minimis F&A vs Purdue's ~57%**, so its true overhead is far lower; and the shared GPU/cloud compute (~$2.5M) is now a program line, not loaded on Cytognosis. Net: **Purdue (prime) is the largest**, Cytognosis sits with the other majors.

---

## 2. Cytognosis roster — per-phase FTE, level, task->cost (Cytognosis-hired)

PM and SWE are Cytognosis hires; Shahin explicit. Loaded Bay-Area rates + 15% de minimis. Shared compute is the program line (§1), not here. Cytognosis scope = TA1 disease model + TA1-TA2 hypothesis generation (TA2 engine is Purdue-led).

| Role (level) | FTE PhI / PhII / PhIII | Assigned tasks | ~Loaded $/yr |
|---|---|---|---|
| **Shahin Mohammadi** (CEO; TA1 lead, TA1-TA2 hypothesis lead, semantic-foundation co-lead) | 0.5 / 0.5 / 0.5 | TA1 architecture; 3-latent SCM; genomic-factorization direction; hypothesis generation; semantic foundation | ~$140K (0.5 FTE × $228K Rung-1 cap base + fringe + OH) |
| **Software & Systems Architect** (senior; Cytognosis hire) | 1.0 / 1.0 / 1.0 | TA1-TA2 interface; LinkML/Biolink schema; open-source release; infra | ~$250K |
| **Project Manager — Patricia Purcell** (Cytognosis hire) | 0.3 / 0.3 / 0.3 | Cross-TA coordination, delivery tracking, ARPA-H reporting, milestone docs | ~$80K |
| **Senior ML/AI Engineer** (TA1) | 1.0 / 1.0 / 1.0 | Causal generative model + SCM; treatment-embedding language (innov. 2); graph-wavelet GNN (innov. 5) | ~$260K |
| **ML Research Scientist** (TA1) | 1.0 / 1.0 / 1.0 | Genomic factorization on genomic FMs (AlphaGenome/VariantFormer, innov. 4); factorized-PRS; disease axes | ~$240K |
| **Computational Biologist #1** (TA1) | 1.0 / 1.0 / 1.0 | Residual-space cellular-clinical alignment via OT/MMD (innov. 1); pipelines | ~$210K |
| **Computational Biologist #2** (TA1; ramps in) | 0 / 1.0 / 1.0 | Bipolar extension; TransBox ontology embeddings + OOD head (innov. 3) | ~$210K |
| **Research Scientist — eval** (TA1-TA2) | 1.0 / 1.0 / 1.0 | Hypothesis-tournament eval; VOI scoring; benchmarks | ~$120K |
| **Cytognosis FTE total** | ~5.8 / ~6.8 / ~6.8 | | ~$9.5M 5-yr |

**Rate-setting principle (all orgs):** Shahin's comp is finalized as a 3-rung ladder (Rung 1 = the $228K HHS cap, current); the IGoR federal charge = $228K × effort. Set every role's rate by **experience level, consistent across organizations**, adjusted for **location** (Bay Area for Cytognosis vs West Lafayette for Purdue) using standard, data-backed locality differentials (BLS/OEWS metro wages, locality/COL indices), so no org is an outlier for equivalent seniority.

## 3. Cellanome (TA4-industry) — three scenarios off confirmed ~$425K instrument

| Scenario | Planning 5-yr | What it is |
|---|---|---|
| **BUY (in-house capex)** | TCO ~$0.7-1.1M + experiments | R3200 (~$425K) + maintenance ($40-60K/yr) + reagents ($2-5K/expt) + off-instrument sequencing (~$1/cell). |
| **RENT (placed, we run)** — recommended base | ~$5-6M | Cellanome places an R3200 in a PsychIGoR lab (~$200-300K placement) + reagents + our labor; negotiate. |
| **SERVICE (they/CRO run)** | ~$6-7M+ | Ship materials; Cellanome or the new Psomagen CellCage CRO runs it (pilots ~$15-40K; genome-scale $200K-1M+). |

Confirmed: R3200 ~$425K (GenomeWeb AGBT 2026); consumables undisclosed. Get a Cellanome BD + Psomagen quote. PCX is NOT a sequencing comparator (it harmonizes existing clinical data).

## 4. Duane Valz — legal/IP line (fair; don't lose him)

Per Duane's contract: **$750/hr regular, $500/hr nonprofit.** Use **$750/hr** for this proposal (per Shahin; the work spans for-profit-relevant IP/commercialization and we want to keep him well-treated). Allocation: model as an **hourly consultant line** (most flexible), not a fixed % FTE; optionally a small not-to-exceed retainer per phase. Scope -> hours: OT agreement review (~40-60 h, Phase I), IP strategy + field-of-use (~30-40 h), subaward/teaming legal + Cellanome NDA (~20-30 h), data/IP-flow + OSS licensing (~10-15 h/yr). Total ~150-300 h over 5 yr -> **~$0.15-0.25M at $750/hr**. Tag Duane (scope) + Ananth (verify). Bill through Cytognosis.

## 5. Matt Tegtmeyer — expertise alignment (web-verified 2026-06-21)

**Verdict: confirmed.** Matt is an Assistant Professor at Purdue (PhD 2023, Broad/Stanley Center, Nehme lab with McCarroll), with a **secondary appointment in Computational and Systems Biology** and a primary one in Integrative Neuroscience. He is first author of NeuroPainting (Tegtmeyer et al., *Nat Commun* 2025; iPSC-NGN2 neurons + astrocytes, Cell Painting morphology + scRNA-seq across 44 donors for the 22q11.2 deletion, with Random-Forest classification), and of an earlier phenomics paper (*Nat Commun* 2024). This supports him as **lead of the TA4-academic experimental arm** AND as a credible **TA1 disease-modeling contributor** at the interpretive end (cellular phenotype to disease mechanism); TA1 modeling leadership stays with Grama/Cytognosis.

**Broad/Carpenter collaboration is real and direct (acknowledge as a strength, no subaward):** Anne Carpenter, Shantanu Singh, and Beth Cimini (all Broad Imaging Platform) are **co-authors with Matt on NeuroPainting**; NeuroPainting adapts Carpenter's Cell Painting to neurons. This means our cellular team (Matt + Anne) has **already collaborated and published together** on exactly the iPSC-neuron multimodal phenotyping IGoR needs, which materially strengthens the "one integrated team" narrative. Acknowledge the Broad Imaging Platform collaboration as the methodological foundation; keep all of it in-house at Purdue/IPAI for the award (no Broad budget line).

**Bio capability statement (proposal-ready):** "Dr. Matthew Tegtmeyer (Assistant Professor, Purdue) is the developer of NeuroPainting, a scalable high-content morphological profiling platform for iPSC-derived neural cell types (*Nature Communications*, 2025). His lab integrates morphological phenotyping with single-cell transcriptomics to map the cellular consequences of neuropsychiatric risk variants, including the 22q11.2 deletion, across neurons, progenitors, and astrocytes at cohort scale."

## 6. Decisions for Shahin + Ananth

1. **Total ~$43M** bottom-up (range $40-46M); confirm the IGoR per-award ceiling.
2. **Purdue computational ~$6.5M** (TA1 + TA2 engine), above SIFT; confirm RA/student count (scalable).
3. **Matt** = TA4-academic lead + TA1 disease-modeling contributor; confirm effort split (or define TA4 broadly).
4. **Cellanome** RENT-and-we-run base (~$5-6M); get quotes. Name the Cellanome TA4-industry lead.
5. **Sequencing CRO ~$2.0M**; Matt + Cellanome size volumes. Illumina optional in-kind (PCX framing).
6. **Duane** nonprofit rate + hours. **Broad collaboration** acknowledgment for Matt/Anne: decide.

## 7. Resource / cost sharing (research-verified 2026-06-21)

- **Status:** the ISO lists "Resource sharing: **Encouraged**" = a PREFERENCE, not a requirement. But it MUST be quantified in the BOE and the C.3 Price Proposal with a Government/Performer split that sums to 100% (no minimum %). As a university + nonprofit team (both nontraditional), the statutory prototype-OT cost-share is waived; any share is discretionary and competitive. It is not an explicit scored sub-criterion (Criterion 4 = cost is lowest-weighted), but a credible share supports the required "taxpayer value proposition."
- **Recommended package (target ~5-10%, ~$2-5M on the award):**
  - IPAI/Purdue **HPC compute** (Anvil/Brown) in-kind: **~$1.5-2.0M** (valued at NSF ACCESS allocation rates; dedicated, verifiable).
  - Purdue **wet-lab facilities** for the Tegtmeyer arm: **~$150K** (facility usage credit).
  - Cellanome **instrument/run credits**: **~$160K** (needs a commitment letter; clear with Duane under the NDA + keep separate from the Cellanome sub so no fee stacks).
  - Do NOT include Anne's non-dedicated effort or Cytognosis background IP (rated low-quality / contestable by AOs).
- **Interaction with the budget:** if IPAI HPC is contributed in-kind, shift part of the "shared program compute (~$2.5M)" line from direct cost to in-kind. **Decide the target % with Ananth** (a formal Purdue match letter unlocks ~10%); confirm the Cellanome in-kind with Duane.

## 8. PM + SWE/Architect (research-validated 2026-06-21)

- **PM dedication:** Appendix A §5.5 requires "a Project Manager with project management expertise and **sufficient level of effort**" for cross-TA coordination, delivery tracking, and reporting. **NOT 100% FTE.** ~0.3 FTE (Patty, ~400 hrs/yr) is defensible; tie it explicitly to those three functions in the narrative, and note PI Grama carries inter-org coordination.
- **SWE/Architect is REQUIRED, not optional:** §5.5 also requires a Software Architect distinct from PI and PM with API-first systems experience. So the 1.0 FTE SWE/Architect (Cytognosis hire) is mandated.
- **Pricing validated (Bay Area, loaded):** PM ~$80K/yr (0.3 FTE at ~$200/hr loaded) is below a full-time nonprofit PM (~$155K loaded). SWE/Architect ~$250K/yr is the low end of the senior Bay-Area market; base (~$200K) is under the $228K cap. Senior ML engineer ~$260K and ML/comp-bio ~$210-240K are market. Prior Cytognosis grants (Google Impact, LTFF, Coefficient, AWS Imagine) used far leaner rosters (PI + ~1 engineer at a ~$100K mission-driven nonprofit rate); IGoR's market rates and ~6.8 FTE are appropriate and explained by a $50M federal program's scope. NONE of those prior grants carried a PM or a named SWE/Architect, so both are IGoR-driven additions.

---

## 9. Salary-cap (HHS Executive Level II) compliance — which positions are legally bound

**Rule.** ARPA-H program funds may not pay **direct salary** above the **Federal Executive Schedule Level II** rate, **$228,000/yr** for 2026 obligations (NIH NOT-OD-26-034, eff. 2026-01-11), incorporated into this award via the OT Model Agreement (Appendix E). The cap is on the **direct-salary rate, prorated by committed effort**. It does NOT limit fringe, F&A/indirect, or commercial fee, and it does NOT limit an individual's total institutional compensation (only the federally funded direct-salary share). Controlling figure = the Exec Level II rate **at the time of obligation** (confirm the then-current rate at award).

**BOUND (institutional base > cap → must charge at the capped rate x effort):**

| Person | Base (est.) | Effort | ARPA-H direct salary (capped) | Status |
|---|---|---|---|---|
| Ananth Grama (Purdue/IPAI) | ~$320K | 0.25 | $228K x 0.25 = ~$57K/yr | Respected (cost model Table 3 + SS BOE) |
| Anne Carpenter (Purdue/IPAI) | ~$300K | 0.25 | ~$57K/yr | Respected |
| W. Brad Ruzicka (McLean/HMS) | ~$250K | 0.20 | ~$45.6K/yr | Respected |

Purdue and McLean cover the remainder from institutional funds. These three are already capped correctly in the cost model and the SS.

**AT CAP (base = cap exactly; charge cap × effort):**

- **Shahin Mohammadi (Cytognosis CEO):** comp Rung 1 base = the $228K cap exactly, so charge $228K × effort (treat as at-cap); Rungs 2/3 ($270K/$350K) above the cap are funded from unrestricted funds, never from the award.

**NOT bound (base <= cap; fund normally):** Tegtmeyer (~$220K, close — re-check if his base rises above the cap) and the other Cytognosis hires. **Important nuance:** the cap is on **base direct salary**, not the loaded rate, so a Cytognosis hire whose loaded rate is ~$250-260K is fine **as long as base < $228K**; verify each hire's base stays under the cap. PhD students, postdocs, and lab techs are far below.

**NEEDS a counsel + contracts determination (flag Duane + Purdue SPS):** commercial subcontractors (SIFT, Cellanome, Illumina, Phylo) bill fully-loaded commercial rates; whether/how the Exec-Level-II cap applies to the direct-salary component of a commercial OT sub's high earners is an OT-specific question. Do NOT assume; confirm with Duane and the Purdue contracts office before finalizing those rates.

**Action:** (1) the three bound academics are capped correctly; (2) verify Cytognosis hires' BASE salaries stay under $228K; (3) get the commercial-sub treatment confirmed by Duane + contracts; (4) re-confirm the Exec Level II rate at obligation.

---

*External figures (2026-06-21): R3200 ~$425K (GenomeWeb AGBT 2026); NovaSeq X+ ~$2,050/1.25B-read lane (UW-Madison core); Psomagen CellCage CRO (Mar 2026); PCX = $50M pediatric data-interoperability program; resource sharing "Encouraged" per ISO; PM "sufficient level of effort" per Appendix A §5.5; Duane $750/$500 per contract; salary cap $228K Exec Level II per NIH NOT-OD-26-034. Full source lists in the session research briefs.*
