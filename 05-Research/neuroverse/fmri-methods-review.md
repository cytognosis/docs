> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: researchers, stakeholders
> **Tags**: `research`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

> **Status:** Active · **Date:** 2026-05-01 (authored), 2026-07-01 (canonicalized) · **Author:** Cytognosis Foundation
> **Canonical home:** `05-Research/neuroverse/fmri-methods-review.md` · **Consolidated from:** `Science and Platform/resources/fMRI_papers_review_2026.docx` (converted to Markdown; the .docx was a render).

**Review of Five 2025–2026 fMRI / Foundation-Model Papers**

Datasets, preprocessing pipelines, atlases, code, and FAIR/open-science
assessment

with recommendations for a cross-cohort, cross-study Cytognosis fMRI
pipeline

Prepared for Shahin Mohammadi, Cytognosis Foundation

01 May 2026

**1. Executive summary**

Five papers were reviewed. One (Taylor et al., HCP/lifespan) is a
normative atlas of functional-connectivity gradients built from five
public lifespan cohorts; it does not train a foundation model but is the
most polished example in the set of how to harmonise fMRI across cohorts
spanning 16 days to 100 years. The other four train transformer-based
fMRI foundation models pretrained on tens of thousands of scans drawn
from a small overlapping pool of public datasets (UK Biobank, ABCD, HCP,
AOMIC, ABIDE, ADHD-200, etc.).

Across the five papers, three pipelines dominate preprocessing: the HCP
minimal preprocessing pipeline, fMRIPrep, and FSL-based custom pipelines
(mcflirt + topup + ICA-AROMA / ICA-FIX). Two parcellation systems
dominate the ROI-based foundation models: Schaefer-400 + Tian-III
subcortical + Buckner-7 cerebellum (giving ~450–457 ROIs), with Yeo-7
networks used for tokenisation. The two newest atlas-free models
(SLIM-Brain, Omni-fMRI) avoid parcellations entirely and operate on 4D
voxel volumes resampled to 2 mm isotropic / 96×96×96 / TR ≈ 0.72–0.8 s.
NeuroSTORM sits in between, using 2 mm MNI152 voxel volumes.

All five papers rely entirely on openly available datasets, but only two
release pretrained weights and code under permissive licences
(NeuroSTORM, Brain-Semantoks). None publish the preprocessed pretraining
derivatives in a FAIR-compliant form (BIDS-Derivatives + DataLad +
persistent DOIs). For a cross-cohort Cytognosis dataset that is intended
to be both FAIR-shareable and ready for large-scale model pretraining,
the recommended target standard is therefore: BIDS raw + fMRIPrep /
ABCD-HCP / HCP-MPP derivatives in BIDS-Derivatives → harmonised
parcellated time series in NetCDF/Zarr → atlas-free 4D Zarr volumes at 2
mm / 0.72 s. The detailed argument is in §8.

**2. Side-by-side comparison**

The table below compresses the per-paper detail. Subsequent sections
expand each row.

| **Paper** | **Type** | **Pretraining N (sessions / participants)** | **Atlas / resolution** | **Pipeline** | **Code / weights** |
|----|----|----|----|----|----|
| HCP (Taylor 2026) | Lifespan FC-gradient atlas (no foundation model) | 3 972 gradient sets / 3 556 individuals across BCP, HCP-D, HCP-YA, HCP-A, HBN | Vertex-wise on cortical surface; Schaefer-7/400 for analysis | Custom HCP-style: FSL mcflirt + topup + BBR + ICA-AROMA; ANTs; Spherical Demons | Open access (CC-BY 4.0); code in Methods/Supp. |
| NeuroSTORM (Wang 2026) | 4D voxel foundation model (Mamba/Swin) | ≈ 28.65 M frames / \> 50 000 participants. Pretrain: UKB 40 842 + ABCD 9 449 + HCP-YA 1 206 + HCP-A 725 + HCP-D 652 | Atlas-free 2 mm MNI152, 96×96×96 volumes, TR 0.8 s | Per-dataset: HCP minimal pipeline, ABCD-HCP, fMRIPrep, ICA-FIX (TCP); aligned to MNI152 + Z-norm | GitHub + pretrained weights (open) |
| Brain-Semantoks (Gijsen 2025) | Self-distilled foundation model with semantic tokeniser | 39 139 UKB rs-fMRI recordings (1 625 held out for downstream) | Schaefer-400 cortical + Tian-III subcortical + Buckner-7 cerebellar = 457 ROIs; Yeo-7 networks for tokeniser | Standard rs-fMRI conventions: 0.01–0.1 Hz bandpass, per-ROI z-score, 2 s temporal resampling | GitHub + weights (open) |
| SLIM-Brain (Wang 2026) | Atlas-free Hiera-JEPA foundation model with key-frame selection | ≈ 4 129 sessions across HCP, CHCP, AOMIC PIOP1+PIOP2, ABCD | Atlas-free 4D voxels at 2 mm isotropic, 96×96×96, TR 0.72 s | HCP / CHCP → HCP-MPP; ABCD → ABCD-HCP; AOMIC → fMRIPrep; ABIDE/ADHD → PCP | Code link in paper |
| Omni-fMRI (Wang 2026) | Atlas-free foundation model with dynamic patch tokenisation | 49 497 sessions / ~ 49 k participants across UKB, AOMIC PIOP1+PIOP2, CHCP, ISYB, ABCD, ABIDE, HCP rest, PPMI | Atlas-free 4D voxels at 2 mm isotropic, 96×96×96, TR 0.72 s, global Z-score | Per-dataset standard (HCP-MPP, fMRIPrep, PCP); resampling + Z-scoring uniform across cohorts | Code link in paper |

**3. Paper-by-paper detail**

**3.1 Taylor et al., "Functional hierarchy of the human neocortex across
the lifespan" (Nature, 2026)**

Citation: Taylor HP IV, Huynh KM, Thung K-H, Lin G, Lyu W, Lin W, Ahmad
S, Yap P-T. Functional hierarchy of the human neocortex across the
lifespan. Nature 652, 955–963 (23 April 2026). DOI:
10.1038/s41586-026-10219-x. Open access, CC-BY 4.0.

This is **not** a foundation-model paper. It builds a continuous
normative reference of three principal FC gradients (sensory–association
SA; visual–somatosensory VS; modulation–representation MR) from infancy
to age 100 by harmonising five public lifespan cohorts and modelling
vertex-wise gradient values with generalised additive mixed models
(GAMMs).

**Datasets (only those used in the analysis)**

| **Cohort** | **Age range** | **Initial N** | **Final N (after QC)** |
|----|----|----|----|
| BCP — Baby Connectome Project | 16 days – 5 years | 652 / 1 095 timepoints | 343 / 759 timepoints |
| HCP-D — HCP Development | 5.6 – 21.9 years | 650 / 1 226 | 650 / 1 206 |
| HCP-YA — HCP Young Adult | 22 – 37 years | 1 206 | 1 068 |
| HCP-A — HCP Aging | 36 – 100 years | 725 | 725 |
| HBN — Healthy Brain Network | 5.6 – 21.9 years | 772 | 770 |
| TOTAL | 0.04 – 100 years | — | 3 556 individuals / 3 972 gradient sets |

**Preprocessing tools and standards**

- rs-fMRI: HCP-style pipeline using FSL — mcflirt (motion correction),
  topup (EPI/distortion correction with reverse phase-encoded SBRefs),
  BBR (boundary-based registration), ICA-AROMA-style 150-component ICA
  denoising, head-motion + edge + CSF correlation classification,
  aggressive regression-out, 0.001 Hz high-pass.

- Structural: automated QA, inhomogeneity correction, T2w→T1w linear
  transformation, automated tissue segmentation; ANTs symmetric
  normalisation; deep-learning-based diffusion QC, manual visual
  inspection.

- Surface: cortical surface registered to age-matched cortical surface
  atlases extended from a previous lifespan template; Spherical Demons
  for sphere-to-sphere registration; one-to-one mapping to a 20
  484-vertex standard surface (18 644 excluding medial wall).

- Microstructure: Spherical Mean Spectrum Imaging (SMSI), DTI-derived
  FA/MD.

**Atlases / parcellations**

- Vertex-wise (no parcellation) for the gradient computation.

- Schaefer-7 networks for network-level summaries; Schaefer-400 for the
  Neurosynth meta-analytic validation.

- Allen Human Brain Atlas (AHBA), processed with the abagen toolbox for
  transcriptomic enrichment analysis.

**Code, formats, openness**

- All five datasets used are openly available (BCP, HCP-D, HCP-YA,
  HCP-A, HBN — all distributed under standard NIMH/NIH data-use
  agreements).

- Outputs: vertex-wise gradient maps, GAMM coefficients.

- FAIR compliance: high for upstream data (all DUA-controlled but open),
  modest for derivatives (no public deposit of the harmonised gradient
  sets at time of writing). No public GitHub repository link is given in
  the main text but the paper is open access (CC-BY 4.0) so derivatives
  can be reproduced from Methods.

**3.2 Wang et al., "Towards a general-purpose foundation model for
functional MRI analysis" — NeuroSTORM (Nature Biomedical Engineering, 23
April 2026)**

Citation: Wang C, Jiang Y, Peng Z, Li C, Bang C-B, Zhao L, Lv J,
Sepulcre J, Yang C, He L, et al. Towards a general-purpose foundation
model for fMRI analysis. Nature Biomedical Engineering (2026). DOI:
10.1038/s41551-026-01666-y.

Code & weights:
[<u>https://github.com/CUHK-AIM-Group/NeuroSTORM</u>](https://github.com/CUHK-AIM-Group/NeuroSTORM)
/ homepage
[<u>https://cuhk-aim-group.github.io/NeuroSTORM/</u>](https://cuhk-aim-group.github.io/NeuroSTORM/).

**Pretraining datasets (Corpus A) — 28.65 M frames, \> 50 000
participants**

| **Cohort** | **N participants** | **TR (s)** | **Spatial resolution** | **Notes** |
|----|----|----|----|----|
| UK Biobank (UKB) | 40 842 | 0.735 | 2.4 × 2.4 × 2.4 mm | Largest single contribution to pretraining |
| ABCD | 9 449 (children) | 0.8 | 2.4 × 2.4 × 2.4 mm | 9–10 yo children, multi-site |
| HCP-YA | 1 206 | 0.72 | 2 × 2 × 2 mm | HCP minimal pipeline |
| HCP-A | 725 | 0.8 | 2 × 2 × 2 mm | HCP-Aging |
| HCP-D | 652 | 0.8 | 2 × 2 × 2 mm | HCP-Development |

**Downstream-only datasets (Corpus B)**

- HCP-EP (early psychosis, n = 173), ADHD200 (n = 973), COBRE
  (schizophrenia, n = 173), UCLA (n = 272), MND (motor neuron disease, n
  = 59), TCP (Transdiagnostic Connectome Project, Yale/McLean, n = 245),
  DMT-HAR-MED (DMT-harmine vs. placebo, n = 40).

**Preprocessing & format**

- All datasets standardised to MNI152, 96 × 96 × 96 voxels, 2 × 2 × 2
  mm, TR 0.8 s. Per-volume Z-normalisation.

- Per-dataset upstream pipelines (per Methods): ADHD200 and HCP-EP go
  through standard ROI-extraction-friendly preprocessing (motion
  correction, MNI normalisation, artefact removal); the TCP dataset uses
  the HCP pipelines including ICA-FIX denoising and global signal
  regression.

- Atlases used by the ROI-based baselines (not by NeuroSTORM itself,
  which is volumetric): AAL3, CC200, Harvard-Oxford, Desikan–Killiany;
  Schaefer for some baselines.

- Software stack disclosed in the Reporting Summary: Python 3.10, torch
  2.1.0, pytorch-lightning 1.9.4, monai 1.3.0, nibabel 5.3.2, nilearn
  0.12.1, FSL 6.0.7.17, mamba-ssm 2.2.2, numpy 1.22.4, scikit-learn
  1.7.2, scipy 1.13.1.

**Architecture & training**

- Backbone: shifted-window Mamba (SWM), hierarchical, 4 stages.

- Pretraining objective: masked autoencoding (MAE) with a Spatiotemporal
  Redundancy Dropout (STRD) module that drops voxels with high
  spatial/temporal matching probability.

- Fine-tuning via Task-specific Prompt Tuning (TPT): freezes the
  backbone, trains \< 5 % of parameters.

- Compute: 4 × A6000 (48 GB) for ~ 13 days, 30 epochs, batch 4 × 8.

**FAIR / openness**

- All pretraining and downstream datasets are publicly listed (UKB,
  ABCD, HCP, ADHD200, ABIDE, UCLA, COBRE, HBN, TCP via OpenNeuro
  ds006644, MND via OpenNeuro ds005237, DMT-HAR-MED via OpenNeuro
  ds005874).

- Code is on GitHub; weights are released; Python dependencies pinned.
  Strong on Findability, Accessibility, Reusability; less explicit about
  Interoperability (no BIDS-Derivatives manifest of the preprocessed
  corpus).

**3.3 Gijsen, Schulz & Ritter, "Brain-Semantoks: Learning Semantic
Tokens of Brain Dynamics with a Self-Distilled Foundation Model"
(arXiv:2512.11582, 12 December 2025)**

Code & weights:
[<u>https://github.com/SamGijsen/Brain-Semantoks</u>](https://github.com/SamGijsen/Brain-Semantoks).

**Pretraining dataset**

- UK Biobank (Miller et al., 2016) rs-fMRI — 39 139 preprocessed
  recordings (UKB application 25163). 1 625 recordings held out for
  downstream demographic prediction within UKB.

**Downstream datasets**

- SRPBS (Tanaka et al., 2021) — multi-site, multi-disorder Japanese
  rs-fMRI: SCZ vs. controls (n=291), MDD vs. controls (n=499).

- ABIDE (Di Martino et al., 2014) — autism (n=974).

- HBN — Healthy Brain Network (Alexander et al., 2017) — paediatric
  mental-health: WISC-FSIQ cognition, CELF language, age, sex (n up to 1
  870).

- LEMON (Babayan et al., 2019) — CVLT verbal learning, TMT, MDBF mood (n
  ≈ 212).

- ADHD200 (preprocessed via Bellec et al., 2017).

**Atlases & preprocessing**

- Cortex: Schaefer-400 (Schaefer et al., 2018).

- Subcortex: Tian-III (Tian et al., 2020).

- Cerebellum: Buckner-7 (Buckner et al., 2011).

- Total: 457 ROIs.

- Tokeniser uses the Yeo 7-network functional parcellation (Yeo et
  al., 2011) extended with 2 additional networks for subcortex and
  cerebellum → 9 networks.

- Standard rs-fMRI conventions: 0.01–0.1 Hz band-pass; per-ROI per-scan
  z-scoring (avoids ROI-specific DC offsets that hurt transferability
  when scanners differ); temporal downsampling to 2 s for the 6-minute
  UKB recordings (UKB native TR = 0.735 s).

- Time-series standardisation across cohorts requires only z-scoring +
  resampling to 2 s — light operations performable online during data
  loading. This is what makes the model genuinely cross-dataset.

- Atlas-ablation results (Appendix Table 10) show the model is
  reasonably robust to the parcellation choice — Gordon-333 substituting
  for Schaefer-400 gives only −0.91 % balanced-accuracy drop on average.

**Architecture & training**

- Self-distillation à la DINO/iBOT, with two long temporal views (T_crop
  = 100), light corruption augmentations (channel zeroing, Gaussian
  noise, amplitude scaling).

- Semantic tokeniser: per-network multi-scale convolutional filter bank
  → temporal patches of length 20.

- Three-loss training objective with a Teacher-guided Temporal
  Regulariser (TTR) that constrains the token space toward the
  time-averaged network signature for the first 5 % of training.

- Compute: \< 2 hours, 1 GPU, \< 20 GB memory — by far the most
  compute-efficient of the four foundation models.

**FAIR / openness**

- Code and pretrained weights both released under permissive licence on
  GitHub. Dataset access is via the standard UKB / SRPBS / ABIDE / HBN /
  LEMON / ADHD200 application paths — all open-access in principle but
  with controlled-access metadata for clinical cohorts.

**3.4 Wang et al., "SLIM-Brain: A Data- and Training-Efficient
Foundation Model for fMRI Data Analysis" (arXiv:2512.21881v3, 30 January
2026)**

Code link is given in the paper but is shielded by an arXiv-anonymised
"link" placeholder; release was promised on acceptance.

**Pretraining datasets — only ~ 4 129 sessions (deliberately small)**

| **Cohort** | **Pipeline used** | **Notes** |
|----|----|----|
| HCP — Van Essen 2013 | HCP minimal preprocessing pipeline (Glasser 2013) | 606 participants used |
| CHCP — Chinese HCP, Ge 2023 | HCP minimal preprocessing pipeline | Demographic diversity contribution |
| AOMIC PIOP1 + PIOP2 — Snoek 2021 | fMRIPrep (Esteban 2019) | Amsterdam Open MRI Collection |
| ABCD — Casey 2018 | ABCD-HCP pipeline | 70 % used for pretraining |
| TOTAL | Mixed | ≈ 4 129 sessions (vs. 64 584 for BrainMass, 32 k for Brain-JEPA, 50 k for NeuroSTORM) |

**Downstream / external-validation datasets**

- ABIDE (autism), ADHD-200, ADNI (Jack 2008 — Alzheimer's MCI/AD), PPMI
  (Marek 2011 — Parkinson's). Preprocessed ABIDE and ADHD-200 came from
  the Preprocessed Connectomes Project (PCP, Craddock 2013; Bellec
  2017).

**Format & uniformisation**

- All images resampled to 2 mm isotropic via cubic B-spline
  interpolation, then padded/cropped to (96, 96, 96).

- Datasets with lower temporal resolution interpolated to a uniform 0.72
  s TR (cubic B-spline). HCP, CHCP, ABCD natively meet 0.72 s.

- Atlas-free voxel-level — no ROI extraction in the model itself.

**Architecture**

- Two-stage adaptive pipeline: (1) lightweight ViT MAE on full sequences
  scores 5-frame windows by mutual masked reconstruction; (2) a
  Hiera-JEPA encoder processes only the top-k informative windows at
  voxel resolution.

- Compute: 1 × A100 (80 GB), ~ 20 hours, 40 epochs, 4 k sessions. ~ 30 %
  of the GPU memory of Swin-based 4D models.

**FAIR / openness**

- All pretraining and downstream datasets are publicly available; code
  release was at preprint anonymisation stage.

- This paper is the strongest argument that the bottleneck for fMRI
  foundation models is not necessarily data scale but training
  efficiency.

**3.5 Wang et al., "Omni-fMRI: A Universal Atlas-Free fMRI Foundation
Model" (arXiv:2601.23090v1, 30 January / 2 February 2026)**

Same lead lab as SLIM-Brain (Quanying Liu, SUSTech). Code & logs
released — link given in paper as "Link" placeholder; standardised
dataset splits and exact test-subject IDs are released alongside the
code.

**Pretraining datasets — 49 497 sessions across 9 cohorts**

| **ID** | **Cohort** | **Participants** | **Sessions** | **Age range** |
|----|----|----|----|----|
| 1 | UK Biobank (Sudlow 2015) | 38 301 | 38 372 | 68.4 ± 7.5 |
| 2 | AOMIC PIOP1 (Snoek 2021) | 168 | 672 | 22.1 ± 1.8 |
| 3 | AOMIC PIOP2 (Snoek 2021) | 180 | 720 | 22.0 ± 1.8 |
| 4 | CHCP (Ge 2023) | 244 | 1 224 | 18–79 |
| 5 | ISYB — Imaging Chinese Young Brains (Gao 2022) | 130 | 520 | 22.5 ± 2.6 |
| 6 | ABCD (Casey 2018) — 70 % | 1 680 | 6 720 | 9.93 ± 0.63 |
| 7 | ABIDE (Di Martino 2014) | 609 | 2 436 | 6–58 |
| 8 | HCP rest (Van Essen 2013) | 606 | 2 424 | 28.8 ± 3.5 |
| 9 | PPMI (Marek 2011) | 331 | 1 324 | 35–84 |
| TOTAL | — | ≈ 42 250 | ≈ 54 412 sessions (Type I + II) | — |

**Downstream-only datasets**

- ADNI (497 / 1 988 sessions, 55–90 yo), SALD (Wei 2017, 493 subjects,
  age regression), BHRC (Brazilian High-Risk Cohort, 465 subjects, sex
  classification — accessed via the Reproducible Brain Corpus / RBC,
  Shafiei 2025), NKI (Telesford 2023, 717 subjects, age + education,
  also via RBC), NSD (Allen 2021, 6 subjects, 70 566 sessions, image
  retrieval), HCP task (118 / 1 647 sessions, 23-way state
  classification), StudyForrest (Hanke 2016, 20 subjects, 71 980 task
  volumes, emotion prediction).

**Format**

- All resampled to 2 mm isotropic, padded/cropped to 96×96×96, temporal
  resampling to 0.72 s TR (cubic B-spline), global Z-scoring at the
  voxel level.

- Atlas-free, but uses dynamic content-adaptive patch tokenisation:
  low-complexity regions get coarse 8³ patches; high-variance regions
  get recursively subdivided to 4³ sub-patches; \> 50 % of the volume
  that is background is discarded.

**Architecture**

- Standard ViT encoder + MAE objective, made tractable by the dynamic
  patch reduction (token count drops from ~14 K to ~4.3 K).

- Compute: 4 × A10G (24 GB), 35 epochs, ~ 32 hours.

**FAIR / openness**

- Strongest commitment to reproducibility of the four foundation-model
  papers: full experiment logs and exact test-subject IDs are released;
  standardised dataset splits in the public code repo. All datasets are
  public; BHRC and NKI are routed through the Reproducible Brain Corpus,
  which is itself a BIDS-Derivatives compliant resource.

**4. Cross-paper synthesis**

**4.1 Convergence on a small pool of public datasets**

Across the four foundation-model papers, the same datasets recur. UKB is
in 3/4. ABCD, HCP, AOMIC are each in 2/4. ABIDE, ADHD-200, ADNI, PPMI
are each used as either pretraining or downstream in 3/4.

| **Dataset** | **NeuroSTORM** | **Brain-Semantoks** | **SLIM-Brain** | **Omni-fMRI** | **HCP/Taylor** |
|----|----|----|----|----|----|
| UK Biobank | Pretrain (40 842) | Pretrain (39 139) | — | Pretrain (38 372) | — |
| ABCD | Pretrain (9 449) | — | Pretrain (subset) | Pretrain (6 720) | — |
| HCP-YA / HCP rest | Pretrain (1 206) | — | Pretrain (606) | Pretrain (2 424) | Used (1 068 final) |
| HCP-D / HCP-A | Pretrain | — | — | — | Used |
| HCP-EP | Downstream | — | — | — | — |
| AOMIC PIOP1+PIOP2 | — | — | Pretrain | Pretrain (672+720) | — |
| CHCP | — | — | Pretrain | Pretrain (1 224) | — |
| ISYB | — | — | — | Pretrain (520) | — |
| ABIDE | — | Downstream | Downstream | Pretrain + downstream | — |
| ADHD-200 | Downstream | Downstream | Downstream | — | — |
| ADNI | — | — | Downstream | Downstream | — |
| PPMI | — | — | Downstream | Pretrain + downstream | — |
| BCP | — | — | — | — | Used |
| HBN | — | Downstream | — | — | Used (770) |
| LEMON | — | Downstream | — | — | — |
| SRPBS | — | Downstream | — | — | — |
| TCP (Yale/McLean) | Downstream | — | — | — | — |
| NSD | — | — | — | Downstream | — |
| StudyForrest | — | — | — | Downstream | — |
| NKI / BHRC (via RBC) | — | — | — | Downstream | — |

**4.2 Convergence on three preprocessing pipelines**

- **HCP minimal preprocessing pipeline** (Glasser et al., 2013;
  Neuroimage 80:105–124) — used by NeuroSTORM (HCP family), SLIM-Brain
  (HCP, CHCP), Omni-fMRI (HCP), Taylor (rs-fMRI pipeline is HCP-style).
  Open source:
  [<u>https://github.com/Washington-University/HCPpipelines</u>](https://github.com/Washington-University/HCPpipelines)

- **ABCD-HCP pipeline** — used by NeuroSTORM and SLIM-Brain for ABCD.
  Built on top of HCP-MPP. Open source:
  [<u>https://github.com/DCAN-Labs/abcd-hcp-pipeline</u>](https://github.com/DCAN-Labs/abcd-hcp-pipeline)

- **fMRIPrep** (Esteban et al., 2019; Nature Methods 16:111–116) — used
  by SLIM-Brain (AOMIC), Omni-fMRI (AOMIC, others). BIDS-Apps native,
  the de-facto FAIR-compatible community standard. Open source:
  [<u>https://github.com/nipreps/fmriprep</u>](https://github.com/nipreps/fmriprep)

- **Preprocessed Connectomes Project (PCP) / Configurable Pipeline for
  the Analysis of Connectomes (C-PAC)** — pre-processed ABIDE, ADHD-200
  derivatives used by Brain-Semantoks, SLIM-Brain. References: Craddock
  2013; Bellec 2017.
  [<u>https://github.com/FCP-INDI/C-PAC</u>](https://github.com/FCP-INDI/C-PAC)

- **FSL** (mcflirt, topup, BBR) and **ICA-AROMA / ICA-FIX** for
  motion-/artefact-component classification — appear in all five papers
  either directly or transitively through HCP-MPP. FSL:
  [<u>https://fsl.fmrib.ox.ac.uk/</u>](https://fsl.fmrib.ox.ac.uk/);
  ICA-AROMA:
  [<u>https://github.com/maartenmennes/ICA-AROMA</u>](https://github.com/maartenmennes/ICA-AROMA).

- **Reproducible Brain Corpus (RBC)** (Shafiei et al., 2025) — the
  formal route by which Omni-fMRI accessed BHRC and NKI. RBC is
  BIDS-Derivatives compliant, harmonised across cohorts with a single
  QSIPrep + fMRIPrep version, and is the most FAIR resource cited in the
  entire set of papers.

**4.3 Convergence on three atlas/parcellation systems**

- **Schaefer-400** (Schaefer et al., 2018; Cerebral Cortex 28:3095–3114)
  — used by Brain-Semantoks (cortex), Brain-JEPA, BrainMass with
  Schaefer-100.
  [<u>https://github.com/ThomasYeoLab/CBIG/tree/master/stable_projects/brain_parcellation/Schaefer2018_LocalGlobal</u>](Schaefer2018_LocalGlobal repo)

- **Tian-III subcortical** (Tian et al., 2020; Nature Neuroscience
  23:1421–1432) — used by Brain-Semantoks, Brain-JEPA.
  [<u>https://github.com/yetianmed/subcortex</u>](https://github.com/yetianmed/subcortex)

- **Buckner-7 cerebellar** (Buckner et al., 2011; J. Neurophysiology
  106:2322–2345) — used by Brain-Semantoks.

- **Yeo 7-network** (Yeo et al., 2011) — used by Brain-Semantoks for
  tokenisation, by Taylor for network-level summaries via Schaefer-7.

- Used as ROI baselines (not by the foundation models themselves): AAL3
  (Rolls 2020), CC200 (Craddock 2012), Harvard-Oxford (Desikan 2006),
  Desikan–Killiany, Gordon-333 (Gordon 2016).

**4.4 Convergence on a target spatio-temporal resolution**

Three of the four foundation-model papers (NeuroSTORM, SLIM-Brain,
Omni-fMRI) converge on the same target volumetric format: 96 × 96 × 96
voxels at 2 mm isotropic, MNI152 space, TR 0.72–0.8 s, with cubic
B-spline temporal resampling. Brain-Semantoks resamples to TR = 2 s on
parcellated time series. Brain-Semantoks ablation (Appendix Table 11)
shows that downsampling UKB from native 0.735 s to 2 s loses ≈ 1.2 %
balanced accuracy on average across 10 downstream tasks, mostly hurting
cognitive prediction in LEMON. The 96³ × 0.72 s standard is therefore a
sensible target if voxel-level model training is in scope; 2 s is
acceptable for parcellated training.

**5. Tools landscape — what is open and FAIR-aligned**

| **Tool / standard** | **What it does** | **Open licence** | **Used by** |
|----|----|----|----|
| BIDS / BIDS-Derivatives | Filesystem standard for raw and derived neuroimaging data; community-maintained, OpenNeuro-native | CC-BY (spec); various (tools) | OpenNeuro, fMRIPrep, RBC — implicit standard for all five papers' upstream data |
| fMRIPrep | BIDS-App preprocessing pipeline (FSL+ANTs+FreeSurfer+AFNI) | Apache 2.0 | SLIM-Brain (AOMIC), Omni-fMRI |
| HCP minimal preprocessing pipeline (HCP-MPP) | Reference HCP rs/tfMRI pipeline (FSL+FreeSurfer+Connectome Workbench) | BSD-3 | All four foundation models, Taylor |
| ABCD-HCP pipeline (DCAN) | ABCD-specific HCP-MPP fork | BSD-3 | NeuroSTORM, SLIM-Brain, Omni-fMRI |
| C-PAC / PCP | Configurable Connectomes pipeline; produces ABIDE, ADHD-200 derivatives | BSD-3 | Brain-Semantoks, SLIM-Brain |
| FSL (mcflirt, topup, BBR, MELODIC, ICA-AROMA, ICA-FIX, FIRST) | Core motion/distortion/denoising engine | FSL licence: free for academic/non-commercial; commercial requires permission | All five papers |
| ANTs | Symmetric normalisation; structural registration | BSD-3 | Taylor; transitively via fMRIPrep / HCP-MPP |
| FreeSurfer | Cortical surface reconstruction & vertex-wise resampling | Free for non-commercial research | Transitively via HCP-MPP and fMRIPrep |
| Connectome Workbench | Surface analysis, GIFTI/CIFTI handling | GPL-2.0 | Transitively via HCP-MPP |
| Spherical Demons | Spherical surface registration | GPL-2.0 | Taylor |
| BrainSpace | Diffusion-map embedding for FC gradients | BSD-3 | Taylor |
| abagen | AHBA gene-expression workflow | BSD-3 | Taylor |
| Neurosynth / NiMARE | Meta-analytic term maps | MIT | Taylor, SLIM-Brain (interpretability) |
| nilearn / nibabel / MONAI | Python neuroimaging I/O and ML | BSD-3 / MIT / Apache 2.0 | All four foundation models |
| Schaefer 2018, Tian-III, Buckner-7, Yeo-7 atlases | Cortical / subcortical / cerebellar / network parcellations | Public; CC-BY / academic | Brain-Semantoks, Taylor, baselines |
| Reproducible Brain Corpus (RBC) | Harmonised multi-cohort BIDS-Derivatives release with QSIPrep+fMRIPrep | Open-access (CC-BY for derivatives, DUA for raw) | Omni-fMRI |
| DataLad | Git-annex-based dataset versioning; FAIR distribution layer | MIT | Not explicitly used by any of the five but is the missing link in their FAIR stories |
| OpenNeuro | BIDS-native public repository | Open access (CC0 default) | Hosts TCP, MND, DMT-HAR-MED used by NeuroSTORM |

**6. How FAIR-aligned are these papers in practice?**

The acronym is Findable, Accessible, Interoperable, Reusable. Scoring
each paper on the dimension that the paper authors actually controlled
(i.e. their derived corpus, code, and pretrained weights) gives:

| **Paper** | **F (Findable)** | **A (Accessible)** | **I (Interoperable)** | **R (Reusable)** | **Comment** |
|----|----|----|----|----|----|
| Taylor (HCP) | High — DOI, Nature open access | High — CC-BY | Medium — vertex-wise outputs in standard surface space, but no public BIDS-Derivatives deposit | Medium — code described in Methods, no public repo link in the main text | Best for transparency of methods; weakest for executable reproducibility |
| NeuroSTORM | High — DOI, GitHub, named release | High — code + weights public | Medium — uses MNI152 + standard NIfTI-likes but does not publish BIDS-Derivatives manifest of pretraining corpus | High — pinned dep versions, fine-tuning recipes, prompt-tuning code | Strongest of the four foundation models on R |
| Brain-Semantoks | High — arXiv + GitHub | High — code + weights public | Medium — parcellated time series in NumPy format; not a BIDS-Derivatives manifest | High — \< 2 hours on 1 GPU; trivially reproducible end-to-end | Best on training reproducibility (lowest compute) |
| SLIM-Brain | Medium — arXiv only; code link anonymised at submission | Medium — promised at acceptance | Medium | Medium | Good methodology; release was pending |
| Omni-fMRI | High — arXiv + code + logs + exact subject IDs | High — code + experiment logs public | Medium-High — uses RBC, BIDS-Derivatives compliant, for two of its downstream cohorts | High — splits and IDs released for fair benchmarking | Best on benchmarking transparency |

None of the four foundation-model papers publish their preprocessed
pretraining corpus as a BIDS-Derivatives release with persistent DOIs
and DataLad versioning. This is the single biggest gap in the field —
they all treat the corpus as a private intermediate artefact, even when
the upstream data is fully open. Two open community efforts are partial
solutions to this gap: the Preprocessed Connectomes Project
(Bellec/Craddock — for ABIDE, ADHD-200, etc.) and the Reproducible Brain
Corpus (Shafiei 2025 — Omni-fMRI uses it for NKI and BHRC). Both are
good models for what a Cytognosis cross-cohort dataset should look like.

**7. Recommendations for the Cytognosis cross-cohort, cross-study fMRI
dataset**

The recommended pipeline below is opinionated. It is composed entirely
of openly licensed components, is the path of least resistance toward
FAIR compliance, and produces derivatives that match the de-facto input
format of the strongest foundation models reviewed here, so future model
pretraining or fine-tuning stays trivial.

**7.1 Storage layer — BIDS at every level**

- **Raw data:** BIDS v1.10+ filesystem layout with NIfTI / NIfTI.gz
  volumes and JSON sidecars. Field-map and reverse-PE acquisitions named
  to BIDS conventions so fMRIPrep and HCP-MPP can run unattended. Use
  [<u>dcm2niix</u>](https://github.com/rordenlab/dcm2niix) +
  [<u>HeuDiConv</u>](https://github.com/nipy/heudiconv) or [<u>Curation
  Bidsify (CuBIDS)</u>](https://github.com/PennLINC/CuBIDS) for batch
  DICOM → BIDS conversion and validation.

- **Derived data:** BIDS-Derivatives — separate subfolders for each
  pipeline (fmriprep/, hcp-mpp/, abcd-hcp/, etc.), each with a
  dataset_description.json pointing to the raw dataset's DOI. This is
  the single discipline that turns scattered preprocessing into
  something FAIR.

- **Versioning:** DataLad (git-annex) for both raw and derived. Each
  cohort sub-dataset is independently versioned and citable; the parent
  dataset is a flat list of sub-dataset pointers. Persistent DOIs via
  Zenodo for tagged releases.

**7.2 Preprocessing — converge on three pipelines, no more**

The literature recommends matching the pipeline to the cohort, not
running everything through one universal pipeline. Concretely:

- **HCP-family cohorts (HCP-YA, HCP-A, HCP-D, CHCP, BCP, HBN if
  HCP-formatted):** HCP minimal preprocessing pipeline. Containerised
  via the official Singularity image. Output: CIFTI grayordinate time
  series in MNINonLinear/Results, ICA-FIX-cleaned dtseries.

- **ABCD:** ABCD-HCP pipeline (DCAN). Same output format as HCP-MPP.

- **Everything else (typical research/clinical cohorts in BIDS):**
  fMRIPrep with consistent settings: --output-spaces
  MNI152NLin6Asym:res-2 fsLR:den-91k, --use-aroma (or --use-syn-sdc when
  fieldmaps absent), --bold2t1w-dof 9.

- **Denoising:** ICA-FIX where the cohort has a trained classifier,
  ICA-AROMA otherwise. Always emit a confound TSV; do not regress
  confounds at the BIDS-Derivatives layer — leave that as an
  analysis-time decision so different downstream consumers can choose.

- **Quality control:** MRIQC reports for raw; fMRIPrep visual reports +
  MRIQC group reports for derivatives. Centralise QC labels (good /
  questionable / fail) in a single TSV at the dataset root, propagated
  as BIDS-Derivatives sidecars.

- **Provenance:** Container hash (Docker/Singularity SHA256) and
  pipeline version stamped in every sidecar. Best practice: mirror what
  RBC does.

**7.3 Parcellation & atlas layer — emit two things, always**

- **Voxel-level 4D arrays,** MNI152 NLin6Asym 2 mm, padded/cropped to a
  uniform 96×96×96 grid, temporally resampled to TR = 0.72 s with cubic
  B-spline interpolation, voxel intensity Z-scored across the time
  series. This is exactly the input format that NeuroSTORM, SLIM-Brain
  and Omni-fMRI consume, so the dataset is ready for atlas-free model
  training without a second pass.

- **Parcellated time series** on the canonical Schaefer-400 (cortex) +
  Tian-III (subcortex) + Buckner-7 (cerebellum) = 457-ROI scheme used by
  Brain-Semantoks. Emit the network membership (Yeo-7 + 2 supplementary
  networks for subcortex/cerebellum) as a sidecar JSON. Per-ROI per-scan
  z-scoring as the baseline normalisation. Optionally emit Schaefer-100
  and AAL3 alongside for compatibility with BrainMass / SwiFT-style
  baselines.

- **Do not pick one parcellation and discard the others.** The cost of
  emitting two or three parcellations is trivial compared to the cost of
  re-running preprocessing.

**7.4 Container format — Zarr v3, not raw NIfTI, for the model-training
tier**

- **4D voxel volumes:** Zarr v3 (or HDF5 with chunked I/O). Chunks of
  (T_chunk, 96, 96, 96), e.g., 32 frames × 96³, compressed with
  Blosc-zstd. Avoids the per-file overhead of NIfTI.gz when batches of
  subjects are loaded into a DataLoader.

- **Parcellated time series:** Parquet (Arrow) or NetCDF-4 with one row
  per (subject, session, run, ROI, timepoint). Cleanly indexed by
  cohort/site/scanner/age/diagnosis covariates.

- **Stay tool-compatible:** Always keep a NIfTI/CIFTI export script. The
  Zarr/Parquet tier is for training scale; the NIfTI tier is for human
  inspection and traditional toolchains.

**7.5 Harmonisation across cohorts — apply at use time, not at storage
time**

- **Site / scanner / acquisition-protocol harmonisation** (ComBat,
  NeuroComBat, longitudinal-ComBat, CovBat, or DL approaches like
  DeepCombat) should be performed at the analysis or fine-tuning layer,
  not baked into the stored derivatives. Different downstream tasks need
  different harmonisation choices, and storing a single harmonised
  version locks the dataset into a methodological choice that will age
  fast.

- **Store, do not overwrite,** the per-scan covariates needed for
  harmonisation: scanner manufacturer, model, software version, head
  coil, TR, TE, voxel size, slice timing, multiband factor,
  phase-encoding direction, AP/PA polarity, motion summary (mean FD, %
  volumes with FD \> 0.5 mm), tSNR, ICA-AROMA component count, etc.
  Treat these as first-class metadata in the BIDS-Derivatives sidecars.

- **Document scanner/site identity** with a controlled vocabulary at the
  dataset level (BIDS "InstitutionName" +
  "InstitutionalDepartmentName" + "DeviceSerialNumber") so that ComBat
  batch variables can be defined unambiguously.

**7.6 Sharing model — three tiers, one DUA**

- **Tier 1 (Open):** De-identified BIDS Derivatives + Zarr + Parquet on
  Zenodo or the European Open Science Cloud, CC-BY 4.0. Persistent DOI
  per release. This is the layer that makes the dataset findable.

- **Tier 2 (Controlled):** Defaced raw NIfTI + DICOM under a single,
  light Cytognosis Foundation DUA, mirroring the OpenNeuro/HBN pattern.
  PII never leaves the institution.

- **Tier 3 (Internal):** Restricted-access clinical metadata (genotype,
  full medical history) under existing IRB / GDPR / HIPAA frameworks.

**7.7 Compliance with Cytognosis openness policy**

- All recommended tools (fMRIPrep, HCP-MPP, ABCD-HCP, C-PAC, ANTs,
  FreeSurfer non-commercial, FSL, BIDS, DataLad, Zarr,
  Schaefer/Tian/Buckner/Yeo atlases, Neurosynth, abagen) are open-source
  under permissive or copyleft licences compatible with the openness
  skill in the Cytognosis workspace.

- FreeSurfer and FSL have non-commercial-only clauses; if a future
  Cytognosis PBC subsidiary commercialises analyses, this needs a
  re-licence step. ANTs (BSD-3), AFNI (GPL-3), Connectome Workbench
  (GPL-2), C-PAC (BSD-3) are all permissive and compatible with PBC
  distribution.

- Atlases: Schaefer-2018 is CC-BY 4.0; Tian-III, Buckner-7, Yeo-7 are
  released for academic use with citation. Treat them as Cytognosis
  dependencies — pin specific atlas versions in the dataset description.

**7.8 Concrete, executable next step**

In one sprint, a Cytognosis demonstrator dataset of (say) 1 000 subjects
across 3 cohorts can be brought to FAIR-and-foundation-model-ready state
by running, in order:

- dcm2niix → HeuDiConv → CuBIDS validate (raw → BIDS).

- fMRIPrep 24+ in a Singularity container, --output-spaces
  MNI152NLin6Asym:res-2 fsLR:den-91k, --use-aroma.

- Voxel-level resampling pass: nilearn.image.resample_to_img → 96³ × TR
  0.72 s → per-voxel Z-score → Zarr v3.

- Parcellation pass: nilearn.maskers.NiftiLabelsMasker with the
  Schaefer-400 + Tian-III + Buckner-7 combined atlas → per-ROI Z-score →
  Parquet.

- DataLad init at the dataset root, sub-dataset for each cohort.

- Mint a Zenodo DOI for the v0.1 release; CC-BY 4.0 on the Tier-1
  derivatives.

- Smoke-test fine-tuning of either NeuroSTORM (volumetric input ready)
  or Brain-Semantoks (parcellated input ready) on the demonstrator to
  confirm the format is foundation-model-ready end-to-end.

**8. Code, data, and standard pointers**

Single consolidated reference list, in the order they appeared above.

| **Resource** | **URL** |
|----|----|
| NeuroSTORM (Wang 2026) | [<u>https://github.com/CUHK-AIM-Group/NeuroSTORM</u>](https://github.com/CUHK-AIM-Group/NeuroSTORM) |
| NeuroSTORM project page | [<u>https://cuhk-aim-group.github.io/NeuroSTORM/</u>](https://cuhk-aim-group.github.io/NeuroSTORM/) |
| Brain-Semantoks (Gijsen 2025) | [<u>https://github.com/SamGijsen/Brain-Semantoks</u>](https://github.com/SamGijsen/Brain-Semantoks) |
| HCP minimal preprocessing pipeline | [<u>https://github.com/Washington-University/HCPpipelines</u>](https://github.com/Washington-University/HCPpipelines) |
| ABCD-HCP pipeline (DCAN) | [<u>https://github.com/DCAN-Labs/abcd-hcp-pipeline</u>](https://github.com/DCAN-Labs/abcd-hcp-pipeline) |
| fMRIPrep | [<u>https://github.com/nipreps/fmriprep</u>](https://github.com/nipreps/fmriprep) |
| MRIQC | [<u>https://github.com/nipreps/mriqc</u>](https://github.com/nipreps/mriqc) |
| C-PAC / Preprocessed Connectomes Project | [<u>https://github.com/FCP-INDI/C-PAC</u>](https://github.com/FCP-INDI/C-PAC) |
| FSL (FMRIB Software Library) | [<u>https://fsl.fmrib.ox.ac.uk/</u>](https://fsl.fmrib.ox.ac.uk/) |
| ICA-AROMA | [<u>https://github.com/maartenmennes/ICA-AROMA</u>](https://github.com/maartenmennes/ICA-AROMA) |
| ICA-FIX | [<u>https://www.fmrib.ox.ac.uk/datasets/techrep/tr14sn1/tr14sn1.pdf</u>](https://www.fmrib.ox.ac.uk/datasets/techrep/tr14sn1/tr14sn1.pdf) |
| ANTs (Advanced Normalization Tools) | [<u>http://stnava.github.io/ANTs/</u>](http://stnava.github.io/ANTs/) |
| FreeSurfer | [<u>https://surfer.nmr.mgh.harvard.edu/</u>](https://surfer.nmr.mgh.harvard.edu/) |
| Connectome Workbench | [<u>https://www.humanconnectome.org/software/connectome-workbench</u>](https://www.humanconnectome.org/software/connectome-workbench) |
| Schaefer 2018 parcellation | [<u>https://github.com/ThomasYeoLab/CBIG/tree/master/stable_projects/brain_parcellation/Schaefer2018_LocalGlobal</u>](https://github.com/ThomasYeoLab/CBIG/tree/master/stable_projects/brain_parcellation/Schaefer2018_LocalGlobal) |
| Tian subcortical parcellation | [<u>https://github.com/yetianmed/subcortex</u>](https://github.com/yetianmed/subcortex) |
| Buckner cerebellar atlases | [<u>https://www.freesurfer.net/fswiki/CerebellumParcellation_Buckner2011</u>](https://www.freesurfer.net/fswiki/CerebellumParcellation_Buckner2011) |
| BrainSpace (gradients) | [<u>https://github.com/MICA-MNI/BrainSpace</u>](https://github.com/MICA-MNI/BrainSpace) |
| abagen (AHBA workflow) | [<u>https://github.com/rmarkello/abagen</u>](https://github.com/rmarkello/abagen) |
| Neurosynth | [<u>https://neurosynth.org/</u>](https://neurosynth.org/) |
| NiMARE | [<u>https://github.com/neurostuff/NiMARE</u>](https://github.com/neurostuff/NiMARE) |
| BIDS specification | [<u>https://bids-specification.readthedocs.io/</u>](https://bids-specification.readthedocs.io/) |
| BIDS Apps | [<u>https://bids-apps.neuroimaging.io/</u>](https://bids-apps.neuroimaging.io/) |
| DataLad | [<u>https://www.datalad.org/</u>](https://www.datalad.org/) |
| OpenNeuro | [<u>https://openneuro.org/</u>](https://openneuro.org/) |
| Reproducible Brain Corpus (RBC) | [<u>https://reprobrainchart.github.io/</u>](https://reprobrainchart.github.io/) |
| UK Biobank | [<u>https://www.ukbiobank.ac.uk/</u>](https://www.ukbiobank.ac.uk/) |
| Adolescent Brain Cognitive Development (ABCD) | [<u>https://nda.nih.gov/abcd</u>](https://nda.nih.gov/abcd) |
| HCP (Connectome Coordination Facility) | [<u>https://www.humanconnectome.org/</u>](https://www.humanconnectome.org/) |
| AOMIC PIOP1 / PIOP2 | [<u>https://nilab-uva.github.io/AOMIC.github.io/</u>](https://nilab-uva.github.io/AOMIC.github.io/) |
| Chinese Human Connectome Project (CHCP) | [<u>https://www.chinese-hcp.cn/</u>](https://www.chinese-hcp.cn/) |
| ABIDE | [<u>http://fcon_1000.projects.nitrc.org/indi/abide/</u>](http://fcon_1000.projects.nitrc.org/indi/abide/) |
| ADHD-200 | [<u>http://fcon_1000.projects.nitrc.org/indi/adhd200/</u>](http://fcon_1000.projects.nitrc.org/indi/adhd200/) |
| ADNI | [<u>https://adni.loni.usc.edu/</u>](https://adni.loni.usc.edu/) |
| PPMI | [<u>https://www.ppmi-info.org/</u>](https://www.ppmi-info.org/) |
| HBN (Healthy Brain Network) | [<u>http://fcon_1000.projects.nitrc.org/indi/cmi_healthy_brain_network/</u>](http://fcon_1000.projects.nitrc.org/indi/cmi_healthy_brain_network/) |
| LEMON dataset | [<u>https://www.nature.com/articles/sdata2018308</u>](https://www.nature.com/articles/sdata2018308) |
| StudyForrest | [<u>http://studyforrest.org/</u>](http://studyforrest.org/) |
| NSD (Natural Scenes Dataset) | [<u>https://naturalscenesdataset.org/</u>](https://naturalscenesdataset.org/) |
| NKI Rockland (via RBC) | [<u>http://fcon_1000.projects.nitrc.org/indi/enhanced/</u>](http://fcon_1000.projects.nitrc.org/indi/enhanced/) |
| Zarr storage format | [<u>https://zarr.readthedocs.io/</u>](https://zarr.readthedocs.io/) |
| dcm2niix | [<u>https://github.com/rordenlab/dcm2niix</u>](https://github.com/rordenlab/dcm2niix) |
| HeuDiConv | [<u>https://github.com/nipy/heudiconv</u>](https://github.com/nipy/heudiconv) |
| CuBIDS | [<u>https://github.com/PennLINC/CuBIDS</u>](https://github.com/PennLINC/CuBIDS) |
| NeuroComBat (Python) | [<u>https://github.com/Jfortin1/ComBatHarmonization</u>](https://github.com/Jfortin1/ComBatHarmonization) |
| nilearn | [<u>https://nilearn.github.io/</u>](https://nilearn.github.io/) |

**9. Closing note**

The four 2025–2026 fMRI foundation-model papers signal that the field is
converging on a small handful of preprocessing pipelines (HCP-MPP,
fMRIPrep), one canonical parcellation triple (Schaefer-400 + Tian-III +
Buckner-7), and one volumetric standard (2 mm MNI152, 96³, TR ≈ 0.72–0.8
s). The Taylor lifespan paper, while not a foundation model, is the
cleanest public example of cross-cohort harmonisation discipline. None
of the four foundation-model papers, however, publishes its preprocessed
corpus as a FAIR-compliant BIDS-Derivatives release with persistent DOIs
and DataLad versioning. That gap is the cheapest place where Cytognosis
can lead, and §7 sketches an executable plan for doing exactly that.
