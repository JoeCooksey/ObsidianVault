---
type: concept
title: "EE Freshman Self-Study Stack"
status: developing
created: 2026-04-19
updated: 2026-04-19
tags:
  - electrical-engineering
  - self-study
  - skills
  - freshman
  - tools
---

# EE Freshman Self-Study Stack

The tools and skills an EE freshman should self-teach *before* coursework formally introduces them. Learning these early creates compounding advantage at every subsequent course and internship.

## Tier 1 — Start Immediately (Year 1)

### LTspice (Circuit Simulator)
- Free SPICE simulator from Analog Devices (Windows/Mac)
- Industry-standard for analog circuit simulation
- Required in EEE 202 (Circuits I) at ASU
- Self-study path: RC circuits → RL → RLC → op-amp basics → filter frequency response
- 10 hours of self-study before Circuits I gives massive advantage

### Python Basics
- Scripting language used heavily in EE data analysis, automation, signal processing
- Not formally taught until upper-division at most schools
- Minimum viable: variables, loops, functions, lists, matplotlib for plotting
- Resource: Python.org tutorial + "Automate the Boring Stuff" (free online)

### Breadboarding + Multimeter
- Physical skill: build circuits on a solderless breadboard
- Multimeter fluency: measure voltage, current, resistance, continuity
- $30 breadboard kit + $20 multimeter from Amazon is sufficient
- Build 5 progressively complex circuits: LED blink → voltage divider → RC filter → transistor switch → op-amp buffer

### Git + GitHub
- Version control is expected at every EE internship
- Self-teach: git init, add, commit, push, pull, branch, README
- Goal: a public GitHub profile with at least one pinned project before applying to internships
- Platforms: GitHub Student Developer Pack (free for students)

## Tier 2 — Build in Year 2 (Before EEE 202)

### MATLAB Basics
- Required in EEE 202 (Circuits I) and EEE 203 (Signals & Systems)
- ASU provides free MATLAB access via student license
- Minimum: matrix operations, plotting, Laplace/Fourier transforms via symbolic toolbox
- MathWorks has free "MATLAB Onramp" course (2 hours)

### Arduino / Embedded C
- Bridges gap between circuit theory and real hardware
- Teaches GPIO, PWM, serial communication, sensor reading
- C/C++ syntax directly applicable to CSE 100/110 coursework
- Build 3–5 projects: LED blink, servo control, sensor display, simple FSM
- Document each project on GitHub

### Oscilloscope Basics
- Learn conceptually via PhET simulations or YouTube before first PHY 132 lab
- Key operations: set trigger, measure frequency/amplitude, probe compensation
- Most EE labs use Tektronix or Keysight 2-channel DSOs

## Tier 3 — Long-Term (Sophomore+)

### Verilog / HDL
- EEE 120 may use schematic-only digital design; upper-division uses Verilog
- Learn Verilog basics before taking digital systems courses

### PCB Design (KiCad)
- Free, open-source PCB layout tool
- Relevant after Circuits I; needed for any hardware project beyond breadboard

### Control Systems Foundation
- 69% job growth YoY (Siemens hiring survey)
- Feedback loops, PID, transfer functions — show up in junior year
- Plant early by understanding what "closed-loop control" means

## Related
- [[ASU EE Year 1-2 Curriculum Map]]
- [[Research - First-Year ASU EE Skills]]
- [[EE Physical Side — Actionable Skill Plan]]
- [[EE Freshman Portfolio Strategy]]
