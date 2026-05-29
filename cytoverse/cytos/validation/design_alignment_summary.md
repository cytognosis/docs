# Design System Alignment Summary

> All three deliverables complete: Design review, branding repo update, CytoExplorer redesign.

## 1. Design System Review

Read and internalized the complete design system exported by Claude Design to `org/design/`:

| Document | Key Decisions |
|----------|--------------|
| [README.md](file:///home/mohammadi/repos/cytognosis/org/design/README.md) | Master source of truth: palette, typography, gradients, radii, motion, layout |
| [colors_and_type.css](file:///home/mohammadi/repos/cytognosis/org/design/colors_and_type.css) | 310-line canonical CSS with full 10-shade scales for all 6 fluorophore colors |
| [LOGO.md](file:///home/mohammadi/repos/cytognosis/org/design/LOGO.md) | Mark usage, clear space, don'ts, favicon spec |
| [IMAGERY.md](file:///home/mohammadi/repos/cytognosis/org/design/IMAGERY.md) | 5 image pillars, color grading rules, sourcing checklist |
| [ACCESSIBILITY.md](file:///home/mohammadi/repos/cytognosis/org/design/ACCESSIBILITY.md) | WCAG AAA contrast audit, focus ring spec, high-contrast override |
| [WRITING.md](file:///home/mohammadi/repos/cytognosis/org/design/WRITING.md) | 4 voice profiles (Foundation, Clinical, Research, Lab) |
| [Components.jsx](file:///home/mohammadi/repos/cytognosis/org/design/components/Components.jsx) | Profile-aware primitives: Button, Card, Modal, Badge, Table, Toast |
| `branding/references/01-12` | 12 section-specific reference docs for agent skill consumption |

### Critical Design Decisions Identified

- **Neutrals**: `#1a1a2e` (Deep Night) for sidebars, not `#0A0A14`. The abyss color is for flagship marketing hero surfaces only.
- **Identity triad**: Azure → Violet → Indigo (the "Patient to Pioneer" gradient), NOT the old Violet → Azure → Magenta.
- **Typography**: Newsreader replaces Source Serif Pro as the default accent. Fraunces and Urbanist are explicitly banned.
- **Shadows**: All shadows use `rgba(26,26,46,*)` (indigo-tinted), never pure black.
- **Badges**: Use 300-shade (daily-use tokens) for text on dark backgrounds, achieving AAA contrast.
- **Magenta**: Strict attention accent only, never part of the identity triad.
- **Radii**: Cards 16px, buttons 8px, inputs 6px, modals 20px, pills 9999px.

---

## 2. Branding Repo Update

**Branch**: `feat/design-system-v10` → pushed to [github.com/cytognosis/branding](https://github.com/cytognosis/branding/tree/feat/design-system-v10)

### Changes

render_diffs(file:///home/mohammadi/repos/cytognosis/org/branding/web/css/brand-variables.css)

**Files added/updated:**

| File | Change |
|------|--------|
| `web/css/brand-variables.css` | Full rewrite: 10-shade palette scales, named gradients, type scale, glass tokens, semantic elements |
| `web/css/cytognosis-tokens.css` | Canonical export from `design/colors_and_type.css` |
| `guidelines/02-12_*.md` | 12 v10 reference docs from design export |
| `guidelines/LOGO.md` | Mark usage spec |
| `guidelines/IMAGERY.md` | 5-pillar imagery guide |
| `guidelines/ACCESSIBILITY.md` | WCAG AAA audit |
| `guidelines/WRITING.md` | Voice per profile |

---

## 3. CytoExplorer Redesign

### Before → After

````carousel
![Before: Original CytoExplorer with custom palette](/home/mohammadi/.gemini/antigravity/brain/30e4c8ce-eb46-4ab7-b626-ef10bb527d7b/artifacts/cytoexplorer_preview.png)
<!-- slide -->
![After: Redesigned with canonical design system tokens](/home/mohammadi/.gemini/antigravity/brain/30e4c8ce-eb46-4ab7-b626-ef10bb527d7b/artifacts/cytoexplorer_redesign.png)
````

### Token Migration Summary

| Token Category | Before (custom) | After (canonical) |
|---------------|-----------------|-------------------|
| Page background | `#0A0A14` flat | `linear-gradient(180deg, #0a0a14, #13131f)` |
| Sidebar background | `#0F0F1C` | `#1a1a2e` (Deep Night) |
| Card background | `rgba(30,41,59,0.5)` | `rgba(30,30,50,0.50)` (glass-bg) |
| Card border | `rgba(120,120,160,0.15)` | `rgba(139,63,199,0.10)` (border-2) |
| Card radius | 12px | 16px (radius-xl) |
| Text primary | `#F8F8FC` | `var(--fg-1)` |
| Text secondary | `#B8B8CC` | `var(--fg-2)` → `#E0E0ED` |
| Text muted | `#7878A0` | `var(--fg-3)` → `#A6ADC8` |
| Border subtle | custom | `var(--border-1)` → `rgba(255,255,255,0.08)` |
| Shadows | pure black | `rgba(26,26,46,*)` (indigo-tinted) |
| Focus ring | violet 3px | Azure 300 `#9BC5F7` 3px + 2px offset |
| Badge text | 600-shade | 300-shade (AAA compliant) |
| Font import | Inter only | Inter + Newsreader + JetBrains Mono + Lexend + Atkinson |
| Type scale | arbitrary rem | Major Third 1.250 (`--text-h1` through `--text-caption`) |
| Spacing base | mixed | 8px grid (`--space-xs` through `--space-4xl`) |
| Motion | `250ms cubic-bezier(0.4,0,0.2,1)` | `--dur-base` + `--ease-out` tokens |
| Gradient | `135deg #8B3FC7→#5A95E8→#E0309E` | `--cg-gradient-signature` (Azure→Violet→Indigo) |

### Files Modified

| File | Changes |
|------|---------|
| [globals.css](file:///home/mohammadi/repos/cytognosis/org/cytoexplorer/src/styles/globals.css) | Complete rewrite using canonical design tokens |
| [AppShell.css](file:///home/mohammadi/repos/cytognosis/org/cytoexplorer/src/components/layout/AppShell.css) | Glassmorphic header, proper focus states |
| [Sidebar.css](file:///home/mohammadi/repos/cytognosis/org/cytoexplorer/src/components/layout/Sidebar.css) | Deep Night bg, canonical fg/border tokens |
| [SearchBar.css](file:///home/mohammadi/repos/cytognosis/org/cytoexplorer/src/components/layout/SearchBar.css) | Azure-300 focus, 1.5px border, 6px input radius |
| [AssetCard.css](file:///home/mohammadi/repos/cytognosis/org/cytoexplorer/src/components/assets/AssetCard.css) | Glass cards, 16px radius, indigo shadows, AAA badges |
| [ExplorePage.css](file:///home/mohammadi/repos/cytognosis/org/cytoexplorer/src/pages/ExplorePage.css) | 1280px max-width, pill chips, tabular-nums, focus visible |
