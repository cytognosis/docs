# Cytognosis Master Plan & Consolidation Program

**Date:** 2026-06-03 · The harmonized track taxonomy, the doc-home map, and the program to consolidate all tracks (strategy + implementation) across the four systems, using **cytomem** as the spine. **FOR AGREEMENT before the heavy build.**

## 0. BLUF

You have four doc systems plus a **live cytomem Neo4j graph** (7,322 artifacts, 14 repos). This harmonizes them to **one canonical track taxonomy** (your existing platform pillars + strategy overlays) and defines a **fresh-session, parallel-subagent consolidation program**. Agree the taxonomy and the canonical-home rule, then build.

## 1. The four systems and the canonical-home rule

| System | Path | Canonical for |
|---|---|---|
| **cytomem** (Neo4j) | `bolt://localhost:7687`; live, 7,322 artifacts, 14 repos | The cross-repo **index + provenance + persistent memory spine** across sessions/agents |
| **docs repo** | `~/repos/cytognosis/docs` | Canonical **engineering/platform** docs (cytonome, cytoverse, schemas, standards, toolchain, infra, design, decisions) |
| **Obsidian vault** | `~/Documents/ObsidianVault` | The **personal, ADHD-variant** working docs (01-Strategy … 07-Agent-Work) |
| **X-Labs** (this project) | `~/Claude/Projects/X-Labs` | The **strategy / funding / grants** workspace (funding, contracts, research dossiers, meeting docs) |

**Rule:** every artifact has **one canonical home**; cytomem **indexes all** and flags duplicates; the master view links across; the ADHD-variant of any doc lives in Obsidian.

## 2. Harmonized track taxonomy (aligns to `tracks.yaml`)

**Platform pillars (= cytomem tracks):**

- **Cytoverse** (The Map): `cytos`, `cytoexplorer` + the **Science Foundation** (BDNF axes, factorized-PRS, bipolar, the cellular micro-to-meso bridge). Funds: IGoR TA1/TA2, NIH TMM, HSF science.
- **Cytonome** (The Navigator): `cytoplex`, `Yar` + on-device AI, the ND app, PBC/dual-entity, YC.
- **Cytoscope** (The Sensor): Psychoscope / Hervé (no repo yet). Funds: NSF X-Labs. **Commercializes through the Cytonome/Yar PBC arm** (soft sensors first → MH sensors → wearable).
- **Toolchain** (implementation/infra): `cytoskeleton`, `cytocast`, `cytoskills`, `cytomem`. Includes the **KG + LinkML schemas/standards** (directly relevant to IGoR's ontology/schema asks).
- **Operational**: `infrastructure`, `branding`, `website`, `docs`, `org`, `tools`.
- **Research**: `neuro-pheno` + the `04-research/` corpus.

**Strategy overlays (cross-cutting, not repos; live in X-Labs/Obsidian):**

- **Funding & Partnerships**: IGoR, HSF/EVIDENT, NSF X-Labs, NIH (TMM) + One Mind, bridge/small grants (AWS, Coefficient x2, EA/LTFF), PAC, mental-health connections.
- **People**: Ananth, Patty, Duane, Manolis, Jordan.
- **Personal / Legal Ops**: CEO contract, Purdue appointment, runway, MIT/Broad wind-down, IRB.

## 3. Interconnections (the spine)

- **Cytoverse science** (BDNF/factorized-PRS, the **cellular micro-to-meso causal bridge**) feeds **IGoR TA1**, **HSF/EVIDENT**, and the **Cytoscope** biotype layer. The cellular bridge is what distinguishes IGoR from HSF (HSF = genomic+connectomic; we add the single-cell genomic→connectomic causal bridge).
- **Cytoscope** is funded by **NSF X-Labs** and **commercializes through Cytonome/Yar** into the PBC arm.
- **Toolchain** (schemas/standards) supports IGoR's ontology asks.
- **People** thread across every track; **Funding** splits by time: bridge/small = survival (now → Oct 1); IGoR/HSF/NIH = 2027 money.

## 4. The consolidation program (fresh session, parallel subagents)

Per track, a Sonnet subagent: (a) **queries cytomem** (`uv run cytomem search <track/term>`) and reads the track's repos/docs/vault sections; (b) summarizes **current state + top-3 priorities + gaps + duplicates**; (c) drafts the **harmonized track doc** (full + ADHD); (d) registers/links it. Max 2 parallel (house rule). Iterate, then assemble the **master view** (top priority per track + unified timeline + cross-links).

**Order:** survival/near-deadline first (Funding/IGoR, People), then the platform pillars (Cytoverse, Cytonome, Cytoscope), then Toolchain/Operational. **Use cytomem to find artifacts; do not crawl the filesystem blindly** (the implementation track is already indexed).

## 5. cytomem usage

- **Now:** CLI via the sandbox (`uv run cytomem search|stats|timeline`). **Read-only for discovery**; do **not** run `ingest` unilaterally (graph is already populated).
- **Recommended:** connect the **`cytomem-mcp`** server as an MCP so Cowork/Claude gets native cross-session recall (`cytomem_recall`, `cytomem_stats`, `cytomem_timeline`).

## 6. Master-view seed

**Timeline:** Jun 5 AWS · **Jun 9 IGoR Proposer Day** · Jun 25 IGoR Summary · Jul 13 NSF X-Labs · **Oct 1 runway cliff** · Oct 6 TMM · 2027 NIH/HSF/One Mind.

The full master view (full + ADHD versions) gets assembled at the end of the program, linking each track's canonical doc.

## 7. To agree before the heavy build

1. The **taxonomy** (six pillars + three overlays) and the **canonical-home rule**.
2. Whether to **connect `cytomem-mcp`** (recommended) so memory is native across sessions.
3. Run the heavy per-track build in a **fresh, dedicated session** (this one is at extreme context depth), with this doc + cytomem as the anchors.
