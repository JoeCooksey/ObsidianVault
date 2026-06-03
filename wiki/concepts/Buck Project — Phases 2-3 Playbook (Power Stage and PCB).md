---
type: project
title: "Buck Project — Phases 2-3 Playbook (Power Stage and PCB)"
status: developing
created: 2026-05-29
updated: 2026-05-29
tags:
  - project
  - power-electronics
  - playbook
  - pcb
  - kicad
related:
  - "[[Project - Digitally Controlled Synchronous Buck Converter]]"
  - "[[Buck Project — Phases 0-1 Playbook (Theory and Simulation)]]"
  - "[[Semiconductor Device Fundamentals]]"
  - "[[EE-Software-on-Linux-Mint]]"
---

# Buck Project — Phases 2–3 Playbook (Power Stage & PCB)

Turn the validated design into a real BOM and a manufacturable board. This is where most of the *engineering judgment* lives — every part is a tradeoff.

## Phase 2 — Power-stage design & BOM (~2 weeks)

Go down this list; for each part, **write the calc or datasheet number that justifies it**. That justification IS the deliverable.

### Week 1 — The power components
- **Inductor (33 µH):** from Phase 0. Now add two more specs: **saturation current ≥ 5 A** (your peak is 3.45 A — leave margin) and **low DCR** (DC resistance, e.g., <30 mΩ, for efficiency). Shielded power inductor.
- **Output capacitor (≈44 µF):** use 2× 22 µF ceramic (X7R, ≥10 V rating). Low ESR keeps ripple down. Check the ESR-ripple term `ΔI_L·ESR` is small vs your 50 mV budget.
- **Input capacitor:** a bulk electrolytic (e.g., 100 µF) + ceramic (10 µF) close to the FETs to handle the pulsed input current.
- **MOSFETs (×2, N-channel):** V_DS ≥ 30 V (≈2.5× your 12 V), **logic-level gate** if your driver outputs ~5 V. Balance low **R_DS(on)** (conduction loss) against low **gate charge Q_g** (switching loss). A 30 V dual-N-channel in one package is beginner-friendly.

### Week 2 — Drive, sense, and feedback
- **Gate driver:** a **half-bridge driver with bootstrap** (e.g., UCC27211 or LM5109). The bootstrap cap (0.1 µF, BST→SW) is the floating supply that turns on the high-side FET. Bypass VCC with 1–2.2 µF.
- **Feedback divider:** scale 5 V down to your MCU's ADC range. STM32 ADC is 0–3.3 V, so divide 5 V → ~2.5 V (e.g., 2 kΩ / 2 kΩ). Add an **anti-alias RC** (small cap) before the ADC pin.
- **Current sense (only needed for current-mode later):** a small shunt + current-sense amp, or inductor-DCR sensing. **Skip for now** — you're doing voltage-mode first.
- **Connectors/test points:** input, output, ground, and a header to the MCU board. Add scope test points on SW, V_out, and gate.
- **Resources:** [[Semiconductor Device Fundamentals]] for picking FETs; the gate-driver and inductor datasheets.

> [!check] Phase 2 done when: a spreadsheet BOM where every row has a part number AND the number (calc or datasheet spec) that justifies it.

> [!tip] Order-ready starting BOM: [[Buck Converter BOM (Order-Ready 2026)]] has exact MPNs + June-2026 availability (FDMS7672/FDS8880 FETs, LM5109B driver, SRP1265A-330M inductor). Still do the justification calc per row yourself — that's the deliverable.

## Phase 3 — PCB layout in KiCad (~3–4 weeks)

KiCad 10 is native on your Mint ([[EE-Software-on-Linux-Mint]]). **Layout is the single highest-skill part of this project** — a working schematic with a bad layout will oscillate, get hot, or radiate noise.

### Week 1 — Learn KiCad + draw the schematic
- **Do:** work one KiCad beginner tutorial end-to-end (search "Phil's Lab KiCad" — the standard free course). Then capture your schematic: input/output connectors, caps, the two FETs, the gate driver, the inductor, the feedback divider, the MCU header. **Assign a footprint to every part.**
- **Deliverable:** a complete, annotated schematic that passes the ERC (electrical rules check).

### Week 2 — Layout fundamentals for power (learn these 5 rules)
1. **Tiny hot loop.** The high-frequency current path is: input cap (+) → high-side FET → low-side FET → input cap (−). Make this loop **as small as physically possible** — it's the #1 source of noise and ringing.
2. **Small SW node.** The switching node (between the FETs and the inductor) swings 12 V at 100 kHz — keep its copper area minimal to cut radiated EMI, but wide enough for the current.
3. **Short gate loops.** Driver output → FET gate → driver return, kept short and tight, or the FET switches poorly.
4. **Split grounds, join once.** Keep the noisy **power ground** separate from the quiet **signal/analog ground** (ADC divider), connected at a single star point.
5. **Thermal.** Copper pour + several vias under the FETs and inductor to spread heat.

### Week 3–4 — Route, check, order
- **Do:** route power traces thick (use a trace-width calculator for 3 A), run **DRC** (design rule check) until clean, add a ground pour, generate **Gerber** files.
- **Order:** upload Gerbers to **JLCPCB** (~$10 for 5 boards). While you wait (~1–2 weeks), order the BOM parts (Digi-Key/Mouser/LCSC).
- **Resources:** Phil's Lab (PCB layout + STM32), Rick Hartley's grounding talk (free on YouTube — the classic).

> [!check] Phase 3 done when: DRC passes, Gerbers ordered, parts ordered. You now have a real board coming in the mail.

## Common beginner mistakes (Phases 2–3)
- Big hot loop → ringing and EMI you'll chase for weeks. Get the loop tight first.
- Forgetting the bootstrap cap → high-side FET never turns on.
- Feedback divider that exceeds the ADC's 3.3 V max → you fry the input. Double-check the math.
- Traces too thin for 3 A → voltage drop and heat. Use the calculator.

→ Next: [[Buck Project — Phases 4-6 Playbook (Bring-up, Firmware, Validation)]]
