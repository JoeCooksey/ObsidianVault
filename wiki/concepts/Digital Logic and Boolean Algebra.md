---
type: concept
title: "Digital Logic and Boolean Algebra"
created: 2026-04-27
updated: 2026-04-27
tags:
  - EE
  - digital-logic
  - boolean-algebra
  - FPGA
  - Verilog
  - first-year
status: developing
---
# Digital Logic and Boolean Algebra

The foundation of every digital system: microcontrollers, FPGAs, CPUs, and mixed-signal designs. Boolean algebra is to digital EE what circuit theory is to analog EE.

## Why This Matters for First-Year EE

Joe's first official EE course is **EEE 120 Digital Design** (Term 3A, Year 2). Arriving fluent means going from struggle to mastery. Beyond the course:
- FPGA engineering averages $175k; digital logic is the direct prerequisite
- Every power converter DSP (TI C2000, STM32) runs state machines designed with sequential logic
- Digital control loops, PWM generation, and protection logic all trace back to Boolean design

## Core Topics in Order

### 1. Number Systems and Representation
- Binary, octal, hexadecimal — conversion methods in each direction
- **Two's complement**: representation for signed integers; allows subtraction via addition hardware
- Binary arithmetic: addition, subtraction, multiplication via shift-add

### 2. Boolean Algebra — The Axiom System
- Variables are strictly 0 or 1
- Basic operations: AND ($\cdot$), OR ($+$), NOT ($\bar{}$)
- Key theorems:
  - Identity: $A \cdot 1 = A$, $A + 0 = A$
  - Complement: $A \cdot \bar{A} = 0$, $A + \bar{A} = 1$
  - Idempotency: $A \cdot A = A$, $A + A = A$
  - **De Morgan's Laws** (critical for circuit optimization):
    - $\overline{A \cdot B} = \bar{A} + \bar{B}$
    - $\overline{A + B} = \bar{A} \cdot \bar{B}$
- Sum of Products (SOP) and Product of Sums (POS) canonical forms

### 3. Logic Gates and CMOS Implementation
- AND, OR, NOT, NAND, NOR, XOR, XNOR
- **NAND and NOR are universal gates** — any logic function can be built from NAND alone
- **CMOS implementation**: complementary N-type (pull-down) and P-type (pull-up) MOSFETs
  - This connects directly to semiconductor device physics
  - CMOS: low static power (only draws current during switching)

### 4. Karnaugh Maps (K-maps) — Boolean Minimization
- Graphical method to find the minimal SOP or POS expression
- Groups of 1, 2, 4, 8 (power of 2) cells → each grouping eliminates one variable
- 2–6 variable K-maps; EEE 120 expects fluency
- Output: minimal gate-level circuit → reduces cost, power, propagation delay

### 5. Combinational Logic Circuits
- Output depends only on current inputs — no memory
- **Half adder**: 1-bit addition; outputs sum and carry
- **Full adder**: 1-bit addition with carry-in; cascadeable to N-bit adder
- **Ripple carry adder**: N full adders chained; simple but slow (carry propagation delay)
- **Multiplexers (MUX)**: selects one of $2^n$ inputs based on $n$ select lines
- **Decoders**: $n$ inputs → $2^n$ one-hot outputs
- **Comparators**: output high when A == B

### 6. Sequential Logic — Memory and State
- Output depends on current inputs AND past state
- **SR Latch**: basic memory; unstable when S=R=1
- **D Flip-Flop**: fundamental memory element; captures input at clock edge
- **Clock-driven design**: all state changes synchronized to clock edge
- **Registers**: parallel array of D flip-flops; store an N-bit word
- **Counters**: cascaded flip-flops; binary counter, Johnson counter, LFSR (shift register)

### 7. Finite State Machines (FSMs) — The Control Paradigm
- Any control system with distinct modes of operation is an FSM
- **Moore FSM**: outputs depend only on current state
- **Mealy FSM**: outputs depend on state AND current inputs (faster response)
- Design flow: problem description → state diagram → state table → K-map minimization → gate/flip-flop implementation → Verilog
- Real applications: traffic light controllers, serial (UART) decoders, sequence detectors, PWM generators

### 8. Introduction to Verilog (Hardware Description Language)
- Verilog describes hardware structure and behavior; it is NOT a programming language — it synthesizes to actual gates and flip-flops
- **Key constructs**:
  - `assign out = a & b;` — combinational logic
  - `always @(posedge clk)` — sequential logic triggered on clock edge
  - `if/else`, `case` — behavioral descriptions that synthesize to MUX/gate structures
- **Testbenches**: simulation-only Verilog that applies stimuli and checks outputs
- **Tools**: Icarus Verilog (free simulator) + GTKWave (waveform viewer)
- HDLBits.01xfpga.com: best free interactive Verilog practice resource

## Best Learning Resources

| Resource | Format | Best For |
|----------|--------|---------|
| Morris Mano "Digital Design" | Textbook | ASU standard; thorough |
| Neso Academy (YouTube) | Video series | Best free comprehensive series |
| Digital Fundamentals — Floyd | Textbook | More accessible language |
| HDLBits.01xfpga.com | Interactive | Best Verilog practice; graded exercises |
| Icarus Verilog + GTKWave | Free tools | Local simulation and waveform viewing |

## Joe's Milestones

1. **Boolean**: Simplify a 4-variable expression using K-map → minimal SOP → verify with truth table
2. **Combinational**: Design a 4-bit ripple carry adder from full adder cells → implement in Verilog → simulate
3. **Sequential**: Build a mod-10 BCD counter with D flip-flops → simulate → verify waveform counts 0–9 then resets
4. **FSM**: Write a Moore FSM for a vending machine ($0.25 → dispense) in Verilog → simulate all paths
5. **GitHub**: Push the FSM Verilog project as first digital logic portfolio item before EEE 120 starts

## Connection to FPGA Career Track (Level 6)

Digital Logic → Verilog fluency → cocotb testbenches (Project 20A in Python EE Project Ladder) → FPGA design role

- FPGA engineers: $175k avg, $251k+ 90th percentile
- Sandia National Lab (Livermore, 5 min drive) is a direct FPGA employer
- Joe's Phase 4 choice (EE High Income Action Plan): Track A = FPGA path, starts with this material

## Related Concepts
- [[EE Topic Depth Priority Map]]
- [[ASU EE Year 1-2 Curriculum Map]]
- [[EE Freshman Self-Study Stack]]
- [[Python EE Project Ladder - Advanced Tracks]]
- [[EE High Income Action Plan]]
- [[Semiconductor Device Fundamentals]]
