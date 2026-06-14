# Cytos Ontology Catalog

> Last updated: 2026-05-12 | **45+ ontology prefixes** | **~2.4M ontology-derived nodes**

## Newly Added Ontologies (2026-05-12)

| Prefix | Name | Nodes | Edges | Entity Types | Status |
|--------|------|------:|------:|-------------|--------|
| **SO** | Sequence Ontology | 2,747 | 3,140 | GenomicEntity (gene, transcript, pseudogene, exon, intron, UTR, variant, repeat) | ✅ Ingested |
| **MI** | Molecular Interactions | 1,656 | 1,665 | MolecularActivity (interaction detection method, interaction type, participant ID method) | ✅ Ingested |
| **SBO** | Systems Biology Ontology | 695 | 745 | BiologicalProcess (mathematical framework, modeling framework, kinetic law, material entity) | ✅ Ingested |
| **EDAM** | EDAM Bioinformatics Ontology | 3,524 | 4,616 | InformationContentEntity (data type, format, operation, topic, identifier) | ✅ Ingested |
| **PGO** | Pseudogene Ontology | — | — | — | ⛔ Deprecated, subsumed by SO |

> [!NOTE]
> PGO is no longer maintained. The Sequence Ontology (SO) contains all pseudogene-related terms (`SO:0000336` pseudogene, `SO:0001760` transcribed_pseudogene, etc.) and is the OBO Foundry standard.

## Complete Ontology Table

### Biomedical Core

| Prefix | Full Name | Nodes | Entity Types | Download URL | Data Lake Path | Version (Ours) | Latest Available |
|--------|-----------|------:|-------------|-------------|----------------|----------------|-----------------|
| GO | Gene Ontology | 47,429 | BiologicalProcess, MolecularFunction, CellularComponent | [OBO PURL](http://purl.obolibrary.org/obo/go.owl) | [go.owl](file:///home/mohammadi/datasets/01-ontologies/latest/go.owl) | 2026-03-25 | 2026-03-25 |
| CHEBI | Chemical Entities of Biological Interest | 774,258 | ChemicalEntity, Drug, Metabolite, Ion, Functional Group | [OBO PURL](http://purl.obolibrary.org/obo/chebi.owl) | [chebi.owl](file:///home/mohammadi/datasets/01-ontologies/latest/chebi.owl) | Release 252 | 252 |
| PR | Protein Ontology | 568,459 | Protein, ProteinComplex, ProteinFamily | [OBO PURL](http://purl.obolibrary.org/obo/pr.owl) | [pr.owl](file:///home/mohammadi/datasets/01-ontologies/latest/pr.owl) | Latest | Latest |
| NCIT | NCI Thesaurus | 208,222 | Disease, Gene, Drug, AnatomicalEntity, Procedure | [OBO PURL](http://purl.obolibrary.org/obo/ncit.owl) | [ncit.owl](file:///home/mohammadi/datasets/01-ontologies/latest/ncit.owl) | Latest | Latest |
| OBI | Ontology for Biomedical Investigations | 6,677 | InformationContentEntity, Assay, Protocol, Instrument | [OBO PURL](http://purl.obolibrary.org/obo/obi.owl) | [obi.owl](file:///home/mohammadi/datasets/01-ontologies/latest/obi.owl) | 2026-03-19 | 2026-03-19 |
| OBIB | Ontology for Biobanking | 12 | InformationContentEntity, Specimen, Repository | [BioPortal](https://bioportal.bioontology.org/ontologies/OBIB) | [via OBI imports](file:///home/mohammadi/datasets/01-ontologies/latest/obi.owl) | Latest | Latest |

### Disease & Phenotype

| Prefix | Full Name | Nodes | Entity Types | Download URL | Data Lake Path | Version (Ours) | Latest Available |
|--------|-----------|------:|-------------|-------------|----------------|----------------|-----------------|
| MONDO | MONDO Disease Ontology | 126,132 | Disease, RareDisease, InfectiousDisease | [OBO PURL](http://purl.obolibrary.org/obo/mondo.owl) | [mondo.owl](file:///home/mohammadi/datasets/01-ontologies/latest/mondo.owl) | 2026-05-05 | 2026-05-05 |
| DOID | Human Disease Ontology | 27,786 | Disease, Syndrome, DiseaseStage | [OBO PURL](http://purl.obolibrary.org/obo/doid.owl) | [doid.owl](file:///home/mohammadi/datasets/01-ontologies/latest/doid.owl) | 2026-04-30 | 2026-04-30 |
| ORDO | Orphanet Rare Disease Ontology | 22,000 | Disease, RareDisease, GeneticDisease | [Orphadata](https://www.orphadata.com) | [ordo.owl](file:///home/mohammadi/datasets/01-ontologies/latest/ordo.owl) | 4.7 | 4.7 |
| HP | Human Phenotype Ontology | 27,389 | PhenotypicFeature, ClinicalModifier, InheritancePattern | [OBO PURL](http://purl.obolibrary.org/obo/hp.owl) | [hp.owl](file:///home/mohammadi/datasets/01-ontologies/latest/hp.owl) | 2026-02-16 | 2026-04-22 |
| MP | Mammalian Phenotype Ontology | 44,515 | PhenotypicFeature (morphological, behavioral, physiological) | [OBO PURL](http://purl.obolibrary.org/obo/mp.owl) | [mp.owl](file:///home/mohammadi/datasets/01-ontologies/latest/mp.owl) | 2026-04-22 | 2026-04-22 |
| PATO | Phenotypic Quality Ontology | 10,145 | PhenotypicQuality (size, color, shape, mass, morphology) | [OBO PURL](http://purl.obolibrary.org/obo/pato.owl) | [pato.owl](file:///home/mohammadi/datasets/01-ontologies/latest/pato.owl) | 2025-05-14 | 2025-05-14 |
| MAXO | Medical Action Ontology | 6,077 | Procedure, TherapeuticIntervention, DiagnosticProcedure | [OBO PURL](http://purl.obolibrary.org/obo/maxo.owl) | [maxo.owl](file:///home/mohammadi/datasets/01-ontologies/latest/maxo.owl) | Latest | Latest |

### Anatomy & Cell Biology

| Prefix | Full Name | Nodes | Entity Types | Download URL | Data Lake Path | Version (Ours) | Latest Available |
|--------|-----------|------:|-------------|-------------|----------------|----------------|-----------------|
| UBERON | Uber Anatomy Ontology | 105,112 | AnatomicalEntity, Tissue, Organ, BodyFluid | [OBO PURL](http://purl.obolibrary.org/obo/uberon.owl) | [uberon.owl](file:///home/mohammadi/datasets/01-ontologies/latest/uberon.owl) | 2026-04-01 | 2026-04-01 |
| CL | Cell Ontology | 21,039 | Cell, NeuralCell, ImmuneCell, StemCell | [OBO PURL](http://purl.obolibrary.org/obo/cl.owl) | [cl.owl](file:///home/mohammadi/datasets/01-ontologies/latest/cl.owl) | 2026-03-26 | 2026-03-26 |
| PCL | Provisional Cell Ontology | 22,278 | Cell (provisional scRNA-seq derived cell types) | [OBO PURL](http://purl.obolibrary.org/obo/pcl.owl) | [pcl.owl](file:///home/mohammadi/datasets/01-ontologies/latest/pcl.owl) | Latest | Latest |
| CLO | Cell Line Ontology | 39,520 | CellLine, HybridomaCellLine, StemCellLine | [OBO PURL](http://purl.obolibrary.org/obo/clo.owl) | [clo.owl](file:///home/mohammadi/datasets/01-ontologies/latest/clo.owl) | Latest | Latest |
| CCF | Common Coordinate Framework (HRA) | 1,713 | AnatomicalEntity, SpatialEntity, ReferenceOrgan | [HuBMAP](https://hubmapconsortium.github.io/ccf-ontology/) | [ccf.owl](file:///home/mohammadi/datasets/05-annotations/HRA/ccf.owl) | v2.4 | v2.4 |
| ZFA | Zebrafish Anatomy | 6,530 | AnatomicalEntity (zebrafish structures) | [OBO PURL](http://purl.obolibrary.org/obo/zfa.owl) | [zfa.owl](file:///home/mohammadi/datasets/01-ontologies/latest/zfa.owl) | Latest | Latest |
| MPATH | Mouse Pathology | 1,465 | PathologicalProcess (lesion, neoplasm, degeneration) | [OBO PURL](http://purl.obolibrary.org/obo/mpath.owl) | [mpath.owl](file:///home/mohammadi/datasets/01-ontologies/latest/mpath.owl) | Latest | Latest |

### Genomics & Sequence

| Prefix | Full Name | Nodes | Entity Types | Download URL | Data Lake Path | Version (Ours) | Latest Available |
|--------|-----------|------:|-------------|-------------|----------------|----------------|-----------------|
| **SO** | **Sequence Ontology** | **2,747** | GenomicEntity (gene, transcript, exon, pseudogene, variant, repeat, UTR, CDS) | [OBO PURL](http://purl.obolibrary.org/obo/so.owl) | [so.owl](file:///home/mohammadi/datasets/01-ontologies/latest/so.owl) | 2024-11-18 | 2024-11-18 |
| GENO | Genotype Ontology | 256 | GenomicEntity (genotype, allele, haplotype, zygosity) | [OBO PURL](http://purl.obolibrary.org/obo/geno.owl) | [geno.owl](file:///home/mohammadi/datasets/01-ontologies/experimental/geno.owl) | Latest | Latest |
| UniProtKB | UniProt Knowledgebase | 574,627 | Protein (reviewed/unreviewed protein entries) | [UniProt FTP](https://ftp.uniprot.org/pub/databases/uniprot/) | [via core KG](file:///home/mohammadi/datasets/04-identifiers/uniprot/) | 2026_02 | 2026_02 |

### Chemistry & Pharmacology

| Prefix | Full Name | Nodes | Entity Types | Download URL | Data Lake Path | Version (Ours) | Latest Available |
|--------|-----------|------:|-------------|-------------|----------------|----------------|-----------------|
| DrugBank | DrugBank | 19,004 | Drug, DrugInteraction, DrugTarget | [DrugBank](https://go.drugbank.com/releases) | via PrimeKG | Latest | Latest |
| DRON | Drug Ontology | 100 | Drug, DrugProduct, ActiveIngredient | [OBO PURL](http://purl.obolibrary.org/obo/dron.owl) | [dron.owl](file:///home/mohammadi/datasets/01-ontologies/latest/dron.owl) | Latest | Latest |

### Experimental & Measurement

| Prefix | Full Name | Nodes | Entity Types | Download URL | Data Lake Path | Version (Ours) | Latest Available |
|--------|-----------|------:|-------------|-------------|----------------|----------------|-----------------|
| EFO | Experimental Factor Ontology | 18,466 | ExperimentalFactor, Assay, Material, DiseaseModel | [EBI](https://www.ebi.ac.uk/efo/) | [efo.owl](file:///home/mohammadi/datasets/01-ontologies/latest/efo.owl) | v3.89.0 | v3.89.0 |
| **MI** | **Molecular Interactions** | **1,656** | MolecularActivity (interaction detection, interaction type, feature type, participant ID) | [OBO PURL](http://purl.obolibrary.org/obo/mi.owl) | [mi.owl](file:///home/mohammadi/datasets/01-ontologies/latest/mi.owl) | Latest | Latest |
| **SBO** | **Systems Biology Ontology** | **695** | BiologicalProcess (modeling framework, math expression, kinetic constant, material entity) | [OBO PURL](http://purl.obolibrary.org/obo/sbo.owl) | [sbo.owl](file:///home/mohammadi/datasets/01-ontologies/latest/sbo.owl) | 2021-08-28 | 2021-08-28 |
| CMO | Clinical Measurement Ontology | 4,884 | ClinicalAttribute (blood chemistry, body weight, organ weight) | [OBO PURL](http://purl.obolibrary.org/obo/cmo.owl) | [cmo.owl](file:///home/mohammadi/datasets/01-ontologies/latest/cmo.owl) | Latest | Latest |
| MMO | Measurement Method Ontology | 869 | InformationContentEntity (assay, measurement method) | [OBO PURL](http://purl.obolibrary.org/obo/mmo.owl) | [mmo.owl](file:///home/mohammadi/datasets/01-ontologies/latest/mmo.owl) | Latest | Latest |
| XCO | Experimental Condition Ontology | 1,822 | ExperimentalFactor (diet, drug treatment, surgical procedure) | [OBO PURL](http://purl.obolibrary.org/obo/xco.owl) | [xco.owl](file:///home/mohammadi/datasets/01-ontologies/latest/xco.owl) | Latest | Latest |
| UO | Units of Measurement | 412 | QuantityValue (SI units, derived units, prefixes) | [BioPortal](https://bioportal.bioontology.org/ontologies/UO) | via core imports | Latest | Latest |
| BAO | BioAssay Ontology | — | ExperimentalFactor (bioassay, screening, endpoint) | [BioPortal](https://bioportal.bioontology.org/ontologies/BAO) | [bao.owl](file:///home/mohammadi/datasets/01-ontologies/latest/bao.owl) | Latest | Latest |

### Developmental Stages

| Prefix | Full Name | Nodes | Entity Types | Download URL | Data Lake Path | Version (Ours) | Latest Available |
|--------|-----------|------:|-------------|-------------|----------------|----------------|-----------------|
| HsapDv | Human Developmental Stages | 601 | LifeStage (embryo, fetal, postnatal, adult stages) | [OBO PURL](http://purl.obolibrary.org/obo/hsapdv.owl) | [hsapdv.owl](file:///home/mohammadi/datasets/01-ontologies/latest/hsapdv.owl) | 2025-01-23 | 2025-01-23 |
| MmusDv | Mouse Developmental Stages | 312 | LifeStage (Theiler, postnatal stages) | [OBO PURL](http://purl.obolibrary.org/obo/mmusdv.owl) | [mmusdv.owl](file:///home/mohammadi/datasets/01-ontologies/latest/mmusdv.owl) | Latest | Latest |
| FBdv | Drosophila Developmental Stages | 477 | LifeStage (embryo, larval, pupal, adult) | [OBO PURL](http://purl.obolibrary.org/obo/fbdv.owl) | [fbdv.owl](file:///home/mohammadi/datasets/01-ontologies/latest/fbdv.owl) | Latest | Latest |
| WBls | C. elegans Life Stages | 781 | LifeStage (embryo, larval L1-L4, adult) | [OBO PURL](http://purl.obolibrary.org/obo/wbls.owl) | [wbls.owl](file:///home/mohammadi/datasets/01-ontologies/latest/wbls.owl) | Latest | Latest |

### Environmental & Exposure

| Prefix | Full Name | Nodes | Entity Types | Download URL | Data Lake Path | Version (Ours) | Latest Available |
|--------|-----------|------:|-------------|-------------|----------------|----------------|-----------------|
| ENVO | Environment Ontology | 9,690 | EnvironmentalFeature (biome, habitat, environmental material) | [OBO PURL](http://purl.obolibrary.org/obo/envo.owl) | core imports | Latest | Latest |
| FOODON | Food Ontology | 39,682 | EnvironmentalFeature (food product, ingredient, preparation) | [OBO PURL](http://purl.obolibrary.org/obo/foodon.owl) | [foodon.owl](file:///home/mohammadi/datasets/01-ontologies/latest/foodon.owl) | Latest | Latest |
| ECTO | Exposure/Conditions Ontology | 3,748 | ExposureEvent (chemical, occupational, radiation) | [OBO PURL](http://purl.obolibrary.org/obo/ecto.owl) | [ecto.owl](file:///home/mohammadi/datasets/01-ontologies/latest/ecto.owl) | Latest | Latest |
| HHEAR | Human Health Exposure | 2,261 | ExposureEvent (environmental agent, pathway, biomarker) | [BioPortal](https://bioportal.bioontology.org/ontologies/HHEAR) | [hhear.owl](file:///home/mohammadi/datasets/01-ontologies/latest/hhear.owl) | Latest | Latest |

### Pathway & Process

| Prefix | Full Name | Nodes | Entity Types | Download URL | Data Lake Path | Version (Ours) | Latest Available |
|--------|-----------|------:|-------------|-------------|----------------|----------------|-----------------|
| PW | Pathway Ontology | 2,746 | Pathway (signaling, metabolic, regulatory, disease) | [OBO PURL](http://purl.obolibrary.org/obo/pw.owl) | [pw.owl](file:///home/mohammadi/datasets/01-ontologies/latest/pw.owl) | Latest | Latest |
| REACTOME | Reactome Pathway DB | 2,516 | Pathway (signaling, metabolism, cell cycle) | [Reactome](https://reactome.org) | via PrimeKG | Latest | Latest |

### Informatics & Data Science

| Prefix | Full Name | Nodes | Entity Types | Download URL | Data Lake Path | Version (Ours) | Latest Available |
|--------|-----------|------:|-------------|-------------|----------------|----------------|-----------------|
| **EDAM** | **EDAM Bioinformatics Ontology** | **3,524** | InformationContentEntity (data type, file format, bioinformatics operation, research topic) | [EDAM stable](https://edamontology.org/EDAM_stable.owl) | [edam.owl](file:///home/mohammadi/datasets/01-ontologies/latest/edam.owl) | 1.25 | 1.25 |
| AIO | Artificial Intelligence Ontology | 442 | InformationContentEntity (AI method, architecture, task) | [BioPortal](https://bioportal.bioontology.org/ontologies/AIO) | [05-annotations/topic-areas/](file:///home/mohammadi/datasets/05-annotations/topic-areas/) | 2024 | 2024 |
| CSO | Computer Science Ontology | 14,736 | InformationContentEntity (CS topic, research area) | [CSO Portal](https://cso.kmi.open.ac.uk) | [05-annotations/topic-areas/](file:///home/mohammadi/datasets/05-annotations/topic-areas/) | 3.5 | 3.5 |
| IAO | Information Artifact Ontology | 453 | InformationContentEntity (document, datum, plan spec) | [OBO PURL](http://purl.obolibrary.org/obo/iao.owl) | via imports | Latest | Latest |

### Neuro-Specific

| Prefix | Full Name | Nodes | Entity Types | Download URL | Data Lake Path | Version (Ours) | Latest Available |
|--------|-----------|------:|-------------|-------------|----------------|----------------|-----------------|
| NBO | Neuro Behavior Ontology | 2,467 | Behavior (locomotion, feeding, social, cognitive) | [OBO PURL](http://purl.obolibrary.org/obo/nbo.owl) | [nbo.owl](file:///home/mohammadi/datasets/01-ontologies/latest/nbo.owl) | Latest | Latest |
| HANCESTRO | Human Ancestry Ontology | 1,472 | PopulationOfIndividualOrganisms (ancestry, ethnicity) | [OBO PURL](http://purl.obolibrary.org/obo/hancestro.owl) | [singlecell/hancestro.owl](file:///home/mohammadi/datasets/01-ontologies/singlecell/hancestro.owl) | Latest | Latest |

### Precision Medicine & Investigation

| Prefix | Full Name | Nodes | Entity Types | Download URL | Data Lake Path | Version (Ours) | Latest Available |
|--------|-----------|------:|-------------|-------------|----------------|----------------|-----------------|
| OPMI | Ontology for Precision Medicine Investigation | 630 | InformationContentEntity (precision medicine study design) | [BioPortal](https://bioportal.bioontology.org/ontologies/OPMI) | [opmi.owl](file:///home/mohammadi/datasets/01-ontologies/latest/opmi.owl) | Latest | Latest |
| ONS | Ontology for Nutritional Studies | 488 | InformationContentEntity (dietary assessment, nutrient) | [OBO PURL](http://purl.obolibrary.org/obo/ons.owl) | [ons.owl](file:///home/mohammadi/datasets/01-ontologies/latest/ons.owl) | Latest | Latest |
| ICO | Informed Consent Ontology | — | InformationContentEntity (consent form, regulatory doc) | [OBO PURL](http://purl.obolibrary.org/obo/ico.owl) | [ico.owl](file:///home/mohammadi/datasets/01-ontologies/latest/ico.owl) | Latest | Latest |

## Deprecated / Not Ingested

| Prefix | Name | Reason |
|--------|------|--------|
| PGO | Pseudogene Ontology | Deprecated; all pseudogene terms in SO |
| GENCODE | GENCODE Annotations | Not an ontology; GTF/GFF3 gene annotation set. Covered by Ensembl 115 gene data |

## Summary Statistics

| Category | Count |
|----------|------:|
| Total ontology prefixes in KG | 45+ |
| OWL files in data lake | 73 |
| Data lake `01-ontologies/` size | 75 GB |
| Ontology-derived nodes (est.) | ~2.4M |
| Ontology hierarchy edges (est.) | ~2.2M |
| Cross-ontology SSSOM edges | 1,132,396 |
| Newly added (this session) | 4 (SO, MI, SBO, EDAM) |
