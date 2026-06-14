# Cytognosis Foundation — Master Infrastructure

**Last Updated**: May 2026
**Status**: ✅ PRODUCTION (operational stack); 🔵 ACTIVE (data strategy consolidation; KG layers landing)

The Cytognosis infrastructure follows extreme simplicity, serverless-first, and HIPAA-ready architectural choices. This repository contains the source of truth for our deployment strategies, domain mappings, identity federation, data analytics ecosystems, and **the data strategy and scholarly knowledge graph that everything serves**.

## Core documentation matrices

### 1. [DNS & GCP Architecture](DNS_AND_GCP_ARCHITECTURE.md)

Topology for the `cytognosis-*` GCP projects, the historical context of the `cg-*` and `*-zone` dual Cloud DNS zones, `.org` / `.com` / `.ai` management, third-party domain validations (Anthropic), and the Serverless IP scheme.

### 2. [Hosting & Deployment](HOSTING_AND_DEPLOYMENT.md)

Migration off legacy GCS static buckets into fully containerized Google Cloud Run deployments. GitHub Actions OIDC federation (`website-deployer`), Uvicorn debugging, and the artifact-registry layout.

### 3. [Communications & Workspace](COMMUNICATIONS_AND_WORKSPACE.md)

Nonprofit Google Workspace environment, automated deprecation of Google Apps Scripts, retirement of the `noreply@cytognosis.org` paid seat, and the inbound alias filtering network (`careers@`, `partnerships@`, `science@`, `info@`, `stories@`, `gcp-data-scientists@`, `gcp-infra-admins@`).

### 4. [Data Strategy & Compliance](data-strategy/README.md)

Unified data hub. Master strategy, public dataset strategy, dataset catalog, FAIRification mandate, HIPAA program, controlled-access SOPs (NIH NDA + academic partnerships), multimodal schemas, DUA template — **plus** the scholarly knowledge graph stack:

- [Sovereign Paper Library Architecture](data-strategy/paper-library-architecture.md) — Google Drive + Zotero (metadata-only) + W3C Web Annotation via Hypothes.is + future Neo4j two-layer KG.
- [Scholarly Knowledge Graph Schema](data-strategy/scholarly-knowledge-graph.md) — LinkML v0.4.0 covering BibTeX, OpenAlex, UMLS, Translator, RO-Crate, typed Paper ↔ Code / Model / Dataset relationships, workflows, protocols, instruments.
- [SSSOM Cross-Ontology Mapping](data-strategy/sssom-cross-ontology-mapping.md) — LinkML-native SSSOM stack for UMLS / MONDO / HP / CL / CHEBI / NCBITaxon / SNOMED CT, with hybrid CELLxGENE harmonization.
- [Monday.com Resource Boards](data-strategy/monday-resource-boards.md) — operational registry for the KG until Neo4j is fully online.
- [LinkML + KG Playbook](data-strategy/linkml-kg-playbook.md) — pointer to the 22-chapter hands-on tutorial (LinkML, Biolink, BioCypher, Koza/Monarch, OLS4 SSSOM, CELLxGENE harmonization).

### 5. [Technical Data Infrastructure (HIPAA & PHI)](data-strategy/TECHNICAL_DATA_INFRASTRUCTURE.md)

Deep dive into the GCS bucket taxonomy, VPC Service Controls, Cloud Healthcare API, Confidential Compute, and IAM controls for sensitive genomics and neuroscience datasets.

### 6. [Core Services & Self-Hosted Infrastructure](self_hosted/README.md)

Single source of truth for self-hosted operations. Architecture, evaluation reports, and deployment walkthroughs for Caddy, Cal.com, Excalidraw, Mermaid Live, Logseq, MLflow, Neo4j, and Jupyter — all powered by the internal [Container Framework](../container_framework/README.md).

### 7. [Tools Catalog](tools/README.md)

Comprehensive **911-tool** technology landscape across the Cytognosis 16-layer infrastructure stack (L1-storage through L16-cloud). Three product surfaces (Cytonome, Cytoverse, Spine), five adoption statuses, seven cross-cutting invariants (open-by-default, schema-as-hub, local-first, MCP interop, operational FAIR, dual-tier S2S, reproducibility). Includes the recommended stack at a glance, voice architecture options, storage hierarchy by data type, neuroimaging/connectomics stack, and full rejection/deferral rationale.

- [Master Tools Catalog](tools/tools-master-catalog.md) — full per-layer breakdown with status, license, org, surface
- [Infrastructure Stack Deep-Dive](tools/tools-infrastructure-stack.md) — data flow from bytes to FAIR-published reasoning with Mermaid diagrams
- [Filterable Spreadsheet](tools/tools-master-catalog.xlsx) — views by layer, surface, status, organization, plus tag glossary and stats
- [External Repository Directory](tools/external-repos-directory.md) — BioContextAI, BioCypher, GA4GH, KGHub, LinkML, Monarch, NCATS Translator, AI2, FAIRDOM-SEEK, RO-Crate

### 8. [Research Programs](programs/)

Active scientific programs with dedicated data environments, regulatory requirements, and external collaborators.

#### [Neuroverse](programs/neuroverse/README.md)

Cytognosis's first major research program: a multimodal, transdiagnostic, individual-level
foundation model for brain and psyche. Collaborators: McLean Hospital / MGB (Brad Ruzicka)
and Purdue University (Ananth Grama).

- [Datasets & Cohorts](programs/neuroverse/datasets-cohorts.md) — Batch 1–3 cohort table, modality coverage, data tiers, DUC sequence, estimated volumes
- [Infrastructure](programs/neuroverse/infrastructure.md) — SAE architecture, Purdue REED+, McLean ERIS, cross-institution auth model
- [Action Plan](programs/neuroverse/action-plan.md) — Regulatory, training, DUC submission, ingestion, training, and open-release phases

### 9. [Reproducibility & FAIR Strategy](reproducibility/README.md)

Six-principle reproducibility framework applying to all Cytognosis computational outputs
(cytoskeleton, cytos, Yar, neuro-*). Goal: any published result re-runnable with a single
`cytoskeleton reproduce <doi>` by a third party.

- [Schema Strategy](reproducibility/schema-strategy.md) — LinkML as single schema source; ISA, RO-Crate, GA4GH alignment
- [Artifact VFS & SWHID](reproducibility/artifact-vfs-swhid.md) — content-addressed VFS; SWHID, DVC-md5, sha256, OCI digest
- [Environments & Containers](reproducibility/envs-containers.md) — 66-cell env matrix; OCI image policy; sigstore signing; SLSA L3
- [Provenance & Lineage](reproducibility/provenance-lineage.md) — in-toto attestation; DSSE envelopes; WRROC / Process Run Crate / Five Safes Crate
- [SEEK & WorkflowHub](reproducibility/seek-workflowhub.md) — FAIRDOM-SEEK + WorkflowHub self-hosted deployment; LifeMonitor; FAIRSCAPE
- [Acceptance KPIs](reproducibility/acceptance-kpis.md) — Definitions of FAIR Workflow / Dataset / Model; monthly KPI targets; EOY 2026 success criterion

---

> [!NOTE]
> **HIPAA compliance dashboard**: [`data-strategy/compliance/HIPAA-STATUS.md`](data-strategy/compliance/HIPAA-STATUS.md) —
> single pane of glass for all 45 CFR controls with current status, evidence links, and owners.
>
> **NIH GDS 2025 requirements**: [`data-strategy/compliance/nih-gds-requirements.md`](data-strategy/compliance/nih-gds-requirements.md) —
> 8 operational requirements, NIST SP 800-171 mapping, generative AI restriction, DUC checklist.

