# Teton vs. Cellanome R3200: the 2-minute version

**Reading time: ~2 min.**

**If you only read one line:** They are opposite tools. **Teton** = dead cells, huge numbers, deep molecular snapshot. **Cellanome** = live cells, smaller numbers, watched over days, perturbed on-chip, then same-cell RNA-seq. **For calcium imaging, only Cellanome works.**

---

## The split

- **Element Teton (AVITI24):** **fixed** cells (formaldehyde is step one), millions per run, 350 RNA + up to ~88 protein + morphology, result in **under 24 h**, but **one time point** and **no live anything**.
- **Cellanome R3200:** **live** cells in tiny programmable cages, tens of thousands per run, **watched for days**, dosed with drugs and pooled CRISPR **on the machine**, then whole-transcriptome RNA-seq on the **same** cell.

---

## Decision table

| You need... | Pick |
|---|---|
| Millions of cells, deep molecular snapshot | **Teton** |
| Read out a big CRISPR or drug screen | **Teton** |
| Subcellular spatial molecular detail | **Teton** |
| Live cells over time | **Cellanome** |
| **Calcium imaging / functional neurons** | **Cellanome** (only one) |
| Perturb on the machine itself | **Cellanome** |
| True electrophysiology (MEA, patch clamp) | **Neither** (needs external rig) |

---

## The one caveat that matters for us

Cellanome calcium imaging is **proven for slow, multi-day activity**, not yet for **fast neuronal firing (sub-second spikes)**. **Confirm temporal resolution with Dwight** before we lean on it for the Phase I functional readout. And remember: **neither box does real electrophysiology**.

---

## Bottom line

**Complementary, not either/or.** Use **Cellanome** for live discovery and perturbation; use **Teton** for high-throughput, high-plex molecular readout at the endpoint.
