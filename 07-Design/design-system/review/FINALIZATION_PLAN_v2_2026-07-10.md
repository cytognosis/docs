# Design System Finalization Plan v2

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: designers, stakeholders
> **Tags**: `design`, `design-system`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

**Date:** 2026-07-10. **Supersedes:** `FINALIZATION_PLAN_2026-07-09.md`. **Reading time:** about 7 minutes.
**If you only read one thing:** the v11.2.0 export is 83% done and close to publish-ready; one two-sentence copy fix stands between it and publishing. The bigger news is that the same brand canon lives in three places (the v11 export, the cytoskills skills, and the March 2026 Google doc), and they disagree on four identity values. The current, correct values are settled (v11 and cytoskills agree); the Google doc is simply stale. One decision is yours: the hero gradient.

---

## 0. BLUF

- **v11.2.0 export:** structurally strong (Helix purged, three profiles, warm default, CrisisBanner and ConsentPrompt added, motion gated). One ship-blocker: a "good example" line in the voice reference still implies diagnosis, and the self-report falsely claims it was fixed. Two-sentence fix (Revision 4).
- **Canon is now resolved across sources.** Signature gradient, magenta's role, accent font, and icon stroke are settled in favor of the current v11 and cytoskills values. The Google doc (March 2026) is outdated on all four and needs updating, not defending.
- **New problem the design work did not cover:** Helix still ships as a fake fourth product in five cytoskills skill files (with a `helix-model.png` asset). Those skills drive your day-to-day content generation, so this must be fixed there too, separately.
- **Consolidation home is decided:** the finalized guideline goes to the docs repo `07-Design/`; the production tokens and assets go to `branding/design-system/`, but that write is blocked until the branding repo is recovered from CytoStyle (the Ali conversation).

---

## 1. What is DONE (verified in v11.2.0)

Helix purged from the entire export (zero live occurrences); three-product architecture correct on both landing pages; three profiles with Lab folded into a density toggle; CrisisBanner and ConsentPrompt components shipped with full docs and registered; warm paper is the default surface; motion gated behind reduced-motion; body floor 16px reconciled; profiles fully tokenized; archived logos no longer referenced live; VERSION and SKILL.md both 11.2.0; the corrected logo family, favicons, app icons, social assets, and 48+48 icons from earlier revisions all intact.

## 2. What NEEDS REVISION

### 2a. Publish-blocker (Revision 4, tiny)

`references/02_voice_and_tone.md:88-93` still ships the diagnosis-implying "good" example ("Our AI analyzes your cells... finding patterns that signal disease..."), which contradicts your non-diagnostic positioning, and a contradicting "does not diagnose" line sits five lines below it. The changelog and self-report claim this was fixed; it was not. Fix now, before this system generates any public or funder copy.

### 2b. Cosmetic (fold into Revision 4, non-blocking)

`README.md` iconography section still says Phosphor/Feather at 2px (the shipped set is the 1.6px custom 48-icon set); the landing page Neuroverse nav link is a dead `href="#"` with no section; `_adherence.oxlintrc.json` regained 2 em dashes and never got the 4 profile fonts added; the therapeutic evidence appendix defers its citations; REVISION3_REPORT.md carries two false claims (a chromosome-icon rename and phantom bundle residue). None block publishing.

### 2c. cytoskills Helix cleanup (separate work order)

Helix appears as a named product in five cytoskills files plus shipped `helix-model.png` assets. This is the reason "Helix is gone" is true of the export but not of the system. Fix per `cytoskills_helix_cleanup_workorder.md`. The voice reference in cytoskills likely carries the same diagnosis-copy issue as 2a; grep and fix both in the same pass.

## 3. The three-source reconciliation (settled)

| Value | Google doc (Mar 2026) | Current canon (v11 + cytoskills, agree) | Verdict |
|---|---|---|---|
| Signature gradient | violet to bright-azure to magenta `#8B3FC7 → #5A95E8 → #E0309E` | azure to violet to indigo `#3B7DD6 → #8B3FC7 → #5145A8` | **Current canon** (see decision D10) |
| Magenta | listed as a 4th primary | accent only, never identity or logo | **Current canon** |
| Accent font | Source Serif Pro | Newsreader default; Source Serif Pro kept as Clinical-profile default | **Current canon** |
| Icon set | 2px Phosphor/Feather | 1.6px custom 48-icon set; Phosphor/Feather re-stroked gap-fill | **Current canon** |
| Neutrals | Deep Night `#13131F` | 8-step scale (abyss `#0A0A14` → deep `#13131F` → ...) | reconcile doc to the shipped scale |

The Google doc still has genuinely valuable content to keep: the full messaging framework, taglines, audience and funder tone tables, boilerplate, the Google Docs and Slides template specs, email/social/print specs, and the five design motifs. The absorption map (`raw_v11_2_audit_and_absorption.md` section 4) says exactly which of these to fold into the design system and which stay as doc-only rendering guidance.

## 4. Decisions (recommended defaults; I proceed unless you redirect)

| # | Decision | Recommendation | Note |
|---|---|---|---|
| D10 | Hero signature gradient | **CONFIRMED 2026-07-10: keep current canon (azure to violet to indigo).** Shahin approved. The Google doc's violet-to-magenta version is retired to a historical note. | Matches the shipping website, the five current canon files, and the calm/all-cool science rationale. |
| D11 | The Google guideline doc | **Update in place, do not create new.** | It is the URL three companion docs already link to. I have the exact change list ready; on your go I apply the four canon corrections plus the absorption additions, and add a version bump to v3.0 aligned to v11.2.0. |
| D12 | cytoskills Helix + version | **Fix Helix now; sync the "Version 10.0" stamps to v11.2.0 after publish.** | Skills drive daily content; the stale product is higher-risk there than in the export. |
| D13 | Logo/icon creation | **Curate and regenerate as matched light+dark pairs per surface** (slides, web, phone, desktop, dashboard), per `prompt_logo_icon_curation.md`. | Every key asset ships as a dark+light pair designed together. |

## 4b. Neurodiverse compliance (verified 2026-07-10, now driving Revision 4)

Ran the full 45-item research checklist against the final v11.2.0 export (`raw_neurodiverse_compliance_v11_2.md`). Score: 23/45 clean, ~66% with partials. Revision 3 genuinely fixed the known problems (parallax opt-in, Clinical magenta contradiction, warm surfaces, data-profile + skip links, prefers-contrast layer, 16px token). But the fresh contrast math exposed a more serious, previously unmeasured issue: patient-facing Clinical body text and the landing hero sentence compute to ~4.7:1 and ~3.0:1, below the 7:1 AAA the system promises that exact audience, and decorative signal-node motion still loops unconditionally. Four principles (progressive disclosure, BLUF doc convention, person-first, Flesch-Kincaid target) are not anchored anywhere in the system. All 26 exact fixes are grouped in that file's Section 3 and are now fully incorporated into Revision 4 (`prompt_v11_revision_4_publish_ready.md`), and the calm standard is written into the logo/icon and template/artifact prompts too, so calm-by-design runs through every downstream deliverable, not just the tokens. Decision D14: the neurodiverse standard is system-wide and non-negotiable, patient-facing surfaces get the strictest contrast and calm.

## 4c. Revision 4 result + the Clinical contrast decision (2026-07-10)

Revision 4 (v11.2.1) reported complete with computed ratios and three honest limitations (audit files not in export; the 2 oxlint em dashes are compiler-emitted, font fix is at source and survives; font binaries not yet uploaded, ready `@font-face` block staged). Report is credibly more honest than prior revisions, but NOT YET VERIFIED against files: the v11.2.1 zip has not landed in Downloads. Verify on arrival (target >=44/45, confirm the 4 contrast pairs, infinite-loop removal, CrisisBanner/ConsentPrompt wiring, ShowMore).

**D15, Clinical body contrast (open question the tool surfaced): KEEP the soft `#4A4A66` (7.6 to 8.5:1), do not go near-black.** Rationale is science-backed, not just aesthetic: the dyslexia, scotopic-sensitivity, and Irlen research in the org's own corpus warns AGAINST maximum black-on-paper contrast (glare, text "swimming"), and the system already bans pure black and mandates calm-by-default. `#4A4A66` clears AAA (the promise) while staying calm for the most anxiety-sensitive audience. Serve maximum contrast on demand instead: ensure the existing `prefers-contrast: more` layer escalates Clinical body to near-black (~`#1E1E32`, ~14.6:1) for users who request it. That gives soft-AAA by default and maximum contrast for those who need it, no compromise. Fold the prefers-contrast Clinical escalation into the verification pass if not already present.

## 5. Sequence to finish (ordered)

1. **Revision 4** (fix 2a + 2b) in the current or a fresh Claude Design chat; re-audit; then tick Published. `prompt_v11_revision_4_publish_ready.md`.
2. **Update the Google doc** to v3.0 (D11), on your go.
3. **cytoskills Helix cleanup + voice fix** (D12), `cytoskills_helix_cleanup_workorder.md`.
4. **Regenerate the separate `brand-identity` skill** from v11.2.0 (still on the v8 gradient).
5. **Logo/icon curation run** (D13), then **Google templates + artifact pack** (`prompt_google_and_artifact_templates.md`): Google Docs template, letterhead, Slides deck template, meeting and social backgrounds, VS Code theme family, all as light+dark pairs.
6. **Relocate** finalized outputs (Section 6).
7. **Profiles settlement + accessibility re-audit;** then **branding repo recovery** (Ali gate); then **interface templates** re-pointed and built.

## 6. Relocation (where finalized work lands; full detail in `raw_canon_and_relocation.md` Part 3)

- **Consolidated guideline (prose):** docs repo `07-Design/`, with a plain-language Obsidian companion. No blocker.
- **Production tokens, CSS, assets, templates, themes:** `branding/design-system/` and `branding/themes/`. **Blocked** until the branding repo is recovered from CytoStyle (Ali conversation); stage under a new `03_artifacts/` subfolder here meanwhile.
- **This working folder** (`design-system-merge-2026-07/`): archive with a forward link only after the design-system content lands in its target repo; do not archive yet.
- **Naming:** docs follow the `cytognosis-doc` skill (metadata header + Obsidian companion); exported docs `[Type]-[Topic]-[Version]-[Date]`; branding semver per `governance.md`.

## 7. Sources

`raw_v11_2_audit_and_absorption.md`, `raw_canon_and_relocation.md`, `reference_google_brand_guide_v2_march2026.md`, plus the 07-09 research set (`raw_neurodiverse_research_inventory.md`, `raw_vocabulary_alignment.md`, `raw_profiles_usecases_critique.md`, `raw_artifact_pack_spec.md`).
