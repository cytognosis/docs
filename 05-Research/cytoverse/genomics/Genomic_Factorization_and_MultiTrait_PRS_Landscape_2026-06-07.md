# Genomic Factorization, Multi-Trait PRS, and Genome Foundation Models for Neuropsychiatric Indications: Landscape and State of the Art (June 2026)

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: researchers, stakeholders
> **Tags**: `research`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

**Purpose.** One reference map for how to factorize and embed GWAS summary statistics across related neuro indications, compute factor-level polygenic scores, reconcile summary statistics with individual genotypes, and bridge all of this to genomic foundation models, sparse-LD infrastructure, the pangenome, and pathway-anchored interpretability. Built to sharpen Cytognosis grants (NIH, ARPA-H HSF/IGoR, NSF, AWS) and to guide the real Cytoverse and factorized-PRS build.

**Reading time.** About 18 minutes full; 4 minutes if you read only Sections 0, 1, and 11.

**If you read one thing.** Read **Section 0 (BLUF)** then **Section 11 (recommended pipeline)**. Section 9 holds the precise novelty argument for our factorized PRS.

**Sources.** Synthesizes four internal seed docs (`Multi-Trait GWAS Analysis Methods.md`, `AI_ML_dimensional_biotyping_landscape_2026.md`, `BDNF_TrkB_Neuroplasticity_Axes_Dossier_2026-06-03.md`, `multiscale-biomarkers.md`) with fresh 2025-2026 web research across four areas (genomic foundation models, sparse-LD/LDGM, pangenome, multi-trait panels and pathway-factorization). Citations are inline with DOIs or URLs; newest 2026 DOIs are flagged for confirmation at cite-time.

---

## 0. BLUF

Three conclusions frame where we sit.

1. **The statistical-genetics core is mature and our methods sit at its frontier.** Factorizing many GWAS into shared latent axes is now done well by **Genomic SEM** (model-based, summary-level) and **GLEANR** (sparse, sample-sharing-robust matrix factorization), complemented by **DeGAs**, **FactorGo**, **MTAG**, and **GWAS-by-subtraction**. Symptom-level and item-level factor GWAS already beats categorical DSM GWAS on discovery power. Multi-trait PRS (wMT-SBLUP, PRSmix+, PPRS) reliably outperforms single-trait PRS. We are not inventing a field; we are extending it into per-person, mechanism-anchored neuro axes.

2. **Genomic foundation models are powerful for variant annotation, not yet for polygenic prediction.** AlphaGenome and Borzoi predict regulatory variant effects at base-pair to 32 bp resolution including brain tracks; Evo 2 gives zero-shot variant and haplotype scores at 1 Mb. But the "personal-genome gap" (Sasse and Kelley 2023; Karollus 2023) means no foundation model yet beats a GWAS-trained PRS for a common-variant psychiatric trait. **Their defensible 2026 use is as functional priors feeding S-LDSC, PolyFun, and our TF-region factorization, plus rare-variant scoring.**

3. **The interpretable, per-person, pathway-factorized axis is still an open gap, and our factorized PRS lands precisely in it.** **PRSet** and **S-LDSC** are the closest prior art and neither does what we propose. The combination of (a) restricting per-person PRS to **transcription-factor-binding-footprint regions** (CREB-bound, SREBP-bound ChIP-seq peaks), (b) anchoring each region set to a **named molecular program** (BDNF/TrkB neuroplasticity, cholesterol biosynthesis), and (c) delivering the result as a **continuous coordinate system** for psychiatric stratification has no published precedent as of June 2026.

**The unfilled gap equals our contribution.** No method unifies multi-trait genomic factorization, foundation-model functional priors, sparse-LD efficiency, and pathway-anchored per-person axes into one neuropsychiatric coordinate. That is the Cytoverse and factorized-PRS objective.

---

## 1. Where Cytognosis sits in this landscape

Our genomic thesis, established in the seed docs, is a directed chain: **fixed germline genome → factorized, pathway-anchored genetic axes → (mediating connectome) → dimensional phenotype.** The genome supplies stable, noninvasive priors; the connectome is the causal mediator; phenotype emerges from both plus environment (`multiscale-biomarkers.md`, Section 8).

Our crown-jewel genomic IP (`BDNF_TrkB_Neuroplasticity_Axes_Dossier`, Section 5) is the **factorized PRS**: process-specific polygenic scores restricted to TF-bound regions (CREB for the Mood/neuroplasticity axis, SREBP for the cholesterol/TrkB axis, additional TF sets for the Cognitive axis), computable from genotype alone in living people. This document maps the full method space around that idea and identifies the tools that build, validate, and extend it.

Positioning in one line: **we are building the per-person, mechanism-labeled, multi-trait genomic coordinate that the mature statistical-genetics stack and the new foundation models each only partly support.**

---

## 2. The problem the field is solving

Single-trait GWAS discards the pervasive pleiotropy of the genome and the dimensional structure of psychiatry. Categorical DSM diagnoses capture only a fraction of molecular heritability (about 8 percent for MDD, about 24 percent for schizophrenia per the seed deep-research doc), because shared genetic liability cuts across diagnostic boundaries. The Grotzinger 14-disorder analysis found **five genomic factors explaining on average about 66 percent of per-disorder genetic variance** across more than one million people (Nature 2025, doi:10.1038/s41586-025-09820-3). The field has therefore moved to multivariate, dimensional, and multi-omic frameworks. The four families below are the toolkit.

---

## 3. The statistical-genetics core (summary plus expansion)

### 3a. Multi-trait factorization and embedding of summary statistics

This is the heart of "factorize GWAS across related indications." Methods differ in whether they model a covariance matrix or the raw effect-size matrix, how they handle sample overlap, and how sparse and interpretable the factors are.

| Method | Year | Input | Factorization approach | Sample-overlap handling | Interpretability / sparsity | Citation |
|---|---|---|---|---|---|---|
| **Genomic SEM** | 2019 | LDSC genetic covariance matrix | Structural equation model; CFA (confirmatory) or EFA (exploratory); GWAS of latent factors | Robust to arbitrary overlap via LDSC cross-trait intercepts | Researcher-specified factors; very interpretable; fit indices (CFI, SRMR) | Grotzinger, Nat Hum Behav 2019, doi:10.1038/s41562-019-0566-x |
| **GLEANR** | 2024-2025 | Effect-size (Z) matrix, many traits | Sparse matrix factorization with L1 regularization and data-driven factor count | Explicit sample-sharing noise model (key differentiator) | High sparsity; factors enriched for cell type, pathway, selection signatures; replicates across biobanks | AJHG 2025; bioRxiv 2024.11.12.623313 |
| **DeGAs** | 2019 | Variant x phenotype Z matrix (2,138 UKB traits) | Truncated SVD; components of genetic association | Implicit (single-cohort UKB) | Dense by default; variant and trait contribution scores; web app | Tanigawa, Nat Commun 2019, doi:10.1038/s41467-019-11953-9 |
| **FactorGo** | 2023 | Standardized beta/SE matrix (2,483 Pan-UKBB traits) | Variational Bayesian factor analysis with ARD prior; JAX-accelerated | Single-cohort; no explicit cross-study overlap term | ARD auto-prunes factors; probabilistic loadings (uncertainty); sparser than tSVD | Zhang, Mancuso lab, AJHG 2023, doi:10.1016/j.ajhg.2023.09.003 |
| **MTAG** | 2018 | Per-SNP sumstats, multiple traits | Inverse-variance multi-trait meta-analysis; boosts per-trait Z | Explicit overlap correction (LDSC covariance) | No latent factors; a power-boosting pre-step | Turley, Nat Genet 2018, doi:10.1038/s41588-017-0009-4 |
| **GWAS-by-subtraction** | 2021 | Two sumstats via Genomic SEM | Cholesky residualization; GWAS of orthogonalized factor | Via Genomic SEM intercepts | One interpretable residual factor; clean axis orthogonalization | Demange, Nat Genet 2021, doi:10.1038/s41588-020-00735-5 |
| **HDL** | 2020 | Pair of sumstats plus LD reference | Full-likelihood genetic correlation (about 60 percent variance reduction vs LDSC) | Default assumes no overlap | Pairwise rg; better covariance input to Genomic SEM | Ning, Nat Genet 2020, doi:10.1038/s41588-020-0653-y |
| **SUPERGNOVA** | 2021 | Pair of sumstats plus LD reference | Local genetic correlation across about 2,353 segments | Cross-trait local LD intercepts | Region-resolved sharing; characterizes where a factor lives | Zhang, Genome Biol 2021, doi:10.1186/s13059-021-02478-w |

**What to take.** **Genomic SEM** is the interpretive anchor (it produced the 5-factor scaffold our axes align to). **GLEANR** is the discovery engine because it is the only sparse factorizer that explicitly defends against sample-sharing artifacts, which matter when factorizing overlapping biobank GWAS. **FactorGo** adds loading uncertainty for propagating into PRS. **MTAG** and **HDL** are pre-processing upgrades; **SUPERGNOVA** is post-hoc characterization. No published deep-learning autoencoder operating directly on the summary-statistic matrix has displaced GLEANR or FactorGo as of mid-2026 (a genuine open methods niche).

### 3b. Symptom-level and item-level dimensional factor GWAS

The route past categorical diagnoses. Run GWAS on individual symptom items (PHQ-9, GAD-7, EPQR-S neuroticism), estimate the genetic correlation matrix with LDSC, run exploratory factor analysis to find dimensions (typically DEP, ANX, and an underpowered Somatic factor), then model the validated structure in Genomic SEM and run multivariate factor GWAS. Pairwise regional decomposition (gwas-pw over about 1,703 regions) then separates shared pleiotropy from trait-specific biology (depression-specific links to hypertriglyceridemia; anxiety-specific links to blood pressure). The seed deep-research doc documents the large discovery-power gains: a P-factor model found 128 lead SNPs versus 4 for univariate bipolar and 0 for univariate PTSD. This workflow is exactly how our **Mood, Thought, and Cognitive axes** get genomic definition at the symptom level.

### 3c. Multi-trait polygenic scores

| Method | Design | Advantage | Limitation | Performance highlight |
|---|---|---|---|---|
| **wMT-SBLUP** | Weighted multi-trait summary BLUP | Highest accuracy across architectures | Compute-heavy; needs matched LD panel | Beats simpler multi-trait methods on continuous and binary traits |
| **PRSmix / PRSmix+** | Ensemble of single-trait PRS (PRSmix+ adds correlated traits) | No pre-defined traits; auto-selects; portable | Needs individual-level validation set for weights | 1.72-fold (EUR) and 1.42-fold (SAS) accuracy gains |
| **PPRS** | Multiple disease-relevant PRS plus functional annotations | Preserves interpretable per-trait contributions | Needs annotation data and tuning | POAG AUC 0.814 (EUR); top-decile 74-fold risk |
| **mPRS** | LASSO over a panel of component PRS | Simple; sparse selection | Depends on training cohort | 9-trait heart-failure PRS, two-fold incident risk |
| **PRScsx / SDPRx** | Bayesian cross-trait (continuous shrinkage / nonparametric) | Models LD and cross-trait architecture | PRScsx ignores rg; SDPRx pairwise only | Leverages pleiotropy for single-target gain |

These are the population-level multi-trait PRS comparators we benchmark against. Our factorized PRS is different in kind (per-pathway, per-person axes), so these are baselines, not competitors.

### 3d. Reconciling summary statistics with individual genotypes

The "jointly analyze sumstats and individual genotypes" ask.

- **Meta-PRS** beats Meta-GWAS in many cases: a simple linear combination of independently trained per-person PRS matches or exceeds meta-analyzing the underlying sumstats, including for psychiatric traits (bioRxiv 2020.11.27.401141).
- **S-JointLMM and LS-imputation** impute both the genetic and the environmental/omic component of a trait by combining SNP-trait and metabolite-trait sumstats with individual-level data (PMC10460491). Joint SNP-plus-metabolite imputation recovers environmental associations that SNP-only imputation misses (r 0.995 vs 0.314 for BMI).
- **Multivariate LMMs (GEMMA, MTG2)** remain the gold standard when full individual genotypes (WGS or arrays) are available: they fit multiple phenotypes jointly with a genomic relationship matrix and estimate exact multi-trait genetic covariance (GEMMA, github.com/genetics-statistics/GEMMA; MTG2).

For us, **Meta-PRS** is the pragmatic way to combine our genotype cohorts (NeuroBioBank-class) with external PGC sumstats; **mvLMM** is the reference when we hold raw genotypes; **S-JointLMM** is the template for fusing genome with the metabolomic and sensor streams later.

---

## 4. Special interest 1: Genomic foundation models and fine-tuning for neuro

**BLUF.** As of 2026, genomic FMs predict regulatory variant effects (expression, chromatin, splicing) at high resolution, including brain cell types (Borzoi Prime resolves microglia-specific eQTLs). They do not yet deliver competitive common-variant psychiatric PRS out of the box. The defensible use is **FM-derived variant scores as functional priors** into S-LDSC, PolyFun, and our TF-region factorization, plus **rare-variant scoring** that GWAS underpowers.

| Model | Year | Arch / context | Variant-effect output | Fine-tune / adapt | Neuro / disease use | Citation |
|---|---|---|---|---|---|---|
| **AlphaGenome** | 2026 | U-Net + Transformer, 1 Mb, 1 bp to 32 bp; about 5,930 human tracks | 11 modalities incl. RNA-seq, splice, ChIP, Hi-C; confident direction for at least one variant in 49% of GWAS credible sets (complementary to COLOC; about 4x more in lowest-MAF quintile) | API inference; no public fine-tune yet | Brain partial (neurons in; microglia under-represented) | Avsec et al., Nature 2026, doi:10.1038/s41586-025-10014-0 (verified); bioRxiv 2025.06.25.661532 |
| **Evo 2 (7B/40B)** | 2026 | StripedHyena 2, 1 Mb, 9.3T bp, 128k genomes | Zero-shot log-likelihood; haplotype and whole-gene scores | Zero-shot; embeddings for downstream heads | APOE/AD proof-of-concept linked to ADNI/UKB (medRxiv 2025.09.09.25335438) | Nature 2026; arXiv 2502.18638 |
| **Borzoi** | 2024 | Conv + Transformer + U-Net, 524 kb; 7,611 human tracks | RNA-seq at 32 bp; eQTL and sQTL direction/effect | **LoRA + Locon**, fits one 24 GB GPU; full FT best if compute allows | GTEx brain eQTL included | Linder, Nat Genet 2024, doi:10.1038/s41588-024-02053-6; PEFT bioRxiv 2025.05.26.656171 |
| **Borzoi Prime** | 2025 | Borzoi + scRNA atlases | Cell-type-specific effects (correct microglia ADGRD1 eQTL) | Trained on scRNA pseudo-bulk | First direct brain cell-type eQTL demonstration | bioRxiv 2025.06.10.658961 |
| **Enformer** | 2021 | CNN + Transformer, 196 kb | CAGE/ChIP/DNase at 128 bp; ISM eQTL scoring | Head replacement / fine-tune | Brain CAGE tracks; personal-genome critique anchor | Avsec, Nat Methods 2021, doi:10.1038/s41592-021-01264-7 |
| **Nucleotide Transformer** | 2023-24 | BERT-style, 6-mer, 6-12 kb | Zero-shot LLR variant scoring; embeddings | Full or linear-probe fine-tune | Zero-shot deleteriousness | Dalla-Torre, Nat Methods 2024, doi:10.1038/s41592-024-02523-z |
| **NTv3** | Dec 2025 | U-Net, 1 Mb, single-nt; 16k+ tracks, 24 species | Single-nt variant effect, 106-task benchmark | Not yet characterized | None neuro-specific yet | bioRxiv 2025.12.22.695963 [preliminary] |
| **HyenaDNA** | 2023 | Hyena SSM, up to 1 M tokens | Zero-shot variant scoring | In-context / fine-tune | Lower than GPN-MSA on deleteriousness | NeurIPS 2023, arXiv:2306.15794 |
| **Caduceus** | 2024 | Bi-Mamba, RC-equivariant, 131 kb | Zero-shot long-range variant effect | Standard fine-tune; RC-equivariant | Beats 10x-larger models on long-range benchmark | ICML 2024, arXiv:2403.03234 |
| **GPN / GPN-MSA** | 2023-24 | Dilated CNN / Transformer on MSA | Genome-wide SNV pathogenicity; precomputed for about 9B SNVs | Unsupervised; scores downloadable | Best zero-shot deleteriousness (beats CADD, phyloP) | PNAS 2023, doi:10.1073/pnas.2311219120; GPN-MSA Nat Biotechnol 2024 |

**FM scores into polygenic prediction.** The validated chain is: score GWAS variants with Borzoi or Enformer in brain tracks (allelic difference or in-silico mutagenesis), then feed those predicted effects as **continuous annotations into S-LDSC** (heritability enrichment) or as **priors into PolyFun/SuSiE** (fine-mapping). **Epi-PRS** (PNAS 2025, doi:10.1073/pnas.2419202122) is the most direct FM-to-PRS bridge so far: it imputes cell-type epigenomic signals from diploid personal genomes and feeds them into a risk model, handling rare variants and diploid interactions standard PRS ignores (demonstrated on breast cancer and T2D, not yet neuro, but directly transferable). Gene-expression risk scores from S-PrediXcan in prefrontal cortex already predict schizophrenia variance (Am J Hum Genet 2021, PMID 33979660), the empirical-eQTL analog of the FM approach.

**Limitations to state honestly in grants.** Current S2F models **underpredict inter-individual expression variation** and often get cis-eQTL direction wrong (Sasse and Kelley, Nat Genet 2023, doi:10.1038/s41588-023-01574-w). They lean on promoter-proximal variants and largely ignore distal enhancers beyond about 50 kb (Karollus, Nat Genet 2023, doi:10.1038/s41588-023-01524-6). They are strong on rare high-impact variants, weak on common small-effect GWAS variants. AlphaGenome resolves direction for only 49 percent of credible sets and under-represents microglia, a cell type central to psychiatric immune-pathway signals.

**Recommended neuro fine-tuning path.** Base model **Borzoi** (best-characterized PEFT and existing brain tracks; AlphaGenome lacks a public fine-tune API). Fine-tune on **GTEx v9 brain (13 regions), PsychENCODE (CommonMind, BrainGVEX), BrainVar, and ENCODE brain ATAC/H3K27ac (NeuN+/NeuN- fractions)**. Use **LoRA (r=8, alpha=16) on attention Q/V plus Locon (r=4) on late conv layers**, about 0.6 percent trainable params, one A100 or RTX 4090. Then score credible-set variants and feed predicted log-fold-changes as **priors into PolyFun/S-LDSC**. For our axes specifically, this gives a foundation-model-derived functional weight for **CREB-bound and SREBP-bound region variants**, complementary to the ChIP-seq region definition (Section 9).

---

## 5. Special interest 2: Sparse LD and precision-matrix methods (LDGM)

**BLUF.** **LDGM** precision matrices (O'Connor lab, Nat Genet 2023, doi:10.1038/s41588-023-01487-8) are extremely sparse inverses of the LD correlation matrix, derived from ancestral-recombination-graph genealogies and estimated with graphical lasso. They cover about 18 million variants across five ancestry groups and give order-of-magnitude (10-100x) speedups on LD operations versus dense panels. Two production toolkits consume them: **graphld** (Python, O'Connor lab) and **score** (Giulio Genovese's bcftools plugin suite). This is the most practically mature infrastructure for scalable, multi-ancestry, summary-statistic PRS and heritability analysis available today.

**Why it matters.** The dense LD matrix R is O(N^2) memory and O(N^3) compute; its precision matrix P = R-inverse is local and sparse because LD is generated by a genealogy. An LD block fits in kilobytes instead of megabytes. Pre-built **multi-ancestry** LDGMs (AFR, AMR, EAS, EUR, SAS from 1000 Genomes tree sequences) directly address the cross-ancestry portability problem.

| Tool | What it does | LDGM usage | Language / status | Link |
|---|---|---|---|---|
| **ldgm** (awohns/ldgm) | Reference construction and BLUPx-ldgm PRS | Generates and exposes precision matrices | MATLAB + Python; maintained | github.com/awohns/ldgm |
| **graphld** (oclb/graphld) | graphREML heritability partitioning, BLUP, LD clumping, GWAS simulation, sumstat I/O | Loads precision matrices as a sparse operator; all ops exploit sparsity | Python; v1.0 Jan 2025 | github.com/oclb/graphld |
| **graphREML** | Likelihood-based heritability enrichment; about 2.5x more significant annotation findings than S-LDSC at equal compute | LDGM makes full-likelihood log-det and quadratic forms tractable | In graphld | medRxiv 2024.11.04.24316716 |
| **bcftools +pgs** | Full graphpred PRS: BLUP then sparse-prior Gibbs (SuSiE generalization); 10-100x faster than PRS-CS, 5-10% R-squared boost over HapMap3-only | LDGM-VCF for all LD computations | C plugin; bcftools 1.22 | github.com/freeseek/score |
| **bcftools +blup / +munge / +metal / +score** | BLUP weights, sumstat munging, meta-analysis, PGS application | +blup uses LDGM; others are sumstat ops | C plugins | github.com/freeseek/score |
| **VIPRS** | Variational Bayesian PRS to 18M variants; 50x storage reduction, 1-2 orders faster than LDpred2/PRS-CS | Compressed sparse LD (analogous design) | Python; AJHG 2025, doi:10.1016/j.ajhg.2025.04.007 | — |

**Versus LDpred2, PRS-CS, SBayesR.** Those rely on dense regional panels (usually HapMap3, about 1.3M variants), are RAM-heavy genome-wide, and are largely EUR-only. LDGM methods scale to 18M variants, ship multi-ancestry precision matrices, run 10-100x faster, and (graphREML, graphpred) exceed their accuracy. **For us, LDGM is the efficiency substrate that makes per-pathway, per-ancestry factorized PRS tractable at whole-genome scale.** Note the open niche the subagent flagged: **no published method yet combines LDGM with multi-trait factorized PRS**, a concrete methods contribution we could make.

---

## 6. Special interest 3: The pangenome

**BLUF.** The HPRC 2023 draft pangenome (Liao et al., Nature, doi:10.1038/s41586-023-05896-x; 47 diploid, 94 haplotypes, 119 Mbp new sequence) plus **Release 2 (May 2025, 200-plus individuals)** make graph-based variant calling the new standard for reducing reference bias and catching structural variants. But **direct pangenome-based GWAS and PRS remain nascent in 2026**: the field is producing better variant catalogs, while the statistical machinery for graph-based association and polygenic scoring is still being built.

**What is production-grade.** Pangenome-aware mapping with **vg giraffe** on **Minigraph-Cactus** graphs (and the heavier **PGGB** builder) detects SVs (insertions, deletions, inversions) that linear pipelines miss and reduces the GRCh38 European reference bias that hurts non-European variant calling. For neuropsychiatric genetics this matters at CNV-rich and complex loci (HLA, the BDNF region, 22q11.2 deletions, central to our user context). **Swave** (Nat Genet 2025/2026) characterizes population-level SVs from pangenome graphs, a step toward SV catalogs usable in association testing.

**What is not ready.** Cross-ancestry PRS portability is still driven mainly by LD and allele-frequency differences, not reference representation, so pangenomes help PRS only indirectly today. No production SV-PRS framework exists. **Maturity verdict: adopt pangenome-aware variant calling now for any cohort we sequence (especially multi-ancestry); treat graph-based GWAS/PRS as a 2026-2028 research frontier, not operational tooling.**

| Resource | Type | Key fact | Link |
|---|---|---|---|
| HPRC draft pangenome | Paper | 94 haplotypes, 119 Mbp new, Minigraph-Cactus | doi:10.1038/s41586-023-05896-x |
| HPRC Release 2 | Data | 200-plus individuals, May 2025 | hgdownload.soe.ucsc.edu/hubs/HPRC |
| vg / vg giraffe | Software | GBWT-indexed haplotype-aware mapping | github.com/vgteam/vg |
| Minigraph-Cactus | Builder | Official HPRC graph | PMC10638906 |
| Swave | Method | Population SV from graphs (deep learning) | Nat Genet 2025/2026 [confirm DOI] |

---

## 7. Special interest 4: Multi-trait summary-statistic panels (Pan-UKBB, PGC, NeuroGWAS)

**BLUF.** Six harmonized panels are ready to factorize today. The neuro anchors are **PGC** (14 disorders; the CDG3 cross-disorder sumstats and 5 factor sumstats are downloadable) and **Pan-UKBB** (7,228 phenotypes, 6 ancestries, free). **FinnGen R12** adds about 2,502 Finnish endpoints with rich neuro coverage. **"NeuroGWAS" is not a public resource**; it is our internal label for a tailored cross-neuro panel assembled from PGC, FinnGen, and UKB neuro endpoints for Genomic SEM and GLEANR factorization. Treat it as a Cytognosis asset, not a citable external tool.

| Resource | Scope | Ancestries | Neuro relevance | Access |
|---|---|---|---|---|
| **Pan-UKBB** | 7,228 phenotypes, 16,131 GWAS | 6 groups (EUR, AFR, AMR, CSA, EAS, MID) | Mental health, brain imaging, cognition; cross-ancestry resolution | pan.ukbb.broadinstitute.org (AWS open) |
| **PGC CDG3** | 14 disorders plus 5 latent-factor sumstats | EUR-primary plus diverse | The cross-psychiatric factorization foundation; about 1.06M cases | pgc.unc.edu; figshare 10.6084/m9.figshare.30359017 |
| **PGC per-disorder** | About 15 disorders, multiple waves | EUR-primary, growing diverse | SCZ (69K/237K, 2022), BIP (59K/781K, 2024), MDD (about 689K cases, 2025), ADHD, ASD, PTSD, OCD, AN, TS, Anxiety, SUD | pgc.unc.edu (figshare DOIs per study) |
| **FinnGen R12** | About 2,502 endpoints, about 500K people | Finnish isolate (EUR) | Depression, SCZ, BIP, anxiety, epilepsy, MS, PD, AD; fine-mapping files | finngen.fi/en/access_results |
| **GWAS Catalog** | 6,000-plus studies, 10,000-plus traits | Multi-ancestry | Broad neuro/psych deposition hub | ebi.ac.uk/gwas (API) |
| **IEU OpenGWAS** | 50,000-plus curated datasets | EUR-primary, growing | Large psych coverage; MR and rg-matrix input | gwas.mrcieu.ac.uk |
| **MVP** | About 900K veterans | EUR, AFR, LAT (AFR-rich) | Depression (340K cases), PTSD, anxiety, SCZ, BIP, OUD; trans-ancestry power | dbGaP phs001672 |

**For us.** The factorization input set is **PGC CDG3 plus FinnGen neuro plus Pan-UKBB neuro/cognitive phenotypes**; MVP adds non-European power; the **Grotzinger 5-factor structure is the interpretive anchor** for whatever GLEANR or FactorGo discovers. Our internal NeuroGWAS panel is the curated, deduplicated, sample-overlap-mapped version of this for direct factorization.

---

## 8. Special interest 5: Network and pathway priors for interpretability

**BLUF.** Two mature lineages inject biological priors. The **statistical-genetics lineage** (S-LDSC, MAGMA, H-MAGMA, PolyFun, LDpred-funct, SBayesRC) reweights or filters variants by functional annotation. The **deep-learning lineage** (P-NET, DCell, pathway-VAEs) structures model architecture by gene-set or ontology membership. The DL pathway-VAEs are almost entirely transcriptomic and have **not** been applied to germline variants, which is a transferable opportunity.

| Method | Year | What it does | Pathway / annotation prior | Per-person? | Citation |
|---|---|---|---|---|---|
| **S-LDSC** | 2015/2018 | Partitions heritability by annotation; enrichment per category | Coding, conserved, regulatory, enhancers, **TF ChIP-seq regions**, cell-type open chromatin | No (population) | Finucane, Nat Genet 2015 doi:10.1038/ng.3404; 2018 doi:10.1038/s41588-018-0081-4 |
| **MAGMA** | 2015 | Gene and gene-set association from sumstats | KEGG/Reactome/GO gene sets | No | de Leeuw, PLoS Comput Biol 2015, doi:10.1371/journal.pcbi.1004219 |
| **H-MAGMA** | 2020 | MAGMA plus brain Hi-C to map noncoding SNPs to genes | Fetal/adult brain chromatin interactions | No | Sey, Nat Neurosci 2020, doi:10.1038/s41593-020-0603-0 |
| **PolyFun / PolyPred** | 2020/2022 | Functionally-informed fine-mapping; causal-effect PRS, better cross-ancestry | Hundreds of baseline-LD annotations; custom supported | PolyPred yes (one genome-wide score) | Weissbrod, Nat Genet 2020 doi:10.1038/s41588-020-00735-5; 2022 doi:10.1038/s41588-022-01016-z |
| **LDpred-funct** | 2021 | Bayesian PRS with S-LDSC functional priors | Baseline-LD categories | Yes (one score) | Marquez-Luna, AJHG 2021, doi:10.1016/j.ajhg.2021.05.014 |
| **AnnoPred** | 2017 | Bayesian PRS, annotation-set causal priors | Baseline-LD annotations | Yes (one score) | Hu, PLoS Genet 2017, doi:10.1371/journal.pgen.1006619 |
| **SBayesRC** | 2024 | Annotation-integrated Bayesian PRS; 14-33% accuracy gain | Functional annotations in shrinkage | Yes (one score) | Zheng, Nat Genet 2024, doi:10.1038/s41588-024-01704-y |
| **TWAS pathway** | 2020 | Aggregates eQTL-imputed gene associations across pathways | Tissue eQTL panels plus MSigDB | No | Lu, Nat Neurosci 2020 |

**Takeaway.** S-LDSC is the one population-level method that already supports **TF-binding ChIP-seq annotations**, so it is both our closest annotation-level precedent and our cheapest de-risking step (confirm CREB-bound and SREBP-bound regions are heritability-enriched before building the per-person pipeline). None of these produce per-person, mechanism-labeled axes, which is Section 9.

---

## 9. Special interest 6: Factorizing variants into pathway-enriched, interpretable axes (and our novelty)

**BLUF.** The methods that produce biologically interpretable latent dimensions split into population-level genomic factorizers (GLEANR), germline per-person pathway scorers (PRSet, PRS-Net, scPRS), and architecture-constrained DL (P-NET, pathway-VAEs, mostly transcriptomic). **No published method does TF-binding-footprint-restricted, mechanism-anchored, per-person pathway PRS as a coordinate system.** That is our gap.

| Method | Year | Input | How priors injected | Output | Germline? | Citation |
|---|---|---|---|---|---|---|
| **GLEANR** | 2024-25 | GWAS sumstats | Sparse factorization; post-hoc pathway/cell-type enrichment | Population sparse factors | Yes | AJHG 2025; bioRxiv 2024.11.12.623313 |
| **PRSet** | 2023 | Genotype plus sumstats | Gene-set membership (KEGG/Reactome/GO) by gene coordinates plus flanks | **Per-person vector of k pathway PRS** | Yes | Choi, PLoS Genet 2023, doi:10.1371/journal.pgen.1010624 |
| **PRS-Net** | 2025 | Genotype plus sumstats | GNN message-passing over PPI network; attention attribution | Per-person score, gene-level attribution | Yes | Shu, Genome Res 2025, doi:10.1101/gr.279115.124 |
| **scPRS** | 2025 | Genotype plus scATAC atlas | Restricts to cell-type open chromatin (under 11% of variants) | Per-person, cell-type-resolved score | Yes | Zhang, Nat Biotechnol 2025, doi:10.1038/s41587-025-02725-6 [confirm] |
| **P-NET** | 2021 | Somatic mutation/CNA | Reactome-hierarchy-constrained net (3,007 pathways, 5 layers) | Per-patient pathway-node attribution | No (somatic; transferable) | Elmarakeby, Nature 2021, doi:10.1038/s41586-021-03922-4 |
| **DCell** | 2018 | Germline genotype (yeast) | GO-hierarchy-structured net | Per-genotype subsystem activations | Yes (yeast) | Ma, Nat Methods 2018, doi:10.1038/nmeth.4627 |
| **VEGA / pmVAE / OntoVAE / expiMap / f-scLVM** | 2017-23 | Single-cell transcriptome | VAE latent nodes masked to pathway membership | Per-cell pathway activity | No (transcriptome only) | VEGA Nat Commun 2021; expiMap Nat Cell Biol 2023; f-scLVM Mol Syst Biol 2017 |

**Precise novelty of the Cytognosis factorized PRS (for grants).**

- **vs PRSet (closest prior art).** PRSet defines pathway membership by **gene-coordinate proximity** to curated KEGG/Reactome/GO genes and applies the same GWAS weights across pathways. Our method defines membership by **TF-binding occupancy** (CREB, SREBP ChIP-seq footprints) and treats occupancy itself as the functional prior, and it anchors each set to a **named mechanism**, not a database ontology term. Architecturally distinct.
- **vs S-LDSC.** S-LDSC can test enrichment in CREB-bound or SREBP-bound regions (our de-risking step) but emits only population-level statistics, never a per-person score.
- **vs LDpred-funct / PolyPred / SBayesRC.** These reweight the whole genome into one improved score; they do not decompose risk into separate mechanism-specific axes.
- **vs GLEANR.** Population-level factors with post-hoc enrichment; no per-person score, and the mechanism is read off after factorization, not anchored before it.
- **vs PRS-Net / scPRS.** PRS-Net uses a PPI graph (not TF footprints) with post-hoc gene attribution; scPRS resolves by cell type (not by named TF program). Neither yields a per-person vector indexed to named mechanistic programs.
- **vs pathway-VAEs.** Same structural idea (mask latent nodes to gene sets) but applied to **transcriptomes**, never to germline variants in published form.

**The novel contribution, stated for a reviewer:** per-person genetic liability scores defined by **TF-binding occupancy as a cis-regulatory proxy for a named molecular program** (CREB occupancy = BDNF/TrkB neuroplasticity; SREBP occupancy = cholesterol/TrkB axis), delivered as **continuous axes in a psychiatric coordinate system**. Claim the TF-region-factorized, mechanism-anchored, coordinate-system formulation precisely; cite PRSet and S-LDSC as precedent for per-pathway scoring and TF-annotation enrichment respectively; do not claim "per-person pathway PRS" itself as new (PRSet owns that).

---

## 10. Deep learning versus traditional statistical genetics: when to use which

| Need | Use traditional statgen | Use deep learning |
|---|---|---|
| Factorize many GWAS into shared axes | Genomic SEM, GLEANR, FactorGo | (open niche; no DL winner on sumstats yet) |
| Per-person multi-trait PRS | wMT-SBLUP, PRSmix+, LDGM graphpred | PRS-Net (PPI-GNN), scPRS (cell-type) |
| Variant functional effect (esp. rare, noncoding) | S-LDSC annotations, eQTL | AlphaGenome, Borzoi, Evo 2, GPN-MSA |
| Cross-ancestry portability | PolyPred, SBayesRC, multi-ancestry LDGM | FM functional priors (indirect) |
| Pathway-anchored interpretability | PRSet, MAGMA, H-MAGMA | P-NET, pathway-VAEs (transcriptome today) |
| Scale to 18M variants efficiently | LDGM (graphld, bcftools +pgs), VIPRS | — |

**Rule of thumb.** Traditional methods win for factorization, heritability, and calibrated PRS on common variants. Deep learning wins for variant-to-function annotation and rare-variant effects. The strongest 2026 designs are **hybrids**: FM-derived priors feeding statistical-genetics PRS and factorization.

---

## 11. Recommended pipeline for Cytognosis (the synthesis)

A defensible, cutting-edge build that uses each tool where it is strongest.

1. **Assemble the neuro multi-trait panel ("NeuroGWAS," internal):** PGC CDG3 (14 disorders plus 5 factor sumstats) plus FinnGen R12 neuro endpoints plus Pan-UKBB neuro/cognitive phenotypes plus MVP for non-European power. Harmonize and map sample overlap.
2. **Pre-boost low-N disorders** (OCD, TS, AN) with **MTAG**; upgrade the genetic-covariance matrix with **HDL** before any SEM step.
3. **Factorize in parallel:** **GLEANR** (sparse, sample-sharing-robust discovery) and **FactorGo** (probabilistic loadings); cross-validate against the **Genomic SEM 5-factor** scaffold as the interpretive anchor; characterize factor genomic architecture with **SUPERGNOVA**.
4. **Build the factorized PRS (crown jewel):** define **CREB-bound and SREBP-bound region sets** from brain ChIP-seq; **de-risk with S-LDSC** (confirm heritability enrichment) before building; restrict per-person PRS to these regions to produce **Mood, Thought, Cognitive axes** as a coordinate. Layer **foundation-model variant priors** (Borzoi fine-tuned on GTEx brain, PsychENCODE, BrainVar via LoRA+Locon) and **PolyFun** fine-mapping to weight within-region variants.
5. **Run efficiently at whole-genome scale** on **LDGM** infrastructure (graphld / bcftools +pgs) with **multi-ancestry precision matrices** for portability.
6. **Reconcile with individual genotypes:** **Meta-PRS** to combine our genotype cohorts with external sumstats; **mvLMM (GEMMA)** where we hold raw genotypes; **S-JointLMM** template to fuse genome with metabolomic and sensor streams later.
7. **Validate the axes:** GWAS loci per axis, **Mendelian randomization** for axis-to-disorder direction, and (per the biotyping landscape doc) projection toward the connectome as causal mediator.
8. **Adopt pangenome-aware variant calling** (vg giraffe, Minigraph-Cactus) for any cohort we sequence; hold graph-based GWAS/PRS as a future frontier.

---

## 12. Honest novelty and gap map

| Claim | Status | How to frame |
|---|---|---|
| Multi-trait genomic factorization | Mature (Genomic SEM, GLEANR) | We extend, not invent; cite generously |
| Per-pathway per-person PRS | Exists (PRSet) | Do not claim as new |
| TF-footprint-restricted, mechanism-anchored per-person axes | **No precedent (June 2026)** | **Claim precisely; our moat** |
| FM-derived priors into neuro PRS | Emerging (Epi-PRS, no neuro yet) | Position as novel application |
| LDGM plus multi-trait factorized PRS | **No published combination** | Concrete methods contribution available |
| Deep autoencoder on sumstat matrix | **Open niche** | Possible methods paper |
| Pangenome-based GWAS/PRS | Nascent | Adopt calling now; frontier for scoring |
| Genome-connectome-phenotype mediation, per-person longitudinal | Asserted, not measured at scale | The multimodal/platform gap (biotyping doc, Section 1) |

---

## 13. Key references (consolidated)

**Factorization and multi-trait:** Grotzinger Genomic SEM, Nat Hum Behav 2019 (doi:10.1038/s41562-019-0566-x); Grotzinger 14-disorder, Nature 2025 (doi:10.1038/s41586-025-09820-3); GLEANR, AJHG 2025 (bioRxiv 2024.11.12.623313); Tanigawa DeGAs, Nat Commun 2019 (doi:10.1038/s41467-019-11953-9); Zhang FactorGo, AJHG 2023 (doi:10.1016/j.ajhg.2023.09.003); Turley MTAG, Nat Genet 2018 (doi:10.1038/s41588-017-0009-4); Demange GWAS-by-subtraction, Nat Genet 2021 (doi:10.1038/s41588-020-00735-5); Ning HDL, Nat Genet 2020 (doi:10.1038/s41588-020-0653-y); Zhang SUPERGNOVA, Genome Biol 2021 (doi:10.1186/s13059-021-02478-w).

**Multi-trait PRS and hybrid sumstat-genotype:** wMT-SBLUP (MacSphere thesis); PRSmix+, PMC11019356; PPRS, Front Genet 2026; PRScsx/SDPRx, PLOS Genet (doi:10.1371/journal.pgen.1012026); S-JointLMM/LS-imputation, PMC10460491; Meta-PRS, bioRxiv 2020.11.27.401141; GEMMA, github.com/genetics-statistics/GEMMA; MTG2.

**Foundation models:** AlphaGenome, Nature 2026 / bioRxiv 2025.06.25.661532; Evo 2, Nature 2026 / arXiv 2502.18638; Borzoi, Nat Genet 2024 (doi:10.1038/s41588-024-02053-6); Borzoi PEFT, bioRxiv 2025.05.26.656171; Borzoi Prime, bioRxiv 2025.06.10.658961; Enformer, Nat Methods 2021 (doi:10.1038/s41592-021-01264-7); Nucleotide Transformer, Nat Methods 2024 (doi:10.1038/s41592-024-02523-z); NTv3, bioRxiv 2025.12.22.695963; HyenaDNA, arXiv:2306.15794; Caduceus, arXiv:2403.03234; GPN, PNAS 2023 (doi:10.1073/pnas.2311219120); GPN-MSA, Nat Biotechnol 2024; Epi-PRS, PNAS 2025 (doi:10.1073/pnas.2419202122); Evo2+AD, medRxiv 2025.09.09.25335438; Sasse and Kelley critique, Nat Genet 2023 (doi:10.1038/s41588-023-01574-w); Karollus critique, Nat Genet 2023 (doi:10.1038/s41588-023-01524-6); GeRS schizophrenia, AJHG 2021 (PMID 33979660).

**Sparse LD / LDGM:** Nowbandegani LDGM, Nat Genet 2023 (doi:10.1038/s41588-023-01487-8); graphld, github.com/oclb/graphld; graphREML, medRxiv 2024.11.04.24316716; score (bcftools plugins), github.com/freeseek/score; ldgm, github.com/awohns/ldgm; VIPRS, AJHG 2025 (doi:10.1016/j.ajhg.2025.04.007).

**Pangenome:** HPRC draft, Nature 2023 (doi:10.1038/s41586-023-05896-x); HPRC Release 2, hgdownload.soe.ucsc.edu/hubs/HPRC; Minigraph-Cactus, PMC10638906; vg, github.com/vgteam/vg; Swave, Nat Genet 2025/2026 (confirm DOI).

**Pathway priors and interpretable factorization:** S-LDSC, Nat Genet 2015 (doi:10.1038/ng.3404) and 2018 (doi:10.1038/s41588-018-0081-4); PRSet, PLoS Genet 2023 (doi:10.1371/journal.pgen.1010624); PolyFun, Nat Genet 2020 (doi:10.1038/s41588-020-00735-5); PolyPred, Nat Genet 2022 (doi:10.1038/s41588-022-01016-z); LDpred-funct, AJHG 2021 (doi:10.1016/j.ajhg.2021.05.014); AnnoPred, PLoS Genet 2017 (doi:10.1371/journal.pgen.1006619); SBayesRC, Nat Genet 2024 (doi:10.1038/s41588-024-01704-y); MAGMA, PLoS Comput Biol 2015 (doi:10.1371/journal.pcbi.1004219); H-MAGMA, Nat Neurosci 2020 (doi:10.1038/s41593-020-0603-0); P-NET, Nature 2021 (doi:10.1038/s41586-021-03922-4); DCell, Nat Methods 2018 (doi:10.1038/nmeth.4627); VEGA, Nat Commun 2021 (doi:10.1038/s41467-021-26017-0); expiMap, Nat Cell Biol 2023; OntoVAE, Bioinformatics 2023 (doi:10.1093/bioinformatics/btad387); f-scLVM/Slalom, Mol Syst Biol 2017; PRS-Net, Genome Res 2025 (doi:10.1101/gr.279115.124); scPRS, Nat Biotechnol 2025 (confirm DOI); PRSet precedent for our axes, plus Finucane S-LDSC.

**Panels:** Pan-UKBB, pan.ukbb.broadinstitute.org; PGC, pgc.unc.edu (CDG3 figshare 10.6084/m9.figshare.30359017); FinnGen R12, finngen.fi; GWAS Catalog, ebi.ac.uk/gwas; IEU OpenGWAS, gwas.mrcieu.ac.uk; MVP, dbGaP phs001672.

**Verification flags.** Newest 2026 Nature-format DOIs (AlphaGenome article DOI, Evo 2 article DOI, scPRS, Swave) should be confirmed against the published record at cite-time; the bioRxiv/arXiv IDs are stable. GLEANR appears under multiple PMC accessions (preprint vs AJHG 2025 final); cite the AJHG version. NeuroGWAS is an internal label, not a public resource.
