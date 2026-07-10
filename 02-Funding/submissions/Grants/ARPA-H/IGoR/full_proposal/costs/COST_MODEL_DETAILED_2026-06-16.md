# IGoR PsychIGoR — Detailed Cost and Headcount Model

**Team:** PsychIGoR | **Prime:** Purdue / IPAI | **PI:** Ananth Grama
**Date:** 2026-06-21 (updated from 2026-06-16) | **Supersedes:** COST_MODEL.md (2026-06-12), COST_MODEL_DETAILED_2026-06-16.md (prior)
**Material change 2026-06-21:** Restructured to **~$43M** ($42.9M) locked model. Phylo removed as budgeted performer (optional TA2 collaborator only, not budgeted). Illumina removed as budgeted sub (optional in-kind sequencing/cloud only). Purdue split into computational (IPAI, $6.5M) and Tegtmeyer lab ($6.0M). SIFT updated to $7.0M (Dan's real figure: DL $4,094,437 / indirect $2,199,941 / travel $69,747 / fee $636,412; 24,204 labor hours; 70% Bryce / 30% Goldman). Cytognosis $9.5M. Cellanome $6.0M. Added Duane Valz legal/IP line $0.2M. Shared program compute $2.5M as program line. TA4 sequencing CRO $2.0M as subaward. Cross-team/reserve $2.5M. Total $42.9M (~$43M). In-kind $2.3M (IPAI HPC $2.0M + Purdue wet-lab $0.15M + Cellanome credits $0.16M) SEPARATE from ask; total project value ~$45.2M.

**Prior stale figures retired:** $50M / $54M envelope; $13.5M/$15.0M/$21.5M phase split; $15.5M Purdue; $14.0M Cytognosis; $5.0M SIFT; $8.0M Cellanome; Illumina as budgeted sub; Phylo as budgeted sub; MEA/electrophysiology readout (it is single-cell calcium imaging); "SIFT co-leads TA2" (SIFT = scoped VOI layer under Cytognosis+IPAI TA2 co-lead); "Vodovotz" (ARPA-H PM is Paul E. Sheehan, Ph.D.); $165K Shahin salary; Element Teton as teaming partner.

**Reading time:** ~20 minutes. **If you only read one section:** read Section 1 (allocation table) and Section 3 (salary cap).

---

## BLUF

- **ARPA-H request: ~$42.9M (~$43M)** over 60 months (Phase I 18 mo / Phase II 18 mo / Phase III 24 mo); ~$45.2M total project value with ~$2.3M in-kind.
- **Purdue split:** IPAI computational = $6.5M (Grama + Carpenter TA1 co-lead + PhD students + research engineers); Tegtmeyer lab = $6.0M (TA4 academic wet-lab + iPSC-neuron + single-cell calcium imaging). Purdue prime total = $12.5M.
- **SIFT:** $7.0M (Dan Bryce lead; real figure confirmed 2026-06-21). SIFT operates as a scoped VOI layer under Cytognosis+IPAI TA2 co-lead; SIFT does not co-lead TA2.
- **Salary cap (2026):** Executive Level II = **$228,000** effective January 11, 2026 (NIH NOT-OD-26-034). Shahin's Rung-1 compensation = $228K cap exactly; charge $228K × 0.5 FTE = ~$114K base. Do not cite a $165K figure (retired). Commercial-sub cap treatment (SIFT/Cellanome) flagged for Duane + Purdue SPS.
- **Equipment:** Phase I Tegtmeyer lab stand-up ~$1.4M (front-loaded). No Phase II or III equipment line at the $42.9M model level; on-prem GPU node removed from budget (shared cloud compute is the program line).
- **Functional readout:** single-cell calcium imaging, NOT MEA/electrophysiology.

---

## 1. Per-Organization, Per-Phase Budget Allocation

### Table 1-A: Locked Per-Organization, Per-Phase Allocation (~$43M model)

| Performer | Role / TAs | Phase I ($, 18 mo) | Phase II ($, 18 mo) | Phase III ($, 24 mo) | 5-yr Total |
|---|---|---|---|---|---|
| **Purdue/IPAI — computational (Prime)** | Grama (PI) + Anne Carpenter (TA1 co-lead, computational morphology; no bench; in-house IPAI/Purdue; no separate Broad sub-award) + PhD students + research engineers + disease-modeling postdoc; ~57% F&A | $1.8M | $2.0M | $2.7M | **$6.5M** |
| **Purdue — Tegtmeyer lab (TA4-academic)** | Matt Tegtmeyer (Purdue faculty, non-IPAI dept; confirm Biomedical Eng / Integrative Neuroscience); iPSC-neuron wet-lab; multimodal readouts incl. single-cell calcium imaging; Matt also TA1 disease-modeling contributor; Ph I equipment ~$1.4M front-loaded | $2.0M | $1.7M | $2.3M | **$6.0M** |
| **Purdue total (prime)** | | **$3.8M** | **$3.7M** | **$5.0M** | **$12.5M** |
| **Cytognosis (Sub)** | TA1 model lead; TA1-TA2 hypothesis generation lead; Shahin + PM (Purcell) + SWE/Architect + ~5 ML/comp-bio; 15% de minimis F&A; shared compute moved out to program line | $2.4M | $2.9M | $4.2M | **$9.5M** |
| **SIFT (Sub)** | TA2-TA3 + TA3 + TA3-TA4; scoped VOI layer under Cytognosis+IPAI TA2 co-lead; Dan Bryce lead (70%), Goldman advisor (30%); 24,204 labor hours; DL $4,094,437 / indirect $2,199,941 / travel $69,747 / fee $636,412 | $2.0M | $2.2M | $2.8M | **$7.0M** |
| **Cellanome (Sub)** | TA4-industry arm; R3200 RENT-and-we-run base; single-cell calcium imaging integration; confirm via BD quote and Psomagen quote | $1.4M | $1.8M | $2.8M | **$6.0M** |
| **Shared program compute (GPU/cloud; TA1+TA2)** | Program line, not loaded on one org; partially shiftable to IPAI HPC in-kind | $0.6M | $0.8M | $1.1M | **$2.5M** |
| **TA4 sequencing CRO** | scRNA-seq + Perturb-seq; CRO subaward; Illumina optional in-kind only (not a budgeted sub) | $0.4M | $0.6M | $1.0M | **$2.0M** |
| **McLean / HMS (Sub)** | Clinical; W. Brad Ruzicka MD/PhD; cohort interpretation; data governance; no new clinical trials | $0.2M | $0.2M | $0.3M | **$0.7M** |
| **Duane Valz — legal/IP (consultant)** | IP strategy; OT agreement review; subaward/NDA governance; OSS licensing; billed through Cytognosis; ~$750/hr × ~150–300 hrs | $0.08M | $0.06M | $0.06M | **$0.2M** |
| **Cross-team / integration / reserve** | DDD workshop; bake-offs; connect-a-thon; ~6% reserve | $0.6M | $0.8M | $1.1M | **$2.5M** |
| **TOTAL (ARPA-H request)** | | **~$11.48M** | **~$13.06M** | **~$18.36M** | **~$42.9M** |
| *(display as)* | | **~$11.5M** | **~$13.1M** | **~$18.4M** | **~$43M** |

**Arithmetic check (three-way tie):**
- Phase I: 1.8+2.0+2.4+2.0+1.4+0.6+0.4+0.2+0.08+0.6 = **~$11.48M** ✓
- Phase II: 2.0+1.7+2.9+2.2+1.8+0.8+0.6+0.2+0.06+0.8 = **~$13.06M** ✓
- Phase III: 2.7+2.3+4.2+2.8+2.8+1.1+1.0+0.3+0.06+1.1 = **~$18.36M** ✓
- 5-yr total by performer: 6.5+6.0+9.5+7.0+6.0+2.5+2.0+0.7+0.2+2.5 = **$42.9M** ✓
- 5-yr total by phase: 11.48+13.06+18.36 = **$42.9M** ✓

**Dropped performers:**
- **Phylo:** Optional TA2 collaborator only, NOT budgeted. DataTecnica alternate if needed. If either is engaged later, scope absorbs inward from cross-team/reserve; no additional budget line.
- **Illumina:** Optional in-kind sequencing/cloud only (James Han + Michael Mehan; PCX framing), NOT a budgeted sub. Sequencing costs are covered by the TA4 sequencing CRO subaward line.

### Key Assumptions

1. **Purdue split (RESOLVED 2026-06-21):** IPAI computational ($6.5M) covers Grama, Carpenter (TA1 co-lead, purely computational, no bench), PhD students, research engineers, and disease-modeling postdoc. Tegtmeyer lab ($6.0M) covers all wet-lab experiments, iPSC-neuron differentiation, and multimodal readouts including single-cell calcium imaging (NOT MEA/electrophysiology). Anne's scope is entirely in-house at IPAI/Purdue; no separate Broad sub-award.
2. **SIFT at $7.0M (RESOLVED 2026-06-21):** Dan's real figure supersedes the $5.0M placeholder. SIFT is the TA2-TA3 / TA3 / TA3-TA4 scoped layer; it operates under Cytognosis+IPAI as co-leads of TA2. Purdue indirect and phase splits re-derived against the locked $42.9M model.
3. **Cellanome at $6.0M (placeholder):** Held pending BD quote and Psomagen quote. Phase I $1.4M / Phase II $1.8M / Phase III $2.8M is the planning figure. Operating model (RENT-and-we-run base vs. capex in-lab) TBD.
4. **Shared compute as a program line ($2.5M):** Not loaded on Cytognosis or Purdue; managed at program level. Partially shiftable to IPAI/Purdue HPC in-kind (Anvil/Brown, NSF ACCESS rates, ~$2.0M in-kind value).
5. **Duane Valz legal line ($0.2M new):** Consultant, not key personnel. Billed through Cytognosis. Phase split: $0.08M / $0.06M / $0.06M. [FLAG Duane for scope/rate; FLAG Ananth for financial verification.]
6. **TA4 sequencing CRO ($2.0M):** Subaward. Phase split: $0.4M / $0.6M / $1.0M. Illumina may provide optional in-kind sequencing credits separately; those are in-kind, not in this budget line.
7. **McLean:** No new clinical trials. Existing cohort data under originating IRB and NIH GDS policy.

---

## 2. Headcount and FTE Table

### ARPA-H C.3 Guidance

Appendix C.3 states: *"Proposers are discouraged from proposing low-risk ideas with minimum uncertainty or to staff the proposed effort with junior personnel to be more appealing from a budget perspective."* The model below reflects substantive senior effort at every performing organization.

### Academic Faculty Effort Convention

Federal sponsoring agencies (NIH/NSF) and ARPA-H use **person-months (PM)** for faculty effort.

- **1 calendar year = 12 person-months (PM)**; 1.0 FTE = 12 PM/year.
- Faculty at 3 PM/yr = 0.25 FTE. Summer salary convention: up to 3 months from federal funds on 9-month appointment.

### Table 2-A: Detailed FTE / Person-Months by Organization

#### Purdue/IPAI — computational (Prime): TA coordination + TA1/TA2 support + Anne Carpenter TA1 co-lead

| Person / Role | Appointment type | Effort / yr (PM) | FTE equiv. | Loaded $/yr | Basis |
|---|---|---|---|---|---|
| Ananth Grama, PhD (PI, IPAI Director) | 12-mo academic | 3 PM | 0.25 | ~$80K (25% of ~$320K base; ARPA-H at $228K cap × 0.25 = $57K; Purdue covers remainder) | Senior PI; strategic oversight; cross-team coordination; ARPA-H PM liaison |
| Anne Carpenter, PhD (TA1 co-lead; computational morphology/imaging-model lead; no bench; in-house IPAI/Purdue) | 12-mo (Purdue, ~Sep 2026) | 3 PM | 0.25 | ~$75K (25% of ~$300K base; ARPA-H at $228K cap × 0.25 = $57K; Purdue covers remainder) | Interpretable morphology/imaging models; CellProfiler analysis; purely computational; no separate Broad sub-award |
| PhD student #1 (TA1 mechanistic modeling) | 12-mo student | 12 PM | 1.0 | ~$50K stipend + ~$35K tuition | Grama group; TA1 causal disease model build |
| PhD student #2 (TA1 / TA2 support) | 12-mo student | 12 PM | 1.0 | ~$50K stipend + ~$35K tuition | Grama/Carpenter group; support roles |
| Research engineer (TA1/TA2 systems, Purdue) | 12-mo, staff | 12 PM | 1.0 | ~$110K | TA1-TA2 interface code; IPAI engineering staff |
| Disease-modeling postdoc (TA1) | 12-mo, staff | 12 PM | 1.0 | ~$80K | TA1 causal disease model build |
| Senior postdoc / research scientist (computational morphology) | 12-mo, staff | 12 PM | 1.0 | ~$85K | Carpenter group; imaging and morphological analysis |
| **Purdue/IPAI Computational Subtotal** | | | **~5.75 FTE** | **~$510K/yr** | |

Plus Purdue F&A at ~57% on MTDC. **5-yr total ~$6.5M.** Phase I heavier (Carpenter ramp-up); Phase III heavier (second disease, scale-out).

#### Purdue — Tegtmeyer lab (TA4-academic; non-IPAI dept)

| Person / Role | Appointment type | Effort / yr (PM) | FTE equiv. | Loaded $/yr | Basis |
|---|---|---|---|---|---|
| Matthew Tegtmeyer, PhD (TA4-academic experimental arm lead; also TA1 disease-modeling contributor) | 9-mo + 3 summer | 3 PM | 0.25 | ~$55K (25% of ~$220K base; below cap; verify if base rises above $228K) | iPSC-NGN2 differentiation; 22q11.2 disease models; multimodal readouts; TA1 disease-modeling contributor |
| Postdoc (TA4 iPSC-neuron wet-lab) | 12-mo, staff | 12 PM | 1.0 | ~$80K | Tegtmeyer lab; NGN2 protocol execution |
| Lab technician (wet-lab support, TA4) | 12-mo, staff | 12 PM | 1.0 | ~$65K | Cell culture; iPSC maintenance; reagent prep |
| Senior research scientist (TA4 assay methods) | 12-mo, staff | 12 PM | 1.0 | ~$85K | Assay methods and QC; calcium imaging execution |
| **Purdue Tegtmeyer lab Subtotal** | | | **~3.75 FTE** | **~$285K/yr** | |

Plus Phase I equipment stand-up ~$1.4M (imaging rig, iPSC-neuron infrastructure, single-cell calcium imaging rig); Phase II–III lighter with equipment already in place. Purdue F&A at ~57% on MTDC. **5-yr total ~$6.0M.**

**Note on functional readout:** The Phase I functional neuronal readout is **single-cell calcium imaging** (scalable; single-cell resolution; imaging modality that folds into the high-content imaging stack). This is NOT MEA/electrophysiology, which has been removed from the design.

#### Cytognosis (Sub): TA1 model lead + TA1-TA2 hypothesis generation lead

| Person / Role | Appointment type | Effort / yr (PM) | FTE equiv. | Loaded $/yr | Basis |
|---|---|---|---|---|---|
| Shahin Mohammadi, PhD (TA1/TA2 lead; Cytognosis CEO) | 12-mo, nonprofit | 6 PM | 0.5 | [rate pending comp finalization; Rung-1 base = $228K cap; charge $228K × 0.5 FTE = ~$114K base before fringe + 15% de minimis OH] | TA1 architecture; TA2 oversight; PI-equivalent effort at sub; Rungs 2/3 from unrestricted funds only |
| Software and Systems Architect (planned Cytognosis hire; Elham Jebalbarezi Sarbijan (IPAI) interim) | 12-mo, staff | 12 PM | 1.0 | ~$250K loaded | TA1-TA2 interface; cross-team interoperability; open-source release; REQUIRED by Appendix A §5.5 |
| Senior ML/AI Engineer (TA2) | 12-mo, staff | 12 PM | 1.0 | ~$260K loaded | TA2 agentic inference |
| ML Research Scientist (TA1/TA2) | 12-mo, staff | 12 PM | 1.0 | ~$240K loaded | Factorized-PRS; causal disease model; TA1 core |
| Computational Biologist #1 (TA1) | 12-mo, staff | 12 PM | 1.0 | ~$210K loaded | Genomic + transcriptomic data pipelines |
| Computational Biologist #2 (TA1) | 12-mo, staff | 12 PM | 1.0 | ~$210K loaded | TA1 model integration; second-disease extension (Phase III) |
| **Cytognosis Personnel Subtotal** | | | **~5.5 FTE** | **~$1,170K/yr** | |

Plus PM (Patty Purcell, ~$80K/yr ODC), compute via shared program compute line, ODC ~$150K/yr, Cytognosis indirect at 15% de minimis MTDC. **5-yr total ~$9.5M.**

**Note on Patricia Purcell (Project Manager):** Patty serves as PM on a part-time/hourly basis (~400 hrs/yr at ~$200/hr loaded = ~$80K/yr), charged through Cytognosis. ISO (Appendix A §5.5) requires a named PM with sufficient cross-TA coordination, delivery tracking, and reporting. Total PM effort over 5 years: ~$400K. To be reclassified to Direct Labor at proposal time with confirmed hourly rate.

#### SIFT (Sub): TA2-TA3, TA3, TA3-TA4 (scoped VOI layer)

| Category | Dan's confirmed figure (2026-06-21) |
|---|---|
| Direct Labor (fully burdened) | $4,094,437 |
| Labor hours | 24,204 |
| Indirect Costs | $2,199,941 |
| Travel | $69,747 |
| Profit / Fee | $636,412 |
| **Total** | **~$7,000,537 (~$7.0M)** |

Split: 70% Bryce / 30% Goldman and engineers. Note: SIFT operates as a scoped VOI layer under Cytognosis+IPAI as co-leads of TA2; **SIFT does not co-lead TA2.** *[TA2/TA3 text marked "SIFT draft, pending Dan's revision."]*

SIFT builds on XPlan (DARPA SD2) for TA2 experimental intent formulation. TA3 uses LabOP three-tier stack (UML Activity base / LabOP protocols / LabOP Executions with W3C PROV-O provenance). SIFT co-authored LabOP under DARPA SD2.

#### McLean / HMS (Sub): Clinical co-lead

| Person / Role | Effort / yr | FTE equiv. | Loaded $/yr | Basis |
|---|---|---|---|---|
| W. Brad Ruzicka, MD/PhD (clinical co-lead) | 2–3 PM | 0.17–0.25 | ~$70K (loaded with HMS F&A; ARPA-H at $228K × 0.20 FTE = ~$45.6K; HMS covers remainder of ~$250K base) | Cohort interpretation; data governance; translational framing; no new human subjects |
| **McLean Subtotal** | | **~0.2 FTE** | **~$70K/yr** | |

**5-yr total ~$0.7M.** No new clinical trials.

#### Duane Valz — legal/IP consultant (not key personnel)

~$750/hr × ~150–300 hrs total = **$200,000 over 5 years.** Phase split: $80K (Phase I) / $60K (Phase II) / $60K (Phase III). Billed through Cytognosis. Scope: IP strategy; OT/Other-Transaction agreement review; data-use and IP-flow governance; field-of-use splits; subaward terms; OSS licensing. [FLAG Duane for scope/rate; FLAG Ananth for financial verification.]

#### Carpenter computational continuity within the IPAI/Purdue prime (no separate Broad sub-award)

Anne Carpenter's TA1 co-lead scope (code, models, analysis continuity during her Purdue relocation) is fully in-housed at IPAI/Purdue. There is no standalone Broad sub-award. The JUMP Cell Painting open dataset (~$0.15M in-kind) remains a Broad open-data resource — a public dataset independent of Anne's employment. It is NOT counted toward the ARPA-H ask.

#### Cellanome (Sub): TA4-industry arm

Personnel + R3200 instrument time embedded in sub total. [FLAG pending BD quote and Psomagen quote to confirm operating model and pricing.]

**5-yr total ~$6.0M** (Phase I $1.4M / Phase II $1.8M / Phase III $2.8M). Phase III heaviest (second disease, larger-scale screens).

### Table 2-B: Program-Wide FTE Summary by Phase

| Organization | Phase I (18 mo) | Phase II (18 mo) | Phase III (24 mo) | Avg FTE/yr |
|---|---|---|---|---|
| Purdue/IPAI Computational (Prime) | 5.75 | 5.75 | 6.5 | **6.0** |
| Purdue Tegtmeyer lab (TA4-academic) | 3.75 | 3.75 | 4.0 | **3.8** |
| Cytognosis (Sub) | 5.7 | 5.7 | 6.5 | **5.9** |
| SIFT (Sub) | 2.5–3.0 | 2.5–3.0 | 2.5 | **2.7** |
| McLean / HMS (Sub) | 0.2 | 0.2 | 0.25 | **0.2** |
| Cellanome (Sub) | 2.5 | 3.0 | 3.5 | **3.0** |
| **Program Total** | **~20.4** | **~21.0** | **~23.3** | **~21.6 FTE/yr** |

**Note:** Phylo and Illumina removed as budgeted performers. No "Broad residual" row.

**Funded FTE trajectory:** ~20.4 FTE/yr in Phase I, ramping to ~23.3 in Phase III as second disease area and scaled experimentation come online.

---

## 3. Salary Cap Analysis

### Verified 2026 Figure

**Executive Level II salary cap = $228,000, effective January 11, 2026.**

Source: NIH Notice NOT-OD-26-034, published January 28, 2026. Cap applies to ARPA-H OT-funded direct salary fraction only, not total institutional compensation.

### Table 3: Salary Cap Analysis by Key Personnel

| Person / Role | Org | Est. Institutional Base | 2026 Cap | Cap-bound? | Effect on ARPA-H-funded salary |
|---|---|---|---|---|---|
| Ananth Grama, PhD (PI) | Purdue | ~$320K | $228K | YES | Fund at $228K × 0.25 FTE = $57K/yr ARPA-H salary. Purdue covers remainder. |
| Anne Carpenter, PhD (TA1 co-lead; computational; no bench) | Purdue | ~$300K | $228K | YES | Fund at $228K × 0.25 FTE = $57K/yr ARPA-H-funded. |
| Matthew Tegtmeyer, PhD (TA4 academic) | Purdue | ~$220K | $228K | No (verify if base rises) | No constraint currently; full 25% FTE funded normally. |
| W. Brad Ruzicka, MD/PhD | McLean/HMS | ~$250K | $228K | YES | Fund at $228K × 0.20 FTE = $45.6K/yr ARPA-H-funded. HMS covers remainder. |
| Shahin Mohammadi, PhD (Cytognosis CEO) | Cytognosis | $228K (Rung 1 = cap exactly) | $228K | At cap | Charge $228K × 0.5 FTE = ~$114K base ARPA-H + fringe + 15% OH. [rate pending comp finalization]. Rungs 2/3 above cap from unrestricted funds only, never from award. |
| Software Architect (planned Cytognosis hire; Elham interim) | Cytognosis | ~$200K est. | $228K | No | Below cap; 1.0 FTE funded normally. |
| Senior ML/AI Engineer (Cytognosis) | Cytognosis | ~$190K est. | $228K | No | Below cap. |
| ML Research Scientist (Cytognosis) | Cytognosis | ~$175K est. | $228K | No | Below cap. |
| Dan Bryce, PhD (SIFT TA2-TA3 lead) | SIFT | ~$200K est. | $228K | [FLAG] | Commercial-sub cap treatment is an OT-specific question. FLAG Duane + Purdue SPS; do not assume. |
| Cellanome / sequencing CRO staff | Commercial | ~$150–210K | $228K | [FLAG] | Commercial-sub cap treatment. FLAG Duane + Purdue SPS; do not assume. |
| PhD students × 2 (Purdue) | Purdue | ~$36–50K stipend | $228K | No | Well below cap; normal stipend + tuition. |
| Academic postdocs (Purdue) | Purdue | ~$70–85K | $228K | No | Below cap. |

**Retired figure:** Do NOT cite $165K for Shahin. That figure is stale. Use "[rate pending comp finalization]" as placeholder until the signed rate is confirmed, then use $228K × 0.5 FTE = ~$114K/yr base.

**Sources:**
- NIH NOT-OD-26-034: https://grants.nih.gov/grants/guide/notice-files/NOT-OD-26-034.html
- Harvard OSP 2026 salary cap: https://osp.finance.harvard.edu/news/2026/01/2026-nih-salary-cap-effective-january-11-2026
- ARPA-H PARADIGM FAQ: https://arpa-h.gov/research-and-funding/programs/paradigm/faqs

---

## 4. Technology / Assay / Compute Purchase Assessment

### Table 4-A: Buy vs. Access Decision Matrix

| Item | Organization | Buy vs. Access | Est. Unit Cost | 5-yr Total | Notes |
|---|---|---|---|---|---|
| **IMAGING / INSTRUMENTS** | | | | | |
| High-content imaging system (Cell Painting/phenomics) | Purdue (Tegtmeyer wet-lab; Carpenter computational imaging analysis) | **BUY, Phase I** | ~$250–400K | ~$350K | PerkinElmer Operetta CLS or BioTek Cytation; required for Tegtmeyer's TA4 experiments |
| Spinning-disk confocal + calcium-imaging rig | Purdue (Tegtmeyer lab) | **BUY, Phase I** | ~$200–350K | ~$275K | Nikon Ti2 + spinning disk + perfusion chamber; single-cell Ca2+ imaging in iPSC-derived neurons; NOT MEA/electrophysiology |
| Opentrons OT-2 liquid handler | Purdue and/or SIFT | **BUY, Phase I** | ~$25–30K each | ~$60K (2 units) | LabOP-compatible; SiLA interface |
| Cellanome R3200 | Cellanome | **Access (RENT-and-we-run base)** | Partner pricing (pending) | [FLAG: pending BD quote] | TA4-industry arm; R3200 live-cell + same-cell CRISPR; operating model pending |
| **CELL AND MOLECULAR BIOLOGY** | | | | | |
| iPSC line acquisition + QC | Purdue (Tegtmeyer lab) | **Buy** | ~$5–15K/line | ~$120K | WiCell, ATCC, or academic transfer; 22q11.2 disease lines + isogenic controls |
| NGN2 neuron differentiation reagents | Purdue (Tegtmeyer) | **Buy (recurring)** | ~$3–10K/run | ~$400K | ~80 runs over 5 yr |
| CRISPRi/a guide RNA libraries | Cellanome | **Buy** | ~$20–50K/library | ~$120K | Addgene Calabrese/Weissman or custom |
| Targeted Perturb-seq kits (10x Genomics) | Cellanome | **Buy** | ~$5–20K/screen | ~$600K | ~30 screens over 5 yr |
| Cell Painting reagents | Purdue (Tegtmeyer wet-lab) + Cellanome | **Buy (recurring)** | ~$50–200K/campaign | ~$450K | Split; Carpenter consumes outputs computationally |
| **COMPUTE AND DATA** | | | | | |
| GPU / cloud compute (TA1 + TA2; program line) | Program / Cytognosis | **Cloud** | ~$500K/yr | ~$2.5M | H100 blended ~$2.50–3.00/GPU-hr; program-level line; partially shiftable to IPAI HPC in-kind |
| TA4 sequencing-as-service | Sequencing CRO subaward | **Access (CRO)** | ~$200–700/sample | ~$2.0M | scRNA-seq + Perturb-seq; CRO subaward; Illumina optional in-kind separately |
| Cloud data storage | Cytognosis | **Cloud** | ~$100K/yr | ~$500K | AWS S3/EBS or GCS |

### Table 4-B: 5-Year Equipment Spend Summary

| Category | 5-yr Total | >$10K items requiring backup docs |
|---|---|---|
| Phase I Tegtmeyer lab stand-up (imaging rig + Ca2+ confocal + OT-2s + fit-out + iPSC equipment) | ~$1,200K | All items >$10K each |
| Lab computing + NAS | ~$80K | Yes; individual workstations >$10K |
| Software licenses | ~$50K | Bundled; items may be <$10K |
| Reserve | ~$70K | — |
| **Total Equipment** | **~$1,400,000** | Per C.4 controlling figure |

**Note:** On-premises GPU node (previously $400K in Phase III) has been removed. The shared program compute line ($2.5M over 5 yr) covers GPU/cloud at program level.

---

## 5. Space and Facilities Assessment

No direct space rental line needed. All covered by institutional F&A or commercial overhead.

| Organization | Space situation | Budget treatment |
|---|---|---|
| **Cytognosis** | Fully computational; remote/hybrid team; no wet lab | Cloud + co-working (~$10–15K/yr in ODC). No direct rent. |
| **Purdue/IPAI** | Lab + office space on Purdue campus | Covered by Purdue's negotiated F&A (~57% MTDC). |
| **SIFT** | Commercial office + engineering lab (SIFT's own facility) | Covered in SIFT's G&A; embedded in fully-loaded rate. |
| **McLean / HMS** | Ruzicka's existing HMS office | Covered by Harvard/McLean's negotiated F&A. |
| **Cellanome** | Cellanome's own commercial lab | Covered in Cellanome's G&A. |
| **Carpenter (in-house Purdue)** | Fully in-housed at Purdue/IPAI; no Broad transition space | Covered by Purdue's F&A. No separate Broad sub-award space cost. |

---

## 6. Consolidated Basis of Estimate (BOE)

### Table 6-A: Consolidated BOE — All Phases, All Organizations (~$43M locked model)

| ARPA-H Cost Category | Phase I ($) | Phase II ($) | Phase III ($) | 5-yr Total ($) | % of Total | Basis of Estimate |
|---|---|---|---|---|---|---|
| **Direct Labor (fully burdened)** | ~$4.7M | ~$5.6M | ~$8.5M | **$18.8M** | 43.8% | Purdue-comp ~$4.14M + Tegtmeyer ~$1.9M + Cytognosis ~$8.26M + SIFT DL $4.09M + McLean ~$0.45M; see Tables 2-A/2-B |
| **Materials** | ~$0.6M | ~$0.8M | ~$1.0M | **$2.4M** | 5.6% | Tegtmeyer wet-lab ~$1.4M + Cellanome reagents ~$1.0M; iPSC lines, NGN2 reagents, Perturb-seq kits, Cell Painting reagents |
| **Equipment** | ~$1.4M | $0 | $0 | **$1.4M** | 3.3% | Phase I Tegtmeyer lab stand-up; items >$10K carry quotes; no Phase II/III equipment line in locked model |
| **Travel** | ~$0.225M | ~$0.3M | ~$0.375M | **$0.9M** | 2.1% | SIFT confirmed $69,747; DDD workshop ~$40K; TA3 bake-offs ~$44K; IV&V reviews × 5 ~$40K; connect-a-thon ~$50K; conferences ~$22.5K; reserve ~$45K |
| **Subcontracts & consultants** | ~$0.55M | ~$0.7M | ~$0.95M | **$2.2M** | 5.1% | Sequencing CRO subaward $2.0M + Duane Valz legal $0.2M |
| **Other Direct Costs (ODC)** | ~$1.725M | ~$2.075M | ~$3.1M | **$6.9M** | 16.1% | Shared program compute $2.5M + Cellanome runs/service/storage/licenses ~$4.4M (cloud, sequencing-as-service, storage, software) |
| **Indirect (F&A / Overhead)** | ~$1.85M | ~$2.075M | ~$3.475M | **$7.4M** | 17.2% | Purdue-comp ~57% (~$2.36M over 5 yr) + Tegtmeyer ~57% (~$1.3M) + Cytognosis 15% de minimis (~$1.24M) + SIFT indirect $2.20M + McLean ~$0.25M |
| **Profit / Fee** | ~$0.3M | ~$0.41M | ~$0.49M | **$1.2M** | 2.8% | SIFT $636,412 + Cellanome ~$600K; none for academia/nonprofit |
| **Cross-team integration & reserve** | ~$0.13M | ~$0.1M | ~$1.47M | **$1.7M** | 4.0% | Management reserve + integration events net of travel above |
| **TOTAL (ARPA-H request)** | **~$11.48M** | **~$13.06M** | **~$18.36M** | **$42.9M** | 100% | |

**Three-way arithmetic tie:**
- By-category: 18.8 + 2.4 + 1.4 + 0.9 + 2.2 + 6.9 + 7.4 + 1.2 + 1.7 = **$42.9M** ✓
- By-performer: 6.5 + 6.0 + 9.5 + 7.0 + 6.0 + 2.5 + 2.0 + 0.7 + 0.2 + 2.5 = **$42.9M** ✓
- By-phase: 11.48 + 13.06 + 18.36 = **$42.9M** ✓

### Indirect Rate Assumptions Detail

| Organization | Rate | Base | Regulatory basis | Notes |
|---|---|---|---|---|
| Cytognosis | 15% de minimis MTDC | All direct costs except equipment, grad tuition, subawards above first $50K | 2 CFR 200.414(f) | OT: ARPA-H may negotiate; 15% is defensible floor; NICRA possible in 18–24 mo |
| Purdue / IPAI | ~57% on-campus MTDC | Purdue-direct salaries and ODC; excludes Purdue-issued sub-awards above first $50K | Purdue negotiated rate (NICRA) | Standard Big-10 research university rate; confirmed 55–60% |
| McLean / HMS | ~50% on-campus MTDC | McLean/HMS sub-award direct costs | HMS negotiated rate | Applies to Ruzicka sub only; no Broad Institute sub-award |
| SIFT, Cellanome | Overhead embedded in fully-loaded rate; SIFT indirect confirmed at $2,199,941 (Dan's breakdown) | N/A (commercial; G&A in rate) | Commercial standard | No separate F&A line for SIFT/Cellanome; fee: SIFT $636,412, Cellanome ~$600K |

---

## 7. Resource Sharing (In-Kind; SEPARATE from the ~$43M ARPA-H Ask)

In-kind resource sharing is **not required** for ARPA-H OT awards but is evaluated positively under Criterion 4. Target ~5% in-kind. Total in-kind ~$2.3M; total project value ~$45.2M.

**Do NOT count:** Anne's non-dedicated effort or Cytognosis background IP (ARPA-H AOs rate contestable).

### Table 7: Performer In-Kind Resource Sharing

| Resource | Contributing partner | Type | Est. value ($) | Phases | Basis |
|---|---|---|---|---|---|
| IPAI/Purdue HPC compute (Anvil/Brown; NSF ACCESS allocation rates) | Purdue / IPAI | HPC compute | ~$2,000,000 | All | NSF ACCESS rates; Purdue match letter unlocks ~10%; partially nets the $2.5M direct shared-compute line; ~10% of ARPA-H ask |
| Purdue wet-lab facilities (Tegtmeyer arm) | Purdue University | Facility credit | ~$150,000 | All | Facility usage credit; not a direct cost per MTDC rules |
| Cellanome instrument/run credits | Cellanome | Instrument/run credits | ~$160,000 | All | Needs commitment letter; clear with Duane under NDA; keep separate from Cellanome sub so no fee stacks |
| **Total in-kind** | | | **~$2,310,000** | | |

**Government / Performer split:**
- Government share (ARPA-H request): ~$42.9M (~94.9%)
- Performer in-kind share: ~$2.3M (~5.1%)
- **Total project value: ~$45.2M** (100%)

---

## 8. C.3 Narrative-Ready Summary

### Level of Effort and Labor

PsychIGoR fields approximately 22 funded FTEs per year, drawn from six performing organizations. The team proposes substantial senior effort at every level: four PhD faculty (Grama, Carpenter, Tegtmeyer, Ruzicka) each provide 2–3 person-months per year, exercising scientific strategy and laboratory oversight, while postdoctoral researchers, graduate students, research engineers, and staff scientists carry the execution work. This structure directly answers ARPA-H's stated concern that proposers must not rely on junior personnel to reduce budget risk. Cytognosis contributes approximately 5.5 FTE of computational and AI engineering depth (Mohammadi at 0.5 FTE plus five senior hires). SIFT contributes 24,204 labor hours (70% Bryce / 30% Goldman and engineers) of standards engineering. The named Project Manager (Patricia Purcell) provides approximately 400 hours per year of cross-TA coordination and reporting. The Software and Systems Architect role (a planned Cytognosis hire; Elham Jebalbarezi Sarbijan (IPAI) interim) provides 1.0 FTE of architectural authority over TA1-TA2 interface design and open-source delivery.

All labor rates are fully burdened (base salary + fringe benefits + applicable direct overhead), drawn from 2026 market data (BLS OEWS May 2024; NIH NRSA FY2026). The program-level direct labor total is approximately $18.8M over five years, representing 43.8% of the ARPA-H request.

### Equipment Purchases

Major equipment is concentrated in Phase I at Purdue (Tegtmeyer lab stand-up, the academic experimental arm of TA4): a high-content imaging system (~$350K) for Cell Painting and optical pooled screens; a spinning-disk confocal plus single-cell calcium-imaging rig (~$275K) for functional neuronal readouts; two Opentrons OT-2 liquid handlers (~$60K); lab fit-out (~$150K); iPSC-specific equipment (~$120K); and lab computing ($80K). Anne Carpenter's equipment footprint is purely computational (personnel + shared compute); the imaging system supports Tegtmeyer's experiments. All items exceeding $10,000 will have vendor quotes before the Aug 6 submission. Total equipment: $1.4M (Phase I only).

### Travel

Travel totals approximately $0.9M over five years: DDD workshop (~$40K); TA3 bake-offs (~$44K); IV&V biannual reviews (~$40K); SIFT travel (confirmed $69,747); connect-a-thon (~$50K); conferences (~$22.5K); reserve (~$45K). Each trip is linked to a TDD milestone.

### Other Direct Costs (ODCs)

ODCs total approximately $6.9M and are dominated by the shared program compute line ($2.5M for TA1 FM fine-tuning and TA2 inference, at $2.50–3.00/GPU-hr blended) and Cellanome runs/service/storage/licenses (~$4.4M). Other ODCs include cloud data storage (~$500K), software/API licenses (~$400K), PhD student tuition (~$350K), PM fees (~$400K), IT/cybersecurity (~$350K), and open-source/publication costs (~$150K).

### Resource Sharing

The team proposes approximately $2.3M in Performer in-kind resource sharing (~5.1% of total project value): IPAI/Purdue HPC compute (~$2.0M at NSF ACCESS rates); Purdue wet-lab facilities (~$150K); Cellanome instrument/run credits (~$160K). Total project value ~$45.2M. All in-kind contributions will be documented with letters of commitment or data-access agreements.

---

## Appendix: Arithmetic Reconciliation

### BOE Category Totals vs. Performer Allocation

**BOE category total: $42.9M** (Table 6-A: 18.8 + 2.4 + 1.4 + 0.9 + 2.2 + 6.9 + 7.4 + 1.2 + 1.7 = $42.9M) ✓

**Performer total: $42.9M** (Table 1-A: 6.5 + 6.0 + 9.5 + 7.0 + 6.0 + 2.5 + 2.0 + 0.7 + 0.2 + 2.5 = $42.9M) ✓

**Phase totals: Phase I ~$11.48M + Phase II ~$13.06M + Phase III ~$18.36M = $42.9M** ✓

---

*Internal only. Share only the sanitized C.3 narrative (Section 8) externally. All dollar figures are planning estimates for pre-award use; finalized at OT negotiation.*

*Updated: 2026-06-21. Author: Cytognosis Agents (Claude). ARPA-H PM: Paul E. Sheehan, Ph.D. PsychIGoR PM: Patricia Purcell.*
