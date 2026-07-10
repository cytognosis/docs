# Cytognosis Vocabulary Alignment Audit

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: designers, stakeholders
> **Tags**: `design`, `design-system`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

**Purpose:** establish canonical Cytognosis vocabulary, product architecture, and current strategic content, then flag every divergence in the design system at `01_extracted/v11_1/` (content identical in the newer 11.1.1 export). Read-only research; no design-system files edited.

**Date:** 2026-07-09. **Sources:** science-platform skill (`.claude/skills/science-platform/`), Strategic Planning `master_plan/` (verified directly, not just relayed), Website Design Handbook, LinkedIn public post, PsychIGoR/IGoR grant documents, cytomem recall, and a direct line-by-line audit of the design system tree (cross-checked against an independent subagent pass; the Helix count matches exactly: 23 live occurrences across 14 files).

**If you only read one thing:** the design system currently ships a fourth public "product," **Helix Model, the Engine**, alongside Cytoverse/Cytoscope/Cytonome, in its live skill description, README, writing guide, brand-foundation reference, landing page, landing UI kit, dashboard, icon set (with its own logo asset), and compiled bundle. Per the founder, "Helix" is only ever the internal org-structure draft. It must be purged from every public-facing surface, not renamed or softened.

---

## 1. Canonical vocabulary

### 1.1 Product architecture

| Name | Metaphor | One-line role | Status |
|---|---|---|---|
| **Cytoverse** | The map | AI health mapping system; continuous, multimodal coordinates across micro (molecules/cells), meso (connectomes/circuits), and macro (behavior/phenotype) biological scales | Public |
| **Cytoscope** | The sensor | Programmable, universal biosensor and wearable layer; triangulates an individual's coordinates on the Cytoverse map in real time | Public |
| **Cytonome** | The navigator | Privacy-first, on-device causal AI; converts coordinates into personalized recommendations (defensive, corrective, supportive); the consumer-facing app most users experience | Public |

Verbatim, most authoritative (master_plan, v2.0, May 2026): *"The Cytognosis Platform is what we build. It has three components, in plain language: a map (Cytoverse), a sensor (Cytoscope), and a navigator (Cytonome). Together they are GPS for Human Health."* (`10_platform_architecture.md:5`; near-identical in `00_executive_summary.md:15-23`.)

There is **no fourth public product**. Supporting, non-product pillars exist behind the platform (org/infra, never customer-facing brand names): **P4 Open-Science Substrate**, **P5 Clinical Translation**, **P6 Organization and Helix** (`01_identity_and_framework.md:91`; the "Helix" here is the internal org-structure token, see Section 2).

**First flagship deployment (public):** **Neuroverse**, brain and mental health as continuous phenotypes. This is already correctly named in the design system's own `README.md:26`: *"First major deployment: Neuroverse, a continuous multi-scale map of brain and mental health integrating genomics, single-cell biology, connectomics, wearable physiology, and behavioral signals."* Confirmed public via a LinkedIn post (`Strategic Planning/LinkedIn_Addendum_Neuroverse_2026-05-04.md`) and the dashboard UI kit ("Neuroverse Dashboard"). **Next planned (naming pattern only, not yet public):** "Immunoverse," for immune/metabolic/oncology domains.

### 1.2 Approved framings and taglines

- **"GPS for Human Health"** — canonical full form. Majority usage inside the design system itself (`README.md:11`, `references/01_brand_foundation.md:25`, `guidelines/brand-voice.card.html` tagline bank) and in the most recent master-plan version (`00_executive_summary.md`, May 2026).
- **"GPS for Health"** — a shorter variant in live concurrent use elsewhere (science-platform skill's own `critical_rules`, the Website Design Handbook, and the org's own "safe to publish" list). Not wrong, but inconsistent with the design system's majority usage. See Open Question 5.1.
- **Three blindspots** (verbatim, `00_executive_summary.md:7-13`, matches science-platform skill exactly):
  - *Mechanistic blindness* — "Treating clusters, not biology. Depression has 4+ molecular subtypes; first-line antidepressants fail 30 to 60% of patients. Autoimmune diagnosis takes 4.5 to 7 years across 4+ specialists."
  - *Temporal blindness* — "Alzheimer's pathology begins decades before memory loss; cancer mutations circulate years before tumors form; type 2 diabetes is 50 to 80% reversible at prediabetes but under 10% after clinical onset."
  - *Complexity blindness* — "Continuous glucose monitoring revealed that identical meals produce dramatically different metabolic responses across people. We have not generalized that revolution beyond a single molecule." (Note: "revolution" here describes the CGM scientific advance, not marketing language; keep as-is, it is not a banned-word violation in context.)
  - This framing does **not currently appear anywhere in the design system**, in-scope or in `uploads/`. Content gap, not a divergence; see Section 4.
- **"Disease as trajectory, not label."** Already correctly present, `README.md:13`: *"Core belief: Disease is a trajectory, not a label. Cytognosis maps that trajectory before symptoms emerge."* Keep as-is.
- **"Before diagnosis. Before symptoms. There's Cytognosis."** Closing tagline, on-canon, keep.
- **Bridge line:** "Cytognosis exists so no one else waits decades for answers." (master_plan `README.md:7`; science-platform skill.)
- **Etymology:** Greek *cyto* (cell) + *gnosis* (knowledge), "cellular knowledge that precedes diagnosis."
- **Terminology preference:** "intercept," not "prevent"; "years before symptoms," not "early."

### 1.3 Org identity facts

| Fact | Value |
|---|---|
| Legal name | Cytognosis Foundation, Inc. |
| Type | 501(c)(3) nonprofit; Delaware nonprofit corporation |
| Incorporated | September 8, 2025 (design system's own README already has this right) |
| EIN | 39-4383634 |
| UEI | HS4PRLL7AKY5 |
| HQ / registered address | South San Francisco, CA. Mailing address is the founder's Daly City residence; reconcile against the IRS determination letter before any public surface requires a physical address (the org's own Website Handbook already flags this as unresolved). |
| Founder | Shahin Mohammadi, Founder and CEO |
| Website | cytognosis.org |
| Design system contact | branding@cytognosis.org |

### 1.4 Founder story (public-safe boundary)

Core narrative: 20 years as a computational biologist (MIT, Broad Institute, insitro, GenBio AI) plus a 37-year diagnostic odyssey resolved by self-directed genomic analysis that found a single ultra-rare causal mutation. **Public phrasing stays at "a single rare genetic mutation" / "37 years, 10 misdiagnoses, one rare mutation."** The specific gene (TBX1) is grants/scientific-context only, never public-facing (explicit org policy, Website Design Handbook DO-NOT-PUBLISH list). Multiple approved, public-safe length/context variants already exist in `science-platform/references/founder-story-variants.md` (pitch deck, website hero, grants, social, video) and should be the source for any founder-story copy the design system carries, rather than freehand rewrites.

### 1.5 Current neuropsych positioning (what is safe to put in public design-system copy)

**Neuroverse is the front-of-house framing.** Strongest current, public-safe phrasings:

- *"We are starting with brain health, focused on psychiatric and neurodegenerative conditions. We call this first deployment Neuroverse."* (public LinkedIn post, 2026-05-04)
- *"A continuous multi-scale map of brain and mental health integrating genomics, single-cell biology, connectomics, wearable physiology, and behavioral signals."* (design system's own README:26, already approved, just not yet on the landing page)
- *"Continuous transdiagnostic axes now span 66% of psychiatric genetic variance, backed by our own cell atlases in schizophrenia (Science 2024) and Alzheimer's (Nature 2019). Categorical DSM labels are giving way to component phenotypes that move on measurable trajectories."* (same LinkedIn post; citing already-published, already-public papers is safe)
- Supporting evidence already used in approved pitch/grant contexts (safe, literature-based, no grant specifics): *"Depression has 4+ molecular subtypes; first-line antidepressants fail 30 to 60% of patients."*

**Not safe for the design system:** anything from the PsychIGoR / ARPA-H IGoR solution summary (program name, teaming partners, budget, solicitation number, schizophrenia/bipolar disorder as a *named grant target*). The org's own Website Handbook DO-NOT-PUBLISH list explicitly bars "ARPA-H / IGoR specifics (solicitation numbers, status, teaming partners)." Citing the already-published schizophrenia and Alzheimer's science papers is fine; describing the unannounced $50M/$43M grant built around them is not.

### 1.6 Mechanics (already well-enforced in the live design system; not a divergence)

Banned: "revolutionary," "breakthrough," "cure," "game-changing," plus "disrupt," "cutting-edge," "best-in-class," "seamless," "powerful," "just/simply/only." No em dashes; Oxford comma; active voice. The audit found no live banned-word violations or em dashes in authored design-system copy (two historical violations were already fixed in Revision 1, confirmed by direct read). This is working correctly and needs no correction.

---

## 2. Internal-only list

| Term | Definition | Where it correctly lives | Public design-system status |
|---|---|---|---|
| **Helix** | Per the founder: an internal draft evaluating the existing org structure and proposing a scalable, mission-centric, moonshot org design. Federated Foundation + PBC (+ eventual regional sister orgs) structure. NOT a product, NOT public. | `personal-drafts/Operations/Organizational Strategy (Helix)/`, `Grants/01-strategy/helix/`, `Strategic Planning/draft/Helix_Framework_Paper.md`, `master_plan/20_organization_helix.md` (pillar token P6) | **Must not appear anywhere.** Currently appears 23 times across 14 files as a fabricated fourth product, "Helix Model." See Section 3. This is a naming collision, not an authorized shorthand: the product usage and the org-draft usage are unrelated and must never be conflated. |
| **Yar** | Internal codename for an early Cytonome build ("Cytonome v0.1"). | `Yar/` project | Correctly absent from the design system already (the merge project's own review explicitly scoped it out: "D1: Yar in or out? Out."). No action needed, just confirming no leakage. |
| **Ali_old** | Ali's personal brand system, unrelated to Cytognosis. | N/A | Confirmed out of scope, zero Cytognosis references. No action needed. |
| **PsychIGoR / ARPA-H IGoR specifics** | The $50M/$43M ARPA-H grant proposal (Purdue/IPAI prime, Cytognosis subawardee, plus SIFT, Cellanome, McLean, Illumina) targeting schizophrenia (Phase I/II) and bipolar disorder (Phase III). | `Grants/02-submissions/Grants/ARPA-H/IGoR/` | Barred from public surfaces by the org's own DO-NOT-PUBLISH policy (program name, teaming partners, budget, status). Not currently in the design system; keep it that way. |
| **TBX1 / specific gene variant** | The founder's causal mutation. | Grants and scientific contexts only | Public phrasing stays at "a single rare genetic mutation." Relevant because the design system's landing-page origin story needs a public-safe founder-story rewrite (Section 3); do not introduce the gene name while fixing it. |
| **"Dr. Lena Park" / "Dr. A. Moreau"** | Recurring fictional personas used across three templates each (`deck.html`, `one-pager.html`, `email-signature.html`, `social-cards.html`) with realistic-looking emails/phone numbers. | N/A, placeholder content | Not a codename, but realistic enough to be mistaken for a real person if shipped unedited. Flag for a "replace before use" note, not necessarily a rewrite now. |
| **"Signal, Cohort, Trace"** | Retired placeholder product names, now lingering only as feature-naming examples in `WRITING.md`. | N/A | Confirmed harmless (not asserted as products) by the merge project's own audit, but reads confusingly close to product names. Low-priority cleanup, see Section 4. |

---

## 3. Divergence audit

All paths relative to `Science and Platform/design-system-merge-2026-07/01_extracted/v11_1/`. Full replacement copy is in Section 4; this table is the map from problem to fix.

| # | File:line | Current text (excerpt) | Problem | Fix in Section 4 |
|---|---|---|---|---|
| 1 | `SKILL.md:4` | "...for the Cytognosis platform (Cytoverse, Cytoscope, Cytonome, and the Helix Model)..." | Helix exposure, in the live active skill description | 4.2 |
| 2 | `README.md:1,3` | "Cytognosis Design System, v10.1.0" / "Version: 10.1.0" | Stale version; contradicts `SKILL.md` (v11.0.0), `VERSION` file, and `CHANGELOG.md` (all v11.x) | 4.1 |
| 3 | `README.md:17-24` | Four-row "Platform Architecture (four products)" table incl. Helix Model | Stale/incorrect product architecture; Helix exposure | 4.1 |
| 4 | `WRITING.md:140` | "Products: the Cyto- family (Cytoverse, Cytoscope, Cytonome) plus Helix Model. Product names are already set..." | Helix exposure; actively instructs future writers to treat it as a set product name | 4.2 |
| 5 | `WRITING.md` (feature-naming examples) | "Signal, Cohort, Trace" lingering as examples | Retired placeholder names read as product-adjacent | 4.2 |
| 6 | `references/01_brand_foundation.md:54-61` | Platform architecture table incl. "Helix model \| Foundation AI model \| The Engine" | Helix exposure | 4.3 |
| 7 | `ICONOGRAPHY.md:38` | "Products \| cytoverse, cytoscope, cytonome, helix \|" | Helix listed as a shipped Products icon | 4.6 |
| 8 | `assets/icons/line/helix.svg`, `assets/icons/solid/helix.svg` | Icon files | Shipped assets for a non-existent product | 4.6 |
| 9 | `assets/icons/cytognosis-icons-line.svg:11`, `cytognosis-icons-solid.svg:11` | `<symbol id="cg-helix">` | Helix baked into both sprite sheets | 4.6 |
| 10 | `assets/icons/icons.card.html:30,79,119` | Symbol defs + rendered gallery figure with `figcaption>helix` grouped under "Products" | Visible, rendered Helix product icon in the gallery | 4.6 |
| 11 | `ui_kits/landing/index.html:333-334` | Heading "Four systems, working as one instrument" + sub-copy naming Helix | Helix exposure; contradicts the flagship landing page's own "Three systems" heading | 4.4 |
| 12 | `ui_kits/landing/index.html:352-354` | Fourth platform card, "Helix Model / the engine" | Helix exposure | 4.4 |
| 13 | `ui_kits/landing/index.html:483` | Footer nav link "Helix Model" | Helix exposure | 4.4 |
| 14 | `"Cytognosis Landing Page.html":197-198` vs `:230-242` | Heading says "Three systems... Cytoverse, Cytoscope, and Cytonome," but a separate `.engine-row` block directly below reintroduces "Helix Model, the engine" | Direct self-contradiction inside one file; Helix exposure | 4.4 |
| 15 | `"Cytognosis Landing Page.html":363` | Footer nav link "Helix Model" | Helix exposure | 4.4 |
| 16 | `profiles/lab-example.jsx:19,41` | Fake terminal prompt `shahin@helix ›` | Pairs founder's name with "helix" as a literal hostname in shipped example code | 4.5 |
| 17 | `_ds_bundle.js:6794,6960,9596,9762` | Compiled string `"helix"` (from the icon gallery figcaption) | Auto-generated; will keep recurring until the icon gallery source is fixed | 4.6 (regenerate after) |
| 18 | `guidelines/type-display.card.html:24` | H1-gradient specimen text "GPS for Health" | Tagline drift from canonical "GPS for Human Health" (see Open Question 5.1) | 4.3 |
| 19 | `ui_kits/dashboard/index.html:116,170` | "Neuroverse · v10.1 · Research" sidebar meta; `v10.1.0` topbar badge | Stale version string baked into a v11.1-era mockup; ambiguous whether it is the design system's own version leaking in | 4.5 |
| 20 | `references/02_voice_and_tone.md` ("good" headline example); `guidelines/type-body.card.html` (Body Large sample) | "Our AI analyzes your cells/cellular signals at the molecular level, finding/mapping... before traditional tests can detect anything" | Reads close to the system's own flagged "bad example" of implying diagnosis; inconsistent with "non-diagnostic by design" and the skill's "intercept" language | 4.3 |
| 21 | `"Cytognosis Landing Page.html"` origin/story section (~lines 103-121) | Generic, unattributed founder narrative, no names/dates/institutions | Does not reflect the real, approved, public-safe founder story | 4.4 |
| 22 | `"Cytognosis Landing Page.html"` hero/platform section | No mention of Neuroverse anywhere | Content gap: understates the org's current brain-health-first focus, which the design system's own README and the dashboard UI kit already reflect | 4.4 |
| 23 | Design system tree-wide | No "three blindspots" content anywhere, in-scope or in `uploads/` | Content gap: a load-bearing problem-framing used everywhere else (master plan, science-platform skill, planned website /science page) is absent here | 4.3 |
| 24 | `_ds_manifest.json` (Lumen Glass System card subtitle) | "v0.2 — blue/green forward, sharper scientific tone" | Em dash in a live, in-scope JSON file | Already known and waived per `CHANGELOG.md` (sourced from a frozen `uploads/` card, auto-regenerated); no action needed unless fixing the upstream `uploads/` source too |
| 25 | `references/06_iconography.md:16` vs `ICONOGRAPHY.md` | Two different, inconsistent icon-family breakdowns (a `dna-helix` planned icon here vs. the shipped 8-family, 48-icon system in `ICONOGRAPHY.md`) | Structural duplication/conflict between two files both claiming to define the icon set | 4.6 |
| 26 | `templates/deck.html`, `one-pager.html`, `email-signature.html`, `social-cards.html` | Recurring fictional personas "Dr. Lena Park" and "Dr. A. Moreau" with realistic contact details | Realistic enough to be mistaken for real if shipped unedited | Flag only; not urgent, note in Section 4 |

**Root-cause note:** the Helix-as-product error is not a one-off AI hallucination. It is baked into the design system's own source brief, `uploads/05_final_landing_page_and_design_system_prompt.md:34` ("5. Platform Architecture: Cytoverse, Cytoscope, Cytonome, Helix model") and the earlier `uploads/Cytognosis_Design_System_v10_1_Source.md:66` and `uploads/CEO_Loved_Design_System_Reference.html:305`. `uploads/` is out of scope for direct editing per the audit instructions, but if a future v12 export is regenerated from that same prompt file without correcting it first, this exact error will recur. Worth a one-line fix in the prompt file itself, not just in the outputs.

---

## 4. Content revision spec

Exact copy for the design-system revision prompt to carry, grouped as requested.

### 4.1 `README.md` (top level)

Replace the title block:
> Cytognosis Design System, v10.1.0
> **Last updated:** June 2026 | **Version:** 10.1.0 | **Maintained by:** Cytognosis Foundation Design

with the current version string (pull from `VERSION` file / `SKILL.md` frontmatter, currently v11.x, not v10.1.0).

Replace the four-row "Platform Architecture (four products)" table with:

```
### Platform Architecture (three products)

| Product | Metaphor | Role |
|---------|---------|------|
| **Cytoverse** | The Map | AI health mapping system, constructs the health coordinate space |
| **Cytoscope** | The Sensor | Programmable biosensors, triangulates position over time |
| **Cytonome** | The Navigator | On-device causal AI, translates coordinates to insights |
```

Keep line 26 exactly as-is ("First major deployment: Neuroverse...") and propagate it to the landing page (4.4).

### 4.2 `WRITING.md`

Replace line 140:
> "Products: the Cyto- family (Cytoverse, Cytoscope, Cytonome) plus Helix Model. Product names are already set; do not coin new ones without brand review, and never append numerals to a product name."

with:
> "Products: the Cyto- family (Cytoverse, Cytoscope, Cytonome). Product names are already set; do not coin new ones without brand review, and never append numerals to a product name."

Separately, replace any lingering "Signal, Cohort, Trace" feature-naming examples with verb+object examples that match the line immediately above them ("compare cohorts," not "Cohort Comparison"), e.g. "track trajectory," "flag deviation," "review history."

### 4.3 References

`references/01_brand_foundation.md:54-61` — same fix as 4.1: drop the Helix Model row, keep the three-row table.

`references/02_voice_and_tone.md` "good" headline example — replace:
> "Our AI analyzes your cells at the molecular level, finding patterns that signal disease long before traditional tests can detect anything."

with:
> "Cytognosis maps cellular signals into a continuous picture of health. Shifts become visible years before symptoms would otherwise appear. Non-diagnostic by design."

`guidelines/type-body.card.html` Body Large sample — replace:
> "Our AI analyzes cellular signals at the molecular level, mapping disease trajectories before traditional tests detect anything."

with the same replacement text as above, or:
> "Cytognosis transforms complex biological and behavioral signals into interpretable phenotype vectors, mapping trajectories years before symptoms emerge."

`guidelines/type-display.card.html:24` — replace "GPS for Health" specimen text with "GPS for Human Health" (matches the rest of the system; see Open Question 5.1 if the founder prefers to standardize the whole system on the short form instead).

Add a new reference module for the three blindspots (content gap, item 23), mirroring `science-platform/references/three-blindspots-detail.md`:

```
### The Three Blindspots

Mechanistic blindness. Treating clusters, not biology. Depression has 4+ molecular
subtypes; first-line antidepressants fail 30 to 60% of patients. Autoimmune diagnosis
takes 4.5 to 7 years across 4+ specialists.

Temporal blindness. Alzheimer's pathology begins decades before memory loss; cancer
mutations circulate years before tumors form; type 2 diabetes is 50 to 80% reversible
at prediabetes but under 10% after clinical onset.

Complexity blindness. Continuous glucose monitoring revealed that identical meals
produce dramatically different metabolic responses across people. We have not
generalized that beyond a single molecule.
```

### 4.4 Landing page hero and sections

`ui_kits/landing/index.html:333-334` — replace:
> "Four systems, working as one instrument." / "Cytoverse, Cytoscope, Cytonome, and the Helix Model form one connected platform..."

with:
> "Three systems, working as one instrument." / "Cytoverse, Cytoscope, and Cytonome form one connected platform for mapping health across biological, behavioral, and clinical dimensions, each named for the role it plays in understanding a person."

Delete the fourth platform card (`:352-356`) and the footer nav link "Helix Model" (`:483`).

`"Cytognosis Landing Page.html":230-242` — delete the entire `.engine-row` block (the "Helix Model, the engine" card) and its footer nav link (`:363`). The heading (`:197`) and three-card grid (`:201-228`) already match canon exactly and need no change once the engine-row is removed.

Add a Neuroverse callout to the platform section (content gap, item 22), using the design system's own already-approved README language:
> "Our first deployment, Neuroverse, maps brain and mental health as continuous phenotypes, integrating genomics, single-cell biology, connectomics, wearable physiology, and behavioral signals."

Replace the generic origin/story section (~lines 103-121) with a public-safe founder-story variant pulled from `science-platform/references/founder-story-variants.md` (WEB2, "Shorter Hero," 67 words, already vetted against the DO-NOT-PUBLISH gene-variant rule):
> "After 37 years navigating a labyrinth of misdiagnoses, ten specialists, and failed treatments, I did what no doctor could: I used the AI and genomics tools I'd spent my career building to find my own answer. One ultra-rare mutation. One root cause. Everything connected. That journey exposed what's broken in medicine, and what Cytognosis exists to fix. No one should need a PhD in computational biology to understand their own health."

(Adjust em dashes to commas if the source variant uses any; the version above already does.)

### 4.5 Dashboard UI kit labels and misc.

`ui_kits/dashboard/index.html:116,170` — "Neuroverse" label is correct and should stay. Replace the `v10.1` / `v10.1.0` strings: if these are meant to mirror the design system's own version, update to current; if they are a fictional in-app product version, restyle so they cannot be mistaken for the design system's version (e.g., "Neuroverse · Research Build," no version number).

`profiles/lab-example.jsx:19,41` — replace the `shahin@helix ›` hostname with a product-neutral one, e.g. `shahin@cytoctl ›` or `shahin@lab ›`.

### 4.6 Icon set names

`ICONOGRAPHY.md:38` — replace:
> "Products | cytoverse, cytoscope, cytonome, helix |"

with:
> "Products | cytoverse, cytoscope, cytonome |"

Delete `assets/icons/line/helix.svg` and `assets/icons/solid/helix.svg`. Remove the `id="cg-helix"` symbol from both `cytognosis-icons-line.svg:11` and `cytognosis-icons-solid.svg:11`. Remove the corresponding symbol defs and the rendered gallery figure (`figcaption>helix`) from `assets/icons/icons.card.html:30,79,119`. Regenerate `_ds_bundle.js` afterward so the four compiled `"helix"` strings (`:6794,6960,9596,9762`) clear on their own.

A DNA/bio-molecule glyph is not needed to replace it: the "Bio & science" family already has a distinct `dna` icon. If a more literal double-helix glyph is wanted for that family specifically (not for Products), add it there under a new id such as `cg-dna-helix`, matching the existing bio-family naming pattern, and reconcile it against the conflicting entry in `references/06_iconography.md:16` (item 25) so only one file defines the shipped icon set going forward.

### 4.7 Manifest card subtitles

`_ds_manifest.json` Lumen Glass System card subtitle, em dash: no action needed now (already documented and waived in `CHANGELOG.md` as inherited from a frozen `uploads/` source). Optional: fix the em dash in the upstream `uploads/v11_grafts_2026-07-08/lumen-glass-system.html` source card too, so the exception can eventually be retired instead of permanently waived.

---

## 5. Open questions

1. **"GPS for Human Health" vs. "GPS for Health."** Both are canonical in different places: the design system's own majority usage and the newest master-plan version favor the full form; the operational science-platform skill and the live Website Design Handbook favor the short form. Recommend standardizing the design system on "GPS for Human Health" (matches its own majority usage) and revisiting the short form as a possible universal simplification in a separate, single decision that also touches the skill and the website, rather than solving it piecemeal here.
2. **The underlying foundation model's public name.** Cytoverse's description already covers "multimodal foundation models" without needing a separate named "engine." If the founder wants a distinct public name for that layer someday, it must not be "Helix" (reserved for the org draft) and should go through the same brand-review process as any new product name. Not resolved here; flagging so it doesn't get silently reintroduced under a different label.
3. **Dashboard version strings.** Whether `ui_kits/dashboard/index.html`'s "v10.1" badges represent the design system's own version (needs updating) or a fictional in-app product version (fine as-is, just needs restyling to avoid confusion). Needs a founder call.
4. **"Blueprint v8" and "two-axis taxonomy."** Referenced in prior consolidation notes but not found as literal artifacts anywhere in `~/Claude/Projects`; likely a paraphrase or an archived/renamed document from the 2026-06-21 to 07-08 consolidation window. This is a document-organization taxonomy question, orthogonal to the design system's public content; no action needed for this audit.
5. **Two conflicting icon-family files** (`ICONOGRAPHY.md` vs. `references/06_iconography.md`). Needs a decision on which is canonical going forward; see item 25 above.
6. **"Founded in 2024" vs. September 8, 2025.** Several active grant applications (including the current Google Impact revision) state the Foundation was "founded in 2024," contradicted by the confirmed incorporation date. The design system's own README already has the correct date, so this is not a design-system fix, but it is a live factual error elsewhere worth a separate correction pass.
