# BDNF/TrkB Neuroplasticity Axes: Science Dossier and Publish-vs-Platform Strategy

**Date:** 2026-06-03 · **Internal, confidential.** Source document for grants (EVIDENT/HSF, IGoR TA1, NIH), for the bipolar paper scoping, and for strategic planning. **Contains platform-confidential IP (Section 5, the factorized PRS) that must be kept OFF the bipolar paper and out of any consortium-facing material.**

**Reading guide:** Sections 1 to 3 are the publishable science (the paper PoC and the grant through-line). Section 5 is the proprietary platform layer. Section 7 is the decision: what goes in the paper vs what stays the moat.

---

## 0. BLUF

Cytognosis's first scientific keystone is a set of **continuous, molecularly grounded neuropsychiatric axes (Mood, Thought, Cognitive)** defined by dysregulation **downstream of BDNF/TrkB signaling**, demonstrated first in bipolar disorder. The biology is publishable and aligns directly with the **EVIDENT neuroplastogen mechanism** (antidepressants and psychedelics act by binding TrkB). The proprietary bridge, kept off the paper, is a **factorized polygenic score** that reconstructs these axes from a person's genome alone (noninvasive, in living people), which is the foundation of the genotype factorization model and the Psychoverse coordinate.

---

## 1. Core scientific thesis

- Psychiatric variation is better described by **continuous dimensional axes** than by discrete DSM categories. We define the primary axes by the molecular programs **downstream of BDNF/TrkB**:
  - **Mood / neuroplasticity axis** (CREB-driven plasticity program).
  - **Thought axis** (GABAergic / excitation-inhibition balance; the PKC/PI3K branch).
  - **Cognitive axis** (BDNF-CREB learning/memory programs; partly distinct, partly shared with Thought).
- We project individual samples onto these axes from their **overall dysregulation downstream of BDNF/TrkB**, supervised using disease labels (a "Mood-vs-Thought" projection, with a Cognitive axis).
- **Novelty:** first to demonstrate this dimensional, BDNF-anchored decomposition **in bipolar disorder**, discovered in the McLean cohort (already published in the PsychENCODE schizophrenia capstone) and cross-validated out-of-distribution in the MtSinai cohort.

---

## 2. Molecular biology (publishable science)

### 2.1 BDNF/TrkB core signaling, converging on CREB

Mature BDNF (mBDNF) binds TrkB, activating three arms that converge on **CREB (Ser133)** to drive a neuroplasticity gene program (BDNF, Arc, PSD-95, GluA1):

- **MAPK/ERK** to RSK to CREB (immediate-early genes; late-LTP). Positive feedback: CREB drives the BDNF promoter.
- **PI3K/Akt** to mTORC1 (dendritic local translation; synaptic protein synthesis).
- **PLCgamma/PKC** to Ca2+/CaMKIV to CREB/CBP (amplifies transcription); also engages **TRPC** channels (per the draft's TRPC entry).

Authoritative reviews: Barde physiopathology of BDNF (2025); Gupta et al., BDNF/TrkB to CREB axis (Mol Neurobiol 2025, PMID 40342191).

### 2.2 Two-branch model (the axis biology)

- **Branch A, neuroplasticity (Mood axis): mBDNF/TrkB to CREB.** Neurogenesis, dendritic arborization, LTP; the mechanism antidepressants restore.
- **Branch B, GABA regulation (Thought axis): TrkB-PLCgamma-PKC and PI3K to KCC2 and GABA-A trafficking.** Per **WikiPathways WP4829** ("mBDNF and proBDNF regulation of GABA neurotransmission"): mBDNF/TrkB stabilizes KCC2 and GABA-A surface expression (maintains hyperpolarizing GABA), while proBDNF/p75NTR (RhoA/ROCK) destabilizes KCC2 (depolarizing shift). The **mBDNF/proBDNF ratio** sets inhibitory tone. (E/I imbalance via this exact axis is a leading hypothesis in ASD and maps onto interneuron dysfunction in mood/psychosis.)

### 2.3 proBDNF vs mBDNF (yin-yang)

proBDNF (p75NTR + sortilin; RhoA/JNK/NF-kB; LTD, pruning, apoptosis) opposes mBDNF (TrkB; survival, LTP). The depression-relevant variable is the **processed-to-unprocessed ratio**, not absolute BDNF. Chronic stress raises proBDNF/p75NTR; antidepressants increase conversion to mBDNF.

### 2.4 Cholesterol as a TrkB modulator (the differentiating mechanism, and the EVIDENT bridge)

- **Casarotto et al., Cell 2021 (PMID 33606976):** TrkB has a **cholesterol-sensing transmembrane domain (TMD)**; cholesterol binding controls synaptic TrkB localization, and **antidepressants (fluoxetine, ketamine) bind the TrkB TMD directly** as allosteric "BDNF sensitizers." The draft's CRAC-motif paper (2021) and the TrkB-TMD structural papers (2024) reinforce the cholesterol-recognition and antidepressant-activation mechanism.
- **Moliner et al., Nat Neurosci 2023 (PMID 37280397):** psychedelics (LSD, psilocin) bind TrkB at ~1000x higher affinity than classical antidepressants; plasticity effects are TrkB-dependent and **5-HT2A-independent** (the neuroplastogen design rationale).
- **SREBP/mTOR cholesterol axis:** brain cholesterol is made in the CNS, mainly by **astrocytes** (exported via ApoE; taken up by neurons). **mTORC1 (downstream of TrkB-PI3K-Akt) activates SREBP**, which drives cholesterol biosynthesis, which enriches the lipid-raft environment TrkB needs. This closes a **feedforward loop: TrkB to mTOR to SREBP to cholesterol to TrkB localization/signaling.** Your observation linking **astrocyte cholesterol signaling to BDNF signaling** fits here. **Flag:** the full SREBP/mTOR/TrkB loop is inferred from component studies, not yet shown in one mood-disorder system; label it a model/hypothesis in the paper.
- The draft also adds a **TrkB-glucocorticoid-receptor interaction** (2026) mechanism, a direct stress-to-plasticity link worth integrating.

### 2.5 Cognition axis

BDNF/TrkB is required for late-LTP (ERK/CREB/BDNF; mTOR-4EBP1 local translation). Cognitive deficits in BD/MDD map to hippocampal/prefrontal circuits where BDNF plasticity is reduced. Cognition GWAS implicates synaptic biology broadly; BDNF-pathway genes appear in enriched sets though BDNF itself is rarely a top genome-wide locus.

### 2.6 BDNF/TrkB genetics in BD and depression (use carefully)

- **BDNF Val66Met (rs6265):** impairs activity-dependent BDNF secretion (~30%). Meta-analyses **conflict** (ORs ~0.95 to 1.13; population-specific). **Not** a robust genome-wide main-effect risk allele; model it as a **modifier of secretion/plasticity**, not a causal locus.
- **NTRK2 (TrkB):** suggestive, not genome-wide significant; stronger as **pharmacogenomic** (valproate response, PMID 40810762) and **transdiagnostic** (suicidality, cognition) signals.
- The point for the paper: BDNF/TrkB pathway genetics are **modest and context-dependent at the single-variant level**, which is precisely why an **aggregated, pathway-level** genomic readout (Section 5) is the right instrument.

**Uncertainties to flag in the paper (do not overclaim):** Val66Met main effect is weak/contested; the SREBP/mTOR/TrkB loop is inferred; adult proBDNF secretion is debated; BDNF-KCC2 evidence is strongest in development/ASD, less direct in adult BD/MDD.

---

## 3. Neuroplastogen / EVIDENT through-line (grant framing)

- The field consensus (Castren/Moliner): **all antidepressants and psychedelics converge on TrkB**; therapeutic action is **plasticity induction**, not receptor agonism. Ketamine/esketamine (approved TRD), psilocybin (late-stage TRD trials), MDMA (PTSD), and TrkB-targeting neuroplastogens follow this logic.
- **ARPA-H EVIDENT** (Evidence-based validation for behavioral-health therapeutics): **$139.4M, first 13 teams announced April 21, 2026**; funds objective measures, treatment-monitoring biomarkers, responder identification, and shared data, explicitly for **neuroplastogens, neuromodulation, digital therapeutics**, with a mandated psychedelic-research allocation. Likely under the **HSF** Mission Office (probable, not confirmed from primary ARPA-H pages).
- **Cytognosis's fit:** our BDNF-axis biology is the **mechanistic substrate** for exactly what EVIDENT therapeutics target. We offer an **objective, molecular-to-genomic biomarker** of the plasticity state EVIDENT wants to measure and a way to **identify responders** (who sits where on the Mood/neuroplasticity axis). This is a strong EVIDENT/HSF narrative and reinforces IGoR TA1.

---

## 4. The bridge: from postmortem biotypes to living people

The molecular biotypes are derived from **snRNA-seq of postmortem brain**, so they cannot be measured in living patients. That gap is the reason the platform exists, and the transition point from publishable science (Sections 1 to 3) to the proprietary layer (Section 5).

---

## 5. ⚠️ PLATFORM-CONFIDENTIAL: the factorized PRS and genotype factorization model (KEEP OFF THE PAPER)

> This section is the proprietary moat. Do not include in the bipolar paper or share with the consortium. It is the "add-on for IP."

**The idea.** Reconstruct the same BDNF-axis biotypes from a person's **genome alone** by computing **process-specific polygenic scores restricted to transcription-factor-bound regions**:

- **CREB-bound regions** (ChIP-seq) as a genome proxy for the **BDNF/TrkB neuroplasticity** program (Mood axis).
- **SREBP-bound regions** as a proxy for **cholesterol biosynthesis** (mechanistically tied to TrkB's cholesterol dependence, Section 2.4).
- Additional TF sets for the Cognitive axis.

Instead of one genome-wide PRS, aggregate GWAS variant effects **within each functionally defined, interpretable set**, yielding **per-person, process-specific axes**, a coordinate computable **noninvasively from genotype**. Validatable on genotype-only datasets (NeuroBioBank and others). This is a core component of the broader **genotype factorization model**.

**Honest novelty assessment (so we claim it precisely):**

| Component | Prior art | Our position |
|---|---|---|
| Per-person, per-pathway PRS | **PRSet (Choi 2023, PMID 36732591)** already does this | **Not novel**; cite it, do not claim it |
| Partition by **TF-binding regions** (ChIP-seq) as the unit | Not done as a PRS unit | **Novel** |
| TFs as **mechanistic process proxies** (CREB to neuroplasticity; SREBP to cholesterol/TrkB) | Not applied in PRS | **Novel**, mechanistically anchored |
| Axes as a **coordinate system** for stratification / treatment-matching | PRSet is an enrichment tool; not framed this way | **Novel framing/use** |

- **Do not overclaim** "per-person pathway PRS is new" (PRSet owns that). **Do claim** the TF-region-factorized, mechanism-anchored, coordinate-system formulation.
- Closest prior art to distinguish from: **PRSet**, **stratified-LDSC** (Finucane 2015, population-level enrichment only, no per-person scores), functionally-informed PRS (LDpred-funct, AnnoPred, PolyPred; whole-genome weights, not subset restriction).
- **Cheap de-risking step before building the pipeline:** run **stratified-LDSC** to confirm CREB-bound (and SREBP-bound) regions are **enriched for the relevant trait heritability**. If yes, the factorization is biologically justified.

This is what makes the postmortem biotypes **measurable in living people from genome alone**, the heart of the noninvasive Psychoverse coordinate.

---

## 6. Alignment with prior Cytognosis biotype research (`04-research/`)

This dossier deepens the molecular layer of work already in the repo:

- `transdiagnostic/transdiagnostic-micro.md` and `molecular-cellular-biotypes.md`: the BDNF/TrkB plasticity program is the **molecular instantiation** of the transdiagnostic micro-axes already mapped (BDNF/TrkB, E/I, mitochondrial, inflammation).
- `disease-biotypes/bipolar.md` and `mdd.md`: this is the BD-specific, BDNF-anchored axis decomposition.
- `neuroplastogen-response.md` and `neuromodulation-response.md`: the TrkB-convergent mechanism is the throughline to treatment response.
- `multiscale-biomarkers.md`: the factorized PRS is the **genomic scale** of the multiscale biomarker stack (genome to cell to circuit), feeding the Psychoverse coordinate (see the Psychoscope X-Labs draft).

---

## 7. Decision: what to publish vs keep separate

| Goes IN the bipolar paper (the PoC, claim priority) | Stays the PLATFORM moat (off paper) |
|---|---|
| The Mood-Thought(-Cognitive) **dimensional axes** | The **factorized PRS** (CREB/SREBP TF-region scores) |
| BDNF/TrkB molecular biology + the two branches | The **genotype factorization model** and genome-derived noninvasive proxies |
| Cholesterol-TrkB + astrocyte SREBP link (as model) | Operationalization into the **Psychoverse coordinate** |
| Discovery (McLean, published) + **OOD validation (MtSinai)** | Multiscale/multimodal integration; sensor/clinical deployment |
| The neuroplastogen/EVIDENT mechanistic tie-in | Cytognosis-generated/independent data |

**Principle:** publish the principle (the biology and that the axes exist and generalize) for priority and credit; own the platform (the genome-derived measurement, integration, and product). Do **not** fragment the biology to "save IP", the moat is the layer above.

**Compute/compliance:** McLean = published re-analysis (Cytognosis resources fine); MtSinai single-cell = Cytognosis resources if the DUA permits (paper work); **MtSinai WGS (controlled) = run inside Mt Sinai's approved environment with Panos's team**, not imported into Cytognosis; avoid Luria for anything Cytognosis-relevant (IPPIA). **Build the platform on published results + independent data only.**

**Credit:** Manolis is CC'd on all threads; lock clear **Shahin/Brad/Xikun** authorship of the axis framework (priority and IP point the same way).

---

## 8. Open scientific to-dos

1. Join the **neuroplasticity (CREB) and cholesterol (SREBP)** stories into one model; finalize the **Cognitive-axis** pathway set.
2. Integrate the **TrkB-glucocorticoid** (stress) and **TRPC** mechanisms from the draft.
3. Run **stratified-LDSC** to justify the CREB/SREBP factorization (de-risk before the full PRS pipeline).
4. Specify the **factorized-PRS** pipeline and the NeuroBioBank validation plan (platform).
5. Decide final paper scope with Brad and Xikun (Section 7 table).

## 9. Key references

Casarotto et al., Cell 2021 (PMID 33606976, [doi](https://doi.org/10.1016/j.cell.2021.01.034)); Moliner et al., Nat Neurosci 2023 (PMID 37280397, [doi](https://doi.org/10.1038/s41593-023-01316-5)); Gupta et al., Mol Neurobiol 2025 (PMID 40342191); Barde, physiopathology of BDNF 2025 (draft); WikiPathways WP4829 ([link](https://www.wikipathways.org/pathways/WP4829.html)); Leal et al., Neuropharmacology 2013 (PMID 23602987); Caviedes et al. 2017 (PMID 28078988); González-Castro et al., Bipolar Disord 2014 (PMID 25041243); Wang et al., BMC Psychiatry 2014 (PMID 25539739); Camarena et al., Pharmacol Rep 2025 (PMID 40810762); Choi et al. (PRSet), PLOS Genet 2023 (PMID 36732591); Finucane et al. (S-LDSC), Nat Genet 2015 ([doi](https://doi.org/10.1038/ng.3404)); van der Vaart et al., J Clin Psychiatry 2026 (PMID 42138588); ARPA-H EVIDENT ([program](https://arpa-h.gov/explore-funding/initiatives-and-sprints/evident), [awardees](https://arpa-h.gov/news-and-events/arpa-h-announces-first-research-teams-139-million-initiative-transform-behavioral)). Plus the draft's curated set (TrkB-TMD structure 2024; cholesterol CRAC-motif 2021; TrkB-GR interaction 2026; dendritic-spine BDNF 2020; SynGO BDNF gene set).
