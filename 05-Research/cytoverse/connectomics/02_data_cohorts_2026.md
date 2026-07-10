# fMRI data, cohorts, and sample sizes (2025 to 2026)

Coverage of every dataset used as pretraining or downstream evaluation across six papers (Taylor 2026 HCP lifespan, NeuroSTORM, Brain-Semantoks, SLIM-Brain, Omni-fMRI, BrainGFM), plus the HCP family, the ENIGMA fMRI working groups, the OpenNeuro datasets that enter the foundation-model corpora, NeuroGAP-Psychosis, and the Reproducible Brain Corpus.

All counts are cited as in the original publications. Sample-size discrepancies between papers reflect different access dates and QC criteria.

---

## 1. Headline corpora across the six papers

| Paper | Pretraining N | Pretraining frames / sessions | Pretraining cohorts |
|---|---|---|---|
| Taylor (HCP lifespan) | 3 556 individuals (analysis only, no pretraining) | 3 972 gradient sets | BCP, HCP-D, HCP-YA, HCP-A, HBN |
| NeuroSTORM | > 50 000 participants | 28.65 M frames | UKB (40 842), ABCD (9 449), HCP-YA (1 206), HCP-A (725), HCP-D (652) |
| Brain-Semantoks | 39 139 recordings | 39 139 sessions | UKB only |
| SLIM-Brain | ~ 4 129 sessions | 4 129 sessions | HCP, CHCP, AOMIC PIOP1+PIOP2, ABCD |
| Omni-fMRI | ~ 42 250 participants | 49 497 sessions | UKB, AOMIC PIOP1+PIOP2, CHCP, ISYB, ABCD, ABIDE, HCP rest, PPMI |
| BrainGFM | > 25 000 subjects | 60 000 fMRI scans, 400 000 graph samples (8 parcellations) | 19 datasets (see §4 below) |

The BrainGFM 400 000 graph-sample figure is the largest pretraining corpus in the set when measured in graph samples; it is achieved by reusing the same fMRI sessions across 8 different parcellations. In session count it is mid-pack.

---

## 2. Cross-paper dataset usage matrix

| Dataset | NeuroSTORM | Brain-Semantoks | SLIM-Brain | Omni-fMRI | BrainGFM | Taylor |
|---|---|---|---|---|---|---|
| UK Biobank | Pretrain (40 842) | Pretrain (39 139) | | Pretrain (38 372) | | |
| ABCD | Pretrain (9 449) | | Pretrain (subset) | Pretrain (6 720) | Pretrain (11 878 / 35 770) | |
| HCP-YA / HCP-rest | Pretrain (1 206) | | Pretrain (606) | Pretrain (2 424) | | Use (1 068) |
| HCP-D | Pretrain (652) | | | | | Use (650) |
| HCP-A / HCP-Aging | Pretrain (725) | | | | Pretrain (724) | Use (725) |
| HCP-EP (early psychosis) | Downstream (173) | | | | | |
| AOMIC PIOP1 + PIOP2 | | | Pretrain | Pretrain (672 + 720) | Pretrain (210) | |
| CHCP (Chinese HCP) | | | Pretrain | Pretrain (1 224) | | |
| ISYB | | | | Pretrain (520) | | |
| ABIDE I | | | | Pretrain + downstream (2 436) | Pretrain (1 112) | |
| ABIDE II | | Downstream (974) | Downstream | | Semi-external test (1 044) | |
| ADHD200 | Downstream (973) | Downstream | Downstream | | Pretrain + Internal test (973 / 1 382) | |
| ADNI | | | Downstream | Downstream | Pretrain (ADNI 3, 1 071 / 1 410); semi-external (ADNI 2, 1 171 / 1 306) | |
| OASIS3 | | | | | Pretrain + Internal (1 172 / 4 090) | |
| PPMI | | | Downstream | Pretrain + downstream (331 / 1 324) | | |
| BCP | | | | | | Use (343 final) |
| HBN | | Downstream (up to 1 870) | | | Pretrain + Internal (2 228 / 4 039) | Use (770) |
| LEMON | | Downstream | | | Pretrain (213) | |
| SRPBS Japan | | Downstream | | | Pretrain (1 410) | |
| TCP | Downstream (245, OpenNeuro ds006644) | | | | | |
| MND | Downstream (59, OpenNeuro ds005237) | | | | | |
| DMT-HAR-MED | Downstream (40, OpenNeuro ds005874) | | | | | |
| COBRE | Downstream (252) | | | | | |
| HCP-EP | Downstream (173) | | | | | |
| UCLA / UCLA_CNP | Downstream (272) | | | | External test (261) | |
| NSD | | | | Downstream (6, 70 566 sessions) | | |
| StudyForrest | | | | Downstream (20, 71 980 task volumes) | | |
| NKI Rockland (via RBC) | | | | Downstream (717) | | |
| BHRC (via RBC) | | | | Downstream (465) | | |
| SALD | | | | Downstream (493) | | |
| NYU_CUD | | | | | Pretrain (29 / 56) | |
| SubMex_CUD | | | | | Semi-external (135) | |
| SubMex_RTMS | | | | | Pretrain (150) | |
| AURORA | | | | | Pretrain (284, PTSD) | |
| CAM-CAN | | | | | Pretrain (652) | |
| CATD | | | | | Pretrain (127 / 454) | |
| GSP (Genomics Superstruct) | | | | | Pretrain (1 569 / 2 706) | |
| EMBARC | | | | | Pretrain (308, MDD) | |
| HABS (Harvard Aging Brain) | | | | | Pretrain (284 / 1 371) | |
| PREVEND_AD | | | | | Pretrain (343 / 2 427) | |
| REST-META-MDD | | | | | External test (2 379, MDD) | |

Together the foundation-model papers reach ~50 cohorts. Of these, UKB, ABCD, HCP, AOMIC, CHCP, ABIDE, ADHD200, ADNI, PPMI, OASIS3, HBN, and the Reproducible Brain Corpus appear in 2 or more papers; everything else appears in only one.

---

## 3. Disease coverage across papers

| Disorder | Datasets in this review | Papers covering it |
|---|---|---|
| Schizophrenia (SCHZ) | COBRE, SRPBS Japan, UCLA_CNP, HCP-EP (early psychosis) | NeuroSTORM, Brain-Semantoks, BrainGFM |
| Major Depressive Disorder (MDD) | SRPBS, EMBARC, REST-META-MDD, HBN-MDD | Brain-Semantoks, BrainGFM |
| Bipolar Disorder (BP) | UCLA_CNP | BrainGFM |
| Autism Spectrum Disorder (ASD) | ABIDE I, ABIDE II | Brain-Semantoks, SLIM-Brain, Omni-fMRI, BrainGFM |
| ADHD | ADHD200, HBN-ADHD | NeuroSTORM, Brain-Semantoks, SLIM-Brain, BrainGFM |
| Anxiety (ANX) | HBN-ANX | BrainGFM |
| OCD | HBN-OCD | BrainGFM |
| PTSD | AURORA, HBN-PTSD | BrainGFM |
| Oppositional Defiant Disorder (ODD) | HBN-ODD | BrainGFM |
| Provisional Tic Disorder (PTD) | HBN-PTD | BrainGFM |
| Tourette Syndrome (TS) | HBN-TS | BrainGFM |
| Adjustment Disorder (AJD) | HBN-AJD | BrainGFM |
| Persistent Depressive Disorder (PDD) | HBN-PDD | BrainGFM |
| Speech Sound Disorder (SSD) | HBN-SSD | BrainGFM |
| Communication Disorder (CD) | HBN-CD | BrainGFM |
| Specific Learning Disorder (SLD) | HBN-SLD | BrainGFM |
| Language Disorder (LD) | HBN-LD | BrainGFM |
| Intellectual Disability (ID) | HBN-ID | BrainGFM |
| Encopresis (ECP) | HBN-ECP | BrainGFM |
| Enuresis (ENU) | HBN-ENU | BrainGFM |
| Motor Disorder (MD) | HBN-MD | BrainGFM |
| Cocaine Use Disorder (CUD) | NYU_CUD, SubMex_CUD, SubMex_RTMS | BrainGFM |
| Other substance use | DMT-HAR-MED (DMT-harmine vs. placebo) | NeuroSTORM (medication-state classification) |
| Alzheimer's disease (AD) | ADNI 2, ADNI 3, OASIS3, HABS, PREVEND_AD | SLIM-Brain, Omni-fMRI, BrainGFM |
| Mild Cognitive Impairment (MCI) | ADNI 2, ADNI 3, OASIS3 | SLIM-Brain, Omni-fMRI, BrainGFM |
| Dementia (DM) | OASIS3 | BrainGFM |
| Parkinson's disease (PD) | PPMI | SLIM-Brain, Omni-fMRI |
| Motor Neuron Disease (ALS) | MND (OpenNeuro ds005237) | NeuroSTORM |

BrainGFM covers 25 disorders; this is the broadest disease coverage in the literature. HBN drives 17 of those 25 because HBN is a transdiagnostic paediatric resource. ADNI / OASIS3 / HABS / PREVEND_AD drive the AD / MCI / dementia coverage. ABIDE drives ASD; ADHD200 and HBN drive ADHD; SRPBS, REST-META-MDD, and HBN drive MDD; UCLA_CNP drives schizophrenia and bipolar.

---

## 4. BrainGFM dataset breakdown (the most thorough disease catalogue)

Pre-train (19 datasets, > 50 000 samples):

| Dataset | Subjects | Samples | Disease focus |
|---|---|---|---|
| ABCD | 11 878 | 35 770 | multi-disorder developmental |
| ADHD200 | 973 | 1 382 | ADHD |
| ABIDE I | 1 112 | 1 112 | ASD |
| ADNI 3 | 1 071 | 1 410 | AD, MCI |
| AOMIC | 210 | 210 | multiple |
| AURORA | 284 | 284 | PTSD |
| CAM-CAN | 652 | 652 | lifespan healthy aging |
| CATD | 127 | 454 | multi-disorder |
| GSP (Genomics Superstruct) | 1 569 | 2 706 | healthy young adult |
| HCP-Aging | 724 | 724 | healthy aging |
| EMBARC | 308 | 308 | MDD |
| LEMON | 213 | 213 | MDD-adjacent / cognition |
| HABS (Harvard Aging Brain) | 284 | 1 371 | aging / preclinical AD |
| PREVEND_AD | 343 | 2 427 | AD pre-symptomatic |
| SRPBS Japan | 1 410 | 1 410 | multi-site multi-disorder |
| NYU_CUD | 29 | 56 | Cocaine use disorder |
| OASIS3 | 1 172 | 4 090 | dementia |
| HBN | 2 228 | 4 039 | paediatric transdiagnostic (17 disorders) |
| SubMex_RTMS | 150 | 150 | repetitive transcranial magnetic stimulation, CUD |

Internal Test (subsets of pretrain): ADHD200, HBN, OASIS3.
Semi-External Test (cohort-shift only): ABIDE II (1 044), ADNI 2 (1 171), SubMex_CUD (135).
External Test (held-out distribution): UCLA_CNP (261), REST-META-MDD (2 379).

This three-tier split (pretrain / internal / semi-external / external) is the cleanest evaluation protocol in the set and is a model worth copying for any Cytognosis benchmark.

---

## 5. Healthy vs disease coverage by dataset class

| Class | Datasets | Subject count (rough) |
|---|---|---|
| Healthy lifespan, large | UKB, ABCD, HCP-YA, HCP-D, HCP-A, BCP, GSP, CAM-CAN, ISYB, AOMIC, CHCP, NKI Rockland, SALD, HABS, NSD, StudyForrest | > 100 000 in aggregate |
| Healthy paediatric | ABCD, BCP, HCP-D, HBN (subset), AOMIC | ~ 14 000 |
| Healthy aging | HCP-A, OASIS3 (controls), HABS, CAM-CAN, GSP-aging, SALD | ~ 4 000 |
| Neurodevelopmental disorders | ABIDE, ADHD200, HBN | ~ 5 700 |
| Mood / anxiety / trauma | EMBARC, REST-META-MDD, HBN-MDD/ANX/PTSD/AJD/PDD, AURORA, SRPBS-MDD | ~ 8 000 |
| Psychotic disorders | COBRE, HCP-EP, UCLA_CNP, SRPBS-SCZ | ~ 1 000 |
| Substance use | NYU_CUD, SubMex_CUD, SubMex_RTMS, DMT-HAR-MED | ~ 350 |
| Neurodegenerative | ADNI 2 / 3, OASIS3, HABS, PREVEND_AD, PPMI | ~ 3 500 |
| Brazilian high-risk (paediatric) | BHRC (via RBC) | 465 |
| Motor neuron disease | MND (OpenNeuro ds005237) | 59 |

The healthy:disease ratio in the pretraining corpora is roughly 10:1, dominated by UKB (~ 50 000 generally healthy adults) and ABCD (~ 12 000 healthy children). This is a feature, not a bug, since pretraining benefits from the largest available healthy corpus. Disease coverage enters at fine-tuning or downstream evaluation, where transdiagnostic resources (HBN, BrainGFM's 25-disorder catalogue) are the primary contributors.

---

## 6. Lifespan and age coverage

| Age range (years) | Coverage | Primary sources |
|---|---|---|
| 0 to 5 (infant / toddler) | thin | BCP (only), used by Taylor lifespan |
| 5 to 12 (paediatric) | dense | ABCD (9 to 11), HBN (5 to 21), HCP-D (5 to 21) |
| 13 to 21 (adolescent) | dense | HBN, HCP-D, ABCD follow-up |
| 22 to 35 (young adult) | very dense | UKB young, HCP-YA, AOMIC, CHCP, ISYB, GSP |
| 35 to 65 (mid life) | dense | UKB, CAM-CAN, REST-META-MDD, EMBARC, ENIGMA datasets |
| 65 to 90 (older adult) | dense | HCP-A, OASIS3, ADNI, HABS, PREVEND_AD, PPMI, SALD |
| 90 to 100 (oldest old) | thin | Taylor's HCP-A subset only |
| 0.04 to 100 unified | only Taylor | BCP + HCP-D + HCP-YA + HCP-A + HBN |

The Taylor 2026 paper is the only resource in the set that knits the full lifespan into a single normative atlas. Its specific cohort use is:

* BCP (Baby Connectome Project): 16 days to 5 years, 343 individuals after QC, 759 timepoints.
* HCP-D (Human Connectome Project Development): 5.6 to 21.9 years, 650 individuals, 1 206 sessions.
* HCP-YA (HCP Young Adult): 22 to 37 years, 1 068 individuals after QC.
* HCP-A (HCP Aging): 36 to 100 years, 725 individuals.
* HBN (Healthy Brain Network): 5.6 to 21.9 years, 770 individuals after QC.

Total: 3 556 individuals, 3 972 gradient sets, all under standard NIMH / NIH data-use agreements, all openly available.

---

## 7. The HCP family (the canonical cross-cohort spine)

Five HCP-style cohorts dominate cross-cohort fMRI infrastructure. All five are included in Taylor's lifespan atlas; all five are pretraining inputs in NeuroSTORM; HCP-YA (1 206) is in NeuroSTORM, SLIM-Brain (606 used), Omni-fMRI (606 / 2 424), and Brain-Semantoks (no, UKB only). CHCP (the Chinese HCP, Ge et al. 2023) is in SLIM-Brain and Omni-fMRI for demographic diversity.

| Cohort | Age range | TR (s) | Voxel size | N sessions in HCP release |
|---|---|---|---|---|
| BCP, Baby Connectome Project | 16 days to 5 years | 0.8 | 2 mm | ~ 1 000 |
| HCP-D, Development | 5.6 to 21.9 | 0.8 | 2 mm | ~ 1 200 |
| HCP-YA, Young Adult | 22 to 37 | 0.72 | 2 mm | ~ 1 200 |
| HCP-A, Aging | 36 to 100 | 0.8 | 2 mm | ~ 725 |
| CHCP, Chinese HCP | 18 to 79 | 0.72 | 2 mm | 1 224 |

These cohorts share a near-identical acquisition protocol (multiband EPI, ~ 2 mm voxels, ~ 0.72 to 0.8 s TR) and the HCP minimal preprocessing pipeline. They are the closest the field has to a canonical spine for cross-cohort harmonisation, and the Reproducible Brain Corpus extends this discipline to non-HCP cohorts (NKI, BHRC).

---

## 8. ENIGMA fMRI working groups (cross-disorder mega-analysis backbone)

ENIGMA is overwhelmingly known for structural-MRI mega-analyses. The resting-state fMRI working groups that have produced peer-reviewed harmonised analyses, as of 2026, are:

| ENIGMA fMRI working group | Maturity | Notes |
|---|---|---|
| Schizophrenia (SCHZ) rs-fMRI | mature | Multi-site harmonised resting-state mega-analysis published; collaborator network active. |
| Major Depressive Disorder (MDD) rs-fMRI | mature | Veer 2022 mega-analysis (~ 2 000 participants); the most cited ENIGMA rs-fMRI paper. |
| PTSD rs-fMRI | mature | Multi-site rs-fMRI working group active; integrates with AURORA where appropriate. |
| OCD rs-fMRI | mature | Multi-site rs-fMRI working group active; structural mega-analysis was the entry point. |
| Bipolar Disorder (BD) rs-fMRI | nascent | Working group exists but no harmonised mega-analysis dataset yet released; primarily structural. Recommend not listing as on-par with the other four. |
| 22q11.2 deletion / OCD ALS | small | Non-rs-fMRI focuses (structural, task-fMRI in selected subsets). |

For Cytognosis purposes, the four mature rs-fMRI working groups are SCHZ, MDD, PTSD, and OCD. Access is via working-group MoUs, not direct download. Each working group operates under its own data-sharing agreement with contributing sites; the consortium does not host a centralised raw-data repository.

This is consistent with the BrainGFM treatment of psychiatric disorders: of the 25 BrainGFM disorders, 17 come from HBN, the rest from disease-specific cohorts (REST-META-MDD, EMBARC, AURORA, SRPBS, UCLA_CNP). ENIGMA itself does not contribute pretraining data to any of the six papers reviewed here, because of access constraints. This is exactly the gap a Cytognosis ENIGMA-rs-fMRI MoU would close.

---

## 9. OpenNeuro datasets entering the foundation-model corpora

OpenNeuro hosts hundreds of public BIDS-formatted fMRI datasets. The ones that explicitly enter the 2025–2026 foundation-model literature are:

| OpenNeuro ID | Dataset | Used by | N subjects |
|---|---|---|---|
| ds006644 | Transdiagnostic Connectome Project (TCP), Yale / McLean | NeuroSTORM (downstream) | 245 |
| ds005237 | Motor Neuron Disease (MND), Royal Brisbane | NeuroSTORM (downstream) | 59 (44 ALS + 15 controls) |
| ds005874 | DMT-HAR-MED (DMT-harmine vs. placebo) | NeuroSTORM (downstream) | 40 |
| ds000030 | UCLA Consortium for Neuropsychiatric Phenomics | NeuroSTORM, BrainGFM (UCLA_CNP downstream) | 261 |
| ds002785 / ds002790 | AOMIC PIOP1 / PIOP2 | SLIM-Brain, Omni-fMRI (pretrain) | 168 + 180 |
| ds000228 | NSD-related task-fMRI (where applicable) | Omni-fMRI (downstream) | varies |
| ds000113 | StudyForrest auditory movie | Omni-fMRI (downstream) | 20 |

Several other major OpenNeuro datasets are not yet in the foundation-model corpora but are obvious candidates for a Cytognosis cross-cohort dataset:

* CamCAN (Cambridge Centre for Ageing and Neuroscience), already used by BrainGFM via direct release.
* SLIM (Southwest University Longitudinal Imaging Multimodal).
* MyConnectome (single subject deep-phenotyping, Poldrack).
* ds002245 / ds002338 / ds002893 (various clinical fMRI).
* Dozens of OpenNeuro task-fMRI datasets that NeuroSTORM and Omni-fMRI explicitly flag as out-of-scope due to manual-curation cost.

BrainGFM's "Limitations" section is candid that they could not include the full OpenNeuro repository because of manual curation cost, particularly the large task-fMRI subset. This is the largest piece of low-hanging fruit available to anyone with engineering bandwidth: an automated OpenNeuro-to-foundation-model pipeline using BIDS App tooling would unlock thousands of additional sessions for pretraining.

---

## 10. NeuroGAP-Psychosis (cross-ancestry coverage)

NeuroGAP-Psychosis (Stevenson et al. 2019, Stein et al. 2020) is the largest cross-ancestry psychosis genomics + clinical-phenotype study, with > 35 000 participants across Ethiopia, Kenya, South Africa, and Uganda, plus US comparators. It is the canonical resource for African-ancestry psychosis genetics.

Important caveat for the Milestone 1 framing: NeuroGAP-Psychosis is primarily a genotype + clinical phenotype resource. It does not currently have an established rs-fMRI release. If cross-ancestry rs-fMRI coverage is the actual goal, the candidate datasets are:

* AFRINEURO and the African Brain Health Initiative (in development).
* BHRC (Brazilian High-Risk Cohort), accessible via the Reproducible Brain Corpus, used by Omni-fMRI.
* SRPBS Japan (multi-site Japanese rs-fMRI), used by Brain-Semantoks and BrainGFM.
* CHCP (Chinese Human Connectome Project), used by SLIM-Brain and Omni-fMRI.
* SubMex_CUD and SubMex_RTMS (Mexican cohorts on cocaine use disorder), used by BrainGFM.

NeuroGAP can stay as the genotype + phenotype anchor for the Cytognosis substrate, but the rs-fMRI cross-ancestry slot needs at least one of CHCP, SRPBS, BHRC, or SubMex to ship.

---

## 11. Reproducible Brain Corpus (RBC) (the FAIR exemplar)

RBC (Shafiei et al. 2025) is the only resource in the set that publishes its preprocessed pretraining derivatives as a BIDS-Derivatives release with persistent DOIs and DataLad versioning. Currently hosts:

* NKI Rockland (717 subjects), used by Omni-fMRI for age and education regression.
* BHRC (Brazilian High-Risk Cohort, 465 subjects), used by Omni-fMRI for sex classification.
* PNC, HBN, HCP-D, BHRC, NKI all harmonised under one QSIPrep + fMRIPrep + sMRIPrep pipeline version with deterministic container hashes.

RBC is the model Cytognosis should explicitly imitate.

---

## 12. Sex, age, multi-site demographics

* **Sex:** UKB, ABCD, HBN, HCP-* are all sex-balanced or close to balanced. BrainGFM explicitly constructs sex-balanced subsets for every downstream classification task to prevent label leakage from sex. NeuroSTORM and Omni-fMRI evaluate sex prediction in-distribution and out-of-distribution as a baseline benchmark.
* **Age:** the lifespan from 16 days to 100 years is covered, but density is not uniform. The 0–5 year band has only BCP. The 90+ band has only HCP-A's tail. The mid-life (35 to 60) band is dense in UKB but thin in HCP-family cohorts.
* **Multi-site harmonisation:** UKB, ABCD, HCP, AOMIC, CHCP, ISYB, ABIDE, ADHD200, ADNI, OASIS3, HBN are all multi-site by design. SRPBS Japan and REST-META-MDD are explicit harmonisation testbeds (Yamashita 2019). Foundation models in this review delegate site / scanner harmonisation to either ComBat-family methods (applied at use time) or to the model's own representation learning (no explicit harmonisation).
* **Race / ethnicity:** ABCD has the most explicit demographic annotation. UKB is overwhelmingly white European-ancestry. HCP-YA is mostly white European-ancestry US. CHCP and SRPBS contribute East Asian samples; BHRC and SubMex contribute Latin American; AURORA and HBN have the most US racial diversity. The cross-ancestry gap is the field's most serious data-coverage problem and is explicitly flagged in BrainGFM and Omni-fMRI.

---

## 13. Diversity and coverage gaps to flag for Cytognosis Milestone 1

* **African-ancestry rs-fMRI is missing.** NeuroGAP-Psychosis is genotype-only.
* **Latin-American rs-fMRI is thin.** BHRC (via RBC) and SubMex (via BrainGFM) are the only entries.
* **South-Asian rs-fMRI is essentially absent.** No reviewed paper uses an Indian-cohort fMRI dataset.
* **Indigenous and Pacific-Islander populations are absent.** No reviewed paper covers them.
* **Bipolar Disorder rs-fMRI is thin.** UCLA_CNP (49 / 55 in BrainGFM) is the only entry. ENIGMA-BD rs-fMRI working group is nascent.
* **Substance use disorders (other than cocaine) are absent.** No alcohol, opioid, methamphetamine cohorts in the reviewed papers.
* **Eating disorders, sleep disorders, somatoform disorders are absent.**
* **Task-fMRI is treated as evaluation only, not pretraining.** The largest body of OpenNeuro task-fMRI is unused.
* **No multi-modal pretraining yet.** Simultaneous EEG-fMRI, ophys-fMRI, and DTI-fMRI corpora exist (e.g., StudyForrest extension, PNC EEG-MRI) but are not entering pretraining yet.

These are the cleanest places where a Cytognosis cross-cohort substrate could measurably extend the field.

---

## 14. Recommended Cytognosis cross-cohort substrate for Milestone 1

Given the above, the defensible Milestone 1 commitment is:

* **Healthy lifespan spine:** HCP-YA + HCP-A + HCP-D + BCP + ABCD + UKB (subject to access). This single combination spans 16 days to 100 years and is what the foundation models already train on; aligning the Cytognosis substrate to this spine guarantees out-of-the-box compatibility.
* **Disease coverage via mature rs-fMRI consortia:** ENIGMA SZ + MDD + PTSD + OCD (via working-group MoUs); HBN for paediatric transdiagnostic; ABIDE for ASD; ADHD200 for ADHD; ADNI / OASIS3 / HABS for AD; PPMI for PD.
* **Cross-ancestry (rs-fMRI):** CHCP and SRPBS for East Asian; BHRC for Latin American; SubMex for Latin American substance use. Hold a slot open for AFRINEURO when it ships.
* **OpenNeuro datasets (BIDS-native, immediate):** TCP, MND, AOMIC PIOP1+PIOP2, UCLA_CNP, plus a curated batch of task-fMRI datasets (NSD, StudyForrest, the HCP task release). These are all ds-IDed and DataLad-distributable today.
* **NeuroGAP-Psychosis** as the genotype + clinical phenotype layer rather than the imaging layer.
* **Reproducible Brain Corpus** as the harmonisation gold standard to imitate (BIDS-Derivatives + DataLad + persistent DOI per cohort).

If all of the above lands at v0.1, Cytognosis ships ~3 500 to 5 000 BIDS rs-fMRI scans, ~4 mature disorder coverage areas, and is the only public substrate in the world with FAIR-compliant cross-cohort fMRI plus genotype plus clinical phenotype in a single release.
