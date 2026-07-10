# Monday Board Update Plan — Strategic Planning + Funding Opportunities

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: grant team
> **Tags**: `funding`, `slot-library`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

**Status:** Plan only — no Monday writes yet (per user instruction). This document is the playbook for the next implementation pass.
**Authored:** 2026-04-25
**Scope:** Two folders in Main workspace (id `14426768`):
1. `Strategic Planning` (folder id `20228556`) — exposes the universal slot taxonomy as columns/items so strategy items reuse the canonical schema.
2. `Fundraising` (folder id `20229240`) — adds columns for F12–F30 metadata + canonical slot mappings derived from `opportunity_mapping.yaml`.

---

## Part 1 — Strategic Planning folder

### Current state (read-only inventory)

| Board | ID | Items | Key columns | What it currently models |
|---|---|---:|---|---|
| Strategic Objectives | `18409731707` | 14 | SO ID, Horizon (H1/H2/H3), Pillars (P1–P6), Meta-tracks (M1–M5), Subtracks (T1–T16), Status, Owner, Description, Goals link, Initiatives link, Grants link, Risks link, VMV link, Horizon link, Tracks link | OGSM Objectives per horizon, linked downstream |
| Tracks | `18409731706` | 19 | Level (Meta/Sub), Meta-track, Parent, Scope, Owner, H1/H2/H3 weight, Primary Pillar, Linked Resources | 4 meta-tracks (M1–M4) + 16 subtracks (T1–T16); the strategy taxonomy itself |
| Horizons & Gates | `18409731703` | tbd | (not read in detail) | Three Horizons + gate criteria |
| Vision, Mission, Values | `18409731701` | tbd | (not read in detail) | VMV statements, possibly anchor for U01.1 |
| Values | `18409744381` | tbd | (not read in detail) | Brand/value archetypes — referenced by Funding Opportunities `Aligned Values` column |
| Strategic Goals | `18409731710` | tbd | (not read in detail) | Goals downstream of Objectives |
| Strategic Initiatives | `18409731713` | tbd | (not read in detail) | Initiatives downstream of Goals |
| Milestones Roadmap | `18409731715` | tbd | (not read in detail) | Cross-track milestones |
| KPIs | `18409731717` | tbd | (not read in detail) | Quarter-keyed measures |
| Risks Register | `18409731742` | tbd | (not read in detail) | Risks linked to Objectives |

### Gap (what the canonical schema adds that Strategic Planning does not yet expose)

The canonical template defines **universal slots** (U01–U22, A01–A05) — content categories that every grant/proposal/pitch needs. Today the Strategic Planning boards organize **strategic items** (objectives, goals, initiatives) but don't tag *which canonical slot they feed*. Result: when authoring a proposal, an author has to manually look up which strategic items contain the content for, say, U03 Novelty or U18 Translation. The mapping is implicit.

### Proposal: add a "Canonical Slot" column to the strategic boards

Three boards get a new dropdown_multi column listing the universal slot IDs that this item populates content for. Stable IDs match `canonical/manifest.yaml`.

**Boards to modify:**

| Board | New column | Type | Allow multi | Default | Purpose |
|---|---|---|---|---|---|
| Strategic Objectives | `Canonical Slots` | dropdown_multi | yes | empty | Mark which U/A slots this objective generates content for. |
| Strategic Initiatives | `Canonical Slots` | dropdown_multi | yes | empty | Same for initiatives. |
| Milestones Roadmap | `Canonical Slots` | dropdown_multi | yes | empty | Marks milestone evidence as feed-stock for U08 Exams. |
| Risks Register | `Canonical Slots` | dropdown_multi | yes | empty | Links risks to U05 Risks (and sometimes U14, U16). |
| KPIs | `Canonical Slots` | dropdown_multi | yes | empty | Links KPIs to U08 Exams; some to U04 Stakes (impact KPIs). |
| Strategic Goals | `Canonical Slots` | dropdown_multi | yes | empty | Same pattern. |

**Dropdown labels:** all 27 slot IDs as labels — `U01 Objective`, `U02 SOTA & limits`, `U03 Novelty & approach`, `U04 Stakes`, `U05 Risks`, `U06 Cost`, `U07 Schedule`, `U08 Exams`, `U09 Opportunity-space`, `U10 Why-not-academia/VC`, `U11 Team`, `U12 Open science`, `U13 Equity / access`, `U14 Responsible AI`, `U15 IP & data`, `U16 Regulatory / biosecurity`, `U17 Adoption / transition`, `U18 Translation-to-Mission`, `U19 Sustainability`, `U20 Partnerships`, `U21 Counterfactual`, `U22 Theory of change`, `A01 Org identity`, `A02 POC`, `A03 Eligibility`, `A04 Artifacts`, `A05 Intake meta`.

**Migration:** for each existing strategic item, populate `Canonical Slots` based on the item's content. Suggested heuristics:
- Strategic Objective text mentions "platform" or "Cytoverse/Cytoscope/Cytonome" → tag U03, U17, U18.
- Strategic Objective in Meta-track M2 Translation → tag U17, U18, U20.
- Strategic Objective in Meta-track M3 Organization → tag U10, U11.6, U19.2.
- Risk in Risks Register → tag U05; if AI-specific tag U14; if regulatory tag U16.
- KPI quantitative target → tag U08; if impact metric tag U04.

The migration is a one-time tagging pass; once tagged, the Strategic Planning boards become a queryable knowledge base that the canonical template render pipeline can pull from.

### Proposal: add a "Slot Coverage" mirror item per slot (optional, deferred)

Out-of-scope for this pass but worth flagging: a separate board (or `root_items` list) called `Slot Coverage` with one item per universal slot. Each item shows:
- Slot ID + name
- Status (`stub`, `draft`, `reviewed`, `approved`)
- Authoring owner
- Cross-link to all Strategic Objectives / Initiatives / KPIs that feed it

This board mirrors `canonical/slots/` and gives a Monday-side view of slot completion. **Defer to v1.2** — not needed for the current pass.

### Migration cadence

1. **Phase 1 (this implementation pass):** add the `Canonical Slots` column to 6 strategic boards. No data backfill yet.
2. **Phase 2 (one focused session):** backfill the column for all existing items using the heuristics above. ~50 items total across 6 boards.
3. **Phase 3 (continuous):** when authoring new strategic items, set the column at creation time.

---

## Part 2 — Fundraising / Funding Opportunities board (id 18409744388)

### Current state

71 items, 26 columns. Columns already aligned with the inventory's F01–F11 (Funding Category, Maturity Stage, Priority, Status, Funding Source, Funding Type/Subtype, Focus Areas, Amount Min/Max/Typical, Deadline, Deadline Type, Eligibility, Mission Alignment, Initial Submission Format).

### Gap (what's missing relative to canonical schema v1.1)

The board does not yet model:
1. **Funder Kind** (canonical `funder_kinds` registry — 13 values) — needed to drive proposal-rendering subset selection.
2. **F12–F30 funder-metadata fields** — instrument, submission stages, application effort, indirect-cost rule, residency, etc.
3. **Canonical Slot Mapping** — which U/A slots each opportunity requires content for.
4. **Canonical Funder File Reference** — pointer to `canonical/funders/<id>.yaml` when one exists.

### Proposal: add 22 columns to Funding Opportunities

Order them after the existing F01–F11 block, before `Strategic Advantages`.

| F-id / purpose | Column title | Type | Settings / values | Source for default |
|---|---|---|---|---|
| Funder Kind | `Funder Kind` | status | 13 labels: universal_baseline, federal_grant, federal_OT, intergovernmental_grant, private_grant, philanthropic_grant_proactive, ea_micro_grant, private_fellowship, accelerator, vc_investment, venture_builder, corporate_credit, nonprofit_discount | from `opportunity_mapping.yaml` |
| F12 | `Instrument` | status | grant, investment, credits, discount, in-kind, fellowship, hybrid, TBD-at-closing | F12 |
| F13 | `Submission Stages` | dropdown_multi | full, LOI, concept, abstract, summary, round1, round2, invitation_only | F13 |
| F14 | `Application Effort` | status | light (≤2h), medium (≤20h), heavy (>20h) | F14 |
| F15 | `Investment Horizon (yrs)` | numbers | int; null for non-VC | F15 |
| F16 | `Application Required` | status | yes, verification_only, no, invitation_only | F16 |
| F17 | `Cost Share Required` | text | "false" or "X%" or "true" | F17 |
| F18 | `Indirect Cost Rule` | status | flat_15pct, flat_10pct, flat_25pct, capped_negotiated, fEC, F&A_negotiated, OT_negotiated, direct_only, uncapped, n/a | F18 |
| F19 | `Award Period (mo)` | numbers | int | F19 |
| F20 | `Joint Program Partners` | text | semicolon-separated org names | F20 |
| F21 | `Funder Process Type` | status | proactive, reactive, hybrid | F21 |
| F22 | `Canonical Funder File` | text | filename of `canonical/funders/<id>.yaml` or empty | F22 |
| F25 | `Residency Required` | checkbox | true/false | F25 |
| F26 | `Residency Location` | text | city/region | F26 |
| F27 | `Confidentiality Policy` | status | standard, no_confidential_ip, nda_required | F27 |
| F28 | `Written Feedback Gate` | checkbox | true/false | F28 |
| F29 | `Review Criteria` | long_text | bulleted list, one criterion per line | F29 |
| F30 | `Required Partners Count` | numbers | int (consortium minimum) | F30 |
| Slots | `Required Slots` | dropdown_multi | 27 labels (U01–U22 + A01–A05) | from `required_slots` in mapping yaml |
| Sub-slots | `Required Sub-slots` | text | semicolon-separated sub-slot IDs | from `required_sub_slots` |
| Useful slots | `Useful Slots` | dropdown_multi | 27 labels (same as Required Slots) | from `useful_slots` |
| Notes | `Submission Notes` | long_text | one paragraph guidance | from `submission_notes` |

**Why these column types:**
- `status` (single-select) is best for closed enums where only one value applies (Instrument, Application Effort, Funder Process, Indirect Cost Rule).
- `dropdown_multi` for many-from-list (Required Slots, Useful Slots, Submission Stages, Joint Program Partners if we materialize them).
- `text` for free-form strings that vary too much for an enum (Joint Program Partners written as semicolon list, Canonical Funder File as filename).
- `long_text` for narrative (Review Criteria, Submission Notes).
- `numbers` for integers (Award Period, Investment Horizon).
- `checkbox` for booleans (Residency Required, Written Feedback Gate).

### Migration playbook (later session, not this one)

Once the columns exist, populate from `opportunity_mapping.csv` (also produced in this session). The CSV has one row per Monday item (joinable on `monday_id`), one column per F-field, plus the slot-mapping columns. A Monday `change_item_column_values` call per row, or a bulk import via Monday's CSV importer, fills the board.

**Sequence:**
1. Add the 22 new columns. Do NOT delete any existing columns.
2. For each of the 71 items, look up the row in `opportunity_mapping.csv` by `monday_id`.
3. Set each column from the matching CSV column. Empty/null values are left blank.
4. Verify by spot-checking 5 items across different `funder_kind` values.

### Lightweight subset rule

For `funder_kind: nonprofit_discount` items (~20 of 71), don't populate F13–F30 deeply. The minimum viable record is:
- F12 Instrument: `discount`
- F14 Application Effort: `light`
- F16 Application Required: `verification_only`
- F03 Pipeline Status: `Approved / Granted` for those already onboarded

Same applies to `funder_kind: corporate_credit` items.

For `funder_kind: federal_OT` and `federal_grant` items, populate every F-field that has a value — these are the schema-stretching ones.

---

## Part 3 — Cross-board joins (Grants Pipeline ↔ Funding Opportunities)

The Funding Opportunities board has a `Grants Pipeline` board_relation already. Three additional cross-links are useful but deferred to v1.2:

1. **Funding Opportunities → Strategic Initiatives** (board_relation) — when the team commits to applying, link the opportunity to the strategic initiative(s) the proposal advances.
2. **Strategic Objectives → Funding Opportunities** (board_relation) — reverse lookup: which opportunities are aligned with each objective. Useful for portfolio review meetings.
3. **Risks Register → Funding Opportunities** (board_relation) — fundraising risks (e.g., "ARPA-H delay risks H1 timeline") get linked to the upstream opportunity item.

These board_relations sharpen the strategy → opportunity → grant pipeline pull-through. Not needed to land v1.1.

---

## Part 4 — Sequencing (when to actually update Monday)

1. **Now:** review this plan, decide which columns / boards to land first.
2. **Implementation pass A — Strategic Planning columns** (lowest risk; only adds columns to existing boards, no data migration required immediately): add `Canonical Slots` to the 6 strategic boards.
3. **Implementation pass B — Funding Opportunities columns** (medium risk; 22 new columns): add the F12–F30 + slot-mapping columns. Existing F01–F11 columns unchanged.
4. **Implementation pass C — Backfill data** (highest risk; many writes; one item at a time): use `opportunity_mapping.csv` to populate the new columns for all 71 items. Optionally do a single `funder_kind` batch first (e.g., `nonprofit_discount`) to validate the pipeline.
5. **Implementation pass D — Strategic items backfill**: tag existing Objectives / Initiatives / KPIs / Risks with their `Canonical Slots`.
6. **Implementation pass E (optional, v1.2)** — cross-board relations between Strategic and Fundraising.

Each pass is its own Cowork session — none should be combined.

---

## Part 5 — Risk register for this plan

| Risk | Probability | Severity | Mitigation |
|---|:-:|:-:|---|
| Column-type choice (`status` vs `dropdown_multi`) needs revisiting | M | L | Easy to change before backfill; agree the types before pass A. |
| F-family enum values drift from canonical | L | M | Validation rule in `manifest.yaml` (`funder_metadata_id: ^F\d{2}$`); regenerate mapping CSV from manifest, not from Monday. |
| Backfill collides with manual edits in Funding Opportunities | M | M | Snapshot the board (CSV export) immediately before pass C; resolve conflicts manually. |
| `Canonical Slots` column on Strategic Objectives confuses users (looks like a workflow status) | M | L | Set the column description clearly and don't add it as a default group_by. |
| Canonical schema bumps to v1.2 invalidate column enums | M | L | Version-stamp columns: prefix labels with `v1.1` to make a future migration explicit. |
| Joint funders (e.g., Microsoft + NVIDIA) have ambiguous `Funder Kind` | L | L | Add `joint_program_partners` (F20) as a list; pick the dominant kind for `Funder Kind`. |

---

## Part 6 — Validation (run before each implementation pass)

A pre-flight check for each Monday update:

1. The columns being added have stable IDs (`column_id`) recorded in `monday_column_map.yaml` (write this file in pass A and update with each new column).
2. Every label in a `status` column has an explicit `id` (Monday assigns one when the label is created).
3. The `dropdown_multi` columns have all 27 slot labels (or 30 F-field labels) present.
4. `opportunity_mapping.csv`'s columns line up with the new Monday columns (column-name match or explicit alias map).
5. A dry-run: pick one opportunity (e.g., Astera Residency, since we have a real funder file and rich profile), populate manually, render the resulting Monday item to check the data shape.

Once validation passes, commit the column-add to all 71 items in a single batch.

---

*Authored 2026-04-25. Companion to `manifest.yaml` (v1.1), `opportunity_mapping.yaml`, and `opportunity_mapping.csv`.*
