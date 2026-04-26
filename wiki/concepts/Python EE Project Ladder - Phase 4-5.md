---
type: concept
title: "Python EE Project Ladder - Phase 4-5"
created: 2026-04-26
updated: 2026-04-26
tags:
  - python
  - electrical-engineering
  - projects
  - simulation-automation
  - instrument-control
  - PyLTSpice
  - PyVISA
status: developing
related:
  - "[[Python EE Project Ladder]]"
  - "[[Python EE Project Ladder - Phase 2-3]]"
  - "[[Python EE Project Ladder - Advanced Tracks]]"
  - "[[Python in Electrical Engineering]]"
  - "[[LTSpice Complete Skills Guide]]"
---

# Python EE Project Ladder — Phase 4–5: Simulation Automation and Instrument Control

Projects 14–19. Covers PyLTSpice parametric analysis and PyVISA real-instrument automation. These are professional skills used daily in EE labs and test engineering. Total: ~4–5 months at 3–5 hrs/week.

---

## Phase 4: Simulation Automation with PyLTSpice (Projects 14–16)

**Setup prerequisite**: Install LTSpice (free, Analog Devices), then `pip install PyLTSpice`

---

### Project 14: RC Filter Parametric Sweep
**New Python concept**: `PyLTSpice.AscEditor` (edit component values in .asc schematic), `SimRunner` (run simulation), reading `.raw` output files  
**EE concept**: RC lowpass filter cutoff frequency f_c = 1/(2πRC); component value optimization; viewing all responses overlaid  
**Output**: Python loop sweeps R from 1kΩ to 100kΩ and C from 1nF to 100nF, runs LTSpice AC simulation for each pair, overlays all Bode responses in one Matplotlib plot, identifies combination closest to target cutoff  
**Libraries**: PyLTSpice, Matplotlib, NumPy

```python
from PyLTSpice import AscEditor, SimRunner
import numpy as np

runner = SimRunner(output_folder='./sweep_output')
asc = AscEditor('./rc_filter.asc')

for R_val in [1e3, 4.7e3, 10e3, 47e3]:
    asc.set_component_value('R1', R_val)
    asc.set_component_value('C1', 10e-9)
    asc.save_netlist('./rc_sweep.net')
    raw, log = runner.run_now(asc)
    # extract frequency and gain from raw file
    freq = raw.get_axis()
    gain_dB = 20 * np.log10(np.abs(raw.get_trace('V(out)')))
    plt.semilogx(freq, gain_dB, label=f'R={R_val/1000:.0f}kΩ')
```

**Teaches**: Parametric sweeps that would take 30 minutes of manual LTSpice clicking run in seconds. This skill directly applies to component optimization in Phase 2 of the EE action plan (Erickson + power filter design).  
**GitHub deliverable**: `rc_sweep.py` + `rc_filter.asc` + overlaid plot PNG showing all cutoffs

---

### Project 15: Monte Carlo Tolerance Analysis
**New Python concept**: PyLTSpice Monte Carlo mode, Pandas DataFrames for statistical analysis, `df.describe()`, histogram plotting  
**EE concept**: Component tolerances (1%/5%/10%); yield estimation (% parts meeting spec); ±3σ spread; worst-case analysis vs. statistical analysis  
**Output**: Runs 200 Monte Carlo iterations on an active Sallen-Key lowpass filter (.asc provided), collects cutoff frequency from each run, plots histogram of f_c distribution, computes ±3σ spread and yield at ±5% tolerance spec  
**Libraries**: PyLTSpice, Pandas, NumPy, Matplotlib

```python
import pandas as pd

results = []
for i in range(200):
    # PyLTSpice Monte Carlo: adds Gaussian variation to component values
    raw, log = runner.run_now(asc, run_filename=f'mc_{i}.net')
    fc = extract_cutoff(raw)   # -3dB frequency from AC trace
    results.append(fc)

df = pd.DataFrame({'cutoff_Hz': results})
print(df.describe())   # mean, std, min/max/quartiles
# 3-sigma yield estimate
yield_pct = ((df['cutoff_Hz'] > spec_low) & (df['cutoff_Hz'] < spec_high)).mean() * 100
```

**Teaches**: Pandas DataFrames are the right tool for large tabular simulation results. Monte Carlo is the industry standard for estimating production yield. This skill is used directly in power supply design sign-off.  
**GitHub deliverable**: `monte_carlo_filter.py` + histogram + yield report + sample `.asc`

---

### Project 16: Buck Converter Efficiency Sweep
**New Python concept**: LTSpice `.meas` SPICE directives (automated measurements), Pandas `read_csv()`, line plots with dual Y-axis  
**EE concept**: Converter efficiency η = P_out/P_in; switching losses (increase with frequency and current); conduction losses (I²R); optimal load point; efficiency curve η vs. I_load  
**Output**: Python script modifies load resistance in a buck converter .asc, runs transient simulation for each load step, extracts average V_out, I_in, I_out using .meas SPICE directives, computes efficiency, plots η(%) vs. I_load curve  
**Libraries**: PyLTSpice, Pandas, Matplotlib

```python
# .meas SPICE directives tell LTSpice to compute averages automatically
# .meas TRAN Iavg_in AVG I(Vin) FROM {0.8/fs} TO {1.0/fs}
# .meas TRAN Vavg_out AVG V(out) FROM {0.8/fs} TO {1.0/fs}

Iload_vals = np.arange(0.5, 10.0, 0.5)  # 0.5A to 10A
efficiencies = []
for IL in Iload_vals:
    R_load = 12.0 / IL   # Vout/Iload
    asc.set_component_value('R_LOAD', R_load)
    raw, log = runner.run_now(asc)
    # parse .meas results from log
    Pout = Vavg_out * IL
    Pin = Vin * Iavg_in
    efficiencies.append(Pout / Pin * 100)
```

**Teaches**: Efficiency curves are THE deliverable of a power electronics characterization. This project is exactly what a power electronics test engineer does. Direct overlap with LLNL/Tesla/Wolfspeed internship workflows.  
**GitHub deliverable**: `buck_efficiency_sweep.py` + η vs. I_load plot + `.asc` file with MOSFET model

---

## Phase 5: Instrument Control with PyVISA (Projects 17–19)

**Setup prerequisite**: `pip install pyvisa pyvisa-py` (use pyvisa-py backend to avoid requiring NI-VISA on Windows)  
**Hardware needed**: A programmable power supply (Rigol DP800 series, ~$200) or oscilloscope (Rigol DS1054Z, ~$350)  
**Alternative**: Use a USB-connected bench multimeter as a low-cost entry point

---

### Project 17: Power Supply + Multimeter I-V Sweep
**New Python concept**: `pyvisa.ResourceManager()`, `rm.open_resource()`, SCPI `.write()` and `.query()` commands, instrument discovery  
**EE concept**: SCPI protocol (IEEE 488.2 standard); remote instrument control; I-V characterization curve; diode/transistor characterization  
**Output**: Python script ramps power supply voltage from 0V to 5V in 50mV steps, queries multimeter for current at each step, plots I-V curve; for a diode, the exponential I-V relationship is clearly visible  
**Libraries**: PyVISA, Matplotlib, NumPy

```python
import pyvisa
import time

rm = pyvisa.ResourceManager('@py')   # use pyvisa-py backend
psu = rm.open_resource('USB0::RIGOL TECH::DP832::...')
dmm = rm.open_resource('USB0::RIGOL TECH::DM3068::...')

psu.write(':OUTP CH1,ON')
voltages, currents = [], []
for V in np.arange(0, 5.0, 0.05):
    psu.write(f':SOUR1:VOLT {V:.3f}')
    time.sleep(0.05)   # settle
    I = float(dmm.query(':MEAS:CURR:DC?'))
    voltages.append(V)
    currents.append(I)
```

**Teaches**: SCPI is the universal language of bench instruments. Every professional EE lab runs Python sweeps instead of clicking buttons. This skill alone justifies putting "lab automation" on your resume.  
**GitHub deliverable**: `psu_iv_sweep.py` — plots I-V curve; includes instrument discovery helper function

---

### Project 18: Oscilloscope Waveform Capture + Analysis
**New Python concept**: PyVISA waveform binary preamble decoding, Pandas DataFrame for multi-channel data, CSV export  
**EE concept**: Oscilloscope waveform acquisition; timebase scaling; Vpp, Vrms, frequency measurement; digital vs. analog waveform fidelity  
**Output**: Python script connects to oscilloscope, captures waveform from CH1 and CH2, decodes binary data to voltage/time arrays using preamble, saves to CSV, plots both channels with extracted measurements (Vpp, Vrms, f, rise time)  
**Libraries**: PyVISA, NumPy, Pandas, Matplotlib

```python
scope = rm.open_resource('USB0::RIGOL TECH::DS1054Z::...')
scope.write(':WAV:SOUR CHAN1')
scope.write(':WAV:MODE NORM')
scope.write(':WAV:FORM BYTE')

preamble = scope.query(':WAV:PRE?').split(',')
dt = float(preamble[4])     # time increment
y_inc = float(preamble[7])  # voltage increment
y_orig = float(preamble[8]) # voltage origin

raw = scope.query_binary_values(':WAV:DATA?', datatype='B')
voltage = (np.array(raw) - float(preamble[9])) * y_inc + y_orig
time_vec = np.arange(len(raw)) * dt

df = pd.DataFrame({'time_s': time_vec, 'voltage_V': voltage})
df.to_csv('waveform_capture.csv', index=False)
```

**Teaches**: Waveform binary decoding is the real PyVISA skill gap — most tutorials stop at SCPI text commands. Knowing the preamble structure unlocks high-speed waveform capture and post-processing.  
**GitHub deliverable**: `scope_capture.py` — captures and plots waveform; extracts and prints Vpp, Vrms, frequency

---

### Project 19: Automated Amplifier Bode Plot (Real Hardware)
**New Python concept**: Dual-instrument control loop (function generator + oscilloscope), frequency loop, Pandas export to Excel  
**EE concept**: Frequency response measurement from real hardware; −3dB bandwidth; gain in dB; phase lag; comparing measured vs. simulated Bode plot  
**Output**: Full automated ATE sweep: steps function generator frequency from 10Hz to 10MHz (20 points/decade), measures V_in and V_out amplitude from oscilloscope at each frequency, computes Gain(dB) and phase(°), plots measured Bode plot; compares to LTSpice simulation result from Project 14  
**Libraries**: PyVISA, Pandas, NumPy, Matplotlib

```python
import pyvisa
import numpy as np
import pandas as pd

fgen = rm.open_resource('USB0::RIGOL TECH::DG4162::...')
scope = rm.open_resource('USB0::RIGOL TECH::DS1054Z::...')

frequencies = np.logspace(1, 7, 60)  # 10 Hz to 10 MHz
results = []
for f in frequencies:
    fgen.write(f':SOUR1:FREQ {f:.2f}')
    time.sleep(0.2)   # settle
    Vpp_in  = float(scope.query(':MEAS:VAMP? CHAN1'))
    Vpp_out = float(scope.query(':MEAS:VAMP? CHAN2'))
    phase   = float(scope.query(':MEAS:RPHA? CHAN1,CHAN2'))
    gain_dB = 20 * np.log10(Vpp_out / Vpp_in)
    results.append({'freq_Hz': f, 'gain_dB': gain_dB, 'phase_deg': phase})

df = pd.DataFrame(results)
df.to_excel('bode_measured.xlsx', index=False)
```

**Teaches**: This is the capstone instrument automation project. It replicates what a test engineer does when characterizing a new amplifier or filter board. Combining simulation (Project 14 LTSpice) with measurement (Project 19 hardware) and comparing results is the professional verification workflow.  
**GitHub deliverable**: `amp_bode_sweep.py` — full sweep + comparison plot vs. simulated; requires function generator + oscilloscope

---

## Phase 4–5 Summary

| Project | Core Python Skill | Core EE Skill |
|---------|-------------------|---------------|
| 14 — RC Sweep | PyLTSpice SimRunner | Parametric optimization, cutoff frequency |
| 15 — Monte Carlo | PyLTSpice + Pandas | Tolerance analysis, yield, ±3σ |
| 16 — Efficiency Sweep | .meas SPICE directives | η vs. load, switching/conduction losses |
| 17 — PSU I-V Sweep | PyVISA SCPI | Remote instrument control, I-V curves |
| 18 — Scope Capture | Binary waveform decode | Waveform acquisition, Vpp/Vrms/f |
| 19 — Auto Bode Plot | Dual-instrument loop | Measured frequency response, ATE |

**By the end of Phase 5**: You can automate any simulation parametric analysis in LTSpice and control any bench instrument in Python. This directly maps to test engineering, power electronics characterization, and ATE development roles.
