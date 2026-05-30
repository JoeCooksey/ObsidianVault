---
type: synthesis
title: "Research - Heterogeneous Integration in Power Electronics"
created: 2026-05-29
updated: 2026-05-29
tags:
  - research
  - power-electronics
  - heterogeneous-integration
  - packaging
status: developing
related:
  - "[[Heterogeneous Integration (Power Electronics)]]"
  - "[[Multi-Chip Power Module Packaging]]"
  - "[[Common-Source Inductance]]"
  - "[[Silver Sintering Die-Attach]]"
  - "[[Power Module Ceramic Substrates]]"
  - "[[Gate Driver Timing Coordination]]"
  - "[[Moore4Power]]"
  - "[[Infineon Technologies]]"
  - "[[Wide Bandgap Semiconductors]]"
  - "[[Silicon Carbide Power Electronics]]"
  - "[[Gallium Nitride Power Electronics]]"
  - "[[WBG Thermal Management]]"
  - "[[Moore's Law and Dennard Scaling]]"
sources:
  - "[[Moore4Power Launch — Semiconductor Today]]"
  - "[[Parasitic Inductance and Switching — Power Electronic Tips]]"
---

# Research: Heterogeneous Integration in Power Electronics

## Overview

Heterogeneous integration (HI) packages **Si, SiC, and GaN dice into one module**, each material doing what it does best — Si for cheap mature drivers/logic, SiC for high-voltage/high-temp switching, GaN for high-frequency low-loss. It is the "More than Moore" answer to broken [[Moore's Law and Dennard Scaling|Dennard scaling]]: gains now come from integration, not node shrink. The €91M EU **[[Moore4Power]]** project (May 2026, [[Infineon Technologies|Infineon]]-led, 62 partners) is the concrete institutional bet on this path. The engineering reality: HI's payoff is bought by **interface engineering** — die-attach, parasitics, gate-timing, thermal, and substrate — and the package, not the silicon, sets the limits.

## Key Findings

- **The thesis is material specialization.** Si ≈ drivers; SiC ≈ 1200 V+, 175–200 °C switches; GaN ≈ 1 MHz+, low-loss. No single material wins everywhere (Source: [[Moore4Power Launch — Semiconductor Today]]; confidence: high).
- **CTE mismatch is the central reliability driver.** SiC ~4.0 vs Si ~2.6 ppm/°C strains the die-attach; **sintered silver** (sinter 250–300 °C, remelt >900 °C, ~250 W/m·K, >4000 cycles 50–250 °C) replaced Pb solder. **Sintered copper** is an emerging challenger with lower CTE mismatch and longer fatigue life (Source: search synthesis, eepower/Springer; confidence: high / medium for Cu) → [[Silver Sintering Die-Attach]].
- **Common-source inductance throttles switching.** L_CS feeds power-loop di/dt back onto the gate (V=L·di/dt), slowing transitions and raising loss; **target < 1 nH**. Worked case: 30 A/50 ns through 3 nH → **1.8 V** CSI bump; flip-chip 0.8 nH → **0.48 V**. With −3 V off-bias and V_th 2.5 V, margin goes 3.7 V → 5.0 V (Source: [[Parasitic Inductance and Switching — Power Electronic Tips]]; confidence: high) → [[Common-Source Inductance]].
- **Gate-timing skew = shoot-through risk.** GaN (1–5 ns) vs SiC (20–50 ns) switching demands matched driver delays; a **10 ns skew** risks shoot-through. Best drivers spec ~2 ns skew (Source: search synthesis, Analog Devices; confidence: high) → [[Gate Driver Timing Coordination]].
- **Substrate trade-off: heat-spread vs fatigue.** AlN DBC (~170 W/m·K) spreads heat best; **Si₃N₄ AMB** (CTE ~3.2 ppm/K, fracture-tough) wins automotive thermal-cycling (3,000–5,000+ cycles, ~50× reliability vs DBC). AMB/Si₃N₄ preferred above ~10,000 cycles or ΔT > 200 °C (Source: search synthesis; confidence: high) → [[Power Module Ceramic Substrates]].
- **Thermal ceiling set by the weakest die.** SiC tolerates ~200 °C; GaN-on-Si caps at ~150–175 °C (buffer-trap leakage). Co-packaged cooling must protect the most fragile device and manage **thermal crosstalk** (Source: search synthesis, MDPI; confidence: high) → [[WBG Thermal Management]].

## Key Entities

- [[Moore4Power]] — €91M EU flagship HI project, 62 partners / 15 countries, 3-year runtime
- [[Infineon Technologies]] — project lead; Si/SiC/GaN supplier
- Named partners: ALSTOM, ABB Finland, Fraunhofer ENAS, INGETEAM, INNOVATION DISCO

## Key Concepts

- [[Heterogeneous Integration (Power Electronics)]] — the umbrella concept (5 engineering tensions)
- [[Multi-Chip Power Module Packaging]] — the stack, wire-bondless trend, new failure modes
- [[Common-Source Inductance]] — parasitic feedback + worked calculation
- [[Silver Sintering Die-Attach]] — CTE-mismatch mitigation
- [[Power Module Ceramic Substrates]] — DBC vs AMB, AlN vs Si₃N₄
- [[Gate Driver Timing Coordination]] — dead-time, propagation-delay skew

## Contradictions

- **Ag-sinter vs Cu-sinter die-attach.** Production automotive SiC uses sintered **silver** (incumbent, proven >4000 cycles). 2024–2025 papers (Springer JEM) argue sintered **copper** has lower CTE mismatch to the Cu substrate and longer fatigue life. Both are credible; the difference is maturity (Ag in production) vs lab-demonstrated advantage (Cu). Not yet resolved.
- **AlN vs Si₃N₄ substrate.** AlN has ~2× the thermal conductivity, yet Si₃N₄ is "better" for automotive — because reliability (CTE match, fracture toughness) outranks raw heat-spreading once thermal-cycling life dominates. Not a contradiction so much as different objective functions (peak thermal vs fatigue life).

## Open Questions

- **Three primary sources were blocked (HTTP 403/404):** the IEEE Heterogeneous Integration Roadmap 2023 power chapter (404 at the tried URL), the eepower silver-sintering article (403), and the MDPI WBG thermal-management review (403). Their claims here rest on search-result synthesis + the two fetched primaries; a follow-up should re-locate and ingest these (try IEEE EPS HIR landing page, DOI for the MDPI paper).
- Quantitative Cu-sinter vs Ag-sinter fatigue-life comparison under identical test conditions — unresolved.
- Real co-packaged Si+SiC+GaN module data (vs separate single-material modules): efficiency, density, and cost deltas — not found; likely still pre-product (Moore4Power deliverables pending).
- GaN-on-SiC (CTE ~4.0) vs GaN-on-Si (CTE ~2.6) trade-off in *heterogeneous* modules specifically — touched but not deep-dived.

## Sources

- [[Moore4Power Launch — Semiconductor Today]] — Semiconductor Today, 2026-05-22 (fetched, high confidence)
- [[Parasitic Inductance and Switching — Power Electronic Tips]] — Power Electronic Tips, undated (fetched, medium confidence)
- Search-synthesis corroboration (not individually filed): eenewseurope & New Electronics (Moore4Power), Analog Devices / PSMA (gate-driver timing), Springer JEM 2025 & Wolfspeed (die-attach reliability), PatSnap / eepower / ScienceDirect (DBC vs AMB substrates), MDPI Electronics 2025 (WBG thermal management), IEEE HIR 2023 power chapter (blocked — see Open Questions).
