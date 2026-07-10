## 40. Disease strategy and evidence base

### Significance: from genetic evidence to testable mechanism

Drug targets with human genetic support reach approval about two to three times more often than those without (Nelson et al. 2015 estimated ~2x; Minikel et al. 2024 refined it to 2.6x), and the multiplier grows with confidence in the causal gene and varies by therapeutic area. That makes human genetics the highest-yield starting point, and it makes mechanistic precision the variable that moves the payoff.

Capturing that advantage in psychiatry is hard. Most signal is noncoding with ambiguous variant-to-gene mapping; effect sizes are small and dispersed across many loci; and even an unambiguous causal gene rarely yields a mechanism (the *C9orf72* repeat expansion in ALS and frontotemporal dementia is the canonical case, where the gene is certain but loss-of-function, toxic-RNA, and dipeptide-repeat mechanisms still compete). The mature industry response, a statistical-genetics-and-machine-learning discovery function feeding post-hoc validation in iPSC-derived NGN2 neurons or organoids read out through proxy phenotypes (hyperexcitability, synaptic density, protein aggregation), confirms that a variant does something but rarely explains how it drives disease, cannot certify that the observed axis is the disease-relevant one, does not reveal which other molecules in the pathway are easier or safer to drug, and discards the convergence of weaker variants on shared biology.

We close that gap by grounding one causal model in **two complementary experiments at once**: engineered cellular perturbations, where the intervention is known but the system is artificial, and natural population genetics, where the system is real but the intervention cannot be tested. Joint genomic factorization represents every signal as a shift in shared pathway space, so each method covers the other's blind spot and the model surfaces disease axes that are mechanistic, population-relevant, and testable. The full treatment is in `research/SIGNIFICANCE_AND_INNOVATION_dual_grounding_2026-06-15.md`.

---

**IGoR framing rule (committed strategy):** "Do not propose a single disease (22q11DS alone): too narrow, reads as the well-bounded problem they reject. Do not propose a vague area with no anchor. Frame as: a neuropsychiatric area, with 22q11DS as the Phase I-II flagship exemplar, generalizing to idiopathic schizophrenia or broader transdiagnostic psychiatry in Phase III."

**Proposal title:** "A Closed-Loop, Mechanistically Grounded Research Engine for Complex Neuropsychiatric Disease: Schizophrenia to Bipolar Disorder."

---

### Phase I/II anchor: 22q11.2 deletion syndrome (22q11DS)

**Rationale (committed framing):** "22q11DS is the highest-penetrance known genetic risk factor for psychosis; its deletions span TBX1, COMT, and DGCR8, genes with well-characterized but mechanistically unlinked effects on cell-type pathology and thalamocortical/fronto-temporal circuit function. Formalizing that molecular-to-circuit causal chain, and using it to drive systematic experiment design, is a tractable, scientifically important, and measurable deliverable."

**Key epidemiological statistics (meta-analysis evidence):**

| Metric | Value | Source |
|---|---|---|
| Pooled prevalence of psychotic disorders in 22q11DS | 11.5% (95% CI: 9.4-14.0%) | Schneider et al. 2023 *BJPsych* (PMID: 36786112) |
| Pooled prevalence of schizophrenia specifically | 9.7% (95% CI: 6.5-14.2%) | Same meta-analysis |
| 5-year incidence of psychosis | 10.6% (95% CI: 6.6-16.7%) | Same meta-analysis |
| Relative risk for schizophrenia spectrum | ~20-25x vs. general population | Bassett and Chow 1999; Murphy et al. 1999 *Arch Gen Psychiatry* (PMID: 10199234) |
| Prevalence of 22q11.2 deletion in schizophrenia cohorts | ~0.3-1% vs. ~0.025% in general population | Multiple CNV/GWAS studies |

**The causal chain we commit to formalizing:**

```
TBX1 / COMT / DGCR8 (22q11.21 locus)
    -> cell-type pathology (oligodendrocyte lineage; cortical and somatosensory; interneuron/excitatory imbalance)
    -> thalamocortical / fronto-temporal circuit dysfunction
```

**TBX1 as the primary genetic handle:** TBX1 (OMIM:602054; chr 22q11.21) is the primary causal gene for cardiovascular and pharyngeal defects of 22q11.2DS. It is also expressed in the oligodendrocyte lineage and embryonic cortex.

Supporting evidence for TBX1 as a schizophrenia model anchor:

- Tbx1+/- mice show reduced prepulse inhibition (PPI), a validated schizophrenia endophenotype (Paylor et al. 2006 *PNAS*; PMID: 16684884)
- Tbx1 loss in mesodermal cells disrupts corticogenesis via premature neurogenesis in the somatosensory cortex anlage (Vitelli et al. 2017 *Cereb Cortex*; PMID: 27131548)
- Tbx1 heterozygosity in the oligodendrocyte lineage specifically disrupts myelination of fimbria axons (Kim and Bhatt 2025 *bioRxiv* 2025.12.30.697076)

**Caveat acknowledged (required for proposal):** TBX1 sequence variation does NOT significantly contribute to the genetic etiology of psychotic or affective disorders in the general nonsyndromic population (Funke et al. 2007 *Mol Med*; PMID: 17622321). TBX1 is framed as the primary genetic handle within 22q11DS, not as a standalone schizophrenia gene. Other 22q11 genes (DGCR8, PRODH, GNB1L, COMT) carry stronger direct mechanistic links to psychosis pathways in idiopathic schizophrenia.

**Phase I anchor experiment:** Paired isogenic iPSC lines carrying a patient-derived 22q11.2-region (TBX1 exon 2 CNV) validation line; see restricted section 41. Lines are CRISPR-corrected to a matched healthy control and differentiated to NGN2 neurons.

**MONDO/ontology note:** 22q11DS-associated schizophrenia maps to SCZD4 (OMIM:600850/PRODH). SCZD4 is not a direct child of MONDO:0005090 (schizophrenia); 22q11DS is a separate MONDO entity (MONDO:0011511, DiGeorge syndrome/velocardiofacial syndrome). This distinction must be encoded correctly in the TA1 ontology layer.

---

### Key datasets and assays supporting Phase I/II

| Dataset/assay | Description | Use in TA1 |
|---|---|---|
| **PsychENCODE brainSCOPE** (Emani et al. *Science* 2024; DOI: 10.1126/science.adi5199) | Single-cell genomics and regulatory networks for 388 human brains; 24 brain cell types | GRN layer; cell-type-specific TF-to-target edges |
| **PsychAD atlas** (Batiuk et al. *Nat Neurosci* 2024) | Upper-layer cortical neuron pathology in schizophrenia | Cell-type resolution; co-author |
| **Ruzicka, Mohammadi et al. *Science* 2024** (multi-cohort schizophrenia atlas; DOI: 10.1126/science.adg5136) | Single-cell multi-cohort dissection of schizophrenia transcriptome | Primary schizophrenia cell-type atlas; PI co-led |
| **ROSMAP atlas** (Mathys, Mohammadi et al. *Nature* 2019) | Single-cell Alzheimer's disease atlas | Demonstrates atlas-building capability; co-author |
| **SCHEMA exome** (Singh et al. *Nat Genet* 2022; DOI: 10.1038/s41586-022-04556-w) | 24,248 cases vs. 97,322 controls; 10 exome-wide genes | Rare-variant genomic layer; glutamate/chromatin/ubiquitin pathways |
| **NeuroPainting / Tegtmeyer et al. *Nat Commun* 2025** (DOI: 10.1038/s41467-025-61547-x) | Cell-type-specific morphological and molecular signatures of the 22q11.2 deletion in iPSC-derived neurons and astrocytes | Direct TA1/TA3 validation precedent; Carpenter senior author |
| **JUMP Cell Painting Consortium** (>116K compounds) | Genome-scale morphological profiles; Carpenter/Broad | TA4 Phase I morphological readout baseline |
| **Open Targets Platform** (Falaguera et al. *Nat Commun* 2025) | Temporal trends in drug target evidence; GWAS causal gene scoring (L2G) | Target credentialing and genetic support scoring |
| **PGC schizophrenia GWAS** (Trubetskoy et al. *Nature* 2022; DOI: 10.1038/s41586-022-04434-5) | Mapping genomic loci implicating genes and synaptic biology | Genomic layer; soft interventions into TA1 causal model |

---

### Phase III: Idiopathic schizophrenia

The same modeling framework generalizes to idiopathic schizophrenia in Phase III, satisfying IGoR's explicit second-disease generalization requirement. The schizophrenia GWAS layer (PGC, Trubetskoy et al. 2022), SCHEMA rare-variant data, and the PsychENCODE/multi-cohort atlas directly support this extension. Brad Ruzicka (McLean/Harvard, clinical co-lead) is the primary interface for the Phase III schizophrenia translational validation layer.

---

### Bipolar disorder: cautious Phase III extension

Bipolar disorder is the stated Phase III second disease in the full proposal title and cover block ("Schizophrenia to Bipolar Disorder"). The 22q11DS model carries bipolar disorder relevance (an estimated 15-25% rate in 22q11DS cohorts). The BDNF/TrkB axes, which underpin mood, thought, and cognitive dimensions, and the shared mechanistic pathway to rapid-acting antidepressant plasticity (ketamine, psilocybin), provide the scientific bridge.

Framing guidance: bipolar is presented as a biologically and genetically related Phase III extension that shares cellular biology and disease axes with schizophrenia, not as a primary focus. The degree of independence between the schizophrenia and bipolar extensions is framed as an empirical question that the causal model will address.

> [!NOTE]
> **Penetrant-form deep dive:** the MONDO and OMIM SCZD subtype landscape, the 22q11DS risk statistics, the TBX1 evidence (for and against), and the SCHEMA rare-variant convergence that justify building cellular models on penetrant forms are consolidated in section 42.
