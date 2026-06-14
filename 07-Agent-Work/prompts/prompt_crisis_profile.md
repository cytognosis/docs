# Claude Design Prompt: Crisis Profile

> Paste this prompt into Claude Design when you want to build or refine the Crisis profile.
> Cytognosis context: companion-profile.md, crisis-profile.md, nd-design-guide.md

---

## Brief

Build the Crisis profile for urgent health states, anomaly alerts, and situations requiring immediate action. This profile strips away all decorative elements and presents a single clear call-to-action with maximum readability.

## 1. Typography

- Body font: Inter at 18px minimum, weight 500+
- Display: Inter at 32px (2rem)
- Code: JetBrains Mono at 16px
- Max content width: 55ch (shorter than Companion's 65ch for quicker scanning under stress)
- No italic, no underline; bold and color only for emphasis

## 2. Colors

### Surfaces
- Dark: `#0D0D1A` (surface), `#1A1A2E` (elevated)
- Light: `#FFF8F7` (surface), `#FFFFFF` (elevated)
- Never pure black or pure white

### Severity Scale
- Low: Azure-300 `#9BC5F7` (informational)
- Medium: Amber `#E8C040` (caution)
- High: Coral `#F26355` (urgent, action required)
- Critical: Bright Coral `#FF6B6B` (emergency, immediate action)

### Rules
- Use Coral (`#F26355`) as urgency accent, never red
- Always pair severity colors with text label + icon
- Never rely on color alone to convey meaning

## 3. Layout

### Crisis Card (primary container)
- Max width: 480px, center aligned
- 16px border radius (larger than standard)
- 2rem padding
- 1px border: coral at 30% opacity

### Crisis Banner (overlay on any profile)
- Fixed top, full width
- 2px bottom border: coral at 30% opacity
- Box shadow: `0 4px 24px rgba(242, 99, 85, 0.12)`

### Crisis Dialog (modal)
- Max width: 520px
- 20px border radius
- Backdrop: `rgba(10, 10, 20, 0.85)`
- No close-on-click-outside (require explicit dismiss)

## 4. Interaction

### Primary Action Button
```css
background: #F26355;
color: #FFFFFF;
border: none;
border-radius: 12px;
padding: 1rem 2rem;
font-size: 1.125rem;
font-weight: 600;
min-height: 56px;
min-width: 200px;
```

### Secondary Action (dismiss, defer)
- Transparent background
- Low-opacity text and border
- Same 56px touch target

### Focus States
- 3px solid coral outline, 4px offset

## 5. Motion

**Completely disabled. Not configurable.**

```css
[data-profile="crisis"] *,
[data-profile="crisis"] *::before,
[data-profile="crisis"] *::after {
  animation: none !important;
  transition: none !important;
}
```

No motion toggle in Crisis. Animations are architecturally inappropriate in urgent contexts.

## 6. Stripped Elements

Hide when Crisis is active:
- `.decorative` elements
- `.badge` elements (except `.severity-badge`)
- `.avatar` elements
- `aside` elements (except `.crisis-info`)

## 7. Usage Modes

### Standalone
- Full page with Crisis profile as the only profile
- Single crisis card centered

### Banner Overlay
- `[data-crisis="banner"]` on any existing profile
- Fixed top, pushes content down

### Dialog
- `<dialog data-profile="crisis" open>`
- Heavy backdrop darkening
- Single card inside

## 8. Accessibility

- Touch targets: 56px minimum
- Contrast: WCAG AAA (7:1) for all text
- Single primary CTA per screen (max 2 buttons total)
- No autoplay, no motion, no distractions
- Clear next-action in every error/alert state

## 9. Testing

- Verify no animation plays under any circumstance
- Verify touch targets meet 56px minimum
- Verify contrast passes WCAG AAA
- Verify decorative elements are hidden
- Verify single-action focus (no competing CTAs)
- Test banner overlay on all other profiles
- Test dialog modal with heavy backdrop
