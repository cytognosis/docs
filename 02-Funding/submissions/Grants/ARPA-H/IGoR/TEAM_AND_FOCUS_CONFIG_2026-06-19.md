# PsychIGoR — Canonical Team and Focus Configuration

**Last updated:** 2026-06-19. Single source of truth for the project title, team roster, role/focus descriptions, and submission POCs. Apply to the Solution Summary, the full proposal, and the Google Docs versions. Supersedes team/role text in older drafts.

## Title and naming

- **Team / short name:** PsychIGoR
- **Full project title:** PsychIGoR: Intelligence Generation of Disease Mechanisms for Psychiatric Disorders
- **Solicitation:** ARPA-H-SOL-26-155 (IGoR), Proactive Health Office
- **Prime (lead organization):** Purdue University, Institute for Physical AI (IPAI)

## Framing decision

We describe contributions by **work focus**, not by the program's TA1 to TA4 labels, because the TA definitions are inconsistent. The focus set is arranged as the program's closed loop (model, generate, protocol, execute, update), so coverage of the program's interest areas stays clear to reviewers.

## Program roles

| Role | Person / org | Status |
|---|---|---|
| Lead organization (prime) | Purdue IPAI | Confirmed |
| Principal Investigator | Ananth Grama (IPAI, Purdue) | Confirmed |
| Project Manager | Patricia Purcell (hired via Cytognosis) | Confirmed |
| Software Engineer / Architect | Cytognosis hire (recruiting); Elham Jebalbarezi Sarbijan (IPAI) interim | Recruiting |
| Prime Technical POC (one only, per ISO) | Ananth Grama (IPAI), ayg@purdue.edu | — |
| Subawardee Technical POC | Shahin Mohammadi (Cytognosis), mohammadi@cytognosis.org | — |
| Prime Administrative POC | Tabitha M. Cinowski, Operations Manager, IPAI (cinowski@purdue.edu) | Confirmed |
| Submitter (ARPA-H Solutions account) | Shahin Mohammadi, mohammadi@cytognosis.org | Confirmed |

## Focus areas (closed loop)

| Focus area | Lead | Contributors | Status |
|---|---|---|---|
| Disease-mechanism modeling, computational | Shahin Mohammadi (Cytognosis) and Ananth Grama (IPAI) | Anne Carpenter (IPAI) | Confirmed |
| Disease-mechanism modeling, experimental | Matthew Tegtmeyer (Purdue/IPAI) | — | Confirmed |
| Disease-mechanism modeling, clinical/translational | W. Brad Ruzicka (McLean/HMS) | — | Confirmed |
| Mechanism-grounded hypothesis and experiment-intent generation | Shahin Mohammadi (Cytognosis) | Ananth Grama (IPAI) | Confirmed |
| Autonomous experiment-design engine | Ananth Grama (IPAI) | Phylo/Biomni, Kexin Huang (optional) | Lead confirmed |
| Interoperable perturbation protocols (and user interface) | Dan Bryce (SIFT) | Robert Goldman (SIFT, advisor) | Confirmed |
| Experimental execution and validated-lab marketplace, industry | Cellanome | — | Partner confirmed; costs/docs pending |
| Experimental execution and validated-lab marketplace, academic | Matthew Tegtmeyer (Purdue) | Fixed-cell high-plex readouts (RNA ~350-plex, protein ~50-plex, Cell-Painting-style morphology, in-situ CRISPR-guide sequencing) | Confirmed |
| Cross-cutting semantic foundation (schemas, ontologies, interfaces) | Shahin Mohammadi (Cytognosis) and Dan Bryce (SIFT) | — | Confirmed |
| Sequencing and cloud platform | Illumina, James Han and Michael Mehan | — | Optional / TBD |
| Strategic partnership | Xaira, Ci Chu | — | Optional / TBD |

**Loop note:** modeling feeds hypothesis and experiment-intent generation and the design engine, which emit interoperable protocols executed by the marketplace arms; results return to update the models. The semantic foundation spans the whole loop so an entity keeps one identifier across the model, the protocol, and the lab record.

## Status notes (internal)

- **Confirmed:** Grama, Carpenter, Tegtmeyer (all Purdue/IPAI), Purcell (PM), Ruzicka (McLean), Bryce and Goldman (SIFT), Mohammadi (Cytognosis).
- **Project Manager and Software Architect are Cytognosis hires** (Ananth's suggestion), so their labor plus Cytognosis's de minimis indirect accrue to Cytognosis as income. In the proposal cost model, place both lines under Cytognosis, not Purdue. The architect is a planned Cytognosis hire, not a Purdue person; Elham Jebalbarezi Sarbijan (IPAI) is an interim placeholder, subject to change. Anna Merkoulovitch is off market and no longer a candidate.
- **Cellanome:** confirmed industry execution arm. Proceed with our own cost estimate and share it with Cellanome afterward to verify (they have not returned docs/costs).
- **Optional / TBD:** Illumina, Xaira, Phylo/Biomni. Name only where it strengthens the case; do not gate on them.
- **Academic arm fixed-cell readouts (Element Biosciences AVITI24 instrument):** available through Matt Tegtmeyer's lab; likely not required at this scope as a separate teaming line. Element is not a teaming partner; no budget line.

## Interpretations applied

- "David (SIFT)" read as **Dan Bryce** (lead), with **Robert Goldman** as advisor, matching the roster.
- Anne Carpenter set to **Confirmed** per this configuration (reverses the earlier "prospective" marking).
