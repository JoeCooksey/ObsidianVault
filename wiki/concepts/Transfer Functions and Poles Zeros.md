---
type: concept
title: "Transfer Functions and Poles Zeros"
created: 2026-05-03
updated: 2026-05-03
tags:
  - EE
  - control-systems
  - transfer-function
  - stability
  - Bode-plot
  - s-domain
  - signals-and-systems
status: developing
---
# Transfer Functions, Poles, Zeros, and Stability

The transfer function is the complete description of a linear time-invariant (LTI) system. Everything about how a circuit, filter, or control loop behaves — its speed, its overshoot, its stability, its frequency selectivity — is encoded in the pole and zero locations.

---

## Transfer Function Definition

For any LTI system with input $X(s)$ and output $Y(s)$, **assuming zero initial conditions**:

$$H(s) = \frac{Y(s)}{X(s)} = \frac{N(s)}{D(s)} = \frac{b_m s^m + b_{m-1}s^{m-1} + \cdots + b_0}{a_n s^n + a_{n-1}s^{n-1} + \cdots + a_0}$$

- $N(s)$ = numerator polynomial (degree $m$)
- $D(s)$ = denominator polynomial (degree $n$)
- **System order** = $n$ (number of poles; equals number of energy storage elements in a circuit)
- $m \leq n$ for a physically realizable system (can't have more derivatives of input than output)

---

## Poles and Zeros

### Zeros

Roots of the **numerator** $N(s) = 0$:

$$z_1, z_2, \ldots, z_m \quad \text{such that } N(z_k) = 0$$

At $s = z_k$: $H(z_k) = 0$ — the system blocks that input completely.

**Physical meaning:** A zero at $s = j\omega_0$ means the system has zero gain at frequency $\omega_0$. Notch filters exploit this (zero pair on imaginary axis removes a specific frequency).

### Poles

Roots of the **denominator** $D(s) = 0$:

$$p_1, p_2, \ldots, p_n \quad \text{such that } D(p_k) = 0$$

At $s = p_k$: $|H(p_k)| \to \infty$ — the denominator vanishes.

**Physical meaning:** Each pole contributes a natural frequency mode. If you excite the system at $s = p_k$, the response grows without bound (or in the LHP, decays as $e^{p_k t}$).

### Factored Form

$$H(s) = K \cdot \frac{(s-z_1)(s-z_2)\cdots(s-z_m)}{(s-p_1)(s-p_2)\cdots(s-p_n)}$$

$K$ is the **gain constant** (DC gain × leading coefficients).

---

## The $s$-Plane and Stability

Plot all poles (×) and zeros (○) in the complex $s$-plane:

```
    jω  (imaginary axis)
     ↑
     |  ○        |
  ×  |       ×   |    LHP = stable
     |            |   RHP = unstable
  ---+------------+--- σ (real axis)
     |            |
  ×  |            |
     |            |
```

**Stability rules for poles:**

| Pole Location | Time Response | Stability |
|---------------|---------------|-----------|
| Real, negative: $s = -a$ ($a>0$) | $e^{-at}$ — decays | Stable |
| Real, positive: $s = +a$ | $e^{at}$ — grows | **Unstable** |
| Complex pair, LHP: $s = -\sigma \pm j\omega_d$ | $e^{-\sigma t}\cos(\omega_d t)$ — decaying oscillation | Stable |
| Complex pair, RHP: $s = +\sigma \pm j\omega_d$ | $e^{+\sigma t}\cos(\omega_d t)$ — growing oscillation | **Unstable** |
| Imaginary pair: $s = \pm j\omega_0$ | $\cos(\omega_0 t)$ — sustained oscillation | Marginally stable |
| Repeated on imaginary axis | $t\cos(\omega_0 t)$ — grows | **Unstable** |
| At origin $s = 0$ (simple) | Constant | Marginally stable |

**BIBO Stability (Bounded-Input Bounded-Output):**
A system is BIBO stable if and only if **all poles are strictly in the left half-plane** (LHP), i.e., $\text{Re}(p_k) < 0$ for all $k$.

---

## Damping Ratio and Natural Frequency (2nd-Order Systems)

For a standard second-order denominator $s^2 + 2\zeta\omega_n s + \omega_n^2$:

- **$\omega_n$** = natural (undamped) frequency → how fast the system wants to oscillate
- **$\zeta$** = damping ratio → how fast oscillation decays

**Poles:** $s_{1,2} = -\zeta\omega_n \pm j\omega_n\sqrt{1-\zeta^2}$

| $\zeta$ | Name | Pole Type | Time Response |
|---------|------|-----------|---------------|
| $\zeta > 1$ | Overdamped | Two real, negative poles | Two decaying exponentials; no oscillation; slow |
| $\zeta = 1$ | Critically damped | Repeated real pole at $-\omega_n$ | Fastest no-overshoot response |
| $0 < \zeta < 1$ | Underdamped | Complex pair in LHP | Decaying oscillation; overshoot |
| $\zeta = 0$ | Undamped | Imaginary pair | Sustained sinusoid |
| $\zeta < 0$ | Negative damping | Complex pair in RHP | Growing oscillation — **unstable** |

**Quick design facts (step response of underdamped 2nd-order):**
- Percent overshoot: $\text{OS\%} = 100\, e^{-\pi\zeta/\sqrt{1-\zeta^2}}$
  - $\zeta = 0.5 \Rightarrow$ OS% ≈ 16%
  - $\zeta = 0.7 \Rightarrow$ OS% ≈ 5% (often the target in control loops)
  - $\zeta = 1.0 \Rightarrow$ OS% = 0%
- Rise time: decreases as $\omega_n$ increases (faster pole)
- Settling time: $t_s \approx 4/(\zeta\omega_n)$ — putting poles further left settles faster

---

## Bode Plots

A Bode plot displays $H(j\omega)$ — the transfer function evaluated on the imaginary axis — as two plots vs. log frequency:

1. **Magnitude plot**: $|H(j\omega)|$ in dB = $20\log_{10}|H(j\omega)|$
2. **Phase plot**: $\angle H(j\omega)$ in degrees

### Asymptotic Bode Rules (Sketching by Hand)

**Starting point:** At $\omega \to 0$, evaluate DC gain $H(0)$; plot as flat line at $20\log_{10}|H(0)|$ dB.

**Each real pole at $s = -\omega_p$** (break frequency $\omega_p$):
- Magnitude: slope decreases by $-20$ dB/decade for $\omega > \omega_p$
- Phase: $-45°$ at $\omega_p$; total $-90°$ shift over 2 decades centered at $\omega_p$

**Each real zero at $s = -\omega_z$**:
- Magnitude: slope increases by $+20$ dB/decade for $\omega > \omega_z$
- Phase: $+45°$ at $\omega_z$; total $+90°$ shift over 2 decades

**Pure integrator** (pole at origin, $s = 0$):
- $-20$ dB/decade from the start; $-90°$ phase constant

**Second-order pair** (complex poles at $\omega_n$):
- Magnitude: $-40$ dB/decade above $\omega_n$
- Resonant peak at $\omega_r = \omega_n\sqrt{1-2\zeta^2}$ (for $\zeta < 0.707$)
- Phase: $-180°$ total shift; $-90°$ at $\omega = \omega_n$

### Example: RC Low-Pass Filter $H(s) = \omega_c/(s+\omega_c)$

- DC gain: 0 dB (magnitude = 1 at $\omega = 0$)
- Pole at $\omega = \omega_c$: magnitude drops $-20$ dB/dec above $\omega_c$
- At $\omega_c$: magnitude is $-3$ dB, phase is $-45°$
- At $10\omega_c$: magnitude ≈ $-20$ dB, phase ≈ $-84°$

---

## Gain Margin and Phase Margin (Stability of Closed-Loop Systems)

When a transfer function $H(s)$ is placed in a feedback loop:

$$\text{Closed-loop} = \frac{H(s)}{1 + H(s)}$$

The closed loop is stable if the **open-loop** $H(s)$ satisfies:

**Phase Margin (PM):**
$$\phi_m = 180° + \angle H(j\omega_{gc})$$
where $\omega_{gc}$ is the **gain crossover frequency** ($|H(j\omega_{gc})| = 1 = 0$ dB).

**Gain Margin (GM):**
$$G_m = -20\log_{10}|H(j\omega_{pc})|$$
where $\omega_{pc}$ is the **phase crossover frequency** ($\angle H(j\omega_{pc}) = -180°$).

**Design targets:**
- Phase margin: $45° \leq \phi_m \leq 70°$ (PM < 45° → excessive overshoot; PM > 70° → sluggish)
- Gain margin: $\geq 6$ dB

**EE application — buck converter control loop:**
A buck converter's control loop has a plant $G_{vd}(s)$ (second-order LC filter with −40 dB/dec roll-off) and a compensator $C(s)$. The open-loop $T(s) = G_{vd}(s) \cdot C(s)$ must cross 0 dB with enough phase margin. Type II or type III compensators add zeros to boost phase margin at the crossover frequency.

---

## Effect of Zeros on Step Response

Zeros modify the step response shape without changing the exponential modes:

- **Zero in LHP** (minimum phase zero): speeds up initial response; increases overshoot
- **Zero in RHP** (non-minimum phase zero): causes initial undershoot — the response goes the "wrong way" before correcting. This is a fundamental limitation in control design. Non-minimum phase zeros are common in boost and flyback converters.
- **Zero at origin** ($s = 0$): forces DC output to zero (high-pass characteristic)

---

## Pole-Zero Cancellation

If a pole and zero coincide at $s = p = z$, they cancel algebraically:

$$H(s) = \frac{(s-z)}{(s-p)(s-q)} \xrightarrow{z=p} \frac{1}{s-q}$$

**Warning:** This cancellation only works if the pole is stable (LHP). Canceling an unstable RHP pole with a zero makes the transfer function look stable but the internal state is still growing — the system is **internally unstable** (not detectable from the output). This is a critical pitfall in control design.

---

## Python: Poles, Zeros, and Bode Plots

```python
import numpy as np
import scipy.signal as sig
import matplotlib.pyplot as plt

# RC low-pass: H(s) = 100/(s + 100)
omega_c = 100  # rad/s
num = [omega_c]
den = [1, omega_c]

system = sig.TransferFunction(num, den)

# Poles and zeros
zeros, poles, gain = sig.tf2zpk(num, den)
print(f"Poles: {poles}")   # [-100.]
print(f"Zeros: {zeros}")   # []

# Bode plot
omega = np.logspace(0, 4, 500)  # 1 to 10000 rad/s
w, mag, phase = sig.bode(system, w=omega)
plt.subplot(2,1,1); plt.semilogx(w, mag)
plt.ylabel('Magnitude (dB)'); plt.title('Bode Plot')
plt.subplot(2,1,2); plt.semilogx(w, phase)
plt.ylabel('Phase (deg)'); plt.xlabel('Frequency (rad/s)')
plt.show()
```

For a second-order RLC:
```python
# RLC: H(s) = omega_n^2 / (s^2 + 2*zeta*omega_n*s + omega_n^2)
omega_n = 1000  # rad/s
zeta = 0.5
num2 = [omega_n**2]
den2 = [1, 2*zeta*omega_n, omega_n**2]
sys2 = sig.TransferFunction(num2, den2)

# Step response
t, y = sig.step(sys2)
# Pole-zero map: sig.tf2zpk(num2, den2)
```

---

## Summary: Reading Poles Tells You Everything

| Poles of $H(s)$ | What You Immediately Know |
|-----------------|--------------------------|
| One real pole at $-1/\tau$ | First-order system, time constant $\tau$, $-20$ dB/dec rolloff |
| Two complex poles at $-\sigma \pm j\omega_d$ | Second-order; decaying oscillation at $\omega_d$ Hz; stability margin $\sigma$ |
| Any pole in RHP | System is unstable — will blow up |
| Poles at $\pm j\omega_0$ | Undamped oscillator at $\omega_0$ (LC tank, crystal) |
| Double real pole at $-\omega_n$ | Critically damped; fastest non-oscillatory response |
| $n$ poles: $n$ energy storage elements | Circuit has $n$ capacitors + inductors total |

---

## Related Concepts
- [[Laplace Transform — Mathematical Foundations]]
- [[Laplace Transform in Circuit Analysis]]
- [[Signals and Systems — Laplace and Fourier]]
- [[Differential Equations in Electrical Engineering]]
- [[EV Fast Charging Topologies]]
- [[Python EE Project Ladder - Phase 2-3]]
