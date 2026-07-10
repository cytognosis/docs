## 10. Core thesis: disease as the causal perturbation operator

> [!IMPORTANT]
> **The bet:** existing virtual-cell and perturbation models learn the effects of experimentally delivered perturbations (a CRISPR knockout, a compound). We instead treat **disease, specifically disease-associated genetic variation across patient cohorts, as the causal perturbation operator** acting on a latent causal model of cellular biological processes. This single reframing is what makes our TA1 mechanistic, multiscale, and clinically grounded rather than correlational.

### Why this is the right frame

Most foundation models of the cell are **correlational**: they learn a static representation and predict expression, but they do not encode which molecular events cause which downstream changes, and they do not update when new experiments arrive (section 20). Perturbation predictors add partial causality but stay at one scale and one objective. None integrate atlas-scale data, causal-network inference, and circuit-level physiology into a model that **updates from new experiments**. That integration is our TA1, and the disease-as-perturbation frame is what unlocks it.

### Three components of the thesis

1. **Disease genotype as a soft intervention.** A patient's risk variants act as a sparse, partially specified intervention on unobserved latent biological processes. This is exactly the setting for which **identifiability guarantees exist** for causal disentanglement from soft interventions (Zhang et al. 2023), and it inherits the sparse-mechanism-shift structure of **SAMS-VAE** (Bereket and Karaletsos 2023) and the sVAE lineage (section 23).
2. **Polygenic variation as sparse mechanism identification.** Rather than collapsing risk into a single score, we factorize patient genetic variation into a small number of pathway-disentangled, transdiagnostic axes. The factorization method is proprietary and is documented in restricted section 31; its precedent and the precise novelty claim against **PRSet** are stated there.
3. **Disease axes as a disentangled causal representation.** The recovered axes double as **candidate biotypes**: interpretable coordinates that connect genotype to cell-type pathology to circuit-scale dysfunction, and that TA2 can target for the highest-value experiments.

### The inversion, stated precisely

> We invert the virtual-cell paradigm (Bunne et al. 2024) so that disease-associated genetic variation acts as a soft intervention on a latent causal model of cellular biological processes, for which identifiability guarantees exist (Zhang et al. 2023).

This is the committed novelty sentence used across the Solution Summary and full proposal. It is defensible, specific, and tied to named prior art, which is what ARPA-H reviewers reward.

### What stays constant across every proposal variant

Section 70 shows the team, budget, and disease title all changed over time. The thesis did not. The constants are: a **self-updating, multiscale, mechanistic causal TA1**; a TA2 that is **not a wrapper around a frontier LLM**; and **22q11.2 deletion syndrome** as the Phase I cellular anchor. Treat these three as the load-bearing claims to protect in any revision.
