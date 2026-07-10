# ARPA-H IGoR at a glance: program, technical areas, and our team

**A skim-friendly briefing for collaborators new to the program.** Contact: Shahin Mohammadi, Cytognosis Foundation, mohammadi@cytognosis.org.

## The overall goal

**IGoR** (Integrated Generation of Robust biomedical knowledge; ARPA-H-SOL-26-155) will fund about **three teams** to build a **closed loop** that produces validated biomedical knowledge at least **10x faster** than today. Instead of one-off studies, a model predicts, an AI engine designs the next experiment, validated labs run it, and the results flow straight back into the model.

**The loop:** **TA1** model → **TA2** designs the highest-value experiment → **TA3** portable protocol → **TA4** validated labs execute → model-ready data back to **TA1**.

## The four Technical Areas

| TA | Goal | Core objectives |
|---|---|---|
| **TA1, Comprehensive disease models** | A mechanistic, multiscale, causal model of a disease that updates as new data arrive | Capture molecular-to-phenotype causality; quantify its own uncertainty; ingest new results automatically rather than being rebuilt by hand |
| **TA2, New Science Engine** | An AI system that designs the highest-value next experiment by interrogating the model (not just the literature) | Rank candidate experiments by value of information; generate and tournament testable hypotheses; pre-screen designs by simulation. Explicitly not a wrapper around a single language model |
| **TA3, Interoperable experimental procedures** | Open, portable protocols so an experiment transfers between labs as easily as a data file | Machine-readable protocol plus execution record and provenance; specialize one protocol out to many instruments and labs |
| **TA4, Experiment marketplace** | A set of validated laboratories that execute protocols and return model-ready data | At least two labs; multiple measurement modalities; demonstrated cross-laboratory reproducibility |

## The interfaces (the seams that make the loop work)

These hand-offs, not just the four areas, are what IGoR rewards:

- **TA1 to TA2:** the model exposes its uncertain parameters and conflicting edges; the engine targets exactly those.
- **TA2 to TA3:** the chosen experiment compiles into a portable, scheduled, machine-readable protocol.
- **TA3 to TA4:** the same protocol executes consistently across different validated laboratories.
- **TA4 to TA1:** results are ingested automatically and update the model, closing the loop and starting the next, faster cycle.

## Program structure and timeline

- **About five years, three phases** (roughly **18, 18, and 24 months**), each phase-gated on quantitative milestones.
- **Marquee milestones:** experimental cycle time at least **4x** faster by Phase II and **10x** by Phase III; cross-laboratory concordance rising from about **80% to 90%**.
- Funded through an **Other Transaction (OT) agreement**, which is more flexible than a standard federal grant on intellectual property and data rights.
- **Selection:** a short **Solution Summary** first, then a full proposal. **Solution Summary due June 25, 2026; full proposal early August 2026.**

## Our team and lead: PsychIGoR

We propose as **Team PsychIGoR** (psychiatry plus IGoR), reflecting our psychiatric-disease pilot.

| Role | Who |
|---|---|
| Prime and Principal Investigator | IPAI, Purdue University; Ananth Grama |
| TA1 and TA2 co-leads (disease model, AI engine) | Cytognosis Foundation (Shahin Mohammadi, sub-awardee) and IPAI, Purdue |
| Clinical and translational | W. Brad Ruzicka, McLean Hospital |
| TA4 academic experimental arm | Matt Tegtmeyer lab, Purdue (iPSC-neuron wet-lab experiments; fixed-cell high-plex readouts: RNA ~350-plex, protein ~50-plex, Cell-Painting-style morphology, in-situ CRISPR-guide sequencing) |
| TA4 industry arm | Cellanome (live-cell imaging, same-cell scRNA-seq, Perturb-LINK CRISPR; advancing) |
| Computational morphology and imaging models | Anne Carpenter (IPAI/Purdue; interpretable models; no wet bench) |
| Project manager | Patricia Purcell |
| Software and systems architect | Elham Jebalbarezi Sarbijan, IPAI/Purdue (tentative) |
| TA3 interoperable protocols | SIFT; Daniel Bryce (lead), Robert Goldman (advisory) |
| TA4.2 sequencing and bioinformatics | Illumina (optional / TBD) |

**Our pilot.** Psychiatric disease (**schizophrenia, extending to bipolar disorder**), grounded in **penetrant genetic forms** (such as the **22q11.2 deletion**) modeled in **iPSC-derived neurons**, read out by **transcriptomics, morphology, and single-cell calcium imaging**. Penetrant genetics give the closed loop strong, causal, in-dish signal to learn from.

**TA4 structure.** Two experimental arms satisfy the program's requirement of at least two validated laboratories. The academic arm is Matt Tegtmeyer's Purdue lab, which runs all wet-lab experiments using fixed-cell high-plex readouts (RNA ~350-plex, protein ~50-plex, Cell-Painting-style morphology, in-situ CRISPR-guide sequencing). The industry arm is Cellanome, providing live-cell imaging and same-cell scRNA-seq on the R3200. Anne Carpenter contributes computational morphology and imaging models as the common analysis layer across both arms; she does not operate a wet bench.

**What we are assembling.** TA3 interoperable protocols and the TA4 validated-laboratory team, with real budget attached.

**Contact.** Shahin Mohammadi, Cytognosis Foundation, mohammadi@cytognosis.org.
