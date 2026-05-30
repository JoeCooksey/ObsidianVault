---
type: concept
title: "Gate Driver Timing Coordination"
created: 2026-05-29
updated: 2026-05-29
tags:
  - concept
  - domain/engineering
  - power-electronics
  - gate-drive
status: developing
complexity: advanced
domain: engineering
aliases: ["dead-time", "propagation delay skew", "gate driver timing", "shoot-through prevention"]
related:
  - "[[Heterogeneous Integration (Power Electronics)]]"
  - "[[Common-Source Inductance]]"
  - "[[Multi-Chip Power Module Packaging]]"
  - "[[Gallium Nitride Power Electronics]]"
  - "[[Silicon Carbide Power Electronics]]"
---

# Gate Driver Timing Coordination

## The half-bridge constraint

In a half-bridge, the high-side and low-side switches must **never conduct simultaneously** — that is a **shoot-through** short across the DC bus. A small **dead-time** (both off) prevents it:

- **Too short** → shoot-through current spikes as the two devices briefly overlap.
- **Too long** → energy wasted in body-diode / synchronous conduction; in WBG this also means costly reverse conduction.

## Why heterogeneity makes it hard

GaN and SiC switch at very different speeds (Source: command brief + web search synthesis; confidence: high):

| Device | Rise/fall (t_r/t_f) |
|---|---|
| **GaN** | ~1–5 ns |
| **SiC** | ~20–50 ns |

Mixing them — or even pairing two devices driven by different driver channels — means **propagation-delay skew** (the mismatch in driver input→output delay) eats directly into the dead-time budget. A **10 ns mismatch** in a mixed GaN/SiC half-bridge is enough to cause shoot-through risk.

For GaN especially, switching is so fast that the dead-time window can be only a few ns, so the **driver's delay skew must be smaller than the dead-time** you are trying to hold.

## Design requirements

- **Low, well-matched propagation delay** between high-side and low-side outputs. Advanced isolated drivers spec **~2 ns skew at 25 °C, ≤5 ns over −40 → +125 °C** (Source: web search synthesis, Analog Devices; confidence: high).
- **Adjustable dead-time** so the window can be tuned to the device pair.
- **High CMTI** (common-mode transient immunity) to survive the fast dV/dt of WBG switching without false triggering.
- Pair with **negative off-bias** and low [[Common-Source Inductance|L_CS]] so a di/dt-induced gate bump cannot finish what a timing skew starts.

> [!tip] The coupling
> Timing skew and [[Common-Source Inductance|common-source inductance]] are the same failure (false/shoot-through turn-on) reached by two roads — one temporal, one parasitic. A robust [[Heterogeneous Integration (Power Electronics)|HI module]] must close both.
