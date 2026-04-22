---
type: concept
title: "LTSpice Complete Skills Guide"
status: developing
created: 2026-04-22
updated: 2026-04-22
tags:
  - ltspice
  - circuit-simulation
  - spice
  - electrical-engineering
  - tools
  - power-electronics
---

# LTSpice Complete Skills Guide

LTSpice is a free, professional-grade circuit simulator from Analog Devices. It runs SPICE simulations — the universal circuit simulation language used in industry since 1973. Free, cross-platform (Windows/Mac), and required in EEE 202. Learning it before coursework hits turns a stressful tools-learning curve into a confirmatory experience.

**Download**: analog.com → Resources → LTSpice Simulator (latest: LTspice 24)

---

## Part 1 — Interface Overview

LTSpice has three main windows:

| Window | What it's for |
|--------|--------------|
| Schematic Editor | Draw circuits; place components; add SPICE directives |
| Waveform Viewer | View simulation results (voltage/current vs. time or frequency) |
| SPICE Netlist | Text representation of your circuit (auto-generated; rarely edit directly) |

The workflow is always: **Draw → Configure simulation → Run → Probe results**.

---

## Part 2 — Schematic Basics

### Placing Components

| Action | Method |
|--------|--------|
| Place component | `F2` or menu: Edit → Component |
| Draw wire | `F3` |
| Add ground | `G` |
| Label a net/node | `F4` — type a name (e.g., "Vout") |
| Add SPICE directive | `S` or Edit → SPICE Directive |
| Rotate component | `Ctrl+R` |
| Mirror component | `Ctrl+M` |
| Delete | `F5` |
| Move | `F7` |
| Drag (wires follow) | `F8` |
| Undo | `Ctrl+Z` |

### Key Components in the Library

| SPICE Name | What it is |
|-----------|-----------|
| `res` | Resistor |
| `cap` | Capacitor |
| `ind` | Inductor |
| `diode` | Generic diode |
| `nmos` | NMOS transistor |
| `pmos` | PMOS transistor |
| `npn` | NPN BJT |
| `pnp` | PNP BJT |
| `voltage` | Voltage source |
| `current` | Current source |
| `opamp2` | Generic op-amp (for importing models) |
| `SW` | Voltage-controlled switch (ideal) |
| `bv` | Behavioral voltage source (arbitrary expression) |

### The Golden Rules of Schematic Entry
1. **Every circuit needs a ground (`G`)** — at least one node must be GND.
2. **Every node must have a DC path to ground** — floating nodes cause "singular matrix" errors.
3. **Label your key nodes** with F4 — makes probing in the waveform viewer much cleaner.
4. **Right-click any component** to edit its value and attributes.

---

## Part 3 — The Four Core Simulation Types

### 3.1 DC Operating Point (`.op`)

**What it does**: Computes the steady-state DC voltages and currents. Capacitors = open circuit; inductors = short circuit.

**When to use it**: Always run first on a new circuit. Confirms bias voltages, quiescent current, and whether the circuit makes basic sense.

**SPICE directive**: `.op`

**How to add**: Press S → type `.op` → place on schematic.

**Read results**: Run → the SPICE error log opens and shows V(node) and I(device) for every node. Or hover over wires in the schematic — voltage appears.

---

### 3.2 Transient Analysis (`.tran`)

**What it does**: Simulates how voltages and currents change over time (time-domain). Most used analysis type.

**When to use it**: RC charging/discharging, RLC impulse response, amplifier step response, switching power supply waveforms, digital signals.

**SPICE directive**: `.tran [Tstop]` or `.tran [Tstart] [Tstop]`

**Examples**:
```
.tran 10m          ← run for 10ms
.tran 1u 5m        ← run from 0–5ms, ignore first 1µs of data
.tran 10n 100u     ← 10ns timestep max, run 100µs (switching converters)
```

**Pro tip**: Start with short Tstop (5–10× your circuit's time constant τ = RC or L/R). You can always run longer once it works.

**Reading results**: Click on any wire in the schematic after simulation → voltage vs. time appears. Alt+click on a component → current vs. time.

---

### 3.3 AC Analysis (`.ac`)

**What it does**: Frequency-domain analysis. Computes gain and phase vs. frequency — produces Bode plots. Linearizes the circuit around its DC operating point first.

**When to use it**: Filter design (find the -3dB frequency), amplifier bandwidth, phase margin, impedance vs. frequency.

**SPICE directive**: `.ac [dec/lin/oct] [N] [Fstart] [Fstop]`

**Examples**:
```
.ac dec 100 1 1Meg    ← 100 points per decade, 1Hz to 1MHz
.ac lin 1000 1k 100k  ← 1000 linear points, 1kHz to 100kHz
```

**Critical setup step**: Right-click your AC voltage source → set "AC Amplitude = 1" in the Small Signal AC Analysis field. Without this, AC analysis runs but the output is all zeros.

**Reading results**: After simulation, voltage probe on output node shows the Bode plot. Right-click waveform → "Add Trace" to overlay phase. Cursor tool (cross-hair icon) lets you read exact values at cutoff.

**Limitation**: AC analysis is linear — it cannot simulate switching transients, clipping, or any nonlinear behavior. For those, use transient.

---

### 3.4 DC Sweep (`.dc`)

**What it does**: Sweeps a DC source from start to stop in steps, running a full DC operating point at each step.

**When to use it**: Transistor I-V curves, op-amp transfer function, diode I-V, voltage regulator output vs. load.

**SPICE directive**: `.dc [source] [start] [stop] [step]`

**Examples**:
```
.dc V1 0 5 0.01        ← sweep V1 from 0V to 5V in 10mV steps
.dc Ib 0 1m 10u        ← sweep base current 0→1mA (BJT characteristics)
```

---

## Part 4 — Power Commands: SPICE Directives

These directives (added via 'S' key) are what separate basic users from power users.

### `.step` — Parametric Sweep (For-Loop)
Runs the entire simulation multiple times while varying a parameter. Equivalent to a for-loop.

```spice
.step param R1 100 1k 100      ← sweep R1: 100Ω → 1kΩ in 100Ω steps
.step param C list 1n 10n 100n ← sweep C through specific values
.step dec param freq 1k 1Meg 5 ← log sweep of a parameter
```

**Usage pattern**: Define a component value as `{R1}` in the schematic, then add `.param R1=1k` and `.step param R1 100 1k 100`. Now every R1 value shows as a separate trace.

---

### `.param` — Named Variable
```spice
.param fs=100k         ← switching frequency
.param D=0.5           ← duty cycle
.param L=10u           ← inductance
```
Use `{fs}` anywhere in the schematic to reference the parameter. Changing one line changes the whole circuit.

---

### `.ic` — Initial Conditions
```spice
.ic V(out)=0           ← start output at 0V
.ic V(C1_plus)=5       ← pre-charge capacitor to 5V
```
Essential for: integrators (prevents arbitrary startup), pre-charged capacitors, resonant circuits.

---

### `.meas` — Measure and Extract Numbers
```spice
.meas tran Vripple pp V(out)                    ← peak-to-peak output ripple
.meas tran rise_time trig V(out) val=0.1 rise=1 targ V(out) val=0.9 rise=1
.meas ac f3db when mag(V(out))=0.707            ← -3dB frequency
```
Results appear in the SPICE error log. This is how you get numbers out of simulations without reading graphs.

---

### `.noise` — Noise Analysis
```spice
.noise V(out) V1 dec 100 1 1Meg
```
Shows input-referred noise spectral density (nV/√Hz) vs. frequency. Use when designing low-noise amplifiers. Run with AC analysis.

---

## Part 5 — Voltage and Current Sources

### Standard Voltage Source Types

| Type | SPICE syntax (in source attributes) | Use |
|------|-------------------------------------|-----|
| DC | `DC 5` | Bias supply |
| SINE | `SINE(0 1 1k)` = 0V offset, 1V amplitude, 1kHz | AC signals |
| PULSE | `PULSE(0 5 0 10n 10n 5u 10u)` = 0→5V, 10ns edges, 5µs on, 10µs period | PWM/clock |
| PWL | `PWL(0 0 1m 5 2m 5 3m 0)` = piecewise linear points | Arbitrary waveform |

### PWM Source for Power Electronics
```
PULSE(0 {Vgate} 0 {tr} {tf} {D/fs} {1/fs})
```
Where `D` = duty cycle, `fs` = switching frequency, `tr/tf` = rise/fall time (set to 10ns for fast switching). This is how you drive a MOSFET gate in a buck converter simulation.

### Behavioral Voltage Source (`bv`)
```
V = V(A) * V(B)           ← multiplier
V = if(V(ctrl)>2.5, 15, 0) ← comparator behavior
V = table(V(x), 0,0, 1,5, 2,8) ← lookup table
```
Use `bv` for anything that can't be expressed as a standard source: multipliers, limiters, lookup tables, function generators.

---

## Part 6 — Importing Third-Party SPICE Models

LTSpice's built-in library covers only Analog Devices parts. For everything else, import the SPICE model from the manufacturer.

### Two Types of SPICE Models

| Type | Description | Examples |
|------|-------------|---------|
| `.MODEL` | One-line model for primitive SPICE devices | Diodes, BJTs, discrete MOSFETs |
| `.SUBCKT` | Multi-line subcircuit (complex IC modeled as internal circuitry) | Op-amps, gate drivers, regulators |

### Three Import Methods

**Method A — Embed in schematic (simplest, for one-off parts)**:
1. Get the `.MODEL` or `.SUBCKT` text from the manufacturer's website
2. Press `S` (SPICE directive)
3. Paste the entire model text directly onto the schematic
4. For `.SUBCKT` models, use the `opamp2` symbol and right-click → "Open Symbol" to edit its pin count if needed

**Method B — External .lib file reference (cleaner for long models)**:
1. Save the model file as `mypart.lib` in any folder
2. Add SPICE directive: `.lib "C:\path\to\mypart.lib"`
3. The simulator reads it at run time

**Method C — Install permanently in LTSpice library (use often)**:
1. Copy `.lib` file to `C:\Users\[you]\AppData\Local\LTspice\lib\sub\`
2. Copy `.asy` symbol file (if provided) to `...\lib\sym\`
3. Part appears in the component picker forever

### Where to Get SPICE Models
- **TI**: ti.com → product page → "Models" tab → download SPICE model
- **Infineon/Wolfspeed/Onsemi**: similar — product page → Documents → SPICE
- **DigiKey Model Library**: digikey.com → product → Documents section
- **SnapEDA / Ultra Librarian**: model aggregators
- **Analog Devices built-in**: 100s of Analog Devices parts already in LTSpice (no import needed)

**Joe's use case**: Download a Wolfspeed SiC MOSFET model (e.g., C3M0030090K) to simulate a real power electronics switching circuit instead of an idealized switch.

---

## Part 7 — The Waveform Viewer

### Basic Operations
- **Add voltage probe**: Click any wire in the schematic during/after simulation
- **Add current probe**: Alt+click a component (shows current through it)
- **Subtract traces**: Ctrl+click two waveform labels → shows difference (great for differential signals)
- **Zoom area**: Ctrl+drag in waveform window
- **Fit all**: Space or Ctrl+A
- **Cursor**: Click waveform title to get measurement cursor; Ctrl+click for second cursor (measures Δt, ΔV, frequency)

### Reading Bode Plots (AC Analysis)
- After `.ac` simulation: probe output node → shows magnitude (dB) by default
- Right-click waveform → "Add Trace" → add `Ph(V(Vout))` for phase
- Right-click left axis → toggle between Bode dB / linear / impedance view
- Use cursor to find exactly where gain = -3dB (0.707×) for bandwidth

### Measuring Power (Transient)
- Add current probe on voltage source (Alt+click on V1)
- Ctrl+click both V(V1) and I(V1) — plots both
- Right-click waveform label → "Attached to..." → integrate over one full period → gives average power = V×I

---

## Part 8 — Monte Carlo Analysis (Tolerance/Yield Simulation)

Monte Carlo randomly varies component values within their tolerance band and runs many iterations. Use it to understand yield, worst-case behavior, and design margin.

### Setup
1. Define a `.param` variable for each component value
2. Use `{mc(nominal, tolerance)}` syntax: `R = {mc(1k, 0.05)}` = 1kΩ with ±5% uniform random variation
3. Add `.step param run 1 100 1` — this runs 100 iterations
4. Run the simulation → 100 traces appear, showing the spread of behavior

### Interpretation
- The spread of traces = the circuit's behavioral sensitivity to component tolerance
- If all traces look the same → design is robust
- If traces spread widely → tighten component tolerances or redesign

---

## Part 9 — Power Electronics in LTSpice

### Buck Converter Simulation (Step by Step)

**Schematic elements**:
- V1 (input supply, e.g., 24V DC)
- M1 (NMOS switch) — use NMOS from library or import a real MOSFET model
- D1 (freewheeling diode) — use D from library; set Rser for realism
- L1 (inductor, e.g., 10µH) — right-click → set Rser = DCR (e.g., 50mΩ)
- C1 (output cap, e.g., 100µF) — right-click → set Rser = ESR (e.g., 20mΩ)
- Rload (output load)
- VPWM (PULSE source for gate drive)

**Gate drive PULSE source** (for 50% duty cycle at 100kHz):
```
PULSE(0 15 0 10n 10n 5u 10u)
```
= 0→15V gate, 10ns edges, 5µs on-time, 10µs period

**SPICE directives**:
```
.tran 0 1m 500u        ← run 1ms, skip first 500µs (startup transient)
.meas tran Vout_avg avg V(Vout)    ← average output voltage
.meas tran Iripple pp I(L1)        ← inductor current ripple
```

**Efficiency measurement**:
```
.meas tran Pout avg V(Vout)*I(Rload)
.meas tran Pin avg V(Vin)*(-I(V1))
.meas tran eta param Pout/Pin
```

### Key Power Electronics Parameters to Observe
- **Inductor current** I(L1): should show triangular ripple in steady state
- **Output voltage** V(Vout): flat DC with small ripple
- **Switch node** V(SW): should toggle between Vin and ~0V cleanly
- **Gate voltage** V(Gate): confirm PWM is correct amplitude and frequency
- **Output ripple**: use `.meas tran pp V(Vout)` — target <1% of Vout for good design

---

## Part 10 — Common Beginner Mistakes and Fixes

| Mistake | Symptom | Fix |
|---------|---------|-----|
| No DC path to ground | "Singular matrix" or "timestep too small" error | Add a large resistor (e.g., 1GΩ) from floating node to GND, or fix the schematic |
| AC source not set up | AC analysis runs but output is flat zero | Right-click voltage source → set AC Amplitude = 1 |
| Transient too long | Simulation takes forever | Estimate τ = RC or L/R; run 10×τ maximum to start |
| Op-amp supply missing | Output clips immediately to rail | Add V+ and V- supply voltage sources connected to op-amp power pins |
| Missing initial condition | Integrator output starts at random voltage | Add `.ic V(out)=0` directive |
| 741 model instability | Oscillations where there should be none | Replace LM741 with LT1001 or OP07 model for learning circuits |
| Convergence failure in switching sim | "Timestep too small" on buck converter | Add `.options reltol=0.003` and smaller max timestep: `.tran 0 1m 0 10n` |
| Forgetting to name nodes | Can't tell which trace is which | Use F4 to label every key node before running |

---

## Part 11 — Recommended Learning Path (Joe-Specific)

### Phase 1 — Foundations (Month 1, ~10 hours)

1. Install LTSpice (analog.com, free, 15 min)
2. Watch SparkFun or Afrotechmods "Getting Started" tutorial (1h)
3. Build voltage divider → run `.op` → verify KVL (30 min)
4. Build RC filter → run `.ac dec 100 1 1Meg` → find -3dB frequency (1h)
5. Build RLC circuit → run `.tran` → observe underdamped/overdamped switching (1h)
6. Build diode half-wave rectifier → observe clamping in transient (45 min)
7. Screenshot and save all 4 schematics to a "ltspice-projects" folder (→ future GitHub)

**Milestone**: You can open LTSpice, draw any basic R/L/C/D circuit, and run all four simulation types.

---

### Phase 2 — Op-Amps and Power Commands (Month 2, ~8 hours)

1. Build inverting op-amp → run `.ac` to find bandwidth (1h)
2. Build Sallen-Key low-pass filter → use `.step` to sweep R and see cutoff shift (1.5h)
3. Import a third-party op-amp model (e.g., TI LM358) using Method A (45 min)
4. Add `.meas` to automatically extract -3dB frequency without reading graph (45 min)
5. Explore `.param` + `{variable}` workflow: change one value, circuit updates everywhere (1h)
6. Build MOSFET switch → run `.dc` to plot I-V drain characteristics (1h)

**Milestone**: You can use `.step`, `.param`, `.meas`, and import any SPICE model from TI or Infineon.

---

### Phase 3 — Power Electronics (Month 3, ~8 hours)

1. Build a simple buck converter with SW (ideal switch) + diode + LC + Rload (2h)
2. Set up PWM gate drive using PULSE source (30 min)
3. Run transient, verify output voltage = Vin × D (30 min)
4. Add efficiency measurement via `.meas` (30 min)
5. Replace ideal SW with a real MOSFET model (import Wolfspeed or Infineon part) (1h)
6. Add output voltage feedback (error amp + comparator) for closed-loop operation (2h)
7. Use `.step` to sweep duty cycle → plot Vout vs. D (30 min)

**Milestone**: You can simulate a real switching power supply with measured efficiency. This puts you ahead of most juniors at internship time.

---

### Phase 4 — Advanced (Month 4+, ongoing)

- Monte Carlo on component tolerances → yield analysis
- Noise analysis (`.noise`) on op-amp circuits
- FRA/loop gain measurement (LTSpice 17+ feature)
- EMC simulation (parasitic inductance in power loops)
- Thermal modeling (power dissipation vs. junction temperature)

---

## Quick Reference Card

```
SIMULATION TYPES
.op                           ← DC bias point
.tran 10m                     ← transient, 10ms
.ac dec 100 1 1Meg            ← Bode plot, 1Hz–1MHz
.dc V1 0 12 0.1               ← DC sweep, 0–12V

POWER COMMANDS
.step param R1 100 1k 100     ← sweep R1 (for-loop)
.param fs=100k                ← define variable
.ic V(out)=0                  ← initial condition
.meas tran Vpp pp V(out)      ← measure peak-to-peak

PWM GATE SIGNAL
PULSE(0 15 0 10n 10n {D/fs} {1/fs})

IMPORT MODEL (METHOD B)
.lib "C:\models\mypart.lib"

MONTE CARLO
R = {mc(1k,0.05)}             ← 1kΩ ±5%
.step param run 1 100 1       ← 100 runs

KEY SHORTCUTS
F2=component F3=wire F4=label G=ground S=directive
F7=move F8=drag Ctrl+R=rotate Ctrl+Z=undo
```

---

## Related
- [[Research - LTSpice Skills Guide]] — research summary with 8 key findings
- [[EE Freshman Action Plans]] — Action Plan 2: LTSpice month-by-month
- [[EE Freshman Self-Study Stack]] — full freshman tool context
- [[EE Physical Side — Actionable Skill Plan]] — 18-month power electronics roadmap
- [[EV Fast Charging Topologies]] — circuits you will eventually simulate
- [[Silicon Carbide Power Electronics]] — real MOSFET models to import
