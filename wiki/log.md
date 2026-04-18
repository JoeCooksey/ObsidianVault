---
type: meta
title: "Wiki Log"
updated: 2026-04-18
tags:
  - meta
---
# Wiki Log

Append-only. New entries go at the TOP. Format: `## [YYYY-MM-DD] operation | title`

---

## [2026-04-18] ingest | Impostors - Susan David on Emotional Agility
- Source: `.raw/transcripts/A Harvard Psychologist Teaches Us How to Increase Our Emotional Intelligence.txt`
- Summary: [[Impostors - Susan David on Emotional Agility]]
- Pages created: [[Impostors - Susan David on Emotional Agility]], [[Susan David]], [[Emotional Agility]], [[Emotional Rigidity]], [[Gentle Acceptance]], [[Emotion Granularity]], [[Defusion Language]], [[Toxic Positivity]], [[Emotions as Functional]]
- Pages updated: [[Wiki Index]], concepts/_index.md, entities/_index.md
- Key insight: Suppressing difficult emotions (toxic positivity) makes people less resilient; the three practical tools — gentle acceptance, emotion granularity, and defusion language — move from paralysis to values-connected action.

## [2026-04-18] autoresearch | Evolution of CPUs and GPUs
- Rounds: 2
- Sources found: 5 web searches + 1 fetched page (SIGGRAPH 2025)
- Pages created: [[SIGGRAPH - Eras of GPU Development 2025]], [[Intel]], [[AMD]], [[NVIDIA]], [[CPU Architecture Evolution]], [[GPU Architecture Evolution]], [[Moore's Law and Dennard Scaling]], [[Heterogeneous Computing]], [[CUDA Programming Model]], [[GPU Interconnects]], [[Unified Memory Architecture]], [[Research - Evolution of CPUs and GPUs]]
- Synthesis: [[Research - Evolution of CPUs and GPUs]]
- Key finding: CPU performance scaling broke in 2005 (Dennard scaling failure) forcing the multi-core and heterogeneous GPU era; PCIe bandwidth (~64 GB/s) is the bottleneck between CPU and discrete GPU — unified memory (Apple Silicon, AMD APU) eliminates it at the cost of raw TFLOPS; NVLink 5 at 1.8 TB/s is why NVIDIA dominates AI training.

## [2026-04-18] ingest | Huberman Lab Essentials - The Science of Making & Breaking Habits
- Source: `.raw/transcripts/Essentials_ The Science of Making _ Breaking Habits.txt`
- Summary: [[Huberman Lab Essentials - Habit Formation and Breaking]]
- Pages created: [[Huberman Lab Essentials - Habit Formation and Breaking]], [[Andrew Huberman]], [[Wendy Wood]], [[Limbic Friction]], [[Task Bracketing]], [[Neuroplasticity and Habit Formation]], [[Habit Strength]], [[Linchpin Habits]], [[Identity-Based vs Goal-Based Habits]], [[Three-Phase Day Framework]], [[21-Day Habit Formation System]], [[Habit Breaking via Replacement Behavior]], [[Procedural Memory Visualization]]
- Pages updated: [[Wiki Index]], concepts/_index.md, entities/_index.md, domains/Research.md
- Key insight: The dorsal lateral striatum brackets the start and end of habits (not the middle) — aligning habits with circadian neurochemical phases and inserting a replacement behavior immediately after a bad habit are the two highest-leverage practical tools.

## [2026-04-18] autoresearch | Supplements for Young Male Health, Learning, and EE Performance
- Rounds: 3
- Sources found: 2 PMC meta-analyses + supporting PubMed literature
- Pages created: [[Foundational Health Supplements]], [[Creatine for Cognitive Performance]], [[Caffeine and L-Theanine Stack]], [[Bacopa Monnieri]], [[Lion's Mane Mushroom]], [[Rhodiola Rosea]], [[Sleep Optimization Supplements]], [[Supplement Priority Stack for Young Males]], [[PMC Creatine Meta-analysis 2024]], [[PMC Caffeine Theanine Review 2022]], [[Research - Supplements for Young Male Health and Learning]]
- Synthesis: [[Research - Supplements for Young Male Health and Learning]]
- Key finding: Fix vitamin D deficiency first (36% of 18–29 year olds are deficient); caffeine+L-theanine is the strongest acute cognitive stack; creatine adds memory benefit at low cost; sleep and exercise outperform all supplements combined.

## [2026-04-18] autoresearch | Wide Bandgap Semiconductor Applications in EV Fast Charging
- Rounds: 3
- Sources found: 2 papers + IEEE Spectrum article
- Pages created: [[Wide Bandgap Semiconductors]], [[Silicon Carbide Power Electronics]], [[Gallium Nitride Power Electronics]], [[Gallium Oxide Power Electronics]], [[800V EV Architecture]], [[EV Fast Charging Topologies]], [[V2G Bidirectional Charging]], [[WBG Thermal Management]], [[Wolfspeed]], [[STMicroelectronics SiC]], [[IEEE Spectrum SiC vs GaN 2024]], [[MDPI WBG Comparative Review 2024]], [[Research - WBG Semiconductors in EV Fast Charging]]
- Synthesis: [[Research - WBG Semiconductors in EV Fast Charging]]
- Key finding: SiC is physically mandatory for 800V EV architectures (1200V blocking requirement eliminates silicon IGBTs); GaN is ascending for OBCs at higher switching frequency; thermal management — not compute — is the primary reliability bottleneck.

## [2026-04-18] autoresearch | LLM Quantization and Optimization for Edge Hardware
- Rounds: 3
- Sources found: 4 papers (arXiv)
- Pages created: [[Post-Training Quantization]], [[GGUF Format]], [[LLM Pruning]], [[Knowledge Distillation for Edge LLMs]], [[Speculative Decoding]], [[BitNet]], [[llama.cpp]], [[MLC-LLM]], [[Survey - Low-bit LLMs 2024]], [[Edge LLM Inference Benchmark 2026]], [[Framework Comparison Apple Silicon 2025]], [[Bitnet.cpp Edge Inference 2025]], [[Research - LLM Quantization and Edge Hardware]]
- Synthesis: [[Research - LLM Quantization and Edge Hardware]]
- Key finding: Thermal throttling on mobile devices is the primary edge deployment bottleneck — not raw TOPS — and INT4 weight-only quantization (AWQ/GGUF Q4_K_M) is the practical sweet spot for edge LLM deployment.

## [2026-04-18] scaffold | Initial vault structure created
- Mode: D (Personal) + E (Research) + F (Books)
- Purpose: Personal second brain connecting ideas across engineering, math, books, and research topics
- Structure created: wiki/, .raw/, _templates/, _attachments/
- Domains created: [[Engineering]], [[Mathematics]], [[Books]], [[Research]], [[Theology]]
- Meta files created: [[Wiki Index]], [[Wiki Overview]], [[Hot Cache]], [[Dashboard]]
