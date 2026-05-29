---
type: concept
title: "Deep-Work Compounding Projects Tier List"
status: developing
created: 2026-05-29
updated: 2026-05-29
tags:
  - concept
  - deep-work
  - career
  - projects
  - tier-list
related:
  - "[[Deep Work]]"
  - "[[Compounding Daily Projects Tier List]]"
  - "[[EE Physical Side — Actionable Skill Plan]]"
  - "[[Verilog and FPGA Learning Path]]"
  - "[[ASU EE Mentorship Pathways]]"
  - "[[Sustainable Daily Practice (Streak Design)]]"
---

# Deep-Work Compounding Projects Tier List

Companion to [[Compounding Daily Projects Tier List]], for the **opposite design axis**. That list optimized for a low daily floor (one commit, automated DCA) so the streak survives bad days. This list optimizes for the thing Joe actually asked for: **projects whose difficulty is the point** — work that demands distraction-free concentration at the limit of his ability, and compounds *because* it's hard and most people won't do it. (Source: [[Deep Work]])

## Ranking lens

A deep project earns a high tier when:

1. **Focus intensity** — it genuinely requires 60–120 min uninterrupted blocks, not 5-minute touches. *High-Quality Work = Time × Intensity of Focus.*
2. **Trains a hard, rare skill** — it builds one of Newport's two core abilities: *master hard things fast* + *produce at an elite level*. (Source: [[Deep Work]])
3. **Trajectory fit** — pulls toward WBG power electronics / FPGA → LLNL/Sandia. (Source: [[EE High Income Action Plan]])
4. **Terminal artifact** — ends in something undeniable: a working board, a running core, a reproduced result, a ranked finish.

> [!note] How this relates to the first list
> The build-in-public repo and blog from the first list are the **container**; these deep projects are what *fills* it. Do the deep work, then make it visible. They're complementary, not competing.

## S-Tier — full-focus, on the bullseye of Joe's career

- **Build a real power converter end-to-end.** Spec → LTSpice → PCB (KiCad) → firmware → **closed-loop digital control** → bench validation. Candidates: a digitally-controlled synchronous buck, a bidirectional DC-DC, or an MPPT solar charger. This single project exercises circuit theory + [[Semiconductor Device Fundamentals]] + [[Control Systems]] + embedded C + lab skills — *the* portfolio crown jewel for power-electronics roles. Months of deep daily work. (See [[EE Physical Side — Actionable Skill Plan]], [[Silicon Carbide Power Electronics]].)
- **Build a CPU/SoC on an FPGA from scratch.** nand2tetris → then a real **RISC-V core**: datapath, pipeline, hazards, run actual programs. Daily HDL + verification with cocotb. Feeds the $175k FPGA track and Sandia directly. (See [[Verilog and FPGA Learning Path]].)
- **Reproduce a paper / pursue a real open question (apply to ASU FURI).** The deepest option and the strongest LLNL/Sandia signal — undergrad research with Ranjram/Ayyanar on WBG. Reading a paper until you can *rebuild its result* is maximal deep work. (See [[ASU EE Mentorship Pathways]].)

## A-Tier — deep, builds first-principles understanding

- **Build something hard from scratch to understand it.** Your own SPICE-style circuit simulator, your own neural net (Karpathy *Zero to Hero* → micrograd → nanoGPT), a from-scratch FFT/DSP library, or a Verilog simulator. The "build X from scratch" genre forces understanding no tutorial gives. (See [[AI Skills Roadmap for Electrical Engineers]].)
- **Work a hard textbook cover-to-cover — every problem.** Erickson *Fundamentals of Power Electronics* (the field bible), Razavi (analog), Ogata (control), or SICP. A daily problem set *with feedback* is textbook deliberate practice; it compounds into the theory moat that separates engineers. (See [[EE Topic Depth Priority Map]].)
- **Competitive deliberate practice to a ranked result.** Codeforces to a rating, Kaggle to a medal, or Putnam prep. Hard timed problems daily; some Kaggle finishes convert *directly* to interviews (a Facebook-competition winner moved into DeepMind). (See [[High Income Skills Tier List]].)

## B-Tier — deep but lower trajectory-fit or higher variance

- **Own a substantial open-source tool** (not one-off PRs) — architect + maintain a real package solving an EE problem (power-electronics design lib, thermal sim, gate-driver calculator). Sustained software architecture.
- **TinyML / embedded ML on real hardware** — train → quantize → deploy a model to an MCU/FPGA for a live sensing task; deep cross-stack work. (See [[AI Applications in Electrical Engineering]].)
- **Serious team systems project** — ASU Solar Car, or build a real battery-management system end to end. Deep integration + the team relationships compound too. (See [[EE Freshman Portfolio Strategy]].)

## How to sustain a *deep* project (different from the streak list)

Deep work breaks the 5-minute-floor model. Instead:

- **Pick ONE deep project at a time** — depth comes from concentration, not parallelism.
- **Protect a daily distraction-free block** (60–120 min, phone in another room) — *rhythmic* philosophy: same time every day. (Source: [[Deep Work]])
- **Ride ultradian rhythms** — schedule the block in a high-alertness window; one or two cycles, then real recovery. (See [[Sustainable Daily Practice (Streak Design)]], [[Three-Phase Day Framework]].)
- **Guard against shallow-work creep** — email/notifications/busywork are the default the *Principle of Least Resistance* pulls you toward; the deep block must be defended on purpose.

## Joe's recommended pick

Run **one S-tier project as the daily deep block** (the power converter is the highest-fit single choice), with **one A-tier "from scratch" build or textbook** as the secondary track for variety on lower-energy days. Make both visible via the repo/blog from [[Compounding Daily Projects Tier List]] — deep work that nobody sees doesn't build the career asset.
