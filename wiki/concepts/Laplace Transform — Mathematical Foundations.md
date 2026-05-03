---
type: concept
title: "Laplace Transform — Mathematical Foundations"
created: 2026-05-03
updated: 2026-05-03
tags:
  - mathematics
  - Laplace
  - transforms
  - signals-and-systems
  - differential-equations
status: developing
---
# Laplace Transform — Mathematical Foundations

The Laplace Transform is an integral transform that converts a function of time $f(t)$ into a function of a complex variable $s$. Its power lies in a single fact: **differentiation in time becomes multiplication in the $s$-domain**, turning differential equations into algebra.

---

## The Definition

### Unilateral (One-Sided) Laplace Transform

$$\mathcal{L}\{f(t)\} = F(s) = \int_0^{\infty} f(t)\, e^{-st}\, dt$$

- $s = \sigma + j\omega$ is a complex frequency variable
- $\sigma = \text{Re}(s)$ is the damping/growth rate
- $\omega = \text{Im}(s)$ is the angular frequency in rad/s
- The lower limit $0^-$ means initial conditions at $t=0$ are captured

The **bilateral** (two-sided) form uses limits $-\infty$ to $\infty$ and is used in signal theory; the unilateral form is standard in circuit analysis and control systems because circuits start at $t=0$.

### The Complex Frequency $s$

$s$ is not a single frequency — it is a plane. The $s$-plane has:
- Real axis $(\sigma)$: controls whether a signal grows, decays, or stays constant
- Imaginary axis $(j\omega)$: controls oscillation frequency
- The combination $e^{st} = e^{\sigma t} \cdot e^{j\omega t}$ = a growing (or decaying) sinusoid

This is why poles in the left half-plane (LHP) correspond to stable, decaying responses.

---

## Region of Convergence (ROC)

The Laplace integral converges only for certain values of $s$. The ROC is the set of $s$ values where the integral is finite.

- For causal signals (one-sided), the ROC is always a **right half-plane**: $\text{Re}(s) > \sigma_0$
- The ROC must include the imaginary axis for the Fourier Transform to exist (stability requirement)
- Poles are **never** inside the ROC (the integral diverges at poles)

**Practical rule:** For most EE problems, all signals are causal and stable, so the ROC is always the right half-plane and you rarely need to think about it explicitly.

---

## Common Laplace Transform Pairs

| Time Domain $f(t)$ | $s$-Domain $F(s)$ | Notes |
|--------------------|-------------------|-------|
| $\delta(t)$ (impulse) | $1$ | Flat spectrum — contains all frequencies |
| $u(t)$ (unit step) | $\dfrac{1}{s}$ | Step input is 1/s |
| $t\,u(t)$ (ramp) | $\dfrac{1}{s^2}$ | Each integration = divide by $s$ |
| $e^{-at}u(t)$ | $\dfrac{1}{s+a}$ | Most important pair — decaying exponential |
| $te^{-at}u(t)$ | $\dfrac{1}{(s+a)^2}$ | Repeated poles |
| $\sin(\omega_0 t)\,u(t)$ | $\dfrac{\omega_0}{s^2+\omega_0^2}$ | Sustained sinusoid |
| $\cos(\omega_0 t)\,u(t)$ | $\dfrac{s}{s^2+\omega_0^2}$ | Sustained cosine |
| $e^{-at}\sin(\omega_0 t)$ | $\dfrac{\omega_0}{(s+a)^2+\omega_0^2}$ | Damped sinusoid (RLC response) |
| $e^{-at}\cos(\omega_0 t)$ | $\dfrac{s+a}{(s+a)^2+\omega_0^2}$ | Damped cosine |
| $t^n u(t)$ | $\dfrac{n!}{s^{n+1}}$ | Polynomial |

**Memory trick:** The exponential $e^{-at}$ shifts the $s$-domain by $a$: $e^{-at}f(t) \leftrightarrow F(s+a)$.

---

## Key Properties

### Linearity
$$\mathcal{L}\{af(t) + bg(t)\} = aF(s) + bG(s)$$

### Differentiation — The Core Property
$$\mathcal{L}\left\{\frac{df}{dt}\right\} = sF(s) - f(0^-)$$

$$\mathcal{L}\left\{\frac{d^2f}{dt^2}\right\} = s^2F(s) - sf(0^-) - f'(0^-)$$

**Why this matters:** $d/dt \to s$. An inductor with $v_L = L\,di/dt$ becomes $V_L(s) = sL\,I(s)$ — algebraic. Initial conditions appear automatically as added source terms. No separate complementary-solution work needed.

### Integration
$$\mathcal{L}\left\{\int_0^t f(\tau)\,d\tau\right\} = \frac{F(s)}{s}$$

Integration in time = divide by $s$. A capacitor with $i_C = C\,dv/dt$ rearranges to $v_C = \frac{1}{C}\int i\,dt$, giving $V_C(s) = \frac{I(s)}{sC}$.

### Convolution Theorem
$$\mathcal{L}\{f(t) * g(t)\} = F(s) \cdot G(s)$$

Convolution in time = multiplication in $s$. This means **cascaded systems multiply their transfer functions** — the most powerful simplification in linear systems analysis.

### Time Shifting
$$\mathcal{L}\{f(t-t_0)u(t-t_0)\} = e^{-st_0}F(s)$$

A time delay of $t_0$ seconds = multiply by $e^{-st_0}$ in the $s$-domain.

### Frequency Shifting (s-Domain Shift)
$$\mathcal{L}\{e^{-at}f(t)\} = F(s+a)$$

### Initial Value Theorem
$$f(0^+) = \lim_{s \to \infty} sF(s)$$

Get the initial value of a signal from its transform — no inverse needed.

### Final Value Theorem
$$\lim_{t \to \infty} f(t) = \lim_{s \to 0} sF(s)$$

**Critical constraint:** Only valid if all poles of $sF(s)$ are in the LHP (stable signal). Used constantly in control systems to find DC steady-state output.

---

## Inverse Laplace: Partial Fraction Decomposition

Going from $F(s)$ back to $f(t)$ is the key computational step. The standard method:

### Step 1: Factor the Denominator
$$F(s) = \frac{N(s)}{D(s)} = \frac{N(s)}{(s+p_1)(s+p_2)\cdots(s+p_n)}$$

### Step 2: Expand into Partial Fractions

**Case 1 — Distinct real poles:**
$$F(s) = \frac{A_1}{s+p_1} + \frac{A_2}{s+p_2} + \cdots$$

Find residues: $A_k = [(s+p_k)F(s)]_{s=-p_k}$ (cover-up method)

**Case 2 — Repeated pole of order $m$:**
$$\frac{A_1}{s+p} + \frac{A_2}{(s+p)^2} + \cdots + \frac{A_m}{(s+p)^m}$$

**Case 3 — Complex conjugate poles** $(s+a)^2 + \omega_0^2$:
$$\frac{As + B}{(s+a)^2 + \omega_0^2} \leftrightarrow e^{-at}[C_1\cos(\omega_0 t) + C_2\sin(\omega_0 t)]$$
These give the damped oscillatory responses seen in underdamped RLC circuits.

### Step 3: Look Up Each Term in the Transform Table

After decomposition, every term maps to a known pair. No integration needed.

### Worked Example: RC Step Response

Circuit: RC series, step input $V_s = 1$ V, zero initial voltage.

$$V_C(s) = \frac{1/RC}{s(s + 1/RC)} = \frac{1/RC}{s \cdot (s+1/\tau)} \quad \text{where } \tau = RC$$

Partial fractions:
$$V_C(s) = \frac{1}{s} - \frac{1}{s + 1/\tau}$$

Inverse transform:
$$v_C(t) = \left(1 - e^{-t/\tau}\right)u(t)$$

This matches the exact result from solving the ODE — but it took algebra, not integration.

---

## Connection to the Fourier Transform

The Fourier Transform is a special case of the Laplace Transform:

$$X(j\omega) = X(s)\big|_{s=j\omega} = \int_{-\infty}^{\infty} x(t)\,e^{-j\omega t}\,dt$$

Setting $\sigma = 0$ (i.e., evaluating on the imaginary axis) gives the Fourier Transform. This is exactly what Bode plots do: substitute $s = j\omega$ into $H(s)$ to get the frequency response.

**Key differences:**
| | Fourier Transform | Laplace Transform |
|--|--|--|
| Variable | $j\omega$ (imaginary axis only) | $s = \sigma + j\omega$ (entire plane) |
| Handles transients | No — needs steady state | Yes — handles initial conditions |
| Region | Imaginary axis | Half-plane |
| EE use | Steady-state frequency response | Complete time-domain response |

The Laplace Transform is strictly more powerful for circuit analysis because it captures both the steady-state (Fourier) and transient behavior in one formula.

---

## Historical Context

Introduced by Pierre-Simon Laplace (~1790) in probability theory. Adopted by electrical engineers in the early 20th century as the primary tool for analyzing linear circuits with energy storage elements. Oliver Heaviside (1850–1925) independently developed operational calculus — essentially the Laplace transform — for telegraph line analysis, decades before it became formalized.

---

## Related Concepts
- [[Signals and Systems — Laplace and Fourier]]
- [[Laplace Transform in Circuit Analysis]]
- [[Transfer Functions and Poles Zeros]]
- [[Differential Equations in Electrical Engineering]]
- [[Python in Electrical Engineering]]
