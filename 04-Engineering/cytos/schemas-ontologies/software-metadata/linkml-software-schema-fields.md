# LinkML Schema Field Inventory for CodeRepository & Software

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: engineers
> **Tags**: `engineering`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

**Purpose**: Comprehensive field listing for building a unified LinkML schema covering software and code repositories based on CodeMeta, CFF, Schema.org, Zenodo, and Software Heritage standards.

**Status**: Ready for LinkML implementation
**Last Updated**: April 4, 2026

---

## Schema Overview

The recommended LinkML schema should support two primary entities:

1. **CodeRepository** - Source code repositories with development metadata
2. **Software** - Packaged software applications and research tools

Both entities inherit common fields and extend with specialized properties.

---

## Complete Field Inventory by Category

### A. IDENTIFICATION & NAMING

```yaml
identifier_fields:
  - id: name
    type: string
    required: true
    description: "Software name/title"
    source: ["CodeMeta", "CFF", "Schema.org", "Zenodo"]
    examples: ["NumPy", "GDAL", "My Climate Analysis Tool"]

  - id: description
    type: string
    required: true
    description: "Brief description of software functionality"
    source: ["CodeMeta", "CFF", "Schema.org", "Zenodo"]
    examples: ["Python package for numerical computing", "Geospatial data library"]

  - id: abstract
    type: string
    required: false
    description: "Longer abstract describing purpose and scope"
    source: ["CodeMeta", "CFF"]
    examples: ["Comprehensive framework for climate data analysis..."]

  - id: url
    type: uri
    required: false
    description: "Project website/homepage URL"
    source: ["CodeMeta", "CFF", "Schema.org"]
    examples: ["https://numpy.org", "https://gdal.org"]

  - id: identifier
    type: string
    required: false
    multivalued: true
    description: "Unique identifiers (DOI, UUID, SPDX, etc.)"
    source: ["CodeMeta", "CFF", "Schema.org", "Zenodo"]
    pattern: "uuid|doi|urn|url"
    examples: ["10.5281/zenodo.1234567", "urn:uuid:12345678-1234-5678-1234-567812345678"]

  - id: keywords
    type: string
    required: false
    multivalued: true
    description: "Keywords/tags for discovery"
    source: ["CodeMeta", "CFF", "Schema.org", "Zenodo"]
    examples: ["climate", "data-analysis", "python"]

  - id: applicationCategory
    type: string
    required: false
    description: "Type of software application"
    source: ["CodeMeta", "Schema.org"]
    examples: ["Scientific Software", "Developer Tool", "Data Analysis"]

  - id: applicationSubCategory
    type: string
    required: false
    description: "Subcategory of application"
    source: ["CodeMeta", "Schema.org"]
    examples: ["Climate Data Processing", "Geospatial Analysis"]
```

---

### B. VERSIONING & TEMPORAL INFORMATION

```yaml
versioning_fields:
  - id: version
    type: string
    required: true
    description: "Current software version (semantic versioning recommended)"
    source: ["CodeMeta", "CFF", "Schema.org", "Zenodo"]
    pattern: "^\d+\.\d+(\.\d+)?(-[a-zA-Z0-9]+)?(\+[a-zA-Z0-9]+)?$"
    examples: ["2.0.4", "1.0.0-alpha.1", "2.1.0+20230115"]

  - id: softwareVersion
    type: string
    required: false
    description: "Alternative version field (redundant with version)"
    source: ["CodeMeta"]

  - id: dateCreated
    type: date
    required: false
    description: "Date when software was first created"
    source: ["CodeMeta", "Schema.org"]
    examples: ["2020-01-15"]

  - id: dateModified
    type: date
    required: false
    description: "Date of last modification"
    source: ["CodeMeta", "Schema.org"]

  - id: datePublished
    type: date
    required: false
    description: "Date of first publication/release"
    source: ["CodeMeta", "Schema.org", "Zenodo"]

  - id: dateReleased
    type: date
    required: false
    description: "Date when this version was released"
    source: ["CFF", "Zenodo"]

  - id: releaseNotes
    type: string
    required: false
    description: "Description of what changed in this version"
    source: ["CodeMeta", "Schema.org"]
    examples: ["Added GPU acceleration, improved memory efficiency"]

  - id: commit
    type: string
    required: false
    description: "Git commit hash for this version"
    source: ["CFF", "Software Heritage"]
    examples: ["abc123def456"]

  - id: developmentStatus
    type: enum
    required: false
    description: "Current development status (per repostatus.org)"
    source: ["CodeMeta"]
    enum_values:
      - active
      - inactive
      - suspended
      - abandoned
      - unsupported
      - moved
      - transitional
      - concept
      - wip

  - id: embargoEndDate
    type: date
    required: false
    description: "Date until software is embargoed from public access"
    source: ["CodeMeta"]
```

---

### C. AUTHORSHIP & ATTRIBUTION

```yaml
authorship_fields:
  - id: authors
    type: Person
    required: true
    multivalued: true
    description: "Primary software authors"
    source: ["CodeMeta", "CFF", "Schema.org", "Zenodo"]

  - id: contributors
    type: Person
    required: false
    multivalued: true
    description: "Secondary contributors to the software"
    source: ["CodeMeta", "Schema.org", "Zenodo"]

  - id: maintainers
    type: Person
    required: false
    multivalued: true
    description: "Individuals responsible for maintaining software"
    source: ["CodeMeta"]

  - id: editors
    type: Person
    required: false
    multivalued: true
    description: "Person(s) who edited the software/documentation"
    source: ["CodeMeta", "Schema.org"]

  - id: copyrightHolder
    type: "Person or Organization"
    required: false
    description: "Party holding legal copyright"
    source: ["CodeMeta", "Schema.org"]

  - id: copyrightYear
    type: integer
    required: false
    description: "Year copyright was first asserted"
    source: ["CodeMeta", "Schema.org"]
    examples: [2020, 2023]

  - id: funders
    type: Organization
    required: false
    multivalued: true
    description: "Organizations providing financial support"
    source: ["CodeMeta", "Zenodo"]

  - id: sponsors
    type: Organization
    required: false
    multivalued: true
    description: "Organizations supporting software development"
    source: ["CodeMeta"]

  - id: producer
    type: "Person or Organization"
    required: false
    description: "Producer of the software"
    source: ["CodeMeta", "Schema.org"]

  - id: publisher
    type: Organization
    required: false
    description: "Publisher of the software"
    source: ["CodeMeta", "Schema.org"]

  - id: provider
    type: "Person or Organization"
    required: false
    description: "Service provider/operator"
    source: ["CodeMeta", "Schema.org"]

  - id: funding
    type: string
    required: false
    multivalued: true
    description: "Funding source (grant numbers, etc.)"
    source: ["CodeMeta", "CFF"]
    examples: ["Grant #NSF-1234567", "EC Horizon Europe"]

  - id: contact
    type: Person
    required: false
    multivalued: true
    description: "Contact person(s) for software inquiries"
    source: ["CFF"]
```

**Person Object Structure**:
```yaml
Person:
  attributes:
    familyName: string (required)
    givenName: string (required)
    nameParticle: string (optional, e.g., "von", "de")
    nameSuffix: string (optional, e.g., "Jr.", "III")
    email: string (optional)
    affiliation: Organization (optional)
    address: PostalAddress (optional)
    identifier: string (optional, ORCID recommended)
    website: uri (optional)
    telephone: string (optional)
```

**Organization Object Structure**:
```yaml
Organization:
  attributes:
    name: string (required)
    url: uri (optional)
    email: string (optional)
    address: PostalAddress (optional)
    ror: uri (optional, ROR ID)
    identifier: string (optional)
```

---

### D. TECHNICAL SPECIFICATIONS

```yaml
technical_fields:
  - id: programmingLanguages
    type: ComputerLanguage
    required: false
    multivalued: true
    description: "Programming language(s) used to build software"
    source: ["CodeMeta", "Schema.org"]
    examples: ["Python", "C++", "Java"]

  - id: softwareRequirements
    type: SoftwareSourceCode
    required: false
    multivalued: true
    description: "Required software dependencies"
    source: ["CodeMeta", "Schema.org"]
    examples: ["numpy>=1.19.0", "scipy>=1.5.0"]

  - id: softwareSuggestions
    type: SoftwareSourceCode
    required: false
    multivalued: true
    description: "Optional dependencies for optional features"
    source: ["CodeMeta"]
    examples: ["jupyter (for notebooks)", "matplotlib (for visualization)"]

  - id: runtimePlatforms
    type: string
    required: false
    multivalued: true
    description: "Runtime platform/interpreter requirements"
    source: ["CodeMeta", "Schema.org"]
    examples: ["Python 3.8+", "JVM 11+", ".NET Framework 4.8"]

  - id: operatingSystems
    type: string
    required: false
    multivalued: true
    description: "Supported operating systems"
    source: ["CodeMeta", "Schema.org", "Zenodo"]
    examples: ["Linux", "macOS", "Windows"]

  - id: processorRequirements
    type: string
    required: false
    description: "Processor architecture requirements"
    source: ["CodeMeta", "Schema.org"]
    examples: ["x86_64", "arm64", "IA64"]

  - id: memoryRequirements
    type: string
    required: false
    description: "Minimum and recommended memory"
    source: ["CodeMeta", "Schema.org"]
    examples: ["2GB minimum, 8GB recommended"]

  - id: storageRequirements
    type: string
    required: false
    description: "Storage requirements (disk space)"
    source: ["CodeMeta", "Schema.org"]
    examples: ["500MB installation, plus data files"]

  - id: fileSize
    type: string
    required: false
    description: "Size of application package"
    source: ["CodeMeta", "Schema.org"]
    examples: ["18MB", "250KB"]

  - id: fileFormats
    type: string
    required: false
    multivalued: true
    description: "File formats supported/produced"
    source: ["CodeMeta", "Schema.org"]
    examples: ["application/json", "text/csv", "application/netcdf"]

  - id: permissions
    type: string
    required: false
    multivalued: true
    description: "Permissions/capabilities required to run"
    source: ["CodeMeta", "Schema.org"]
    examples: ["internet access", "GPU access", "filesystem read-write"]
```

**ComputerLanguage Object Structure**:
```yaml
ComputerLanguage:
  attributes:
    name: string (required)
    url: uri (optional)
    version: string (optional)
    identifier: uri (optional, Wikidata)
```

**SoftwareSourceCode Object Structure**:
```yaml
SoftwareSourceCode:
  attributes:
    name: string (required)
    url: uri (optional)
    version: string (optional)
    description: string (optional)
    license: string (optional)
    identifier: uri (optional)
```

---

### E. REPOSITORY & DISTRIBUTION

```yaml
repository_fields:
  - id: codeRepository
    type: uri
    required: true
    description: "URL to source code repository"
    source: ["CodeMeta", "CFF", "Schema.org", "Zenodo"]
    examples: ["https://github.com/numpy/numpy", "https://gitlab.com/gdal/gdal"]

  - id: repositoryCode
    type: uri
    required: false
    description: "Alternative field for code repository"
    source: ["CFF"]

  - id: artifactRepository
    type: uri
    required: false
    description: "URL to packaged software artifact repository"
    source: ["CFF", "Zenodo"]
    examples: ["https://pypi.org/project/numpy", "https://hub.docker.com/r/library/python"]

  - id: downloadUrl
    type: uri
    required: false
    description: "URL to download binary/executable"
    source: ["CodeMeta", "Schema.org"]
    examples: ["https://github.com/numpy/numpy/releases/download/v1.24.0/"]

  - id: installUrl
    type: uri
    required: false
    description: "URL where app may be installed"
    source: ["CodeMeta", "Schema.org"]

  - id: fileFormat
    type: string
    required: false
    description: "MIME format of distributed software"
    source: ["CodeMeta", "Schema.org"]
    examples: ["application/zip", "application/gzip", "application/x-tar"]

  - id: isAccessibleForFree
    type: boolean
    required: false
    description: "Whether software is accessible/available for free"
    source: ["CodeMeta", "Schema.org"]

  - id: repositoryArtifact
    type: uri
    required: false
    description: "Synonym for artifactRepository"
    source: ["CFF"]
```

---

### F. BUILD, TESTING & CI/CD

```yaml
build_testing_fields:
  - id: buildInstructions
    type: uri
    required: false
    description: "Link to build/installation documentation"
    source: ["CodeMeta"]
    examples: ["https://github.com/project/blob/main/INSTALL.md"]

  - id: continuousIntegration
    type: uri
    required: false
    description: "Link to CI/CD pipeline"
    source: ["CodeMeta"]
    examples: ["https://github.com/project/actions", "https://travis-ci.org/project"]

  - id: issueTracker
    type: uri
    required: false
    description: "URL to bug reporting/issue tracking system"
    source: ["CodeMeta", "Schema.org"]
    examples: ["https://github.com/project/issues"]

  - id: readme
    type: uri
    required: false
    description: "Link to README file"
    source: ["CodeMeta"]
    examples: ["https://github.com/project/blob/main/README.md"]

  - id: softwareHelp
    type: CreativeWork
    required: false
    description: "Link to software documentation/help"
    source: ["CodeMeta", "Schema.org"]

  - id: testFramework
    type: string
    required: false
    multivalued: true
    description: "Testing framework(s) used"
    source: [custom]
    examples: ["pytest", "unittest", "Jest", "JUnit"]

  - id: buildSystem
    type: string
    required: false
    description: "Build system used"
    source: [custom]
    examples: ["setuptools", "Maven", "Gradle", "CMake"]
```

---

### G. LICENSING & RIGHTS

```yaml
licensing_fields:
  - id: licenses
    type: string
    required: true
    multivalued: true
    description: "SPDX license identifier(s)"
    source: ["CodeMeta", "CFF", "Schema.org", "Zenodo"]
    pattern: "SPDX expression"
    examples: ["MIT", "Apache-2.0", "GPL-3.0-or-later", "(MIT OR Apache-2.0)"]

  - id: licenseUrl
    type: uri
    required: false
    description: "URL to full license text"
    source: ["CFF"]
    examples: ["https://opensource.org/licenses/MIT"]

  - id: license
    type: "uri or string"
    required: false
    description: "License in full form (URL or object)"
    source: ["CodeMeta", "Schema.org"]

  - id: rights
    type: string
    required: false
    description: "Rights statement/declaration"
    source: ["Zenodo"]

  - id: rightsUri
    type: uri
    required: false
    description: "URI for rights statement"
    source: ["Zenodo"]
```

---

### H. CITATIONS & REFERENCES

```yaml
citation_fields:
  - id: referencePublications
    type: ScholarlyArticle
    required: false
    multivalued: true
    description: "Academic publications related to/describing software"
    source: ["CodeMeta", "CFF", "Zenodo"]

  - id: preferredCitation
    type: Citation
    required: false
    description: "Preferred way to cite this software"
    source: ["CFF"]

  - id: citations
    type: Citation
    required: false
    multivalued: true
    description: "All citations for this software"
    source: ["CodeMeta", "CFF"]

  - id: references
    type: CreativeWork
    required: false
    multivalued: true
    description: "Works this software references or builds upon"
    source: ["CFF", "Schema.org"]

  - id: relatedPublications
    type: CreativeWork
    required: false
    multivalued: true
    description: "Publications related to this software"
    source: ["CodeMeta"]

  - id: relatedDatasets
    type: Dataset
    required: false
    multivalued: true
    description: "Datasets associated with or used by software"
    source: [custom]

  - id: citation
    type: CreativeWork
    required: false
    multivalued: true
    description: "A citation or reference to another creative work"
    source: ["CodeMeta", "Schema.org"]

  - id: relatedLinks
    type: uri
    required: false
    multivalued: true
    description: "Related links (documentation, examples, etc.)"
    source: ["CodeMeta", "Schema.org"]
    examples: ["https://project.org/docs", "https://project.org/tutorial"]
```

**ScholarlyArticle Object Structure**:
```yaml
ScholarlyArticle:
  attributes:
    name: string (required)
    author: array[Person] (optional)
    datePublished: date (optional)
    journal: string (optional)
    volume: string (optional)
    issue: string (optional)
    pages: string (optional)
    doi: uri (optional)
    url: uri (optional)
    identifier: uri (optional)
```

**Citation Object Structure**:
```yaml
Citation:
  attributes:
    type: enum (book, journal-article, conference, software, etc.)
    authors: array[Person] (optional)
    title: string (required)
    year: integer (optional)
    doi: uri (optional)
    url: uri (optional)
    journal: string (optional for articles)
    volume: string (optional)
    issue: string (optional)
    pages: string (optional)
```

---

### I. RELATIONSHIPS & HIERARCHIES

```yaml
relationship_fields:
  - id: hasPart
    type: CreativeWork
    required: false
    multivalued: true
    description: "CreativeWork that is part of this work (sub-modules, plugins)"
    source: ["CodeMeta", "Schema.org"]

  - id: isPartOf
    type: CreativeWork
    required: false
    description: "CreativeWork this is part of (parent project)"
    source: ["CodeMeta", "Schema.org"]

  - id: hasSourceCode
    type: SoftwareSourceCode
    required: false
    multivalued: true
    description: "Link to where source code is located"
    source: ["CodeMeta"]

  - id: isSourceCodeOf
    type: SoftwareApplication
    required: false
    multivalued: true
    description: "Software application(s) built from this source code"
    source: ["CodeMeta"]

  - id: targetProducts
    type: SoftwareApplication
    required: false
    multivalued: true
    description: "Target operating systems or products"
    source: ["CodeMeta", "Schema.org"]

  - id: relatedSoftware
    type: SoftwareSourceCode
    required: false
    multivalued: true
    description: "Other software packages related to this one"
    source: [custom]

  - id: sameAs
    type: uri
    required: false
    multivalued: true
    description: "URLs for canonical identities (Wikidata, Wikipedia, etc.)"
    source: ["CodeMeta", "Schema.org"]
    examples: ["https://www.wikidata.org/wiki/Q4294914", "https://en.wikipedia.org/wiki/NumPy"]
```

---

### J. CONTENT & DOCUMENTATION

```yaml
content_fields:
  - id: supportingData
    type: Dataset
    required: false
    multivalued: true
    description: "Datasets supporting or used by software"
    source: ["CodeMeta", "Schema.org"]

  - id: encoding
    type: MediaObject
    required: false
    multivalued: true
    description: "Media objects encoding this software"
    source: ["CodeMeta", "Schema.org"]

  - id: reviewRecords
    type: Review
    required: false
    multivalued: true
    description: "Code review records and peer review"
    source: ["CodeMeta"]

  - id: reviewBody
    type: string
    required: false
    description: "Review body text"
    source: ["CodeMeta"]

  - id: reviewAspect
    type: string
    required: false
    description: "Aspect of software being reviewed"
    source: ["CodeMeta"]
    examples: ["Code Quality", "Documentation", "Testing"]
```

---

### K. SPECIALIZED FIELDS (Software Heritage, Provenance)

```yaml
provenance_fields:
  - id: provenanceOrigin
    type: uri
    required: false
    description: "Where software was originally discovered"
    source: ["Software Heritage"]
    examples: ["https://github.com/numpy/numpy"]

  - id: intrinsicMetadata
    type: object
    required: false
    description: "Metadata embedded in source code"
    source: ["Software Heritage"]
    examples: ["setup.py, pyproject.toml, package.json"]

  - id: extrinsicMetadata
    type: object
    required: false
    description: "Metadata not in source code (platform-specific)"
    source: ["Software Heritage"]
    examples: ["GitHub stars, repository creation date"]

  - id: archiveUrl
    type: uri
    required: false
    description: "URL in Software Heritage archive"
    source: ["Software Heritage"]
    examples: ["https://archive.softwareheritage.org/"]

  - id: swhHash
    type: string
    required: false
    description: "Software Heritage intrinsic identifier (SWID)"
    source: ["Software Heritage"]
    pattern: "swh:[0-9]+:[a-z]+:[0-9a-f]{40}"

  - id: releaseTags
    type: string
    required: false
    multivalued: true
    description: "Git/VCS release tags"
    source: ["Software Heritage"]
    examples: ["v1.0.0", "v2.0.4"]

  - id: branches
    type: string
    required: false
    multivalued: true
    description: "Primary development branches"
    source: ["Software Heritage"]
    examples: ["main", "develop", "master"]
```

---

### L. ZENODO-SPECIFIC FIELDS

```yaml
zenodo_fields:
  - id: zenodoRecordId
    type: integer
    required: false
    description: "Zenodo record ID"
    source: ["Zenodo"]
    examples: [1234567]

  - id: zenodoConceptId
    type: integer
    required: false
    description: "Zenodo concept ID (for version series)"
    source: ["Zenodo"]

  - id: zenodoUrl
    type: uri
    required: false
    description: "URL to Zenodo deposit"
    source: ["Zenodo"]
    examples: ["https://zenodo.org/record/1234567"]

  - id: accessRights
    type: enum
    required: false
    description: "Access rights level"
    source: ["Zenodo"]
    enum_values:
      - open
      - embargoed
      - restricted
      - closed

  - id: relationType
    type: string
    required: false
    multivalued: true
    description: "Relationship type to other resources"
    source: ["Zenodo"]
    examples: ["isVersionOf", "hasPart", "isPartOf", "references"]

  - id: contributors
    type: Person
    required: false
    multivalued: true
    description: "Contributors with roles"
    source: ["Zenodo"]
```

---

## Summary Statistics

**Total Fields: 127**

**By Category**:
- Identification & Naming: 10
- Versioning & Temporal: 13
- Authorship & Attribution: 14
- Technical Specifications: 13
- Repository & Distribution: 8
- Build, Testing & CI/CD: 8
- Licensing & Rights: 5
- Citations & References: 10
- Relationships & Hierarchies: 9
- Content & Documentation: 6
- Specialized (SWH, Provenance): 10
- Zenodo-Specific: 9

**Coverage by Standard**:
- CodeMeta: 95+ fields
- CFF: 45+ fields
- Schema.org: 60+ fields
- Zenodo: 40+ fields
- Software Heritage: 25+ fields

---

## Recommended Field Selection by Use Case

### Minimal (Repository-Only)
Essential fields for version control repositories:
```
name, description, url, codeRepository, version, datePublished,
authors, licenses, developmentStatus, issueTracker, readme
```
**Total: 11 fields**

### Standard (Research Software)
Comprehensive coverage for typical research software:
```
[Minimal] +
abstract, keywords, identifier, programmingLanguages,
softwareRequirements, operatingSystems, runtimePlatforms,
maintainers, funders, referencePublications, buildInstructions,
continuousIntegration, applicationCategory
```
**Total: 24 fields**

### Complete (Archive/Registry)
Full metadata for preservation and discovery:
```
[Standard] +
dateCreated, dateModified, releaseNotes, contributors,
softwareSuggestions, testFramework, buildSystem,
memoryRequirements, storageRequirements, processorRequirements,
sponsors, publisher, copyrightHolder, copyrightYear,
hasPart, isPartOf, relatedLinks, reviewRecords,
fileFormat, downloadUrl, artifactRepository,
embargoEndDate, developmentStatus, commit
```
**Total: 47+ fields**

### Archive & Preservation (Software Heritage)
Maximum metadata including provenance:
```
[Complete] +
provenanceOrigin, archiveUrl, swhHash, branches,
releaseTags, intrinsicMetadata, extrinsicMetadata,
supportingData, sameAs, hasSourceCode, isSourceCodeOf
```
**Total: 58+ fields**

---

## LinkML Implementation Tips

### 1. Use Enumerations for Constrained Values
```yaml
DevelopmentStatusEnum:
  description: "Development status per repostatus.org"
  permissible_values:
    active: {}
    inactive: {}
    suspended: {}
    abandoned: {}
    unsupported: {}
    moved: {}
    transitional: {}
    concept: {}
    wip: {}
```

### 2. Define Reusable Classes
```yaml
Person:
  attributes:
    family_name: string
    given_name: string
    email: string
    identifier: string
    affiliation: Organization

ComputerLanguage:
  attributes:
    name: string
    url: uri
    version: string

SoftwareRequirement:
  attributes:
    name: string
    version_spec: string
    url: uri
```

### 3. Create Slots for Common Patterns
```yaml
slots:
  identifiable:
    - identifier
    - sameAs

  temporal:
    - dateCreated
    - dateModified
    - datePublished
    - dateReleased

  authored:
    - authors
    - contributors
    - maintainers
```

### 4. Inheritance Hierarchy
```yaml
CreativeWork:
  # Base class with common fields
  attributes:
    name
    description
    url
    identifier
    dateCreated
    dateModified
    license

Software(CreativeWork):
  # Extends CreativeWork
  attributes:
    version
    programmingLanguages
    softwareRequirements
    operatingSystems

CodeRepository(Software):
  # Extends Software with repo-specific fields
  attributes:
    codeRepository
    issueTracker
    continuousIntegration
    developmentStatus
```

---

## Validation Patterns

### Version Format
```yaml
version:
  pattern: "^\d+\.\d+(\.\d+)?(-[a-zA-Z0-9]+)?(\+[a-zA-Z0-9]+)?$"
  description: "Semantic versioning (MAJOR.MINOR.PATCH[-PRERELEASE][+BUILD])"
```

### SPDX License
```yaml
licenses:
  multivalued: true
  pattern: "^[A-Z0-9\\.\\-\\s()]+$"
  description: "SPDX license expression"
```

### URL Format
```yaml
uri_fields:
  - url
  - codeRepository
  - downloadUrl
  - artifactRepository
  - continuousIntegration
  type: uri
```

---

## Cross-Standard Mapping Reference

| CodeMeta | CFF | Schema.org | Zenodo |
|---|---|---|---|
| name | title | name | title |
| description | abstract | description | description |
| version | version | version | version |
| datePublished | date-released | datePublished | publication_date |
| author | authors | author | creators |
| license | license | license | license |
| codeRepository | repository-code | codeRepository | url (code) |
| identifier | identifiers | identifier | identifiers |

---

## Sources

- CodeMeta Project: https://codemeta.github.io/
- Citation File Format: https://citation-file-format.github.io/
- Schema.org Software: https://schema.org/SoftwareSourceCode
- Zenodo Documentation: https://help.zenodo.org/
- Software Heritage: https://softwareheritage.org/
- LinkML Documentation: https://linkml.io/
