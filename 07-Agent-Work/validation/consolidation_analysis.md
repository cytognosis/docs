# Data Strategy + Infrastructure Consolidation

## Diagnosis: Broken Links in `data-strategy/README.md`

### Root Cause

The archive README (commit `8cc8fe3`, unpushed) pointed to GitHub blob URLs (`https://github.com/cytognosis/infrastructure/blob/main/docs/data-strategy/...`), but the consolidation commit in infrastructure (`17fe0c5`) was also unpushed. Both repos were 1 commit ahead of `origin/main`, so all GitHub links returned 404.

> [!IMPORTANT]
> **No files were lost.** All 10 original data-strategy files were successfully migrated to `infrastructure/docs/data-strategy/` in the local consolidation commit, plus 8 new documents.

### Recovery Verification

| Original (data-strategy) | Infrastructure Location | Status |
|---|---|---|
| `docs/master-data-strategy.md` | `docs/data-strategy/master-data-strategy.md` | ✅ |
| `docs/dataset-catalog.md` | `docs/data-strategy/dataset-catalog.md` | ✅ |
| `compliance/hipaa-compliance-framework.md` | `docs/data-strategy/compliance/hipaa-compliance-framework.md` | ✅ |
| `policies/data-governance-policy.md` | `docs/data-strategy/policies/data-governance-policy.md` | ✅ |
| `policies/controlled-data-access.md` | `docs/data-strategy/policies/controlled-data-access.md` | ✅ |
| `policies/nih-nda-access-procedures.md` | `docs/data-strategy/policies/nih-nda-access-procedures.md` | ✅ |
| `schemas/multimodal-health-data-schema.md` | `docs/data-strategy/schemas/multimodal-health-data-schema.md` | ✅ |
| `templates/data-use-agreement-template.md` | `docs/data-strategy/templates/data-use-agreement-template.md` | ✅ |

---

## Changes Made

### 1. Fixed `data-strategy/README.md`
- Removed broken GitHub blob URLs from the migration table
- Replaced with path-only references (no external URLs that depend on push state)
- Added new DMP template to the migration table
- Committed: `7ffb079 fix: remove broken GitHub URLs from archived README`

### 2. Created Data Management Plan Template
- **File**: [data-management-plan-template.md](file:///home/mohammadi/repos/cytognosis/org/infrastructure/docs/data-strategy/templates/data-management-plan-template.md)
- **302 lines** covering all 9 DMP sections plus 3 appendices
- Synthesized from 6 authoritative sources:

| Source | Key Contributions |
|---|---|
| OpenAIRE HE RDM Mandate | DMP timeline, trusted repositories, metadata compliance, "as open as possible" |
| OpenAIRE FAIR Guide | F1-F4, A1-A2, I1-I3, R1-R1.3 principle mapping with actionable checklist |
| OpenAIRE Sensitive Data | Anonymization/pseudonymization/encryption strategies, GDPR considerations |
| OpenAIRE Metadata Guide | Minimum metadata fields, Dublin Core, DataCite schema requirements |
| Utrecht University DMP | DMP structure, data management paragraph, DMPonline workflow |
| Cytognosis Internal | HIPAA classification levels, GCP project boundaries, controlled-access SOPs |

### 3. Updated Infrastructure READMEs
- Added DMP template reference to top-level `README.md`
- Added DMP template row to `docs/data-strategy/README.md` schemas & templates table
- Committed: `698d5e8 feat: add FAIR-compliant Data Management Plan template`

---

## Final Infrastructure Data Strategy Tree

```
docs/data-strategy/
├── README.md                                    # Hub index
├── master-data-strategy.md                      # Unified vision & FAIR mandate
├── public-data-strategy.md                      # Open-science release strategy
├── dataset-catalog.md                           # Multimodal dataset stratification
├── TECHNICAL_DATA_INFRASTRUCTURE.md             # GCP/HIPAA/PHI infrastructure
├── paper-library-architecture.md                # Sovereign library architecture
├── scholarly-knowledge-graph.md                 # LinkML v0.4.0 schema
├── sssom-cross-ontology-mapping.md              # SSSOM cross-ontology stack
├── monday-resource-boards.md                    # Monday.com resource boards
├── linkml-kg-playbook.md                        # 22-chapter playbook pointer
├── compliance/
│   ├── hipaa-compliance-framework.md            # Full HIPAA program
│   └── phi-security-controls-checklist.md       # Quarterly audit checklist
├── policies/
│   ├── data-governance-policy.md                # Classification & lifecycle
│   ├── controlled-data-access.md                # External dataset acquisition SOP
│   └── nih-nda-access-procedures.md             # NIH NDA eDAR pipeline
├── schemas/
│   └── multimodal-health-data-schema.md         # JSON schemas for all modalities
└── templates/
    ├── data-use-agreement-template.md           # Outbound DUA
    └── data-management-plan-template.md         # ✨ NEW: FAIR DMP template
```

## Pending: Push to Remote

Both repos have unpushed commits. When ready:

```bash
# data-strategy (2 commits ahead)
cd /home/mohammadi/repos/cytognosis/org/data-strategy
git push origin main

# infrastructure (2 commits ahead)
cd /home/mohammadi/repos/cytognosis/org/infrastructure
git push origin main
```
