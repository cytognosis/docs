# Transdiagnostic Neuropsychiatric Axes — Literature Synthesis / Research Dossier

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: researchers, stakeholders
> **Tags**: `literature-synthesis`, `dimensional`, `rdoc`, `hitop`, `transdiagnostic-axes`
> **Variants**: Technical (this doc) - Readable (`simple/psych-axes-synthesis.md`) - Agent (n/a)

> [!NOTE]
> **TL;DR**: Psychiatric categories (DSM/ICD) map poorly onto biology. Two dimensional frameworks, RDoC (top-down constructs) and HiTOP (bottom-up empirical structure), plus data-driven genomics and neuroimaging, converge on a small set of transdiagnostic axes. This dossier is the canonical prose synthesis; the machine-readable RDoC harmonization (22 matrices) lives under `rdoc-harmonization/`.

> **Reading time**: ~12 min. **If you only read one thing**: RDoC and HiTOP are complementary (mechanism vs psychometrics); their signed interface (Michelini 2021) plus genomic factor models (Grotzinger 2025) define the axes the platform operationalizes.

---

## 1. Research Question and Scope

**Question**: Along what transdiagnostic axes is human neuropsychiatric variation organized, and how do top-down (construct) and bottom-up (data-driven) approaches converge?
**Scope**: RDoC, HiTOP, their crosswalk, and genomic/neuroimaging dimensional evidence. Machine-readable harmonization is maintained separately (Section 4).
**Why it matters**: defines the dimensional coordinate system for the Cytognosis platform and the disease-biotype work.

## 2. Seed Papers / Organizing References

| # | Citation (author year) | Why it anchors | DOI |
|---|------------------------|----------------|-----|
| 1 | Insel et al. 2010; Cuthbert & Insel 2013 (RDoC) | Top-down construct framework | 10.1176/appi.ajp.2010.09091379 |
| 2 | Kotov et al. 2017 (HiTOP) | Bottom-up empirical taxonomy | 10.1037/abn0000258 |
| 3 | Michelini et al. 2021 (RDoC-HiTOP interface) | The signed crosswalk | 10.1016/j.cpr.2021.102025 |
| 4 | Grotzinger et al. 2025 (14-disorder genomic factors) | Data-driven axis validation | 10.1038/s41586-025-09820-3 |

## 3. Evidence Synthesis

### 3.1 Converging evidence review (merged full version)

Psychiatric diagnoses in the Diagnostic and Statistical Manual (DSM; APA, 2013\) are typically symptom-driven, leaving a large gap between available disease annotations and therapeutically actionable molecular circuits. Furthermore, these diagnoses treat disorders as discrete and unitary entities, whereas recent research suggests they are highly comorbid, span a continuous spectrum, and exhibit heterogeneous symptomatology among patients sharing the same diagnosis, driven in part by shared molecular and circuit-level mechanisms that cut across traditional diagnostic boundaries (Feczko et al., 2019; Stephan et al., 2016). The need for an alternative, quantitative, and mechanistically grounded representation of human psychopathology is now widely accepted within the field, recently underscored by Steven Hyman, former NIMH Director, in his 2025 keynote address "Precision Psychiatry," titled "Time to Retire the DSM and Begin Again."

Extensive evidence points to five major limitations of categorical classifications that make them a poor guide for both research and clinical practice (Cuthbert & Insel, 2013; Kotov et al., 2017; Michelini et al., 2021). First, categorical diagnoses do not adequately reflect the extensive evidence that forms of psychopathology and their underlying processes are continuous in nature; the imposition of artificial categories leads to low diagnostic reliability, diagnostic instability (due to symptoms presenting just above or below the clinical threshold), and failure to recognize subthreshold presentations associated with poor functional outcomes and increased risk for more severe psychopathology (Markon et al., 2011; Shankman et al., 2009). Second, traditional diagnoses are based on subjective reports or observations of symptoms and do not account for underlying etiological and pathophysiological mechanisms that often span diagnostic boundaries, even though this information may be critical for selecting effective treatments (Bzdok & Meyer-Lindenberg, 2018). Third, traditional classifications focus on individual diagnoses and ignore widespread comorbidity and developmental continuity across disorders, substantially undermining the prediction of illness course and the accuracy of treatment decisions (Caspi et al., 2020; McIntyre et al., 2012). Fourth, DSM and ICD do not provide tools to address the extensive heterogeneity within each diagnosis, which causes individuals with the same diagnosis to differ greatly from one another and leads to variable treatment responses (Fried, 2017). Fifth, symptom overlap across diagnostic categories (e.g., distractibility, anhedonia) complicates differential diagnosis and contributes to misdiagnosis (Asherson et al., 2014).

Two major dimensional frameworks have emerged over the past decade to address these limitations with complementary strategies: the Research Domain Criteria (RDoC) framework and the Hierarchical Taxonomy of Psychopathology (HiTOP). More recently, large-scale data-driven analyses of genomic architecture and neuroimaging activation patterns have begun to validate, refine, and challenge both frameworks from the bottom up. Together, these converging lines of evidence are defining the transdiagnostic axes along which human neuropsychiatric variation is organized, providing the scientific foundation for the multi-scale integration that our platform seeks to operationalize.

### Construct-Driven (Top-Down) Approaches: From Symptoms to Dimensions

#### The Research Domain Criteria (RDoC) Framework

The **Research Domain Criteria (RDoC)** framework (Insel et al., 2010; Cuthbert & Insel, 2013), developed by the National Institute of Mental Health (NIMH), is a neuroscience-rooted research framework that aims to further our understanding of transdiagnostic biobehavioral systems underlying psychopathology, ultimately paving the way for refined psychiatric classifications and precision approaches to mental health. RDoC organizes core dimensions of behavior using a **dimensional approach**, viewing mental health and illness on a continuum rather than as binary categories. The framework is operationalized as a matrix: rows represent functional constructs grouped into six higher-order **domains** (Negative Valence Systems, Positive Valence Systems, Cognitive Systems, Systems for Social Processes, Arousal/Regulatory Systems, and Sensorimotor Systems), while columns represent eight **units of analysis** spanning from genes, molecules, and cells through circuits, physiology, behavior, paradigms, and self-reports (Kozak & Cuthbert, 2016). Domains, constructs, and subconstructs were defined through expert consensus by reviewing the scientific literature on major systems relevant to typical and atypical human behavior. This multi-scale structure explicitly encodes the premise that variations along neuropsychiatric axes are driven by factors operating across biological levels, from genomic variation to observable behavior.

RDoC primarily addresses three of the five limitations outlined above: the dimensional nature of psychopathology that categories fail to capture, the absence of etiological and pathophysiological mechanisms from current diagnoses, and the extensive within-disorder heterogeneity that makes individuals sharing the same diagnosis differ greatly from one another (Michelini et al., 2021). By encouraging research organized around biobehavioral systems rather than diagnostic boundaries, RDoC seeks to elucidate the processes underlying mental health problems and inform their future classification.

#### The Hierarchical Taxonomy of Psychopathology (HiTOP)

The **Hierarchical Taxonomy of Psychopathology (HiTOP)** (Kotov et al., 2017; Kotov et al., 2021), developed by a consortium of researchers studying psychiatric nosology, proposes a hierarchical, dimensional classification of mental health problems based on observed covariation among signs, symptoms, maladaptive behaviors, and traits. Constructed through extensive factor-analytic and latent class research, HiTOP organizes psychopathology according to its natural covariance structure at multiple levels of specificity: narrow **symptom components** (e.g., dysphoria, suicidal ideation) aggregate into broader **syndromes** (e.g., depression), which cluster into **subfactors** (e.g., Distress), which in turn compose six **spectra** (Internalizing, Disinhibited Externalizing, Antagonistic Externalizing, Thought Disorder, Detachment, and Somatoform). At the apex sits a general factor of psychopathology, or *p*\-factor (Caspi & Moffitt, 2018). Seven subfactors have been identified within the spectra: Fear, Distress, Mania, and Eating Pathology within Internalizing; Substance Abuse and Antisocial Behavior within Disinhibited Externalizing; and Sexual Problems provisionally linked to Somatoform (Kotov et al., 2017).

HiTOP primarily addresses the first, third, fourth, and fifth limitations: the dimensional nature of psychopathology, widespread comorbidity, within-disorder heterogeneity, and symptom overlap between diagnostic categories. By delineating broader dimensions that explain psychiatric comorbidity alongside specific dimensions that accommodate heterogeneity, the system seeks to provide more informative research and treatment targets than traditional diagnostic categories (Michelini et al., 2021; Mullins-Sweatt et al., 2020).

#### Complementary Strengths and Key Differences

Despite their shared commitment to dimensional approaches and their shared recognition of the limitations of categorical diagnosis, RDoC and HiTOP differ in important ways that make them complementary rather than redundant (Michelini et al., 2021).

First, the two frameworks derive their dimensions by different methods. RDoC domains and constructs were **rationally defined** through expert consensus regarding biobehavioral systems relevant to mental health, whereas HiTOP dimensions reflect a **replicated empirical structure** of psychopathology based on covariation among signs, symptoms, diagnoses, and maladaptive behaviors. Second, the frameworks differ in content and level of analysis: RDoC spans from genes to brain to behavior, placing particular emphasis on neurobiology (e.g., neural circuits), while HiTOP focuses on clinical phenomena assessed through interviews, observer reports, and self-reports. Third, each framework has characteristic gaps. RDoC currently includes self-report and behavior units of analysis, but these do not encompass the majority of signs, symptoms, and behaviors requiring clinical attention (e.g., suicidality, hazardous substance use), and many exemplars in the matrix have inadequate or unclear psychometric properties (Patrick & Hajcak, 2016). Consequently, RDoC functions as a research framework with limited direct clinical applicability. HiTOP, conversely, describes clinical phenomena with psychometric rigor but remains agnostic regarding etiology, offering no inherent mechanism for explaining *why* dimensions of psychopathology cohere.

These complementary gaps create a natural interface: HiTOP can supply psychometrically robust clinical targets for RDoC-informed research, while RDoC provides a transdiagnostic framework for elucidating the neurobiological underpinnings of HiTOP dimensions beyond what categorical diagnoses permit.

#### Mapping RDoC Domains onto HiTOP Spectra

Michelini et al. (2021) systematically delineated this interface through a comprehensive narrative review linking RDoC constructs and subconstructs to HiTOP spectra and subfactors, drawing on evidence from self-report, behavioral, psychophysiological, and neuroimaging studies. Their analysis revealed numerous associations of varying strengths across the two systems, with several core connections standing out for their consistency across multiple constructs within each RDoC domain.

**Negative Valence Systems** showed robust positive associations with the HiTOP **Internalizing** spectrum. RDoC Acute Threat and Potential Threat constructs were most strongly linked to the Fear subfactor (e.g., phobias, panic, OCD), supported by enhanced startle potentiation to uncertain threat, hyperactivation of the fear circuit (amygdala, insula, anterior cingulate and prefrontal cortex), and increased avoidance and freezing behaviors. RDoC Sustained Threat and Loss constructs were robustly linked to the Distress subfactor (e.g., depression, PTSD, generalized anxiety), supported by associations with altered amygdala reactivity, punishment sensitivity, helpless behavior, rumination, and shame/guilt.

**Positive Valence Systems** showed strong negative associations with the HiTOP **Disinhibited Externalizing** spectrum, with one notable exception: the Substance Abuse subfactor showed some positive associations (e.g., enhanced effort-based decision-making, habit formation), suggesting that substance use has specific reward-processing correlates that distinguish it from other externalizing dimensions. Blunted reward responsiveness and impaired reward learning were robustly linked to the Distress subfactor, while atypical reward anticipation and prediction error signaling were associated with both Substance Abuse and Thought Disorder.

**Cognitive Systems** dysfunction was robustly linked to both HiTOP **Thought Disorder** (via impairments in attention, perception, declarative memory, language, and working memory associated with psychotic symptoms) and **Disinhibited Externalizing** (via attentional lapses, response inhibition deficits, and working memory impairments associated with impulsivity, inattention, and hyperactivity). Performance monitoring showed a distinctive double dissociation: enhanced error-related negativity (ERN) was linked to the Fear subfactor (especially OCD), while blunted ERN was linked to Disinhibited Externalizing.

**Systems for Social Processes** were negatively associated with HiTOP **Thought Disorder**, **Detachment**, and **Antagonistic Externalizing** spectra. Impaired facial emotion recognition, deficient empathic functioning, and attachment insecurity were common across these spectra, consistent with the prominent role of social dysfunction in the forms of psychopathology they subsume.

**Arousal and Regulatory Systems** were linked to HiTOP **Internalizing**, but with opposite signs across constructs: elevated arousal (e.g., increased skin conductance, cortisol, psychomotor agitation) was positively associated with the Distress subfactor, whereas poor sleep quality was negatively associated with it. Reduced arousal (hypo-arousal) was linked to both Disinhibited Externalizing (inattention, hyperactivity-impulsivity) and Antagonistic Externalizing (psychopathic traits), consistent with theoretical accounts proposing arousal dysregulation as a core underpinning of externalizing behavior. Circadian rhythm disruption (eveningness) showed associations with most forms of psychopathology, suggesting a tentative link to the general *p*\-factor.

Taken together, these mappings demonstrate that although the interplay between biobehavioral systems and clinical dimensions is complex, a set of core connections can be identified that may serve as the foundation for a nosology integrating both clinical presentation and etiological underpinnings.

#### Limitations of Construct-Driven Approaches

Despite their considerable advances, existing top-down efforts to define neuropsychiatric axes, including both RDoC and HiTOP, share important limitations. Both frameworks begin with clinical symptomatology or expert-defined behavioral constructs and then map them onto underlying biology. However, recent studies suggest that symptom-derived factors may be insufficiently specific or overly broad relative to the underlying brain circuitry they seek to elucidate (Beam et al., 2021; Quah et al., 2025). The many-to-many mapping between biobehavioral systems and clinical dimensions, reflected in the large number of cross-domain associations identified by Michelini et al. (2021), underscores this challenge: most RDoC constructs associate with multiple HiTOP spectra, and most HiTOP dimensions associate with multiple RDoC domains, consistent with high psychiatric comorbidity and limited biomarker specificity (Caspi et al., 2020). Moreover, multiple etiological pathways can contribute to similar clinical presentations in different individuals (Kendler, 2019), and biobehavioral correlates of a given dimension may shift across development (Tseng et al., 2019). These observations motivate complementary data-driven approaches that begin not from symptoms but from biological substrates, allowing dimensional structure to emerge from genomic, connectomic, and cellular data rather than being imposed by clinical observation.

### Data-Driven (Bottom-Up) Approaches: From Biology to Dimensions

#### Genomic Architecture of Transdiagnostic Risk

The most comprehensive genomic examination of cross-disorder psychiatric risk to date, Grotzinger et al. (2025) applied genomic structural equation modeling (genomic SEM) to GWAS data from over one million cases across 14 childhood- and adult-onset psychiatric disorders. Their analysis identified five latent genomic factors that collectively explained approximately 66% of the genetic variance across individual disorders: (F1) a Compulsive disorders factor defined by anorexia nervosa, OCD, and (more weakly) Tourette's syndrome and anxiety; (F2) a Schizophrenia-Bipolar (SB) factor; (F3) a Neurodevelopmental factor defined by ASD, ADHD, and Tourette's syndrome; (F4) an Internalizing disorders factor defined by major depression, PTSD, and anxiety; and (F5) a Substance Use Disorders (SUD) factor defined by opioid, cannabis, alcohol use disorders, nicotine dependence, and (to a lesser extent) ADHD.

These five genomic factors show striking correspondence with the higher-order spectra proposed by HiTOP, particularly the Internalizing, Thought Disorder, and Externalizing dimensions, providing independent, biology-first validation of a hierarchical dimensional structure for psychopathology. A hierarchical model further revealed a general psychopathology factor (the *p*\-factor) on which the Internalizing factor loaded most strongly (0.95), consistent with conceptualizations of *p* as reflecting a general tendency toward negative emotionality.

Several key observations emerged from this work. First, disorders loading on the same genomic factor were largely indistinguishable at the level of individual genetic variants: over 99% of case-case GWAS hits were identified for disorder pairs loading on separate factors. Second, functional annotation revealed divergent neurobiological substrates across factors: the SB factor was enriched in excitatory neuron populations (including hippocampal CA1/CA3 neurons and maturing excitatory neurons in fetal brain), while the Internalizing factor was more consistently enriched in glial cell types, particularly oligodendrocytes and their precursors. Third, broadly pleiotropic variants shared across all 14 disorders were enriched for early neurodevelopmental processes and transcriptional regulation, with the strongest expression differences between factor-associated and disorder-specific genes observed during fetal and early postnatal development. Fourth, the *p*\-factor was most strongly associated with external traits reflecting stress sensitivity, loneliness, neuroticism, self-harm ideation, and suicide attempts, while more specific factor-level associations (e.g., the SB and SUD factors with risk tolerance; the Neurodevelopmental factor with childhood aggression) captured clinically meaningful variation that the general factor alone could not explain.

These findings establish that the genetic architecture of psychiatric disorders is organized along dimensional axes that cut across diagnostic boundaries, with both shared and factor-specific biological mechanisms operating at distinct levels of the hierarchy.

#### Neuroimaging-Derived Dimensional Signatures

Complementing the genomic evidence, a parallel line of data-driven research has used neuroimaging to ask whether the dimensional structure of psychiatric variation can be recovered directly from brain circuitry, rather than imposed by clinical observation. This work addresses a fundamental question: do the axes defined by symptom covariation (HiTOP) or expert consensus (RDoC) correspond to the axes along which brain function actually varies?

Recent studies suggest the answer is nuanced. Beam et al. (2021) applied text-mining and machine learning to a large corpus of neuroimaging studies and found that a bottom-up, data-driven ontological framework generated brain circuit-function links that were more reproducible than either the RDoC or DSM frameworks. Critically, their analysis revealed that multiple RDoC domains (negative valence, positive valence, and arousal/regulatory systems) shared substantial mutual information across the frontal-medial cortex and the amygdala, indicating overlap among nominally distinct domains. They also found that the RDoC negative valence domain encompassed constructs that, from a data-driven perspective, recombine elements of memory, reward, and cognitive systems, suggesting that symptom-defined boundaries do not cleanly map onto underlying circuitry.

Quah et al. (2025) extended this work using a latent-variable approach with bifactor analysis, examining 84 whole-brain task-based fMRI activation maps from 19 studies that encompassed 6,192 participants. They compared four model architectures: theory-driven RDoC factor models (with and without a general factor) and data-driven empirical factor models (with and without a general factor). Their analysis yielded three key findings. First, adding a task-general factor to the conventional RDoC framework significantly improved model fit, suggesting that a superordinate domain representing shared activation across functional tasks is missing from the current framework. Second, a data-driven bifactor model consistently outperformed RDoC models when validated against both held-out whole-brain activation maps (internal validation) and peak coordinate activation maps from Neurosynth (external validation), demonstrating generalizability across data types. Third, the RDoC Cognitive Systems domain exhibited low intra-domain consistency, with its constituent constructs (attention, working memory, semantic processing/perception, and theory of mind) forming separate data-driven factors, suggesting that this single domain may be better represented as multiple distinct domains. In contrast, the Sensorimotor Systems, Positive Valence Systems, and Social Processes domains showed relatively coherent activation patterns confined to fewer data-driven factors.

Notably, Quah et al. found that no activation maps in their dataset fit within the RDoC Arousal and Regulatory Systems domain, identifying it as underrepresented in the current neuroimaging literature and underscoring the need for task paradigms specifically targeting this domain. Their analysis also revealed that the Negative Valence Systems domain, while not loading significantly on any single data-driven factor, showed strong factor score correlations with two data-driven factors, suggesting that its boundaries may need reconsideration.

These neuroimaging findings converge with the genomic evidence from Grotzinger et al. (2025) on a central point: dimensions defined by clinical observation or expert consensus do not straightforwardly map onto the axes along which biology varies. The genomic factors identified by Grotzinger et al. explained approximately 66% of genetic variance but left a median of 33.5% unexplained, with some disorders (e.g., Tourette's syndrome, 87% residual) showing a substantial unique signal. Similarly, the neuroimaging-derived factors of Quah et al. captured meaningful structure in brain activation patterns but achieved only moderate overall model fit, reflecting the irreducible complexity of brain-behavior relations. Both lines of evidence point to the same conclusion: the true axes of neuropsychiatric variation are only partially captured by existing frameworks, and a more complete mapping will require integration across biological scales rather than reliance on any single level of analysis.


## 4. Machine-readable harmonization (RDoC matrices)

The RDoC units-of-analysis harmonization (6 units, 58 constructs, 922 associations) and the signed RDoC to HiTOP crosswalk are maintained as CSV matrices with an index:

- **Index**: `rdoc-harmonization/README.md`
- **Matrices**: `rdoc-harmonization/matrices/` (construct x unit association matrices, incl. `matrix_hitop*.csv`)
- **Reference tables**: `rdoc-harmonization/reference_tables/` (ontology mappings: PubChem, Cell Ontology, Allen atlas, SNOMED, HPO/NBO/PATO)
- **Clinical instruments crosswalk**: `../../cytoverse/behavioral/clinical-instruments/` (PHQ-9/GAD-7, DASS, schizophrenia symptoms)
- **Neuroplasticity axes**: `BDNF_TrkB_Neuroplasticity_Axes_Dossier_2026-06-03.md`

## 5. Most Defensible Axes (cross-framework)

1. **Internalizing / Negative-Valence** (Fear vs Distress subfactors): amygdala-insula-ACC threat circuitry; robust RDoC-HiTOP link. Confidence: HIGH.
2. **Externalizing / Positive-Valence and disinhibition**: reward-processing and response-inhibition dimensions; substance-abuse reward correlates distinct. Confidence: MEDIUM-HIGH.
3. **Thought Disorder / Cognitive Systems**: attention, working memory, perception deficits; 40Hz ASSR and spindle signatures (see biotypes). Confidence: MEDIUM-HIGH.
4. **Detachment / Social Processes**: facial-emotion, empathy, attachment deficits across thought-disorder, detachment, antagonistic spectra. Confidence: MEDIUM.
5. **Arousal / Regulatory** (incl. circadian): signed links to Distress and externalizing; eveningness tentatively linked to the p-factor. Confidence: MEDIUM.
6. **Cross-cutting plasticity (BDNF/TrkB)**: strongest single transdiagnostic molecular axis (see disease-biotypes cheat sheet). Confidence: HIGH.

## 6. Gaps and Open Questions

- RDoC self-report/behavior units have uneven psychometrics; HiTOP is agnostic on etiology. The interface is the value.
- Drysdale four-biotype result did not replicate (Dinga 2019); prefer Williams six-axis scaffold.
- Genomic factor structure (Grotzinger 2025) vs construct frameworks: alignment is partial and active.

## 7. Provenance and Maintenance

- **Folds in**: the SOTA "Converging Evidence for Transdiagnostic Neuropsychiatric Axes" review (long version). Original kept as raw source at `05-Research/foundational/problem-and-gap/original/` with a pointer banner (also holds short and ultra-short variants).
- **Related synthesis (archived history, not modified)**: `03-Products/Cytonome/Yar/_archive/consolidation_2026-06-21/_research/PSYCH_AXES_SYNTHESIS.md`.
- **Strategy landscape**: `01-Strategy/ai-ml-dimensional-biotyping-landscape-2026.md`.
- **Last verified**: 2026-07-10.
- **Revisit when**: new RDoC/HiTOP crosswalk data or genomic factor release.
