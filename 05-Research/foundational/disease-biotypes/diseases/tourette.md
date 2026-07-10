# Biotypes: Tourette syndrome (and chronic tic disorders)

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: researchers, stakeholders
> **Tags**: `literature-synthesis`, `disease-biotypes`, `tourette`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

Genomic factor loading (Nature 2025): **Neurodevelopmental factor** (ASD + ADHD + Tourette, childhood-onset) with a substantial secondary loading on the **compulsive/eating factor** (OCD + anorexia + Tourette). Tourette is one of the few disorders in the Grotzinger et al. analysis that loads meaningfully on two factors, which mirrors its clinical reality: childhood-onset neurodevelopmental motor disorder with heavy obsessive-compulsive and attentional comorbidity.

Tourette syndrome (TS) is a childhood-onset neurodevelopmental disorder defined by multiple motor tics and at least one phonic/vocal tic persisting more than one year. The biology converges on the cortico-striato-thalamo-cortical (CSTC) motor loop: a dopaminergic and GABAergic imbalance inside the striatum that releases motor programs the cortex cannot adequately suppress. The genetics point to striatal interneuron development and a small number of high-penetrance rare variants (the histamine gene HDC being the landmark example). The connectomics point to a hyperactive sensorimotor CSTC loop with reduced striatal and motor-cortical inhibition. This document harmonizes molecular findings to Gene Ontology (GO), connectomic findings to the Allen Human Reference Atlas 3D (2020), and phenotypes to SNOMED CT and the Human Phenotype Ontology (HPO). The OCD CSTC framing (excluded from the anxiety document and deferred to OCD) is the natural circuit backbone here, because TS and OCD share both the loop and a genomic factor. We flag two contested areas explicitly: the PANDAS/PANS streptococcal-autoimmune subtype, and the recently negative VMAT2-inhibitor pivotal trials.

## Seed papers

- Grotzinger AD, Werme J, Peyrot WJ, ... Smoller JW. Mapping the genetic landscape across 14 psychiatric disorders. Nature. 2025. doi:10.1038/s41586-025-09820-3. (Organizing reference; places Tourette on the neurodevelopmental factor with a secondary compulsive-factor loading.)
- Yu D, Sul JH, Tsetsos F, ... Scharf JM. Interrogating the genetic determinants of Tourette syndrome and other tic disorders through genome-wide association studies. Am J Psychiatry. 2019;176(3):217-227. doi:10.1176/appi.ajp.2018.18070857. (PGC-TS GWAS; first genome-wide significant locus at FLT3.)
- Tsetsos F, Topaloudi A, Jain P, ... Paschou P. Genome-wide association study meta-analysis of 9,619 cases with tic disorders. Biol Psychiatry. 2024;97(9):S0006-3223(24)01648-2. doi:10.1016/j.biopsych.2024.10.001. (Expanded GWAS; SNP heritability ~13.8%; BCL11B, NDFIP2, RBM26 gene-based hits; still underpowered for replicable single loci.)
- Ercan-Sencicek AG, Stillman AA, Ghosh AK, ... State MW. L-histidine decarboxylase and Tourette's syndrome. N Engl J Med. 2010;362(20):1901-1908. doi:10.1056/NEJMoa0907006. (Rare high-penetrance HDC W317X mutation; the histaminergic anchor.)
- Kataoka Y, Kalanithi PSA, Grantz H, ... Vaccarino FM. Decreased number of parvalbumin and cholinergic interneurons in the striatum of individuals with Tourette syndrome. J Comp Neurol. 2010;518(3):277-291. doi:10.1002/cne.22206. (Postmortem striatal interneuron loss; the core cellular biotype.)
- Worbe Y, Marrakchi-Kacem L, Lecomte S, ... Poupon C. Altered structural connectivity of cortico-striato-pallido-thalamic networks in Gilles de la Tourette syndrome. Brain. 2015;138(2):472-482. doi:10.1093/brain/awu311. (CSTC structural connectivity model.)

## MICRO scale (molecular / genetic / cellular / immune) vs GO-harmonized

TS is highly heritable; twin and family studies place heritability near 0.6-0.8 and the architecture is mixed: highly polygenic common-variant risk plus a small number of rare, high-penetrance variants and copy-number variants [1,2]. The PGC-TS GWAS (Yu et al. 2019) reported the first genome-wide significant locus at FLT3 on chromosome 13q12.2 (rs2504235), which did not replicate in a population-based sample, and estimated SNP heritability around 0.21 [3]. The expanded tic-disorder GWAS meta-analysis (Tsetsos, Topaloudi, Paschou and colleagues 2024; 9,619 cases, 981,048 controls) lowered SNP heritability to ~13.8%, identified gene-based signals at BCL11B, NDFIP2, and RBM26, and a lead SNP within MCHR2-AS1 that again failed replication; the authors conclude TS GWAS remains underpowered for high-confidence replicable loci [4]. The Nature 2025 cross-disorder analysis is therefore important context: it places Tourette on the neurodevelopmental factor (shared with ASD and ADHD) and a secondary compulsive factor (shared with OCD and anorexia), and confirms that signal shared across all 14 disorders is enriched for broad transcriptional regulation [5].

Against this still-thin common-variant backdrop, the rare-variant and pharmacological evidence is what anchors the molecular biotypes. The landmark rare gene is HDC (histidine decarboxylase), the rate-limiting enzyme for histamine synthesis: a nonsense mutation (W317X) segregated in a two-generation pedigree with high penetrance, and Hdc-knockout mice show tic-like stereotypies and dopaminergic dysregulation that are rescued or worsened in predictable ways, giving TS a rare causal histaminergic anchor with strong functional support [6,7]. SLITRK1 (neurite-outgrowth modulator) and CELSR3 (planar-cell-polarity / axon guidance) are additional rare-variant candidates, and rare CNVs at NRXN1 and CNTN6 recur across cohorts [8,9].

The single most reproducible neuropathology is striatal interneuron loss. Postmortem stereology (Kataoka et al. 2010) found a 50-60% reduction in both parvalbumin-positive (GABAergic fast-spiking) and choline-acetyltransferase-positive (cholinergic) interneurons in the caudate and putamen of individuals with severe TS; transcriptomic work (Lennington et al. 2016) and a 2025 basal-ganglia transcriptome study extended this, adding evidence of microglial activation alongside the interneuron deficit [10,11,12]. Mouse ablation of striatal cholinergic and PV interneurons reproduces tic-like repetitive movements, closing the causal loop [13].

| Biotype / dysregulation | GO term(s) + ID | Specific finding | Neurotransmitter family | BDNF / neurotrophin + plasticity | E/I imbalance (+ region) | Oxidative / mito / ROS | Immune / inflammatory | Confidence | Source |
|---|---|---|---|---|---|---|---|---|---|
| Dopaminergic hyperfunction (CENTRAL) | dopamine receptor signaling pathway (GO:0007212); dopamine metabolic process (GO:0042417); dopamine transport (GO:0015872) | Hyperdopaminergic models: phasic dopamine release excess, elevated striatal DAT and D2 in some PET/SPECT samples; D2-blocking antipsychotics (haloperidol, aripiprazole) and presynaptic dopamine-depleting VMAT2 inhibitors reduce tics; the strongest pharmacological anchor in TS | **Dopamine** | not primary | dopamine biases striatal output toward disinhibition (indirect E/I) | not primary | none reported | HIGH (pharmacology), MEDIUM (PET specifics) | Buse 2013 [14]; Mink 2001 [15] |
| Striatal GABAergic interneuron deficit (CENTRAL) | GABAergic synaptic transmission (GO:0051932); regulation of GABAergic synaptic transmission; neuron migration (GO:0001764) | 50-60% loss of parvalbumin-positive fast-spiking interneurons in caudate/putamen postmortem; reduced striatal and motor-cortical inhibition; SMA GABA+ (MRS) inversely tracks premonitory-urge severity | **GABA** | possible (interneuron developmental/migration genes) | **I-down in striatum**; reduced fast-spiking inhibition releases striatal projection neurons; **I-down in SMA** (low GABA+) | not primary | microglial activation co-localizes with interneuron loss | HIGH (postmortem), MEDIUM (MRS) | Kataoka 2010 [10]; Lennington 2016 [11]; Draper 2014 [16] |
| Striatal cholinergic interneuron deficit | acetylcholine biosynthetic process (GO:0008292); cholinergic synaptic transmission (GO:0007271) | Reduced ChAT+ cholinergic (tonically active) interneurons in associative/sensorimotor striatum postmortem; experimental ablation reproduces tics in mice (note: one VAChT PET study found normal transporter expression) | Acetylcholine | not primary | loss of cholinergic tone destabilizes striatal microcircuit dynamics | not primary | co-occurs with microglial activation | MEDIUM-HIGH (postmortem + mouse), conflicting PET | Kataoka 2010 [10]; Xu 2015 [13]; Lee 2017 [17] |
| Histaminergic deficiency (rare, high-penetrance) | histamine biosynthetic process (GO:0001694); histamine secretion (GO:0001821) | HDC W317X nonsense mutation segregates with TS at high penetrance; Hdc-knockout mice show tic-like stereotypies and dysregulated nigrostriatal dopamine; histamine normally restrains striatal dopamine | **Histamine** (modulates dopamine) | not primary | histamine deficit disinhibits striatal dopamine signaling | not primary | none reported | HIGH (single-gene causal), rare | Ercan-Sencicek 2010 [6]; Castellan Baldan 2014 [7] |
| Glutamatergic / corticostriatal synaptic | glutamate receptor signaling pathway (GO:0007215); glutamatergic synaptic transmission (GO:0035249) | Corticostriatal glutamatergic drive to the loop; MRS shows altered striatal/frontal Glx in some samples; synaptic and cell-adhesion genes (NRXN1, SLITRK1, CELSR3) implicate excitatory synapse formation | **Glutamate** | possible (synaptic-adhesion genes) | excitatory corticostriatal input to a disinhibited striatum; direction unsettled | not primary | none reported | MEDIUM | Kanaan 2017 [18]; Huang 2017 [9] |
| Serotonergic modulation | serotonin receptor signaling pathway (GO:0007210); serotonin transport (GO:0006837) | Serotonergic contribution mainly via comorbid OCD; SSRIs target OCD symptoms not tics; modest direct tic relevance | **Serotonin** | not primary | not the primary E/I story | not primary | none reported | LOW-MEDIUM (mostly OCD-mediated) | Buse 2013 [14] |
| Neurodevelopmental / cell-adhesion program | nervous system development (GO:0007399); neuron migration (GO:0001764); cell adhesion (GO:0007155) | SLITRK1, CELSR3, NRXN1, CNTN6, BCL11B implicate axon guidance, interneuron migration, and synapse formation; consistent with a developmental striatal-interneuron-deficit model | none reported (developmental axis) | YES (developmental plasticity); BDNF not a primary TS gene but interneuron maturation is plasticity-relevant | links to striatal interneuron migration deficit | not primary | none reported | MEDIUM | Yu 2019 [3]; Tsetsos 2024 [4]; Abelson 2005 [8] |
| Immune / autoimmune (PANDAS/PANS subtype, CONTESTED) | inflammatory response (GO:0006954); complement activation (GO:0006956); microglial cell activation (GO:0001774) | Postmortem microglial activation in basal ganglia (replicable); the PANDAS/PANS streptococcal-antibody-mediated subtype is clinically defined but mechanistically disputed; anti-neuronal antibody and immunotherapy evidence is inconsistent | none reported | not primary | not primary | YES (microglia HIGH postmortem; streptococcal-autoimmune subtype CONTESTED) | MEDIUM (microglia), LOW-CONTESTED (PANDAS) | Lennington 2016 [11]; Frick 2016 [19]; Sigra 2018 [20] |

GO IDs above are drawn from standard GO term names; histamine secretion and histamine biosynthesis terms should be verified against a current GO release (marked approx where uncertain). The neurotransmitter mapping is deliberate and individual: **dopamine** is CENTRAL (the antipsychotic/VMAT2 pharmacology anchor), **GABA** is CENTRAL (the striatal interneuron-loss and SMA-MRS anchor), **acetylcholine** is the third interneuron family, **histamine** is the landmark rare-gene family, **glutamate** is the corticostriatal driver, and **serotonin** is largely OCD-mediated. The immune row separates the replicable postmortem microglial signal (MEDIUM) from the contested PANDAS/PANS autoimmune construct (LOW, flagged).

## MESO scale (connectomic) vs Allen Atlas nodes + edges

The dominant circuit model is the sensorimotor cortico-striato-thalamo-cortical (CSTC) loop, the same architecture invoked for OCD but anchored in the motor rather than the orbitofronto-limbic territory of the striatum [21,22]. In the standard basal-ganglia framework (Mink), tics arise when striatal disinhibition (from the interneuron deficit) allows abnormally focused activity to propagate through the direct pathway, releasing unwanted motor programs that the cortex cannot suppress [15]. Two functional themes recur: (1) sensorimotor CSTC hyperactivity with reduced striatal and motor-cortical inhibition, and (2) an insula/SMA substrate for the premonitory urge (the uncomfortable sensory precursor that tics relieve). Structurally, the most consistent findings are reduced caudate volume across the lifespan and sensorimotor cortical thinning proportional to tic severity, with compensatory prefrontal/callosal changes in children who control tics better [23,24].

Functional labels are mapped to their containing Allen anatomical structures. The CM-Pf (centromedian-parafascicular) thalamic complex, the principal DBS target, sits within the Allen "thalamus" structure and is noted as a functional subregion.

### NODES

| Allen region (functional label) | Observed change | Modality | Confidence | Source |
|---|---|---|---|---|
| Caudate nucleus (dorsal/associative striatum) | reduced volume across the lifespan; the most consistent structural finding | structural | HIGH | Peterson 2003 [23]; Bloch 2005 [25] |
| Putamen (sensorimotor striatum) | volume changes (reduced in adults; pleiotropy with TS risk in ENIGMA-TS); locus of interneuron loss | structural | MEDIUM-HIGH | Worbe 2015 [21]; ENIGMA-TS 2022 [26] |
| Globus pallidus (internal/external segments) | altered volume and connectivity; GPi is an established DBS target | structural; fMRI | MEDIUM-HIGH | Worbe 2015 [21] |
| Thalamus (centromedian-parafascicular complex, CM-Pf) | altered volume/activity; principal DBS target; relays striatal output back to motor cortex | structural; DBS | HIGH (as DBS target) | Müller-Vahl 2021 [27] |
| Precentral gyrus / paracentral lobule (primary motor cortex, M1) | reduced short-interval intracortical inhibition (SICI, TMS); thinning tracks tic severity | TMS; structural | HIGH (SICI), MEDIUM-HIGH (structural) | Orth 2008 [28]; Batschelett 2023 [29] |
| Frontal lobe, superior frontal gyrus, medial part (supplementary motor area, SMA / pre-SMA) | reduced GABA+ (MRS) inversely correlated with premonitory-urge severity; hyperactivity preceding tics; rTMS/tDCS target | MRS; fMRI; EEG | HIGH (urge-GABA link) | Draper 2014 [16]; Mahjoub 2025 [30] |
| Insula, anterior part (anterior insula, interoception) | reduced grey-matter thickness; activity scales with premonitory-urge intensity | fMRI; structural | MEDIUM-HIGH | Jackson 2020 [31]; Draper 2016 [32] |
| Cingulate gyrus, anterior part (ACC) | altered activity; substrate of urge/compulsivity overlap with OCD | fMRI | MEDIUM | Worbe 2015 [21] |
| Frontal lobe, orbital part (OFC) | involved in compulsivity-overlap territory; relevant to comorbid OCD | fMRI; structural | MEDIUM (OCD-overlap) | Worbe 2015 [21] |
| Prefrontal cortex / corpus callosum (compensatory) | hypertrophy / larger callosum in children with better tic control (activity-dependent plasticity) | structural | MEDIUM | Plessen 2004 [33]; Peterson 2001 [34] |

### EDGES

| Region A vs Region B (functional labels) | Association sign | Observed change in Tourette | Modality | Confidence | Source |
|---|---|---|---|---|---|
| Sensorimotor cortex (M1/SMA) vs putamen/caudate (sensorimotor striatum): **motor CSTC loop** | positive (cortex drives striatum) | hyperactive sensorimotor CSTC loop; abnormal corticostriatal drive into a disinhibited striatum is the core circuit lesion | fMRI; DTI | HIGH | Worbe 2015 [21]; Mink 2001 [15] |
| Striatum (caudate/putamen) vs globus pallidus / thalamus (CM-Pf): striato-pallido-thalamic output | positive/inhibitory (normal direct/indirect balance) | reduced striatal interneuron inhibition shifts the balance toward disinhibited thalamocortical output; releases tics | fMRI; structural; DBS | HIGH | Mink 2001 [15]; Müller-Vahl 2021 [27] |
| Thalamus (CM-Pf) vs sensorimotor/premotor cortex: thalamocortical return | positive | excess thalamocortical drive to motor/premotor cortex; CM-Pf DBS normalizes this loop | DBS; fMRI | HIGH (DBS evidence) | Müller-Vahl 2021 [27] |
| SMA / pre-SMA vs striatum (sensorimotor): **urge-generation and tic-release loop** | positive | SMA hyperactivity precedes tics; low SMA GABA tracks premonitory urge; SMA neuromodulation reduces tics/urge | fMRI; MRS; rTMS/tDCS | MEDIUM-HIGH | Draper 2014 [16]; Mahjoub 2025 [30] |
| Anterior insula vs SMA / sensorimotor cortex: interoceptive-urge network | positive | insula activity scales with premonitory-urge intensity; couples interoception to motor preparation | fMRI | MEDIUM | Jackson 2020 [31] |
| Motor cortex vs sensory cortex: surround/sensorimotor inhibition | inhibitory (normal) | reduced motor-system suppression of sensory input; reduced SICI (TMS) indexes deficient GABA-A intracortical inhibition | TMS; fMRI | HIGH (SICI) | Orth 2008 [28]; Batschelett 2023 [29] |
| OFC/ACC vs ventral/associative striatum: limbic-associative CSTC loop (OCD-overlap) | positive | the OCD-shared compulsive loop; engaged in TS+OCD; differentiates motor-tic from compulsive phenotypes | fMRI | MEDIUM | Worbe 2015 [21] |

### EEG / MEG / TMS markers

- **Reduced short-interval intracortical inhibition (SICI).** TMS-measured SICI, predominantly GABA-A-mediated, is reduced in TS and the reduction scales with tic severity; this is the most defensible neurophysiological marker and it converges directly with the striatal/cortical GABAergic-deficit biotype [28,29]. Confidence: HIGH.
- **Altered sensorimotor mu rhythm.** Mu (8-13 Hz) desynchronization over sensorimotor cortex is altered around tic generation and voluntary tic suppression; mu/beta event-related dynamics index motor-cortical engagement before tics [35]. Confidence: MEDIUM.
- **Premonitory-urge electrophysiology.** Pre-tic potentials (Bereitschaftspotential-like readiness activity is often absent before tics, distinguishing tics from voluntary movement) and SMA-localized signals correlate with urge build-up [36]. Confidence: MEDIUM.
- **Reduced surround inhibition.** Functional and TMS evidence indicates the motor system fails to adequately suppress neighbouring/sensory activity, consistent with the SICI and mu findings [37]. Confidence: MEDIUM-HIGH.

The neurophysiology story is unusually coherent for a psychiatric/neurological disorder: SICI reduction (cortical GABA-A deficit), low SMA GABA+ on MRS, and postmortem striatal GABAergic interneuron loss all point to the same disinhibition mechanism across three independent modalities.

## MACRO scale (phenotype) vs SNOMED CT / HPO

TS presents as combined motor and phonic tics with a characteristic waxing-waning course, often preceded by premonitory urges and accompanied by heavy comorbidity: roughly 50% of clinic samples have OCD/obsessive-compulsive features and roughly 50% have ADHD. Coprolalia (involuntary obscene utterances), the symptom that dominates public perception, is actually uncommon (under ~10-20% of cases).

| Biotype phenotype | SNOMED CT term + ID | HPO term + ID | Short description of observations that led to this mapping | Source |
|---|---|---|---|---|
| Tourette syndrome (combined motor + phonic tics) | Gilles de la Tourette's syndrome (5158005) | Tics (HP:0100033) | Multiple motor tics plus ≥1 phonic tic >1 year, childhood onset; the defining diagnosis | DSM-5; Robertson 2017 [1] |
| Motor tics | Motor tic (45718004, approx, needs curation) | Motor tics / Abnormal involuntary movements (HP:0000734, approx, needs curation) | Sudden, recurrent, nonrhythmic motor movements (blinking, head jerks, complex sequences); maps to sensorimotor CSTC loop and M1/SMA | DSM-5; Mink 2001 [15] |
| Vocal / phonic tics | Vocal tic (approx, needs curation) | Vocalizations / phonic tics (approx, needs curation) | Sniffing, throat-clearing, grunting, word fragments; same circuit, laryngeal/respiratory effectors | DSM-5 |
| Premonitory urge | (no precise SNOMED concept; approx, needs curation) | (no precise HPO term; approx, needs curation) | Uncomfortable sensory antecedent relieved by performing the tic; maps to anterior insula and SMA (low GABA) | Draper 2014 [16]; Jackson 2020 [31] |
| Coprolalia (rare) | Coprolalia (15777002, approx, needs curation) | (no precise HPO term; approx) | Involuntary utterance of obscene words; uncommon (<20%); historically overemphasized | DSM-5; Robertson 2017 [1] |
| Comorbid OCD / obsessive-compulsive features | Obsessive-compulsive disorder (191736004) | Obsessive-compulsive behavior (HP:0000722) | Compulsions/obsessions in ~50% of TS; maps to OFC/ACC-ventral-striatal CSTC loop; shared compulsive genomic factor | Hirschtritt 2015 [38] |
| Comorbid ADHD | Attention deficit hyperactivity disorder (406506008) | Attention deficit hyperactivity disorder (HP:0007018) | Inattention/hyperactivity in ~50% of TS; shared neurodevelopmental genomic factor; SICI reduction tracks ADHD scores | Hirschtritt 2015 [38]; Gilbert 2004 [39] |
| Chronic (persistent) motor or vocal tic disorder | Chronic motor tic disorder (44712009, approx, needs curation) | Tics (HP:0100033) | Motor or vocal (not both) >1 year; shares the same polygenic risk spectrum as full TS | DSM-5; Tsetsos 2024 [4] |

SNOMED concept IDs marked "approx, needs curation" require verification against a current SNOMED CT release; the root TS concept (5158005), OCD (191736004), and ADHD (406506008) concepts and the HPO Tics term (HP:0100033) are reliable. Premonitory urge lacks a clean ontology concept and is flagged accordingly. The comorbidity rows are essential: TS is rarely "pure," and its two dominant comorbidities map onto its two genomic-factor loadings.

## Interventional studies (incl. neuromodulation, DBS, neuroplastogens)

Treatment converges on the dopaminergic and behavioral targets. Behavioral therapy (CBIT) is first-line; dopamine antagonists and alpha-2 agonists are the established pharmacology; DBS of the CM-Pf thalamus or GPi is the validated option for refractory adult TS. We flag two honest negatives: the VMAT2-inhibitor pivotal trials (ARTISTS) failed, and PANDAS-directed immunotherapy lacks an evidence base.

| Biotype it targets | Intervention (class + specific) | Study (author year, design, n) | Outcome | Confidence | Source |
|---|---|---|---|---|---|
| Urge-tic loop / SMA-sensorimotor (behavioral) | CBIT (habit-reversal + functional intervention) | Piacentini 2010 (RCT, n=126, children) and Wilhelm 2012 (RCT, n=122, adults); 248 total | Significant tic reduction vs supportive therapy; durable; designated first-line by AAN | HIGH | Piacentini 2010 [40]; Wilhelm 2012 [41]; Pringsheim 2019 [42] |
| Dopaminergic hyperfunction (D2 blockade) | Antipsychotic: haloperidol, pimozide; aripiprazole (D2 partial agonist) | Multiple RCTs; aripiprazole FDA-approved for TS (2014); AAN guideline | Robust tic reduction; aripiprazole better tolerated than typical antipsychotics; metabolic/EPS risks | HIGH | Pringsheim 2019 [42]; Yang 2019 [43] |
| Noradrenergic / prefrontal (esp. TS+ADHD) | Alpha-2 agonist: guanfacine, clonidine | RCTs; meta-analysis; AAN guideline | Moderate tic reduction; first-choice pharmacology when ADHD co-occurs; favorable safety in children | HIGH (efficacy in TS+ADHD), MEDIUM (tics alone) | Pringsheim 2019 [42]; Weisman 2013 [44] |
| Presynaptic dopamine depletion (VMAT2) | VMAT2 inhibitor: tetrabenazine; deutetrabenazine; valbenazine | Open-label/real-world positive (Jankovic); **ARTISTS 1 & 2 phase 3 deutetrabenazine RCTs negative**; valbenazine pivotal program also failed primary endpoint | Real-world benefit reported but pivotal placebo-controlled trials did NOT show meaningful YGTSS reduction; **efficacy contested** | LOW-MEDIUM (negative pivotal trials) | Jankovic 2016 [45]; Coffey 2021 (ARTISTS) [46] |
| Focal/disabling individual tics | Botulinum toxin (intramuscular, focal) | Small RCT (Marras 2001) and case series | Reduces frequency/intensity of targeted focal motor tics and premonitory urge at injected site | MEDIUM | Marras 2001 [47] |
| Refractory CSTC loop (thalamic target) | DBS: centromedian-parafascicular (CM-Pf) thalamus | Müller-Vahl 2021 (randomized double-blind thalamic vs GPi); international registry; meta-analyses | ~40-50% mean YGTSS reduction; ~69% of patients >50% improvement across registry; validated for refractory adult TS | MEDIUM-HIGH | Müller-Vahl 2021 [27]; Martinez-Ramirez 2018 [48]; Johnson 2021 [49] |
| Refractory CSTC loop (pallidal target) | DBS: globus pallidus internus (GPi, anteromedial/posteroventral) | Same comparative and registry datasets | Comparable efficacy to thalamic target; target choice individualized | MEDIUM-HIGH | Müller-Vahl 2021 [27]; Johnson 2021 [49] |
| Motor-cortical / SMA disinhibition | rTMS: low-frequency (1 Hz) inhibitory SMA | Youth RCT (active 1 Hz vs sham); systematic reviews | Active rTMS reduced tic frequency in some task conditions; overall evidence mixed/insufficient for routine use | LOW-MEDIUM | Kahl 2021 [50]; Hsu 2018 [51] |
| Premonitory urge / SMA | tDCS: cathodal SMA | Mahjoub 2025 (RCT, SMA tDCS) | Larger decrease in premonitory-urge intensity at 1 week vs sham; small, needs replication | LOW-MEDIUM | Mahjoub 2025 [30] |
| Streptococcal-autoimmune (PANDAS/PANS, CONTESTED) | Immunotherapy: IVIG, plasma exchange, antibiotics | Small/conflicting trials; Delphi consensus | Not routinely recommended; evidence inconsistent; the construct itself is disputed | LOW-CONTESTED | Sigra 2018 [20]; Frick 2016 [19] |
| Reward/plasticity | Neuroplastogens (ketamine, psilocybin) | No controlled TS trials | Not an evidence-based TS treatment; anecdotal cannabinoid reports exist but are separate | LOW (no evidence) | vs |

The interventional evidence reinforces the molecular picture from two directions. The robust responders, D2 antagonists/partial agonists, confirm the central dopaminergic biotype; CBIT confirms the urge-tic/SMA loop is behaviorally modifiable; and DBS of the CM-Pf thalamus or GPi confirms the CSTC loop as the actionable circuit. The most informative negative is the ARTISTS program: VMAT2 inhibitors, which deplete presynaptic dopamine and were mechanistically expected to work, failed their pivotal pediatric endpoints, a useful caution against over-reading the hyperdopaminergic model as the whole story.

## Most defensible biotypes (cross-scale synthesis)

1. **Striatal disinhibition biotype (the core TS biotype).** MICRO: 50-60% loss of parvalbumin GABAergic and cholinergic interneurons in caudate/putamen, with microglial activation. MESO anchor Allen nodes: caudate, putamen, globus pallidus, thalamus (CM-Pf). Anchor edge: striatum vs globus pallidus/thalamus output, where reduced interneuron inhibition shifts the balance toward disinhibited thalamocortical drive. MACRO: motor and phonic tics. Confidence: HIGH (postmortem + DBS).

2. **Hyperdopaminergic biotype.** MICRO: phasic dopamine excess, D2 sensitivity; the pharmacology anchor (haloperidol, aripiprazole reduce tics). MESO: sensorimotor striatum within the motor CSTC loop. MACRO: tic frequency/severity. Confidence: HIGH on pharmacology, MEDIUM on PET specifics; tempered by the negative VMAT2 trials.

3. **Sensorimotor CSTC hyperactivity / cortical disinhibition biotype.** MESO anchor Allen nodes: primary motor cortex (M1), SMA/pre-SMA, sensorimotor putamen. Anchor edge: sensorimotor cortex vs putamen, positive corticostriatal drive that is hyperactive; plus reduced motor-system surround inhibition. Neurophysiology: reduced SICI (TMS, GABA-A) tracking tic severity. MACRO: tics; rTMS/tDCS-modifiable. Confidence: HIGH (SICI), MEDIUM-HIGH (loop).

4. **Premonitory-urge / interoceptive biotype.** MESO anchor Allen nodes: anterior insula, SMA. Anchor edge: insula vs SMA/sensorimotor cortex, positive interoceptive-to-motor coupling; low SMA GABA+ (MRS) tracks urge severity. MACRO: premonitory urge, the CBIT-responsive target. Confidence: MEDIUM-HIGH.

5. **Compulsive-overlap biotype (TS+OCD).** MESO anchor Allen nodes: OFC, ACC, ventral/associative striatum. Anchor edge: OFC/ACC vs associative striatum (the OCD-shared limbic CSTC loop). MICRO: secondary compulsive genomic-factor loading. MACRO: comorbid OCD/obsessive-compulsive features (~50%). Confidence: MEDIUM.

6. **Rare-variant histaminergic biotype (small subset).** MICRO: HDC loss-of-function (W317X) and the histamine-restrains-dopamine axis; SLITRK1/CELSR3/NRXN1 developmental variants. A mechanistically clean but numerically small biotype. Confidence: HIGH within carriers, rare overall.

Genomic factor: Tourette loads primarily on the **neurodevelopmental factor** (with ASD and ADHD) and secondarily on the **compulsive/eating factor** (with OCD and anorexia) in the Nature 2025 cross-disorder analysis, consistent with its dual clinical identity as a childhood-onset motor disorder with dominant attentional and obsessive-compulsive comorbidity.

## References

[1] Robertson MM, Eapen V, Singer HS, et al. Gilles de la Tourette syndrome. Nat Rev Dis Primers. 2017;3:16097. doi:10.1038/nrdp.2016.97

[2] Mataix-Cols D, Isomura K, Pérez-Vigil A, et al. Familial risks of Tourette syndrome and chronic tic disorders: a population-based cohort study. JAMA Psychiatry. 2015;72(8):787-793. doi:10.1001/jamapsychiatry.2015.0627

[3] Yu D, Sul JH, Tsetsos F, et al. Interrogating the genetic determinants of Tourette syndrome and other tic disorders through genome-wide association studies. Am J Psychiatry. 2019;176(3):217-227. doi:10.1176/appi.ajp.2018.18070857

[4] Tsetsos F, Topaloudi A, Jain P, et al. Genome-wide association study meta-analysis of 9,619 cases with tic disorders. Biol Psychiatry. 2024. doi:10.1016/j.biopsych.2024.10.001

[5] Grotzinger AD, Werme J, Peyrot WJ, et al. Mapping the genetic landscape across 14 psychiatric disorders. Nature. 2025. doi:10.1038/s41586-025-09820-3

[6] Ercan-Sencicek AG, Stillman AA, Ghosh AK, et al. L-histidine decarboxylase and Tourette's syndrome. N Engl J Med. 2010;362(20):1901-1908. doi:10.1056/NEJMoa0907006

[7] Castellan Baldan L, Williams KA, Gallezot JD, et al. Histidine decarboxylase deficiency causes Tourette syndrome: parallel findings in humans and mice. Neuron. 2014;81(1):77-90. doi:10.1016/j.neuron.2013.10.052

[8] Abelson JF, Kwan KY, O'Roak BJ, et al. Sequence variants in SLITRK1 are associated with Tourette's syndrome. Science. 2005;310(5746):317-320. doi:10.1126/science.1116502

[9] Huang AY, Yu D, Davis LK, et al. Rare copy number variants in NRXN1 and CNTN6 increase risk for Tourette syndrome. Neuron. 2017;94(6):1101-1111.e7. doi:10.1016/j.neuron.2017.06.010

[10] Kataoka Y, Kalanithi PSA, Grantz H, et al. Decreased number of parvalbumin and cholinergic interneurons in the striatum of individuals with Tourette syndrome. J Comp Neurol. 2010;518(3):277-291. doi:10.1002/cne.22206

[11] Lennington JB, Coppola G, Kataoka-Sasaki Y, et al. Transcriptome analysis of the human striatum in Tourette syndrome. Biol Psychiatry. 2016;79(5):372-382. doi:10.1016/j.biopsych.2014.07.018

[12] Vaccarino FM, et al. Interneuron loss and microglia activation by transcriptome analyses in the basal ganglia of Tourette disorder. Biol Psychiatry. 2025. doi:10.1016/j.biopsych.2025.01.018 (approx, needs curation)

[13] Xu M, Kobets A, Du JC, et al. Targeted ablation of cholinergic interneurons in the dorsolateral striatum produces behavioral manifestations of Tourette syndrome. Proc Natl Acad Sci USA. 2015;112(3):893-898. doi:10.1073/pnas.1419533112

[14] Buse J, Schoenefeld K, Münchau A, Roessner V. Neuromodulation in Tourette syndrome: dopamine and beyond. Neurosci Biobehav Rev. 2013;37(6):1069-1084. doi:10.1016/j.neubiorev.2012.10.004

[15] Mink JW. Basal ganglia dysfunction in Tourette's syndrome: a new hypothesis. Pediatr Neurol. 2001;25(3):190-198. doi:10.1016/S0887-8994(01)00262-4

[16] Draper A, Stephenson MC, Jackson GM, et al. Increased GABA contributes to enhanced control over motor excitability in Tourette syndrome. Curr Biol. 2014;24(19):2343-2347. doi:10.1016/j.cub.2014.08.038

[17] Lee CY, et al. Normal striatal vesicular acetylcholine transporter expression in Tourette syndrome. eNeuro. 2017;4(4):ENEURO.0178-17.2017. doi:10.1523/ENEURO.0178-17.2017

[18] Kanaan AS, Gerasch S, García-García I, et al. Pathological glutamatergic neurotransmission in Gilles de la Tourette syndrome. Brain. 2017;140(1):218-234. doi:10.1093/brain/aww285

[19] Frick L, Pittenger C. Microglial dysregulation in OCD, Tourette syndrome, and PANDAS. J Immunol Res. 2016;2016:8606057. doi:10.1155/2016/8606057

[20] Sigra S, Hesselmark E, Bejerot S. Treatment of PANDAS and PANS: a systematic review. Neurosci Biobehav Rev. 2018;86:51-65. doi:10.1016/j.neubiorev.2018.01.001

[21] Worbe Y, Marrakchi-Kacem L, Lecomte S, et al. Altered structural connectivity of cortico-striato-pallido-thalamic networks in Gilles de la Tourette syndrome. Brain. 2015;138(2):472-482. doi:10.1093/brain/awu311

[22] Greene DJ, Schlaggar BL, Black KJ. Neuroimaging in Tourette syndrome: research highlights from 2014-2015. Curr Dev Disord Rep. 2015;2(4):300-308. doi:10.1007/s40474-015-0061-7

[23] Peterson BS, Thomas P, Kane MJ, et al. Basal ganglia volumes in patients with Gilles de la Tourette syndrome. Arch Gen Psychiatry. 2003;60(4):415-424. doi:10.1001/archpsyc.60.4.415

[24] Sowell ER, Kan E, Yoshii J, et al. Thinning of sensorimotor cortices in children with Tourette syndrome. Nat Neurosci. 2008;11(6):637-639. doi:10.1038/nn.2121

[25] Bloch MH, Leckman JF, Zhu H, Peterson BS. Caudate volumes in childhood predict symptom severity in adults with Tourette syndrome. Neurology. 2005;65(8):1253-1258. doi:10.1212/01.wnl.0000180957.98702.69

[26] Müller-Vahl KR, Loft S, et al. (ENIGMA-TS Working Group). Enhancing neuroimaging genetics through meta-analysis for Tourette syndrome (ENIGMA-TS): a worldwide platform for collaboration. Front Psychiatry. 2022;13:958688. doi:10.3389/fpsyt.2022.958688

[27] Müller-Vahl KR, Szejko N, Saryyeva A, et al. Randomized double-blind sham-controlled trial of thalamic versus GPi stimulation in patients with severe medically refractory Gilles de la Tourette syndrome. Brain Stimul. 2021;14(2):320-329. doi:10.1016/j.brs.2021.01.003

[28] Orth M, Münchau A, Rothwell JC. Corticospinal system excitability at rest is associated with tic severity in Tourette syndrome. Biol Psychiatry. 2008;64(3):248-251. doi:10.1016/j.biopsych.2007.12.009

[29] Batschelett MA, Gilbert DL, Wu SW, et al. Biomarkers of tic severity in children with Tourette syndrome: motor cortex inhibition measured with transcranial magnetic stimulation. Dev Med Child Neurol. 2023;65(11):1483-1491. doi:10.1111/dmcn.15578

[30] Mahjoub Y, et al. Randomized controlled trial of transcranial direct current stimulation over the supplementary motor area in Tourette syndrome. Mov Disord Clin Pract. 2025. doi:10.1002/mdc3.14285

[31] Jackson SR, Loayza J, Crighton M, et al. The role of the insula in the generation of motor tics and the experience of the premonitory urge-to-tic in Tourette syndrome. Cortex. 2020;126:119-133. doi:10.1016/j.cortex.2019.12.021

[32] Draper A, Jackson GM, Morgan PS, Jackson SR. Premonitory urges are associated with decreased grey matter thickness within the insula and sensorimotor cortex in young people with Tourette syndrome. J Neuropsychol. 2016;10(1):143-153. doi:10.1111/jnp.12089

[33] Plessen KJ, Wentzel-Larsen T, Hugdahl K, et al. Altered interhemispheric connectivity in individuals with Tourette's disorder. Am J Psychiatry. 2004;161(11):2028-2037. doi:10.1176/appi.ajp.161.11.2028

[34] Peterson BS, Staib L, Scahill L, et al. Regional brain and ventricular volumes in Tourette syndrome. Arch Gen Psychiatry. 2001;58(5):427-440. doi:10.1001/archpsyc.58.5.427

[35] Niccolai V, Korczok S, Finis J, et al. A peek into premonitory urges in Tourette syndrome: temporal and spectral EEG dynamics. Clin Neurophysiol. 2019;130(11):2150-2159. doi:10.1016/j.clinph.2019.08.024

[36] Hallett M. Tourette syndrome: update. Brain Dev. 2015;37(7):651-655. doi:10.1016/j.braindev.2014.11.005

[37] Buse J, et al. The suppressive effect of the motor system on the sensory system in patients with Tourette syndrome. Front Neurol. 2020;11:855. doi:10.3389/fneur.2020.00855

[38] Hirschtritt ME, Lee PC, Pauls DL, et al. Lifetime prevalence, age of risk, and genetic relationships of comorbid psychiatric disorders in Tourette syndrome. JAMA Psychiatry. 2015;72(4):325-333. doi:10.1001/jamapsychiatry.2014.2650

[39] Gilbert DL, Bansal AS, Sethuraman G, et al. Association of cortical disinhibition with tic, ADHD, and OCD severity in Tourette syndrome. Mov Disord. 2004;19(4):416-425. doi:10.1002/mds.20044

[40] Piacentini J, Woods DW, Scahill L, et al. Behavior therapy for children with Tourette disorder: a randomized controlled trial. JAMA. 2010;303(19):1929-1937. doi:10.1001/jama.2010.607

[41] Wilhelm S, Peterson AL, Piacentini J, et al. Randomized trial of behavior therapy for adults with Tourette syndrome. Arch Gen Psychiatry. 2012;69(8):795-803. doi:10.1001/archgenpsychiatry.2011.1528

[42] Pringsheim T, Okun MS, Müller-Vahl K, et al. Practice guideline recommendations summary: treatment of tics in people with Tourette syndrome and chronic tic disorders. Neurology. 2019;92(19):896-906. doi:10.1212/WNL.0000000000007466

[43] Yang C, Hao Z, Zhu C, et al. Comparative efficacy and safety of antipsychotic drugs for tic disorders: a systematic review and Bayesian network meta-analysis. Pharmacopsychiatry. 2019;52(1):7-15. doi:10.1055/s-0043-124872

[44] Weisman H, Qureshi IA, Leckman JF, et al. Systematic review: pharmacological treatment of tic disorders, efficacy of antipsychotic and alpha-2 adrenergic agonist agents. Neurosci Biobehav Rev. 2013;37(6):1162-1171. doi:10.1016/j.neubiorev.2012.09.008

[45] Jankovic J. Dopamine depleters in the treatment of hyperkinetic movement disorders. Expert Opin Pharmacother. 2016;17(18):2461-2470. doi:10.1080/14656566.2016.1258063

[46] Coffey B, Jankovic J, Claassen DO, et al. Efficacy and safety of fixed-dose deutetrabenazine in children and adolescents for tics associated with Tourette syndrome (ARTISTS 1 and ARTISTS 2). JAMA Netw Open. 2021/2023. doi:10.1001/jamanetworkopen.2023.50988 (approx, needs curation)

[47] Marras C, Andrews D, Sime E, Lang AE. Botulinum toxin for simple motor tics: a randomized, double-blind, controlled clinical trial. Neurology. 2001;56(5):605-610. doi:10.1212/wnl.56.5.605

[48] Martinez-Ramirez D, Jimenez-Shahed J, Leckman JF, et al. Efficacy and safety of deep brain stimulation in Tourette syndrome: the International Tourette Syndrome Deep Brain Stimulation Public Database and Registry. JAMA Neurol. 2018;75(3):353-359. doi:10.1001/jamaneurol.2017.4317

[49] Johnson KA, Duffley G, Anderson DN, et al. Structural connectivity predicts clinical outcomes of deep brain stimulation for Tourette syndrome. Brain. 2020;143(8):2607-2623. doi:10.1093/brain/awaa188

[50] Kahl CK, Kirton A, Pringsheim T, et al. Bilateral transcranial magnetic stimulation of the supplementary motor area in children with Tourette syndrome. Dev Med Child Neurol. 2021;63(7):808-815. doi:10.1111/dmcn.14828

[51] Hsu CW, Wang LJ, Lin PY. Efficacy of repetitive transcranial magnetic stimulation for Tourette syndrome: a systematic review and meta-analysis. Brain Stimul. 2018;11(5):1110-1118. doi:10.1016/j.brs.2018.06.002
