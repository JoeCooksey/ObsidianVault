---
type: source
title: "LeRobot + SO-101 — Hugging Face Open Robotics Stack"
source_type: documentation
author: Hugging Face / TheRobotStudio
date_published: 2025
url: https://github.com/huggingface/lerobot
created: 2026-06-04
updated: 2026-06-04
confidence: high
tags:
  - source
  - robotics
  - physical-ai
  - hardware
  - tooling
status: complete
related:
  - "[[Physical AI Build Guide (Roadmap for Joe)]]"
  - "[[Physical AI Project Ladder]]"
  - "[[Robotics Foundation Models (VLA)]]"
key_claims:
  - "SO-101 is a 3D-printable 6-axis arm buildable for ~$130 (kits $220-240)"
  - "LeRobot is an end-to-end library: teleoperate, record, train (ACT/Diffusion Policy), deploy on the arm"
  - "It is the de-facto low-cost entry point to real-world imitation learning in 2026"
---
# LeRobot + SO-101 (Hugging Face)

The open-source hardware + software stack that makes real-world robot learning affordable — the central hands-on toolchain for the [[Physical AI Build Guide (Roadmap for Joe)]].

## What It Is

- **LeRobot** — Hugging Face's open robotics library + model/dataset hub. Provides datasets, pretrained models, and the full pipeline: **teleoperate → record demonstrations → train → deploy**. Supports imitation learning (ACT, Diffusion Policy) and reinforcement learning. (Source: GitHub huggingface/lerobot)
- **SO-101** — a low-cost, 3D-printable **6-axis** robot arm, second generation of the SO-100, by TheRobotStudio + Hugging Face. Buildable for **~$130**; pre-made kits **$220–240** (AliExpress/Seeed). The SO-101 removed the SO-100 gear-disassembly step (easier build).

## Why It Matters For Joe

This collapses the cost of *real* (not just simulated) Physical AI from "lab budget" to "one summer's pocket money." The workflow — collect your own teleoperated data, train an imitation policy, run it on the arm — is exactly Tier 2 of the [[Physical AI Project Ladder]], and the place where Joe's EE skills (wiring, servos, power, calibration, latency) are the differentiator.

## Key Resources

- `huggingface/lerobot` (GitHub) — the library.
- LeRobot docs: **`il_robots`** ("Imitation Learning on Real-World Robots") — the canonical real-arm tutorial.
- `so101` docs page — build + bring-up.
- Hugging Face Hub — community SO-101 datasets to learn from / benchmark against.

## Reliability Note

Primary/official documentation and widely-corroborated hardware specs across HF, Hackster, CNX-Software, Seeed, Waveshare — **high** confidence on the toolchain and price points (~$130 DIY, $220–240 kit).

## Feeds

- [[Physical AI Build Guide (Roadmap for Joe)]] · [[Physical AI Project Ladder]]
- [[Robotics Foundation Models (VLA)]]
