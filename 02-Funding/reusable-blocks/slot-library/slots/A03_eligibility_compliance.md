---
slot_id: A03
slot_name: Eligibility & compliance
required_by:
  - arpah_mission_office
  - doe_genesis
  - google_impact_challenge
  - yc_nonprofit
useful_for:
  - nih_r01
  - nsf_tech_labs
  - astera_residency
  - brains_accelerator
  - foresight_nodes
sub_slots:
  - id: A03.1
    name: Government ties / foreign influence disclosures
    max_words: 200
    max_chars: null
    funder_hooks:
      - google_impact_challenge.Q48
      - google_impact_challenge.Q49
      - google_impact_challenge.Q50
      - yc_nonprofit.YC33
      - yc_nonprofit.YC34
      - doe_genesis.compliance
      - arpah_mission_office.cost_proposal
  - id: A03.2
    name: Sanctioned-country dealings
    max_words: 150
    max_chars: null
    funder_hooks:
      - google_impact_challenge.Q51
      - google_impact_challenge.Q52
      - yc_nonprofit.YC35
      - yc_nonprofit.YC36
  - id: A03.3
    name: Prior SBIR / federal funding history
    max_words: 200
    max_chars: null
    funder_hooks:
      - google_impact_challenge.Q53
      - doe_genesis.current_and_pending
  - id: A03.4
    name: Research security posture
    max_words: 200
    max_chars: null
    funder_hooks:
      - arpah_mission_office.cost_proposal
      - doe_genesis.compliance
cytognosis_anchor: "Compliance disclosures — no foreign-influence conflicts; research-security attestations per solicitation"
last_reviewed: 2026-04-23
owner: mohammadi@cytognosis.org
status: stub
---

# A03 — Eligibility & compliance

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: grant team
> **Tags**: `funding`, `reusable-slot`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

## A03.1 — Government ties / foreign influence disclosures

<!-- STUB: fill with Cytognosis canonical content. See cytognosis_anchor. -->

## A03.2 — Sanctioned-country dealings

<!-- STUB: fill with Cytognosis canonical content. See cytognosis_anchor. -->

## A03.3 — Prior SBIR / federal funding history

<!-- STUB: fill with Cytognosis canonical content. See cytognosis_anchor. -->

## A03.4 — Research security posture

<!-- STUB: fill with Cytognosis canonical content. See cytognosis_anchor. -->
