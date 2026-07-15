# A Map-First FRO for Psychiatric Disease Biology: Open, Bounded, and Shaped for Convergent

**Outreach to:** Adam Marblestone, PhD, and the Convergent Research team; Focused Research Organization portfolio.
**From:** Shahin Mohammadi, PhD, Founder & CEO, Cytognosis Foundation (501(c)(3)); TA1/TA2 sub-lead, PsychIGoR consortium (IPAI/Purdue prime, PI Ananth Grama).
**Contact:** mohammadi@cytognosis.org
**Date:** 2026-07-14

## Why we are writing

Cytognosis Foundation was set up as a nonprofit precisely because the artifact we most want to build for psychiatry is **infrastructure, not a product**. It has diffuse downstream value across academia, industry, ARPA-H (EVIDENT, IGoR), the VA, the FDA expedited-approval pipeline, and every mental health delivery organization that will use the map to match a person to a treatment. No single company can capture enough of that value to justify building it, and any company that did build it would then own it, which is exactly the failure mode the FRO concept was designed to avoid.

The IGoR consortium we lead (a $42.9M ARPA-H proposal due 2026-08-13) is a large integrated program that includes disease-model discovery, AI-driven experiment design, protocol interoperability, and a multi-lab validation marketplace. Inside that program is a smaller, **cleanly separable, FRO-shaped artifact**: the **universal dimensional map of psychiatric disease biology**. We would like to explore whether that artifact is a fit for Convergent Research to stand up separately from IGoR, as an open, time-bounded, dissolution-oriented FRO.

## The artifact, in one paragraph

The map is a **continuous, dimensional, transdiagnostic coordinate system** for psychiatric disease, mechanistically grounded in molecular biotypes (BDNF-plasticity, PV-gamma / E-I imbalance, oxidative-stress / mitochondrial, hyperdopaminergic, inflammatory, serotonergic), cellular biotypes (from PsychENCODE brainSCOPE, PsychAD, and the Ruzicka-Mohammadi *Science* 2024 schizophrenia atlas), circuit biotypes (Drysdale, B-SNIP, Williams six-biotype, Beam-Etkin, Quah RDoC-imaging), and the Grotzinger 2025 five-factor cross-disorder genomic scaffold. It is anchored in penetrant, near-Mendelian genetic forms (22q11.2 deletion, high-OR SCHEMA genes) in the same tradition that made neurodegeneration cellular biology tractable (APP/PSEN1, LRRK2/SNCA), and it generalizes to idiopathic and transdiagnostic psychiatry through learned axes. It is designed to be released openly under permissive licenses and FAIR-data terms so the field can build on it.

## The FRO shape test, applied

| Convergent criterion | Fit for the map |
|---|---|
| **Concrete artifact, not open-ended exploration** | The artifact is a shipping, versioned, dimensional coordinate system with defined interfaces (data schemas, ontology bindings, model APIs), released under Apache 2.0 for code, CC BY for docs, and controlled-access DUAs where cohorts require. "Done" is defined at v1.0 release. |
| **Infrastructure with diffuse downstream value** | Downstream users: academic PIs, biotech target-discovery groups, ARPA-H programs adjacent to IGoR (EVIDENT for endpoint definition; Proactive Health for personalization), FDA expedited-approval sponsors needing objective endpoints, VA precision-psychiatry pilots. The map's value is not captured by any single downstream. |
| **Neither an academic grant nor a company** | The engineering is a coordinated multi-team build (data ingestion, ontology, causal inference, cell-type atlases, dimensional-axis fitting, longitudinal update loop). It does not decompose cleanly into PI-scale grants, and no company would build it and then release it openly. |
| **Time-bounded, dissolution-oriented** | We propose a 3-to-5-year build with a defined dissolution or hand-off: at v1.0, custodianship of the map transfers to a permanent open-science steward (a candidate structure: shared custody among a small consortium of academic centers plus an open-science governance body, similar to the ENCODE and PsychENCODE precedents). |
| **Deliverable rather than platform-in-perpetuity** | The FRO ships the map. Downstream organizations, including Cytognosis itself for its wearable programs (Cytoscope) and its on-device causal AI (Cytonome), then figure out how to use it. This is exactly the relationship you have described between the molecular-monitoring FRO and its downstream users. |

## The split, and why disease biology is not IP-protected

The IGoR program spans four Technical Areas (mechanistic disease models, AI-driven experiment design, protocol interoperability, validated-lab marketplace). Not all four are FRO-shaped. Two components fit cleanly, and we propose surfacing them separately:

- **Map only (FRO-shaped, open-source, Phase 1 anchor).** The dimensional coordinate system itself, the cell-type atlases and reference axes it composes, the penetrant-form iPSC phenotype library, the ontology bindings, and the causal-inference framework that treats disease-associated genetic variation as a soft intervention. This is disease biology; US law is clear that human disease biology, unmodified, is not patentable, and Cytognosis has no interest in trying. Open-source Phase 1 is deliberately chosen.
- **Kept confidential (not part of the FRO scope).** A specific factorization method that decomposes patient polygenic variation into sparse pathway-disentangled axes, and a related perturbation-modeling method under anonymous review, are held as IP with commercial application downstream. These are methods for using the map, not the map itself, and they can be developed and licensed separately without affecting the openness of the map.

The design principle: **the substrate is a public good; specific methods for exploiting the substrate can be treated as IP where the downstream economics justify it**. This mirrors how genome-reference infrastructure (GRCh38, the ENCODE regulatory catalog) is open, while specific variant-calling or clinical-interpretation methods over that infrastructure are proprietary.

## Anchors that make the timeline real

The scientific substrate is not hypothetical. Direct precedents from our own record and our consortium's:

- **Ruzicka, Mohammadi et al. 2024 (*Science*).** Multi-cohort single-cell dissection of the schizophrenia transcriptome across 388 human brains, published as the reference cellular atlas for schizophrenia.
- **Mathys, Mohammadi et al. 2019 (*Nature*).** ROSMAP single-cell Alzheimer atlas, demonstrating we can build cell-type atlases at scale.
- **Tegtmeyer et al. 2025 (*Nat Commun*).** NeuroPainting cell-type morphology of 22q11.2 in iPSC-derived neurons and astrocytes, senior-authored by Anne Carpenter; the direct 22q11-in-a-dish precedent that Phase 1 extends to a multi-variant panel.
- **Grotzinger et al. 2025 (*Science*).** Cross-disorder five-factor genomic scaffold across 14 psychiatric disorders, the reference axis system.
- **Surreal-GAN, DNE, MULTI Consortium.** Continuous dimensional axes at population scale in aging and neurodegeneration (Nat Med 2024, Nat Biomed Eng 2025, Nat Med 2026); direct precedent for continuous, genetically-validated, healthy-anchored dimensional axes.

The consortium we already lead spans the required expertise (IPAI/Purdue prime with Ananth Grama; Cytognosis for TA1 and TA2; Matt Tegtmeyer at Purdue for wet-lab experiments; Anne Carpenter at IPAI/Purdue for computational morphology; Brad Ruzicka at McLean/HMS for clinical translation; SIFT for protocol interoperability; Cellanome for live-cell perturbation; Illumina for perturbation-scale sequencing). We are prepared to spin out a smaller, dedicated map-only build team if the FRO fit is real.

## What we are asking for

A 30-minute exploratory conversation on whether the map-only artifact is FRO-shaped by Convergent's criteria, and if so, whether it fits the operational model that Convergent stands up FROs through. A parallel path (IGoR funds the larger integrated program; an FRO stands up the map-only artifact as open public infrastructure, with tight coordination) is one hypothesis we would like to test with you. An alternative path (the FRO stands alone, without IGoR dependency) is another. We are open to either, and to your read on which is cleaner.

**Shahin Mohammadi, PhD.** Founder & CEO, Cytognosis Foundation (501(c)(3), EIN 39-4383634, South San Francisco). Twenty years in computational biology (MIT, Broad Institute, insitro, GenBio AI); first author on the Ruzicka-Mohammadi *Science* 2024 schizophrenia atlas. Cytognosis was built to make precision health a human right, not a privilege; a public map of the human psyche, released openly, is the most direct instantiation of that mission we can put in the field.
