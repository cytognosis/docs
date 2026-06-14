> **Status**: Active
> **Date**: 2026-06-14
> **Author**: Cytognosis Foundation
> **Audience**: designers, engineers, brand reviewers
> **Tags**: `branding`, `cytognosis-branding`, `design-system`, `v10`

# cytognosis-branding — Deep Brand Reference Skill

> **Reading time**: ~6 minutes
> **If you only read one thing**: Load `cytognosis-design-system-master` for routine design tasks. Load THIS skill only when you need the full v10 brand book depth: complete shade scales, every icon variant, full accessibility audit, complete template library.

---

## What It Is and Why

`cytognosis-branding` is the **deep-content home** for the Cytognosis Foundation v10 brand documentation. It contains 12 numbered reference files covering the complete brand system: color, typography, logo, iconography, imagery, motion, layout, templates, accessibility, and data visualization.

This is the reference library, not the operational entry point. For most design tasks, load `cytognosis-design-system-master` instead. That skill carries the cheatsheets and operational kits, and routes to this skill only when depth is needed.

### When to load THIS skill (not design-system-master)

- Need the **full color system** with per-color shade scales and CVD safety
- Need the **full typography spec** with all weights and hard rules
- Need the **full logo placement matrix** (every lockup, every size, every background)
- Need the **full iconography spec** for all 48 icons
- Need the **full imagery sourcing rules** and shot list
- Need the **full motion library** with all durations and easings
- Need the **full layout grid** with spacing scale, radii, and shadows
- Need the **complete template library** (deck, docs, email, social, print)
- Need the **full WCAG audit** with contrast matrices and neurodiversity provisions
- Need the **full data-viz palette** and pattern rules
- Any request explicitly citing the "full v10 documentation" or "12 sections"

### When NOT to load this skill

For routine design tasks (applying brand colors, writing copy, picking a profile, placing a logo), load `cytognosis-design-system-master` instead. Do not load both skills in the same response.

---

## Skill Family Positioning

| Need | Load |
|------|------|
| Cheatsheets, tokens at a glance, profile picker, asset paths | `cytognosis-design-system-master` |
| Full v10 references (this skill) | `cytognosis-branding` |
| Building or revising an interface template | `cytognosis-template-master` |
| Voice rules for grant / scientific writing | `cytognosis-writer` |
| Coordinated task across multiple Cytognosis skills | `cytognosis-orchestrator` |

---

## The 12 v10 Reference Files

| File | Load When |
|------|----------|
| `references/01_brand_foundation.md` | Mission, identity, narrative architecture, brand pillars, platform architecture |
| `references/02_voice_and_tone.md` | Voice rules, audience messaging, terminology, do/don't |
| `references/03_logo.md` | Logo placement, lockups, clear space, minimum size, approved backgrounds, don'ts, favicon, social |
| `references/04_color_system.md` | Full fluorophore-derived palette, per-color shade scales, named gradients, neutrals, CVD safety |
| `references/05_typography.md` | Type families with alternates, scale (Major Third), weights, hard rules, accessibility fonts |
| `references/06_iconography.md` | 48-icon set spec, color semantics, usage rules, gap-filling rules |
| `references/07_imagery.md` | Photography + illustration tone, treatment, palette grading, sourcing checklist, shot list |
| `references/08_motion.md` | Durations, easings, what to animate, motion patterns, reduced-motion |
| `references/09_layout.md` | 12-column grid, spacing scale, radii, shadows, glassmorphism rules |
| `references/10_templates.md` | Deck (12 layouts), one-pager, email signature, social cards, print |
| `references/11_accessibility.md` | WCAG 2.2 AA + AAA, contrast audit, hit targets, focus, non-color signal, neurodiversity |
| `references/12_dataviz.md` | Chart palettes, sequential, diverging, multi-series, pattern fills for colorblind contexts |

Load only the file relevant to the current task. Loading two reference files in the same response burns context.

---

## Operational Kits

```
templates/deck/                   12-layout reference deck (light + dark themes)
templates/email-signature.html    full + compact variants; email-client safe
```

For decks, copy `templates/deck/` and customize. The deck ships with `theme.css`, `deck-stage.js`, and 12 layouts.

---

## Identity at a Glance

| Field | Detail |
|-------|--------|
| Legal name | Cytognosis Foundation, Inc. |
| Type | 501(c)(3) Nonprofit |
| EIN | 39-4383634 |
| UEI | HS4PRLL7AKY5 |
| Founded | September 8, 2025 |
| HQ | South San Francisco, CA |
| Website | https://www.cytognosis.org/ |

**Vision**: To transform healthcare from reactive treatment of disease to proactive preservation of healthspan.

**Mission**: To pioneer a cellular intelligence platform that maps personalized health states, detecting and intercepting disease years before symptoms emerge.

**Promise**: To make precision health a human right, not a privilege.

**Primary tagline**: "Before diagnosis. Before symptoms. There's Cytognosis."

---

## Brand Pillars

| Pillar | Statement |
|--------|-----------|
| Prevention Over Treatment | Detect disease before it defines destiny. |
| AI-Powered Precision | Where artificial intelligence meets human intuition. |
| Equitable Access | Healthcare innovation for all, not just some. |
| Time as Medicine | Every moment before symptoms is a lifetime saved. |

---

## Platform Architecture

| Component | Role | Metaphor |
|-----------|------|---------|
| Cytoverse | AI health mapping system | The Map |
| Cytoscope | Programmable biosensors | The Sensor |
| Cytonome | On-device causal AI navigator | The Navigator |
| Helix model | Foundation AI model | The Engine |

---

## Key Tokens at a Glance

(Full color spec in `references/04_color_system.md`; full type spec in `references/05_typography.md`.)

- **Identity triad**: Violet `#8B3FC7`, Azure `#3B7DD6`, Indigo `#5145A8`
- **Accents**: Magenta `#E0309E` (attention only), Coral `#F26355` (warmth), Teal `#14A3A3` (success)
- **Type**: Inter (display + body), Newsreader (accent), JetBrains Mono (code)
- **Dark bg**: `#1E1E32` (Rich Night), never pure black
- **Light bg**: `#F0F0F7` (Pale Day), never pure white
- **Signature gradient**: `linear-gradient(135deg, #3B7DD6 0%, #8B3FC7 50%, #5145A8 100%)`

---

## Asset Paths

Canonical assets live in the branding repo at `design-system/assets/`:

- `logos/`: wordmark + mark; light/dark; SVG + PNG
- `icons/{line,solid}/`: 48 icons per variant; individual files
- `icons/_bundle-line.svg`, `_bundle-solid.svg`: consolidated `<symbol>` sprites for embed
- `products/`: Cytoverse / Cytoscope / Cytonome / Helix marks
- `fonts/`: self-hosted production fonts (when licensed)

---

## Hard NEVER

- Pure black `#000000` or pure white `#FFFFFF`
- Tailwind Indigo `#6366f1` or any "SaaS purple"
- Emoji in product surfaces
- Fraunces, Urbanist, Arial, or Times as default typefaces
- Gradient backgrounds at viewport scale (accent only)
- Stock-photo doctors-with-clipboards imagery
- Em dashes in any output
- Passive voice in marketing or product copy
- "Revolutionary", "cure", "game-changing", "breakthrough" as hype words
- Recoloring microscopy or fluorescence imagery away from its true color
- Drop shadows, glows, or bevels on the logo

---

## Tone

Compassionate, scientifically rigorous, hopeful. Never hype-driven. Always pair urgency with evidence. The Revelation Arc structures every Cytognosis narrative: **Mystery → Insight → Resolution**.

---

## Example: When to Load This Skill vs. design-system-master

**Routine**: "What color is the Azure token?" → Load `cytognosis-design-system-master` (cheatsheet has it).

**Deep reference**: "Give me every shade in the Azure color scale with their hex values, contrast ratios, and CVD-safe alternatives." → Load `cytognosis-branding` → read `references/04_color_system.md`.

**Routine**: "Apply the signature gradient to this hero section." → Load `cytognosis-design-system-master`.

**Deep reference**: "I need every named gradient in the system, its use case, and whether it passes WCAG AA." → Load `cytognosis-branding` → read `references/04_color_system.md` and `references/11_accessibility.md` (in separate responses).
