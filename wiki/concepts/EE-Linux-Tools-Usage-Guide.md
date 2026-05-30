---
type: concept
title: "EE Linux Tools — Usage Guide (How to Run Each)"
status: developing
created: 2026-05-28
updated: 2026-05-28
tags:
  - electrical-engineering
  - linux
  - linux-mint
  - tools
  - howto
  - cheatsheet
  - open-source
related:
  - "[[EE-Software-on-Linux-Mint]]"
  - "[[EE Software and Lab Tools Complete Stack]]"
  - "[[Python in Electrical Engineering]]"
  - "[[Verilog and FPGA Learning Path]]"
  - "[[LTSpice Complete Skills Guide]]"
---

# EE Linux Tools — Usage Guide (How to Run Each)

What each tool Joe installed on **Linux Mint 22.2** *does* and *how to actually run it*, with a copy-paste "try this" for each. This is the **usage** companion to the **install** page [[EE-Software-on-Linux-Mint]].

> [!tip] Avoid the paste-wrapping trap
> Pasting a multi-line command into the terminal often breaks it across lines and errors out (a `SyntaxError` or `unterminated string`). For anything longer than one line, **put it in a file** with a text editor (`xed myfile.py` on Mint, or the "Text Editor" app), then run the file. Single short commands are fine to type directly.

> [!note] The golden rule for Python tools
> The Python libraries (`control`, `numpy`, `scipy`, `matplotlib`, `PyLTSpice`, `spicelib`, `pyvisa`, `cocotb`) live in the **venv**. Activate it first every session:
> ```bash
> source ~/ee-venv/bin/activate
> ```
> Your prompt shows `(ee-venv)` when it's on. The **system tools** below (ngspice, iverilog, gtkwave, octave, pulseview, wireshark, git) need **no** venv — run them anytime.

---

## Math & system analysis (the MATLAB replacement)

### python-control + NumPy + SciPy + Matplotlib
**What it does:** control-systems and signal analysis in Python — Bode plots, step response, root locus, PID, FFT, filters. The free MATLAB/Simulink stand-in. See [[Python in Electrical Engineering]].

**How to run:** activate the venv, write a `.py` file, run `python3 file.py`.

**Try this — Bode plot of an RC low-pass filter.** Create the file:
```bash
xed ~/rc_bode.py
```
Paste this in, save:
```python
import control
import matplotlib.pyplot as plt

R, C = 1e3, 1e-6                  # 1 kΩ, 1 µF  → cutoff ≈ 159 Hz
H = control.tf([1], [R * C, 1])   # H(s) = 1 / (RC·s + 1)

control.bode_plot(H, dB=True)
plt.savefig("rc_bode.png")        # saves an image you can open
plt.show()                        # opens a plot window
```
Run it:
```bash
source ~/ee-venv/bin/activate
python3 ~/rc_bode.py
```
You get a Bode plot showing the filter rolling off after ~159 Hz. That's your stack working end-to-end.

### GNU Octave
**What it does:** near-drop-in MATLAB clone; runs `.m` scripts and MATLAB syntax. Good when coursework hands you MATLAB code.
**How to run:** launch `octave` in a terminal (or "GNU Octave" from the menu for the GUI).
**Try this** (at the Octave `>>` prompt, one line):
```matlab
t = 0:0.001:1; plot(t, sin(2*pi*5*t)); title("5 Hz sine")
```

---

## Circuit simulation (SPICE)

### ngspice
**What it does:** open-source SPICE — simulates analog circuits from a text "netlist." The native-Linux alternative to LTSpice.
**How to run:** write a `.cir` netlist, then `ngspice file.cir`.
**Try this — RC low-pass AC sweep.** `xed ~/rc.cir`, paste, save:
```spice
* RC low-pass filter
V1 in 0 AC 1
R1 in out 1k
C1 out 0 1u
.ac dec 10 1 100k
.control
run
plot vdb(out)        ; magnitude in dB vs frequency
.endc
.end
```
Run:
```bash
ngspice ~/rc.cir
```
A plot window opens showing the same ~159 Hz roll-off as the Python example above — same circuit, different tool.

> [!note] LTSpice itself isn't installed yet — it needs Wine (see [[EE-Software-on-Linux-Mint]]). `ngspice` covers most coursework natively in the meantime.

---

## Digital / FPGA design (Verilog)

The trio **iverilog → vvp → gtkwave** is your Verilog learning loop: compile, run, view waveforms. See [[Verilog and FPGA Learning Path]].

### Icarus Verilog (`iverilog`) + GTKWave
**What they do:** `iverilog` compiles & simulates Verilog; `vvp` runs the compiled sim; `gtkwave` shows the resulting signals as timing diagrams.

**Try this — a 1-bit blinker.** Two files:

`xed ~/blink.v`:
```verilog
module blink(input clk, output reg led);
  always @(posedge clk) led <= ~led;   // toggle every clock edge
endmodule
```

`xed ~/tb.v` (the testbench — drives the clock, records waves):
```verilog
module tb;
  reg clk = 0;
  wire led;
  blink dut(clk, led);
  initial begin
    $dumpfile("wave.vcd");     // output waveform file
    $dumpvars(0, tb);
    repeat (20) #5 clk = ~clk; // 20 clock toggles
    $finish;
  end
endmodule
```
Compile, run, view (three commands, one at a time):
```bash
iverilog -o sim ~/blink.v ~/tb.v
vvp sim
gtkwave wave.vcd
```
In GTKWave, drag `clk` and `led` from the left panel into the wave window — you'll see `led` toggling at half the clock rate.

### Verilator
**What it does:** the *fast* Verilog simulator — compiles your HDL to C++ for big designs. Overkill for first exercises; reach for it when iverilog gets slow.
**How to run (lint a file as a first taste):**
```bash
verilator --lint-only ~/blink.v
```

### cocotb
**What it does:** write your Verilog **testbench in Python** instead of Verilog — powerful once you know Python well. Needs a small `Makefile` to wire it to iverilog/verilator.
**How to run:** advanced; follow the cocotb quickstart when you reach the FPGA verification stage in [[Verilog and FPGA Learning Path]]. Remember to have the venv active (cocotb lives there).

---

## Lab hardware & instruments

### PyVISA (+ pyvisa-py)
**What it does:** control real bench instruments — oscilloscopes, power supplies, function generators — over USB/LAN using SCPI commands. Needs actual hardware plugged in.
**How to run (list connected instruments):** with the venv active, `python3 -c "import pyvisa; print(pyvisa.ResourceManager('@py').list_resources())"`. Empty `()` just means no instruments are connected yet.

### PulseView (sigrok)
**What it does:** logic-analyzer GUI — capture and decode UART / SPI / I²C from a cheap USB logic analyzer (e.g. a Saleae clone).
**How to run:** launch **PulseView** from the menu, pick your device, set the protocol decoder, hit Run.

### Wireshark
**What it does:** network packet analyzer — inspect Ethernet/IP traffic, debug networked devices/protocols.
**How to run:** launch **Wireshark** from the menu, pick your network interface, start capture. (If it complains about permissions, you were prompted to add your user to the `wireshark` group during install — log out/in once.)

---

## Version control

### Git
**What it does:** tracks every revision of your code, schematics, and simulations — your safety net and portfolio history. See the EE git workflow in [[EE Software and Lab Tools Complete Stack]].
**Try this — start tracking a project:**
```bash
cd ~/my-ee-project
git init
git add .
git commit -m "first commit"
```
One-time identity setup (only needed once, ever):
```bash
git config --global user.name "Joe"
git config --global user.email "joe.43427@gmail.com"
```

---

## One-screen cheat sheet

| Tool | Type | Start it with | Needs venv? |
|---|---|---|---|
| python-control / numpy / scipy / matplotlib | Python lib | `python3 myscript.py` | ✅ yes |
| Octave | app | `octave` | ❌ |
| ngspice | CLI | `ngspice file.cir` | ❌ |
| iverilog + vvp | CLI | `iverilog -o sim *.v` → `vvp sim` | ❌ |
| GTKWave | GUI | `gtkwave wave.vcd` | ❌ |
| Verilator | CLI | `verilator --lint-only file.v` | ❌ |
| cocotb | Python+Make | via Makefile | ✅ yes |
| PyVISA | Python lib | `import pyvisa` | ✅ yes |
| PulseView | GUI | menu → PulseView | ❌ |
| Wireshark | GUI | menu → Wireshark | ❌ |
| Git | CLI | `git init` / `git commit` | ❌ |

> [!gap] Next tools to add (not yet installed)
> **KiCad** (PCB design — `ppa:kicad/kicad-10.0-releases`) and **STM32CubeIDE / Arduino IDE** (embedded) are the obvious next installs — see [[EE-Software-on-Linux-Mint]]. LTSpice via Wine if a course specifically needs it.
