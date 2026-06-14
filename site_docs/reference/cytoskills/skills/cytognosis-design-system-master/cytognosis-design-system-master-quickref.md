> **Status**: Active
> **Date**: 2026-06-14
> **Author**: Cytognosis Foundation
> **Audience**: designers, engineers, writers
> **Tags**: `quick-reference`, `cytognosis-design-system-master`

# cytognosis-design-system-master — Quick Reference

> **One line**: Load this skill first for any Cytognosis visual design, styling, or branded writing task; it has the tokens and rules needed for 90% of work and routes to `cytognosis-branding` only when full v10 depth is needed.
> **Full doc**: [cytognosis-design-system-master.md](cytognosis-design-system-master.md)

---

## Key Concepts

| Term | Definition |
|------|-----------|
| **Identity triad** | The three primary brand colors: Violet (#8B3FC7), Azure (#3B7DD6), Indigo (#5145A8). |
| **Signature gradient** | `linear-gradient(135deg, #3B7DD6 0%, #8B3FC7 50%, #5145A8 100%)` — the Patient-to-Pioneer wash. |
| **Profile** | One of four use-case modes (Foundation, Clinical, Research, Lab) applied via `[data-profile="<name>"]` in CSS. |
| **Glassmorphism** | `rgba(30,41,59,0.4)` + `backdrop-filter: blur(12-16px)`. Used sparingly; never stack glass on glass. |
| **Revelation Arc** | Narrative structure: Mystery → Insight → Resolution. Applies to all Cytognosis content. |
| **Fluorophore palette** | Colors spectrally derived from biological fluorophores: DAPI, Alexa Fluor 488, GFP, etc. |

---

## Color Tokens

| Token | Hex | Use |
|-------|-----|-----|
| `--cg-violet-600` | `#8B3FC7` | Main brand color |
| `--cg-azure-600` | `#3B7DD6` | Patient, data input |
| `--cg-indigo-500` | `#5145A8` | Pioneer, AI outputs |
| `--cg-teal-600` | `#14A3A3` | Success, harmony |
| `--cg-coral-600` | `#F26355` | Warmth, hope |
| `--cg-magenta-600` | `#E0309E` | ATTENTION ONLY |
| `--bg-ink-deep` | `#0A0A14` | Darkest background |
| `--bg-rich-night` | `#1E1E32` | Default dark background |
| `--bg-pale-day` | `#F0F0F7` | Default light background |
| `--bg-clinical` | `#F5F5FA` | Clinical light variant |

Signature gradient: `linear-gradient(135deg, #3B7DD6 0%, #8B3FC7 50%, #5145A8 100%)`

---

## Typography Defaults

| Font | Token | Default use | Alternates |
|------|-------|-------------|-----------|
| Inter | `--font-display` | Display + body | General Sans, IBM Plex Sans |
| Newsreader | `--font-accent` | Accent / editorial | Source Serif Pro, Recursive |
| JetBrains Mono | `--font-code` | Code | Fira Code, Recursive Mono |
| Atkinson Hyperlegible | `--font-a11y` | Patient forms, low vision | Lexend (ADHD/dyslexia) |

---

## Profile Quick-Select

| Profile | Use for | Voice |
|---------|---------|-------|
| **Foundation** | cytognosis.org, decks, press | Visionary, hopeful |
| **Clinical** | Patient app, consumer | Calm, reassuring |
| **Research** | Cytoverse, dashboards | Precise, neutral |
| **Lab** | CLI, dev docs, terminal | Technical, playful |

Decision: investors/press → Foundation; patients → Clinical; scientists → Research; developers → Lab.

---

## Visual Rules (abbreviated)

| Rule | Value |
|------|-------|
| Min body text | 16px |
| Line height | 1.6 |
| Alignment | Left only (never justified) |
| Card radius | 16px |
| Button radius | 8px (pill: 9999px marketing only) |
| Input radius | 6px |
| Modal radius | 20px |
| Motion: fast | 150ms |
| Motion: base | 250ms |
| Motion: slow | 350ms |
| Animate only | `transform` and `opacity` |

---

## Voice Rules (abbreviated)

| Rule | Example |
|------|---------|
| No em dashes | Use commas or semicolons instead |
| No emoji | Use icons from the 48-icon set |
| No "patients" | Use "people", "individuals", or role name |
| No hype words | No "revolutionary", "cure", "breakthrough" |
| Oxford comma | "A, B, and C" |
| Active present | "We detect disease" (not "Disease is detected") |
| Title Case headings | Sentence case for UI labels |

---

## Commands / Syntax

| Action | Pattern |
|--------|---------|
| Apply profile in CSS | `[data-profile="foundation"] { ... }` |
| Inline signature gradient | `background: linear-gradient(135deg, #3B7DD6 0%, #8B3FC7 50%, #5145A8 100%)` |
| Inline glassmorphism | `background: rgba(30,41,59,0.4); backdrop-filter: blur(14px)` |
| Use icon sprite | `<use href="assets/icons/_bundle-line.svg#icon-name" />` |

---

## NEVER

- `#000000` or `#FFFFFF` (use ink-deep or pale-day)
- `#6366f1` (Tailwind Indigo)
- Em dashes in any output
- Magenta as identity color (attention only)
- Gradient at viewport scale
- Justified text or center-aligned body
- Drop shadows / glows on logo
- `prefers-reduced-motion` ignored

---

## See Also

- [Full documentation](cytognosis-design-system-master.md) — comprehensive reference + explanation
- [cytognosis-branding](../cytognosis-branding/cytognosis-branding.md) — full v10 depth (12 reference files)
- [cytognosis-template-master](../cytognosis-template-master/cytognosis-template-master.md) — interface app scaffolding
- [cytognosis-writer](../cytognosis-writer/cytognosis-writer.md) — grant and science narrative writing
