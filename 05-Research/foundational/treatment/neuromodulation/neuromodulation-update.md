# Noninvasive Neuromodulation: Resolution, Depth, Node-vs-Edge Targeting, and Sensing-Paired Closed-Loop Systems

Technology deep-dive prepared for the Cytognosis Foundation NSF X-Labs / ARPA-H program.
Compiled 25 May 2026. This document extends the two prior briefs (neuromodulation.md and neuromodulation-response.md) and does not repeat the modality-by-disorder efficacy tables already laid out there. It concentrates on the four engineering axes that the proposal must defend: how focal stimulation can get (spatial resolution), how fast it can adjust (temporal resolution), how deep it reaches noninvasively, and whether it can engage a single circuit node or a network edge or subnetwork. A long dedicated section then covers the state of the art in pairing neuromodulation with a sensing technology in adaptive, interactive closed-loop systems, with an honest accounting of which claims rest on a single study.

---

## 1. Why node-vs-edge is the organizing question

The prior briefs established that the dominant performance lever in noninvasive neuromodulation is target personalization, anchored by the Stanford SAINT/SNT result in which connectivity-guided dorsolateral prefrontal cortex (DLPFC) targeting raised remission to 79 percent in a 29-patient randomized sham-controlled trial (1). That argument is about choosing the right node. The next argument, and the one this deep-dive develops, is that psychiatric and neurological disorders are increasingly understood as disorders of connections between nodes, not of single regions. Depression is a frontolimbic disconnection. Parkinson's disease is a pathological synchronization across the cortico-basal-ganglia-thalamic loop. Schizophrenia is a dysconnection syndrome. If the disease lives on the edges, the therapeutic question becomes whether a given modality can modulate an edge, a directed coupling between two nodes or a coordinated subnetwork, rather than merely depolarizing a single patch of cortex.

The vocabulary is worth making precise. A node is an anatomical region or functional parcel. An edge is a statistical or causal relationship between two nodes, measured as correlation, coherence, phase coupling, or effective (directed) connectivity. A subnetwork is a set of nodes plus the edges among them, for example the default mode network or the salience network. Single-site, fixed-frequency stimulation acts on a node. Engaging an edge requires one of three strategies: stimulating one node and exploiting its known anatomical projections to influence a downstream node through connectivity (network-targeted single-site stimulation), stimulating two or more nodes with a controlled timing or phase relationship (multi-site or dual-site stimulation), or tuning the stimulation frequency and phase to the oscillation that carries communication along a specific edge (oscillation-targeted stimulation). The modality sections below evaluate each technique against this framework.

---

## 2. Transcranial magnetic stimulation (TMS)

### 2.1 Resolution, depth, and what limits them

A figure-of-eight coil induces a suprathreshold electric field over a cortical patch roughly 1 to 3 cm in diameter, with effective penetration to about 1.5 to 2.5 cm (2). The H-coil family (Brainsway H1, H4, H7) trades focality for depth, reaching approximately 3 to 4 cm but stimulating a broader, less defined volume (3). The physics is unforgiving: the induced field falls off steeply with distance from the coil, so any attempt to reach a deeper structure by raising intensity also widens the superficial field and recruits more overlying cortex. No TMS coil reaches subcortical gray matter (amygdala, striatum, subthalamic nucleus) with focal precision. The deepest reliable TMS targets remain cortical.

Temporal resolution is TMS's strength. A single pulse is delivered in under 1 ms, and the physiological perturbation it evokes can be read within tens of milliseconds. Repetitive protocols operate on the timescale of the protocol design: theta-burst stimulation (TBS) delivers 50-Hz triplets repeated at 5 Hz, and intermittent TBS compresses a session into a few minutes (4). This millisecond-scale precision is what makes TMS the natural effector for state-dependent closed-loop systems (Section 8).

### 2.2 Node vs edge: TMS is the most developed for edge targeting

TMS is the noninvasive modality with the richest toolkit for engaging edges, for a simple reason: a TMS pulse delivered to one cortical node propagates trans-synaptically to anatomically connected regions, so the stimulated node is a handle on the whole subnetwork it belongs to. Four distinct techniques exploit this.

Network-targeted single-site TMS. The SAINT logic is already an edge strategy in disguise. The DLPFC is stimulated not for its own sake but because it is the most accessible node anticorrelated with the subgenual anterior cingulate (sgACC), and the therapeutic effect is hypothesized to travel along the DLPFC-sgACC edge (1, 5). The same connectivity-seeded logic now extends to mild cognitive impairment and Alzheimer's disease, where a prefrontal TMS seed map overlaps the salience network and is anticorrelated with the AD-vulnerable posterior cingulate, while a parietal seed engages the default network, so the choice of cortical entry node selects which subnetwork is modulated (6). A 2025 review formalizes this as choosing the surface node that best leverages the target edge (7).

Dual-site TMS. Two coils deliver precisely timed conditioning and test pulses to two connected nodes. The interval between pulses (typically 6 to 20 ms) determines whether the connection is facilitated or suppressed, and the technique directly probes and modulates directed connectivity and spike-timing-dependent plasticity along a specific corticocortical edge (7). This is the cleanest demonstration that noninvasive stimulation can act on an edge as a unit of intervention, not just on a node.

Sequential multi-site TMS. Different targets are stimulated in succession within a session to engage distributed networks, used in depression and Alzheimer's protocols that target two or more network hubs (7).

Multi-locus TMS (mTMS). The Aalto group (Koponen, Ilmoniemi, and colleagues) replaced the single coil with a transducer of up to six independently driven coils, so the induced field's location and orientation can be switched electronically, without moving any hardware, between cortical sites a few millimeters apart and on a millisecond timescale (8). A 2024 electronic-robotic platform and a 2025 pulse-width-modulation extension push the switching into the microsecond regime, enabling true interaction with local cortical networks at millimeter and millisecond scales (9). mTMS is the hardware that makes interactive, within-network sequencing of pulses feasible, and it is the closest noninvasive analog to programming a multi-contact electrode array. It remains a research instrument with no clinical clearance.

The honest caveat: dual-site and mTMS edge modulation are demonstrated mechanistically (motor-evoked potentials, TMS-EEG connectivity) in healthy cortex and small samples. No clinical trial has yet shown that edge-targeted multi-site TMS beats single-node TMS on a psychiatric endpoint.

### 2.3 Regulatory status

TMS is FDA-cleared for major depressive disorder (MDD, 2008), OCD (2018), smoking cessation (2020), anxious depression (2021), adolescent MDD (2024), and accelerated/SAINT-style individualized protocols (Magnus Medical, 2022, commercial launch 2024) (10). Brainsway received clearance for an accelerated protocol and an adolescent indication in 2025. No closed-loop TMS system is FDA-cleared for psychiatry.

### Table 2. TMS at a glance

| Axis | Figure-of-eight rTMS | Deep TMS (H-coil) | Multi-locus TMS (mTMS) |
| --- | --- | --- | --- |
| Spatial resolution | 1 to 3 cm cortical patch | broader, 3 to 5 cm patch | mm-scale electronic switching between adjacent sites |
| Best achieved focality | ~1 cm with neuronavigation | least focal of the three | sub-cm, no coil movement |
| Temporal resolution | <1 ms per pulse; iTBS minutes | <1 ms per pulse | microsecond target switching (PWM, 2025) |
| Depth (noninvasive) | 1.5 to 2.5 cm | 3 to 4 cm | cortical |
| Limit on depth | field falloff with distance | focality cost | cortical only |
| Node vs edge | node, plus connectivity-seeded edge | node/diffuse | edge, programmable multi-site |
| Regulatory | FDA-cleared (multiple psychiatric) | FDA-cleared (MDD, OCD, smoking) | research only |

---

## 3. Transcranial electrical stimulation (tES): tDCS, tACS, tRNS, tTIS

### 3.1 Conventional tES resolution and depth

Conventional tDCS spreads current diffusely across large cortical territories and is best understood as a low-spatial-resolution neuromodulator that biases excitability rather than targeting a focal volume (11). High-definition tDCS (HD-tDCS) with 4x1 ring montages tightens the focus to roughly 1 to 2 cm at the cost of delivered magnitude. Depth is limited to superficial cortex because the field that reaches a deep structure is always smaller than the field delivered to the cortex above it. Temporal resolution for tDCS is poor in the sense that effects build over minutes of stimulation and outlast it; tACS, by contrast, can entrain oscillations on a cycle-by-cycle basis and so carries the temporal precision needed for phase-based edge targeting.

### 3.2 tACS is intrinsically an edge tool

tACS deserves separate treatment because frequency and phase are exactly the variables that define edges in the oscillatory-communication framework. Single-site tACS at an individual's own peak frequency entrains a node, but the more interesting development is dual-site phase-controlled tACS, in which two regions are stimulated at the same frequency with a controlled phase lag to facilitate or disrupt their synchronization, the physical substrate of an edge.

The 2024-2025 literature on this is now substantial. Phase-lagged tACS between executive and default mode network nodes modulates working memory, with 0-degree (in-phase) and 180-degree (anti-phase) lags producing opposite behavioral effects (12). Cross-frequency bifocal tACS (for example alpha to one node, gamma to another) modulates inter-areal coupling between primary visual cortex and area MT in healthy participants and stroke patients in a single session (13). Concurrent tACS-fMRI shows state- and frequency-specific modulation of hippocampal-cortical functional connectivity, demonstrating that the stimulation reaches a measurable network edge rather than only a local node (14). Individual-alpha-frequency tACS reduces static functional connectivity across the default mode network (15). The mechanistic logic, that phase- and frequency-matched stimulation can selectively strengthen or weaken a specific functional coupling, is the cleanest case in noninvasive neuromodulation for direct edge control. The caveats are the familiar ones: small samples, healthy-volunteer dominance, and the difficulty of confirming that the entrainment delivered at the scalp actually reaches the intended deep edge.

### 3.3 Temporal interference (tTIS): the noninvasive depth advance

tTIS is the most important development for the depth axis. Two electrode pairs deliver high-frequency carriers (for example 9.00 and 9.13 kHz), each individually too fast to drive neurons. Where the two fields overlap, they produce a low-frequency beat envelope (here 130 Hz, or any chosen difference frequency) that can drive neural activity at depth while the overlying cortex sees only the inaudibly fast carriers (16). This is the first noninvasive electrical technique that focally engages deep structures.

The human evidence has matured rapidly. Wessel, Hummel, and colleagues showed theta-burst tTIS focally engaging the human striatum with fMRI confirmation and improved motor learning in older adults (Nature Neuroscience 2023) (17), and a 2024 follow-up showed bidirectional control by disrupting reinforcement learning (18). Violante and colleagues demonstrated noninvasive tTIS of the human hippocampus, verified by cadaver field measurement and human fMRI, with enhanced episodic-memory accuracy (Nature Neuroscience 2023) (19). In 2025, Lamoš and colleagues focused a tTIS envelope on the motor subterritory of the subthalamic nucleus in Parkinson's patients (carriers 9.00 and 9.13 kHz, 4 mA peak-to-peak per pair, temporoparietal electrodes) and recorded suppression of high-beta local field potential power comparable to conventional DBS, measured through the patients' own implanted leads (Movement Disorders 2025) (20). A companion 2025 paper targeted the globus pallidus (21), and a 2025 Hummel review frames tTIS as the pioneering noninvasive deep-brain modality for movement disorders (22).

The limits are real and quantified. Focality is good but not perfect: optimized tTIS focality at a deep target varies by up to 1.2 cm across 25 subjects because of inter-individual anatomical differences, which means group-level montages miss the target in many heads and individualized electric-field optimization is necessary, not optional (23). Multi-pair and multipolar tTIS, adding electrode pairs or carrier frequencies, can tighten focality at the target and reduce off-target cortical engagement, and primate work has reached the superior colliculus with multipolar tTIS (24). The achievable subcortical field strengths remain modest, so the question of whether the envelope reliably reaches the threshold needed for a clinical effect in a real human head is still open. Temporal resolution is good because the envelope frequency is a free parameter that can be set to any physiological rhythm, which makes tTIS in principle a deep oscillation-targeted (edge) tool, not merely a deep node tool.

### 3.4 Node vs edge for tES

tDCS modulates nodes (diffusely). tACS modulates edges through frequency and phase, and is the strongest noninvasive case for direct functional-coupling control. tTIS modulates deep nodes focally and, because its envelope frequency is tunable, can in principle modulate deep edges, though the human edge-targeting evidence for tTIS is still preliminary.

### 3.5 Regulatory status

The Flow Neuroscience FL-100 at-home tDCS device received FDA approval in December 2025 for moderate-to-severe MDD, the registration trial being EMPOWER (174 participants, 58 percent remission in the active arm) (25). No tACS, tRNS, or tTIS device has an FDA psychiatric indication as of May 2026.

### Table 3. tES family at a glance

| Axis | tDCS / HD-tDCS | tACS (dual-site) | tTIS |
| --- | --- | --- | --- |
| Spatial resolution | diffuse; HD ~1 to 2 cm | per-node, edge via phase | focal deep, ~0.5 to 1.5 cm (variable) |
| Temporal resolution | minutes to build | cycle-by-cycle entrainment | envelope-frequency tunable |
| Depth (noninvasive) | superficial cortex | cortex | striatum, hippocampus, STN, GP |
| Limit on depth | field smaller than overlying cortex | same | field strength; inter-individual variability (1.2 cm) |
| Node vs edge | node (diffuse) | edge (phase/frequency coupling) | deep node, deep edge in principle |
| Regulatory | FDA-approved at-home (Flow, 2025) | none | none |

---

## 4. Focused ultrasound (FUS / LIFU)

### 4.1 Resolution and depth: the best noninvasive focality

FUS is the spatial-resolution leader. With MR guidance and skull-aberration correction, an acoustic focus of a few cubic millimeters can be placed at essentially any depth, including thalamus, subthalamic nucleus, nucleus accumbens, and amygdala, structures no electrical or magnetic method reaches focally. A 2025 wearable forehead matrix-array LIFU system illustrates the achievable specification: a steerable beam with a focal spot 4.5 mm in diameter and 25 mm axial extent at 50 mm depth, electronically steered across a broad prefrontal volume without moving the transducer (26). Depth resolution and focality are roughly an order of magnitude better than any noninvasive electrical or magnetic method.

Temporal resolution depends on regime. Sonication bursts can be gated on a millisecond-to-second timescale, so LIFU can in principle be pulsed in a state-dependent loop, but the neuromodulatory effect and its mechanism (mechanosensitive ion-channel gating) are slower and less well characterized than a TMS pulse's, and the latency from sonication to a readable physiological change is not yet tightly bounded.

### 4.2 Node vs edge

FUS is fundamentally a node tool, and the best node tool available. Its millimeter focus is its strength for hitting a single deep nucleus and its limitation for engaging an edge: a single focus does not stimulate two nodes at once. Edge engagement with FUS is therefore indirect (modulate one deep node and rely on its projections) or, prospectively, multi-focal (steerable arrays that can sequence or split the focus across two targets). The 2025 steerable matrix array is the hardware that could make multi-focal FUS feasible, but multi-target edge protocols are not yet demonstrated in humans. FUS also pairs with connectivity-guided targeting: a 2024 LIFU-to-DLPFC depression trial reported increased sgACC-medial PFC connectivity after treatment, an edge-level readout of a node-level intervention (see neuromodulation.md ref 40).

### 4.3 Regulatory status

High-intensity MRgFUS (Insightec ExAblate) is FDA-approved for essential tremor and tremor-dominant and staged-bilateral Parkinson's disease. Low-intensity LIFU for psychiatry is investigational, with multiple active IDE studies (depression, anxiety, substance use disorder). No LIFU psychiatric indication is FDA-cleared.

### Table 4. FUS at a glance

| Axis | Low-intensity FUS (LIFU) |
| --- | --- |
| Spatial resolution | a few cubic mm; 4.5 mm focal diameter achievable (2025) |
| Temporal resolution | ms-to-s sonication gating; effect latency less defined |
| Depth (noninvasive) | whole brain, including deep nuclei |
| Limit on depth | skull aberration; requires individualized acoustic modeling |
| Node vs edge | node (best available); edge only indirectly or via future multi-focal arrays |
| Regulatory | investigational for psychiatry; MRgFUS approved for ET/PD |

---

## 5. Transcutaneous vagus nerve stimulation (tVNS)

tVNS is the outlier on every axis discussed here because it does not target a brain region at all. It stimulates a peripheral nerve (auricular or cervical vagus) and recruits brain-wide ascending neuromodulatory systems (locus coeruleus noradrenergic, dorsal raphe serotonergic) plus the cholinergic anti-inflammatory reflex (see neuromodulation.md and neuromodulation-response.md). It has no cortical spatial resolution, slow and diffuse effects, no meaningful depth concept, and acts on a broadcast system rather than a node or an edge. Its closed-loop relevance is real but lies in autonomic gating (respiration-phase or HRV-locked delivery), not in spatial targeting. It is included here as a contrast that sharpens the point: the modalities with spatial targeting (TMS, tES, FUS) are the ones for which the node-vs-edge question and the sensing-paired loop are meaningful.

Regulatory status: cervical nVNS (electroCore Gammacore) is FDA-cleared for migraine and cluster-headache indications; auricular tVNS devices are research-grade or wellness-grade with no FDA psychiatric clearance.

---

## 6. Invasive DBS as the high-resolution comparator

Deep brain stimulation is the reference standard against which noninvasive modalities should be measured, because it achieves what they aspire to. An implanted multi-contact electrode delivers stimulation to a sub-millimeter volume at any depth with millisecond temporal control, and segmented (directional) leads now steer the field within a nucleus. Critically, DBS is the only modality that has closed the full sense-infer-modulate-resense loop in an approved product (Section 7). DBS is also an edge tool in a way noninvasive methods are not yet: a single lead in the subthalamic nucleus modulates the entire pathologically synchronized cortico-basal-ganglia loop, and multi-lead configurations (for example ventral capsule plus other targets in psychiatric DBS) explicitly engage subnetworks. The relevant question for the proposal is not whether noninvasive methods match DBS resolution today (they do not) but which DBS capabilities, especially the closed-loop architecture, transfer to a noninvasive sensor-plus-effector system.

### Table 6. Cross-modality resolution and depth summary

| Modality | Spatial resolution | Temporal resolution | Noninvasive depth | Node vs edge | FDA psychiatric/neuro status |
| --- | --- | --- | --- | --- | --- |
| rTMS (fig-8) | 1 to 3 cm | <1 ms/pulse | 1.5 to 2.5 cm | node + connectivity edge | cleared (MDD, OCD, etc.) |
| Deep TMS (H-coil) | 3 to 5 cm | <1 ms/pulse | 3 to 4 cm | node/diffuse | cleared (MDD, OCD, smoking) |
| mTMS | mm switching | microsecond switching | cortical | programmable edge | research |
| tDCS / HD-tDCS | diffuse / 1 to 2 cm | minutes | superficial cortex | node (diffuse) | at-home tDCS approved (Flow 2025) |
| tACS (dual-site) | per-node | cycle-by-cycle | cortex | edge (phase/freq) | none |
| tTIS | 0.5 to 1.5 cm (variable) | envelope-tunable | deep nuclei | deep node, deep edge (preliminary) | none |
| LIFU | few mm (4.5 mm achievable) | ms-to-s | whole brain | node (best); multi-focal future | investigational (psych) |
| tVNS | none (peripheral) | slow/diffuse | n/a | broadcast system | cleared (migraine/cluster) |
| DBS (invasive comparator) | sub-mm | ms | any depth | node + edge (multi-lead) | approved incl. adaptive (2025) |

---

## 7. Closed-loop and sensing-paired neuromodulation

This is the section the proposal most needs. A truly adaptive, interactive system implements a loop: sense a brain state, infer the optimal action, modulate, then re-sense to verify and adjust. Open-loop systems do the modulate step on a fixed schedule and never read the result. The distinction matters because the entire Cytognosis thesis is that the missing leg of the loop in noninvasive neuromodulation is the sense-and-infer leg, not the modulate leg.

### 7.1 The proof of concept lives in invasive devices

Adaptive DBS (Medtronic Percept with BrainSense). The FDA approved BrainSense Adaptive DBS in February 2025, the first regulatory blessing of a fully adaptive sense-infer-modulate-resense loop for chronic brain stimulation (27). The same electrodes that deliver stimulation sense subthalamic local field potentials; the algorithm reads beta-band power (the Parkinsonian motor-state biomarker), compares it to patient-specific single or dual thresholds, and adjusts stimulation amplitude in real time. The ADAPT-PD trial (45 patients, single-blind randomized crossover, each patient as own control) reported improved on-time without troublesome dyskinesia, lower total stimulation energy, and better quality-of-life scores versus continuous DBS, published in JAMA Neurology in 2025; ADAPT-START extended the chronic adaptive findings and programming principles (27, 28). This is a genuine, FDA-approved, multi-patient adaptive loop, the firmest closed-loop evidence in the entire field.

NeuroPace RNS. Responsive neurostimulation for drug-resistant epilepsy has run a closed loop in cortex since 2013: it detects ictal patterns and delivers responsive stimulation, with median seizure reduction reaching 53 percent at two years and 72 percent at six to nine years (see neuromodulation-response.md ref 52). RNS is the longest-running closed-loop neuromodulation evidence base, though its loop is event-triggered (detect-then-stimulate) rather than continuously adaptive.

Closed-loop intracranial DBS for depression. Scangos and colleagues demonstrated a single-patient closed-loop system for treatment-resistant depression: an amygdala gamma biomarker triggered ventral-capsule stimulation, with sustained antidepressant response (Nature Medicine 2021) (29). This is the conceptual blueprint for noninvasive translation. It is a single patient; the PRESIDIO multi-patient trial is ongoing. Provenza and colleagues showed personalized symptom-state biomarkers triggering DBS for OCD.

The lesson for the proposal: the loop architecture is proven and FDA-approved, but only with implanted electrodes that both sense and stimulate through the same hardware. The noninvasive task is to substitute a wearable sensor for the implanted sensing leg.

### 7.2 TMS-EEG closed-loop: the most mature noninvasive loop

Brain-state-dependent TMS, developed by Zrenner, Bergmann, and Ziemann at Tübingen, triggers TMS pulses on the real-time phase of an ongoing EEG oscillation. The foundational demonstration showed larger motor-evoked potentials and greater plasticity when pulses arrived at the trough of the sensorimotor mu rhythm rather than the peak, establishing that real-time EEG-defined excitability state determines TMS efficacy (30, 31). This is a true closed loop on the millisecond timescale: sense phase, infer the favorable window, fire, and the technique now extends to Bayesian-optimized and reinforcement-learning-based per-patient phase selection (see neuromodulation.md refs 60, 61).

The clinical translation to depression is real but thin. The MUSC group (Leuchter, George, and colleagues) ran a first-in-human double-blind randomized controlled trial of EEG-synchronized left-prefrontal rTMS for treatment-resistant depression, synchronizing each rTMS train to the patient's individual prefrontal alpha frequency at the F3 position (NCT03241808). The trial demonstrated that synchronization is feasible across a full 30-visit course, that synchronized stimulation produces greater EEG phase entrainment than unsynchronized stimulation, and that the clinical response is entrainment-dependent (32). It also showed, mechanistically, that a single prefrontal pulse produces larger anterior-cingulate effects depending on the alpha phase at which it is fired, an edge-level (DLPFC-sgACC) readout gated by brain state. The honest summary: this is a small feasibility-and-mechanism trial (roughly a dozen completers per arm), not a definitive efficacy trial. The 2025 BOSSFRONT2 trial design compares four weeks of EEG-synchronized dorsomedial-PFC rTMS (triple 100-Hz pulses phase-locked to the trough of individual theta) against standard iTBS, but results are not yet reported (33). A 2025 mu-rhythm study found that pre-stimulus power, not phase, predicted motor-evoked potentials, complicating the simple phase story (see neuromodulation.md ref 62). So the most mature noninvasive closed loop rests on solid mechanism and feasibility but unsettled clinical superiority.

### 7.3 tACS-EEG closed-loop oscillatory entrainment

Closed-loop tACS locks the stimulation to a detected feature of the ongoing EEG. The best-developed example is closed-loop slow-wave tACS during sleep, locked to detected slow-oscillation up-states, which augments slow oscillations and improves overnight memory consolidation in healthy adults (Ketz, Jones, and colleagues) (see neuromodulation-response.md ref 35). The core engineering obstacle for closed-loop tACS in the awake brain is that the stimulation itself injects a large electrical artifact into the EEG channels needed for state estimation, which is precisely the problem an optical (fNIRS) sensor sidesteps, because light is immune to the electrical artifact. Frohlich and colleagues are developing closed-loop tACS for depression locked to frontal alpha. Awake closed-loop tACS for psychiatry remains a laboratory technique.

### 7.4 fMRI-guided, fMRI-neurofeedback, and fNIRS

fMRI-guided targeting is the offline backbone of personalized TMS (the SAINT rsfMRI scan) but is not a real-time loop; the scan is acquired once, the target is computed, and treatment proceeds open-loop thereafter. Real-time fMRI neurofeedback is a genuine closed loop in which the patient sees and self-regulates a region's activation, but it requires the participant to be in the scanner and does not by itself drive an external stimulator. Combining real-time fMRI with stimulation has been demonstrated within single sessions but is not packaged or scalable.

fNIRS-guided and fNIRS-neurofeedback closed loops are the most relevant and the least mature. fNIRS measures cortical hemodynamics, is immune to TMS and tES electrical artifact, and is portable, which makes it the natural wearable sensing leg for a noninvasive loop. The existing literature is small: concurrent fNIRS-TMS measurement studies, a randomized study using fNIRS to navigate rTMS for motor hemiplegia, and a 2024 meta-analysis of fNIRS-measured cortical responses to rTMS (see neuromodulation.md refs 63 to 65). A 2025 study used longitudinal EEG to assess adaptive responses to FUS and argued that real-time closed-loop neuromodulation would benefit from EEG (or analogous) feedback integration (34). No commercial fNIRS-guided or fNIRS-neurofeedback closed-loop stimulation product exists in 2026. This is the precise gap a Cytoscope-class wearable would fill, and the proposal should state plainly that the fNIRS closed-loop case rests today on a handful of feasibility studies, not on clinical trials.

### 7.5 MEG-guided and OPM-MEG

MEG localizes oscillatory sources better than EEG and has been used to define individualized TMS targets in research, but conventional MEG needs a magnetically shielded room and a multi-million-dollar cryogenic system, which rules it out as a wearable loop sensor. Optically pumped magnetometers (OPMs) are changing the cost and form factor: OPM-MEG is wearable, operates without cryogenics, tolerates head movement, and a 2024-2025 generation of platforms implements three-axis closed-loop field control and even wireless operation, allowing recording during free movement (35). OPM-MEG is a closed loop in the sensor-engineering sense (the magnetometers run closed-loop field nulling), not yet in the therapeutic sense (it does not yet drive a stimulator in a sense-infer-modulate loop). It is a candidate future sensing leg, still pre-wearable-product for neuromodulation.

### 7.6 Closed-loop FUS

Closed-loop FUS is early. MR thermometry already provides closed-loop dosimetry for high-intensity ablation. For low-intensity LIFU, within-session physiological feedback using simultaneous EEG or fMRI has been demonstrated but not packaged; the 2025 wearable steerable forehead array (Section 4) is the hardware platform on which a closed loop could be built, and the longitudinal-EEG-plus-FUS work points the direction (26, 34). Openwater's announced roadmap targets AI-driven closed-loop FUS of the default mode network. None of this is yet an adaptive product.

### 7.7 Which systems are truly adaptive and interactive

Sorting the field by whether the full loop (sense, infer, modulate, re-sense) actually runs:

- Genuinely adaptive, approved: Medtronic Percept BrainSense Adaptive DBS (continuous beta-driven adaptation, FDA 2025); NeuroPace RNS (event-triggered detect-then-stimulate, FDA 2013). Both invasive.
- Genuinely closed-loop, noninvasive, research-grade: brain-state-dependent TMS-EEG (millisecond phase-triggered, mature mechanism, feasibility-stage clinical); closed-loop slow-wave tACS-EEG during sleep (healthy-volunteer memory studies).
- Single-patient or single-study proof of principle: Scangos closed-loop intracranial DBS for depression (one patient); EEG-synchronized rTMS for depression (one small feasibility RCT).
- Open-loop today, despite personalization: SAINT (offline rsfMRI target, then open-loop treatment); standard rTMS, tDCS, LIFU, tVNS protocols.
- Sensor exists, loop not yet built: fNIRS-guided stimulation; OPM-MEG-guided stimulation; closed-loop LIFU.

### 7.8 The gap: what a wearable fNIRS-class sensor must provide

For a wearable sensor to enable noninvasive closed-loop targeting of edges and subnetworks, it must deliver four capabilities that no current wearable delivers together:

1. Edge-level state estimation, not just node activity. The sensor must estimate functional connectivity (a frontolimbic edge, a default-mode coupling), not merely the activation of one cortical patch, because the therapeutic target is an edge. fNIRS can estimate cortical-cortical hemodynamic connectivity in the 0.01 to 0.1 Hz band; the open question is whether surface optical channels can recover the specific edges (especially edges involving deep nodes like sgACC, amygdala, striatum) that the disease lives on. The deep nodes are out of fNIRS reach directly, so the sensor must infer deep-edge state from cortical proxies, which is an inference problem, not a measurement problem.
2. Real-time, artifact-immune operation during stimulation. The sensor must keep estimating state while TMS, tES, or FUS runs. Optical sensing is immune to the electrical artifact that defeats EEG during tES, which is the single strongest technical argument for an optical wearable in this role.
3. Latency matched to the effector. A phase-triggered TMS loop needs millisecond latency; an fNIRS hemodynamic signal is intrinsically slow (seconds). A wearable loop will therefore likely run at two timescales: fast electrical (EEG) for phase-locking and slower optical (fNIRS) for connectivity-state and target selection, a hybrid the proposal should make explicit.
4. A trained policy mapping state to action. The infer leg requires a model that maps the multivariate sensor state to a stimulation modality, target, and parameter set. This is the Cytonome layer, and it is where the wearable platform creates defensible value beyond the (already FDA-cleared) effectors.

The concise framing for the proposal: every effector leg of the loop is FDA-cleared or in advanced trials (TMS, tDCS, LIFU, and the full adaptive loop in DBS), but the noninvasive sense-and-infer leg, especially edge-level state estimation from a wearable, does not exist as a product. That is the tractable gap.

### 7.9 2024-2026 closed-loop systems and trials, summarized honestly

| System / trial | Loop type | Sensor | Effector | Evidence strength (2026) |
| --- | --- | --- | --- | --- |
| Medtronic BrainSense aDBS (ADAPT-PD, JAMA Neurol 2025) | adaptive, continuous | implanted LFP (beta) | DBS | strong; FDA-approved Feb 2025; n=45 RCT crossover |
| NeuroPace RNS | event-triggered | implanted ECoG | cortical stim | strong; >9 yr data; FDA 2013 |
| Scangos intracranial CL-DBS for TRD (Nat Med 2021) | adaptive | implanted gamma | DBS | single patient; multi-patient trial ongoing |
| Tübingen brain-state-dependent TMS-EEG | adaptive, ms phase | scalp EEG | TMS | strong mechanism; clinical feasibility-stage |
| MUSC EEG-synchronized rTMS for TRD | adaptive, alpha phase | scalp EEG | rTMS | one small double-blind RCT; entrainment-dependent response |
| BOSSFRONT2 (2025) | adaptive, theta phase | scalp EEG | rTMS | design published; results pending |
| Closed-loop slow-wave tACS (sleep) | adaptive, up-state | scalp EEG | tACS | healthy-volunteer memory studies |
| fNIRS-guided rTMS | open-loop guidance | fNIRS | TMS | feasibility studies only; no product |
| OPM-MEG platforms (2024-2025) | sensor closed-loop only | OPM | none yet | sensor mature; not yet driving stimulation |
| Closed-loop LIFU (Openwater roadmap) | proposed adaptive | EEG/fMRI | LIFU | early; not yet a product |

---

## 8. Synthesis for the X-Labs / ARPA-H proposal

Three conclusions carry the technical argument.

First, on resolution and depth, the field has a clear division of labor. TMS owns millisecond temporal precision and the richest edge-targeting toolkit but cannot reach deep structures. tTIS and LIFU own depth: tTIS is the first noninvasive electrical method to focally modulate striatum, hippocampus, and subthalamic nucleus, and LIFU is the focality leader at a few millimeters anywhere in the brain. tACS owns oscillatory edge control through frequency and phase. The proposal can therefore promise an effector portfolio that, across modalities, already spans node and edge, superficial and deep.

Second, on node vs edge, the state of the art is that noninvasive edge modulation is demonstrated mechanistically (dual-site TMS, mTMS, phase-controlled dual-site tACS, cross-frequency bifocal tACS) but not yet proven clinically superior to single-node stimulation on a psychiatric endpoint. The most clinically validated edge strategy remains connectivity-seeded single-site stimulation (the SAINT DLPFC-sgACC logic), which is an edge intervention executed through one accessible node.

Third, on closed-loop, the full adaptive loop is FDA-approved only in invasive DBS (Percept BrainSense, February 2025) and proven in invasive RNS. The most mature noninvasive loop is brain-state-dependent TMS-EEG, strong on mechanism but only feasibility-stage in psychiatry, with the EEG-synchronized rTMS depression result resting on a single small trial. Every effector leg is cleared or in advanced trials; the missing leg is a wearable, artifact-immune, edge-level sensing-and-inference system. That is the gap Cytognosis proposes to close, and it should be stated as a gap, not as a solved problem.

---

## References

1. Cole EJ, Phillips AL, Bentzley BS, et al. Stanford Neuromodulation Therapy (SNT): A Double-Blind Randomized Controlled Trial. Am J Psychiatry. 2022;179(2):132-141. https://doi.org/10.1176/appi.ajp.2021.20101429
2. Deng ZD, Lisanby SH, Peterchev AV. Electric field depth-focality tradeoff in transcranial magnetic stimulation: simulation comparison of 50 coil designs. Brain Stimul. 2013;6(1):1-13. https://doi.org/10.1016/j.brs.2012.02.005
3. Zibman S, Daniel E, Alyagon U, et al. Application of transcranial magnetic stimulation for major depression: coil design and neuroanatomical variability considerations. Eur Neuropsychopharmacol. 2021;45:73-88. https://doi.org/10.1016/j.euroneuro.2019.06.009
4. Huang YZ, Edwards MJ, Rounis E, Bhatia KP, Rothwell JC. Theta burst stimulation of the human motor cortex. Neuron. 2005;45(2):201-206. https://doi.org/10.1016/j.neuron.2004.12.033
5. Fox MD, Buckner RL, White MP, Greicius MD, Pascual-Leone A. Efficacy of TMS targets for depression is related to intrinsic functional connectivity with the subgenual cingulate. Biol Psychiatry. 2012;72(7):595-603. https://doi.org/10.1016/j.biopsych.2012.04.028
6. Network-targeted transcranial magnetic stimulation (TMS) for mild cognitive impairment (MCI). NeuroImage: Clinical. 2025. https://pmc.ncbi.nlm.nih.gov/articles/PMC12192757/
7. Targeting brain networks: a review of multi-site TMS techniques and applications. 2025. https://www.tandfonline.com/doi/full/10.1080/27706710.2025.2583774
8. Koponen LM, Nieminen JO, Ilmoniemi RJ, et al. Multi-locus transcranial magnetic stimulation system for electronically targeted brain stimulation. Brain Stimul. 2022;15(1):116-124. https://pmc.ncbi.nlm.nih.gov/articles/PMC8807400/
9. Characterizing an electronic-robotic targeting platform for precise and fast brain stimulation with multi-locus TMS. bioRxiv. 2024. https://www.biorxiv.org/content/10.1101/2024.03.12.584601.full.pdf ; Multi-locus TMS with pulse-width modulation. Aalto. 2025. https://research.aalto.fi/en/publications/multi-locus-transcranial-magnetic-stimulation-with-pulse-width-mo
10. Magnus Medical Announces Commercial Launch of SAINT Neuromodulation System. April 2024. https://www.magnusmed.com/press-releases/magnus-medical-announces-commercial-launch-of-groundbreaking-saint-neuromodulation-system/
11. Nitsche MA, Paulus W. Excitability changes induced in the human motor cortex by weak transcranial direct current stimulation. J Physiol. 2000;527(3):633-639. https://doi.org/10.1111/j.1469-7793.2000.t01-1-00633.x
12. Phase-lagged tACS between executive and default mode networks modulates working memory. Sci Rep. 2025. https://www.nature.com/articles/s41598-025-91881-5
13. Single session cross-frequency bifocal tACS modulates visual motion network activity in young healthy population and stroke patients. Brain Stimul. 2024. https://www.sciencedirect.com/science/article/pii/S1935861X24000895
14. Simultaneous tACS-fMRI reveals state- and frequency-specific modulation of hippocampal-cortical functional connectivity. Commun Psychol. 2025. https://www.nature.com/articles/s44271-025-00202-z
15. Individual alpha frequency tACS reduces static functional connectivity across the default mode network. Front Hum Neurosci. 2025. https://www.frontiersin.org/journals/human-neuroscience/articles/10.3389/fnhum.2025.1534321/full
16. Grossman N, Bono D, Dedic N, et al. Noninvasive Deep Brain Stimulation via Temporally Interfering Electric Fields. Cell. 2017;169(6):1029-1041.e16. https://doi.org/10.1016/j.cell.2017.05.024
17. Wessel MJ, Beanato E, Popa T, et al. Noninvasive theta-burst stimulation of the human striatum enhances striatal activity and motor skill learning. Nat Neurosci. 2023;26(11):2005-2016. https://doi.org/10.1038/s41593-023-01457-7
18. Vassiliadis P, Beanato E, Popa T, et al. Non-invasive stimulation of the human striatum disrupts reinforcement learning of motor skills. Nat Hum Behav. 2024. https://www.nature.com/articles/s41562-024-01901-z
19. Violante IR, Alania K, Cassarà AM, et al. Non-invasive temporal interference electrical stimulation of the human hippocampus. Nat Neurosci. 2023;26(11):1994-2004. https://www.nature.com/articles/s41593-023-01456-8
20. Lamoš M, et al. Noninvasive Temporal Interference Stimulation of the Subthalamic Nucleus in Parkinson's Disease Reduces Beta Activity. Mov Disord. 2025. https://doi.org/10.1002/mds.30134
21. Yang et al. Transcranial Temporal Interference Stimulation of the Right Globus Pallidus in Parkinson's Disease. Mov Disord. 2025. https://doi.org/10.1002/mds.29967
22. Hummel FC, et al. Transcranial Temporal Interference Stimulation (tTIS): Pioneering Non-Invasive Deep Brain Neuromodulation for Movement Disorders and Beyond. Mov Disord. 2025. https://doi.org/10.1002/mds.30237
23. On the need of individually optimizing temporal interference stimulation of human brains due to inter-individual variability. Brain Stimul. 2025. https://www.brainstimjrnl.com/article/S1935-861X(25)00274-8/fulltext
24. Beyond the surface: a review of transcranial temporal interference stimulation for deep brain modulation. Front Neurol. 2025. https://www.frontiersin.org/journals/neurology/articles/10.3389/fneur.2025.1661049/full
25. Woodham RD, Selvaraj S, Lajmi N, et al. Home-based transcranial direct current stimulation treatment for MDD: a fully remote phase 2 randomized sham-controlled trial (EMPOWER). Nat Med. 2025;31:87-95. https://doi.org/10.1038/s41591-024-03305-y
26. A Wearable, Steerable, Transcranial Low-Intensity Focused Ultrasound System. J Ultrasound Med. 2025. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11719763/
27. Groundbreaking study published in JAMA Neurology demonstrates effectiveness of Medtronic BrainSense Adaptive DBS for Parkinson's (ADAPT-PD); FDA approval February 2025. https://news.medtronic.com/Groundbreaking-study-published-in-the-Journal-of-the-American-Medical-Association-JAMA-Neurology-demonstrates-effectiveness-of-Medtronic-BrainSense-TM-Adaptive-deep-brain-stimulation-for-people-with-Parkinsons
28. Chronic adaptive deep brain stimulation in Parkinson's disease: ADAPT-START findings and programming principles. npj Parkinsons Dis. 2026. https://www.nature.com/articles/s41531-026-01269-z
29. Scangos KW, Khambhati AN, Daly PM, et al. Closed-loop neuromodulation in an individual with treatment-resistant depression. Nat Med. 2021;27(10):1696-1700. https://doi.org/10.1038/s41591-021-01480-w
30. Zrenner C, Desideri D, Belardinelli P, Ziemann U. Real-time EEG-defined excitability states determine efficacy of TMS-induced plasticity in human motor cortex. Brain Stimul. 2018;11(2):374-389. https://doi.org/10.1016/j.brs.2017.11.016
31. Zrenner C, Ziemann U. Closed-Loop Brain Stimulation. Biol Psychiatry. 2024;95(6):545-552. https://doi.org/10.1016/j.biopsych.2023.09.014
32. EEG synchronized left prefrontal TMS for treatment resistant depression is feasible and produces an entrainment dependent clinical response: a randomized controlled double blind clinical trial (MUSC; Leuchter, George, et al.; NCT03241808). Brain Stimul. 2024. https://pmc.ncbi.nlm.nih.gov/articles/PMC10872322/
33. Brain oscillation-synchronized stimulation for major depression: a randomized controlled trial comparing EEG-triggered rTMS with standard iTBS (BOSSFRONT2). Eur Arch Psychiatry Clin Neurosci. 2025. https://link.springer.com/article/10.1007/s00406-025-02176-9
34. Longitudinal EEG-based assessment of neuroplasticity and adaptive responses to transcranial focused ultrasound stimulation. J Neurosci Methods. 2025. https://pubmed.ncbi.nlm.nih.gov/40581220/
35. A novel, robust, and portable platform for magnetoencephalography using optically-pumped magnetometers. Imaging Neuroscience. 2024. https://www.ncbi.nlm.nih.gov/pmc/articles/PMC11533384/
