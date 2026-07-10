# Funder Metadata Schema (F-series)

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: leadership, grant team
> **Tags**: `funding`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

**Status:** Authoritative reference for F01–F38 funder-metadata fields.
**Authored:** 2026-04-26 (manifest v1.2; groups v1.0).
**Companion to:** [`universal_template.md`](universal_template.md) (U-side) and [`canonical/groups.yaml`](slot-library/groups.yaml) (inheritance taxonomy).

This document explains what the F-series fields are, why they exist, and how they group together for inheritance. The machine-readable definitions live in [`canonical/manifest.yaml`](slot-library/manifest.yaml) under `funder_metadata_fields:`.

---

## Why an F-series

The U/A series describe **proposal content** — what we write into a grant application. The F-series describes **the funding opportunity itself** — what we know about a program before we apply, while we apply, and after we apply.

F-fields drive three downstream surfaces:
1. **Monday Funding Opportunities board columns** — every F-field maps to a column or column cluster.
2. **Funder profile YAML** — `canonical/funders/<funder>.yaml` carries an opportunity-level `funder_metadata:` block.
3. **Drive funding-research summary** — the `Funding Opportunities` and `Funding Opportunities (shortlist)` Google Docs are organized by F-field clusters.

---

## Field-group taxonomy

F-fields organize into **seven groups**, declared in `canonical/groups.yaml`. Funder profiles inherit one or more groups instead of declaring fields one-by-one.

| Group | Members | Drives Monday cluster |
|---|---|---|
| `f_classification` | F01, F04, F05, F06, F07, F12, F33 | classification (status, dropdowns, tags) |
| `f_pipeline` | F02, F03, F10, F21 | pipeline (stage, status, alignment, process) |
| `f_timeline` | F08, F09, F13, F19 | timeline (deadline, stages, period) |
| `f_financial` | F23, F24, F15, F17, F18 | financial (min/max award, indirect, cost-share) |
| `f_application` | F11, F14, F16, F28, F29, F35, F36 | application (format, effort, gates, criteria, review mechanism) |
| `f_eligibility` | F25, F26, F27, F30, F37, F20 | eligibility (residency, partners, NDA, academic affiliation) |
| `f_relationships` | F22, F31, F32, F34, F38 | relationships (canonical ref, insider connections, sub-programs, pairings) |

Each group also has a `monday_column_cluster:` annotation in `groups.yaml` so the Monday board generator knows which columns to bundle visually.

---

## Field reference (F01–F38)

### Group `f_classification` — what kind of opportunity is this

| ID | Name | Type | Notes |
|---|---|---|---|
| F01 | `funding_category` | enum | Grants · Small Grants · Accelerators & Incubators · Credits · Discounts · Investment |
| F04 | `funding_source_type` | enum | Government · Philanthropic Foundation · FRO/Moonshot · Corporate · VC · EA/Longtermist · Intergovernmental · Nonprofit Program |
| F05 | `funding_type` | text | Free-text type (e.g., "research grant", "fellowship", "OT contract") |
| F06 | `funding_subtype` | text | Free-text subtype (e.g., "U54", "OT-Other Transaction", "FRO-style", "TechSoup-mediated") |
| F07 | `focus_areas` | dropdown_multi | Fixed enum: AI for Science · Healthcare · Open Science · Proactive Health · AI Safety · Biotech/Pharma · Climate/Energy · General Tech · Digital Health |
| F12 | `instrument` | enum | grant · investment · credits · discount · in-kind · fellowship · hybrid · TBD-at-closing |
| F33 | `thematic_tags` | list[str] | **New v1.2.** Hashtag taxonomy from Drive: #Moonshot · #FRO · #Open · #Cytoscope · #Cytoverse · #Cytonome · #Proactive · #Healthspan · #Neuro · #AI · #Biotech · #ImpactCenter · #Equity. Flexible and program-specific. |

### Group `f_pipeline` — where does this sit in our process

| ID | Name | Type | Notes |
|---|---|---|---|
| F02 | `maturity_stage` | enum | Early · Intermediate · Late |
| F03 | `pipeline_status` | enum | Not Started · Under Consideration · Under Preparation · Internal Review · Applied · Approved/Granted · Rejected · Archived |
| F10 | `mission_alignment` | rating 0–5 | Subjective fit score |
| F21 | `funder_process_type` | enum | proactive (funder reaches out) · reactive (open application) · hybrid |

### Group `f_timeline` — temporal characteristics

| ID | Name | Type | Notes |
|---|---|---|---|
| F08 | `deadline` | date | Next deadline (single or computed) |
| F09 | `deadline_type` | enum | Single Deadline · Recurring Annual · Ongoing/Rolling |
| F13 | `submission_stages` | list | E.g., `[concept, full]` · `[LOI, full]` · `[abstract, full]` · `[round1, round2]` |
| F19 | `award_period_months` | int | Period of performance |

### Group `f_financial` — money in, money out

| ID | Name | Type | Notes |
|---|---|---|---|
| F23 | `min_award_usd` | numeric | Existing Monday `numeric_mm2bddjd` |
| F24 | `max_award_usd` | numeric | Existing Monday `numeric_mm2bw7ds` |
| F15 | `investment_horizon_years` | int | VC / venture-builder; null for grants |
| F17 | `cost_share_required` | bool/percent | E.g., NSF Tech Labs requires partner cost-share |
| F18 | `indirect_cost_rule` | enum | flat_15pct · flat_10pct · flat_25pct · capped_negotiated · fEC · F&A_negotiated · OT_negotiated · direct_only · uncapped |

### Group `f_application` — what the application process looks like

| ID | Name | Type | Notes |
|---|---|---|---|
| F11 | `initial_submission_format` | text | E.g., "5-page Solution Summary" · "1-2 page concept note" · "15-page project description + 2-page collaboration plan" |
| F14 | `application_effort` | enum | light (≤2h) · medium (≤20h) · heavy (>20h) |
| F16 | `application_required` | enum | yes · verification_only · no · invitation_only |
| F28 | `written_feedback_gate` | bool | Funder requires written feedback round before full proposal (ARPA-H) |
| F29 | `review_criteria` | list | Structured criteria with weights when published |
| F35 | `heilmeier_required` | bool | **New v1.2.** Funder explicitly requires Heilmeier Catechism addressing |
| F36 | `review_mechanism` | enum | **New v1.2.** peer_review · program_officer · internal_panel · invitation_only · expert_committee · dual_anonymous · hybrid |

### Group `f_eligibility` — who can apply

| ID | Name | Type | Notes |
|---|---|---|---|
| F25 | `residency_required` | bool | E.g., Astera Emeryville requirement |
| F26 | `residency_location` | string | City/region required |
| F27 | `confidentiality_policy` | enum | standard · no_confidential_ip · nda_required |
| F30 | `required_partners_count` | int | Horizon Europe min 3 partners from 3 EU countries |
| F37 | `academic_affiliation_required` | bool | **New v1.2.** PI must hold academic appointment (NIH default) |
| F20 | `joint_program_partners` | list[str] | Partner-org names for joint programs (e.g., NSF-NIH Smart Health) |

### Group `f_relationships` — cross-references and connections

| ID | Name | Type | Notes |
|---|---|---|---|
| F22 | `canonical_funder_ref` | string | Path to `canonical/funders/<funder_id>.yaml` when modeled |
| F31 | `strategic_connection` | list[obj] | **New v1.2.** Insider connections: name · role · relationship · notes. From Drive: Adam Marblestone (Convergent), Milad Alucozai (ARPA-H), Angela Pisco (CZI), Shankar Subramaniam (Wellcome Leap), Erin Rist (CZI). |
| F32 | `strategic_pairing` | list[str] | **New v1.2.** Linked opportunity IDs (e.g., `nsf_tech_labs` paired with `convergent_research_fro`) |
| F34 | `sub_programs` | list[obj] | **New v1.2.** Child / companion programs: id · name · url · relationship (child / companion / predecessor / successor). Captures ARPA-H ISO → DELPHI/PROSPR/EVIDENT and NIH Common Fund → Bridge2AI/PRIMED-AI. |
| F38 | `funding_score_rationale` | text | **New v1.2.** Free-text "why this F10 score" |

---

## Group inheritance — how funder profiles compose

A funder profile in `canonical/funders/<funder>.yaml` declares either a **preset** (a named composition of groups) or a custom **inherit_groups** triple. Both pull in U/A/F slot bundles in one shot.

### Preset shorthand (recommended)

```yaml
funder_id: arpah_mission_office
display_name: ARPA-H Mission Office ISO
preset: preset_federal_OT          # pulls u_heilmeier_core + u_extensions_research
                                   # + u_extensions_values + u_org_form_fit
                                   # + a_full + all 7 f_groups
funder_metadata:
  F01: Grants
  F04: Government
  F05: federal_OT
  F33: ["#Moonshot", "#PHO", "#HSF"]
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

### Custom inheritance

```yaml
funder_id: czi_billion_cells
preset: preset_private_grant
inherit_groups:
  u: [u_extensions_values]   # add extra group on top of preset
add_slots: [U22]             # one-off slot inclusion
remove_slots: [U18]          # opt out of translation-to-mission
add_fields: []
remove_fields: [F18]         # CZI doesn't enforce a uniform indirect rule
```

### Resolution algorithm

1. Expand `preset:` → three group lists (u/a/f).
2. Merge `inherit_groups:` lists in (deduplicate).
3. Expand groups → flat slot/field IDs.
4. Apply `add_slots`, `remove_slots`, `add_fields`, `remove_fields`.
5. The final flat lists are the funder's effective schema.

Validation: every referenced group must exist in `groups.yaml`; every slot/field ID must exist in `manifest.yaml`.

---

## Monday board mapping

Every F-field carries either an existing `monday_column_id:` (for v1.1 fields) or a placeholder pending a Monday board pass (for v1.2 fields F31–F38). The execution spec for the next Monday-update session declares which new columns to add. See [`agent/prompts/execution_spec_v1.md`](../../agent/prompts/execution_spec_v1.md) §3 (Fundraising/Monday consolidation).

| F-field | Monday column id | Status |
|---|---|---|
| F01–F11, F23, F24 | various existing | Existing in board 18409744388 |
| F12–F22, F25–F30 | (none yet) | v1.1 — proposed for next Monday pass |
| F31–F38 | (none yet) | v1.2 — proposed for next Monday pass |

---

## Coverage against the 71-opportunity inventory

The Drive funding-research summary plus the Monday board contain **71 opportunities**. Treating each by its **submission shape** rather than its funder identity, the F-series + group taxonomy covers all six categorical groups:

| Inventory group | Opportunities | Recommended preset |
|---|---:|---|
| Federal full proposals | 14 | `preset_federal_grant` or `preset_federal_OT` |
| Philanthropic full proposals | 13 | `preset_private_grant` or `preset_philanthropic_proactive` |
| EA / counterfactual micro-grants | 6 | `preset_ea_micro_grant` |
| Accelerator / incubator applications | 10 | `preset_accelerator` |
| VC investments | 7 | `preset_vc_investment` or `preset_venture_builder` |
| Corporate credits / API access | 7 | `preset_corporate_credit` |
| Nonprofit discounts | 20 | `preset_nonprofit_discount` |

Total 77 (10 opportunities counted in two groups due to dual-classification, e.g., Anthropic AI for Science is both a credit program and a grant). Net **71 unique** opportunities, all reachable from the seven `preset_*` compositions.

---

## Changelog

| Version | Date | Change |
|---|---|---|
| 1.0 | 2026-04-26 | Initial F-series schema; F01–F11 documented from existing Monday columns |
| 1.1 | 2026-04-25 | Added F12–F30 (instrument, application_effort, indirect_cost_rule, residency, etc.) |
| 1.2 | 2026-04-26 | Added F31–F38 (strategic_connection, strategic_pairing, thematic_tags, sub_programs, heilmeier_required, review_mechanism, academic_affiliation_required, funding_score_rationale). Introduced groups.yaml with seven F-groups and ten composition presets. |
