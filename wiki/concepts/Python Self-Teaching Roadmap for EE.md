---
type: concept
title: "Python Self-Teaching Roadmap for EE"
status: developing
created: 2026-04-24
updated: 2026-04-24
tags:
  - python
  - self-teaching
  - roadmap
  - electrical-engineering
  - programming
  - signal-processing
  - control-systems
---

# Python Self-Teaching Roadmap for EE

A phased, Joe-specific roadmap for learning Python from scratch through professional EE-grade skills. Total timeline: **9–14 months** of consistent part-time study (~3–5 hrs/week). Year 1 is the exploit window — zero EE courses at ASU means maximum available time for this.

---

## Phase 0 — Python Fundamentals (Month 1–2, 3–5 hrs/wk)

**Goal**: Write real Python programs from scratch. No copy-pasting tutorials — write it yourself.

### What to learn
- Variables, data types (int, float, str, list, dict, tuple)
- Control flow: `if`/`elif`/`else`, `for` loops, `while` loops
- Functions: define, parameters, return values
- String formatting (`f"The voltage is {v:.2f} V"`)
- List comprehensions (`[x**2 for x in range(10)]`)
- File I/O: reading CSV files (`open()`, then upgrade to pandas)
- Basic error handling: `try/except`
- Classes and objects (basics only — understand `self`, `__init__`)

### Resources (in order)
1. **Automate the Boring Stuff with Python** (automatetheboringstuff.com) — free online. Read Ch. 1–8. The most readable intro textbook that exists.
2. **Python.org official tutorial** — supplement for any confusion on syntax.
3. **Real Python** (realpython.com) — excellent short articles for intermediate gaps.

### Environment setup
1. Download Python 3.12+ from python.org
2. Install VS Code + Python extension (IntelliSense, debugger)
3. Install Jupyter Lab: `pip install jupyterlab` → run `jupyter lab` for interactive coding

### Milestones
- [ ] Written a function from scratch (not copied) and tested it
- [ ] Built a simple calculator program from scratch
- [ ] Read a CSV file and printed its contents
- [ ] Written a list comprehension and understood it
- [ ] Debugged a real error using VS Code's debugger

### Joe's first EE project
**Ohm's Law calculator**: `V = I * R` — write a Python script that takes voltage and resistance as input, calculates current, prints it formatted to 3 decimal places. Trivial but confirms you can write from scratch. Push to GitHub.

---

## Phase 1 — NumPy, Matplotlib, SciPy Basics (Month 2–3, 3–5 hrs/wk)

**Goal**: Plot circuits. Understand FFT. This is Signals & Systems in Python.

### Install
```bash
pip install numpy matplotlib scipy pandas
```

### NumPy essentials
```python
import numpy as np
t = np.linspace(0, 1, 10000)        # 10,000 time points from 0 to 1 second
f = 60                               # 60 Hz signal
v = 120 * np.sqrt(2) * np.sin(2*np.pi*f*t)  # US mains voltage waveform
print(f"Peak: {v.max():.1f} V, RMS: {np.sqrt(np.mean(v**2)):.1f} V")
```
This is MAT 266 integration and EEE 203 waveform analysis in one block.

### Matplotlib essentials
```python
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 4))
plt.plot(t[:500], v[:500])  # plot first 500 points
plt.xlabel('Time (s)'); plt.ylabel('Voltage (V)')
plt.title('60 Hz Mains Voltage'); plt.grid(); plt.show()
```

### SciPy basics
```python
from scipy import signal
# RC low-pass filter: H(s) = 1/(RCs + 1)
R, C = 1e3, 1e-6  # 1 kΩ, 1 µF → cutoff 159 Hz
sys = signal.TransferFunction([1], [R*C, 1])
w, mag, phase = signal.bode(sys)  # Bode plot data
```

### Milestones
- [ ] Plotted a sine wave at a chosen frequency
- [ ] Calculated RMS of a sine wave numerically and verified analytically
- [ ] Plotted a Fourier series approximation of a square wave (sum of harmonics)
- [ ] Plotted an RC filter Bode plot and compared to LTSpice output
- [ ] Read oscilloscope CSV data from a real or simulated experiment and plotted it

---

## Phase 2 — Signal Processing + Control Systems (Month 3–5, 3–5 hrs/wk)

**Goal**: Design filters and controllers. This is EEE 203 + EEE 350 (Feedback Control) in Python.

### Signal processing with SciPy
```python
from scipy import signal

# FFT — find frequency content of a noisy signal
noisy = v + 0.1*np.random.randn(len(t))
freqs = np.fft.rfftfreq(len(t), d=1/10000)  # sample rate 10 kHz
fft_mag = np.abs(np.fft.rfft(noisy)) / len(t)
plt.plot(freqs[:500], fft_mag[:500])  # shows 60 Hz spike clearly

# Design a 500 Hz low-pass Butterworth filter
b, a = signal.butter(4, 500, btype='low', fs=10000)
filtered = signal.filtfilt(b, a, noisy)  # zero-phase filtering
```

### Control systems — python-control
```bash
pip install control
```

```python
import control

# Plant: first-order DC motor model
Km = 10; tau = 0.1  # motor gain, time constant
plant = control.tf([Km], [tau, 1])

# PI controller
Kp, Ki = 2, 20
C = control.tf([Kp, Ki], [1, 0])  # Kp + Ki/s

# Closed-loop analysis
open_loop = C * plant
closed_loop = control.feedback(open_loop)

# Verify stability margins
gm, pm, _, _ = control.margin(open_loop)
print(f"Gain margin: {gm:.1f} dB, Phase margin: {pm:.1f}°")

control.bode(open_loop, title='Open Loop Bode')
T, yout = control.step_response(closed_loop)
plt.plot(T, yout); plt.title('Closed-Loop Step Response')
```

### Projects at this phase
1. **Filter design project**: Design a 60 Hz notch filter (to remove power line noise from a measurement signal). Implement with SciPy. Verify the notch with an FFT before and after.
2. **PI controller design**: Model a simple DC-DC converter plant (first-order) in python-control. Design a PI controller. Verify phase margin > 45°. Plot step response.

### Milestones
- [ ] Used FFT to identify dominant frequencies in a signal
- [ ] Designed and applied a Butterworth low-pass filter
- [ ] Designed a PI controller in python-control
- [ ] Verified gain margin and phase margin on a Bode plot
- [ ] Closed-loop step response looks correct (no ringing, fast settle)

---

## Phase 3 — PyVISA Instrument Control + PyLTSpice Automation (Month 5–8, 3 hrs/wk)

**Goal**: Automate the bench. This is what separates test automation engineers from manual bench workers.

### PyVISA — if you have access to equipment
```bash
pip install pyvisa pyvisa-py
```

Keysight provides a free **Keysight IO Libraries Suite** virtual instrument (KeySight BenchVue) with simulated instruments — lets you practice PyVISA with no real hardware.

```python
import pyvisa
rm = pyvisa.ResourceManager('@py')  # pure Python backend
resources = rm.list_resources()
print(resources)  # lists all connected instruments

psu = rm.open_resource(resources[0])
psu.write('*RST')                  # reset to defaults
psu.write('VOLT 5.0')             # 5 V output
psu.write('OUTP ON')              # turn on
meas = float(psu.query('MEAS:VOLT?'))
print(f"Measured: {meas:.4f} V")
psu.write('OUTP OFF')
psu.close()
```

**SCPI** (Standard Commands for Programmable Instruments) is the language every modern bench instrument speaks. Key commands: `*IDN?` (identify instrument), `*RST` (reset), `MEAS:VOLT?` (measure voltage), `OUTP ON/OFF`.

### PyLTSpice automation
```bash
pip install PyLTSpice
```

```python
from PyLTSpice import LTspice

lt = LTspice('my_buck_converter.asc')

# Sweep duty cycle from 30% to 70% in 5% steps
results = []
for duty in [0.3, 0.35, 0.4, 0.45, 0.5, 0.55, 0.6, 0.65, 0.7]:
    lt.set_component_value('Vpwm', f'PULSE(0 12 0 10n 10n {duty/100e3} {1/100e3})')
    lt.run()
    trace = lt.get_trace('V(out)')
    v_avg = trace.get_wave('V(out)').mean()
    results.append((duty, v_avg))
    
# Plot duty cycle vs output voltage
plt.plot([d for d,v in results], [v for d,v in results])
plt.xlabel('Duty Cycle'); plt.ylabel('Vout (V)'); plt.title('Buck: Vout vs D')
```

### Milestones
- [ ] Listed connected instruments via PyVISA (even if simulated)
- [ ] Sent a SCPI command and read back a measurement
- [ ] Wrote a Python sweep that changes an LTSpice component value in a loop
- [ ] Generated a parametric simulation plot from Python (no manual LTSpice clicking)

---

## Phase 4 — Advanced EE Python (Month 9–14, optional, 2–3 hrs/wk)

**Goal**: Professional-grade skills. Pick based on career track.

### Track A — FPGA Verification (cocotb)
Relevant if pursuing Track A (FPGA/Sandia) from the [[EE High Income Action Plan]]:
```bash
pip install cocotb
```
Write Python testbenches for VHDL/Verilog HDL. Works with most simulators (Icarus, ModelSim, Xcelium). Skills directly complement Verilog/VHDL knowledge.

### Track B — Power System Simulation (pandapower)
Relevant for grid-scale power electronics, utility, or power systems:
```bash
pip install pandapower
```
pandapower is an open-source Python library for power flow, short-circuit, and OPF analysis. Used for distribution network analysis, microgrid simulation, renewable integration studies.

### Track C — ML for EE (scikit-learn)
Relevant for predictive maintenance, fault detection, data-driven control:
```bash
pip install scikit-learn
```
Train a classifier to detect motor bearing fault from vibration FFT features. This is the "ML for industrial systems" use case that's growing fast in 2026.

### Milestones (pick your track)
- [ ] Track A: Passed a simple counter testbench with cocotb
- [ ] Track B: Ran a power flow analysis on a small network model
- [ ] Track C: Built a simple fault classifier from waveform features

---

## Complete Resource List

| Resource | Format | Cost | When |
|----------|--------|------|------|
| Automate the Boring Stuff with Python | Book (free online) | Free | Phase 0 |
| Real Python (realpython.com) | Articles | Free | All phases |
| NumPy documentation | Docs | Free | Phase 1 |
| SciPy documentation | Docs | Free | Phase 1–2 |
| python-control documentation + examples | Docs + GitHub | Free | Phase 2 |
| "Python for Engineers" — Hans-Petter Halvorsen | Free PDF | Free | Phase 1–2 |
| PyVISA documentation | Docs | Free | Phase 3 |
| PyLTSpice GitHub | GitHub | Free | Phase 3 |
| cocotb documentation | Docs | Free | Phase 4A |

### YouTube channels
- **3Blue1Brown** — Linear Algebra playlist (essential for understanding NumPy operations at a deeper level; also understand what `np.linalg.solve()` is doing)
- **Socratica** — best Python basics videos (short, precise)
- **sentdex** — Python for data science (NumPy/Matplotlib heavy)
- **Brian Douglas** — Control systems theory (perfect companion to python-control work)

---

## Timeline Summary

| Month | Phase | Key output |
|-------|-------|-----------|
| 1–2 | Phase 0: Python basics | Write programs from scratch; GitHub repo live |
| 2–3 | Phase 1: NumPy/Matplotlib/SciPy | RC filter Bode plot in Python matches LTSpice |
| 3–5 | Phase 2: Signal processing + control | FFT filter + PI controller designed |
| 5–8 | Phase 3: PyVISA + PyLTSpice | Automated LTSpice sweep; instrument control basics |
| 9–14 | Phase 4: Advanced | Pick track based on career direction |

**Joe's immediate next step**: Complete Action Plan 3 from [[EE Freshman Action Plans]] (already in place). Then bridge from "Python basics" to Phase 1 (NumPy + signal plotting) during the same Year 1 window.

---

## Related
- [[Python in Electrical Engineering]]
- [[C++ Self-Teaching Roadmap for EE]]
- [[EE Freshman Action Plans]]
- [[EE Freshman Self-Study Stack]]
- [[Research - Python and C++ in Electrical Engineering]]
- [[LTSpice Complete Skills Guide]]
