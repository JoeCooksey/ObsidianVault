---
type: guide
title: "Physical AI Build Guide (Roadmap for Joe)"
created: 2026-06-04
updated: 2026-06-04
tags:
  - guide
  - roadmap
  - ai
  - robotics
  - physical-ai
  - vla
  - career
status: developing
related:
  - "[[Physical AI (Embodied Intelligence)]]"
  - "[[Robotics Foundation Models (VLA)]]"
  - "[[Physical AI Project Ladder]]"
  - "[[LeRobot and SO-101 (Hugging Face)]]"
  - "[[Linear Algebra for AI and Quant]]"
  - "[[Research - Most Useful Topics to Learn Now (for Joe)]]"
sources:
  - "[[What Is Physical AI (SVRC)]]"
  - "[[LeRobot and SO-101 (Hugging Face)]]"
---
# Physical AI Build Guide (Roadmap for Joe)

A full, sequenced path from where Joe is now (1st-year EE, strong Python, some C++, already builds AI agents) to a competent **Physical AI / VLA builder**. Pair this with the concrete [[Physical AI Project Ladder]].

## The Strategic Thesis — Lean Into the EE Edge

The 2026 bottleneck in Physical AI is **not model capability — it's reliable, repeatable action in the messy real world** (Source: [[What Is Physical AI (SVRC)]]). That gap is *engineering* turf: sensors, actuators, power delivery, control loops, latency, calibration, thermal limits. **An ML PhD owns the model; an EE who can also fine-tune a VLA owns the deployment.** Joe should aim to be the person who makes foundation-model robots *actually work* on cheap, power-constrained hardware — not compete on architecture research.

> [!tip] Positioning: "I make VLAs run reliably on real, low-cost, edge-power robots." That sentence is a career, and almost nobody in the general-SWE flood can say it.

## How To Use This Roadmap

- **Phases 0–2 run during the school year** (they overlap your EE math/control coursework — double-dip).
- **Phases 3–5 are summer / project-time** (hardware + foundation models).
- Everything is **sim-first**: you can do 70% of this for $0 before buying any hardware.
- Ship every phase publicly (GitHub + short writeup) — building in public *is* the portfolio ([[EE Freshman Portfolio Strategy]]).

---

## Phase 0 — Foundations (parallel, ongoing)

The math/ML floor. Most overlaps EE coursework.

- **[[Linear Algebra for AI and Quant|Linear algebra]]** — non-negotiable; it's every forward pass (3Blue1Brown → Strang).
- **Python scientific stack** — NumPy, Matplotlib, then **PyTorch** (you already have Python; add tensors + autograd).
- **Probability + a little calculus** — gradients, distributions (you'll get calc in EE; lean in).
- **Transformers intuition** — what attention does, why it generalizes; you don't need to derive it, just wield it (you already use LLMs daily).
- **Control basics** — PID, state-space; **this is literally your EE [[Signals and Systems — Laplace and Fourier|signals/control]] coursework**. Robotics control = applied control theory.

**Done when:** you can train a small PyTorch net on a toy dataset and explain a PID loop.

---

## Phase 1 — Robotics Fundamentals + Simulation

Learn how robots are described and simulated. Pure software, $0.

- **Book/course:** *Modern Robotics* (Lynch & Park, Northwestern) — free PDF + Coursera. Ch 1–6: configuration space, rigid-body motions (screw theory), forward/inverse kinematics, velocity kinematics. This is the vocabulary of the whole field.
- **Simulator:** **MuJoCo** (now free, from DeepMind) — best for fast, contact-rich manipulation and minimal setup (Source: search synthesis). Install, load a robot arm model, command joint targets.
- **Glue:** **Gymnasium** (the maintained Gym fork) environment API.

**Done when:** you can spawn a simulated arm in MuJoCo and move its end-effector to a target pose with inverse kinematics.

---

## Phase 2 — Learning-Based Control (RL + Imitation Learning)

The two ways robots learn. Still sim, still ~$0.

- **Deep RL:** Sutton & Barto (free book) for theory → **Berkeley CS285** (free lectures) for deep RL. Implement/understand **PPO** (stable on-policy) and **SAC** (sample-efficient, continuous control) — the two workhorses (Source: search synthesis).
- **Imitation learning (more important for manipulation):** behavior cloning → **ACT** (Action Chunking Transformer) → **Diffusion Policy**. These are what actually drive the cheap arms.
- **Scale option:** **NVIDIA Isaac Lab** — GPU-parallel sim for thousands of simultaneous rollouts (humanoid locomotion, domain randomization). MuJoCo and Isaac Lab are **complementary**: MuJoCo for fast contact iteration, Isaac Lab for photorealistic, GPU-scaled training (Source: search synthesis). Use Isaac Lab once you have an NVIDIA GPU and outgrow MuJoCo.

**Done when:** you train a sim arm to do a reach/pick task via both an RL policy (PPO) and an imitation policy (ACT or Diffusion Policy).

---

## Phase 3 — Real Hardware (where the EE edge shows up) 🔧

Cross the sim-to-real gap on a robot you build. **~$130–250.**

- **Hardware:** **Hugging Face SO-101** arm — 3D-printable for ~$130, or $220–240 kit; 6-axis; second-gen, easier build than SO-100 (Source: [[LeRobot and SO-101 (Hugging Face)]]). Add a USB webcam.
- **Software:** **LeRobot** (Hugging Face) — the end-to-end library: teleoperate → record demonstrations → train (ACT/Diffusion Policy) → deploy *on the arm*. Follow the official `il_robots` ("Imitation Learning on Real-World Robots") tutorial.
- **The EE work that others skip:** servo wiring + bus, power budgeting, USB latency, camera-to-arm calibration, mechanical backlash, emergency stop. **This is your moat** — these are the reliability problems the field is stuck on, and they're your home turf.

**Done when:** your real SO-101 autonomously completes a pick-and-place it learned from your own teleoperated demos.

---

## Phase 4 — VLA Foundation Models 🧠

Go from task-specific policies to language-conditioned generalists.

- **Understand the two architectures:** **single-model** (RT-2, OpenVLA, π0 — one forward pass from image+text→action) vs **dual-system** (Helix, NVIDIA GR00T N1 — slow VLM planner + fast action head) (Source: search synthesis).
- **Fine-tune an open VLA on your own data:**
  - **OpenVLA** (7B, Stanford, Open X-Embodiment) — mature **LoRA** + **OFT** fine-tuning recipes; the best-documented entry point.
  - **π0 / openpi** (Physical Intelligence) — flow-matching action head; smooth contact-rich control (see [[Robotics Foundation Models (VLA)]]).
  - **NVIDIA GR00T N1** (2B, humanoid) — if you go the Isaac/humanoid route.
- **Edge deployment (peak EE+AI):** quantize and run inference on a **Jetson Orin Nano** (~$250–500) on the robot. Reuse your [[Post-Training Quantization]] / [[GGUF Format|edge-LLM]] knowledge — VLAs are transformers too. [[Neuromorphic Computing]] is the long-horizon version of this.
- **Sim-to-real:** domain randomization, action smoothing, latency compensation.

**Done when:** you fine-tune an open VLA on your SO-101 data and it follows a *natural-language* instruction ("pick up the red block").

---

## Phase 5 — Capstone + Portfolio

One end-to-end project that proves the whole stack, ideally tied to your identity.

- **Pick a niche only you can own:** "VLA manipulation on sub-$300 hardware," or fuse it with your power track — a robot doing a physical EE/bench task, or focusing on the **actuator/power/embedded reliability** layer.
- **Publish:** GitHub repo + README with video, a short technical writeup (blog or X thread), and the dataset on the Hugging Face Hub.
- **Plug into ASU:** pitch this as an **FURI** research project (you're eligible from semester 2 — see [[Freshman Summer Project Plan (Tier List)]]); cold-email a robotics/controls professor.

**Done when:** a stranger can watch a 60-second video and a repo and understand that you build language-controlled robots.

---

## Resource Quick-Reference

| Need | Resource (mostly free) |
|------|------------------------|
| Robotics math/kinematics | *Modern Robotics* — Lynch & Park (book + Coursera) |
| Manipulation course | Tedrake **Robotic Manipulation** (manipulation.csail.mit.edu, uses Drake) |
| Dynamics / legged | Tedrake **Underactuated Robotics** (MIT 6.832) |
| Deep RL | **Berkeley CS285**, Stanford CS234, Sutton & Barto |
| Hands-on robot learning | **Hugging Face LeRobot** library + docs + course |
| Cheap hardware | **SO-101** arm (~$130 DIY / $220–240 kit) |
| Fast sim | **MuJoCo** (free) |
| Scaled sim | **NVIDIA Isaac Lab** (GPU) |
| Open VLA models | **OpenVLA**, **openpi (π0)**, **GR00T N1** |
| Big dataset | **Open X-Embodiment** (1M+ episodes, 22 embodiments) |
| Edge inference | **Jetson Orin Nano** + quantization |

## The Honest Timeline

This is a **2–4 year** arc layered on top of your EE degree, not a summer sprint. But Phases 0–2 are pure overlap with coursework, and Phase 3 (a real learning robot for ~$130) is achievable in one focused summer. The compounding is the point: every EE control/power/embedded class makes you *better* at the part of Physical AI that everyone else finds hardest.

## See Also

- [[Physical AI Project Ladder]] — the concrete project-by-project sequence
- [[Physical AI (Embodied Intelligence)]] · [[Robotics Foundation Models (VLA)]] — the concept pages
- [[LeRobot and SO-101 (Hugging Face)]] — the central hands-on toolchain
