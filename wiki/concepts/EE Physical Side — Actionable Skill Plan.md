---
type: concept
title: "EE Physical Side — Actionable Skill Plan"
created: 2026-04-19
updated: 2026-04-19
tags:
  - concept
  - domain/engineering
  - semiconductors
  - power-electronics
  - career
  - actionable-plan
status: developing
complexity: intermediate
domain: engineering
related:
  - "[[Wide Bandgap Semiconductors]]"
  - "[[Silicon Carbide Power Electronics]]"
  - "[[Gallium Nitride Power Electronics]]"
  - "[[Research - EE Physical Side Skills for Semiconductors and Power]]"
---
# EE Physical Side — Actionable Skill Plan

18-month structured plan to become hireable as a physical-side EE (semiconductors and power electronics). Designed for an EE student or early-career engineer. Milestones are concrete, verifiable, and interview-story-worthy.

## Skill Map

The physical side of EE breaks into five pillars:

```
1. Device Physics        — understand the silicon (and SiC/GaN)
2. Power Circuit Design  — topology fluency + magnetics
3. Simulation & Tools    — LTspice, MATLAB/Simulink, PCB CAD
4. Lab & Bench Skills    — DPT, probing, thermal measurement
5. Digital Control       — DSP implementation, closed-loop control
```

## Phase 1 — Foundations (Months 0–3)

**Goal**: Pass any screening question on device physics and basic converter operation.

| Week | Task | Resource |
|------|------|----------|
| 1–2 | P-N junction: depletion region, built-in potential, I-V equation | Neamen Ch. 1–3 |
| 3–4 | MOSFET: threshold voltage, triode/saturation, transfer characteristics | Neamen Ch. 8–9 |
| 5–6 | IGBT operation; why IGBT ≠ MOSFET at high voltage | Datasheet comparison: Si IGBT vs SiC MOSFET |
| 7–8 | Buck converter steady-state: duty cycle, volt-second balance, CCM vs DCM | Erickson Ch. 1–2 |
| 9–10 | Boost and flyback topology; isolated vs non-isolated | Erickson Ch. 3, 6 |
| 11–12 | LTspice simulation: simulate buck, boost, flyback from scratch | LTspice tutorial (Analog Devices YouTube) |

**Milestone**: Explain why SiC MOSFET has lower conduction and switching loss than Si IGBT at 650V+. Simulate a 12V→5V buck with real component models.

---

## Phase 2 — Core Power Design (Months 3–6)

**Goal**: Design a complete power stage on paper and in simulation.

| Week | Task | Resource |
|------|------|----------|
| 13–16 | Magnetics: core material, AL value, inductor winding, transformer design | Erickson Ch. 13–14; Wurth Electronics online calculator |
| 17–18 | Gate driver design: drive strength, propagation delay, Miller clamp | TI SLUA618; UCC21710 datasheet |
| 19–20 | WBG gate requirements: negative turn-off voltage, isolated gate driver, Rogowski coil | Wolfspeed gate driver app note |
| 21–22 | Double pulse test theory: what Eon, Eoff, Qrr mean and how to measure | Wolfspeed AN-1175 |
| 23–24 | Full converter design exercise: 400V→12V flyback, design to spec | Erickson + TI SLAC679 reference design |

**Milestone**: Complete a paper design for a 400V→12V, 50W flyback converter: turns ratio, core selection, gate driver selection, snubber sizing.

---

## Phase 3 — WBG Specialization (Months 6–12)

**Goal**: Be conversant in SiC/GaN device tradeoffs and have one complete WBG project.

| Month | Task | Resource |
|-------|------|----------|
| 7 | SiC MOSFET primer: body diode, CGD/CGS/CDS, cosmic ray immunity, threshold shift | Wolfspeed AN-011 |
| 7 | GaN HEMT primer: 2DEG, enhancement-mode vs depletion-mode, no body diode | EPC application notes |
| 8 | 800V EV fast charger architecture: totem-pole PFC → CLLC resonant DC-DC | IEEE TPEL 2023 paper on DCFC topologies |
| 8–9 | PCB layout rules for WBG: power loop inductance, Kelvin connection, decoupling | Infineon layout app note; Altium tutorial |
| 9–10 | Coursera Power Electronics Specialization — modules 3–5 | CU Boulder (audit free) |
| 11–12 | Build or heavily simulate a >1 kW WBG converter | Personal project or lab work |

**Milestone**: 20-minute technical presentation (even just to yourself on video) covering: device selection rationale, gate drive circuit, PCB layout choices, and switching loss calculation for a WBG converter.

---

## Phase 4 — Advanced (Months 12–18)

**Goal**: Become a T-shaped engineer with deep WBG + digital control specialty.

| Month | Task | Resource |
|-------|------|----------|
| 13–14 | TI C2000 F28379D: set up, PWM peripheral, ADC synchronization, PI loop | TI C2000 MotorControl SDK; SPRUI33 launchpad guide |
| 13–14 | Implement PI current control loop in fixed-point arithmetic | TI controlSUITE examples |
| 15 | EMC basics for power electronics: CM/DM noise, filter design, conducted emissions | Henry Ott *EMC for Power Electronics*; CISPR 32 overview |
| 15–16 | Thermal simulation: build a thermal model in SolidWorks or ANSYS; compare to datasheet Rth | ANSYS student license |
| 16–17 | AEC-Q101 qualification: understand HTGB, HTRB, THB, power cycling tests | AEC-Q101 standard (free download) |
| 17–18 | Mock technical interview: cover device physics, topology, PCB layout, bench story, control | Peer review or recorded self-interview |

**Milestone**: Technical portfolio with 3 project stories, each covering: problem → design choices → simulation/measurement result → what you'd do differently.

---

## Weekly Habit (Ongoing)

- **30 min/week**: Read one IEEE TPEL or APEC paper abstract — track trends in SiC/GaN
- **1 hr/week**: LTspice simulation of something you read about
- **Monthly**: One app note from a WBG manufacturer (Wolfspeed, Infineon, STMicro, EPC, GaN Systems)

## Key Tools to Learn (Priority Order)

1. **LTspice** — free, fast, the industry scratchpad
2. **Altium Designer** or **KiCad** — PCB design (KiCad free, Altium university license)
3. **MATLAB/Simulink** — system-level modeling; required at most power companies
4. **TI Code Composer Studio + C2000** — digital control DSP development
5. **ANSYS Icepak** or **SolidWorks Flow** — thermal simulation (use student license)

## Interview Readiness Checklist

- [ ] Can explain SiC vs GaN tradeoffs for a 400V vs 800V system
- [ ] Can derive switching loss from Eon + Eoff + frequency
- [ ] Can describe what a double pulse test measures and why
- [ ] Can identify 3 layout mistakes that increase switching noise
- [ ] Have completed one PCB design for a power converter
- [ ] Can explain thermal derating and why Tjmax ≠ operating temperature
- [ ] Have implemented or studied a PI control loop on a DSP
- [ ] Can name 2–3 WBG manufacturers and their flagship devices per market segment
