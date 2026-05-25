---
type: concept
title: "EE Complete Mastery Roadmap"
created: 2026-05-25
updated: 2026-05-25
tags:
  - electrical-engineering
  - programming
  - career
  - roadmap
  - mastery
status: developing
---
# EE Complete Mastery Roadmap — Beginner to Master

The complete progression from zero programming experience to professional EE mastery. Organized as 8 compounding layers and 4 career phases. Each layer is a prerequisite for the next.

---

## Layer 1: Math Foundations
**Timeline**: 18–24 months (Year 1–2 in university) | **Cost**: Free (Khan Academy) to university tuition

All EE is applied math. You can't skip or shortcut these.

| Course | Key EE Applications |
|--------|---------------------|
| Calculus 1 | Capacitor i=C·dv/dt; inductor v=L·di/dt; rate-of-change in circuits |
| Calculus 2 | RMS voltage; energy storage (½CV²); Fourier series coefficients |
| Calculus 3 | Maxwell's equations (gradient, divergence, curl); EM fields |
| Differential Equations | RC/RL (1st-order ODE); RLC (2nd-order ODE); Laplace as shortcut |
| Linear Algebra | Nodal/mesh analysis (matrix form); state-space; signal processing |
| Probability & Statistics | Noise floor; Monte Carlo simulation; tolerance yield analysis |

**Free resources**: Khan Academy → MIT OCW → textbook problems

---

## Layer 2: Physics Foundations
**Timeline**: Concurrent with math (Year 1–2)

- **Classical Mechanics** → motor dynamics, MEMS, mechanical-electrical analogies (mass↔inductor, spring↔capacitor, damper↔resistor — same ODE, different labels)
- **Electrostatics** → capacitor physics, electric fields, Coulomb's law
- **Magnetostatics** → inductor physics, Ampere's law, magnetic flux density
- **Electrodynamics** → Faraday's law (WHY transformers work); Lorentz force (WHY motors work)
- **Waves** → RF engineering, antenna radiation, optical fiber

**Best text**: Griffiths "Introduction to Electrodynamics" | **Free**: MIT 8.02 OCW

---

## Layer 3: Core EE Theory Curriculum
**Timeline**: Years 2–4 | **Order is non-negotiable** — skipping layers = pattern-matching without understanding

### 3A. Circuit Theory (First — always)
**Prerequisite**: Calc 1 + algebra | **Textbook**: Nilsson & Riedel "Electric Circuits"

- KVL, KCL, nodal analysis, mesh analysis
- Thevenin/Norton equivalent circuits
- AC analysis: phasors, impedance, complex power
- RLC transient response: natural frequency ωₙ, damping ζ, step response
- Op-amp circuits: inverting/non-inverting, summing, integrator, differentiator
- **Tool**: LTSpice from Day 1 — simulate every concept as you learn it
- **Free**: MIT 6.002 OCW | Khan Academy Circuits | All About Circuits (free textbook)

### 3B. Digital Logic
**Prerequisite**: Some circuit exposure | **Textbook**: Morris Mano "Digital Design"

- Boolean algebra, De Morgan's laws, truth tables
- Karnaugh maps (K-maps), sum-of-products minimization
- Combinational circuits: MUX, decoder, priority encoder, full adder
- Sequential logic: D flip-flop, T flip-flop, shift registers, counters
- Finite State Machines (FSMs): Moore vs Mealy
- Intro Verilog / VHDL
- **Free**: Neso Academy (YouTube — ~100 digital electronics videos) | HDLBits.01xz.net (browser Verilog)

### 3C. Semiconductor Device Physics
**Prerequisite**: Circuit Theory + Physics E&M | **Textbook**: Neamen "Semiconductor Physics and Devices"

- p-n junction: depletion region, I-V curve, built-in potential
- Diode circuit analysis, rectifiers, Zener regulation
- BJT: common-emitter, saturation, cutoff, small-signal model
- MOSFET: triode/saturation regions, threshold voltage, body effect
- Power MOSFET: on-resistance, body diode, switching behavior, gate charge
- SiC vs GaN device physics — gateway to WBG power electronics
- **Free**: MIT 6.012 OCW

### 3D. Signals and Systems
**Prerequisite**: Circuit Theory + Linear Algebra + Diff Eq | **Textbook**: Lathi "Linear Systems and Signals"

- Continuous-time signals: impulse, step, sinusoid, complex exponential
- Convolution: the fundamental operation of LTI systems
- Fourier Series: decompose periodic signals into harmonics
- Fourier Transform: move to frequency domain; see what frequencies are present
- **Laplace Transform**: convert ODE → algebraic equation; H(s) encodes poles/zeros/stability/Bode
- Bode plots: magnitude (dB) and phase (degrees) vs log frequency
- Z-transform: discrete-time equivalent of Laplace (DSP gateway)
- **Free**: MIT 6.003 OCW | Neso Academy Signals playlist
- **This is the most powerful mathematical tool in all of EE** — used identically in circuits, control, DSP, and power electronics

### 3E. Control Systems
**Prerequisite**: Signals & Systems | **Textbook**: Ogata "Modern Control Engineering"

- Transfer functions, block diagrams, feedback loops
- Root locus: how poles move as gain varies → stability
- Bode plots: gain margin (GM), phase margin (PM) → stability metrics
- PID controller design: proportional, integral, derivative action
- State-space representation: x' = Ax + Bu, y = Cx + Du
- Modern control: LQR, Kalman filter (advanced)
- **Free**: MIT 6.302 OCW | Neso Academy Control Systems
- **Job demand**: 69% YoY LinkedIn growth 2025–2026; every power converter has a control loop

### 3F. Electromagnetics
**Prerequisite**: Calc 3 + Physics E&M | **Textbook**: Hayt & Buck "Engineering Electromagnetics"

- Maxwell's equations in differential form (4 equations that explain all EM)
- Electrostatics: Gauss's law for E-field; capacitance from geometry
- Magnetostatics: Ampere's law for H-field; inductance from geometry
- EM induction: Faraday's law — the math of transformer operation
- Plane waves: wave equation, velocity, polarization, skin effect
- Transmission lines: impedance matching, reflection coefficient, standing waves, Smith chart
- Antenna basics: radiation pattern, gain, effective area, Friis equation
- PCB-level EM: power loop inductance, trace impedance, EMI/EMC
- **Free**: MIT 6.007 OCW

---

## Layer 4: Programming for EE
**Timeline**: Start Day 1 — runs parallel to all other layers forever

### Language Priority (Ordered)

**1. Python** — Start immediately
- Month 1–2: Variables, loops, functions, data structures (automatetheboringstuff.com, free)
- Month 2–3: NumPy, Matplotlib — arrays, plotting, basic signal visualization
- Month 3–5: SciPy — FFT, filter design (scipy.signal), ODE solvers (scipy.integrate)
- Month 5–8: python-control — Bode plots, root locus, PID design
- Month 5–8: PyLTSpice — automate LTSpice parameter sweeps from Python
- Month 8–12: PyVISA — control lab instruments (oscilloscopes, power supplies) via SCPI
- See [[Python EE Project Ladder]] — full 20-project progression

**2. Git + GitHub** — Start Month 1, never stop
- Init, commit, push, branch, merge (git-scm.com/book, free)
- GitHub portfolio = your engineering resume for every internship
- Version control for schematics (.kicad_sch), simulation (.asc), firmware (all .c files)

**3. Embedded C** — Start Month 2–3
- Month 2–3: Data types, pointers, structs, bit manipulation, memory-mapped registers (K&R, free)
- Month 3–4: Bare-metal MCU: GPIO, UART, ADC, PWM (Arduino → STM32)
- Month 5–7: Interrupt service routines (ISRs), timers, DMA
- Month 7–10: FreeRTOS: tasks, queues, semaphores, mutex, priority inversion
- Month 10–18: CAN bus, SPI, I2C, I2S — real peripheral integration
- See [[C++ in Electrical Engineering]] for the full C/C++ roadmap

**4. C++** — After solid C foundation (Month 4+)
- OOP: classes, templates, namespaces for embedded code organization
- HAL (Hardware Abstraction Layer) wrappers for STM32
- FreeRTOS with C++ wrapper classes

**5. MATLAB** — When coursework demands it (Year 2)
- Matrix operations, basic scripting
- Signal Processing Toolbox: FFT, filter design, Bode
- Simulink: block-diagram simulation, control loop design + verification
- **Free alternative**: GNU Octave (same syntax, 90% of student needs)

**6. Verilog** — Year 2+ (Track C: FPGA)
- Module declarations, wire/reg, assign statements
- Always blocks: combinational vs sequential
- Testbenches + simulation (Icarus Verilog free, ModelSim student free)
- FSM implementation, parameterized modules, IP cores
- FPGA synthesis: Quartus Lite (Intel) or Vivado ML (AMD) — both free
- See [[Verilog and FPGA Learning Path]] — full FPGA progression

---

## Layer 5: EE Software Tools Stack

| Tool | When to Start | Primary Use | Cost |
|------|--------------|-------------|------|
| LTSpice | Day 1 (Layer 3A) | SPICE simulation, analog/power | Free |
| Python + NumPy | Month 1 | Signal processing, automation | Free |
| Git + GitHub | Month 1 | Version control, portfolio | Free |
| KiCad | Year 2 | PCB schematic + layout | Free |
| MATLAB/Simulink | Year 2 | Signals/control coursework | University |
| STM32CubeIDE | Year 1–2 | STM32 embedded C + debugger | Free |
| Quartus Lite | Year 2 (FPGA) | Intel FPGA synthesis | Free |
| Vivado ML | Year 2 (FPGA) | AMD/Xilinx FPGA synthesis | Free |
| TI Code Composer | Year 2–3 | TI C2000 power electronics | Free |
| Altium Designer | Year 3+ | Professional PCB (industry) | Student free |
| Cadence Virtuoso | Year 3–4 (IC track) | Analog IC schematic/layout | University |

See [[EE Software and Lab Tools Complete Stack]] for full tool reference.

---

## Layer 6: Lab and Hardware Skills
**Timeline**: Year 1–2 | Hardware cost: ~$50–400 total

### Bench Skills Progression
1. **Multimeter** (Week 1): voltage, current, resistance, continuity, diode test
2. **Breadboard circuits** (Week 1–4): LED → voltage divider → RC filter → transistor switch → op-amp buffer
3. **Oscilloscope** (Month 1–3): probe compensation, trigger, measure Vpp/period/frequency/phase/rise time
4. **Power supply** (Month 1+): CC vs CV mode, current limiting, power sequencing
5. **Signal/function generator** (Month 2–4): sine/square/triangle, sweep mode, modulation
6. **Logic analyzer** (Year 2): decode UART/SPI/I2C/CAN frames from MCU in real time
7. **LCR meter** (Year 2): measure actual inductance/capacitance vs frequency (not just datasheet)
8. **Spectrum analyzer** (Year 3, RF track): frequency domain, noise floor, spurious emissions
9. **PCB soldering** (Year 1–2): through-hole first, SMD reflow second (hot air or oven)
10. **PCB bring-up** (Year 2+): power-on sequence, shorts check, oscilloscope-based debug

### Starter Hardware Budget (~$100 total)
| Item | Price |
|------|-------|
| Breadboard + jumper wires | ~$10 |
| Digital multimeter (UT61E or similar) | ~$25 |
| Component kit (resistors/caps/LEDs/transistors) | ~$15 |
| Arduino Uno | ~$20 |
| STM32 Nucleo F446RE (for serious embedded) | ~$15 |

---

## Layer 7: Specialization Tracks
**Timeline**: Year 3+ | Choose one primary, add secondaries later

### Track A — Power Electronics / WBG (Highest Demand Growth)
- **Core skills**: converter topologies (buck/boost/flyback/CLLC/DAB), gate drive design, magnetics design, SiC/GaN device physics, EMI/EMC, thermal management, double pulse test
- **Key tools**: LTSpice + PyLTSpice, TI C2000, KiCad 4-layer PCB, oscilloscope + DPT
- **Key text**: Erickson & Maksimovic "Fundamentals of Power Electronics" (the bible)
- **Salary**: $132k–$230k | Employers: Tesla, ON Semi, Wolfspeed, STMicro, Texas Instruments
- **See also**: [[Silicon Carbide Power Electronics]], [[EE Physical Side — Actionable Skill Plan]]

### Track B — Embedded Firmware (Fastest Time-to-Job-Ready)
- **Core skills**: C + RTOS (FreeRTOS/Zephyr), MCU peripherals (GPIO/UART/SPI/I2C/CAN), bare-metal to HAL, MISRA-C, FSMs
- **Key tools**: STM32CubeIDE, JTAG debugger, logic analyzer, Python for test automation
- **Key texts**: Barr Group "Programming Embedded Systems" | White "Making Embedded Systems"
- **Salary**: $114k–$244k | Employers: automotive, aerospace, defense, medical devices
- **Timeline**: 12–18 months to job-ready with focused effort

### Track C — FPGA / Digital Design
- **Core skills**: Verilog/VHDL, synthesis, timing analysis, AXI bus, cocotb testbenches, DSP on FPGA
- **Key tools**: Quartus Lite or Vivado ML, ModelSim, HDLBits, EDA Playground, cocotb
- **Hardware ladder**: Lattice iCEstick ($25) → Digilent Basys 3 ($150) → Arty A7 ($250)
- **Salary**: $175k avg, $251k+ 90th percentile | Employers: Sandia NL, defense, data centers
- **See also**: [[Verilog and FPGA Learning Path]], [[Digital Logic and Boolean Algebra]]

### Track D — Analog / Mixed-Signal IC Design
- **Core skills**: transistor-level circuit design, op-amp topologies, noise analysis, layout (DRC/LVS), Cadence Virtuoso, SPICE at transistor level
- **Salary**: $191k avg, $349k 90th percentile — highest ceiling in EE
- **Employers**: Apple, NVIDIA, Qualcomm, Texas Instruments, Analog Devices
- **Timeline**: 5–10 years to mastery — hardest and highest-reward EE track
- **Key text**: Razavi "Design of Analog CMOS Integrated Circuits"

### Track E — RF / Wireless Engineering
- **Core skills**: S-parameters, Smith chart, impedance matching, antenna design, RF link budget, noise figure, PA/LNA design
- **Key tools**: ADS (Keysight), HFSS/CST (EM simulation), VNA, spectrum analyzer
- **Salary**: $130k–$180k | Employers: Qualcomm, Apple, defense, telecom
- **Prerequisite**: Strong electromagnetics (Layer 3F) — hardest theory-to-track dependency

### Track F — Control Systems (AI-Adjacent, Fastest Job Growth)
- **Core skills**: PID design, state-space, LQR, Kalman filters, model predictive control, system ID, HIL testing, ROS2
- **Key tools**: MATLAB/Simulink, python-control, ROS2
- **Salary**: $120k–$170k | Employers: automotive (ADAS), robotics, aerospace, energy
- **Demand**: 69% YoY LinkedIn growth 2025–2026; every autonomous system has a control loop

---

## Layer 8: Career Portfolio
**Timeline**: Start Day 1 — portfolio compounds across all 4 years

### GitHub Portfolio Architecture
| Year | What to Push |
|------|-------------|
| Year 1 | Python CLI tools + LTSpice automation scripts + breadboard circuit photos |
| Year 2 | Embedded C on STM32 + Verilog on FPGA + KiCad schematic |
| Year 3 | Full system: MCU + sensor + Python visualization + LTSpice + test data |
| Year 4 | Capstone project (flagship public repo) + internship project (if shareable) |

**Rule**: Every repo needs a README. What it does, what you used, what you learned.

### Progression Milestones by Year
| Year | Milestone |
|------|-----------|
| 1 | Python + Git + LTSpice 10-circuit ladder + breadboard 5 circuits + 3 GitHub repos |
| 2 | MATLAB coursework + STM32 embedded C + KiCad PCB + Verilog on FPGA + first internship app |
| 3 | Specialization track chosen + internship completed + advanced simulation project + IEEE active |
| 4 | Capstone flagship project + MS applications or FTE search + 10+ GitHub repos |

### Professional Affiliations
- **IEEE student membership** (~$32/year): Collabratec mentorship, job board, conferences
- **Research** (FURI equivalent): faculty mentorship + research output = MS application differentiator
- **Conferences by track**: APEC (power electronics), DAC (chip design), ISSCC (IC), FPL (FPGA)

---

## Fastest Path to Job-Ready
If you need a job ASAP and can only focus on one path:

**Python + Git + Embedded C + STM32 + FreeRTOS = 12–18 months → $114k–$244k**

1. Month 1–2: Python basics + Git (automatetheboringstuff.com)
2. Month 2–3: C fundamentals — K&R, pointers, bit manipulation
3. Month 3–6: Arduino → STM32 Nucleo (STM32CubeIDE, free) — GPIO, UART, ADC, PWM
4. Month 6–9: FreeRTOS — tasks, queues, semaphores
5. Month 9–12: CAN bus + real I2C/SPI sensor integration
6. Month 12–18: Open-source contribution or full GitHub system project (MCU + Python UI)

---

## Common Mistakes That Kill Progress

1. **Skipping math**: Linear algebra and differential equations are non-negotiable. They are the EE.
2. **Jumping to specialization too early**: Signals → Control → Power is a real dependency chain.
3. **Tutorial hell**: Stop watching, start building. Real projects beat 100 hours of videos.
4. **Ignoring Git from Day 1**: Version control is a career-multiplying habit, not an advanced topic.
5. **Treating LTSpice as optional**: Simulate every circuit you study. Theory without simulation = 3× slower learning.
6. **MATLAB before Python**: Python is more versatile and career-transferable. MATLAB is the second tool.
7. **Only theoretical study**: Physical debugging intuition is irreplaceable — handle real hardware early.
8. **Specializing in everything**: One deep primary track beats shallow knowledge in five.

---

## Cross-References
- [[EE Topic Depth Priority Map]] — 6-level leverage stack ordered by EE dependency
- [[Python EE Project Ladder]] — 20 progressively harder Python+EE projects
- [[LTSpice Complete Skills Guide]] — 10-circuit ladder with all SPICE directives
- [[ASU EE Year 1-2 Curriculum Map]] — ASU-specific course sequence
- [[EE Physical Side — Actionable Skill Plan]] — 18-month WBG power electronics plan
- [[Verilog and FPGA Learning Path]] — FPGA track deep dive
- [[EE Software and Lab Tools Complete Stack]] — full simulation/PCB/lab tool reference
- [[Research - Programmer to EE Master Complete Guide]] — source page for this content
