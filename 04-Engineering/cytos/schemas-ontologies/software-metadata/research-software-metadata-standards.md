# Research Software Metadata Standards - Comprehensive Analysis

**Date**: April 4, 2026
**Purpose**: Reference guide for building a LinkML schema covering CodeRepository and Software entity types

---

## 1. CodeMeta (https://codemeta.github.io/)

**Overview**: A shared, minimal metadata vocabulary for software designed to support research, discovery, citation, and interoperability across platforms. Uses JSON-LD format and Schema.org terms as foundation.

### CodeMeta Core Properties (from Schema.org Software terms)

#### Identification & Naming
- `name` (Text): The name of the software
- `description` (Text): A description of the software
- `url` (URL): URL of the software/project
- `identifier` (PropertyValue or URL): ISBNs, GTIN codes, UUIDs, etc.
- `sameAs` (URL): URL unambiguously indicating item identity (Wikipedia, Wikidata, official website)

#### Authorship & Attribution
- `author` (Organization or Person): The author of the software
- `contributor` (Organization or Person): Secondary contributors
- `maintainer` (Person): Individual responsible for maintaining the software (with email)
- `editor` (Person): Person who edited the CreativeWork
- `copyrightHolder` (Organization or Person): Party holding legal copyright
- `copyrightYear` (Number): Year copyright was first asserted
- `funder` (Organization or Person): Financial supporter/sponsor
- `sponsor` (Organization or Person): Supporter through pledge or promise
- `producer` (Organization or Person): Person/organization who produced the work
- `publisher` (Organization or Person): Publisher of the work
- `provider` (Organization or Person): Service provider, operator, or performer

#### Versioning & Temporal
- `version` (Number or Text): Version of the software
- `softwareVersion` (Text): Version of software instance
- `dateCreated` (Date): Date when software was created
- `dateModified` (Date): Date when software was last modified
- `datePublished` (Date): Date of first publication
- `releaseNotes` (Text or URL): Description of what changed in this version

#### Technical Specifications
- `programmingLanguage` (ComputerLanguage or Text): Programming language used
- `runtimePlatform` (Text): Runtime platform/script interpreter dependencies (Java v1, Python 2.3, .Net Framework 3.0)
- `softwareRequirements` (SoftwareSourceCode): Required software dependencies
- `softwareSuggestions` (SoftwareSourceCode): Optional dependencies for features or development
- `processorRequirements` (Text): Processor architecture (e.g., IA64)
- `operatingSystem` (Text): Supported operating systems (Windows 7, OSX 10.6, Android 1.6)
- `memoryRequirements` (Text or URL): Minimum memory requirements
- `storageRequirements` (Text or URL): Storage requirements (free space required)
- `fileSize` (Text): Size of application/package (e.g., 18MB)

#### Repository & Distribution
- `codeRepository` (URL): Link to repository (SVN, GitHub, GitLab, CodePlex)
- `downloadUrl` (URL): URL to download binary if file can be downloaded
- `installUrl` (URL): URL where app may be installed
- `fileFormat` (Text or URL): MIME format of software (e.g., application/zip)
- `encoding` (MediaObject): Media object encoding this CreativeWork

#### Licensing & Rights
- `license` (CreativeWork or URL): License document/URL
- `isAccessibleForFree` (Boolean): Flag if publication accessible for free

#### Application Classification
- `applicationCategory` (Text or URL): Type of software (Game, Multimedia)
- `applicationSubCategory` (Text or URL): Subcategory (Arcade Game)
- `targetProduct` (SoftwareApplication): Target Operating System/Product

#### Relationships & References
- `citation` (CreativeWork or URL): Reference to another publication/work
- `hasPart` (CreativeWork): CreativeWork that is part of this CreativeWork
- `isPartOf` (CreativeWork): CreativeWork this is part of (reverse of hasPart)
- `relatedLink` (URL): Related links, e.g., related web pages
- `softwareHelp` (CreativeWork): Software application help documentation

#### Content & Metadata
- `keywords` (Text): Keywords/tags describing content (comma-delimited)
- `permissions` (Text): Required permissions (e.g., internet access, wifi-only)
- `supportingData` (DataFeed): Supporting data for application
- `position` (Integer or Text): Position in series/sequence (way to order arrays)
- `review` (Review): A review of the source code (v3)

### CodeMeta-Specific Extensions (non-Schema.org terms)

These properties fill gaps not covered by Schema.org:

- `buildInstructions` (URL): Link to installation instructions/documentation
- `continuousIntegration` (URL): Link to continuous integration service (v3; v2 used `contIntegration`)
- `developmentStatus` (Text): Development status (active, inactive, suspended) per repostatus.org
- `embargoEndDate` (Date): Embargo period for public access (pending publication, 1 year post-publication)
- `funding` (Text): Funding source (e.g., specific grant)
- `hasSourceCode` (SoftwareSourceCode): Link indicating where software code is located (v3)
- `isSourceCodeOf` (SoftwareApplication): Reverse property - software built from given source code (v3)
- `issueTracker` (URL): Link to bug reporting/issue tracking system
- `readme` (URL): Link to README file

### Person/Organization Properties (for author, contributor, etc.)

**Schema.org Person terms**:
- `address` (PostalAddress or Text): Physical address
- `affiliation` (Organization): Organization person affiliated with
- `email` (Text): Email address
- `familyName` (Text): Family name
- `givenName` (Text): Given name
- `identifier` (URL): ORCID ID preferred for individuals, FundRef ID for funders
- `name` (Text): Full name if separate given/family names unavailable

**Schema.org Role terms** (v3):
- `roleName` (Text or URL): Role played (Design, Architecture, Debugging, Maintenance, Coding, Documentation, Testing, Support, Management)
- `startDate` (Date/Datetime): ISO 8601 format
- `endDate` (Date/Datetime): ISO 8601 format

### Review Properties (v3)
- `reviewBody` (Text): The actual body of the review
- `reviewAspect` (Text): Part or facet of object being reviewed

---

## 2. CITATION.cff (Citation File Format) - https://citation-file-format.github.io/

**Format**: YAML 1.2 plain text files
**Purpose**: Machine- and human-readable citation information for software and datasets
**Version**: Current is 1.2.0

### Required Fields (minimum for valid CFF)
- `cff-version` (string): Version of CFF schema (e.g., "1.2.0")
- `message` (string): Message to display when citing (e.g., "If you use this software, please cite it as below.")
- `title` (string): Software name/title
- `authors` (array): List of author objects

### Core Metadata Fields

#### Basic Information
- `abstract` (string): Brief description of software purpose/functionality
- `contact` (array of person objects): Contact information for authors/maintainers
- `repository` (URL): General repository/homepage URL
- `repository-code` (URL): URL to source code repository (GitHub, GitLab, etc.)
- `repository-artifact` (URL): URL to artifact repository (package registry, Docker Hub, etc.)
- `url` (URL): Project website/landing page

#### Versioning & Dates
- `version` (string): Current version of software (semantic versioning recommended)
- `date-released` (YYYY-MM-DD): Release date
- `commit` (string): Git commit hash for this version

#### Citation & References
- `identifiers` (array): Array of identifier objects:
  - `type` (string): "doi", "url", "other"
  - `value` (string): The actual identifier value
- `doi` (string): Digital Object Identifier (deprecated in favor of identifiers array)
- `preferred-citation` (reference object): Preferred way to cite software
- `references` (array): List of references (publications, standards, software)
  - Each reference can include: `type`, `authors`, `title`, `year`, `doi`, `url`, etc.

#### Licensing & Legal
- `license` (string or array): SPDX identifier(s) (e.g., "Apache-2.0", "MIT")
- `license-url` (URL): URL to full license text (if SPDX not available)

#### Keywords & Classification
- `keywords` (array of strings): Keywords describing software
- `type` (string): "software" or "dataset" (default: "software")

### Person/Entity Fields in CFF

**Person object properties**:
- `family-names` (string): Last name
- `given-names` (string): First/given name
- `name-particle` (string): Particle in name (e.g., "van", "de")
- `name-suffix` (string): Suffix (e.g., "Jr.", "III")
- `orcid` (URL): ORCID identifier (https://orcid.org/XXXX-XXXX-XXXX-XXXX)
- `email` (string): Email address
- `affiliation` (string or object): Organization affiliation
- `address` (string): Physical mailing address
- `city`, `region`, `postal-code`, `country` (strings): Address components
- `website` (URL): Personal/institutional website
- `telephone` (string): Phone number
- `fax` (string): Fax number

**Entity object properties** (for organizations):
- `name` (string): Organization name
- `city`, `region`, `postal-code`, `country` (strings): Address
- `website` (URL): Organization website
- `ror` (URL): Research Organization Registry identifier
- `url` (URL): Alternative to website

### Valid Fields Summary (21 total keys)
`abstract`, `authors`, `cff-version`, `commit`, `contact`, `date-released`, `doi`, `identifiers`, `keywords`, `license`, `license-url`, `message`, `preferred-citation`, `references`, `repository`, `repository-artifact`, `repository-code`, `title`, `type`, `url`, `version`

---

## 3. Software Heritage - https://www.softwareheritage.org/

**Purpose**: Universal source code archive; collects, preserves, and shares software from various sources

### Software Heritage Data Model & Metadata

#### Core Artifacts
Software Heritage's data model is centered around **software artifacts**:
- Source code files and projects
- Version control repositories (Git, SVN, Mercurial, etc.)
- Software releases and snapshots
- Metadata about source code origin

#### Two Types of Metadata

**Intrinsic Metadata**: Embedded in source code itself
- Found in specific files (e.g., README, setup.py, package.json, codemeta.json)
- Includes version, author, license information in source

**Extrinsic Metadata**: Not in source code
- Platform-specific information (GitHub stars, creation date)
- Aggregated metadata from registries
- Harvested from external sources

#### Preservation Model
- Uses **Merkle-directed acyclic graph**: Combines tree structure with cryptographic hash functions
- **Universal source code archive**: Converts all collected source code into single universal data structure
- **Provenance tracking**: Full information stored about where software was found
- **Metadata translation**: Converts to CodeMeta format for indexing and sharing

#### Indexed Metadata Storage
- Stores harvested source code in standardized structure
- Metadata indexed using CodeMeta translation
- Enables cross-platform discovery and reuse

#### Software Artifact Identification
- Content-based identification (hash-based)
- Repository origin metadata
- Version/release information
- Authorship and licensing data

---

## 4. Schema.org SoftwareSourceCode and SoftwareApplication

**Official Reference**: https://schema.org/SoftwareSourceCode and https://schema.org/SoftwareApplication

### SoftwareSourceCode Properties

Inherits from CreativeWork and extends with:
- All properties listed in CodeMeta (Section 1 above)
- Primary focus: source code, development, technical specifications
- Emphasizes: repository, programming language, dependencies, requirements

### SoftwareApplication Properties

Inherits from CreativeWork and extends with:
- All properties listed in CodeMeta (Section 1 above)
- Primary focus: packaged, distributable applications
- Emphasizes: operating system, download URL, installation, application category

### Key Distinctions
- **SoftwareSourceCode**: Emphasizes version control repository, developer-facing metadata
- **SoftwareApplication**: Emphasizes distributable package, end-user-facing metadata
- **Both**: Share 50+ properties from Schema.org and CodeMeta extension

### Notable Software-Specific Properties
- `applicationCategory` (application)
- `applicationSubCategory` (application)
- `operatingSystem` (both)
- `runtimePlatform` (both)
- `softwareRequirements` (both)
- `processorRequirements` (both)
- `memoryRequirements` (both)
- `storageRequirements` (both)
- `codeRepository` (both)

---

## 5. Zenodo Software Metadata

**Platform**: https://zenodo.org/
**Purpose**: Preserve and share research data and software with digital object identifiers (DOIs)

### Software Deposit Metadata Fields

#### Basic Required Metadata
- **Title**: Main software name
- **Creators/Authors**: List of creators
- **Publication date**: When release was made public
- **License**: Rights and licensing (supports SPDX)

#### Recommended Metadata
- **Additional titles**: Subtitle, alternative names
- **Keywords**: Subject keywords
- **Description/Abstract**: Detailed description
- **Version**: Software version number
- **Language**: Programming language or language of documentation
- **Contributors**: Additional contributors with roles
- **Funding information**: Grants and funding sources
- **Related identifiers**: Related publications, datasets, other versions

#### Format Support
- Recognizes **CITATION.cff** files in GitHub repositories
- Parses **.zenodo.json** metadata files
- Integrates with GitHub releases → Zenodo preservation workflow
- Supports CodeMeta format for mapping

#### DOI & Persistent Identifier
- Assigns DOI to each software release
- Enables software citation
- Preserves specific version for reproducibility

#### GitHub Integration
- Automatic deposit on tagged release from GitHub
- Parses CITATION.cff and .zenodo.json for metadata
- Links GitHub repository to Zenodo record

#### Software-Specific Fields (CodeMeta-based)
- **Programming language(s)**
- **Software dependencies**
- **Runtime platform**
- **Operating system compatibility**
- **Development status**
- **Issue tracker URL**
- **Code repository URL**

---

## 6. Mapping Matrix: Field Coverage Across Standards

| Field Category | CodeMeta | CFF | Schema.org | Zenodo | SWH |
|---|---|---|---|---|---|
| **Identification** |
| Name/Title | ✓ | ✓ | ✓ | ✓ | ✓ |
| Description/Abstract | ✓ | ✓ | ✓ | ✓ | ✓ |
| Identifiers (DOI, UUID) | ✓ | ✓ | ✓ | ✓ | ✓ |
| URL/Website | ✓ | ✓ | ✓ | ✓ | - |
| **Authors & Attribution** |
| Author(s) | ✓ | ✓ | ✓ | ✓ | ✓ |
| Contributor(s) | ✓ | ✓ | ✓ | ✓ | ✓ |
| Maintainer | ✓ | - | ✓ | - | - |
| Funder/Sponsor | ✓ | - | ✓ | ✓ | - |
| Copyright Holder | ✓ | - | ✓ | - | - |
| **Versioning** |
| Version | ✓ | ✓ | ✓ | ✓ | ✓ |
| Release Date | ✓ | ✓ | ✓ | ✓ | ✓ |
| Git Commit | - | ✓ | - | - | ✓ |
| Release Notes | ✓ | - | ✓ | - | - |
| **Technical Specs** |
| Programming Language(s) | ✓ | - | ✓ | ✓ | - |
| Dependencies/Requirements | ✓ | - | ✓ | ✓ | - |
| Runtime Platform | ✓ | - | ✓ | ✓ | - |
| Operating System | ✓ | - | ✓ | ✓ | - |
| Processor Requirements | ✓ | - | ✓ | - | - |
| Memory Requirements | ✓ | - | ✓ | - | - |
| Storage Requirements | ✓ | - | ✓ | - | - |
| **Repository & Distribution** |
| Repository URL | ✓ | ✓ | ✓ | ✓ | ✓ |
| Code Repository | ✓ | ✓ | ✓ | ✓ | ✓ |
| Download URL | ✓ | - | ✓ | - | - |
| Artifact Repository | - | ✓ | - | - | - |
| **Build & CI/CD** |
| Build Instructions | ✓ | - | - | - | - |
| Continuous Integration | ✓ | - | - | - | - |
| Issue Tracker | ✓ | - | - | - | - |
| **Licensing** |
| License(s) | ✓ | ✓ | ✓ | ✓ | ✓ |
| Copyright Year | ✓ | - | ✓ | - | - |
| **Content & Metadata** |
| Keywords | ✓ | ✓ | ✓ | ✓ | - |
| Citation(s) | ✓ | ✓ | ✓ | ✓ | - |
| Related Publications | ✓ | ✓ | ✓ | ✓ | - |
| README | ✓ | - | - | - | - |
| Development Status | ✓ | - | - | ✓ | - |
| **Specialized** |
| Software Help | ✓ | - | ✓ | - | - |
| Review | ✓ | - | ✓ | - | - |
| Provenance | - | - | - | - | ✓ |
| Embargo Date | ✓ | - | - | - | - |

---

## 7. Key Fields for LinkML CodeRepository & Software Schema

Based on comprehensive analysis, recommended fields for a unified LinkML schema:

### Core Software Identity
```
name: string (required)
description: string (required)
abstract: string
url: URL
identifier: string or PropertyValue (DOI, UUID, etc.)
keywords: array[string]
version: string (semantic versioning)
```

### Authorship & Attribution
```
authors: array[Person]
contributors: array[Person]
maintainers: array[Person]
funders: array[Organization]
copyrightHolder: Organization or Person
copyrightYear: integer
```

### Temporal
```
dateCreated: date
dateModified: date
datePublished: date
dateReleased: date
```

### Technical Specifications
```
programmingLanguages: array[string]
softwareRequirements: array[SoftwareSourceCode]
softwareSuggestions: array[SoftwareSourceCode] (optional)
runtimePlatforms: array[string]
operatingSystems: array[string]
processorRequirements: string
memoryRequirements: string
storageRequirements: string
```

### Repository & Distribution
```
codeRepository: URL
downloadUrl: URL
artifactRepository: URL
installUrl: URL
fileFormat: string (MIME type)
fileSize: string
```

### Build & Development
```
buildInstructions: URL
continuousIntegration: URL
issueTracker: URL
developmentStatus: enum (active, inactive, suspended)
readme: URL
```

### Citation & References
```
references: array[CitationObject]
relatedPublications: array[CreativeWork]
relatedDatasets: array[DataFeed]
preferredCitation: Citation
citations: array[CitationObject]
```

### Licensing & Rights
```
licenses: array[string] (SPDX identifiers)
licenseUrl: URL
isAccessibleForFree: boolean
```

### Application Classification (optional)
```
applicationCategory: string
applicationSubCategory: string
targetProducts: array[SoftwareApplication]
```

### Advanced Metadata
```
review: array[Review]
hasSourceCode: array[SoftwareSourceCode]
isSourceCodeOf: array[SoftwareApplication]
hasPart: array[CreativeWork]
isPartOf: array[CreativeWork]
relatedLinks: array[URL]
supportingData: array[DataFeed]
funding: array[string or FundingObject]
embargoEndDate: date
provenance: object (Software Heritage)
```

---

## 8. Interoperability: Crosswalk Recommendations

### CodeMeta ↔ CFF Conversion
- CodeMeta → CFF: Map codemeta.json properties to CITATION.cff YAML
- CFF → CodeMeta: Converter tools available (cff-converter-python)
- Both support author, license, version, URL, identifier fields

### CodeMeta ↔ Zenodo
- Zenodo metadata fields derived from CodeMeta
- Software deposits use CodeMeta-based fields
- CITATION.cff parsed automatically on Zenodo deposit

### Software Heritage Integration
- Ingests CodeMeta from codemeta.json files
- Translates intrinsic metadata to CodeMeta
- Preserves both extrinsic and intrinsic metadata

### Schema.org Alignment
- CodeMeta built on Schema.org foundation
- CFF maps to Schema.org through CodeMeta
- Zenodo and Software Heritage use Schema.org/CodeMeta mapping

---

## Sources

1. CodeMeta Terms Documentation: [https://codemeta.github.io/terms/](https://codemeta.github.io/terms/)
2. CodeMeta Project Home: [https://codemeta.github.io/](https://codemeta.github.io/)
3. Citation File Format (CFF): [https://citation-file-format.github.io/](https://citation-file-format.github.io/)
4. CFF Schema Guide: [Guide to Citation File Format schema version 1.2.0](https://elib.dlr.de/147385/1/schema-guide.pdf)
5. CFF Schema Repository: [https://github.com/citation-file-format/schema](https://github.com/citation-file-format/schema)
6. Software Heritage: [https://www.softwareheritage.org/](https://www.softwareheritage.org/)
7. Software Heritage Data Model: [https://docs.softwareheritage.org/devel/swh-model/data-model.html](https://docs.softwareheritage.org/devel/swh-model/data-model.html)
8. Software Heritage Metadata Deep Dive: [https://www.softwareheritage.org/2023/08/24/archival-of-software-metadata/](https://www.softwareheritage.org/2023/08/24/archival-of-software-metadata/)
9. Schema.org SoftwareSourceCode: [https://schema.org/SoftwareSourceCode](https://schema.org/SoftwareSourceCode)
10. Schema.org SoftwareApplication: [https://schema.org/SoftwareApplication](https://schema.org/SoftwareApplication)
11. Zenodo Software Deposits: [https://help.zenodo.org/docs/github/describe-software/](https://help.zenodo.org/docs/github/describe-software/)
12. Zenodo Help Documentation: [https://help.zenodo.org/docs/deposit/](https://help.zenodo.org/docs/deposit/)
