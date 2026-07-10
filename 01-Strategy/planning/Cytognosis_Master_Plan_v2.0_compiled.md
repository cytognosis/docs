# Cytognosis Foundation · Master Strategic Plan

**Version 2.0 · May 2026 · Compiled single-document edition**

**Author:** Shahin Mohammadi · **Compilation date:** 2026-05-08


This is a compiled single-document edition of the Cytognosis Foundation Master Strategic Plan v2.0. The source-of-truth lives as a set of interconnected markdown files in `master_plan/`; see `README.md` in that folder for the modular index. Diagrams are embedded as rendered PNG images.


---



# Section: 00_executive_summary.md


# Executive Summary

**Cytognosis Foundation · Master Strategic Plan v2.0 · May 2026**

## The problem we exist to solve

Modern medicine treats symptoms after damage occurs. Three structural blindspots prevent the shift to proactive health:

- **Mechanistic blindness.** Treating clusters, not biology. Depression has 4+ molecular subtypes; first-line antidepressants fail 30 to 60% of patients. Autoimmune diagnosis takes 4.5 to 7 years across 4+ specialists.
- **Temporal blindness.** Alzheimer's pathology begins decades before memory loss; cancer mutations circulate years before tumors form; type 2 diabetes is 50 to 80% reversible at prediabetes but under 10% after clinical onset.
- **Complexity blindness.** Continuous glucose monitoring revealed that identical meals produce dramatically different metabolic responses across people. We have not generalized that revolution beyond a single molecule.

These are not three problems. They are one structural failure: medicine has no platform that maps disease at its molecular roots, tracks trajectory in real time, and guides intervention before pathology becomes irreversible.

## What we are building

A **cellular intelligence platform** that we call **GPS for Human Health**. It has three components, in plain language:

| Component | Role | What it produces |
|---|---|---|
| **Cytoverse** · the **map** | Continuous, multimodal coordinates for human biology across micro (molecules + cells), meso (connectomes + circuits), and macro (behavior + phenotype) scales | A universal health-state coordinate system that replaces categorical diagnoses with quantitative, trackable position |
| **Cytoscope** · the **sensor** | Programmable biosensors plus wearables that triangulate each person's coordinates on the Cytoverse map in real time, across molecular, connectomic, and phenotypic modalities | Continuous, multivariate biological data for any individual |
| **Cytonome** · the **navigator** | Privacy-first edge AI that converts real-time coordinates into causally grounded recommendations: defensive (what to avoid), corrective (how to reverse), supportive (how to cope) | A personal, on-device coach that protects healthspan across decades |

Our pilot indication is **mental health**, where the absence of biotyping creates the largest gap between current standard of care (one-size-fits-all symptom-cluster diagnosis) and what cellular intelligence enables (precise stratification by mood, thought, anxiety, attention axes grounded in molecular and connectomic signatures).

## Three horizons in one diagram

![Diagram 1 from 00_executive_summary](/tmp/master_plan_compile/diagrams/00_executive_summary__1.png)


## What is new in this version

Five updates that change how we operate in the next 24 months.

**Bifurcation marker at 36 months.** All work, models, and data produced in the first 36 months remain open under Apache 2.0 and CC BY 4.0, owned by the Foundation, released annually with public versioning, and adoptable in clinical care without licensing barriers. From the start of our clinical study (Year 4), the proprietary continuous-tracking layer (paired clinical + wearable longitudinal data on the same individuals; the personalized navigation engine) accumulates inside the PBC subsidiary, licensed back to the Foundation under terms that keep the open map perpetually maintained. This gives us both: an open map as a public good, and a defensible sensor + navigator product line that can attract VC at Gate 1.

**Parallel cellular + connectomics foundation models.** Per the 2026-05-07 architecture meeting with the Purdue team: same building blocks (WaveGC for multi-resolution graph diffusion, AlphaGenome-style cross-resolution attention for inter-block information sharing) applied at two scales. Genes-as-units cellular FM and voxels-as-units connectomic FM share infrastructure and benchmarks but operate independently, with cross-scale alignment via paired data (ENIGMA, PsychENCODE 388 paired). Shourya leads both tracks with Mohammadi support; Mango remains contributor as bandwidth allows.

**Multi-scale nested foundation models.** Our cellular FM treats each gene as a unit and uses a molecular foundation model (e.g., ESM, AlphaGenome) as the embedding source, but unlike scPrint2 and TranscriptFormer (which freeze the molecular FM as a static dictionary), we train the molecular and cellular FMs end-to-end through cross-resolution transformer blocks. Disease modeling concentrates on the residual space (delta from healthy baseline) using conditional flow matching, so that the entire stack converges to the language of residuals (which is also the language of individual genomic variation).

**Patient Advocacy Council promoted to governance.** PAC, an innovation we introduced in the Google Impact proposal, becomes a first-class governance structure with charter, seats across both entities, and decision rights on grant prioritization, study designs, release timing, and the open / proprietary boundary. It is not advisory. Its veto on participant-impacting decisions is binding by Foundation bylaws.

**Clinical-to-wearable alignment subtrack added.** Without paired clinical (fMRI, EEG) and wearable (fNIRS, consumer EEG, physiology) data on the same individuals, the Y4-Y5 wearable transition fails. We start in Y1 with the Inclusion Study and FRESH initiative public datasets, plus an internal core-team pilot wearing both research headsets and undergoing clinical fMRI/EEG. This is the dress rehearsal for the Y4 clinical trial.

## What we ask of readers

| Reader | Action |
|---|---|
| Funders (Astera, Google.org, ARPA-H) | Treat the open Cytoverse track (H1) as the deliverable of your award; the proprietary track is funded separately at Gate 1 |
| Foundation Board | Ratify the 36-month bifurcation policy and the PAC governance charter |
| Scientific Advisory Board | Review the parallel FM architecture and the cross-modal alignment plan |
| Patient Advocacy Council (forming) | Provide binding input on study design, release pace, and the open / proprietary boundary |
| Engineering team | Adopt the four-repo structure (neurogenomics, neuroconnectomics, neurotranscriptomics, neurobehavior) with shared infrastructure package |
| Clinical partners (McLean, Mount Sinai, Manchester) | Confirm protocol alignment with the Y2 external pilot and the Y4 clinical trial |

## Status at a glance

![Diagram 2 from 00_executive_summary](/tmp/master_plan_compile/diagrams/00_executive_summary__2.png)


The plan that follows turns this picture into operating decisions, milestones, and quantitative measures across the next decade.






# Section: 01_identity_and_framework.md


# Identity and Framework

**Companion to:** `00_executive_summary.md`, `02_horizons_and_bifurcation.md`

## Identity (L0)

| Field | Value |
|---|---|
| Legal name | Cytognosis Foundation, Inc. |
| Type | 501(c)(3) Nonprofit Healthcare Innovation Foundation |
| EIN | 39-4383634 |
| UEI | HS4PRLL7AKY5 |
| HQ | South San Francisco, California |
| Web | https://www.cytognosis.org/ |
| Etymology | Greek: *cyto* (cell) + *gnosis* (knowledge). "Cellular knowledge that precedes diagnosis." |

### Vision

To transform healthcare from reactive treatment of disease to proactive preservation of healthspan.

### Mission

To pioneer a cellular intelligence platform that maps personalized health states, detecting and intercepting disease years before symptoms emerge.

### Mission, GPS variant

Building the GPS for Health: mapping, sensing, and navigating individual health trajectories before disease takes hold.

### Promise

To make precision health a human right, not a privilege.

### Values

| Value | What it means in operating decisions |
|---|---|
| **Openness** | Code, data, models, and protocols are open by default. The 36-month bifurcation is the only structured exception, with documented mission-protective rationale. |
| **Rigor** | Every public release passes the release checklist: license, model card, data card, eval card, differential-privacy probe, re-identification probe. No exceptions. |
| **Equity** | Health equity is design input, not afterthought. Every cohort, dataset, sensor calibration, and language coverage decision is audited for whose data it represents and whom the resulting tool can serve. |
| **Courage** | We take the bets that academia is structurally too small to take and that industry is structurally too short-term to take. We document failure as a deliverable. |
| **Care** | The Patient Advocacy Council holds binding decision rights. We move at the speed of trust where participants are involved, even where speed of science would prefer otherwise. |

These are the canonical wording. Earlier drafts that used "Continuity" or "Convergence" are superseded.

## Framework (L1 to L4)

We use a four-layer hybrid because no single framework covers a 15-year health-research nonprofit with an R&D to clinical to globalization arc and a two-entity Helix structure. The four layers are stacked so each lower layer cleanly serves the layer above.

![Diagram 1 from 01_identity_and_framework](/tmp/master_plan_compile/diagrams/01_identity_and_framework__1.png)


### Why this hybrid

- **Three Horizons** mirrors the Bylaws Article I §1.2 three-phase structure and is the native idiom at ARPA-H, NSF, and most government science funders. Reviewers do not need translation.
- **OGSM** forces every qualitative ambition (Objective) to name a measurable Goal, concrete Strategy, and quantitative Measures. Grant reviewers look for exactly that discipline.
- **Hoshin Kanri** supplies catch-ball alignment between the Foundation, the future PBC subsidiary, the UK office, and (later) regional sister organizations at annual cadence.
- **OKRs** are the existing operational rhythm in the Portfolio Management folder of the Monday workspace and align with how engineering teams already plan.
- **McKinsey 12** replaces the older 7-S framework and keeps the operating model audit-ready under one consistent lens.

Pure OKRs underserve a 15-year horizon. Wardley Maps are hard to audit in grant review. Balanced Scorecard does not accommodate R&D-to-deployment transitions. The hybrid is the deliberate compromise.

## Vocabulary

The whole plan uses the same set of identifiers throughout. Train new readers and new tools on this once and stop translating.

| Token | Meaning | Example |
|---|---|---|
| `Hx` | Horizon (H1, H2, H3) | `H1` = Years 1 to 5, R&D phase |
| `Gn` | Gate (G1, G2, G3) | `G1` = H1 to H2 transition, target Year 5 |
| `GC-Gn.k` | Gate criterion | `GC-G1.S2` = scientific criterion 2 of Gate 1 |
| `Py` | Pillar | `P1` = Cytoverse, `P2` = Cytoscope, `P3` = Cytonome, `P4` = Open-Science Substrate, `P5` = Clinical Translation, `P6` = Organization and Helix |
| `Mn` | Meta-track (1 of 5) | `M1` = Discovery and Platform |
| `Tn` | Subtrack (1 of 15) | `T1` = Science and Discovery |
| `SO-Hn.k` | Strategic Objective | `SO-H1.1` = "The Map" objective for Horizon 1 |
| `Hx.Py.Gz` | Strategic Goal | `H1.P1.G1` = first goal of Cytoverse pillar in Horizon 1 |
| `SI-*` | Strategic Initiative | `SI-Neuroverse-Micro` |
| `Mz` | Milestone | `MS-GI-1` = Google Impact phase 1 milestone |
| `Kz` | KPI / measure | `K1`, `K2`... per Goal |
| `Px.Oy` / `Px.Oy.KRz` | Phase OKR | `P1.O1.KR2` = pillar 1, objective 1, key result 2 |

## Meta-track structure (5 × 15)

Per the user-confirmed track-taxonomy preference (3 to 5 top-level meta-tracks with finer subtracks for multi-resolution organization), the operating layer carries five meta-tracks, each containing finer subtracks. Every Strategic Initiative is tagged to at least one subtrack.

| Meta-track | Scope narrative | Subtracks |
|---|---|---|
| **M1 · Discovery and Platform** | The science we produce and the platform we build to instrument, deploy, and learn from it. *"What we build."* | T1 Science and Discovery · T2 Technology and Platform |
| **M2 · Translation** | The pathway from platform to population impact: trials, partners, participants, policy. *"How it reaches people."* | T3 Clinical and Regulatory · T5 Partnerships and Ecosystem · T6 Community and Engagement · T7 Policy and Advocacy |
| **M3 · Openness** | The open substrate, standards, and outward communication that ensure reproducibility, adoption, and credibility. *"What we open up."* | T4 Open Science and Standards · T12 Communications and Brand |
| **M4 · Organization** | The Helix structure, people, finances, and operational infrastructure that make the mission durable. *"How we function."* | T8 Governance and Legal · T9 People and Culture · T10 Finance and Sustainability · T11 Operations and Infrastructure · T14 Patient Advocacy Council *(new in v2.0)* |
| **M5 · Learning** | The cross-cutting measurement, evaluation, and retrospection system that feeds every other track and every gate. *"How we know we're working."* | T13 Measurement, Evaluation and Learning · T15 Cross-modal Alignment Subtrack *(new in v2.0)* |

The two new subtracks (T14 PAC, T15 Cross-modal Alignment) are explicit responses to the v1.1 to v2.0 changes documented in `README.md`. T15 holds the clinical-to-wearable alignment work that bridges H1 open data to H2 proprietary data; T14 holds the participant-governance work that runs in parallel.

## McKinsey 12-element overlay

Maintained as a standing rolling lens on the operating model in `20_organization_helix.md`. The twelve elements are: Purpose, Value Agenda, Structure, Ecosystem, Leadership, Governance, Processes, Technology, Behaviors, Rewards, Footprint, Talent. Where the operating section is silent on an element, that silence is itself a planning decision and is flagged in the next annual review.

## How this layer relates to the others

- **Identity (L0)** does not change between annual reviews. A Bylaws amendment is the only path to revising vision, mission, or values.
- **L1 Three Horizons** is reaffirmed annually. Horizon redefinition (e.g., dropping a horizon, expanding a phase) requires Board action.
- **L2 OGSM** lives in the Strategic Roadmap (this plan) and is updated at each annual planning cycle (October).
- **L3 Hoshin** lives in the X-matrix board (currently archived) and is rebuilt annually at the catch-ball workshop.
- **L4 OKRs** live in the Portfolio Management folder of the Monday workspace and turn over quarterly.

## Cross-references

- `02_horizons_and_bifurcation.md` defines the L1 Horizons in concrete operational terms with the 36-month bifurcation overlay.
- `03_short_term_1to2y.md`, `04_mid_term_5to6y.md`, `05_long_term_10y.md` detail L2 OGSM by horizon.
- `20_organization_helix.md` carries the McKinsey 12 overlay.
- `21_patient_advocacy_council.md` defines the PAC charter that sits behind subtrack T14.






# Section: 02_horizons_and_bifurcation.md


# Three Horizons and the 36-Month Bifurcation

**Companion to:** `01_identity_and_framework.md`, `03_short_term_1to2y.md`, `04_mid_term_5to6y.md`, `05_long_term_10y.md`, `23_open_science_and_ip.md`

## Three Horizons at a glance

Cytognosis runs a 15-year strategic shell with three horizons and three gates. Each horizon has its own strategic posture, its own funding pattern, and its own deliverable. The transition between horizons is a formal Board-level decision, not a calendar tick.

| Horizon | Years | Phase | Strategic posture |
|---|---|---|---|
| **H1** | 1 to 5 | R&D · "build the map" | Capital-restricted to time-restricted. Primarily non-dilutive funding (grants, philanthropy). All artifacts open by default. |
| **H2** | 5 to 10 | Clinical and commercialization · "build the sensor and navigator" | Hybrid funding: Foundation continues open mission with non-dilutive sources; PBC subsidiary raises VC for the proprietary tracking and navigation product. |
| **H3** | 10 to 15 | Globalization and equity · "deploy worldwide" | Federated structure: regional sister organizations carry local trust and local approvals. Foundation coordinates, licenses, and redistributes. |

![Diagram 1 from 02_horizons_and_bifurcation](/tmp/master_plan_compile/diagrams/02_horizons_and_bifurcation__1.png)


## The 36-month bifurcation

The single most consequential structural decision in this plan: at month 36 of Horizon 1, the deliverable splits into two tracks that develop in parallel for the rest of the lifespan of the platform.

### Why the bifurcation exists

Foundations and product companies have opposite optimal incentives. A foundation's job is to keep critical infrastructure open and trustworthy in perpetuity. A product company's job is to convert defensible assets into revenue that funds further R&D. Most attempts to fold both into one organization fail because the incentives collide on every release decision.

The 36-month boundary is where the collision becomes unavoidable, because it is the moment when our work transitions from "open clinical-grade tooling that anyone can adopt" to "continuous, individualized tracking data that requires direct relationship with each participant." Continuous tracking data cannot be open in the same way that a cell atlas can. Privacy law, participant consent, and the physical economics of operating a sensor and navigation product all push it into a different organizational form.

We solve this by building two entities (Foundation 501(c)(3) plus future PBC subsidiary, the Helix structure) and by drawing a clean, dated line: anything before the line stays in the Foundation forever; anything after the line is owned by the entity that invests in continuous data collection.

### What the bifurcation says, exactly

![Diagram 2 from 02_horizons_and_bifurcation](/tmp/master_plan_compile/diagrams/02_horizons_and_bifurcation__2.png)


### What stays open after the bifurcation

The Foundation continues to:

- maintain Cytoverse (the Map) and ship a major release at least annually, with the same release checklist and the same open licenses;
- publish disease-axis discoveries, biotype validations, and cross-modal alignment models;
- maintain the open clinical-grade software stack so the map is adoptable in clinical care and patient stratification in trials without licensing barriers;
- continue to fund this work with grants, philanthropic capital, and a perpetual royalty stream from the PBC.

The Foundation does not give up ownership. It does not stop releasing. It does not become a pre-publication shop for the PBC. The map is a public good in perpetuity, and the Foundation's job after Gate 1 is to keep that promise.

### What becomes proprietary after the bifurcation

The PBC subsidiary, once activated at Gate 1, owns:

- continuous longitudinal data on consented individuals (paired clinical-grade sensing during onboarding, then continuous wearable-grade sensing thereafter);
- the personalized navigation engine that runs causal recommendation on each individual's history;
- the Cytoscope hardware lineage and the Cytonome on-device regulated product;
- improvements to the navigator that depend on the proprietary continuous dataset.

The PBC is structurally bound to the Foundation through the Helix Framework: the Foundation holds enough governance to prevent mission drift, holds a perpetual license to the open layers of the platform, and receives a documented royalty stream that funds the open mission.

### Why the bifurcation is *operationally* a clean line

Three reasons the line is clean rather than a fuzzy boundary that legal will fight about for a decade:

- The bifurcation marker is a single, dated act of the Foundation Board. Before it, no clinical-trial proprietary data exists; after it, every consent form on the new study cohort is structured for the dual ownership.
- Open releases through Year 3 use only public, consortium, or appropriately licensed third-party data (PsychENCODE, NeuroBioBank, ENIGMA, UKBB, ABCD, HCP). Nothing from the future trial leaks back into pre-36m artifacts.
- Open releases after Year 3 use only the same kinds of data plus newly published consortium data. Insights that depend on proprietary continuous tracking are kept behind the PBC line.

## Gates

Each transition is a formal Board-level go/no-go decision. Gate criteria are inherited from `01_Cytognosis_Strategic_Roadmap_15-Year.md` v1.1, refined and repeated here.

### Gate 1 (H1 to H2, target Year 5)

This is the hardest gate. R&D success is necessary but not sufficient for clinical validation, and the organization is rarely structured to carry research directly into clinical and commercial execution. The Helix Framework exists precisely because of this gate.

| Category | Criterion | Evidence required |
|---|---|---|
| **Scientific** | `GC-G1.S1` Cytoverse v2 (meso) and v3 (macro) released as open artifacts | External validation against ≥2 frameworks (HiTOP, Grotzinger 5-factor, RDoC) |
| | `GC-G1.S2` Cross-scale imputation works for at least one indication | AUROC ≥ 0.75, held-out cohort |
| | `GC-G1.S3` Dimensional coordinates predict treatment response | Effect size ≥ 15% over DSM baseline, retrospective dataset |
| | `GC-G1.S4` Phase 0 self-instrumentation and external 20-30 person pilot complete | Documented learnings published |
| **Clinical** | `GC-G1.C1` Clinical-scale follow-on grant secured | $10M+ over 3 years (ARPA-H, NIH R01, Wellcome Leap) |
| | `GC-G1.C2` IRB infrastructure and clinical partners ready for 500+ participant study | Signed agreements |
| | `GC-G1.C3` FDA pre-submission completed; regulatory pathway identified | DHCE meeting record |
| **Organizational** | `GC-G1.O1` Helix structure operational | PBC charter; promise-of-future-equity allocations; people-as-seed-funders mechanism legally vetted |
| | `GC-G1.O2` UK office operational | ≥5 FTE, independent grant pipeline |
| | `GC-G1.O3` ≥24 months operating runway at H1 burn | Audited financials |
| | `GC-G1.O4` No material governance, IP, or compliance findings | External audit |
| **Adoption** | `GC-G1.A1` Open artifacts adopted | ≥1,000 downloads, ≥50 citing publications |
| | `GC-G1.A2` UBAP adopted by external groups | ≥2 external biosensor or clinical partners |
| **PAC** *(new in v2.0)* | `GC-G1.P1` Patient Advocacy Council operational | Charter ratified, seats filled, two annual review cycles complete |
| | `GC-G1.P2` PAC has exercised binding decision rights at least once | Documented case where PAC input changed a study, release, or grant scope |

**Halt or re-scope if** two or more Scientific criteria fail and at least one path to closure is not obvious within 12 months, OR Clinical criterion `GC-G1.C1` fails and no bridge funding covers 12 months.

### Gate 2 (H2 to H3, target Year 10)

Dominated by clinical success. Commercial sustainability is necessary but not sufficient; equity of access and regulatory maturity are the binding constraints.

| Category | Criterion |
|---|---|
| Clinical | ≥1 FDA De Novo or 510(k) clearance for a Cytonome-powered product |
| | Clinical-scale evidence in ≥3 indications, each with effect size ≥20% over standard of care |
| | Post-market surveillance infrastructure live |
| Financial | PBC at or near break-even, or on a funded path to break-even within 24 months |
| | Foundation operations independent of further philanthropic catalytic capital |
| | Net Promoter Score ≥50 with no demographic subgroup below 30 |
| Equity | Demonstrated emerging-market deployment model |
| | All data pipelines post-quantum safe and decentralized |
| | PAC expanded to multi-continental composition |

**Halt or re-scope if** clinical clearance is not achieved AND no regulatory pathway is credible within 18 months, OR equity criteria are systematically failing without a plan.

### Gate 3 (Year 15)

Less a gate than a governance milestone. Board reviews whether the Foundation's role should continue, consolidate, or hand off to successor consortia. Dissolution provisions of Bylaws Article XIII apply only if successor organizations are ready to receive the charitable assets.

## Why this bifurcation is what funders want

| Funder type | Why they like the line |
|---|---|
| Astera, Convergent Research, Speculative Technologies | They fund R&D that becomes a public good. The 36-month commitment to keep the map open in perpetuity is exactly their thesis. |
| Google.org, philanthropic AI-for-science | Same as above. Open releases against time-bound milestones map cleanly to their funding instrument. |
| ARPA-H, DOE, NIH | Federal funders want clear deliverables that benefit the public. The open track answers that. The proprietary track does not have to be funded by them. |
| Wellcome Leap, EU Horizon, regional foundations | They want the deliverable to be operational in their geography. The open map travels well. |
| Future PBC investors | They want a defensible asset. The proprietary tracking layer plus continuous individual data is defensible; the open map alone is not. The bifurcation gives them the asset class they need to write a check at Gate 1. |

## Bifurcation operational rules

The bifurcation is not an aspiration; it is a set of rules engineering and grants follow on every release.

- Every Strategic Initiative carries a **Bifurcation Phase** tag in Monday: `pre-36m-open`, `post-36m-open`, `post-36m-proprietary`.
- Every dataset has a documented provenance chain that establishes whether it falls before or after the line.
- Every model release is tagged with the latest bifurcation-clean training data cutoff.
- Pre-36m artifacts cannot consume any data tagged `post-36m-proprietary`. CI gates this.
- Post-36m open artifacts may consume aggregated, consented insights from the proprietary side, with explicit differential-privacy budget accounting and PAC sign-off, but cannot consume raw individual-level proprietary data.

## Cross-references

- `23_open_science_and_ip.md` carries the licensing detail and the PBC IP-licensing terms.
- `20_organization_helix.md` carries the legal structure that enforces the bifurcation.
- `21_patient_advocacy_council.md` carries the PAC governance role at the bifurcation gate.
- `30_funding_strategy.md` shows how the funding pipeline maps to the two tracks.






# Section: 03_short_term_1to2y.md


# Short-Term Plan (Years 1 to 2)

**Target window:** April 2026 to March 2028
**Companion to:** `02_horizons_and_bifurcation.md`, `11_technical_track_FMs.md`, `12_clinical_to_wearable.md`, `30_funding_strategy.md`
**Authoritative OKR cascade:** `02_Cytognosis_Phase1_Operational_Plan.md`. This document gives the strategic narrative; the OKR cascade gives the quarterly KRs. They must agree.

## What we ship in 24 months

By end of Year 2, Cytognosis Foundation has delivered:

- a parallel cellular and connectomic foundation-model stack with end-to-end multi-scale training capability, and at least one open release of each (Neuroverse Micro v1, Neuroverse Meso v0.5);
- the open-science substrate that wraps every release (Copier template, release-checklist CI, model + data + eval cards);
- a fielded wearable integration layer for Oura Ring 4, Muse S Athena, g.Nautilus, Emotiv Insight, with a working Phase 0 internal pilot on the core team;
- the three-layer privacy architecture for Cytonome v0.1 with a hard-coded crisis-detection module and zero raw-data egress;
- the macro LLM (≤3B params) that quantifies mental health states from conversation, deployed on-device;
- an established UK office (legal entity formed, first FTE hired) anchored on the Manchester autoimmune collaboration;
- the PBC subsidiary charter drafted and reviewed by counsel, plus the promise-of-future-equity plan documented;
- the Patient Advocacy Council charter ratified, seats filled, first two quarterly review cycles completed;
- $5 to 13M cumulative non-dilutive funding secured across Astera, Google.org Impact (if awarded), additional philanthropic, and early ARPA-H planning grants.

## Strategic posture

H1 strategic posture is **capital-restricted to time-restricted transition**. We are funding-constrained at the start; by end of Year 2, time becomes the binding constraint. Every Strategic Initiative carries a clear "what would happen if we slipped two quarters" answer, because that is the question the next funding round will ask.

All Year 1-2 outputs are pre-36m and **open by default** (Apache 2.0 for code and weights, CC BY 4.0 for documentation, CC0 for derived data where source licenses permit). No participant-level data leaves the Foundation. The Phase 0 internal pilot uses only consented core-team data and is released as an open public good with appropriate differential-privacy gating.

## What we focus on

The five strategic objectives carrying H1 (set in v1.1, refined in this plan):

| Objective | What it produces in Y1-Y2 |
|---|---|
| **SO-H1.1 · The Map** | Neuroverse Micro v1, Neuroverse Meso v0.5, Neuroverse Macro v1; cross-modal alignment subtrack initiated; Immunoverse v0 scoping (UK) |
| **SO-H1.2 · The Tracker** | Wearable integration layer; Phase 0 pilot complete; UBAP draft v0.1 circulating; Delphi LOI in flight |
| **SO-H1.3 · The Navigator** | Cytonome v0.1 on-device runtime; crisis-detection module hard-coded; long-term memory and voice interface in scope |
| **SO-H1.4 · Open Substrate** | Copier template v1.0, release-pipeline CI live, Helix Framework paper drafted |
| **SO-H1.5 · First Clinical Footprint** | IRB live; clinical partnerships signed (McLean, Mount Sinai, Manchester); LEAC and PAC operational; retrospective dimensional-vs-DSM evidence drafted |
| **SO-H1.6 · Helix Activation Readiness** | SAB stood up; UK office stood up; PBC charter drafted; first $5-13M secured |

## Detailed Y1-Y2 deliverables

### Cytoverse pillar (P1 · the Map)

![Diagram 1 from 03_short_term_1to2y](/tmp/master_plan_compile/diagrams/03_short_term_1to2y__1.png)


**Neuroverse Micro v1 (`SI-Neuroverse-Micro` · M18 · Apache 2.0).** Per the technical-track design, the cellular foundation model is built end-to-end with a molecular foundation model rather than a frozen-dictionary embedding source. Concrete deliverable:

- pseudobulked PsychENCODE single-nucleus RNA-seq plus ATAC-seq, conditioned on TransBox semantic embeddings of cell type, tissue, and brain region;
- AlphaGenome (1bp, 1Mb) fine-tuned on the pseudobulked data, with cross-resolution attention blocks (per `11_technical_track_FMs.md`) that share information across scales;
- conditional flow matching layer that models the **residual** space (delta from healthy baseline) rather than absolute expression, so the model speaks the language of disease shifts from the start;
- public release on Hugging Face plus Zenodo, with full model card, data card, eval card, and release-checklist CI pass.

Performance gate: fine-tuned model outperforms off-the-shelf AlphaGenome on held-out cell types by ≥15% on cell-type-specific expression prediction; learned axes recover the Grotzinger 5-factor structure (Fréchet mean) and a jointly trained DSM classifier preserves ≥90% of label-supervised diagnostic information.

**Neuroverse Meso v0.5 (`SI-Neuroverse-Meso` · M24).** Connectomics foundation model on harmonized BIDS/FAIR data using the same building blocks (WaveGC for multi-resolution graph diffusion, AlphaGenome-style cross-resolution attention). Pre-training task is stratified subgraph masking. Yale dataset and Open Era's Y dataset (over 300 samples, harmonized) are the prototyping data; UK Biobank imaging subset is the scale-up. Architecture sharing with the cellular pillar is enforced through a shared infrastructure package (the "Lego pieces" decision from the 2026-05-07 architecture meeting). Final v1 release in mid-term document.

**Neuroverse Macro v1 (`SI-Neuroverse-Macro-LLM` · M18).** Fine-tuned ≤3B parameter LLM that maps clinical-dialogue and EHR-derived language into validated mental-health scales (PHQ-9, GAD-7, HiTOP factors, RDoC dimensions). Quantized to run on consumer phones for Cytonome v0.1. Sparse autoencoder interpretability track runs in parallel; SAEs publish features and their clinical-construct mapping by M15.

**Cross-modal alignment subtrack (T15, new in v2.0).** Initiated Y1; matures across Y2-Y3. Anchored on the Inclusion Study (Nature Human Behaviour 2025) and FRESH initiative (Nature Communications Biology 2025) public datasets, plus the internal core-team pilot (see `12_clinical_to_wearable.md`). The alignment subtrack is the prerequisite that lets H1 open data inform the H2 clinical study.

### Cytoscope pillar (P2 · the Tracker)

**Wearable integration layer (`SI-Cytoscope-Wearable-Integration` · M9-M12).** SDK integrations for Oura Ring 4, Muse S Athena, g.Nautilus (research-grade EEG), Emotiv Insight. Continuous, lossless, timestamped ingest. Coverage is intentionally broad-then-deep: cover four sensor modalities first, validate one against research-grade ground truth.

**Phase 0 internal pilot (`SI-Cytoscope-Wearable-Integration` continued · M12).** Core team of three to five wears all sensors daily for three months, with biweekly self-administered clinical scales. Data completeness ≥90%. Output: open public-good dataset under CC BY 4.0 with consent and DP gating, plus internal multimodal fusion model v0 trained on the Phase 0 data. This is the dress rehearsal for the external pilot in Year 2-3.

**UBAP draft v0.1 (`SI-UBAP-v1` · M18).** Universal Biosensor Adapter Protocol draft circulated to ARPA-H Delphi, the Caltech molecular-monitoring FRO, OpenBCI, and academic biosensor groups for feedback. Final v1.0 publication in mid-term document.

**Delphi LOI (`SI-Delphi-Collaboration` · M24).** Formal Letter of Intent or cooperative agreement with ARPA-H Delphi for personalized programmable biosensor panel design.

### Cytonome pillar (P3 · the Navigator)

**Three-layer privacy spec (`SI-Privacy-Architecture` · M12 · open protocol).** Documented architecture covering perception (on-device LLM), local compute (personal node), distributed storage (community blockchain-inspired layer), and external interaction (heavily encrypted, post-quantum embeddings to the Cytognosis training layer). External review by ≥2 qualified security researchers. Reference implementation Apache 2.0. See `16_patient_safety_architecture.md` for the full specification.

**Cytonome v0.1 on-device runtime (`SI-Cytonome-v0.1` · M18).** Quantized macro LLM running on iOS and Android reference devices at sub-second response latency. Hard-coded crisis-detection module surfaces 988 Suicide and Crisis Lifeline plus Crisis Text Line on detection; opt-in clinician alerting. Validated before any participant exposure. Zero raw-data egress verified by automated integration tests on every release.

**Long-term memory module (`SI-Memory-Module` · M24).** On-device episodic memory store with vector index, consolidated to semantic memory on schedule. Recall ≥80% at six-month lag in Phase 0 pilot. User-auditable: every stored item is viewable, editable, deletable in-app.

### Open-Science Substrate pillar (P4)

**Copier template v1.0 (`SI-OpenScience-Template` · M6).** Wraps every Cytognosis project in LinkML/BioLink schemas, RO-Crate profiles, SPDX license declarations, and W3C Web Annotation hooks. ≥3 Foundation projects use the template by M6.

**Release pipeline (`SI-Release-Pipeline` · M12).** CI job on every release repo runs the checklist: license, model card, data card, eval card, differential-privacy probe, re-identification probe. No release without checklist pass.

**Helix Framework paper draft (`SI-Helix-Paper` · M18).** Open commentary paper drafted, circulated to Astera, Convergent Research, and Speculative Technologies for co-signing invitation. Publishes Y2 Q4 to Y3 Q2.

### Clinical Translation pillar (P5)

**IRB and clinical infrastructure (`SI-Clinical-Infrastructure` · M3-M18).** Salus IRB contract live by M3; Phase 0 internal IRB by M9; Northstar IRB option also evaluated for retrospective analyses (per Patty meeting). Clinical partnership agreements signed with McLean Hospital (Brad Ruzicka subaward), Mount Sinai, and University of Manchester (Madhvi Menon, autoimmune) by M9.

**Lived Experience Advisory Council operational** by M18 (8 to 12 members across MDD, GAD, PTSD, SZ, BD), meeting quarterly.

**PAC charter ratified and seats filled** by M12 (see `21_patient_advocacy_council.md` for charter detail). Two quarterly review cycles completed by M24. Note: PAC and LEAC are distinct bodies with overlapping membership but different charters; PAC has binding rights at the bifurcation gate, LEAC advises on study design and accessibility.

### Organization and Helix pillar (P6)

**Scientific Advisory Board (`SI-SAB-Board-Expansion` · M6).** 5 to 7 members across HiTOP, ENIGMA, PsychENCODE, ARPA-H Delphi, Convergent FRO communities.

**UK office (`SI-UK-Office` · M12-M18).** UK legal entity formed by M12 (form per UK counsel: charity, CIO, or subsidiary). Manchester-area lease M15. First FTE M18.

**PBC subsidiary charter draft (`SI-PBC-Charter` · M24-M30).** Draft completed and reviewed by independent nonprofit and corporate counsel. Bylaws-aligned IP licensing terms documented. Promise-of-future-equity plan reviewed against IRS intermediate-sanctions rules.

**Phase 1 funding (`SI-Phase1-Funding` · continuous).** Y1 target $3-5M; Y2 target $5-8M; cumulative Y1-Y2 floor $8M. Source mix: Astera Residency, Google.org Impact (in review at compilation time, $2.2M ask), early ARPA-H planning grants, EA Fund, philanthropic partners. No quarter with under 12 months runway.

## Key risks for Y1-Y2

| Risk | Likelihood | Impact | Primary mitigation |
|---|---|---|---|
| Astera + Google.org both reject | Medium | High | Diversified Y1-Y2 pipeline (EA Fund, Convergent Research, philanthropic) keeps minimum runway. Continued reduction of burn until next decision point. |
| Cellular FM parallel build slips because Mango is bandwidth-limited | Medium | Medium | Confirmed at 2026-05-07 meeting: Shourya leads both tracks; Mango contributes as bandwidth allows. Shared infrastructure package keeps the work parallel rather than serial. |
| Phase 0 internal pilot shows no signal | Low | Medium | The pilot's primary value is engineering (data plumbing, sensor integration, on-device pipeline); scientific signal is exploratory. Failure narrows but does not collapse Y2 scope. |
| UK legal entity formation delayed | Medium | Medium | Start with US-only operation if delayed; UK office is value-add not block. Immunoverse v1 timing slips by one quarter per UK delay. |
| PBC charter blocked by counsel review | Low | Medium | Charter is drafted and vetted but not activated until Gate 1; review cycle has 18 months of slack. |
| Bifurcation policy is not Board-ratified by M24 | Low | High | Without it, PAC cannot operate at the gate; without PAC at the gate, Gate 1 fails. Ratify at M12 or earlier. |

## Notes from recent meetings

The Patty Purcell strategic-development meeting (2026-05-08) reaffirmed the high-level GPS-for-Health framing in plain language for funder audiences, and confirmed:

- the working title for the Astera proposal: "open multiscale dimensional map of human psychiatry" (alternate: "multimodal multiscale map of mental health states");
- a consulting role for Patty against the Astera proposal at approximately $300/hr, eight hours per week, included in the proposal budget for early payment;
- pet and infant cohorts as opportunistic early-market data sources, with cleaner consent pathways than adult-clinical data, and many psychiatric manifestations in dogs that map closely to human ones;
- the immediate Astera focus on the micro scale (genotype + single cell) for the first 18 months, the Google.org focus on meso (connectomics), and the cross-scale work commencing after M18.

The Cell-State / Perturbation Modeling meeting (2026-05-07) finalized:

- the parallel cellular + connectomic FM architecture with shared building blocks (WaveGC + AlphaGenome cross-resolution attention);
- the four-repository structure: `neurogenomics`, `neuroconnectomics`, `neurotranscriptomics`, `neurobehavior`;
- a shared, reusable infrastructure package within `neuroconnectomics` for the "Lego pieces" wavelet+transformer convolution layer;
- the prototyping data (Open Era's Y dataset, then Yale, then UK Biobank);
- the publication target: Nature Methods or Nature Machine Intelligence for the multi-scale infrastructure paper;
- Shourya leading both connectomics and cellular tracks given Mango's Meta start;
- a planned Mohammadi visit to Purdue at end of May or early June to white-board the three-to-six-month milestone plan.

## What graduates to mid-term (Years 3+)

- Neuroverse Meso v1 release (M36) and Cross-Scale Paired Models (M48) move to `04_mid_term_5to6y.md`.
- External 20-30 person pilot (M30) and ARPA-H PHO proposal (M54) move to mid-term.
- Causal recommendation engine, ontology-grounded passive sensing, post-quantum decentralized storage move to mid-term.
- The bifurcation marker itself (Year 4 quarter 1, M37) is the headline event of mid-term.






# Section: 04_mid_term_5to6y.md


# Mid-Term Plan (Years 3 to 6)

**Target window:** April 2028 to March 2032
**Companion to:** `03_short_term_1to2y.md`, `05_long_term_10y.md`, `02_horizons_and_bifurcation.md`, `12_clinical_to_wearable.md`, `30_funding_strategy.md`

This is the period the strategic plan turns most visibly. The first half (Years 3 to early Year 4) finishes the open Cytoverse map and prepares the bifurcation. The second half (mid Year 4 onward) executes the bifurcation, runs the proprietary clinical study, drafts FDA pathways, and transits Gate 1 into Horizon 2.

## What we ship in this window

By end of Year 6, Cytognosis Foundation has delivered:

- **Cytoverse v1 across all three scales** in fully open form: Neuroverse Meso v1 (M36), Cross-Scale Paired Models (M48), Immunoverse v1 (M60), all with annual update cycles thereafter;
- **the 36-month bifurcation** ratified, applied, and operational in the workspace, with the open clinical map continuing to ship from the Foundation and the proprietary tracking layer accumulating in the PBC subsidiary;
- **the proprietary clinical study** running: 12 months of multimodal data collection on a consented cohort, paired clinical-grade and wearable-grade sensors on the same individuals, designed to learn the clinical-to-wearable alignment that powers the Year 7+ continuous tracking product;
- **the external 20 to 30 person pilot** completed (M30) and the ARPA-H PHO follow-on proposal submitted (M54);
- **FDA Digital Health Center of Excellence pre-submission** complete, regulatory pathway identified, biomarker qualification track engaged;
- **Cytonome v1.0 candidate** with bidirectional voice interface, ontology-grounded passive sensing, and the personalized causal recommendation engine (defensive, corrective, supportive);
- **Universal Biosensor Adapter Protocol v1.0** published and adopted by ≥2 external biosensor groups;
- **PBC subsidiary activated at Gate 1** with promise-of-future-equity vested, people-as-seed-funders mechanism live, first VC raise opening or closed;
- **UK office at scale** (≥5 FTE, independent grant pipeline, lead on Immunoverse), and the Patient Advocacy Council operating across both entities at full charter capacity.

## The headline of mid-term: the bifurcation event

The bifurcation is a single, dated act of the Foundation Board, supported by the Patient Advocacy Council. It happens at the start of the proprietary clinical study, target M37. Before it, no participant-level continuous tracking data exists; after it, every consent form is structured for the dual-ownership Helix.

![Diagram 1 from 04_mid_term_5to6y](/tmp/master_plan_compile/diagrams/04_mid_term_5to6y__1.png)


## Strategic Objectives covering mid-term

Mid-term is the meeting point of the H1 closing objectives and the H2 opening objectives. Both sets are active simultaneously through the bifurcation event.

### H1 closing (carries into Year 5)

- **SO-H1.1 · The Map** (closes with Cross-Scale Paired Models v1 and Immunoverse v1)
- **SO-H1.2 · The Tracker** (closes with UBAP v1.0 publication and Delphi cooperative agreement)
- **SO-H1.5 · First Clinical Footprint** (closes with ARPA-H PHO submission and FDA pre-sub completion)
- **SO-H1.6 · Helix Activation Readiness** (closes with G1 gate pack assembled)

### H2 opening (begins in Year 5)

- **SO-H2.1 · First regulated product.** FDA De Novo or 510(k) pathway selected; Cytoscope or Cytonome clinical module on regulatory critical path.
- **SO-H2.2 · Scale deployment.** First field-deployed continuous-tracking cohort beyond clinical study; federated learning at scale architecture validated.
- **SO-H2.3 · Ecosystem ignition.** UBAP v2 in flight; multiple third-party sensor implementations live; academic re-use of substrate accelerating.
- **SO-H2.4 · PBC operational.** PBC raising VC on royalties-back-to-Foundation model; promise-of-future-equity vested.

## The proprietary clinical study (Year 4 to Year 5)

The clinical study is the centerpiece of the bifurcation. Its design directly determines whether the H2 product is feasible.

### Study purpose

- Collect 12 months of paired clinical and wearable multimodal data on the same individuals.
- Train clinical-to-wearable alignment models that translate the expensive, episodic ground truth (fMRI, clinical-grade EEG, full clinical assessments) into the inexpensive, continuous wearable stream (fNIRS, consumer EEG, wearable physiology, conversation).
- Produce the first proprietary asset that justifies the PBC and the VC raise at Gate 1.

### Study modality pairing

| Clinical-grade modality (episodic) | Wearable modality (continuous) | Alignment model produced |
|---|---|---|
| fMRI (BOLD, resting-state and task) | fNIRS (consumer headset, e.g., Kernel, OpenBCI Galea) | Hemodynamic translation model |
| Research-grade EEG (e.g., g.Nautilus 64-channel) | Consumer EEG (Muse S Athena, Emotiv Insight) | Channel reduction model |
| Clinical interview + structured scales (PHQ-9, GAD-7, etc.) | LLM-derived passive conversational tracking | Macro-axis projection model |
| Clinical wet-lab molecular markers (cytokines, autoantibodies, neuroinflammation panel) | Wearable proxies (HRV, sleep, activity, glucose where appropriate) | Inflammation-state proxy model |
| Clinical examination (gait, motor, neuro) | Wearable physiology (Oura, Apple Watch, ambient) | Motor and physiological signature |
| Genome (WGS at baseline) | n/a, baseline only | Personalization prior |

### Cohort design

- **Size.** Target 200 participants across MDD, GAD, PTSD, SZ, BD, OCD, neurotypical controls, with an oversample of the 500+ neurodiverse cohort already identified (per Patty meeting) for adjacent recruitment.
- **Duration.** 12 months continuous wearable plus monthly clinical assessment plus quarterly fMRI and clinical-grade EEG.
- **Equity.** Stratified for skin tone, hair characteristics, age, gender, and socioeconomic status because fNIRS signal quality varies systematically with hair and skin (Inclusion Study, Nature Human Behaviour 2025); the alignment model is only valid if its training distribution covers the deployment distribution.
- **Consent structure.** Bifurcation-aware: participants consent to both Foundation use of derived insights (aggregated, DP-bounded) and PBC use of individual-level continuous data, with separate granular controls for each.
- **PAC sign-off.** Patient Advocacy Council reviews and approves the protocol before IRB submission.

### Pre-study Y1-Y3 prep (in `12_clinical_to_wearable.md`)

The clinical study at Year 4 is not the first time we are doing alignment work. We have done two preparatory passes:

- **Public-data pass (Y1-Y2).** Inclusion Study (OpenNeuro ds006377) and FRESH initiative (OSF b4wck) datasets for fNIRS reproducibility and signal-quality modeling.
- **Internal core-team pilot (Y2-Y3).** Consented core team wears research headsets (fNIRS + EEG) and undergoes initial clinical fMRI + EEG. Calibration and modeling phase 1.

By Year 4, the alignment models exist as priors; the clinical study refines them with cohort-scale data.

## Cross-references for mid-term decisions

- The bifurcation rule and IP boundary: `02_horizons_and_bifurcation.md`, `23_open_science_and_ip.md`.
- The full clinical-to-wearable alignment plan: `12_clinical_to_wearable.md`.
- The PAC charter and its role at the bifurcation: `21_patient_advocacy_council.md`.
- The FM technical architecture that powers the open releases through Year 6: `11_technical_track_FMs.md`.
- The funding pipeline through Year 6: `30_funding_strategy.md`.
- Risk register update for mid-term: `41_risks_and_mitigations.md`.

## Key mid-term decisions and their dates

| Decision | Target date | Owner | Backup plan if delayed |
|---|---|---|---|
| Bifurcation policy ratified by Board | M30 (Y3 Q3) | Board, advised by counsel | Hold ratification but begin operating under provisional policy from M30 with explicit Board-directed risk acceptance |
| PAC charter binding | M24 (Y2 Q4) | CEO + counsel | Operate PAC as advisory until charter binding; document advisory→binding transition |
| Clinical study IRB live | M40 (Y4 Q2) | CSO + Salus or Northstar IRB | Single-site (McLean) start while multi-site agreements complete |
| ARPA-H PHO submission | M54 (Y5 Q1) | CEO + Grants | NIH R01 + Wellcome Leap as portfolio insurance |
| FDA pre-sub meeting | M48 (Y4 Q4) | Regulatory lead (hire by Y3 Q4) | Push to Y5 Q1; the gate criterion is identification of pathway, not pre-sub timing alone |
| Cytoscope wearable v1 architecture freeze | M55 (Y5 Q2) | CTO (hire by Y3 Q2) | Continue partner-first sensor strategy through Y6 if architecture not frozen |
| PBC activation | M60 (Y5 Q4) | Board + counsel | Hold at activation-ready until first VC commitment in writing |
| Cytonome v1.0 candidate | M65 (Y6 Q1) | CTO + Engineering lead | Cytonome v0.9 with reduced scope; defer voice or memory module |

## Funding mid-term

| Year | Target | Primary sources |
|---|---|---|
| Y3 | $8 to 12M | ARPA-H planning grant; first UK grant (UKRI, Wellcome); EA Fund; corporate philanthropy |
| Y4 | $8 to 15M | ARPA-H PHO if awarded; NIH R01 if awarded; UK MRC; first VC engagement (PBC, not Foundation, post-Gate-1) |
| Y5 | $5 to 10M (Foundation) + first VC tranche (PBC) | Bridge to PBC activation; PBC first round target $25-50M |
| Y6 | $5 to 10M (Foundation) | PBC scaling round; Foundation continues non-dilutive operations |

## What graduates to long-term (Years 7+)

- Cytonome v1.0 production and FDA clearance (de Novo or 510(k));
- Cytoscope wearable v1 fielded at scale (≥10K devices);
- Federated learning at production scale with formal differential-privacy budget accounting;
- Regional sister organization scoping (LATAM, EU outside UK, Africa, Southeast Asia);
- Substrate handoff planning for Year 15.

These move to `05_long_term_10y.md`.






# Section: 05_long_term_10y.md


# Long-Term Plan (Years 7 to 10, with line-of-sight to Year 15)

**Target window:** April 2032 to March 2036, with strategic line of sight to 2041
**Companion to:** `04_mid_term_5to6y.md`, `02_horizons_and_bifurcation.md`, `20_organization_helix.md`

The long-term plan covers the second half of Horizon 2 (clinical and commercialization) and the opening of Horizon 3 (globalization). The plan stays high-level for years beyond the next decade, since the relevant uncertainty about regulatory, geopolitical, and scientific developments grows large past Year 10. The intent is to set direction and decision criteria, not commitments.

## What we expect to be true by end of Year 10

- **Cytonome regulated product on the market** with an FDA De Novo or 510(k) clearance for at least one disease-detection claim, plus a general-wellness registration covering lifestyle biomarkers as the broader funnel.
- **Cytoscope wearable v1** in market with ≥10,000 active devices, post-market surveillance running.
- **Cytoverse map at clinical-grade across ≥5 indications** in the open Foundation track, with annual major releases continuing per the bifurcation policy.
- **PBC subsidiary at or near operational break-even**, financing core engineering and continuous data operations from product revenue plus VC.
- **Foundation operations sustained** by perpetual royalty stream from the PBC plus continuing non-dilutive sources (philanthropic, federal, regional foundations), independent of further philanthropic catalytic capital.
- **Patient Advocacy Council expanded multi-continentally** with seats from each region we operate in, binding rights at every annual release decision.
- **Federated learning at scale** with ≥50,000 participating devices, formal differential-privacy budget accounting, and zero re-identification incidents on the public probe set.
- **Net Promoter Score ≥50** across active users, disaggregated by age, income, race, and region with no demographic subgroup below 30.

## Headline diagram

![Diagram 1 from 05_long_term_10y](/tmp/master_plan_compile/diagrams/05_long_term_10y__1.png)


## Long-term strategic objectives

Inherited from H2 and H3 in the strategic roadmap, refined here.

### H2 closing (Years 7 to 10)

- **SO-H2.1 · First regulated product.** FDA clearance for the first Cytonome-powered or Cytoscope-powered product. Single most consequential commercial milestone of the decade.
- **SO-H2.2 · Scale deployment.** ≥10,000 federated devices in the field with post-market surveillance live; UBAP v2+ adopted by ≥5 third-party biosensor partners.
- **SO-H2.3 · Ecosystem ignition.** Open substrate adopted in academic curricula, replicate-and-extend studies, and at least one independent open derivative platform.
- **SO-H2.4 · PBC operational.** PBC raising follow-on rounds at terms that preserve the Helix structure; royalty stream to Foundation funding core mission operations.

### H3 opening (Years 10 to 15, line of sight)

- **SO-H3.1 · Regional sister organizations.** 3 to 5 regional entities (LATAM, EU, Africa, SE Asia) federated to the Foundation, each independently governed and locally trusted.
- **SO-H3.2 · Multilingual, multi-regional.** 20+ languages supported in Cytonome; regulatory clearance in ≥5 jurisdictions; multi-ancestry validation completed for the open map.
- **SO-H3.3 · Policy and standards leadership.** WHO-level policy contributions; de-facto interoperability standards adopted; UBAP recognized as the open standard for individualized biosensor integration.
- **SO-H3.4 · Substrate handoff.** Open substrate and core IP transitioned to a multi-stakeholder steward; Foundation continues as one of several stewards or sunsets per Bylaws Article XIII review.

## Long-term programs

### Cytoverse at clinical-grade scale

By Year 10, the open map covers ≥5 indications: neuropsychiatric (the original pilot, plus expansion to mood, anxiety, psychotic, attention, autism axes), neurodegenerative (MCI to AD; Parkinson's), autoimmune transdiagnostic (UK-led: SLE, RA, Crohn's, MS, psoriasis), metabolic (extending the CGM revolution beyond glucose), cardiovascular (with at least one partnership covering CV biomarker integration). Annual release cadence carries through this expansion.

### Cytoscope multi-modal sensor ecosystem

By Year 10, Cytoscope has graduated from off-the-shelf integration to a programmable multi-analyte platform, co-developed through the ARPA-H Delphi collaboration or its successor and through the Caltech molecular-monitoring FRO. Targets: 10 to 20 analytes simultaneously, programmable post-manufacturing, consumer pricing band ≤$200/device annual subscription model akin to OpenAI/Claude consumer plans but tied to health monitoring. Subscription replaces unit purchase as the dominant revenue model.

### Cytonome consumer product

By Year 10, Cytonome v2.x is the consumer-grade product. Bidirectional voice interface with sub-500ms latency. Long-term memory with user-auditable storage. Personalized causal recommendation in the three-mode framework: defensive (avoid), corrective (reverse), supportive (cope). Crisis-detection module continuously updated as standard of care evolves. Edge-first; raw data never leaves device; aggregated insights flow back through the four-tier compute architecture (perception, local, distributed, Cytognosis layer) only with explicit user consent and DP budget accounting.

### Federated learning at scale

By Year 10, federated learning runs across ≥50,000 devices with formal differential-privacy budget accounting at the device level. The substrate is post-quantum-safe end-to-end (NIST PQC compliant). Aggregation runs over encrypted embeddings only; training data stays on device. The federated architecture is what lets the open Cytoverse map continue improving from real-world distribution shift without violating the bifurcation rule (proprietary individual data stays proprietary; aggregated, consented, DP-bounded insights flow to the open map).

### Regional federation (H3 opening)

Years 10 to 15 line-of-sight: regional sister organizations (LATAM, EU outside UK, Africa, SE Asia, possibly East Asia) each:

- governed by a local board with local stakeholders;
- operating in local languages with locally validated cohorts and locally appropriate sensors;
- licensing the Cytoverse map and the UBAP standard from the Foundation;
- supported by regional philanthropic funding (Gates, Wellcome, regional foundations);
- focused on emerging-market access, where subsidy or low-cost sensor variants are the binding requirement.

The federation model resists the colonial-research pattern of large-Western-institution-extracts-from-low-resource-region. Regional entities are not branches; they are sovereign peers in a federation with shared infrastructure.

### WHO and standards work

Years 8+: explicit policy track. UBAP submitted to relevant standards bodies as a recommended practice. Cytognosis contributes to WHO digital health and AI-in-health policy work. The open map is positioned as international scientific infrastructure, accessible across regulatory regimes.

## Long-term financial picture

| Year | Foundation target | PBC target | Combined notes |
|---|---|---|---|
| Y7 | $5-10M non-dilutive | First major scaling round (Series B equivalent) | PBC funds engineering and continuous data ops |
| Y8 | $5-10M | Same | Foundation expands UK office; regional scoping starts |
| Y9 | $5-10M plus growing royalty | Series C target | Royalty stream becomes material |
| Y10 | $5-15M plus royalty | Approaching break-even | Gate 2 pack assembled |
| Y11-Y15 | Stable mission funding | Self-sustaining | Regional federation funded by mix of regional philanthropy and Foundation pass-through |

The Foundation does not raise from VCs at any point. The PBC raises VC under terms that preserve Helix governance. Royalty mechanics are documented in `23_open_science_and_ip.md`.

## Long-term hiring and footprint

| Phase | US HQ (SSF) | UK office (Manchester) | Regional partners | Total |
|---|---|---|---|---|
| End Y7 | 25 to 35 | 8 to 12 | 0 to 1 scoping engagements | 35 to 50 |
| End Y10 | 50 to 100 (incl. PBC engineering) | 20 to 40 | 1 to 2 active partnerships | 70 to 140 |
| End Y15 | Coordinator role | Peer regional org | 3 to 5 sister orgs | Federation |

The H2 to H3 transition shrinks the central headcount as regional capacity grows. By Year 15 the Foundation is primarily a coordinator and standards body, not a research operator at the same scale. This is intentional: the mission is met when the work is happening everywhere, not when it is happening centrally.

## Risks that bind the long-term plan

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| FDA pathway changes mid-program (e.g., new AI/ML guidance) | Medium | Catastrophic | Continuous engagement with FDA DHCE from Y2; regulatory team in-house by Y4; pivot agility built into product architecture |
| PBC mission drift after VC entry | Medium | Catastrophic | Bylaws Articles VI and XI; board composition requirements; people-as-seed-funders alignment; PAC binding rights |
| Privacy incident at scale | Low | Catastrophic | Edge-first architecture; DP probes on every release; zero raw-data egress SLO; post-quantum substrate; bug bounty program by Y6 |
| Regional partnerships fail to develop | Medium | High | Federation is gradual; if regional partners do not emerge, Foundation continues central operation longer with explicit equity-of-access mitigation (subsidy program, open-source clones) |
| Ecosystem alternative emerges | Medium | High | UBAP and the open map make us the open standard; commercial differentiation is at the navigator and continuous tracking layer, not at the open map layer |
| Talent attrition as PBC matures | Medium | High | Promise-of-future-equity vests over Y5-Y10; Foundation career path remains viable through perpetual mission |
| Climate or geopolitical disruption affecting US or UK base | Medium | High | Regional federation creates structural resilience; no single jurisdiction holds all the operating capacity |

## Cross-references

- The Foundation-PBC governance and IP-licensing terms that fund this entire arc: `20_organization_helix.md` and `23_open_science_and_ip.md`.
- The PAC role that grows multi-continental in this period: `21_patient_advocacy_council.md`.
- The full milestone map across all horizons: `40_milestones_and_kpis.md`.
- The risk register in detail: `41_risks_and_mitigations.md`.






# Section: 10_platform_architecture.md


# Platform Architecture: GPS for Health

**Companion to:** `11_technical_track_FMs.md`, `13_sensor_ecosystem.md`, `14_navigation_recommendations.md`, `15_app_design.md`, `16_patient_safety_architecture.md`

The Cytognosis Platform is what we build. It has three components, in plain language: a **map** (Cytoverse), a **sensor** (Cytoscope), and a **navigator** (Cytonome). Together they are GPS for Human Health. Everything else in the plan, scientific bets, organizational design, funding structure, exists to make this platform real and to make it serve the mission.

## The integrated picture

![Diagram 1 from 10_platform_architecture](/tmp/master_plan_compile/diagrams/10_platform_architecture__1.png)


The diagram looks like a simple pipeline. The reality is bidirectional and continuous: sensors stream into the map, the map updates each individual's coordinates in real time, the navigator reads coordinates and produces recommendations, the recommendations become interventions, the interventions are themselves logged data that feeds the next cycle.

## Cytoverse: the map

| | |
|---|---|
| **Role** | AI health mapping system |
| **Output** | Continuous, multimodal coordinates across micro, meso, and macro biological scales for any individual |
| **Foundation pillars used** | P1 (Cytoverse) primary; P4 (Open-Science Substrate) as the substrate it ships on |
| **Bifurcation status** | Pre-36m and post-36m **OPEN**. Foundation perpetually owns. Annual major releases. |
| **Pilot indication** | Mental health (neuropsychiatric transdiagnostic) |

Cytoverse replaces categorical disease labels (depressed / not depressed) with continuous health coordinates analogous to latitude and longitude in GPS. At every scale, it learns axes that explain variation across individuals, and it does so jointly across scales rather than sequentially.

The three biological scales:

| Scale | Near-term modality (research-grade) | Long-term modality (wearable / continuous) |
|---|---|---|
| **Micro** | Genomic (WGS) plus single-cell transcriptomics and epigenomics | Circulating cell-free molecular signatures via Cytoscope biosensors |
| **Meso** | Neuroimaging (fMRI, structural MRI, dMRI, PET) | Wearable neuro-monitoring (consumer EEG, fNIRS) |
| **Macro** | LLM-derived phenotypic assessment plus EHR | Wearable physiology plus passive ambient sensing |

Concrete H1 deliverables across the three scales are detailed in `03_short_term_1to2y.md` and `04_mid_term_5to6y.md`. The technical architecture, including the parallel cellular and connectomic foundation models with shared building blocks, is in `11_technical_track_FMs.md`.

The central scientific bet: cross-scale paired modeling lets inexpensive, always-on signals (wearable) stand in for expensive, episodic ground truth (clinical). This is the "cross-modal imputation" premise that powers the H2 product, and it is what the Year 4 to Year 5 clinical study is designed to validate against the proprietary continuous dataset.

## Cytoscope: the sensor

| | |
|---|---|
| **Role** | Programmable, universal sensor layer that triangulates individual coordinates on the Cytoverse map |
| **Output** | Continuous, multivariate biological data across molecular, connectomic, and phenotypic modalities |
| **Foundation pillars used** | P2 (Cytoscope) primary; P5 (Clinical Translation) for hardware regulatory; P4 for the open UBAP standard |
| **Bifurcation status** | **Mixed**. The UBAP open spec is permanent open property. Cytoscope hardware lineage from Y4 onward is proprietary, owned by the PBC. Hardware design that is published or co-developed with open partners (Delphi, Caltech FRO) follows partner-specific licensing. |
| **Architecture** | Plug-in ecosystem. Any sensor that implements UBAP can feed into the navigator. |

Cytoscope is not one device. It is a universal interface plus a specific lineage of hardware that we develop directly or co-develop with partners.

The full spec of the universal sensor adapter, what counts as a sensor, how plug-ins are certified, and how the open standard relates to the proprietary hardware, is in `13_sensor_ecosystem.md`. The headline:

- **Sensors are categorized by biology** (molecular, connectomic, phenotypic), not by physical form.
- Each category has both **clinical/episodic** and **wearable/continuous** members.
- The interface is open; the standard is owned by the Foundation; specific hardware implementations may be open or proprietary depending on the partner.

This design lets companies, labs, hospitals, and academic groups build plug-ins that bring their signals into our 360-degree health picture without giving us their raw data, while still allowing the navigator to use those signals as intermediate state for causal prediction of health outcomes.

## Cytonome: the navigator

| | |
|---|---|
| **Role** | Privacy-first edge AI that converts real-time coordinates into causally grounded recommendations |
| **Output** | Personalized recommendations in three modes: defensive, corrective, supportive |
| **Foundation pillars used** | P3 (Cytonome) primary; P6 (Helix) for the privacy and safety substrate |
| **Bifurcation status** | **Mixed**. Pre-36m components (privacy spec, three-layer architecture, on-device runtime, crisis detection, voice interface, memory module, ontology-grounded passive sensing) are open. Post-36m proprietary components (continuous personal causal model trained on the proprietary continuous dataset; navigation policy informed by continuous tracking) are PBC. |
| **Compute** | Four-tier: perception layer (phone), local layer (personal node), distributed layer (community substrate), Cytognosis layer (central training and discovery). |

Cytonome is the consumer-facing component. Most users will experience the platform through it: as a guardian-coach app on their phone that knows their history, tracks their state, and helps them navigate their health day to day.

The recommendation framework, defensive (avoid), corrective (reverse), supportive (cope), is the canonical taxonomy across the entire plan. Detail in `14_navigation_recommendations.md`. The app design, including sections for sensors, interventions, patient care, clinical trials, and patient communities, is in `15_app_design.md`. The four-tier compute and patient-safety architecture is in `16_patient_safety_architecture.md`.

## The supporting pillars

Cytoverse, Cytoscope, and Cytonome are the three core pillars (P1, P2, P3). Three supporting pillars make them durable, deployable, and trustworthy.

| Pillar | Function | Relationship to platform |
|---|---|---|
| **P4 · Open-Science Substrate** | Schemas, licenses, templates, dataset packaging, model cards, governance protocols | Enforces openness across all three core pillars; CI release pipeline gates every public artifact |
| **P5 · Clinical Translation** | IRB infrastructure, regulatory strategy, clinical partnerships, trial design, evidence | Carries the platform across the regulatory boundary at Gate 1 and Gate 2 |
| **P6 · Organization and Helix** | Foundation + PBC structure, talent, finance, US + UK + regional federation, governance, PAC | Carries the mission, makes the bifurcation work, ensures equity of access |

All six pillars work simultaneously across all three horizons. Their relative emphasis shifts: H1 weights P1 and P4 most heavily; H2 weights P2, P3, P5; H3 weights P6 (regional federation) and P4 (substrate handoff).

## Three forms of data, one foundation model

The model integrates three forms of data, each with its own role:

![Diagram 2 from 10_platform_architecture](/tmp/master_plan_compile/diagrams/10_platform_architecture__2.png)


The Cytoverse map acts as the **mediator variable** in the causal chain from interventions and genetic factors to clinically and personally relevant outcomes. This mediator role is what makes the navigation recommendations causal rather than associational, and it is what makes counterfactual estimation possible: with the map fixed as a state representation, we can ask "what would happen to this person if they took this intervention given this genotype and this current state?"

## Why the architecture is what it is

Several architectural decisions are answers to specific failures of existing systems:

- **Continuous coordinates instead of categorical labels.** Categorical diagnoses collapse heterogeneity. Continuous coordinates preserve it and let us see the early shifts that categorical labels cannot.
- **Multi-scale coupling.** Single-scale models miss cross-scale invariants. By pairing micro, meso, and macro through end-to-end training, we capture what each scale alone cannot.
- **Edge-first compute.** Every cloud-based health platform faces the trust ceiling at scale. Edge-first puts the most sensitive inference where the data already lives, the user's device.
- **Open map plus proprietary navigator.** A single closed platform cannot win the trust of a global mission. A single fully-open platform cannot fund the engineering and continuous data work needed to keep the navigator current. The bifurcation is the deliberate compromise that gets both.
- **Universal sensor interface.** Locking in to one sensor vendor or one biology is the failure mode of nearly every health-tech company that came before us. UBAP says: the platform is the standard, not the device.
- **Patient Advocacy Council with binding rights.** Every previous attempt at participant-centered health tech put participants on advisory committees with no veto. The PAC has veto on participant-impacting decisions because care is one of our values, not a slogan.

## Cross-references

The deep technical implementation is in `11_technical_track_FMs.md`. The clinical-to-wearable alignment is in `12_clinical_to_wearable.md`. The sensor ecosystem detail is in `13_sensor_ecosystem.md`. The navigation framework is in `14_navigation_recommendations.md`. The app, four-tier compute, and patient safety are in `15_app_design.md` and `16_patient_safety_architecture.md`. The organizational structure that funds and governs all of this is in `20_organization_helix.md` and `21_patient_advocacy_council.md`.






# Section: 11_technical_track_FMs.md


# Technical Track: Parallel Cellular and Connectomic Foundation Models

**Companion to:** `10_platform_architecture.md`, `12_clinical_to_wearable.md`, `appendix/A_cell_state_meeting_synthesis.md`
**Source meeting:** Cell-State / Perturbation Modeling, 2026-05-07 (Shourya Verma, Mango Wang, Nadia Atallah Lanman, Ananth Grama, Shahin Mohammadi)

This document captures the architectural decisions for the Cytoverse foundation-model stack. It is the most technically detailed document in the master plan. Engineering reviewers, methods reviewers, and grant reviewers asking about scientific approach should start here.

## Headline architectural decision

Build cellular and connectomic foundation models **in parallel**, sharing the same architectural building blocks but operating at two different biological scales. The Purdue team and Mohammadi confirmed this on 2026-05-07. Shourya Verma leads both tracks given Mango's transition to Meta. Mango contributes as bandwidth allows.

The shared building blocks:

- **Multi-resolution graph diffusion** using components from WaveGC (Wave Graph Convolution).
- **Cross-resolution information sharing** using interconnected transformer blocks introduced in AlphaGenome.
- **Multi-scale nested foundation models** with the molecular FM trained end-to-end with the cellular FM, not used as a frozen dictionary.
- **Conditional flow matching for residuals**, modeling disease as a delta from healthy baseline rather than absolute state.

## The general framework

![Diagram 1 from 11_technical_track_FMs](/tmp/master_plan_compile/diagrams/11_technical_track_FMs__1.png)


The same framework applies at two scales:

| Element | Cellular FM | Connectomic FM |
|---|---|---|
| **Measurement units** | Genes | Voxels (anatomical bins, similar to epigenome bins) |
| **Unit embedding source** | Molecular FM (e.g., AlphaGenome, ESM, EVO2) | Spatial / anatomical embedding |
| **Context-specific signal** | Single-cell or pseudobulk RNA-seq, ATAC-seq | fMRI BOLD, dMRI tractography, PET |
| **Event / conditioning** | Cell type, tissue, treatment, disease | Stimulus, task, resting-state, condition |
| **Network construction** | All-pairs (genes are countable) or KNN | KNN sparsified (voxels are not) |
| **Pre-training task** | Masked unit prediction; perturbation prediction | Stratified subgraph masking (e.g., predict amygdala or hippocampus activity from rest of brain) |
| **Prototyping data** | PsychENCODE pseudobulk | Open Era Y dataset (~300 samples), then Yale, then UK Biobank |
| **Lead** | Shourya (lead), Mango (contributor), Mohammadi (advisor) | Shourya (lead), Mohammadi (advisor) |
| **Repository** | `neurogenomics`, `neurotranscriptomics` | `neuroconnectomics` |

## Why WaveGC and why AlphaGenome blocks

### WaveGC for multi-resolution

WaveGC defines wavelet atoms and bases for signal projection on graphs using efficient Chebyshev approximations to avoid matrix factorization. It produces a multi-resolution decomposition: for each scale, a vector representation of the signal at that scale. This matches our scientific need: biology operates at multiple scales (gene to pathway to cell type; voxel to region to network), and forcing a single-resolution representation discards information.

The known weakness of WaveGC: each scale operates independently. The MLP block that processes resolutions does not share information across scales. This is exactly the limitation we replace.

### AlphaGenome cross-resolution attention

AlphaGenome's interconnected transformer blocks structure information sharing **across** scales. Each block represents a scale, and attention across blocks lets the model decide, for each unit and each context, which scales matter and how they combine. We adopt this pattern as the replacement for WaveGC's MLP block.

The result is a multi-resolution network with explicit cross-resolution information transfer. Cell biology and brain biology both have this property: pathway-level patterns inform gene-level prediction, region-level patterns inform voxel-level prediction. The model captures both.

## The "Lego pieces" infrastructure layer

A core decision from the 2026-05-07 meeting: the multi-resolution wavelet plus cross-scale attention layer is implemented as a **standalone reusable package** inside the `neuroconnectomics` repo, but used by both connectomic and cellular tracks. Mohammadi referred to this as "Lego pieces": wrapped, standardized interfaces declaring inputs and outputs so models can be mixed and matched without manual rewiring.

This is what makes parallel development tractable. Both tracks consume the same package; both tracks contribute back to the same package; benchmarks at the package level apply to both. When one track finds a bug or improvement, both tracks benefit.

![Diagram 2 from 11_technical_track_FMs](/tmp/master_plan_compile/diagrams/11_technical_track_FMs__2.png)


## Multi-scale nested foundation models

The most consequential design choice in the cellular FM, and the one that distinguishes our work from scPrint2 and TranscriptFormer.

### How scPrint2 and TranscriptFormer use molecular FMs

Both treat a molecular foundation model (e.g., ESM for protein sequences, AlphaGenome for genomic sequences) as a **frozen dictionary**: gene embeddings are looked up at training time, but the molecular FM is never updated. This is computationally cheap and decouples the molecular and cellular layers, but it has structural costs:

- the molecular embeddings cannot adapt to cellular context;
- the cellular FM cannot push gradient signal back into the molecular layer to learn what aspects of molecular identity matter for which cellular phenomena;
- end-to-end training across molecular and cellular scales is impossible;
- multi-scale phenomena (a missense variant changes protein folding which changes cellular network behavior) cannot be modeled jointly.

### How we do it differently

The molecular FM is a **trainable component** of the cellular FM, connected through the cross-resolution attention blocks. The metric space induced by molecular embeddings, together with appropriate kernels, defines the molecular graph that acts on the context-specific cellular signal. Gradient flows end-to-end through both scales. The molecular FM at the start of training resembles the published model (e.g., AlphaGenome); after fine-tuning, the molecular layer has learned cellular-context-aware representations.

This is more expensive computationally. It is also fundamentally what gives us the cross-scale modeling capability that the static-dictionary approach forecloses. The Astera proposal funds this approach explicitly because it is a research bet that scPrint2 and TranscriptFormer cannot make.

![Diagram 3 from 11_technical_track_FMs](/tmp/master_plan_compile/diagrams/11_technical_track_FMs__3.png)


## Conditional flow matching of the residual space

The third architectural decision: model the **residual space** rather than the baseline.

### Why residuals

In every layer of biology, the disease shift is a sparse perturbation on a much larger healthy baseline. If we model the absolute state, the model spends most of its capacity learning healthy biology and very little on disease shifts. If we model the residual (the delta from healthy baseline), the entire model capacity goes to the signal that matters for disease detection and intercept.

Individual genomic variation is **already** a residual concept: each genome differs from the reference at specific positions. Differential expression is the residual concept at the cellular layer. Disease-axis shifts in connectomic data are the residual concept at the connectomic layer. By converging the entire stack to the language of residuals, we make all layers and scales speak the same language.

### Conditional flow matching

We use conditional flow matching (CFM), a class of generative models that learn to create the residual embeddings from noise, conditioned on health-state context. The model produces counterfactual cells (or counterfactual brains, or counterfactual phenotypes) that are as close as possible to the original observation when run through the corresponding decoder, measured against population distance metrics like Maximum Mean Discrepancy (MMD).

This gives us:

- a generative tool for synthesizing health-state counterfactuals (what would this cell look like under intervention X?);
- a principled way to evaluate the quality of disease-axis discovery (do generated counterfactuals match observed perturbations?);
- a unified language for cross-scale residual modeling.

## The four repositories

Decision from the 2026-05-07 meeting:

| Repository | Scope | Lead |
|---|---|---|
| `neurogenomics` | Genome-level work: WGS, GWAS-style, polygenic scoring, baseline molecular FM fine-tuning | Mohammadi (initial), AI/ML hire |
| `neuroconnectomics` | Connectomic FM, voxel-level work, multimodal imaging integration. **Hosts the shared `neuroconnectomics-core` Lego-pieces package.** | Shourya Verma |
| `neurotranscriptomics` | Cellular FM, single-cell + pseudobulk, multi-scale molecular-to-cellular work | Shourya Verma + Mango (when bandwidth allows) + Mohammadi |
| `neurobehavior` | Macro phenotyping, LLM-derived neurobehavioral axis quantification, NBO ontology integration | Mohammadi (initial), ML hire |

A `neurogenomics` Cookiecutter template will be created (Mohammadi action item from the meeting) so each repo bootstraps with the Cytognosis dev-standards (Python, ruff, mypy, nox, pre-commit, src-layout, CI).

## Pre-training tasks and benchmarks

### Connectomic track

- **Pre-training task.** Stratified subgraph masking. Mask voxels in specific anatomical regions (e.g., amygdala, hippocampus) and predict their activity from the rest of the brain. Hard task chosen for representation learning. Allows region-specific evaluation.
- **Initial prototyping data.** Open Era Y dataset (~300 samples, harmonized). Mohammadi to send paper and code link.
- **Scale-up data.** Yale dataset (Shourya to secure access). Then UK Biobank (≥40,000 fMRI). Then ABCD, HCP.
- **Downstream tasks.** Disease label prediction; subtype prediction; HiTOP factor recovery; cross-cohort validation.

### Cellular track

- **Pre-training task.** Masked gene prediction conditioned on cellular context. Perturbation prediction (predict expression under treatment given baseline). Multi-task with the connectomic stratified-masking objective for shared infrastructure.
- **Prototyping data.** PsychENCODE pseudobulk first (open). NeuroBioBank WGS (10K+ donors) for genotype-phenotype joint training. Allen Brain Atlas microarray data for connectomic deconvolution alignment.
- **Downstream tasks.** Cell-type-specific expression prediction; perturbation outcome prediction; PGC 14-condition recovery; Grotzinger 5-factor recovery.

### Cross-track integration

The decisive long-term technical bet: bridges between the cellular and connectomic FMs trained on **paired data** (the same individual or cohort with both connectomic and cellular measurements). The ENIGMA consortium dataset is the central paired resource: disease-centric, multimodal, with both fMRI and genotype data. PsychENCODE has 388 paired WGS plus single-cell plus connectomics where available.

The integration strategy uses cross-attention or contrastive loss objectives, with the alignment task simplified by the fact that each individual model is already oriented toward predicting phenotype.

## What is intentionally out of scope for the first multi-scale paper

Per the meeting: the **first publication** focuses on the multi-scale infrastructure connecting molecular and cellular data. The connectome is **excluded** from this first paper to keep the scope clean. The connectomics work continues in parallel (Shourya leads it) but the methods paper for the connectomic side is a separate output. Mohammadi noted that the methodology paper is a strong fit for Nature Methods or Nature Machine Intelligence; Nature Machine Intelligence is rapidly growing in impact factor and emphasizes methodology over result-centric framing.

## Architectural questions still open

These are the explicit unknowns the team is investigating:

- **Projection back to original space.** Does each spectral graph convolution layer need to project back to the original space, or only the outermost layer? Affects the standard interface design for the Lego-pieces package. Resolution target: end of May 2026 visit to Purdue.
- **Standard embedding layer interface.** What does the unit-and-embedding combination interface look like as a clean API that both tracks can consume?
- **Conditioning structure for conditional flow matching.** What forms of conditioning (categorical disease label, continuous health-state coordinate, individualized prior from genome) work best? Likely answer: all three, ablated.
- **Computational scaling.** End-to-end multi-scale training with trainable molecular FM is expensive. What is the scaling regime? What are the decision points where we trade end-to-end training for partial freezing?

## Three-to-six-month milestone planning

Mohammadi tentatively planning a Purdue visit at end of May or early June 2026 to white-board these questions and produce a concrete three-to-six-month milestone schedule with quantitative success metrics and specific submission venues. Professor Grama offered to cover travel reimbursement.

Output of the visit will be added to Monday Strategic Initiatives `SI-Neuroverse-Micro`, `SI-Neuroverse-Meso`, and `SI-Neuroverse-Macro-LLM` as updated KRs and milestones, and to the Phase 1 Operational Plan as updated OKR detail.

## Cross-references

- The platform-level role of these models: `10_platform_architecture.md`.
- The clinical-to-wearable alignment that uses these models as the "clinical" anchor: `12_clinical_to_wearable.md`.
- The full meeting record this section synthesizes: `appendix/A_cell_state_meeting_synthesis.md`.
- The funding strategy that supports this work, primarily Astera (micro) and Google.org Impact (meso): `30_funding_strategy.md`.
- Repository creation and bootstrapping: dev-standards skill (cookiecutter template).






# Section: 12_clinical_to_wearable.md


# Clinical-to-Wearable Alignment

**Subtrack:** T15 (new in v2.0) under M5 Learning
**Companion to:** `04_mid_term_5to6y.md`, `11_technical_track_FMs.md`, `13_sensor_ecosystem.md`

The clinical-to-wearable alignment subtrack is the bridge that lets H1 open work inform the H2 proprietary clinical study and the H2+ continuous tracking product. Without it, the Year 4 clinical study has no priors and the Year 7+ tracking product has no validated translation between the rich clinical signals it cannot capture continuously and the inexpensive signals it can.

This subtrack runs from Year 1 through Year 5 with three phases of increasing scope.

## Why this subtrack exists

After 36 months we transition from learning the open Cytoverse map (using public, consortium, and consented core-team data) to learning the proprietary continuous-tracking layer (using the clinical-trial cohort with paired clinical and wearable measurements over 12 months).

The transition has a hard scientific dependency: we need to know how to translate from clinical-grade modalities to wearable modalities, on the same individual. This is not the same as classifying disease from a wearable signal. It is the harder problem of reproducing the rich representation a clinical-grade modality produces, using only the cheap continuous signal.

Three concrete examples:

- **fMRI to fNIRS.** fMRI captures whole-brain hemodynamic signal at high spatial resolution but requires a magnet. fNIRS captures cortical hemodynamic signal at the wearable-headset level. We need a translation model that produces fMRI-quality representation from fNIRS data, calibrated per individual.
- **Clinical-grade EEG to consumer EEG.** Research-grade EEG (g.Nautilus 64 channels) captures dense electrical activity. Consumer EEG (Muse S Athena, Emotiv Insight) captures sparse activity at much lower channel count. Translation requires learning what each consumer channel proxies in the dense space.
- **Structured clinical assessment to passive conversational tracking.** Clinicians administer PHQ-9, GAD-7, and full structured interviews. The Cytonome macro LLM infers the same axes from passive conversation. Translation is a regression task with carefully labeled paired data.

## Three-phase plan

### Phase A: Public-data prep (Years 1 to 2)

Before any internal data collection or clinical study, build alignment models against publicly available paired datasets. Two anchors:

**Inclusion Study (OpenNeuro ds006377).** "Quantifying the impact of hair and skin characteristics on fNIRS signal quality for enhanced inclusivity," published in Nature Human Behaviour 2025. Public dataset with paired fNIRS measurements stratified by hair and skin characteristics. The dataset is exactly what we need to make sure our alignment models do not silently fail on under-represented populations. Equity is built into the alignment subtrack from the start.

**FRESH initiative (OSF b4wck).** "fNIRS reproducibility varies with data quality, analysis pipelines, and researcher experience," published in Nature Communications Biology 2025. Public dataset and analysis pipeline benchmarks. Lets us train alignment models with full pipeline awareness and lets us reproduce community benchmarks before we publish.

**Outputs by end of Year 2:**

- alignment-model v0 from fNIRS to fMRI representation, trained on public data;
- equity audit framework: how does alignment quality vary across hair, skin, age, gender? What sensor configurations and what training data corrections does the equity gap require?
- consumer-EEG to research-EEG channel mapping baseline using public datasets;
- conversation-to-PHQ-9 and conversation-to-GAD-7 baseline models (these reuse work from the macro LLM track).

### Phase B: Internal core-team pilot (Years 2 to 3)

Consented internal core team (3 to 5 people) wears research headsets (fNIRS plus EEG) plus undergoes initial clinical fMRI plus EEG. This is the dress rehearsal: the same individual wears every modality so we can validate alignment models end-to-end on the same person.

![Diagram 1 from 12_clinical_to_wearable](/tmp/master_plan_compile/diagrams/12_clinical_to_wearable__1.png)


The pilot is small (intentionally) because the goal is validation of the alignment pipeline, not statistical power for cohort-level claims. The dataset is released as an open public good under CC BY 4.0 with consent and DP gating.

### Phase C: Cohort-scale (Years 4 to 5, proprietary track)

The Year 4 to Year 5 clinical study is detailed in `04_mid_term_5to6y.md`. From the alignment subtrack's perspective, it is the data source that turns Phase A and Phase B priors into production-grade alignment models. Cohort size 200, duration 12 months, paired clinical and wearable on every individual, equity stratification baked in from the Inclusion Study experience.

After the clinical study, alignment models become **proprietary** under the bifurcation rule. The Foundation continues to maintain the **open** alignment models trained on public and core-team-pilot data; the PBC owns the cohort-trained models that power the H2+ continuous tracking product.

## Key technical decisions

### Per-individual calibration

Alignment quality is improved substantially by per-individual calibration. Skin pigmentation, hair density, head shape, individual neural anatomy all vary. The Cytonome runtime supports a calibration phase per user where short clinical-grade measurements (one-time fMRI plus EEG plus structured assessment) define an individualized prior that the wearable signal is then read against. This is one reason the H2 product is fundamentally onboarded through a clinical entry point.

### Equity gates

Every alignment model carries a documented equity gate at release time. The release checklist (`SI-Release-Pipeline`) extends to require:

- alignment quality reported across protected attribute strata;
- minimum quality thresholds met for every represented group;
- documented coverage gaps (groups not represented in training data);
- public commitment to expanding cohort coverage in subsequent releases.

This is not a secondary concern. The Inclusion Study exists because fNIRS literature systematically under-represents non-white-skin and non-straight-hair populations. We refuse to ship alignment models that fail on the same populations.

### Hardware partner choices

We are partner-first on hardware through Year 3. Decisions on hardware partners depend on equity quality, openness of SDK, and continuity of supply.

| Modality | Y1-Y2 partner candidates | Notes |
|---|---|---|
| fNIRS wearable | Kernel, OpenBCI Galea, Artinis | Kernel for clinical-grade portability; Galea for the open hardware ethos; Artinis for academic continuity |
| Consumer EEG | Muse S Athena, Emotiv Insight | Muse for affordability and developer ecosystem; Emotiv for higher channel count |
| Research-grade EEG | g.Nautilus 64-channel | Reference standard |
| Wearable physiology | Oura Ring 4, Apple Watch, Whoop | Oura for sleep and HRV; Apple Watch for ECG and reach; Whoop for continuous strain |
| Wet-lab molecular (clinical) | Standard clinical labs (Quest, LabCorp); UK partner labs | For the trial cohort baseline |
| Future biomolecular (continuous) | ARPA-H Delphi (cooperative agreement) | Programmable, multi-analyte; Y4+ |

Hardware decisions are reviewed annually as the field changes rapidly.

## Risks specific to this subtrack

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| fNIRS-to-fMRI alignment is too lossy | Medium | High | Multimodal fusion (fNIRS plus EEG plus physiology together) recovers more than fNIRS alone; the goal is "good enough on enough axes" not "fMRI-equivalent" |
| Equity gap in alignment quality is structural and unfixable | Low | Catastrophic | If unfixable, the affected modality is not deployed for the affected population; we ship inclusive subset |
| Public data is insufficient to train robust priors | Medium | Medium | Internal core-team pilot fills the gap; Phase B is exactly designed for this |
| Calibration burden too high for end users | Medium | High | Calibration phase is part of the clinical onboarding (already a touchpoint); duration target ≤2 hours |
| Hardware partner discontinues or pivots | Medium | Medium | Multi-vendor strategy; UBAP open standard ensures replacement-ability |

## Cross-references

- The cohort design and protocol that drives Phase C: `04_mid_term_5to6y.md`.
- The technical FM stack the alignment models build on: `11_technical_track_FMs.md`.
- The sensor ecosystem and UBAP standard: `13_sensor_ecosystem.md`.
- Equity and openness rules that gate alignment-model releases: `23_open_science_and_ip.md`.
- The privacy architecture that moves alignment-model inference to the edge: `16_patient_safety_architecture.md`.






# Section: 13_sensor_ecosystem.md


# Sensor Ecosystem and Universal Biosensor Adapter Protocol (UBAP)

**Companion to:** `10_platform_architecture.md`, `12_clinical_to_wearable.md`, `15_app_design.md`

Cytoscope is not one device. It is a universal interface plus a specific lineage of hardware we develop directly or co-develop with partners. The interface is open; the standard is owned by the Foundation; specific hardware implementations may be open or proprietary depending on the partner.

## What counts as a sensor

A "sensor" is anything that produces a measurement of a person's biology, physiology, behavior, or environment. We organize sensors along two axes: **biology** (what they measure) and **deployment context** (how they are deployed).

| Biology | Clinical / episodic | Wearable / continuous |
|---|---|---|
| **Molecular** | Clinical labs (blood draws, biopsies, cytology, molecular panels) | CGM, future biomolecular sensors (ARPA-H Delphi class) |
| **Connectomic** | fMRI, structural MRI, dMRI, PET, research-grade EEG | fNIRS wearable headsets, consumer EEG |
| **Phenotypic** | Clinical interview, structured assessments, neuro exam | Wearable physiology (HRV, sleep, activity), passive ambient sensing |
| **Behavioral** | Standardized neuropsych tests | Conversation tracking via Cytonome, social-context proxies |

Each cell of this matrix is a sensor category. UBAP is the open standard that lets any device or service in any cell feed into the navigator without bespoke integration.

## Universal Biosensor Adapter Protocol (UBAP)

![Diagram 1 from 13_sensor_ecosystem](/tmp/master_plan_compile/diagrams/13_sensor_ecosystem__1.png)


### What UBAP specifies

- **Measurement type.** What is being measured (analyte, voltage, hemodynamic signal, behavioral count, etc.) with structured ontology link (CHEBI, UBERON, NBO, SNOMED CT, ICD-11 as appropriate).
- **Unit.** SI or field-standard unit, machine-readable.
- **Uncertainty.** Each value carries an explicit uncertainty estimate (standard error, confidence interval, or distributional summary), or a documented reason for absence.
- **Sampling regime.** Continuous, event-driven, scheduled, sporadic. Frequency or trigger conditions specified.
- **Biological meaning.** Link to the relevant Cytoverse axis or axes; a human-readable description of why this signal matters.
- **Provenance.** Device model, firmware version, calibration history, signal-processing pipeline version. Enables reproducibility and audit.
- **Consent metadata.** What consent the participant has given for what use of this data, in machine-readable form, so the navigator can enforce participant choice automatically.

### What UBAP does not specify

- The signal-processing pipeline inside the device. Vendors are free to compute their own derived metrics. UBAP only specifies the contract at the boundary.
- The device hardware itself. UBAP is a software contract.
- Whether the data is shared with Cytognosis. UBAP describes the data; the consent metadata says what can happen with it.
- Whether the device is open-source. We hope partners will open-source what they can; we do not require it for UBAP conformance.

## Plug-in ecosystem

UBAP is the standard that enables a plug-in ecosystem. Companies, hospitals, academic groups, and individual makers can build plug-ins that bring their signals into the Cytognosis platform without giving us their raw data.

![Diagram 2 from 13_sensor_ecosystem](/tmp/master_plan_compile/diagrams/13_sensor_ecosystem__2.png)


### Plug-in modes

A plug-in can operate in any of three modes, depending on how much the user trusts the plug-in builder and how much the builder is willing to share:

- **Raw signal.** The plug-in sends raw measurements (UBAP-formatted) to the navigator. Most transparent; lowest barrier for the navigator to use the signal.
- **Derived embedding.** The plug-in computes a proprietary embedding and sends only the embedding to the navigator. Useful for vendors who want to protect signal-processing IP. The navigator can still use the embedding as an intermediate state for causal prediction; it just cannot reverse-engineer the raw signal.
- **Local-only.** The plug-in computes derived signals on-device and never leaves the device. Useful for high-sensitivity data. The navigator runs against the on-device output without seeing the underlying signal at all.

All three modes are first-class UBAP citizens. Mode selection is a deployment-time choice.

## Cytognosis-built plug-ins

Cytognosis itself ships several plug-ins as the reference implementations:

| Plug-in | Mode | Notes |
|---|---|---|
| **Apple Watch / Oura / Whoop** | Raw signal | Wearable physiology |
| **Muse / Emotiv consumer EEG** | Raw signal | Consumer EEG, with on-device preprocessing |
| **fNIRS partner headsets** | Raw signal | Per partnership |
| **Standardized clinical-scale instruments** (PHQ-9, GAD-7, HiTOP profile, attachment style, personality, etc.) | Raw signal | Used for both initial calibration and tracking; mapped to universal phenotypic axes |
| **Conversational behavioral tracking** | Local-only | Cytonome's own LLM-derived passive sensing of mood, lifestyle, social context |
| **Lab connector** | Raw signal | Quest, LabCorp, hospital labs via direct connector |
| **Clinical-imaging connector** | Raw signal | DICOM / BIDS receiving from imaging centers |

Future Cytoscope-developed hardware (programmable multi-analyte sensors co-developed with ARPA-H Delphi or the Caltech FRO) becomes a Cytognosis plug-in like any other. Its hardware lineage may be proprietary post-bifurcation, but its UBAP interface stays open.

## How sensors map to the three forms of data

Per `10_platform_architecture.md`, the platform integrates three forms of data: phenotypic outputs, intermediate endophenotypes (mediators), and interventions. Sensors map to all three:

- **Outputs.** Wearable physiology, behavioral tracking, clinical assessments, symptom logs.
- **Mediators.** Imaging (fMRI, fNIRS), molecular markers, cellular signatures from blood-based assays, connectomics.
- **Interventions.** Therapy logs, medication tracking, lifestyle logs, environmental exposures, social-interaction logs.

The navigator's causal modeling requires all three. UBAP supports all three.

## Bifurcation rules for the sensor ecosystem

Per `02_horizons_and_bifurcation.md` and `23_open_science_and_ip.md`:

- **UBAP itself stays open in perpetuity.** Foundation owns the spec, contributes it to standards bodies, and accepts community contributions. Apache 2.0 reference implementation, Apache 2.0 conformance suite.
- **Cytognosis-developed sensor hardware in H1 (Y1 to Y3) is open** by default if Cytognosis funded the hardware design alone, or per partnership terms if co-developed.
- **Cytoscope wearable v1 hardware lineage from Y4+ is proprietary** to the PBC. Its UBAP interface is open; its design is not.
- **Third-party plug-ins** may be open or proprietary at the builder's choice. UBAP conformance is required; openness is encouraged but not mandated.

## Adoption strategy

The single most important measure of UBAP success is adoption by external groups. Strategic Initiative `SI-UBAP-v1` carries the cumulative target: by Year 5, ≥2 external biosensor groups have adopted UBAP; by Year 10, ≥5.

Adoption is encouraged through:

- **Reference implementation in Apache 2.0** (Python and TypeScript) with first-class support.
- **Conformance test suite** so vendors can self-certify.
- **Co-development partnerships** with strategic partners (ARPA-H Delphi, Caltech molecular monitoring FRO, OpenBCI, academic biosensor groups).
- **Submission to standards bodies** at Y6+: IEEE, ISO, HL7-style health data standards.
- **Publication track** that documents UBAP and its use cases in the open scientific literature.

## Risks and limits

| Risk | Mitigation |
|---|---|
| Vendors prefer their own closed standards | Accept that UBAP will not win every partner; focus on the partners who share the open thesis |
| UBAP versioning fragments the ecosystem | Backward compatibility commitment; versioned conformance suite; lighter-weight v1 to broaden adoption |
| Plug-in store creates moderation burden | Tiered approach: open store is community-moderated, licensed store is Cytognosis-curated; tier of trust per plug-in |
| Privacy implications of plug-in store | Every plug-in declares consent metadata; navigator enforces; PAC reviews high-impact plug-ins |
| Hardware churn outpaces standard adoption | Lightweight UBAP v1; rapid iteration on minor versions; deprecate slowly |

## Cross-references

- The platform-level role: `10_platform_architecture.md`.
- App-level integration of plug-ins (sensor section, plug-in store): `15_app_design.md`.
- The clinical-to-wearable alignment that uses UBAP-formatted data on both sides: `12_clinical_to_wearable.md`.
- The bifurcation rules that govern hardware lineage: `02_horizons_and_bifurcation.md`, `23_open_science_and_ip.md`.






# Section: 14_navigation_recommendations.md


# Navigation: Causal Recommendation Framework

**Companion to:** `10_platform_architecture.md`, `13_sensor_ecosystem.md`, `15_app_design.md`, `16_patient_safety_architecture.md`

Cytonome converts a person's continuous health-state coordinates into actionable recommendations. The recommendation taxonomy in this document, defensive, corrective, supportive, is the canonical framework across the entire master plan and is what we use in app design, clinical trial protocols, grant narratives, and PAC review.

## Three modes of navigation

Causal recommendation operates in three distinct modes, each tied to a different relationship between current state and desired state.

![Diagram 1 from 14_navigation_recommendations](/tmp/master_plan_compile/diagrams/14_navigation_recommendations__1.png)


### Defensive (protective)

What to avoid: behaviors, exposures, environments, social interactions, and contexts that, given the current state and personal history, are likely to worsen the trajectory. Learned both from population-level evidence (general patterns) and from personalized history (what has previously triggered this individual).

**Examples:**

- A person with a history of social-anxiety spikes after specific kinds of meetings receives an early warning when a similar meeting is upcoming, with concrete suggestions: arrive earlier to acclimate, take a brief recovery break afterward, plan a calming activity post-meeting.
- A person with a metabolic genotype showing strong evening-meal-glucose coupling receives a default "eat earlier today" recommendation when the day's pattern looks similar to past spike days.
- A person with sleep-mood coupling and a poor sleep night receives a defensive recommendation to skip a particular high-stakes meeting if it can be moved.

### Corrective (therapeutic)

How to reverse, when reversal is possible. Suggestions tailored to the unique biology, biotype, and current health state of the individual that aim to restore a desired state.

**Examples:**

- A person with prediabetes, given their genotype and previous dietary outcomes on observable biomarkers, receives a personalized diet plan tuned to their specific glucose response (the post-CGM finding that potato-spikers respond differently from grape-spikers, but extended to the full molecular orchestra and individual genome).
- A person with a depression biotype that maps to BDNF signaling receives an indication that this biotype responds to specific therapies (such as psilocybin in clinical-trial settings, where appropriate, or evidence-based interventions like exercise that affect the same pathway).
- A person whose connectomic biotype matches a TMS-responsive depression subtype receives a targeted recommendation, with the connectomic detail prepared for a clinician's review, to enable precise targeting of brain regions.

### Supportive

When reversal is not possible (or a negative outcome is imminent), supportive recommendations equip the person to cope, manage, or live well with the trajectory.

**Examples:**

- For people whose psychiatric symptoms are recurrent and not currently reversible, evidence-based skills (CBT, DBT, ACT) delivered through trusted partners or partner-built plug-ins, tailored to the specific symptom profile.
- For autistic individuals, skills training to recognize facial emotions or read social cues in the contexts they identify as challenging.
- For chronic-pain or fatigue trajectories, pacing strategies, energy-budget awareness, and matching to support communities of similar biotype.
- For people facing acute medical news, practical coping tools, decision-support resources, and matching to peer communities who have navigated similar trajectories.

## How recommendations are generated

The navigator's causal-recommendation engine, `SI-Causal-Recommendation`, due M42 in Y4. Per `02_Cytognosis_Phase1_Operational_Plan.md` `P3.O6`, the engine combines:

- **Causal inference layer** using do-calculus and structural causal models for proposed lifestyle and pharmacological actions, with counterfactual logging on every recommendation.
- **Delayed-reward reinforcement learning** using CATE (Conditional Average Treatment Effect) or equivalent uplift modeling. Reward signal is user-reported outcome on validated scales, with clinical-partner review.
- **Personalized prior** from the genome, distilled per-individual from a centralized genotypic FM, telling the engine which biology to focus on for this person.
- **Population-level evidence** from the open Cytoverse map: what works in general for this biotype.
- **Personal-history signal** from the long-term memory module: what has actually worked or not worked for this specific person.

The engine integrates all five into a navigation decision. The decision is presented to the user with explicit reasoning, not as an oracle.

## Safety envelope

Recommendation modes are not all equally safe to deliver autonomously. Safety envelopes:

| Recommendation type | Default behavior | Escalation path |
|---|---|---|
| Lifestyle (diet, exercise, sleep, social) | Direct recommendation | None unless user opts to share with clinician |
| Coping skills (CBT, DBT, ACT exercises) | Direct delivery | None |
| Behavioral interventions (consultation prompts, support-community matching) | Direct prompt | None |
| Medication adherence or timing within prescribed bounds | Direct prompt | Notifies clinician on consistent miss |
| Medication dose changes or new prescriptions | **Never autonomous** | Always routed through prescribing clinician via the Patient Care section of the app |
| Clinical-trial matching | Direct recommendation | Connects to the clinician or trial coordinator |
| Crisis indications | **Always escalates** | Hard-coded crisis-detection module (see `15_app_design.md` and `16_patient_safety_architecture.md`) |

This envelope is not a finished product. PAC reviews it annually; clinical advisors review it on every release.

## Why this is causal, not associational

A purely associational recommender ("people with this profile took action X and felt better") fails in two known ways: confounding (the action and the outcome may share an unmeasured cause) and counterfactual unavailability (the user wants to know what would happen specifically to them, not what happened on average).

The navigator addresses both by:

- using the Cytoverse map as a **mediator state** in a structural causal model. Interventions and genetic factors are causes; outcomes are effects; the map sits between them. With the mediator fixed in interpretation, counterfactual estimation is well-defined.
- using **delayed-reward reinforcement learning** that treats lifestyle and treatment changes as actions with lagged consequences, not instantaneous effects.
- using **conditional flow matching** (per `11_technical_track_FMs.md`) to generate counterfactual states that the engine can evaluate against, rather than relying solely on observed comparison groups.

This is harder than associational recommendation. It is also the only approach that can responsibly say "given your current state and history, this action has X probability of moving you toward your goal." The navigator never claims certainty; it always presents probability with uncertainty.

## Recommendation sources, transparency

Every recommendation surfaced to the user carries a transparent source:

- **Population evidence:** which study or trial supports this recommendation in general?
- **Personal history:** what in this user's recorded history backs this recommendation?
- **Genome / biotype:** what aspect of this user's biology makes this a personalized recommendation?
- **Confidence:** how confident is the engine in this recommendation, with uncertainty visible?
- **Counterfactual:** what would happen if the user did not follow this recommendation? (Where the engine has the data to estimate.)

Users can explore any recommendation's source. PAC reviews recommendation transparency at every annual release.

## Cross-references

- The Cytonome runtime that delivers these recommendations: `10_platform_architecture.md`, `15_app_design.md`.
- The privacy and safety architecture that gates how data flows: `16_patient_safety_architecture.md`.
- The technical FM stack that powers causal inference: `11_technical_track_FMs.md`.
- The PAC charter that holds the navigator accountable: `21_patient_advocacy_council.md`.






# Section: 15_app_design.md


# App Design: Cytonome User Experience

**Companion to:** `10_platform_architecture.md`, `13_sensor_ecosystem.md`, `14_navigation_recommendations.md`, `16_patient_safety_architecture.md`

The Cytonome app is the user-facing component of the platform for most users. This document captures the design principles, primary sections, and the loved-ones extension. Implementation specifics evolve; the structure here is the durable framing.

## Design principles

Five principles drive every product decision:

- **Edge-first.** Inference runs on-device. Raw data never leaves the device unless the user explicitly opts in to a specific kind of sharing. Detail in `16_patient_safety_architecture.md`.
- **Bidirectional.** The app is not a dashboard. It is a coach. It can speak with the user, listen, remember, and guide.
- **Time-aware.** A user's history is the substrate for personalization. Memory is structured, time-tagged, user-auditable.
- **User-controlled.** The user can see, edit, or delete any stored item. Sharing is opt-in and revocable.
- **Crisis-aware.** Crisis-detection is hard-coded and ships before any participant exposure. There is no version of the app that does not have it.

## Primary sections

![Diagram 1 from 15_app_design](/tmp/master_plan_compile/diagrams/15_app_design__1.png)


### Home: bidirectional guardian-coach

The default experience. Bidirectional voice-enabled communication with sub-500ms latency using a speech-to-speech model class (per `H1.P3.G4`). The coach:

- talks with the user every day, gathering mood and context (what they did, who they were with, how they slept, what they ate, what stressed or delighted them);
- helps plan the day given the user's goals, current state, and past patterns;
- offers motivation, reframing, and emotional support when appropriate;
- routes any crisis indication immediately to the crisis-detection module.

Long-term memory is structured. Every interaction creates time-tagged events stored on-device with user-visible content. Recall is searchable; users can edit or delete any event.

### Sensors

Where users add, configure, and audit their data sources. Three categories of sensors are configurable through the app:

**Instruments and tests.** Validated psychological and medical assessments delivered as in-app tools. PHQ-9, GAD-7, and the broader catalog of clinical scales for depression, anxiety, PTSD, attachment, personality, neurobehavioral function. These tools serve two roles: initial calibration and ongoing tracking. Each scale is mapped to the universal phenotypic axes (the 1500 to 2000 minimal-feature-set neurobehavioral axes Cytognosis is curating, per the Patty meeting), so the app can unify and complement different scales rather than treating each as a separate readout.

**Commercial devices.** Configuration for Apple Watch, Oura Ring, Whoop, Muse S Athena, Emotiv Insight, fNIRS partner headsets, and other UBAP-conformant devices. Each device is a plug-in (per `13_sensor_ecosystem.md`); add-and-go.

**Lab and clinic linking.** Connector to commercial labs (Quest, LabCorp), hospital labs, and the user's clinicians. Routine clinical labs flow into the app as structured data. Imaging centers can transmit DICOM directly. The user controls what flows where.

The sensor section is also where the **plug-in store** lives, with two tiers: an open community-maintained store and a Cytognosis-curated licensed store.

### Interventions

Repository of personalized interventions, prioritized and nominated to the unique biology and current health state of the user. Interventions are not necessarily FDA-approved; they are evidence-supported and matched to biotype.

Two broad categories:

**Non-invasive lifestyle.** Personalized diet plans, exercise plans, sleep schedules, social-routine recommendations. Each plan is tied to the user's biotype, observed responses, genotype, and goal.

**CBT, DBT, ACT and skills tools.** Interactive evidence-based skills, including pattern from CSAIL like "The Guardian" for depression, plus emerging tools as the field develops. Skills are biotype-matched: an autistic user practicing facial-emotion recognition gets different content from a person managing recurrent depression.

### Patient Care

Where the user connects with clinicians. Two flows:

- **Find a doctor.** Match users to clinicians based on the user's biology, biotype, and current state, given the clinician's specialties and approach.
- **Add an existing doctor.** Bring an existing clinician into the loop. Recommended personalized therapies (medications, treatments) can be shared with the clinician as a structured "treatment plan recommendation" that the clinician reviews, modifies, or rejects in their own workflow.

The app never bypasses clinicians. Recommended medications never auto-administer; they always go through a prescribing clinician.

### Clinical Trials

Where the user is matched to ongoing trials based on their biotype. Matching criteria are explicit (the user can see why a trial is recommended). Trials matched on biotype rather than only on diagnostic label improve trial efficacy and the user's chance of benefiting; this is the same logic that underpins precision oncology, applied to psychiatry and other domains.

### Patient Communities

Opt-in communities of users with similar biology. Not communities organized around diagnostic label (which collapses heterogeneity), but communities organized around biotype: people with shared mood-axis position, shared connectomic signature, shared autoimmune trajectory, etc.

This is a social network built on biology rather than self-declared identity. The match is opt-in and revocable; no biology data is shared in the community by default. The community is a place users go because they feel connected; the biotype match is the substrate that produces that connection.

## Loved-Ones extension

Each user can optionally add their loved ones, including children and pets, to be tracked alongside themselves in the same app. Each loved-one type is a distinct market with its own product surface but shares the underlying platform.

![Diagram 2 from 15_app_design](/tmp/master_plan_compile/diagrams/15_app_design__2.png)


### Kids

Children, especially infants, are simultaneously the most vulnerable population (because they cannot articulate pain or distress) and one of the highest-value early markets (because parents are highly motivated to track their children's health). Current monitoring is dominated by video devices integrated into health tracking; Cytonome's kid-mode integrates these plus developmental scales mapped to the phenotypic axes used for adults, plus parental observations entered through the conversational interface.

PAC has explicit input on kid-mode design. Privacy and consent for minors are governed by parental consent with developmental-age awareness; older children can be brought into the consent process directly as they mature.

### Pets

Pets, particularly dogs, have unusual data hygiene relative to human clinical data: clean genotyping is widely available; behavioral phenotyping is well-developed; many psychiatric manifestations map closely to human ones; consent is uncomplicated. The pet market is an opportunistic data source for early-platform validation and a sustainable product market in its own right.

Cytonome pet-mode connects to existing pet communities and datasets (which are largely open), provides comprehensive genotyping connectors, and uses behavioral phenotyping aligned with human axes where appropriate (cross-species mood and anxiety axes are an active research area).

### Cross-mode consistency

The same multimodal multiscale platform operates across all modes. The cellular and connectomic foundation models are species-aware (cross-species training where data permits; species-specific fine-tuning where required). Recommendations are mode-appropriate (a recommendation surface that fits a parent looking at their child is different from one that fits the child themselves).

## What the app does *not* do

A short list of explicit non-goals, because each was tempting and each would corrupt the platform:

- **It does not replace clinicians.** Recommendations route through clinicians where prescriptions are involved.
- **It does not gamify health into addiction.** The app's success is measured in user wellbeing, not engagement minutes. Engagement metrics are inputs to internal review, not optimization targets.
- **It does not sell data.** The Foundation does not sell user data. The PBC does not sell user data. The Helix Framework legally constrains both. The 23&me precedent (genotype data sold to therapeutics company under unclear consent) is the exact failure mode we engineer against.
- **It does not promise what it cannot deliver.** Every recommendation carries explicit uncertainty; counterfactuals are estimates, not predictions of what will definitely happen.
- **It does not handle untrained-LLM therapy substitution.** Crisis-detection module is hard-coded; the macro LLM does not pretend to be a therapist; it is a coach with a clearly defined scope and a clear escalation path.

## App-development bifurcation

Per the bifurcation rule, the app's components split:

- **Open (Foundation):** the on-device runtime, the macro LLM, the privacy architecture, the crisis-detection module, the structured memory module, the basic personalized-recommendation engine. All Apache 2.0 / open hardware specs / open protocols. Annual updates.
- **Proprietary (PBC, post-bifurcation):** the personalized causal model trained on the proprietary continuous-tracking dataset; the navigation policy informed by continuous tracking; the integrated regulated-product features needed for FDA clearance; the subscription business model.

Users get the open app for free with the open features. Users opt into PBC continuous tracking under a separate consent, with a separate price model (subscription, akin to OpenAI/Claude consumer plans but tied to health). The two layers are distinct in the user experience and in the legal architecture.

## Cross-references

- The four-tier compute that makes edge-first possible: `16_patient_safety_architecture.md`.
- The recommendation framework the app delivers: `14_navigation_recommendations.md`.
- The sensor ecosystem the Sensors section consumes: `13_sensor_ecosystem.md`.
- The PAC charter that reviews app design: `21_patient_advocacy_council.md`.
- The bifurcation rules that govern app components: `02_horizons_and_bifurcation.md`, `23_open_science_and_ip.md`.






# Section: 16_patient_safety_architecture.md


# Patient Safety Architecture: Four-Tier Compute and Privacy

**Companion to:** `10_platform_architecture.md`, `15_app_design.md`, `23_open_science_and_ip.md`
**Strategic Initiative:** `SI-Privacy-Architecture` (M12 deliverable; open protocol)

This document specifies the layered compute and privacy architecture that protects participants and users across the Cytognosis platform. The architecture is published as an open protocol with an Apache 2.0 reference implementation (per `H1.P3.G1`). External review by at least two qualified security researchers is a release gate.

## Why this exists in v2.0

Three concrete failure modes in adjacent products inform the architecture:

- **23andMe precedent.** Genotype data sold to therapeutics partners under consent forms that did not clearly communicate the use case to participants. Consent must be granular, machine-readable, revocable, and continuously visible to the user.
- **Therapy LLM precedent.** Sensitive therapeutic conversations sent to LLM backends without HIPAA-compliant infrastructure, plus reports of suicidal ideation in users of untrained LLMs as substitute therapy. Crisis-detection must be hard-coded; LLM scope must be bounded; therapy substitution is not a product mode we ship.
- **Harvest Now, Decrypt Later threat.** Quantum-computing emergence plus vulnerable storage practices produce a threat model where data captured today can be decrypted in a future where current cryptography fails. Storage must be post-quantum-safe end-to-end (NIST PQC compliant) by Y4 (`H1.P3.G7` `K5`).

## The four-tier compute architecture

![Diagram 1 from 16_patient_safety_architecture](/tmp/master_plan_compile/diagrams/16_patient_safety_architecture__1.png)


### Tier 1: Perception (phone)

The user's daily-driver device. Carries:

- the on-device LLM (Gemma-family or equivalent ≤3B parameters, quantized) for the macro phenotypic-axis quantification (`SI-Neuroverse-Macro-LLM`);
- the bidirectional voice interface using a speech-to-speech model class (Step-Audio-R1.1, Fish Audio S2 Pro, or successor; not three-stage STT→LLM→TTS pipelines, which lose paralinguistic cues);
- the hard-coded crisis-detection module that surfaces 988 Suicide and Crisis Lifeline plus Crisis Text Line on detection, with optional clinician alerting;
- the structured, time-tagged conversational memory store, user-auditable.

All inference here runs locally. Voice processing is local unless the user explicitly opts in to encrypted external processing for a specific request. The device is the smallest unit of trust, and it never sends raw audio or raw conversation to anything else by default.

### Tier 2: Local compute (personal node)

A dedicated local-compute appliance, running either on the user's existing hardware (laptop, desktop) or as a separately marketed Cytognosis device (analogous in form to Alexa-class home appliances but operating primarily offline with restricted, encrypted, anonymized communication outward).

This tier carries:

- the long-term semantic memory store, distinct from the on-device episodic memory, with the consolidation pipeline that promotes episodic events to semantic understanding;
- the causal recommendation engine that runs the heavier inference (`SI-Causal-Recommendation`);
- the sensor-aggregation layer that pulls UBAP-formatted streams from all of the user's sensors and fuses them into a unified state representation;
- the bridge to Tier 3, with explicit consent gating for what flows where.

The personal node is what makes the platform genuinely on-the-edge for users with non-trivial workloads. A user can run the full platform without the personal node (everything happens on the phone, with reduced model sizes); the personal node simply unlocks higher-fidelity recommendations.

### Tier 3: Distributed substrate (community)

A decentralized storage and federated-learning layer that does not give any single node access to a significant fraction of any user's data. The substrate adopts technologies from BitTorrent and blockchain-class consensus systems to provide redundancy and verifiability without centralization.

This tier:

- holds shards of users' encrypted data across many nodes, no single one of which can reconstruct meaningful state;
- runs federated learning over encrypted embeddings, with aggregation handled by a consensus protocol;
- enforces per-user differential-privacy budgets explicitly, with budget accounting visible to the user.

Tier 3 is the architectural answer to the question "how can a population of Cytognosis users improve the platform together without surrendering individual privacy?" The substrate is open-source, post-quantum-safe (NIST PQC compliant by Y4), and externally audited.

### Tier 4: Cytognosis layer (central)

The Foundation's central training and pattern-discovery infrastructure. Receives only:

- aggregated, consented embeddings (not raw data);
- DP-bounded summary statistics with explicit ε accounting;
- post-quantum-encrypted gradient updates from the federated-learning protocol.

Tier 4 produces:

- updated foundation models (Cytoverse, Cytoscope-relevant alignment models, Cytonome navigation models) that are released as open updates back to all tiers;
- cross-patient pattern discovery that informs new clinical hypotheses for the open Cytoverse map;
- post-bifurcation, the Foundation Tier 4 also coordinates with the PBC Tier 4 (a separate proprietary training cluster) for the proprietary navigation engine, with the bifurcation rule enforced at the data layer.

## Consent architecture

![Diagram 2 from 16_patient_safety_architecture](/tmp/master_plan_compile/diagrams/16_patient_safety_architecture__2.png)


Every data flow from Tier 1 outward is gated by an explicit, granular, machine-readable consent record:

- **Granular.** Consent is per data type, per purpose, per recipient. "Share my sleep data with the federated learning aggregation for the next 6 months" is a different consent than "share my sleep data with my clinician once."
- **Machine-readable.** UBAP-conformant consent metadata enforces consent automatically; no human in the runtime path.
- **Revocable.** The user can revoke at any time. Revocation propagates to derived-data deletion through the substrate (with technical limits: encrypted shards already in the substrate cannot always be re-collected, but their decryption keys can be destroyed, rendering them inaccessible).
- **Visible.** The user sees what they have consented to, in plain language, every time they open the app.
- **Defaulted to most-restrictive.** New data types and new purposes do not opt the user in by default. Affirmative re-consent is required.

PAC reviews the consent architecture at every annual release.

## Crisis-detection module

The crisis-detection module is the only mode in which the navigator is allowed to override user-controlled flows. It is hard-coded, ships before any participant exposure, and is reviewed by clinical advisors on every release.

Behavior on crisis detection:

- Surface 988 Suicide and Crisis Lifeline and Crisis Text Line in-app, in plain language, with one-tap call or message.
- If the user has opted in to clinician alerting, send a structured alert to the clinician with the minimum information needed for response.
- Log the detection event in the user's memory with a clear, non-stigmatizing description.
- Continue conversation in a supportive, non-clinical mode that does not pretend to be a therapist.

The detection threshold is intentionally biased toward over-detection: a false alarm is acceptable; a missed crisis is not. Clinical advisors set and review the threshold.

## Post-quantum substrate

By M48, every cryptographic primitive in persistent storage uses NIST PQC draft-compliant algorithms:

- **Key encapsulation:** CRYSTALS-Kyber (or successor as standardization evolves).
- **Signatures:** CRYSTALS-Dilithium (or successor).
- **Hash:** SHA-3 family.

The substrate has documented migration plans for each primitive (NIST is finalizing standards into Y2026; subsequent versions may change selections). External cryptographic audit passes before first external pilot uses the substrate.

This addresses the Harvest Now, Decrypt Later threat: data captured by adversaries today, even if undecryptable now, would become readable when quantum computing matures. Post-quantum storage means that an adversary intercepting Tier 3 traffic today still cannot decrypt it 20 years hence.

## Privacy probes

The release-checklist pipeline (`SI-Release-Pipeline`) gates every public release on:

- a **differential-privacy probe** that confirms claimed ε budgets hold against observed model behavior;
- a **re-identification probe** that confirms an adversary with population-scale auxiliary data cannot re-identify training participants from the released artifact.

Zero re-identification incidents on the public probe set is a Gate 1 criterion (`GC-G1.O4` adoption-and-impact).

## Cross-references

- The four-tier compute is the substrate the entire navigator depends on: `10_platform_architecture.md`.
- The app's user-facing privacy controls live in the consent architecture: `15_app_design.md`.
- The PAC's role in privacy review: `21_patient_advocacy_council.md`.
- The Helix legal architecture that enforces non-sale of data: `20_organization_helix.md`.
- The bifurcation rule that governs how proprietary continuous data is segregated: `02_horizons_and_bifurcation.md`.
- The full open-science substrate that ships these specs publicly: `23_open_science_and_ip.md`.






# Section: 20_organization_helix.md


# Organization and Helix Structure

**Companion to:** `21_patient_advocacy_council.md`, `22_people_and_consultants.md`, `23_open_science_and_ip.md`, `02_horizons_and_bifurcation.md`

This document captures the operating-model layer using the McKinsey 12-element overlay. Where the strategic plan elsewhere asks "what are we doing," this document answers "how are we organized to do it."

## The Helix structure

![Diagram 1 from 20_organization_helix](/tmp/master_plan_compile/diagrams/20_organization_helix__1.png)


The Helix is a federated structure with one parent (the Foundation) and two classes of children (the PBC subsidiary and, eventually, regional sister organizations). Each child is independently governed within constraints set by the Foundation through bylaws and license terms. The Foundation does not run product, but it cannot lose control of the open mission.

## McKinsey 12-element operating model

Maintained as a rolling lens. The twelve elements answer twelve operating questions; where the answer is "not yet documented," the absence is itself a planning decision flagged for the next annual review.

### Purpose

To pioneer a cellular intelligence platform that maps personalized health states, detecting and intercepting disease years before symptoms emerge. Codified in the Vision and Mission. Not subject to change without Bylaws amendment.

### Value agenda

The bridge between mission and business model. For Cytognosis:

- **Foundation value:** maintaining open precision-health infrastructure as a public good in perpetuity, funded by grants, philanthropy, and PBC royalties.
- **PBC value:** continuous personalized health monitoring and navigation as a regulated product, funded by subscription revenue and VC, with royalty back to the Foundation.

The Helix is precisely how the value agenda survives the tension between these two halves.

### Structure

Documented above. Foundation parent, PBC subsidiary post-Gate 1, regional sister orgs in H3 line of sight.

### Ecosystem

Strategic relationships beyond the entity:

| Type | Partners |
|---|---|
| Funders (active) | Astera Institute, Google.org, Foresight Institute (rejected), EA Fund |
| Funders (target) | ARPA-H (PHO and HSF), NSF (Tech Labs), Convergent Research, Wellcome Leap, CZI, NIH |
| Clinical | McLean Hospital (Brad Ruzicka), Mount Sinai, University of Manchester (Madhvi Menon, autoimmune) |
| Scientific | PsychENCODE, NeuroBioBank, ENIGMA consortium, HiTOP community, Grotzinger group, ROSMAP |
| Technology | ARPA-H Delphi (programmable biosensors), Caltech molecular monitoring FRO, Hugging Face (open releases), Voltage Park / GCP / cloud compute |
| Standards | LinkML/BioLink, RO-Crate, SPDX, W3C Web Annotation, NIST PQC working group, future submissions to IEEE / ISO / HL7 |
| Counsel and audit | Duane Valz (legal), Salus IRB and/or Northstar IRB, external security researchers (cryptographic audit) |

### Leadership

| Role | Y1-Y2 | Y3-Y5 | Y5+ |
|---|---|---|---|
| CEO | Mohammadi | Mohammadi | Mohammadi or split with PBC CEO at Gate 1 |
| CSO | Mohammadi (acting) | First CSO hire | Dedicated CSO |
| CTO | Mohammadi (acting) + Engineering lead hire | Dedicated CTO | Dedicated CTO |
| Head of Clinical / Regulatory | None | Hire by Y3 Q2 | Dedicated head |
| UK lead | Menon-style affiliate or first UK hire by Y2 | Dedicated UK CEO or Country Director | Per UK structure |
| PBC CEO | n/a | n/a | Hire at Gate 1 if not Mohammadi |

### Governance

Foundation Board: at least three external directors by M24 (`H1.P6.G1` `K1`). Bylaws Article VI covers IP, Article XI covers PBC governance, Article XIII covers dissolution provisions. PBC Board, post-activation, has Foundation-controlled governance majority.

Patient Advocacy Council is a governance entity, not advisory, with binding rights at the bifurcation gate and on study design, release timing, and grant prioritization. Charter detail in `21_patient_advocacy_council.md`.

Scientific Advisory Board (5 to 7 members, in place by M6) advises on platform technical direction; not binding.

Lived Experience Advisory Council (8 to 12 members, in place by M18) advises on study design and accessibility; not binding.

### Processes

The processes catalog (drafted across `01_..` to `41_..` documents in this plan) covers:

- annual planning catch-ball (October);
- quarterly OKR review;
- monthly cross-pillar sync;
- weekly initiative standups;
- bidirectional connection between Strategic Initiatives and the Monday workspace;
- release pipeline (`SI-Release-Pipeline`) with the gated checklist;
- bifurcation enforcement (`SI-OpenScience-Template` plus the bifurcation tagging in Monday);
- PAC review on every grant submission and major release;
- annual environment scan (SWOT, PESTLE, VRIO).

### Technology

The platform itself: Cytoverse, Cytoscope, Cytonome, plus the open-science substrate. Detail in `10_platform_architecture.md`. The choice of computing infrastructure (compute, storage, federated learning) is documented in `16_patient_safety_architecture.md`.

### Behaviors

- Active voice, direct communication.
- Open-by-default unless the bifurcation rule says otherwise.
- Failure documented as deliverable; no silent retreats.
- Every public artifact passes the release checklist.
- Every participant-facing decision routes through PAC.
- No em dashes, no forbidden words, no passive voice, no hardcoded section numbers (formatting and brand bans codified across the skills system).
- Every grant proposal references prior corrections and validated approaches; no reinvention of guidance the team has already settled.

### Rewards

Compensation has three components, by phase:

| Phase | Foundation comp | PBC comp |
|---|---|---|
| Pre-Gate 1 | Salary at Foundation level (intern, junior, senior bands per `budget_role_levels.md`); promise-of-future-equity for founding team and early hires (legally vetted, IRS-aware) | n/a |
| Gate 1 onward | Salary at Foundation level continues for Foundation roles | PBC equity (real, vested) for PBC roles; Foundation roles can also vest into PBC equity per Helix terms |
| H3 | Foundation salaries continue; regional sister orgs operate on regional comp norms with Foundation-funded subsidies where appropriate | n/a |

The promise-of-future-equity mechanism is the structural alignment between mission-driven Foundation work today and economic value capture at Gate 1. Without it, talent drifts toward straight startups. With it, mission-driven talent that takes Foundation-level salary in H1 has a documented path to economic upside through PBC equity in H2.

### Footprint

| Phase | US HQ | UK office | Other |
|---|---|---|---|
| Y1 | South San Francisco (small office or co-working) | None | Remote-first |
| Y2 | SSF (lease step-up) | Manchester (lease) | Remote-first |
| Y3-Y5 | SSF (full HQ) | Manchester (full office) | Remote-first plus partner-hosted seats |
| H2 | SSF expanded (PBC engineering) | Manchester expanded | Regional scoping engagements |
| H3 | Coordinator role at SSF | Peer regional org | 3 to 5 sister orgs |

Footprint is intentionally modest at the central level. The federation in H3 distributes capacity rather than concentrating it.

### Talent

Hiring trajectory in `01_Cytognosis_Strategic_Roadmap_15-Year.md` Section 8 and refreshed here:

| Phase | US HQ FTE | UK FTE | Total |
|---|---|---|---|
| End Y1 | 5 to 8 | 0 to 1 | 5 to 9 |
| End Y3 | 10 to 14 | 3 to 5 | 13 to 19 |
| End Y5 | 15 to 25 | 5 to 10 | 20 to 35 |
| End Y10 | 50 to 100 (incl. PBC) | 20 to 40 | 70 to 140 |
| End Y15 | Coordinator role | Peer regional org | Federation |

Cross-scale expertise (people who can work across micro / meso / macro biological scales) is rare. The affiliate-first model lets us collaborate with the right people without insisting on relocation; the UK office expands the talent pool. The Science / Engineering pairing on every major initiative spreads the load across people who do not need to be unicorns.

## Where this connects

- The PAC charter that sits inside this operating model: `21_patient_advocacy_council.md`.
- Named consultants and rates: `22_people_and_consultants.md`.
- IP and openness rules that constrain the Helix: `23_open_science_and_ip.md`.
- The bifurcation rule that the Helix exists to make tractable: `02_horizons_and_bifurcation.md`.
- Funding strategy across the Helix: `30_funding_strategy.md`.






# Section: 21_patient_advocacy_council.md


# Patient Advocacy Council (PAC)

**Companion to:** `20_organization_helix.md`, `02_horizons_and_bifurcation.md`, `15_app_design.md`
**Subtrack:** T14 (new in v2.0) under M4 Organization

The Patient Advocacy Council is the governance innovation Cytognosis introduced in the Google.org Impact proposal and now formalizes as a first-class organizational design. PAC is **not advisory**. It holds binding decision rights on participant-impacting decisions and exists to make the Foundation's commitment to the *Care* value operational rather than rhetorical.

## Why PAC exists

Every prior attempt at participant-centered health technology has put participants on advisory committees with no veto. The result is predictable: when scientific or commercial pressure conflicts with participant interest, scientific or commercial pressure wins, and the participants on the committee are heard but not heeded.

PAC closes that loop. It is structurally analogous to the role an ethics board plays in pharmaceutical research, but extended to the full lifecycle of a continuous health platform: study design, release timing, the bifurcation boundary, IP decisions that affect participants, app surface decisions, and grant prioritization where participant interest is at stake.

## Charter scope (binding rights)

PAC has binding rights on:

- **Study design.** Any participant-facing study (Phase 0, external pilot, the Year 4-Year 5 clinical trial, post-bifurcation cohort studies) requires PAC review and approval before IRB submission.
- **Release timing.** PAC reviews proposed release pace for participant-impacting artifacts. Releasing too fast (before adequate validation) or too slow (withholding benefit) is contestable.
- **The bifurcation boundary.** PAC reviews and approves the specific data, models, and analyses that move from open to proprietary at the 36-month bifurcation. PAC has binding sign-off on the bifurcation policy as ratified by the Foundation Board.
- **Consent architecture.** PAC reviews proposed consent forms, the structure of granular consent, and the runtime enforcement architecture. Changes to default settings require PAC approval.
- **App surface decisions.** Material changes to app design that affect participant experience (e.g., crisis-detection module updates, new sensor categories surfaced, recommendation modes changed) require PAC review.
- **Grant prioritization.** PAC reviews the grant pipeline annually and can flag grant opportunities that conflict with participant interest. The Foundation Board considers PAC flags but retains final grant-acceptance authority.

PAC does not have binding rights on technical architecture, scientific methodology, or business model decisions that do not affect participants directly. Those remain with the relevant scientific, technical, or operational leadership.

## Charter scope (advisory rights)

In addition to binding rights, PAC has advisory voice on:

- platform direction;
- prioritization of indications and biotypes;
- partnership decisions where participant interest is implicated but not central;
- communications and messaging that involve participant stories.

## Composition

| Phase | Size | Geographic mix | Indication mix |
|---|---|---|---|
| Founding (M12) | 6 to 9 members | US-anchored, with 1 to 2 UK seats | Mental health primary (MDD, GAD, PTSD, BD, SZ); 1 to 2 cross-domain (autoimmune, neurodegen) |
| Y3-Y5 | 9 to 12 members | US plus UK plus 1 international | Expanded indication mix as platform expands |
| H2 | 12 to 15 members | Multi-continental | All currently active indications |
| H3 | 15+ in federation structure | One PAC seat per region per active indication; central council coordinates regional councils | Full federation |

Selection criteria:

- lived experience with the indication;
- demonstrated capacity for collaborative decision-making in adversarial moments;
- diversity across age, gender, race, geography, socioeconomic status;
- no conflict of interest with Cytognosis funders or the PBC;
- compensated time at fair-market rates (not token gestures).

## Operating model

![Diagram 1 from 21_patient_advocacy_council](/tmp/master_plan_compile/diagrams/21_patient_advocacy_council__1.png)


PAC meets quarterly at minimum, with ad-hoc reviews triggered by specific decision needs (e.g., before a study IRB submission, before a major release, before a bifurcation policy change).

PAC has direct access to the Foundation Board for escalation. Disagreement between PAC and operational leadership is resolved by the Foundation Board, with the PAC position presented in writing.

## Distinction from LEAC

The Lived Experience Advisory Council (LEAC, established in v1.1 of the strategic roadmap) is **advisory**: it provides input on study design and accessibility but does not have binding rights. LEAC is broader (8 to 12 members, more diverse mix), meets quarterly, and influences specific releases.

PAC is narrower, more selectively composed for governance-grade work, has binding rights, and meets more often when needed. Membership may overlap (a person can sit on both), but the bodies are distinct in role.

LEAC continues to exist after PAC stands up. The two complement each other: LEAC for breadth of input, PAC for depth of governance.

## Compensation

PAC members are compensated at rates appropriate to the time and skill demanded:

- quarterly meetings paid as professional consulting time (rate per market);
- ad-hoc reviews paid hourly;
- travel and accessibility costs covered by the Foundation;
- term limits with renewable terms (default: 3-year terms, renewable once).

PAC compensation is included in the operating budget from Y1 and tracked in the Phase 1 funding plan (`SI-Phase1-Funding`).

## PAC at the bifurcation gate

The bifurcation event at M37 is PAC's most consequential moment in H1. PAC must:

- review the proposed bifurcation boundary in detail (which data, models, and analyses move into the PBC; which stay in the Foundation);
- confirm or amend the boundary;
- approve the participant consent forms for the proprietary clinical study;
- ratify the open release commitments that the Foundation makes for the post-bifurcation period.

PAC has binding sign-off here. If PAC does not approve, the Foundation Board cannot ratify the bifurcation. This is the strongest governance moment in the Helix and is what makes the bifurcation legitimate to participants and to funders.

## Charter ratification timeline

| Milestone | Target | Status |
|---|---|---|
| Charter drafted | M6 (Y1 Q3) | Pending |
| Counsel review | M9 | Pending |
| Foundation Board review and approval | M10 | Pending |
| First seat recruitment opens | M11 | Pending |
| First seats filled, charter binding | M12 | Pending |
| First quarterly meeting | M13 | Pending |
| Two complete review cycles (G1 prerequisite) | M24 | Pending |
| First binding-rights exercise on a real decision (G1 criterion `GC-G1.P2`) | by M30 | Target |

## Risks specific to PAC

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| PAC and operational leadership reach genuine deadlock | Medium | High | Escalation to Foundation Board with both positions; pre-committed timeboxing on resolution |
| PAC drifts toward operational micromanagement | Medium | Medium | Clear charter scope; quarterly review of charter scope; PAC self-discipline |
| PAC becomes captured by single sub-population | Medium | Medium | Composition criteria with explicit diversity targets; rotating chair role; term limits |
| PAC compensation creates conflict-of-interest | Low | High | Standard COI disclosure framework; market-rate not above-market compensation |
| PAC delays critical decisions | Medium | Medium | Pre-set decision SLAs (e.g., 14 days for routine review); ad-hoc emergency convening capacity |
| Conflict-of-interest with funders | Medium | High | Members do not have material funding ties to Cytognosis funders; conflict disclosure framework |

## Cross-references

- The Helix structure that PAC sits inside: `20_organization_helix.md`.
- The bifurcation gate where PAC has binding sign-off: `02_horizons_and_bifurcation.md`.
- The privacy and consent architecture PAC reviews: `16_patient_safety_architecture.md`.
- The app design PAC reviews materially: `15_app_design.md`.
- The grant pipeline PAC reviews annually: `30_funding_strategy.md`.






# Section: 22_people_and_consultants.md


# People and Consultants

**Companion to:** `20_organization_helix.md`, `30_funding_strategy.md`

This document captures the team, named consultants and rates, and the hiring trajectory across the next 24 months. Detail-level planning is in the operational plan (`02_Cytognosis_Phase1_Operational_Plan.md`); this document carries the strategic narrative on people decisions.

## Founding team

| Role | Person | Role detail |
|---|---|---|
| Founder, CEO, Acting CSO, Acting CTO | Shahin Mohammadi | 20 years computational biology (MIT, Broad Institute, insitro, GenBio AI); the platform is built on this expertise |

The Foundation operates with a lean founding team in Y1. CEO doubles as CSO and CTO until those roles are formally hired. The first material role hires (per `01_Cytognosis_Strategic_Roadmap_15-Year.md` Section 8) target Y1 Q2 to Q4.

## Named consultants and rates

These are the consultants under engagement or under negotiation. Rates are documented per the canonical `key_consultants.md` memory; do not vary without explicit approval.

| Consultant | Role | Rate | Engagement |
|---|---|---|---|
| **Duane Valz** | Legal counsel (Foundation, IP, Helix, PBC) | $500/hr | Active. Note: NOT Duane Morris (the firm). |
| **Patricia Purcell, PhD** | Grants and communications consultant | ~$150/hr base; ~$300/hr for proposal-density work like Astera | Active. New: ~8 hr/wk against the Astera proposal at $300/hr; included in the proposal budget (per Patty meeting 2026-05-08). Anticipated continuing role through Y1-Y2 grant cycle. |
| **Brad Ruzicka, MD** | Clinical lead at McLean Hospital | Subaward through McLean | Active. McLean subaward via the joint study including IRB and clinical infrastructure work. |
| **Jose Davila-Velderrain, PhD** | Cross-scale neuro lead | Subaward through Human Technopole or via Google.org Impact | Active. Lead on connectomic FM, paired-data integration, ENIGMA integration. |
| **Ananth Grama, PhD** | Computational lead at Purdue IPAI | Subaward through Purdue, via Google.org Impact | Active. Faculty supervisor for Shourya Verma; co-PI on parallel cellular and connectomic FM work; offered to cover Mohammadi's Purdue visit travel. |
| **Salus IRB** | Independent IRB for clinical work | ~$15K | Active for retrospective IRB. Northstar IRB also under evaluation (per Patty meeting). |

## Active research staff

| Person | Role | Affiliation | Engagement |
|---|---|---|---|
| **Shourya Verma** | Lead RA on cellular and connectomic foundation models | Purdue IPAI | Active. Per 2026-05-07 meeting, leading both connectomic and cellular tracks (Mango is starting at Meta and is bandwidth-limited). Plans to start a separate product company with Grama in summer; Cytognosis engagement remains intact. |
| **Mango Wang** | Cellular FM contributor | Purdue / Meta | Active as bandwidth allows. Contributing to cellular track. |
| **Madhvi Menon, PhD** | UK autoimmune lead | University of Manchester | Active. Lead on Immunoverse v1; anchors UK office geographically. |

## Y1-Y2 hiring priorities

In rough priority order for Y1, refined per Phase 1 OKRs and grant-driven funding:

| Hire | Earliest target | Notes |
|---|---|---|
| AI/ML Engineer 1 (cellular FM) | Y1 Q2 | Pair with Mohammadi on `SI-Neuroverse-Micro` |
| Platform Engineer | Y1 Q2 | `SI-OpenScience-Template`, `SI-Release-Pipeline`, dev infrastructure |
| ML Engineer (macro LLM, Cytonome) | Y1 Q3 | `SI-Neuroverse-Macro-LLM`, `SI-Cytonome-v0.1` |
| Mobile Engineer | Y1 Q4 or Y2 Q1 | Cytonome v0.1 on iOS and Android |
| AI/ML Engineer 2 (connectomic FM) | Y2 Q1 | Davila-Velderrain pairing, `SI-Neuroverse-Meso` |
| First UK FTE | Y2 Q1 | Manchester-anchored, autoimmune-track |
| Clinical / Regulatory lead | Y2 Q3 | Manage IRB, FDA pre-sub track, study coordination |
| Privacy engineer (contracted then full-time) | Y1 ongoing | `SI-Privacy-Architecture` reference implementation |
| Grants and operations | Y1 Q3 | Compensation rate per `personnel_rate_cards` Monday board |

## Affiliate-first hiring model

Cross-scale expertise is rare. Forcing relocation makes hiring harder. The affiliate model lets us collaborate with the right people without insisting on relocation:

- subawards through partner institutions (Purdue IPAI, McLean, Mount Sinai, Manchester, Human Technopole) for senior collaborators who hold their primary appointment elsewhere;
- contractor engagements at well-defined rates for specific deliverables;
- promise-of-future-equity for full-time founding hires who take Foundation salary in exchange for upside at Gate 1;
- UK office as a second center of gravity for hiring outside the Bay Area.

## Compensation philosophy

Per `budget_role_levels.md` and the operating-model rewards element:

- **Foundation salaries** sit in non-profit-research bands. Senior research staff salary is below comparable private-industry pay. Promise-of-future-equity bridges the gap for founding-team and early hires.
- **Intern and junior bands.** Clinical Data Scientist ($75K) and Computational Neuroscientist ($70K) titles are intern-level despite the industry-aligned wording. Do not flag as under-market.
- **Senior hires (CTO, CSO, regulatory lead, head of clinical).** Compete on mission plus equity promise plus reasonable salary. Foundation comp benchmarked against precision-health nonprofits and FROs, not for-profit healthtech.
- **PBC hires from Gate 1 onward.** Comped on equity-bearing terms competitive with for-profit precision-health; promise-of-future-equity from Foundation roles vests into PBC equity per Helix terms.

## Relationship with academic affiliates

Several of our key consultants have primary academic appointments. Conflict-of-interest is managed:

- subaward agreements specify deliverable scope, IP terms, and publication policy;
- Cytognosis-funded work is acknowledged in resulting publications per Astera Open Science Policy;
- IP arising from subawards is licensed back to the Foundation per the subaward template;
- the Helix Framework allows academic affiliates to hold roles in both worlds without forcing a binary choice.

## What the Patty meeting changed

The 2026-05-08 strategic-development meeting with Patty Purcell:

- formalized Patty's consulting role on the Astera proposal at ~$300/hr for ~8 hr/wk;
- included Patty's compensation in the Astera budget for early payment (rather than absorbing into operations);
- confirmed Patty's continuing role into the Y1-Y2 grant cycle, with anticipated transition out as the in-house grants and operations capacity grows;
- aligned on the Astera and Google.org tone and emphasis for the proposal narrative.

## What the Shourya meeting changed

The 2026-05-07 cell-state / perturbation-modeling meeting with the Purdue team:

- shifted Shourya's role from "lead on connectomics" to "lead on connectomics and cellular," given Mango's Meta start;
- confirmed Mohammadi as the primary advisor on the cellular track despite less hands-on experience with connectomics;
- planned a Mohammadi visit to Purdue at end of May or early June 2026 to white-board three-to-six-month milestones;
- confirmed Grama as the on-paper supervisor at Purdue and primary subaward channel.

## Cross-references

- The Helix structure that holds these roles: `20_organization_helix.md`.
- The PAC governance role and compensation: `21_patient_advocacy_council.md`.
- The funding strategy that pays for hiring: `30_funding_strategy.md`.
- The technical track that Shourya leads: `11_technical_track_FMs.md`.






# Section: 23_open_science_and_ip.md


# Open Science and IP Strategy

**Companion to:** `02_horizons_and_bifurcation.md`, `20_organization_helix.md`, `21_patient_advocacy_council.md`

The Cytognosis open-science and IP strategy is straightforward in principle and disciplined in operation. The principle: open by default; the bifurcation is the only structured exception. The discipline: every artifact carries explicit license terms, every license is enforced through the release pipeline, and every closed component traces to a documented mission-protective rationale.

## License defaults

| Artifact type | Default license | Rationale |
|---|---|---|
| Code | Apache 2.0 | Permits commercial reuse with attribution; compatible with PBC subsidiary use; trademark protection |
| Trained model weights | Apache 2.0 (when source data permits); OpenRAIL-M when responsible-AI considerations apply | Maximum reuse with responsibility gates where appropriate |
| Documentation, papers, blog content | CC BY 4.0 | Citation-required; commercial reuse permitted |
| Derived datasets | CC0 where source licenses permit; CC BY 4.0 otherwise; controlled access for sensitive participant data | Maximize utility; protect participants where required |
| Schemas, ontologies, standards | CC0 | Standards must travel without barriers |
| UBAP specification | Apache 2.0 reference implementation; CC BY 4.0 spec text | Encourages adoption; no friction on conformance |
| Hardware designs (where Cytognosis-funded) | CERN OHL-S v2 or per partnership terms | Open hardware where we have the IP; partner terms otherwise |
| Conformance test suites | Apache 2.0 | Vendors must be able to self-certify without legal friction |

The list of source licenses we have to consider is in `funder_metadata.md` and the canonical-template-system reference docs.

## FAIR principles

Every public release passes FAIR (Findable, Accessible, Interoperable, Reusable) compliance:

- **Findable.** Stable identifiers (DOI via Zenodo or DataCite), rich metadata, indexed in registries (Hugging Face for models, Zenodo for archive, GitHub for code).
- **Accessible.** Standard protocols (HTTPS, S3 with signed URLs, IPFS for the substrate), open or controlled-access with documented access procedures.
- **Interoperable.** Linked Data principles, ontology-grounded metadata (UBERON, CHEBI, NBO, MONDO, SNOMED CT, ICD-11 as appropriate), schema-validated.
- **Reusable.** Provenance documented through RO-Crate, model cards, data cards, eval cards. Licenses unambiguous in machine-readable SPDX form.

The release pipeline (`SI-Release-Pipeline`, M12 deliverable) gates every public release on FAIR compliance plus differential-privacy and re-identification probes.

## The 36-month bifurcation rule, in licensing terms

Per `02_horizons_and_bifurcation.md`, the bifurcation is the single structured exception to open-by-default. In licensing terms:

![Diagram 1 from 23_open_science_and_ip](/tmp/master_plan_compile/diagrams/23_open_science_and_ip__1.png)


The PBC subsidiary, post-activation, holds defined IP in the proprietary categories and pays the Foundation:

- a perpetual open license for the open-track components;
- a royalty stream documented in the PBC charter and IP-licensing terms (`SI-PBC-Charter`, M30 deliverable);
- a non-revocable commitment that ensures the Foundation's open mission is not rescinded by PBC business decisions.

These terms protect against the failure mode where a successor organization takes the proprietary track in a direction that closes the open mission. The Foundation always holds enough governance and license rights to keep the map perpetually open.

## What "open" means concretely

A common failure mode in open-science policy is to declare "open" without operationalizing it. We operationalize:

- **Versioned releases.** Every release has a stable identifier and is preserved in archive (Zenodo) so that future researchers can reproduce results against the exact artifact used.
- **No "open soon."** If an artifact is not yet open, it is private; we do not promise future openness as a commitment we cannot enforce.
- **No backsliding.** Once an artifact is released open, it stays open. Even if a future Cytognosis decides differently, the existing artifact's existing license travels with the artifact in perpetuity.
- **Annual public review.** Every artifact's continued openness is reviewed annually as part of the Hoshin catch-ball; PAC participates.
- **Reproducibility.** Model card, data card, eval card on every release, plus a reproduction kit (Copier-template-bootstrapped) that anyone can run.
- **Equity.** Equity gates on every alignment-model release (per `12_clinical_to_wearable.md`).
- **Documentation as deliverable.** The Helix Framework paper, the UBAP specification, and the open-science substrate documentation are themselves public deliverables (`SI-Helix-Paper`, `SI-UBAP-v1`, `SI-OpenScience-Template`).

## The Astera Open Science Policy and similar instruments

Astera Institute (a primary funder for the open work in Y1-Y2) has an explicit Open Science Policy. We comply by default. Other funders with similar policies (Convergent Research, Speculative Technologies, EA Fund, Wellcome, Gates) align with our defaults. Federal funders (ARPA-H, NSF, NIH) have their own data-management-plan (DMP) requirements; we satisfy them while preserving our higher openness defaults wherever possible.

The grant-template canonical system (`canonical_template_system` memory) handles funder-specific licensing nuance per proposal; the master defaults above are the starting position.

## Trademark

"Cytognosis" and "Cytoverse," "Cytoscope," "Cytonome" are trademarks of Cytognosis Foundation. Trademark registration is in process (ongoing with counsel). Apache 2.0 license on code does not transfer the trademark; use of the marks requires separate approval. This is the standard approach for protecting brand without restricting code reuse.

## IP licensing to the PBC

Per Bylaws Article VI and the `SI-PBC-Charter` work product (M30):

- Foundation holds and retains all IP arising from Foundation-funded work pre-Gate 1.
- PBC at activation receives a royalty-bearing perpetual non-exclusive license to use Foundation IP in commercial products, with explicit field-of-use definitions.
- IP arising from PBC-funded work post-Gate 1 belongs to the PBC.
- The Foundation has perpetual non-revocable rights to use any Foundation-funded IP in the open mission, regardless of PBC commercial choices.
- Audit and dispute resolution mechanisms specified in PBC charter.

Counsel review (Duane Valz) is required before any IP-licensing terms are approved by the Board. Counsel review is also required before the PBC is activated. PAC has binding sign-off on the bifurcation that establishes which assets fall under which side of the line.

## Patents

Cytognosis does not seek defensive patents on Foundation-developed methods or models. Open releases plus prior-art creation provide stronger protection against later patenting by adversaries than defensive patents do for an open-mission organization. The PBC may pursue patents on hardware designs and product-specific innovations where doing so protects a market position; the Foundation's open releases serve as prior art preventing those patents from blocking foundational research.

## How this connects to grant strategy

The open-science posture is a competitive advantage with primary funders:

- Astera, Convergent Research, Speculative Technologies, EA Fund: open-by-default is their thesis. We are aligned by default.
- Google.org, philanthropic AI-for-science: open releases against time-bound milestones map cleanly to their funding instrument.
- ARPA-H, DOE, NSF, NIH: federal funders want public benefit; open releases satisfy that explicitly.
- Wellcome Leap, EU Horizon, regional foundations: open across geographies is exactly what they require.

The bifurcation itself is also a positive feature for funders: it gives them a credible answer to "how does this scale beyond your grant?" The PBC at Gate 1 is the answer, and they did not have to fund it.

## Cross-references

- The bifurcation rule itself: `02_horizons_and_bifurcation.md`.
- Helix legal architecture and PBC charter timeline: `20_organization_helix.md`.
- PAC governance role at the bifurcation: `21_patient_advocacy_council.md`.
- Funding strategy that aligns with this open posture: `30_funding_strategy.md`.
- The release-pipeline tooling that enforces FAIR and license compliance: `11_technical_track_FMs.md` (release-checklist CI).






# Section: 30_funding_strategy.md


# Funding Strategy

**Companion to:** `20_organization_helix.md`, `02_horizons_and_bifurcation.md`, `40_milestones_and_kpis.md`

The Cytognosis Foundation funding strategy is a portfolio across three categories: active grants, planned grants, and the post-Gate-1 PBC capital. The portfolio is structured so no single source determines whether the mission survives, and so the dual nature of the open Cytoverse map and the proprietary tracking layer maps cleanly to funder types.

## The portfolio at a glance

![Diagram 1 from 30_funding_strategy](/tmp/master_plan_compile/diagrams/30_funding_strategy__1.png)


## Active grants (as of compilation)

| Grant | Amount | Status | Notes |
|---|---|---|---|
| Astera Residency (Fall 2026) | $200K to $1.25M | In review (Round 2 v13 draft) | Patty consulting at $300/hr included in budget; due Sunday 2026-05-10 |
| Google.org AI for Science Impact Challenge | $2.2M | Submitted 2026-04-17 | Awaiting decision; estimated 2,000+ submissions |

## Recent decisions

| Grant | Outcome | Notes |
|---|---|---|
| Foresight AI for Safety | Rejected | Decision documented; Foresight milestones marked NOT EXECUTED in Monday |
| Y Combinator Winter 2025 | Rejected | Early-stage application |
| Y Combinator Spring 2026 | Rejected | Repeat application; non-priority going forward |

## In preparation (planned grants for Y1 to Y5)

Per the funding pipeline maintained in Monday's `Funding Opportunities` board (71 tracked opportunities) and `Grants Pipeline` board (19 active applications):

| Opportunity | Target | Stage | Strategic role |
|---|---|---|---|
| **ARPA-H PHO** | $50M+ | Planning; LOI target Y3 Q1 | Clinical-scale follow-on; powers Y4-Y5 trial |
| **NSF Tech Labs** | $15M | Pending RFP | Cytoverse map at clinical-grade scale |
| **Convergent Research FRO** | $50M | In preparation | Multi-year research-organization scale |
| **Wellcome Leap** | $8M | Planned | UK autoimmune track via Manchester partnership |
| **CZI** | $5M | Planned | Open-science alignment |
| **EA Fund** | $250K to $500K | Planned | Bridge / runway; mission-aligned |
| **Brains Accelerator** | Cohort position | Applied | Helix design refinement |
| **NIH R01 (Mohammadi as PI)** | $2-3M over 5 years | Planned | Standard mechanism for psychiatric biotyping work |
| **Gates Foundation** | TBD | Long-term planned | LMIC pilot; H2-H3 line of sight |
| **Wellcome Trust** | TBD | Long-term planned | UK ecosystem deepening |

## Funding pattern by horizon

### H1 (Years 1 to 5)

Target raise: **$30 to 50M non-dilutive over H1.**

| Year | Target (low-high) | Primary sources |
|---|---|---|
| Y1 | $3 to 5M | Astera Residency (if awarded) + Google.org Impact (if awarded) + EA Fund + early ARPA-H planning grants + first philanthropic partners + personal runway |
| Y2 | $5 to 8M | Google.org Impact milestones + EA Fund + early ARPA-H planning grants + first philanthropic partners |
| Y3 | $8 to 12M | ARPA-H PHO planning grant + NSF Tech Labs (if awarded) + NIH R01 resubmission + continuing philanthropic + first UK grant |
| Y4 | $8 to 15M | Clinical-scale ARPA-H + NIH R01 + Wellcome Leap (if applicable) + UK MRC + first Wellcome Trust |
| Y5 | $5 to 10M | Bridge to PBC activation + continuing philanthropic |

### Gate 1 (Year 5)

Foundation continues non-dilutive. **PBC raises VC** under terms that:

- preserve Foundation governance majority on PBC Board;
- include royalty terms documented in PBC charter;
- target Series A equivalent of $25 to 50M to fund the proprietary clinical study scale-up and the regulated-product engineering;
- preserve Helix structural alignment via Bylaws Article XI provisions.

### H2 (Years 5 to 10)

Target: **$75 to 150M combined** across Foundation and PBC.

- **Foundation continues** non-dilutive at $5 to 15M annually.
- **PBC** raises VC progressively (Series A, B, C); targets break-even or near-break-even by Year 10.
- **Royalty stream** from PBC to Foundation becomes material by Y8.

### H3 (Years 10 to 15)

Primarily revenue from the PBC plus regional philanthropic partners (Gates, Wellcome, regional foundations) funding emerging-market access. Foundation remains non-profit and mission-locked.

## Funder strategic roles

The portfolio is composed so different funders match different strategic needs:

| Strategic role | Best-fit funders |
|---|---|
| Open R&D, mission-aligned, multi-year | Astera, Convergent Research, Speculative Technologies, EA Fund |
| AI-for-science, time-bound milestones | Google.org Impact, foundation AI programs |
| Clinical-scale validation | ARPA-H PHO, NIH R01, NSF Tech Labs |
| UK and EU expansion | Wellcome Leap, Wellcome Trust, UKRI, MRC, Horizon Europe |
| Equity and emerging markets | Gates Foundation, regional philanthropies, Wellcome |
| PBC commercialization | Mission-aligned VC (e.g., Lux, DSV, Foresite, ARCH if alignment fits) |
| Bridge / runway | EA Fund, philanthropic donors, family offices |

## Funder-specific positioning per the bifurcation

Per `23_open_science_and_ip.md`, the bifurcation is itself a positive feature for funders:

- **Pre-bifurcation funders** (Astera, Google.org, ARPA-H, NSF, NIH, Wellcome): treat the open Cytoverse map (H1) as the deliverable of their award. The proprietary track is funded separately at Gate 1 by a different class of capital.
- **Post-bifurcation funders for the open track** (continuing philanthropic, federal, regional): underwrite continued open-map maintenance, equity-of-access work, regional sister organizations, and the open clinical adoption.
- **PBC investors at Gate 1 onward**: underwrite the proprietary tracking and navigation product. Foundation governance majority and Helix structure are explicit terms of the deal.

This composition means we never have to ask one funder for both halves of the work, and we never put the open mission at the mercy of a single commercial decision.

## Funding pipeline operations

The pipeline is operationalized in the Monday workspace:

- **Funding Opportunities** board: catalog of all 71+ tracked opportunities with research profiles, requirement extraction, strategic-fit scoring.
- **Grants Pipeline** board: active applications with stage, status, dependencies on Strategic Initiatives and Strategic Goals.
- **Grant Resource Plan**: personnel and compute lines per grant-stage with tiered pricing.
- **Personnel and Compute Rate Cards**: reference pricing tables.

Operating cadence:

- **Weekly:** grants pipeline review with active stage-gate movements.
- **Monthly:** funding-opportunities scan for new RFPs and emerging programs.
- **Quarterly:** strategic-fit re-scoring and pipeline pruning.
- **Annually:** funder portfolio audit at the Hoshin catch-ball.

## Risk: funding concentration

The single largest financial risk in H1 is over-concentration on a small number of funders. The mitigation is the portfolio approach: at any time, no single funder source can be more than 50% of total annual operating budget. UK office creation in Y2 explicitly diversifies the geography of the funding base. The EA Fund and small philanthropic partners create a long tail that buffers against major-grant denial.

## Cross-references

- The bifurcation that gives the funding strategy its structure: `02_horizons_and_bifurcation.md`.
- The Helix governance that keeps the PBC capital aligned to mission: `20_organization_helix.md`.
- The IP and open-science posture funders are buying into: `23_open_science_and_ip.md`.
- The milestone-and-KPI map that funders track against: `40_milestones_and_kpis.md`.
- The risk register entry on funding concentration: `41_risks_and_mitigations.md`.






# Section: 40_milestones_and_kpis.md


# Consolidated Milestones and KPIs

**Companion to:** all horizon documents (`03_*`, `04_*`, `05_*`), the platform documents (`10_*`, `11_*`, `12_*`), and the funding strategy (`30_*`)

This document gives the consolidated view of the milestone roadmap and the KPIs that govern progress. It is the dashboard reference for Board reviews, advisor briefings, and grant reviewer questions about timeline.

## The 10-year milestone Gantt

![Diagram 1 from 40_milestones_and_kpis](/tmp/master_plan_compile/diagrams/40_milestones_and_kpis__1.png)


## KPIs by horizon

### H1 (Years 1 to 5)

| KPI ID | Description | Target | Owner |
|---|---|---|---|
| `KPI-01` | Cumulative non-dilutive funding secured | $30 to 50M | CEO |
| `KPI-02` | Cytoverse axes recover Grotzinger 5-factor structure | r ≥ 0.5 on ≥3 of 5 dimensions | CSO |
| `KPI-03` | Cross-scale imputation AUROC | ≥ 0.75 for ≥1 indication | CSO |
| `KPI-04` | Open releases pass release checklist | 100% | Platform Engineering |
| `KPI-05` | Hugging Face downloads of Cytoverse models | ≥1,000 unique users (Y3) | Communications |
| `KPI-06` | Citing publications | ≥50 within 18 months of release (Y4) | CSO |
| `KPI-07` | UBAP adopted externally | ≥2 partners (Y5) | CTO |
| `KPI-08` | Clinical IRB and partner agreements | ≥3 partner sites (Y2) | Clinical lead |
| `KPI-09` | UK office FTE | ≥5 by Y3 | UK lead |
| `KPI-10` | Zero raw-data egress incidents | 0 incidents (continuous) | Privacy lead |
| `KPI-11` | PAC binding decisions exercised | ≥1 documented case by Y3 | Board secretary |
| `KPI-12` | Clinical-to-wearable alignment quality across protected attributes | No subgroup ≥10% below median (Y3) | Equity lead |
| `KPI-13` *(new)* | Bifurcation Phase tagging on Strategic Initiatives | 100% by Y3 Q1 | Operations |

### H2 (Years 5 to 10)

| KPI ID | Description | Target |
|---|---|---|
| `KPI-21` | FDA cleared products | ≥1 by Y10 |
| `KPI-22` | Field-deployed continuous tracking devices | ≥10,000 by Y10 |
| `KPI-23` | UBAP adopted externally | ≥5 partners by Y10 |
| `KPI-24` | NPS across active users | ≥50 with no demographic subgroup below 30 |
| `KPI-25` | PBC operational status | Break-even or funded path within 24 months |
| `KPI-26` | PAC multi-continental composition | At least one seat per active region |
| `KPI-27` | Foundation operations | Self-sustained without further philanthropic catalytic capital |
| `KPI-28` | Annual open releases of Cytoverse map | ≥1 per year |

### H3 (Years 10 to 15)

| KPI ID | Description | Target |
|---|---|---|
| `KPI-41` | Regional sister organizations | 3 to 5 active by Y15 |
| `KPI-42` | Languages supported in Cytonome | ≥20 by Y12 |
| `KPI-43` | Regulatory clearances | ≥5 jurisdictions by Y15 |
| `KPI-44` | WHO-level policy contributions | ≥1 substantive contribution by Y14 |
| `KPI-45` | UBAP recognition | International standards body adoption (IEEE, ISO, or HL7) |
| `KPI-46` | Substrate handoff readiness | Multi-stakeholder steward ready by Y15 |

## KPI cadence

- **Quarterly review.** All H1 KPIs reviewed quarterly at the OKR review.
- **Annual update.** All KPIs reviewed annually at the Hoshin catch-ball; targets adjusted with explicit justification.
- **Board cadence.** Foundation Board sees KPI-01 (funding), KPI-04 (release-checklist compliance), KPI-10 (privacy), KPI-11 (PAC) every meeting; full set quarterly.
- **Funder cadence.** Funder reports use KPIs aligned to the specific grant; the master KPI list is the superset.

## Bifurcation tagging KPI

A new KPI for v2.0: every Strategic Initiative carries a Bifurcation Phase tag (`pre-36m-open`, `post-36m-open`, `post-36m-proprietary`). Coverage is the KPI: 100% by Y3 Q1. Without complete tagging, the bifurcation cannot be operationalized cleanly at M37.

## Cross-references

- Detailed milestones by horizon: `03_short_term_1to2y.md`, `04_mid_term_5to6y.md`, `05_long_term_10y.md`.
- Gate criteria that the KPIs feed: `02_horizons_and_bifurcation.md`.
- Funding KPIs in detail: `30_funding_strategy.md`.
- Risk register: `41_risks_and_mitigations.md`.
- Monday boards that hold the operational KPI state: `appendix/C_monday_restructure_spec.md`.






# Section: 41_risks_and_mitigations.md


# Risks and Mitigations

**Companion to:** all horizon documents and `40_milestones_and_kpis.md`

The Cytognosis risk register is maintained on the Risks Register Monday board. This document presents the strategic-level risk picture and the new risks introduced by the v2.0 changes (bifurcation, parallel FM track, PAC, clinical-to-wearable subtrack).

## Risk matrix

![Diagram 1 from 41_risks_and_mitigations](/tmp/master_plan_compile/diagrams/41_risks_and_mitigations__1.png)


## Strategic-level risk register

| ID | Risk | Likelihood | Impact | Mitigation | Track | Source |
|---|---|---|---|---|---|---|
| R-01 | Cross-scale imputation fails at clinically useful effect sizes | Medium | High | Three independent indications (neuropsychiatric, autoimmune, neurodegen) so domain-specific failure does not collapse platform; early retrospective evidence by M24 | T1, T3 | v1.0 |
| R-02 | FDA pathway unclear for continuous monitoring products | Medium | High | Engage FDA DHCE and Biomarker Qualification Program from Y1; general-wellness first, disease-claim second | T3, T7 | v1.0 |
| R-03 | Single-source grant funding concentration | Medium | High | Portfolio approach; UK office creates second grant ecosystem; Helix structure gives optionality into VC for PBC | T10 | v1.0 |
| R-04 | H1 to H2 Helix transition fails | Medium | Catastrophic | Helix Framework is itself a deliverable; legal counsel from Y1; PBC charter drafted before Y3 | T8, T9, T10 | v1.0 |
| R-05 | Talent: cross-scale expertise is rare | High | High | Affiliate-first hiring model; Science+Engineering track pairing; UK expansion diversifies talent pool | T9 | v1.0 |
| R-06 | Privacy: single re-ID incident destroys trust | Low | Catastrophic | Edge-first architecture; DP and re-ID probes on every release; zero raw-data egress SLO | T2, T4, T8 | v1.0 |
| R-07 | Mission drift post-PBC activation | Medium | Catastrophic | Bylaws Articles VI and XI; board composition requirements; people-as-seed-funders alignment; PAC binding rights | T8, T9 | v1.0 |
| R-08 *(new in v2.0)* | Bifurcation policy not Board-ratified before M30 | Low | High | Without it, PAC cannot operate at the gate; without PAC at the gate, Gate 1 fails. Ratify at M12 or earlier; provisional operating policy before formal ratification if needed | T8, T14 | v2.0 |
| R-09 *(new in v2.0)* | fNIRS-to-fMRI alignment too lossy for clinical-to-wearable transition | Medium | High | Multimodal fusion (fNIRS + EEG + physiology together) recovers more than fNIRS alone; equity-stratified alignment quality reporting; defer wearable-only deployment for affected populations | T15, T2 | v2.0 |
| R-10 *(new in v2.0)* | Equity gap in alignment-model quality is structural and unfixable for some subgroups | Low | Catastrophic | If unfixable, the affected modality is not deployed for the affected population; ship inclusive subset rather than ship-and-fail | T15, T6, T13 | v2.0 |
| R-11 *(new in v2.0)* | Cellular FM track bandwidth constrained because Mango unavailable | Medium | Medium | Confirmed at 2026-05-07: Shourya leads both tracks; Mango contributes as bandwidth allows; shared infrastructure package keeps work parallel rather than serial | T1, T2 | v2.0 |
| R-12 *(new in v2.0)* | PAC and operational leadership deadlock on a participant-impacting decision | Medium | High | Pre-committed escalation to Foundation Board with both positions; SLAs on routine decisions; pre-committed timeboxing on resolution | T14 | v2.0 |
| R-13 *(new in v2.0)* | UBAP fails to gain external adoption | Medium | Medium | Lightweight v1; reference implementation in Apache 2.0; co-development with strategic partners (Delphi, Caltech FRO); standards-body engagement at Y6+ | T4, T2, T5 | v2.0 |
| R-14 *(new in v2.0)* | Patient consent revocation creates technical inability to delete from federated substrate | Medium | Medium | Cryptographic revocation (destroy decryption keys, render shards inaccessible) where physical deletion is not possible; user-facing transparency about technical limits | T8, T11, T14 | v2.0 |
| R-15 *(new in v2.0)* | Hardware partner discontinues or pivots before alignment models are robust | Medium | Medium | Multi-vendor strategy from Y1; UBAP standard ensures replaceability; review hardware partners annually | T2, T5 | v2.0 |
| R-16 *(new in v2.0)* | Patty Purcell unavailable mid-Astera draft | Low | Medium | Astera proposal architecture is owned by Mohammadi with Patty as collaborator; backup grants-and-comms capacity in-house by Y2; explicit succession plan for the consultant role | T10, T9 | v2.0 |
| R-17 *(new in v2.0)* | Astera consulting payment workflow delays Patty's ability to fully engage | Low | Low | Consulting fee included in proposal budget for early payment; bridge agreement if needed; alternative funding source identified if proposal not awarded | T10 | v2.0 |

## Risk owners

The Risks Register Monday board (id `18409731742`) tracks each entry with an owner. Per the Monday survey, the board exists but operational metadata (owners, current status updates) was empty at compilation. Restructure spec (`appendix/C_monday_restructure_spec.md`) includes populating risk owners.

| Risk category | Owner |
|---|---|
| Scientific (R-01, R-09, R-11) | CSO (Mohammadi acting through Y1; dedicated CSO Y2+) |
| Regulatory (R-02) | Clinical / Regulatory lead (hire by Y2 Q3) |
| Financial (R-03, R-17) | CEO and grants/operations |
| Organizational (R-04, R-05, R-08, R-12, R-16) | CEO and Board secretary |
| Privacy (R-06, R-14) | Privacy lead and PAC |
| Mission (R-07) | Foundation Board |
| Equity (R-10) | Equity lead and PAC |
| Ecosystem (R-13, R-15) | CTO |

## Risk review cadence

- **Quarterly review** at the OKR review meeting; status updates on any high-priority risk.
- **Annual deep review** at the Hoshin catch-ball; matrix recomputed; new risks added as the operating environment shifts.
- **Trigger-based emergency review** if any high-priority risk escalates between scheduled reviews.

## What this v2.0 adds

The v1.0 risk register had 7 strategic risks (R-01 through R-07). v2.0 adds 10 (R-08 through R-17) reflecting the new structural decisions:

- bifurcation requires governance ratification (R-08);
- clinical-to-wearable alignment introduces specific scientific and equity risks (R-09, R-10);
- parallel cellular and connectomic tracks introduce a bandwidth risk specific to the Purdue partnership (R-11);
- PAC governance introduces deadlock risk (R-12);
- UBAP open standard introduces adoption risk (R-13);
- post-quantum and federated substrate introduce technical-deletion risk under consent revocation (R-14);
- hardware partner dependency introduces continuity risk (R-15);
- Astera consultant engagement introduces specific grant-cycle risks (R-16, R-17).

Each new risk has a documented mitigation and a track tag for ongoing ownership.

## Cross-references

- The bifurcation that drives several v2.0 risks: `02_horizons_and_bifurcation.md`.
- The clinical-to-wearable subtrack that drives R-09 and R-10: `12_clinical_to_wearable.md`.
- The PAC charter that addresses R-12: `21_patient_advocacy_council.md`.
- The patient-safety architecture that addresses R-06 and R-14: `16_patient_safety_architecture.md`.
- The funding strategy that addresses R-03: `30_funding_strategy.md`.
- The Helix structure that addresses R-04 and R-07: `20_organization_helix.md`.






# Section: A_cell_state_meeting_synthesis.md


# Appendix A: Cell-State / Perturbation Modeling Meeting Synthesis

**Date:** 2026-05-07
**Source:** [Google Meet notes](https://docs.google.com/document/d/16slm-XKv_Hejr4gby7OpLFcPqqUIa6UMK07pzKWbkts/edit)
**Attendees:** Shourya Verma (Purdue, lead RA), Nadia Atallah Lanman (Purdue), Ananth Grama (Purdue, faculty), Shahin Mohammadi (Cytognosis), Mango Wang (Meta, contributor), additional Purdue IPAI team members
**Companion to:** `11_technical_track_FMs.md`

This synthesis records the architectural decisions and operational decisions taken at the cell-state / perturbation-modeling meeting. Decisions are normative; the technical-track document (`11_technical_track_FMs.md`) is built on this record.

## Decisions

### Architectural

- Build cellular and connectomic foundation models **in parallel** using the same architectural building blocks at two scales.
- The shared building blocks are: WaveGC (Wave Graph Convolution) for multi-resolution graph diffusion, plus AlphaGenome-style cross-resolution transformer attention for inter-block information sharing.
- Replace WaveGC's MLP block (which is oblivious across scales) with the AlphaGenome interconnected attention pattern.
- Implement the multi-resolution wavelet plus cross-scale attention layer as a **standalone reusable package** (the "Lego pieces" approach) inside the `neuroconnectomics` repository, used by both connectomic and cellular tracks.
- Treat the molecular foundation model as a **trainable component** of the cellular FM, with end-to-end gradient flow through cross-resolution attention bridges. This is distinct from scPrint2 / TranscriptFormer which freeze the molecular FM as a static dictionary.
- Model the **residual space** (delta from healthy baseline) using conditional flow matching, generating counterfactual states from noise conditioned on health-state context.

### Repository structure

Four parallel repositories:

- `neurogenomics`: genome-level work, WGS, baseline molecular FM fine-tuning. Mohammadi initial lead.
- `neuroconnectomics`: connectomic FM, voxel-level work, multimodal imaging integration. **Hosts the shared `neuroconnectomics-core` Lego-pieces package.** Shourya lead.
- `neurotranscriptomics`: cellular FM, single-cell + pseudobulk, multi-scale molecular-to-cellular work. Shourya + Mango (bandwidth allowing) + Mohammadi.
- `neurobehavior`: macro phenotyping, LLM-derived neurobehavioral axis quantification, NBO ontology integration. Mohammadi initial lead.

A `neurogenomics` Cookiecutter template will be created (Mohammadi action item) so each repo bootstraps with the Cytognosis dev-standards.

### Roles

- Shourya leads both connectomic AND cellular tracks given Mango's transition to Meta.
- Mango contributes to cellular as bandwidth allows; remains formally on the team.
- Mohammadi is the primary advisor on the cellular track, despite less hands-on connectomic experience.
- Grama is the on-paper supervisor at Purdue and primary subaward channel.
- Mohammadi visits Purdue at end of May or early June 2026 to white-board three-to-six-month milestones; Grama covers travel reimbursement.

### Pre-training and prototyping

- **Connectomic.** Pre-training task: stratified subgraph masking. Initial prototyping on Open Era's Y dataset (~300 samples, harmonized). Scale-up: Yale dataset (Shourya secures access), then UK Biobank (≥40K fMRI), then ABCD, HCP.
- **Cellular.** Masked gene prediction conditioned on cellular context; perturbation prediction. PsychENCODE pseudobulk first (open). NeuroBioBank WGS for genotype-phenotype joint training. Allen Brain Atlas microarray data for connectomic deconvolution alignment.

### Cross-track integration

- Bridges between cellular and connectomic FMs trained on **paired data**: ENIGMA consortium primary (disease-centric, multimodal, fMRI plus genotype); PsychENCODE 388 paired samples secondary.
- Strategy: cross-attention or contrastive loss objectives with the alignment task simplified by both models being phenotype-oriented.

### Publication strategy

- First publication: multi-scale infrastructure connecting molecular and cellular data. Connectome **excluded** from this first paper to keep scope clean.
- Connectomics methods paper: separate output, also targeting Nature Methods or Nature Machine Intelligence.
- Mohammadi noted Nature Machine Intelligence is rapidly growing in impact factor and emphasizes methodology over result-centric framing.

### Project management

- Adoption of Monday.com for project management with OKRs.
- Quantitative metrics for success defined at the milestone-planning visit.
- Industry-style approach intended to improve project definition and tracking.

## Action items recorded

| Owner | Item |
|---|---|
| Shahin Mohammadi | Send WaveGC paper and code repository links to Shourya and Mango. |
| Shahin Mohammadi | Create and share non-connectomics Copier repository for boilerplate. |
| Shahin Mohammadi | Create discussion thread for prioritized neuro datasets and FM papers (include Tier 1 papers like Neurostorm). |
| Shourya Verma | Download Y dataset from Open Era. |
| Shourya Verma | Implement separate standardized package containing wavelet and transformer convolution layer; refactor components from WGC and AlphaGenome repos. |
| Group | Define architecture: explore whether projection back to original space is needed after each spectral graph convolution layer or only at the outside boundary. |
| Shourya Verma | Acquire Yale dataset access permission. |
| Shourya Verma | Build basic architecture and implement spectral graph convolution; build pre-training with graph masking. |
| Shourya Verma | Manage both connectomic and cellular development since Mango is unavailable. |
| Group | Implement Monday-based project tracking using OKRs. |
| Shourya Verma | Provide progress update next week. |

## Open architectural questions

- Projection back to original space: per layer or only outermost? Affects standardized embedding-layer interface.
- Conditioning structure for conditional flow matching: categorical disease label, continuous health-state coordinate, individualized prior from genome? Likely all three, ablated.
- Computational scaling of end-to-end multi-scale training with trainable molecular FM. What scaling regime?
- Resolution: target end of May 2026 visit to Purdue.

## Strategic significance

This meeting effectively defines the technical track for H1 P1 (Cytoverse). The decisions are operationalized in:

- `11_technical_track_FMs.md` (architecture detail);
- `03_short_term_1to2y.md` (Y1-Y2 deliverables and OKRs);
- `30_funding_strategy.md` (Astera proposal funds the cellular FM track; Google.org Impact funds the connectomic track per the meeting alignment);
- `appendix/C_monday_restructure_spec.md` (FM Family tag added to Strategic Initiatives so cellular vs connectomic vs cross-scale is queryable).






# Section: B_patty_meeting_synthesis.md


# Appendix B: Patty Purcell Strategic Meeting Synthesis

**Date:** 2026-05-08
**Source:** [Google Meet notes](https://docs.google.com/document/d/1nr4lfNSD1JrHhq5fIaEoZAQuimlEAFFtS3L0wNUUFkw/edit)
**Attendees:** Patricia Purcell PhD (consultant), Shahin Mohammadi (Cytognosis)
**Companion to:** `00_executive_summary.md`, `03_short_term_1to2y.md`, `22_people_and_consultants.md`, `30_funding_strategy.md`

This synthesis records the strategic-development decisions and the consulting-engagement decisions taken at the Patty Purcell meeting. The meeting reaffirmed the high-level GPS-for-Health framing in funder-facing language and finalized the Astera proposal positioning.

## Decisions

### Consulting engagement

- Patty Purcell is engaged as a consultant on the Astera proposal at approximately **$300/hr**, **~8 hr/wk**, on an hourly basis.
- Compensation is **included in the Astera proposal budget** for early payment (rather than absorbing into Foundation operations).
- Continuing role anticipated through the Y1-Y2 grant cycle as additional grants are written.

### Astera proposal positioning

- Working title: **"Open Multiscale Dimensional Map of Human Psychiatry"** (alternate framing: "Multimodal Multiscale Map of Mental Health States to Democratize Precision Psychiatry").
- Astera focus is on the **micro scale** (genotype + single cell) for the first 18 months; uses PsychENCODE-class data to fine-tune the AlphaGenome model toward brain cell types.
- Google.org Impact focus is on the **meso scale** (connectomic work).
- Cross-scale modeling **commences after the first 18 months**, aligning models using ENIGMA consortium data.
- **Astera due date: Sunday, 2026-05-10.**

### Strategic narrative

The platform's three-scale framing was reaffirmed for funder audiences:

- **Micro:** molecules and cells (genotype + single-cell RNA-seq).
- **Meso:** connectomics and neuroimaging (fMRI + EEG).
- **Macro:** neurobehavioral phenotypes (LLM-derived axes from conversation + clinical scales).

Three building blocks for a "GPS for human health":

- a multi-axis **map** (Cytoverse);
- multiple tracking **sensors** (Cytoscope);
- a **navigation** system providing personalized causal recommendations (Cytonome).

### Investor-facing two-fold value proposition

- Non-invasive interventions tailored to biotype (e.g., personalized CBT skills, lifestyle plans).
- Targeted therapeutics tailored to biotype (e.g., precision TMS, biomarker-stratified pharmacology).

### Bipolar biotype example as proof of concept

The bipolar biotyping example was used to demonstrate platform value:

- At least two distinct axes: **mood axis** and **thought axis**.
- Mood axis is genetically shared with Major Depressive Disorder and is linked to **BDNF signaling pathway**, which is relevant to successful psilocybin clinical trials for depression.
- Demonstrates molecular biotyping for psychiatric disorders that captures patient heterogeneity (one of approximately 1,500 to 2,000 neurobehavioral axes Cytognosis is curating).

### Data sources for the Astera proposal

UK Biobank, NeuroBioBank, the MVP military database, PsychCode, and the ENIGMA consortium. Some of these have never been connected before; the cross-source integration is itself a contribution.

### Lived-experience-informed motivation

- Mohammadi's TBX1 mutation (a 32 base pair insertion in exon 2) is novel but falls within the 22q11 deletion syndrome (1 in 2000 to 4000 children, often undiagnosed).
- The single-gene mutation is easier to study than the larger 22q11 deletion because a healthy control cell line can be created via CRISPR editing.
- Demonstrates the broader thesis: knowing the genetic cause does not "fix" the issue (the temporal window of fetal development is missed); we need to understand each patient's **trajectory** since the genetic cause initiated.

### Pet and infant cohorts as opportunistic data sources

- Pet data, particularly in dogs, is often clean and available with comprehensive genotyping and behavioral phenotyping.
- Many dog psychiatric manifestations map closely to human ones.
- Infants are vulnerable (cannot articulate pain) but also valuable early targets.
- These markets are revisited in `15_app_design.md` as the loved-ones extension.

### IRB strategy

- A non-profit external IRB called **Northstar IRB** is under consideration for the joint Cytognosis study with Brad Ruzicka (focusing on factorizing genotype and phenotype from neurobiological data into an interpretable space).
- Salus IRB remains the canonical option per `key_consultants.md`; both are evaluated.

### Grant strategy and trust

- NIH is structured to fund incremental work, making it difficult to get funding for groundbreaking, different research.
- ARPA-H (founded 2023) explicitly values novelty and may help change this dynamic.
- Reviewers must trust both the idea AND the applicant; explicit team-fit sections are needed in proposals.
- Google.org Impact estimated submission pool around 2,000.

## Action items recorded

| Owner | Item |
|---|---|
| Shahin Mohammadi | Share Jordan's two recent papers covering cross-14 disorders work with Patty. |
| Shahin Mohammadi | Allocate specific time for Patty in Monday meeting. |
| Shahin Mohammadi | Send the Astera proposal draft, including cost estimates and milestones, to Patty for review and feedback. |

## Strategic significance

This meeting effectively reaffirms the funder-facing strategic narrative for the active grant cycle:

- the **GPS for Health** framing is the canonical funder-facing language;
- the **three-scale** (micro / meso / macro) framing maps cleanly to the three pillars (P1 Cytoverse + scale anchors);
- the **bipolar mood / thought** dual-axis biotyping example anchors the proof-of-concept narrative;
- the **Astera (micro)** + **Google.org (meso)** + **post-M18 cross-scale** funding sequence is operationally aligned;
- Patty's compensation arrangement (included in proposal budget at $300/hr) sets the precedent for future grant-funded consulting engagements.

The meeting also touched on broader themes (ethics, work-environment culture, NIH structural critique, the founder's TBX1 motivation), which are not directly operational but inform the founder-narrative content used in `science-platform` skill and grant materials.






# Section: C_monday_restructure_spec.md


# Appendix C: Monday Workspace Restructure Specification

**Companion to:** `01_identity_and_framework.md`, `02_horizons_and_bifurcation.md`, `21_patient_advocacy_council.md`

This appendix specifies the Monday.com workspace changes required to align the operational source of truth with the v2.0 master plan. The restructure is mandatory: without it, the bifurcation tagging, parallel FM tracks, PAC governance, and three-time-horizon framing cannot be operationalized.

User decision (per AskUserQuestion at the start of this engagement): "Document + full Monday restructure to match the new master plan." Backup is recommended before changes are applied.

## Workspace target

| Workspace | ID | Role |
|---|---|---|
| Cytognosis Foundation | 15010552 | Read-only reference (do not modify) |
| Cytognosis OS | 15001658 | Untouched |
| **Main workspace** | **14426768** | **Active build target** |

All changes apply to the Main workspace.

## Changes by folder

### Strategic Planning folder

| Change | Action | Notes |
|---|---|---|
| Add T14 PAC subtrack to Tracks board | New item | Subtrack T14 (Patient Advocacy Council) under M4 Organization. Tag any PAC-relevant initiatives with T14. |
| Add T15 Cross-modal Alignment subtrack to Tracks board | New item | Subtrack T15 under M5 Learning. Tag clinical-to-wearable alignment work with T15. |
| Update Meta-track dropdown to fully populate M1-M5 | Schema | Currently dropdown supports M1-M5 but only 4 meta-tracks exist; populate all five. |
| Backfill H3 Strategic Initiatives | New items | Add 8-12 H3 initiatives covering globalization, consortium hand-off, Cytoverse v2, regional federation. Anchor: existing SI-LMIC-Pilot. |
| Add **Bifurcation Phase** status column to Strategic Initiatives | Column | Values: `pre-36m-open`, `post-36m-open`, `post-36m-proprietary`. Tag every existing SI; default to `pre-36m-open` until reviewed. |
| Add **Bifurcation Phase** status column to Milestones Roadmap | Column | Same values; tag every existing milestone. |
| Add **FM Family** dropdown to Strategic Initiatives | Column | Values: `Cellular`, `Connectomic`, `Behavioral`, `Cross-scale`, `n/a`. Tag SI-Neuroverse-Micro, SI-Neuroverse-Meso, SI-Neuroverse-Macro-LLM, SI-CrossScale-Paired accordingly. |
| Rename pillars P1/P2/P3 to plain language | Schema | Current: `P1 Cytoverse`, `P2 Cytoscope`, `P3 Cytonome`. Update labels to: `Cytoverse Map (P1)`, `Cytoscope Sensor (P2)`, `Cytonome Navigator (P3)` for plain-language alignment with the master narrative. |
| Add three time-horizon tags as a column | Column | Values: `Short 1-2y`, `Mid 3-6y`, `Long 7-10y`. Apply to Strategic Initiatives, Strategic Goals, Milestones. Maps to the user-facing horizon framing of v2.0 (which is decoupled from the H1/H2/H3 5/10/15-year structural framing). |
| Re-tag Foresight-related milestones | Status update | Move from Active Strategic Planning to Archive. Foresight rejected per `30_funding_strategy.md`. |
| Populate KPI current values | Data | Per `40_milestones_and_kpis.md` KPI list. KPI-01 through KPI-13 (H1) at minimum. |
| Populate Risks Register owners | Data | Per `41_risks_and_mitigations.md` owner mapping. Include new R-08 through R-17. |

### Portfolio Management folder

| Change | Action | Notes |
|---|---|---|
| Populate Projects pillar dropdowns | Schema + data | Currently empty. Define labels per the renamed pillars; tag each Project. |
| Add Bifurcation Phase column to Projects | Column | Mirror the Strategic Initiatives change. |
| Populate OKR owners | Data | Per Phase 1 Operational Plan ownership mapping. |

### New: PAC governance board

| Change | Action | Notes |
|---|---|---|
| Create board: `PAC · Patient Advocacy Council` | New board | Under Strategic Planning folder. Holds charter document, seat roster, decision log, meeting cadence. |
| Charter linked to board | Doc | Reference to `21_patient_advocacy_council.md` and the formal charter document once ratified. |
| Seat roster | Items | One row per seat, columns: name, indication area, geography, term start, term end, rate, conflict-of-interest disclosed. |
| Decision log | Subitems | Each decision with: date, scope, outcome, dissents, links to affected Strategic Initiatives or studies. |

### Fundraising folder

| Change | Action | Notes |
|---|---|---|
| Update Astera grant pipeline entry | Data | Add Patty consulting line ($300/hr × ~8 hr/wk × duration) per Patty meeting. |
| Update Google.org Impact entry | Data | Confirm submission status as of 2026-04-17. |
| Update Foresight entry | Status | REJECTED. |
| Add v2.0 grant pipeline targets | New items where missing | ARPA-H PHO at $50M, NSF Tech Labs $15M, Convergent Research FRO $50M, Wellcome Leap $8M, CZI $5M, Gates (long-term planned). |

### Resources folder

| Change | Action | Notes |
|---|---|---|
| Add Patricia Purcell to Personnel & Hiring as consultant | New item | Rate $300/hr (Astera) / $150/hr base, hours and engagement detail. |
| Add Northstar IRB option to Personnel & Hiring | New item | Cross-reference to Salus IRB. |

## New columns specification

### Bifurcation Phase (Status type)

```yaml
column_name: Bifurcation Phase
column_type: status
values:
  - label: pre-36m-open
    color: "#3B7DD6"  # Cytognosis Azure
    description: Open by default; pre-bifurcation.
  - label: post-36m-open
    color: "#5145A8"  # Cytognosis Indigo
    description: Open Foundation track post-bifurcation.
  - label: post-36m-proprietary
    color: "#8B3FC7"  # Cytognosis Violet
    description: Proprietary PBC track post-bifurcation.
  - label: n/a
    color: "#757575"  # Neutral
    description: Not yet classified or not subject to bifurcation.
```

### FM Family (Dropdown type)

```yaml
column_name: FM Family
column_type: dropdown
values:
  - Cellular
  - Connectomic
  - Behavioral
  - Cross-scale
  - n/a
```

### User-facing Time Horizon (Status type)

```yaml
column_name: Time Horizon (UF)
column_type: status
values:
  - label: Short 1-2y
    color: "#3B7DD6"
  - label: Mid 3-6y
    color: "#8B3FC7"
  - label: Long 7-10y
    color: "#5145A8"
  - label: 10y+
    color: "#14A3A3"
```

Note: User-facing time horizons are decoupled from the structural H1/H2/H3 (5/10/15-year) framing. Many initiatives span both. This column is for narrative alignment with the user's horizon framing in v2.0.

## Tag-application rules

### For every Strategic Initiative

- Bifurcation Phase: required, default `pre-36m-open` if uncertain.
- FM Family: required, default `n/a` for non-FM initiatives.
- Time Horizon (UF): required.
- Existing tags (Pillar, Meta-track, Subtrack, Horizon, Status) preserved.

### For every Milestone

- Bifurcation Phase: required.
- Time Horizon (UF): required.

### For every Project

- All of the above; also Pillar dropdown populated (currently empty).

## Restructure execution order

1. **Backup.** Export current state of Main workspace (Monday's CSV export per board).
2. **Schema additions.** Add new columns (Bifurcation Phase, FM Family, Time Horizon UF). Empty by default.
3. **PAC board creation.** New board with seat roster, charter link, decision log structure.
4. **Subtrack additions.** T14 PAC and T15 Cross-modal Alignment added to Tracks board.
5. **H3 SI backfill.** 8-12 new Strategic Initiatives for Horizon 3.
6. **Tag application.** Tag existing items with new column values.
7. **Pillar relabeling.** Update P1/P2/P3 labels.
8. **Foresight archive.** Move Foresight items to Archive.
9. **Operational metadata.** Populate KPI values, Risk owners, OKR owners, Projects pillar labels.
10. **Verification.** Spot-check a representative sample of items per board to confirm tags applied correctly.

## What this restructure does NOT change

- The four-layer hybrid framework (Three Horizons / OGSM / Hoshin / OKRs) and the McKinsey 12 overlay are preserved unchanged.
- The 6-folder layout (Strategic Planning / Portfolio Management / Archive / Fundraising / Resources / Research Outputs) is preserved.
- The 4 meta-tracks (M1-M4) plus M5 are preserved; T14 and T15 add to the existing subtrack list rather than replacing it.
- Existing SI IDs are preserved; new tags are applied to existing items rather than items being recreated.
- Bidirectional linkage between Funding Opportunities and Strategic Initiatives is preserved.

## Cross-references

- Why these changes are needed: `01_identity_and_framework.md`, `02_horizons_and_bifurcation.md`.
- The PAC governance role: `21_patient_advocacy_council.md`.
- The bifurcation rule that the new tags enforce: `23_open_science_and_ip.md`.
- The original Monday survey that identified these gaps: communicated in the 2026-05-08 conversation with Shahin (compiled at compilation time of v2.0).



