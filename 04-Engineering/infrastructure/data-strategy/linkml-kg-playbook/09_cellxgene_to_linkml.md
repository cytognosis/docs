# 09 — CZI CELLxGENE Schema → LinkML

> **Goal** – encode the CELLxGENE single-cell schema as a LinkML schema,
> so we can validate AnnData `obs` declaratively while still running
> `cellxgene-schema validate` for structural checks (the hybrid pattern).
> **Time** – 60 minutes.
> **Prereqs** – chapters 01, 02, 04 (Biolink);
> `sssom_tooling_for_cytognosis.md` §10.

---

## What CZI publishes

The CZI single-cell-curation repo ships the schema as **markdown +
Python validators**, not LinkML. There's no machine-readable source
file `schemauto` can import, so you hand-author a LinkML mirror derived
from the markdown.

```bash
git clone --depth 1 https://github.com/chanzuckerberg/single-cell-curation \
  downloads/cellxgene/single-cell-curation
ls downloads/cellxgene/single-cell-curation/schema/
# 5.0.0/  5.1.0/  5.2.0/  ...
```

The reference doc to mirror: `schema/<latest>/schema.md`. Pin your
LinkML schema to the matching version (`cytognosis_cellxgene_5_2_0.yaml`).

---

## CELLxGENE in one diagram

```mermaid
flowchart LR
    AnnData[.h5ad file] --> Struct{Structural rules}
    Struct --> X[X is sparse CSR/CSC]
    Struct --> Var[var indexed by ENSG IDs]
    Struct --> Obsm[obsm has X_umap or equivalent]
    AnnData --> Obs{obs columns}
    Obs --> CL[cell_type_ontology_term_id ~ ^CL:[0-9]+$]
    Obs --> MD[disease_ontology_term_id ~ ^MONDO:[0-9]+$]
    Obs --> NC[organism_ontology_term_id ~ ^NCBITaxon:[0-9]+$]
    Obs --> UB[tissue_ontology_term_id ~ ^UBERON:[0-9]+$]
    Obs --> EFO[assay_ontology_term_id ~ ^EFO:[0-9]+$]
    Obs --> Sex[sex_ontology_term_id ~ ^PATO:[0-9]+$]
    Obs --> SR[self_reported_ethnicity_ontology_term_id]
    Obs --> Dev[development_stage_ontology_term_id]
    Obs --> Susp[suspension_type enum]
    Obs --> IsP[is_primary_data bool]
```

---

## 1. Skeleton LinkML schema

```yaml
# schemas/cellxgene/cellxgene_5_2_0.yaml
id: https://cytognosis.org/schemas/cellxgene_5_2_0
name: cellxgene_5_2_0
description: |
  LinkML mirror of CZI CELLxGENE single-cell schema v5.2.0 (obs columns).
  Structural AnnData checks remain delegated to `cellxgene-schema`.
prefixes:
  cxg:        https://cellxgene.cziscience.com/schema/5.2.0/
  CL:         http://purl.obolibrary.org/obo/CL_
  MONDO:      http://purl.obolibrary.org/obo/MONDO_
  HsapDv:     http://purl.obolibrary.org/obo/HsapDv_
  MmusDv:     http://purl.obolibrary.org/obo/MmusDv_
  UBERON:     http://purl.obolibrary.org/obo/UBERON_
  NCBITaxon:  http://purl.obolibrary.org/obo/NCBITaxon_
  EFO:        http://www.ebi.ac.uk/efo/EFO_
  PATO:       http://purl.obolibrary.org/obo/PATO_
  HANCESTRO:  http://purl.obolibrary.org/obo/HANCESTRO_
  linkml:     https://w3id.org/linkml/
default_prefix: cxg
default_range: string
imports:
  - linkml:types

classes:
  CellMetadataRow:
    description: One row of `adata.obs` under CELLxGENE schema 5.2.
    slots:
      - cell_type_ontology_term_id
      - assay_ontology_term_id
      - disease_ontology_term_id
      - organism_ontology_term_id
      - sex_ontology_term_id
      - tissue_ontology_term_id
      - self_reported_ethnicity_ontology_term_id
      - development_stage_ontology_term_id
      - suspension_type
      - is_primary_data
      - donor_id

slots:
  cell_type_ontology_term_id:
    range: uriorcurie
    pattern: "^CL:[0-9]{7}$"
    required: true
  assay_ontology_term_id:
    range: uriorcurie
    pattern: "^EFO:[0-9]{7}$"
    required: true
  disease_ontology_term_id:
    range: uriorcurie
    pattern: "^(MONDO:[0-9]{7}|PATO:0000461)$"   # PATO:0000461 = "normal"
    required: true
  organism_ontology_term_id:
    range: uriorcurie
    pattern: "^NCBITaxon:[0-9]+$"
    required: true
  sex_ontology_term_id:
    range: uriorcurie
    pattern: "^(PATO:0000383|PATO:0000384|unknown)$"
    required: true
  tissue_ontology_term_id:
    range: uriorcurie
    pattern: "^UBERON:[0-9]{7}( \\(cell culture\\)| \\(organoid\\))?$"
    required: true
  self_reported_ethnicity_ontology_term_id:
    range: string
    pattern: "^(HANCESTRO:[0-9]+|na|unknown|multiethnic)$"
    required: true
  development_stage_ontology_term_id:
    range: uriorcurie
    pattern: "^(HsapDv:[0-9]{7}|MmusDv:[0-9]{7}|unknown)$"
    required: true
  suspension_type:
    range: SuspensionTypeEnum
    required: true
  is_primary_data:
    range: boolean
    required: true
  donor_id:
    range: string
    required: true

enums:
  SuspensionTypeEnum:
    permissible_values:
      cell:
      nucleus:
      na:
```

> Pin the version exactly. CZI changes pattern requirements between
> minor releases (e.g., introducing `(cell culture)` suffixes).

---

## 2. Validate `adata.obs` against the LinkML schema

```python
# scripts/validate_obs.py
import sys, anndata as ad
from linkml.validator import Validator

adata = ad.read_h5ad(sys.argv[1])
v = Validator("schemas/cellxgene/cellxgene_5_2_0.yaml",
              target_class="CellMetadataRow")

errors = []
for i, rec in enumerate(adata.obs.to_dict(orient="records")):
    rec = {k: (None if v_ != v_ else v_)            # NaN -> None
           for k, v_ in rec.items()}
    rep = v.validate(rec)
    for r in rep.results:
        errors.append((i, r.message))

print(f"{len(errors)} obs errors across {len(adata.obs)} rows")
for i, msg in errors[:20]:
    print(f"  row {i}: {msg}")
```

Run:

```bash
python scripts/validate_obs.py dataset.h5ad
```

> **Checkpoint** – zero errors. If non-zero, the messages tell you which
> column violates which pattern; fix in chapter 18.

---

## 3. Combine with structural validation

```bash
# Structural (sparsity, var, obsm) – CZI's tool
cellxgene-schema validate dataset.h5ad

# Semantic (obs values) – your LinkML
python scripts/validate_obs.py dataset.h5ad
```

Both must pass before publishing or ingesting.

---

## 4. Codegen for downstream services

```bash
gen-pydantic schemas/cellxgene/cellxgene_5_2_0.yaml \
  > build/cellxgene_pydantic.py

gen-json-schema schemas/cellxgene/cellxgene_5_2_0.yaml \
  > build/cellxgene.schema.json
```

Use the Pydantic class in your data-curation API; use the JSON Schema in
your front-end form generator.

---

## 5. Cytognosis extensions

Add internal-only fields without forking CZI:

```yaml
# schemas/cytognosis/cell.yaml
imports:
  - linkml:types
  - ../cellxgene/cellxgene_5_2_0
classes:
  CytoCellMetadataRow:
    is_a: CellMetadataRow
    slots:
      - treatment_group
      - cohort_id
      - patient_pseudonym
      - clinical_trial_arm
slots:
  treatment_group:
    range: TreatmentGroupEnum
  cohort_id:
    range: string
    pattern: "^cyto:Cohort/[A-Z0-9-]+$"
  patient_pseudonym:
    range: string
  clinical_trial_arm:
    range: string
enums:
  TreatmentGroupEnum:
    permissible_values:
      control:
      treated:
      placebo:
      crossover:
```

Now `CytoCellMetadataRow` is CELLxGENE-compliant *plus* internally
extended.

---

## 6. Hands-on

1. Clone single-cell-curation, find the latest `schema.md`.
2. Pull the ontology pattern table from it; verify against the YAML
   above.
3. Run both `cellxgene-schema validate` and your LinkML validator on a
   sample `.h5ad`.
4. Add one Cytognosis-specific slot and re-validate.

---

## 7. Pitfalls

- **CL/MONDO/UBERON IDs always have 7 digits**, but EFO and other OBO
  IDs vary. Get the pattern from the markdown spec, not from intuition.
- **`disease_ontology_term_id`** allows the bare PATO term `PATO:0000461`
  ("normal"); your pattern must include it.
- **`tissue_ontology_term_id`** can carry `" (cell culture)"` /
  `" (organoid)"` suffixes — that's why the pattern has the `( ...)?`
  group.
- **`cellxgene-schema` enforces **exact** ontology versions** (e.g.,
  CL 2024-01-04). Your LinkML pattern only validates *syntax*; for
  ontology-version validation, keep using `cellxgene-schema`.
- **The schema bumps majors fairly often.** Re-derive `*_5_x_y.yaml`
  per release; keep old versions for backward-compat ingest.

---

## Further reading

- CELLxGENE schema docs:
  https://github.com/chanzuckerberg/single-cell-curation/blob/main/schema/5.2.0/schema.md
- cellxgene-schema CLI: `pip install cellxgene-schema`
- AnnData docs: https://anndata.readthedocs.io/
