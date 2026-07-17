# PsychIGoR, ARPA-H SOL-26-155 (IGoR, Proactive Health Office), FINAL SUBMITTED Solution Summary

> **Source (hand-edited by Shahin):** https://docs.google.com/document/d/12bxWF0ZkK7FVMOhsnlt4DijfRWkxDy0Wf7sR-ww85Fw/edit
> **Snapshot:** pulled read-only 2026-07-17; canonical record of the Solution Summary submitted 2026-06-25. Do not edit the Google Doc programmatically; this is a read-only mirror.
> **Headline facts (as submitted):** Prime = IPAI, Purdue (UEI YRXVL4JYCEF5); 60 months; total ARPA-H request **$51,500,000** (+ ~$3.1M in-kind, ~$54.6M total); Animal subjects No; Human subjects No.

---

| **Innovative Solutions Opening Title** | ARPA-H-SOL-26-155 (Intelligent Generator of Research, IGoR), Proactive Health Office |
| --- | --- |
| **Solution Summary Title** | **PsychIGoR**: Intelligent Generator of Disease Mechanisms for Psychiatric Disorders |
| **Prime Organization** | Institute for Physical AI (IPAI), Purdue University (Academia) |
| **UEI** | YRXVL4JYCEF5 |
| **Duration** | 60 Months |
| **Total ARPA-H request** | $51,500,000 |
| **Resource sharing** | ~$3.1M in-kind (IPAI/Purdue HPC + wet-lab; Cellanome R3200/imaging, ~$0.95M); total project value ~$54.6M |
| **Places of performance** | Purdue (IN); Cytognosis (CA); SIFT (MN); Cellanome (CA); McLean (MA) |

**Key personnel:** Ananth Grama (Purdue IPAI, PI); Anne Carpenter (IPAI / Broad); Matthew Tegtmeyer (Purdue); Shahin Mohammadi (Cytognosis); Daniel Bryce (SIFT); Shawn Levy (Cellanome); W. Brad Ruzicka (HMS / McLean).

## 1. Concept summary

More than nine in ten drug candidates that enter human trials never reach patients, and psychiatric and neurological programs perform the worst of all. These programs fail for three interconnected reasons: patients are grouped by a diagnostic label (such as schizophrenia), masking heterogeneity across their underlying pathophysiology; the cellular mechanisms that drive the illness are often unknown, so therapies aim at the wrong targets; and even promising therapies are often tested on the wrong patients, diluting their real effect. In short, today's trials test the wrong mechanism, on the wrong patients, defined by the wrong labels. PsychIGoR overcomes these challenges by (1) replacing categorical labels with quantitative, personalized phenotypic measures computed directly from clinical records, capturing the heterogeneity of observed symptoms across patients, such as the negative (e.g., social withdrawal) and positive (e.g., delusions) symptoms in schizophrenia; (2) identifying the specific cellular processes (endotypes) that both carry human genetic support and, when corrected, reverse the disease state in human-cell models, so that each target is grounded in cause, not correlation; and (3) matching each prioritized mechanism to the subgroup of patients who share it (a biotype), inferred jointly from their genetic and clinical profiles, so the right therapy reaches the right individuals.

To address these challenges at scale, we build a mechanistic, AI-driven world model of disease that continuously integrates new data from human genetics and laboratory experiments into robust models, paired with an AI engine that uses the model to simulate, design, and prioritize the most informative experiments, closing the loop between prediction and evidence, and improving both the speed and the success rate of discovery with each cycle. A shared semantic foundation lets every component represent bioentities and processes unambiguously, so information transfers seamlessly across the model, protocols, and laboratories, and feeds back into the model.

We focus on schizophrenia, one of the most debilitating psychiatric disorders, as the primary target on which to build our platform, and bipolar disorder, its most strongly genetically correlated relative, as the Phase III extension. Our team integrates complementary expertise in the clinical (Mohammadi, Ruzicka) and cellular (Tegtmeyer, Carpenter) study of psychiatric disorders with computational depth in physical AI and large-scale scientific computing (Grama, Mohammadi), and in automated planning, autonomous experimentation, and interoperable laboratory standards (Bryce, Goldman).

## 2. Innovation and impact

Only 7.9% of drugs entering Phase I are approved, and psychiatry (7.3%) and neurology (5.9%) rank lowest of all; the bottleneck is Phase II, which only 28.9% of candidates clear (Thomas 2021). Three compounding gaps drive failure: unaccounted disease heterogeneity (patients grouped by label mix biologically distinct biotypes; Drysdale 2017, Clementz 2016; the field is moving to RDoC/HiTOP, Insel 2010, Kotov 2017, Grotzinger 2025); unknown causal mechanism (most psychiatric risk variants are noncoding; a likely causal gene is assigned to only 120 of 287 schizophrenia loci, Trubetskoy 2022; virtual-cell perturbation predictors rarely beat linear baselines, Ahlmann-Eltze 2025); and ignored patient heterogeneity.

Four innovations turn genetic and cellular evidence (human genetic support makes a target 2.6x likelier to be approved, Nelson 2015, Minikel 2024) into a discovery engine: (1) dual grounding, jointly factorizing isogenic perturbations and population genetics into one sparse set of transdiagnostic disease axes that are both drug targets and per-person biotype scores; (2) disease as a causal operator, a deep structural causal model that predicts, counterfactually, on-target (efficacy) and off-target (safety) effects in human cells; (3) a self-driving discovery loop that proposes experiments by expected information gain; (4) a reusable, interoperable engine (LabOP, SiLA 2) with QC gates so any qualified lab can run protocols identically.

Impact: psychiatric and neurological disorders are leading causes of disability, and people with serious mental illness die roughly 15 to 20 years earlier (GBD 2019, Hjorthoj 2017). PsychIGoR makes candidates two to three times likelier to reach the clinic, and sooner. Success is measured by effective therapies reaching the right patients sooner, and by lives and healthy years restored.

## 3. Proposed work

A closed-loop system with four components: (TA1) mechanistic world model of disease (Cytognosis with IPAI; Tegtmeyer and Carpenter labs); (TA2) autonomous experiment-planning engine (Cytognosis, IPAI, SIFT; XPlan, Bayesian value of information); (TA3) virtual instrumentation engine (SIFT lead; LabOP, Biolink-grounded); (TA4) experimental execution and marketplace (academic arm: Purdue on Element Teton; industry arm: Cellanome R3200 with CellCage, adding calcium-imaging readout).

**Milestones.** Phase I (0-18 mo): build cellular models (22q11.2 deletion in five SSPsyGene control lines), interoperable protocols, joint model nominating 20 candidate processes; gate = cross-lab Jaccard > 0.85 and at least one genomic archetype with a differential clinical phenotype in the MGB cohort. Phase II (18-36 mo): narrow to 5 processes then 1 lead process, cycle time from 6 months to 1.5 months (>= 4x faster); gate = Jaccard >= 0.90 and archetypes with differential clinical phenotypes. Phase III (36-60 mo): extend to bipolar disorder, onboard a third lab, nominate lead process and targets, release open protocols, code, and IP.

**Clinical validity:** Mass General Brigham Biobank (Ruzicka); score each person on genomic archetypes, test separation by positive/negative symptom status and antipsychotic treatment resistance.

## 4. Team organization and capabilities

Team PsychIGoR is an integrated performer under a single PI (Grama). Disease-modeling core in-house; academic wet-lab at Purdue; Project Manager and Software/Systems Architect hired directly by Cytognosis and distinct from the PI. Cytognosis (Mohammadi) leads the TA1 disease model and TA1-TA2 interface. SIFT (Bryce, Goldman advisory) leads TA3 and the TA2-TA3 interface. Cellanome (Levy) is the TA4 industry execution arm. McLean/HMS (Ruzicka) leads clinical validation.

## 5. Basis of estimate

Bottom-up, scope-driven; total ARPA-H request ~$51.5M over 60 months (range $50M-$53M). Per-performer (5-yr, approx.): IPAI/Purdue computational $6.5M; Purdue Tegtmeyer lab ~$5.6M; Cytognosis $9.5M; SIFT $7.0M; Cellanome ~$9.5M; third lab ~$2.5M; shared compute $2.5M; TA4 sequencing ~$4.0M; McLean/HMS ~$1.5M; legal/IP $0.2M; integration/reserve ~$2.7M. Plus ~$3.1M in-kind (total ~$54.6M). Value to the public measured in health, not dollars.

**References:** full 38-reference list retained in the source Google Doc (Ahlmann-Eltze 2025; Avsec 2026 AlphaGenome; Bartley 2023 LabOP; Blau 2022; Grotzinger 2025 Nature; Minikel 2024; Nelson 2015; Thomas 2021 BIO; Trubetskoy 2022 PGC; Tegtmeyer 2025 NeuroPainting; and others).
