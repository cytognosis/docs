# ElevenLabs Impact Partner Application

> Ready to submit at [elevenlabs.io/impact-partners](https://elevenlabs.io/impact-partners)

---

## Field 1: Organization Name

```
Cytognosis Foundation
```

## Field 2: Organization Website

```
https://cytognosis.org
```

## Field 3: Registered Non-Profit?

```
Yes
```

## Field 4: Full Name

```
Shahin Mohammadi
```

## Field 5: Email

```
shahin@cytognosis.org
```

## Field 6: Supporting Documentation

> Upload 501(c)(3) determination letter (EIN: 39-4383634)

---

## Field 7: Partnership Details

*"How are you hoping to partner together? Please provide a description of your organization and a clear use case for ElevenLabs."*

### Draft Response

Cytognosis Foundation is a 501(c)(3) nonprofit building open-source tools for precision mental health. Our founder's 37-year diagnostic odyssey, resolved only through self-directed genomic analysis, drives our mission: no one should wait decades for answers.

We are developing Yar, a private, on-device AI companion for neurodivergent individuals (ADHD, autism, mood and anxiety disorders). Yar runs entirely on the user's phone or laptop, with no data transmitted to external servers. It combines two parallel AI systems: a speech layer powered by Google's Gemma 4 for natural conversation in 35+ languages, and a separate emotion sensing layer using HuBERT and openSMILE to extract vocal biomarkers (pitch variability, speech rate, jitter, shimmer) that track cognitive load and emotional state over time. These structured biomarker observations stay on-device and give users longitudinal insight into their own mental health patterns, including objective before-and-after measures when trying new medications, therapies, or routines.

Yar is the first deployment of Cytonome, our broader "navigator" for a cellular intelligence platform we call a GPS for Health. Within Cytonome, we have designed a universal sensor architecture where each input modality (voice, wearables, text, video) is a pluggable sensor that users can connect or disconnect at will. The voice emotion sensor is our first sensor, and ElevenLabs TTS is the voice users will hear when Yar speaks back to them. The quality, warmth, and naturalness of that voice directly affects whether a neurodivergent person can build trust with their companion during vulnerable moments.

**How we want to partner with ElevenLabs:**

1. **On-device TTS for private, multilingual companion voice.** Our users include neurodivergent individuals across languages and cultures, many in communities with limited access to mental health professionals. ElevenLabs' on-device TTS with 70+ language support would let Yar speak to users in their native language, entirely offline, with no audio ever leaving their device. This is a hard requirement: our Communication Augmentation Protocol (CAP) enforces that all biometric data, including voice, stays on-device.

2. **Voice Design for Yar's default companion voice.** We want to create a warm, calm, non-clinical voice identity for Yar using ElevenLabs Voice Design, without recording a real person. This voice needs to feel like a trusted companion, not a customer service bot or a medical authority. A one-time cloud-based voice design, then deployed permanently on-device.

3. **Audio isolation for cleaner emotion sensing.** Many of our users interact with Yar in noisy environments (public transit, shared housing, busy households). ElevenLabs' audio isolation could pre-process the microphone input before it reaches our HuBERT emotion sensor, improving the accuracy of vocal biomarker extraction without requiring the user to find a quiet room.

4. **HIPAA-compliant infrastructure for future clinical research.** As we move toward IRB-approved clinical studies validating Yar's longitudinal biomarker tracking against gold-standard neuropsychological assessments, we will need HIPAA-compliant voice processing. ElevenLabs' BAA and VPC deployment options are the most mature in the voice AI space and would support our clinical validation pathway.

All of our software is open-source under Apache 2.0. Our sensor architecture is designed so that any organization can build a sensor plugin for Cytonome. We believe voice AI should be accessible to everyone, and we want to demonstrate that through a partnership where ElevenLabs technology reaches underserved neurodivergent communities worldwide, in their own languages, on their own devices, under their own control.

---

> [!TIP]
> **Word count**: ~470 words. Concise enough for a form field, detailed enough to demonstrate technical depth and clear use cases. Adjust length if the form has a character limit.
