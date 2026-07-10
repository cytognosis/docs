---
slot_id: U03
proposal: astera_2026
funder: astera_residency
submission_date: 2026-04-19
status: submitted
source_doc: input/applications/Astera/Astera_submited_application_responses.md
---

# U03 — Novelty & approach (Astera 2026 overlay)

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: grant team
> **Tags**: `funding`, `proposal`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

## U03.1 — Core insight / thesis of novelty

Current genome-regulatory foundation models (AlphaGenome, variantFormer) treat tissue and cell type as either independent output channels or as free-parameter learnable embeddings. Neither approach exploits the **known hierarchical similarity structure** across cellular contexts (Cell Ontology, UBERON, Gene Ontology), and neither generalizes to unseen contexts. We replace one-hot or learnable embeddings with **TransBox-pretrained semantic embeddings** of GO-Plus ontology terms, projected into the model as attention-layer conditioning. Because conditioning preserves cross-context similarity, the model interpolates to unseen cellular contexts via their ontology-manifold neighbors.

## U03.2 — Technical approach

**Phase 1 (Months 1-4) — PFC cell-type-specific ATAC + RNA prediction.** Embed GO-Plus ontologies (UBERON tissues + Cell Ontology cell types + GO functions) using TransBox to pretrain semantic embeddings respecting ontology logical structure. A learnable linear layer projects pretrained ontological terms into the model, replacing one-hot embeddings. Inject these as variantFormer-style attention conditioning at each layer. Iterative hierarchical fine-tuning: GTEx PFC tracks first → 7 PEC major brain cell types (2,716 snRNA + 413 snATAC pseudobulks) → 24 BICCN cell-type annotations (9,312 snRNA pseudobulks). Use frozen AlphaGenome to embed cell-type-specific CREs and gene promoters, with windows [TSS-900kb, TSS+100kb] and [TSS-100kb, TSS+900kb]; ablate against FUMA (10kb upstream / 1.5kb downstream), 5kb/1.5kb, and wide (35kb/10kb) windows. Apply hyperbolic contrastive loss (H-InfoNCE) over CRE and promoter embeddings to predict cell-type-specific signed TF-promoter edge weights.

**Phase 2 (Months 5-8) — Cell-type-specific disease-associated dysregulation.** Patient track scaling: divide each patient track by the mean and standard deviation of matched controls per study, producing differential targets. Train a transcriptional-variant head on differential RNA-seq tracks, regularized by functional gene networks for biological disentanglement of dysregulation patterns. Single-cell extension: pair each patient cell with control cells from the same study in proportion to their entropic optimal-transport plan; pushforward of control cells gives residual transcriptional profiles; train conditional flow-matching model conditioned on paired control expression and individual genetic variation to predict cell-resolved transcriptional dysregulations.

**Phase 3 (Months 9-12) — Disentangled phenotypic axes from genotypic variation.** Use NIH NeuroBioBank (NBB, 10,000+ individuals across HBTRC at McLean and 5 partner biobanks; collaborator Brad Ruzicka). Predict cell-type-specific differential signatures from WGS for each individual. Map DSM diagnoses to Neurobehavior Ontology (NBO) terms — RDoC-style units of analysis, refining categorical labels into phenotypic components. Embed NBO terms preserving ontology structure (matching Phase-1 cell-type ontology treatment) and use as regularization. Joint subspace alignment of phenotypic + genotypic modalities via principal-direction alignment. Five-objective optimization: (1) cross-modal subspace alignment, (2) biological disentanglement of genotypic axes via graph-diffusion-wavelet on functional gene networks, (3) phenotypic disentanglement via NBO ontology-structure regularization, (4) genotypic reconstruction loss, (5) phenotypic reconstruction loss. Validation: Frechet-mean per-diagnosis embedding pairwise similarities benchmarked against Grotzinger 2026 cross-disorder five-factor genomic architecture across 14 psychiatric conditions.

## U03.3 — Why it will work now

The enabling conditions specifically converge for this proposal: (a) AlphaGenome and variantFormer just published, providing the embedding scaffold; (b) PsychENCODE Phase 2 and PsychAD just released the snRNA + snATAC pseudobulks at the cell-type resolutions we need; (c) GO-Plus ontology in EL++ form just stabilized as the unified UBERON/CL/GO logical reasoner; (d) TransBox (2025) made it tractable to pretrain ontology-aware semantic embeddings respecting logical structure; (e) Grotzinger 2026 just provided the 14-disorder cross-cohort five-factor genomic benchmark we validate against. None of these existed in their current form even 18 months ago.

## U03.4 — Evidence of feasibility

Cytognosis founder Shahin Mohammadi co-led the Science 2024 publication identifying continuous "disease axes" in schizophrenia at the single-cell level; co-led the Nature 2019 paper revealing pre-symptomatic cell-type vulnerability in Alzheimer's. The hyperbolic contrastive loss (H-InfoNCE) was developed within the same lab tradition. PsychENCODE / PsychAD Phase 2 datasets are accessible via existing consortium agreements. NeuroBioBank access via Brad Ruzicka (HBTRC McLean), already-collaborator. GTEx, BICCN, GO-Plus, and AlphaGenome are public.
