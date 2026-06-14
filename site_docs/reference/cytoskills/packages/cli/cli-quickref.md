> **Status**: Active
> **Date**: 2026-06-14
> **Author**: Cytognosis Foundation
> **Audience**: engineers, operators
> **Tags**: `quick-reference`, `cli`, `cyto-skills`

# @cytognosis/cyto-skills-cli — Quick Reference

> **One line**: `cyto-skills` is the shell interface to the entire cytoskills ecosystem. List, judge, tag, deploy profiles, sync editors, and manage agent memories.
> **Full doc**: [cli.md](cli.md)

---

## Key Concepts

| Term | Definition |
|------|-----------|
| **Profile** | YAML file under `profiles/` defining a bundled skill list for a use case. Supports inheritance. |
| **Judge** | Quality scorer (6 axes, 0–100, PASS/WARN/FAIL). Run before committing a new skill. |
| **Review** | Collection-level analysis: naming conflicts, Jaccard vocab overlap, split candidates. |
| **Tag** | Assigns CSO CURIE terms to a skill via `.cyto-tags.yaml` sidecar, then promotes to frontmatter. |
| **deploy-configs** | Deploys `CLAUDE.md` / `GEMINI.md` from `configs/core_memory/` to `~/.claude/` / `~/.gemini/antigravity/`. |
| **sync-skills** | Creates flat symlinks from `skills/` to editor-specific directories (antigravity, agents). Dry-run by default. |
| **memory-diff** | Detects sections present in deployed memory but missing from source (drift). |

---

## Command Groups

| Group | Base command |
|-------|-------------|
| Skill discovery | `list`, `inspect`, `classify`, `root` |
| Quality | `judge skill/all/cytognosis`, `review collection/cytognosis` |
| Tagging | `tag skill/all/promote/show` |
| Ontology | `ontology list/search/expand/mappings/validate` |
| Profiles | `profile list/show/deploy` |
| Deploy/sync | `deploy-configs`, `sync-editors`, `sync-brand`, `sync-skills`, `sync-all` |
| Agent mgmt | `agent list/install/batch/doctor/doctor-desktop/memory/memory-diff/...` |
| Catalog | `catalog list/fetch/diff` |

---

## Commands

### Skill Discovery

| Command | What It Does |
|---------|-------------|
| `cyto-skills list [--root <path>]` | List all discoverable skills with CSO tags |
| `cyto-skills inspect <skillDir>` | Print name, description, tags, IO, scripts, references |
| `cyto-skills classify <skillDir>` | Print CSO CURIEs for a skill |
| `cyto-skills doctor <skillDir>` | Run diagnostics (exits 1 if unhealthy) |
| `cyto-skills validate <file>` | Validate a JSONL file |
| `cyto-skills synthesize [--root <path>]` | Find overlapping skill clusters |

### Judge

| Command | What It Does |
|---------|-------------|
| `cyto-skills judge skill <path> [-v] [--tag]` | Score one skill |
| `cyto-skills judge all [--root] [--min-score] [--verdict]` | Score all under a root |
| `cyto-skills judge cytognosis [-v] [--roots]` | Score Cytognosis skills |

### Review

| Command | What It Does |
|---------|-------------|
| `cyto-skills review collection [--root]` | Naming, overlap, split analysis |
| `cyto-skills review cytognosis` | Same for cytoskeleton + branding |

### Tag

| Command | What It Does |
|---------|-------------|
| `cyto-skills tag skill <path> [--dry-run] [--confidence]` | Write `.cyto-tags.yaml` |
| `cyto-skills tag all [--root] [--dry-run]` | Tag all SKILL.md files |
| `cyto-skills tag promote <path> [--dry-run] [--confidence]` | Merge sidecar into frontmatter |
| `cyto-skills tag show <path>` | Print sidecar contents |

### Ontology

| Command | What It Does |
|---------|-------------|
| `cyto-skills ontology list [--axis A|B|C|meta]` | List CSO terms |
| `cyto-skills ontology search <query>` | Full-text search |
| `cyto-skills ontology expand cso:Python` | Get full IRI |
| `cyto-skills ontology mappings cso:Python` | Show SSSOM mappings |
| `cyto-skills ontology validate cso:Python` | Check CURIE validity |

### Profiles

| Command | What It Does |
|---------|-------------|
| `cyto-skills profile list` | List YAML profiles |
| `cyto-skills profile show <name>` | Show resolved skill list |
| `cyto-skills profile deploy <name> [--clean] [--target] [--dry-run]` | Deploy symlinks |

### Deploy / Sync

| Command | What It Does |
|---------|-------------|
| `cyto-skills deploy-configs [--dry-run] [--target claude|gemini]` | Deploy agent configs |
| `cyto-skills sync-skills [--execute] [--clean] [--target]` | Sync skill symlinks (dry-run by default) |
| `cyto-skills sync-all [--clean]` | Deploy all profiles |
| `cyto-skills sync-editors` | Sync editor settings |
| `cyto-skills sync-brand` | Sync brand skill |

### Agent

| Command | What It Does |
|---------|-------------|
| `cyto-skills agent list [agent]` | List installed skills |
| `cyto-skills agent install <skill> [-a agent] [--dry-run]` | Install skill |
| `cyto-skills agent batch <group> [-a agent] [--all-agents]` | Batch install group |
| `cyto-skills agent uninstall <skill> [-a agent]` | Remove skill |
| `cyto-skills agent doctor [agent] [--fix]` | Health check |
| `cyto-skills agent doctor-all [--fix]` | Check all agents |
| `cyto-skills agent doctor-desktop` | Check Claude Desktop |
| `cyto-skills agent fix-launcher [--dry-run]` | Install version-agnostic launcher |
| `cyto-skills agent fix-paths <old> <new> [--dry-run]` | Fix stale paths after folder move |
| `cyto-skills agent purge-cache [--dry-run]` | Purge Electron caches |
| `cyto-skills agent memory <agent>` | Print memory file |
| `cyto-skills agent memory-update <agent> <section> [-f file]` | Upsert section |
| `cyto-skills agent memory-diff [agent] [--json]` | Detect memory drift |
| `cyto-skills agent memory-harmonize [--backport] [--json]` | Backport deployed sections |
| `cyto-skills agent memory-revision <section> [-f file] [-c text]` | Update section in source |
| `cyto-skills agent vault-link <repoPath> [--vault-section]` | Link docs/ to Obsidian |

### Catalog

| Command | What It Does |
|---------|-------------|
| `cyto-skills catalog list [--root] [--json]` | List third-party sources |
| `cyto-skills catalog fetch <org/repo>` | Clone / pull a skill repo |
| `cyto-skills catalog diff [--source] [--json]` | Skills in catalog not installed locally |

---

## Common Patterns

```bash
# Full tagging + judging workflow
cyto-skills tag skill skills/my-skill/SKILL.md
cyto-skills tag promote skills/my-skill/SKILL.md
cyto-skills judge skill skills/my-skill -v

# Deploy configs after memory change
cyto-skills agent memory-harmonize --backport
cyto-skills deploy-configs

# Sync skills to all editors
cyto-skills sync-skills --execute

# Install cytognosis group to Claude
cyto-skills agent batch cytognosis -a claude

# Claude Desktop health check
cyto-skills agent doctor-desktop
cyto-skills agent fix-launcher

# Check memory drift for all agents
cyto-skills agent memory-diff
```

---

## Options at a Glance

| Option | Commands | Meaning |
|--------|----------|---------|
| `--dry-run` | Most mutating commands | Preview without writing |
| `-v, --verbose` | `judge skill/all` | Show per-axis breakdown |
| `--clean` | `profile deploy`, `sync-skills`, `sync-all` | Remove existing entries first |
| `--execute` | `sync-skills` | Apply (default is dry-run) |
| `-a, --agent <id>` | `agent install/batch/uninstall` | Target agent (default: antigravity) |
| `--all-agents` | `agent batch` | Install to antigravity + claude + agents |
| `--tag` | `judge skill` | Run tagger before scoring |
| `--json` | `catalog list/diff`, `agent memory-diff/harmonize` | Machine-readable output |
| `--backport` | `agent memory-harmonize` | Apply backport changes |
| `--root <path>` | `list`, `synthesize`, `judge all`, `sync-skills` | Override search/source root |

---

## Error Quick-Fix

| Error / Symptom | Fix |
|-----------------|-----|
| `No skills found in search roots` | Pass `--root` pointing to a directory that contains phase subdirs, or set `CYTO_SKILLS_ROOT` |
| `Profile 'X' not found` | Run `cyto-skills profile list` to see available profiles |
| `Unknown agent: X` | Valid IDs: `antigravity`, `claude`, `agents`, `cursor`, `kiro` |
| `sync-skills` does nothing | Default is dry-run; pass `--execute` to apply |
| Judge CSO axis is 0 | Re-run with `--tag` or run `cyto-skills tag skill <path> && cyto-skills tag promote <path>` manually |
| `deploy-configs` writes wrong sections | Run `memory-diff` first to see what will merge, then deploy |

---

## See Also

- [Full CLI documentation](cli.md)
- [Core package quick reference](../core/core-quickref.md) — programmatic API
- [Deploy package quick reference](../deploy/deploy-quickref.md) — deploy/sync functions
