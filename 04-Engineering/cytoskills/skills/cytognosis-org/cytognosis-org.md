> **Status**: Active
> **Date**: 2026-06-14
> **Author**: Cytognosis Foundation
> **Audience**: all staff, engineers, operations
> **Tags**: `operations`, `cytognosis-org`, `workspace`, `google-workspace`

# cytognosis-org — Organizational Resources Skill

> **Reading time**: ~5 minutes
> **If you only read one thing**: Load this skill when you need to know where something lives, how to perform a Google Workspace operation, or which email address to use. It is the authoritative map of Cytognosis file locations, repos, and workspace scripts.

---

## What It Is and Why

`cytognosis-org` is the resource routing and workspace operations skill for the Cytognosis Foundation. When asked "where is X?" or "how do I do Y in Workspace?", this skill provides the authoritative map: code repos, Drive folder structure, email matrix, document naming conventions, and workspace automation scripts.

**When to load this skill**:

- Finding where a file, resource, or repo lives
- Performing Google Workspace operations (email, docs, calendar, drive, sheets, slides)
- Looking up the correct email address for a domain (grants, board, science, etc.)
- Naming a new file or document correctly
- Looking up GCP / Cloud Run / DNS topology
- Any question involving `@cytognosis.org`, Drive folders, or shared workspace

**When NOT to load this skill**:

- Visual design standards: load `cytognosis-design-system-master`
- Development tooling (nox, cytocast, uv): load `cytognosis-dev`
- Interface templates: load `cytognosis-template-master`
- Cloud deployment decisions: defer to the `infrastructure` repo

---

## Organization Identity

| Field | Value |
|-------|-------|
| Legal Name | Cytognosis Foundation, Inc. |
| Type | 501(c)(3) Nonprofit |
| EIN | 39-4383634 |
| UEI | HS4PRLL7AKY5 |
| Founded | September 8, 2025 |
| Domain | @cytognosis.org |
| HQ | South San Francisco, CA |

---

## Code Repositories (GitHub: `cytognosis-foundation/`)

| Repo | Purpose | Local Path |
|------|---------|------------|
| `branding` | Design System + Cytognosis-wide skills (SoT for the design system) | `https://github.com/cytognosis/branding` |
| `cytocast` | Copier templating engine + dev skills + shared CI/CD | `https://github.com/cytognosis/cytocast` |
| `cytoskeleton` | Environment manager + interface templates + template-usage skills | `https://github.com/cytognosis/cytoskeleton` |
| `cytos` | Foundation kernel (data + models + schemas) | `https://github.com/cytognosis/cytos` |
| `cytoagent` | Runtime agents + orchestration + fabric | `https://github.com/cytognosis/cytoagent` |
| `cytoverse` | Foundation AI models | `https://github.com/cytognosis/cytoverse` |
| `cytoscope` | Biosensor firmware | `https://github.com/cytognosis/cytoscope` |
| `cytonome` | On-device edge AI | `https://github.com/cytognosis/cytonome` |
| `website` | Public UI (`cytognosis.org`) | `https://github.com/cytognosis/website` |
| `infrastructure` | DNS, Cloud Run, Terraform | `https://github.com/cytognosis/infrastructure` |
| `papers` | LaTeX manuscripts | `https://github.com/cytognosis/papers` |

---

## Google Drive (Cytognosis Foundation Shared Drive)

| Folder | Contents |
|--------|---------|
| `01-Grants-and-Funding` | NIH/ARPA-H proposals, LOIs, budgets |
| `02-Scientific-Platform` | DMPs, FAIR mapping, open science protocols |
| `03-Brand-and-Marketing` | Website copy, campaign matrices, social assets |
| `04-Legal-and-Regulatory` | Bylaws, contracts, compliance docs |
| `05-Operations` | Finance, board materials, HR |

---

## Email Matrix

| Group | Email | Purpose |
|-------|-------|---------|
| General | info@cytognosis.org | Public inquiries |
| Grants | grants@cytognosis.org | Funder correspondence |
| Board | board@cytognosis.org | Board of directors |
| Science | science@cytognosis.org | Scientific operations |
| Partnerships | partnerships@cytognosis.org | External alliances |

---

## Document Naming Convention

Format: `[Type]-[Topic]-[Version]-[Date]`

Types: `Grant`, `Deck`, `Report`, `Meeting`, `Template`, `Data`, `Draft`

Examples:

- `Grant-ARPA-H-Specific-Aims-v2-2026-03`
- `Report-Literature-Review-CTC-v1-2026-01`
- `Meeting-Board-Q2-Review-2026-06`

Never name files casually. Always enforce this convention.

---

## Google Docs / Slides Styling

For document and slide styling, load `cytognosis-design-system-master` for canonical token names. Quick reference:

| Element | Font | Size | Token |
|---------|------|------|-------|
| Title | Inter Bold | 28pt | `--cg-indigo-700` |
| Heading 1 | Inter Bold | 20pt | `--cg-indigo-500` |
| Heading 2 | Inter SemiBold | 16pt | `--cg-violet-600` |
| Heading 3 | Inter Medium | 14pt | `--cg-violet-600` |
| Body | Inter Regular | 11pt | `--text-primary-light` |
| Links | Inter Regular | 11pt | `--cg-magenta-600` |

Slides: 16:9 only. Max 6 bullets per slide. Cytognosis logo top-right. Start from `branding/design-system/templates/deck/`.

---

## Cloud Topology

- `cytognosis.org` → GCP Cloud DNS + Cloud Run
- All GCP actions must align with the `infrastructure` repo
- Internal PyPI: GCP Artifact Registry; OIDC via Workload Identity Federation per `cytocast/_shared/` workflows

---

## Workspace Scripts

Use existing scripts in the `branding` repo's `scripts/` directory. Do not write new auth logic.

| Script | Service |
|--------|---------|
| `scripts/gmail.py` | Email |
| `scripts/gcal.py` | Calendar |
| `scripts/drive.py` | Drive |
| `scripts/docs.py` | Docs |
| `scripts/sheets.py` | Sheets |
| `scripts/slides.py` | Slides |
| `scripts/chat.py` | Chat |

OAuth auto-refreshes via `scripts/auth.py` and system keyring.

---

## Email Signature

The branded HTML signature ships with the design system at `branding/design-system/templates/email-signature.html`. Never hand-author signatures inline. Load `cytognosis-design-system-master` to get the canonical version.

---

## Hard Rules (NEVER)

- NEVER send external emails without the branded signature
- NEVER create visual documents without consuming brand tokens
- NEVER use em dashes in email or document content
- NEVER name files casually; enforce the naming convention
- NEVER write new OAuth auth logic; use existing scripts
- NEVER guess where files live; look up in the matrices above

---

## Routing Rules

| Domain | Skill |
|--------|-------|
| Visual design standards, brand voice, microcopy | `cytognosis-design-system-master` |
| Scaffolding interface apps | `cytognosis-template-master` |
| Deep v10 brand reference | `cytognosis-branding` |
| Cytocast / cytoskeleton / nox / pyproject details | `cytognosis-dev` |
| Grants, narrative, scientific writing | `cytognosis-writer` |
| Cross-platform workflows, coordinated multi-skill task | `cytognosis-orchestrator` |
| Cloud deployment decisions | defer to `infrastructure` repo |

---

## Example: Finding Where a Specific Grant Document Lives

Task: "Where is the ARPA-H Specific Aims document?"

1. Load `cytognosis-org`.
2. Check Drive: `01-Grants-and-Funding` folder.
3. Name format: `Grant-ARPA-H-Specific-Aims-v<N>-<YYYY-MM>`.
4. If it is a code asset (LaTeX manuscript), check `https://github.com/cytognosis/papers`.
