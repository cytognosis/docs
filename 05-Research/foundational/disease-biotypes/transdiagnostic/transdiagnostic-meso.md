# Transdiagnostic MESO-scale synthesis: connectomic nodes and edges across 14 psychiatric disorders

Prepared for Cytognosis Foundation. This document synthesizes the MESO (connectomic: fMRI, EEG, MEG, structural) sections of the 14 per-disorder biotype docs (schizophrenia, bipolar disorder, major depression, PTSD, anxiety, ASD, ADHD, OCD, Tourette, anorexia nervosa, and the four substance use disorders: alcohol, opioid, nicotine, cannabis). All regions are named in Allen Human Reference Atlas 3D (2020, 141 anatomical regions) terms, with functional labels in parentheses. The goal is to identify the most reproducible NODES (regions) and EDGES (connections) that recur across disorders, tag direction (hyper / hypo / atrophy), and flag where the evidence is fragile. This directly feeds a downstream brain-map visual; the machine-readable `VISUAL_DATA` block at the end is the load-bearing output.

Date: May 25, 2026. Style notes: confidence ratings (HIGH multi-cohort replication, MEDIUM single-consortium or moderate effect, LOW single-lab or failed external replication) appear throughout; replication failures are flagged explicitly.

---

## 1. Framing: nodes vs edges, and why edges are the actionable biomarkers

A connectome has two kinds of object. A NODE is a brain region with an observed change (it gets thinner, hyperactive, atrophies, loses cells). An EDGE is the functional or structural relationship between two regions (their activity correlates, anticorrelates, or couples through a tract). The 14 disorders share a striking property: at the node level they overlap heavily and unhelpfully (almost every disorder thins or perturbs prefrontal cortex, insula, and striatum), whereas at the edge level the disorders separate more cleanly and, crucially, the edges map onto actual interventions.

The canonical example is the dorsolateral prefrontal cortex versus subgenual anterior cingulate (dlPFC-sgACC) anticorrelation in depression. The region "sgACC is hyperactive" is a weak, nonspecific node fact. The edge fact, that dlPFC and sgACC are normally anticorrelated and that a stronger baseline anticorrelation predicts better TMS response, is what powers Stanford SAINT/SNT: the protocol targets the individual dlPFC voxel most anticorrelated with the sgACC, and reported 79% remission in treatment-resistant depression (Cole 2022). The actionable biomarker is the edge sign, not the node. The same logic recurs across the set: the amygdala-vmPFC threat-regulation edge (anxiety, PTSD), the OFC-caudate cortico-striato-thalamo-cortical (CSTC) loop (OCD, Tourette), the NAc-prefrontal fronto-striatal edge (all four SUDs plus ADHD), the thalamus-sensorimotor vs thalamus-prefrontal reciprocal pattern (schizophrenia), and the default-mode internal edge (depression, PTSD, ASD, ADHD).

The Allen Human Reference Atlas 3D (2020) is the reference frame because it spans the whole MRI brain at a resolution that wearable and adaptive-headset sensing can plausibly target. The persistent tension across the set is that most published findings are reported for FUNCTIONAL regions and networks (dlPFC, sgACC, default mode network, salience network) that are not 1:1 with Allen ANATOMICAL parcels. Each functional region is therefore mapped to its containing Allen anatomical structure with the functional label in parentheses (for example, "cingulate gyrus, subgenual part (sgACC / BA25)"). Section 6 audits where this mapping is clean and where it required approximation or a sub-parcel addition below the Allen 141-region resolution.

---

## 2. NODES master table

Rows are the recurring Allen regions. The disorder columns use abbreviations: SCZ (schizophrenia), BD (bipolar), MDD (depression), PTSD, ANX (anxiety), ASD, ADHD, OCD, TS (Tourette), AN (anorexia), and the four SUDs: ALC, OPI, NIC, CAN. Direction is hyper (overactive/hyperconnected), hypo (underactive/hypoconnected), atrophy (volume/thickness loss), or mixed/state-dependent. "Reproducibility" reflects cross-disorder AND within-disorder replication strength.

| Allen region (functional label) | Disorders implicating it (direction) | Dominant direction | Reproducibility |
|---|---|---|---|
| Middle / superior frontal gyrus (dorsolateral prefrontal cortex, dlPFC / BA9, BA46) | SCZ (hypo/thinning), BD (hypo), MDD (hypo), PTSD (I-down cellular), ANX (right hyper), ADHD (hypo), OCD (mixed), AN (hyper over-control), ALC/OPI/NIC/CAN (hypo control) | hypo (executive-control failure; ANX/AN invert to hyper) | HIGH |
| Cingulate gyrus, subgenual part (sgACC / BA25) | MDD (hyper), BD (mixed), ANX (hypo-recruitment), PTSD (hypoactivation) | hyper in MDD; hypo-recruitment elsewhere | HIGH (MDD); MEDIUM (others) |
| Cingulate gyrus, anterior part, dorsal (dACC / midcingulate, BA24/32) | SCZ (glutamate-high), MDD (mixed), PTSD (hyper threat), ANX (hyper), OCD (hyper, ERN), TS (mixed), AN (hyper), ALC/NIC/CAN (hyper salience), ADHD (hypo) | hyper (salience / error monitoring); ADHD inverts | HIGH |
| Frontal lobe, orbital / medial orbital (vmPFC) | BD (hypo regulation), MDD (thinning), PTSD (hypo), ANX (hypo), ADHD (altered reward), ALC/OPI/NIC/CAN (cue-reactive / hypo control), AN (altered valuation) | hypo top-down regulation | HIGH |
| Frontal lobe, orbital part (orbitofrontal cortex, OFC / BA11, BA47) | OCD (hyper, provocation), TS (OCD-overlap), AN (altered valuation), ALC/OPI/NIC/CAN (hypometabolism + cue hyper), ADHD (altered reward) | mixed (hyper on provocation/cue; hypometabolic at rest) | HIGH (SUDs/OCD) |
| Insula, anterior part (anterior insula / salience-interoception) | SCZ (thinning), BD (hypo), MDD (thinning), PTSD (hyper; dissociative hypo), ANX (hyper), ASD (reduced coupling), AN (altered interoception), ALC/OPI/NIC/CAN (hyper craving) | hyper (craving / interoceptive vigilance) | HIGH |
| Amygdala (basolateral + centromedial) | BD (hyper), MDD (altered), PTSD (hyper; dissociative hypo), ANX (hyper), ASD (hypo social), ADHD (atrophy), AN (hypo), ALC/OPI/NIC (hyper stress/withdrawal), CAN (hyper threat) | hyper threat-reactivity (ASD/AN/dissociative-PTSD invert to hypo) | HIGH (anxiety/PTSD); MEDIUM (others) |
| Hippocampal formation, anterior (CA1 / CA3 / dentate) | SCZ (hyper CA1), BD (atrophy), MDD (atrophy), PTSD (atrophy), ADHD (atrophy), ALC (atrophy), CAN (atrophy, inconsistent) | atrophy (SCZ inverts to CA1 hyperactivity) | HIGH (volume); MEDIUM (function) |
| Striatum, ventral / nucleus accumbens (ventral striatum, reward) | SCZ (DA-driven), BD (hyper mania/blunted depression), MDD (hypo reward), PTSD (low reward, weak), ADHD (atrophy, largest subcortical), AN (hypo), ALC/OPI/NIC/CAN (cue-hyper / non-drug-reward blunted), OCD (DBS node) | mixed: cue-hyper but blunted to natural reward; ADHD atrophy | HIGH (SUDs); MEDIUM (others) |
| Caudate nucleus (dorsal / associative striatum) | SCZ (DA-high associative), OCD (hyper, head of caudate), TS (atrophy, most consistent), ADHD (atrophy + hypo), AN (hyper control coupling), ALC (habit shift) | mixed (hyper OCD; atrophy TS/ADHD) | HIGH (OCD/TS/ADHD) |
| Putamen (sensorimotor / dorsal striatum) | SCZ (enlarged subset), OCD (structural), TS (interneuron loss, sensorimotor), ADHD (atrophy), ALC (habit shift) | mixed | MEDIUM-HIGH |
| Thalamus, mediodorsal nucleus (mediodorsal thalamus) | SCZ (dysconnectivity), OCD (hyper, CSTC closure), TS (CM-Pf DBS target), ALC (atrophy, Korsakoff), OPI (altered connectivity) | mixed (hyper OCD; dysconnective SCZ) | HIGH (SCZ/OCD) |
| Superior temporal gyrus incl. transverse temporal gyrus (Heschl's / primary auditory cortex, BA41-42) | SCZ (thinning + ASSR loss), ASD (ASSR loss, left) | hypo (40Hz ASSR reduction) | HIGH |
| Superior temporal sulcus (STS, social-brain hub) | ASD (hypo to faces / biological motion) | hypo | HIGH (ASD) |
| Fusiform gyrus (fusiform face area, FFA) | ASD (hypo to faces) | hypo | HIGH (ASD) |
| Inferior frontal gyrus, pars opercularis (IFG; response inhibition / Broca / mirror) | SCZ (language-AVH), ASD (hypo mirror), ADHD (hypo right IFG, inhibition hub), PTSD (reduced inhibition, weak) | hypo (inhibition) | HIGH (ADHD); MEDIUM (others) |
| Posterior cingulate cortex / precuneus (posterior DMN hub) | SCZ (hyper DMN), MDD (hyper rumination), PTSD (reduced within-DMN), ASD (hypo intrinsic), ADHD (failure to deactivate), ALC/OPI/NIC/CAN (DMN-salience switching) | mixed (hyper MDD/SCZ; hypo PTSD/ASD) | MEDIUM-HIGH |
| Inferior parietal lobule / angular gyrus (temporoparietal junction, TPJ / VAN / DMN posterior) | PTSD (reduced VAN), ASD (atypical mentalizing), ADHD (hypo attention), AN (hypo body-image) | hypo | MEDIUM |
| Bed nucleus of stria terminalis (BNST / extended amygdala) | ANX (hyper sustained threat), PTSD (DBS target), ALC/OPI (stress/withdrawal CRF tone) | hyper (sustained/uncertain threat) | MEDIUM |
| Cerebellum, posterior lobe (Crus I/II) and vermis | SCZ (atrophy, negative symptoms), PTSD (atrophy), ASD (atrophy Crus I/II), ADHD (vermis atrophy), ALC (atrophy, alcohol-distinctive), CAN (altered, high CB1) | atrophy / hypoconnection | MEDIUM-HIGH |
| Locus coeruleus (pons; noradrenergic source) | PTSD (NE hyperdrive), OPI (withdrawal NE surge), ASD (tonic upregulation) | hyper | MEDIUM (HIGH mechanism, sparse human imaging) |
| Hypothalamus (homeostatic) | AN (altered appetite/leptin-ghrelin) | altered | MEDIUM |
| Epithalamus, medial habenula (sub-parcel) | NIC (aversion/withdrawal) | hyper (withdrawal) | MEDIUM (rodent) |
| Precentral / postcentral gyrus (sensorimotor cortex) | SCZ (thalamus-coupled hyper), TS (M1 reduced inhibition), ASD (reduced GABA+), OCD (thalamus-sensorimotor hyper) | mixed (reduced inhibition) | MEDIUM-HIGH |
| Supplementary motor area / pre-SMA (medial superior frontal gyrus) | TS (hyper, low GABA, urge), PTSD (reduced inhibition, weak) | hyper (TS) | HIGH (TS urge-GABA) |
| Periaqueductal gray (midbrain) | OPI (descending pain / withdrawal hyperalgesia) | altered | MEDIUM |

---

## 3. EDGES master table

Edges are the heart of the actionable biomarker story. "Normal sign" is the healthy resting association; "disorder perturbation" is how it shifts. Association signs follow the convention: positive, negative (anticorrelation), or mixed.

| Edge (Region A -- Region B, functional labels) | Normal sign | Disorder perturbation | Disorders | Reproducibility |
|---|---|---|---|---|
| dlPFC (middle frontal gyrus) -- sgACC (cingulate subgenual) | negative (anticorrelation) | Stronger baseline anticorrelation predicts better TMS response; the SAINT/SNT targeting biomarker | MDD (anchor); BD (extrapolated) | HIGH |
| Amygdala -- vmPFC (orbital/medial frontal) | negative (anticorrelation: vmPFC inhibits amygdala) | Weakened/failed top-down regulation; bottom-up threat drive. Inverts to positive (overmodulation) in dissociative PTSD | ANX, PTSD, BD, MDD; (ALC withdrawal) | HIGH |
| OFC (orbital frontal) -- caudate (head) | positive (cortico-striatal drive) | Hyperactive/hypermetabolic on provocation and FDG-PET; normalizes with treatment. NOTE: NOT reproduced as resting hyperconnectivity in ENIGMA-OCD (Bruin 2023) | OCD (anchor), TS (motor-CSTC variant) | MEDIUM-HIGH (provocation/metabolic); LOW (resting) |
| Caudate/putamen -- globus pallidus -- mediodorsal thalamus (CSTC loop closure) | positive (loop) | Reduced striatal braking releases thalamocortical drive; disinhibition model | OCD, TS | MEDIUM (model + FDG-PET) |
| Ventral striatum / NAc -- OFC / vmPFC (reward circuit) | positive (valuation-reward) | Increased cue-driven coupling; blunted to non-drug/natural reward | ALC, OPI, NIC, CAN, ADHD, AN, MDD | HIGH (SUDs); MEDIUM (others) |
| dlPFC / IFG (frontal control) -- striatum (caudate/putamen): fronto-striatal control loop | positive when cooperative; top-down inhibitory in SUD framing | Reduced/weakened fronto-striatal control; the core ADHD and SUD circuit deficit | ADHD (anchor), ALC, OPI, NIC, CAN; AN (excessive, inverted) | HIGH |
| PCC / precuneus -- medial PFC (DMN internal core) | positive | DMN hyperconnectivity (rumination/self-reference); reduced in PTSD and ASD long-range | MDD, SCZ (hyper); PTSD, ASD (hypo) | MEDIUM-HIGH |
| DMN (PCC/precuneus-mPFC) -- task-positive / salience network | negative (anticorrelation; network switching) | Anticorrelation reduced or failing; DMN intrudes during tasks | ADHD (default-mode interference), ALC, OPI, NIC, CAN, ANX | MEDIUM-HIGH |
| Thalamus (mediodorsal/whole) -- postcentral/precentral gyrus (sensorimotor cortex) | positive | Hyperconnectivity; magnitude predicts symptom severity and CHR conversion. Shared with OCD thalamus-sensorimotor hyper | SCZ (anchor), OCD | HIGH (SCZ); MEDIUM (OCD) |
| Thalamus -- middle/superior frontal gyrus (prefrontal cortex) | positive (normally) | Hypoconnectivity (thalamo-prefrontal under-coupling); reciprocal to sensorimotor hyper | SCZ | HIGH |
| Anterior insula -- dorsal ACC (salience network) | positive | Salience-network hyperconnectivity; vigilance/craving readiness; moderates deep-TMS cessation response | ANX, NIC, ALC, OPI; (SUDs broadly) | HIGH (anxiety/nicotine) |
| Anterior insula -- ventral striatum / OFC (insula-craving circuit) | positive | Increased insula-reward coupling during cue-induced craving; insula lesion abolishes the urge to smoke | NIC (anchor), ALC, OPI; CAN (weak) | HIGH (nicotine/alcohol) |
| STS -- fusiform (FFA) / amygdala (social-brain effective connectivity) | positive (normal) | Reduced STS modulatory input to FFA/amygdala; social-brain undercoupling | ASD | MEDIUM-HIGH |
| Anterior hippocampus (CA1/subiculum) -- caudate/putamen (associative striatum) | positive | Hippocampal disinhibition drives striatal dopamine (subiculum-accumbens-pallidum-VTA, Grace loop) | SCZ | HIGH (mechanism); MEDIUM (human edge) |
| Amygdala / extended amygdala -- vmPFC / BNST (stress circuit) | negative (anticorrelation; vmPFC dampens stress) | Weakened top-down regulation; increased amygdala-BNST stress reactivity in withdrawal/negative-affect | ALC, OPI; PTSD; ANX | MEDIUM-HIGH |
| SMA/pre-SMA -- sensorimotor striatum (urge-generation/tic-release) | positive | SMA hyperactivity precedes tics; low SMA GABA tracks premonitory urge | TS | MEDIUM-HIGH |
| Cerebellum (Crus I/II, vermis) -- prefrontal / neocortex (cerebro-cerebellar) | positive (normal) | Reduced supramodal coupling; cerebello-prefrontal hypoconnectivity (negative symptoms); shifted sensorimotor coupling | SCZ, ASD, ADHD (fronto-cerebellar timing) | MEDIUM |
| Locus coeruleus -- cortex/limbic (NE projection) | positive (arousal) | Surge of LC-NE output drives withdrawal autonomic storm; alpha-2 agonists suppress | OPI; PTSD (NE drive) | HIGH (mechanism); MEDIUM (human connectivity) |
| Amygdala -- precuneus / posterior insula (dissociative coupling) | weak / mixed | Increased coupling (depersonalization, derealization) | PTSD (dissociative subtype) | MEDIUM |

---

## 4. Most reproducible regions (ranked)

Ranked by cross-disorder recurrence weighted by within-disorder replication strength. Each region carries a single summary direction (the modal direction across disorders) and the implicating disorders. This list is the key output for the visual; the machine-readable version is in `VISUAL_DATA`.

1. **Anterior insula** (Allen: insula, anterior part; salience/interoception). Direction: hyper. Disorders: SCZ, BD, MDD, PTSD, ANX, ASD, AN, ALC, OPI, NIC, CAN (11 of 14). The most broadly transdiagnostic node; central to craving (all SUDs), interoceptive threat (anxiety/PTSD), and salience. Reproducibility HIGH.

2. **vmPFC** (Allen: frontal lobe, orbital/medial orbital gyri; ventromedial prefrontal cortex). Direction: hypo (top-down regulation). Disorders: BD, MDD, PTSD, ANX, ADHD, AN, ALC, OPI, NIC, CAN (10). The regulatory failure node opposite amygdala and striatum. Reproducibility HIGH.

3. **dlPFC** (Allen: middle/superior frontal gyrus; BA9/46). Direction: hypo (executive control; ANX/AN invert to hyper). Disorders: SCZ, BD, MDD, PTSD, ANX, ADHD, OCD, AN, ALC, OPI, NIC, CAN (12). Most universal node but nonspecific; its VALUE is as the SAINT/SNT TMS target via its edge to sgACC. Reproducibility HIGH.

4. **Dorsal ACC** (Allen: cingulate gyrus, anterior part, dorsal; midcingulate, BA24/32). Direction: hyper (salience/error). Disorders: SCZ, MDD, PTSD, ANX, OCD, TS, AN, ALC, NIC, CAN (10; ADHD inverts to hypo). Substrate of the error-related negativity (ERN). Reproducibility HIGH.

5. **Amygdala** (Allen: amygdala). Direction: hyper threat-reactivity (ASD/AN/dissociative-PTSD invert to hypo). Disorders: BD, MDD, PTSD, ANX, ASD, ADHD, AN, ALC, OPI, NIC, CAN (11). The threat node; its edge to vmPFC is the actionable biomarker. Reproducibility HIGH (anxiety/PTSD).

6. **Ventral striatum / NAc** (Allen: striatum, ventral part / accumbens; reward). Direction: mixed (cue-hyper, natural-reward blunted; ADHD atrophy). Disorders: SCZ, BD, MDD, PTSD, ADHD, OCD, AN, ALC, OPI, NIC, CAN (11). Reward/incentive hub; RewP source. Reproducibility HIGH (SUDs).

7. **OFC** (Allen: frontal lobe, orbital part; BA11/47). Direction: mixed (hyper on cue/provocation, hypometabolic at rest). Disorders: OCD, TS, AN, ADHD, ALC, OPI, NIC, CAN (8). Valuation node; the OCD CSTC entry point. Reproducibility HIGH (SUDs/OCD).

8. **Anterior hippocampus** (Allen: hippocampal formation; CA1/CA3/dentate). Direction: atrophy (SCZ inverts to CA1 hyperactivity). Disorders: SCZ, BD, MDD, PTSD, ADHD, ALC, CAN (7). Reproducibility HIGH (volume).

9. **Caudate** (Allen: caudate nucleus; associative/dorsal striatum). Direction: mixed (hyper OCD; atrophy TS/ADHD). Disorders: SCZ, OCD, TS, ADHD, AN, ALC (6). CSTC and fronto-striatal node. Reproducibility HIGH (OCD/TS/ADHD).

10. **Mediodorsal thalamus** (Allen: thalamus, mediodorsal nucleus). Direction: mixed (dysconnective SCZ; hyper OCD). Disorders: SCZ, OCD, TS, ALC, OPI (5). The thalamocortical hub. Reproducibility HIGH (SCZ/OCD).

11. **Posterior cingulate / precuneus** (Allen: posterior cingulate cortex / precuneus; DMN hub). Direction: mixed (hyper MDD/SCZ; hypo PTSD/ASD). Disorders: SCZ, MDD, PTSD, ASD, ADHD, ALC, OPI, NIC, CAN (9). DMN core; P300/P3b source. Reproducibility MEDIUM-HIGH.

12. **Cerebellum Crus I/II + vermis** (Allen: cerebellar hemisphere, posterior lobe; finer lobular labels are non-Allen). Direction: atrophy/hypoconnection. Disorders: SCZ, PTSD, ASD, ADHD, ALC, CAN (6). Reproducibility MEDIUM-HIGH.

13. **Superior temporal / transverse temporal gyrus** (Allen: superior temporal gyrus incl. Heschl's; auditory cortex). Direction: hypo (40Hz ASSR reduction). Disorders: SCZ, ASD (2, but the strongest shared EEG/MEG node). Reproducibility HIGH.

14. **sgACC** (Allen: cingulate gyrus, subgenual part; BA25). Direction: hyper (MDD). Disorders: MDD, BD, ANX, PTSD (4). The DBS/TMS anchor. Reproducibility HIGH (MDD).

---

## 5. Most reproducible edges (ranked)

Ranked by cross-disorder recurrence and intervention-relevance. Tagged positive / negative / mixed. Machine-readable version in `VISUAL_DATA`.

1. **NAc / ventral striatum -- OFC / vmPFC (reward circuit).** Sign: positive (cue-driven increase, natural-reward blunting). Disorders: ALC, OPI, NIC, CAN, ADHD, AN, MDD. The most cross-disorder edge; the substance-use through-line. Reproducibility HIGH.

2. **dlPFC / IFG -- striatum (fronto-striatal control loop).** Sign: positive/top-down inhibitory, perturbed to reduced. Disorders: ADHD, ALC, OPI, NIC, CAN, AN. The control-deficit edge. Reproducibility HIGH.

3. **Amygdala -- vmPFC (threat-regulation).** Sign: negative (anticorrelation) normally; weakened in disorder, inverted to positive in dissociative PTSD. Disorders: ANX, PTSD, BD, MDD, ALC. Reproducibility HIGH.

4. **dlPFC -- sgACC (depression TMS biomarker).** Sign: negative (anticorrelation). Disorders: MDD (anchor), BD. The single most validated actionable connectomic biomarker (SAINT/SNT). Reproducibility HIGH.

5. **DMN internal: PCC/precuneus -- mPFC.** Sign: positive. Disorders: MDD (hyper), SCZ (hyper), PTSD (hypo), ASD (hypo long-range). Reproducibility MEDIUM-HIGH.

6. **DMN -- salience/task-positive network (anticorrelation switching).** Sign: negative (anticorrelation), perturbed to reduced/failing. Disorders: ADHD, ALC, OPI, NIC, CAN, ANX. Default-mode interference + craving-relapse switching. Reproducibility MEDIUM-HIGH.

7. **Anterior insula -- dACC (salience network).** Sign: positive. Disorders: ANX, NIC, ALC, OPI. Vigilance/craving and a deep-TMS response moderator. Reproducibility HIGH.

8. **OFC -- caudate (CSTC loop).** Sign: positive. Disorders: OCD (anchor), TS. NOTE: robust on symptom-provocation/FDG-PET but NOT reproduced as resting-state hyperconnectivity in ENIGMA-OCD (Bruin 2023). Reproducibility MEDIUM-HIGH (task/metabolic); LOW (resting).

9. **Thalamus -- sensorimotor cortex (positive) reciprocal with thalamus -- prefrontal (hypo).** Sign: mixed (sensorimotor positive/hyper; prefrontal hypo). Disorders: SCZ (anchor), OCD (sensorimotor variant). Reproducibility HIGH (SCZ).

10. **STS -- FFA -- amygdala (social brain).** Sign: positive (normal), reduced. Disorders: ASD. The autism-specific social-brain edge. Reproducibility MEDIUM-HIGH.

---

## 6. Allen-atlas coverage note

Functional regions that map CLEANLY to single Allen anatomical parcels: dlPFC (middle/superior frontal gyrus), sgACC (cingulate gyrus, subgenual part), dACC (cingulate gyrus, anterior part), vmPFC and OFC (orbital and medial orbital gyri), anterior insula (insula, anterior part), amygdala, hippocampal formation, ventral striatum/NAc (striatum, ventral part), caudate, putamen, mediodorsal thalamus (thalamus, mediodorsal nucleus), superior temporal and transverse temporal gyrus (auditory cortex), inferior frontal gyrus, posterior cingulate and precuneus, hypothalamus, and corpus callosum. These need no supplementation.

Functional regions that required APPROXIMATION (functional region is finer than, or distributed across, the Allen parcel):
- **DMN, salience network, ventral attention network, frontoparietal control** are functional networks, not single parcels. Each is anchored to representative Allen regions (DMN to PCC/precuneus + medial PFC + angular gyrus; salience to anterior insula + dACC; VAN to right anterior insula + dACC + anterior MFG + supramarginal gyrus).
- **TPJ** is mapped to the inferior parietal lobule / angular gyrus (supramarginal for the VAN variant).
- **FFA** is mapped to the fusiform gyrus; it is a functional patch within that parcel.
- **STS** is treated as the superior temporal sulcus running within/between superior and middle temporal gyri.
- **dlPFC TMS subvoxel targeting** (SAINT/SNT) operates at a within-region functional coordinate finer than the Allen parcel; treated as a within-region coordinate.

Regions FLAGGED as sub-parcel or NOT cleanly resolved in the Allen 141-region set:
- **Cerebellar Crus I/II and lobules VI/VII** are finer than the Allen single "cerebellum / cerebellar hemisphere" parcels (flagged in ASD and ADHD docs as non-Allen finer lobular labels).
- **Medial habenula (MHb) and interpeduncular nucleus (IPN)** (nicotine) are below Allen 141-region resolution; flagged as sub-parcel additions.
- **Locus coeruleus** is a small pontine nucleus; present as a structure but at the edge of in-vivo human imaging resolution.
- **BNST / sublenticular extended amygdala** exists in the Allen scheme but at sub-millimeter functional resolution; human cohorts are small.
- **Periaqueductal gray, CM-Pf thalamic complex, VTA, substantia nigra** are small midbrain/thalamic structures named as functional subregions within larger Allen parcels.

No finding required importing a region that is genuinely absent from a whole-brain atlas; all additions are sub-parcel resolution issues, not missing structures.

---

## 7. EEG/MEG signatures localized to these nodes

EEG and MEG give the temporal and oscillatory readout that localizes to the same nodes, and they are wearable-compatible (notably OPM-MEG for pediatric ASD). The most reproducible signatures and their Allen sources:

- **40Hz auditory steady-state response (ASSR).** Reduced power and phase-locking. Source: transverse temporal gyrus (auditory cortex). Mechanism: parvalbumin/GABA + NMDA microcircuit integrity. Disorders: SCZ (HIGH, g~0.8), ASD (HIGH, left auditory cortex, correlates with language). This is the cleanest shared EEG/MEG node between two disorders.
- **Reward Positivity (RewP / feedback positivity).** Blunted 250-300 ms deflection to reward. Source: ventral striatum / medial PFC (frontocentral). Disorders: MDD (MEDIUM-HIGH, anhedonia marker), AN (blunted feedback-related negativity to reward, LOW-MEDIUM). Localizes to the reward circuit nodes above.
- **Error-related negativity (ERN).** Enhanced amplitude (OCD/anxiety) or context-dependent. Source: dorsal ACC / midcingulate (Fz/FCz). Disorders: OCD (HIGH, g~0.5, present in unaffected relatives, an endophenotype), ANX (HIGH for OCD/GAD-onset). Directly localizes to the dACC node.
- **P300 / P3b (oddball).** Reduced amplitude. Source: precuneus / inferior parietal + frontal. Disorders: SCZ (HIGH, g~0.85, endophenotype), ALC (HIGH, the COGA heritable vulnerability marker present in alcohol-naive relatives), OPI/NIC/CAN (MEDIUM, reduced baseline + enhanced cue-P300), ADHD (MEDIUM, nonspecific). Localizes to the posterior DMN/parietal node.
- **Sleep spindle density (NREM2, 11-16 Hz).** Reduced. Source: thalamus (reticular/mediodorsal) to cortex. Disorders: SCZ (HIGH, present in relatives), ASD (MEDIUM, reduced frontal/central spindles). Localizes to the thalamocortical edge.
- **Aperiodic 1/f slope (E/I proxy).** Flatter (excitatory bias). Source: broadband cortical. Disorders: ASD (HIGH resting, >=5 labs), SCZ (MEDIUM, mixed), ADHD (LOW-MEDIUM). An E/I-balance readout rather than a single node.
- **Reduced short-interval intracortical inhibition (SICI, TMS-EEG).** Source: primary motor cortex (precentral gyrus). Disorder: TS (HIGH; converges with low SMA GABA and striatal interneuron loss). The most coherent neurophysiology story in the set.
- **Resting beta power (elevated).** Source: frontocentral cortex. Disorder: ALC (MEDIUM-HIGH, GABRA2-linked withdrawal hyperexcitability). Anxiety also shows elevated resting beta (LOW effect size).

Flagged EEG/MEG replication failures and low-confidence markers: **theta-beta ratio** in ADHD (LOW; FDA-cleared NEBA basis but failed rigorous multi-site replication and shrinks under multiverse analysis); **frontal alpha asymmetry** in MDD (LOW; small inconsistent effect at group level, not reliable for individual stratification); **mismatch negativity** is robust in SCZ (HIGH, g~1.0) but transdiagnostic and less ASD-specific; **PPI/P50 gating** in ASD is mixed/LOW.

---

## 8. Cross-disorder structure and flagged replication failures

Three super-circuits organize the transdiagnostic picture:

1. **The threat-regulation circuit** (amygdala - vmPFC/sgACC - anterior insula - dACC - BNST). Shared by anxiety, PTSD, MDD, BD, and the negative-affect/withdrawal stage of the SUDs. The amygdala-vmPFC anticorrelation is its actionable edge.
2. **The reward / control circuit** (ventral striatum/NAc - OFC/vmPFC - dlPFC/IFG - dACC, with the DMN-salience switch). Shared by all four SUDs, ADHD, anorexia (inverted to over-control), and the anhedonic pole of depression.
3. **The cortico-striato-thalamo-cortical / motor-control circuit** (OFC or SMA - caudate/putamen - globus pallidus - mediodorsal/CM-Pf thalamus). Shared by OCD, Tourette, and (via thalamocortical dysconnectivity and associative striatum) schizophrenia.

ASD sits partly apart on a **social-brain + cerebellar + thalamocortical-EEG** axis (STS-FFA-amygdala, Crus I/II, 40Hz ASSR), overlapping the others mainly through DMN, insula, and the auditory ASSR shared with schizophrenia.

Explicitly flagged replication failures and tensions (do not over-state these in the visual):
- **Drysdale four-biotype depression clustering (Drysdale 2017) failed external replication (Dinga 2019).** The dlPFC-sgACC anticorrelation edge survives as a robust biomarker; the specific four-cluster labels do not.
- **AURORA acute PTSD fMRI biotypes (Stevens 2021) did not replicate (Ben-Zion 2023).** The ventral-striatum reward and rIFG/preSMA inhibition acute nodes are LOW confidence; the dissociative subtype and amygdala-vmPFC edge remain robust.
- **ENIGMA-OCD resting hypoconnectivity (Bruin 2023) vs task/provocation hyperconnectivity.** The OFC-caudate CSTC hyperconnectivity is robust on symptom provocation and FDG-PET but the large resting-state mega-analysis found predominantly global HYPOconnectivity, reproducing only thalamus-sensorimotor hyper. This modality-dependence is the single most important caveat for the CSTC edge.
- **Cannabis (CUD)** is the least consistent SUD: structural findings (hippocampal volume) replicate poorly; reward-task fMRI splits between blunted and intact. Its most reproducible feature is CB1-density-weighted regional involvement and the DMN-salience switching shared with other SUDs.
- **BD EEG/MEG and many BD node findings are state-dependent** (flip between mania and depression), keeping confidence MEDIUM-LOW for pooled analyses.
- **Prazosin (PTSD, VA CSP #563) was negative on its primary endpoint**, and the **Drysdale dmPFC TMS biotype** lacks replication, both reinforcing that node-level claims need edge-level and treatment-response validation.

---

## VISUAL_DATA

```
REGIONS
anterior insula | bilateral mid-lateral (frontoinsular operculum) | SCZ,BD,MDD,PTSD,ANX,ASD,AN,ALC,OPI,NIC,CAN | hyper | HIGH
vmPFC | medial orbital frontal (ventromedial prefrontal) | BD,MDD,PTSD,ANX,ADHD,AN,ALC,OPI,NIC,CAN | hypo | HIGH
dlPFC | left+right lateral frontal (middle/superior frontal gyrus) | SCZ,BD,MDD,PTSD,ANX,ADHD,OCD,AN,ALC,OPI,NIC,CAN | hypo | HIGH
dorsal ACC | medial frontal/midcingulate (anterior cingulate dorsal) | SCZ,MDD,PTSD,ANX,OCD,TS,AN,ALC,NIC,CAN | hyper | HIGH
amygdala | deep medial temporal | BD,MDD,PTSD,ANX,ASD,ADHD,AN,ALC,OPI,NIC,CAN | hyper | HIGH
ventral striatum NAc | deep basal forebrain (ventral striatum) | SCZ,BD,MDD,PTSD,ADHD,OCD,AN,ALC,OPI,NIC,CAN | mixed | HIGH
OFC | ventral orbital frontal | OCD,TS,AN,ADHD,ALC,OPI,NIC,CAN | mixed | HIGH
anterior hippocampus | deep medial temporal | SCZ,BD,MDD,PTSD,ADHD,ALC,CAN | atrophy | HIGH
caudate | deep central (dorsal striatum head) | SCZ,OCD,TS,ADHD,AN,ALC | mixed | HIGH
mediodorsal thalamus | deep central (thalamus) | SCZ,OCD,TS,ALC,OPI | mixed | HIGH
posterior cingulate precuneus | medial posterior parietal | SCZ,MDD,PTSD,ASD,ADHD,ALC,OPI,NIC,CAN | mixed | MEDIUM-HIGH
putamen | deep central (sensorimotor striatum) | SCZ,OCD,TS,ADHD,ALC | mixed | MEDIUM-HIGH
cerebellum Crus I/II vermis | posterior fossa | SCZ,PTSD,ASD,ADHD,ALC,CAN | atrophy | MEDIUM-HIGH
sgACC | medial subgenual frontal | MDD,BD,ANX,PTSD | hyper | HIGH
inferior frontal gyrus | lateral frontal (pars opercularis) | SCZ,ASD,ADHD,PTSD | hypo | MEDIUM-HIGH
superior/transverse temporal gyrus | lateral superior temporal (auditory cortex) | SCZ,ASD | hypo | HIGH
STS | lateral superior temporal sulcus | ASD | hypo | HIGH
fusiform FFA | ventral temporal | ASD | hypo | HIGH
TPJ angular gyrus | lateral inferior parietal | PTSD,ASD,ADHD,AN | hypo | MEDIUM
BNST | deep basal forebrain (extended amygdala) | ANX,PTSD,ALC,OPI | hyper | MEDIUM
SMA pre-SMA | medial superior frontal | TS,PTSD | hyper | HIGH
sensorimotor cortex | dorsal central (pre/postcentral gyrus) | SCZ,TS,ASD,OCD | mixed | MEDIUM-HIGH
locus coeruleus | dorsal pons (brainstem) | PTSD,OPI,ASD | hyper | MEDIUM
hypothalamus | deep medial diencephalon | AN | mixed | MEDIUM
medial habenula | deep epithalamus (sub-parcel) | NIC | hyper | MEDIUM
periaqueductal gray | dorsal midbrain | OPI | mixed | MEDIUM

EDGES
ventral striatum NAc -- OFC/vmPFC | positive | ALC,OPI,NIC,CAN,ADHD,AN,MDD | HIGH
dlPFC/IFG -- striatum (fronto-striatal control) | positive | ADHD,ALC,OPI,NIC,CAN,AN | HIGH
amygdala -- vmPFC (threat regulation) | negative | ANX,PTSD,BD,MDD,ALC | HIGH
dlPFC -- sgACC (depression TMS target) | negative | MDD,BD | HIGH
PCC/precuneus -- mPFC (DMN internal) | positive | MDD,SCZ,PTSD,ASD | MEDIUM-HIGH
DMN -- salience/task-positive (anticorrelation switch) | negative | ADHD,ALC,OPI,NIC,CAN,ANX | MEDIUM-HIGH
anterior insula -- dorsal ACC (salience) | positive | ANX,NIC,ALC,OPI | HIGH
anterior insula -- ventral striatum/OFC (craving) | positive | NIC,ALC,OPI,CAN | HIGH
OFC -- caudate (CSTC loop) | positive | OCD,TS | MEDIUM-HIGH
caudate/putamen -- pallidum -- mediodorsal thalamus (CSTC closure) | positive | OCD,TS | MEDIUM
thalamus -- sensorimotor cortex | positive | SCZ,OCD | HIGH
thalamus -- prefrontal cortex | negative | SCZ | HIGH
STS -- fusiform FFA/amygdala (social brain) | positive | ASD | MEDIUM-HIGH
anterior hippocampus -- associative striatum (Grace loop) | positive | SCZ | MEDIUM
amygdala/extended amygdala -- vmPFC/BNST (stress) | negative | ALC,OPI,PTSD,ANX | MEDIUM-HIGH
SMA -- sensorimotor striatum (urge/tic) | positive | TS | MEDIUM-HIGH
cerebellum Crus I/II -- prefrontal cortex (cerebro-cerebellar) | positive | SCZ,ASD,ADHD | MEDIUM
locus coeruleus -- cortex/limbic (NE) | positive | OPI,PTSD | MEDIUM
amygdala -- precuneus/posterior insula (dissociative) | mixed | PTSD | MEDIUM
```
