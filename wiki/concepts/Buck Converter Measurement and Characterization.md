---
type: concept
title: "Buck Converter Measurement and Characterization"
created: 2026-05-05
updated: 2026-05-05
tags:
  - concept
  - domain/engineering
  - power-electronics
  - measurement
  - oscilloscope
status: complete
complexity: intermediate-advanced
domain: engineering
aliases: ["buck converter testing", "power converter measurement", "Bode plot measurement"]
related:
  - "[[Buck Converter Theory and Design]]"
  - "[[STM32 Digital Control for Buck Converter]]"
  - "[[Buck Converter PCB Design and Fabrication]]"
  - "[[Transfer Functions and Poles Zeros]]"
sources:
  - "[[Research - Buck Converter Build Guide]]"
---
# Buck Converter Measurement and Characterization

Complete oscilloscope measurement guide, efficiency testing, and Bode plot procedure for the 12V→5V, 1A, 100 kHz buck converter.

## 1. Equipment List

| Tool | Purpose | Source |
|------|---------|--------|
| Oscilloscope (4-channel) | Waveform capture | ASU EE lab (borrow) |
| 2× 10:1 probes | Voltage measurement | With scope |
| Current probe or shunt resistor | Inductor current waveform | Lab or DIY |
| DMM (×2) | DC voltage and current | Any DMM |
| Variable bench supply (0–15V, 2A) | Controlled input | Lab |
| Load resistors (5Ω, 10Ω, 5W) | Programmable load | Amazon |
| Variac or load switch | Transient load testing | DIY switch |

**ASU EE lab**: Keysight DSOX1204G (200 MHz, 4-channel) is available. Book a lab slot.

## 2. Measurement Safety Protocol

Before every measurement session:
1. **Current limit** bench supply to 500 mA until full test sequence is complete
2. **Oscilloscope ground clip** goes to power ground — never leave it floating
3. **Avoid floating measurements** (both channels referenced to different grounds → can cause oscilloscope ground loop and damage)
4. **High-voltage caution**: the SW node (between MOSFETs) swings between 0V and 12V at 100 kHz. Use a 10:1 probe, not a 1:1 probe (reduces capacitive loading and keeps measurement within safe limits)
5. **Hand rule**: one hand only when probing live circuits — keeps fingers away from contact with both polarities simultaneously

## 3. Measurement 1: Output Voltage (DC)

**Goal**: Confirm Vout = 5.00V ± 50 mV

**Procedure**:
1. Connect DMM across output terminals (Vout and GND)
2. Apply nominal load: R = 5Ω (1A load)
3. Apply Vin = 12.0V
4. Read Vout → target: 5.00V ± 0.05V

If Vout is off by > 5%:
- Check ADC reference voltage (measure STM32 3.3V with DMM)
- Verify feedback divider resistors (should be 1% tolerance, not 5%)
- Check V_REF_ADC constant in firmware calculation

## 4. Measurement 2: Output Voltage Ripple

**Goal**: Measure peak-to-peak ripple at 100 kHz; target < 50 mV

**Oscilloscope Setup**:
- Channel 1: probe at Vout with respect to local power GND (keep probe cable short, < 5 cm)
- **AC coupling** mode (press "coupling" → AC)
- Time/div: 2 µs/div (shows 5 switching cycles)
- Voltage/div: 20 mV/div
- Trigger: CH1, rising edge, level at 0V (AC-coupled)

**What you should see**:
```
    ~17 mV p-p
    ___________
   /           \___/‾‾‾\___/‾‾‾\___
↑ (100 kHz sawtooth ripple)
```

**Measurement procedure**:
1. Run → stabilize → Single acquisition
2. Use "Measure → Vpp" function
3. Report: ripple voltage in mV and as % of Vout

**Troubleshooting large ripple (> 100 mV)**:
- Ground loop: move scope ground clip to directly beside the probing point
- Probe ground loop: use a "probe ground spring" (short ground adapter)
- ESR too high: check electrolytic cap type; replace with MLCC
- Oscillation: control loop instability — reduce Kp

## 5. Measurement 3: Switching Waveforms

**Goal**: Confirm proper switching, dead time, and no shoot-through

### Waveform A: Switching Node Voltage (V_sw)

- Channel 2: probe at SW node (MOSFET junction) vs GND
- **DC coupling**
- Time/div: 2 µs/div
- Voltage/div: 5V/div

Expected waveform: rectangular pulse between 0V and 12V at 41.7% duty cycle. The "high" portion should last 4.17 µs, "low" portion 5.83 µs.

**Observe**: any ringing at the switching transitions. A 50–200 mV overshoot spike at turn-off is normal (from parasitic inductance of PCB traces). Spikes > 5V (clamped at Zener level) indicate layout problems.

### Waveform B: Gate-Source Voltages (Vgs1 and Vgs2)

For synchronous buck, verify dead time with a 2-channel measurement:
- Channel 1: M1 gate (probe across gate-source of high-side MOSFET)
  - Note: M1 source is the SW node (not GND!) — use differential measurement or note the reference
  - Simplification: for gate drive IC output HO and LO, measure both with respect to common GND from gate driver side
- Channel 2: M2 gate (probe across gate-source of low-side MOSFET, referenced to power GND)

**Key verification**: The two gate signals should NEVER be simultaneously high. The dead time gap should be visible as ~100 ns where both are at 0V. If there's no gap → immediate shut down (shoot-through will destroy both MOSFETs in microseconds).

### Waveform C: Inductor Current

**Without a current probe** (use a shunt resistor):
- Place a 0.1Ω, 1W precision resistor in series with the inductor (between L1 and Vout)
- Measure voltage across the shunt: V_shunt = I_L × 0.1Ω
- At 1A: V_shunt = 100 mV (needs 20 mV/div scale, sensitive measurement)
- I_L = V_shunt / 0.1

**With a Rogowski current probe** (lab equipment):
- Clamp around the inductor lead
- Calibrate per probe instructions
- Read directly in Amps

Expected: triangle wave at 100 kHz, average = 1A, peak-to-peak ≈ 0.3A (150 mA to 1.15A).

## 6. Measurement 4: Efficiency

**Goal**: Measure total conversion efficiency η = P_out / P_in

**Setup**:
```
V_source (12V) ──── A_in (DMM in current mode) ──── DUT ──── R_load ──── GND
                                                      │
                                                    V_out (DMM)
```

**Procedure**:

| Measurement | Instrument | Reading |
|------------|-----------|---------|
| V_in | DMM on bench supply | 12.00V |
| I_in | DMM in series at input | ~0.46A |
| V_out | DMM on output terminals | 5.00V |
| I_out | Calculate: V_out / R_load | 5V/5Ω = 1.00A |

```
P_in  = 12.0V × 0.46A = 5.52W
P_out = 5.0V × 1.0A = 5.0W
η = P_out / P_in = 5.0 / 5.52 = 90.6%
```

**Measure at multiple load points for an efficiency curve** (important for FURI report):

| I_out (A) | R_load (Ω) | Expected η (%) |
|-----------|-----------|---------------|
| 0.2 | 25 | ~80% (DCM, lower eff) |
| 0.5 | 10 | ~88% |
| 1.0 | 5 | ~91–93% |
| 1.2 | 4.2 | ~90% (near limit) |

Plot efficiency vs load current — this is a standard figure in every power electronics paper and FURI poster.

## 7. Measurement 5: Load Transient Response

**Goal**: Quantify how well the control loop rejects a sudden load step

**Setup**:
- Connect R_main = 10Ω (0.5A steady-state load) permanently
- Connect R_step = 10Ω in parallel via a switch (MOSFET switch or manual relay)
- Applying R_step steps load from 0.5A to 1.0A suddenly

**Oscilloscope setup**:
- Channel 1: Vout (DC coupled, 100 mV/div)
- Channel 2: Switch signal (shows when step occurs)
- Time/div: 0.5 ms/div
- Trigger: channel 2 edge

**Measure from the waveform**:
1. **Voltage undershoot/overshoot**: how far Vout deviates from 5V during the transient
2. **Settling time**: how long until Vout returns to within ±1% of 5V
3. **Ringing**: any oscillation after settling (indicates marginal phase margin)

**Target performance** for a well-tuned PI controller:
- Undershoot < 200 mV (4% of Vout)
- Settling time < 1 ms
- No sustained ringing

## 8. Measurement 6: Bode Plot (Control Loop)

**Goal**: Measure gain and phase margin of the closed-loop control system to prove stability

This is the most impressive measurement for a FURI application — it demonstrates genuine power electronics expertise.

### Method: Swept-Sine Injection

**Concept**: inject a small sinusoidal perturbation into the feedback path. Measure how the output responds vs the injection frequency. This is the "loop gain" Bode plot.

**Hardware injection circuit**:
```
Vout ──── R_inject (100Ω) ──── R_fb1 (10kΩ) ──── V_sense
                │
           V_inject (function generator, 50mV sine, 50Ω output)
```

The 100Ω inject resistor and function generator's 50Ω output form a voltage divider that injects a small (~25 mV) perturbation at each frequency point.

**Oscilloscope setup**:
- Channel 1: V_inject (at function generator output)
- Channel 2: Vout (the system response)
- Use scope's built-in math: CH2/CH1 ratio as a function of frequency

**Frequency sweep procedure** (manual — no network analyzer needed):
1. Set function generator to 100 Hz, 50 mVpp sine
2. Note CH1 amplitude (V_inject) and CH2 amplitude (V_response)
3. Note phase difference between CH1 and CH2 (scope cursor measurement)
4. Calculate: Gain = 20×log10(V_response/V_inject) [dB], Phase = measured phase shift
5. Repeat at: 200Hz, 500Hz, 1kHz, 2kHz, 5kHz, 10kHz, 20kHz
6. Plot gain and phase vs frequency

**Key values to report**:
- **Gain crossover frequency** (f_c): where gain = 0 dB
- **Phase margin**: 180° + phase at f_c → should be > 45°
- **Bandwidth**: typically f_c is a good approximation

**Alternative**: use Python with STM32 serial output to log Vout while chirping the duty cycle setpoint. Then compute FFT of Vout/duty_cycle to get the closed-loop frequency response.

## 9. Technical Report Structure (Weeks 10–12)

Required deliverables for FURI portfolio and GitHub README.

### Report Outline (3–5 pages)

1. **Abstract** (1 paragraph): what you built, key specs, results
2. **Introduction**: motivation, application (EV/solar/embedded), scope
3. **Design and Analysis**:
   - Topology selection (synchronous vs non-synchronous, justification)
   - Design equations with your numbers substituted in
   - Component selection rationale (MOSFET Rds, inductor DCR, cap ESR)
   - Control loop design (PI, crossover frequency choice)
4. **Simulation Results**:
   - LTspice waveforms: Vout, I_L, V_sw
   - Bode plot from LTspice AC analysis showing phase margin
5. **Experimental Results**:
   - Photograph of completed board
   - Table: specified vs measured Vout, ripple, efficiency at 3 load points
   - Oscilloscope screenshots: ripple, switching waveform, gate signals, transient response
   - Bode plot (measured or simulated)
6. **Lessons Learned**: what went wrong, what surprised you, what you'd do differently
7. **References**: IR2110 datasheet, STM32 reference manual, Erickson & Maksimović (power electronics textbook)

### GitHub Repository Structure

```
buck-converter-stm32/
├── README.md              ← with photos, results table, scope screenshots
├── hardware/
│   ├── schematics/        ← KiCad project files
│   ├── pcb/               ← KiCad PCB files
│   ├── gerbers/           ← ready-to-order Gerber zip
│   └── bom.csv            ← Bill of materials
├── firmware/
│   ├── Core/              ← STM32CubeIDE generated code
│   └── Core/Src/main.c   ← PI control loop in here
├── simulation/
│   ├── buck_converter.asc ← LTspice schematic
│   └── results/           ← screenshots from LTspice
└── report/
    └── buck_converter_report.pdf
```

A polished GitHub repo with scope screenshots, efficiency curve, and Bode plot is the FURI differentiator. No other applicant will have this.
