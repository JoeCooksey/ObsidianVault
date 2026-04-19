---
type: concept
title: "Differential Equations in Electrical Engineering"
status: developing
created: 2026-04-19
updated: 2026-04-19
tags:
  - mathematics
  - differential-equations
  - electrical-engineering
  - circuits
  - control-systems
---

# Differential Equations in Electrical Engineering

Differential equations (ODEs and PDEs) are the native language of circuit dynamics. Every circuit with an energy-storing element (capacitor or inductor) produces a differential equation when you apply KVL or KCL.

---

## Why Circuits Produce ODEs

Capacitors and inductors have memory — their behavior depends on their history, not just the instantaneous voltage or current. This is captured by derivative relationships:

- $i_C = C \, dv/dt$ → voltage across a capacitor cannot change instantaneously
- $v_L = L \, di/dt$ → current through an inductor cannot change instantaneously

When you write KVL around a loop containing these elements, derivatives appear, and you have an ODE.

---

## First-Order Circuits — RC and RL (1st-Order ODE)

### RC Circuit Example
A series RC circuit driven by a step voltage $V_s$:
$$V_s = Ri + \frac{1}{C}\int i\,dt \quad \Rightarrow \quad RC\frac{dv_C}{dt} + v_C = V_s$$

This is a first-order linear ODE with constant coefficients. Solution:
$$v_C(t) = V_s\left(1 - e^{-t/\tau}\right), \quad \tau = RC$$

- **Time constant** $\tau$: in 5τ the capacitor is 99.3% charged.
- Application: **filter design**. An RC low-pass filter has $f_c = 1/(2\pi RC)$; above $f_c$ the output is attenuated. Every analog filter (passive and active) is derived from this ODE.
- Application: **power-supply decoupling**. The RC time constant determines how fast a bypass capacitor can respond to a sudden load current.

### RL Circuit Example
Series RL circuit (relay coil, motor winding, inductor in a buck converter):
$$L\frac{di}{dt} + Ri = V_s \quad \Rightarrow \quad i(t) = \frac{V_s}{R}\left(1 - e^{-Rt/L}\right)$$

Time constant $\tau = L/R$. Application: **inductive kickback** — when the switch opens, di/dt tries to go to infinity, inducing a large voltage spike (hence flyback diodes in motor drivers).

---

## Second-Order Circuits — RLC (2nd-Order ODE)

A series RLC circuit with voltage source $V_s$:
$$L\frac{d^2i}{dt^2} + R\frac{di}{dt} + \frac{i}{C} = \frac{dV_s}{dt}$$

Or equivalently in terms of $v_C$:
$$LC\frac{d^2v_C}{dt^2} + RC\frac{dv_C}{dt} + v_C = V_s$$

**Characteristic equation**: $s^2 + \frac{R}{L}s + \frac{1}{LC} = 0$

Key parameters:
- **Natural frequency**: $\omega_n = 1/\sqrt{LC}$
- **Damping ratio**: $\zeta = \frac{R}{2}\sqrt{C/L}$

| $\zeta$ | Behavior | Example |
|---|---|---|
| $\zeta > 1$ | Overdamped — slow exponential return | Heavy resistance, sluggish response |
| $\zeta = 1$ | Critically damped — fastest no-overshoot | Optimal transient in many power supplies |
| $\zeta < 1$ | Underdamped — oscillatory ring | LC tank in a radio tuner; ringing in switching supplies |
| $\zeta = 0$ | Undamped — sustains oscillation | Lossless LC oscillator |

### Applications
- **LC tank circuits (radio tuning)**: Tune $L$ and $C$ so $\omega_n = 2\pi f_\text{station}$. The DiffEQ tells you the resonant frequency.
- **Power supply output filter**: A buck converter output LC filter must be critically damped to avoid output voltage ringing.
- **Audio crossover networks**: RLC combinations implement Butterworth/Chebyshev filter polynomials — all from 2nd-order ODE families.

---

## Laplace Transforms — The Engineering Shortcut

Solving ODEs with initial conditions every time is tedious. The Laplace transform converts the ODE to an algebraic equation in the complex frequency domain ($s$-domain):

$$L\{f'(t)\} = sF(s) - f(0)$$

Example: the RLC ODE becomes:
$$LCs^2V_C(s) + RCsV_C(s) + V_C(s) = V_s(s) + \text{IC terms}$$
$$\Rightarrow \quad H(s) = \frac{V_C(s)}{V_s(s)} = \frac{1/LC}{s^2 + (R/L)s + 1/LC}$$

This $H(s)$ is the **transfer function** — the single most important tool in EEE 202 and EEE 350 (Signals & Systems). It encodes:
- Pole locations → transient behavior
- Frequency response → $|H(j\omega)|$ vs $\omega$ (Bode plot)
- Stability → all poles in left half plane?

---

## Control Systems — DiffEQ at System Level (EEE 480)

A DC motor with speed control:
$$J\frac{d\omega}{dt} + b\omega = K_\tau i_a$$
$$L_a\frac{di_a}{dt} + R_a i_a = V_a - K_e\omega$$

This is a coupled system of two first-order ODEs (2nd-order system overall). A **PID controller** modifies the input based on the error $e(t) = \omega_\text{ref} - \omega$:
$$V_a = K_p e + K_i \int e\,dt + K_d \frac{de}{dt}$$

The closed-loop dynamics are determined by the characteristic polynomial of the combined ODE system — placing poles (choosing $K_p, K_i, K_d$) is exactly solving differential equation eigenvalue problems.

---

## Op-Amp Circuits That Are Analog Computers

- **Integrator**: $V_\text{out} = -\frac{1}{RC}\int V_\text{in}\,dt$ — literally performs integration in hardware
- **Differentiator**: $V_\text{out} = -RC\frac{dV_\text{in}}{dt}$ — literally computes derivatives
- **Second-order active filter** (Sallen-Key topology): implements an arbitrary 2nd-order transfer function with op-amps, Rs, and Cs

Before digital computers, engineers used op-amp analog computers to simulate differential equations in real time — solving ballistic trajectories, aircraft dynamics, etc.

---

## Maxwell's PDEs

At the EM level, differential equations become partial differential equations:
$$\nabla^2 \mathbf{E} = \mu\varepsilon\frac{\partial^2\mathbf{E}}{\partial t^2}$$

This is the **electromagnetic wave equation** — a second-order PDE whose solutions are traveling waves with speed $c = 1/\sqrt{\mu\varepsilon}$. The entire field of RF/microwave engineering and antenna design flows from this equation.

---

## Summary: Where DiffEQ Appears in the EE Curriculum

| DiffEQ Type | Circuit Context | EE Course |
|---|---|---|
| 1st-order ODE | RC/RL transients; filter time constants | EEE 202 |
| 2nd-order ODE | RLC circuits; resonance; damping | EEE 202 |
| Laplace / transfer functions | System analysis; Bode plots | EEE 202, EEE 350 |
| Coupled ODEs (state space) | Motor dynamics; multi-loop circuits | EEE 480 |
| PDE (wave equation) | EM waves; transmission lines; antennas | EEE 340, EEE 476 |
| Numerical ODE (SPICE) | LTspice transient simulation | All lab courses |

---

## Related
- [[Calculus in Electrical Engineering]]
- [[Electromagnetism Foundations for EE]]
- [[Classical Mechanics in Electrical Engineering]]
- [[EE Physical Side — Actionable Skill Plan]]
