# IGoR teaming: Cellanome and PsychIGoR (Cytognosis and IPAI), TA4 live-cell and single-cell laboratory

**Team PsychIGoR. IPAI (Purdue) prime, with its director, Ananth Grama, as PI. Cytognosis and IPAI lead the disease-model and AI core (TA1 and TA2); McLean Hospital (Harvard) anchors clinical genomics; the protocol layer (TA3) is LabOP-based. TA4 has two arms: Matt Tegtmeyer's academic lab at Purdue (all wet-lab experiments) and Cellanome (industry execution). Cellanome is advancing as the industry TA4 arm; the operating model is under active discussion.**

## The team has come together

- **Prime and PI:** IPAI, Purdue University; Ananth Grama, Director of IPAI, computation at scale and systems integration.
- **TA1 and TA2, the disease model and AI engine:** Cytognosis (Shahin Mohammadi) and IPAI. A decade of single-cell disease atlases, including the first multi-cohort single-cell atlas of schizophrenia (Ruzicka, Mohammadi et al., Science 2024), and, at insitro, multimodal virtual-cell modeling of NGN2 disease models using genome-wide optical pooled screening (POSH) plus Perturb-seq, the exact imaging-and-transcriptomics screens the R3200 is built to run.
- **Clinical and translational:** W. Brad Ruzicka, McLean Hospital, a Harvard Medical School affiliate, psychiatric single-cell genomics through PsychENCODE.
- **TA4 academic arm:** Matt Tegtmeyer, Purdue, runs all wet-lab experiments, including iPSC-neuron disease models with multi-modal fixed-cell readouts (RNA ~350-plex, protein ~50-plex, Cell-Painting-style morphology, and in-situ CRISPR-guide sequencing).
- **Computational morphology and imaging-model lead:** Anne Carpenter (IPAI/Purdue), inventor of Cell Painting and CellProfiler. Purely computational: interpretable models for morphology and cellular-imaging data. Consumes readouts from both TA4 arms as the common analysis layer.
- **Interoperable protocols (TA3):** an open, LabOP-based stack.

## What we are building

A self-updating, mechanistic causal model of psychiatric disease, starting with schizophrenia and extending to bipolar disorder in Phase III, that designs its own next experiments (TA2) and validates them in iPSC-derived neural models across penetrant genetic forms such as the 22q11.2 deletion, with transcriptomic, morphological, and functional readouts. Phase I is a phenotypic-triage screen on isogenic iPSC pairs, ready to run. The first joint use case we proposed, automating hypothesis testing through pooled CRISPR screens in neuron and glia co-cultures anchored in a tractable genetic disease model, is exactly the closed loop IGoR rewards.

## Where Cellanome fits (TA4)

- **The industry TA4 arm.** Cellanome and Matt Tegtmeyer's academic lab together satisfy the program's requirement of at least two TA4 laboratories. They are orthogonal, not redundant: Matt's lab delivers fixed-cell high-plex readouts at very high scale (RNA ~350-plex, protein ~50-plex, Cell-Painting-style morphology, in-situ CRISPR-guide sequencing); Cellanome brings live-cell and temporal readouts the fixed-cell academic arm cannot provide.
- **One instrument, two of our three core readouts.** The R3200, with programmable CellCage enclosures, longitudinal live-cell fluorescence imaging, and same-cell scRNA-seq, links time-resolved phenotype directly to the single-cell transcriptome in the same cell. That coupling is rare, and it is exactly what a causal, perturbation-based disease model needs to learn from.
- **In-lab perturbation.** Perturb-LINK pooled CRISPR lets us test TA1-predicted causal edges and feed the results straight back to the model.
- **Cross-arm concordance.** Running the same iPSC-neuron samples through both the academic fixed-cell platform and the Cellanome R3200 gives a built-in Phase I cross-platform reproducibility milestone, directly mapping onto the program's concordance gates. Anne Carpenter's computational morphology models serve as the common analysis layer that makes the two arms comparable.
- **Operating model.** We are discussing two options: placing an R3200 in a PsychIGoR lab (in-house control and capability building) versus sending cells and samples to Cellanome for execution (service model). Cellanome will provide pricing; the decision follows from those numbers. The 2026-06-17 call advanced this discussion with Cellanome eager to collaborate.
- **Clean division of labor.** We own the TA1 and TA2 modeling; Cellanome anchors the industry TA4 execution node returning model-ready data for automatic ingestion, with the LabOP protocol layer carrying assays in and data out.

## What we want to confirm

Two points shape how we scope the work. First, neuro readouts: the Cellanome neurobiology page shows calcium activity tracked on the R3200 in the neurosphere case study, so the precise question is whether calcium imaging is a standard, shipping capability today and at what temporal resolution (longitudinal calcium activity versus faster neuronal-firing readouts), or whether it sits in a separate configuration. Second, automation and interoperability: how the R3200 exposes assay execution and data (API or scripting) so it can plug into the universal, interoperable protocol layer (TA3, LabOP-based) we are building.

## Team and next step

| Role | Who |
|---|---|
| Prime and PI | IPAI, Purdue University; Ananth Grama (Director, IPAI) |
| TA1 and TA2 co-leads | Cytognosis Foundation (Shahin Mohammadi, sub-awardee) and IPAI, Purdue |
| Clinical and translational | W. Brad Ruzicka, McLean Hospital (Harvard Medical School affiliate) |
| TA4.1 academic experimental arm | Matt Tegtmeyer lab, Purdue (iPSC-neuron wet-lab experiments; fixed-cell high-plex readouts: RNA ~350-plex, protein ~50-plex, morphology, in-situ CRISPR-guide sequencing) |
| TA4.1 industry arm (advancing) | Cellanome (live-cell imaging, same-cell scRNA-seq, Perturb-LINK CRISPR on the R3200) |
| Computational morphology and imaging models | Anne Carpenter (IPAI/Purdue; interpretable models; no wet bench) |
| TA3 interoperable protocols | SIFT; Daniel Bryce (lead), Robert Goldman (advisory) |
| TA4.2 sequencing and bioinformatics | Illumina (optional / TBD) |
| Software and Systems Architect | Elham Jebalbarezi Sarbijan, IPAI/Purdue (tentative) |
| Project Manager | Patricia Purcell |

**Timeline.** Solution Summary due June 25, 2026; full proposal early August 2026. With the deadline close, we would like to confirm the TA4 role this week, with real budget attached. **Contact:** Shahin Mohammadi, mohammadi@cytognosis.org.
