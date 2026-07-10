# Master Drive Plan — Genomic Factorization & Multi-Trait PRS Synthesis

**Started:** 2026-06-07 · **Owner:** Shahin (via Cowork) · **Status:** in progress

## Goal
Summarize + expand the four seed docs into one comprehensive landscape on factorizing/embedding GWAS sumstats across related neuro indications, factor PRS, sumstat↔individual-genotype reconciliation, with deep dives on six special interests. Deliverable lives in `04-research/`.

## Seed docs (read ✓)
- `Multi-Trait GWAS Analysis Methods.md` (Downloads) — GLEANR, Genomic SEM, symptom-level factor GWAS, multi-trait PRS (wMT-SBLUP, PRSmix+, PPRS, mPRS, PRScsx/SDPRx), hybrid sumstat+genotype (S-JointLMM, Meta-PRS, mvLMM/GEMMA).
- `AI_ML_dimensional_biotyping_landscape_2026.md` — genomic FMs (Evo2, AlphaGenome, Borzoi, NT, Caduceus, GPN), VAE-PRS, multimodal unified-vs-alignment (COMICAL), recommended architecture.
- `BDNF_TrkB_Neuroplasticity_Axes_Dossier_2026-06-03.md` — crown-jewel factorized PRS: CREB/SREBP TF-region-restricted per-person pathway axes; PRSet/S-LDSC precedent.
- `multiscale-biomarkers.md` — genome→connectome→phenotype prior art; Genomic SEM 5-factor/14-disorder; imaging transcriptomics; MR.

## Research subagents (Sonnet, max 2 parallel)
- [ ] **A — Genomic foundation models for neuro** (AlphaGenome, Evo2, Borzoi/Enformer, NT, Caduceus, GPN-MSA; fine-tuning/LoRA; variant→function for PRS weighting; neuro/brain QTL; latest 2025-26).
- [ ] **B — Sparse LD/precision matrices + Pangenome** (LDGM, graphld, score/bcftools; HPRC pangenome, Minigraph-Cactus, vg; impact on GWAS/PRS/portability).
- [ ] **C — Multi-trait sumstat panels + factorization beyond GLEANR** (Pan-UKBB, PGC cross-disorder, FinnGen, NeuroGWAS; DeGAs, FactorGo, tSVD/NMF, EFA/CFA Genomic SEM).
- [ ] **D — Network/pathway priors + pathway-enriched variant factorization** (S-LDSC, PRSet, PolyFun/PolyPred, LDpred-funct, AnnoPred, MAGMA; P-NET & biologically-informed nets; pathway/ontology VAEs; TF-region factorization).

## Synthesis
- [ ] Merge 4 seed docs + 4 research returns into `Genomic_Factorization_MultiTrait_PRS_Landscape_2026-06-07.md`.
- [ ] BLUF + "if you read one thing"; tables for tool comparisons; Cytognosis-positioning section; honest novelty vs prior art; verification pass on citations.
