---
type: research
title: "Research - Math and Physics Foundations for EE"
status: developing
created: 2026-04-19
updated: 2026-04-19
tags:
  - research
  - electrical-engineering
  - calculus
  - differential-equations
  - physics
  - mechanics
  - electromagnetism
  - foundations
---

# Research — Math and Physics Foundations for EE

**Topic**: How do Calculus 1–3, Differential Equations, Physics Mechanics, and Physics E&M directly connect to electrical engineering coursework and career?

**For**: Joe — Year 1 ASU EE student in math/physics courses, no EE courses yet

---

## Key Findings

### 1. Every circuit with L or C is a differential equation
The moment you have a capacitor ($i = C\,dv/dt$) or inductor ($v = L\,di/dt$), KVL produces an ODE. An RC circuit is a 1st-order ODE; an RLC circuit is 2nd-order. The transient behavior, time constants, and resonance you see in LTspice simulations are the physical manifestation of solving these ODEs. **DiffEQ is the math, circuits are the application.**

### 2. Calculus 1 appears every day in EEE 202 (Circuits I)
- $i = C\,dv/dt$ and $v = L\,di/dt$ are derivatives — Calc 1 vocabulary
- Op-amp slew rate is a derivative limit (V/μs = dV/dt max)
- Small-signal BJT/MOSFET models use linearization (tangent-line approximation at a bias point)
- Power $p(t) = v(t)\cdot i(t)$; energy = $\int p\,dt$ — Calc 2

### 3. Calc 2 integration gives you RMS, energy storage, and Fourier series
- RMS voltage is a definite integral over a period — essential for AC power calculations
- $\tfrac{1}{2}CV^2$ and $\tfrac{1}{2}LI^2$ come from integrating the V-I relationships
- Fourier series decomposition (periodic signals into sinusoids) uses integral coefficients — this is how a spectrum analyzer works and how filter design is grounded

### 4. Calc 3 vector calculus IS Maxwell's equations
All four Maxwell's equations use gradient, divergence, and curl. Without Calc 3, EEE 340 (Electromagnetics) is inaccessible. The Poynting vector ($\mathbf{S} = \mathbf{E}\times\mathbf{H}$), which gives the direction and magnitude of EM power flow, is a cross product — Calc 3.

### 5. Mechanics provides the motor/generator framework
Newton's 2nd law for rotation ($\tau = J\,d\omega/dt$) is the mechanical half of every motor equation. The coupled electrical-mechanical ODE system (two linked 1st-order ODEs) is exactly what you simulate when designing a motor controller in EEE 480 (Control Systems). Conservation of energy in mechanics → power balance equation in circuits.

### 6. The mechanical-electrical analogy is exact and powerful
Mass $m$ ↔ inductance $L$, spring compliance ↔ capacitance $C$, damper $b$ ↔ resistance $R$. The ODE is identical: $m\ddot{x}+b\dot{x}+kx = F$ maps exactly to $L\ddot{q}+R\dot{q}+q/C = V$. Once you solve one, you've solved both. MEMS sensors (accelerometers, gyroscopes in every phone) are literal mass-spring systems read out as electrical signals.

### 7. Faraday's and Ampere's laws are the transformer and inductor
Faraday's law ($\mathcal{E} = -N\,d\Phi/dt$) is the operating principle of every transformer and generator. Ampere's law ($\oint\mathbf{H}\cdot d\mathbf{l} = NI$) lets you calculate inductance from geometry — how many turns on a toroid to get 100 μH? That's Ampere's law. Every switching power supply (buck, boost, flyback) uses inductors and transformers designed with these laws.

### 8. Lorentz force explains motors, Hall sensors, and why wires have inductance
$\mathbf{F} = q\mathbf{v}\times\mathbf{B}$ — force on a moving charge in a magnetic field — is motor torque ($F = BIL$), Hall sensor operation, and the reason a PCB trace has parasitic inductance. At GHz frequencies, this parasitic inductance causes ringing in digital signals (signal integrity). Understanding the Lorentz force lets you reason about EMC and high-speed PCB layout.

---

## Math-to-EE Course Map

| Math/Physics | Core Tool | First EE Use | Course |
|---|---|---|---|
| Calc 1 | Derivative | Cap/inductor V-I; linearization | EEE 202 |
| Calc 2 | Integral, series | RMS, energy, Fourier, convolution | EEE 202, EEE 350 |
| Calc 3 | Gradient/div/curl | Maxwell's equations; field analysis | EEE 340 |
| DiffEQ | ODE solution, Laplace | Circuit transients; transfer functions | EEE 202 |
| DiffEQ | 2nd-order ODE | RLC resonance; filter design | EEE 202 |
| DiffEQ (coupled) | State space | Motor control; control systems | EEE 480 |
| Mechanics (linear) | Newton 2nd, work-energy | Power balance; solenoid actuators | EEE 202 |
| Mechanics (rotational) | Torque, inertia | Motor/generator dynamics | EEE 480 |
| Mechanics (vibration) | Resonance, damping | MEMS; RLC analogy | EEE 202 |
| E&M (Gauss) | Surface integral | Capacitance from geometry | EEE 340 |
| E&M (Faraday) | $d\Phi/dt$ | Transformer; generator; inductor | EEE 340 |
| E&M (Ampere) | Line integral | Inductance; magnetic circuit design | EEE 340 |
| E&M (Lorentz) | $q\mathbf{v}\times\mathbf{B}$ | Motor torque; Hall sensors; EMC | EEE 340, 480 |
| E&M (Maxwell full) | Wave equation | RF; transmission lines; antennas | EEE 340, 476 |

---

## For Joe: The Year 1 Perspective

You're currently in MAT 265/266 (Calc 1/2) and either in or approaching PHY 121/122. Here's the payoff timeline:

| Right Now | Math/Physics Payoff in EE |
|---|---|
| MAT 265 (Calc 1) | You're learning the math for $i = C\,dv/dt$ and $v = L\,di/dt$ right now |
| MAT 266 (Calc 2) | You're learning RMS integrals, energy formulas, Fourier — used every week in EEE 202 |
| MAT 267 (Calc 3) | You're learning the language of Maxwell's equations before EEE 340 |
| MAT 275 (DiffEQ) | You're learning to solve the actual circuit ODEs before EEE 202 |
| PHY 121 (Mechanics) | You're learning motor/generator mechanics, conservation of energy, resonance |
| PHY 122 (E&M) | You're learning where circuits come from — every component is E&M |

**Practical tip**: when you build an RC circuit on a breadboard (even now, before EEE 202), you're watching a first-order ODE play out in real time on an oscilloscope. The exponential charging curve is $v(t) = V_s(1 - e^{-t/RC})$.

---

## Open Questions

1. How does Fourier transform (Calc 2 + complex analysis) connect to the Z-transform used in digital filters (EEE 407)?
2. How does multivariable optimization (Calc 3 Lagrange multipliers) appear in optimal control theory?
3. At what point does the mechanical-electrical analogy break down (nonlinear mechanics, saturation)?
4. How does quantum mechanics (not covered here) modify E&M at the semiconductor device level?
5. When does numerical solving (finite element analysis, SPICE) replace analytical DiffEQ in industry?

---

## Concept Pages Created
- [[Calculus in Electrical Engineering]] — Calc 1-3 mapped to specific EE applications
- [[Differential Equations in Electrical Engineering]] — ODE types, Laplace, control systems
- [[Classical Mechanics in Electrical Engineering]] — mechanical-electrical analogy, motors, MEMS
- [[Electromagnetism Foundations for EE]] — Maxwell's equations to component design

---

## Related
- [[ASU EE Year 1-2 Curriculum Map]]
- [[EE Freshman Self-Study Stack]]
- [[EE Physical Side — Actionable Skill Plan]]
- [[Research - First-Year ASU EE Skills]]
