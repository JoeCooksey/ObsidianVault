---
type: concept
title: "Python EE Project Ladder"
created: 2026-04-26
updated: 2026-04-26
tags:
  - python
  - electrical-engineering
  - projects
  - roadmap
  - portfolio
status: developing
related:
  - "[[Python EE Project Ladder - Phase 0-1]]"
  - "[[Python EE Project Ladder - Phase 2-3]]"
  - "[[Python EE Project Ladder - Phase 4-5]]"
  - "[[Python EE Project Ladder - Advanced Tracks]]"
  - "[[Python Self-Teaching Roadmap for EE]]"
  - "[[Python in Electrical Engineering]]"
  - "[[EE Freshman Portfolio Strategy]]"
---

# Python EE Project Ladder

A 20-project sequence from basic Python to professional EE automation. Each project introduces exactly one new Python/library concept while solving a real EE problem. Every project = one GitHub commit = portfolio artifact.

**Total time**: ~9–12 months at 3–5 hrs/week  
**Prerequisites**: Basic Python syntax (variables, loops, functions)  
**End state**: Can automate simulations, run instrument control, and perform DSP in Python at internship/entry-level standard

---

## Phase 0: Python + Math Foundations (Projects 1–3)
*New skills: functions, NumPy arrays, Matplotlib basics*

| # | Project | New Python Concept | EE Concept | Libraries |
|---|---------|-------------------|------------|-----------|
| 1 | **Ohm's Law Calculator** | Functions, f-strings, user input | V=IR, P=IV, unit conversions | None |
| 2 | **Resistor Network Analyzer** | NumPy arrays, loops over arrays | Series/parallel resistance, voltage divider | NumPy, Matplotlib |
| 3 | **E-Series Component Plotter** | np.logspace, log-scale axes | E12/E24 standard values, tolerance bands | NumPy, Matplotlib |

---

## Phase 1: DC and AC Circuit Analysis (Projects 4–6)
*New skills: linear algebra, complex numbers, ODE solving*

| # | Project | New Python Concept | EE Concept | Libraries |
|---|---------|-------------------|------------|-----------|
| 4 | **Nodal Analysis Matrix Solver** | np.linalg.solve, matrix construction | KCL, conductance matrix, node voltages | NumPy, Matplotlib |
| 5 | **AC Phasor Impedance Analyzer** | Python complex() type, complex arrays | Impedance Z=R+jX, phasor arithmetic, \|Z\|, ∠Z | NumPy, Matplotlib |
| 6 | **RC/RL/RLC Transient Simulator** | scipy.integrate.odeint, subplots | 1st/2nd order ODEs, ωn, damping ζ, step response | SciPy, NumPy, Matplotlib |

---

## Phase 2: Frequency Domain and DSP (Projects 7–10)
*New skills: FFT, filter design, frequency response*

| # | Project | New Python Concept | EE Concept | Libraries |
|---|---------|-------------------|------------|-----------|
| 7 | **Bode Plot Generator** | scipy.signal.bode, dB conversion | Transfer functions, poles/zeros, −20 dB/decade | SciPy, Matplotlib |
| 8 | **FFT Spectrum Analyzer** | np.fft.rfft, windowing functions | DFT, Nyquist theorem, spectral leakage, windowing | NumPy, Matplotlib |
| 9 | **FIR Lowpass Filter Designer** | scipy.signal.firwin, freqz, convolution | FIR design, cutoff frequency, linear phase | SciPy, NumPy, Matplotlib |
| 10 | **IIR Filter + Pole-Zero Plot** | scipy.signal.butter, tf2zpk, z-plane | Butterworth/Chebyshev tradeoffs, poles in z-plane | SciPy, NumPy, Matplotlib |

---

## Phase 3: Control Systems (Projects 11–13)
*New skills: python-control, state-space, feedback loops*

| # | Project | New Python Concept | EE Concept | Libraries |
|---|---------|-------------------|------------|-----------|
| 11 | **Transfer Function Analysis** | control.tf(), bode_plot(), root_locus() | Frequency response, stability, closed-loop response | python-control, Matplotlib |
| 12 | **PID Controller Tuning Simulator** | control.feedback(), parameter sweep loops | Ziegler-Nichols tuning, gain margin, phase margin | python-control, NumPy, Matplotlib |
| 13 | **Closed-Loop Buck Converter Sim** | scipy.integrate.solve_ivp, state equations | Buck converter state-space, PI current control, duty cycle | SciPy, NumPy, Matplotlib |

---

## Phase 4: Simulation Automation with PyLTSpice (Projects 14–16)
*New skills: subprocess control, SPICE netlist manipulation, Pandas*

| # | Project | New Python Concept | EE Concept | Libraries |
|---|---------|-------------------|------------|-----------|
| 14 | **RC Filter Parametric Sweep** | PyLTSpice SimRunner, asc_editor, raw file read | f=1/(2πRC) optimization, overlaid Bode responses | PyLTSpice, Matplotlib, NumPy |
| 15 | **Monte Carlo Tolerance Analysis** | PyLTSpice Monte Carlo, Pandas DataFrames | Component tolerances (1%/5%/10%), yield estimation, ±3σ | PyLTSpice, Pandas, Matplotlib |
| 16 | **Buck Converter Efficiency Sweep** | PyLTSpice .meas directives, Pandas export | Efficiency η=Pout/Pin, switching losses vs. load current | PyLTSpice, Pandas, Matplotlib |

---

## Phase 5: Instrument Control with PyVISA (Projects 17–19)
*New skills: SCPI commands, instrument automation, real-hardware data*

| # | Project | New Python Concept | EE Concept | Libraries |
|---|---------|-------------------|------------|-----------|
| 17 | **Power Supply + Multimeter I-V Sweep** | PyVISA ResourceManager, SCPI write/query | SCPI protocol, automated bench testing, I-V curves | PyVISA, Matplotlib |
| 18 | **Oscilloscope Waveform Capture** | PyVISA waveform binary decode, Pandas CSV | Waveform acquisition, timebase, Vpp/RMS extraction | PyVISA, NumPy, Pandas, Matplotlib |
| 19 | **Automated Amplifier Bode Plot** | Dual-instrument control loop, Pandas export | Automated frequency response: −3dB BW, gain (dB), phase | PyVISA, Pandas, NumPy, Matplotlib |

---

## Advanced Tracks (Choose One)

### Track A: FPGA Verification

| # | Project | New Python Concept | EE Concept | Libraries |
|---|---------|-------------------|------------|-----------|
| 20A | **cocotb RTL Testbench** | cocotb coroutines, clock gen, DUT signal drive | RTL verification, testbench methodology, pass/fail assertions | cocotb, Icarus Verilog |

### Track B: Power Electronics Data Analysis

| # | Project | New Python Concept | EE Concept | Libraries |
|---|---------|-------------------|------------|-----------|
| 20B | **Double Pulse Test Analyzer** | Pandas peak detection, scipy.signal event detection | Eon/Eoff switching energy, Qrr reverse recovery charge | Pandas, SciPy, Matplotlib |

---

## Library Unlock Order

```
Month 1-2:  Pure Python → NumPy → Matplotlib         (Projects 1-3)
Month 2-4:  SciPy (linalg, integrate, signal)          (Projects 4-10)
Month 4-6:  python-control                             (Projects 11-13)
Month 6-8:  PyLTSpice + Pandas                         (Projects 14-16)
Month 8-12: PyVISA                                     (Projects 17-19)
Month 12+:  cocotb (Track A) or advanced analysis (B)  (Project 20)
```

## GitHub Portfolio Structure

```
python-ee-projects/
├── phase0_basics/        P1-3
├── phase1_circuits/      P4-6
├── phase2_dsp/           P7-10
├── phase3_control/       P11-13
├── phase4_ltspice/       P14-16
├── phase5_instruments/   P17-19
└── advanced/             P20A or 20B
```

Each subdirectory = one README.md + scripts + sample output plots.

---

> See [[Python EE Project Ladder - Phase 0-1]] for full project specs (Phase 0–1)  
> See [[Python EE Project Ladder - Phase 2-3]] for full project specs (Phase 2–3)  
> See [[Python EE Project Ladder - Phase 4-5]] for full project specs (Phase 4–5)  
> See [[Python EE Project Ladder - Advanced Tracks]] for Track A/B specs
