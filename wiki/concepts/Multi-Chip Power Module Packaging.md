---
type: concept
title: "Multi-Chip Power Module Packaging"
created: 2026-05-29
updated: 2026-05-29
tags:
  - concept
  - domain/engineering
  - power-electronics
  - packaging
status: developing
complexity: advanced
domain: engineering
aliases: ["MCPM", "multi-chip power module", "power module packaging"]
related:
  - "[[Heterogeneous Integration (Power Electronics)]]"
  - "[[Common-Source Inductance]]"
  - "[[Silver Sintering Die-Attach]]"
  - "[[Power Module Ceramic Substrates]]"
  - "[[WBG Thermal Management]]"
  - "[[Silicon Carbide Power Electronics]]"
sources:
  - "[[Parasitic Inductance and Switching — Power Electronic Tips]]"
---

# Multi-Chip Power Module Packaging

The package is the system. In WBG and [[Heterogeneous Integration (Power Electronics)|heterogeneous]] modules, packaging — not the die — sets the practical limits on speed, reliability, and power density.

## The stack (bottom → top)

1. **Baseplate / heatsink** (Cu or AlSiC) — heat path out
2. **Thermal interface material (TIM)** — couples baseplate to cooler
3. **Ceramic substrate** — electrical isolation + heat spreading → [[Power Module Ceramic Substrates]] (DBC on AlN, AMB on Si₃N₄)
4. **Die-attach** — bonds chip to substrate → [[Silver Sintering Die-Attach]]
5. **Power dice** — Si / SiC / GaN
6. **Top-side interconnect** — Al/Cu bond wires, or wire-bondless (Cu clip, flip-chip, sintered planar)

## Trends pushing power density

- **Wire-bond → wire-bondless.** Bond wires dominate parasitic [[Common-Source Inductance|inductance]] and are a top fatigue/failure site. Cu clips, flip-chip, and planar sintered interconnect cut both inductance and failure rate.
- **Double-sided cooling.** Heat extracted from both faces of the die roughly halves thermal resistance vs single-side.
- **Embedded die.** Embedding SiC dice into multilayer ABF/PCB substrates (e.g. Single-Side-Copper exposed modules) shortens interconnects and shrinks the module (Source: web search synthesis, PCIM 2026; confidence: medium).
- **Co-packaged gate drivers.** Placing the Si driver in-package next to the WBG switch minimizes gate-loop inductance and ringing — central to the [[Heterogeneous Integration (Power Electronics)|HI]] thesis.

## New failure modes from heterogeneity

- **CTE-mismatch fatigue** at die-attach and substrate interfaces under thermal cycling (the dominant wear-out path) → [[Silver Sintering Die-Attach]], [[Power Module Ceramic Substrates]].
- **Thermal crosstalk** — a hot SiC die raising the junction temperature of an adjacent, more-fragile GaN die in the same package.
- **Parasitic coupling** between dissimilar dice with very different di/dt and dV/dt → [[Common-Source Inductance]], [[Gate Driver Timing Coordination]].

> [!tip] Design rule
> Reliability of a multi-chip module is governed by its **weakest interface**, and its speed by its **largest parasitic loop**. Both live in the packaging, not the silicon.
