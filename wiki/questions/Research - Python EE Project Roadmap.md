---
type: synthesis
title: "Research: Python EE Project Roadmap"
created: 2026-04-26
updated: 2026-04-26
tags:
  - research
  - python
  - electrical-engineering
  - projects
  - roadmap
status: developing
related:
  - "[[Python EE Project Ladder]]"
  - "[[Python EE Project Ladder - Phase 0-1]]"
  - "[[Python EE Project Ladder - Phase 2-3]]"
  - "[[Python EE Project Ladder - Phase 4-5]]"
  - "[[Python EE Project Ladder - Advanced Tracks]]"
  - "[[Python Self-Teaching Roadmap for EE]]"
  - "[[Python in Electrical Engineering]]"
  - "[[EE Freshman Portfolio Strategy]]"
sources:
  - "[[PyPedia EE with Python GitHub]]"
  - "[[Prasun Barua Python Circuit Analysis 2025]]"
  - "[[PySDR Python Filters Guide]]"
  - "[[Prasun Barua Python Power Electronics 2025]]"
  - "[[Heslip Labs Python LTSpice Tutorial]]"
---

# Research: Python EE Project Roadmap

## Overview

A 20-project ladder takes a learner from basic Python syntax to professional EE automation skills — each project teaches exactly one new Python concept while solving a real EE problem. The ladder spans 5 phases (basics → circuit analysis → DSP → control systems → automation) and ends with two advanced tracks (FPGA verification via cocotb, or power electronics data analysis). Total duration at 3–5 hrs/week: ~9–12 months.

## Key Findings

- **Libraries unlock in order**: Pure Python → NumPy → Matplotlib → SciPy → python-control → PyLTSpice → PyVISA. Each new library adds a tier of EE capability. (Source: [[PyPedia EE with Python GitHub]])
- **Matrix math = circuit solver**: Nodal analysis (KCL) reduces to a matrix equation Gv = I solvable with `np.linalg.solve()`. This is the single most powerful EE use of NumPy. (Source: [[Prasun Barua Python Circuit Analysis 2025]])
- **scipy.signal is a full EE lab**: FFT, FIR/IIR filter design, Bode plot data, poles/zeros, ODE solvers — one library replaces most MATLAB Signal Toolbox functionality for zero cost. (Source: [[PySDR Python Filters Guide]])
- **python-control = free MATLAB Control Toolbox**: `pip install control` → Bode plots, root locus, step response, gain margin/phase margin, pole-zero maps. Transfer function syntax mirrors MATLAB exactly. (Source: python-control docs)
- **PyLTSpice bridges design and simulation**: Parametric sweeps, Monte Carlo tolerance analysis, and efficiency curves all run from a Python loop — what would take hours manually runs in minutes. (Source: [[Heslip Labs Python LTSpice Tutorial]])
- **PyVISA is the professional ATE skill**: Oscilloscope waveform capture, power supply ramping, and automated frequency response characterization (Bode plot from real hardware) are all achievable with `pyvisa` and SCPI commands. (Source: [[Prasun Barua Python Power Electronics 2025]])
- **cocotb brings Python to FPGA verification**: RTL testbenches written in Python using cocotb are simulator-agnostic (Icarus Verilog, ModelSim, Verilator) and are used at industry ASIC houses — a directly relevant advanced skill. (Source: cocotb.org)
- **Every project should go on GitHub**: Each project in the ladder is a portfolio artifact. 20 sequential projects = 20 commits = a coherent portfolio story readable by an EE hiring manager.

## Key Entities

- [[python-control]]: Python Control Systems Library — free MATLAB Control Toolbox equivalent; Bode/rlocus/step response
- [[PyLTSpice]]: PyPI library for automating LTSpice parametric sweeps, Monte Carlo, and RAW file parsing
- [[PyVISA]]: Python VISA library for SCPI instrument control over USB/GPIB/Ethernet
- [[cocotb]]: Python-based RTL verification framework for FPGA/ASIC testbenches

## Key Concepts

- [[Python EE Project Ladder]]: The full 20-project sequenced roadmap
- [[Python in Electrical Engineering]]: Library ecosystem overview
- [[Python Self-Teaching Roadmap for EE]]: Phase-based timeline with months

## Contradictions

No major contradictions found. PySpice (an alternative SPICE interface) and spicelib (the underlying library for PyLTSpice) are sometimes confused — PyLTSpice is the higher-level wrapper and the correct tool for most automation tasks.

## Open Questions

- Best source for PyVISA tutorials with RIGOL oscilloscopes specifically (most common student scope)
- Whether pandapower (power systems) is a better Phase 5+ target than PyVISA for power-systems-track students
- How to set up PyVISA without NI-VISA on Windows (NI-VISA alternatives: pyvisa-py backend)

## Sources

- [[PyPedia EE with Python GitHub]]: PyPedia, 2024
- [[Prasun Barua Python Circuit Analysis 2025]]: Barua, April 2025
- [[PySDR Python Filters Guide]]: PySDR.org, 2025
- [[Prasun Barua Python Power Electronics 2025]]: Barua, April 2025
- [[Heslip Labs Python LTSpice Tutorial]]: Heslip Labs, 2024
