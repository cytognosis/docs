# NIH NIMH Data Archive (NDA) Access Procedures

This document outlines the strict regulatory pathway required for the Cytognosis Foundation (and any collaborating entities) to submit a Data Access Request (eDAR) for Controlled Access datasets within the NIH NIMH Data Archive (NDA), specifically targeting collections such as PsychENCODE.

## 1. Core Institutional Prerequisites

To handle sensitive human genomic or clinical data, an institution cannot rely merely on informal collaborations. The National Institutes of Health require a rigorous chain of institutional accountability.

### 1.1 Federalwide Assurance (FWA)

The cornerstone of access to all human subjects research is the **Federalwide Assurance**. The Office for Human Research Protections (OHRP) issues an FWA as a binding written assurance that an institution agrees to comply with the Common Rule (45 CFR 46) for the protection of human subjects.

* **Requirement**: Cytognosis Foundation must maintain an active FWA number.
* **Limitation**: To apply for an FWA, the organization must first legally designate an Institutional Review Board (IRB) of record.

### 1.2 Institutional Review Board (IRB) and IORG

The IRB is the oversight committee responsible for ensuring the ethical and safe treatment of research subjects. The organization managing the IRB is issued an **IORG number** by the OHRP.

* **Requirement**: For "Controlled Access" datasets, the Lead Recipient usually must provide explicit, documented IRB approval (not just a generic waiver of oversight) confirming that the specific secondary research proposed aligns strictly with the original subjects' informed consent.
* **Action**: Cytognosis must execute an **IRB Authorization Agreement (IAA)** with a partnered university (e.g., Purdue) or a commercial entity (e.g., WCG/Advarra) to borrow their IORG designation for our FWA application.

### 1.3 eRA Commons & Signing Official (SO)

To interact with NIH electronic systems:

* Cytognosis must have a registered institutional profile in **eRA Commons**.
* The organization must officially designate at least one **Signing Official (SO)**. The SO is the only administrator authorized to legally bind the institution to Data Use Certifications (DUCs) and approve DAR requests submitted by staff researchers.

## 2. The Electronic Data Access Request (eDAR) Pipeline

With the institutional infrastructure (FWA, IRB, SO) secured, individual researchers (Principal Investigators) may execute the eDAR pipeline via the NDA portal.

### Step-by-Step Execution

1. **Account Creation**: The Lead Recipient (Principal Investigator) creates an NDA account tied to their institutional email and links it directly to their eRA Commons PI account.
2. **Data Selection & Justification**: Using the NDA Query Tool, the PI selects the restricted Data Collections (e.g., PsychENCODE) and submits a comprehensive Research Data Use Statement detailing specific aims.
3. **Establishing the Roster**: The PI adds all secondary scientists or data engineers who need computational access onto the DAR array. **Crucial Limit**: All secondary recipients must either be covered under the single institutional IRB Approval or hold separate IRB approvals explicitly uploaded as part of the DAR packet.
4. **IRB Documentation Upload**: For restricted collections, upload the precise IRB approval letter. Standard templates (such as the PsychENCODE template) require the Institutional SO to guarantee data deletion upon project/DUC expiration and to strictly prohibit reidentification attempts.
5. **Electronic Signatures**: The PI electronically signs the initial DAR. The system then automatically routes the DAR to the institution's Signing Official (SO).
6. **SO Ratification**: The SO logs in with their independent eRA Commons credentials and electronically ratifies the Data Use Certification (DUC).
7. **NIH Data Access Committee (DAC) Review**: The NIH DAC reviews the DAR, validating the FWA standing, IRB scope, and research justification. Review timelines vary from 2 to 4 weeks.

## 3. Post-Approval Operations

* **Duration**: Authorized DARs are active for exactly **one calendar year**.
* **Renewal Window**: Progress reports and extension requests must be formally submitted within **60 days** of expiration to avoid being locked out.
* **Compliance**: As stipulated by the SO signature, all downloaded data must be stored on NIST 800-171-compliant infrastructure, cannot be shared outside the approved roster, and must be permanently wiped upon completion.

---

**Document Version**: 1.0
**Effective Date**: March 2026
**Classification**: Internal Use Only
