---
type: concept
title: "Calculus in Electrical Engineering"
status: developing
created: 2026-04-19
updated: 2026-04-19
tags:
  - mathematics
  - calculus
  - electrical-engineering
  - foundations
---

# Calculus in Electrical Engineering

Every EE course from Circuits I onward uses calculus continuously. Here is where each semester of calc shows up in practice.

---

## Calculus 1 — Differentiation

**Core EE use: rates of change in circuits.**

### Voltage and current relationships
- **Capacitor current**: $i(t) = C \dfrac{dv}{dt}$ — the current into a cap equals capacitance times the rate of voltage change. If you charge a 100 μF cap and the voltage rises at 1000 V/s, you're sourcing 100 mA.
- **Inductor voltage**: $v(t) = L \dfrac{di}{dt}$ — voltage across an inductor equals inductance times rate of current change. This is why inductors resist sudden current changes; a steep di/dt demands a large voltage spike.

### Instantaneous power
$p(t) = v(t) \cdot i(t)$ — power at any moment. Differentiate energy to get power: $p = dW/dt$.

### Slew rate
Op-amp slew rate (V/μs) is literally a derivative limit — the maximum dV/dt the output can achieve. Exceeding it causes waveform distortion.

### Linearization / small-signal models
Diode I-V is exponential ($I = I_S(e^{V/V_T}-1)$). Engineers take the derivative at the operating point $Q$ to get the small-signal resistance $r_d = dV/dI|_Q = V_T/I_Q$. This linearization is the foundation of all BJT/MOSFET small-signal analysis (EEE 303 / EEE 334).

---

## Calculus 2 — Integration and Series

**Core EE use: energy storage, RMS values, Fourier series.**

### Charge and energy
- Charge stored: $q = \int i \, dt$ — integrating current over time gives charge.
- Energy in a capacitor: $W = \int_0^V C v \, dv = \tfrac{1}{2}CV^2$
- Energy in an inductor: $W = \int_0^I L i \, di = \tfrac{1}{2}LI^2$

### RMS values — critical for AC power
$$V_\text{rms} = \sqrt{\frac{1}{T}\int_0^T v^2(t)\,dt}$$
For a 120 V outlet the peak is 170 V; the RMS is 120 V. You need integration to prove it. Average power dissipated in a resistor: $P = V_\text{rms}^2 / R$.

### Fourier Series (Calc 2 + trig series)
Any periodic signal can be decomposed into sinusoids:
$$v(t) = a_0 + \sum_{n=1}^\infty \left[a_n \cos(n\omega_0 t) + b_n \sin(n\omega_0 t)\right]$$
Coefficients $a_n, b_n$ are integrals over one period. This is how a spectrum analyzer works — it reveals which harmonics are present. Used extensively in signals & systems (EEE 350).

### Convolution
The output of any LTI circuit: $y(t) = (x * h)(t) = \int_{-\infty}^{\infty} x(\tau)h(t-\tau)\,d\tau$. Convolution in time domain = multiplication in frequency domain (Laplace/Fourier). Foundation of filter design.

---

## Calculus 3 — Multivariable and Vector Calculus

**Core EE use: Maxwell's equations, field calculations, transmission lines.**

### Gradient, divergence, curl
Maxwell's equations are written with these operators:
- $\nabla \cdot \mathbf{E} = \rho/\varepsilon_0$ (Gauss's law in differential form)
- $\nabla \times \mathbf{E} = -\partial\mathbf{B}/\partial t$ (Faraday's law)
- $\nabla \times \mathbf{H} = \mathbf{J} + \partial\mathbf{D}/\partial t$ (Ampere-Maxwell law)
- $\nabla \cdot \mathbf{B} = 0$ (no magnetic monopoles)

Without Calc 3, these four equations are uninterpretable.

### Specific applications
- **Capacitor electric field**: Use Gauss's law (surface integral) to find $E = \sigma/\varepsilon_0$ between parallel plates → derive $C = \varepsilon A/d$.
- **Inductor magnetic field**: Biot-Savart law uses a line integral over current to find $\mathbf{B}$. Ampere's law uses a closed-loop line integral.
- **Poynting vector**: Power flow density $\mathbf{S} = \mathbf{E} \times \mathbf{H}$ (W/m²). This is a cross product — the direction of EM wave propagation in a transmission line or antenna.
- **Laplace's equation**: $\nabla^2 V = 0$ (in source-free regions). Used to find voltage distribution in 2D/3D geometries — PCB trace fields, coaxial cable analysis.
- **Stokes' theorem**: Converts surface integrals of curl to line integrals around a boundary — used to derive Faraday's law in integral form from its differential form.

### Transmission lines
The telegrapher's equations require partial derivatives in both space and time:
$$\frac{\partial V}{\partial x} = -L'\frac{\partial I}{\partial t}, \quad \frac{\partial I}{\partial x} = -C'\frac{\partial V}{\partial t}$$
Solving these gives the wave equation — essential for RF, PCB signal integrity at >~100 MHz.

---

## Summary Table

| Calc Course | Key Tool | EE Application | Course Where Used |
|---|---|---|---|
| Calc 1 | Derivative | Cap/inductor V-I relations; slew rate; small-signal models | EEE 202, 303 |
| Calc 1 | Linearization | BJT/MOSFET bias + small-signal analysis | EEE 303, 334 |
| Calc 2 | Definite integral | Energy storage (½CV², ½LI²); charge accumulation | EEE 202 |
| Calc 2 | RMS integral | AC power calculations; power factor | EEE 202 |
| Calc 2 | Fourier series | Signal spectrum; harmonic distortion | EEE 350 |
| Calc 2 | Convolution | LTI system output; filter response | EEE 350 |
| Calc 3 | Gradient/div/curl | Maxwell's equations; EM fields | EEE 340 |
| Calc 3 | Surface/line integrals | Capacitance, inductance derivations from first principles | EEE 340 |
| Calc 3 | Partial derivatives | Transmission line wave equation | EEE 340, 476 |

---

## Related
- [[Differential Equations in Electrical Engineering]]
- [[Electromagnetism Foundations for EE]]
- [[ASU EE Year 1-2 Curriculum Map]]
- [[EE Freshman Self-Study Stack]]
