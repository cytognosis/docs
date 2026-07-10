> [!WARNING]
> **Readout correction (2026-06-14):** the functional neuronal readout is **single-cell calcium imaging** (scalable, single-cell), not MEA. Calcium imaging is an optical/imaging modality covered by Cellanome's live-cell fluorescence imaging and high-content imaging, so **there is no electrophysiology-lab gap** and MEA is not required. Treat the 'MEA / electrophysiology gap' analysis below as superseded; the detailed MEA schema (formats, QC, encoders) is to be reworked to calcium imaging in the full-proposal build.

# TA4 Validated-Lab Marketplace: Platform Deep Dive

**Document type:** Internal research analysis, full version  
**Compiled:** 2026-06-14  
**Authors:** Cytognosis research team  
**Audience:** Internal; IGoR proposal development team only  
**Paired doc:** `TA4_labs__brief.md` (ADHD-friendly companion)

---

## Abstract

ARPA-H IGoR requires at least two validated laboratories (TA4) that execute reproducible, QC-gated experiments and return model-ready data to TA1. For the psychiatric cellular phenotyping program anchored on 22q11.2 deletion syndrome and idiopathic schizophrenia, TA4 must deliver three core modalities in Phase I: transcriptomic (single-cell RNA-seq), morphological (Cell Painting and high-content imaging), and electrophysiological (multi-electrode array). Two additional modalities, multi-omic (metabolomics, lipidomics, proteomics) and protein/protein-protein interaction (PPI) characterization, serve as Phase II extensions and optional TA1 causal-edge validators respectively.

This document reviews candidates against those requirements: Matt Tegtmeyer lab (Purdue; academic experimental arm, all wet-lab experiments, Element AVITI24 / Teton CytoProfiling), Cellanome (R3200 programmable CellCage, live-cell imaging plus same-cell scRNA-seq, Perturb-LINK; industry experimental arm), Anne Carpenter (computational morphology/imaging-model lead; no wet-lab bench), Illumina BioInsight (Billion Cell Atlas, perturbation-scale scRNA-seq), and Panome Bio (untargeted metabolomics, lipidomics, phosphoproteomics). SPOC Biosciences (cell-free protein arrays, SPR, Cryo-EM, MALDI) is assessed as a bounded optional add-on for protein-level PPI validation rather than a core cellular lab.

**Updated model (2026-06-17):** TA4 has two experimental arms that satisfy the ">= 2 TA4 labs" requirement. The **academic arm** is the **Matt Tegtmeyer lab (Purdue)**, running all wet-lab experiments using the **Element AVITI24 / Teton CytoProfiling** platform (RNA 350-plex + protein/phospho 50-plex + Cell-Painting-style organelle morphology + CRISPR-guide DISS; neuroscience panel; fixed-cell in-situ at massive scale). The **industry arm** is **Cellanome** (R3200 + Perturb-LINK; live-cell temporal). **Anne Carpenter** is the **computational morphology/imaging-model lead** (interpretable models, morphological profiling; no wet-lab bench). The two experimental platforms are orthogonal/complementary (Element = fixed-cell in-situ; Cellanome = live-cell temporal), enabling a cross-arm concordance check aligned with the program's 85% concordance gates. Illumina is Lab 3. SPOC and Panome are orthogonal optional additions for targeted tasks in Phases II and III.

---

## 1. What TA4 Must Deliver

### 1.1 Programmatic requirements from ARPA-H Appendix A

Appendix A of the IGoR solicitation (ARPA-H-SOL-26-155) states two TA4 objectives:

**Objective TA4-1: Validated Reproducible Experimentation.** Every experiment must be executed under a TA3-defined protocol, return QC-passing data, and meet concordance thresholds across the marketplace. The phase ramp is:

| Phase | Scope | Concordance threshold |
|---|---|---|
| Phase I (18 months) | Cultured cells; at least two team laboratories; intra-team validation | >= 80% intra-team |
| Phase II (18 months) | Multicellular systems; cross-team execution; >= 3 experiments | >= 90% cross-team |
| Phase III (24 months) | Unified marketplace; external researcher access; >= 3 labs | >= 90% across marketplace |

**Objective TA4-2: Marketplace Operations.** A request-to-return interface in which TA2 submits a defined experiment, TA3 generates the instrument-specific protocol, TA4 executes and returns a QC-rich, IGoR-common-data-model-formatted package to TA1. Phase I establishes the two-way capability communication; Phase II makes the interface operational; Phase III delivers the full marketplace with autonomous exception handling targeting >= 70% of exceptions.

Additional hard requirements from the solicitation:
- Instrument validation with IV&V calibration artifacts at each lab by end of Phase I.
- Data update latency <= 24 hours (Phase II) and <= 4 hours (Phase III) from data receipt to TA1 model update.
- Open data release at each phase milestone under Apache 2.0 (code) and CC BY 4.0 (documentation).

### 1.2 The phenotypic-triage screen: what TA4 executes in Phase I

Section 42.7 of the IGoR Research Master defines the Phase I phenotypic-triage screen. The screen runs a panel of penetrant psychiatric variants (22q11.2 deletion, TBX1 exon 2 CNV, and high-odds-ratio SCHEMA genes including SETD1A, GRIN2A, GRIA3, and CUL1) in isogenic iPSC-derived neurons and astrocytes, measuring three required modalities and two optional readouts:

| Modality | Phase | Rationale |
|---|---|---|
| **Transcriptomic** (scRNA-seq) | Required, Phase I | Pathway-space shifts, cell-type markers, variant-specific signatures; feeds TA1 directly |
| **Morphological** (Cell Painting, neuronal morphometry) | Required, Phase I | High-content morphological fingerprints; established in 22q11 by Carpenter's NeuroPainting (Tegtmeyer et al. *Nat Commun* 2025, DOI: 10.1038/s41467-025-61547-x) |
| **Electrophysiological** (MEA, patch-clamp) | Required, Phase I | Circuit-level dysfunction readout for GRIN2A (NMDA) and GRIA3 (AMPA) variants; maps to glutamate-signaling SCHEMA convergence |
| **Proteomic / metabolomic** | Optional, Phase II | Mechanistic depth for lipid, energy, or chromatin (SETD1A) pathways; validates TA1 causal edges |
| **Protein/PPI characterization** | Optional, Phase II-III | Binds TA1 predicted PPIs to biochemical validation; deep mutational scanning of variant panel |

The screen produces a ranked variant-to-phenotype map. Strong-signal lines anchor TA1 and are carried forward. Weak-signal lines are deprioritized.

### 1.3 TA3-TA4 interface contract

TA3 (SIFT, LabOP) delivers instrument-specific protocol specifications to TA4 through a four-layer stack (Intent, Protocol, Calibration, Hardware). TA4 laboratories must operate under those locked specifications and return exceptions through the RFC-governed change process. The TA4-TA1 interface delivers QC-rich data packages formatted to the IGoR common data model. Concordance is computed across the same experiment executed at two or more labs; failures below the threshold gate data ingestion into TA1.

---

## 2. Per-Candidate Platform Deep Dives

### 2.0 Matt Tegtmeyer Lab (Purdue) — Academic Experimental Arm + Element AVITI24 / Teton CytoProfiling

**Role in TA4:** Academic experimental arm. Matt Tegtmeyer's lab runs **all wet-lab experiments**: iPSC-neuron disease models, multi-modal same-cell readouts. Confirmed Purdue faculty; confirmed on PsychIGoR team 2026-06-15.

**Element AVITI24 / Teton CytoProfiling platform (verified 2026-06-17, elementbiosciences.com/products/aviti24/cytoprofiling).**

Single-cell and spatial co-detection of RNA, protein, phospho-protein, and cell morphology from one sample at subcellular resolution; imaging plus in-situ sequencing via Avidity Base Chemistry (ABC); next-day results; <1 hr sample prep; hundreds of thousands to millions of cells.

**Modalities:**

| Modality | Detail |
|---|---|
| **Cell morphology** | Nucleus, membrane, actin, ER, Golgi, mitochondria (Cell-Painting-style organelle features); onboard segmentation + feature extraction. Natively outputs Cell-Painting-like morphological profiles that feed directly into Anne Carpenter's computational models. |
| **RNA** | 350-plex subcellular in-situ; thousands of transcripts per cell |
| **Protein + phospho-protein** | 50-plex (surface, intracellular, phospho) |
| **DISS** | Direct In Sample Sequencing: untargeted 3' RNA, **in-situ CRISPR-guide sequencing**, expressed-mutation detection |
| **Neuroscience panel** | Exists (neurodifferentiation, neurotransmission/synaptic, neurodegeneration, neuroinflammation) -- directly relevant to Matt's iPSC-neuron work |

**Element vs. Cellanome (key differences for the two-arm concordance story):**

| Dimension | Element AVITI24 / Teton | Cellanome R3200 |
|---|---|---|
| Cell state | Fixed-cell, in-situ | Live-cell, longitudinal |
| Scale | Hundreds of thousands to millions of cells | Tens of thousands of CCEs per flow cell |
| Morphology | Cell-Painting-style organelle features natively | AI morphotyping from live brightfield + fluorescence |
| Transcriptomics | 350-plex in-situ RNA | Same-cell scRNA-seq (whole transcriptome) |
| CRISPR readout | DISS in-situ guide sequencing | Perturb-LINK same-cell guide + RNA |
| Temporal | Fixed endpoint (fast turnaround) | Multi-day longitudinal tracking |
| Relationship | Orthogonal/complementary to Cellanome | Orthogonal/complementary to Element |

The two platforms' differences are the basis of the cross-arm concordance story: same variant lines assayed on both, with Anne Carpenter's computational models as the common analysis layer.

> [!CAUTION]
> **Element is a platform Matt uses, not a confirmed teaming/partnership agreement.** Do not claim a formal Element partnership without confirmation. **[FLAG 2026-06-17: confirm Element teaming status before including in submission language.]**

---

### 2.1 Carpenter Laboratory (Anne Carpenter, PhD; Broad Institute / transitioning to Purdue/IPAI)

**Role in TA4:** **Computational morphology/imaging-model lead.** Anne's role is **purely computational**: she builds interpretable models for morphology and cellular imaging data, runs no bench, and provides the TA4 analysis + TA1/TA2 interpretability bridge. She consumes readouts from both the Matt Tegtmeyer lab (Element platform) and Cellanome arms. Her open-source infrastructure (CellProfiler, Cell Painting Gallery, JUMP) seeds TA3 data standards.

> [!NOTE]
> **Role correction (2026-06-17):** Prior drafts listed Anne as "TA4 experimental phenomics" (implying a wet bench). Correct classification is computational morphology/imaging-model lead. All wet-lab experiments in TA4 are run by Matt Tegtmeyer's lab (academic arm) and Cellanome (industry arm).

**Cost-model note:** Anne's budget line covers **personnel + compute**, not wet-lab capex. **[FLAG 2026-06-17: re-derive dollar figures after Anne reattribution from experimental to computational; defer to Shahin/Ananth.]**

**Platform summary.** Anne Carpenter's laboratory at the Broad Institute developed CellProfiler, the primary open-source platform for high-content image analysis, and pioneered Cell Painting, a six-dye multiplex morphological profiling assay that captures hundreds of morphological features per cell (Bray et al. *Nat Protoc* 2016; Cimini et al. *Nat Methods* 2023). The JUMP-CP consortium dataset contains Cell Painting profiles across >116,000 compounds and >15,000 gene perturbations in U2OS cells, with expanding coverage to additional cell types. This dataset is fully open and already formatted to Illumina's DRAGEN-compatible output standards.

**Optical pooled CRISPR screening.** The Carpenter laboratory published a pooled Cell Painting CRISPR screening platform that enables de novo inference of gene function through self-supervised deep learning, demonstrated in both standard cell lines and, critically for our program, neurons with complex and overlapping dendritic morphologies (Bray and Carpenter group, *Nat Commun* 2025, DOI: 10.1038/s41467-025-66778-6). This is directly relevant to the Phase I screen: pooled optical screening combines CRISPR guide identification via in situ sequencing (ISS) with morphological profiling of individual cells, yielding per-cell genotype-phenotype pairs at scale without splitting the sample for separate sequencing runs.

**NeuroPainting precedent.** The 22q11 isogenic iPSC neuronal differentiation and Cell Painting study (Tegtmeyer et al. *Nat Commun* 2025, DOI: 10.1038/s41467-025-61547-x) is the direct precedent for our Phase I anchor. It establishes that 22q11.2-deletion-specific morphological signatures exist in NGN2-derived neurons, are reproducible across wells, and can be captured by Cell Painting and CellProfiler. The Phase I screen expands this from one deletion and one modality to the full SCHEMA-plus-22q11 variant panel across morphological and transcriptomic modalities.

**Open standards contribution.** Carpenter's Cell Painting Gallery (AWS open data bucket), JUMP dataset, OASIS, and COBA serve as the TA3 reference standard for morphological data representation. This is the starting point for the TA3 schema seeding described in section 34 of the Research Master.

**Throughput and data types.** A single Cell Painting run on a standard 384-well plate captures >10,000 cells per well at sub-micron resolution across six channels. Optical pooled screening can evaluate hundreds to thousands of CRISPR perturbations in a single plate. Output: CellProfiler feature matrices (>500 features per cell), compressed TIFF image stacks, per-cell guide assignments from ISS barcode reads.

**MEA electrophysiology.** The Carpenter lab does not operate MEA rigs as a primary platform. For Phase I electrophysiology, either a dedicated MEA sub-CRO must be contracted or Cellanome's calcium-imaging proxy must substitute pending MEA data from a third provider.

**Transition note.** Anne Carpenter is transitioning to Purdue / IPAI (~September 2026). Broad Institute is the experimental home for the first 12 months of Phase I; subaward routing (Broad versus Purdue versus both) affects cost model and IP assignment and must be resolved before submission.

### 2.2 Cellanome (R3200 Programmable CellCage; Dwight Baker, SVP Product Development)

**Role in TA4:** TA4 Lab 2. Primary live-cell and same-cell transcriptomics laboratory.

**Platform architecture.** The Cellanome R3200 integrates six functions in a single walk-away instrument: cell loading and selection, longitudinal live-cell imaging (brightfield plus four-channel fluorescence at 4X and 10X objectives), programmable reagent and media delivery, CellCage enclosure management, RNA capture, and cloud data integration. Each flow cell contains tens of thousands of permeable CellCage enclosures (CCEs); cells remain adherent and viable within CCEs for experiments spanning days to weeks.

The key innovation is that every CCE is a matched experimental unit: its spatial address links live-cell imaging observations (morphological trajectories, calcium transients, fluorescent marker intensities) to end-point RNA-seq and, where specified, CRISPR guide reads from the same physical cells. No dissociation or transfer step intervenes; the well-documented loss of fragile CNS cells during enzymatic dissociation and the severing of longitudinal imaging continuity are both eliminated.

**Neurobiology-specific capabilities (from cellanome.com/neurobiology, accessed 2026-06-14).**

- Neurons, astrocytes, and microglia attach to fibronectin-, laminin-, or poly-L-ornithine-coated CCE surfaces without dissociation, preserving morphology and viability.
- Neurospheres (100 to 200 cells each) have been cultured in windowed CCEs, with axon extension, synapse formation, and calcium activity tracked over multiple days, and end-point RNA-seq linked back to each neurosphere's functional behavior.
- Microglia phagocytosis assay: individual microglia enclosed with fluorescent particles, phagocytic activity tracked over 12 hours, end-point transcriptome resolved per cell. High-activity microglia upregulated complement signaling, lipid metabolism, and lysosomal pathways, demonstrating that functional heterogeneity is transcriptomically distinguishable at single-cell resolution.
- Co-culture support: enclosed microglia can be layered over intact neuronal networks, enabling cell-cell interaction studies.

**Perturb-LINK (pooled CRISPR screening plus longitudinal imaging plus same-cell scRNA-seq).** The Perturb-LINK workflow delivers CRISPR guide libraries to CCE-enclosed cells, tracks live-cell phenotypes longitudinally, and reads out end-point guide identity plus transcriptome from the same cells. This is the single workflow that covers two of the three required Phase I modalities (morphological via live-cell imaging and transcriptomic via RNA-seq) in one experiment, with the guide barcode providing the perturbation identity for each cell.

**Data architecture.** The Cellanome Cloud platform produces a structured per-CCE data object linking perturbation delivery, morphological embeddings (AI-derived), multi-channel fluorescence timeseries, and end-point RNA/sgRNA reads. Output can be exported as Seurat-compatible `.rds` files for direct TA1 ingestion. AI-based morphotyping is integrated into the standard analysis pipeline without additional protocols.

**Throughput.** Tens of thousands of CCEs per flow cell run; scalable to screening libraries of hundreds to low thousands of perturbations per run. Turnaround is limited by differentiation time (NGN2 neurons: approximately 7 days for transdifferentiation, longer for patterned protocols) rather than instrument throughput.

**Electrophysiology.** Calcium imaging is available as a functional proxy for electrophysiology within the R3200 workflow. The platform does not provide patch-clamp or MEA as primary assays; MEA-based electrophysiology requires an external platform.

**Internal caveat (from TEAM_TRACKER.md, 2026-06-14).** The Cellanome relationship carries an interpersonal flag: the in-person product lead left a poor impression, and early NDA edits were shared from a personal account outside of counsel review. Process fix is in place (all NDAs routed through Duane Valz before sharing). Treat as TA4 only; do not expand Cellanome to TA3 despite any claims of protocol standardization capabilities.

### 2.3 Illumina BioInsight (Billion Cell Atlas)

**Role in TA4:** TA4 Lab 3. High-throughput perturbation-scale scRNA-seq; in-kind resource contribution.

**The Billion Cell Atlas (announced January 13, 2026; Illumina press release).** Illumina introduced the world's largest genome-wide genetic perturbation dataset on January 13, 2026, through its new BioInsight business division. The Atlas captures how 1 billion individual cells respond to CRISPR-based genetic perturbations (all 20,000 genes systematically switched on or off) across more than 200 disease-relevant human cell lines, including neurological disease cell lines. The full program targets 5 billion cells over three years (by early 2029).

**Technology stack.** The Atlas is powered by the Illumina Single Cell 3' RNA Prep platform operating on NovaSeq X / NovaSeq X Plus instruments, which enable millions of individual cells per experiment. CRISPR perturbations are delivered genome-wide. Data are processed through the DRAGEN pipeline with hardware acceleration and hosted on Illumina Connected Analytics. Projected data generation rate: 20 petabytes of single-cell transcriptomic data per year.

**Partnership context.** Founding pharma participants are AstraZeneca, Merck, and Eli Lilly. Illumina is in active discussion with the IGoR team (call scheduled for 2026-06-16 with Sebastian). The contribution model being explored is in-kind resource sharing: Atlas data access for neurological cell lines plus sequencing credits, estimated at approximately $4.0M combined with other in-kind items (section 34, Research Master).

**Fit to TA4 needs.** Illumina contributes primarily to the transcriptomic modality at perturbation scale. The Billion Cell Atlas's neurological cell lines can provide a reference context for our 22q11.2 isogenic screen and SCHEMA gene panel. In IGoR Phase I, Illumina's contribution as an in-kind partner lowers the experimental cost for bulk perturbation scRNA-seq runs. In Phase II and III, Illumina's high-throughput platform provides scaling capacity beyond what Cellanome's per-CCE workflow can reach for population-level statistical power.

**Coverage gaps.** Illumina does not provide live-cell imaging, morphological profiling, electrophysiology, or multi-omic readouts. As a sequencing platform, it is a pure transcriptomic node. Its value to TA4 is complementary: breadth and scale for the transcriptomic layer, not multimodal depth.

**Sequencing platform capabilities for TA3 protocol standardization.** Illumina's NovaSeq X and library preparation kits (DRAGEN pipeline) have ISOcompliant LIMS integration (Clarity LIMS) and documented SOP frameworks that align naturally with TA3's Hardware and Calibration layers. Seeding TA3 with Illumina's sequencing SOPs for single-cell library preparation provides a reproducible baseline.

### 2.4 Panome Bio (Multi-Omics; Adam Richardson, VP Operations)

**Role in TA4:** Alternate / optional add-on for Phase II multi-omic extension.

**Platform overview.** Panome Bio is a multi-omics contract research organization headquartered in St. Louis, Missouri, offering CLIA-certified untargeted metabolomics, lipidomics, phosphoproteomics, targeted proteomics, transcriptomics, and integrated multi-omic analysis (panomebio.com, accessed 2026-06-14). Their Next-Generation Metabolomics and Next-Generation Lipidomics services use untargeted LC/MS techniques to profile the full metabolome and lipidome without restriction to a predefined standards library.

**April 2025 phosphoproteomics launch.** Panome Bio announced global phosphoproteomics in April 2025 (press release via PRNewswire, 2025-04-29). The platform delivers unbiased, comprehensive analysis of both protein abundance and phosphorylation events, fully compatible with their metabolomics and lipidomics services. This enables integrated signal-protein-metabolite pathway analysis across all omics layers from the same sample.

**Neuroscience applications.** Panome Bio lists a dedicated neuroscience application area (panomebio.com/applications/neuroscience) and an Alzheimer's disease multi-omic integration application (panomebio.com/applications/multi-omics-in-alzheimers-disease). Published data reports include multi-omic integration of colorectal cancer cells and KRAS knockdown metabolic profiling. For our program, the relevant application is metabolic and lipidomic phenotyping of iPSC-derived neurons carrying SETD1A, CUL1, or 22q11.2 variants, where chromatin regulation and ubiquitin-proteasome disruption are expected to propagate to metabolic and lipid signatures (consistent with the Neurolipid Atlas findings in ApoE4 astrocytes, Sienski et al. *bioRxiv* 2024.07.01.601474).

**Integration approach.** Panome's proprietary bioinformatics database maps metabolomic, proteomic, and transcriptomic signals onto shared biochemical networks. The output is a multi-omics feature matrix amenable to integration with TA1's causal network. Their TissueBridge FFPE Metabolomics service extends to tissue samples if the program requires post-mortem brain validation.

**Fit to TA4 phases.** Panome does not cover cellular phenotyping (imaging, live-cell scRNA-seq, electrophysiology) and therefore is not a Phase I core anchor. As a Phase II optional extension, it would contribute the metabolic and lipidomic layer to variant lines with strong Phase I transcriptomic and morphological signals, adding mechanistic depth to TA1 causal-edge assignment.

**Status.** Panome Bio is listed as an Alternate in the team tracker (not yet contacted; hold until the core team is confirmed). Engagement is deferred until after the Carpenter, Cellanome, and Illumina relationships are settled.

### 2.5 SPOC Biosciences (Cell-Free Protein Arrays; Lydia Gushgari, PhD)

**Role in TA4:** Optional add-on for protein-level PPI validation; not a cellular phenotyping lab.

**Platform.** SPOC (Sensor-Integrated Proteome On Chip) uses cell-free in vitro transcription and translation (IVTT) on proprietary Protein NanoFactory systems to synthesize proteins directly on chip or sensor surfaces. Up to 2,400 unique full-length folded proteins or antibodies (VHH, scFv, Fab, mAb) per chip are captured via HaloTag in situ purification onto SPR biosensor slides or glass substrates. The platform supports real-time label-free kinetic analysis (on-rate, off-rate, affinity, residence time, expression level), Cryo-EM structure determination, and MALDI mass spectrometry.

**Key publications (from SPOC_Biosciences_teaming_2026-06-14.md):**

- Commun Biol 2025, DOI: 10.1038/s42003-025-07844-z: "Multiplexed proteomic biosensor platform for label-free real-time simultaneous kinetic screening of thousands of protein interactions." This is the primary platform description paper; it validates up to 2,400-plex simultaneous SPR kinetic measurements.
- bioRxiv 2025.01.11.632576: On-chip antibody library characterization.
- Biomolecules 2025, DOI: 10.3390/biom15060882: "Real-time SPR biosensing to detect and characterize fast dissociation rate binding interactions missed by endpoint detection." This paper motivates the SPR kinetic approach over endpoint assays for off-target toxicity screening and weak/fast-off binders.
- bioRxiv 2026.04.30.722015: High-throughput SPR characterization of antigen deep mutational scanning (DMS) variants for epitope mapping.

**Fit to IGoR.** The SPOC platform is orthogonal to the cellular modalities: it operates cell-free, not with iPSC-derived neurons. Its value lies downstream of the TA1 causal network, where the model predicts specific protein-protein interactions (e.g., altered SETD1A complex stoichiometry, CUL1 ubiquitin-ligase substrate binding, GRIN2A interaction partners after genetic perturbation). SPOC can confirm or deny those predicted edges at biochemical resolution, providing a direct TA1 causal-edge validation function. The deep mutational scanning (DMS) capability is also relevant for the variant panel: it can quantify the binding consequences of every amino acid substitution in a variant protein in a single experiment.

**What SPOC does not cover.** SPOC does not produce transcriptomic, morphological, or electrophysiological readouts. It cannot assess cell-state or cell-type context. It is suitable only for defined protein targets, not for hypothesis-free phenotypic screens.

**Status.** Inbound teaming request received 2026-06-14 (Lydia Gushgari). Scope call pending. Treat as optional; priority is lower than core cellular labs.

---

## 3. Capability-versus-Need Matrix

The following matrix maps each candidate against the five modalities required or desired by TA4 in the IGoR program, plus IGoR-specific structural criteria.

| Modality / Criterion | Carpenter / Broad | Cellanome R3200 | Illumina BioInsight | Panome Bio | SPOC Biosciences |
|---|---|---|---|---|---|
| **Transcriptomic (scRNA-seq)** | Partial (via optical pooled ISS reads; bulk RNA possible) | **Full** (same-cell RNA-seq per CCE, Seurat-ready export) | **Full** (perturbation-scale; 20 PB/yr rate; genome-wide CRISPR) | Partial (RNA-seq as add-on; not primary platform) | None |
| **Morphological (Cell Painting / imaging)** | **Full** (Cell Painting, CellProfiler, JUMP dataset, optical pooled CRISPR with morphology) | **Full** (brightfield + 4-channel fluorescence; AI morphotyping integrated) | None | None | None |
| **Electrophysiological (MEA / calcium)** | None (requires external MEA provider) | Partial (calcium imaging proxy; no MEA or patch-clamp) | None | None | None |
| **Multi-omic (metabolomic / lipidomic / proteomic)** | None | None | Partial (Illumina Protein Prep NGS-based proteomics via SOMAmer; limited) | **Full** (CLIA-certified untargeted metabolomics, lipidomics, phosphoproteomics, targeted proteomics) | Partial (expression + kinetics, not cellular omics) |
| **Protein/PPI characterization** | None | None | Partial (targeted proteomics via Protein Prep / SOMAmer) | Partial (discovery proteomics, mass spec) | **Full** (2400-plex SPR kinetics, DMS, Cryo-EM, MALDI) |
| **Live-cell longitudinal imaging** | None | **Full** (multi-day, temperature-controlled, programmable reagent delivery) | None | None | None |
| **Pooled CRISPR screening** | **Full** (optical pooled CRISPR, proven in neurons) | **Full** (Perturb-LINK in CCEs) | **Full** (genome-wide, 20K genes, >200 cell lines) | None | None |
| **Neuronal / CNS cell support** | Yes (NeuroPainting precedent; neuron optical pooled screening described with caveats) | **Yes** (neurospheres, neurons, microglia, astrocytes; adherent CNS cell protocols documented) | Yes (neurological cell lines included in Atlas) | Yes (neuroscience application listed; Alzheimer multi-omics case study) | Limited (cell-free; no cell-type context) |
| **Open data / TA3 seeding** | **Yes** (JUMP dataset open; Cell Painting Gallery; CellProfiler open-source) | Partial (Seurat-compatible export; proprietary cloud platform) | Partial (Atlas data may be licensed; sequencing SOPs open) | No (proprietary database; licensed service) | No |
| **IGoR marketplace fit (Phase I)** | Computational analysis layer (not a TA4 wet lab; see Section 2.1) | **Core anchor (industry arm)** | In-kind resource + Lab 3 | Phase II extension | Optional add-on |

**Summary judgment.** The two TA4 experimental arms — Matt Tegtmeyer's lab (Element AVITI24; academic) and Cellanome (R3200; industry) — together cover three of the five modalities directly: morphological (both arms), transcriptomic (Cellanome primary, Element DISS partial), and live-cell longitudinal (Cellanome). Anne Carpenter's computational models serve as the analysis layer across both arms; the Carpenter lab is NOT counted as a TA4 wet lab in Phase I. Electrophysiology is the critical Phase I gap; MEA must be sourced from a separate provider or the program must justify substituting calcium imaging as a proxy. Multi-omic and PPI validation are well-served by Panome and SPOC respectively as Phase II optional additions.

---

## 4. Recommended TA4 Composition and Laboratory Pairing

### 4.1 Anchor pair: Matt Tegtmeyer lab (academic arm) and Cellanome (industry arm)

> **Role correction (2026-06-17):** Prior drafts labeled this section "Anchor pair: Carpenter and Cellanome," treating Anne Carpenter as a TA4 experimental lab. The correct anchor pair is Matt Tegtmeyer's lab (academic arm) and Cellanome (industry arm). Anne Carpenter is purely computational; see Section 2.1.

**Matt Tegtmeyer lab anchors the academic experimental arm.** The NeuroPainting precedent (Tegtmeyer et al. 2025) establishes directly that 22q11.2 isogenic iPSC neurons express Cell Painting-detectable morphological signatures. Matt's lab runs all wet-lab experiments: iPSC-neuron disease models and multi-modal same-cell readouts using the Element AVITI24 / Teton CytoProfiling platform. Extending the NeuroPainting approach to the full SCHEMA variant panel is the Phase I screen. Anne Carpenter's open data infrastructure (CellProfiler, JUMP, Cell Painting Gallery) seeds TA3 schemas and satisfies the IGoR open-data mandate; her computational morphology models analyze the imaging data Matt's lab generates.

**Cellanome R3200 anchors the industry arm: live-cell imaging and same-cell transcriptomics.** The R3200's CellCage design resolves the primary technical limitation of standard scRNA-seq for adherent CNS cells: dissociation-induced state changes and loss of morphological context. By retaining cells in CCEs throughout imaging and RNA capture, Cellanome provides the same-cell morphological-plus-transcriptomic linkage that TA1 requires for model training. Perturb-LINK delivers the CRISPR perturbation identity within the same data object, enabling per-cell genotype-to-phenotype mapping without multiplexing or sample splitting.

**How the two arms compose.** Run the same isogenic variant lines at both arms under the same TA3 protocol. Matt's lab runs Cell Painting and optical pooled CRISPR screening via Element AVITI24. Cellanome runs Perturb-LINK (live imaging plus same-cell scRNA-seq) on the R3200. Anne Carpenter's computational morphology models serve as the common analysis layer, comparing morphological embeddings across both platforms. The concordance check for Phase I (>= 80%) compares the morphological and transcriptomic signatures on the shared variant panel; where both arms detect a robust signal, the line advances.

**Two-way capability communication (Phase I milestone).** Each arm documents instrument models, cell-line handling protocols, QC thresholds, and data format schemas in the TA3 calibration layer. SIFT's LabOP toolchain generates protocol specification files for both platforms, ensuring the same locked scientific parameters drive execution at both sites.

### 4.2 Illumina as TA4 Lab 3

Illumina's Billion Cell Atlas (January 2026 release) contributes two distinct values: (1) Atlas neurological cell-line perturbation data as a reference context for the Phase I isogenic screen (does the 22q11.2 morphological/transcriptomic signature generalize to the population-scale Atlas?), and (2) high-throughput sequencing capacity for Phase II bulk-perturbation experiments at scales beyond Cellanome's per-CCE throughput. The in-kind contribution (~$4.0M combined) reduces direct sequencing costs and de-risks the budget.

Illumina's engagement (Sebastian; call scheduled 2026-06-16) should scope: which Atlas neurological cell lines include 22q11.2 or SCHEMA-gene perturbations, what data access model applies to IGoR performers, and whether dedicated sequencing runs on our isogenic lines are included in the in-kind package.

### 4.3 SPOC Biosciences: optional bounded add-on

SPOC addresses a specific, bounded TA4 sub-task: protein-level validation of TA1-predicted PPIs and quantitative deep mutational scanning of variant proteins. Its value is highest in Phase II or III, after TA1 has produced a curated set of predicted causal edges (e.g., altered SETD1A complex assembly, CUL1 substrate binding shifts, GRIN2A-PSD95 interaction changes). At that point, SPOC's 2,400-plex SPR platform can confirm or deny those edges in a single experiment. The SPR kinetic readout (on-rate, off-rate, affinity, residence time) is more informative than endpoint binding assays for distinguishing strong from weak interactions.

The scope call with Lydia Gushgari should confirm whether SPOC has reagents for recombinant psychiatric-disease-relevant proteins (SETD1A domains, CUL1/SKP1 complex, GRIN2A extracellular domain) and whether plasma/CSF proteomics from patient biobanks (McLean cohort data) falls within their service scope.

### 4.4 Panome Bio: optional Phase II extension

Panome Bio is most valuable if a Phase I variant line produces a strong transcriptomic but mechanistically ambiguous metabolic or lipid signature. For example, SETD1A haploinsufficiency is predicted to alter histone H3K4 methylation and downstream metabolic gene expression; a lipidomic or targeted metabolomic profile would provide orthogonal evidence. Similarly, CUL1 dysfunction (ubiquitin-proteasome) is expected to produce a proteomic turnover shift detectable by phosphoproteomics.

Panome's integrated multi-omic pipeline (metabolomics + lipidomics + phosphoproteomics + transcriptomics from one sample) aligns with the IGoR "all from the same cells" aspiration, but the requirement for separate sample aliquots (LC/MS is destructive) means it cannot be a same-cell assay within a single Cellanome run. Coordination with Cellanome at the sample-splitting step is required.

**Engagement timing.** Hold Panome engagement until after the Carpenter, Cellanome, and Illumina relationships are confirmed and the Phase I variant-to-phenotype map is designed. Panome selection should be driven by which Phase I variants show the most mechanistically interesting but transcriptomically incomplete signatures.

---

## 5. Alignment to TA4 ISO Objectives and Phase Ramp

### 5.1 Phase I (18 months): Concept and Component Validation

| IGoR requirement | How the recommended TA4 covers it |
|---|---|
| At least 2 TA4 laboratories | Matt Tegtmeyer lab (Purdue; academic arm) + Cellanome (industry arm); Anne Carpenter is the computational analysis layer, not a TA4 wet lab |
| Two-way capability communication established | TA3 (SIFT/LabOP) documents both arms' instrument specs, SOPs, and QC thresholds in Phase I kick-off workshop |
| Instrument validation with IV&V artifacts | IV&V calibration slides / standard cell-line controls run at both arms; concordance computed |
| >= 80% intra-team concordance | Element AVITI24 morphological features and Cellanome morphotype embeddings compared on same variant lines; RNA-seq signature overlap computed via Anne Carpenter's computational models |
| Walking skeleton closed loop | TA2 proposes experiment, TA3 generates Matt Tegtmeyer lab and Cellanome protocol specs, both arms execute, data returned to TA1 within <= 24 hrs |
| Phase I anchor experiment | 22q11.2 isogenic iPSC neurons (TBX1 exon 2 CNV validation line) at both Matt Tegtmeyer's lab (academic arm) and Cellanome (industry arm); Anne Carpenter's models analyze both arms' morphological data |
| >= 2 modalities | Morphological (Matt Tegtmeyer lab + Cellanome) + Transcriptomic (Cellanome) = 2 primary; calcium imaging = partial electrophysiology proxy |

**Electrophysiology gap resolution for Phase I.** None of the three anchor labs provides MEA electrophysiology. Mitigation options: (a) subcontract a CRO with proven iPSC-neuron MEA capacity (e.g., AxoSim, Axion Biosystems as a service, or a collaborating academic MEA lab); (b) designate calcium imaging from Cellanome as the Phase I electrophysiology proxy and commit to MEA integration in Phase II; or (c) bring MEA on-site at Purdue/IPAI for the isogenic lines. Option (b) is the lowest-friction Phase I solution and should be stated explicitly in the proposal with Phase II MEA-integration milestones.

### 5.2 Phase II (18 months): Integration and Interoperability

| IGoR requirement | How the recommended TA4 covers it |
|---|---|
| Multicellular systems | Cellanome supports co-culture (neuron-glia, neuron-microglia); Matt Tegtmeyer's lab runs co-culture Cell Painting imaging; Carpenter's computational models analyze the resulting morphological data |
| >= 3 labs executing >= 3 experiments | Matt Tegtmeyer lab + Cellanome + Illumina; experiments: isogenic screen (Phase I variant lines), second disease area extension, Illumina Atlas concordance check |
| >= 90% cross-team concordance | Same variant lines run at Matt Tegtmeyer's lab and Cellanome; concordance on morphological embeddings and transcriptomic pathway scores via Carpenter's computational models |
| Marketplace request/return interface | TA2 submits experiment request via API; TA3 generates protocol; lab executes; data returned to TA1 |
| Optional multi-omic | Panome Bio engaged for Phase II extension if Phase I reveals metabolically interesting lines |
| Optional PPI validation | SPOC engaged if TA1 produces testable PPI predictions from Phase I model training |

### 5.3 Phase III (24 months): Scaling and Generalization

| IGoR requirement | How the recommended TA4 covers it |
|---|---|
| Unified marketplace across teams | Matt Tegtmeyer lab, Cellanome, Illumina operating under shared TA3 protocol schemas; Carpenter's computational models as the cross-platform analysis layer; cross-team experiment at >= 90% concordance |
| >= 70% exceptions handled autonomously | TA3 exception-handling logic built on RFC process; Cellanome's Cloud platform and Illumina's DRAGEN pipeline support automated QC gates |
| Second disease area extension | Idiopathic schizophrenia (polygenic) and optional bipolar extension; same lab roster; TA1 disease axes projected from Phase I anchor |
| External researcher access | JUMP / Cell Painting open data layer; Illumina Atlas access; IGoR common data model published |
| Connect-a-thon | Cross-team reproducibility demonstration; Matt Tegtmeyer lab and Cellanome protocols submitted to LabOP standard; Carpenter's computational pipeline validated across both arms |

---

## 6. Gaps and Interface Analysis

### 6.1 Critical gap: electrophysiology

The electrophysiological modality (MEA or patch-clamp) is required for the Phase I screen because GRIN2A (NMDA receptor) and GRIA3 (AMPA receptor) variants implicate synaptic transmission directly. None of the four primary TA4 candidates provides MEA as a primary service. This is the single largest TA4 gap. Resolution options in order of preference:

1. **Designate Cellanome calcium imaging as Phase I electrophysiology proxy.** Most tractable for Phase I; committed with Phase II MEA upgrade.
2. **Subcontract AxoSim or Axion Biosystems** (both offer iPSC-neuron MEA as a service). This adds a fourth wet-lab performer in Phase I, which exceeds the minimum and demonstrates execution depth.
3. **Bring MEA capacity on-site at Purdue/IPAI** using Axion's Maestro MEA system or similar. One-time capital cost (~$150K) plus operations. This is feasible but increases budget.

### 6.2 TA3-TA4 interface: protocol spec delivery

TA3 (SIFT, LabOP) must generate protocol specification files that both Carpenter (CellProfiler workflows, optical pooled CRISPR ISS cycles) and Cellanome (R3200 run configurations, CCE loading specs, Perturb-LINK guide delivery) can ingest. LabOP currently has OpenTrons and SiLA instrument primitives; CellProfiler pipeline specs and Cellanome R3200 run configs are not yet in the LabOP standard. This is a Phase I standards-development deliverable: both labs must work with SIFT to encode their instrument capabilities in the LabOP Calibration and Hardware layers.

**Action item:** Confirm with SIFT (Dan Bryce, Robert Goldman) that extending LabOP to the CellProfiler imaging pipeline and Cellanome R3200 API is in scope for Phase I. This is the central TA3-TA4 interface risk.

### 6.3 TA4-TA1 interface: data format and update latency

TA1 requires QC-rich data packages formatted to the IGoR common data model. Key format requirements:
- Carpenter: CellProfiler feature matrices and ISS barcode reads must be converted to TA1-compatible format. CellProfiler output is CSV-based; conversion to the common data model needs a lightweight ETL step.
- Cellanome: Seurat-compatible `.rds` export aligns well with TA1's expected scRNA-seq input. The morphological embedding objects need a defined serialization schema.
- Illumina: DRAGEN/BaseSpace output (BAM, h5 matrices) is standard; conversion pipeline is well-understood.

The Phase II latency requirement (<= 24 hours) and Phase III requirement (<= 4 hours) are achievable for the transcriptomic and morphological readouts but may be challenging for long-duration live-cell experiments (multi-day Cellanome runs) where partial data is generated continuously. The data return specification must distinguish between end-of-run final packages and streaming QC updates.

### 6.4 Same-cell multimodal integration

The IGoR program aspires to same-cell integration across modalities. Cellanome's R3200 achieves this for morphology plus transcriptomics. Extending to electrophysiology (MEA) in the same experimental unit is currently not possible with any of the four candidates; MEA reads out population-level or electrode-local signals, not single-cell RNA. The realistic model is: run Cellanome for same-cell morphology and transcriptomics, run a separate MEA experiment on the same isogenic lines for population-level electrophysiological signatures, and match signatures computationally at the cell-line level rather than the single-cell level.

### 6.5 Sub-performer overlap rule

If a second IGoR team selects Illumina or Carpenter as a TA4 performer, the ARPA-H sub-performer overlap rule may require the overlapping sub-performer to elect one project or may fund the work only once. The proposal should acknowledge this risk and name the backup strategy (Panome Bio for multi-omic expansion, an additional academic imaging core for morphological backup).

---

## References and Citation Status

All citations below should be verified against PubMed, DOI resolvers, or official press releases before proposal submission.

| Item | Citation | Verification status |
|---|---|---|
| 22q11 NeuroPainting precedent | Tegtmeyer et al. *Nat Commun* 2025, DOI: 10.1038/s41467-025-61547-x | **Verify** (cited in Research Master section 34; confirm DOI resolves and authorship includes Carpenter lab) |
| Pooled Cell Painting CRISPR screen | Bray and Carpenter group, *Nat Commun* 2025, DOI: 10.1038/s41467-025-66778-6 | **Verify** (confirm authorship and year from Nature Communications website) |
| JUMP Cell Painting dataset | Chandrasekaran et al. *Nat Methods* 2023 and JUMP-CP consortium papers | **Confirm** exact citation; JUMP-CP is publicly documented on GitHub (jump-cellpainting.github.io) |
| SPOC platform | Commun Biol 2025, DOI: 10.1038/s42003-025-07844-z | **Verify** (DOI confirmed in SPOC inbound doc; confirm title: "Multiplexed proteomic biosensor platform for label-free real-time simultaneous kinetic screening of thousands of protein interactions") |
| SPOC fast-off SPR | Biomolecules 2025, DOI: 10.3390/biom15060882 | **Verify** |
| SPOC antibody on-chip | bioRxiv 2025.01.11.632576 | **Verify** |
| SPOC DMS antigen | bioRxiv 2026.04.30.722015 | **Verify** (2026 preprint; confirm accessibility) |
| Illumina Billion Cell Atlas | Illumina press release, January 13, 2026; investor.illumina.com | **Confirmed** (fetched 2026-06-14) |
| Panome Bio phosphoproteomics | PRNewswire, April 2025 | **Confirm** exact date and content |
| CellProfiler / Cell Painting | Bray et al. *Nat Protoc* 2016 (Cell Painting assay); Cimini et al. *Nat Methods* 2023 (Cell Painting Gallery) | **Confirm** Cimini et al. 2023 DOI |
| SCHEMA rare variants | Singh et al. 2022, *Nat Genet*, PMID: 35396579 | **Confirmed** (Research Master section 42) |
| 22q11 psychosis risk | Schneider et al. 2023, PMID: 36786112 | **Confirmed** (Research Master section 42) |
| Neurolipid Atlas (context for Panome fit) | Sienski et al. *bioRxiv* 2024.07.01.601474 | Preprint; not yet peer-reviewed; use as supporting context only |
