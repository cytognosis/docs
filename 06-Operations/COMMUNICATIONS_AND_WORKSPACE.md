# Communications & Workspace Infrastructure

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: operators
> **Tags**: `operations`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

**Last Updated**: May 2026
**Ecosystem**: Google Workspace for Nonprofits

## 1. Domain Organization

- **Primary Domain**: `cytognosis.org`
- **Secondary Domains**: `cytognosis.com`, `cytognosis.ai`
- **Admin Console**: `admin.google.com`
- **Primary Administrator**: `mohammadi@cytognosis.org`

## 2. Groups & Role-Based Routing

We have optimized our intake routing to deprecate single-point dependency on individual inboxes. Site form submissions automatically direct into the following matrices:

| Group Address | Handled Forms / Operations | Default Access |
|---------------|---------------------------|----------------|
| `careers@cytognosis.org` | Applications (`/api/talent`), Volunteers (`/api/volunteer`) | Core Team |
| `partnerships@cytognosis.org` | Corporate & Strategic Inquiries (`/api/partnership`) | Core Team |
| `science@cytognosis.org` | Research Collaborations, Clinical Tools (`/api/research`) | Science Leads |
| `info@cytognosis.org` | General Contact, Press/Media inquiries (`/api/contact`) | Core Team |
| `stories@cytognosis.org` | HIPAA-compliant patient story intake (`/api/stories`) | Restricted |
| `gcp-data-scientists@` | RBAC provisioning for `cytognosis-phi-prod` Data Access | GCP Analytics |
| `gcp-infra-admins@` | Systems administration across Google Cloud | Infra Admins |

## 3. The "Noreply" Architecture & Seat Optimization

Historically, `noreply@cytognosis.org` consumed a paid Google Workspace seat. To aggressively optimize nonprofit tier allocations:

- **Deprecation**: The licensed `noreply` user account has been purged.
- **Current State**: Automated email dispatches from our Cloud Run application server simulate or route through standard group aliases or Google's raw SMTP infrastructure, preventing seat licensing waste.

## 4. Google Apps Scripts Deprecation

**Status: TERMINATED**
Historically, Cytognosis relied on Google Apps Scripts attached to `mohammadi@cytognosis.org` or `noreply` to intercept and process frontend website HTML form payloads.

**Why Deprecated**:

- Security: Apps scripts execute as the authorizing user, exposing Workspace scopes.
- Maintainability: Code was scattered across undocumented script editor windows.
- Concurrency: Severe rate limits on Gmail API dispatches.

**Current Paradigm**:
All form data directly hits our containerized Python (`FastAPI`) backend where it triggers robust NLP parsing, relational database ingestion (`SQLite/PostgreSQL`), and asynchronous email notification routing.
