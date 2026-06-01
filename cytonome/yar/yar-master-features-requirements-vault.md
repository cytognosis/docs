---
title: "Yar Master — Simple Overview"
date: "2026-05-31"
source: "vault-variant"
category: "product"
status: "current"
spec: "yar-master-features-requirements.md"
tags:
  - cytognosis
  - yar
  - product
  - flagship
  - adhd-friendly
---

# Yar, in plain terms

> [!NOTE]
> **This is the easy-read variant.** The full spec is the source of truth: [yar-master-features-requirements.md](yar-master-features-requirements.md). Edit there; this page links back.

## One paragraph

Yar is a **local-first, voice-aware companion for neurodivergent people, built by and for neurodivergent people**. You talk or type; Yar uses on-device AI to turn the mess into structured notes, tasks, and a living map of your thinking. Your raw data stays on your device. A safety gate (CAP) blocks anything clinical or unsafe. Yar is the consumer face of Cytognosis's **Cytonome** navigator layer.

## The flagship: the branching brainmap

> [!IMPORTANT]
> You think out loud. Yar grows a **living thought-tree** in real time: it attaches each idea where it belongs, quietly fixes earlier mistakes, learns your slang, and can turn any branch into a proposal, paper, or plan. It is a GPS for your own thinking.

| What it does | Why it helps |
|---|---|
| Attaches each new thought to the right branch | No more "where does this go?" stalling |
| Reorganizes the tree as the idea grows | Fits how associative minds actually work |
| A background agent fixes earlier placements | Mistakes get repaired without breaking your flow |
| Learns your slang and nicknames | Speaks your language, not a rigid command set |
| Untangles parallel trains of thought | Separates the threads you jump between |
| "Add a TODO" handled on a side thread | Catch a task without losing your place |
| Turns a branch into a draft document | Closes the gap from idea to finished thing |
| Beautiful force-directed tree view | A calm, spatial way to see your mind |

It saves into your own knowledge graph (Obsidian / LogSeq), on your device.

## Two more anchor features

- **Adaptive personas**: pick a coach, buddy, or guardian voice. It tunes itself from how you interact (no setup tax). It cannot act like a clinician.
- **Sensors (CSP / USAP)**: one socket for any sensor (voice, watch, questionnaires, future brain trackers). Each needs your separate yes.

## North star: the ADHD paper

Yar follows five design rules from Chen, Meng & Nie (2026), "Not Just Me and My To-Do List":

| Rule | What it means for Yar |
|---|---|
| **Relational accountability** | A present companion, not a nagging alarm |
| **Time as rhythm, not grid** | Ideal vs. baseline plans; streaks that survive bad days |
| **Mood-adaptive** | Reads tone and energy; eases off instead of shaming |
| **Affirm ND cognition** | The brainmap and Brain Weather fit how you think |
| **Co-regulation** | Body-doubling, shared plans, a real community cohort |

The paper's 13 concepts are the validated feature backlog. Top-rated: **Brain Weather** dashboard, **gentle streaks**, **body-doubling**.

## Who is building it and for whom

Built by an openly neurodivergent, queer founder and a close **queer / trans / nonbinary / poly / neurodivergent** community who are the first users, design partners, and (already) data contributors. "Nothing about us without us." The founder also has a track record of inclusive work (diversity groups and HR planning at insitro) and breaking the taboo around mental health.

## Safety, in one line

CAP keeps Yar a companion, not a clinician: on-device by default, no diagnosis, nothing leaves without your yes.

## Glossary

- **Cytonome**: Cytognosis's on-device navigator layer. Yar is its product form.
- **CAP**: Controller-Authority Protocol. The safety gate. Spec lives in [cytoplex/](cytoplex/).
- **CSP / USAP**: the sensor protocol. Two names, same thing. Docs in [sensors/](sensors/).
- **Brain Weather**: a friendly picture of your cognitive state ("light fog with patches of clarity").
- **Gentle streaks**: progress markers that do not reset when you skip a day.

---

**Full detail**: [yar-master-features-requirements.md](yar-master-features-requirements.md) · Safety: [cytoplex/README.md](cytoplex/README.md) · Sensors: [sensors/README.md](sensors/README.md)
