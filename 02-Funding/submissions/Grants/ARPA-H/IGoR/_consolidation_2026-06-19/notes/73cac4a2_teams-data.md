# IGoR Teams Data Extraction — Consolidation Note

**Source session:** `local_73cac4a2-de18-4954-8626-7718644884ec`
**Session title:** IGoR teams data extraction
**Extracted:** 2026-06-19
**Session status at read:** idle (completed)

---

## Summary

This session scraped the full ARPA-H IGoR teaming page (https://arpa-h.gov/explore-funding/programs/igor/teaming) and produced two output files: a raw roster TSV (149 teams) and an enriched TSV with org-intelligence fields (entity type, funding, stage, products, job listings). The official page truncates at 123 rows when fetched programmatically (byte limit cuts off after "Uncharted Software"); the missing 26 rows were recovered from the live DOM via browser automation. No Cytognosis/PsychIGoR-specific teaming decisions were made in this session — it was a data-collection run.

---

## Team/candidate data (with dates)

**Date of page scrape:** session was executed before 2026-06-19 (no explicit date in transcript; recency rank 26).

### Full roster stats (149 teams on ARPA-H page)

| Entity type | Count |
|---|---|
| Startup | 48 |
| Academic/University | 47 |
| SME/Private company | 16 |
| Nonprofit | 9 |
| Biotech | 5 |
| Large/Public company | 8 (Databricks, J&J, ICF, Verily, others) |
| FFRDC/Research Institute | 4 |
| Consulting | 3 |
| Individual/Independent | 2 |
| Could not identify | ~9 |

### Orgs with no findable web presence (9 flagged "Not found")

These were in the roster but could not be verified — likely individuals or very early-stage:
- Akraia
- Chimera Research
- CYBERINQ
- ggomics
- Hetzerk
- NebulAi
- SciKnowIO Consulting
- Talzera
- Open Enzyme

### Notable orgs with funding/valuation data (spot-checked)

| Org | Stage/Funding | Notes |
|---|---|---|
| Databricks | $134B valuation (Series L) | Large compute/AI platform |
| Asimov | ~$209M raised | Synthetic biology |
| Tahoe Therapeutics | ~$42M raised / $120M valuation | Appears twice in source list (rows 109 and 124 — duplicate in ARPA-H page itself) |

### Duplicates in source data

- **Tahoe Therapeutics** — rows 109 and 124 (same org, two entries on the official ARPA-H page)
- **University of Pittsburgh** — rows 136 and 137 (two different contacts)
- Several other universities listed twice with different contacts

### TA distribution note

A large share of for-profit teams skew **TA2 (New Science Engine)** — AI/compute players. Fewer are TA1 (Comprehensive Disease Models) biology-focused. This is relevant for PsychIGoR if scanning for complementary TA1 partners.

---

## Costs/effort

No cost or FTE figures were captured in this session. The session was limited to public teaming-page data and org intelligence (funding rounds, employee counts, products). No budget or effort-allocation data was discussed.

---

## Decisions

- The session was purely a data-collection task; no PsychIGoR teaming decisions were made.
- The assistant flagged a potential follow-on: adding a column to flag strong TA1 (Comprehensive Disease Models) fits or filtering to the biotech/disease-modeling subset. This was offered as a next step, not executed.
- Data kept as-is to match the official ARPA-H page, including duplicates.

---

## Conflicts to flag

1. **File locations may be stale.** The session produced `IGoR_teaming_roster.tsv` and `IGoR_teams_enriched.tsv` and presented them via `mcp__cowork__present_files`. These files were delivered to the session's output folder. Per the git status at the start of this consolidation conversation, both files (`IGoR_teaming_roster.tsv` and `IGoR_teams_enriched.tsv`) show as **deleted** (`D`) from the repo index in `02-submissions/Grants/ARPA-H/IGoR/`. The enriched data may need to be re-staged or recovered from the Cowork outputs folder.
2. **149 vs. 123 row discrepancy.** Any prior analyses done against the truncated 123-row file are incomplete. The full dataset is 149 teams. Downstream work (e.g., filtering for PsychIGoR teaming candidates) should use the 149-row enriched file.
3. **Tahoe Therapeutics duplicate.** The ARPA-H page itself has Tahoe listed twice. If building a de-duplicated contact list, flag this before outreach.
4. **9 unverifiable orgs.** These are marked "Not found" in the enriched file. Do not use them for outreach without additional vetting.
5. **Funding data currency.** Figures reflect June 2026 data as found by subagent web research. Valuation figures (especially Databricks $134B) are from the session date and may shift.
