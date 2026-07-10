# Astera Residency 2026 Submission — Per-proposal overlay

**Status:** Submitted 2026-04-19; outcome pending.
**Funder profile:** [`canonical/funders/astera_residency.yaml`](../../funders/astera_residency.yaml).
**Funding Opp:** Monday item 11813491505.
**Grants Pipeline entry:** Monday item 11813518971.
**Source materials:** [`input/applications/Astera/Astera_submited_application_responses.md`](../../../../../input/applications/Astera/Astera_submited_application_responses.md), [`input/applications/Astera/expanded_version_technology.md`](../../../../../input/applications/Astera/expanded_version_technology.md), [`input/applications/Astera/Astera’s Open Science Policy.md`](../../../../../input/applications/Astera/Astera’s%20Open%20Science%20Policy.md).

This directory holds proposal-specific content overlays for the Astera 2026 cycle. Each file under `slots/` carries the content that was actually submitted, mapped to canonical slot IDs. Generic content lives in the canonical slot files at `canonical/slots/`; this directory captures only the Astera-specific framing and the extracted content authored for this submission.

## Section → slot mapping

| Astera question | Submitted content focus | Slot(s) |
|---|---|---|
| Q1 (300 char thesis) | "Genotype-to-regulation foundation modeling at single-cell resolution; disease-axis discovery from genotype" | U01.1, U01.2 |
| Q2 (technical approach) | Three phases: PFC ATAC/RNA prediction → cell-type dysregulation → disentangled phenotypic axes from genotype | U03.2, U06.2, U07.3 |
| Q3 (team, prior work) | Cytognosis core team, prior Science 2024 + Nature 2019 publications, PsychENCODE/PsychAD lineage | U11.1, U11.2, U11.3, U03.4 |
| Q4 (current state, beneficiaries) | Limits of categorical psychiatric diagnosis; people with neurodegenerative + neuropsychiatric conditions | U02.1, U02.2, U04.2 |
| Q5 (end-users, adoption) | Researchers running variant-effect prediction on neuropsychiatric WGS; clinicians via dimensional biotypes | U04.1, U17.1, U17.3 |
| Q6 (why-not-academia / why FRO) | Cross-disciplinary scope, sustained engineering effort, open infrastructure not viable in single-PI lab | U10.1, U10.2, U10.3 |
| Q7 (in-scope / out-of-scope) | In: Phase 1+2; Out (residency 12 mo): clinical trial, multi-site federated deployment | U09.4, U07.2 |
| Q8 (open science commitments) | Apache 2.0 code; CC BY 4.0 docs; HuggingFace + Zenodo releases; FAIR ontologies (UBERON+CL+GO via TransBox) | U12.1, U12.2, U12.4 |
| Video + resume | Founder background video; CV | A04 |

## Per-slot extracted content

The `slots/` subdirectory contains one file per slot used in this submission. Each file carries the exact prose submitted, plus a frontmatter block identifying the source paragraph(s) and any deviations from the canonical slot template.

This pattern is the template for the remaining 5 prior applications (Brains, Foresight, Google, YC Spring 2026, YC Winter 2025, qb3) per `agent/prompts/execution_spec_v1.md` Phase D.

## Extraction status

| Slot | Status | File |
|---|---|---|
| U01 (thesis + objective) | Drafted | [slots/U01_objective.md](slots/U01_objective.md) |
| U03.2 (technical approach) | Drafted | [slots/U03_novelty_and_approach.md](slots/U03_novelty_and_approach.md) |
| U10 (org-form fit) | Drafted | [slots/U10_org_form_fit.md](slots/U10_org_form_fit.md) |
| Other slots | Pending | — |
