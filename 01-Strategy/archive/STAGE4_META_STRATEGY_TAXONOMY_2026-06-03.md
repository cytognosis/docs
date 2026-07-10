# Stage 4 — Meta-Strategy: Finalized Taxonomy, Convergence, and Canonical-Home Reconciliation

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: leadership
> **Tags**: `strategy`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

**Date:** 2026-06-03 · Built from the now-complete cytomem corpus (10,006 artifacts / 27 sources). Validates the taxonomy, fixes canonical homes for redundant strategy content, and briefs the Stage 5 per-track build. Reading time ~6 min. **If you only read one thing: the taxonomy holds as-is; the work now is reconciling redundant strategy copies to one canonical home per cluster, then running the per-track consolidation.**

## BLUF

The six-pillar + three-overlay taxonomy survives contact with the full corpus, so no re-architecture is needed. The real finding is **redundancy**: the core strategy (the "Helix" org model, the 15-Year Roadmap, funding strategy) exists in 3+ copies across the vault, personal-drafts, and the strategic-planning project. Stage 4 assigns each cluster one canonical home; Stage 5 then runs per-track subagents to consolidate.

## Done (Stages 0–1)

- ✅ Corpus complete: **10,006 artifacts, 27 sources** (repos + Obsidian + 7 Cowork projects + 6 curated archive sources)
- ✅ Archive audit closed; nothing deleted; dedup (content-hash) operational with `docs` repo preferred as canonical
- ✅ Strategy corpus confirmed semantically searchable (Helix cluster, 15-Year Roadmap surface cleanly)

## 1. Taxonomy confirmed (six pillars + three overlays)

| Pillar / overlay | Role | Primary sources in graph |
|---|---|---|
| **Cytoverse** (Map) | Science foundation, KG | `cytos`, `docs/cytoverse`, science dossiers |
| **Cytonome** (Navigator) | On-device + causal AI, ND app, PBC | `cytoplex`, `Yar` |
| **Cytoscope** (Sensor) | Biosensor / Psychoscope | (no repo yet) NSF X-Labs docs |
| **Toolchain** | Infra, schemas, standards | `cytoskeleton`, `cytocast`, `cytoskills`, `cytomem` |
| **Operational** | Org, brand, web, infra | `infrastructure`, `branding`, `website`, `org`, `docs` |
| **Research** | Dossiers, RDoC, neuro-pheno | `archive-rdoc`, `04-research` corpus |
| overlay: **Funding & Partnerships** | IGoR, HSF, NSF, NIH, bridge grants | `cowork-grants`, X-Labs funding docs |
| overlay: **People** | Ananth, Patty, Duane, Manolis, Jordan | meetings, key-people memory |
| overlay: **Personal/Legal Ops** | Contract, runway, appointments | X-Labs/03-contracts, Helix org docs |

No corpus content fell outside these categories. The taxonomy is **frozen** for the build.

## 2. Organizing lens: value-streams × lifecycle

Vertical = pillars; horizontal = lifecycle stage. Each cell points to its canonical home.

| Pillar → / Stage ↓ | Strategy | Science | Funding | Implementation/PM | Product |
|---|---|---|---|---|---|
| Cytoverse | strategic-planning | 04-research / docs | IGoR, HSF, TMM | cytos | asset explorer |
| Cytonome | strategic-planning | (causal AI) | YC, PBC | cytoplex, Yar | ND app |
| Cytoscope | strategic-planning | sensor design | NSF X-Labs | (no repo) | soft sensors |
| Toolchain | docs | schemas | (cross-cut) | cytoskeleton/cast/skills/mem | — |

## 3. Convergence points (the spine)

- **Cellular micro-to-meso causal bridge** is the keystone: it feeds **IGoR TA1**, **HSF/EVIDENT**, and the **Cytoscope** biotype layer, and is what differentiates IGoR from HSF (HSF = genomic+connectomic; we add the single-cell genomic→connectomic causal link). Keep the factorized-PRS confidential and off the bipolar paper.
- **Cytoscope** is funded by **NSF X-Labs** and commercializes through the **Cytonome/Yar PBC** arm (soft sensors → MH sensors → wearable).
- **Toolchain schemas/standards** (LinkML KG) directly support IGoR's ontology asks.
- **Funding splits by time:** bridge/small grants = survival to Oct 1 runway cliff; IGoR/HSF/NIH = 2027 money.

## 4. Canonical-home reconciliation (the actionable finding)

cytomem dedup plus semantic recall surfaced the same strategy content in multiple homes. Assignments:

| Content cluster | Copies found in | **Canonical home** | Disposition of others |
|---|---|---|---|
| **Helix organizational strategy** (Hybrid Orgs, FRO models, org_helix, people, funding strategy) | `archive-old-obsidian/Operations/Organizational Strategy (Helix)/`, `personal-drafts/Operations/{Organizational Strategy (Helix), Strategic Planning}/`, `cowork-strategic-planning/master_plan/` | **`cowork-strategic-planning/master_plan/`** (active workspace) | archive-old-obsidian + personal-drafts copies = superseded; keep indexed, do not edit |
| **15-Year Strategic Roadmap** | `cowork-strategic-planning/draft/01_..._15-Year.md` + old-obsidian numbered variants | **`cowork-strategic-planning`** | old-obsidian numbered drafts = historical |
| **`01_plan_prose` / platform plan** | `cytos/design/historical`, `cytos/docs/historical/historical`, `docs/cytoverse/cytos/historical/historical` | **`docs/cytoverse/cytos`** (engineering canonical) | cytos historical copies = superseded |

Rule reaffirmed: one canonical home per artifact; cytomem indexes all and flags duplicates; the ADHD-variant lives in Obsidian.

## 5. Graph hygiene finding (quick win)

The convergence-theme recall returned **non-content noise**: `cytoskeleton/.dvc/tmp/{rwlock,btime,lock}`, `.github/PULL_REQUEST_TEMPLATE.md`, `.coderabbit.yaml`. These dilute semantic search. **Recommendation: add `.dvc/tmp`, `.github`, and lockfiles to the repo-scan excludes in `cytomem/configs/repos.yaml`** and re-ingest repos. Low effort, improves recall precision. (Flagged, not yet done.)

## 6. Stage 5 plan — per-track subagent briefs

Run Sonnet subagents, **max 2 parallel** (house rule), survival/near-deadline tracks first. Each subagent gets: the cytomem corpus + this taxonomy + explicit goals, deliverables, verification.

| Order | Track / overlay | Goal | Deliverable | Verification |
|---|---|---|---|---|
| 1 | **Funding & IGoR** (Jun 9 Proposer Day) | Consolidate funding pipeline + IGoR positioning | Full + ADHD track doc, unified funding timeline | Deadlines web-verified; cellular-bridge differentiator present |
| 2 | **People** | One roster with status + asks | People doc cross-linked to meetings | Matches key-people memory |
| 3 | **Cytoverse** | Science foundation state + top-3 | Track doc (full + ADHD) | factorized-PRS kept confidential |
| 4 | **Cytonome** | PBC/Yar/ND app state | Track doc | PBC pathway consistent with openness policy |
| 5 | **Cytoscope** | Sensor strategy + NSF fit | Track doc | NSF X-Labs Jul 13 reflected |
| 6 | **Toolchain + Operational** | Infra/schema/standards state | Track doc | schema↔IGoR ontology link captured |

After the six tracks: assemble the **master view** (top priority per track + one unified timeline + cross-track links), full and ADHD variants.

## Timeline anchor

Jun 5 AWS · **Jun 9 IGoR Proposer Day** · Jun 25 IGoR Summary · Jul 13 NSF X-Labs · **Oct 1 runway cliff** · Oct 6 TMM (RFA-DA-27-004) · 2027 NIH/HSF/One Mind.
