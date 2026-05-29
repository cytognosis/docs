# PDF Parser Benchmark: Final Results (Manual Review)

Focused comparison of **Docling**, **Marker**, **Surya**, and **Chandra** on AlphaGenome (14p) and PaSCient (13p), all on AMD Strix Halo with AOTriton.

## Quantitative Results

### AlphaGenome (14 pages)

| Metric | Docling | Marker | Surya | Chandra |
|--------|--------:|-------:|------:|--------:|
| **Time** | **10.1s** | 1171s | 298s | 5993s |
| **Figures** | 0 | 9 | 8 | 8 |
| **Refs** | 0 | 0 | — | 0 |
| **Sections** | 25 | 19 | — | 20 |
| **MD chars** | 82,276 | 88,423 | — | 104,965 |
| **MD lines** | 322 | 320 | — | 1,333 |

### PaSCient (13 pages)

| Metric | Docling | Marker | Surya | Chandra |
|--------|--------:|-------:|------:|--------:|
| **Time** | **9.6s** | 900s | 456s | 4555s |
| **Figures** | 0 | 20 | 21 | 4 |
| **Refs** | 17 | 0 | — | 0 |
| **Sections** | 52 | 50 | — | 33 |
| **MD chars** | 58,647 | 64,541 | — | 66,067 |
| **MD lines** | 473 | 442 | — | 531 |

### Speed

| Backend | Total (27pg) | Pages/min |
|---------|------------:|---------:|
| **Docling** | 20s | **81.0** |
| **Surya** | 754s | 2.1 |
| **Marker** | 2071s | 0.8 |
| **Chandra** | 10,548s | **0.15** |

## Manual Review Findings

> [!IMPORTANT]
> Qualitative review by Shahin reveals that quantitative metrics alone are misleading. Chandra is the clear winner on extraction fidelity despite being the slowest.

### Docling

| Aspect | Rating | Notes |
|--------|--------|-------|
| **Main text** | ✅ Decent | Captures text body accurately |
| **Tables** | ❌ Fails | Tables not properly parsed (KEY RESOURCES TABLE as flat text, with some markdown tables working) |
| **Equations** | ❌ Fails | Renders as `<!-- formula-not-decoded -->` placeholders |
| **Figures** | ❌ Fails | All figures replaced with `<!-- image -->` comments, zero extraction |
| **Structural artifacts** | ❌ Fails | Retains "Article" header stamps, "Please cite this article..." watermarks, column-break artifacts |
| **Citations** | ❌ Fails | Inline citations rendered as bare numbers (e.g., `1-4` instead of `[1-4]` or superscripts), no semantic linking |
| **Text flow** | ⚠️ Messy | Excessive whitespace from column-layout rendering: `singlecell  foundation  models` with multiple spaces |

### Marker

| Aspect | Rating | Notes |
|--------|--------|-------|
| **Main text** | ✅ Good | Clean body text, fewer spacing artifacts than Docling |
| **Tables** | ⚠️ Partial | Some table recognition but inconsistent |
| **Equations** | ⚠️ Attempts | Tries to render but not always successful |
| **Figures** | ✅ Good | 9 figures from AlphaGenome (all 7 main + 2 misc), 20 from PaSCient (includes sub-panel crops) |
| **Structural artifacts** | ⚠️ Partial | Cleans some artifacts but text structure still messy |
| **Citations** | ❌ Fails | References section not cleanly delimited |
| **Text flow** | ⚠️ Messy | Better than Docling but still exhibits layout-induced structural noise |

### Surya (Layout-only)

| Aspect | Rating | Notes |
|--------|--------|-------|
| **Layout detection** | ✅ Good | Correctly identifies Figure, Picture, Caption, SectionHeader, Table, Equation elements |
| **Figure bounding boxes** | ✅ Good | 8 AlphaGenome figures, 21 PaSCient detections with confidence scores |
| **Text extraction** | ❌ N/A | Layout-only tool, no markdown or text output generated |

> [!NOTE]
> Surya output exists at `data/processed/papers_test/focused/{Paper}/surya/` with `figures/` and `summary.json`. It is layout-only (no `.md` file), which may cause confusion when browsing the directory.

### Chandra ⭐

| Aspect | Rating | Notes |
|--------|--------|-------|
| **Main text** | ✅ Excellent | Clean, flowing prose with proper paragraph breaks |
| **Tables** | ✅ Good | Renders KEY RESOURCES TABLE as proper HTML `<table>` with headers, even reconstructs figure chart data as tables |
| **Equations** | ✅ Excellent | Full LaTeX: `$X_i \in \mathbb{R}^{M_i \times d_g}$`, numbered equations with labels |
| **Figures** | ✅ Good | 8/8 AlphaGenome figures. 4/7 PaSCient main figures (pages 4-7) |
| **Figure descriptions** | ✅ Excellent | VLM generates detailed alt-text descriptions of each figure's visual content |
| **Structural artifacts** | ✅ Clean | No "Article" stamps, no "Please cite..." watermarks, no column-break noise |
| **Citations** | ✅ Good | Superscript format preserved: `<sup>1-4</sup>`, DOIs as hyperlinks |
| **References** | ✅ Excellent | Full structured refs with authors, titles, journals, DOIs as proper links |
| **Text flow** | ✅ Excellent | Natural paragraph structure, no double-spacing artifacts |

**PaSCient Figure 1 miss**: Chandra extracted 4/7 PaSCient figures (pages 4-7 only). Figure 1 was missed because it uses a non-standard layout: the figure spans both columns but has its caption embedded on the right side of the figure panel rather than below it. This is an unusual layout that challenges the VLM's figure detection heuristics.

## Detailed Quality Comparison (PaSCient paper excerpt)

### Equations

| Backend | Rendering |
|---------|-----------|
| **Docling** | `<!-- formula-not-decoded -->` (total failure) |
| **Marker** | Partial — some equations as text, some missing |
| **Chandra** | `$$\mathbf{w}_i = \text{softmax}(a_\theta(\mathbf{Z}_i)) \quad (\text{Equation 1})$$` ✅ |

### Inline Citations

| Backend | Example |
|---------|---------|
| **Docling** | `...biology. 1-4 In particular...` (bare numbers, extra spaces) |
| **Marker** | Similar bare numbers |
| **Chandra** | `...biology.<sup>1–4</sup> In particular...` (proper superscript) ✅ |

### Structural Noise

| Backend | Artifacts Present |
|---------|-------------------|
| **Docling** | `Article` (repeated as section header), `Please cite this article in press as...` (repeated 4x), `<!-- image -->` placeholders |
| **Marker** | Some reduced but still present |
| **Chandra** | None ✅ |

### Reference Quality

| Backend | Example Ref #1 |
|---------|----------------|
| **Docling** | `1. Arowoogun,  J.O.,  Babawarun,  O...` (multi-space artifacts, no DOI links) |
| **Chandra** | `1. Arowoogun, J.O., ... *World J. Adv. Res. Rev.* 21, 1810–1821. <https://doi.org/10.30574/...>` ✅ |

## Verdict

| Criterion | Winner | Runner-up |
|-----------|--------|-----------|
| **Speed** | Docling (81 pg/min) | Surya (2.1 pg/min) |
| **Text quality** | **Chandra** | Marker |
| **Equation fidelity** | **Chandra** | — |
| **Table parsing** | **Chandra** | Docling (markdown tables only) |
| **Figure extraction** | Marker/Surya (quantity) | **Chandra** (quality + descriptions) |
| **Citation handling** | **Chandra** | Docling (partial) |
| **Reference structure** | **Chandra** | Docling |
| **Artifact cleanup** | **Chandra** | Marker |
| **Overall fidelity** | **Chandra** ⭐ | Marker |

## Production Strategy

| Tier | Backend | Use Case | Speed |
|------|---------|----------|-------|
| **Tier 1 (Default)** | Docling | Fast triage, bulk indexing, search corpus | 81 pg/min |
| **Tier 2 (Figures)** | Surya | Layout analysis, figure bounding boxes for any paper | 2.1 pg/min |
| **Tier 3 (Quality)** | Chandra | High-fidelity extraction for KG ingestion, equations, structured refs | 0.15 pg/min |
| **Tier 4 (Hybrid)** | Marker | Fallback all-in-one when Chandra is too slow | 0.8 pg/min |

**Recommended pipeline**: Docling for fast first-pass → Chandra for papers entering the Knowledge Graph. Surya for figure bounding box augmentation when Chandra misses figures (e.g., non-standard layouts).

## Output Locations

```
data/processed/papers_test/focused/
├── AlphaGenome/
│   ├── docling/   AlphaGenome.md (80KB, 322 lines)
│   ├── marker/    AlphaGenome.md (86KB) + figures/ (9 jpeg)
│   ├── surya/     summary.json + figures/ (8 png)
│   └── chandra/   AlphaGenome.md (102KB, 1333 lines) + .html + figures/ (8 webp)
└── PaSCient/
    ├── docling/   PaSCient.md (57KB, 473 lines)
    ├── marker/    PaSCient.md (63KB) + figures/ (20 jpeg)
    ├── surya/     summary.json + figures/ (21 png)
    └── chandra/   PaSCient.md (64KB, 531 lines) + .html + figures/ (4 webp)
```

## Environment Notes

- `transformers` upgraded 4.57.6 → 5.8.1 for Chandra (Qwen3.5 architecture)
- `marker-pdf 1.10.2` has `transformers<5.0.0` constraint — functionally unaffected
- AOTriton: Marker layout went from ~7 min/page → 1.7s/page (250x speedup)
- Chandra model: `datalab-to/chandra-ocr-2` (5.3B params, 10.6 GB bf16)
