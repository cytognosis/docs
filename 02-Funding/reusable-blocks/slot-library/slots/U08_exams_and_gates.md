---
slot_id: U08
slot_name: Mid-term & final exams (quantitative go/no-go)
heilmeier_parent: Q8
required_by:
  - heilmeier
  - nih_r01
  - arpah_mission_office
  - doe_genesis
  - brains_accelerator
  - foresight_nodes
  - google_impact_challenge
useful_for:
  - nsf_tech_labs
  - astera_residency
  - yc_s26_pbc
sub_slots:
  - id: U08.1
    name: Quantitative success metrics
    max_words: 300
    max_chars: null
    funder_hooks:
      - heilmeier.Q8
      - google_impact_challenge.Q19a
      - google_impact_challenge.Q28
      - brains_accelerator.B5
      - arpah_mission_office.appendix_a_3
      - doe_genesis.narrative_3
  - id: U08.2
    name: Go/no-go decision gates per phase
    max_words: 400
    max_chars: null
    funder_hooks:
      - heilmeier.Q8
      - google_impact_challenge.Q43
      - google_impact_challenge.Q44
      - google_impact_challenge.Q45
      - google_impact_challenge.Q46
      - google_impact_challenge.Q47
      - foresight_nodes.F18
      - doe_genesis.narrative_5
      - arpah_mission_office.tech_mgmt_proposal
  - id: U08.3
    name: Negative signals / failure indicators
    max_words: 250
    max_chars: null
    funder_hooks:
      - heilmeier.Q8
      - google_impact_challenge.Q19b
      - brains_accelerator.B6
      - arpah_mission_office.appendix_a_5
  - id: U08.4
    name: Baseline vs. expected change
    max_words: 250
    max_chars: null
    funder_hooks:
      - heilmeier.Q8
      - google_impact_challenge.Q19c
      - arpah_mission_office.appendix_a_3
cytognosis_anchor: "Quantitative success metrics keyed to OKRs; 4×/100×-style targets; go/no-go gates at H1→H2 and H2→H3 transitions"
last_reviewed: 2026-04-23
owner: mohammadi@cytognosis.org
status: stub
---

# U08 — Mid-term & final exams (quantitative go/no-go)

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: grant team
> **Tags**: `funding`, `reusable-slot`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

## U08.1 — Quantitative success metrics

Success metrics are authored as numeric, ambitious targets tied to OKRs — the kind of 4×/100× framing a reviewer can cite without re-reading the proposal. Each metric ties to a layer of the platform (Cytoverse coverage in cell-states catalogued; Cytoscope sensitivity in detectable perturbations per sample; Cytonome latency and accuracy per on-device inference) and has a stated baseline so year-over-year progress is falsifiable.

## U08.2 — Go/no-go decision gates per phase

Each Horizon transition (H1→H2, H2→H3) has an explicit go/no-go gate built from the metrics in U08.1. The gate is passed only when the quantitative target is hit and the downstream prerequisite — IRB enrollment, partner commitment, or regulatory pathway — is in place. Failing a gate triggers the U03.5 fallback rather than a silent slip.

## U08.3 — Negative signals / failure indicators

Named early-warning indicators: cell-state-catalog growth stalling below annual target, Cytonome false-positive rate above clinical tolerance, or pilot-site attrition exceeding a defined threshold. Each is paired with the monitoring cadence (quarterly) and the mitigation that would be triggered.

## U08.4 — Baseline vs. expected change

Every metric is stated as a baseline (today, measured) and an expected end-of-phase value. This prevents the proposal from claiming "improvement" without a denominator, and lets funders calibrate ambition across the moderate and ambitious budget tiers.
