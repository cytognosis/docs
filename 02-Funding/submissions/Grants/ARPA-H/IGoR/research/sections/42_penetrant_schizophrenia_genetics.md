## 42. Penetrant schizophrenia genetics and the familial-disease rationale for cellular models

> [!TIP]
> **If you read one thing:** schizophrenia is mostly polygenic and therefore hard to model in a dish, but it has **high-penetrance genetic forms** (the 22q11.2 deletion and a set of large-effect rare-variant genes such as SETD1A, GRIN2A, and CUL1) that behave almost Mendelian. We use these the way neurodegeneration research uses **familial Alzheimer (APP, PSEN1) and familial Parkinson (SNCA, LRRK2)**: as near-deterministic genotype handles that give a strong, interpretable genotype-to-cellular-phenotype signal, justifying cellular models built on them first and then generalized to idiopathic disease.

### 42.1 Why penetrant forms justify cellular models

A diffuse polygenic score spreads tiny effects across thousands of loci, which no iPSC model can express as a clean phenotype. A penetrant variant concentrates the causal signal, which is exactly what a cellular model needs to read out. This is the same move that made neurodegeneration tractable in a dish.

| Field | Familial / penetrant handle | Why it enabled cellular models |
|---|---|---|
| **Alzheimer disease** | APP, PSEN1, PSEN2 (autosomal dominant) | Near-deterministic genotype; iPSC neurons show amyloid and tau phenotypes that anchor the sporadic disease model |
| **Parkinson disease** | SNCA, LRRK2, GBA | Strong genotype-to-phenotype signal in iPSC dopaminergic neurons; defines the axes sporadic cases are read against |
| **Schizophrenia (our entry)** | **22q11.2 deletion (~25x risk)** and large-effect SCHEMA genes (SETD1A, GRIN2A, GRIA3, CUL1) | Penetrant, near-Mendelian handles that produce measurable cellular phenotypes, anchoring a model later generalized to idiopathic schizophrenia |

> [!IMPORTANT]
> This is the bridge from the thesis (section 10): a **penetrant variant is the cleanest soft-intervention** on the latent causal model, so penetrant forms are where the disease-as-perturbation frame is most identifiable. They are the Phase I cellular anchor (section 41, restricted); idiopathic schizophrenia is the harder Phase III generalization (section 40).

### 42.2 The genetic-subtype landscape (MONDO and OMIM SCZD loci)

OMIM defines **19 numbered SCZD loci**; the gene-level ones are the usable cellular handles. An ontology caveat matters for TA1 design.

| SCZD | Gene / locus | Mechanism class | Evidence | Notes |
|---|---|---|---|---|
| **SCZD4** | 22q11.21 deletion (**PRODH**, plus DGCR8, COMT, TBX1, GNB1L) | CNV, multi-gene | Strongest known risk | The flagship penetrant handle (42.3) |
| **SCZD9** | **DISC1** (1q42.2) | Translocation | De-emphasized in recent GWAS | Historical; not in SCHEMA |
| **SCZD13** | **CHRNA7** (15q13.3 microdeletion) | CNV | Replicated CNV | nicotinic receptor |
| **SCZD15** | **SHANK3** (22q13.33) | Rare CNV/deletion | Phelan-McDermid overlap | postsynaptic scaffold |
| **SCZD16** | **VIPR2** (7q36.3 microduplication) | CNV | Nature 2011 | VIP receptor |
| **SCZD17** | **NRXN1** (2p16.3 deletion) | CNV/deletion | Replicated | presynaptic adhesion |
| **SCZD18** | **SLC1A1** (9p24.2) | Rare coding | Glutamate transporter EAAC1 | glutamate clearance |
| **SCZD19** | **RBM12** (20p13) | Heterozygous LoF | Danish pedigrees | RNA binding |

> [!CAUTION]
> **Ontology gap to handle in TA1 (sections 24 and 30):** SCZD4 (22q11/PRODH, OMIM 600850) is **not a direct child of MONDO:0005090 (schizophrenia)**; 22q11.2DS is a separate MONDO entity (MONDO:0011511, DiGeorge/velocardiofacial syndrome). Six SCZD loci (SCZD4, 6, 9, 13, 14, 18) have MONDO IDs but are not direct schizophrenia children. Our ontology-conditioned model must reconcile the genetics-first view (22q11DS as a schizophrenia handle) with the MONDO classification, or it will mis-place the disease.

### 42.3 22q11.2 deletion syndrome: the highest-penetrance handle

| Metric | Value | Source |
|---|---|---|
| Lifetime psychosis risk | **~25%** (~25-fold vs. general population) | Murphy et al. 1999; consensus reviews |
| Pooled psychotic-disorder prevalence | **11.5%** (95% CI 9.4 to 14.0) | Schneider et al. 2023 (PMID:36786112) |
| Pooled schizophrenia prevalence | **9.7%** (95% CI 6.5 to 14.2) | Same meta-analysis |
| 22q11.2 deletion in schizophrenia cohorts | **~0.3 to 1%** vs. ~0.025% general | Karayiorgou et al. 1995; CNV studies |
| Fraction of all schizophrenia attributable | **~1 to 2%** | Karayiorgou et al. 1995 |

The deletion spans multiple psychosis-relevant genes (PRODH glutamate/proline, DGCR8 miRNA biogenesis, COMT dopamine catabolism, GNB1L, TBX1), which is why it is a multi-gene causal handle rather than a single-gene model.

### 42.4 TBX1: a partial model, used precisely

TBX1 is the primary causal gene for the cardiac, thymic, and craniofacial features of 22q11DS, and it has real but bounded psychiatric evidence. We state it honestly to avoid overclaiming.

- **For (mechanistic):** Tbx1+/- mice show reduced prepulse inhibition, a validated schizophrenia endophenotype (Paylor et al. 2006); a human family with a TBX1 frameshift co-segregated psychiatric features without the full deletion; Tbx1 loss disrupts corticogenesis (Vitelli et al. 2017) and oligodendrocyte myelination of fimbria axons (Kim and Bhatt 2025).
- **Against (genetic):** TBX1 sequence variation does not significantly contribute to nonsyndromic schizophrenia (Funke et al. 2007); variants are rare and underpowered in case-control studies; PRODH, DGCR8, COMT, and GNB1L have stronger direct links to psychosis pathways.

> [!IMPORTANT]
> **How we use TBX1:** as a high-penetrance developmental handle that mimics a familial-disease entry, not as a standalone schizophrenia gene. Its best-supported neural phenotypes (corticogenesis, myelination, prepulse inhibition) are the cellular and circuit readouts the model targets, and the honest genetic caveat is stated in the proposal rather than buried.

### 42.5 Rare-variant convergence (SCHEMA) defines what the cellular models read out

SCHEMA (Singh et al. 2022, *Nat Genet*, PMID:35396579; 24,248 cases, 97,322 controls) provides an orthogonal, gene-level tier of large-effect rare variants. Ten genes reach exome-wide significance and 32 reach 5% FDR. The high-odds-ratio genes are the cleanest cellular handles.

| Tier | Genes (illustrative) |
|---|---|
| **Exome-wide significant (10)** | **SETD1A, CUL1, XPO7, TRIO, CACNA1G, SP4, GRIA3, GRIN2A, HERC1, RB1CC1** |
| **Highest odds ratios** | CUL1 (OR ~44), XPO7 (~28), GRIN2A (~24), GRIA3 (~20) |

The convergent biology tells the cellular models which phenotypes to measure:

| Pathway | SCHEMA genes |
|---|---|
| **Glutamate signaling** | GRIA3 (AMPA), GRIN2A (NMDA), CACNA1G (T-type Ca channel) |
| **Chromatin and histone regulation** | SETD1A, ASH1L, KDM6B, H1-4, ZMYM2, ZNF136 |
| **Synaptic and presynaptic** | PCLO, SV2A, DAGLA, MAGI2 |
| **Ubiquitin-proteasome** | CUL1, HERC1 |
| **Rho/actin signaling** | TRIO, FYN |
| **Autophagy and mTOR** | RB1CC1, NPRL3 |
| **Transcription factors** | SP4, NR3C2, NR4A2 |

> [!NOTE]
> The full 42-gene SCHEMA table (P < 5e-4), the complete 19-locus SCZD table with MONDO and OMIM identifiers, and the SCZD-named genes outside the SCHEMA top list are preserved verbatim in `_sources/schizophrenia_MONDO_subtypes_22q11_TBX1.md`.

### 42.6 Implications for our cellular models

- **Build on penetrant forms first.** The 22q11.2 deletion and high-OR SCHEMA genes give iPSC-derived neuron and astrocyte models a measurable phenotype, anchoring TA1 (sections 30 and 40) and the Phase I experiment (section 41).
- **Read out convergent pathways.** Glutamatergic (GRIN2A, GRIA3), chromatin (SETD1A), and synaptic (NRXN1, SHANK3) axes are the molecular and cellular phenotypes the models must capture, and they double as the candidate disease axes the factorization targets (section 31, restricted).
- **Generalize via learned axes.** Penetrant forms calibrate the causal model; the transdiagnostic axes then project idiopathic, polygenic schizophrenia onto the same coordinate system (sections 10 and 40), which is the Phase III generalization.
- **Respect the ontology.** Encode the SCZD4-versus-MONDO:0005090 gap explicitly (sections 24 and 30) so genetics-first handles and disease classification stay consistent.

### Sources

22q11DS and schizophrenia: Murphy et al. 1999 (PMID:10199234); Schneider et al. 2023 (PMID:36786112); Karayiorgou et al. 1994 (PMID:8213821) and 1995 (PMID:7667299); Gothelf et al. 2007 (PMID:17046719); Vorstman et al. 2017 (PMID:28379838); Fiksinski et al. 2022 (PMID:35577927); Malone et al. 2022 (doi:10.1038/s41380-022-01674-9). TBX1: Paylor et al. 2006 (PMID:16684884); Funke et al. 2007 (PMID:17622321); Vitelli et al. 2017 (PMID:27131548); Kim and Bhatt 2025 (bioRxiv 2025.12.30.697076); Stark et al. 2008 (IJNP). Rare variants: SCHEMA, Singh et al. 2022 (PMID:35396579). Ontology: MONDO:0005090 and MONDO:0011511 (OLS4); OMIM SCZD1 to SCZD19.


### 42.7 Isogenic disease-in-a-dish and the Phase I phenotypic-triage screen

**Why engineered isogenic lines, not only patient lines.** A patient-derived iPSC line carries the variant but has **no genetically matched healthy control**, so any cellular difference is confounded by genetic background. Starting from a **common healthy iPSC background and inducing each variant by CRISPR** yields **isogenic case-control pairs** that isolate the causal effect of the variant, which is the clean soft-intervention the thesis (section 10) requires. Patient lines remain a useful complementary, real-genome check.

**The phenotypic-triage (phenoproxy) screen.** Not every penetrant variant produces a measurable in-dish phenotype, so Phase I runs a **systematic screen across the variant panel** (the 22q11.2 deletion and TBX1, high-odds-ratio SCHEMA genes such as SETD1A, GRIN2A, GRIA3, and CUL1, and selected SCZD loci) in iPSC-derived neurons and astrocytes, measuring **multimodal phenotypes**:

- **Transcriptomic:** single-cell RNA-seq signatures and pathway-space shifts.
- **Morphological:** high-content Cell Painting and neuronal morphometry.
- **Functional activity:** single-cell **calcium imaging**, the scalable single-cell activity readout and an optical modality that folds into the high-content and live-cell imaging stack; MEA is not required.
- Optional proteomic and metabolomic readouts where a variant implicates those layers.

**What it produces.** A ranked variant-to-phenotype map showing which genetic forms yield robust, reproducible disease-in-a-dish signatures. Strong-signal lines anchor the TA1 causal model and are carried forward; weak-signal variants are deprioritized. This **expands the Carpenter group's 22q11 NeuroPainting precedent** (Tegtmeyer et al. 2025) from one deletion and one modality to a **systematic, multi-variant, multi-modal screen**, which is both a concrete Phase I deliverable and the empirical basis for selecting the disease axes (sections 30 and 31).
