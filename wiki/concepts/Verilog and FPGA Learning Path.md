---
type: concept
title: "Verilog and FPGA Learning Path"
created: 2026-05-25
updated: 2026-05-25
tags:
  - verilog
  - fpga
  - digital-design
  - hardware-description-language
  - electrical-engineering
status: developing
---
# Verilog and FPGA Learning Path

Complete beginner-to-advanced progression for hardware description language (HDL) and FPGA engineering. This is Track C in [[EE Complete Mastery Roadmap]].

**Salary target**: $175k avg, $251k+ 90th percentile (2026)
**Time to job-ready**: 2–4 years from first Verilog line

---

## Prerequisites (Non-Negotiable)
- [[Digital Logic and Boolean Algebra]] — Boolean algebra, K-maps, D flip-flops, FSMs
- Basic programming experience (Python or C ideal — control flow, loops, functions)
- Circuit Theory basics (what a clock signal is, voltage levels, propagation delay)

---

## Phase 0: Digital Logic Foundation
**Duration**: 4–8 weeks | **Cost**: Free | **Tool**: None yet — paper + YouTube

Master these concepts before writing a single line of Verilog:
- Boolean algebra: AND, OR, NOT, XOR, XNOR truth tables
- De Morgan's laws: NOT(A AND B) = NOT(A) OR NOT(B)
- Combinational circuits: MUX, decoder, full adder, comparator
- Sequential circuits: SR latch, D flip-flop, T flip-flop, JK flip-flop
- Synchronous vs asynchronous reset (synchronous preferred in synthesis)
- Setup time, hold time, clock-to-Q delay (timing constraints)
- Finite State Machines: Moore (output = f(state)) vs Mealy (output = f(state, input))

**Resource**: Neso Academy "Digital Electronics" playlist (YouTube, free, ~120 videos)

---

## Phase 1: Verilog Fundamentals
**Duration**: 6–10 weeks | **Tool**: HDLBits.01xz.net (browser, no install needed)

HDLBits gives instant simulation feedback. Work every problem in order.

### Core Verilog Syntax

```verilog
// Module structure
module counter #(parameter WIDTH = 8) (
    input  wire             clk,
    input  wire             rst_n,   // active-low reset
    output reg  [WIDTH-1:0] count
);
    always @(posedge clk or negedge rst_n) begin
        if (!rst_n)
            count <= {WIDTH{1'b0}};
        else
            count <= count + 1;
    end
endmodule
```

### Concepts to Master in Phase 1
| Concept | Common Mistake |
|---------|---------------|
| `wire` vs `reg` | `reg` does NOT mean a hardware register — it's just a variable |
| `assign` (combinational) | Only drives `wire`; right side evaluated continuously |
| `always @(posedge clk)` (sequential) | Use non-blocking `<=` inside sequential always blocks |
| Blocking `=` vs non-blocking `<=` | **Biggest beginner mistake**: use `=` in combinational, `<=` in sequential |
| `parameter` and `localparam` | Make modules reusable (data width, FIFO depth) |
| `generate` blocks | Replicate hardware structures without copy-pasting |
| Concatenation `{a, b}` | Join signals; `{4{a}}` replicates a 4 times |
| Signed vs unsigned | `$signed()` cast needed for signed arithmetic |

### HDLBits Progression Order
1. Getting Started (just submit a module)
2. Basics: wires, inverters, AND/OR gates
3. Vectors: multi-bit wires, indexing, concatenation
4. Modules: hierarchical design, port connections
5. Procedures: always blocks, if/case statements
6. More Features: for loops, generate, parameter
7. Circuits — Combinational: MUX, decoder, adder, shifter
8. Circuits — Sequential: D flip-flop, counter, shift register
9. Building Larger Circuits: FSMs, serial protocols

---

## Phase 2: Testbenches and Simulation
**Duration**: 3–5 weeks | **Tools**: Icarus Verilog (free) + GTKWave (free)

A testbench is a non-synthesizable Verilog file that generates inputs and checks outputs.

```verilog
`timescale 1ns/1ps
module tb_counter;
    reg clk = 0;
    reg rst_n;
    wire [7:0] count;

    // Instantiate Device Under Test
    counter #(.WIDTH(8)) dut (
        .clk(clk), .rst_n(rst_n), .count(count)
    );

    // 10 ns clock period
    always #5 clk = ~clk;

    initial begin
        $dumpfile("tb_counter.vcd");   // For GTKWave
        $dumpvars(0, tb_counter);

        rst_n = 0; #20;                // Assert reset
        rst_n = 1; #200;               // Run 20 cycles
        $display("Final count: %0d", count);
        $finish;
    end
endmodule
```

**Testbench checklist**:
- Test reset assertion and de-assertion
- Test corner cases: all-zeros input, all-ones, overflow
- Use `$display` for debug prints (like printf)
- Save `.vcd` waveform → open in GTKWave to visualize signals
- Use `$assert` or manual `if (expected != actual) $error(...)` for automated checks

---

## Phase 3: First FPGA Board
**Duration**: 4–8 weeks | **Hardware**: Lattice iCEstick ($25) or Digilent Basys 3 ($150)

### FPGA Implementation Flow
```
RTL Design (Verilog) 
    ↓ Synthesis (Quartus/Vivado/IceStorm)
Logic Gates + Flip-Flops
    ↓ Place and Route
FPGA Fabric Mapping
    ↓ Timing Analysis
Setup/Hold Verification
    ↓ Bitstream Generation
.bit / .bin file
    ↓ FPGA Programming
Working Hardware
```

### Starter Projects for FPGA (in order)
1. LED blink: clock divider counter → GPIO output
2. Button debouncer: FSM + shift register filter
3. 7-segment display driver: BCD → segment decoder
4. 4-bit counter on 7-seg: combines projects 1, 2, 3
5. UART transmitter: serial communication at 115200 baud
6. UART receiver + echo: round-trip serial
7. PWM generator: variable duty cycle via button input
8. SPI master: talk to external SPI sensor/DAC
9. VGA signal generator: 640×480@60 Hz timing (timing-critical)
10. Simple RISC processor: 8-bit CPU in ~500 lines of Verilog

### FPGA Vendor Tools (All Free Lite Versions)
| Vendor | Tool | Best For |
|--------|------|---------|
| Intel (Altera) | Quartus Prime Lite | Cyclone V, MAX 10 |
| AMD (Xilinx) | Vivado ML WebPACK | Artix-7, Kintex-7 |
| Lattice | iCEcube2 / Diamond | iCE40 (low power) |
| Open-source | IceStorm + Yosys | iCE40 fully open flow |

---

## Phase 4: Advanced HDL
**Duration**: Months 5–9 | Prerequisite: Phase 3 complete

- **Parameterized modules**: data width, depth, number of channels as parameters
- **Synchronous FIFO design**: pointers, full/empty flags, gray code for CDC
- **Clock Domain Crossing (CDC)**: two-flop synchronizer, FIFO CDC
- **AXI4-Lite bus**: industry-standard interface for SoC interconnects
- **SystemVerilog** (superset of Verilog): `interface`, `modport`, `class`, `constraint`, `enum`
- **cocotb**: Python-driven testbenches — write Python, simulate Verilog

```python
# cocotb testbench — Python controls the simulation
import cocotb
from cocotb.triggers import RisingEdge, Timer
from cocotb.clock import Clock

@cocotb.test()
async def test_counter(dut):
    cocotb.start_soon(Clock(dut.clk, 10, units="ns").start())
    dut.rst_n.value = 0
    await Timer(30, units="ns")
    dut.rst_n.value = 1
    for i in range(20):
        await RisingEdge(dut.clk)
    assert dut.count.value == 20, f"Expected 20, got {dut.count.value}"
```

---

## Phase 5: Real-World FPGA Engineering
**Duration**: Months 9–24 | Builds toward job-ready portfolio

### Portfolio-Grade Projects
- **FIR filter on FPGA**: implement scipy.signal design in hardware, verify with cocotb
- **ADC interface**: capture samples at 100+ MSPS, write to BRAM, read via SPI
- **High-speed SERDES**: PCIe, JESD204B, or Ethernet MAC interface
- **Image processing pipeline**: camera sensor → FPGA → VGA display with frame buffering
- **Motor control (FOC)**: field-oriented control in hardware for hard real-time torque control
- **RISC-V soft processor**: build from scratch or port PicoRV32/SERV

### Key Verification Skills
- **Coverage-driven verification**: track which code paths have been exercised
- **UVM (Universal Verification Methodology)**: industry standard for complex IP verification
- **Formal verification**: prove hardware correct mathematically (SymbiYosys for open-source)

---

## Free Learning Resources

| Resource | Level | URL |
|----------|-------|-----|
| HDLBits | Beginner | hdlbits.01xz.net |
| EDA Playground | Beginner-Int. | edaplayground.com |
| Neso Academy | Beginner | YouTube |
| fpga4fun.com | Intermediate | fpga4fun.com |
| Intel Verilog HDL Basics | Beginner | learning.intel.com |
| ZipCPU Blog (Dan Gisselquist) | Advanced | zipcpu.com |
| ChipVerify | Beginner | chipverify.com |
| Icarus Verilog (simulator) | All | iverilog.icarus.com |
| GTKWave (waveform viewer) | All | gtkwave.sourceforge.net |
| cocotb documentation | Intermediate | docs.cocotb.org |

---

## Career Targets
- **Sandia National Laboratory** (Livermore, CA) — FPGA engineering direct from BS; high-value defense/national-security work
- **Defense contractors**: Raytheon, Northrop Grumman, L3Harris — FPGA heavy
- **Data center networking**: Broadcom, Marvell, Cisco — network FPGA/ASIC
- **HFT (High-Frequency Trading)**: FPGA at nanosecond timing precision
- **Telecom**: Nokia, Ericsson — baseband processing FPGAs

---

## Cross-References
- [[Digital Logic and Boolean Algebra]] — prerequisite concept page
- [[EE Complete Mastery Roadmap]] — full EE progression; Track C details
- [[Python EE Project Ladder - Advanced Tracks]] — cocotb Track A
- [[EE Software and Lab Tools Complete Stack]] — FPGA tool reference section
