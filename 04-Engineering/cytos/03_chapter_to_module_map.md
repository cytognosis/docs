# Playbook Chapter to Cytos Module Map

Companion to `01_cytos_package_design.md`. Maps each chapter of the linkml_kg_playbook to the cytos modules, schemas, and source descriptors that implement it. The chapter prose becomes the notebook narrative; the cytos library does the work.

## How to read this table

* **Notebook**: a notebook under `notebooks/<NN>_<topic>.ipynb` that orchestrates the chapter using cytos.
* **Modules**: cytos subpackages exercised.
* **Schemas**: LinkML files authored or touched.
* **Sources**: `configs/sources/*.yaml` descriptors involved.
* **CLI**: end-to-end command sequence that reproduces the chapter.

## Chapter map

### 00_setup

* Notebook: `notebooks/00_setup.ipynb`
* Modules: `cytos.utils.resource`, `cytos.cli.main` (only `doctor` is invoked)
* Schemas: none
* Sources: none
* CLI: `nox -s setup_venv && cytos sources doctor`

### 01_linkml_in_an_hour

* Notebook: `notebooks/01_linkml_in_an_hour.ipynb`
* Modules: `cytos.schema.codegen`, `cytos.schema.renderers`, `cytos.validate.linkml_validate`
* Schemas: `schemas/core.yaml`, a one-shot `schemas/example.yaml`
* Sources: none
* CLI: `cytos schema generate --all --schema schemas/example.yaml && cytos schema validate schemas/example.yaml`

### 02_schema_landscape

* Notebook: `notebooks/02_schema_landscape.ipynb`
* Modules: `cytos.sources.registry`, `cytos.schema.importers`
* Schemas: none (introspects)
* Sources: every entry in `configs/sources/`
* CLI: `cytos sources list --license-class open`

### 03_jsonld_to_linkml

* Notebook: `notebooks/03_jsonld_to_linkml.ipynb`
* Modules: `cytos.sources.registry` (schema_org, bioschemas), `cytos.schema.bridges.jsonld_to_ttl`, `cytos.schema.automator`, `cytos.ingest.linkmlize.schema_org`
* Schemas: `schemas/auto/schema_org_slice.yaml`, `schemas/domains/publication.yaml` (Bioschemas Sample subset)
* Sources: `schema_org.yaml`, `bioschemas.yaml`
* CLI: `cytos sources fetch schema_org && cytos ingest linkmlize schema_org`

### 04_biolink_and_core_schemas

* Notebook: `notebooks/04_biolink_and_core_schemas.ipynb`
* Modules: `cytos.schema.importers`, `cytos.harmonize.curies`, `cytos.sources.biothings` (for prefix introspection)
* Schemas: `schemas/cytos.yaml` (umbrella imports Biolink)
* Sources: `biolink.yaml`, `bioregistry` (handled by `cytos.harmonize.curies`)
* CLI: `cytos sources fetch biolink && cytos harmonize curies lint`

### 05_umls_snomed

* Notebook: `notebooks/05_umls_snomed.ipynb`
* Modules: `cytos.sources.umls`, `cytos.sources.snomed`, `cytos.ingest.parsers.rrf`, `cytos.schema.bridges.rrf_to_rdf`, `cytos.kg.biocypher.adapters.snomed`
* Schemas: `schemas/mappings/crosswalks/umls.yaml`, `schemas/mappings/crosswalks/snomed.yaml`
* Sources: `umls.yaml` (controlled), `snomed_ct.yaml` (controlled)
* CLI (opt-in): `CYTOS_LICENSE_UMLS=accepted UMLS_API_KEY=... cytos sources fetch umls && cytos ingest linkmlize umls`

### 06_biothings

* Notebook: `notebooks/06_biothings.ipynb`
* Modules: `cytos.sources.biothings`, `cytos.ingest.parsers.jsonschema`, `cytos.ingest.linkmlize.biothings`, `cytos.publish.dde`
* Schemas: `schemas/domains/biothings.yaml`, `schemas/auto/dde_<namespace>.yaml`
* Sources: `biothings_mygene.yaml`, `biothings_myvariant.yaml`, `biothings_mychem.yaml`, `biothings_mydisease.yaml`, `biothings_dde.yaml`
* CLI: `cytos sources fetch biothings_mygene && cytos ingest linkmlize biothings`

### 07_ga4gh

* Notebook: `notebooks/07_ga4gh.ipynb`
* Modules: `cytos.sources.ga4gh`, `cytos.schema.bridges.yamljs_to_jsonjs`, `cytos.schema.bridges.proto_to_jsonjs`, `cytos.ingest.linkmlize.ga4gh`, `cytos.kg.phenopacket_lift`
* Schemas: `schemas/domains/ga4gh.yaml`, `schemas/domains/variant.yaml` (VRS), `schemas/domains/disease.yaml` (Phenopackets), `schemas/auto/ga4gh_beacon.yaml`
* Sources: `ga4gh_vrs.yaml`, `ga4gh_phenopackets.yaml`, `ga4gh_beacon.yaml`
* CLI: `cytos ingest linkmlize ga4gh && cytos kg phenopacket-lift <file>`

### 08_sosa_ssn_to_linkml

* Notebook: `notebooks/08_sosa_ssn_to_linkml.ipynb`
* Modules: `cytos.sources.registry`, `cytos.schema.bridges.jsonld_to_ttl`, `cytos.schema.automator`, `cytos.ingest.linkmlize.sosa`
* Schemas: `schemas/domains/sensor.yaml`
* Sources: `sosa_ssn.yaml`
* CLI: `cytos sources fetch sosa_ssn && cytos ingest linkmlize sosa`

### 09_cellxgene_to_linkml

* Notebook: `notebooks/09_cellxgene_to_linkml.ipynb`
* Modules: `cytos.sources.cellxgene`, `cytos.ingest.linkmlize.cellxgene`, `cytos.validate.cellxgene_validate`
* Schemas: `schemas/domains/expression.yaml`
* Sources: `cellxgene_5_2.yaml`
* CLI: `cytos validate cellxgene path/to/dataset.h5ad`

### 10_hdmf_nwb

* Notebook: `notebooks/10_hdmf_nwb.ipynb`
* Modules: `cytos.sources.nwb`, `cytos.schema.bridges.hdmf_namespace_walker`, `cytos.publish.linkml_arrays`, `cytos.validate.nwbinspector`
* Schemas: `schemas/domains/nwb.yaml`
* Sources: `nwb_core.yaml`
* CLI: `cytos ingest linkmlize nwb && cytos validate nwb path/to/file.nwb`

### 11_open_targets_to_linkml

* Notebook: `notebooks/11_open_targets_to_linkml.ipynb`
* Modules: `cytos.sources.opentargets`, `cytos.schema.bridges.parquet_to_linkml`, `cytos.ingest.linkmlize.opentargets`, `cytos.kg.biocypher.adapters.opentargets`
* Schemas: `schemas/auto/opentargets.yaml`, derived crosswalk in `schemas/mappings/crosswalks/`
* Sources: `opentargets.yaml`
* CLI: `cytos sources fetch opentargets && cytos kg biocypher run configs/mappings/biocypher_opentargets.yaml`

### 12_openalex_bibtex_to_linkml

* Notebook: `notebooks/12_openalex_bibtex_to_linkml.ipynb`
* Modules: `cytos.sources.openalex`, `cytos.ingest.parsers.bibtex`, `cytos.ingest.linkmlize.openalex`, `cytos.ingest.linkmlize.bibtex`
* Schemas: `schemas/domains/publication.yaml`
* Sources: `openalex.yaml`, `bibtex.yaml`
* CLI: `cytos sources fetch openalex && cytos ingest linkmlize openalex`

### 13_organize_and_visualize

* Notebook: `notebooks/13_organize_and_visualize.ipynb`
* Modules: `cytos.schema.renderers`, `cytos.schema.schemasheets`, `cytos.schema.importers`
* Schemas: `schemas/cytos.yaml` (master importer regenerated)
* Sources: none
* CLI: `cytos schema generate erdiagram --schema schemas/cytos.yaml && cytos schema sheets export`

### 14_sssom_snomed_workflow

* Notebook: `notebooks/14_sssom_snomed_workflow.ipynb`
* Modules: `cytos.sources.ols4`, `cytos.harmonize.sssom`, `cytos.kg.storage.neo4j`, `cytos.kg.storage.duckdb`
* Schemas: `schemas/mappings/sssom/snomed_to_mondo.sssom.tsv` (and others, written here)
* Sources: `ols4_mappings.yaml`
* CLI: `cytos sources fetch ols4_mappings && cytos harmonize sssom merge --sources mondo,snomed`

### 15_biocypher

* Notebook: `notebooks/15_biocypher.ipynb`
* Modules: `cytos.kg.biocypher.adapters.*`, `cytos.kg.biocypher.ontology_graft`, `cytos.kg.biocypher.schema_config`, `cytos.kg.biocypher.runner`
* Schemas: `schemas/cytos.yaml` mapped via `configs/mappings/biocypher_schema.yaml`
* Sources: `monarch_kg.yaml`, `opentargets.yaml`, `string.yaml` (for example adapters)
* CLI: `cytos kg biocypher run configs/mappings/biocypher_schema.yaml`

### 16_koza_and_monarch

* Notebook: `notebooks/16_koza_and_monarch.ipynb`
* Modules: `cytos.kg.koza.source_scaffold`, `cytos.kg.koza.biolink_emit`, `cytos.kg.koza.runner`, `cytos.sources.monarch`
* Schemas: `schemas/domains/phenotype.yaml` (Phenopacket-to-Biolink)
* Sources: `monarch_kg.yaml`
* CLI: `cytos kg koza run --source <source-id>`

### 17_biocypher_vs_monarch

* Notebook: `notebooks/17_biocypher_vs_monarch.ipynb`
* Modules: `cytos.kg.decision`, `cytos.kg.merge`
* Schemas: none
* Sources: any pair of sources with different framework decisions
* CLI: `cytos kg merge kg/working/biocypher/<src1> kg/working/koza/<src2>`

### 18_anndata_harmonization

* Notebook: `notebooks/18_anndata_harmonization.ipynb`
* Modules: `cytos.harmonize.tiered_resolver`, `cytos.harmonize.embeddings`, `cytos.harmonize.llm_tiebreaker`, `cytos.harmonize.curator_queue`, `cytos.harmonize.biothings_resolver`, `cytos.validate.cellxgene_validate`
* Schemas: `schemas/domains/expression.yaml`
* Sources: `cellxgene_5_2.yaml`, `ols4_mappings.yaml`, optionally controlled `umls.yaml`
* CLI: `cytos harmonize resolve --column tissue --source <h5ad-table>`

### 19_llm_rag_for_biology

* Notebook: `notebooks/19_llm_rag_for_biology.ipynb`
* Modules: `cytos.rag.cypher_generator`, `cytos.rag.kg_retriever`, `cytos.rag.semsimian_tool`, `cytos.rag.paper_corpus`, `cytos.rag.langgraph_router`, `cytos.rag.grounded_answer`
* Schemas: `schemas/cytos.yaml` (used to seed Cypher generator prompt)
* Sources: a published snapshot under `kg/snapshots/<release>/`
* CLI: `cytos rag ask "What variants are associated with Long QT Syndrome?"`

### 20_structured_extraction

* Notebook: `notebooks/20_structured_extraction.ipynb`
* Modules: `cytos.rag.ontogpt`, `cytos.rag.instructor_extractor`, `cytos.rag.pydantic_ai_agent`, `cytos.rag.scispacy_hybrid`
* Schemas: `schemas/domains/disease.yaml`, `schemas/domains/variant.yaml` used as extraction templates
* Sources: literature corpus (`openalex.yaml`)
* CLI: `cytos rag extract schemas/domains/disease.yaml path/to/abstract.txt`

### 21_appendix

* Notebook: `notebooks/21_appendix.ipynb`
* Modules: `cytos.utils.errors` (registry), `cytos.cli.main`
* Schemas: none
* Sources: none
* CLI: `cytos --help` and `cytos schema --help`

## Coverage matrix

Every playbook chapter has at least one corresponding cytos module, schema, and CLI invocation. Chapters 15, 16, 17 share `cytos.kg.*`. Chapters 19 and 20 share `cytos.rag.*`. Chapters 5 and 14 share license-gated download behavior. Chapters 3, 7, 8, 11, 12 each exercise one `cytos.schema.bridges.*` adapter.
