---
type: entity
entity_type: product
title: "555 Timer IC"
created: 2026-06-23
updated: 2026-06-23
tags:
  - entity
  - electronics
  - ic
  - breadboard
related:
  - "[[Coolest Breadboard Projects]]"
  - "[[Breadboard Project Ladder]]"
  - "[[How a Breadboard Works]]"
---

# 555 Timer IC

The most popular and versatile timing chip in hobby electronics — an 8-pin DIP introduced by Signetics in **1972** and still in production. It is *the* gateway chip on a breadboard: a handful of resistors and capacitors around it produces blinkers, tones, and timers with **no programming**.

## Why it's the beginner workhorse
- 8-pin DIP straddles the breadboard ravine perfectly.
- Three operating modes teach the core of analog timing:
  - **Astable** — free-running oscillator (LED flasher, tone generator, clock). Frequency set by two resistors + one capacitor.
  - **Monostable** — one-shot timer (push button → output high for a set time).
  - **Bistable** — a simple latch / flip-flop.
- Cheap, forgiving of wiring mistakes, and every project book has circuits for it.

## Where it sits in the learning arc
After plain LED circuits, the 555 astable flasher is the canonical **second project** — it introduces oscillators, the RC time constant, and reading a datasheet. From there it scales into [[Coolest Breadboard Projects|sirens, theremins, LED roulettes, and synths]]. For anything needing memory or logic, you graduate from the 555 to a programmable [[Raspberry Pi Pico|microcontroller]].
