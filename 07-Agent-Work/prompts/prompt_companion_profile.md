# Claude Design Prompt: Companion Profile

> Paste this prompt into Claude Design when you want to build the full Companion profile specification and implementation.
> Cytognosis context: `cytognosis-branding/profiles/companion.md`, `cytognosis-branding/references/04_color_system.md`, `cytognosis-branding/references/05_typography.md`.

---

## Brief

Build the complete Companion profile for the Cytognosis Design System. The Companion profile is the ND-first (neurodivergent-first) daily-use profile, designed for people with ADHD, autism, dyslexia, and other neurodevelopmental conditions. It powers the Yar companion app's mobile surfaces, the patient-mode browser extension, and any surface marked for ND daily use.

The Companion profile is not a "simplified" or "reduced" version of Clinical. It is a distinct register with its own typography, color, spacing, motion, and interaction patterns, all optimized for cognitive accessibility and sustained daily engagement.

## 1. Typography

### 1.1 Font stack

| Role | Font | Weight | Size range | Rationale |
|---|---|---|---|---|
| Body text | Lexend | 400 (regular), 500 (medium) | 16-18px | Designed for reading fluency; variable tracking reduces visual crowding |
| Headings | Inter | 600 (semibold) | 20-28px | Familiar across Cytognosis profiles; consistent brand identity |
| Code and data | Atkinson Hyperlegible Mono | 400 | 14-16px | Maximum character distinguishability; designed for low-vision, benefits ND users |
| UI labels | Lexend | 500 | 14-16px | Consistent with body; slightly heavier for scannability |
| Alternate body | OpenDyslexic | 400 | 16-18px | User-selectable toggle for dyslexic users; weighted bottoms reduce letter rotation |

### 1.2 Font toggle

The Companion profile ships a font toggle that allows users to switch between:

1. **Lexend** (default): optimized for reading fluency.
2. **Inter**: standard Cytognosis font; familiar from Foundation profile.
3. **Atkinson Hyperlegible**: maximum character distinguishability.
4. **OpenDyslexic**: designed specifically for dyslexic readers.

The toggle persists the user's choice across sessions. Implementation: a CSS custom property (`--cg-font-body`) on the root element, updated by the `FontToggle` component.

### 1.3 Typography metrics

| Property | Value | Rationale |
|---|---|---|
| Line height | 1.7 | Generous spacing reduces line-tracking difficulty |
| Max line width | 65ch | Shorter lines reduce re-reading in ADHD |
| Paragraph gap | 1.5em | Clear separation between blocks reduces merge errors |
| Letter spacing | Lexend default (variable) | Lexend's built-in variable tracking handles this |
| Word spacing | normal | No modification needed with Lexend |

## 2. Colors

### 2.1 Base palette

The Companion profile uses the muted 300-shade variant of every Cytognosis brand color:

| Color | 300-shade value | Token | Use |
|---|---|---|---|
| Violet 300 | `#C9A0E8` | `--cg-companion-violet` | Mood signal, heading accents |
| Azure 300 | `#8CB8EB` | `--cg-companion-azure` | Focus signal, interactive elements |
| Magenta 300 | `#F09DCF` | `--cg-companion-magenta` | Energy signal, achievement badges |
| Indigo 300 | `#A09AD4` | `--cg-companion-indigo` | Section dividers, secondary text |
| Coral 300 | `#F9B1AA` | `--cg-companion-coral` | Stress signal, gentle alerts |
| Teal 300 | `#7AD1D1` | `--cg-companion-teal` | Sleep signal, success, calm |

### 2.2 Cognitive-signal colors

Five cognitive signals mapped to specific colors (never reassigned within Companion):

- Focus = Azure 300
- Energy = Magenta 300
- Mood = Violet 300
- Sleep = Teal 300
- Stress = Coral 300

### 2.3 Background colors

| Context | Light mode | Dark mode |
|---|---|---|
| Page background | `#FAFAFE` (warm white with indigo undertone) | `#0E0E18` (deep ink with indigo undertone) |
| Card background | `#F2F2FA` | `#1A1A2E` |
| Elevated surface | `#EBEBF5` | `#25253D` |
| Active/selected | Azure 100 `#E6F0FA` | Azure 900 `#1A2A3D` |

### 2.4 Forbidden colors in Companion

- No 600+ shades as background fills (too visually intense for sustained use).
- No pure white (`#FFFFFF`) or pure black (`#000000`) backgrounds (too stark; use warm variants).
- No gradients with more than two stops.
- No animated color transitions longer than 200ms.

## 3. Spacing

### 3.1 Spacing scale

The Companion profile uses a more generous spacing scale than other profiles:

| Token | Base value | Companion multiplier | Companion value |
|---|---|---|---|
| `--space-xs` | 4px | 1.25x | 5px |
| `--space-sm` | 8px | 1.25x | 10px |
| `--space-md` | 16px | 1.25x | 20px |
| `--space-lg` | 24px | 1.25x | 30px |
| `--space-xl` | 32px | 1.25x | 40px |
| `--space-2xl` | 48px | 1.25x | 60px |

### 3.2 Component spacing

| Property | Value | Rationale |
|---|---|---|
| Card padding | 20px | More breathing room within cards |
| Button padding | 12px 24px | Larger touch targets, more readable labels |
| Input padding | 12px 16px | Easier to tap and read |
| List item gap | 12px | Clear separation between items |
| Section gap | 40px | Strong visual breaks between content sections |

### 3.3 Touch targets

- Minimum touch target: 48px (vs 44px standard).
- Interactive elements have at least 8px gap between them.
- Primary actions use larger targets (56px) when space allows.

## 4. Motion

### 4.1 Default: reduced motion

The Companion profile sets `prefers-reduced-motion: reduce` behavior by default, regardless of the system setting. Users can opt in to full motion via Settings.

### 4.2 Motion budget

| Motion type | Default | Opt-in |
|---|---|---|
| Page transitions | Instant (opacity fade only, 150ms) | Slide transitions, 300ms |
| Loading indicators | Static spinner or progress bar | Animated spinner |
| Hover effects | Color change only | Scale + color change |
| Scroll effects | None | Subtle parallax |
| Celebration animations | Static badge display | Confetti, pulse, glow |
| Agent state indicators | Static icon swap | Animated pulse, breathing |

### 4.3 Motion opt-in UI

A motion toggle in Settings with three levels:

1. **Minimal** (default): opacity fades only, < 200ms.
2. **Moderate**: transitions for navigation and feedback, < 300ms.
3. **Full**: all animations enabled, including celebrations and agent state.

## 5. Gamification

### 5.1 Token system

The Companion profile supports lightweight gamification to support habit formation:

| Token | Trigger | Visual | Reward |
|---|---|---|---|
| Streak | Consecutive daily check-ins | Flame icon (magenta-300) with day count | Visible streak counter |
| Progress | Completing a health task | Progress ring (azure-300) filling | Percentage display |
| Achievement | Reaching a milestone | Badge (violet-300) with description | Collection in profile |
| Consistency | Regular engagement pattern | Calendar heat map (teal-300) | Monthly view |

### 5.2 Gamification rules

- Gamification is opt-in. Default: OFF. User enables in Settings.
- No punitive mechanics (no streak-breaking penalties, no lost progress).
- "Pause day" feature: users can pause their streak without losing it.
- No competitive elements (no leaderboards, no comparisons).
- Celebrations are respectful: a brief badge display, not an overwhelming animation.
- All gamification tokens use 300-shade colors to maintain visual calm.

## 6. Density controls

### 6.1 Three density levels

| Level | Line height | Font size | Spacing multiplier | Max width | Default for |
|---|---|---|---|---|---|
| Compact | 1.5 | 14px | 1.0x | 75ch | Not recommended for Companion |
| Comfortable | 1.6 | 16px | 1.15x | 70ch | Secondary option |
| Spacious (default) | 1.7 | 18px | 1.25x | 65ch | Companion default |

### 6.2 Density toggle

The density toggle lives in Settings > Display and as a compact control in the app shell. It adjusts:

- Font size
- Line height
- Spacing multiplier
- Max content width
- Card padding
- Touch target size

## 7. Light and dark mode variants

### 7.1 Light mode

- Background: warm white with indigo undertone (`#FAFAFE`).
- Cards: light lavender (`#F2F2FA`).
- Text: deep indigo ink (`#1C1C2E`).
- Accent: 300-shade palette.
- Preferred for: daytime use, reading-heavy sessions.

### 7.2 Dark mode

- Background: deep ink with indigo undertone (`#0E0E18`).
- Cards: dark indigo (`#1A1A2E`).
- Text: soft white (`#E0E0ED`).
- Accent: 300-shade palette (same values; they read well on dark backgrounds).
- Glassmorphism: `rgba(30,41,59,0.5)` + `blur(12px)` for elevated surfaces.
- Preferred for: evening use, reduced eye strain.

### 7.3 Auto mode

Default to system preference. Companion profile follows the OS light/dark setting with no additional logic.

## 8. Component overrides

The Companion profile overrides these Design System components:

| Component | Override | Rationale |
|---|---|---|
| Button | 48px min height, rounded-lg, 300-shade colors | Larger targets, softer appearance |
| Card | 20px padding, subtle border instead of shadow | Less visual noise |
| Input | 48px min height, 16px font size, clear placeholder text | Easier to use |
| Modal | Max 480px width, single primary action, clear dismiss | Reduced cognitive load |
| Nav | Simplified, max 5 top-level items, icon + label always | Predictable navigation |
| Toast/notification | Persistent until dismissed, no auto-dismiss for important messages | Prevents missed information |

## 9. Deliverables to ship back

1. `branding/design-system/profiles/companion.md` with the complete specification.
2. `branding/design-system/profiles/companion.css` with all token overrides.
3. `branding/design-system/profiles/examples/companion.html` with a rendered example page.
4. `branding/design-system/profiles/examples/companion-dark.html` with the dark mode variant.
5. Updated `branding/design-system/profiles/profiles.css` with Companion overlay tokens.
6. A `branding/design-system/profiles/companion-rationale.md` documenting the evidence base for each design decision.

## 10. Open questions to surface back to Cytognosis

1. Should the Companion profile support "themes" within itself (e.g., "Ocean" with more teal, "Sunset" with more coral)? Recommendation: defer to v2.
2. Lexend vs Atkinson Hyperlegible as the default body font? Lexend is recommended (designed for reading fluency), but Atkinson Hyperlegible has stronger accessibility credentials. Worth A/B testing.
3. The gamification system: should it track across devices (via fabric sync) or stay device-local? Recommendation: sync, but with clear data-ownership messaging.
4. Should the Companion profile support a "quiet hours" mode that suppresses all non-crisis visual updates during specified time windows? Recommendation: yes, in v2.
5. Touch target minimum: 48px (recommended) or 56px (matches Crisis)? Recommendation: 48px default, 56px for primary actions.
