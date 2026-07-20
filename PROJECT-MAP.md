# Project Map: one organization, every source

> **Status**: Active (the contract; if reality diverges from this table, fix reality)
> **Date**: 2026-07-11
> **Author**: @shahin
> **Audience**: everyone, every agent
> **Tags**: `organization`, `projects`, `taxonomy`, `map`
> **Variants**: Technical (this doc) - Readable (same filename in Obsidian vault)

> [!NOTE]
> **TL;DR**: One table maps every Claude project to its docs pillar, its content, and its repos. The docs repo's 8 pillars are the master vocabulary; Obsidian mirrors them 1:1; every Claude project points at its pillar slice via `_context/`. Design is its own project, mirroring its own pillar.

## The map

| Claude project | Docs pillar(s) | What it holds | Key repos | Obsidian |
|---|---|---|---|---|
| **Grants** | `02-Funding` | grant applications, funder research, submissions, strategy (absorbed Strategic Planning content at `01-Strategy`) | docs | 02-Funding |
| **Science and Platform** | `05-Research` (+ science side of `03-Products`) | **the Neuroverse home**: scientific research, biotypes, psych axes, platform science narrative (Cytoverse, Cytoscope, Cytonome) | docs, neuro-pheno | 05-Research |
| **Design** | `07-Design` | design system, brand knowledge, track plans, Claude Design bridge | branding, docs | 07-Design |
| **Website** | `03-Products` (website slice) | website work drafts; site content decisions | website | 03-Products |
| **Yar** | `03-Products` (Yar slice) | Yar product work (ND app, PBC pathway) | Yar, cytoplex | 03-Products |
| **Cytos** | `04-Engineering` (schemas slice) | schemas, ontologies, LinkML standards work | cytos | 04-Engineering |
| **Infrastructure and Tooling** | `04-Engineering` | infra, cloud, CI, agent tooling, **cytomem**, mission hub | cytomem, infrastructure, cytoskills, cytocast, cytoskeleton, tools | 04-Engineering |
| **Operations** | `06-Operations` | legal, compensation, HR, inventory, filings | docs | 06-Operations |
| **Cytognosis** | `01-Strategy` | org-level strategy, board, entity structure | org, docs | 01-Strategy |
| **Refactor** | `04-Engineering` (meta) | consolidation backbone, master drive plans, this round's work | docs (registry) | 04-Engineering |
| **Personal** | none (private, NOT in docs repo) | cv, biosketch, networking | none | none |
| Strategic Planning (stub) | `01-Strategy` | empty pointer; content lives in Grants/01-strategy | - | - |

`00-Inbox` is the docs repo's landing zone only; it has no project (by design).

## The rules that keep this identical everywhere

1. **The 8 pillars are the master vocabulary** (`00-Inbox, 01-Strategy, 02-Funding, 03-Products, 04-Engineering, 05-Research, 06-Operations, 07-Design`). Obsidian mirrors them exactly. Claude projects map to pillar slices via `_context/` shortcuts; a project never invents its own taxonomy.
2. **One home of record** (docs repo) per document; projects hold working drafts only; datasets live in `https://github.com/cytognosis/datasets/tree/main/cytognosis`.
3. **A category that exists as a pillar gets its own project when it has active work** (this is why Design moved out of Science and Platform on 2026-07-11).
4. Tags on docs use the pillar vocabulary plus the two-axis skill ontology for skills only; the platform component taxonomy (Cytoverse/Cytoscope/Cytonome) describes the product, never file locations.
5. Project folders keep their historical names; THIS TABLE is where name-to-pillar equivalence lives (rename only if Shahin asks; the map makes renames unnecessary).

## Change log

- 2026-07-11: created; Design promoted to its own project (supersedes the same-morning fold into Science and Platform); Science and Platform explicitly documented as the Neuroverse home.

- 2026-07-15: W2 started — Infrastructure `_context` narrowed to owned Engineering slices (infrastructure, toolchain, agent-integration, specs, decisions, architecture, standards); removed the whole-`04-Engineering` link that leaked cytoplex/cytos/yar. Backup at `Infrastructure and Tooling/_archive/_context-bak-2026-07-15`. Remaining projects audited case-by-case (shared-pillar links kept only where the project legitimately works in that slice).

- 2026-07-15: W2 cont. — Cytognosis `_context` narrowed to 01-Strategy + org (removed whole-`06-Operations` link that exposed legal/comp/HR). Audited the rest (Grants strategy/research, Science-and-Platform, Yar, Cytos) — their shared-pillar links are legitimate working slices, kept. W2 substantially done; W1 (vault legacy-root migration) + W3 (sprawl) remain, running after the companion lane releases the vault.
