---
type: project
title: "Buck Converter BOM (Order-Ready 2026)"
status: developing
created: 2026-06-03
updated: 2026-06-03
tags:
  - project
  - power-electronics
  - bom
  - portfolio
related:
  - "[[Project - Digitally Controlled Synchronous Buck Converter]]"
  - "[[Buck Project — Phases 2-3 Playbook (Power Stage and PCB)]]"
  - "[[Semiconductor Device Fundamentals]]"
  - "[[Consumer Purchase Value Tier List]]"
sources:
  - "[[NUCLEO-G474RE Availability — DigiKey]]"
  - "[[Bourns SRP1265A-330M — DigiKey]]"
  - "[[onsemi FDMS7672 / FDS8880 MOSFETs]]"
  - "[[TI LM5109B / UCC27211 Gate Drivers]]"
  - "[[Rigol DHO800 Series Oscilloscope]]"
---

# Buck Converter BOM (Order-Ready 2026)

Concrete, orderable parts list for the [[Project - Digitally Controlled Synchronous Buck Converter]] (12 V → 5 V @ 3 A, 100 kHz, STM32G4 digital control). Pairs with the [[Buck Project — Phases 2-3 Playbook (Power Stage and PCB)]] — that page has the *why*; this page has the *what to buy*.

> [!warning] How to read "availability" in 2026
> The part numbers below are **manufacturer part numbers (MPNs)** — exact, unambiguous, and what you actually type into the DigiKey/Mouser search box. **Live stock quantity changes daily**, so I can't promise a number will be green at checkout — but I verified each part's **production status** (in production vs end-of-life) as of **June 2026**. Always confirm the green "In Stock" + quantity on the distributor page before you order, and add a backup line where noted.

> [!check] Verified production-status changes vs the project page's representative list
> - ❌ **FDMC8030 dropped** — onsemi lists it **NRND** ("available until stocks exhausted, alternative available"). Replaced with in-production parts below.
> - ✅ **Inductor upgraded** — the suggested Bourns SRP1265A-330M actually has **I_sat ≈ 11 A** (huge margin over your 3.45 A peak), confirmed in stock.
> - 🔄 **Scope rec modernized** — Rigol's current budget line is the **12-bit DHO800 series**; the older DS1054Z still works but is last-gen.

---

## A. Control / brains
| Qty | Item      | MPN                         | Pkg       | Key spec                         | ~$  | Status                                            |
| --- | --------- | --------------------------- | --------- | -------------------------------- | --- | ------------------------------------------------- |
| 1   | MCU board | **NUCLEO-G474RE** (ST)      | Nucleo-64 | HRTIM 184 ps, FMAC, ADC-PWM sync | $16 | ✅ In stock (DigiKey #10231585, Mouser, ST direct) |
| 1   | USB cable | micro-USB (check board rev) | —         | program + power                  | $3  | ✅                                                 |

## B. Power stage (on the PCB)
| Qty | Item | MPN (primary) | Pkg | Key spec | ~$ | Status / notes |
|----|------|---------------|-----|----------|----|----------------|
| 1 | Inductor 33 µH | **SRP1265A-330M** (Bourns) | 12.5×12.5 mm SMD | 33 µH, I_sat ≈ 11 A, I_rms 8 A, DCR 58 mΩ | $2 | ✅ In stock. DCR is a bit high → see low-DCR alt below |
| 2 | MOSFET (low-side + high-side) | **FDMS7672** (onsemi) | Power 56 / SOIC-8 | 30 V, 5.0 mΩ, optimized for sync buck | $1 ea | ✅ In production. **Buy 4** (spares) |
| — | ↳ easier-to-solder alt | **FDS8880** (onsemi) | SOIC-8 | 30 V, 11.6 A, logic-level, classic & cheap | $0.70 ea | ✅ Great hand-solder pick |
| — | ↳ through-hole/breadboard alt | **IRLB8721PBF** (Infineon) | TO-220 | 30 V, logic-level, 62 A | $1 ea | ✅ Best for a first dead-bug / TO-220 build |
| 1 | Gate driver | **LM5109BMA/NOPB** (TI) | SOIC-8 | half-bridge, **integrated bootstrap diode**, ≤90 V | $2 | ✅ In production. Fewer parts (no ext. boot diode) |
| — | ↳ alt (better noise immunity) | **UCC27211D** (TI) | SOIC-8 | half-bridge, integrated 120 V boot diode, hi hysteresis | $2.50 | ✅ Pick if SW-node ringing causes false triggers |

## C. Capacitors
| Qty | Item | MPN / spec | Pkg | Why | ~$ |
|----|------|-----------|-----|-----|----|
| 2 | Output cap 22 µF | **GRM32ER61E226KE15** (Murata) X7R 25 V | 1210 | 2×22 µF for <50 mV ripple, low ESR | $0.50 ea |
| 1 | Input bulk 100 µF | **EEU-FR1E101** (Panasonic FR) 25 V | radial | pulsed input current | $0.50 |
| 1 | Input ceramic 10 µF | **GRM31CR61E106KA12** (Murata) X7R 25 V | 1206 | HF input bypass at the FETs | $0.30 |
| 1 | Bootstrap cap 0.1 µF | C0G/X7R 50 V, 0603 (BST→SW) | 0603 | floating high-side supply — **do not omit** | $0.10 |
| 2 | Driver VCC bypass | 1 µF + 0.1 µF X7R 25 V | 0603 | decouple driver supply | $0.20 |

## D. Resistors, feedback & small signal
| Qty | Item | Spec | Pkg | Why | ~$ |
|----|------|------|-----|-----|----|
| 2 | Feedback divider | 2 kΩ, 1 % | 0805 | 5 V → ~2.5 V into 3.3 V ADC. **Recheck math: never exceed 3.3 V** | $0.10 |
| 1 | Anti-alias cap | ~1 nF C0G | 0603 | RC before the ADC pin | $0.05 |
| 2 | Gate resistors | 2.2–10 Ω | 0805 | tune switching speed / ringing | $0.10 |
| 1 | Passive assortment | 0603/0805 R + C book | — | pull-downs, decoupling, tweaks | $12 |

## E. PCB & mechanical
| Qty | Item | Source | ~$ |
|----|------|--------|----|
| 5 | PCB fab from your KiCad Gerbers | **JLCPCB** (5-board minimum) | $5–10 |
| 2 | Screw terminals (in/out), 5 mm pitch | DigiKey/LCSC generic | $1 |
| 1 | 0.1" pin header strip (MCU interface) | generic | $1 |
| — | Scope test loops on SW / V_out / gate / GND | bare wire | ~$0 |
| — | (defer) current-sense shunt + amp | only for current-mode v2 | — |

---

## F. Bench equipment (one-time; reused on every future build)
| Item | 2026 pick | Why | ~$ |
|------|-----------|-----|----|
| **Oscilloscope** | **Rigol DHO802** (12-bit, 2 ch, 70 MHz, $329) — or **DHO804/DHO814** for 4 ch | Current-gen 12-bit replaces the old DS1054Z; SW-node + transient work. SFRA in firmware avoids a separate network analyzer | $329+ |
| Bench PSU | used 0–30 V / ≥4 A, **current-limit capable** | bring up behind a 4 A limit every time (your safety floor) | $50–70 |
| DC electronic load | used (e.g., budget 150 W unit) — or power resistors ~1.7 Ω / 15 W+ | load sweep for efficiency + transient steps | $25–40 |
| Multimeter | any decent DMM | V / I / continuity | $20–40 |

## G. Tools & consumables (skip what you own)
- Temperature-controlled soldering iron **+ hot-air station** (the SOIC-8 driver/FETs are far easier with hot air; the TO-220 IRLB8721 alt needs only the iron)
- Leaded 63/37 solder, **flux pen**, solder wick, fine tweezers, isopropyl alcohol
- Solderless breadboard + jumpers (early Nucleo/PWM bring-up before the board arrives)
- **Safety glasses** — first power-up

---

## Cost roll-up
| Bucket | ~Cost |
|--------|-------|
| Converter board (A–E) | **$45–60** |
| Bench gear (F) | $425–480 |
| Tools (G), from zero | $60–120 |

**Minimum to first power-up (Phase 4):** A–E + current-limited PSU + a scope. Electronic load, hot-air, and assortment kits are convenience, not blockers.

## Ordering strategy
1. **One DigiKey or Mouser cart** for A–D (free shipping over ~$50 at DigiKey US — easy to hit). LCSC is cheaper for the passive assortment + connectors if you don't mind a separate slow-boat order.
2. **JLCPCB** for the board — upload Gerbers, order while parts ship (~1–2 wk board lead).
3. **Order 2–4× quantity** of the cheap passives and the **bootstrap cap** (tiny, easy to lose/kill).
4. At checkout, **verify each MPN shows green "In Stock"** + your quantity; if a MOSFET line is low, fall back to the listed alt (FDS8880 ↔ FDMS7672 ↔ IRLB8721 are all valid).

> [!gap] Still design-dependent: final inductor DCR (efficiency), exact feedback-divider values (set against your real ADC reference), and cap voltage ratings if you ever raise V_in above 12 V. Confirm against your Phase 0–2 numbers before the cart.

### Low-DCR inductor alternative (efficiency upgrade)
The SRP1265A's 58 mΩ DCR costs ~0.5 W at 3 A. For a cooler, more efficient build: **Würth 7443340330** (33 µH) or **Coilcraft XAL1010-333MEB** (33 µH, ~33 mΩ) — both in production, slightly pricier.
