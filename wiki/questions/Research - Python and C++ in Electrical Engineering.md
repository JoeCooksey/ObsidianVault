---
type: research
title: "Research - Python and C++ in Electrical Engineering"
status: developing
created: 2026-04-24
updated: 2026-04-24
tags:
  - electrical-engineering
  - python
  - cpp
  - embedded-systems
  - programming
  - self-teaching
  - roadmap
---

# Research — Python and C++ in Electrical Engineering

**Research question**: How do Python and C++ relate to the physical side of electrical engineering, and what is the full roadmap to self-teach both for an EE student?

---

## Key Finding 1 — The Two Languages Serve Completely Different Roles

Python and C++ are not competitors in EE — they are a **two-layer stack**:

| Layer | Language | Domain |
|-------|----------|--------|
| Analysis / automation | Python | Simulation, data, instruments, control design |
| Real-time / embedded | C/C++ | Firmware, DSP, motor control, safety-critical |

The canonical physical-EE workflow: **design in Python → validate in LTSpice → implement in C++ on a microcontroller**. A power converter engineer uses Python to design and verify the PI control algorithm offline, then ports that same math to C running at 100 kHz on a TI C2000 DSP.

---

## Key Finding 2 — Python Owns the Test Lab

The single biggest physical-EE use of Python is **automated test equipment (ATE) control** via PyVISA. Every piece of bench equipment — oscilloscope, power supply, LCR meter, function generator, impedance analyzer — can be controlled programmatically over GPIB, USB, or LAN using SCPI commands.

Real workflow:
```python
import pyvisa
rm = pyvisa.ResourceManager()
psu = rm.open_resource('GPIB0::5::INSTR')
psu.write('VOLT 12')       # Set output to 12 V
v = float(psu.query('MEAS:VOLT?'))  # Read back measured voltage
```

Instrument brands with native Python APIs: Keysight (keysight-pyvisa), Tektronix (tm_devices), Rohde & Schwarz (RsInstrument). Every professional EE lab runs Python scripts to run characterization sweeps instead of doing them by hand — frequency sweeps, load steps, thermal cycling, efficiency maps.

---

## Key Finding 3 — Python Replaces MATLAB for Control Systems Design

The **python-control** library (pip install control) is a direct MATLAB Control Toolbox equivalent:

```python
import control
G = control.tf([1], [1, 2, 1])   # Transfer function 1/(s²+2s+1)
control.bode(G)                   # Bode plot
control.rlocus(G)                  # Root locus
T = control.feedback(G, 1)        # Closed-loop TF
control.step_response(T)          # Step response
```

This is how you design PI/PID controllers for power converters in Python. **SciPy.signal** adds FIR/IIR filter design, FFT, and state-space representation. Together they cover 90% of what MATLAB does in signals and control, for free.

---

## Key Finding 4 — C++ (and C) Runs Every Power Converter's Brain

Every digital power converter — EV traction inverter, DC-DC converter, motor drive — has a DSP or MCU running a control loop in C. The **TI C2000 F28379D** is the industry-standard automotive/industrial power DSP. It runs:

- **PI current control** at 10–100 kHz update rates
- **SVPWM** (Space Vector PWM) generation
- **Dead time compensation**
- **Overcurrent protection** (hardware interrupt → software response < 100 ns)
- **CAN bus communication** to the vehicle BMS/VCM

Fixed-point arithmetic is often required because C2000 historically lacked floating-point performance. Knowing how to implement a PI loop in fixed-point C is a direct hiring signal for power electronics roles.

Example C firmware loop structure:
```c
__interrupt void epwm1_isr(void) {
    adc_raw = AdcaResultRegs.ADCRESULT0;
    error = setpoint - adc_raw;
    integral += Ki * error;
    output = Kp * error + integral;
    EPwm1Regs.CMPA.bit.CMPA = (uint16_t)output;
    EALLOW;
    AdcaRegs.ADCINTFLGCLR.bit.ADCINT1 = 1;
    PieCtrlRegs.PIEACK.all = PIEACK_GROUP3;
    EDIS;
}
```

---

## Key Finding 5 — Python Scripts the Physical EE Toolchain

Python sits above and around every EE tool:

| Tool | Python integration |
|------|-------------------|
| LTSpice | PyLTSpice: run simulations programmatically, sweep parameters, extract waveforms |
| KiCad | Built-in Python scripting API — automate footprint placement, generate BOM |
| Altium | Python scripting via COM interface |
| ANSYS / COMSOL | Python API for parametric simulation runs |
| Oscilloscopes | PyVISA SCPI control; Tektronix TekScope Python library |
| Vivado (FPGA) | Tcl/Python scripting for synthesis automation |
| FPGA verification | cocotb: write RTL testbenches in Python instead of VHDL/Verilog |

The pattern: Python automates the things humans do repetitively. Instead of manually changing one component value in LTSpice 50 times, a PyLTSpice loop does it in 30 seconds and exports a clean Matplotlib plot.

---

## Key Finding 6 — C/C++ Is Required for Safety-Critical EE

**MISRA-C** (Motor Industry Software Reliability Association) is the coding standard for automotive, aerospace, and industrial-grade embedded C. ISO 26262 (functional safety for automotive) mandates MISRA-C compliance. Key rules:
- No dynamic memory allocation (no malloc/free)
- No recursive functions
- All variables initialized before use
- No unreachable code

This is why automotive firmware is C, not Python, not C++. High-integrity embedded systems (ABS, airbags, EV inverter control) must be MISRA-C compliant. Knowing even the basics of MISRA puts you ahead at internship interviews for automotive EE roles.

---

## Key Finding 7 — Python + C++: Language Handoff Pattern

The most important professional pattern to understand: **algorithm prototype → embedded deployment**.

1. **Python**: Write a control algorithm (e.g., adaptive dead-time compensation for a SiC inverter). Simulate with scipy/control. Validate with synthetic data.
2. **C-translation**: Manually port the algorithm to C. Replace floating-point with fixed-point if needed. Replace numpy arrays with C arrays or DSP library calls (ARM CMSIS-DSP).
3. **Hardware-in-the-loop (HIL)**: Run the C code on the real MCU, feeding it signals from a Python-controlled simulation environment.

Tools that bridge the gap:
- **MATLAB Coder**: converts MATLAB/Python algorithm to C automatically (paid, industry-standard)
- **Cython**: converts Python to C extension (open source)
- **ARM CMSIS-DSP**: pre-optimized C library for FFT, FIR/IIR, PID — implements the same math Python does, in C, on ARM Cortex-M

---

## Key Finding 8 — Salary and Career Impact

From existing wiki research + 2026 market data:

- **EE + Python/AI**: 20–30% salary premium vs. EE alone (already confirmed in [[High Income Skills Tier List]])
- **Embedded Firmware/C++**: $114k–$244k entry-to-senior range; one of the most consistent A-tier EE tracks
- **Test automation engineer** (Python-heavy): $90–130k entry; Tesla, Apple, Qualcomm, National Instruments hire heavily
- **Python in power electronics**: Wolfspeed, Onsemi, Infineon, Texas Instruments all post Python + C/C++ as primary skills for power applications roles
- **Specific signal**: job postings for SiC/GaN application engineers list Python (LTSpice automation, device characterization scripting) + C (embedded gate driver/DSP firmware) as the exact skill pair

**For Joe specifically**: Python Phase 1 is already in the Year 1 action plan. C++ deepens via Arduino (Year 1–2) → STM32 (Year 2) → TI C2000 (Year 3+). This pairs directly with the [[EE Physical Side — Actionable Skill Plan]] 18-month plan.

---

## Open Questions

1. Should Joe prioritize Python-Control (control design in Python) or go straight to MATLAB via ASU license?
2. At what ASU course does FreeRTOS or RTOS appear? (EEE 488 Embedded Systems, or independent study?)
3. Is TI C2000 Academy still the best free resource for digital power control in 2026?
4. What is the best way to practice PyVISA without owning bench equipment? (Virtual instruments? Keysight PathWave free trial?)
5. Does cocotb skill translate to LLNL/Sandia hiring criteria, or is VHDL/Verilog + Python secondary?

---

## Related Pages
- [[Python in Electrical Engineering]]
- [[C++ in Electrical Engineering]]
- [[Python Self-Teaching Roadmap for EE]]
- [[C++ Self-Teaching Roadmap for EE]]
- [[EE Freshman Action Plans]]
- [[EE Physical Side — Actionable Skill Plan]]
- [[EE Freshman Self-Study Stack]]
- [[High Income Skills Tier List]]
- [[Research - First-Year ASU EE Skills]]
- [[LTSpice Complete Skills Guide]]
