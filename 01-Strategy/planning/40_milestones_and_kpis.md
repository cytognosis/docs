# Consolidated Milestones and KPIs

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: leadership
> **Tags**: `strategy`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

**Companion to:** all horizon documents (`03_*`, `04_*`, `05_*`), the platform documents (`10_*`, `11_*`, `12_*`), and the funding strategy (`30_*`)

This document gives the consolidated view of the milestone roadmap and the KPIs that govern progress. It is the dashboard reference for Board reviews, advisor briefings, and grant reviewer questions about timeline.

## The 10-year milestone Gantt

```mermaid
gantt
    title Cytognosis 10-Year Roadmap · Months Anchored to April 2026
    dateFormat YYYY-MM
    axisFormat %Y
    section Foundation
    SAB stood up                            :milestone, m_sab, 2026-10, 0d
    Copier template v1                       :milestone, m_copier, 2026-10, 0d
    PAC charter binding                      :milestone, m_pac, 2027-04, 0d
    UK office formed                         :milestone, m_uk, 2027-04, 0d
    PBC charter draft                        :milestone, m_pbc_draft, 2028-10, 0d
    Bifurcation policy ratified              :crit, milestone, m_bif, 2029-04, 0d
    Gate 1 transit (PBC activation)          :crit, milestone, m_g1, 2031-04, 0d
    Foundation expansion to regional         :milestone, m_reg, 2033-04, 0d
    Gate 2 transit                           :crit, milestone, m_g2, 2036-04, 0d
    section Cytoverse (Map)
    Neuroverse Micro v1                      :milestone, m_nv1, 2027-10, 0d
    Neuroverse Macro v1                      :milestone, m_nv1m, 2027-10, 0d
    Neuroverse Meso v0.5                     :milestone, m_nv05, 2028-04, 0d
    Helix Framework paper                    :milestone, m_helix, 2028-04, 0d
    Neuroverse Meso v1                       :milestone, m_nv1mes, 2029-04, 0d
    Cross-Scale Paired Models                :milestone, m_cs, 2030-04, 0d
    Immunoverse v1 (UK)                      :milestone, m_iv1, 2031-04, 0d
    Annual major releases (open, post-bif)   :open_rel, after m_bif, 84M
    section Cytoscope (Sensor)
    Phase 0 internal pilot                   :milestone, m_p0, 2027-04, 0d
    UBAP draft v0.1 RFC                      :milestone, m_ubap0, 2027-10, 0d
    External 20-30 person pilot              :milestone, m_ext, 2028-10, 0d
    Delphi LOI                               :milestone, m_del, 2028-04, 0d
    UBAP v1.0                                :milestone, m_ubap1, 2029-04, 0d
    Cytoscope wearable v1 architecture freeze :milestone, m_csv1arch, 2030-10, 0d
    Cytoscope wearable v1 fielded             :milestone, m_csv1, 2032-04, 0d
    section Cytonome (Navigator)
    Three-layer privacy spec                 :milestone, m_priv, 2027-04, 0d
    Cytonome v0.1 runtime                    :milestone, m_cn01, 2027-10, 0d
    Long-term memory module                  :milestone, m_mem, 2028-04, 0d
    Voice interface v1                       :milestone, m_voice, 2028-10, 0d
    Causal recommendation v1                 :milestone, m_causal, 2029-10, 0d
    Post-quantum substrate                   :milestone, m_pqc, 2030-04, 0d
    Cytonome v1.0 candidate                  :milestone, m_cn1, 2032-04, 0d
    Cytonome FDA cleared                      :milestone, m_fda, 2034-04, 0d
    section Clinical Translation
    Salus IRB live                           :milestone, m_irb, 2026-07, 0d
    Clinical partnerships signed             :milestone, m_part, 2027-01, 0d
    Retrospective dimensional evidence        :milestone, m_retro, 2028-04, 0d
    FDA pre-sub                              :milestone, m_fdasub, 2030-04, 0d
    ARPA-H PHO submission                    :milestone, m_pho, 2030-10, 0d
    Clinical study at full enrollment        :milestone, m_full, 2030-04, 0d
    section Cross-Modal Alignment (T15)
    Public-data alignment v0                 :milestone, m_align0, 2028-04, 0d
    Internal core-team pilot complete        :milestone, m_core, 2029-04, 0d
    Cohort-scale alignment models            :milestone, m_cohort, 2031-04, 0d
```

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
