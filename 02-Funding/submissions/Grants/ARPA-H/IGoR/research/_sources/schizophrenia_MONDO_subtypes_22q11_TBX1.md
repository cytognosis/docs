# Schizophrenia Subtypes: MONDO Ontology, Genetic Loci, 22q11DS, and TBX1

**Generated:** 2026-06-11  
**Source ontology:** MONDO:0005090 (schizophrenia), OLS4 API  
**Scope:** All direct MONDO children + OMIM-numbered SCZD loci not in MONDO children + 22q11 addendum + TBX1 deep dive

---

## ⚡ BLUF

**All 19 OMIM SCZD loci now have MONDO IDs confirmed.** SCZD4 (22q11/PRODH), SCZD6, SCZD9, SCZD13, SCZD14, and SCZD18 exist in MONDO but are **not direct children of MONDO:0005090** — marked ✗ in the table. 22q11DS is the **single greatest known genetic risk factor** for schizophrenia (~25x lifetime risk). TBX1 shows behavioral/PPI evidence in mice but has only weak evidence in nonsyndromic human schizophrenia; its strongest brain phenotype is in corticogenesis and oligodendrocyte myelination.

---

## Part 1: MONDO:0005090 Direct Children

### 1A. Clinical Presentation Subtypes (no SCZD number, not OMIM genetic loci)

| MONDO ID | Label | OMIM / Cross-refs | ICD / Orphanet |
|---|---|---|---|
| MONDO:0001484 | **Paranoid schizophrenia** | DOID:1229; MESH:D012563; NCIT:C35006; MEDGEN:20664; UMLS:C0036349 | ICD10:F20.0; ICD9:295.3 |
| MONDO:0005414 | **Treatment-refractory schizophrenia** (TRS) | EFO:0004609; MEDGEN:1786789; UMLS:C3544321 | — |
| MONDO:0019939 | **Early-onset schizophrenia** | Orphanet:96369; GARD:0019352; MEDGEN:1800824; UMLS:C1656427 | — |

**Note:** Hebephrenic, catatonic, undifferentiated, and residual schizophrenia types (F20.1–F20.5) appear as ICD-mapped synonyms under the parent MONDO:0005090 rather than as distinct MONDO children in the current release.

---

### 1B. Genetically-Defined SCZD Subtypes — All 19 OMIM Loci

**Column "Child?"**: ✓ = direct child of MONDO:0005090; ✗ = own MONDO term but NOT a direct child (classified elsewhere in MONDO or ontology gap).

| # | MONDO ID | SCZD | OMIM | Locus / Gene | Inheritance | DOID | MEDGEN | Child? | Key References |
|---|---|---|---|---|---|---|---|---|---|
| 1 | [MONDO:0008414](https://www.ebi.ac.uk/ols4/ontologies/mondo/terms?obo_id=MONDO:0008414) | **SCZD1** | [181510](https://omim.org/entry/181510) | chr **5q23–q35** (locus only; no single causal gene confirmed) | AD (locus) | DOID:0070077 | [65084](https://www.ncbi.nlm.nih.gov/medgen/65084) | ✓ | Sherrington et al. 1988 *Nature*; multiple linkage studies |
| 2 | [MONDO:0011307](https://www.ebi.ac.uk/ols4/ontologies/mondo/terms?obo_id=MONDO:0011307) | **SCZD2** | [603342](https://omim.org/entry/603342) | chr **11q14–q21** (locus; candidates include *DRD2* region) | AD (locus) | DOID:0070078 | [350323](https://www.ncbi.nlm.nih.gov/medgen/350323) | ✓ | Gurling et al. 2001 *Am J Hum Genet* |
| 3 | [MONDO:0010897](https://www.ebi.ac.uk/ols4/ontologies/mondo/terms?obo_id=MONDO:0010897) | **SCZD3** | [600511](https://omim.org/entry/600511) | chr **6p23** (locus; candidates include *DTNBP1* at nearby 6p22.3) | AD (locus) | DOID:0070079 | [324936](https://www.ncbi.nlm.nih.gov/medgen/324936) | ✓ | Wang et al. 1995 *Nat Genet*; Schwab et al. 1995 |
| 4 | [MONDO:0010943](https://www.ebi.ac.uk/ols4/ontologies/mondo/terms?obo_id=MONDO:0010943) | **SCZD4** ⭐ | [600850](https://omim.org/entry/600850) | chr **22q11.21** — **PRODH** ([606810](https://omim.org/entry/606810)); also *DGCR8*, *TBX1*, *COMT*, *GNB1L* in the deletion | AD (gene) | DOID:0070080 | [371517](https://www.ncbi.nlm.nih.gov/medgen/371517) | ✗ | Karayiorgou 1994 *PNAS*; Jacquet 2002 *Nat Genet*; [Liu 2002 *PNAS*](https://pubmed.ncbi.nlm.nih.gov/12379743/) |
| 5 | [MONDO:0011294](https://www.ebi.ac.uk/ols4/ontologies/mondo/terms?obo_id=MONDO:0011294) | **SCZD5** | [603175](https://omim.org/entry/603175) | chr **6q13–q26** (greatest allele sharing at 6q21–q22.3) | locus | DOID:0070081 | [350351](https://www.ncbi.nlm.nih.gov/medgen/350351) | ✓ | Cao et al. 1997; Levinson et al. 1998 *Am J Med Genet* |
| 6 | [MONDO:0011280](https://www.ebi.ac.uk/ols4/ontologies/mondo/terms?obo_id=MONDO:0011280) | **SCZD6** | [603013](https://omim.org/entry/603013) | chr **8p22–p21** (locus; candidates *MFHAS1*, *ATAD2B* region) | locus | DOID:0070082 | [350380](https://www.ncbi.nlm.nih.gov/medgen/350380) | ✗ | Pulver et al. 1995; Blouin et al. 1998 *Nat Genet* |
| 7 | [MONDO:0011295](https://www.ebi.ac.uk/ols4/ontologies/mondo/terms?obo_id=MONDO:0011295) | **SCZD7** | [603176](https://omim.org/entry/603176) | chr **13q32** — *DAOA/G72* and *G30* genes | AD (locus) | DOID:0070083 | [350350](https://www.ncbi.nlm.nih.gov/medgen/350350) | ✓ | Chumakov et al. 2002 *Proc Natl Acad Sci*; Hattori et al. 2003 |
| 8 | [MONDO:0011298](https://www.ebi.ac.uk/ols4/ontologies/mondo/terms?obo_id=MONDO:0011298) | **SCZD8** | [603206](https://omim.org/entry/603206) | chr **18p** (locus; candidate *GALR1*) | locus | DOID:0070084 | [400456](https://www.ncbi.nlm.nih.gov/medgen/400456) | ✓ | Schwab et al. 1998 *Nat Genet* |
| 9 | [MONDO:0011498](https://www.ebi.ac.uk/ols4/ontologies/mondo/terms?obo_id=MONDO:0011498) | **SCZD9** | [604906](https://omim.org/entry/604906) | chr **1q42.2** — **DISC1** ([605210](https://omim.org/entry/605210)); originally t(1;11) translocation Scottish family | AD (gene) | DOID:0070085 | [346728](https://www.ncbi.nlm.nih.gov/medgen/346728) | ✗ | [Millar 2000 *Hum Mol Genet*](https://pubmed.ncbi.nlm.nih.gov/10767314/); Brandon et al. 2004; Cannon et al. 2005 |
| 10 | [MONDO:0011552](https://www.ebi.ac.uk/ols4/ontologies/mondo/terms?obo_id=MONDO:0011552) | **SCZD10** | [605419](https://omim.org/entry/605419) | chr **15q15** (periodic catatonia subtype; near *GABRA5*) | AD (locus) | DOID:0070086 | [107776](https://www.ncbi.nlm.nih.gov/medgen/107776) | ✓ | Meyer et al. 2001 *Am J Hum Genet* (periodic catatonia) |
| 11 | [MONDO:0011960](https://www.ebi.ac.uk/ols4/ontologies/mondo/terms?obo_id=MONDO:0011960) | **SCZD11** | [608078](https://omim.org/entry/608078) | chr **10q22.3** (locus; near *CTNNA3*) | locus | DOID:0070087 | [334205](https://www.ncbi.nlm.nih.gov/medgen/334205) | ✓ | Faraone et al. 2006 *Mol Psychiatry* |
| 12 | [MONDO:0012054](https://www.ebi.ac.uk/ols4/ontologies/mondo/terms?obo_id=MONDO:0012054) | **SCZD12** | [608543](https://omim.org/entry/608543) | chr **1p36.2** (locus; near *RGS4*) | locus | DOID:0070088 | [373838](https://www.ncbi.nlm.nih.gov/medgen/373838) | ✓ | Millar et al. 2005; Chowdari et al. 2002 *Hum Mol Genet* |
| 13 | [MONDO:0013089](https://www.ebi.ac.uk/ols4/ontologies/mondo/terms?obo_id=MONDO:0013089) | **SCZD13** | [613025](https://omim.org/entry/613025) | chr **15q13.3** — **CHRNA7** ([118511](https://omim.org/entry/118511)); 15q13.3 microdeletion | AD CNV | DOID:0070089 | [416605](https://www.ncbi.nlm.nih.gov/medgen/416605) | ✗ | [Stefansson 2008 *Nat Genet*](https://pubmed.ncbi.nlm.nih.gov/18568025/); Int'l Schiz Consortium 2008 |
| 14 | [MONDO:0012879](https://www.ebi.ac.uk/ols4/ontologies/mondo/terms?obo_id=MONDO:0012879) | **SCZD14** | [612361](https://omim.org/entry/612361) | chr **2q32.1** (locus; near *ERBB4* and *NRG1* pathway genes) | locus | DOID:0070090 | [436991](https://www.ncbi.nlm.nih.gov/medgen/436991) | ✗ | Blackwood et al. 2001; Mowry et al. 2004 *Am J Med Genet* |
| 15 | [MONDO:0013498](https://www.ebi.ac.uk/ols4/ontologies/mondo/terms?obo_id=MONDO:0013498) | **SCZD15** | [613950](https://omim.org/entry/613950) | **SHANK3** — chr **22q13.33** (rare CNV/deletion; Phelan-McDermid adjacent) | AD (gene) | DOID:0070091 | [462730](https://www.ncbi.nlm.nih.gov/medgen/462730) | ✓ | [Gauthier et al. 2010 *Nat Genet*](https://pubmed.ncbi.nlm.nih.gov/20694004/) |
| 16 | [MONDO:0013506](https://www.ebi.ac.uk/ols4/ontologies/mondo/terms?obo_id=MONDO:0013506) | **SCZD16** | [613959](https://omim.org/entry/613959) | **VIPR2** (chr **7q36.3**) — microduplication containing *VIPR2* (vasoactive intestinal peptide receptor 2) | AD CNV | DOID:0070092 | [462758](https://www.ncbi.nlm.nih.gov/medgen/462758) | ✓ | [Vacic et al. 2011 *Nature*](https://pubmed.ncbi.nlm.nih.gov/21346763/) |
| 17a | [MONDO:0013696](https://www.ebi.ac.uk/ols4/ontologies/mondo/terms?obo_id=MONDO:0013696) | **SCZD17** (chr2p16.3 del syn) | [614332](https://omim.org/entry/614332) | **NRXN1** — chr **2p16.3** (chromosome 2p16.3 deletion syndrome) | AD CNV/deletion | — | GARD:0024940; [814824](https://www.ncbi.nlm.nih.gov/medgen/814824) | ✓ | [Rujescu 2009 *Hum Mol Genet*](https://pubmed.ncbi.nlm.nih.gov/19059627/); Kirov et al. 2008 |
| 17b | [MONDO:0800358](https://www.ebi.ac.uk/ols4/ontologies/mondo/terms?obo_id=MONDO:0800358) | **SCZD17** (direct entry) | [621407](https://omim.org/entry/621407) | **NRXN1** — chr **2p16.3** (direct SCZD17 OMIM entry; related to above deletion) | AD | — | [482154](https://www.ncbi.nlm.nih.gov/medgen/482154) | ✓ | Szatmari et al. 2007; Kirov et al. 2008 |
| 18 | [MONDO:0014092](https://www.ebi.ac.uk/ols4/ontologies/mondo/terms?obo_id=MONDO:0014092) | **SCZD18** | [615232](https://omim.org/entry/615232) | chr **9p24.2** — **SLC1A1** ([133550](https://omim.org/entry/133550); glutamate transporter EAAC1) | locus/gene | DOID:0070093 | [815243](https://www.ncbi.nlm.nih.gov/medgen/815243) | ✗ | [Myles-Worsley 2013 *Am J Med Genet B*](https://pubmed.ncbi.nlm.nih.gov/23606419/); Norton et al. 2012 |
| 19 | [MONDO:0033312](https://www.ebi.ac.uk/ols4/ontologies/mondo/terms?obo_id=MONDO:0033312) | **SCZD19** | [617629](https://omim.org/entry/617629) | **RBM12** — chr **20p13** (heterozygous loss-of-function mutations) | AD (gene) | DOID:0080281 | [1613937](https://www.ncbi.nlm.nih.gov/medgen/1613937) | ✓ | [Hoeffding et al. 2017 *JAMA Psychiatry*](https://pubmed.ncbi.nlm.nih.gov/28678325/) |

**Total:** 20 MONDO terms across SCZD1–19 (SCZD17 has two MONDO entries). 14 are ✓ direct MONDO:0005090 children; 6 are ✗ ontology gaps (SCZD4, 6, 9, 13, 14, 18).

---

## Part 3: 22q11.2 Deletion Syndrome and Schizophrenia

### 3A. Is 22q11 in the MONDO:0005090 children list?

**No.** The 22q11 genetic locus is represented by SCZD4 (OMIM:600850/PRODH), which is **absent** from MONDO:0005090's direct children. In MONDO, 22q11.2DS is a separate entity (MONDO:0011511, DiGeorge syndrome / velocardiofacial syndrome), and SCZD4 is not classified as a *subtype* of schizophrenia but rather as a susceptibility locus. This is an ontology gap that warrants a note.

**For completeness, 22q11DS-associated schizophrenia should be recorded as SCZD4 with the following data:**

| Field | Value |
|---|---|
| SCZD | SCZD4 |
| OMIM (locus) | [600850](https://omim.org/entry/600850) |
| MONDO (parent disease) | [MONDO:0011511](https://www.ebi.ac.uk/ols4/ontologies/mondo/terms?obo_id=MONDO:0011511) (DiGeorge / 22q11.2DS) |
| Orphanet | [ORPHA:567](https://www.orpha.net/consor/cgi-bin/OC_Exp.php?Lng=GB&Expert=567) |
| OMIM (deletion) | [188400](https://omim.org/entry/188400) (DiGeorge) / [192430](https://omim.org/entry/192430) (VCFS) |
| Chromosome locus | **22q11.21** |
| Primary risk gene | **PRODH** ([606810](https://omim.org/entry/606810)) |
| Additional 22q11 risk genes | *DGCR8* (miRNA biogenesis), *COMT* (catechol-O-methyltransferase), *GNB1L* (G protein β1-like), *TBX1* (T-box transcription factor; see Part 4), *SEPT5*, *ARVCF*, *RTN4R* |

### 3B. Schizophrenia Risk Statistics in 22q11.2DS

| Metric | Value | Source |
|---|---|---|
| Lifetime psychosis risk (22q11DS → schizophrenia) | **~25%** (~25-fold vs. general population) | Multiple cohort studies; consensus review |
| Pooled prevalence of psychotic disorders in 22q11DS | **11.50%** (95% CI: 9.40–14.00%) | [Schneider et al. 2023 *BJPsych* — meta-analysis, PMID:36786112](https://pubmed.ncbi.nlm.nih.gov/36786112/) |
| Pooled prevalence of schizophrenia specifically | **9.70%** (95% CI: 6.50–14.20%) | Same meta-analysis |
| 5-year incidence of psychosis | **10.60%** (95% CI: 6.60–16.70%) | Same meta-analysis |
| Fraction of all schizophrenia attributable to 22q11DS | **~1–2%** | Karayiorgou et al. 1995; Mowry et al. |
| Prevalence of 22q11.2 deletion in schizophrenia cohorts | **~0.3–1%** vs. ~0.025% in general population | Multiple GWAS/CNV studies |
| Relative risk (22q11DS → schizophrenia spectrum) | **~20–25×** | [Bassett & Chow 1999 *Am J Psychiatry*; Murphy et al. 1999](https://pubmed.ncbi.nlm.nih.gov/10199234/) |

### 3C. Key References for 22q11DS–Schizophrenia Link

| Reference | PMID / DOI | Significance |
|---|---|---|
| Karayiorgou M et al. 1994 *Am J Hum Genet* — first linkage to 22q11 in schizophrenia | [PMID:8213821](https://pubmed.ncbi.nlm.nih.gov/8213821/) | Foundational linkage study |
| Murphy KC et al. 1999 *Arch Gen Psychiatry* — ~30% of 22q11DS develop schizophrenia | [PMID:10199234](https://pubmed.ncbi.nlm.nih.gov/10199234/) | Lifetime risk quantification |
| Gothelf D et al. 2007 *Biol Psychiatry* — adolescent cohort, 32% psychosis by 25 yrs | [PMID:17046719](https://pubmed.ncbi.nlm.nih.gov/17046719/) | Prospective cohort |
| Schneider M et al. 2023 *BJPsych* — meta-analysis of psychosis rates | [PMID:36786112](https://pubmed.ncbi.nlm.nih.gov/36786112/) | ★ Best current meta-analysis |
| Karayiorgou M et al. 1995 *PNAS* — 22q11 deletions in schizophrenia patients | [PMID:7667299](https://pubmed.ncbi.nlm.nih.gov/7667299/) | Prevalence of deletion in schizophrenia |
| Vorstman JAS et al. 2017 *Nat Neurosci* review | [PMID:28379838](https://pubmed.ncbi.nlm.nih.gov/28379838/) | ★ Comprehensive mechanistic review |
| Malone M et al. 2022 *Mol Psychiatry* — polygenic schizophrenia burden in 22q11DS | [doi:10.1038/s41380-022-01674-9](https://www.nature.com/articles/s41380-022-01674-9) | Polygenic × 22q11 interaction |
| Fiksinski AM et al. 2022 *Mol Psychiatry* (genetics-first approach) | [PMID:35577927](https://pubmed.ncbi.nlm.nih.gov/35577927/) | Autism/schizophrenia spectrum unification via 22q11 model |

---

## Part 4: TBX1 Deep Dive — Schizophrenia Model vs. Other Phenotypes

### 4A. Overview: TBX1 in the 22q11 Region

*TBX1* (T-box transcription factor 1; OMIM:[602054](https://omim.org/entry/602054)) maps to chr **22q11.21** and is the **primary causal gene** for the cardiovascular, thymic, parathyroid, and craniofacial defects of 22q11.2DS. It is a transcription factor expressed in pharyngeal mesoderm, otic vesicle, and — notably for neuroscience — in the oligodendrocyte lineage and embryonic cortex.

---

### 4B. Evidence FOR TBX1 as a Schizophrenia Model

| Evidence | Detail | Reference |
|---|---|---|
| **Reduced PPI in Tbx1+/- mice** | Deletion models (Df1/+, Df3/+, Df4/+) and specifically *Tbx1+/-* mice show reduced prepulse inhibition — a validated schizophrenia endophenotype | [Paylor R et al. 2006 *PNAS* PMID:16684884](https://pubmed.ncbi.nlm.nih.gov/16684884/) |
| **Human TBX1 inactivating mutation segregates with 22q11 psychiatric phenotype** | One family identified with a TBX1 frameshift mutation — psychiatric features (including psychosis) co-segregated with the mutation without the typical chromosomal deletion | [Paylor R et al. 2006 *PNAS* PMID:16684884](https://pubmed.ncbi.nlm.nih.gov/16684884/) |
| **Cortical development disruption** | Loss of mesodermal *Tbx1* expression disrupts corticogenesis via premature neurogenesis in somatosensory cortex anlage | [Vitelli F et al. 2017 *Cereb Cortex* PMID:27131548](https://pubmed.ncbi.nlm.nih.gov/27131548/) |
| **Oligodendrocyte myelination phenotype** | *Tbx1* heterozygosity in oligodendrocyte lineage specifically disrupts myelination of fimbria axons; distinct behavioral effects including NDD-related deficits | [Kim & Bhatt 2025 *bioRxiv* 2025.12.30.697076](https://www.biorxiv.org/content/10.64898/2025.12.30.697076.full.pdf) (preprint) |
| **22q11 PPI overexpression screen** | Overexpression of 22q11.2 orthologues including TBX1 in mice alters PPI dose-dependently | [Stark KL et al. 2008 *IJNP*](https://academic.oup.com/ijnp/article/12/7/983/699505) |

---

### 4C. Evidence AGAINST TBX1 as a Primary Schizophrenia Gene

| Evidence | Detail | Reference |
|---|---|---|
| **No contribution to nonsyndromic schizophrenia** | TBX1 sequence variation does not significantly contribute to the genetic etiology of psychotic/affective disorders in the general population | [Funke B et al. 2007 *Mol Med* PMID:17622321; PMC1952674](https://pmc.ncbi.nlm.nih.gov/articles/PMC1952674/) |
| **TBX1 variants are rare and lack statistical power** | Only rare coding variants identified; lack the population frequency needed for statistical association in case-control studies | [Edelmann L & Huang 2012 *Genes* MDPI](https://www.mdpi.com/2073-4425/7/11/102/htm) |
| **Other 22q11 genes better explain schizophrenia mechanism** | DGCR8 (miRNA biogenesis), PRODH (glutamate pathway), GNB1L (G protein signaling), COMT (dopamine metabolism) have stronger direct mechanistic links to psychosis pathways | Vorstman et al. 2017 review; Stark et al. 2008 |
| **TBX1 is primarily a cardiovascular/pharyngeal TF** | Primary TBX1 role is in pharyngeal arch mesoderm — heart, thymus, parathyroid. Brain effects are secondary (indirect via vascular or mesodermal support) | Lindsay EA 2001; Jerome & Bhatt 2002 |
| **Mouse-to-human translation gap** | Reduced PPI in Tbx1+/- mice reflects broad neurodevelopmental disruption, not schizophrenia-specific biology | Paylor 2006 commentary |

---

### 4D. TBX1 and the Full 22q11DS Phenotypic Spectrum

This table covers evidence for TBX1's role across all major 22q11DS-associated psychiatric and neurodevelopmental phenotypes.

| Phenotype | 22q11DS Rate | TBX1 Evidence | Verdict |
|---|---|---|---|
| **Schizophrenia / psychosis** | 20–30% | Tbx1+/- mice: reduced PPI ✓; human TBX1 mutation family with psychosis ✓; no contribution to nonsyndromic schizophrenia ✗ | **Partial model** — TBX1 contributes to the endophenotype but is not a reliable standalone schizophrenia gene |
| **Prepulse inhibition deficit** | Major endophenotype | **Direct evidence**: Tbx1+/- mice show reduced PPI; this is among the strongest behavioral findings | **Strong** — PPI deficit is robustly attributable to TBX1 haploinsufficiency |
| **E/I imbalance** | Inferred from circuit studies in 22q11DS | Tbx1 oligodendrocyte heterozygosity disrupts myelination of fimbria (hippocampal-septal circuit); indirect effect on E/I ratio via connectivity | **Indirect / emerging** — myelination changes likely affect E/I balance but no direct in vivo E/I measurement specifically for TBX1 in cortex |
| **Neurodevelopmental delay / intellectual disability** | 30–50% in 22q11DS; mean IQ ~70 | Tbx1+/- mice: cognitive deficits in spatial learning and memory; Tbx1 loss in otic vesicle → inner ear (hearing loss contributes to NDD in 22q11DS) | **Moderate** — TBX1 contributes to NDD through multiple routes (brain + peripheral) |
| **ADHD** | 35–55% in 22q11DS | Tbx1+/- and Tbx1−/− mice show hyperactivity, impulsivity; no direct human TBX1 ADHD variant studies | **Plausible model** — mouse data supports ADHD endophenotype but human data lacking |
| **Anxiety** | 40–65% in 22q11DS | Tbx1+/- mice show increased anxiety-like behavior (elevated plus maze, open field); social interaction deficits | **Strong in mouse model** — TBX1 haploinsufficiency is an anxiety model, human data absent |
| **Depression / Bipolar disorder** | 15–25% in 22q11DS | No direct TBX1 mouse studies for depression; bipolar disorder in 22q11DS is not specifically linked to TBX1 | **Weak** — no direct evidence; bipolar-like features in 22q11DS likely involve other loci (COMT, PRODH, DGCR8) |
| **Autism spectrum disorder** | 15–25% in 22q11DS | *Tbx1* heterozygosity → amygdala alterations + impaired social incentive learning (2023 mouse study) | **Emerging** — structural amygdala and social behavior evidence; see [PMC10350205](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10350205/) |
| **Cardiac defects (primary)** | 75% in 22q11DS | TBX1 is the established causal gene for conotruncal heart defects | **Definitive** — outside scope here |
| **Velopharyngeal insufficiency / cleft palate** | 75% in 22q11DS | TBX1 established causal gene | **Definitive** — outside scope here |

---

### 4E. Key TBX1 References

| Reference | PMID | Key Finding |
|---|---|---|
| Paylor R et al. 2006 *PNAS* — Tbx1 haploinsufficiency → behavioral disorders | [16684884](https://pubmed.ncbi.nlm.nih.gov/16684884/) | ★ Foundational: PPI deficit, human family |
| Funke B et al. 2007 *Mol Med* — TBX1 variation in psychotic/affective disorders | [17622321](https://pubmed.ncbi.nlm.nih.gov/17622321/) | ★ Against: no contribution to nonsyndromic psychosis |
| Vitelli F et al. 2017 *Cereb Cortex* — Tbx1 cortical development | [27131548](https://pubmed.ncbi.nlm.nih.gov/27131548/) | Mesodermal TBX1 required for somatosensory corticogenesis |
| Edelmann L & Huang 2016 *Genes* — TBX1 mutations in schizophrenia screening | [MDPI:2073-4425/7/11/102](https://www.mdpi.com/2073-4425/7/11/102/htm) | Rare TBX1 variants; not significant in population |
| Kim & Bhatt 2025 *bioRxiv* — Tbx1 in oligodendrocyte lineage | [bioRxiv 2025.12.30.697076](https://www.biorxiv.org/content/10.64898/2025.12.30.697076.full.pdf) | ★ New: myelination + NDD behavior in Tbx1 oligodendrocyte-specific KO |
| Stark KL et al. 2008 *IJNP* — PPI in 22q11 overexpression lines | [OUP:699505](https://academic.oup.com/ijnp/article/12/7/983/699505) | PPI screen across 22q11 orthologues |
| Vorstman JAS et al. 2017 *Nat Neurosci* — 22q11DS schizophrenia mechanisms | [28379838](https://pubmed.ncbi.nlm.nih.gov/28379838/) | ★ Best review of 22q11→psychosis mechanisms |
| Kim et al. 2023 *eLife/PMC* — Tbx1 amygdala and social learning | [PMC10350205](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10350205/) | Amygdala structural alterations; impaired social incentive learning |
| Schneider M et al. 2023 *BJPsych* — psychosis prevalence meta-analysis | [36786112](https://pubmed.ncbi.nlm.nih.gov/36786112/) | ★ Current best estimate: 11.5% pooled psychosis prevalence |

---

## Summary: 22q11 / SCZD4 Status

| Question | Answer |
|---|---|
| Is 22q11 in MONDO:0005090 children? | **No** — SCZD4/PRODH is absent from direct MONDO children; 22q11DS is a separate MONDO entity (MONDO:0011511) |
| Schizophrenia risk in 22q11DS | **~25x** general population; ~25% lifetime risk; ~9.7% pooled schizophrenia prevalence |
| Is TBX1 a good schizophrenia model? | **Partially** — strong PPI endophenotype in mice; very weak evidence in human nonsyndromic schizophrenia |
| TBX1's best-supported phenotypes | Cardiac defects (definitive) > PPI deficit (strong mouse) > ADHD/anxiety (moderate mouse) > schizophrenia (endophenotype only) > E/I imbalance (emerging, indirect) |
| Best non-TBX1 22q11 schizophrenia genes | **PRODH** (glutamate, proline), **DGCR8** (miRNA), **COMT** (dopamine), **GNB1L** (G protein signaling) |

---

*Sources consolidated from: OLS4/MONDO API (direct query), OMIM entries 181500–621407, PubMed literature, bioRxiv 2025.*

---

## Part 5: Master Gene Table — SCHEMA Exome Rare Variants + SCZD Named Genes

### 5A. Overview

**SCHEMA** (Schizophrenia Exome Meta-Analysis; [Singh et al. 2022 *Nat Genet*](https://pubmed.ncbi.nlm.nih.gov/35396579/)) analyzed ultra-rare protein-truncating variants (PTVs) and damaging missense variants in **24,248 cases and 97,322 controls** (125,748 exomes). This is an orthogonal evidence tier to SCZD1–19: SCHEMA is gene-level rare-variant burden from exome sequencing; SCZD1–19 is locus-level linkage/GWAS/CNV evidence. Very few genes overlap between the two datasets.

**Variant classes:**
- **Class I** = ultra-rare PTVs + Missense MPC ≥ 3 (highest functional impact; OR Class I in table)
- **Class II** = Missense 2 ≤ MPC < 3 (moderately damaging; OR Class II in table)

**Significance tiers:**
- ★★★ **Exome-wide** (P < 2.14 × 10⁻⁶): 10 genes
- ★★ **FDR 5%** (Q < 0.05): 32 genes total (includes exome-wide)
- ★ **Suggestive** (P < 5 × 10⁻⁴, Q > 0.05): 10 additional genes shown

**SCZD loci overlap (†):** Some SCHEMA genes fall within large SCZD linkage windows. Overlap is annotated but does not imply the same causal variant — linkage windows are typically 10–50 Mb.

---

### 5B. SCHEMA Exome Rare Variant Results (all 42 genes with P < 5 × 10⁻⁴)

| Gene | Locus | Description | Case PTV | Ctrl PTV | P_meta | Q_meta | OR (Class I) | OR (Class II) | Tier | SCZD / Note |
|---|---|---|---|---|---|---|---|---|---|---|
| [SETD1A](https://schema.broadinstitute.org/results) | 16p11.2 | SET domain histone lysine methyltransferase | 15 | 3 | 2.00e−12 | 3.62e−8 | 10.3 | 4.42 | ★★★ | — |
| [CUL1](https://schema.broadinstitute.org/results) | 7q36.1 | Cullin 1 (SCF ubiquitin ligase scaffold) | 8 | 1 | 2.01e−9 | 1.82e−5 | 44.2 | 1.76 | ★★★ | — |
| [XPO7](https://schema.broadinstitute.org/results) | 8p21.3 | Exportin 7 (nuclear export) | 12 | 1 | 7.18e−9 | 4.34e−5 | 28.1 | 1.25 | ★★★ | †SCZD6 (8p22–p21) |
| [TRIO](https://schema.broadinstitute.org/results) | 5p15.2 | TRIO Rho guanine nucleotide exchange factor | 18 | 16 | 6.35e−8 | 2.88e−4 | 5.02 | 0.94 | ★★★ | — |
| [CACNA1G](https://schema.broadinstitute.org/results) | 17q21.33 | Voltage-gated Ca²⁺ channel α1G (T-type, Cav3.1) | 10 | 13 | 4.57e−7 | 1.54e−3 | 4.25 | 1.68 | ★★★ | — |
| [SP4](https://schema.broadinstitute.org/results) | 7p15.3 | Sp4 transcription factor (neural-specific KZF) | 13 | 6 | 5.08e−7 | 1.54e−3 | 7.59 | 0 | ★★★ | — |
| [GRIA3](https://schema.broadinstitute.org/results) | Xq23 | Glutamate AMPA receptor subunit GluA3 | 5 | 0 | 5.98e−7 | 1.55e−3 | 20.1 | 1.67 | ★★★ | — |
| [GRIN2A](https://schema.broadinstitute.org/results) | 16p13.2 | Glutamate NMDA receptor subunit GluN2A | 9 | 2 | 7.37e−7 | 1.67e−3 | 24.1 | 2.37 | ★★★ | — |
| [HERC1](https://schema.broadinstitute.org/results) | 15q22.31 | HECT/RLD E3 ubiquitin ligase | 28 | 32 | 1.26e−6 | 2.54e−3 | 3.51 | 1.00 | ★★★ | — |
| [RB1CC1](https://schema.broadinstitute.org/results) | 8q11.23 | RB1-inducible coiled-coil 1 (autophagy initiator) | 9 | 4 | 2.00e−6 | 3.63e−3 | 10.0 | — | ★★★ | — |
| [HCN4](https://schema.broadinstitute.org/results) | 15q24.1 | Hyperpolarization-activated cyclic nucleotide-gated K⁺ channel 4 | 8 | 0 | 2.54e−6 | 4.19e−3 | ∞ | — | ★★ | — |
| [AKAP11](https://schema.broadinstitute.org/results) | 13q14.11 | A-kinase anchoring protein 11 (PKA scaffold) | 17 | 13 | 8.28e−6 | 1.25e−2 | 5.25 | — | ★★ | Also BD risk† |
| [ZNF136](https://schema.broadinstitute.org/results) | 19p13.2 | Zinc finger protein 136 (KRAB-ZFP) | 23 | 25 | 9.42e−6 | 1.31e−2 | 3.70 | — | ★★ | — |
| [SRRM2](https://schema.broadinstitute.org/results) | 16p13.3 | Serine/arginine repetitive matrix protein 2 | 16 | 9 | 1.53e−5 | 1.94e−2 | 7.14 | — | ★★ | — |
| [NR3C2](https://schema.broadinstitute.org/results) | 4q31.23 | Nuclear receptor subfamily 3 group C member 2 (mineralocorticoid receptor) | 7 | 3 | 1.60e−5 | 1.94e−2 | 9.37 | 2.92 | ★★ | — |
| [ZMYM2](https://schema.broadinstitute.org/results) | 13q12.11 | Zinc finger MYM-type containing 2 (NuRD complex) | 16 | 14 | 1.73e−5 | 1.96e−2 | 4.82 | 2.68 | ★★ | — |
| [FAM120A](https://schema.broadinstitute.org/results) | 9q22.31 | Family with sequence similarity 120A (RNA binding) | 7 | 1 | 2.22e−5 | 2.37e−2 | 5.02 | 0.62 | ★★ | — |
| [SLF2](https://schema.broadinstitute.org/results) | 10q24.33 | SMC5-SMC6 complex localization factor 2 (DNA repair) | 19 | 25 | 2.50e−5 | 2.45e−2 | 3.05 | — | ★★ | near SCZD11 (10q22.3) |
| [KDM6B](https://schema.broadinstitute.org/results) | 17p13.1 | Lysine demethylase 6B (H3K27me3 eraser) | 8 | 5 | 2.57e−5 | 2.45e−2 | 6.69 | 2.01 | ★★ | — |
| [DNM3](https://schema.broadinstitute.org/results) | 1q24.3 | Dynamin 3 (endocytosis, synaptic vesicle recycling) | 11 | 13 | 3.53e−5 | 3.20e−2 | 3.71 | 0 | ★★ | — |
| [ASH1L](https://schema.broadinstitute.org/results) | 1q22 | ASH1-like H3K36 methyltransferase (chromatin) | 9 | 2 | 3.77e−5 | 3.25e−2 | 18.1 | 0.60 | ★★ | — |
| [STAG1](https://schema.broadinstitute.org/results) | 3q22.3 | STAG1 cohesin complex component | 6 | 3 | 5.26e−5 | 4.34e−2 | 8.03 | 3.12 | ★★ | — |
| [H1-4](https://schema.broadinstitute.org/results) | 6p22.2 | H1.4 linker histone (chromatin compaction) | 7 | 4 | 5.84e−5 | 4.47e−2 | 7.03 | — | ★★ | near SCZD3 (6p23) |
| [PREP](https://schema.broadinstitute.org/results) | 6q22.1 | Prolyl endopeptidase (neuropeptide cleavage) | 10 | 11 | 5.99e−5 | 4.47e−2 | 3.65 | — | ★★ | †SCZD5 (6q13–q26) |
| [MAGEC1](https://schema.broadinstitute.org/results) | Xq27.2 | MAGE family member C1 | 37 | 66 | 6.18e−5 | 4.47e−2 | 2.25 | — | ★★ | — |
| [MAGI2](https://schema.broadinstitute.org/results) | 7q21.11 | Membrane-associated guanylate kinase WW and PDZ domain 2 | 11 | 5 | 6.41e−5 | 4.47e−2 | 8.03 | 1.09 | ★★ | — |
| [DAGLA](https://schema.broadinstitute.org/results) | 11q12.2 | Diacylglycerol lipase alpha (2-AG endocannabinoid synthesis) | 9 | 6 | 6.87e−5 | 4.61e−2 | 6.02 | 1.19 | ★★ | — |
| [OR4P4](https://schema.broadinstitute.org/results) | 11q11 | Olfactory receptor family 4 subfamily P member 4 | 10 | 4 | 7.43e−5 | 4.67e−2 | 10.0 | — | ★★ | — |
| [SLC22A11](https://schema.broadinstitute.org/results) | 11q13.1 | Solute carrier family 22 member 11 (OAT4 organic anion transporter) | 22 | 23 | 7.56e−5 | 4.67e−2 | 3.84 | — | ★★ | — |
| [ANKRD12](https://schema.broadinstitute.org/results) | 18p11.22 | Ankyrin repeat domain 12 | 23 | 26 | 7.87e−5 | 4.67e−2 | 3.55 | — | ★★ | †SCZD8 (chr 18p) |
| [SV2A](https://schema.broadinstitute.org/results) | 1q42.1 | Synaptic vesicle glycoprotein 2A (levetiracetam target) | 10 | 7 | 8.21e−5 | 4.67e−2 | 4.42 | 2.13 | ★★ | — |
| [EIF2S3](https://schema.broadinstitute.org/results) | Xp22.11 | Eukaryotic translation initiation factor 2 subunit γ | 3 | 0 | 8.23e−5 | 4.67e−2 | ∞ | 4.01 | ★★ | — |
| [PCLO](https://schema.broadinstitute.org/results) | 7q11.23 | Piccolo presynaptic cytomatrix protein | 20 | 20 | 1.30e−4 | 7.06e−2 | 4.02 | — | ★ | — |
| [SOBP](https://schema.broadinstitute.org/results) | 6q22.2 | Sine oculis binding protein homolog | 5 | 2 | 1.32e−4 | 7.06e−2 | 12.0 | — | ★ | †SCZD5 (6q13–q26) |
| [BSCL2](https://schema.broadinstitute.org/results) | 11q12.3 | BSCL2 seipin (lipid droplet biogenesis) | 14 | 15 | 2.22e−4 | 1.15e−1 | 3.75 | — | ★ | — |
| [NR4A2](https://schema.broadinstitute.org/results) | 2q24.1 | Nuclear receptor subfamily 4 group A member 2 (NURR1) | 4 | 0 | 2.55e−4 | 1.28e−1 | 5.35 | ∞ | ★ | — |
| [XKR6](https://schema.broadinstitute.org/results) | 8p23.1 | XK-related protein 6 (phospholipid scramblase) | 5 | 0 | 3.30e−4 | 1.62e−1 | ∞ | 1.04 | ★ | near SCZD6 (8p22–p21) |
| [ATP9A](https://schema.broadinstitute.org/results) | 20p13 | ATPase phospholipid transporting 9A | 15 | 11 | 3.72e−4 | 1.75e−1 | 5.48 | 1.23 | ★ | †same band as SCZD19/RBM12 (20p13) |
| [FYN](https://schema.broadinstitute.org/results) | 6q21 | FYN proto-oncogene Src family tyrosine kinase | 7 | 3 | 3.75e−4 | 1.75e−1 | 10.7 | 1.26 | ★ | †SCZD5 (6q13–q26) |
| [CRAT](https://schema.broadinstitute.org/results) | 9q34.1 | Carnitine O-acetyltransferase (mitochondrial) | 20 | 22 | 4.01e−4 | 1.79e−1 | 3.65 | — | ★ | — |
| [NPRL3](https://schema.broadinstitute.org/results) | 16p13.3 | NPR3-like GATOR1 complex subunit (mTORC1 regulator) | 5 | 5 | 4.12e−4 | 1.79e−1 | 4.01 | — | ★ | — |
| [SCAF1](https://schema.broadinstitute.org/results) | 19p13.3 | SR-related CTD associated factor 1 (pre-mRNA splicing) | 6 | 4 | 4.15e−4 | 1.79e−1 | 6.02 | — | ★ | — |

**† SCZD locus overlap notes:** XPO7 (8p21.3) falls within the SCZD6 linkage window (8p22–p21). PREP, SOBP, FYN are all within the SCZD5 linkage window (6q13–q26). H1-4 is in the adjacent band to SCZD3 (6p22.2 vs 6p23). ANKRD12 is within SCZD8 (chr 18p). ATP9A shares the 20p13 band with RBM12/SCZD19. These are proximity annotations only — linkage windows span many genes and the causal variants may differ.

---

### 5C. SCZD-Named Genes NOT in SCHEMA Top Results

The following genes are specifically named in OMIM SCZD entries but do not appear in the SCHEMA top 42 gene list (P < 5 × 10⁻⁴). Evidence type is linkage, CNV, or older candidate-gene studies — orthogonal to SCHEMA exome analysis.

| Gene | SCZD# | OMIM (SCZD) | Locus | Evidence type | SCHEMA status | Key References |
|---|---|---|---|---|---|---|
| **PRODH** | SCZD4 | [600850](https://omim.org/entry/600850) | 22q11.21 | Rare missense (proline dehydrogenase); 22q11.2 deletion | Not in SCHEMA top list; rare variant data suggest modest signal | Jacquet 2002 *Nat Genet*; Liu 2002 *PNAS* |
| **DAOA / G72** | SCZD7 | [603176](https://omim.org/entry/603176) | 13q33.2 | Linkage; common variant association; G72 protein modulates DAAO | Not in SCHEMA top list | Chumakov 2002 *PNAS*; Hattori 2003 |
| **DISC1** | SCZD9 | [604906](https://omim.org/entry/604906) | 1q42.2 | Balanced t(1;11) translocation; disrupts DISC1 protein | Not in SCHEMA; translocation not captured by exome SNP burden | Millar 2000 *Hum Mol Genet* |
| **CHRNA7** | SCZD13 | [613025](https://omim.org/entry/613025) | 15q13.3 | 15q13.3 microdeletion (CNV); contains CHRNA7 | CNVs excluded from SCHEMA; not in PTV/missense top list | Stefansson 2008 *Nat Genet* |
| **SHANK3** | SCZD15 | [613950](https://omim.org/entry/613950) | 22q13.33 | Rare CNV/deletion; Phelan-McDermid syndrome overlap | CNVs excluded from SCHEMA; not in PTV/missense top list | Gauthier 2010 *Nat Genet* |
| **VIPR2** | SCZD16 | [613959](https://omim.org/entry/613959) | 7q36.3 | Rare 7q36.3 microduplication (CNV) | CNVs excluded from SCHEMA | Vacic 2011 *Nature* |
| **NRXN1** | SCZD17 | [614332](https://omim.org/entry/614332) | 2p16.3 | 2p16.3 deletion (CNV); NRXN1 exonic deletion | CNVs excluded from SCHEMA; NRXN1 PTVs may appear in full dataset | Rujescu 2009 *Hum Mol Genet* |
| **SLC1A1** | SCZD18 | [615232](https://omim.org/entry/615232) | 9p24.2 | Rare coding variants in glutamate transporter EAAC1 | Not in SCHEMA top list | Myles-Worsley 2013 *Am J Med Genet B* |
| **RBM12** | SCZD19 | [617629](https://omim.org/entry/617629) | 20p13 | Heterozygous loss-of-function in Danish families | Not in SCHEMA top list (small Danish pedigree signal) | Hoeffding 2017 *JAMA Psychiatry* |

**Note on DISC1:** The DISC1 gene has been substantially de-emphasized in recent schizophrenia genetics. Multiple GWAS have failed to implicate the 1q42.2 region, and the original t(1;11) family is now considered an atypical case. DISC1 is not in the SCHEMA top gene list.

**Note on CHRNA7, SHANK3, VIPR2, NRXN1:** These are primarily CNV genes. SCHEMA analyzes PTVs and missense variants from exome sequencing, which does not capture large structural variants / copy number variants. Their absence from SCHEMA does not diminish their CNV-level evidence.

---

### 5D. Quick Reference: Pathway Enrichment of SCHEMA Genes

| Pathway / Function | SCHEMA Genes |
|---|---|
| **Glutamate signaling** | GRIA3 (AMPA), GRIN2A (NMDA), CACNA1G (T-type Ca²⁺ channel) |
| **Chromatin / histone regulation** | SETD1A, ASH1L, KDM6B, H1-4, ZMYM2, ZNF136 |
| **Ubiquitin-proteasome** | CUL1, HERC1 |
| **Nuclear export / transport** | XPO7, EIF2S3 |
| **Rho/actin signaling** | TRIO, FYN |
| **Ion channels** | CACNA1G, HCN4 |
| **Synaptic / presynaptic** | PCLO, SV2A, DAGLA, MAGI2 |
| **Autophagy / mTOR** | RB1CC1, NPRL3 |
| **Cohesin / DNA repair** | STAG1, SLF2 |
| **Transcription factors** | SP4, NR3C2, NR4A2 |
| **RNA processing** | SRRM2, FAM120A, SCAF1 |
| **Lipid metabolism** | DAGLA, BSCL2, ATP9A, CRAT |

*Source: [SCHEMA browser](https://schema.broadinstitute.org/results), Singh et al. 2022 *Nat Genet* PMID:35396579*
