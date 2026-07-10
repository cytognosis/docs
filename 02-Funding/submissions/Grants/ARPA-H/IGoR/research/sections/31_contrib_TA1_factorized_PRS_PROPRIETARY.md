## 31. Our contribution: TA1 Pillar 2b factorized-PRS (PROPRIETARY)

> [!CAUTION]
> **PROPRIETARY, CROWN-JEWEL IP. Internal only.** Do not include this section in partner-facing one-pagers, teaming pages, the `shareable` build, or any non-proprietary part of an ARPA-H submission. Where the method must appear in a submission, mark those pages "Proprietary" (do not use "Confidential"). The full algorithm lives in `IGoR_TA1-TA2_Methods_DeepDive_2026-06-05.md`.

### What it is

Pillar 2b sits inside the TA1 causal generative model (section 30, Pillar 2) and is the platform moat. It **factorizes patient-level genetic variation into a small set of sparse, pathway-disentangled, transdiagnostic axes** that serve simultaneously as (a) the soft-intervention parameters that drive the disease-as-perturbation model (section 10) and (b) interpretable **candidate biotypes** spanning diagnostic boundaries.

### How it differs from prior art

- **Precedent:** the nearest published method is **PRSet / PRSice-2** (Choi et al. 2020), which computes pathway-restricted polygenic scores. PRSet partitions a polygenic score by annotated pathway; it does not learn a disentangled, per-person factorization tied to a latent causal model.
- **Our advance:** we learn **per-person genome axes** as sparse mechanism identifications, expressed over transcription-factor-region and pathway structure (for example CREB and SREBP regulatory programs), and bind them to the SAMS-VAE-style latent intervention so the axes are causal coordinates rather than additive risk sums.
- **Why it is defensible:** the novelty claim is made **precisely against PRSet** (a disentangled, causal, per-person factorization versus a pathway-restricted additive score), which is the specific, citable differentiation reviewers can check.

### Why it is the moat

- The axes are **transdiagnostic**: the same coordinate system orders patients across schizophrenia, bipolar, and 22q11DS, which is what turns a single-disease model into a platform.
- They are **biotypes with mechanism attached**: each axis points at the pathways and cell types TA2 should perturb next, closing the loop with the highest value of information.
- They are **reusable IP**: independent of any one disease pilot, so they survive the nonprofit-to-PBC commercial pathway.

### Handling rule

Public and partner-facing descriptions use only this sentence: "we additionally factorize patient-level genetic variation into sparse, pathway-disentangled, transdiagnostic axes that double as candidate biotypes; the detailed factorization method is proprietary." Nothing more.


## 31b. Genomic-to-disease-axis front-end (detailed architecture; PROPRIETARY)

> [!CAUTION]
> Crown-jewel IP. Internal only. This is the elaborated method behind the disease axes; public-facing text uses only the high-level summary in section 30.

This front-end turns a genome (or GWAS summary statistics) into a small set of interpretable, sparse **disease-axis factors** that condition the generative core.

1. **Sequence to gene embeddings (pretrained genomic foundation models).** Initialize from pretrained genomic foundation models (**AlphaGenome, VariantFormer, Evo 2**) to map base-pair sequence to embeddings, focusing on **gene bodies and regulatory regions**, with **cross-attention** contextualizing the gene-body embeddings (VariantFormer style). We may add a gene-expression-prediction head as an auxiliary objective, but the primary path takes the **contextualized gene-sequence embeddings** directly. A potential collaboration with **Francesco Paolo Casale** (a senior VariantFormer author, ex-insitro) covers this sequence-to-embedding map, either within IGoR or independently.
2. **Project onto a gene functional network.** A projection head (output dimension D) places the contextualized gene embeddings as **initial node embeddings** on a gene functional network.
3. **Multiresolution graph diffusion.** Expand context from a gene's regulatory neighborhood to **cross-gene relationships** with a **multiresolution graph-diffusion** operator (graph-wavelet style, in the spirit of WaveGC). If typed and signed, weighted edges are needed, use a relation-aware propagation such as **NBFNet** (Neural Bellman-Ford networks).
4. **Archetypal factorization into disease axes.** Learn **k archetypes**: each is a **convex weight vector over nodes** (nonnegative, summing to one) that, multiplied by the final node embeddings, yields an **archetypal representation** of dimension D; remaining nodes are representable as convex combinations of the archetypes (this latter constraint may later be relaxed). The simplex constraint makes the archetype weight vectors **sparse**; we may additionally impose **graph-total-variation** regularization for graph-aware sparsity. **Alternative:** learn the factors with **sparse autoencoders** (the more common recent approach). The result is **k disease-axis factors of dimension D**, each acting as a disease axis or intervention that conditions the generative model.
5. **Deep structural causal model over the axes.** The genomic factors additionally serve as **exogenous variables of a deep structural causal model** (discrepancy-VAE and Zhang-style), so the model **simultaneously learns the causal interactions among the disease axes** (a directed structure over axes), rather than treating them as independent.
