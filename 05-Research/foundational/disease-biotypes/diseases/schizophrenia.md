# Biotypes: Schizophrenia

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: researchers, stakeholders
> **Tags**: `literature-synthesis`, `disease-biotypes`, `schizophrenia`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

Genomic factor loading (Nature 2025): **SB factor** (schizophrenia + bipolar disorder), the cross-disorder genetic axis whose shared signal is enriched in genes expressed in excitatory neurons. Schizophrenia is the prototypical loader on this factor; its factor-specific genetic signal converges on synaptic and excitatory-neuronal biology rather than glia or peripheral immune cells (Grotzinger et al., Nature 2025, doi:10.1038/s41586-025-09820-3).

This document harmonizes schizophrenia biotype evidence across three scales: MICRO (molecular/genetic/cellular/immune, mapped to Gene Ontology), MESO (connectomic fMRI/EEG/MEG, mapped to the Allen Human Reference Atlas 3D 2020), and MACRO (phenotype, mapped to SNOMED CT and HPO). It reuses findings from the parent psychosis review and the EEG/MEG and molecular/cellular cross-cutting reviews, and updates them with 2024 to 2026 literature.

---

## Seed papers

- Trubetskoy V, Pardinas AF, Qi T, et al. Mapping genomic loci implicates genes and synaptic biology in schizophrenia. Nature. 2022;604:502-508. doi:10.1038/s41586-022-04434-5 (PGC3 GWAS, 287 loci)
- Singh T, Poterba T, Curtis D, et al. Rare coding variants in ten genes confer substantial risk for schizophrenia. Nature. 2022;604:509-516. doi:10.1038/s41586-022-04556-w (SCHEMA)
- Grotzinger AD, Werme J, Peyrot WJ, et al. Mapping the genetic landscape across 14 psychiatric disorders. Nature. 2025. doi:10.1038/s41586-025-09820-3
- Clementz BA, Sweeney JA, Hamm JP, et al. Identification of distinct psychosis biotypes using brain-based biomarkers. Am J Psychiatry. 2016;173:373-384. doi:10.1176/appi.ajp.2015.14091200 (B-SNIP Biotypes 1-3)
- Howes OD, Onwordi EC. The hypothesis of biologically based subtypes of schizophrenia: a 10-year update. World Psychiatry. 2025;24:46-47. doi:10.1002/wps.21265 (Type A / Type B continuum)
- McCutcheon RA, Krystal JH, Howes OD. Dopamine and glutamate in schizophrenia. World Psychiatry. 2020;19:15-33. doi:10.1002/wps.20693
- Ruzicka WB, Mohammadi S, Fullard JF, et al. Single-cell multi-cohort dissection of the schizophrenia transcriptome. Science. 2024;384:eadg5136. doi:10.1126/science.adg5136
- Sekar A, Bialas AR, de Rivera H, et al. Schizophrenia risk from complex variation of complement component 4. Nature. 2016;530:177-183. doi:10.1038/nature16549

---

## MICRO scale (molecular / genetic / cellular / immune) vs GO-harmonized

Each neurotransmitter family is marked individually. The recurring mechanistic spine of schizophrenia molecular biology is a cortical microcircuit lesion: NMDA hypofunction on parvalbumin (PV) interneurons disinhibits pyramidal cells, degrades gamma-band synchrony, and (via hippocampal disinhibition through the subiculum-accumbens-pallidum-VTA loop) drives associative-striatal hyperdopaminergia. Oxidative stress on PV cells and complement-mediated over-pruning of excitatory synapses sit upstream and parallel to this lesion.

| Biotype / dysregulation | GO term(s) + ID | Specific finding (genes, variants, molecules) | Neurotransmitter family | BDNF / neurotrophin + plasticity? | E/I imbalance (+ region) | Oxidative / mito / ROS? | Immune / inflammatory? | Confidence | Source (author year, DOI) |
|---|---|---|---|---|---|---|---|---|---|
| Associative-striatal presynaptic hyperdopaminergia | G protein-coupled dopamine receptor signaling pathway GO:0007212; regulation of dopamine secretion GO:0014059 | Elevated [18F]-DOPA dopamine synthesis capacity, largest in associative striatum (dorsal caudate, anterior putamen), not limbic striatum; meta-analytic d~0.8 | **Dopamine** (primary) | not central to this axis | downstream of upstream hippocampal/PV disinhibition | no | no | HIGH | McCutcheon 2019 doi:10.1016/j.tins.2018.12.004; Howes 2025 doi:10.1002/wps.21265 |
| NMDA-receptor hypofunction (glutamatergic) | glutamate receptor signaling pathway GO:0007215; regulation of glutamate receptor signaling GO:1900449; chemical synaptic transmission GO:0007268 | NMDA hypofunction on PV interneurons; elevated ACC glutamate/glutamine on 1H-MRS, especially in treatment-resistant cases; GRIN2A and GRIA3 risk genes | **Glutamate** (primary) | none reported here | E-up (pyramidal disinhibition) in ACC and DLPFC; glutamate elevated in anterior cingulate | no | no | HIGH (MRS in TRS, GWAS); MEDIUM (causal direction) | Marsman 2013 doi:10.1093/schbul/sbr069; Mouchlianitis 2016; Egerton 2023 doi:10.1038/s41386-022-01508-w |
| PV interneuron / GABA deficit and gamma loss | gamma oscillation generation (approx, needs curation; relates to regulation of neuronal synaptic plasticity GO:0048168); GABAergic synaptic transmission GO:0051932 | Reduced PV interneuron density (Hedges g~-0.27) and PV mRNA, reduced GAD67 in DLPFC layers III-IV and hippocampal CA1; predicts reduced 40-Hz ASSR | **GABA** (primary) | none reported here | I-down (PV interneurons) in DLPFC and hippocampal CA1; net E-up | links to redox (see oxidative row) | no | HIGH (postmortem, multi-cohort) | Lewis 2012 doi (PMC3253230); Kaar 2019 (PMC6856257) |
| C4 / complement-mediated synaptic over-pruning | complement activation GO:0006956; synapse pruning GO:0098883; microglial cell activation GO:0001774 | Increased C4A copy number raises risk; ~40% elevated C4A expression in postmortem cortex; complement tags synapses for microglial removal | none reported (immune-glial) | reduces synapse/spine density (anti-plasticity) | indirectly lowers excitatory synapse density, layer III pyramidal cells | no | **yes** (complement, microglia) | HIGH (genetics + mouse mechanism) | Sekar 2016 doi:10.1038/nature16549 |
| Oxidative stress / glutathione deficit on PV cells | response to oxidative stress GO:0006979; glutathione metabolic process GO:0006749 | Reduced or high-variance anterior cingulate glutathione (GSH) on MRS; redox imbalance damages fast-spiking PV interneurons (Do/Cabungcal model) | none reported directly | redox damage impairs PV-dependent plasticity | exacerbates I-down (PV) in ACC and PFC | **yes** (GSH down, ROS up; mito implicated) | partial (redox-inflammation crosstalk) | MEDIUM (variance effect; subset-specific) | Iwata 2018; Murray 2022 (PMC8669304) |
| Peripheral / kynurenine inflammation | inflammatory response GO:0006954; kynurenine metabolic process GO:0097052; tryptophan catabolic process GO:0006569 | Elevated IL-6, CRP, TNF-alpha (subset ~30-40%); childhood IL-6/CRP predicts adult psychosis (ALSPAC); elevated brain/CSF kynurenic acid (NMDA + a7-nicotinic antagonist) | none direct; KYNA modulates Glutamate/ACh | cytokines downregulate BDNF | KYNA contributes to NMDA hypofunction (E/I shift) | redox crosstalk via IDO | **yes** (cytokines, kynurenine) | MEDIUM (subset); HIGH (childhood IL-6 MR) | Khandaker 2014; Goldsmith 2016 doi:10.1038/mp.2016.3; Erhardt 2017 |
| BDNF / neurotrophin reduction | neurotrophin TRK receptor signaling pathway GO:0048011; regulation of synaptic plasticity GO:0048167 | Reduced peripheral BDNF (smaller effect than MDD); reduced BDNF mRNA in DLPFC/hippocampus in some postmortem cohorts; BDNF+TNF haplotypes predict cognitive impairment | none direct (neurotrophin) | **yes**: low BDNF/TrkB, reduced iPlasticity; plasticity-deficit subset | contributes to I-down via PV-TrkB coupling | indirect (BDNF supports mito biogenesis) | BDNF x TNF interaction | MEDIUM | Fernandes 2015; Ray 2014 doi:10.1038/tp.2014.26 |
| Excitatory-neuron transcriptomic convergence | regulation of synapse organization GO:0050807; nervous system development GO:0007399 | snRNA-seq of DLPFC (140 subjects, McLean + Mount Sinai): excitatory neurons most transcriptionally altered; cell-type DE overlaps GWAS loci | **Glutamate** (excitatory neurons) | synaptic/neurodevelopmental pathways | E-cell-centric dysregulation, DLPFC | no | no | HIGH | Ruzicka 2024 doi:10.1126/science.adg5136 |
| Common-variant polygenic risk (SB factor) | regulation of trans-synaptic signaling GO:0099177; calcium ion transmembrane transport GO:0070588 | PGC3: 287 loci, neuron-enriched, synaptic (CACNA1C, GRIN2A, GRIA3); SB factor enriched in excitatory-neuron-expressed genes; PRS explains ~7-10% liability | **Glutamate, Dopamine** (synaptic) | synaptic-plasticity genes implicated | broad synaptic E/I genes | no | no | HIGH | Trubetskoy 2022 doi:10.1038/s41586-022-04434-5; Grotzinger 2025 doi:10.1038/s41586-025-09820-3 |
| Rare large-effect variants | covalent chromatin modification GO:0016569 (SETD1A); glutamate receptor signaling GO:0007215 (GRIN2A) | SCHEMA: SETD1A (OR ~20, LoF), GRIN2A, GRIA3, CACNA1G, TRIO, SP4, RB1CC1, XPO7, CUL1, HERC1; up to ~20% of early-onset psychosis carry rare GRIN2A variants | **Glutamate** (GRIN2A, GRIA3) | none direct | glutamatergic-deficit subgroup | no | no | HIGH (SCHEMA); MEDIUM (subgroup treatment implication) | Singh 2022 doi:10.1038/s41586-022-04556-w; GRIN2A 2025 doi:10.1038/s41380-025-03279-4 |
| 22q11.2 deletion CNV | (syndromic; multiple GO processes) | ~25-fold elevated risk; ~25% develop schizophrenia spectrum; reduced cortical surface area, altered subcortical volumes; reciprocal duplication protective | mixed (DGCR8, COMT in interval) | none direct | regional cortical disruption | mito genes in interval (e.g., MRPL40) | no | HIGH (genetics); identifiable in advance | Schneider 2014; Sun 2020 doi:10.1038/s41380-018-0078-5 |

Notes on GO IDs: "gamma oscillation generation" does not have a single canonical GO biological-process ID; the closest curated anchors are regulation of neuronal synaptic plasticity (GO:0048168) and chemical synaptic transmission (GO:0007268), flagged as approx, needs curation. GO:0006979 (oxidative stress), GO:0006956 (complement activation), GO:0001774 (microglial activation), GO:0007212/GO:0007215 (dopamine/glutamate signaling), GO:0006954 (inflammatory response), and GO:0048011 (neurotrophin TRK signaling) are confirmed against AmiGO/MGI.

---

## MESO scale (connectomic) vs Allen Atlas nodes + edges

Functional labels are given in parentheses after the containing Allen Human Reference Atlas 3D (2020) anatomical structure. Several psychosis findings are reported for functional networks (DMN, thalamocortical) that are not 1:1 with Allen anatomical parcels; for each I name the Allen anatomical structure that contains the functional region.

### NODES

| Allen region (functional label) | Observed change | Modality | Confidence | Source |
|---|---|---|---|---|
| Middle frontal gyrus / superior frontal gyrus (dorsolateral prefrontal cortex, DLPFC / BA9, BA46) | Cortical thinning; reduced activation; smallest gray matter in B-SNIP BT1 | structural / fMRI | HIGH | van Erp 2018 (PMC6177304); Clementz 2016 doi:10.1176/appi.ajp.2015.14091200 |
| Cingulate gyrus, anterior part (anterior cingulate cortex, ACC / BA24, BA32) | Elevated glutamate/glutamine (MRS), most marked in treatment-resistant cases; reduced GSH | MEG/MRS/fMRI | HIGH (TRS glutamate); MEDIUM (GSH) | Mouchlianitis 2016; Egerton 2023 doi:10.1038/s41386-022-01508-w |
| Superior temporal gyrus, including transverse temporal gyrus (Heschl's gyrus, primary auditory cortex / BA41-42, planum temporale) | Thinning; overactive sensory response and reduced 40-Hz ASSR; aberrant connectivity tracks hallucinations | structural / EEG / MEG | HIGH | Clementz 2016; Schijven 2023 doi:10.1073/pnas.2213880120 |
| Hippocampal formation, anterior (anterior hippocampus, CA1 subfield) | Hyperactivity / elevated CA1 cerebral blood volume; spreads anteriorly over illness course | fMRI (CBV) | HIGH | Schobel 2013 (PMC4141978); McHugo 2019 doi:10.1176/appi.ajp.2019.19020151 |
| Thalamus, mediodorsal nucleus (mediodorsal thalamus) | Altered connectivity; differentiates SCZ from non-psychotic bipolar; sleep-spindle deficit substrate | fMRI / EEG | HIGH | Woodward 2012 doi:10.1176/appi.ajp.2012.12010056; Baran 2019 doi:10.1016/j.bpsc.2019.04.012 |
| Thalamus, pulvinar (visual thalamus / pulvinar) | Altered connectivity in psychotic groups (SCZ and psychotic BD) | fMRI | MEDIUM | Anticevic 2014 (PMID 25031221) |
| Caudate nucleus and putamen, dorsal/anterior (associative striatum) | Elevated dopamine synthesis capacity; enlarged basal ganglia in HYDRA SG2 (partly medication) | PET / structural | HIGH | McCutcheon 2019; Chand 2020 doi:10.1093/brain/awaa025 |
| Cerebellar hemisphere, posterior lobe (Crus I/II) and vermis | Volume reduction; weaker cerebello-cortical connectivity; negative-symptom correlate | structural / fMRI | MEDIUM | Brady 2019 doi:10.1176/appi.ajp.2018.18040429; Bernard 2019 |
| Precuneus / posterior cingulate gyrus (posterior DMN hub) | Hyperconnectivity / hyperactivity (DMN) | fMRI | HIGH (DMN); LOW specificity | Whitfield-Gabrieli 2009 doi:10.1073/pnas.0809141106 |
| Insular cortex (insula) | Thinning; increased structural variability | structural | MEDIUM | Brouwer 2024 doi:10.1176/appi.ajp.20230806 |

### EDGES

| Region A vs Region B (functional labels) | Association sign | Observed change in disorder | Modality | Confidence | Source |
|---|---|---|---|---|---|
| Thalamus, mediodorsal/whole (thalamus) vs postcentral & precentral gyrus (sensorimotor cortex) | positive | Hyperconnectivity (thalamus over-coupled to sensorimotor cortex); magnitude predicts symptom severity and CHR conversion | fMRI | HIGH (transdiagnostic, replicated) | Anticevic 2014; Anticevic 2015 (PMC4892891) |
| Thalamus (thalamus) vs middle/superior frontal gyrus (prefrontal cortex) | negative (anticorrelation) | Hypoconnectivity (thalamus under-coupled to prefrontal and to striatum/cerebellum); reciprocal to the sensorimotor hyperconnectivity | fMRI | HIGH | Woodward 2012; Anticevic 2014 |
| Precuneus/posterior cingulate (PCC) vs medial frontal gyrus (mPFC) [DMN core] | positive | DMN hyperconnectivity; present in chronic SCZ, FEP, CHR, and unaffected relatives (endophenotype) | fMRI | HIGH (finding); LOW (specificity) | Whitfield-Gabrieli 2009; Hu 2017 |
| Anterior hippocampus CA1 (hippocampus) vs caudate/putamen (associative striatum) | positive | Hippocampal disinhibition drives striatal dopamine via subiculum-accumbens-pallidum-VTA loop (Grace model) | fMRI / mechanistic | HIGH (mechanism); MEDIUM (in vivo human edge) | Grace 2016 doi:10.1038/nrn.2016.57; Schobel 2013 |
| Thalamus, mediodorsal (thalamus) vs middle frontal gyrus (prefrontal cortex) [spindle circuit] | positive (normally) | Reduced spindle-related thalamocortical coupling; sleep spindle density reduced (NREM2, 11-16 Hz) | EEG (sleep) | HIGH (spindle deficit replicated) | Baran 2019; Ferrarelli/Manoach meta-analysis 2021 |
| Cerebellar hemisphere Crus I/II (cerebellum) vs middle frontal gyrus (prefrontal cortex) | positive (normally) | Reduced cerebello-prefrontal connectivity, associated with negative symptoms; target of cerebellar rTMS | fMRI | MEDIUM | Brady 2019 |
| Superior temporal/Heschl's (auditory cortex) vs inferior frontal gyrus (Broca / language network) | mixed | Aberrant auditory-language connectivity associated with auditory verbal hallucinations | MEG / fMRI | MEDIUM | MEG SCZ connectivity review 2023 |

### EEG/MEG evoked and oscillatory markers (cortical-source, mapped to nodes above)

| Marker | Direction | Allen source region | Mechanistic anchor | Confidence | Source |
|---|---|---|---|---|---|
| 40-Hz auditory steady-state response (ASSR) | reduced power and phase-locking | transverse temporal gyrus (auditory cortex) | PV / GABA-A and NMDA microcircuit integrity | HIGH (>30 samples, g~0.8) | 40-Hz ASSR meta-analysis JAMA Psychiatry 2016 (PMID 27732692) |
| Mismatch negativity (MMN, duration/frequency) | reduced amplitude | superior temporal gyrus + middle frontal gyrus | NMDA-dependent superficial-layer auditory microcircuit | HIGH (g~1.0 chronic; predicts CHR conversion) | Erickson 2016 (PMID 26444073) |
| P3b (oddball) | reduced amplitude, prolonged latency | precuneus / inferior parietal + frontal | attentional resource allocation; endophenotype (present in relatives) | HIGH (g~0.85) | Earls 2016; COGS-2 |
| Sleep spindle density (NREM2) | reduced | thalamus (reticular/mediodorsal) -> cortex | thalamic reticular PV-circuit / thalamocortical | HIGH (multi-lab, present in relatives) | Manoach/Ferrarelli meta-analysis 2021 |
| EEG microstate D | shortened duration/occurrence | dorsal attention network (frontoparietal) | dynamic network instability; endophenotype | MEDIUM-HIGH | da Cruz 2020 doi:10.1038/s41467-020-16914-1 |
| Aperiodic 1/f slope | flatter (mixed) | broadband cortical | E/I balance proxy (flatter = excitatory bias) | MEDIUM (mixed replication) | Donoghue 2025 doi:10.1111/ejn.70255 |

---

## MACRO scale (phenotype) vs SNOMED CT / HPO

| Biotype phenotype | SNOMED CT term + ID | HPO term + ID | Short description of observations | Source |
|---|---|---|---|---|
| Schizophrenia (disorder, umbrella) | Schizophrenia 58214004 | Schizophrenia HP:0100753 | Persistent psychosis with positive, negative, cognitive, and disorganized dimensions; >=6 months with >=1 month characteristic symptoms | findacode SNOMEDCT 58214004; HPO |
| Positive dimension, auditory verbal hallucinations | Hallucinations 7011001; Auditory hallucinations 45403008 | Hallucinations HP:0000738; Auditory hallucination HP:0008765 (approx, needs curation) | Perceptual experiences without external stimulus; map to aberrant auditory cortex / language-network connectivity; low-frequency rTMS target | Clementz 2016; SNOMED |
| Positive dimension, delusions / paranoia | Delusions 2073000 | Delusion HP:0000746 | Fixed false beliefs; mechanistically tied to aberrant-salience from associative-striatal hyperdopaminergia (Type A) | Howes 2025; SNOMED |
| Negative dimension, avolition / anhedonia / alogia | Negative symptom of schizophrenia 16990005 (approx, needs curation) | Avolition HP:0031589 (approx, needs curation); Anhedonia HP:0033676 | Reduced motivation, pleasure, speech output; correlate with prefrontal thinning and cerebello-prefrontal hypoconnectivity; TMS / cerebellar target | Walton 2017; Brady 2019; HPO |
| Cognitive dimension, working memory / processing-speed deficits | Cognitive impairment 386806002 (general) | Cognitive impairment HP:0100543; Impaired working memory HP:0500024 (approx) | Broad neurocognitive deficit; severe in B-SNIP BT1 and HYDRA SG1; PV/gamma and DLPFC substrate | Hill 2025 ADEPT-2; Clementz 2016 |
| Disorganization dimension, formal thought disorder | Disorganized schizophrenia / hebephrenic 35252006 (approx) | Disorganized speech HP:0033714 (approx, needs curation) | Loosened associations, derailment; ties to microstate-D instability and thalamocortical dysconnectivity | da Cruz 2020 |
| Sensory gating / sensorimotor disturbance | (no precise SNOMED concept; approx, needs curation) | Abnormal sensory gating (approx, needs curation) | Reduced P50 gating and PPI; prominent in B-SNIP BT2 (sensory-hyperresponsive) | Swerdlow 2017; Clementz 2016 |

HPO note: HP:0100753 ("Schizophrenia") and HP:0000738 (Hallucinations) / HP:0000746 (Delusions) are confirmed. Several finer terms (Auditory hallucination, Avolition, disorganized-speech codes) are marked approx, needs curation pending direct HPO/SNOMED lookup. SNOMED 58214004 (Schizophrenia), 7011001 (Hallucinations), and 2073000 (Delusions) are confirmed.

---

## Interventional studies (incl. neuromodulation, DBS, neuroplastogens)

| Biotype it targets | Intervention (class + specific) | Study (author year, design, n) | Outcome | Confidence | Source |
|---|---|---|---|---|---|
| Hyperdopaminergic / Type A (positive symptoms) | D2 antagonist / partial-agonist antipsychotics (risperidone, haloperidol, aripiprazole) | Pooled clinical evidence; D2 occupancy 65-80% required | ~two-thirds respond; response tracks elevated striatal DA synthesis | HIGH | Howes & Kapur 2014; McCutcheon 2020 doi:10.1002/wps.20693 |
| Treatment-resistant / Type B (glutamatergic) | Clozapine | Kane 1988 RCT; meta-analyses | Effective in ~60% of treatment-resistant cases; non-responders show normal striatal DA but elevated ACC glutamate | HIGH | Kane 1988; Mouchlianitis 2016 |
| Type A and broad spectrum (positive + some negative) | Muscarinic M1/M4 agonist + peripheral antagonist (xanomeline-trospium, Cobenfy / KarXT) | EMERGENT-2 and -3, 5-week RCTs, 470 adults; FDA-approved Sep 2024 | Significant PANSS total reduction vs placebo; first non-dopaminergic mechanism approved; works via cholinergic modulation of dopamine/glutamate circuits | HIGH (registration trials); MEDIUM (biotype stratification untested) | BMS 2024; Frontiers Pharmacol 2026 doi:10.3389/fphar.2026.1774437 |
| Clozapine-resistant subgroup | ECT augmentation of clozapine | Petrides 2015 RCT; Lally 2016 meta-analysis | Response in ~54-66% of clozapine-resistant cases; correlates with hippocampal volume change | MEDIUM-HIGH | Petrides 2015; Lally 2016 |
| Negative-symptom / prefrontal-deficit biotype | High-frequency rTMS to left DLPFC | Multiple RCTs and meta-analyses | Modest benefit for negative symptoms | MEDIUM | rTMS reviews (parent doc) |
| Auditory-hallucination / temporal biotype (B-SNIP BT2-like) | Low-frequency rTMS to left temporoparietal cortex | 2024 RCT, n=62, sham-controlled | Active superior to sham for auditory verbal hallucinations; effect scaled to TMS-induced electric field | MEDIUM | JAMA Netw Open 2024 |
| Cerebellar / cognitive-affective biotype | Cerebellar rTMS / iTBS (vermis, lateral hemispheres) | Early trials (Brady-line) | Restored cerebello-prefrontal connectivity and reduced negative symptoms in pilot work | LOW-MEDIUM (pilot) | Brady 2019 doi:10.1176/appi.ajp.2018.18040429 |
| Auditory-hallucination biotype | tDCS (cathodal left temporoparietal, anodal left DLPFC) | Brunelin 2012 RCT and successors | Reduced refractory auditory verbal hallucinations; replication mixed | MEDIUM (Brunelin); LOW (overall replication) | Brunelin 2012 |
| Oxidative-stress / GSH-deficit biotype | N-acetylcysteine (glutathione precursor) | Berk 2008 RCT; Yolland 2020 meta-analysis | Modest benefit for total and negative symptoms at >=24 weeks; effect concentrated in chronic SCZ (consistent with a redox-positive subgroup) | MEDIUM | Yolland 2020 doi:10.1177/0269881119899428 |
| Glutamatergic / Type B (adjunct) | NMDA-glycine-site and GlyT1 modulators (sarcosine, glycine, bitopertin) | Multiple adjunct trials | Small, inconsistent benefit for negative symptoms; bitopertin Phase 3 largely negative; stratification weak | LOW | McCutcheon 2020; Park 2025 |
| Inflammatory subgroup (high CRP) | Anti-inflammatory adjuncts (minocycline, celecoxib, omega-3, NAC) | Various RCTs | Mixed; benefit plausibly limited to high-inflammation subset; no deployed stratification threshold | LOW | Pillinger 2023 doi:10.1016/S2215-0366(23)00056-1 |
| Refractory whole-disorder (experimental) | Deep brain stimulation (DBS): targets trialed include nucleus accumbens, ventral striatum/ALIC, substantia nigra pars reticulata, mediodorsal thalamus, habenula | Small open-label and case series (<25 patients total across targets) | Preliminary, heterogeneous; no controlled efficacy established; remains experimental for treatment-refractory schizophrenia | LOW (experimental) | Gault et al. DBS-for-SCZ reviews; parent psychosis doc |

DBS note: unlike sgACC DBS for TRD or NAc/ALIC DBS for OCD, DBS for schizophrenia has no controlled efficacy evidence. The most-discussed candidate targets follow the circuit logic above: associative striatum / NAc and mediodorsal thalamus (dopaminergic and thalamocortical nodes) and substantia nigra (dopamine source). All remain at the case-series stage and are flagged experimental.

---

## Most defensible biotypes (cross-scale synthesis)

The following five biotypes integrate the three scales. They are not mutually exclusive; a single person may load on two or three. Replication strength and regional specificity rank them.

### Biotype 1: Atrophy-dominant cognitive-deficit psychosis
- **MICRO:** excitatory-neuron transcriptomic dysregulation (Ruzicka 2024), PV/GABA deficit, polygenic SB-factor load.
- **MESO (anchor Allen regions):** middle/superior frontal gyrus (DLPFC), superior temporal gyrus, anterior hippocampal formation (CA1), thalamus mediodorsal nucleus, anterior cingulate gyrus. EEG: reduced P3b, reduced 40-Hz ASSR.
- **MACRO:** severe cognitive deficit, negative symptoms.
- **Why defensible:** converges across B-SNIP BT1, HYDRA SG1, ENIGMA frontotemporal thinning, and NAPLS3 prodromal thinning. Confidence HIGH.

### Biotype 2: Sensory-hyperresponsive, gating-impaired psychosis
- **MICRO:** PV-interneuron loss producing gamma-band deficits; elevated cortical glutamate; redox stress on PV cells.
- **MESO (anchor Allen regions):** transverse temporal gyrus / Heschl's (auditory cortex), postcentral/precentral gyrus (sensorimotor), thalamus (mediodorsal). Edge: thalamus-sensorimotor positive hyperconnectivity. EEG: reduced P50 gating, reduced 40-Hz ASSR.
- **MACRO:** auditory hallucinations, sensory-gating failure.
- **Why defensible:** EEG-gating, MRS-glutamate, and thalamocortical-fMRI converge; auditory cortex is optically accessible. Confidence MEDIUM-HIGH.

### Biotype 3: Hyperdopaminergic striatal psychosis (Howes Type A)
- **MICRO axes:** associative-striatal presynaptic hyperdopaminergia (GO:0007212), driven upstream by hippocampal CA1 disinhibition.
- **MESO (anchor Allen regions):** caudate/putamen, dorsal/anterior (associative striatum), anterior hippocampus CA1. Edge: hippocampus-striatum positive (subiculum-accumbens-pallidum-VTA loop).
- **MACRO:** delusions, paranoia, aberrant salience; good first-line antipsychotic response.
- **Why defensible:** decades of PET dopamine evidence plus the most-replicated upstream circuit finding; treatment response is the clinical anchor. Confidence HIGH.

### Biotype 4: Treatment-resistant glutamatergic psychosis (Howes Type B)
- **MICRO axes:** elevated anterior cingulate glutamate, normal/low striatal dopamine, enrichment for glutamatergic rare variants (GRIN2A, SETD1A).
- **MESO (anchor Allen regions):** cingulate gyrus anterior part (ACC), thalamus (mediodorsal and pulvinar), DLPFC.
- **MACRO:** persistent positive and negative symptoms refractory to D2 blockade.
- **Why defensible:** MRS, treatment-response, and SCHEMA genetics align; clozapine and ECT-augmentation provide treatment-stratified validation. Confidence HIGH (axis); MEDIUM (clean dichotomy; Howes 2025 reframes as a continuum).

### Biotype 5: Immune / C4-pruned and oxidative psychosis
- **MICRO axes:** C4A copy-number-driven synaptic over-pruning (GO:0006956), microglial involvement, elevated IL-6/CRP and kynurenine, ACC glutathione deficit (GO:0006979).
- **MESO (anchor Allen regions):** prefrontal layer-III pyramidal cells (DLPFC), anterior cingulate gyrus, hippocampus (kynurenine-glutamate intersection).
- **MACRO:** broad symptom burden; possible NAC and anti-inflammatory responsiveness in the redox/inflammation-positive subset.
- **Why defensible:** strongest causal evidence is Mendelian randomization on IL-6 plus C4 mouse mechanism; flag TSPO microglial PET as not robustly replicated and the inflammatory subgroup threshold as undefined. Confidence MEDIUM.

**Anchor Allen regions across all five biotypes for an adaptive headset:** middle/superior frontal gyrus (DLPFC), cingulate gyrus anterior part (ACC), superior temporal + transverse temporal gyrus (auditory cortex), anterior hippocampal formation (CA1), and caudate/putamen (associative striatum), with cerebellar Crus I/II as a tier-2 target. These cover the bulk of replicated schizophrenia circuit findings.

**Genomic factor statement:** schizophrenia loads on the **SB factor** of the Nature 2025 five-factor model, the excitatory-neuron-enriched axis it shares with bipolar disorder.

---

## References

1. Grotzinger AD, Werme J, Peyrot WJ, et al. Mapping the genetic landscape across 14 psychiatric disorders. Nature. 2025. doi:10.1038/s41586-025-09820-3
2. Trubetskoy V, Pardinas AF, Qi T, et al. Mapping genomic loci implicates genes and synaptic biology in schizophrenia. Nature. 2022;604:502-508. doi:10.1038/s41586-022-04434-5
3. Singh T, Poterba T, Curtis D, et al. Rare coding variants in ten genes confer substantial risk for schizophrenia. Nature. 2022;604:509-516. doi:10.1038/s41586-022-04556-w
4. GRIN2A null variants confer a high risk for early-onset schizophrenia. Mol Psychiatry. 2025. doi:10.1038/s41380-025-03279-4
5. Clementz BA, Sweeney JA, Hamm JP, et al. Identification of distinct psychosis biotypes using brain-based biomarkers. Am J Psychiatry. 2016;173:373-384. doi:10.1176/appi.ajp.2015.14091200
6. Hill SK, et al. Cognitive performance and differentiation of B-SNIP psychosis Biotypes (ADEPT-2). Schizophr Res Cogn. 2025. PMC12061035
7. Chand GB, Dwyer DB, Erus G, et al. Two distinct neuroanatomical subtypes of schizophrenia revealed using machine learning. Brain. 2020;143:1027-1038. doi:10.1093/brain/awaa025
8. van Erp TGM, Walton E, Hibar DP, et al. Cortical brain abnormalities in 4474 individuals with schizophrenia and 5098 controls via the ENIGMA consortium. Biol Psychiatry. 2018;84:644-654. PMC6177304
9. Schijven D, et al. Large-scale analysis of structural brain asymmetries in schizophrenia via the ENIGMA consortium. PNAS. 2023. doi:10.1073/pnas.2213880120
10. Brouwer RM, et al. Estimating Multimodal Structural Brain Variability in Schizophrenia Spectrum Disorders: A Worldwide ENIGMA Study. Am J Psychiatry. 2024. doi:10.1176/appi.ajp.20230806
11. Whitfield-Gabrieli S, et al. Hyperactivity and hyperconnectivity of the default network in schizophrenia. PNAS. 2009;106:1279-1284. doi:10.1073/pnas.0809141106
12. Hu M-L, et al. A Review of the Functional and Anatomical Default Mode Network in Schizophrenia. Neurosci Bull. 2017.
13. Grace AA. Dysregulation of the dopamine system in the pathophysiology of schizophrenia and depression. Nat Rev Neurosci. 2016;17:524-532. doi:10.1038/nrn.2016.57
14. Schobel SA, Chaudhury NH, Khan UA, et al. Imaging patients with psychosis and a mouse model establishes a spreading pattern of hippocampal dysfunction. Neuron. 2013;78:81-93. PMC4141978
15. McHugo M, et al. Hyperactivity and Reduced Activation of Anterior Hippocampus in Early Psychosis. Am J Psychiatry. 2019. doi:10.1176/appi.ajp.2019.19020151
16. Anticevic A, Cole MW, Repovs G, et al. Characterizing thalamo-cortical disturbances in schizophrenia and bipolar illness. Cereb Cortex. 2014;24:3116-3130. PMID 23825317
17. Anticevic A, Haut K, Murray JD, et al. Association of Thalamic Dysconnectivity and Conversion to Psychosis. JAMA Psychiatry. 2015;72:882-891. PMC4892891
18. Woodward ND, Karbasforoushan H, Heckers S. Thalamocortical dysconnectivity in schizophrenia. Am J Psychiatry. 2012;169:1092-1099. doi:10.1176/appi.ajp.2012.12010056
19. Baran B, et al. Increased Thalamocortical Connectivity in Schizophrenia Correlates With Sleep Spindle Deficits. Biol Psychiatry CNNI. 2019. doi:10.1016/j.bpsc.2019.04.012
20. McCutcheon RA, Abi-Dargham A, Howes OD. Schizophrenia, dopamine and the striatum. Trends Neurosci. 2019;42:205-220. doi:10.1016/j.tins.2018.12.004
21. Howes OD, Onwordi EC. The hypothesis of biologically based subtypes of schizophrenia: a 10-year update. World Psychiatry. 2025;24:46-47. doi:10.1002/wps.21265
22. McCutcheon RA, Krystal JH, Howes OD. Dopamine and glutamate in schizophrenia. World Psychiatry. 2020;19:15-33. doi:10.1002/wps.20693
23. Brady RO Jr, et al. Cerebellar-Prefrontal Network Connectivity and Negative Symptoms in Schizophrenia. Am J Psychiatry. 2019. doi:10.1176/appi.ajp.2018.18040429
24. Marsman A, van den Heuvel MP, Klomp DWJ, et al. Glutamate in schizophrenia: a focused review and meta-analysis of 1H-MRS studies. Schizophr Bull. 2013;39:120-129. doi:10.1093/schbul/sbr069
25. Mouchlianitis E, et al. Treatment-Resistant Schizophrenia Patients Show Elevated Anterior Cingulate Cortex Glutamate. Schizophr Bull. 2016. PMID 26683625
26. Egerton A, et al. Anterior cingulate glutamate metabolites as a predictor of antipsychotic response in first episode psychosis: STRATA. Neuropsychopharmacology. 2023. doi:10.1038/s41386-022-01508-w
27. Lewis DA, Curley AA, Glausier JR, Volk DW. Cortical parvalbumin interneurons and cognitive dysfunction in schizophrenia. Trends Neurosci. 2012;35:57-67. PMC3253230
28. Pre-frontal parvalbumin interneurons in schizophrenia: a meta-analysis of post-mortem studies (Kaar et al.). Mol Psychiatry. 2019. PMC6856257
29. Iwata Y, et al. Glutathione levels and glutathione-glutamate correlation in schizophrenia (meta-analysis). 2018; Murray et al. variance meta-analysis 2022. PMC8669304
30. Sekar A, Bialas AR, de Rivera H, et al. Schizophrenia risk from complex variation of complement component 4. Nature. 2016;530:177-183. doi:10.1038/nature16549
31. Khandaker GM, et al. Association of serum interleukin 6 and CRP in childhood with depression and psychosis. JAMA Psychiatry. 2014;71:1121-1128.
32. Goldsmith DR, et al. A meta-analysis of blood cytokine network alterations in psychiatric patients. Mol Psychiatry. 2016;21:1696-1709. doi:10.1038/mp.2016.3
33. Erhardt S, et al. The kynurenine pathway in schizophrenia and bipolar disorder. Neuropharmacology. 2017;112:297-306.
34. Pillinger T, et al. Cytokines in psychosis: from mechanism towards treatment and prediction. Lancet Psychiatry. 2023. doi:10.1016/S2215-0366(23)00056-1
35. Fernandes BS, et al. Peripheral brain-derived neurotrophic factor in schizophrenia (meta-analysis). Mol Psychiatry. 2015; Ray MT et al. BDNF mRNA in DLPFC. Transl Psychiatry. 2014. doi:10.1038/tp.2014.26
36. Ruzicka WB, Mohammadi S, Fullard JF, et al. Single-cell multi-cohort dissection of the schizophrenia transcriptome. Science. 2024;384:eadg5136. doi:10.1126/science.adg5136
37. Schneider M, et al. Psychiatric disorders from childhood to adulthood in 22q11.2 deletion syndrome. Am J Psychiatry. 2014;171:627-639; Sun D, et al. Mol Psychiatry. 2020. doi:10.1038/s41380-018-0078-5
38. The 40-Hz Auditory Steady-State Response in Patients With Schizophrenia: A Meta-analysis. JAMA Psychiatry. 2016. PMID 27732692
39. A Meta-Analysis of Mismatch Negativity in Schizophrenia (Erickson et al.). Biol Psychiatry. 2016. PMID 26444073
40. Earls HA, et al. Meta-analytic Review of Auditory ERP Components as Endophenotypes for Schizophrenia. Schizophr Bull. 2016;42:1504-1516.
41. Investigating Sleep Spindle Density and Schizophrenia: A Meta-Analysis (Manoach/Ferrarelli line). Psychiatry Res. 2021.
42. da Cruz JR, et al. EEG microstates are a candidate endophenotype for schizophrenia. Nat Commun. 2020;11:3089. doi:10.1038/s41467-020-16914-1
43. Donoghue T. A Systematic Review of Aperiodic Neural Activity in Clinical Investigations. Eur J Neurosci. 2025. doi:10.1111/ejn.70255
44. Swerdlow NR, et al. Deficient prepulse inhibition in schizophrenia in a multi-site cohort. Schizophr Res. 2017. PMID 28549722
45. Kane J, Honigfeld G, Singer J, Meltzer H. Clozapine for the treatment-resistant schizophrenic. Arch Gen Psychiatry. 1988;45:789-796.
46. Petrides G, et al. Electroconvulsive Therapy Augmentation in Clozapine-Resistant Schizophrenia. Am J Psychiatry. 2015;172:52-58; Lally J, et al. Schizophr Res. 2016. PMID 26827129
47. U.S. FDA Approves Bristol Myers Squibb's COBENFY (xanomeline and trospium chloride). BMS press release, 26 Sep 2024; From dopamine to muscarine: xanomeline-trospium (KarXT). Front Pharmacol. 2026. doi:10.3389/fphar.2026.1774437
48. Repetitive Transcranial Magnetic Stimulation for Auditory Verbal Hallucinations in Schizophrenia: A Randomized Clinical Trial. JAMA Netw Open. 2024.
49. Brunelin J, et al. Examining transcranial direct-current stimulation for refractory auditory verbal hallucinations. Am J Psychiatry. 2012.
50. Yolland CO, et al. N-acetylcysteine in schizophrenia (meta-analysis). J Psychopharmacol. 2020. doi:10.1177/0269881119899428
51. Howes OD, Kapur S. A neurobiological hypothesis for the classification of schizophrenia: type A and type B. Br J Psychiatry. 2014;205:1-3.
52. Park LT, et al. Glutamatergic and serotonergic mechanisms of rapid-acting and psychedelic antidepressants (review). 2025.
53. SNOMED CT concept 58214004 (Schizophrenia); 7011001 (Hallucinations); 2073000 (Delusions). findacode.com / NCBO BioPortal.
54. Human Phenotype Ontology: HP:0100753 (Schizophrenia); HP:0000738 (Hallucinations); HP:0000746 (Delusions); HP:0033676 (Anhedonia). hpo.jax.org.
55. Gene Ontology / AmiGO 2: GO:0006979 (response to oxidative stress); GO:0006956 (complement activation); GO:0001774 (microglial cell activation); GO:0007212 (G-protein-coupled dopamine receptor signaling); GO:0007215 (glutamate receptor signaling); GO:1900449 (regulation of glutamate receptor signaling); GO:0006954 (inflammatory response); GO:0048011 (neurotrophin TRK receptor signaling); GO:0048167 (regulation of synaptic plasticity).
