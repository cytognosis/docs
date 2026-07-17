# Guideline: Progress Report + Living Index (general, reusable)

> **Status:** Standing rule · **Date:** 2026-07-17 · **Author:** Shahin Mohammadi · **Tags:** `process`, `guideline`
> Applies to any multi-artifact effort (consolidation, build, research program), not just funding.

**After every working turn, always do all four:**

1. **Progress report.** Create or update `PROGRESS_REPORT.md` in the Claude project folder and present it as the turn's deliverable. ADHD-friendly: BLUF, reading time, tables, at least one mermaid chart, GitHub alert blocks (NOTE / IMPORTANT / WARNING / TIP), and direct links. Sections: scoreboard, live status, what was built (with links), master points of entry, health audit, guardrails, follow-ups.

2. **Living index graph.** Maintain one master `INDEX.md` entry point. Every hub folder gets its own `INDEX.md`; every folder that holds content is reachable from a parent index and links back. The goal is a single citation graph where no file is an island.

3. **Audit each turn.** Run three checks and remediate or queue in the report: orphans (files not reachable from any index), duplicates (identical basenames and byte-identical content via hash), and folders with content but no `INDEX.md`. Distinguish true orphans from leaf files referenced by machine configs (YAML/glob) and from intentional `_archive/` and `_RELOCATED` pointers.

4. **Version control.** Commit sequentially in the canonical repo as the user (Shahin Mohammadi); create a backup tag before any destructive or irreversible action; archive over delete; never delete unique content.

The progress report is the canonical "where are we" surface, refreshed and shown every turn.

## Additional standing rules (2026-07-17)

- **Deadline calendar is mandatory.** Every `PROGRESS_REPORT.md` MUST include a complete deadline calendar (a table plus a mermaid timeline) listing every dated opportunity; never drop a dated item when regenerating the report. Rolling and entity-blocked items are listed separately.
- **ADHD pairing.** Every main spec doc must be paired with an ADHD-friendly variant in ObsidianVault that mirrors the same structure and links back to the original (`<stem>_adhd.md`; frontmatter `variant: adhd-friendly` + `canonical: docs:<relpath>`; template at `ObsidianVault/_templates/adhd-friendly-template.md`).
- **wiki.js visibility.** All docs-repo docs must be visible, explorable, and commentable via wiki.js (`cyto-wiki`, Git-storage to `github.com/cytognosis/docs`, comments on). This requires pushing the local docs repo to origin; wiki.js auto-syncs every 5 minutes.
