---
type: concept
title: "EE Topic Depth Priority Map"
created: 2026-04-27
updated: 2026-04-27
tags:
  - EE
  - learning
  - curriculum
  - first-year
  - career
status: developing
---
# EE Topic Depth Priority Map

A prioritized depth ladder for a first-year EE student targeting WBG power electronics. Each level should be worked before going deep into the next — the stack is ordered by dependency and leverage.

## The 6-Level Leverage Stack

### Level 1 — Circuit Theory (Start Now)
**Why first**: Every EE course assumes this. Can't do EEE 202 without it. LTSpice + Python projects already use it implicitly — making it explicit multiplies both.
**Key topics**: KVL/KCL, nodal/mesh analysis, Thevenin/Norton, RC/RL/RLC transients, AC phasors, impedance, power in AC circuits, resonance
**Best resources**:
- Nilsson & Riedel "Electric Circuits" (ASU standard)
- Hayt & Kemmerly "Engineering Circuit Analysis" (more intuitive)
- LTSpice 10-circuit ladder (do in parallel with theory)
**Joe milestone**: Solve every node voltage in the 10-circuit LTSpice ladder analytically AND verify via simulation

### Level 2 — Digital Logic and Boolean Algebra (Start Now)
**Why second**: EEE 120 Digital Design is Joe's first official EE course; arriving fluent changes the experience from struggle to mastery; foundational for the FPGA track ($175k avg)
**Key topics**: Boolean algebra, De Morgan's laws, K-maps, combinational circuits (adders, MUX, decoders), D flip-flops, counters, finite state machines, intro Verilog
**Best resources**:
- Morris Mano "Digital Design" (standard textbook)
- Neso Academy YouTube series (free, comprehensive)
- HDLBits.01xfpga.com (Verilog interactive practice)
**Joe milestone**: Write a Moore FSM for a vending machine in Verilog → simulate → push to GitHub

### Level 3 — Semiconductor Device Physics (Year 1 / Concurrent with MAT 267)
**Why third**: Direct path to WBG understanding; cannot understand SiC/GaN without p-n junction physics, MOSFET channel formation, and gate oxide behavior; Neamen is ASU standard
**Key topics**: p-n junction, diode I-V curve, BJT modes, MOSFET operation (threshold voltage, channel pinch-off, drain current equation), power MOSFET body diode, IGBT basics, SiC/GaN differences from Si
**Best resources**:
- Neamen "Semiconductor Physics and Devices" (ASU standard)
- Sedra & Smith "Microelectronic Circuits" (more design-oriented)
- All About Circuits — Power Semiconductors (free reference)
**Joe milestone**: Interpret a SiC MOSFET datasheet (Rds_on, Vth, Ciss, Qg, Qrr) → simulate switching transient in LTSpice with real Wolfspeed model

### Level 4 — Signals and Systems / Laplace Transform (Year 2)
**Why fourth**: Requires Calc 2 + DiffEQ foundation (MAT 266 + MAT 275); this is where EE math goes from "solving circuits" to "understanding all linear systems"
**Key topics**: Laplace Transform, inverse Laplace, transfer functions, poles and zeros, Bode plots, Fourier Transform, Fourier Series, convolution, impulse response, Z-transform
**Best resources**:
- Lathi "Linear Systems and Signals" (best for self-study; heuristic approach)
- MIT OpenCourseWare 6.003 (full course, free)
- 3Blue1Brown "But what is the Fourier Transform?" (intuition first)
**Joe milestone**: Derive transfer function of an RC filter → plot Bode plot analytically → verify with scipy.signal.bode() in Python

### Level 5 — Control Systems and Feedback (Year 2–3)
**Why fifth**: Requires Signals/Laplace first (transfer functions are the language of control); 69% YoY LinkedIn job growth; used in every power converter PI control loop
**Key topics**: Open/closed loop systems, PID control, root locus, Bode stability margins (gain/phase margin), Routh-Hurwitz criterion, lead/lag compensators, state-space representation
**Best resources**:
- Ogata "Modern Control Engineering" (standard)
- python-control library (`pip install control` — free MATLAB)
- Brian Douglas YouTube control series (best video explanations)
**Joe milestone**: Design a PI controller for a buck converter → verify gain/phase margins with python-control → port to TI C2000 firmware

### Level 6 — Electromagnetics (Year 2 / EEE 340 Prep)
**Why sixth**: Requires Calc 3 (MAT 267) and circuits background; hardest EE topic but essential for power loop design, transformer physics, PCB layout, and RF
**Key topics**: Electric field, Gauss's Law, magnetic field, Faraday's Law, Ampere's Law, Biot-Savart, electromagnetic induction, Maxwell's equations in integral and differential form, transmission lines
**Best resources**:
- Hayt & Buck "Engineering Electromagnetics" (ASU standard)
- MIT OCW 6.007 (electromagnetism videos)
- PBS Space Time electromagnetism episodes (intuition building)
**Joe milestone**: Derive the inductance of a toroid → calculate skin depth at a given frequency → explain PCB power loop inductance using Biot-Savart

## Year-by-Year Depth Target

| Year | Primary Depth Target | Secondary Target |
|------|----------------------|-----------------|
| Year 1 (now) | Circuit Theory + Digital Logic | Python/LTSpice projects |
| Year 1–2 | Semiconductor Devices | Breadboard + Arduino C |
| Year 2 | Signals & Systems / Laplace | STM32 + FreeRTOS intro |
| Year 2–3 | Control Systems | python-control converter projects |
| Year 3+ | Electromagnetics | WBG device physics deep dive |

## The Key Insight: Leverage Is Not Equal Across Topics

Most first-year students spread effort across all topics equally. The highest-ROI approach:
- **Circuit Theory** — go very deep; it multiplies everything else
- **Signals/Laplace** — go very deep; unlocks systems-level thinking
- **Semiconductor Devices** — go deep for Joe's WBG specialization
- **Control, EM** — go competent first, then deepen as you specialize

The most common first-year EE mistake: spending Year 1–2 energy memorizing Electromagnetics before building fluency in Circuits + Signals. The stack exists for a reason.

## Related Concepts
- [[Circuit Theory Fundamentals]]
- [[Signals and Systems — Laplace and Fourier]]
- [[Semiconductor Device Fundamentals]]
- [[Digital Logic and Boolean Algebra]]
- [[Calculus in Electrical Engineering]]
- [[Differential Equations in Electrical Engineering]]
- [[Electromagnetism Foundations for EE]]
- [[EE Freshman Self-Study Stack]]
- [[EE Freshman Action Plans]]
- [[Research — EE Deep Learning Topics for First-Year Students]]
