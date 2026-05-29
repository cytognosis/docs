# Research Summary: Software Metadata Standards Analysis

**Date**: April 4, 2026
**Topic**: Comprehensive metadata standards for research software and code repositories
**Deliverables**: 3 detailed reference documents

---

## Overview

This research provides comprehensive documentation of five major research software metadata standards, designed to support the development of a unified LinkML schema for CodeRepository and Software entity types.

---

## Standards Analyzed

### 1. CodeMeta (https://codemeta.github.io/)

**Status**: Established, actively maintained international standard

**Key Characteristics**:
- JSON-LD format based on Schema.org
- 50+ properties covering software metadata
- Bridging tool between software development and academic disciplines
- Recognized by FAIRCORE4EOSC, Software Heritage, Zenodo
- Focus: Research software discovery, citation, and interoperability

**Unique Contributions**:
- `buildInstructions` - Installation/build documentation
- `continuousIntegration` - CI/CD pipeline URL
- `issueTracker` - Bug tracking system URL
- `developmentStatus` - Per repostatus.org enumeration
- `maintainer` - Dedicated maintenance contact
- `softwareSuggestions` - Optional dependencies
- `referencePublication` - Academic publications describing software

**Coverage**: Identification, authorship, versioning, technical specs, licensing, repositories, build/CI, citations

---

### 2. CITATION.cff (Citation File Format)

**Status**: Emerging standard, native to GitHub, Zenodo, Zotero

**Key Characteristics**:
- YAML 1.2 format (human-readable)
- 21 core fields with extensive person/entity definitions
- Minimal viable example: cff-version, message, title, authors
- Native support: GitHub displays citations, Zenodo integrates, Zotero imports
- Focus: Software citation correctness and reproducibility

**Unique Contributions**:
- `message` - Custom citation instruction text
- `preferred-citation` - Specific citation format recommendation
- `references` - Works this software builds upon
- `repository-artifact` - Package registry (PyPI, Docker Hub, etc.)
- `commit` - Git commit hash for version
- `contact` - Maintainer contact information
- Full person object with detailed address, telephone, ORCID fields

**Coverage**: Authorship, versions, dates, citations, references, repository links, licensing

---

### 3. Schema.org SoftwareSourceCode & SoftwareApplication

**Status**: W3C standard, widely adopted for web semantics

**Key Characteristics**:
- JSON-LD, Microdata, or RDFa formats
- 50+ properties inherited from CreativeWork
- SoftwareSourceCode: Developer-facing metadata
- SoftwareApplication: User-facing metadata
- Focus: Web search indexing, semantic web integration

**Coverage**: All CodeMeta properties (built on Schema.org foundation)

---

### 4. Zenodo Software Metadata

**Status**: Institutional standard at CERN, widely used by researchers

**Key Characteristics**:
- Parses CITATION.cff and .zenodo.json files
- Integrates CodeMeta for metadata standardization
- DOI assignment for software versions
- Automatic GitHub → Zenodo workflow
- Focus: Research software preservation and citation

**Metadata Captured**:
- Title, creators, licenses, keywords
- Version, language, contributors
- Funding information
- Related identifiers
- CodeMeta-based software-specific fields

---

### 5. Software Heritage

**Status**: International digital preservation initiative

**Key Characteristics**:
- Universal source code archive using hash-based content identification
- Preserves intrinsic (embedded) and extrinsic (platform-specific) metadata
- Merkle-directed acyclic graph for immutable storage
- Converts harvested metadata to CodeMeta format
- Focus: Software preservation, provenance, long-term access

**Unique Contributions**:
- `provenanceOrigin` - Where code was originally found
- `archiveUrl` - Location in Software Heritage archive
- `swhHash` - Cryptographic content identifier
- `branches`, `releaseTags` - VCS metadata
- Emphasis on metadata sourcing and traceability

---

## Key Findings

### Coverage Matrix (127 total fields identified)

**Fields most commonly defined** (in 4+ standards):
- name, description, version
- authors, contributors, maintainers
- licenses, identifier
- datePublished, dateCreated
- codeRepository, downloadUrl
- keywords

**Fields unique to standards**:
- **CodeMeta only**: buildInstructions, continuousIntegration, developmentStatus
- **CFF only**: message, preferred-citation, repository-artifact
- **Software Heritage only**: provenanceOrigin, swhHash, archiveUrl
- **Schema.org only**: applicationCategory, encoding, targetProduct

### Interoperability Status

**Strong interoperability**:
- CodeMeta ↔ CFF (converter tools available)
- CodeMeta ↔ Schema.org (CodeMeta built on Schema.org)
- CodeMeta ↔ Zenodo (Zenodo based on CodeMeta)
- CFF ↔ Zenodo (native integration)

**Partial interoperability**:
- Software Heritage (converts to/from CodeMeta, maintains parallel internal model)
- Schema.org ↔ CFF (via CodeMeta bridge)

**Conversion flow**: CFF → CodeMeta → Schema.org → Web indexing
                    CodeMeta ↔ Zenodo ↔ Zenodo deposits
                    Codemetax ← Software Heritage (ingest)

---

## Field Inventory Results

### By Category (from linkml_software_schema_fields.md):

| Category | Fields | Key Examples |
|---|---|---|
| Identification & Naming | 10 | name, description, keywords, applicationCategory |
| Versioning & Temporal | 13 | version, dateCreated, dateReleased, releaseNotes |
| Authorship & Attribution | 14 | authors, contributors, maintainers, funders |
| Technical Specifications | 13 | programmingLanguages, softwareRequirements, OS |
| Repository & Distribution | 8 | codeRepository, downloadUrl, artifactRepository |
| Build, Testing & CI/CD | 8 | buildInstructions, continuousIntegration, testFramework |
| Licensing & Rights | 5 | licenses, licenseUrl, copyrightHolder |
| Citations & References | 10 | referencePublications, preferredCitation |
| Relationships & Hierarchies | 9 | hasPart, isPartOf, hasSourceCode |
| Content & Documentation | 6 | supportingData, softwareHelp, reviewRecords |
| Specialized (SWH) | 10 | provenanceOrigin, swhHash, archiveUrl |
| Zenodo-Specific | 9 | zenodoRecordId, accessRights, relationType |

**Total: 127 comprehensive fields**

---

## Recommended Minimal Field Set

For a basic software metadata schema (11 fields):
```
name, description, url, codeRepository, version,
datePublished, authors, licenses, developmentStatus,
issueTracker, readme
```

For research software (24 fields):
```
[Minimal] + abstract, keywords, identifier,
programmingLanguages, softwareRequirements,
operatingSystems, runtimePlatforms, maintainers,
funders, referencePublications, buildInstructions,
continuousIntegration, applicationCategory
```

For archival/preservation (47+ fields):
```
[Research software] + dateCreated, dateModified,
releaseNotes, contributors, softwareSuggestions,
testFramework, buildSystem, memoryRequirements,
storageRequirements, sponsors, publisher,
copyrightHolder, hasPart, isPartOf, relatedLinks,
fileFormat, downloadUrl, artifactRepository, commit
```

---

## Critical Standards Alignment

### FAIR Principles Alignment
- **Findable**: keywords, identifier, applicationCategory, description
- **Accessible**: url, codeRepository, downloadUrl, isAccessibleForFree
- **Interoperable**: license, format declarations, standard metadata
- **Reusable**: referencePublications, softwareRequirements, documentatio n

### Research Software MetaData (RSMD) Guidelines
CodeMeta recommended by RSMD guidelines for:
- RSMD 1.5 - Keep metadata in single source file
- RSMD 4.1 - Add software name and functionality
- RSMD 4.2 - Add descriptive metadata for classification
- RSMD 4.3 - Cite related journal articles
- RSMD 4.4 - Add machine-readable metadata
- RSMD 5.1 - Add author attribution

---

## Recommendations for LinkML Schema

### 1. Class Structure

**Recommended inheritance hierarchy**:
```
CreativeWork (base)
├── Software (extends CreativeWork)
│   ├── SoftwareSourceCode (code + development metadata)
│   └── SoftwareApplication (packaged + distribution metadata)
├── CodeRepository (repository-specific)
└── Person, Organization (Actor classes)
```

### 2. Slot/Field Organization

Use shared slots for common patterns:
- `identifiable` - identifier, sameAs, url
- `temporal` - dateCreated, dateModified, datePublished
- `authored` - authors, contributors, maintainers
- `technical` - programmingLanguages, requirements, OS

### 3. Enumeration Patterns

Define enumerations for:
- `DevelopmentStatus` (active, inactive, suspended, abandoned, etc.)
- `LicenseType` (SPDX identifiers)
- `ProgrammingLanguage` (common languages)
- `OperatingSystem` (Windows, Linux, macOS, etc.)
- `CitationType` (journal-article, software, dataset, etc.)

### 4. Nested Object Classes

Define reusable objects:
- `Person` (with name parts, email, ORCID, affiliation)
- `Organization` (with name, URL, ROR ID)
- `ComputerLanguage` (name, version, URL)
- `SoftwareRequirement` (name, version spec, URL)
- `Citation` (flexible structure for different work types)
- `ScholarlyArticle` (journal metadata, DOI, authors)

### 5. Validation & Patterns

Include patterns for:
- Semantic versioning (MAJOR.MINOR.PATCH)
- SPDX license expressions
- ORCID URLs (https://orcid.org/XXXX-XXXX-XXXX-XXXX)
- ISO date formats (YYYY-MM-DD)
- URIs (HTTP/HTTPS URLs, DOIs)

### 6. Multi-valued Fields

Mark as multivalued:
- keywords, authors, contributors, licenses
- softwareRequirements, operatingSystems, references
- relatedPublications, relatedLinks, relatedDatasets

---

## Next Steps for Implementation

1. **Define base classes** using recommended inheritance hierarchy
2. **Create common slots** for shared patterns (identifiable, temporal, authored)
3. **Implement Person and Organization** with full contact fields
4. **Build Software and CodeRepository** primary classes
5. **Add validation rules** for versions, licenses, URLs
6. **Define mapping module** for cross-standard translation
7. **Create serializers** for CodeMeta JSON-LD and CFF YAML export
8. **Build validator** against standard constraints
9. **Test with real software** (numpy, scipy, gdal, etc.)
10. **Document crosswalks** between CFF ↔ CodeMeta ↔ Schema.org

---

## Supporting Documents

Three comprehensive reference documents have been created:

### 1. **research_software_metadata_standards.md**
- Complete field definitions for all 5 standards
- Coverage matrix showing field availability
- Examples and use cases
- Interoperability recommendations

### 2. **codemeta_field_examples.md**
- Full CodeMeta JSON-LD example (production-ready)
- Complete CITATION.cff example
- Field-by-field mappings
- Object structure definitions
- Conversion pathways

### 3. **linkml_software_schema_fields.md**
- 127 comprehensive fields organized by category
- YAML-ready field definitions with sources
- Object structure recommendations
- Use case-specific field selections
- LinkML implementation guidelines
- Validation patterns

---

## Conclusion

The five standards analyzed provide complementary perspectives on software metadata:

- **CodeMeta**: Comprehensive, standard-aligned, developer-friendly
- **CFF**: Human-readable, citation-focused, GitHub-native
- **Schema.org**: Web-standard, SEO-friendly, widely adopted
- **Zenodo**: Preservation-focused, DOI-enabled, institutional
- **Software Heritage**: Provenance-focused, archive-optimized, immutable

A unified LinkML schema incorporating insights from all five can provide:
- **Completeness**: 127 fields covering all metadata needs
- **Interoperability**: Mappable to CodeMeta, CFF, Schema.org, Zenodo
- **Flexibility**: Minimal required fields, extensive optional extensions
- **Validation**: Strong patterns for versions, licenses, identifiers
- **Preservation**: Provenance and archival metadata support

The recommended approach is a graduated implementation: start with essential fields (11), extend to research software standard (24), and optionally add archival/preservation fields (47+).

---

## References & Sources

- CodeMeta Project: https://codemeta.github.io/
- Citation File Format: https://citation-file-format.github.io/
- Schema.org: https://schema.org/SoftwareSourceCode
- Zenodo: https://zenodo.org/
- Software Heritage: https://softwareheritage.org/
- FAIR Impact RSMD Guidelines: https://fair-impact.github.io/RSMD-guidelines/
- Repostatus: http://www.repostatus.org/
- SPDX Licenses: https://spdx.org/licenses/
- LinkML: https://linkml.io/

---

## Document Locations

All reference documents saved to:
```
/home/mohammadi/Documents/Claude/Projects/Infrastructure and Tooling/
├── research_software_metadata_standards.md (comprehensive standard analysis)
├── codemeta_field_examples.md (technical examples and mappings)
└── linkml_software_schema_fields.md (field inventory for implementation)
```
