# Data Strategy & Compliance

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: engineers
> **Tags**: `engineering`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

> **Single source of truth** for Cytognosis Foundation data governance, privacy and security architecture, regulated dataset acquisition, schemas, and the scholarly knowledge graph that ties research artifacts together.

This subtree was previously split across the `cytognosis/data-strategy` repository and this directory. As of May 2026 it is consolidated here. Older `data-strategy.md` content has been merged into [`master-data-strategy.md`](master-data-strategy.md); the historical `data-strategy` repository now redirects here.

## Map

### 1. Strategy

| Document | Purpose |
| --- | --- |
| [`master-data-strategy.md`](master-data-strategy.md) | Unified vision, FAIRification mandate, public dataset portfolio, governance structure, regulatory landscape |
| [`public-data-strategy.md`](public-data-strategy.md) | Open-science release strategy, dataset roadmap, privacy-preserving release techniques, partnerships |
| [`dataset-catalog.md`](dataset-catalog.md) | Stratification of multimodal datasets (genomic, neuroimaging, clinical, wearable) by access tier and infrastructure requirements |

### 2. Technical Infrastructure

| Document | Purpose |
| --- | --- |
| [`TECHNICAL_DATA_INFRASTRUCTURE.md`](TECHNICAL_DATA_INFRASTRUCTURE.md) | GCP project boundaries, GCS bucket taxonomy, VPC Service Controls, Healthcare API, Confidential Compute, IAM controls for PHI |

### 3. Scholarly Knowledge Graph & Sovereign Library

| Document | Purpose |
| --- | --- |
| [`paper-library-architecture.md`](paper-library-architecture.md) | Sovereign library: Google Drive (canonical PDFs) + Zotero (metadata-only) + W3C Web Annotation via Hypothes.is + future Neo4j two-layer KG |
| [`scholarly-knowledge-graph.md`](scholarly-knowledge-graph.md) | LinkML schema (BibTeX, OpenAlex, UMLS, Translator, RO-Crate, typed Paper↔Code/Model/Dataset edges, workflows, protocols, instruments) |
| [`sssom-cross-ontology-mapping.md`](sssom-cross-ontology-mapping.md) | LinkML-native SSSOM stack for cross-ontology mapping (UMLS, MONDO, HP, CL, CHEBI, NCBITaxon, SNOMED CT) and CELLxGENE harmonization |
| [`monday-resource-boards.md`](monday-resource-boards.md) | Monday.com Resources workspace: Papers / Models / Code / Datasets / Workflows / Protocols + typed relationship boards |
| [`linkml-kg-playbook.md`](linkml-kg-playbook.md) | Pointer to the 22-chapter hands-on playbook for LinkML, Biolink, BioCypher, Koza/Monarch, OLS4 SSSOM, CELLxGENE harmonization |

### 4. Compliance

| Document | Purpose |
| --- | --- |
| **[`compliance/HIPAA-STATUS.md`](../../../06-Operations/data-strategy/compliance/HIPAA-STATUS.md)** | **Master status dashboard**: all 45 CFR controls with ✅/⏳ status, evidence links, and owners |
| [`compliance/nih-gds-requirements.md`](../../../06-Operations/data-strategy/compliance/nih-gds-requirements.md) | NIH GDS 2025 operational requirements: 8 requirements, NIST SP 800-171 mapping, generative AI restriction, DUC checklist |
| [`compliance/hipaa-compliance-framework.md`](../../../06-Operations/data-strategy/compliance/hipaa-compliance-framework.md) | Full HIPAA program: administrative, physical, technical safeguards; BAA management; appendix A operational checklists |
| [`compliance/phi-security-controls-checklist.md`](../../../06-Operations/data-strategy/compliance/phi-security-controls-checklist.md) | Operational HIPAA Security Rule checklist used during quarterly reviews and audits |

### 5. Policies

| Document | Purpose |
| --- | --- |
| [`policies/data-governance-policy.md`](../../../06-Operations/data-strategy/policies/data-governance-policy.md) | Foundational governance policy: classification levels, lifecycle, roles, sanctions |
| [`policies/controlled-data-access.md`](../../../06-Operations/data-strategy/policies/controlled-data-access.md) | SOP for acquiring controlled-access external datasets (NIH NDA, PEC, NBB) — IRB, FWA, and academic partnership pathways |
| [`policies/nih-nda-access-procedures.md`](../../../06-Operations/data-strategy/policies/nih-nda-access-procedures.md) | Step-by-step NIH NDA eDAR pipeline, eRA Commons, Signing Official, post-approval obligations |

### 6. Schemas & Templates

| Document | Purpose |
| --- | --- |
| [`schemas/multimodal-health-data-schema.md`](schemas/multimodal-health-data-schema.md) | JSON schemas for genomic, proteomic, clinical (FHIR R4), imaging, behavioral profiles + unified patient record |
| [`templates/data-use-agreement-template.md`](../../../_templates/data-use-agreement-template.md) | DUA template for outbound dataset releases — permitted/prohibited uses, security requirements, indemnification |
| [`templates/data-management-plan-template.md`](../../../_templates/data-management-plan-template.md) | FAIR-compliant DMP template aligned with Horizon Europe, NIH DMSP, and HIPAA requirements |

## Data Governance Principles

1. **Privacy by Design** — PHI protection is baked into every stratum (collection, processing, storage, sharing). Minimum-necessary collection. Differential privacy / k-anonymity for derivatives. Continuous re-identification risk assessment.
2. **Data Sovereignty** — All canonical data lives on Cytognosis-controlled infrastructure. Third-party SaaS is only used for synchronization where the canonical copy still resides on Drive or in our own GCP projects (see `paper-library-architecture.md`).
3. **FAIR + Open Science** — Every public release satisfies the 15 FAIR Guiding Principles (`master-data-strategy.md`). Schemas, ontologies, and licenses are explicit. Synthetic and aggregated derivatives flow into the public commons.
4. **Regulatory Compliance** — HIPAA, GDPR, FDA SaMD, ICH GCP, 21 CFR Part 11, ISO 27001/27799/13485. State and country-specific overlays where applicable.
5. **Equity & Representation** — Datasets are stratified, audited, and rebalanced for global representation; partnerships explicitly target underserved populations.

## Strategic Focus Areas

- **Multimodal Integration** — Genomic, proteomic, neuroimaging, clinical (EHR), behavioral, and continuous biosensing streams unified through the multimodal schema and the scholarly KG.
- **AI-Native Architecture** — Data structures optimized for ML pipelines (federated learning, edge inference, privacy-preserving computation).
- **Preventive Healthcare Focus** — Early detection biomarkers, longitudinal trajectories, intervention effectiveness, risk prediction.
- **Knowledge-Graph-Backed Research** — All papers, code, models, datasets, workflows, protocols, and instruments are first-class entities with typed relationships (see `scholarly-knowledge-graph.md`).

## Implementation Roadmap

| Phase | Window | Outcomes |
| --- | --- | --- |
| Foundation | Months 0–6 | Governance committee operating; HIPAA program live; sovereign library (Drive + Zotero) operational; infrastructure project boundaries enforced |
| Expansion | Months 7–18 | First public datasets released; LinkML scholarly KG ingesting Zotero/OpenAlex; SSSOM-driven cross-ontology pipelines in CI; federated learning pilots |
| Scale | Months 19–36 | Global research network; advanced privacy-preserving AI techniques in production; regulatory submissions for clinical-grade models |

## Contacts

- **Chief Data Officer** — Shahin Mohammadi (mohammadi@cytognosis.org)
- **HIPAA Security Officer** — Shahin Mohammadi (interim)
- **Privacy Officer** — to be appointed
- **Compliance Officer** — to be appointed
- **Research Director** — to be appointed

## Related Subsystems

- [Master Infrastructure Index](../MASTER_INFRASTRUCTURE.md)
- [DNS & GCP Architecture](../DNS_AND_GCP_ARCHITECTURE.md)
- [Tools Catalog](../tools/README.md) — 911-tool technology landscape; L1-storage, L6-FAIR, L7-provenance, and L9-standards layers directly underpin data strategy
- [Container Framework](../container-framework.md) — orchestrates Neo4j, Jupyter, MLflow, Zotero (metadata) self-hosted services
- [Self-Hosted Services](../self-hosted/README.md)
- **[Neuroverse Program](../../../05-Research/neuroverse/README.md)** — first Cytognosis research program; drives the controlled-access data acquisition pipeline documented here
- **[Reproducibility & FAIR Strategy](../reproducibility/README.md)** — defines how data managed here gets packaged as RO-Crates and published through SEEK/WorkflowHub

---
© 2026 Cytognosis Foundation. All rights reserved.

*This subtree is reviewed quarterly. The scholarly knowledge graph schema and SSSOM stack evolve more frequently — see their version banners.*
