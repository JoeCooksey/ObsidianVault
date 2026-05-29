---
type: concept
title: "Heterogeneous Integration (Power Electronics)"
created: 2026-05-29
updated: 2026-05-29
tags:
  - concept
  - domain/engineering
  - power-electronics
  - packaging
  - heterogeneous-integration
status: developing
complexity: advanced
domain: engineering
aliases: ["HI power electronics", "heterogeneous integration", "Si/SiC/GaN co-packaging", "More than Moore power"]
related:
  - "[[Wide Bandgap Semiconductors]]"
  - "[[Silicon Carbide Power Electronics]]"
  - "[[Gallium Nitride Power Electronics]]"
  - "[[Multi-Chip Power Module Packaging]]"
  - "[[Common-Source Inductance]]"
  - "[[Power Module Ceramic Substrates]]"
  - "[[Silver Sintering Die-Attach]]"
  - "[[Gate Driver Timing Coordination]]"
  - "[[WBG Thermal Management]]"
  - "[[Moore's Law and Dennard Scaling]]"
  - "[[Moore4Power]]"
sources:
  - "[[Moore4Power Launch — Semiconductor Today]]"
  - "[[Parasitic Inductance and Switching — Power Electronic Tips]]"
---

# Heterogeneous Integration (Power Electronics)

## Definition

Heterogeneous integration (HI) in power electronics is the packaging of transistors built from **different semiconductor materials into a single module**, using the optimal material for each function rather than forcing one material across the whole design (Source: [[Moore4Power Launch — Semiconductor Today]]):

| Material | Best at | Typical role |
|---|---|---|
| **Si** | cheap, mature low-voltage logic | gate drivers, sensing, control |
| **SiC** | high voltage (1200 V+), high temp (175–200 °C) | main power switches |
| **GaN** | high frequency (1 MHz+), low switching loss | fast-switching legs, point-of-load |

This is the **"More than Moore"** thesis: with classical [[Moore's Law and Dennard Scaling|Dennard scaling]] broken, system-level gains now come from co-packaging and integration rather than node shrink. No single material wins at all operating points — so integrate them.

## Why now

The **[[Moore4Power]]** EU flagship project (launched May 2026, €91M, 62 partners, led by [[Infineon Technologies]]) is a concrete bet that HI is the path forward. It explicitly combines Si, SiC, and GaN "together with sensing, control and communication functions to form tightly integrated systems" (Source: [[Moore4Power Launch — Semiconductor Today]]).

## The five engineering tensions

HI does not come free. Putting dissimilar materials in one package surfaces interface problems that monolithic modules avoid. Each has a dedicated atomic note:

1. **CTE mismatch & die-attach** → [[Silver Sintering Die-Attach]]. SiC ~4.0 ppm/°C vs Si ~2.6 ppm/°C; mismatched expansion fatigues the bond under thermal cycling. Sintered Ag (sinter at 250–300 °C, remelt >900 °C) replaced Pb solder in automotive SiC.
2. **Parasitic inductance** → [[Common-Source Inductance]]. Bond-wire + substrate routing between the Si driver and SiC/GaN switch adds common-source inductance (L_CS) that feeds di/dt back onto the gate, slowing transitions. Target L_CS < 1 nH.
3. **Gate-drive timing** → [[Gate Driver Timing Coordination]]. GaN (t_r/t_f ~1–5 ns) and SiC (~20–50 ns) need matched propagation delays; a 10 ns skew in a mixed half-bridge risks shoot-through.
4. **Thermal management** → [[WBG Thermal Management]]. SiC tolerates ~200 °C junction; GaN-on-Si is capped ~150–175 °C by buffer-trap leakage. A co-packaged module's cooling must serve the hottest device while protecting the most sensitive.
5. **Substrate choice** → [[Power Module Ceramic Substrates]]. AlN DBC (~170 W/m·K) spreads heat; Si₃N₄ AMB (CTE ~3.2 ppm/°C, fracture-tough) wins thermal-cycling reliability for automotive.

> [!tip] The unifying principle
> HI's payoff (each material at its sweet spot) is bought by **interface engineering** — die-attach, parasitics, timing, thermal, substrate. The hard part of HI is not the dice; it is everything between them.

## Co-design, not co-location

Industry consensus: an integrated **co-design spanning devices, packaging, EMI-aware layout, and cooling** is the only viable strategy for reliable high-density WBG systems. New failure modes — especially **thermal crosstalk** between co-packaged dice — must be designed out, not patched (Source: web search synthesis, IEEE HIR 2023 power chapter; confidence: high).

## See also

- [[Multi-Chip Power Module Packaging]] — the packaging umbrella (wire-bond vs wire-bondless, embedded die, double-sided cooling)
- [[Research - Heterogeneous Integration in Power Electronics]] — full synthesis of this research session
