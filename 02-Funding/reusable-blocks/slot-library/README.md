# Cytognosis Canonical Template System

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: grant team, leadership
> **Tags**: `funding`, `slot-library`, `system-of-record`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

> [!IMPORTANT]
> **Funding system of record.** The slot-library (slots + funders + profiles + proposals) is canonical for all Cytognosis funding. Funder profiles follow the Funding Opportunity Profile template (cytognosis-doc skill v5.6.0).

**Status:** Draft (lives under `_draft/canonical/` until promoted to `01_framework/` root).
**Authored:** 2026-04-23. **Last updated:** 2026-04-26 (manifest v1.2, groups v1.0).
**Maintainer:** mohammadi@cytognosis.org.

This directory holds the harmonized source-of-truth for every Cytognosis grant, application, white paper, LOI, pitch deck, and proposal. It consolidates 10+ funder frameworks into 27 addressable proposal-content slots (U01–U22 + A01–A05), 38 funder-metadata fields (F01–F38), and 11 named composition presets, rendering primarily to Google Workspace.

## Read this first

1. **Spec:** [`../canonical_template_format.md`](../canonical_template_format.md) — format invariants, directory layout, YAML schema, ID conventions, groups & inheritance (§13), F-side schema (§14).
2. **Slot definitions (U/A side):** [`../universal_template.md`](../universal_template.md) — human-readable slot rationale (Part C has per-funder mappings).
3. **Funder metadata (F side):** [`../funder_metadata.md`](../funder_metadata.md) — F01–F38 reference organized by group, with examples.
4. **Groups & inheritance:** [`groups.yaml`](groups.yaml) — eight F-groups, six U-groups, four A-groups, eleven composition presets.
5. **Crosswalk matrix:** [`../funder_crosswalk_matrix.md`](../funder_crosswalk_matrix.md) — reverse lookup (funder question → slot) and slot × funder matrix.
6. **Rendering tools:** `../format_conversion_decision_tree.md` (target archived/removed) — which tool for which input/output format.

## Directory layout

```
canonical/
├── manifest.yaml              # Authoritative slot + funder + F-field registry
├── groups.yaml                # Group definitions + composition presets (v1.2)
├── CHANGELOG.md               # Schema version history
├── slots/                     # 27 slot files — U/A canonical authored content
│   ├── U01_objective.md           # Heilmeier Q1 + extensions
│   ├── U02_sota_and_limits.md
│   ├── ...
│   ├── U20_partnerships.md
│   ├── U21_counterfactual.md      # added v1.1 (counterfactual & impact-without-funder)
│   ├── U22_theory_of_change.md    # added v1.1 (explicit causal-chain artifact)
│   ├── A01_org_identity.md        # Administrative (non-content)
│   └── ... (A02–A05)
├── funders/                   # 10 funder files — how each funder consumes slots
│   ├── heilmeier.yaml             # Universal baseline
│   ├── nih_r01.yaml               # NIH R01
│   ├── nsf_tech_labs.yaml         # NSF Tech Labs RFI
│   ├── arpah_mission_office.yaml  # ARPA-H Mission Office ISO
│   ├── doe_genesis.yaml           # DOE Genesis Mission
│   ├── astera_residency.yaml      # Astera Residency
│   ├── brains_accelerator.yaml    # Brains Accelerator
│   ├── foresight_nodes.yaml       # Foresight Nodes
│   ├── google_impact_challenge.yaml  # Google.org Impact Challenge
│   └── yc_nonprofit.yaml          # YC Nonprofit
├── research/                  # Funder discovery materials
│   ├── funding_opps_inventory.md  # 71-opportunity Monday board inventory
│   └── profiles/                  # Per-opportunity profiles (30+ funders)
├── lib/
│   ├── macros/                # Reusable Jinja macros (TBD)
│   └── validators/            # LinkML/Pydantic validators (TBD)
└── README.md                  # This file
```

F-fields (F01–F38) are not slot files; they are inline schema in `manifest.yaml` under `funder_metadata_fields:` with human-readable documentation in `../funder_metadata.md`.

## Coverage snapshot

| Metric | Count | Notes |
|---|---:|---|
| Universal slots (U01–U22) | 22 | U21/U22 added in v1.1 |
| Administrative slots (A01–A05) | 5 | |
| Funder-metadata fields (F01–F38) | 38 | F31–F38 added in v1.2 |
| U-groups (proposal-content bundles) | 6 | u_heilmeier_core, u_extensions_minimal, u_extensions_research, u_extensions_values, u_org_form_fit, u_full |
| A-groups (administrative bundles) | 4 | a_baseline, a_compliance, a_artifacts, a_full |
| F-groups (funder-metadata bundles) | 8 | f_classification, f_pipeline, f_timeline, f_financial, f_application, f_eligibility, f_relationships, f_full |
| Composition presets | 11 | one per `funder_kind` |
| Funders modeled | 10 | heilmeier + 9 real funders |
| Funding opportunities tracked (Monday) | 71 | covered by 11 presets |
| Slot files authored with real content | 2 full (U01, U08) · 2 partial (U03, U06) · 21 stubs | U21/U22 are stubs |

## Slot content status

Slots with real prose (Cytognosis canonical content hooks applied):
- `U01` Objective — all 4 sub-slots
- `U08` Exams & gates — all 4 sub-slots
- `U03` Novelty & approach — U03.1, U03.3 (U03.2/U03.4/U03.5 are stubs)
- `U06` Cost — U06.1, U06.5 (U06.2/U06.3/U06.4 are stubs)

All other slots carry `<!-- STUB: ... -->` placeholders and `status: stub` in frontmatter. Advance to `status: draft → reviewed → approved` as content is authored.

## Quick start

To see how a funder consumes slots:

```bash
less canonical/funders/arpah_mission_office.yaml
```

To see the canonical content for a slot:

```bash
less canonical/slots/U01_objective.md
```

To see the full slot × funder matrix:

```bash
less _draft/funder_crosswalk_matrix.md
```

## Next steps (in order)

1. **Migrate the 10 existing funder yamls to `preset:` shorthand.** Each existing funder file currently lists slots explicitly; replace with the matching preset (e.g., `arpah_mission_office.yaml` → `preset: preset_federal_OT`) plus any one-off overrides. Reduces ~80% of the boilerplate per funder file.
2. **Author Tier-1 priority funder yamls.** Wellcome Leap, NIH PRIMED-AI, Horizon Europe Cluster 1, Convergent Research FRO, ARPA-H PHO (companion to existing Mission Office ISO), CZI, Gates Grand Challenges. Each uses `preset:` plus `funder_metadata:` block.
3. **Author lightweight templates.** `corporate_credit_template.yaml`, `nonprofit_discount_template.yaml`, `vc_investment_template.yaml` — covers the long tail of similar opportunities without one-funder-one-file proliferation.
4. **Fill prose in U02, U04, U05, U07, U09–U22, A01–A05.** Pull canonical phrasing from the brand, science, and openness skills. The crosswalk matrix and execution spec (`agent/prompts/execution_spec_v1.md`) tell you every funder prompt the content will serve.
5. **Write validators.** Python script under `lib/validators/` that checks frontmatter ↔ H2 parity, manifest ↔ funder-yaml consistency, group resolution, preset existence, funder_hooks resolvability.
6. **Write renderers.** One for each target kind:
   - `google_docs` — Google Docs API `batchUpdate` with slot → Doc body text replacement.
   - `docxtpl` — Jinja fill against funder-provided `.docx` in `raw/`.
   - `openpyxl_jinja` — Budget XLSX fill with `recalc.py` post-step.
   - `quarto` — narrative PDF/HTML render for internal review.
7. **Promote to `01_framework/`.** Once validators pass and at least one funder renders end-to-end into Google Docs, move this folder out of `_draft/` and into the `01_framework/` root.
8. **Versioning.** Tag this as `canonical-template-v1.2` in git once promoted.

## Design constraints (do not violate)

- **Slot IDs are immutable.** Never renumber. Add new slots at the end.
- **Length limits are render-time, not author-time.** Author at the longest funder limit; the render pipeline trims.
- **One slot file per slot.** Do not split a slot across files.
- **No funder-specific prose in slot files.** Funder-specific framing lives in funder yaml `heading:` text, not in slot bodies.
- **Source-of-truth stays in git.** Google Docs renders are views, not sources. Never round-trip content back from Docs to `.md` without a diff review.
