# Cytognosis x IGoR: TA1 Partner Brief (DRAFT content)

> Partner-facing. 1–2 pages. Proprietary factorized-PRS method intentionally omitted; described only as interpretable "disease axes." For sharing with prospective TA2/TA3/TA4 partners.

---

## A closed-loop research engine for complex disease: and where you fit

**The opportunity.** ARPA-H IGoR (ARPA-H-SOL-26-155) will fund roughly three integrated teams to build an AI-enabled, interoperable research ecosystem that generates validated biomedical knowledge at least 10x faster than conventional research. Each team must cover all four Technical Areas as one performer, over five years. We are assembling that team around a mechanistic disease model for **schizophrenia**, extending to **bipolar disorder** in Phase III. This brief describes what Cytognosis contributes as the **TA1 (Comprehensive Disease Models)** lead, and how TA2, TA3, and TA4 partners connect to it.

**The loop.** TA1 (our disease model) identifies the knowledge gaps that matter most → TA2 designs the experiment that best resolves each gap → TA3 encodes it as an instrument-agnostic protocol → TA4 laboratories execute it and return data → TA1 updates. The interfaces between areas matter as much as the parts.

## What Cytognosis builds as TA1

**A mechanistic, multiscale, causal disease model.** Most "virtual cell" and perturbation models predict the effect of an experimenter's genetic or chemical intervention. We invert that frame: we model **disease itself, and disease-associated genetic variation, as the causal perturbation on cell state**, and we represent its effect as sparse, interpretable shifts in the activity of biological processes ("disease axes"). This is physically grounded, mechanistic AI rather than a correlational embedding, which is what lets the model be queried, validated, and updated.

**Network and pathway modeling.** We build the model on a curated multiscale interaction network, including protein-protein, signaling, regulatory, and cell-type-specific edges, with a coverage map that tells the system which processes are well supported by evidence and which are not. That coverage map is what TA2 uses to target experiments at the highest-value gaps.

**Joint cellular and clinical representation.** We measure every signal, whether from a patient cohort or a dish, as a shift in the same pathway space relative to a matched control. Aligning induced (cellular) and natural (clinical) signals in one space is how we separate clinically relevant disease biology from artifacts of a culture system, a failure mode of in-vitro-only pipelines.

**Data we bring.** A single-cell multi-cohort schizophrenia atlas (co-led by our team), PsychENCODE single-cell and regulatory-network resources, PGC schizophrenia genetics, target evidence from the Open Targets Platform, and a scholarly knowledge graph for literature grounding. Targets that emerge carry **human genetic support, which roughly doubles to triples the probability of clinical success.**

## Where partners plug in

- **TA2: New Science Engine (agentic experiment design).** Turn TA1's gaps and uncertainties into ranked, high-value experiments with explainable reasoning. We seek a partner with a strong agentic-science platform to co-lead this with us.
- **TA3: Interoperable protocols.** Translate each experiment design into a layered, open protocol (intent → protocol → calibration → hardware) that any qualified lab can run. We seek a partner with deep protocol-representation and automated-planning expertise.
- **TA4: Validated-lab marketplace (≥2 labs).** Execute protocols and return high-quality, model-ready data across complementary modalities: live-cell imaging with same-cell sequencing, optical and morphological screening, and high-throughput sequencing. We seek laboratories that can validate to shared concordance standards.

## Why this team, why now

We pair an atlas-scale, mechanistically grounded disease model with the engineering and laboratory partners needed to close the loop. The disease focus plays to documented strengths: our clinical multi-cohort work and a tractable, high-penetrance cellular model of schizophrenia (the 22q11.2 deletion) with experimentally validated cell-type signatures. Everything we build is released open-source under permissive licenses, consistent with IGoR's open-science goals and Cytognosis's nonprofit mission, with narrowly scoped proprietary methods clearly marked.

**Let's talk about your role on the team.** Contact: Shahin Mohammadi, Founder and CEO, Cytognosis Foundation (mohammadi@cytognosis.org).

---

### Selected references
- Bunne C, et al. How to build the virtual cell with artificial intelligence. *Cell* 2024;187:7045–7063.
- Ruzicka WB, **Mohammadi S**, et al. Single-cell multi-cohort dissection of the schizophrenia transcriptome. *Science* 2024;384:eadg5136.
- Tegtmeyer M, et al. Cell-type-specific morphological and molecular signatures of the 22q11.2 deletion. *Nat Commun* 2025;16:6332.
- Minikel EV, et al. Refining the impact of genetic evidence on clinical success. *Nature* 2024;629:624–629.
- Trubetskoy V, et al. Mapping genomic loci implicates genes and synaptic biology in schizophrenia. *Nature* 2022;604:502–508.
