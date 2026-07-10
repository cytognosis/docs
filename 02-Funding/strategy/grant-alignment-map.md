# Grant-Alignment Map (technical)

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: leadership, grant team
> **Tags**: `funding`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

> **Variants**: Technical (this doc) - Readable (grant-alignment-map.md in Obsidian vault: 02-Funding/strategy/) - Agent (grant-alignment-map_prompt.md)

> **Status:** Active · **Date:** 2026-07-01 · **Author:** Funding & Grants (canonicalized from `Grants/01-strategy/funding/Cytognosis_Strategy_and_Grant_Alignment_Map_2026-06-11.md`, 2026-06-11)
> **Canonical home:** `docs/02-Funding/strategy/grant-alignment-map.md` · **Variants:** [readable](grant-alignment-map.md) · [agent](grant-alignment-map_prompt.md)
> **Scope note:** This is the funder-facing grant-alignment reference. The platform strategy master is owned by Strategic Planning (`01-Strategy`); this doc maps that strategy onto funders. Strategy, not legal or financial advice.

**If you only read one thing:** There is one **framing fork**. Biswas hears the **health** story (open AI model for bipolar biotyping). Coefficient (both programs), LTFF, and Manifund hear the **AI-safety** story (Cytonome on-device safety layer, cognitive liberty, data capture). It is the **same work**, told in the vocabulary each funder already values. Keep the two families in separate documents.

## 1. Platform in three tracks

Every pitch traces back to one of three tracks, so a reviewer can place the ask inside a coherent program.

| Track | Plain meaning | Funds via |
|---|---|---|
| **Cytoverse** (the Map) | Open AI foundation model that replaces disease labels with continuous health coordinates; first release is neuro and psych (14 disorders) | Biswas, AWS Imagine, NIH TMM, Templeton, OS4LS, IGoR TA1 science |
| **Cytoscope** (the Sensor) | Wearable that locates a person on that map (fNIRS/DCS plus ultrasound, with Hervé); open UBAP protocol | NSF X-Labs Psychoscope, NIH BBQS, Smart Health |
| **Cytonome / Yar** (the Navigator) | On-device causal AI and safety layer (Cytoplex); Yar is the neurodivergent app; the **AI-safety primitives** live here | Coefficient (CDT and Capacity), LTFF, Manifund, YC, One Mind Accelerator |

**Open-core line:** the Foundation keeps the open map, the open sensor protocol, and the safety primitives; the future PBC takes the hardware and the consumer app.

## 2. The five scientific threads and the grants each feeds

| Thread | Feeds |
|---|---|
| Dimensional biotyping / Cytoverse model | Biswas, AWS, NIH TMM, IGoR TA1, Templeton |
| **BDNF/TrkB bipolar proof-of-concept** (McLean published plus Mount Sinai validation) | IGoR (22q11DS anchor), ARPA-H EVIDENT/HSF, Baszucki, the bipolar paper |
| **Factorized-PRS** | Platform only. See the confidentiality rule below. |
| **Cellular micro-to-meso causal bridge** | IGoR TA1/TA2 (the differentiator versus HSF), Cellanome work |
| On-device causal AI plus neurodivergent user research | Coefficient, LTFF, Manifund, Yar/PBC funders |

The threads converge: the bipolar paper establishes the axes, the foundation model operationalizes them, the cellular bridge gives the gene-to-circuit ladder IGoR needs, and Yar generates the data that trains the next model.

> [!CAUTION]
> **CONFIDENTIAL, platform moat: factorized-PRS stays off every application and every partner document.** It is validated on psychiatric data and is the underlying moat, not a deliverable. Do not describe it, name its mechanism, or cite it in any external funding or partner material.

## 3. The Foresight alignment method (reusable template)

Reuse this on all four AI-safety applications:

1. **Lead with the funder's exact concern**, not the science (for example, centralized-LLM capture of cognitive data).
2. **Translate the work into their vocabulary** without changing a single deliverable.
3. **Anchor the ask in already-shipped proof** (Cytoplex-Lite, 93 passing safety tests, the working on-device voice loop) to convert perceived startup risk into de-risked execution.
4. **List every concurrent application** with a one-line non-overlap note, which removes the double-funding concern.
5. **Keep the science accurate but funder-filtered** ("dimensional biotyping" becomes "recovering continuous biological axes").

## 4. Per-application alignment plan

| # | Opportunity | Recipient | Framing | Draft status | What it needs |
|---|---|---|---|---|---|
| 1 | **Biswas Fast Grants** | Org ($100K) | **Health** (open biomodel, bipolar biotyping) | Near-final | Add 2-3 paper links plus Scholar URL; do not add AI-safety language |
| 2 | **Coefficient Career Transition** | Individual (rate pending comp finalization) | AI-safety pivot plus lived experience | Near-final | Update Co-Lead to Brad; tie lived experience to the data-capture risk |
| 3 | **EA LTFF** | Individual or org (~$75K to $125K) | AI-safety (cognitive manipulation plus biotype capture) | Near-final | Update Co-Lead to Brad; fix Foresight-status line; decide ask size |
| 4 | **Manifund** | Org or individual ($15K to $30K) | AI-safety, one concrete deliverable | No draft | Build from scratch; decide deliverable and accept public visibility |
| 5 | **Coefficient Capacity Building** | Org (~$175K) | AI-safety infrastructure plus talent pipeline | Near-final | Fill address; add talent-pipeline paragraph; coordinate PI effort with #2 |

**Deadlines:** Biswas is the only hard wall (verify the mid-June date; it may have passed). The other four are rolling (Coefficient ~6 weeks, LTFF 2-4 weeks, Capacity ~3 months, Manifund ~2 weeks once a regrantor commits).

## 5. Decisions before writing

1. **LTFF ask size.** Mainline $125K (full sprint including hardware) versus minimal $75K (software-only). LTFF median is near $25K and its precedent for applied neuroscience is thin, so a tighter software-only ask is more fundable. **Lean:** headline $75K software-only, list $125K as the with-hardware stretch.
2. **Manifund: go or skip, and what deliverable.** The post is public and permanent. **Lean:** go, scoped narrowly to one open-source artifact (the Cytoplex safety-boundary release or a post-quantum-crypto reference implementation), $15K to $30K.
3. **Coefficient: submit both programs?** CDT funds the individual; Capacity Building funds the org. **Lean:** submit both, with an explicit PI-effort coordination clause so no reviewer sees double-funded PI time.
4. **Foresight status.** Confirm whether Foresight was declined or is still pending so concurrent-funding lines are accurate.
5. **Co-Lead update.** Replace Jose Davila-Velderrain with Brad Ruzicka everywhere (CDT, LTFF, Capacity).

## 6. IGoR TA1 direction

**Recommendation:** stay psychiatric, anchored on 22q11DS leading to idiopathic schizophrenia, with the BDNF/TrkB bipolar bridge. Treat neurodegeneration as a possible later generalization arm, not the core.

**Rationale.** 22q11DS is a rare, high-penetrance CNV (the cleanest genotype-to-circuit chain in psychiatry, with an existing NeuroPainting cellular atlas) that generalizes to common, sporadic schizophrenia. It delivers the clean molecular signatures and the rare-familial plus common-sporadic structure that motivated the neurodegeneration idea, without leaving the field where the assets live. Switching to neurodegeneration would strand the published McLean schizophrenia paper, the in-progress bipolar proof-of-concept, the psychiatric-validated moat, the BDNF-to-EVIDENT ARPA-H play, the 22q11DS founder narrative, and the clinical network (Brad, Panos, Manolis, the Smoller target).

**Caveat.** Psychiatric common-variant effect sizes are noisier than familial neurodegeneration, so TA4 perturbation phenotypes are harder; 22q11DS (large-effect, high-penetrance) is the answer and should be the Phase I/II exemplar.

## 7. Sequence

Small writing remains for four of five. Sprint order: **Biswas** first (deadline), then **CDT** (personal income), then **LTFF** and **Capacity** (reuse the AI-safety frame), then **Manifund** (smallest, build last). Do the rewrites in a focused session with the grant-writing, science-platform, and brand-identity skills loaded, using this map as the brief.
