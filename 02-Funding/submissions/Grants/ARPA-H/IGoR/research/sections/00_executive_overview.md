## 00. Executive overview

> [!TIP]
> **If you read one thing:** we propose the only IGoR TA1 that treats **disease-associated genetic variation as the causal perturbation operator** on a self-updating, multiscale, mechanistic model of cellular biology, then drive a non-LLM-wrapper reasoning engine (TA2) and a validated execution loop (TA3, TA4) from it. Section 10 states the thesis; sections 30 to 34 state how we build it.

**What this document is.** This is the consolidated scientific and technical source of record for the IGoR proposal. It holds two things: the **external methods landscape** (sections 20 to 23) and **our key contributions** as they have stabilized across proposal variants (sections 30 to 70). It is the master that the one-pager, Solution Summary, and full proposal are refined from.

**The program in one paragraph.** ARPA-H IGoR (ARPA-H-SOL-26-155) funds approximately three teams over five years to build a closed loop: TA1 mechanistic disease models, a TA2 New Science Engine that finds gaps and designs experiments, a TA3 interoperable protocol stack, and a TA4 validated-lab marketplace. The marquee metric is a **10x reduction in experimental cycle time** by Phase III. Full solicitation truth lives in `../materials/IGoR_Comprehensive_Reference.md`.

**Our approach in five moves.**

1. **TA1, four pillars** (section 30): a cell-type-aware mechanistic network; a causal generative model in which genotype acts as a sparse soft intervention; a joint cellular and clinical shift-space; and ontology-conditioned experiment design. Required properties: modular, mechanistic, multiscale, verifiable.
2. **The crown-jewel factorization** (section 31, proprietary): patient genetic variation factorized into sparse, pathway-disentangled, transdiagnostic axes that double as candidate biotypes.
3. **TA2 New Science Engine** (section 33): a hypothesis tournament, mechanistic-model-grounded retrieval-augmented planning, and test-time validation scaling. Explicitly not a wrapper around a frontier LLM.
4. **TA3 and TA4 execution** (section 34): an open layered protocol stack plus a validated multi-lab marketplace with two experimental arms: Matt Tegtmeyer's lab at Purdue (academic, all wet-lab experiments, Element AVITI24 / Teton CytoProfiling) and Cellanome (industry, R3200 live-cell + Perturb-LINK), with Anne Carpenter providing computational morphology/imaging models across both arms. Illumina provides perturbation-scale sequencing as Lab 3.
5. **Disease strategy** (section 40): 22q11.2 deletion syndrome as the Phase I cellular anchor, idiopathic schizophrenia as the required second area, with a cautious bipolar extension.

**Where the proposal stands (2026-06-12 drafts).** A **7-performer consortium at $50M**, **IPAI/Purdue as prime** with Ananth Grama as PI, Cytognosis and IPAI jointly leading TA1 and TA2. Section 60 holds the team and cost model; section 70 traces how we got here; section 90 lists what is still open.

> [!CAUTION]
> **Restricted sections (31, 32, 41) are internal only.** They contain the proprietary factorization, a perturbation model under anonymous review, and a personal-genomic Phase I anchor. They appear only in the `internal` build and must never enter partner-facing or public submission text.

### How to navigate

| If you want | Read |
|---|---|
| The one-line bet and why it is novel | Section 10 |
| What others have built and where the gap is | Sections 20 to 23 |
| What we build, pillar by pillar | Sections 30, 33, 34 |
| Disease rationale and evidence | Section 40 |
| Targets we must hit | Section 50 |
| Who is on the team and what it costs | Section 60 |
| How the proposal evolved | Section 70 |
| What is unresolved before submission | Section 90 |
