---
type: concept
title: "AI Five-Layer Cake"
created: 2026-04-18
updated: 2026-04-18
tags:
  - ai
  - strategy
  - nvidia
  - framework
status: developing
related:
  - "[[NVIDIA]]"
  - "[[Jensen Huang]]"
  - "[[CUDA Ecosystem Flywheel]]"
  - "[[Accelerated Computing]]"
sources:
  - "[[Darkesh-Patel-Jensen-Huang-Nvidia-2025]]"
---

# AI Five-Layer Cake

[[Jensen Huang]]'s framework for understanding the AI industry as a stack of five interdependent layers. Every layer must succeed for the industry to win; no single layer is sufficient.

## The Five Layers

| Layer | Description | Key Players |
|-------|-------------|-------------|
| **1. Energy** | Power for data centers. The hardest bottleneck — policy and infrastructure constrained; takes years to scale | Grid operators, utilities, energy policy |
| **2. Chips** | Compute hardware. Semiconductor fabs, memory, packaging | NVIDIA, TSMC, ASML, SK Hynix, Huawei |
| **3. Compute Platform** | Software stack, drivers, interconnects, inference engines | CUDA, NVLink, cuBLAS, vLLM, Triton |
| **4. Models** | Foundation models and training | OpenAI, Anthropic, Google DeepMind, Meta |
| **5. Applications** | The layer that diffuses into society; generates most economic value | Enterprise software, SaaS, AI agents, tools |

## Strategic Implications

### Layer 5 is the most important economically
The application layer is where AI benefits diffuse into society. Jensen argues the US should win *all five* layers — but the application layer creates the most societal and economic value.

### Layer 1 (energy) is the real bottleneck
Jensen consistently redirects supply chain discussions to energy: "You can't build an AI factory without energy, and those things take a long time." Chips and packaging can be scaled in 2–3 years given demand signals. Energy policy cannot.

### Why this framework matters for export controls
Jensen uses the five-layer model to argue against sacrificing Layer 2 (chips) for a marginal advantage in Layer 4 (models). Conceding the chip market to China accelerates their domestic ecosystem across *all* layers.

### China's position by layer
1. Energy: **abundant** — ghost cities, ghost datacenters, abundant power
2. Chips: **large but lagging** — 7nm capability, Huawei Ascend 910C; no EUV; catching up
3. Compute platform: **diverging** — forced off CUDA toward Huawei/domestic stacks
4. Models: **competitive** — DeepSeek, Qwen, 50% of world's AI researchers
5. Applications: **growing** — largest open-source contributor globally

## Related Concepts
- [[CUDA Ecosystem Flywheel]] — how Nvidia dominates Layer 2–3
- [[GPU vs TPU Trade-offs]] — tradeoffs within Layer 2–3
- [[Accelerated Computing]] — Nvidia's Layer 3 platform
