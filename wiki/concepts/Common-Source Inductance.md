---
type: concept
title: "Common-Source Inductance"
created: 2026-05-29
updated: 2026-05-29
tags:
  - concept
  - domain/engineering
  - power-electronics
  - parasitics
  - gate-drive
status: developing
complexity: advanced
domain: engineering
aliases: ["L_CS", "common source inductance", "CSI", "source inductance"]
related:
  - "[[Heterogeneous Integration (Power Electronics)]]"
  - "[[Multi-Chip Power Module Packaging]]"
  - "[[Gate Driver Timing Coordination]]"
  - "[[Silicon Carbide Power Electronics]]"
  - "[[Gallium Nitride Power Electronics]]"
sources:
  - "[[Parasitic Inductance and Switching — Power Electronic Tips]]"
---

# Common-Source Inductance

## What it is

**Common-source inductance (L_CS)** is the parasitic inductance *shared* by the drain-to-source power-current path and the gate-driver loop — typically the source bond wires plus substrate routing between a [[Silicon Carbide Power Electronics|SiC]]/[[Gallium Nitride Power Electronics|GaN]] switch and its Si gate driver (Source: [[Parasitic Inductance and Switching — Power Electronic Tips]]).

In [[Heterogeneous Integration (Power Electronics)|heterogeneous modules]], the Si-driver-to-WBG-switch routing is exactly where L_CS lives. **Target: L_CS < 1 nH.**

## Why it hurts: negative feedback

As drain current changes rapidly during switching, the di/dt induces a voltage across L_CS that **opposes the gate-drive voltage** (V = L·di/dt). This:

- reduces the effective gate-drive voltage and current,
- slows turn-on and turn-off,
- and therefore **increases switching loss** (Source: [[Parasitic Inductance and Switching — Power Electronic Tips]]).

During turn-off it can also push a *positive bump* onto V_GS, risking false turn-on / shoot-through (see [[Gate Driver Timing Coordination]]).

## Worked calculation (V = L_CS · di/dt)

Half-bridge SiC module: 800 V, 30 A switching, turn-on ~50 ns.

**(a) Brief's literal framing — gate-drive current 2 A over 50 ns:**
$$dI/dt = 2\,\text{A}/50\,\text{ns} = 4\times10^{7}\,\text{A/s}$$
$$V = 3\,\text{nH}\times4\times10^{7} = \mathbf{0.12\ V}$$

**(b) Physically dominant framing — the *drain* current (30 A) couples through L_CS:**
$$dI/dt = 30\,\text{A}/50\,\text{ns} = 6\times10^{8}\,\text{A/s}$$
$$V = 3\,\text{nH}\times6\times10^{8} = \mathbf{1.8\ V}$$

> [!note] Which framing is right?
> The common-source feedback that decelerates switching is driven by the **power-loop (drain) di/dt**, not the gate current — so (b) is the meaningful number. The brief's (a) gate-current framing understates the effect by ~15×. Both are shown for completeness.

## Margin against false turn-on

With off-state bias **−3 V** and a 1200 V SiC MOSFET **V_th ≈ 2.5 V**:

| L_CS | CSI bump (drain framing) | Gate sits at | Margin below V_th |
|---|---|---|---|
| 3.0 nH | +1.8 V | −1.2 V | 3.7 V ✅ |
| 0.8 nH (flip-chip) | +0.48 V | −2.52 V | 5.0 V ✅ |

**Assessment:** −3 V off-bias is comfortable margin in both cases. Reducing L_CS from 3 nH → 0.8 nH (e.g. **flip-chip die-attach** eliminating source bond wires) widens the margin from 3.7 V to 5.0 V and roughly **4× lowers** the switching-loss penalty. The real shoot-through risk is L_CS combined with Miller dV/dt coupling through C_gd — negative bias defends against both.

## Mitigations

- **Kelvin-source connection**: a dedicated source pin gives the gate loop its own return path, *not* shared with the power loop — removes L_CS from the gate circuit (Source: web search synthesis, Wolfspeed; confidence: high).
- **Flip-chip / wire-bondless die-attach**: eliminates source bond-wire inductance.
- **Driver placement**: gate driver physically adjacent to the switch minimizes total gate-loop inductance.
- **Negative off-bias** (−3 to −5 V for SiC): holds the gate clear of V_th against CSI + Miller bumps.
