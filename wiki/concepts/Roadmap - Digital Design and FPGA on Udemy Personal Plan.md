---
type: concept
title: "Roadmap - Digital Design and FPGA on Udemy Personal Plan"
created: 2026-07-27
updated: 2026-07-27
tags:
  - concept
  - domain/engineering
  - roadmap
  - fpga
  - vlsi
  - udemy
status: developing
complexity: advanced
domain: engineering
aliases: ["Udemy FPGA roadmap", "VHDL roadmap", "VLSI roadmap Udemy"]
related:
  - "[[Udemy Personal Plan EE Coverage Map]]"
  - "[[Research - Udemy Personal Plan Course Roadmaps for an EE Career]]"
  - "[[Research - High Income Skills Tier List]]"
sources:
  - "[[Udemy Catalog Audit — EE Topics, Premium Badge Method (July 2026)]]"
---

# Roadmap - Digital Design and FPGA on Udemy Personal Plan

**Total: ~40 hours.** The weakest of the hardware tracks — only 6 of the top 17 FPGA courses are in the plan. Include it in a subscription window only if FPGA is a deliberate career target rather than curiosity.

## The constraint that shapes this roadmap

The in-plan FPGA courses are **VHDL on Intel/Altera**. The excluded ones are the Verilog and Xilinx/Vivado courses — including `FPGA Embedded Design, Part 1 – Verilog` (4.5, 1,140 reviews), the most-reviewed FPGA course on the platform.

This matters because **US industry — and particularly the national labs and defense-adjacent employers around Livermore — skews Xilinx/AMD and Verilog/SystemVerilog.** The plan teaches the other dialect.

The concepts transfer (RTL is RTL, and a VHDL engineer picks up Verilog in a couple of weeks), but if the goal is an FPGA internship at [[Lawrence Livermore National Laboratory|LLNL]] or Sandia, this track is a compromise. Buying the Verilog course outright for $15–20 on sale may simply be the better move.

## The ladder

**Stage 1 — HDL and synthesis (25.5 h)**
`Learn FPGA Design With VHDL (Intel/Altera)` ✅ 4.4 (663)
The only substantial in-plan entry point. Combinational and sequential logic, FSMs, testbenches, full toolchain to a programmed device.

**Stage 2 — Reinforcement (15 h, optional)**
`Learn VHDL and FPGA Development` ✅ 4.5 (118) — a second pass through the same material with a different instructor. Take it only if Stage 1 didn't land.

**Stage 3 — High-level synthesis (17.5 h)**
`High-Level Synthesis for FPGA, Part 1 – Combinational` ✅ 4.6 (568) 8h → `Part 2 – Sequential` ✅ 4.6 (187) 9.5h
C-to-RTL. Increasingly how accelerator work is actually done, and a differentiator most undergraduates don't have.

**Stage 4 — Verification, if the target is ASIC/industry (11 h)**
`Verification Series Part 3: UVM Essentials` ✅ 4.6 (1,816)
Verification is where most digital-design headcount actually is, and UVM is its language. Note the plan includes Part 3 and Part 5 but not the earlier parts — a broken sequence you'd have to fill in elsewhere.

## VLSI / ASIC side (partial coverage)

✅ `VSD – Physical Design Flow` 4.2 (3,497) 6.5h · ✅ `UPF Power Aware Design & Verification` 4.4 (1,493) · ✅ `Mastering Digital VLSI/ASIC/Verilog Interview Questions` 4.3 (426)
❌ `Complete ASIC Design Flow: Idea to Silicon` (4.6, 45.5h) · ❌ the VSD custom-layout and SPICE-simulation courses

So: **verification and DFT are in; physical design and custom layout are mostly out.**

## Hardware

A **Terasic DE10-Lite or similar Intel/Altera board** (~$85–100) matches the in-plan courses. If you already own a Xilinx board, that argues for buying the Verilog course instead and skipping this roadmap entirely.

## The artifact

A synthesized design running on real hardware with a testbench in the repo — UART transceiver, VGA/HDMI signal generator, or a small pipelined processor. Simulation-only FPGA work is much weaker evidence than a board doing something visible.

> [!important] Priority verdict: **fourth of five tracks.** FPGA is a legitimately high-income skill ([[Research - High Income Skills Tier List]]), but this is the one track where the Personal Plan is a worse deal than a $15 targeted purchase.
