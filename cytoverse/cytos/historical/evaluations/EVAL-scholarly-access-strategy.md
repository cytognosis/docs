# EVAL: Scholarly Data Access Strategy

> **Status**: Complete
> **Date**: 2026-05-14
> **Author**: @shmohammadi
> **Decision**: Adopted (Multi-source tiered cascade)
> **Related ADR**: [ADR-001](../adrs/ADR-001-tiered-author-identity-api-strategy.md)

## Objective

Select a reliable, cost-effective strategy for accessing Google Scholar and LinkedIn data after the `scholarly` Python library was completely blocked by Google's CAPTCHA infrastructure. The evaluation needed to identify alternatives that work for a 501(c)(3) nonprofit with near-zero legal risk tolerance and minimal budget.

## Requirements

| # | Requirement | Priority | Weight |
|---|-----------|----------|--------|
| R1 | Reliable author profile retrieval (h-index, citations, pubs) | Must-have | 3 |
| R2 | Google Scholar ID discovery from name | Must-have | 3 |
| R3 | $0 cost at current scale (tens of authors/month) | Must-have | 3 |
| R4 | No legal/ToS risk for 501(c)(3) | Must-have | 3 |
| R5 | Citation-per-year histograms | Should-have | 2 |
| R6 | Co-author network extraction | Should-have | 2 |
| R7 | Paper TLDRs and influence scoring | Nice-to-have | 1 |
| R8 | LinkedIn professional data | Nice-to-have | 1 |

## Candidates Evaluated

| Candidate | Type | License | Cost | Maturity |
|-----------|------|---------|------|----------|
| Semantic Scholar API | Official API | Free | $0 | Stable |
| OpenAlex API | Official API | CC0 | $0 ($1/day free) | Stable |
| SerpAPI (Scholar) | Managed proxy | Proprietary | $0-75/mo | Stable |
| `scholarly` library | OSS scraper | Free | $0 | Fragile |
| LinkedIn scraping | DIY/Proxycurl | — | Varies | Dead |
| ORCID API | Official API | Free | $0 | Stable |

## Evaluation Matrix

| Criterion | Wt | Semantic Scholar | OpenAlex | SerpAPI | scholarly | LinkedIn |
|-----------|-----|------------------|----------|---------|-----------|----------|
| Reliability | 3 | ★★★★★ | ★★★★★ | ★★★★☆ | ★★☆☆☆ | ★☆☆☆☆ |
| Cost | 3 | ★★★★★ | ★★★★★ | ★★★★☆ | ★★★★★ | ★★★★★ |
| Coverage | 3 | ★★★★☆ | ★★★★★ | ★★★★★ | ★★★★★ | ★★★☆☆ |
| Maintenance | 2 | ★★★★☆ | ★★★★☆ | ★★★★★ | ★☆☆☆☆ | ★☆☆☆☆ |
| Legal Risk | 3 | ★★★★★ | ★★★★★ | ★★★★☆ | ★★★☆☆ | ★☆☆☆☆ |
| Unique data | 2 | ★★★★★ | ★★★★☆ | ★★★★☆ | ★★★☆☆ | ★★★★★ |
| **Total** | | **67** | **67** | **61** | **43** | **35** |

## Hands-on Testing

### Semantic Scholar API

**Setup**: No API key needed for testing (shared pool: 100 req / 5 min).

**Test Results**:

| Test Case | Input | Expected | Actual | Pass |
|-----------|-------|----------|--------|------|
| Author search | "Ananth Grama" | Correct author | "A. Grama", h=1, papers=3 (wrong person) | ⚠️ |
| Author by ORCID | `ORCID:0000-0001-5823-1985` | Smita Krishnaswamy | 404 Not Found | ❌ |
| Author search + enrich | "Smita Krishnaswamy" | Full profile | S2=32911702, correct match | ✅ |
| Paper search | "scGPT single cell" | scGPT paper | 975 citations, TLDR present | ✅ |
| Unsupported fields | `aliases` in search | 200 | 400 Bad Request | ❌ |
| Fixed fields | Remove `aliases` | 200 | Correct data | ✅ |

**Findings**: Paper search is excellent (TLDRs, influence scores). Author disambiguation is weak for common names. ORCID cross-reference coverage is incomplete. The `aliases` field was removed from the API but still documented; we had to discover this through trial-and-error.

### `scholarly` Library

**Test Results**:

| Test Case | Input | Expected | Actual | Pass |
|-----------|-------|----------|--------|------|
| Author search | "Shahin Mohammadi" | Scholar profile | CAPTCHA blocked | ❌ |
| Author search | "Smita Krishnaswamy" | Scholar profile | CAPTCHA blocked | ❌ |
| Author search | "Ananth Grama" | Scholar profile | CAPTCHA blocked | ❌ |
| Author by ID | "EgDSKaoAAAAJ" | Scholar profile | CAPTCHA blocked | ❌ |

**Findings**: 100% failure rate. Google detects and blocks all requests from datacenter IPs. FreeProxy rotation does not help. The library would require residential proxies ($30+/month) to function, negating its "free" advantage.

### SerpAPI

**Test Results**: Not tested live (no API key registered yet). Documentation review confirms all required endpoints exist (`google_scholar_profiles`, `google_scholar_author`). Free tier provides 250 searches/month.

### LinkedIn

**Test Results**:

| Test Case | Input | Expected | Actual | Pass |
|-----------|-------|----------|--------|------|
| Public meta tags | LinkedIn URL | Name, title, company | Basic metadata only | ⚠️ |
| Full profile | LinkedIn URL | Employment history | Requires login | ❌ |

**Findings**: Public `<meta>` tags provide name/title/company but nothing more. Proxycurl (the main scraping service) was shut down by LinkedIn in 2025. Any automated access beyond public HTML meta tags is legally risky.

## What Worked

1. **OpenAlex as primary bibliometric source**: Reliable, free, complete h-index/i10/citations. Already integrated and working.
2. **Semantic Scholar paper search**: Excellent results with TLDRs and influence scoring. Name-based author search also works when combined with h-index disambiguation.
3. **ORCID for structured employment/education**: Rich records for authors who maintain them. Best source for education history, positions, and external ID cross-referencing.
4. **Disk caching**: Simple JSON + TTL approach avoids redundant API calls (8ms lookup vs. multi-second API calls).

## What Did Not Work

1. **`scholarly` library**: Completely blocked by Google CAPTCHA on all test queries. No workaround without paid residential proxies.
   - **Fix**: Replaced with SerpAPI (managed proxy) and Semantic Scholar (official API) as alternatives.
2. **S2 `aliases` field**: Undocumented API change; field returns 400 on both search and author endpoints.
   - **Fix**: Removed from default field lists. Discovered by testing against live API.
3. **S2 ORCID cross-reference**: `ORCID:` prefix lookup returns 404 for many valid ORCIDs.
   - **Fix**: Fall back to name search + h-index disambiguation when ORCID lookup fails.
4. **LinkedIn scraping**: Legal risk too high for a nonprofit. Proxycurl shut down.
   - **Fix**: Rely on ORCID researcher-urls for LinkedIn discovery; manual entry for key people.

## Lessons Learned

1. **Never depend on a single scraping library**: Google/LinkedIn will always win the arms race. Use official APIs or managed services.
2. **Test API fields against live endpoints**: Documentation can be stale. The S2 `aliases` issue wasted 15 minutes of debugging.
3. **Multi-source cascade is more resilient than single-source**: Each API has gaps; combining 3-4 sources fills nearly all fields.
4. **Cache early**: Even simple disk caching dramatically reduces API calls and enables iterative development without rate-limit anxiety.
5. **ORCID records vary wildly**: Some researchers (Shahin Mohammadi: 4 education, 4 positions) maintain rich records; others (Ananth Grama: empty) have minimal data. Never assume completeness.

## Recommendation

**Recommended**: Multi-source tiered cascade (ORCID → OpenAlex → Semantic Scholar → SerpAPI Scholar)

**Rationale**: Scores highest on combined reliability + cost + legal safety. $0/month at current scale. Each source fills different gaps. Graceful degradation if any single source is unavailable.

## Implementation Impact

| Aspect | Impact |
|--------|--------|
| New dependencies | `requests` (already present) |
| New modules | `semantic_scholar.py` (409 LOC), `serp_scholar.py` (317 LOC), `cache.py` (136 LOC) |
| Modified modules | `google_scholar.py` (4-tier fallback), `author_identity.py` (S2 + cache phases) |
| Config changes | `S2_API_KEY`, `SERPAPI_KEY` env vars (optional) |
| Cost projection | $0/month (free tiers sufficient for current volume) |

## References

- [Semantic Scholar API docs](https://api.semanticscholar.org/api-docs/)
- [SerpAPI Google Scholar](https://serpapi.com/google-scholar-api)
- [OpenAlex API docs](https://docs.openalex.org/)
- [ORCID API docs](https://info.orcid.org/documentation/api-tutorials/)
- [hiQ Labs v. LinkedIn (legal precedent)](https://en.wikipedia.org/wiki/HiQ_Labs_v._LinkedIn)
