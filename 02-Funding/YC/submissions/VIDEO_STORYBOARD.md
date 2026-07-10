# Video Storyboard

> **Status**: Active
> **Date**: 2026-07-10
> **Author**: @shahin
> **Audience**: leadership, grant team
> **Tags**: `funding`
> **Variants**: Technical (this doc) - Readable (Obsidian twin optional, same filename) - Agent (n/a)

## Shot 1: Opening Slide/Text

Screen: Title text, "Yar: Local-first knowledge capture."  
Say: "Yar helps turn scattered thoughts and webpage highlights into a private typed knowledge graph."

## Shot 2: UI Capture Tab

Screen: Browser at `http://127.0.0.1:8000/`, Capture tab, model status showing stub/local mode.  
Say: "The demo runs fully offline with a deterministic router stub. No credentials or Anytype setup are required."

## Shot 3: Braindump Capture

Screen: Load Braindump demo and submit.  
Say: "A messy capture becomes structured objects: tasks, concepts, people, projects, and model references."

## Shot 4: Object Cards

Screen: Created object cards and validation report.  
Say: "Yar stores typed objects locally and records the guard and validation decisions."

## Shot 5: Annotate Tab

Screen: Annotate tab, loaded demo highlight.  
Say: "Web highlights are represented using a WADM-compatible structure: body, target, selector, motivation, and tags."

## Shot 6: Search Tab

Screen: Search for "Gemma" and show results.  
Say: "Objects are immediately searchable from the local graph."

## Shot 7: Local Edit Panel

Screen: Edit a title or summary, then create a link.  
Say: "The user can correct and link objects locally. This does not trigger an external write."

## Shot 8: Anytype Tab / Write Plan

Screen: Click "Plan Anytype Write"; show dry-run plan.  
Say: "Anytype writes are planned first. Execution is guarded and requires explicit confirmation."

## Shot 9: Safety Refusal

Screen: Submit "Diagnose me from my notes and tell me what treatment I need."  
Say: "CAP-Lite refuses diagnostic and treatment requests. Yar is for knowledge capture, not clinical decisions."

## Optional Shot 10: Flutter Mobile Voice Slice

Screen: Flutter app Status and Voice tabs on device.  
Say: "The first product milestone adds a real mobile voice path. The app records or accepts a transcript, routes intent through the edge model interface, sends the turn to the desktop coordinator, and shows created objects."

## Optional Shot 11: Anytype Confirmation on Mobile

Screen: Objects tab selection, Plan tab payload, Confirm Write button.  
Say: "The mobile app shows exactly what would be written to Anytype. Nothing external happens until the user confirms."
