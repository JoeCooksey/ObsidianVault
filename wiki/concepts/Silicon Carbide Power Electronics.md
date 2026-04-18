---
type: concept
title: "Silicon Carbide Power Electronics"
created: 2026-04-18
updated: 2026-04-18
tags:
  - concept
  - domain/engineering
  - power-electronics
  - SiC
status: developing
complexity: advanced
domain: engineering
aliases: ["SiC", "SiC MOSFET", "silicon carbide"]
related:
  - "[[Wide Bandgap Semiconductors]]"
  - "[[800V EV Architecture]]"
  - "[[EV Fast Charging Topologies]]"
  - "[[WBG Thermal Management]]"
  - "[[Wolfspeed]]"
  - "[[Research - WBG Semiconductors in EV Fast Charging]]"
sources:
  - "[[IEEE Spectrum SiC vs GaN 2024]]"
  - "[[MDPI WBG Comparative Review 2024]]"
---
# Silicon Carbide Power Electronics

Silicon carbide (SiC) is the dominant [[Wide Bandgap Semiconductors|wide bandgap semiconductor]] in production EV systems today. It enables higher voltage, higher frequency, and more efficient power conversion than silicon IGBTs.

## Key Advantages Over Si IGBT

| Property | Si IGBT | SiC MOSFET |
|----------|---------|-----------|
| Max switching freq | 20–50 kHz | 100–300+ kHz |
| Slew rate | Baseline | ~2× faster |
| On-resistance | Higher | Lower |
| Max junction temp | ~175°C | 200°C+ |
| EV range improvement | baseline | ~5% |
| Conduction loss | Higher (bipolar) | Lower (unipolar) |

## EV Applications

### Traction Inverter (Primary use)
Tesla adopted SiC (STMicroelectronics supply) for the Model 3 motor inverter in 2017 — the pivotal inflection point for automotive SiC. All 800V platforms now use SiC inverters: Porsche Taycan, Hyundai Ioniq 5/6, Kia EV6/EV9, Audi Q6 e-tron.

### DC Fast Charging (DCFC) Infrastructure
SiC enables compact, high-efficiency 150–350+ kW fast chargers. Higher switching frequency shrinks transformer and filter size, reducing charger footprint.

### Onboard Charger (OBC)
SiC-based OBCs achieve >97% peak efficiency at switching frequencies of 67–250 kHz. 22kW bidirectional SiC OBC designs demonstrated at 140–250 kHz CLLC stage.

### DC-DC Converters
12V auxiliary power conversion inside the vehicle; bidirectional 400V↔800V boost converters on vehicles with mixed-voltage architectures.

## Why 800V Specifically Needs SiC

400V systems can still use optimized silicon IGBTs with acceptable losses. At 800V, the higher blocking voltage requirement makes silicon economically and thermally unviable — only SiC (and potentially 1200V GaN) can handle these voltages with acceptable efficiency.

## Voltage Classes

- **750V SiC**: 400V system applications
- **1200V SiC**: 800V system standard (dominant automotive class)
- **2300V SiC**: Grid-scale and ultra-high-power applications

## Key Manufacturers

See [[Wolfspeed]], [[STMicroelectronics SiC]], Infineon (CoolSiC), onsemi, ROHM Semiconductor.

## Reliability Challenges

Gate oxide degradation under high electric field stress is SiC's primary long-term reliability concern. Power cycling causes thermomechanical fatigue in packaging. Junction temperature monitoring via temperature-sensitive electrical parameters (TSEPs) is an active research area. See [[WBG Thermal Management]].
