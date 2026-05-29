---
type: source
source_type: documentation
title: "Digital Power Conversion with STM32G4 (sync buck) + related digital-power references"
author: "STMicroelectronics; Texas Instruments; eePower; Omicron Lab; Tektronix"
date_published: 2022
url: "https://www.st.com/content/dam/apec22/pdf/demo-apec22-digital-power-stm32g4.pdf"
confidence: high
created: 2026-05-29
updated: 2026-05-29
tags:
  - source
  - documentation
  - power-electronics
  - digital-control
related:
  - "[[Project - Digitally Controlled Synchronous Buck Converter]]"
---

# STM32G4 Digital Power Buck Reference

Bundled reference set for the [[Project - Digitally Controlled Synchronous Buck Converter]] build.

## Key claims / facts

- **STM32G4 platform:** implements a 3p3z compensator using the FMAC accelerator with HRTIM fine PWM control (**184 ps** resolution); ST **AN4539 (HRTIM cookbook)** includes single-phase synchronous-buck examples. (confidence: high — vendor docs)
- **TI C2000 platform:** `TIDM-DC-DC-BUCK` reference design; TMS320F2806x has a floating-point **CLA** coprocessor to run the control loop independent of the CPU; tested on F28069M LaunchPad + `BOOSTXL-BUCKCONV`; powerSUITE + **SFRA** for on-board loop measurement.
- **Digital compensator design = design-by-emulation:** design an analog Type-II/Type-III compensator in continuous time, then discretize (bilinear) to a difference equation.
- **Sampling:** when per-cycle sampling isn't possible, f_sample ≈ f_sw/3; synchronize ADC to DPWM to track steady-state average; DPWM adds phase lag that limits achievable bandwidth.
- **Loop-gain validation:** inject 10–100 mV across a 10–50 Ω resistor in the feedback path; network analyzer (Bode 100 / RidleyBox) sweeps and measures T(s)=V_A/V_B. SFRA achieves the same in firmware.
- **Double-Pulse Test:** standardized in IEC 60747-8/9; characterizes switching loss; AFG + scope + differential/current probes.

## Contribution to this topic

Supplies the platform decision, the control-design method, and the bench-validation methodology for the project roadmap.

> [!note] Vendor application notes and test-equipment app notes — high confidence as engineering references; not peer-reviewed research.
