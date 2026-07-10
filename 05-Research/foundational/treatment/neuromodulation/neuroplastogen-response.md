# Neuroplastogen Differential Response: Trials, Mechanisms, and Biotype Predictors

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: researchers, stakeholders
> **Tags**: `research`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

A landscape review for the Cytognosis Foundation and Hervé Marie-Nelly NSF X-Labs / ARPA-H PHO proposal. Compiled May 25, 2026.

## Scope and thesis

Neuroplastogens are agents that rapidly induce structural and functional neuroplasticity in the central nervous system through BDNF-TrkB signaling, mTOR activation, AMPA receptor potentiation, and dendritic spine growth. The class includes ketamine, the classical serotonergic psychedelics (psilocybin, LSD, DMT, 5-MeO-DMT, ayahuasca), the entactogen MDMA, the iboga alkaloids, and a new generation of engineered non-hallucinogenic congeners. Trials across treatment-resistant depression (TRD), generalized anxiety disorder (GAD), post-traumatic stress disorder (PTSD), alcohol use disorder (AUD), tobacco use disorder, and anorexia nervosa show response rates that consistently outperform standard-of-care monoamine antidepressants on rapid onset, with sustained response in 30–60% of participants. The unresolved problem is identifying who responds. This document inventories the trial evidence and the biotype-level response predictors that could be measured noninvasively. The unifying argument: a plasticity-deficit biotype (low BDNF tone, reduced cortical glutamate dynamics, blunted reward-circuit signaling, low neural-signal complexity) predicts response across the class, and many of these features are accessible through wearable fNIRS, EEG, and digital phenotyping platforms now within Cytoscope's design envelope [1,2,3].

---

## 1. Ketamine and esketamine

### Mechanism

Ketamine is a non-competitive NMDA receptor antagonist. The dominant antidepressant account links transient NMDA blockade on inhibitory parvalbumin interneurons to a glutamate burst, AMPA receptor potentiation, mTORC1 activation, rapid BDNF release, and synaptogenesis in medial prefrontal cortex and hippocampus within hours [4,5]. The (2R,6R)-hydroxynorketamine (HNK) metabolite contributes through an AMPA-dependent, NMDA-independent route in animal models. Sustained antidepressant effects depend on TrkB signaling and on input-specific synaptic adaptations in nucleus accumbens D1-MSNs, particularly at mPFC and ventral hippocampus inputs [6].

### Approval status

Esketamine intranasal spray (Spravato, Janssen) received FDA approval for TRD in March 2019, for major depressive disorder with acute suicidal ideation in August 2020, and a monotherapy expansion for TRD adults without an oral antidepressant in January 2025. Racemic intravenous ketamine remains off-label and is dispensed through hundreds of US infusion clinics under prescriber discretion. No head-to-head randomized comparison of racemic versus esketamine has been published; observational comparisons favor IV ketamine on response and remission, though confounded by dose and route [7].

### Response rates

Across pooled phase 3 and naturalistic data, single-infusion response (50% MADRS or HDRS reduction at 24–72 hours) sits at 50–70% in TRD; sustained response at 4 weeks falls to 30–40% without repeat dosing. The largest real-world dataset from at-home esketamine-equivalent compounding (Mindbloom, n = 11,441) reported 56.4% depression response and 56.1% anxiety response, with PTSD response of 79% and remission of 60% in a 374-patient subset [8]. These naturalistic figures suffer expectancy and selection bias.

### Response predictors and biotypes

- **BDNF Val66Met (rs6265)**: Met carriers show reduced antidepressant response to low-dose racemic ketamine; Val/Val homozygotes respond more reliably [9,10]. This is the strongest pharmacogenetic signal in the class and points directly at TrkB-dependent plasticity as the rate-limiting step.
- **Anhedonic / reward-deficit biotype**: Pizzagalli's Probabilistic Reward Task work shows that ketamine improves reward responsiveness in TRD patients and in chronically stressed rats through the same neural substrate. Animal data localize the effect to D1-MSN strengthening in NAc [6]. Patients with high anhedonia at baseline are over-represented among ketamine responders.
- **Anxious depression (Williams / Drysdale biotypes 1 and 4)**: A meta-analysis of TRD trials found anxious-depression subjects show greater ketamine response and longer time-to-relapse than non-anxious-depression subjects [11]. The Drysdale 2017 biotype scheme (limbic-frontostriatal hyperconnectivity for biotypes 1 and 4) maps onto this anxious-anhedonic responder phenotype, with the caveat that Drysdale's biotype solution did not replicate in independent samples [12]. The 2024 Williams six-biotype refinement in Nature Medicine improves the framework and links specific circuit scores to differential treatment response [13].
- **Default mode network connectivity at baseline**: Reduced lateral PFC to subgenual ACC (sgACC) connectivity predicts response. Increased post-ketamine connectivity between right lateral PFC and sgACC tracks symptom reduction [14]. Baseline amygdala-to-sgACC connectivity discriminates responders and nonresponders with 88.9% sensitivity and 100% specificity in one cohort [15].
- **Anterior cingulate glutamate (MRS)**: Lower baseline ACC glutamate and larger post-infusion glutamate increases in pregenual ACC predict response [16]. The Glx/GABA ratio in dorsal ACC has been advanced as a clinically tractable proxy [17]. This is the most direct neurochemical signal of the rapid-plasticity mechanism.
- **Polygenic depression risk**: Higher MDD polygenic risk scores correlate weakly with reduced ketamine response in pooled samples, though effect sizes are small and the signal is not yet clinically actionable.
- **CYP2B6 metabolism**: Slow metabolizers achieve higher peak plasma ketamine and norketamine and show stronger antidepressant response in some studies [10].
- **Sex**: Meta-analytic data show comparable efficacy by sex, though males may show modestly longer single-dose response durations and females reach higher hydroxynorketamine concentrations. Preclinical models show female greater sensitivity at low doses [18].

### Esketamine versus racemic debate

Esketamine has 2–3 fold higher NMDA affinity than R-ketamine but R-ketamine has produced longer and more potent antidepressant effects in rodents with fewer psychotomimetic effects. Clinical comparisons are observational and consistently favor IV racemic on raw response numbers; PCORI is funding a comparative effectiveness trial (NCT06713616) [7].

---

## 2. Psilocybin

### Mechanism: dual route through 5-HT2A and TrkB

Psilocybin is a prodrug; psilocin is the active species. The canonical mechanism is partial agonism at 5-HT2A receptors on layer-V pyramidal neurons, glutamate release in cortex, and downstream BDNF-dependent plasticity. The Moliner, Castrén, and Olson 2023 paper in Nature Neuroscience demonstrated that psilocin and LSD bind directly to the transmembrane domain of TrkB dimers with affinity roughly 1,000-fold higher than conventional antidepressants, that this binding occurs at a site distinct from but partially overlapping the SSRI binding pocket, and that pharmacological 5-HT2A blockade does not eliminate the plasticity-inducing and antidepressant-like effects of psilocybin in mice [19,20]. This dual mechanism is mechanistically important: it predicts that any human stratification by 5-HT2A genotype alone will miss responders whose benefit derives from direct TrkB binding, and it provides the molecular basis for engineering non-hallucinogenic congeners (see section 8).

### Trial landscape

- **Goodwin et al. NEJM 2022 (COMP360 phase 2b, n = 233)**: Single 25 mg dose produced a –6.6-point MADRS difference versus 1 mg at week 3, with sustained response in roughly twice as many 25 mg recipients as 1 mg recipients through week 12. Remission at week 3 was about 30% at the 25 mg dose [21].
- **Compass Pathways COMP005 (phase 3, n = 258)**: Topline 2025; single 25 mg dose versus placebo met the primary MADRS endpoint with statistical significance and no unexpected safety signals.
- **Compass Pathways COMP006 (phase 3, n = 568)**: Topline 2026; two fixed 25 mg doses three weeks apart versus 1 mg active comparator, –3.8 MADRS point difference at primary endpoint (p < 0.001). This is the first replicated phase 3 readout in psychedelic-assisted therapy [22].
- **Usona psilocybin (phase 2, JAMA 2023)**: 25 mg in non-resistant MDD produced large MADRS reductions versus placebo at week 8.
- **Bogenschutz JAMA Psychiatry 2022 (AUD, n = 93)**: Psilocybin-assisted therapy produced 83% reduction in heavy drinking days versus 51% in diphenhydramine placebo arm over 32 weeks [23].
- **Peck Nature Medicine 2023 (anorexia nervosa, n = 10)**: Phase 1 open-label feasibility; safe and tolerated; 60% of participants reported reduced appearance concerns at 3 months. Weight restoration was not the endpoint [24].
- **Johnson Johns Hopkins (tobacco use disorder)**: Pilot 2014 found 80% smoking abstinence at 6 months and 67% at 12 months in 15 participants. The expanded 2026 RCT versus nicotine patch (n ≈ 80) reported 40.5% prolonged abstinence with psilocybin versus 10.0% with patch [25].

### Response predictors and biotypes

- **Default mode network disintegration during dosing**: Acute DMN desynchronization, measured by reduced functional connectivity within DMN nodes and reduced network modularity, correlates with sustained BDI reductions across Imperial College trials. Carhart-Harris's REBUS model frames this as relaxation of high-level priors that allows new affective predictions to be encoded [26].
- **Personality openness**: MacLean, Johnson, Griffiths 2011 showed a sustained openness increase 1 year post-session in participants who reported mystical-type experiences [27]. Baseline openness predicts session quality in observational data, and openness shift mediates downstream clinical effects in some analyses.
- **"Ego dissolution" intensity**: The Ego Dissolution Inventory score and Mystical Experience Questionnaire MEQ30 score during dosing are the strongest within-trial mediators of MADRS change to date. The mediation is partial and contested: COMP360 phase 2b data show MEQ30 predicts response only weakly after adjustment for dose and baseline severity.
- **Baseline BDNF and plasticity markers**: Serum BDNF does not reliably track central BDNF and has limited predictive value in meta-analyses [28]. Peripheral BDNF response to a single psilocybin dose is null in pooled data. This argues that wearable surrogates of plasticity (cortical excitability, signal complexity, fNIRS hemodynamic dynamics) should be developed in parallel.
- **Trait absorption and prior psychedelic experience**: Modestly predictive in observational datasets; confounded with expectancy.

### Replication and unblinding caveats

Functional unblinding is a structural feature of psychedelic trials: a participant who experiences ego dissolution knows they are on active drug. Expectancy effects inflate self-reported outcomes. The FDA's August 2024 rejection of Lykos MDMA cited blinding as a primary concern. The Compass COMP006 design partially mitigates this by comparing two active psilocybin doses (25 mg versus 1 mg) rather than placebo, though 1 mg is not subjectively inert. Independent rater blinding and active-comparator designs are the current best mitigations [29].

---

## 3. MDMA-assisted psychotherapy

### Mechanism

MDMA is a substituted amphetamine that releases serotonin via SERT reversal and, secondarily, dopamine and norepinephrine. Acute oxytocin release and reduced amygdala fear response create a therapeutic window in which trauma memories can be reconsolidated without the usual fear-circuit interference. Downstream BDNF increases and TrkB-dependent plasticity have been documented in rodents; Dölen and colleagues showed MDMA reopens a social reward learning critical period through oxytocin-receptor-dependent metaplasticity in NAc with a duration of about 2 weeks, longer than ketamine but shorter than LSD [30,31].

### Trial results

- **MAPP1 Nature Medicine 2021 (n = 90, severe PTSD)**: 67% of MDMA-arm participants no longer met PTSD criteria at primary endpoint versus 32% in placebo plus therapy [32].
- **MAPP2 Nature Medicine 2023 (n = 104, moderate to severe PTSD)**: Replicated MAPP1 with 71.2% loss of PTSD diagnosis versus 47.6% in placebo arm; Cohen's d roughly 0.7 [33].
- Subgroup analyses showed treatment was not significantly affected by dissociative subtype, severe adverse childhood experiences, alcohol or substance use comorbidity, or baseline severity. Patients with dissociative subtype showed numerically larger CAPS-5 reductions in pooled analyses.

### FDA status (as of May 2026)

In August 2024 the FDA issued a Complete Response Letter to Lykos Therapeutics rejecting the MDMA NDA, citing safety reporting integrity, functional unblinding, expectancy effects, and questions about trial durability. The CRL was made public September 2025. The FDA requested a third phase 3 study. Lykos reduced workforce by approximately 75% and reorganized as Resilient Pharmaceuticals; as of May 2026 there is no approved resubmission. The MDMA setback has reshaped FDA expectations for the entire class [34,35].

### Response predictors

- **Dissociative PTSD subtype (Lanius)**: Conceptually predicted to respond well because MDMA reduces dissociation acutely. MAPP1 and MAPP2 pooled subgroup analyses confirm at least equivalent response in dissociative subtype, with a trend to greater absolute CAPS-5 reduction [32,33].
- **Childhood trauma**: Adverse Childhood Experiences (ACE) score does not attenuate response in MAPP cohorts; this is unusual because childhood-onset PTSD predicts worse response to standard SSRIs and to prolonged exposure therapy.
- **Initial response trajectory**: Session 1 response is the strongest single predictor of session 3 outcome in MAPS pooled data, suggesting an early-responder phenotype that could be flagged within days of first dose.
- **Oxytocin receptor polymorphisms (OXTR rs53576)**: Hypothesized predictor based on the Dölen mechanism but not yet adequately powered in clinical samples.

---

## 4. Ibogaine and ibogaine analogs

### Mechanism

Ibogaine is a complex multi-target drug: NMDA antagonism, kappa-opioid agonism, mu-opioid modulation, sigma-2 agonism, nicotinic acetylcholine antagonism, and SERT inhibition. Its active metabolite noribogaine has a long half-life (24–48 hours) and is thought to drive sustained anti-craving effects. The compound increases GDNF and BDNF expression in VTA dopamine neurons. The non-hallucinogenic congener tabernanthalog (TBG) was engineered by Olson's lab to preserve the plasticity-inducing and anti-addictive properties while removing cardiac and hallucinogenic effects [36].

### Trial evidence

- **Stanford Magnesium-Ibogaine: The Stanford Experience (MISTIC)**: Nature Medicine 2024 study of 30 US Special Forces veterans with TBI and chronic psychiatric symptoms. One-month post-treatment, 88% no longer met PTSD criteria; depression and anxiety symptom reductions exceeded 80%. The study used pre-treatment magnesium to mitigate ibogaine cardiotoxicity [37].
- **Heroic Hearts Project and VETS**: Nonprofit-organized veteran cohorts to international ibogaine clinics; observational data only, with selection bias.
- **18-MC (18-methoxycoronaridine)**: MindMed's synthetic analog, phase 1 completed 2022 with favorable safety; phase 2 trajectory unclear as of May 2026.
- **TBG-1 / tabernanthalog**: Preclinical only as of May 2026; reduces alcohol and heroin self-administration in rodents without hallucinogenic effects.

### Cardiac safety

Ibogaine blocks the hERG potassium channel and causes QT/QTc prolongation. Torsades de pointes, ventricular fibrillation, and cardiac arrest have been reported in clinical and unsupervised settings, including at therapeutic doses in people without preexisting cardiac disease [38]. CYP2D6 polymorphisms drive interindividual variability. The magnesium pre-treatment strategy (MISTIC) is one risk-mitigation approach; engineered non-cardiotoxic analogs are the alternative.

### Response predictors

Data are sparse. Pretreatment ECG QTc, CYP2D6 phenotype, and substance class (opioid versus alcohol) are the practical stratifiers. Mechanistically, opioid use disorder responders may share the plasticity-deficit profile and BDNF responsiveness seen in ketamine and psilocybin responders.

---

## 5. 5-MeO-DMT

### Mechanism

5-MeO-DMT is a tryptamine with high affinity at 5-HT1A and 5-HT2A receptors; the 5-HT1A action is strong relative to other classical psychedelics and may contribute to its distinct phenomenology (ego dissolution without rich visual content). TrkB binding has been demonstrated in vitro. Inhaled or vaporized 5-MeO-DMT has very fast onset (1–2 minutes) and offset (15–40 minutes), enabling a clinic visit of under an hour.

### Pipeline and trial results

- **GH Research GH001 (inhalable mebufotenin)**: Phase 2b in TRD reported February 2025. N = 81 (40 active, 41 placebo). Primary endpoint MADRS change at day 8: –15.2 points in active arm versus +0.3 in placebo, for a –15.5-point placebo-adjusted difference. Remission at day 8: 57.5% versus 0%. Open-label extension 6-month remission: 77.8% in completers [39]. These are among the largest effect sizes in the field, though small sample and unblinding caveats apply.
- **Beckley Psytech BPL-003 (intranasal 5-MeO-DMT)**: Phase 2b TRD readout 2025 reported rapid and durable MADRS reduction.

### Indications

TRD primary; suicidal ideation secondary (no formal suicidality trial as of May 2026 but the fast offset makes it appealing for acute use).

### Response predictors

Insufficient sample size to derive biotype predictors. The fast pharmacokinetic profile creates an opportunity for tight closed-loop monitoring: a 30-minute clinic visit can capture pre, peri, and post-dose EEG signatures with minimal patient burden.

---

## 6. LSD

### Mechanism

LSD is a non-selective serotonin agonist with strong 5-HT2A activity, dopaminergic effects at D2, and direct TrkB binding (Moliner 2023) [19]. Acute effects last 8–12 hours, longer than psilocybin.

### Trials

- **MindMed MM120 phase 2b (GAD, n = 198)**: Single 100 µg dose of LSD-D-tartrate reduced HAM-A by –7.6 points more than placebo at week 4 (p < 0.001). At week 12, 65% clinical response and 48% remission [40]. FDA Breakthrough Therapy designation March 2024. Phase 3 first patient dosed late 2024. Published JAMA September 2025.
- **University Hospital Basel (LSD for depression and anxiety, phase 2)**: Smaller trials showing reduced anxiety in patients with life-threatening illness.

### Response predictors

GAD-specific predictors are still emerging from MM120. The strong 12-week durability suggests a critical-period reopening effect (Dölen mouse data show LSD opens the social-reward critical period for ~3 weeks) [30].

---

## 7. Ayahuasca and DMT

### Mechanism

DMT is a 5-HT2A agonist with high TrkB affinity. Ayahuasca combines DMT with beta-carboline MAO-A inhibitors (harmine, harmaline, tetrahydroharmine), giving oral bioavailability and a 4-hour experience. Standalone IV DMT (SPL026) bypasses the MAO inhibition and gives a 30-minute experience.

### Trials

- **Palhano-Fontes Psychological Medicine 2018**: Single ayahuasca dose in TRD (n = 29) reduced HAM-D at days 1, 2, and 7 versus placebo, with response rates of 50% at day 1 and 64% at day 7 [41].
- **Small Pharma / Cybin SPL026 phase 2a (n = 34, MDD)**: Single 21.5 mg IV DMT plus therapy versus placebo. –7.4 point MADRS difference at 2 weeks; 57% remission at 3 months [42]. Imperial College and Cybin reporting through 2025.

### Predictors

Sparse; baseline severity and dose intensity dominate.

---

## 8. Non-hallucinogenic plastogens

David Olson coined "psychoplastogen" in 2018 to describe small molecules that rapidly and lastingly promote neuroplasticity. The class includes both classical psychedelics and engineered congeners designed to dissociate plasticity from hallucinogenesis.

- **Tabernanthalog (TBG)**: Ibogaine analog from Olson's lab; preclinical only as of May 2026. Does not produce the rodent head-twitch response (proxy for hallucinogenesis) but promotes dendritic spine growth, reduces alcohol and heroin self-administration, and produces antidepressant-like effects. Recent Nature Neuroscience 2025 work showed TBG induces plasticity through 5-HT2A without the immediate glutamate burst or immediate-early-gene activation seen with classical psychedelics, suggesting a quieter plasticity mechanism [43].
- **DLX-001 (zalsupindole, AAZ-A-154)**: Delix Therapeutics lead; phase 1 in MDD ongoing as of January 2026 [44].
- **DLX-007**: Tabernanthalog-derived, preclinical.
- **Other entrants**: Mindset Pharma 5-MeO-DMT analogs; Terran Biosciences psilocybin and DMT prodrugs.

The non-hallucinogenic class is the strongest argument for biotype stratification on plasticity-deficit endophenotypes: if the therapeutic effect derives entirely from BDNF-TrkB signaling and downstream synaptogenesis, then patients with intact baseline plasticity may not benefit, and patients with deep plasticity deficits should benefit most.

---

## 9. Cross-cutting biotype-response patterns

Three patterns recur across drugs.

### 9.1 The plasticity-deficit biotype

Combining ketamine BDNF Val66Met data, ACC glutamate MRS data, anhedonia-response data, and the Moliner TrkB binding mechanism produces a consistent picture: patients with reduced baseline BDNF tone, lower cortical thickness, reduced spine density in postmortem samples (Duman, Sanacora work), lower ACC glutamate, and blunted reward circuit signaling are over-represented among responders. This is the most testable unifying hypothesis. The Cytoscope plan to monitor cortical hemodynamic dynamics, autonomic variability, and EEG complexity gives plausible noninvasive proxies for all four features.

### 9.2 The critical-period framework

Dölen and colleagues' 2019 Nature paper and 2023 follow-up established that classical psychedelics, MDMA, ibogaine, and ketamine all reopen the social-reward learning critical period in mice, with duration tracking the subjective duration of the human experience: ketamine ~48 hours, psilocybin ~2 weeks, MDMA ~2 weeks, LSD ~3 weeks, ibogaine ~4 weeks [30,31]. This frames the post-dose period as a metaplastic window during which targeted psychological work has outsized effect. Patient features that predict the depth and quality of metaplasticity (developmental history, age, sex, sleep architecture, circadian phase) should predict response. None of these is currently used to triage patients.

### 9.3 Sex and age

Sex differences in response are real but inconsistent across drugs. Female rats are more sensitive to ketamine at low doses through estrogen-dependent NMDA modulation; female humans show comparable clinical response but different pharmacokinetics [18]. Age effects are stronger: older patients respond less to ketamine in pooled meta-analyses, consistent with reduced baseline plasticity. Developmental window effects (e.g., MDMA in adolescents versus adults) are under-studied for ethical and regulatory reasons.

---

## 10. Connectomic predictors

- **DMN baseline integration and acute desynchronization**: The most reproduced connectomic signature across psilocybin, LSD, DMT, and ayahuasca. Higher baseline DMN integration in TRD and larger acute reduction during dosing predict sustained response [26].
- **sgACC connectivity**: Increased post-ketamine connectivity between lateral PFC and sgACC tracks response [14]. Reduced amygdala-sgACC connectivity at baseline predicts ketamine response with high specificity in one cohort [15].
- **Salience network**: Acute reorganization of salience network nodes (anterior insula, dorsal ACC) during psilocybin tracks ego-dissolution intensity, which partially mediates clinical response.
- **Reward circuit**: Ketamine response in anhedonic depression depends on D1-MSN strengthening at mPFC and ventral hippocampus inputs to NAc in mice [6]. Human-side proxies are limited to fMRI reward-task connectivity and ventral striatum-cortical coupling, which require scanner access.
- **Modular reset / REBUS**: Carhart-Harris's framework predicts that acute reduction in network modularity correlates with sustained therapeutic effect. Tested across multiple Imperial trials with consistent partial correlations [26].

---

## 11. EEG/MEG predictors

These signals are tractable for wearables and are a plausible Cytoscope readout.

- **Alpha power**: Reduces during classical psychedelic dosing; magnitude of alpha suppression in occipital and parietal electrodes correlates with subjective intensity in MEG (Carhart-Harris, Muthukumaraswamy) [45].
- **Theta increase**: Frontal theta increases during ketamine infusion; magnitude has been tested as a near-real-time response biomarker.
- **Lempel-Ziv (LZ) complexity**: Increased across ketamine, LSD, psilocybin, DMT in MEG and EEG [45]. LZ complexity is one of the most robust state markers in human consciousness research.
- **Aperiodic 1/f slope flattening**: Inverse to LZ complexity and a robust marker of cortical E/I imbalance shift. Aperiodic-slope flattening tracks dose-dependent psychedelic intensity in recent studies and is mathematically related to LZ [46].
- **Spectral entropy and signal diversity**: Generalize the above.

These features are all measurable with consumer-grade EEG hardware (Muse, OpenBCI, Emotiv) at lower fidelity, and with research-grade dry-electrode systems (g.tec, ANT, Cognionics) at higher fidelity. The combination of frontal theta, occipital alpha, broadband LZ complexity, and aperiodic 1/f slope yields a four-feature wearable signature that could plausibly track plasticity-window opening in real time.

---

## 12. Implications for Cytoscope

Cytoscope's design vision (continuous noninvasive monitoring of brain hemodynamics, autonomic state, and neural signal complexity) maps cleanly onto the neuroplastogen-response problem in four ways.

1. **Pre-treatment biotype stratification**: A 30-minute Cytoscope baseline session combining fNIRS hemodynamic dynamics, EEG aperiodic slope, EEG complexity, heart-rate variability, and a brief reward-task probe would yield a multivariate plasticity-readiness score. Patients in the lowest quartile of this score are predicted to be the strongest responders to the plasticity-deficit biotype hypothesis. This is testable in a few-hundred-patient prospective study and would directly address the highest-value gap in the field: who responds.

2. **Real-time peri-dose monitoring**: Aperiodic-slope flattening, alpha suppression, theta gain, and LZ complexity increase together define a "plasticity window open" state. A clinician-facing real-time display would let staff confirm window engagement, identify under-responders early (low LZ delta), and adjust support intensity. Tryp Therapeutics is already pursuing a similar concept with TRP-8803 [47]; a wearable form factor would extend it to outpatient settings.

3. **Post-treatment plasticity-restoration tracking and re-treatment timing**: The critical-period reopening duration varies by drug (Dölen) and presumably by patient. Daily Cytoscope sessions for 2–4 weeks after dosing would track when the window closes, informing re-treatment timing rather than the current calendar-based protocols.

4. **Closed-loop psychedelic-assisted therapy**: A near-term concept: integrate Cytoscope readouts into a clinician dashboard that flags suboptimal window engagement and prompts adjunct psychological or sensory intervention during the dose. A longer-term concept: pair Cytoscope monitoring with low-intensity neuromodulation (focused ultrasound, tACS, photobiomodulation) timed to the plasticity window. This is speculative but converges with Tryp's TRP-8803 program and with recent Stanford TMS-EEG closed-loop work [48].

5. **"Cytoscope + psilocybin clinic" integrated product vision**: The natural commercial pathway, given the COMP005 and COMP006 phase 3 successes and a likely Compass FDA approval in the 2027–2028 window, is to position Cytoscope as the standard-of-care monitoring layer for psilocybin clinics. The bundle is small (sensor, app, cloud service), fits the existing clinic workflow, and addresses the field's central operational problem: high cost per session combined with uncertain response. A monitoring tool that improves response rates by 10–15 percentage points pays for itself within months of the program.

---

## Honest caveats

The replication landscape for psychedelic-assisted therapy is fragile. Functional unblinding inflates self-reported outcomes. Effect sizes from open-label and unblinded RCTs (MAPS MDMA, Mindbloom ketamine, GH Research 5-MeO-DMT) likely overstate true causal effect. The COMP006 25 mg versus 1 mg active-comparator design is the strongest blinded readout in the class and gave a –3.8-point MADRS difference, smaller than the –6.6-point difference reported in COMP005 versus inert placebo. The Lykos MDMA CRL is a structural warning: the FDA will not accept the field's preferred trial designs without methodological tightening. Cytoscope's value proposition partly rests on tightening that methodology: an objective biological response signal that does not depend on patient self-report would substantially reduce the unblinding problem in future trials.

The biotype-response literature also has internal replication problems. Drysdale's four-biotype solution did not replicate at the original sample size in the 2019 Dinga reanalysis. Williams's six-biotype refinement is more recent and not yet independently replicated. BDNF Val66Met effects on ketamine response are modest and inconsistent across cohorts. The "plasticity-deficit biotype" framing in this document is a working hypothesis, not a validated phenotype. The work proposed here is exactly the work needed to test it.

---

## References

[1] Aleksandrova LR, Phillips AG. Neuroplasticity as a convergent mechanism of ketamine and classical psychedelics. *Trends in Pharmacological Sciences*. 2021;42(11):929-942. doi:10.1016/j.tips.2021.08.003

[2] Vargas MV et al. Psychedelics promote neuroplasticity through the activation of intracellular 5-HT2A receptors. *Science*. 2023;379:700-706. doi:10.1126/science.adf0435

[3] Calder AE, Hasler G. Towards an understanding of psychedelic-induced neuroplasticity. *Neuropsychopharmacology*. 2023;48:104-112. doi:10.1038/s41386-022-01389-z

[4] Duman RS, Aghajanian GK. Synaptic dysfunction in depression: potential therapeutic targets. *Science*. 2012;338:68-72. doi:10.1126/science.1222939

[5] Li N et al. mTOR-dependent synapse formation underlies the rapid antidepressant effects of NMDA antagonists. *Science*. 2010;329:959-964. doi:10.1126/science.1190287

[6] Bonnavion P et al. Ketamine rescues anhedonia by cell-type- and input-specific adaptations in the nucleus accumbens. *Neuron*. 2025. doi:10.1016/j.neuron.2025.02.009. https://www.cell.com/neuron/fulltext/S0896-6273(25)00139-4

[7] PCORI / NCT06713616. Comparative effectiveness of esketamine versus IV ketamine for TRD. https://clinicaltrials.gov/study/NCT06713616

[8] Mindbloom Real-World Outcomes Study. 2024. https://www.mindbloom.com/research

[9] Liou YJ et al. Effects of treatment refractoriness and BDNF Val66Met polymorphism on antidepressant response to low-dose ketamine infusion. *European Archives of Psychiatry and Clinical Neuroscience*. 2021. https://pubmed.ncbi.nlm.nih.gov/33959800/

[10] Chen MH et al. BDNF Val66Met and CYP2B6 polymorphisms as predictors for ketamine effectiveness in patients with TRD. 2024. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11010549/

[11] Salloum NC et al. Response to ketamine therapy in anxious and non-anxious major depressive disorder: a meta-analysis. 2025. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12437854/

[12] Dinga R et al. Evaluating the evidence for biotypes of depression: methodological replication and extension of Drysdale et al. (2017). *NeuroImage: Clinical*. 2019;22:101796. doi:10.1016/j.nicl.2019.101796

[13] Tozzi L et al. Personalized brain circuit scores identify clinically distinct biotypes in depression and anxiety. *Nature Medicine*. 2024;30:2076-2087. doi:10.1038/s41591-024-03057-9

[14] Abdallah CG et al. Functional connectivity between prefrontal cortex and subgenual cingulate predicts antidepressant effects of ketamine. *European Neuropsychopharmacology*. 2019. https://pubmed.ncbi.nlm.nih.gov/30819549/

[15] Sahib AK et al. Functional connectivity between the amygdala and subgenual cingulate gyrus predicts antidepressant effects of ketamine. 2021. https://pmc.ncbi.nlm.nih.gov/articles/PMC8340826/

[16] Evans JW et al. Predicting antidepressant effects of ketamine: the role of the pregenual anterior cingulate cortex as a multimodal neuroimaging biomarker. *Int J Neuropsychopharmacol*. 2022;25(12):1003-1013. doi:10.1093/ijnp/pyac049

[17] Glx/GABA ratio predictor study. 2025. https://www.sciencedirect.com/science/article/abs/pii/S0165032725007505

[18] Freeman MP et al. Sex differences in response to ketamine as a rapidly acting intervention for TRD. *J Psychiatr Res*. 2019. https://pmc.ncbi.nlm.nih.gov/articles/PMC6360121/

[19] Moliner R et al. Psychedelics promote plasticity by directly binding to BDNF receptor TrkB. *Nature Neuroscience*. 2023;26:1032-1041. doi:10.1038/s41593-023-01316-5

[20] Castrén E. Psychedelics bind to TrkB to induce neuroplasticity and antidepressant-like effects. *Nature Neuroscience* (companion). 2023. doi:10.1038/s41593-023-01317-4

[21] Goodwin GM et al. Single-dose psilocybin for a treatment-resistant episode of major depression. *NEJM*. 2022;387:1637-1648. doi:10.1056/NEJMoa2206443

[22] Compass Pathways. COMP006 Phase 3 readout. 2026. https://ir.compasspathways.com/News--Events-/news/news-details/2026/Compass-Pathways-Successfully-Achieves-Primary-Endpoint-in-Second-Phase-3-Trial-Evaluating-COMP360-Psilocybin-for-Treatment-Resistant-Depression/default.aspx

[23] Bogenschutz MP et al. Percentage of heavy drinking days following psilocybin-assisted psychotherapy vs placebo in AUD: a randomized clinical trial. *JAMA Psychiatry*. 2022;79(10):953-962. doi:10.1001/jamapsychiatry.2022.2096

[24] Peck SK et al. Psilocybin therapy for females with anorexia nervosa: a phase 1, open-label feasibility study. *Nature Medicine*. 2023;29:1947-1953. doi:10.1038/s41591-023-02455-9

[25] Johnson MW et al. Psilocybin or nicotine patch for smoking cessation: a pilot randomized clinical trial. 2026. https://pubmed.ncbi.nlm.nih.gov/41805956/

[26] Carhart-Harris RL, Friston KJ. REBUS and the anarchic brain: toward a unified model of the brain action of psychedelics. *Pharmacological Reviews*. 2019;71:316-344. doi:10.1124/pr.118.017160

[27] MacLean KA, Johnson MW, Griffiths RR. Mystical experiences occasioned by the hallucinogen psilocybin lead to increases in the personality domain of openness. *J Psychopharmacol*. 2011;25(11):1453-1461. doi:10.1177/0269881111420188

[28] Molla H et al. Effects of psychoplastogens on blood levels of BDNF in humans: a systematic review and meta-analysis. *Molecular Psychiatry*. 2024. doi:10.1038/s41380-024-02830-z

[29] Muthukumaraswamy SD et al. Blinding and expectancy confounds in psychedelic randomized controlled trials. *Expert Rev Clin Pharmacol*. 2021;14(9):1133-1152. doi:10.1080/17512433.2021.1933434

[30] Nardou R et al. Oxytocin-dependent reopening of a social reward learning critical period with MDMA. *Nature*. 2019;569:116-120. doi:10.1038/s41586-019-1075-9

[31] Nardou R et al. Psychedelics reopen the social reward learning critical period. *Nature*. 2023;618:790-798. doi:10.1038/s41586-023-06204-3

[32] Mitchell JM et al. MDMA-assisted therapy for severe PTSD: a randomized, double-blind, placebo-controlled phase 3 study. *Nature Medicine*. 2021;27:1025-1033. doi:10.1038/s41591-021-01336-3

[33] Mitchell JM et al. MDMA-assisted therapy for moderate to severe PTSD: a randomized, placebo-controlled phase 3 trial. *Nature Medicine*. 2023;29:2473-2480. doi:10.1038/s41591-023-02565-4

[34] FDA Complete Response Letter to Lykos Therapeutics. Released September 2025. https://psychedelicalpha.com/news/breaking-fda-publishes-lykos-therapeutics-mdma-complete-response-letter-crl

[35] MAPS statement on FDA CRL public release. September 2025. https://maps.org/2025/09/04/fda-public-release-of-crl/

[36] Cameron LP et al. A non-hallucinogenic psychedelic analogue with therapeutic potential. *Nature*. 2021;589:474-479. doi:10.1038/s41586-020-3008-z

[37] Cherian KN et al. Magnesium-ibogaine therapy in veterans with traumatic brain injuries. *Nature Medicine*. 2024;30:373-381. doi:10.1038/s41591-023-02705-w

[38] Brunt TM et al. Ibogaine and cardiovascular complications: prolonged QT interval and ventricular arrhythmias. *Addiction*. 2026. doi:10.1111/add.70319

[39] GH Research. GH001 Phase 2b TRD topline results. February 2025. https://investor.ghres.com/news-releases/news-release-details/gh-research-announces-primary-endpoint-met-phase-2b-trial-gh001/

[40] MindMed (Definium Therapeutics). MM120 Phase 2b GAD JAMA publication. September 2025. https://ir.definiumtx.com/news-events/press-releases/detail/192/

[41] Palhano-Fontes F et al. Rapid antidepressant effects of the psychedelic ayahuasca in TRD: a randomized placebo-controlled trial. *Psychological Medicine*. 2019;49(4):655-663. doi:10.1017/S0033291718001356

[42] Small Pharma / Cybin. SPL026 IV DMT Phase 2a results. 2024. https://www.imperial.ac.uk/news/articles/2026/ayahuasca-compound-has-significant-and-lasting-effect-on-depression-/

[43] The psychoplastogen tabernanthalog induces neuroplasticity without proximate immediate early gene activation. *Nature Neuroscience*. 2025. doi:10.1038/s41593-025-02021-1

[44] Delix Therapeutics. DLX-001 phase 1 initiation. 2023-2026. https://www.delixtherapeutics.com/news/delix-therapeutics-initiates-phase-i-trial-for-novel-compound-dlx-001/

[45] Schartner M et al. Increased spontaneous MEG signal diversity for psychoactive doses of ketamine, LSD and psilocybin. *Scientific Reports*. 2017;7:46421. doi:10.1038/srep46421

[46] Mediano PAM et al. Spectrally and temporally resolved estimation of neural signal diversity. *eLife*. 2024. https://elifesciences.org/reviewed-preprints/88683v1

[47] Tryp Therapeutics / TRP-8803 EEG biomarker collaboration. 2024. https://www.proactiveinvestors.com/companies/news/1077064/

[48] Zrenner C et al. Real-time TMS-EEG for brain state-controlled research and precision treatment. 2024. https://pmc.ncbi.nlm.nih.gov/articles/PMC11528152/

---

*Compiled May 25, 2026 for Cytognosis Foundation NSF X-Labs Phase 0 and ARPA-H PHO proposal development.*
