# Quick Reference: Research Software Metadata Standards

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: engineers
> **Tags**: `engineering`
> **Variants**: Technical (this doc) - Readable (quick-reference.md in Obsidian vault: 04-Engineering/cytos/schemas-ontologies/software-metadata/) - Agent (n/a)

**For rapid lookup of field definitions and standard coverage**

---

## What Each Standard Does

| Standard | Format | Purpose | Best For |
|---|---|---|---|
| **CodeMeta** | JSON-LD | Software metadata vocabulary bridge | Registry indexing, discovery |
| **CFF** | YAML | Software citation format | Human editing, version control |
| **Schema.org** | JSON-LD / Microdata | Semantic web markup | Web search indexing |
| **Zenodo** | JSON metadata | Research data archival | DOI assignment, preservation |
| **SWH** | Proprietary | Code preservation | Long-term archival, provenance |

---

## Essential Fields (Must Have)

```
1. name                 - Software title
2. description         - What it does
3. version             - Version number (semantic)
4. authors             - Who created it
5. licenses            - Legal terms (SPDX)
6. codeRepository      - Where code lives
7. url                 - Project website
8. datePublished       - Release date
9. identifier          - DOI or UUID
10. keywords           - Subject tags
```

---

## Extended Fields by Category

### Technical (for requirements/dependencies)
- `programmingLanguages` - Languages used
- `softwareRequirements` - Dependencies
- `runtimePlatforms` - Runtime environment (Python 3.8+)
- `operatingSystems` - Supported OS (Linux, Windows, macOS)
- `processorRequirements` - CPU architecture (x86_64, ARM)
- `memoryRequirements` - RAM needed
- `storageRequirements` - Disk space

### Development (for builders/maintainers)
- `buildInstructions` - How to build
- `continuousIntegration` - CI/CD URL (GitHub Actions, Travis)
- `issueTracker` - Bug tracking (GitHub Issues)
- `developmentStatus` - active/inactive/abandoned
- `maintainers` - People responsible for maintenance
- `testFramework` - Testing tool (pytest, Jest)
- `buildSystem` - Build tool (setuptools, Maven)

### Research (for citations)
- `referencePublications` - Academic papers describing it
- `preferredCitation` - How to cite it
- `references` - Works it builds on
- `relatedPublications` - Related papers
- `relatedDatasets` - Associated datasets
- `funding` - Grant info
- `funders` - Funding organizations

### Legal (for licensing/rights)
- `licenses` - SPDX license IDs (MIT, Apache-2.0, GPL-3.0)
- `licenseUrl` - Full license text URL
- `copyrightHolder` - Who owns copyright
- `copyrightYear` - Copyright year
- `rights` - Rights statement

---

## Field Availability Matrix

### Fields in 4+ standards (highest interop)
```
name              CFF  CodeMeta  Schema.org  Zenodo  SWH
description       ✓    ✓         ✓           ✓       ✓
version           ✓    ✓         ✓           ✓       ✓
datePublished     -    ✓         ✓           ✓       ✓
authors           ✓    ✓         ✓           ✓       ✓
licenses          ✓    ✓         ✓           ✓       ✓
identifier        ✓    ✓         ✓           ✓       ✓
url               ✓    ✓         ✓           -       ✓
codeRepository    ✓    ✓         ✓           ✓       ✓
keywords          ✓    ✓         ✓           ✓       -
```

### Fields unique to one standard
```
CodeMeta:        buildInstructions, continuousIntegration, developmentStatus
CFF:             message, preferredCitation, repositoryArtifact
Schema.org:      applicationCategory, encoding
SWH:             provenanceOrigin, swhHash, archiveUrl
Zenodo:          zenodoRecordId, accessRights
```

---

## Quick Conversion Guide

### CITATION.cff → CodeMeta
```
cff.title           → codemeta.name
cff.abstract        → codemeta.description
cff.authors         → codemeta.author
cff.version         → codemeta.version
cff.date-released   → codemeta.datePublished
cff.repository-code → codemeta.codeRepository
cff.license         → codemeta.license (SPDX)
cff.keywords        → codemeta.keywords
cff.identifiers     → codemeta.identifier
```

### CodeMeta → CFF
```
codemeta.name           → cff.title
codemeta.description    → cff.abstract
codemeta.author         → cff.authors
codemeta.version        → cff.version
codemeta.datePublished  → cff.date-released
codemeta.codeRepository → cff.repository-code
codemeta.license        → cff.license
```

### CodeMeta → Zenodo
```
codemeta.name           → title
codemeta.author         → creators
codemeta.description    → description
codemeta.version        → version
codemeta.datePublished  → publication_date
codemeta.license        → license (SPDX)
```

---

## Common SPDX Licenses

```
MIT                    - Permissive, simple
Apache-2.0             - Permissive, patent clause
GPL-3.0-or-later       - Copyleft, require source sharing
BSD-3-Clause           - Permissive, similar to MIT
LGPL-3.0-or-later      - Weak copyleft, library-friendly
MPL-2.0                - Copyleft, file-level
AGPL-3.0-or-later      - Strong copyleft, network clause
ISC                    - Minimalist, permissive
Unlicense              - Public domain
CC0-1.0                - Public domain dedication
```

**Tool**: [SPDX License List](https://spdx.org/licenses/)

---

## Development Status Values

```
active         - Actively developed, maintained
inactive       - No longer maintained
suspended      - Temporarily paused
abandoned      - Abandoned by original authors
unsupported    - No longer supported
moved          - Moved to different location
concept        - Early prototype/proof of concept
wip            - Work in progress
```

**Reference**: [repostatus.org](http://www.repostatus.org/)

---

## Semantic Versioning Format

```
MAJOR.MINOR.PATCH[-PRERELEASE][+BUILD]

1.0.0          - First release
2.1.0          - New features, backward compatible
2.1.1          - Bug fix, backward compatible
2.0.0          - Breaking changes
2.0.0-alpha.1  - Pre-release
2.0.0-rc.1     - Release candidate
2.0.0+build123 - Build metadata
```

---

## Where to Put Metadata

### CFF
```
File: CITATION.cff
Location: Repository root
Format: YAML 1.2
Tool: cffinit (web form)
Integration: GitHub native, Zenodo, Zotero
```

### CodeMeta
```
File: codemeta.json
Location: Repository root or .codemeta/
Format: JSON-LD
Tool: CodeMeta Generator
Integration: Software Heritage, registries
```

### Zenodo
```
File: .zenodo.json (optional)
Location: Repository root
Format: JSON metadata
Auto-parsed: From CITATION.cff or codemeta.json
DOI: Auto-assigned on release
```

---

## Nested Objects (Complex Fields)

### Person
```yaml
family-names: Smith
given-names: Jane
email: jane@example.org
affiliation: University of Example
orcid: https://orcid.org/0000-0001-2345-6789
```

### Organization
```yaml
name: National Science Foundation
url: https://nsf.gov
identifier: https://ror.org/021nxhr62
```

### ComputerLanguage
```yaml
name: Python
url: https://python.org
version: 3.8+
```

### Citation (Reference)
```yaml
type: journal-article
title: Publication Title
authors: [...]
year: 2023
doi: 10.1234/example
journal: Journal Name
```

---

## Validation Checklist

### Minimal (will be accepted everywhere)
- [ ] name (title)
- [ ] description
- [ ] version
- [ ] authors
- [ ] license (SPDX format)
- [ ] url or codeRepository

### Recommended (good for discoverability)
- [ ] abstract
- [ ] keywords (3-5)
- [ ] identifier (DOI preferred)
- [ ] datePublished
- [ ] programmingLanguages
- [ ] operatingSystems
- [ ] softwareRequirements (if any)
- [ ] issueTracker
- [ ] continuousIntegration
- [ ] referencePublications (if any)

### Complete (for archival)
- [ ] [Recommended fields above]
- [ ] dateCreated, dateModified
- [ ] maintainers
- [ ] contributors
- [ ] copyrightHolder, copyrightYear
- [ ] buildInstructions
- [ ] developmentStatus
- [ ] softwareSuggestions
- [ ] relatedDatasets
- [ ] relatedLinks
- [ ] hasPart, isPartOf (if applicable)

---

## Common Mistakes to Avoid

| Mistake | Fix |
|---|---|
| Using license name instead of SPDX | Use SPDX ID: "MIT" not "MIT License" |
| Version without semantic format | Use "2.0.4" not "version 2" or "v2" |
| Missing author email | Add contact email for citations |
| Dead URLs in references | Test all links before publication |
| Incomplete person info | Include givenName + familyName |
| Wrong date format | Use ISO 8601: YYYY-MM-DD |
| Outdated metadata | Keep files in version control |
| No identifier/DOI | Get DOI from Zenodo or DataCite |
| Forgetting license URL | Use SPDX or link to full text |
| Redundant fields | CFF/CodeMeta overlap intentionally |

---

## Tools & Resources

### Create/Edit
- CFF Initializer: https://citation-file-format.github.io/cff-initializer-javascript/
- CodeMeta Generator: https://codemeta.github.io/create/
- cffr (R): https://docs.ropensci.org/cffr/

### Validate
- CFF Schema: https://github.com/citation-file-format/schema
- CodeMeta JSON Schema: https://w3id.org/codemeta/3.0/

### Convert
- cff-converter-python: https://github.com/citation-file-format/cff-converter-python
- codemeta-harvester: https://github.com/proycon/codemeta-harvester

### Registry/Archival
- Zenodo: https://zenodo.org/
- Software Heritage: https://softwareheritage.org/
- PyPI (Python): https://pypi.org/
- GitHub Packages: https://github.com/features/packages

### Reference
- SPDX Licenses: https://spdx.org/licenses/
- Repostatus: http://www.repostatus.org/
- Schema.org: https://schema.org/
- FAIR Principles: https://www.go-fair.org/fair-principles/

---

## Quick Lookup: Field → Standards

### authentication
NOT in any standard (custom field)

### buildInstructions
CodeMeta ✓ | CFF - | Schema.org - | Zenodo (via CodeMeta)

### citation
CodeMeta ✓ | CFF ✓ | Schema.org ✓ | Zenodo (via identifiers)

### codeRepository
All standards ✓✓✓✓

### continuousIntegration
CodeMeta ✓ | CFF - | Schema.org - | Zenodo (via CodeMeta)

### datePublished
CodeMeta ✓ | CFF (as date-released) | Schema.org ✓ | Zenodo ✓

### developmentStatus
CodeMeta ✓ | CFF - | Schema.org - | Zenodo (via CodeMeta)

### downloadUrl
CodeMeta ✓ | CFF - | Schema.org ✓ | Zenodo (artifact)

### funders
CodeMeta ✓ | CFF - | Schema.org ✓ | Zenodo ✓

### issueTracker
CodeMeta ✓ | CFF - | Schema.org - | Zenodo (via CodeMeta)

### keywords
All standards ✓✓✓

### license
All standards ✓✓✓✓

### maintainer
CodeMeta ✓ | CFF (contact) | Schema.org - | Zenodo (contact)

### name/title
All standards ✓✓✓✓

### operatingSystem
CodeMeta ✓ | CFF - | Schema.org ✓ | Zenodo (via CodeMeta)

### programmingLanguage
CodeMeta ✓ | CFF - | Schema.org ✓ | Zenodo (via CodeMeta)

### referencePublication
CodeMeta ✓ | CFF (references) | Schema.org ✓ | Zenodo ✓

### softwareRequirements
CodeMeta ✓ | CFF - | Schema.org ✓ | Zenodo (via CodeMeta)

### version
All standards ✓✓✓✓

---

## Use Case Quick Start

### "I want to make my software citable"
**Create**: CITATION.cff + codemeta.json
**Files**: CITATION.cff (root), codemeta.json (root)
**Tools**: cffinit (web form)
**Time**: 10 minutes

### "I want to archive my software"
**Create**: CITATION.cff + .zenodo.json
**Platform**: Zenodo (with GitHub integration)
**Tools**: cffinit + Zenodo UI
**Time**: 20 minutes
**Result**: DOI assigned

### "I want comprehensive software metadata"
**Create**: codemeta.json (complete)
**Files**: codemeta.json (root)
**Tools**: CodeMeta Generator or code
**Time**: 30-45 minutes
**Coverage**: 50+ metadata fields

### "I want to register in a software registry"
**Create**: CITATION.cff or codemeta.json
**Examples**:
  - Python: setuptools metadata + PyPI
  - R: DESCRIPTION file + CRAN
  - General: Software Heritage
**Time**: Variable (registry-dependent)

---

## One-Minute Checklist

Have you defined?
- [ ] **name** - What is your software called?
- [ ] **description** - What does it do? (1 sentence)
- [ ] **version** - What version is this? (MAJOR.MINOR.PATCH)
- [ ] **authors** - Who created it?
- [ ] **license** - What license? (use SPDX code)
- [ ] **url** - Where do people find it?
- [ ] **codeRepository** - Where is the source code?

If you answered YES to all 7: **You have minimum viable software metadata.**

Add these for better discovery:
- [ ] **keywords** - 3-5 subject tags
- [ ] **abstract** - What problem does it solve?
- [ ] **operatingSystems** - What OS does it run on?
- [ ] **programmingLanguages** - What language(s)?
- [ ] **softwareRequirements** - What does it depend on?
- [ ] **referencePublications** - Any papers about it?
- [ ] **datePublished** - When was it released?

If you answered YES to most: **You have publication-ready software metadata.**

---

**For complete details, see the three comprehensive reference documents.**

---

Last updated: April 4, 2026
