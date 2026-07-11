# How to interact with Claude Design bidirectionally (the browser bridge)

> **Status**: Active
> **Date**: 2026-07-11
> **Author**: @shahin
> **Audience**: designers, engineers
> **Tags**: `design`, `design-system`, `tracks`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

**Established 2026-07-10.** Claude Design (claude.ai/design) has no standalone MCP connector, but it runs in the browser, and the Claude-in-Chrome MCP renders JavaScript and reads the DOM. That is the bridge. No more manual zip exports for reading or verifying.

## Prerequisite (one-time)

The Chrome extension must be connected (it is: "Browser 1", Linux, local). Keep a Chrome window signed in to claude.ai.

## READ path (verify a design without a zip)

1. `list_connected_browsers` then `tabs_context_mcp {createIfEmpty:true}` to get a tab id.
2. `navigate` to the project URL (e.g. `https://claude.ai/design/p/<id>`), then `wait` ~3s for the client render.
3. `get_page_text` returns the full rendered readme, file manifest, component list, and the entire chat transcript. This alone verifies version, product architecture, gradient, tokens, component inventory, and copy.
4. For a specific source file: open it via the file selector (the "No file open" control / project menu), then `get_page_text` or `read_page`. Or use `javascript_tool` to pull exact DOM/text.
5. For visual checks: `computer` screenshot, or `read_page filter:interactive` to find controls.

## WRITE path (drive Claude Design's own chat)

1. `find` the composer ("Describe what you want to create") to get its element ref.
2. `computer` left_click the composer, then `type` the prompt (or paste). Our revision prompts can be sent directly here instead of the user pasting them.
3. Submit and let Claude Design run; poll with `get_page_text` to read its progress and final report.
4. Trigger Export or tick Published through the UI the same way (click by ref/coordinate).

## Safety rules for the WRITE path

- Sending a prompt into the composer, ticking Published, and exporting are actions taken on the user's behalf. Get explicit user go-ahead each session before firing them; do not publish or send unilaterally.
- Reading (the whole READ path) is safe and needs no confirmation.

## What this replaces

The old loop was: user runs prompt in Claude Design, exports a zip to Downloads, Claude moves and audits the zip. New loop: Claude sends the prompt into the composer, reads the result live, and verifies against the rendered DOM. The zip is now optional (only needed to promote files into a repo).
