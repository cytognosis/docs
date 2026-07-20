> **Status**: Active
> **Date**: 2026-07-19
> **Author**: @mohammadi
> **Audience**: @shahin (ADHD-friendly navigation)
> **Tags**: `yar`, `index`, `adhd`

# Yar Docs, the 60-Second Map

**One sentence:** Yar is a local-first, fully free AI companion built by and for neurodivergent adults; everything about it lives in this folder, and this page tells you where.

**Twin:** the full master index is [`README.md`](./README.md). This page is the fast version.

## I want to...

| I want to... | Open this | Time |
|---|---|---|
| Remember what Yar IS | [`yar-product-spec.md`](./yar-product-spec.md) | 10 min |
| Look up ONE feature | [`YAR_FEATURE_CATALOG.md`](./YAR_FEATURE_CATALOG.md) | 1 min |
| See the feature tree visually | [`assets/viz/yar-feature-tree.html`](./assets/viz/yar-feature-tree.html) | instant |
| Check how something will be BUILT | [`spec/README.md`](./spec/README.md), then the one spec you need | 2 min |
| See timeline and effort | [`research/YAR-WAVE-ROADMAP.md`](./research/YAR-WAVE-ROADMAP.md) | 8 min |
| Prep for YC | [`submission/README.md`](./submission/README.md) | 2 min |
| Find WHY a decision was made | Decision records in [`research/README.md`](./research/README.md) | 2 min |

## The 5 things that matter most

1. **`yar-product-spec.md`**: the product. Identity, architecture, safety. Start here after a break.
2. **`YAR_FEATURE_CATALOG.md`**: all **69 features** by build wave. The front door.
3. **`spec/`**: 20 active specs. All founder-approved 2026-07-19.
4. **`research/YAR-WAVE-ROADMAP.md`**: what gets built when, with what team.
5. **`research/features.json`**: the machine source of truth. Scripts read this, not the markdown.

## Decisions locked on 2026-07-19 (do not re-open)

- **69 features** (F65-F69 added; F24 got interactive refinement).
- **Sync:** any-sync as transport only; Yar's own reducer stays boss; Loro for CRDT.
- **Memory:** PeT temporal knowledge graph on the existing SQLite/FalkorDB storage; converges with cytomem.
- **Agents:** Supervisor, Interviewer, Transcriber, Proofreader, Mind-mapper. Those five names, nothing else.
- **Framework:** Tauri v2 on phone AND desktop. Flutter is contingency only.
- **Routing:** simple local-vs-cloud selection. Cactus is gone (license trap).
- **Diarization (F69):** internal use now; lawyers only before PUBLIC release.
- **Encryption:** required when cloud agents arrive, not before.

## Where things are NOT

- Old MVP docs, old steering docs, the Flutter recommendation: **removed 2026-07-19**, live in git history.
- Sensor science: **Cytoscope project**, not here.
- Tool evaluations (EVAL-*): `04-Engineering/yar/research/`.
- Code: `~/repos/cytognosis/Yar`.

**Feeling lost?** Open [`README.md`](./README.md) and use the Start-here table.
