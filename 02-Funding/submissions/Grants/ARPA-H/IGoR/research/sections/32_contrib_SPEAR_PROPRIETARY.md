## 32. Our contribution: SPEAR perturbation model (UNDER REVIEW)

> [!CAUTION]
> **CONFIDENTIAL, UNDER ANONYMOUS REVIEW. Internal only, do not distribute.** SPEAR is our team's manuscript submitted to NeurIPS 2026 and is under double-blind review. Treat this as a confidential reviewer copy. Keep it out of the `shareable` build, partner materials, and any public submission text. It may be referenced in the proposal only as "a proprietary spectral perturbation model (internal, under review)."

### What it is

**SPEAR (Spectral Adaptive Repositioning)** is our perturbation-response model that grounds gene identity in co-expression geometry rather than arbitrary token positions. It underpins the gene-identity representation used by the TA1 Pillar 2 causal generative model (section 30) and is part of why our TA1 is more than a foundation-model wrapper.

### Two innovations

- **Spectral Co-expression Encoding (SPE):** gene positional information is derived from the **eigenvectors of the co-expression graph Laplacian**, replacing the arbitrary or learned positional encodings used by transformer-style single-cell models. Genes that participate in the same programs sit near each other in the encoding by construction.
- **Adaptive Repositioning (AR):** gene positions are **updated dynamically from the perturbation-conditioned hidden state**, so the representation moves as the cell's state moves under intervention, rather than staying fixed.

### Why it matters here

- **Benchmark standing:** SPEAR reportedly outperforms CPA, GEARS, Geneformer, scGPT, STATE, and CellFlow on perturbation-prediction benchmarks (see manuscript; internal).
- **Fit to the thesis:** SPE plus AR give the causal model a gene-identity prior that is biologically structured and perturbation-aware, which is what the disease-as-perturbation frame (section 10) needs to remain mechanistic rather than correlational.

### Handling rule

Do not name "SPEAR", "Spectral Co-expression Encoding", or "Adaptive Repositioning" in any external document until the paper is public. In submissions, cite it as internal proprietary work and, if needed for grounding claims, describe only the capability ("a co-expression-aware, perturbation-adaptive gene representation"), never the method name or mechanism.


## 32b. Planned SPEAR extensions (detailed; CONFIDENTIAL, under review)

> [!CAUTION]
> Confidential and under anonymous review. Internal only; never name these mechanisms externally.

These extensions specialize the generative core to learn the causal mechanism conditioned on the disease axes (section 31b).

1. **Row-sparse differential-attention residual.** In the differential-transformer attention (from scDFM), impose that the residual map, softmax(Q1 K1^T) minus lambda times softmax(Q2 K2^T), be **row-sparse**, which encodes the **sparsity of the shift mechanism** directly in the attention.
2. **Compositional conditioning across axes.** Use the **Guided Compositional Generation with Multiple Attributes** formulation, which generalizes **classifier-free guidance** from diffusion to **conditional flow matching**, to represent a **combination** of perturbations, disease axes, and archetypes as a single conditioned generation.
3. **Delta-pathway featurization.** Reformulate the differential transformer to operate on **delta pathways** rather than delta genes, giving a **uniform featurization across modalities** (consistent with the pathway-space view of SENA).
4. **Multimodal fusion by barycenter.** Each cellular modality has a **modality-specific encoder**; the **barycenter** of their embeddings (an optimal-transport-style average) is the **multimodal representation** that is fit to the generative system.
5. **Coupling to the three-latent SCM.** The disease-axis conditioners (section 31b) enter as the disease-effect operator of the three-latent SCM (section 30.5), and the deep SCM over axes supplies their causal structure.
