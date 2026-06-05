---
type: reference
title: "Self-Study Textbook List + NotebookLM Prompt"
created: 2026-06-05
updated: 2026-06-05
tags:
  - reference
  - learning
  - textbooks
  - self-study
  - notebooklm
  - personalized
status: stable
related:
  - "[[Most Self-Teachable High-Value Skills (Tier List for Joe)]]"
  - "[[Research: How to Learn Anything (The Science of Learning)]]"
  - "[[Metalearning (Drawing the Map)]]"
  - "[[Active Recall (Retrieval Practice)]]"
  - "[[The Feynman Technique]]"
  - "[[Linear Algebra for AI and Quant]]"
  - "[[Calculus in Electrical Engineering]]"
  - "[[Differential Equations in Electrical Engineering]]"
---

# Self-Study Textbook List + NotebookLM Prompt

The best textbook for each subject you can realistically self-teach from a book, plus a reusable [[NotebookLM]] prompt that turns any of them into a structured study plan.

> [!tip] The one rule
> Only pick a self-study book that **grades you** — worked examples + end-of-chapter problems + a solutions manual (official or community). The answer key *is* your feedback loop. See [[Most Self-Teachable High-Value Skills (Tier List for Joe)]].

## The textbook list

| Subject | Best self-study textbook | Backup / supplement | Has solutions? |
|---|---|---|---|
| **Linear algebra** | Strang, *Introduction to Linear Algebra* | Free MIT OCW 18.06 lectures | ✅ |
| **Calculus** | Stewart, *Calculus* (gentle) | Spivak, *Calculus* (rigorous) | ✅ |
| **Differential equations** | Boyce & DiPrima, *Elementary Differential Equations* | Strang, *Differential Equations and Linear Algebra* | ✅ |
| **Probability & statistics** | Blitzstein & Hwang, *Introduction to Probability* | Free PDF + Harvard Stat 110 (edX) | ✅ |
| **Analog circuits** | Sedra & Smith, *Microelectronic Circuits* | Razavi, *Fundamentals of Microelectronics* | ✅ |
| **Practical electronics** | Horowitz & Hill, *The Art of Electronics* | *AoE — Student Manual* | ⚠️ build/measure |
| **Signals & systems / DSP** | Oppenheim, *Signals and Systems* | Oppenheim, *Discrete-Time Signal Processing* | ✅ |
| **Algorithms / CS** | Cormen et al., *CLRS* | *SICP*; Nand2Tetris (auto-grades) | ✅ |
| **Electromagnetics** | Griffiths, *Introduction to Electrodynamics* | Purcell & Morin, *Electricity and Magnetism* | ✅ |
| **Economics / finance** | Hull, *Options, Futures, and Other Derivatives* | Mankiw, *Principles of Economics* | ✅ |

> [!warning] ⚠️ = no clean answer key
> *The Art of Electronics* teaches by building and measuring on a bench, not by graded problem sets — pair it with hardware, not a solutions manual.

## The NotebookLM prompt (reusable)

Upload the textbook PDF (and any solutions manual / lecture notes) as sources in [[NotebookLM]], then paste this:

```
You are my study coach for this textbook. I am self-teaching it solo and want to
learn it efficiently using active recall, spaced repetition, and the Feynman technique.

Using ONLY the uploaded source(s), do the following:

1. MAP THE SUBJECT. List the major topics in dependency order (what must I learn
   before what?). Flag any prerequisite knowledge the book assumes I already have.

2. SPLIT EACH TOPIC into three buckets:
   - CONCEPTS I must understand (explain in plain English)
   - FACTS I must memorize (turn these into flashcards)
   - PROCEDURES I must practice (the problem types I should be able to solve closed-book)

3. BUILD A STUDY PATH. Give me an ordered chapter-by-chapter plan with a realistic
   number of hours per chapter and a one-line "you can do X when this is done" goal
   for each.

4. FOR THE CHAPTER I NAME BELOW, produce:
   - A 5-sentence Feynman-style explanation of its core idea
   - 10 active-recall questions (mix of concept + procedure), answers hidden at the end
   - 8 Anki-ready flashcards in "Front | Back" format for the must-memorize facts
   - The 3 problem types I should drill until automatic, with one worked example each

5. Tell me the single most common mistake learners make on this material and how to
   avoid it.

Start with: CHAPTER = [Chapter 1]
Keep everything grounded in the uploaded source. If something isn't covered, say so.
```

### Quick follow-up prompts (once it's mapped)

- `Quiz me on Chapter ___ — ask one question at a time, wait for my answer, then grade it and explain.`
- `I got this problem wrong: [paste]. Diagnose my misconception, don't just give the answer.`
- `Generate 20 interleaved problems mixing Chapters ___ to ___ in random order.`
- `Explain [concept] as if I'm a smart 12-year-old, then again at full rigor.` ([[The Feynman Technique]])
- `Make an Anki deck (Front | Back) for every formula and definition in Chapter ___.`

## How to use this with the protocol

1. **Map first** with the NotebookLM prompt → [[Metalearning (Drawing the Map)]]
2. **Facts → Anki**, **Concepts → Feynman**, **Procedures → closed-book problems** → [[Active Recall (Retrieval Practice)]]
3. **Work every example closed-book before reading the solution** — re-reading teaches almost nothing; solving is the point.
4. **Interleave** problem types and **compound daily**.

→ Full reasoning in [[Most Self-Teachable High-Value Skills (Tier List for Joe)]].
