# Ali Conversation Brief (branding-repo recovery gate)

> **Status**: Active  |  **Date**: 2026-07-10  |  **Audience**: Shahin, Ali

**Why:** the branding repo was replaced by CytoStyle (Ali's rebuild) at commit `9bf41cb`, and the website similarly got a new version on top of the old one; both lost features that must be recovered from git and reconciled, not discarded.

## Decisions to align with Ali
1. **Branding repo recovery**: recover the pre-CytoStyle features from git history and reconcile them into the current structure (do not simply overwrite Ali's rebuild). Agree the merge strategy.
2. **npm scope**: move package scope `@alimohammadiwork` -> `@cytognosis`.
3. **License**: resolve the ISC (current) vs Apache-2.0 / CC-BY (intended) mismatch.
4. **Website**: confirm which lost features to recover from git (pre-Ali-rebuild) and the July 6 Inter->Space Grotesk revert.

Everything NOT in this list can proceed now (Template build, artifact pack, website CI/CD diagnosis).
