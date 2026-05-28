---
type: synthesis
title: "Research: EE Software on Linux Mint"
created: 2026-05-28
updated: 2026-05-28
tags:
  - research
  - electrical-engineering
  - linux-mint
  - software
  - eda
  - fpga
status: developing
related:
  - "[[EE-Software-on-Linux-Mint]]"
  - "[[EE Software and Lab Tools Complete Stack]]"
  - "[[Linux-Software-Alternatives]]"
  - "[[Linux-Mint-Fresh-Install-Essential-Apps]]"
sources:
  - "[[KiCad-Official-Linux-Install]]"
---

# Research: EE Software on Linux Mint

## Overview
Follow-up to "best apps for EE" given Joe just installed Linux Mint. The wiki already had a thorough platform-agnostic [[EE Software and Lab Tools Complete Stack]], but it barely addressed Linux. This research fills that gap: which EE tools run **natively** on Mint vs need a workaround, with current (2026) install commands. Bottom line — Linux is a strong EE platform; KiCad, the Python stack, the HDL toolchain, and the vendor IDEs (STM32CubeIDE, Vivado, Quartus) are all native. The lone real gap is **LTSpice** (Wine only).

Output: one Mint-specific install guide ([[EE-Software-on-Linux-Mint]]) that complements the existing stack page.

## Key Findings
- **KiCad's primary platform is Linux**; current stable is **KiCad 10** via `ppa:kicad/kicad-10.0-releases`. (Source: [[KiCad-Official-Linux-Install]]) *(high)*
- **LMDE (Debian Mint) breaks the KiCad PPA** — those users must use Flatpak. Ubuntu-based Mint works. (Source: [[KiCad-Official-Linux-Install]]) *(high)*
- **LTSpice has no native Linux build** — runs under Wine (with quirks) or via dual-boot. Still the best free analog/power simulator. *(high)*
- **QSPICE** (Qorvo, the LTSpice "successor" by the same author) is **Windows-only and does not run under Wine** — a dead end on Linux. *(high)*
- Native Linux SPICE options: **ngspice**, **KiCad+ngspice** (integrated), **Qucs-S** (RF/S-params), **Xyce** (Sandia, parallel). *(high)*
- **Vivado (AMD/Xilinx)** and **Quartus Prime Lite (Intel/Altera)** both have **native Linux installers** — no dual-boot needed for FPGA work. Vivado is ~70–120 GB; Quartus must **not** be installed as root. *(high)*
- **STM32CubeIDE, Arduino IDE, PlatformIO, Icarus Verilog, GTKWave, Verilator, cocotb, GNU Octave, Python/SciPy, Wireshark** — all native. *(high)*
- Two Linux-specific gotchas worth a one-time fix on a fresh box: add user to **`dialout`** group for serial-port access; large vendor FPGA tools want lots of disk. *(high)*

## Key Concepts
- [[EE-Software-on-Linux-Mint]]: the new Mint install guide (native-vs-Wine table + copy-paste day-one setup).
- [[EE Software and Lab Tools Complete Stack]]: the full platform-agnostic tool reference (existing).
- [[Linux-Software-Alternatives]]: Windows→Linux app mapping incl. an EE-specific table (existing).

## Contradictions
- A search snippet implied KiCad 9.0 (Feb 2025) was current; the **official KiCad page shows 10.0** as the current stable PPA. Resolved in favor of the primary source: **KiCad 10**. (Source: [[KiCad-Official-Linux-Install]])
- The existing [[Linux-Software-Alternatives]] EE table says only "LTSpice via Wine" as the SPICE story — accurate but incomplete; the native **KiCad+ngspice / Xyce** path and the **QSPICE-won't-run** caveat are new additions here.

## Open Questions
- Which Mint edition is Joe on — standard (Ubuntu-based) or LMDE? Determines KiCad install path (PPA vs Flatpak).
- Does Joe have a Windows dual-boot for LTSpice-specific coursework, or should he commit to KiCad+ngspice natively?
- Which FPGA board (if any) will his ASU coursework use — that decides Vivado vs Quartus vs open iCE40 flow before the multi-GB download.
- MATLAB: confirm ASU provides the student license (native Linux installer exists either way).

## Sources
- [[KiCad-Official-Linux-Install]]: KiCad project — official Linux/Mint install docs (primary source)
- Supporting (not filed as pages): KiCad.org Flatpak page; ngspice/Qucs-S/Xyce comparison discussions; AMD & Intel FPGA Linux installer docs; ST STM32CubeIDE Linux install guide.
