---
type: concept
title: "Power Electronics Deep Study Roadmap"
status: complete
created: 2026-05-09
updated: 2026-05-09
tags:
  - power-electronics
  - WBG
  - roadmap
  - self-study
  - electrical-engineering
  - GaN
  - SiC
---

# Power Electronics Deep Study Roadmap

> A research-track self-study guide for power electronics, calibrated for an ASU EE freshman who wants to be FURI-ready and outpace coursework by 2 years. Goes well beyond the [[EE Freshman Self-Study Stack]].

---

## Why Power Electronics Matters (Joe's Context)

- Your FURI targets (Ranjram — MHz magnetics + ML-CEMS; Ayyanar — EV/PV/WBG) both sit squarely in power electronics research
- The EV electrification wave + grid modernization = the most hiring-intensive domain in EE for the next 20 years
- WBG (GaN + SiC) is the frontier: 10× faster switching, 3× higher voltage, higher temp — everything is being redesigned
- Most undergrads don't open Erickson until grad school; getting there in Year 1–2 is a category-defining signal to PIs

---

## Phase 0 — Prerequisites (Before You Start)

You need these before the main textbooks make sense:

| Skill | Where to Get It |
|-------|----------------|
| Complex impedance (Z = R + jωL) | EEE 202 / any circuits textbook |
| Laplace transforms | EEE 202 / MIT OCW 18.03 |
| Basic op-amp circuits | EEE 202 labs |
| LTspice basics | [[Buck Converter LTspice Simulation]] — you already have this |
| C/C++ basics | [[EE Freshman Self-Study Stack]] |

---

## Phase 1 — Foundations (Months 1–4)

### Primary Textbook: Daniel Hart — *Power Electronics* (6th ed.)

**Why Hart first, not Erickson?** Hart is explicitly written for undergraduates; Erickson assumes graduate-level background. Hart builds the vocabulary Hart → Erickson transition is smooth.

**Chapter sequence:**
1. Ch. 2: Half-wave & full-wave rectifiers (AC→DC fundamentals)
2. Ch. 3: Half-wave & full-wave controlled rectifiers (thyristors, SCRs)
3. Ch. 6: DC-DC converters (Buck, Boost, Buck-Boost — the core)
4. Ch. 8: Inverters (DC→AC; needed for EV drives + solar)
5. Ch. 5: AC voltage controllers

### Parallel: MIT OCW 6.622 — Power Electronics (Spring 2023)
- Professor David Perreault's course, free online with lectures, problem sets, and solutions
- Complement Hart with these lectures — MIT-level rigor without grad school tuition
- URL: ocw.mit.edu/courses/6-622-power-electronics-spring-2023/

### LTspice Practice (Build as You Read)
- Simulate every converter topology from Hart in LTspice before moving on
- Sequence: ideal buck → buck with parasitics → boost → buck-boost → full-bridge
- Goal by end of Phase 1: can design a 12V→5V, 1A buck converter from scratch in LTspice (you already did this in [[Buck Converter LTspice Simulation]])

---

## Phase 2 — Graduate-Level Core (Months 4–10)

### Primary Textbook: Erickson & Maksimovic — *Fundamentals of Power Electronics* (3rd ed., 2020)

This is the bible. Every power electronics researcher has it. Prof. Erickson (CU Boulder) is one of the field's leading figures.

**Critical chapters for Joe's WBG track:**
- Ch. 1–3: Steady-state analysis of converters (averaging, small ripple approximation)
- Ch. 4: Switch realization (practical MOSFET/diode constraints)
- Ch. 7: AC equivalent circuit modeling (the most important chapter — canonical circuit model)
- Ch. 8: Converter transfer functions (Bode plots, loop gain)
- Ch. 9: Controller design (compensator design, PID, Type II/III)
- Ch. 13: Magnetic design (inductors + transformers — Ranjram's specialty)
- Ch. 14–16: Semiconductor devices (Si vs. SiC vs. GaN comparison)

**Companion resource:** Prof. Dragan Maksimovic's CU Boulder lectures are available on YouTube — search "Maksimovic power electronics CU Boulder."

### Coursera: Power Electronics Specialization (University of Colorado)
- 4-course specialization taught by Prof. Erickson's group
- Mirrors the textbook; includes graded simulations
- Free to audit; ~$50/month for certificates

---

## Phase 3 — WBG Deep Dive (Months 10–18)

### GaN-Specific Resources
- **Book**: *GaN and SiC Power Devices: From Fundamentals to Applied Design and Market Analysis* — Maurizio Di Paolo Emilio (2024)
- **Papers**: Search IEEE Xplore for "GaN HEMT power converter" — read 5 survey papers before reading design-specific papers
- **Devices to understand**: EPC eGaN FETs (enhancement-mode GaN); TI GaN ICs; Navitas GaNFast

### SiC-Specific Resources
- **Company training**: Wolfspeed (62% market share) has free online SiC design training at wolfspeed.com
- **STMicroelectronics**: SiC application notes + reference designs (Tesla Model 3 supply chain)
- **Book**: Chapter 3–6 of *Power Electronics Handbook* (Rashid, 4th ed.) — SiC and GaN chapters

### WBG Magnetics (Ranjram's Research Area)
- Ranjram's lab focuses on MHz-frequency magnetics — coreless and air-core inductors at megahertz switching frequencies
- Read: Ranjram's published papers via Google Scholar (search "Mike Ranjram magnetics")
- Key concept: at MHz frequencies, PCB trace inductors and coreless windings replace conventional ferrite cores

---

## Phase 4 — Digital Control (Months 12–24)

Essential for FURI with either Ranjram (ML-CEMS) or Ayyanar (digital control of EV converters).

### STM32 Digital Control
- Build on [[STM32 Digital Control for Buck Converter]]
- Expand to: PID in floating point → discrete-time z-domain design → state-space control → model predictive control
- Resource: *Digital Control of Switching Power Converters* — Martin Ordonez & Issa Batarseh (IEEE Press)

### MATLAB/Simulink for Power Electronics
- Simulink Power Systems Toolbox: simulate closed-loop converters with realistic switching
- ASU provides free MATLAB license — use it
- Goal: simulate a digitally controlled buck-boost with inner current loop + outer voltage loop

---

## Best YouTube Channels

| Channel | Focus | Quality |
|---------|-------|---------|
| **Phil's Lab** | PCB design + power electronics + firmware (STM32) | ★★★★★ |
| **EEVblog (Dave Jones)** | Measurement, troubleshooting, component-level analysis | ★★★★★ |
| **Texas Instruments Training** | Professional-grade application training (free) | ★★★★★ |
| **MIT OpenCourseWare** | 6.622 lectures (David Perreault) | ★★★★☆ |
| **Wolfspeed** | SiC/GaN application videos and design seminars | ★★★★☆ |
| **Robert Boylestad** | Basic electronics theory (complement to Hart) | ★★★☆☆ |
| **Great Scott!** | Beginner power projects; good for intuition building | ★★★☆☆ |

---

## Books Ranked by Phase

| Book | Phase | Level | Use |
|------|-------|-------|-----|
| *Power Electronics* — Daniel Hart | 1 | Undergrad | First pass through all topologies |
| *Fundamentals of Power Electronics* — Erickson & Maksimovic | 2 | Grad | Primary deep reference |
| *Power Electronics* — Ned Mohan (3rd ed.) | 2 | Grad | Alternative perspective; strong on drives |
| *GaN and SiC Power Devices* — Di Paolo Emilio | 3 | Grad/Research | WBG device-to-converter bridge |
| *Power Electronics Handbook* — Muhammad Rashid (ed.) | 3 | Reference | Encyclopedia-style reference |
| *Digital Control of Switching Power Converters* — Ordonez/Batarseh | 4 | Advanced | Digital control theory |

---

## Key Articles and Papers (Starter List)

1. Erickson, R. W. (1997). "Fundamentals of Power Electronics" — original seminal paper trail; read his IEEE papers on Fundamentals
2. Ranjram, M. et al. — search Google Scholar for "MHz-frequency power converter" + "coreless inductor"
3. IEEE COMPEL Conference papers — dedicated to power electronics control; good research-level reading
4. PowerAmerica Institute publications — WBG roadmap + industry perspective

---

## Milestones (Checkpoints)

| Milestone | Target Date | Signal |
|-----------|------------|--------|
| Complete Hart Ch. 2–3 + 6 | Month 2 | Can explain buck operation to anyone |
| LTspice: all 3 basic topologies simulated | Month 3 | Waveforms match theory |
| Complete Erickson Ch. 1–9 | Month 8 | Can read IEEE power electronics papers |
| STM32 closed-loop buck converter working | Month 10 | Hardware validates simulation |
| Read 5 Ranjram papers | Month 12 | FURI conversation prep complete |
| Complete Erickson Ch. 13 (magnetics) | Month 14 | Ready to contribute to Ranjram lab |

---

## See Also
- [[Buck Converter Theory and Design]]
- [[Buck Converter LTspice Simulation]]
- [[STM32 Digital Control for Buck Converter]]
- [[Wide Bandgap Semiconductors]]
- [[Silicon Carbide Power Electronics]]
- [[Gallium Nitride Power Electronics]]
- [[Mike Ranjram]]
- [[Raja Ayyanar]]
- [[Top Topics to Research — Master Guide]]
