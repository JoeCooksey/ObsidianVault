---
type: concept
title: "Semiconductor Device Fundamentals"
created: 2026-04-27
updated: 2026-04-27
tags:
  - EE
  - semiconductors
  - MOSFET
  - diode
  - BJT
  - power-electronics
  - device-physics
status: developing
---
# Semiconductor Device Fundamentals

Understanding what happens inside electronic devices — not just their circuit behavior, but their physics. This is the gateway to power electronics, WBG device selection, and IC design.

## Why Device Physics Matters

The power MOSFET is the most common power semiconductor device in the world. SiC and GaN are wide-bandgap MOSFETs at their core. Without device physics, you cannot understand:
- Why SiC switches faster than silicon
- What causes $E_{on}$, $E_{off}$, and $Q_{rr}$ in a double pulse test
- How to choose gate resistance for switching loss vs. ringing tradeoff
- Why parallel MOSFETs require matched threshold voltages
- Why the body diode matters in a synchronous buck converter

The hiring filter in power electronics interviews is often: *"Can you explain what determines switching loss from first principles?"*

## The Device Stack (in order of complexity)

### 1. Semiconductor Material Basics
- Silicon: 4 valence electrons, crystal diamond lattice, band gap 1.1 eV
- **N-type doping**: add Group V (phosphorus, arsenic) → excess free electrons
- **P-type doping**: add Group III (boron) → excess holes
- **Band gap energy**: the energy between valence and conduction bands
  - Si: 1.1 eV | SiC: 3.26 eV | GaN: 3.4 eV
  - Higher band gap → higher breakdown field → key to WBG advantage

### 2. P-N Junction and Diode
- When P and N materials contact: electrons diffuse into P, holes into N → depletion region forms
- Built-in potential ~0.6V (Si); ~2.7V (SiC Schottky)
- **Forward bias**: narrows depletion region → exponential current increase
- **Reverse bias**: widens depletion region → blocks current (small leakage only)
- **Diode equation**: $I = I_s(e^{V/nV_T} - 1)$ where $V_T = kT/q \approx 26$ mV at room temp
- **Reverse recovery charge ($Q_{rr}$)**: charge stored in diode minority carriers during forward conduction; must be extracted when diode turns off; causes current spike and switching loss; SiC Schottky diodes have near-zero $Q_{rr}$ — a key WBG advantage

### 3. Bipolar Junction Transistor (BJT)
- Three regions: emitter (heavily doped), base (thin), collector
- **Current-controlled**: $I_C = \beta I_B$ where $\beta$ (current gain) = 50–300
- **Operating modes**:
  - Active: $V_{BE} > 0$, $V_{BC} < 0$ → amplifier
  - Saturation: both junctions forward biased → switch ON (low $V_{CE}$)
  - Cutoff: both junctions reverse biased → switch OFF
- Not used in modern power electronics (replaced by MOSFET/IGBT) but essential for analog design, op-amp internals, and understanding transistor switching concepts

### 4. MOSFET — The Core Power Device
- **Voltage-controlled**: gate voltage controls channel conductivity; almost no steady-state gate current
- **N-channel enhancement MOSFET** (most common in power electronics):
  - $V_{GS} < V_{th}$: no channel → device in cutoff (OFF)
  - $V_{GS} > V_{th}$: inversion layer forms → channel conducts (ON)
- **Key datasheet parameters**:
  - $R_{DS(on)}$: on-state resistance — determines conduction loss $P_{cond} = I^2 R_{DS(on)}$
  - $V_{th}$: threshold voltage — sets gate drive voltage requirements
  - $C_{iss}, C_{oss}, C_{rss}$: input/output/reverse capacitances — determine switching speed
  - $Q_g$: gate charge — determines gate drive current needed
  - $Q_{rr}$: body diode reverse recovery — critical for synchronous converters
- **Body diode**: inherent to MOSFET structure (parasitic p-n junction); acts as free-wheeling diode in converter dead time; must be considered in synchronous converter dead-time design

### 5. MOSFET I-V Characteristics
- **Linear (ohmic) region**: $I_D \approx k(V_{GS}-V_{th})V_{DS}$ for small $V_{DS}$
  - $R_{DS(on)} = 1/[k(V_{GS}-V_{th})]$ — minimized at high gate drive voltage
- **Saturation region**: $I_D = \frac{k}{2}(V_{GS}-V_{th})^2$ — current saturates with $V_{DS}$
- In power switching: want fully enhanced gate ($V_{GS}$ >> $V_{th}$) → minimize $R_{DS(on)}$

### 6. IGBT — High-Voltage Power Device
- Combines MOSFET gate control with bipolar current capacity
- Used when blocking voltage > 600V (EV main traction inverter, grid inverters)
- Slower switching than MOSFET (minority carrier device); but handles higher currents at same die size
- SiC MOSFET is actively replacing IGBT even at 1200V in new automotive designs

### 7. Wide Bandgap Device Physics

**SiC MOSFET advantages over Si:**
- 10× higher breakdown electric field → thinner drift region → lower $R_{DS(on)}$ at same blocking voltage
- Higher thermal conductivity (3.7× vs Si) → runs cooler at same power density
- Higher operating junction temperature (up to 175°C)
- Body diode has higher forward voltage (~3V) → often paralleled with external SiC Schottky

**GaN HEMT (High Electron Mobility Transistor) differences:**
- **Not a MOSFET** — uses 2D electron gas (2DEG) at AlGaN/GaN interface
- Lateral device (current flows horizontally, not vertically)
- No inherent body diode (anti-parallel Schottky required externally)
- Very low gate charge → extremely fast switching at lower voltages
- Current power envelope: up to 650V/100A commercial; 1200V in development

## Key Resources

| Resource | Best For |
|----------|---------|
| Neamen "Semiconductor Physics and Devices" | ASU standard; physics-first |
| Sedra & Smith "Microelectronic Circuits" | Design-oriented; circuits + devices |
| All About Circuits — Power Semiconductors | Free reference, excellent diagrams |
| Wolfspeed / Infineon application notes | Real SiC/GaN device behavior |

## Joe's Milestones: Device Physics → WBG

1. Derive the diode I-V equation qualitatively from depletion region physics
2. Explain why SiC has higher breakdown voltage: larger band gap → higher electric field before avalanche
3. Read a full SiC MOSFET datasheet (e.g., Wolfspeed C3M0016120K): find $R_{DS(on)}$, $V_{th}$, $C_{iss}$, $Q_g$, $Q_{rr}$, thermal resistance
4. Simulate MOSFET switching transient in LTSpice using real Wolfspeed SPICE model
5. Calculate turn-on switching loss: $E_{on} \approx \frac{1}{2} V_{DS} I_D t_{ri}$ where $t_{ri}$ = current rise time
6. Explain why $Q_{rr} \approx 0$ in SiC Schottky diode → hard-switching loss reduction

## Related Concepts
- [[Wide Bandgap Semiconductors]]
- [[Silicon Carbide Power Electronics]]
- [[Gallium Nitride Power Electronics]]
- [[Circuit Theory Fundamentals]]
- [[EE Physical Side — Actionable Skill Plan]]
- [[EE Topic Depth Priority Map]]
