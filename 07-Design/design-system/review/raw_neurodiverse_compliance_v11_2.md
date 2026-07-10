# Neurodiverse, Calm, and Therapeutic Design Compliance Audit, v11.2.0 (Revision 3)

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: designers, stakeholders
> **Tags**: `design`, `design-system`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

**Compiled:** 2026-07-10. **Scope:** `design-system-merge-2026-07/01_extracted/v11_new` (v11.2.0), audited fresh against `02_review/raw_neurodiverse_research_inventory.md` Sections 2 to 5. This supersedes `raw_profiles_usecases_critique.md` Section B (21/45, scored against the older v11_1) for all v11.2.0 purposes. No em dashes used per house style.

**Reading time:** about 20 minutes. **If you only read one thing:** v11.2.0 fixed the motion and profile problems the org already knew about (parallax is now opt-in, the Clinical magenta contradiction is gone, `data-profile` and a skip link now exist on both ui_kits) but introduced or left standing a more consequential problem nobody had measured before: the actual color-contrast math on the shipped surfaces. The Clinical profile's own primary explanatory paragraphs (trajectory reasoning, alert detail) run at 15px on a muted token that computes to roughly 4.7:1, not the 7:1 AAA this exact audience is promised in `ACCESSIBILITY.md`'s opening line, and the Research dashboard hardcodes a 14px body floor system-wide. Motion still loops forever, unconditionally, on the shipped marketing hero.

---

## 1. Scoreboard

**23 of 45 PASS clean** (11 PARTIAL, 8 FAIL, 3 ABSENT/untestable). Counting partials as half credit: approximately 29.5/45 (66%).

| Category | Pass | Partial | Fail | Absent | Items | Pass rate |
|---|---:|---:|---:|---:|---:|---:|
| 4.1 Tokens and color | 5 | 2 | 1 | 0 | 8 | 62.5% |
| 4.2 Typography | 6 | 2 | 1 | 0 | 9 | 66.7% |
| 4.3 Motion | 4 | 2 | 2 | 0 | 8 | 50% |
| 4.4 Layout and interaction | 2 | 2 | 3 | 1 | 8 | **25%, worst category** |
| 4.5 Copy and content | 6 | 3 | 1 | 2 | 12 | 50% |
| **Total** | **23** | **11** | **8** | **3** | **45** | **51%** |

**Worst category: 4.4 Layout and interaction** (2/8 clean, 3 outright fails). This is the same category the prior (v11_1) run flagged as worst, and it remains worst by both pass-rate and fail-rate measures. Section padding still has three unreconciled values, dense-content grouping still ships with no show-more anywhere in the system, and the shipped Research dashboard has two concrete, unfixed touch-target gaps (sidebar nav links, the "Export CSV" pseudo-button).

**Genuine, verified fixes since v11_1:** parallax off-by-default and opt-in only; Clinical magenta-in-alert contradiction resolved (now coral); Clinical backgrounds re-pointed to warm paper; both ui_kits now set `data-profile` and ship a skip-to-content link; a global `prefers-contrast: more` layer now exists independent of `data-profile`; Lab folded into Research as a density toggle; `CrisisBanner` and `ConsentPrompt` now exist as real, well-built components; the 16px body-floor conflict between `tokens/typography.css` and `ACCESSIBILITY.md` is resolved (both now say 16px).

**New or newly-quantified problems found in this pass** (the prior audit did not compute contrast math): landing page and Clinical-profile body copy sitting on a "muted" token that computes to 4.37 to 4.69:1 on the actual shipped warm-paper background, below or barely at AA, nowhere near the AAA this exact profile promises; the Research dashboard's hardcoded 14px body font; `landing/animations.js`'s decorative signal-node animations, which loop unconditionally and were not touched by the Revision 3 motion fixes (only parallax was fixed).

---

## 2. Full checklist, 45 items, with evidence

Legend: P = Pass, PT = Partial, F = Fail, A = Absent/untestable.

### 4.1 Tokens and color

| # | Item | Verdict | Evidence |
|---|---|---|---|
| 1 | Extended-reading backgrounds warm/cool low-saturation, never pure white/black | **P** | `tokens/colors.css:157` `--cg-lp-bg: #F4F2EF` (warm) is now the default `--bg-1`; dark theme `--cg-lp-bg: #15131C` (indigo-tinted, not `#000`); pure white (`--cg-lp-surface`) scoped to small cards only. |
| 2 | Dark neutrals carry consistent hue tint, never neutral gray/`#000000` | **P** | `tokens/colors.css:126-133`, `--cg-abyss #0A0A14` through `--cg-neutral-500 #50506E`, all indigo-hued; `tokens/shadows.css:3-4,11-15` shadows also use `rgba(26,26,46,…)`, never `rgba(0,0,0,…)`. |
| 3 | 300-400 pastel set exists and is used on daily-use/8hr/dashboard surfaces, separate from 600-shade | **PT** | Token set exists (`--cg-violet-soft` etc., `tokens/colors.css:106-111`). But `profiles/profiles.css:108` sets the base `[data-profile="research"]` (the profile profiles/README.md itself calls the "8-hour session" surface) `--accent-primary: var(--cg-indigo)`, the full 600-shade; the 300-shade only activates under the separate `[data-profile="research"][data-density="lab"]` combination (`profiles.css:138`). The shipped dashboard (`ui_kits/dashboard/index.html:109`, `data-profile="research" data-density="compact"`, not `"lab"`) mixes 300- and 600-shade hex freely rather than defaulting to the softer set. |
| 4 | Lowest-contrast text token documented non-content-only, never used on content | **F** | Documented correctly in `ACCESSIBILITY.md:55` ("Never place body copy on `--text-muted`"). Violated repeatedly: `landing/styles.css` uses `--muted #6F7178` on `.section-sub` (:102, 18px), `.hero-note` (:176, 16px real sentence), `.sc-body` (:254), `.trip-desc` (:289), `.os-body` (:330), `.p-body` (:341). Computed contrast of `#6F7178` on `#F4F2EF` ≈ **4.37:1**, below AA (4.5:1). `ui_kits/landing/index.html:45` `.hero-note` uses an even fainter `#8A8C94` on the actual hero's key sentence ("We built this because too many people are missed…"), computed ≈ **3.0:1**, a clear AA failure on real, load-bearing copy. All four Clinical example screens (`profiles/clinical-example.jsx:17,59,115,146,152`) set their main explanatory paragraph color to `var(--pf-clinical-text-muted)` (`#6A6A84` on the new warm `#F4F2EF` base), computed ≈ **4.69:1**, barely AA, far short of the 7:1 AAA `ACCESSIBILITY.md`'s own opening line promises for exactly this audience. |
| 5 | Body-text links on light backgrounds clear 5:1, not the decorative accent token | **PT** | `tokens/base.css:61-62` sets the canonical default `a { color: var(--cg-azure-300,#9BC5F7) }` globally; computed against the warm-paper `#F4F2EF` background this is ≈ **1.6:1**, ineffectively invisible. The shipped landing page avoids this only via a local override (`landing/styles.css:63`, `a{color:inherit}`), not by fixing the base token. A new light-surface consumer of `styles.css` who does not replicate that local override would inherit a near-invisible link color. |
| 6 | Danger/error tokens restricted to short phrases/icons/large text, never body copy | **P** | Clinical alert uses coral only for a small dot + short uppercase label (`clinical-example.jsx:139-140`); body paragraphs use the muted token, not the danger token. Research keeps magenta for danger, confined to status-chip labels (`ui_kits/dashboard/index.html:410,415`). |
| 7 | Colorblind-safe pairing table exists; no component distinguishes categories by color alone | **P** | `references/04_color_system.md:127-131`, `references/12_dataviz.md:18-33`; `profiles/dataviz.css:89-98` ships six pattern overlays (dots, lines, grid, crosshatch, waves, chevron), demonstrated paired with color in `guidelines/colors-fluorophore.card.html:33-38`. Dashboard status chips pair color with text labels ("Stable," "Elevated," "Review") plus a dot, not color alone. |
| 8 | System names "calm default" vs. "canonical strong" with a one-line rule | **P** | `ACCESSIBILITY.md §8:167` states the governing principle explicitly; `README.md:111` repeats it with a cross-reference to `ACCESSIBILITY.md §8`. (Enforcement is still by convention, not a linter or build check; see Section 5.) |

### 4.2 Typography

| # | Item | Verdict | Evidence |
|---|---|---|---|
| 1 | Minimum body font size 16px+ (18px long-form) | **F** | `tokens/typography.css:23` and `ACCESSIBILITY.md:89` both now say 16px (the prior 14px conflict is resolved at the token/doc layer). But `ui_kits/dashboard/index.html:12` hardcodes `body{font-size:14px}` and no text anywhere in that file reaches 16px (labels 9.5-13px, table cells 12.5px). `profiles/clinical-example.jsx:59` and `:146` set the main body paragraph in `ClinicalTrajectory` and `ClinicalAlert` to `fontSize:15`, below the floor, in exactly the profile meant to protect a distressed reader. |
| 2 | Measure does not exceed 75ch (target ≈68ch) | **P** | `tokens/typography.css:72` `--measure: 68ch`; `tokens/base.css:45` applies it to `p{max-width}` globally; `CrisisBanner.jsx:51` and `ConsentPrompt.jsx:42` both explicitly use it. `--measure-wide:80ch` exists but no body-copy usage was found. |
| 3 | Line height ≥1.5 for body | **P** | `tokens/typography.css:39` `--lh-body: 1.6`; consistently 1.6-1.7 in Clinical/Foundation examples. |
| 4 | No `text-align: justify` anywhere | **P** | Repo-wide grep, zero matches. |
| 5 | Accessible reading-mode font stack shipped, self-hosted, persists choice | **PT** | Opt-in mechanism and `localStorage` persistence (key `cg-reading-font`) are real and documented (`profiles/a11y.css:14-27`, `ACCESSIBILITY.md:73-85`). Not self-hosted: `tokens/fonts.css:11` still loads via Google Fonts CDN `@import`; `assets/fonts/README.md` explicitly defers self-hosting pending binary upload. |
| 6 | Decorative fonts never appear in body/label/form roles | **P** | Space Grotesk scoped to `--font-heading-alt` (landing headings only); Inter used for body throughout every file read. |
| 7 | Serif scoped to pullquotes of 3 sentences or fewer | **P** | Newsreader/Source Serif Pro confined to `.q`/`.serif` classes, always single-sentence in every example read (`clinical-example.jsx:39`, `foundation-example.jsx:26,80,116`). |
| 8 | No ALL CAPS body/labels; uppercase eyebrows ≥0.08em | **P** | `tokens/typography.css:54-55` `--ls-label:0.08em`, `--ls-caps:0.12em`. All uppercase instances found in both ui_kits are short mono labels/eyebrows at 0.07-0.14em letter-spacing (two selectors, `ui_kits/dashboard/index.html:73,90`, sit at 0.07em, a trivial shortfall below the 0.08em floor). No ALL-CAPS body copy or form labels found anywhere. |
| 9 | Heading steps each ≥20% larger than the level below | **PT** | Holds at desktop width for every adjacent pair (h1/h2 20%, h2/h3 25%, h3/h4 20%, display/h1 33%). But `tokens/typography.css:18-19`: `--text-h4: clamp(1.25rem, 1.75vw, 1.5625rem)` shares the same 1.25rem **minimum** as `--text-h5: 1.25rem` (fixed). At the clamp's narrow-viewport floor (effectively mobile), h4 and h5 render at the identical 20px, a 0% step, exactly where the hierarchy matters most on a phone-first Clinical surface. |

### 4.3 Motion

| # | Item | Verdict | Evidence |
|---|---|---|---|
| 1 | Reduced-motion path replaces spatial transforms with opacity-only, not a sped-up wrapper | **P** | Multiply implemented: `tokens/motion.css:38-45` and `landing/styles.css:390-399` crush duration to ~0.001-0.01ms; `profiles/motion.css:128-136` explicitly nulls `transform` on every named `.anim-*` class; `landing/animations.js:33-37` explicitly sets `.cg-node,.cg-ring,.cg-travel{animation:none!important}` under reduced motion. Functionally equivalent to opacity-only/no-motion, reinforced across four layers. |
| 2 | Scroll-jacking library destroyed, not paused, under reduced motion | **P** | No Lenis/GSAP scroll-jacking library exists. Native `scroll-behavior:smooth` is gated the other way, `tokens/base.css:18-20` only enables it under `prefers-reduced-motion: no-preference`, so it is never active for a reduced-motion user in the first place; a cleaner pattern than "enable then destroy." |
| 3 | No default, unconditional scroll-coupled parallax | **P**, verified fix | `landing/animations.js:9-16,330-347`: `layerParallax()` now gated behind `parallaxEnabled = !reduce && (data-parallax==="on" || localStorage 'cg-parallax'==='on')`. Off by default, opt-in only, blocked under reduced motion. This is the single highest-priority fix from the prior audit and it is genuinely done. |
| 4 | No animation loops indefinitely in the periphery under any setting | **F** | `landing/animations.js:22-37` injects `.cg-node{animation:cgPulse … infinite}`, `.cg-ring{… infinite}`, `.cg-travel{… infinite}`, gated only by `prefers-reduced-motion`, not by any opt-in. Used pervasively: the hero-map halo and 9 scattered signal nodes (`:139-152`), and all three platform-triptych micro-animations (`:280-327`, Cytoverse/Cytoscope/Cytonome). For any visitor without the OS reduced-motion flag set, these loop forever on the flagship marketing hero. Separately, `profiles/motion.css:84-86,95-104`'s `.anim-pulse/.anim-breathe/.anim-spin/.anim-shimmer` utility classes are also unconditionally `infinite`, but a repo-wide check found them applied nowhere in any shipped surface, dormant rather than live. |
| 5 | No autoplay >5s (internal target 3s/250px) without a pause control | **F** | Same root cause as item 4: `cg-node`/`cg-ring`/`cg-travel` cycle every 3.2-6s indefinitely with no pause affordance anywhere in the markup. |
| 6 | No flashing/blinking faster than 3Hz | **P** | Fastest cycle found (`cg-ring`, 3.4s) is far under the 3Hz threshold; no blink/flash pattern found anywhere. |
| 7 | Duration controlled by named tokens, not hardcoded per component | **PT** | Real consolidation: `profiles/motion.css:12-17`'s `--m-xs/sm/md/lg` now derive from canonical `var(--dur-fast/base/slow/slower, …)` with matching fallbacks (fixes the prior "parallel duration scale" finding). Holdouts remain: `--m-xl:800ms` is explicitly hardcoded ("no canonical step," `:16`); `landing/animations.js` still has scattered raw literals (900ms, 1400ms, 2200ms, 2600ms) not routed through any named token. |
| 8 | Stagger/cascade timing capped at ≈45-60ms | **PT** | Default stagger is 60ms increments, in range (`profiles/motion.css:109-118`). A documented "slow" variant at 120ms increments exists (`:120-125`) and exceeds the cap; a repo-wide check found `data-stagger="slow"` applied nowhere in shipped markup, so this is dormant, not live. `landing/animations.js:90` hero axis-fill bars stagger at 160ms/step (small, 2-3 item sequence, not a large cascade, but still outside the documented cap). |

### 4.4 Layout and interaction

| # | Item | Verdict | Evidence |
|---|---|---|---|
| 1 | Section padding/whitespace generous and consistent, not ad hoc | **F** | Three unreconciled values persist: `references/09_layout.md:27` documents 80px desktop; `landing/styles.css:92` ships 124px; `ui_kits/landing/index.html:72` ships 96px. Unchanged from the prior audit. |
| 2 | No section ships 2+ competing primary CTAs in one zone | **P** | Landing hero and closing both pair one filled primary with one lower-weight secondary; `ClinicalAlert` pairs "Message Dr. Okafor" (primary) with "See the data" (secondary reference action). Consistent throughout every screen read. |
| 3 | Consistent structural section pattern; constant nav location | **P**, scope-limited | Confirmed within the single landing page and single dashboard that exist (eyebrow/headline/subhead/body repeated across every landing section; sticky nav; fixed sidebar). Cross-page consistency is not verifiable since only one page per kit exists. |
| 4 | Dense groupings capped (~4 items) with an explicit "show more" | **F** | `ui_kits/landing/index.html:396-427` ships 6 capability cells at once, no disclosure control. `ui_kits/dashboard/index.html:356-440` shows "6 of 1,847" as a text caption only (`:360`), no pagination control rendered. A repo-wide search for "show more"/"pagination" found zero matches anywhere in the system; no such component or pattern exists at all. Unchanged from the prior audit. |
| 5 | 44×44 (40×40 icon-only) touch targets enforced | **F** | The mechanism is genuinely solid at the component layer (`tokens/base.css:139-142` global rule; `Button.jsx`, `Input.jsx`, `CrisisBanner.jsx`, `ConsentPrompt.jsx` all explicit 44px). But the shipped Research dashboard bypasses the design-system components with raw HTML: `.nav-item a` (12 sidebar links, `ui_kits/dashboard/index.html:25`) computes to roughly 29px tall with no min-height, and anchors are not covered by the global button rule. The "Export CSV" control (`:362`) is a bare `<div style="cursor:pointer">`, not a button/role="button"/anchor, so it gets no size enforcement and is not keyboard reachable. Both are unchanged from the prior audit. |
| 6 | Visible focus indicator ≥3:1, no bare `outline: none` | **PT** | Real, verified consolidation: `tokens/base.css:72-76` and `profiles/states.css:36-39` now converge on one ring (3px, azure-300, ~0.85 alpha). But `components/core/Input.jsx:68` still sets `outline:'none'` and replaces it with a custom `boxShadow` at only 2px width, 0.15 alpha (`:30-34`), a much fainter, non-conforming ring, unchanged from the prior audit. |
| 7 | Holds at 200% zoom, no truncation/forced horizontal scroll | **A** | Not testable from static file review; no rendering pass performed. `clamp()`/`ch`/fluid-grid usage is zoom-friendly in principle, not verified in practice. |
| 8 | `prefers-contrast: more` override exists and has been tested | **PT** | Now exists at two levels and is correctly wired: `tokens/base.css:82-91` (global, activates on any `styles.css` consumer) and `profiles/a11y.css:5-12` (profile-scoped); both ui_kits now set `data-profile` (`ui_kits/landing/index.html:179`, `ui_kits/dashboard/index.html:109`), so the profile-scoped layer now actually activates, fixing the prior audit's core finding. No evidence found that it has actually been tested; `ACCESSIBILITY.md §6:147-152` lists it as a pending pre-ship checklist item, not a confirmed pass. |

### 4.5 Copy and content

| # | Item | Verdict | Evidence |
|---|---|---|---|
| 1 | No banned word appears in shipped copy | **P** | Repo-wide, case-insensitive grep for the full banned list found zero live hits outside the banned-word lists themselves (`WRITING.md`, `README.md`, `SKILL.md`, `guidelines/brand-voice.card.html`) and the untouched `uploads/` folder. "Transforming" (`foundation-example.jsx:22`) remains adjacent-in-spirit but not literally banned, same soft note as the prior audit. |
| 2 | Health-outcome claims retain uncertainty, no diagnosis/treatment/clinician-replacement implication | **P** | Clinical copy consistently hedges ("still well within your range," "no action recommended," "Not an emergency, but…"); landing page has an explicit "Non-diagnostic, by design" section. Minor soft spot: `foundation-example.jsx:112-114`'s social-card headline ("Mapping the cellular signature of Alzheimer's, 11 years early") carries no in-card hedge, though it reads as a research-brief teaser, not a per-patient claim. |
| 3 | Person-first phrasing for medical/disability references | **A** | Confirmed via grep: zero instances of "person-first" phrasing or guidance anywhere in `v11_new` (outside the research corpus, which lives elsewhere). No disability-reference copy exists in sampled content to check either way. |
| 4 | General/landing copy scores Flesch-Kincaid grade 7-9 | **A** | No FK scoring tool was run; confirmed via grep that no reading-level target (Flesch-Kincaid, "grade 7," "reading level") is stated anywhere inside `v11_new` itself. Sampled sentences read impressionistically plain, but this is not measured. |
| 5 | No sentence exceeds ~25 words as routine | **PT** | Mostly short throughout. One concrete violation in the single most-read sentence on the site: `ui_kits/landing/index.html:211` hero-sub, approximately 38 words ("Cytognosis turns biological, behavioral, and clinical research signals into an interpretable map of a person's health, so the quiet shifts that precede illness can be seen, studied, and understood years earlier"). |
| 6 | No em dashes; Oxford comma; active voice | **P** | Repo-wide grep found em dashes only inside `uploads/` (explicitly untouched per the hard rule) and one compiler-generated config file; zero in authored content. Oxford comma applied consistently; voice predominantly active throughout. |
| 7 | Every major section closes with a plain-language summary before its CTA | **PT** | Present at the page-closing level (landing's final CTA subhead functions as a summary). Not consistently present section-by-section; "Problem" and "Capabilities" sections end directly on the last card with no closing "so what" sentence. |
| 8 | No page uses more than 2 distinct metaphors | **P** | Map/Sensor/Navigator (Cytoverse/Cytoscope/Cytonome) plus "trajectory"/"coordinates"/"baseline" all belong to one coherent cartography metaphor family, not stacked, unrelated metaphors. |
| 9 | Every acronym/technical term defined on first use per page | **PT** | Research-context density (PHQ-9, GAD-7, PSS in the Foundation capabilities section) is appropriate for that audience. But `clinical-example.jsx:153-155`'s `ClinicalAlert` shows a patient reader "IL-6 above your baseline" and "TNF-α rising" with no lay gloss, in the one profile whose own framing (`profiles/README.md:32`) is "someone who just learned something worrying about their body." |
| 10 | Copy register matches its surface (voice dials), not one uniform tone | **P** | `WRITING.md`'s dial table is clear; sampled Foundation, Clinical, and Research copy read in genuinely distinct, correct registers. |
| 11 | Clinical error/empty-state/alert copy names a concrete next step and human fallback | **P** | `WRITING.md`'s worked examples are strong and consistent; the shipped `ClinicalAlert` example matches exactly ("Message Dr. Okafor," "your care team should see this"). |
| 12 | Long-form pages/documents open with a BLUF-style anchor line | **F** | None of `README.md`, `ACCESSIBILITY.md`, `WRITING.md`, `profiles/README.md`, or `CHANGELOG.md` opens with a reading-time or "if you only read one thing" line, unlike the org's own research documents. Unchanged from the prior audit. |

---

## 3. Grouped exact-fix list (paste-ready for a revision prompt)

### Group A: Color and contrast (highest priority, affects the most patient-facing surfaces)

1. **`profiles/clinical-example.jsx`, lines 17, 59, 115, 146, 152.** Change `color:"var(--pf-clinical-text-muted)"` to `color:"var(--cg-neutral-900)"` (or a new `--pf-clinical-text-secondary`-class token computing to ≥7:1) for every primary explanatory paragraph in `ClinicalHome`, `ClinicalTrajectory`, `ClinicalOnboarding`, and `ClinicalAlert`. Reserve `--pf-clinical-text-muted` for captions/labels only (dates, tiny metadata), never for the sentence a patient is meant to read and act on.
2. **`landing/styles.css`, lines 102, 176, 254, 289, 330, 341.** Replace `color: var(--muted)` with a new local alias resolving to at least 7:1 on `#F4F2EF` (target hex ≈`#3E3F46`/`--fg-2`, which computes to 9.36:1) for `.section-sub`, `.hero-note`, `.sc-body`, `.trip-desc`, `.os-body`, `.p-body`. Reserve `--muted`/`--faint` strictly for the short uppercase labels/tags they are already correctly used for elsewhere in the same file (`.cmp-tag`, `.trip-role`, `.layer-txt .lt-meta`).
3. **`ui_kits/landing/index.html`, line 45.** `.hero-note` currently sets `color: #8A8C94` (≈3.0:1 on `#F4F2EF`). Change to `#3E3F46` or darker (target ≥7:1).
4. **`ui_kits/landing/index.html`, lines 44, 76, 88, 97, 123, 132, 142.** Consolidate the four different hardcoded "muted" hex values in this one file (`#5C5E66`, `#6F7178`, `#545560`, plus the lighter meta tones) onto a single token reference instead of four independent hardcoded hex strings, so a future contrast fix only has to change one place.
5. **`tokens/base.css`, lines 61-62.** Default link color `var(--cg-azure-300,#9BC5F7)` computes to ≈1.6:1 on the warm-paper default background. Add a light-surface override (e.g., inside the existing `[data-theme="light"]`/default block in `tokens/colors.css`) so links resolve to `--cg-violet-700` or darker on any light surface that does not locally override link color the way `landing/styles.css:63` does.

### Group B: Motion (the org's own research names this the single highest-leverage risk category)

6. **`landing/animations.js`, lines 22-37, and every call site at 139-152, 282-289, 296-302, 320-326.** The injected `.cg-node`, `.cg-ring`, `.cg-travel` keyframes run `infinite` unconditionally except under `prefers-reduced-motion`. Either (a) cap each to a finite iteration count (e.g., `animation-iteration-count: 6` for `cg-node`, then hold the final frame), or (b) gate them behind the same `parallaxEnabled`-style opt-in already used for `layerParallax()`, so peripheral decorative motion is opt-in by default, not opt-out. Do not rely on `prefers-reduced-motion` alone to catch this, per the org's own research (#25).
7. **`profiles/motion.css`, line 16.** `--m-xl: 800ms` is explicitly hardcoded with "no canonical step." Add `--dur-xl: 800ms` to `tokens/motion.css` and re-point `--m-xl` to reference it, so all durations trace to one file.
8. **`profiles/motion.css`, lines 120-125.** The `[data-stagger="slow"]` 120ms-per-step variant exceeds the 45-60ms cap. Either delete it (it is not used anywhere in shipped markup today) or re-label it clearly as an explicit, rare exception with a stated maximum group size, so it cannot silently become the default for a future cascade.

### Group C: Layout and touch targets

9. **Section padding, three files.** Pick one desktop value and one mobile value and apply everywhere: `references/09_layout.md:27` (80px documented), `landing/styles.css:92` (124px shipped), `ui_kits/landing/index.html:72` (96px shipped) currently disagree. Recommend ratifying 96px desktop / 48px mobile (a middle value already shipping somewhere) and updating all three to match.
10. **`ui_kits/landing/index.html`, lines 396-427 (capability grid) and `ui_kits/dashboard/index.html`, lines 356-440 (subject table).** Add a real "show more"/pagination control. Build one shared `ShowMore`/`Pagination` pattern in `components/` since none currently exists anywhere in the system.
11. **`ui_kits/dashboard/index.html`, line 25 (`.nav-item a`).** Add `min-height: 44px; display:flex; align-items:center` (or apply `role="button"` styling) so sidebar nav links meet the touch-target floor; anchors are not covered by the global `button:not(.btn-icon)` rule in `tokens/base.css:139-142`.
12. **`ui_kits/dashboard/index.html`, line 362 ("Export CSV").** Replace the bare `<div style="cursor:pointer">` with a real `<button>` (or `role="button" tabindex="0"` plus a keydown handler), and ensure it inherits the 44px floor.
13. **`components/core/Input.jsx`, lines 30-34, 68.** Replace the custom `boxShadow` focus treatment (2px, 0.15 alpha) with the canonical `--focus-ring` token (3px, 0.85 alpha) already used in `profiles/states.css:37-39`, so there is exactly one focus-ring implementation system-wide.

### Group D: Typography

14. **`ui_kits/dashboard/index.html`, line 12.** Remove the hardcoded `font-size: 14px` on `body`; set it to `var(--text-body, 1rem)` (16px) and re-check every class in the file that currently relies on the 14px cascade default, promoting any actual prose/description text (e.g., `.arc-desc`, `.topbar-path`) to 16px while dense tabular/metadata cells may stay smaller by explicit, documented exception.
15. **`profiles/clinical-example.jsx`, lines 59, 146.** Raise `fontSize:15` to `fontSize:16` in `ClinicalTrajectory` and `ClinicalAlert`'s main body paragraphs.
16. **`tokens/typography.css`, line 18.** `--text-h4`'s clamp minimum (1.25rem) collides with `--text-h5`'s fixed 1.25rem. Lower the h4 clamp minimum to about 1.0625rem (17px) or raise h5 to a clamp, so the 20%+ step holds at every viewport width, not only above the clamp's midpoint.

### Group E: Copy

17. **`ui_kits/landing/index.html`, line 211 (hero-sub).** Split the ~38-word sentence into two sentences at the natural clause break ("...map of a person's health. That means the quiet shifts that precede illness can be seen, studied, and understood years earlier.").
18. **`profiles/clinical-example.jsx`, lines 153-155.** Gloss "IL-6" and "TNF-α" in plain language on first use for the patient reader (e.g., "IL-6, a marker of inflammation, above your baseline since April 11"), consistent with Clinical's own "highest warmth" voice dial.
19. **`WRITING.md`.** Add an explicit person-first-language line and an explicit Flesch-Kincaid grade 7-9 target for Foundation/Clinical copy; neither currently appears anywhere inside the design system's own documentation (confirmed by grep), only in the separate research corpus.
20. **`README.md`, `ACCESSIBILITY.md`, `WRITING.md`, `profiles/README.md`.** Add a two-to-three-line BLUF/reading-time opener to each, matching the convention the org's own research documents already use consistently.

### Group F: Documentation and architecture debt (lower urgency, but actively misleading if left)

21. **`references/04_color_system.md` and `references/11_accessibility.md`.** Both still describe the old cool "Ghost Day"/"Pale Day" light-theme family exclusively and never mention the warm `--cg-lp-*` paper family that is now the actual documented default (`README.md`, `ACCESSIBILITY.md §8`). Update both reference docs to describe the warm-paper default, or add a prominent pointer to `ACCESSIBILITY.md §8` at the top of each.
22. **`references/12_dataviz.md`.** The file's own "Multi-series sequence" list (line 7, violet/azure/magenta/indigo/teal/coral) and its "Fluorophore channels" table (line 22, dapi-violet/alexa-azure/gfp-teal/mito-coral/rhodamine-magenta/uv-indigo) use two different orderings for the same six colors, and `profiles/dataviz.css`'s `--q-1..8` (line 59) uses a third. Pick one canonical order and reference it from the other two locations instead of restating it.
23. **`README.md`, "Iconography" section (lines 201-219).** States "Actual SVG icon sets are not bundled in this design system, use Phosphor Icons CDN," but `assets/icons/line/` and `assets/icons/solid/` actually contain roughly 100 real, bundled, brand-specific SVGs (`cell.svg`, `dna.svg`, `heart-pulse.svg`, `shield.svg`, and the rest). Update this section to describe the bundled set as primary; this is actively misleading to an implementer deciding which icons to use.
24. **`components/core/CrisisBanner.jsx` and `ConsentPrompt.jsx`.** Both are well-built and well-documented but are not invoked anywhere in `profiles/clinical-example.jsx` or any ui_kit. Add `<ConsentPrompt>` to `ClinicalOnboarding` (which currently describes starting data collection with no consent gate shown) and add `<CrisisBanner>` to at least one Clinical screen so the pairing between component and use case is demonstrated, not just documented in the `.prompt.md` file.
25. **`profiles/profiles.css`, lines 106-133.** Re-point the base `[data-profile="research"]` (non-lab) `--accent-primary` from `var(--cg-indigo)` (600-shade) to a 300-shade token, reserving 600 for short-duration/marketing contexts, consistent with the system's own "8-hour session" framing of the Research profile.
26. **`assets/fonts/README.md` / `tokens/fonts.css`.** Self-hosting is well-specified but not done. Upload the listed `.woff2` binaries and replace the CDN `@import` with `@font-face` rules; this has been an open item across two revisions now.

---

## 4. 56-principle coverage matrix

Legend: **Tok** = anchored in tokens, **Comp** = anchored in a component, **Doc** = anchored in a documented rule (`ACCESSIBILITY.md`/`WRITING.md`/`references/`), **Viol** = anchored in doc/token but contradicted by shipped usage, **NONE** = not represented anywhere in `v11_new` (present only in the external research corpus).

### Section 2.1, Color and palette (1-9)

| # | Principle | Anchored where | Note |
|---|---|---|---|
| 1 | Cool hue family is therapeutic | Tok, Doc | `ACCESSIBILITY.md §8`, `references/04_color_system.md` |
| 2 | ~20pp desaturated calm vs. canonical strong | Tok, Doc | `--cg-lp-violet` vs. `--cg-violet` |
| 3 | 300-400 shade for 8hr/daily-use surfaces | Tok only, weak Comp | Token exists; Research profile default does not use it (see 4.1.3 above) |
| 4 | Warm neutral bg, never pure white for large surfaces | Tok, Comp, Doc | Fully anchored |
| 5 | Dark surfaces never pure black, indigo undertone | Tok (colors + shadows) | Fully anchored, thorough |
| 6 | Faint token restricted to decorative use | Doc, but **Viol** | Documented correctly, violated on real body copy in three surfaces |
| 7 | Warm accent doses in cool palette | Tok, Comp | Coral/yellow used sparingly as documented |
| 8 | Saturated danger tokens restricted to short/large text | Tok, Doc, Comp | Fully anchored |
| 9 | Never color alone; colorblind-safe pairs | Tok, Comp, Doc | Fully anchored, strong (fluorophore ramp, pattern overlays) |

### Section 2.2, Typography (10-19)

| # | Principle | Anchored where | Note |
|---|---|---|---|
| 10 | 16/18px body floor | Tok, Doc, but **Viol** | Dashboard and half of Clinical examples ship below it |
| 11 | 68ch measure cap | Tok, Comp | Fully anchored |
| 12 | Line height 1.5-1.7 | Tok | Fully anchored |
| 13 | Left-align, never justify | Comp | Fully anchored |
| 14 | Lexend/Atkinson opt-in, self-hosted, persisted | Tok, Comp, Doc (persistence); NOT self-hosted | Partial |
| 15 | Display fonts scoped to headings only | Tok | Fully anchored |
| 16 | Serif scoped to short pullquotes | Comp | Fully anchored |
| 17 | No ALL CAPS body; uppercase ≥0.08em | Tok | Anchored, two trivial 0.07em shortfalls |
| 18 | Paragraph limit 3-4 sentences | Doc | `WRITING.md` "Cognitive load" section |
| 19 | Heading steps ≥20% | Tok, but **Viol** at clamp floor | h4/h5 collapse to 0% step at narrow viewport |

### Section 2.3, Motion (20-27)

| # | Principle | Anchored where | Note |
|---|---|---|---|
| 20 | Reduced motion = opacity-only, not sped-up wrapper | Tok, Comp | Fully anchored, four redundant layers |
| 21 | Autoplay >5s pausable / 3s-250px internal cap | Doc, but **Viol** | `ACCESSIBILITY.md §4`; violated by cg-node/ring/travel |
| 22 | No blink/flash >3Hz | (no violation found) | Nothing to anchor against; clean |
| 23 | Scroll-jacking destroyed under reduced motion | Comp (via a cleaner gate) | N/A, no library; smooth-scroll gated behind no-preference instead |
| 24 | Parallax/scrub is highest risk, replace with calm entrance | Comp | **Fixed and verified this revision** |
| 25 | No looping/peripheral motion ever, unconditional pause | Doc, but **directly Viol** | The single most important unresolved gap in this audit |
| 26 | Stagger encouraged, cap ~45-60ms | Tok | Default anchored; "slow" variant is a dormant exception |
| 27 | Three named duration tokens as single override point | Tok | Anchored, with scattered raw-ms holdouts in `landing/animations.js` |

### Section 2.4, Layout, spacing, interaction (28-35)

| # | Principle | Anchored where | Note |
|---|---|---|---|
| 28 | Generous, consistent section padding | Doc, but **Viol** | Three-way mismatch, unresolved |
| 29 | One CTA per zone | Doc, Comp | Fully anchored |
| 30 | Consistent structural pattern, constant nav | Comp | Anchored within existing single-page kits |
| 31 | Progressive disclosure, cap ~4 items, "show more" | **NONE** | Confirmed via grep, zero "show more"/pagination pattern anywhere in the system |
| 32 | Touch targets 44/40px | Tok, Comp, but leaky at the edges | Solid in design-system components; bypassed by raw HTML in both ui_kits |
| 33 | Visible focus ring | Tok, Comp | Anchored system-wide, except `Input.jsx`'s own override |
| 34 | 200% zoom support | Doc (as a testing gate) | Not verified executed |
| 35 | `prefers-contrast: more` override | Tok, Comp | **Fixed and verified this revision** (global layer + `data-profile` wiring) |

### Section 2.5, Cognitive load and content structure (36-41)

| # | Principle | Anchored where | Note |
|---|---|---|---|
| 36 | Reduce cognitive load, limit choices | Doc, but **Viol** in places | Density violations remain (6-cell grid) |
| 37 | Close sections with "so what" | Doc, incomplete Comp | Rule stated; only executed at page-closing level |
| 38 | Cap 2 metaphors | Comp | Fully anchored |
| 39 | Define acronyms/jargon on first use | Doc, but **Viol** in Clinical | IL-6/TNF-α undefined for the patient reader |
| 40 | Bullet lists over dense prose | Comp | Fully anchored |
| 41 | BLUF/reading-time opener convention | **NONE** | Confirmed via read of all top-level docs; never applied to the design system's own documentation |

### Section 2.6, Condition-specific bundles (42-45)

| # | Principle | Anchored where | Note |
|---|---|---|---|
| 42 | ADHD pattern bundle | Doc | `ACCESSIBILITY.md` "Neurodiversity support," verbatim-close to research |
| 43 | Dyslexia pattern bundle | Doc, Tok (fonts) | Anchored |
| 44 | Autism pattern bundle | Doc | Anchored; undercut in practice by the live motion loops (item 25) |
| 45 | Anxiety/depression pattern bundle | Doc, Comp (Clinical copy) | Anchored, genuinely well executed in `WRITING.md`'s Clinical section |

### Section 3, Tone and content (46-56)

| # | Principle | Anchored where | Note |
|---|---|---|---|
| 46 | Authoritative/compassionate/optimistic, never fear-based | Doc | Fully anchored |
| 47 | Banned words union list | Doc | Fully anchored, redundantly documented, zero live violations |
| 48 | Non-diagnostic safety rules always | Doc | Fully anchored, multiply redundant |
| 49 | Person-first language | **NONE** | Confirmed via grep, zero mentions inside `v11_new` |
| 50 | Reading-level grade 7-9 target | **NONE** | Confirmed via grep, zero mentions inside `v11_new`; lives only in the external research corpus |
| 51 | One idea/sentence, <25 words | Doc (general ethos only) | No explicit word-count rule stated; violated once in the hero |
| 52 | Active voice, Oxford comma, no em dash | Doc | Fully anchored, confirmed compliant |
| 53 | Benefits over features framing | Doc | Fully anchored |
| 54 | Three-dial voice tuning per surface | Doc | Fully anchored, thoroughly demonstrated |
| 55 | Clinical calm/non-alarming construction rules | Doc, Comp | Fully anchored and demonstrated |
| 56 | No filler phrases, no performed emotion | Doc | Fully anchored |

**Principles not anchored anywhere in the system (pure "research notes only"): 3 of 56** (#31 progressive disclosure/show-more, #41 BLUF/reading-time convention, #49/#50 grouped as a pair but counted individually below).

Correction for precision: the three unanchored principles are **#31, #41, and #50**. #49 (person-first language) is also confirmed absent from `v11_new`'s own text, so the honest count of principles with zero anchoring anywhere in the shipped system is **4 of 56** (#31, #41, #49, #50). All four were independently confirmed via grep returning zero matches, not inferred.

---

## 5. Section 5 conflicts, resolution status

| Tension | Status in v11.2.0 |
|---|---|
| Canonical vibrancy vs. calm-by-default | **Resolved as a stated rule**, now with an explicit cross-reference (`README.md` to `ACCESSIBILITY.md §8`). Still enforced by convention only, no linter/build check exists. |
| Warm beige vs. cool indigo-tinted light background | **Resolved at the token layer, not at the documentation layer.** `tokens/colors.css` and `ACCESSIBILITY.md §8` now clearly make warm paper the default. But `references/04_color_system.md` and `references/11_accessibility.md` were never updated and still describe only the old cool "Ghost Day"/"Pale Day" family with no mention of `--cg-lp-*`. A reader of either reference doc alone would still not know the warm family exists or is now the default. **Partially resolved.** |
| Minimum body font size (16px vs. 14px) | **Resolved.** `tokens/typography.css` and `ACCESSIBILITY.md` both now state 16px. (A new, different violation was found this pass: the 16px rule is stated correctly but not enforced in the dashboard and half of the Clinical examples, see 4.2.1. That is an enforcement gap, not a restatement of the old numeric conflict.) |
| Autoplay/motion duration ceiling (5s WCAG vs. 3s/250px internal) | **Unchanged, still undocumented as an intentional tightening**, though now moot in practice since the actual live violation (unconditional infinite loops) is a more basic problem than the exact ceiling number. |
| Two accessibility documents, two rigor profiles, unreconciled | **Improved but still not merged.** `ACCESSIBILITY.md §8` now has its own therapeutic-design evidence section (a genuine, verified addition this revision). But `references/11_accessibility.md` still exists as a separate, older, un-merged file with its own "Therapeutic color theory" table naming different specific sources (Squirrelsong, Coding Horror) than `ACCESSIBILITY.md §8`'s more generic prose. Two overlapping, non-identical evidence sections now exist instead of one. The citation appendix in `ACCESSIBILITY.md §8` is explicitly **deferred, not real named-study citations**: its final line states "Sources are summarized rather than quoted; maintainers should attach the specific citations… when this appendix is formally published." |
| Serif choice for calm/reassuring contexts (Newsreader vs. Source Serif Pro) | **Unresolved, unchanged.** `profiles/README.md` still specifies Source Serif Pro for Clinical while the landing page uses Newsreader; no single decision recorded. |
| Accessibility font stack order (Lexend-first vs. Atkinson-first) | **Resolved in the shipped code** (`profiles/a11y.css` and `ACCESSIBILITY.md` both list Atkinson Hyperlegible before Lexend in prose, though the `--font-a11y-*` custom property declarations in `profiles/a11y.css:17-18` list Hyperlegible first, Lexend second, consistent internally at least). Not a live conflict any longer within `v11_new`, though it still does not match the research inventory's own recommended order (Lexend first); low severity. |
| Where "calm" comes from conceptually (hue family alone vs. actively dialed down) | **Implicitly resolved in favor of the stricter view**, matching the research's own recommendation: `ACCESSIBILITY.md §8`'s governing principle explicitly requires both a cool/muted default AND active motion restraint, not hue family alone. Undercut in practice by the still-live motion loops (item 25), which shows the "actively dialed down" standard is stated but not fully executed. |
| Considered and declined (further beige softening, 140px padding) | Still correctly not reflected anywhere; no regression found. |

**Net: 2 of 9 named tensions fully resolved with no residue** (canonical-vibrancy-vs-calm at the rule level, minimum-body-font-size at the token/doc level), **5 partially resolved** (warm-vs-cool docs, two-accessibility-docs, font-stack-order, calm-conceptual-framing, autoplay-ceiling-undocumented), **1 unresolved** (serif choice), **1 not applicable to re-check** (considered-and-declined, still holding).

---

## 6. Verdict

v11.2.0 is meaningfully calmer and more neurodiverse-aware than v11_1 in the places its own revision process targeted directly, parallax is genuinely opt-in now, the Clinical profile's magenta contradiction is gone, the profile system is consolidated to three surfaces with a working `prefers-contrast` layer, and two real safety components exist where none did before. But "calm by design" is not yet true end to end: this audit computed actual contrast ratios for the first time and found that the Clinical profile, the single surface built to serve a distressed reader, ships its own primary explanatory copy at roughly 4.7:1 contrast and 15px type, both below what the system's own accessibility document promises for exactly that audience, and the flagship marketing hero still runs unconditional, infinite decorative animation loops that the org's own research names as the single highest-leverage risk in the entire corpus. The system is better than before and still not yet what it claims to be; the gap has moved from "known and named" (motion, profiles) to "real but previously unmeasured" (contrast math, dashboard type size), which is progress in one direction and a new discovery in another.

---

*End of audit. 45-item checklist re-run fresh against v11.2.0; scores here are not comparable arithmetic to the 21/45 prior run, which audited a different, older export (v11_1) per the task's own instruction not to trust that run for v11.2.0.*
