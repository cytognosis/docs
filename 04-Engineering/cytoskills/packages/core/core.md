> **Status**: Active
> **Date**: 2026-06-14
> **Author**: Cytognosis Foundation
> **Audience**: engineers, contributors, integrators
> **Tags**: `core`, `cytoskills`, `skill-management`, `ontology`, `api-reference`

# @cytognosis/cyto-skills — Core Package

> **Reading time**: ~12 minutes
> **If you only read one thing**: `@cytognosis/cyto-skills` is the programmatic heart of the cytoskills monorepo. It owns the full lifecycle: parse SKILL.md manifests, discover skills across phase repositories, classify them against the CSO ontology, judge quality, review collections, tag with sidecars, and manage agent installations and memory.

---

## What It Is and Why

`@cytognosis/cyto-skills` is the **core library package** of the cytoskills monorepo. All other packages (`cli`, `deploy`) depend on it. It provides every data structure, algorithm, and filesystem operation needed to work with skills programmatically.

Skills in the Cytognosis ecosystem are directories containing a `SKILL.md` file with YAML frontmatter. The core package defines what a valid skill looks like, how to find them across the multi-repository layout, how to score and classify them, and how to install and maintain them for specific AI agent runtimes.

**When to import this package**:

- Building tooling that reads, validates, or transforms SKILL.md files.
- Classifying skills against the Cyto Skill Ontology (CSO).
- Running quality scores (judge) or collection audits (reviewer).
- Installing or managing skills for a specific agent (claude, antigravity, cursor, kiro).
- Reading, writing, or harmonizing agent memory files.

**Package metadata**:

| Field | Value |
|-------|-------|
| npm name | `@cytognosis/cyto-skills` |
| Version | 1.0.0 |
| Entry point | `dist/index.js` |
| Types | `dist/index.d.ts` |
| License | Apache-2.0 |
| Runtime | Node >= 20, ESM |
| Registry | Cytognosis private npm (GCP Artifact Registry) |

---

## Monorepo Position

```
cytoskills/
├── packages/
│   ├── core/          ← THIS PACKAGE — all logic, types, and algorithms
│   ├── cli/           → imports @cytognosis/cyto-skills, exposes commands
│   └── deploy/        → imports @cytognosis/cyto-skills, provides sync helpers
├── skills/            ← skill directories consumed by this package
├── profiles/          ← YAML skill bundles consumed by deploy
└── configs/           ← core_memory/ files consumed by agent.ts
```

The core package has no monorepo siblings as dependencies. Everything else in the repo depends on it.

---

## Public API (Modules)

### manifest.ts — SKILL.md Parsing and Validation

The manifest module owns the Zod schemas for `SKILL.md` frontmatter and the `BaseSkill` class.

**Key exports**:

| Export | Type | Purpose |
|--------|------|---------|
| `BaseSkill` | class | Wraps a parsed skill directory. Main handle for all skill operations. |
| `SkillFrontmatterSchema` | Zod schema | Validates frontmatter against the full spec (name, description, tags, inputs, outputs, edam, agent_compat, ...). |
| `SkillIOSchema` | Zod schema | Validates a single IO slot. Requires `namespace:Type` form for schema references. |
| `EdamMetadataSchema` | Zod schema | Optional EDAM/biotoolsSchema alignment metadata. |
| `AgentCompatSchema` | Zod schema | Agent runtime compatibility (runtimes, mcp_servers, min_context). |
| `CSOAxisTagSchema` | Zod schema | Structured CSO tag with primary CURIE, confidence, intent, apqc_code. |
| `parseSkillMd(text)` | function | Parse raw SKILL.md text into `{frontmatter, body}`. |

**`BaseSkill` methods**:

| Method / Property | Returns | Notes |
|-------------------|---------|-------|
| `BaseSkill.load(skillDir)` | `Promise<BaseSkill>` | Static factory. Reads `SKILL.md` from directory. |
| `new BaseSkill(skillDir, text)` | `BaseSkill` | Synchronous constructor for pre-loaded text. |
| `.name` | `string` | Frontmatter `name`. |
| `.description` | `string` | Frontmatter `description`. |
| `.tags` | `string[]` | Flat tag list. For structured CSO tags, extracts primary CURIEs. |
| `.structuredTags` | `StructuredTagsSchema \| undefined` | Raw CSO axes object, or undefined for flat tags. |
| `.inputs` / `.outputs` | `SkillIO[]` | IO slot definitions. |
| `.dirName` | `string` | Directory basename. |
| `.scripts()` | `Promise<string[]>` | Files in `scripts/` subdirectory. |
| `.references()` | `Promise<string[]>` | Files in `references/` subdirectory. |

---

### loader.ts — Multi-Repository Skill Discovery

The loader maps 15 named **phase directories** across the cytoskills/cytoskeleton/branding multi-repo layout and provides two discovery functions.

**Phase directories** (canonical names → relative paths from a search root):

| Phase | Relative path | Contents |
|-------|--------------|----------|
| `cytognosis` | `cytoskills/skills/cytognosis` | Cytognosis production skills |
| `brand` | `branding/skills` | Brand skills |
| `universal` | `cytoskeleton/skills/universal` | Universal meta skills |
| `dev-language` | `cytoskills/skills/languages` | Language skills (Python, TypeScript, etc.) |
| `dev-ai-ml` | `cytoskills/skills/ai-ml` | AI/ML skills |
| `community` | `cytoskills/skills/community` | Namespaced third-party skills |
| `third-party` | `cytoskills/third_party` | Raw git submodules |
| *(+ 8 others)* | — | See `PHASE_DIRS` in source |

**Key exports**:

| Export | Purpose |
|--------|---------|
| `discoverSkill(name, searchRoots)` | Find a single skill by name across all phases. |
| `iterSkills(searchRoots)` | Load all skills across all phases. Throws `SkillLoadError` if any skill fails to parse. |
| `PHASE_DIRS` | The full phase-to-path mapping (a `Record<string, string>`). |
| `SkillLoadError` | Error class with optional `skillPath` property. |

The `CYTO_SKILLS_ROOT` environment variable prepends an additional search root, overriding the default layout.

---

### classifier.ts — CSO Keyword Classification

The classifier assigns CSO CURIEs to skills using rule-based keyword matching against an inline taxonomy that mirrors the CSO TTL ontology.

**CSO axes in the classifier taxonomy**:

| Axis | Parent CURIE | Examples |
|------|-------------|---------|
| A — Software Engineering | `cso:SpecializedCoding`, `cso:GeneralCoding` | `cso:Python`, `cso:TypeScript`, `cso:DevOps` |
| B — Scientific Domains | `cso:Bioinformatics`, `cso:AIMl` | `cso:SingleCellAnalysis`, `cso:LLMs` |
| C — Organizational/Meta | `cso:GeneralMeta`, `cso:LiteratureReview` | `cso:Planning`, `cso:Writing` |

**Key exports**:

| Export | Purpose |
|--------|---------|
| `classify(skill)` | Returns `string[]` of CSO CURIEs for a single skill. Deduplicates; prefers children over parents. |
| `classifyAll(skills)` | Returns `Map<string, string[]>` of skill-name → CURIEs. |
| `clusterByCso(skills)` | Returns `Map<string, BaseSkill[]>` grouped by primary CSO term. |
| `csoLabel(curie)` | Converts `cso:Python` → `"Python"`. |
| `CSO_LABELS` | Full CURIE → label mapping record. |

---

### ontology.ts — CSO Registry

The `OntologyRegistry` class loads the bundled CSO JSON-LD and SSSOM TSV data at construction time (no network calls).

**Key exports**:

| Export | Purpose |
|--------|---------|
| `OntologyRegistry` | Class. Loads CSO data bundles from `src/cso-data/`. |
| `registry` | Singleton instance. Used by `SkillTagger`. |
| `CSOTerm` | Interface: `{iri, curie, label, axis, parents, aliases, wikidataIRI, apqcCode}`. |
| `SSSOMRow` | Interface: one SSSOM mapping row. |
| `TagScore` | Interface: `{curie, label, score, axis}`. |

**`OntologyRegistry` methods**:

| Method | Returns | Notes |
|--------|---------|-------|
| `getTerm(curie)` | `CSOTerm \| undefined` | Look up a term by CURIE. |
| `validate(curie)` | `boolean` | Check if a CURIE exists in the CSO. |
| `expand(curie)` | `string \| null` | Expand CURIE to full IRI. |
| `list(axis?)` | `CSOTerm[]` | All terms, optionally filtered by axis (A/B/C/meta). |
| `search(query)` | `CSOTerm[]` | Full-text search across labels and aliases. |
| `getMappings(curie)` | `SSSOMRow[]` | SSSOM cross-ontology mappings for a term. |
| `scoreTermMatch(keywords, opts)` | `TagScore[]` | Score keyword list against the CSO. Used by `SkillTagger`. |
| `.size` | `number` | Total terms loaded. |

---

### tagger.ts — CSO Sidecar Tagging

The `SkillTagger` class writes `.cyto-tags.yaml` sidecar files next to `SKILL.md` and can promote high-confidence tags into frontmatter.

**Sidecar format** (`.cyto-tags.yaml`):

```yaml
version: "0.1"
tagged_date: "2026-06-14"
tagged_by: auto
tags:
  use_case:
    primary: cso:Construction
    confidence: 0.91
  org_function:
    primary: cso:ManageIT
    apqc_code: "8.0"
    confidence: 0.78
  domain:
    primary: cso:FastAPI
    language: cso:Python
    confidence: 0.95
  github_topics: [fastapi, python, rest-api]
  intent: [feature, scripting]
mappings:
  cso:Construction:
    - {predicate: skos:closeMatch, object: acm:..., label: "..."}
```

**`SkillTagger` methods**:

| Method | Returns | Notes |
|--------|---------|-------|
| `new SkillTagger(options?)` | `SkillTagger` | Options: `confidenceThreshold` (default 0.5), `dryRun`. |
| `.tag(skillPath)` | `CytoTags \| null` | Read skill, score against CSO, write sidecar. |
| `.read(skillPath)` | `CytoTags \| null` | Read existing sidecar. |
| `.promote(skillPath, threshold?)` | `boolean` | Merge high-confidence sidecar tags into SKILL.md frontmatter. Default threshold: 0.7. |

---

### judge.ts — Skill Quality Scoring

The judge scores a single `SKILL.md` across 6 weighted axes and emits a structured report.

**Scoring axes**:

| Axis | Weight | What it checks |
|------|--------|----------------|
| `structure` | 20% | Frontmatter completeness (name, description, author, license, version), body length, H2 sections |
| `trigger` | 25% | Trigger language in description, quoted trigger keywords, routing guidance |
| `content` | 25% | Decision Tree, References section, guardrail (NEVER) rules, code blocks or tables |
| `cso` | 10% | Presence and validity of structured CSO tags (use_case, org_function, domain) |
| `naming` | 10% | Kebab-case slug, slug length ≤ 40 chars, slug matches frontmatter `name` |
| `freshness` | 10% | Version field, status field, `last_revised` date not older than 6 months |

**Verdicts**: PASS (≥ 70), WARN (50–69), FAIL (< 50).

**Key exports**:

| Export | Purpose |
|--------|---------|
| `judgeSkill(skillPath)` | Score a single skill. Returns `JudgeReport`. |
| `judgeAll(root)` | Walk a directory, judge all skills, return sorted by score. |
| `formatJudgeReport(report, verbose?)` | Format report as human-readable string with progress bars. |
| `JudgeReport` | Interface: `{skillPath, skillName, overall, verdict, axes, recommendations, issues}`. |
| `AxisScore` | Interface: `{axis, score, weight, notes}`. |
| `Verdict` | `"PASS" | "WARN" | "FAIL"` |

---

### reviewer.ts — Collection Analysis

The reviewer scans a directory of skills, runs judge on all of them, and produces a `CollectionReview` identifying naming problems, vocabulary overlaps (Jaccard ≥ 0.35), and oversized split candidates.

**Key exports**:

| Export | Purpose |
|--------|---------|
| `reviewCollection(root)` | Full analysis. Returns `CollectionReview`. |
| `formatCollectionReview(review)` | Human-readable summary string. |
| `CollectionReview` | Interface: `{totalSkills, avgScore, issues, namingIssues, overlapGroups, splitCandidates, scoreSummary}`. |
| `ReviewIssue` | Interface: `{type, severity, skills, message, recommendation}`. |

---

### synthesizer.ts — Skill Consolidation Reports

The synthesizer clusters skills by their primary classifier tag and generates consolidation proposals for clusters of size ≥ 2.

**Key exports**:

| Export | Purpose |
|--------|---------|
| `synthesize(skills)` | Returns `ConsolidationReport[]` for all overlapping clusters. |
| `clusterByTaxonomy(skills)` | Returns `SkillCluster[]` — grouped by primary CSO tag. |
| `generateReport(cluster)` | Returns a single `ConsolidationReport` with proposed name and merged triggers. |

---

### doctor.ts — Diagnostic Framework

The doctor module provides a reusable diagnostic result accumulator, JSONL validation utilities, and skill-specific diagnostics.

**Key exports**:

| Export | Purpose |
|--------|---------|
| `DiagnosticResult` | Class. Accumulates errors/warnings/info. `.formatReport()` returns Markdown. |
| `diagnoseSkill(skillDir)` | Check SKILL.md integrity: frontmatter, tags, triggers, IO schemas, body. |
| `diagnoseAll(searchRoots)` | Diagnose all skills across search roots. |
| `parseJsonl(filePath)` | Parse JSONL with error recovery. Returns `JsonlEntry[]`. |
| `validateJsonl(filePath)` | Validate JSONL for duplicate UUIDs and orphaned parent references. |

---

### agent.ts — Agent Installation and Memory Management

The agent module manages skill installation as symlinks into agent-specific directories, and reads/writes agent memory files.

**Supported agents**:

| Agent ID | Label | Skills dir | Memory file |
|----------|-------|-----------|------------|
| `claude` | Claude Code / Cowork | `~/.claude/skills` | `~/.claude/CLAUDE.md` |
| `antigravity` | Antigravity (Google Gemini IDE) | `~/.gemini/antigravity/skills` | `~/.gemini/antigravity/GEMINI.md` |
| `agents` | Shared agents | `~/.agents/skills` | `~/.agents/AGENTS.md` |
| `cursor` | Cursor | `~/.cursor/skills` | `~/.cursor/CURSOR.md` |
| `kiro` | Kiro (AWS) | `~/.kiro/skills` | `~/.kiro/KIRO.md` |

**Key exports**:

| Export | Purpose |
|--------|---------|
| `AGENTS` | Record of all agent configurations. |
| `installSkill(agent, skillName, searchRoots, opts)` | Install a skill to an agent via symlink. Returns `InstallResult`. |
| `uninstallSkill(agent, skillName, opts)` | Remove a skill from an agent. |
| `batchInstall(agent, group, searchRoots, opts)` | Install a named skill group. Built-in groups: `cytognosis`, `coding`, `science`, `writing`, `meta`. |
| `doctorAgent(agent)` | Check for broken/stale symlinks and missing memory file. Returns `DoctorResult`. |
| `fixDoctor(agent)` | Remove broken symlinks found by `doctorAgent`. |
| `listInstalledSkills(agent)` | Return sorted list of installed skill names. |
| `readMemory(agent)` | Read the agent's memory file. |
| `writeMemory(agent, content)` | Overwrite the agent's memory file. |
| `upsertMemorySection(agent, heading, content)` | Upsert a `## Heading` section in the memory file. |
| `memoryDiff(agent)` | Compare source `configs/core_memory/` with deployed memory. Returns `MemoryDiffResult`. |
| `memoryDiffAll()` | Run `memoryDiff` for all agents with deployed memory files. |
| `memoryHarmonize(opts)` | Propose (and optionally apply) backport of deployed-only sections. |
| `memoryRevision(heading, content, opts)` | Update a section in source files. |
| `createVaultLink(repoPath, opts)` | Symlink a repo's `docs/` into the ObsidianVault. |

---

### claude-desktop-doctor.ts — Claude Desktop Diagnostics

This module diagnoses and repairs issues specific to the Claude Desktop / Cowork installation: SDK binary resolution across apt-versioned directories, version-agnostic launcher scripts, Cowork `spaces.json` path validation, and Electron renderer cache management.

**Key exports**:

| Export | Purpose |
|--------|---------|
| `doctorClaudeDesktop()` | Full diagnostic. Returns `ClaudeDesktopDiagnostic`. |
| `checkLauncher()` | Check launcher script status. |
| `fixClaudeDesktopLauncher()` | Install version-agnostic launcher to `~/.local/bin/claude`. |
| `launcherScriptContent` | The canonical launcher script string. |
| `findSpacesJson()` | Locate `spaces.json` on disk. |
| `validateSpaces(spacesPath)` | Check for stale folder paths in spaces. |
| `fixStaleSpacePaths(oldPath, newPath)` | Rewrite stale paths in `spaces.json`. |
| `fixSessionConfigs(oldPath, newPath)` | Rewrite stale paths in session config files. |
| `purgeElectronCache()` | Remove Electron renderer caches (IndexedDB, Local Storage, etc.). |

---

## Usage Examples

### Example 1: Load and classify skills from a custom root

```typescript
import { iterSkills, classify, csoLabel } from "@cytognosis/cyto-skills";

const skills = await iterSkills(["/home/user/repos/my-skills"]);
for (const skill of skills) {
  const tags = classify(skill);
  console.log(`${skill.name}: ${tags.map(csoLabel).join(", ")}`);
}
```

### Example 2: Judge a skill and print the report

```typescript
import { judgeSkill, formatJudgeReport } from "@cytognosis/cyto-skills";

const report = judgeSkill("/home/user/skills/my-skill");
console.log(formatJudgeReport(report, true)); // verbose = true
if (report.verdict === "FAIL") process.exit(1);
```

### Example 3: Install the cytognosis skill group to Claude

```typescript
import { batchInstall } from "@cytognosis/cyto-skills";

const result = await batchInstall("claude", "cytognosis", [
  "/home/user/repos/cytognosis/cytoskeleton/skills",
  "/home/user/repos/cytognosis/branding/skills",
]);
for (const r of result.results) {
  console.log(`[${r.action}] ${r.skill}`);
}
```

---

## Architecture Notes

- All imports use `.js` extensions (ESM, TypeScript `module: NodeNext`).
- The `ontology.ts` module bundles CSO data from `src/cso-data/` at build time (copied to `dist/cso-data/`).
- `agent.ts` resolves the cytoskills repo root by looking for `configs/core_memory/MEMORY.md` in candidate paths.
- The `doctor.ts` JSONL utilities are adapted from the cowork-session-doctor pattern and are reusable outside the skill context.
- Tag axis letters: Axis A = use-case (what the skill does), Axis B = org function (APQC alignment), Axis C = domain/technology.

---

## Reference Index

| Module | File |
|--------|------|
| Manifest / BaseSkill | `packages/core/src/manifest.ts` |
| Loader / discovery | `packages/core/src/loader.ts` |
| Classifier | `packages/core/src/classifier.ts` |
| Ontology registry | `packages/core/src/ontology.ts` |
| Tagger | `packages/core/src/tagger.ts` |
| Judge | `packages/core/src/judge.ts` |
| Reviewer | `packages/core/src/reviewer.ts` |
| Synthesizer | `packages/core/src/synthesizer.ts` |
| Doctor | `packages/core/src/doctor.ts` |
| Agent management | `packages/core/src/agent.ts` |
| Claude Desktop doctor | `packages/core/src/claude-desktop-doctor.ts` |
| Public index | `packages/core/src/index.ts` |

- Quick reference: [core-quickref.md](core-quickref.md)
- CLI commands that expose this API: [../cli/cli.md](../cli/cli.md)
- Deploy utilities: [../deploy/deploy.md](../deploy/deploy.md)
