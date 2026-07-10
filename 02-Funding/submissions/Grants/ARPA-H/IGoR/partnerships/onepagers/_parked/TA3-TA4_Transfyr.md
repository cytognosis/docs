# IGoR teaming: Transfyr and Cytognosis/IPAI, cross-lab reproducibility and execution observability

**Team PsychIGoR. IPAI (Purdue) prime, with its director, Ananth Grama, as PI; Cytognosis and IPAI lead the disease-model and AI core (TA1 and TA2). We are exploring Transfyr as the execution-observability and cross-lab reproducibility layer that strengthens TA4 concordance and feeds TA2.**

## What we bring, and have already built

- **A causal, self-updating disease model (TA1)** for psychiatric disease (schizophrenia as the primary focus, extending to bipolar disorder in Phase III), grounded in penetrant genetic forms (such as 22q11.2) modeled in iPSC cells, pairing clinical and cellular evidence in one framework.
- **A New Science Engine (TA2)** that interrogates the model itself to design the highest-value next experiment; not another literature-reading co-scientist.
- **An open protocol-portability layer (TA3) built on LabOP**, so a protocol transfers between laboratories as easily as a data file.
- **A team that has built the field's atlases**, including the first multi-cohort single-cell atlas of schizophrenia (Ruzicka, Mohammadi et al., Science 2024), with clinical depth at McLean Hospital (Harvard).

## The problem Transfyr could own

IGoR's closed loop is only as trustworthy as the fidelity of the experiments feeding the model. Two hard requirements stand out:

- **Cross-laboratory concordance.** The same protocol must produce the same result across sites and operators, and the proposal is scored on it.
- **Execution truth, not paper truth.** The model needs what actually happened at the bench (drift, operator decisions, environmental variables), not only the written protocol.

Transfyr's multimodal execution capture (vision, audio, instrument, and environmental signals) and your stated goal of learning transferable structure rather than site-specific artifacts map directly onto both. LabOP specifies and ports the protocol at design time; an observability layer would verify it at execution time, and the divergences become grounded training signal for the TA2 engine.

## Where Transfyr fits

- **Execution observability and reproducibility (cross-cutting TA4 and TA2).** The layer makes TA4 data model-ready and cross-lab comparable, and feeds the experiment-design engine real-world execution data so it does not optimize against clean, artificial datasets.
- **Runtime verification for TA3.** If the layer flags where actual execution diverged from the LabOP-specified protocol, it becomes the runtime check that closes the spec-to-execution gap.

## The one question we want to resolve first

Transfyr describes itself as "the API layer for science." We want to scope the role precisely: is that genuine cross-vendor interoperability (open APIs and standard export formats, working alongside other companies' instruments, software, and protocol layers such as LabOP), or an observability layer built around your own stack? Both are valuable, but they slot into an open IGoR architecture differently. Related: have you deployed in iPSC and imaging settings, and what is the lab-onboarding lift?

## Team and next step

| Role | Who |
|---|---|
**[HISTORICAL DRAFT -- Transfyr declined 2026-06-18. File retained for reference only. Transfyr is not in the PsychIGoR team.]**

| Prime and PI | IPAI, Purdue University; Ananth Grama (Director, IPAI) |
| TA1 and TA2 co-leads | Cytognosis Foundation (Shahin Mohammadi, sub-awardee) and IPAI, Purdue |
| Clinical and translational | W. Brad Ruzicka, McLean Hospital (Harvard Medical School affiliate) |
| TA4.1 academic experimental arm | Matt Tegtmeyer lab, Purdue |
| TA4.1 industry arm | Cellanome (advancing) |
| Computational morphology and imaging models | Anne Carpenter (IPAI/Purdue; no wet bench) |
| TA3 interoperable protocols | SIFT; Daniel Bryce (lead), Robert Goldman (advisory) |
| TA4.2 sequencing and bioinformatics | Illumina (proposed) |
| Software and Systems Architect | Elham Jebalbarezi Sarbijan, IPAI/Purdue (tentative) |
| Project Manager | Patricia Purcell |

**Timeline.** Solution Summary due June 25, 2026; full proposal early August 2026. We would value a 30-minute call to scope fit. **Contact:** Shahin Mohammadi, mohammadi@cytognosis.org.
