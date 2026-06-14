# Grant Pipeline — Architecture & Data Flow

## End-to-End Pipeline

```mermaid
graph TD
    subgraph "Stage 1: Ingestion"
        A[("Raw Documents<br/>(PDF, DOCX, XLSX)")] --> B["parser.py<br/>GrantDocumentParser"]
        B --> C[("Staged Markdown<br/>+ _tables.md<br/>+ _metadata.json<br/>+ _annotations.json<br/>+ _criticmarkup.md")]
    end

    subgraph "Stage 2: Extraction"
        C --> D["extractor.py<br/>GrantInfoExtractor"]
        D -->|"instructor + Pydantic"| E[("Structured JSON<br/>(GrantInfo schema)")]
        F["LLM Backend<br/>(Ollama: llama3.1 / nemotron)"] -.->|"API"| D
    end

    subgraph "Stage 3: Harmonization"
        E --> G["harmonizer.py<br/>GrantDocumentHarmonizer"]
        H[("Funder YAML<br/>(schemas/funders/)")] --> G
        I[("Slot Files<br/>(schemas/slots/)")] --> G
        G --> J[("HarmonizedGrant<br/>(CanonicalSection[])")]
    end

    subgraph "Stage 4: Generation"
        J --> K["generator.py<br/>GrantMaterialGenerator"]
        L[("Jinja2 Templates<br/>(templates/)")] --> K
        K --> M[("Generated Scaffold<br/>(Markdown)")]
    end

    subgraph "Stage 5: Rendering"
        M --> N["render.py<br/>TemplateRenderer"]
        N -->|Pandoc/Quarto| O[("PDF / DOCX")]
        N -->|Google Docs API| P[("Google Docs View")]
        N -->|openpyxl| Q[("XLSX Budget")]
    end

    subgraph "Schema Registry"
        R["registry.py<br/>GrantTemplateRegistry"] --> D
        R --> G
        R --> K
        S[("manifest.yaml<br/>v1.2")] --> R
        T[("groups.yaml")] --> R
        U[("opportunity_mapping.yaml<br/>71 opportunities")] -.-> R
    end

    style A fill:#5145A8,color:#fff
    style E fill:#3B7DD6,color:#fff
    style J fill:#E0309E,color:#fff
    style O fill:#14A3A3,color:#fff
    style P fill:#14A3A3,color:#fff
    style Q fill:#14A3A3,color:#fff
    style B fill:#25253D,color:#E0E0ED
    style D fill:#25253D,color:#E0E0ED
    style G fill:#25253D,color:#E0E0ED,stroke:#F26355,stroke-width:2px,stroke-dasharray: 5 5
    style K fill:#25253D,color:#E0E0ED,stroke:#F26355,stroke-width:2px,stroke-dasharray: 5 5
    style N fill:#25253D,color:#E0E0ED,stroke:#F26355,stroke-width:2px,stroke-dasharray: 5 5
```

> Dashed red borders indicate scaffolded/incomplete modules.

## Component Health

```mermaid
pie title Pipeline Stage Completion
    "Parser (100%)" : 100
    "Extractor (85%)" : 85
    "Registry (100%)" : 100
    "Harmonizer (20%)" : 20
    "Generator (30%)" : 30
    "Renderer (15%)" : 15
```

## Schema Hierarchy

```mermaid
graph LR
    subgraph "Canonical Schema (v1.2)"
        M["manifest.yaml"] --> SF["Slot Families<br/>heilmeier_core: U01-U08<br/>extensions: U09-U22<br/>administrative: A01-A05"]
        M --> FK["Funder Kinds<br/>12 types"]
        M --> FF["F-Fields<br/>F01-F38"]
    end

    subgraph "Groups & Presets"
        G["groups.yaml"] --> UG["U-Groups (6)"]
        G --> AG["A-Groups (4)"]
        G --> FG["F-Groups (8)"]
        G --> PR["Presets (11)<br/>preset_federal_grant<br/>preset_federal_OT<br/>preset_accelerator<br/>..."]
    end

    subgraph "Funder Profiles"
        FP["funders/*.yaml<br/>(17 files)"] --> RS["required_slots"]
        FP --> US["useful_slots"]
        FP --> PA["primary_artifacts<br/>(section→slot mapping)"]
        FP --> RT["render_targets"]
        FP --> FM["funder_metadata<br/>(F01-F38 values)"]
    end

    subgraph "Opportunity Mapping"
        OM["opportunity_mapping.yaml<br/>(71 entries)"] --> MF["30+ F-fields per opp"]
        OM --> SL["Slot requirements per opp"]
        OM --> MB["Monday.com board sync"]
    end

    M --> FP
    PR -.->|"inherits"| FP
    FK --> FP

    style M fill:#8B3FC7,color:#fff
    style G fill:#5145A8,color:#fff
    style FP fill:#3B7DD6,color:#fff
    style OM fill:#E0309E,color:#fff
```

## File Layout

```
src/cytos/scholarly/grants/
├── __init__.py                     # Public API (5 classes)
├── parser.py                       # Stage 1: Document ingestion (601 lines)
├── extractor.py                    # Stage 2: LLM structured extraction (192 lines)
├── harmonizer.py                   # Stage 3: Slot mapping (133 lines, SCAFFOLDED)
├── generator.py                    # Stage 4: Scaffold generation (130 lines, SCAFFOLDED)
├── render.py                       # Stage 5: Template rendering (90 lines, SCAFFOLDED)
├── registry.py                     # Registry & validation (601 lines)
├── schemas/
│   ├── manifest.yaml               # Authoritative registry (v1.2, 634 lines)
│   ├── groups.yaml                 # Preset inheritance system (v1.0)
│   ├── opportunity_mapping.yaml    # 71 opportunities × 30+ F-fields (3404 lines)
│   ├── opportunity_mapping.csv     # Flat tabular export for Monday import
│   ├── funders/                    # 17 funder YAML profiles
│   │   ├── heilmeier.yaml          # Universal baseline
│   │   ├── nsf_xlabs.yaml          # NSF X-Labs (federal_OT)
│   │   ├── arpah_solution_summary.yaml  # ARPA-H Solution Summary
│   │   ├── arpah_mission_office.yaml    # ARPA-H Mission Office ISO
│   │   ├── arpah_program_iso.yaml       # ARPA-H Program ISO
│   │   ├── ... (12 more)
│   │   └── yc_nonprofit.yaml      # YC Nonprofit (accelerator)
│   └── slots/                      # 27 canonical slot files
│       ├── U01_objective.md        # Heilmeier Q1 (AUTHORED)
│       ├── U02_sota_and_limits.md  # (stub)
│       ├── ... (25 more)
│       └── A05_intake_meta.md      # (stub)
└── templates/
    └── nsf_xlabs.md                # Only Jinja2 template that exists

data/staged/grants/
├── parse_report.json               # 39 files processed, 556 pages, 249 annotations
├── arpah/
│   ├── mission_office_isos/        # HSF + PHO amendments (6 files)
│   ├── programs/
│   │   ├── delphi/                 # Delphi ISO + appendix (9 files)
│   │   ├── evident/                # EVIDENT TA1-3 + TA4 (22 files)
│   │   └── prospr/                 # PROSPR ISO + model OT (6 files)
│   └── templates/                  # Official ARPA-H templates (15 files)
├── nsf_xlabs/
│   ├── *.md + *.json               # Solicitations + extractions (14 files)
│   └── templates/                  # NSF X-Labs templates (4 files)
├── nsf_tech_labs/                  # OT Guide + RFI + webinar (10 files)
└── doe_genesis/                    # FOA + overview + templates (10 files)
```
