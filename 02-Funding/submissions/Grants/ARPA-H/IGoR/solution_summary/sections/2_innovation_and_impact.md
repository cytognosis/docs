## 2. Innovation and Impact

**Why genetics, and why it is not enough.** Drug targets with human genetic support succeed clinically about two to three times more often than those without (Nelson et al. 2015; Minikel et al. 2024), and the lift rises with confidence in the causal gene. Yet most psychiatric signal is noncoding with ambiguous variant-to-gene mapping, and even an unambiguous gene rarely hands over a mechanism. The standard repair, statistical-genetics and machine-learning target discovery validated post-hoc in cellular models, confirms that a variant does something but seldom explains how it drives disease, whether that axis is the disease-relevant one, or what else in the pathway is easier to drug.

**What current approaches miss.** Foundation cell models are correlational and static; perturbation predictors are narrow and single-scale; agentic-science systems wrap a language model around a literature search. None integrate atlas-scale data, causal-network inference, and circuit-scale physiology into a model that **updates from new experiments**, and none distinguish a therapeutic effect from a side effect.

**Our innovations.**

1. **Dual grounding in two complementary experiments.** We model cellular and clinical evidence in one shared pathway space. Engineered cellular perturbations give a **known causal intervention** that acts directly on genes but live in an artificial system; natural population genetics give **real, population-scale causal evidence** through inheritance but cannot be experimentally tested and miss the exposome. Each covers the other's blind spot, so the model surfaces disease axes that are mechanistic, population-relevant, and robust to culture artifacts. Genomic factorization (pathway-PRS lineage; method proprietary) aggregates weak, convergent variants into these interpretable axes.
2. **Disease as the causal perturbation operator.** We invert the virtual-cell paradigm (Bunne et al. 2024) so that disease-associated genetic variation acts as a soft intervention on a latent causal model of cellular processes, for which identifiability guarantees exist (Zhang et al. 2023).
3. **A three-latent structural causal model** that separates a cell's **basal state**, the **disease effect** (causal on the cell state), and a **treatment effect** that acts either **directly** on the cell (a side-effect route) or by **modulating the disease** (the therapeutic route). This makes "does an intervention correct the disease or merely move the cell" an identifiable question.
4. **A self-updating, multiscale, mechanistic TA1** grounded in human genetics and clinical cohorts and paired with isogenic cellular models, rather than a static foundation model.

| Capability | Foundation cell models | Perturbation predictors | Agentic-science systems | IGoR (this proposal) |
|---|---|---|---|---|
| Mechanistic and causal | No | Partial | No | **Yes** |
| Multiscale (molecule to circuit) | No | No | No | **Yes** |
| Self-updating from new experiments | No | No | Partial | **Yes** |
| Disease genotype as the perturbation | No | No | No | **Yes** |
| Grounded in both cellular and clinical evidence | No | No | No | **Yes** |
| Separates therapy from side effect | No | No | No | **Yes** |
| Closed loop to validated laboratories | No | No | Partial | **Yes** |

**Impact.** Targets that emerge from a model carrying **human genetic support** are roughly two to three times more likely to succeed clinically (Nelson et al. 2015; Minikel et al. 2024), and that multiplier rises with confidence in the causal gene, which is exactly what dual grounding delivers. Penetrant forms calibrate disease axes that **generalize to idiopathic schizophrenia** and span **bipolar disorder** as transdiagnostic coordinates, and the therapy-versus-side-effect distinction directly serves drug discovery. The marquee outcome is **at least 10x faster validated knowledge** by Phase III, with all artifacts delivered to a public repository.
