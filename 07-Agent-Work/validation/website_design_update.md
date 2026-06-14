# Website Design System v10 Update

> All CSS and HTML files updated to canonical Design System v1.0.0 tokens.

## Preview

````carousel
![Hero section with canonical design tokens](/home/mohammadi/.gemini/antigravity/brain/2ce2367d-8f4a-49e8-91a6-b20d0c7b4c99/artifacts/website_hero_redesign.png)
<!-- slide -->
![Technology pillars with glassmorphic cards](/home/mohammadi/.gemini/antigravity/brain/2ce2367d-8f4a-49e8-91a6-b20d0c7b4c99/artifacts/website_tech_redesign.png)
````

## Changes Summary

### 1. brand-variables.css (full replacement)

Replaced the old 184-line file with the canonical 386-line v10 export from `branding/web/css/brand-variables.css`. Now includes:

| Token Category | What's New |
|---------------|-----------|
| Palette | Full 10-shade scales for all 6 fluorophore colors |
| Neutrals | Indigo-tinted neutral scale (`#1a1a2e` Deep Night through `#F8F8FC` Ghost Day) |
| Gradients | 5 named gradients + page gradient |
| Typography | Newsreader accent, Major Third 1.250 type scale, font aliases |
| Shadows | Indigo-tinted `rgba(26,26,46,*)`, glow variants |
| Glass | `rgba(30,30,50,0.50)` + `blur(12px)` |
| Semantic | `--fg-1` through `--fg-4`, `--bg-1` through `--bg-4`, `--border-1/2/focus` |
| Light theme | Full `@media (prefers-color-scheme: light)` overrides |

### 2. styles.css (token migration)

| Before | After |
|--------|-------|
| `--primary-dark: #1e1e32` | `--primary-dark: #1a1a2e` (Deep Night) |
| `--glass-bg: rgba(30,41,59,0.4)` | `rgba(30,30,50,0.50)` (canonical) |
| `--glass-blur: blur(16px)` | `blur(12px)` (canonical) |
| `--shadow: rgba(0,0,0,*)` | `rgba(26,26,46,*)` (indigo-tinted) |
| `--gradient-bg: inline gradient` | `var(--cg-gradient-signature)` |
| `font-family: "Inter", ...` | `var(--font-body)` / `var(--font-display)` |
| `background-color: var(--bg-abyss)` | `var(--cg-gradient-page)` with `fixed` attachment |
| `Roboto`, `Montserrat` refs | `var(--font-body)` / `var(--font-display)` |
| Header: `rgba(10,10,20,0.8)` | `rgba(26,26,46,0.85)` (Deep Night glass) |
| Footer: `var(--primary-dark)` | `var(--cg-neutral-950, #1a1a2e)` |

### 3. base.css (token migration)

- Replaced all `--dawn-*` / `--dusk-*` Catppuccin references with canonical `--fg-*`, `--bg-*`, `--border-*` tokens
- Removed the entire `@media (prefers-color-scheme: dark)` block (dark is now the default; brand-variables.css handles light theme)
- Focus rings now use Azure 300 (`#9BC5F7`)

### 4. index.html

- Google Fonts: Source Serif Pro → Newsreader + JetBrains Mono + Lexend + Atkinson Hyperlegible
- Body background: `var(--cg-gradient-page)` with `background-attachment: fixed`
- "Healthcare Revolution" → "Healthcare Transformation" (banned word)
- All inline shadows: `rgba(0,0,0,*)` → `rgba(26,26,46,*)` (indigo-tinted)
- Card radii: hardcoded → `var(--radius-2xl, 20px)`
- Cal.com brand color: `#4361EE` → `#8B3FC7` (Violet)

### 5. extended-styles.css

- All `rgba(67,97,238,*)` (non-brand #4361EE) → `rgba(59,125,214,*)` (Azure)
- All `rgba(157,132,183,*)` (non-brand) → `rgba(139,63,199,*)` (Violet)
- All pure-black box shadows → indigo-tinted
- Dropdown background: `var(--primary-dark)` → `var(--cg-neutral-950, #1a1a2e)`
- Header: glassmorphic with `backdrop-filter` and canonical border token
- Roboto → `var(--font-body)`

### 6. All sub-pages (16 HTML files)

- Batch replaced `Source+Serif+Pro` font import with Newsreader + full canonical font stack
