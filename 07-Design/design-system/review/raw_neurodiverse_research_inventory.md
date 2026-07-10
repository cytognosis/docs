# Raw Neurodiverse, Calm, and Therapeutic Design Research Inventory

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: designers, stakeholders
> **Tags**: `design`, `design-system`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

**Compiled:** 2026-07-09. **Purpose:** consolidate all prior Cytognosis research on neurodiverse-friendly, calm, and therapeutic design into one actionable, deduplicated inventory to drive the current design-system revision. No em dashes used per house style.

**Reading time:** about 18 minutes. **If you only read one thing:** the single highest-leverage, most evidence-dense finding across every source is that heavy scroll-coupled motion (parallax, smooth-scroll, scrub animation) is a bigger risk to neurodivergent and vestibular-sensitive users than any color choice, and the governing resolution for every color tension is "calm/muted by default, full-saturation canonical brand color only at the few high-emphasis recognition moments." Section 5 flags where sources still disagree.

---

## 1. Source inventory

| Code | Document | Date | What it established |
|---|---|---|---|
| **NDR** | `Website/_drive/research-neurodiverse-design.md` | 2026-06-09 | Primary external-evidence research doc. Maps W3C COGA/WCAG 2.2, Calm Tech Institute, ADHD UX literature, color psychology, typography, and motion research onto the Cytognosis site stack. Ends with a prioritized recommendation table and a top-5 leverage list. |
| **RDC** | `Website/_drive/research-design-consolidation.md` | 2026-06-09 | Compares the old dark-only site against Ali's new light-theme design token by token, evaluates brand v2's gaps (missing semantic colors, no focus spec, no a11y font slot), and proposes a "v3" token set with named neurodiverse-calm revision hooks. |
| **DSD1** | `Website/_drive/design-system-decision.md` | 2026-06-09 | "Brand v2" reconciliation. States the governing principle "calm by default, canonical-strong where contrast or brand recognition demands it," resolves each Ali-vs-canonical color drift, and ships the first paste-ready `:root` block. |
| **DSD2** | `Website/_drive/design-system-decision-v2.md` | 2026-06-09 | Supersedes DSD1's token and motion sections. The authoritative "calm by default" decision: replaces hero parallax, fixes reading-load issues, adds Reading-mode and Reduce-motion controls, and fills every missing token slot. |
| **WDH** | `Website/WEBSITE_DESIGN_HANDBOOK.md` | 2026-06-09 | Onboarding handbook; Section 4 ("Calm and neurodiverse design") documents what actually shipped on branch `feat/vite-frontend-serving` in Phase 7a, plus the one-paragraph research rationale. |
| **HSD** | `Website/_drive/handbook-src-design.md` | 2026-06-09 | Dense digest merging NDR, RDC, DSD1, DSD2, and content-strategy.md with exact per-value citations. The most complete single cross-reference of "what changed and why," including a sourced findings table. |
| **BRG@9559138** | branding repo git history, commit `9559138` ("finalize therapeutic design guidelines and VSCode theme integration"), files `guidelines/02_color_system.md`, `guidelines/07_accessibility.md`, `guidelines/05_design_motifs.md`, `README.md` (v10.1.0), `guidelines/agent-prompts/AGENT_PROMPT*.md` | 2026-03-13 | The only corpus location that names "therapeutic design" as an explicit, evidence-cited design category (NIH/iMotions, Squirrelsong, Coding Horror/Stack Exchange, chromotherapy research) with its own 600-vs-300-shade token system. Overwritten in the working tree by commit `130dee7` (CytoStyle replacement); recovered read-only from git history for this inventory. |
| **V11-ACC** | `design-system-merge-2026-07/01_extracted/v11_1/ACCESSIBILITY.md` | current (v11_1 baseline) | Newest, WCAG-2.2-native accessibility spec. Per-profile contrast audit (Foundation/Clinical/Research/Lab), hit targets, focus, non-color signal, motion, high-contrast override, and a testing checklist. Flags its own contrast tables as pending re-audit against the v11 token ramp. |
| **V11-REF11** | `.../v11_1/references/11_accessibility.md` (byte-identical in `v11`, `v11_1`, `v11_1_1`) | superseded, carried forward unchanged | The old v9/v10-era accessibility doc, stale copy of the same lineage as BRG@9559138's `07_accessibility.md`. Still contains the explicit "Mental Health & Therapeutic Design" section and its citations; not reconciled with V11-ACC. |
| **V11-PROF** | `.../v11_1/profiles/README.md` | current | Defines the four-surface profile system (Foundation, Clinical, Research, Lab), each with its own type stack, palette emphasis, and voice register. Clinical is the calm/reassuring profile. |
| **V11-WRITE** | `.../v11_1/WRITING.md` | current | Voice dials (warmth, precision, length) per profile; concrete before/after copy examples for errors, empty states, alerts, onboarding; banned-words list; non-diagnostic safety rules. |
| **V11-README** | `.../v11_1/README.md` | v10.1.0 lineage | Top-level design-system doc. Names "therapeutic design" as one of three mission-critical visual-philosophy pillars (with scientific grounding and accessibility-first). Same lineage as BRG@9559138. |
| **RCI** | `design-system-merge-2026-07/02_review/raw_context_inventory.md` | 2026-07-08 | Not itself a principle source; sibling inventory documenting that three non-converged design systems exist and that the branding repo's therapeutic-guidelines content is recoverable only via git history. Used here for cross-checking, not cited as design evidence. |

Grep sweep of `~/Claude/Projects` for `neurodiv|therapeutic|sensory|overstimul|autism|ADHD-friendly` returned mostly Grants/Yar clinical-research documents (ADHD, autism, and anxiety as disease biotypes for the Yar product's science, not design guidance); these are out of scope for a design inventory and were excluded. The design-relevant hits all fall under the paths already listed above.

`cytomem_recall` (semantic) surfaced two documents this session cannot reach: `docs` repo path `07-Design/adhd-neurodiversity-design-research.md`, and `website` repo (the actual git repo at `~/repos/cytognosis/website`, not the Claude Projects folder) paths `.agents/skills/brand/references/design-system.md` and `docs/design_requirements.md`. None of these live under a folder attached to this session. Flagged in Section 6 as follow-up, not incorporated below.

---

## 2. THE PRINCIPLES: visual and interaction design

Each entry: operational rule, then evidence/citation, then source code (see Section 1 for full paths).

### 2.1 Color and palette

| # | Rule (operational) | Evidence / citation | Source |
|---|---|---|---|
| 1 | The entire primary palette lives in the cool hue family (violet, azure, indigo, teal); this family is treated as "therapeutic" in itself. | Cool blue/green/purple environments lower heart rate and cortisol (cited to NIH, iMotions). Violet specifically tied to calm introspection (chromotherapy research). | BRG@9559138 (`02_color_system.md`, `07_accessibility.md`), V11-README |
| 2 | Reduce the primary accent's saturation by roughly 20 percentage points versus the canonical brand shade for calm-audience contexts; keep a "strong" full-saturation variant for high-emphasis use only. Concretely: `--violet #6E5BD1` (calm default, HSL ≈ 248°,56%,58%) vs. `--violet-strong #8B3FC7` (canonical, HSL ≈ 276°,55%,50%). | Muted accents read as psychologically calmer for anxiety/ADHD audiences; both pass WCAG AA (button fill 5.14:1 / 5.78:1; text link on beige 4.65:1 tight / 5.23:1 comfortable). | NDR §4, DSD1, DSD2 §3 |
| 3 | Daily-use, extended-session, or 8-hour-plus interfaces (dashboards, IDEs, internal tools) use a pastel-shifted "therapeutic application palette" (shade 300-400), never the full-saturation shade-600 brand colors, which are reserved for marketing and short-duration viewing. | Soft, low-contrast palettes measurably help ADHD/neurodivergent focus (cited to "Squirrelsong research"). | BRG@9559138 (`07_accessibility.md`, `02_color_system.md`), V11-README |
| 4 | Backgrounds for large reading surfaces use a warm, low-saturation neutral (`#F4F2EF` family), never pure white (`#FFFFFF`); reserve pure white for small contained elements like cards. | Low-saturation pastel backgrounds measurably reduce eye strain and cognitive fatigue in extended reading sessions. | NDR §4, DSD2 §2 |
| 5 | Dark surfaces are never pure black; all dark neutrals carry an indigo undertone (hue ≈ 240) and use a lifted "night" ramp (e.g., `#15151F` to `#23233A`, or the therapeutic ramp `#1a1a2e` to `#3d3d5c`). | Pure black (`#000`) increases halation around white text and raises eye strain (cited to Coding Horror, Stack Exchange). | BRG@9559138 (`02_color_system.md`, `07_accessibility.md`), NDR §4 |
| 6 | The lowest-contrast text token (`--faint`, ≈3.0:1 on beige) is restricted to non-content, decorative use only (dividers, meta icons); it fails WCAG AA (4.5:1) and must never carry text a reader needs to read. | Direct computed-contrast finding; forcing readable content onto sub-AA tokens raises reading effort and cognitive load. | NDR §4, DSD2 §3/§5, HSD §1.2 |
| 7 | Warm accent colors (coral, amber) appear in small, deliberate doses inside the cool-dominant palette to prevent emotional flatness, without overstimulating. | Small warm touches in cool palettes prevent monotony without adding arousal. | BRG@9559138 (`07_accessibility.md`) |
| 8 | Saturated red/orange/danger tokens are intentionally vivid but restricted to short UI phrases, large text, or component chrome, never to body copy or large adjacent zones. | Saturated warm colors spike arousal and interfere with sustained focus near body content. | NDR §4, V11-ACC §1 |
| 9 | Never rely on color alone to convey meaning or category; pair every color distinction with an icon, label, or pattern. Colorblind-safe pairs are pre-approved: Violet+Coral, Azure+Magenta, Indigo+Teal (always safe); Violet+Indigo and Azure+Teal need an added differentiator. | Standard colorblind-accessibility practice; codified as a specific pairing table rather than a general reminder. | BRG@9559138 (`07_accessibility.md`), V11-ACC §3 |

### 2.2 Typography

| # | Rule (operational) | Evidence / citation | Source |
|---|---|---|---|
| 10 | Minimum body font size: 16px web as the shipped floor, with an 18px AAA aspiration for article body copy. (Section 5 flags a live conflict with a separately shipped 14px floor.) | British Dyslexia Association style guide and W3C COGA Task Force converge on larger minimums for reading comprehension. | NDR §5, DSD2 §5, BRG@9559138 (`README.md`) |
| 11 | Body and article line length capped at 60-75 characters; operational target is `--measure: 68ch` (narrowed `.article-wrap` from ~820px/~95-100ch down to 680px). | British Dyslexia Association and W3C COGA Task Force converge on 60-75ch; WCAG SC 1.4.8 (AAA) sets an 80-character ceiling and bans justified text. | NDR §5, DSD2 §3/§5, HSD §1.1.11/§2.3 |
| 12 | Line height 1.5 to 1.7 for body text (brand spec 1.6; up to 1.7 permitted for long-form articles). | WCAG 1.4.8 (AAA) recommends line spacing at least 1.5x font size. | NDR §5, WDH §3.3 |
| 13 | Text is left-aligned everywhere; never justified. | Justified text creates uneven word spacing that disrupts reading flow for dyslexic and ADHD readers (WCAG SC 1.4.8, AAA). | NDR §5, DSD2 §5, BRG@9559138 (`README.md`) |
| 14 | Ship Lexend and Atkinson Hyperlegible as an opt-in "reading mode," self-hosted (not CDN), toggled via a body class, and persisted in `localStorage`; default stays on the profile/brand font. | Lexend was designed with cognitive scientists specifically to reduce visual crowding and demonstrated improved reading speed in randomized trials (cited to a "Bonafide study" in V11-ACC; also Nook, FocusFlow, AudioEye ADHD-font roundups in NDR). Atkinson Hyperlegible (Braille Institute) optimizes letterform distinction (dotted zero, distinct l/1/I) for low vision and dyslexia. | NDR §5, DSD2 §3/§6, V11-ACC §2, BRG@9559138 (`07_accessibility.md`) |
| 15 | Display/decorative fonts (Space Grotesk) are scoped to headings and eyebrows only, never body copy, labels, or form text. | Distinctive, irregular letterforms aid heading scannability but are measurably harder for dyslexic readers at body-text sizes. | NDR §5, DSD1, DSD2 §5, WDH §3.2 |
| 16 | Serif fonts (Newsreader) are scoped to pullquotes of three sentences or fewer; never article body paragraphs. | Serif fonts increase reading difficulty on lower-resolution screens and for some dyslexic readers; the Neurodiversity Design System recommends sans-serif for all digital body copy. | NDR §5, DSD2 §5, WDH §3.2 |
| 17 | No ALL CAPS for body text or form labels; where uppercase eyebrows are used, apply a minimum letter-spacing of 0.08em. | Uppercase running text reduces word-shape recognition and slows reading for dyslexic and ADHD readers. | NDR §5, DSD2 §5 |
| 18 | Paragraph limit: 3 to 4 sentences maximum. | Shorter paragraphs reduce working-memory load and support scanning; stated directly in brand guidelines and reinforced by COGA. | NDR §3, WDH §2, BRG@9559138 (`07_accessibility.md`) |
| 19 | Heading hierarchy: each level at least 20% larger than the level below it. | Recommended by the Neurodiversity Design System (Will Soward) as part of a clear, scannable hierarchy. | NDR §8 |

### 2.3 Motion and animation

| # | Rule (operational) | Evidence / citation | Source |
|---|---|---|---|
| 20 | The `prefers-reduced-motion` fallback must replace spatial transforms (translate, scale beyond 1.05, rotation) with opacity-only fades. Gating a library behind the media query is necessary but not sufficient if the fallback still moves things. | GSAP's own accessibility guidance recommends "reduce to opacity" or "remove entirely" for decorative motion; WCAG SC 2.3.3 (AAA) requires scroll-triggered motion to be disableable. | NDR §6, DSD2 §4 |
| 21 | Auto-playing content longer than 5 seconds must be pausable (WCAG SC 2.2.2, Level A, normative). A stricter internal rule caps decorative autoplay at 3 seconds or 250px of movement. (Section 5 flags this as a numeric mismatch, not a resolved single rule.) | WCAG SC 2.2.2. | NDR §1/§6, V11-ACC §4 |
| 22 | No blinking or flashing faster than 3 times per second; cognitive harm from blinking begins well below the seizure threshold. | WCAG 2.3.1. | NDR §3/§6, V11-ACC §4 |
| 23 | Scroll-jacking or smooth-scroll libraries (Lenis) must be destroyed, not merely skipped, when reduced motion is active (OS preference or in-page toggle). | Removing a user's control over scroll pace is a documented ADHD stressor and a vestibular risk; "destroy vs. skip" is the operational distinction that makes the reduced-motion path real rather than token. | NDR §6, DSD2 §4, WDH §4.1 |
| 24 | Large scroll-coupled parallax and scrub transforms are the single highest-risk animation pattern on a marketing site; replace with a calm-by-default entrance (opacity 0→1, scale 0.98→1, about 600ms ease-out) rather than relying on reduced-motion alone to catch it. | Vestibular disorders affect an estimated 35% of adults over 40, with a documented ADHD/vestibular processing link; scroll-parallax is the classic vestibular trigger and simultaneously the top ADHD attention-capture risk, "ahead of any color question." | NDR §6/§10, DSD2 §4, WDH §4.1, HSD §2.2 |
| 25 | No looping or peripheral decorative motion, ever, not only under reduced motion; pause any infinite loop unconditionally. | Peripheral looping motion involuntarily captures ADHD attention even at low intensity. | NDR §3/§6, DSD2 §4 |
| 26 | Stagger and entrance reveals (opacity plus upward translateY capped at about 16px) are low risk and encouraged; cap stagger step timing at roughly 45 to 60ms increments. | Sequential guided reveals are calming rather than disorienting; excessive stagger density adds unnecessary cascade complexity. | NDR §6, RDC §4, DSD2 §4 |
| 27 | Motion duration is controlled by three named tokens (`--dur-fast`, `--dur-base`, `--dur-slow`) as a single override point so an entire system can be slowed for a calmer pass without touching individual transitions. Ratified values: 240ms / 400ms / 640ms. | Provides a documented "calm hook": changing three values re-tunes all motion system-wide. | RDC §3.1/§4, DSD2 §3 |

### 2.4 Layout, spacing, and interaction

| # | Rule (operational) | Evidence / citation | Source |
|---|---|---|---|
| 28 | Generous, consistent section padding and whitespace (shipped: 124px desktop / 80px tablet section padding). | Busy backgrounds and tight layout measurably increase cognitive load; ample whitespace is a repeated COGA and ADHD-UX recommendation. | NDR §3, RDC §4 |
| 29 | One primary call to action per visual zone; audit and reduce any section carrying multiple competing CTAs. | Multiple competing CTAs cause decision paralysis, disproportionately costly for ADHD users. | NDR §3/§9, WDH §2 |
| 30 | Every page and section follows the same structural pattern (eyebrow, headline, subhead, body); navigation stays in the same location on every page. | Structural surprise breaks re-entry after an attention lapse; matches WCAG SC 3.2.3/3.2.4 (Consistent Navigation / Identification). | NDR §1/§3 |
| 31 | Progressive disclosure: cap dense groupings (e.g., at 4 items) before revealing more; give every section a visible label or anchor so a reader who paused mid-scroll can reorient instantly. | Reduces the cost of re-entry after attention lapses; directly serves COGA's "support memory and attention" objective. | NDR §1/§3/§7 |
| 32 | Touch targets minimum 44×44px for primary or secondary controls; minimum 40×40px for icon-only buttons. | WCAG 2.5.8 (Target Size, AAA). | RDC §1.3, V11-ACC §3 |
| 33 | Every focusable element shows a visible focus ring (shipped spec: 3px solid azure, 2px offset, 3px corner radius); never remove an outline without a replacement. | WCAG 2.4.7 (Focus Visible) and 2.4.11 (Non-text Contrast, new in 2.2); disproportionately used by ADHD users who navigate by keyboard. | NDR §3, RDC §2/§3.1, DSD2 §3, V11-ACC §3 |
| 34 | Support 200% browser zoom without layout breakage, truncation, or horizontal scroll. | Standard low-vision accessibility requirement, retained as an explicit test-before-ship item. | BRG@9559138 (`07_accessibility.md`), V11-ACC §6 |
| 35 | Ship a `prefers-contrast: more` override that upgrades muted text to secondary-text contrast and removes soft/tinted backgrounds. | Gives users who need maximum contrast a system-level override rather than requiring a manual in-product toggle. | V11-ACC §5 |

### 2.5 Cognitive load and content structure (design-adjacent)

| # | Rule (operational) | Evidence / citation | Source |
|---|---|---|---|
| 36 | Reduce cognitive load by limiting the number of choices and competing visual elements on any one page or section. | Each additional decision or distractor costs disproportionately more for ADHD users than for neurotypical users (W3C COGA). | NDR §1 |
| 37 | Close every major section with a 1-2 sentence plain-language "so what" summary, before the CTA. | Lets a reader who skipped the body still land the key message; an explicit ADHD-reader accommodation. | NDR §7/§10, HSD §4.4 |
| 38 | Cap metaphor use at 2 distinct metaphors per page ("GPS for health" is the signature; keep the rest literal). | Metaphor stacking raises cognitive load for some autistic and ADHD readers who process language more literally. | NDR §7, HSD §4.4 |
| 39 | Define acronyms and jargon on first use; prefer benefits framing over feature framing. | Undefined technical vocabulary ("COGA," "FAIR," "multimodal embedding space") alienates lived-experience contributors and patient advocates; benefits land better for ADHD readers than mechanism descriptions. | NDR §7 |
| 40 | Prefer bullet lists over dense prose for any feature or capability list. | Reduces parsing effort versus paragraph-embedded lists; matches COGA's "reduce cognitive load" guidance. | NDR §3, WDH §2 |
| 41 | Long-form documents and pages open with a BLUF or a one-line "if you only read one thing" anchor, plus a stated reading-time estimate. | Not sourced to external literature; self-modeled convention observed consistently across every long Cytognosis research and decision document reviewed for this inventory (NDR, DSD2, WDH, HSD all open this way). Treated here as a design-adjacent content principle worth carrying into the product itself, not only internal docs. | NDR, DSD2, WDH, HSD (structural, all) |

### 2.6 Condition-specific pattern bundles

| # | Condition | Pattern bundle | Source |
|---|---|---|---|
| 42 | ADHD | Clear visual hierarchy with generous whitespace; short paragraphs (3-4 sentences); bolded key information for scanning; minimal or no autoplay; low-contrast pastel themes for daily-use surfaces; avoid clutter, prioritize progressive disclosure; consistent, predictable layouts. | BRG@9559138 (`07_accessibility.md`), NDR §3 |
| 43 | Dyslexia | Sans-serif for all primary text; line height 1.5 or greater; left-aligned only; no long italic passages; Lexend or OpenDyslexic for patient-facing forms; Atkinson Hyperlegible for instructions and labels. | BRG@9559138 (`07_accessibility.md`) |
| 44 | Autism spectrum | Predictable, consistent layouts; avoid sensory-overloading animation or color flashes; clear literal language (avoid unexplained idioms); present structured information as tables and lists. | BRG@9559138 (`07_accessibility.md`) |
| 45 | Anxiety and depression | Warm, hopeful color accents alongside cool calming tones; progress indicators to reduce uncertainty; non-alarming error states (avoid harsh red full-screen treatments); encouraging, non-judgmental microcopy. | BRG@9559138 (`07_accessibility.md`) |

**45 visual/interaction principles distilled in Section 2.**

---

## 3. Tone and content principles

Same format: operational rule, evidence, source.

| # | Rule (operational) | Evidence / citation | Source |
|---|---|---|---|
| 46 | Voice is authoritative, compassionate, and optimistic; never "revolutionary," "breakthrough," "cure," or fear/urgency-based messaging. | Stated brand mandate; reinforced across every content-facing document as the one universal, non-negotiable rule. | WDH §2, V11-WRITE |
| 47 | Banned words (union list): revolutionary, breakthrough, cure, game-changing, disrupt, cutting-edge, best-in-class, seamless, powerful (unqualified), just, simply, only, whoops. | Each carries either a false-certainty risk (health claims) or a minimizing effect ("just," "simply") that reads as dismissive to an anxious reader. | V11-WRITE, BRG@9559138 (`README.md`) |
| 48 | Non-diagnostic safety rules, always: never claim to diagnose disease, predict disease with certainty, replace clinicians, recommend treatment, or make medical decisions. Always retain uncertainty language (confidence bounds, sample size) and a human fallback ("contact your care team"). | Direct organizational mandate tied to Cytognosis's non-diagnostic research positioning. | V11-WRITE, WDH §2 |
| 49 | Person-first language for any medical or disability reference ("people with ADHD," not "ADHD people"). | Standard person-first-language practice, stated as a house rule. | WDH §2 |
| 50 | Reading-level targets: Flesch-Kincaid grade 7-9 for landing and general copy; grade 10+ acceptable for technical blog content aimed at scientists; flag anything above grade 10 in non-technical copy at the verification gate. | WCAG SC 3.1.5 (Reading Level, AAA) recommends supplemental lower-complexity content when reading level exceeds lower-secondary education. | NDR §7, WDH §2, HSD §4.5 |
| 51 | One idea per sentence; sentences over 25 words consistently test harder regardless of word difficulty. | Plain-language research synthesis (Siteimprove, Acrolinx, Harvard accessible-content technique, cited in NDR §7). | NDR §7, HSD §4.5 |
| 52 | Mechanics: active voice throughout, Oxford comma always, no em dashes anywhere (use commas or semicolons). | House style, applied uniformly across every reviewed document including this one. | WDH §2, V11-WRITE, all sources |
| 53 | Frame benefits over features. Example given: "This helps your doctor see your health trajectory over time" over "Our multimodal embedding engine generates continuous health-state coordinates." | ADHD readers respond better to concrete benefit statements than to mechanism-forward technical language. | NDR §7 |
| 54 | Voice is tuned per surface on three dials (warmth, precision, length), not applied uniformly: Foundation (marketing) is high warmth/medium precision/short length; Clinical (patient-facing) is highest warmth/high precision/shortest length; Research (internal/scientific) is low warmth/highest precision/longest length; Lab (dev tooling) is lowest warmth/high precision/short length. | Different readers in different emotional states need different registers; a single voice would either under-serve a distressed patient reader or waste a researcher's time with excess warmth. | V11-WRITE, V11-PROF |
| 55 | Clinical-register copy is calm and non-alarming by explicit construction: acknowledge uncertainty, always state a concrete next step, always include a human fallback; never use "simply / just / only." Errors, empty states, and alerts are written as specific and actionable, not generic or severity-coded ("Call your care team today" rather than "Critical: immediate action required"; "We couldn't save that, your note is still here" rather than "Something went wrong"). | Matches the anxiety/depression pattern bundle (#45) at the copy layer; a distressed reader benefits from specificity and an offered next action more than from a technically accurate but emotionally flat error code. | V11-WRITE, V11-PROF |
| 56 | No filler phrases ("great question," "I'd be happy to help"); do not perform emotion in system copy ("whoops!" is explicitly banned, replaced with silence). | Filler and performed emotion read as insincere and add reading burden without information value. | WDH §2, V11-WRITE |

**11 tone and content principles distilled in Section 3.**

**Total distilled: 56 principles (45 visual/interaction + 11 tone/content).**

---

## 4. Checklist: auditable yes/no items

Organized to run directly against a design system's tokens, components, motion layer, and copy.

### 4.1 Tokens and color

- [ ] Every background used for extended reading is a warm or cool low-saturation neutral, never pure white or pure black.
- [ ] Dark-theme neutrals carry a consistent hue tint (never neutral gray, never `#000000`).
- [ ] A pastel/soft (300-400 shade) token set exists and is used for any daily-use, dashboard, or 8-hour-plus surface, separate from the full-saturation brand (600 shade) tokens.
- [ ] The lowest-contrast text token in the system is documented as non-content-only and is not used on any content string in the codebase.
- [ ] Every body-text link on a light background uses a token that clears 5:1, not the decorative-only accent token.
- [ ] Every danger/error/warning token is restricted to short phrases, icons, or large text; none is applied to a body-copy text color.
- [ ] A documented colorblind-safe pairing table exists, and no component distinguishes categories by color alone without an icon, label, or pattern.
- [ ] The system names which token is "calm default" and which is "canonical strong," with a one-line rule for when each applies.

### 4.2 Typography

- [ ] Minimum body font size is 16px or larger (18px for long-form article bodies).
- [ ] Body and article measure does not exceed 75 characters per line (target ≈68ch).
- [ ] Line height for body text is 1.5 or greater.
- [ ] No component sets `text-align: justify` anywhere.
- [ ] An opt-in accessible reading-mode font stack (Lexend and/or Atkinson Hyperlegible) is shipped, self-hosted, and persists a user's choice.
- [ ] Display/decorative fonts never appear in a body-copy, label, or form-input role.
- [ ] Serif fonts, if used, are scoped to pullquotes of 3 sentences or fewer.
- [ ] No body text or form label is set in ALL CAPS; any uppercase eyebrow/label has letter-spacing ≥0.08em.
- [ ] Heading scale steps are each at least 20% larger than the level below.

### 4.3 Motion

- [ ] The reduced-motion path (OS preference or in-page toggle) replaces spatial transforms with opacity-only change; it is not merely a media-query wrapper around the same animation.
- [ ] Any smooth-scroll or scroll-jacking library is destroyed (instance removed), not just paused, when reduced motion is active.
- [ ] No component contains scroll-coupled parallax or scrub transforms as the default, unconditional experience.
- [ ] No animation loops indefinitely in the periphery under any settings.
- [ ] No autoplaying content exceeds 5 seconds without a pause control (harder internal target: 3 seconds or 250px of travel).
- [ ] No component flashes or blinks faster than 3 times per second.
- [ ] Motion duration is controlled through a small number of named tokens (fast/base/slow), not hardcoded per component.
- [ ] Stagger/cascade entrance timing is capped at a documented step interval (≈45-60ms).

### 4.4 Layout and interaction

- [ ] Section padding and whitespace are generous and consistent across the system, not ad hoc per page.
- [ ] No section ships more than one primary call to action in the same visual zone.
- [ ] Every page follows the same structural section pattern (label, headline, subhead, body) and keeps navigation in a constant location.
- [ ] Dense content groupings are capped (e.g., 4 items) with an explicit "show more," not dumped in full by default.
- [ ] All primary/secondary interactive controls meet a 44×44px minimum touch target; icon-only controls meet 40×40px.
- [ ] Every focusable element has a visible focus indicator at ≥3:1 contrast; no `outline: none` without a replacement.
- [ ] The layout holds at 200% browser zoom with no truncation and no forced horizontal scroll.
- [ ] A `prefers-contrast: more` (or equivalent) override exists and has been tested.

### 4.5 Copy and content

- [ ] No banned word (revolutionary, breakthrough, cure, game-changing, disrupt, cutting-edge, best-in-class, unqualified "powerful," just/simply/only, whoops) appears anywhere in shipped copy.
- [ ] Every claim about health outcomes retains uncertainty language and never implies diagnosis, treatment recommendation, or a claim to replace a clinician.
- [ ] Person-first phrasing is used for every medical or disability reference.
- [ ] General/landing copy scores Flesch-Kincaid grade 7-9; anything above grade 10 outside technical/scientific content is flagged for revision.
- [ ] No sentence in reviewed copy exceeds roughly 25 words as a matter of routine, not exception.
- [ ] No em dashes appear anywhere; Oxford comma is used consistently; voice is active, not passive.
- [ ] Every major section closes with a 1-2 sentence plain-language summary before its CTA.
- [ ] No page uses more than 2 distinct metaphors.
- [ ] Every acronym or technical term is defined on first use per page.
- [ ] Copy register matches its surface (Foundation/Clinical/Research/Lab voice dials), not a single uniform tone applied everywhere.
- [ ] Clinical-register error, empty-state, and alert copy names a concrete next step and a human fallback; none reads as a bare error code or an unqualified severity label.
- [ ] Long-form pages/documents open with a BLUF-style anchor line stating the single most important takeaway.

---

## 5. Conflicts and open tensions

| Tension | Where canonical/vibrant applies | Where calm/muted applies | Resolution status |
|---|---|---|---|
| **Canonical brand vibrancy vs. calm-by-default.** Full-saturation identity triad (`#8B3FC7` violet, 135deg signature gradient) vs. muted calm tokens (`#6E5BD1` violet, pastel 300-shade daily-use palette). | Logos; the single signature gradient; body-text links needing extra contrast margin (`--violet-strong`); print, decks, IDE themes, and other short-exposure or internal-only surfaces. | The public website body and UI at large; any daily-use surface with extended sessions (dashboards, IDEs); any anxiety-sensitive or neurodivergent-facing surface. | **Resolved as a stated governing principle** ("calm by default, canonical-strong on recognition moments") in DSD1/DSD2, but the rule is enforced by convention and documentation, not by a linter or build-time check (confirmed by RCI: no schema validation exists anywhere in the reviewed materials). |
| **Warm beige vs. cool indigo-tinted light background.** Website uses `#F4F2EF` (warm). Canonical brand-skill light background ("Ghost Day") is `#F8F8FC` (cool, indigo-tinted, matching the "every neutral carries an indigo undertone" rule stated elsewhere in the same lineage). | Print, decks, internal tools, IDE themes (per DSD1/DSD2's explicit carve-out). | The public website (compassion-positioning rationale for a health nonprofit). | **Resolved by scope, not by value.** Two different "light theme truths" now coexist depending on surface; nothing in the corpus unifies them, and a reader who only sees one document will not know the other exists. |
| **Minimum body font size.** NDR argues for an 18px AAA target and treats 16px as a gap to close upward. V11-ACC (the current, newest accessibility spec) states a 14px web floor. | N/A | N/A | **Open, unresolved.** The website's own shipped spec (16px, 18px article) is more conservative than V11-ACC's system-wide 14px floor. Whoever revises the shared design system next should pick one number; recommend keeping the more conservative 16px floor given the weight of neurodiversity evidence behind it. |
| **Autoplay/motion duration ceiling.** WCAG SC 2.2.2 (normative, Level A) sets 5 seconds as the pausability threshold. V11-ACC's internal rule is stricter: no autoplay beyond 3 seconds or 250px of travel. | N/A | N/A | **Not a real conflict, but undocumented as intentional.** The stricter internal number is not cited to any evidence; it reads as a reasonable margin over the WCAG floor but should be labeled as a deliberate internal tightening, not left looking like an inconsistency. |
| **Two accessibility documents, two rigor profiles, un-reconciled.** V11-REF11 (stale, carried byte-identical across `v11`, `v11_1`, and `v11_1_1`) still contains the full "Mental Health & Therapeutic Design" section with its NIH/Squirrelsong/Coding-Horror/chromotherapy citations. V11-ACC (the newest, actively maintained file) replaced this with a WCAG-2.2 profile-based contrast audit and dropped the evidence-narrative section entirely, while also flagging its own contrast numbers as "pending re-audit against the v11 ramp." | N/A | N/A | **Open and material.** The newer document is more rigorous on measured contrast but has quietly lost the explicit therapeutic-design rationale and citations that justified the palette in the first place. Recommend merging: keep V11-ACC's audit rigor, restore V11-REF11's evidence section (or point to this inventory), and delete the stale duplicate once merged. |
| **Serif choice for "calm/reassuring" contexts.** The website chose Newsreader over the canonical Source Serif Pro for licensing and shipping reasons only, not an evidence-driven choice. Separately, V11-PROF's Clinical profile (the design system's own "calm, reassuring" surface) specifies Source Serif Pro italic for short reassurances. | V11-PROF's Clinical profile (Source Serif Pro). | The public website (Newsreader). | **Open, low-severity.** Two products aimed at similar calm/reassuring goals made different, uncoordinated serif choices for non-evidence reasons (font licensing and shipping timing). Worth a single decision the next time both surfaces are touched together. |
| **Accessibility font stack order.** NDR and WDH order the reading-mode stack Lexend-first, then Atkinson Hyperlegible. RDC's "v3" proposal orders it Atkinson-Hyperlegible-first, then Lexend. | N/A | N/A | **Minor, unresolved.** Both fonts are validated for different populations (Lexend: ADHD/dyslexia reading speed; Atkinson Hyperlegible: low-vision letterform distinction), so stack order matters as a default. Recommend Lexend first (broader neurodivergent evidence base per this corpus) with Atkinson Hyperlegible as an explicit "low-vision mode" second option, matching NDR's original recommendation. |
| **Where "calm" comes from, conceptually.** The branding-repo/v9-v10 lineage (BRG@9559138, V11-README) frames the canonical cool-hue palette itself as inherently therapeutic, "calm" is a property of being in the blue/violet/teal hue family at all. The website-specific research (NDR, DSD1/2) treats calm as something actively achieved by further muting saturation and slowing/removing motion, on top of an already-cool palette. | N/A | N/A | **Conceptual tension, not yet named anywhere in the corpus.** This affects how much license a designer has to reuse canonical colors "as is" and call the result calm, versus needing to actively dial down saturation and motion regardless of hue family. The evidence in this corpus supports the second, stricter view: hue family alone (cool vs. warm) is necessary but not sufficient, saturation and motion reduction are what the actual before/after decisions (DSD1, DSD2) spent nearly all their effort on. |
| **Considered and declined, not a live conflict.** RDC floated softening the beige further (to `#F6F4F1`) and increasing section padding to 140px as calm-revision hooks. DSD2 explicitly declined both, on the grounds that motion and reading-load fixes rank far higher in leverage than further palette or spacing micro-adjustments. | N/A | N/A | **Resolved; noted here only so a future reader of RDC in isolation does not mistake a floated hook for a shipped decision.** |

---

## 6. Follow-up needed (out of session scope)

Two `cytomem_recall` hits could not be retrieved because they live outside this session's attached folders:

1. `docs` repo, path `07-Design/adhd-neurodiversity-design-research.md` (semantic match score 0.848 against "neurodiverse design research"). Title suggests this may be a consolidated-docs-repo copy or successor of NDR; unclear if it is a duplicate or contains net-new material.
2. `website` repo (the live git repo at `~/repos/cytognosis/website`, distinct from the Claude Projects `Website/` research folder used throughout this inventory), paths `.agents/skills/brand/references/design-system.md` and `docs/design_requirements.md`.

Recommend attaching `~/repos/cytognosis/website` and the `docs` repo to a future session and re-running the same `cytomem_recall` queries to confirm whether either document adds principles not already captured above.

---

*End of inventory. 56 principles distilled across Sections 2 and 3, with a 45-item cross-cutting audit checklist in Section 4 and 9 named conflicts/tensions in Section 5.*
