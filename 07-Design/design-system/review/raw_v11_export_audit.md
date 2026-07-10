# Raw Audit: Cytognosis Design System v11 Export

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: designers, stakeholders
> **Tags**: `design`, `design-system`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

Audited against: `03_next_prompts/prompt_merge_v11.md` (Sections 2 to 12).
Export root (all relative paths below are relative to this): `01_extracted/v11/`
Comparison references: `01_extracted/ali_latest/` (base project), `01_extracted/mine/`, `04_graft_bundle/v11_grafts/` (raw graft, pre-fix), `04_graft_bundle/v11_grafts/MANIFEST.md`.
Audit date: 2026-07-08.

This is a raw evidence file, not the plain-language summary. Read section 1 for the fast pass, section 3 for what to fix first.

---

## 1. Scoreboard

| # | Item | Verdict | One-line evidence |
|---|---|---|---|
| 1 | Root structure / one SKILL.md / no stray shells | PARTIAL | All Section 8 items present; exactly one `SKILL.md` in the tree; but `readme.md` should be `README.md`, and pre-existing base clutter (`ui_kits/`, `Cytognosis Landing Page.html`, `_ds_bundle.js`) sits outside the Section 8 list |
| 2 | Forbidden strings return zero matches | FAIL | "breakthrough" used as live copy (not a banned-word citation) in 2 files; em dash present in 3 root files (35 characters total) |
| 3 | Governance files (VERSION, CHANGELOG, CONTRIBUTING, ACCESSIBILITY, WRITING) | PASS | All five present with every required sub-element, verbatim quotes below |
| 4 | Tokens (spacing, easing, day scale, semantic aliases, lp violet, new dark block, primitives unchanged) | PASS | All values match spec exactly; diff vs `ali_latest` shows zero value changes, only comment punctuation |
| 5 | Components (.jsx/.d.ts/.prompt.md, Button 44px, adherence registration) | PARTIAL | All 7 components complete and Button meets 44px; but adherence config's font allowlist was not extended for profile fonts, contradicting the changelog's own claim |
| 6 | Grafts landed (profiles/, templates/, references/, IMAGERY/LOGO, uploads provenance) | PASS | All structural requirements met; uploads/ diff vs `ali_latest/uploads/` is empty outside the new graft folder |
| 7 | SKILL.md indexes everything | PASS | All required sections present and quoted below |
| 8 | Yar absent | PASS | Zero matches for "yar" outside CHANGELOG's own out-of-scope list |
| 9 | Old-token bleed-through | PARTIAL | Named old-only tokens: clean. Hardcoded non-token hex values: 14 distinct values in `templates/`, 48 in `profiles/` |
| 10 | Logos (Phase 2) | NOT STARTED | Master mark uncorrected; no wordmark family, no archive/ folder |
| 11 | Favicons/app icons/social/slides (Phase 2) | NOT STARTED | Zero matching files found anywhere in the tree |
| 12 | Icons (Phase 2) | NOT STARTED (Phase 1 graft only) | Only the 2 starter sprite sheets exist; stroke width is 1.5/1.75/2px, not the claimed 1.6px; no ICONOGRAPHY.md |
| 13 | Non-token colors in NEW assets (Phase 2) | N/A, gated | No Phase 2 assets exist yet to check beyond the still-uncorrected master mark (covered under item 10) |
| 14 | Changelog/report evidence of Phase 2 | FAIL (absent) | CHANGELOG.md has only the v11.0.0 Phase 1 entry; no report file exists anywhere |
| 15 | Unexpected items | PASS | Everything net-new traces to the graft manifest or explicit governance instructions; legacy clutter confirmed pre-existing in `ali_latest` |

**Phase 1 read:** 5 clean PASS, 3 PARTIAL, 1 FAIL, out of 9 gating items. Section 10's Definition of Done is not fully met, so Phase 2 correctly has not been run.

---

## 2. Detailed evidence

### Item 1: Root structure

Section 8 target: `SKILL.md, README.md, VERSION, CHANGELOG.md, CONTRIBUTING.md, ACCESSIBILITY.md, WRITING.md, IMAGERY.md, LOGO.md, tokens/, styles.css, components/, guidelines/, profiles/, references/, templates/, assets/, uploads/, _adherence.oxlintrc.json, _ds_manifest.json`.

- All of the above exist at root. Confirmed by directory listing.
- Exactly one `SKILL.md` in the whole tree: `find . -iname "SKILL.md"` returns only `SKILL.md` at root. PASS.
- No stray `delivery.html`, `index.html`, or `lumen-glass-system*.html` at root: confirmed, none found. PASS.
- Deviation: the readme is `readme.md` (lowercase), not `README.md`. This predates the merge (confirmed present as lowercase in `ali_latest/readme.md` too), so it is inherited, not introduced, but it still does not match the Section 8 casing.
- Extra root-level items not in the Section 8 list: `Cytognosis Landing Page.html` (31,541 bytes), `_ds_bundle.js` (405,349 bytes), `ui_kits/` (2 files: `dashboard/index.html`, `landing/index.html`). All three are confirmed byte-for-byte inherited from `ali_latest` (present there under identical names before the merge). `frames/`, `landing/`, `screenshots/` are also present but the audit brief itself names these as expected leftovers from the base, so they are not scored as defects here.

### Item 2: Forbidden strings

| String | Live matches outside `uploads/` | Verdict |
|---|---|---|
| `#7159A7` | 0 | PASS |
| "Version 10.0" | 0 (all 12 hits are in `uploads/v11_grafts_2026-07-08/references/*.md`, the raw pre-fix upload copy) | PASS |
| "Version 9.0" | 0 | PASS |
| Signal/Cohort/Trace as product names in `WRITING.md` | 0. `WRITING.md:140` reads "the Cyto- family (Cytoverse, Cytoscope, Cytonome) plus Helix Model." The one "Cohort" hit in `WRITING.md:141` is the lowercase feature-naming example "compare cohorts", not a product name | PASS |
| `#6366F1` / `#6366f1` | 0 live uses; all matches are "do not use" documentation, e.g. `references/04_color_system.md:123`, `\| Tailwind Indigo \| #6366f1 \| Too cold, too SaaS \|` | PASS |
| "revolutionary" | 0 live uses; all matches are banned-word-list citations (`SKILL.md:30`, `WRITING.md:114`, `readme.md:79`, `references/02_voice_and_tone.md:60` and `:89`, `guidelines/brand-voice.card.html:50`) | PASS |
| "game-changing" | 0 live uses; same pattern as above | PASS |
| "breakthrough" | **2 live uses**, see below | **FAIL** |
| em dash character | **35 instances across 3 files**, see below | **FAIL** |

**"breakthrough" defects (real usage, not banned-word citation):**
- `guidelines/colors-gradients.card.html:27`: `<div class="use">Scientific rigor → breakthrough. Research sections.</div>`. Confirmed pre-existing and unchanged in `ali_latest/guidelines/colors-gradients.card.html`; the merge touched this exact file (converted its em-dash subtitle to a comma) but did not catch this word.
- `references/01_brand_foundation.md:36`: `2. **Health Equity.** Universal access to breakthrough technologies.` Confirmed present unchanged in the raw graft (`04_graft_bundle/v11_grafts/references/01_brand_foundation.md:36`); Section 3 only instructed a version-string and routing fix for this file, not a banned-word scrub, but Section 1's ground rule is unconditional ("anywhere, in any file").

**Em dash defects (count per file):**
- `_adherence.oxlintrc.json`, 2 instances, both inside authored lint-message strings:
  - line 36: `"message": "Raw hex color — use a design-system color token via var()."`
  - line 40: `"message": "Raw px value — use a design-system spacing token via var()."`
- `_ds_manifest.json`, 2 instances, inside auto-generated subtitle metadata that describes files under `uploads/`, e.g. `"v0.2 — blue/green forward, sharper scientific tone"` (Lumen Glass System card) and `"Foundation · Clinical · Research · Lab — 16 surfaces total"` (the uploads copy of Profile explorations). Likely regenerated automatically by the design tool rather than hand-authored.
- `_ds_bundle.js`, 31 instances, all inside JavaScript code comments (e.g. line 8396 `// Profile explorations — 4 profiles × 4 surfaces`). This file is a 405 KB bundle that reads as tool-generated output, not hand-authored merge content.

Note: every comment in every `tokens/*.css` file and in `styles.css` had its em dashes converted to commas during this merge (confirmed by diffing against `ali_latest`, see Item 4). That sweep touched files it was arguably not supposed to touch under "tokens stay exactly as they are", but it was necessary to satisfy the absolute em-dash rule, and no token value changed. It is noted here as context, not scored as a defect, since the em-dash rule is higher priority than the "do not restyle" rule and only comments were affected.

### Item 3: Governance

- `VERSION`: file content is exactly `11.0.0` (7 bytes, trailing newline only). PASS.
- `CHANGELOG.md`, `[11.0.0] - 2026-07-08` entry contains all three required elements:
  - (a) Migration table under "Semantic-alias migration (old system to v11)": `| --bg-1 | darkest surface | --bg-4 (darkest, --cg-abyss #0A0A14) |` and `| --bg-4 | card / raised | --bg-1 territory (primary surface / card) |`, matching Section 2's instruction exactly.
  - (b) Yar out-of-scope list under "Moved out of scope (Yar)": lists `yar-app/` (with all named subparts), `Yar Desktop.html`, `Yar Prototype.html`, `Yar Presence Directions.html`, `Yar Handoff.md`.
  - (c) Retirement note under "Retired": "Version numbers 9.0, 10.0, and 1.0.0 are retired. v11.0.0 is the single current standard."
  - PASS on all three.
- `CONTRIBUTING.md` present at root, names this project as source of truth: "This project, the Cytognosis Design System v11, is the single source of truth for tokens, components, guidelines, profiles, references, templates, and brand assets." PASS.
- `ACCESSIBILITY.md` flags old `--fg-*` pairs as pending re-audit: global note "⚠ Pending re-audit against the v11 ramp" plus every one of the four contrast tables (Foundation, Clinical, Research, Lab) subtitled "⚠ pending re-audit against v11 ramp". PASS.
- `WRITING.md` has real product names ("the Cyto- family (Cytoverse, Cytoscope, Cytonome) plus Helix Model", line 140) and a merged banned-claims list under "Banned words and non-diagnostic safety (union with the base system)" (line 110), explicitly stated as "the union of this doc's rejected words and the base design system's guardrails." PASS.

### Item 4: Tokens

All confirmed in `tokens/motion.css`, `tokens/spacing.css`, `tokens/colors.css`:

| Token | Required | Found | Verdict |
|---|---|---|---|
| `--space-4xl` | 80px | 80px | PASS |
| `--space-5xl` | 120px | 120px | PASS |
| `--ease-out` | `cubic-bezier(0.16,1,0.3,1)` | `cubic-bezier(0.16, 1, 0.3, 1)` | PASS |
| `--ease-in-out` | `cubic-bezier(0.65,0,0.35,1)` | `cubic-bezier(0.65, 0, 0.35, 1)` | PASS |
| `--cg-day-*` scale | present | `--cg-day-50/100/200/300/400` all present | PASS |
| `--fg-1/2/3` | `#E8E8F4 / #C0C0D8 / #8888A8` | exact match | PASS |
| `--border-1` | violet-tinted | `rgba(139, 63, 199, 0.15)`, which is `--cg-violet-600 #8B3FC7` | PASS |
| `--cg-lp-violet` | `#6E5BD1` | exact match | PASS |
| New `[data-theme="dark"]` `--cg-lp-*` block | present, dark warm bg like `#15131C` | present at `tokens/colors.css:202-221`; `--cg-lp-bg: #15131C` exact match | PASS |

Diff of `tokens/colors.css` (and every other `tokens/*.css` and `styles.css`) against `ali_latest`: every changed line is a comment where an em dash was replaced with a comma (e.g. `Cytognosis Color System — v10.1.0` to `Cytognosis Color System, v10.1.0`). No hex value, spacing value, or curve value differs. The only substantive addition is the new dark-theme `--cg-lp-*` block appended at the end of `colors.css`. Primitive scales are unchanged. PASS.

### Item 5: Components

- All 7 components (`Badge`, `Button`, `Card`, `Input`, `Tag` in `components/core/`; `DataBar`, `MetricTile` in `components/data/`) have `.jsx` + `.d.ts` + `.prompt.md`. `DataBar.prompt.md` and `Tag.prompt.md` both exist with full usage docs matching `Button.prompt.md`'s format. PASS.
- `Button.jsx:3-8` size map:
  ```
  sm:   { ... minHeight: '44px', ... }
  md:   { ... minHeight: '44px', ... }
  lg:   { ... minHeight: '48px', ... }
  pill: { ... minHeight: '44px', ... }
  ```
  All four sizes are at or above 44px. `Button.d.ts` and `Button.prompt.md` both state this correctly. PASS.
- `_adherence.oxlintrc.json`, `x-omelette.components` key lists exactly 7 entries (`Badge, Button, Card, DataBar, Input, MetricTile, Tag`), matching the actual component count. Every one of the 7 also has prop and enum validation rules under `no-restricted-syntax`. PASS.
- `x-omelette.tokens` and `tokenKinds` include the full `--cg-lp-*` dark family. PASS.
- **Defect:** the CHANGELOG claims "Adherence config extended to track... the profile fonts (IBM Plex Sans/Mono, Source Serif Pro, Recursive)," but `_adherence.oxlintrc.json`'s `x-omelette.fontFamilies` list is `["Atkinson Hyperlegible", "Inter", "JetBrains Mono", "Lexend", "Newsreader", "Space Grotesk"]`, six families, none of the four profile fonts. The `no-restricted-syntax` font-family regex (line ~30) only allow-lists those same six. `profiles/profiles.css` (lines 92-114) legitimately declares `"IBM Plex Sans"`, `"IBM Plex Mono"`, `"Source Serif Pro"`, and `"Recursive"` as real `font-family` values. As written, every one of those declarations would trip the lint rule's "Font not provided by the design system" warning. The changelog's claim does not match the shipped config.

### Item 6: Grafts landed

- `profiles/`: 5 CSS files (`a11y.css`, `dataviz.css`, `motion.css`, `profiles.css`, `states.css`) + `README.md` + 7 examples (`app.jsx`, `clinical-example.jsx`, `design-canvas.jsx`, `foundation-example.jsx`, `lab-example.jsx`, `research-example.jsx`, `Profile explorations.html`). All 12 files contain the string "settlement" (verified: `grep -rln settlement profiles/` returns all 12; zero files missing it). PASS.
- `templates/`: `deck.html`, `deck-stage.js`, `one-pager.html`, `email-signature.html`, `social-cards.html` all present. No leftover `colors_and_type.css` or `--font-mono` references (`grep` returns nothing), confirming the CHANGELOG's claimed token-name updates. PASS.
- `references/`: 12 files present. `references/02_voice_and_tone.md` opens with "# Cytognosis Voice & Tone"; `references/03_logo.md` opens with "# Cytognosis Logo & Mark." Routing is correct and `SKILL.md:114-115` explicitly documents the fix: "Routing note: 02 is voice and tone, 03 is logo. An earlier index had these two swapped; v11 corrects it." PASS.
- `IMAGERY.md`, `LOGO.md` present at root (copied as-is per Section 3, no changes required). PASS.
- `uploads/` provenance: `diff -rq ali_latest/uploads v11/uploads`, excluding the new `v11_grafts_2026-07-08/` subfolder, returns zero differences. Nothing pre-existing was edited or deleted. PASS.

### Item 7: SKILL.md indexes

`SKILL.md` frontmatter: `name: cytognosis-design-system`, `version: 11.0.0`. Body title: "# Cytognosis Design System, v11.0.0".

Section headers present, in order:
1. "## Read order for agents" (7-step list covering this file, `readme.md`, `tokens/` + `styles.css`, `references/`, `components/` then `guidelines/` then `profiles/` then `templates/`, `WRITING.md`/`ACCESSIBILITY.md`, `CONTRIBUTING.md`/`CHANGELOG.md`/`VERSION`)
2. "## The hard NEVER list" (em dash, banned words, pure black/white, Tailwind Indigo, magenta as primary identity, non-diagnostic safety)
3. "## Key things to know immediately"
4. "## Structure", with subsections "### Governance and root docs", "### Tokens (`tokens/`, entry point `styles.css`)", "### Components (`components/`)", "### Guidelines (`guidelines/`, Design System tab specimen cards)", "### Profiles (`profiles/`)", "### References (`references/`, deep specs, numbered)" (lists all 12 filenames and the 02/03 routing note), "### Templates (`templates/`)", "### Assets (`assets/`)", "### Provenance (`uploads/`)"
5. "## If invoked without other guidance"

Every required index category is present with correct filenames. Component convention (`.jsx`/`.d.ts`/`.prompt.md`) is explained under "Components". Uploads provenance is explained under "Provenance". PASS, comprehensively.

### Item 8: Yar absent

`grep -rniI "yar" .` (excluding `uploads/`) returns matches only in `CHANGELOG.md` lines 104-113, all inside the sanctioned "### Moved out of scope (Yar)" section. No `yar-app/` directory and no `Yar Desktop.html` / `Yar Prototype.html` / `Yar Presence Directions.html` / `Yar Handoff.md` files exist anywhere in the live tree. PASS.

### Item 9: Old-token bleed-through

**Named old-only tokens** (`--cg-card-dark`, `--font-docs`, `--font-a11y`, `--font-display-alt-1`, `--font-accent-alt-1`) in `templates/` and `profiles/`: zero live matches. The single tree-wide mention of `--font-display-alt-1` is in `references/05_typography.md:40`, correctly confined to documentation of optionality ("Alternates also live as `--font-display-alt-1` etc."), per Section 2's instruction. Note `--font-docs` and `--font-a11y` are not actually old-only; both are live current tokens in `tokens/fonts.css:21-22`. PASS on this sub-check.

**Hardcoded hex not in `tokens/colors.css`:** built the allowed set from `tokens/colors.css` (96 unique hex values) and diffed against every hex literal in `templates/` and `profiles/`.

- `templates/`, 14 distinct off-token values: `#000, #1E1E2E, #2A2A3D, #4A4A66, #6A6A84, #8989A0, #E0E0E8, #E5E5EC, #E8E5F2, #F0F0F5, #F4B942, #F5F5FA, #FAFAFC, #FFF`. Examples: `templates/deck.html:14-16,25` defines `--ink-3:#1E1E2E; --ink-soft:#2A2A3D; --paper:#FAFAFC; --gold:#F4B942;` as local CSS variables, not sourced from `tokens/`. `templates/one-pager.html:10` sets `background:#E5E5EC`. Note `#1E1E2E` and `#2A2A3D` are near-misses of the real tokens `--cg-neutral-900 #1E1E32` and `--cg-neutral-800 #262640`, close enough to suggest hand-drift rather than an intentional separate palette.
- `profiles/`, 48 distinct off-token values, e.g. `#F5F5FA, #4A4A66, #6A6A84, #8989A0, #E8E5F2, #C96442, #F26D9F`. Many of these are exactly the old-system per-profile contrast hexes already called out as "pending re-audit" in `ACCESSIBILITY.md` (e.g. `#F5F5FA` is the Clinical light base, `#4A4A66`/`#6A6A84` are its text ramp). `CONTRIBUTING.md` rule 2 says profile-specific colors belong in the profile ("add it to the profile, don't inline a hex value"), so a bespoke per-profile palette is arguably intentional design, not a bug. It is flagged here because these values were never reconciled into named, documented profile tokens; they are bare literals scattered through `profiles/profiles.css`, `states.css`, `dataviz.css`, and the example `.jsx` files.

### Item 10: Logos (Phase 2, not gated to have started, reporting what exists)

`assets/logos/` has 11 files: the pre-existing flat-mark family (`cytognosis-dark-clean.svg`, `cytognosis-dark.svg`, `cytognosis-dark.png`, `cytognosis-light-clean.svg`, `cytognosis-light.svg`, `cytognosis-light.png`, `cytognosis-logo-only-clean.svg`, `cytognosis-logo-only-square-clean.svg`, `cytognosis-logo-only.png`, `cytognosis-mark.svg`) plus the new `cytognosis-logo-latest-2026-07.svg` (6,041 bytes).

Section 12.1 color audit on `cytognosis-logo-latest-2026-07.svg`, checked with exact-hash grep:

| Color | Occurrences | Detail | Corrected? |
|---|---|---|---|
| `#d1d1d1` | 0 | Not found in hex or rgb-equivalent form; the prompt's "one instance" prediction does not hold for this export | N/A |
| `#000000` | 1 | Line 3: `<sodipodi:namedview ... pagecolor="#ffffff" bordercolor="#000000" borderopacity="0.25">`, Inkscape editor canvas metadata, not a visible shadow or filter as the prompt described | No |
| `#ffffff` | 2 | One at line 3 (same inert namedview metadata), one at line 91: `fill="#ffffff" opacity="0.2"` on a small ellipse, a genuine visible specular highlight | No |
| `#635ECE` | 1 | `stop-color="#635ECE"`, a gradient blend stop | No (recommended snap to `--cg-lp-violet #6E5BD1`, which has 0 occurrences in the file, confirming it has not been applied) |
| `#6E42B7` | 3 | `stop-color="#6E42B7"` x3, the documented "keep as blend stop" color | N/A, no change required |

On-token anchors confirmed present and correct: `#3B7DD6` x2, `#8B3FC7` x4, `#5145A8` (mixed case, x5 lowercase + x4 uppercase in stop-color), `#9BC5F7` x1, `#CAA0F0` x1, matching the signature triad and orb/node radials described in Section 12.1.

No wordmark lockups (light/dark), no monochrome variant, no reversed variant, no simplified small-size variant, and no `assets/logos/archive/` folder exist. Phase 2.2 has not started.

### Item 11: Favicons/app icons/social/slides (Phase 2)

File search for `*favicon*`, `*apple-touch*`, `*android-chrome*`, `*app-icon*`, `*1024*`, `*og-image*`, `*avatar*`, `*linkedin*banner*`, `*deck-cover*`, `*section-divider*` across the entire `v11/` tree: zero results. None of this Phase 2 asset work has started.

`templates/social-cards.html` (lines 76, 91, 106, 125, 140, 152) and `templates/email-signature.html` (line 75) both reference `../assets/logos/cytognosis-light-clean.svg` and `../assets/logos/cytognosis-dark-clean.svg`, the old flat "-clean" marks, not any new mark family. Expected, since Phase 2.2 (which would refresh these references) has not run.

### Item 12: Icons (Phase 2, partial credit from the Phase 1 graft)

Only `assets/icons/cytognosis-icons-line.svg` and `assets/icons/cytognosis-icons-solid.svg` exist (the graft-copied starter set), plus `assets/icons/README.md`.

- `README.md` explicitly discloses the gap: "The 48-icon production pass is pending... Do not treat this set as final coverage," and forward-references "`ICONOGRAPHY.md` (added in Phase 2)". This matches Section 3's instruction exactly. Good self-documentation.
- viewBox spot check: every icon in both sprite sheets uses `viewBox="0 0 24 24"`. PASS.
- Stroke-width spot check: actual values found are `1.5`, `1.75`, and `2`. The literal `1.6` never appears, which contradicts the README's own claim that "Both are drawn on a 24x24 grid with a 1.6px stroke." FAIL on this specific sub-check.
- Rough count: approximately 42 icon-like group/symbol definitions per sheet (short of the 48-icon target; this is the pre-Phase-2 starter set, as disclosed).
- No root `ICONOGRAPHY.md` exists yet (only the pre-existing `references/06_iconography.md`, which is a different, already-existing reference document, not the new Phase 2 index).

### Item 13: Non-token colors in NEW assets (Phase 2, gated)

No Phase 2 assets exist yet (no favicons, app icons, or generated logo variants), so there is nothing new to check beyond the still-uncorrected master mark, already covered in Item 10.

### Item 14: Changelog/report evidence of Phase 2

`CHANGELOG.md` contains only the single `[11.0.0] - 2026-07-08` entry, which documents Phase 1 work only. A tree-wide search for `*phase2*` or `*report*` filenames across the entire `design-system-merge-2026-07/` project returns nothing. No record exists anywhere of "assets generated, assets archived, corrections applied." FAIL, by absence, consistent with Phase 2 not having started.

### Item 15: Unexpected items

Cross-referenced every net-new v11 item against `04_graft_bundle/v11_grafts/MANIFEST.md` and against `ali_latest`:

- Every new root governance file (`VERSION`, `CHANGELOG.md`, `CONTRIBUTING.md`, `ACCESSIBILITY.md`, `WRITING.md`, `IMAGERY.md`, `LOGO.md`) and every new directory (`profiles/`, `references/`, `templates/`) traces directly to the MANIFEST's contents list.
- `assets/logos/cytognosis-logo-latest-2026-07.svg` is explicitly named in the MANIFEST as the one file arriving outside the `references/`-renamed structure.
- The pre-existing clutter (`ui_kits/`, `frames/`, `landing/`, `screenshots/`, `Cytognosis Landing Page.html`, `_ds_bundle.js`, lowercase `readme.md`) is confirmed present in `ali_latest` before the merge, so none of it is unexplained; it is simply inherited scope the merge prompt never asked to touch.
- No orphan, mysterious, or unaccounted-for file was found anywhere in the export. PASS.

---

## 3. Defect list, ordered by severity

**High, blocks Phase 1 sign-off:**

1. Ground-rule violation ("breakthrough"), 2 instances:
   - `guidelines/colors-gradients.card.html:27`
   - `references/01_brand_foundation.md:36`
2. Ground-rule violation (em dash), 3 files, 35 characters total:
   - `_adherence.oxlintrc.json:36` and `:40` (2 instances, in authored lint-rule messages, straightforward to hand-fix)
   - `_ds_manifest.json` (2 instances, auto-generated subtitle metadata describing `uploads/` content)
   - `_ds_bundle.js` (31 instances, in JS comments, appears tool-generated)
3. `_adherence.oxlintrc.json`'s font allowlist (`x-omelette.fontFamilies` and the `no-restricted-syntax` font-family regex) was not extended for the four profile-bound fonts (IBM Plex Sans, IBM Plex Mono, Source Serif Pro, Recursive), contradicting the CHANGELOG's explicit claim that it was. Every legitimate font declaration in `profiles/profiles.css:92-114` will trip the lint rule as written.

**Medium:**

4. Old-system hardcoded hex values not sourced from `tokens/colors.css`: 14 distinct values in `templates/` (worst offenders: `templates/deck.html:14-16,25`), 48 distinct values in `profiles/` (matching the old per-profile contrast palette `ACCESSIBILITY.md` already flags as pending re-audit).
5. `assets/icons/` sprite sheets use stroke-width 1.5/1.75/2px, never the 1.6px the README and Phase 2 spec both claim.

**Low, cosmetic or inherited from base (not introduced by this merge):**

6. `readme.md` should be `README.md` per Section 8's exact casing.
7. Root carries pre-existing base clutter outside the literal Section 8 tree (`Cytognosis Landing Page.html`, `_ds_bundle.js`, `ui_kits/`); not a merge defect, but worth a decision on whether to archive it out at some point.

---

## 4. Unexpected and leftover items

None found that are not already explained. For completeness, the full inherited-from-base list (present in `ali_latest` prior to this merge, untouched by it): `frames/` (4 files), `landing/` (2 files), `screenshots/` (13 files), `ui_kits/` (2 files), `Cytognosis Landing Page.html`, `_ds_bundle.js`, `readme.md`. All confirmed via `diff`/presence check against `ali_latest`.

---

## 5. Phase 2 work missing entirely

Everything in Section 12 of the merge prompt. Specifically:

- **12.1, color correction:** none of the 3 real corrections applied (`#000000` namedview metadata, `#ffffff` specular highlight, `#635ECE` blend stop snap to `#6E5BD1`). Before/after renders at 512/64/32/16px do not exist. Open question 4 has not been surfaced or answered.
- **12.2, logo family generation:** no wordmark lockups (light/dark), no monochrome variant, no reversed variant, no simplified small-size/favicon-source variant, no `assets/logos/archive/` folder, no move of either old mark family into archive. Open question 5 (retire the flat `cytognosis-mark.svg` family or keep it) has not been surfaced or answered.
- **12.2, favicon/app-icon/social/slide assets:** none exist (`favicon.svg`, 16/32/48px PNGs, apple-touch-icon, android-chrome PNGs, 1024px app-icon master plus platform exports, 1200x630 og-image, square avatar, LinkedIn banner, deck cover, section-divider assets).
- **12.2, template refresh:** `templates/social-cards.html` and `templates/email-signature.html` still reference the old flat `-clean` marks, not any new family.
- **12.3, icon completion:** still the graft's 2 starter sprite sheets only (roughly 42 icons each, mixed stroke widths). No individual per-icon SVGs, no second production sprite pair, no manifest/adherence registration, no root `ICONOGRAPHY.md`.
- **12.4, Phase 2 Definition of Done:** none of the 5 items met.
- **12.5, open questions:** neither Phase 2 open question (4 or 5) has been surfaced for a decision yet, correctly, since Phase 2 is gated on Phase 1 passing and Phase 1 has not passed.
