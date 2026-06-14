# Yar Repo Structure Optimization

## Changes Made

### Root Cleanup

| Before | After | Rationale |
|---|---|---|
| `YarDarkLogo.jpg/png` + `YarLightLogo.jpg/png` at root | `assets/brand/` | Brand assets belong in a dedicated directory, not root |
| `Yar.zip` at root | Deleted + gitignored (`*.zip`) | Build artifact, regenerable |
| `dist/` (contained old wheel) | Deleted (already gitignored) | Build artifact |
| `logs/` (1.4MB log file) | Deleted + gitignored (`logs/`) | Runtime artifact |
| `Docs/` (capital D, 14 files) | Deleted, content already in `docs/planning/mvp/` | Replaced by normalized `docs/` |
| `submission/` (11 files) | Moved to `docs/submission/` | All docs consolidated under `docs/` |
| `refactor/` (100 working files) | Gitignored | Working/scratch directory, not part of the package |

### New Files

| File | Purpose |
|---|---|
| `src/yar/py.typed` | PEP 561 marker for type stub discovery |
| `assets/brand/` | Brand logo assets (4 files) |
| `docs/submission/` | Relocated hackathon submission docs (11 files) |

### Configuration Updates

| File | Change |
|---|---|
| `.gitignore` | Added: `logs/`, `refactor/`, `*.zip`, `*.whl` |
| `.env.example` | Added: `ANYTYPE_API_BASE_URL` with auto-discovery comment |
| `pyproject.toml` | Fixed: Documentation URL `Docs` → `docs`; added Changelog URL; added `py.typed` inclusion |
| `src/yar/web/__init__.py` | Added module docstring |

## Final Directory Tree

```
Yar/
├── .env.example                     # Environment variable template
├── .gitignore                       # Updated with new ignores
├── CHANGELOG.md                     # Version history
├── README.md                        # Project overview
├── pyproject.toml                   # Build config (hatchling)
│
├── assets/                          # Static assets
│   └── brand/                       # Logo files (jpg/png, dark/light)
│
├── CAP/                             # Communication Augmentation Protocol
│   ├── docs/                        # CAP specification (20 files)
│   ├── schemas/                     # JSON Schemas (cap-core, cap-med)
│   ├── policies/                    # Policy definitions
│   ├── cap_conformance/             # Conformance tests
│   └── ...                          # Scripts, notebooks, reference impls
│
├── docs/                            # All documentation (34 .md files)
│   ├── README.md                    # Index
│   ├── architecture/                # System design (3 files)
│   ├── integrations/                # Anytype API ref + refactor plan
│   ├── research/                    # Voice models, CAP+Yar analysis
│   ├── planning/                    # Revision plan + MVP docs (15 files)
│   └── submission/                  # Gemma hackathon materials (11 files)
│
├── examples/                        # Demo data and sample schemas
├── mobile/                          # Flutter mobile app
├── schemas/                         # JSON Schemas (Yar domain)
├── scripts/                         # Setup, demo, and verification scripts
│
├── src/yar/                         # Python backend (63 .py files)
│   ├── py.typed                     # PEP 561 marker
│   ├── __init__.py                  # Package root, version
│   ├── main.py                      # FastAPI app factory
│   ├── cli.py                       # CLI entry point
│   ├── cap_profile.py               # CAP primitives (future: cap/ subpkg)
│   ├── logging_config.py            # Structured logging
│   ├── main_dependencies.py         # DI container
│   ├── api/                         # Route modules (14 files)
│   ├── core/                        # Business logic (8 files)
│   ├── integrations/                # External service adapters
│   │   ├── anytype/                 # Anytype subpackage (11 files)
│   │   ├── linkml_loader.py         # LinkML schema loader
│   │   └── wadm_adapter.py          # W3C Web Annotation adapter
│   ├── models/                      # Pydantic models (10 files)
│   ├── prompts/                     # LLM prompt templates (3 .md files)
│   ├── storage/                     # SQLite + Graph store (2 files)
│   └── web/                         # Static web shell (HTML/CSS/JS)
│
└── tests/                           # Test suite (35 files, 162 tests)
```

## Metrics

| Metric | Count |
|---|---|
| Source files (`.py`) | 63 |
| Test files | 35 |
| Tests passing | 162/162 |
| Documentation files (`.md`) | 34 |
| Schema files (`.json`) | 4 |
| Script files | 8 |
| Root-level clutter files | 0 (was 5) |
