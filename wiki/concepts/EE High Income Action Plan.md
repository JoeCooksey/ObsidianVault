---
type: concept
title: "EE High Income Action Plan"
status: developing
created: 2026-04-22
updated: 2026-04-22
tags:
  - action-plan
  - career
  - electrical-engineering
  - income
  - skills
---

# EE High Income Action Plan

A Joe-specific, 4-phase roadmap to build the highest-income EE skills from ASU Year 1 through the LLNL/Sandia 2027 internship and beyond.

**North Star**: Power Electronics (WBG specialist) as primary track → FPGA and/or AI-for-EE as secondary skill stack → $150k+ within 5 years of graduation.

---

## Why This Order

The skill build sequence is: **foundation → power electronics → WBG specialization → second skill stack**. Each phase provides the prerequisites for the next. Skipping phases creates gaps that show up in interviews (e.g., trying to learn SiC gate driving without understanding MOSFET physics first).

The second skill stack (FPGA or AI/ML) is not a pivot — it's a multiplier. Engineers who can simulate converters AND write Python automation scripts AND set up test benches get significantly better offers than those who do only one.

---

## Phase 1 — Foundation Lock-In (Now → Month 6, Apr–Oct 2026)

**Goal**: Build the tools that make every future phase 2× faster. No EE courses yet at ASU — this is the exploitation window.

**Priority stack**:

| Skill | Action | Time Investment | Why Now |
|---|---|---|---|
| Python fluency | Complete Python for Everybody (Coursera, free) + NumPy + matplotlib | 40 hrs | Prerequisites for every data/control/simulation task |
| LTspice mastery | Complete 10-circuit ladder: divider → RC → RL → RLC → diode → op-amp → MOSFET → buck | 30 hrs | Already started; finish before EEE 202 |
| Git/GitHub portfolio | 3 repos: Python calculator, LTspice simulation output, Arduino LED | 10 hrs | Internship hiring filter by Year 2 |
| Breadboard + multimeter | Build 5 circuits: LED → voltage divider → RC filter → transistor switch → op-amp buffer | $50 + 15 hrs | Bench intuition; shows up in lab practical tests |
| MAT 265 mastery | Drill derivatives → V-I relations; solve RC/RL circuits analytically | ongoing | Foundation for EEE 202 Term 4A |

**Milestone**: By October 2026 — LTspice buck converter simulated, 3 GitHub repos live, Python script plotting RC step response, bench with multimeter capable.

---

## Phase 2 — Power Electronics Entry (Month 6–12, Oct 2026 – Apr 2027)

**Goal**: Build the foundational power electronics knowledge that opens the door to the WBG world. Run parallel to EEE 120 and ASU coursework.

**Textbook stack** (both in parallel from day 1):
- **Erickson & Maksimovic** — *Fundamentals of Power Electronics* (3rd ed.) — the Bible; work Chapters 1–7 (DC-DC basics, inductor/capacitor design, discontinuous mode)
- **Neamen** — *Semiconductor Physics and Devices* (4th ed.) — device physics foundation; Chapters 1–6 (energy bands → p-n junction → MOSFET)

**LTspice progression**:
- Buck converter with MOSFET model (import from TI/Wolfspeed .lib)
- Boost converter
- Flyback converter (isolated topology)
- Measure efficiency with `.meas` directive
- Monte Carlo on magnetic component tolerances

**Embedded basics** (parallel track):
- Arduino Uno → C programming basics (loops, pointers, I/O registers)
- STM32 Nucleo → GPIO + UART + ADC (bare-metal, no HAL)
- FreeRTOS task scheduling on STM32 (blink LED with 2 tasks)

**October 2026 action**: Apply to LLNL Engineering Summer Internship (applications open ~October; 2027 target)

**Milestone**: By April 2027 — Can explain CCM/DCM buck converter behavior, simulate Eon/Eoff from a datasheet-realistic gate drive, write a blinking LED FreeRTOS task on STM32.

---

## Phase 3 — WBG Specialization (Month 12–18, Apr 2027 – Oct 2027)

**Goal**: Be the rare EE undergraduate who can talk SiC/GaN fluently in a technical interview. This is what separates Joe from 95% of candidates at Wolfspeed, Onsemi, and LLNL.

**WBG study stack**:
- Wolfspeed application notes: C3M0060065D SiC MOSFET gate drive design guide (free PDF)
- Infineon SiC application notes: CoolSiC MOSFET gate driver requirements
- GaN Systems: "How to Design with GaN" application note series
- Double Pulse Test (DPT): understand Eon, Eoff, Qrr, Vds overshoot, Miller plateau — these are the interview litmus test

**PCB layout skills** (critical):
- KiCad: 4-layer board design
- Power loop inductance minimization (Kelvin source connection, tight commutation loop)
- Download Wolfspeed evaluation board Gerbers; study the layout decisions

**Digital control entry**:
- TI C2000 F28379D LaunchPad XL (~$40 on TI.com)
- Implement a simple PI controller on a buck converter (simulated in MATLAB first, then hardware)
- Read: TI application note SLAA370: "Digital Power Control Using C2000" (free)

**FURI Application** (April 2027, Year 2 Spring):
- Apply to ASU FURI program with a research proposal in power electronics or WBG simulation
- Target faculty working in power electronics or SiC characterization at ASU ECEE
- FURI publication → direct signal for NC State MS-WBGS and VT CPES applications

**Milestone**: By October 2027 — Can explain double pulse test setup, discuss SiC vs. GaN trade-offs in OBC vs. inverter application, have a C2000 PWM project on GitHub.

---

## Phase 4 — Second Skill Stack + Advanced Specialization (Month 18–24, Oct 2027 – Apr 2028)

**Goal**: Layer a second high-income skill on top of the WBG power foundation. Choose one of two tracks based on what clicked most in Phases 1–3.

### Track A: FPGA + Digital Design (recommended for Sandia/LLNL path)
- **Why**: Sandia National Lab (Livermore!) uses FPGA extensively for nuclear safety systems and test instrumentation. An EE student with both power electronics AND FPGA knowledge is essentially purpose-built for their needs.
- **How to start**: Xilinx Nexys A7 board ($200) → Verilog HDL basics → 4-bit counter → SPI interface → simple CPU → publish on GitHub
- **Resources**: Nandland.com (best free Verilog tutorials), Xilinx Vivado (free WebPACK license), FPGA-ASIC-Roadmap (GitHub: m3y54m)
- **Time to usable**: 150–200 hours to first FPGA project worth showing in an interview

### Track B: Python / AI for EE (recommended for tech-sector EV/startup path)
- **Why**: Tesla, Apple, and semiconductor startups value EE engineers who can write Python data pipelines, automate test benches, and apply basic ML to fault detection in power converters.
- **How to start**: PySpice (Python-based SPICE simulator) → pandas for test data analysis → sklearn for converter anomaly detection → deploy on GitHub
- **Resources**: PySpice documentation, scipy.signal for DSP, Coursera Andrew Ng ML specialization (most rigorous)
- **Time to usable**: 100–150 hours to first combined EE+Python project

### Both Tracks: Technical Communication
- Write one IEEE-style technical report per major project (3–4 pages, proper citations, circuit diagrams)
- Submit a paper to IEEE APEC student paper contest (senior year)
- Present at ASU FURI symposium

---

## Summary Timeline

```
Apr 2026  → Phase 1 START: Python + LTspice 10-circuit ladder + GitHub
Oct 2026  → LLNL/Sandia 2027 application opens — APPLY NOW
Oct 2026  → Phase 2 START: Erickson + Neamen + STM32 firmware
Apr 2027  → Phase 3 START: WBG app notes + DPT theory + KiCad
Apr 2027  → FURI application (Year 2)
Summer 2027 → Target: LLNL engineering internship or ASU virtual internship
Oct 2027  → Phase 4 START: FPGA Track A or Python/AI Track B
May 2028  → Year 3 milestone: 2 significant GitHub projects, FURI complete, 1 internship
Fall 2028  → Begin MS-WBGS (NC State) or VT CPES application process
```

---

## Parallel Tracks (No Phases — Do Continuously)

- **LinkedIn** — update monthly; add each new skill; EE headline formula: "EE Student @ ASU | Python + LTspice + Power Electronics | Seeking 2027 Summer Internship"
- **GitHub** — commit something every week, even small; consistency matters more than any single project
- **IEEE ASU Branch** — join power/energy technical committee; attend 1–2 meetings/month; warmest network for EE jobs
- **Reading** — *Deep Work* (Newport) on learning methodology; *Ego Is the Enemy* (Holiday) on staying focused during the long build

---

## The One-Line Priority Test

When choosing between two things to study: **"Which of these is more likely to help me pass a power electronics lab interview at LLNL or Wolfspeed in 18 months?"** If the answer is clear, do that first.

---

## Related Pages
- [[EE Specialization Salary Tier List]]
- [[High Income Skills Tier List]]
- [[EE Physical Side — Actionable Skill Plan]]
- [[EE Freshman Self-Study Stack]]
- [[EE Freshman Action Plans]]
- [[First Job Roadmap — Livermore Tri-Valley]]
- [[LTSpice Complete Skills Guide]]
- [[Wide Bandgap Semiconductors]]
- [[MS EE Programs Power Electronics Semiconductors]]
