# ARPA-H IGoR: a self-updating causal model of psychiatric disease, with the lab loop to prove it

**Team PsychIGoR. A partnership opportunity, anchored by IPAI (Purdue University) as prime with Ananth Grama as PI, and Cytognosis and IPAI leading the disease-model and AI core (TA1 and TA2). We are now assembling the experimental partners (TA3 and TA4) for a full-team proposal.**

ARPA-H's **IGoR** program (ARPA-H-SOL-26-155) will fund about three teams to build a closed loop that produces validated biomedical knowledge at least **10x faster**: mechanistic disease models (TA1), an AI engine that designs experiments (TA2), interoperable protocols (TA3), and a validated-laboratory marketplace (TA4). A responsive proposal must cover all four areas. **Solution Summary due June 25, 2026; full proposal in early August 2026.**

## The idea

Most AI cell models are correlational and never update. We build the opposite: a **mechanistic, multiscale, causal model of disease that updates from every new experiment**, in which **disease-associated genetic variation is treated as the perturbation** that drives cellular biology. An AI New Science Engine reads that model, finds the most informative knowledge gap, and designs the next experiment, closing the loop with the laboratory.

**Disease focus: schizophrenia, extending to bipolar disorder.** Psychiatric disease is largely polygenic and hard to model in a dish, so we start where the genetics is **penetrant and near-Mendelian**, namely the 22q11.2 deletion and large-effect rare-variant genes such as SETD1A and GRIN2A. This mirrors how familial Alzheimer (APP, PSEN1) and Parkinson (LRRK2, SNCA) variants made those diseases tractable in cells, then generalizes to idiopathic disease.

## What the anchor team brings (TA1 and TA2)

- **TA1, comprehensive disease models** (Cytognosis with IPAI): a cell-type-aware, mechanistic, multiscale causal model that turns **pretrained genomic foundation models into interpretable disease-axis factors**, ingests single-cell atlases and perturbation data, and **updates automatically** as new results arrive, built on open standards.
- **TA2, the New Science Engine** (Cytognosis and IPAI): an orchestration layer that interrogates the **TA1 model itself**, not just the literature, runs competing hypotheses, and designs the highest-value next experiment. It is explicitly **not a wrapper around a single large language model**.
- **A partner-ready Phase I experiment: a phenotypic-triage screen.** Using **isogenic iPSC pairs** (a healthy line with each variant introduced by CRISPR, the matched controls patient lines lack), we screen the penetrant-variant panel for **transcriptomic, morphological, and functional calcium-imaging** phenotypes, extending the published 22q11 Cell Painting work to more variants and readouts to select the lines that anchor the model.

## Partners we are assembling (TA3 and TA4)

We are in **active discussion with several leading groups** and are finalizing the experimental side of the team. We are looking for partners who bring one or more of the following:

- **TA3, interoperable protocols:** experience with open protocol standards and laboratory automation (for example LabOP-style declarative protocols and LinkML schemas), so an experiment transfers between labs as easily as a data file.
- **TA4, validated laboratories** (a team needs at least two): strengths across **live-cell imaging with same-cell single-cell RNA-seq, pooled CRISPR (Perturb-seq), high-content morphological (Cell Painting) screening, single-cell calcium-imaging neuronal activity, and multi-omics**, with a track record of cross-laboratory reproducibility.

If your group runs any of these at scale, there is a clear, fundable role for you on this team, with real budget attached.

## Team and roles

| Role | Who |
|---|---|
| Prime and Principal Investigator | IPAI, Purdue University; Ananth Grama |
| TA1 and TA2 co-leads (disease models, AI engine) | Cytognosis Foundation (Shahin Mohammadi, sub-awardee) and IPAI, Purdue |
| TA4 academic experimental arm | Matt Tegtmeyer lab, Purdue (iPSC-neuron wet-lab experiments; fixed-cell high-plex readouts: RNA ~350-plex, protein ~50-plex, Cell-Painting-style morphology, in-situ CRISPR-guide sequencing) |
| TA4 industry arm | Cellanome (live-cell imaging, same-cell scRNA-seq, Perturb-LINK CRISPR; advancing) |
| Computational morphology and imaging models | Anne Carpenter (IPAI/Purdue; interpretable models; TA4 analysis layer) |
| Clinical and translational | W. Brad Ruzicka, McLean Hospital |
| Project Manager | Patricia Purcell |
| Software and Systems Architect | Elham Jebalbarezi Sarbijan, IPAI/Purdue (tentative) |
| TA3 interoperable protocols | SIFT; Daniel Bryce (lead), Robert Goldman (advisory) |
| TA4.2 sequencing and bioinformatics | Illumina (optional / TBD) |

**Why this team.** A causal-modeling and AI core with deep single-cell and psychiatric-genetics expertise, an open-standards and reproducibility commitment that fits the ARPA-H mandate, and a concrete Phase I experiment that an experimental partner can run from day one.

**Timeline.** Solution Summary June 25, 2026; full proposal early August 2026. We are finalizing the team now and welcome a conversation this week.

**Contact.** Shahin Mohammadi, Cytognosis Foundation, mohammadi@cytognosis.org.
