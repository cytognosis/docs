# ADR-001: Multi-Source Author Identity Pipeline with Tiered API Strategy

> **Status**: Accepted
> **Date**: 2026-05-14
> **Author**: @shmohammadi
> **Tags**: `data-source`, `api`, `schema`, `scholarly`
> **Variants**: Technical (this doc) - Readable (ADR-001-tiered-author-identity-api-strategy.md in Obsidian vault: 04-Engineering/cytos/adrs/) - Agent (n/a)

## Context

The Cytos scholarly module needs to resolve author identities across multiple data sources (ORCID, OpenAlex, Google Scholar, Semantic Scholar, LinkedIn) and merge them into a unified `AuthorIdentity` record. The initial implementation used the `scholarly` Python library for Google Scholar access, which was immediately blocked by Google's CAPTCHA/rate-limiting infrastructure. LinkedIn public profile scraping also proved legally risky and technically fragile.

We evaluated six data access strategies and needed to select a durable, cost-effective architecture that works reliably for a nonprofit with limited budget.

### Forces at play
- Google Scholar has no official API and aggressively blocks scrapers
- LinkedIn has zero-tolerance for automated access (Proxycurl shut down 2025)
- Free official APIs (OpenAlex, Semantic Scholar, ORCID) exist but have different coverage
- Our volume is low (tens of researchers/month) but reliability must be high
- As a 501(c)(3), legal risk tolerance is near-zero

## Decision

**We will use a 4-tier multi-source enrichment cascade with disk caching.**

1. **Tier 1 (Free, Official)**: ORCID → OpenAlex → Semantic Scholar
2. **Tier 2 (Paid, Managed)**: SerpAPI for Google Scholar (250 free/month)
3. **Tier 3 (Deprecated)**: `scholarly` library as last resort
4. **Cache**: Disk-backed JSON cache with 30-day TTL

LinkedIn data is obtained only from ORCID researcher-urls or manual entry. No login-based scraping.

## Alternatives Considered

### Option A: Residential proxy + scholarly library
- **Pros**: Free, uses existing code
- **Cons**: High maintenance, legally gray, breaks frequently, Google actively detects
- **Why rejected**: Unreliable for production use; ToS violation risk for a nonprofit

### Option B: SerpAPI-only (replace all sources)
- **Pros**: Single integration point, reliable
- **Cons**: $25-75/month, no ORCID/education data, limited to Scholar's coverage
- **Why rejected**: Over-reliance on single paid service; misses ORCID and S2 capabilities

### Option C: Semantic Scholar as sole replacement
- **Pros**: Free, official, excellent STEM coverage
- **Cons**: Weaker on non-STEM fields, no Google Scholar IDs, limited author disambiguation for common names
- **Why rejected**: Incomplete as sole source; best used as part of multi-source cascade

## Consequences

### Positive
- $0/month cost at current scale (all free tiers)
- No legal risk (all official APIs or managed services)
- Cached results enable offline operation and instant re-lookups
- Each source fills different gaps (ORCID: education, OpenAlex: h-index, S2: TLDRs, Scholar: co-authors)
- Graceful degradation: if one source is down, others still work

### Negative
- More code to maintain (4 clients vs. 1)
- S2 API has author disambiguation challenges for common names
- SerpAPI free tier (250/month) requires monitoring

### Neutral
- `scholarly` library remains in code as fallback but is effectively deprecated

## Implementation Notes

- `semantic_scholar.py`: 409 lines, 8 public functions
- `serp_scholar.py`: 317 lines, 5 public functions
- `cache.py`: 136 lines, 6 public functions
- `author_identity.py`: Updated `enrich_author()` cascade (9 phases)
- `google_scholar.py`: Updated `get_scholar_profile()` with 4-tier fallback

## References

- [Scholarly Access Strategy](../../../.gemini/antigravity/brain/cd6537fc-9f66-43c5-80fd-f9d2c8fe6893/artifacts/scholarly_access_strategy.md)
- [Semantic Scholar API docs](https://api.semanticscholar.org/api-docs/)
- [SerpAPI Scholar docs](https://serpapi.com/google-scholar-api)
- [OpenAlex API docs](https://docs.openalex.org/)
