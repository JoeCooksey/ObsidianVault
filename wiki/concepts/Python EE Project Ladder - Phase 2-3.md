---
type: concept
title: "Python EE Project Ladder - Phase 2-3"
created: 2026-04-26
updated: 2026-04-26
tags:
  - python
  - electrical-engineering
  - projects
  - signal-processing
  - control-systems
status: developing
related:
  - "[[Python EE Project Ladder]]"
  - "[[Python EE Project Ladder - Phase 0-1]]"
  - "[[Python EE Project Ladder - Phase 4-5]]"
  - "[[Differential Equations in Electrical Engineering]]"
---

# Python EE Project Ladder — Phase 2–3: DSP and Control Systems

Projects 7–13. Covers frequency domain analysis (FFT, filter design) and control theory (Bode, PID, state-space). Total: ~3–5 months at 3–5 hrs/week.

---

## Phase 2: Frequency Domain and Signal Processing (Projects 7–10)

---

### Project 7: Bode Plot Generator
**New Python concept**: `scipy.signal.bode()`, dB conversion (`20*np.log10`), two-subplot frequency response  
**EE concept**: Transfer function H(s) = numerator/denominator polynomials; poles and zeros; −20 dB/decade per pole; −45°/decade phase shift at pole frequency  
**Output**: Takes transfer function numerator/denominator coefficients, plots magnitude (dB) and phase (°) Bode plot with pole/zero frequencies marked  
**Libraries**: SciPy, Matplotlib

```python
from scipy import signal
import numpy as np, matplotlib.pyplot as plt

# H(s) = 1 / (s^2 + 0.2s + 1)   second-order lowpass
num = [1]
den = [1, 0.2, 1]
sys = signal.TransferFunction(num, den)
w, mag, phase = signal.bode(sys, w=np.logspace(-1, 2, 500))

fig, (ax1, ax2) = plt.subplots(2, 1)
ax1.semilogx(w/(2*np.pi), mag)   # Bode magnitude
ax2.semilogx(w/(2*np.pi), phase) # Bode phase
```

**Teaches**: `scipy.signal` transfer functions → the same H(s) you write on paper, now plotable in 5 lines. This is used directly in EEE 350 (Control Systems) and every filter design task.  
**GitHub deliverable**: `bode_generator.py` — accepts arbitrary num/den coefficients, annotates poles and −3dB point

---

### Project 8: FFT Spectrum Analyzer
**New Python concept**: `np.fft.rfft()`, frequency bin calculation, window functions (Hanning, Blackman), power spectral density  
**EE concept**: Discrete Fourier Transform; Nyquist sampling theorem (fs > 2×fmax); spectral leakage and how windowing reduces it; dBFS representation  
**Output**: Reads a time-domain signal from CSV (e.g., oscilloscope export), computes FFT, plots single-sided spectrum in dBFS with windowing options  
**Libraries**: NumPy, Matplotlib

```python
import numpy as np

fs = 1e6  # sample rate 1 MHz
t, x = np.loadtxt("waveform.csv", delimiter=",", unpack=True)
N = len(x)
window = np.hanning(N)
X = np.fft.rfft(x * window)
freqs = np.fft.rfftfreq(N, d=1/fs)
mag_dB = 20 * np.log10(np.abs(X) / N * 2)  # single-sided, normalized
```

**Teaches**: FFT is the most important algorithm in EE signal processing. Windowing is mandatory for real measurements. This project connects theory (Fourier series from MAT 266) to real oscilloscope data.  
**GitHub deliverable**: `fft_analyzer.py` — reads CSV, plots spectrum with selectable window function

---

### Project 9: FIR Lowpass Filter Designer
**New Python concept**: `scipy.signal.firwin()`, `scipy.signal.freqz()`, convolution with `np.convolve()`  
**EE concept**: Finite Impulse Response (FIR) filter design; cutoff frequency, transition band width; linear phase property; filter order vs. sharpness tradeoff  
**Output**: Designs a lowpass FIR filter at a specified cutoff frequency, plots frequency response, applies filter to a noisy sinusoidal signal, plots before/after  
**Libraries**: SciPy, NumPy, Matplotlib

```python
from scipy.signal import firwin, freqz, lfilter

fs = 44100
cutoff = 1000  # Hz
numtaps = 101
taps = firwin(numtaps, cutoff, fs=fs)  # Hamming-windowed FIR

w, h = freqz(taps, worN=8000, fs=fs)
filtered = lfilter(taps, 1.0, noisy_signal)
```

**Teaches**: FIR filter design is the most common DSP task in EE. Knowing order/cutoff/window tradeoffs is a standard interview question for embedded/DSP roles.  
**GitHub deliverable**: `fir_designer.py` — interactive filter design tool with before/after spectra

---

### Project 10: IIR Filter and Pole-Zero Plot
**New Python concept**: `scipy.signal.butter()` / `scipy.signal.cheby1()`, `scipy.signal.tf2zpk()`, z-plane pole-zero plot using unit circle  
**EE concept**: Infinite Impulse Response (IIR) filters; Butterworth (maximally flat) vs. Chebyshev (equal ripple) tradeoff; poles inside unit circle = stable; filter in z-domain  
**Output**: Designs Butterworth and Chebyshev bandpass filters, plots both frequency responses overlaid, plots pole-zero map with unit circle for each  
**Libraries**: SciPy, NumPy, Matplotlib

```python
from scipy.signal import butter, cheby1, tf2zpk, freqz, sosfilt

# Butterworth 4th order lowpass
sos = butter(4, 0.2, output='sos')  # normalized cutoff 0.2*Nyquist
# Chebyshev 4th order, 1 dB ripple
sos_cheby = cheby1(4, 1, 0.2, output='sos')

z, p, k = tf2zpk(*butter(4, 0.2))  # for pole-zero plot
```

**Teaches**: Understanding poles in the z-plane = understanding digital filter stability. This concept is foundational for DSP firmware, control loop design in microcontrollers, and digital power supplies.  
**GitHub deliverable**: `iir_designer.py` — frequency response comparison + pole-zero plot for any IIR type

---

## Phase 3: Control Systems (Projects 11–13)

---

### Project 11: Transfer Function Analysis with python-control
**New Python concept**: `control.tf()`, `control.bode_plot()`, `control.root_locus()`, `control.step_response()`  
**EE concept**: Transfer functions H(s) in closed-loop system; frequency response; stability from root locus; step response transient characteristics (rise time, overshoot, settling time)  
**Output**: Unified Jupyter notebook — given any H(s), plots: Bode (open loop), Nyquist, root locus, closed-loop step response  
**Libraries**: python-control, Matplotlib

```python
import control

H = control.tf([1], [1, 2, 1])          # H(s) = 1/(s^2+2s+1)
G = control.feedback(H, 1)              # unity negative feedback

control.bode_plot(H)
control.root_locus(H)
t, y = control.step_response(G)
```

**Teaches**: `python-control` is a direct MATLAB replacement — same syntax, zero cost, runs in VS Code. Every function in this project maps to a concept in ASU EEE 350 (Control Systems).  
**GitHub deliverable**: `control_analysis_notebook.ipynb` — reusable template for any transfer function

---

### Project 12: PID Controller Tuning Simulator
**New Python concept**: `control.feedback()` with cascaded transfer functions, nested loops for parameter sweep, gain/phase margin calculation  
**EE concept**: PID control (proportional + integral + derivative); Ziegler-Nichols tuning rules; gain margin and phase margin as stability metrics  
**Output**: Sweeps Kp, Ki, Kd values for a given plant, plots grid of step responses, prints stability margins for each; identifies "best" tuning by fastest settling with >30° phase margin  
**Libraries**: python-control, NumPy, Matplotlib

```python
import control
import numpy as np

Plant = control.tf([1], [1, 2, 1])   # example second-order plant

for Kp in np.arange(0.5, 5.0, 0.5):
    PID = control.tf([Kp], [1])      # proportional only (extend for I+D)
    G_ol = PID * Plant
    gm, pm, wcg, wcp = control.margin(G_ol)
    G_cl = control.feedback(G_ol)
    t, y = control.step_response(G_cl)
    # plot and record pm for each Kp
```

**Teaches**: PID is the dominant controller in industrial and power electronics applications. Phase margin > 45° is the universal stability design rule. This project builds the mental model used in digital power supply design (TI C2000 PI controller).  
**GitHub deliverable**: `pid_tuner.py` — sweep plots + Jupyter notebook with stability contour plot

---

### Project 13: Closed-Loop Buck Converter PI Simulation
**New Python concept**: `scipy.integrate.solve_ivp`, state-space modeling, switching simulation with event-driven logic  
**EE concept**: Buck converter state equations (inductor IL, capacitor VC as state variables); PI current controller; duty cycle D; switching frequency; output voltage regulation  
**Output**: Time-domain simulation of buck converter (L=100μH, C=100μF, fs=100kHz, Vin=24V, Vout=12V target) with PI current controller; plots V_out(t), I_L(t), and duty cycle D(t) over transient response to load step  
**Libraries**: SciPy, NumPy, Matplotlib

```python
import numpy as np
from scipy.integrate import solve_ivp

def buck_ode(t, y, Vin, R_load, L, C, D):
    IL, VC = y
    if D > 0:  # switch ON
        dIL = (Vin - VC) / L
    else:      # switch OFF
        dIL = -VC / L
    dVC = (IL - VC/R_load) / C
    return [dIL, dVC]

# PI controller
error = Vref - VC
D = Kp * error + Ki * integral_error
D = np.clip(D, 0.0, 0.95)  # duty cycle limits
```

**Teaches**: This is the most important project in the ladder. It connects Python (ODE solver), EE theory (state-space model), and power electronics (buck converter control) — the exact skill set required for WBG internship interviews.  
**GitHub deliverable**: `buck_pi_sim.py` — full simulation with load step transient, plots IL + Vout + D(t)

---

## Phase 2–3 Summary

| Project | Core Python Skill | Core EE Skill |
|---------|-------------------|---------------|
| 7 — Bode Plot | scipy.signal.bode, dB | Transfer functions, poles/zeros |
| 8 — FFT Analyzer | np.fft.rfft, windowing | DFT, Nyquist, spectral leakage |
| 9 — FIR Filter | firwin, freqz, convolve | FIR design, cutoff, linear phase |
| 10 — IIR Filter | butter, tf2zpk, z-plane | IIR, Butterworth/Chebyshev, poles |
| 11 — TF Analysis | control.tf, root_locus | Stability, step response, Nyquist |
| 12 — PID Tuner | control.feedback, margin() | PID tuning, gain/phase margin |
| 13 — Buck Sim | solve_ivp, state-space | Buck converter, PI control, duty cycle |

**By the end of Phase 3**: You can design and verify digital filters, analyze control systems, and simulate a switching power converter — skills that directly overlap with ASU EEE 350, EEE 480, and any power electronics internship.
