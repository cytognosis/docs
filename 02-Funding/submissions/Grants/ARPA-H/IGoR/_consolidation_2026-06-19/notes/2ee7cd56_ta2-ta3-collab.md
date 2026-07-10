# TA2/TA3 Collaboration Strategy — Transcript Extraction Note

**Source session:** local_2ee7cd56-ab0d-4550-9266-f53e5ad9bcfc ("TA2/TA3 collaboration strategy")
**Session recency rank:** 5
**No explicit date in session content** (no timestamp visible in transcript); recency rank 5 places this between the TA3-protocols session (rank 7, 2026-06-16) and the most recent sessions.
**Extracted:** 2026-06-19
**Extraction method:** mcp__session_info__read_transcript (format: full, limit: 400) + corroborating file reads.

---

## Summary

The session is a single-exchange: the user uploaded a PDF of the full email thread with Dan Bryce (SIFT) and asked for a strategic rewrite of a draft follow-up email. The transcript shows the assistant read the PDF, performed a strategy synthesis, and produced a revised send-ready email. The primary deliverable from this session is the email-strategy revision and the codified TA2/TA3 interface model it documents. No separate consolidation doc was written to disk during the session; the revised email was presented via `mcp__cowork__present_files`. Cross-referencing with corroborating IGoR files (SIFT_capabilities_analysis.md, TEAM_AND_FOCUS_CONFIG_2026-06-19.md, C1_Technical_and_Management_Proposal.md) confirms the decisions documented here are canonical.

**Single most important finding:** The session established the canonical TA2 ownership split: **Cytognosis and IPAI anchor the mechanistic core of TA2 (disease-model-grounded engine); SIFT owns a defined TA2 planning-and-scheduling layer** (Bayesian VOI experiment ranking, plan-and-schedule, compile-to-protocol). "Co-lead TA2" framing was explicitly rejected as blurring ownership; the revised email reframes SIFT's TA2 role as a scoped contribution under Cytognosis lead.

---

## Key Facts (with dates)

All facts below carry "no explicit date; recency rank 5" unless otherwise noted.

### TA2 Ownership and Architecture

- **Cytognosis (Shahin Mohammadi) is TA2 lead.** Cytognosis and IPAI anchor the mechanistic core. (Confirmed also in TEAM_AND_FOCUS_CONFIG_2026-06-19.md and C1_Technical_and_Management_Proposal.md.)
- **SIFT's TA2 role:** a **scoped Bayesian value-of-information (VOI) planning-and-scheduling layer** that (a) ranks experiment candidates by VOI against the TA1 mechanistic model, (b) turns the model's chosen experiment into a scheduled, resource-allocated, executable plan, and (c) hands it off to LabOP in TA3. This is explicitly NOT "co-lead TA2."
- **The "mechanistic-RAG" framing:** the core TA2 engine is described as a "mechanistic-RAG that uses the full representation of the disease model as the context for the AI agent." This is the Cytognosis/IPAI contribution; SIFT handles the downstream TA2-to-TA3 handoff.
- **TA2 architecture (from C1_Technical_and_Management_Proposal.md, confirmed consistent):** three components: (1) tournament of competing causal-link hypotheses with adversarial critics; (2) mechanistic-model-grounded retrieval-augmented planning (TA1 structured output as retrieval corpus, not literature alone); (3) test-time validation via lightweight simulations.
- **Hypothesis/experiment-intent generation split:** Shahin leads mechanism-grounded hypothesis generation and experiment-intent; SIFT contributes the planning/scheduling layer that operationalizes those intents into executable plans.
- **Consequential actions require human authorization** (explicit in C1).

### SIFT Role and Scope (Dan Bryce, Robert Goldman)

- **Dan Bryce** (dbryce@sift.net): TA3 lead; scoped TA2 planning/scheduling contributor. Role confirmed.
- **Robert Goldman** (rpgoldman@sift.net): TA3 advisory role. Confirmed.
- **SIFT FTE estimate for TA3:** "2-3 FTEs" (Dan Bryce's own estimate, cited verbatim in the email thread and corroborated in SIFT_capabilities_analysis.md and C1_Technical_and_Management_Proposal.md). Dan had a June 25 deadline to finalize.
- **SIFT FTE for TA2:** 1 FTE (implied by the "3 + 1" baseline in the revised email). Soft-confirmed pending scope finalization.
- **Proposed seniority mix for SIFT team (Shahin's suggestion, deferred to Dan):** 1 staff/principal-level lead to own architecture; ~2 senior engineers/architects for core build; 1 mid-level engineer for testing and experimentation.
- **SIFT TA3 lead credentials:** SIFT co-authored LabOP (Laboratory Open Protocol language) under DARPA SD2 (2016-2022). This is the reason SIFT is the natural TA3 lead, not just a technology match.
- **SIFT TA2 credentials:** Published Bayesian model for experiment choice (Goldman, Trivedi, Bryce; AAAI Fall Symp); hierarchical experiment planning (Kuter, Goldman, Bryce, Beal; XP; 2018); VOI-based ranking and LLM-augmented planning/scheduling. All published in SynBio domain; generalization to mammalian iPSC workflows identified as an open technical question.
- **June 25 deadline** (from corroborating files): Dan needs to send (a) cost figures and (b) a one-to-two-page TA3/LabOP science write-up for integration into the proposal. Draft-by-Monday (June 22) plan, review/feedback by Wednesday (June 24), finalize June 25.

### Cross-Cutting Semantic Foundation (Shahin + Dan)

- **Shahin Mohammadi and Dan Bryce jointly own the cross-cutting semantic foundation** (schemas, ontologies, interfaces spanning all TAs). (Confirmed in TEAM_AND_FOCUS_CONFIG_2026-06-19.md.)
- The goal is one semantic identity for every entity (gene, variant, cell model, perturbation, protocol object) across TA1, TA2, TA3, and TA4 -- no translation at seams.
- **LinkML + Biolink Model** is the chosen stack (LinkML as schema language; Biolink as upper ontology; RDF as serialization). (From TA3-protocols session, rank 7; consistent with all subsequent docs.)

### ExperimentIntent and LabCapabilityProfile Interfaces

- **ExperimentIntent:** structured object passed from TA2 to TA3. Fields: URI-bound scientific question, quality requirements, value-of-information score, human authorization flag. TA3 returns a LabOP protocol within one business day.
- **LabCapabilityProfile:** object declaring what a given laboratory supports (cell models, perturbations, readouts). TA3 matches ExperimentIntent requirements against LabCapabilityProfiles to route experiments to labs. SiLA Feature discovery auto-populates profiles.
- Both interfaces are **concrete deliverables and open standards**; schemas ratified at Month 3 DDD workshop (Phase I milestone per C1).
- (Sources: C1_Technical_and_Management_Proposal.md line 130; 90daed69_ta3-protocols.md; TEAM_AND_FOCUS_CONFIG_2026-06-19.md.)

### Phylo / Biomni (Kexin Huang) — Optional TA2 Role

- **Kexin Huang** (creator of Biomni) is listed as **optional TA2 collaborator** in TEAM_AND_FOCUS_CONFIG_2026-06-19.md (row: "Autonomous experiment-design engine"; Ananth Grama lead; "Phylo/Biomni, Kexin Huang (optional)").
- In C1 biosketch list: "Kexin Huang (TA2, optional; agentic biomedical AI, Biomni)."
- No FTE or cost commitment for Phylo/Biomni is documented. Named only where it strengthens the case; do not gate on it.
- Biomni is characterized in C1 as an "agentic-science system" that "proposes experiments without interrogating a mechanistic disease model" -- used as a contrast in the superiority argument, not a dependency.

### TA2-to-TA3 Interface (from session email and corroborating files)

- The strategic framing is: Cytognosis/IPAI own TA2 core (disease model query + experiment-intent generation); SIFT owns the TA2-to-TA3 seam (planning/scheduling layer + protocol handoff). The two are designed as joint architecture from day one, NOT independent efforts aligned post-hoc.
- **"Joint design from day one"** is stated explicitly in the email and the strategy (verbatim: "I don't want two efforts that are meant to align later (which never works), but one joint design from day one, with the architecture and interfaces defined up front.")
- **User interface:** not explicitly addressed in this session. The TA2 engine "explains its reasoning through narratives and visualizations so the researcher directs the work" and "consequential actions require human authorization" (from C1). No specific UI spec in this transcript.

---

## Decisions

1. **DECIDED: "Co-lead TA2" framing rejected.** SIFT does NOT co-lead TA2. Cytognosis and IPAI are TA2 leads. SIFT contributes a scoped planning/scheduling layer. (Session; also reflected in TEAM_AND_FOCUS_CONFIG_2026-06-19.md.)
2. **DECIDED: SIFT leads TA3.** LabOP is the TA3 backbone. (Consistent across all IGoR docs from rank 7 onward.)
3. **DECIDED: SIFT's TA2 role is the VOI ranker and plan-to-protocol layer** (not the mechanistic engine). Cytognosis owns the mechanistic engine; SIFT owns the downstream planning/scheduling operationalization.
4. **DECIDED: FTE baseline = 3 (TA3) + 1 (TA2) for SIFT**, give-or-take 1 FTE as scope firms up. Soft-confirmed pending Ananth sign-off on budget.
5. **DECIDED: Seniority mix recommendation** (from Shahin to Dan): 1 staff/principal lead, ~2 senior engineers, 1 mid-level engineer. Deferred to Dan for final composition.
6. **DECIDED: June 25 deadline** for Dan to deliver cost figures and TA3 science write-up; June 22 for first proposal draft incorporating SIFT inputs.
7. **DECIDED: Joint architecture design from day one**, not independent workstreams to be aligned. Second call between Shahin and Dan to lock TA2 scope and interfaces before June 25 Solution Summary.

---

## Conflicts to Flag

1. **"Co-lead TA2" terminology:** Shahin's original email draft used "co-leading TA2." This was reframed in the revised email (this session) to SIFT owning a "defined planning and scheduling layer" under Cytognosis lead. Any IGoR document (Solution Summary, full proposal, team one-pagers) that still says SIFT "co-leads TA2" must be corrected.
2. **SIFT FTE numbers:** The transcript confirms "3 + 1 FTEs" as a baseline with wiggle room, but Dan had not yet sent formal cost figures as of this session. The June 18 follow-up (SIFT_Dan_followup_2026-06-18.md) shows these were still pending. The cost model must be updated once Dan delivers. Do not treat any prior FTE number as final.
3. **Phylo/Biomni cost:** No FTE or dollar amount for Phylo/Biomni exists anywhere. If Kexin Huang is included in the proposal, a line item needs to be derived. The proposal currently marks this as optional/TBD; no conflict, but flag as a gap if the optional becomes required.
4. **TA2 scope vs. TA3 scope seam:** The TA2-to-TA3 boundary is still being designed. Specifically, whether the VOI ranker and XP planner sit fully in TA2 (SIFT contribution to TA2) or at the TA2-TA3 seam affects SIFT's TA2 FTE. The 90daed69_ta3-protocols.md note (rank 7) flags this as an open item; this session does not resolve it definitively. Until the architecture call (the "second call" this email proposed) happens, treat the TA2-TA3 seam assignment as pending.
5. **User interface spec:** Not addressed in this session. The C1 proposal describes the researcher as directing work via "narratives and visualizations" with human authorization gates, but there is no detailed UI spec. If ARPA-H reviewers ask about user experience, this needs to be developed.
