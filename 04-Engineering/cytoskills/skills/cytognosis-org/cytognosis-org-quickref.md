> **Status**: Active
> **Date**: 2026-06-14
> **Author**: Cytognosis Foundation
> **Audience**: all staff, engineers, operations
> **Tags**: `quick-reference`, `cytognosis-org`

# cytognosis-org — Quick Reference

> **One line**: Load this skill to find where any Cytognosis resource lives, perform Google Workspace operations, or look up email addresses, naming conventions, and workspace scripts.
> **Full doc**: [cytognosis-org.md](cytognosis-org.md)

---

## Key Concepts

| Term | Definition |
|------|-----------|
| **Shared Drive** | Cytognosis Foundation Google Shared Drive with 5 top-level folders (01-Grants-and-Funding through 05-Operations). |
| **Document naming format** | `[Type]-[Topic]-[Version]-[Date]` (e.g., `Grant-ARPA-H-Specific-Aims-v2-2026-03`). |
| **Workspace scripts** | Pre-existing Python scripts in `scripts/` that wrap Gmail, Calendar, Drive, Docs, Sheets, Slides, and Chat. Never rewrite auth. |
| **@cytognosis.org** | The organizational domain. All email addresses are `<function>@cytognosis.org`. |
| **Infrastructure repo** | Source of truth for all GCP/Cloud Run/DNS decisions (`https://github.com/cytognosis/infrastructure`). |

---

## Drive Folder Map

| Folder | Contents |
|--------|---------|
| `01-Grants-and-Funding` | NIH/ARPA-H proposals, LOIs, budgets |
| `02-Scientific-Platform` | DMPs, FAIR mapping, open science protocols |
| `03-Brand-and-Marketing` | Website copy, campaign matrices, social assets |
| `04-Legal-and-Regulatory` | Bylaws, contracts, compliance docs |
| `05-Operations` | Finance, board materials, HR |

---

## Repo Map

| Repo | Purpose | Local Path |
|------|---------|------------|
| `branding` | Design system + skills | `https://github.com/cytognosis/branding` |
| `cytocast` | Copier template engine | `https://github.com/cytognosis/cytocast` |
| `cytoskeleton` | Environment manager | `https://github.com/cytognosis/cytoskeleton` |
| `cytos` | Foundation kernel | `https://github.com/cytognosis/cytos` |
| `cytoverse` | Foundation AI models | `https://github.com/cytognosis/cytoverse` |
| `cytoscope` | Biosensor firmware | `https://github.com/cytognosis/cytoscope` |
| `cytonome` | On-device edge AI | `https://github.com/cytognosis/cytonome` |
| `website` | cytognosis.org public site | `https://github.com/cytognosis/website` |
| `infrastructure` | DNS, Cloud Run, Terraform | `https://github.com/cytognosis/infrastructure` |
| `papers` | LaTeX manuscripts | `https://github.com/cytognosis/papers` |

---

## Email Matrix

| Group | Address |
|-------|---------|
| General | info@cytognosis.org |
| Grants | grants@cytognosis.org |
| Board | board@cytognosis.org |
| Science | science@cytognosis.org |
| Partnerships | partnerships@cytognosis.org |

---

## Naming Convention

Pattern: `[Type]-[Topic]-[Version]-[Date]`

| Type values | Deck, Draft, Grant, Meeting, Report, Template, Data |
|-------------|-----------------------------------------------------|

Examples: `Grant-NIH-R01-Specific-Aims-v1-2026-06`, `Report-CTC-Literature-Review-v2-2026-01`

---

## Workspace Scripts

| Script | Service |
|--------|---------|
| `scripts/gmail.py` | Email (send, read, search) |
| `scripts/gcal.py` | Calendar (create, update events) |
| `scripts/drive.py` | Drive (upload, search, share) |
| `scripts/docs.py` | Google Docs (create, update) |
| `scripts/sheets.py` | Google Sheets (read, write) |
| `scripts/slides.py` | Google Slides (create, update) |
| `scripts/chat.py` | Google Chat (send messages) |

Auth: `scripts/auth.py` + system keyring. Never rewrite.

---

## Common Patterns

```bash
# Find a grant document on Drive (use scripts/drive.py)
python scripts/drive.py search "Grant-ARPA-H-Specific-Aims"

# Send an email with the branded signature
# Load the signature from: branding/design-system/templates/email-signature.html
python scripts/gmail.py send --to grants@cytognosis.org --signature canonical
```

---

## Error Quick-Fix

| Error / Symptom | Fix |
|-----------------|-----|
| Can't find a file on Drive | Check the correct top-level folder; use naming convention pattern to narrow |
| Email missing branded signature | Load `cytognosis-design-system-master` for canonical signature path |
| OAuth error in workspace script | Do not rewrite auth; check `scripts/auth.py` and system keyring |
| Cloud change needed | Always align with `infrastructure` repo before making GCP changes |
| File named casually | Rename to match `[Type]-[Topic]-[Version]-[Date]` format |

---

## See Also

- [Full documentation](cytognosis-org.md) — comprehensive reference + explanation
- [cytognosis-design-system-master](../cytognosis-design-system-master/cytognosis-design-system-master.md) — brand tokens for document styling
- [cytognosis-dev](../cytognosis-dev/cytognosis-dev.md) — development tooling (cytocast, nox, uv)
- [cytognosis-writer](../cytognosis-writer/cytognosis-writer.md) — grants and proposals (content, not file location)
