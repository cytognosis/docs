# Claude Design Prompt: Create the `app-website` Template

> Paste this prompt into Claude Design when you want it to produce the **initial scaffold** of the Cytognosis public website template (`cytoskeleton/templates/app-website/`). This template is the basis for `cytognosis.org` and any future content-driven Cytognosis site.
> Cytognosis context: full spec in `cytognosis-branding/references/website.md`.

> **Revised from**: `Documents/Cytognosis/Infra and design/03_claude_design_prompts/prompt_template_website.md`
> **Changes**: replaced `cytognosis-template-master` with `cytognosis-branding`, Foundation profile remains default, added accessibility section mentioning WCAG AAA for clinical pages, added font toggle component (Inter/Lexend/Atkinson Hyperlegible), removed em dashes.

---

## Brief

Produce the initial scaffold for the Cytognosis public website template. The template will be consumed via `copier copy cytoskeleton/templates/app-website <product>` by every downstream Cytognosis website (primarily `cytognosis.org`). The scaffold must build cleanly on first clone, pass the cross-template quality gates, and ship working starter pages that demonstrate the full content + forms + admin shape.

The current production site at `https://cytognosis.org/` is FastAPI + vanilla HTML + Jinja2 with a SQLModel-backed forms/admin/blog backend running on Cloud Run. Your earlier May 2026 recreation of the landing page (in `Downloads/website/`) was a useful design exploration but used React 18 via UMD + Babel without a build system. The production template uses **Astro** for the frontend and keeps **FastAPI** for the forms/admin/blog backend.

## 1. Stack (mandatory choices)

- **Frontend framework**: Astro, latest stable.
- **Content**: MDX with content collections (`src/content/`) for blog, stories, team.
- **Styling**: Tailwind CSS configured from the Design System tokens preset (consumed via `design-system-package`).
- **Components**: Astro components for content, React islands (TypeScript strict) for the few interactive pieces (forms, agent panel, theme switcher, font toggle).
- **Backend**: FastAPI + SQLModel for forms, admin, blog. Lives at `backend/` inside the template.
- **Auth (admin)**: Google OAuth via Workload Identity Federation.
- **Search**: Pagefind (Astro-native static).
- **Deployment**: Cloud Run for both the static export and the FastAPI backend.
- **CMS**: none in the initial scaffold; Markdown files in the repo. Stub the integration so Decap or Keystatic can be added later.

## 2. Mandatory artifacts in the scaffold

### 2.1 Pages

Ship every page below with placeholder content that demonstrates the layout and the design system. Real content is filled by Cytognosis after the scaffold lands.

```
src/pages/
├── index.astro                 home: hero, mission cards, platform summary, latest stories, agent CTA
├── about.astro                 foundation, vision, mission, values, board, EIN/UEI footer
├── platform.astro              Cytoverse, Cytoscope, Cytonome, Helix model (4 cards + deep links)
├── team.astro                  team grid; pulls from src/content/team/
├── team/[slug].astro           individual team-member pages (Astro dynamic route)
├── stories.astro               stories index (patient + clinician stories from content collection)
├── stories/[slug].astro        individual story page
├── stories/submit.astro        story-submission form (HIPAA-aware)
├── blog.astro                  blog index
├── blog/[slug].astro           individual post
├── careers.astro               open positions + intake form
├── partner.astro               partnership intake form
├── contact.astro               general contact form
├── events.astro                upcoming events
├── support.astro               donate / volunteer
├── community.astro             community
├── adventure.astro             outreach (current site has this; preserve)
├── candidates.astro            candidate experience (current site has this; preserve)
├── admin/
│   ├── index.astro             dashboard landing (OAuth-gated)
│   ├── submissions.astro       submission moderation
│   └── blog.astro              draft/publish manager
├── api/                        Astro endpoints proxying to the FastAPI backend where useful
├── 404.astro
└── sitemap.xml.ts              build-time sitemap generator
```

### 2.2 Layouts

```
src/layouts/
├── BaseLayout.astro            HTML shell: <head> with SEO meta + OG + JSON-LD, nav, footer, skip-to-content
├── PageLayout.astro            standard content page (hero band + prose body)
├── PostLayout.astro            blog post (with author, date, tags, social-card auto-generation)
├── PersonLayout.astro          team member page
└── AdminLayout.astro           OAuth-gated admin shell
```

Profile assignment: BaseLayout sets `<main data-profile="foundation">` by default; PostLayout for stories sets `data-profile="clinical"`; AdminLayout sets `data-profile="research"`.

### 2.3 Components

```
src/components/
├── nav/
│   ├── Header.astro            fixed-top glass nav; scroll-shrink; scroll-spy; mobile drawer
│   ├── Footer.astro            footer with links, EIN, legal, social
│   ├── MobileNav.astro
│   └── Breadcrumb.astro
├── hero/
│   ├── HeroLanding.astro       home hero (the headline tagline pattern from your May 2026 design)
│   └── HeroPlatform.astro      platform-page hero (Cytoverse/Cytoscope/Cytonome triad)
├── content/
│   ├── Prose.astro             rendered MDX body with brand typography
│   ├── Pullquote.astro
│   ├── Callout.astro           info, warning, tip variants
│   └── ReadingTime.astro
├── forms/                      React islands (client:load)
│   ├── ContactForm.tsx
│   ├── CareerForm.tsx          with CV upload (PDF)
│   ├── PartnerForm.tsx
│   ├── StoryForm.tsx           HIPAA-aware
│   └── NewsletterForm.tsx
├── ui/                         shadcn-derived, design-system-tokenized
│   ├── Button.tsx
│   ├── Card.tsx
│   ├── Badge.tsx
│   ├── Input.tsx
│   ├── ConsentCheckbox.tsx
│   └── FontToggle.tsx          (NEW: switches between Inter/Lexend/Atkinson Hyperlegible)
├── agent/                      React islands
│   ├── TalkToCytognosis.tsx    fixed-position affordance bottom-right
│   └── AgentPanel.tsx          consumes agent-presentation-package + fabric-client-package
├── platform/
│   ├── CytoverseCard.astro
│   ├── CytoscopeCard.astro
│   ├── CytonomeCard.astro
│   └── HelixCard.astro
└── seo/
    ├── SEOHead.astro
    ├── StructuredData.astro
    └── (Open Graph card generator script)
```

### 2.4 Content collections

```
src/content/
├── config.ts                   collection schemas (TypeScript)
├── blog/
│   ├── _placeholder-post.mdx   one example post demonstrating front matter + MDX
│   └── ...
├── stories/
│   └── _placeholder-story.mdx  one example with HIPAA-consent metadata
└── team/
    └── _placeholder-member.mdx one example with bio + photo + role
```

Front matter schemas: title, slug, author, date, tags, social card, status (draft/published), reading time. For stories, add: consent class, anonymous flag, reviewed-by, reviewed-date.

### 2.5 Backend (FastAPI)

```
backend/
├── main.py                     Uvicorn entry; mounts routers
├── pyproject.toml              uv-managed; ruff + ty + nox
├── routes/
│   ├── forms.py                POST /api/forms/{type} with typed SQLModel validation
│   ├── blog.py                 admin CRUD + public read (cached)
│   ├── stories.py              admin moderation queue
│   └── newsletter.py
├── models.py                   SQLModel tables for every form + content type
├── database.py                 SQLite for dev, Cloud SQL Postgres for prod
├── auth.py                     Google OAuth + allowlist
├── admin.py                    admin endpoint helpers
├── cv_parser.py                PDF to structured fields
├── email_service.py            outbound transactional email
├── HIPAA_COMPLIANCE_PLAN.md    documented compliance plan (mandatory file)
└── tests/                      pytest + integration
```

### 2.6 Tests

```
tests/
├── unit/
│   ├── components/             Astro + React Testing Library
│   └── lib/
├── integration/                cross-component flows
├── accessibility/              axe-core on every shipped page
└── e2e/                        Playwright: home, contact-form-submit, story-submit-with-consent, admin-login
```

### 2.7 Documentation

```
docs/
├── README.md                   how to run, how to author content, how to deploy
├── architecture.md             template structure walkthrough
├── accessibility.md            how WCAG rules land in this template (including AAA for clinical pages)
├── privacy.md                  data flow; HIPAA points; consent surfaces
├── seo.md                      sitemap, OG, structured data
├── content-authoring.md        for non-developers: how to add a blog post or a story
└── deployment.md               Cloud Run deploy steps + scripts
```

### 2.8 SEO + structured data

Every page has unique title + description, OG tags, Twitter card tags, canonical URL, and JSON-LD (`Organization` on every page; `Article` on posts; `Person` on team; `BreadcrumbList` on nested pages). Sitemap and robots.txt built at compile time.

### 2.9 Agent CTA

A persistent "Talk to Cytognosis" affordance (bottom-right, brand-aligned, not intrusive) that opens an in-page side panel. The side panel uses the `agent-presentation-package` and `fabric-client-package` so the agent presence is consistent with the phone / desktop / extension templates. Text-only for the first revision; voice support deferred to a later revision.

### 2.10 Accessibility (WCAG AAA for clinical pages)

The scaffold ships with these accessibility requirements:

- **Foundation pages** (marketing, about, platform): WCAG AA minimum, AAA where feasible.
- **Clinical pages** (stories, patient-facing content): WCAG AAA required. All text meets 7:1 contrast ratio. No decorative elements that interfere with comprehension.
- **Admin pages**: WCAG AA minimum.
- Font toggle component available on every page, allowing users to switch between Inter (default), Lexend (reading fluency), and Atkinson Hyperlegible (maximum distinguishability).
- Font preference persists in `localStorage` and applies site-wide.
- Skip-to-content link first focusable; visible breadcrumbs on non-home; ARIA landmarks; one `<h1>` per page; `prefers-reduced-motion` honored.

### 2.11 Font toggle component

The `FontToggle.tsx` React island provides:

- Three font options: Inter (default), Lexend, Atkinson Hyperlegible.
- Accessible dropdown with clear labels explaining each font's benefit.
- Applies the selected font family to the `<html>` element via a CSS custom property.
- Persists choice in `localStorage`.
- Respects the active profile's default font (Foundation defaults to Inter).
- Available in the header settings area and in the footer accessibility section.

### 2.12 Performance + accessibility budgets

The scaffold ships with these baked in:

- LCP < 1.8 s, TTI < 2.5 s, CLS < 0.05, FCP < 0.9 s on mid-tier mobile + 4G.
- Lighthouse: Performance 95+, Accessibility 95+, Best Practices 95+, SEO 100.
- Total page weight < 500 KB (content pages), < 1 MB (home).
- Reading-level checker runs in CI on `/`, `/about`, `/platform`; target Flesch-Kincaid grade <= 10.

## 3. File layout (top of `app-website/`)

```
app-website/
├── README.md
├── package.json
├── astro.config.mjs
├── tsconfig.json
├── tailwind.config.ts          (extends design-system preset)
├── biome.json
├── public/
│   ├── favicon.svg
│   ├── robots.txt
│   ├── manifest.webmanifest
│   ├── _redirects
│   ├── fonts/                  (self-hosted: Inter, Lexend, Atkinson Hyperlegible)
│   └── assets/                 (logos, icons, team photos, generated OG cards)
├── src/                        (per §2.1-§2.4 above)
├── backend/                    (per §2.5)
├── tests/                      (per §2.6)
├── docs/                       (per §2.7)
└── microcopy.json              every UI string keyed
```

## 4. Brand alignment

Consume `design-system-package`'s Tailwind preset. Never inline a `#hex` color. Logo wordmark in the header; logo mark in the favicon. Brand voice rules apply to every visible string:

- No em dashes.
- No "patients" outside clinical context (story pages can use "patient" since they ARE clinical context).
- No hype words (revolutionary, cure, game-changing, breakthrough, disrupt).
- Active present tense.
- Title Case headings, sentence case for UI labels.
- "Cytognosis" always capital C; product names capital.

Hero copy follows the Foundation profile patterns: visionary yet grounded; signature gradient as hero wash; minor magenta accent for "Get involved" CTAs only.

## 5. What to NOT produce

- No React 18 UMD + Babel inline build. The scaffold uses Astro with a proper build system.
- No Google Forms / Typeform embeds. Forms are owned end-to-end.
- No third-party tracking pixels or analytics SDKs.
- No webfont blocking first paint. Self-host fonts where possible; Google Fonts with `font-display: swap` as fallback.
- No "lorem ipsum" placeholder text. Use Cytognosis brand-voice-aligned placeholder copy.
- No inline `<script>` tags (CSP-compatible).
- No tracking pixels in the admin section.
- No raw page content logged server-side.

## 6. Migration salvage (from prior work)

Salvage from your May 2026 React-UMD recreation (in `Downloads/website/`):

- The hero composition (left split: tagline, sub, CTAs, biomarker pills; right split: cellular visual).
- The "Commitment" three-card pattern (Vision, Mission, Values with numbered accents).
- The Platform card pattern (Cytoverse / Cytoscope / Cytonome).
- The icon sprite approach (single SVG with `<symbol>` definitions, referenced via `<use href="#ic-x"/>`).
- The Tweaks-panel concept (could become an admin-only "Theme tweaks" feature).

Do NOT salvage:

- The UMD build (use Astro's build system).
- The inline `<style>` overrides (use the design-system Tailwind preset).
- Hardcoded gradient stops (use signature-gradient token).
- The "v9.0" version chip (we are on v10).

## 7. Definition of done

The scaffold is complete when:

1. `npm install && npm run dev` brings up a working Astro dev server.
2. `npm run build` produces a static export with no errors.
3. `pytest backend/tests/` passes.
4. Every starter page renders with brand-aligned placeholder content.
5. Lighthouse 95+ on the home page on a mid-tier device profile.
6. axe-core reports zero critical or serious issues on home, about, contact-form, story-submit.
7. Story submission form refuses submission without the HIPAA consent checkbox.
8. Admin route returns 401 without OAuth; returns the dashboard with the seeded allowlisted email.
9. `docs/README.md` walks a new developer from clone to running in under 10 minutes.
10. Font toggle switches between Inter, Lexend, and Atkinson Hyperlegible and persists the choice.
11. Clinical pages (stories) meet WCAG AAA contrast ratios.
12. No em dashes anywhere; no v9 brand colors anywhere.

## 8. Deliverables to ship back

1. The complete `app-website/` tree.
2. A `MIGRATION.md` listing what was salvaged from the current production site (`org/website/`) and what was deprecated.
3. A `seed-content.json` describing the placeholder content (so Cytognosis can swap in real content systematically).
4. The first PR-ready commit message in Conventional Commits format.

## 9. Open questions to surface back to Cytognosis (do not silently decide)

1. Newsletter provider: Buttondown vs Beehiiv vs ConvertKit vs self-hosted Listmonk. Recommendation: Listmonk.
2. Analytics: Plausible self-hosted vs Umami self-hosted vs none. Recommendation: Plausible.
3. Story submission moderation flow: who approves? what is the SLA?
4. Search: Pagefind (this scaffold) vs hosted alternative.
5. The "Talk to Cytognosis" affordance: text-only first revision (default), or voice-from-day-one?
6. Photography for team pages: existing photos (in `org/website/static/assets/team/`) or new commissioned shots?
7. Production fonts: self-host or Google Fonts CDN with `display=swap`? Self-host is preferred but needs licensed font files uploaded.
8. Cookie banner: do we need one? Recommendation: yes if any first-party analytics; no otherwise.
9. Should the font toggle include OpenDyslexic as a fourth option on the website? Recommendation: yes, with a note explaining it is designed for dyslexic readers.
