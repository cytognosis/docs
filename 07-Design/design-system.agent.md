# Cytognosis Design System — Agent Brief

> **Status:** Active · **Date:** 2026-07-01 · **Variant:** agent (self-contained) · **Technical source:** `branding-design-system-spec.md` · **Readable:** `design-system.readable.md`

**If you only read one thing:** You are editing a token-based design system whose source of truth is the `cytognosis/branding` repo. This docs spec (`07-Design/branding-design-system-spec.md`) is the downstream reference. Never hardcode Tailwind or Bootstrap colors, never use Space Grotesk, always use the fluorophore palette and Inter. Confirm the open gradient-drift item before shipping brand-critical gradients.

---

## Goal

Keep the Cytognosis visual identity consistent across every surface (website, apps, dashboards, CLI, ND companion, crisis alerts) using one CSS token layer scoped by `data-profile`.

## Scope

- **In scope:** design tokens (color, type, space, radius, shadow, motion, glass), the six profiles, the website implementation profile (§14), component styling that consumes tokens, accessibility rules, the sync protocol.
- **Out of scope:** website hosting and DNS (Infrastructure pillar), product feature specs (Yar/Cytonome), content copy (see `_drive/content-*` in the Website project).

## Decided / done

- Palette is fluorophore-derived and fixed: violet `#8B3FC7`, azure `#3B7DD6`, indigo `#5145A8`, teal `#14A3A3`, coral `#F26355`, magenta `#E0309E` (accent only).
- Display and body font is **Inter**; accent is Newsreader; code is JetBrains Mono. Space Grotesk and the Sage/Amber palette are superseded (2026-07-01).
- Website profile (calm violet `#6E5BD1`, warm-light theme, calmer motion) folded into the spec as §14 (2026-07-01).
- Six profiles defined and scoped via `data-profile`.

## Open questions / risks

- **Signature-gradient drift (OPEN):** brand skill v8.0 (`#8B3FC7`, `#5A95E8`, `#E0309E`) vs this spec v10.1.0 (`#3B7DD6`, `#8B3FC7`, `#5145A8`). Confirm with founder, re-run sync. Tracked in `Website/00-CONSOLIDATION/CONFLICTS.md`.
- **Upstream §14:** the website implementation profile lives in this docs spec; push it into the branding repo `guidelines/` at the next sync so the skill carries it.
- **Stale `CLAUDE.md` values:** both the project and global `CLAUDE.md` still list Space Grotesk and Sage/Amber. Project copy corrected 2026-07-01; global correction recommended.

## Source-of-truth files

| Need | Path |
|------|------|
| Full technical spec | `07-Design/branding-design-system-spec.md` |
| Readable summary | `07-Design/design-system.readable.md` |
| ND evidence base | `07-Design/adhd-neurodiversity-design-research.md` |
| Sync steps and scripts | `07-Design/claude-design-sync-protocol.md` |
| Brand voice + visual authority | `brand-identity` skill (auto-synced from `cytognosis/branding`) |
| Token source of truth | `cytognosis/branding` repo, `design-system/tokens/design-tokens.css` |

## Exact start commands

```bash
# Where the tokens actually live (source of truth):
cd ~/repos/cytognosis/branding

# Detect drift across the three canonical locations:
python3 scripts/claude_design_diff.py            # expect zero critical differences

# After editing tokens in the branding repo, sync outward:
python3 scripts/sync_from_claude_design.py --input <export-dir>
python3 ../cytoskills/scripts/sync_branding_skill.py --verbose
python3 scripts/sync_to_claude_design.py         # close the loop
```

Editing this docs spec directly is a documentation act; token changes must originate in the branding repo, or they will be overwritten at the next sync.

## Success criteria

- Any surface you touch uses only fluorophore tokens and Inter; no forbidden color frameworks, no Space Grotesk.
- `claude_design_diff.py` reports zero critical drift after your change.
- New brand-facing gradients wait on the resolved signature-gradient decision.
- Accessibility holds: WCAG AA for text, 44px touch targets (48px Companion, 56px Crisis), reduced-motion respected.
