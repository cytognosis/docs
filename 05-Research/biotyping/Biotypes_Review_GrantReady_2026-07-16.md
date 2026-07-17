# Toward a Universal Dimensional Map of Psychiatric Biotypes: A Synthesis Across Molecular, Connectomic, and Phenotypic Scales

> **Status**: Active
> **Date**: 2026-07-16
> **Author**: Shahin Mohammadi
> **Audience**: funders, peer reviewers, co-authors
> **Tags**: `research`, `biotyping`, `neuro`
> **Variants**: Technical (this doc); publishable toward a review paper, following the `cytognosis-doc` skill Literature Synthesis template

---

## Abstract

Categorical psychiatric diagnosis, as codified in DSM-5-TR, groups patients into discrete labels that
correspond poorly to underlying biology. An accumulating body of evidence instead supports a
dimensional architecture in which shared genetic risk, molecular and cellular dysregulation,
large-scale brain connectivity, and symptom phenomenology all organize along a small number of
continuous axes that cut across diagnostic boundaries. This synthesis integrates a genome-wide
five-factor structure spanning 14 psychiatric disorders with a formal crosswalk across the Research
Domain Criteria (RDoC), the Hierarchical Taxonomy of Psychopathology (HiTOP), and DSM-5-TR
cross-cutting symptom measures, and aligns that structure to molecular (micro), connectomic (meso),
and phenotypic (macro) evidence layers for three anchor disorders, major depressive disorder (MDD),
bipolar disorder (BD), and schizophrenia (SCZ), with post-traumatic stress disorder (PTSD) and
anxiety disorders noted as direct extensions within the same Internalizing factor. We map this
architecture onto contemporary treatment frameworks, Neuroscience-based Nomenclature (NbN)
pharmacology, neuroplastogen mechanisms relevant to the ARPA-H EVIDENT program, and connectomic
neuromodulation targeting, and close with explicit limitations, replication caveats, and a list of
citations to complete before external submission. A confidential proprietary extension of this work
(a genome-derived factorized polygenic score reconstructing these axes without direct brain
measurement) exists in a separate internal dossier and is intentionally excluded from this document.

---

## 1. Introduction: the case for a dimensional architecture

Categorical diagnosis is clinically operational but maps unevenly onto biology. Diagnostic overlap is
substantial (Tourette syndrome clinic samples carry roughly 50 percent comorbid OCD and 50 percent
comorbid ADHD), single diagnoses fragment into biologically distinct subtypes (melancholic versus
atypical MDD), and diagnostic presentations shift across development (ADHD subtype instability from
childhood to adulthood). Two complementary frameworks have emerged to organize psychiatric variation
dimensionally rather than categorically.

**RDoC** (NIMH Research Domain Criteria) organizes function across six domains, Negative Valence
Systems, Positive Valence Systems, Cognitive Systems, Social Processes, Arousal and Regulatory
Systems, and Sensorimotor Systems (added 2019), each measurable across a Molecules-to-Self-Report
hierarchy of units of analysis.

**HiTOP** (Hierarchical Taxonomy of Psychopathology) is empirically derived from symptom covariation
and organizes psychopathology into spectra, Internalizing (Fear and Distress subfactors), Thought
Disorder, Disinhibited Externalizing, Antagonistic Externalizing, Detachment, and Somatoform.

Michelini, Palumbo, DeYoung, Latzman, and Kotov (2021, *Clinical Psychology Review*) formally
crosswalked RDoC constructs to HiTOP spectra by direction of association; that crosswalk, extended
and independently re-verified against subsequent literature, underlies the disorder-level matrices
used in this synthesis (Section 3). No genome-wide genetic architecture had, until recently, been
tested against either framework directly; Section 2 closes that gap.

---

## 2. The five-genomic-factor architecture

Grotzinger and colleagues (*Nature*, 2025, doi:10.1038/s41586-025-09820-3; n = 1,056,201 cases across
14 psychiatric disorders) resolved shared genetic risk into **five genomic factors** explaining
approximately 66 percent of genetic variance across 238 pleiotropic loci. The factor-specific
cell-type enrichments are the structural anchor for this synthesis, because they connect a
genome-wide statistical factor to a concrete cellular substrate that can, in principle, be measured
or targeted.

| Factor | Disorders (canonical) | Cell-type signature | DSM-5-TR / HiTOP / RDoC alignment |
|---|---|---|---|
| **SB** (schizophrenia + bipolar) | Schizophrenia, bipolar disorder | Excitatory neurons | HiTOP Thought Disorder spectrum; RDoC Cognitive Systems and Positive Valence Systems; DSM-5-TR cross-cutting Psychosis and Mania domains |
| **Internalizing** | Major depressive disorder, PTSD, anxiety disorders | Oligodendrocyte / myelin biology | HiTOP Internalizing/Fear and Internalizing/Distress; RDoC Negative Valence Systems; DSM-5-TR cross-cutting Depression and Anxiety domains |
| **Neurodevelopmental** | Autism spectrum disorder, ADHD, Tourette syndrome | Synaptic and interneuron developmental programs | HiTOP neurodevelopmental columns (extended matrix); RDoC Cognitive Systems and Social Processes |
| **Compulsive/eating** *(extended scope)* | OCD, anorexia nervosa, Tourette syndrome | Synaptic / interneuron biology | HiTOP Thought Disorder-adjacent; outside core scope |
| **Substance-use** *(extended scope)* | Alcohol, opioid, nicotine, cannabis use disorders | Reward-dopaminergic and metabolic biology | HiTOP Disinhibited/Antagonistic Externalizing; outside core scope |

The finding most relevant to a sensing-and-treatment platform is that the two largest factors carry
distinct cell-type signatures: SB is excitatory-neuron-centric (consistent with single-nucleus
RNA-seq confirming excitatory neurons as the most transcriptionally altered class in schizophrenia,
Ruzicka et al. 2024), while Internalizing is oligodendrocyte/myelin-centric, consistent with
longstanding postmortem glial-loss findings in MDD and PTSD. This synthesis treats the SB and
Internalizing factors, together with the Neurodevelopmental factor for context, as the core scope;
Compulsive/eating and Substance-use are noted as available but out of scope for the current figure.

**Precision caveat for the review draft:** the per-disorder factor loading magnitudes reported in the
Grotzinger et al. supplementary tables have not yet been extracted into this dossier's machine-readable
assets. The factor assignments above are categorical (disorder belongs to factor X) rather than
continuous (disorder loads at Y on factor X), and the continuous loadings should be pulled from the
primary source before the figure is rendered for external submission (see Section 7, references-to-add).

---

## 3. Crosswalk methodology: RDoC, HiTOP, DSM-5-TR, and disease ontology

The disorder-level crosswalk draws on three machine-readable canonical assets, used jointly rather
than independently:

1. **`matrix_hitop_disease.csv`** and **`matrix_rdoc_disease.csv`** (33 MONDO-coded disorders,
   signed and weighted associations to RDoC constructs and HiTOP dimensions respectively). Sign
   convention follows the Jacksonian positive/negative direction (gain/release/excess versus
   loss/deficit/absence relative to neurotypical baseline), with magnitude reflecting literature
   reproducibility (from >=0.85 meta-analyzed down to 0.20-0.35 emerging).
2. **`_MASTER_ontology_mapping.csv`** (111 clinical instruments, 2,399 items), which carries both an
   `rdoc_construct` and a `hitop_dimension` column per item, alongside HPO, SNOMED CT, LOINC,
   ICD-10-CM, MeSH, and MedDRA mappings. This is the direct bridge from genomic factor to
   patient-facing outcome instrument (for example, PHQ-9 items map to specific RDoC Negative Valence
   constructs and to the HiTOP Internalizing/Distress dimension).
3. **DSM-5-TR Level 1/2 Cross-Cutting Symptom Measures** (`dsm5tr/` mapping set), which supplies the
   DSM cross-cutting leg of the three-way crosswalk (RDoC/HiTOP to DSM-5-TR domains) referenced in
   Section 2's alignment column.

The join key across all three assets is the shared `rdoc_construct` and `hitop_dimension` vocabulary
established in the RDoC-HiTOP harmonization work (Michelini et al. 2021 base crosswalk, extended with
independently verified literature additions; 0 of 88 base associations were contradicted on
independent re-verification, 29 corroborated directly, 43 consistent-indirect, 16 not found in
adjacent literature). This gives the crosswalk a documented verification status rather than treating
it as a single unverified source.

---

## 4. Micro / meso / macro evidence, anchor disorders

### 4.1 Major depressive disorder (MDD)

**Micro.** Reduced serum/plasma BDNF that recovers with treatment response; Val66Met (rs6265) Met
carriers show blunted BDNF release and reduced ketamine/SSRI response; TrkB is the convergent
antidepressant pivot (Moliner et al. 2023, *Nat Neurosci*, doi:10.1038/s41593-023-01316-5).
CRP-stratified inflammatory subgroup; PV-interneuron/gamma-deficit in a cognitive subtype.

**Meso.** The dorsolateral prefrontal cortex (dlPFC) to subgenual anterior cingulate cortex (sgACC)
anticorrelation is the load-bearing edge-level finding: stronger baseline anticorrelation predicts
better response to targeted TMS (Fox and Cash; the Stanford SAINT/SNT protocol, Cole et al. 2022,
approximately 79 percent remission in treatment-resistant depression). Complementary nodes:
anhedonic biotype (ventral striatum, vmPFC hypoactivation), DMN-rumination biotype (sgACC, posterior
cingulate cortex/precuneus, medial PFC hyperconnectivity), cognitive-control biotype (dlPFC, dorsal
ACC).

**Macro.** PHQ-9 as the primary outcome instrument; six-axis biotype scaffold from Williams (iMAP,
2024, n = 801) is the current best-supported connectomic-plus-behavioral framework, superseding the
Drysdale et al. (2017) four-biotype solution, which failed independent replication (Dinga et al.
2019). This replication failure is a central methodological caveat for any biotype claim in MDD and
is carried forward explicitly rather than omitted.

### 4.2 Bipolar disorder (BD)

**Micro.** Peripheral BDNF falls in both manic and depressive states and recovers in euthymia; the
mature-BDNF-to-proBDNF ratio differentiates BD from MDD (state-dependent, MEDIUM-HIGH confidence).
Elevated oxidative stress markers (lipid peroxides, 8-OHdG, protein carbonyls) with reduced
antioxidant defense, partially N-acetylcysteine-responsive, consistent with the Berk/Kato
neuroprogression model.

**Meso.** Shares the SB genomic factor's excitatory-neuron substrate with schizophrenia. Elevated
glutamate/glutamine (Glx) on magnetic resonance spectroscopy across mood states; GABAergic deficits;
amygdala hyperactivity; hippocampal and prefrontal volume reductions consistent with the broader
atrophy pattern seen across mood and psychotic disorders.

**Macro.** YMRS for manic symptoms; depression-specific instruments during depressive episodes. The
episodic, bidirectional symptom structure (mania and depression as opposite poles rather than a
single-direction deficit) distinguishes BD's macro-level phenotype from the unidirectional deficit
pattern typical of MDD.

### 4.3 Schizophrenia (SCZ)

**Micro.** NMDA receptor hypofunction on parvalbumin-positive (PV) interneurons; reduced PV density
and GAD67 expression; elevated anterior cingulate glutamate on MRS in treatment-resistant cases
(HIGH confidence, the most reproducible single MICRO finding across all 14 disorders in this
synthesis). Excitatory-neuron transcriptional alteration is the dominant single-nucleus RNA-seq
signature (Ruzicka et al. 2024), consistent with the SB genomic factor's cell-type enrichment.

**Meso.** Thalamus loses its normal reciprocal balance between sensorimotor and prefrontal cortical
coupling (hyperconnectivity to sensorimotor cortex, hypoconnectivity to prefrontal cortex), a HIGH-
confidence, disorder-specific edge pattern. The B-SNIP consortium's two-biotype solution
(Clementz and Tamminga 2016) remains the best-replicated connectomic-plus-EEG stratification:
B-SNIP 1 (cognitive-deficit, DLPFC/superior temporal/anterior hippocampus, reduced P300) and B-SNIP 2
(sensory-hyperresponsive, Heschl's gyrus/planum temporale/sensorimotor, reduced 40Hz auditory
steady-state response and mismatch negativity).

**Macro.** PANSS as the primary outcome instrument, covering positive, negative, and general
psychopathology domains, each separately mappable to RDoC constructs (positive symptoms to Cognitive
Systems perceptual/belief-formation constructs; negative symptoms to Positive Valence Systems reward
constructs).

### 4.4 Extensions: PTSD and anxiety disorders

Both fall within the Internalizing genomic factor alongside MDD and share substantial meso-level
architecture, principally a weakened amygdala-vmPFC threat-regulation edge (normally an
anticorrelation in which vmPFC dampens amygdala reactivity; weakened or inverted in PTSD's
dissociative subtype and in generalized anxiety disorder). Because both disorders are already fully
represented in the transdiagnostic MICRO/MESO/MACRO syntheses and the RDoC-HiTOP-disease matrices,
their inclusion in the universal dimensional map is a scope filter rather than new synthesis work.

---

## 5. Treatment mapping across scales

### 5.1 Micro: NbN pharmacology and neuroplastogen mechanisms

The Neuroscience-based Nomenclature (NbN) system reclassifies psychotropic medications by
pharmacological mechanism (target neurotransmitter system, mode of action) rather than legacy
indication-based category (antidepressant, antipsychotic, mood stabilizer, anxiolytic). This
reclassification aligns directly with the micro-level biotype axes above: SSRIs and SNRIs
(serotonin/norepinephrine reuptake inhibition) map to the serotonergic axis; ketamine and esketamine
map to the glutamatergic/BDNF-TrkB axis; second-generation antipsychotics (dopamine D2 plus serotonin
5-HT2 receptor antagonism) map to the hyperdopaminergic axis relevant to SCZ and BD mania.
Neuroplastogens (ketamine, psilocybin, and related TrkB-binding compounds) are mechanistically
distinguished from classical antidepressants by binding affinity: psilocin and LSD bind TrkB at
roughly 1,000-fold higher affinity than fluoxetine (Moliner et al. 2023). This is the direct
mechanistic link to the ARPA-H EVIDENT program (Evidence-based validation for behavioral-health
therapeutics, $139.4M, first 13 teams announced April 21, 2026), which funds objective,
biomarker-based responder identification for neuroplastogens, neuromodulation, and digital
therapeutics.

### 5.2 Meso: connectomic nodes, edges, and subgraphs

The connectomic treatment-mapping logic privileges edges (the relationship between two regions) over
nodes (a single region's activity level), because edges are what map onto interventions. The
canonical example, the dlPFC-sgACC anticorrelation targeted by SAINT/SNT in depression, generalizes
across disorders: the OFC-caudate cortico-striato-thalamo-cortical (CSTC) loop in OCD and Tourette
syndrome (FDA-cleared deep TMS targeting dorsal mPFC and ACC, 2018), the nucleus accumbens-OFC/vmPFC
reward circuit across substance use disorders, and the default-mode network's internal core
(posterior cingulate cortex/precuneus to medial PFC), which is hyperconnected in MDD and SCZ
(rumination, self-referential processing) and hypoconnected in PTSD and ASD (reduced within-network
integration). Subgraph-level treatment targeting (an entire functional network rather than a single
edge) is least mature but conceptually anchors network-based neuromodulation approaches beyond
single-target TMS.

### 5.3 Macro: symptom-scale outcomes

PHQ-9, GAD-7, PANSS, and YMRS function as the macro-level readouts that close the loop back to the
RDoC/HiTOP crosswalk (Section 3): each instrument's items are individually mapped to RDoC constructs
and HiTOP dimensions in `_MASTER_ontology_mapping.csv`, allowing an outcome-scale score change to be
interpreted as movement along a specific dimensional axis rather than only as a change in an
aggregate symptom count.

---

## 6. Open questions and limitations

- **Replication.** The Drysdale et al. (2017) four-biotype MDD solution failed external replication
  (Dinga et al. 2019); the Williams iMAP (2024) six-axis scaffold is the current best-supported
  alternative but itself awaits further independent replication.
- **State versus trait.** Several micro-level findings (BDNF in MDD and BD, glutamate in SCZ) are
  state-dependent, tracking illness episode rather than trait vulnerability; this complicates their
  use as stable biomarkers and should be stated explicitly wherever the figure implies a static
  biotype.
- **Region-to-function mapping.** Allen Human Reference Atlas anatomical parcels do not map 1:1 onto
  the functional regions and networks reported in the primary literature (dlPFC, sgACC, default mode
  network); approximations are flagged in the source transdiagnostic-meso synthesis and should be
  preserved as flagged, not silently resolved, in any downstream figure or publication.
- **Genomic factor loadings.** As noted in Section 2, this synthesis currently uses categorical
  disorder-to-factor assignment; continuous per-disorder loadings from Grotzinger et al. (2025)
  supplementary materials are not yet extracted and should be added before external submission.
- **Scope boundary.** OCD, autism, ADHD, Tourette syndrome, eating disorders, and substance use
  disorders are fully represented in the underlying transdiagnostic canon but are treated as outside
  the core scope of this particular map; extending the figure to them is a filter change, not new
  research, and should be flagged as future work rather than silently expanded.
- **Excluded by design.** A genome-derived, transcription-factor-region-restricted polygenic scoring
  method that reconstructs the same molecular axes noninvasively from genotype alone exists in a
  separate confidential internal dossier (BDNF/TrkB Neuroplasticity Axes Dossier, Section 5). It is
  the proprietary platform layer and is intentionally and permanently excluded from this document and
  from any consortium-facing or published material derived from it.

---

## 7. References to add before external submission

The following citations are used above by author/year/venue but have not yet been verified against
full bibliographic records (DOI, page numbers, volume/issue) in this dossier; complete before
submission:

- Grotzinger, A.D. et al. "Mapping the genetic landscape across 14 psychiatric disorders." *Nature*, 2025. doi:10.1038/s41586-025-09820-3.
- Michelini, G., Palumbo, I.M., DeYoung, C.G., Latzman, R.D., Kotov, R. "Linking RDoC and HiTOP: A new interface for advancing psychiatric nosology and neuroscience." *Clinical Psychology Review*, 2021.
- Moliner, R. et al. "Psychedelics promote plasticity by directly binding to BDNF receptor TrkB." *Nature Neuroscience*, 2023. doi:10.1038/s41593-023-01316-5.
- Casarotto, P.C., Umemori, J., Castren, E. et al. "Antidepressant drugs act by directly binding to TRKB neurotrophin receptors." *Cell*, 2021. PMID:33606976.
- Cole, E.J. et al. Stanford Accelerated Intelligent Neuromodulation Therapy (SAINT/SNT) remission rate, 2022 (full citation and journal to confirm).
- Drysdale, A.T. et al. "Resting-state connectivity biomarkers define neurophysiological subtypes of depression." *Nature Medicine*, 2017 (original four-biotype paper, needs full citation).
- Dinga, R. et al. Replication failure of Drysdale et al. (2017) biotypes, 2019 (needs full citation and venue).
- Williams, L.M. et al. iMAP six-axis depression biotype scaffold (n=801), 2024 (needs full citation).
- Clementz, B.A., Tamminga, C.A. et al. B-SNIP consortium biotype paper, 2016 (needs full citation).
- Ruzicka, W.B. et al. Single-nucleus RNA-seq excitatory neuron findings in schizophrenia, 2024 (needs full citation).
- Castren, E., Saarma, M. "iPlasticity" framework reviews, 2022 (needs full citation).

---

## Appendix: source canon used

This synthesis draws directly on the following canonical Cytognosis assets, all current as of the
2026-07-16 dossier index: `BIOTYPING_DOSSIER_INDEX.md`; `BIOTYPES_CHEATSHEET_v2.md`;
`BDNF_TrkB_Neuroplasticity_Axes_Dossier_2026-06-03.md` (Sections 1-3 only, publishable science;
Section 5 excluded per above); `transdiagnostic-micro.md`, `transdiagnostic-meso.md` (including its
`VISUAL_DATA` machine-readable block), and `transdiagnostic-macro.md`; the RDoC-HiTOP harmonization
matrices (`matrix_hitop_disease.csv`, `matrix_rdoc_disease.csv`, and the underlying
`matrix_hitop.csv`/`matrix_hitop_extended.csv`/`matrix_hitop_weighted.csv` crosswalk chain);
`_MASTER_ontology_mapping.csv` and the DSM-5-TR cross-cutting mapping set; `NbN.csv`, `NbN_extended.csv`,
and `NbN_Glossary.md`.
