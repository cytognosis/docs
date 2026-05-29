# CodeMeta & CFF Field Examples and Technical Reference

## 1. CodeMeta JSON-LD Example

```json
{
  "@context": "https://w3id.org/codemeta/3.0/context.jsonld",
  "@type": "SoftwareSourceCode",
  "name": "My Research Software",
  "description": "A Python package for analyzing climate data with advanced statistical methods.",
  "identifier": "https://doi.org/10.5281/zenodo.1234567",
  "codeRepository": "https://github.com/myorg/myproject",
  "url": "https://myproject.example.org",
  "version": "2.0.4",
  "softwareVersion": "2.0.4",
  "issueTracker": "https://github.com/myorg/myproject/issues",
  "readme": "https://github.com/myorg/myproject/blob/main/README.md",
  "downloadUrl": "https://github.com/myorg/myproject/releases/download/v2.0.4/myproject-2.0.4.tar.gz",
  "license": "https://opensource.org/licenses/MIT",
  "copyrightHolder": {
    "@type": "Organization",
    "name": "Research Institute"
  },
  "copyrightYear": 2021,
  "dateCreated": "2020-01-15",
  "dateModified": "2023-11-20",
  "datePublished": "2023-11-20",
  "releaseNotes": "Added GPU acceleration and improved memory efficiency in v2.0.0",
  "programmingLanguage": [
    {
      "@type": "ComputerLanguage",
      "name": "Python",
      "url": "https://www.python.org/",
      "version": "3.8+"
    }
  ],
  "runtimePlatform": "Python 3.8+",
  "operatingSystem": ["Linux", "macOS", "Windows"],
  "processorRequirements": "x86_64",
  "memoryRequirements": "2GB minimum, 8GB recommended",
  "storageRequirements": "500MB for installation, plus data files",
  "softwareRequirements": [
    {
      "@type": "SoftwareSourceCode",
      "name": "numpy",
      "url": "https://numpy.org/",
      "version": ">=1.19.0"
    },
    {
      "@type": "SoftwareSourceCode",
      "name": "scipy",
      "url": "https://scipy.org/",
      "version": ">=1.5.0"
    },
    {
      "@type": "SoftwareSourceCode",
      "name": "pandas",
      "url": "https://pandas.pydata.org/",
      "version": ">=1.0.0"
    }
  ],
  "softwareSuggestions": [
    {
      "@type": "SoftwareSourceCode",
      "name": "jupyter",
      "url": "https://jupyter.org/",
      "description": "Optional: for interactive notebook support"
    },
    {
      "@type": "SoftwareSourceCode",
      "name": "matplotlib",
      "url": "https://matplotlib.org/",
      "description": "Optional: for visualization"
    }
  ],
  "buildInstructions": "https://github.com/myorg/myproject/blob/main/INSTALL.md",
  "continuousIntegration": "https://github.com/myorg/myproject/actions",
  "developmentStatus": "active",
  "keywords": [
    "climate-science",
    "data-analysis",
    "statistics",
    "machine-learning"
  ],
  "author": [
    {
      "@type": "Person",
      "givenName": "Jane",
      "familyName": "Smith",
      "email": "jane@example.org",
      "affiliation": {
        "@type": "Organization",
        "name": "University of Example",
        "url": "https://example.edu"
      },
      "identifier": "https://orcid.org/0000-0001-2345-6789"
    }
  ],
  "contributor": [
    {
      "@type": "Person",
      "givenName": "John",
      "familyName": "Doe",
      "email": "john@example.org",
      "affiliation": {
        "@type": "Organization",
        "name": "Example Lab"
      }
    }
  ],
  "maintainer": {
    "@type": "Person",
    "givenName": "Jane",
    "familyName": "Smith",
    "email": "jane@example.org"
  },
  "funder": {
    "@type": "Organization",
    "name": "National Science Foundation",
    "url": "https://www.nsf.gov/",
    "identifier": "https://ror.org/021nxhr62"
  },
  "funding": "Grant #NSF-1234567",
  "referencePublication": [
    {
      "@type": "ScholarlyArticle",
      "name": "Advanced Climate Analysis Methods",
      "author": [
        {
          "@type": "Person",
          "givenName": "Jane",
          "familyName": "Smith"
        }
      ],
      "datePublished": "2021",
      "doi": "https://doi.org/10.1234/example",
      "url": "https://example.org/publication"
    }
  ],
  "citation": [
    {
      "@type": "CreativeWork",
      "name": "Climate Data Standard Format",
      "url": "https://climatestd.example.org/"
    }
  ],
  "relatedLink": [
    "https://myproject.example.org/docs",
    "https://github.com/myorg/myproject/wiki"
  ],
  "publisher": {
    "@type": "Organization",
    "name": "Example Publishing"
  },
  "sameAs": [
    "https://www.wikidata.org/wiki/Q123456",
    "https://en.wikipedia.org/wiki/My_Research_Software"
  ],
  "applicationCategory": "Scientific Software",
  "softwareHelp": {
    "@type": "CreativeWork",
    "name": "User Guide",
    "url": "https://myproject.example.org/docs/guide"
  },
  "supportingData": {
    "@type": "DataFeed",
    "name": "Example Climate Dataset",
    "url": "https://data.example.org/climate"
  }
}
```

---

## 2. CITATION.cff Example (Full)

```yaml
cff-version: 1.2.0
type: software
message: >-
  If you use this software, please cite it using the metadata from this file.
  Cite as: Smith et al., (2023). My Research Software: A climate data analysis toolkit.
  Journal of Software Tools, 15(3), 456. https://doi.org/10.1234/journal.2023.15.456

title: "My Research Software"
abstract: >-
  A comprehensive Python package for analyzing climate data with advanced
  statistical methods. Supports multi-dimensional data processing, time series
  analysis, and machine learning integration.

authors:
  - family-names: Smith
    given-names: Jane
    orcid: "https://orcid.org/0000-0001-2345-6789"
    affiliation: "University of Example"
    email: "jane@example.org"
    website: "https://jane.example.org"

  - family-names: Doe
    given-names: John
    email: "john@example.org"
    affiliation:
      name: "Example Lab"
      city: "Boston"
      country: "US"

contact:
  - family-names: Smith
    given-names: Jane
    email: "jane@example.org"
    website: "https://jane.example.org"

keywords:
  - "climate-science"
  - "data-analysis"
  - "python"
  - "statistics"
  - "machine-learning"

version: "2.0.4"
date-released: "2023-11-20"
repository-code: "https://github.com/myorg/myproject"
repository-artifact: "https://pypi.org/project/myproject/"
url: "https://myproject.example.org"

license: "MIT"
license-url: "https://opensource.org/licenses/MIT"

identifiers:
  - type: "doi"
    value: "10.5281/zenodo.1234567"
  - type: "url"
    value: "https://github.com/myorg/myproject"

commit: "abc123def456"

preferred-citation:
  type: journal-article
  authors:
    - family-names: Smith
      given-names: Jane
    - family-names: Doe
      given-names: John
  title: "Advanced Climate Analysis Methods"
  journal: "Journal of Software Tools"
  volume: 15
  issue: 3
  pages: "456-470"
  year: 2023
  doi: "10.1234/journal.2023.15.456"
  url: "https://journal.example.org/2023/15/456"

references:
  - type: software
    authors:
      - family-names: "Numpy Contributors"
    title: "NumPy"
    url: "https://numpy.org/"
    version: "1.19.0"

  - type: journal-article
    authors:
      - family-names: McKinney
        given-names: Wes
    title: "Data Structures for Statistical Computing in Python"
    journal: "Proceedings of the 9th Python in Science Conference"
    year: 2010
    doi: "10.25080/Majora-92bf1922-00a"

  - type: standard
    title: "Climate and Forecast Metadata Conventions"
    url: "http://cfconventions.org/"
```

---

## 3. Field-by-Field Mapping: CodeMeta Properties

### Essential Properties (implement first)

| CodeMeta Property | Type | Example | Notes |
|---|---|---|---|
| `name` | string | "My Research Software" | Required; software title |
| `description` | string | "A Python package for..." | Required; brief summary |
| `version` | string | "2.0.4" | Version number (semantic versioning) |
| `identifier` | PropertyValue or URL | "10.5281/zenodo.1234567" | DOI, UUID, or other unique ID |
| `url` | URL | "https://myproject.example.org" | Project website |
| `codeRepository` | URL | "https://github.com/myorg/myproject" | Link to source code |
| `license` | URL or CreativeWork | "https://opensource.org/licenses/MIT" | License URL or SPDX name |
| `author` | Person or Organization | See Person example | Primary author(s) |
| `datePublished` | Date | "2023-11-20" | Publication date |
| `keywords` | array[string] | ["climate", "data-analysis"] | Subject tags |

### Recommended Properties

| CodeMeta Property | Type | Example | Notes |
|---|---|---|---|
| `programmingLanguage` | ComputerLanguage or Text | {"name": "Python", "version": "3.8+"} | Implementation language(s) |
| `softwareRequirements` | array[SoftwareSourceCode] | See example above | Required dependencies |
| `operatingSystem` | array[string] | ["Linux", "macOS", "Windows"] | Supported OS |
| `runtimePlatform` | string | "Python 3.8+" | Runtime environment |
| `releaseNotes` | URL or Text | "Added GPU acceleration..." | Version change notes |
| `contributor` | array[Person] | See Person example | Contributors beyond authors |
| `maintainer` | Person | See Person example | Primary maintainer contact |
| `funder` | Organization or Person | {"name": "NSF"} | Financial supporters |
| `issueTracker` | URL | "https://github.com/.../issues" | Bug reporting system |
| `continuousIntegration` | URL | "https://github.com/.../actions" | CI/CD pipeline |
| `buildInstructions` | URL | "https://github.com/.../INSTALL.md" | Installation guide |
| `referencePublication` | array[ScholarlyArticle] | See example above | Related publications |
| `developmentStatus` | string (enum) | "active" or "inactive" | Status per repostatus.org |
| `readme` | URL | "https://github.com/.../README.md" | README file location |

### Optional but Valuable Properties

| CodeMeta Property | Type | Example | Notes |
|---|---|---|---|
| `softwareSuggestions` | array[SoftwareSourceCode] | Optional dependencies | Features requiring extra software |
| `memoryRequirements` | string | "2GB minimum, 8GB recommended" | System requirements |
| `storageRequirements` | string | "500MB + data files" | Disk space needed |
| `processorRequirements` | string | "x86_64" | CPU architecture |
| `downloadUrl` | URL | "https://github.com/.../releases" | Download location |
| `copyrightHolder` | Organization or Person | {"name": "Research Institute"} | Copyright owner |
| `copyrightYear` | integer | 2023 | Copyright year |
| `dateCreated` | Date | "2020-01-15" | Project start date |
| `dateModified` | Date | "2023-11-20" | Last modification date |
| `sameAs` | array[URL] | [Wikidata, Wikipedia links] | Canonical identifiers |
| `hasPart` | array[CreativeWork] | Sub-modules or plugins | Composite projects |
| `isPartOf` | CreativeWork | Parent project reference | If part of larger project |
| `applicationCategory` | string | "Scientific Software" | Application classification |
| `supportingData` | DataFeed | Climate dataset reference | Associated datasets |
| `review` | array[Review] | Peer review records | Code review information |

---

## 4. Person Object Structure

### Minimal Person
```json
{
  "@type": "Person",
  "name": "Jane Smith"
}
```

### Standard Person
```json
{
  "@type": "Person",
  "givenName": "Jane",
  "familyName": "Smith",
  "email": "jane@example.org",
  "identifier": "https://orcid.org/0000-0001-2345-6789"
}
```

### Extended Person
```json
{
  "@type": "Person",
  "givenName": "Jane",
  "familyName": "Smith",
  "nameParticle": "von",
  "nameSuffix": "Jr.",
  "email": "jane@example.org",
  "url": "https://jane.example.org",
  "identifier": "https://orcid.org/0000-0001-2345-6789",
  "affiliation": {
    "@type": "Organization",
    "name": "University of Example",
    "url": "https://example.edu",
    "address": {
      "@type": "PostalAddress",
      "streetAddress": "123 Example St",
      "addressCity": "Boston",
      "addressRegion": "MA",
      "postalCode": "02101",
      "addressCountry": "US"
    }
  }
}
```

### In CFF Format (YAML)
```yaml
authors:
  - family-names: Smith
    given-names: Jane
    name-particle: von
    name-suffix: Jr.
    orcid: "https://orcid.org/0000-0001-2345-6789"
    email: jane@example.org
    website: https://jane.example.org
    affiliation: "University of Example"
    address:
      street-address: "123 Example St"
      city: Boston
      region: MA
      postal-code: "02101"
      country: US
```

---

## 5. ComputerLanguage Object

```json
{
  "@type": "ComputerLanguage",
  "name": "Python",
  "url": "https://www.python.org/",
  "version": "3.8+",
  "identifier": "https://www.wikidata.org/wiki/Q28865"
}
```

---

## 6. SoftwareSourceCode (Dependency) Object

```json
{
  "@type": "SoftwareSourceCode",
  "name": "numpy",
  "url": "https://numpy.org/",
  "version": ">=1.19.0",
  "description": "Fundamental package for array computing",
  "license": "BSD-3-Clause",
  "identifier": "https://doi.org/10.5281/zenodo.3897577"
}
```

---

## 7. ScholarlyArticle (Reference Publication)

```json
{
  "@type": "ScholarlyArticle",
  "name": "Advanced Climate Analysis Methods",
  "author": [
    {
      "@type": "Person",
      "givenName": "Jane",
      "familyName": "Smith"
    }
  ],
  "datePublished": "2023-11-20",
  "journal": "Journal of Software Tools",
  "volume": "15",
  "issue": "3",
  "pages": "456-470",
  "doi": "https://doi.org/10.1234/journal.2023.15.456",
  "url": "https://journal.example.org/2023/15/456"
}
```

---

## 8. Organization Object

```json
{
  "@type": "Organization",
  "name": "National Science Foundation",
  "url": "https://www.nsf.gov/",
  "identifier": "https://ror.org/021nxhr62",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "2415 Eisenhower Avenue",
    "addressCity": "Alexandria",
    "addressRegion": "VA",
    "postalCode": "22314",
    "addressCountry": "US"
  }
}
```

---

## 9. Review Object (CodeMeta v3)

```json
{
  "@type": "Review",
  "reviewBody": "Well-structured code with comprehensive test coverage. Documentation could be improved.",
  "reviewAspect": "Code Quality"
}
```

---

## 10. Key Differences: CodeMeta vs CFF vs Schema.org

| Aspect | CodeMeta | CFF | Schema.org |
|---|---|---|---|
| **Format** | JSON-LD | YAML | JSON or Microdata |
| **Expressiveness** | Rich, complex structures | Simple, human-readable | Flexible but verbose |
| **Ideal Use Case** | Software registry indexing | Human-managed citation | Web semantic markup |
| **Person Fields** | Separate object types | Embedded objects | Inline structured data |
| **Nested Objects** | Extensive support | Limited nesting | Deep nesting possible |
| **Tool Support** | Many converters | GitHub, Zenodo native | Web crawler friendly |
| **Validation** | JSON Schema | YAML Schema | Schema.org vocabulary |
| **Best For** | Archival, discovery, interop | Human editing, version control | SEO, web indexing |

---

## 11. Conversion Pathways

### CodeMeta JSON-LD → CITATION.cff (YAML)

Key mappings:
- `codemeta.name` → `cff.title`
- `codemeta.description` → `cff.abstract`
- `codemeta.author[*]` → `cff.authors[*]`
- `codemeta.identifier` → `cff.identifiers[*]` (convert DOI format)
- `codemeta.codeRepository` → `cff.repository-code`
- `codemeta.license` → `cff.license` (extract SPDX name)
- `codemeta.version` → `cff.version`
- `codemeta.datePublished` → `cff.date-released`
- `codemeta.referencePublication[*]` → `cff.references[*]`

### CFF → CodeMeta JSON-LD

- `cff.title` → `codemeta.name`
- `cff.abstract` → `codemeta.description`
- `cff.authors` → `codemeta.author`
- `cff.keywords` → `codemeta.keywords`
- `cff.license` → `codemeta.license` (construct URL)
- `cff.version` → `codemeta.version`

Tool: [cff-converter-python](https://github.com/citation-file-format/cff-converter-python)

---

## 12. SPDX License Identifiers (Common)

```
MIT
Apache-2.0
GPL-2.0-only
GPL-2.0-or-later
GPL-3.0-only
GPL-3.0-or-later
BSD-2-Clause
BSD-3-Clause
LGPL-2.1-only
LGPL-2.1-or-later
LGPL-3.0-only
LGPL-3.0-or-later
ISC
MPL-2.0
AGPL-3.0-only
AGPL-3.0-or-later
Unlicense
CC0-1.0 (public domain)
```

See: [SPDX License List](https://spdx.org/licenses/)

---

## 13. Semantic Versioning in CodeMeta/CFF

Recommended format: `MAJOR.MINOR.PATCH[-PRERELEASE][+BUILD]`

Examples:
- `1.0.0` - Initial release
- `2.1.0` - New features, backward compatible
- `2.1.1` - Bug fix, backward compatible
- `2.0.0` - Breaking changes
- `2.0.0-alpha.1` - Pre-release
- `2.0.0-rc.1` - Release candidate
- `2.0.0+20230115` - Build metadata

---

## 14. Development Status Values (repostatus.org)

```
active          - Development is active
inactive        - Development has stopped
suspended       - Development is temporarily suspended
abandoned       - Development has been abandoned
unsupported     - Software is no longer supported
moved           - Development has moved elsewhere
transitional    - Transitioning to new owner/maintainer
concept         - Concept/early prototype only
wip             - Work in progress
```

---

## 15. Test Framework & CI/CD Examples in CodeMeta

### Continuous Integration URL Examples
```
https://github.com/myorg/myproject/actions
https://travis-ci.com/myorg/myproject
https://circleci.com/gh/myorg/myproject
https://app.travis-ci.com/github/myorg/myproject
```

### Test Framework References (as SoftwareSuggestions)
```json
{
  "@type": "SoftwareSourceCode",
  "name": "pytest",
  "url": "https://pytest.org/",
  "version": ">=6.0",
  "description": "Python testing framework"
}
```

### Build System References
```json
{
  "@type": "SoftwareSourceCode",
  "name": "setuptools",
  "url": "https://setuptools.pypa.io/",
  "description": "Build system"
}
```

---

## 16. Related Datasets & Publications Links

### Supporting Dataset Example
```json
{
  "@type": "DataFeed",
  "name": "Climate Benchmark Dataset v2.0",
  "url": "https://zenodo.org/record/123456",
  "identifier": "https://doi.org/10.5281/zenodo.123456",
  "datePublished": "2023-06-01",
  "creator": {
    "@type": "Organization",
    "name": "Climate Data Center"
  }
}
```

### Related Publication Example
```json
{
  "@type": "ScholarlyArticle",
  "name": "Software Architecture for Climate Analysis",
  "author": [{
    "@type": "Person",
    "name": "Jane Smith"
  }],
  "datePublished": "2022-03-15",
  "journal": "Journal of Scientific Software",
  "doi": "https://doi.org/10.1234/example.2022"
}
```

---

## Sources

- CodeMeta Terms: https://codemeta.github.io/terms/
- CodeMeta JSON-LD Context: https://w3id.org/codemeta/3.0/context.jsonld
- Citation File Format 1.2.0: https://citation-file-format.github.io/
- CFF Schema Guide: https://github.com/citation-file-format/citation-file-format/blob/main/schema-guide.md
- Schema.org SoftwareSourceCode: https://schema.org/SoftwareSourceCode
- SPDX Licenses: https://spdx.org/licenses/
- Repostatus: http://www.repostatus.org/
