---
type: concept
title: "Buck Converter PCB Design and Fabrication"
created: 2026-05-05
updated: 2026-05-05
tags:
  - concept
  - domain/engineering
  - power-electronics
  - PCB
  - KiCad
  - hardware
status: complete
complexity: intermediate
domain: engineering
aliases: ["KiCad buck PCB", "JLCPCB power electronics PCB"]
related:
  - "[[Buck Converter Theory and Design]]"
  - "[[STM32 Digital Control for Buck Converter]]"
  - "[[Buck Converter Measurement and Characterization]]"
sources:
  - "[[Research - Buck Converter Build Guide]]"
---
# Buck Converter PCB Design and Fabrication

KiCad schematic capture, PCB layout, and JLCPCB fabrication guide for the 12V→5V, 1A, 100 kHz synchronous buck converter.

## 1. Phase 1: Breadboard Prototype (Weeks 7–8)

**Do this before PCB.** The breadboard catches wiring mistakes and lets you adjust component values without throwing away a board.

### Breadboard Gotchas for Power Electronics

- **Long breadboard wires = antennas**: keep power loop wires < 3 cm. Twist Vin+ and GND wires together.
- **Breadboard parasitic inductance**: ~10 nH/cm of trace. At 100 kHz this is negligible, but at 1 MHz it would matter. Fine for 100 kHz.
- **Ground: use a thick wire**: 22 AWG minimum for 1A current paths.
- **Decoupling capacitors**: place 100 nF ceramic directly at IR2110 VCC and VDD pins — not 5 cm away.
- **Bootstrap diode**: must be ultrafast (UF4007, not 1N4007). Place right next to IR2110 VB pin.
- **Test waveforms first at low power**: use 5V input and a 10Ω, 5W load resistor before going to 12V.

## 2. KiCad Schematic Capture

### Install KiCad

Download KiCad 8.x (free, open-source) from kicad.org. No license required.

### Project Structure

Create a new project: `buck_converter/`. KiCad creates:
- `buck_converter.kicad_sch` — schematic
- `buck_converter.kicad_pcb` — PCB layout
- `buck_converter.kicad_pro` — project file

### Schematic Sections (by functional block)

Draw these as separate sections on the schematic, labeled with power flags and net names.

#### Section 1: Input Power Stage
```
J1 (XT60 connector, Vin+) ──── F1 (polyfuse 2A) ──── Vin net
J1 (GND) ──── GND net
C_in1 (47µF/25V electrolytic) between Vin and GND
C_in2 (100nF ceramic) between Vin and GND
```

#### Section 2: Gate Driver (IR2110)
```
U1 IR2110:
  VCC ──── 12V rail
  VDD ──── 3.3V rail (from STM32 3V3 pin)
  HIN ──── PA8 (STM32 header)
  LIN ──── PB13 (STM32 header)
  SD  ──── 3.3V (always enabled; tie to GPIO for enable control)
  VB  ──── Bootstrap circuit (via D_boot UF4007 from VCC; C_boot 220nF to VS)
  VS  ──── SW node
  HO  ──── R_gate_hi (10Ω) ──── M1 Gate (high-side MOSFET)
  LO  ──── R_gate_lo (10Ω) ──── M2 Gate (low-side MOSFET)
  COM ──── GND
```

#### Section 3: Power Stage
```
M1 (IRLZ44N or IRFZ44N):
  Drain ──── Vin
  Gate  ──── R_gate_hi
  Source ──── SW node

M2 (IRLZ44N or IRFZ44N):
  Drain ──── SW node
  Gate  ──── R_gate_lo
  Source ──── GND (power ground)

L1 (100µH Bourns) between SW node and Vout
C_out1 (22µF/10V MLCC) between Vout and GND
C_out2 (22µF/10V MLCC) between Vout and GND
C_out3 (100µF/10V electrolytic) between Vout and GND
```

#### Section 4: Feedback Divider
```
R_fb1 (10kΩ, 1%) between Vout and V_sense
R_fb2 (10kΩ, 1%) between V_sense and GND
C_fb (100nF) between V_sense and GND
J2 (2-pin header): V_sense and GND → STM32 PA0
```

#### Section 5: Output Connector
```
J3 (XT30 or screw terminal): Vout+ and Vout−/GND
```

### KiCad Symbol Tips

- Built-in library has IRFZ44N under `Device:IRFZ44N`
- IR2110: search for it in "Analog_SwitchingRegulator" or add manually from Mouser part
- Add power symbols (PWR_FLAG) at Vin, GND, 3.3V to eliminate ERC warnings
- Use net labels instead of wires across long distances (cleaner schematic)

## 3. PCB Layout — Priority Order

Power electronics PCB layout is 90% about current loop minimization. Follow this order:

### Rule 1: Minimize the Primary Switching Loop

The highest-priority current loop: Vin cap → M1 Drain → M1 Source (SW node) → L1 → Vout → Load → GND → Vin cap

This loop carries pulsed current at 100 kHz with fast switching edges. Every cm² of loop area = more EMI, more ringing, more voltage spikes.

**Layout target**: Input cap, M1, M2, and their common nodes should fit within a 15×15mm square.

### Rule 2: Component Placement

Place in this order (don't route yet):
1. **Input capacitors** directly at M1 drain (Vin) and M2 source (GND) — this is non-negotiable
2. **M1 and M2** side by side, sharing the SW node between them
3. **Gate driver (IR2110)** directly behind the MOSFETs
4. **Bootstrap diode and capacitor** touching the IR2110 VB and VS pins
5. **Inductor L1** at the SW node, away from signal traces
6. **Output capacitors** directly at the output end of L1
7. **Feedback divider** away from the switching node (far side of the board)
8. **STM32 connector** at the edge of the board

### Rule 3: Copper Pour Zones

- Create a **power ground plane** on the bottom layer covering the entire power section
- Create a **signal ground plane** on the bottom layer for the feedback/control section
- Connect both grounds at a single point (star ground) near the input capacitor
- The SW node (M1 source/M2 drain junction) is the noisiest node — use a minimal copper pour here (just enough for current capacity). Oversized SW node pours radiate more EMI.

### Rule 4: Trace Widths

Current carrying capacity (using PCB trace width calculator, 1 oz copper, 10°C rise):

| Current | Minimum Width | Recommended Width |
|---------|--------------|-------------------|
| 1A (output) | 0.5 mm | 1.0 mm |
| 1A (SW node, pulsed) | 0.5 mm | 1.5 mm (wider for lower inductance) |
| Gate drive (~100 mA) | 0.2 mm | 0.5 mm |
| Feedback signal (<1 mA) | 0.127 mm | 0.25 mm |

### Rule 5: Via Placement

- Use vias to stitch ground pour top↔bottom every 5–10 mm throughout the power ground plane
- Place vias under MOSFETs (if using SMD packages) for thermal relief → connects to bottom copper pour as heatsink
- Don't place vias in the middle of power traces

### JLCPCB Design Rules (KiCad DRC Settings)

| Parameter | JLCPCB Standard |
|-----------|-----------------|
| Min trace width | 0.127 mm (5 mil) |
| Min trace spacing | 0.127 mm (5 mil) |
| Min via drill | 0.2 mm |
| Min via annular ring | 0.2 mm |
| Min silkscreen width | 0.15 mm |
| Board thickness | 1.6 mm (standard) |

Import the `.kicad_dru` file from github.com/labtroll/KiCad-DesignRules into your project folder. This auto-configures KiCad's DRC to match JLCPCB specs.

### Board Size and Layer Stack

**2-layer board (cheapest option)**:
- Top layer: power traces and components
- Bottom layer: ground plane (copper pour)
- Board size: 60×50mm is sufficient for this design

2-layer is fine at 100 kHz. You'd want 4-layer for > 500 kHz designs.

## 4. Generating Gerbers for JLCPCB

1. **Run DRC** (Inspect → Design Rule Checker): zero errors required before generating
2. **File → Fabrication Outputs → Gerbers**:
   - Output folder: `gerbers/`
   - Select layers: F.Cu, B.Cu, F.Mask, B.Mask, F.SilkS, B.SilkS, Edge.Cuts
   - Enable: Plot footprint values, Plot reference designators
3. **File → Fabrication Outputs → Drill Files**:
   - Format: Excellon
   - Units: mm
4. **Zip** the `gerbers/` folder
5. Upload to jlcpcb.com → drag zip file → review 3D preview

### JLCPCB Order Settings (Standard 2-Layer)

| Setting | Value |
|---------|-------|
| Layers | 2 |
| Dimensions | from your board |
| PCB Color | Green (cheapest) |
| Surface Finish | HASL (cheapest, fine for through-hole and large SMD) |
| Copper Weight | 1 oz (standard) |
| Quantity | 5 |
| **Price** | **~$2–5 + $15–20 shipping** |

Total cost: ~$20 for 5 boards delivered in 2–3 weeks.

## 5. PCB Assembly

You'll solder the boards yourself. Order of assembly:

1. **Inspect PCB**: check for obvious shorts under magnification
2. **Solder SMD components first** (if using SMD): resistors, capacitors, diode
3. **Solder IR2110** (if DIP-14 package is used for prototyping): easiest to start with
4. **Solder MOSFETs**: TO-220 through-hole — add heatsink compound if thermally stressed
5. **Solder inductor**: largest component, goes last
6. **Solder connectors and headers**: output connector, STM32 header, test point pads

### Test Points — Add to Schematic

Add TP (test point) pads to the schematic/layout for:
- Vin and GND
- SW node (inductor current waveform measurement)
- Vout and GND
- Gate of M1 (HO) and Gate of M2 (LO)
- V_sense (feedback ADC input)

These are just exposed copper pads where you can clip oscilloscope probes. Critical for debugging.

## 6. Component Sourcing

| Component | Part Number | Source | ~Cost |
|-----------|------------|--------|-------|
| STM32 Nucleo-64 | NUCLEO-F446RE | Mouser/Digi-Key | $15 |
| Gate driver | IR2110PBF | Mouser | $2.50 |
| High-side MOSFET | IRLZ44NPBF | Mouser | $0.80 |
| Low-side MOSFET | IRLZ44NPBF | Mouser | $0.80 |
| Bootstrap diode | UF4007 | Mouser | $0.15 |
| Inductor | Bourns SRR1260-101Y | Digi-Key | $1.50 |
| Output cap | GRM31CR61A476ME15 (47µF) | Mouser | $0.60 ea |
| Input cap | 47µF/25V electrolytic | Amazon | $0.10 |
| Gate resistor | 10Ω 0.25W | Amazon (pack) | <$0.10 |
| Bootstrap cap | 220nF ceramic | Amazon (pack) | <$0.10 |
| Feedback resistors | 10kΩ 1% | Amazon (pack) | <$0.10 |
| PCB | JLCPCB (5 boards) | JLCPCB | ~$20 shipped |
| **Total** | | | **~$45–55** |
