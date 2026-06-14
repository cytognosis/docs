# Data Management Plan Template

> **Version**: 1.0.0
> **Aligned with**: Horizon Europe DMP requirements, FAIR Guiding Principles, NIH Data Management and Sharing Policy, OpenAIRE RDM best practices, HIPAA Security Rule
> **Applicable to**: All Cytognosis Foundation research projects generating, reusing, or processing research data

> [!NOTE]
> **Implementation status**: This template is complete and ready for use.
> The first DMP to be written from this template will be for the **Neuroverse program**.
> See [Neuroverse datasets](../../programs/neuroverse/datasets-cohorts.md) for the cohorts
> that will populate sections 2.1 and 2.3 of the DMP.

## Instructions

This template follows the [European Commission Horizon Europe DMP template](https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/temp-form/report/data-management-plan_he_en.docx) structure and integrates guidance from the [OpenAIRE RDM compliance guide](https://www.openaire.eu/how-to-comply-with-horizon-europe-mandate-for-rdm), the [OpenAIRE FAIR data guide](https://www.openaire.eu/how-to-make-your-data-fair), and the [Utrecht University DMP planning guide](https://www.uu.nl/en/research/research-data-management/guides/data-management-planning).

Complete each section below. Replace `[placeholder]` text with project-specific information. Sections marked with **(HIPAA)** require additional review by the HIPAA Security Officer. Sections marked with **(FAIR)** map directly to FAIR sub-principles.

A DMP is a living document. Update it whenever significant changes arise (new data types, revised access conditions, repository changes). At minimum:

- **Month 0**: Initial draft (proposal-stage summary)
- **Month 6**: Full DMP deliverable
- **Quarterly**: Review and update as needed
- **Project end**: Final DMP reflecting actual data management outcomes

---

## 1. Project Overview

### 1.1 Administrative Information

| Field | Value |
| --- | --- |
| Project title | [title] |
| Project acronym | [acronym] |
| Grant/funding reference | [grant number, funder name] |
| Project start date | [YYYY-MM-DD] |
| Project end date | [YYYY-MM-DD] |
| DMP version | [e.g. 1.0] |
| DMP last updated | [YYYY-MM-DD] |
| Principal investigator | [name, ORCID iD, affiliation] |
| Data steward / contact | [name, email] |
| HIPAA Security Officer | [name, email] |

### 1.2 Project Summary

Provide a brief description (3-5 sentences) of the project, its objectives, and the role of data in achieving them.

> [project summary]

---

## 2. Data Description

### 2.1 Data Types and Formats

For each dataset or data category the project will generate or reuse, complete the table below.

| Dataset ID | Name / Description | Type | Format(s) | Estimated Size | Origin | Sensitivity Level |
| --- | --- | --- | --- | --- | --- | --- |
| DS-001 | [e.g. Single-cell RNA-seq] | [Genomic] | [AnnData (.h5ad), FASTQ] | [~500 GB] | [Generated / Reused] | [Public / Internal / Controlled / PHI] |
| DS-002 | [e.g. Clinical phenotypes] | [Clinical] | [FHIR R4 JSON, CSV] | [~2 GB] | [Reused from NDA] | [PHI] |
| DS-003 | [e.g. Trained ML models] | [Model] | [ONNX, PyTorch .pt] | [~50 GB] | [Generated] | [Internal] |

> **Guidance**: Use open, non-proprietary formats where possible (CSV/TSV, JSON, HDF5, Parquet, ONNX). If proprietary formats are required for collection (e.g., vendor instrument output), document the conversion pipeline to an open format. See the [Cytognosis Multimodal Health Data Schema](../schemas/multimodal-health-data-schema.md) for canonical format specifications and the [Tools Catalog — L1 Storage](../../tools/tools-master-catalog.md#l1-storage) for approved storage formats (TileDB, Zarr v3, AnnData/h5ad, Safetensors, GGUF, Parquet). The [Storage Hierarchy](../../tools/tools-master-catalog.md#storage-hierarchy-by-data-type) and [Dataset Versioning by Scale](../../tools/tools-master-catalog.md#dataset-versioning-by-scale) tables specify which tools to use at each data-lifecycle stage.

### 2.2 Data Classification **(HIPAA)**

All data must be classified according to the [Cytognosis Data Governance Policy](../policies/data-governance-policy.md):

| Level | Definition | Examples | Storage Requirement |
| --- | --- | --- | --- |
| **Public** | No restrictions on access or sharing | Published datasets, open-source code, aggregated statistics | Any approved storage |
| **Internal** | For internal use; no PHI or PII | Intermediate analysis results, draft manuscripts, internal reports | Cytognosis-controlled infrastructure |
| **Controlled** | Subject to access agreements (DUA, MTA) | NIH NDA datasets, dbGaP, UK Biobank extracts | Isolated GCP project with audit logging |
| **PHI** | Protected Health Information under HIPAA | Patient records, identifiable genomic data, clinical notes | `cytognosis-phi-prod` with full HIPAA controls |

### 2.3 Existing Data Reuse

For each reused dataset, document:

| Dataset | Source | Access mechanism | License / DUA | Restrictions |
| --- | --- | --- | --- | --- |
| [e.g. ADNI neuroimaging] | [LONI portal] | [Approved DUA #XYZ] | [ADNI DUA v3] | [No redistribution; derived data inherits restrictions] |

---

## 3. FAIR Data Principles

### 3.1 Making Data Findable **(FAIR: F1-F4)**

- **Persistent identifiers**: All deposited datasets will receive a DOI via [Zenodo / institutional repository]. Code repositories use GitHub with Zenodo DOI integration. Researchers are identified via ORCID iD.
- **Rich metadata**: Each dataset record will include at minimum: author(s), description/abstract, date of deposit, license, keywords, funder information (grant name, acronym, number), related publications (via DOI), and methodology summary.
- **Metadata standards**: [Specify standards, e.g., Dublin Core, DataCite Metadata Schema, ISA-Tab for omics, MIAME for microarrays, MINSEQE for sequencing]. Domain-specific standards are identified via [FAIRsharing](https://fairsharing.org/) and the [RDA Metadata Standards Catalog](https://rdamsc.bath.ac.uk/).
- **Searchable resource**: Data records will be registered in [repository name] which is indexed by [OpenAIRE EXPLORE / Google Dataset Search / DataCite Commons / re3data].

### 3.2 Making Data Accessible **(FAIR: A1-A2)**

- **Access protocol**: Data are retrievable via HTTPS. APIs are documented with OpenAPI specifications where applicable.
- **Authentication**: [Describe access controls, e.g., "Public datasets: anonymous HTTPS. Controlled datasets: institutional SSO via InCommon federation. PHI datasets: VPN + MFA + role-based access within cytognosis-phi-prod GCP project."]
- **Metadata persistence**: Metadata records remain publicly accessible even if the underlying data are restricted, embargoed, or removed. Repository selection criteria include long-term metadata preservation commitments.
- **Embargo period**: [If applicable, specify embargo duration and justification, e.g., "12 months post-publication for competitive advantage on derivative models."]

### 3.3 Making Data Interoperable **(FAIR: I1-I3)**

- **Open formats**: Primary data outputs use open, documented file formats (see section 2.1). Conversion scripts from proprietary formats are version-controlled in the project repository.
- **Vocabularies and ontologies**: [List controlled vocabularies, e.g., "Gene Ontology (GO), Human Phenotype Ontology (HPO), Cell Ontology (CL), MONDO Disease Ontology, SNOMED CT, UMLS, CHEBI, NCBITaxon"]. Cross-ontology mappings follow the [SSSOM specification](../sssom-cross-ontology-mapping.md).
- **Qualified references**: Datasets link to related entities via PIDs: article DOIs, ORCID iDs, ROR IDs for institutions, grant IDs, and software DOIs. Relationship types use CiTO or DataCite relation types.

### 3.4 Making Data Reusable **(FAIR: R1-R1.3)**

- **Documentation**: Each dataset includes a README (Markdown or plain text) with: file descriptions, column/variable definitions (data dictionary), units, missing value codes, processing steps, quality control procedures, and known limitations.
- **License**: [Specify, e.g., "Public datasets: CC BY 4.0. Code: Apache 2.0 or MIT. PHI-derived aggregates: CC BY 4.0 with de-identification certification. Controlled-access datasets: custom DUA per source agreement."] Default to CC BY 4.0 or CC0 for maximum reuse unless restrictions apply.
- **Provenance**: Processing pipelines are documented as reproducible workflows (Nextflow, Snakemake, or equivalent). Container images (Docker/Podman) are versioned and deposited alongside data. Git commit hashes and software versions are recorded in metadata. See the [Tools Catalog — L7 Provenance](../../tools/tools-master-catalog.md#l7-provenance) for the adopted provenance stack: LaminDB + bionty for lineage, redun for AST + data hashing, DVC for dataset versioning, and MLflow/Aim for experiment tracking.
- **Community standards**: [Specify domain standards, e.g., "BIDS for neuroimaging, AnnData/CELLxGENE schema for single-cell, GA4GH for genomic data exchange, HL7 FHIR R4 for clinical data."]. The [Tools Catalog — L9 Standards](../../tools/tools-master-catalog.md#l9-standard) catalogs 211 standards, schemas, ontologies, and protocols evaluated for Cytognosis. The [L6 FAIR Packaging](../../tools/tools-master-catalog.md#l6-fair) section covers RO-Crate, FAIRSCAPE, WRROC, and persistent identifier systems (DOI + SWHID + ARK).

---

## 4. Data Security and Privacy **(HIPAA)**

### 4.1 Sensitive Data Assessment

| Dataset ID | Contains PHI? | Contains PII? | GDPR applies? | Genetic data? | Requires IRB? | Requires DUA/MTA? |
| --- | --- | --- | --- | --- | --- | --- |
| DS-001 | [Yes/No] | [Yes/No] | [Yes/No] | [Yes/No] | [Yes/No] | [Yes/No] |

### 4.2 Privacy Protection Measures

For datasets containing sensitive information, describe the privacy protection strategy:

- **De-identification / anonymization**: [Method, e.g., "Safe Harbor method per 45 CFR 164.514(b)(2): removal of 18 HIPAA identifiers. Verification by qualified statistical expert." or "Expert determination method." or "k-anonymity with k≥5 using Amnesia tool."]
- **Pseudonymization**: [If applicable, describe key management, e.g., "Participant IDs are pseudonymized using a SHA-256 hash with a project-specific salt stored in a separate, access-restricted keystore."]
- **Encryption**: [Specify, e.g., "Data encrypted at rest using AES-256 (GCP default). Data encrypted in transit using TLS 1.3. Encryption keys managed via GCP Cloud KMS with HSM-backed key material."]
- **Access controls**: [Describe IAM roles, MFA requirements, VPN, audit logging per the HIPAA Security Controls Checklist](../compliance/phi-security-controls-checklist.md).

### 4.3 Ethical and Legal Compliance

- **IRB approval**: [Protocol number, approving institution, approval date, expiration]
- **Informed consent**: [Describe consent scope, e.g., "Broad consent for genomic research and data sharing per NIH Genomic Data Sharing Policy. Consent forms stored in [location] with restricted access."]
- **GDPR**: [If applicable, document lawful basis (Art. 6), special category processing (Art. 9), DPIA reference, Data Protection Officer contact]
- **Regulatory frameworks**: [List all applicable, e.g., "HIPAA (45 CFR 160/164), Common Rule (45 CFR 46), NIH GDS Policy, 21 CFR Part 11 (if applicable), state-specific laws (CCPA, etc.)"]

---

## 5. Data Storage, Backup, and Preservation

### 5.1 Storage During the Project

| Data class | Storage location | Access method | Responsible party |
| --- | --- | --- | --- |
| Public / Internal | [e.g. GCS `cytognosis-data` project, regional buckets] | [HTTPS, gsutil, programmatic API] | [Data steward name] |
| Controlled | [e.g. GCS `cytognosis-data` isolated project with VPC-SC] | [Authenticated API, audit-logged] | [Data steward name] |
| PHI | [e.g. GCS `cytognosis-phi-prod` with HIPAA BAA] | [VPN + MFA + IAM roles] | [HIPAA Security Officer] |
| Code / pipelines | [GitHub cytognosis org, private repos] | [Git + SSH/HTTPS] | [Engineering lead] |

### 5.2 Backup Strategy

- **Frequency**: [e.g., "Continuous replication for GCS (dual-region). Daily snapshots for Cloud SQL. Git repos mirrored to secondary remote."]
- **Retention**: [e.g., "30-day rolling backups with monthly archives retained for 1 year. Long-term archival backups retained for 10 years per institutional policy."]
- **Testing**: [e.g., "Quarterly backup restoration test for a randomly selected dataset."]
- **Disaster recovery**: [RTO and RPO targets, failover procedures]

### 5.3 Long-term Preservation

- **Retention period**: [e.g., "Minimum 10 years after project completion for raw data underlying publications. Indefinite for public datasets deposited in trusted repositories."]
- **Preservation formats**: [e.g., "Data converted to preservation-friendly formats (CSV, HDF5, TIFF) before archival. Format migration plan reviewed every 5 years."]
- **Repository**: [Name the trusted repository for long-term deposit, e.g., Zenodo, institutional archive, domain repository. Verify it meets CoreTrustSeal or equivalent criteria per the [OpenAIRE trusted repository guide](https://www.openaire.eu/find-trustworthy-data-repository).]

---

## 6. Data Sharing and Access

### 6.1 Sharing Strategy

Describe which data will be shared, with whom, when, and how, following the principle "as open as possible, as closed as necessary."

| Dataset ID | Shareable? | Access level | Repository | License | Embargo | Justification for restrictions |
| --- | --- | --- | --- | --- | --- | --- |
| DS-001 | Yes (processed) | Open | [Zenodo / GEO] | CC BY 4.0 | [None / 12 mo] | [N/A] |
| DS-002 | Partial (aggregated) | Controlled | [NDA] | Custom DUA | None | PHI; individual-level data restricted per consent |
| DS-003 | Yes | Open | [HuggingFace / Zenodo] | Apache 2.0 | None | N/A |

### 6.2 Exceptions to Open Access

For any data not shared openly, document the legitimate exception:

- [ ] Intellectual property / commercial exploitation
- [ ] Privacy / data protection (HIPAA, GDPR)
- [ ] Confidentiality / trade secrets
- [ ] Security considerations
- [ ] Obligations under grant agreement or DUA
- [ ] Other: [specify]

> **Guidance**: Even when data cannot be shared, metadata describing the dataset must be made openly accessible (CC0). Deposit a metadata-only record in the repository describing what the data contains, how it was generated, and how to request access.

### 6.3 Code and Software Sharing

- **Repository**: [e.g., GitHub `cytognosis` organization, public repos]
- **License**: [e.g., Apache 2.0 for libraries, MIT for utilities]
- **Citation**: Software releases are deposited on Zenodo with DOI minting via the GitHub-Zenodo integration.
- **Documentation**: README, API docs, installation instructions, and example notebooks accompany all releases.

---

## 7. Roles and Responsibilities

| Role | Person | Responsibilities |
| --- | --- | --- |
| Principal Investigator | [name] | Overall accountability for DMP compliance; approves data sharing decisions |
| Data Steward | [name] | Day-to-day data management; metadata curation; repository deposits; DMP updates |
| HIPAA Security Officer | [name] | PHI access controls; security incident response; quarterly HIPAA reviews |
| Privacy Officer | [name] | GDPR/privacy compliance; consent management; DPIA coordination |
| IT / Infrastructure Lead | [name] | Storage provisioning; backup verification; access control implementation |
| Research Lead(s) | [name(s)] | Data collection protocols; quality control; documentation of methods |

---

## 8. Costs and Resources

| Item | Estimated Cost | Funding Source | Notes |
| --- | --- | --- | --- |
| Cloud storage (GCS) | [$/year] | [Grant / operational budget] | [Tiered: standard for active, nearline for archive] |
| Repository deposit fees | [$ or free] | [Grant] | [Zenodo: free; domain repos may charge] |
| Personnel (data steward) | [% FTE] | [Grant / institutional] | [Ongoing throughout project lifecycle] |
| Compliance (HIPAA audit) | [$/year] | [Operational budget] | [Annual third-party assessment] |
| Software licenses | [$ or open-source] | [Grant] | [List any commercial tools required] |
| Data anonymization tools | [$ or free] | [Grant] | [e.g., Amnesia (free), ARX (free)] |

> **Guidance**: RDM costs are eligible under Horizon Europe grants (Article 6.2). Plan early to reduce costs. Use the [OpenAIRE RDM costing tool](https://www.openaire.eu/estimating-costs-rdm-tool) for estimation.

---

## 9. Version History

| Version | Date | Author | Changes |
| --- | --- | --- | --- |
| 0.1 | [YYYY-MM-DD] | [name] | Initial draft (proposal stage) |
| 1.0 | [YYYY-MM-DD] | [name] | Full DMP (month 6 deliverable) |

---

## Appendix A: FAIR Self-Assessment Checklist

Use this checklist (adapted from [Jones & Grootveld, 2017](https://doi.org/10.5281/zenodo.1065991)) to evaluate each dataset:

### Findable

- [ ] F1: Data have a globally unique and persistent identifier (DOI, Handle, ARK)
- [ ] F2: Data are described with rich metadata (see minimum fields in section 3.1)
- [ ] F3: Metadata clearly include the identifier of the data they describe
- [ ] F4: Data and metadata are registered or indexed in a searchable resource

### Accessible

- [ ] A1: Data are retrievable by their identifier using a standardized protocol (HTTPS)
- [ ] A1.1: The protocol is open, free, and universally implementable
- [ ] A1.2: The protocol allows for authentication/authorization where necessary
- [ ] A2: Metadata remain accessible even when data are no longer available

### Interoperable

- [ ] I1: Data use a formal, accessible, shared, and broadly applicable language (e.g., JSON-LD, RDF, CSV with schema)
- [ ] I2: Data use vocabularies that follow FAIR principles (published, PID-identified ontologies)
- [ ] I3: Data include qualified references to other data (PIDs with relationship types)

### Reusable

- [ ] R1: Data have a clear and accessible data usage license
- [ ] R1.1: Data are associated with detailed provenance information
- [ ] R1.2: Data meet domain-relevant community standards
- [ ] R1.3: Data are described with a plurality of accurate and relevant attributes

---

## Appendix B: Cytognosis-Specific References

- [Master Data Strategy](../master-data-strategy.md)
- [Data Governance Policy](../policies/data-governance-policy.md)
- [HIPAA Compliance Framework](../compliance/hipaa-compliance-framework.md)
- [**HIPAA Compliance Status Dashboard**](../compliance/HIPAA-STATUS.md) — single pane of glass for all 45 CFR controls
- [NIH GDS 2025 Requirements](../compliance/nih-gds-requirements.md) — NIST 800-171 mapping, generative AI restriction
- [PHI Security Controls Checklist](../compliance/phi-security-controls-checklist.md)
- [Controlled Data Access Policy](../policies/controlled-data-access.md)
- [NIH NDA Access Procedures](../policies/nih-nda-access-procedures.md)
- [Multimodal Health Data Schema](../schemas/multimodal-health-data-schema.md)
- [Data Use Agreement Template](data-use-agreement-template.md)
- [Scholarly Knowledge Graph Schema](../scholarly-knowledge-graph.md)
- [Technical Data Infrastructure](../TECHNICAL_DATA_INFRASTRUCTURE.md)
- [Tools Catalog](../../tools/README.md) — 911-tool technology landscape with storage, FAIR, provenance, workflow, and standards picks
- [Infrastructure Stack Deep-Dive](../../tools/tools-infrastructure-stack.md) — data flow from bytes to FAIR-published reasoning
- [**Neuroverse Datasets & Cohorts**](../../programs/neuroverse/datasets-cohorts.md) — primary data sources for the first Cytognosis DMP
- [**Reproducibility & FAIR Strategy**](../../reproducibility/README.md) — how data gets packaged as WRROC and published via SEEK/WorkflowHub

## Appendix C: External Reference Standards

| Standard | URL | Applicability |
| --- | --- | --- |
| FAIR Guiding Principles | https://doi.org/10.1038/sdata.2016.18 | All research data |
| Horizon Europe DMP Template | https://ec.europa.eu/info/funding-tenders/opportunities/docs/2021-2027/horizon/temp-form/report/data-management-plan_he_en.docx | EU-funded projects |
| NIH Data Management and Sharing Policy | https://sharing.nih.gov/data-management-and-sharing-policy | NIH-funded projects |
| HIPAA Security Rule | https://www.hhs.gov/hipaa/for-professionals/security/ | All PHI handling |
| GA4GH Framework | https://www.ga4gh.org/genomic-data-toolkit/ | Genomic data exchange |
| BIDS Specification | https://bids-specification.readthedocs.io/ | Neuroimaging data |
| CELLxGENE Schema | https://github.com/chanzuckerberg/single-cell-curation | Single-cell data |
| OpenAIRE ARGOS | https://argos.openaire.eu/ | DMP creation and publishing |
| CoreTrustSeal | https://www.coretrustseal.org/ | Repository certification |
| FAIRsharing | https://fairsharing.org/ | Standards and repository registry |
| re3data | https://www.re3data.org/ | Repository discovery |

---

© 2026 Cytognosis Foundation. All rights reserved.

*This template is reviewed annually. Domain-specific annexes (genomics, neuroimaging, clinical) may be appended as the project portfolio grows.*

## Appendix D: DMP Section to Tools Catalog Mapping

This appendix maps DMP sections to the relevant layers of the [Cytognosis Tools Catalog](../../tools/README.md) to help project teams select approved tools.

| DMP Section | Catalog Layer(s) | Key Primary Picks |
| --- | --- | --- |
| 2.1 Data Types and Formats | [L1-storage](../../tools/tools-master-catalog.md#l1-storage) | TileDB, Zarr v3, Parquet, AnnData/h5ad, Safetensors, GGUF |
| 2.1 Preprocessing pipelines | [L2-preprocessing](../../tools/tools-master-catalog.md#l2-preprocessing) | fMRIPrep, Docling, GROBID, PLINK2, Scanpy, scVI |
| 3.1 Findable (PIDs, metadata) | [L6-fair](../../tools/tools-master-catalog.md#l6-fair) | Zenodo (DOI), SWHID, ARK (FAIRSCAPE), CITATION.cff |
| 3.3 Interoperable (schemas) | [L9-standard](../../tools/tools-master-catalog.md#l9-standard) | LinkML, BIDS, NWB, GA4GH VRS, Biolink Model, CELLxGENE |
| 3.4 Reusable (provenance) | [L7-provenance](../../tools/tools-master-catalog.md#l7-provenance) | LaminDB, redun, DVC, DataLad, MLflow, Aim |
| 3.4 FAIR packaging | [L6-fair](../../tools/tools-master-catalog.md#l6-fair) | RO-Crate (WRROC), FAIRSCAPE |
| 4.2 Security controls | [L13-net](../../tools/tools-master-catalog.md#l13-net) | Tailscale, WireGuard, NATS+JetStream |
| 5.1 Storage infrastructure | [L1-storage](../../tools/tools-master-catalog.md#l1-storage) | GCS, TileDB, AIStor (MinIO), DuckDB |
| 5.3 Long-term preservation | [L3-repository](../../tools/tools-master-catalog.md#l3-repository) | Zenodo, DANDI, OpenNeuro, Software Heritage |
| 6.1 Data sharing (repositories) | [L3-repository](../../tools/tools-master-catalog.md#l3-repository) | GitHub, HuggingFace Hub, Zenodo, OpenNeuro |
| 6.3 Code sharing | [L4-meta](../../tools/tools-master-catalog.md#l4-meta) | Zoekt, GitNexus, CITATION.cff |
| 8 Costs (open-source stack) | [Cross-cutting themes](../../tools/tools-master-catalog.md#cross-cutting-themes) | All primary picks permissively licensed |
