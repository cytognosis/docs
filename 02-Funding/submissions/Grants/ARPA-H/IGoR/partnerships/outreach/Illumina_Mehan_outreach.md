# Illumina / Michael Mehan outreach (TA4.2 sequencing and bioinformatics)

**Status:** Ready to send. Warm referral from Sebastian Pineda.
**To:** Michael Mehan (Director of Bioinformatics, Illumina)
**Attach:** `onepagers/TA4_Illumina_Mehan.pdf` (and optionally `onepagers/00_IGoR_Program_Overview.pdf`).
**Who he is:** PhD in computational biology (USC, Zhou lab, gene-phenotype prediction); ~9 years at Illumina, risen from bench bioinformatics scientist to Director (Dec 2025); earlier clinical genomics and proteomics (Boston Heart Diagnostics, SomaLogic). A hands-on scientist, not a sales contact, so the note engages him on the technical architecture and the data layer, which is his domain.
**Tone:** professional, understated, scientist-to-scientist; no salesy or self-congratulatory phrasing; let the substance carry it.

---

## EMAIL

**To:** Michael Mehan
**Subject:** ARPA-H IGoR: Illumina as the TA4.2 sequencing and bioinformatics node

Hi Michael,

Sebastian Pineda suggested I reach out. I am putting together the disease-model and AI core (TA1 and TA2) of an ARPA-H IGoR proposal, with Purdue's Institute for Physical AI as prime and Ananth Grama as PI. The part where Illumina would fit is squarely bioinformatics, which is why Sebastian pointed me to you.

Briefly, IGoR funds a closed loop: a self-updating causal model of psychiatric disease (schizophrenia, extending to bipolar) that designs its own next experiment, validated labs that run it, and model-ready data that flows back and updates the model. We are organizing the laboratory layer in two parts. TA4.1 does the wet work (iPSC models, perturbation, imaging; Cellanome and others), and TA4.2 is the sequencing and bioinformatics readout, where Illumina would sit, downstream of the cell work, with NovaSeq, DRAGEN, and Connected Analytics turning each iteration's libraries into standardized data the model can ingest.

The reason this is a bioinformatics conversation and not only a sequencing one: the program is scored on cycle time, and the rate-limiter is how fast and how cleanly each round of data returns to the model. DRAGEN and ICA are what let that loop close, so the data layer is load-bearing rather than downstream cleanup. Your background, from the gene-phenotype prediction work onward, is close to how we are thinking about moving from genomic variation to cellular and clinical phenotype, so I suspect you will see the gaps faster than I can describe them.

I have attached a one-pager with the architecture and where TA4.2 fits. Two things I would value your read on: how the libraries from the TA4.1 labs would hand off cleanly into a DRAGEN and ICA pipeline, and what collaboration vehicle fits Illumina best (in-kind sequencing and reagents, an investigator collaboration, or a named subcontract).

Would a short call in the next week work? The first milestone, the Solution Summary, is due June 25, so sooner helps, but I am glad to work around your schedule.

Best,
Shahin

Shahin Mohammadi, PhD
Founder and CEO, Cytognosis Foundation
mohammadi@cytognosis.org

---

## Internal notes (do not send)

- Michael is the hands-on technical owner Sebastian routed you to (Director of Bioinformatics, under James Han). Engage on substance; the goal of a first call is a technical read on the TA4.2 interface plus identifying the right collaboration vehicle and internal sponsor.
- The genotype-to-phenotype hook is grounded in his actual background (USC gene-phenotype prediction); do not claim a shared collaborator, as none is verified.
- Keep TA1 in-house framing; do not disclose proprietary methods pre-NDA; route any NDA through Duane.
- If procurement is slow, in-kind sequencing or an investigator collaboration is likely faster than a named subcontract, consistent with the PCX precedent.
