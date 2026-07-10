---
slot_id: U22
slot_name: Theory of change
heilmeier_parent: null
required_by:
  - drk_foundation
  - rwjf
  - ea_long_term_future_fund
  - ea_infrastructure_fund
  - coefficient_giving
  - astrazeneca_change
useful_for:
  - gates_grand_challenges
  - czi
  - fast_forward
  - foresight_nodes
  - brains_accelerator
  - convergent_research_fro
sub_slots:
  - id: U22.1
    name: Causal chain (problem → activities → outputs → outcomes → impact)
    max_words: 350
    max_chars: null
    funder_hooks:
      - drk_foundation.theory_of_change_q
      - rwjf.theory_of_change_q
      - coefficient_giving.theory_of_change_q
      - astrazeneca_change.theory_of_change_q
  - id: U22.2
    name: Assumptions and risks per link
    max_words: 250
    max_chars: null
    funder_hooks:
      - drk_foundation.theory_of_change_q
      - rwjf.assumptions_q
      - ea_long_term_future_fund.application_q
  - id: U22.3
    name: Evidence base for each causal link
    max_words: 200
    max_chars: null
    funder_hooks:
      - rwjf.evidence_q
      - coefficient_giving.evidence_q
      - drk_foundation.theory_of_change_q
  - id: U22.4
    name: Indicators of progress along the chain
    max_words: 150
    max_chars: null
    funder_hooks:
      - drk_foundation.measurement_q
      - rwjf.indicators_q
cytognosis_anchor: "GPS for Health causal chain: cellular-resolution measurement at scale (Cytoscope) → computable atlas of cellular state (Cytoverse) → personalized edge-AI navigation (Cytonome) → earlier intervention windows → reduced disease burden, lower lifetime cost of care, increased healthspan."
last_reviewed: 2026-04-25
owner: mohammadi@cytognosis.org
status: stub
added_in: "1.1"
---

# U22 — Theory of change

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: grant team
> **Tags**: `funding`, `reusable-slot`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

## U22.1 — Causal chain

<!-- STUB: 1-2 paragraphs walking the standard ToC chain: problem statement → key activities → near-term outputs → medium-term outcomes → long-term impact. For Cytognosis, follows the GPS-for-Health chain noted in cytognosis_anchor. -->

## U22.2 — Assumptions and risks per link

<!-- STUB: For each link in the causal chain, name the assumption(s) it depends on and the risk(s) that would break the link. Keep concrete. -->

## U22.3 — Evidence base for each causal link

<!-- STUB: For each causal link, cite the evidence (literature, prior work, pilot data, analogous successes) that makes the link credible. Empty for links that are speculative — flag them. -->

## U22.4 — Indicators of progress along the chain

<!-- STUB: Leading and lagging indicators tied to each outcome. Should align with U08 (exams) but framed at the outcome/impact level rather than at the technical-milestone level. -->
