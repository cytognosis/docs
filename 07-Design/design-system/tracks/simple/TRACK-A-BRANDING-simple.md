# Track A (Branding), in Plain Words

> **Status**: Active
> **Date**: 2026-07-11
> **Author**: @shahin
> **Audience**: designers, engineers
> **Tags**: `design`, `design-system`, `tracks`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

**Reading time: 90 seconds.** Full plan: `TRACK-A_BRANDING-REPO_PLAN.md`.

> **101 box:** The branding repo on GitHub should be the mirror of your Design System. Right now it holds Ali's unrelated component library instead. This track fixes that and wires it so the repo always has your latest design automatically.

## What is wrong now

- The branding repo was replaced (commit `9bf41cb`, July 3) with Ali's "CytoStyle" library. Your old design files (logos, ~220 icons, the design-system folder, 6 of 7 brand skills, the auto-sync pipeline) are gone from the current version but still recoverable from history.
- One useful thing survived: CytoStyle already has your correct brand colors buried inside it, just not wired up.

## What this track builds

1. Recover the old design-system structure from git history.
2. Graft in the published v11.2.1 design (tokens, logos, icons, the new artifacts).
3. Wire the auto-sync: a safe daily check reads your published Design System through the browser and flags any drift; a confirmed pull updates the repo, with a validator that blocks anything off-brand or any Helix-as-product slip.
4. Produce the Website Template (the handoff to the website track) and the package Yar uses.

## The one gate

Recovering the repo means partly undoing Ali's change, so it needs a conversation with him first. But building the new design content and the sync can start now without waiting.

## Your part

Run this as its own chat opening with the full plan. Have the Ali conversation when you can; everything else proceeds.
