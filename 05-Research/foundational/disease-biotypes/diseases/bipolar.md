# Biotypes: Bipolar Disorder (BD-I and BD-II)

Genomic factor loading (Nature 2025): **SB factor** (shared with schizophrenia). In Grotzinger et al., "Mapping the genetic landscape across 14 psychiatric disorders," Nature 2025 (doi:10.1038/s41586-025-09820-3, 1,056,201 cases), bipolar disorder co-loads with schizophrenia on the SB factor, whose shared signal is enriched in genes expressed in excitatory neurons. This is consistent with the Mullins et al. 2021 finding that bipolar risk alleles concentrate in synaptic-signaling genes with high expression specificity in prefrontal and hippocampal neurons (doi:10.1038/s41588-021-00857-4). The signal shared across all 14 disorders was enriched for broad transcriptional regulation; the SB-factor-specific pathways are more synaptic and ion-channel-specific.

This document follows the shared template (`_TEMPLATE_AND_CONVENTIONS.md`). Confidence ratings: HIGH (multi-cohort replication), MEDIUM (single-consortium or moderate effect), LOW (single-lab or failed external replication). Replication problems are flagged explicitly.

## Seed papers

- Mullins N, Forstner AJ, O'Connell KS, et al. Genome-wide association study of more than 40,000 bipolar disorder cases provides new insights into the underlying biology. Nat Genet. 2021;53:817-829. doi:10.1038/s41588-021-00857-4. (41,917 cases; 64 loci; 33 novel; synaptic, calcium-channel, MHC signal.)
- Hou L, Heilbronner U, Degenhardt F, et al. Genetic variants associated with response to lithium treatment in bipolar disorder: a genome-wide association study. Lancet. 2016;387:1085-1093. doi:10.1016/S0140-6736(16)00143-4. (ConLiGen; n=2,563; single genome-wide-significant locus on chr21 spanning two lncRNAs; the lithium-responder biotype anchor.)
- Grotzinger AD, Werme J, Peyrot WJ, et al. Mapping the genetic landscape across 14 psychiatric disorders. Nature 2025. doi:10.1038/s41586-025-09820-3. (Organizing reference; SB factor.)
- Shkundin A, Halaris A. Associations of BDNF/BDNF-AS SNPs with Depression, Schizophrenia, and Bipolar Disorder. J Pers Med. 2023;13:1395. doi:10.3390/jpm13091395. (BD-specific BDNF SNP and haplotype findings; read in full from the project PDF library.)
- Berk M, Kapczinski F, Andreazza AC, et al. Pathways underlying neuroprogression in bipolar disorder: focus on inflammation, oxidative stress and neurotrophic factors. Neurosci Biobehav Rev. 2011;35:804-817. doi:10.1016/j.neubiorev.2010.10.001. (Oxidative-stress and neuroprogression model.)
- Favre P, Pauling M, Stout J, et al. (ENIGMA Bipolar DTI Working Group). Widespread white matter microstructural abnormalities in bipolar disorder. Neuropsychopharmacology. 2019;44:2285-2293. doi:10.1038/s41386-019-0485-6. (n=3,033; corpus callosum and fronto-limbic FA reductions.)

---

## MICRO scale (molecular / genetic / cellular / immune): GO-harmonized

The single most clinically defensible molecular stratifier in bipolar disorder is **lithium response**, not a risk locus. Roughly one in three patients respond optimally to lithium (Hou et al. 2016), and lithium responsivity is heritable and polygenic, which makes it the strongest candidate molecular biotype. Calcium-channel and ion-channel genetics (CACNA1C, ANK3) and a state-dependent BDNF signature are the next most defensible axes.

| Biotype / dysregulation | GO term(s) + ID | Specific finding (genes, variants, molecules) | Neurotransmitter family | BDNF / neurotrophin + plasticity? | E/I imbalance (+ region) | Oxidative / mito / ROS? | Immune / inflammatory? | Confidence | Source (author year, DOI) |
|---|---|---|---|---|---|---|---|---|---|
| Lithium-responder biotype (the key BD stratifier) | regulation of gene expression (GO:0010468); lncRNA-mediated regulation (approx, needs curation) | Single genome-wide locus of 4 linked SNPs on chr21 (rs79663003, rs78015114, rs74795342, rs75222709) spanning two long non-coding RNA genes (AL157359.1-region lncRNAs); markers also predicted relapse on lithium in an independent prospective sample | none reported (lithium acts on GSK3-beta, IMPase, not a single transmitter) | indirect: lithium raises BDNF over treatment | not directly | lithium normalizes mitochondrial complex I/III and reduces lipid peroxidation (downstream) | not primary | MEDIUM (single consortium, genome-wide-significant, independent replication of relapse prediction) | Hou 2016, doi:10.1016/S0140-6736(16)00143-4 |
| Polygenic lithium-response phenotype | broad transcriptional regulation (GO:0006355, approx) | Lower MDD polygenic score and lower SCZ polygenic load associate with BETTER lithium response in BD; combining SCZ + MDD PGS improves prediction; ConLiGen 2024 HRC re-imputation strengthened PGS analyses (n up to 2,586) | none reported | n/a | n/a | n/a | n/a | MEDIUM (consortium-level, modest variance explained) | International Consortium on Lithium Genetics, doi:10.1186/s40345-024-00341-y; Amare 2021, doi:10.1038/s41380-020-0689-5 |
| Calcium-channel / CACNA1C biotype | voltage-gated calcium channel activity (GO:0005245); calcium ion transmembrane transport (GO:0070588) | CACNA1C (rs11062170) encodes CaV1.2 L-type channel alpha-1C; top BD locus across multiple GWAS; calcium-channel-blocker target genes enriched in Mullins 2021 | Glutamate (activity-dependent Ca influx at glutamatergic synapses) | regulates activity-dependent plasticity | contributes to excitatory-neuron excitability (SB factor enriched in excitatory neurons) | not primary | not primary | HIGH (replicated across GWAS waves) | Mullins 2021, doi:10.1038/s41588-021-00857-4; Ferreira 2008, doi:10.1038/ng.209 |
| Sodium-channel anchoring / ANK3 biotype | structural constituent of axon initial segment / node of Ranvier (approx, needs curation); regulation of action potential (GO:0098900) | ANK3 (rs10994415) encodes Ankyrin-G, clusters voltage-gated Na channels at axon initial segment and nodes of Ranvier; epistasis with KCNQ2 reported | none direct (modulates neuronal excitability broadly) | n/a | alters excitatory-neuron firing | not primary | not primary | HIGH (replicated GWAS hit) | Ferreira 2008, doi:10.1038/ng.209; Mullins 2021, doi:10.1038/s41588-021-00857-4 |
| State-dependent BDNF / neurotrophin biotype | neurotrophin TRK receptor signaling (GO:0048011); regulation of synaptic plasticity (GO:0048167) | Peripheral BDNF falls during BOTH manic and depressive episodes and recovers in euthymia (52-study meta-analysis); m-BDNF/pro-BDNF ratio differentiates BD from MDD depression; BD-enriched haplotypes rs6265(C)-rs16917237(G) and rs6265(C)-rs16917237(G)-rs12273363(T); rs16917237 G allele more frequent in BD-I, BD-II, schizoaffective-bipolar | none direct | YES: low BDNF/TrkB during episodes implies reduced plasticity-competence; state marker | n/a | low BDNF biotype overlaps low-mitochondrial-reserve | not primary | MEDIUM-HIGH (BDNF state marker meta-analytic; haplotypes single-lab) | Fernandes 2015, doi:10.1186/s12916-015-0529-7; Shkundin & Halaris 2023, doi:10.3390/jpm13091395; Ivanova 2013 |
| Hyperdopaminergic mania biotype | dopamine receptor signaling pathway (GO:0007212); dopamine secretion (GO:0014046) | Mania associated with elevated dopaminergic tone; dopamine-agonist and stimulant exposure can precipitate mania; antimanic agents reduce dopaminergic transmission; depressive pole associated with reduced reward-related DA signaling | Dopamine | indirect (NAc BDNF interacts with DA) | tilts toward excitation in mesolimbic/ventral striatum | not primary | not primary | MEDIUM (pharmacological inference; direct PET in BD sparse) | review in Berk 2011, doi:10.1016/j.neubiorev.2010.10.001 |
| Glutamate / GABA (E/I) biotype | glutamatergic synaptic transmission (GO:0035249); GABAergic synaptic transmission (GO:0051932) | Elevated glutamate/glutamine on MRS in BD across mood states; GABAergic deficits reported; lamotrigine (glutamate-release modulator) efficacy in BD depression supports glutamatergic component | Glutamate; GABA | n/a | E-up reported in ACC and prefrontal regions (MRS) | n/a | not primary | MEDIUM (MRS heterogeneous across labs) | Gigante 2012 (MRS meta-analysis); see refs |
| Oxidative-stress / mitochondrial biotype | response to oxidative stress (GO:0006979); mitochondrial ATP synthesis coupled electron transport (GO:0042775) | Lipid peroxides, 8-OHdG, protein carbonyls elevated in active mania and depression; reduced antioxidant defense; mitochondrial dysfunction central to Berk/Kato neuroprogression model; NAC RCT (Berk 2008) benefits BD depression (d~0.7) | none direct | low-BDNF state co-occurs | n/a | YES: strong BD evidence; one of the better-supported BD molecular axes | crosstalk with inflammation | MEDIUM-HIGH (replicated markers; NAC effect modest at group level) | Berk 2011, doi:10.1016/j.neubiorev.2010.10.001; Kato 2007; Andreazza 2008 |
| Immune / inflammatory biotype | inflammatory response (GO:0006954); cytokine-mediated signaling (GO:0019221) | IL-6, TNF-alpha, CRP elevated especially in mania and partly in depression; IL-6 tied to cognitive outcomes; MHC locus reached genome-wide significance in BD for the first time in Mullins 2021 | none direct | n/a | n/a | crosstalk (cytokines lower BDNF, raise ROS) | YES: state-dependent (mania > euthymia); MHC GWAS signal | MEDIUM (peripheral cytokine meta-analyses replicated; mechanism partial) | Mullins 2021, doi:10.1038/s41588-021-00857-4; Modabbernia 2013 |
| Circadian / CLOCK biotype | circadian rhythm (GO:0007623); circadian regulation of gene expression (GO:0032922) | Core clock genes (CLOCK, ARNTL/BMAL1, PER1-3, CRY1/2) dysregulated; PER3 and ARNTL association signals; advanced rhythm/short sleep in mania, delayed rhythm in depression; evening chronotype enriched; CLOCK variants linked to recurrence and mania severity | none direct (couples to monoamine and metabolic rhythms) | n/a | n/a | clock genes regulate mitochondrial metabolic rhythm | n/a | MEDIUM (consistent association; causal direction unresolved) | Bipolar Disorder, Circadian Rhythm and Clock Genes review 2024, PMC11024693; Benedetti 2003 |

Notes on the MICRO scale:
- The lithium-responder biotype is the standout. Hou et al. 2016 is the only genome-wide-significant single-locus finding for a treatment-response trait in BD, and the chr21 lncRNA region also predicted relapse prospectively. Replication of the exact SNPs has been partial in later samples, so confidence is MEDIUM rather than HIGH, but the polygenic version of the same biotype (lower MDD/SCZ polygenic load predicts better response) is internally consistent and replicated at the consortium level.
- CACNA1C and ANK3 are the most defensible risk loci and both point to ion-channel / excitatory-neuron biology, matching the SB-factor enrichment (Grotzinger 2025).
- The BDNF signature in BD is STATE-DEPENDENT: it drops in episodes and recovers in euthymia. This differs from the more trait-like low-BDNF picture in chronic schizophrenia and is a candidate state biomarker rather than a diagnostic one.

---

## MESO scale (connectomic): Allen Atlas nodes + edges

Findings are mapped to the Allen Human Reference Atlas 3D (2020, 141 regions). Functional labels (vmPFC, sgACC, DLPFC) are given in parentheses against the containing Allen anatomical structure. The dominant BD circuit story is fronto-limbic dysregulation: amygdala hyperactivity with deficient ventral-prefrontal top-down control, plus white-matter (oligodendrocyte) disruption. State matters: many findings flip sign between mania and depression.

### NODES

| Allen region (functional label) | Observed change (hyper / hypo / atrophy / thinning / hyperconnectivity) | Modality (fMRI / EEG / MEG / structural) | Confidence | Source |
|---|---|---|---|---|
| Amygdala | hyper (heightened reactivity to emotional faces, both states; subregion-specific) | fMRI (task + rs-fMRI) | HIGH | Phillips & Swartz 2014, doi:10.1176/appi.ajp.2014.13081008; amygdala-subregion rs-fMRI 2024 (S2405844024141461) |
| Frontal lobe, orbital gyri (ventromedial PFC / vmPFC) | hypo (reduced top-down regulatory activation; reduced effective connectivity to amygdala for positive affect) | fMRI | HIGH | Phillips & Swartz 2014; effective-connectivity studies |
| Cingulate gyrus, subgenual/pregenual part (ACC / sgACC, pgACC) | mixed (altered activation; volume reductions reported) | fMRI / structural | MEDIUM | review Strakowski 2012, doi:10.1038/mp.2011.169 |
| Frontal lobe, middle frontal gyrus (dorsolateral PFC / DLPFC) | hypo (reduced engagement during cognitive/executive tasks; cortical thinning) | fMRI / structural | MEDIUM | ENIGMA-BD cortical (Hibar 2018, doi:10.1038/mp.2017.73) |
| Striatum, ventral part / nucleus accumbens (ventral striatum) | hyper in mania (reward hypersensitivity); blunted in depression | fMRI | MEDIUM | Nusslock 2012; reward-network endophenotype (S0165032720330020) |
| Corpus callosum (white matter) | atrophy / reduced FA (largest effect among tracts) | structural / DTI | HIGH | ENIGMA-BD DTI, Favre 2019, doi:10.1038/s41386-019-0485-6 |
| Hippocampal formation | atrophy (volume reductions, partly medication-modulated; lithium associated with larger volume) | structural | MEDIUM-HIGH | ENIGMA-BD subcortical, Hibar 2016, doi:10.1038/mp.2015.227 |
| Insula | hypo / altered (interoceptive and salience processing) | fMRI | MEDIUM | review Strakowski 2012 |
| Cerebral white matter, oligodendrocyte compartment | reduced FA across 29 regions; fewer oligodendroglia and altered myelin-gene expression | DTI / postmortem | HIGH (DTI), MEDIUM (postmortem) | Favre 2019, doi:10.1038/s41386-019-0485-6 |

### EDGES

| Region A to Region B (functional labels) | Association sign | Observed change in disorder | Modality | Confidence | Source |
|---|---|---|---|---|---|
| Amygdala to orbital frontal gyri (vmPFC) | normally negative (anticorrelation): vmPFC regulates amygdala | reduced (anticorrelation) effective connectivity; weakened top-down control of emotion, prominent for positive/happy affect | fMRI (DCM, rs-fMRI) | HIGH | Phillips & Swartz 2014; effective-connectivity 2024 |
| Amygdala to cingulate gyrus, subgenual (sgACC) | negative (anticorrelation) | disrupted fronto-limbic regulation; state-dependent | fMRI | MEDIUM | Strakowski 2012, doi:10.1038/mp.2011.169 |
| Amygdala to wider amygdala-centered network | mixed | depressed state: baseline HYPOconnectivity; manic state: reduced baseline HYPERconnectivity; both shift with clinical improvement | rs-fMRI longitudinal | MEDIUM | longitudinal amygdala connectivity, PMC8280117 |
| DLPFC (middle frontal gyrus) to ventral striatum / NAc | positive (cognitive control over reward) | weakened control; reward hypersensitivity in mania | fMRI | MEDIUM | Nusslock 2012; reward-network endophenotype |
| Prefrontal to limbic via corpus callosum / cingulum | structural (myelinated coupling) | reduced FA degrades fronto-limbic communication efficiency | DTI | HIGH | Favre 2019, doi:10.1038/s41386-019-0485-6 |

EEG/MEG notes: BD shows reduced and less reactive alpha, abnormal gamma-band and 40-Hz responses overlapping schizophrenia (consistent with the shared SB factor), and circadian-linked sleep-EEG disturbance (reduced REM latency, fragmented architecture in episodes). Manic states associate with increased high-frequency/cortical-excitability indices; depressive states with frontal asymmetry resembling unipolar depression. Most EEG/MEG findings in BD are MEDIUM-to-LOW confidence because of small samples, medication effects, and weak external replication; the state-dependence makes cross-study pooling unreliable.

Atlas note: amygdala, vmPFC (orbital gyri), sgACC (subgenual cingulate), DLPFC (middle frontal gyrus), ventral striatum/NAc, corpus callosum, hippocampus, and insula all exist in the Allen 141-region set, so no non-Allen additions were required.

---

## MACRO scale (phenotype): SNOMED CT / HPO

| Biotype phenotype | SNOMED CT term + ID | HPO term + ID | Short description of observations that led to this mapping | Source |
|---|---|---|---|---|
| Bipolar I disorder (full manic episodes) | Bipolar I disorder 371596008 | Bipolar affective disorder HP:0007302 | At least one manic episode meeting full duration/severity criteria; maps to the elevated-mood / hyperdopaminergic / circadian-advance dimension | DSM-5/ICD-11; SNOMED browser |
| Manic episode (elevated mood, decreased need for sleep, grandiosity, risk-taking) | Manic bipolar I disorder 68569003 | Mania HP:0100754 | Elevated/expansive or irritable mood, reduced sleep need, grandiosity, pressured speech, distractibility, increased goal-directed activity, risk-taking; circadian-advance and hyperdopaminergic dimensions | SNOMED browser; HPO |
| Bipolar II disorder (hypomania + major depression) | Bipolar II disorder 83225003 (approx, needs curation) | Mania HP:0100754 (hypomania subthreshold; needs curation) | Hypomanic episodes (shorter, no marked functional impairment, no psychosis) alternating with full depressive episodes; lower-amplitude excitation dimension | SNOMED browser; HPO |
| Bipolar depressive episode | Bipolar affective disorder, current episode depression 191627008 | Depression / Depressivity HP:0000716 | Low mood, anhedonia, psychomotor change, often hypersomnia and reduced energy; maps to low-BDNF state, reward-circuit blunting, circadian delay | SNOMED browser; HPO |
| Mixed features | Mixed bipolar I disorder 191618007 (approx, needs curation) | (no single specific HPO term; combine HP:0100754 + HP:0000716) | Co-occurring manic and depressive symptoms in one episode; high suicide risk; maps to simultaneous excitatory and depressive dysregulation | SNOMED browser |
| Rapid cycling | Rapid cycling bipolar disorder (approx, needs curation) | (no specific HPO term; needs curation) | Four or more mood episodes per year; associated with circadian dysregulation and antidepressant exposure; harder lithium response | review literature |
| Psychotic features | Severe manic bipolar I disorder with psychotic features (approx, needs curation; cf. without-psychosis 162004) | Psychosis HP:0000709 | Delusions/hallucinations during mood episodes, often mood-congruent grandiose in mania; overlaps SB-factor psychosis dimension | SNOMED browser; HPO |

Mapping notes:
- Bipolar I disorder 371596008 and bipolar disorder (general) 13746004 are confirmed SNOMED concept IDs; manic bipolar I disorder 68569003 and the depression-episode concept 191627008 are confirmed. BD-II, mixed-features, rapid-cycling, and with-psychotic-features concept IDs are marked "approx, needs curation" because I did not independently verify each exact ID and should not invent them.
- HP:0007302 (Bipolar affective disorder) and HP:0100754 (Mania) are confirmed HPO terms. HPO is built for Mendelian-disease phenotyping, so several BD course specifiers (rapid cycling, mixed features) lack dedicated HPO terms and are left for curation rather than fabricated.

---

## Interventional studies (incl. neuromodulation, DBS, neuroplastogens)

The defensible interventional story in BD is treatment STRATIFICATION by mood state and by lithium-responder status. Lithium is uniquely disease-modifying for the responder biotype; antidepressants and serotonergic plastogens carry a real manic-switch risk that must gate their use.

| Biotype it targets | Intervention (class + specific) | Study (author year, design, n) | Outcome | Confidence | Source |
|---|---|---|---|---|---|
| Lithium-responder biotype (chr21 lncRNA / low MDD-SCZ polygenic load) | Mood stabilizer: lithium | Hou 2016, GWAS on prospectively phenotyped responders, n=2,563; Amare 2021 PGS analysis | ~1 in 3 respond optimally; genetic markers predict response and relapse; lithium reduces suicide and is the reference disease-modifying agent | MEDIUM-HIGH (efficacy HIGH; genetic stratifier MEDIUM) | Hou 2016, doi:10.1016/S0140-6736(16)00143-4; Amare 2021, doi:10.1038/s41380-020-0689-5 |
| Oxidative-stress / mitochondrial + lithium-responder | Lithium (antioxidant, GSK3-beta inhibition, mitochondrial complex I/III support, larger hippocampal volume) | Maurer 2009; ENIGMA-BD subcortical Hibar 2016 (lithium-volume association) | Lithium normalizes redox markers and associates with preserved hippocampal/gray-matter volume | MEDIUM | Berk 2011, doi:10.1016/j.neubiorev.2010.10.001; Hibar 2016, doi:10.1038/mp.2015.227 |
| Glutamate/E-I + rapid-cycling/mixed | Anticonvulsant mood stabilizer: valproate (sodium-channel + GABA + glutamate modulation) | Multiple RCTs; meta-analyses for acute mania | Effective for acute mania and mixed features; teratogenic, contraindicated in pregnancy | HIGH | Bowden 1994 and later meta-analyses |
| Bipolar-depression pole / glutamate | Anticonvulsant: lamotrigine (glutamate-release modulation) | Calabrese maintenance trials; meta-analysis | Prevents depressive relapse more than manic; first-line for BD depression maintenance; low manic-switch risk | HIGH | Calabrese 2003; Geddes 2009 meta-analysis |
| Hyperdopaminergic mania / psychotic features | Atypical antipsychotics: quetiapine, olanzapine, aripiprazole, cariprazine, lurasidone | Numerous RCTs; quetiapine and lurasidone positive in BD depression; aripiprazole/cariprazine in mania | Quetiapine and lurasidone reduce bipolar depression; D2-modulators control mania and psychosis | HIGH | RCT base; Yatham CANMAT/ISBD 2018 guideline |
| Treatment-resistant bipolar depression (low-BDNF state, glutamatergic) | NMDA modulator / plastogen: IV ketamine / esketamine | Scoping & systematic reviews (PMC10296406; academic.oup.com/ijnp 24:535); esketamine retrospective cohort n=2,126 | Rapid antidepressant and anti-suicidal effect; manic/hypomanic switch risk reported LOW-to-modest under mood-stabilizer cover, but no dedicated RCTs (BD usually excluded from pivotal esketamine trials) | MEDIUM-LOW (efficacy promising; RCT evidence sparse; switch caution) | systematic review doi:10.1093/ijnp/pyab031; cohort doi:10.1016/j.euroneuro.2025... |
| Bipolar depression (broad) | Neuromodulation: rTMS / deep TMS | Network meta-analysis 2025 (ketamine vs rTMS vs ECT); BD subgroups small | rTMS comparable to ketamine for response/remission in TRD/BD subgroups; evidence low-to-very-low quality; manic-switch reports rare | LOW-MEDIUM | 2025 network meta-analysis (neuromtl review) |
| Severe / treatment-resistant BD (mania, depression, mixed, catatonia) | Neuromodulation: ECT | Meta-analyses incl. IV-ketamine-vs-ECT RCTs; case series in TR bipolar depression | ECT is among the most effective acute treatments in BD across poles; some RCTs find ECT superior to ketamine | HIGH | Bahji 2024 meta-analysis, doi:10.1016/j.jad.2024...; case report PMC11205489 |
| Refractory BD (experimental) | DBS (sgACC; also targets used for TRD) | Small case series; mostly extrapolated from TRD DBS | Experimental only; no controlled BD evidence; bipolarity is often an exclusion in TRD DBS trials due to hypomania-induction risk | LOW | TRD DBS literature (extrapolated) |
| Adjunct, oxidative-stress biotype | N-acetylcysteine (glutathione precursor) | Berk 2008 multicenter RCT | Benefit for BD depressive symptoms (d~0.7); group-level effect modest, likely concentrated in oxidative-stress-positive subgroup | MEDIUM | Berk 2008, doi:10.1016/j.biopsych.2008.03.004 |
| ALL biotypes (safety gate) | Antidepressants AND serotonergic psychedelics (psilocybin, LSD) | Manic-switch literature; up to ~40% switch rates with unopposed antidepressants in some BD cohorts | CAUTION: antidepressant and psychedelic monotherapy can precipitate mania/hypomania, rapid cycling, or mixed states; classical psychedelics are generally contraindicated or used only under strict mood-stabilizer cover in BD-I | MEDIUM-HIGH (switch risk well-recognized clinically) | review base; ketamine-switch cohort doi:10.1016/j.euroneuro.2025... |

Intervention notes:
- Lithium is the through-line. It is the one agent with a genetically defined responder biotype, a suicide-reduction signal, and convergent antioxidant/mitochondrial and neuroprotective (volume-preserving) mechanisms. Stratifying patients into likely lithium responders before a months-long trial is the highest-value clinical use of a BD molecular biotype.
- The manic-switch caution is a structural feature of BD treatment and is the reason the project's psychedelic/TrkB plasticity strategy, which is attractive for unipolar depression, must be applied to BD only with extreme care and mood-stabilizer cover.

---

## Most defensible biotypes (cross-scale synthesis)

1. **Lithium-responder biotype** (the anchor). MICRO: chr21 lncRNA locus (Hou 2016) plus low MDD/SCZ polygenic load (Amare 2021); convergent antioxidant/mitochondrial mechanism. MESO: lithium associates with preserved hippocampal and gray-matter volume and normalized amygdala connectivity. MACRO: classic episodic BD-I with euthymic inter-episode recovery, often non-rapid-cycling, frequently with positive family history of lithium response. This is the single most actionable BD biotype. Confidence MEDIUM-HIGH.

2. **Calcium/ion-channel excitability biotype** (CACNA1C / ANK3). MICRO: CaV1.2 and Ankyrin-G variants, the most replicated BD risk loci, enriched in excitatory neurons consistent with the SB factor. MESO: fronto-limbic excitability and amygdala hyperreactivity. MACRO: mania-prone BD-I. Anchor Allen regions: amygdala, vmPFC (orbital gyri). Confidence HIGH for genetics, MEDIUM for circuit mapping.

3. **Fronto-limbic dysregulation biotype** (the core circuit phenotype). MESO: amygdala hyperactivity with deficient vmPFC top-down control (weakened amygdala-vmPFC anticorrelation), plus corpus-callosum and fronto-limbic white-matter FA reduction. MICRO: oligodendrocyte/myelin-gene and BDNF-plasticity involvement. MACRO: emotional dysregulation across manic and depressive poles. Anchor Allen regions: amygdala, orbital frontal gyri (vmPFC), subgenual cingulate (sgACC), corpus callosum. Confidence HIGH.

4. **Oxidative-stress / mitochondrial biotype** (Berk/Kato neuroprogression). MICRO: elevated lipid peroxides, 8-OHdG, mitochondrial dysfunction; NAC-responsive. MESO: links to gray-matter loss over repeated episodes. MACRO: neuroprogressive, multi-episode, cognitively-affected BD. Confidence MEDIUM-HIGH.

5. **Circadian / CLOCK biotype**. MICRO: CLOCK/PER3/ARNTL dysregulation. MESO/behavioral: advanced rhythm and reduced sleep need in mania, delayed rhythm in depression, evening chronotype. MACRO: rapid-cycling and sleep-driven episode triggering; targetable with chronotherapy and lithium. Confidence MEDIUM.

State-dependence is the cross-cutting caveat: BDNF, dopaminergic tone, inflammatory markers, and amygdala connectivity all FLIP between mania and depression, so any BD biotype must be read as a trajectory across states rather than a static signature.

**Genomic factor statement:** Bipolar disorder loads on the **SB factor** (shared with schizophrenia; excitatory-neuron-enriched) in Grotzinger et al. Nature 2025, consistent with its calcium/ion-channel, synaptic, and shared-psychosis genetics.

---

## References

1. Grotzinger AD, Werme J, Peyrot WJ, et al. Mapping the genetic landscape across 14 psychiatric disorders. Nature. 2025. doi:10.1038/s41586-025-09820-3.
2. Mullins N, Forstner AJ, O'Connell KS, et al. Genome-wide association study of more than 40,000 bipolar disorder cases provides new insights into the underlying biology. Nat Genet. 2021;53:817-829. doi:10.1038/s41588-021-00857-4.
3. Hou L, Heilbronner U, Degenhardt F, et al. Genetic variants associated with response to lithium treatment in bipolar disorder: a genome-wide association study. Lancet. 2016;387:1085-1093. doi:10.1016/S0140-6736(16)00143-4.
4. International Consortium on Lithium Genetics (ConLiGen). Exploring the genetics of lithium response in bipolar disorders. Int J Bipolar Disord. 2024. doi:10.1186/s40345-024-00341-y.
5. Amare AT, Schubert KO, Hou L, et al. Association of polygenic score for major depression with response to lithium in patients with bipolar disorder. Mol Psychiatry. 2021;26:2457-2470. doi:10.1038/s41380-020-0689-5.
6. Ferreira MAR, O'Donovan MC, Meng YA, et al. Collaborative genome-wide association analysis supports a role for ANK3 and CACNA1C in bipolar disorder. Nat Genet. 2008;40:1056-1058. doi:10.1038/ng.209.
7. Shkundin A, Halaris A. Associations of BDNF/BDNF-AS SNPs with Depression, Schizophrenia, and Bipolar Disorder. J Pers Med. 2023;13:1395. doi:10.3390/jpm13091395.
8. Fernandes BS, Molendijk ML, Kohler CA, et al. Peripheral brain-derived neurotrophic factor (BDNF) as a biomarker in bipolar disorder: a meta-analysis of 52 studies. BMC Med. 2015;13:289. doi:10.1186/s12916-015-0529-7.
9. Berk M, Kapczinski F, Andreazza AC, et al. Pathways underlying neuroprogression in bipolar disorder: focus on inflammation, oxidative stress and neurotrophic factors. Neurosci Biobehav Rev. 2011;35:804-817. doi:10.1016/j.neubiorev.2010.10.001.
10. Favre P, Pauling M, Stout J, et al. Widespread white matter microstructural abnormalities in bipolar disorder: evidence from mega- and meta-analyses across 3033 individuals. Neuropsychopharmacology. 2019;44:2285-2293. doi:10.1038/s41386-019-0485-6.
11. Phillips ML, Swartz HA. A critical appraisal of neuroimaging studies of bipolar disorder: toward a new conceptualization of underlying neural circuitry and a road map for future research. Am J Psychiatry. 2014;171:829-843. doi:10.1176/appi.ajp.2014.13081008.
12. Strakowski SM, Adler CM, Almeida J, et al. The functional neuroanatomy of bipolar disorder: a consensus model. Bipolar Disord. 2012;14:313-325. doi:10.1111/j.1399-5618.2012.01022.x.
13. Hibar DP, Westlye LT, Doan NT, et al. Cortical abnormalities in bipolar disorder: an MRI analysis of 6503 individuals from the ENIGMA Bipolar Disorder Working Group. Mol Psychiatry. 2018;23:932-942. doi:10.1038/mp.2017.73.
14. Hibar DP, Westlye LT, van Erp TGM, et al. Subcortical volumetric abnormalities in bipolar disorder. Mol Psychiatry. 2016;21:1710-1716. doi:10.1038/mp.2015.227.
15. Berk M, Copolov DL, Dean O, et al. N-acetyl cysteine for depressive symptoms in bipolar disorder - a double-blind randomized placebo-controlled trial. Biol Psychiatry. 2008;64:468-475. doi:10.1016/j.biopsych.2008.04.022.
16. Bahji A, Vazquez GH, Zarate CA. Comparative efficacy of racemic ketamine and esketamine for depression: a systematic review and meta-analysis. J Affect Disord. 2024. (IV ketamine vs ECT for MDD/BD meta-analysis.)
17. Yatham LN, Kennedy SH, Parikh SV, et al. CANMAT and ISBD 2018 guidelines for the management of patients with bipolar disorder. Bipolar Disord. 2018;20:97-170. doi:10.1111/bdi.12609.
18. Geddes JR, Calabrese JR, Goodwin GM. Lamotrigine for treatment of bipolar depression: independent meta-analysis and meta-regression of individual patient data from five randomised trials. Br J Psychiatry. 2009;194:4-9. doi:10.1192/bjp.bp.107.048504.
19. Nusslock R, Almeida JRC, Forbes EE, et al. Waiting to win: elevated striatal and orbitofrontal cortical activity during reward anticipation in euthymic bipolar disorder adults. Bipolar Disord. 2012;14:249-260. doi:10.1111/j.1399-5618.2012.01012.x.
20. Bipolar Disorder, Circadian Rhythm and Clock Genes (review). Clin Psychopharmacol Neurosci. 2024. PMC11024693.
21. Modabbernia A, Taslimi S, Brietzke E, Ashrafi M. Cytokine alterations in bipolar disorder: a meta-analysis of 30 studies. Biol Psychiatry. 2013;74:15-25. doi:10.1016/j.biopsych.2013.01.007.
22. Ketamine for bipolar depression: a systematic review. Int J Neuropsychopharmacol. 2021;24:535-545. doi:10.1093/ijnp/pyab031.
