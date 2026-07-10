## 23. Theory: causal representation learning and identifiability

This section summarizes the theoretical foundations that underpin the TA1 causal generative model. All claims are drawn from cited literature; this section is conceptual and does not describe our proprietary methods.

---

### 23.1 The sparse mechanism shift hypothesis

The foundational principle of our causal architecture is the **sparse mechanism shift hypothesis** (Schölkopf et al. 2021). The hypothesis states: when an intervention occurs, only a few mechanisms change at a time. Formally, if the data-generating process is governed by a set of causal mechanisms, an intervention on a variable X changes only the mechanism for X, leaving all other mechanisms intact. This sparse change is what distinguishes interventional distributions from observational distributions and is what makes causal structure learnable from multi-environment data.

The sparse mechanism shift is the correct prior for biological perturbation data: a CRISPR knockout of gene X, or a disease-associated variant at locus Y, perturbs a small number of downstream biological process mechanisms rather than globally reorganizing the cell's regulatory state.

---

### 23.2 Mechanism sparsity regularization and identifiable disentanglement (sVAE)

Lachapelle et al. (CLeaR 2022) translated the sparse mechanism shift into a practical disentanglement algorithm via **mechanism sparsity regularization**. The key result (Theorem 5 in Lachapelle et al.): if the latent factors of interest depend sparsely on observed auxiliary variables (perturbation labels) via a causal graphical model (CGM), then regularizing the learned CGM to be sparse recovers the latent variables up to permutation equivalence.

The implementation is a VAE-based model, called **sVAE**, where:

- Latent factors z_1, ..., z_p each represent a distinct biological process.
- Each perturbation label a_k connects to a sparse subset of latent factors via the bipartite adjacency G^a (the "action-to-latent" graph).
- Regularizing G^a toward sparsity forces the model to allocate each perturbation to a minimal, disentangled set of biological process dimensions.
- The recovered latent factors are permutation-identifiable: the model cannot confuse two distinct biological processes, up to an arbitrary reordering of the latent dimensions.

This established the first principled, identifiable disentanglement method grounded in causal theory for biological perturbation data.

---

### 23.3 Sparse mechanism shift in single-cell genomics (sVAE+)

Lopez et al. (CLeaR 2023) applied the sparse mechanism shift framework directly to single-cell genomics. **sVAE+** treats each genetic or chemical perturbation as a stochastic soft intervention targeting an unknown, sparse subset of latent variables. The key biological interpretation: each latent unit z_i represents "the activity of a distinct biological process." The sparse bipartite graph G^a learned by the model identifies which biological processes are shifted by each perturbation and by how much.

sVAE+ introduces a Bayesian extension via a Beta(1, K) prior on perturbation-target probabilities, avoiding the hyperparameter sensitivity of the original sVAE binary masks. Models exploiting the sparse mechanism shift hypothesis significantly outperform non-causal baselines on out-of-distribution transfer learning tasks in CRISPR perturbation data.

---

### 23.4 Additive sparse mechanism shifts (SAMS-VAE)

Bereket and Karaletsos (NeurIPS 2023) advanced the framework as **SAMS-VAE** (Sparse Additive Mechanism Shift VAE). The model decomposes perturbed cell state as:

> z_i = z^b_i + z^p_i, where z^p_i = sum_{t} d_{i,t} (e_t * m_t)

Here z^b_i is the basal (unperturbed) state embedding, e_t is a global latent effect vector for perturbation t, and m_t is a binary mask (Bernoulli prior with small alpha) that enforces sparsity. The mask m_t identifies which biological process dimensions are shifted by perturbation t; the global effect vector e_t represents the direction and magnitude of the shift.

The identifiability claim follows directly from the Sparse Mechanism Shift framework: sparsifying the shift mechanism (via m_t) recovers disentangled, perturbation-specific latent subspaces that compose additively for combinatorial generalization. SAMS-VAE was developed in part with contributions from the Cytognosis team at insitro, and its additive decomposition is the immediate architectural predecessor of our TA1 generative core.

---

### 23.5 Identifiability guarantees from soft interventions (Zhang et al.)

Zhang et al. (NeurIPS 2023) provide the deepest formal identifiability theory for our setting. The paper establishes: given **soft interventions** on unobserved latent causal variables, and under a generalized faithfulness assumption, one can recover the latent causal model up to a **CD-equivalence class** (permutation, scale, and shift of latent variables) and predict the effect of unseen combinations of interventions.

Key concepts:

- **Soft intervention**: changes the conditional distribution of a latent variable U_i given its parents, but does not remove the parental dependency (unlike a hard/do-calculus intervention). Disease-associated genetic variants are soft interventions: they shift the activity of a biological process while preserving its regulatory context.
- **Hard intervention**: eliminates the parental dependency entirely (e.g., a complete gene knockout). This is the standard in CRISPR perturbation models.
- **Deep structural causal model (DSCM)**: the decoder architecture proposed by Zhang et al.; models the latent DAG G with nodes representing unobserved causal variables U = (U_1, ..., U_p), where the decoder is a DSCM over this structure.
- **CD-equivalence class**: the set of latent causal models that are statistically indistinguishable from the data; recovery up to this class is the best possible result without additional assumptions.

The paper proves that soft interventions, even when they do not identify the exact mechanism, provide sufficient constraint to guarantee latent causal structure recovery. This is the formal theoretical backbone for why our proposed approach, treating disease-associated genetic variants as soft interventions on a latent biological-process DAG, is identifiable in principle.

The closely related **SENA-discrepancy-VAE** (de la Fuente et al. ICLR 2025) applies causal representation learning with latent factors explicitly constrained to GO biological-process space and provides the current leading edge of causal, interpretable, pathway-grounded single-cell modeling. SENA-style causal identifiability is a design principle for our TA1 extension of SAMS-VAE.

---

### 23.6 The virtual-cell world-model paradigm

The AI virtual cell (AIVC) agenda (Bunne et al. Cell 2024) formally defines the virtual cell as "a multi-scale, multi-modal, large-neural-network-based model capable of representing and simulating the behavior of molecules, cells, and tissues across diverse states," requiring a simultaneously predictive, generative, and queryable system.

Xing and Song (GenBio AI 2026) provide the sharpest operational definition as the **Virtual Cell World Model (VCWM)**, adapting the world-model framework from embodied AI:

> p(x' | x, a, e): next cell state x' conditioned on current state x, action (intervention) a, and cellular environment e.

The VCWM has three components: a structured encoder E mapping multi-modal observations and environment to a latent cellular manifold M, an action-conditioned transition core F that evolves latent state under interventions, and a generative decoder D rendering cross-modally consistent outputs.

The transition core F maps directly to our proposed causal perturbation operator: disease-associated genetic variation constitutes the action a that drives state evolution on the cellular manifold. This transforms the genotype-phenotype problem into action-conditioned latent state evolution, for which identifiability guarantees exist under the soft-intervention framework of Zhang et al.

---

### 23.7 Disease as soft causal intervention: the key reframing

All existing perturbation models treat experimentally delivered genetic knockouts or chemical compounds as the intervention. The intervention is discrete, directly observed, and imposed from outside the cell.

We instead treat disease and disease-associated genetic variation as the causal perturbation operator. This reframing has three theoretical components:

1. **Disease genotype as soft intervention.** Disease-associated variants shift the activity of biological processes in a graded, probabilistic way rather than ablating gene function. This maps onto the soft-intervention identifiability framework of Zhang et al. (2023), providing the theoretical guarantee that disease axes are recoverable from multi-cohort data.

2. **Polygenic decomposition as sparse mechanism identification.** Disease is a polygenic signal: many variants, each with small effect, collectively shift a sparse set of biological process dimensions. Decomposing polygenic genetic scores into biological process components is equivalent to learning the sparse bipartite graph G^a of sVAE/SAMS-VAE from genomic rather than CRISPR perturbation data.

3. **Disease axes as disentangled causal representation.** The output is a set of sparse, biologically disentangled disease axes, each corresponding to a biological process dimension shifted by the disease genotype, recoverable up to CD-equivalence class by the identifiability guarantees of Zhang et al. These axes factorize the genotype-phenotype map and constitute the core scientific contribution of TA1.

This theoretical framing positions our work within the AIVC/VCWM research agenda while addressing the open gap: using the virtual cell to model the biological perturbation that disease imposes on cell state across patient populations, not only the response to an experimenter's discrete intervention.
