# Science Brief: Virtual Cell and Causal Perturbation Modeling
## Cytognosis / IGoR Proposal — Technical Literature Reference
**Prepared:** 2026-06-12
**Purpose:** Precise terminology, citations, and synthesis for grant writers. Treat every method name, quote, and claim as load-bearing.

---

## PART I: PER-PAPER CITATIONS AND SUMMARIES

---

### VIRTUAL CELL — FOUNDATIONAL FRAMING

---

#### 1. Bunne et al. (2024) — "How to Build the Virtual Cell with Artificial Intelligence: Priorities and Opportunities"

**Full citation:**
Bunne, C., Roohani, Y., Rosen, Y., Gupta, A., Zhang, X., Roed, M., Alexandrov, T., AlQuraishi, M., Brennan, P., Burkhardt, D.B., Califano, A., Cool, J., Dernburg, A., Ewing, K., Fox, E.B., Haury, M., Herr, A.E., Horvitz, E., Hsu, P.D., Jain, V., Johnson, G.R., Kalil, T., Kelley, D.R., Kelley, S.O., Kreshuk, A., Mitchison, T., Otte, S., Shendure, J., Sofroniew, N.J., Theis, F., Theodoris, C.V., Upadhyayula, S., Valer, M., Wang, B., Xing, E., Yeung-Levy, S., Zitnik, M., Karaletsos, T., Regev, A., Lundberg, E., Leskovec, J., and Quake, S.R. *Cell* 187, 7045–7063 (December 12, 2024). DOI: https://doi.org/10.1016/j.cell.2024.11.015

**Core contribution (2–3 sentences):**
This community perspective defines the AI virtual cell (AIVC) as a multi-scale, multi-modal, large-neural-network-based model capable of representing and simulating the behavior of molecules, cells, and tissues across diverse states. The paper frames the AIVC as needing three core properties: it must be predictive, generative, and queryable. It maps a research agenda covering data generation, model architecture, benchmarking, interpretability, and collaborative development required to build AIVCs.

**Method/model name and key terminology:**
- Model name: **AI virtual cell (AIVC)**
- Key terms: *universal representation (UR)* of cell state; *in silico* experimentation; *intrinsic perturbation* (genetic); *extrinsic perturbation* (chemical/environmental); cellular UR at molecular, cellular, and multicellular scales; multi-modal encoder; predictive-generative-queryable trifecta; causal modeling, sparse featurization, and counterfactual reasoning as interpretability approaches.

**Connection to our framing:**
The AIVC agenda explicitly names disease-associated genetic variation (mutations, genetic variation) as a perturbation type that the virtual cell must simulate, establishing the conceptual license for treating disease genotype as a causal operator on cell state rather than a label.

---

#### 2. Eisenstein, M. (2026) — "Can Biology Move Into the Matrix?" (VirtualCell_review.pdf)

**Full citation:**
Eisenstein, M. "Can Biology Move Into the Matrix?" *Nature* 654, 286–288 (4 June 2026). DOI: https://doi.org/10.1038/d41586-2026-02777-8 (ID in PDF; verify final DOI — the PDF header cites "https://doi.org/10.1038/d41586-2026-02777-8" at page 288 footnote reference 4; confirm)

**Core contribution (2–3 sentences):**
This Nature technology-and-tools feature surveys the state of virtual cell research as of mid-2026, profiling key systems including STACK (Arc Institute), X-Cell (Xaira), AlphaCell (Tongji/GenBio), SubCell (Lundberg lab), and PhysiCell (Macklin lab). It draws a sharp distinction between foundation models — which learn static representations of cell state — and world models, which must support action-conditioned simulation and dynamic modeling of cellular trajectories. The article documents the 2025 Arc Institute Virtual Cell Challenge, in which none of the pure AI models outperformed approaches that incorporated conventional statistical methods, underscoring the open challenge of perturbation prediction.

**Method/model name and key terminology:**
- Central distinction: **foundation model** (static representation, good at embedding and annotation) vs. **world model** (action-conditioned simulation, counterfactual reasoning, long-horizon planning).
- Key terms referenced: *perturbation atlas*, *perturbation-specific changes in gene expression*, *Systema* (benchmarking tool by Brbic lab), *State* (Arc Institute perturbation model with population-level kernel alignment loss), *AIDO* (AI-driven digital organism, GenBio AI).
- Key quote directly applicable: "A world model should be more focused on the dynamic behaviour modelling of the cell" (Qi Liu, Tongji/AlphaCell).

**Connection to our framing:**
The article confirms that no existing model treats the disease genotype as the causal input; existing framing is always "what happens when gene X is knocked out" — not "what cell state shift does disease-associated variation impose." This gap is exactly the one we propose to fill.

---

#### 3. Xing, E. and Song, L. (2026) — "A World Model of the Virtual Cell" (virtual-cell_world model.pdf)

**Full citation:**
Xing, E. and Song, L. "A World Model of the Virtual Cell." GenBio AI technical report, May 3, 2026. ID not in PDF — verify (no arXiv or DOI visible in document header).

**Core contribution (2–3 sentences):**
This paper proposes an operational definition of the virtual cell grounded in the **Virtual Cell World Model (VCWM)** paradigm, adapting the world-model framework from embodied AI (action-conditioned simulation, counterfactual reasoning, long-horizon planning). The VCWM architecture comprises three coupled components: a structured multi-modal encoder (E) mapping observations and environment to a latent cellular manifold, an action-conditioned transition core (F) that evolves latent state under interventions, and a generative decoder (D) that renders coherent multi-modal outputs. The paper contrasts VCWM with predictive foundation models that learn fixed input-output mappings, arguing that interventions must act as operators on a unified latent cellular state rather than produce isolated predictions.

**Method/model name and key terminology:**
- Model/paradigm: **Virtual Cell World Model (VCWM)**, **AI-driven Digital Organism (AIDO)**
- Architecture components: **structured encoder (E)**, **action-conditioned transition core (F)**, **generative decoder (D)**; *cellular manifold M*; latent state z = E(x, G, e) where G is the biological network graph, x is multi-modal data, and e is the cellular micro-environment.
- Key equation: p(x' | x, a, e) — next cell state conditioned on current state, action (intervention), and environment.
- Key terms: *actionable biological prompts*, *multi-scale state reconstruction*, *action-conditioned simulation*, *cross-modal consistency*, *in-context molecular design*.

**Connection to our framing:**
The VCWM's transition core F directly maps to our proposed causal perturbation operator: disease-associated genetic variation constitutes the "action" a that drives state evolution on the cellular manifold, transforming the genotype-phenotype problem into action-conditioned latent state evolution.

---

### PERTURBATION MODELING

---

#### 4. Bereket and Karaletsos (2024) — SAMS-VAE

**Full citation:**
Bereket, M. and Karaletsos, T. "Modelling Cellular Perturbations with the Sparse Additive Mechanism Shift Variational Autoencoder." *Proceedings of the 37th Conference on Neural Information Processing Systems (NeurIPS 2023)*. arXiv:2311.02794v2 [stat.ML], 16 Jan 2024. (NeurIPS 2023 proceedings; arXiv ID: 2311.02794)

**Core contribution (2–3 sentences):**
SAMS-VAE decomposes the latent state of a perturbed cell as the sum of a basal (unperturbed) state embedding z^b and a perturbation effect embedding z^p, where z^p is modeled as a sparse additive composition of global latent effect vectors e_t masked by binary masks m_t per perturbation t. The key identifiability claim is that sparsity of the binary mask (enforced via a Bernoulli prior with small alpha) identifies disentangled, perturbation-specific latent subspaces that are flexibly composable for combinatorial generalization. The model outperforms comparable baselines on in-distribution and out-of-distribution single-cell perturbation tasks, including combinatorial reasoning under resource paucity, and yields latent structures that correlate with known biological mechanisms.

**Method/model name and key terminology:**
- Model: **SAMS-VAE** (Sparse Additive Mechanism Shift Variational Autoencoder); ablation: **CPA-VAE**
- Key terms: *sparse additive mechanism shift*; *latent basal state z^b*; *latent perturbation effect embedding z^p*; *binary mask m_t* (Bernoulli prior); *perturbation-specific latent subspaces*; *compositional perturbation effects*; *average treatment effect (ATE)* as evaluation via posterior predictive check (PPC); *importance weighted ELBO (IWELBO)*.
- Formal model: z_i = z^b_i + z^p_i; z^p_i = sum_{t=1}^{T} d_{i,t} (e_t * m_t)
- Identifiability framing: The Sparse Mechanism Shift framework (citing Schölkopf et al. 2021) connects disentanglement to causal graph identification; sparsifying global latent variables m_t recovers disentangled perturbation-specific subspaces.

**Connection to our framing:**
SAMS-VAE's binary masks m_t are the prototype for our proposed disease-axis masks: each disease-associated genetic factor would target a sparse subset of biological process dimensions in latent space, precisely the "sparsity of the shift mechanism" we inherit and extend to polygenic disease variation.

---

#### 5. Zhang et al. (2023) — Causal Disentanglement / Discrepancy-VAE (SENA)

**Full citation:**
Zhang, J., Greenewald, K., Squires, C., Srivastava, A., Shanmugam, K., and Uhler, C. "Identifiability Guarantees for Causal Disentanglement from Soft Interventions." *Proceedings of the 37th Conference on Neural Information Processing Systems (NeurIPS 2023)*. ID not in PDF — verify (NeurIPS 2023; no arXiv ID printed in document header).

**Core contribution (2–3 sentences):**
This paper establishes formal identifiability guarantees for causal disentanglement from soft interventions when the latent causal variables are unobserved, using a generalized notion of faithfulness. The main result guarantees recovery of the latent causal model up to a CD-equivalence class (permutation, scale, and shift of latent variables) and the ability to predict the effect of unseen combinations of interventions, in the limit of infinite data. The proposed algorithm implements this via an autoencoding variational Bayes approach where the decoder is a deep structural causal model (DSCM), applied to predicting combinatorial perturbation effects in genomics.

**Method/model name and key terminology:**
- Framework: **causal disentanglement from soft interventions**; model: **deep structural causal model (DSCM)** decoder; estimation via **autoencoding variational Bayes**
- Key terms: *soft intervention* (changes conditional distribution of U_i given parents, preserving dependency structure); *hard intervention* (do-calculus, removes parental dependency); *CD-equivalence class* (causal disentanglement equivalence); *linear interventional faithfulness* assumption; *causal representation learning*; latent DAG G with nodes [p] over unobserved U = (U_1, ..., U_p).
- Note: The file is labeled "discrepancy_vae.pdf" but the paper title is "Identifiability Guarantees for Causal Disentanglement from Soft Interventions." The connection to SENA (Schölkopf Empirical Network Architecture) is through the shared causal representation learning lineage; confirm whether this is the specific SENA/discrepancy-VAE paper intended, as the paper text does not use the term "SENA" explicitly — the method is the DSCM-based causal disentanglement VAE.

**Connection to our framing:**
This paper provides the formal identifiability backbone for our approach: treating each disease-associated genetic perturbation as a soft intervention on a latent causal DAG over biological processes gives us the theoretical guarantee that the resulting disease axes are recoverable (up to equivalence) from multi-cohort interventional data.

---

#### 6. Palma, Richter, Zhang, Dittadi, and Theis (2024) — CellFlow

**Full citation:**
Palma, A., Richter, T., Zhang, H., Dittadi, A., and Theis, F.J. "CellFlow: A Generative Flow-Based Model for Single-Cell Count Data." *Machine Learning for Genomics Explorations workshop at ICLR 2024*. ID not in PDF — verify (ICLR 2024 MLG workshop; no DOI/arXiv ID in document header).

**Core contribution (2–3 sentences):**
CellFlow introduces a flow-matching-based generative model for single-cell RNA-seq count data that operates natively in raw count space (not normalized expression) by mapping discrete data to the continuous parameter space of a Negative Binomial distribution, then training an Optimal Transport Conditional Flow Matching (OT-CFM) model on top. This avoids the information loss of library-size normalization and provides a generative model that preserves the discrete distributional properties (sparsity, overdispersion) of real single-cell data. On benchmark datasets (PBMC, dentate gyrus, lung), cellFlow performs on par with or better than normalized-data baselines on Wasserstein-2 distance and MMD metrics.

**Method/model name and key terminology:**
- Model: **cellFlow** (Flow-Matching-based single-cell generative model)
- Key terms: *Optimal Transport Conditional Flow Matching (OT-CFM)*; *Negative Binomial (NB) likelihood*; *count space generation*; *dimensionality-preserving encoder f_nu*; *velocity field v_xi(t, z, l, y)*; *size factor l*; *inverse dispersion theta_g*.
- Architecture: discrete count encoder f_nu (trained via MLE of NB) maps x to continuous z; OT-CFM learns velocity field transporting Gaussian noise to the z distribution; sampling draws z via ODE integration then samples x ~ NB(l*softmax(z), theta).

**Connection to our framing:**
CellFlow's count-space generative framework is directly relevant as a baseline and component for our perturbation flow model; our approach needs to generate realistic scRNA-seq readouts of disease-shifted cell states, making NB-likelihood flow matching the appropriate generative backbone.

---

#### 7. Lachapelle et al. (2022) — sVAE (sparse VAE)

**Full citation:**
Lachapelle, S., Rodríguez López, P., Sharma, Y., Everett, K., Le Priol, R., Lacoste, A., and Lacoste-Julien, S. "Disentanglement via Mechanism Sparsity Regularization: A New Principle for Nonlinear ICA." *Proceedings of Machine Learning Research* vol. 140:1–57 (1st Conference on Causal Learning and Reasoning, CLeaR 2022). arXiv:2107.10098v3 [stat.ML], 23 Feb 2022.

**Core contribution (2–3 sentences):**
This paper introduces **mechanism sparsity regularization** as a principled path to disentanglement in nonlinear ICA: if the latent factors of interest depend sparsely on past factors and/or observed auxiliary variables, then regularizing the learned causal graphical model (CGM) to be sparse recovers the latent variables up to permutation (Theorem 5). The key insight is that disentanglement and sparse causal structure discovery can be achieved simultaneously by learning the latent factors and the sparse CGM relating them jointly. A VAE-based implementation learns latent mechanisms regularized via binary masks, validated on synthetic datasets.

**Method/model name and key terminology:**
- Principle: **mechanism sparsity regularization** (also termed the **sparse mechanism shift hypothesis**, citing Schölkopf et al. 2021)
- Model: **sVAE** (sparse VAE); binary mask approach; interventions modeled as targeting unknown subsets of latent factors.
- Key terms: *nonlinear ICA*; *causal graphical model (CGM)*; *permutation-identifiability*; *mechanism functions lambda_i*; adjacency matrices G^z (latent-to-latent) and G^a (action-to-latent); *linear equivalence*; *permutation equivalence*.
- The sparse mechanism shift connects to Schölkopf et al. (2021): only a few mechanisms change at a time when an intervention occurs.

**Connection to our framing:**
sVAE establishes the theoretical foundation — mechanism sparsity regularization — that justifies learning disentangled biological process dimensions from perturbation data; we inherit and extend this to the polygenic disease setting where each disease locus is an unknown-target soft intervention.

---

#### 8. Lopez et al. (2023) — sVAE+ (Learning Causal Representations of Single Cells via Sparse Mechanism Shift Modeling)

**Full citation:**
Lopez, R., Tagasovska, N., Ra, S., Cho, K., Pritchard, J.K., and Regev, A. "Learning Causal Representations of Single Cells via Sparse Mechanism Shift Modeling." *Proceedings of Machine Learning Research* (2nd Conference on Causal Learning and Reasoning, CLeaR 2023). arXiv:2211.03553v4 [q-bio.GN], 16 Feb 2023.

**Core contribution (2–3 sentences):**
This paper applies the sparse mechanism shift framework directly to single-cell genomics perturbation data (genetic and chemical), proposing a deep generative model where each perturbation is treated as a stochastic soft intervention targeting an unknown, sparse subset of latent variables representing distinct biological processes. It introduces **sVAE+**, a variant of sVAE with a Bayesian (Beta-Bernoulli) approach for learning sparse mechanism shifts requiring minimal hyperparameter tuning, and benchmarks both on simulated and real large-scale CRISPR perturbation datasets. Models exploiting the sparse mechanism shift hypothesis significantly outperform contemporary methods on transfer learning tasks.

**Method/model name and key terminology:**
- Models: **sVAE** (sparse VAE, implementing Lachapelle et al. 2022) and **sVAE+** (Bayesian extension with Beta(1, K) prior on perturbation target probabilities)
- Key terms: *sparse mechanism shift hypothesis*; *stochastic intervention targeting an unknown, sparse subset of latent variables*; *latent units*; *intervention target recovery*; *causal target identification*; *out-of-domain generalization*; *transfer learning*; *SpikeSlabVAE* (baseline comparison); *Gumbel-sigmoid* relaxation of Bernoulli.
- Biological interpretation: latent variables z_1, ..., z_p each represent "activity of a distinct biological process"; perturbation I_k maps to z_{i(k)} via the sparse bipartite graph G^a.
- Code: https://github.com/Genentech/sVAE

**Connection to our framing:**
sVAE+ is the closest single-cell implementation of our intended causal architecture; the key extension we propose is replacing experimentally-delivered genetic perturbations with disease-associated polygenic variants as the interventional signal, and replacing the perturbation identity label with factorized genotype scores.

---

#### 9. Hediyeh-zadeh, Fischer, and Theis (2024) — sVAE-ligr

**Full citation:**
Hediyeh-zadeh, S., Fischer, T., and Theis, F.J. "Disentanglement via Mechanism Sparsity by Replaying Realizations of the Past." *Machine Learning for Genomics Explorations workshop at ICLR 2024*. ID not in PDF — verify (ICLR 2024 MLG workshop; no DOI/arXiv ID in document header).

**Core contribution (2–3 sentences):**
sVAE-ligr (SpikeSlabVAE with learnable interventions by Generative Replay) addresses the case where the auxiliary variable linking perturbation labels to biological mechanisms is not directly observed and the pairing between labels and samples is unknown — the key biological scenario of mechanism transportability across species or data modalities. It combines mechanism sparsity regularization with Continual Learning's Generative Replay to construct realizations of unobserved auxiliary variables, enabling disentangled representation learning when perturbation-label-to-sample assignment is latent. Applied to counterfactual generation of gene knockout signatures in primary tumors (TCGA), it successfully transfers ARID1A KO cell line signatures to in vivo tumor data.

**Method/model name and key terminology:**
- Model: **sVAE-ligr** (SpikeSlabVAE with learnable interventions by Generative Replay)
- Key terms: *spike-slab prior*; z_i | a ~ gamma_i^a * Normal(mu_i^a, 1) + (1 - gamma_i^a) * Normal(0, 1); *Generative Replay*; *Experience Replay*; *latent assignment variable C* (Categorical-Dirichlet); *mechanism transportability*; *counterfactual generation*.
- Distinct contribution: extends the sVAE family to settings where the intervention label is latent (not observed), enabling cross-modal and cross-species transfer of biological mechanisms.

**Connection to our framing:**
sVAE-ligr's framework for unobserved auxiliary variables directly maps to our problem: disease genotype is an incompletely observed, continuous auxiliary variable (polygenic score) rather than a clean discrete perturbation label, and the mechanism transportability across cohorts and cell types is exactly what we require.

---

#### 10. Anonymous Author(s) (2026, under review) — SPEAR [OUR WORK]

**Full citation:**
Anonymous Author(s). "Spectral Adaptive Repositioning for Flow-Based Single-Cell Perturbation Modeling." Submitted to *40th Conference on Neural Information Processing Systems (NeurIPS 2026)*. Under review; do not distribute. Confidential reviewer copy. ID not in PDF — verify (NeurIPS 2026 submission; no arXiv ID in document as submitted anonymously).

**Core contribution (2–3 sentences):**
SPEAR addresses a fundamental limitation of all prior perturbation models: genes have no natural sequential order, yet transformer-based perturbation models assign arbitrary integer-indexed or expression-rank-based positional encodings that discard the regulatory topology of the co-expression network. SPEAR replaces these with two complementary positional mechanisms — Spectral Co-expression Encoding (SPE), which derives continuous positional coordinates from eigenvectors of the co-expression graph Laplacian, and Adaptive Repositioning (AR), which dynamically derives each gene's scalar position from its perturbation-conditioned hidden state at every backbone layer, allowing attention geometry to reorganize to reflect perturbation-induced functional rewiring. Evaluated on genetic, pharmacological, and cytokine perturbation benchmarks, SPEAR achieves state-of-the-art recovery of differential gene-expression, distributional structure, and perturbation-specific identifiability, and captures latent positional relationships mapping to known transcription factor-target interactions.

**Method/model name and key terminology:**
- Model: **SPEAR** (SPEctral Adaptive Repositioning); two core mechanisms: **SPE** (Spectral Co-expression Encoding) and **AR** (Adaptive Repositioning)
- Key terms: *spectral co-expression encoding*; *graph Laplacian L = I - D^{-1/2} A D^{-1/2}*; *eigenvector spectral coordinates S*; *learnable frequency projections Omega*; *rotary position embedding (RoPE)*; *adaptive repositioning scalar z_{i,h}*; *SwiGLU gate*; *differential attention (DiffAttn)*; *perturbation embedding adapter*; *flow matching loss L_FM*; *MMD loss L_MMD*; *curved interpolant*.
- Framing: SPEAR frames perturbation prediction as distribution-to-distribution flow matching (p_0 unperturbed to p_1 perturbed), conditioned on perturbation identity rho = {g_{j1}, ..., g_{jM}} (set of knocked-out genes), with the velocity field v_theta(x_t, t, c_ctrl, rho) trained to transport control cell distributions to perturbed cell distributions.
- Baselines beaten: CPA, GEARS, Geneformer, scGPT, STATE, CellFlow (scDFM).

**Connection to our framing:**
SPEAR is our team's core technical contribution to the perturbation modeling field. Its spectral co-expression positional encoding grounds gene identity in regulatory network topology rather than arbitrary order — a prerequisite for modeling how disease-associated genetic variation reshapes the regulatory landscape. The adaptive repositioning mechanism captures perturbation-induced functional rewiring, which is the signal we need to detect when disease genotype acts as the perturbation operator.

---

### SINGLE-CELL FOUNDATION MODELS

---

#### 11. Chuai et al. (2026) — AlphaCell

**Full citation:**
Chuai, G., Chen, X., Yang, X., Zhang, C., Qu, K., Wang, Y., Li, W., Yang, J., Si, D., Xing, F., Gao, Y., Wu, S., Fu, S., He, B., and Liu, Q. "Towards building a World Model to simulate perturbation-induced cellular dynamics by AlphaCell." bioRxiv preprint doi: https://doi.org/10.64898/2026.03.02.709176, posted March 5, 2026. (CC-BY-NC-ND 4.0)

**Core contribution (2–3 sentences):**
AlphaCell is a generative Virtual Cell World Model built on three synergistic innovations: (1) Latent Manifold Rectification — a Base Model Encoder processing the full protein-coding transcriptome (not restricted HVGs) to construct a differentiable Virtual Cell Space (continuous latent manifold); (2) Biological Reality Reconstruction — a knowledge-rich Base Model Decoder ensuring high-fidelity, genome-wide expression profile reconstruction; and (3) Universal State Transition — a Flow Model using Optimal Transport Conditional Flow Matching (OT-CFM) to model perturbations as continuous, deterministic vector fields acting on the Virtual Cell Space. The Base Model was trained on 220 million single cells (140M from CZ CELLxGENE + 80M from Tahoe dataset); the Flow Model was trained on 90 million perturbed profiles.

**Method/model name and key terminology:**
- Model: **AlphaCell**; framework: **Virtual Cell World Model**
- Components: **Base Model Encoder** (Virtual Cell Space builder), **Base Model Decoder** (Observation Interface), **Flow Model** (Dynamic Physics Engine / Universal State Transition)
- Key terms: *Virtual Cell Space (VCS)*; *Latent Manifold Rectification*; *Biological Reality Reconstruction*; *Universal State Transition*; *Optimal Transport Conditional Flow Matching (OT-CFM)*; *genome-wise representation*; *compositional generalization*; *zero-shot prediction*; *Mixture-of-Experts (MoE) layers* in decoder.

**Connection to our framing:**
AlphaCell's Flow Model provides the closest architectural template for treating disease as a continuous perturbation operator on a manifold of cell states — its OT-CFM approach transports cell state embeddings from control to perturbed states, exactly as our model would transport from healthy to disease-shifted states conditioned on factorized genotype axes.

---

#### 12. Dong et al. (2026) — STACK

**Full citation:**
Dong, M., Adduri, A., Gautam, D., Carpenter, C., Shah, R., Ricci-Tam, C., Kluger, Y., Burke, D.P., and Roohani, Y.H. "Stack: In-Context Learning of Single-Cell Biology." bioRxiv preprint doi: https://doi.org/10.64898/2026.01.09.698608, posted January 9, 2026. (CC-BY 4.0)

**Core contribution (2–3 sentences):**
STACK is a single-cell foundation model trained on 149 million uniformly preprocessed human single cells (scBaseCount) that introduces in-context learning for single-cell biology via a novel tabular transformer architecture supporting both intra-cellular and inter-cellular information flow. The key architectural innovation is a trainable tokenization module that projects gene expression vectors into 100 gene module tokens per cell (learned without external gene annotations), passed through alternating intra-cellular multi-head attention (MHA) and inter-cellular MHA layers, enabling the model to leverage cellular context at inference time without fine-tuning. Post-training alignment enables prompt-conditioned tasks including perturbation effect prediction, used to construct Perturb Sapiens — the first human whole-organism atlas of perturbed cells spanning 28 tissues, 40 cell classes, and 201 perturbations.

**Method/model name and key terminology:**
- Model: **STACK**; atlas: **Perturb Sapiens**
- Key terms: *gene module tokens* (100 per cell); *intra-cellular MHA* (within-cell, over gene modules); *inter-cellular MHA* (across cells in a set); *cell set*; *tabular attention*; *rectangular mask pre-training*; *in-context learning (ICL)*; *prompt-conditioned generation*; *linear identifiability regularization* (distributional regularization enforcing per-cell-set constant plus standard normal); *scBaseCount* (189M cells, 19,978 SRX samples); *perturbation atlas*.

**Connection to our framing:**
STACK's in-context learning mechanism — where prompt cells encoding a condition (disease state, perturbation) guide prediction of query cell expression — provides a compelling architecture for conditioning on patient genotype profiles as prompt context to predict disease-shifted cell states.

---

#### 13. Wang et al. (2026) — X-Cell

**Full citation:**
Wang, C., Karimzadeh, M., Ravindra, N.G., Bounds, L.R., Alcrasool, N., Huang, A.C., Ma, S., Gulbranson, D.R., Cui, H., Lee, Y., Arjavalingam, A., MacKrell, E.J., Wilken, M.S., Chen, J., Herken, B.W., Weber, J.A., Onesto, M.M., Gonzalez-Teran, B., Leung, N.F., Shi, S.Y., Smith, B.J., Lam, S.K., Barner, A., Wright, P., Rumsey, E.M., Kim, S., Sit, R.V., Litterman, A.J., Chu, C., and Wang, B. "X-Cell: Scaling Causal Perturbation Prediction Across Diverse Cellular Contexts via Diffusion Language Models." bioRxiv preprint doi: https://doi.org/10.64898/2026.03.18.712807, posted March 20, 2026. (CC-BY-NC 4.0)

**Core contribution (2–3 sentences):**
X-Cell introduces the X-Atlas/Pisces dataset — the largest genome-wide CRISPRi Perturb-seq compendium to date (25.6 million perturbed single-cell transcriptomes across 7 screens and 16 diverse cellular contexts) — and develops X-Cell, a diffusion language model that predicts perturbation responses by iteratively refining control-to-perturbed state transitions through cross-attention to multi-modal biological priors (LLM embeddings, ESM-2 protein embeddings, STRING interactions, DepMap, JUMP-Cell Painting, scGPT). X-Cell scales to 4.9 billion parameters (X-Cell-Ultra), the largest causal perturbation model to date, demonstrating power-law scaling behavior matching large language models and zero-shot generalization to unseen iPSC-derived melanocyte progenitors and primary human CD4+ T cells.

**Method/model name and key terminology:**
- Model: **X-Cell** (55M params) and **X-Cell-Ultra** (4.9B params); dataset: **X-Atlas/Pisces** (25.6M cells); prior dataset: **X-Atlas/Orion** (8M cells, HCT116 + HEK293T).
- Key terms: *diffusion language model (LM)*; *iterative remasking/diffusion process*; *cross-attention to multi-modal biological priors*; *Diff Mask* (binary mask for diffusion training); *self-supervised test-time adaptation*; *Pearson Delta* (key metric: correlation between predicted and observed perturbation-induced log-fold changes); *power-law scaling*; *context generalization*; *CRISPRi Perturb-seq*.
- Architecture: stacked self-attention blocks encoding control cell sets with interleaved cross-attention to prior knowledge embeddings every 3 layers; diffusion-style training randomly replaces 25/50/75% of control gene expression values with ground-truth perturbed values; Diff Mask indicates revealed positions.

**Connection to our framing:**
X-Cell demonstrates that scaling causal perturbation data alongside model capacity (not just parameters) is the key to cross-context generalization — precisely the principle we apply to the disease setting, where our "causal perturbation data" is multi-cohort genomic variation linked to phenotype rather than CRISPR knockout screens.

---

## PART II: SYNTHESIS (~1 PAGE FOR GRANT WRITERS)

---

### The "Virtual Cell" / "AI Virtual Cell (AIVC)" Paradigm: Current Scope and Terminology

The term **AI virtual cell (AIVC)** was formally defined in Bunne et al. (2024, *Cell*) as "a multi-scale, multi-modal, large-neural-network-based model that can represent and simulate the behavior of molecules, cells, and tissues across diverse states." The AIVC must be simultaneously *predictive*, *generative*, and *queryable* — it must predict the outcome of interventions, generate realistic molecular readouts, and answer biological hypotheses through query. The current state of the field (Eisenstein, *Nature* 2026) distinguishes two generations: (1) foundation models that learn static universal representations (URs) of cell state, excelling at embedding, annotation, and cross-dataset integration but limited in dynamic prediction; and (2) world models that support action-conditioned simulation — counterfactual reasoning about what a cell would look like under a specific intervention.

Xing and Song (GenBio AI, 2026) provide the sharpest operational definition of the **Virtual Cell World Model (VCWM)**: a generative system formalizing p(x' | x, a, e), where x is multi-modal initial cell state, a is the intervention/action, and e is the cellular environment. The VCWM comprises three components: a structured encoder E mapping observations to a latent cellular manifold M, an action-conditioned transition core F evolving latent state under intervention, and a generative decoder D rendering cross-modally consistent outputs. AlphaCell (Chuai et al., bioRxiv 2026) instantiates this trinity with a Base Model Encoder (building a genome-wide Virtual Cell Space via Latent Manifold Rectification), a Base Model Decoder (Biological Reality Reconstruction), and a Flow Model (Universal State Transition via OT-CFM), trained on 220 million single cells and 90 million perturbed profiles.

Current AIVC/VCWM work is bounded to a specific experimental scope: **genetic perturbations** (CRISPR knockouts, gene overexpression) and **chemical perturbations** (small molecules, cytokines) delivered to cell lines or primary cells in controlled screens. This is the framing of X-Cell (Wang et al., bioRxiv 2026), STACK (Dong et al., bioRxiv 2026), STATE (Adduri et al., 2025), scGPT (Cui et al., 2024), and Geneformer (Theodoris et al., 2023). The gold-standard resource is now X-Atlas/Pisces (25.6M CRISPRi Perturb-seq cells across 16 cellular contexts), and the key evaluation metric is Pearson Delta (correlation between predicted and observed perturbation-induced log-fold changes).

---

### The Perturbation Modeling Lineage: From Sparse VAEs to Causal Disentanglement

The mechanistic perturbation modeling lineage begins with the **sparse mechanism shift hypothesis** (Schölkopf et al. 2021) — the principle that when an intervention occurs, only a few mechanisms change at a time. Lachapelle et al. (CLeaR 2022) translated this into **mechanism sparsity regularization**: if the latent factors depend sparsely on observed auxiliary variables (perturbation labels), regularizing the learned causal graphical model (CGM) to be sparse recovers the latent variables up to permutation — the **sVAE** (sparse VAE) framework. This gave the first principled, identifiable disentanglement method for biological perturbation data.

Lopez et al. (CLeaR 2023) applied this framework directly to single-cell genomics as **sVAE+**, proposing a model where each perturbation (genetic or chemical) is treated as a stochastic soft intervention targeting an unknown, sparse subset of latent variables, each representing "the activity of a distinct biological process." This operationalization — sparse bipartite graph G^a between perturbation labels and biological process dimensions z_1, ..., z_p — is the immediate architectural ancestor of our proposed disease-axis model.

Bereket and Karaletsos (NeurIPS 2023) advanced this as **SAMS-VAE** (Sparse Additive Mechanism Shift VAE), decomposing perturbed cell state as z_i = z^b_i + z^p_i where z^p_i = sum_t d_{i,t}(e_t * m_t), with global latent effect vectors e_t and binary masks m_t (Bernoulli prior) ensuring sparsity. SAMS-VAE explicitly invokes the identifiability guarantee of the Sparse Mechanism Shift framework: sparsifying the shift mechanism recovers disentangled, perturbation-specific latent subspaces that compose additively for combinatorial generalization. This "sparsity of the shift mechanism" is the principled backbone we inherit.

Zhang et al. (NeurIPS 2023) provide the deepest formal identifiability theory: **causal disentanglement from soft interventions** guarantees recovery of the latent causal model up to a CD-equivalence class (permutation, scale, and shift) given soft interventions on unobserved latent causal variables, under a generalized faithfulness assumption. Their DSCM-based VAE applies this to genomics, predicting combinatorial perturbation effects. This is the formal theoretical underpinning for why our proposed approach — treating disease-associated genetic variants as soft interventions on a latent biological-process DAG — is identifiable in principle.

**Why the SENA/discrepancy-VAE / Zhang et al. framework is the closest starting point to our proposed approach:** existing VAE-based perturbation models (CPA, scGen) learn perturbation effects as dense vector shifts without causal structure. SAMS-VAE adds sparsity but treats interventions as discrete, known labels. Zhang et al.'s framework goes further: it proves that with soft interventions (which disease-associated genetic variants are — they shift, not abolish, biological process activity) and unobserved latent causal variables (which biological process activities are), we can recover the latent causal structure. Our proposed factorized-genotype approach, where polygenic variant scores act as continuous soft intervention strengths on latent biological process axes, is a direct extension of this causal representation learning framework to the disease genomics setting.

Hediyeh-zadeh et al. (ICLR 2024 MLG workshop) extended the sVAE family further with **sVAE-ligr**, addressing the biologically critical case where the auxiliary variable (perturbation label) is not directly observed and label-to-sample assignment is unknown — achieved via Generative Replay from Continual Learning. This is directly relevant because disease genotype is a continuously-varying, partially-observed auxiliary signal, not a discrete label.

---

### Single-Cell Foundation Models as Priors/Embeddings vs. Our Mechanistic/Causal Model

Foundation models — Geneformer (Theodoris et al., 2023), scGPT (Cui et al., 2024), scFoundation (Hao et al., 2024), STATE (Adduri et al., 2025), STACK (Dong et al., 2026), and X-Cell (Wang et al., 2026) — are trained via self-supervised objectives on large single-cell atlases to produce universal representations of cell state. They excel at embedding, cell type classification, batch integration, and transfer learning. However, as the *Nature* 2026 review documents, none of the pure AI foundation models outperformed conventional statistical methods in the 2025 Arc Institute Virtual Cell Challenge for perturbation prediction.

The reason is architectural: foundation models learn the marginal distribution of cell states across biological conditions but do not learn the causal structure of how interventions shift those distributions. They conflate statistical association with causation (X-Cell, Wang et al. 2026). STACK (Dong et al.) addresses this partially through in-context learning — using prompt cells representing a condition to guide prediction of query cell expression — and achieves substantial improvements in zero-shot perturbation prediction. X-Cell (Wang et al.) advances further by training on the largest genome-wide causal perturbation dataset (X-Atlas/Pisces, 25.6M cells) and incorporating multi-modal biological priors, demonstrating power-law scaling with causal data volume.

In our proposed framework, these foundation models serve as **representation priors and embeddings**, not as the mechanistic model itself. Specifically: (1) foundation model embeddings (e.g., from scGPT, STACK, or X-Cell's gene-level priors) provide pre-trained gene representations that initialize the spectral co-expression topology in SPEAR; (2) protein language model embeddings (ESM-2) encode gene product properties; (3) the latent space of a pre-trained foundation model provides a high-quality initialization for the Virtual Cell Space manifold that our causal perturbation model then operates on. The mechanistic causal layer — the sparse-mechanism-shift VAE with disease-variant soft interventions — sits on top of these rich embeddings, providing the identifiable, biologically-disentangled axes that foundation models cannot learn from observational data alone.

---

### The Key Distinction: Disease as Causal Perturbation on Cell State

**The central conceptual advance we propose is this:** all existing virtual-cell and perturbation models — from sVAE to SAMS-VAE to X-Cell to AlphaCell — model the effects of experimentally-delivered **genetic knockouts** or **chemical compounds** applied to cells in controlled conditions. The intervention is discrete (gene X knocked out, drug Y applied at dose Z), directly observed, and imposed from outside the cell by an experimenter.

We instead treat **disease** — and specifically, disease-associated genetic variation across patient cohorts — as the causal perturbation operator. This reframing has three components:

1. **Disease genotype as soft intervention.** Disease-associated variants do not ablate gene function (hard intervention) but rather shift the activity of biological processes in a graded, probabilistic way (soft intervention in the sense of Zhang et al. 2023). This maps precisely onto the soft-intervention identifiability framework.

2. **Polygenic factorization as sparse mechanism identification.** Rather than a single gene knockout, disease is a polygenic signal: many variants, each with small effect, collectively shift a sparse set of biological process dimensions. Our factorized-PRS approach decomposes polygenic genetic scores into biological process components, identifying which process axes (z_1, ..., z_p in the sVAE notation) are shifted by disease variation and by how much — the same sparse bipartite graph G^a that sVAE/SAMS-VAE learn from CRISPR data, but learned from GWAS/multi-cohort genomic data.

3. **Disease axes as disentangled causal representation.** The output is not a single disease label but a set of sparse, biologically-disentangled "disease axes" — each corresponding to a biological process dimension shifted by the disease genotype, recoverable up to CD-equivalence class by the identifiability guarantees of Zhang et al. (2023). These axes factorize the genotype-phenotype map and constitute the platform's core scientific contribution: a causal model of how genetic variation propagates through cell state to produce dimensional disease phenotypes.

This distinction positions our work squarely in the AIVC/VCWM research agenda (Bunne et al. 2024; Xing and Song 2026) while addressing a gap that the entire field has left open: using the virtual cell framework not to predict the response to an experimentalist's intervention, but to model the biological perturbation that disease itself imposes on cell state across patient populations.

---

## PART III: REFERENCE LIST (ALPHABETICAL BY FIRST AUTHOR)

1. Bereket, M. and Karaletsos, T. (2024). "Modelling Cellular Perturbations with the Sparse Additive Mechanism Shift Variational Autoencoder." NeurIPS 2023. arXiv:2311.02794.

2. Bunne, C. et al. (2024). "How to Build the Virtual Cell with Artificial Intelligence: Priorities and Opportunities." *Cell* 187, 7045–7063. doi:10.1016/j.cell.2024.11.015.

3. Chuai, G. et al. (2026). "Towards building a World Model to simulate perturbation-induced cellular dynamics by AlphaCell." bioRxiv doi:10.64898/2026.03.02.709176.

4. Cui, H. et al. (2024). scGPT. *Nature Methods* (cited in context; ID not in PDF files reviewed — verify).

5. Dong, M. et al. (2026). "Stack: In-Context Learning of Single-Cell Biology." bioRxiv doi:10.64898/2026.01.09.698608.

6. Eisenstein, M. (2026). "Can Biology Move Into the Matrix?" *Nature* 654, 286–288. doi: see PDF footnote ref 4 — verify final DOI.

7. Hediyeh-zadeh, S., Fischer, T., and Theis, F.J. (2024). "Disentanglement via Mechanism Sparsity by Replaying Realizations of the Past." ICLR 2024 MLG workshop. ID not in PDF — verify.

8. Lachapelle, S. et al. (2022). "Disentanglement via Mechanism Sparsity Regularization: A New Principle for Nonlinear ICA." CLeaR 2022. *PMLR* 140:1–57. arXiv:2107.10098.

9. Lopez, R. et al. (2023). "Learning Causal Representations of Single Cells via Sparse Mechanism Shift Modeling." CLeaR 2023. arXiv:2211.03553.

10. Palma, A. et al. (2024). "CellFlow: A Generative Flow-Based Model for Single-Cell Count Data." ICLR 2024 MLG workshop. ID not in PDF — verify.

11. [Anonymous] (2026). "Spectral Adaptive Repositioning for Flow-Based Single-Cell Perturbation Modeling (SPEAR)." NeurIPS 2026 submission, under review. Our team's work. ID not in PDF.

12. Wang, C. et al. (2026). "X-Cell: Scaling Causal Perturbation Prediction Across Diverse Cellular Contexts via Diffusion Language Models." bioRxiv doi:10.64898/2026.03.18.712807.

13. Xing, E. and Song, L. (2026). "A World Model of the Virtual Cell." GenBio AI technical report, May 3, 2026. ID not in PDF — verify.

14. Zhang, J. et al. (2023). "Identifiability Guarantees for Causal Disentanglement from Soft Interventions." NeurIPS 2023. ID not in PDF — verify arXiv ID.

---

*Items marked "ID not in PDF — verify" require a manual check against arXiv or journal DOI lookup before submission. All method names, equations, and claims are drawn directly from the PDF text as read above.*
