---
type: meta
title: "Hot Cache"
updated: 2026-04-18T12:00:00
tags:
  - meta
---
# Recent Context

## Last Updated
2026-04-18 — Ingest: Dwarkesh Patel × Jensen Huang Nvidia Interview (2025)

## Key Recent Facts

### Nvidia Strategy (newest — Jensen Huang interview)
- **Electrons → Tokens**: Jensen's core mental model for Nvidia. Input is electrons, output is tokens; Nvidia is what's in between
- **Five-Layer Cake**: AI stack = energy → chips → compute platform → models → applications. US must win all five. Energy is the hardest bottleneck (years, not 2–3 years like chips)
- **CUDA Flywheel**: install base (hundreds of millions GPUs, all clouds) → developer ecosystem → richest frameworks → best TCO → more customers → larger install base
- **Hopper→Blackwell 50× improvement**: ~75% from hardware; rest from MoE, disaggregation, new kernels — enabled by CUDA programmability
- **Moore's Law claim**: ~25%/year from transistors alone; great CS = 10–100× leaps; architecture > lithography
- **TPU vs GPU**: GPUs win on programmability; TPUs win on fixed-workload efficiency. Jensen: "TPU won't come to InferenceMAX benchmarks"
- **Anthropic on TPU**: Jensen says this is "unique, not a trend" — driven by Google/AWS equity deals at Anthropic's founding, not tech superiority
- **China export controls**: Jensen against — China already has threshold compute (7nm + abundant energy); 50% of AI researchers are Chinese; conceding market accelerates Huawei ecosystem
- **Supply chain**: FIFO by PO; no auction pricing; committed $100B+; CoWoS/HBM bottlenecks resolved; energy now the real bottleneck
- **Company philosophy**: "Do as much as needed, as little as possible" — build what only Nvidia can; partner for rest; not a hyperscaler; invest in all foundation labs, don't pick winners
- **Chip roadmap**: Blackwell → Vera Rubin → Vera Rubin Ultra → Feynman → (unnamed)
- **Groq acquisition**: folded into CUDA for premium latency tokens (high-ASP, lower throughput segment)

### Cycling Periodization (previous)
- Annual arc (5 phases): Base+Strength (Oct–Dec) → Build+Power (Jan–Mar) → VO2 Max Blocks (Apr–May) → Competition (Jun–Aug) → Transition (Sep–Oct)
- Polarized model (Seiler): 80% Zone 1 / ~20% Zone 3
- Training plan created: 6-day/week (rest Sunday)

### Emotional Agility (previous)
- Emotional agility (Susan David): compassion + curiosity + courage to take values-connected steps

### CPU / GPU Architecture (previous)
- PCIe bottleneck (64 GB/s) vs NVLink 5 (1.8 TB/s); unified memory (Apple M5 Max, AMD APU)

## Recent Changes
- Created: [[Darkesh-Patel-Jensen-Huang-Nvidia-2025]], [[Jensen Huang]], [[Dwarkesh Patel]]
- Created: [[AI Five-Layer Cake]], [[CUDA Ecosystem Flywheel]], [[GPU vs TPU Trade-offs]], [[Accelerated Computing]]
- Updated: [[NVIDIA]], [[CUDA Programming Model]], [[Wiki Index]], [[Wiki Log]]

## Active Threads
- **Nvidia × Edge LLM cross-link**: CUDA ecosystem flywheel explains why llama.cpp/MLC-LLM/vLLM all target CUDA first — consistent with [[Survey - Low-bit LLMs 2024]] and [[Edge LLM Inference Benchmark 2026]]
- **China compute × DeepSeek**: Jensen's point that DeepSeek shows algorithm advances > hardware; important for understanding why inference efficiency papers matter
- **Energy bottleneck**: Jensen names energy (not chips) as the multi-year constraint; relevant to EV/WBG work — data centers and EVs compete for grid capacity
- Personal context: 19-year-old male EE student, trains 6 days/week, rest Sunday
