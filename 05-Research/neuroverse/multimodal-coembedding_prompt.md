# Multimodal co-embedding (agent brief)

> **Variants**: Agent seed (this doc) - Technical (see docs repo 05-Research/neuroverse/) - Readable (multimodal-coembedding.md in Obsidian vault)

> **Status:** Active · **Date:** 2026-07-01 · **Variant:** agent (self-contained). **Technical sources:** [methods review](multimodal-coembedding-methods-review.md) + [addendum](multimodal-coembedding-addendum.md).

## Goal
Choose and stage an architecture that embeds paired multi-modal patient data (phenotype, genotype, single-cell omics, connectome, imaging) into one shared geometry where the same patient aligns across modalities.

## Scope
In: method taxonomy (generative-joint, contrastive, OT, matrix factorization), a ranked recommendation, a decision tree, an implementation roadmap, and four deep-dive updates (FGW necessity, cross-attention, MoE, causal representation). Out: the phenotype axis definition (see feature-space doc), data access and governance.

## Decided / done
- Problem formalized as N paired-patient embeddings with patient-level pairing known.
- Recommended baseline: **MOFA+** (fast, interpretable). Recommended target: **PoE-VAE + cross-modal contrastive + archetypal head**.
- Addendum Q1 resolved: with paired patients, prefer **CKA** over FGW for geometry comparison and as a loss; FGW's correspondence machinery is unnecessary.
- Missing modalities: PoE masking. Interpretable anchors: archetypal analysis.

## Open questions
- How far to pursue causal (SCM) multimodal representation (Q4); data-hungry.
- Exact contrastive-loss and masking design for cross-attention (Q2) to prevent modality-identity leakage.
- Integration point with the archetypal-analysis pipeline already run in [pipeline-report-v0](pipeline-report-v0.md).

## Pending tasks (prioritized)
1. Stand up the MOFA+ baseline on an available paired subset.
2. Prototype the PoE-VAE + contrastive backbone; add CKA as a diagnostic and loss term.
3. Attach an archetypal projection head; compare archetypes to the k=13 set in pipeline-report-v0.

## Source-of-truth files
- Technical: `05-Research/neuroverse/multimodal-coembedding-methods-review.md` and `...-addendum.md`
- Related pipeline run: `05-Research/neuroverse/pipeline-report-v0.md`
- Phenotype axes: `05-Research/neuroverse/neurobehavioral-phenotype-feature-space.md`

## Success criteria
Same-patient embeddings align across modalities (high CKA/Procrustes); missing-modality patients embed sensibly; archetypes are biologically interpretable and stable under bootstrap.

## Start commands
Read the methods review section 7 (recommended architecture) and section 8 (decision tree), then the addendum's final "how these change the architecture" section. Baseline tooling per `neuroimaging-python-stack-defaults.md` (PyTorch, scvi-tools, PyG).
