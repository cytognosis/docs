# Standard: Cowork <-> Claude Code <-> Claude Design Integration (local)

> **Status**: Active
> **Date**: 2026-07-11
> **Author**: @shahin
> **Audience**: engineers, operators
> **Tags**: `engineering`, `agent-integration`, `mcp`, `standard`
> **Variants**: Technical (this doc) - Readable (`simple/COWORK-CODE-DESIGN-INTEGRATION-STANDARD_2026-07-11.md`) - Agent (n/a)

> [!NOTE]
> **TL;DR**: One desktop app (Chat / Cowork / Code tabs + Design sidebar), one @cytognosis.org account, kept open. Register remote MCP connectors once (they auto-load across all surfaces). Bridge Code -> Cowork with `claude mcp serve`; bridge Code <-> Design with `/design-sync` + the hosted Design MCP + UI handoff; use Claude-in-Chrome as the universal fallback actuator; use host-terminal for full host access. Share one working directory; use git worktrees for concurrency.

> **Reading time**: ~6 min. Grounded in the 48-doc `Refactor/spec-driven-stack_2026-07/` research + mechanisms verified 2026-07-11.

## 1. The reality we wire around

- **Cowork is remote-by-default.** Its agent loop runs on Anthropic servers and reaches this laptop only through the **Claude desktop app** (or a local-execution VM). Keep the desktop app open, signed in, folders connected. (support.claude.com "Claude Cowork architecture overview".)
- **Code and Cowork are tabs of the same desktop app; Design is the sidebar / claude.ai/design.** Most "wiring" is keeping that app running + registering connectors once. (code.claude.com/docs/en/desktop; support "Get started with Claude Design".)

## 2. Integration matrix (mechanisms, official unless noted)

| Pair | Direction | Mechanism |
|------|-----------|-----------|
| Code -> Cowork/Chat | expose Code's tools | `claude mcp serve` (stdio MCP). Caveat: no permission UI; the consumer must gate actions. |
| all surfaces <- connectors | shared tools/data | Register remote MCP connectors once at `claude.ai/customize/connectors`; they auto-load in Chat, Cowork, and Code CLI under the same account. |
| Code <-> Design | design system + handoff | `/design-sync` (push design system to Design); hosted **Design MCP** `claude mcp add --scope user --transport http claude-design https://api.anthropic.com/v1/design/mcp` then `/design-login`; Design UI "Handoff to Claude Code / Send to local coding agent". |
| Cowork/Code -> Design (no MCP path) | drive the browser tool | **Claude-in-Chrome** bridge (renders JS, reads/writes DOM). Our path is `07-Design/design-system/tracks/CLAUDE_DESIGN_BRIDGE.md`. Chrome/Edge only; not WSL. |
| phone/web -> local Code | steer a running session | Remote Control (outbound HTTPS only, no inbound port), Channels, Dispatch, Slack, Scheduled tasks. |
| agent -> full host | unrestricted local ops | **host-terminal MCP** (runs on host as the user, sudo) + shared filesystem. This is how this Cowork session already does git/deletes on `~/repos`. |

## 3. Recommended standard setup (seamless + persistent)

1. **Always-on desktop app, one @cytognosis.org account.** Treat it as infrastructure, not an app you open occasionally.
2. **Register remote connectors once** (connectors registry) so they sync to Chat + Cowork + Code CLI.
3. **`claude mcp serve`** registered as a local MCP entry in the desktop config -> gives Cowork/Chat programmatic reach into a full Code agent loop + filesystem tools.
4. **Design wired** via `/design-sync` + the hosted Design MCP (user scope) + `/design-login`; use UI handoff for Design -> Code.
5. **Claude-in-Chrome connected** as the universal fallback actuator (Design, Canva, Figma, any logged-in web app).
6. **Folders pre-trusted** in `~/.claude.json` (`projects[path].hasTrustDialogAccepted=true`) to kill the "folder isn't trusted" gate (done 2026-07-11 for all repos + projects). CAVEAT: a trust-bypass advisory (CVE-2026-33068) exists; this is a convenience on our own machine, re-check advisories before treating pre-seeding as policy.
7. **Shared working directory** (`~/repos/cytognosis/*`, `~/Claude/Projects/*`, docs repo) across Cowork + Code; **git worktrees** when both might edit one repo at once.
8. **host-terminal MCP** kept available for unrestricted host git/destructive/sudo ops (never route those through the sandbox).

## 4. Auth and the headless 401 (fix)

Headless `claude -p` failed here with 401 because the CLI login was stale. Fix: **unset any stale `ANTHROPIC_API_KEY`**, then either `claude setup-token` (long-lived, inference-only) or `--bare` + a real `ANTHROPIC_API_KEY` from console.anthropic.com for automation; use full `/login` when you need Remote Control or Design's `/design-login`. Prefer the one-click desktop (ccd) launch for interactive Code work.

## 5. Config locations

- **Claude Code:** `~/.claude.json` (top-level `mcpServers` = user scope; `projects[path]` = per-project incl. trust); `.mcp.json` at a repo root = project scope (shared on clone).
- **Desktop app:** Settings > Extensions (`.mcpb` one-click) + Settings > Connectors (remote); legacy `claude_desktop_config.json` (Linux path under `~/.config/Claude/`, verify on this build).

## 6. ToS and safety

Automating your own Anthropic tools under your own account is permitted; prohibited uses are guardrail bypass, model scraping/distillation, and reselling access. Respect third-party site ToS. Because this becomes org policy for a 501(c)(3), get a short counsel pass on the own-account-automation vs prohibited-resale distinction before publishing.

## 7. Gaps and current workarounds

- **No unified local-MCP registry:** only remote connectors auto-sync; stdio servers are configured per surface.
- **No documented direct Cowork <-> Design bridge:** use Claude-in-Chrome, or add the Design connector to the shared registry and confirm Cowork picks it up.
- **`claude mcp serve` has no permission UI:** the consumer must gate dangerous tool calls.
- **Research-preview churn** (Remote Control, Channels, Cowork remote exec): pin versions, re-verify.
- **Cowork activity is not in audit logs / exports:** OpenTelemetry streaming is the only current trail (Team/Enterprise).

## 8. Sources

- **Local research (build on this):** `Refactor/spec-driven-stack_2026-07/` (48 docs: `research-G-integration`, `INTEGRATION-ROUTING`, `research-K-routing-design`, `ANTIGRAVITY-BRIDGE-OPTIONS`, `research-L-anthropic-tos`, `MISSION-CENTER-ARCHITECTURE`); design bridge `07-Design/design-system/tracks/CLAUDE_DESIGN_BRIDGE.md`.
- **Official:** code.claude.com/docs (mcp, mcp-quickstart, desktop, chrome, remote-control, channels, headless, permissions); support.claude.com (Cowork architecture, Cowork safety, Claude Design, Claude in Chrome); modelcontextprotocol.io; anthropic.com/legal/aup.

## 9. Implementation checklist (set as standard)

- [ ] Desktop app installed, updated, signed in to @cytognosis.org, kept open.
- [ ] Remote MCP connectors registered once in the connectors registry.
- [ ] `claude mcp serve` added to desktop config (Code -> Cowork bridge).
- [ ] Design MCP added (`--scope user`, hosted URL) + `/design-login`; `/design-sync` verified.
- [ ] Claude-in-Chrome connected (fallback actuator).
- [ ] Folders pre-trusted in `~/.claude.json` (done); advisories re-checked.
- [ ] host-terminal MCP available for host ops (done).
- [ ] Shared working dir + git-worktree discipline documented in each repo README.
