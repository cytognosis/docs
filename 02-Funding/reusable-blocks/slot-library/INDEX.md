# Cytognosis Canonical Template System — Master Index

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: grant team
> **Tags**: `funding`, `slot-library`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

**Status:** Draft (under `_draft/canonical/` until promoted to `01_framework/` root).
**Schema version:** 1.1 (2026-04-25)
**Maintainer:** mohammadi@cytognosis.org

This is the orientation map. It points to every artifact in the canonical system, its purpose, and what to read next.

---

## What this system does

One source-of-truth for every Cytognosis grant, application, white paper, LOI, pitch, or proposal. Content is authored once per **slot** (stable IDs `U01`–`U22` + `A01`–`A05`), and the same content is rendered into any funder's required shape by selecting slots, applying length limits, and reordering sections. Funder-opportunity metadata (instrument, deadline, indirect-cost rules, etc.) lives in the `F01`–`F30` family on funder files and on the Monday `Funding Opportunities` board.

Primary output target: **Google Workspace** (Docs / Sheets / Slides via API). Local DOCX/XLSX is generated only when a funder requires their specific template.

---

## Read me first

- **What's here:** [`README.md`](./README.md) — quick orientation, directory layout, content status.
- **What changed in v1.1:** [`CHANGELOG.md`](./CHANGELOG.md) — F-family registry, U21/U22, 8 new funder kinds, 30+ deferred sub-slots.
- **The spec:** [`../canonical_template_format.md`](../canonical_template_format.md) — file format invariants, YAML schema, ID conventions.
- **Slot definitions (human-readable):** [`../universal_template.md`](../universal_template.md) — Part C has per-funder Q→slot mappings.

## Manifest and slot files

- **Manifest:** [`manifest.yaml`](./manifest.yaml) — authoritative slot registry (U01–U22 + A01–A05 = 27 slots), funder registry (10 modeled), funder-kind registry (13 kinds), F-family fields (F01–F30), validation rules.
- **Slot files:** [`slots/`](./slots/) — 27 markdown files; each has YAML frontmatter + H2 per sub-slot.
  - U01–U08 Heilmeier core (U01 + U08 fully authored; U03 + U06 partial)
  - U09–U20 extensions (stubs)
  - U21 Counterfactual + U22 Theory of change (new in v1.1, stubs)
  - A01–A05 administrative (stubs)
- **Funder files:** [`funders/`](./funders/) — 10 yaml files (heilmeier, nih_r01, nsf_tech_labs, arpah_mission_office, doe_genesis, astera_residency, brains_accelerator, foresight_nodes, google_impact_challenge, yc_nonprofit). 15 more proposed in CHANGELOG for v1.2.

## Funder crosswalk

- **[`../funder_crosswalk_matrix.md`](../funder_crosswalk_matrix.md)** — slot × funder matrix + per-funder reverse lookup. Authoritative mapping.

## Format conversion

- **[`../format_conversion_decision_tree.md`](../format_conversion_decision_tree.md)** — for each input or output format, which tool to use. Active reference.
- **[`../templating_stack_v2.md`](../templating_stack_v2.md)** — SHELVED full evaluation. Read only for rationale.

---

## Funding-opportunity research (v1.1 driver)

The canonical schema was extended to v1.1 based on research of all 71 funding opportunities tracked in Monday `Fundraising → Funding Opportunities` (board id `18409744388`).

| Artifact | Purpose |
|---|---|
| [`research/funding_opps_inventory.md`](./research/funding_opps_inventory.md) | Master list of 71 opportunities pulled from Monday with key columns (URL, deadline, amount, focus areas). |
| [`research/profiles/`](./research/profiles/) | 71 per-opportunity Markdown profiles: eligibility, funding range, submission shape, required artifacts, schema gaps. |
| [`research/research_summary.md`](./research/research_summary.md) | Aggregated schema gaps (57+ deduplicated) with proposed schema additions. The driver of the v1.0 → v1.1 bump. |

## Per-opportunity canonical mapping (v1.1 deliverable)

| Artifact | Format | Use |
|---|---|---|
| [`opportunity_mapping.yaml`](./opportunity_mapping.yaml) | YAML | 71 opportunity blocks; each has all 30 F-fields, required/useful slot lists, sub-slot specifics, submission notes. Source-of-truth for board population. |
| [`opportunity_mapping.csv`](./opportunity_mapping.csv) | CSV | Flat tabular form of the YAML. One row per Monday item, columns aligned to proposed Monday columns. Loadable via Monday CSV import or `change_item_column_values` API calls. |
| [`opportunity_mapping_index.md`](./opportunity_mapping_index.md) | Markdown | Reader's index grouped by `funder_kind`, with deadlines, amounts, slugs, and load-bearing-slot summaries. |

## Monday-board update plan

- **[`monday_update_plan.md`](./monday_update_plan.md)** — playbook for adding canonical-slot columns to Strategic Planning boards and F12–F30 + slot-mapping columns to the Funding Opportunities board. Five sequenced implementation passes; no Monday writes yet.

---

## Quick metrics

| Dimension | Count |
|---|---|
| Universal slots | 22 (U01–U22) |
| Administrative slots | 5 (A01–A05) |
| Total slot files | 27 |
| Funder files (canonical) | 10 |
| Funder kinds | 13 |
| F-family metadata fields | 30 (F01–F30) |
| Funding opportunities researched | 71 (67 full + 4 partial + 0 failed) |
| Opportunity profile pages | 71 |
| Per-opportunity slot citations | ~620 |
| Per-opportunity sub-slot citations | ~110 |
| Per-opportunity useful-slot citations | ~330 |
| Existing Monday columns matched (F01–F11) | 11 |
| New Monday columns proposed (F12–F30 + 4 slot/notes columns) | 22 |
| Strategic boards proposed to gain `Canonical Slots` column | 6 |

## Coverage breakdown

| Funder kind | Count of opportunities | Canonical subset | Status |
|---|:-:|:-:|---|
| federal_grant | 5 | heavy | Mapped, 1 funder file (nih_r01) |
| federal_OT | 4 | heavy | Mapped, 3 funder files (nsf_tech_labs, arpah_mission_office, doe_genesis) |
| intergovernmental_grant | 2 | heavy | Mapped, 0 funder files (Horizon Europe, UNESCO/WHO needed) |
| private_grant | 5 | heavy | Mapped, 1 funder file (google_impact_challenge) |
| philanthropic_grant_proactive | 6 | heavy | Mapped, 0 funder files |
| ea_micro_grant | 3 | medium | Mapped, 0 funder files |
| private_fellowship | 3 | heavy | Mapped, 3 funder files (astera_residency, brains_accelerator, foresight_nodes) |
| accelerator | 6 | medium | Mapped, 1 funder file (yc_nonprofit) |
| vc_investment | 7 | medium | Mapped, 0 funder files |
| venture_builder | 3 | medium | Mapped, 0 funder files |
| corporate_credit | 7 | light | Mapped, 0 funder files (shared template recommended) |
| nonprofit_discount | 20 | light | Mapped, 0 funder files (shared template recommended) |

(Counts are approximate from `opportunity_mapping_index.md`.)

---

## How to use this system

### "I'm authoring a new proposal — where do I start?"
1. Find the opportunity in `opportunity_mapping_index.md`. Note its `slug` and `required_slots`.
2. Read the corresponding `funders/<id>.yaml` if it exists; otherwise use `manifest.yaml` `funder_kinds.<kind>` to pick the right subset.
3. Edit the slot files in `slots/` that the opportunity requires. Author once; the same content fills every funder that needs that slot.
4. Render via the pipeline (deferred — Google Docs renderer is paused).

### "I want to add a new funding opportunity to the system"
1. Add it to the Monday `Funding Opportunities` board (the source-of-truth for the inventory).
2. Append a profile under `research/profiles/<slug>.md`.
3. Add a row to `opportunity_mapping.yaml` and `opportunity_mapping.csv`.
4. If it requires content not covered by U01–U22 + A01–A05, file a CHANGELOG candidate for v1.2.

### "I want to update Monday boards to reflect this schema"
1. Read [`monday_update_plan.md`](./monday_update_plan.md). Five sequenced passes.
2. Run validation (Part 6 of the plan) before each pass.
3. Do one pass per Cowork session; never combine.

### "I want to extend the schema"
1. Open a CHANGELOG entry for the proposed bump (e.g., 1.1 → 1.2).
2. Update `manifest.yaml` for new IDs.
3. If adding a slot, write the slot file in `slots/`.
4. If adding a funder, write the funder file in `funders/`.
5. If adding an F-family field, update `funder_metadata_fields:` in the manifest and the Monday plan.
6. Re-run verification (slot ↔ frontmatter parity, funder `required_by` consistency).

---

## What's NOT here (yet)

- **Slot-file prose** for U02, U04–U07 (partial), U09–U22, A01–A05 — most are STUBs. Authoring is the next major work after promotion.
- **Validators** — Python scripts in `lib/validators/` to enforce manifest ↔ funder-yaml ↔ slot-file consistency.
- **Renderers** — currently paused per user instruction. Google Docs renderer is the v1.2 deliverable.
- **15 new canonical funder files** — listed in CHANGELOG; build on demand as proposals are scheduled.
- **Lightweight templates** for `corporate_credit` and `nonprofit_discount` shared across ~27 opportunities each.

---

## File map (truncated)

```
_draft/canonical/
├── INDEX.md                       (this file)
├── README.md
├── CHANGELOG.md
├── manifest.yaml                  (v1.1, F-family + U21/U22 + 13 funder kinds)
├── opportunity_mapping.yaml       (71 opportunities × 30 F-fields + slot lists)
├── opportunity_mapping.csv        (loadable into Monday)
├── opportunity_mapping_index.md   (reader's view by funder kind)
├── monday_update_plan.md          (5-pass implementation plan)
├── slots/
│   ├── U01_objective.md ... U22_theory_of_change.md   (22 universal slots)
│   └── A01_org_identity.md ... A05_intake_meta.md     (5 administrative slots)
├── funders/
│   ├── heilmeier.yaml             (universal baseline)
│   ├── nih_r01.yaml
│   ├── nsf_tech_labs.yaml
│   ├── arpah_mission_office.yaml
│   ├── doe_genesis.yaml
│   ├── astera_residency.yaml
│   ├── brains_accelerator.yaml
│   ├── foresight_nodes.yaml
│   ├── google_impact_challenge.yaml
│   └── yc_nonprofit.yaml          (10 / ~25 needed)
├── research/
│   ├── funding_opps_inventory.md  (71 opportunities, Monday-pull)
│   ├── research_summary.md        (gap analysis driving v1.1)
│   └── profiles/
│       ├── aria-uk-full-programmes.md
│       └── ... 70 more profiles ...
└── lib/
    ├── macros/                    (Jinja macros — not yet written)
    └── validators/                (Python validators — not yet written)
```

---

*Authored 2026-04-25. Companion to `manifest.yaml` v1.1.*
