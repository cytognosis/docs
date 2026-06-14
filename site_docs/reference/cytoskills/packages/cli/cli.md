> **Status**: Active
> **Date**: 2026-06-14
> **Author**: Cytognosis Foundation
> **Audience**: engineers, skill authors, operators
> **Tags**: `cli`, `cytoskills`, `cyto-skills`, `commands`, `reference`

# @cytognosis/cyto-skills-cli — CLI Package

> **Reading time**: ~15 minutes
> **If you only read one thing**: `cyto-skills` is the command-line interface for the entire cytoskills skill ecosystem. It exposes every operation from the core and deploy packages as shell commands: list, inspect, classify, doctor, judge, review, tag, deploy, sync, and manage agent memories.

---

## What It Is and Why

`@cytognosis/cyto-skills-cli` is a thin Commander.js wrapper around the `@cytognosis/cyto-skills` (core) and `@cytognosis/cyto-skills-deploy` (deploy) packages. It translates every programmatic API into a `cyto-skills <command>` shell invocation.

The CLI is the **primary operator interface** for day-to-day skill management: deploying profiles, judging skill quality, tagging with CSO terms, syncing to editor directories, and managing agent memory files.

**Package metadata**:

| Field | Value |
|-------|-------|
| npm name | `@cytognosis/cyto-skills-cli` |
| Binary | `cyto-skills` |
| Version | 1.0.0 |
| Runtime | Node >= 20, ESM |
| Dependencies | `@cytognosis/cyto-skills`, `@cytognosis/cyto-skills-deploy`, `commander`, `chalk` |

---

## Monorepo Position

```
cytoskills/
├── packages/
│   ├── core/          ← provides all logic
│   ├── deploy/        ← provides sync/deploy helpers
│   └── cli/           ← THIS PACKAGE — wraps core + deploy as shell commands
│       └── src/bin/cyto-skills.ts   ← single source file
```

The CLI has no runtime logic of its own. It is a pure adapter: parse flags, call core/deploy functions, format output.

---

## Command Reference

### Top-Level Commands

| Command | Purpose |
|---------|---------|
| `cyto-skills list` | List all discoverable skills across phase repositories |
| `cyto-skills inspect <skillDir>` | Print frontmatter and paths for a skill |
| `cyto-skills classify <skillDir>` | Classify a skill using the CSO taxonomy |
| `cyto-skills doctor <skillDir>` | Run diagnostics on a skill directory |
| `cyto-skills validate <file>` | Validate a JSONL file for structural integrity |
| `cyto-skills synthesize` | Find overlapping skills and generate consolidation reports |
| `cyto-skills root` | Print the resolved `skills/` root directory |
| `cyto-skills deploy-configs` | Deploy CLAUDE.md / GEMINI.md to user dirs |
| `cyto-skills sync-editors` | Sync editor settings and extensions across IDEs |
| `cyto-skills sync-brand` | Sync the brand skill from cytognosis branding source |
| `cyto-skills sync-skills` | Sync skill symlinks to editor directories |
| `cyto-skills sync-all` | Deploy ALL profiles to their respective targets |

---

### `profile` — Skill Profile Management

Profiles are YAML files under `profiles/` that bundle skill lists for specific use cases, with optional inheritance from `_base.yaml`.

| Subcommand | Purpose |
|------------|---------|
| `cyto-skills profile list` | List available profiles |
| `cyto-skills profile show <name>` | Show resolved profile contents (with inherited skills) |
| `cyto-skills profile deploy <name>` | Deploy a profile by creating symlinks |

**`profile deploy` options**:

| Flag | Description |
|------|-------------|
| `--clean` | Remove all existing entries before deploying |
| `--target <path>` | Override the target directory |
| `--dry-run` | Preview without making changes |

---

### `judge` — Skill Quality Scoring

Scores skills on 6 axes (structure 20%, trigger 25%, content 25%, CSO 10%, naming 10%, freshness 10%). Verdicts: PASS ≥ 70, WARN 50–69, FAIL < 50.

| Subcommand | Purpose |
|------------|---------|
| `cyto-skills judge skill <path>` | Score a single skill SKILL.md |
| `cyto-skills judge all` | Judge all skills under a root directory |
| `cyto-skills judge cytognosis` | Judge Cytognosis skills across cytoskeleton + branding |

**`judge skill` options**:

| Flag | Description |
|------|-------------|
| `-v, --verbose` | Show per-axis breakdown and all issues |
| `--tag` | Auto-run tagger before scoring (so CSO axis is not a false zero) |

**`judge all` options**:

| Flag | Description |
|------|-------------|
| `--root <path>` | Search root (default: cwd) |
| `-v, --verbose` | Show per-axis notes |
| `--min-score <n>` | Show only skills below this score |
| `--verdict <v>` | Filter by verdict: PASS, WARN, or FAIL |

**Example output**:

```
✅ my-skill [82/100] [████████████████····]

  structure     90/100  [██████████]
  trigger       85/100  [█████████·]
  content       80/100  [████████··]
  cso           75/100  [████████··]
  naming       100/100  [██████████]
  freshness     70/100  [███████···]
```

---

### `review` — Collection Analysis

Analyzes a directory of skills for naming conflicts, vocabulary overlap (Jaccard ≥ 0.35 on description words), and oversized split candidates (> 20 trigger terms, > 300 body lines, or > 1000-char description).

| Subcommand | Purpose |
|------------|---------|
| `cyto-skills review collection` | Analyze a skill directory |
| `cyto-skills review cytognosis` | Review Cytognosis skills across cytoskeleton + branding |

**`review collection` options**:

| Flag | Description |
|------|-------------|
| `--root <path>` | Collection root (default: cwd) |

---

### `tag` — CSO Ontology Tagging

Tags skills with CSO CURIE terms. Writes `.cyto-tags.yaml` sidecars and promotes high-confidence tags into SKILL.md frontmatter.

| Subcommand | Purpose |
|------------|---------|
| `cyto-skills tag skill <skillPath>` | Tag a single SKILL.md (writes `.cyto-tags.yaml`) |
| `cyto-skills tag all` | Tag all SKILL.md files under a directory |
| `cyto-skills tag promote <skillPath>` | Promote sidecar tags into SKILL.md frontmatter |
| `cyto-skills tag show <skillPath>` | Display existing sidecar tags |

**Common `tag` options**:

| Flag | Description |
|------|-------------|
| `--dry-run` | Preview without writing |
| `--confidence <threshold>` | Minimum confidence 0–1 (default 0.5 for tag, 0.7 for promote) |
| `--root <path>` | Root for `tag all` (default: cwd) |

**Tagging workflow**:

```bash
# 1. Write sidecar
cyto-skills tag skill skills/my-skill/SKILL.md

# 2. Inspect results
cyto-skills tag show skills/my-skill/SKILL.md

# 3. Promote to frontmatter (threshold 0.7)
cyto-skills tag promote skills/my-skill/SKILL.md

# 4. Verify judge score improved
cyto-skills judge skill skills/my-skill -v
```

---

### `ontology` — CSO CURIE Operations

Direct access to the Cyto Skill Ontology (CSO) registry.

| Subcommand | Purpose |
|------------|---------|
| `cyto-skills ontology list` | List all CSO terms |
| `cyto-skills ontology search <query>` | Search CSO terms by keyword |
| `cyto-skills ontology expand <curie>` | Expand a CURIE to a full IRI |
| `cyto-skills ontology mappings <curie>` | Show SSSOM cross-ontology mappings |
| `cyto-skills ontology validate <curie>` | Check if a CURIE is a valid CSO term |

**`ontology list` options**:

| Flag | Description |
|------|-------------|
| `--axis <A|B|C|meta>` | Filter by ontology axis |

---

### `agent` — Agent Skill and Memory Management

Install, audit, and manage skills and memory files for AI agent runtimes.

| Subcommand | Purpose |
|------------|---------|
| `cyto-skills agent list [agent]` | List installed skills for an agent |
| `cyto-skills agent install <skill>` | Install a skill to an agent's skills directory |
| `cyto-skills agent batch <group>` | Batch install a skill group to one or all agents |
| `cyto-skills agent uninstall <skill>` | Remove a skill from an agent's directory |
| `cyto-skills agent doctor [agent]` | Health-check an agent's skills directory |
| `cyto-skills agent doctor-all` | Health-check all known agents |
| `cyto-skills agent doctor-desktop` | Health-check the Claude Desktop / Cowork installation |
| `cyto-skills agent fix-launcher` | Install the version-agnostic Claude Code launcher |
| `cyto-skills agent fix-paths <old> <new>` | Fix stale folder paths in spaces/sessions after a move |
| `cyto-skills agent purge-cache` | Purge Electron renderer caches |
| `cyto-skills agent memory <agent>` | Show an agent's memory file |
| `cyto-skills agent memory-update <agent> <section>` | Update or append a section in a memory file |
| `cyto-skills agent memory-diff [agent]` | Compare source memory with deployed memory |
| `cyto-skills agent memory-harmonize` | Backport deployed-only sections to source files |
| `cyto-skills agent memory-revision <section>` | Update a section across all source files |
| `cyto-skills agent vault-link <repoPath>` | Symlink a repo's docs/ into ObsidianVault |

**Valid agent IDs**: `antigravity`, `claude`, `agents`, `cursor`, `kiro`

**Skill groups for `agent batch`**: `cytognosis`, `coding`, `science`, `writing`, `meta`

**`agent doctor-desktop`** checks:

- SDK binary path (version-sorted, survives apt updates)
- Launcher script (version-agnostic vs. hardcoded)
- `~/.config/Claude/config.json` validity
- Cowork `spaces.json` for stale folder paths
- Session config files for stale paths

**`agent memory-diff` flags**:

| Flag | Description |
|------|-------------|
| `--json` | Output raw JSON |

**`agent memory-harmonize` flags**:

| Flag | Description |
|------|-------------|
| `--backport` | Apply backport changes (default is dry-run) |
| `--dry-run` | Preview without writing |
| `--json` | Output raw JSON |

---

### `catalog` — Third-Party Skill Repository Catalog

Manage `third_party/` git submodules as a curated skill source.

| Subcommand | Purpose |
|------------|---------|
| `cyto-skills catalog list` | List all configured catalog sources and their skill counts |
| `cyto-skills catalog fetch <source>` | Clone or pull a skill repo from GitHub |
| `cyto-skills catalog diff` | Show catalog skills not yet installed locally |

**`catalog fetch` source formats**:

```bash
# GitHub owner/repo shorthand
cyto-skills catalog fetch jeffallan/my-skills

# Full URL
cyto-skills catalog fetch https://github.com/org/repo.git

# Update existing
cyto-skills catalog fetch jeffallan/my-skills  # runs git pull if already cloned
```

---

### Deploy / Sync Commands (Top-Level)

| Command | Purpose | Key Flags |
|---------|---------|-----------|
| `cyto-skills deploy-configs` | Deploy CLAUDE.md / GEMINI.md with section-aware merge | `--dry-run`, `--skip-git`, `--target <name>` |
| `cyto-skills sync-editors` | Sync editor settings across IDEs | — |
| `cyto-skills sync-brand` | Sync brand skill from cytognosis branding source | — |
| `cyto-skills sync-skills` | Sync skill symlinks to editor directories | `--execute`, `--clean`, `--target <name>`, `--skills-dir <path>` |
| `cyto-skills sync-all` | Deploy all profiles to their targets | `--clean` |

Note: `sync-skills` defaults to dry-run. Pass `--execute` to apply changes.

---

## Common Workflows

### New skill quality check

```bash
# Score the skill
cyto-skills judge skill skills/my-skill -v

# If CSO axis is zero, tag it first
cyto-skills judge skill skills/my-skill --tag -v

# Fix issues, re-score
cyto-skills judge skill skills/my-skill
```

### Deploy skills to all agents

```bash
# Preview
cyto-skills sync-skills

# Apply
cyto-skills sync-skills --execute

# Or deploy a specific profile
cyto-skills profile deploy cytognosis --dry-run
cyto-skills profile deploy cytognosis
```

### Memory drift check and repair

```bash
# Check all agents
cyto-skills agent memory-diff

# Inspect specific agent
cyto-skills agent memory-diff claude

# Propose backports (dry-run)
cyto-skills agent memory-harmonize

# Apply backports
cyto-skills agent memory-harmonize --backport

# Re-deploy after backport
cyto-skills deploy-configs
```

### Claude Desktop health check

```bash
cyto-skills agent doctor-desktop

# Fix launcher if hardcoded version detected
cyto-skills agent fix-launcher

# Fix stale paths after moving the Claude folder
cyto-skills agent fix-paths ~/Documents/Claude ~/Claude --dry-run
cyto-skills agent fix-paths ~/Documents/Claude ~/Claude

# Purge caches after path fix
cyto-skills agent purge-cache
```

---

## Architecture Notes

- The CLI is a single file: `packages/cli/src/bin/cyto-skills.ts`.
- All heavy logic is imported from `@cytognosis/cyto-skills` and `@cytognosis/cyto-skills-deploy`. The CLI itself has no business logic.
- The `judge`, `review`, and `reviewCollection` commands are dynamically imported with `await import(...)` to keep top-level parse fast.
- `--dry-run` is supported on all mutating commands. Always check behavior with `--dry-run` before applying.

---

## Reference Index

| Resource | Path |
|----------|------|
| CLI source | `packages/cli/src/bin/cyto-skills.ts` |
| Core package docs | [../core/core.md](../core/core.md) |
| Deploy package docs | [../deploy/deploy.md](../deploy/deploy.md) |
| Quick reference | [cli-quickref.md](cli-quickref.md) |
| Existing CLI reference (older) | `cli-reference.md` (internal repo) |
