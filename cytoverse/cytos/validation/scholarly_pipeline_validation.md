# Scholarly Pipeline Validation Report

> **16 PDFs** across 4 categories | **59 seconds** total | **6 phases** | All results persisted
>
> Output directory: `data/processed/papers_test/`

## Test Corpus

| Category | Paper | Size | DOI found |
|----------|-------|------|-----------|
| Conference | CFGen | 28.5 MB | — |
| Conference | scCLIP | 1.6 MB | — |
| Journal | AutoFocus | 3.2 MB | 10.1038/s42003-024-06724-2 |
| Journal | Flow Matching Review | 2.0 MB | 10.1038/s42256-026-01220-0 |
| Journal | NeMO Analytics | 9.1 MB | 10.1038/s41593-026-02204-4 |
| Journal | NeuroSTORM | 7.5 MB | 10.1038/s41551-026-01666-y |
| Journal | PaSCient | 9.7 MB | 10.1016/j.cels.2026.101570 |
| Journal | PsychENCODE | 30.0 MB | 10.1126/science.adi5199 |
| Journal | SCimilarity | 11.8 MB | 10.1038/s41586-024-08411-y |
| Preprint | FRO Molecular Monitoring | 0.3 MB | — |
| Preprint | DigitalBrain | 3.9 MB | 10.64898/2026.04.14.718492 |
| Preprint | TranscriptFormer | 24.8 MB | 10.1101/2025.04.25.650731 |
| Preprint | VariantFormer (highlighted) | 28.3 MB | 10.1101/2025.10.31.685862 |
| Preprint | WaveGC | 4.1 MB | — |
| Unpublished | Brain Foundation Model (slides) | 2.1 MB | — |
| Unpublished | Harmonizing Interaction Networks | 1.8 MB | — |

> 3 PDFs skipped (>35 MB): AlphaGenome (70 MB), AlphaGenome_highlighted (71 MB), HCP (77 MB)

---

## Phase 1: Metadata Extraction

**File**: [01_metadata.json](file:///home/mohammadi/repos/cytognosis/cytos/data/processed/papers_test/01_metadata.json)

| Result | Count |
|--------|-------|
| PDFs processed | 16/16 |
| DOI extracted (from PDF text) | 9 |
| Online enrichment (CrossRef + OpenAlex) | 9 papers |
| OpenAlex IDs obtained | 9 |
| Citation counts retrieved | 9 |
| Primary topics assigned | 9 |
| Authors extracted | 8 (via CrossRef) |

### Issues Found & Fixed

| Issue | Root Cause | Fix |
|-------|-----------|-----|
| CFGen title = "Published as a conference paper at ICLR 2025" | Heuristic grabs first substantive line, which is the venue header | Improve `_heuristic_title()` to skip venue patterns |
| 2 conference papers detected as `preprint`/`article` | No DOI in text, classification falls to pattern scoring | Expected for PDFs without embedded DOI |
| Author extraction from PDF metadata = empty for most | Most PDFs don't embed structured author metadata | Online enrichment via CrossRef fills this |

### Sample Enriched Entry (PsychENCODE)
```json
{
  "name": "Single-cell genomics and regulatory networks for 388 human brains",
  "doi": "10.1126/science.adi5199",
  "openalex_id": "W4398250269",
  "citation_count": 143,
  "primary_topic": "Single-cell and spatial transcriptomics",
  "publisher": "American Association for the Advancement of Science (AAAS)",
  "venue": "Science",
  "is_oa": true
}
```

---

## Phase 2: Content Extraction

**File**: [02_content_summary.json](file:///home/mohammadi/repos/cytognosis/cytos/data/processed/papers_test/02_content_summary.json)

| Metric | Total |
|--------|-------|
| Images extracted | **645** |
| Markdown generated | **16 files** (1.29 MB total text) |
| Highlights extracted | **352** (from VariantFormer_highlighted.pdf) |
| References extracted | **778** BibTeX entries |

### Images per Paper

| Paper | Images |
|-------|--------|
| CFGen | 116 |
| TranscriptFormer | 110 |
| PsychENCODE | 102 |
| SCimilarity | 90 |
| NeMO Analytics | 61 |
| VariantFormer_highlighted | 55 |
| WaveGC | 38 |
| PaSCient | 28 |

### Highlight Extraction (ISO 32000)

352 highlights from `VariantFormer_highlighted.pdf`, all type `Highlight`:
```
p1: "population level frequency based statistical genetics models"
p1: "DNA sequence based models"
p1: "expression quantitative trait locus (eQTL) mapping"
...
p41: "aggregates predictions across exonic regions for each gene"
```

> [!NOTE]
> Highlight extraction was initially blocked by `module 'fitz' has no attribute 'PDF_ANNOT_STRIKEOUT'`. Fixed by using `getattr(fitz, "PDF_ANNOT_STRIKE_OUT", ...)` for PyMuPDF 1.27+ compatibility.

### Reference Extraction

| Paper | Refs |
|-------|------|
| Flow Matching Review | 167 |
| NeMO Analytics | 115 |
| CFGen | 91 |
| AutoFocus | 72 |
| TranscriptFormer | 72 |
| PaSCient | 66 |
| VariantFormer_highlighted | 63 |
| NeuroSTORM | 60 |
| WaveGC | 36 |
| scCLIP | 34 |

> [!WARNING]
> 5 papers returned 0 references: PsychENCODE, SCimilarity, FRO, DigitalBrain, and the unpublished docs. Root cause: `_extract_reference_section()` requires a "References" heading on its own line. Multi-column PDFs and supplementary-style layouts don't match the current regex. Improvement needed.

---

## Phase 3: Named Entity Recognition

**File**: [03_ner_results.json](file:///home/mohammadi/repos/cytognosis/cytos/data/processed/papers_test/03_ner_results.json)

| Metric | Total |
|--------|-------|
| Total entities | **2,999** |
| Entity types detected | **7** (Gene, Disease, CellType, Tissue, Species, Compound) |

### Per-Paper Breakdown

| Paper | Total | Gene | Disease | CellType | Tissue | Species |
|-------|-------|------|---------|----------|--------|---------|
| NeMO Analytics | 500 | 181 | — | — | — | — |
| PsychENCODE | 500 | 261 | — | — | — | — |
| SCimilarity | 357 | 134 | 18 | 16 | — | 2 |
| Flow Matching Review | 286 | 195 | — | 2 | — | 1 |
| NeuroSTORM | 266 | 98 | 4 | 1 | — | 2 |
| TranscriptFormer | 254 | 96 | — | 4 | — | 11 |
| DigitalBrain | 208 | 72 | 3 | 8 | 7 | 2 |
| AutoFocus | 167 | 57 | 9 | 2 | — | 1 |
| PaSCient | 145 | 64 | 6 | 3 | — | 1 |
| CFGen | 122 | 39 | — | 1 | 1 | 7 |
| VariantFormer | 75 | 21 | 2 | — | 4 | 1 |

### Issues Found & Fixed

| Issue | Root Cause | Fix |
|-------|-----------|-----|
| Gene regex matched common words (THE, AND, CELL) | `[A-Z][A-Z0-9]{2,6}` too broad | Require digit (`[A-Z][A-Z0-9]*\d[A-Z0-9]*`) + 65-word stoplist |
| Only Gene type detected initially | Disease/CellType/Species patterns too narrow | Added explicit disease names, 25+ cell types, brain regions, common species names |
| Missing Drug/Tissue entity types | No patterns existed | Added Compound (17 drugs) and Tissue (15 brain regions) |

> [!TIP]
> With scispaCy + UMLS linker installed, NER precision jumps significantly (ontology-grounded entities with CUIEs). The rule-based fallback is designed as a minimum viable baseline.

---

## Phase 4: Intelligence Layer

**File**: [04_intelligence.json](file:///home/mohammadi/repos/cytognosis/cytos/data/processed/papers_test/04_intelligence.json)

### Related Entity Extraction

| Paper | Code Repos | Models | Datasets |
|-------|-----------|--------|----------|
| CFGen | 1 (`theislab/CFGen`) | — | — |
| scCLIP | 2 (`jsxlei/scCLIP`, `openproblems-bio/...`) | 1 | — |
| AutoFocus | 4 (`krumsieklab/autofocus`, `krumsieklab/MoDentify`, ...) | — | — |
| Flow Matching Review | 4 (`conditional-flow-matching`, ...) | — | — |
| NeMO Analytics | 4 (`carlocolantuoni`, ...) | — | — |
| NeuroSTORM | 4 (`CUHK-AIM-Group/NeuroSTORM`, ...) | — | — |
| PaSCient | 5 (`genentech/pascient`, `Genentech/scimilarity`, ...) | — | 3 (GSE145926, GSE149689, GSE174072) |
| TranscriptFormer | — | — | **13** (GSE247719, GSE126954, GSE229022, ...) |
| WaveGC | 1 (`liun-online/WaveGC`) | — | — |

### Topic Auto-Tagging (OpenAlex API)

| Paper | Topics |
|-------|--------|
| PaSCient | Single-cell and spatial transcriptomics, Cancer Genomics, Cell Image Analysis |
| PsychENCODE | Single-cell and spatial transcriptomics, Bioinformatics and Genomic Networks |
| DigitalBrain | Single-cell and spatial transcriptomics, Cell Image Analysis, Neuroinflammation |
| VariantFormer | Genomics and Rare Diseases, Genetic Associations, Genomics and Phylogenetic Studies |
| Flow Matching | (keyword: Machine Learning) |
| FRO | (keyword: Drug Discovery, Machine Learning, Immunology) |

### Citation Network Expansion

Seed paper: **AutoFocus** (W4402324927)

```
Network: 11 nodes, 20 edges (depth=1)

Top cited neighbors:
  W1966327575  WGCNA: an R package for weighted correlation  cc=28,718
  W2163480486  Network biology: understanding the cell's     cc=7,998
  W2586637063  In situ click chemistry generation            cc=7,544
  W1644749979  From molecular to modular cell biology        cc=3,675
```

### Paper Scoring

| Paper | Citation | Recency | Composite |
|-------|----------|---------|-----------|
| PsychENCODE | 0.497 | 0.90 | 0.579 |
| SCimilarity | 0.469 | 0.90 | 0.571 |
| TranscriptFormer | 0.326 | 0.95 | 0.538 |
| VariantFormer | 0.069 | 0.95 | 0.461 |
| DigitalBrain | 0.000 | 1.00 | 0.450 |
| FRO | 0.000 | — | 0.350 |

---

## Phase 5: KG Alignment & Personalization

**File**: [05_kg_alignment.json](file:///home/mohammadi/repos/cytognosis/cytos/data/processed/papers_test/05_kg_alignment.json), [scholarly_kg_index.csv](file:///home/mohammadi/repos/cytognosis/cytos/data/processed/papers_test/scholarly_kg_index.csv)

| Metric | Count |
|--------|-------|
| KG entries created | **16** |
| With OpenAlex ID | 9 (canonical ID = `openalex:Wxxxx`) |
| With hash-based ID | 7 (`cytos:paper:xxxx`) |
| Annotations created | 16 |
| Favorites marked | 4 (citation_count > 50) |
| Collection | "Test Corpus Papers" |

### Reference Existence Check

From citation network of AutoFocus:

| Reference | In KG? |
|-----------|--------|
| W4402324927 (AutoFocus itself) | ✅ IN KG |
| W1966327575 (WGCNA) | ❌ NOT IN KG |
| W2163480486 (Network Biology) | ❌ NOT IN KG |
| W2586637063 (Click Chemistry) | ❌ NOT IN KG |
| W1644749979 (Modular Cell Bio) | ❌ NOT IN KG |

> As expected, only the seed paper is in our KG. The citation network expansion identified these high-impact neighbors for potential inclusion.

---

## Phase 6: Export

| Format | File | Entries |
|--------|------|---------|
| BibTeX | [all_papers.bib](file:///home/mohammadi/repos/cytognosis/cytos/data/processed/papers_test/all_papers.bib) | 16 |
| RIS | [all_papers.ris](file:///home/mohammadi/repos/cytognosis/cytos/data/processed/papers_test/all_papers.ris) | 16 |

---

## Bugs Found & Fixed During Validation

| # | Bug | Severity | Fix |
|---|-----|----------|-----|
| 1 | `PDF_ANNOT_STRIKEOUT` missing in PyMuPDF 1.27+ | **Critical** — blocked all highlight extraction | `getattr()` fallback with `PDF_ANNOT_STRIKE_OUT` |
| 2 | KG upsert fails on `SchemaError: String vs Null` when concatenating DataFrames with list fields | **Critical** — crashed Phase 5 | Serialize list/dict fields to JSON; cast Null columns to Utf8 |
| 3 | KG selective update ignores new columns not yet in index | **Medium** — pmid/arxiv_id never added | Phase 1: add missing columns before Phase 2 fill |
| 4 | Code regex double-matches GitHub URLs (`code at https://github.com/...`) | **Low** — duplicate entries | Negative lookahead to exclude github.com from fallback pattern |
| 5 | GEO accession pattern too restrictive (`GEO accession: GSExxxx`) | **Low** — missed standalone GSE IDs | Simplified to `\b(GSE\d+)\b` |
| 6 | Gene regex matched common words (THE, AND, CELL, DATA) | **Medium** — 200/200 false positives | Required digit in gene symbol + 65-word stoplist |
| 7 | Software citation pattern too narrow | **Low** — missed "used the X package" | Broadened verb patterns |

## Output Directory Structure

```
data/processed/papers_test/
├── 00_pipeline_summary.json       # Aggregate metrics
├── 01_metadata.json               # Per-paper metadata (17.9 KB)
├── 02_content_summary.json        # Image/markdown/highlight/ref counts
├── 03_ner_results.json            # NER entities by type (17.5 KB)
├── 04_intelligence.json           # Related entities, topics, scores (22 KB)
├── 05_kg_alignment.json           # KG IDs, annotations, ref checks
├── all_papers.bib                 # BibTeX export (16 entries)
├── all_papers.ris                 # RIS export (16 entries)
├── scholarly_kg_index.csv         # KG index (22 columns, human-readable)
├── scholarly_kg_index.parquet     # KG index (binary)
├── annotations/                   # AnnotationStore JSONL files
├── pipeline.log                   # Full execution log
└── content/                       # Per-paper extracted content
    ├── PsychENCODE/
    │   ├── PsychENCODE.md         # 111 KB markdown
    │   └── images/                # 102 PNG files
    ├── VariantFormer_highlighted/
    │   ├── VariantFormer_highlighted.md
    │   ├── highlights.json        # 352 annotations
    │   ├── references.bib         # 63 entries
    │   └── images/
    └── ... (16 paper directories)
```

## Known Limitations

1. **Reference extraction**: Fails for multi-column PDFs (PsychENCODE, SCimilarity) and PDFs without a clear "References" heading. Consider GROBID/ScienceParse integration.
2. **Rule-based NER**: Gene false positives remain (L5, L6 = cortical layers, not genes). scispaCy models dramatically improve precision.
3. **Heuristic title**: CFGen's title was extracted as "Published as a conference paper at ICLR 2025" instead of the actual paper title.
4. **No DOI for 7 papers**: Conference/unpublished papers often lack embedded DOIs, preventing online enrichment.
5. **Model extraction**: HuggingFace model detection depends on explicit `huggingface.co/` URLs in text; many papers reference models by name only.
