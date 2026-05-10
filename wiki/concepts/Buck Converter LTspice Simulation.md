---
type: concept
title: "Buck Converter LTspice Simulation"
created: 2026-05-05
updated: 2026-05-05
tags:
  - concept
  - domain/engineering
  - power-electronics
  - simulation
  - LTspice
status: complete
complexity: intermediate
domain: engineering
aliases: ["LTspice buck", "buck converter SPICE simulation"]
related:
  - "[[Buck Converter Theory and Design]]"
  - "[[LTSpice Complete Skills Guide]]"
  - "[[STM32 Digital Control for Buck Converter]]"
sources:
  - "[[Research - Buck Converter Build Guide]]"
---
# Buck Converter LTspice Simulation

Step-by-step LTspice simulation of the 12V→5V, 1A, 100 kHz buck converter. Simulate before building — catch design errors for free.

## 1. Why Simulate First

Simulation reveals:
- Whether component values are correct (does Vout actually hit 5V?)
- Inductor current ripple (is it in CCM? what's the peak current for saturation check?)
- Output voltage ripple (does it meet spec?)
- Gate drive waveforms (are MOSFETs switching cleanly?)
- Control loop stability (Bode plot — gain/phase margin)

## 2. Non-Synchronous Buck Schematic (Phase 1)

Build this first in LTspice. It's simpler and lets you verify the power stage before adding gate drivers.

### Component List

| Symbol | Value | Notes |
|--------|-------|-------|
| V1 | 12 V DC | Input voltage source |
| V_PWM | PULSE source | Gate drive signal |
| M1 | NMOS switch | High-side MOSFET model |
| D1 | Schottky diode | Catch diode |
| L1 | 100 µH | With series R = 110 mΩ (DCR) |
| C1 | 44 µF | Output cap (two 22µF in parallel) |
| R_ESR | 5 mΩ | ESR of output caps (place in series with C1) |
| R_load | 5 Ω | Load (1A at 5V) |
| R_feedback | 10 kΩ / 10 kΩ | Voltage divider (for AC analysis) |

### PULSE Source Settings for V_PWM

Right-click the PWM voltage source → Advanced → PULSE:
```
Initial value:  0
Pulsed value:   5 (for logic-level gate drive to MOSFET)
Delay time:     0
Rise time:      10n
Fall time:      10n
On time:        4.17u    ← D × T = 0.417 × 10µs
Period:         10u      ← 1/f_sw = 1/100kHz
```

### Schematic Topology (text description)

```
         M1 (NMOS)
V1+ ──── Drain
          Source ──┬──── L1 ──── Vout ──── R_load ──── GND
                   │              │
                  D1↓            C1 (+ R_ESR)
                   │              │
V1- ─────────────┴──────────────┴──── GND
```

### LTspice MOSFET Setup

Use the built-in NMOS model with these parameters (approximates an IRLZ44N):
- Right-click MOSFET → Pick New Transistor → Type "IRF" → select IRFZ44N

Or create a behavioral switch:
- Use the `.param` directive and a VOLTAGE-CONTROLLED SWITCH (symbol: SW)
- SW closes when V_PWM > 2.5V, opens when V_PWM < 2.5V

For V_PWM → M1 gate: connect V_PWM between gate and source of M1. The source of M1 is the switching node (not GND!) — this means V_PWM must float with the switching node. **Simplest workaround for initial sim**: use a behavioral switch (SW) instead of MOSFET.

### Behavioral Switch Alternative (Simpler)

```spice
.model SW SW(Ron=10m Roff=1Meg Vt=2.5 Vh=0.5)
```

Connect: switch control pin to V_PWM, switch between Vin and switching node.

## 3. Transient Simulation

Add this directive to the schematic (press 'S' for SPICE directive):
```spice
.tran 0 3m 2.9m 10n
```
- Simulates 3 ms total
- Plots only the last 0.1 ms (steady state after startup transient)
- Time step: 10 ns (sufficient for 100 kHz waveforms)

### What to Plot

After running, right-click the waveform window → Add Trace:

1. **V(Vout)** — Should settle to ~5V. Check: actual value, startup time (~0.5–1 ms)
2. **I(L1)** — Inductor current. Should show 1A average with ~0.3A triangle ripple (peak 1.15A)
3. **V(Vout) − 5** — After zooming in: AC-coupled ripple. Should be < 20 mV
4. **V(sw_node)** — Switching node voltage. Rectangular wave between 0V and 12V

### Expected Waveforms

```
V(Vout):  ___________/‾‾‾‾‾‾‾‾‾‾‾‾‾  → settles to 5.0V
I(L1):    /\/\/\/\/\/\/\/\/\/\/\/\/\/  → 1A average, 0.3A p-p ripple  
V(sw):    _¯¯¯_¯¯¯_¯¯¯_¯¯¯_¯¯¯_¯¯¯   → 41.7% duty cycle
```

### Key Measurements

Use LTspice's cursor (Ctrl+click on trace):
- **Average Vout**: place cursor, read DC average → should be ~5.00V
- **Ripple**: zoom to 2 cycles, cursor on peak and valley → ΔV
- **Inductor peak current**: read I(L1) peak → must be < inductor saturation rating

## 4. Synchronous Buck (Phase 2)

Replace the catch diode D1 with a second MOSFET (M2, low-side). Both MOSFETs need complementary gate signals with dead time.

### Dead Time Implementation in LTspice

Generate two PWM signals with a gap between them:

```spice
; High-side gate (same as before)
V_HI PULSE(0 5 0 10n 10n 4.17u 10u)

; Low-side gate: delayed by dead time, shorter by dead time on both sides
; Dead time = 100 ns (10% of 1µs = oversized for clarity)
V_LO PULSE(0 5 4.27u 10n 10n 5.63u 10u)
```

Verify in simulation: both gate voltages should NEVER be HIGH simultaneously (shoot-through). Look at V(HI_gate) and V(LO_gate) together — confirm the gap exists.

## 5. AC Analysis — Bode Plot of Open-Loop Plant

This tells you where to set the PI crossover frequency and how much phase margin you have.

### Method: Break the Feedback Loop

1. Add a voltage divider: R_top = 10kΩ from Vout to Vfb, R_bot = 10kΩ from Vfb to GND
2. Break the loop at Vfb — insert a 1 kΩ resistor in series at the break point
3. Add an AC voltage source V_ac = 1V (AC) at the break
4. Measure ratio: Vout / V_ac

### SPICE Directive for AC Analysis

```spice
.ac dec 100 10 100k
```
- Logarithmic sweep, 100 points/decade
- 10 Hz to 100 kHz

### Run and Read the Bode Plot

Plot:
- **20*log10(V(Vout)/V(Vac))** — gain in dB
- **Phase(V(Vout)/V(Vac))** — phase in degrees

Look for:
- **LC double pole at f_0 ≈ 2.4 kHz**: gain drops −40 dB/decade, phase drops rapidly toward −180°
- **ESR zero** (if using electrolytic with 50+ mΩ ESR): phase recovers slightly above 100 kHz
- **Gain crossover** (where gain = 0 dB): note the frequency and phase at that point
- **Phase margin** = phase at gain crossover + 180°: must be > 45° for stability

### Target for PI-Compensated System

After adding PI compensation (C(s) = Kp × (1 + 1/(τ_i × s))):
- Gain crossover at f_c = 1–5 kHz
- Phase margin ≥ 45°

## 6. Parametric Sweep — Find Optimal Inductor Value

Test multiple inductor values at once:

```spice
.param L_val list 47u 68u 100u 150u 220u
L1 sw_node Vout {L_val}
.tran 0 3m 2.9m 10n
.step param L_val list 47u 68u 100u 150u 220u
```

This runs 5 simulations. Plot I(L1) for all 5 — you'll visually see how ripple current changes with inductance.

## 7. Monte Carlo Analysis (Component Tolerances)

Check if the design still works with ±20% component tolerances:

```spice
.param L_nom=100u C_nom=44u
.param L_tol=0.2 C_tol=0.2
L1 sw_node Vout {L_nom*(1 + L_tol*(2*mc(1)-1))}
C1 Vout GND {C_nom*(1 + C_tol*(2*mc(1)-1))}
.mc 50 tran 0 3m 2.9m 10n
```

Run 50 Monte Carlo iterations. Examine the spread of Vout steady-state values — should stay within 5V ± 5%.

## 8. Common Simulation Mistakes

| Mistake | Symptom | Fix |
|---------|---------|-----|
| Forgetting inductor DCR | Efficiency looks too high | Add R_series to L1 |
| Missing MOSFET gate resistance | Gate voltage too square | Add 10Ω in series with V_PWM→Gate |
| Capacitor without ESR | Gain plot shows no ESR zero | Add R_ESR in series with C_out |
| Too-large timestep | Switching edges look distorted | Use .tran with max timestep ≤ 1/100 of switching period |
| Simulating steady state too early | Vout not settled | Simulate long enough (≥ 5× L/R ≈ 5 × 100µH / 5Ω = 100 µs) |
| Forgetting bootstrap for high-side | High-side MOSFET won't turn on | Use floating gate drive or bootstrap circuit |
