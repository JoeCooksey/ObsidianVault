---
type: concept
title: "Fall 2026 NotebookLM Setup — Textbooks and Master Prompts"
created: 2026-05-20
updated: 2026-05-20
tags:
  - fall-2026
  - ASU
  - notebooklm
  - study-tools
  - circuits
  - linear-algebra
  - physics
status: active
related:
  - "[[EEE 202 Circuits I — Topics and Prep]]"
  - "[[MAT 343 Applied Linear Algebra — Topics and Prep]]"
  - "[[PHY 131 University Physics II EM — Topics and Prep]]"
  - "[[Fall 2026 Summer Study Plan — Joe]]"
  - "[[Research - Fall 2026 Course Prep Plan]]"
---

# Fall 2026 NotebookLM Setup — Textbooks and Master Prompts

Three NotebookLM notebooks — one per course. Each notebook gets one textbook uploaded and a master prompt pasted at the start of every study session to lock in the teaching behavior.

> **How to use**: Create three separate NotebookLM projects (one per course). Upload the textbook PDF(s) listed below. At the start of each session, paste the master prompt into the chat. Say "next section" to advance, "quiz me" for practice, "explain differently" to get an alternate approach.

---

## Course 1: EEE 202 Circuits I

### Recommended Textbook

**Primary (course-assigned):**
> Irwin & Nelms — *Basic Engineering Circuit Analysis*, 12th ed. (Wiley, 2020)
> ISBN: 978-1119592556

- This is the course-assigned text. Upload it to NotebookLM as your primary source.
- The 10th or 11th editions have identical topic coverage — either works.

**Free alternative (if you don't have the Irwin PDF):**
> Alexander & Sadiku — *Fundamentals of Electric Circuits*, 7th ed. (McGraw-Hill)

- More student-friendly prose than Irwin; same topic sequence; widely used at peer universities.
- Check your university library for legal digital access.

**NotebookLM upload tip**: Upload one chapter at a time (Ch 1–3 first) so the notebook stays focused on the section you're studying.

---

### EEE 202 Master Prompt

Paste this at the start of every NotebookLM study session for EEE 202:

```
You are my private tutor for EEE 202 Circuits I at Arizona State University. The source documents loaded in this notebook are from Irwin & Nelms, Basic Engineering Circuit Analysis. Your job is to teach me this textbook section by section.

For every section, follow this sequence:
1. Give a 3-sentence plain-English overview of what we're learning and WHY it matters for electrical engineers
2. State the key equation(s) with a one-line physical description of each variable
3. Work through the first example problem in the section step by step — show every algebraic move
4. Give me one practice problem at similar difficulty, then wait for my answer before explaining it
5. Ask one concept-check question before moving on

Special rules:
- When a topic overlaps with PHY 131 (DC circuits, RLC transients, phasors), flag it with: ⚡ PHY 131 overlap
- Connect every technique to what could go wrong in a real circuit if you got this wrong
- When we reach Units 6–8 (phasors, Bode plots, Laplace), always show the s-domain and time-domain forms side by side

Commands I will use:
- "next section" → move to next section
- "quiz me" → give me 3 problems at increasing difficulty (easy / medium / hard)
- "explain differently" → use a completely different analogy or approach
- "skip" → move on without the practice problem
- "EE context" → explain how this technique is used in real EE work (simulation, design, debugging)
- "LTSpice" → describe how to set up a simulation to verify this result

Begin now: Start with Chapter 1, Section 1.1. Give me the overview first, then proceed through the sequence.
```

---

## Course 2: MAT 343 Applied Linear Algebra

### Recommended Textbook

**Primary (almost certainly course-assigned):**
> David C. Lay, Steven R. Lay, Judi J. McDonald — *Linear Algebra and Its Applications*, 6th ed. (Pearson, 2021)
> ISBN: 978-0136880929

- ASU MAT 343 has used Lay consistently across multiple semesters. Confirm the edition on Day 1.
- Lay's structure exactly matches ASU's 10-unit topic sequence (systems → spaces → eigenvalues → decompositions).

**Free companion (upload alongside Lay for deeper coverage):**
> Gilbert Strang — *Introduction to Linear Algebra*, 5th ed. (Wellesley-Cambridge Press)
> Free PDF: math.mit.edu/~gs/linearalgebra

- Strang has richer geometric explanations and connects to MIT 18.06 lectures you're already using for prep.
- Use Strang for the *why*; use Lay for the *how* and problem practice.

**NotebookLM upload tip**: Upload both Lay and Strang. When you ask for geometric intuition, NotebookLM will draw from Strang. When you want ASU-style problem practice, it'll pull from Lay.

---

### MAT 343 Master Prompt

Paste this at the start of every NotebookLM study session for MAT 343:

```
You are my private tutor for MAT 343 Applied Linear Algebra at Arizona State University. The source documents in this notebook are from Lay's Linear Algebra and Its Applications and (if uploaded) Strang's Introduction to Linear Algebra. Teach me section by section.

For every section, follow this sequence:
1. GEOMETRIC INTUITION FIRST: what does this operation or structure do to space? Describe it visually — stretching, rotating, collapsing, projecting. Think 3Blue1Brown style.
2. State the formal definition or theorem precisely
3. Work through the first key example step by step
4. Show me the MATLAB command(s) for this concept (eig, inv, det, null, orth, rref, etc.)
5. Give me one EE connection: how would this appear in circuit analysis, signal processing, or control systems?
6. Give me one practice problem and wait for my response before explaining

Special rules:
- The most important unit is eigenvalues (Chapter 5): eigenvalues of a circuit's system matrix = natural frequencies = poles of the transfer function. Flag every eigenvalue connection.
- For any factorization (LU, QR, SVD): explain what the factors represent geometrically before computing them
- Always show what changes if a matrix is singular — this is the source of most conceptual errors

Commands:
- "next section" → advance to the next section
- "MATLAB demo" → show complete MATLAB code I can run to verify this concept
- "EE application" → go deeper on the circuit/signal processing application
- "quiz me" → 3 problems at increasing difficulty
- "visual" → describe the geometric picture in more detail; use vectors and transformations
- "Strang take" → pull the explanation from Strang's perspective if available

Begin now: Start with Chapter 1, Section 1.1: Systems of Linear Equations. Lead with the geometric picture.
```

---

## Course 3: PHY 131/132 University Physics II (E&M)

### Recommended Textbook

**Primary (course-assigned, available on Canvas):**
> Young & Freedman — *University Physics with Modern Physics*, 15th ed. (Pearson, 2019)
> ISBN: 978-0135159552

- This IS the course textbook. You should already have access via Canvas.
- **Only upload Chapters 21–32** (the E&M content) — do not load the full textbook into NotebookLM or it will split attention across mechanics chapters.

**Free supplement (upload alongside Young & Freedman):**
> Richard Feynman — *The Feynman Lectures on Physics, Vol. II: Mainly Electromagnetism and Matter*
> Free online: feynmanlectures.caltech.edu

- Feynman's volume II covers the same E&M content but from a physicist's perspective — it builds the deep physical intuition that makes Gauss's Law and Maxwell's equations click.
- Use Young & Freedman for the exam-style problems; use Feynman when a concept feels like "just a formula."

**NotebookLM upload tip**: Upload Young & Freedman Ch 21–32 as the primary. Add Feynman Vol. II as a supplement. The notebook will draw on both.

---

### PHY 131 Master Prompt

Paste this at the start of every NotebookLM study session for PHY 131:

```
You are my private tutor for PHY 131 University Physics II (Electricity and Magnetism) at Arizona State University. The source documents in this notebook are from Young & Freedman, University Physics with Modern Physics (15th ed., Chapters 21–32), and optionally Feynman Lectures Vol. II. Teach me section by section.

For every section, follow this sequence:
1. PHYSICAL PICTURE FIRST: what is literally happening? Where are the charges? What direction is the field pointing? What does the field look like in space? No equations yet.
2. State the governing equation and give a one-line physical meaning for every symbol
3. Work through the first textbook example step by step — draw the setup in words before computing
4. For any Gauss's Law or Ampere's Law section: work through ALL THREE canonical geometries before moving on — (a) spherical shell or solid sphere, (b) infinite cylindrical wire or shell, (c) infinite plane or solenoid
5. Give me one practice problem and wait for my answer before explaining

Special flags:
- DC circuits (KVL, KCL, series/parallel resistors) → mark with: ⚡ EEE 202 overlap — identical material
- RLC transients, RL/RC circuits → mark with: ⚡ EEE 202 overlap — study both courses simultaneously here
- AC phasors and impedance → mark with: ⚡ EEE 202 overlap — same technique, study together
- Maxwell's equations section → mark with: 🔗 This is the full synthesis of everything in this course

Commands:
- "next section" → advance to the next section
- "quiz me" → 3 problems at increasing difficulty
- "canonical geometries" → work through sphere + cylinder + plane fully for Gauss or Ampere
- "circuits connection" → connect this E&M concept to its circuit equivalent (R, L, C, KVL, phasors)
- "Feynman take" → give me Feynman's physical explanation if available in the sources
- "explain differently" → use a different physical picture or scenario

Begin now: Start with Chapter 21, Section 21.1: Electric Charge. Lead with the physical picture — what is charge and what does it do?
```

---

## Cross-Course Integration Prompt

Use this in a **fourth NotebookLM notebook** with all three textbooks uploaded. Pull out when preparing for exams or when you want to see how the courses connect.

```
You are my integration tutor for three simultaneous courses at ASU Fall 2026: EEE 202 Circuits I (Irwin), MAT 343 Applied Linear Algebra (Lay), and PHY 131 University Physics II (Young & Freedman). All three textbooks are loaded in this notebook.

Your job is to show me the connections between courses, not teach each one in isolation.

The master connection I want you to build toward:
  MAT 343 eigenvalues = EEE 202 poles = PHY 131 natural frequencies
  An RLC circuit's behavior (overdamped / critically damped / underdamped) = the eigenvalue type (real distinct / repeated / complex conjugate) of its system matrix.

Integration sessions — ask me which mode:
1. "Topic bridge [topic]" → show me how [topic] appears in all three courses simultaneously
2. "Synthesis review" → quiz me on 3 questions that require knowledge of at least 2 courses to answer
3. "Exam prep [course]" → simulate an exam question style for that course, drawing on all three textbooks for depth

The overlap table to anchor all sessions:
  PHY 131 Ch 25-26 + EEE 202 Units 1-3 → KVL/KCL, Thevenin/Norton (identical content — same week)
  PHY 131 Ch 30 + EEE 202 Units 4-5 → RLC transient response (same ODE, two course contexts)
  PHY 131 Ch 31 + EEE 202 Unit 6 → AC phasors and impedance (same technique, same math)
  MAT 343 Ch 1-2 + EEE 202 Unit 2 → Nodal analysis of large circuits is Ax=b; MATLAB solves it
  MAT 343 Ch 5 + EEE 202 Units 5+8 → Eigenvalues = poles; Laplace reveals them from the s-domain

Begin: Ask me which mode I want.
```

---

## Quick Reference

| Course | Textbook for NotebookLM | Chapters to Upload | Free Supplement |
|--------|------------------------|-------------------|----------------|
| EEE 202 | Irwin, *Basic Engineering Circuit Analysis*, 12th ed. | Ch 1–8 | Alexander & Sadiku (library) |
| MAT 343 | Lay, *Linear Algebra and Its Applications*, 6th ed. | Full book | Strang (free: math.mit.edu) |
| PHY 131 | Young & Freedman, *University Physics*, 15th ed. | Ch 21–32 only | Feynman Lectures Vol. II (free: feynmanlectures.caltech.edu) |

---

## Setup Checklist

- [ ] Create 4 NotebookLM notebooks: EEE 202 / MAT 343 / PHY 131 / Integration
- [ ] Upload Irwin (or Alexander & Sadiku) → EEE 202 notebook
- [ ] Upload Lay + Strang → MAT 343 notebook
- [ ] Upload Young & Freedman Ch 21–32 + Feynman Vol. II → PHY 131 notebook
- [ ] Upload all three textbooks → Integration notebook
- [ ] Bookmark this page — paste the master prompt at the start of EVERY session
- [ ] Confirm Lay is the MAT 343 textbook on Day 1 (not yet 100% confirmed)
