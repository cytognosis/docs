# Cal.com Integration Evaluation

> **Status**: Historical evaluation — Cal.com is deployed at `cal.cytognosis.org`.
> **Date**: 2026-06-14
> **Author**: @mohammadi
> **Audience**: engineers
> **Tags**: `self-hosted`, `calcom`, `scheduling`

**Last verified: 2026-06-14** — `cal.cytognosis.org` is live, pointing to cytohost (`34.171.23.255`, ephemeral; `cg-org` DNS zone).

## Overview
Cal.com is an open-source scheduling tool that replaced Calendly for Cytognosis scheduling. This document is the original integration evaluation record.

## Deployment Options

### 1. Cal.com Cloud (Hosted)
- **Description:** Use Cal.com's managed hosting and simply embed the booking links on the Cytognosis website.
- **Pros:** Zero maintenance, easy to set up, high availability. Free for individuals (Core plan).
- **Cons:** Team features (Round Robin, Collective Events, Workflows, Routing logic) require the Team plan ($12/user/month). Data is hosted on Cal.com's servers.

### 2. Self-Hosted (Standalone Scheduling Website)
- **Description:** Deploy the open-source Cal.com repository on our own infrastructure (e.g., using Docker/Railway on Google Cloud/AWS). We would access it via a subdomain like `cal.cytognosis.ai` or internally.
- **Pros:** Completely free without per-seat licensing. Full control over data privacy and security. We get access to premium features (workflows, custom branding, round-robin) without a monthly fee.
- **Cons:** Requires maintenance, monitoring, and updates. We'll need to set up a PostgreSQL database and configure email sending (SMTP) for scheduling notifications.

## Integration Strategies (Cytognosis Website)

Regardless of the deployment option chosen, Cal.com provides robust options for integrating with our existing FastAPI/HTML frontend (`cytognosis/website`):

### Option A: Direct Embedding (Recommended)
Cal.com provides React components and raw HTML/JS snippets to embed the scheduler directly.
- **Inline Embed:** We can create a new page at `cytognosis.ai/book` (or add to `pages/`) and embed the calendar seamlessly within the page layout.
- **Popup Modal:** We can add a "Book a Demo" or "Meet the Team" button in our existing website header or footer that triggers a floating Cal.com modal.
- **Implementation:** Very straightforward. Just drop the embed snippet into `index.html` or the relevant HTML files in `/pages`, and load the script.

### Option B: Deep Integration via API/Webhooks
- **Description:** Since our website uses a Python backend (FastAPI, SQLite), we can capture scheduling events via Cal.com webhooks.
- **Use Case:** Creating custom user flows. For example, when a user books a meeting via our website embed, Cal.com triggers a webhook to our FastAPI backend. We can process this in `main.py`, update our internal `cytognosis.db` with the lead's information, and perhaps provision an account or send custom internal Slack/Teams notifications.

## Team Scheduling Features Overview
Cal.com excels in team scheduling, offering features perfectly suited for company-wide use:
- **Round Robin:** Automatically distributes meetings among available team members (useful for sales/demos).
- **Collective Events:** Allows users to book a time when *all* selected team members are available.
- **Routing Pages:** Ask visitors questions (e.g., "What are you interested in?") before directing them to the correct team member's booking calendar.
- **Time Zone Intelligence:** Effortlessly handles cross-timezone scheduling for remote teams.

## Recommendation & Next Steps

If the goal is to utilize team features without per-seat licensing costs, **Self-Hosting Cal.com on a dedicated server (e.g., `cal.cytognosis.ai`)** is the recommended path forward.

### Proposed Implementation Steps:
1. **Decision point:** Decide between Cloud Hosted ($12/mo/user for teams) vs Self-Hosted (Free + infra costs/maintenance).
2. **Infrastructure (If Self-Hosted):** Set up a VM or containerized service on our existing cloud provider to host the Cal.com Docker image and a PostgreSQL database.
3. **Configuration:** Connect Cal.com to our Google Workspace / Outlook for real-time calendar syncing. Set up SMTP for notifications.
4. **Team Setup:** Onboard the company, create team pages, and set up Round-Robin/Collective event types.
5. **Website Integration:** Grab the embed snippets for the relevant event types and inject them into the `cytognosis/website` HTML pages (inline or modal).
6. **(Optional) Backend Sync:** Create a new webhook route in `main.py` to listen for `/api/calcom-webhook` to sync meeting data with `database.db`.
