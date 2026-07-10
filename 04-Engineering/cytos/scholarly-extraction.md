# Scholarly Extraction & Grant Harmonization Pipeline

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: engineers
> **Tags**: `engineering`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

The `src/cytos/scholarly/grants/` subpackage processes unstructured grant documents (PDFs, DOCX, XLSX) and transforms them into standardized, structured data ready for proposal generation.

## 1. Parsing (`parser.py` & `grobid.py`)
- **PyMuPDF**: Used as the primary engine for high-fidelity text and table extraction. It specifically extracts annotations (Highlight, StrikeOut, etc.) and seamlessly injects them directly into the generated markdown using CriticMarkup syntax (`{==highlight==}`).
- **GROBID**: Used as a fallback or parallel extraction engine specifically geared toward academic papers, providing strong section and citation boundary detection.

## 2. LLM Structured Extraction (`llm_extraction.py`)
Once a raw Markdown representation is created, `llm_extraction.py` uses `Instructor` to interface with local or remote language models (e.g., Ollama or OpenAI).
- Using **Pydantic Validation**, the LLM is constrained to output exactly the sections, requirements, and metadata required by our internal `GrantInfo` schema.
- This ensures JSON-schema compliance regardless of the model chosen.

## 3. Harmonization (`harmonizer.py`)
Raw extracted structures are mapped into the canonical "Proposal Slots" system (`U01`, `U02`, etc.) based on funder-specific declarative schemas (e.g., `nsf_xlabs.yaml` or `arpah_solution_summary.yaml`).
- NSF's "Intellectual Merit" and ARPA-H's "Technical Approach" both map seamlessly to `U02_TECHNICAL_APPROACH`.

## 4. Document Compilation (`generator.py` & `compiler.py`)
- **Generator**: Uses Jinja2 to render the harmonized data back into Funder-specific templates (e.g., `nsf_xlabs.md`).
- **Compiler**: Uses Pandoc and Quarto to compile the final rendered markdown into target formats (PDF, DOCX) automatically.

### Running the Pipeline
You can trigger the pipeline end-to-end via Nox:
```bash
nox -s parse_papers          # Bulk parse all documents in a directory
nox -s extract_nsf_xlabs     # Extract structured data using Ollama
nox -s compile_document      # Compile generated markdown to DOCX/PDF
```
