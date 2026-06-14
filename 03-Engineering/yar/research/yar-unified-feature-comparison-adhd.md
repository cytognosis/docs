# 🧠 Yar Tool Comparison: The ADHD-Friendly Version

> [!NOTE]
> **TL;DR**: We compared 9 productivity tools to figure out what Yar should build. Super Productivity wins for getting tasks done, Goblin Tools wins for ADHD support, and Tana wins for organizing knowledge. No single tool does everything Yar will do.
> **Source**: [Full technical comparison](file:///home/mohammadi/repos/cytognosis/docs/cytonome/yar/research/yar-unified-feature-comparison.md)

---

## ⚡ The Quick Version

| Tool | Score | Best At | Should Yar Copy? |
|:---|:---:|:---|:---:|
| Super Productivity | ⭐⭐⭐⭐ | Focus mode, time tracking, breaks | YES, core task layer |
| Leantime | ⭐⭐⭐⭐ | Emoji task mood tracking, AI priorities | YES, emotion features |
| Saner AI | ⭐⭐⭐ | Auto-finding tasks in emails/notes | YES, proactive AI |
| Tana | ⭐⭐⭐ | Smart note types with auto-fields | YES, type system |
| Anytype | ⭐⭐⭐ | Local-first encrypted storage | YES, storage backend |
| Capacities | ⭐⭐⭐ | Easy "things" organizer, offline | YES, UX patterns |
| MCP Pattern | ⭐⭐⭐ | Open data, your own AI memory | YES, architecture |
| Goblin Tools | ⭐⭐⭐ | ADHD task breakdown, spiciness! | YES, AI features |
| Speechify | ⭐⭐ | Listen to anything with highlighting | PARTIAL, TTS only |

---

## 🏆 Category Winners

| What We Measured | Winner | Score |
|:---|:---|:---:|
| 📋 Task Management | Super Productivity | 9/10 |
| ⏰ Time Management | Super Productivity | 10/10 |
| 📚 Knowledge Management | Tana | 10/10 |
| 🤖 AI Integration | Goblin Tools + Saner AI | 9/10 |
| 🧠 ND-Specific Features | ⭐ Goblin Tools | 10/10 |
| 🔓 Open Source | Super Productivity + MCP | 10/10 |
| ♿ Accessibility | Speechify | 9/10 |
| 📱 Mobile Support | Speechify | 9/10 |
| 💰 Best Value | Super Productivity + Goblin + MCP | 10/10 |

---

## 🔍 What Each Tool Does (Tap to Expand)

<details>
<summary>⭐ Super Productivity: The Focus Machine (86/120)</summary>

**What it is**: Free, open-source task manager + time tracker with built-in ADHD support.

**Why ADHD brains love it**:
- **Focus Mode**: Full-screen single-task view so you literally can't wander to other tasks
- **Idle Detection**: Notices when you walk away and pauses your timer (no guilt!)
- **Break Reminders**: Gentle nudge to step away before burnout hits during hyperfocus
- **"Finish Day" celebration**: Dopamine reward when you complete your daily tasks

> [!NOTE]
> **What is idle detection?** (101)
> A feature that watches if you stop using your mouse/keyboard for a while. When you come back, it asks "Were you still working?" so your time tracking stays accurate even if you got distracted.

**What's missing**: No AI, no note-taking, no voice input.
**Cost**: Completely free (MIT license, no catches).

</details>

<details>
<summary>⭐ Goblin Tools: The ADHD Swiss Army Knife (57/120)</summary>

**What it is**: 9 free AI micro-tools, each solving one specific executive function problem.

**The 9 tools**:

| Tool | What It Does | ADHD Problem It Solves |
|:---|:---|:---|
| 🌶️ Magic ToDo | Breaks tasks into steps (with spiciness slider!) | Task paralysis |
| ⏱️ Estimator | Predicts how long tasks take | Time blindness |
| 🧹 Compiler | Turns brain dumps into clean lists | Working memory overload |
| 🎭 Judge | Explains the tone/emotion in messages | Social cue reading |
| ✍️ Formalizer | Rewrites text in any tone you need | Communication anxiety |
| 👨‍🍳 Chef | Suggests recipes from your ingredients | Decision fatigue |
| 🎓 Professor | Explains any topic at your level | Learning support |
| 🤔 Consultant | Helps you make decisions | Analysis paralysis |
| 🎯 Taskmaster | Keeps you on ONE task at a time | Task switching |

> [!NOTE]
> **What is the spiciness slider?** (101)
> When you tell Magic ToDo "clean the house," you can set the spiciness from 1 (mild: 3-4 big steps) to 5 (extra hot: 20+ micro-steps like "pick up the blue towel from the bathroom floor"). Higher spiciness = smaller, easier-to-start steps.

**What's missing**: No data storage, no task tracking, no calendar. It's a thinking tool, not a doing tool.
**Cost**: Free web, $3 one-time for apps. No subscriptions.

</details>

<details>
<summary>📚 Tana: The Smart Notebook (61/120)</summary>

**What it is**: AI-powered knowledge graph where every note becomes a typed, queryable object.

**The big ideas**:
- **Supertags**: Stamp any note as a "Book", "Person", "Meeting" and it auto-adds the right fields
- **Live Search**: Saved searches that update themselves as you add notes
- **Command Nodes**: Little automation robots that transform your notes with AI

> [!NOTE]
> **What are Supertags?** (101)
> Think of them as smart labels. When you tag a note as "#Meeting", it automatically adds fields for Date, Attendees, Action Items. Tag it as "#Book" and you get Author, Genre, Rating. You define what fields each tag creates.

**What's missing**: No time tracking, no focus mode, proprietary cloud (no data ownership).
**Cost**: Free (limited), $10-18/mo for full features.

</details>

<details>
<summary>🆕 Capacities: The "Thinking in Things" Organizer (58/120)</summary>

**What it is**: Knowledge manager where you think in "things" (Books, People, Projects) instead of pages and folders.

**Why it matters**:
- **Simpler than Tana**: Same concept of typed objects, but friendlier UX
- **Offline-first**: Works without internet (important for focus sessions!)
- **Graph visualization**: See how your ideas connect visually

> [!NOTE]
> **What does "thinking in things" mean?** (101)
> Instead of creating a blank page and writing "I met with Alex about Project X," you create a "Meeting" thing, link it to the "Alex" person thing and the "Project X" project thing. Each thing has its own page with all related info. It's like organizing your brain into labeled boxes that link together.

**What's missing**: Less automation than Tana, limited collaboration.
**Cost**: Free tier, ~$12/mo Pro.

</details>

<details>
<summary>🤖 Saner AI: The Proactive Assistant (63/120)</summary>

**What it is**: AI-powered "executive OS" that reads your emails, notes, and calendar, then tells you what to do.

**The standout features**:
- **Skai AI**: Learns from YOUR data, suggests tasks, organizes notes automatically
- **Multi-model**: Choose between GPT-4, Claude 3, or Gemini Pro in one app
- **PiP Focus Window**: A floating window that keeps your current priority visible on screen
- **"Plan My Day"**: AI generates a time-blocked schedule by scanning everything

> [!NOTE]
> **What is PiP Focus?** (101)
> Picture-in-Picture Focus is a small floating window that stays on top of other apps, showing your current priority task. So even when you open your browser and start going down a rabbit hole, that little window is there reminding you what you're supposed to be doing.

**What's missing**: Cloud-only (no offline), no self-hosting, limited free tier.
**Cost**: Free (30 AI msgs/mo), $8-20/mo paid.

</details>

<details>
<summary>🗣️ Speechify: The Reading Helper (46/120)</summary>

**What it is**: Text-to-speech app that reads anything aloud while highlighting each word.

**How it helps ADHD readers**:
- Listen + read at the same time (two brain pathways = better retention)
- Speed up to 4.5x during hyperfocus periods
- AI summarizes long documents before you commit to reading them
- 1,000+ voices including celebrity voices (Snoop Dogg, MrBeast)

> [!NOTE]
> **Why does listening + reading help?** (101)
> ADHD brains often struggle with sustained visual attention (eyes drift, re-read the same line). Audio provides forward momentum, like a guide rail for your eyes. The synchronized word highlighting gives your eyes something to follow, reducing the effort of reading.

**What's missing**: No task management, no note-taking. Expensive ($139/yr).
**Warning**: Auto-renewal complaints are frequent. Watch your billing.

</details>

<details>
<summary>🔧 MCP Pattern + Anytype: The DIY Future (58-61/120)</summary>

**What they are**: The building blocks Yar is built on.

- **Anytype**: Free, encrypted, local-first storage. Your data stays on YOUR device.
- **MCP Pattern**: A protocol that lets AI assistants talk to your personal knowledge graph.

> [!NOTE]
> **What is MCP?** (101)
> Model Context Protocol is like a universal language that lets AI assistants read and write to your personal databases. Think of it as a USB port for AI: any AI tool can plug into your data if it speaks MCP.

**What's missing**: Requires tech skills to set up. No ADHD-specific features.
**Cost**: Free and open-source.

</details>

---

## 🎯 What Yar Will Build (From Best of All)

### 🔴 Build Now (Priority 1)

| Feature | Inspired By | Why It Matters |
|:---|:---|:---|
| 🌶️ Spiciness slider for tasks | Goblin Tools | Break "clean the house" into micro-steps you can actually start |
| ⏱️ Time estimation | Goblin Tools | "This will take 20 minutes" fights time blindness |
| 🧹 Brain dump compiler | Goblin Tools | Chaos in, structure out |
| 🔍 Auto task extraction | Saner AI | AI finds action items hiding in your notes/emails |
| 😊 Emoji mood on tasks | Leantime | Track how tasks make you feel, AI adapts priorities |
| 🏷️ Smart note types | Tana | Tag it "Meeting" and fields appear automatically |
| 🔎 Live search queries | Tana | Saved searches that update themselves |

### 🟡 Build Next (Priority 2)

| Feature | Inspired By | Why It Matters |
|:---|:---|:---|
| 🎯 Focus mode | Super Productivity | Full-screen, one task, no distractions |
| ⏸️ Idle detection | Super Productivity | Pauses when you drift, no guilt |
| ☕ Break reminders | Super Productivity | Prevents hyperfocus burnout |
| 🗣️ TTS with highlighting | Speechify | Listen + read for better comprehension |
| 📋 "Plan my day" | Saner AI | AI makes your schedule |
| 🎭 Tone analysis | Goblin Tools | "Was that email rude or am I overthinking?" |
| 📌 PiP Focus window | Saner AI | Floating reminder of what you should be doing |

### 🟢 Only Yar Will Have (Priority 3)

| Feature | What Makes It Special |
|:---|:---|
| 🎤 Voice-first emotional awareness | Yar hears your voice AND detects how you're feeling |
| 🛡️ CAP safety gate | Boundaries that prevent AI from being harmful or overwhelming |
| 🏠 Local-first AI brain | AI runs on YOUR device, YOUR data never leaves |
| 🧩 Unified ND companion | Task + time + knowledge + emotion + AI in ONE app |
| 🔌 MCP server | Other AI tools can plug into Yar's data (open ecosystem) |

---

## 🕳️ The Big Gap (Why Yar Exists)

Here's the reality for ADHD users today:

```
To get through a day, you currently need:

📋 Super Productivity  → for task tracking + focus mode
🌶️ Goblin Tools       → for breaking down overwhelming tasks
📚 Tana or Capacities  → for organizing knowledge
🤖 Saner AI           → for AI that auto-finds your tasks
🗣️ Speechify          → for listening to documents
🔧 Anytype            → for owning your data

That's 5-6 apps. 5-6 logins. 5-6 places your information lives.
Context switching between them is EXACTLY the problem they're trying to solve.
```

**Yar replaces all of them with one app.**

One local-first, AI-native, voice-aware, emotionally intelligent companion that keeps your data on your device, adapts to your brain, and never charges you a subscription.

---

<details>
<summary>📚 Glossary</summary>

| Term | Definition |
|:---|:---|
| **Brain dump** | Writing/speaking everything in your head without organizing it first. The cleanup happens after. |
| **CAP** | Controller-Authority Protocol. Yar's safety system that prevents AI from being harmful. |
| **E2E encryption** | End-to-end encryption. Only you can read your data, not even the app developers. |
| **Executive function** | Brain skills for planning, organizing, starting tasks, managing time, and controlling impulses. ADHD impairs these. |
| **Focus mode** | A full-screen view showing only one task, blocking access to other tasks to prevent distraction. |
| **Hyperfocus** | When ADHD brains lock onto something interesting so intensely that time, hunger, and responsibilities disappear. |
| **Idle detection** | Watches if you stop using your computer/phone. Useful for pausing timers when you drift away. |
| **Knowledge graph** | A web of connected information where every note/task/person links to related things. |
| **Local-first** | Your data stays on your device. Works without internet. You own everything. |
| **MCP** | Model Context Protocol. A standard that lets AI tools read/write to your personal data stores. |
| **Micro-steps** | Very small, concrete actions (like "open the kitchen drawer" instead of "organize the kitchen"). Easier to start. |
| **Neurodivergent (ND)** | Brains that work differently from the "typical" pattern. Includes ADHD, autism, dyslexia, and others. |
| **On-device AI** | AI that runs on your phone/computer instead of in the cloud. Private and works offline. |
| **PiP** | Picture-in-Picture. A small window that floats on top of other apps. |
| **Pomodoro** | Work technique: 25 minutes of focus, then 5 minutes of break. Repeat. |
| **Spiciness slider** | Goblin Tools' way of controlling how detailed task breakdowns get. More spicy = more micro-steps. |
| **Supertag** | Tana's name for smart labels that auto-add fields to notes. |
| **Task paralysis** | When a task feels so big/unclear that you can't start it at all. Common in ADHD. |
| **Time blindness** | Difficulty estimating how long things take or noticing time passing. A core ADHD trait. |
| **TTS** | Text-to-speech. Converts written text to spoken audio. |

</details>
