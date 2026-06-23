---
type: entity
entity_type: product
title: "Raspberry Pi Pico"
created: 2026-06-23
updated: 2026-06-23
tags:
  - entity
  - electronics
  - microcontroller
  - breadboard
related:
  - "[[Breadboard Starter Kit (What You Need)]]"
  - "[[Breadboard Project Ladder]]"
  - "[[Coolest Breadboard Projects]]"
---

# Raspberry Pi Pico

A ~$4 microcontroller board built on the **RP2040** (dual-core Arm Cortex-M0+ up to 133 MHz). Its DIP-style form factor drops straight into a breadboard, making it the cheapest and most breadboard-friendly way to add programmable "brains" to a circuit (Source: [[Research - Breadboard Electronics (Getting Started + Coolest Projects + Ladder)]]).

## Pico vs Arduino Uno (the beginner's fork)
| | Raspberry Pi Pico | Arduino Uno R3 |
|---|---|---|
| Price | ~$4–7 | ~$20–25 |
| CPU | dual-core M0+ @ 133 MHz | ATmega328P @ 16 MHz |
| Perf/watt | ~8.3× the Uno (RP2040) | baseline |
| Language | MicroPython / C++ | C++ (Arduino IDE) |
| Killer feature | **PIO** programmable I/O state machines | largest ecosystem / examples |
| Breadboard fit | excellent (DIP, breadboardable) | board + jumpers |

**Verdict for 2025+ beginners**: the Pico is cheaper, faster, and natively breadboard-friendly — great if you like Python and tinkering. Arduino still wins on the sheer volume of copy-paste examples and tutorials, so it remains the safest *first* board for absolute beginners. Either is fine; many start on Arduino and move to Pico.

## Where it sits
On the [[Breadboard Project Ladder]] the Pico/Arduino is the **mid-ladder unlock**: once analog (555, transistors, op-amps) feels comfortable, a microcontroller adds memory, logic, sensors, and networking.
