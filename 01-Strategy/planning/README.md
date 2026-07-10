# Cytognosis Foundation · Master Strategic Plan

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: leadership
> **Tags**: `strategy`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

**Version:** 2.0 (May 2026) · **Author:** Shahin Mohammadi · **Compiled:** 2026-05-08
**Supersedes:** `01_Cytognosis_Strategic_Roadmap_15-Year.md` v1.1 (April 2026) at the synthesis layer; carries forward the OGSM, Hoshin, and OKR cascades from `02_Cytognosis_Phase1_Operational_Plan.md`.
**Companions retained:** Phase 1 OKR cascade, SI Registry, Framework Synthesis, Roadmap Diagrams.

> **Bridge line.** *Cytognosis exists so no one else waits decades for answers.*

## What this plan is

A consolidated, public-readable master plan for Cytognosis Foundation that integrates:

- The approved four-layer hybrid framework (Three Horizons · OGSM · Hoshin Kanri · OKRs) with the McKinsey 12-element overlay.
- The full GPS-for-Health platform across three components: **Cytoverse** (the map), **Cytoscope** (the sensor), and **Cytonome** (the navigator).
- The 36-month open-science / proprietary-tracking bifurcation that protects the Foundation's mission while creating the IP base for the Public Benefit Corporation subsidiary at Gate 1.
- The parallel cellular and connectomics foundation-model architecture decided in the Cell-State / Perturbation Modeling meeting on 2026-05-07 (with Shourya Verma, Ananth Grama, Nadia Atallah Lanman, and the Purdue IPAI team).
- The high-level strategic narrative aligned with Patty Purcell on 2026-05-08, plus her formal consulting engagement against the Astera proposal.
- The Patient Advocacy Council (PAC) as a first-class governance structure across both entities.

## How to read this plan

The plan is organized as a set of interconnected markdown documents. Each document is self-contained, embeds Mermaid diagrams, and links to its siblings. A consolidated single-document Google Doc version exists for printing, board distribution, and grant-appendix use.

| File | What it covers | Audience |
|---|---|---|
| `00_executive_summary.md` | One-page overview, with status, asks, and headline diagram | Board, funders, advisors |
| `01_identity_and_framework.md` | Vision, mission, values, framework recap, vocabulary | All readers |
| `02_horizons_and_bifurcation.md` | Three Horizons timeline, Gates, the 36m open/proprietary bifurcation | Board, funders |
| `03_short_term_1to2y.md` | Years 1-2 detailed plan: cellular + connectomics FM build, Astera, Google.org Impact, Phase 0 pilot | Operating team, grant reviewers |
| `04_mid_term_5to6y.md` | Years 3-6: clinical study, 36m bifurcation, regulated-product readiness | Board, ARPA-H reviewers |
| `05_long_term_10y.md` | Years 7-10: Gate 1 PBC activation, Cytoscope/Cytonome regulated products, scaled deployment | Board, investors |
| `10_platform_architecture.md` | Cytoverse · Cytoscope · Cytonome integrated platform with data-flow diagram | Technical reviewers |
| `11_technical_track_FMs.md` | Parallel cellular + connectomics FM design (WaveGC + AlphaGenome attention, multi-scale nesting, residual/CFM modeling) | Engineering team, methods reviewers |
| `12_clinical_to_wearable.md` | Multi-modal alignment (fMRI ↔ fNIRS+EEG), Inclusion Study, FRESH initiative, internal core-team pilot | Clinical reviewers |
| `13_sensor_ecosystem.md` | UBAP universal sensor adapter, plug-in store model | Technical reviewers, partners |
| `14_navigation_recommendations.md` | Defensive · corrective · supportive recommendation framework | Clinical reviewers, advocacy |
| `15_app_design.md` | Guardian-coach app sections, kids and pets extension | Product reviewers |
| `16_patient_safety_architecture.md` | Four-tier compute (perception · local · distributed · Cytognosis), post-quantum substrate | Privacy, security, governance |
| `20_organization_helix.md` | Foundation + PBC structure, IP boundary, US + UK + regional federation | Legal, board, funders |
| `21_patient_advocacy_council.md` | PAC charter, seats, decision rights, role across all components | Board, governance |
| `22_people_and_consultants.md` | Team, named consultants and rates, hiring trajectory | Internal, finance |
| `23_open_science_and_ip.md` | Openness policy, dual-licensing, the 36m bifurcation rule | Legal, partners |
| `30_funding_strategy.md` | Active grants, planned grants, Gate 1 VC entry | Finance, board |
| `40_milestones_and_kpis.md` | Consolidated milestone roadmap with Gantt-style Mermaid; KPIs by horizon | All readers |
| `41_risks_and_mitigations.md` | Updated risk register with new entries (PAC, FM parallel-track, fNIRS pilot) | Board, risk |

### Appendices

- `appendix/A_cell_state_meeting_synthesis.md` (Shourya, 2026-05-07)
- `appendix/B_patty_meeting_synthesis.md` (Patty Purcell, 2026-05-08)
- `appendix/C_monday_restructure_spec.md` (operational change list applied to the Monday workspace)

### Diagrams

All Mermaid diagrams are embedded in their parent document and also exported as PNGs in `diagrams/`. The Google Doc compilation embeds the PNGs.

## What changed between v1.1 and v2.0

The five structural updates that justify a major version bump:

- **Bifurcation marker.** The roadmap explicitly distinguishes pre-36-month open clinical/research models (which stay in the Foundation indefinitely with annual public release cycles) from post-36-month proprietary continuous-tracking models (which underpin Gate 1 commercialization through the PBC subsidiary).
- **Parallel cellular + connectomics foundation models.** The technical track reflects the 2026-05-07 architectural decision: shared building blocks (WaveGC + AlphaGenome cross-resolution attention), four parallel repositories, end-to-end multi-scale training (genes-as-units, scRNA-seq as sensor), and residual/CFM modeling of disease shifts.
- **Patient Advocacy Council promoted.** PAC moves from a buried Strategic Initiative (`SI-Participant-Council`) to a first-class governance entity with charter, seats, and decision rights across grants, releases, and clinical study design.
- **Clinical-to-wearable alignment introduced explicitly.** Years 1-3 add a dedicated alignment subtrack (fMRI ↔ fNIRS, plus EEG cross-modality) using the Inclusion Study and FRESH initiative datasets, plus a consented internal core-team pilot. Without this, the Y4-Y5 wearable transition collapses.
- **Three time-horizon framing for navigation recommendations.** Defensive (avoid), corrective (reverse), supportive (cope) becomes the canonical taxonomy in app, grants, and clinical narrative.

## Status snapshot at compilation time

| Indicator | Value | Notes |
|---|---|---|
| Submitted active grants | 2 | Astera Residency (in review), Google.org Impact (submitted 2026-04-17, $2.2M ask) |
| Rejected, decided | 2 | Foresight AI for Safety, YC W25 + S26 |
| In preparation | 5+ | ARPA-H PHO, NSF Tech Labs, Convergent Research FRO, Wellcome Leap, CZI |
| Confirmed consultants | 5 | Duane Valz (legal), Patricia Purcell (grants/comms, $300/hr added to Astera), Brad Ruzicka (clinical subaward), Jose Davila-Velderrain (cross-scale neuro subaward), Ananth Grama (Purdue IPAI subaward) |
| Active research staff | 1 lead RA | Shourya Verma (Purdue), now leading both connectomics and cellular FM tracks given Mango's Meta start |
| Foundation entity | 501(c)(3) active | EIN 39-4383634, UEI HS4PRLL7AKY5, SSF California |
| PBC charter | Drafted, not activated | Activation reserved for Gate 1 (target Y5) |
| Monday workspace state | Four-layer scaffold complete | Restructure applied per `appendix/C` |

## Maintenance

- **Owner:** Shahin Mohammadi (CEO)
- **Cadence:** Annual major revision in October catch-ball; quarterly update of metrics and grant pipeline.
- **Source-of-truth boundary:** This plan owns the integrated narrative. The Monday workspace owns the operational state (boards, OKRs, projects, grants). The SI Registry owns canonical Strategic Initiative identifiers.
