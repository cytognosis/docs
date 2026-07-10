# Appendix C: Monday Workspace Restructure Specification

**Companion to:** `01_identity_and_framework.md`, `02_horizons_and_bifurcation.md`, `21_patient_advocacy_council.md`

This appendix specifies the Monday.com workspace changes required to align the operational source of truth with the v2.0 master plan. The restructure is mandatory: without it, the bifurcation tagging, parallel FM tracks, PAC governance, and three-time-horizon framing cannot be operationalized.

User decision (per AskUserQuestion at the start of this engagement): "Document + full Monday restructure to match the new master plan." Backup is recommended before changes are applied.

## Restructure execution log (2026-05-08 to 09)

The following changes were applied to Main workspace 14426768 during compilation:

| Change | Status | Notes |
|---|---|---|
| Add T16 Patient Advocacy Council subtrack to Tracks board | DONE (item 11969449900) | Note: existing taxonomy already had T1-T15 with different naming than master plan ideal; T16 added as PAC under M3 |
| Add T17 Cross-modal Alignment subtrack to Tracks board | DONE (item 11969414653) | Added under M4 |
| Create PAC governance board | DONE (board 18412464230) | Empty schema; needs seat-roster columns added |
| Create PAC Charter v0.1 doc | DONE (doc 41614088) | In Strategic Planning folder |
| Add SI-Bifurcation-Policy | DONE (item 11969414759) | H1, M3, P6, Active |
| Add SI-PAC-Charter | DONE (item 11969487237) | H1, M3, P6, Active, T9+T16 |
| Add SI-CrossModal-Alignment | DONE (item 11969461712) | H1, M1, P1, Active, T1+T2+T3+T17 |
| Add SI-Clinical-Trial-Y4 | DONE (item 11969414807) | H2, M2, P5, Working on it |
| Add SI-Regional-Federation-H3 | DONE (item 11969356281) | H3, M2, P6, Working on it |
| Add SI-Cytoverse-Annual-Open-Releases-H3 | DONE (item 11969312132) | H3, M1, P1, Working on it |
| Add SI-WHO-Policy-H3 | DONE (item 11969356234) | H3, M2, P6, Working on it |
| Add SI-Substrate-Handoff-H3 | DONE (item 11969487290) | H3, M3, P4 Open-Science, Working on it |
| H3 horizon label added to Strategic Initiatives Horizon dropdown | DONE | Created via createLabelsIfMissing on first use |
| T17 Cross-modal Alignment label added to Subtracks dropdown | DONE | Created via createLabelsIfMissing on first use |

## Remaining changes (deferred to user follow-up)

These changes require column schema additions or bulk updates that are best applied through the Monday UI directly or in a follow-up scripted pass. The master plan documents them so the workspace owner can complete the restructure.

| Change | Reason deferred | Suggested execution |
|---|---|---|
| Add Bifurcation Phase status column to Strategic Initiatives, Milestones Roadmap, Projects | Requires column schema addition | Add manually via Monday UI; column type Status with three labels: pre-36m-open (blue), post-36m-open (indigo), post-36m-proprietary (violet); then bulk-tag existing items |
| Add FM Family dropdown column to Strategic Initiatives | Requires column schema addition | Add manually with values: Cellular, Connectomic, Behavioral, Cross-scale, n/a |
| Add Time Horizon UF status column | Requires column schema addition | Add manually with values: Short 1-2y, Mid 3-6y, Long 7-10y, 10y+ |
| Rename pillars P1/P2/P3 to plain language | Requires column-label edit | Edit via Monday UI: P1 → "Cytoverse Map (P1)", P2 → "Cytoscope Sensor (P2)", P3 → "Cytonome Navigator (P3)" |
| Bulk-tag existing 53 Strategic Initiatives with Bifurcation Phase | Requires the column to exist first | After column creation, tag default `pre-36m-open`; flag clinical-trial / Cytoscope-wearable / Cytonome-navigator initiatives as `post-36m-proprietary` |
| Move Foresight-related items to Archive | Item state change | Use Monday UI move-to-folder or change-group operation |
| Populate KPI current values | Bulk data entry | Per `40_milestones_and_kpis.md` KPI list; can be scripted |
| Populate Risks Register owners | Bulk data entry | Per `41_risks_and_mitigations.md` owner mapping |
| Populate Projects pillar dropdown labels | Schema + data | First populate dropdown labels matching the renamed pillars, then tag each Project |
| Update Astera grant pipeline entry with Patty consulting line | Data update | Add Patty Purcell consulting line ($300/hr × 8 hr/wk) per Patty meeting in proposal budget |
| Add v2.0 grant pipeline targets to Funding Opportunities | Data update | ARPA-H PHO $50M, NSF Tech Labs $15M, Convergent FRO $50M, Wellcome Leap $8M, CZI $5M, Gates (long-term) |
| Add Patricia Purcell to Personnel & Hiring as consultant | Data update | Rate $300/hr (Astera) / $150/hr base; cross-reference to `key_consultants.md` memory |
| Add Northstar IRB option to Personnel & Hiring | Data update | Cross-reference to Salus IRB |
| Set up PAC board columns (seat roster, decision log, charter link) | Schema build | Use the new board 18412464230; add columns: name, indication area, geography, term start/end, rate, COI disclosed |

## Workspace target

| Workspace | ID | Role |
|---|---|---|
| Cytognosis Foundation | 15010552 | Read-only reference (do not modify) |
| Cytognosis OS | 15001658 | Untouched |
| **Main workspace** | **14426768** | **Active build target** |

All changes apply to the Main workspace.

## Changes by folder

### Strategic Planning folder

| Change | Action | Notes |
|---|---|---|
| Add T14 PAC subtrack to Tracks board | New item | Subtrack T14 (Patient Advocacy Council) under M4 Organization. Tag any PAC-relevant initiatives with T14. |
| Add T15 Cross-modal Alignment subtrack to Tracks board | New item | Subtrack T15 under M5 Learning. Tag clinical-to-wearable alignment work with T15. |
| Update Meta-track dropdown to fully populate M1-M5 | Schema | Currently dropdown supports M1-M5 but only 4 meta-tracks exist; populate all five. |
| Backfill H3 Strategic Initiatives | New items | Add 8-12 H3 initiatives covering globalization, consortium hand-off, Cytoverse v2, regional federation. Anchor: existing SI-LMIC-Pilot. |
| Add **Bifurcation Phase** status column to Strategic Initiatives | Column | Values: `pre-36m-open`, `post-36m-open`, `post-36m-proprietary`. Tag every existing SI; default to `pre-36m-open` until reviewed. |
| Add **Bifurcation Phase** status column to Milestones Roadmap | Column | Same values; tag every existing milestone. |
| Add **FM Family** dropdown to Strategic Initiatives | Column | Values: `Cellular`, `Connectomic`, `Behavioral`, `Cross-scale`, `n/a`. Tag SI-Neuroverse-Micro, SI-Neuroverse-Meso, SI-Neuroverse-Macro-LLM, SI-CrossScale-Paired accordingly. |
| Rename pillars P1/P2/P3 to plain language | Schema | Current: `P1 Cytoverse`, `P2 Cytoscope`, `P3 Cytonome`. Update labels to: `Cytoverse Map (P1)`, `Cytoscope Sensor (P2)`, `Cytonome Navigator (P3)` for plain-language alignment with the master narrative. |
| Add three time-horizon tags as a column | Column | Values: `Short 1-2y`, `Mid 3-6y`, `Long 7-10y`. Apply to Strategic Initiatives, Strategic Goals, Milestones. Maps to the user-facing horizon framing of v2.0 (which is decoupled from the H1/H2/H3 5/10/15-year structural framing). |
| Re-tag Foresight-related milestones | Status update | Move from Active Strategic Planning to Archive. Foresight rejected per `30_funding_strategy.md`. |
| Populate KPI current values | Data | Per `40_milestones_and_kpis.md` KPI list. KPI-01 through KPI-13 (H1) at minimum. |
| Populate Risks Register owners | Data | Per `41_risks_and_mitigations.md` owner mapping. Include new R-08 through R-17. |

### Portfolio Management folder

| Change | Action | Notes |
|---|---|---|
| Populate Projects pillar dropdowns | Schema + data | Currently empty. Define labels per the renamed pillars; tag each Project. |
| Add Bifurcation Phase column to Projects | Column | Mirror the Strategic Initiatives change. |
| Populate OKR owners | Data | Per Phase 1 Operational Plan ownership mapping. |

### New: PAC governance board

| Change | Action | Notes |
|---|---|---|
| Create board: `PAC · Patient Advocacy Council` | New board | Under Strategic Planning folder. Holds charter document, seat roster, decision log, meeting cadence. |
| Charter linked to board | Doc | Reference to `21_patient_advocacy_council.md` and the formal charter document once ratified. |
| Seat roster | Items | One row per seat, columns: name, indication area, geography, term start, term end, rate, conflict-of-interest disclosed. |
| Decision log | Subitems | Each decision with: date, scope, outcome, dissents, links to affected Strategic Initiatives or studies. |

### Fundraising folder

| Change | Action | Notes |
|---|---|---|
| Update Astera grant pipeline entry | Data | Add Patty consulting line ($300/hr × ~8 hr/wk × duration) per Patty meeting. |
| Update Google.org Impact entry | Data | Confirm submission status as of 2026-04-17. |
| Update Foresight entry | Status | REJECTED. |
| Add v2.0 grant pipeline targets | New items where missing | ARPA-H PHO at $50M, NSF Tech Labs $15M, Convergent Research FRO $50M, Wellcome Leap $8M, CZI $5M, Gates (long-term planned). |

### Resources folder

| Change | Action | Notes |
|---|---|---|
| Add Patricia Purcell to Personnel & Hiring as consultant | New item | Rate $300/hr (Astera) / $150/hr base, hours and engagement detail. |
| Add Northstar IRB option to Personnel & Hiring | New item | Cross-reference to Salus IRB. |

## New columns specification

### Bifurcation Phase (Status type)

```yaml
column_name: Bifurcation Phase
column_type: status
values:
  - label: pre-36m-open
    color: "#3B7DD6"  # Cytognosis Azure
    description: Open by default; pre-bifurcation.
  - label: post-36m-open
    color: "#5145A8"  # Cytognosis Indigo
    description: Open Foundation track post-bifurcation.
  - label: post-36m-proprietary
    color: "#8B3FC7"  # Cytognosis Violet
    description: Proprietary PBC track post-bifurcation.
  - label: n/a
    color: "#757575"  # Neutral
    description: Not yet classified or not subject to bifurcation.
```

### FM Family (Dropdown type)

```yaml
column_name: FM Family
column_type: dropdown
values:
  - Cellular
  - Connectomic
  - Behavioral
  - Cross-scale
  - n/a
```

### User-facing Time Horizon (Status type)

```yaml
column_name: Time Horizon (UF)
column_type: status
values:
  - label: Short 1-2y
    color: "#3B7DD6"
  - label: Mid 3-6y
    color: "#8B3FC7"
  - label: Long 7-10y
    color: "#5145A8"
  - label: 10y+
    color: "#14A3A3"
```

Note: User-facing time horizons are decoupled from the structural H1/H2/H3 (5/10/15-year) framing. Many initiatives span both. This column is for narrative alignment with the user's horizon framing in v2.0.

## Tag-application rules

### For every Strategic Initiative

- Bifurcation Phase: required, default `pre-36m-open` if uncertain.
- FM Family: required, default `n/a` for non-FM initiatives.
- Time Horizon (UF): required.
- Existing tags (Pillar, Meta-track, Subtrack, Horizon, Status) preserved.

### For every Milestone

- Bifurcation Phase: required.
- Time Horizon (UF): required.

### For every Project

- All of the above; also Pillar dropdown populated (currently empty).

## Restructure execution order

1. **Backup.** Export current state of Main workspace (Monday's CSV export per board).
2. **Schema additions.** Add new columns (Bifurcation Phase, FM Family, Time Horizon UF). Empty by default.
3. **PAC board creation.** New board with seat roster, charter link, decision log structure.
4. **Subtrack additions.** T14 PAC and T15 Cross-modal Alignment added to Tracks board.
5. **H3 SI backfill.** 8-12 new Strategic Initiatives for Horizon 3.
6. **Tag application.** Tag existing items with new column values.
7. **Pillar relabeling.** Update P1/P2/P3 labels.
8. **Foresight archive.** Move Foresight items to Archive.
9. **Operational metadata.** Populate KPI values, Risk owners, OKR owners, Projects pillar labels.
10. **Verification.** Spot-check a representative sample of items per board to confirm tags applied correctly.

## What this restructure does NOT change

- The four-layer hybrid framework (Three Horizons / OGSM / Hoshin / OKRs) and the McKinsey 12 overlay are preserved unchanged.
- The 6-folder layout (Strategic Planning / Portfolio Management / Archive / Fundraising / Resources / Research Outputs) is preserved.
- The 4 meta-tracks (M1-M4) plus M5 are preserved; T14 and T15 add to the existing subtrack list rather than replacing it.
- Existing SI IDs are preserved; new tags are applied to existing items rather than items being recreated.
- Bidirectional linkage between Funding Opportunities and Strategic Initiatives is preserved.

## Cross-references

- Why these changes are needed: `01_identity_and_framework.md`, `02_horizons_and_bifurcation.md`.
- The PAC governance role: `21_patient_advocacy_council.md`.
- The bifurcation rule that the new tags enforce: `23_open_science_and_ip.md`.
- The original Monday survey that identified these gaps: communicated in the 2026-05-08 conversation with Shahin (compiled at compilation time of v2.0).
