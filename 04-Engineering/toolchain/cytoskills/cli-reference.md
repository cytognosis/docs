# cyto-skills CLI Reference

**Binary**: `cyto-skills`
**Source**: `packages/cli/src/bin/cyto-skills.ts`
**Framework**: Commander.js

All commands support `--help` for inline usage. The CLI is organized
into eight command groups covering the full cytoskills lifecycle.

## Skill Management

### `cyto-skills list`

List all discoverable skills across phase repositories.

```bash
cyto-skills list [--root <path>]
```

| Option | Default | Description |
|--------|---------|-------------|
| `--root <path>` | `cwd` | Search root directory |

Each skill is printed with its CSO classification tags and
description. Searches the given root and its parent directory.

**Exit codes**: 0 on success, 1 on load error.

### `cyto-skills inspect <skillDir>`

Print frontmatter and paths for a single skill.

```bash
cyto-skills inspect ./skills/languages/python-pro
```

Displays: name, description, tags, directory path, input/output
counts, script files, and reference files.

**Exit codes**: 0 on success, 1 if skill cannot be loaded.

### `cyto-skills classify <skillDir>`

Classify a skill using the CSO taxonomy hierarchy.

```bash
cyto-skills classify ./skills/ai-ml/deep-learning
# Skill: deep-learning
# Tags:  cso:DeepLearning, cso:MachineLearning
```

**Exit codes**: 0 on success, 1 on error.

### `cyto-skills doctor <skillDir>`

Run diagnostics on a single skill directory. Checks SKILL.md
presence, frontmatter validity, description quality, tags, triggers,
scripts, references, body content, and IO schema references.

```bash
cyto-skills doctor ./skills/cytognosis/brand
```

Output is a formatted Markdown diagnostic report.

**Exit codes**: 0 if healthy, 1 if unhealthy.

### `cyto-skills validate <file>`

Validate a JSONL file for structural integrity. Checks JSON parse
errors, duplicate UUIDs, and orphaned parent references.

```bash
cyto-skills validate session.jsonl
```

**Exit codes**: 0 if valid, 1 if issues found.

### `cyto-skills synthesize`

Find overlapping skills and generate consolidation reports.

```bash
cyto-skills synthesize [--root <path>]
```

| Option | Default | Description |
|--------|---------|-------------|
| `--root <path>` | `cwd` | Search root directory |

Clusters skills by primary classifier tag. Reports clusters of 2+
skills with proposed merged names and unified trigger counts.

### `cyto-skills root`

Print the resolved `skills/` root directory path.

```bash
cyto-skills root
# /home/user/repos/cytognosis/cytoskills/skills
```

## Profile Management

### `cyto-skills profile list`

List all available profile YAML files.

```bash
cyto-skills profile list
# Available profiles (12):
#   coding
#   science/ai-scientist
#   science/research-scientist
#   writing
```

### `cyto-skills profile show <name>`

Show the resolved contents of a profile, including inherited skills.

```bash
cyto-skills profile show coding
```

Displays: name, description, target, inherited profiles, and the
full resolved skill list (with inheritance flattened).

**Exit codes**: 0 on success, 1 if profile not found.

### `cyto-skills profile deploy <name>`

Deploy a profile by creating symlinks in the target directory.

```bash
cyto-skills profile deploy coding [--clean] [--target <dir>] [--dry-run]
```

| Option | Description |
|--------|-------------|
| `--clean` | Remove all existing entries before deploying |
| `--target <dir>` | Override the target directory |
| `--dry-run` | Preview without making changes |

Reports created, skipped (unchanged), and removed symlink counts.
Warns about skills not found in the skill repository.

## Deploy and Sync

### `cyto-skills deploy-configs`

Deploy agent memory configs (CLAUDE.md, GEMINI.md, KIRO.md) to user
directories using section-aware merge.

```bash
cyto-skills deploy-configs [--dry-run] [--skip-git] [--target <name>]
```

| Option | Description |
|--------|-------------|
| `--dry-run` | Preview changes without writing |
| `--skip-git` | Skip git init and commit tracking |
| `--target <name>` | Deploy only a specific target (claude, gemini, kiro) |

**Merge strategy**: reads agent-specific config + shared MEMORY.md,
merges with existing target file preserving user-specific sections.
Optionally snapshots before/after via git.

### `cyto-skills sync-skills`

Sync skill symlinks to editor-specific directories.

```bash
cyto-skills sync-skills [--execute] [--clean] [--target <name>] [--skills-dir <path>]
```

| Option | Description |
|--------|-------------|
| `--execute` | Apply changes (default is dry-run) |
| `--clean` | Remove all existing entries before recreating |
| `--target <name>` | Sync only a specific target (antigravity, agents) |
| `--skills-dir <path>` | Override the skills/ directory |

> [!IMPORTANT]
> Default mode is **dry-run**. Pass `--execute` to apply changes.

### `cyto-skills sync-editors`

Sync IDE configuration files (settings.json, keybindings.json,
launch.json) and install extensions across all detected IDEs.

```bash
cyto-skills sync-editors
```

Supported IDEs: VS Code, Antigravity, Cursor, Windsurf, Positron.
Reads config from `configs/editors/{ide}/`.

### `cyto-skills sync-brand`

Sync the brand skill from the cytognosis branding repository.

```bash
cyto-skills sync-brand
```

Pulls SKILL.tpl.md, guideline `.md` files, and brand assets from
the branding repo into `skills/cytognosis/brand/`. The branding repo
location can be overridden with `CYTOGNOSIS_BRANDING_DIR`.

### `cyto-skills sync-all`

Deploy ALL profiles to their respective targets.

```bash
cyto-skills sync-all [--clean]
```

| Option | Description |
|--------|-------------|
| `--clean` | Clean target before deploying each profile |

## Ontology (CSO)

### `cyto-skills ontology list`

List all Cyto Skill Ontology terms.

```bash
cyto-skills ontology list [--axis <A|B|C|meta>]
```

| Option | Description |
|--------|-------------|
| `--axis <axis>` | Filter by axis (A, B, C, or meta) |

Shows CURIE, label, and SSSOM mapping count for each term.

### `cyto-skills ontology search <query>`

Search CSO terms by keyword against labels and aliases.

```bash
cyto-skills ontology search python
# 3 match(es) for "python":
#   cso:Python                       Python [Axis A]
#     aliases: CPython, pip, ruff
```

### `cyto-skills ontology expand <curie>`

Expand a CURIE to a full IRI.

```bash
cyto-skills ontology expand cso:Python
# https://w3id.org/cytognosis/cso/Python
```

**Exit codes**: 0 on success, 1 if prefix unknown.

### `cyto-skills ontology mappings <curie>`

Show SSSOM cross-ontology mappings for a CSO term.

```bash
cyto-skills ontology mappings cso:Genomics
```

**Exit codes**: 0 on success, 1 if CURIE not found.

### `cyto-skills ontology validate <curie>`

Check if a CURIE is a valid CSO term.

```bash
cyto-skills ontology validate cso:Python
# ✓ cso:Python — Python [Axis A]
```

**Exit codes**: 0 if valid, 1 if invalid.

## Tagging

### `cyto-skills tag skill <skillPath>`

Tag a single SKILL.md with CSO terms. Writes a `.cyto-tags.yaml`
sidecar file alongside the skill.

```bash
cyto-skills tag skill ./skills/languages/python-pro [--dry-run] [--confidence <0-1>]
```

| Option | Default | Description |
|--------|---------|-------------|
| `--dry-run` | — | Preview tags without writing sidecar |
| `--confidence <n>` | `0.5` | Minimum confidence threshold (0-1) |

Accepts either a directory path or a direct SKILL.md path.

### `cyto-skills tag all`

Tag all SKILL.md files under a directory.

```bash
cyto-skills tag all [--root <path>] [--dry-run] [--confidence <n>]
```

| Option | Default | Description |
|--------|---------|-------------|
| `--root <path>` | `cwd` | Root directory to scan |
| `--dry-run` | — | Preview without writing sidecars |
| `--confidence <n>` | `0.5` | Minimum confidence threshold |

### `cyto-skills tag promote <skillPath>`

Promote high-confidence tags from `.cyto-tags.yaml` into SKILL.md
frontmatter.

```bash
cyto-skills tag promote ./skills/languages/python-pro/SKILL.md [--dry-run] [--confidence <n>]
```

| Option | Default | Description |
|--------|---------|-------------|
| `--dry-run` | — | Preview without writing |
| `--confidence <n>` | `0.7` | Minimum confidence to promote |

**Exit codes**: 0 on success, 1 if no sidecar or no tags above
threshold.

### `cyto-skills tag show <skillPath>`

Show current `.cyto-tags.yaml` sidecar for a skill.

```bash
cyto-skills tag show ./skills/languages/python-pro/SKILL.md
```

## Quality: Judge

### `cyto-skills judge skill <path>`

Score a single skill on 6 weighted axes (structure, trigger, content,
CSO, naming, freshness).

```bash
cyto-skills judge skill ./skills/languages/python-pro [-v|--verbose]
```

| Option | Description |
|--------|-------------|
| `-v, --verbose` | Show per-axis notes and all issues |

Output includes overall score (0-100), verdict (PASS/WARN/FAIL),
visual bar chart, and prioritized recommendations.

**Exit codes**: 0 if PASS or WARN, 1 if FAIL.

### `cyto-skills judge all`

Judge all skills under a root directory.

```bash
cyto-skills judge all [--root <path>] [-v] [--min-score <n>] [--verdict <PASS|WARN|FAIL>]
```

| Option | Description |
|--------|-------------|
| `--root <path>` | Search root (default: cwd) |
| `-v, --verbose` | Show per-axis notes |
| `--min-score <n>` | Only show skills below this score |
| `--verdict <v>` | Filter by verdict: PASS, WARN, or FAIL |

### `cyto-skills judge cytognosis`

Judge all Cytognosis skills across `cytoskeleton/skills/` and
`branding/skills/`.

```bash
cyto-skills judge cytognosis [-v|--verbose]
```

## Quality: Review

### `cyto-skills review collection`

Analyze a skill directory for naming issues, overlaps, and split
candidates.

```bash
cyto-skills review collection [--root <path>]
```

Reports: total skills, average score, PASS/WARN/FAIL counts, naming
issues, overlap groups (Jaccard >= 0.35), and split candidates.

### `cyto-skills review cytognosis`

Review all Cytognosis skills across cytoskeleton + branding repos.

```bash
cyto-skills review cytognosis
```

## Agent Management

### `cyto-skills agent list [agent]`

List installed skills for an agent.

```bash
cyto-skills agent list antigravity
cyto-skills agent list claude
```

**Supported agents**: `antigravity`, `claude`, `agents`, `cursor`,
`kiro`.

### `cyto-skills agent install <skill>`

Install a skill to an agent's skills directory via symlink.

```bash
cyto-skills agent install python-pro [-a antigravity] [--root <path>] [--dry-run]
```

| Option | Default | Description |
|--------|---------|-------------|
| `-a, --agent <id>` | `antigravity` | Target agent |
| `--root <path>` | — | Additional skill search root |
| `--dry-run` | — | Preview without changes |

Searches cytoskeleton, branding, and cytoskills skill directories.

### `cyto-skills agent uninstall <skill>`

Remove a skill from an agent's skills directory.

```bash
cyto-skills agent uninstall python-pro [-a antigravity] [--dry-run]
```

### `cyto-skills agent batch <group>`

Batch install a skill group to one or all agents.

```bash
cyto-skills agent batch cytognosis [-a antigravity] [--all-agents] [--dry-run]
```

| Option | Description |
|--------|-------------|
| `-a, --agent <id>` | Target agent (default: antigravity) |
| `--all-agents` | Install to antigravity, claude, and agents |
| `--dry-run` | Preview without changes |

**Built-in groups**: `cytognosis`, `coding`, `science`, `writing`,
`meta`. Unknown group names are treated as single skill names.

### `cyto-skills agent doctor [agent]`

Health-check an agent's skills directory for broken symlinks,
missing SKILL.md, and memory file status.

```bash
cyto-skills agent doctor antigravity [--fix]
```

| Option | Description |
|--------|-------------|
| `--fix` | Auto-remove broken symlinks |

**Exit codes**: 0 if all healthy, 1 if broken symlinks found.

### `cyto-skills agent doctor-all`

Health-check all known agents in a single run.

```bash
cyto-skills agent doctor-all [--fix]
```

### `cyto-skills agent doctor-desktop`

Health-check the Claude Desktop / Cowork installation.

```bash
cyto-skills agent doctor-desktop
```

Checks: SDK binary, launcher script, desktop config,
spaces.json paths, session configs. See
[module-spec-claude-desktop-doctor.md](module-spec-claude-desktop-doctor.md)
for details.

**Exit codes**: 0 if healthy, 1 if unhealthy.

### `cyto-skills agent fix-launcher`

Install or update the version-agnostic Claude Code launcher script.

```bash
cyto-skills agent fix-launcher [--dry-run]
```

If the launcher is already installed and version-agnostic, reports
no changes needed.

### `cyto-skills agent fix-paths <oldPath> <newPath>`

Fix stale folder paths in Cowork spaces and session configs after a
directory move.

```bash
cyto-skills agent fix-paths ~/Documents/Claude ~/Claude [--dry-run]
```

Replaces all occurrences of `oldPath` with `newPath` in
`spaces.json` and all `local_*.json` session config files. Supports
`~` expansion.

> [!IMPORTANT]
> Restart Claude Desktop after running this command.

### `cyto-skills agent purge-cache`

Purge Electron renderer caches to force re-sync from backend.

```bash
cyto-skills agent purge-cache [--dry-run]
```

Removes: IndexedDB, Local Storage, Session Storage, Cache,
Code Cache, GPUCache.

> [!IMPORTANT]
> Restart Claude Desktop after purging caches.

## Memory Management

### `cyto-skills agent memory <agent>`

Show the full memory file contents for an agent.

```bash
cyto-skills agent memory antigravity
cyto-skills agent memory claude
```

### `cyto-skills agent memory-update <agent> <section>`

Update or append a section in an agent's deployed memory file.

```bash
# From file
cyto-skills agent memory-update claude "Custom Rules" -f rules.md

# From stdin
echo "New content" | cyto-skills agent memory-update antigravity "Notes"
```

| Option | Description |
|--------|-------------|
| `-f, --file <path>` | Read content from file instead of stdin |

### `cyto-skills agent memory-diff [agent]`

Compare source memory (`configs/core_memory/`) with deployed memory
for drift detection.

```bash
# Single agent
cyto-skills agent memory-diff antigravity [--json]

# All agents
cyto-skills agent memory-diff [--json]
```

| Option | Description |
|--------|-------------|
| `--json` | Output as JSON |

Reports: identical, deployed-only (drift), source-only (deploy
needed), and modified sections.

**Exit codes**: 0 if no drift, 1 if drift detected.

### `cyto-skills agent memory-harmonize`

Reconcile deployed-only sections by backporting to source files.

```bash
cyto-skills agent memory-harmonize [--backport] [--dry-run] [--json]
```

| Option | Description |
|--------|-------------|
| `--backport` | Apply the backport changes (default: dry-run) |
| `--dry-run` | Preview without writing (default behavior) |
| `--json` | Output as JSON |

Proposes three action types:
- `backport-shared` — universal sections → `MEMORY.md`
- `backport-agent` — single-agent sections → agent source file
- `needs-review` — sections in some but not all agents

### `cyto-skills agent memory-revision <section>`

Update a memory section in the source files. Determines whether the
section is shared (MEMORY.md) or agent-specific.

```bash
cyto-skills agent memory-revision "Code Standards" -f standards.md [--dry-run]
cyto-skills agent memory-revision "Notes" -c "Updated content" [--dry-run]
echo "Content" | cyto-skills agent memory-revision "Section Name"
```

| Option | Description |
|--------|-------------|
| `-f, --file <path>` | Read content from file |
| `-c, --content <text>` | Section content as string |
| `--dry-run` | Preview without writing |

After updating source, run `cyto-skills deploy-configs` to
propagate changes to deployed files.

### `cyto-skills agent vault-link <repoPath>`

Create or update a symlink from ObsidianVault to a repo's `docs/`
folder.

```bash
cyto-skills agent vault-link ~/repos/cytognosis/cytoskills \
  [--vault-section 03-Engineering] \
  [--vault-root <path>] \
  [--dry-run]
```

| Option | Default | Description |
|--------|---------|-------------|
| `--vault-section` | `03-Engineering` | Vault section subdirectory |
| `--vault-root` | `~/Documents/ObsidianVault` | Vault root path |
| `--dry-run` | — | Preview without creating symlink |

**Exit codes**: 0 on success, 1 on error.

## Catalog Management

### `cyto-skills catalog list`

List all configured third-party skill catalog sources.

```bash
cyto-skills catalog list [--root <path>] [--json]
```

| Option | Description |
|--------|-------------|
| `--root <path>` | Skills root directory (default: cwd) |
| `--json` | Output as JSON |

Scans `third_party/` subdirectory for skill repositories.

### `cyto-skills catalog fetch <source>`

Fetch or update a skill repo from a catalog source.

```bash
# GitHub shorthand
cyto-skills catalog fetch jeffallan/claude-skills [--root <path>] [--dry-run]

# Full URL
cyto-skills catalog fetch https://github.com/org/repo.git

# Local path
cyto-skills catalog fetch /path/to/local/repo
```

| Option | Description |
|--------|-------------|
| `--root <path>` | Skills root directory (default: cwd) |
| `--dry-run` | Preview without cloning |

Clones new repos or runs `git pull --ff-only` on existing ones.

**Exit codes**: 0 on success, 1 on clone/pull failure.

### `cyto-skills catalog diff`

Show skills in catalog sources not yet installed locally.

```bash
cyto-skills catalog diff [--root <path>] [--source <name>] [--json]
```

| Option | Description |
|--------|-------------|
| `--root <path>` | Skills root directory (default: cwd) |
| `--source <name>` | Limit to a specific catalog source |
| `--json` | Output as JSON |

## Global Options

All commands support the standard Commander.js flags:

| Flag | Description |
|------|-------------|
| `--help` | Display help for the command |
| `--version` | Display the CLI version (1.0.0) |
