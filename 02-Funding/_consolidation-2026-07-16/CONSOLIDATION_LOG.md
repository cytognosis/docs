# Grants & Applications Consolidation, Living Log (2026-07-16)

> **Status:** Complete for this session (follow-ups listed) · **Owner:** Shahin Mohammadi (with Claude) · **Backup tags:** `pre-grants-consolidation-2026-07-16` (docs @ dc3dfd9); `pre-slotlib-codetasks-2026-07-16` (docs + cytos, before engine code tasks).
> Companion docs: `MASTER_CONSOLIDATION_PLAN_2026-07-16.md`, `01_ASSET_INVENTORY.md`, `00_PRIOR_WORK_SYNTHESIS.md`, `submission-registry.REBUILT.md`.

**If you only read one thing:** the commit ledger and the follow-ups. Docs work is in `~/repos/cytognosis/docs`; engine/code changes ran as an independent worker on docs + `cytos`, both tagged. All commits authored Shahin Mohammadi.

## What was consolidated

- Standardization verified and finished: canonical-source/sync doc, section-size budgets (ISO SS = 6 pages official), per-funder values view, funder-count fixes, and a CODE_TASKS spec.
- Submission registry rebuilt to verified truth; statuses corrected (Coefficient Capacity, ElevenLabs, Anthropic AI-for-Science = not yet applied).
- 3 orphan duplicates folded (archived, pointers, no deletions).
- Per-application INDEX records across all submissions + stubs.
- Funding opportunities: eligibility axes, EU/UK rows, entity memo, comprehensive US+UK/EU landscape, and NIH/NSF additions (NSF SCH 25-542, Bridge2AI, PRIMED-AI D2M-AIP), plus a best-fit shortlist and near-term watchlist.
- One-pagers located (Smoller, Coppersmith/PHO-PD, Convergent, send-ready) + asset locator.
- Precision psychiatry: 1-pager, 6-page ISO Solution Summary draft, and a FULL unabridged proposal draft (biotypes, gaps, personalized + rapid-acting treatment, EVIDENT, verified references).
- Biotyping dossier: index, two variants (ND-friendly + grant/review), dimensional-map figure v1.
- Engine code tasks (independent worker): 4 new funder configs (arpah_program_iso, nsf_xlabs, primed_ai, nsf_sch), 6 registry entries reconciled, `yc_nonprofit` renamed to `yc_s26_pbc` atomically, docs synced to cytos; validated via `cytos funding registry list` (all 18 funders resolve).

## Commit ledger (all authored Shahin Mohammadi)

| # | Subject | Hash |
|---|---|---|
| tag | safety tag (docs) | dc3dfd9 |
| 1-11 | kickoff, registry, orphans, counts, canonical/sync, sizes+values, dossier index, eligibility+EU/UK+entity, per-app records, precision-psych 1-pager, log+README | 9d942f1 … 07aae78 |
| 12 | correct not-yet-applied statuses | 68c195f |
| 13 | US+UK/EU opportunity landscape | 97830fa |
| 14 | outreach one-pager asset locator | 5147138 |
| 15 | wire SN-26-156 + shortlist + Ali route | c11876c |
| 16 | 6-page ISO Solution Summary draft | cf02afc |
| 17 | biotyping dossier 2 variants + figure v1 | 3b3071a |
| 18 | finalize log (session 2) | 63e0590 |
| 19 | full unabridged precision-psych proposal | 7823d0c |
| 20 | NSF SCH + Bridge2AI + PRIMED-AI + NIH; Ali PhD routes | c942081 |
| 21 | registry Ali PhD + PRIMED-AI shortlist | cd153c4 |
| 22 | CODE_TASKS spec | f38dc86 |
| 23 | finalize log (session 3, this) | (this) |

**Independent engine worker (docs):** dbdaa3c (registry entries), c624494 (arpah_program_iso + nsf_xlabs), af863a0 (primed_ai + nsf_sch), a155ba0 + 60ecb51 (yc_s26_pbc rename), 7b18117 (rename cleanup).
**Independent engine worker (cytos):** cfabee2 (schema sync).

## Follow-ups (tracked)

1. **Monday board sync** once the connector is re-authorized. Shahin.
2. **cytos noxfile bug (pre-existing):** `nox -s parse_grants` calls the old `cytos grants` CLI; rename to `cytos funding` (own fix ticket).
3. **Build remaining configs** when needed: nih_r21, nsf_sbir_phase1/2/2b (currently `planned: true`); convert their cytos legacy stubs to canonical format; remove orphan `arpah_solution_summary.yaml`.
4. **Push to Google Docs** the outreach one-pagers, ISO SS, and full proposal for sharing/comments (IGoR docs stay hand-edited by Shahin).
5. **Finalize the ISO SS/full proposal:** convert the dimensional-map figure to a publication SVG; budget with Purdue SPS; then send the Smoller lead-ask and Coppersmith note.
6. **Biotyping ingest:** NbN into `datasets/treatments/nbn/`; recent ADHD/depression papers, Stanford biotypes, ADHD DSM blog.
7. **Entity:** decide UK/EU vehicle with Duane Valz + CPA (recommendation: no entity; route via Madhvi/Manchester).
8. **Ali (PhD student):** confirm citizenship to unlock GRFP/F31; default to a grant-funded GRA slot or a direct industry-sponsored/co-supervised PhD (both citizenship-agnostic).
9. **Gmail check:** Smoller/Coppersmith/Convergent threads, sent vs file versions.

## Near-term deadlines to act on

Jul 31 ARIA Neural Interfaces; Sep 9 MSCA Postdoctoral; Oct 6 NIH RFA-DA-27-004 (TMM R01, via Purdue/Grama); Oct 19 PRIMED-AI D2M-AIP (Cytognosis can be PI); ARPA-H PHO ISO SN-26-156 rolling (send one-pagers now).
