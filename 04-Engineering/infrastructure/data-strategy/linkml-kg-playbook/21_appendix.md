# 21 — Appendix: cheat sheets, common errors, and links

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: engineers
> **Tags**: `engineering`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

> **Goal** – fast lookup when you forget a flag.
> **Prereqs** – none.

---

## A. LinkML CLI cheat sheet

| Command | What it does |
| --- | --- |
| `linkml-validate -s SCHEMA -C CLASS data.yaml` | Validate data |
| `gen-pydantic SCHEMA > out.py` | Pydantic v2 models |
| `gen-json-schema SCHEMA > out.schema.json` | JSON Schema |
| `gen-owl SCHEMA > out.owl.ttl` | OWL Turtle |
| `gen-shacl SCHEMA > out.shacl.ttl` | SHACL shapes |
| `gen-sqlddl SCHEMA > out.sql` | SQL DDL |
| `gen-graphql SCHEMA > out.graphql` | GraphQL types |
| `gen-doc SCHEMA --directory docs/` | Markdown docs |
| `gen-erdiagram SCHEMA > out.mmd` | Mermaid ER diagram |
| `gen-mermaid-class-diagram SCHEMA > out.mmd` | Mermaid class diagram |
| `gen-yuml SCHEMA > out.yuml` | yUML |
| `schemauto import-rdfs FILE.ttl --output OUT.yaml` | Import from RDFS/OWL Turtle (use rdflib first if source is JSON-LD) |
| `schemauto import-owl FILE.owl --output OUT.yaml` | Import from OWL (strict) |
| `schemauto import-jsonschema FILE.json --output OUT.yaml` | Import from JSON Schema |
| `schemauto generalize-tsv FILE.tsv --output OUT.yaml` | Infer schema from a TSV |
| `schemauto generalize-json FILE.json --output OUT.yaml` | Infer schema from JSON instances |
| `linkml2sheets SCHEMA -o out.xlsx` | Project to spreadsheet |
| `sheets2linkml in.xlsx -o SCHEMA` | Project from spreadsheet |
| `linkml-convert -t json -s SCHEMA in.yaml -o out.json` | Convert data |

## B. SSSOM CLI cheat sheet

| Command | What it does |
| --- | --- |
| `sssom validate FILE.tsv` | LinkML-backed validation |
| `sssom convert -O {tsv,json,owl,rdf,fhir-r4} FILE.tsv -o OUT` | Format conversion |
| `sssom merge A.tsv B.tsv -o C.tsv` | Union mapping sets |
| `sssom diff A.tsv B.tsv` | Diff two sets |
| `sssom filter --predicate-id "skos:exactMatch" FILE.tsv -o OUT` | Filter rows |
| `sssom split FILE.tsv --split-by subject_source` | Split by column |
| `sssom dedupe FILE.tsv -o OUT.tsv` | De-duplicate |

## C. OAK (`runoak`) cheat sheet

| Command | What it does |
| --- | --- |
| `runoak -i sqlite:obo:cl labels CL:0000084` | Look up label |
| `runoak -i sqlite:obo:cl ancestors CL:0000084` | List ancestors |
| `runoak -i sqlite:obo:cl descendants CL:0000084` | List descendants |
| `runoak -i sqlite:obo:cl mappings CL:0000084` | Embedded mappings |
| `runoak -i sqlite:obo:cl lexmatch -o cl-mondo.sssom.tsv` | Bootstrap mapping set |
| `runoak -i sqlite:obo:cl diff -X obo:cl@2024-01-01 -X obo:cl@2024-06-01` | Version diff |
| `runoak -i sqlite:obo:cl viz CL:0000084` | Open ontology viewer |
| `runoak -i sqlite:obo:cl validate-mappings X.sssom.tsv` | Cross-check |

## D. BioCypher cheat sheet

| Step | Code |
| --- | --- |
| Init | `bc = BioCypher(schema_config_path=..., biocypher_config_path=...)` |
| Add nodes | `bc.write_nodes(adapter.get_nodes())` |
| Add edges | `bc.write_edges(adapter.get_edges())` |
| Materialize | `bc.write_import_call()` then run the printed shell command |
| Inspect counts | `bc.summary()` |
| Switch output | edit `dbms.dbms` in `biocypher_config.yaml` (`neo4j` / `rdf` / `arangodb` / `csv`) |

## E. Koza cheat sheet

| Step | Command |
| --- | --- |
| Run a single source | `koza transform --source path/transform_source.yaml --output-dir out/` |
| List configs | `koza list-sources --config monarch.yaml` |
| Validate output | `kgx validate -i out/foo_nodes.tsv -i out/foo_edges.tsv` |
| Merge | `kgx merge --merge-config merge.yaml -o merged.tar.gz` |

---

## F. Common errors and their fixes

| Error | Likely cause | Fix |
| --- | --- | --- |
| `linkml-validate: ImportError ...` | Wrong python env | `which python; which linkml-validate` |
| `KeyError: 'curie_map'` from `parse_sssom_table` | Old sssom-py | `pip install -U sssom>=0.4` |
| `oaklib` says "ontology not found" | First-run cache failed | `rm -rf ~/.data/oakx-sqlite-*; runoak -i sqlite:obo:cl labels CL:0000000` |
| BioCypher `unknown ontology element X` | `schema_config.yaml` has class not in Biolink/your schema | Add to `master.yaml` or rename |
| Koza `Source name does not exist` | wrong `--source` path | absolute path to the `transform_source.yaml` |
| `cellxgene-schema validate` says obsolete CL term | upstream schema bumped CL pin | `pip install -U cellxgene-schema` |
| `gen-pydantic` outputs v1 syntax | old linkml | `pip install -U linkml>=1.7` |
| `gen-erdiagram` produces empty diagram | no slots have ranges to other classes | add `range:` to relevant slots |
| `gen-linkml: 'jsonld' is not one of 'json', 'yaml'` | `gen-linkml` is **not** a multi-format importer — it only reloads existing LinkML YAML/JSON | Use `schemauto` from the `schema-automator` package: rdflib-convert JSON-LD → TTL, then `schemauto import-rdfs FILE.ttl --output OUT.yaml` |
| `schemauto import-jsonschema` produces many anonymous classes | nested objects in source | re-run with `--use-attributes`, or post-process to lift them into named classes |

---

## G. URL bookmark pack

### Specs
- LinkML: https://linkml.io
- LinkML metamodel: https://linkml.io/linkml-model/
- Biolink Model: https://biolink.github.io/biolink-model/
- SSSOM: https://mapping-commons.github.io/sssom/
- Phenopackets: https://phenopacket-schema.readthedocs.io/
- SOSA/SSN: https://www.w3.org/TR/vocab-ssn/
- schema.org: https://schema.org
- Bioschemas: https://bioschemas.org/profiles/
- CELLxGENE: https://github.com/chanzuckerberg/single-cell-curation
- Open Targets: https://platform-docs.opentargets.org

### Tools
- OAK: https://incatools.github.io/ontology-access-kit/
- BioCypher: https://biocypher.org
- Koza: https://koza.monarchinitiative.org/
- monarch-ingest: https://github.com/monarch-initiative/monarch-ingest
- phenopacket-ingest: https://github.com/monarch-initiative/phenopacket-ingest
- KGX: https://github.com/biolink/kgx
- bmt: https://github.com/biolink/biolink-model-toolkit
- schema-automator: https://github.com/linkml/schema-automator

### BioThings ecosystem
- BioThings overview: https://biothings.io/
- BioThings APIs (My*): https://docs.mygene.info/, https://docs.myvariant.info/, https://docs.mychem.info/, https://docs.mydisease.info/
- biothings_client (Python): https://github.com/biothings/biothings_client.py
- biothings_schema.py: https://github.com/biothings/biothings_schema.py
- Data Discovery Engine: https://discovery.biothings.io/
- DDE registry API: https://discovery.biothings.io/api/registry
- BioThings GitHub (where occasional snapshots live as Releases): https://github.com/biothings
- Issue tracker for ad-hoc snapshot / quota requests: https://github.com/biothings/biothings.api/issues

### Bulk-dump BioThings to Parquet — quick recipe
```bash
# 1) JSONL via fetch_all (resumable script in chapter 06 §1.3)
python scripts/biothings_dump.py --api gene --query "taxid:9606" \
    --out downloads/biothings/mygene_human.jsonl.gz

# 2) JSONL -> Parquet via DuckDB
duckdb -c "
COPY (SELECT * FROM read_json_auto(
        'downloads/biothings/mygene_human.jsonl.gz',
        union_by_name=true, ignore_errors=true))
TO 'downloads/biothings/mygene_human.parquet'
(FORMAT PARQUET, COMPRESSION 'zstd');
"
```
*Don't* do this for MyVariant — go upstream to dbSNP/ClinVar/gnomAD instead.

### GA4GH
- Home: https://www.ga4gh.org/
- Products index: https://www.ga4gh.org/our-products/
- VRS: https://vrs.ga4gh.org/ — repo https://github.com/ga4gh/vrs
- vrs-python: https://github.com/ga4gh/vrs-python
- VA: https://va-ga4gh.readthedocs.io/ — repo https://github.com/ga4gh/va-spec
- Phenopackets (Protobuf): https://phenopacket-schema.readthedocs.io/
- Phenopackets (LinkML port): https://cmungall.github.io/linkml-phenopackets/ — repo https://github.com/cmungall/linkml-phenopackets
- Pedigree: https://github.com/ga4gh/pedigree-standard
- Beacon v2: https://docs.genomebeacons.org/ — repo https://github.com/ga4gh-beacon/beacon-v2

### HDMF / NWB
- HDMF docs: https://hdmf.readthedocs.io/
- HDMF Schema Language: https://hdmf-schema-language.readthedocs.io/
- hdmf-common-schema: https://hdmf-common-schema.readthedocs.io/
- HDMF (repo): https://github.com/hdmf-dev/hdmf
- HDMF-Zarr: https://github.com/hdmf-dev/hdmf-zarr
- HERD (term sets): https://hdmf.readthedocs.io/en/stable/term_set.html
- NWB schema: https://nwb-schema.readthedocs.io/
- PyNWB: https://pynwb.readthedocs.io/
- NWB Inspector: https://github.com/NeurodataWithoutBorders/nwbinspector
- NWB extension template: https://github.com/nwb-extensions/ndx-template
- DANDI archive: https://dandiarchive.org/
- linkml-arrays: https://github.com/linkml/linkml-arrays

### Mapping sources
- Mapping Commons: https://github.com/mapping-commons
- Biomappings: https://github.com/biopragmatics/biomappings
- OLS4 SSSOM: https://ftp.ebi.ac.uk/pub/databases/spot/ols/latest/

### Identifier hygiene
- Bioregistry: https://bioregistry.io
- curies (Python): https://github.com/biopragmatics/curies
- prefixmaps: https://github.com/linkml/prefixmaps

---

## H. Suggested next steps for Cytognosis

1. Restructure `cytognosis_scholarly_kg_v0.4.0.yaml` into the hybrid
   layout (chapter 14).
2. Add SSSOM and Biolink imports; codegen Pydantic.
3. Stand up a Koza ingest for OpenAlex on the bibliographic side and a
   BioCypher adapter for Open Targets on the biomedical side; merge via
   KGX.
4. Wire OAK + SSSOM into a `harmonize_obs.py` and run it on one real
   dataset.
5. Add a CI step that runs `linkml-validate`, `sssom validate`, and
   `cellxgene-schema validate` on every change.
