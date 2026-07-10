# IGoR Master Drive Plan — EXECUTION (2026-06-21)

**This is the navigation backbone + shared budget source-of-truth for the full revision.** Subagents and the main thread both read this. It operationalizes `MASTER_REVISION_PLAN_2026-06-21.md`. Source inputs: `BUDGET_FRAMEWORK_v2_2026-06-21.md`, `INTEGRATION_SPEC_2026-06-21.md`, `IGoR_CONSOLIDATED_STATE.md`, `CEO_Compensation_DETERMINATION_2026-06-21.md`.

**BLUF (3 sentences):** Rebuild every IGoR deliverable to the restructured **~$43M** budget and the corrected role map, weave in Dan's TA2/TA3 + 5 innovations + 3 stages + best-team messaging, regenerate docx/pdf, then sync all Google Docs via Chrome with per-person inline comments. The SS (due 2026-06-25) is the priority and is rebuilt first by the main thread; C1/C2/C3/cost model/C4 (due 2026-08-06) are delegated to Sonnet subagents against the locked numbers below. Google = source of truth from now on (standing rule).

---

## 0. LOCKED BUDGET MODEL — ~$43M (planning level; C4 workbook is controlling)

**Use these exact figures in every deliverable.** Bottom-up, NOT force-fit to $50M. Phylo dropped from budget; Illumina optional in-kind only. Ties three ways (below).

### Per-performer (5-yr), with phase split

| Performer / line | 5-yr | Ph I | Ph II | Ph III | Scope |
|---|---|---|---|---|---|
| Purdue/IPAI — computational (TA1 + TA2 engine) | $6.5M | $1.8M | $2.0M | $2.7M | Grama (PI) + Anne Carpenter (TA1 co-lead, morphology) + PhD students + research engineers + disease-modeling postdoc; ~57% F&A |
| Purdue — Tegtmeyer lab (TA4-academic, non-IPAI dept) | $6.0M | $2.0M | $1.7M | $2.3M | iPSC-neuron wet-lab + multimodal readouts; Ph I equipment ~$1.4M (front-loaded); Matt also TA1 disease-modeling contributor |
| **Purdue total (prime)** | **$12.5M** | | | | Largest line, as prime should be |
| Cytognosis (TA1 model + TA1-TA2 hypothesis) | $9.5M | $2.4M | $2.9M | $4.2M | Shahin + PM (Patty) + SWE/Architect + ~5 ML/comp-bio; 15% de minimis F&A; shared compute moved out |
| SIFT (TA2-TA3 + TA3 + TA3-TA4) | $7.0M | $2.0M | $2.2M | $2.8M | Dan's real figure: DL $4,094,437 / indirect $2,199,941 / travel $69,747 / fee $636,412; 24,204 hrs; 70% Bryce / 30% Goldman |
| Cellanome (TA4-industry) | $6.0M | $1.4M | $1.8M | $2.8M | R3200 RENT-and-we-run base; confirm via quote (placeholder until Cellanome BD + Psomagen quotes) |
| Shared program compute (GPU/cloud; TA1+TA2) | $2.5M | $0.6M | $0.8M | $1.1M | Program line, not loaded on one org; partially shiftable to IPAI HPC in-kind |
| TA4 sequencing (service/CRO) | $2.0M | $0.4M | $0.6M | $1.0M | scRNA-seq + Perturb-seq; CRO subaward; Illumina optional in-kind |
| McLean / HMS (Ruzicka) | $0.7M | $0.2M | $0.2M | $0.3M | Clinical + data governance |
| Duane Valz — legal/IP (consultant) | $0.2M | $0.08M | $0.06M | $0.06M | $750/hr × ~150-300 hrs; OT review, IP/field-of-use, subaward/NDA, OSS licensing; bill through Cytognosis |
| Cross-team / integration / reserve | $2.5M | $0.6M | $0.8M | $1.1M | DDD workshop, bake-offs, connect-a-thon, ~6% reserve |
| **TOTAL (ARPA-H request)** | **~$42.9M** | **~$11.5M** | **~$13.1M** | **~$18.4M** | Round to **~$43M** |

Phase sums: Ph I $11.48M, Ph II $13.06M, Ph III $18.36M = **$42.9M** ✓

### By category (planning; ties to $42.9M)

| Category | Amount | Basis |
|---|---|---|
| Direct labor (fully burdened) | $18.8M | Purdue-comp $4.14M + Tegtmeyer $1.9M + Cytognosis $8.26M + SIFT $4.09M + McLean $0.45M |
| Materials & supplies | $2.4M | Tegtmeyer wet-lab $1.4M + Cellanome reagents $1.0M |
| Equipment | $1.4M | Phase I Tegtmeyer imaging stand-up (items >$10K carry quotes) |
| Travel | $0.9M | SIFT $0.07M + cross-team DDD/bake-offs/connect-a-thon $0.8M |
| Subcontracts & consultants | $2.2M | Sequencing CRO $2.0M + Duane legal $0.2M |
| Other direct costs | $6.9M | Shared compute $2.5M + Cellanome runs/service $4.4M (cloud, sequencing-as-service, storage, software/licenses) |
| Indirect (F&A) | $7.4M | Purdue ~57% ($2.36M+$1.3M) + Cytognosis 15% de minimis ($1.24M) + SIFT indirect ($2.20M) + McLean ($0.25M) |
| Profit / fee | $1.2M | SIFT $0.64M + Cellanome $0.6M; none for academia/non-profit |
| Cross-team integration & reserve | $1.7M | Management reserve + integration events (net of travel above) |
| **TOTAL** | **$42.9M** | ✓ |

### Resource sharing (in-kind; SEPARATE from the $43M ask; target ~5%)

| In-kind item | Value | Note |
|---|---|---|
| IPAI/Purdue HPC compute (Anvil/Brown) | ~$2.0M | NSF ACCESS allocation rates; a Purdue match letter unlocks ~10%; partially nets the $2.5M direct shared-compute line |
| Purdue wet-lab facilities (Tegtmeyer arm) | ~$0.15M | Facility usage credit |
| Cellanome instrument/run credits | ~$0.16M | Needs commitment letter; clear with Duane under NDA; keep separate from Cellanome sub so no fee stacks |
| **Total in-kind** | **~$2.3M** | Total project value **~$45.2M** |

Do NOT count Anne's non-dedicated effort or Cytognosis background IP as share (AOs rate contestable).

### Salary cap (HHS Exec Level II, $228K/yr, 2026; NIH NOT-OD-26-034)
- Bound academics charged at cap × effort: Grama (~$320K base, 0.25), Carpenter (~$300K, 0.25), Ruzicka (~$250K, 0.20). Institutions cover remainder.
- Shahin (Cytognosis CEO): comp Rung 1 = $228K cap exactly → charge $228K × 0.5 FTE = ~$114K base before fringe; Rungs 2/3 from unrestricted funds, never the award. **Do not cite a $165K figure (retired).**
- Tegtmeyer (~$220K, re-check if base rises above cap) + other Cytognosis hires: verify each base < $228K (loaded rate may exceed cap; base may not).
- Commercial subs (SIFT, Cellanome, Illumina): cap treatment on direct-salary component is an OT-specific question → **flag Duane + Purdue SPS**; do not assume.

---

## 1. CANONICAL ROLE MAP (use verbatim across all docs)

| Scope | Lead(s) | Notes |
|---|---|---|
| Prime / PI | Purdue IPAI; PI **Ananth Grama** | Anne's PI succession is internal-only; Grama is PI in all submissions |
| TA1 (mechanistic disease model) | **Purdue IPAI (Grama + Anne Carpenter co-lead)** + **Cytognosis (Shahin lead)** | Anne = TA1 co-lead (computational morphology), not a separate org / no Broad sub |
| TA1-TA2 (model-grounded hypothesis generation) | **Cytognosis (Shahin lead)** | |
| TA2 (experiment-design engine) | **Co-led: Purdue IPAI (Grama) + Cytognosis (Shahin)** | Optional Phylo later; both orgs co-lead TA1 AND TA2 |
| TA2-TA3 (incl. user interface) | **SIFT (Dan Bryce lead, Goldman advisor)** | |
| TA3 (interoperable protocols) | **SIFT (Dan Bryce lead)** | LabOP backbone; SIFT co-authored LabOP under DARPA SD2 |
| TA3-TA4 | **SIFT (Dan) + TA4 partners** | |
| TA4 academic arm | **Purdue — Tegtmeyer lab** (his dept, NOT IPAI; confirm Biomedical Eng / Integrative Neuroscience) | Matt ALSO contributes TA1 disease modeling |
| TA4 industry arm | **Cellanome** (lead TBD) | R3200 |
| TA4 sequencing/cloud | **Illumina** (optional/in-kind; James Han + Michael Mehan) | PCX framing |
| TA4-TA1 (data back to model) | **Purdue (Grama + Anne) + Cytognosis (Shahin)** | |
| Semantic foundation (all TAs) | **Shahin + Dan co-lead** | One LinkML/Biolink identity, no seam translation |
| Project Manager | **Patricia Purcell** (Cytognosis hire; ~0.3 FTE) | |
| Software/Systems Architect | **Cytognosis hire** (Elham = interim placeholder) | REQUIRED per Appendix A §5.5; 1.0 FTE |
| Clinical | **W. Brad Ruzicka** (McLean/HMS) | |
| Legal/IP | **Duane Valz** (consultant; not key personnel) | |

**Broad/Cell Painting:** acknowledge as methodological foundation + team strength (Matt + Anne co-authored NeuroPainting), NO subaward, all in-house at Purdue/IPAI.

**Retired / banned terms:** $50M (forced), $165K, Vodovotz (PM = **Paul E. Sheehan, Ph.D.**), Element Teton as a teaming partner/platform name, MEA/electrophysiology as Phase I readout (it is **single-cell calcium imaging**), "SIFT co-leads TA2" (SIFT = scoped VOI layer under Cytognosis+IPAI TA2 lead), Anna Merkoulovitch, Phylo/Illumina as budgeted partners.

---

## 2. CONTENT TO WEAVE IN

**Best-team messaging (Patty):** PsychIGoR uniquely unites world experts in BOTH the clinical (Shahin, Brad) AND cellular (Matt, Anne) sides of psychiatric disease — usually pursued in separate orgs with different methods/literatures. The cellular pair already collaborated + published together (NeuroPainting 2025). Frame as integration strength, never criticism of others.

**5 innovations:** (1) residual-space alignment of cellular + clinical models (OT/MMD on disease axes); (2) universal treatment+disease language on shared delta-pathway space → one 3-latent SCM (basal / disease / treatment with direct side-effect + indirect therapeutic paths); (3) ontology-grounded semantic embeddings (TransBox EL++ for MONDO/GO/Cell Ontology) + OOD projection head; (4) pretrained genomic FMs (AlphaGenome, VariantFormer) + genomic factorization into genotypic archetypes; (5) multiresolution network-diffusion (graph-wavelet) GNNs.

**3 experimental stages → phases:** Stage 1 (create + prioritize disease models; SZ panel = CNVs + SCHEMA genes + BD/broad/control; transcriptomic + morphological + calcium-imaging; pick 5-10 highest-effect genes) = **Phase I**. Stage 2 (unbiased pooled Perturb-seq in prioritized lines → treatment embeddings) = **Phase II**. Stage 3 (targeted combinatorial perturbation of TA1/TA2-nominated pathways) = **Phase III**. Quantitative gene-count + effect-size metrics from Stage 1 = Phase I milestones.

**Dan's TA2/TA3 text (mark "SIFT draft, pending Dan's revision"):** TA2 builds on SIFT's XPlan planner (DARPA SD2); ExperimentIntent in a new ontology layer. TA2-TA3 = shared ontologies/KGs on LabOP, formalized in the Phase I Domain-Driven Design workshop. TA3 = LabOP three-tier (UML Activity base / LabOP protocols / LabOP Executions with W3C PROV-O provenance); enhance engine to author against TA1 mechanistic models, expand primitive libraries, support IV&V bake-offs + RFC. NEW specifics to add: XPlan/SD2 lineage, PROV-O provenance.

---

## 3. EXECUTION WAVES

- **Wave 1 (main thread, Opus): SS rebuild** → cover $43M, Section 5 BOE (both tables + Duane + resource sharing), Section 3/4 roles + 3 stages + best-team, light Section 1/2 innovation touches. Keep Sec 1-4 ≤5 pages. ✅ priority (due 6/25).
- **Wave 2 (Sonnet subagent A): C3 Price Proposal + COST_MODEL_DETAILED + C4 workbook** to the locked numbers. (Heavy arithmetic; precise spec.)
- **Wave 2 (Sonnet subagent B): C1 + C2** role map + Dan's TA2/TA3 (marked draft) + 3 stages + innovations.
- **Wave 3 (main thread): regenerate docx/pdf** (pandoc; SS via Inter 11pt brand build; verify ≤5pp).
- **Wave 4 (Sonnet subagent): read prior grants** (Google Impact, Astera, AWS Imagine, Coefficient) for extra innovations/context.
- **Wave 5 (main thread): VERIFY** — $43M ties 3 ways; salary cap; zero stale terms; citations resolve.
- **Wave 6 (main thread, Chrome): Google sync** — update SS/C1/C2/C3/C4 to local source of truth + per-person inline comments per the map below.

## 4. PER-PERSON GOOGLE COMMENT MAP

| Section/topic | Tag | Note style |
|---|---|---|
| TA2 + TA3 sections | **Dan (SIFT)** | Mark sketches/drafts; invite him + team to revise |
| TA1 (disease modeling, causal/SCM, genomic factorization) | **Ananth** | Questions / review requests |
| Experimental procedures, costs, Purdue equipment/feasibility, buyable-vs-not | **Matt** (optionally Anne) | Confirm feasibility, equipment, line counts |
| Computational morphology / Cell Painting / imaging | **Anne** | Confirm method/feasibility |
| Legal / IP / financial flows | **Duane** | Legal/IP review |
| Any financial figure | **Ananth** (+ Duane for legal-financial) | Verify |
| TA4 R3200 + TA3-TA4 + TA4-TA1 interfaces | **Cellanome** | Confirm platform + interfaces |
| Concept Summary + crisp no-jargon messaging | **Patty + Ananth** | Clarity/impact feedback |

## 5. GOOGLE TARGETS (from IGoR_CONSOLIDATED_STATE §7)

| Deliverable | URL |
|---|---|
| Solution Summary | https://docs.google.com/document/d/12JTwOclWLLOBb8wn7WyH9Hw46cvxR_yP/edit |
| C.1 Technical & Management | https://docs.google.com/document/d/1ertYHzLIouEqT_9uPFJ-HG_qqVbzKjCz/edit |
| C.2 Task Description | https://docs.google.com/document/d/1FNzUAE5Q2mb1ziB3TUJhjd1spmIrAh6s7_XShVbKuac/edit |
| C.3 Price Proposal | https://docs.google.com/document/d/1GDd3r0B1-khdg_ks9Ju20K-_yYsHvVzRihdpSomHxiQ/edit |
| C.4 Price Workbook | https://docs.google.com/spreadsheets/d/1XseQOlC5PNgTr9uGphCrabH2vvu1pGczqW5b6geCG7A/edit |
| Drive folder | https://drive.google.com/drive/folders/1Tnenqw-pBJpZ1t_rHN-2B33KFXzuAVPn |

## 6. OPEN DECISIONS (flag for Shahin + Ananth; do not block on them)
1. Confirm IGoR per-award ceiling (so ~$43M headroom is right).
2. Resource-sharing target % (5-10%); Purdue HPC match letter unlocks ~10%.
3. Cellanome model (RENT base ~$5-6M); get BD + Psomagen quotes; name Cellanome TA4-industry lead.
4. Matt's exact Purdue department (TA4-academic attribution, non-IPAI).
5. Commercial-sub salary-cap treatment (Duane + Purdue SPS).
6. Whether to add Phylo on TA2 before final.

---

## EXECUTION STATUS — end of 2026-06-21 session

**DONE (local, verified):**
- **SS** (`solution_summary/IGoR_Solution_Summary_SUBMISSION_2026-06-19.{md,docx,pdf}`): rebuilt to ~$43M; per-performer + category + phase BOE all tie to **$42.9M** three ways; Duane line added; resource sharing repackaged to **~$2.3M in-kind**; roles corrected (TA1+TA2 co-led Purdue+Cytognosis; Matt = TA4-academic + TA1 in his Purdue dept, not IPAI; Anne TA1 co-lead; SIFT scoped VOI); 3 experimental stages mapped to phases; best-team + Broad/NeuroPainting acknowledgment; calcium imaging (not MEA); SiLA Juchli DOI. **Sections 1-4 = 5 pages** (LibreOffice Letter render of the DOCX; Section 5 starts p7). Stale-term scan = clean.
- **C3 + COST_MODEL_DETAILED**: rebuilt to ~$43M, tie three ways; C3 category-table Phase III footer bug fixed (now 13.06 / 18.36); both docx current.
- **C1 + C2**: canonical role map; Dan's TA2/TA3 inserted with VISIBLE `***[SIFT-authored draft — Dan Bryce / SIFT to revise]***` markers; 5 innovations; 3 stages + milestones; best-team messaging; Sheehan as PM; docx rebuilt.
- **C4 workbook**: Summary, Per-Performer×Phase, Indirect&Fee, Resource-Sharing sheets updated to the $43M model. **Labor (45 rows) + Travel (16 rows) detail sheets NOT updated** — need Shahin+Ananth headcount/rates (Task 7).

**PENDING:**
- **Google sync via Chrome (Task 6):** Chrome connected (Browser 1, local) but the first `navigate` to the SS Doc **timed out at 180s**. Google Docs canvas editing via automation is slow/fragile — do this as a DEDICATED focused session. Runbook: §5 URLs + §4 per-person comment map. Sync order: SS (priority, due 6/25) → C1 → C2 → C3 → C4. Per doc: bring content to the local source of truth, then add the per-person inline comments. NOTE: a full in-place rewrite of branded funding docs via browser is high-risk; the cleaner path is to upload the regenerated `.docx` as new Drive versions (preserves formatting) and add the comments — confirm method with Shahin.
- **C4 Labor/Travel re-derivation (Task 7):** needs Shahin+Ananth.

**OPEN DECISIONS for Shahin + Ananth:** per-award ceiling; resource-share % (Purdue HPC match letter → ~10%); Cellanome RENT model + lead name + quote; Matt's exact Purdue dept; commercial-sub salary-cap treatment (Duane + Purdue SPS); DataTecnica risk-row status in C1; whether to add Phylo on TA2.
