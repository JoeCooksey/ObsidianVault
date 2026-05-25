---
type: question
title: "Research - Buck Converter Build Guide"
created: 2026-05-05
updated: 2026-05-05
tags:
  - research
  - domain/engineering
  - power-electronics
  - hardware
  - FURI
  - STM32
status: complete
domain: engineering
related:
  - "[[Buck Converter Theory and Design]]"
  - "[[Buck Converter LTspice Simulation]]"
  - "[[STM32 Digital Control for Buck Converter]]"
  - "[[Buck Converter PCB Design and Fabrication]]"
  - "[[Buck Converter Measurement and Characterization]]"
  - "[[90 Day Project Tier List]]"
  - "[[FURI Program Complete Guide]]"
---
# Research — Buck Converter Build Guide

**Question**: How do I build a 12V→5V, 1A, 100 kHz synchronous buck converter with STM32 digital control over a 90-day period?

## 8 Key Findings

**1. Duty cycle is derived entirely from volt-second balance — D = Vout/Vin = 41.7%.**
All other design equations flow from this. The inductor sizing (L = (Vin−Vout)×D / (fsw×ΔiL)) gives 97 µH → use 100 µH standard value. The output capacitor (C = ΔiL / (8×fsw×ΔVout)) gives 7.5 µF → use 44 µF (two 22 µF MLCC in parallel) for headroom. The design is fully determined before touching a component.

**2. STM32 TIM1 complementary outputs + hardware dead-time is the correct architecture.**
TIM1 and TIM8 are Advanced-Control Timers with dedicated complementary PWM channels (TIMx_CH1 and TIMx_CH1N) and a hardware Dead-Time Generator in the BDTR register. This handles dead-time insertion in hardware at zero software overhead — the right tool for the job. At 168 MHz clock, 100 kHz PWM requires ARR = 839 (center-aligned) giving 1680 duty-cycle steps = 0.06% resolution. ADC triggered at the PWM carrier peak samples the minimum-ripple point, eliminating switching noise contamination.

**3. The IR2110 bootstrap gate driver is the correct choice for a synchronous half-bridge.**
It accepts 3.3V logic inputs (VDD = 3.3V), drives both high-side and low-side MOSFETs from a single 12V supply via a bootstrap circuit, and has no issues at 100 kHz. The bootstrap capacitor must be ≥ Qg/ΔV = 63 nC / 1V = 63 nF → use 220 nF. The bootstrap diode must be ultrafast (UF4007 — NOT 1N4007, which will fail in nanoseconds at 100 kHz).

**4. PCB layout quality determines whether the design works or oscillates — power loop minimization is the single most important rule.**
The loop area of: input capacitor → high-side MOSFET → switching node → low-side MOSFET → back to input cap must be minimized to sub-centimeter scale. Every cm² of this loop adds parasitic inductance that creates voltage spikes at switching transitions. Place the input capacitor, both MOSFETs, and the bootstrap capacitor within a 15×15mm square. A large ground plane on the bottom layer is essential.

**5. LTspice simulation before hardware is mandatory, not optional.**
The transient simulation reveals whether you're actually in CCM (you are — L_crit = 14.6 µH vs L = 100 µH), what the actual ripple is, and whether the LC resonant frequency (~2.4 kHz) places the phase margin in a safe region. The AC analysis Bode plot tells you where to set the PI crossover frequency. Building without simulating first is how students destroy MOSFETs and waste weeks debugging.

**6. Start non-synchronous (diode), then upgrade to synchronous (two MOSFETs).**
The non-synchronous topology (one MOSFET + Schottky catch diode) is simpler, eliminates shoot-through risk, and can be debugged faster. Efficiency loss is ~4% (diode drop × (1−D) × Iout). Once the non-synchronous build works, upgrading to synchronous replaces the diode with M2 and adds the complementary PWM — all the hardware and firmware infrastructure is already in place.

**7. Efficiency curve + transient response + Bode plot = the three measurements that prove you understand power electronics.**
A DMM reading "5V out" proves nothing to a FURI reviewer. An efficiency curve from 20% to 120% load proves you understand conduction and switching losses. A load transient response shows closed-loop bandwidth. A Bode plot with 45°+ phase margin proves you understand stability. Together these are the technical content of a 3-page engineering report that no other freshman applicant will have.

**8. The project is achievable in 90 days with a phased approach and costs under $55.**
Week 1–3: STM32 exercises (GPIO→PWM→ADC→UART→interrupt) build the firmware skills. Week 4–6: LTspice design and simulation validates the schematic before spending money. Week 7–9: breadboard prototype → KiCad PCB → JLCPCB fabrication ($20 for 5 boards). Week 10–12: characterization measurements + technical report + GitHub repo. Total BOM cost: ~$45–55 including Nucleo board ($15), IR2110 ($2.50), MOSFETs ($2), inductor ($1.50), passives ($5), PCB ($20 shipped).

## Open Questions

1. Should the feedback compensator be PI or PID? (PID adds a derivative term that can improve transient response but introduces noise — likely unnecessary for a 1 kHz crossover frequency)
2. Can the STM32 HRTIM peripheral (on STM32F334 Nucleo) provide better resolution than TIM1 for tighter regulation? (Yes — HRTIM has 217 ps resolution vs ~6 ns for TIM1 — but overkill for this project)
3. What is the optimal gate resistance value for balancing switching speed vs EMI? (10Ω is a safe starting point; reduce to 5Ω if efficiency matters more; increase to 22Ω if EMI is problematic)
4. How to measure the Bode plot without a $5,000 network analyzer? (Swept-sine injection with function generator + oscilloscope, or Python-based swept chirp injection via STM32 UART)
5. What happens to efficiency and stability when Vin drops from 12V to 9V (discharged battery)? (Duty cycle increases to 0.556, ripple current slightly changes — worth simulating and measuring across Vin range for a thorough report)

## Pages Created

- [[Buck Converter Theory and Design]] — complete design equations, component sizing, efficiency budget, control loop basics
- [[Buck Converter LTspice Simulation]] — step-by-step sim guide: transient, AC analysis, parametric sweep, Monte Carlo
- [[STM32 Digital Control for Buck Converter]] — TIM1 PWM setup, IR2110 wiring, PI control C code, tuning procedure, beginner exercises
- [[Buck Converter PCB Design and Fabrication]] — KiCad schematic sections, layout priority rules, JLCPCB order procedure, component BOM
- [[Buck Converter Measurement and Characterization]] — oscilloscope protocols for all 6 measurements, efficiency method, Bode plot procedure, technical report outline
