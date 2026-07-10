# Dimensional Biotyping with Deep Learning: Landscape & State of the Art (2026)

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: leadership
> **Tags**: `strategy`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

**Purpose.** A reference map of the cutting-edge AI/ML for finding disease-related dimensional signatures ("biotypes," "archetypes," "endophenotypes," "axes") across connectomic, genomic, single-omics, and phenotypic data, and for combining them when modalities are only partially paired. Built to sharpen Cytognosis grants (AWS, NIH, ARPA-H, NSF) and to guide the real Cytoverse/Psychoverse build.

**Reading guide.** If you read one thing, read Section 1 (the gap we fill) and Section 8 (recommended architecture). Tables list, per model: training paradigm, loss, output type, and citation.

---

## 1. BLUF — where Cytognosis sits in this landscape

Three findings frame our positioning:

1. **The pretrain-then-finetune paradigm has won within each modality.** Genomic foundation models (Evo 2, AlphaGenome, Borzoi), fMRI foundation models (NeuroSTORM, Brain-JEPA, BrainGFM), and single-cell foundation models (Geneformer, scFoundation) all SSL-pretrain on large healthy/reference corpora, then fine-tune on small disease cohorts with classifier/metric heads. Training a disease model from scratch is no longer competitive.

2. **Continuous, interpretable dimensional axes are still rare and almost entirely single-modality.** Surreal-GAN (the field's gold standard for continuous disease axes) is structural-MRI-only. No genomic or fMRI foundation model yet outputs continuous, named, genetically validated per-person axes; they output embeddings fine-tuned for classification. DeCoDE (cVAE + CCA) is the closest brain-behavior analog but single-site, two-modality, not generative.

3. **For partial/unpaired modalities, generative "unified" models beat alignment-only ones.** CLIP-style contrastive alignment (including COMICAL, the one published genotype-imaging model) cannot impute a missing modality and is hard to extend with a new one. Generative unified models (MoPoE-VAE, MultiVI, MIDAS) impute missing data and add modalities modularly.

**The unfilled gap = our contribution.** No model unifies: (a) an SSL-pretrained genomic foundation encoder, (b) a phenotype encoder, (c) aligned/fused into continuous, interpretable, transdiagnostic biotype axes (Surreal-GAN-style), (d) on a generative backbone that tolerates missing modalities and is modular for connectomics, (e) in psychiatry. That is precisely the Cytoverse/Psychoverse objective.

---

## 2. Local grounding — what Cytognosis has already established

From `04-research/` (transdiagnostic macro/meso/micro, connectomic synthesis, EEG/MEG biotypes):

- A **5–6 axis transdiagnostic connectomic coordinate** (negative-affect/threat, reward/anhedonia, cognitive control, salience/interoception, attention/vigilance, sensory gating), mapped to RDoC/HiTOP.
- A **10-symptom-dimension × 14-disorder matrix** aligned to the Grotzinger 2025 five-factor genomic scaffold (arousal/sleep most universal; psychosis most restricted).
- **High-reproducibility meso edges**: dlPFC–sgACC anticorrelation (SAINT target), amygdala–vmPFC threat regulation, NAc–OFC reward; plus an explicit **replication-failure audit** (Drysdale, AURORA, Etkin, Williams six-biotype).
- **EEG/MEG anchors**: 40 Hz ASSR, sleep-spindle density, RewP, ERN, P300.
- Design philosophy already in place: **biotype-as-Bayesian-prior** updated longitudinally, and the connectome as the **causal mediator** between genomic priors and phenotype (the bridge to the factorized-PRS / BDNF-TrkB work).

This is a strong scientific substrate; the gap is the unified generative model that turns it into per-person multimodal axes.

---

## 3. Single-modality dimensional biotyping — the model landscape

### 3a. Connectomics / fMRI

**Trained directly on disease (continuous axes or contrastive):**

| Model | Yr | Arch | Loss for disease signal | Output | Citation |
|---|---|---|---|---|---|
| Smile-GAN | 2021 | Semi-supervised coupled GAN | adversarial + cycle + cluster | discrete subtypes | Yang, Davatzikos, Med Image Anal 2021 |
| **Surreal-GAN** | 2022 | Semi-supervised GAN, healthy→patient mapping | adversarial + inverse-consistency + monotonicity + orthogonality | **continuous R-index axes** | Yang et al., ICLR 2022 (arXiv 2205.04523) |
| **DeCoDE** | 2025 | contrastive VAE + deep generalized CCA | contrastive ELBO + CCA | continuous brain-behavior axes + biotypes | bioRxiv 2025.10.13.682243 (ABCD, n=3,508) |
| Neurodynamic cVAE (SCZ) | 2024 | contrastive VAE on dynamic FC | contrastive ELBO | disorder-specific latent | Transl Psychiatry 2024 (PMC11655856) |
| Brain-DiT | 2025 | diffusion transformer | score-matching | individualized profiles; digital lesioning | bioRxiv 2025.04.12.648506 |

**SSL-pretrain → fine-tune on disease (fMRI foundation models):**

| Model | Yr | Arch | Pretrain / finetune | Output | Citation |
|---|---|---|---|---|---|
| BrainLM | 2024 | Transformer on ROI time series | masked-recon / supervised | embeddings → age, anxiety, PTSD | Caro et al., ICLR 2024 |
| **Brain-JEPA** | 2024 | JEPA (latent prediction) | latent-prediction / supervised | embeddings, SOTA trait/disease | Song et al., NeurIPS 2024 (arXiv 2409.19407) |
| **NeuroSTORM** | 2026 | Shifted-Window Mamba on raw 4D fMRI; STRD masking; **TPT prompt-tuning (<5% params)** | MAE / supervised CE+MSE | phenotype + disease on **TCP transdiagnostic** (245 pts, 17 dx) | Wang et al., Nat Biomed Eng 2026, DOI 10.1038/s41551-026-01666-y |
| BrainGFM | 2026 | graph FM; graph-contrastive + graph-MAE; language/graph prompts; meta-learning | contrastive+MAE / prompt-supervised | few/zero-shot across 25 disorders | Wei et al., ICLR 2026 (arXiv 2506.02044) |
| LCM | 2025 | 1.2B-param connectome transformer | multitask+brain-environment / supervised | embeddings | AAAI 2026 (arXiv 2510.18910) |

**NeuroSTORM (your linked paper), precisely:** an fMRI foundation model on raw 4D volumes (Shifted-Window Mamba), MAE-pretrained on 50,000+ participants with spatiotemporal redundancy dropout, then adapted by **Task-specific Prompt Tuning** (<5% params) with plain cross-entropy/MSE heads. Applied to the **Transdiagnostic Connectome Project** for phenotype prediction (best PANSS-positive PCC 0.558) and 17-diagnosis classification. No contrastive/GAN/dimensional component, it produces embeddings for supervised heads, not continuous named axes. It is our closest peer and direct comparator.

### 3b. Genomic (WGS / SNP array)

**Sequence-to-function (fine-tune for individual disease effects):**

| Model | Yr | Arch | Disease adaptation | Citation |
|---|---|---|---|---|
| Enformer | 2021 | Transformer (~200 kb) | LoRA fine-tune → individual eQTL | Avsec et al., Nat Methods 2021 |
| Borzoi | 2023 | U-Net + Transformer (~500 kb) | PEFT/LoRA (0.1% params) → personal expression | Linder et al., Nat Genet 2023 |
| **AlphaGenome** | 2025/26 | U-Net+Transformer+2D contact (1 Mb, 1 bp) | multi-modal variant scoring; assigns direction to 49% of GWAS credible sets | Nature 2026 (bioRxiv 2025.06.25.661532) |

**Genomic language models (zero-shot + fine-tune heads):** Nucleotide Transformer (Nat Methods 2024), HyenaDNA (NeurIPS 2023), **Caduceus** (Bi-Mamba, RC-equivariant, ICML 2024), GPN / GPN-MSA (noncoding pathogenicity), **Evo 2** (StripedHyena 7B/40B, 9.3T bp; haplotype embeddings linked to ADNI/UKB AD risk, Nature 2026).

**Deep polygenic / individual-variation models:** **VAE-PRS** (VAE latent coupled to traits; closest published "factorized-PRS" analog; HGG Advances 2025), PRS-Net (GNN epistasis, gene-level attribution), DEEN (ensemble autoencoders), Delphi (transformer over SNPs).

### 3c. Single-omics (transcriptomic / proteomic / epigenomic)

- **scANVI / scVI** (semi-supervised CVAE; disease labels steer latent; production-grade for interpretable axes; Xu et al. 2021).
- **Geneformer** (Nature 2023; v2 95M cells), **scGPT** (Nat Methods 2024), **scFoundation** (100M params, NSR 2024), **UCE** (protein-token, cross-species), **CellFM** (Nat Commun 2025) — SSL-pretrain → fine-tune classifier/perturbation heads.
- **MIDAA** (deep archetypal analysis → interpretable Pareto-extreme archetypes, Genome Biology 2025).
- **Sparse autoencoders on frozen single-cell FMs** (arXiv 2603.02952, 2025): decompose embeddings into GO/KEGG-aligned programs, but current FMs encode **co-expression, not causal regulation**; a disease-supervised fine-tune is needed to make features disease-predictive.

### 3d. Phenotypic / clinical

- **EHR foundation models** (representation layers, pretrain-on-population → finetune-on-disease): **Med-BERT** (npj Digit Med 2021), **CLMBR / CLMBR-T-Base** (Stanford, autoregressive, OMOP), **Foresight** (KCL, generative GPT over SNOMED, Lancet Digit Health 2024), **ETHOS** (zero-shot trajectory, arXiv 2407.21124).
- **Deep dimensional/subtyping on clinical data:** **VaDeSC-EHR** (transformer VAE + survival clustering, Nat Commun 2025), **DeCoDE** (brain-behavior), **BrainSCL** (subtype-guided contrastive, 2026).
- **Key lesson:** EHR FMs give patient embeddings, not interpretable axes; a second-stage healthy-anchored dimensional head (cVAE / Surreal-GAN-style / sparse factor) is required.

---

## 4. Two training paradigms + the loss that extracts disease signal

- **Trained directly on disease** (controls as reference): Smile-/Surreal-GAN, DeCoDE, cVAEs. Losses: **adversarial** (GAN), **contrastive/metric** (cVAE, InfoNCE), monotonicity/orthogonality for axes.
- **SSL-pretrain → fine-tune on disease**: all foundation models. Pretrain loss: masked reconstruction (MAE/MLM), latent prediction (JEPA), autoregressive. Fine-tune head: **classifier (cross-entropy)**, **regression (MSE)**, **metric/contrastive**, or **LoRA/prompt-tuning** for parameter efficiency (NeuroSTORM TPT <5%; Borzoi LoRA 0.1%).
- **Takeaway for us:** adopt a foundation encoder per modality (frozen or LoRA), then a disease-supervised + contrastive head that yields **continuous monotonic axes** (Surreal-GAN insight), anchored to a healthy reference.

---

## 5. Surreal-GAN deep-dive + MULTI Consortium (the dimensional gold standard)

**Surreal-GAN** learns a mapping (healthy control + latent r) → patient, where each component of r is a **continuous, disentangled R-index** (0–1 severity on one neuropathological pattern; a patient expresses several at once). Losses: adversarial + inverse cycle-consistency + **monotonicity** (each r is a severity score) + **pattern orthogonality** (axes capture distinct variance) + Lipschitz smoothness. This is why it yields interpretable continuous axes rather than discrete clusters.

**Applications:** 2 AD dimensions (diffuse vs MTL; Nat Commun 2021); **5 brain-aging dimensions** across 49,482 people with distinct genetics/prognosis (Nat Med 2024); **9 dimensional neuroimaging endophenotypes** across AD/ASD/LLD/SCZ projected into 39,178 UKB, 31 GWAS loci, MR causal path AD2→AD dx (Nat Biomed Eng 2025).

**MULTI Consortium** (Wen, Columbia; Davatzikos, Penn AI2D/iSTAGING): seven **organ-specific MRI biological-age gaps** across brain/heart/liver/adipose/spleen/kidney/pancreas in 313,645 people, linked to proteome/metabolome/genome, 53 loci, 9 druggable anti-aging targets (Nat Med 2026). Validates that per-person continuous dimensional scores generalize to populations, have genetic substrates, and predict cross-organ disease, exactly the endophenotype logic Cytognosis uses.

**Design lessons for us:** (1) **healthy-reference anchoring** removes confound-driven dimensions; (2) **monotonicity + orthogonality** give interpretable, comorbidity-friendly axes; (3) Surreal-GAN is structural-MRI/single-modality, the **functional-connectome and the multimodal versions are open gaps**.

---

## 6. Multimodal with missing / partially-paired modalities (generative imputation)

Reality: different cohorts pair different subsets (genome-only, genome+phenotype, later +connectome). Models that handle this:

| Model | Yr | Modalities | Missing-modality handling | Citation |
|---|---|---|---|---|
| MVAE (PoE) | 2018 | general | product-of-experts; drop missing expert | Wu & Goodman, arXiv 1802.05335 |
| MMVAE (MoE) | 2019 | general | mixture-of-experts; any subset | Shi et al., NeurIPS 2019 |
| **MoPoE-VAE** | 2022 | general | PoE over every subset; principled arbitrary missingness | Sutter et al., ICLR 2022 |
| totalVI | 2021 | RNA+protein | impute protein from RNA via shared latent | Gayoso et al., Nat Methods 2021 |
| **MultiVI** | 2023 | RNA+ATAC(+protein) | single-modality cells use one encoder; impute by decoding shared z | Ashuach et al., Nat Methods 2023 |
| scGLUE | 2022 | multi-omics | graph-guided adversarial alignment of unpaired data | Cao & Gao, Nat Biotech 2022 |
| **MIDAS** | 2024 | RNA+ATAC+protein **mosaic** | shared + private latents; imputes + batch-corrects across mosaic cohorts | PMC11471558 |
| AMM-Diff / ACADiff | 2025 | imaging (+clinical) | conditional **diffusion** generates missing modality | arXiv 2501.12840 / 2603.09931 |
| 4M / Meta-Transformer / Perceiver IO | 2022–24 | many | masked any-to-any; latent bottleneck tolerates any subset | NeurIPS 2023 / arXiv 2307.10802 / ICML 2022 |

**Most relevant pattern:** **MIDAS** (mosaic-aware, shared+private latents, imputation+batch correction) is the closest inductive bias for multi-cohort patient data; PoE/MoPoE and MultiVI are modular (add a modality = add one encoder/decoder).

---

## 7. Unified/joint representation **vs** alignment-only (the explicit distinction)

| | (a) **UNIFIED** — one new fused representation | (b) **ALIGNMENT-ONLY** — per-modality embeddings pulled together |
|---|---|---|
| Examples | totalVI, MultiVI, MIDAS, Cobolt, scMM, MVAE/MMVAE/MoPoE, 4M, Perceiver IO, diffusion fusers | CLIP, ImageBind, BiomedCLIP, **COMICAL** (SNP↔brain-IDP), MaxFuse, scGLUE (mostly) |
| Mechanism | generative fusion / cross-attention / PoE latent | contrastive (InfoNCE) / deep-CCA between fixed encoders |
| Missing modality | handled by the generative process (impute) | tolerated at inference (use available encoder) but **cannot impute** |
| Add a new modality | modular (add expert) | usually **retrain the alignment objective** |
| Cross-modal generation | native | needs an extra decoder |
| Trade-off | single clean representation; harder with missing data unless designed for it | preserves modality-specific info; no new joint space |
| Hybrid | **MIDAS** (shared+private), **mSTAR**, **PRIME** | — |

**Biomedical genome+imaging+clinical fusion is nascent.** **COMICAL** (2024, UKB; CLIP-style SNP↔brain-IDP, rediscovers AD/ADHD/BD associations) is the direct prior art, but it is **alignment-only**, uses imaging-derived phenotypes (not psychiatric dimensions), and cannot impute. mSTAR and PRIME fuse pathology+genomics+text in oncology. **No published model fuses genomic + psychiatric-phenotype (+ later connectome) into a unified, mosaic-aware, dimensional patient representation.**

---

## 8. Recommended architecture for Cytoverse / Psychoverse

Synthesizing the above, the defensible, cutting-edge design is a **generative, mosaic-aware, unified multimodal model with a contrastive alignment term and a Surreal-GAN-style dimensional head**:

1. **Per-modality foundation encoders.** Genomic: pretrained genomic FM (Evo 2 / Nucleotide Transformer), adapted via LoRA. Phenotypic: sparse-autoencoder encoder for interpretable symptom factors. (Later) Connectomic: an fMRI FM encoder (NeuroSTORM/Brain-JEPA-class).
2. **Generative unified backbone** (MoPoE-/MultiVI-/MIDAS-style) with **shared + private latents**, so the model (a) imputes a missing modality, (b) trains on mosaic cohorts with different pairings, and (c) **adds connectomics later as one new expert** without rebuilding, this is what makes the multiscale roadmap real.
3. **Contrastive alignment term** (InfoNCE between genomic and phenotypic latents) layered on the generative ELBO to force cross-modal coherence (the mSTAR/PRIME hybrid lesson).
4. **Healthy-reference-anchored, monotonic, orthogonal dimensional head** (Surreal-GAN insight) to output **continuous, interpretable, transdiagnostic biotype axes** with per-person severity scores, not just embeddings or discrete clusters.
5. **Causal layer (later):** test genomic→phenotypic (→connectomic) drive with mediation/MR, consistent with the DNE precedent (AD2→AD diagnosis).

**Precise novelty vs prior art (for grants):**
- vs **Surreal-GAN**: multimodal and genomic+phenotypic (not structural-MRI single-modality), foundation-model-based.
- vs **COMICAL**: generative **unified** + imputation + dimensional axes (not alignment-only on imaging IDPs).
- vs **NeuroSTORM/Brain-JEPA/BrainGFM**: continuous interpretable **axes** (not classifier embeddings), multimodal.
- vs **DeCoDE**: genomic modality + generative unified + mosaic + foundation encoders (not single-site brain-behavior cVAE).
- vs **MIDAS**: patient-level genomic+psychiatric+connectomic (not single-cell omics).

---

## 9. Implications for grant writing

- **AWS (Round One):** impact-focused; the technical framing in 3.1 ("align genomic + phenotypic embeddings; contrastive") is valid and accessible. The research suggests the stronger, more accurate framing is a **generative unified model that tolerates missing data and is modular for connectomics**, which also coheres better with the multiscale roadmap. Optional to add for Round One; recommended for Round Two and the build.
- **NIH / ARPA-H / NSF (technical):** lead with the **named gap** (Section 1, Section 8 novelty bullets), cite **Surreal-GAN, COMICAL, NeuroSTORM, DeCoDE, MIDAS, Grotzinger 2025** as the comparator set, and benchmark on **UK Biobank, ABCD, HCP, TCP, ADNI**.
- **Benchmarks to claim/target:** cross-modal imputation accuracy (vs MultiVI/MIDAS), dimensional-axis genetic validation (GWAS loci per axis, MR; vs Surreal-GAN DNEs), and transdiagnostic phenotype prediction on TCP (vs NeuroSTORM).
- **Honest constraints:** single-cell/SAE FMs encode co-expression not causal regulation; Drysdale-type cluster solutions failed replication, so claim **continuous axes with monotonicity**, not discrete clusters; model-weight release is constrained by controlled-access DUAs (serve openly for inference; share weights where permitted).

---

## Appendix — key citations
Surreal-GAN (ICLR 2022, arXiv 2205.04523); 5 aging dimensions (Nat Med 2024, s41591-024-03144-x); 9 DNEs (Nat Biomed Eng 2025, s41551-025-01412-w); MULTI Consortium (Nat Med 2026, s41591-025-03999-8); NeuroSTORM (Nat Biomed Eng 2026, s41551-026-01666-y); Brain-JEPA (NeurIPS 2024, arXiv 2409.19407); BrainGFM (ICLR 2026, arXiv 2506.02044); DeCoDE (bioRxiv 2025.10.13.682243); AlphaGenome (Nature 2026, bioRxiv 2025.06.25.661532); Evo 2 (Nature 2026, arXiv 2502.18638); Caduceus (ICML 2024, arXiv 2403.03234); VAE-PRS (HGG Adv 2025); Geneformer (Nature 2023); scFoundation (NSR 2024); MultiVI (Nat Methods 2023, s41592-023-01909-9); MIDAS (PMC11471558); MoPoE-VAE (ICLR 2022, arXiv 2105.02449); COMICAL (medRxiv 2024.11.02.24316653); 4M (NeurIPS 2023, arXiv 2312.06647); Foresight (Lancet Digit Health 2024); Grotzinger 5-factor/14-disorder (Nature 2025, s41586-025-09820-3).
