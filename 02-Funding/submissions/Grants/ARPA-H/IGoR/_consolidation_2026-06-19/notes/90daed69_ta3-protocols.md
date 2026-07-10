# TA3 Layered Protocol Research — Transcript Extraction Note
**Source session:** local_90daed69-3fe6-4035-bd34-ef9ab48b035b ("TA3 layered protocol research")
**Date of session activity:** 2026-06-16 (meeting notes timestamp; session recency rank 7)
**Extracted:** 2026-06-19
**Extraction method:** Full transcript read via mcp__session_info__read_transcript (limit 400)

---

## Summary

This session consolidated two parallel research streams (LabOP/protocol-standards landscape; ARPA-H IGoR TA3 slide parse) with a meeting between Shahin Mohammadi, Daniel Bryce (SIFT), and Matthew Tegtmeyer (Purdue/mttegtme@purdue.edu) held 2026-06-16. The core finding is that the IGoR TA3 "layered protocol stack" shown on the proposer-day slide is **not a new invention**. It is the OSI/Internet-stack concept applied to wet labs, already realized as **LabOP** (co-authored by SIFT during DARPA SD2, 2016-2022, with follow-on funding from Schmidt Futures). The session produced two deliverables: a 14-section full integrated design doc and an ADHD-friendly companion brief, both saved to the IGoR research folder.

**Single most important finding:** The LabOP backbone (LabOP/PAML, Bartley et al. *ACM JETC* 2023) is the correct intent+process layer; SIFT (Dan Bryce) built it under DARPA SD2 and is willing to lead TA3. The SiLA 2 correct citation is **Juchli 2022 (doi:10.1007/10_2022_204)**, not Ulrich; this was explicitly corrected in the session after a verification pass.

---

## Key Facts (with dates/source)

All facts below have no explicit date in the individual claim; session recency date is 2026-06-16 (meeting) and session active date is 2026-06-16/17 based on transcript context.

### The Four-Layer Protocol Stack (adopted, not invented)

The ARPA-H IGoR proposer-day slide described a four-layer architecture. The session identified this as an adoption of the established OSI-stack concept applied to wet-lab automation:

| Layer | Role | Standard/Tool |
|-------|------|---------------|
| **Intent layer** | What the experiment should achieve (disease model, perturbation, readout goal) | LabOP/PAML |
| **Process layer** | Abstract protocol steps (primitives that expand into sub-protocols) | LabOP/PAML |
| **Calibration / QC layer** | Quantitative quality control gates (differentiation markers, perturbation success metrics); RFC governance overlay described as the novel Cytognosis contribution | RFC overlay (novel) + LabOP runtime variables |
| **Hardware layer** | Device-specific execution (liquid handlers, SiLA 2 instrument drivers) | SiLA 2 |

### LabOP / PAML

- **LabOP** (Laboratory Open Protocol language): semantic web-based protocol language for describing laboratory experiments using ontologies.
- **Origin:** DARPA SD2 program, 2016-2022. Goal was to harmonize experimental data across multiple laboratories.
- **Follow-on funding:** Schmidt Futures (open data sets initiative, post-2022).
- **SIFT's role:** Daniel Bryce (dbryce@sift.net) and SIFT were direct co-authors/builders of LabOP during DARPA SD2. This makes SIFT the natural TA3 lead.
- **Canonical citation:** Bartley et al., *ACM Journal on Emerging Technologies in Computing Systems (JETC)*, 2023. (Confirmed correct by verification subagent.)
- **Key capabilities:**
  - Supports high-level primitives that expand into sub-protocols, allowing consistent structure across lab sites while accommodating local variations.
  - Includes a Python library and an execution engine that simulates protocols and emits specific formats (e.g., Autoprotocol, Emerald Cloud Lab instructions).
  - Differentiates between liquid transfer methods (stamping vs. cherrypicking).
  - Allows defining protocols not yet executed and linking them to materialized executions (provenance tracking / root-cause analysis).
  - Uses approximately a dozen integrated ontologies for measurement units, strain types, container types, etc.
  - "Container" in LabOP = material items (96-well plates, flasks), NOT software containers.
- **Runtime variable example:** optical density measurement as a real-time QC check enabling abort/adjust decisions mid-experiment.

### SiLA 2 (Hardware Layer)

- **Role in stack:** device-level hardware abstraction / instrument driver standard.
- **Correct citation:** Juchli 2022, doi:10.1007/10_2022_204. (Session explicitly corrected this from an incorrect prior reference to "Ulrich".)
- **Note:** The session verification subagent flagged the SiLA 2 reference as wrong and the fix was applied to both deliverable docs.

### LinkML / Biolink as the Single Semantic Foundation

- **Position:** One shared semantic foundation across all TAs (TA1, TA2, TA3, TA4), not separate schemas with translation at interfaces.
- **Shahin's explicit statement:** "Building a universal language across technical areas TA1, TA2, and TA3 is essential for ensuring consistent data ingestion and standardized interaction descriptions, which creates a unified foundation for experimental reasoning."
- **LinkML advantages over OWL (as stated in session):** more programmer-friendly; abstracts away RDF complexity while maintaining RDF compatibility; generates Pydantic models and JSON schemas from a single description.
- **Validation precedent:** The NIH Translator project (government-backed) already validated this LinkML workflow.
- **Biolink Model** is the upper ontology layer; LinkML is the schema language; RDF is the serialization format used by LabOP.
- **TA1 connection:** gene/protein/variant descriptions must use the same Biolink/LinkML entities so all TAs share consistent identifiers without translation seams.
- **GA4GH VRS / HGVS** cited as standards for variant representation (relevant to TA1 variant schema compatibility).

### Three-Phase LabOP Extension for Perturbation Biology

LabOP was originally built for synthetic biology (SynBio). The session established a three-phase extension to cover neuropsychiatric perturbation experiments:

1. **Cellular model phase** — differentiation to create the cellular context (e.g., iPSC-to-neuron); QC gate = differentiation biomarkers (specific markers to confirm neuron maturity).
2. **Perturbation phase** — chemical or genetic perturbation (CRISPRi/a, small molecules); QC gate = perturbation success metrics (e.g., integration scores for CRISPR-mediated knockouts).
3. **Readout phase** — transcriptional, morphological, or functional analysis; confirmed to be single-cell calcium imaging for Phase I functional neuronal readout (not MEA electrophysiology).

### ExperimentIntent Interface (TA2 -> TA3)

- **ExperimentIntent** is the structured object passed from TA2 (experimental planning/VOI ranker) to TA3 (protocol execution). It encodes what the experiment is trying to achieve.
- Quantitative metrics must be embedded in each ExperimentIntent to enable root-cause analysis downstream.

### LabCapabilityProfile Interface (TA3 -> TA4)

- **LabCapabilityProfile** communicates TA3-to-TA4 compatibility: which cell models, perturbations, and readouts a given technology (e.g., Cellanome R3200) supports.
- The TA3-to-TA4 translation is **not 1-to-1**; it is a subset relationship. Some technologies support only a subset of readouts or cell models, and the LabCapabilityProfile captures these constraints.
- **Cellanome R3200 SiLA Feature Definition** identified as the single highest-risk Phase I item.

### LLM Extraction Pipeline (Text-to-Structured Protocol)

- **Framework stack:** Instructor + Pydantic (Shahin's proposal) for converting free-form text protocols into structured LabOP objects; DSPy from Stanford (Dan Bryce's validated approach) for trained-model extraction.
- **Purpose:** Onboarding new laboratories efficiently by translating their existing unstructured protocols into the LabOP schema.
- Both Instructor/Pydantic and DSPy are confirmed as valid approaches; the session agreed "employing a trained model is a reasonable approach."

### Other Standards in the Landscape (session research stream)

- **Autoprotocol** — execution format emitted by LabOP execution engine; used by Emerald Cloud Lab.
- **Opentrons** — supported hardware platform.
- **SBOL3** — cited with corrected DOI suffix (.01009; was wrong in draft, fixed in session).
- **Allotrope, Aquarium, BioCoder, Cello** — cited as prior-art lineage for lab protocol languages.
- **IETF/SBOL/GA4GH "RFC-and-bake-off" governance model** — proposed as the governance structure for the RFC calibration/QC overlay layer.
- **MIACARM** — author attribution was wrong in draft; corrected in session.

### FTE Estimates and Staffing (TA3)

- Dan Bryce estimated **2-3 FTEs for TA3**, rising if SIFT also covers TA2 experiment planning (VOI ranker, XP planner).
- Dan's action item: draft three TA3 staffing variants (bare minimum / ideal / overachieving).
- **June 25 deadline** to finalize team configuration.
- TA1 is largely finalized; TA2 requires further discussion.

---

## Decisions

The session produced two explicit "Aligned" decisions (from the Gemini meeting notes) and additional design decisions from the research synthesis:

1. **ADOPTED: LabOP + LinkML as the foundational standardization framework** for protocol modeling and data integration across all TAs. (Aligned; from 2026-06-16 Dan/Shahin meeting.)
2. **ADOPTED: Quantitative experimental metrics and intent tracking** embedded in protocol design to enable root-cause analysis. (Aligned; from 2026-06-16 Dan/Shahin meeting.)
3. **ADOPTED: Single LinkML/Biolink/RDF semantic foundation** for all TAs; no seam translation at interfaces.
4. **ADOPTED: Three-phase LabOP extension** (cellular model / perturbation / readout) with QC gates at each phase.
5. **ADOPTED: SiLA 2 as hardware layer** standard; correct citation is Juchli 2022.
6. **ADOPTED: RFC governance overlay** (Cytognosis-novel contribution) for the calibration layer.
7. **DECISION: PsychIGoR TA3 extends LabOP** rather than adopting a competing standard; this aligns with SIFT as TA3 lead since SIFT co-authored LabOP under DARPA SD2.
8. **DECISION: MEA electrophysiology is NOT the Phase I functional readout** (previously in stale schema); single-cell calcium imaging is correct. The deep-dive MEA schema was flagged to be reworked.

---

## Open Items

1. **TA2 scope decision pending:** Whether TA2 covers the VOI ranker and XP planner, or those sit at the TA2-TA3 seam, is unresolved. This directly determines SIFT's FTE count and budget.
2. **SIFT staffing finalization:** Dan Bryce needs management approval and to share three FTE variants. Deadline: June 25.
3. **Cellanome NDA closure:** Required before the R3200 SiLA Feature Definition (highest-risk TA4 item) can be fully scoped.
4. **LinkML schema repo:** Needs to be stood up; not yet created.
5. **Stale MEA schema text:** Deep-dive TA3 doc section on MEA electrophysiology needs rework to reflect calcium imaging decision.
6. **Dan/Shahin follow-up call:** Was scheduled for June 17 morning to discuss TA2 alignment and SIFT's internal scoping.

---

## Conflicts to Flag

1. **SiLA 2 citation:** Prior IGoR docs (pre-session) used "Ulrich" as the SiLA 2 author. The correct citation is **Juchli 2022 (doi:10.1007/10_2022_204)**. Any IGoR document that still references "Ulrich" for SiLA 2 must be corrected.
2. **MEA vs. calcium imaging:** Pre-session IGoR materials included MEA electrophysiology as a functional readout option for TA4. This is stale; Phase I functional neuronal readout is single-cell calcium imaging only. MEA text needs to be reworked.
3. **SBOL3 DOI:** Prior draft had incorrect DOI suffix; corrected to .01009 in the session deliverables. Check any other IGoR docs citing SBOL3.
4. **LabOP scope (SynBio vs. perturbation biology):** LabOP was built for SynBio (DARPA SD2). The three-phase extension to neuropsychiatric perturbation biology is a Cytognosis/PsychIGoR contribution; this must be framed carefully in the proposal (extending the standard, not claiming LabOP itself as novel).
