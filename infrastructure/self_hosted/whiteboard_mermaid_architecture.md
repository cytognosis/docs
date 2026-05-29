# Extended Self-Hosting Evaluation Report

This report evaluates the feasibility, pricing, and architectural options for self-hosting advanced features of Cal.com, Zotero, Neo4j, and Mermaid.js for the Cytognosis Foundation.

---

## 📅 1. Cal.com Advanced Features

**Domain Strategy (`cal.cytognosis.org/{USER}`)**
- **Feasibility:** High. By setting `NEXT_PUBLIC_WEBAPP_URL=https://cal.cytognosis.org` in our self-hosted instance, all user booking pages will automatically generate at `cal.cytognosis.org/{username}`. We can use Cloud DNS to point `cal.cytognosis.org` directly to the GCP instance we previously provisioned.

**Multiple Personal Calendars**
- **Feasibility:** High. The self-hosted version of Cal.com fully supports connecting multiple calendars per user (e.g., their `@cytognosis.org` Google Workspace calendar AND their personal Gmail calendar) to avoid double-bookings. There are no artificial limits on integrations in the open-source version.

**Android App Compatibility**
- **Feasibility:** Low/Workaround Required. The official Cal.com Android app is hardcoded to connect to their commercial cloud infrastructure (`cal.com`). 
- **Solution:** Instead of the native app, users can rely on the **Progressive Web App (PWA)**. By navigating to `cal.cytognosis.org` in their mobile browser and selecting "Add to Home Screen," it behaves almost identically to a native app, complete with responsive mobile views and caching.

---

## 📚 2. Zotero & Google Drive Integration

> **Status — superseded.** The original plan in this section (self-hosted Zotero data server + Drive for PDFs) was replaced after the `foxsen/zotero-selfhost` image was abandoned upstream and the maintained forks proved too thin to bet sovereignty on. The current architecture uses Zotero's free cloud for metadata-only sync (no PDFs ever leave Cytognosis-controlled storage) and Google Drive `Library/Attachments/` as the canonical PDF store. Annotations live in Drive-synced ISO 32000 in-PDF markup plus a self-hosted Hypothes.is instance for W3C Web Annotation. See [`../data-strategy/paper-library-architecture.md`](../data-strategy/paper-library-architecture.md) for the canonical architecture and [`logseq_knowledge_architecture.md`](logseq_knowledge_architecture.md) for the researcher-facing workflow.

The historical evaluation below is preserved for context.

<details>
<summary>Original (superseded) self-hosted Zotero plan</summary>

**Self-hosted Zotero stack** — coordinating `zotero-dataserver` (PHP/MySQL), `zotero-web-library` (Node.js), and `zotero-connectors` is notoriously complex. The community-maintained `foxsen/zotero-selfhost` image was the proposed packaging path; it has since been removed from Docker Hub.

**Google Drive for storage** — directly syncing Zotero's SQLite database to Drive will corrupt it. Original integration route:

1. Self-host the Zotero data server for metadata sync.
2. Disable Zotero's built-in file synchronization.
3. Create an organizational Drive Shared Drive (`Cytognosis Literature`).
4. Use ZotMoov or ZotFile to rename attachments and route them into Drive.
5. Result: metadata via the self-hosted server, PDFs via Drive.

This was abandoned in favor of the simpler architecture above.

</details>

---

## 🕸️ 3. Neo4j Graph Database

**Community Edition (CE) vs. Enterprise Edition (EE)**

| Feature | Community Edition (CE) | Enterprise Edition (EE) |
| :--- | :--- | :--- |
| **Pricing** | Free (GPLv3) | Contact Sales (Tiered Licensing) |
| **Use Case** | Prototyping, Single-instances, Internal tools | Production, High Availability, Org-wide analytics |
| **Architecture** | Single Instance only | Causal Clustering (High Availability / Scale-out) |
| **Security** | Basic Authentication | RBAC, LDAP / Active Directory Integration, SSO |
| **Backups** | Offline only | Hot/Online Backups, Point-in-time recovery |
| **Performance** | Standard | Parallel graph runtimes, highly optimized queries |

**Recommendation:** If the application requires high-availability over multiple zones, or fine-grained Role-Based Access Control (RBAC) linked to your Google Workspace, the Enterprise Edition is required. For initial data science pipelines and single-point graph analytics, the Community Edition on an isolated, well-backed-up GCP instance is highly cost-effective.

---

## 📊 4. Mermaid.js Diagramming

If you want to host Mermaid diagram generation locally to keep documentation data private:

**Option A: Mermaid Live Editor (Self-Hosted IDE)**
- We can deploy the official `mermaid-live-editor` via a Docker container on Cloud Run or a VM. This provides an internal web interface (`mermaid.cytognosis.org`) where the team can collaboratively write and export diagrams in real-time.

**Option B: Headless Rendering Server (API)**
- For programmatic use (e.g., an internal tool that automatically generates flowcharts from data), we can deploy `mermaid-cli` or `mermaid-server` via a lightweight Docker container. This creates an internal API where you send it mermaid code and it returns an SVG or PNG image.

**Option C: Client-Side Rendering**
- If it's just for the website or internal documentation (like Markdown or HTML files), we don't need a standalone server. We simply embed the `mermaid.min.js` script, and user browsers render the diagrams automatically on page load. 

---

### Suggested Next Steps
1. **Cal.com:** Map `cal.cytognosis.org` to the external IP we provisioned and verify the PWA functionality on Android.
2. **Neo4j / Zotero:** Confirm which pieces you want to prioritize setting up in a dedicated Google Compute instance. Zotero requires substantial configuration time for the dataserver.
