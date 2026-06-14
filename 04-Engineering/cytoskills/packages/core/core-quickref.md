> **Status**: Active
> **Date**: 2026-06-14
> **Author**: Cytognosis Foundation
> **Audience**: engineers, contributors
> **Tags**: `quick-reference`, `core`, `cytoskills`

# @cytognosis/cyto-skills — Quick Reference

> **One line**: Core library for the cytoskills monorepo. Owns SKILL.md parsing, skill discovery, CSO classification, quality judging, tagging, and agent management.
> **Full doc**: [core.md](core.md)

---

## Key Concepts

| Term | Definition |
|------|-----------|
| **BaseSkill** | Class wrapping a parsed skill directory. The main handle for all skill operations. |
| **CSO** | Cyto Skill Ontology. CURIE-based taxonomy (e.g. `cso:Python`) used to classify skills. |
| **Phase directory** | One of 15 named subdirectory paths the loader searches across the multi-repo layout. |
| **Judge** | Quality scorer: 6 weighted axes (structure, trigger, content, cso, naming, freshness) → PASS/WARN/FAIL. |
| **Sidecar** | `.cyto-tags.yaml` file written next to `SKILL.md` by the tagger, before promotion to frontmatter. |
| **Memory file** | Agent-specific Markdown config (`CLAUDE.md`, `GEMINI.md`, etc.) managed by the agent module. |
| **SkillIO** | Input or output slot on a skill. Must use `namespace:Type` schema references. |

---

## Modules and Exports

| Module | Key exports |
|--------|-------------|
| `manifest.ts` | `BaseSkill`, `SkillFrontmatterSchema`, `SkillIOSchema`, `parseSkillMd` |
| `loader.ts` | `discoverSkill`, `iterSkills`, `PHASE_DIRS`, `SkillLoadError` |
| `classifier.ts` | `classify`, `classifyAll`, `clusterByCso`, `csoLabel`, `CSO_LABELS` |
| `ontology.ts` | `OntologyRegistry`, `registry` (singleton), `CSOTerm`, `TagScore` |
| `tagger.ts` | `SkillTagger`, `CytoTags`, `AxisTag` |
| `judge.ts` | `judgeSkill`, `judgeAll`, `formatJudgeReport`, `JudgeReport`, `Verdict` |
| `reviewer.ts` | `reviewCollection`, `formatCollectionReview`, `CollectionReview` |
| `synthesizer.ts` | `synthesize`, `clusterByTaxonomy`, `ConsolidationReport` |
| `doctor.ts` | `DiagnosticResult`, `diagnoseSkill`, `validateJsonl`, `parseJsonl` |
| `agent.ts` | `AGENTS`, `installSkill`, `batchInstall`, `doctorAgent`, `memoryDiff`, `memoryHarmonize`, `createVaultLink` |
| `claude-desktop-doctor.ts` | `doctorClaudeDesktop`, `fixClaudeDesktopLauncher`, `fixStaleSpacePaths`, `purgeElectronCache` |

---

## BaseSkill API

| Method / Property | Returns |
|-------------------|---------|
| `BaseSkill.load(skillDir)` | `Promise<BaseSkill>` |
| `.name` | `string` |
| `.description` | `string` |
| `.tags` | `string[]` (primary CSO CURIEs from structured tags, or flat list) |
| `.inputs` / `.outputs` | `SkillIO[]` |
| `.scripts()` | `Promise<string[]>` |
| `.references()` | `Promise<string[]>` |

---

## Judge Axes

| Axis | Weight | Threshold |
|------|--------|-----------|
| `trigger` | 25% | Quoted keywords, routing guidance |
| `content` | 25% | Decision Tree, References, guardrails |
| `structure` | 20% | name/description/author/license/version, body length |
| `cso` | 10% | Structured use_case/org_function/domain tags |
| `naming` | 10% | Kebab-case, ≤ 40 chars, slug = frontmatter name |
| `freshness` | 10% | version, status, last_revised within 6 months |

**Verdicts**: PASS ≥ 70 / WARN 50–69 / FAIL < 50

---

## Agent IDs and Paths

| Agent | ID | Skills dir | Memory file |
|-------|-----|-----------|------------|
| Claude Code / Cowork | `claude` | `~/.claude/skills` | `~/.claude/CLAUDE.md` |
| Antigravity (Gemini) | `antigravity` | `~/.gemini/antigravity/skills` | `~/.gemini/antigravity/GEMINI.md` |
| Shared agents | `agents` | `~/.agents/skills` | `~/.agents/AGENTS.md` |
| Cursor | `cursor` | `~/.cursor/skills` | `~/.cursor/CURSOR.md` |
| Kiro (AWS) | `kiro` | `~/.kiro/skills` | `~/.kiro/KIRO.md` |

---

## Skill Groups (batchInstall)

| Group | Skills |
|-------|--------|
| `cytognosis` | cytognosis-dev, cytognosis-doc, cytognosis-org, cytognosis-writer, cytognosis-orchestrator, cytognosis-branding, cytognosis-design-system-master, cytognosis-template-master |
| `coding` | python-pro, typescript-pro, react-expert, debugging, testing, technical-documentation, skill-creator, skill-judge |
| `science` | machine-learning, deep-learning, bioinformatics, visualization, literature, ontology-tools |
| `writing` | writing, communication, grants, scientific-documentation, meeting-summarizer |
| `meta` | skill-creator, skill-judge, thinking, orchestrator, personality |

---

## Common Patterns

```typescript
// Load all skills from a root
import { iterSkills } from "@cytognosis/cyto-skills";
const skills = await iterSkills(["/home/user/repos/my-skills"]);

// Classify a single skill
import { classify } from "@cytognosis/cyto-skills";
const tags = classify(skill); // string[] of CSO CURIEs

// Judge a skill
import { judgeSkill, formatJudgeReport } from "@cytognosis/cyto-skills";
const report = judgeSkill("/path/to/skill");
console.log(formatJudgeReport(report, true));

// Tag a skill (write sidecar)
import { SkillTagger } from "@cytognosis/cyto-skills";
const tagger = new SkillTagger({ confidenceThreshold: 0.5 });
tagger.tag("/path/to/skill/SKILL.md");
tagger.promote("/path/to/skill/SKILL.md", 0.7);

// Install cytognosis group to Claude
import { batchInstall } from "@cytognosis/cyto-skills";
await batchInstall("claude", "cytognosis", ["/path/to/skills"]);

// Check memory drift for Claude
import { memoryDiff } from "@cytognosis/cyto-skills";
const diff = await memoryDiff("claude");
console.log(diff.hasDrift, diff.deployedOnly);
```

---

## Error Quick-Fix

| Error / Symptom | Fix |
|-----------------|-----|
| `SkillLoadError: Failed to load N skill(s)` | One or more SKILL.md files have invalid frontmatter. Check the listed paths for missing required fields. |
| `IO slot 'x' has unqualified schema reference` | `inputs`/`outputs` schema field must use `namespace:Type` form, e.g. `bio:Protein`. |
| `iterSkills` returns empty array | Verify `PHASE_DIRS` paths exist under `searchRoots`. Try setting `CYTO_SKILLS_ROOT`. |
| `tagger.promote` returns false | No sidecar found (run `tagger.tag` first) or no tags met the 0.7 threshold. |
| Agent doctor reports broken symlinks | Run `fixDoctor(agent)` to remove them, then reinstall. |

---

## See Also

- [Full documentation](core.md) — comprehensive reference + explanation
- [CLI quick reference](../cli/cli-quickref.md) — commands that expose this API
- [Deploy quick reference](../deploy/deploy-quickref.md) — sync/deploy utilities
- [packages/core/src/](../../../../packages/core/src/) — source code
