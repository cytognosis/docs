# Raw: Artifact Pack Spec (VS Code Theme Recovery + Post-Finalization Pack)

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: designers, stakeholders
> **Tags**: `design`, `design-system`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

Working research file. Covers three things: (1) full recovery of the prior VS Code/Geany/Starship theme work from the branding repo's git history, since it no longer exists in the checked-out tree, (2) an inventory of what artifact work already exists versus what's missing, and (3) the full spec for the post-finalization artifact pack to be generated in Claude Design once v11 is frozen.

**If you only read one thing:** the old "Cytognosis Dusk" VS Code/Geany/Starship dark theme already uses the exact same hex values that are now v11's 300-shade "therapeutic" tokens, so it is highly reusable. It has two real defects to fix (unmapped leftover Catppuccin hexes for foreground text and for success/warning/error) and no light or calm variant exists yet for VS Code or Geany (Starship already has a light "dawn" palette drafted). Everything else in the artifact pack (meeting backgrounds, Slack, most social) is net new; only favicons, app icons, OG image, avatar, LinkedIn company banner, slide cover/divider, email signature, and a one-pager exist today.

---

## 1. VS Code theme precedent recovery

### 1.1 Where this lives

The theme files (`themes/vscode/`, `themes/geany/`, `themes/starship/`) **do not exist in the current branding repo working tree.** Commit `130dee7` ("Replace branding repo with CytoStyle package") replaced the entire repo with a React theming package (`src/providers/ThemeProvider.tsx`, `createCytoStyleTheme.ts`, etc.). The old theme files are recoverable **only from git history**, read-only, via:

```
git show <commit>:<path>
```

All commit references below are from `branding` repo history (`git log --oneline --all`), read-only, no checkout performed.

### 1.2 Timeline (oldest to newest)

| Commit | Date-order | What happened to the themes |
|---|---|---|
| `c360e57` | oldest | "add optimized IDE settings for VSCode, Cursor, and Windsurf". First appearance of `themes/vscode/settings.json`, `extensions.json`, `keybindings.json`, `launch.json`, plus `themes/cursor/settings.json`, `themes/windsurf/settings.json`, and four **third-party** Starship presets (catppuccin-powerline, gruvbox-rainbow, tokyo-night, nerd-font-symbols) alongside the Cytognosis one. |
| `526fa28` | ↓ | "update Antigravity/VSCode settings and extensions for 2026". Same file set, settings tweaks. |
| `9d39813` | ↓ | "rewrite Cytognosis Dusk theme with official brand colors". Despite the message, the geany/starship files at this commit **still carry the old Catppuccin Macchiato palette** (rosewater, flamingo, mauve, etc.); this commit's rewrite appears to have landed the VS Code JSON but not yet geany/starship. |
| `ceba750` | ↓ | "consolidate themes and remove stale settings/configs". This is the commit that actually swapped geany and starship from Catppuccin Macchiato to the brand fluorescence-microscopy palette (commit message says so explicitly: "replaced Catppuccin Macchiato → fluorescence microscopy palette"). Also **removed** `settings.json`, `extensions.json`, `keybindings.json`, `launch.json`, and the `cursor/`/`windsurf/` folders from the branding repo entirely, relocating them to `cytognosis/agents/configs/editors/{vscode,cursor,windsurf}/` (a different repo, not in scope for this session). Also dropped the four third-party Starship presets as "not our theme." From this commit on, `branding/themes/` contains **only** the four Cytognosis-authored files: `README.md`, `vscode/cytognosis_vscode_theme.json`, `starship/cytognosis_starship_preset.toml`, `geany/cytognosis_geany_theme.conf`. |
| `abc9741` | ↓ | "add package.json for Cytognosis Dusk theme extension". Added `themes/vscode/package.json` so the theme installs as a VS Code/Antigravity/Positron extension. |
| `9559138` | newest of this group | "finalize therapeutic design guidelines and VSCode theme integration". Despite the commit message, diff stat shows it only touched `themes/vscode/package.json` (6 lines) plus guideline docs; the theme color files were unchanged from `ceba750`/`abc9741`. **This is the final, most-complete state of the theme work** and is the version recorded below. |
| `130dee7` (HEAD) | current | `themes/` directory removed entirely; repo replaced with the CytoStyle React package. |

**Recovery command used for everything below:** `git show 9559138:themes/vscode/cytognosis_vscode_theme.json` (and equivalent paths for starship/geany/package.json).

### 1.3 VS Code: "Cytognosis Dusk" (dark, only variant that ever existed)

Extension metadata (`themes/vscode/package.json`, verbatim):

```json
{
  "name": "cytognosis-dusk-theme",
  "displayName": "Cytognosis Dusk",
  "description": "A therapeutic dark theme using Cytognosis brand fluorescence colors, pastel tokens for neurodiversity support",
  "version": "4.0.0",
  "publisher": "cytognosis",
  "engines": { "vscode": "^1.60.0" },
  "categories": ["Themes"],
  "contributes": {
    "themes": [
      { "label": "Cytognosis Dusk", "uiTheme": "vs-dark", "path": "./cytognosis_vscode_theme.json" }
    ]
  }
}
```

(Note: the original file uses an em dash in the description; reproduced above with a comma per house style. Original theme JSON: `"type": "dark"`, `"semanticHighlighting": true`.)

**Curated UI color mapping** (full set is ~250 keys; these are the ones the task asked for by name, editor bg, sidebar, accents; full JSON recoverable via the git command above):

| VS Code key | Hex | Maps to v11 token | Match |
|---|---|---|---|
| `editor.background` | `#262640` | `--cg-neutral-800` | exact |
| `editor.foreground` / `foreground` | `#cdd6f4` | none | **drift, see 1.6** |
| `activityBar.background`, `sideBar.background`, `statusBar.background`, `titleBar.activeBackground` | `#1a1a2e` | `--cg-neutral-950` | exact |
| `editorWidget.background`, `dropdown.background`, `input.background`, `panel.background` | `#1e1e32` | `--cg-neutral-900` | exact |
| `list.activeSelectionBackground`, `input.border`, `dropdown.border` | `#3d3d5c` | `--cg-neutral-600` | exact |
| `editorLineNumber.foreground` | `#50506e` | `--cg-neutral-500` | exact |
| `tab.inactiveForeground`, `breadcrumb.foreground` | `#8888a8` | `--fg-3` | exact |
| `editorCursor.foreground` | `#F9A5DD` | `--cg-magenta-300` | exact |
| `button.background`, `activityBar.activeBorder`, `editorLineNumber.activeForeground` | `#CAA0F0` | `--cg-violet-300` / `--cg-violet-soft` | exact |
| `focusBorder`, `activityBarBadge.background` | `#9BC5F7` | `--cg-azure-300` / `--cg-azure-soft` | exact |
| `editorError.foreground`, `gitDecoration.deletedResourceForeground`, `statusBarItem.errorBackground` | `#f38ba8` | none (v11 `--cg-error` is `#EF4444`) | **drift, see 1.6** |
| `editorWarning.foreground`, `gitDecoration.modifiedResourceForeground` | `#f9e2af` | none (v11 `--cg-warning` is `#F59E0B`) | **drift, see 1.6** |
| `editorGutter.addedBackground`, `gitDecoration.addedResourceForeground` | `#a6e3a1` | none (v11 `--cg-success` is `#10B981`) | **drift, see 1.6** |
| `editorInfo.foreground` | `#7FE8E8` | `--cg-teal-300` / `--cg-teal-soft` | exact |

**Terminal ANSI 16** (full set, this is exactly what the task asked for):

| ANSI role | Hex | Maps to v11 token |
|---|---|---|
| ansiBlack | `#3d3d5c` | `--cg-neutral-600` |
| ansiBrightBlack | `#50506e` | `--cg-neutral-500` |
| ansiRed / ansiBrightRed | `#f38ba8` (both, no distinct bright) | none, drift |
| ansiGreen / ansiBrightGreen | `#a6e3a1` (both, no distinct bright) | none, drift |
| ansiYellow / ansiBrightYellow | `#f9e2af` (both, no distinct bright) | none, drift |
| ansiBlue | `#9BC5F7` | `--cg-azure-300` |
| ansiBrightBlue | `#BCDCFB` | `--cg-azure-200` |
| ansiMagenta | `#CAA0F0` | `--cg-violet-300` (mapped to violet, not magenta, intentional) |
| ansiBrightMagenta | `#F9A5DD` | `--cg-magenta-300` |
| ansiCyan | `#7FE8E8` | `--cg-teal-300` |
| ansiBrightCyan | `#94e2d5` | none, off-scale Catppuccin leftover |
| ansiWhite | `#C4C4D8` | `--cg-day-300` |
| ansiBrightWhite | `#F0F0F7` | `--cg-day-100` |

**`tokenColors` (syntax highlighting scopes), verbatim, this is directly reusable as-is:**

| Rule name | Scopes | Foreground | Notes |
|---|---|---|---|
| Comments | `comment`, `punctuation.definition.comment` | `#8888a8` (`--fg-3`) | italic |
| Strings | `string`, `string.quoted`, `string.template` | `#a6e3a1` | drift, see 1.6 |
| Numbers | `constant.numeric` | `#FFBFB5` (`--cg-coral-300`) | |
| Keywords | `keyword`, `keyword.control`, `keyword.operator`, `storage.type`, `storage.modifier` | `#9BC5F7` (`--cg-azure-300`) | |
| Functions | `entity.name.function`, `meta.function-call`, `support.function` | `#CAA0F0` (`--cg-violet-300`) | |
| Variables | `variable`, `meta.definition.variable.name`, `support.variable` | `#F9A5DD` (`--cg-magenta-300`) | |
| Classes & Types | `entity.name.type`, `entity.name.class`, `support.class`, `support.type` | `#ADA0E8` (`--cg-indigo-300`) | |
| Constants | `constant`, `constant.language`, `support.constant` | `#FFBFB5` (`--cg-coral-300`) | |
| Tags (HTML/XML) | `entity.name.tag`, `meta.tag.sgml` | `#9BC5F7` (`--cg-azure-300`) | |
| Attributes | `entity.other.attribute-name` | `#ADA0E8` (`--cg-indigo-300`) | italic |
| JSON Keys | `support.type.property-name.json` | `#7FE8E8` (`--cg-teal-300`) | |
| Markdown Headers | `heading.1..6.markdown` | `#9BC5F7` | bold |
| Markdown Bold | `markup.bold` | `#FFBFB5` | bold |
| Markdown Italic | `markup.italic` | `#F9A5DD` | italic |
| Markdown Links | `markup.underline.link` | `#7FE8E8` | underline |
| Markdown Code | `markup.inline.raw`, `markup.fenced_code.block` | `#a6e3a1` | drift |
| Operators & Punctuation | `keyword.operator`, `punctuation` | `#7FE8E8` | |
| Decorators & Annotations | `meta.decorator`, `punctuation.decorator` | `#f9e2af` | italic, drift |
| Invalid | `invalid`, `invalid.illegal` | `#f38ba8` | drift |
| Deprecated | `invalid.deprecated` | `#50506e` | strikethrough |

**`semanticTokenColors` (verbatim):** `variable` #F9A5DD, `variable.declaration` #CAA0F0, `variable.readonly` #9BC5F7, `parameter` #FFBFB5, `function`/`method` #CAA0F0, `property` #7FE8E8, `enumMember`/`event` #FFBFB5, `type`/`class`/`interface`/`namespace` #ADA0E8, `typeParameter`/`regexp` #F9A5DD, `comment` #8888a8 italic, `string` #a6e3a1, `keyword` #9BC5F7, `number` #FFBFB5, `operator` #7FE8E8. This structure (generic scope-based, not per-language) covers Python/JS/TS/Go/Rust/etc via their standard TextMate grammars without per-language duplication; keep this approach for the redo.

### 1.4 Starship preset: dark AND light already exist (verbatim palettes)

This is the best-preserved precedent. The preset (`themes/starship/cytognosis_starship_preset.toml`, "based on official brand fluorescence microscopy color system v9.0") ships **two full palettes**, dark active by default, light fully written but commented out:

**`[palettes.cytognosis_dusk]` (dark, default):**
```
bg_darkest = '#1a1a2e'   # --cg-neutral-950
bg_dark    = '#1e1e32'   # --cg-neutral-900
bg_mid     = '#262640'   # --cg-neutral-800
bg_light   = '#303050'   # --cg-neutral-700
bg_muted   = '#3d3d5c'   # --cg-neutral-600
text_dim   = '#50506e'   # --cg-neutral-500
text_muted = '#8888a8'   # --fg-3
text_sub   = '#C4C4D8'   # --cg-day-300
text       = '#cdd6f4'   # NOT a v11 token, drift
text_bright= '#F0F0F7'   # --cg-day-100
violet='#CAA0F0' azure='#9BC5F7' magenta='#F9A5DD' indigo='#ADA0E8'   # all --cg-*-300
coral='#FFBFB5' teal='#7FE8E8'                                        # both --cg-*-300
violet_light='#DFC0F7' azure_light='#BCDCFB' indigo_light='#CFC5F3'  # all --cg-*-200 exact
magenta_light='#FCC9EC'   # off-scale, no v11 magenta-200 exists
success='#a6e3a1' warning='#f9e2af' error='#f38ba8'   # NOT v11 semantic tokens, drift
```

**`[palettes.cytognosis_dawn]` (light, currently unused, commented out):**
```
bg_darkest='#F8F8FC' bg_dark='#F0F0F7' bg_mid='#E0E0ED' bg_light='#C4C4D8' bg_muted='#A8A8C0'
# = --cg-day-50 / 100 / 200 / 300 / 400, all EXACT matches
text_dim='#3E3E5C' text_muted='#2E2E4C' text_sub='#25253D' text='#1C1C2E' text_bright='#0A0A14'
# text_bright matches --cg-abyss exactly; the rest are a custom ramp, not named v11 tokens
violet='#7230A3' azure='#2761A3' magenta='#C02380' indigo='#3D3485'
# = --cg-violet-700 / --cg-azure-700 / --cg-magenta-700 / --cg-indigo-700, all EXACT
coral='#D94A3D' teal='#0D7C7C'   # = --cg-coral-700 / --cg-teal-700, EXACT
success='#10B981' warning='#F59E0B' error='#EF4444'   # EXACT match to v11 semantic tokens
```

**Important asymmetry to fix in the redo:** the dark palette's semantic colors (success/warning/error) are leftover Catppuccin pastels with no brand mapping, but the light palette's semantic colors are the *real* v11 semantic tokens used as-is (fully saturated, not softened). Neither is wrong on its own, but they're inconsistent with each other, one should win as the pattern, and it should probably be a softened derivative in both cases to preserve the "therapeutic pastel" premise.

Also verbatim and reusable as-is: the prompt format (OS icon, username, hostname, directory, git branch/status, node/rust/go/python/docker version, time, all segment-styled), battery display thresholds, `cmd_duration`, and two custom Cytognosis modules (`custom.cytognosis_env`, `custom.cytognosis_model`) that shell out to `$CYTOGNOSIS_ENV`/`$CYTOGNOSIS_MODEL` env vars. None of this needs redesign, only the palette values need the drift fix.

### 1.5 Geany: "Cytognosis Dusk" (dark only, deep per-language work)

Same named-color structure as the VS Code/Starship dark palette (`bg_darkest` #1a1a2e through `bg_elevated` #3d3d5c, `text`/`text_muted`/`text_bright`, brand 300-shades, same `text=#cdd6f4` and `success`/`warning`/`error` drift as above). Version `4.0`, "Official brand theme using fluorescence microscopy color system v9.0."

What's valuable here and worth carrying forward largely unchanged: **per-language syntax stanzas** for Python, JavaScript, HTML, CSS, PHP, and C/C++, plus Markdown and Diff, each with 10 to 25 mapped roles (identifiers, strings, numbers, keywords, comments, operators, tags/attributes for markup languages, decorators). Example (Python): `python_classname=indigo_light`, `python_defname=violet`, `python_decorator=warning`, `python_string=success`. This is the single richest piece of "syntax scopes per language family" precedent across all three tools and should anchor the redo's language coverage (Python first, since that's the dominant Cytognosis language per dev-standards). No light Geany variant exists; net new.

The file also ends with three accessibility notes worth preserving verbatim: line spacing 1.8x, minimum font size 14px, recommended fonts JetBrains Mono / Recursive Mono / Fira Code (JetBrains Mono is already the v11 `--font-code` token, so this is already brand-aligned).

### 1.6 Drift audit: what does NOT map to a v11 token

Four concrete defects, present identically across VS Code, Starship (dark palette only), and Geany:

| Drift item | Current hex | Problem | Fix direction |
|---|---|---|---|
| Primary foreground/`text` | `#cdd6f4` | Literal leftover Catppuccin value, was never swapped in the "rewrite with brand colors" pass | Replace with `--fg-1` (`#E8E8F4`), the v11 dark-theme primary-text token |
| `success` | `#a6e3a1` | Not derived from `--cg-success` (`#10B981`) at all | Derive a softened/pastel version of `--cg-success`, don't reuse the raw Catppuccin hex |
| `warning` | `#f9e2af` | Not derived from `--cg-warning` (`#F59E0B`) | Same approach, soften `--cg-warning` |
| `error` | `#f38ba8` | Not derived from `--cg-error` (`#EF4444`) | Same approach, soften `--cg-error` |
| `magenta_light` (hover shade) | `#FCC9EC` | No `--cg-magenta-200` exists in v11 to match against | Either mint a magenta-200 in the token system, or drop this hover shade and reuse `--cg-magenta-300` at reduced opacity |
| `ansiBrightCyan` | `#94e2d5` | Off-scale Catppuccin teal, doesn't match `--cg-teal-300` or `--cg-teal-400` | Snap to `--cg-teal-400` (`#48D8D8`) as the "bright" step above `--cg-teal-300` |

Everything else (all bg neutrals, all six brand 300-shade accents, the three 200-shade "light" accents, and the entire light "dawn" palette) is an **exact, already-correct match** to current v11 tokens. This is a small, well-scoped fix list, not a rebuild.

### 1.7 Keep vs. redo verdict

| Keep as-is (just relabel to explicit v11 token names) | Fix (drift, listed above) | Redo/net new |
|---|---|---|
| All bg neutral steps, all six brand 300/700-shade accents, gradient logic, Starship module layout, Geany per-language stanzas, `tokenColors`/`semanticTokenColors` structure in VS Code | Foreground text hex, success/warning/error hex (all three tools), magenta-light hover, ansiBrightCyan | Light VS Code theme ("Cytognosis Day," see 3a), calm/low-contrast VS Code variant, light Geany variant, harmonized bg-label naming across the three tools (geany says `bg_base`/`bg_surface`/`bg_elevated`, starship says `bg_mid`/`bg_light`/`bg_muted` for the identical three hex values, pick one vocabulary) |

---

## 2. Existing artifact inventory

### 2.1 What already exists (v11.1.0 bundle, confirmed on disk)

Location: `design-system-merge-2026-07/01_extracted/v11_1/assets/logos/` and `/templates/`.

| Artifact | File(s) | Spec (per `LOGO.md`/`CHANGELOG.md`) |
|---|---|---|
| Favicon | `favicon.svg` (root), `favicon-16/32/48.png` | SVG source + PNG triplet |
| Apple touch icon | `apple-touch-icon.png` | 180px, mark on `#0A0A14` |
| Android Chrome icons | `android-chrome-192.png`, `android-chrome-512.png` | |
| App icon master + exports | `app-icon-master-1024.svg`, `app-icon-ios-1024.png`, `app-icon-macos-1024.png`, `app-icon-android-512.png` | squircle-safe padding, mark at ~62% |
| OG image | `og-image.png` | 1200x630, light wordmark on `#0A0A14`, subtle signature-gradient wash |
| Profile avatar | `avatar.png` | 1:1, icon mark on `#0A0A14`, 15% padding |
| LinkedIn company banner | `linkedin-banner.png` | 1584x396, white wordmark on `#0A0A14`, mark ~50% of canvas height |
| Slide cover | `slide-cover.svg` | 1920x1080, signature gradient plus mark and wordmark |
| Slide divider | `slide-divider.svg` | 1920x1080, ink surface, mark, gradient rule |
| Social cards template | `templates/social-cards.html` | HTML preview, 3 OG variants (dark/paper/violet-accent) at 1200x630 and 3 square variants at 1080x1080 (headline metric, quote card, announcement) |
| Email signature | `templates/email-signature.html` | Full + compact variants, table-based, system fonts only |
| One-pager | `templates/one-pager.html` | US Letter (8.5x11in), research-brief layout; masthead (logo + doc meta, 1px ink-deep rule) and footer (violet dot + org name, contact, page number) function as a de facto letterhead pattern, though it is not a standalone blank letterhead |
| Deck template | `templates/deck.html`, `templates/deck-stage.js` | |
| VS Code theme, dark only | git history only (`branding` repo, see section 1) | not in current v11_1 bundle at all |
| Geany theme, dark only | git history only | same |
| Starship preset, dark + light both drafted | git history only | same, light palette unused but complete |

That is **16 existing artifact categories** (13 present in the current v11.1 bundle on disk, plus 3 recoverable only from branding-repo git history).

### 2.2 Sweep methodology and negative results

Searched `Projects/Science and Platform` and `Projects/Website` (excluding `node_modules` and `uploads`) for two keyword passes: `zoom|meeting background|wallpaper|slack|linkedin|social` and a supplementary pass for `github|youtube|bluesky|emoji|channel art|letterhead|favicon|app icon`. Every hit resolved to one of: the v11_1 bundle files already listed above, generic design-system reference docs that mention a keyword in passing (e.g., a favicon TODO note inside a markdown reference doc, not a dedicated asset file), or website HTML pages with a plain favicon `<link>` tag. **No dedicated file for any of the following was found anywhere in either tree:**

- Meeting/Zoom/Google Meet virtual backgrounds
- A LinkedIn personal-profile banner distinct from the company banner
- LinkedIn-native post/carousel sizes (1200x1200, 1080x1350)
- A LinkedIn event cover
- Slack workspace icon, channel header art, or custom emoji
- X/Bluesky banner art (avatar is covered by the existing generic `avatar.png`)
- YouTube channel art
- A GitHub org avatar sized for GitHub, or a GitHub-spec (1280x640) social preview image
- An email header banner (distinct from the email signature, which does exist)
- A standalone blank letterhead file

That is **17 missing/net-new deliverables** (counting the VS Code/Geany light variants and the VS Code calm variant as three of the 17, since Starship's light palette already exists and just needs the drift fix plus a rename).

---

## 3. Artifact pack spec

Every dimension, format, and token below assumes v11 is frozen at the point of generation. Token names refer to `tokens/colors.css` and `tokens/fonts.css` in `design-system-merge-2026-07/01_extracted/v11_1/`.

### 3a. VS Code theme (+ Starship + optional Geany)

| Variant | Base tokens | Foreground | Accent logic | Notes |
|---|---|---|---|---|
| **Cytognosis Night** (dark, default) | `--cg-neutral-950/900/800/700/600` for the bg ramp (chrome/widgets/editor/elevated/borders) | `--fg-1` (`#E8E8F4`), fixes the old `#cdd6f4` drift | `--cg-violet-300` functions/keywords-accent, `--cg-azure-300` keywords/links, `--cg-magenta-300` variables/cursor, `--cg-indigo-300` types, `--cg-coral-300` numbers/params, `--cg-teal-300` operators | Direct continuation of "Cytognosis Dusk," same structure, drift fixed per 1.6 |
| **Cytognosis Day** (light, warm lp palette) | `--cg-lp-bg` (`#F4F2EF`) or `--cg-lp-surface` (`#FFFFFF`) for chrome, `--cg-lp-bg-section` (`#ECE9E4`) sidebar, `--cg-lp-bg-soft` (`#FAF8F2`) widgets | `--cg-lp-text` (`#2E3036`), muted `--cg-lp-muted` (`#6F7178`) | `--cg-lp-violet` (`#6E5BD1`) as primary accent; azure/indigo/coral/teal/magenta 700-shades exactly as already validated in the old Starship "dawn" palette | Deliberately warmer than the old "dawn" (which used cool `--cg-day-*` neutrals); this is the one place the new spec diverges from straight precedent reuse, matching the warmer landing-page aesthetic instead |
| **Cytognosis Calm** (low-contrast) | `--cg-neutral-700` as base (one step lighter than Night, less "hole"-like) | `--fg-2` (`#C0C0D8`) instead of `--fg-1`, softer | 200-shade accents instead of 300-shade (`--cg-violet-200`, `--cg-azure-200`, etc.), single muted bracket-highlight color (no rainbow), bright-* ANSI collapsed to match base ANSI | Net new. For sensory-sensitive or end-of-long-session use; deliberately less vivid than Night, not simply Night at lower opacity |

**Terminal ANSI 16:** reuse the Night table in 1.3 verbatim (fixing the two drift rows: red/green/yellow families should derive from softened `--cg-error`/`--cg-success`/`--cg-warning`, not raw Catppuccin hex; ansiBrightCyan snaps to `--cg-teal-400`). Day derives its ANSI 16 from the 700-shade accents plus warm neutrals. Calm derives from 200-shade accents with bright-* collapsed to base.

**Syntax scopes:** keep the existing generic TextMate `tokenColors` structure from 1.3 verbatim (it already covers all language families through standard grammars); add semantic-token overrides for Python and TypeScript specifically, since those are Cytognosis's primary languages (per `dev-standards`), reusing the existing `semanticTokenColors` block unchanged.

**Starship:** rename `cytognosis_dusk` to `cytognosis_night` and `cytognosis_dawn` to `cytognosis_day` (re-deriving `bg_*`/`text_*` under Day to the warm `--cg-lp-*` values rather than cool `--cg-day-*`, per the Day spec above), fix the dark palette's semantic drift, and add a third `cytognosis_calm` palette following the same desaturation logic as VS Code Calm. Everything else (format string, modules, custom Cytognosis env/model modules) carries forward unchanged.

**Geany:** optional per the task; same three-variant treatment (Night exists and needs the drift fix, Day and Calm are net new), and the existing per-language stanzas (1.5) carry forward almost unchanged, just re-pointed at corrected named colors.

**Format:** JSON (VS Code), TOML (Starship), `.conf` (Geany). No platform constraints beyond VS Code's own theme-contribution schema.

### 3b. Meeting backgrounds (Zoom/Google Meet)

| Variant | Treatment | Tokens/assets |
|---|---|---|
| Dark signature gradient | Full-bleed `--cg-gradient-signature` wash over `--cg-abyss`, echoing `slide-cover.svg`'s treatment | `--cg-gradient-signature` (azure to violet to indigo, 135deg), `cytognosis-wordmark-light.svg` small, corner-anchored |
| Warm light | `--cg-lp-bg`/`--cg-lp-surface` base with a subtle `--cg-lp-violet` wash | `cytognosis-wordmark-dark.svg` small, corner-anchored |
| Subtle cell-network motif | Faint, low-opacity abstract network pattern (nodes, stems, glow) derived from the mark's visual language on `--cg-abyss`, not the mark itself (avoids the "don't recolor/stretch the mark" rule since it's an ambient derived pattern) | Node/glow vocabulary from `cytognosis-logo-latest-2026-07.svg`; keep opacity low enough to stay texture, not distraction |
| Plain calm | Solid `--cg-neutral-900` or `--cg-abyss` field, no gradient, no motif, tiny icon-mark bottom corner only | For the most sensory-sensitive setting |

**Dimensions:** 1920x1080, PNG, sRGB, all four variants. **Platform constraints:** keep the center 60% width x 70% height clear for face/torso; keep the bottom ~120px clear for the Zoom/Meet name-and-caption strip and the top ~60px clear of the app's own chrome overlay; apply LOGO.md's existing clear-space rule (x-height of the wordmark's capital C) around whichever mark placement is used; stay under typical platform upload limits (Zoom: 5MB per image).

### 3c. LinkedIn

| Artifact | Dimensions | Status | Tokens/assets | Constraint |
|---|---|---|---|---|
| Company banner | 1584x396 | **exists** (`linkedin-banner.png`) | | |
| Personal-profile banner | 1584x396 | net new | Signature gradient wash, wordmark/icon-mark small and corner-anchored (not centered, a large centered logo reads as a company page) | Keep left ~250px clear; LinkedIn's profile-photo circle overlaps that region of the banner |
| Post/carousel, square | 1200x1200 | net new (existing 1080x1080 in `social-cards.html` is IG/X-sized, slightly undersized for LinkedIn's current native recommendation) | Reuse `social-cards.html`'s dark/paper/accent variant system | Regenerate at 1200x1200 specifically for LinkedIn |
| Post/carousel, portrait | 1080x1350 (4:5) | net new, no precedent at all | Same masthead pattern as above, or the one-pager's masthead simplified | LinkedIn's higher-engagement vertical format |
| Event cover | 1584x396 | net new content variant | Same canvas as company banner, event name/date/violet accent | |

### 3d. Slack

| Artifact | Spec | Tokens/assets | Constraint |
|---|---|---|---|
| Workspace icon | 512x512 master, square, solid `--cg-violet-600` or `--cg-abyss` background (Slack composites on its own chrome, so avoid transparency) | `cytognosis-mark-simplified.svg` centered, ~15% padding, matching `avatar.png`'s existing approach | Slack minimum upload 132x132 |
| Channel/Canvas header banner | 1600x400 (wide banner) | Same visual language as social cards | Slack has **no native "channel header image" field** the way Zoom has backgrounds; this is a graphic for manual pinning at the top of a channel or as a Slack Canvas cover, not a system-level asset. Flag this constraint explicitly when this gets generated |
| Custom emoji starter set | 128x128 PNG, transparent background, ~8-10 glyphs | Pull from the existing 48-icon solid (duotone) variant: `check-circle` (approved), `cell`/`dna` (identity), `flask` (science), `live-dot` (shipped/live), `sync` (in progress), `heart-pulse` (care), `alert-triangle` (heads up), `atom` (research), `support` | Depends on the iconography revision in `prompt_icons.md` if that revision ships first (see section 4); solid variant already validated to read on both light and dark per that doc |

### 3e. Other social

| Artifact | Dimensions | Status | Tokens/assets | Constraint |
|---|---|---|---|---|
| X/Bluesky avatar | 1:1 | **reuse existing** `avatar.png` | | X/Bluesky both crop to circle; confirm the existing 15% padding clears a circular crop |
| X banner | 1500x500 (3:1) | net new | Same gradient/light options as meeting backgrounds, wordmark small and off-center | Bottom-left overlaps the avatar circle, keep that corner clear |
| Bluesky banner | 3000x1000 (3:1, same ratio, higher-res) | net new | Same design as X banner, scaled | |
| YouTube channel art | 2560x1440 canvas | net new | Wordmark/tagline must sit inside the guaranteed-visible center **1546x423** box; outer bleed can carry gradient/motif | Classic YouTube safe-zone constraint, must be explicit, this is the most commonly botched spec of the set |
| GitHub org avatar | 500x500 minimum | net new (re-export at correct size) | Reuse `avatar.png` treatment | |
| GitHub social preview | 1280x640 | net new | **Not** the same as the existing 1200x630 `og-image.png`, GitHub requires its own exact size, don't just reuse the OG image as-is | |
| Email header banner | ~600px wide x 200-250px tall | net new | Static PNG/JPG only, no SVG, no web fonts, no CSS gradients (email clients need baked raster); distinct from the email signature, which already exists and stays as-is | Reuse the signature template's hard-won client-safety lessons (host, don't inline; system-safe widths) |

### 3f. Print/one-pager letterhead

Precedent (`one-pager.html`) already has a working masthead (logo left, doc-meta right, 1px ink-deep rule) and footer (violet dot, org name, contact, page number, 1px rule) built for a specific research-brief content layout. **Recommendation: extract a standalone blank letterhead** (`templates/letterhead.html`), same page setup as the one-pager (US Letter, 0.75in margins, `--cg-day-50` page on `--cg-day-200` canvas), with just the masthead and footer and an empty body region, so it is usable for board letters and general correspondence without repurposing the research-brief template. Optional variant: a very-low-opacity signature-gradient watermark bottom-right, echoing the OG image's "subtle signature-gradient wash" treatment.

---

## 4. Suggested generation order

1. **VS Code/Starship/Geany theme family** (Night fix, Day, Calm). Highest reuse of validated precedent, smallest defect list, and Shahin uses this daily, fastest path to a visible, usable win.
2. **Meeting backgrounds**, all four variants. Fully net new but low-risk; reuses `slide-cover.svg`/`slide-divider.svg` gradient work almost directly, and gets used on every call starting immediately.
3. **LinkedIn set** (personal banner, 1200x1200 and 1080x1350 post templates, event cover). Builds directly on the existing company banner and `social-cards.html` patterns.
4. **Other social batch** (X/Bluesky banner, YouTube channel art, GitHub avatar + 1280x640 preview, email header). Same design language as the OG/social-card system, mostly resizes and re-crops of already-established compositions; batch together in one pass.
5. **Slack set** (workspace icon, Canvas/channel header, emoji starter set). Sequence after the iconography revision in `prompt_icons.md` if that revision is still pending, since the emoji set draws directly from the 48-icon library and picking from a mid-revision set risks rework.
6. **Print letterhead.** Lowest frequency of use; do last, or bundle opportunistically with any other print-collateral request.
