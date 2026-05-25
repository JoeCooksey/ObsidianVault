---
type: concept
title: "Laplace Transform in Circuit Analysis"
created: 2026-05-03
updated: 2026-05-03
tags:
  - EE
  - circuits
  - Laplace
  - s-domain
  - transfer-function
  - circuit-analysis
status: developing
---
# Laplace Transform in Circuit Analysis

The Laplace transform converts every circuit analysis problem from solving differential equations to manipulating algebra. The moment you replace each component with its $s$-domain model, KVL and KCL still apply — but now the "impedances" of capacitors and inductors are just algebraic fractions.

---

## The Central Insight: s-Domain Element Models

Every passive element gets a complex impedance that depends on $s$:

| Element | Time Domain | $s$-Domain Impedance $Z(s)$ | Admittance $Y(s) = 1/Z$ |
|---------|------------|---------------------------|------------------------|
| Resistor $R$ | $v = iR$ | $Z_R = R$ | $Y_R = 1/R$ |
| Capacitor $C$ | $i = C\,dv/dt$ | $Z_C = \dfrac{1}{sC}$ | $Y_C = sC$ |
| Inductor $L$ | $v = L\,di/dt$ | $Z_L = sL$ | $Y_L = \dfrac{1}{sL}$ |

**Why these are correct:**
- Capacitor: $I_C(s) = sC \cdot V_C(s)$, so $Z_C = V_C/I_C = 1/(sC)$
- Inductor: $V_L(s) = sL \cdot I_L(s)$, so $Z_L = V_L/I_L = sL$

These reduce to phasor impedances at steady state: set $s = j\omega$ and you recover $Z_C = 1/j\omega C$, $Z_L = j\omega L$ — exactly what phasor analysis uses.

---

## Handling Initial Conditions

The differentiation property $\mathcal{L}\{f'\} = sF(s) - f(0^-)$ produces initial-condition terms. In circuit models, these appear as **source terms in series or parallel with the element**.

### Capacitor with Initial Voltage $V_0 = v_C(0^-)$

Series model (voltage source form):
$$\frac{1}{sC}\,I(s) + \frac{V_0}{s} = V_C(s)$$

This is a capacitor impedance $1/sC$ in series with a voltage source $V_0/s$.

### Inductor with Initial Current $I_0 = i_L(0^-)$

Series model (voltage source form):
$$sL\,I(s) - LI_0 = V_L(s)$$

This is an inductor impedance $sL$ in series with a voltage source $LI_0$ (the "back-EMF" from the stored magnetic energy).

**The big advantage:** Initial conditions are automatically included as algebraic source terms. With classical ODE methods, you solve the homogeneous equation separately to match initial conditions — extra work that Laplace makes unnecessary.

---

## Analysis Procedure

1. **Transform** each source to the $s$-domain (step input → $V_s/s$; impulse → $V_s$)
2. **Replace** each R, L, C with its $s$-domain impedance; add IC source terms if applicable
3. **Write** KVL or KCL — now purely algebraic (no derivatives)
4. **Solve** the algebraic equations for the desired voltage or current in the $s$-domain
5. **Inverse transform** via partial fractions to get the time-domain answer

---

## Worked Example 1: RC Low-Pass Filter — Step Response

**Circuit:** Voltage source $v_s(t) = V_s \cdot u(t)$ in series with $R$ and $C$. Find $v_C(t)$.

**Step 1:** $V_s(s) = V_s/s$

**Step 2:** S-domain circuit is $V_s/s$ → $R$ → $Z_C = 1/sC$ → (output across $C$)

**Step 3:** Voltage divider in the $s$-domain:

$$V_C(s) = V_s(s) \cdot \frac{Z_C}{R + Z_C} = \frac{V_s}{s} \cdot \frac{1/sC}{R + 1/sC} = \frac{V_s/RC}{s\left(s + \dfrac{1}{RC}\right)}$$

**Step 4:** Partial fractions with $\tau = RC$:

$$V_C(s) = \frac{V_s}{s} - \frac{V_s}{s + 1/\tau}$$

**Step 5:** Inverse transform:

$$\boxed{v_C(t) = V_s\left(1 - e^{-t/\tau}\right)u(t)}$$

**Transfer function** (ratio output/input in s-domain, zero ICs):

$$H(s) = \frac{V_C(s)}{V_s(s)} = \frac{1/RC}{s + 1/RC} = \frac{\omega_c}{s + \omega_c}$$

where $\omega_c = 1/RC$ is the cutoff frequency. One pole at $s = -1/RC$ (LHP → stable).

---

## Worked Example 2: RLC Series Circuit — Underdamped Response

**Circuit:** Step voltage $V_s \cdot u(t)$ drives a series $R$-$L$-$C$. Find $v_C(t)$ for zero initial conditions.

**S-domain KVL:**

$$V_s(s) = I(s)\left(R + sL + \frac{1}{sC}\right)$$

$$I(s) = \frac{V_s/s}{R + sL + 1/sC}$$

**Transfer function for $V_C$:**

$$H(s) = \frac{V_C(s)}{V_s(s)} = \frac{1/LC}{s^2 + (R/L)s + 1/LC}$$

**Identify parameters:**
- Natural frequency: $\omega_n = 1/\sqrt{LC}$
- Damping ratio: $\zeta = \dfrac{R}{2}\sqrt{\dfrac{C}{L}} = \dfrac{R}{2L\omega_n}$
- Damped natural frequency: $\omega_d = \omega_n\sqrt{1-\zeta^2}$ (for $\zeta < 1$)

**Poles of $H(s)$:**

$$s_{1,2} = -\zeta\omega_n \pm j\omega_d$$

**For underdamped ($\zeta < 1$):** complex conjugate poles → damped oscillation

$$v_C(t) = V_s\left[1 - \frac{e^{-\zeta\omega_n t}}{\sqrt{1-\zeta^2}}\sin\left(\omega_d t + \phi\right)\right]u(t)$$

where $\phi = \arccos(\zeta)$.

**Interpretation of pole positions:**
- Moving poles left (more negative $\sigma$) → faster decay, more damping
- Moving poles away from the real axis (larger $\omega_d$) → faster oscillation
- Critically damped ($\zeta = 1$): poles meet on the real axis, $s = -\omega_n$ (double pole)

---

## Worked Example 3: RL Circuit with Nonzero Initial Condition

**Circuit:** Series $R$-$L$ with initial inductor current $I_0 = 2$ A. Source switches off at $t=0$.

**S-domain model:** With $V_s(s) = 0$, the inductor provides its IC source $LI_0$:

$$L I_0 = I(s)(R + sL)$$

$$I(s) = \frac{LI_0}{sL + R} = \frac{I_0}{s + R/L}$$

**Inverse:**

$$i(t) = I_0\, e^{-Rt/L}\,u(t)$$

The inductor "rings down" through the resistor. This is inductive kickback — the stored energy $\frac{1}{2}LI_0^2$ must go somewhere when the switch opens.

---

## Transfer Function Definition and Meaning

$$H(s) = \frac{\text{Output}(s)}{\text{Input}(s)}\bigg|_{\text{zero initial conditions}}$$

A transfer function:
- Fully describes any LTI system's input-output behavior
- Is independent of the specific input — it's a property of the circuit
- Gives frequency response by substituting $s = j\omega$: $H(j\omega)$ is the steady-state gain and phase shift at frequency $\omega$
- Has poles that determine transient response and stability
- Has zeros that determine frequency shaping (notches, boosts)

### Standard Forms

**First-order system:**
$$H(s) = \frac{K\omega_c}{s + \omega_c} \quad \text{(low-pass)} \qquad H(s) = \frac{Ks}{s+\omega_c} \quad \text{(high-pass)}$$

**Second-order system (standard form):**
$$H(s) = \frac{K\omega_n^2}{s^2 + 2\zeta\omega_n s + \omega_n^2}$$

Reading off $\omega_n$ and $\zeta$ from the denominator tells you everything about the transient.

---

## Nodal and Mesh Analysis in the $s$-Domain

The same systematic methods from resistive circuit analysis work exactly in the $s$-domain — just use impedances $Z(s)$ instead of $R$:

**Nodal analysis:** Write KCL at each node using $I = V/Z(s)$. Result: system of algebraic equations in $V_1(s), V_2(s), \ldots$

**Mesh analysis:** Write KVL around each mesh. Result: $[Z]\,[I] = [V]$ where $[Z]$ is the impedance matrix, solvable by Cramer's rule or matrix inversion.

Both methods produce rational functions in $s$, ready for partial fractions.

---

## Frequency Response from the Transfer Function

To find the steady-state frequency response, substitute $s = j\omega$:

$$H(j\omega) = |H(j\omega)|\,e^{j\angle H(j\omega)}$$

- $|H(j\omega)|$: magnitude (gain) at frequency $\omega$
- $\angle H(j\omega)$: phase shift at frequency $\omega$

**Example — RC low-pass:**
$$H(j\omega) = \frac{\omega_c}{j\omega + \omega_c} = \frac{1}{1 + j\omega/\omega_c}$$

$$|H(j\omega)| = \frac{1}{\sqrt{1 + (\omega/\omega_c)^2}}$$

- At $\omega = \omega_c$: $|H| = 1/\sqrt{2} \approx 0.707$ → this is the $-3$ dB point
- At $\omega \ll \omega_c$: $|H| \approx 1$ (passband)
- At $\omega \gg \omega_c$: $|H| \approx \omega_c/\omega$ → decays at $-20$ dB/decade (1 pole)

---

## Application: Buck Converter Small-Signal Model

This is where circuit Laplace directly meets power electronics. A buck converter running at duty cycle $D$ has a linearized (small-signal) model around its operating point. The output voltage-to-duty-cycle transfer function:

$$G_{vd}(s) = \frac{\hat{v}_o(s)}{\hat{d}(s)} = \frac{V_g}{LC} \cdot \frac{1}{s^2 + \frac{s}{RC} + \frac{1}{LC}}$$

where $V_g$ is the input voltage, $L$ and $C$ are the output filter values, $R$ is the load.

This is a second-order system with:
- $\omega_n = 1/\sqrt{LC}$ (filter resonant frequency)
- $\zeta = \frac{1}{2R}\sqrt{L/C}$

**Why this matters for WBG design:** The output filter pole frequency $\omega_n$ and the control loop crossover frequency must be carefully separated. At high switching frequencies (enabled by SiC/GaN), $L$ and $C$ shrink, pushing $\omega_n$ higher and enabling faster dynamic response.

The control loop designer uses $G_{vd}(s)$ to design a compensator (type II or type III) to achieve desired gain margin and phase margin — all in the $s$-domain.

---

## Summary: Why Laplace is the EE's Primary Circuit Tool

| Problem | Without Laplace | With Laplace |
|---------|----------------|-------------|
| RC step response | Solve 1st-order ODE, match ICs | Partial fractions on $H(s)$ |
| RLC transient | Solve 2nd-order ODE, homogeneous + particular | Factor $H(s)$, read off poles directly |
| Cascaded filters | Convolve impulse responses | Multiply transfer functions |
| Initial conditions | Separate work | Automatic in element models |
| Stability check | Solve characteristic equation | Inspect pole locations |
| Frequency response | Derive from ODE solution | Substitute $s = j\omega$ |

---

## Related Concepts
- [[Laplace Transform — Mathematical Foundations]]
- [[Transfer Functions and Poles Zeros]]
- [[Circuit Theory Fundamentals]]
- [[Differential Equations in Electrical Engineering]]
- [[Signals and Systems — Laplace and Fourier]]
- [[EV Fast Charging Topologies]]
