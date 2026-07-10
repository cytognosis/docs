# Cytognosis Design System v11.1.0 Re-Audit

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: designers, stakeholders
> **Tags**: `design`, `design-system`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

Scope: `01_extracted/v11_1`, diffed against `01_extracted/v11`, evaluated against `03_next_prompts/prompt_v11_revision_1.md`.
Date: 2026-07-08.

## 1. Scoreboard

| # | Item | Verdict |
|---|---|---|
| 1 | Copy fixes, "breakthrough" sweep | PASS |
| 2 | Em dashes | FAIL |
| 3 | Font allowlist | FAIL |
| 4 | Tokenization (templates/, profiles/) | PARTIAL (4a pass, 4b fail) |
| 5 | Small fixes (README, icons README, SKILL.md showcase) | PARTIAL |
| 6 | Phase 1 regression greps | PARTIAL |
| 7 | Diff tokens/styles/components/uploads vs v11 | PASS |
| 8 | Master mark SVG corrections | PASS |
| 9 | Logo family (wordmark/mono/reversed/simplified/archive) | PARTIAL |
| 10 | Favicons, app icons, social, slides | PASS |
| 11 | Template re-pointing | PASS |
| 12 | Icons (48 line + 48 solid) | PASS |
| 13 | Non-token color sweep, all new SVGs | PASS |
| 14 | PHASE2_REPORT.md content and render evidence | PASS |
| 15 | CHANGELOG truthfulness | FAIL |
| 16 | Unexpected/leftover files | PASS |

Count: 9 PASS, 4 PARTIAL, 3 FAIL.

## 2. Evidence per item

### 1. Copy fixes and "breakthrough" sweep — PASS

- `guidelines/colors-gradients.card.html:27`: `<div class="use">Scientific rigor to discovery. Research sections.</div>`. Matches required text exactly.
- `references/01_brand_foundation.md:36`: `2. **Health Equity.** Universal access to advanced health technologies.`. Matches required text exactly.
- Full "breakthrough" sweep (case-insensitive, outside `uploads/`):
  - `README.md:79`, `guidelines/brand-voice.card.html:50`, `SKILL.md:30`, `references/02_voice_and_tone.md:60`, `WRITING.md:114` and `:128`: all are banned-word-list citations (explicitly whitelisted by the audit brief). Classified CITATION.
  - No other live matches found anywhere else in the tree outside `uploads/`.
- Bonus sweep for "revolutionary" / "cure" / "game-changing" (not explicitly required but same failure mode): only found inside the same banned-word-list citations plus one explicit bad-example callout (`references/02_voice_and_tone.md:89`, `"> Revolutionary Healthcare Technology ← bad"`), which is a labeled anti-example, not live copy. All CITATION.

### 2. Em dashes — FAIL

- `diff v11/_adherence.oxlintrc.json v11_1/_adherence.oxlintrc.json` returns **no diff**. The file is byte-identical to v11. The two em dashes the prompt named are still present verbatim:
  - Line 36: `"message": "Raw hex color — use a design-system color token via var()."`
  - Line 40: `"message": "Raw px value — use a design-system spacing token via var()."`
- Counts across the tree (outside `uploads/`): `_ds_bundle.js` 31 em dashes (waived, tool-generated, acceptable), `_ds_manifest.json` 2 em dashes (both inside auto-generated `subtitle` fields with a hash-based namespace, consistent with "platform regenerates it"; acceptable per the prompt's conditional clause), `_adherence.oxlintrc.json` 2 em dashes (**not acceptable**, this file is hand-authored lint config with explicit line-level fix instructions, not a generated bundle/manifest).
- `CHANGELOG.md:18` claims: "Replaced em dashes in the `_adherence.oxlintrc.json` lint messages with periods." **This claim is false.**
- `CHANGELOG.md:36-41` (the waiver note) claims `_adherence.oxlintrc.json` "is likewise platform-regenerated, so its lint-message and allowlist edits are applied in-tree." **Both halves of this sentence are false**: the file is not platform-regenerated (it is the project's own hand-authored lint config, and the prompt gave it precise manual edit instructions), and no edits were applied in-tree (confirmed byte-identical to v11).

### 3. Font allowlist — FAIL

Direct consequence of item 2: since `_adherence.oxlintrc.json` was never touched, neither required extension was made.
- `x-omelette.fontFamilies` (line 566-573) still lists only the original six: Atkinson Hyperlegible, Inter, JetBrains Mono, Lexend, Newsreader, Space Grotesk. IBM Plex Sans, IBM Plex Mono, Source Serif Pro, and Recursive are absent.
- The font-family `no-restricted-syntax` regex (line 43) is unchanged: `(?:Inter|Newsreader|JetBrains Mono|Space Grotesk|Lexend|Atkinson Hyperlegible)`. Same four fonts absent.
- This is not a paperwork gap: `profiles/profiles.css` and `profiles/README.md` actively reference IBM Plex Sans/Mono and Source Serif Pro (confirmed via grep), so the adherence config now actively mis-flags legitimate, shipped profile content.
- `CHANGELOG.md:19-21` claims the allowlist was extended "so the profile fonts validate." **False**, for the same reason as item 2.

### 4. Tokenization — PARTIAL

**4a. templates/ — PASS (one trivial residual).**
- Built the allowed hex set from `tokens/colors.css`: 96 distinct 6-digit hex values.
- Diffed all four template HTML files against v11. All 12 distinct off-token values the revision needed to fix (`#1E1E2E`, `#2A2A3D`, `#FAFAFC`, `#F5F5FA`, `#E8E5F2`, `#6A6A84`, `#F4B942`, `#E5E5EC`, `#4A4A66`, `#F0F0F5`, `#E0E0E8`, `#8989A0`) were converted to `var(--token)`, matching `PHASE2_REPORT.md` section 4's table exactly. This reconciles with the changelog's "12 distinct values" claim (the prompt's original estimate of "14" was just a pre-fix estimate).
- Gold handling: `--gold` in `deck.html:25` now reads `var(--cg-lp-yellow)`. No `--template-gold` was defined anywhere (confirmed via tree-wide grep). This is one of the two prompt-approved outcomes, and it is documented in both `CHANGELOG.md:22-25` and `PHASE2_REPORT.md` section 4.
- Residual: `templates/deck-stage.js:65,135` still has `background: #000;` (pure black, no corresponding design token exists in the system by design). This is pre-existing (byte-identical to v11, confirmed via diff), not part of the 12 values the prompt flagged, and is internal shadow-DOM stage chrome (a fixed backdrop behind the rendered slide canvas), not brand-visible content. Flagged as a minor residual against the checklist's literal "ZERO off-token hexes in templates/" wording.

**4b. profiles/ — FAIL.**
- The prompt named four targets: `profiles.css`, `states.css`, `dataviz.css`, and the example `.jsx` files.
- `diff v11/profiles/states.css v11_1/profiles/states.css` → 0 lines. **Untouched.** Still has 53 bare hex literals in unprefixed custom properties (`--state-success: #14A3A3`, `--text-secondary: #4A4A66`, `--text-muted: #6A6A84`, etc., none named `--pf-*`).
- `diff v11/profiles/dataviz.css v11_1/profiles/dataviz.css` → 0 lines. **Untouched.** Still has 44 bare hex literals (`--seq-violet-1: #F2E8FB`, `--div-neg-3: #E0309E`, `--chart-label: #8989a0`, etc., none named `--pf-*`).
- `profiles.css` itself was partially converted: 63 new `--pf-*` definitions were added (a `[data-profile="foundation|clinical|research|lab"]` block plus a `:root` canvas block), but 22 pre-existing top-level declarations (`--cg-azure: #3B7DD6`, `--emphasis: #8B3FC7`, `--surface: #F5F5FA`, etc.) remain bare and non-`--pf-*`.
- Net: at least 119 bare hex literals remain outside `--pf-*` definitions across the three CSS files (53 + 44 + 22), against a requirement of zero.
- The five `.jsx` example files and `design-canvas.jsx` **were** fully converted (0 residual bare hex in each), and spot-checks confirm values were preserved exactly: `--pf-clinical-1: #F5F5FA` (was inline `"#F5F5FA"` in `clinical-example.jsx:7`), `--pf-clinical-6: #6A6A84` (was inline `"#6A6A84"`), `--pf-clinical-5: #1E1E32`, `--pf-clinical-4: #CAA0F0`, `--pf-clinical-7: #9BC5F7` — all 5 spot-checked values unchanged.
- The checklist's own example, "text ramp #4A4A66/#6A6A84," is the smoking gun: that exact pair lives at `profiles/states.css:92-93` (`--text-secondary: #4A4A66;` / `--text-muted: #6A6A84;`), still bare, still un-prefixed, because `states.css` was never touched. This specific spot-check target **fails**.
- Naming quality note: where `--pf-*` names were created, they are non-semantic sequential indices (`--pf-clinical-1` through `-13`, then `-101`, `-102`) rather than the descriptive pattern the prompt modeled (`--pf-clinical-bg`, `--pf-clinical-text-2`). Deferred to "the profiles settlement pass" per an inline CSS comment; defensible but worth flagging since the sequencing makes the file harder to read than intended.
- `CHANGELOG.md:26-28` claims: "Lifted every bare hex literal in `profiles/` (385 usages) into scoped `--pf-<profile>-N` custom properties... values unchanged." **False** as an "every" claim; only the `.jsx` files were fully converted.
- `PHASE2_REPORT.md` section 4 claims: "No bare hex literals remain outside `--pf-*` definitions." **False**, and this report's own accounting silently omits `states.css` and `dataviz.css` from its file list entirely, despite both being named in the original prompt.
- This item was supposed to gate Phase 2 ("Report the checklist result before starting Part C"). The gate was not honestly reported before Phase 2 execution proceeded.

### 5. Small fixes — PARTIAL

- README casing: `README.md` exists at root; `find -iname readme.md` across the live tree returns only correctly-cased files (`README.md`, `assets/icons/README.md`, `profiles/README.md`). No lowercase `readme.md` remains, and no live file still references the old casing (confirmed via grep and via the `SKILL.md` diff, which shows both references updated). PASS.
- `assets/icons/README.md`: now reads "The starter set uses mixed stroke widths (1.5 / 1.75 / 2 px)... the Phase 2 production pass normalizes every icon to a 1.6 px stroke," matching the requested wording exactly. However, this file was written for the Part A checkpoint and never revisited after Phase 2 actually ran in the same pass: it still says "The 48-icon production pass is pending... Do not treat this set as final coverage," which is now false, the 48-icon set shipped in this same release (confirmed in item 12). Wording-level PASS, currency-level FAIL (stale).
- `SKILL.md`: "### Showcase (inherited reference implementations)" section exists at line 138, and indexes all five required items: `ui_kits/landing/index.html` and `ui_kits/dashboard/index.html` (covers `ui_kits/`), `Cytognosis Landing Page.html`, `landing/`, `frames/`, `screenshots/`. PASS.

### 6. Phase 1 regression greps — PARTIAL

| Check | Result |
|---|---|
| `#7159A7` | Zero matches outside uploads/. PASS |
| "Version 10.0" / "Version 9.0" | Zero matches outside uploads/. PASS |
| `#6366F1` / `#6366f1` | 2 matches: `SKILL.md:32` ("Never use Tailwind Indigo `#6366F1`.") and `references/04_color_system.md:123` (a "why we rejected this" comparison table). Both are banned-color citations, same pattern as item 1's accepted citations. CITATION, not a live use |
| Signal/Cohort/Trace as product names | No standalone use as a proper-noun product name (unlike the old Signal/Cohort/Trace placeholders `CHANGELOG.md:144` describes retiring). Found only as generic English/data-science words: "cohort B," "immune signal," "Cohort Explorer" (a dashboard nav label in `ui_kits/dashboard/index.html`, itself Showcase/legacy reference material), "Cohort dashboard" (a section id/label in `_ds_bundle.js` and `profiles/app.jsx`). Borderline but not a violation; flagged for a human glance since "Cohort Explorer" reads close to a leftover placeholder |
| Exactly one `SKILL.md` | `find . -iname SKILL.md` returns exactly one, at root. PASS |
| `VERSION` file | Contains `11.1.0`. PASS |
| `SKILL.md` frontmatter/body version consistency | **FAIL.** Frontmatter (`SKILL.md:3`) still reads `version: 11.0.0`; the H1 title (`SKILL.md:8`) still reads "Cytognosis Design System, v11.0.0." Neither was touched (confirmed via diff, these lines do not appear in the v11-to-v11_1 diff at all). Meanwhile `SKILL.md:59` body text does say "`VERSION` (11.1.0)." The file is internally inconsistent about its own version |

### 7. Regression diff summary — PASS

- `diff -rq v11/tokens v11_1/tokens`: no output, byte-identical.
- `diff v11/styles.css v11_1/styles.css`: no output, byte-identical.
- `diff -rq v11/components v11_1/components`: no output, byte-identical.
- `diff -rq v11/uploads v11_1/uploads`: only difference is `v11_1/uploads/prompt_v11_revision_1.md`, a new file (this revision's own instructions, added for provenance). No existing upload file was modified. This is an expected, benign addition, not a violation of "uploads/ untouched."

### 8. Master mark SVG corrections — PASS

`diff` of `assets/logos/cytognosis-logo-latest-2026-07.svg` against v11 shows exactly three changes and nothing else (no geometry touched):
1. `<namedview id="namedview39" pagecolor="#ffffff" bordercolor="#000000" borderopacity="0.25">` deleted entirely.
2. Gradient stop 2 (25%): `#635ECE` to `#6E5BD1`.
3. Specular ellipse fill: `#ffffff` to `#F8F8FC`, opacity 0.2 preserved exactly.

Verified in the resulting file: zero `#ffffff`, zero `#000000` anywhere. `#6E42B7` retained at 3 sites (signature gradient 75% stop, both radar-gradient midpoints). On-token anchors `#3B7DD6`, `#8B3FC7`, `#5145A8`, `#9BC5F7`, `#CAA0F0` all present and unchanged. `LOGO.md:18` documents `#6E42B7` explicitly as "an **approved blend stop**... the one non-scale hex permitted in the mark artwork." One purely cosmetic nit: the SVG root still declares the now-unused `xmlns:sodipodi=` namespace attribute (harmless, doesn't render, doesn't reintroduce a color); the namedview element itself is confirmed gone.

### 9. Logo family — PARTIAL

- `cytognosis-mono.svg`: every fill/stroke is `#8B3FC7`, nothing else. PASS.
- `cytognosis-reversed.svg`: every fill/stroke is `#F8F8FC`, nothing else. PASS.
- `cytognosis-wordmark-dark.svg` / `-light.svg`: both embed the full corrected mark plus a `<text>` element ("CYTOGNOSIS," Space Grotesk). Dark variant text fill `#0A0A14` (for light backgrounds); light variant text fill `#F8F8FC` (for dark backgrounds). Both on-token. PASS.
- `cytognosis-mark-simplified.svg`: the rendered body correctly drops the beam paths (no `radar1`/`radar2` `<path>` in the body) and the gloss ellipse, and thickens the spoke stroke-width from 2.5 to 5. **But** the `<defs>` block still contains the unused `<filter id="glow">` with `<feGaussianBlur>` and the unused `radar1`/`radar2` gradient definitions (dead code, not referenced by anything in the body). Literal grep count: `filter` appears 2 times, `feGaussian` appears 3 times, for 5 total matches against a required 0. **FAIL** on the literal checklist wording, though the rendered/visual output is correct since defs alone don't paint anything.
- Archive: `assets/logos/archive/` contains exactly the 10 expected files (the flat set: `cytognosis-mark.svg`, `cytognosis-dark.svg/.png`, `cytognosis-light.svg/.png`; the blue-lavender dimensional set: `cytognosis-dark-clean.svg`, `cytognosis-light-clean.svg`, `cytognosis-logo-only-clean.svg`, `cytognosis-logo-only-square-clean.svg`, `cytognosis-logo-only.png`). PASS on inventory.
- **"Nothing outside archive references them" fails.** Three live, non-documentation files still have working-as-written but now-broken `<img>` tags pointing at the pre-archive paths (confirmed these lines are unchanged from v11, so the archival move broke a reference that used to resolve):
  - `Cytognosis Landing Page.html:21` (`assets/logos/cytognosis-light.svg`, header logo) and `:354` (`assets/logos/cytognosis-dark.svg`, footer logo). This is the flagship public landing page, and it is newly indexed in this same revision's SKILL.md Showcase section.
  - `ui_kits/landing/index.html:186` and `:474`, identical pattern.
  - `ui_kits/dashboard/index.html:114`, same pattern for the dark variant, though this one has an `onerror="this.style.display='none'"` fallback so it fails silently (missing logo) rather than showing a broken-image icon.
  - Other mentions of the old filenames (`CHANGELOG.md`, `LOGO.md`, `README.md`, `references/03_logo.md`, `PHASE2_REPORT.md`) are prose/table documentation, not live embeds; those are citations, not violations, though `README.md:237-239` and `references/03_logo.md:18-22` are now stale (describe the retired file set as if current).
  - This was not explicitly in the prompt's re-pointing scope (which only named `deck.html`, `social-cards.html`, `email-signature.html`), but the archival action's blast radius was never checked against the rest of the live tree before finalizing.

### 10. Favicons, app icons, social, slides — PASS

All PNG dimensions verified via `file`:

| Asset | Required | Actual |
|---|---|---|
| favicon-16.png | 16x16 | 16 x 16 |
| favicon-32.png | 32x32 | 32 x 32 |
| favicon-48.png | 48x48 | 48 x 48 |
| apple-touch-icon.png | 180x180 | 180 x 180 |
| android-chrome-192.png | 192x192 | 192 x 192 |
| android-chrome-512.png | 512x512 | 512 x 512 |
| app-icon-ios-1024.png | 1024x1024 | 1024 x 1024 |
| app-icon-macos-1024.png | 1024x1024 | 1024 x 1024 |
| app-icon-android-512.png | 512x512 | 512 x 512 |
| og-image.png | 1200x630 | 1200 x 630 |
| avatar.png | square | 512 x 512 |
| linkedin-banner.png | plausible banner ratio | 1584 x 396 (exact official LinkedIn banner spec) |

`favicon.svg` exists at root. `app-icon-master-1024.svg` viewBox and width/height are `1024`. `slide-cover.svg` and `slide-divider.svg` use only tokens plus the approved `#6E42B7` blend stop (verified in item 13's sweep); no off-token or off-brand colors.

### 11. Template re-pointing — PASS

Grep for `-clean.(svg|png)`, `logos/archive`, `cytognosis-mark.svg`, `cytognosis-logo-only` across `templates/` returns zero matches. Final logo references in templates/: `deck.html` uses `slide-cover.svg` and `cytognosis-wordmark-light.svg`; `email-signature.html` and `one-pager.html` use `cytognosis-wordmark-dark.svg`; `social-cards.html` uses both wordmark variants across its 6 card faces. `deck.html`'s gold handling (`var(--gold)` resolving to `var(--cg-lp-yellow)`) is consistent with item 4a. Note `one-pager.html` was re-pointed too, beyond the prompt's explicit three-file list; this is a positive, and it is accurately disclosed in `CHANGELOG.md:62-64`.

### 12. Icons — PASS

- `assets/icons/line/` and `assets/icons/solid/` each contain exactly 48 SVGs (target met).
- Spot-check of 6 line icons (atom, bell, cytonome, heatmap, microscope, trajectory) and 6 solid icons (cell, chart-bar, cytoscope, helix, scatter, warning): all 12 have `viewBox="0 0 24 24"`, `stroke-width="1.6"`, `stroke-linecap="round"`, and use only `currentColor` (zero hardcoded hex across all sampled files).
- Sprite regeneration confirmed: `cytognosis-icons-line.svg` and `cytognosis-icons-solid.svg` differ substantially from v11 (324 and 320 diff lines respectively, not stale), contain exactly 48 `<symbol>` elements each, and every stroke-width in the line sprite is uniformly `1.6` (no leftover 1.5/1.75/2 mix).
- `ICONOGRAPHY.md` exists at root, is indexed from `SKILL.md`, and its claims check out: the documented 8-family breakdown (6+4+8+4+6+6+6+8) sums to exactly 48, and every one of the 48 documented icon names matches an actual file in both `line/` and `solid/`.
- Registration: icons are registered in `_ds_manifest.json` (an `icons.card.html` gallery card entry under group "Iconography," subtitle "Production icons, 24x24, 1.6px stroke..."). Not registered in `_adherence.oxlintrc.json` (that file was never touched, see item 2/3), but the checklist's "and/or" wording is satisfied by the manifest registration alone.

### 13. Non-token color sweep, all new SVG assets — PASS

Built the full normalized hex set from every file in `assets/logos/*.svg` (root level, excluding `archive/`), `favicon.svg`, `slide-cover.svg`, and `slide-divider.svg`, then diffed against (tokens/colors.css set + `#6E42B7`). Result: zero offenders. Separately swept every file in `assets/icons/line/`, `assets/icons/solid/`, and both sprite sheets for any hex literal at all: zero matches (confirming all icon color is `currentColor`-only, no hardcoded hex anywhere).

### 14. PHASE2_REPORT.md — PASS

Contains all five required sections: mark corrections (with a before/after table), assets generated, assets archived, Part A.4 token mappings (both the full 12-value templates table and the profiles summary), and Phase 2 Definition of Done. Render evidence claims were checked against the filesystem, not just taken on faith: `screenshots/phase2/mark-before-{512,64,32,16}.png` and `mark-after-{512,64,32,16}.png` all exist and each file's actual pixel dimensions (verified via `file`) match its filename exactly (e.g., `mark-after-16.png` is genuinely 16x16). `mark-comparison.png` and the icon contact sheets (`icons-line.png`, `icons-solid.png`) also exist as claimed.

### 15. CHANGELOG truthfulness — FAIL

Structurally, the 11.1.0 entry does cover both Revision 1 and Phase 2. Spot-verifying claims against the tree (more than the requested 3, because the pattern kept recurring):
1. "Replaced em dashes in the `_adherence.oxlintrc.json` lint messages with periods." **False** (item 2).
2. "Extended the font allowlist... so the profile fonts validate." **False** (item 3).
3. "Lifted every bare hex literal in `profiles/`... into scoped `--pf-<profile>-N` custom properties." **False** (item 4b, states.css and dataviz.css untouched).
4. "`deck.html` title and section-opener slides now use the slide backgrounds" (Phase 2 section). **Partly false**: only the title slide references `slide-cover.svg`; the "Section, Findings" slide still uses the plain flat `.accent` background class, and `slide-divider.svg` is generated but referenced nowhere in the live tree (confirmed via tree-wide grep, it only appears in `LOGO.md` and `PHASE2_REPORT.md`'s own documentation of itself).

Claims that did verify true: the copy fixes, the mark corrections table, the archive list, the README rename, the Showcase section addition, the favicon/app-icon/social asset list, and the icon count and spec. The changelog is not uniformly dishonest, most of it is accurate, but on the specific claims that map to this revision's core purpose (the audit-driven fixes), it overstates completion at least 3 separate times, plus a fourth overstatement in the Phase 2 section.

### 16. Unexpected/leftover files — PASS

Full file-level diff (`comm` on sorted `find` output) between v11 and v11_1 shows every added file is explicable: `ICONOGRAPHY.md`, `PHASE2_REPORT.md`, `README.md` (rename), `assets/icons/icons.card.html`, all 96 new icon SVGs, all new logo/favicon/app-icon/social/slide assets, the 10 archived files (at their new archive path), all 12 `screenshots/phase2/` render files, and `uploads/prompt_v11_revision_1.md`. Every removed file is explicable too: the 10 old flat-family files (moved to archive, not deleted) and `readme.md` (renamed). No duplicate sprites, no stray temp files, nothing orphaned outside what's already flagged above.
- Old sprite files `assets/icons/cytognosis-icons-line.svg` / `cytognosis-icons-solid.svg` at the `assets/icons/` root: confirmed **regenerated**, not stale (see item 12; 324/320 diff lines, uniform 1.6px stroke, 48 symbols each).
- `assets/icons/icons.card.html`: a living-style-guide gallery page (consistent with the `.card.html` pattern used throughout, e.g. `colors-gradients.card.html`, `core.card.html`) that renders all 48 icons, both variants, via the sprite's `<symbol>` definitions. It is a legitimate, purposeful file, registered in `_ds_manifest.json`, not leftover cruft.

## 3. Defects by severity

**Ship-blocking:**
- `profiles/states.css` (53 bare hexes) and `profiles/dataviz.css` (44 bare hexes) were never touched despite being explicitly named in the prompt; `profiles.css` itself retains 22 more. This was supposed to be a re-verified gate before Phase 2 started, and it was not honestly gated. (Items 4b, 15)
- `_adherence.oxlintrc.json` is completely untouched: 2 required em-dash fixes not applied, font allowlist not extended even though the profiles it should validate actively use those fonts. (Items 2, 3, 15)
- Broken logo `<img>` references in `Cytognosis Landing Page.html` (the flagship public page) and both `ui_kits/` reference builds, caused by this revision's own archival step. (Item 9)
- The CHANGELOG and PHASE2_REPORT contain multiple specific, verifiable false completion claims. Beyond the individual defects this undermines confidence in every other unverified claim in both documents. (Item 15)

**Moderate:**
- `SKILL.md` frontmatter (`version: 11.0.0`) and H1 title still say v11.0.0 while the body and VERSION file say 11.1.0. (Item 6)
- `cytognosis-mark-simplified.svg` still contains a full unused `<filter>`/`<feGaussianBlur>` block and unused beam gradient defs; visually correct, textually non-compliant. (Item 9)
- `slide-divider.svg` was generated but is wired into nothing; the changelog's "section-opener slides now use the slide backgrounds" claim does not hold. (Items 9, 15)
- `--pf-*` naming in `profiles.css` is non-semantic (sequential numbers, plus an inconsistent `-101`/`-102` pair), undercutting the readability goal of "named" custom properties.

**Cosmetic:**
- `templates/deck-stage.js` retains 2 pre-existing `#000` (pure black) instances, outside the scope of the 12 flagged template values, non-brand-visible stage chrome. (Item 4a)
- `assets/icons/README.md`, `README.md`'s logo asset table, and `references/03_logo.md` describe the pre-Phase-2 world (starter icon set "pending," old flat logo files as current) and were never revisited after Phase 2 shipped in the same pass. (Items 5, 9)
- Master mark SVG root still declares an unused `xmlns:sodipodi` namespace attribute after the namedview element was deleted. (Item 8)
- `deck.html`'s `--text-muted` now resolves to `var(--cg-lp-muted)`, a light-mode/landing token, even inside dark "ink" sections; nearest-hex-value mapping is technically correct but may read as a legibility regression on dark backgrounds worth a design glance. (Item 4a)
- "Cohort Explorer" / "Cohort dashboard" labels in legacy Showcase reference files read close to the retired placeholder product name; almost certainly fine (generic term, not a proper noun) but worth a human glance. (Item 6)

## 4. Regression diff summary

`tokens/`, `styles.css`, and `components/` are byte-identical to v11: zero regressions. `uploads/` gained exactly one new file (this revision's own prompt, for provenance) and no existing upload was modified. This is the cleanest part of the entire audit; nothing to fix here.

## 5. Publish-readiness verdict

**Not ready to ship as v11.1.0 final.** Three ship-blocking issues, all independently confirmed with file-level evidence: `profiles/` tokenization is roughly 70 percent incomplete against an explicit, named, gated requirement; the adherence/lint config that two separate checklist items depend on was never edited at all; and the flagship landing page now has broken logo images as a direct side effect of this revision's own archival step. Layered on top, the changelog and Phase 2 report both overstate completion on exactly the items that turn out to be incomplete, which means the next reviewer cannot trust either document without re-verifying against the tree, as this audit just did.

The favicon/app-icon/social/slide asset generation, the icon production set, the master mark color correction, and the template re-pointing are all genuinely well executed and precisely match their specs; that work does not need to be redone. Recommend a narrowly scoped Revision 2 pass: (1) actually apply the two line-level edits plus the font allowlist extension to `_adherence.oxlintrc.json`; (2) tokenize `states.css`, `dataviz.css`, and the remaining 22 literals in `profiles.css` into `--pf-*` properties, ideally with semantic suffixes rather than sequential numbers; (3) fix or re-point the three broken logo references outside `templates/`; (4) either wire `slide-divider.svg` into a deck section-opener slide or correct the changelog claim; (5) strip the dead filter/beam defs from `cytognosis-mark-simplified.svg`; (6) bump `SKILL.md` frontmatter and title to 11.1.0; (7) reissue the changelog to state only what is verifiably true. None of this is large in volume, it is concentrated in two files (`_adherence.oxlintrc.json`, `profiles/states.css` and `dataviz.css`) plus a handful of one-line reference fixes, but it is load-bearing for the Definition of Done this revision was supposed to close out.
