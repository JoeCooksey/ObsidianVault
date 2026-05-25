---
type: concept
title: "EE Software and Lab Tools Complete Stack"
created: 2026-05-25
updated: 2026-05-25
tags:
  - electrical-engineering
  - tools
  - software
  - simulation
  - pcb
  - lab-instruments
  - fpga
status: developing
---
# EE Software and Lab Tools Complete Stack

Full reference for all software and hardware tools a professional EE uses. Organized by category and phase of learning. See [[EE Complete Mastery Roadmap]] for where each tool fits in the progression.

---

## Category 1: Circuit Simulation (SPICE)

### LTSpice — Tier 1, Start Day 1
- **By**: Analog Devices | **Cost**: Free
- **Best for**: analog circuits, power electronics, switched-mode converters
- **Key simulation types**: `.op` (DC bias) → `.tran` (time domain) → `.ac` (Bode plot) → `.dc` (source sweep)
- **10-circuit ladder**: voltage divider → RC filter → RL → RLC → diode rectifier → op-amp inverting → active filter → MOSFET I-V → buck converter → closed-loop buck
- **Monte Carlo**: `R={mc(1k,0.05)}` + `.step param run 1 100 1` → 100 random tolerance runs
- **Model import**: download `.lib` from TI/Wolfspeed/Infineon → `.lib "path/model.lib"` directive
- See [[LTSpice Complete Skills Guide]] for the full reference

### Other SPICE Tools
| Tool | Best For | Cost |
|------|---------|------|
| LTSpice | Analog / power electronics | Free |
| Ngspice | Open-source, scriptable, Python-driven | Free |
| PSpice (Cadence) | Academic circuits | University |
| Spectre (Cadence) | Transistor-level IC simulation | University |
| HSPICE (Synopsys) | High-accuracy IC | University |
| Tinkercad Circuits | Absolute beginners + Arduino | Free |
| Falstad Circuit Sim | Visual, browser-based learning | Free |

---

## Category 2: System-Level Simulation

### Python Scientific Stack (Free MATLAB replacement)
```
numpy              — arrays, matrix ops, linear algebra
scipy.signal       — filter design (firwin, butter, freqz), Bode, FFT
scipy.linalg       — matrix factorization, solve Ax=b (nodal analysis)
scipy.integrate    — ODE solvers → circuit transients (solve_ivp)
matplotlib         — all plotting (time domain, Bode, FFT, pole-zero)
python-control     — Bode, root locus, step response, gain/phase margin, PID
PyLTSpice          — LTSpice automation: parametric sweep → extract → plot
PyVISA             — lab instrument control via GPIB/USB/LAN (SCPI commands)
pandas             — waveform data analysis, Monte Carlo results
```

### MATLAB + Simulink
- **For**: signals/systems coursework, control systems design, DSP, power systems
- **Key toolboxes**: Signal Processing, Control System, Power Electronics, Communications, DSP, Robotics
- **Free alternative for scripting**: GNU Octave (~90% compatible)
- **Simulink alternatives**: python-control + matplotlib for simple loops; Modelica for complex physical systems
- **Matlab Coder**: auto-generates C from MATLAB (bridge Python→C for embedded)

---

## Category 3: PCB Design

### KiCad — Tier 1 for Students
- **By**: CERN | **Cost**: Free, open-source
- **Features**: schematic capture, PCB layout, 3D preview, DRC, Gerber/drill export
- **Native format**: text-based (.kicad_sch, .kicad_pcb) — excellent for Git version control
- **Learning path**: Schematic (Week 1) → Component library (Week 2) → PCB layout (Week 2–3) → DRC + Gerber (Week 3) → 4-layer board with controlled impedance (Month 3)
- **Best free course**: Phil's Lab on YouTube — hands-on KiCad STM32 + ESP32 boards

### PCB Design Tool Comparison
| Tool | Tier | Industry Fit | Cost |
|------|------|-------------|------|
| KiCad | Student/startup | Growing fast | Free |
| Altium Designer | Professional (industry #1) | Most jobs | Paid ($6k/yr, student free) |
| Eagle (Autodesk) | Maker-friendly | Smaller companies | Free (limited) |
| OrCAD/Allegro | Large companies | Defense, telecom | University |
| Fusion 360 Electronics | MCAD+ECAD integration | Product design | Free (personal) |
| Cadence Allegro | High-speed digital | Chip companies | University |

### PCB Design Skill Milestones
1. **Schematic**: place components, draw nets, add power symbols, generate BOM
2. **PCB layout**: import netlist, place components, draw traces, fill copper pour
3. **DRC (Design Rule Check)**: fix spacing violations, clearance errors
4. **Gerber output**: generate files for PCB fabrication (JLCPCB, PCBWay, OSH Park)
5. **4-layer stack-up**: signal – GND – VCC – signal; controlled impedance traces (50 Ω)
6. **High-speed design**: differential pairs, length matching, stitching vias
7. **Power electronics layout**: minimize power loop inductance, Kelvin gate, thermal vias

---

## Category 4: FPGA Design Tools

### Vendor Tools (Both Free)
| Tool | Vendor | FPGAs | Notes |
|------|--------|-------|-------|
| Quartus Prime Lite | Intel/Altera | Cyclone V, MAX 10 | Best for beginners; clean GUI |
| Vivado ML WebPACK | AMD/Xilinx | Artix-7, Spartan-7 | Industry most common; complex but powerful |
| Diamond | Lattice | ECP5, iCE40 | Smaller FPGAs; low power |
| iCEcube2 | Lattice | iCE40 only | Minimal; pair with IceStorm open flow |

### Open-Source FPGA Flow (Fully Open)
- **Yosys**: synthesis (Verilog → gate netlist)
- **nextpnr**: place and route (gates → FPGA fabric)
- **IceStorm**: iCE40 bitstream tools + programmer
- **Project Trellis**: ECP5 open flow
- Supports: Lattice iCE40 and ECP5 families fully

### HDL Simulation Tools
| Tool | Cost | Notes |
|------|------|-------|
| Icarus Verilog | Free | Open-source Verilog simulator; command-line |
| GTKWave | Free | Waveform viewer; opens .vcd files from Icarus |
| ModelSim/Questa | Student free | Industry standard; GUI simulation |
| EDA Playground | Free | Browser-based; no install; multiple simulator backends |
| cocotb | Free | Python-driven testbench framework |
| Verilator | Free | Fast cycle-accurate simulation (C++ output) |

---

## Category 5: Embedded Development Tools

| Tool | MCU Family | Features | Cost |
|------|-----------|---------|------|
| STM32CubeIDE | STM32 (ARM Cortex-M) | HAL codegen, debugger, FreeRTOS | Free |
| TI Code Composer Studio | MSP430/C2000/Tiva | Power EE DSP, C2000 Academy | Free |
| Arduino IDE | AVR, ARM, ESP32 | Beginner-friendly; large library ecosystem | Free |
| PlatformIO (VS Code ext.) | Multi-MCU | Best VS Code integration; 800+ frameworks | Free |
| MPLAB X (Microchip) | PIC, AVR | Automotive/industrial PIC line | Free |
| IAR Embedded Workbench | Multi-MCU | Industry standard; best MISRA-C checker | Paid (student trial) |
| Keil MDK | ARM Cortex-M | Common in automotive/defense | Paid (community free) |

### JTAG / Debug Hardware
| Tool | Price | Notes |
|------|-------|-------|
| ST-Link V3 | ~$10–15 | Built into STM32 Nucleo; standalone available |
| J-Link EDU | ~$60 | Industry standard; works with all ARM MCUs |
| Black Magic Probe | ~$70 | Open-source JTAG; GDB server built-in |
| CMSIS-DAP (generic) | ~$5–30 | USB HID; supported by OpenOCD |

---

## Category 6: Lab Instruments

### Must-Own for Students (< $400 total)
| Instrument | Function | Recommended | Price |
|-----------|---------|------------|-------|
| Digital Multimeter | V, I, R, continuity, diode | UT61E | ~$40 |
| Oscilloscope (2ch) | Waveform visualization, timing | Rigol DS1054Z | ~$300 |
| Bench power supply | Adjustable CC/CV 0–30V | Hanmatek HM305 | ~$50 |
| Function generator | Sine/square/triangle/arbitrary | JOY-iT FY6900 | ~$50 |
| Logic analyzer | UART/SPI/I2C/CAN decode | Saleae Logic 8 clone | ~$10–30 |

### Lab Instrument Skill Milestones
1. **Multimeter**: measure V/I/R, identify shorts, polarity check, diode forward voltage
2. **Oscilloscope**: probe compensation (10× probe calibration), trigger type (edge/pulse/serial), measure Vpp/period/frequency/rise time/phase lag
3. **Power supply**: CC (current-source) vs CV (voltage-source) mode; current limiting as fuse for prototyping; power sequencing for multi-rail boards
4. **Signal generator**: output sine/square/triangle; sweep frequency; AM/FM modulation; set precise amplitude and DC offset
5. **Logic analyzer**: set protocol decoder (UART 115200 8N1, SPI mode 0, I2C); capture and decode frames; verify MCU peripheral output
6. **LCR meter**: measure real L, C, R values vs frequency (compare to datasheet); find self-resonant frequency (SRF) of inductors
7. **Spectrum analyzer**: view harmonics of switching converter; find EMI spurs; measure noise floor; understand dBm, dBc
8. **VNA (advanced)**: S-parameters; Smith chart; impedance matching; antenna measurement

### Oscilloscope Key Skills Cheat Sheet
- **Probe compensation**: attach to CAL output, adjust trimmer until square wave has flat top
- **Trigger**: Edge trigger on rising edge of signal; use Level to set exact threshold
- **Measure**: Press Measure → add Vpp, Period, Frequency, Rise Time
- **Cursor**: Use vertical cursors to measure time difference between two edges (phase)
- **FFT mode**: Press Math → FFT → see frequency content of waveform (spectrum view)
- **Serial decode**: Protocol decode → UART/I2C/SPI → set parameters → see decoded frames

---

## Category 7: Version Control for EE

### Git for Hardware Engineers
**Why EE needs Git**: every schematic revision, firmware version, and simulation run should be tracked. Git provides safety net, collaboration, and portfolio history.

```
repo/
├── firmware/          # All .c, .h, .ld, Makefile files
├── schematics/        # KiCad .kicad_sch, .kicad_pcb (text, diff-able)
├── simulation/        # LTSpice .asc files, Python scripts, NOT .raw files
├── docs/              # Datasheets, application notes (PDF)
├── tests/             # cocotb testbenches, Python test scripts
└── README.md          # What it is, how to build, what you learned
```

### .gitignore Template for EE Projects
```
# LTSpice simulation outputs (too large, regenerate on demand)
*.raw
*.log
*.op.log

# KiCad manufacturing outputs (regenerate from sources)
gerbers/
*.gbr
*.drl
*.xml
fp-info-cache

# FPGA synthesis outputs (regenerate from RTL)
output_files/
*.bit
*.bin
db/
incremental_db/

# MATLAB auto-saves
*.asv

# Python cache
__pycache__/
*.pyc
```

### Git Best Practices for EE
- **Commit schematics frequently**: every functional change (added component, changed net)
- **Never commit**: `.raw` waveform files (can be 100+ MB), compiled bitstreams, binary outputs
- **Branch strategy**: `main` = last known-working hardware; `feature/add-uart` = active work
- **Meaningful commits**: "add overcurrent protection circuit" not "changes"
- **Tag releases**: `v1.0` when first PCB passes bring-up; `v1.1` when bug-fix spin ordered
- **Resource**: AllSpice.io — free Git guide for hardware engineers

---

## Tool Introduction Timeline

```
Day 1    → LTSpice (simulate first voltage divider)
Day 1    → Git + GitHub (init repo, first commit)
Week 1   → Python (variables, loops, functions)
Month 1  → NumPy + Matplotlib (plot LTSpice data in Python)
Month 2  → STM32CubeIDE (first LED blink, then UART)
Month 3  → KiCad (schematic for breadboard circuit)
Month 4  → SciPy (FFT, filter design, Bode)
Month 5  → PyLTSpice (automate parametric sweeps)
Year 2   → MATLAB/Simulink (when coursework requires)
Year 2   → Quartus or Vivado (FPGA track: first Verilog on hardware)
Year 3   → Altium Designer (professional PCB, if industry-bound)
Year 3+  → Cadence Virtuoso (IC design track only)
```

---

## Cross-References
- [[LTSpice Complete Skills Guide]] — deep SPICE simulation reference
- [[Python EE Project Ladder]] — 20-project Python progression with tool integration
- [[Verilog and FPGA Learning Path]] — FPGA tools deep dive
- [[EE Complete Mastery Roadmap]] — full 8-layer progression arc
- [[Python in Electrical Engineering]] — PyVISA, python-control, PyLTSpice details
