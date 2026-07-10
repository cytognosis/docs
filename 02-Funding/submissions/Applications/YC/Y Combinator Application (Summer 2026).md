# Y Combinator Application

## Summer 2026 — Yar

> Strategic note (delete before submitting): This application pivots from the prior two (which pitched the Cytognosis deep-tech health platform as a nonprofit) to **Yar, a for-profit consumer app**, with Cytognosis Foundation as the upstream nonprofit science platform. Rationale: YC's nonprofit track is narrow (2 to 4 per batch, and it favors fee-charging, startup-shaped nonprofits, not research foundations), and the platform is a 10-year capital-intensive effort. Yar is shippable now, has genuine founder-market fit, and is the consumer wedge of the same mission. Apply as a for-profit; that is where the odds, the deal, and YC's evaluation all favor this work.

---

## FOUNDERS

### Founder

Shahin Mohammadi, Founder and CEO.

### Work history

- **Cytognosis Foundation, Founder & CEO (Oct 2025 to present).** Building the open science platform Yar is built on; leading the AI and product work.
- **GenBio AI, Staff Research Scientist (Oct 2024 to Sep 2025).** Led interactome modeling for AIDO, the first multiscale biological foundation model.
- **insitro, Senior Data Scientist (Aug 2020 to Oct 2024).** Built multimodal "virtual cell" models for drug-target discovery.
- **MIT CSAIL / Broad Institute, Research Scientist (2017 to 2020, affiliate to present).** Led the first single-cell brain atlases for Alzheimer's (Nature 2019, contributing author) and schizophrenia (Science 2024, co-first author).
- **PhD, Computer Science, Purdue (2010 to 2016).** Built ACTIONet, open-source single-cell tools used across the field.

### Please tell us about a time you most successfully hacked some (non-computer) system to your advantage.

Academia has a bug: transformative collaborations take four-plus years, but you must publish every six months to survive. I found a workaround. Volunteer affiliate status gives full academic access without the publish-or-perish pressure, which let me become the neutral bridge between McLean and Mount Sinai, two competitors who needed to collaborate but could not trust each other with credit. Four years of patient protocol alignment later, we published the first multi-cohort schizophrenia atlas in Science. I patched a broken incentive system with a structural trick rather than brute force, and it is now being replicated for bipolar disorder.

### Please tell us in one or two sentences about the most impressive thing other than this startup that you have built or achieved.

After 37 years misdiagnosed across ten medical specialties, I used the computational genomics tools I had spent my career building to analyze my own data and found the single ultra-rare TBX1 mutation that connected every "unrelated" condition. I diagnosed myself when ten specialists could not.

### Tell us about things you've built before.

I built and shipped open-source software used by thousands of researchers: ACTIONet (single-cell state discovery, github.com/shmohammadi86/ACTIONet, Apache 2.0) and its ecosystem. I led the engineering of multimodal foundation models (AIDO at GenBio AI; virtual-cell models at insitro). Most relevant here: I built Yar's working MVP myself, solo, with an on-device AI pipeline and 243 passing tests, in a single intense build cycle.

### List any competitions/awards you have won, or papers you've published.

Over 40 peer-reviewed publications, roughly 4,000 citations (Google Scholar), including Science (2024, schizophrenia atlas, co-first), Nature (2019, Alzheimer's atlas, contributing author), and three in Nature Communications. Khwarizmi National Youth Award, Iran's top national science competition (2002).

---

## FOUNDER QUESTIONS

### Who writes code, or does other technical work on your product? Was any of it done by a non-founder?

I write all of it. Yar's Flutter app, the FastAPI backend, the on-device model integration, the safety layer, and the knowledge-graph schemas are mine. Twenty years of ML engineering and a lifetime of needing this tool. No non-founder code to date.

### Are you looking for a cofounder?

Yes. I am actively looking for a cofounder who is neurodivergent themselves and brings consumer product, design, and growth experience to complement my technical and scientific depth. I am building the thing I need; I want a cofounder who lives the same problem from the user side.

---

## COMPANY

### Company name

Yar

### Describe what your company does in 50 characters or less.

A private AI companion for neurodivergent minds

### Company URL, if any

cytognosis.org/yar (product site in development)

### Demo Video

[To be recorded: 60-second screen capture of voice brain-dump to structured, retrievable objects, fully on-device]

### Please provide a link to the product, if any.

Working MVP (TestFlight build in preparation); repository private pending launch.

### What is your company going to make?

Yar is a private, on-device AI companion for the roughly one in five adults whose brains work differently: people with ADHD, autistic adults, twice-exceptional and late-diagnosed adults.

It does three things, in order of how far along we are:

1. **Capture and structure (working today).** You brain-dump by voice or text, the way the thought actually arrives, and Yar turns the mess into structured, retrievable items (tasks, notes, ideas, papers, people, decisions) without you fighting a form. It captures from anywhere, understands the context of what you are working on, and its voice interface does not force a linear train of thought, which is exactly where every other tool fails an ADHD brain. We anchor a note to whatever you are working on using the open W3C Web Annotation standard (the same one hypothes.is is built on), so a thought stays attached to its context instead of floating away. Thoughts stop vanishing.
2. **Translate (next).** A bidirectional communication translator: tell Yar "I need to say this to my boss and not sound angry," and it helps you say it; paste "my manager said we should discuss your priorities," and it tells you what that actually means and how worried to be. It reads each person through the temporal context of your past interactions with them and a learned sense of how they actually communicate, not a generic tone model. Plus emotional aftercare after the hard conversations.
3. **Companion (later).** Longitudinal, judgment-free context about your life and the people in it, and eventually voice-based wellbeing signals over time.

Here is the wedge, and it is the part incumbents miss. Health and wearable apps share one fatal flaw: people start excited and abandon them within a month or two, and continuous tracking is worthless once they stop showing up. For neurodivergent users it is worse, because every separate app charges a context-switching tax our brains can least afford. So Yar does not start as a health app. It earns a place in your daily routine first by being genuinely useful for what ND adults struggle with every day, and only then adds "sensors" gradually, in software, on top of a habit that already exists: a speech-emotion mood signal from the voice you are already using, a cycle tracker, a social-interaction tracker. Each of these is a pluggable sensor in a universal on-device adapter (an "MCP for sensors"), so a user can connect their Oura ring or smartwatch today and our own mood or brain sensors later, all feeding one private local hub. And the companion itself is an adaptive persona (coach, buddy, guardian, and so on) that auto-tunes to the user and their mood, instead of making an overwhelmed ADHD brain configure it. Each one helps immediately, and, with consent, builds the longitudinal, multimodal picture of a life that no abandoned health app ever gets to see.

The defining choice: Yar runs on your own devices and your data does not leave by default. A safety layer we built (Cytoplex) sits in front of every model call and hard-blocks diagnosis, treatment advice, and unconfirmed data sharing. Not "we promise not to look." We literally cannot.

### Where do you live now, and where would the company be based after YC?

Daly City, CA. We would be based in San Francisco.

### Explain your decision regarding location.

I am already here, the consumer-AI and design talent I need is here, and YC is here. Yar is software, so unlike the hardware platform, it has no wet-lab dependency. We can move at consumer-app speed from day one.

---

## PROGRESS

### How far along are you?

I have a working MVP. On-device Gemma 4 turns voice and text into validated, typed knowledge-graph objects, stored locally, with optional confirmed sync to a personal knowledge graph. Product Milestone 1 — the end-to-end mobile voice loop (capture → on-device Gemma → Cytoplex-Lite safety gate → confirmed knowledge-graph write) — is shipped. The build has 243 passing automated tests, including 93 tests on the safety layer alone, and zero lint violations across the codebase. What I do not have yet: real users. The honest state is "the engine runs; now I put it in people's hands."

### How long have each of you been working on this?

I have been full-time on the Cytognosis mission since October 2025. Yar itself, the consumer product, I built in an intense recent cycle as the shippable front edge of that mission. The neurodivergent insight behind it is lifelong.

### What tech stack are you using, or planning to use?

Flutter (mobile), FastAPI (backend), on-device Gemma 4 via LiteRT and Ollama for local inference, SQLite for local storage, optional Anytype sync for the personal knowledge graph, and our own Cytoplex safety protocol in front of every model call. Schemas are LinkML-style YAML so every AI output is validated before it is written. Cursor for development. The Tier 3 wellbeing layer will add a paralinguistic voice pipeline (openSMILE, HuBERT) down the road.

### Are people using your product?

Not in production yet, but not from a standing start either. I am embedded in tightly-knit neurodivergent and queer/trans communities that are exactly Yar's first users, and they are already pulling: friends have sent me their own whole-genome data unprompted, and several, including engineers who build and wear their own sensors, are ready to be design partners and first users today. The next 90 days turn this warm cohort into a measured, retained beta.

### When will you have a version people can use?

A TestFlight beta within 4 to 6 weeks; a public App Store launch within the batch. The capture-and-structure core is already functional, so the gap to "real people using it daily" is packaging and onboarding, not core technology.

### Do you have revenue?

No.

### If you are applying with the same idea as a previous batch, did anything change?

Yes, and the change is the point. I applied twice (Winter 2025, Spring 2026) pitching the full Cytognosis platform: a "GPS for Health" with AI models and biosensors, as a nonprofit. It is real and I am still building it, but it is a 10-year, capital-intensive science effort, which is a poor fit for a 3-month YC sprint and an awkward fit for the nonprofit track.

Yar is the pivot: the same mission's consumer wedge, shippable now. The platform's third pillar was always an on-device "navigator" that helps a person act on what their biology and behavior are telling them. Yar is that navigator, stripped to the part I can put in users' hands today, for the population I belong to and understand. I stopped pitching the infrastructure and started shipping the product.

### If you have already participated in an incubator/accelerator?

I completed NUCLEATE (2019). I have grant applications pending (ARPA-H, Coefficient Giving, EA Funds) that fund the upstream nonprofit science platform, separate from Yar the product.

---

## IDEA

### Why did you pick this idea to work on? Do you have domain expertise? How do you know people need it?

I am neurodivergent. I spent 37 years misdiagnosed, built a career in AI because it was the one environment that fit how I think, and I have lost more good thoughts to the gap between having an idea and capturing it than I can count. Every productivity tool I have tried was built for a brain that is not mine, and punished me for it with streaks, red overdue badges, and rigid forms. I built Yar because the tool I needed did not exist.

The strategic spark came from my friend Anna, who worked at a wearable health company. Their users signed up excited and then quietly stopped opening the app within a month or two, which is the dirty secret of the whole category: continuous health tracking is worthless if people do not show up. For neurodivergent users it is worse, because every separate app carries a context-switching cost our brains can least afford. My conclusion: you do not win health engagement by asking people to adopt a health app, you win it by being genuinely useful in daily life first, then adding sensing on top of a habit that already exists. That is the entire wedge behind Yar.

Domain expertise: 20 years building AI/ML, including foundation models, and the engineering to ship a private on-device pipeline solo. Founder-market fit is not a line in this application; it is the entire thesis.

How I know people need it: roughly 5 to 10% of adults have ADHD, 2 to 3% are autistic, and late diagnosis is a fast-growing wave. Today these users stitch together three or four tools (a notes app, a task app, a voice recorder, a separate "explain this message" hack) because no single tool is built for them. People already pay for Notion, Obsidian, and Tana; the willingness to pay for thinking tools is proven. And I am not guessing at the user, I am the user: embedded in the neurodivergent and queer/trans communities Yar serves, where people are already sending me their own genomic and sensor data and asking to try it. That warm first cohort is exactly what most consumer apps lack. I will validate the specific wedge with these design partners in the batch rather than assert it from a deck.

### Who are your competitors? What do you understand that they don't?

Tana and Obsidian (powerful knowledge graphs, but steep, cloud-tied, and built for power users, not for an overwhelmed ADHD brain at 2am). Goblin Tools (loved by the ND community, but stateless micro-utilities with no memory). Saner AI and Notion AI (cloud-only, your data lives on their servers). Leantime (targets ADHD, but server-first, no voice). The closest new entrants are voice-first capture tools (OMI, open-source and wearable; Letterly, brain-dump-to-text), but they capture beautifully and then do nothing with it: no task execution, no knowledge graph, no emotional awareness. None are local-first, none combine frictionless voice capture with a real knowledge graph and ND-specific design, and none translate communication.

What I understand that they do not: neurodivergent support is fragmented across tools designed for neurotypical cognition, and the winning product is not another feature, it is a single companion that meets the user where their brain actually is, and that earns trust by being structurally private. The moat is the ND-native experience plus the privacy architecture plus, once users arrive, a longitudinal personal-context flywheel no cloud tool can copy without asking users to give up the privacy that brought them. And the insight the health-app incumbents miss is that retention has to come before sensing: win the daily habit first, then layer soft sensors onto an app people already open many times a day. That inverts the abandonment curve that kills health and wearable apps.

### How do or will you make money? How much could you make?

Freemium consumer subscription. The local capture-and-structure core is free, which drives adoption in ND communities that (rightly) distrust data-hungry apps. Paid (target $12/month) unlocks cross-device sync, the communication translator, deeper knowledge-graph integration, and longitudinal insight. Later, a B2B tier: neurodiversity support for employers and university disability-services offices, who already spend on accommodations and have no good software.

Size: an ND-adult TAM in the tens of millions in English-speaking markets alone. At 1 million paying users and $12/month, that is ~$140M ARR, and the consumer-thinking-tools comps (Notion, Obsidian, Tana) show the category supports venture-scale outcomes. The wedge is ND adults; the eventual market is everyone who thinks better out loud.

### Which category best applies to your company?

Consumer (AI app).

### If you had any other ideas you considered applying with, please list them.

The upstream platform itself is the obvious alternative: Cytoverse/Psychoverse (an AI "map" of mental health) and Psychoscope (a wearable brain sensor), which Cytognosis Foundation builds as nonprofit science. I am deliberately not leading with those here, because they are long-horizon and grant-funded. If you would rather we apply with the platform, I can, but I believe Yar is the right YC-shaped bet.

### Describe the scientific basis for your product. How does it work?

Yar is mostly product, not science, which is part of why it fits YC. The one genuinely novel technical piece is Cytoplex (the safety protocol): a deterministic guard layer that intercepts every model call, validates proposed actions against typed schemas, blocks an explicit list of harms (diagnosis, treatment advice, risk scoring, unconfirmed external writes), and requires user confirmation before anything leaves the device. It is how you build an emotionally-aware AI for a vulnerable population without it becoming a reckless therapist or a data leak.

There is also a serious long-term thesis under the product, and it is now backed by peer-reviewed evidence. A 2026 pilot trial (Nan et al., NPP Digital Psychiatry and Neuroscience) built a personalized N-of-1 machine-learning model for each person that learned their own relationship between mood and daily lifestyle (sleep, exercise, diet, social connection), then targeted the single factor that most drove that individual's mood. It produced a large, durable drop in depression (Cohen's d = -0.89, with 55% of completers reaching remission), far beyond the small effects of generic one-size-fits-all advice, and it showed that an LLM could match a trained human coach's personalized plan with up to 95% accuracy. That result took a labor-intensive, coach-bottlenecked, 40-person research setup to reach. Yar is how the same thing happens continuously, privately, on-device, and at scale: the soft sensors (mood from speech, sleep, activity, social patterns) are exactly those signals, captured in daily life instead of a two-week study, and the on-device model plus LLM is the coach. We are explicit that the clinical-grade version is long-term and belongs to the nonprofit's regulated, RCT-validated track, not to Yar's consumer launch. But it means Yar sits on top of a scientifically validated destination, not a hope.

### Describe the next few stages in developing your product. For each stage, how much time and money will it take?

- **Now to Month 1:** TestFlight beta, onboarding flow, first 50 to 100 ND users from communities I am part of. Cost: sweat.
- **Month 1 to 3 (batch):** App Store launch, ship the communication translator (Tier 2), instrument retention, recruit a cofounder. Target: real daily-active users and first paid conversions.
- **Month 3 to 12:** Grow to tens of thousands of users, prove week-4 retention and freemium conversion, launch the B2B pilot. This is what the YC SAFE and a seed round fund.

### If you were accepted into YC, what could you accomplish by Demo Day?

A public app with real, retained users (target 1,000+), the communication translator shipped, a week-4 retention number we are proud of, early paid conversions, and a cofounder onboarded. The MVP already works; the batch turns it into a product people use every day.

### Does your product need regulatory approval (FDA)?

No. Yar is a wellness and productivity app, and Cytoplex structurally blocks any diagnostic or treatment claim, so it is not a medical device. That keeps the consumer launch clean and fast. The regulated, clinical work lives in the separate nonprofit platform, not in Yar.

### What experimental data do you have showing this would work?

Product evidence rather than clinical: a working on-device MVP (243 passing tests), and a documented competitive gap (a 12-tool competitive analysis in which Yar targets 107/120 on feature coverage versus 86 for the next-best tool, showing no existing product combines voice-first capture, a knowledge graph, ND-specific design, privacy-by-architecture, and communication support). Independently, a 2026 ADHD HCI study (Chen, Meng & Nie) speed-dated 13 design concepts with 20 ADHD adults; the highest-rated three — a "brain weather" self-awareness dashboard, dual-track (ideal-vs-baseline) planning, and an AI body-doubling companion — are precisely Yar's top-priority features, so the roadmap is validated by target users before I build it. The real experiment, getting ND users to adopt and retain, is exactly what I want to run in the batch.

---

## EQUITY

### Have you formed ANY legal entity yet?

The nonprofit exists; Yar's operating company does not yet. We will incorporate it if accepted, using YC's standard incorporation path. We do not need it formed to apply.

### Please list all legal entities you have.

Two, and neither is the Yar operating company yet. (1) Cytognosis Foundation, Inc., a Delaware 501(c)(3) nonprofit (incorporated Sep 8, 2025; EIN 39-4383634), which runs the open science platform. (2) An older Cytognosis LLC, effectively dormant and with no share structure, which we will not use as the operating entity. For Yar we will incorporate a clean Delaware C-corp (or PBC) on acceptance, which can take the standard YC SAFE without complication. Yar builds on the Foundation's openly licensed (Apache 2.0) components, which are already public, so no proprietary IP transfer out of the nonprofit is required. The Foundation's exact role (a founding equity stake and/or a collaboration agreement) will be set with counsel to keep the 501(c)(3) clean.

### Please describe the breakdown of the equity ownership.

No equity issued yet, so the cap table is clean for YC. At incorporation: founder(s) majority, a standard employee option pool, and likely a minority founding stake for Cytognosis Foundation so the nonprofit shares in the upside of technology it helped seed. Investors enter through YC's SAFE.

### Have you taken any investment yet?

No.

### Are you currently fundraising?

Not for Yar (the Foundation has nondilutive grant applications pending for the separate platform). Yar's first outside capital would be YC.

---

## CURIOUS

### What convinced you to apply to Y Combinator?

I applied twice with the platform and learned the lesson: YC rewards shippable products with real users and clear founder-market fit, not 10-year infrastructure decks. Yar is the first thing I have built that is all three. I want the forcing function to go from a working MVP to thousands of users and a cofounder in 90 days, and I want YC's consumer and AI network to do it. Will MacAskill's case for mission-driven founders at YC is part of why I first looked; shipping Yar is why I am back.

### Batch Preference

Summer 2026 (applying after the on-time deadline; submitting now and will keep the application updated as users come online).
