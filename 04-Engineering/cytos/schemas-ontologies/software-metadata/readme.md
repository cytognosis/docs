# Research Software Metadata Standards Documentation

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: engineers
> **Tags**: `engineering`
> **Variants**: Technical (this doc) - Readable (readme.md in Obsidian vault: 04-Engineering/cytos/schemas-ontologies/software-metadata/) - Agent (n/a)

Complete reference materials for implementing a unified LinkML schema for CodeRepository and Software entities based on CodeMeta, CFF, Schema.org, Zenodo, and Software Heritage standards.

**Research Date**: April 4, 2026
**Status**: Complete and ready for LinkML implementation

---

## Documents Included

### 1. **QUICK_REFERENCE.md** (Start Here!)
**Best for**: Quick lookups, rapid development, one-page checklists

**Contents**:
- What each standard does (quick comparison table)
- Essential fields (top 10)
- Extended fields by category
- Field availability matrix
- Quick conversion guide
- Common SPDX licenses
- Development status values
- Semantic versioning format
- Nested object structures
- Validation checklist
- Common mistakes to avoid
- One-minute metadata checklist
- Quick lookup: field → standards mapping

**Use when**: You need a quick answer without detailed context

**Length**: ~400 lines (reference)

---

### 2. **RESEARCH_SUMMARY.md** (Executive Overview)
**Best for**: Understanding the big picture, decision-making, project planning

**Contents**:
- Overview of all 5 standards analyzed
- Key findings and coverage matrix
- Field inventory results by category
- Recommended minimal field sets (3 tiers)
- Critical standards alignment (FAIR, RSMD)
- Recommendations for LinkML implementation
- Next steps for implementation
- Conclusion and strategic recommendations

**Use when**: You need to understand scope, coverage, and strategic direction

**Length**: ~200 lines (summary)

---

### 3. **research_software_metadata_standards.md** (Comprehensive Reference)
**Best for**: In-depth understanding, detailed field definitions, implementation reference

**Contents**:

#### CodeMeta Analysis
- 50+ properties organized by functional category
- Schema.org Person/Organization/Role terms
- Review and special properties
- Complete field table with descriptions

#### CFF Analysis
- 21 core fields with validation patterns
- Person and entity object structure
- Required vs. optional fields
- Valid fields summary

#### Software Heritage Analysis
- Data model and artifact types
- Intrinsic vs. extrinsic metadata
- Preservation and indexing approach
- Metadata translation and archival

#### Schema.org SoftwareSourceCode and SoftwareApplication
- Property inheritance structure
- Key distinctions between types
- Notable software-specific properties

#### Zenodo Metadata
- Required and recommended fields
- Software deposit workflow
- DOI and persistent identifier system
- GitHub integration

#### Mapping Matrix
- 6x6 table showing field coverage across standards
- Interoperability analysis

#### LinkML Design Guidance
- Recommended field selections (minimal, standard, complete, archive)
- Key field coverage by use case

**Use when**: You need authoritative definitions and comprehensive reference material

**Length**: ~800 lines (extensive reference)

---

### 4. **codemeta_field_examples.md** (Technical Implementation Guide)
**Best for**: Code examples, JSON-LD/YAML samples, object structure definitions

**Contents**:

#### CodeMeta JSON-LD Example
- Full production-ready example with 40+ fields populated
- Real-world climate science software example
- All object types demonstrated
- Proper nesting and cardinality

#### CFF Example (Complete)
- Full CITATION.cff with YAML structure
- Extended person object with all fields
- Preferred citation definition
- Multiple author/contributor examples
- References array with varied types

#### Field-by-Field Mapping Tables
- Essential properties (CodeMeta)
- Recommended properties (CodeMeta)
- Optional but valuable properties

#### Object Structure Definitions
- Person (minimal, standard, extended)
- ComputerLanguage
- SoftwareSourceCode (as dependency)
- ScholarlyArticle (as reference)
- Organization
- Review

#### Conversion Pathways
- CodeMeta JSON-LD → CFF mapping
- CFF → CodeMeta mapping
- Tool recommendations

#### SPDX License Identifiers
- Common licenses with descriptions
- Reference to official list

#### Semantic Versioning
- Format and examples
- Pre-release and build metadata

#### CI/CD and Testing Examples
- URL patterns for CI services
- Test framework references
- Build system examples

#### Related Objects
- Supporting dataset structure
- Related publication structure

**Use when**: You're writing actual JSON-LD, YAML, or implementing object structures

**Length**: ~600 lines (code-heavy)

---

### 5. **linkml_software_schema_fields.md** (Implementation Inventory)
**Best for**: LinkML schema design, field inventory, validation patterns

**Contents**:

#### Complete Field Inventory (127 fields total)
Organized by 12 categories:
1. Identification & Naming (10 fields)
2. Versioning & Temporal (13 fields)
3. Authorship & Attribution (14 fields)
4. Technical Specifications (13 fields)
5. Repository & Distribution (8 fields)
6. Build, Testing & CI/CD (8 fields)
7. Licensing & Rights (5 fields)
8. Citations & References (10 fields)
9. Relationships & Hierarchies (9 fields)
10. Content & Documentation (6 fields)
11. Specialized (SWH/Provenance) (10 fields)
12. Zenodo-Specific (9 fields)

Each field entry includes:
- ID and type
- Required/optional flag
- Description
- Source standards
- Examples
- Validation patterns (where applicable)

#### Object Structure Definitions (YAML-ready)
- Person with full contact fields
- Organization with ROR ID
- ComputerLanguage
- SoftwareSourceCode
- Citation with flexible structure

#### Recommended Field Selection by Use Case
- Minimal (11 fields) - repository-only
- Standard (24 fields) - research software
- Complete (47+ fields) - archive/registry
- Archive & Preservation (58+ fields) - Software Heritage

#### LinkML Implementation Tips
- Enumeration patterns (DevelopmentStatus, License, etc.)
- Reusable class definitions
- Inheritance hierarchy recommendations
- Slot organization for shared patterns
- Validation patterns with regex
- Cross-standard mapping tables

**Use when**: Building the actual LinkML schema

**Length**: ~800 lines (schema-focused)

---

## Quick Navigation Guide

### By Use Case

**"I'm implementing a minimal software schema"**
→ Read: QUICK_REFERENCE.md (11 fields) + linkml_software_schema_fields.md (Minimal section)

**"I'm building research software metadata"**
→ Read: RESEARCH_SUMMARY.md + linkml_software_schema_fields.md (Standard section) + codemeta_field_examples.md

**"I'm designing a comprehensive archive system"**
→ Read: research_software_metadata_standards.md + linkml_software_schema_fields.md (Complete section) + codemeta_field_examples.md

**"I need to implement CodeMeta in my system"**
→ Read: QUICK_REFERENCE.md + codemeta_field_examples.md + research_software_metadata_standards.md (CodeMeta section)

**"I need to convert between CFF and CodeMeta"**
→ Read: codemeta_field_examples.md (Conversion Pathways section) + QUICK_REFERENCE.md (Conversion tables)

**"I need to understand Zenodo software metadata"**
→ Read: research_software_metadata_standards.md (Zenodo section) + QUICK_REFERENCE.md (Zenodo table)

**"I want to preserve software with Software Heritage"**
→ Read: research_software_metadata_standards.md (Software Heritage section) + linkml_software_schema_fields.md (Specialized fields)

### By Depth

**Quick (5 minutes)**
1. QUICK_REFERENCE.md - Essential Fields section
2. One-Minute Checklist at end of QUICK_REFERENCE.md

**Medium (30 minutes)**
1. QUICK_REFERENCE.md (entire document)
2. RESEARCH_SUMMARY.md (Overview + Findings)

**Deep (2-3 hours)**
1. RESEARCH_SUMMARY.md (complete)
2. research_software_metadata_standards.md (complete)
3. linkml_software_schema_fields.md (complete field inventory)

**Implementation (8+ hours)**
1. All of the above
2. codemeta_field_examples.md (all code examples)
3. Build LinkML schema with linkml_software_schema_fields.md as reference

### By Standard

**CodeMeta**
- Overview: RESEARCH_SUMMARY.md (CodeMeta section)
- Details: research_software_metadata_standards.md (Section 1)
- Examples: codemeta_field_examples.md (Sections 1-7)
- Quick ref: QUICK_REFERENCE.md (CodeMeta section)

**CFF**
- Overview: RESEARCH_SUMMARY.md (CFF section)
- Details: research_software_metadata_standards.md (Section 2)
- Examples: codemeta_field_examples.md (Section 2)
- Quick ref: QUICK_REFERENCE.md (CFF mapping)

**Schema.org**
- Overview: RESEARCH_SUMMARY.md (Schema.org section)
- Details: research_software_metadata_standards.md (Section 4)
- Quick ref: QUICK_REFERENCE.md (field matrix)

**Zenodo**
- Overview: RESEARCH_SUMMARY.md (Zenodo section)
- Details: research_software_metadata_standards.md (Section 5)
- Quick ref: QUICK_REFERENCE.md (Zenodo conversion)

**Software Heritage**
- Overview: RESEARCH_SUMMARY.md (SWH section)
- Details: research_software_metadata_standards.md (Section 3)
- Field ref: linkml_software_schema_fields.md (Specialized fields)

---

## Standards Analyzed

### 1. CodeMeta
- **Focus**: Software metadata vocabulary
- **Format**: JSON-LD
- **Fields**: 50+ properties
- **Key Use**: Registry indexing, discovery, interoperability
- **URL**: https://codemeta.github.io/

### 2. CITATION.cff
- **Focus**: Software citation
- **Format**: YAML 1.2
- **Fields**: 21 core fields
- **Key Use**: Human-readable, version-control-friendly, GitHub native
- **URL**: https://citation-file-format.github.io/

### 3. Schema.org
- **Focus**: Semantic web markup
- **Format**: JSON-LD, Microdata, RDFa
- **Fields**: 50+ inherited from CreativeWork
- **Key Use**: SEO, web indexing
- **URL**: https://schema.org/SoftwareSourceCode

### 4. Zenodo
- **Focus**: Research data & software archival
- **Format**: JSON metadata
- **Fields**: 40+ (CodeMeta-based)
- **Key Use**: DOI assignment, institutional archiving
- **URL**: https://zenodo.org/

### 5. Software Heritage
- **Focus**: Source code preservation
- **Format**: Proprietary + CodeMeta mapping
- **Fields**: 25+ (custom provenance model)
- **Key Use**: Long-term archival, provenance, immutable storage
- **URL**: https://softwareheritage.org/

---

## Key Statistics

| Metric | Value |
|---|---|
| Total fields analyzed | 127 |
| CodeMeta properties | 50+ |
| CFF fields | 21 |
| Standards compared | 5 |
| Cross-standard mappings | 12+ |
| Object types defined | 8 |
| Use case tiers | 4 |
| Document pages | 2000+ |

---

## Standards Alignment

### Interoperability
- **Strong**: CodeMeta ↔ CFF ↔ Schema.org
- **Partial**: Software Heritage (maintains parallel model)
- **Integration**: Zenodo (native CFF/CodeMeta support)

### FAIR Principles
- **Findable**: Keywords, identifiers, classification
- **Accessible**: URL, download, access control
- **Interoperable**: Standard formats (JSON-LD, YAML)
- **Reusable**: License, documentation, requirements

### RSMD Guidelines
- CodeMeta recommended for all requirements (RSMD 1.5, 4.1-4.4, 5.1)
- Supports research software metadata best practices
- Enables FAIR software implementations

---

## Next Steps for Implementation

1. **Select use case tier** (minimal/standard/complete/archive)
2. **Review linkml_software_schema_fields.md** for field inventory
3. **Define class hierarchy** (Software, CodeRepository, etc.)
4. **Create slots** for shared patterns
5. **Implement enumerations** (DevelopmentStatus, License, etc.)
6. **Build Person/Organization** objects
7. **Add validation rules** (versioning, URLs, SPDX)
8. **Create serializers** for CFF/CodeMeta export
9. **Build validator** against standard constraints
10. **Test with real software** (numpy, scipy, GDAL)

---

## Document Statistics

| Document | Lines | Words | Focus |
|---|---|---|---|
| QUICK_REFERENCE.md | ~400 | ~3000 | Quick lookups, checklists |
| RESEARCH_SUMMARY.md | ~200 | ~2500 | Strategic overview |
| research_software_metadata_standards.md | ~800 | ~8000 | Comprehensive reference |
| codemeta_field_examples.md | ~600 | ~5000 | Code examples |
| linkml_software_schema_fields.md | ~800 | ~7000 | Schema implementation |
| **Total** | **~2800** | **~25500** | Complete package |

---

## Standards References

- CodeMeta Project: https://codemeta.github.io/
- Citation File Format: https://citation-file-format.github.io/
- Schema.org: https://schema.org/
- Zenodo: https://zenodo.org/
- Software Heritage: https://softwareheritage.org/

## Related Standards

- FAIR Principles: https://www.go-fair.org/fair-principles/
- RSMD Guidelines: https://fair-impact.github.io/RSMD-guidelines/
- SPDX Licenses: https://spdx.org/licenses/
- Repostatus: http://www.repostatus.org/
- LinkML: https://linkml.io/

---

## How to Use These Documents

### For Developers
1. Start with QUICK_REFERENCE.md for overview
2. Use codemeta_field_examples.md for implementation patterns
3. Reference linkml_software_schema_fields.md for field definitions

### For Project Managers
1. Read RESEARCH_SUMMARY.md for strategic context
2. Reference field selection recommendations
3. Understand interoperability landscape

### For Data Scientists
1. Use QUICK_REFERENCE.md for field lookup
2. Reference research_software_metadata_standards.md for details
3. Apply citation best practices from codemeta_field_examples.md

### For Standards Implementers
1. Start with research_software_metadata_standards.md
2. Deep dive into specific standards with referenced sources
3. Use linkml_software_schema_fields.md for comprehensive inventory
4. Reference mapping tables for cross-standard translation

---

## Maintenance & Updates

**Last Updated**: April 4, 2026
**Version**: 1.0 - Complete Research Package
**Status**: Ready for LinkML implementation

### To Update
- Monitor: https://codemeta.github.io/, https://citation-file-format.github.io/
- Review: GitHub repositories for schema changes
- Track: Software Heritage and Zenodo updates

---

## Questions?

Refer to:
1. **Quick answer?** → QUICK_REFERENCE.md
2. **How does X work?** → QUICK_REFERENCE.md (field lookup) or research_software_metadata_standards.md
3. **Show me an example** → codemeta_field_examples.md
4. **I'm building a schema** → linkml_software_schema_fields.md
5. **What's the strategy?** → RESEARCH_SUMMARY.md

---

## Document Organization

```
📁 Research Software Metadata Standards
├── 📄 README.md (this file)
├── 📄 QUICK_REFERENCE.md (⭐ START HERE)
├── 📄 RESEARCH_SUMMARY.md (Executive overview)
├── 📄 research_software_metadata_standards.md (Comprehensive reference)
├── 📄 codemeta_field_examples.md (Code examples)
└── 📄 linkml_software_schema_fields.md (Implementation inventory)
```

---

**Created**: April 4, 2026
**For**: LinkML schema development for research software and code repositories
**Coverage**: 5 major metadata standards (CodeMeta, CFF, Schema.org, Zenodo, Software Heritage)
**Total Content**: 2800+ lines, 25,500+ words, 127 fields analyzed
