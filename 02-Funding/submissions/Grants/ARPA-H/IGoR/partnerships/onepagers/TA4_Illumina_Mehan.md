# IGoR teaming: Illumina as the TA4.2 sequencing and bioinformatics readout

**Team PsychIGoR. IPAI (Purdue) prime, with its director, Ananth Grama, as PI; Cytognosis and IPAI lead the disease-model and AI core (TA1 and TA2); McLean Hospital (Harvard) anchors clinical genomics. We are assembling the validated-laboratory layer (TA4) of an ARPA-H closed-loop program, and would value Illumina as the sequencing and bioinformatics node (TA4.2), downstream of the wet-lab partners.**

## The closed loop, and where sequencing sits

IGoR funds a self-updating loop: a causal disease model (TA1) designs the highest-value next experiment (TA2); validated laboratories run it (TA4) and return model-ready data that updates the model. We are organizing TA4 in two layers:

- **TA4.1, wet-lab and perturbation.** Cell culture, isogenic iPSC models, perturbation, and imaging (Matt Tegtmeyer's lab at Purdue as the academic experimental arm; Cellanome as the industry arm for live-cell imaging and same-cell library prep). These partners generate cells, run perturbations, and prepare libraries. Anne Carpenter contributes computational morphology and imaging models as the common analysis layer; she does not operate a wet bench.
- **TA4.2, sequencing and bioinformatics (Illumina).** Each iteration produces single-cell and bulk libraries that must be sequenced and processed quickly, then returned to the model: NovaSeq sequencing, DRAGEN for standardized high-speed processing, and Illumina Connected Analytics (ICA) as the data backbone.

Illumina sits **downstream of the cell work**, so there is no wet-lab or cell-culture burden on your side: prepared libraries in, standardized model-ready data out.

## Why this fits Illumina, and the bioinformatics core

- **Genome-wide single-cell transcriptomics is the readout**, Illumina's core strength. The targeting lives in which lines and perturbations the wet labs run, not in the sequencing, so the genome-wide capability is the asset.
- **Sequencing and bioinformatics only.** Cell culture, perturbation, and imaging belong to the TA4.1 partners; Illumina owns the readout and the data pipeline.
- **The loop's cycle-time target rests on the data layer.** DRAGEN's speed and ICA's standardized, machine-readable outputs are what let each iteration flow back into the model fast enough to hit the program's acceleration goal. The bioinformatics layer is load-bearing here, not downstream cleanup.
- **Precedent is established.** Illumina already supports an ARPA-H genomic-data program (the PCX pediatric effort with D3b, using DRAGEN and ICA), so a research collaboration on a federal program is a known path rather than net-new.
- **Optional single-cell chemistry.** If useful at the TA4.1-to-TA4.2 handoff, PIPseq (instrument-free single-cell) offers a standardized library-generation interface.

## Protocols and interoperability

TA3 provides protocol portability, built on LabOP, so an experiment can move between laboratories. Illumina's interface is well-defined under either workable arrangement:

- LabOP standardizes protocols across both TA4.1 (assays and perturbation) and TA4.2 (sequencing), giving one portable representation end to end; or, more likely,
- LabOP remains the independent protocol layer, and each laboratory translates its own needs into executable protocols, including the sequencing handoff. Either way, TA4.2 is a clean, standardized interface: defined libraries and sample sheets in, DRAGEN and ICA outputs out.

## Team and next step

| Role | Who |
|---|---|
| Prime and PI | IPAI, Purdue University; Ananth Grama (Director, IPAI) |
| TA1 and TA2 co-leads | Cytognosis Foundation (Shahin Mohammadi, sub-awardee) and IPAI, Purdue |
| Clinical and translational | W. Brad Ruzicka, McLean Hospital (Harvard Medical School affiliate) |
| TA4.1 academic experimental arm | Matt Tegtmeyer lab, Purdue (iPSC-neuron wet-lab experiments) |
| TA4.1 industry arm | Cellanome (live-cell imaging, same-cell scRNA-seq; advancing) |
| Computational morphology and imaging models | Anne Carpenter (IPAI/Purdue; no wet bench) |
| TA4.2 sequencing and bioinformatics | Illumina (optional / TBD) |
| Interoperable protocols (TA3) | LabOP-based |

**Timeline.** Solution Summary due June 25, 2026; full proposal early August 2026. We would value a short conversation to scope the TA4.2 role and the collaboration vehicle that fits Illumina best (in-kind sequencing and reagents, an investigator collaboration, or a named subcontract). **Contact:** Shahin Mohammadi, mohammadi@cytognosis.org.
