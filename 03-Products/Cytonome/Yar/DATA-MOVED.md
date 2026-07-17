# Yar primary tables moved to the datasets tree

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: engineers, stakeholders
> **Tags**: `yar`, `product`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

> **Status:** Active pointer · **Date:** 2026-07-01

Per the data policy (blueprint Section 16h, primary tables are data, not docs), the Yar feature and prioritization tables moved out of this docs tree to the canonical datasets home.

| Table | New canonical location |
|---|---|
| `yar-feature-matrix-v4.csv` | `~/datasets/cytognosis/yar/data/yar-feature-matrix-v4.csv` |
| `yar-feature-naming-map.csv` | `~/datasets/cytognosis/yar/data/yar-feature-naming-map.csv` |
| `yar-feature-prioritization.csv` | **missing** — not found at this or any other known location as of 2026-07-17; open gap, not yet re-created after the move |
| `yar-internal-prioritization-v1.csv` | `~/datasets/cytognosis/yar/data/yar-internal-prioritization-v1.csv` |

Committed in the datasets repo on branch `reorg/yar-2026-07-01` (commit `ebff402`) with a provenance README. The tables are under 30 KB, so they are committed to git there, not tracked via DVC.

> **Correction (2026-07-17):** this table previously pointed at `~/datasets/cytognosis/products/yar/`. That directory exists but holds only a `.gitkeep`. The tables actually live at `~/datasets/cytognosis/yar/data/`, verified against the `reorg/yar-2026-07-01` branch; paths above corrected.
