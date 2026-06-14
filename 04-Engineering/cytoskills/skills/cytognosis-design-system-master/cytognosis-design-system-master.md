> **Status**: Active
> **Date**: 2026-06-14
> **Author**: Cytognosis Foundation
> **Audience**: designers, engineers, writers
> **Tags**: `design-system`, `cytognosis-design-system-master`, `branding`, `tokens`

# cytognosis-design-system-master — Design System Master Skill

> **Reading time**: ~7 minutes
> **If you only read one thing**: Load this skill first for any visual design, styling, branding, or copy task. It carries all the tokens and rules you need for 90% of work. Route to `cytognosis-branding` only for full v10 depth.

---

## What It Is and Why

`cytognosis-design-system-master` is the **master entry skill** for the Cytognosis Foundation Design System (v10). It provides operational cheatsheets for colors, typography, voice, profiles, and assets that cover most daily design and writing tasks without needing to load the full v10 reference files.

**When to load this skill**:

- Designing or styling anything for Cytognosis: web pages, product UI, slide decks, social cards, email signatures, CSS
- Applying brand voice or writing microcopy
- Conducting accessibility audits
- Picking a brand profile (Foundation / Clinical / Research / Lab)
- Applying logos, icons, or data viz palettes
- Any Cytognosis-branded artifact

**When NOT to load this skill**:

- Scaffolding interface app templates (phone, web, desktop, extension): use `cytognosis-template-master`
- Full v10 depth (every shade, every icon variant, full accessibility matrices): load `cytognosis-branding` instead
- Do not load this skill and `cytognosis-template-master` in the same response

---

## Organization Identity

Cytognosis Foundation is a 501(c)(3) building "GPS for Human Health": a cellular intelligence platform that detects and intercepts disease years before symptoms emerge.

| Component | Role | Metaphor |
|-----------|------|---------|
| Cytoverse | AI health mapping system | The Map |
| Cytoscope | Programmable biosensors | The Sensor |
| Cytonome | On-device causal AI navigator | The Navigator |
| Helix model | Foundation AI model | The Engine |

**Taglines**: "Before diagnosis. Before symptoms. There's Cytognosis." (primary, 54 chars) / "GPS for human health." (metaphor) / "See disease coming. Change its course." (impact)

---

## Color Tokens (Cheatsheet)

```
IDENTITY TRIAD (the brand)
  --cg-violet-600   #8B3FC7   MAIN BRAND (DAPI, DNA stain, 461nm)
  --cg-azure-600    #3B7DD6   the Patient, data input (Alexa Fluor 488)
  --cg-indigo-500   #5145A8   the Pioneer, AI outputs (UV excitation, 358nm)

SECONDARY (support)
  --cg-teal-600     #14A3A3   biological harmony, success (GFP, 509nm)
  --cg-coral-600    #F26355   human warmth, hope (MitoTracker, 576nm)
  --cg-magenta-600  #E0309E   ATTENTION ACCENT ONLY (Rhodamine, 565nm)

SIGNATURE GRADIENT (the "Patient to Pioneer" wash)
  linear-gradient(135deg, #3B7DD6 0%, #8B3FC7 50%, #5145A8 100%)

NEUTRALS (all carry hue 240 indigo undertone; never pure)
  --bg-ink-deep     #0A0A14   darkest dark background
  --bg-rich-night   #1E1E32   default dark background
  --bg-pale-day     #F0F0F7   default light background
  --bg-clinical     #F5F5FA   clinical light variant

TYPE (per-category default + 2 alternates)
  --font-display    'Inter'                 alts: General Sans, IBM Plex Sans
  --font-accent     'Newsreader'            alts: Source Serif Pro, Recursive
  --font-code       'JetBrains Mono'        alts: Fira Code, Recursive Mono
  --font-a11y       'Atkinson Hyperlegible' (patient forms, low vision)
                    'Lexend'                (ADHD, dyslexia)
```

---

## Visual Hard Rules

1. **Never pure black.** Darkest is `#0A0A14` (indigo-tinted).
2. **Never pure white.** Light mode uses `#F0F0F7` (Pale Day) for foundation; `#F5F5FA` for clinical.
3. **Neutrals carry hue ~240** (indigo undertone). No `#888`, no `#333`.
4. **Identity triad = Azure → Violet → Indigo.** Magenta is **attention only**.
5. **Body text 16px minimum**, line-height 1.6, **left-aligned only** (never justified).
6. **Card radius 16px**, **button radius 8px** (pill 9999px for marketing only). Inputs 6px. Modals 20px.
7. **Glassmorphism sparingly**: `rgba(30,41,59,0.4)` + `backdrop-filter: blur(12-16px)`. Never stack glass on glass.
8. **Motion durations**: 150ms (fast), 250ms (base), 350ms (slow), 500ms (slower). `ease-out` for micro, `ease-in-out` for transitions. Honor `prefers-reduced-motion`.
9. **60fps only**: animate `transform` and `opacity` only.
10. **No drop shadows on the logo.** No bevels, no glows on the mark.

---

## Voice Hard Rules

1. **No em dashes.** Use commas, semicolons, periods, or parentheses.
2. **No emoji** in product or marketing.
3. **No "patients"** (except clinical context). Use "people", "individuals", "you", or role name.
4. **No hype words**: revolutionary, cure, game-changing, breakthrough, disrupt.
5. **Oxford comma always.** Title Case headings, sentence case for UI labels.
6. **Active present tense.** "We detect disease," not "Disease is detected by us."
7. **Lead with what it means for the reader**, then how it works.
8. **Three voice tensions**: visionary yet grounded, scientific yet accessible, empathetic yet professional.
9. **The Revelation Arc**: Mystery → Insight → Resolution.
10. **Capitalization**: "Cytognosis" always capital C; product names capital (Cytoverse, Cytoscope, Cytonome, Helix model).

---

## Profile Selection (Cheatsheet)

| Profile | Surface | Type | Palette | Voice |
|---------|---------|------|---------|-------|
| **Foundation** | cytognosis.org, decks, social, press | Inter / Newsreader / JetBrains Mono | Signature triad gradient | Visionary, hopeful |
| **Clinical** | Patient + consumer app | Inter / Source Serif Pro / JetBrains Mono | Muted 300-shade pastels | Calm, reassuring |
| **Research** | Cytoverse workbench, dashboards | IBM Plex Sans + Plex Mono | Indigo + magenta alert | Precise, neutral |
| **Lab** | CLI, editor, dev docs, terminal | Recursive (variable axes) | Violet-300 on ink | Technical, playful |

Decision tree:

- Prospective audience (investors, press, partners) → **Foundation**
- Someone who just learned something worrying about their body → **Clinical**
- Scientists with a hypothesis → **Research**
- Developers shipping code → **Lab**
- Public-facing default: **Foundation**
- Internal default: **Research**

---

## Reference Files (When to Load)

| Reference | Load when |
|-----------|-----------|
| `references/tokens.md` | Applying or changing colors, type, spacing, shadows, radii, motion |
| `references/voice.md` | Writing copy, microcopy, error messages, headlines, taglines |
| `references/logo-and-marks.md` | Placing or adapting any Cytognosis mark; favicon, social avatar |
| `references/iconography.md` | Picking, sourcing, or revising icons; gap-filling rules |
| `references/profiles.md` | Picking among Foundation / Clinical / Research / Lab; mixing profiles |
| `references/accessibility.md` | Contrast audit, screen-reader, keyboard, reduced motion, a11y typography |
| `references/motion.md` | Choosing duration / easing; what to animate, what not to |
| `references/governance.md` | Versioning, changelog, contribution, sync with Claude Design |

For **deep content** (full v10 shade scales, every icon variant, full WCAG matrices), load `cytognosis-branding`.

---

## Asset Inventory

```
assets/
├── logos/
│   ├── cytognosis-light.svg / .png    (dark wordmark for light backgrounds)
│   ├── cytognosis-dark.svg / .png     (light wordmark for dark backgrounds)
│   ├── cytognosis-mark.svg / .png     (icon-only "C" glyph)
│   └── cytognosis-mark-square.svg     (square version for favicon / avatar)
├── icons/
│   ├── _bundle-line.svg               (48 icons as <symbol> sprites; line variant)
│   └── _bundle-solid.svg              (48 icons as <symbol> sprites; solid variant)
└── products/
    ├── cytoverse.png
    ├── cytoscope.png
    ├── cytonome.png
    └── helix-model.png
```

---

## Hard NEVER List

- Pure black `#000000` or pure white `#FFFFFF`
- Tailwind Indigo `#6366f1` or any other "SaaS purple" that isn't `#8B3FC7`
- Em dashes in any output
- Emoji in product surfaces
- Fraunces, Urbanist, Arial, or Times as default typefaces
- Gradient backgrounds at viewport scale
- Stock-photo "diverse team around a monitor" imagery or doctors-with-clipboards
- Recoloring microscopy or fluorescence imagery away from true fluorophore color
- Drop shadows / glows / bevels / outlines on the Cytognosis logo
- Magenta as part of identity (it is attention only)
- Justified text or center-aligned body copy
- "Patient" outside clinical context; "user" anywhere; hype words anywhere
- Animation that ignores `prefers-reduced-motion`

---

## Routing to Sibling Skills

| Task | Skill |
|------|-------|
| Scaffolding or revising an interface template | `cytognosis-template-master` |
| Deep reference into the 12 v10 brand docs | `cytognosis-branding` |
| Building or configuring Cytognosis software | `cytognosis-dev` |
| Where files live, Google Workspace ops | `cytognosis-org` |
| Grants, proposals, narratives, scientific writing | `cytognosis-writer` |
| Unsure which skill to load | `cytognosis-orchestrator` |

---

## Example 1: Applying the Signature Gradient

Task: "Add the signature gradient to this marketing hero section."

1. Load `cytognosis-design-system-master` (cheatsheet has the gradient).
2. Apply: `background: linear-gradient(135deg, #3B7DD6 0%, #8B3FC7 50%, #5145A8 100%)`.
3. Confirm text color uses `--bg-pale-day` (`#F0F0F7`), not white.
4. Confirm gradient is at hero scope, not full viewport.

## Example 2: Picking a Profile for a New Dashboard

Task: "What profile should a clinician-facing workbench use?"

1. Load `cytognosis-design-system-master` (profile cheatsheet).
2. Audience = clinicians with a hypothesis about a patient = **Research** profile (precise, neutral, Indigo + magenta alert).
3. Note: if the dashboard has a patient-facing view, that surface switches to **Clinical**.
