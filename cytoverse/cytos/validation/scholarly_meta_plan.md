# Scholarly Meta-Wrapper Architecture

## Module Map

| New Module | Responsibility | Reuses From |
|---|---|---|
| `paper_profile.py` | Meta-wrapper: gathers all info for a paper | `citations.py`, `intelligence.py`, `pdf.py` |
| `download.py` | Paper PDF retrieval from multiple sources | `pypaperretriever.PaperRetriever` |
| `classify.py` | Publication type, scale, computational tags | `intelligence.py` (patterns), PubMed MeSH |
| `citation_graph.py` | Network expansion, reference classification, prioritization | `intelligence.py`, `citations.py` |

## 1. `classify.py` — Paper Classification Taxonomy

### Publication Types (from NLM MeSH)
- Journal Article, Review, Meta-Analysis, Clinical Trial, Case Report, Dataset, Preprint, etc.

### Scale Tags (multi-label)
- `molecular`, `cellular`, `tissue`, `organ`, `connectomics`, `organism`, `population`, `clinical`

### Computational Tags
- `computational/discovery` — uses existing tools for science
- `computational/modeling` — introduces new methods/models
- Flags: `has_code`, `has_model`, `has_pretrained_weights`, `code_upon_request`, `no_code`

### Data Tags
- `data_generation/novel` — generated new dataset
- `data_generation/curation` — curated existing data

## 2. `download.py` — Paper Retrieval

Wraps `pypaperretriever.PaperRetriever` with:
- Proxy/institution support (configurable)
- Preprint fallback (bioRxiv/medRxiv/arXiv)
- Open journal direct download
- Unpaywall + Sci-Hub (optional)

## 3. `paper_profile.py` — Meta-Wrapper

Main entry: `profile_paper(doi=, pmid=, pdf_path=, config=)`
- Resolves identifiers (DOI ↔ PMID ↔ PMC ↔ OpenAlex)
- Finds preprint ↔ published version
- Classifies (type, scale, computational, data)
- Extracts entities (code, models, datasets)
- Fetches references + classifies them
- Scores paper (citation quality, foundational)
- Returns `PaperProfile` dataclass

## 4. `citation_graph.py` — Citation Network

- `build_citation_graph(seeds, ...)` — expand from seeds with filters
- `classify_references_by_role(...)` — modeling/dataset/used/benchmarked
- `prioritize_papers(graph, ...)` — centrality, citation count, PageRank
