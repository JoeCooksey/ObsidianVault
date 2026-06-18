---
type: synthesis
title: "Build Your Own X Picks — Summer Deep Work"
created: 2026-06-17
updated: 2026-06-17
tags:
  - synthesis
  - projects
  - deep-work
  - ai
  - ee
  - embedded
status: developing
question: "From the build-your-own-x repo, which projects are the best daily deep-work build for Joe (freshman EE, EE×AI track) this summer — and which specific tutorial in each category?"
answer_quality: solid
related:
  - "[[Freshman Summer Project Plan (Tier List)]]"
  - "[[Andrej Karpathy]]"
  - "[[Physical AI Build Guide (Roadmap for Joe)]]"
  - "[[Linear Algebra for AI and Quant]]"
  - "[[ML Surrogate Modeling — Week 1 Daily Plan (Physical EE)]]"
  - "[[GGUF Format]]"
  - "[[llama.cpp]]"
  - "[[C and C++ Embedded Tutor Prompt (Power-Focused)]]"
  - "[[Deep Work]]"
  - "[[Research - Long-Term Compounding Daily Projects]]"
---

# Build Your Own X Picks — Summer Deep Work

Curated deep-work build plan drawn from [codecrafters-io/build-your-own-x](https://github.com/codecrafters-io/build-your-own-x), filtered for **fit with Joe's trajectory** (freshman EE at ASU, WBG power electronics, heavy current focus on the **EE × AI** intersection, wants embedded C/C++ depth and the linear-algebra foundation for ML).

`build-your-own-x` is strong deep-work fuel because each project produces a **real artifact** (working software, not "hours studied"), demands **sustained focus**, and teaches how everyday tools work underneath — knowledge that doesn't expire. The discipline: **read the concept, then implement it yourself before looking at the tutorial's code.** Don't transcribe — that's the line between deep work and busywork.

## The two picks

### Main project — Build your own Neural Network
**Best resource: Python — *Neural Networks: Zero to Hero* (Andrej Karpathy).**

This is the single highest-leverage project on the whole list *for Joe*, and it isn't close. It lands exactly on the EE×AI frontier his vault is oriented toward and forces the [[Linear Algebra for AI and Quant|linear algebra]] he flagged as his gap.

- The best NN teaching resource in any format — free, video + code, builds from one neuron up to a working GPT. Other entries teach *one* network; this teaches you to build the engine and understand *why*. (See [[Andrej Karpathy]].)
- **Path:** micrograd → makemore → nanoGPT, coding along.
- **Follow-up for the C / edge-AI payoff:** **SlowTorch** (rebuild PyTorch in pure Python) cements autograd + tensor machinery, then a tiny inference engine in C bridges toward [[GGUF Format]] / [[llama.cpp]] / TinyML.
- Feeds directly into [[ML Surrogate Modeling — Week 1 Daily Plan (Physical EE)]] and [[Physical AI Build Guide (Roadmap for Joe)]].

The "11 lines of Python" and "Implement from Scratch" entries are appetizers Zero to Hero makes redundant.

### Warm-up / embedded reinforcement — Build your own Emulator
**Best resource: C — *Write Your Own Virtual Machine* (LC-3).**

For Joe this beats the CHIP-8 options. It's pure C and one of the best-written tutorials in the repo. Building the **LC-3** teaching CPU means implementing the real **fetch → decode → execute** loop, registers, memory-mapped I/O, and condition flags — exactly how the STM32 he writes buck-converter firmware on works underneath. Direct transfer to embedded ([[C and C++ Embedded Tutor Prompt (Power-Focused)]]).

- **Runner-up (pick instead if you want graphics + a faster win):** C++ — *How to write an emulator (CHIP-8 interpreter)* (Laurence Muller). Simpler, pixels on screen in a weekend, more motivating; less "real CPU" than LC-3.
- **Defer:** Game Boy / NES emulators — great, but a big jump in scope. Do LC-3 or CHIP-8 first.

## Order & verdict

1. **Warm-up:** Write Your Own Virtual Machine (LC-3) in C — or CHIP-8 in C++ for graphics. A weekend → momentum + embedded fundamentals.
2. **Main summer project:** Neural Networks: Zero to Hero → SlowTorch → tiny C inference engine.

This combo hits both halves of the EE×AI thesis — the AI brain and the hardware it runs on.

**Skip for now** (off Joe's path): web browser, front-end framework, search engine, template engine.

A related option: CodeCrafters (the repo's maintainer) sells the same projects as paid, test-driven guided stages — useful only if Joe wants imposed structure; the free repo is plenty.
