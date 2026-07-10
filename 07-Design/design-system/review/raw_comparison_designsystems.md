# Design System Merge Review — Raw Comparison

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: designers, stakeholders
> **Tags**: `design`, `design-system`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

All paths below are relative to:
`/home/mohammadi/Claude/Projects/Science and Platform/design-system-merge-2026-07/01_extracted/`

Three systems compared: `mine/` (457 files), `ali_old/` (83 files), `ali_latest/` (129 files).

---

## 1. Executive Summary

1. **`ali_old` is not a Cytognosis asset at all.** It is Ali Mohammadi's personal brand system (monochrome + single blue accent, fintech/executive positioning, built from `ali_old/uploads/CV-AliMohammadi-0b66c6f6.pdf` and `ali_old/uploads/ali_mohammadi_work_user_manual.docx`). Zero occurrences of the word "Cytognosis" anywhere in `ali_old/` (verified by full-directory grep). Its only merge value is as a structural/process reference for how Ali builds systems, not as a source of Cytognosis tokens or copy.
2. **Core brand-600 color values are byte-identical between `mine` and `ali_latest`.** All six hue scales (violet, azure, indigo, teal, coral, magenta, ~10 shades each) in `mine/colors_and_type.css` and `ali_latest/tokens/colors.css` match exactly. The merge has essentially zero primitive-color conflict to resolve.
3. **The semantic alias layer conflicts directly.** `--fg-1` through `--fg-4`, `--bg-1` through `--bg-4`, and `--border-1`/`--border-2` exist in both systems under the *same names* but resolve to *different values*, and `--bg-1`/`--bg-4` are semantically inverted (mine: `--bg-1`=darkest/page, `--bg-4`=lightest/card; ali_latest: `--bg-1`=mid-dark/primary, `--bg-4`=darkest/abyss). This is the single highest-risk silent-conflict for a merge — code from one system dropped into the other will compile and render, just wrong.
4. **`ali_latest` is far more machine/AI-adherence-ready.** Its `_adherence.oxlintrc.json` encodes per-component prop contracts (7 components, 19 validation rules incl. enum checks) generated from the paired `.d.ts`/`.prompt.md` files. `mine`'s adherence config tracks more raw tokens (293 vs 208) but has **zero** registered components (`x-omelette.components` is an empty object) — it cannot catch a single invalid prop.
5. **`mine`'s own entry point (`mine/SKILL.md`) undersells the system.** It indexes only README/CSS/assets/preview/one ui_kit. It never mentions `profiles/`, `branding/`, `templates/`, `export/`, or any of the six governance markdown files at root — arguably `mine`'s best content is undiscoverable to an agent that only reads `SKILL.md`.
6. **`mine` ships three non-identical SKILL.md-style entry points** (`mine/SKILL.md`, `mine/branding/SKILL.md`, `mine/uploads/brand/SKILL.md`) with three different `name:` values and scopes. `mine/uploads/brand/SKILL.md` self-declares as auto-generated ("Do not manually edit... overwritten during sync") from a `cytognosis/branding` repo this export doesn't otherwise connect to.
7. **`mine/branding/SKILL.md`'s own routing table is broken.** It tells an agent to load `references/02_logo.md` and `references/03_color_quickref.md`, but the actual files are `references/02_voice_and_tone.md` and `references/03_logo.md`. Following the skill's own instructions loads the wrong document twice.
8. **`mine` has unresolved internal version drift.** `mine/README.md` cites brand guide "Version 9.0, March 2026"; `mine/branding/references/04_color_system.md`, `mine/Cytognosis Design System.html`, and `mine/delivery.html` all say "Version 10.0"; `mine/VERSION` says `1.0.0` (a separate semver track per `mine/CHANGELOG.md`). Three numbering systems, none reconciled in one place.
9. **`mine`'s CHANGELOG describes a system that doesn't exist on disk.** `mine/CHANGELOG.md` documents fonts (Geist, Geist Mono, Fraunces), a file called `ICONOGRAPHY.md`, and top-level `imagery/`, `data-viz/`, `motion/`, `a11y/` folders. None of that exists; Fraunces is explicitly **banned** in `mine/README.md`. The changelog is aspirational/stale, not a record of the real build.
10. **`mine`'s "Lumen" glass-system proposal and `ali_latest`'s canonical landing-light palette are the same palette.** `mine/lumen-glass-system.html` (dated 16 May 2026, "v0.2 Proposal") defines a warm off-white glass palette that is hex-identical to `ali_latest/tokens/colors.css`'s `--cg-lp-*` tokens on 8 of 9 shared colors (background triad, sky, lavender, data-blue, teal, yellow, sage all match exactly). Only the primary violet differs: Lumen `#7159A7` vs. ali_latest `#6E5BD1`. This should be one of the easiest conflicts to close in the whole merge.
11. **`ali_latest` bundles a second, unrelated product ("Yar").** `ali_latest/yar-app/`, `ali_latest/Yar Desktop.html`, `Yar Prototype.html`, `Yar Presence Directions.html`, and `Yar Handoff.md` (11 files) describe "a calm AI companion" with its own object model, orb states, and navigation. It reuses Cytognosis color tokens but is not one of the four products (Cytoverse/Cytoscope/Cytonome/Helix Model) documented in `ali_latest/readme.md`. This needs an explicit in/out-of-scope call before merging component or token files.
12. **Governance is `mine`'s strongest and `ali_latest`'s weakest area; machine-readable component contracts are the reverse.** `mine` has `CONTRIBUTING.md`, `CHANGELOG.md`, `VERSION`, an ownership matrix, and a genuinely distinctive four-profile system (Foundation/Clinical/Research/Lab) with its own contrast-audit doc (`mine/ACCESSIBILITY.md`). `ali_latest` has none of that (no CHANGELOG, no VERSION, no CONTRIBUTING) but wins decisively on component typing, token modularity, and provenance transparency (it ships its actual 12 source upload documents; `mine` only describes its sources in prose).

---

## 2. Per-System Inventory

### 2.1 `mine/` — 457 files

| Area | Path(s) | Notes |
|---|---|---|
| Entry points | `SKILL.md`, `README.md`, `VERSION`, `CHANGELOG.md` | Three-doc front matter; `SKILL.md` says "Read README.md first" |
| Governance docs | `ACCESSIBILITY.md`, `WRITING.md`, `IMAGERY.md`, `LOGO.md`, `CONTRIBUTING.md` | Root-level, prose + tables, none elsewhere in the three systems |
| Tokens (flat) | `colors_and_type.css` (309 lines) | Single file: color, gradient, type, spacing, radius, shadow, motion, glass |
| Tokens (aggregate) | `styles.css` (19 lines) | `@import`s `colors_and_type.css` + all 5 `profiles/*.css` files |
| Adherence | `_adherence.oxlintrc.json` (659 lines) | 293 tracked tokens, 0 registered components |
| Manifest/bundle | `_ds_manifest.json` (52,860 bytes), `_ds_bundle.js` (257,104 bytes) | Tool-generated (Claude Design "omelette" scaffold), 37 cards, 3 themes |
| Nested brand docs | `branding/SKILL.md`, `branding/references/01_brand_foundation.md` … `12_dataviz.md` | Parallel, more granular restatement of the brand guide, cites "Version 10.0" |
| Uploads/dupes | `uploads/brand/SKILL.md`, `uploads/brand/SKILL.tpl.md` | Third SKILL.md variant; self-describes as auto-synced from `cytognosis/branding` |
| Profile system | `profiles/` (profiles.css, states.css, motion.css, dataviz.css, a11y.css, README.md, 4 `*Example.jsx`, `design-canvas.jsx`) | Foundation/Clinical/Research/Lab — unique to `mine` |
| Components | `components/Components.jsx` (302 lines, 19 components in one file) | No `.d.ts`, no per-component docs |
| UI kit | `ui_kits/website/` (App/Header/Hero/Platform/Timeline.jsx + styles.css) | Page-section kit, not atomic |
| Templates | `templates/deck.html`, `deck-stage.js`, `one-pager.html`, `email-signature.html`, `social-cards.html` | Deliverable-ready output formats — unique to `mine` |
| Export mirror | `export/cytognosis-branding.html`, `export/src/cytognosis-branding.html` | Static branding-repo mirror |
| Exploratory | `lumen-glass-system.html`, `lumen-glass-system v1.html`, `Cytognosis Design System.html`, `delivery.html`, `index.html` | See finding #10; large single-file HTML artifacts |
| Assets | `assets/logos/` (11 files), `assets/icons/violet/` (2 SVG sprite sheets), `assets/products/` (3 PNGs), `assets/Helix_model_logo.png` | |
| Preview cards | `preview/*.html` (25 files) | Use `<!-- @dsCard ... -->` metadata comment, same convention as `ali_latest/guidelines/` |

### 2.2 `ali_old/` — 83 files (Ali Mohammadi personal brand — not Cytognosis)

| Area | Path(s) | Notes |
|---|---|---|
| Entry points | `SKILL.md` (13 lines), `README.md` (294 lines) | `name: ali-design`; monochrome + blue accent, "executive interface aesthetic" |
| Tokens | `colors_and_type.css` (330 lines) | `--ink`, `--blue`, `--surface`, `--line` naming; `[data-theme="dark"]` override block |
| Fonts | `fonts/SF-Pro-Display-{Bold,Black,BlackItalic}.otf` | Only system of the three to self-host actual font binaries |
| UI kits | `ui_kits/executive-dashboard/` (8 files), `ui_kits/personal-portfolio/` (6 files), `ui_kits/work-user-manual/` (12 files) | Page-section kits, fintech/editorial/long-form-doc use cases |
| Slide deck | `slides/` (6 `*Slide.jsx` + `deck-stage.js` + `slides.css` + `index.html`) | `slides/deck-stage.js` is line-for-line identical to `mine/templates/deck-stage.js` (verified via diff) — shared platform scaffolding, not brand-specific |
| Preview cards | `preview/*.html` (23 files) | Plain `<title>` tags, no `@dsCard` comment convention |
| Uploads | `uploads/CV-AliMohammadi*.pdf`, `uploads/ali_mohammadi_work_user_manual.docx` | Explicitly named as the two sole sources in `README.md` |
| No adherence config, no manifest, no bundle, no VERSION/CHANGELOG | — | Confirmed absent from directory tree |

### 2.3 `ali_latest/` — 129 files (Cytognosis Foundation, v10.1.0 — the intended new standard)

| Area | Path(s) | Notes |
|---|---|---|
| Entry points | `SKILL.md` (44 lines), `readme.md` (287 lines) | `name: cytognosis-design`; states version "10.1.0," last updated June 2026 |
| Tokens (modular) | `tokens/base.css`, `colors.css`, `fonts.css`, `motion.css`, `shadows.css`, `spacing.css`, `typography.css` (7 files, 560 lines total) | One concept per file, unlike `mine`'s single `colors_and_type.css` |
| Tokens (aggregate) | `styles.css` (13 lines) | `@import`-only entry point over `tokens/*` |
| Adherence | `_adherence.oxlintrc.json` (572 lines) | 208 tracked tokens, **7 registered components** with prop/enum validation |
| Manifest/bundle | `_ds_manifest.json` (28,273 bytes), `_ds_bundle.js` (376,404 bytes) | 20 cards, 1 theme, 4 `startingPoints` (mine has 0) |
| Components (atomic) | `components/core/{Badge,Button,Card,Input,Tag}.{jsx,d.ts,prompt.md}`, `components/data/{DataBar,MetricTile}.{jsx,d.ts[,prompt.md]}` | Only system with TypeScript defs + natural-language usage docs per component |
| Guidelines | `guidelines/*.card.html` (16 files) | `<!-- @dsCard ... -->` tagged specimen cards, same convention as `mine/preview/` |
| Frames (scaffolding) | `frames/design-canvas.jsx`, `ios-frame.jsx`, `macos-window.jsx`, `tweaks-panel.jsx` | All four headed `// @ds-adherence-ignore -- omelette starter scaffold` — platform tooling, not brand content |
| UI kits | `ui_kits/landing/index.html`, `ui_kits/dashboard/index.html` | Full-page reference implementations |
| Landing production assets | `landing/animations.js`, `landing/styles.css` | Supports the root `Cytognosis Landing Page.html` |
| Second product | `yar-app/*.jsx` (10 files), `Yar Desktop.html`, `Yar Prototype.html`, `Yar Presence Directions.html`, `Yar Handoff.md` | Not part of documented "Platform Architecture" — see finding #11 |
| Uploads (provenance) | `uploads/00_README_UPLOAD_ORDER.md` … `12_all_in_one_copy_paste_setup.md`, `11_cytognosis_design_tokens.json`, `CEO_Loved_Design_System_Reference.html` | Full literal build paper-trail, unmatched by the other two systems |
| No CHANGELOG.md, no VERSION file, no CONTRIBUTING.md | — | Confirmed absent from directory tree |

---

## 3. Token Comparison Tables

### 3.1 Identity triad + accents (hex values) — `mine/colors_and_type.css` vs `ali_latest/tokens/colors.css`

| Token (600/main) | mine | ali_latest | Match? |
|---|---|---|---|
| Violet | `#8B3FC7` | `#8B3FC7` | Identical |
| Azure | `#3B7DD6` | `#3B7DD6` | Identical |
| Indigo | `#5145A8` | `#5145A8` | Identical |
| Teal | `#14A3A3` | `#14A3A3` | Identical |
| Coral | `#F26355` | `#F26355` | Identical |
| Magenta | `#E0309E` | `#E0309E` | Identical |
| 300-shade "daily-use" (violet/azure/indigo/teal/coral/magenta) | `#CAA0F0` / `#9BC5F7` / `#ADA0E8` / `#7FE8E8` / `#FFBFB5` / `#F9A5DD` | same, all six | Identical |
| Full 10-11-step scales (50–950) | defined in `colors_and_type.css` L26-99 | defined in `tokens/colors.css` L26-101 | Identical, every step checked |
| Bare aliases `--cg-violet` / `--cg-azure` / `--cg-indigo` (no shade suffix) | **absent** | present, = 600 value | ali_latest only |
| Signature/Innovation/Vitality/Data/Alert gradients | identical strings, both 135° | identical strings | Identical |

### 3.2 Semantic aliases — direct conflicts

| Token | mine (`colors_and_type.css`) | ali_latest (`tokens/colors.css`) | Conflict |
|---|---|---|---|
| `--fg-1` | `#F8F8FC` | `#E8E8F4` | **Different value** |
| `--fg-2` | `#E0E0ED` | `#C0C0D8` | **Different value** |
| `--fg-3` | `#A6ADC8` | `#8888A8` | **Different value** |
| `--fg-4` | `#50506e` | `#50507A` | Nearly identical (minor hue shift) |
| `--bg-1` | `var(--cg-abyss)` (darkest, "page") | `var(--cg-neutral-900)` (mid-dark, "primary bg") | **Semantically inverted** |
| `--bg-4` | `var(--cg-neutral-700)` (lightest of the four, "card") | `var(--cg-abyss)` (darkest) | **Semantically inverted** |
| `--border-1` | `rgba(255,255,255,0.08)` (white-based) | `rgba(139,63,199,0.15)` (violet-tinted) | **Different hue basis** |
| `--border-2` | `rgba(139,63,199,0.10)` | `rgba(139,63,199,0.08)` | Same hue, different opacity |

### 3.3 Neutral scale — naming/structure divergence

| Concept | mine | ali_latest |
|---|---|---|
| Dark "Night" tiers | `--cg-neutral-950` … `--cg-neutral-500` (single 11-step scale spans both themes) | `--cg-neutral-950` … `--cg-neutral-500` (dark tier only, same hex values) |
| Light "Day" tiers | Same scale, continues `--cg-neutral-400` … `--cg-neutral-50` | **Renamed** to a separate `--cg-day-400` … `--cg-day-50` scale (same hex values, different variable family) |
| Abyss / Deep | `--cg-abyss: #0a0a14`, `--cg-deep: #13131f`, `--cg-card-dark: #25253d` | `--cg-abyss: #0A0A14`, `--cg-deep: #13131F` (no `--cg-card-dark` equivalent; case of hex differs cosmetically) |

### 3.4 Landing/light palette — `mine`'s "Lumen" proposal vs `ali_latest`'s canonical `--cg-lp-*`

| Concept | `mine/lumen-glass-system.html` var | value | `ali_latest/tokens/colors.css` var | value | Match |
|---|---|---|---|---|---|
| Main background | `--bg-main` | `#F4F2EF` | `--cg-lp-bg` | `#F4F2EF` | Identical |
| Soft background | `--bg-soft` | `#FAF8F2` | `--cg-lp-bg-soft` | `#FAF8F2` | Identical |
| Section background | `--bg-section` | `#ECE9E4` | `--cg-lp-bg-section` | `#ECE9E4` | Identical |
| Sky | `--c-sky` | `#D7E9FF` | `--cg-lp-sky` | `#D7E9FF` | Identical |
| Lavender | `--c-lavender` | `#A8B6FF` | `--cg-lp-lavender` | `#A8B6FF` | Identical |
| Data blue | `--c-data-blue` | `#8FBDF5` | `--cg-lp-data` | `#8FBDF5` | Identical |
| Teal | `--c-teal` | `#63C9C6` | `--cg-lp-teal` | `#63C9C6` | Identical |
| Yellow | `--c-yellow` | `#FFC845` | `--cg-lp-yellow` | `#FFC845` | Identical |
| Sage | `--c-sage` | `#A7C68A` | `--cg-lp-sage` | `#A7C68A` | Identical |
| Violet-deep | `--c-violet-deep` | `#3E3478` | `--cg-lp-violet-deep` | `#3E3478` | Identical |
| **Primary landing violet** | `--c-violet` | **`#7159A7`** | `--cg-lp-violet` | **`#6E5BD1`** | **Conflict — only real diff in this table** |
| Dark-mode variant | defined (`--bg-main:#15131C` etc., `--color-scheme:dark`) | — | **absent** | — | `ali_latest` has no dark variant of the landing palette; `mine`'s Lumen proposal does |

### 3.5 Typography

| Aspect | mine | ali_latest |
|---|---|---|
| Display/body | Inter | Inter |
| Accent/quote | Newsreader | Newsreader |
| Code/mono | JetBrains Mono | JetBrains Mono |
| A11y specialist fonts | Lexend (`--font-docs`), Atkinson Hyperlegible (`--font-a11y`) | Lexend, Atkinson Hyperlegible (listed in font-substitution note, no dedicated a11y token) |
| Alternate-font system | 3-deep stack per role: `--font-display-alt-1/2` (General Sans / IBM Plex Sans), `--font-accent-alt-1/2` (Source Serif Pro / Recursive), `--font-code-alt-1/2` (Fira Code / Recursive Mono) — `mine/colors_and_type.css` L191-196 | Single alt: `--font-heading-alt: Space Grotesk` — `ali_latest/tokens/fonts.css` | Alternates system simplified/reduced in ali_latest |
| Banned fonts | Fraunces (rejected in prose), Urbanist (rejected in prose) | Fraunces, Urbanist, Arial, Times New Roman, Helvetica, Roboto (explicit banned list, `readme.md` L144) | ali_latest's ban list is a superset |
| Type scale method | Fixed rem, computed once, Major Third 1.25 (`--text-h1: 3.052rem`) | `clamp()` fluid responsive for display–h4, fixed rem below that | Different implementation, same ratio concept |
| Smallest/most granular step | `--text-caption` (12px) | `--text-caption` (12px), `--text-code` (14px), `--text-label` (11px), `--text-micro` (10px) | ali_latest has 3 more granular steps |
| Letter-spacing / line-height / weight as tokens | Hardcoded per-selector in `colors_and_type.css` (e.g. `h1{letter-spacing:-0.02em}`), not exposed as variables | Fully tokenized: `--ls-*` (10), `--lh-*` (10), `--fw-*` (6) in `tokens/typography.css` | ali_latest more machine-consumable |

### 3.6 Spacing / Radius / Shadow / Motion

| Token family | mine | ali_latest | Conflict? |
|---|---|---|---|
| `--space-xs` … `--space-xl` (4/8/16/24/32px) | identical | identical | No |
| `--space-4xl` | **96px** | **80px** | **Same name, different value** |
| `--space-5xl` | absent | 120px (new top step, "hero sections") | Addition only |
| `--radius-sm/md/lg/xl/2xl/pill` | 4/8/12/16/20/9999px | identical | No |
| `--shadow-sm/md/lg/xl` | identical rgba(26,26,46,*) values | identical | No |
| `--shadow-2xl`, `--shadow-inset` | absent | present | Addition only |
| Glow shadows | violet, indigo, magenta (3) | violet, azure, indigo, teal, magenta + 2 "sm" tight variants (7) | Addition only |
| `--dur-fast/base/slow/slower` | 150/250/350/500ms | identical | No |
| `--dur-pulse` | absent | 1500ms | Addition only |
| `--ease-out` | `cubic-bezier(0,0,0.2,1)` | `cubic-bezier(0.16,1,0.3,1)` | **Same name, different curve** |
| `--ease-in-out` | `cubic-bezier(0.4,0,0.2,1)` | `cubic-bezier(0.65,0,0.35,1)` | **Same name, different curve** |

### 3.7 `ali_old` reference point (different brand — for calibration only)

| Token family | ali_old value | Compare to Cytognosis shared value |
|---|---|---|
| Base spacing unit | 8px, 13 steps (4→128) | Same 8px base as both Cytognosis systems |
| Radius steps | 0/4/8/12/16px (5 steps) | Cytognosis systems go to 20px + pill; ali_old has no pill except avatars/dots |
| Motion durations | 120/180/240ms (quick/base/slow) | Faster than both Cytognosis systems' 150/250/350/500ms — expected, different brand calibration |
| Primary accent | `--blue: #2563EB` | Not comparable — monochrome+blue system vs. six-hue fluorophore system |

---

## 4. Component Matrix

| Component / surface | mine | ali_old | ali_latest |
|---|---|---|---|
| Button | `components/Components.jsx` `CG.Button` (variant/size inline, no pill) | Implicit only (`.btn` class in `colors_and_type.css`) | `components/core/Button.jsx` + `.d.ts` + `.prompt.md` — variant: primary/secondary/ghost/danger; size: sm/md/lg/pill |
| Input / Field | `CG.Field`, `CG.Input`, `CG.Textarea`, `CG.Select` | none as component (raw CSS only) | `components/core/Input.jsx` + `.d.ts` + `.prompt.md` — label/error/helper/id/type states |
| Checkbox/Radio/Toggle | `CG.Check`, `CG.Radio`, `CG.Toggle` | none | none |
| Card | `CG.Card` (padding prop only) | `.ds-card` utility class only | `components/core/Card.jsx` + `.d.ts` — accentBar/glass/padding(sm-lg)/theme(dark/light) |
| Modal | `CG.Modal` | none | none |
| Dropdown / Tooltip / Tabs | `CG.Dropdown`, `CG.Tooltip`, `CG.Tabs` | none | none |
| Badge | `CG.Badge` (tone prop) | none | `components/core/Badge.jsx` + `.d.ts` + `.prompt.md` — variant: violet/azure/indigo/teal/coral/magenta…; size sm/md; dot indicator |
| Tag/Chip | `CG.Chip` | none | `components/core/Tag.jsx` + `.d.ts` — variant: violet/azure/teal/neutral/code |
| Avatar | `CG.Avatar` | none | none |
| Table | `CG.Table` | `SourcesTable.jsx` (page-specific, not generic) | none generic (dashboard-specific markup in `ui_kits/dashboard/index.html`) |
| Banner / Toast | `CG.Banner`, `CG.Toast` (tone: info, etc.) | none | none |
| Metric / KPI tile | none generic (`profiles/*Example.jsx` embed metrics ad hoc) | `KpiRow.jsx` (page-specific) | `components/data/MetricTile.jsx` + `.d.ts` — status: normal/elevated/alert/optimal |
| Data bar / axis score | `dataviz.css` primitives (not componentized) | none | `components/data/DataBar.jsx` + `.d.ts` — baseline marker, unit, label |
| Icon system | `assets/icons/violet/` (20 branded SVGs, sprite sheet) | `Icon.jsx` (14 inline Lucide-style strokes) | Phosphor/Feather via CDN only — **no bundled SVGs** (`readme.md` L216 explicitly notes this gap) |
| Device frames (iOS/macOS mockup) | none | none | `frames/ios-frame.jsx`, `frames/macos-window.jsx` (platform scaffold, tagged `@ds-adherence-ignore`) |
| Design canvas / tweaks tooling | `profiles/design-canvas.jsx` (622 lines) | none | `frames/design-canvas.jsx` (974 lines), `frames/tweaks-panel.jsx` (541 lines) — same scaffold lineage, newer version |
| Slide deck system | `templates/deck.html` + `deck-stage.js` + `templates/deck/` | `slides/` — 6 slide types + `deck-stage.js` (**identical file** to mine's, verified by diff) | none |
| One-pager / email signature / social cards | `templates/one-pager.html`, `email-signature.html`, `social-cards.html` | none | none |
| Full-page kits | `ui_kits/website/` (5 sections) | `ui_kits/executive-dashboard/` (8), `ui_kits/personal-portfolio/` (6), `ui_kits/work-user-manual/` (12) | `ui_kits/landing/index.html`, `ui_kits/dashboard/index.html` (2 full single-file references) |
| Second-product app screens | none | none | `yar-app/*.jsx` (10 files) — separate product, see §6 |
| Component prop typing (`.d.ts`) | **none** | **none** | Yes, all 7 core/data components |
| Per-component usage doc (`.prompt.md`) | **none** | **none** | Yes, 4 of 7 components (`Badge`, `Button`, `Card`, `Input`; `DataBar`/`MetricTile`/`Tag` lack one — `DataBar.prompt.md` and `Tag.prompt.md` are absent from the file tree despite `MetricTile.prompt.md` existing) |

---

## 5. Unique-to-Each Lists

### 5.1 Only `mine` has

- Governance suite: `ACCESSIBILITY.md` (WCAG 2.2 contrast audit table per profile + testing checklist), `WRITING.md` (voice dials + good/bad copy per profile), `IMAGERY.md` (5 image pillars + sourcing checklist + shot list), `LOGO.md` (clear space, min size, approved backgrounds, favicon/social spec), `CONTRIBUTING.md` (4 rules, workflow, ownership matrix), `CHANGELOG.md` + `VERSION`.
- The **four-profile system** (`profiles/`: Foundation, Clinical, Research, Lab) — a documented, CSS-scoped (`[data-profile="…"]`) re-theming mechanism with its own `profiles/README.md` matrix. Nothing comparable exists in either Ali system.
- Deliverable **templates**: `templates/deck.html`, `one-pager.html`, `email-signature.html`, `social-cards.html`.
- `branding/` subfolder: a second, more granular 12-file restatement of the brand guide (`branding/references/01…12_*.md`), plus its own `branding/SKILL.md`.
- `export/` directory — a static mirror of branding-repo HTML.
- The exploratory **"Lumen" glass-system proposal** (`lumen-glass-system.html`, `lumen-glass-system v1.html`) — see §3.4 and §6.
- `uploads/brand/SKILL.md` / `SKILL.tpl.md` — a third skill-entry variant self-described as auto-synced from an external repo.
- Self-hosted deliverable HTML shells: `Cytognosis Design System.html`, `delivery.html`, `index.html`.

### 5.2 Only `ali_latest` has

- Modular `tokens/` directory (7 files by concern) vs. one flat CSS file.
- Atomic **`components/`** library with paired `.d.ts` type files and (mostly) `.prompt.md` usage docs — the only system with machine-checkable component contracts.
- `guidelines/` — 16 individually addressable `@dsCard`-tagged specimen files (colors, type, spacing, motion, voice).
- `frames/` device-mockup and tooling scaffold (`ios-frame.jsx`, `macos-window.jsx`, `tweaks-panel.jsx`) — confirmed platform scaffolding (`// @ds-adherence-ignore -- omelette starter scaffold`), not bespoke brand work.
- A dedicated **landing-light palette** (`--cg-lp-*`, 14 tokens) with a `[data-theme="light"]` override block — a formal second theme mine never built out at the base-token level (mine's closest analog is the Clinical *profile*, built for a different purpose).
- Full literal **provenance trail**: 12 upload documents (`uploads/00_README_UPLOAD_ORDER.md` through `12_all_in_one_copy_paste_setup.md`), the canonical `uploads/11_cytognosis_design_tokens.json`, and the "CEO-approved" reference (`uploads/CEO_Loved_Design_System_Reference.html`).
- Component-prop-aware linting: 19 `no-restricted-syntax` rules (vs. mine's 3), including JSX enum validation per component.
- A second product, **Yar** (`yar-app/`, 4 root HTML files, `Yar Handoff.md`) — see §6.
- Explicit non-diagnostic safety/copy guardrails as a first-class section of `readme.md` ("Non-Diagnostic Safety Rules," banned-claims list) — more elaborated than mine's banned-words list.

### 5.3 Only `ali_old` has (context, not mergeable into Cytognosis)

- Self-hosted font binaries (`fonts/SF-Pro-Display-*.otf`) — neither Cytognosis system self-hosts any font; both rely on Google Fonts CDN `@import` and flag this as an open question (`mine/README.md` L281: "please upload the files and we'll swap the `@import` for `@font-face`").
- A dedicated slide-deck kit with 6 named slide types (`AgendaSlide`, `ClosingSlide`, `ComparisonSlide`, `MetricSlide`, `QuoteSlide`, `TitleSlide`).
- Three distinct page-section UI kits for a personal-brand use case (executive dashboard, personal portfolio, long-form "work user manual" document) — structurally the same *pattern* mine uses for `ui_kits/website/`, just applied to different content.
- A plain `<title>`-based preview-card convention (no `@dsCard` metadata comment) — suggesting `ali_old` predates the `@dsCard`/manifest convention shared by `mine` and `ali_latest`.

---

## 6. Conflicts List

| # | Conflict | Systems | Evidence (exact paths) | Severity |
|---|---|---|---|---|
| 1 | `--fg-1/2/3` and `--bg-1…4` share names but differ in value; `--bg-1`/`--bg-4` are semantically inverted | mine vs ali_latest | `mine/colors_and_type.css` L128-137 vs `ali_latest/tokens/colors.css` L178-187 | High — silent visual breakage on merge |
| 2 | `--border-1` uses a different hue basis entirely (white-based vs. violet-tinted) | mine vs ali_latest | `mine/colors_and_type.css` L138 vs `ali_latest/tokens/colors.css` L182 | Medium |
| 3 | `--space-4xl` same name, different value (96px vs 80px) | mine vs ali_latest | `mine/colors_and_type.css` L220 vs `ali_latest/tokens/spacing.css` L14 | Medium |
| 4 | `--ease-out` and `--ease-in-out` same names, different cubic-bezier curves | mine vs ali_latest | `mine/colors_and_type.css` L245-246 vs `ali_latest/tokens/motion.css` L21-22 | Medium — changes felt motion quality system-wide |
| 5 | Neutral light scale renamed `--cg-neutral-*` → `--cg-day-*` (same hex, different variable family) | mine vs ali_latest | `mine/colors_and_type.css` L114-118 vs `ali_latest/tokens/colors.css` L138-142 | Low (mechanical rename) |
| 6 | Landing-violet hex differs: Lumen `#7159A7` vs. canonical `--cg-lp-violet` `#6E5BD1` | mine (Lumen proposal) vs ali_latest | `mine/lumen-glass-system.html` (`--c-violet`) vs `ali_latest/tokens/colors.css` L148 | Low — isolated single token, everything else in the palette already matches |
| 7 | Brand-guide version number inconsistent within `mine` itself: "9.0" (README) vs "10.0" (branding refs, HTML titles) vs "1.0.0" (VERSION, different scheme) | mine internal | `mine/README.md` L30 vs `mine/branding/references/04_color_system.md` L3 vs `mine/Cytognosis Design System.html` `<title>` vs `mine/VERSION` | Medium — governance/trust issue, not visual |
| 8 | `mine/branding/SKILL.md`'s file-routing table doesn't match actual filenames in `branding/references/` (02 and 03 are swapped/wrong) | mine internal | `mine/branding/SKILL.md` L11-13 (`02_logo.md`, `03_color_quickref.md`) vs actual `mine/branding/references/02_voice_and_tone.md`, `03_logo.md` | High — following the skill's own instructions loads the wrong file |
| 9 | `mine/CHANGELOG.md` documents fonts (Geist, Geist Mono, Fraunces) and files (`ICONOGRAPHY.md`, top-level `imagery/`/`data-viz/`/`motion/`/`a11y/`) that do not exist in the delivered folder; Fraunces is explicitly banned elsewhere | mine internal | `mine/CHANGELOG.md` L22-36 vs `mine/colors_and_type.css` (actual fonts: Inter/Newsreader/JetBrains Mono/Lexend/Atkinson Hyperlegible) vs `mine/README.md` L169 ("Rejected: Fraunces") | Medium — documentation debt, misleads about system history |
| 10 | Three non-identical SKILL.md-style entry points with different `name:` values and one claiming external auto-sync | mine internal | `mine/SKILL.md` (`name: Cytognosis Design System`) vs `mine/branding/SKILL.md` (untitled, "Cytognosis Branding Skill") vs `mine/uploads/brand/SKILL.md` (`name: brand-identity`, "auto-generated by `scripts/sync_brand.py`... Do not manually edit") | Medium — unclear which is authoritative |
| 11 | `ali_latest`'s `Button.jsx` component violates the system's own 44px touch-target rule | ali_latest internal | `ali_latest/components/core/Button.jsx` L3-8 (`sm`=32px, `md`=40px, `pill`=40px minHeight) vs `ali_latest/components/core/Button.prompt.md` L27 ("Touch-target ≥ 44px always") vs `ali_latest/tokens/spacing.css` L34 (`--touch-min: 44px`) vs `ali_latest/Yar Handoff.md` L139 ("All interactive targets are ≥ 44px") | Medium — only `lg` (48px) actually complies |
| 12 | WRITING.md's naming-convention examples use placeholder product names ("Signal," "Cohort," "Trace") that contradict the actual, established product architecture defined everywhere else | mine internal | `mine/WRITING.md` L129-132 vs `mine/README.md` L10-16 and `mine/SKILL.md` L63-67 (Cytoverse/Cytoscope/Cytonome) | Low — cosmetic/example text, not a live token |
| 13 | Font-alternates strategy diverges: mine's 3-deep per-role alternate stack (General Sans, IBM Plex Sans, Source Serif Pro, Recursive, Fira Code, Recursive Mono) is reduced to a single alternate (Space Grotesk) in ali_latest, with no stated reason | mine vs ali_latest | `mine/colors_and_type.css` L191-196 vs `ali_latest/tokens/fonts.css` | Low — simplification, but loses documented optionality |
| 14 | "Yar" product's design language (warm-light off-white/pale lavender home, central orb, poetic copy register) is not reconciled with, or referenced by, the core Cytognosis brand voice/visual rules in the same export | ali_latest internal | `ali_latest/Yar Handoff.md` L14-18 vs `ali_latest/readme.md` (Content Fundamentals / Visual Foundations sections, no mention of Yar) | Medium — scope-boundary question, not a token bug |
| 15 | `mine`'s root `SKILL.md` does not index `profiles/`, `branding/`, `templates/`, `export/`, or any governance `.md` file | mine internal | `mine/SKILL.md` L10-19 ("What this project contains") vs actual `mine/` tree | High for AI-discoverability — most of mine's differentiated content is invisible to an agent that trusts SKILL.md alone |

---

## 7. Quality Scores

Scale: 1 (poor) – 5 (excellent). Scored on the dimensions that matter for "will an AI agent reliably produce on-brand output from this."

| Dimension | mine | ali_old | ali_latest | Rationale |
|---|---|---|---|---|
| **Completeness** | 5 | 2 (n/a for Cytognosis) | 4 | mine covers accessibility, writing, imagery, logo, contributing, profiles, templates, export — the broadest scope of the three. ali_latest is strong on tokens/components/guidelines but has no equivalent of mine's ACCESSIBILITY/WRITING/IMAGERY/LOGO docs. ali_old is complete *for its own small brand* but contributes nothing to Cytognosis coverage. |
| **Internal consistency** | 2 | 5 | 4 | mine has three unreconciled version numbers (finding #7), a broken file-routing table in `branding/SKILL.md` (#8), a stale CHANGELOG describing nonexistent files/fonts (#9), and three divergent SKILL.md entry points (#10). ali_old is small and tight — nothing found in conflict. ali_latest has one real defect found (Button.jsx violates its own 44px rule, #11) but is otherwise coherent — one version number, one source of truth, tokens matching the canonical `uploads/11_cytognosis_design_tokens.json` almost exactly. |
| **Machine-readability / AI adherence** | 2 | 3 | 5 | ali_latest is best-in-class: 7 components with `.d.ts` + `.prompt.md` + oxlint rules that validate actual prop names and enum values (19 rules); modular `tokens/`; `@dsCard`-tagged guideline cards; a SKILL.md that ends with a concrete clarifying-question checklist. mine tracks more raw tokens (293 vs 208) but `x-omelette.components` is empty — the linter cannot catch a single invalid component usage — and its own SKILL.md fails to index most of its content (#15). ali_old has a clear, short SKILL.md pointing at real files, but zero automated enforcement of any kind (no adherence config, no manifest). |
| **Governance & maintainability** | 5 | 1 | 2 | mine is the only system with `CONTRIBUTING.md` (explicit ownership matrix, 4 rules, release workflow), `CHANGELOG.md`, and `VERSION`. ali_latest tracks its version only as a string in `readme.md`'s header, with no changelog and no contribution process. ali_old has neither. |
| **Provenance documentation** | 3 | 4 | 5 | ali_latest ships the literal source documents it was built from (12 files in `uploads/`, plus the canonical token JSON and the CEO-approved reference HTML) — a full, auditable paper trail. ali_old names its two sources plainly in `README.md`'s "Sources" section. mine describes its sources in prose (`README.md` "Sources" section, referencing private GitHub repos `cytognosis/branding` and `cytognosis/website`) but ships none of the literal source files, and one of its three SKILL.md variants claims to be auto-generated from a repo this export can't verify against. |
| **Scope discipline** | 4 | 5 | 3 | mine stays on-topic throughout (one exploratory side-proposal, Lumen, clearly labeled as such). ali_old is a single coherent personal-brand scope. ali_latest bundles an entire second, unrelated product (Yar, 11 files) into what is nominally "the Cytognosis Design System," without flagging the boundary in `readme.md`. |

**Net read:** `ali_latest` is the stronger foundation to build the merged system *on* (token modularity, component contracts, adherence tooling, provenance), but it needs `mine`'s governance layer (CHANGELOG/VERSION/CONTRIBUTING), accessibility audit rigor, and writing/imagery/logo docs grafted in, plus a decision on whether Yar ships as part of this design system at all. The semantic-alias conflicts (§6, items 1-4) and the two broken internal references in `mine` (items 7, 8, 10) are the concrete items that need a resolution decision before any file-copying starts.
