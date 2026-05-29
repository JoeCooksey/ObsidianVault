---
type: project
title: "Buck Project — Phases 4-6 Playbook (Bring-up, Firmware, Validation)"
status: developing
created: 2026-05-29
updated: 2026-05-29
tags:
  - project
  - power-electronics
  - playbook
  - firmware
  - digital-control
related:
  - "[[Project - Digitally Controlled Synchronous Buck Converter]]"
  - "[[Buck Project — Phases 2-3 Playbook (Power Stage and PCB)]]"
  - "[[C++ Self-Teaching Roadmap for EE]]"
  - "[[Signals and Systems — Laplace and Fourier]]"
  - "[[STM32G4 Digital Power Buck Reference]]"
---

# Buck Project — Phases 4–6 Playbook (Bring-up, Firmware, Validation)

The board arrived. Now make it work — *safely* — then make it controlled, then prove it. This is the deepest stretch and the most satisfying.

## Phase 4 — Bring-up & open-loop bench test (~2 weeks)

### Week 1 — Solder & inspect
- **Do:** solder the power parts first (FETs, inductor, caps, driver), then the small signal parts. Under good light, inspect for bridges. **Multimeter continuity check: confirm no short between V_in and GND, and V_out and GND.**
- **Deliverable:** a populated board that passes the short check.

### Week 2 — First power (the careful part)
- **Do, in this exact order:**
  1. Bench PSU to **12 V, current limit 0.1 A**, no load, no PWM yet. Connect. It should draw almost nothing. If it slams into current limit → you have a short; stop and find it.
  2. Program the MCU to output a **fixed open-loop PWM** (duty 0.417, low f_sw to start) with dead-time, *no feedback*. Add a small load (the 1.67 Ω, or a power resistor).
  3. Raise the current limit to ~4 A. Scope the **SW node** — you should see a clean 12 V square wave with short dead-time notches (no shoot-through spikes).
  4. Measure V_out — should be ≈5 V. Sweep duty, confirm it tracks. Take a first efficiency point.
- **Deliverable:** a scope photo of the SW node + a table of V_out vs duty matching your Phase-1 sim.

> [!warning] Always bring up behind a current limit, glasses on. If anything smells hot or smokes, kill power. Low voltage (12 V) won't shock you, but a shorted FET or reversed electrolytic can vent.

> [!check] Phase 4 done when: open-loop regulated output, clean SW node, first efficiency number.

## Phase 5 — Digital control firmware (~4–5 weeks)

This is the heart of the project. Tooling: **STM32CubeIDE** (on your [[C++ Self-Teaching Roadmap for EE]] path). Reference designs: [[STM32G4 Digital Power Buck Reference]] (ST AN4539 HRTIM cookbook has a worked sync-buck).

### Week 1 — PWM + ADC plumbing
- **Do:** in CubeMX, configure **HRTIM** for complementary PWM (high + low side) with programmable **dead-time**. Configure the **ADC triggered by the timer** so it samples V_out at the same point every cycle (sample near mid-cycle to read the average, not the ripple).
- **Deliverable:** scope confirms PWM + dead-time; debugger shows ADC reading a sane V_out value.

### Week 2 — The measurement → error path
- **Do:** in the control ISR: read ADC → scale counts to volts → compute **error = V_ref − V_out** (V_ref = 5 V, in ADC counts). Verify the numbers in the debugger by changing the load by hand.
- **Deliverable:** a live, correct error signal you can watch.

### Week 3 — Design the compensator (back to math)
- **Do:** take the plant G_vd(s) from Phase 0. Because it's an L–C double-pole (phase falls ~180°), design a **Type-III compensator** (two zeros, gives phase *boost*) for: **crossover ≈ f_sw/10 = 10 kHz**, **phase margin ≥ 45°**. Use Python (`python-control`) to place the poles/zeros and check the resulting loop Bode.
- **Deliverable:** an analog compensator C(s) with a loop-gain Bode showing your target crossover and PM.
- **Resource:** Christophe Basso's compensator design material is the authority; [[Signals and Systems — Laplace and Fourier]] for the s-domain work.

### Week 4 — Discretize & implement
- **Do:** convert C(s) → discrete C(z) with the **bilinear (Tustin) transform** (`c2d` in Python). That gives difference-equation coefficients. Implement in the ISR:
  `y[n] = b0·x[n] + b1·x[n−1] + b2·x[n−2] − a1·y[n−1] − a2·y[n−2]`, where x = error, y = duty command.
- **Sampling note:** if you can't finish the ISR every switching cycle, sample at **f_s ≈ f_sw/3**. The **DPWM adds phase lag** — it eats some of your phase margin, so design with margin to spare.
- **Deliverable:** the difference equation running in the ISR, output clamped to legal duty.

### Week 5 — Close the loop (carefully)
- **Do:** enable feedback with **low gain first**. Add **soft-start** (ramp the reference) and **anti-windup** (stop the integrator running away when duty saturates). Watch V_out on the scope — if it oscillates, you're near instability; back off gain or revisit the compensator.
- **Deliverable:** closed-loop regulation holding 5 V.

> [!check] Phase 5 done when: the loop holds 5 V and recovers when you change the input voltage or the load by hand.

## Phase 6 — Closed-loop validation (~3–4 weeks)

Now *prove* it with data — these plots are what go in your portfolio.

### Loop-gain Bode (the professional measurement)
- **Two options:**
  - **Physical:** insert a 10–50 Ω resistor in the feedback path, inject a small AC sweep across it, measure with a network analyzer (Bode 100).
  - **Budget win — SFRA (Software Frequency Response Analysis):** have the *firmware* inject a sine and measure the response, so the controller plots its own loop gain. **No expensive analyzer needed** — this is how TI's powerSUITE does it, and it's a standout résumé feature.
- **Deliverable:** measured loop-gain Bode → read off crossover and phase margin; compare to your Phase-5 design.

### Load-transient test
- **Do:** step the load 1 A ↔ 3 A (a MOSFET + signal generator makes a load step). Scope V_out recovery: overshoot and settling time. Tune the compensator if it's sluggish or rings.
- **Deliverable:** a transient-response scope capture.

### Efficiency curve
- **Do:** sweep load 0.5 → 3 A, record P_in and P_out, plot **η vs I_out**. Find peak efficiency.
- **Deliverable:** an efficiency plot.

### Double-Pulse Test (stretch / advanced)
- Characterize the FET turn-on/off switching loss (method standardized in IEC 60747-8/9). This connects directly to [[WBG Thermal Management]] and your DPT-analyzer track in [[Python EE Project Ladder - Advanced Tracks]].

> [!check] Phase 6 done when: you have three plots — loop-gain Bode (PM ≥ 45°), load transient, efficiency curve — each compared against your design prediction.

## Common beginner mistakes (Phases 4–6)
- Powering up at full current with no limit → one mistake destroys the board.
- ISR too slow for the sample rate → the loop runs on stale data and goes unstable.
- Designing the compensator without enough phase margin → the DPWM lag tips it into oscillation on the bench.
- Integrator wind-up at startup → big overshoot; add soft-start + anti-windup.

→ Finish with **Phase 7 (publish)** in [[Project - Digitally Controlled Synchronous Buck Converter]]: README + schematic + these three plots + the control writeup on GitHub. That's the deep work becoming a visible career asset ([[Building in Public]]).
