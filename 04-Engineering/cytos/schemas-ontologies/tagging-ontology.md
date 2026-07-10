---
title: Skill-Tagging Ontology Recommendation for Cytoskeleton / Cytoagent
author: Shahin Mohammadi (with Claude)
date: 2026-05-18
status: recommendation, ready for review
scope: choose controlled vocabularies for tagging agent skills on two distinct axes
---

# Skill-Tagging Ontologies — Recommendation

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: engineers
> **Tags**: `engineering`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

## 1. Problem framing

We need to tag the agent-skill library on **two orthogonal axes**, because the skills carry two kinds of meaning that don't reduce to each other:

- **Axis A — *Coding / use-case axis*.** What kind of software-engineering activity is this skill *doing*? (Construction, refactoring, test writing, CI scaffolding, code review, documentation, debugging, etc.) This applies to anything code-shaped: `dev-standards`, `skill-creator`, `bio-research:nextflow-development`, `web-artifacts-builder`, `doc-coauthoring`, the `xlsx`/`pptx`/`docx`/`pdf` builders, etc.

- **Axis B — *Virtual-organization axis*.** Which org function does this skill serve? A skill like `legal:review-contract` exists to do work that belongs to the Legal/Compliance function; `human-resources:draft-offer` belongs to HR; `finance:reconciliation` belongs to Finance. Many skills sit cleanly inside one function (legal, HR, sales, marketing, product, ops, IT). Some skills cross functions and need multi-tag.

The two axes are not redundant because a single skill can score on both — e.g., a custom skill that scaffolds an audit-evidence Python harness is *Axis A: construction + scripting* AND *Axis B: APQC 11.0 Risk, Compliance & Resiliency*. Collapsing them loses information; keeping them separate makes routing, search, and capability mapping clean.

Per your stated preference, every tag should resolve to an **open / standard URI as the canonical ID**, with **popular/colloquial labels as aliases** for LLM-recognition and human readability.

---

## 2. Axis A — Coding / use-case taxonomy

### 2.1 Candidates evaluated

| Candidate | Open license | Stable IDs / SKOS | LLM-recognized | Granularity | Verdict |
|---|---|---|---|---|---|
| **SWEBOK v4 (IEEE, 2024)** — 18 Knowledge Areas (Requirements, Architecture, Design, Construction, Testing, Maintenance, Config Mgmt, SE Management, SE Process, Models & Methods, Quality, Professional Practice, Economics, **Security**, **Operations**, plus 3 Foundation KAs) | ❌ IEEE copyright, paywalled PDF | ❌ No SKOS/OWL release | ✅ Strong on KA names | Shallow (~3 levels, ~300 leaves) | **Use the *label set*, not the document.** KA names are generic ("Software Testing", "Software Construction") and not IP-protected. Excellent backbone. |
| **ACM CCS 2012** — 13 root categories, ~2,100 concepts in SKOS/RDF | ⚠ Research/education only; commercial reuse needs ACM permission | ✅ SKOS/RDF available; stable URIs | ⚠ Moderate — research-flavored phrasing | Deep (4–6 levels) | Useful as an *additional ID* for the heavyweight SE concepts (the `Software and its engineering` subtree), but the verbose path-phrasing is awkward as a primary tag. |
| **GitHub Topics (curated)** — `github/explore` repo, ~500 curated topics, flat | ✅ CC-BY-4.0 | ✅ Markdown + JSON feed; topic URLs are stable (e.g. `github.com/topics/refactoring`) | ✅ Excellent — saturated in training data | Flat | **Use as the alias layer.** Labels like `testing`, `ci`, `refactoring`, `static-analysis`, `code-review` are how everyone (and every LLM) talks about these tasks. Weakness: technology-heavy and unstructured. |
| **Stack Overflow tags** | ✅ CC-BY-SA on tag wikis | ✅ Data dump + API | ✅ Strong | Flat folksonomy, ~63k tags | Too noisy for a controlled vocab — most tags are technologies (`postgres`) or error symptoms, not task-types. Skip as primary. |
| **SWE-bench Pro / SWE Atlas categories** — bug-fixes, feature requests, optimizations, security updates, UI/UX, code-Q&A, test writing, refactoring | ✅ MIT | ⚠ GitHub repo, no SKOS | ✅ Strong in code-AI literature | Flat, ~8 leaves | **Use as an "intent" sub-axis.** These are *what is the user trying to accomplish* labels, complementary to SWEBOK's *what kind of engineering work*. |
| **ISO/IEC/IEEE 12207:2017** — 30 lifecycle processes | ❌ ~CHF 200 standard | ❌ PDF only | ⚠ Process names known | Shallow | Process-centric not task-centric, paywalled, kills it. |
| **IEEE Thesaurus / IEEE Taxonomy** — ~12k preferred terms, BT/NT/RT | ⚠ Free PDF after form, redistribution unclear | ❌ No public SKOS | ⚠ Moderate | Very deep but covers all of EE/CS | Too broad for SE-tagging; redistribution friction. Skip. |
| **CodeXGLUE (Microsoft Research)** — 10 code-AI task types | ✅ MIT / CC-BY | ❌ README only | ✅ Strong in code-AI | Flat, 10 leaves | Useful as a niche "capability type" axis (code-summarization, clone-detection), not as a primary use-case tag. Skip as primary. |
| **SEON (academic SE Ontology Network)** | ⚠ Academic | ✅ OWL | ❌ Low recognition | Deep | Too academic, low LLM recognition, low adoption. Skip. |
| **Wikidata SE Q-IDs** | ✅ CC0 (most permissive) | ✅ Stable Q-IDs, SPARQL | ✅ Strong on labels | ❌ No curated SE subtree | **Use for stable URI minting** — every SWEBOK KA has a Wikidata Q-ID we can attach. Doesn't carry its own hierarchy, so it's a registrar not a taxonomy. |
| **Microsoft Learn Azure agent-skills catalog** | ⚠ MS proprietary docs | ✅ Public repo | ✅ Strong | 6 role bundles, 193 skills | Azure-specific. Useful as a sibling reference (same shape as cytoagent), not a vendor-neutral tag vocab. |
| **anthropics/skills repo folders** — Creative & Design, Development & Technical, Enterprise & Communication, Document Skills | ✅ Public | ❌ No formal vocab | ✅ Strong | 4 buckets | Too coarse to be the primary; use as a high-level fallback. |

### 2.2 Recommendation for Axis A

**Hybrid: SWEBOK v4 KA names (re-derived, not copied) as the backbone, SWE-bench task intents as the intent sub-axis, GitHub Topics as the alias layer, Wikidata Q-IDs as the canonical URIs.**

Concretely, build a small (~20-term) cytoskeleton-owned vocabulary `cyto:se/*` whose labels mirror the SWEBOK KAs (no IP issue — these are generic terms: "Requirements", "Construction", "Testing", "Refactoring", "Documentation"…), each enriched with:

- `wikidata`: a stable Wikidata Q-ID — gives you a CC0 canonical URI;
- `aliases`: 3–5 GitHub-Topics-style labels for LLM/search recognition;
- `intent` (optional, multi-value): one of the SWE-bench/SWE-Atlas task intents (`bugfix`, `feature`, `refactor`, `test-writing`, `optimization`, `security-update`, `codebase-qa`, `ui-ux`).

Why this beats the alternatives:
- SWEBOK v4 is the most thoughtfully partitioned coding-skill carving in existence and just added **Security** and **Operations** in 2024 (real coverage of DevSecOps);
- Re-deriving the *label set* avoids the SWEBOK paywall/IP problem since the words are generic;
- GitHub-Topic aliases are how the LLM actually thinks about it;
- Wikidata Q-IDs give you the CC0 stable URI without inheriting ACM CCS's research framing.

---

## 3. Axis B — Virtual organization (department/function) taxonomy

### 3.1 Candidates evaluated

| Candidate | Open license | Stable IDs / SKOS | LLM-recognized | Shape | Verdict |
|---|---|---|---|---|---|
| **APQC PCF Cross-Industry v7.4 (Aug 2024)** — 13 top-level categories, 5 levels deep, ~1,000+ leaves, every node has a 5-digit ID | ✅ Free download, perpetual royalty-free reuse w/ attribution ("open standard") | ⚠ PDF/Excel canonical; no out-of-the-box SKOS but trivial to wrap | ✅ Strong on category labels | **Function/process-based** (this is exactly what you want) | **TOP PICK.** Cross-industry, function-shaped, 5-digit IDs perfect for stable refs, and the 13 roots map 1:1 to virtual-org departments. |
| **ESCO v1.2.0 (May 2024)** — 3,039 occupations + 13,939 skills + qualifications, all SKOS-XL | ✅ EUPL-equivalent open license | ✅ **Gold-standard machine-readable**: SKOS-XL, OWL, JSON-LD, TTL, stable `data.europa.eu/esco/...` URIs | ⚠ Moderate (known in EU/HR contexts) | **Hybrid occupations + skills** | **Layer this UNDER PCF for the *skill* dimension.** ESCO Skills is the right place to ground "what specific capability does this skill embody" — its skill hierarchy is much richer than PCF's. Don't use it for *function* tagging — ESCO Occupations is ISCO-shaped and you'd be tagging jobs not departments. |
| **ArchiMate 3.2 Business Layer (Open Group, 2023)** — metamodel with classes for Business Function, Business Process, Business Service, Business Role, Business Capability | ✅ Free spec | ⚠ Open Exchange XML; no canonical SKOS of department names because there *aren't* any | ✅ Strong on the metamodel | **Metamodel, not a populated taxonomy** | **Use as the upper layer.** Adopt `archimate:BusinessFunction` as the RDF/SKOS *class*, then populate instances with APQC PCF leaves. Best-of-both. |
| O*NET-SOC 30.2 (US DOL, 2025) | ✅ CC-BY-4.0, rich machine-readable | ✅ Stable codes | ✅ Strong | Occupations, not functions | Wrong shape — tags "software developer," not "Engineering dept." Skip as primary; useful only if you also want to tag *who would do this work*. |
| ISCO-08 (ILO, 2008) | ✅ Free | ⚠ ESCO ships ISCO mappings in SKOS | ✅ Strong | Occupations | Same problem as O*NET — occupations not departments. Useful as cross-walk only. |
| SOC 2018 (US BLS) | ✅ Public domain | ✅ | ✅ Strong | Occupations, US flavor | Same problem. Skip. |
| TOVE (Univ. of Toronto, 1990s) | ✅ Academic | ✅ OWL | ❌ Low | Foundational ontology | Dormant. Foundational reading only. Skip. |
| Schema.org `Organization` / `department` / `Role` | ✅ Open | ✅ JSON-LD stable | ✅ Very strong | **Wrapper classes only**, no values | Use as the outer wrapper (`schema:department` property), but it provides no controlled vocabulary of department *names* — you still need APQC for that. |
| Uschold Enterprise Ontology (1995) | ✅ Academic | ⚠ | ❌ | Foundational | Dormant, foundational only. Skip. |
| Business Architecture Guild BIZBOK v15 (2025) | ❌ Members-only paywall | ❌ Behind login | ⚠ | Capability-based industry refs | Skip — proprietary. |
| NACE Rev 2.1 (Eurostat, Jan 2025) | ✅ Free | ✅ | ⚠ | **Industry**, not function | Use only if you also want to tag the *enterprise's industry*, not internal departments. Skip for this purpose. |
| ITIL 4 (34 practices) / COBIT 2019 (40 objectives) | ❌ Axelos/ISACA proprietary | ❌ | ⚠ | IT-only | Excellent for the **IT-subtree under PCF Cat 8.0** if you go deep on IT skills, but proprietary licensing means we can only *reference* their names. Skip as a primary; possible internal sub-vocab for IT. |

### 3.2 Recommendation for Axis B

**Primary: APQC PCF v7.4 Cross-Industry,** with **ArchiMate 3.2** as the RDF meta-layer (`archimate:BusinessFunction`), optionally **ESCO Skills** layered underneath when you also want a *skill* (not function) granularity, and **schema.org `Organization` / `department`** as the outer JSON-LD wrapper.

APQC PCF wins on every axis that matters for this use case:
1. **Function-shaped** — its 13 roots are literal department slots (HR, IT, Finance, Risk/Compliance, Sales/Marketing, Operations, Strategy, …).
2. **Cross-industry** — won't pin you to one vertical.
3. **Free + reusable** — published under a perpetual royalty-free attribution license.
4. **Stable 5-digit IDs** at every node — perfect for `urn:apqc:pcf:1.0/8.1.4` style refs.
5. **LLM-recognized** — APQC PCF is heavily cited in enterprise/consulting literature; LLMs know the category labels.
6. **5 levels deep** — enough granularity that skills can pin to a sub-process, not just a department.

The only real weakness — no native SKOS — is trivially addressed: cytoskeleton can ship a generated SKOS conversion of the relevant subtree (the PCF license permits derivative works under attribution).

For the **specialized-skill bundles already in your stack**, the APQC top-level mapping is unusually clean:

| Existing skill namespace | APQC PCF top-level |
|---|---|
| `finance:*` (8 skills) | **9.0 Manage Financial Resources** |
| `human-resources:*` (9 skills) | **7.0 Develop and Manage Human Capital** |
| `legal:*` (9 skills) | **11.0 Manage Enterprise Risk, Compliance, Remediation, and Resiliency** |
| `sales:*` (9 skills), `marketing:*` (8 skills) | **3.0 Market and Sell Products and Services** |
| `product-management:*` (8 skills), `design:*` (7 skills) | **2.0 Develop and Manage Products and Services** |
| `operations:*` (8 skills) | spans **11.0** (risk/compliance), **13.0** (Business Capabilities), and **8.0** (IT) — multi-tag |
| `enterprise-search:*`, `google-workspace`, `slack-by-salesforce:*` | **8.0 Manage Information Technology** |
| `data:*` (8 skills) | **8.0 Manage IT** + **13.0 Business Capabilities** |
| `internal-comms`, `brand-identity`, `brand-voice:*` | **3.0 Market and Sell** + **12.0 Manage External Relationships** (when external) |
| `bio-research:*` | Cytognosis-domain extension — extend PCF locally with a `cyto:science/*` subtree (research is the core product of a research org) |
| `grant-writing`, `science-platform`, `openness` | **1.0 Develop Vision and Strategy** + **12.0 Manage External Relationships** |

That every namespace lands cleanly is the strongest practical signal that PCF is the right backbone.

---

## 4. Combined recommendation

Use **both** ontologies in parallel — they live on different axes and answer different routing questions:

```
┌──────────────────────────────────────────────────────────────┐
│  AXIS A — coding/use-case                                    │
│  cyto:se/* (SWEBOK-derived labels)                           │
│    └─ wikidata: Q-ID (canonical URI, CC0)                    │
│    └─ aliases: GitHub-Topics labels (LLM recognition)        │
│    └─ intent: SWE-bench intent (bugfix/refactor/test/…)      │
├──────────────────────────────────────────────────────────────┤
│  AXIS B — virtual organization                               │
│  apqc:pcf:<code> (PCF v7.4 canonical 5-digit ID)             │
│    └─ rdf:type archimate:BusinessFunction                    │
│    └─ aliases: human-readable dept name + ESCO Occupation    │
│    └─ skill: optional ESCO Skill URI (when finer than PCF)   │
└──────────────────────────────────────────────────────────────┘
```

A skill is tagged on **whichever axes apply**:
- Pure-coding skills (e.g., `web-artifacts-builder`) get **Axis A only**.
- Pure-function skills (e.g., `legal:review-contract`) get **Axis B only**.
- Function-specific coding skills (e.g., a "scaffold a SOX audit Python harness" skill) get **both**.

---

## 5. Worked tagging example (against your existing skills)

YAML frontmatter additions, showing both axes, primary IDs first, aliases second:

```yaml
# legal:review-contract
tags:
  org_function:
    primary: apqc:pcf:11.2.3      # Manage regulatory compliance
    class: archimate:BusinessFunction
    aliases: [legal, contracts, compliance]
    esco_occupation: http://data.europa.eu/esco/occupation/2611.1  # Lawyer
  # no Axis A — this is not a coding skill
```

```yaml
# human-resources:draft-offer
tags:
  org_function:
    primary: apqc:pcf:7.1.5       # Recruit, source, and select employees
    class: archimate:BusinessFunction
    aliases: [hr, recruiting, offer-letter]
    esco_skill: http://data.europa.eu/esco/skill/...  # "draft employment contracts"
```

```yaml
# dev-standards          (pure coding skill, no specific org function — applies anywhere)
tags:
  use_case:
    primary: cyto:se/quality       # SWEBOK KA "Software Quality"
    wikidata: Q1156234              # software quality
    aliases: [code-quality, linting, static-analysis, ci]
    intent: [refactor, test-writing]
```

```yaml
# bio-research:nextflow-development
tags:
  use_case:
    primary: cyto:se/construction
    wikidata: Q282682               # software construction
    aliases: [bioinformatics, pipeline, workflow, nextflow]
    intent: [feature, scripting]
  org_function:
    primary: cyto:science/computational-biology   # cytognosis local extension
    class: archimate:BusinessFunction
    aliases: [bioinformatics, research, computational-biology]
```

```yaml
# skill-creator          (coding skill that operates on the meta-layer)
tags:
  use_case:
    primary: cyto:se/se-process
    wikidata: Q1330336              # software development process
    aliases: [scaffolding, meta-programming, code-generation]
    intent: [feature, refactor]
  org_function:
    primary: apqc:pcf:8.5           # Manage IT knowledge, innovation, and ways of working
    class: archimate:BusinessFunction
    aliases: [developer-experience, internal-tooling]
```

---

## 6. Drop-in schema for cytoskeleton

Recommend cytoskeleton ship **two SKOS files** (with stable cytoskeleton URIs as the primary IDs, all standard ontology URIs as `skos:closeMatch` / `skos:exactMatch`):

```
cytoskeleton/ontologies/
├── cyto-se-usecase.ttl          # Axis A — ~20 SWEBOK-derived concepts,
│                                 #          each cross-walked to Wikidata + GH Topics
├── cyto-org-function.ttl        # Axis B — APQC PCF v7.4 subtree (the
│                                 #          ~80 nodes you actually use), each
│                                 #          typed as archimate:BusinessFunction,
│                                 #          with ESCO occupation/skill links
└── README.md                    # change log, versioning policy
```

Both files vendored into cytoskeleton, versioned, and re-exported from cytocast so downstream packages (cytoagent, cytos, Yar) consume one canonical copy. Pin a version (`@cyto-se-usecase/v1.0.0`) in skill frontmatter so taxonomy evolution doesn't silently retag existing skills.

---

## 7. What I'd skip and why

- **ACM CCS** alone — verbose, research-flavored, commercial-use friction. Acceptable as a *secondary* cross-walk for theoretical-CS skills, not as primary.
- **ISO 12207** — paywalled, process- not task-centric.
- **O*NET / ISCO / SOC** — these tag *occupations*, not *departments*. Wrong shape. (Optional: keep one ESCO Occupation cross-walk on each function tag for HR-style queries like "what role would do this?")
- **TOVE / Uschold Enterprise Ontology** — academic, dormant.
- **BIZBOK** — paywalled.
- **NACE** — industry not function.
- **ITIL / COBIT** — IT-only, proprietary; OK as a private sub-vocab inside PCF 8.0 if you go deep on IT, but don't redistribute their labels.
- **SEON** — academic, low recognition.
- **Stack Overflow tags** — folksonomy, too noisy as a controlled vocab.

---

## 8. Implementation order (suggested)

1. **Author `cyto-org-function.ttl`** — start by manually picking the ~80 APQC PCF leaves that cover your installed skills (the table in §3.2 already pins 95% of namespaces to a PCF root). Add `archimate:BusinessFunction` typing and `schema:Organization`-friendly aliases. Add a `cyto:science/*` local extension for the bio-research subtree.
2. **Author `cyto-se-usecase.ttl`** — write ~20 SWEBOK-derived concepts, each with Wikidata cross-walk and GitHub-Topic aliases. Add the SWE-bench intent enum as a separate property (not a class).
3. **Add `tags:` to skill frontmatter** in cytoskeleton's skill template (and propagate via cytocast).
4. **Backfill** the ~200 existing skills — most can be auto-tagged from namespace prefix using §3.2's mapping; spot-check by hand.
5. **Add a CI gate** in cytoskeleton that fails if a skill is missing both `tags.use_case` and `tags.org_function` (one or both is required).
6. **Publish** SKOS files at `https://cytognosis.org/ontology/{cyto-se-usecase,cyto-org-function}/v1.0.0` once cytoskeleton's site infra is up — gives every downstream consumer a stable dereferenceable URI.

---

## Sources

### Axis A
- [ACM CCS 2012](https://www.acm.org/publications/class-2012)
- [SWEBOK v4 (IEEE Computer Society)](https://www.computer.org/education/bodies-of-knowledge/software-engineering)
- [SWEBOK v4 release announcement](https://www.basicinputoutput.com/2024/10/guide-to-swebok-v40-has-been-released.html)
- [IEEE Thesaurus (Jan 2026 PDF)](https://www.ieee.org/publications/services/thesaurus.html)
- [ISO/IEC/IEEE 12207:2017](https://www.iso.org/standard/63712.html)
- [github/explore (GitHub Topics source)](https://github.com/github/explore)
- [Stack Overflow tag trends](https://trends.stackoverflow.co/)
- [Microsoft CodeXGLUE](https://github.com/microsoft/CodeXGLUE)
- [SEON ontology](https://nemo.inf.ufes.br/seon/)
- [Wikidata: software development (Q638608)](https://www.wikidata.org/wiki/Q638608)
- [Azure Agent Skills catalog](https://learn.microsoft.com/en-us/training/support/agent-skills)
- [SWE-bench leaderboards](https://www.swebench.com/)
- [anthropics/skills repo](https://github.com/anthropics/skills)

### Axis B
- [APQC PCF Cross-Industry v7.4 PDF](https://www.apqc.org/resource-library/resource-listing/apqc-process-classification-framework-pcf-cross-industry-pdf-12)
- [APQC Process Frameworks hub](https://www.apqc.org/process-frameworks)
- [ESCO Classification](https://esco.ec.europa.eu/en/classification)
- [ESCO v1.2 release notes](https://esco.ec.europa.eu/en/about-esco/escopedia/escopedia/esco-v12)
- [ESCO SKOS documentation](https://esco.ec.europa.eu/en/about-esco/escopedia/escopedia/simple-knowledge-organisation-system-skos)
- [ESCO Download portal](https://esco.ec.europa.eu/en/use-esco/download)
- [ArchiMate 3.2 — Business Layer](https://pubs.opengroup.org/architecture/archimate3-doc/ch-Business-Layer.html)
- [O*NET 30.2 Database & License](https://www.onetcenter.org/license_db.html)
- [ISCO-08 (ILO)](https://www.ilo.org/publications/international-standard-classification-occupations-2008-isco-08-structure)
- [SOC 2018 Major Groups (BLS)](https://www.bls.gov/soc/2018/major_groups.htm)
- [TOVE — Univ. of Toronto EIL](https://eil.mie.utoronto.ca/theory/enterprise-modelling/tove/)
- [schema.org Organization](https://schema.org/Organization)
- [schema.org department property](https://schema.org/department)
- [BIZBOK v15 release](https://www.prnewswire.com/news-releases/business-architecture-guild-releases-bizbok-guide-v15-302736535.html)
- [NACE Rev. 2.1 (Eurostat 2025)](https://ec.europa.eu/eurostat/web/products-manuals-and-guidelines/w/ks-gq-24-007)
- [COBIT (ISACA)](https://www.isaca.org/resources/cobit)
