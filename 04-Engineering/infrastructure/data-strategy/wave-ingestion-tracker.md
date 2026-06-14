# Wave-Based Ingestion Tracker

> Track progress of dataset ingestion through the Cytognosis data pipeline.

## Wave 0: Infrastructure Testing (In Progress)

**Goal**: Validate entire pipeline end-to-end, find all missing functionality.

| Dataset | Download | Parse | DVC Track | DVC Push | DVC Pull | Provenance | RO-Crate | Neo4j | Status |
|---------|----------|-------|-----------|----------|----------|------------|----------|-------|--------|
| GO ontology (124MB) | ✅ Present | ✅ Via registry | ✅ Tracked | ✅ Pushed | ✅ Pulled | ⏳ | ⏳ | ⏳ | 🔄 |
| OLS4 SSSOM (2GB) | ✅ Present | ✅ Consolidated | ⏳ | ⏳ | ⏳ | ⏳ | ⏳ | N/A | 📋 |
| UMLS 2026AA (42GB) | ✅ Present | ✅ Parsed | ⏳ | ⏳ | ⏳ | 93.3% | ⏳ | ⏳ | 📋 |
| SnomedCT (28GB) | ✅ Present | ✅ Parsed | ⏳ | ⏳ | ⏳ | 90% | ⏳ | ⏳ | 📋 |
| LOINC (2GB) | ✅ Present | ⏳ Raw | ⏳ | ⏳ | ⏳ | 50% | ⏳ | ⏳ | 📋 |

### Wave 0 Issues Discovered
- `rocrate` Python package needed installation (`pip install rocrate`)
- `fetch_ontology()` requires OntologyResource + OntologyRegistry objects (registry-based, not URL-based)
- Branch protection rules on all repos — need PR workflow for commits
- DVC round-trip: ✅ VERIFIED (push 124MB in 26s at 4.94 MB/s, pull instant from cache)

## Wave 1: Public Knowledge Graphs (Next Session)

**Goal**: Build complete KG from all public sources via `dvc repro`.

| Dataset | Size | Ingestion Status | DVC | Pipeline Stage |
|---------|------|-----------------|-----|----------------|
| Monarch KG | 45GB | ✅ kg-integrated | ⏳ | `monarch_merge` |
| PrimeKG | 2GB | ✅ kg-integrated | ⏳ | `primekg_convert` |
| Open Targets 25.03 | 180GB | ✅ parsed | ⏳ | `opentargets_ingest` |
| UniChem | 5GB | ✅ kg-integrated | ⏳ | `unichem_xrefs` |
| PKG 2.0 | 8GB | ✅ kg-integrated | ⏳ | (topic_areas) |

## Wave 2: Controlled Access (After DUC Submissions)

| Cohort | Modalities | Samples | DUC Status |
|--------|-----------|---------|------------|
| NBB | WGS | ~10,000 | 📋 Pending |
| PsychENCODE | scRNA-seq, WGS | ~3,000 | 📋 Pending |
| PsychAD | snRNA-seq | ~1,500 | 📋 Pending |
| ROSMAP | Multi-omics | ~3,500 | 📋 Pending |

**Prerequisites**: FWA, SMART IRB, NIST 800-171 self-assessment

## Wave 3: PHI Cohorts (Future)

**Prerequisites**: VPC-SC, CMEK, BAA with Google, full HIPAA controls
