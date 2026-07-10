# Design Critique: Profiles, Use Cases, Color Uniqueness, and Platform Readiness (v11_1)

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: designers, stakeholders
> **Tags**: `design`, `design-system`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

**Compiled:** 2026-07-09. **Scope:** `design-system-merge-2026-07/01_extracted/v11_1/` (content unchanged in the pending 11.1.1 export except mechanical fixes, so this critique applies to 11.1.1 as shipped). No em dashes used per house style.

**Reading time:** about 22 minutes. **If you only read one thing:** every area of this system shows the same failure mode, a rule gets stated once, clearly and well, then reimplemented two to four different ways across `profiles/`, `landing/`, and `components/`, so no single token change actually controls the system. Four focus-ring implementations, three motion-duration scales, three body-text-size floors, two dataviz ramps, two icon-library claims, and a profile system that every single file in `profiles/` still flags as "settlement pass pending." Fix the drift before adding anything new.

---

## Overall impression

**First impression.** The system reads far more finished than it is. Four well-voiced profiles, a real accessibility spec, a genuine color story, and a working landing page create an impression of production readiness. Every profile file (`profiles/README.md:1`, `profiles/profiles.css:1`, all four `*-example.jsx` files) carries the same header comment, "Profile settlement pass pending (see backlog)," and `SKILL.md:98-99` confirms the whole profile mechanism is "under review." The system is a strong draft wearing a finished coat.

**Usability.** For the people who will actually use these profiles, patients on a phone, clinicians on a dashboard, scientists in a workbench, the voice and tone layer (`WRITING.md`) is genuinely ready to ship today. The visual and motion layer is not: real, live scroll-coupled parallax and five different unbounded looping animations exist in the shipped landing page right now, not as a hypothetical risk.

**Visual hierarchy.** Strong at the token-definition level (type scale, heading-step ratios, profile-specific palette emphasis all check out). Weaker at the shipped-surface level, where `--muted` gray is applied to full paragraphs of real product copy, not just hints, undercutting the hierarchy the tokens were designed to protect.

**Consistency.** This is the system's central problem, see the BLUF above. Every one of the four critique areas below independently surfaces the same drift pattern.

**Accessibility.** The best-documented dimension by far, ACCESSIBILITY.md is honest about its own gaps and self-flags a pending re-audit rather than hiding it. But documentation quality is outrunning implementation: the checklist run below scores 21 of 45 items as a clean pass.

---

## Section A: Profiles vs. real use cases

**Framing.** First impression of the profile system is strong, four distinct, well-argued voices. Usability breaks down at the edges: the highest-stakes use case (patient phone app) is the least resolved. Visual hierarchy across profiles is intentional (Foundation loud, Clinical quiet, Research dense, Lab technical). Consistency is undermined by the standing "fold Lab into Research" question still being open two brief-cycles later. Accessibility-wise, Clinical's stated calm intent does not fully match its shipped background tokens.

### A1. Use-case-to-profile matrix

| Use case | Assigned profile | Source | Fit | Key issue |
|---|---|---|---|---|
| Public website, logged out | Foundation | `references: app-website BaseLayout` | Good | Heading scale (40-52px) is applied system-wide rather than scoped to true hero moments; `prompt_profiles.md:129` already recommends 28-32px for in-page headings and this has not been actioned |
| Public website, patient stories | Clinical | `app-website PostLayout` | Good in intent, gap in execution | Clinical's own surface tokens (`--pf-clinical-1: #F5F5FA`, profiles.css:153) come from the cool indigo-tinted "Ghost Day" family, not the warm `--cg-lp-bg: #F4F2EF` family the checklist requires for extended reading (Section 4.1, item 1) |
| Public website, admin | Research | `app-website AdminLayout` | Good | None material |
| Patient phone app (voice-first, anxiety-aware, crisis-safe) | Clinical | `app-phone` (mandatory) | At risk | Zero Flutter/Dart artifacts exist anywhere in v11_1; no "calm pulse" listening visual exists in any file read; no `CrisisBanner` or `ConsentPrompt` component exists anywhere; body-text floor conflicts three ways (14px vs. 16px vs. the template's own 17pt ask) |
| Clinician / web dashboard | Research | `app-web` logged-in routes | Good | Indigo-600 (full brand strength) is the default emphasis on a surface explicitly described as an 8-hour-session surface, see Section B item 4.1.3 |
| Researcher tools (Cytoverse workbench) | Research | `app-web` + `prompt_profiles.md` matrix | Good | `research-example.jsx`'s dense tabular layouts are the best-matched profile-to-surface pairing in the whole audit |
| Desktop app (internal hub, supervisor sidecar) | Research | `app-desktop` | Good on paper | The one scaffold that exists, `frames/macos-window.jsx`, is self-tagged `@ds-adherence-ignore -- omelette starter scaffold` and has zero Tauri wiring |
| Browser extension, patient mode | Clinical | `app-extension` | Good in intent | No side-panel-width component variant exists; every frame/canvas dimension in the system (`ios-frame.jsx` at 402x874px, `design-canvas.jsx`) assumes a far larger surface than a 320-400px side panel |
| Browser extension, internal mode | "Lab or Research," literally undecided | `prompt_template_extension.md` section 5 | Unresolved | Direct downstream symptom of the profiles brief's own open question 2 (fold Lab into Research?) never being closed |
| Decks, one-pagers, funder / grant materials | Foundation, no separate profile | `profiles/README.md` matrix + `templates/deck.html` etc. | Good | Best-served use case in the whole audit, see Section D |
| CLI, dev docs, terminal, logs | Lab | `profiles/README.md` matrix | Redundant | See A2 |

### A2. Profile-by-profile assessment

| Profile | Severity | Finding | Recommendation |
|---|---|---|---|
| Lab | Moderate | Visually and structurally near-identical to Research: same dark-ink surfaces (`--pf-lab-1: #1A1A2E` vs. Research's `--pf-lab-15/research-5: #13131F`), same violet/indigo-family accent, same tabular-mono treatment. `prompt_profiles.md:127` already flagged this as its own recommendation 2 and it remains unresolved two design passes later. The extension template's own brief cannot decide between "Lab or Research" for internal mode, a direct, concrete cost of leaving this open. | Fold Lab into Research as a `[data-density="terminal"]` toggle rather than a fifth (now fourth) standing profile. This resolves the extension template's ambiguity immediately and drops total profile count from 4 to 3. |
| Clinical, "does it implement the calm/therapeutic principles" | Critical | Mixed. Genuinely good: Source Serif Pro italic reassurance quotes, tabular figures on every numeric cell, quieter heading scale (22-30px vs. Foundation's 40-52px), and WRITING.md's Clinical section is the strongest copy work in the system (concrete next steps, human fallback, "just/simply/only" banned). Genuinely not good: `profiles/README.md:35` states "magenta never appears" in Clinical, yet `clinical-example.jsx:139-140` uses `--pf-clinical-11 (#E0309E, magenta 600)` as the alert-header accent color and dot, a direct contradiction inside the same profile's own documentation. Background tokens are the cool Ghost Day family, not the warm family the checklist calls for (see A1). Because the profile exists only as static example artboards, there is no verified reduced-motion or scroll behavior specific to a distressed reader, the single population this profile exists to serve. | Rewrite the Clinical "forbidden colors" line to match what the examples actually do (magenta permitted only as a small alert accent, matching the system-wide danger-token rule), or remove magenta from the alert example and enforce the "never" literally. Either is fine; the current state, where the rule and the example disagree, is not. Separately, re-point Clinical's surface tokens to the warm `--cg-lp-*` family. |
| "Clinical-Patient" vs. "Clinical-Clinician" split (open question 1 and 5 in `prompt_profiles.md`) | Resolved, needs documenting | Not a real open question. The platform templates already resolve it: a clinician acting as an analyst gets Research (`app-web` AdminLayout, `app-desktop`), and only the patient's own view stays Clinical. `profiles/README.md:63` states this exact logic already ("clinician acting in clinical mode" vs. "clinician acting in analyst mode"). | Close the open question in `prompt_profiles.md` explicitly rather than leaving it live; no fifth profile is needed. |
| Funder / deck profile (implicit question in the task brief) | Resolved, no gap | Foundation covers decks adequately; `templates/deck.html`, `deck-stage.js`, `one-pager.html`, and `social-cards.html` are the most production-shaped artifacts in the entire audit (real synthetic content, a genuinely complete 622-line interactive deck component, not a stub). | No new profile needed. If deck density ever becomes a real problem, treat it the same way as Lab, a density toggle on Foundation, not a new register. |
| Missing: a real crisis/safety visual language | Critical | This is the sharpest gap in the whole audit. The Clinical audience paragraph in `prompt_profiles.md:33` describes someone "anxious or uncertain... reading the screen with reduced mental bandwidth," and the phone template's own brief requires a `crisis-banner` and `consent-prompt` "from the Design System." Neither exists anywhere in v11_1's `components/` directory, which contains only Button, Badge, Card, Input, Tag, DataBar, and MetricTile. | Build `CrisisBanner` and `ConsentPrompt` before any other net-new component work. This blocks the single highest-stakes surface in the platform. |

### A3. Recommended settled profile lineup

**Foundation, Clinical, Research.** Three profiles, not four. Fold Lab into Research as a density toggle rather than a standing register. This:

- Directly answers `prompt_profiles.md`'s open question 2 (yes, fold it).
- Directly unblocks the extension template's own unresolved "Lab or Research" choice for internal mode.
- Leaves the "Clinical-Clinician" question closed as already-resolved by the template layer (see A2), not reopened as a fifth profile.
- Requires no new profile for decks or funders; Foundation plus the existing deck templates already serve that use case well.
- Requires urgent, separate component work (CrisisBanner, ConsentPrompt) that is not a profile problem at all, it is a missing-component problem that sits underneath whichever profile ships on the phone.

---

## Section B: Neurodiverse checklist run

**Framing.** First impression: the checklist itself (Section 4 of `raw_neurodiverse_research_inventory.md`) is excellent and this system was clearly written with real awareness of it, most rules exist somewhere in the token layer. Usability and accessibility both suffer from the same drift problem named in the BLUF. Visual hierarchy is well specified in tokens and poorly enforced in shipped CSS. Consistency is the dominant theme across every subsection below.

**Scorecard.** 45 items scored PASS, PARTIAL, FAIL, or ABSENT (no evidence either way; not the same as a fail). Methodology note: the checklist itself asks for pass/fail/absent; PARTIAL was added here where the rule is documented correctly but not enforced, since collapsing that into a flat pass or fail would misrepresent the finding.

| Subsection | Pass | Partial | Fail | Absent | Items |
|---|---:|---:|---:|---:|---:|
| 4.1 Tokens and color | 4 | 2 | 2 | 0 | 8 |
| 4.2 Typography | 6 | 1 | 2 | 0 | 9 |
| 4.3 Motion | 1 | 0 | 6 | 1 | 8 |
| 4.4 Layout and interaction | 2 | 0 | 5 | 1 | 8 |
| 4.5 Copy and content | 8 | 0 | 1 | 3 | 12 |
| **Total** | **21** | **3** | **16** | **5** | **45** |

**Clean pass rate: 21 of 45 (47%).** Counting partials as half credit moves this to roughly 53%. Sixteen items fail outright, concentrated almost entirely in motion (6 of 8) and layout and interaction (5 of 8), the two sections the org's own prior research already named as the highest-leverage risk category.

### 4.1 Tokens and color

| # | Item | Verdict | Evidence | Recommendation |
|---|---|---|---|---|
| 1 | Extended-reading backgrounds are warm/cool low-saturation, never pure white or black | Pass | `tokens/colors.css:141-157`, warm `--cg-lp-bg #F4F2EF` and cool `--cg-day-50 #F8F8FC` both exist; pure white (`--pf-clinical-3`) is scoped to small cards only, which the source rule explicitly permits | None |
| 2 | Dark neutrals carry a consistent hue tint, never neutral gray or `#000000` | Pass | `tokens/colors.css:126-133`, `--cg-abyss #0A0A14` through `--cg-neutral-500 #50506E`, all indigo-hued | None |
| 3 | A pastel 300-400 token set exists and is used on daily-use/8hr surfaces, separate from full-saturation 600 tokens | Fail | Research, the profile explicitly built for "scientists... across 8-hour sessions" (`profiles/README.md:41`), defaults its emphasis to `--cg-indigo` (600, full brand strength), not `--cg-indigo-300`, per `profiles/profiles.css:97` | Re-point Research's `--emphasis` to the 300-shade token; reserve 600 for short-exposure marketing use as the token naming already intends |
| 4 | The lowest-contrast text token is documented as non-content-only and never used on content | Fail | `landing/styles.css`, `--muted #6F7178` is applied to full-sentence product copy via `.section-sub` and `.sc-body`, not just hints or labels | Swap `.section-sub`/`.sc-body` to the secondary text token; reserve `--muted` for labels and metadata only, matching its own documented intent |
| 5 | Body-text links on light backgrounds clear 5:1, not the decorative accent token | Partial | Underline-as-non-color-cue is confirmed (`profiles/a11y.css:30-35`) but no independent contrast measurement of Clinical's actual link color was performed | Run a direct contrast check on Clinical's link color against `#F5F5FA` and record the result in ACCESSIBILITY.md |
| 6 | Danger/error tokens restricted to short phrases, icons, large text, never body copy | Pass | Magenta and coral usage in `clinical-example.jsx`'s alert card is confined to a small label, dot, and bordered callout box, not body-copy color | None (see A2 for the separate documentation-contradiction finding) |
| 7 | Colorblind-safe pairing table exists; no component relies on color alone | Pass | `references/04_color_system.md:127-131` and `ACCESSIBILITY.md` both document the pairing table; `profiles/dataviz.css` ships pattern overlays (dots, lines, grid, crosshatch, waves, chevron) as a non-color differentiator | None |
| 8 | System names which token is "calm default" vs. "canonical strong," with a rule for when each applies | Partial | Documented clearly at the family level (`README.md`, `references/04_color_system.md`) but not enforced, see item 3 above | Add a lint-style check (even a manual pre-ship checklist item) verifying profile `--emphasis` values point at 300-shade tokens on daily-use surfaces |

### 4.2 Typography

| # | Item | Verdict | Evidence | Recommendation |
|---|---|---|---|---|
| 1 | Minimum body font size 16px+ (18px long-form) | Fail | Three different numbers live simultaneously: `tokens/typography.css:21` states 16px "never below this"; `ACCESSIBILITY.md:80` states "Minimum body size: 14px web, 10pt print"; `prompt_template_phone.md:163` requires 17pt for Clinical patient-facing body text | Ratify one number system-wide. Recommend keeping 16px given the weight of neurodiversity evidence cited elsewhere in the org's own research inventory (Section 5 of `raw_neurodiverse_research_inventory.md` already flags this exact conflict and recommends the same) |
| 2 | Measure does not exceed 75ch (target ~68ch) | Partial | `tokens/typography.css:69` default `--measure: 65ch` is fine, but `--measure-wide: 80ch` exceeds the ceiling and no evidence confirms it is never applied to body copy | Audit where `--measure-wide` is actually used; rename or scope it away from body text if it is |
| 3 | Line height >= 1.5 for body | Pass | `tokens/typography.css:36`, `--lh-body: 1.6` | None |
| 4 | No `text-align: justify` anywhere | Pass | No instance found across all files read; not an exhaustive repo-wide grep, treat as high confidence, not certainty | None |
| 5 | Accessible reading-mode font stack shipped, self-hosted, persists choice | Fail | Mechanism exists and is well designed (`profiles/a11y.css:16-27`, localStorage persistence per `README.md`), but fonts load via Google Fonts CDN `@import` (`profiles/profiles.css:7-10`), and `README.md`'s own "Font Substitution Note" admits this needs fixing for production | Self-host Lexend and Atkinson Hyperlegible `.woff2` files now; the gap is already self-documented, just not actioned |
| 6 | Decorative fonts never appear in body/label/form roles | Pass | Newsreader and Source Serif Pro scoped strictly to the `.q` pullquote class (`profiles/profiles.css:44`) | None |
| 7 | Serif scoped to pullquotes of 3 sentences or fewer | Pass | Confirmed in both the token architecture and the Clinical example's single-sentence quotes | None |
| 8 | No ALL CAPS body/labels; uppercase eyebrows have letter-spacing >= 0.08em | Pass | `tokens/typography.css:51-52`, `--ls-label: 0.08em`, `--ls-caps: 0.12em`, both meet or exceed the floor | Minor aside: several inline JSX styles set `letterSpacing` as a bare number (for example `letterSpacing:3` in `foundation-example.jsx`), which is not a valid CSS unit for that property and may render as `normal` in some browsers; worth a follow-up fix, does not change this item's score since the token layer is correct |
| 9 | Heading steps each >= 20% larger than the level below | Pass | `tokens/typography.css:11-17`, every step from h6 (16px) to display (61px) exceeds 20% | None |

### 4.3 Motion

| # | Item | Verdict | Evidence | Recommendation |
|---|---|---|---|---|
| 1 | Reduced motion replaces spatial transforms with opacity-only, not just a sped-up wrapper | Fail | `profiles/states.css:193-206` crushes durations to `0.01ms`, a fast wrapper around the same transform, not an opacity-only substitution; only nine named `.anim-*` classes in `profiles/motion.css:126-134` get a real `transform:none` override | Extend the `transform:none` override to every animated selector, not just the nine named classes |
| 2 | Scroll-jacking libraries destroyed, not paused, under reduced motion | Absent | No scroll-jacking library exists in the codebase to evaluate (confirmed no Lenis/GSAP); native `scroll-behavior:smooth` is reset via the blanket `!important` rule | None needed unless a scroll library is added later; if one is, wire an explicit destroy call |
| 3 | No default, unconditional scroll-coupled parallax | Fail | `landing/animations.js:318-336`, `layerParallax()` drives scroll-linked `translateX` for every visitor who has not set the OS-level reduced-motion flag; this is exactly the pattern the org's own prior research names as the single highest risk in the whole corpus | Remove scroll-coupled parallax entirely, or gate it behind an explicit opt-in rather than opt-out |
| 4 | No infinite peripheral looping animation under any setting | Fail | `profiles/motion.css:82-84,101` (`.anim-pulse`, `.anim-breathe`, `.anim-spin`, `.anim-shimmer`, all `infinite`) and `landing/animations.js:23-25` (`.cg-node`, `.cg-ring`, `.cg-travel`, all `infinite`) run forever unless the OS preference is set | Cap every loop with a finite iteration count or a pause-after-N-cycles behavior by default, not only under reduced motion |
| 5 | No autoplay beyond 5s (internal target 3s/250px) without a pause control | Fail | Same citations as item 4; loops are unbounded with no pause affordance in any markup read | Add a visible pause control to any surviving looping animation |
| 6 | No flashing/blinking faster than 3Hz | Pass | Fastest cycle found is 900ms (about 1.1Hz), well under the threshold | None |
| 7 | Duration controlled by a small set of named tokens, not hardcoded | Fail | `profiles/motion.css:10-15` ships a second, parallel duration scale (`--m-xs` through `--m-xxl`) alongside the canonical `--dur-*` tokens, and both files additionally hardcode raw millisecond values directly on selectors (for example `2000ms`, `3200ms` in `profiles/motion.css:82-101`; roughly 15 scattered raw values across `landing/styles.css`) | Delete the parallel `--m-*` scale; route every duration through `--dur-fast/base/slow/slower` with no raw literals left in either file |
| 8 | Stagger step capped at ~45-60ms | Fail | Three different values ship simultaneously: 60ms (`profiles/motion.css:107-116`, in range), 120ms (`profiles/motion.css:118-123`, exceeds), and 90ms (`landing/styles.css:134-138`, exceeds) | Pick one value (recommend 60ms, the one already in range) and remove the other two |

### 4.4 Layout and interaction

| # | Item | Verdict | Evidence | Recommendation |
|---|---|---|---|---|
| 1 | Section padding generous and consistent, not ad hoc | Fail | Three unreconciled values: 80px/48px documented (`tokens/spacing.css`, `references/09_layout.md:27-28`), 124px shipped (`landing/styles.css:92`), 96px shipped elsewhere (`ui_kits/landing/index.html:72`) | Pick one desktop and one mobile value and apply them everywhere; right now three different pages disagree with the spec and each other |
| 2 | No section ships 2+ competing primary CTAs in one zone | Pass | Hero and closing sections of `ui_kits/landing/index.html` each pair exactly one filled primary with one lower-weight secondary (lines 211-214, 461-464), matching `Button.prompt.md:28`'s explicit rule | None |
| 3 | Consistent section pattern (label, headline, subhead, body); constant nav location | Pass, single-page caveat | Confirmed within the one marketing page reviewed; sticky nav at `ui_kits/landing/index.html:182`; cross-page consistency was not verifiable since only one page exists to check | Re-verify once `app-website`'s multi-page scaffold exists |
| 4 | Dense groupings capped (~4 items) with an explicit "show more" | Fail | `ui_kits/landing/index.html:399-429` ships 6 capability cells at once with no show-more; `ui_kits/dashboard/index.html:356-436` shows 6 of 1,847 subjects as a text caption only, no pagination control rendered | Add a real show-more/pagination control to both surfaces |
| 5 | 44x44 (40x40 icon-only) touch targets | Fail | Component definitions are correct (`Button.jsx`, `Input.jsx` both 44px+), but shipped usage fails repeatedly: dashboard filter buttons, nav links, and the "Export CSV" badge in `ui_kits/dashboard/index.html` all ship under-sized with only small padding, no min-height | Enforce the `--touch-min` token (already defined at `tokens/spacing.css:41`) on every interactive element in both ui_kits, not only in the component library |
| 6 | Visible focus indicator >= 3:1, no bare `outline: none` | Fail | Four non-identical mechanisms coexist: `tokens/base.css` (3px azure-300 outline), `profiles/states.css` (outline:none plus a box-shadow ring, reachable only via a specific attribute combination), `landing/styles.css` (a locally reimplemented 3px outline bypassing the design-system token entirely), and `Input.jsx` (a much fainter 2px, 0.15-alpha ring). Each individually has a replacement for `outline:none`, so none is a bare removal, but there is no single shared, contrast-verified focus system | Consolidate to one `--focus-ring` implementation referenced everywhere; retire the landing-page-local reimplementation and the Input-specific faint variant |
| 7 | Holds at 200% zoom, no truncation or forced horizontal scroll | Absent | Not testable from static files without a rendering pass; `clamp()`/`ch`/`1fr` usage is zoom-friendly in principle, which is not the same as verified | Run an actual 200% zoom pass on both ui_kits and the landing page before claiming this item |
| 8 | `prefers-contrast: more` override exists and is wired beyond the profile layer | Fail | The override exists only in `profiles/a11y.css`. Neither shipped ui_kit sets a `data-profile` attribute anywhere, so the override, and every other profile-scoped accessibility rule, never activates on the system's own showcase pages | Set `data-profile` on both ui_kits immediately; this is a one-line fix that currently silently disables an entire accessibility layer on the system's own demo surfaces |

### 4.5 Copy and content

`WRITING.md` is the strongest artifact in the whole audit; most of this section passes cleanly.

| # | Item | Verdict | Evidence | Recommendation |
|---|---|---|---|---|
| 1 | No banned word appears in shipped copy | Pass | No instance of the banned list found in sampled copy; note "transforming" in `foundation-example.jsx:22` is adjacent in spirit to hype language but is not on the literal banned list | Consider adding "transforming" and similar near-miss words to a watch list, not a hard fail |
| 2 | Health-outcome claims retain uncertainty language, no diagnosis implication | Pass | `clinical-example.jsx`'s trajectory and alert copy ("still well within your range," "not an emergency, but...") and `WRITING.md`'s non-diagnostic rules are both consistent and strong | None |
| 3 | Person-first phrasing for medical/disability references | Absent | No disability-reference copy was encountered in the sampled files to confirm or deny; the org-wide rule exists in `README.md` | Spot-check this specifically the next time patient-facing disability-adjacent copy is written |
| 4 | General/landing copy scores Flesch-Kincaid grade 7-9 | Absent | No reading-level scoring tool was run against actual shipped copy; no CI hook for this exists in the design system itself (distinct from `app-website`'s own future requirement to run this check) | Run an FK check against the actual landing page copy and record the score |
| 5 | No sentence exceeds ~25 words as a matter of routine | Pass | Spot-checked sentences in `WRITING.md` and the profile examples are consistently short | None |
| 6 | No em dashes; Oxford comma; active voice | Pass | Confirmed as a repeated, explicit hard rule across `README.md`, `WRITING.md`, and `profiles/README.md`; no em dashes observed in any sampled copy | None |
| 7 | Every major section closes with a plain-language summary before its CTA | Absent | Not clearly demonstrated either way; the profile examples are isolated artboards rather than full page flows, and the landing ui_kit's `.section-sub` reads as a lead-in, not a closing summary | Verify this pattern explicitly once full page flows exist |
| 8 | No page uses more than 2 distinct metaphors | Pass | "Map / Sensor / Navigator" (Cytoverse/Cytoscope/Cytonome) and "trajectory / coordinates" read as one coherent cartography metaphor family, consistent with the org's own approved signature metaphor ("GPS for health"), not metaphor-stacking | None |
| 9 | Acronyms/technical terms defined on first use per page | Pass | Foundation and Clinical copy avoids undefined jargon; Research profile's use of unexplained technical shorthand (IL-6, TNF-alpha, bh-corrected) is correct and expected given Research's own "highest precision" voice dial in `WRITING.md`, not a violation | None |
| 10 | Copy register matches its surface (Foundation/Clinical/Research/Lab dials), not one uniform tone | Pass | `WRITING.md`'s dial table and before/after examples per profile are clear and well differentiated | None |
| 11 | Clinical error/empty-state/alert copy names a concrete next step and a human fallback | Pass | `WRITING.md`'s Clinical examples consistently do this ("Call your care team today," "contact your care team if this keeps happening") | None |
| 12 | Long-form pages/documents open with a BLUF-style anchor line | Fail | None of the design system's own documentation files (`README.md`, `ACCESSIBILITY.md`, `WRITING.md`, `profiles/README.md`) open with a reading-time or "if you only read one thing" anchor, unlike the org's own research documents (this file's own sibling, `raw_neurodiverse_research_inventory.md`, does this consistently) | Add the same BLUF convention to the design system's own top-level docs; low severity, applies to internal documentation, not shipped product copy |

---

## Section C: Color uniqueness

**Framing.** First impression of the palette-as-documented is distinctive and confident. First impression of the palette-as-shipped is more mixed: the flagship example artboard (`foundation-example.jsx`) reads as a well-executed but generic dark-mode AI product hero. Usability is unaffected either way (color choice here is a brand question, not a functional one). Visual hierarchy and consistency are addressed below with concrete evidence. Accessibility overlaps with Section B and is not repeated here.

### C1. What is genuinely distinctive

| Evidence | Detail | Where it currently lives |
|---|---|---|
| Fluorophore wavelength naming | Violet=DAPI ~461nm, Azure=Alexa Fluor 488 ~488nm, Indigo=UV ~358nm, Teal=GFP ~509nm, Coral=MitoTracker ~576nm, Magenta=Rhodamine ~565nm (`references/04_color_system.md:9-16`) | Only in `guidelines/colors-brand.card.html:28-53`, an internal build-reference card per `SKILL.md:87-92`. Never appears in the shipped landing page or any user-facing copy checked |
| Warm paper neutral family | `--cg-lp-bg #F4F2EF`, sage `#A7C68A`, warm yellow accent `#FFC845` (`tokens/colors.css:145-163`) | Already shipped as the actual landing-page hero background (`landing/styles.css:12-13`), a genuine, already-realized differentiator versus dark-mode-only AI SaaS |
| Explicit forbidden-palette table | Tailwind Indigo `#6366f1`, Material Purple `#9c27b0`, Bootstrap Primary `#0d6efd`, each with a stated reason ("too SaaS," "no biological warmth," "too electric, clinical") | `references/04_color_system.md:120-125`, a level of self-aware intentionality most design systems never document |
| Biology-coded icon families | Cell membrane, nucleus, mitochondria, DNA helix, RNA, genome (`references/06_iconography.md:16`) | Documented but see C2 for a naming inconsistency with the top-level icon library claim |
| Logo's radial construction | PHASE2_REPORT.md documents the mark as built from a "ring" gradient plus an "orb radial" and a "node radial" (`PHASE2_REPORT.md:16`), a describable circular, cell-like geometry | Confined to logo construction; not reused anywhere else in the UI as a recurring motif |
| Colorblind-safe pairing table plus pattern-overlay dataviz | Six pattern types (dots, lines, grid, crosshatch, waves, chevron) as genuine non-color differentiators | `profiles/dataviz.css:81-86`, real rigor beyond the legal minimum |

### C2. Where it collapses into generic

| Evidence | Detail | Severity |
|---|---|---|
| Flagship hero artboard | `foundation-example.jsx`'s dark ink background, 135-degree violet-azure-indigo gradient-clipped headline, and radial violet glow is structurally identical to the common 2023-2026 "AI startup" visual trope (dark canvas, diagonal cool gradient wash, soft glow), independent of the specific hex values used | Moderate |
| Interior sections of the actual shipped page | The hero itself is warm (a real win, see C1), but `.trajectory`, `.neuro`, and `.closing` sections (`landing/styles.css:257,310,345`) revert to dark night backgrounds with violet radial glows, the same generic register the hero avoids | Moderate |
| Gradient spec card | `guidelines/colors-gradients.card.html` renders a plain 135-degree violet-to-azure-to-indigo bar; stripped of its caption text, it is visually indistinguishable from any generic AI-product gradient chip. Distinctiveness lives entirely in the words, not the pixels | Minor |
| Two conflicting dataviz ramp specs | `profiles/dataviz.css` and `references/12_dataviz.md` disagree on both series order and hex values for the same named ramps; `profiles/dataviz.css:1` is separately flagged "settlement pass pending" | Moderate |
| Two conflicting icon-library claims | `README.md`'s file manifest states the primary icon library is Phosphor Icons CDN, while `ICONOGRAPHY.md`/`references/06_iconography.md` describe a custom biological icon set (cell-membrane, mitochondria, genome). Unclear if these coexist by design or drifted apart | Minor |
| Unfulfilled photography direction | `IMAGERY.md:80` notes real photography has not been commissioned yet ("use explicit placeholders"); the shipped page instead uses abstract SVG glassmorphism and gradient glows, close to the "particle-system tech swirls" the org's own imagery doc explicitly warns against (`references/07_imagery.md:46-51`) | Moderate |
| Retired logo files still in production | The shipped landing page references `cytognosis-light.svg`/`cytognosis-dark.svg`, both marked retired in `LOGO.md:100`, instead of the current 2026-07 mark | Minor |

### C3. Five concrete moves, ranked by leverage, all compatible with the calm-by-default rules

1. **Surface the fluorophore story on a real page.** Move it out of internal guideline cards and onto the About or Platform page as a short, calm, factual caption under the palette, or as deck footnotes. This costs nothing against the calm rules since it is information, not motion or saturation.
2. **Make the warm paper family the default surface everywhere, not just the landing hero.** Extend `--cg-lp-bg` and its neighbors into the mid-page narrative sections that currently drop into dark-violet-glow mode, and re-point Clinical's background tokens to this family (this also closes the Section B, item 4.1.1-adjacent gap noted in A2). One move, two benefits.
3. **Turn the logo's ring/orb/node radial geometry into a recurring UI motif.** Radial-gradient card accents, circular status dots, a signature rounded "cell membrane" corner treatment on cards, rather than confining that geometry to the mark alone. This is a shape-language move, not a saturation or motion move, so it does not conflict with any therapeutic-design rule.
4. **Resolve the two competing dataviz ramp specs into one, and name the resolved ramp's stops after their source dyes in any public-facing legend**, not only internally. Charts become brand storytelling, not just chrome.
5. **Replace the abstract gradient-glow hero treatment with the already-commissioned microscopy imagery** (`glass-brain.png`, `molecular-network.png`, `dna-helix.png` already exist as static assets) as the default section visual, restoring the "scientific grounding" pillar the system's own `README.md` names as mission-critical.

---

## Section D: Platform template readiness

**Framing.** First impression varies sharply by template, website and decks look ready, phone and extension do not exist yet in any concrete sense. Usability for a real developer picking this up cold would be good for `app-web`'s component layer and poor for `app-phone`'s total absence of Flutter artifacts. Visual hierarchy and consistency are addressed per-template below. Accessibility carries over from Section B; the gaps below are structural/scaffolding gaps, not a repeat of the checklist.

| Template | What v11_1 already provides | What is missing | Severity |
|---|---|---|---|
| **Website** (Astro) | A full working reference implementation: the shipped landing page plus `landing/styles.css`; Foundation/Clinical/Research example JSX; real, non-lorem social card templates with actual copy (`templates/social-cards.html:71-160`); a fluid `clamp()` type scale; two proven breakpoints (1000px/720px) in the shipped page | No reusable breakpoint or type-ramp tokens outside that one page's local CSS (zero hits for `@media`/`breakpoint` anywhere in `tokens/`, `guidelines/`, or `references/10_templates.md`); no skip-to-content link in the shipped markup; no Lighthouse or reading-level CI hook referenced anywhere; the profile system itself is flagged "settlement pending" (`SKILL.md:98-99`), undercutting the per-layout profile routing this template depends on | Moderate |
| **Phone** (Flutter, voice-first, crisis-safe) | Clinical profile intent; a 6-icon "Crisis and safety" icon family already exists (shield, alert-triangle, heart-pulse, support, flag, info) | Zero Flutter or Dart artifacts anywhere in v11_1; no "calm pulse" listening-state visual exists in any file; confirmed zero `CrisisBanner`/`ConsentPrompt` component anywhere; body-text floor conflicts three ways (see B, 4.2.1); no Dynamic Type guidance | Critical |
| **Web** (React 19 + Vite) | The full core component set (Button, Badge, Card, Input, Tag, DataBar, MetricTile); Foundation and Research profile examples; light/dark token families ready for a theme switcher; a maskable PWA icon already spec'd (`LOGO.md:85`) | No print stylesheet matching the required "print a report, no nav, single column" behavior; the only `@media print` implementation in the system is `templates/deck-stage.js`'s slide-per-page pagination, a different problem, and `templates/one-pager.html:9` only sets `@page{size:letter;margin:0}` with no override logic. No calm-pulse voice affordance visual anywhere (same absence as phone). No full PWA icon manifest beyond the single maskable icon | Critical (two Definition-of-Done items directly blocked) |
| **Desktop** (Tauri v2) | `frames/macos-window.jsx` renders convincing macOS-style chrome (traffic lights, sidebar, toolbar, search field); Research profile example; a full icon export set ready for PNG/ICO/ICNS packaging (`LOGO.md:84`) | `macos-window.jsx` is explicitly self-tagged `@ds-adherence-ignore -- omelette starter scaffold` with zero real Tauri wiring, it is presentation chrome for mockups and screenshots, not app scaffolding, despite living in a `frames/` directory that could suggest otherwise (this applies equally to the `ios-frame.jsx` scaffold and to any equivalent copy under `ali_latest/frames/`); no ICO/ICNS repackaging pipeline is documented | Moderate |
| **Extension** (Manifest V3) | Clinical and Research profile examples as a starting voice register | Confirmed zero side-panel-width tokens or components anywhere (repo-wide check for "side panel"/"extension" returns nothing relevant); confirmed zero Manifest V3 artifacts; no compact/dense component variant exists, all seven shipped components target normal desktop density; every frame/canvas in the system assumes a far larger surface than a 320-400px side panel; the "Lab or Research" indecision for internal mode (see A2) remains unresolved and blocks this template's own profile assignment | Critical |

**Deck and one-pager templates, for contrast.** `templates/deck.html`, `one-pager.html`, `social-cards.html`, and `email-signature.html` all contain specific, coherent synthetic content (a real research narrative with named cohorts, accuracy figures, and a named clinician), not placeholder text, and `deck-stage.js` is a genuinely complete 622-line interactive component with keyboard navigation, print pagination, and state persistence. This is the most production-ready corner of the entire system and a useful proof that the rest of the audit's findings are about drift and incompleteness, not a lack of capability.

---

## What works well

- `WRITING.md` is publication-ready today. The per-profile voice dial table, the before/after examples for errors, empty states, and alerts, and the non-diagnostic safety rules are consistently strong across every document checked.
- The colorblind-safe pairing table and the pattern-overlay dataviz alternatives represent real rigor beyond what any regulation requires.
- The fluorophore-wavelength color story and the explicit forbidden-palette table (naming Tailwind, Material, and Bootstrap by name) show a level of intentionality most design systems skip entirely.
- The four profile voices, even where the visuals and motion do not yet back them up, are clearly and distinctly articulated; this is a strong foundation to build enforcement onto.
- `templates/deck.html`, `one-pager.html`, `social-cards.html`, and `email-signature.html`, plus `deck-stage.js`, are the most production-ready artifacts in the audit.
- The actual shipped landing page hero already uses the warm paper palette rather than a dark violet gradient, a real, already-realized differentiator that is easy to miss if a reviewer only looks at the profile example artboards instead of the live page.
- `ACCESSIBILITY.md` is unusually honest for a spec document: it self-flags its own pending contrast re-audit and lists its own known gaps (no disability-consultancy review of the Lab profile, no dataviz sonification) rather than presenting itself as finished.

---

## Priority recommendations, top 10, ordered

1. **[Critical]** Build `CrisisBanner` and `ConsentPrompt` components before any further phone or extension work proceeds. This is the single safety-critical gap blocking the platform's highest-stakes surface.
2. **[Critical]** Ratify one body-text-size floor system-wide, resolving the live three-way conflict between `ACCESSIBILITY.md` (14px), `tokens/typography.css` (16px), and the phone template's own requirement (17pt). Recommend 16px, consistent with the org's own prior research recommendation.
3. **[Critical]** Remove or gate the two live motion violations that exist today, not hypothetically: the unconditional scroll-coupled parallax in `landing/animations.js` and the five-plus unbounded looping animations across `profiles/motion.css` and `landing/animations.js`. This is the exact failure mode the org's own prior research names as its single highest-leverage finding.
4. **[Moderate, architectural]** Fold the Lab profile into Research as a density toggle. This directly resolves the extension template's own unresolved "Lab or Research" indecision and reduces the settled lineup to three profiles.
5. **[Moderate]** Re-point Clinical's background tokens to the warm `--cg-lp-*` family instead of the cooler Ghost Day family. This simultaneously closes a checklist gap and strengthens distinctiveness on the single most patient-critical surface.
6. **[Moderate]** Consolidate every duplicate motion-duration and stagger value back onto the canonical `--dur-*` tokens. As shipped, changing "calm mode" system-wide, the entire stated purpose of the token approach, would miss most real surfaces.
7. **[Moderate]** Fix the Clinical profile's internal contradiction (documentation says "magenta never appears," the shipped alert example uses magenta as its accent) and decide, explicitly, which is true.
8. **[Moderate]** Set `data-profile` on both shipped ui_kits and add a skip-to-content link. Right now neither ui_kit activates any profile-scoped accessibility override, including the entire `prefers-contrast: more` layer.
9. **[Minor, already self-identified]** Self-host Lexend and Atkinson Hyperlegible instead of loading them from Google Fonts CDN; the system's own README already admits this gap.
10. **[Minor, distinctiveness]** Surface the fluorophore color story and the logo's ring/orb/node radial geometry on at least one real user-facing surface. Both exist today and are fully real, but neither has left internal documentation.
