> **Status**: Active
> **Date**: 2026-06-01
> **Author**: \@mohammadi
> **Audience**: engineers
> **Tags**: `yar`, `sensors`, `usap`, `architecture`

# 🧠 Sensor Architecture — ADHD Summary

**BLUF:** Cytonome uses a pluggable sensor framework where each sensor is a self-contained unit that produces structured observations. Users control which sensors are active. All processing happens on-device.

## ⚡ Three Core Principles

| Principle | What It Means |
|-----------|--------------|
| **Sensor Independence** | Each sensor is standalone, knows nothing about others |
| **User Sovereignty** | Connect/disconnect at will, nothing mandatory, data stays on-device |
| **Universal Schema** | Every sensor (voice, wearable, image) uses the same schema language |

## 🔬 How a Sensor Works

Every sensor has a **Descriptor** (identity card) and implements a **Protocol** (interface):

| Component | Purpose |
|-----------|---------|
| `SensorDescriptor` | Declares ID, modality, privacy level, output fields, hardware needs |
| `Sensor` Protocol | `initialize()` → `start()` → `observe()` / `stream()` → `stop()` → `teardown()` |
| `SensorObservation` | Timestamped structured output with confidence score |
| `SensorRegistry` | Central hub: list available/active sensors, connect/disconnect |

> [!tip] Push vs Pull
> **Push sensors** (mic, camera) receive data chunks. **Pull sensors** (wearables) poll their source on a schedule.

## 🎙️ Sensor 0: Voice Emotion (HuBERT + openSMILE)

The first sensor. Receives 16kHz audio, outputs per-utterance emotion + vocal biomarkers.

| Property | Value |
|----------|-------|
| Modality | Voice (language-independent) |
| Privacy | Biometric (never transmitted) |
| Models | HuBERT-large, openSMILE eGeMAPSv02 |
| Output | 13 fields: emotion, valence, arousal, pitch, jitter, shimmer, HNR, pauses |
| Latency | Real-time (<100ms), 250ms observation interval |

> [!warning] Raw audio is ephemeral
> Deleted after feature extraction. Only structured observations are stored locally (SQLite).

**Data flow:** Mic → VAD (Silero) → Audio Splitter → HuBERT + openSMILE → Merged Observation → Local SQLite + Event Bus → Supervisor Agent + App UI

## 📊 Sensor Roadmap

| Version | Sensor | Source |
|---------|--------|--------|
| v0.1 | Voice Emotion | HuBERT + openSMILE |
| v0.2 | Text Emotion | BERT sentiment |
| v0.3 | Facial Emotion | DeiT / MobileFaceNet |
| v0.4 | Multimodal Fusion | Transformer cross-attention |
| v1.0+ | Apple Watch, OURA, CGM | HealthKit, OURA API, Dexcom |

> [!tip] Key Research Finding
> MindMed AI (2026) shows **voice is the strongest single modality** for emotion detection (91.22%). Intermediate fusion with cross-attention beats all unimodal approaches (91.89%).

## 🛡️ Privacy Model

| Level | Examples | Rule |
|-------|----------|------|
| Biometric | Voice prints, facial features | Never transmitted |
| Health | Heart rate, HRV, SpO2 | On-device only |
| Behavioral | Activity, sleep patterns | User-controlled export |
| Contextual | Ambient noise, time of day | Lowest sensitivity |

**Multi-language is built in from day one.** Paralinguistic features (pitch, jitter) are universal. Text sensors use multilingual models (mBERT, XLM-R).