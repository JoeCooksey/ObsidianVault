---
type: meta
title: "Hot Cache"
updated: 2026-04-18T00:00:00
tags:
  - meta
---
# Recent Context

## Last Updated
2026-04-18 — Autoresearch: LLM Quantization and Optimization for Edge Hardware

## Key Recent Facts
- **INT4 weight-only (AWQ/GGUF Q4_K_M)** is the practical sweet spot for edge LLM deployment — halves memory vs INT8, works on any hardware, minimal accuracy loss
- **Thermal throttling** is the dominant bottleneck on mobile edge devices (iPhone, Android) — TOPS marketing numbers are misleading for sustained inference
- **RPi 5 + Hailo-10H NPU**: only platform sustaining <2W continuous operation; best for always-on agents (270.5 mJ/token, 1.87W)
- **BitNet b1.58**: Microsoft ternary LLMs achieve 2.4–6× CPU speedup and 55–82% energy reduction; can run 100B params on single CPU; requires training from scratch (no FP16 conversion)
- **EAGLE-3 / VSD**: state-of-the-art speculative decoding achieving 2–3.6× decoding speedup; primarily validated on server GPUs, not edge NPUs
- **Framework landscape**: MLX (throughput) > MLC-LLM (latency) > llama.cpp (portability) on Apple Silicon

## Recent Changes
- Created: [[Post-Training Quantization]], [[GGUF Format]], [[LLM Pruning]], [[Knowledge Distillation for Edge LLMs]], [[Speculative Decoding]]
- Created: [[BitNet]], [[llama.cpp]], [[MLC-LLM]]
- Created: 4 source pages, 1 synthesis page
- Updated: [[Wiki Index]], [[Wiki Log]]

## Active Threads
- Research topic: LLM quantization and edge hardware — 13 pages filed, 5 open questions
- Open question: speculative decoding on NPU hardware (not yet benchmarked)
- Open question: BitNet quality floor across task types
- Open question: sub-1B model reasoning capability limits
