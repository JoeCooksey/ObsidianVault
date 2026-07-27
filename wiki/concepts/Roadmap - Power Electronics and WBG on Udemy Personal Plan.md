---
type: concept
title: "Roadmap - Power Electronics and WBG on Udemy Personal Plan"
created: 2026-07-27
updated: 2026-07-27
tags:
  - concept
  - domain/engineering
  - roadmap
  - power-electronics
  - wbg
  - udemy
status: developing
complexity: intermediate
domain: engineering
aliases: ["Udemy power electronics roadmap", "WBG roadmap Udemy", "SiC GaN course roadmap"]
related:
  - "[[Udemy Personal Plan EE Coverage Map]]"
  - "[[Research - Udemy Personal Plan Course Roadmaps for an EE Career]]"
  - "[[Research - EE Physical Side Skills for Semiconductors and Power]]"
  - "[[Research - WBG Semiconductors in EV Fast Charging]]"
sources:
  - "[[Udemy Catalog Audit — EE Topics, Premium Badge Method (July 2026)]]"
---

# Roadmap - Power Electronics and WBG on Udemy Personal Plan

**Total: ~48 hours across 4 courses.** This is the track that matches the WBG power-electronics career direction — and it is the one where the plan's limits show most clearly. It is a genuinely good *on-ramp* and a poor *destination*.

## The honest framing

Power Electronics has **54 courses total** on Udemy, of which roughly 7 of the top 17 are in the plan. There is **no wide-bandgap device physics course** anywhere in the catalog — SiC and GaN appear as chapters inside one broader course, not as subjects. The plan gets you converter literacy; it does not get you to WBG depth. That comes from [[Research - Top MS EE Programs Physical Side|graduate coursework]], vendor app notes (Wolfspeed, Infineon, TI), and lab work.

## The ladder

**Stage 0 — Circuits foundation, only if EEE 202 hasn't happened yet (36.5 h)**
`Ultimate Electrical Circuits for Electrical Engineering` ✅ 4.7 (798)
Skip this outright once you've taken circuits at ASU. Paying attention twice to the same nodal analysis is the most common way to waste a subscription month.

**Stage 1 — The core course (18 h)** ← start here
`Basics of Power Electronics` — Walid Issa ✅ 4.5 (1,509)
Explicitly covers **Si, SiC, GaN, LTspice, DC/DC converters, inverters, power dissipation, thermal stresses**. This is the most on-target single course in the entire Personal Plan for this career track. If you do only one thing from this roadmap, do this.

**Stage 2 — Gate drivers (3.5 h)**
`Mastering MOSFET & IGBT Gate Driver Circuit Design` ✅ 4.5 (139)
Short and disproportionately valuable. Gate drive is where WBG stops being a datasheet claim and starts being an engineering problem — dv/dt, Miller plateau, negative bias, layout inductance. This is what SiC design conversations are actually about.

**Stage 3 — Simulation, pick one**
- `Simulating dc-dc converters with QSPICE` ✅ 4.7 (49) 10h — QSPICE is the Mike Engelhardt successor to LTspice, faster for switching sims
- `Simulating Power Electronic Circuits using Python` ✅ 4.6 (307) 18.5h — pairs with [[Research - Python EE Project Roadmap]]

**Stage 4 — Systems context (52.5 h, optional, sample don't complete)**
`Ultimate Power Electronics and Electrical Protection Bundle` — Ahmed Mahdy ✅ 4.6 (1,112)
Treat as a **reference shelf**, not a course. Pull the converter and protection chapters; ignore the rest. Nobody should sit through 52 hours linearly.

## What you cannot get here

❌ **PSIM** and ❌ **PLECS** — the two industry-standard power-electronics simulators — are both excluded, as is the ❌ Power Factor Correction design series. If a specific internship names PSIM or PLECS, that course is a separate $15–20 purchase.
❌ No WBG device physics, no magnetics design course, no EMC/EMI course.

## The artifact

Close Stage 1 + 2 with a **buck converter designed, simulated, and documented**: chosen topology, switching frequency, device selection with a Si-vs-SiC loss comparison, gate-drive design, thermal estimate, and simulated waveforms. Write it up as a PDF or a repo. This is exactly the object a [[Lawrence Livermore National Laboratory|LLNL]] or Lam Research internship interview can be built around, and it maps onto Joe's existing [[Research - Python EE Project Roadmap|double-pulse-test project track]].

> [!important] Ranking within a limited subscription window: this track is **second** behind [[Roadmap - Embedded Firmware on Udemy Personal Plan|embedded]] — not because it matters less to the career, but because Udemy covers it less completely. The best power-electronics learning available to an undergrad is free (vendor app notes) or academic (coursework), while the best embedded learning genuinely is on Udemy.
