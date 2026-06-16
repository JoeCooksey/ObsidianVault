---
type: concept
title: "Problem-Solving Practice Activities (Concrete Menu)"
created: 2026-06-16
updated: 2026-06-16
tags:
  - concept
  - problem-solving
  - practice
  - resources
status: developing
related:
  - "[[Problem-Solving Skill-Building Protocol]]"
  - "[[Research: Best Way to Develop Problem-Solving Skills]]"
  - "[[Deliberate Practice]]"
  - "[[Interleaving (Learning)]]"
  - "[[Most Self-Teachable High-Value Skills (Tier List for Joe)]]"
---

# Problem-Solving Practice Activities (Concrete Menu)

The actual places to go and problems to solve, in Joe's three domains. Run every item through the [[Problem-Solving Skill-Building Protocol|loop]]: **understand → struggle (timeboxed) → check & self-explain → compare a second similar problem → look-back post-mortem.** The platform is just the problem source; the *process* is what builds the skill.

> [!warning] The one rule that decides if this works
> Far transfer is weak ([[Near vs Far Transfer]]) — getting good at LeetCode makes you good at *LeetCode-shaped problems*. Pick the domains whose problems you actually want to be good at. For Joe that's **programming, math, and EE**.

## 1. Programming (the highest-feedback domain)

| Resource | What it's for | Start with |
|---|---|---|
| **NeetCode 150** (neetcode.io) | The curated gold-standard roadmap — 150 problems organized by *pattern* (two pointers, sliding window, binary search, trees, graphs, DP). | Do it **pattern by pattern**, not randomly. |
| **LeetCode** (leetcode.com) | Volume + company-tagged sets once you know the patterns. | Easy → Medium; skip Hard until Mediums feel routine. |
| **CSES Problem Set** (cses.fi) | Free, deeper algorithmic CS problem solving beyond interviews. | "Introductory Problems" (25), then Sorting & Searching. |
| **Codeforces** (timed contests) | The *think-under-pressure* skill — solving novel problems on a clock. | Div 3 / Div 4 rounds, virtual contests. |
| **Advent of Code** (Dec, free) | Fun, varied, story-based — great for breadth. | Any past year, days 1–10. |
| **Exercism** (mentored) | Language fluency + human feedback (real feedback loop). | A track in Python or C++. |

**Pattern emphasis (the deep structure to extract):** two pointers, sliding window, prefix sum, binary search, BFS/DFS, backtracking, dynamic programming, heaps, union-find. Naming the pattern after each problem *is* the [[Analogical Encoding (Comparing Cases)|schema-building]] step.

## 2. Mathematics (builds the rawest reasoning)

| Resource | What it's for | Start with |
|---|---|---|
| **Project Euler** (projecteuler.net) | Number-theory problems that need *math insight + a program* — perfect for an EE/programmer. | Problems 1–50, in order. |
| **Art of Problem Solving** (AoPS) | Competition-math training; the deep end of elementary problem solving. | *Getting Started with Competition Math*, then AoPS Vol. 1. |
| **Brilliant.org** | Guided, interactive, low-friction daily reps. | Daily problems + a logic/number-theory course. |
| **"How to Prove It"** (Velleman) | The **proof** skill — how to construct and verify an argument. | Work the exercises with pen, not just read. |
| **Putnam archive** (Kedlaya's site) | Hard, beautiful problems once the above feel easy. | One problem; spend 30+ min before peeking. |

## 3. Electrical Engineering (your applied moat)

| Resource | What it's for | Start with |
|---|---|---|
| **Textbook end-of-chapter problems** | Where EE problem-solving skill actually lives. | **Sedra & Smith** (microelectronics), **Nilsson/Irwin** (circuits), **Razavi** (analog). |
| **All About Circuits** (worksheets) | Free graded circuit-analysis practice. | DC → AC analysis worksheets. |
| **Falstad / LTSpice "predict-then-sim"** | Build a circuit, **predict** the behavior, then simulate to check — a tight feedback loop. | Pick a node, predict V/I, verify. See [[LTSpice Complete Skills Guide]]. |
| **Your STM32G4 buck project** | The ultimate applied problem set — real bugs, real constraints. | [[Project - Digitally Controlled Synchronous Buck Converter]]. |

## 4. Cheap daily reps (low cost, modest transfer)

- **Pólya's own problems** in *[[Polya 1945 — How to Solve It|How to Solve It]]* — practice the method on the source.
- **Fermi estimation** — "how many X in Y?" back-of-envelope; trains decomposition + assumption-making.
- ⚠️ **Logic puzzles / riddles / brain-training apps** — fun, but low transfer to real domains ([[Near vs Far Transfer]]). Treat as entertainment, not training.

## A concrete week (interleaved, ~1 hr/day)

Mixing domains is deliberate — [[Interleaving (Learning)|interleaving]] builds the skill of *choosing the right method*.

- **Mon** — 2 NeetCode problems (one pattern), name the pattern after each.
- **Tue** — 1 Project Euler problem, timeboxed 25 min before checking.
- **Wed** — 1 EE textbook section's problems (or a Falstad predict-then-sim).
- **Thu** — 1 LeetCode Medium in the same pattern as Monday → *compare the two*.
- **Fri** — 1 Codeforces virtual problem (under the clock).
- **Sat** — proof exercise from *How to Prove It*, or AoPS section.
- **Sun** — review your **"key moves" log**; re-solve one problem from earlier in the week from a blank page ([[Active Recall (Retrieval Practice)]]).

> [!tip] Non-negotiable
> Keep a one-line-per-problem **"key moves" log** (the insight that cracked it). That log — not the problem count — is the record of skill being built.
