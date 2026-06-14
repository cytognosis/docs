---
title: "Tana Outliner Deep Dive: Feature Analysis and Yar Mapping"
date: "2026-05-25"
source: "migrated from org/plans"
category: "product"
status: "current"
tags:
  - cytognosis
  - product
---

# Tana Outliner Deep Dive: Feature Analysis and Yar Mapping

> **Owner**: Shahin Mohammadi · **Created**: 2026-05-24 · **Status**: DRAFT
> **Canonical location**: `~/repos/cytognosis/org/plans/research/tana-outliner-deep-dive.md`
> **Purpose**: Exhaustive feature analysis of Tana Outliner for Cytonome/Yar feature prioritization

---

## Section Map

| # | Section | Purpose |
|---|---------|---------|
| 1 | [Executive Summary](#1-executive-summary) | Key takeaways for Yar |
| 2 | [Product Overview](#2-product-overview) | What Tana is, pricing, platforms |
| 3 | [Core Data Model](#3-core-data-model) | Nodes, outlining, workspaces |
| 4 | [Supertags System](#4-supertags-system) | Full specification of typed objects |
| 5 | [Automations and Templates](#5-automations-and-templates) | Command nodes, triggers, template bundles |
| 6 | [AI Features](#6-ai-features) | Models, meeting intelligence, voice, commands |
| 7 | [Live Searches and Dynamic Queries](#7-live-searches-and-dynamic-queries) | Query syntax, views, filtering |
| 8 | [Graph and Relationships](#8-graph-and-relationships) | Bidirectional references, backlinks, panels |
| 9 | [Import Export and API](#9-import-export-and-api) | Data portability, Input API, integrations |
| 10 | [UX and Navigation](#10-ux-and-navigation) | Keyboard shortcuts, panels, sidebar |
| 11 | [Comparative Analysis](#11-comparative-analysis) | Tana vs other tools |
| 12 | [Yar Feature Mapping](#12-yar-feature-mapping) | Every feature mapped to Yar equivalent |
| 13 | [Recommendations](#13-recommendations) | Priority features for Yar adoption |

---

## 1. Executive Summary

### Key Finding

Tana represents the most advanced implementation of a "programmable knowledge graph for individuals" available today. Its supertag system, which maps directly to our concept of "node types with schemas," demonstrates the viability and user demand for structured, typed objects within a flexible outliner interface. Tana's AI-native architecture, meeting intelligence, and command node automation system provide a proven reference architecture for Yar's design.

### Critical Insights for Yar

1. **Supertags = Node Types with Schemas**: Tana validates that users want and will adopt typed objects with defined fields, inheritance, and template content. This maps directly to Yar's object type system.
2. **Live Searches = Dynamic Retrieval**: Tana's search nodes (queries that are themselves nodes) prove that queries should be first-class objects in the system, composable and embeddable.
3. **AI-Native Design**: Tana's deep AI integration (meeting transcription, voice-to-structure, custom AI commands) shows the market expectation for AI that works *with* structured data, not just on raw text.
4. **Graph-First Architecture**: Everything-is-a-node with unique persistent IDs and bidirectional references validates Yar's planned graph model.
5. **Template Bundles**: Tana's composable template system (supertags + fields + commands + views packaged together) is a compelling model for Yar's extensibility story.

### Strategic Assessment

Tana is the closest existing product to Yar's vision. The key differentiator for Yar is the biomedical domain specificity, cellular intelligence integration, and health-context awareness that Tana's general-purpose architecture cannot provide. Yar should adopt Tana's proven UX patterns (supertags, live searches, command nodes) while layering on Cytognosis-specific intelligence.

---

## 2. Product Overview

### Company and History

- **Product**: Tana — AI-native, graph-based outliner and knowledge management workspace
- **Founded**: ~2022, by former engineers from Notion, Linear, and other productivity tools
- **Architecture**: Knowledge Graph where everything is a node
- **Philosophy**: "The Everything OS" — combines outliner flexibility with database structure

### Pricing

| Plan | Monthly | Annual (per month) | Key Focus |
|:-----|:--------|:-------------------|:----------|
| **Free** | $0 | $0 | Casual use and evaluation |
| **Plus** | $10 | $8 | Busy individuals and meeting management |
| **Pro** | $18 | $14 | Power users, teams, and automation |

#### Free Tier Limitations

- **Supertags**: Capped at 5 custom supertags (the most significant restriction)
- **Workspaces**: Limited to 2 workspaces
- **AI Credits**: 500 credits/month (chat, voice transcription, image generation)
- **Integrations**: No Google Calendar sync or advanced automation
- **Storage**: 0.5 GB for uploaded files

#### Plus Plan ($10/mo or $8/mo annual)

- AI Credits: ~2,000/month
- Integrations: Google Calendar sync, Readwise integration
- Unlimited supertags and workspaces
- Command nodes with event triggers
- Password protection on shared pages

#### Pro Plan ($18/mo or $14/mo annual)

- AI Credits: ~5,000/month
- Input API access
- Model selection in AI chat (GPT, Claude, Gemini)
- Publishing templates
- Unlimited file storage and upload size

#### Discounts

- Student and NGO discounts: 50% off
- Free trial available for full-featured version

### Platforms

- **Desktop**: Mac, Windows, Linux (with offline support)
- **Mobile**: iOS, Android (native apps with full editing, voice capture, AI workflows)
- **Web**: Browser-based access

---

## 3. Core Data Model

### Everything is a Node

The fundamental building block in Tana is the "node." There are no traditional folders or files; instead, all information exists as nodes that can be nested, referenced, and structured.

- Every node has a **unique persistent Node ID** assigned upon creation
- Nodes can be **nested infinitely** (outliner model)
- A node's Node ID is visible in the URL bar when zoomed in, or via the "Copy link" command
- Editing a reference edits the original node (they share the same Node ID)

### System Fields

Tana automatically tracks metadata for every node via system fields:

| System Field | Description |
|:-------------|:------------|
| **Created Time** | Automatically recorded at node creation |
| **Last Modified Time** | Tracks when the node was last updated |
| **Last Modified By** | Records the user who made the last change |
| **Owner** | The "home" location or parent node in the outline hierarchy |
| **Tags** | Applied supertags |
| **Workspace** | Which workspace the node belongs to |
| **Number of References** | Count of references/backlinks |

System fields are used as Display or Sort options within views (tables, lists, cards) or as parameters in Live Searches for filtering and organizing data.

### Outlining

Tana is a full-featured outliner with:

- **Indent/Outdent**: Tab / Shift+Tab
- **Expand/Collapse**: Cmd+↓ / Cmd+↑
- **Move nodes**: Cmd+Shift+↑/↓
- **Zoom into any node**: Cmd+. to zoom in, Cmd+, to zoom out
- **Quick Add**: Cmd+Shift+Space captures to daily notes without context switching
- **Insert Node**: Shift+Enter

### Workspaces

Workspaces act as independent containers for projects or different areas of life:

- Each workspace includes its own settings, schema, library, and trash
- Collaboration: Add members, view edit histories, notify users about specific nodes
- Publishing: Workspaces can be published as read-only via web link

---

## 4. Supertags System

### Overview

Supertags are the core primitive that transforms Tana from a simple outliner into a programmable knowledge graph. They act as schemas (or classes) that transform nodes into structured objects.

### How Supertags Work

When you apply a supertag to a node, you are essentially assigning it a class, which gives that node specific attributes defined as fields.

- **Applying a supertag**: Type `#` followed by the tag name on any node
- **Multiple supertags**: A single node can have multiple supertags applied simultaneously
- **Default content**: Define template sub-nodes or fields that automatically appear when the tag is applied
- **Base types**: Assign a "Base" type (Task, Person, Meeting) to help Tana's AI understand the core nature of the object and unlock specific behaviors or optimized UI views

### Field Types

Fields are metadata attached to nodes, following the "has-a" relationship (e.g., a *Book* "has-an" *Author*).

| Field Type | Description |
|:-----------|:------------|
| **Plain** | Any text/information |
| **Options** | Fixed dropdown selections |
| **Options from Supertag** | Dynamic dropdown populated by all instances of a specific supertag |
| **Date** | Date picker |
| **Number** | Numeric value |
| **URL** | Web link |
| **Email** | Email address |
| **Checkbox** | Boolean true/false |

### Adding Fields

- Type `>` followed by the field name to add a field to a node
- Use "Configure field" command to change a field's data type
- Fields can be marked as required or optional

### Inheritance: The "Extend" Feature

Tana's Extend feature functions like inheritance in object-oriented programming:

- When Supertag B "extends" Supertag A, it inherits all fields and template content from Supertag A
- Creates taxonomic hierarchies (e.g., `#Bug` extends `#Task`, inheriting Status, Due Date, Assignee, while adding Severity, Reproduction Steps)
- Reduces schema duplication across related types
- Changes to the parent supertag propagate to extending supertags

### Supertag Composition

A node can have multiple supertags applied, enabling composition:

- Apply `#Meeting` and `#Project-Update` to get fields from both
- Unlike inheritance (vertical), composition is horizontal — mix and match behaviors
- Conflicts resolved by the order of tag application

### Built-in vs User-Created Supertags

- **Built-in**: Task (with checkbox, status, progress), Person, Meeting, and other base types
- **User-created**: Unlimited custom supertags (on paid plans; 5 on free tier)
- Template bundles from the Tana Template Store provide pre-configured supertags for common workflows

### Mapping to Yar

| Tana Concept | Yar Equivalent |
|:-------------|:---------------|
| Supertag | Node Type / Object Schema |
| Field | Property / Attribute |
| Extend | Schema Inheritance |
| Multiple supertags | Multi-type composition |
| Default content | Template instantiation |
| Base types | Core type categories |
| Options from Supertag | Dynamic enum from type instances |

---

## 5. Automations and Templates

### Command Nodes

Command nodes are Tana's automation primitive. They package AI prompts, API requests, and field manipulations into reusable, triggerable actions.

#### Creating a Command Node

1. Create an empty node and type its name (e.g., "Send to Make")
2. Select the node and use `Cmd/Ctrl + K` to run "Convert to command node"
3. Add child nodes with specific commands (`@Make API request`, AI prompts, etc.)
4. Attach to a supertag as a button via the "AI and Commands" configuration panel

#### Available Command Types

- **AI Commands**: Custom prompts that process node content through LLMs
- **Make API Request**: Send HTTP requests to external services
- **Set Field Values**: Programmatically update field values
- **Compound Commands**: Chain multiple commands together

### Make API Request (Outgoing Webhooks)

Since Tana lacks native webhooks, the "Make API request" command serves as the outgoing integration mechanism:

- **URL**: Webhook URL from automation platform (Make.com, Zapier, n8n)
- **Method**: POST
- **Payload**: JSON with Prompt Expressions for dynamic data: `{"name": "${name}", "due_date": "${due date}"}`
- **Parse result**: Can disregard response or process it back into Tana

### Prompt Expressions

Dynamic data insertion into command payloads:

- `${name}` — Node name/title
- `${sys:nodeId}` — Unique node identifier
- `${field label}` — Value of a specific field
- Prompt Workbench available for testing payload structure

### Event-Based Automation

While Tana lacks native event-triggered webhooks, automation is achievable through:

- **Supertag Event Automation**: Map commands to specific states (e.g., "Done" checkbox triggers API request)
- **Command Buttons**: One-click execution attached to supertags
- **Compact/Full Command Menus**: Organize multiple buttons cleanly on supertags

### Template Bundles

Template bundles are pre-configured systems consisting of supertags, fields, commands, and views:

- **What they are**: "Live, composable" systems — not static templates but actual configuration copied into your workspace
- **Built-in Library**: Official Template Store accessible via "Browse templates" in the Supertags sidebar
- **Installation**: Copies building blocks into your workspace; no active connection to the original (updates don't auto-push)

#### Available Template Workflows

| Template | Contents |
|:---------|:---------|
| **Simple Projects** | Project supertag, task tracking, Kanban view |
| **Goals That Stick (OKRs)** | Objectives, Key Results, linked tasks, hierarchy |
| **Meeting to Comms** | Meeting supertag, attendees, action items, AI extraction |
| **Habit Tracking** | Habit supertag, streak tracking, daily check-ins |
| **AI-Enabled Tasks** | Task automation with AI classification and routing |

#### Publishing Custom Templates

1. Build workflow in a dedicated shared workspace
2. Use `publish template` command to generate preview and public link
3. Anyone with the link can install the template bundle into their workspace

#### Templates vs Published Pages

- **Templates** share *workflows and structures* (supertags, fields, commands)
- **Tana Publish (Page)** shares *content* (meeting notes, research) as clean web documents

### Implementing Specific Workflows

| Workflow | Implementation |
|:---------|:---------------|
| **Meetings** | `#Meeting` supertag with attendees, date, linked projects. AI agent transcribes and extracts action items. |
| **Projects** | `#Project` supertag as hub. Link tasks and meetings; they auto-appear in project views. |
| **Kanban** | Live search for tasks with status field, switched to Kanban/Card view mode. |
| **OKRs** | Template bundle linking Objectives → Key Results → Tasks in hierarchy. |
| **Sprints** | Nodes representing sprint cycles with date-range queries to aggregate tasks. |

---

## 6. AI Features

### Overview

Tana has evolved into an AI-native workspace where voice, meeting intelligence, and custom AI commands are deeply integrated into the knowledge graph architecture.

### Multi-Model Support

Tana provides access to leading LLMs:

- **OpenAI GPT series** (GPT-4, etc.)
- **Anthropic Claude**
- **Google Gemini**
- Paid plans include monthly AI credits
- Model selection available on Pro plan
- Configurable reasoning levels

### Meeting Intelligence

Tana offers a "botless" meeting experience:

#### Botless Transcription

- Record and transcribe system audio directly via the Tana Desktop app
- Captures your voice and others' voices (video calls, in-person) without a meeting bot
- No third-party bot joins your calls

#### Calendar Integration

- Google Calendar integration surfaces meetings automatically
- Desktop notifications to start transcribing with a single click
- Meetings imported into daily notes and linked to contacts, projects, tasks

#### Post-Meeting AI Processing

- **Automatic summaries**: AI generates meeting summaries from transcripts
- **Action item extraction**: Tasks automatically tagged and routed to task system
- **AI Chat on meetings**: Ask questions about specific discussions, decisions, or context weeks or months later

### Voice Filing and Capture

#### Mobile Voice Memos

- Record voice memos on iOS and Android
- Transcribed and automatically structured into knowledge graph based on applied supertags
- Voice notes transformed into formatted agendas, tasks, or blog posts

#### Voice Chat

- Early access feature on mobile
- Conversational, two-way interaction with your data via voice
- Voice-to-structure via supertags and fields

### Custom AI Commands

- Create reusable AI command buttons attached to supertags
- Single-click transform: raw transcript → project plan, email, task list
- Attached to supertags via "AI and Commands" configuration
- Prompt Workbench for testing and refining prompts

### Integrated AI Chat

- Press Space bar below any note to engage in AI chat
- Chat references the current note as context
- Generate content, brainstorm, review information without leaving flow
- Combined with web search for context-aware assistance

### Image Generation

- Integrated image generation (Nano Banana Pro)
- Turn notes or ideas into diagrams, infographics, or banners within workspace

### Key 2024-2025 AI Enhancements

- **Offline support**: Desktop app works without internet
- **Improved mobile**: Full editing, voice capture, AI workflows on mobile
- **Fine-tuned reasoning**: Configurable reasoning levels, model + web search combination
- **AI credits system**: Tiered allocation across Free/Plus/Pro plans

---

## 7. Live Searches and Dynamic Queries

### Overview

Tana's live search (search nodes) dynamically query and visualize data across the workspace. Because search nodes are themselves nodes, they can be embedded, referenced, and composed like any other node.

### Creating Live Searches

| Method | How |
|:-------|:----|
| **Command Palette** | `Cmd/Ctrl + K` → "Find nodes..." with step-by-step prompts |
| **Keyboard Shortcut** | Type `?` on an empty node → "Create search node" |
| **Query Builder** | Click "Edit query" to add conditions with logical operators |

### Query Syntax and Logic

#### Conditions

- Search by **tag**: `#book`, `#task`, `#meeting`
- Search by **field existence**: nodes containing a specific field (e.g., `Author`)
- Search by **field value**: `Status == "Reading"`, `Priority == "High"`
- Search by **text match**: exact text within node content
- Search by **date**: `CREATED/EDITED LAST X DAYS`

#### Logical Operators

- **AND** (default): All conditions must match
- **OR**: Any condition matches
- **NOT**: Exclude matching nodes

#### Dynamic References

- `PARENT`: Items related to the parent node of the search
- `GRANDPARENT`: Items related to the grandparent node
- Use case: Finding discussion items for a meeting attendee

### Views

Search results can be rendered in multiple view modes:

| View | Description |
|:-----|:------------|
| **List** | Simple vertical list of matching nodes |
| **Table** | Spreadsheet-like with columns for each field |
| **Kanban/Card** | Cards grouped by a field (e.g., Status) |
| **Calendar** | Items plotted on calendar by date field |
| **Tabs** | Grouped results in switchable tabs |

### Sorting and Grouping

- **Sort by**: Any field (Date, Name, Created, Modified, custom fields)
- **Group by**: Any field to create sections (e.g., group tasks by Project)
- **Filter within views**: Further narrow results after initial query

### Search Nodes as First-Class Objects

- Search nodes can be embedded anywhere in the outline
- They update dynamically as data changes
- Can be nested within supertag default content for auto-populated views
- Shareable and publishable like any other node

---

## 8. Graph and Relationships

### Knowledge Graph Architecture

Tana functions as a massive, interconnected knowledge graph:

- Every node has a unique identifier enabling deep bidirectional relationships
- No traditional hierarchy constraints — nodes can be referenced from anywhere
- The graph model supports non-linear thinking and discovery

### Bidirectional References

#### Creating References

- **@-Mentions**: Type `@` followed by node name to create a reference/inline link
- **Copy/Paste**: Copy a node (Cmd+C) and paste (Cmd+V) as a reference
- References are mirrors: editing a reference edits the original (shared Node ID)

#### Automatic Backlinks

- Creating an @-mention automatically generates a backlink on the target node
- All references tracked and surfaced in the Reference Panel

### References (Mirrors)

- Multiple "mirrored" copies of a single node can exist in different locations
- All mirrors share the same Node ID
- Changes propagate instantly across all instances
- Distinct from duplicates (which create separate nodes)

### Reference Panel (Backlinks)

Every node has a reference section showing:

- All locations where the node has been linked via @-mentions
- **Unlinked mentions**: System identifies plain-text appearances of the node's name elsewhere, offering to link them formally
- Grouped by source context for easy navigation

### Graph Navigation

- Zoom into any node to explore its subgraph
- Reference panel at the bottom of each node
- Side panels for viewing connected nodes alongside current focus
- Command line search across entire graph

### Summary: Graph Concepts

| Feature | Description |
|:--------|:------------|
| **Node** | The fundamental, atomic unit of information |
| **Unique ID** | Persistent identifier for every node, essential for linking |
| **System Fields** | Automatic metadata (Created, Modified, Owner) for sorting/filtering |
| **References** | Mirrored instances of a node; updating one updates all |
| **Backlinks** | Auto-generated references showing where a node is linked |
| **Unlinked Mentions** | Plain-text occurrences suggested for formal linking |

---

## 9. Import Export and API

### Export Options

Tana has addressed data lock-in concerns with robust export:

| Format | Description |
|:-------|:------------|
| **Markdown** | Export workspaces or selected nodes as .zip of human-readable .md files. Preserves links and references. |
| **JSON** | Full Tana-specific metadata and structural information. For technical use cases. |
| **Selective Export** | Download specific subsets: items with a particular supertag, or search query results. |

### Input API

The Tana Input API is the primary method for programmatically adding data:

- **Endpoint**: `https://europe-west1-tagr-prod.cloudfunctions.net/addToNodeV2`
- **Method**: POST
- **Authentication**: Tana API Token (generated in Settings → API Tokens)
- **Availability**: Pro plan only

#### API Capabilities

- **Node Creation**: Create simple nodes, nested hierarchies, structured data
- **Supertags and Fields**: Define new supertags, create fields, apply existing supertags using nodeID
- **File Uploads**: Upload files and associate with specific nodes

#### Working with Node IDs

- Every object (nodes, supertags, fields) has a nodeID
- Retrieve via "Copy link" command (ID is the part after `nodeid=`)
- Or use "Show API schema" command on a supertag config

#### API Schema

- View required JSON structure by running "Show API schema" on a supertag
- GitHub samples: [tanainc/tana-input-api-samples](https://github.com/tanainc/tana-input-api-samples)

### Webhooks and Read Access

- **No native webhooks**: Tana does not provide native webhook endpoints for triggering external actions
- **Outgoing workaround**: "Make API request" command within Command Nodes sends data to external services
- **Community tools**: `tana-helper`, `supertag-cli` bridge gaps via Tana's Local API (Desktop)
- **No public read API**: No official API for reading data from Tana (Local API on Desktop offers expanded capabilities)

### Integration Ecosystem

| Integration | Type | Description |
|:------------|:-----|:------------|
| **Google Calendar** | Native | Auto-import meetings into daily notes |
| **Readwise** | Native | Sync highlights and annotations |
| **Make.com / Zapier / n8n** | API | Via Make API Request command node |
| **Tana Capture (Chrome)** | Extension | Clip web content into Tana |
| **tana-helper** | Community | Webhook bridge and processing |
| **supertag-cli** | Community | CLI for Tana's Local API |

---

## 10. UX and Navigation

### Navigation and Interface

#### Tabs

- Native tab support in Tana Desktop
- **Open in new tab**: Cmd/Ctrl + Click (on node) or Cmd/Ctrl + T
- **Switch tabs**: Ctrl + Tab
- **Close tab**: Cmd/Ctrl + W

#### Panels

- View nodes side-by-side
- **Open in new panel**: Shift + Click on a node
- Panels open to the right, resizable and independently scrollable

#### Sidebar

- Quick access to Today (daily notes), Pinned items, Supertags, Workspaces
- Toggle visibility: full, mini, or collapsed
- Pin any node via right-click

#### Zooming

- **Zoom in**: Cmd/Ctrl + . (period) on a node bullet
- **Zoom out**: Cmd/Ctrl + , (comma)

### Keyboard Shortcuts

| Action | Shortcut |
|:-------|:---------|
| **Command Line** | Cmd/Ctrl + K |
| **Quick Add** | Cmd/Ctrl + Shift + Space |
| **Move Node Up/Down** | Cmd/Ctrl + Shift + ↑/↓ |
| **Indent/Outdent** | Tab / Shift + Tab |
| **Expand/Collapse** | Cmd/Ctrl + ↓/↑ |
| **Insert Node** | Shift + Enter |
| **Zoom In** | Cmd/Ctrl + . |
| **Zoom Out** | Cmd/Ctrl + , |
| **Open in New Tab** | Cmd/Ctrl + Click |
| **Open in New Panel** | Shift + Click |
| **Custom Shortcut** | Cmd/Ctrl + Shift + K (to assign) |

### Slash Commands and Block Types

- Type `/` to trigger creation menu (fields, supertags, structures)
- Type `>` followed by field name to add fields
- Type `#` to apply supertags
- Type `@` to create references
- Type `?` to create search nodes

### Command Menus

- Compact and Full command menus on supertags
- Organize AI and automation buttons cleanly
- Reduce visual clutter on nodes

---

## 11. Comparative Analysis

### Tana vs Capacities

| Feature | Tana | Capacities |
|:--------|:-----|:-----------|
| **Primary Paradigm** | Outliner-based (nested nodes) | Object-based (type-specific containers) |
| **Data Model** | Knowledge Graph (Nodes/Edges) | Relational/Graph-like (Postgres backend) |
| **Automation** | High (commands, AI fields, workflows) | Moderate (growing, less programmatic) |
| **Accessibility** | Steeper learning curve | More intuitive, "out of the box" |
| **Mobile/Offline** | Desktop-first, growing mobile | Stronger mobile/cross-platform focus |
| **Integrations** | Advanced, focus on data manipulation | Strong ecosystem (Readwise, Raycast) |
| **AI** | Deep, multi-model, custom commands | Contextual assistant, property autofill |
| **Collaboration** | Basic (workspace sharing) | Primarily single-user PKM |
| **Structure** | Opt-in, retroactive | Upfront, guided |

### Tana vs Notion

| Feature | Tana | Notion |
|:--------|:-----|:-------|
| **Data Model** | Graph (nodes) | Relational (databases + pages) |
| **AI** | Deep, multi-model | AI-assisted writing/search |
| **Flexibility** | Higher (everything is a node) | More structured |
| **Collaboration** | Basic | Advanced (real-time, permissions) |
| **Learning Curve** | Steep | Moderate |
| **Templates** | Composable bundles | Static templates |

### Tana vs Obsidian

| Feature | Tana | Obsidian |
|:--------|:-----|:---------|
| **Storage** | Cloud-first | Local-first (markdown files) |
| **Data Model** | Knowledge graph | File-based with links |
| **Plugins** | Template bundles | Extensive plugin ecosystem |
| **AI** | Native, deep | Via plugins |
| **Offline** | Desktop app | Native (local files) |
| **Extensibility** | Command nodes + API | Community plugins |

---

## 12. Yar Feature Mapping

### Core Data Model

| Tana Feature | Existing Yar Equivalent | Required Yar Implementation | Priority |
|:-------------|:------------------------|:----------------------------|:---------|
| Everything-is-a-node | Partial (object model) | Unified node model with persistent IDs | P0 |
| Unique Node IDs | Planned | UUID/ULID generation for all objects | P0 |
| System fields (Created, Modified, Owner) | Partial | Auto-tracked metadata on all objects | P0 |
| Infinite nesting (outliner) | Not present | Hierarchical node structure with indent/outdent | P1 |
| Workspaces | Not present | Workspace containers with independent settings | P1 |
| Daily notes | Not present | Calendar-linked entry point nodes | P1 |

### Supertags System

| Tana Feature | Existing Yar Equivalent | Required Yar Implementation | Priority |
|:-------------|:------------------------|:----------------------------|:---------|
| Supertags (typed objects) | Planned (node types) | Schema-based node types with field definitions | P0 |
| Field types (plain, date, number, URL, etc.) | Not present | Property type system with validation | P0 |
| Options from Supertag (dynamic enums) | Not present | Dynamic option lists from type instances | P1 |
| Extend (inheritance) | Not present | Schema inheritance with field propagation | P1 |
| Multiple supertags (composition) | Not present | Multi-type composition on single object | P1 |
| Default content (templates) | Not present | Template instantiation on type application | P1 |
| Base types (Task, Person, Meeting) | Not present | Core type categories with specialized behavior | P1 |

### Automations and Templates

| Tana Feature | Existing Yar Equivalent | Required Yar Implementation | Priority |
|:-------------|:------------------------|:----------------------------|:---------|
| Command nodes | Not present | Programmable action nodes | P1 |
| Make API Request | Not present | HTTP request action type | P2 |
| Custom AI commands | Not present | LLM prompt + context execution pipeline | P1 |
| Template bundles | Not present | Composable workflow packages (supertags + fields + views) | P2 |
| Event-based automation | Not present | Trigger system (on field change, on creation, etc.) | P2 |
| Prompt expressions | Not present | Dynamic variable injection in command payloads | P2 |

### AI Features

| Tana Feature | Existing Yar Equivalent | Required Yar Implementation | Priority |
|:-------------|:------------------------|:----------------------------|:---------|
| Multi-model LLM support | Not present | Pluggable LLM backend (GPT, Claude, Gemini) | P1 |
| Meeting transcription | Not present | Audio capture + transcription pipeline | P2 |
| Post-meeting AI processing | Not present | Transcript → summary + action items extraction | P2 |
| Voice-to-structure | Not present | Voice input → typed object creation | P2 |
| AI Chat on nodes | Not present | Contextual AI chat referencing node + subgraph | P1 |
| Image generation | Not present | Optional, low priority | P2 |

### Live Searches and Dynamic Queries

| Tana Feature | Existing Yar Equivalent | Required Yar Implementation | Priority |
|:-------------|:------------------------|:----------------------------|:---------|
| Search nodes (queries as objects) | Not present | Query objects with persistent storage | P0 |
| Query builder (tag, field, value filters) | Not present | Visual query builder with conditions | P0 |
| AND/OR/NOT logic | Not present | Logical operators in query system | P0 |
| Dynamic references (PARENT, GRANDPARENT) | Not present | Relative context references in queries | P1 |
| Multiple views (List, Table, Kanban, Calendar) | Not present | Multi-view rendering for query results | P0 |
| Group by / Sort by | Not present | Aggregation and ordering controls | P1 |
| Date-based filtering | Not present | Temporal query conditions | P1 |

### Graph and Relationships

| Tana Feature | Existing Yar Equivalent | Required Yar Implementation | Priority |
|:-------------|:------------------------|:----------------------------|:---------|
| Bidirectional references | Planned | Auto-backlink generation on @-mention | P0 |
| @-mentions (inline references) | Not present | Inline linking syntax with autocomplete | P0 |
| Reference panel (backlinks) | Not present | Backlink display section on every object | P0 |
| Unlinked mentions | Not present | Text-match detection for potential links | P2 |
| Mirrors (multi-location references) | Not present | Same-object references across hierarchy | P1 |

### Import Export and API

| Tana Feature | Existing Yar Equivalent | Required Yar Implementation | Priority |
|:-------------|:------------------------|:----------------------------|:---------|
| Markdown export | Not present | Export to .md with link preservation | P1 |
| JSON export | Not present | Full metadata export in JSON | P1 |
| Input API (write) | Not present | REST API for node/type creation | P1 |
| Selective export (by tag/search) | Not present | Filtered export by type or query | P2 |
| Google Calendar integration | Not present | Calendar sync (read/write) | P2 |

### UX and Navigation

| Tana Feature | Existing Yar Equivalent | Required Yar Implementation | Priority |
|:-------------|:------------------------|:----------------------------|:---------|
| Command palette (Cmd+K) | Not present | Universal command palette | P0 |
| Keyboard-first navigation | Not present | Comprehensive keyboard shortcut system | P0 |
| Tab interface | Not present | Multi-tab node browsing | P1 |
| Side panels | Not present | Side-by-side node viewing | P1 |
| Sidebar (Today, Pinned, Tags) | Not present | Navigation sidebar with sections | P0 |
| Quick Add capture | Not present | Global capture shortcut to inbox/daily | P1 |
| Slash commands | Not present | `/` menu for inline content creation | P0 |

---

## 13. Recommendations

### P0 Features (Must Have for Yar MVP)

1. **Unified node model with persistent IDs** — Foundation of everything
2. **Schema-based node types** (equivalent to supertags) — Core differentiator
3. **Property type system** — Text, Date, Number, URL, Checkbox, Options
4. **Query objects with visual builder** — Queries as first-class citizens
5. **Multi-view rendering** — List, Table, Kanban, Calendar views
6. **Bidirectional references with backlinks** — Graph relationships
7. **Command palette and keyboard shortcuts** — Power user UX
8. **Navigation sidebar** — Today, Pinned, Types, Search
9. **Slash commands** — Inline content creation menu

### P1 Features (High Priority)

1. **Schema inheritance** (Extend)
2. **AI Chat on nodes** with pluggable LLM backends
3. **Custom AI commands** (prompt + context execution)
4. **Dynamic option lists** from type instances
5. **Template instantiation** on type application
6. **Markdown/JSON export**
7. **REST API** for programmatic access
8. **Multi-tab interface** and **side panels**
9. **Quick capture** to inbox/daily notes
10. **Group by / Sort by** controls on views

### P2 Features (Future)

1. **Meeting transcription and intelligence**
2. **Voice-to-structure** capture
3. **Template bundles** (composable workflow packages)
4. **Event-based automation** triggers
5. **HTTP request action** nodes
6. **Unlinked mention detection**
7. **Calendar integration**
8. **Image generation**
9. **Publishing** (read-only web views)

### Key Design Decisions for Yar

1. **Adopt the "everything is a node" model**: Tana validates this approach. Every object, query, view, and template should be a node in Yar's graph.
2. **Make queries first-class objects**: Tana's search nodes that are themselves nodes is elegant and powerful. Yar should adopt this pattern.
3. **Schema system should support inheritance AND composition**: Allow types to extend other types AND allow objects to have multiple types.
4. **AI should work WITH structure, not just text**: Tana's AI commands that understand supertag schemas are more powerful than raw-text AI. Yar's AI should be schema-aware.
5. **Template bundles > static templates**: Package schemas + fields + queries + AI commands together as installable workflow bundles.

---

*Research conducted: 2026-05-24. Sources: tana.inc, tana.inc/docs, community forums (Reddit r/tana), YouTube tutorials, G2/Software Advice reviews, medium.com articles, substack analyses.*
