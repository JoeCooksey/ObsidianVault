---
type: concept
title: "Buck Converter Theory and Design"
created: 2026-05-05
updated: 2026-05-05
tags:
  - concept
  - domain/engineering
  - power-electronics
  - embedded
  - hardware
status: complete
complexity: intermediate-advanced
domain: engineering
aliases: ["step-down converter", "synchronous buck", "buck converter design equations"]
related:
  - "[[STM32 Digital Control for Buck Converter]]"
  - "[[Buck Converter LTspice Simulation]]"
  - "[[Buck Converter PCB Design and Fabrication]]"
  - "[[Buck Converter Measurement and Characterization]]"
  - "[[EV Fast Charging Topologies]]"
  - "[[Silicon Carbide Power Electronics]]"
sources:
  - "[[Research - Buck Converter Build Guide]]"
---
# Buck Converter Theory and Design

A buck converter is a DC-DC step-down converter: it takes a higher input voltage and produces a lower, regulated output voltage with high efficiency (typically 85–95%). This page covers everything needed to design the 12V→5V, 1A, 100 kHz build from first principles.

## 1. How It Works — Intuition First

A buck converter works by rapidly switching the input voltage on and off, then averaging that switched waveform through an LC filter. When the switch (high-side MOSFET) is ON, energy flows from Vin into the inductor and load. When the switch is OFF, the inductor's stored energy freewheels through the return path (either a diode or a synchronous low-side MOSFET), continuing to supply the load. The LC filter averages the switched voltage into a steady DC output.

The key insight: the average output voltage equals the fraction of time the switch is ON (the duty cycle D) times the input voltage.

## 2. Fundamental Equations

### Volt-Second Balance (the foundation of all DC-DC analysis)

In steady state, the volt-second product across the inductor must be zero per switching cycle (otherwise the inductor current would drift to infinity).

**During ON-time** (switch closed):
- V_L = Vin − Vout = 12 − 5 = 7 V
- Duration: t_on = D / f_sw

**During OFF-time** (switch open, diode/low-side MOSFET conducts):
- V_L = −Vout = −5 V
- Duration: t_off = (1 − D) / f_sw

Setting volt-seconds to zero:
```
(Vin − Vout) × D = Vout × (1 − D)
```
Solving for duty cycle:
```
D = Vout / Vin = 5 / 12 ≈ 0.417 (41.7%)
```

This is the central equation of a buck converter. For our design:
- t_on = 0.417 × 10 µs = 4.17 µs
- t_off = 0.583 × 10 µs = 5.83 µs

### Inductor Ripple Current

The ripple current ΔiL riding on top of the DC output current determines inductor and capacitor sizing.

```
ΔiL = (Vin − Vout) × D / (L × f_sw)
```

Rearranging to size the inductor given a target ripple:
```
L = (Vin − Vout) × D / (f_sw × ΔiL)
```

**Design choice**: target ΔiL = 30% of I_out = 0.3 A (standard rule — balances transient response vs inductor size)

```
L = 7 × 0.417 / (100,000 × 0.3) = 2.917 / 30,000 ≈ 97 µH → use 100 µH
```

**Inductor peak current** (important for saturation rating):
```
i_L,peak = I_out + ΔiL/2 = 1.0 + 0.15 = 1.15 A
```
Select an inductor rated for at least 1.5 A saturation current (2× margin is ideal).

### Output Capacitor Sizing

The output ripple voltage has two contributors:

**1. Capacitive ripple** (charge stored during one half-cycle):
```
ΔV_C = ΔiL / (8 × f_sw × C_out)
```

**2. ESR ripple** (resistive drop from ripple current):
```
ΔV_ESR = ΔiL × ESR
```

Total: ΔV_out ≈ ΔV_C + ΔV_ESR (they can add in worst case)

Targeting ΔV_out = 50 mV (1% of Vout), for a 22 µF ceramic capacitor with ESR ≈ 5 mΩ:
```
ΔV_C = 0.3 / (8 × 100,000 × 22e-6) = 0.3 / 17.6 ≈ 17 mV
ΔV_ESR = 0.3 × 0.005 = 1.5 mV (negligible for ceramics)
Total ≈ 18.5 mV ✓ (well under 50 mV spec)
```

**Recommended**: 2× 22 µF ceramic (MLCC, X7R, 10V rating) in parallel = 44 µF total, giving ΔV_out ≈ 9 mV. This headroom helps with transient response.

### Input Capacitor Sizing

The high-side switch draws pulsed current from the input — this must be filtered by the input capacitor to prevent input voltage ripple from propagating to the source.

```
C_in ≥ I_out × D × (1 − D) / (f_sw × ΔV_in)
```

Targeting ΔV_in = 120 mV (1% of 12V):
```
C_in ≥ 1.0 × 0.417 × 0.583 / (100,000 × 0.12) = 0.243 / 12,000 ≈ 20 µF
```

**Recommended**: 47 µF electrolytic (bulk) + 100 nF ceramic (high-frequency bypass) close to the MOSFETs. The ceramic handles the fast switching transients; the electrolytic handles lower-frequency bulk energy.

### CCM vs DCM — Which Mode Are We In?

**Continuous Conduction Mode (CCM)**: inductor current never hits zero. This is the desired operating mode.
**Discontinuous Conduction Mode (DCM)**: current hits zero during the OFF-time at light loads.

The critical inductance that defines the CCM/DCM boundary at full load:
```
L_crit = (Vin − Vout) × D / (2 × f_sw × I_out) = 7 × 0.417 / (2 × 100,000 × 1) = 14.6 µH
```

Our 100 µH >> 14.6 µH: firmly in CCM at full load. At very light loads (< ~150 mA), the converter may enter DCM — the design equations change but the converter still regulates. For the FURI demo, operating at full load is the priority.

## 3. Topology Choice: Synchronous vs Non-Synchronous

| Feature | Non-Sync (diode) | Synchronous (2 MOSFETs) |
|---------|-------------------|--------------------------|
| Complexity | Simpler | Moderate (need dead time) |
| Efficiency | ~88–90% | ~92–96% |
| Diode loss | 0.7V × (1−D) × Iout ≈ 0.4W | ~0 (MOSFET Rds loss only) |
| Shoot-through risk | None | Yes (requires dead time) |
| Best for learning | Demo builds | FURI-level project |

**Recommendation for this build**: Start with non-synchronous (simpler debugging), then upgrade to synchronous for FURI presentation. The STM32 TIM1 complementary outputs handle dead time automatically once you move to synchronous.

## 4. Component Selection

### High-Side and Low-Side MOSFETs (Synchronous Build)

Key selection criteria:
- **Vds rating**: ≥ 1.5× Vin = 1.5 × 12 = 18V → use 30V-rated devices
- **Rds(on)**: as low as possible for efficiency (but lower Rds often means higher gate charge)
- **Qg (total gate charge)**: determines switching losses → lower is better at 100 kHz
- **Logic-level compatible**: either use gate driver with 10–12V drive, or select logic-level FETs

**Recommended MOSFETs**:

| Part | Vds | Rds(on) | Qg | Package | ~Cost |
|------|-----|---------|-----|---------|-------|
| IRF3205 | 55V | 8 mΩ | 150 nC | TO-220 | $1 |
| IRFZ44N | 60V | 17.5 mΩ | 140 nC | TO-220 | $0.80 |
| IRLZ44N | 60V | 22.5 mΩ | 63 nC | TO-220 | $0.80 |
| FDS8958A | 30V | 18 mΩ | 19 nC | SOIC-8 | $0.60 |

For a prototype: **IRLZ44N** (logic-level, TO-220, easy to handle) or **FDS8958A** (dual N-channel in one package, designed for sync buck).

### Catch Diode (Non-Synchronous Build)

Must be a **Schottky diode** — never use a standard rectifier diode (1N4007) because its slow recovery (trr ≈ 30 µs) would cause massive losses at 100 kHz.

**Recommended**: Schottky diode — **MBR340** (3A, 40V) or **SS34** (3A, 40V, SMD SMA package). Choose current rating 3× I_out = 3A minimum.

### Inductor

**Requirements**: 100 µH ± 20%, saturation current ≥ 1.5 A, DCR (winding resistance) < 200 mΩ for efficiency

**Recommended options**:
- **Bourns SRR1260-101Y**: 100 µH, 1.4A sat, 250 mΩ DCR, $1.50 (through-hole friendly)
- **Vishay IHLP-2525CZ**: 100 µH, 2.0A sat, 110 mΩ DCR, SMD (higher performance)
- **Core type**: shielded drum core or toroidal for lower EMI; avoid open-bobbin types

### Output Capacitors

**2× 22 µF MLCC X7R ceramic, 10V rating** — X7R maintains capacitance over temperature. Avoid Y5V — it loses 80% capacitance at DC bias + temperature.

MLCC advantage: ESR < 5 mΩ (vs 100+ mΩ for electrolytic). This eliminates the ESR ripple term entirely and allows stable control loop design.

Add 1× 100 µF electrolytic in parallel for bulk charge during transients.

## 5. Efficiency Budget

At Vout = 5V, Iout = 1A, Pin = Vout × Iout / η:

| Loss Source | Calculation | Value |
|-------------|-------------|-------|
| High-side MOSFET conduction | I²_rms × Rds = (D×Iout)² × Rds = (0.417×1)² × 0.022 | 3.8 mW |
| Low-side MOSFET conduction (sync) | (1−D)×Iout² × Rds = (0.583×1)² × 0.022 | 7.5 mW |
| Inductor DCR | Iout² × DCR = 1² × 0.11 | 110 mW |
| Switching losses (both FETs) | ≈ 0.5 × Vin × Iout × (tr+tf) × fsw ≈ 0.5×12×1×20ns×100kHz | 12 mW |
| Gate drive | Qg × Vgate × fsw × 2 = 63nC × 12 × 100kHz × 2 | 151 mW |
| **Total losses** | | **~285 mW** |
| **Efficiency** | Pout/(Pout+Ploss) = 5/5.285 | **~94.6%** |

Actual measured efficiency will be lower (additional PCB trace resistance, bootstrap diode loss, etc.) but 90–93% is achievable with care.

## 6. Control Loop Basics

The buck converter plant (without compensation) has a transfer function with a double pole at the LC resonant frequency:
```
ω_0 = 1/√(L × C) = 1/√(100µH × 44µF) = 1/√(4.4×10⁻⁹) ≈ 15,075 rad/s → f_0 ≈ 2.4 kHz
```

At f_0, the LC filter causes a −40 dB/decade rolloff and −180° phase shift. Without compensation, the closed-loop system will be unstable if the loop gain is >0 dB at the phase crossover.

**PI compensation strategy**:
- Place the integrator zero (1/τ_i) below the LC resonance to add phase
- Target crossover frequency: f_c = 1 kHz (well below f_sw/10 = 10 kHz)
- Kp chosen so |G(jω_c) × C(jω_c)| = 0 dB
- Result: typical Kp ≈ 0.1–0.5, Ki ≈ 500–2000 (digital implementation)

See [[STM32 Digital Control for Buck Converter]] for the complete digital PI implementation.
