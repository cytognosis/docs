# Master Asset Registry — where everything lives

> **Status**: Active (authoritative index; regenerate with the enumerator, keep cytomem as the queryable system of record)
> **Date**: 2026-07-15  |  **Author**: @shahin  |  **Audience**: everyone, every agent
> **Tags**: `inventory`, `assets`, `registry`, `organization`
> **Variants**: Technical (this doc) - Readable (same filename in Obsidian vault)

> [!NOTE]
> **TL;DR**: One place to find any asset. The queryable system of record is **cytomem** (`cytomem recall "X"`, 31 repos indexed). This doc is the human-readable map: every Claude project, git repo, docs pillar, the vault, the datasets store, and the Google Drive, with live git state. Contracts that govern placement: PROJECT-MAP.md, ONTOLOGY.md, ORGANIZATION-ATLAS_2026-07-11.md (all at docs repo root).

**Reading time: ~4 min. If you only read one thing:** section 1 (the 5 homes) then section 6 (how to find anything).

## 1. The homes (where any asset can be)
| Home | Path | What lives here |
|---|---|---|
| Docs repo (home of record) | `https://github.com/cytognosis/docs` | all technical docs, 8 pillars, specs, contracts |
| Obsidian vault (twins) | `~/Documents/ObsidianVault` | plain-language twins, same path+filename |
| Claude projects (workspaces) | `~/Claude/Projects` | drafts + _context slices into docs |
| Datasets store | `https://github.com/cytognosis/datasets/tree/main/cytognosis` | data, large binaries |
| Code repos | `https://github.com/cytognosis` | all git repositories |
| Mission board | http://127.0.0.1:40601 (+ tailnet URL) | task cards, worktrees, runs (pointers only) |
| cytomem (graph) | Neo4j @ localhost:7687 + MCP | queryable index of all of the above |
| Google Drive (shared) | `~/.mnt/cytognosis-gdrive/Cytognosis Foundation` | governance, originals, some assets only-here |

## 2. Claude projects (12) + their docs slices
- **Cytognosis**  — _context: 01-Strategy->01-Strategy 06-Operations->06-Operations org->06-Operations/org
- **Cytos**  — _context: cytoplex->04-Engineering/cytoplex cytos->04-Engineering/cytos
- **Design**  — _context: 07-Design->07-Design
- **Grants**  — _context: 01-Strategy->01-Strategy 02-Funding->02-Funding 05-Research->05-Research
- **Infrastructure and Tooling**  — _context: agent-integration->04-Engineering/agent-integration architecture->04-Engineering/architecture decisions->04-Engineering/decisions infrastructure->04-Engineering/infrastructure specs->04-Engineering/specs standards->04-Engineering/standards toolchain->04-Engineering/toolchain
- **Operations**  — _context: 06-Operations->06-Operations
- **Personal**  — _context: (none)
- **Refactor** (consolidation cockpit) — _context: (none)
- **Science and Platform**  — _context: 03-Products->03-Products 05-Research->05-Research cytos->04-Engineering/cytos
- **Strategic Planning**  — _context: 01-Strategy->01-Strategy
- **Website**  — _context: 07-Design->07-Design
- **Yar**  — _context: Yar->03-Products/Cytonome/Yar yar->04-Engineering/yar

## 3. Git repos (live state as of 2026-07-15)
| Repo | Branch | Ahead/Behind origin | Dirty files | Last commit |
|---|---|---|---|---|
| Yar | main |  | 0 | dbadd6f feat: add .agents/steering/ docs |
| branding | feat/branding-consolidation-2026-07 |  | 0 | 44254f6 docs(brand): add spec 001 verification (FA |
| cytocast | feat/spec-driven-profile |  | 0 | 521e2e5 feat(template): wire spec-guard pre-commit |
| cytoexplorer | main |  | 0 | a099c97 feat: initial CytoExplorer — desktop web |
| cytomem | feat/mission-integration-specs |  | 0 | 57bfd56 docs(specs): add specs 002-mission-hub-bri |
| cytoplex | main |  | 0 | d23153f feat: add .agents/steering/ docs |
| cytos | main |  | 0 | d4a3df4 merge: feat/papers-ingestion-kg into main |
| cytoskeleton | main |  | 0 | 83b39d0 merge: reorg/toolchain-2026-07-01 into mai |
| cytoskills | main |  | 0 | 257acf4 skills(dev): add Mission Stack section (tw |
| docs | main |  | 1 | 4506b84 docs(links): repair movable links + annota |
| infrastructure | main |  | 0 | 1529245 chore: update SKILL.md |
| org | main |  | 0 | 1213861 chore: initial commit from workspace |
| tools | main |  | 0 | 0e43fe5 chore: initial commit from workspace |
| website | feat/spec-driven-2026-07-11 |  | 7 | a11b69d docs(steering): seed AGENTS.md (spec-drive |

## 4. Docs pillars (level-1 doc + subdir counts)
| Pillar | subdirs | .md files |
|---|---|---|
| 00-Inbox | 1 | 6 |
| 01-Strategy | 6 | 70 |
| 02-Funding | 14 | 387 |
| 03-Products | 2 | 153 |
| 04-Engineering | 14 | 320 |
| 05-Research | 3 | 89 |
| 06-Operations | 8 | 63 |
| 07-Design | 1 | 41 |

## 5. Datasets store + Drive top-level
**Datasets** (`https://github.com/cytognosis/datasets/tree/main/cytognosis`):
- 5.7M	https://github.com/cytognosis/datasets/tree/main/cytognosis/ICD-11-CDDR
- 16K	https://github.com/cytognosis/datasets/tree/main/cytognosis/curations
- 475M	https://github.com/cytognosis/datasets/tree/main/cytognosis/design-system-sources
- 4.0K	https://github.com/cytognosis/datasets/tree/main/cytognosis/external
- 46M	https://github.com/cytognosis/datasets/tree/main/cytognosis/grants-large
- 12K	https://github.com/cytognosis/datasets/tree/main/cytognosis/metadata
- 140M	https://github.com/cytognosis/datasets/tree/main/cytognosis/neuroverse-ontologies
- 3.2M	https://github.com/cytognosis/datasets/tree/main/cytognosis/ontologies
- 16K	https://github.com/cytognosis/datasets/tree/main/cytognosis/operations
- 8.0K	https://github.com/cytognosis/datasets/tree/main/cytognosis/products
- 4.0M	https://github.com/cytognosis/datasets/tree/main/cytognosis/science-platform
- 8.0K	https://github.com/cytognosis/datasets/tree/main/cytognosis/treatments
- 64K	https://github.com/cytognosis/datasets/tree/main/cytognosis/yar

**Google Drive shared** (`~/.mnt/cytognosis-gdrive/Cytognosis Foundation`):
- Cytognosis
- Branding
- &
- Identity
- Cytognosis
- Funding
- Cytognosis
- Library
- Cytognosis
- Operations
- Cytognosis
- Proposal
- Cytognosis
- Strategy
- Cytognosis
- unsorted

## 6. How to find ANYTHING
1. **Ask cytomem**: `cytomem recall "<what you're looking for>"` (semantic search over 31 repos). System of record.
2. **Where does a NEW asset go?** -> ONTOLOGY.md placement ladder + PROJECT-MAP.md (project<->pillar).
3. **A specific doc?** -> its pillar in the docs repo; plain-language version = same path in the vault.
4. **A dataset?** -> `https://github.com/cytognosis/datasets/tree/main/cytognosis`; access/modality in the dataset registry (06-Operations, in progress).
5. **A grant/proposal?** -> `02-Funding/submissions` (IGoR = `.../ARPA-H/IGoR/INDEX.md`).
6. **Governance/legal/branding originals?** -> Google Drive mount + `gdrive-*-index.md` under the relevant pillar.
7. **In-flight agent work?** -> the mission board (worktree branches `vk/*`); nothing merges to main without review.

## 7. Safety points (git tags, restore anywhere)
- **docs**: pre-igor-harmonize-2026-07-12 pre-linkfix-2026-07-11 pre-promotion-2026-07-10 
- **ObsidianVault**: pre-consolidate-merge-2026-07-15 
- **branding**: checkpoint/pre-antigravity-2026-05-23 pre-consolidate-merge-2026-07-15 

## 8. Regenerate
This registry is generated by the enumerator in `scripts/asset-registry.sh` (host). cytomem is the live index; regenerate this human map after major moves. Backups: `Refactor/_safety-archives` + per-repo `_archive/` + git tags above.
