# Recovered material: 2.3 (technical version, pre-restructure) — raw material to rewrite 3.1

This is the **2.3 "describe your project in depth" section as it stood before** we split Part 2 (impact) from Part 3 (technical) and before the generative-unified/open-free edits. It still carries the full technical method, which is what you want for rebuilding 3.1. Your live app's 2.3 is the impact-only version; this file is just material and is not part of the submission.

---

## Full prior 2.3 (NBB technical version)

Cytognosis is building a cellular intelligence platform, a GPS for Health, with three parts: the Cytoverse, a multimodal map whose continuous biological axes (a longitude and latitude for health) replace imprecise disease labels; the Cytoscope, a sensor that locates each person on that map; and the Cytonome, a navigator that turns coordinates into mechanistic guidance. This project builds the Cytoverse map for neuropsychiatric conditions, the Psychoverse.

Today a person is labeled with "schizophrenia," "autism," or "depression" and treated by that label, yet patients who share a diagnosis often differ biologically and respond very differently, one reason being that roughly half do not improve on their first treatment.

When patients within a diagnosis are instead sorted into biologically defined subgroups (biotypes) and treated as individuals, outcomes improve sharply: individualized brain-stimulation targeting, behind Stanford's FDA-cleared SAINT therapy, drove remission in most treatment-resistant cases, and a 2026 study that personalized each patient's intervention from their own data produced large, on-target symptom reductions. The individual, not the diagnostic average, is the right unit of analysis.

These drivers also cross diagnostic lines: a recent study of 14 psychiatric conditions and over one million people found about two-thirds of inherited risk collapses into five shared factors.

This grant builds the first public release of such a transdiagnostic map. Powerful genomic foundation models capture the evolutionary constraints encoded in the DNA (the "genomic grammar"), but are not trained to capture disease-relevant signals; our core contribution is to fine-tune these models using clinically enriched data from our collaboration with the NIH NeuroBioBank (NBB). We pair pretrained genomic foundation models (e.g., Evo 2) with our in-house phenotype encoder, a sparse autoencoder that compresses clinical symptoms into interpretable factors, and fine-tune them jointly with a contrastive loss that aligns these embedding spaces. We release both the fine-tuned adapters and a full model that projects any patient onto shared genomic-phenotypic axes, which is trained on clinically relevant populations and is open to researchers, clinicians, and patient-advocacy groups. Because the axes are learned jointly, nearby patients share both genomic and clinical structure, yielding biotypes that are biologically grounded and clinically actionable.

---

## Menu of method phrasings we've used (pick/remix for 3.1)

**Foundation-model + fine-tuning framing (NBB):**
> Powerful genomic foundation models capture the evolutionary constraints encoded in DNA (the "genomic grammar") but are not trained on disease; our core contribution is to fine-tune them on clinically enriched NIH NeuroBioBank data.

**Encoders + objective:**
> We pair a pretrained genomic foundation model (e.g., Evo 2) with an in-house sparse-autoencoder phenotype encoder that compresses clinical symptoms into interpretable factors, and fine-tune them jointly with a contrastive loss that aligns the two embedding spaces.

**Alignment analogy (optional, for an ML-literate reader):**
> conceptually like CCA or PLS, but aligning nonlinear embeddings rather than linear projections.

**Generative-unified framing (handles missing data + modular for connectomics):**
> We fuse the genome- and phenotype-derived factors into one shared representation using a generative model with a contrastive alignment term; being generative, it works when a patient is missing a data type and lets us add brain-connectivity (connectomic) data later as another input without rebuilding.

**Deliverables / openness:**
> We release the fine-tuned adapters and a full model that projects any patient onto shared genomic-phenotypic axes; we serve the model openly for inference and publish code and documentation, releasing model weights where data-use agreements permit.

**AWS stack (for the "applicability of AWS services" criterion):**
> AWS HealthOmics (genomic data store); Amazon SageMaker (training + a real-time inference endpoint behind Amazon API Gateway); Amazon S3 + FSx for Lustre (large files/checkpoints); AWS KMS, CloudTrail, Config, Audit Manager (HIPAA-eligible compliance trail); Amazon EC2 P5 GPU instances for fine-tuning.

**Payoff line:**
> Because the axes are learned jointly, nearby patients share both genomic and clinical structure, yielding biotypes that are biologically grounded and clinically actionable.
