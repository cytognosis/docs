# Cytoskills Brand Canon and Relocation: Raw Reconciliation

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: designers, stakeholders
> **Tags**: `design`, `design-system`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

**Date:** 2026-07-10. **Reading time:** about 10 minutes.
**If you only read one thing:** cytoskills already matches the good, shipping v11 state on gradient, magenta, font, and icon stroke (the Google doc from March 2026 is the outdated source on all four). The one real defect is Helix: it appears as a public fourth product across five cytoskills files, which contradicts Shahin's own stated rule and the fix already planned for the Claude Design export. Branding-repo placement is blocked; the repo currently holds an unrelated CytoStyle component library, recovery gated on the Ali conversation (matches existing memory).

No em dashes used anywhere in this document, per house style.

---

## PART 1: CYTOSKILLS BRAND CANON (verbatim)

### 1.0 Source map and version

Two sibling skills carry the brand canon inside `/home/mohammadi/repos/cytognosis/cytoskills/skills/cytognosis/`:

| Skill | version (frontmatter) | last_revised | status | Role |
|---|---|---|---|---|
| `cytognosis-branding/SKILL.md` | 3.0.0 | 2026-05-27 | production | Deep-content home; the 12 numbered v10 references |
| `cytognosis-design-system-master/SKILL.md` | 3.0.0 | 2026-05-27 | production | Master entry point; cheatsheets; routes to the 12 references |

The brand content itself (not the skill-packaging version) is stamped **"Version 10.0"** throughout all 12 reference files (`01_brand_foundation.md` through `12_dataviz.md`), with `01_brand_foundation.md` additionally stamped "Updated May 2026." `governance.md` (design-system-master) states: "Current version (as of 2026-05-13): **v10.0.0**," tracked via a `VERSION` file at the branding-repo root. Tag files (`.cyto-tags.yaml`, both skills) show `tagged_date: 2026-05-18`, `version: "0.1"` (this is the tagging-schema version, not the brand-content version).

A third file, `cytognosis-design-system-master/brand-guide.md`, is a **legacy import**, not a SKILL.md: it self-identifies as sourced from "Brand guide... Version 9.0, March 2026" and describes a 20-icon set at 2px stroke with Phosphor/Feather as the base library. This is almost certainly the same lineage as, or a close cousin of, the Google Doc used as comparison source (A) in Part 2. It predates and is superseded by the 12 v10 references; do not treat it as canon, though it explains where some of the Google doc's now-outdated values originated.

The actively-loaded canon for any Cytognosis design or writing task is therefore: **cytognosis-design-system-master SKILL.md + its 8 local references, routing to cytognosis-branding's 12 deep references, both v10.0, last_revised 2026-05-27.**

### 1.1 Signature gradient (exact hex stops and direction)

```css
--cg-gradient-signature: linear-gradient(135deg, #3B7DD6 0%, #8B3FC7 50%, #5145A8 100%);
```

Azure to Violet to Indigo, the "Patient to Pioneer" wash. Identical string appears in `cytognosis-branding/SKILL.md` section 7, `cytognosis-branding/references/04_color_system.md`, `cytognosis-design-system-master/SKILL.md` section 3, and `cytognosis-design-system-master/references/tokens.md` section 2.

Four other named gradients (all 135deg), from `04_color_system.md`:

```css
--cg-gradient-innovation: linear-gradient(135deg, #14A3A3 0%, #3B7DD6 50%, #8B3FC7 100%);
--cg-gradient-vitality:   linear-gradient(135deg, #8B3FC7 0%, #F26355 50%, #B580E6 100%);
--cg-gradient-data:       linear-gradient(135deg, #3B7DD6 0%, #5145A8 50%, #6B5DC7 100%);
--cg-gradient-alert:      linear-gradient(135deg, #E0309E 0%, #F26355 100%);
```

### 1.2 Full color palette (primaries, accents, neutrals), verbatim from `04_color_system.md` and `tokens.md`

**Identity triad** (exactly three; magenta is explicitly excluded from this set):

| Color | Hex (600) | Source dye | Wavelength | Role |
|---|---|---|---|---|
| Violet | `#8B3FC7` | DAPI (DNA stain) | ~461nm | MAIN BRAND |
| Azure | `#3B7DD6` | Alexa Fluor 488 | ~488nm | "the Patient," data input |
| Indigo | `#5145A8` | UV excitation | ~358nm | "the Pioneer," AI outputs |

**Secondary and accent:**

| Color | Hex (600) | Source dye | Role |
|---|---|---|---|
| Teal | `#14A3A3` | GFP, ~509nm | biological harmony, success |
| Coral | `#F26355` | MitoTracker Orange, ~576nm | human warmth; functional data primary; never identity or logo |
| Magenta | `#E0309E` | Rhodamine-Phalloidin, ~565nm | ATTENTION ACCENT ONLY; never triad, never logo, never gradients except Alert |

**Full 11-step scales** (Violet, Azure, Indigo), from `04_color_system.md`:

| Shade | Violet | Azure | Indigo |
|---|---|---|---|
| 950 | #2E1147 | #071E3A | #110F2E |
| 900 | #4A1D6F | #0D3B66 | #1E1B4B |
| 800 | #5E2589 | #1A4D7F | #2D2766 |
| 700 | #7230A3 | #2761A3 | #3D3485 |
| 600 | **#8B3FC7** | **#3B7DD6** | **#5145A8** |
| 500 | #A05FD9 | #5A95E8 | #6B5DC7 |
| 400 | #B580E6 | #7AAEF2 | #8B7DD9 |
| 300 | #CAA0F0 (daily-use) | #9BC5F7 (daily-use) | #ADA0E8 (daily-use) |
| 200 | #DFC0F7 | #BCDCFB | #CFC5F3 |
| 100 | #F0E0FB | #DEF0FD | #E8E3FA |
| 50 | #F8F0FD | #EFF8FE | #F4F2FD |

**Neutrals** (all carry hue ~240, indigo undertone; never pure black or white):

Dark, per `04_color_system.md`: Abyss `#0a0a14` (marketing flagship dark) -> Deep Night `#1a1a2e` (sidebar, activity bar) -> Rich Night `#1e1e32` (panel backgrounds, default dark bg) -> Bold Night `#262640` (editor bg) -> Core Night `#303050` (elevated cards) -> Lite Night `#3d3d5c` (borders) -> Mist Night `#50506e` (dividers).

Dark, per `tokens.md` (a differently-abbreviated version of the same ladder): `--bg-ink-deep #0A0A14` (darkest) -> `--bg-deep-night #13131F` (research-tier dark) -> `--bg-rich-night #1E1E32` (foundation-tier, default dark bg).

These two cytoskills documents name **different hex values "Deep Night"** (`#1a1a2e` in one, `#13131F` in the other). See Part 2, conflict 5, for reconciliation against the shipped CSS.

Light: Pale Day `#F0F0F7` (primary light bg) -> Ghost Day `#F8F8FC` (page bg) -> Soft Day `#E0E0ED` (borders, inputs) -> Lite Day `#C4C4D8` (secondary text) -> Mist Day `#A8A8C0` (placeholders). Clinical variant: `#F5F5FA`.

Semantic: Success `#10B981`, Warning `#F59E0B`, Error `#EF4444`, Info `#3B7DD6` (= Azure 600).

Forbidden palettes (explicit, `04_color_system.md`): Tailwind Indigo `#6366f1`, Material Purple `#9c27b0`, Bootstrap Primary `#0d6efd`.

### 1.3 Typography

| Role | Default | Alt 1 | Alt 2 |
|---|---|---|---|
| Display + body | **Inter** | General Sans | IBM Plex Sans |
| Accent / quotes | **Newsreader** | Source Serif Pro | Recursive (cursive axis) |
| Code / mono | **JetBrains Mono** | Fira Code | Recursive Mono |

Accessibility specialists (dedicated use, not alternates): **Atkinson Hyperlegible** (patient forms, low vision), **Lexend** (ADHD, dyslexia documentation surfaces).

Banned as defaults: Fraunces (overused), Urbanist (too geometric for long sessions), Arial, Times.

Scale: Major Third (1.250 ratio). H1 48px/700/1.1 down to Caption 12px/500/1.4. Hard rules: body text never below 16px, line length 50 to 75 characters, left-aligned only (never justify), paragraphs three to four sentences maximum.

CSS tokens (`05_typography.md`):

```css
--font-display: 'Inter', system-ui, sans-serif;
--font-accent:  'Newsreader', Georgia, serif;
--font-code:    'JetBrains Mono', 'Fira Code', monospace;
--font-a11y:    'Atkinson Hyperlegible', sans-serif;
--font-docs:    'Lexend', sans-serif;
```

Font licensing and self-hosting (Lexend, Atkinson Hyperlegible, Newsreader) is noted elsewhere in this project (`V11.1_EXPORT_EVALUATION_2026-07-08.md` line 172) as "the one open question every prior effort deferred." Still open; fonts currently load from the Google Fonts CDN.

### 1.4 Iconography spec

48 brand-aligned icons across seven domains (Cell and molecular biology 10, Healthcare and medicine 10, AI and ML 8, Networks and graph 6, Sensing/GPS/radar 6, Time and process 4, People and equity 4). Two canonical variants:

| Property | Value |
|---|---|
| Format | SVG, viewBox 24x24 |
| Stroke width | **1.6px** (line variant) |
| Caps and joins | round |
| Fill | none (line); duotone, shade-600 primary + shade-300 accent (solid) |
| Scales | 16, 24, 32, 48, 64px |
| Gap-filling libraries | **Phosphor Icons (primary), Feather Icons (secondary)**, both re-stroked to 1.6px and re-colored to a Cytognosis token before use, never kept at their native stroke |

Ten older numbered icon-style folders (`01_solid_violet` through `10_duotone`) are explicitly deprecated as of v10 and archived at `branding/archive/2026-pre-v10/icons/`. The 48-icon set is self-described as **"preliminary"**; iteration priorities named in `iconography.md` are crisis-rail icons, voice and paralinguistic glyphs, a clearer sensor family, and richer equity representation.

Minor implementation note: the shipped SVG bundle (`assets/icons/cytognosis-icons-line.svg`, both skills) has at least one symbol (`dna-helix`) at `stroke-width="1.75"`, not 1.6, a small drift from the written spec worth a fix ticket.

### 1.5 Product architecture and Helix

Three product surfaces are described consistently everywhere as "GPS for Human Health":

| Component | Role | Metaphor |
|---|---|---|
| Cytoverse | AI health mapping system | The Map |
| Cytoscope | Programmable biosensors | The Sensor |
| Cytonome | On-device causal AI navigator | The Navigator |

**Helix model, listed as a fourth row ("Foundation AI model" / "The Engine"), appears in the live cytoskills canon** in:

- `cytognosis-branding/SKILL.md` section 6 (platform architecture table) and section 10 (asset paths: "products/, Cytoverse / Cytoscope / Cytonome / Helix marks")
- `cytognosis-branding/references/01_brand_foundation.md` (platform architecture table)
- `cytognosis-design-system-master/SKILL.md` section 1 (platform architecture table) and section 7 (ships `assets/products/helix-model.png`)
- `cytognosis-writer/SKILL.md` (capitalization rule: "product names capital (Cytoverse, Cytoscope, Cytonome, Helix model)"; proper-noun list)
- `cytognosis-template-master/references/website.md` (site nav map and component list: `CytoverseCard, CytoscopeCard, CytonomeCard, HelixCard`)

Dedicated `helix-model.png` product assets ship in both `cytognosis-branding/assets/products/` and `cytognosis-design-system-master/assets/products/`. See Part 2 section 6 for the full grep report and verdict.

### 1.6 Voice (brief, for completeness)

A brilliant scientist who genuinely cares about people. Five traits: authoritative, compassionate, innovative, accessible, optimistic. Every narrative follows the Revelation Arc (Mystery, Insight, Resolution). Hard rules: no em dashes, no passive voice, Oxford comma always, no "revolutionary / cure / game-changing / breakthrough / disrupt," "people" or "individuals" instead of "patients" outside clinical context. Source: `cytognosis-branding/references/02_voice_and_tone.md`, identical in substance to `design-system-master/references/voice.md`.

---

## PART 2: THREE-WAY CONFLICT RESOLUTION

Summary table, detail and reasoning below each row.

| # | Conflict | Google doc (Mar 2026) | v11 tokens (verified) | cytoskills (v10, 2026-05-27) | WINNER |
|---|---|---|---|---|---|
| 1 | Signature gradient | Violet to bright-Azure to Magenta | Azure to Violet to Indigo | Azure to Violet to Indigo (identical string, 4 files) | **v11 / cytoskills** |
| 2 | Magenta primary? | Yes, 4th primary | No, attention-only, hard NEVER | No, "exactly three," attention-only (5 files) | **v11 / cytoskills** |
| 3 | Accent font | Source Serif Pro | Newsreader (default) | Newsreader (default), Source Serif Pro demoted to alt / Clinical-profile default | **v11 / cytoskills** |
| 4 | Icon stroke | 2px, Phosphor/Feather as the set | (not in colors/fonts CSS; confirmed 1.6px via audits) | 1.6px custom 48-set; Phosphor/Feather gap-fill only, re-stroked | **v11 / cytoskills** |
| 5 | Neutrals | Deep Night #13131F, Deepest Night #0A0A12 | 8-step scale, both #13131F and #1A1A2E present | Two docs, each names a different hex "Deep Night" | **shipped colors.css scale** (reconcile both docs to it) |
| 6 | Helix as product | No, 3 products only, correct | N/A directly, but this project's own note says v11 agrees, no Helix | **Yes, appears as 4th product in 5 files** | **neither; live regression, needs fixing** |

### 1. Signature gradient

- **Google doc:** `linear-gradient(135deg, #8B3FC7 0%, #5A95E8 50%, #E0309E 100%)`, violet to a lighter azure (the 500 shade, not 600) to magenta.
- **v11 tokens** (`01_extracted/v11_new/tokens/colors.css`, read directly): `linear-gradient(135deg, #3B7DD6 0%, #8B3FC7 50%, #5145A8 100%)`, azure to violet to indigo. Confirmed byte-identical against Ali's independent export too (`DESIGN_SYSTEM_MERGE_REVIEW_2026-07-08.md` line 73: "all five gradients... match exactly").
- **cytoskills:** identical to v11, in `04_color_system.md`, `tokens.md`, and both SKILL.md cheatsheets.
- **WINNER: azure to violet to indigo (v11 and cytoskills agree).**
- **Why:** Recency; the Google doc is four-plus months older and its own values do not reappear anywhere else. Internal consistency; the azure-violet-indigo string is byte-identical across five independent cytoskills and export files versus the Google doc's single, unreplicated value. Science-grounding; the "cool primaries reduce cortisol, therapeutic by design" premise is stated identically in both eras but is only satisfied by an all-cool-hue gradient. Ending on magenta, a warm-leaning color defined everywhere else as "urgency, alerts only," directly contradicts that premise. Shipping reality; this is the literal gradient in production `tokens.css`.

### 2. Magenta as primary vs. magenta-never-identity

- **Google doc:** lists Violet, Azure, Magenta, Indigo as primaries; magenta is a primary color.
- **v11 tokens:** magenta is commented "Attention accent ONLY. Never in logos, brand gradients, or primary UI" (`colors.css` line 92-96).
- **cytoskills:** identity triad is defined as "exactly three primary identity colors: Azure, Violet, Indigo... Magenta is never part of the triad" (`04_color_system.md`), restated in `tokens.md`, and in both SKILL.md hard-NEVER lists ("Magenta as part of the identity, it is attention only").
- **WINNER: magenta is accent-only, never identity (v11 and cytoskills, 2 to 1).**
- **Why:** Internal consistency is decisive here; cytoskills states the never-identity rule in no fewer than five separate places versus the Google doc's single, looser assertion. This also reads as a genuine tightening over time rather than a live disagreement; the fluorophore-wavelength logic assigns magenta an alert/urgency meaning in every source including the Google doc's own philosophy, so treating it as a primary contradicts the color's own assigned semantics. The Google doc is an earlier, less-disciplined draft on this point.

### 3. Accent / quote font

- **Google doc:** Source Serif Pro.
- **v11 tokens** (`fonts.css`, read directly): `--font-accent: 'Newsreader', Georgia, 'Times New Roman', serif;`, Newsreader is default.
- **cytoskills:** Newsreader default, Source Serif Pro demoted to alt 1 (`05_typography.md`, `tokens.md`); Source Serif Pro remains the live default specifically for the Clinical profile (`design-system-master/SKILL.md` section 6 profile table).
- **WINNER: Newsreader as the global default; Source Serif Pro survives as a named alternate and the Clinical-profile default, nothing is lost.**
- **Why:** This project's own reconciliation note states the website "substituted [Newsreader] for Source Serif Pro for licensing reasons," meaning a deliberate, later, documented decision rather than an unresolved disagreement. Newsreader appears as default in three independent cytoskills sources plus the shipped `fonts.css`.

### 4. Icon stroke

- **Google doc:** 2px stroke, Phosphor primary and Feather secondary, implied to be the icon set itself (consistent with the older, 20-icon, v9.0-era `brand-guide.md` found inside `design-system-master/`, which describes exactly this state).
- **v11:** not set in colors/fonts CSS, but independently audited and confirmed: "48 line + 48 solid icons at uniform 1.6px using only currentColor, zero hardcoded hex" (`V11.1_EXPORT_EVALUATION_2026-07-08.md` lines 10 and 22).
- **cytoskills:** custom 48-icon set at 1.6px stroke is primary; Phosphor (primary) and Feather (secondary) are gap-filling only, re-stroked to 1.6px, never used at native stroke (`06_iconography.md`, `iconography.md`).
- **WINNER: 1.6px custom 48-icon set, Phosphor/Feather demoted to re-stroked gap-fill.**
- **Why:** This is a real, intentional design evolution, not a live contradiction. The pre-v10 system (documented in the legacy `brand-guide.md`, itself close kin to the Google doc) leaned on Phosphor/Feather at native 2px as the effective backbone with only 20 custom icons. The v10 canon replaced that with a fully brand-owned 48-icon set and tightened the stroke, explicitly deprecating "10 older numbered icon styles... as of v10." Independently verified as shipped and byte-correct as of the 2026-07-08 audit.

### 5. Neutrals, dark-scale reconciliation

- **Google doc:** Deep Night `#13131F`, Deepest Night `#0A0A12`.
- **v11 tokens** (`colors.css`, read directly): `--cg-abyss #0A0A14` (absolute darkest) -> `--cg-deep #13131F` (sidebar, activity bar) -> `--cg-neutral-950 #1A1A2E` -> `--cg-neutral-900 #1E1E32` (Rich Night, primary dark bg) -> `-800 #262640` -> `-700 #303050` -> `-600 #3D3D5C` -> `-500 #50506E`. Eight steps, both `#13131F` and `#1A1A2E` present as distinct rungs.
- **cytoskills:** two internally inconsistent partial views. `04_color_system.md`'s seven-step scale calls `#1A1A2E` "Deep Night" (sidebar, activity bar) and never mentions `#13131F`. `tokens.md`'s five-step scale calls `#13131F` "bg-deep-night" (research-tier dark) and never mentions `#1A1A2E`.
- **WINNER: the shipped `colors.css` eight-step scale.** It already contains both disputed values as distinct rungs, so nothing from either cytoskills doc is lost, they are two different steps of one ladder that got documented separately.
- **Reconciliation recommended:** update both `04_color_system.md` and `tokens.md` to the full eight-step scale with one consistent naming pass (Abyss `#0A0A14`, a new distinct name for `#13131F` such as "Deep" per the CSS comment, keep "Deep Night" for `#1A1A2E`, Rich Night `#1E1E32`, Bold Night `#262640`, Core Night `#303050`, Lite Night `#3D3D5C`, Mist Night `#50506E`). The Google doc's "Deepest Night `#0A0A12`" is almost certainly a transcription typo for `#0A0A14`; every other source, including the Google-doc reconciliation note's own comparison line, agrees on `#0A0A14`. Treat `#0A0A14` as canonical and discard `#0A0A12` as a documentation error, not a real design variant.

Also relevant and not yet written into the 12 references: a separate warm "Lumen" landing palette (`--cg-lp-*`, in the shipped `colors.css` but absent from `04_color_system.md` and `tokens.md`) is slated to become **the new default surface**, not dark. This is an already-recommended decision (D6) in `FINALIZATION_PLAN_2026-07-09.md`: "Warm paper (`--cg-lp-*`) as the default, dark as an explicit theme... your calm research names this the highest-leverage distinctiveness and calm move at once." The 12 v10 references have not caught up to this decision; flag for the next reference-doc revision alongside the neutral-scale fix.

### 6. Helix grep report (explicit, as requested)

Command: `grep -rin helix` across `/home/mohammadi/repos/cytognosis/cytoskills/skills/cytognosis`.

**Result: Helix appears as a named, public-facing product in the live canon, not merely as an incidental mention.** Full hit list:

| File | Context |
|---|---|
| `cytognosis-branding/SKILL.md:120` | Platform architecture table, row 4: "Helix model \| Foundation AI model \| The Engine" |
| `cytognosis-branding/SKILL.md:158` | Asset paths: "products/, Cytoverse / Cytoscope / Cytonome / Helix marks" |
| `cytognosis-branding/references/01_brand_foundation.md:61` | Platform architecture table, identical row |
| `cytognosis-branding/references/website.md:50, 230` | Site nav map; component list `HelixCard` |
| `cytognosis-design-system-master/SKILL.md:57` | Platform architecture table, identical row |
| `cytognosis-design-system-master/SKILL.md:190` | Asset ship list: `helix-model.png` |
| `cytognosis-writer/SKILL.md:77, 88` | Capitalization rule and proper-noun list, includes "Helix model" |
| `cytognosis-template-master/references/website.md:50, 230` | Same nav map and component list as above |
| Both skills' `assets/products/helix-model.png` | Dedicated shipped product mark asset |

**This directly contradicts the "internal-only" expectation, and it is not a new discovery in isolation: `FINALIZATION_PLAN_2026-07-09.md` (this same project, dated yesterday) already found the identical bug in the Claude Design export itself: "'Helix' ships as a fake fourth public product, 23 times across 14 files... Per your note, Helix is an internal org-structure draft, not a product."** That plan's step 4 schedules a fix by "regenerating the brand-identity skill from v11.2.0," but the brand-identity skill is a different artifact from cytoskills (see Part 3 note below). **The cytoskills tree audited here is not covered by that planned fix and carries the same defect independently, across five files.**

**Verdict and recommendation:** this is a live regression to correct, not a three-way vote to resolve. Remove Helix from all public-facing platform-architecture tables and the "always capitalize as a product name" rule in cytoskills (`cytognosis-branding/SKILL.md`, `01_brand_foundation.md`, `cytognosis-design-system-master/SKILL.md`, `cytognosis-writer/SKILL.md`, `cytognosis-template-master/references/website.md`), replacing with a footnote that Helix is the internal foundation model, not part of the disclosed product lineup. Archive rather than delete the `helix-model.png` assets, per the standing archive-over-delete rule. Add "cytoskills Helix cleanup" as its own line item alongside the existing brand-identity-skill regen in the finalization sequence (Part 3), since fixing one does not fix the other.

---

## PART 3: RELOCATION TARGETS

### Ground truth checked directly (not just planned)

`~/repos/cytognosis/branding` (the repo `cytognosis-org/SKILL.md` names as the design system's source of truth, local path `~/repos/cytognosis/branding`) **currently contains an unrelated React/Material-UI component library, "CytoStyle"** (`README.md`: `npm install @alimohammadiwork/cytostyle`; Storybook; Persian/Farsi IranYekan font files; audit docs like `CORRECTED_FIGMA_FIRST_DESIGN_SYSTEM_AUDIT.md`), **not** the `design-system/` target layout described in `branding_repo_plan.md`. This matches and confirms existing session memory ("branding repo holds CytoStyle; recovery gated on Ali chat") and `FINALIZATION_PLAN_2026-07-09.md` step 7, "Branding repo recovery (gated on the Ali conversation; Antigravity prompt ready)." **Do not write finalized design-system content directly into this repo until that gate clears.**

### (a) Where the finalized Claude Design export + consolidated guideline should live

Two destinations, serving different purposes, per the pattern used everywhere else in this consolidation (docs repo = narrative home of record; product/code repos = production mirror):

1. **`docs/07-Design/`** (docs repo, Obsidian-mirrored 1:1). Confirmed as the real, already-designated prose-spec home: `Website/CLAUDE.md` states "Design layer -> `07-Design/`" and "Brand identity -> vault `07-Design/` + `brand-identity` skill"; `ANTIGRAVITY-WAVE1-REVIEW_2026-07-08.md` records the explicit decision "`docs/07-Design/` ownership: docs repo owns prose spec; branding repo consumes." This is the correct landing spot for the finalized, reconciled guideline (the human and agent-readable spec), following the same two-variant rule (technical plus Obsidian plain-language companion) used for every other pillar. No blocker; can happen as soon as content is final.
2. **`~/repos/cytognosis/branding/design-system/`** (production CSS/token/asset mirror), per the already-agreed target layout in `Science and Platform/design-system-consolidation-2026-05/02_repo_organization/branding_repo_plan.md` (`references/01-12`, `tokens.css`, `LOGO.md`, `WRITING.md`, `IMAGERY.md`, `ACCESSIBILITY.md`, `profiles/`, `assets/`, `templates/`, `components/`, `preview/`, `data-viz/`). **This write is blocked** on the CytoStyle/Ali recovery gate above; stage the content but do not commit it there yet.

The skill packages themselves (`cytognosis-branding`, `cytognosis-design-system-master`, and five siblings) stay at `~/repos/cytognosis/cytoskills/skills/cytognosis/` for now. `branding_repo_plan.md` (2026-05-13) assumed these would eventually move to `branding/skills/`; that move is downstream of the same blocked gate and should not be attempted before it clears. Fix the content in place (Helix removal, neutral-scale sync, Lumen-palette and Space Grotesk doc-sync) rather than relocating files this round.

### (b) Where generated artifacts (themes, backgrounds, social) should live

Per the same `branding_repo_plan.md` target layout, once the gate clears: `branding/design-system/templates/` for social-cards.html, email-signature.html, one-pager.html, and the deck/ folder; `branding/design-system/assets/` for logos, icons, products, fonts, plus a new `backgrounds/` sibling folder (not yet named in the 2026-05-13 plan, since bokeh and gradient background generation is newer work; recommend `design-system/assets/backgrounds/` as a natural extension of the existing logos/icons/products/fonts pattern); `branding/themes/` for the VS Code, Starship, and Geany developer themes.

`FINALIZATION_PLAN_2026-07-09.md` step 5 already schedules this as "Artifact pack run... `raw_artifact_pack_spec.md` covers all 17 missing artifacts. Order: VS Code theme family, meeting backgrounds, LinkedIn, other social, Slack, letterhead," listed after Revision 3 and the v11.2.0 audit and publish steps, and before branding-repo recovery. Until the gate clears, keep newly generated artifacts staged inside `design-system-merge-2026-07/` (a `03_artifacts/`-style subfolder), clearly labeled as staged for the branding repo pending recovery.

### (c) Where the design-system-merge-2026-07 working folder should end up

**Archive, not promote wholesale, once distilled outputs have been extracted.** This folder is structurally identical to every other working-project folder in the consolidation: a large raw-extraction dump (2,000-plus files under `01_extracted/ali_latest/` alone, plus `01_extracted/v11_new/`) plus `02_review/` analysis and reconciliation notes, this file included. Per the standing rule restated everywhere in this consolidation ("archive, never delete"; governance.md: "working files, Claude Design uploads, exports, debug folders... stay in Claude Design," not the repo), only the distilled outputs (the guideline, reconciled `tokens.css`/`fonts.css`, chosen assets) get promoted to `docs/07-Design/` and, once unblocked, `branding/design-system/`.

**Do not archive yet.** `FINALIZATION_PLAN_2026-07-09.md` section 3 defines the still-open sequence this folder is mid-way through: Revision 3 (content, calm, profiles fixes, fresh Claude Design chat) -> audit v11.2.0 -> publish -> regenerate the brand-identity skill -> artifact pack run -> profiles settlement and accessibility re-audit -> **branding repo recovery (Ali gate)** -> interface templates re-pointed and built. `MASTER-DRIVE-PLAN_2026-07-09.md` additionally constrains the parallel consolidation mega-thread not to touch this folder "until the design chat lands." Archive this working folder only after branding-repo recovery completes and the design-system content actually lands in its target repo path, with a SUPERSEDED-style forward link, matching every other completed area in this consolidation.

### (d) Naming conventions to follow

- **Docs promoted to `docs/07-Design/`:** follow the `cytognosis-doc` skill (v5.5.0, per `HANDOFF-2026-07-10.md`): blockquote metadata header (Status, Date, Author, Audience, Tags), and the two-variant rule (technical canonical plus an Obsidian-mirrored plain-language companion, not a third "agent" variant unless it is a genuine coding work order).
- **Drive or exported documents:** `[Type]-[Topic]-[Version]-[Date]`, per `cytognosis-org/SKILL.md` (example: `Report-Design-System-v1-2026-07`).
- **Branding-repo semver:** follow `governance.md`'s existing discipline strictly (MAJOR for breaking token renames or removed components, MINOR for new tokens or profiles or icons, PATCH for fixes or doc clarifications), against the `VERSION` file. **Important correction to an earlier assumption in this document's drafting:** the project has already moved past a purely-v10.x line in practice. `FINALIZATION_PLAN_2026-07-09.md` targets **v11.2.0** as the next real published version (not an informal nickname), meaning a v10 to v11 major bump has already been adopted by the design-chat track, separately from `governance.md`'s still-unrevised "v10.0.0 as of 2026-05-13" snapshot. The "stale v10.1.0 version header" currently embedded in the shipped `colors.css` is itself flagged as a bug to fix in Revision 3, not a value to preserve. **Recommendation: once v11.2.0 publishes, update `governance.md`'s version snapshot and the cytoskills `Version 10.0` stamps across all 12 references in the same pass**, so the skill canon and the shipping design system carry one matching version string. Do not let cytoskills keep saying "Version 10.0" once the production tokens say v11.2.0.
- **Working-folder file names:** keep the existing `raw_*.md` prefix for extraction and reconciliation notes inside `02_review/` (matching `raw_neurodiverse_research_inventory.md` and this file), reserve un-prefixed, capitalized names (like `FINALIZATION_PLAN_2026-07-09.md`) for synthesized decision documents that get a `simple/` companion.

### Note on the separate "brand-identity" skill

`Website/CLAUDE.md` and `ANTIGRAVITY-WAVE1-REVIEW_2026-07-08.md` both reference a distinct **`brand-identity` skill** (vault `07-Design/`), separate from the `cytoskills`-hosted `cytognosis-design-system-master`/`cytognosis-branding` pair audited in Part 1. That skill is independently confirmed stale ("still v8.0 gradient," per the wave-1 review; "the live skill still carries an outdated signature gradient," per `V11.1_EXPORT_EVALUATION_2026-07-08.md`), and its regeneration from v11.2.0 is already step 4 of the finalization sequence. **This is not the same artifact as the cytoskills tree this report audits, and fixing one will not fix the other.** Both need the Helix and gradient corrections; only cytoskills' need was previously unflagged.
