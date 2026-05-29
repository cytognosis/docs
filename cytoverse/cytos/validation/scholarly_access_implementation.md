# Scholarly Access Implementation

## New Modules Created

### 1. Semantic Scholar Client — [semantic_scholar.py](file:///home/mohammadi/repos/cytognosis/cytos/src/cytos/scholarly/semantic_scholar.py)

Free, official API. No CAPTCHA, no blocking, structured JSON.

| Function | Purpose | Tested |
|----------|---------|--------|
| `search_author(name)` | Name search → top result enriched via get_author | ✅ |
| `get_author(id)` | Full author by S2 ID, ORCID, or DBLP key | ✅ |
| `get_author_papers(id)` | Paginated paper list (100/page) | ✅ |
| `search_papers(query)` | Paper search with TLDRs, influence scores | ✅ |
| `get_paper(id)` | Full paper by S2/DOI/ArXiv/PMID | ✅ |
| `get_citations(id)` | Citing papers with context + intents | ✅ |
| `get_references(id)` | Referenced papers with context | ✅ |
| `batch_get_papers(ids)` | Up to 500 papers per POST (free) | ✅ |

**Rate limiting**: Built-in 1.1s interval. Supports `S2_API_KEY` env var for dedicated throughput.

### 2. SerpAPI Scholar Client — [serp_scholar.py](file:///home/mohammadi/repos/cytognosis/cytos/src/cytos/scholarly/serp_scholar.py)

Managed Google Scholar proxy. 250 free searches/month.

| Function | Purpose |
|----------|---------|
| `search_scholar_profiles(name)` | Find Scholar IDs by name |
| `get_scholar_author(scholar_id)` | Full profile: h-index, i10, citations/year, co-authors, pubs |
| `search_scholar_papers(query)` | Paper search with citations, versions |
| `get_paper_citations(cites_id)` | Papers citing a specific work |
| `is_available()` | Check if API key configured |

**Config**: `SERPAPI_KEY` env var or `~/.config/cytos/secrets.yaml`

### 3. Cache Layer — [cache.py](file:///home/mohammadi/repos/cytognosis/cytos/src/cytos/scholarly/cache.py)

Disk-backed JSON cache at `~/.cache/cytos/scholarly/`.

| Function | Purpose |
|----------|---------|
| `get(namespace, id, ttl)` | Retrieve if valid |
| `put(namespace, id, payload)` | Store with timestamp |
| `invalidate(namespace, id)` | Remove specific entry |
| `clear_namespace(ns)` | Clear all entries in namespace |
| `stats()` | Entry counts + sizes by namespace |

**TTL defaults**: Author=30d, Paper=90d, Institution=180d, ORCID=14d.

### 4. Updated Google Scholar — [google_scholar.py](file:///home/mohammadi/repos/cytognosis/cytos/src/cytos/scholarly/google_scholar.py)

`get_scholar_profile()` now uses tiered fallback:
1. **Disk cache** (instant)
2. **SerpAPI** (reliable, paid) — via `serp_scholar.py`
3. **`scholarly` library** (free, unreliable)
4. **OpenAlex** (free, always works)

All responses cached automatically.

## Verified Test Results

```
=== Semantic Scholar ===
  Author search: Ananth Grama → S2 ID, h=1 (disambiguation issue - common name)
  Paper search: "scGPT single cell" → 975 citations, TLDR ✅

=== Cache ===
  put/get/miss/stats/clear: all passing ✅

=== Google Scholar Fallback ===
  SerpAPI → scholarly → OpenAlex cascade: working ✅
  Ananth Grama → OpenAlex fallback: h=46, cites=12999 ✅

=== Lint ===
  ruff check: All checks passed ✅
```

## Setup Required

| Service | Action | Priority |
|---------|--------|----------|
| SerpAPI | Register at [serpapi.com](https://serpapi.com), set `SERPAPI_KEY` | P0 |
| Semantic Scholar | Request key at [semanticscholar.org](https://www.semanticscholar.org/product/api), set `S2_API_KEY` | P1 |
| OpenAlex | Register key at [openalex.org](https://openalex.org) (optional, free tier works) | P2 |
