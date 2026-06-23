---
type: source
source_type: tutorial
title: "How to Use a Breadboard"
author: SparkFun Electronics
date_published: 2024-01-01
url: https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard/all
confidence: high
tags:
  - source
  - electronics
  - breadboard
key_claims:
  - "Breadboard holes are on a standard 0.1 inch (2.54 mm) pitch; each terminal-strip row connects exactly 5 tie points."
  - "A center ravine isolates the two halves of each row and is sized to straddle DIP chip legs."
  - "Power rails run the length of the board and are typically all connected; the two side rails are NOT connected to each other."
  - "Common sizes: mini 170 tie points, full-size 400, larger 830; SparkFun 'giant' has 2,016 points."
---

# SparkFun — How to Use a Breadboard

The canonical beginner tutorial on solderless breadboard anatomy. Primary source for [[How a Breadboard Works]].

## What it contributes
- **Tie points & pitch**: every hole sits on a 0.1" (2.54 mm) grid so DIP-package chips drop in cleanly. Each terminal-strip row ties **5 holes** to one electrical node (Source: high).
- **The ravine**: the center channel electrically isolates the top and bottom halves of every row and is exactly wide enough to seat a DIP IC so its two pin rows land on separate nodes.
- **Power rails (bus strips)**: the long `+`/`–` rails down the sides distribute power everywhere. The two side rails are independent — bridge them with jumpers if you need power on both sides.
- **Beginner essentials**: jumper-wire kits (~140 pcs), and a power source — borrow 5 V/3.3 V from an Arduino/Pico, use a benchtop supply, or a dedicated breadboard power module.

> [!note] SparkFun is a primary educational vendor; the electrical facts here are corroborated by Wikipedia and multiple tutorials → **high confidence**.
