---
type: project
title: "Project - Digitally Controlled Synchronous Buck Converter"
status: developing
created: 2026-05-29
updated: 2026-06-11
tags:
  - project
  - power-electronics
  - deep-work
  - portfolio
  - digital-control
related:
  - "[[Deep-Work Compounding Projects Tier List]]"
  - "[[EE Physical Side — Actionable Skill Plan]]"
  - "[[Semiconductor Device Fundamentals]]"
  - "[[Signals and Systems — Laplace and Fourier]]"
  - "[[LTSpice Complete Skills Guide]]"
  - "[[Python EE Project Ladder - Advanced Tracks]]"
  - "[[Silicon Carbide Power Electronics]]"
  - "[[C++ Self-Teaching Roadmap for EE]]"
sources:
  - "[[STM32G4 Digital Power Buck Reference]]"
---

# Project — Digitally Controlled Synchronous Buck Converter

> [!check] Progress (2026-06-11): **Phases 0–1 COMPLETE** — repo: `github.com/JoeCooksey/digital-buck-converter`
> - Phase 0: hand derivations (PDF) + G_vd(s) Bode in Python (f₀ ≈ 4.2 kHz)
> - Phase 1 ideal sim: ripple 45 mV ✓ (<50 mV spec), ΔI_L ≈ 0.95 A ✓ (~30% target), startup ring matches the 4.2 kHz double-pole; **open-loop needs D ≈ 0.45, not ideal 0.417** (diode + parasitic drops) — the DC error the Phase 5 loop will null
> - Phase 1 sync sim ("Realness"): 2-FET stage + 200 ns dead time + DCR/ESR → 5.03 V / 3.02 A, **η = 93.6%** with generic .model cards
> - **Now in Phase 2** — replace generic models with real-part datasheet numbers, justify each BOM row, order parts

The S-tier deep-work build from [[Deep-Work Compounding Projects Tier List]]: take **one** power converter from spec to validated hardware, controlled by a microcontroller running a closed loop *you* designed. It exercises every EE layer at once and is the portfolio crown jewel for power-electronics roles.

## Target spec (chosen for a safe, canonical first build)

| Parameter | Value | Why |
|---|---|---|
| Topology | Synchronous buck (2 MOSFETs, no diode) | Canonical, most-documented, highest efficiency |
| Input | 12 V DC (bench supply) | Low-voltage = **safe**; no mains, no shock risk |
| Output | 5 V @ 3 A (15 W) | Useful, undemanding thermals |
| f_sw | 100 kHz to start → 300–500 kHz later | Low first = easier layout/scope; raise once it works |
| Control | Digital voltage-mode, then peak-current-mode | Voltage-mode first (simpler loop) |
| Inductor ripple | ~30% of I_out (≈0.9 A) | Standard design rule |
| Output ripple | <50 mV | Cap + ESR target |

> [!warning] Safety floor
> Stay at 12 V. Current-limit the bench supply to ~4 A. A shorted MOSFET or backwards electrolytic can still vent — wear glasses on first power-up, and bring up behind a current limit every time.

## Platform choice — recommended: STM32G4 (Nucleo-G474RE)

- **STM32G4 (recommended for you):** HRTIM gives 184 ps PWM resolution, FMAC accelerates the 3-pole/3-zero compensator, well-documented via ST **AN4539 (HRTIM cookbook)** which has a synchronous-buck example. ~$15 board, and you already have STM32CubeIDE on your roadmap ([[C++ Self-Teaching Roadmap for EE]]). (Source: [[STM32G4 Digital Power Buck Reference]])
- **TI C2000 (industry-standard alternative):** `LAUNCHXL-F280049C` + `BOOSTXL-BUCKCONV` BoosterPack = a *proven* power stage + powerSUITE/SFRA tooling and the CLA math coprocessor. Pick this if you want the toolchain LLNL/industry actually uses and a de-risked power stage. Trade-off: pricier, heavier toolchain.
- Decision rule: **STM32G4 if you want to design the power stage yourself on a budget; C2000 if you want the industry toolchain and a known-good board to focus purely on control.**

## Step-by-step playbooks (detailed "what to do each week")

The phase summaries below are the map; these three pages are the turn-by-turn directions:
- [[Buck Project — Phases 0-1 Playbook (Theory and Simulation)]] — derive it, simulate it
- [[Buck Project — Phases 2-3 Playbook (Power Stage and PCB)]] — BOM + KiCad board
- [[Buck Project — Phases 4-6 Playbook (Bring-up, Firmware, Validation)]] — solder, control loop, prove it

**Order-ready parts list:** [[Buck Converter BOM (Order-Ready 2026)]] — exact MPNs + June-2026 availability (note: FDMC8030 is now EOL, replaced there).

## The 7 phases (≈6 months at ~1–1.5 hr/day deep block)

### Phase 0 — Theory & modeling (≈3 weeks)
Derive the buck from first principles: volt-second balance, CCM duty D = V_out/V_in, ripple equations. Build the **small-signal average model** (control-to-output transfer function) by hand — this is the plant you'll later compensate. Prereqs you already have pages for: [[Semiconductor Device Fundamentals]], [[Signals and Systems — Laplace and Fourier]], [[Differential Equations in Electrical Engineering]]. *Daily output: one derivation or one plant Bode plot in Python (python-control).*

### Phase 1 — Open-loop simulation (≈2 weeks)
Model the power stage in **LTSpice** (or ngspice — both installed, see [[EE-Software-on-Linux-Mint]]). Verify D, ripple, MOSFET switching, dead-time. Sweep load. Confirm your hand-derived model matches the sim Bode. *Daily output: one simulation experiment logged.* (See [[LTSpice Complete Skills Guide]].)

### Phase 2 — Power-stage design & BOM (≈2 weeks)
Component selection with real math:
- **Inductor:** L = (V_in−V_out)·D / (f_sw·ΔI_L) ≈ 22–33 µH at 100 kHz; pick saturation current > peak.
- **Output cap:** size for ripple + ESR; low-ESR ceramics or polymer.
- **MOSFETs:** two N-channel (e.g., 30 V logic-level); compare R_DS(on) vs gate charge.
- **Gate driver:** half-bridge driver with bootstrap (e.g., UCC27211 / LM5109) + 0.1 µF bootstrap cap BST→SW.
- **Current sense** (for current-mode later): shunt + amp, or inductor-DCR sense.
- **Feedback divider** into the MCU ADC; anti-alias RC.
*Daily output: one component justified with its datasheet number.*

### Phase 3 — PCB layout in KiCad (≈3–4 weeks)
The make-or-break skill. **Minimize the SW-node area** (EMI), keep the power loop (V_in cap → high-side FET → low-side FET → back) tight, star-ground the analog return, place the bootstrap and gate loops short. Fab 5 boards at JLCPCB (~$10). *Daily output: one section of the layout + a layout-rule learned.* (KiCad 10 native on Mint — see [[EE-Software-on-Linux-Mint]].)

### Phase 4 — Bring-up & open-loop bench test (≈2 weeks)
Populate, smoke-test behind a current limit, drive PWM at fixed duty from the MCU (no feedback yet). Scope the SW node, measure V_out vs duty, confirm dead-time, take a first efficiency point. *Daily output: one measured waveform vs the Phase-1 sim prediction.*

### Phase 5 — Digital control firmware (≈4–5 weeks)
The deepest phase. **Design-by-emulation**: design an analog Type-II (voltage-mode) or Type-III compensator for your plant, then discretize (Tustin/bilinear) into a difference equation the MCU runs each ISR.
- Configure HRTIM PWM + ADC **synchronized to PWM** (sample mid-cycle to track the average).
- Sampling: if you can't sample every cycle, use f_sample ≈ f_sw/3.
- Implement the difference equation in the control ISR; watch the DPWM phase-lag eating your phase margin.
Target loop bandwidth ≈ f_sw/10, phase margin ≥ 45°. *Daily output: one control-loop subsystem coded + bench-checked.* (See [[Control Systems]], and the DPT/analysis Python tooling in [[Python EE Project Ladder - Advanced Tracks]].)

### Phase 6 — Closed-loop tuning & validation (≈3–4 weeks)
- **Loop-gain Bode (the pro step):** inject a small signal across a 10–50 Ω resistor in the feedback path and sweep with a network analyzer (Bode 100) — *or*, the budget win: implement **Software Frequency Response Analysis (SFRA)** so the controller measures its own loop gain (TI ships this; doable on STM32). No $1k analyzer needed.
- **Load-transient test:** step the load, scope V_out recovery (overshoot, settling).
- **Efficiency curve:** sweep load, plot η vs I_out.
- **Double-Pulse Test** on the switching cell to characterize turn-on/off losses (codified in IEC 60747-8/9) — ties straight into [[WBG Thermal Management]] and your DPT analyzer track.
*Daily output: one validation measurement + its plot.*

### Phase 7 — Document & publish (ongoing)
README + schematic + measured Bode/transient/efficiency plots + the control-design writeup on GitHub. This is where the deep work becomes the **visible career asset** ([[Building in Public]]) — deep work nobody sees doesn't build the résumé.

## Budget (~$120–500 depending on scope ownership)
- Nucleo-G474RE ~$15 · components ~$40 · PCB (5×) ~$10 · bench PSU (used) ~$60 · electronic load or power resistors ~$30.
- **The real gap is an oscilloscope** — a used 2-ch scope (Rigol DS1054Z ~$350, already on your [[Consumer Purchase Value Tier List]]) is needed for SW-node and transient work. SFRA removes the need for a separate network analyzer.

## Daily-work structure (how to actually grind it)
- **One protected 60–90 min deep block/day** (rhythmic philosophy, phone away — [[Deep Work]]).
- End each session writing the next session's first task + a tiny fallback (kills start-up friction — [[Sustainable Daily Practice (Streak Design)]]).
- One phase at a time; don't parallelize. Log every experiment in the repo so the streak produces a visible artifact daily.

## Why the buck first (vs the other two candidates)
- **Bidirectional DC-DC:** same buck stage + a boost mode + direction control — natural *Phase 8 upgrade* once the buck works.
- **MPPT solar charger:** adds an MPP-tracking algorithm and a real source/load — best as the *second* project, reusing this power stage and firmware skeleton.
Build the buck, then graduate to one of these by reusing 80% of the work — the converter project compounds into a converter *platform*.

> [!gap] Component part numbers above are representative starting points, not a finalized BOM — confirm voltage/current/thermal ratings against your final spec before ordering.
