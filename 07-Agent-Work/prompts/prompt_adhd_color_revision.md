# Claude Design Prompt: ADHD Color Revision

> Paste this prompt into Claude Design when you want to revise the Cytognosis color system across all profiles for neurodivergent (ND) compatibility.
> Cytognosis context: `cytognosis-branding/references/04_color_system.md`, `cytognosis-branding/profiles/companion.md`, `cytognosis-branding/profiles/crisis.md`.

---

## Brief

Revise the Cytognosis color system to ensure neurodivergent compatibility across all six profiles, with special attention to the Companion and Crisis profiles. This revision applies evidence-based color choices from ADHD and autism research, establishes a muted 300-shade palette as the Companion default, defines the cognitive-signal color mapping, documents per-profile color overrides, and applies therapeutic color theory where supported by evidence.

## 1. Evidence base

Ground every color decision in published research. Key findings to integrate:

| Finding | Source domain | Design implication |
|---|---|---|
| High-saturation colors increase cognitive load and visual fatigue in ADHD | Attention research, occupational therapy | Default to 300-shade (muted) palettes for Companion |
| Cool blues and greens reduce arousal and support sustained attention | Color psychology, clinical environments | Azure and teal as primary Companion palette anchors |
| Warm reds and oranges trigger alertness but increase anxiety when overused | Arousal research | Reserve coral and magenta for alerts and signals only |
| High contrast improves comprehension under cognitive load | Reading research, low-vision studies | Crisis profile requires 7:1 minimum; Companion requires AAA body text |
| Color-meaning consistency reduces cognitive overhead | UX research, accessibility | Cognitive-signal colors must be stable across all surfaces |
| Pattern recognition is faster than color-alone recognition for colorblind users | Colorblind design research | Always pair color with shape, label, or pattern |

Cite sources in the deliverables. Use peer-reviewed research where available; practitioner guidelines (CHADD, NICE) where peer review is sparse.

## 2. Muted 300-shade palette defaults for Companion

The Companion profile defaults to the 300-shade (muted) variant of every Cytognosis brand color:

| Brand color | 600-shade (standard) | 300-shade (Companion default) | Use in Companion |
|---|---|---|---|
| Violet | `#8B3FC7` | `#C9A0E8` | Mood signal, headings accent |
| Azure | `#3B7DD6` | `#8CB8EB` | Focus signal, interactive elements |
| Magenta | `#E0309E` | `#F09DCF` | Energy signal, achievement badges |
| Indigo | `#5145A8` | `#A09AD4` | Headers, section dividers |
| Coral | `#F26355` | `#F9B1AA` | Stress signal, gentle alerts |
| Teal | `#14A3A3` | `#7AD1D1` | Sleep signal, success states, calm indicators |

Design rules for the Companion 300-shade palette:

- Backgrounds use shades lighter than 300 (100-200 range) or the neutral ink palette.
- Text on 300-shade backgrounds must meet AAA contrast (7:1 for body, 4.5:1 for large text).
- Never use 600+ shades as large background fills in Companion; they are too visually intense for sustained ND use.
- Accent details (badges, progress indicators, streak marks) may use 400-shade for emphasis.

## 3. Cognitive-signal color mapping

The Companion profile maps five cognitive signals to specific colors. These colors are stable across all surfaces and never reassigned to other meanings within the Companion profile:

| Signal | Color | Token | Rationale |
|---|---|---|---|
| Focus | Azure 300 `#8CB8EB` | `--cg-companion-focus` | Blue reduces arousal, supports sustained attention |
| Energy | Magenta 300 `#F09DCF` | `--cg-companion-energy` | Warm pink signals vitality without triggering anxiety |
| Mood | Violet 300 `#C9A0E8` | `--cg-companion-mood` | Purple associated with introspection and emotional awareness |
| Sleep | Teal 300 `#7AD1D1` | `--cg-companion-sleep` | Cool green-blue associated with rest and biological rhythms |
| Stress | Coral 300 `#F9B1AA` | `--cg-companion-stress` | Muted warm signals awareness without amplifying stress |

Implementation requirements:

- Each signal color must be paired with an icon and a text label; never color-alone.
- Signal colors render identically in light and dark modes (adjust background, not signal color).
- Signal colors must pass WCAG AA contrast against both light and dark Companion backgrounds.
- Colorblind fallback: each signal uses a distinct pattern fill (dots for Focus, lines for Energy, crosshatch for Mood, waves for Sleep, dashes for Stress) in addition to color.

## 4. Per-profile color overrides

Document how each profile modifies the base color system:

### 4.1 Foundation (no changes)

Uses the full 600-shade brand palette. Signature gradient (`linear-gradient(135deg, #8B3FC7, #5A95E8, #E0309E)`) as hero wash. No restrictions.

### 4.2 Clinical

- Muted 300-shade pastels as default backgrounds.
- No magenta in body content (reserved for critical alerts only).
- Teal and azure as primary interactive colors.
- AAA contrast required for all body text.

### 4.3 Research

- Full palette available but with indigo as the dominant accent.
- Magenta reserved for alerts and anomaly highlighting.
- Data visualization uses the sequential and diverging palettes from `data-viz/`.

### 4.4 Lab

- Violet-300 on dark ink as the default.
- Full palette available for syntax highlighting and terminal themes.
- No restrictions; Lab users are technical and prefer information density.

### 4.5 Companion

- 300-shade defaults for everything (per §2).
- Cognitive-signal colors locked to their assignments (per §3).
- No 600+ shades as backgrounds.
- Gamification elements (streak flames, achievement badges) use 400-shade accents.
- Background gradients, if used, are subtle (opacity < 0.1) and use only 100-200 shades.

### 4.6 Crisis

- High-contrast mode: text on near-white or near-black backgrounds.
- Coral 600 for urgency. Azure 600 for action buttons.
- Severity scale: Teal 600 (low), Violet 600 (medium), Coral 600 (high), Magenta 600 on dark (critical).
- No gradients. No decorative color. Color serves function only.
- All color choices must pass 7:1 contrast ratio minimum.

## 5. Therapeutic color theory application

Where research supports therapeutic color effects, apply them:

| Principle | Application | Evidence level |
|---|---|---|
| Blue light reduces agitation | Use azure-tinted backgrounds for calm states in Companion | Moderate (clinical lighting studies) |
| Green promotes reading comfort | Use teal-tinted overlays for long-form reading in Companion | Moderate (reading research) |
| Red increases error detection | Use coral for error states across all profiles | Strong (UX research) |
| Warm tones increase engagement | Use coral and magenta accents for gamification in Companion | Moderate (engagement research) |
| Neutral backgrounds reduce distraction | Use indigo-undertone neutrals (never cold gray) in all profiles | Strong (attention research) |

Important: do not overclaim therapeutic effects. Document the evidence level for each application. Cytognosis is a nonprofit focused on evidence-based design, not color therapy.

## 6. Testing checklist for color contrast and visual comfort

Before shipping any color revision, validate:

### 6.1 Automated checks

- [ ] Every text-on-background combination passes WCAG AAA (7:1) in Companion and Crisis profiles.
- [ ] Every text-on-background combination passes WCAG AA (4.5:1) in Foundation, Clinical, Research, and Lab profiles.
- [ ] Large text (24px+) passes 3:1 minimum across all profiles.
- [ ] Cognitive-signal colors are distinguishable in deuteranopia, protanopia, and tritanopia simulations.
- [ ] No two adjacent cognitive-signal colors are confusable in any colorblind simulation.
- [ ] All interactive elements have visible focus indicators with sufficient contrast.

### 6.2 Visual comfort checks

- [ ] Companion profile backgrounds do not cause visual fatigue after 30 minutes of simulated use.
- [ ] No color combination in any profile triggers photosensitive seizure risk (WCAG 2.3.1).
- [ ] Gradient backgrounds do not create banding artifacts on common displays.
- [ ] Dark mode variants maintain the same relative hierarchy as light mode variants.
- [ ] Muted 300-shade palette reads as intentionally designed, not washed out or broken.

### 6.3 ND-specific checks

- [ ] ADHD participants can distinguish all five cognitive signals without relying on color alone.
- [ ] Autistic participants report the Companion palette as "calm" or "comfortable" (not "boring" or "institutional").
- [ ] Dyslexic participants report adequate contrast for body text in Companion profile.
- [ ] No color in the Companion palette triggers sensory overload reports in pilot testing.

## 7. Deliverables to ship back

1. Updated `branding/design-system/references/04_color_system.md` with per-profile color tables and the cognitive-signal mapping.
2. Updated `branding/design-system/profiles/profiles.css` with 300-shade token overrides for Companion.
3. A `branding/design-system/references/04a_color_nd_rationale.md` documenting the evidence base for each ND-specific color decision.
4. Updated `branding/design-system/data-viz/` colorblind-safe palettes verified against the cognitive-signal colors.
5. A testing report template at `branding/design-system/references/04b_color_testing_checklist.md`.

## 8. Open questions to surface back to Cytognosis

1. Should the 300-shade palette be generated algorithmically from the 600-shade base (e.g., via HSL lightness shift), or should each 300-shade value be hand-tuned? Recommendation: hand-tune, then document the formula for consistency.
2. The cognitive-signal colors are assigned based on color psychology literature. Should Cytognosis commission a small study with ND participants to validate the assignments? Recommendation: yes, even a 5-person pilot would strengthen the evidence base.
3. Should the Companion profile support a "warm" and "cool" variant (warm leans coral/magenta, cool leans azure/teal) for user preference? Recommendation: defer to v2; one default first.
4. Crisis severity scale: is four tiers (low/medium/high/critical) the right granularity, or should it simplify to three (low/high/critical)? Clinical safety team should decide.
