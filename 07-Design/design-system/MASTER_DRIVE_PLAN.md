# Master Drive Plan: Design System Merge (v11)

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: designers, stakeholders
> **Tags**: `design`, `design-system`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

**Updated:** 2026-07-08. **Owner:** Shahin (driving via Cowork). **Backbone doc:** `02_review/DESIGN_SYSTEM_MERGE_REVIEW_2026-07-08.md`.

## Done (2026-07-08 session)

- [x] Moved the three zips from `~/Downloads` to `00_source_zips/` (md5-verified, originals deleted; four older DS zips left in Downloads untouched)
- [x] Extracted all three systems to `01_extracted/` (mine 457 files, ali_old 83, ali_latest 129)
- [x] Full three-way comparison written (`02_review/raw_comparison_designsystems.md`)
- [x] Full context sweep written: 8 prior Claude Design prompts, structure standards, website token lineage, branding repo status (`02_review/raw_context_inventory.md`)
- [x] Merge review + decisions D1-D4 written (`02_review/DESIGN_SYSTEM_MERGE_REVIEW_2026-07-08.md`)
- [x] Claude Design merge prompt ready (`03_next_prompts/prompt_merge_v11.md`)
- [x] Antigravity branding-repo recovery prompt ready, gated on D2 (`03_next_prompts/antigravity_branding_recovery.md`)
- [x] Graft bundle built for Claude Design attach (`04_graft_bundle/v11_grafts_2026-07-08.zip`, 58 files)
- [x] Newest logo (July 2026) audited against tokens and bundled; merge prompt extended with Phase 2 (logo family, favicons, app icons, slide assets, 48-icon set)

## Key facts (plain language)

- Brand primitives never forked; Shahin's and Ali's latest systems share identical colors, gradients, and fonts. Conflicts are confined to semantic aliases, one spacing step, and two easing curves, all resolved in the review.
- Ali_old is Ali's personal brand system, not Cytognosis; archived as reference only.
- Ali_latest bundles Yar (separate product); v11 removes it (D1).
- Branding repo currently holds CytoStyle (Ali's unrelated MUI library); pre-replacement Cytognosis content is recoverable from git (D2, needs Ali conversation).
- The live `brand-identity` skill that current Cowork sessions load is an older lineage: canonical violet `#8B3FC7` but a different signature gradient (`#8B3FC7 -> #5A95E8 -> #E0309E` vs canonical `#3B7DD6 -> #8B3FC7 -> #5145A8`) and a 9-file reference set vs the 12-file v10 set. It must be regenerated from v11 via cyto-skills after the merge.

## Progress log

- DONE 2026-07-08: merge ran (v11.0.0 audited: 5/3/1) -> Revision 1 + Phase 2 ran (v11.1.0 audited: 9 pass / 4 partial / 3 fail). Assets verified excellent; 3 ship-blockers found and falsely self-reported. Revision 2 prompt written.
- DONE 2026-07-09: research wave (neurodiverse corpus, canonical vocabulary, profiles/platform critique, artifact-pack recovery) + finalization synthesis. Backbone eval: `02_review/FINALIZATION_PLAN_2026-07-09.md`. v11.1.1 export was NOT in Downloads (download did not land); Revision 2 items folded into Revision 3 preflight so nothing is lost.
- DONE 2026-07-10: Revision 3 ran; v11.2.0 export landed and audited (83%: Helix purged, 3 profiles, warm default, CrisisBanner/ConsentPrompt in, motion gated). Read the March 2026 Google Brand Guide + cytoskills canon; three-way reconciliation done. NEW backbone: `02_review/FINALIZATION_PLAN_v2_2026-07-10.md`. Ship-blocker: 1 diagnosis-implying line in voice ref (self-report falsely claimed fixed). NEW finding: Helix still a product in 5 cytoskills files. Canon settled (v11+cytoskills win vs stale Google doc): gradient azure-violet-indigo, magenta accent-only, Newsreader, 1.6px icons.

## EXECUTED 2026-07-10 (autonomous drive via the Claude-in-Chrome bridge)

- [x] **v11.2.1 PUBLISHED** in Claude Design, and set as the team **Default** design system (both confirmed green via screenshot).
- [x] **cytoskills Helix cleanup COMMITTED** (commit 2ecd727, as Shahin): Helix removed as a product across 6 files, helix-model.png archived (both skills), diagnosis-implying voice example replaced, dna-helix icon stroke 1.75 -> 1.6. Verified: zero product-Helix, only biology dna-helix remains.
- [x] **Google Brand Guide doc updated in place** (13 find/replace corrections, no new doc per D11): signature gradient -> azure/violet/indigo; "Primary Colors" -> "Identity Triad and Accent Colors" + magenta reframed to alerts-only; Source Serif Pro -> Newsreader; icons -> 1.6px custom 48-set bundled primary; One Dark Pro -> Cytognosis Night theme; footer -> v3.0 / July 2026; "Aligned to Design System v11.2.1" note added. Residuals (cosmetic, noted): header table "Version 2.0" + "Effective March 2026" cells (table-cell, not safely targetable via find/replace); secondary gradients (innovation/vitality/data/healthspan) still hold older values, finer follow-up.
- [x] **Logo/icon generation DONE + verified** (via bridge): full family in light/dark pairs, product glyphs (Cytoverse/Cytoscope/Cytonome), logos.card.html contact sheet, icon set reconciled to real 64-icon / 10-family line+solid currentColor set, check_design_system clean. Two flags: 06_iconography.md reconciled from an aspirational set; horizontal wordmark keeps tight right margin (say if you want more breathing room).
- [x] **Live cytognosis.org inspected**: aligned on core palette (warm #F4F2EF, lp-violet #6E5BD1, ladder #FAF8F2/#ECE9E4). Deltas to fold into the Website Template: Space Grotesk weight 500 display (not Bold 700), near-ink #23232B body, generous 96/48 spacing + "one idea per viewport" airiness, uppercase-mono eyebrows. (Yar + Neuroverse are live top-level nav sections.)
- [x] **TWO-TRACK plan authored** at `05_tracks/`: TRACK-A_BRANDING-REPO_PLAN.md, TRACK-B_WEBSITE_PLAN.md, TRACKS_ORCHESTRATION_AND_RELOCATION_2026-07-10.md, TRACKS-STATUS-BOARD.md (+ simple/). Contract = the Website Template (DS -> Template -> website). Relocation map + multi-agent coordination protocol included (user executes moves).

## Remaining (ordered)

1. Verify the logo/icon run output (bridge); then send the templates + backgrounds + VS Code theme run (`prompt_google_and_artifact_templates.md`), all light/dark pairs.
2. Regenerate the separate `brand-identity` skill (vault 07-Design) from v11.2.1.
3. Minor follow-ups: cytoskills "Version 10.0" -> 11.2.1 stamp sync; Google doc header version cell + secondary gradients.
4. Relocation: guideline -> docs repo `07-Design/` (needs docs repo mounted); tokens/assets/themes -> `branding/design-system/` + `branding/themes/` **HARD-GATED on branding-repo recovery = the Ali conversation** (CytoStyle currently occupies the repo). This is the one thing that blocks "everything done."
5. Profiles settlement + a11y re-audit; interface templates re-pointed + built.

## Next actions (ordered; backbone = FINALIZATION_PLAN_v2_2026-07-10.md)

1. **Run Revision 4** (`03_next_prompts/prompt_v11_revision_4_publish_ready.md`): NOW COMPREHENSIVE. Publish-blockers (diagnosis copy, iconography README, Neuroverse link, oxlint) PLUS all 26 neurodiverse fixes from `raw_neurodiverse_compliance_v11_2.md` Section 3 (contrast to 7:1 on patient-facing + hero text, kill infinite motion loops, 16px floor in dashboard/Clinical, one focus ring, ShowMore component, wire CrisisBanner/ConsentPrompt, anchor person-first + Flesch-Kincaid + BLUF, self-host fonts, real citations). Targets v11.2.1. Then re-audit (target >=44/45) and tick Published. Gradient D10 CONFIRMED keep-current.
2. **Update the Google Brand Guide doc in place to v3.0** (D11): apply the 4 canon corrections + absorption additions. On Shahin's go. (Do NOT create a new doc; URL is referenced by 3 companion docs.)
3. **cytoskills Helix cleanup + canon sync** (`03_next_prompts/cytoskills_helix_cleanup_workorder.md`): 5 files + archive helix-model.png + fix diagnosis copy + version sync after publish.
4. **Regenerate the separate `brand-identity` skill** (vault 07-Design) from v11.2.1 (still on v8 gradient).
5. **Logo/icon curation** (`prompt_logo_icon_curation.md`) then **Google templates + artifact pack** (`prompt_google_and_artifact_templates.md`): Google Docs template, letterhead, Slides deck template, meeting + social backgrounds, VS Code theme family. ALL as matched light/dark pairs. Stage under a new `03_artifacts/`.
6. **Relocate**: guideline -> docs repo `07-Design/` (no blocker); tokens/assets/themes -> `branding/design-system/` + `branding/themes/` (BLOCKED on branding-repo recovery / Ali). Archive this working folder only after content lands in target repo.
7. **Profiles settlement + accessibility re-audit**; **branding repo recovery** (Ali gate); **interface templates** re-pointed to v11.2.1 + built.

## Decisions

| # | Decision | Status |
|---|---|---|
| D1 | Yar out of the design system | Done (confirmed absent) |
| D2 | Restore branding repo, quarantine CytoStyle to its own repo | **Needs Ali conversation + dependency check** |
| D3 | Adopt Ali's semantic token values wholesale | Done (in v11) |
| D4 | Version single semver | Done (v11.x) |
| D5 | Profiles: Foundation, Clinical, Research (fold Lab in) | Recommended; in Revision 3 |
| D6 | Warm paper as default surface, dark opt-in | Recommended; in Revision 3 |
| D7 | Body text floor 16px | Recommended; in Revision 3 |
| D8 | Standardize "GPS for Human Health" | Recommended; in Revision 3 |
| D9 | Restore therapeutic citations from git into ACCESSIBILITY.md | Recommended; in Revision 3 |

## Risks

- Silent visual breakage when porting old artifacts (inverted `--bg-*` semantics); mitigated by the changelog migration table.
- Adopted `--fg-*` ramp is lower-contrast; accessibility re-audit is action 4's prerequisite inside the merge prompt (flagged pairs).
- CytoStyle may have production consumers; Phase 1 dependency check runs before anything moves.
