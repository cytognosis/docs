# Sovereign Library Architecture: Zotero + Google Drive + Self-Hosted Annotation
## Setup Guide for Cytognosis Foundation

## Design Philosophy

All data lives on infrastructure we control. PDFs on our Google Drive. Metadata in local Zotero SQLite databases synced via Zotero's free metadata tier (no files on their servers). Annotations written directly into PDF files (ISO 32000 standard) and synced via Google Drive. Everything has an API that feeds into our future knowledge graph.

**What Zotero stores on their servers:** Only bibliographic metadata (titles, authors, DOIs, dates, tags, collections, notes). This is inherently public information. No PDFs, no files, no proprietary data. Free and unlimited.

**What lives on our infrastructure:**
- All PDFs → Google Drive `Library/Attachments/`
- All annotations → written into PDF files on Google Drive (ISO 32000 open standard)
- Full local database → `zotero.sqlite` on each member's machine
- Custom metadata (code/dataset/model links) → Zotero Extra field, synced as metadata
- Future knowledge graph → Neo4j on GCP (annotations extracted from PDFs via PyMuPDF)

**Cross-device workflow:** Annotations are embedded in the PDF file itself, so they sync everywhere Google Drive syncs — laptop, phone, tablet, web browser. Use any standard PDF reader on any device. No proprietary annotation layer needed.

---

## Architecture Overview

```
┌──────────────────────────────────────────────────────────────┐
│  GOOGLE DRIVE (Cytognosis Foundation Shared Drive)            │
│  Library/                                                     │
│  ├── Attachments/   ← canonical PDFs, browsable by everyone   │
│  ├── Intake/        ← new papers landing zone                 │
│  │   ├── Pending/                                             │
│  │   └── Review/                                              │
│  └── Supplementary/ ← code snapshots, datasets, figures       │
└──────────────────────────┬───────────────────────────────────┘
                           │ Linked URL attachments (free)
┌──────────────────────────▼───────────────────────────────────┐
│  ZOTERO GROUP LIBRARY (metadata-only sync, free tier)         │
│  ├── Bibliographic metadata (unlimited, free)                 │
│  ├── Collections (hierarchical organization)                  │
│  ├── Tags (flat cross-cutting labels)                         │
│  ├── Linked URLs → Google Drive PDF for each paper            │
│  ├── Extra field: drive-pdf, code, dataset, model links       │
│  ├── Notes (rich text, synced as metadata)                    │
│  └── NO stored file attachments (zero Zotero storage used)    │
│                                                               │
│  LOCAL: zotero.sqlite + storage/ on each machine              │
│  CHROME: Zotero Connector for one-click paper capture         │
│  GDOCS: Zotero plugin for citation insertion                  │
└──────────────────────────┬───────────────────────────────────┘
                           │
┌──────────────────────────▼───────────────────────────────────┐
│  SELF-HOSTED HYPOTHES.IS (collaborative annotation)           │
│  ├── Docker on GCP (or any infra you control)                 │
│  ├── Private Cytognosis annotation group                      │
│  ├── Annotates PDFs directly via Google Drive URLs             │
│  ├── Highlights, notes, replies, tags                         │
│  └── Data in YOUR PostgreSQL + Elasticsearch                  │
└──────────────────────────┬───────────────────────────────────┘
                           │ APIs feed into...
┌──────────────────────────▼───────────────────────────────────┐
│  FUTURE: KNOWLEDGE GRAPH (Neo4j on GCP)                       │
│  ├── Papers (Zotero API + OpenAlex enrichment)                │
│  ├── Authors, Institutions (OpenAlex, 100M+ authors)          │
│  ├── Code repos (GitHub API)                                  │
│  ├── Models (HuggingFace API)                                 │
│  ├── Datasets (internal registry + external APIs)             │
│  ├── Biological entities (Gene Ontology, Disease Ontology,    │
│  │   Cell Ontology, etc.)                                     │
│  ├── Annotations (Hypothes.is API)                            │
│  └── Typed, ontology-backed relationships                     │
└──────────────────────────────────────────────────────────────┘
```

---

## Part 1: Google Drive Folder Setup

### 1.1 Folder Structure

In the existing Cytognosis Foundation shared drive (`https://drive.google.com/drive/u/0/folders/0ABPuxniNx-iAUk9PVA`), within `Library/`:

```
Library/
├── Papers/           ← existing ReadCube PDFs (keep during migration)
├── Attachments/      ← new canonical folder for Zotero-managed PDFs
│   └── {Author}_{Year}_{ShortTitle}.pdf
├── Intake/
│   ├── Pending/      ← new papers awaiting triage
│   └── Review/       ← couldn't auto-identify (no DOI)
└── Supplementary/    ← code snapshots, datasets, supplementary figures
```

### 1.2 Install Google Drive for Desktop

Each member installs [Google Drive for Desktop](https://www.google.com/drive/download/) so the shared drive is accessible as a local folder.

- macOS: `/Volumes/GoogleDrive/Shared drives/Cytognosis Foundation/Library/`
- Windows: `G:\Shared drives\Cytognosis Foundation\Library\`

---

## Part 2: Zotero Group Library Setup (Admin)

### 2.1 Create the Zotero Group

1. Log in to [zotero.org](https://www.zotero.org) as the `cytognosis` account
2. Go to [zotero.org/groups](https://www.zotero.org/groups) → **Create a New Group**
3. Name: **Cytognosis Foundation**
4. Visibility: **Private**
5. Library Settings:
   - Library Reading: "Any group member"
   - Library Editing: "Any group member"
   - File Editing: "Any group member" (for linked URLs; actual PDFs live on Drive)

### 2.2 No Paid Storage Needed

Data sync (metadata, notes, tags, collections) is **free and unlimited** for group libraries. Since we store no file attachments in Zotero, we use zero storage. The free tier is all we need.

### 2.3 Get the API Key

For automation scripts:
1. Go to [zotero.org/settings/keys](https://www.zotero.org/settings/keys) (logged in as cytognosis)
2. Create a new key with read/write access to the group library
3. Note the group library ID (visible in URL on zotero.org group page)
4. Store in `.env` file, never commit to git

### 2.4 Invite Members

Invite team members by Zotero username or email. Set roles as Member or Admin.

---

## Part 3: Member Setup (Each Person)

### 3.1 Install Zotero Desktop

1. Download [Zotero 7](https://www.zotero.org/download)
2. Go to **Edit > Settings > Sync**
3. Enter your personal Zotero account credentials
4. Check "Sync automatically"
5. **Uncheck** "Sync attachment files in group libraries using Zotero" (we don't use Zotero storage)
6. Click Sync

The Cytognosis Foundation group library appears in the sidebar with all metadata, collections, and tags.

### 3.2 Install the Zotero Connector

Install from [zotero.org/download](https://www.zotero.org/download) for Chrome/Firefox/Edge/Safari.

**When saving a paper from the web:**
1. Navigate to a journal article page
2. Click the Zotero Connector icon
3. Select the Cytognosis Foundation group library as the destination
4. Zotero captures full metadata in one click
5. The PDF is NOT stored in Zotero — instead, our intake automation (Part 7) handles placing it on Google Drive and adding the linked URL

### 3.3 Install Google Drive for Desktop

See Part 1.2. Verify the Library folder is accessible locally.

---

## Part 4: Migrating from ReadCube Papers

### 4.1 Export Metadata

**Option A: RIS export**
In ReadCube, select all → right-click → Export > RIS (.ris)

**Option B: XLS cross-reference**
Use the existing XLS with all paper details to verify and fix metadata after import.

### 4.2 Prepare PDFs

PDFs are already in `Library/Papers/` on Google Drive. Copy them to `Library/Attachments/` with consistent naming: `AuthorYear_ShortTitle.pdf`.

### 4.3 Import Metadata into Zotero

1. Select the Cytognosis Foundation group library
2. File > Import > select the .ris file
3. Place imported items into the group library
4. Verify a sample of entries

### 4.4 Link PDFs to Google Drive (Programmatic)

After metadata import, run the Drive-Zotero Link Sync script (Part 7.2) to:
1. Match each Zotero item to its PDF in `Library/Attachments/`
2. Get the Google Drive file ID
3. Add a linked URL attachment: `https://drive.google.com/file/d/{ID}/view`
4. Add `drive-pdf:` to the Extra field

### 4.5 Rebuild Organization

Using the XLS:
- Recreate folder hierarchy as Zotero **Collections**
- Add **Tags** (lowercase, hyphenated: `single-cell`, `methods`, `cytognosis-core`)
- For 100+ papers, automate with pyzotero script

---

## Part 5: Custom Metadata Schema

### 5.1 Extra Field Convention

Each paper's Extra field stores structured key-value pairs (one per line):

```
drive-pdf: https://drive.google.com/file/d/ABC123/view
code-original: https://github.com/original-author/repo
code-internal: https://github.com/cytognosis/our-fork
dataset-original: https://zenodo.org/record/12345
dataset-internal: gs://cytognosis-data/datasets/name
model-original: https://huggingface.co/author/model
model-internal: https://huggingface.co/cytognosis/variant
hypothes-is-uri: https://hyp.cytognosis.org/a/ANNOTATION_ID
```

These are searchable in Zotero, accessible via the API, and sync to all members as metadata (free).

### 5.2 Tag Conventions

| Category | Tags |
|----------|------|
| Type | `review-paper`, `methods-paper`, `benchmark`, `preprint` |
| Topic | `single-cell`, `spatial-transcriptomics`, `causal-ai`, `biosensor` |
| Relevance | `cytognosis-core`, `background`, `competitor` |
| Status | `to-read`, `reading`, `read`, `annotated` |
| Resources | `has-code`, `has-data`, `has-model` |

### 5.3 Collection Structure

```
Cytognosis Foundation/
├── Core Technology/
│   ├── Biosensors/
│   ├── Causal AI/
│   ├── Edge Computing/
│   └── Disease Geometry/
├── Applications/
│   ├── Cancer Detection/
│   ├── Metabolic Disease/
│   └── Infectious Disease/
├── Methods/
│   ├── Single-Cell Analysis/
│   ├── Spatial Transcriptomics/
│   └── Deep Learning/
├── Background/
├── Grants & Proposals/
└── Intake/
```

---

## Part 6: Citing in Google Docs

### 6.1 Inserting Citations

1. Open Google Doc in Chrome (Zotero Connector installed, Zotero desktop running)
2. Click **Zotero > Add/Edit Citation**
3. Search by author, title, or year
4. Select paper from group library, press Enter
5. Citation appears in chosen style

### 6.2 Bibliography with Clickable Drive Links

Zotero's Google Docs plugin doesn't natively hyperlink citations to external URLs. We solve this with a Google Apps Script:

1. After finalizing citations, run the Cytognosis Bibliography Linker script
2. Script scans bibliography entries, extracts DOI/title
3. Queries Zotero API for matching item's `drive-pdf` Extra field value
4. Hyperlinks each bibliography entry to the Google Drive PDF

Any reader of the document can click a reference to open the PDF directly from Drive.

### 6.3 Collaborative Citing

All group library members can insert/edit citations in the same shared Google Doc. Each person's Zotero resolves citations from their local sync of the group library metadata.

---

## Part 7: Automation Scripts

### 7.1 Paper Intake Pipeline

**Purpose:** Automatically ingest new papers from local downloads.

**Flow:**
```
New PDF in ~/PaperIntake/ or ~/Downloads/
  → Extract DOI from PDF (pdfminer + regex)
  → Lookup metadata via CrossRef API
  → Check Zotero group library for existing DOI (pyzotero)
  → IF new:
      Copy PDF to Library/Intake/Pending/ on Google Drive
      Create Zotero item in "Intake" collection
      Add linked URL to Drive file
      Add drive-pdf to Extra field
  → IF exists: skip, notify
  → IF not a paper (no DOI): move to Library/Intake/Review/
```

**Deployment:** cron/launchd per laptop, or Cloud Function on Drive Intake folder.

**Dependencies:** `pyzotero`, `pdfminer.six`, `google-api-python-client`, `crossrefapi`

### 7.2 Drive-Zotero Link Sync

**Purpose:** Ensure every Zotero item has its Google Drive URL.

**Flow:**
```
For each item in Zotero group library:
  → Check if drive-pdf exists in Extra field
  → IF missing:
      Search Library/Attachments/ for matching PDF (by DOI, filename, title)
      Get Google Drive file ID
      Add linked URL attachment
      Update Extra field with drive-pdf URL
```

**Run:** Weekly cron or on-demand after bulk imports.

### 7.3 Bibliography Hyperlinker (Google Apps Script)

**Purpose:** Hyperlink bibliography entries in Google Docs to Drive PDFs.

**Flow:**
```
Scan active Google Doc for bibliography section
For each entry:
  → Extract DOI or author-year-title
  → Query Zotero API for matching item
  → Get drive-pdf from Extra field
  → Hyperlink the bibliography text to the Drive URL
```

**Deployment:** Bound script on a Google Docs template, or org-wide Apps Script add-on.

### 7.4 Zotero-to-Connector PDF Redirect

**Purpose:** When the Zotero Connector saves a paper, automatically route the PDF to Google Drive instead of Zotero storage.

**Flow:**
```
Zotero Connector saves paper → metadata goes to group library (free)
  → Connector also downloads the PDF locally
  → ZotMoov plugin watches for new attachments
  → Moves PDF from Zotero's local storage to Google Drive Library/Attachments/
  → Script converts stored attachment to linked URL pointing to Drive
```

**Note:** ZotMoov works for personal libraries. For group library items, we need a custom Zotero plugin or post-processing script.

---

## Part 8: Cross-Device Reading and Annotation

### 8.1 Core Principle: Annotations Live in the PDF

PDF annotations (highlights, comments, sticky notes, freehand drawings) are an ISO standard (ISO 32000). When you annotate a PDF, the annotations are embedded in the file itself — not in any proprietary database. Google Drive syncs the file. Therefore, annotations sync automatically across every device where you access Google Drive.

This is the most sovereign approach: your annotations are in an open standard format, in files you own, on infrastructure you control.

### 8.2 Recommended PDF Readers by Device

**Critical requirement:** The reader must write annotations into the PDF file (ISO 32000), not into its own proprietary database. This is what enables cross-device sync via Google Drive.

#### Free / Open-Source Options

| Device | Reader | License | Writes to PDF? | Notes |
|--------|--------|---------|----------------|-------|
| **Ubuntu/Linux** | **Okular** (KDE) | GPL | **Yes** | Best open-source PDF annotator. Highlights, notes, freehand, typewriter. Our top pick for Linux. |
| **Ubuntu/Linux** | **Xournal++** | GPL | **Yes** | Excellent for handwritten/freehand annotation with stylus. Also handles highlights and text. |
| **macOS** | Preview (built-in) | Proprietary (free) | **Yes** | Solid annotation. Works well for most needs. |
| **macOS** | **Skim** | BSD | **Yes** | Adds research features: notes panel, bookmarks, LaTeX integration, reading list. |
| **Windows** | **Drawboard PDF** (free tier) | Proprietary (free) | **Yes** | Rich annotation tools, pen/touch support. |
| **Android** | Google Drive (built-in) | Proprietary (free) | **Yes** | Basic pen/highlighter/eraser. Already there. |
| **Android** | **Xodo** (free tier) | Proprietary (free) | **Yes** | Richer annotation than Drive. Connects directly to Google Drive. |
| **Web** | **PdfDing** (self-hosted) | Open source | **Yes** | Deploy at `pdf.cytognosis.org`. Responsive mobile UI. |
| **Web** | **Hypothes.is** (self-hosted) | BSD | No (W3C Web Annotation DB) | Annotation overlay for threaded team discussion. Not a reader. |

**Warning — readers that do NOT write to PDF:**

| Reader | Where annotations go | Risk |
|--------|---------------------|------|
| **Sioyek** | Own SQLite database | Annotations invisible to other readers and don't sync via Drive. Great for reading/navigation (portals, smart search, reference jumping) but NOT for annotation in our architecture. Use Sioyek for reading, Okular for annotating. |
| **Zotero built-in reader** | `zotero.sqlite` local database | Same problem. Don't use Zotero's reader for annotation. |
| **Evince** (GNOME default) | Limited annotation support | Can read existing annotations but writing support is minimal and unreliable. |

#### Premium / Paid Options (One-Time Purchase)

For those who want a polished experience beyond what free tools offer:

| Reader | Platforms | Price | License | Writes to PDF? | Why Consider It |
|--------|-----------|-------|---------|----------------|-----------------|
| **Xodo PDF Studio Pro** | Linux, macOS, Windows | ~$240 perpetual | Proprietary | **Yes** | The only premium PDF editor with **native Linux support**. 60+ features: OCR, digital signatures, batch processing, side-by-side comparison, redaction. Java-based, runs identically on all three desktop OSes. 2-device license. |
| **Qoppa PDF Studio Pro** | Linux, macOS, Windows | ~$90-140 perpetual | Proprietary | **Yes** | Same company behind Xodo PDF Studio (Qoppa Software). Mature product, long track record on Linux. Previous generation — check if Xodo PDF Studio has superseded it. |
| **PDF Expert** | macOS, iOS | ~$80 perpetual | Proprietary | **Yes** | Beautifully designed, fast, excellent annotation UX on Mac/iPad. No Linux or Android. |
| **GoodReader** | iOS | ~$5 one-time | Proprietary | **Yes** | Best iOS PDF reader for annotation. Connects to Google Drive, annotates locally, syncs back. Cheap and polished. |
| **MuPDF** | Linux, macOS, Windows, Android | Free (AGPL) | AGPL | **Yes** | Extremely fast, lightweight. Full annotation toolbar (`a` key). Two Android viewers with different complexity levels. Not the prettiest UI but blazing performance. |

**Recommendation per budget:**

- **Free and sovereign:** Okular (Linux), Preview/Skim (macOS), Drawboard (Windows), Xodo free (Android), GoodReader (iOS, $5), PdfDing (web)
- **Premium desktop (one-time):** Xodo PDF Studio Pro ($240) — the only option that runs natively on Linux AND macOS AND Windows with identical features. Worth it if you switch between OSes or want OCR/batch/signatures.
- **Premium mobile:** GoodReader ($5 iOS) is a no-brainer. Android lacks good one-time-purchase options — the market has unfortunately shifted to subscriptions. Xodo free tier is the best Android option.

**Important:** Do NOT use Zotero's built-in PDF reader for annotation if you want cross-device sync. Zotero's reader stores annotations in its local database, not in the PDF file. Use Zotero for metadata/citations; use a standard PDF reader for annotation.

### 8.3 Self-Hosted Reading: PdfDing

PdfDing ([github.com/mrmn2/PdfDing](https://github.com/mrmn2/PdfDing)) is a lightweight self-hosted PDF manager, viewer, and editor. Deploy it as a Docker container on your existing server alongside cal.cytognosis.org and Mermaid.

**Features:** highlights, comments, drawings, PDF library management, responsive mobile UI, tag-based organization.

**Access:** `https://pdf.cytognosis.org` (or similar). Works in any browser on any device.

**Deployment:**
```bash
docker pull mrmn2/pdfding:latest
# Configure via docker-compose alongside your other services
```

**Use cases:**
- Quick web-based reading and annotation from any device
- Shared library browsable by all Cytognosis members
- Mobile reading via phone browser (responsive UI)

**Limitation:** PdfDing is a web app only — no native desktop or mobile app. For the best desktop reading experience, use Okular/Sioyek/Preview locally. For mobile, use Google Drive's built-in viewer or Xodo.

### 8.4 The Cross-Device Workflow

1. Paper is in `Library/Attachments/` on Google Drive
2. **On your Ubuntu laptop:** open the PDF from the local Google Drive folder in **Okular** (or Xodo PDF Studio Pro if you bought it). Highlight key findings, add margin notes. Save (Ctrl+S). Drive syncs within seconds. (Use **Sioyek** for reading/navigating papers with its portal and reference-jumping features, but switch to Okular when you want to annotate — Sioyek's annotations live in its own database and won't sync.)
3. **On the bus (Android):** open the Google Drive app, navigate to the same PDF. Your laptop's highlights are already there. Add a quick comment using Drive's built-in tools or Xodo. Save. Drive syncs.
4. **At a cafe (web):** open `pdf.cytognosis.org` (PdfDing) in your phone's browser, find the paper, annotate. Download back to Drive.
5. **A teammate at their desk:** opens the same PDF from Drive. Sees all annotations from steps 2-4. Adds their own.
6. **For team discussion:** open the Drive PDF URL with Hypothes.is overlay. Start a threaded conversation around a specific passage. Others reply. These annotations go to your PostgreSQL as W3C Web Annotation objects (see Part 10.3).
7. **Knowledge graph pipeline:** weekly PyMuPDF script extracts all in-PDF annotations (highlights, comments, coordinates, colors) from PDFs on Drive. Hypothes.is API exports all W3C Web Annotations. Both feed into Neo4j as Layer 1 and Layer 2 nodes respectively.

### 8.5 Handling Simultaneous Annotation

If two people annotate the same PDF at the exact same time, Google Drive will save one version and create a conflict copy of the other. For a 2-5 person team, this is rare and manageable:

- **Assign papers for deep annotation** (e.g., "Shahin reads and annotates Paper X this week")
- **Use Google Drive's version history** to recover annotations from conflict copies
- **If conflicts become frequent:** consider adding self-hosted Hypothes.is as a supplementary web-based annotation layer (see 8.7)

### 8.6 Extracting Annotations for Knowledge Graph

PyMuPDF (open source, Python) can programmatically extract all annotations from PDFs:

```python
import fitz  # PyMuPDF

doc = fitz.open("paper.pdf")
for page in doc:
    for annot in page.annots():
        print(f"Type: {annot.type}, Content: {annot.info['content']}")
        if annot.type[0] == 8:  # Highlight
            # Extract highlighted text
            quads = annot.vertices
            # ... extract text from coordinates
```

This extracts highlights, comments, sticky notes, and their coordinates — ready to feed into Neo4j as annotation nodes linked to paper nodes.

**Automation:** Run as a weekly cron job or Cloud Function that scans `Library/Attachments/` for recently modified PDFs and extracts new annotations.

### 8.7 Supplementary: Self-Hosted Hypothes.is (Optional, for Threaded Discussion)

If you need richer collaborative features (threaded replies, tagging, structured discussion around specific passages), deploy a self-hosted Hypothes.is instance:

```
Docker Compose stack (on GCP):
├── hypothesis/h          ← annotation server (Python/Pyramid)
├── hypothesis/client     ← web annotation client
├── hypothesis/via        ← PDF proxy for annotating remote PDFs
├── PostgreSQL            ← annotation storage (YOUR database)
├── Elasticsearch         ← search index
└── RabbitMQ              ← task queue
```

Hypothes.is is open source (BSD license), works in browsers via Chrome extension, and can annotate PDFs hosted on Google Drive URLs. It stores annotations in your own PostgreSQL — fully sovereign.

**Limitation:** Hypothes.is has no native mobile app. It works on tablets (7"+) via browser but is clunky on phones. Use it as a supplementary tool for web-based collaborative discussion, not as the primary annotation method.

### 8.8 Summary: What to Use Where

```
┌──────────────┬──────────────────────────┬────────────────────┬──────────┐
│ Device       │ Tool                     │ Annotations Stored │ License  │
├──────────────┼──────────────────────────┼────────────────────┼──────────┤
│ Ubuntu       │ Okular (free)            │ In PDF → Drive     │ GPL      │
│ Ubuntu       │ Xodo PDF Studio ($240)   │ In PDF → Drive     │ Prop.    │
│ Ubuntu       │ Sioyek (reading only!)   │ Own DB (no sync)   │ GPL      │
│ macOS        │ Preview / Skim           │ In PDF → Drive     │ Free/BSD │
│ macOS        │ PDF Expert (~$80)        │ In PDF → Drive     │ Prop.    │
│ Windows      │ Drawboard (free)         │ In PDF → Drive     │ Prop.    │
│ Windows      │ Xodo PDF Studio ($240)   │ In PDF → Drive     │ Prop.    │
│ Android      │ Drive / Xodo (free)      │ In PDF → Drive     │ Prop.    │
│ iOS          │ GoodReader (~$5)         │ In PDF → Drive     │ Prop.    │
│ Web (read)   │ PdfDing (self-hosted)    │ In PDF / server DB │ Open     │
│ Web (discuss)│ Hypothes.is (self-host)  │ Your PostgreSQL    │ BSD      │
│ Citations    │ Zotero                   │ Local zotero.sqlite│ AGPL     │
└──────────────┴──────────────────────────┴────────────────────┴──────────┘
```

### 8.9 What Connects It All

The key insight: **Google Drive is the sync layer, the PDF file is the annotation store.** No matter which reader you use on which device, as long as it writes standard PDF annotations (ISO 32000) and saves back to Drive, every other device sees those annotations instantly. This is the most sovereign, most universal, most future-proof approach — zero lock-in to any annotation service.

For the small gaps on iOS (no great open-source option) and Android (Xodo is free but proprietary): these are acceptable trade-offs. The annotations themselves are in an open standard format in files you own. The readers are just windows into your data — swap them anytime.

---

## Part 9: Reading Papers Locally

### 9.1 Opening Papers from Zotero

When you find a paper in Zotero and want to read it:

1. Double-click the **linked URL attachment** → opens the PDF from Google Drive in your browser
2. OR: Right-click → **Show File** to find it in the local Google Drive folder, then open in your preferred PDF reader

### 9.2 Recommended Workflow

- **Annotating (any device):** Open the PDF directly from Google Drive (local folder or app). Use a standard PDF reader. Annotations embed in the file, sync via Drive.
- **Finding a paper:** Use Zotero's search (Ctrl/Cmd+Shift+F) to find it by author/title/DOI, then click the Drive link.
- **Quick reference:** Open from the Google Drive folder or app directly — the `Library/Attachments/` folder is organized and browsable.

---

## Part 10: Future Knowledge Graph

### 10.1 Data Sources and APIs

| Source | API | What It Provides |
|--------|-----|-----------------|
| Zotero (our library) | pyzotero / Zotero Web API | Our curated papers, custom metadata, collections, tags |
| OpenAlex | REST API (free, no auth) | 474M+ works, 100M+ authors, institutions, funders, topics, citations |
| Semantic Scholar | REST API (free) | Paper embeddings, related papers, citation contexts |
| GitHub | REST/GraphQL API | Code repos linked to papers |
| HuggingFace | Hub API | Models linked to papers |
| Hypothes.is (ours) | REST API | Our team's annotations on papers |
| Gene Ontology | OBO/OWL files | Biological function ontology |
| Disease Ontology | OBO/OWL files | Disease classification |
| Cell Ontology | OBO/OWL files | Cell type classification |

### 10.2 Graph Schema (Neo4j)

```
(Paper)-[:AUTHORED_BY]->(Author)
(Paper)-[:PUBLISHED_IN]->(Journal)
(Paper)-[:CITES]->(Paper)
(Paper)-[:HAS_CODE]->(CodeRepo)
(Paper)-[:HAS_MODEL]->(MLModel)
(Paper)-[:HAS_DATASET]->(Dataset)
(Paper)-[:STUDIES]->(BiologicalEntity)
(Paper)-[:ANNOTATED_BY]->(Annotation)
(BiologicalEntity)-[:IS_A]->(BiologicalEntity)  // ontology hierarchy
(BiologicalEntity)-[:PART_OF]->(BiologicalEntity)
(Author)-[:AFFILIATED_WITH]->(Institution)
(CodeRepo)-[:FORK_OF]->(CodeRepo)
(MLModel)-[:FINE_TUNED_FROM]->(MLModel)
(Dataset)-[:DERIVED_FROM]->(Dataset)
```

### 10.3 W3C Web Annotation as the Personalization Layer

The knowledge graph holds **objective** information — papers exist, authors wrote them, code implements them. But research is also deeply **personal**: which passages matter to you, what you think about a finding, how you connect ideas across papers. This subjective layer needs its own standard.

**W3C Web Annotation Data Model** (the same standard Hypothes.is implements) is that standard. It can annotate any URI-addressable resource — not just web pages, but PDFs on Drive, GitHub repos, HuggingFace models, dataset records, even ontology terms. Each annotation is a JSON-LD object with a `target` (what you're annotating), a `body` (your note/highlight/tag), and a `creator`.

**Architecture: Two-Layer Knowledge Graph**

```
┌─────────────────────────────────────────────────────────┐
│  LAYER 1: OBJECTIVE KNOWLEDGE GRAPH (Neo4j / LinkML)    │
│                                                          │
│  Generic objects with canonical metadata:                │
│  • Papers (from Zotero API + OpenAlex)                   │
│  • Code repos (from GitHub API)                          │
│  • Models (from HuggingFace API)                         │
│  • Datasets (from internal registry + external APIs)     │
│  • Biological entities (from GO, DO, CL ontologies)      │
│  • Authors, Institutions, Journals                       │
│                                                          │
│  Schema: LinkML (our chosen KG standard)                 │
│  Storage: Neo4j Community Edition on GCP                 │
└────────────────────────┬────────────────────────────────┘
                         │ annotates ↓
┌────────────────────────▼────────────────────────────────┐
│  LAYER 2: PERSONALIZATION LAYER (W3C Web Annotation)     │
│                                                          │
│  Subjective annotations on ANY Layer 1 object:           │
│  • Highlights + margin notes on papers (PDF annotations) │
│  • Code review comments on repos                         │
│  • Model evaluation notes                                │
│  • Dataset quality assessments                           │
│  • Personal tags, ratings, reading status                │
│  • Cross-object connections ("this model implements      │
│    the method described in §3.2 of that paper")          │
│                                                          │
│  Standard: W3C Web Annotation Data Model (JSON-LD)       │
│  Storage: Self-hosted Hypothes.is PostgreSQL              │
│  Query: Hypothes.is API → Neo4j annotation nodes         │
└─────────────────────────────────────────────────────────┘
```

**Why this matters:**

- **Personal libraries become queries, not copies.** A "personal library" is just a filtered view of the KG: "all papers where creator=shahin AND motivation=bookmarking." No duplication.
- **Annotations are portable.** W3C Web Annotation is a W3C Recommendation (not a draft). JSON-LD serialization. Import/export trivially.
- **Any KG object is annotatable.** A W3C annotation can target a paper, a code repo, a model, a dataset, or an ontology term — all with the same schema. One annotation system for everything.
- **Team vs. personal is just a filter.** Annotations have creators. Show me all team annotations on this paper, or just mine.

**Example: Annotating a paper in the KG**

```json
{
  "@context": "http://www.w3.org/ns/anno.jsonld",
  "type": "Annotation",
  "creator": "https://cytognosis.org/team/shahin",
  "created": "2026-04-04T14:30:00Z",
  "motivation": "highlighting",
  "body": {
    "type": "TextualBody",
    "value": "Key finding: pairwise disease geometry outperforms single-marker approaches by 3.2x",
    "format": "text/plain"
  },
  "target": {
    "source": "https://drive.google.com/file/d/ABC123/view",
    "selector": {
      "type": "FragmentSelector",
      "value": "page=7&highlight=142,380,510,395"
    }
  }
}
```

**Example: Annotating a code repo**

```json
{
  "@context": "http://www.w3.org/ns/anno.jsonld",
  "type": "Annotation",
  "creator": "https://cytognosis.org/team/shahin",
  "motivation": "commenting",
  "body": {
    "type": "TextualBody",
    "value": "We should fork this — their causal discovery implementation is solid but needs adaptation for streaming biosensor data",
    "format": "text/plain"
  },
  "target": {
    "source": "https://github.com/original-author/causal-discovery",
    "selector": {
      "type": "FragmentSelector",
      "value": "path=/src/discovery.py&line=45-89"
    }
  }
}
```

**Integration with LinkML:**

LinkML is our schema standard for the objective KG. W3C Web Annotation doesn't replace LinkML — it sits alongside it. LinkML defines the structure of papers, code, models, datasets, and biological entities. W3C Web Annotation defines the structure of personal/team commentary on those objects. The `target.source` URI in each annotation points to a LinkML-defined entity in the KG.

If a LinkML schema for annotation already exists (or emerges), we can map W3C Web Annotation fields into it. But the W3C standard is mature, widely implemented, and already has a reference implementation (Hypothes.is) that we're deploying — so it's the pragmatic choice for now.

### 10.4 Implementation Path

1. **Now:** Set up Zotero + Google Drive + automation scripts (this guide)
2. **Next quarter:** Deploy self-hosted Hypothes.is on GCP
3. **After that:** Spin up Neo4j, build ingestion pipeline from Zotero API + OpenAlex
4. **Ongoing:** Extend graph with code/model/dataset nodes, biological ontologies
5. **Then:** Connect Hypothes.is annotations as Layer 2 personalization nodes in Neo4j
6. **Long-term:** GraphRAG interface for querying both layers with natural language

---

## Part 11: Zotero Plugin Trade-Offs (Metadata-Only Architecture)

### 11.1 What Breaks Without Stored PDFs

Because we store zero files on Zotero's servers, several Zotero plugins that expect local stored copies won't work:

| Plugin | What It Does | Works? | Why |
|--------|-------------|--------|-----|
| **ZotSeek** | AI-powered semantic search across paper contents | No | Needs indexed PDF text in Zotero storage |
| **Beaver** | AI chat with your papers | No | Needs PDF content accessible to Zotero |
| **PapersGPT** | Chat with papers via LLM | No | Same — expects stored PDFs |
| **Built-in full-text search** | Search inside PDF text | No | Full-text index built from stored attachments |
| **Auto-tagging plugins** | Tag papers by content analysis | No | Need PDF content |
| **Zotero PDF reader** | Built-in reader with annotation | Partially | Can open linked URLs, but annotations go to Zotero's DB, not the PDF |

### 11.2 What Still Works Perfectly

| Feature | Works? | Notes |
|---------|--------|-------|
| Metadata search (title, author, DOI, year) | Yes | This is what Zotero excels at |
| Collections and tags | Yes | Synced as metadata, free |
| Zotero Connector (Chrome) | Yes | One-click metadata capture |
| Google Docs citation plugin | Yes | Inserts citations from metadata |
| pyzotero API access | Yes | Full programmatic access to metadata |
| Extra field custom links | Yes | Our drive-pdf, code, dataset, model links |
| Notes (rich text) | Yes | Synced as metadata |
| Related items | Yes | Cross-reference papers |
| Zotero Better BibTeX | Yes | BibTeX/BibLaTeX export for LaTeX users |

### 11.3 Mitigation: Move Intelligence to Our Infrastructure

The plugins that break all do the same thing: analyze PDF content. Instead of giving Zotero our PDFs, we build these capabilities on our own stack:

| Lost Capability | Our Replacement | Where It Lives |
|----------------|----------------|----------------|
| Full-text search | **Elasticsearch** index over PDFs on Drive | GCP (alongside Hypothes.is) |
| AI chat with papers | **Our own RAG pipeline** (embeddings + LLM) | GCP — PDF text extracted by PyMuPDF, embedded, stored in vector DB |
| Auto-tagging | **OpenAlex topics + our own classifier** | Python script using OpenAlex API enrichment + optional fine-tuned model |
| Semantic search | **Semantic Scholar embeddings** + our index | Feed paper embeddings from S2 API into vector DB |
| Content-based discovery | **Knowledge graph queries** | Neo4j — "papers that cite the same methods" via citation graph |

This is the sovereignty trade-off: we lose convenience of drop-in Zotero plugins, but gain full control over how our papers are indexed, searched, and analyzed. The intelligence lives on our infrastructure, not in a desktop app.

### 11.4 Practical Timeline

- **Phase 1 (now):** Accept the gaps. Use Zotero for metadata/citations, Google Drive for PDFs, standard readers for annotation. Manual tagging via Zotero tags.
- **Phase 2 (with Hypothes.is):** Self-hosted annotation adds threaded discussion. Elasticsearch comes along for free (part of Hypothes.is stack).
- **Phase 3 (with Neo4j):** Knowledge graph enables content-based discovery without needing Zotero plugins.
- **Phase 4 (RAG pipeline):** AI chat with papers, semantic search, auto-tagging — all on our infra.

---

## Part 12: Cost Summary

| Item | Cost | Notes |
|------|------|-------|
| Zotero desktop + Connector | Free | Open source, all members |
| Zotero group library (metadata sync) | Free | Unlimited metadata, zero file storage |
| Google Drive | Included | Already part of Cytognosis Google Workspace |
| PDF readers (free tier) | Free | Okular, Xodo, Drawboard, Preview, PdfDing |
| PDF readers (premium, optional) | ~$240 once | Xodo PDF Studio Pro for Linux/Mac/Win; $5 GoodReader for iOS |
| Self-hosted Hypothes.is | ~$20-50/month | GCP Cloud Run or small Compute Engine instance |
| Self-hosted PdfDing | Negligible | Docker container alongside existing services |
| Neo4j Community Edition | Free | Open source, self-hosted |
| OpenAlex API | Free | No auth needed |
| **Total (free path)** | **~$20-50/month** | All data on your infrastructure |
| **Total (premium readers)** | **~$20-50/month + ~$250 once** | One-time cost for polished desktop + iOS readers |

---

## Part 13: Troubleshooting

**Metadata not syncing in group library:** Ensure "Sync automatically" is checked in Settings > Sync. Data sync is always free — no storage plan needed.

**PDF not found on Drive:** Verify the file exists in `Library/Attachments/` and the linked URL uses `https://drive.google.com/file/d/{FILE_ID}/view` format.

**Zotero menu missing in Google Docs:** Zotero desktop must be running. Check the Connector extension is enabled.

**Hypothes.is not loading on Drive PDF:** The Via proxy may be needed. Use `https://hyp.cytognosis.org/via/{DRIVE_URL}` format.

**Intake script not detecting DOI:** Some PDFs have DOIs only in the text body, not in metadata. The script falls back to text extraction with regex. If that fails, the PDF goes to `Intake/Review/` for manual triage.

---

## Appendix A: Why Not Other Tools?

### Paperpile
Best Google Docs integration, but proprietary. Library metadata stored on Paperpile's servers. No self-hosting. Shared libraries limited to individual Drive accounts. Fails the openness/sovereignty requirement.

### JabRef
Open source, local-first, BibTeX-native. But weak Google Docs integration, no native team sharing, LaTeX-focused. Good for individuals, not for an org using Google Workspace.

### Mendeley
Owned by Elsevier. Proprietary. Encrypts your local database. The antithesis of open science.

### Full self-hosted Zotero data server
Possible (zotero-selfhost, zotprime, dockerized-zotero projects exist). Would give full group library + file sync on your infra. But: community-maintained, requires patching Zotero client, significant maintenance burden. Worth revisiting if these projects mature, but not production-ready today for a small team.

### Custom build from scratch
Maximum flexibility, but building a Chrome extension matching Zotero Connector's breadth (thousands of journal sites) would take person-months. Not justified when Zotero's Connector is open source and works perfectly.
