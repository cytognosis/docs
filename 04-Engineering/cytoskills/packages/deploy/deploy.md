> **Status**: Active
> **Date**: 2026-06-14
> **Author**: Cytognosis Foundation
> **Audience**: engineers, operators
> **Tags**: `deploy`, `cytoskills`, `sync`, `profiles`, `configs`

# @cytognosis/cyto-skills-deploy — Deploy Package

> **Reading time**: ~8 minutes
> **If you only read one thing**: `@cytognosis/cyto-skills-deploy` is the synchronization and deployment layer for the cytoskills monorepo. It handles four operations: deploy agent memory configs, sync editor settings, sync brand skill assets, and create skill symlinks to editor directories.

---

## What It Is and Why

`@cytognosis/cyto-skills-deploy` is the **deployment utility package** of the cytoskills monorepo. The core package (`@cytognosis/cyto-skills`) provides the logic for skills; this package handles the mechanics of moving configurations, skills, and assets out to the right locations on disk.

All four synchronization operations were ported from the original Python implementation (`src/agents/*.py`).

**Package metadata**:

| Field | Value |
|-------|-------|
| npm name | `@cytognosis/cyto-skills-deploy` |
| Version | 1.0.0 |
| Entry point | `dist/index.js` |
| Types | `dist/index.d.ts` |
| Runtime | Node >= 20, ESM |
| Dependencies | `@cytognosis/cyto-skills`, `yaml`, `dotenv` |

---

## Monorepo Position

```
cytoskills/
├── packages/
│   ├── core/          ← provides BaseSkill, DiagnosticResult
│   ├── deploy/        ← THIS PACKAGE — sync/deploy logic
│   └── cli/           → imports deploy, exposes it as commands
├── configs/
│   ├── core_memory/   ← CLAUDE.md, GEMINI.md, KIRO.md, MEMORY.md
│   └── editors/       ← settings.json, keybindings.json per IDE
├── profiles/          ← YAML skill bundles
└── skills/            ← skill directories
```

The deploy package is used directly by the CLI and can also be imported by other TypeScript tooling.

---

## Public API (Modules)

### deploy-configs.ts — Agent Memory Config Deployment

Deploys `CLAUDE.md`, `GEMINI.md`, and `KIRO.md` from `configs/core_memory/` to user-specific directories. Appends the shared `MEMORY.md` to each. Uses a section-aware merge to preserve user-specific sections in existing deployed files.

**Deploy targets**:

| Name | Source file | Destination |
|------|------------|-------------|
| `claude` | `configs/core_memory/CLAUDE.md` | `~/.claude/CLAUDE.md` |
| `gemini` | `configs/core_memory/GEMINI.md` | `~/.gemini/antigravity/GEMINI.md` |
| `kiro` | `configs/core_memory/KIRO.md` | `~/.kiro/KIRO.md` |

**Merge strategy**:

The `mergeConfigs(existing, newContent)` function compares heading-normalized sections. Sections in the existing deployed file that are not present in the new config are preserved under a `# User-Specific Settings` block appended at the end. This prevents local agent customizations from being overwritten.

**Git tracking**: By default, `deployConfigs` initializes a git repo in the target directory (e.g., `~/.claude/`) and commits before and after deployment. Pass `skipGit: true` to disable.

**Key exports**:

| Export | Signature | Purpose |
|--------|-----------|---------|
| `deployConfigs(options?)` | `Promise<void>` | Deploy agent configs to all or selected targets. |
| `mergeConfigs(existing, new)` | `string` | Merge new config over existing, preserving user sections. |
| `DeployConfigsOptions` | interface | `{ targets?: string[], dryRun?: boolean, skipGit?: boolean }` |

**`DeployConfigsOptions`**:

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `targets` | `string[]` | all | Array of target names to deploy (`claude`, `gemini`, `kiro`). |
| `dryRun` | `boolean` | `false` | Preview what would be written without writing. |
| `skipGit` | `boolean` | `false` | Skip git init and commit in the target directory. |

---

### sync-editors.ts — IDE Configuration Sync

Copies `settings.json`, `keybindings.json`, and `launch.json` from `configs/editors/{ide}/` to each IDE's user config directory. Also installs VS Code-compatible extensions via the IDE's CLI.

**Supported IDEs**:

| IDE | CLI command | Config directory |
|-----|------------|-----------------|
| VS Code | `code` | `~/.config/Code/User` |
| Antigravity | `antigravity` | `~/.config/Antigravity/User` |
| Cursor | `cursor` | `~/.config/Cursor/User` |
| Windsurf | `windsurf` | `~/.codeium/windsurf/user` |
| Positron | `positron` | `~/.positron/User` |

The function skips any IDE for which no `configs/editors/{ide}/` directory exists. Extension installation is skipped silently if the IDE CLI is not found on `$PATH`.

**Key exports**:

| Export | Signature | Purpose |
|--------|-----------|---------|
| `syncEditors()` | `Promise<void>` | Copy configs and install extensions for all configured IDEs. |

The `CYTOGNOSIS_BRANDING_DIR` environment variable is not used by `syncEditors`.

---

### sync-brand.ts — Brand Skill Sync

Copies brand guideline Markdown files and assets from the sibling `cytognosis/branding` repository into `skills/cytognosis/brand/` in the cytoskills repo.

**What it syncs**:

- `SKILL.tpl.md` → `skills/cytognosis/brand/SKILL.md` (template → deployed manifest)
- `branding/guidelines/0*.md` → `skills/cytognosis/brand/references/` (numbered guideline files)
- `branding/assets/**` → `skills/cytognosis/brand/assets/` (logos, tokens, design assets)

The sync is **destructive**: it wipes and recreates `references/` and `assets/` each run for a clean state.

**Environment variable**:

| Variable | Default | Description |
|----------|---------|-------------|
| `CYTOGNOSIS_BRANDING_DIR` | `../branding` (sibling of cytoskills) | Override path to the branding repo. |

**Key exports**:

| Export | Signature | Purpose |
|--------|-----------|---------|
| `syncBrand()` | `Promise<void>` | Pull brand assets from the branding repo into `skills/cytognosis/brand/`. |

---

### profiles.ts — Profile Loader and Deployer

Loads YAML profiles from `profiles/` (with inheritance resolution), discovers skill directories under `skills/`, and creates symlinks in editor-specific target directories.

**Profile YAML format**:

```yaml
name: my-profile
description: Skills for X use case
target: agents          # or: claude, antigravity, cursor
inherit:
  - _base               # inherits skills from _base.yaml first
skills:
  - python-pro
  - testing
  - my-custom-skill
```

**Profile resolution**: `inherit` is processed depth-first, deduplicated in order. A profile that inherits from `_base` and adds its own skills will result in `base_skills + own_skills` (deduped).

**Target directory mapping**:

| Target name | Directory |
|-------------|----------|
| `agents` | `~/.agents/skills` |
| `antigravity` | `~/.gemini/antigravity/skills` |
| `claude` | `~/.claude/skills` |
| `cursor` | `~/.cursor/skills` |

**Key exports**:

| Export | Signature | Purpose |
|--------|-----------|---------|
| `loadProfile(name)` | `Profile` | Load and resolve a profile (with inheritance). |
| `deployProfile(name, clean?, targetOverride?, dryRun?)` | `Promise<DeployResult>` | Create skill symlinks for a profile. |
| `syncAll(clean?)` | `Promise<void>` | Deploy all profiles found in `profiles/`. |
| `listProfiles()` | `string[]` | List all profile names (recursive under `profiles/`, excluding `_`-prefixed files). |
| `Profile` | interface | `{name, description, target, skills, inherit, sourceFile}` |
| `DeployResult` | interface | `{created, skipped, removed, missing}` |

---

### sync-skills.ts — Skill Symlink Sync

Creates flat symlinks from every skill directory under `skills/` into the Antigravity and shared-agents directories. Removes broken and stale symlinks on each run.

**Sync targets** (hardcoded):

| Name | Directory |
|------|----------|
| `antigravity` | `~/.gemini/antigravity/skills` |
| `agents` | `~/.agents/skills` |

The `--target` option on the CLI narrows to a single target.

**Key exports**:

| Export | Signature | Purpose |
|--------|-----------|---------|
| `syncSkills(options?)` | `Promise<void>` | Sync skill symlinks to editor directories. |
| `SyncSkillsOptions` | interface | `{execute?, clean?, target?, skillsDir?}` |

**`SyncSkillsOptions`**:

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `execute` | `boolean` | `false` | Apply changes (default: dry-run). |
| `clean` | `boolean` | `false` | Remove all existing entries before sync. |
| `target` | `string` | all | Limit to a single target name. |
| `skillsDir` | `string` | `skills/` under repo root | Override the skills directory to scan. |

---

## Usage Examples

### Example 1: Deploy agent configs programmatically

```typescript
import { deployConfigs } from "@cytognosis/cyto-skills-deploy";

// Deploy only Claude, dry-run
await deployConfigs({ targets: ["claude"], dryRun: true });

// Deploy all targets
await deployConfigs();
```

### Example 2: Deploy a profile

```typescript
import { deployProfile, loadProfile } from "@cytognosis/cyto-skills-deploy";

// Inspect before deploying
const profile = loadProfile("science/research-scientist");
console.log(`${profile.skills.length} skills → ${profile.target}`);

// Deploy
const result = await deployProfile("science/research-scientist", false, "", false);
console.log(`Created: ${result.created}, Missing: ${result.missing.join(", ")}`);
```

### Example 3: Sync all skills (dry-run first)

```typescript
import { syncSkills } from "@cytognosis/cyto-skills-deploy";

// Dry-run
await syncSkills({ execute: false });

// Apply
await syncSkills({ execute: true });
```

---

## Architecture Notes

- `deploy-configs.ts` resolves the repo root by walking up from `import.meta.dirname`. It expects `configs/core_memory/MEMORY.md` to exist at the repo root.
- `profiles.ts` uses synchronous filesystem calls in several places (profile YAML loading, skill discovery) for simplicity during startup.
- `sync-brand.ts` requires the `cytognosis/branding` repo to be cloned as a sibling of `cytoskills`, unless `CYTOGNOSIS_BRANDING_DIR` is set.
- `sync-skills.ts` defaults to dry-run (no `--execute`). The CLI mirrors this: `cyto-skills sync-skills` is always dry-run without `--execute`.
- All four sync operations are idempotent: running them twice has the same effect as running once (broken symlinks removed, correct symlinks skipped).

---

## Reference Index

| Module | File |
|--------|------|
| Deploy configs | `packages/deploy/src/deploy-configs.ts` |
| Sync editors | `packages/deploy/src/sync-editors.ts` |
| Sync brand | `packages/deploy/src/sync-brand.ts` |
| Profiles | `packages/deploy/src/profiles.ts` |
| Sync skills | `packages/deploy/src/sync-skills.ts` |
| Public index | `packages/deploy/src/index.ts` |

- Quick reference: [deploy-quickref.md](deploy-quickref.md)
- CLI commands for this package: [../cli/cli.md](../cli/cli.md)
- Core library: [../core/core.md](../core/core.md)
