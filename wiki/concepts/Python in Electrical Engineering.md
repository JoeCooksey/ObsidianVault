---
type: concept
title: "Python in Electrical Engineering"
status: developing
created: 2026-04-24
updated: 2026-04-24
tags:
  - python
  - electrical-engineering
  - simulation
  - instrument-control
  - signal-processing
  - control-systems
  - programming
---

# Python in Electrical Engineering

Python is the **scripting, analysis, and automation layer** of modern EE practice. It is not used for real-time control or firmware — that is C/C++'s domain. Python is used to design, simulate, characterize, automate, and visualize everything around the hardware.

---

## Where Python Lives in Physical EE

### 1. Simulation and Data Analysis
The most immediate use for EE students: running the math that textbooks show symbolically.

**Core libraries:**
- **NumPy** — arrays, matrix math, FFT, linear algebra. Think of it as MATLAB matrix operations.
- **Matplotlib** — plots Bode plots, time-domain waveforms, I-V curves. Every EE plot you make in MATLAB, you can make in Matplotlib.
- **SciPy** — the heavy-duty science library:
  - `scipy.signal`: FIR/IIR filter design, Bode plots, pole-zero maps, step responses, Laplace/z-transform utilities
  - `scipy.fft`: Fast Fourier Transform — the backbone of Signals & Systems
  - `scipy.integrate`: ODE solvers for circuit transient simulation from scratch
  - `scipy.linalg`: linear system solver (KVL/KCL matrix equations)
- **Pandas** — CSV import, time-series data from oscilloscopes and data loggers

**Example — RC filter frequency response:**
```python
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

R, C = 1e3, 1e-6
sys = signal.TransferFunction([1], [R*C, 1])
w, mag, phase = signal.bode(sys)
plt.semilogx(w/(2*np.pi), mag)
plt.xlabel('Frequency (Hz)'); plt.ylabel('Magnitude (dB)'); plt.grid(); plt.show()
```
This is the same Bode plot you'd get from LTSpice's `.ac` sweep.

---

### 2. Automated Test Equipment (ATE) Control — PyVISA
**The physical EE superpower of Python.** Every piece of bench equipment (oscilloscope, power supply, LCR meter, function generator, source-measure unit) can be controlled programmatically using **PyVISA** over GPIB, USB-TMC, TCP/IP, or RS-232.

```bash
pip install pyvisa pyvisa-py
```

**Basic pattern:**
```python
import pyvisa
rm = pyvisa.ResourceManager()
rm.list_resources()  # discover all connected instruments

osc = rm.open_resource('USB0::0x0699::0x0408::C012345::INSTR')  # Tektronix MSO
osc.write('CH1:SCALE 2')       # 2 V/div
data = osc.query('CURV?')      # download waveform
```

**Industry use**: Instead of manually stepping through 50 input voltage points for an efficiency map, a Python script sweeps the supply voltage, captures power measurements at each point, and exports a beautiful efficiency surface plot — in minutes instead of hours.

**Key brands with Python libraries:**
- Keysight: `keysight-pyvisa` or `pyvisa` with SCPI
- Tektronix: `tm_devices` (open source, excellent)
- Rohde & Schwarz: `RsInstrument`
- National Instruments: `nidaqmx` (DAQ control)

---

### 3. Control Systems Design — python-control
The `python-control` library (pip install control) is a **direct MATLAB Control Toolbox equivalent**:

```python
import control
# Design a PI controller for a DC-DC converter
plant = control.tf([1000], [1, 100])  # first-order plant
C_pi = control.tf([1, 10], [1, 0])   # PI controller (Kp=1, Ki=10)
T = control.feedback(C_pi * plant)    # closed-loop
control.bode(T)
control.step_response(T)
control.rlocus(C_pi * plant)
```

This is the workflow for designing digital power converter control before implementing it in C on a DSP. Design offline in Python, verify with Bode plot margins, then port to C.

---

### 4. LTSpice Automation — PyLTSpice
```bash
pip install PyLTSpice
```
PyLTSpice lets you run LTSpice from Python — modify component values, run simulations, extract waveforms — in a loop. Instead of manually changing a capacitor value 20 times, sweep it:

```python
from PyLTSpice import LTspice
lt = LTspice('buck_converter.asc')
for cap in [10e-6, 22e-6, 47e-6, 100e-6]:
    lt.set_component_value('C1', cap)
    lt.run()
    waveforms = lt.get_trace('V(out)')
    # plot, compare, export
```

This is how professional engineers run Monte Carlo sensitivity analyses and design-of-experiment sweeps.

---

### 5. FPGA Verification — cocotb
**cocotb** (Coroutine-based Cosimulation Testbench) lets you write FPGA testbenches in Python instead of VHDL or Verilog. This is advanced but extremely useful:

```python
import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge

@cocotb.test()
async def test_counter(dut):
    cocotb.start_soon(Clock(dut.clk, 10, units='ns').start())
    dut.reset.value = 1
    await RisingEdge(dut.clk)
    dut.reset.value = 0
    for _ in range(10):
        await RisingEdge(dut.clk)
    assert dut.count.value == 10
```

Directly relevant if Joe pursues Track A (FPGA → Sandia/LLNL path) in Phase 4 of the EE action plan.

---

### 6. KiCad Python Scripting
KiCad has a built-in Python scripting console and API. Use it to:
- Auto-place components based on a netlist
- Run design rule checks programmatically
- Generate BOMs automatically
- Custom footprint generation

---

## Key Libraries — Quick Reference

| Library | Install | Physical EE Use |
|---------|---------|----------------|
| NumPy | built-in via pip | Arrays, FFT, linear algebra |
| Matplotlib | pip install matplotlib | All EE plots |
| SciPy | pip install scipy | Signal processing, filter design, Bode, ODE |
| pandas | pip install pandas | CSV import, oscilloscope data |
| python-control | pip install control | Control design: Bode, rlocus, step response |
| PyVISA | pip install pyvisa | Instrument control (GPIB/USB/LAN) |
| pyvisa-py | pip install pyvisa-py | Pure Python VISA backend (no NI-VISA needed) |
| PyLTSpice | pip install PyLTSpice | LTSpice automation |
| cocotb | pip install cocotb | FPGA testbenches in Python |
| nidaqmx | pip install nidaqmx | NI DAQ hardware control |

---

## Python vs. MATLAB in EE

| Aspect | Python | MATLAB |
|--------|--------|--------|
| Cost | Free, open source | $$$, ASU provides free student license |
| Industry use | Test automation, ML, scripting | Signal processing, academic research |
| Control toolbox | python-control (good but narrower) | MATLAB Control Toolbox (industry standard) |
| Learning curve | Gentler if familiar with coding | Steeper syntax for programmers |
| Job market | Expected everywhere | Expected in controls/signals roles |
| Recommendation | Learn Python first — then MATLAB via ASU license | |

**For Joe**: Learn Python first (already in Year 1 action plan). Then pick up MATLAB via ASU license in Year 2 when EEE 202/203 require it. The skills transfer almost directly.

---

## Related
- [[Python Self-Teaching Roadmap for EE]]
- [[C++ in Electrical Engineering]]
- [[LTSpice Complete Skills Guide]]
- [[EE Freshman Action Plans]]
- [[Research - Python and C++ in Electrical Engineering]]
- [[EE Physical Side — Actionable Skill Plan]]
