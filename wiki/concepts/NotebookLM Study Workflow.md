---
type: concept
title: "NotebookLM Study Workflow"
created: 2026-06-08
updated: 2026-06-08
tags:
  - concept/learning
  - concept/ai
  - study-tools
  - notebooklm
status: developing
related:
  - "[[NotebookLM]]"
  - "[[AI-Augmented Reading Workflow]]"
  - "[[The Feynman Technique]]"
  - "[[Active Recall (Retrieval Practice)]]"
---
# NotebookLM Study Workflow

How to run a book through [[NotebookLM]] chapter by chapter — the concrete "AI second" engine for the [[AI-Augmented Reading Workflow]]. Its advantage: every answer is **grounded in your uploaded book with inline citations**, so it stays on the text and you can verify it.

## Setup

1. Create one notebook **per book**.
2. Add the chapters as sources — paste text, or upload the PDF / EPUB chapter files. (Keep chapters as separate sources if you can, so you can scope questions to one.)

## The Per-Chapter Routine (after your handwritten summary)

1. **Verify, don't generate.** *Only after* writing your own summary, ask: *"What are the main points of Chapter N? Cite the passages."* Compare to yours — the gaps are your study list. (Never read this before step 2 of the [[AI-Augmented Reading Workflow]].)
2. **Quiz yourself.** Use the **flashcards / quiz** generator on that chapter. Answer from memory first, then check — [[Active Recall (Retrieval Practice)|active recall]].
3. **Teach back via Learning Guide.** Its tutor mode asks probing open-ended questions instead of giving answers — your [[The Feynman Technique|Feynman]] partner that stays inside the book.
4. **Interrogate hard passages.** Ask targeted questions on anything you stalled on; the citation lets you jump back to the exact spot.
5. **Audio Overview for review.** Generate a Brief or Debate overview to review the chapter on a walk/commute — *reinforcement, not first contact.*

## Whole-Book Moves

- **Glossary / character map** via the Reports feature.
- **Cross-chapter synthesis:** *"How does the argument in Ch. 3 build on Ch. 1?"* — only meaningful once you've read both.

## The Guardrails

> [!warning] NotebookLM makes it *easy* to read the AI summary instead of the book. That's the offloading trap ([[Cognitive Offloading (Learning Risk)]]). Discipline: book and pen first, NotebookLM as the second pass only.

- It's grounded but **not infallible** — spot-check citations against the actual page.
- Vendor framing oversells "read a 400-page book in 2 hours"; that's skimming, not understanding. Use it to *deepen* reading, not skip it. (Source: [[NotebookLM Student Features — Google]])
