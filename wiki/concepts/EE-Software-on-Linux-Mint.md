---
type: concept
title: "EE Software on Linux Mint — Install Guide"
status: developing
created: 2026-05-28
updated: 2026-05-28
tags:
  - electrical-engineering
  - linux
  - linux-mint
  - software
  - eda
  - simulation
  - fpga
  - open-source
related:
  - "[[EE-Linux-Tools-Usage-Guide]]"
  - "[[EE Software and Lab Tools Complete Stack]]"
  - "[[Linux-Software-Alternatives]]"
  - "[[Linux-Mint-Fresh-Install-Essential-Apps]]"
  - "[[LTSpice Complete Skills Guide]]"
  - "[[Verilog and FPGA Learning Path]]"
---

# EE Software on Linux Mint — Install Guide

What to actually install for electrical-engineering work on a fresh **Linux Mint** box, and which tools run natively vs need a workaround. This is the Mint-specific companion to the platform-agnostic [[EE Software and Lab Tools Complete Stack]]. For the broad Windows→Linux mapping, see [[Linux-Software-Alternatives]].

➡️ **Already installed the stack? See [[EE-Linux-Tools-Usage-Guide]]** for how to *run* each tool, with copy-paste "try this" examples.

> [!tip] Headline: Linux is *good* for EE
> KiCad, the Python/SciPy stack, the FPGA HDL toolchain, and the major vendor IDEs (STM32CubeIDE, Vivado, Quartus) all run natively on Linux. The one real gap is **LTSpice**, which still needs Wine. (Source: [[Research - EE Software on Linux Mint]])

---

## Native vs workaround — the at-a-glance table

| Tool | Category | Mint status (2026) | Install |
|---|---|---|---|
| **KiCad 10** | PCB / EDA | Native ✅ (primary platform) | Official PPA |
| **ngspice** | SPICE sim | Native ✅ | `apt` |
| **KiCad + ngspice** | SPICE in-EDA | Native ✅ | bundled with KiCad |
| **Qucs-S / Xyce** | SPICE sim | Native ✅ | apt / download |
| **LTSpice** | SPICE sim | ⚠️ Wine only (no native build) | Wine / dual-boot |
| **QSPICE** | SPICE sim | ❌ Windows-only, **won't run under Wine** | dual-boot only |
| **Python + NumPy/SciPy/Matplotlib** | system sim | Native ✅ | `apt` / pip |
| **GNU Octave** | MATLAB alt | Native ✅ | `apt` |
| **MATLAB / Simulink** | system sim | Native ✅ (paid; ASU license) | MathWorks installer |
| **Icarus Verilog + GTKWave** | HDL sim | Native ✅ | `apt` |
| **Verilator / cocotb** | HDL sim | Native ✅ | apt / pip |
| **Vivado (AMD/Xilinx)** | FPGA | Native ✅ (~70–120 GB) | AMD installer |
| **Quartus Prime Lite (Intel/Altera)** | FPGA | Native ✅ | Intel installer (don't run as root) |
| **STM32CubeIDE** | embedded | Native ✅ | `.deb` / run script |
| **Arduino IDE / PlatformIO** | embedded | Native ✅ | apt / Flatpak / VS Code ext |
| **KiCad / VS Code / Git / Wireshark** | tooling | Native ✅ | apt / PPA |

(Source: [[Research - EE Software on Linux Mint]]) *(high)*

---

## SPICE / circuit simulation

The one category where Linux is weaker than Windows. (Source: [[Research - EE Software on Linux Mint]])

- **LTSpice** — no native Linux build. Runs under **Wine** (functional with some quirks), or dual-boot into Windows for simulation-critical work. Still the strongest free analog/power simulator — see [[LTSpice Complete Skills Guide]]. *(high)*
- **QSPICE** — the Qorvo "LTSpice successor" by the same author (Mike Engelhardt). **Windows-only and does not run under Wine** despite attempts. Don't chase it on Linux. *(high)*
- **ngspice** — open-source, native, cross-platform; speed comparable to commercial. Some LTSpice `.lib` models won't load. `sudo apt install ngspice`. *(high)*
- **KiCad + ngspice** — KiCad bundles an integrated ngspice workflow: simulate the schematic before laying out the board, no tool-switching. Best Linux-native path for "simulate then PCB." *(high)*
- **Qucs-S** — GUI front-end over ngspice/Xyce; adds S-parameter / RF analysis. UI is dated but loved in academia. *(medium)*
- **Xyce** — Sandia's parallel SPICE; native on Linux/Windows/macOS; good for large circuits. *(medium)*

> [!tip] Practical SPICE plan for Joe
> Keep using **LTSpice** (via Wine, or in your Windows dual-boot) for coursework that follows LTSpice tutorials, and adopt **KiCad + ngspice** natively as you move toward PCB projects. Drive both from Python via **PyLTSpice / spicelib** (see [[Python in Electrical Engineering]]).

---

## PCB / EDA — KiCad (install this first)

KiCad's primary development platform *is* Linux. Current stable is **KiCad 10** (the line moved 9.0 → 10.0; 9.0 from Feb 2025 is the prior LTS-ish release). (Source: [[KiCad-Official-Linux-Install]])

```bash
sudo add-apt-repository --yes ppa:kicad/kicad-10.0-releases
sudo apt update
sudo apt install --install-recommends kicad
```

> [!warning] Mint flavor caveat
> The PPA works on **Ubuntu-based** Linux Mint (the normal edition). **LMDE (Linux Mint Debian Edition) does NOT work with the PPA** — use the **Flatpak** (`flathub org.kicad.KiCad`) there instead. Mint itself is "not officially supported" by KiCad but is reported working via the Ubuntu PPA. (Source: [[KiCad-Official-Linux-Install]])

Flatpak alternative (distro-agnostic, bundles libraries + 3D models + docs): install from the Software Manager (enable Flathub) or `flatpak install flathub org.kicad.KiCad`.

---

## System-level simulation (MATLAB replacement)

- **Python stack** — `sudo apt install python3-numpy python3-scipy python3-matplotlib`, then `pip install --user control PyLTSpice spicelib pyvisa`. Native, free, and the backbone of [[Python EE Project Ladder]].
- **GNU Octave** — `sudo apt install octave`; ~90% MATLAB-compatible for scripting.
- **MATLAB / Simulink** — native Linux installer; use the **ASU student license** when coursework requires it. (See [[ASU EE Year 1-2 Curriculum Map]].)

---

## FPGA / HDL — all native on Linux

Both big-vendor suites have native Linux installers — many students don't realize this and needlessly dual-boot. (Source: [[Research - EE Software on Linux Mint]])

- **Open flow (start here)**: `sudo apt install iverilog gtkwave verilator`. Icarus Verilog + GTKWave covers HDLBits-style learning with zero vendor bloat. Add `cocotb` (in your venv — see PEP 668 note below) for Python testbenches. See [[Verilog and FPGA Learning Path]].
- **Vivado (AMD/Xilinx)** — native Linux self-extracting installer; **70–120 GB** install (2024/2025 builds ~83 GB). For Artix-7 / Spartan-7 boards.
- **Quartus Prime Lite (Intel/Altera)** — native Linux; **do not run the installer as root**. For Cyclone V / MAX 10.
- **Fully-open ASIC/FPGA flow**: Yosys + nextpnr + IceStorm (iCE40) / Project Trellis (ECP5) — all apt-installable, all native.

---

## Embedded development — native

- **STM32CubeIDE** — download from ST; Debian-based install via the provided script (`sudo sh ./st-stm32cubeide_*.sh`) or `.deb`. Native debugger + HAL codegen + FreeRTOS.
- **Arduino IDE** — Software Manager / Flatpak / AppImage. Add your user to the `dialout` group for serial port access: `sudo usermod -aG dialout $USER` (log out/in after).
- **PlatformIO** — VS Code extension; best multi-MCU workflow.
- **JTAG/debug**: `sudo apt install openocd gdb-multiarch` for ST-Link / CMSIS-DAP / Black Magic Probe.

> [!note] Serial-port permissions
> The single most common Linux embedded gotcha: you can't open `/dev/ttyUSB0` / `/dev/ttyACM0` until your user is in the `dialout` group. Do this once on a fresh Mint install.

---

## Lab-instrument control

- **PyVISA** + a backend (`pyvisa pyvisa-py`, installed in your venv — see PEP 668 note) drives oscilloscopes/PSUs/function-gens over USB/LAN via SCPI — native on Linux, no NI drivers needed for `pyvisa-py`.
- **Sigrok / PulseView** — `sudo apt install pulseview`; open-source logic-analyzer software (works with Saleae clones and many cheap analyzers).
- **Wireshark** — native, for any networking/protocol work.

---

## Day-one EE setup on Mint (copy-paste order)

1. `sudo apt install python3-numpy python3-scipy python3-matplotlib octave ngspice iverilog gtkwave verilator pulseview wireshark git python3-full` (the apt-provided NumPy/SciPy/Matplotlib are the optimized builds — install them here, not via pip)
2. Make a project venv for the pure-Python extras (see callout below), then inside it: `pip install control PyLTSpice spicelib pyvisa pyvisa-py cocotb`
3. KiCad: add the `ppa:kicad/kicad-10.0-releases` PPA (or Flatpak on LMDE).
4. `sudo usermod -aG dialout $USER` then log out/in (serial access).
5. STM32CubeIDE + Arduino IDE from vendor / Software Manager as needed.
6. LTSpice via Wine (or use your Windows dual-boot) for LTSpice-specific coursework.
7. Vivado/Quartus only when the FPGA track needs real hardware (large downloads).

> [!warning] PEP 668 — `pip install` is blocked system-wide on Mint 22.x
> Ubuntu 24.04 (Mint 22.x base) marks the system Python "externally managed": a bare `pip install` or `pip install --user` fails with `error: externally-managed-environment`. **Use a virtual environment.** Because the heavy compiled libs are installed via apt, create the venv with `--system-site-packages` so it reuses them and pip only adds the pure-Python extras:
> ```bash
> python3 -m venv --system-site-packages ~/ee-venv
> source ~/ee-venv/bin/activate          # run this each session (or add to ~/.bashrc)
> pip install control PyLTSpice spicelib pyvisa pyvisa-py cocotb
> ```
> Do **not** use `pip install --break-system-packages` — it risks corrupting system tools that depend on the system Python. `cocotb` and lab scripts must be run with the venv active.

> [!gap] Verify against your Mint version
> Confirmed working on **Linux Mint 22.2 "Zena" (Ubuntu 24.04 "Noble" base)** — standard Ubuntu-based edition, so the KiCad PPA path applies (not Flatpak). Vivado/Quartus exact versions and disk needs change per release — check vendor pages before the multi-GB download. LMDE users: prefer Flatpak/AppImage over PPAs throughout.
