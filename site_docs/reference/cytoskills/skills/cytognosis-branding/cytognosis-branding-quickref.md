> **Status**: Active
> **Date**: 2026-06-14
> **Author**: Cytognosis Foundation
> **Audience**: designers, engineers, brand reviewers
> **Tags**: `quick-reference`, `cytognosis-branding`

# cytognosis-branding — Quick Reference

> **One line**: Deep-content home for the Cytognosis v10 brand system (12 reference files); load `cytognosis-design-system-master` for routine tasks and only load this skill for full shade scales, every icon spec, complete accessibility audit, or the full template library.
> **Full doc**: [cytognosis-branding.md](cytognosis-branding.md)

---

## Key Concepts

| Term | Definition |
|------|-----------|
| **v10** | Current major version of the Cytognosis brand system. All 12 reference files are v10. |
| **Identity triad** | The three primary brand colors: Violet, Azure, Indigo. Derived from fluorophore emission wavelengths. |
| **Fluorophore palette** | Brand colors named after and spectrally derived from biological fluorophores (DAPI, Alexa Fluor 488, etc.). |
| **Revelation Arc** | Narrative structure for all Cytognosis content: Mystery → Insight → Resolution. |
| **CVD safety** | Color-vision-deficiency safety; documented in `04_color_system.md` for every palette color. |
| **Profile** | Four use-case modes (Foundation, Clinical, Research, Lab) that adjust palette, typography, and voice. |

---

## The 12 Reference Files

| File | Load When |
|------|----------|
| `references/01_brand_foundation.md` | Full mission, identity, narrative architecture |
| `references/02_voice_and_tone.md` | Full voice rules, audience messaging, do/don't |
| `references/03_logo.md` | Full logo placement matrix, every lockup |
| `references/04_color_system.md` | Full shade scales, CVD safety, named gradients |
| `references/05_typography.md` | Full type families, scale, all weights |
| `references/06_iconography.md` | Full 48-icon spec, color semantics, gap-filling rules |
| `references/07_imagery.md` | Photography tone, treatment, sourcing checklist, shot list |
| `references/08_motion.md` | All durations, easings, motion patterns, reduced-motion |
| `references/09_layout.md` | Full 12-column grid, full spacing scale, glassmorphism rules |
| `references/10_templates.md` | Deck (12 layouts), one-pager, email signature, social, print |
| `references/11_accessibility.md` | Full WCAG 2.2 audit, contrast matrices, neurodiversity |
| `references/12_dataviz.md` | Full chart palettes, pattern fills for colorblind contexts |

---

## When to Load This vs. design-system-master

| Request | Load |
|---------|------|
| "What color is the Azure token?" | `cytognosis-design-system-master` |
| "Give me every shade in the Azure scale with hex + CVD alternatives" | `cytognosis-branding` → `04_color_system.md` |
| "Apply the signature gradient to this hero" | `cytognosis-design-system-master` |
| "Every named gradient with WCAG AA status" | `cytognosis-branding` → `04_color_system.md` + `11_accessibility.md` |
| "Write copy in the Foundation voice" | `cytognosis-design-system-master` |
| "Full voice rules including every do/don't pair" | `cytognosis-branding` → `02_voice_and_tone.md` |
| "Place the logo on a dark background" | `cytognosis-design-system-master` |
| "Complete logo placement matrix for every background type and size" | `cytognosis-branding` → `03_logo.md` |

---

## Key Tokens (Quick Version)

| Token | Hex | Meaning |
|-------|-----|---------|
| `--cg-violet-600` | `#8B3FC7` | Main brand (DAPI, DNA stain, 461nm) |
| `--cg-azure-600` | `#3B7DD6` | The Patient, data input (Alexa Fluor 488) |
| `--cg-indigo-500` | `#5145A8` | The Pioneer, AI outputs (UV excitation, 358nm) |
| `--cg-teal-600` | `#14A3A3` | Success, biological harmony (GFP, 509nm) |
| `--cg-coral-600` | `#F26355` | Human warmth, hope (MitoTracker, 576nm) |
| `--cg-magenta-600` | `#E0309E` | ATTENTION ACCENT ONLY (Rhodamine, 565nm) |
| `--bg-rich-night` | `#1E1E32` | Default dark background |
| `--bg-pale-day` | `#F0F0F7` | Default light background |

---

## NEVER (Hard Rules)

| Forbidden | Reason |
|-----------|--------|
| `#000000` or `#FFFFFF` | Use `#0A0A14` (darkest) or `#F0F0F7` (lightest) |
| `#6366f1` (Tailwind Indigo) | Wrong brand; use `#8B3FC7` |
| Em dashes | Use commas, semicolons, or restructure |
| "Revolutionary", "cure", "breakthrough" | Hype words; find a sharper word |
| Gradient backgrounds at viewport scale | Gradients are accent only |
| Drop shadows on logo | No bevels, no glows, no outlines on the mark |

---

## Operational Kits

| Path | Contents |
|------|---------|
| `templates/deck/` | 12-layout reference deck (light + dark); copy this for new decks |
| `templates/email-signature.html` | Full + compact variants; email-client safe |

---

## Error Quick-Fix

| Error / Symptom | Fix |
|-----------------|-----|
| Loaded this skill for a routine color token lookup | Switch to `cytognosis-design-system-master` (cheatsheet is faster) |
| Loaded two reference files in the same response | Split into separate responses; load one file at a time |
| Gradient applied at full viewport | Restrict gradient to hero washes, primary CTA fills, or accent elements only |

---

## See Also

- [Full documentation](cytognosis-branding.md) — comprehensive reference + explanation
- [cytognosis-design-system-master](../cytognosis-design-system-master/cytognosis-design-system-master.md) — operational entry point for routine design
- [cytognosis-template-master](../cytognosis-template-master/cytognosis-template-master.md) — interface template scaffolding
- [cytognosis-writer](../cytognosis-writer/cytognosis-writer.md) — voice rules for grant and scientific writing
