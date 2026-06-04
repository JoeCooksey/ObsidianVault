---
type: concept
title: "Robotics Foundation Models (VLA)"
created: 2026-06-04
updated: 2026-06-04
tags:
  - concept
  - ai
  - robotics
  - foundation-models
  - emerging-tech
status: developing
related:
  - "[[Physical AI (Embodied Intelligence)]]"
  - "[[Research - Most Useful Topics to Learn Now (for Joe)]]"
  - "[[Speculative Decoding]]"
---
# Robotics Foundation Models (VLA)

**Vision-Language-Action (VLA) models** are the foundation-model class powering [[Physical AI (Embodied Intelligence)|Physical AI]]: they take camera images + a language instruction and output robot actions directly. They are to robots what LLMs are to text. (Source: [[What Is Physical AI (SVRC)]])

## The 2026 Leaders

(Source: search synthesis of MarkTechPost / EVS / Generalist AI, confidence: medium)

- **Physical Intelligence — π0 / π0.5** — most-cited general-purpose VLA. π0 introduced **flow matching** for action generation: smooth, continuous trajectories well-suited to contact-rich manipulation.
- **Google DeepMind — Gemini Robotics / RT-2** — VLA built on a frontier multimodal LLM backbone.
- **NVIDIA — Isaac GR00T** — leads for *humanoid-specific* foundation models + simulation.
- **Octo** — open-source generalist robot policy (academic/community).
- **Generalist AI — GEN-1** — claimed first general physical-AI model to cross commercial-viability threshold across a broad task range. (confidence: low — vendor claim)

## Key Idea: Flow Matching for Actions

Rather than predicting discrete action tokens, **flow matching** learns a continuous transport from noise to a smooth action trajectory (conceptually related to diffusion). This produces the fine, continuous motor control that contact-rich tasks (grasping, insertion) demand. (Source: search synthesis)

> [!gap] The π0 flow-matching detail comes from secondary summaries, not the primary Physical Intelligence paper. Verify against the original before citing as authoritative.

## Why This Matters For Joe

VLAs are the **transferable-skill** layer of robotics: instead of hand-coding each task, you fine-tune a pretrained model — the same workflow Joe already knows from [[GGUF Format|edge LLMs]] and [[Post-Training Quantization|quantization]]. The action side (control, actuators, latency) is where EE knowledge is the differentiator.

## See Also

- [[Physical AI (Embodied Intelligence)]] — the parent field
- [[Neuromorphic Computing]] — running these models on-robot at low power
