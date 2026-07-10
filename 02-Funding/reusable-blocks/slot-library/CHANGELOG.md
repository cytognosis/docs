# CHANGELOG — Cytognosis Canonical Template

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: grant team
> **Tags**: `funding`, `slot-library`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

All notable changes to the canonical template system are tracked here. Format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/) with semantic-ish versioning (`major.minor`).

---

## [1.2] — 2026-04-26

Schema-bump driven by (a) cross-referencing the in-repo opportunity inventory with the Drive `Funding Opportunities` and `Funding Opportunities (shortlist)` summary docs to capture insider-connection data, sub-program companions, strategic pairings, and a hashtag-style thematic taxonomy that the v1.1 F-fields did not encode; and (b) introducing **multi-group inheritance** so funder profiles can compose schemas from named bundles instead of listing every slot/field one-by-one.

### Added

#### Group taxonomy and inheritance system
- **`canonical/groups.yaml`** — first-class group definitions for the U-side (proposal content), A-side (administrative), and F-side (funder metadata). Six U-groups, four A-groups, eight F-groups, plus eleven composition presets (`preset_federal_grant`, `preset_federal_OT`, `preset_intergovernmental_grant`, `preset_private_grant`, `preset_philanthropic_proactive`, `preset_ea_micro_grant`, `preset_private_fellowship`, `preset_accelerator`, `preset_vc_investment`, `preset_venture_builder`, `preset_corporate_credit`, `preset_nonprofit_discount`).
- **Inheritance algorithm** — funder profile names a `preset:`, optionally extends with `inherit_groups:`, and may override individual members with `add_slots` / `remove_slots` / `add_fields` / `remove_fields`. Documented in `canonical_template_format.md` §14.

#### New funder-metadata fields (F31–F38)
Added to manifest `funder_metadata_fields:` and grouped into existing F-groups in `groups.yaml`. Drive funding-research summary surfaced these as missing.
- **F31 `strategic_connection`** (list of objects: name · role · relationship · notes) — insider connections that shape access (Adam Marblestone @ Convergent Research, Milad Alucozai @ ARPA-H, Angela Pisco / Erin Rist @ CZI, Shankar Subramaniam @ Wellcome Leap).
- **F32 `strategic_pairing`** (list of opportunity IDs) — opportunities that move together (NSF Tech Labs ↔ Convergent Research FRO; ARPA-H ISO ↔ DELPHI biosensor companion).
- **F33 `thematic_tags`** (list of strings) — hashtag taxonomy from the Drive doc: `#Moonshot`, `#FRO`, `#Open`, `#Cytoscope`, `#Cytoverse`, `#Cytonome`, `#Proactive`, `#Healthspan`, `#Neuro`, `#AI`, `#Biotech`, `#ImpactCenter`, `#Equity`. Distinct from F07 `focus_areas` (which is a fixed enum).
- **F34 `sub_programs`** (list of objects: id · name · url · relationship) — child / companion / predecessor / successor programs (ARPA-H Mission Office ISO → DELPHI / PROSPR / EVIDENT; NIH Common Fund → Bridge2AI / PRIMED-AI).
- **F35 `heilmeier_required`** (bool) — funder explicitly requires Heilmeier Catechism addressing in the initial submission. Drives template selection in render.
- **F36 `review_mechanism`** (enum: peer_review · program_officer · internal_panel · invitation_only · expert_committee · dual_anonymous · hybrid).
- **F37 `academic_affiliation_required`** (bool) — PI must hold an academic appointment (NIH default).
- **F38 `funding_score_rationale`** (text) — free-text explanation behind the F10 mission-alignment score.

#### Companion documentation
- **`funder_metadata.md`** — human-readable F-side reference, organized by group with field tables. Companion to `universal_template.md` (which covers U/A side).

### Changed
- Manifest version bumped `1.1 → 1.2`.
- `funder_metadata` family now has 38 IDs (was 30).
- Manifest now references `groups_file: groups.yaml` and `funder_metadata_doc: ../funder_metadata.md`.
- `canonical_template_format.md` gains §14 (Groups & Inheritance) and §15 (F-side schema).

### Deferred (will land in v1.3)
- Migrate the 10 existing funder yaml files from explicit slot lists to `preset:` shorthand.
- Add Tier-1 priority funder yaml files using new presets (Wellcome Leap, NIH PRIMED-AI, Horizon Europe Cluster 1, Convergent Research FRO, ARPA-H PHO, CZI, Gates Grand Challenges).
- Author lightweight `corporate_credit_template.yaml`, `nonprofit_discount_template.yaml`, and `vc_investment_template.yaml` to cover the long tail of similar opportunities without one-funder-one-file proliferation.
- Validators (`lib/validators/`) for group resolution, preset existence, and override consistency.

---

## [1.1] — 2026-04-25

Schema-bump driven by analysis of all 71 funding opportunities currently tracked in Monday's `Fundraising → Funding Opportunities` board. Inventory is at `research/funding_opps_inventory.md`; per-opportunity profiles are in `research/profiles/`; aggregated gaps in `research/research_summary.md`.

### Added

#### New slot family
- **`funder_metadata` family (F01–F30)** — 30 fields describing the funding opportunity itself (instrument, submission stages, application effort, indirect-cost rule, residency, etc.). F01–F11 already existed as Monday columns; F12–F30 are new. These are not proposal content — they live on funder files and on the Monday board, not in slot files.

#### New top-level slots (in `extensions` family)
- **U21 Counterfactual & impact-without-funder** — what happens if we don't get this funding (work / talent / venue counterfactuals). Required by EA LTFF, EAIF, Coefficient Giving, DRK; useful for most philanthropy.
- **U22 Theory of change** — explicit causal-chain artifact (problem → activities → outputs → outcomes → impact) with per-link assumptions, evidence, and indicators. Required by DRK, RWJF, EA Funds, Coefficient Giving, AstraZeneca CHANGE.

#### New funder kinds (in `funder_kinds` registry)
Distinguishes which slot subset and rendering pattern a funder needs.
- **federal_OT** — Other Transaction contracts and Mission Office ISOs (ARPA-H ISOs, NSF Tech Labs OT, DOE Genesis if OT-shaped). Adds research-security disclosures, phased-budget envelopes, mandatory feedback gates.
- **intergovernmental_grant** — Multilateral programs (Horizon Europe, UNESCO, WHO).
- **philanthropic_grant_proactive** — Funders who reach out (Coefficient Giving, Wellcome Leap thrusts).
- **ea_micro_grant** — Effective-altruism-style micro-grants with counterfactual emphasis (EA LTFF, EAIF, Emergent Ventures).
- **vc_investment** — Venture-capital investments (Lux, BEV, 5050, Anthology, IndieBio).
- **venture_builder** — Operator-building model (Deep Science Ventures, Foresite Labs, The Next Sequence).
- **corporate_credit** — Cloud / API / software credits (AWS Activate, Google Cloud AI, Anthropic AI for Science, NVIDIA Inception, Microsoft for Startups).
- **nonprofit_discount** — Free / discounted SaaS or hardware for verified 501(c)(3)s, mostly TechSoup-mediated.

Existing kinds retained: `universal_baseline`, `federal_grant`, `private_grant`, `private_fellowship`, `accelerator`.

#### New funder-metadata fields (F-family additions)
F12 instrument · F13 submission_stages · F14 application_effort · F15 investment_horizon_years · F16 application_required · F17 cost_share_required · F18 indirect_cost_rule · F19 award_period_months · F20 joint_program_partners · F21 funder_process_type · F22 canonical_funder_ref · F23 min_award_usd · F24 max_award_usd · F25 residency_required · F26 residency_location · F27 confidentiality_policy · F28 written_feedback_gate · F29 review_criteria · F30 required_partners_count.

### Changed
- Manifest version bumped `1.0 → 1.1`.
- `extensions` slot family now has 14 IDs (was 12).
- Added `funder_metadata_id: ^F\d{2}$` regex to validation rules.

### Deferred (will land in v1.2)
The following sub-slot additions were identified but not authored yet — listed here so they are tracked. Add when authoring the relevant slot files:
- U03.6 Multimodal data integration (NIH PRIMED-AI)
- U04.5 Magnitude-of-impact threshold attestation (Gates ≥ X, BEV ≥ 0.5 Gt, DRK ≥ 10k lives)
- U06.6 Indirect-cost-rate-cap rendering (CZI 15%, Gates 10%, etc.)
- U07.5 Phase-envelope budgets (per-phase $ caps; NSF Tech Labs, DOE Genesis Phase I/II)
- U08.5 Phase-transition (UG3→UH3 / Phase 1→2) go/no-go criteria
- U11.7 Founder-proximity-to-problem narrative (Fast Forward, DRK)
- U11.8 Postdoc IDP / individualized development plan (Schmidt)
- U12.6 AI-readiness commitment (Bridge2AI)
- U12.7 NIH DMSP-aligned plan (structured 6-element template)
- U13.6 Gender dimension in research content (Horizon Europe)
- U13.7 Community co-design / engagement plan (RWJF, AstraZeneca CHANGE)
- U14.7 ELSI plan (Bridge2AI)
- U16.7 Research-security / NSPM-33 disclosures (federal grants post-2024)
- U17.7 Customer-discovery / human-centered-design plan (NSF Convergence)
- U18.6 Cost-effectiveness model (DALY/QALY/$) (Coefficient Giving, EA Funds)
- U18.7 Global Access policy commitment (Gates Foundation)
- U19.6 LMIC implementation plan (Gates, Wellcome LMIC)
- U20.6 Strategic alignment with corporate funder (J&J JLABS, AWS Imagine)
- A02.4 Multi-PI / Coordinating PI structure
- A03.6 Costing-model declaration (fEC/F&A/OT/flat)
- A03.7 Mentor / nominator-sponsor letter required (Schmidt)
- A03.8 In-residency / location-during-program
- A03.9 Permanent-contract / minimum-PI-effort threshold
- A03.10 State / country / region eligibility list
- A03.11 Revenue cap eligibility
- A03.12 Age cap eligibility (organization or applicant)
- A03.13 Limited-submission (1-per-institution) flag
- A04.6 Demo-video gate
- A04.7 Pitch deck (when required vs. optional)
- A04.8 IRS 501(c)(3) determination letter
- A04.9 Confidentiality / unfiled IP marker
- A04.10 Wet-lab needs / facility specification
- A04.11 Publication acknowledgment template (NSF/NIH joint program)
- A05.4 Funder-process-type rendering

### New canonical funder files needed (deferred to v1.2 — not created yet)
Heavy schema funders without a yaml file yet, ranked by priority based on Cytognosis pipeline:
- **Tier-1 priority:** Wellcome Leap, Wellcome Trust Discovery, NIH Bridge2AI, NIH PRIMED-AI, NSF-NIH Smart Health, NSF Convergence Accelerator, Horizon Europe Cluster 1, ARPA-H PHO, Convergent Research FRO, CZI, Gates Grand Challenges
- **Tier-2 priority:** Schmidt Sciences, ARIA Full Programmes + Opportunity Seeds, AWS Imagine, RWJF, DRK Foundation, Coefficient Giving, EA LTFF, EA Infrastructure, Emergent Ventures, AstraZeneca CHANGE, Fast Forward, UNESCO/WHO Open Science, ARPA-H HSF (companion to PHO)
- **Lightweight templates needed (not full funder files):**
  - `kind: corporate_credit` shared template (covers ~7 funders: AWS Activate, Google Cloud AI Startup, Anthropic AI for Science, NVIDIA Inception, Microsoft+NVIDIA Healthcare, Mixpanel, Google HAI-DEF)
  - `kind: nonprofit_discount` shared template (covers ~20 TechSoup-mediated discount programs)
  - `kind: vc_investment` shared template (covers ~7 VC funders)

---

## [1.0] — 2026-04-23

### Added
- Initial canonical template system.
- 25 slots (U01–U20 + A01–A05) with stable IDs and YAML frontmatter.
- 10 funder files: `heilmeier`, `nih_r01`, `nsf_tech_labs`, `arpah_mission_office`, `doe_genesis`, `astera_residency`, `brains_accelerator`, `foresight_nodes`, `google_impact_challenge`, `yc_nonprofit`.
- Manifest with slot-family declaration, funder registry, render targets, and validation rules.
- Authoritative funder crosswalk matrix (`funder_crosswalk_matrix.md`).
- Canonical template format spec (`canonical_template_format.md`).
- Format conversion decision tree (`format_conversion_decision_tree.md`).
- Heilmeier-core prose authored for U01, U08 (full); U03 and U06 (partial); other 21 slots are stubs.

### Verified
- All 25 slot files structurally valid (frontmatter, H2 parity, ID format).
- 10/10 funder files declare a `google_docs` render target.
- 7 cross-consistency blockers fixed during initial verification.

---

*Notes on versioning:*
- **Slot IDs are immutable** — never renumber after content is authored. New slots get new IDs (U21, U22, U23…).
- **Funder kinds and metadata fields can be added but not removed** without a major bump (1.x → 2.0).
- **Sub-slot IDs** are append-only within a slot — adding U06.7 is fine, renumbering U06.3 to U06.4 is not.
