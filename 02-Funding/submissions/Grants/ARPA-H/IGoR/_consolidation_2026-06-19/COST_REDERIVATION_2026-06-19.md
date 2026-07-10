# IGoR Cost Re-Derivation — Cascade Record (2026-06-19)

**BLUF (3 sentences):** This records the cost corrections cascaded into `C3_Price_Proposal.md` and `COST_MODEL_DETAILED_2026-06-16.md` on 2026-06-19. The deterministic, envelope-neutral corrections (Anne Carpenter's $2.0M Broad sub merged into IPAI/Purdue = $15.5M, matching the Solution Summary; $54M-vs-$50M total relabel; Element de-brand; Anna Merkoulovitch removed) were applied automatically. Two figures are **flagged for you and Ananth** to finalize in the C4 workbook because they are not derivable without institutional inputs: the F&A recompute on Anne's reattributed $2.0M, and the Cellanome $8.0M (held pending the June 23 response and the capex-vs-opex decision).

**If you only read one thing:** the headline number — **IPAI/Purdue is now $15.5M** (Phase I $4.5M, Phase II $4.4M, Phase III $6.6M), with the standalone Broad sub-award removed. Per-phase column sums are unchanged: **$54.0M** total project value, **$50.0M** ARPA-H request.

---

## 1. Resolved automatically (deterministic, no envelope change)

| # | Change | Old | New | Why it's safe |
|---|---|---|---|---|
| 1 | **Merge Broad sub into IPAI/Purdue** in the per-org × phase table | IPAI $13.5M + separate "Carpenter Lab / Broad (Sub)" $2.0M | IPAI/Purdue **$15.5M** (4.5 / 4.4 / 6.6); Broad row deleted | Anne is confirmed in-house at IPAI/Purdue, no Broad sub-award (rank-0 config). Just combines two rows already inside the envelope; matches the SS's $15.5M IPAI figure. |
| 2 | **Fix C3 total-row mislabel** | C3 had one row "TOTAL (ARPA-H request only) = 13.5 / 15.0 / 21.5 / 50.0" but the per-org rows actually sum to 15 / 16 / 23 / **54** | Two rows (mirrors the cost model): "TOTAL project value incl. ~$4.0M in-kind = 15 / 16 / 23 / **54**" and "ARPA-H request only = 13.5 / 15.0 / 21.5 / **50**" | The cost model (Table 1-A) already uses this correct two-row structure; C3 is brought into line. |
| 3 | **Element de-brand** | "Element AVITI24 / Teton CytoProfiling" platform name | "fixed-cell high-plex readouts (RNA ~350-plex, protein ~50-plex, Cell-Painting-style morphology, in-situ CRISPR-guide sequencing)" | Element is not a confirmed teaming partner and carries no budget line; it is a platform Tegtmeyer's lab uses. |
| 4 | **Architect name** | "Anna Merkoulovitch (candidate)" | "a planned Cytognosis hire (recruiting); Elham Jebalbarezi Sarbijan (IPAI) interim architect" | Anna is off market, no longer a candidate (rank-0 config). |
| 5 | **FTE summary** | separate "Broad residual" row (0.2 / 0.1 / 0.1) | row removed; folded into IPAI/Purdue line; program totals 24.7→24.5 / 25.1→25.0 / 27.9→27.8 | Simple arithmetic consequence of the merge. |
| 6 | **Remove resolved [FLAG 2026-06-17] tags** | ~13 scattered "Anne reattribution / Cellanome model TBD" tags | Anne-reattribution portion marked resolved; only the two items below remain flagged | The Anne reattribution is now decided and applied. |
| 7 | **Keep legitimately-Broad items** | — | "JUMP Cell Painting" open-data in-kind (~$0.15M) retained as a Broad open dataset | That is public data, independent of Anne's employment. |

---

## 2. Flagged for you + Ananth (NOT fabricated — finalize in C4 workbook)

| # | Item | What is known | What you must decide |
|---|---|---|---|
| A | **F&A on Anne's reattributed $2.0M** | Her ~$2.0M scope moved from the former Broad sub (~50% F&A) into Purdue-direct (~57% F&A). At the performer-total level the $15.5M / $50M envelope is held. | The indirect sub-allocation rises (~57% vs ~50% on ~$2.0M, order ~$0.1M, plus MTDC-base treatment of the former subaward). Recompute Purdue indirect and rebalance within the $50.0M envelope in the C4 workbook. Inserted as an inline `[RE-DERIVE — Shahin+Ananth]` flag in both cost docs. |
| B | **Cellanome $8.0M** (Ph I $2.0M / II $2.4M / III $3.6M) | Held as placeholder. | Confirm or update after the **June 23** Cellanome response and the **capex (R3200 in-lab) vs. opex (send-out)** operating-model decision. |

---

## 3. Authoritative file note

The **Appendix C.4 workbook** (`full_proposal/costs/C4_Price_Proposal_Workbook_2026-06-16.xlsx`) is the controlling price source; the narrative defers to it on any arithmetic discrepancy. Items A and B above must be executed there before the **August 6** full-proposal submission. The **June 25** Solution Summary does not require the finalized splits.

*Generated 2026-06-19 as part of the consolidation cascade. Source of truth: `IGoR_CONSOLIDATED_STATE.md`.*
