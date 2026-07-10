# Controlled Data Access Policy

## 1. Overview and Purpose

This document establishes the official Cytognosis Foundation policy and standard operating procedures (SOP) for acquiring, managing, and utilizing controlled-access biological and clinical datasets.

As an AI-native healthcare non-profit, the Foundation requires access to large-scale, high-fidelity datasets to train predictive models for early disease interception. Many of these seminal datasets, including but not limited to those housed within the National Institutes of Health (NIH) National Institute of Mental Health Data Archive (NDA)—such as PsychENCODE (PEC) and the NeuroBioBank (NBB)—are classified as controlled-access.

This policy outlines the parallel tracks required to secure this access: establishing independent institutional compliance infrastructure and forging formal academic collaborations.

## 2. Scope

This protocol applies to all internal researchers, engineers, and affiliated personnel at Cytognosis Foundation who seek to access, process, or store controlled-access genomic, proteomic, clinical, or phenotypic data from external repositories.

## 3. Regulatory Prerequisites

Before Cytognosis Foundation can formally request controlled data as an independent research entity, two fundamental regulatory prerequisites must be met.

### 3.1 Establishing an Institutional Review Board (IRB) Pipeline

IRB approval or exemption is a universal prerequisite for accessing human subjects data. Cytognosis Foundation pursues a dual-track strategy for IRB compliance:

**Track A: Commercial IRB Partnership (Primary Method)**
Cytognosis Foundation partners with an external, accredited commercial IRB (e.g., WCG IRB, Advarra).

1. The Chief Data Officer or designated Principal Investigator (PI) prepares the research protocol detailing data use, storage, and privacy safeguards.
2. The protocol is submitted to the commercial IRB.
3. The IRB issues a formal determination (typically "Exempt" under Category 4 for secondary research using de-identified pre-existing data, or full approval).

**Track B: Institutional Reliance Agreement (IAA)**
If collaborating directly with an academic institution on a joint grant, Cytognosis Foundation may establish an IRB Authorization Agreement (IAA). This allows the Foundation to rely on the collaborating institution's IRB for oversight, reducing administrative duplication.

### 3.2 Securing a Federalwide Assurance (FWA) number

An FWA is a binding agreement between an institution and the U.S. Department of Health and Human Services (HHS) Office for Human Research Protections (OHRP). It guarantees the institution will comply with the ethical standards of the Common Rule when conducting human subjects research. Many federal repositories, including the NIH NDA, mandate an active FWA.

**FWA Application Process:**

1. The Foundation must designate a Signatory Official (typically the CEO) and a Human Protections Administrator.
2. The application is submitted electronically via the OHRP system.
3. The submission links the Foundation's FWA to the registered IRB (internal, commercial, or academic partner via IAA).
4. Upon approval, the FWA number is recorded in the overarching Data Governance Registry.

## 4. NIH/NDA Specific Data Access Procedures

The NIH National Institute of Mental Health Data Archive (NDA) is a critical repository containing deep multi-omic data (PEC) and post-mortem tissue metadata (NBB). Accessing the NDA requires strict adherence to their Data Access Request (DAR) pipeline.

For detailed, step-by-step regulatory instructions—including FWA linkage, IORG prerequisites, eRA Commons Signing Official workflows, and the specific Data Access Request (eDAR) pipeline—refer to the dedicated [NIH NDA Access Procedures](nih-nda-access-procedures.md).

## 5. Academic Collaboration Track (Alternative Access Pathway)

Recognizing that establishing independent infrastructure (FWA, IRB) takes time, the Foundation maintains a parallel strategy of academic collaboration.

### 5.1 Joint Research Proposals

Cytognosis Foundation scientists will aggressively seek joint research grants with established academic partners (e.g., UCSF, Stanford).

**Workflow:**

1. Identify a complementary academic PI.
2. Draft a joint overarching research structure.
3. The academic partner assumes the role of the primary submitting institution, leveraging their existing FWA, IRB, and eRA Commons credentials.
4. Cytognosis Foundation serves as a sub-awardee or formal collaborator providing advanced AI engineering and computational resources.

### 5.2 Collaborative Data Use Agreements (DUA)

Data accessed through the academic partner must be legally transferred to Cytognosis Foundation computing environments.

1. A formal, custom DUA is drafted between the academic institution and the Foundation.
2. The DUA must explicitly enumerate permitted uses, technical safeguards (AES-256 encryption, access logs), and non-commercialization clauses in strict alignment with the original NDA/DAC stipulations.
3. Once fully executed, encrypted data transfer directly to the Foundation's GCP infrastructure is authorized.

## 6. Security and Compliance

All controlled-access data, regardless of acquisition pathway, is subject to the highest tier of the Cytognosis Foundation Data Governance Policy (Level 4: Restricted Data).

- **Data Locality:** All controlled-access data must land directly in the `cytognosis-phi-prod` project (NIH NDA-style raw imports → `cytognosis-phi-core`; partner-specific spaces → `cytognosis-phi-collab-[id]`). It must never transit through `cytognosis-infrastructure` or `cytognosis-data`. See [`../TECHNICAL_DATA_INFRASTRUCTURE.md`](../../../04-Engineering/infrastructure/data-strategy/TECHNICAL_DATA_INFRASTRUCTURE.md) for bucket taxonomy and CMEK / VPC-SC requirements.
- **Zero-Trust Access:** No data may be downloaded to local developer machines without explicit, project-specific authorization from the CDO. Access is restricted to secure cloud workstations.
- **Audit Logging:** Immutably logged access via Cloud Audit Logs.

## 7. Document History

- **Version**: 1.0
- **Effective Date**: March 2026
- **Owner**: Chief Data Officer
