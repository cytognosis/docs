> **Status**: Active
> **Date**: 2026-06-14
> **Author**: Cytognosis Foundation
> **Audience**: engineers, operators
> **Tags**: `quick-reference`, `deploy`, `cytoskills`

# @cytognosis/cyto-skills-deploy — Quick Reference

> **One line**: Deployment and synchronization utilities for the cytoskills monorepo. Deploys agent configs, syncs editor settings and extensions, syncs brand assets, and creates skill symlinks via profiles.
> **Full doc**: [deploy.md](deploy.md)

---

## Key Concepts

| Term | Definition |
|------|-----------|
| **deploy-configs** | Deploys CLAUDE.md / GEMINI.md / KIRO.md (+ shared MEMORY.md) to user dirs with section-aware merge. |
| **Profile** | YAML file under `profiles/` naming a bundle of skills for a target (agents, claude, antigravity, cursor). Supports inheritance. |
| **sync-skills** | Creates flat symlinks from `skills/` to editor-specific dirs. Dry-run by default. |
| **sync-brand** | One-way copy of branding repo guidelines and assets into `skills/cytognosis/brand/`. Destructive to `references/` and `assets/`. |
| **sync-editors** | Copies `settings.json`/`keybindings.json`/`launch.json` and installs extensions for each configured IDE. |
| **Section-aware merge** | `mergeConfigs` preserves user-specific sections in existing deployed files under `# User-Specific Settings`. |

---

## Modules and Exports

| Module | Key exports |
|--------|-------------|
| `deploy-configs.ts` | `deployConfigs`, `mergeConfigs`, `DeployConfigsOptions` |
| `sync-editors.ts` | `syncEditors` |
| `sync-brand.ts` | `syncBrand` |
| `profiles.ts` | `loadProfile`, `deployProfile`, `syncAll`, `listProfiles`, `Profile`, `DeployResult` |
| `sync-skills.ts` | `syncSkills`, `SyncSkillsOptions` |

---

## Deploy Targets

### deployConfigs targets

| Name | Source | Destination |
|------|--------|-------------|
| `claude` | `configs/core_memory/CLAUDE.md` + MEMORY.md | `~/.claude/CLAUDE.md` |
| `gemini` | `configs/core_memory/GEMINI.md` + MEMORY.md | `~/.gemini/antigravity/GEMINI.md` |
| `kiro` | `configs/core_memory/KIRO.md` + MEMORY.md | `~/.kiro/KIRO.md` |

### syncSkills / Profile targets

| Name | Directory |
|------|----------|
| `antigravity` | `~/.gemini/antigravity/skills` |
| `agents` | `~/.agents/skills` |
| `claude` | `~/.claude/skills` |
| `cursor` | `~/.cursor/skills` |

### syncEditors IDEs

| IDE | CLI | Config dir |
|-----|-----|-----------|
| VS Code | `code` | `~/.config/Code/User` |
| Antigravity | `antigravity` | `~/.config/Antigravity/User` |
| Cursor | `cursor` | `~/.config/Cursor/User` |
| Windsurf | `windsurf` | `~/.codeium/windsurf/user` |
| Positron | `positron` | `~/.positron/User` |

---

## API at a Glance

```typescript
import {
  deployConfigs, mergeConfigs,
  syncEditors, syncBrand,
  loadProfile, deployProfile, syncAll, listProfiles,
  syncSkills,
} from "@cytognosis/cyto-skills-deploy";
```

### deployConfigs

```typescript
await deployConfigs();                           // deploy all targets
await deployConfigs({ targets: ["claude"] });   // deploy only Claude
await deployConfigs({ dryRun: true });          // preview
await deployConfigs({ skipGit: true });         // skip git tracking
```

### Profiles

```typescript
const profiles = listProfiles();                       // ["coding/dev", "science/research-scientist", ...]
const p = loadProfile("science/research-scientist");   // Profile: {name, skills[], target, ...}
const r = await deployProfile("coding/dev");           // DeployResult: {created, skipped, removed, missing}
await syncAll();                                       // deploy every profile in profiles/
await syncAll(true);                                   // clean before deploying
```

### syncSkills

```typescript
await syncSkills();                                    // dry-run (default)
await syncSkills({ execute: true });                   // apply
await syncSkills({ execute: true, clean: true });      // clean + apply
await syncSkills({ execute: true, target: "claude" }); // single target
```

### syncEditors / syncBrand

```typescript
await syncEditors();  // copy configs + install extensions for all found IDEs
await syncBrand();    // pull branding repo into skills/cytognosis/brand/
```

---

## Profile YAML Format

```yaml
name: my-profile
description: Short description
target: agents          # agents | antigravity | claude | cursor
inherit:
  - _base               # inherits skills from _base.yaml
skills:
  - python-pro
  - testing
```

---

## Options

### DeployConfigsOptions

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `targets` | `string[]` | all | Which targets to deploy |
| `dryRun` | `boolean` | `false` | Preview without writing |
| `skipGit` | `boolean` | `false` | Skip git tracking in target dir |

### SyncSkillsOptions

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `execute` | `boolean` | `false` | Apply changes (default: dry-run) |
| `clean` | `boolean` | `false` | Remove all existing entries first |
| `target` | `string` | all | Limit to one target |
| `skillsDir` | `string` | `skills/` | Override skills root |

---

## Common Patterns

```typescript
// Standard deploy sequence after memory update
await deployConfigs({ targets: ["claude"] });

// Full fresh deploy
await syncAll(true);
await deployConfigs();
await syncEditors();

// Dry-run preview before any sync
await syncSkills();            // preview skill links
await deployConfigs({ dryRun: true }); // preview config deploy

// Sync brand assets (branding repo must be sibling or CYTOGNOSIS_BRANDING_DIR set)
await syncBrand();
```

---

## Environment Variables

| Variable | Module | Description |
|----------|--------|-------------|
| `CYTOGNOSIS_BRANDING_DIR` | `sync-brand.ts` | Override path to the branding repo (default: `../branding`) |

---

## Error Quick-Fix

| Error / Symptom | Fix |
|-----------------|-----|
| `MEMORY.md not found` | Ensure `configs/core_memory/MEMORY.md` exists at the repo root |
| `Branding guidelines not found` | Clone cytognosis/branding as a sibling, or set `CYTOGNOSIS_BRANDING_DIR` |
| `Profile 'X' not found` | Run `listProfiles()` or `cyto-skills profile list`; check `profiles/` for the YAML |
| `Profile 'X' is ambiguous` | Multiple YAML files match the name; use a more qualified path like `science/research-scientist` |
| Skills are missing after deploy | Check `DeployResult.missing` for skill names not found in `skills/`; ensure skill dirs have `SKILL.md` |
| `sync-skills` does nothing | Pass `execute: true`; default is dry-run |

---

## See Also

- [Full deploy documentation](deploy.md)
- [Core package quick reference](../core/core-quickref.md)
- [CLI quick reference](../cli/cli-quickref.md) — shell commands for all these operations
- `packages/deploy/src/` — source code
