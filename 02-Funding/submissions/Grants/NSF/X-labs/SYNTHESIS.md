# NSF X-Labs Phase 0 — Research Synthesis

> A condensed view of the per-stream research outputs, organized around the five core arguments the 8-page proposal must make. Each section cites the source research files in `research/` and the problem-doc revision in `drafts/problem/`.

---

## 1. The problem framing (what the proposal must convince reviewers of)

Mental disorders are now the world's leading cause of years lived with disability. The 2026 Lancet GBD update reports 1.17 billion people living with a mental disorder, with 171 million DALYs in 2023 (the fifth-leading cause group globally, up from twelfth in 1990). Anxiety DALYs jumped 47% since 2019 alone, an explicit pandemic effect. The April 2026 White House Executive Order on Accelerating Medical Treatments for Serious Mental Illness names this directly: "our medical research system has yet to produce approved therapies that promote enduring improvements" and calls for "innovative methods beyond existing prescription medications." Source: `drafts/problem/Problem_and_Gap_Statement_MentalHealth.md`.

The proposal frames the failure as three structural blindspots, translated from Cytognosis's general three-blindspot framework into mental-health terms:

1. **Detection blindspot** (temporal): psychiatric disorders have no objective biomarker. The biology of prodromal psychosis, depression, and addiction is detectable but clinically invisible. Suicide is the leading cause of death in U.S. adolescents and has no biomarker predictor.
2. **Personalization blindspot** (mechanistic + complexity): STAR*D reports first-line SSRI response of 42–53%. Williams and Tozzi's 2026 iMAP work (Stanford) shows that biotype-matched, ML-personalized intervention doubles depression remission from the standard ~30% to 55% (PHQ-9 <5, Cohen's d = -0.89). The biology supports stratification but the clinic does not operationalize it.
3. **Feedback blindspot** (continuous monitoring): every other field has continuous biological readout (CGM in diabetes, ECG patches in cardiology, ctDNA in oncology); psychiatry has none. Treatment response is measured by clinician-rated scales weeks after start.

These three blindspots are not separate problems. They are one structural failure: the absence of a wearable sensor that maps a person's brain at biotype-relevant resolution, tracks trajectory in real time, and feeds back to personalized intervention.

---

## 2. The wearable SOTA gap (and the fNIRS-class opening)

Source: `research/wearables-comparative.md` and `research/fnirs-deep-dive.md`.

Among fully noninvasive wearable modalities, fNIRS-class diffuse optical methods occupy the only feasible substrate for personalized, scalable brain readout. EEG offers temporal precision but cortical-surface-only signals and severe spatial smearing. OPM-MEG offers a credible spatial-temporal combination but demands magnetic shielding that defeats wearability at population scale (Kernel killed Flux for exactly this reason). Diffuse optical methods, particularly TD-fNIRS, HD-DOT, DCS/SCOS, and broadband NIRS for cytochrome-c-oxidase, reach 3–4 cm into adult cortex with usable signal-to-noise and tolerate motion.

The depth wall is real and unbroken. No commercial system delivers routine subcortical readout from a wearable. The 2025 state of the art (whole-head TD-DOT; UHD-DOT at 6.5 mm channel spacing) extends coverage but not depth. Openwater's TRUE platform (focused ultrasound plus optical phase conjugation, AGPL-licensed in January 2024) is the only deployed attempt at a depth-targeted optical "zoom-in" headset. Hervé Marie-Nelly's stealth program, reaching 2–3 cm depth with single-cell-class spectroscopic readout in vivo, is the closest competitor.

Three architectural gaps remain open and form the technical wedge for the proposal:

- **No platform integrates multi-chromophore readout** (HbO2, HbR, cytochrome-c-oxidase as a mitochondrial marker, water/lipid SWIR channels). Tachtsidis-lab broadband NIRS makes wearable CCO feasible but no vendor ships it.
- **No platform does adaptive, personalized region selection**. Kernel's "Neuroscience as a Service" pivot is data-as-a-service over a fixed optode geometry. There is no closed-loop "zoom" yet.
- **fNIRS has a melanin-equity problem** (Kwasa et al., 2023, *Nat Hum Behav*; 2024 *Neurophotonics* follow-ups). Building melanin handling as a first-class signal differentiates the platform on health-equity grounds.

EROS (event-related optical signal, the putative fast neuronal readout) is honest red-flag territory and should not be a primary technical claim in the proposal.

---

## 3. The targeted-molecular boundary (what we can and cannot promise)

Source: `research/targeted-noninvasive-scanning.md`.

The PET analog of noninvasive optical molecular imaging is, today, essentially proof-of-concept outside HbO2, HbR, and cytochrome-c-oxidase. The thirty-year history of noninvasive optical continuous glucose monitoring (Pendra, Cygnus/GlucoWatch, Know Labs, DiaMonTech) is the most informative real-world precedent: three decades, multiple bankruptcies, best independent MARDs at 11–12%, and no FDA-cleared purely optical CGM. Brain molecular targets are harder by every axis (depth, concentration, intervening bone).

The credible 5–10 year envelope: multi-chromophore hemodynamics plus metabolism (CCO) plus shortwave-infrared water and lipid channels, with cortical-surface protein-aggregate spectral features (amyloid plaques) as a stretch goal. Three live technology bets could push the boundary: SESORS (spatially offset Raman with SERS); transcranial PACT (Wang 2022 photoacoustic computed tomography); Openwater-style ultrasound-aided optical focusing. The proposal should position Cytognosis as complementary to PET, not as PET's replacement. The Phase 0 to Phase 1 to Phase 2 promise is a continuous, wearable, scalable monitor for a credible biomarker set, with engineering headroom for added channels along a 10-year roadmap.

---

## 4. The biotype motivation for "coarse-to-fine zoom"

Sources: `research/biotypes-depression.md`, `research/biotypes-anxiety.md`, `research/biotypes-psychosis.md`, `research/biotypes-ptsd.md`, `research/biotypes-addiction.md`, `research/transdiagnostic-connectomic-synthesis.md`.

The transdiagnostic synthesis identifies eight anchor regions that, taken together, cover the most defensible biotypes across depression, anxiety, psychosis, PTSD, and addiction:

1. **Dorsolateral prefrontal cortex** (cognitive control biotypes across all five disorders; the canonical TMS target)
2. **Dorsal anterior cingulate cortex / dorsomedial PFC** (salience switching, threat monitoring)
3. **Ventromedial PFC and orbitofrontal cortex** (reward valuation, emotion regulation, addiction)
4. **Anterior insula** (interoceptive vigilance in anxiety and addiction craving; salience hub)
5. **Subgenual ACC** (depression and PTSD; indexed via dlPFC anticorrelation per Mayberg and Fox)
6. **Superior temporal / primary auditory cortex** (sensory-hyperresponsive psychosis biotype, B-SNIP Biotype 2)
7. **Posterior cingulate / precuneus** (DMN rumination across MDD and PTSD)
8. **Ventral striatum and amygdala** (reward deficit and threat hyperreactivity; depth-limited, indexed indirectly through cortical effectors)

A tier-2 anchor at the lateral cerebellum extends coverage for psychosis cognitive dysmetria and addiction-related cerebellar atrophy.

The "mental health coordinate" the platform must place each person on sits on five to six latent axes that align with RDoC and HiTOP frameworks: negative affect / threat, reward / anhedonia, cognitive control, salience / interoception, attention / vigilance, sensory gating. These axes are the operational definition of the Cytoverse psychoverse / neuroverse map for the mental-health subdomain. Knowing a person's position on these axes prunes the region-priority list for the zoom-in step: an anxious presentation indexes anterior insula and amygdala-vmPFC; an anhedonic presentation indexes ventral striatum and OFC; a cognitive-deficit psychosis presentation indexes DLPFC, anterior hippocampus, and superior temporal.

The 2026 ARPA-H PHO map work, running in parallel, supplies the multi-scale (genomic to phenotypic) causal model into which the X-Labs sensor's readouts are placed. The connectomic layer is the mediator: genomic axes (purely inherited) plus connectomic axes (exposome plus genetics) allow causal disentanglement of inherited versus environmental contributions to each axis.

---

## 5. The neuromodulation pairing argument

Source: `research/neuromodulation.md`.

Noninvasive neuromodulation is at an inflection point and is missing exactly what Cytognosis would supply. Stanford's SAINT/SNT protocol delivers 79% remission in treatment-resistant depression versus 28% for standard rTMS (Williams, Cole, et al.; n = 29 RCT). The differentiator is target personalization: SAINT uses individualized rsfMRI to identify each person's anti-correlated dlPFC target. The remaining bottleneck for translation is that rsfMRI is offline, expensive, scarce, and not repeatable on a daily basis.

A wearable sensor that can localize the same functional targets in a clinic visit, or that can do so longitudinally and adaptively, removes this bottleneck. Temporal interference stimulation (Wessel and Hummel, 2023, deep striatal modulation in humans), low-intensity focused ultrasound (LIFU; Openwater and others have shown depression effects in early studies), Flow Neuroscience's December 2025 FDA approval for at-home tDCS, and Medtronic Percept BrainSense's February 2025 full adaptive DBS approval all point in the same direction: closed-loop, sensing-paired, personalized noninvasive neuromodulation is the active frontier.

The proposal must frame the Cytognosis platform as the missing sensor layer for this frontier. Section 5 of `research/neuromodulation.md` lays this out in detail.

---

## 6. NSF X-Labs alignment — explicit mapping

Topic 2 (Sensing and Imaging) names five technical areas that the proposed platform addresses directly:

| X-Labs technical area | How the platform addresses it |
|---|---|
| Adaptive AI-based sensing algorithms | Adaptive optode selection and channel weighting driven by the patient's biotype coordinate; foundation-model-trained on multi-cohort optical and neuroimaging data |
| AI-driven computational imaging | Reconstruction of multi-chromophore tomograms and biotype-coordinate inference are fundamentally AI computational imaging problems; the instrument is designed for the model, not retrofitted |
| MRI-free deep-tissue imaging | Multi-chromophore TD-fNIRS plus DCS/SCOS plus ultrasound-aided optical focusing reach cortical and shallow-subcortical targets at a fraction of MRI cost and at scale |
| Instruments engineered for next-generation AI training pipelines | The platform is a longitudinal data engine; every device produces continuous, paired sensor + biotype + outcome data that no static imaging cohort can match |
| Whole-brain activity at cellular resolution across long timescales | Achievable in cortical targets within Phase 1 to Phase 2 timescale; Phase 0 will demonstrate the core technology and biotype-coordinate inference for the anchor regions identified above |

This is a Topic 2 proposal with strong cross-cutting alignment. The 8-page draft must surface this mapping explicitly in Section 1 (Mission) and Section 2 (Technology Landscape).

---

## 7. The Cytognosis platform components in this proposal

For consistency with the science-platform skill terminology:

- **Cytoverse (the Map)**: the AI foundation model that defines the mental-health coordinate space (the psychoverse / neuroverse subdomain). Built in parallel via the ARPA-H PHO effort.
- **Cytoscope (the Sensor)**: the X-Labs deliverable. The adaptive spectroscopy headset that performs coarse-grained whole-cortex sensing, then triangulates the patient's position on the Cytoverse coordinate and zooms in to the biotype-priority anchor regions for high-resolution multi-chromophore readout.
- **Cytonome (the Navigator)**: the on-device causal AI that turns sensor streams into actionable coordinates and, in the closed-loop neuromodulation roadmap, drives personalized stimulation targets.

The X-Labs proposal is centered on Cytoscope but references Cytoverse and Cytonome as the integrated platform context, consistent with the program's "platform technology" framing.

---

## 8. Voice and compliance checklist for the proposal draft

- Strict 8-page limit, 12pt single-spaced, 1-inch margins, 8.5 x 11.
- Five required sections per Attachment A: Mission, Technology Landscape, Outcomes, Senior/Key Personnel Qualifications, Team Capabilities Statement.
- Separate COI PDF, no page limit.
- No em dashes; active voice; no "revolutionary", "cure", "game-changing", "breakthrough".
- Cytognosis terminology: "detect and intercept", "years before symptoms", "AI-native", person-first ("people with depression", not "depressed patients").
- Joint submission: Cytognosis Foundation as lead organization (501(c)(3), nonprofit FRO model satisfies the Autonomy Factor Test); Hervé Marie-Nelly as co-PI from his stealth company under subcontract.
- Bridge line on close: "Cytognosis exists so no one else waits decades for answers."
