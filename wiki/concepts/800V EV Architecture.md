---
type: concept
title: "800V EV Architecture"
created: 2026-04-18
updated: 2026-04-18
tags:
  - concept
  - domain/engineering
  - electric-vehicles
  - power-electronics
status: developing
complexity: intermediate
domain: engineering
aliases: ["800V platform", "high voltage EV", "E-GMP", "800 volt electric vehicle"]
related:
  - "[[Silicon Carbide Power Electronics]]"
  - "[[Wide Bandgap Semiconductors]]"
  - "[[EV Fast Charging Topologies]]"
  - "[[Research - WBG Semiconductors in EV Fast Charging]]"
sources:
  - "[[IEEE Spectrum SiC vs GaN 2024]]"
---
# 800V EV Architecture

800V EV architectures use an 800V nominal battery pack (vs the conventional 400V standard). They require SiC semiconductors throughout the power chain and enable faster charging with lower current at equivalent power levels.

## Why 800V?

**Power = Voltage × Current.** At the same charging power:
- 400V system at 150kW → 375A of cable current
- 800V system at 350kW → 438A, but thinner cables viable due to reduced proportional heating at higher voltage

Higher voltage reduces I²R heating losses in cables, enables higher power delivery without proportionally thicker/heavier wiring, and allows compact high-power charging stations.

## Charging Speed

| Platform | Architecture | Max Charging Rate | 10→80% Time |
|---------|-------------|-------------------|-------------|
| Porsche Taycan Turbo S | 800V | 270 kW | 22.5 min |
| Hyundai Ioniq 6 | 800V (E-GMP) | 200 kW | 18 min |
| Hyundai Ioniq 5 | 800V (E-GMP) | 200 kW | ~18 min |
| Standard 400V EV | 400V | 50–150 kW | 30–45 min |

## SiC Requirement

800V battery packs require 1200V-rated switching transistors to safely handle transient overvoltages. Silicon IGBTs at 1200V carry unacceptable conduction and switching losses. **SiC MOSFETs at 1200V are mandatory for 800V EVs.** All 800V traction inverters use SiC.

## Platforms and Vehicles

- **Porsche PPE / Taycan**: First mass-produced 800V EV (launched 2019); Macan Electric, Audi A6/Q6 e-tron use same platform
- **Hyundai E-GMP**: Ioniq 5, Ioniq 6, Ioniq 9, Kia EV6, EV9
- **Tesla**: Uses 400V architecture but transitioning to 800V on future platforms

## Market Trajectory

By 2028, >70% of new EVs projected to use 800V+ architecture. 800V EV architecture market: $3.45B in 2024 → $24.4B by 2034 (CAGR 21.3%).

## Charging Infrastructure Requirement

800V EVs require 800V-compatible chargers. Older 400V fast chargers require a DC-DC boost stage within the vehicle or charger. New 350kW+ ultra-fast chargers (e.g., Ionity, Electrify America) are 800V-native. See [[EV Fast Charging Topologies]].
