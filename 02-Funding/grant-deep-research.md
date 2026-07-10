# Grant & Funding Opportunity Pipeline — Deep Research Report

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: leadership, grant team
> **Tags**: `funding`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

**Status:** Living document
**Last updated:** 2026-05-24
**Maintainer:** mohammadi@cytognosis.org

---

## Executive Summary

The Cytognosis grant pipeline is an ambitious system that transforms unstructured funding opportunity announcements (PDFs, DOCX, XLSX) into structured, harmonized data, and then renders that data into funder-specific submission documents. The architecture spans six Python modules, a 27-slot canonical template schema (v1.2), 17 funder profile YAML files, 71 mapped funding opportunities, and a Nox/CLI-based orchestration layer.

**Key finding:** The *schema layer* (manifest, slots, funders, opportunity mappings) is remarkably mature and well-designed. The *pipeline code layer* (parser → extractor → harmonizer → generator → renderer) has production-quality bookends (parser and extractor work end-to-end) but a hollow middle (harmonizer uses placeholder logic, generator needs templates, renderer lacks Pandoc/Quarto wiring).

---

## 1. Schema System — Findings & Convergence Status

### 1.1 Canonical Slot System (CONVERGED)

The 27-slot system (U01–U22 universal + A01–A05 administrative) is the intellectual backbone of the entire pipeline. Slot IDs are immutable and append-only, which is the correct design choice.

| Metric | Value | Assessment |
|---|---|---|
| Total slots defined | 27 | ✅ Sufficient for all 71 tracked opportunities |
| Slots with authored prose | 4 (U01, U03 partial, U06 partial, U08) | ⚠️ 15% coverage |
| Slots as stubs | 23 | 🔴 Content authoring is the main bottleneck |
| Sub-slots identified but deferred | 30+ | Tracked in CHANGELOG v1.1/v1.2 |

**Design decision (sound):** Slot content is author-once, render-many. The same U01 "Core Objective" text serves NSF, ARPA-H, NIH, and every other funder. Funder-specific framing lives in the funder YAML `heading:` text, not in slot bodies.

**Design decision (sound):** Length limits are render-time, not author-time. Content is authored at the longest funder limit and trimmed during rendering.

### 1.2 Funder Metadata Fields (CONVERGED)

The F-field family (F01–F38) captures 38 metadata dimensions per opportunity. This was extended from 11 (Monday board columns) to 30 in v1.1, then to 38 in v1.2.

| Version | Fields | Driver |
|---|---|---|
| v1.0 | F01–F11 | Existing Monday columns |
| v1.1 | F12–F30 | Research of 71 opportunities |
| v1.2 | F31–F38 | Drive funding-research cross-reference (insider connections, strategic pairings, thematic tags) |

Notable v1.2 additions:
- **F31 `strategic_connection`** — Tracks insider contacts (Adam Marblestone, Milad Alucozai, Angela Pisco, etc.)
- **F32 `strategic_pairing`** — Links opportunities that move together (NSF Tech Labs ↔ Convergent Research FRO)
- **F33 `thematic_tags`** — Hashtag taxonomy (#Moonshot, #FRO, #Cytoscope, etc.)
- **F35 `heilmeier_required`** — Whether Heilmeier Catechism is mandatory

### 1.3 Funder Profiles (WORK IN PROGRESS)

17 funder YAML files exist under `schemas/funders/`. Coverage:

| Funder File | Kind | Has Template Definition | Has F31–F38 |
|---|---|---|---|
| `heilmeier.yaml` | universal_baseline | No | Unknown |
| `nih_r01.yaml` | federal_grant | Likely | Unknown |
| `nih_r21.yaml` | federal_grant | Likely | Unknown |
| `nsf_xlabs.yaml` | federal_OT | Yes (via primary_artifacts) | ✅ Yes |
| `nsf_tech_labs.yaml` | federal_OT | Likely | Unknown |
| `nsf_sbir_phase1.yaml` | federal_grant | Likely | Unknown |
| `nsf_sbir_phase2.yaml` | federal_grant | Likely | Unknown |
| `nsf_sbir_phase2b.yaml` | federal_grant | Likely | Unknown |
| `arpah_solution_summary.yaml` | federal_BAA | Yes (3-page solution summary) | ✅ Yes |
| `arpah_mission_office.yaml` | federal_OT | Likely | Unknown |
| `arpah_program_iso.yaml` | federal_OT | Likely | Unknown |
| `doe_genesis.yaml` | federal_OT | Likely | Unknown |
| `astera_residency.yaml` | private_fellowship | Likely | Unknown |
| `brains_accelerator.yaml` | private_fellowship | Likely | Unknown |
| `foresight_nodes.yaml` | private_fellowship | Likely | Unknown |
| `google_impact_challenge.yaml` | private_grant | Likely | Unknown |
| `yc_nonprofit.yaml` | accelerator | Likely | Unknown |

**Missing (Tier-1 priority):** Wellcome Leap, NIH Bridge2AI, NIH PRIMED-AI, NSF Convergence Accelerator, Horizon Europe Cluster 1, ARPA-H PHO, Convergent Research FRO, CZI, Gates Grand Challenges.

**Missing (templates needed):** `corporate_credit` shared template (~7 funders), `nonprofit_discount` shared template (~20 funders), `vc_investment` shared template (~7 funders).

### 1.4 Group & Preset Inheritance System (CONVERGED but UNUSED)

`groups.yaml` defines 6 U-groups, 4 A-groups, 8 F-groups, and 11 composition presets. This is a powerful inheritance system that allows funder profiles to declare `preset: preset_federal_OT` instead of listing every slot.

**Status:** Fully designed but not yet adopted. All 17 existing funder YAMLs still use explicit slot lists. Migration to preset shorthand is deferred to v1.3.

### 1.5 Opportunity Mapping (CONVERGED)

`opportunity_mapping.yaml` contains 71 detailed opportunity blocks with all 30+ F-fields, required/useful slot lists, and submission notes. `opportunity_mapping.csv` is the flat tabular equivalent, loadable into Monday via CSV import.

**This is the most complete artifact in the entire system.** 71 opportunities, each with 30+ metadata fields, slot citations, and sub-slot specifics.

---

## 2. Pipeline Code — Findings & Status

### 2.1 Parser (`parser.py`) — ✅ PRODUCTION

**Lines:** 601 | **Status:** Fully functional

The parser handles PDF, DOCX, and XLSX ingestion using PyMuPDF as the primary engine. Key capabilities:
- **CriticMarkup annotation extraction**: Reads PDF highlights, strikeouts, underlines, and injects them as `{==highlight==}`, `{--deletion--}`, `{++insertion++}` directly into the markdown output.
- **Table extraction**: Generates separate `_tables.md` files with markdown tables.
- **Metadata extraction**: Generates `_metadata.json` files with document properties.
- **GROBID fallback**: For academic papers, uses GROBID for section/citation boundary detection.

**Verified working:** Successfully parsed 21 PDFs from `data/raw/papers/` and all grant documents across 4 funder directories. Running via `nox -s parse_papers` and `nox -s parse_grants`.

### 2.2 Extractor (`extractor.py`) — ✅ PRODUCTION (with caveats)

**Lines:** 192 | **Status:** Functional but model-limited

Uses `instructor` library with Pydantic validation to constrain LLM output to the `GrantInfo` schema. Successfully extracted structured JSON for NSF X-Labs documents.

**Key findings from production run:**
- **Llama 3.1 8B struggles** with the nested `GrantInfo` schema. It frequently outputs `$ref` dictionary syntax instead of arrays, triggering Pydantic validation errors and instructor retry loops.
- **Timeout was too short:** Original 120s timeout caused silent failures. Increased to 600s.
- **`use_mmap: False`** is critical for GPU offloading on Strix Halo hardware.
- **47 minutes** for 4 NSF documents (should be <5 minutes with Nemotron-70B).

**Extraction outputs generated:**
| File | Quality |
|---|---|
| `nsf-topic2-fy26-xlabssensingandimaging.json` | ✅ High (deadlines, phases, requirements extracted correctly) |
| `nsf-otaso-fy26-xlabsinitiative.json` | ⚠️ Low (empty arrays for deadlines, contacts, requirements after retry exhaustion) |
| `nsf-otaso-fy26-xlabsinitiative_criticmarkup.json` | ✅ Good (eligibility, funding, phases extracted) |
| `xlabs_initial_submission_template.json` | ✅ Good (template structure extracted) |

### 2.3 Registry (`registry.py`) — ✅ PRODUCTION

**Lines:** 601 | **Status:** Fully functional

Comprehensive registry system with:
- `GrantTemplateRegistry` — loads manifest, lazily resolves funder profiles and templates
- `FunderProfile` — 16-field dataclass mapping F-fields to typed attributes
- `GrantTemplate` — full template definition with sections, fields, validation rules
- `validate_submission()` — checks required slots, page limits, useful-slot warnings

**Well-designed:** The registry correctly uses lazy loading with caches, handles both `template_definition` and `primary_artifacts` fallback formats, and provides a clean public API.

### 2.4 Harmonizer (`harmonizer.py`) — ⚠️ SCAFFOLDED

**Lines:** 133 | **Status:** Placeholder logic only

The harmonizer is architecturally sound (it takes extracted `GrantInfo` and maps it to canonical `CanonicalSection` objects with slot IDs) but **every section is filled with placeholder text** (`"Placeholder mapped content for {section.id}"`).

**What's missing:** The actual semantic mapping logic. The harmonizer needs to either:
1. Use an LLM to map each section of raw text to the correct canonical slot, or
2. Use rule-based heuristics (heading matching, keyword extraction) for deterministic mapping.

### 2.5 Generator (`generator.py`) — ⚠️ SCAFFOLDED

**Lines:** 130 | **Status:** LLM-based scaffold generation works, but lacks real templates

The generator uses `instructor` to create submission scaffolds from funder profiles. It works end-to-end but produces generic outlines rather than real proposal content.

**What's missing:**
- Real Jinja2 templates for each funder (only `nsf_xlabs.md` exists in `templates/`)
- Integration with authored slot content from `slots/` directory
- Context injection from `GrantInfo` extractions

### 2.6 Renderer (`render.py`) — ⚠️ SCAFFOLDED

**Lines:** 90 | **Status:** Jinja2 rendering works, Pandoc/Quarto not wired

The renderer provides `TemplateRenderer` with `render_template()` and `render_from_string()` methods. It correctly initializes a Jinja2 environment with autoescaping and block trimming.

**What's missing:**
- No Pandoc subprocess integration for PDF/DOCX compilation
- No Quarto project configuration
- No Google Docs API integration (deferred per README)
- `compile_document` nox session exists but lacks wiring to this module

---

## 3. Data Assets — Inventory

### 3.1 Staged Grant Documents

| Funder | Directory | Files | Parsed | Extracted | Harmonized |
|---|---|---|---|---|---|
| **NSF X-Labs** | `data/staged/grants/nsf_xlabs/` | 16 | ✅ All | ✅ 4 JSONs | ❌ |
| **ARPA-H Delphi** | `data/staged/grants/arpah/programs/delphi/` | 8 | ✅ All | ❌ | ❌ |
| **ARPA-H EVIDENT TA1-3** | `data/staged/grants/arpah/programs/evident/ta1_3/` | 6 | ✅ All | ❌ | ❌ |
| **ARPA-H EVIDENT TA4** | `data/staged/grants/arpah/programs/evident/ta4/` | 16 | ✅ All | ❌ | ❌ |
| **ARPA-H PROSPR** | `data/staged/grants/arpah/programs/prospr/` | 8 | ✅ All | ❌ | ❌ |
| **ARPA-H Mission Office ISOs** | `data/staged/grants/arpah/mission_office_isos/` | 4 | ✅ All | ❌ | ❌ |
| **ARPA-H Templates** | `data/staged/grants/arpah/templates/` | 15 | ✅ All | N/A | N/A |
| **NSF Tech Labs** | `data/staged/grants/nsf_tech_labs/` | 6 | ✅ All | ❌ | ❌ |
| **DOE Genesis** | `data/staged/grants/doe_genesis/` | 6 | ✅ All | ❌ | ❌ |

**Total files across all funders:** 105

### 3.2 ARPA-H Submission Templates (High Value)

These are the actual submission template documents from ARPA-H, parsed into markdown:
- `arpah_solution_summary_template.md` (3-page Solution Summary)
- `arpah_solution_summary_content.md` (Content guide)
- `arpah_solution_summary_template.yaml` (Structured YAML template definition)
- `arpa-h_tdd_task_description_document_-_ots.md`
- `arpa-h_tech_management_proposal_-_ots.md`
- `arpa-h_cost_proposal_ots.md`
- `arpa-h_cost_proposal_workbook_-_ots.md` (1.2MB budget workbook)
- `arpa-h_admin-national-policy-document-ots-amend_2.md`

### 3.3 NSF X-Labs Templates

- `xlabs_initial_submission_template.md` (8-page Written Proposal)
- `xlabs_initial_submission_content.md` (Content guide)
- `NSF_XLabs_Consolidated_Reference.md` (Merged reference document from 3 NSF docs)

---

## 4. CLI & Nox Orchestration

### 4.1 CLI Commands (`cytos grants ...`)

| Command | Implementation | Status |
|---|---|---|
| `cytos grants parse <dir>` | `GrantDocumentParser` | ✅ Working |
| `cytos grants extract <dir> [--funder]` | `GrantInfoExtractor` + `LLMConfig` | ✅ Working |
| `cytos grants harmonize <dir> --funder <id>` | `GrantDocumentHarmonizer` | ⚠️ Placeholder |
| `cytos grants generate <funder_id>` | `GrantMaterialGenerator` | ⚠️ Scaffolded |
| `cytos grants registry list` | `GrantTemplateRegistry.list_funders()` | ✅ Working |
| `cytos grants registry show <id>` | `GrantTemplateRegistry.get_funder()` | ✅ Working |
| `cytos scholarly parse-papers <dir>` | `GROBIDParser` | ✅ Working |

### 4.2 Nox Sessions

| Session | Command | Status |
|---|---|---|
| `parse_grants` | `cytos grants parse` on archive input | ✅ Working |
| `parse_papers` | `cytos scholarly parse-papers` on `data/raw/papers` | ✅ Working |
| `extract_grants` | `cytos grants extract` on all staged grants | ✅ Working |
| `extract_nsf_xlabs` | `cytos grants extract` on NSF X-Labs only | ✅ Working |
| `compile_document` | `cytos grants compile` with Pandoc | ⚠️ Exists, not wired |
| `harmonize` | `cytos grants harmonize` | ⚠️ Placeholder |

---

## 5. Test Coverage — Current State

**There are ZERO dedicated tests for the grant pipeline.** No files under `tests/` reference `grant`, `extractor`, `harmonizer`, `registry`, or any grants module. This is the single biggest risk in the system.

The only validation that exists is:
1. Structural verification of slot files (mentioned in CHANGELOG v1.0: "7 cross-consistency blockers fixed")
2. The `validate_submission()` method in `registry.py` (runtime, not tested)

---

## 6. Gap Analysis — What Is Missing

### 6.1 Critical Gaps (Blocking End-to-End Flow)

| Gap | Impact | Effort |
|---|---|---|
| **Harmonizer semantic mapping** | Blocks slot-aware proposal generation | High (LLM integration) |
| **Renderer Pandoc/Quarto wiring** | Blocks PDF/DOCX output | Medium |
| **Funder-specific Jinja2 templates** | Only NSF X-Labs exists | Medium per funder |
| **Unit tests for all 6 modules** | No safety net for refactoring | High (comprehensive) |
| **Nemotron-70B model switch** | Extraction quality + speed | Low (reboot + config change) |

### 6.2 Important Gaps (Needed for Production)

| Gap | Impact | Effort |
|---|---|---|
| **UMLS/SnomedCT semantic tagging** | Blocks accurate medical term matching | High |
| **Monday.com board sync** | Manual board updates required | Medium |
| **Funding opportunity scraper** | Manual discovery of new opportunities | High |
| **Slot prose authoring** | 23/27 slots are stubs | High (content work) |
| **Preset migration** | 17 funder YAMLs use verbose explicit lists | Low |
| **Schema validators** (`lib/validators/`) | No automated consistency checking | Medium |

### 6.3 Nice-to-Have Gaps

| Gap | Impact | Effort |
|---|---|---|
| **Google Docs renderer** | Views in Workspace | High |
| **XLSX budget auto-fill** | Budget template automation | Medium |
| **15 Tier-2 funder profiles** | Long-tail coverage | Low per funder |
| **Lightweight templates** (corporate_credit, nonprofit_discount, vc_investment) | Covers ~34 opportunities | Low |

---

## 7. Key Design Decisions (Documented for Future Reference)

1. **Slot IDs are immutable.** Never renumber. New slots get appended (U23, U24...).
2. **No funder-specific prose in slot files.** Funder framing lives in YAML `heading:` text.
3. **Source-of-truth stays in git.** Google Docs renders are views, not sources.
4. **Author at longest funder limit; trim at render time.**
5. **F-fields describe the opportunity, not the proposal.** They live on funder YAMLs and Monday boards, not in slot files.
6. **Pydantic schemas in `extractor.py` are the LLM contract.** The `GrantInfo` model defines what the LLM must produce. Any schema change here requires re-extraction of all documents.
7. **`instructor` library provides retry + validation loop.** The LLM is retried automatically when output fails Pydantic validation. This is powerful but model-dependent (Llama 3.1 8B struggles; Nemotron-70B should be reliable).
