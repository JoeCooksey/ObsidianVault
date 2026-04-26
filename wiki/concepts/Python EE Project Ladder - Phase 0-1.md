---
type: concept
title: "Python EE Project Ladder - Phase 0-1"
created: 2026-04-26
updated: 2026-04-26
tags:
  - python
  - electrical-engineering
  - projects
  - circuit-analysis
status: developing
related:
  - "[[Python EE Project Ladder]]"
  - "[[Python EE Project Ladder - Phase 2-3]]"
  - "[[Calculus in Electrical Engineering]]"
  - "[[Differential Equations in Electrical Engineering]]"
---

# Python EE Project Ladder — Phase 0–1: Basics and Circuit Analysis

Projects 1–6. Each project introduces one new Python/library concept while solving a real EE problem. Total: ~2–4 months at 3–5 hrs/week.

---

## Project 1: Ohm's Law Calculator
**New Python concept**: Functions, f-strings, conditional input validation  
**EE concept**: V=IR, P=IV=I²R=V²/R, unit conversions (mA, kΩ, mW)  
**Output**: CLI tool — given any two of V/I/R, computes the third + power P  
**Libraries**: None (pure Python)

```python
def ohms_law(V=None, I=None, R=None):
    if V is None: V = I * R
    elif I is None: I = V / R
    elif R is None: R = V / I
    P = V * I
    return V, I, R, P
```

**Teaches**: Functions are the unit of reusable code. Return multiple values. Build CLI tools.  
**GitHub deliverable**: `ohm_calc.py` — 30–50 lines

---

## Project 2: Resistor Network Analyzer
**New Python concept**: NumPy arrays, element-wise operations, Matplotlib bar/line charts  
**EE concept**: Series resistance (Rₛ = ΣRᵢ), parallel resistance (1/Rₚ = Σ1/Rᵢ), voltage divider Vout = Vin × R2/(R1+R2)  
**Output**: Takes a list of resistors and config (series/parallel), computes equivalent R, plots voltage distribution across each resistor  
**Libraries**: NumPy, Matplotlib

```python
import numpy as np
import matplotlib.pyplot as plt

R = np.array([1e3, 2.2e3, 4.7e3])  # resistor values
Vin = 12.0
R_total = np.sum(R)
V_drop = Vin * R / R_total          # voltage divider each
```

**Teaches**: NumPy arrays replace Python lists for math. Broadcasting lets you operate on whole arrays at once.  
**GitHub deliverable**: `resistor_network.py` + voltage distribution bar chart PNG

---

## Project 3: E-Series Component Plotter
**New Python concept**: `np.logspace()`, logarithmic axes, `np.round()` to significant figures  
**EE concept**: E12/E24 preferred value series (logarithmically spaced), 10%/5%/1% tolerance bands, why standard values exist  
**Output**: Plots all E12 and E24 values on a log10 axis with tolerance bands shaded; shows which values are "covered" within tolerance  
**Libraries**: NumPy, Matplotlib

```python
E12 = [1.0, 1.2, 1.5, 1.8, 2.2, 2.7, 3.3, 3.9, 4.7, 5.6, 6.8, 8.2]
decades = [np.array(E12) * 10**n for n in range(5)]
```

**Teaches**: Log-scale thinking is core to EE (Bode plots, decades, dB). `logspace` is used in every frequency domain project.  
**GitHub deliverable**: `e_series_plotter.py` + Jupyter notebook with explanation

---

## Project 4: Nodal Analysis Matrix Solver
**New Python concept**: `np.linalg.solve()`, 2D NumPy matrices, matrix construction from a netlist  
**EE concept**: Kirchhoff's Current Law (KCL), conductance matrix G, node voltages v = G⁻¹i  
**Output**: Takes a resistor netlist (list of (node1, node2, R) tuples), builds conductance matrix, solves for all node voltages, plots as bar chart  
**Libraries**: NumPy, Matplotlib

```python
# G * v = i_source
# G[i][i] += sum of conductances at node i
# G[i][j] -= conductance between nodes i and j
G = np.zeros((n_nodes, n_nodes))
for (n1, n2, R) in netlist:
    g = 1.0 / R
    G[n1][n1] += g
    G[n2][n2] += g
    G[n1][n2] -= g
    G[n2][n1] -= g
v = np.linalg.solve(G[1:, 1:], i_src[1:])  # exclude ground node
```

**Teaches**: Linear algebra is the language of circuit analysis. This same structure handles any resistive network. Matrix solver scales to 100-node circuits effortlessly.  
**GitHub deliverable**: `nodal_analysis.py` — solves any 2–10 node resistive network

---

## Project 5: AC Phasor Impedance Analyzer
**New Python concept**: Python `complex()` type, `np.abs()` and `np.angle()` for complex arrays, `np.linspace` over frequency  
**EE concept**: Impedance Z_R=R, Z_C=1/(jωC), Z_L=jωL; series/parallel combination with complex arithmetic; |Z| and ∠Z vs. frequency  
**Output**: Plots impedance magnitude |Z(f)| and phase ∠Z(f) vs. frequency for a user-specified series or parallel RLC combination  
**Libraries**: NumPy, Matplotlib

```python
f = np.logspace(1, 6, 1000)      # 10 Hz to 1 MHz
omega = 2 * np.pi * f
Z_R = R + 0j
Z_C = 1 / (1j * omega * C)
Z_L = 1j * omega * L
Z_total = Z_R + Z_C + Z_L         # series RLC

plt.subplot(2,1,1)
plt.semilogx(f, 20*np.log10(np.abs(Z_total)))  # dB
plt.subplot(2,1,2)
plt.semilogx(f, np.degrees(np.angle(Z_total)))  # degrees
```

**Teaches**: Complex numbers handle phase naturally. dB = 20·log10(|Z|). This is the foundation of every Bode plot.  
**GitHub deliverable**: `ac_phasor.py` — plots |Z| and phase for any RLC config

---

## Project 6: RC/RL/RLC Transient Simulator
**New Python concept**: `scipy.integrate.odeint`, defining differential equations as Python functions, multi-subplot figures  
**EE concept**: RC step response V(t) = V∞(1 − e^(−t/τ)); RLC step response with ωn = 1/√(LC), ζ = R/(2√(L/C)); underdamped/critically damped/overdamped  
**Output**: Plots V_C(t) for RC circuit, I_L(t) for RL circuit, and V_C(t) for RLC at ζ = 0.2, 0.5, 1.0, 2.0  
**Libraries**: SciPy, NumPy, Matplotlib

```python
from scipy.integrate import odeint

def rc_ode(y, t, R, C, Vin):
    Vc = y[0]
    dVc_dt = (Vin - Vc) / (R * C)
    return [dVc_dt]

def rlc_ode(y, t, R, L, C, Vin):
    Vc, IL = y
    dVc_dt = IL / C
    dIL_dt = (Vin - R*IL - Vc) / L
    return [dVc_dt, dIL_dt]

t = np.linspace(0, 5*tau, 1000)
sol = odeint(rc_ode, y0=[0], t=t, args=(R, C, 12.0))
```

**Teaches**: ODE solvers are the bridge between circuit equations (which you derive) and time-domain waveforms (which you observe). This is the same tool used to simulate switching converters in Phase 3.  
**GitHub deliverable**: `transient_simulator.py` — plots all three circuit types with interactive ζ sweep

---

## Phase 0–1 Summary

| Project | Core Python Skill | Core EE Skill |
|---------|-------------------|---------------|
| 1 — Ohm's Law | Functions + f-strings | V=IR, P=IV |
| 2 — Resistor Network | NumPy arrays + Matplotlib | Series/parallel, voltage divider |
| 3 — E-Series Plotter | logspace, log axes | Standard value series, tolerances |
| 4 — Nodal Analysis | linalg.solve, matrices | KCL, conductance matrix, node voltages |
| 5 — AC Phasor | complex() type | Impedance, phasors, |Z| vs. f |
| 6 — RLC Transient | scipy.integrate.odeint | RC/RL/RLC step response, ζ, ωn |

**By the end of Phase 1**: You can analyze any DC or AC circuit numerically in Python and have a complete replacement for manual hand calculations.
