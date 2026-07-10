# Canonical Template Format Specification

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: leadership, grant team
> **Tags**: `funding`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

**Status:** Authoritative. Defines the single source-of-truth format for every Cytognosis grant, application, proposal, white paper, LOI, and pitch.
**Version:** 1.0 (2026-04-23)
**Rationale:** One format, rendered many ways. Content is authored once and assembled into any funder's required shape by selecting slots, applying length limits, and reordering sections.

---

## 1. Design invariants

1. **Content is not funder-specific.** Every sentence lives under a stable slot ID (U01–U20, A01–A05). Funders are *sinks* that select, reorder, and trim — they do not own authored content.
2. **Plain-text-friendly.** The format is Markdown with YAML frontmatter so it is human-editable, git-diffable, grep-able, and LLM-readable without special tooling.
3. **Machine-addressable.** Every slot and sub-slot has a stable ID that can be referenced from a Jinja template, a Pydantic model, or a Google Docs API text-replace call.
4. **Schema-first.** Slot inventory, length limits, and funder mappings live in a separate manifest file, not inside prose. Authors cannot accidentally invalidate the structure by editing a slot body.
5. **Openness by default.** All metadata and crosswalks are YAML/Markdown so a non-Cytognosis reader can read, audit, and fork the structure without proprietary tooling.

---

## 2. Directory layout

```
templates/01_framework/
├── manifest.yaml                    # Slot inventory, metadata, authoritative schema
├── slots/                           # Canonical content, one file per slot
│   ├── U01_objective.md
│   ├── U02_sota_and_limits.md
│   ├── ...
│   ├── U20_partnerships.md
│   ├── A01_org_identity.md
│   ├── A02_points_of_contact.md
│   └── ...
├── funders/                         # How each funder selects/orders/limits slots
│   ├── nih_r01.yaml
│   ├── nsf_tech_labs.yaml
│   ├── arpah_mission_office.yaml
│   ├── doe_genesis.yaml
│   ├── astera_residency.yaml
│   ├── brains_accelerator.yaml
│   ├── foresight_nodes.yaml
│   ├── google_impact_challenge.yaml
│   ├── yc_nonprofit.yaml
│   └── heilmeier.yaml               # The universal baseline
├── renders/                         # Generated artifacts (git-ignored)
│   └── <funder>/<year>/<proposal-id>/
└── lib/                             # Reusable Jinja macros, utilities
    ├── macros/
    └── validators/
```

Everything under `slots/` and `funders/` is hand-authored source-of-truth. `renders/` is output only.

---

## 3. Slot file format

Every slot file has YAML frontmatter and a Markdown body. Example:

```markdown
---
slot_id: U01
slot_name: Objective, in plain language
heilmeier_parent: Q1
required_by:
  - heilmeier
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
  - id: U01.1
    name: Bold one-sentence thesis
    max_words: 30
    max_chars: 200
    funder_hooks: [heilmeier.Q1, astera.Q1, foresight.F15, yc.YC9]
  - id: U01.2
    name: Plain-language objective
    max_words: 150
    max_chars: null
    funder_hooks: [heilmeier.Q1, google.Q16a, arpah.appendix_a.1, doe.project_abstract]
  - id: U01.3
    name: Short tagline
    max_chars: 50
    funder_hooks: [yc.YC9]
  - id: U01.4
    name: Project title / company name
    max_chars: 120
    funder_hooks: [google.Q11, foresight.F14, yc.YC8, doe.title_page]
cytognosis_anchor: "GPS for Health — Cytoverse · Cytoscope · Cytonome"
last_reviewed: 2026-04-23
owner: mohammadi@cytognosis.org
status: draft            # draft | reviewed | approved | deprecated
---

# U01 — Objective, in plain language

## U01.1 — Bold one-sentence thesis

> Cytognosis is building GPS for Health: a cellular-intelligence platform that
> makes disease interception possible before symptoms appear.

## U01.2 — Plain-language objective

We are building the scientific platform and open tools that let physicians and
patients see the earliest signals of disease — at the level of individual cells —
and act on them years before a diagnosis would otherwise appear. Today, medicine
waits for symptoms. We are shifting to continuous, pre-symptomatic health
monitoring that treats disease as a geometry problem, not a lottery.

## U01.3 — Short tagline

GPS for Health — from reactive to proactive care.

## U01.4 — Project title / company name

Cytognosis Foundation
```

**Rules:**
- Every sub-slot has a level-2 heading matching its ID (`## U01.1 — <name>`).
- Frontmatter `sub_slots` list must match the H2 headings in the body (validated programmatically).
- `max_words` / `max_chars` are the canonical-authoring limits, sized generously. Funder limits are applied at render time and can be smaller.
- `funder_hooks` are the authoritative forward mapping — this sub-slot fills *these* funder questions.
- `cytognosis_anchor` is the free-text pointer to the operational doc that holds the canonical phrasing (Helix paper, brand skill, etc.).

---

## 4. Manifest schema (`manifest.yaml`)

```yaml
version: 1.0
last_updated: 2026-04-23
maintainer: mohammadi@cytognosis.org

slot_families:
  heilmeier_core:
    ids: [U01, U02, U03, U04, U05, U06, U07, U08]
    description: DARPA Heilmeier Catechism, in order. Every proposal answers these.
  extensions:
    ids: [U09, U10, U11, U12, U13, U14, U15, U16, U17, U18, U19, U20]
    description: 12 recurring extensions covering team, openness, equity, AI safety, IP, regulatory, adoption, translation, sustainability, partnerships.
  administrative:
    ids: [A01, A02, A03, A04, A05]
    description: Not proposal content. Org identity, POC, compliance, supplementary artifacts, intake meta.

slots:
  U01:
    name: Objective, in plain language
    family: heilmeier_core
    file: slots/U01_objective.md
    required_by: [heilmeier, nih_r01, nsf_tech_labs, arpah_mission_office, doe_genesis, astera_residency, brains_accelerator, foresight_nodes, google_impact_challenge, yc_nonprofit]
  # ...one entry per slot...

funders:
  heilmeier:
    name: DARPA Heilmeier Catechism
    file: funders/heilmeier.yaml
    kind: universal_baseline
  nih_r01:
    name: NIH R01 Research Strategy
    file: funders/nih_r01.yaml
    kind: federal_grant
  # ...one entry per funder...

length_enforcement:
  strategy: funder_first      # funder limits override slot limits at render
  on_overflow: warn           # warn | truncate | fail
```

---

## 5. Funder sink file format

Each funder file declares how the universal template is projected into that funder's required shape. Example:

```yaml
funder_id: arpah_mission_office
display_name: ARPA-H Mission Office ISO
version: 2025.1
source_doc: raw/arpah_appendix_a_solution_summary.md
primary_artifacts:
  - id: appendix_a
    name: Solution Summary (Appendix A)
    format: docx
    page_limit: 5
    sections:
      - heading: "1. Program fit — what are you trying to do?"
        slots: [U01, U09.1]
        word_limit: 400
      - heading: "2. How is it done today, and what are the limits?"
        slots: [U02]
        word_limit: 400
      - heading: "3. What is new + quantitative metrics"
        slots: [U03, U08.1]
        word_limit: 500
      - heading: "4. Who cares?"
        slots: [U04, U13.1, U17.1]
        word_limit: 300
      - heading: "5. Risks"
        slots: [U05, U14.2, U16]
        word_limit: 300
      - heading: "Team / key personnel"
        slots: [U11]
        word_limit: 200
      - heading: "Budget synopsis"
        slots: [U06]
        word_limit: 200
  - id: tech_mgmt_proposal
    name: Full Technical & Management Proposal
    format: docx
    page_limit: 20
    sections:
      - heading: "Executive Summary"
        slots: [U01, U04, U08.1]
      # ...
  - id: cost_proposal
    name: Cost Proposal
    format: xlsx
    slots: [U06, A01, A03]
  - id: tdd
    name: Technology Development Document
    format: docx
    slots: [U15, U16.4, U20.2]

render_targets:
  - google_docs:
      doc_id_env: ARPAH_SOLUTION_SUMMARY_DOC_ID
      mapping: appendix_a
  - docxtpl:
      template_path: raw/arpah_appendix_a_solution_summary.docx
      mapping: appendix_a
```

**Rules:**
- `sections[].slots` is an ordered list of slot IDs (or sub-slot IDs like `U08.1`) that populate this section.
- `word_limit` / `page_limit` override the slot-level authoring limit at render.
- `render_targets` declare the concrete output surfaces (Google Docs, docxtpl, etc.); a single funder can have multiple targets.

---

## 6. Authoring workflow

1. **Create/update a slot.** Edit `slots/U0X_*.md`. Frontmatter validated on save.
2. **Register a new funder.** Add `funders/<funder>.yaml` declaring sections and slot assignments.
3. **Validate.** `scripts/validate.py` checks:
   - Every slot file has valid frontmatter against the slot schema.
   - Every sub-slot heading in a body matches the frontmatter `sub_slots`.
   - Every `funder_hooks` reference points to a real section in a real funder file.
   - Every `funders/<x>.yaml` section references only known slot IDs.
   - Every `required_by` funder in a slot's frontmatter is declared in the manifest.
4. **Render.** `scripts/render.py --funder <id> --target <target>` produces the artifact under `renders/<funder>/<year>/<proposal-id>/`.

---

## 7. Render pipeline (summary)

```
slots/*.md + funders/<funder>.yaml + manifest.yaml
        │
        ▼
  Jinja2 assembly: pick slots, apply word limits, build ordered sections
        │
        ▼
   Intermediate Markdown (per section)
        │
        ├── → Google Docs API batchUpdate      (primary)
        ├── → Google Sheets API values.batch   (budget)
        ├── → Google Slides API batchUpdate    (deck)
        ├── → docxtpl(funder.docx)             (funder-required DOCX)
        ├── → openpyxl+Jinja+recalc.py         (funder-required XLSX)
        └── → Quarto render                    (internal PDF review)
```

Detailed tool selection: see `format_conversion_decision_tree.md`.

---

## 8. Length limits — who wins

Precedence, highest to lowest:
1. **Funder section limit** (e.g., ARPA-H §1 = 400 words) — hard rule, enforced at render.
2. **Sub-slot authoring limit** (e.g., `U01.1.max_words = 30`) — soft rule, enforced at author time.
3. **Slot authoring limit** (sum of sub-slots, advisory).

On overflow, the default is `warn` — the render completes but prints a diagnostic. Configurable per funder to `truncate` or `fail`.

---

## 9. ID conventions

- **Slot IDs:** `U01`–`U20` (universal), `A01`–`A05` (administrative). Zero-padded, two digits.
- **Sub-slot IDs:** `U01.1`, `U01.2`, … — dot-separated, no leading zero on the sub-number.
- **Funder question IDs:** `<funder>.<question>` — e.g., `google.Q16a`, `foresight.F15`, `arpah.appendix_a.1`. Funder prefix must match the `funder_id` in the funder file.
- **Funder section IDs:** optional; when needed, `<funder>.<artifact>.<section_index_or_name>`.

IDs are case-sensitive and stable — never renumber after authored content exists.

---

## 10. Versioning

- **Slot content:** tracked in git; `status` frontmatter field progresses `draft → reviewed → approved → deprecated`.
- **Funder files:** `version` field is `<year>.<minor>`; bump `minor` when the funder changes a section heading, word limit, or required set; bump `year` when a new cycle's solicitation drops.
- **Manifest:** semantic-ish — `major.minor`; bump `major` on breaking schema changes, `minor` on additive changes.
- **Breaking changes** to slot IDs, sub-slot IDs, or slot families require explicit deprecation notices in the affected slot file and a migration note in `CHANGELOG.md`.

---

## 11. What this format does *not* do

- It does not prescribe prose style — voice and tone live in the brand skill.
- It does not do content discovery — it assumes the author knows which slot to edit.
- It does not enforce scientific rigor — that is the Heilmeier / review-criteria layer.
- It does not generate content — Instructor/LLM fills are a separate concern applied *to* slot files, not done *by* the template format.
- It does not store rendered artifacts — `renders/` is output only and ignored by git.

---

## 12. Relationship to other artifacts

| Artifact | Role | Relationship to this spec |
|---|---|---|
| `framework_catalog.md` | Survey of 10+ funder rubrics | Input — informed the universal slot design |
| `extracted_questions_applications.md` | Raw Q-by-Q extraction of application forms | Input — populated `funders/*.yaml` sections |
| `extracted_grants.md` | Raw extraction of federal grant templates | Input — populated `funders/*.yaml` sections |
| `universal_template.md` | Slot definitions (U01–U20, A01–A05) + mapping table | Canonical slot list; this spec is the machine form of that doc |
| `format_conversion_decision_tree.md` | Tool selection for ingestion/rendering | Downstream — tells you *how* to get content in and out |
| `funder_crosswalk_matrix.md` | Reverse map (every funder question → slot IDs) | Authoritative crosswalk; generated from `funders/*.yaml` |
| `templating_stack_v2.md` | Full tool-evaluation reference | Shelved — consult only for rationale |

---

## 13. Groups & inheritance (added in v1.2)

Groups bundle related slots and fields so a funder profile can compose its schema from named bundles instead of listing every member explicitly. Group definitions live in `canonical/groups.yaml`. Three group families exist:

- `u_*` — proposal-content slot bundles (e.g., `u_heilmeier_core`, `u_extensions_research`, `u_extensions_values`, `u_org_form_fit`).
- `a_*` — administrative-section bundles (`a_baseline`, `a_compliance`, `a_artifacts`, `a_full`).
- `f_*` — funder-metadata-field bundles (`f_classification`, `f_pipeline`, `f_timeline`, `f_financial`, `f_application`, `f_eligibility`, `f_relationships`, `f_full`).

A **preset** is a named composition of one or more groups across all three families. Presets correspond to `funder_kinds` in the manifest, so picking a preset is equivalent to declaring the funder kind and composing its default schema in one step.

### Funder-profile syntax

A funder profile composes its schema in three layers, evaluated top-to-bottom:

```yaml
funder_id: arpah_mission_office
display_name: ARPA-H Mission Office ISO
preset: preset_federal_OT          # layer 1: named composition
inherit_groups:                    # layer 2: extra groups merged in
  u: [u_extensions_values]
  a: []
  f: []
add_slots: [U21]                   # layer 3a: add specific slots
remove_slots: []                   # layer 3b: remove specific slots
add_fields: []                     # layer 3c: add specific fields
remove_fields: [F37]               # layer 3d: remove specific fields
```

Either `preset:` or `inherit_groups:` is sufficient on its own. Using both is allowed and additive.

### Resolution algorithm

1. Expand the named `preset:` (if present) into three group lists (u/a/f).
2. Merge `inherit_groups:` lists in (deduplicating).
3. Expand each group to its members (slot IDs / field IDs) using `groups.yaml`.
4. Apply `add_slots`, `remove_slots`, `add_fields`, `remove_fields` overrides.
5. The resulting flat lists are the funder's effective slot/field set, used by the renderer.

### Conflict resolution

- Group-vs-group: union (additive).
- Override-vs-group: overrides win (`remove_slots` removes a slot even if a group includes it; `add_slots` adds a slot even if no group includes it).
- Multiple presets: not allowed; declare one preset, then add groups via `inherit_groups`.

### Validation

- Every referenced group must exist in `groups.yaml`.
- Every referenced slot ID must exist in `manifest.yaml` `slots:`.
- Every referenced field ID must exist in `manifest.yaml` `funder_metadata_fields:`.
- A preset's `inherits:` must refer only to defined groups.

### When to extend vs override

- **Add a new group** when several funders share a slot/field set that does not match an existing group cleanly. New groups land in `groups.yaml` and become reusable.
- **Use overrides** for one-off deviations. Overrides keep the noise local to one funder file.

---

## 14. F-side schema (funder metadata fields, added in v1.2)

The F-series describes the **funding opportunity itself** — what we know about it before, during, and after applying. F-fields drive the Monday `Funding Opportunities` board columns and live on the funder profile under `funder_metadata:`.

### Where F-fields live

```yaml
# canonical/funders/<funder>.yaml
funder_id: arpah_mission_office
preset: preset_federal_OT
funder_metadata:
  F01: Grants
  F04: Government
  F05: federal_OT
  F33: ["#Moonshot", "#PHO", "#HSF", "#Proactive"]
  F35: true
  F36: program_officer
  F31:
    - name: Milad Alucozai
      role: ARPA-H Program Manager network
      relationship: program guidance & timing intel
  F32: [nsf_tech_labs, convergent_research_fro]
  F34:
    - id: arpah_delphi
      name: DELPHI biosensor program
      url: https://www.arpa-h.gov/explore-funding/programs/delphi
      relationship: companion
```

The renderer uses these values to populate the Monday board row when the funder profile is registered, and the Drive funding-research summary inherits the same fields when generating per-opportunity sections.

### What F-fields are not

- Not proposal content. F-fields never render into a funder's submission artifact.
- Not slot files. F-fields are inline schema (in `manifest.yaml`); they do not have one-file-per-field.
- Not authoritative for U/A content. The slot files (U01–U22, A01–A05) remain the source of truth for what we write into the proposal.

### Full F-field reference

See [`funder_metadata.md`](funder_metadata.md) for human-readable field documentation organized by group, with examples and the Monday-column-cluster mapping.

---

## 15. Open questions (tracked, not yet resolved)

1. **Multiple concurrent proposals reusing the same slots** — how do we fork a slot for proposal-specific variants without losing the canonical content? Likely a proposal-level overlay file.
2. **Attachment/figure management** — figures live where? `slots/assets/` with path references in frontmatter, or separate asset manifest.
3. **Collaboration semantics in Google Workspace** — if two authors edit the same rendered Google Doc, do we round-trip changes back into `slots/*.md`? Probably no (source-of-truth stays in git).
4. **Proposal-specific numeric data** (budgets, timelines) — currently mixed with narrative slots. Candidate: split into `data/<proposal>/*.yaml` and reference from slot bodies.

These are deferred until we have filled the first full proposal end-to-end.

---

*Authored 2026-04-23. Supersedes no prior spec (this is the first formal version).*
