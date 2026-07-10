# IGoR Fact-Check and Capabilities Reference

**Team: PsychIGoR.** **Internal only.** Verified 2026-06-16.
**Reading time:** ~6 minutes. **If you only read one thing:** the Trubetskoy DOI in all drafts is wrong (see Section 2).

---

## 1. Verified Program Facts

### 1.1 ARPA-H IGoR Program (ARPA-H-SOL-26-155)

Source: [arpa-h.gov/explore-funding/programs/igor](https://arpa-h.gov/explore-funding/programs/igor), [HHS press release](https://www.hhs.gov/press-room/arpa-h-launches-intelligent-generator-of-research-igor-program.html)

| Item | Verified fact |
|---|---|
| Program name | Intelligent Generator of Research (IGoR) |
| Notice ID | ARPA-H-SOL-26-155 |
| ARPA-H office | Proactive Health Office (PHO) |
| Program Manager | Paul E. Sheehan, Ph.D. |
| Launched | May 5, 2026 |
| Headline goal | "validate valuable biological knowledge **at least ten times faster** than traditional research approaches" (verbatim from the ARPA-H program page) |
| Award type | Other Transaction (OT) agreements |
| Expected awards | Approximately **three** multidisciplinary performer teams; each must address all four TAs |
| Total budget | **Not publicly stated** in the solicitation; no per-award figure is published |
| Phase structure | 3 phases over 5 years: **Phase I** 18 months, **Phase II** 18 months, **Phase III** 24 months |

**Four Technical Areas (verbatim from the ARPA-H program page):**

| TA | Description |
|---|---|
| TA1 | Mechanistic disease models that encode causal biological relationships across scales |
| TA2 | An AI orchestration layer that identifies knowledge gaps and designs optimal experiments |
| TA3 | A layered protocol architecture that enables any qualified laboratory to execute the same experiment reproducibly |
| TA4 | A distributed marketplace of validated laboratories that execute standardized protocols and return gold-standard data |

### 1.2 Solution Summary and Full Proposal Dates

Source: [arpa-h.gov/explore-funding/programs/igor](https://arpa-h.gov/explore-funding/programs/igor), [Impact Health Policy](https://impacthealthpolicy.com/arpa-h-launches-ai-enabled-igor-program-to-transform-biomedical-research-solution-summaries-due-june-25-and-full-proposals-due-august-6/)

| Milestone | Date | Notes |
|---|---|---|
| Solution Summary due | **June 25, 2026, 12:00 PM ET** | Confirmed. Required to submit a full proposal. 5-page limit. Submit via solutions.arpa-h.gov. |
| Full Proposal due | **August 6, 2026, 12:00 PM ET** | Confirmed. ARPA-H will encourage or discourage submission after SS review. |

---

## 2. Reference Verification

**One correction required. All others confirmed.**

| Citation as in drafts | Status | Notes |
|---|---|---|
| Tegtmeyer M et al. 2025, "Combining phenomics with transcriptomics ... 22q11.2 deletion," *Nat Commun* 16:6332, doi:10.1038/s41467-025-61547-x | **Confirmed.** | Published July 9, 2025. Title on the journal page uses "phenomics" (not "NeuroPainting"). The preprint title used "NeuroPainting"; the published title uses "phenomics." Both resolve to the same article. PMID 39605350. ([Nature Comms](https://www.nature.com/articles/s41467-025-61547-x), [PubMed](https://pubmed.ncbi.nlm.nih.gov/39605350/)) |
| Ruzicka WB, Mohammadi S et al. 2024, single-cell multi-cohort schizophrenia, *Science* 384:eadg5136 | **Confirmed.** | Full title: "Single-cell multi-cohort dissection of the schizophrenia transcriptome." doi:10.1126/science.adg5136. ([Science](https://www.science.org/doi/10.1126/science.adg5136), [PubMed](https://pubmed.ncbi.nlm.nih.gov/38781388/)) |
| Minikel EV et al. 2024, "Refining the impact of genetic evidence on clinical success," *Nature* 629:624-629, doi:10.1038/s41586-024-07316-0 | **Confirmed.** | 2.6x multiplier confirmed. Authors: Minikel EV, Painter JL, Dong CC, Nelson MR. ([Nature](https://www.nature.com/articles/s41586-024-07316-0), [PubMed](https://pubmed.ncbi.nlm.nih.gov/38632401/)) |
| Nelson MR et al. 2015, *Nat Genet* 47:856-860, doi:10.1038/ng.3314 | **Confirmed.** | Title: "The support of human genetic evidence for approved drug indications." ([Nature Genetics](https://www.nature.com/articles/ng.3314), [PubMed](https://www.ncbi.nlm.nih.gov/pubmed/26121088)) |
| Singh T et al. 2022 SCHEMA, *Nature* 604:509-516, doi:10.1038/s41586-022-04556-w | **Confirmed.** | Title: "Rare coding variants in ten genes confer substantial risk for schizophrenia." ([Nature](https://www.nature.com/articles/s41586-022-04556-w), [PubMed](https://pubmed.ncbi.nlm.nih.gov/35396579/)) |
| Trubetskoy V et al. 2022, *Nature* 604:502-508, doi:10.1038/s41586-021-04317-3 | **FLAG: DOI IS WRONG.** | Title and journal/volume/pages are correct. The confirmed DOI is **10.1038/s41586-022-04434-5** (note: `s41586-022`, not `s41586-021`). Correct in all drafts before submission. ([Nature](https://www.nature.com/articles/s41586-022-04434-5)) |
| Bartley et al. 2023, LabOP/PAML, *ACM JETC*, doi:10.1145/3604568 | **Confirmed.** | Title: "Building an Open Representation for Biological Protocols." LabOP was formerly called PAML. ([ACM DL](https://dl.acm.org/doi/abs/10.1145/3604568)) |
| Bunne C et al. 2024, "How to build the virtual cell with artificial intelligence," *Cell* 187:7045-7063, doi:10.1016/j.cell.2024.11.015 | **Confirmed.** | Published December 2024. Full title appends ": Priorities and opportunities." ([Cell](https://www.cell.com/cell/fulltext/S0092-8674(24)01332-1)) |

### LabOP and SiLA 2 infrastructure

- **LabOP** (bioprotocols.github.io/labop): confirmed active open standard for laboratory protocol representation, built on SBOL3 RDF, UML, and PROV provenance; supports specialization to OpenTrons, SiLA-based automation, Autoprotocol, and human-readable formats. ([bioprotocols.github.io](https://bioprotocols.github.io/labop/))
- **SiLA 2**: confirmed active communication standard for laboratory instrument device drivers (readers, liquid handlers, chromatography, other analytical instruments); has a shared device-databank project with LabOP. ([SiLA 2 overview](https://matthieu-croissant.medium.com/sila-2-hands-on-bringing-automation-to-the-laboratory-dacc12df7152))

---

## 3. Capability Statements by Team Member

Status uses the CANDIDATE_DOSSIER.md negotiation scale: **Confirmed** = Stage 7-8 or tracker "Confirmed"; **In discussion** = Stages 3-6 or tracker "In discussion"; **Recruiting** = no person locked.

---

**Ananth Grama, PI and Prime (IPAI/Purdue)** — Confirmed
Director of the Institute for Interdisciplinary Information Sciences (IPAI) at Purdue University; provides the institutional prime-performer home, F&A environment, and computational infrastructure to anchor the 7-performer team. On the critical path as the legally responsible prime and as co-lead for TA1/TA2 software architecture and student/postdoc capacity.

---

**Shahin Mohammadi, TA1 lead and TA2 co-lead (Cytognosis Foundation)** — Confirmed
Computational biologist with 20 years of experience in single-cell genomics, causal representation learning, and psychiatric disease modeling; architect of the dual-grounded disease-axis framework that is PsychIGoR's core TA1 contribution. On the critical path as the scientific originator of the joint genomic factorization method and as the primary intellectual driver across TA1 and TA2.

---

**Anne Carpenter, TA4 computational morphology/imaging-model lead (IPAI/Purdue, joining ~September 2026; computational home; Broad Institute for transition period)** — Confirmed (~90%)
Senior Director of the Imaging Platform at the Broad Institute; co-developer of CellProfiler and the Cell Painting assay; **purely computational role** (interpretable morphology and cellular-imaging models; no wet-lab bench). Her group contributed the analysis methods to the 22q11.2 NeuroPainting phenomics paper (Tegtmeyer et al. 2025, Nat Commun). On the critical path as the computational morphology/imaging-model lead and TA1/TA2 interpretability bridge, consuming readouts from both the Matt Tegtmeyer lab (Element AVITI24) and Cellanome. Open-source infrastructure (CellProfiler, Cell Painting Gallery, JUMP) seeds TA3 schemas.

> [!NOTE]
> **Role correction (2026-06-17):** Prior docs listed Anne as "TA4 experimental phenomics." Correct role is computational morphology/imaging-model lead. All wet-lab experiments in TA4 are run by Matt Tegtmeyer's lab (Element AVITI24, academic arm) and Cellanome (R3200, industry arm). Budget implication: personnel + compute, not wet-lab capex. **[FLAG 2026-06-17: re-derive Anne's cost-model budget line; defer to Shahin/Ananth.]**

---

**Matthew Tegtmeyer, TA4 experimental modeling and TA1 experimental grounding (Purdue, new faculty)** — Confirmed (per memory context: now Purdue faculty)
Purdue faculty with iPSC-neuron disease modeling expertise in 22q11.2 deletion and TBX1; first author of the NeuroPainting phenomics/transcriptomics paper that defines Phase I anchor readouts. On the critical path as the in-house iPSC-neuron experimentalist at the prime institution and as the experimental bridge between the 22q11.2 disease model and the TA4 readout stack.

---

**W. Brad Ruzicka, Clinical and translational co-lead (McLean Hospital / Harvard Medical School)** — Confirmed
Psychiatrist and computational neuroscientist at McLean Hospital/HMS; senior author of the single-cell multi-cohort schizophrenia atlas (Ruzicka, Mohammadi et al. 2024, Science). On the critical path for cohort interpretation, sample and data-access governance (PsychENCODE, McLean datasets), and translational grounding of TA1 disease axes in real clinical populations.

---

**SIFT (Dan Bryce and Robert Goldman), TA3 lead, LabOP/protocol stack** — In discussion
Minneapolis/Dallas company and co-developers of the Laboratory Open Protocol (LabOP) standard; presented at the IGoR Proposers' Day. On the critical path for TA3 because LabOP is the only production-grade open interoperability standard that maps onto the IGoR intent-to-hardware stack; their Bayesian value-of-information planning capability also provides an optional TA2 hypothesis-to-schedule compiler. Full analysis in `partnerships/SIFT_capabilities_analysis.md`.

---

**Anna Merkoulovitch, Software and Systems Architect (recruiting/Tier 1 candidate)** — Recruiting (Tier 1 candidate, conditions on acceptance)
Former insitro; outreach message sent 2026-06-14. This is an IGoR-required named role (distinct from PI and PM) responsible for TA1-TA2 interface specifications, cross-team interoperability standards, and open-source release. On the critical path because the ISO requires a named architect and the role owns the technical coherence layer that lets 7 performers operate as one system. Budget: ~$240K fully loaded. Confirmation needed before August 6.

---

**Patricia (Patty) Purcell, Project Manager (part-time/hourly)** — Confirmed (verbally agreed; terms TBD)
Experienced program/project manager; verbally agreed to a part-time hourly role. On the critical path as a named PM required by the ISO; the specific level of effort (LOE in annual hours) must be confirmed because ISO 13485 and the OT require a stated annual commitment. A backup PM candidate should be identified given the availability risk.

---

**Matthew Tegtmeyer, TA4 academic experimental arm (Purdue faculty)** — Confirmed (2026-06-15)
Purdue faculty; first author of the NeuroPainting phenomics/transcriptomics paper (Tegtmeyer et al. 2025, Nat Commun); iPSC-neuron disease modeling expertise in 22q11.2 / TBX1. Runs all TA4 wet-lab experiments using the **Element AVITI24 / Teton CytoProfiling** platform. Also on an IU-prime IGoR team (~5 lead PIs; likely Purdue subaward); effort/optics to resolve before Aug 6 (not a blocker for Jun 25 SS).

---

**Element AVITI24 / Teton CytoProfiling — Verified Platform Capabilities (2026-06-17)**

Source: elementbiosciences.com/products/aviti24/cytoprofiling (verified 2026-06-17)

| Capability | Verified fact |
|---|---|
| Platform type | Single-cell AND spatial co-detection; imaging + in-situ sequencing via Avidity Base Chemistry (ABC) |
| Throughput | Hundreds of thousands to millions of cells |
| Turnaround | Next-day results; <1 hr sample prep |
| Morphology modality | Nucleus, membrane, actin, ER, Golgi, mitochondria (Cell-Painting-style organelle features); onboard segmentation + feature extraction |
| RNA modality | 350-plex subcellular in-situ; thousands of transcripts per cell |
| Protein / phospho modality | 50-plex (surface, intracellular, phospho-protein) |
| CRISPR-guide readout | DISS (Direct In Sample Sequencing): in-situ CRISPR-guide sequencing, untargeted 3' RNA, expressed-mutation detection |
| Neuroscience panel | Yes (neurodifferentiation, neurotransmission/synaptic, neurodegeneration, neuroinflammation) |
| Cell state | Fixed-cell, in-situ (contrast with Cellanome = live-cell) |
| Relationship to Cellanome | Orthogonal/complementary; overlap = multi-modal same-cell readouts + CRISPR perturbation; differences = fixed-cell vs. live-cell, scale vs. temporal resolution |
| Anne Carpenter interface | Element morphology natively outputs Cell-Painting-like features that feed directly into Anne's computational morphology models |
| Teaming status | Platform Matt uses; **no confirmed formal teaming agreement**; do not assert partnership |

---

**External TA4 candidates (Cellanome, Illumina, SPOC Biosciences)**

*Cellanome* — In discussion (NDA in progress; Stage 6)
San Diego, Series B ($150M, Jan 2024); R3200 platform combines programmable live-cell fluorescence imaging and same-cell scRNA-seq in a single instrument (Perturb-LINK pooled CRISPR). Provides two of PsychIGoR's three Phase I core readouts in one system. Route all further engagement through Duane Valz; treat as TA4 only.

*Illumina (via Sebastian Pineda)* — In discussion (Stage 3; call held 2026-06-16)
Public sequencing company (~$3B revenue); acquired Fluent BioSciences (PIPseq instrument-free single-cell) in 2024; existing ARPA-H relationship via the PCX pediatric-cancer program (April 2026). Provides the scalable transcriptomic sequencing readout for every loop iteration. Next step: identify the internal Strategic Partnerships or Government Affairs sponsor beyond Sebastian Pineda; determine in-kind versus named-subcontractor structure.

*SPOC Biosciences (inbound)* — In discussion (Stage 4; meeting scheduling)
Scottsdale AZ; cell-free protein expression (up to 1,152 proteins or antibodies), SPR kinetics, Cryo-EM, and MALDI. Inbound teaming request 2026-06-14 (Lydia Gushgari). Orthogonal protein-level validation add-on, not a core cellular readout partner; define a bounded protein-validation scope and keep optional.

---

## 4. Key Significance Points (from SIGNIFICANCE_AND_INNOVATION_dual_grounding_2026-06-15.md)

These three points are the load-bearing quantitative and conceptual anchors for the S&I narrative:

1. **Nelson 2x multiplier (2015):** Genetically supported drug targets reach approval at roughly twice the rate of unsupported ones (Nelson MR et al., *Nat Genet* 2015;47:856-860, doi:10.1038/ng.3314).

2. **Minikel 2.6x multiplier (2024):** A decade of expanded data raises the estimate to **2.6x**, and the lift increases with confidence in the causal gene and varies by therapeutic area; the multiplier is the formal quantitative rationale for investing in precision genetic grounding (Minikel EV et al., *Nature* 2024;629:624-629, doi:10.1038/s41586-024-07316-0).

3. **The noncoding-mechanism gap and dual-grounding as the response:** Most psychiatric GWAS signal is noncoding (variant-to-gene mapping is an inference), and even an unambiguous causal gene rarely hands you a mechanism; the standard post-hoc validation pipeline confirms association but not mechanism, and cannot certify disease-relevance or generalize within a pathway. The PsychIGoR response is to represent every signal, cellular or clinical, as a shift in pathway space relative to a matched control, so that engineered cellular perturbations and natural population-genetic evidence constrain the same disease axes: each method's blind spot is the other's strength, and axes that load on both are mechanistic, population-relevant, and testable.

---

## 5. Action items from this verification

| Item | Priority | Owner |
|---|---|---|
| Correct Trubetskoy DOI in all drafts: replace `s41586-021-04317-3` with `s41586-022-04434-5` | **Do now** | Shahin |
| Confirm Tegtmeyer title in citations: published title uses "phenomics," not "NeuroPainting" | Do now | Shahin |
| Confirm Anna Merkoulovitch availability and LOE before Aug 6 | Urgent | Shahin |
| Confirm Patty Purcell annual LOE in hours (ISO requirement) | Urgent | Shahin |
| Finalize Anne Carpenter subaward routing (Purdue/IPAI vs Broad) | Before Aug 6 | Ananth + Shahin |
| No public award dollar figure: PsychIGoR $50M total request is internally set; do not cite a public funding cap that does not exist | Note | All |

---

*Sources for all web-verified facts are inline above. Internal sources: `partnerships/CANDIDATE_DOSSIER.md`, `partnerships/TEAM_TRACKER.md`, `research/SIGNIFICANCE_AND_INNOVATION_dual_grounding_2026-06-15.md`, `research/sections/60_team_consortium_and_cost.md`. Checked 2026-06-16 by Claude Sonnet 4.6 subagent.*
