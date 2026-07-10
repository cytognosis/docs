Before I give any comments, I want to provide further clarification before we proceed, which you should fully understand, comprehend, appreciate, and consolidate with what we discussed earlier, including our core discussion regarding the phenotypic heterogeneity/diversity in the patient population (i.e., phenotypic diversity of patients) and mechanistic heterogeneity/diversity in the patients manifesting identical phenotypics (i.e., mechanistic diversity of phenotypes).

# phenotypic diversity of patients

We propose to represent diseases not as single labels, but using their precise phenotypic manifestations/dysregulations (gain/loss of neuro/behavioral symptoms). In the context neuropsychiatric/neurodegenerative disorders, these would be a curated set of neuro-behavioral phenotypes, capturing relevant shifts across Mood, Anxiety, Psychosis, Cognition, Attention, Memory, Motor, Sleep, Social, Personality, Substance Use axes, to name a few. In other words, instead of using “a minimum of X out Y symptoms” from a given list of diagnostic symptoms, which is the approach used in DSM, we represent each disease as the full phenotypic representations, originally extracted/inferred from diagnostic manuals, but then refined based on their population-scale manifestions and covariation. This is key to point out that DSM-diagnostics and clinical intruments/tests (either self-reported such as PHQ-9 or clinician-rated, such as CGI-S), are probing the same set of axes that psychiatric diagnostics are, but often are also applicable for nondiagnostic uses and also for temporal tracking of shifts on these axes. We will use collection of  available de-identified tests to infer population-scale variation/covariation across these phenotypes. These phenotypic representations allow us to:

1. **Disentangle phenotypic components of disorders**, by representing individual "components" of disease and study components (both shared across or unique in different disorders) … e.g., as our early studies are indicating distinct mechanisms are driving the mood vs thought components of bipolar disorders (ongoing work), where the mood component overlaps with MDD-specific dysregulations while the though-axes overlaps with SZ.
2. **Capture patient heterogeneity**, by Refine/fine-tune personalized phenotypic representations for each patients, using disease-specific learned phenotypic distributions as a prior, together with the notes/records/etc, to compute the posterior, personalized phenotypic representation for each patient, allowing us to represent patient heterogeneity.



# mechanistic diversity of phenotypes

Mechanistic diversity is not always at the molecular/micro-scale/enotype resolutions, and infact many of the established biotypes are actually from connectomics data (e.g., our meso-scale/endophenotypes), including the 4 depression biotypes from Drysdale et all, 2017, which are in fact complementary to the molecular/cellular biotypes (our micro-scale/enodtypes). 

Gentypically identical twins with one developing schizophrenia and one not, and many studies built around it to study environmental factors and genotype-environment interactions, is a canonical example of the diversity of factors that *jointly* drive the initiation, progression, and diversity of disease and it's individual phenotypes (especially since these twins often not only share genotype, but also many environmental factors as often are raised in the same family/environment). 

Multimodal is not a gimmick, it's the core to our foundation to exactly solve this mechanistic diversity, precisely: connectomic/mes-scale and genotypic/micro-scale features driving our multimodal axes contribute complementary view, connectomic captures intermediate drivers, which also captures the joint, complex effect of environmental and other factors, making it harder to disentangle them alone, and also is capturing real-life dynamic shifts/trajectories, while genotypic components of the multimodal axes are blind to the life-experience effects (e.g., environmental factors), but are the richest to source to identify detailed molecular mechanisms, when it exists, and complement connectomics, also help to disentangle genotype-environment (GxE) interactions in that case (these are just two examples for the context).



Use these, and all that we have discussed before within this context, and create a fully polished, organized, well-written document capturing all relevant concepts, principles, and definitions cleanly harminized and linked together





# Our Computational Principles

* Using the phenotypic representation of disorders is the key to our formulation, but also it introduces three fundamental challenges (read /home/mohammadi/Documents/Cytognosis/Science/psych/cdisc-qrs-feature-space-design.md and /home/mohammadi/Documents/Cytognosis/Science/psych/cdisc-qrs-comprehensive-reference.md for additional reference):

  * Curating a comprehensive yet compact set of phenotypic features most relevant to represent all psychiatric manifestations/shifts (

    * At a top-level, this could be organized across 16 domains and 12 cross-cutting axes (draft version)

      * Domains:

        * **Consciousness and arousal** (ICF b110 + RDoC Arousal): vigilance, sustained attention to environment, dissociation.
        * **Orientation and insight** (ICF b114 + ICF b1644): time / place / person orientation, insight, judgment.
        * **Intellectual / general cognitive ability** (ICF b117 + Cognitive Atlas g-factor): crystallized vs fluid.
        * **Attention** (ICF b140 + RDoC Cognitive Systems / Attention): sustained, shifting, divided, selective. Operationalized by NIH Toolbox Flanker, DCCS, plus PROMIS Cognitive Function.
        * **Memory** (ICF b144 + RDoC Declarative + Working Memory): episodic, semantic, working, procedural.
        * **Executive function** (ICF b164 + RDoC Cognitive Control): planning, organization, cognitive flexibility, inhibition, problem-solving.
        * **Language** (ICF b167 + RDoC Cognitive Systems / Language): receptive, expressive, integrative, prosody, pragmatics.
        * **Perception** (ICF b156 + b2 + RDoC Perception + Sensorimotor): visual, auditory, olfactory, gustatory, somatosensory, multimodal; perceptual distortions (hallucinations).
        * **Thought** (ICF b160 + HiTOP Thought Disorder): pace, form (disorganization), content (delusions, obsessions), control (intrusions).
        * **Emotional functions** (ICF b152 + HiTOP Internalizing + RDoC NVS / PVS): appropriateness, regulation, range; specific affects: fear, anxiety, sadness, loss, anger, anhedonia, positive affect, irritability.
        * **Energy and drive** (ICF b130 + RDoC PVS): energy level, motivation, appetite, craving, impulse control.
        * **Sleep** (ICF b134 + RDoC Sleep-Wake / Circadian): amount, onset, maintenance, quality, cycle, sleep-related impairment.
        * **Psychomotor and motor** (ICF b147 + b7 + RDoC Sensorimotor): psychomotor agitation / retardation, motor planning, execution, gait, dexterity, strength, balance.
        * **Self and identity** (ICF b180 + RDoC Social Processes / Self): experience of self, body image, time, agency, dissociation.
        * **Social cognition and behavior** (ICF b122 + d7 + RDoC Social Processes + HiTOP Detachment / Antagonism): affiliation, theory of mind, social communication, interpersonal interactions, family / peer relationships.
        * **Personality traits** (ICF b126 + HiTOP traits): negative affectivity, detachment, antagonism, disinhibition, psychoticism, anankastia; plus normal-range Big Five.

      * Cross-cutting vertical axes (mapped to ICF d-component + PROMIS Social / Physical):

        - A. Activities of daily living (ICF d4, d5, d6).

        - B. Communication participation (ICF d3).

        - C. Interpersonal and relational functioning (ICF d7).

        - D. Work / education / economic participation (ICF d8).

        - E. Community / civic participation (ICF d9).

        - F. Quality of life and subjective well-being (PROMIS Meaning and Purpose, Positive Affect, Life Satisfaction).

        - G. Substance use behavior (HiTOP Dis-Ext / Substance + PROMIS Substance Use).

        - H. Eating behavior (HiTOP Internalizing / Eating Pathology + EDE-Q items).

        - I. Sexual function and behavior (ICF b640 + PROMIS SexFS + ASEX).

        - J. Suicidality (HiTOP cross-cut + C-SSRS).

        - K. Aggression and antisocial (HiTOP Antagonistic / Disinhibited Ext).

        - L. Somatic symptoms (HiTOP Somatoform + PROMIS Physical).

  * Mapping disorders and/or instruments to these phenotypic axes

  * Refining/personalizing phenotypic representation of individual patients/users (instead of using phenotypic representations that are shared within diagnoses).

  * These phenotypic representations of disease are the “north star” that we use to “orient” each of our pretrained foundation models across modalities!

* Modality-specific models follow the same direction / timeline:

  * **Large-scale Pretaining**: Modality-specific foundation models are pretrained using self-supervised and/or other disease-agnostic losses (e.g., predicting functional genomic tracks from genetic sequences)  using the largest collection of data available (curated and harmonized across cohorts/datasets)
  * **Phenotypic Orientation**: Fine-tune/orient each model using curated disease-specific datasets (e.g., NeuroBioBank for genotypes (WGS) or PGC (common variants/arrays))
    * This could be using approaches such as Centered Kernel Alignment (CKA) to align patient representations across phenotypic vs other modalities, i.e., phenotypic kernel (of patients) is used as the reference and modality-specific embeddings are regularized to capture as much of the phenotypic representation structure/space as possible (as we discussed, each modality would capture noisy, and partial subsets of phenotypic axes
  * **Dataset-specific cross-modal alignment**: Using disease-specific datasets with more than one modality available (e.g., genomic and connectomic from the ENGIMA Consortium datasets), we will use the same kernel/subspace alignment loss but now instead of reference (phenotype) vs single-modality, all available modalities will contribute to regularization to our reference phenotypic kernel
    * We will also learn a per sample attention weight to know which modalities to focus on, or using a gating network similar to Mixture of Experts (MoE) models.
    * This also bares similarity to the Similarity Network Fusion approach (originally proposed for combining different omics datasets from the same cancer patients using network diffusion across individual modality-specific networks to create a unified patient network)

* Just like a the perfect example of the “elephant and blind men!”

* Sensitivity

* Phenotypes for org, pathway dys for cellular.

* Role of cellular-scale:



Now use this additional 