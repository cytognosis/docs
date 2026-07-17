# Grant Pipeline — Component Status Matrix

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: leadership, grant team
> **Tags**: `funding`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

**Last updated:** 2026-05-24

## Pipeline Modules

| Component | File | Lines | Status | Notes |
|---|---|---:|---|---|
| **Parser** | `parser.py` | 601 | ✅ Production | PyMuPDF + GROBID. CriticMarkup, tables, annotations. 39 docs processed. |
| **Extractor** | `extractor.py` | 192 | ✅ Production | instructor + Pydantic. Works with Llama 3.1; needs Nemotron for quality. |
| **Registry** | `registry.py` | 601 | ✅ Production | Manifest loading, funder profiles, template parsing, submission validation. |
| **Harmonizer** | `harmonizer.py` | 133 | ⚠️ Scaffolded | Architecture sound; slot mapping uses placeholder text, not real LLM/rule logic. |
| **Generator** | `generator.py` | 130 | ⚠️ Scaffolded | LLM scaffold gen works but produces generic outlines, not real proposals. |
| **Renderer** | `render.py` | 90 | ⚠️ Scaffolded | Jinja2 works. No Pandoc/Quarto subprocess. No Google Docs API. |

## Schema Assets

| Asset | File | Status | Coverage |
|---|---|---|---|
| **Manifest** | `manifest.yaml` | ✅ v1.2 | 27 slots, 10 funders, 38 F-fields, 12 kinds |
| **Groups/Presets** | `groups.yaml` | ✅ v1.0 | 6 U-groups, 4 A-groups, 8 F-groups, 11 presets |
| **Opportunity Map** | `opportunity_mapping.yaml` | ✅ v1.1 | 71 opportunities × 30+ F-fields |
| **Opportunity CSV** | `opportunity_mapping.csv` | ✅ Exists | Monday-importable flat table |
| **Slot Files** | `slots/*.md` | ⚠️ Partial | 27 files; 4 authored (U01, U03p, U06p, U08), 23 stubs |
| **Funder Profiles** | `funders/*.yaml` | ⚠️ Partial | 10 files exist; Tier-1 priority funders missing |
| **Schema README** | `README.md` | ✅ Complete | Directory layout, coverage snapshot, next steps |
| **Schema INDEX** | `INDEX.md` | ✅ Complete | Full orientation map with metrics |
| **Schema CHANGELOG** | `CHANGELOG.md` | ✅ Complete | v1.0 → v1.1 → v1.2 history |

## Funder Profile Coverage

| Funder | YAML File | Kind | Template Def | F31–F38 | Extraction Run |
|---|---|---|---|---|---|
| Heilmeier (baseline) | ✅ | universal_baseline | — | ❓ | — |
| NIH R01 | ✅ | federal_grant | ❓ | ❓ | ❌ |
| NIH R21 | ✅ | federal_grant | ❓ | ❓ | ❌ |
| NSF X-Labs | ✅ | federal_OT | ✅ | ✅ | ✅ |
| NSF Tech Labs | ✅ | federal_OT | ❓ | ❓ | ❌ |
| NSF SBIR Phase I | ✅ | federal_grant | ❓ | ❓ | ❌ |
| NSF SBIR Phase II | ✅ | federal_grant | ❓ | ❓ | ❌ |
| NSF SBIR Phase IIB | ✅ | federal_grant | ❓ | ❓ | ❌ |
| ARPA-H Solution Summary | ✅ | federal_BAA | ✅ | ✅ | ❌ |
| ARPA-H Mission Office | ✅ | federal_OT | ❓ | ❓ | ❌ |
| ARPA-H Program ISO | ✅ | federal_OT | ❓ | ❓ | ❌ |
| DOE Genesis | ✅ | federal_OT | ❓ | ❓ | ❌ |
| Astera Residency | ✅ | private_fellowship | ❓ | ❓ | ❌ |
| Brains Accelerator | ✅ | private_fellowship | ❓ | ❓ | ❌ |
| Foresight Nodes | ✅ | private_fellowship | ❓ | ❓ | ❌ |
| Google Impact Challenge | ✅ | private_grant | ❓ | ❓ | ❌ |
| YC Nonprofit | ✅ | accelerator | ❓ | ❓ | ❌ |

### Missing Funder Profiles (Tier-1 Priority)

| Funder | Kind | Why Priority |
|---|---|---|
| Wellcome Leap | philanthropic_grant_proactive | Active engagement |
| NIH Bridge2AI | federal_grant | Data science focus |
| NIH PRIMED-AI | federal_grant | Precision medicine |
| NSF Convergence Accelerator | federal_OT | Platform tech |
| Horizon Europe Cluster 1 | intergovernmental_grant | Health research |
| ARPA-H PHO | federal_OT | Companion to HSF |
| Convergent Research FRO | private_fellowship | Perfect fit for Cytognosis |
| CZI | private_grant | Single-cell focus |
| Gates Grand Challenges | philanthropic_grant_proactive | Global health |

## Data Asset Status

| Funder Directory | Files | Parsed | Tables | CriticMarkup | Annotations | Extracted | Harmonized |
|---|---:|---|---|---|---|---|---|
| ARPA-H (all) | 63 | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ |
| NSF X-Labs | 16 | ✅ | ✅ | ✅ | ✅ | ✅ (4 JSONs) | ❌ |
| NSF Tech Labs | 10 | ✅ | ✅ | ✅ | ✅ | ❌ | ❌ |
| DOE Genesis | 10 | ✅ | ✅ | — | — | ❌ | ❌ |

## CLI & Nox Coverage

| Command / Session | Implemented | Tested | Notes |
|---|---|---|---|
| `cytos grants parse` / `nox -s parse_grants` | ✅ | ❌ | 39 docs processed successfully |
| `cytos scholarly parse-papers` / `nox -s parse_papers` | ✅ | ❌ | 21 papers parsed via GROBID |
| `cytos grants extract` / `nox -s extract_grants` | ✅ | ❌ | Works with Llama 3.1 |
| `nox -s extract_nsf_xlabs` | ✅ | ❌ | 47-minute run, 4 JSONs produced |
| `cytos grants harmonize` / `nox -s harmonize` | ⚠️ | ❌ | Placeholder logic |
| `cytos grants generate` / `nox -s generate_*` | ⚠️ | ❌ | LLM scaffold only |
| `nox -s compile_document` | ⚠️ | ❌ | Exists but not wired to render.py |
| `cytos grants registry list` | ✅ | ❌ | Works |
| `cytos grants registry show` | ✅ | ❌ | Works |

## Test Coverage

| Module | Unit Tests | Integration Tests | Pressure Tests |
|---|---|---|---|
| parser.py | ❌ | ❌ | ❌ |
| extractor.py | ❌ | ❌ | ❌ |
| registry.py | ❌ | ❌ | ❌ |
| harmonizer.py | ❌ | ❌ | ❌ |
| generator.py | ❌ | ❌ | ❌ |
| render.py | ❌ | ❌ | ❌ |
