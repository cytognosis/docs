# IGoR Research (scientific and technical source of record)

> [!NOTE]
> **`IGoR_Research_Master.md` is the source of record** for the science behind the proposal: the external methods landscape and our key contributions across proposal variants. It is **compiled** from modular section files, so edit the sections, not the compiled master.

## What to open

| File | Use |
|---|---|
| **`IGoR_Research_Master.md`** / `.pdf` | Internal build (all 21 sections, including restricted). The working source of record. |
| `IGoR_Research_Master_shareable.md` / `.pdf` | Same, with proprietary, personal, and internal-decision sections removed. An internal working draft; review before any external use. |
| `sections/` | The content, one file per section. **Edit here.** |
| `_template/` | Structure: `manifest.json` (section order, titles, restricted flags), `master_head.md` (front matter), `pdf.css` (print style). |
| `_sources/` | The original research notes, the two standards reviews, and the schizophrenia/22q11/TBX1 disease-genetics doc, now consolidated into `sections/`. Kept for provenance. |

## How it is built

Content lives in `sections/`; structure and order live in `_template/manifest.json`. `build.py` assembles them into the master (with a linked section index) and renders PDF via pandoc + weasyprint.

```
python3 build.py                      # internal, markdown only
python3 build.py --profile shareable  # drop restricted sections
python3 build.py --pdf                # also render PDF
python3 build.py --all                # both profiles, markdown + PDF
```

## Section map

- **00 to 10:** executive overview and the core thesis (disease as the causal perturbation operator).
- **20 to 24:** external landscape (TA1 virtual-cell methods, TA2 agentic systems, TA3/TA4 lab standards, causal-representation theory, and disease-knowledge and cellular-model standards).
- **30 to 35:** our contributions (TA1 four pillars, TA2 engine, TA3/TA4 execution, and the standards stack); **31 and 32 are restricted** (proprietary factorization, perturbation model under review).
- **40 to 42:** disease strategy, the Phase I anchor (**41 restricted**, personal genomic data), and penetrant-schizophrenia genetics with the familial-disease rationale for cellular models.
- **50 to 70:** metrics, team and cost, proposal-evolution crosswalk.
- **90:** open decisions and pre-submission actions (**restricted**, internal).
- **99:** consolidated references with verification flags.

> [!CAUTION]
> **Restricted sections (31, 32, 41, 90)** appear only in the internal build. The proprietary factorization, the perturbation model under anonymous review, and the personal-genomic anchor must never enter partner-facing or public submission text. Mark proprietary pages "Proprietary" in any ARPA-H submission.

## Next step

This master is the basis for refining the three deliverables (one-pager, Solution Summary, full proposal), each of which will reuse the same templated-section plus compile pattern.
