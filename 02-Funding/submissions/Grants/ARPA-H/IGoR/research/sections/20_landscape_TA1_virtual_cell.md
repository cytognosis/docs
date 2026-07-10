## 20. Landscape: TA1 disease models and virtual-cell methods

This section surveys the methods our TA1 builds on or differentiates from, organized by class. All evaluation claims are drawn from the cited literature.

---

### 20.1 Correlational single-cell foundation models

**Correlational foundation models** learn universal representations (URs) of cell state via self-supervised objectives on large single-cell atlases. They excel at embedding, annotation, batch integration, and transfer learning. None natively support causal perturbation prediction.

| Method | What it does | Causal? | Multiscale? | Auto-updating? |
|---|---|---|---|---|
| **scGPT** (Cui et al. 2024) | Transformer on ranked gene expression; pre-trained on ~33M cells | No | No | No |
| **Geneformer** (Theodoris et al. 2023) | Transformer with expression-rank tokenization; 30M cell corpus | No | No | No |
| **scFoundation** (Hao et al. 2024) | Read-depth-aware pre-training; 50M cells | No | No | No |
| **UCE** (Rosen et al. 2023) | Universal cell embedding; multi-species | No | No | No |
| **TranscriptFormer** | Large-scale cross-species transcriptome FM | No | Partial (GRN head) | No |
| **scPRINT / scPRINT-2** | GRN-aware cell-state encoder; partial causal structure in GRN head | Partial | Partial | No |

The 2025 Arc Institute Virtual Cell Challenge demonstrated that no pure foundation model outperformed conventional statistical methods on perturbation prediction (Eisenstein, Nature 2026). This gap motivates the shift toward world-model and causal architectures.

---

### 20.2 Perturbation predictors

**Perturbation predictors** model the effect of experimentally delivered genetic or chemical interventions on cell state. They are more directly relevant to disease modeling but treat interventions as discrete, observed labels rather than soft causal operators.

| Method | What it does | Causal? | Multiscale? | Auto-updating? |
|---|---|---|---|---|
| **GEARS** (Roohani et al. 2024) | GNN over gene ontology graph; multigene combinatorial perturbation prediction | Partial | No | No |
| **CPA** (Lotfollahi et al. 2023) | Compositional perturbation autoencoder; additive latent shifts | No | No | No |
| **scGen** (Lotfollahi et al. 2019) | Style-transfer VAE for perturbation response | No | No | No |

GEARS incorporates biological graph structure but not latent causal identifiability. CPA and scGen model perturbation effects as additive or style shifts without causal disentanglement.

---

### 20.3 Causal sVAE lineage (mechanism-sparsity models)

The **sparse mechanism-shift** lineage applies causal representation learning to single-cell perturbation data. This is the closest family to our TA1 causal generative core.

| Method | What it does | Causal? | Multiscale? | Auto-updating? |
|---|---|---|---|---|
| **sVAE** (Lachapelle et al. CLeaR 2022) | Mechanism sparsity regularization for nonlinear ICA; permutation-identifiable latents | Yes | No | No |
| **sVAE+** (Lopez et al. CLeaR 2023) | Applies sVAE to single-cell genomics; Beta-Bernoulli sparse bipartite graph between perturbations and latent biological processes | Yes | No | No |
| **SAMS-VAE** (Bereket and Karaletsos NeurIPS 2023) | Sparse additive mechanism-shift VAE; z = basal + additive sparse perturbation effects; IWELBO training | Yes | No | No |
| **sVAE-ligr** (Hediyeh-zadeh et al. ICLR 2024 MLG) | Extends sVAE to latent intervention labels via Generative Replay; mechanism transportability across modalities | Yes | No | No |
| **Zhang et al. DSCM** (Zhang et al. NeurIPS 2023) | Identifiability guarantees for soft interventions on latent causal DAGs; DSCM decoder; CD-equivalence class recovery | Yes | No | No |
| **SENA-discrepancy-VAE** (de la Fuente et al. ICLR 2025) | Causal identifiability with latent factors constrained to GO biological-process space; current leading edge of causal + interpretable + omics | Yes | Partial | No |

The SAMS-VAE architecture is our direct mechanism-shift backbone. Zhang et al. provide the formal identifiability guarantees. SENA provides the pathway-space conditioning precedent. None of these models treat disease-associated polygenic variants as the intervention signal.

---

### 20.4 Virtual-cell world models and large systems

**World models** support action-conditioned simulation rather than static embeddings; they are the next generation of the AIVC agenda (Bunne et al. Cell 2024).

| Method | What it does | Causal? | Multiscale? | Auto-updating? |
|---|---|---|---|---|
| **AIVC / Bunne et al.** (Cell 2024) | Conceptual framework: predictive-generative-queryable trifecta; maps research agenda | Conceptual | Conceptual | No |
| **VCWM / AIDO** (Xing and Song, GenBio AI 2026) | Operational definition: encoder E + transition core F + decoder D; p(x' \| x, a, e) | Partial | Partial | No |
| **AlphaCell** (Chuai et al. bioRxiv 2026) | Three-component world model; OT-CFM flow over 220M cells + 90M perturbed profiles; genome-wide Virtual Cell Space | Yes (OT-CFM) | No | No |
| **STACK** (Dong et al. bioRxiv 2026) | In-context learning for single-cell biology; 149M cells; Perturb Sapiens whole-organism perturbation atlas | Partial (ICL) | Partial | No |
| **X-Cell / X-Atlas** (Wang et al. bioRxiv 2026) | Diffusion LM; 25.6M CRISPRi Perturb-seq cells; 4.9B params (X-Cell-Ultra); power-law scaling; multi-modal priors | Yes | No | No |
| **Arc STATE** (Adduri et al. 2025) | 270M cells; population-level kernel alignment loss; CRISPR perturbation training | Partial | No | No |
| **CellFlow** (Palma et al. ICLR 2024 MLG) | Flow-matching generative model in raw count space; OT-CFM on Negative Binomial parameters | Partial | No | No |

AlphaCell and X-Cell represent the current frontier in scale and perturbation coverage. Neither treats disease-associated genetic variation as the causal perturbation operator; both are anchored to CRISPR/chemical perturbation paradigms.

---

### 20.5 Systems-biology and network tools

These tools model molecular mechanism explicitly but operate at a single scale and are not experimentally self-updating.

| Method | What it does | Causal? | Multiscale? | Auto-updating? |
|---|---|---|---|---|
| **CARNIVAL** (Liu et al. 2019) | Integer linear programming over signaling networks to find causal paths consistent with omics data | Yes | No | No |
| **COSMOS** (Dugourd et al. 2021) | Combines CARNIVAL with metabolomics; multi-omics causal network | Yes | Partial | No |
| **NicheNet** (Browaeys et al. 2020) | Ligand-receptor signaling model; cell-cell communication | Yes | No | No |
| **Virtual Brain Twin** (TVB; virtualbraintwin.eu 2025) | Computational brain circuit model; data-assimilation loop with clinical imaging | Yes | Circuit only | Partial (clinical) |

The Virtual Brain Twin is the closest single-scale mechanistic comparator; it operates at the circuit level only, without a molecular or cellular causal layer.

---

### 20.6 Genomic regulatory tools

| Method | What it does | Causal? | Multiscale? | Auto-updating? |
|---|---|---|---|---|
| **AlphaGenome** (Google DeepMind 2025) | Sequence-to-regulatory grammar; gene regulatory predictions from DNA; Apache-2.0 code, noncommercial weights | Yes (grammar) | No | No |
| **Enformer** (Avsec et al. 2021) | Deep learning from sequence to gene expression and chromatin; 200 kb context | Yes (grammar) | No | No |
| **Borzoi** (Linder et al. 2023) | Long-range sequence model; 524 kb context; cell-type-specific expression | Yes (grammar) | No | No |

We use AlphaGenome as a tool, not a retrained model, to encode COMT/TBX1/DGCR8 regulatory effects into our network prior layer.

---

### 20.7 Intervention-design GNNs

**PDGrapher** (Gonzalez et al. Nat Biomed Eng 2025) is the key intervention-design baseline. It applies a two-phase graph neural network over an interaction network to (1) propose perturbagens that shift a diseased state toward a healthy target (inverse design), and (2) predict the cellular response to a candidate perturbation, with interventions encoded as edge mutilations on the causal graph. We adopt PDGrapher as our intervention-design component in Pillar 2.

---

### 20.8 Covariance-aware decoders

| Method | What it does |
|---|---|
| **CS-CORE** (Su et al. Nat Commun 2023) | Depth/noise-corrected co-expression from scRNA-seq UMI counts; used as decoder prior |
| **scDesign3** (Song et al. Nat Biotechnol 2024) | Vine-copula-based generative model; preserves gene-gene covariance structure |

Prior VAE-based perturbation models (scVI, SAMS-VAE) use conditionally independent negative-binomial decoders that discard gene-gene covariance. We replace these with CS-CORE-informed vine-copula decoders from scDesign3 to preserve real co-expression structure in reconstructed cells.

---

### 20.9 Gap we exploit

No existing platform integrates single-cell atlas data, perturbation modeling, causal-network inference, and circuit-level physiology into a self-updating multiscale model. Specifically:

- Foundation models are correlational; they cannot be queried for causal mechanism.
- Perturbation predictors treat experimentally delivered knockouts as the only perturbation type; none treat disease-associated polygenic genetic variation as the causal operator.
- The causal sVAE lineage provides identifiability theory but operates on experimental perturbation labels, not disease genotype.
- World models (AlphaCell, X-Cell) scale to massive data but remain anchored to CRISPR/chemical perturbation paradigms with no molecular-to-circuit integration.
- Systems-biology tools (CARNIVAL, NicheNet, Virtual Brain Twin) are single-scale and not experimentally self-updating.

Our TA1 closes this gap by treating disease-associated genetic variation as a soft intervention on a latent causal biological-process model, grounding that model in cell-type-aware network priors and a joint cellular-clinical shift space, and coupling it to a closed experimental loop that returns new data to update the model.
