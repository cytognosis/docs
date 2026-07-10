---
slot_id: A01
slot_name: Organizational identity
required_by:
  - nih_r01
  - nsf_tech_labs
  - arpah_mission_office
  - doe_genesis
  - astera_residency
  - brains_accelerator
  - foresight_nodes
  - google_impact_challenge
  - yc_nonprofit
sub_slots:
  - id: A01.1
    name: Legal name, EIN, classification
    max_words: 100
    max_chars: null
    funder_hooks:
      - google_impact_challenge.Q1
      - google_impact_challenge.Q2
      - google_impact_challenge.Q3
      - yc_nonprofit.YC14
      - yc_nonprofit.YC15
      - yc_nonprofit.YC33
      - yc_nonprofit.YC34
      - yc_nonprofit.YC35
      - yc_nonprofit.YC36
      - foresight_nodes.F3
      - doe_genesis.sf424
      - nsf_tech_labs.Q1
  - id: A01.2
    name: Year founded, budget, FTE
    max_words: 100
    max_chars: null
    funder_hooks:
      - google_impact_challenge.Q4
      - google_impact_challenge.Q5
      - foresight_nodes.F5
      - foresight_nodes.F6
  - id: A01.3
    name: Website, socials, public presence
    max_words: 80
    max_chars: null
    funder_hooks:
      - google_impact_challenge.Q6
      - foresight_nodes.F7
      - foresight_nodes.F8
cytognosis_anchor: "Cytognosis Foundation 501(c)(3); EIN and admin metadata in ops doc"
last_reviewed: 2026-04-23
owner: mohammadi@cytognosis.org
status: stub
---

# A01 — Organizational identity

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: grant team
> **Tags**: `funding`, `reusable-slot`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

## A01.1 — Legal name, EIN, classification

<!-- STUB: fill with Cytognosis canonical content. See cytognosis_anchor. -->

## A01.2 — Year founded, budget, FTE

<!-- STUB: fill with Cytognosis canonical content. See cytognosis_anchor. -->

## A01.3 — Website, socials, public presence

<!-- STUB: fill with Cytognosis canonical content. See cytognosis_anchor. -->
