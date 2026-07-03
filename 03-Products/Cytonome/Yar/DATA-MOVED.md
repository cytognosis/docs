# Yar primary tables moved to the datasets tree

> **Status:** Active pointer · **Date:** 2026-07-01

Per the data policy (blueprint Section 16h, primary tables are data, not docs), the Yar feature and prioritization tables moved out of this docs tree to the canonical datasets home.

| Table | New canonical location |
|---|---|
| `yar-feature-matrix-v4.csv` | `~/datasets/cytognosis/products/yar/yar-feature-matrix-v4.csv` |
| `yar-feature-naming-map.csv` | `~/datasets/cytognosis/products/yar/yar-feature-naming-map.csv` |
| `yar-feature-prioritization.csv` | `~/datasets/cytognosis/products/yar/yar-feature-prioritization.csv` |
| `yar-internal-prioritization-v1.csv` | `~/datasets/cytognosis/products/yar/yar-internal-prioritization-v1.csv` |

Committed in the datasets repo on branch `reorg/yar-2026-07-01` (commit `ebff402`) with a provenance README. The tables are under 30 KB, so they are committed to git there, not tracked via DVC.
