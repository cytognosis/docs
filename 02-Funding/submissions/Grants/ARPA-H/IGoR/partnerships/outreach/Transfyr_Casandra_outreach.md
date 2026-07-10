# Transfyr outreach (ARPA-H IGoR / PsychIGoR)

**Drafted:** 2026-06-15. **Status: Ready to send.** Duane cleared the Wegrzyn organizational-conflict question on 2026-06-16. The body still keeps Renee's name and any agency-facing coordination out, which is good practice regardless.
**To:** Casandra Philipson <casandra@transfyr.ai>
**Attach:** `onepagers/TA3-TA4_Transfyr.pdf`
**Why this framing:** Research shows Transfyr is an execution-observability layer (multimodal in-lab capture + ML), not a LabOP-style TA3 standards play. Their public interop posture is unknown (no SiLA/LabOP/Allotrope mentions; Ginkgo-foundry lineage; a "Myth of the Platform" post), so the email leads with the interop question and positions them as a cross-cutting reproducibility layer over TA4 that feeds TA2. Renee Wegrzyn is intentionally not named in the body (OCI plus post-firing political sensitivity at the agency we are bidding to). The opening is honest about origin: we found Transfyr on the IGoR teaming list, with no claim of prior familiarity or admiration.

---

## EMAIL

**To:** Casandra Philipson <casandra@transfyr.ai>
**Subject:** ARPA-H IGoR teaming: Cytognosis/IPAI and Transfyr on reproducibility

Hi Casandra,

Your team came up on the IGoR teaming list, and the problem you are working on, observability and reproducibility for scientific execution, looks like it could complement what we are assembling, so I wanted to reach out and learn more.

Quick context on us. Our team, PsychIGoR, is anchored by Purdue's Institute for Physical AI (IPAI) as prime, with its director, Ananth Grama, as PI. Cytognosis and IPAI jointly lead the disease-model and AI-engine core (TA1 and TA2), and McLean Hospital, a Harvard Medical School affiliate, anchors the clinical and translational genomics. We are building a closed loop: a causal model of psychiatric disease that designs its own next experiments and validates them across laboratories, and the model is only as trustworthy as the fidelity of the experiments feeding it.

That is why your space caught my eye. IGoR hinges on cross-laboratory concordance, the same protocol producing the same result across sites and operators, and on capturing what actually happened at the bench rather than what the protocol said. If I read your positioning right, that is squarely the problem you are tackling. We build protocol portability on LabOP, an open, design-time standard; an execution-time observability layer could complement it and feed our experiment-design engine grounded, real-world data.

I would rather ask plainly than assume, so one question matters most. You describe Transfyr as "the API layer for science." Does that mean genuine cross-vendor interoperability, open APIs and standard export formats, working alongside other companies' instruments, software, and protocol layers such as LabOP, or an observability layer built around your own stack? Both are valuable, but they fit an open architecture very differently, and "interoperable" means different things to different teams.

A few related questions, if a call makes sense:

- Have you deployed in mammalian and iPSC settings (iPSC-derived neurons, high-content and calcium imaging), or has your work centered on other assay types so far?
- What does lab onboarding look like in practice: hardware install, integration lift, and timeline?
- Can execution and provenance records be exported in standard, portable formats?
- Are you pursuing IGoR yourselves, as a prime or a sub, or open to joining a team?

Would 30 minutes in the next week or two be possible? I have attached a short overview of where we think a fit might be.

Best,
Shahin

Shahin Mohammadi, PhD
Founder and CEO, Cytognosis Foundation
mohammadi@cytognosis.org

---

## Internal notes (do not send)

- **Cleared:** Duane cleared the Wegrzyn OCI on 2026-06-16, so this is ready to send. The email stays clean of Renee's name and any agency-facing coordination, which remains good practice.
- **Do not name SIFT** here; the TA3 row stays "LabOP-based, partner in discussion." Do not imply a full or empty roster.
- **If they ask about Renee and the proposal:** keep it neutral and say the team and roles are still being finalized; do not discuss her ARPA-H tenure or framing in writing.
- **Likely answer to watch for:** if their interop is proprietary-only (the Cellanome pattern, "we have our own protocol/stack"), they fit as a cross-cutting reproducibility layer over TA4, not as the TA3 interop lead. If genuinely open, the TA3 conversation widens.
