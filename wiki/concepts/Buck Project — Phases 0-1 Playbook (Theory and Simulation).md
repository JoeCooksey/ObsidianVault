---
type: project
title: "Buck Project — Phases 0-1 Playbook (Theory and Simulation)"
status: developing
created: 2026-05-29
updated: 2026-05-29
tags:
  - project
  - power-electronics
  - playbook
  - simulation
related:
  - "[[Project - Digitally Controlled Synchronous Buck Converter]]"
  - "[[Signals and Systems — Laplace and Fourier]]"
  - "[[LTSpice Complete Skills Guide]]"
  - "[[Calculus in Electrical Engineering]]"
---

# Buck Project — Phases 0–1 Playbook (Theory & Simulation)

The "understand it before you build it" block. No hardware yet — pen, paper, Python, and a simulator. **If you do nothing else, do this**: a converter you don't understand on paper you can't debug on the bench.

> Spec reminder (from [[Project - Digitally Controlled Synchronous Buck Converter]]): 12 V → 5 V, 3 A, f_sw = 100 kHz. So **duty D = V_out/V_in = 5/12 = 0.417**.

## Phase 0 — Theory & modeling (~3 weeks)

### Week 1 — How a buck actually works
- **Learn:** A buck = a switch that chops 12 V into a square wave, then an L–C low-pass filter that averages it to 5 V. "Synchronous" just means the bottom diode is replaced by a second MOSFET (less loss).
- **Do:** Watch a buck-converter explainer (search "buck converter operation Neso Academy" or read **Erickson, *Fundamentals of Power Electronics*, Ch. 2** — the field bible). Then by hand: use **volt-second balance** (the inductor's average voltage over one cycle = 0) to derive D = V_out/V_in. Plug in numbers: D = 0.417.
- **Deliverable:** a half-page derivation of D in your own handwriting.

### Week 2 — The ripple equations (these size your parts)
- **Learn:** the inductor current isn't flat — it ramps up and down (triangle). That swing is **ΔI_L**. The cap smooths the leftover into output voltage ripple **ΔV_out**.
- **Do (hand calc):**
  - Inductor ripple: `ΔI_L = (V_in − V_out)·D / (f_sw·L)`. Target ΔI_L = 30% of 3 A = **0.9 A** → solve for L → **≈33 µH**.
  - Peak inductor current: `I_peak = I_out + ΔI_L/2 = 3.45 A`.
  - Output ripple (ceramic cap): `ΔV_out ≈ ΔI_L / (8·f_sw·C)`. Target <50 mV → **C ≈ 22–44 µF**.
- **Deliverable:** the three numbers above, each with the formula you used. You'll reuse these verbatim in Phase 2.

### Week 3 — The small-signal model (the "plant" you'll control)
- **Learn:** to design the digital controller later, you need the **control-to-output transfer function** G_vd(s) — how a wiggle in duty changes V_out. For a voltage-mode buck it's a **second-order system**: an L–C resonant double-pole.
- **Do:** in Python (your `ee-venv` with `python-control`, `numpy`, `matplotlib`): plot the Bode of
  `G_vd(s) = V_in / (1 + s/(Q·ω₀) + (s/ω₀)²)`, where `ω₀ = 1/√(L·C)`.
  - Compute the resonant frequency: `f₀ = 1/(2π√(LC))` ≈ **4.2 kHz** with L=33 µH, C=44 µF.
  - Notice: the phase drops ~180° past f₀. That's *why* you'll need a Type-III compensator later — remember this plot.
- **Deliverable:** a Bode plot of G_vd(s) you can explain (where's the LC peak? where does phase fall?).
- **Resources:** [[Signals and Systems — Laplace and Fourier]] for transfer functions; [[Calculus in Electrical Engineering]] for the derivation.

> [!check] Phase 0 done when: you can derive D and the ripple equations from scratch, and you have a labeled Bode plot of the plant.

## Phase 1 — Open-loop simulation (~2 weeks)

### Week 1 — Build the ideal buck in LTSpice
- **Do:** open **LTSpice** (or ngspice — both installed, [[EE-Software-on-Linux-Mint]]). Place: a `V` source = 12 V; a voltage-controlled **switch** (start ideal) driven by a `PULSE` source at 100 kHz, duty 0.417; your L = 33 µH; C = 44 µF; load R = V_out/I_out = 5/3 = **1.67 Ω**.
- **Run a `.tran` transient.** Watch V_out rise and settle near 5 V. Measure the ripple (zoom in) — does it match your Phase-0 number?
- **Sweep:** change duty to 0.3 and 0.5; confirm V_out ≈ D·12. This proves your model.
- **Deliverable:** screenshot of V_out settling to 5 V + a ripple measurement matching theory.

### Week 2 — Add reality
- **Do:** swap the ideal switch for two **real MOSFET models** (synchronous: high-side + low-side) with a gate-driver behavior and a small **dead-time** (both off briefly so they don't short 12 V to ground). Add the inductor's DCR and cap ESR. Re-run; estimate efficiency = P_out/P_in from the sim.
- **Stretch (optional):** verify your Phase-0 plant Bode using LTSpice's averaged/PWM-switch model — advanced, skip if it stalls you.
- **Resources:** [[LTSpice Complete Skills Guide]], [[Research - LTSpice Skills Guide]] (your own 10-circuit ladder + directives).

> [!check] Phase 1 done when: the sim regulates 5 V at your target ripple, V_out tracks duty, and you have a sim efficiency estimate. **Now you've validated the design in software before spending a dollar.**

## Common beginner mistakes (Phases 0–1)
- Skipping the hand math and going straight to sim — then you can't tell when the sim is wrong.
- Forgetting dead-time → the sim shows huge current spikes (shoot-through). That's a *real* failure mode you're learning to prevent.
- Using ideal caps forever — real ESR changes the ripple and the loop; add it in Week 2.

→ Next: [[Buck Project — Phases 2-3 Playbook (Power Stage and PCB)]]
