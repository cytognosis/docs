# Cytos Knowledge Graph: Full Audit

> Generated: 2026-05-12 | Pre-Phase-I checkpoint

## KG Totals

| Metric | Value |
|--------|-------|
| **Total Nodes** | **9,673,136** |
| **Total Edges** | **60,111,215** |
| BioLink Categories | 39 |
| Distinct Edge Predicates | 25+ |
| Distinct Edge Sources | 907 |
| SSSOM Mapping Edges | 48,969 (consolidated) + 1,273,903 (OLS4) |
| Neo4j Export | ✅ (nodes: 1.0 GB, edges: 3.0 GB CSV) |
| Parquet Export | ✅ (nodes: 189 MB, edges: 406 MB) |

---

## 1. Node Categories (39 BioLink types)

| Category | Nodes | % |
|----------|------:|--:|
| biolink:OrganismTaxon | 1,592,901 | 16.5% |
| biolink:ClinicalFinding | 1,393,204 | 14.4% |
| biolink:Disease | 959,278 | 9.9% |
| biolink:ClinicalAttribute | 732,460 | 7.6% |
| biolink:NamedThing | 707,133 | 7.3% |
| biolink:Procedure | 681,385 | 7.0% |
| biolink:InformationContentEntity | 557,921 | 5.8% |
| biolink:Drug | 517,649 | 5.4% |
| biolink:ChemicalEntity | 397,951 | 4.1% |
| biolink:AnatomicalEntity | 390,814 | 4.0% |
| biolink:EnvironmentalFeature | 366,145 | 3.8% |
| biolink:PhenotypicFeature | 237,703 | 2.5% |
| biolink:BiologicalProcess | 229,041 | 2.4% |
| biolink:Protein | 212,434 | 2.2% |
| biolink:CellLine | 167,186 | 1.7% |
| biolink:Gene | 141,230 | 1.5% |
| biolink:ExperimentalFactor | 97,298 | 1.0% |
| biolink:Cell | 92,726 | 1.0% |
| biolink:Device | 70,197 | 0.7% |
| biolink:MolecularActivity | 27,097 | 0.3% |
| biolink:ExposureEvent | 20,817 | 0.2% |
| biolink:NucleicAcidEntity | 16,792 | 0.2% |
| biolink:Activity | 12,644 | 0.1% |
| biolink:CellularComponent | 7,989 | <0.1% |
| biolink:IndividualOrganism | 7,792 | <0.1% |
| biolink:PhenotypicQuality | 7,746 | <0.1% |
| biolink:PopulationOfIndividualOrganisms | 6,099 | <0.1% |
| biolink:GeographicLocation | 4,698 | <0.1% |
| biolink:Behavior | 4,244 | <0.1% |
| biolink:Agent | 3,120 | <0.1% |
| biolink:Pathway | 2,746 | <0.1% |
| biolink:LifeStage | 2,040 | <0.1% |
| biolink:Phenomenon | 1,890 | <0.1% |
| biolink:SoftwareOrTool | 1,120 | <0.1% |
| biolink:PathologicalProcess | 1,106 | <0.1% |
| biolink:GenomicEntity | 347 | <0.1% |
| biolink:OntologyClass | 127 | <0.1% |
| biolink:RelationshipType | 54 | <0.1% |
| biolink:MolecularEntity | 12 | <0.1% |

---

## 2. Node Sources Breakdown

| Source Layer | Nodes | % |
|-------------|------:|--:|
| UMLS vocabularies (`umls:*`) | 3,207,892 | 33.2% |
| Unattributed (UMLS base concepts) | 1,814,507 | 18.8% |
| Other UMLS-origin (SAB names) | 3,610,140 | 37.3% |
| OWL ontologies (`owl:*`) | 644,940 | 6.7% |
| SNOMED CT (`snomed*`) | 389,092 | 4.0% |
| HRA / CCF (`hra*`) | 6,565 | 0.1% |

---

## 3. Ingested OWL Ontologies (32 parsed)

| Ontology | Prefix | Nodes | Edges | OWL Size |
|----------|--------|------:|------:|----------|
| EFO | EFO | 93,299 | 156,651 | 332M |
| OBA | OBA | 82,874 | 205,725 | 159M |
| MONDO | MONDO | 58,940 | 98,023 | 232M |
| GO | GO | 51,937 | 74,905 | 124M |
| CLO | CLO | 43,327 | 61,633 | 42M |
| FOODON | FOODON | 39,682 | 55,403 | 189M |
| PCL | PCL | 37,210 | 62,182 | 160M |
| MP | MP | 35,151 | 81,038 | 98M |
| HP | HP | 32,085 | 55,946 | 73M |
| UBERON | UBERON | 27,295 | 72,293 | 94M |
| DOID | DOID | 19,493 | — | 27M |
| CL | CL | 19,150 | 48,516 | 63M |
| ECTO | ECTO | 16,807 | — | 58M |
| ORDO | ORDO | 15,788 | 50,783 | 7.3M |
| NMDCO | NMDCO | 13,682 | — | 31M |
| PATO | PATO | 8,625 | 18,964 | 21M |
| MAXO | MAXO | 7,120 | — | 16M |
| OBI | OBI | 5,178 | — | 9.4M |
| ONS | ONS | 4,834 | — | 2.8M |
| NBO | NBO | 4,546 | 10,776 | 5.4M |
| CMO | CMO | 4,144 | — | 9.0M |
| HHEAR | HHEAR | 4,010 | — | 8.5M |
| FIDEO | FIDEO | 3,543 | — | 4.1M |
| ZFA | ZFA | 3,285 | 12,293 | 7.1M |
| OPMI | OPMI | 3,153 | — | 4.0M |
| PW | PW | 2,760 | 3,389 | 5.2M |
| XCO | XCO | 1,826 | 2,431 | 4.2M |
| ICO | ICO | 1,558 | — | 1.8M |
| BAO | BAO | 1,534 | — | 1.6M |
| DPO | DPO | 1,552 | — | 3.9M |
| MPATH | MPATH | 891 | 949 | 1.4M |
| MMO | MMO | 869 | 982 | 1.9M |
| WBls | WBls | 796 | 3,408 | 1.8M |
| MF | MF | 400 | 452 | 421K |
| HsapDv | HsapDv | 260 | 366 | 517K |
| FBdv | FBdv | 250 | 712 | 512K |
| MmusDv | MmusDv | 178 | 388 | 359K |
| **Subtotal** | | **644,940** | **~1.08M** | **5.4 GB** |

### Deferred Large Ontologies (5)

| Ontology | Size | Already in KG via | SSSOM Mappings |
|----------|------|-------------------|---------------|
| CHEBI | 775M | 230K nodes (UMLS+bero) | 229K |
| PR (Protein Ontology) | 1.3G | 63K nodes | 239K |
| NCIT | 775M | 313K nodes (UMLS) | 155K |
| DRON | 670M | 6 nodes | 37K |
| UPHENO | 397M | 37K nodes | 701 |

### SSSOM-Only (8, no OWL parse needed)

MBA, DMBA, HBA, DHBA, MESH, HGNC, LIPID MAPS, ICTV

---

## 4. OLS4 SSSOM Cross-Ontology Mappings (45 files, 1,273,903 edges)

| SSSOM Source | Edges | | SSSOM Source | Edges |
|-------------|------:|-|-------------|------:|
| PR | 238,940 | | CL | 3,126 |
| CHEBI | 229,395 | | ZFA | 3,108 |
| NCIT | 155,054 | | XCO | 2,870 |
| MONDO | 146,765 | | OBI | 2,097 |
| LIPIDMAPS | 119,807 | | PW | 2,048 |
| ORDO | 56,774 | | BAO | 1,986 |
| UBERON | 49,369 | | PATO | 1,551 |
| DOID | 37,839 | | MAXO | 1,447 |
| DRON | 36,593 | | MMO | 884 |
| EFO | 36,071 | | MPATH | 744 |
| HP | 33,565 | | NBO | 727 |
| GO | 26,807 | | OPMI | 512 |
| MESH | 21,554 | | ICO | 377 |
| CLO | 20,624 | | ONS | 258 |
| PCL | 13,502 | | +13 small | <200 ea |
| OBA | 11,890 | | | |
| MP | 10,244 | | | |
| CMO | 6,114 | | | |

---

## 5. UMLS Vocabularies: Used vs Not Used

### ✅ Ingested (36 SABs)

| SAB | Nodes | Edges (approx) | Category |
|-----|------:|------:|----------|
| NCBI (Taxonomy) | 780,948 + 680,038 | 1,561,662 | Taxonomic |
| SNOMEDCT_US | 386,110 + 286,876 | 3,065,940 + 1,356,762 | Clinical terminology |
| MSH (MeSH) | 355,278 + 415,988 | 2,554,012 | Medical subjects |
| MEDCIN | 338,800 | 2,332,110 | Clinical |
| LNC (LOINC) | 301,558 + 203,897 | 4,061,656 | Lab observations |
| NCI (NCI Thesaurus) | 200,820 + 119,467 | 2,784,812 | Cancer terminology |
| ICD10PCS | 192,560 + 192,180 | 385,118 | Procedure codes |
| RXNORM | 128,902 + 108,878 | 1,673,436 | Drug terminology |
| OMIM | 112,121 + 73,091 | 542,082 | Genetic disorders |
| SNMI (SNOMED Intl) | 109,023 + 13,242 | 343,574 | Clinical (intl) |
| FMA | 104,364 + 90,283 | 366,852 | Anatomy |
| ICD10CM | 98,506 + 62,461 | 215,446 | Diagnosis codes |
| UWDA | 62,285 + 3,151 | 190,308 | Digital anatomy |
| CHV | 57,795 + 4,627 | — | Consumer health |
| HGNC | 44,067 | — | Gene nomenclature |
| GS (Gold Standard) | 40,832 + 10,861 | — | Drug info |
| GO (Gene Ontology) | 40,214 + 54,289 | 238,658 | Gene function |
| SNOMEDCT_VET | 35,716 + 30,695 | 99,340 | Veterinary |
| SNM | 30,937 + 2,989 | 69,598 | SNOMED legacy |
| ICD9CM | 22,406 + 7,689 | — | Legacy dx codes |
| AOD | 19,920 + 5,051 | 78,824 | Alcohol/drugs |
| HPO | 19,393 + 14,073 | 52,128 | Phenotypes |
| PDQ | 13,325 + 1,508 | — | Cancer info |
| ICD10 | 12,318 + 4,125 | — | WHO ICD-10 |
| DRUGBANK | 11,047 + 5,322 | — | Drug database |
| PSY | 7,961 + 1,556 | 51,692 | Psychology |
| MEDLINEPLUS | 3,889 | — | Consumer health |
| NEU | 3,269 + 1,517 | — | Neuronames |
| MTH | 2,657 | 1,126,634 | Metathesaurus |
| PCDS | 2,174 + 1,938 | — | Primary care |
| WHO | 1,724 | — | WHO ATC |
| ICF | 1,495 + 1,054 | — | Functioning |
| CDCREC | 1,324 | — | Race/ethnicity |
| CCS | 1,188 | — | Clinical classif |
| DSM-5 | 873 + 521 | — | Psychiatry |
| JABL | 724 | — | Japanese bilingual |

### ⏭ Not Ingested (Available in UMLS but not added)

| SAB | Why Excluded | Available? |
|-----|-------------|-----------|
| DDB | Diseases Database — low utility, redundant with MONDO/DOID | Yes |
| CPT | Already partially in (45K nodes via UMLS auto-include) | Partial |
| ATC | Already partially in (1.8K nodes via WHO) | Partial |
| HL7V3.0 / HL7V2.5 | Already partially in (3.6K+2.5K nodes) | Partial |
| VANDF | Already partially in (14.4K nodes) | Partial |
| NDDF | Already partially in (13.9K nodes) | Partial |
| MED-RT | Already partially in (2.6K nodes) | Partial |
| MDR (MedDRA) | Included but non-English variants redundant | Partial |
| RCD (Read Codes) | UK-specific, already in (30K nodes) | Partial |

> [!NOTE]
> Many SABs entered the KG automatically through UMLS MRCONSO/MRREL processing. The "36 explicitly targeted" list above is what we deliberately ingested; dozens of additional SABs came along via cross-references.

---

## 6. Biothings DDE Registry Schemas

### Downloaded (16 files, 8 with content)

| Schema File | Status | Classes | Disposition |
|-------------|--------|--------:|------------|
| **Gene.json** | ✅ Content | 28K | **Using** — field mapping reference for gene instance schema |
| **Dataset.json** | ✅ Content | 34K | **Using** — aligned with our datasets.yaml (DCAT+Croissant) |
| **Taxon.json** | ✅ Content | 26K | **Using** — maps to our OrganismTaxon via NCBITaxon |
| **Taxon_draft.json** | ✅ Content | 26K | Reference only (draft version) |
| **MolecularEntity_draft.json** | ✅ Content | 35K | **Using** — reference for ChemicalEntity/Drug schema |
| **schema_org.jsonld** | ✅ Content | 1.5M | Full Schema.org vocabulary — reference backbone |
| BioSample.json | ❌ Stub (14B) | 0 | **Rejected** — empty, no useful content |
| BioSample_draft.json | ❌ Stub | 0 | Rejected |
| ChemicalSubstance.json | ❌ Stub | 0 | Rejected |
| ChemicalSubstance_draft.json | ❌ Stub | 0 | Rejected |
| DataCatalog.json | ❌ Stub | 0 | Rejected |
| DataCatalog_draft.json | ❌ Stub | 0 | Rejected |
| Dataset_draft.json | ❌ Stub | 0 | Rejected |
| Gene_draft.json | ❌ Stub | 0 | Rejected |
| MolecularEntity.json | ❌ Stub | 0 | Rejected |
| Protein.json | ❌ Stub | 0 | Rejected |
| Protein_draft.json | ❌ Stub | 0 | Rejected |

### NOT Downloaded from DDE Registry (~1,154 remaining)

> [!IMPORTANT]
> The Biothings DDE registry at `discovery.biothings.io` indexes **1,170+ schemas**. We downloaded only the 8 Bioschemas.org profiles relevant to our entity types. The remaining ~1,154 are:
> - Community-contributed schemas (many incomplete/draft)
> - Domain-specific schemas (agriculture, environmental, etc.)
> - Duplicate/versioned copies of the same base schemas
>
> **Decision**: We do NOT need to fetch all 1,170+. The 5 with actual content (Gene, Dataset, Taxon, MolecularEntity, schema_org) provide sufficient cross-reference for our LinkML alignment. Our own v0.4.0 schema is more comprehensive than anything in the DDE registry.

### What We Already Have That Supersedes DDE

| DDE Schema | Our Equivalent | Status |
|-----------|---------------|--------|
| Gene | biolink:Gene + Ensembl table (planned) | ✅ Covered |
| Protein | biolink:Protein + UniProt (planned) | ✅ Covered |
| Dataset | datasets.yaml (DCAT+Croissant+RO-Crate) | ✅ Superior |
| ChemicalSubstance | biolink:ChemicalEntity + ChEBI | ✅ Covered |
| MolecularEntity | biolink:MolecularEntity | ✅ Covered |
| BioSample | Not yet — will add in Phenopackets phase | Planned |
| DataCatalog | Not needed (we use DCAT) | N/A |
| Taxon | biolink:OrganismTaxon + 1.6M NCBITaxon | ✅ Covered |

---

## 7. SNOMED CT (Separate from UMLS)

| Component | Nodes | Edges |
|-----------|------:|------:|
| SNOMED International | 381,251 | 1,341,414 |
| SNOMED US Extension | 7,841 | 1,356,762 |
| Simple Maps (Intl) | — | 555,671 |
| Simple Maps (US) | — | 552,575 |
| Extended Maps (US) | — | 314,179 |
| **Total** | **389,092** | **4,120,601** |

---

## 8. HRA / Human Reference Atlas

| Component | Count |
|-----------|------:|
| HRA CCF Nodes | 6,565 |
| ASCT+B Cell Types | ~2,600 |
| Anatomical Structures | ~5,800 |
| Spatial Placements | 101 KB parquet |

---

## 9. Services Implemented

| Service | Status | Tested |
|---------|--------|--------|
| OLS4 REST Client | ✅ | ✅ |
| Biothings REST Client (Gene/Variant/Chem/Disease) | ✅ | ✅ |
| Open Targets GraphQL Client | ✅ | ✅ |
| CellxGene / HBCA Integration | ✅ | ✅ (28K cells) |
| TileDB-SOMA Backend | ✅ | ✅ |
| AnnData Import/Export | ✅ | ✅ |
| Ontology Validation (against KG) | ✅ | ✅ |

---

## 10. Phase II Variant Pipeline — Test Data

### Test Dataset 1: Olivia WGS (single individual, temporary)

| File | Type | Size | Process Order |
|------|------|------|--------------|
| `*.snp-indel.genome.vcf.gz` | SNP/Indel | 284M | **1st** |
| `*.sv.vcf.gz` | Structural Variants | 732K | **2nd** |
| `*.cnv.vcf.gz` | Copy Number | 28K | **3rd** |
| `*.1.fq.gz` | FASTQ R1 | 38G | Reference only |
| `*.2.fq.gz` | FASTQ R2 | 38G | Reference only |

> **Policy**: Parse and test pipeline. Do NOT persist. Drop after validation.

### Test Dataset 2: PsychENCODE (cohort, permanent)

| File | Type | Size | Samples |
|------|------|------|---------|
| `brainSCOPE_PEC_sample_genotypes_no_rna.vcf.gz` | Imputed Genotypes | 94M | Multi-sample cohort |

> **Policy**: Harmonize and persist in TileDB-VCF after pipeline validation.

### Variant Categories to Support

| Category | Sources | Storage |
|----------|---------|---------|
| **Common variants (GWAS)** | Pan-UKBB, GWAS Catalog | Summary stats in Parquet |
| **Rare variants (WGS/WES)** | Test VCFs above, ClinVar | TileDB-VCF arrays |
| **Array data** | Imputed genotypes (PsychENCODE) | TileDB-VCF arrays |

---

## 11. Top Edge Predicates

| Predicate | Edges | % |
|-----------|------:|--:|
| biolink:related_to | 23,911,832 | 39.8% |
| biolink:subclass_of | 12,017,116 | 20.0% |
| biolink:superclass_of | 7,705,727 | 12.8% |
| skos:exactMatch | 4,479,403 | 7.5% |
| biolink:has_attribute | 3,917,736 | 6.5% |
| biolink:same_as | 3,197,755 | 5.3% |
| skos:closeMatch | 2,219,303 | 3.7% |
| biolink:mapped_to | 833,284 | 1.4% |
| biolink:classified_as | 378,930 | 0.6% |
| Other (16+ predicates) | 1,450,129 | 2.4% |
