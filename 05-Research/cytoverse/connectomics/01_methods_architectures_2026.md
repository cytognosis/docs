# fMRI foundation-model methodologies and architectures (2025 to 2026)

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: researchers, stakeholders
> **Tags**: `research`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

Six papers reviewed: Taylor et al. (HCP / lifespan, *Nature* 2026), NeuroSTORM (Wang et al., *Nat. Biomed. Eng.* 2026), Brain-Semantoks (Gijsen et al., arXiv 2025), SLIM-Brain (Wang et al., arXiv 2026), Omni-fMRI (Wang et al., arXiv 2026), and BrainGFM (Wei et al., ICLR 2026). Taylor is included for the lifespan FC-gradient methodology; the other five are foundation models.

---

## 1. Five distinct architectural paradigms now coexist

| Paradigm | Input representation | 2025–2026 exemplar |
|---|---|---|
| Time-series volumetric | Raw 4D BOLD voxel volumes | NeuroSTORM, SLIM-Brain, Omni-fMRI |
| Time-series ROI | Parcel-wise ROI time series (T x N) | Brain-Semantoks, BrainLM |
| Connectome / static FC | Pearson FC matrix per subject | BrainNetTF, BrainMass, BrainNPT |
| Brain graph | Top-k sparsified FC matrix as a graph | BrainGFM (first foundation model in this class) |
| Surface-vertex (no foundation model) | Vertex-wise time series on cortical surface | Taylor (lifespan gradients) |

The headline result of the year is that all four 4D / ROI / connectome / graph paradigms reach broadly comparable accuracy on the same downstream benchmarks (HCP-task classification, ABIDE autism, ADHD200, ADNI). The trade-off is now along compute, memory, and adaptability, not along representation power.

---

## 2. Per-paper methodology

### 2.1 Taylor et al. (HCP lifespan, Nature 2026)

Not a foundation model. The methodology is included here because it is the cleanest 2026 example of harmonised cross-cohort fMRI analysis at population scale.

* **Backbone analysis:** vertex-wise FC gradients computed by diffusion-map embedding of FC matrices, then aligned to a lifespan template via one-shot Procrustes.
* **Statistical model:** generalised additive mixed models (GAMMs) with random intercept per cohort over 3,972 gradient sets across the 16-day to 100-year lifespan.
* **Software:** BrainSpace for diffusion-map embedding; FSL + ANTs + Spherical Demons for upstream alignment.
* **Validation:** held-out cosine similarity between individual gradients and a template; Procrustes alignment; structure-function coupling against morphometric similarity networks (MSNs).

### 2.2 NeuroSTORM (Wang et al., Nat. Biomed. Eng. 2026)

* **Input:** 4D BOLD volumes resampled to 96 cubed at 2 mm MNI152, TR 0.8 s, per-volume Z-norm.
* **Backbone:** Shifted-Window Mamba (SWM), 4-stage hierarchical state-space model.
* **Pretraining objective:** masked autoencoding (MAE) with a Spatiotemporal Redundancy Dropout (STRD) module that masks voxels with high spatial-temporal matching probability so the model learns long-range dependencies rather than reconstruct trivially redundant neighbours.
* **Fine-tuning:** Task-specific Prompt Tuning (TPT). Backbone frozen; a small set of learnable prompts are inserted; trainable parameters under 5 percent.
* **Compute:** 4 x A6000 (48 GB), 30 epochs, ~13 days.
* **Why Mamba:** linear-time sequence modelling, compatible with long temporal axes that Swin-style ViTs choke on.

### 2.3 Brain-Semantoks (Gijsen et al., arXiv 2025)

* **Input:** ROI time series (Schaefer-400 + Tian-III + Buckner-7 = 457 ROIs), 0.01–0.1 Hz band-pass, per-ROI per-scan z-score, 2 s temporal resampling.
* **Backbone:** transformer encoder; depth 8, hidden 768, projection head MLP D_proj = 128.
* **Tokeniser (the contribution):** a per-network multi-scale convolutional filter bank that aggregates adjacent ROIs in the Yeo 7-network parcellation into one token per network per temporal patch (patch length = 20). Yields 9 networks across cortex + subcortex + cerebellum.
* **Pretraining objective:** self-distillation across two long temporal views (T_crop = 100), DINO/iBOT-style, with a Teacher-guided Temporal Regulariser (TTR) that constrains the token space toward the time-averaged network signature for the first 5 percent of training.
* **Three-loss training:** CLS distillation (global) + token distillation (local) + TTR (curriculum).
* **Fine-tuning:** linear probing protocol (no fine-tuning).
* **Compute:** 1 x GPU, < 20 GB memory, < 2 hours. Most efficient model in the set.

### 2.4 SLIM-Brain (Wang et al., arXiv 2026)

* **Input:** atlas-free 4D BOLD, 96 cubed at 2 mm, TR 0.72 s.
* **Two-stage adaptive pipeline.** Stage 1: a lightweight ViT-MAE on full sequences scores 5-frame temporal windows by mutual masked reconstruction and emits the top-k informative windows. Stage 2: only the top-k windows go to a Hiera-JEPA encoder at voxel resolution. ~70 percent of patches are masked; ~50 percent of background voxels are dropped via a brain mask.
* **Pretraining objective:** Joint Embedding Predictive Architecture (JEPA), latent-space prediction rather than pixel-space reconstruction. EMA target encoder, smooth-L1 regression at masked indices.
* **Fine-tuning:** linear probing or full fine-tuning.
* **Compute:** 1 x A100 (80 GB), 40 epochs, ~20 hours, ~4,129 sessions of pretraining. Roughly 30 percent of the GPU memory of Swin-based 4D models.
* **Engineering claim:** training efficiency, not data scale, is the bottleneck.

### 2.5 Omni-fMRI (Wang et al., arXiv 2026)

* **Input:** atlas-free 4D BOLD, 96 cubed at 2 mm, TR 0.72 s, voxel-level global Z-scoring.
* **Backbone:** standard ViT encoder + MAE objective.
* **Tokeniser (the contribution):** dynamic content-adaptive patch tokenisation. Spatiotemporal complexity is estimated from time-averaged intensity variance per local cube. Low-complexity foreground gets coarse 8-cubed patches; high-variance foreground recursively subdivides to 4-cubed sub-patches; > 50 percent background discarded outright. Token count drops from ~14 K to ~4.3 K.
* **Multi-scale embedding:** dual-path projection so coarse and fine patches share one latent space; scale-aware decoder routes each token to a scale-specific reconstruction head.
* **Compute:** 4 x A10G (24 GB), 35 epochs, ~32 hours. Pretrains on 49,497 sessions across 9 cohorts.
* **Reproducibility commitment:** full experiment logs, exact test-subject IDs, and standardised dataset splits released alongside the code.

### 2.6 BrainGFM (Wei et al., ICLR 2026)

* **Input:** brain graphs constructed from Pearson-correlation FC matrices, top-k sparsified, with the ROI's correlation profile as the node feature vector. Multiple atlases simultaneously: Schaefer100/200/300, Shen268, Power264, Gordon333, AAL116, AAL3v1; 8 parcellations total.
* **Backbone:** Graph Transformer (Yun et al. 2019). Random Walk Structural Encoding (RWSE) for positional encoding (more efficient and accurate than Laplacian PE on brain graphs per the appendix ablation).
* **Token sequence:** [T/D] task/disorder token + [A/P] atlas/parcellation token + ROI tokens. Both the [T/D] and [A/P] tokens are language embeddings produced by BioClinicalBERT from short textual descriptions of the disorder or atlas.
* **Pretraining objective (dual):** Graph Contrastive Learning (GCL) with NT-Xent loss over augmented graph views + Graph Masked Autoencoder (GMAE) with random node and edge masking; both objectives share the same encoder.
* **Few-shot adaptation:** MAML-style meta-learning over learnable graph prompts (node and edge prompts), with the backbone frozen. Inner loop adapts prompts on a (disorder, atlas) task; outer loop meta-updates the prompt initialisation.
* **Zero-shot adaptation:** language-prompt tokens describing the previously unseen disorder or atlas are injected via BioClinicalBERT, enabling adaptation without any gradient updates.
* **Compute:** Adam optimizer, batch size 128, lr 1e-4, 50 epochs, single-GPU regime.
* **Generalisation claim:** the only pretrained brain FM evaluated systematically across full-shot, few-shot (10 percent and 1 percent), and zero-shot regimes, against 25 disorders.
* **Code:** <https://github.com/weixinxu666/BrainGFM>.

---

## 3. Architecture comparison

| Aspect | Taylor (HCP) | NeuroSTORM | Brain-Semantoks | SLIM-Brain | Omni-fMRI | BrainGFM |
|---|---|---|---|---|---|---|
| Foundation model | No (analytical) | Yes | Yes | Yes | Yes | Yes |
| Input representation | Surface vertex | 4D voxel | ROI time series | 4D voxel | 4D voxel | Brain graph (FC) |
| Pre-training paradigm | n.a. | MAE + STRD | Self-distillation (DINO/iBOT) + TTR | JEPA | MAE + dynamic patch | GCL + GMAE |
| Backbone | n.a. | Shifted-Window Mamba | Transformer | Hiera-JEPA + ViT-MAE selector | ViT (standard) | Graph Transformer + RWSE |
| Atlas-aware | n.a. | No (volumetric) | Schaefer-400 + Tian-III + Buckner-7 + Yeo-7 | No (volumetric) | No (volumetric) | Yes (8 atlases via [A/P] tokens) |
| Adaptation method | n.a. | Task-specific Prompt Tuning (TPT) | Linear probe | Linear probe / full FT | Linear probe / full FT | MAML over graph prompts (few-shot) + language prompts (zero-shot) |
| Trainable params at FT | n.a. | < 5 % of backbone | linear head only | full or linear | full or linear | graph prompt only (frozen backbone) |
| Compute at pre-training | n.a. | 4 x A6000 (48GB), ~13 days | 1 GPU, < 20 GB, < 2 hours | 1 x A100 (80GB), ~20 hours | 4 x A10G (24GB), ~32 hours | single-GPU, 50 epochs |
| Few-shot regime | n.a. | partial | partial | partial | partial | explicit (1 % and 10 %) |
| Zero-shot regime | n.a. | no | no | no | no | yes (language prompts) |
| Code release | partial (Methods) | yes (open weights) | yes (open weights) | promised at acceptance | yes (open code, logs, IDs) | yes |

---

## 4. Pretraining objectives: a converging space

Five distinct objectives are now in active use; they break into two camps.

* **Reconstruction-style** (low-level, pixel- or token-level): masked autoencoding (MAE) in NeuroSTORM and Omni-fMRI; Graph Masked Autoencoder (GMAE) in BrainGFM.
* **Latent-prediction or contrastive-style** (high-level, abstract): JEPA in SLIM-Brain; self-distillation (DINO/iBOT) in Brain-Semantoks; Graph Contrastive Learning (GCL) in BrainGFM.

BrainGFM combines both (GCL + GMAE) and reports superior performance to either alone, mirroring the same trend in vision (DINOv2 + iBOT). Brain-Semantoks argues explicitly that reconstruction objectives are sub-optimal for noisy fMRI because they incentivise modelling acquisition noise; latent-prediction or distillation gives more transferable representations. Omni-fMRI counters that MAE plus dynamic patch tokenisation can reach comparable transfer at half the compute. The community has not yet settled.

Curriculum tricks matter at the margin:

* Brain-Semantoks: Teacher-guided Temporal Regulariser (TTR) decayed to zero over the first 5 percent of training stabilises self-distillation on low-SNR fMRI.
* NeuroSTORM: Spatiotemporal Redundancy Dropout (STRD) drops voxels whose context is trivially predictable to force long-range learning.
* Omni-fMRI: Zero-initialised residual MLP (ZeroMLP) so the model first learns coarse low-frequency embeddings and only later adds high-frequency structural details.
* BrainGFM: a learnable graph prompt is meta-trained on a held-out task distribution to facilitate fast adaptation on unseen disorders.

---

## 5. Fine-tuning and adaptation

The same direction-of-travel as in NLP is now visible: full fine-tuning is being abandoned in favour of parameter-efficient adaptation.

| Method | Trainable params | Backbone frozen | Used by |
|---|---|---|---|
| Full fine-tuning | 100 % | No | early baselines (BrainNetCNN, BrainGNN) |
| Linear probing | head only | Yes | Brain-Semantoks (default), SLIM-Brain (alt), Omni-fMRI (alt) |
| Prefix tuning (PEFT) | small prefix vectors | Yes | BrainGFM ablation (PEFT-Prefix) |
| LoRA | low-rank adapters | Yes | BrainGFM ablation (PEFT-LoRA) |
| Task-specific Prompt Tuning (TPT) | < 5 % prompt set | Yes | NeuroSTORM (default) |
| Graph Prompt Tuning (G-Prompt) | node and edge prompts | Yes | BrainGFM (default for few-shot) |
| Meta-learned prompts (MAML) | inner-loop prompt updates | Yes | BrainGFM (default for cross-disorder) |
| Language prompts (zero-shot) | none (text-conditioned) | Yes | BrainGFM (default for zero-shot) |

BrainGFM's full ablation shows G-Prompt-Tuning with an edge prompt and multiplicative insertion (instead of additive) reaches 71.2 / 73.5 ACC/AUC on ABIDE II ASD, virtually matching full fine-tuning at 70.5 / 73.3 with two orders of magnitude fewer trainable parameters. This is the strongest evidence in the set that prompt-style adaptation is now the right default for fMRI foundation models.

---

## 6. Hardware and efficiency frontier

| Model | GPU class | Memory | Wall-clock | Pretraining N | Trainable params at FT |
|---|---|---|---|---|---|
| BrainMass (prior baseline) | 8 x V100 | per-GPU | ~150 hours | 64 584 sessions | 100 % |
| Brain-JEPA (prior baseline) | 4 x A100 (40 GB) | per-GPU | ~300 epochs | 32 K sessions | 100 % |
| NeuroSTORM | 4 x A6000 (48 GB) | 44.34 GB / GPU | ~13 days, 30 epochs | > 50 000 participants, 28.65 M frames | < 5 % (TPT) |
| SLIM-Brain | 1 x A100 (80 GB) | ~2.4 GB / sample | ~20 hours, 40 epochs | ~4 129 sessions | linear head |
| Omni-fMRI | 4 x A10G (24 GB) | per-GPU | ~32 hours, 35 epochs | 49 497 sessions | linear head |
| Brain-Semantoks | 1 x GPU | < 20 GB | < 2 hours, 100 epochs | 39 139 UKB recordings | linear head |
| BrainGFM | single-GPU | low | ~50 epochs | > 25 000 subjects, 60 000 scans, 400 000 graph samples | small graph prompt |

Three of the six top out at a single GPU now. Brain-Semantoks's < 2 hour training time on one GPU, and SLIM-Brain's deliberate attack on the data and training efficiency frontier, are evidence that the field has decisively moved away from "pretrain on the largest possible corpus on the largest possible cluster". Cytognosis can credibly enter this space with a single-A100 budget.

---

## 7. Cross-paper trends and open questions

* **Atlas-aware vs atlas-free has become a balanced argument.** Atlas-free volumetric models (NeuroSTORM, SLIM-Brain, Omni-fMRI) avoid a parcellation prior but pay a memory cost. Atlas-aware models (Brain-Semantoks, BrainGFM, ROI baselines) benefit from anatomical priors and are dramatically faster, and BrainGFM shows that pretraining on multiple atlases at once is strictly better than any single atlas. The right Cytognosis bet is to emit both representations from the same preprocessed dataset; see the data doc.
* **Multi-atlas pretraining is the most surprising 2026 result.** BrainGFM Table 2: pretraining on Schaefer100 + Schaefer200 + Schaefer300 + AAL116 with 8 parcellations (mixed atlases) gives 70.5 / 73.3 fine-tuning accuracy on ABIDE II ASD vs. 67.5 / 70.2 on Schaefer100 alone (no pretraining gives 65.2 / 67.1). Multi-atlas effectively augments the pretraining corpus 8x without acquiring any new fMRI data.
* **Language prompts unlock zero-shot in fMRI.** BrainGFM is the first to show that BERT-encoded textual descriptions of disorders and atlases can drive zero-shot adaptation on completely unseen conditions. This is the same pattern that drove CLIP for vision and is the opening shot for fMRI x clinical-text foundation models.
* **Scaling laws are still nascent.** Brain-Semantoks reports the only systematic scaling analysis (Figure 2): performance follows a power-law in pretraining sample size both in-distribution (UKB age and sex) and out-of-distribution (HBN). SLIM-Brain claims data-efficient scaling at 4 K sessions; Omni-fMRI does dataset-size sweeps at 3 K to 50 K subjects and reports continued improvement. There is no consensus exponent yet.
* **Task-fMRI is treated as a downstream test, not a pretraining input.** All five FM papers pretrain on rs-fMRI and benchmark on task-fMRI in zero-shot or few-shot. None have systematically integrated task-fMRI into pretraining; BrainGFM's "Limitations" calls this out explicitly. This is an open frontier where the HED event-annotation standard becomes the enabling technology (see tools doc).
* **Modality fusion is on the roadmap.** BrainGFM "Broader Impact" section lists DTI, EEG, and MEG as immediately adjacent. The graph paradigm is naturally multi-modal because all four modalities reduce to a graph at some level. This is also where the NWB ecosystem becomes relevant for Cytognosis.
* **All models are evaluated on a small overlapping set of downstream tasks.** ABIDE (autism), ADHD200, ADNI (AD/MCI), HCP-task classification, sex prediction, age regression. There is currently no agreed-upon benchmark suite, no held-out test set protocol shared across papers, and no leaderboard. This is the cheapest place where Cytognosis could lead with a single curated, harmonised, FAIR cross-cohort evaluation suite.

---

## 8. Methodology recommendations for a Cytognosis foundation model

Bias toward the simplest design that still captures the 2026 frontier.

1. **Backbone:** Mamba (NeuroSTORM lineage) for 4D voxel input, or Graph Transformer with RWSE (BrainGFM lineage) for graph input. Both are now off-the-shelf.
2. **Pretraining objective:** combine reconstruction and contrastive losses (BrainGFM showed they are complementary). MAE or GMAE for the reconstruction half; SimCLR-style or NT-Xent for the contrastive half; momentum-encoder distillation as a third complementary loss is worth ablating.
3. **Tokenisation:** dynamic / content-adaptive (Omni-fMRI lineage) for voxel input; multi-network semantic tokens (Brain-Semantoks lineage) for ROI input; multi-atlas tokens (BrainGFM lineage) for graph input. Avoid uniform tokenisation.
4. **Fine-tuning:** parameter-efficient first. Default to TPT (NeuroSTORM lineage) or graph prompt tuning (BrainGFM lineage). Reserve full fine-tuning for ablation only.
5. **Cross-disorder generalisation:** meta-learn the prompt initialisation (MAML inner / outer loop, BrainGFM lineage) over a held-out task distribution constructed from (disorder, atlas) pairs.
6. **Zero-shot:** condition on BioClinicalBERT-encoded language descriptions of the disorder, atlas, and acquisition protocol. This is approximately free given the prompt-tuning architecture and is the only known route to true zero-shot transfer in this field.
7. **Hardware footprint:** target a single 80 GB A100 or 4 x 24 GB A10G as the design constraint. The 2026 results show this is now sufficient for state-of-the-art; the era of cluster-scale pretraining for fMRI is plausibly over for the time being.
