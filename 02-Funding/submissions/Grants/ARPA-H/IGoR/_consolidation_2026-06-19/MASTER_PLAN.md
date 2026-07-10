# IGoR Cross-Chat Consolidation — Master Plan and Tracker

**Started:** 2026-06-19. **Goal:** read all prior IGoR chats, extract facts with timestamps, consolidate into one source of truth resolving conflicts by recency (newer wins) cross-checked against content, then cascade to local files, the Solution Summary, the full proposal, and Google Docs.

## Temporal rule

Sessions are ranked by recency (rank 1 = most recent). **Newer overrides older** on conflict, unless content clearly indicates otherwise. The most authoritative layer is THIS session's output: `TEAM_AND_FOCUS_CONFIG_2026-06-19.md` plus the updated `solution_summary/IGoR_Solution_Summary.md`. Prior chats add depth (TA3 research, the TA4 instrument comparison, cost models) and are overridden where they conflict with the canonical config.

## Pipeline

1. One extraction note per chat in `notes/<id>_<topic>.md` (fresh Sonnet subagents; raw transcripts stay out of the main session).
2. Consolidate all notes into `IGoR_CONSOLIDATED_STATE.md` with a conflict-resolution log (fact, chosen value, source chat + date, overridden values).
3. Cascade to files + Solution Summary + full proposal + Google Docs.

## IGoR chats to process (recency rank = position in most-recent-first list)

| Rank | Session ID | Title | Theme | Status |
|---|---|---|---|---|
| 1 | local_abd69da7 | IGoR proposal team and outreach | team/outreach | pending |
| 2 | local_27fe559e | Element Bio Teton vs Cellanome R3200 | TA4 instrument comparison | IN PROGRESS |
| 4 | local_f3f4021c | Contractor and subawardee restrictions | team/costs/eligibility | pending |
| 5 | local_2ee7cd56 | TA2/TA3 collaboration strategy | TA2/TA3 | pending |
| 6 | local_f2e2cbd1 | ARPA-H IGoR proposal revision | proposal | pending |
| 7 | local_90daed69 | TA3 layered protocol research | TA3 best practices | IN PROGRESS |
| 8 | local_01310e86 | IGoR materials documentation | materials | pending |
| 11 | local_e0aeabb0 | IGoR project diagram and logos | figures | pending |
| 15 | local_e858c1e3 | IGoR grant proposal development | proposal | pending |
| 19 | local_55df48cd | Cellular modeling standards comparison | standards (TA1/TA3) | pending |
| 23 | local_134ffdb7 | Cellanome NDA review | TA4 partner | pending |
| 26 | local_73cac4a2 | IGoR teams data extraction | team config | pending |
| 27 | local_677ef6cd | IGoR teaming website draft | teaming | pending |
| 30 | local_f24e3fd1 | ARPA-H Proposer day attendance | program intel | pending |
| 31 | local_3a3bd901 | IGoR materials organization and summaries | materials | pending |
| 37 | local_5262a6f1 | ARPA-H IGOR team matching | team | pending |

## Secondary (verify if relevant)

local_e8ddb252 (Duane partnerships), local_37721096 (Ananth funding), local_a71a3752 (Heilmeier), local_3186aa41 (Risks), local_da09c2ce (Problem/Gap), local_337c1fd4 (science sections), local_30bb61b4 (doc consolidation status), local_1e628264 (team bios).

## Target files to update after consolidation

- `TEAM_AND_FOCUS_CONFIG_2026-06-19.md` (source of truth)
- `solution_summary/IGoR_Solution_Summary.md` (+ docx)
- `full_proposal/C1_Technical_and_Management_Proposal.md`, `C2_Task_Description_Document.md`, `C3_Price_Proposal.md`
- `full_proposal/costs/COST_MODEL_DETAILED_2026-06-16.md`
- `partnerships/partner_onepager/*`, `partnerships/TEAM_TRACKER.md`, `INDEX.md`
- Google Docs: Solution Summary + proposal
