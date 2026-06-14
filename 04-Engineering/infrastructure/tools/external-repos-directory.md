# External Repository Directory

> **Status**: Active
> **Date**: 2026-06-14
> **Author**: @mohammadi
> **Audience**: engineers, researchers
> **Tags**: `tools`, `external-repos`, `dependencies`

**Source**: Cytognosis curations archive | **Last updated**: 2026-06-14
**Coverage**: 10+ major open-source ecosystems with Cytognosis-relevance annotations

> A reference guide to external GitHub organizations and repositories that Cytognosis
> has evaluated, cloned, or actively uses. Each entry includes: GitHub/website links,
> local clone location (if applicable), license, publication reference, what it is,
> Cytognosis relevance, and a table of key repositories.

**Quick Navigation**:
[BioContextAI](#1-biocontextai) ·
[BioCypher](#2-biocypher) ·
[GA4GH](#3-ga4gh-global-alliance-for-genomics-and-health) ·
[KGHub](#4-knowledge-graph-hub-kghub) ·
[LinkML](#5-linkml) ·
[Monarch Initiative](#6-monarch-initiative) ·
[NCATS Translator](#7-ncats-translator) ·
[AI2 / Semantic Scholar](#8-allen-institute-for-ai-ai2) ·
[FAIRDOM-SEEK / WorkflowHub](#9-fairdom-seek--workflowhub) ·
[RO-Crate / ResearchObject](#10-ro-crate--researchobject)

---

# **Cytognosis External Resource Directory**

**Purpose:** Harmonized reference for all external organizational repositories cloned into the Cytognosis development environment.  
**Last updated:** March 2026

---

## 1\. BioContextAI

**GitHub:** [https://github.com/biocontext-ai](https://github.com/biocontext-ai)  
**Website:** [https://biocontext.ai](https://biocontext.ai)  
**Local folder:** `AI_scientist/biocontext-ai/`  
**License:** Apache 2.0  
**Publication:** Nature Biotechnology (2025), doi:10.1038/s41587-025-02900-9

**What it is:** An open-source initiative bridging LLMs and specialized biomedical knowledge through the Model Context Protocol (MCP). BioContextAI provides standardized, composable infrastructure for AI agents to access validated scientific resources without hallucinations. Community-driven registry of biomedical MCP servers enforcing FAIR principles.

**Relevance to Cytognosis:** Core infrastructure for connecting Cytoverse AI components to biomedical databases via MCP. The registry model and cookiecutter template inform how Cytognosis could expose its own data services as MCP servers.

| Repository | Description |
| :---- | :---- |
| `anndata-mcp` | MCP server for querying AnnData objects (single-cell data) via lazy reading |
| `knowledgebase-mcp` | Production MCP server providing unified access to major biomedical databases (UniProt, NCBI, STRING, etc.) |
| `mcp-server-cookiecutter` | Template for creating new biomedical MCP servers |
| `meta-mcp` | Meta-server for orchestrating multiple MCP servers |
| `protocol-mcp` | MCP protocol specifications and utilities |
| `registry` | Community-curated catalog of biomedical MCP servers with metadata; powers biocontext.ai |
| `simple-mcp-evaluation` | Evaluation scripts for benchmarking MCP server reliability |
| `skill-to-mcp` | Converts Claude Skills format into MCP server resources |
| `website` | Source for biocontext.ai (registry UI, chat interface, documentation) |

---

## 2\. BioCypher

**GitHub:** [https://github.com/biocypher](https://github.com/biocypher)  
**Website:** [https://biocypher.org](https://biocypher.org)  
**Local folder:** `BioCypher_ecosystem/`  
**License:** Apache 2.0  
**Publication:** Nature Biotechnology (peer-reviewed)

**What it is:** An ecosystem for building and using biomedical knowledge graphs and LLMs. The two main projects are BioCypher (modular KG creation framework) and BioChatter (connecting KGs and bioinformatics methods to LLMs). Built around threefold modularity: modular data sources, modular ontology structures, modular output formats. Funded by Horizon 2020/DECIDER, DFG, and Open Targets.

**Relevance to Cytognosis:** Primary framework for constructing the Cytoverse knowledge graph. BioCypher's ontology-grounded, modular approach to KG construction aligns with Cytognosis's multi-scale integration architecture. BioChatter provides the LLM interface layer.

| Repository | Description |
| :---- | :---- |
| `BioCypher` | Core framework for building biomedical knowledge graphs with ontology grounding and modular adapters |
| `BioChatter` | Framework for building biomedical AI agents; connects KGs to LLMs via RAG and prompt engineering |
| `Karenina` | Biomedical data extraction from text and other modalities (under development) |
| `alfredo` | Unified interface for accessing BioCypher ecosystem resources |
| `biotope` | BioCypher adapter collection and pipeline management |
| `biolink-model` | Fork/reference of the Biolink Model ontology used by BioCypher for schema mapping |
| `biolink-model-toolkit` | Python toolkit for working with the Biolink Model |
| `information-resource-registry` | Registry of information resources for knowledge graph provenance tracking |
| `ingest-metadata` | Metadata standards for data ingestion pipelines |
| `kgx` | Knowledge Graph Exchange format and tools (Biolink-compatible) |
| `ontobio` | Library for working with OBO ontologies in Python |
| `resource-ingest-guide-schema` | Schema definitions for standardizing resource ingestion documentation |

---

## 3\. GA4GH (Global Alliance for Genomics and Health)

**GitHub:** [https://github.com/ga4gh](https://github.com/ga4gh)  
**Website:** [https://www.ga4gh.org](https://www.ga4gh.org)  
**Local folder:** `GA4GH/`  
**License:** Apache 2.0 (most repos)  
**Founded:** 2013

**What it is:** An international standards-setting organization developing technical standards and policy frameworks for responsible sharing of genomic and health-related data. Over 500 member organizations across 90+ countries. Standards are developed by eight Work Streams and piloted by 24 Driver Projects. Hosted by Wellcome Sanger Institute, Broad Institute, OICR, and EMBL-EBI.

**Relevance to Cytognosis:** GA4GH standards (VRS, Phenopackets, DRS, Passports) are foundational for Cytoverse's genomic data representation, federated access architecture, and interoperability with major genomic data repositories. Compliance with GA4GH standards strengthens grant applications and data sharing commitments.

| Repository | Description |
| :---- | :---- |
| `GA4GH-RegBot` | Automated tooling for GA4GH registry management |
| `cat-vrs` | Categorical Variation Representation Standard; terminology and data model for describing categorical variation concepts |
| `cat-vrs-python` | Python implementation of CatVRS |
| `data-repository-service-schemas` | DRS (Data Repository Service) API specification; standard for locating and accessing data objects across clouds |
| `data-security` | Data security standards and policies for genomic data sharing |
| `experiments-metadata` | Metadata standards for describing genomic experiments |
| `ga4gh-registry` | Registry of GA4GH-compliant service implementations |
| `ga4gh-sdk` | Software development kit for GA4GH APIs |
| `gks2clinvar` | Tooling to convert GA4GH Genomic Knowledge Standards representations to ClinVar submissions |
| `phenopacket-schema` | Phenopackets: standard for sharing disease and phenotype information for diagnostics and research |
| `tool-registry-service-schemas` | TRS (Tool Registry Service) API specification; standard for sharing computational tools and workflows |
| `va-spec` | Variant Annotation specification; information model for representing variant annotations |
| `va-spec-python` | Python implementation of VA-Spec |
| `vrs` | Variation Representation Standard; computational framework for unambiguous representation of genomic variation |
| `vrs-python` | Python implementation of VRS |

---

## 4\. Knowledge Graph Hub (KGHub)

**GitHub:** [https://github.com/Knowledge-Graph-Hub](https://github.com/Knowledge-Graph-Hub)  
**Website:** [https://kghub.org](https://kghub.org)  
**Local folder:** `KGHub/`  
**License:** BSD-3-Clause (varies by repo)

**What it is:** A platform for building, exchanging, and using biomedical knowledge graphs. Provides standardized pipelines for constructing disease-specific and cross-domain KGs using the Biolink Model and KGX exchange format. Closely affiliated with the Monarch Initiative and NCATS Translator.

**Relevance to Cytognosis:** Disease-specific KGs (Alzheimer's, IDG) provide ready-made knowledge layers for Cytoverse. The KG-Chat and agent-alz-assistant repos demonstrate LLM-KG integration patterns relevant to Cytonome's reasoning layer.

| Repository | Description |
| :---- | :---- |
| `agent-alz-assistant` | AI agent for querying Alzheimer's disease knowledge graphs |
| `kg-alzheimers` | Alzheimer's disease knowledge graph construction pipeline |
| `kg-chat` | Chat interface for querying knowledge graphs via LLMs |
| `kg-idg` | Knowledge graph for Illuminating the Druggable Genome (IDG) targets |
| `kg-obo` | Knowledge graph built from OBO Foundry ontologies |
| `kg-phenio` | Knowledge graph for phenotype and disease ontology integration |
| `kg-registry` | Registry of available knowledge graphs and their metadata |
| `universalizer` | Tool for standardizing node identifiers across knowledge graphs |

---

## 5\. LinkML

**GitHub:** [https://github.com/linkml](https://github.com/linkml)  
**Website:** [https://linkml.io](https://linkml.io)  
**Local folder:** `LinkML/`  
**License:** CC0 1.0 (specifications), Apache 2.0/BSD (tools)

**What it is:** A flexible modeling language for defining data schemas that can be compiled to multiple target formats (JSON Schema, ShEx, SPARQL, SQL DDL, OWL, Python dataclasses, etc.). Used extensively across the biomedical data standards ecosystem, including by Biolink Model, Monarch Initiative, and NCATS Translator.

**Relevance to Cytognosis:** Schema definition language for Cytoverse data models. LinkML enables defining data structures once and generating validators, serializers, and documentation for multiple output targets, supporting Cytognosis's multi-format interoperability requirements.

| Repository | Description |
| :---- | :---- |
| `linkml` | Core LinkML framework: schema language, generators, and tooling |
| `linkml-map` | Data transformation and mapping framework using LinkML schemas |
| `linkml-owl` | OWL generator for LinkML schemas; enables ontology-driven data modeling |
| `linkml-registry` | Registry of publicly available LinkML schemas |
| `linkml-store` | Storage abstraction layer for LinkML-defined data |
| `linkml-tutorial` | Interactive tutorials for learning LinkML |
| `linkml-data-qc` | Data quality control tools for validating data against LinkML schemas |
| `linkml-model` | The LinkML metamodel (LinkML defined in LinkML) |
| `linkml-reference-validator` | Reference implementation of LinkML validation |
| `linkml-solr` | Solr search integration for LinkML-defined data |
| `linkml-term-validator` | Vocabulary and terminology validation for LinkML fields |
| `schema-automator` | Automated schema inference from data files (CSV, JSON, etc.) |
| `schemasheets` | Spreadsheet-based authoring of LinkML schemas |
| `pyjsg` | Python implementation of JSON Schema Grammar (used by LinkML internals) |

---

## 6\. Monarch Initiative

**GitHub:** [https://github.com/monarch-initiative](https://github.com/monarch-initiative)  
**Website:** [https://monarchinitiative.org](https://monarchinitiative.org)  
**Local folder:** `Monarch/`  
**License:** BSD-3-Clause (varies)

**What it is:** An open-science initiative integrating biological information from many sources to build a comprehensive knowledge graph linking genes, diseases, phenotypes, and model organisms. Provides the Biolink Model (the de facto ontology for biomedical KGs), phenotype-driven diagnostics tools, and large-scale data integration pipelines. Funded by NIH/NHGRI.

**Relevance to Cytognosis:** The Monarch KG and Biolink Model are foundational to Cytoverse's disease-gene-phenotype layer. Koza provides the ETL framework pattern, and PhEval enables phenotype-driven model evaluation relevant to precision psychiatry applications.

| Repository | Description |
| :---- | :---- |
| `AI` | AI/ML experiments and tools within the Monarch ecosystem |
| `NCBI-gene-pyobo` | PyOBO adapter for NCBI Gene data |
| `biolink-api` | API for querying the Monarch/Biolink knowledge graph |
| `biolink-model-pydantic` | Pydantic models auto-generated from the Biolink Model schema |
| `ingestion` | Data ingestion pipelines for the Monarch knowledge graph |
| `koza` | Data transformation framework for building Biolink-compatible KGs from diverse sources |
| `kozahub` | Hub for discovering and sharing Koza ingestion configurations |
| `ontologies` | Collection of ontologies used by Monarch (HPO, MONDO, UPHENO, etc.) |
| `pheval` | Framework for evaluating phenotype-driven variant/gene prioritization tools |

---

## 7\. NCATS Translator

**GitHub:** [https://github.com/NCATSTranslator](https://github.com/NCATSTranslator)  
**Website:** [https://ncats.nih.gov/research/research-activities/translator](https://ncats.nih.gov/research/research-activities/translator)  
**Local folder:** `NCATSTranslator/`  
**License:** MIT/Apache 2.0 (varies)

**What it is:** An NIH NCATS program building a comprehensive, knowledge-graph-based platform for translational research. Translator integrates data from hundreds of biomedical sources and uses reasoning algorithms to generate novel insights connecting diseases, genes, drugs, and phenotypes. Uses the Biolink Model and standardized APIs (TRAPI) for interoperability.

**Relevance to Cytognosis:** Translator's architecture (knowledge sources, reasoning agents, standardized APIs) is a reference model for Cytoverse's multi-scale integration. Babel and NodeNormalization provide entity resolution infrastructure critical for harmonizing data across Cytognosis's diverse sources.

| Repository | Description |
| :---- | :---- |
| `Babel` | Entity identifier mapping and normalization service; maps between CURIE namespaces |
| `Knowledge_Graph_Exchange_Registry` | Registry of available knowledge graph sources and their Biolink compatibility |
| `NameResolution` | Service for resolving biomedical entity names to canonical identifiers |
| `NodeNormalization` | Service for normalizing node identifiers to preferred CURIEs across KG sources |
| `ReasonerAPI` | TRAPI (Translator Reasoner API) specification; standard query/response format for reasoning agents |
| `Relay` | Infrastructure for relaying queries between Translator components |
| `TranslatorEngineering` | Engineering documentation, architecture diagrams, and deployment guides |
| `TranslatorTechnicalDocumentation` | Comprehensive technical documentation for all Translator components |
| `Translator_component_toolkit` | Shared utilities and libraries for Translator component development |
| `translator-ingests` | Data ingestion pipelines feeding the Translator knowledge graph |

---

## 8\. Allen Institute for AI (AI2)

**GitHub:** [https://github.com/allenai](https://github.com/allenai)  
**Website:** [https://allenai.org](https://allenai.org)  
**Local folder:** `allenai/`  
**License:** Apache 2.0 (most repos)

**What it is:** A nonprofit AI research institute founded by Paul Allen, focused on AI for the common good. Major contributions include open-source LLMs (OLMo family), scientific NLP tools (ScispaCy, Semantic Scholar), and scientific reasoning benchmarks. Recently released OpenScholar for scientific literature synthesis and SERA for scientific experiment reasoning agents.

**Relevance to Cytognosis:** OLMo provides the open-source foundation model backbone for on-device AI (Cytonome). ScispaCy and OpenScholar support literature mining for Cytoverse. SERA and agent frameworks inform Cytognosis's scientific reasoning pipeline. OLMoCR enables PDF-to-structured-data extraction.

| Repository | Description |
| :---- | :---- |
| `AskOlmo` | Interactive Q\&A interface for OLMo models |
| `ContextEval` | Evaluation framework for context-dependent language understanding |
| `FlexOlmo` | Flexible fine-tuning and adaptation toolkit for OLMo |
| `OLMo` | Open Language Model: fully open-source LLM (weights, data, training code) |
| `OLMo-core` | Core training infrastructure for OLMo models |
| `OLMoASR` | Automatic speech recognition using OLMo architecture |
| `OLMoE` | OLMo Mixture-of-Experts variant for efficient inference |
| `OpenScholar` | AI system for synthesizing scientific literature with citations |
| `SERA` | Scientific Experiment Reasoning Agent for autonomous research |
| `SERA-SWE-agent` | SERA integration with SWE-agent for code-level scientific experimentation |
| `SWE-agent` | Software Engineering agent for autonomous code generation and debugging |
| `ScienceWorld` | Interactive text-based environment for testing scientific reasoning |
| `agent-baselines` | Baseline implementations for AI agent benchmarks |
| `ai2-scholarqa-lib` | Library for question-answering over scientific literature (Semantic Scholar) |
| `ai2thor` | Interactive 3D environment for embodied AI research |
| `atlantes` | Large-scale document understanding and extraction |
| `autodiscovery` | Automated scientific discovery framework |
| `codescientist` | AI agent for writing and executing scientific code |
| `dolma` | Dataset for OLMo: curated, open pretraining corpus (3T tokens) |
| `mcp-tool-eval` | Evaluation framework for MCP tool-use capabilities |
| `molmo-utils` | Utilities for Molmo multimodal models |
| `molmo2` | Second-generation multimodal language model |
| `molmoact` | Action-oriented multimodal model for agent tasks |
| `olmes` | OLMo evaluation suite and benchmarks |
| `olmo-cookbook` | Recipes and guides for training, fine-tuning, and deploying OLMo |
| `olmocr` | OCR and document extraction using OLMo; PDF-to-structured-text at scale |
| `open-instruct` | Open-source instruction tuning framework for LLMs |
| `panda` | Parallel data augmentation and processing |
| `prescience` | Predictive science framework |
| `rslearn` | Remote sensing machine learning tools |
| `scispacy` | SpaCy models trained on biomedical text; NER, entity linking, abbreviation detection |

---

## 9\. AWS Labs

**GitHub:** [https://github.com/awslabs](https://github.com/awslabs)  
**Website:** [https://amazon.com/aws](https://amazon.com/aws)  
**Local folder:** `awslabs/`  
**License:** Apache 2.0

**What it is:** Open-source projects from Amazon Web Services covering cloud infrastructure, developer tools, and data services.

**Relevance to Cytognosis:** The MCP implementation provides reference architecture for cloud-integrated MCP servers. The open-data-registry catalogs publicly available datasets on AWS, including genomic and health datasets relevant to Cytoverse.

| Repository | Description |
| :---- | :---- |
| `mcp` | AWS reference implementation of Model Context Protocol servers and tools |
| `open-data-registry` | Registry of open datasets available on AWS (includes genomics, health, climate, etc.) |

---

## 10\. Biopragmatics

**GitHub:** [https://github.com/biopragmatics](https://github.com/biopragmatics)  
**Website:** [https://biopragmatics.github.io](https://biopragmatics.github.io)  
**Local folder:** `biopragmatics/`  
**License:** MIT (most repos)

**What it is:** A collection of pragmatic tools for biomedical data integration, maintained primarily by Charles Tapley Hoyt. Focuses on identifier standardization, ontology access, entity mapping, and semantic resolution. The Bioregistry is the authoritative meta-registry for biomedical identifier prefixes.

**Relevance to Cytognosis:** Bioregistry and PyOBO provide the identifier resolution backbone for Cytoverse. SeMRA (Semantic Mapping Reasoning and Analysis) enables cross-ontology entity alignment critical for multi-scale data integration. Biomappings and biosynonyms support entity harmonization across psychiatric, genomic, and neuroimaging vocabularies.

| Repository | Description |
| :---- | :---- |
| `biolexica` | Biomedical lexicon generation and NER resource building |
| `biolookup` | Web service for resolving biomedical identifiers to names, definitions, and cross-references |
| `biomappings` | Community-curated, manually verified mappings between biomedical entities across ontologies |
| `bioontologies` | Tools for accessing and processing OBO Foundry and other biomedical ontologies |
| `bioregistry` | Meta-registry of biomedical identifier prefixes; resolves CURIEs, normalizes prefixes, tracks resource metadata |
| `biosynonyms` | Curated synonym database for biomedical entities |
| `bioversions` | Tracks latest versions of biomedical databases and ontologies |
| `pyobo` | Unified Python interface to OBO ontologies and other biological nomenclatures |
| `semra` | Semantic Mapping Reasoning and Analysis; large-scale entity alignment across ontologies |

---

## 11\. GROBID Organization

**GitHub:** [https://github.com/grobidOrg](https://github.com/grobidOrg)  
**Website:** [https://grobid.readthedocs.io](https://grobid.readthedocs.io)  
**Local folder:** `grobidOrg/`  
**License:** Apache 2.0 (software), CC-0 (docs), CC-BY (data)

**What it is:** Machine learning library for extracting, parsing, and restructuring scientific PDFs into structured XML/TEI. \~0.87 F1 for reference extraction (deep learning), \>0.90 F1 for isolated reference parsing. Processes \~10.6 PDFs/second at scale. Used in production by OpenAlex, Semantic Scholar, ResearchGate, Internet Archive Scholar, CERN, and others. Supported by INRIA.

**Relevance to Cytognosis:** Automated ingestion and structuring of scientific literature for systematic reviews, citation graph construction, and metadata extraction across neuroscience, genomics, and psychiatry corpora feeding into Cytoverse.

| Repository | Description |
| :---- | :---- |
| `grobid` | Core GROBID library: PDF to structured XML/TEI extraction |
| `grobid-client-python` | Python client for GROBID REST API |
| `grobid-ner` | Named entity recognition module for GROBID |
| `article_dataset_builder` | Pipeline for creating structured scientific article corpora from PDFs |
| `datastet` | Dataset mention identification and extraction from scientific articles |
| `software-mentions` | Software mention recognition in scientific publications |

---

## 12\. LangChain

**GitHub:** [https://github.com/langchain-ai](https://github.com/langchain-ai)  
**Website:** [https://langchain.com](https://langchain.com)  
**Local folder:** `langchain-ai/`  
**License:** MIT (most repos)

**What it is:** Framework for building applications powered by LLMs. Provides composable abstractions for chains, agents, retrieval, and tool use. LangGraph extends LangChain with stateful, multi-agent orchestration via graph-based workflows. Widely adopted across industry and research.

**Relevance to Cytognosis:** LangChain and LangGraph provide the agent orchestration layer for Cytonome's reasoning pipeline. MCP adapter integration enables connecting Cytognosis's biomedical MCP servers to LangChain agents. Deep research and open-canvas patterns inform the scientific reasoning interface.

| Repository | Description |
| :---- | :---- |
| `langchain` | Core framework: chains, agents, retrieval, tool-use abstractions for LLM applications |
| `langgraph` | Stateful, multi-agent orchestration framework using graph-based workflows |
| `langchain-mcp-adapters` | Adapters for connecting MCP servers to LangChain agents |
| `langchain-nextjs-template` | Next.js template for building LangChain-powered web applications |
| `agent-protocol` | Standardized protocol for AI agent communication |
| `deepagents` | Deep research agent implementations |
| `executive-ai-assistant` | Executive assistant agent with planning, scheduling, and document handling |
| `local-deep-researcher` | Local-first deep research agent using open-source models |
| `open-canvas` | Open-source collaborative AI canvas for document creation |
| `open-swe` | Open-source software engineering agent |
| `open_deep_research` | Open-source deep research agent for comprehensive topic investigation |
| `opengpts` | Open-source GPTs platform with customizable agent configurations |

---

## 13\. OBO Phenotype

**GitHub:** [https://github.com/obophenotype](https://github.com/obophenotype)  
**Website:** (OBO Foundry affiliated)  
**Local folder:** `obophenotype/`  
**License:** CC-BY (ontologies), varies (tools)

**What it is:** Home of phenotype-related ontologies within the OBO Foundry ecosystem. Maintains foundational biomedical ontologies including Uberon (anatomy), Cell Ontology, Human Phenotype Ontology, developmental stage ontologies, and the Unified Phenotype Ontology (uPheno). These ontologies provide the formal vocabulary for describing biological structure, cell types, phenotypes, and developmental stages.

**Relevance to Cytognosis:** These ontologies are the semantic backbone for Cytoverse's phenotype, cell-type, and anatomical annotation layers. HPO is essential for RDoC-aligned psychiatric phenotyping. Cell Ontology and the provisional cell ontology are critical for single-cell data annotation. Uberon provides the anatomical framework for neuroimaging data integration.

| Repository | Description |
| :---- | :---- |
| `uberon` | Uberon multi-species anatomy ontology; integrates anatomical structures across species |
| `cell-ontology` | Cell Ontology (CL): structured vocabulary for cell types |
| `human-phenotype-ontology` | HPO: standardized vocabulary for phenotypic abnormalities in human disease |
| `upheno` | Unified Phenotype Ontology: cross-species phenotype integration |
| `bio-attribute-ontology` | Ontology for biological attributes (measurable traits) |
| `brain_data_standards_ontologies` | Ontologies for standardizing brain cell type data (Allen Brain Atlas aligned) |
| `caro` | Common Anatomy Reference Ontology: upper-level anatomy framework |
| `chebi_obo_slim` | Slim version of ChEBI chemical ontology in OBO format |
| `developmental-stage-ontologies` | Stage-specific developmental ontologies across species |
| `ncbitaxon` | NCBI Taxonomy in OBO format |
| `provisional_cell_ontology` | Provisional extensions to the Cell Ontology for emerging cell types |

---

## 14\. Open Targets

**GitHub:** [https://github.com/opentargets](https://github.com/opentargets)  
**Website:** [https://opentargets.org](https://opentargets.org)  
**Local folder:** `opentargets/`  
**License:** Apache 2.0

**What it is:** A public-private partnership (EMBL-EBI, Wellcome Sanger Institute, GSK, and others) that uses human genetics and genomics data to systematically identify and prioritize drug targets. The Open Targets Platform integrates evidence from genomics, transcriptomics, drugs, animal models, and literature to score target-disease associations. Open Targets Genetics provides variant-to-gene-to-disease evidence.

**Relevance to Cytognosis:** Open Targets provides the drug target evidence layer for Cytoverse, connecting genetic associations to therapeutic opportunities in psychiatric disorders. The platform's ETL architecture and evidence scoring framework inform Cytognosis's approach to multi-evidence integration.

| Repository | Description |
| :---- | :---- |
| `OnToma` | Ontology mapping tool for mapping disease/phenotype terms to EFO (Experimental Factor Ontology) |
| `gentropy` | Genetics-based target prioritization pipeline (successor to genetics-pipe) |
| `json_schema` | JSON Schema definitions for Open Targets data model and evidence objects |
| `open-targets-platform-mcp` | MCP server for querying the Open Targets Platform via LLMs |
| `platform-api` | GraphQL API for the Open Targets Platform |
| `platform-etl-backend` | ETL pipeline backend for processing and integrating Open Targets evidence data |

---

## 15\. OurResearch / OpenAlex

**GitHub:** [https://github.com/ourresearch](https://github.com/ourresearch)  
**Website:** [https://openalex.org](https://openalex.org)  
**Local folder:** `ourresearch/`  
**License:** MIT (code), CC0 (data)  
**Publication:** Priem, J., Piwowar, H., & Orr, R. (2022). OpenAlex: A fully-open index of scholarly works, authors, venues, institutions, and concepts. ArXiv:2205.01833

**What it is:** OurResearch is a 501(c)(3) nonprofit building open scholarly infrastructure, committed to the Principles of Open Scholarly Infrastructure (POSI). Their flagship product, OpenAlex, is a fully open catalog of the global research system: over 250 million scholarly works, authors, institutions, sources, topics, publishers, and funders, all interconnected. OpenAlex succeeded the discontinued Microsoft Academic Graph (2021) and serves 115M+ API calls per month. Data is CC0 (public domain). The system integrates data from Crossref, ORCID, DOAJ, Unpaywall, PubMed, and institutional repositories. Earlier OurResearch products include ImpactStory (altmetrics for research outputs) and CiteAs (citation format discovery for software and datasets).

**Relevance to Cytognosis:** OpenAlex is the primary bibliometric and literature graph for Cytoverse's scientific knowledge layer. It enables systematic mapping of the neuroscience, genomics, and psychiatry publication landscape, author collaboration networks, institutional affiliations, and citation flows. The concept tagging and PDF parsing repos are directly useful for automated literature classification and full-text extraction. SemOpenAlex (see below) provides the RDF/SPARQL interface for semantic queries over this data.

| Repository | Description |
| :---- | :---- |
| `openalex-guts` | Core backend computation engine for OpenAlex; processes raw scholarly data into the OpenAlex data model |
| `openalex-concept-tagging` | ML pipeline for automatically tagging scholarly works with hierarchical research concepts |
| `openalex-pdf-parser` | PDF parsing and full-text extraction for scholarly articles ingested into OpenAlex |
| `total-impact-core` | Core engine for ImpactStory/Total Impact; computes altmetrics (social media, downloads, bookmarks) for research outputs |
| `citeas-api` | CiteAs API: discovers and returns correct citation formats for software, datasets, and other research outputs given a URL or DOI |
| `impactstory-tng` | Next-generation ImpactStory platform for researcher impact profiles and altmetric visualization |

---

## 16\. Metaphacts / SemOpenAlex

**GitHub:** [https://github.com/metaphacts](https://github.com/metaphacts)  
**Website:** [https://semopenalex.org](https://semopenalex.org) (data), [https://metaphacts.com](https://metaphacts.com) (company)  
**Local folder:** `metaphacts/`  
**License:** MIT (SemOpenAlex code), CC0 (SemOpenAlex data)  
**Publication:** Färber et al. (2023). SemOpenAlex: The Scientific Landscape in 26 Billion RDF Triples. ISWC 2023\. doi:10.1007/978-3-031-47243-5\_6

**What it is:** Metaphacts is a knowledge graph platform company that builds metaphactory, a Linked Data publication and management platform based on W3C standards (RDF, SPARQL, OWL, SHACL, SKOS). SemOpenAlex is their collaboration with Karlsruhe Institute of Technology to transform the entire OpenAlex dataset into a 26+ billion triple RDF knowledge graph. SemOpenAlex provides: SPARQL endpoint for semantic queries, resolvable URIs for all entities (linked to Wikidata, Wikipedia, MAKG), knowledge graph embeddings for all entities, and a semantic search interface with entity disambiguation. Updated semi-automatically from OpenAlex snapshots via an AWS pipeline (\~5 days per full update). Requires \~5TB storage for raw data; transformation takes 3-4 days on 16 vCPU / 256GB RAM.

**Relevance to Cytognosis:** SemOpenAlex provides the semantic/Linked Data interface to the scholarly literature graph. Where raw OpenAlex gives JSON API access, SemOpenAlex enables SPARQL-based federated queries, integration with the Linked Open Data cloud, and entity embedding-based similarity search. The schema.org fork provides structured data vocabulary alignment. Together with GROBID and OpenAlex, SemOpenAlex completes the literature intelligence stack for Cytoverse.

| Repository | Description |
| :---- | :---- |
| `semopenalex` | Pipeline for transforming OpenAlex snapshots into 26B+ triple RDF knowledge graph; includes data preprocessing, RDF generation (rdflib), GraphDB ingestion, and SPARQL endpoint deployment |
| `schema.org` | Fork of schema.org vocabulary; provides structured data markup definitions used for SemOpenAlex's ontology alignment with web-standard vocabularies |

---

## Cross-Cutting Themes

### Standards and Data Models

GA4GH (genomic standards) → Biolink Model (Monarch/BioCypher) → LinkML (schema language) → OBO ontologies (obophenotype) form a coherent standards stack that Cytoverse should align with.

### Knowledge Graph Construction

BioCypher (framework) \+ Koza/Monarch (ingestion) \+ KGHub (disease-specific KGs) \+ NCATS Translator (reasoning) \+ Biopragmatics (identifier resolution) provide the full KG pipeline from raw data to queryable knowledge.

### AI/Agent Infrastructure

LangChain/LangGraph (orchestration) \+ BioContextAI (biomedical MCP) \+ AI2/OLMo (open LLMs) \+ BioChatter (biomedical LLM interface) compose the agentic AI layer.

### Literature and Document Processing

GROBID (PDF extraction) \+ AI2/ScispaCy (biomedical NLP) \+ AI2/OpenScholar (literature synthesis) \+ AI2/OLMoCR (OCR) handle scientific literature ingestion. OpenAlex (bibliometric graph) \+ SemOpenAlex (RDF/SPARQL layer) \+ CiteAs (citation discovery) provide the scholarly metadata and knowledge graph infrastructure.

### Ontologies and Vocabularies

OBOphenotype (phenotypes, anatomy, cell types) \+ Biopragmatics/Bioregistry (identifier resolution) \+ LinkML (schema definitions) \+ Biolink Model (KG ontology) provide the semantic foundation.

