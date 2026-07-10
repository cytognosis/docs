# Compute & Credits Applications — Anthropic AI for Science · NAIRR Pilot · Cohere Catalyst (DRAFTS v1)

**Compiled 2026-05-31.** Lowest-priority funnel items (non-dilutive compute/credits). All three are rolling; none is deadline-critical. Cytognosis org facts for every form: **Cytognosis Foundation, Delaware 501(c)(3), EIN 39-4383634, Daly City CA; use an institutional `@cytognosis.org` email** (NAIRR rejects personal/gmail).

| Program | What you get | Channel | Cadence | Fit | Verify |
|---|---|---|---|---|---|
| **NAIRR Pilot — Research Resources** | GPU/compute allocation (12 mo) for AI research; **open results required** | 3-page PDF + form at submit-nairr.xras.org | Monthly (by 15th → decision end of next month) | High — funds Cytoverse FM training; nonprofit-eligible | resource catalog at submit-nairr.xras.org/resources |
| **Anthropic — AI for Science** | ~$20–50K Claude API credits | Google Form (from anthropic.com/news/ai-for-science-program) | Rolling, monthly review | High — Claude for curation/agentic experiment design/macro-LLM layer | confirm form fields + current credit ceiling |
| **Cohere Labs — Catalyst Grant** | Cohere API credits (Command/Embed/Rerank) | Form at cohere.com/research/grants/application (JS-rendered; email labs@cohere.com) | Rolling | Med-High — healthcare is an explicit focus; embeddings/rerank for the Yar/Cytonome knowledge graph | exact fields not web-exposed — confirm on form |

---

## 1. NAIRR Pilot — Research Resources (3-page proposal draft)

**Eligibility/fit:** US nonprofit ✓; focus-area match = "creating open-source AI tools, models, datasets, and methods," "AI methods that enable scientific discovery + interpretability," and "applying AI to integrate sensitive data from multiple sources." **All results open/publishable** — aligns with Cytognosis's Apache 2.0/CC BY mandate.
**Eval criteria (write to these):** focus-area alignment · readiness/near-term progress · technical feasibility · need for the resources · team knowledge/experience · resource estimate + justification.

**Title:** *Cytoverse: an open, multiscale foundation-model map of human biology for scientific discovery (precision-psychiatry proving ground).*

**Project (≤3 pp):**
- **Problem & focus-area alignment.** No open, multiscale, mechanistic model integrates molecular → cellular → connectomic → behavioral data at individual resolution; we build one as open-source models/datasets/methods (NAIRR focus areas 1, 3, 5). Proving ground: precision psychiatry (where categorical DSM models fail).
- **Approach.** Foundation models trained end-to-end across scales (cross-resolution attention; residual/"delta-from-healthy" disease modeling; genomics-as-instrument causal disentanglement). Training data: PsychENCODE 388 paired WGS+snRNA/ATAC, ROSMAP, NeuroBioBank — i.e., integrating sensitive multi-source data (focus area 3).
- **Readiness.** Architecture designed; datasets accessible under existing DUAs; PI built the upstream atlases; methods piloted (ACTIONet). Near-term milestone: cellular + connectomic FM v1 + open release.
- **Resource request + justification.** Large-GPU allocation (H100/A100-class) for FM pre-training/fine-tuning; estimate from the NAIRR resource catalog (e.g., a multi-thousand GPU-hour allocation across 12 months). Justify by model scale (genes/voxels-as-tokens, cross-scale blocks).
- **Team.** PI Mohammadi (PsychENCODE/PsychAD/ROSMAP; *Science* 2024) + Purdue IPAI (Grama; scalable compute) + Ruzicka (clinical; McLean / Harvard).
- **Open dissemination.** Models/weights/code → Apache 2.0/CC BY; preprint + repository; aligns with NAIRR's open mandate.

**Actions:** register at submit-nairr.xras.org with `@cytognosis.org` email; pick resources from the catalog; submit by the 15th for next-month decision.

---

## 2. Anthropic — AI for Science (Claude API credits) draft

*(Rolling; submit the Google Form linked from anthropic.com/news/ai-for-science-program. Confirm exact fields + ceiling. Biosecurity screening applies.)*

- **Project summary.** Cytognosis builds Cytoverse, an open multiscale model of human biology (pilot: precision psychiatry). We request Claude API credits to accelerate the AI-orchestration and knowledge-curation layers.
- **How Claude will be used.** (1) Agentic literature/biotype curation across psychiatric/neurodegenerative disease (assembling the reproducible, well-cited biotype corpus that anchors the map); (2) experiment/analysis-design assistance (uncertainty-driven "what to measure next" — the same active-learning logic as ARPA-H IGoR's orchestration layer); (3) the macro-scale language layer of the Cytonome navigator (on-device Gemma for inference; Claude for development/eval/distillation targets); (4) code generation for the open pipeline.
- **Significance.** Open, reproducible infrastructure for precision psychiatry; replaces categorical DSM labels with biology-anchored coordinates.
- **Open science / safety.** Outputs released open (Apache 2.0/CC BY); Cytoplex safety layer blocks diagnosis/treatment claims; no PHI sent to the API; biosecurity-aware (no dual-use wet-lab protocols).
- **Team.** PI Mohammadi (20 yrs AI-for-biology; *Science*/*Nature* atlases) + collaborators (Purdue IPAI, McLean, Mount Sinai). Org: Cytognosis Foundation, 501(c)(3).
- **Credit estimate.** [fill against the form's ceiling — e.g., the max offered].

---

## 3. Cohere Labs — Catalyst Grant (API credits) draft

*(Rolling; apply at cohere.com/research/grants/application; the page is JS-rendered — if the form isn't visible, email labs@cohere.com. Healthcare & Life Sciences is an explicit Cohere focus.)*

- **Project.** Cytonome / Yar's knowledge-graph + retrieval layer for neurodivergent and precision-mental-health users: turning messy multimodal capture into a typed, semantically-retrievable personal knowledge graph.
- **Why Cohere models.** **Embed** + **Rerank** for high-quality semantic retrieval over the personal knowledge graph (the "scaffolded memory" ND users need); **Command** for structuring/summarization where on-device models need a stronger fallback; **Aya** multilingual for equitable, culturally-responsive access.
- **Public-impact / open science.** Nonprofit, open-source components (Apache 2.0); health-equity framing (underserved neurodivergent + mental-health populations); privacy-first (local-first by default; Cytoplex safety gate).
- **Team & ask.** PI Mohammadi + Cytognosis Foundation (501(c)(3)); request API credits (amount per the program) + (optionally) `labs@cohere.com` for additional credits.

---

### Cross-cutting verify-before-submit
- Use `@cytognosis.org` institutional email everywhere (NAIRR hard rule).
- Confirm each form's current exact questions/limits (Anthropic + Cohere forms are not web-scrapable; NAIRR's 3-page instructions at nairrpilot.org/nairr-pilot-proposal-instructions).
- NAIRR is **compute, not cash**, and requires open results + brief 1-mo/6-mo updates + a 3-page final report.
- These are non-dilutive and low-effort; sequence them after the deadline-critical apps (AWS, Foresight, IGoR).
