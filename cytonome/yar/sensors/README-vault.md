---
title: "Yar Sensors (CSP / USAP) — Simple Overview"
date: "2026-05-31"
source: "vault-variant"
category: "sensing"
status: "current"
spec: "README.md"
tags:
  - cytognosis
  - yar
  - sensors
  - csp
  - usap
  - adhd-friendly
---

# Yar Sensors, in plain terms

> [!NOTE]
> **This is the easy-read variant.** The full entry point is the source of truth: [README.md](README.md). Edit there; this page links back.

## One sentence

The sensing component is the **plug socket** for Yar: any sensor (your voice, your watch, a questionnaire, a future brain tracker) plugs in the same way and feeds one shared picture of how you are doing.

## Why it matters

- **One socket, many sensors.** Add a sensor like adding an app. The voice sensor is just the first one.
- **You stay in control.** Each sensor needs its own yes. Raw data stays on your device by default.
- **Everything lines up.** Every sensor speaks the same typed language, so the data feeds Brain Weather and your knowledge graph cleanly.

## What can plug in

| Sensor | Example signals |
|---|---|
| **Voice** | tone and emotion (vocal biomarkers) |
| **Wearables** | Oura, Apple Watch: heart-rate variability, sleep, activity |
| **Self-report** | PHQ-9, GAD-7, ASRS and similar check-ins |
| **Future** | Cytognosis mood tracker, brain trackers (Cytoscope / fNIRS) |

## Glossary

- **CSP / USAP**: the sensor protocol. CSP = Cytonome Sensor Protocol (strategy docs). USAP = Universal Sensor Adapter Protocol (engineering docs). Same protocol, two names.
- **Adapter**: the small piece of code that connects one sensor to Yar.
- **CAP**: the safety gate that makes each sensor ask permission.

---

**Full detail**: [README.md](README.md) · [unified-sensor-report.md](unified-sensor-report.md) · Yar sensor section: [../yar-master-features-requirements.md](../yar-master-features-requirements.md)
