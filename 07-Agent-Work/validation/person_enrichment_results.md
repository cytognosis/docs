# Person Enrichment Test Results

All exports saved to `data/kg/person_tests/` — 14 JSON files total.

## Combined Results (LinkedIn + Scholar + Intelligence)

| Person | ORCID | OpenAlex | Scholar ID | h | Cites | Works | Career | Highest Degree |
|--------|-------|----------|-----------|---|-------|-------|--------|----------------|
| Ananth Grama | ✅ 0000-0002-9378-9244 | A5019202832 | `bpsZlEQAAAAJ` | 54 | 21,356 | 401 | distinguished | — (ORCID empty) |
| Shahin Mohammadi | ✅ 0000-0001-8734-2326 | A5000254294 | `EgDSKaoAAAAJ` | 22 | 4,976 | 30 | distinguished | postdoc (MIT CSAIL) |
| Madhvi Menon | ✅ 0000-0003-2516-9438 | A5055671080 | — (none) | 20 | 5,495 | 32 | senior | — (ORCID empty) |
| Smita Krishnaswamy | ✅ 0000-0001-5823-1985 | A5045475274 | `l2Pr9m8AAAAJ` | 44 | 14,002 | 37 | distinguished | doctorate (U Michigan, EECS) |
| Jose Davila-Velderrain | ✅ 0000-0003-0271-6267 | A5068597405 | `8_YpcOkAAAAJ` | 33 | 11,435 | 44 | senior | — (ORCID empty) |
| Patricia Purcell | — | A5068070190 | — | 2 | 127 | 3 | early_career | — |

## Detailed Education & Position Intelligence

### Shahin Mohammadi (richest ORCID record)
```
Education:
  ★ MIT                          postdoc   ISCED=9  CSAIL
    Cold Spring Harbor Lab       course    ISCED=4
    Purdue University            doctorate ISCED=8  Computer Science
    University of Tehran         bachelor  ISCED=6  Computer Science

Positions:
  ● Founder and CEO              founder     nonprofit
    Senior Research Scientist    senior      industry (insitro)
    Research Scientist           mid_level   industry (GenBio AI)
    Collaborator                 mid_level   academic (MIT)
```

### Smita Krishnaswamy (ORCID has education)
```
Education:
  ★ University of Michigan       doctorate ISCED=8  EECS

Positions:
  ● Associate Professor          associate_professor  academic (Yale)
```

### Jose Davila-Velderrain
```
Positions:
  ● Research Associate           entry_level  industry (Human Technopole)
```

> [!NOTE]
> "Research Associate" at Human Technopole is more accurately a Group Leader position. The seniority classifier uses title patterns and doesn't account for European academic nomenclature where "Research Associate" can mean group leader. This is a known gap to address.

## Google Scholar Findings

| Person | Scholar Search | Fallback | Notes |
|--------|---------------|----------|-------|
| Ananth Grama | ❌ Not found via `scholarly` | OpenAlex ✅ | Scholar ID verified via browser: `bpsZlEQAAAAJ` |
| Shahin Mohammadi | ❌ Not found via `scholarly` | OpenAlex ✅ | Scholar ID verified: `EgDSKaoAAAAJ` |
| Madhvi Menon | ❌ No Scholar profile | OpenAlex ✅ | No public Google Scholar account exists |
| Smita Krishnaswamy | ❌ Not found via `scholarly` | OpenAlex ✅ | Scholar ID verified: `l2Pr9m8AAAAJ` |
| Jose Davila-Velderrain | ❌ Not found via `scholarly` | OpenAlex ✅ | Scholar ID verified: `8_YpcOkAAAAJ` |

> [!WARNING]
> The `scholarly` Python library is currently being blocked by Google (CAPTCHA/rate-limiting). All Scholar searches fell back to OpenAlex. The browser subagent successfully found all Scholar IDs manually. Consider integrating SerpAPI or ScraperAPI as a paid proxy for reliable Scholar access.

## Export Files for Manual Verification

| File | Size | Description |
|------|------|-------------|
| [ananth_grama_combined.json](file:///home/mohammadi/repos/cytognosis/cytos/data/kg/person_tests/ananth_grama_combined.json) | 935B | ORCID + OpenAlex + Scholar ID |
| [shahin_mohammadi_combined.json](file:///home/mohammadi/repos/cytognosis/cytos/data/kg/person_tests/shahin_mohammadi_combined.json) | 3.4KB | Full profile with education + positions |
| [madhvi_menon_combined.json](file:///home/mohammadi/repos/cytognosis/cytos/data/kg/person_tests/madhvi_menon_combined.json) | 1.6KB | ORCID + OpenAlex |
| [smita_krishnaswamy_combined.json](file:///home/mohammadi/repos/cytognosis/cytos/data/kg/person_tests/smita_krishnaswamy_combined.json) | 1.7KB | Education + Yale position |
| [jose_davila_velderrain_combined.json](file:///home/mohammadi/repos/cytognosis/cytos/data/kg/person_tests/jose_davila_velderrain_combined.json) | 1.2KB | ORCID + Scholar ID |
| [patricia_purcell_combined.json](file:///home/mohammadi/repos/cytognosis/cytos/data/kg/person_tests/patricia_purcell_combined.json) | 778B | OpenAlex only |

## Known Gaps to Address

1. **`scholarly` library blocked** — needs proxy integration (SerpAPI/ScraperAPI) or browser-based fallback
2. **Sparse ORCID records** — Ananth Grama, Madhvi Menon, Jose Davila have minimal employment/education in ORCID
3. **European title mapping** — "Research Associate" at institutions like Human Technopole is group-leader level
4. **Missing LinkedIn URLs** — only Shahin's ORCID has a LinkedIn researcher-url; others need manual entry or discovery
5. **Patricia Purcell disambiguation** — OpenAlex matched a different Patricia Purcell (A5068070190, 3 works); needs manual verification
