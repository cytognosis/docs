# Cytognosis: Strategy + Grant-Alignment Map

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: leadership, grant team
> **Tags**: `funding`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

**Date:** 2026-06-11 · Reading time: ~8 min · Birds-eye reference for aligning each application to both our direction and the funder's values. Built from the current strategy files and a live verification of each funder. Strategy, not legal/financial advice.

> **If you only read one thing:** There is one **framing fork**. Biswas hears the **health** story (open AI model for bipolar biotyping). Coefficient (both programs), LTFF, and Manifund hear the **AI-safety** story (Cytonome on-device safety layer, cognitive liberty, data capture). It is the **same work**, told in the vocabulary each funder already values. Keep the two families in separate documents.

---

## 1. The platform in three tracks (so every pitch traces back here)

| Track | Plain meaning | Funds via |
|---|---|---|
| **Cytoverse** (the Map) | Open AI foundation model that replaces disease labels with continuous health coordinates; first release = neuro/psych (14 disorders) | Biswas, AWS Imagine, NIH TMM, Templeton, OS4LS, IGoR TA1 science |
| **Cytoscope** (the Sensor) | Wearable that locates you on that map (fNIRS/DCS + ultrasound, with Herve); open UBAP protocol | NSF X-Labs Psychoscope, NIH BBQS, Smart Health |
| **Cytonome / Yar** (the Navigator) | On-device causal AI + safety layer (Cytoplex); Yar = neurodivergent app; the **AI-safety primitives** live here | Coefficient (CDT + Capacity), LTFF, Manifund, YC, One Mind Accelerator |

**Open-core line:** the Foundation keeps the open map, the open sensor protocol, and the safety primitives; the future PBC takes the hardware and the consumer app.

---

## 2. The five scientific threads, and which grant each feeds

| Thread | Feeds |
|---|---|
| Dimensional biotyping / Cytoverse model | Biswas, AWS, NIH TMM, IGoR TA1, Templeton |
| **BDNF/TrkB bipolar proof-of-concept** (McLean published + MtSinai validation) | IGoR (22q11DS anchor), ARPA-H EVIDENT/HSF, Baszucki, the bipolar paper |
| **Factorized-PRS** (CONFIDENTIAL moat) | Platform only; **keep off every application and partner doc** |
| **Cellular micro-to-meso causal bridge** | IGoR TA1/TA2 (the differentiator vs HSF), Cellanome work |
| On-device causal AI + ND user research | Coefficient, LTFF, Manifund, Yar/PBC funders |

The threads converge: the bipolar paper establishes the axes, the foundation model operationalizes them, the cellular bridge gives the gene-to-circuit ladder IGoR needs, and Yar generates the data that trains the next model. The factorized-PRS is the moat underneath, and it stays private.

---

## 3. The Foresight alignment method (our reusable template)

This is the method to reuse on all four AI-safety applications:

1. **Lead with the funder's exact concern**, not our science (e.g., centralized-LLM capture of cognitive data).
2. **Translate the work into their vocabulary** without changing a single deliverable.
3. **Anchor the ask in already-shipped proof** (Cytoplex-Lite, 93 passing safety tests, the working on-device voice loop) to convert "startup risk" into "de-risked."
4. **List every concurrent application** with a one-line non-overlap note (kills the double-funding worry).
5. **Keep the science accurate but funder-filtered** ("dimensional biotyping" becomes "recovering continuous biological axes").

---

## 4. Per-application alignment plan (the 5)

| # | Opportunity | Recipient | Framing to use | Draft status | What it needs |
|---|---|---|---|---|---|
| 1 | **Biswas Fast Grants** | Org ($100K) | **Health** (open biomodel, bipolar biotyping) | Near-final | Add 2-3 paper links + Scholar URL; **do not add AI-safety language** |
| 2 | **Coefficient Career Transition** | **You** ($165K) | AI-safety pivot + lived experience | Near-final | Jose→Brad; tie the lived-experience to the data-capture risk |
| 3 | **EA LTFF** | You or org (~$75-125K) | AI-safety (cognitive manipulation + biotype capture) | Near-final | Jose→Brad; fix Foresight-status line; **decide ask size** |
| 4 | **Manifund** | Org/you ($15-30K) | AI-safety, one concrete deliverable | **No draft** | Build from scratch; **decide deliverable + accept public visibility** |
| 5 | **Coefficient Capacity Building** | Org (~$175K) | AI-safety **infrastructure + talent pipeline** | Near-final | Fill address; add talent-pipeline paragraph; coordinate PI effort with #2 |

**Deadlines:** Biswas is the only hard wall (**~Jun 15**, confirm). The other four are rolling (Coefficient ~6 weeks, LTFF 2-4 weeks, Capacity ~3 months, Manifund ~2 weeks once a regrantor commits).

---

## 5. Decisions to make before writing (where more than one path exists)

1. **LTFF ask size.** Mainline **$125K** (full sprint incl. hardware) vs minimal **$75K** (software-only).
   - $75K pros: LTFF median is ~$25K and their precedent for applied neuroscience is thin, so a tighter software-only ask is more fundable and faster.
   - $125K pros: funds the whole defensible-primitives sprint in one shot.
   - **Lean:** ask $75K software-only as the headline, list $125K as the "with hardware" stretch.

2. **Manifund: go or skip, and what deliverable.** The post is **public and permanent**, so its AI-safety framing will sit next to our health-facing brand forever.
   - **Lean:** go, but scope it narrowly to one open-source artifact (e.g., the Cytoplex safety-boundary release or a post-quantum-crypto reference implementation), $15-30K, so the public framing is a clean "we shipped a safety primitive," not an org pitch.

3. **Coefficient: submit both programs?** CDT funds **you** personally ($165K); Capacity Building funds the **org** ($175K, no clean salary line).
   - **Lean:** yes, submit both, with the explicit PI-effort coordination clause so no reviewer sees double-funded PI time. CDT is your cleanest personal-income path; Capacity Building builds the org.

4. **Foresight status.** Three drafts cite Foresight as concurrent funding. Confirm whether it was **declined or still pending** so we state it accurately (reviewers can check).

5. **Jose → Brad.** Three drafts (CDT, LTFF, Capacity) still list Jose Davila-Velderrain where **Brad Ruzicka** is now Co-Lead. Confirm and we update everywhere.

---

## 6. IGoR TA1 direction: my recommendation

**Recommendation: stay psychiatric, anchored on 22q11DS leading to idiopathic schizophrenia, with the BDNF/TrkB bipolar bridge.** Treat neurodegeneration as a possible later generalization arm, not the core.

**Why this also gives you what you liked about the neurodegeneration idea.** Your reasons for neurodegeneration were clean molecular signatures and a clean rare-familial plus common-sporadic structure for cellular and clinical modeling. **22q11DS delivers exactly that inside psychiatry:** it is a rare, high-penetrance CNV (the cleanest genotype-to-circuit chain in psychiatry, with an existing NeuroPainting cellular atlas) that generalizes to common, sporadic schizophrenia. So you get the modeling clarity without leaving the field where all your assets live.

**What switching to neurodegeneration would cost.** It would strand the published McLean schizophrenia paper, the in-progress bipolar PoC, the factorized-PRS moat (validated on psychiatric data), the BDNF-to-EVIDENT two-vector ARPA-H play, the 22q11DS founder narrative, and your entire clinical network (Brad, Panos, Manolis, the Smoller target). Your 2019 AD Nature paper buys credibility, but credibility is not a built program.

**The one honest caveat:** psychiatric common-variant effect sizes are noisier than familial neurodegeneration, so TA4 perturbation phenotypes are harder. 22q11DS is the answer to that too (large-effect, high-penetrance), which is why it should be the Phase I/II exemplar. This is a real strategic fork, so it is your call; my recommendation is psychiatric-with-22q11DS, and I will frame IGoR that way unless you say otherwise.

---

## 7. Next step

The writing is now small for four of five: Biswas needs two inputs from you, and CDT/LTFF/Capacity need targeted edits plus the decisions above; only Manifund is net-new. Given those inputs and decisions, the sprint order is: **Biswas first** (deadline), then **CDT** (your income), then **LTFF** and **Capacity** (reuse the AI-safety frame), then **Manifund** (smallest, build last). I recommend doing the actual rewrites in a focused session with the grant-writing, science, and brand skills loaded, using this map as the brief.
