---
type: concept
title: "Circuit Theory Fundamentals"
created: 2026-04-27
updated: 2026-04-27
tags:
  - EE
  - circuits
  - fundamentals
  - first-year
  - KVL
  - KCL
status: developing
---
# Circuit Theory Fundamentals

The bedrock of all electrical engineering. Every advanced EE topic — power electronics, control systems, communications, semiconductors — assumes fluency in circuit theory.

## Why This Is Topic #1

Circuit theory is explicitly prerequisite for every advanced EE course. At ASU, EEE 202 (Circuits I) is the foundational EE course; understanding circuit theory before taking it creates a massive advantage. Every LTSpice simulation, Python calculation, and breadboard build uses these concepts.

## Core Topics in Priority Order

### 1. KVL and KCL — The Two Axioms
- **Kirchhoff's Voltage Law (KVL)**: Sum of voltages around any closed loop = 0
- **Kirchhoff's Current Law (KCL)**: Sum of currents at any node = 0
- All other circuit analysis is derived from these two laws; master them deeply

### 2. Nodal and Mesh Analysis
- **Nodal Analysis**: Apply KCL at each non-reference node; solve system of equations for node voltages
- **Mesh Analysis**: Apply KVL around each independent mesh; solve for mesh currents
- Essential for analyzing any multi-component circuit; KCL is what LTSpice's SPICE solver does internally

### 3. Thevenin and Norton Equivalents
- Any linear circuit with two terminals can be replaced by:
  - **Thevenin**: $V_{th}$ in series with $R_{th}$
  - **Norton**: $I_{sc}$ in parallel with $R_{th}$
- $V_{th} = V_{oc}$ (open-circuit voltage) and $R_{th}$ found by zeroing independent sources
- Used everywhere: battery internal impedance, amplifier stage matching, load sensitivity analysis

### 4. AC Circuits and Phasors
- Replace sinusoidal voltages/currents with complex phasors: $V = V_0 \angle\theta$
- **Impedance**: $Z_R = R$, $Z_C = 1/j\omega C$, $Z_L = j\omega L$
- KVL and KCL still apply — now with complex arithmetic
- Power: average power $P = V_{rms} I_{rms} \cos\theta$; reactive power $Q = V_{rms} I_{rms} \sin\theta$

### 5. Frequency Response
- How circuit gain and phase shift vary with frequency
- **Low-pass RC filter**: $|H(j\omega)| = 1/\sqrt{1+(\omega RC)^2}$; cutoff at $\omega_c = 1/RC$
- **Resonance**: $\omega_0 = 1/\sqrt{LC}$; quality factor $Q = \omega_0 L / R$
- Preview of Signals & Systems — the Bode plot is a frequency response plot

### 6. Time-Domain Transient Analysis
- **RC circuit** (1st order): $v(t) = V_f + (V_i - V_f)e^{-t/\tau}$ where $\tau = RC$
- **RLC circuit** (2nd order): characterized by $\omega_n = 1/\sqrt{LC}$ and $\zeta = R/(2)\sqrt{C/L}$
  - $\zeta < 1$: underdamped (oscillation)
  - $\zeta = 1$: critically damped (fastest non-oscillatory)
  - $\zeta > 1$: overdamped (sluggish)
- These are first and second-order ODEs — the link to MAT 275

### 7. Op-Amp Circuits
- Ideal op-amp rules: $V_+ = V_-$ (virtual short), $I_{in} = 0$ (no input current)
- Key configurations: inverting amplifier, non-inverting amplifier, voltage follower, summing amplifier, integrator, differentiator
- Used in: analog filters, signal conditioning, instrumentation amplifiers, comparators

### 8. Power in Circuits
- **Instantaneous power**: $p(t) = v(t) \cdot i(t)$
- **Average power**: $P_{avg} = V_{rms} I_{rms} \cos\theta$
- **RMS**: $V_{rms} = V_0/\sqrt{2}$ for sinusoids; $P_{avg} = V_{rms}^2/R$
- **Maximum power transfer**: load resistance $R_L = R_{th}$ for maximum power

## Best Textbooks

| Book                                                   | Best For                     |
| ------------------------------------------------------ | ---------------------------- |
| Nilsson & Riedel "Electric Circuits"                   | ASU standard; comprehensive  |
| Hayt & Kemmerly "Engineering Circuit Analysis"         | Intuitive, readable          |
| Alexander & Sadiku "Fundamentals of Electric Circuits" | Good problem variety         |
| The Art of Electronics (Horowitz & Hill)               | Practical design perspective |

## Free Resources
- **Khan Academy** — basic circuits, KVL/KCL (entry level)
- **All About Circuits** (allaboutcircuits.com) — free textbook equivalent
- **MIT OCW 6.002** (Circuits and Electronics) — full course with video

## Connection to LTSpice and Python
- The 10-circuit LTSpice ladder maps exactly to this: voltage divider → RC/RL/RLC → op-amp → buck converter
- Python projects 1–6 (Ohm's Law → RLC transient) are circuit theory in code
- Build each LTSpice/Python circuit while studying the corresponding theory concept

## Connection to Joe's WBG Career
- Every power converter (buck, boost, flyback) is analyzed with circuit theory first
- Thevenin impedance is required for gate driver design and dead-time analysis
- Phasor analysis is required for AC power systems and PFC topology design
- RLC resonance is the heart of LLC converters used in modern EV chargers (350 kW DCFC)

## Related Concepts
- [[Differential Equations in Electrical Engineering]]
- [[Signals and Systems — Laplace and Fourier]]
- [[LTSpice Complete Skills Guide]]
- [[Python EE Project Ladder - Phase 0-1]]
- [[EE Topic Depth Priority Map]]
