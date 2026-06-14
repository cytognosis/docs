---
title: "Cytoplex (CAP) — Simple Overview"
date: "2026-05-31"
source: "vault-variant"
category: "safety"
status: "current"
spec: "README.md"
tags:
  - cytognosis
  - yar
  - cytoplex
  - cap
  - adhd-friendly
---

# Cytoplex (CAP), in plain terms

> [!NOTE]
> **This is the easy-read variant.** The full spec overview is the source of truth: [README.md](README.md). Edit there; this page links back.

## One sentence

Cytoplex is the **safety gate**. It decides what Yar is allowed to do, keeps your private data on your device, and writes down every decision so it can be checked later.

## Why it matters

- Yar can suggest things. Cytoplex makes sure it can never **act** in an unsafe way.
- No diagnosis. No treatment claims. No data leaving your device without your yes.
- Every "yes" or "no" is logged in a tamper-evident trail.

## The pieces (plain names)

| Piece | What it does |
|---|---|
| **Directive** | A request to do something ("save this", "send that"). |
| **Guard** | The bouncer. It checks each Directive and can say no. "No" always wins. |
| **Refusal message** | A clear reason when the Guard says no. |
| **Audit chain** | A locked logbook of every decision. |
| **CAP-Lite / CAP-Med** | Two strictness levels. Yar uses **CAP-Lite**. Clinics would use **CAP-Med**. |

## How it connects to Yar

- It is the boundary **before** the AI runs and **before** anything is written out.
- It governs **personas** (a persona can never act like a doctor).
- It governs **sensors** (each sensor needs your separate permission).

## Glossary

- **CAP**: Controller-Authority Protocol. The safety protocol. (Not "Cognitive Architecture" or "Communication Augmentation"; those are old mistakes.)
- **Cytoplex**: the doc set and spec that defines CAP.
- **Deny-wins**: if any check says no, the answer is no.

---

**Full detail**: [README.md](README.md) · [spec/](spec/) · Yar safety section: [../yar-master-features-requirements.md](../yar-master-features-requirements.md)
