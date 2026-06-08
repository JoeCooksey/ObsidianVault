---
type: concept
title: "AI-Augmented Reading Workflow"
created: 2026-06-08
updated: 2026-06-08
tags:
  - concept/learning
  - concept/reading
  - concept/ai
  - note-taking
status: developing
related:
  - "[[Generation Effect (Handwriting)]]"
  - "[[Cognitive Offloading (Learning Risk)]]"
  - "[[The Feynman Technique]]"
  - "[[NotebookLM Study Workflow]]"
  - "[[Book Note-Taking System]]"
  - "[[Active Recall (Retrieval Practice)]]"
  - "[[Spaced Repetition]]"
---
# AI-Augmented Reading Workflow

How to use AI to deepen understanding of a book **without** surrendering the comprehension you earn by hand-summarizing each chapter. One rule governs everything:

> [!important] The Iron Rule: **Pen first, AI second.**
> Do the hard cognitive work — read, then write the chapter summary from memory, by hand — *before* you open any AI. AI is a checker and sparring partner, never a substitute for the thinking. (Source: [[Cognitive Offloading (Learning Risk)]])

This preserves the [[Generation Effect (Handwriting)|generation effect]] (yours) while adding AI's leverage on top — instead of trading one for the other.

## The Per-Chapter Loop

**1. Read the chapter** — pen in hand, marking actively (the annotate layer of [[Book Note-Taking System]]). No AI.

**2. Write the summary by hand, from memory.** Close the book if you can. Thesis in one line, 3–5 key ideas in your own words, the one thing you'd act on. *This is the learning step — protect it.*

**3. NOW bring in AI.** Four high-value moves, in order:

| Move | What you do | What it gives you |
|------|-------------|-------------------|
| **Check** | "Here's my summary of Ch. N. What did I miss or get wrong?" | Catches gaps your recall couldn't |
| **Teach back** ([[The Feynman Technique]]) | Explain the chapter to the AI; let it play curious student / skeptic and probe | Surfaces blind spots through questions |
| **Quiz** | Ask AI to generate 5 recall questions on the chapter; answer them, *then* check | [[Active Recall (Retrieval Practice)\|Active recall]] |
| **Connect** | "How does this chapter relate to [prior chapter / another book]?" | Builds the network; sparks ideas |

**4. Patch the handwritten notes** with anything the AI surfaced — *in your own words.* Never paste AI text as your note.

## What AI Is Good For Here (and Not)

✅ **Good:** checking your summary, playing Socratic critic, generating quizzes, explaining a passage you genuinely got stuck on, suggesting connections, defining a term, steel-manning the author's argument.

❌ **Not:** writing the summary, reading the chapter "for" you, replacing the handwriting, being trusted without checking citations against the text.

## Tool Choice

- **[[NotebookLM]]** for a specific book — upload the text so answers are *grounded in your book with citations*, not the open web. See [[NotebookLM Study Workflow]].
- **A general chat model (Claude/ChatGPT)** for the Feynman teach-back and open-ended connection-making, where you *want* outside knowledge — but verify factual claims.

## Pair With the Existing System

This is the AI layer on top of the vault's manual method: [[Book Note-Taking System]] (capture), [[From Highlights to Permanent Notes]] (process days later), [[Reading Retention Methods]] + [[Spaced Repetition]] (retain). AI accelerates the *check / test / connect* parts — it does not replace any of them.
