# Cytognosis Skills Finalization

## Goal

Complete the three skill consolidation tasks that were interrupted by model quota limits:
1. Fix 5 missing reference files in `cytognosis-dev`
2. Fix 1 missing reference in `cytognosis-doc`
3. Merge `cytognosis-design-system-master` and `cytognosis-template-master` into `cytognosis-branding`

## Current State

### cytognosis-doc (458 lines, v5.2.0)
- ✅ ADHDfy pipeline: `adhdfy-pipeline.md` (213 lines) + `transformation-rules.md` (234 lines)
- ✅ ADHD-friendly template: `adhd-friendly-template.md` (136 lines)
- ✅ 28 of 29 reference templates present
- ❌ **1 broken link**: `references/cytos-standards.md` (exists in cytognosis-dev, not doc)
- **Fix**: Copy or symlink from cytognosis-dev, or remove the reference

### cytognosis-dev (383 lines, v5.2.0)
- ✅ Cytocast integration in SKILL.md (24 mentions, profiles table, architecture diagram)
- ✅ Steering docs: 3 complete references (init-guide, management, templates)
- ✅ Cytos standards: `cytos-standards.md` (163 lines)
- ❌ **5 broken links**: SKILL.md references files that don't exist:
  - `references/cytocast-workflow.md` — Copier scaffolding, profiles, hooks, CI/CD
  - `references/cytoskeleton-reference.md` — Environment management, DAG resolution
  - `references/cyto-skills-authoring.md` — Writing new cytoskills
  - `references/multi-app-monorepo.md` — Monorepo patterns (uv workspace, pnpm, Melos)
  - `references/project-dev-guide.md` — Daily dev workflow, debugging, testing

### cytognosis-branding (165 lines, v3.0.0)
- ✅ Has 12 deep reference files (brand foundation through dataviz)
- ❌ **Merge not executed**: Still tells agents to "LOAD cytognosis-design-system-master INSTEAD"
- ❌ `cytognosis-design-system-master` (242 lines + assets/) still standalone
- ❌ `cytognosis-template-master` (262 lines) still standalone

## Proposed Changes

### Phase 1: Fix cytognosis-dev (5 missing references)

#### [NEW] `references/cytocast-workflow.md`
Content from `~/repos/cytognosis/cytocast/` — Copier copy/update workflow, profile selection, component graph, hooks, CI/CD scaffolding.

#### [NEW] `references/cytoskeleton-reference.md`
Content from `~/repos/cytognosis/cytoskills/skills/infrastructure/cytoskeleton/SKILL.md` and cytoskeleton source — environment strategies, DAG resolution, lock generation, compute backends.

#### [NEW] `references/cyto-skills-authoring.md`
How to write a new cytoskill: folder structure, SKILL.md format, references/ pattern, testing, publishing.

#### [NEW] `references/multi-app-monorepo.md`
Monorepo patterns: uv workspace, pnpm workspace, Melos (Flutter), mise.toml, prek (pre-commit).

#### [NEW] `references/project-dev-guide.md`
Daily development: running tests, debugging, code quality tiers, CI checks, Docker workflow.

---

### Phase 2: Fix cytognosis-doc (1 missing reference)

#### [NEW] `references/cytos-standards.md`
Copy from cytognosis-dev's version (163 lines) since both skills reference it.

---

### Phase 3: Merge branding skills

#### [MODIFY] `cytognosis-branding/SKILL.md`
Absorb the routing tables, cheatsheets, tokens, and profile picker from `cytognosis-design-system-master`. Absorb the template patterns from `cytognosis-template-master`. Restructure as:
- § Routing: Quick decision tree (what was design-system-master's §1)
- § Tokens: Color/type/spacing cheatsheet (what was design-system-master's cheatsheet)
- § Profiles: 4 use-case profiles (Foundation/Clinical/Research/Lab)
- § Templates: Deck/doc/email/social/print patterns (what was template-master)
- § Deep References: Point to existing `references/01_*.md` through `references/12_*.md`

#### [MODIFY] `cytognosis-branding/references/`
Move relevant assets from design-system-master and template-master into branding's references/.

#### [DELETE] `cytognosis-design-system-master/` (standalone skill)
Remove from `~/.agents/skills/` and `cytoskills/skills/cytognosis/`.

#### [DELETE] `cytognosis-template-master/` (standalone skill)
Remove from `~/.agents/skills/` and `cytoskills/skills/cytognosis/`.

---

### Phase 4: Sync all locations

After all edits, sync `~/.agents/skills/` → `cytoskills/skills/cytognosis/` for:
- cytognosis-dev
- cytognosis-doc
- cytognosis-branding
- Remove cytognosis-design-system-master
- Remove cytognosis-template-master

## Verification Plan

### Automated
```bash
# Check no broken references remain
for skill in cytognosis-dev cytognosis-doc cytognosis-branding; do
  for ref in $(grep -oP 'references/[a-z0-9_-]+\.md' ~/.agents/skills/$skill/SKILL.md | sort -u); do
    full="$HOME/.agents/skills/$skill/$ref"
    [ -f "$full" ] || echo "❌ $skill: $ref MISSING"
  done
done

# Check standalone skills removed
[ -d ~/.agents/skills/cytognosis-design-system-master ] && echo "❌ design-system-master still exists"
[ -d ~/.agents/skills/cytognosis-template-master ] && echo "❌ template-master still exists"

# Verify cytoskills sync
for skill in cytognosis-dev cytognosis-doc cytognosis-branding; do
  diff <(md5sum ~/.agents/skills/$skill/SKILL.md | cut -d' ' -f1) \
       <(md5sum ~/repos/cytognosis/cytoskills/skills/cytognosis/$skill/SKILL.md | cut -d' ' -f1) \
    && echo "✅ $skill: synced" || echo "❌ $skill: out of sync"
done
```
