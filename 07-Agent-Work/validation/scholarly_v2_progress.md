# Scholarly Pipeline V2 — Final Status

> All 7 workstreams complete | 7 commits | 3 new modules | 13 modules total | ~190 KB

## Completed Workstreams

### WS1: Content Quality ✅
- `extract_figures()`: caption-paired extraction, page rendering for vector figures
- `inline_highlights_in_markdown()`: CriticMarkup/HTML/MyST annotation inlining
- **Known issue**: Page rendering captures full page, not figure bounding box. Needs GROBID/pdffigures2 for cropping. Some false-positive non-figures included.

### WS2: Reference Extraction ✅
- 4-strategy `_extract_reference_section()`: heading → spaced → numbered-dense → DOI-dense
- `_search_additional_identifiers()`: PubMed, arXiv, OpenAlex title search
- `cleanup_references_online()`: CrossRef + Google Scholar verification

### WS3: NER Ontology Alignment ✅
- `TARGET_ONTOLOGIES`: 9 entity types → canonical ontologies
- `biomedical_config()`: pre-tuned NERConfig for scholarly papers
- `tag_with_mesh()`: PubMed MEDLINE MeSH extraction — tested ✓
- `auto_tag_topics()`: multi-source tagging (MeSH + keyword)

### WS4: Resource Resolution ✅
- `resource_resolver.py`: GitHub/HF/GEO/Zenodo resolution + DUO access classification
- `search_data_access()`: 11 known repositories with access URLs

### WS5: Model & Dataset Helpers ✅
- `model_helpers.py`: param counting (ESM2: 649M ✓), model card, ONNX conversion, Mermaid arch viz
- `dataset_helpers.py`: unified metadata fetch, 30+ data type mappings, size estimation

### WS6: Scoring ✅
- Field-normalized citation percentile, influential citation ratio
- `score_explanation` field, `compute_topic_relevance()` for network filtering

### WS7: Topic Tagging ✅ (via WS3)
- MeSH descriptors via PubMed MEDLINE
- Keyword extraction via frequency analysis

## Known Issues (for next iteration)

1. **Figure extraction**: Full-page rendering instead of figure bounding boxes; non-figure raster images included. Need GROBID TEI XML figure coordinates or pdffigures2 for proper cropping.
2. **Reference cleanup**: Google Scholar scraping is fragile (rate limits, CAPTCHA). Should prefer Semantic Scholar API.
3. **NER grounding**: Rule-based NER has inherent precision limits. scispaCy + UMLS linker installation needed for production.

## Module Inventory (13 files, ~190 KB)

| Module | Lines | Purpose |
|--------|-------|---------|
| `pdf.py` | 956 | Metadata, content, figures, highlights, references |
| `intelligence.py` | 716 | Citation network, scoring, classification, topics |
| `ner.py` | 728 | NER, ontology alignment, MeSH/UMLS tagging |
| `resource_resolver.py` | 605 | URL resolution, license/access classification |
| `annotation.py` | 370 | W3C WADM annotation store |
| `ingest.py` | 400 | OpenAlex/SemOpenAlex/PKG ingestion |
| `zotero.py` | 400 | Zotero integration |
| `export.py` | 350 | BibTeX/RIS/model card export |
| `dataset_helpers.py` | 320 | Dataset metadata, type classification, ref cleanup |
| `model_helpers.py` | 280 | Model card, params, conversion, arch viz |
| `topics.py` | 300 | OpenAlex topic hierarchy |
| `kg.py` | 280 | KG upsert and personalization |
