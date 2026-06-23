---
type: concept
title: "How a Breadboard Works"
created: 2026-06-23
updated: 2026-06-23
tags:
  - concept
  - electronics
  - breadboard
status: stable
related:
  - "[[Breadboard Starter Kit (What You Need)]]"
  - "[[Breadboard Project Ladder]]"
  - "[[555 Timer IC]]"
sources:
  - "[[SparkFun — How to Use a Breadboard]]"
---

# How a Breadboard Works

A **solderless breadboard** is a plastic block full of spring clips that lets you build temporary circuits by plugging in components — nothing is soldered, so you can rearrange endlessly while prototyping (Source: [[SparkFun — How to Use a Breadboard]]). Understanding the hidden metal strips is the whole game.

## The four parts

**1. Tie points (holes).** Every hole sits on a standard **0.1" (2.54 mm) pitch** and presses a component lead against a metal spring clip. Several clips are joined into one **electrical node**.

**2. Terminal strips (the main field).** In the central area, each short metal strip ties **exactly 5 holes** in a row to one node — e.g. `A1–B1–C1–D1–E1` are connected; the column next to them (`A2…`) is a separate node. Connections run *across the short rows*, never down the columns.

**3. The center ravine.** A channel down the middle electrically **isolates the top half of each row from the bottom half**. It is sized so a **DIP chip** (like a [[555 Timer IC]]) straddles it, putting its two pin rows on separate nodes — exactly what you want.

**4. Power rails (bus strips).** The long `+` (red) and `–` (blue/black) rails along the edges are each one continuous node, used to distribute power to the whole board. Caveat: the **two side rails are NOT connected to each other**, and on some boards a rail is split in the middle — bridge with jumper wires as needed.

## The mental model
> Plug positive voltage into a `+` rail and ground into a `–` rail. Run a jumper from each rail into a terminal column to power that part of your circuit. Components in the **same 5-hole row are wired together**; jump between rows to make connections. The ravine keeps the two halves of a chip apart.

## Common sizes
| Name | Tie points | Use |
|---|---|---|
| Mini | 170 | one tiny circuit, 1 small IC |
| Half | 400 | most beginner projects |
| Full | 830 | multi-IC circuits (the default kit board) |
| Giant / multi | 2,000+ | [[Ben Eater — Build an 8-bit Computer\|8-bit computers]], big builds |
