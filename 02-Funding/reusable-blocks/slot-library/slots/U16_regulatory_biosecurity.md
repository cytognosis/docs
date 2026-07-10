---
slot_id: U16
slot_name: Regulatory, dual-use & biosecurity
required_by:
  - arpah_mission_office
  - doe_genesis
  - yc_nonprofit
useful_for:
  - nih_r01
  - astera_residency
  - brains_accelerator
  - foresight_nodes
  - google_impact_challenge
  - nsf_tech_labs
sub_slots:
  - id: U16.1
    name: FDA / SaMD / IVD pathway
    max_words: 300
    max_chars: null
    funder_hooks:
      - yc_nonprofit.YC31
      - arpah_mission_office.appendix_a_5
  - id: U16.2
    name: IRB / human subjects plan
    max_words: 250
    max_chars: null
    funder_hooks:
      - arpah_mission_office.cost_proposal
      - doe_genesis.compliance
  - id: U16.3
    name: Animal use / IACUC
    max_words: 150
    max_chars: null
    funder_hooks:
      - arpah_mission_office.cost_proposal
      - doe_genesis.compliance
  - id: U16.4
    name: Dual-use research of concern
    max_words: 250
    max_chars: null
    funder_hooks:
      - arpah_mission_office.tdd
      - doe_genesis.compliance
  - id: U16.5
    name: Biosecurity screening
    max_words: 200
    max_chars: null
    funder_hooks:
      - arpah_mission_office.tdd
      - doe_genesis.compliance
  - id: U16.6
    name: Ethics self-assessment
    max_words: 200
    max_chars: null
    funder_hooks:
      - arpah_mission_office.appendix_a_5
      - doe_genesis.compliance
cytognosis_anchor: "SaMD/IVD pathway per clinical axis · IRB partners · DURC review posture"
last_reviewed: 2026-04-23
owner: mohammadi@cytognosis.org
status: stub
---

# U16 — Regulatory, dual-use & biosecurity

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: grant team
> **Tags**: `funding`, `reusable-slot`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

## U16.1 — FDA / SaMD / IVD pathway

<!-- STUB: fill with Cytognosis canonical content. See cytognosis_anchor. -->

## U16.2 — IRB / human subjects plan

<!-- STUB: fill with Cytognosis canonical content. See cytognosis_anchor. -->

## U16.3 — Animal use / IACUC

<!-- STUB: fill with Cytognosis canonical content. See cytognosis_anchor. -->

## U16.4 — Dual-use research of concern

<!-- STUB: fill with Cytognosis canonical content. See cytognosis_anchor. -->

## U16.5 — Biosecurity screening

<!-- STUB: fill with Cytognosis canonical content. See cytognosis_anchor. -->

## U16.6 — Ethics self-assessment

<!-- STUB: fill with Cytognosis canonical content. See cytognosis_anchor. -->
