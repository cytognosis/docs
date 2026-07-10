# v11.2.0 Audit and Google Guide Absorption Map

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: designers, stakeholders
> **Tags**: `design`, `design-system`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

**Date:** 2026-07-10. **Scope:** (A) line-by-line audit of `01_extracted/v11_new` (the
Claude Design export, self-labeled v11.2.0) against
`03_next_prompts/prompt_v11_revision_3_content_and_calm.md`, diffed where useful
against `01_extracted/v11_1`; (B) an absorption map from
`02_review/reference_google_brand_guide_v2_march2026.md` into v11.2.0, cross-checked
against `02_review/raw_canon_and_relocation.md`. No em dashes used, per house style.

**If you only read one thing:** v11.2.0 passes 29 of 35 checked items outright, 3
partial, 3 fail. The one real ship-blocker is a diagnosis-implying "good" copy
example still live in `references/02_voice_and_tone.md`, unfixed, despite the
Revision 3 report and CHANGELOG both claiming this exact file was fixed. Helix is
fully purged from this export, but the identical fake-fourth-product defect still
lives, unfixed, in 5 cytoskills files entirely outside this export's reach.

---

## 1. v11.2.0 scoreboard

| Area | Items checked | Pass | Partial | Fail |
|---|---|---|---|---|
| Part A, content and vocabulary | 10 | 8 | 1 | 1 |
| Part B, calm and neurodiverse | 6 | 5 | 1 | 0 |
| Part C, profiles and platform | 7 | 7 | 0 | 0 |
| Part D, color distinctiveness | 4 | 4 | 0 | 0 |
| Closeout (version, changelog, self-report) | 3 | 2 | 1 | 0 |
| Revision 2 preflight re-check | 5 | 3 | 0 | 2 |
| **Total** | **35** | **29 (83%)** | **3 (9%)** | **3 (9%)** |

The 3 fails: diagnosis-implying copy (Part A), oxlintrc em dashes (preflight),
oxlintrc missing 4 profile fonts (preflight). The 3 partials: Neuroverse callout
on only one of two landing pages (Part A), evidence appendix without real
citations (Part B), REVISION3_REPORT.md's mixed truthfulness (closeout).

---

## 2. Evidence per area

### Part A, content and vocabulary

| # | Item | Verdict | Evidence |
|---|---|---|---|
| 1 | Zero live "helix" outside uploads/CHANGELOG | **PASS** | `grep -rin "helix" 01_extracted/v11_new --exclude-dir=uploads --exclude=CHANGELOG.md` returns matches in exactly one file, `REVISION3_REPORT.md` (lines 19, 23, 24, 29, 91, 92), and all six are meta-commentary describing the fix, not live product content. Zero occurrences anywhere else, including `_ds_bundle.js` (see item 21). |
| 2 | Three-product tables, no fourth | **PASS** | `README.md:17-25` and `references/01_brand_foundation.md:58-62` both ship exactly 3 rows (Cytoverse, Cytoscope, Cytonome). |
| 3 | "Three systems" on both landing pages | **PASS** | `ui_kits/landing/index.html:335` "Three systems, working as one instrument." `Cytognosis Landing Page.html:197` identical heading. |
| 4 | Neuroverse callout added | **PARTIAL** | `Cytognosis Landing Page.html:239,279-280` carries a full dedicated Neuroverse section with the approved README language. `ui_kits/landing/index.html` has only a footer nav link, `:480 <a href="#">Neuroverse</a>`, a dead anchor (`href="#"`, not `#neuroverse`) with no callout paragraph anywhere in the file. The Revision 3 prompt's own item 4 discusses both landing pages in the same breath before calling for the callout; only one got it. |
| 5 | Founder story replaced with public-safe variant | **PASS, with a content note** | `Cytognosis Landing Page.html:110-112` reads "Cytognosis began with a 37-year search for a single answer. One person, ten misdiagnoses... one rare genetic mutation..." All three safety-critical facts land (37 years, ten misdiagnoses, one rare mutation) and the gene is never named (confirmed zero hits for BRCA/MTHFR/APOE/"the gene" patterns). This is a third-person paraphrase, not the verbatim first-person "WEB2 Shorter Hero" variant quoted in `raw_vocabulary_alignment.md` 4.4. Substance is safe; wording is not a verbatim match. |
| 6 | No diagnosis-implying copy | **FAIL** | `guidelines/type-body.card.html:23` is correctly fixed ("Cytognosis transforms complex biological and behavioral signals into interpretable phenotype vectors. Non-diagnostic by design."). But `references/02_voice_and_tone.md:88-93` still carries the exact flagged text, unchanged, still labeled the exemplar: `"Imagine knowing about a health condition years before you feel sick. Our AI analyzes your cells at the molecular level, finding patterns that signal disease long before traditional tests can detect anything.   ← good"`. This is the identical clause `raw_vocabulary_alignment.md` section 4.3 specified for replacement, still shipping as the design system's own "good" example, five lines above a newly added "three blindspots" closer that says "It maps trajectories; it does not diagnose" (`:103`), an internal contradiction inside one file. |
| 7 | Helix icon files deleted (line/solid/sprites/icons.card.html/ICONOGRAPHY.md) | **PASS** | `ls assets/icons/line,solid` shows no `helix.svg`. `grep helix` on both sprite sheets and `icons.card.html` returns nothing. `ICONOGRAPHY.md:38` reads `| Products | cytoverse, cytoscope, cytonome |`. |
| 8 | "GPS for Human Health" standardized | **PASS** | Confirmed consistent in `README.md:11,19`, `references/01_brand_foundation.md:25,62`, `WRITING.md:140`, `SKILL.md:4`, `guidelines/brand-voice.card.html:42`, and the previously-flagged `guidelines/type-display.card.html:24` (now reads "GPS for Human Health," not the short form). Zero remaining "GPS for Health" short-form hits. |
| 9 | Three blindspots module added | **PASS, with a fidelity note** | `references/02_voice_and_tone.md:95-103`, "## The three blindspots" with a 3-item list and a "so what" closer. Thematically correct (mechanistic/temporal/complexity blindness, renamed "Signals that don't speak / Labels that hide difference / Understanding that arrives late") but uses different labels and drops the supporting statistics (4+ molecular subtypes, 30-60% antidepressant failure rate, etc.) specified verbatim in `raw_vocabulary_alignment.md` 4.3. Reasonable editorial adaptation for a voice guide, not a literal transcription. |
| 10 | Personas replaced | **PASS** | Zero remaining "Lena Park" or "Moreau" hits outside `CHANGELOG.md`'s own changelog note. `[Name], [Title]` or `[Name], [Credentials]` placeholders confirmed in all four templates: `one-pager.html:187`, `email-signature.html:76-77,104-106`, `social-cards.html:144`, `deck.html:135,222,302`, plus `references/10_templates.md:52-53`. |

### Part B, calm and neurodiverse compliance

| # | Item | Verdict | Evidence |
|---|---|---|---|
| 11 | Body floor 16px, ACCESSIBILITY.md + typography.css | **PASS** | `ACCESSIBILITY.md:89-90` "Minimum body size: 16px web... Body text is never set below 16px." `tokens/typography.css:23` `--text-body: 1rem; /* 16px, default (never below this) */`. No remaining 14px body-floor contradiction (the one surviving "14px" hit, `ACCESSIBILITY.md:56`, is a contrast-exception rule for semi-bold labels, a different concern). |
| 12 | prefers-reduced-motion complete in animations.js + motion.css | **PASS** | `landing/animations.js:9-16` gates parallax `!reduce && (data-parallax="on" \|\| localStorage)`, never runs under reduced motion. Its injected `:33-37` reduced-motion block sets `animation:none` on the looping SVG elements, `scroll-behavior:auto`, and a global near-zero duration cap. `profiles/motion.css:127-136` disables all four infinite classes (`anim-pulse`, `anim-breathe`, `anim-spin`, `anim-shimmer`) with `animation:none !important; transform:none !important`. `tokens/motion.css:34-41` (the canonical, system-wide block) also forces `scroll-behavior: auto !important`. |
| 13 | Motion tokens consolidated onto --dur-/--ease- | **PASS, minor nit** | `profiles/motion.css:12-17` rewrote the `--m-*` scale as `var(--dur-fast, 150ms)` etc., referencing the canonical `tokens/motion.css` tokens with literal fallbacks. One fallback is stale: `--m-xxl: var(--dur-pulse, 1400ms)` but the real `--dur-pulse` is `1500ms`; cosmetic only, since the token always resolves first. |
| 14 | --measure line-length token added | **PASS** | `tokens/typography.css:71-73`, `--measure-narrow: 45ch`, `--measure: 68ch`, `--measure-wide: 80ch`. Applied at minimum in `tokens/base.css`, `guidelines/colors-fluorophore.card.html`, and both new components. |
| 15 | Lexend/Atkinson opt-in, self-host note | **PASS** | `ACCESSIBILITY.md:75` documents the opt-in reading-mode toggle, persisted via `localStorage` key `cg-reading-font`. `assets/fonts/README.md` lists exact `.woff2` files needed (core, reading-mode, and profile-specific faces) and explicitly keeps the CDN import until they exist. |
| 16 | Therapeutic evidence appendix with citations | **PARTIAL** | `ACCESSIBILITY.md:163-176`, section "8 · Therapeutic-design evidence" exists, correctly re-narrates the governing "calm by default, canonical-strong on recognition moments" principle, and names the evidence categories (NIH/NLM, chromotherapy, dyslexia and autism research). But line 176 explicitly defers the actual citations: "Sources are summarized rather than quoted; maintainers should attach the specific citations... when this appendix is formally published." `raw_neurodiverse_research_inventory.md` Section 1 has a ready, specific source table (document codes, paths, dates) that could have been cited directly; it was not. |

### Part C, profiles and platform readiness

| # | Item | Verdict | Evidence |
|---|---|---|---|
| 17 | Only three profiles, Lab folded to density toggle | **PASS** | `profiles/README.md:7,13-18,47-53` states three profiles (Foundation, Clinical, Research) with "Research · lab density" as a `data-density="lab"` sub-mode, not a fourth profile. |
| 18 | data-density grep, lab-example handling | **PASS** | `grep data-density` confirms the attribute is documented and used. `lab-example.jsx` still exists as a separate file but `profiles/README.md:79` explicitly reframes it as "holds the Research lab-density surfaces," a defensible reading of "fold," not a literal file deletion. |
| 19 | Clinical re-pointed to warm --cg-lp-*, magenta resolved | **PASS** | `profiles/README.md:32,35` "Backgrounds are the warm paper family (`--cg-lp-bg`...)" and "Magenta never appears in Clinical... Coral owns attention here." Zero magenta hits in `profiles/clinical-example.jsx`. |
| 20 | data-profile + skip-link on both ui_kits | **PASS** | `ui_kits/dashboard/index.html:109,111` `data-profile="research" data-density="compact"` + skip-link to `#dash-main`. `ui_kits/landing/index.html:179,181` `data-profile="foundation"` + skip-link to `#hero`. |
| 21 | CrisisBanner/ConsentPrompt exist, registered | **PASS** | Both ship `.jsx` + `.d.ts` + `.prompt.md` under `components/core/`. `_adherence.oxlintrc.json` carries JSX prop-validation rules for both, and `x-omelette.components` lists all 9 components (Badge, Button, Card, ConsentPrompt, CrisisBanner, DataBar, Input, MetricTile, Tag), matching REVISION3_REPORT.md's "confirmed: 9 components" claim exactly. `CrisisBanner.jsx:22-25` is `position:sticky` with `dismissable=false` default; `ConsentPrompt.jsx:17` initializes `checked=false` with the comment "consent OFF by default." |
| 22 | touch-min enforced | **PASS** | `components/core/ConsentPrompt.jsx:69,84` and `CrisisBanner.jsx:61` use `minHeight: 'var(--touch-min,44px)'`. `tokens/base.css:141` and `tokens/spacing.css:41` define the token. `Button.jsx` hardcodes `44px`/`48px` directly rather than referencing the token; functionally identical, just not wired through the variable (minor). |
| 23 | Extension side-panel width documented | **PASS** | `references/10_templates.md:111`, "Browser-extension side panel \| 360-400px \| Design the narrow layout at ~380px..." |

### Part D, color distinctiveness

| # | Item | Verdict | Evidence |
|---|---|---|---|
| 24 | Warm paper is the default surface, dark opt-in | **PASS** | `tokens/colors.css:181-184` defines the un-scoped default `--bg-1: var(--cg-lp-bg)` etc., identical to the explicit `[data-theme="light"]` block (`:194-198`), while `[data-theme="dark"]` (`:208-226`) is a separate override block. `README.md:111` states the rule in prose. |
| 25 | Cell-network motif asset added | **PASS** | `assets/images/cell-network.svg` exists. `LOGO.md:98-105` specs it fully: derivation, opacity ranges (0.04-0.10), `currentColor` usage, placement rules, explicit "not a substitute for the mark." |
| 26 | Fluorophore data-viz ramps | **PASS** | `references/12_dataviz.md` documents all 6 channels (DAPI, Alexa Fluor, GFP, MitoTracker, Rhodamine, UV) with emission wavelengths and pattern pairings. `profiles/dataviz.css:73-78` defines all 6 `--fluor-*` tokens matching the doc exactly. |
| 27 | Fluorophore story on a guidelines card | **PASS** | `guidelines/colors-fluorophore.card.html` renders a full merged 6-channel specimen field plus a legend, captioned "NON-DIAGNOSTIC · RESEARCH ILLUSTRATION." |

### Closeout

| # | Item | Verdict | Evidence |
|---|---|---|---|
| 28 | VERSION and SKILL.md both 11.2.0 | **PASS** | `VERSION` file contents: `11.2.0`. `SKILL.md:1-8` frontmatter `version: 11.2.0` and H1 "Cytognosis Design System, v11.2.0." |
| 29 | CHANGELOG 11.2.0 entry | **PASS** | `CHANGELOG.md:9-107` is a full, well-organized entry covering all four parts plus an honest "Known limitations" subsection. |
| 30 | REVISION3_REPORT.md exists, claims verify | **PARTIAL, mixed truthfulness** | See Section 3 below for the full breakdown. Of 4 spot-checked claims, 2 are confirmed false, 1 is an honest, verified disclosure, 1 is confirmed true. A 5th claim (diagnosis-copy fixed) checked separately in item 6 above is also false. |

### Revision 2 preflight re-check

| # | Item | Verdict | Evidence |
|---|---|---|---|
| 31 | oxlintrc zero em dashes | **FAIL, regression** | `grep -c "—" _adherence.oxlintrc.json` returns 2. Lines 34 and 38: `"Raw hex color — use a design-system color token via var()."` and `"Raw px value — use a design-system spacing token via var()."` `CHANGELOG.md:116-119` (the 11.1.1 entry) explicitly claims this exact file was fixed and "Verified: zero em dashes." It has regressed in 11.2.0, the second time this exact defect has round-tripped (11.1.0 shipped it, 11.1.1 fixed it, 11.2.0 reintroduced it). |
| 32 | 4 profile fonts in oxlintrc fontFamilies + regex | **FAIL, disclosed** | Neither location contains IBM Plex Sans, IBM Plex Mono, Source Serif Pro, or Recursive. `fontFamilies` lists only `["Atkinson Hyperlegible", "Inter", "JetBrains Mono", "Lexend", "Newsreader", "Space Grotesk"]`; the font-family lint regex names the same six. `REVISION3_REPORT.md`'s own "Discrepancies surfaced" section honestly names this exact gap and its root cause (profile fonts live in `profiles.css`, outside the compiler's `styles.css` `@import` closure). Disclosed, but still a checklist fail. |
| 33 | profiles/*.css no bare hex outside --pf-* | **PASS** | Clean sweep of `profiles.css`, `states.css`, `dataviz.css`, `a11y.css`; every hex literal sits on a `--pf-*` definition line. |
| 34 | No live archived-logo references outside archive/ | **PASS** | All hits for the 10 archived filenames (`cytognosis-mark.svg`, `cytognosis-dark*`, `cytognosis-light*`, `cytognosis-logo-only*`) land only in `CHANGELOG.md`, `LOGO.md`, and `PHASE2_REPORT.md`, all documentary prose explaining what is archived and why. Zero live `src=`/`href=`/`url()` embeds. |
| 35 | Simplified mark, no dead feGaussianBlur/filter defs | **PASS** | `grep "feGaussianBlur\|filter=\|<filter"` on `cytognosis-mark-simplified.svg` returns nothing. |

---

## 3. Defects by severity

| # | Defect | Severity | In-export? | Also in cytoskills? |
|---|---|---|---|---|
| D1 | Diagnosis-implying "good" example still live, `references/02_voice_and_tone.md:88-93`, contradicts the org's own non-diagnostic positioning | **Ship-blocking** | Yes, confirmed | Not directly checked; `raw_canon_and_relocation.md` 1.6 calls cytoskills' `voice.md` "identical in substance" to this file, so the same stale example likely exists there too. Recommend a direct grep of `cytognosis-branding/references/02_voice_and_tone.md` and `design-system-master/references/voice.md` before publishing either. |
| D2 | Helix ships as a live, named fourth public product (with a dedicated `helix-model.png` asset) across 5 cytoskills files | **Ship-blocking** | **No**, confirmed clean in `v11_new` | **Yes**, confirmed independently in `cytognosis-branding/SKILL.md`, `references/01_brand_foundation.md`, `design-system-master/SKILL.md`, `cytognosis-writer/SKILL.md`, `cytognosis-template-master/references/website.md`, per `raw_canon_and_relocation.md` Part 2 Section 6. This is the single most important reason "helix is purged" cannot be said of the whole system yet, only of this one export. |
| D3 | `_adherence.oxlintrc.json` carries 2 em dashes, a second-time regression of a rule stated as absolute | Cosmetic (lint is warn-level, not build-blocking) but flags a **fragile-fix process** | Yes | Not applicable, cytoskills has no equivalent compiler config |
| D4 | `_adherence.oxlintrc.json` missing 4 profile fonts from its allowlist | Cosmetic (warn-level; honestly disclosed; root cause understood) | Yes | Not applicable |
| D5 | REVISION3_REPORT.md contains 2 confirmed false claims (chromosome-icon rename that shipped no such asset; `_ds_bundle.js` helix residue that does not exist) | Cosmetic in product terms, **moderate in process-trust terms** | Yes, the report is part of this export | N/A (report is export-specific) |
| D6 | Therapeutic evidence appendix defers real citations | Cosmetic, but undercuts the appendix's own "evidence-driven, not stylistic" claim | Yes | cytoskills' `references/11_accessibility.md` is separately flagged in `raw_neurodiverse_research_inventory.md` as a stale, unreconciled copy carrying different, older citations; the two docs disagree and neither is fully cited to the current source table. |
| D7 | `README.md:201-214` "Iconography" section still describes Phosphor/Feather at 2px stroke, contradicting the actual shipped 1.6px custom 48-icon set (`ICONOGRAPHY.md`, `PHASE2_REPORT.md`) | Moderate, cosmetic, pre-existing (not a Revision 3 regression, not in its scope, but uncorrected) | Yes | Not verified; `raw_canon_and_relocation.md` suggests cytoskills' own `06_iconography.md`/`iconography.md` already got this right, so this drift may be isolated to `v11_new`'s top-level `README.md`. Worth a five-minute fix regardless. |
| D8 | Neuroverse callout missing from `ui_kits/landing/index.html` (dead `href="#"` nav link only) | Cosmetic | Yes | N/A, this file has no cytoskills equivalent |

---

## 4. Google guide absorption map

Source: `02_review/reference_google_brand_guide_v2_march2026.md` (the March 2026 Google
Doc extract) cross-checked against `02_review/raw_canon_and_relocation.md` (which
already resolved the doc's 4 identity conflicts against v11 and cytoskills, both
agreeing against the Google doc, on gradient, magenta-as-primary, accent font, and
icon stroke; treat those 4 values as settled and the Google doc's versions as
superseded, not open questions).

| Google guide section | Verdict | Target file / citation |
|---|---|---|
| Messaging framework (Revelation Arc, tone-by-context, problem framing) | **ALREADY IN v11.2** | `references/02_voice_and_tone.md` (Revelation Arc, tone-by-context table, three blindspots), `WRITING.md` |
| Taglines / one-sentence summaries | **ALREADY IN v11.2** | `guidelines/brand-voice.card.html` (tagline bank), `README.md:11,19`, `guidelines/type-body.card.html:35`. Diff the Google doc's full tagline list against this bank before archiving the doc, since only a condensed extract was available for this audit, not the full verbatim text. |
| Audience + funder tone tables | **ABSORB INTO v11.2** | `references/02_voice_and_tone.md`. The existing "Tone by context" table (lines 37-46) is organized by content type (grant proposals, investor pitches, social media), not by audience (funders, program officers, academic collaborators, patient advocates, media). A nonprofit relying on grant funding needs the audience axis; add it as a second table or a column. |
| Boilerplate (standard one-paragraph org description) | **ABSORB INTO v11.2** | `references/01_brand_foundation.md`. No consolidated boilerplate paragraph exists anywhere in v11.2 today; facts are scattered across `README.md`. |
| Google Docs template spec (page setup, pt sizes, block quotes, code blocks) | **KEEP IN GOOGLE DOC ONLY** | Tool-specific rendering guidance for a word processor; a CSS/token design system has no natural home for it. If refreshed, source colors and type scale from `tokens/colors.css` and `tokens/typography.css`, not the reverse. |
| Google Slides template spec (layouts, animation standards, slide rules) | **ABSORB INTO v11.2 (rules only)** | `references/10_templates.md`, cross-referencing `templates/deck.html`. The rules (one topic per slide, animation restraint, layout types) are tool-agnostic and worth documenting once; the actual `.gslides` file stays a Google Workspace production artifact, built from v11.2 tokens. |
| Email signature | **ALREADY IN v11.2** | `templates/email-signature.html` supersedes the Google doc's copy; this is the actively maintained version now. |
| Social sizes | **ALREADY IN v11.2** | `LOGO.md` (Social section), backed by real generated assets: `og-image.png` (1200x630), `avatar.png` (1:1), `linkedin-banner.png` (1584x396), plus `templates/social-cards.html`. |
| OG tags | **ABSORB INTO v11.2** | `references/10_templates.md`. The `og-image.png` asset exists and is specced, but zero live `<meta property="og:*">` markup exists anywhere in the tree (confirmed by direct grep; the one apparent hit was a binary-file false positive). Add the literal snippet. |
| Print CMYK + print stylesheet | **ALREADY IN v11.2 (partial)** | `references/10_templates.md:82-85` (CMYK for violet, azure, indigo, magenta), `templates/deck-stage.js:230,402` (`@media print` deck layout). Teal, coral, and semantic-color CMYK values are not yet added, and `one-pager.html`'s print behavior was not verified in this pass. |
| Five design motifs (molecular networks, data flow, light in darkness, organic geometry, temporal progression) | **ABSORB INTO v11.2 (consolidate, don't invent from scratch)** | `references/07_imagery.md`. Three of five already exist piecemeal and unnamed as a set: node/edge networks (`README.md:187-190`), light-in-darkness radial glow (`references/07_imagery.md:24`, `references/03_logo.md:10`), and 8px-grid data flow (`references/07_imagery.md:22`), plus the brand-new cell-network motif (`LOGO.md:98-105`). "Organic geometry" and "temporal progression" are not named anywhere. Recommend one canonical, named list in one file instead of four scattered mentions. |
| Photography | **ALREADY IN v11.2** | `IMAGERY.md` (five image pillars, palette and grading rules, sourcing checklist, specimen shot list), `references/07_imagery.md`. More detailed than the Google doc's version. |
| Pre-publish checklist | **ABSORB INTO v11.2 (consolidate)** | `CONTRIBUTING.md`. Scoped checklists already exist (`IMAGERY.md:57` photo-sourcing checklist, `WRITING.md:158` writing checklist) but no single cross-cutting pre-publish gate exists that also folds in the legal DO-NOT-PUBLISH list (no gene name, no ARPA-H/IGoR specifics, per `raw_vocabulary_alignment.md` section 1.5). |

**Conflicts already resolved, not open questions:** signature gradient, magenta-as-primary,
accent font (Newsreader over Source Serif Pro as the global default, with Source
Serif Pro surviving as the Clinical-profile default), and icon stroke (1.6px
custom 48-icon set over 2px Phosphor/Feather) were all adjudicated in
`raw_canon_and_relocation.md` Part 2 in favor of v11 and cytoskills, both
agreeing against the March 2026 Google doc on all four. Treat the Google doc as
stale on these specific values; no further reconciliation work needed.

---

## 5. Publish-readiness verdict

**Not yet publish-ready as a whole system, though this specific export is close.**
Fix D1 (diagnosis-implying copy) before any content is generated from this
design system for public or funder-facing use; it is a two-sentence edit in one
file. D3 through D8 are cosmetic and can ship with a follow-up ticket rather than
blocking. D2 is the real gate on the broader claim "Helix is gone": it is gone
from `v11_new`, not from cytoskills, and cytoskills is what actually drives
day-to-day content generation per the org's own skill-routing setup. Recommend
sequencing as: (1) fix `references/02_voice_and_tone.md` now, a trivial change,
(2) publish v11.2.0 from this export once that lands, (3) treat the cytoskills
Helix cleanup as its own tracked line item, not assumed-done by this export's
existence, matching the recommendation already on record in
`raw_canon_and_relocation.md`.
