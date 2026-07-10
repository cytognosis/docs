# SIFT capabilities analysis (TA3, and TA2) for IGoR

**Date:** 2026-06-14. **Source:** SIFT lightning-talk slide (IGoR Proposers' Day) plus the cited literature and the LabOP site. **POCs:** Daniel (Dan) Bryce (dbryce@sift.net), Robert Goldman (rpgoldman@sift.net). SIFT, Minneapolis MN and Dallas TX.

> [!TIP]
> **Bottom line:** anchor SIFT as the **TA3 lead (LabOP)**, the single strongest open interoperable-protocol option we have. **Invest additionally in a scoped TA2 planning-and-scheduling contribution** (their Bayesian value-of-information experiment ranking complements our model-grounded engine and strengthens the TA2-to-TA3 interface, which IGoR scores). Treat their **closed-loop DBTL** work as track-record credibility, not a capability to build on, because it is synthetic-biology specific.

## What the slide claims (parsed)

- **TA3, LabOP Open Protocol Representation [2][4]:** co-developed LabOP (Laboratory Open Protocol language), layered, open, interoperable; a portable execution engine runs protocols across heterogeneous lab architectures.
- **TA2, Planning and Scheduling [5][6][4]:** human-specified and fully automated experiment and campaign planning; **Bayesian Value-of-Information to rank experiment candidates**; LLM-augmented optimizing and satisficing planning/scheduling; LLM coding agents for automated plan-model generation.
- **Closed-Loop DBTL Execution [1][7][8][3]:** a Round Trip pipeline (design to execute to analyze, end to end); high-throughput yeast logic-circuit replication across platforms; AutoGater, ML-based flow-cytometry gating for QC.

## TA3: LabOP (strong fit, anchor here)

**What it is.** LabOP (formerly PAML, the Protocol Activity Markup/Modeling Language) is an **open specification for laboratory protocols** that solves interchange across scale, labware, instruments, and automation. It is built on **UML activity models, SBOL3 RDF, Autoprotocol, Aquarium, and the PROV provenance ontology**.

**Key principles and terminology (use these in the proposal and the call):**

- **Protocol primitives:** an extensible library capturing control and data flow, from calibration and culturing to industrial control.
- **Records of execution and data, with provenance:** LabOP represents not only the protocol but the **execution record and resulting data** (PROV), which is exactly the metadata layer IGoR TA3 requires.
- **Specialization:** one protocol exports to multiple execution backends, **Autoprotocol, OpenTrons OT2, SiLA-based automation, Echo, and human-readable Markdown**, which is the "transfers between labs like a data file" property.
- **Tooling:** the `labop` Python library (program, serialize to RDF, execute in native UML-activity semantics, specialize, integrate instruments) and the `laboped` low-code web editor; governed by the open **Bioprotocols Working Group**.

**Mapping to our TA3 layered stack:** LabOP's intent-level primitives map to our **intent and protocol** layers; SBOL/identifier grounding and PROV map to **calibration and metadata**; specialization maps to the **hardware** layer. This is a clean, credible, open foundation, and it is genuinely the leading option (stronger than a bespoke schema, and more mature than Transfyr for protocol execution).

## TA2: planning and scheduling (worthwhile scoped add-on)

**What it is and how legit.** Well-published, real work: a **Bayesian model for experiment choice** (Goldman, Trivedi, Bryce; ref 4), **hierarchical experiment planning** (Kuter, Goldman, Bryce, Beal, ref 5), and **formalizing sample-transformation plans** (ref 6), now augmented with LLM planning and coding agents. Venues include AAAI symposia and ACS Synthetic Biology.

**Fit with our engine.** Our TA2 New Science Engine chooses the **highest-value-of-information experiment** from the TA1 causal model. SIFT's **Bayesian value-of-information ranking** and **plan-and-schedule then compile-to-protocol** capability are a natural complement: our engine decides **what** to test and why; their planner turns that into a **scheduled, resource-allocated, executable plan** that hands off to LabOP (TA3). That is precisely the TA2-to-TA3 interface IGoR rewards.

**Recommendation:** **yes, invest in a scoped TA2 planning-and-scheduling role for SIFT**, with **Cytognosis remaining TA2 lead** (the disease-model-grounded hypothesis engine stays ours; SIFT contributes the planning/scheduling and plan-to-protocol layer). This is additive, not a distraction, and it tightens the TA2/TA3 seam.

**Caveat (confirmed 2026-06-18; SIFT accepted):** their planning track record is in **synthetic biology**; confirmed generalization to mammalian iPSC and imaging/scRNA-seq/calcium-imaging workflows is the key technical validation target for Phase I.

## Closed-loop DBTL (credibility, not a core need)

Round Trip (ref 7, ACS Synth Biol 2022), AutoGater (ref 3, Sci Reports 2024), Cummins et al. (ref 1, 2023), and Goldman et al. (ref 8, 2022) are strong **automation and reproducibility** results, but in the **synthetic-biology domain** (yeast logic circuits, flow-cytometry gating). AutoGater's flow-cytometry QC is tangential to our imaging, scRNA-seq, and calcium-imaging readouts. **Use these as evidence of SIFT's automation and reproducibility pedigree; do not scope them as a capability we depend on.**

## How much to invest, and versus other options

- **TA3:** SIFT **confirmed as TA3 lead** (Dan Bryce formally accepted 2026-06-18). Robert Goldman advisory (~30% shared SIFT FTE). Tim Fallon (UCSD) can add as an academic co-contributor if useful; not required.
- **TA2:** scoped Bayesian VOI planning/scheduling layer under Cytognosis TA2 lead. Confirmed as part of SIFT engagement. Cytognosis remains TA2 lead.
- **Closed-loop DBTL:** cite as track record only.

## Talking points for the call

- Lead with LabOP for TA3, using the terminology above (primitives, specialization, execution records and PROV, SBOL3/UML).
- Float the TA2 planning/scheduling and value-of-information complement, framed as a scoped contribution under our TA2 lead.
- Surface the synthetic-biology to mammalian-disease generalization as the key technical question.
- Keep it capability-focused; do not name TA4 candidates; route any NDA through Duane.

## Citations

- LabOP site: https://bioprotocols.github.io/labop ; GitHub: https://github.com/bioprotocols/labop
- [2] Bartley et al., Building an Open Representation for Biological Protocols (PAML to LabOP). *ACM JETC* 19(3), 2023. doi:10.1145/3604568 (bioRxiv 2022.07.05.498808).
- [4] Goldman, Trivedi, Bryce et al., A Bayesian Model for Experiment Choice in Synthetic Biology. AAAI Fall Symp.
- [5] Kuter, Goldman, Bryce, Beal, XP: Experiment Planning for Synthetic Biology. 2018.
- [6] Bryce, Goldman, Beal et al., Formalizing Sample Transformation Plans. AAAI Fall Symp.
- [7] Bryce et al., Round Trip: Automated Pipeline for Experimental Design, Execution, and Analysis. *ACS Synth Biol* 2022. doi:10.1021/acssynbio.1c00305.
- [1] Cummins et al., Robustness and reproducibility of synthetic logic circuit designs using a DBTL loop. *Synth Biol* 2023.
- [3] Eslami, Moseley, Eramian, Bryce, Haase, AutoGater. *Sci Reports* 2024.
- [8] Goldman, Moseley, Roehner, Cummins et al., Highly-automated high-throughput replication of yeast-based logic-circuit assessments. *Synth Biol* 2022.
