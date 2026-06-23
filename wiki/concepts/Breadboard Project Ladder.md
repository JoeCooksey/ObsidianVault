---
type: guide
title: "Breadboard Project Ladder"
created: 2026-06-23
updated: 2026-06-23
tags:
  - guide
  - electronics
  - breadboard
  - projects
status: stable
related:
  - "[[Coolest Breadboard Projects]]"
  - "[[Breadboard Starter Kit (What You Need)]]"
  - "[[How a Breadboard Works]]"
  - "[[555 Timer IC]]"
  - "[[Raspberry Pi Pico]]"
  - "[[Ben Eater]]"
  - "[[Physical AI Project Ladder]]"
sources:
  - "[[Science Buddies — 10 Breadboard Projects to Get Started]]"
  - "[[Ben Eater — Build an 8-bit Computer]]"
---

# Breadboard Project Ladder

A progressive sequence that turns the [[Breadboard Starter Kit (What You Need)|starter kit]] into shipped circuits. Same philosophy as the [[Physical AI Project Ladder]]: each rung is small, finishable, and adds **exactly one new idea**. The natural arc is **LED → 555 timer → transistor → op-amp/audio → microcontroller → digital logic → CPU** (Source: [[Science Buddies — 10 Breadboard Projects to Get Started]]).

## Tier 0 — First light (DC basics)
1. **Light one LED** — battery/5 V → resistor → LED → ground. Teaches Ohm's law, current-limiting resistors, polarity, and [[How a Breadboard Works|reading the board]].
2. **Two LEDs + a pushbutton** — series vs. parallel, switches, the power rails.
3. **Voltage divider + potentiometer** — dim an LED by turning a knob; teaches dividers and variable resistance.

## Tier 1 — The 555 era (oscillators & timing)
4. **555 astable LED flasher** — your first oscillator; RC time constant sets the blink rate. ([[555 Timer IC]])
5. **555 monostable one-shot timer** — button press → LED on for N seconds.
6. **555 tone generator → siren** — drive a piezo/speaker; sweep frequency for a siren.
7. **555 + 4017 LED chaser / roulette** — add a decade counter; first taste of sequential logic.

## Tier 2 — Transistors & analog (signals & power)
8. **Transistor as a switch** — small signal turns on a motor/LED strip; base resistor, current gain.
9. **Light/dark sensor (LDR + transistor)** — automatic night light or soil-moisture indicator.
10. **LM386 audio amplifier** — amplify a phone/mic into a speaker; intro to audio.
11. **Theremin or breadboard synth** — *the impressive analog capstone*; oscillators + hand-controlled pitch.

## Tier 3 — Programmable brains (microcontroller)
12. **Blink on a [[Raspberry Pi Pico]]/Arduino** — "hello world" of MCUs; GPIO + code.
13. **Read a sensor, drive an output** — pot/ultrasonic/temperature → LED bar, servo, or OLED.
14. **A small system** — reaction-timer game, digital dice, OLED clock/weather station, or a servo robot.

## Tier 4 — Digital logic → a computer (trophy tier)
15. **Build logic gates from transistors / 74-series chips** — physically realize [[Digital Logic and Boolean Algebra|Boolean algebra]].
16. **Binary counter + 7-segment display** — clock, counter, decoder; the building blocks of a CPU.
17. **[[Ben Eater]]'s 8-bit breadboard computer** — clock → registers → ALU → RAM → control logic. The capstone that ties everything together.

## How to climb
- Finish each rung (working circuit) before moving on — breadboarding rewards reps.
- Keep a build log / photos; these become a portfolio for an [[Engineering|EE]] résumé.
- Don't skip the 555 tier — RC timing and oscillators underpin almost everything analog.
- Buy the [[Raspberry Pi Pico]] only when Tier 1–2 feel easy; the chip can mask gaps in fundamentals if you start there.
