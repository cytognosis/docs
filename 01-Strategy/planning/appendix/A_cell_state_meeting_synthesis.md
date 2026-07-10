# Appendix A: Cell-State / Perturbation Modeling Meeting Synthesis

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: leadership
> **Tags**: `strategy`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

**Date:** 2026-05-07
**Source:** [Google Meet notes](https://docs.google.com/document/d/16slm-XKv_Hejr4gby7OpLFcPqqUIa6UMK07pzKWbkts/edit)
**Attendees:** Shourya Verma (Purdue, lead RA), Nadia Atallah Lanman (Purdue), Ananth Grama (Purdue, faculty), Shahin Mohammadi (Cytognosis), Mango Wang (Meta, contributor), additional Purdue IPAI team members
**Companion to:** `11_technical_track_FMs.md`

This synthesis records the architectural decisions and operational decisions taken at the cell-state / perturbation-modeling meeting. Decisions are normative; the technical-track document (`11_technical_track_FMs.md`) is built on this record.

## Decisions

### Architectural

- Build cellular and connectomic foundation models **in parallel** using the same architectural building blocks at two scales.
- The shared building blocks are: WaveGC (Wave Graph Convolution) for multi-resolution graph diffusion, plus AlphaGenome-style cross-resolution transformer attention for inter-block information sharing.
- Replace WaveGC's MLP block (which is oblivious across scales) with the AlphaGenome interconnected attention pattern.
- Implement the multi-resolution wavelet plus cross-scale attention layer as a **standalone reusable package** (the "Lego pieces" approach) inside the `neuroconnectomics` repository, used by both connectomic and cellular tracks.
- Treat the molecular foundation model as a **trainable component** of the cellular FM, with end-to-end gradient flow through cross-resolution attention bridges. This is distinct from scPrint2 / TranscriptFormer which freeze the molecular FM as a static dictionary.
- Model the **residual space** (delta from healthy baseline) using conditional flow matching, generating counterfactual states from noise conditioned on health-state context.

### Repository structure

Four parallel repositories:

- `neurogenomics`: genome-level work, WGS, baseline molecular FM fine-tuning. Mohammadi initial lead.
- `neuroconnectomics`: connectomic FM, voxel-level work, multimodal imaging integration. **Hosts the shared `neuroconnectomics-core` Lego-pieces package.** Shourya lead.
- `neurotranscriptomics`: cellular FM, single-cell + pseudobulk, multi-scale molecular-to-cellular work. Shourya + Mango (bandwidth allowing) + Mohammadi.
- `neurobehavior`: macro phenotyping, LLM-derived neurobehavioral axis quantification, NBO ontology integration. Mohammadi initial lead.

A `neurogenomics` Cookiecutter template will be created (Mohammadi action item) so each repo bootstraps with the Cytognosis dev-standards.

### Roles

- Shourya leads both connectomic AND cellular tracks given Mango's transition to Meta.
- Mango contributes to cellular as bandwidth allows; remains formally on the team.
- Mohammadi is the primary advisor on the cellular track, despite less hands-on connectomic experience.
- Grama is the on-paper supervisor at Purdue and primary subaward channel.
- Mohammadi visits Purdue at end of May or early June 2026 to white-board three-to-six-month milestones; Grama covers travel reimbursement.

### Pre-training and prototyping

- **Connectomic.** Pre-training task: stratified subgraph masking. Initial prototyping on Open Era's Y dataset (~300 samples, harmonized). Scale-up: Yale dataset (Shourya secures access), then UK Biobank (≥40K fMRI), then ABCD, HCP.
- **Cellular.** Masked gene prediction conditioned on cellular context; perturbation prediction. PsychENCODE pseudobulk first (open). NeuroBioBank WGS for genotype-phenotype joint training. Allen Brain Atlas microarray data for connectomic deconvolution alignment.

### Cross-track integration

- Bridges between cellular and connectomic FMs trained on **paired data**: ENIGMA consortium primary (disease-centric, multimodal, fMRI plus genotype); PsychENCODE 388 paired samples secondary.
- Strategy: cross-attention or contrastive loss objectives with the alignment task simplified by both models being phenotype-oriented.

### Publication strategy

- First publication: multi-scale infrastructure connecting molecular and cellular data. Connectome **excluded** from this first paper to keep scope clean.
- Connectomics methods paper: separate output, also targeting Nature Methods or Nature Machine Intelligence.
- Mohammadi noted Nature Machine Intelligence is rapidly growing in impact factor and emphasizes methodology over result-centric framing.

### Project management

- Adoption of Monday.com for project management with OKRs.
- Quantitative metrics for success defined at the milestone-planning visit.
- Industry-style approach intended to improve project definition and tracking.

## Action items recorded

| Owner | Item |
|---|---|
| Shahin Mohammadi | Send WaveGC paper and code repository links to Shourya and Mango. |
| Shahin Mohammadi | Create and share non-connectomics Copier repository for boilerplate. |
| Shahin Mohammadi | Create discussion thread for prioritized neuro datasets and FM papers (include Tier 1 papers like Neurostorm). |
| Shourya Verma | Download Y dataset from Open Era. |
| Shourya Verma | Implement separate standardized package containing wavelet and transformer convolution layer; refactor components from WGC and AlphaGenome repos. |
| Group | Define architecture: explore whether projection back to original space is needed after each spectral graph convolution layer or only at the outside boundary. |
| Shourya Verma | Acquire Yale dataset access permission. |
| Shourya Verma | Build basic architecture and implement spectral graph convolution; build pre-training with graph masking. |
| Shourya Verma | Manage both connectomic and cellular development since Mango is unavailable. |
| Group | Implement Monday-based project tracking using OKRs. |
| Shourya Verma | Provide progress update next week. |

## Open architectural questions

- Projection back to original space: per layer or only outermost? Affects standardized embedding-layer interface.
- Conditioning structure for conditional flow matching: categorical disease label, continuous health-state coordinate, individualized prior from genome? Likely all three, ablated.
- Computational scaling of end-to-end multi-scale training with trainable molecular FM. What scaling regime?
- Resolution: target end of May 2026 visit to Purdue.

## Strategic significance

This meeting effectively defines the technical track for H1 P1 (Cytoverse). The decisions are operationalized in:

- `11_technical_track_FMs.md` (architecture detail);
- `03_short_term_1to2y.md` (Y1-Y2 deliverables and OKRs);
- `30_funding_strategy.md` (Astera proposal funds the cellular FM track; Google.org Impact funds the connectomic track per the meeting alignment);
- `appendix/C_monday_restructure_spec.md` (FM Family tag added to Strategic Initiatives so cellular vs connectomic vs cross-scale is queryable).
