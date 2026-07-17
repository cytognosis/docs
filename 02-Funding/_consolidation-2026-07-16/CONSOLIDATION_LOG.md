# Grants & Applications Consolidation, Living Log (2026-07-16)

> **Status:** Complete for this session (follow-ups listed) · **Owner:** Shahin Mohammadi (with Claude) · **Backup tag:** `pre-grants-consolidation-2026-07-16` @ `dc3dfd9`
> Companion docs: `MASTER_CONSOLIDATION_PLAN_2026-07-16.md`, `01_ASSET_INVENTORY.md`, `00_PRIOR_WORK_SYNTHESIS.md`, `submission-registry.REBUILT.md`.

**If you only read one thing:** the commit ledger and the follow-ups. Everything is in `~/repos/cytognosis/docs` (branch `main`), committed as Shahin Mohammadi.

## What was consolidated (all 9 phases + expansions)

- Standardization verified and finished: canonical-source/sync doc, section-size budgets (ISO SS = 6 pages official), consolidated per-funder values view, funder-count fixes.
- Submission registry rebuilt to verified 2026-07-16 truth; 3 statuses corrected to "not applied" (Coefficient Capacity, ElevenLabs, Anthropic AI-for-Science).
- 3 orphan duplicates folded (archived, pointers, no deletions).
- Per-application INDEX records across all submissions + 2 stubs.
- Funding opportunities expanded: eligibility axes, EU/UK rows, entity memo, and a comprehensive US+UK/EU landscape with best-fit shortlist, Ali-fundable schemes, and a near-term deadline watchlist.
- One-pager assets located and mapped (Smoller, Coppersmith/PHO-PD, Convergent all exist and are send-ready).
- Precision-psychiatry: 1-pager + 6-page ISO Solution Summary draft v1 (target SN-26-156), plus ISO/Convergent homes.
- Biotyping dossier: index, two variants (ND-friendly + grant/review), and dimensional-map figure v1 (mermaid + render spec).

## Commit ledger (docs repo, all authored Shahin Mohammadi)

| # | Subject | Hash |
|---|---|---|
| tag | safety tag `pre-grants-consolidation-2026-07-16` | dc3dfd9 |
| 1 | kickoff (plan, inventory, synthesis, log) | 9d942f1 |
| 2 | rebuild submission registry | 7ffd062 |
| 3 | fold 3 orphan duplicates | cf5081b |
| 4 | correct funder-config count to 10 | a47460b |
| 5 | slot-library canonical-source + sync doc | e3d5c66 |
| 6 | section-size budgets + values view | 76c9f6f |
| 7 | biotyping dossier index + figure spec | 16f1040 |
| 8 | eligibility axes + EU/UK + entity memo | a8d4fcd |
| 9 | per-application INDEX records | 8df7f7f |
| 10 | precision-psych 1-pager + ISO/Convergent homes | d9bb93b |
| 11 | finalize log + README pointer | 07aae78 |
| 12 | correct not-yet-applied statuses | 68c195f |
| 13 | US+UK/EU opportunity landscape + shortlist | 97830fa |
| 14 | outreach one-pager asset locator | 5147138 |
| 15 | wire SN-26-156 + shortlist + Ali route into registry | c11876c |
| 16 | 6-page ARPA-H PHO ISO Solution Summary draft v1 | cf02afc |
| 17 | biotyping dossier 2 variants + dimensional-map figure v1 | 3b3071a |
| 18 | finalize log (this commit) | (this) |

## Follow-ups (tracked; several need Shahin or a fresh session)

1. **Monday board sync** once the connector is re-authorized (rows are Monday-ready). Shahin.
2. **Standardization:** adopt the 6 extra funder registry entries into the docs manifest; build `arpah_program_iso` and `nsf_xlabs` configs; sync docs to cytos; run `nox -s parse_grants`. Relabel `yc_nonprofit` (for-profit PBC) atomically.
3. **Push to Google Docs** the outreach one-pagers and the ISO Solution Summary for sharing and comments (they are markdown-only today; IGoR docs stay hand-edited by Shahin).
4. **Finalize the ISO SS:** references, convert the dimensional-map figure to a publication SVG, quantitative budget with Purdue SPS; then send the Smoller lead-ask and Coppersmith note (both drafted in `outreach-onepagers/`).
5. **Biotyping ingest:** NbN tables into `datasets/treatments/nbn/`; recent ADHD/depression papers (~Jul 11), Stanford biotypes page, ADHD DSM blog.
6. **Entity:** decide UK/EU vehicle with Duane Valz + CPA (recommendation on file: no entity; route via Madhvi/Manchester).
7. **Gmail check:** 8 threads matching Smoller/Coppersmith/Convergent, confirm sent text vs file versions.

## Near-term deadlines to act on

Jul 31 ARIA Neural Interfaces seed; Sep 9 MSCA Postdoctoral (can fund Ali); Oct 6 NIH RFA-DA-27-004 (TMM R01, via Purdue/Grama); ARPA-H PHO ISO SN-26-156 rolling (send one-pagers now).
