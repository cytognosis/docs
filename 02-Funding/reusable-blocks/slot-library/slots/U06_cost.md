---
slot_id: U06
slot_name: Cost
heilmeier_parent: Q6
required_by:
  - heilmeier
  - nih_r01
  - nsf_tech_labs
  - arpah_mission_office
  - doe_genesis
  - astera_residency
  - foresight_nodes
  - google_impact_challenge
  - yc_nonprofit
useful_for:
  - brains_accelerator
sub_slots:
  - id: U06.1
    name: Total ask (USD) and period
    max_words: 80
    max_chars: null
    funder_hooks:
      - heilmeier.Q6
      - google_impact_challenge.Q37
      - foresight_nodes.F12
      - foresight_nodes.F27
      - nsf_tech_labs.Q4e
      - arpah_mission_office.cost_proposal
  - id: U06.2
    name: Budget categories
    max_words: 400
    max_chars: null
    funder_hooks:
      - heilmeier.Q6
      - google_impact_challenge.Q38
      - google_impact_challenge.Q39
      - google_impact_challenge.Q40
      - google_impact_challenge.Q41
      - google_impact_challenge.Q42
      - foresight_nodes.F21
      - foresight_nodes.F22
      - foresight_nodes.F23
      - foresight_nodes.F24
      - foresight_nodes.F25
      - foresight_nodes.F26
      - foresight_nodes.F28
      - foresight_nodes.F29
      - foresight_nodes.F32
      - foresight_nodes.F33
      - foresight_nodes.F34
      - astera_residency.Q2
      - arpah_mission_office.cost_proposal
      - doe_genesis.budget_justification
  - id: U06.3
    name: Per-category justification
    max_words: 600
    max_chars: null
    funder_hooks:
      - heilmeier.Q6
      - google_impact_challenge.Q38
      - google_impact_challenge.Q39
      - google_impact_challenge.Q40
      - google_impact_challenge.Q41
      - google_impact_challenge.Q42
      - foresight_nodes.F30
      - yc_nonprofit.YC31
      - arpah_mission_office.cost_proposal
      - doe_genesis.budget_justification
  - id: U06.4
    name: Cost share / matching funds
    max_words: 200
    max_chars: null
    funder_hooks:
      - heilmeier.Q6
      - doe_genesis.sf424
      - arpah_mission_office.cost_proposal
  - id: U06.5
    name: Phased / tiered budget
    max_words: 400
    max_chars: null
    funder_hooks:
      - heilmeier.Q6
      - foresight_nodes.F31
      - nsf_tech_labs.Q4e
      - yc_nonprofit.YC30
      - yc_nonprofit.YC26
cytognosis_anchor: "Total ask keyed to H1/H2/H3 phased budget; personnel + compute + wet-lab + partners; cost share via PBC Helix revenue reinvestment"
last_reviewed: 2026-04-23
owner: mohammadi@cytognosis.org
status: stub
---

# U06 — Cost

## U06.1 — Total ask (USD) and period

The program's total headline ask for the current cycle lives here, anchored to the Three Horizons roadmap so ambitious and moderate tiers stay comparable across funders. Numbers render from `data/<proposal>/budget.yaml` at author time; this slot holds the narrative framing and the USD band, not the line-items.

## U06.2 — Budget categories

<!-- STUB: fill with Cytognosis canonical content. See cytognosis_anchor. -->

## U06.3 — Per-category justification

<!-- STUB: fill with Cytognosis canonical content. See cytognosis_anchor. -->

## U06.4 — Cost share / matching funds

<!-- STUB: fill with Cytognosis canonical content. See cytognosis_anchor. -->

## U06.5 — Phased / tiered budget

Budget is structured in an ambitious/moderate pair so funders that ask for tiered options (Foresight F31, NSF Tech Labs Phase 0/1/2, YC YC30) can select cleanly. The ambitious tier funds parallel execution across all three Cytognosis layers (Cytoverse, Cytoscope, Cytonome); the moderate tier sequences Cytoverse first and defers wet-lab scale-up.
