# IGoR Master Revision Plan — local full-revision + Google sync (2026-06-21)

**Purpose:** the single execution plan to (A) fully revise all LOCAL IGoR deliverables to the finalized state, and (B) revise the Google Docs (still pending). Inputs are all settled and captured: `BUDGET_FRAMEWORK_v2_2026-06-21.md` (restructured budget + roles + resource-sharing + salary-cap), `INTEGRATION_SPEC_2026-06-21.md` (Dan's TA2/TA3, 5 innovations, 3 stages, best-team messaging, comment map), `IGoR_CONSOLIDATED_STATE.md` (canonical facts + Google URLs §7), and `CEO_Compensation_DETERMINATION_2026-06-21.md` (comp ladder, Rung 1 = $228K).

**BLUF:** comp ($228K Rung 1) is being propagated now; the remaining work is a large, numerically-interdependent rebuild of the deliverables (SS, C1/C2/C3, cost model, C4 workbook) to the restructured ~$43M budget and the corrected roles, then a Google master sync with per-person inline comments. This deserves a fresh, focused session for accuracy; this plan sequences it so nothing is lost.

---

## A. Local full-revision sequence (execute in a fresh session, ideally via Sonnet subagents with these specs)

1. **Cost model + C3 + C4 workbook — restructure to the v2.2 framework.** Per-performer: Purdue computational (TA1+TA2) ~$6.5M, Purdue TA4-academic (Tegtmeyer, non-IPAI dept) ~$6.0M, Cytognosis ~$9.5M, SIFT $7.0M (Dan's real breakdown: DL $4.09M / indirect $2.20M / travel $69.7K / fee $0.64M / 24,204 hrs), Cellanome ~$6.0M (RENT base), shared program compute ~$2.5M, TA4 sequencing CRO ~$2.0M, McLean $0.7M, Duane ~$0.2M ($750/hr hourly consultant), cross-team/reserve ~$2.5M. **Total ~$43M (NOT $50M).** Drop Phylo and Illumina-as-partner (Illumina optional in-kind only). Add the resource-sharing package (IPAI HPC ~$1.5-2M, Purdue lab ~$150K, Cellanome credits ~$160K) as the in-kind line; net the shared-compute line against IPAI HPC in-kind. Re-derive F&A (Purdue ~57%, Cytognosis 15% de minimis) and keep all three views (per-performer, category BOE, phase) internally consistent. Comp: Shahin $228K Rung-1 base × effort (already propagated). Salary cap: Grama/Carpenter/Ruzicka at cap; Shahin at cap; verify Cytognosis hire BASES < $228K; commercial-sub cap treatment flagged for Duane + Purdue SPS.
2. **SS (submission md) — BOE + team + roles.** Update the BOE per-performer + category tables to the restructured numbers; update Section 4 team to the canonical role map (TA1 + TA2 both co-led Purdue+Cytognosis; Matt = TA4-academic lead + TA1 contributor, non-IPAI dept; Anne TA1 co-lead; SIFT TA2-TA3+TA3+TA3-TA4; Cellanome TA4-industry; Illumina optional). Keep Sections 1-4 <= 5 pages at Inter 11pt; the BOE/refs are excluded. Add the resource-sharing line. Weave the best-team messaging (clinical: Shahin+Brad; cellular: Matt+Anne, already published NeuroPainting together) and the 5 innovations (residual-space OT/MMD alignment; treatment+disease SCM; TransBox ontologies; genomic-FM factorization; graph-wavelet GNNs) into Sections 1-3. Acknowledge the Broad/Cell Painting collaboration (no subaward).
3. **C1 / C2 — roles + science.** Apply the canonical role map; integrate Dan's TA2/TA3 text (mark SIFT-authored DRAFT); add the 3 experimental stages (prioritize disease models -> unbiased Perturb-seq -> targeted combinatorial perturbation) mapped to the 3 phases + milestones; fold in the innovations.
4. **Regenerate .docx (+ SS .pdf)** for every edited file (pandoc; SS via the Inter 11pt brand build; verify SS Sections 1-4 still <= 5 pages).
5. **Read prior grants** (Google Impact, Astera, AWS Imagine, Coefficient) to harvest any additional innovations/context for the full proposal (per the integration spec TODO).
6. **Verify:** total ~$43M reconciles across the three budget views; salary cap respected; zero stale terms ($165K, $50M-forced, Element-as-partner, Vodovotz, Anna, Phylo/Illumina-as-budgeted); citations resolve.

## B. Google master revision (PLAN — still pending; needs a pathway decision)

**Pathway:** no native Google Docs edit/comment connector is available; use **Claude in Chrome** (you confirmed you've had me edit these before) OR stand up a Google Workspace MCP. Recommend Chrome for now.

**Targets (URLs in `IGoR_CONSOLIDATED_STATE.md` §7):** SS (`12JTwOcl...`), C1 (`1ertYHzLI...`), C2 (`1FNzUAE5...`), C3 (`1GDd3r0B...`), C4 sheet (`1XseQOlC...`), Drive folder `1Tnenqw...`. Note these are the 2026-06-16 versions; after the local rebuild, push the revised content (replace stale figures/roles) into each.

**Per-person inline comments to place (from the integration spec map):**
- TA2/TA3 sections -> **Dan** (mark as sketches/drafts to revise).
- TA1 sections -> **Ananth**.
- Experimental procedures, costs, Purdue equipment/feasibility, what's buyable vs not -> **Matt** (optionally Anne).
- Computational morphology / Cell Painting -> **Anne**.
- Legal / IP / financial flows -> **Duane**.
- Any financial figure -> **Ananth** (verify).
- TA4 R3200 + TA3-TA4 and TA4-TA1 interfaces -> **Cellanome**.
- Concept Summary + crisp no-jargon messaging -> **Patty + Ananth**.

**Sequence:** (1) finish the local rebuild (A); (2) regenerate the branded SS docx; (3) in Chrome, update each Google Doc/Sheet to match the local source of truth; (4) add the per-person comments; (5) confirm the folder is internally consistent. From now on, every IGoR update reflects in Google as the source of truth (standing rule).

## C. Decisions still open for Shahin + Ananth (carry into the build)

1. Confirm the IGoR per-award **ceiling** (so ~$43M headroom is right).
2. **Resource-sharing target %** (recommend 5-10%); a Purdue HPC match letter unlocks ~10%.
3. **Cellanome model** (RENT-and-we-run base ~$5-6M); get Cellanome BD + Psomagen quotes; name the Cellanome TA4-industry lead.
4. **Matt's exact Purdue department** (for the TA4-academic attribution, non-IPAI).
5. Commercial-sub **salary-cap treatment** (Duane + Purdue SPS).
6. Whether to add **Phylo on TA2** before final (optional).

*Comp note: Shahin Rung 1 = $228K (HHS cap), federal charge $228K × effort; Rungs 2/3 above-cap from unrestricted funds. $165K retired.*
