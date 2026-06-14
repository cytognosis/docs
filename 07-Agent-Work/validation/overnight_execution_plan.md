# Overnight Execution Plan

> **Start**: 2026-05-14 02:03 PST | **Target**: Complete by 10:00 PST

## Phase 1: Neo4j Infrastructure (P0)
- [ ] 1.1 Install Neo4j 5.x via Docker
- [ ] 1.2 Configure APOC + indexes
- [ ] 1.3 Import 88M CSV rows
- [ ] 1.4 Verify with Cypher queries
- [ ] COMMIT: `feat: neo4j 5.x setup and 88M row import`

## Phase 2: GWAS/Genomics Pipeline (P1)
- [ ] 2.1 GWAS summary stats parser (LDSC, metal, plink formats)
- [ ] 2.2 Liftover + allele harmonization module
- [ ] 2.3 PGC/GWAS Catalog/Pan-UKBB download functions
- [ ] 2.4 TileDB-VCF writer integration
- [ ] 2.5 Download + ingest 14 psychiatric GWAS datasets
- [ ] COMMIT: `feat: gwas ingestion pipeline with tiledb-vcf`

## Phase 3: GraphLD Data (P1)
- [ ] 3.1 Download LDGM precision matrices
- [ ] 3.2 GraphLD ↔ Cytos variant bridge
- [ ] 3.3 Verify with test LD computation
- [ ] COMMIT: `feat: graphld data download and cytos bridge`

## Phase 4: BioCypher Integration (P2)
- [ ] 4.1 Create schema_config.yaml
- [ ] 4.2 Write first working adapter (ontology → Neo4j)
- [ ] 4.3 Test multi-source ingestion
- [ ] 4.4 Test export formats
- [ ] COMMIT: `feat: biocypher integration with adapters`

## Phase 5: Observational KG Validation (P2)
- [ ] 5.1 Run all 10 LinkML adapters
- [ ] 5.2 Document edge schemas
- [ ] 5.3 Validate outputs against domain schemas
- [ ] 5.4 Add missing ontologies (GO, ChEBI, SO, NCBITaxon)
- [ ] COMMIT: `feat: observational kg validation and missing ontologies`
