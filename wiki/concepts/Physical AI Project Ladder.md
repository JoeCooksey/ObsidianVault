---
type: guide
title: "Physical AI Project Ladder"
created: 2026-06-04
updated: 2026-06-04
tags:
  - guide
  - projects
  - robotics
  - physical-ai
  - vla
status: developing
related:
  - "[[Physical AI Build Guide (Roadmap for Joe)]]"
  - "[[Physical AI (Embodied Intelligence)]]"
  - "[[Robotics Foundation Models (VLA)]]"
  - "[[Python EE Project Ladder]]"
---
# Physical AI Project Ladder

The concrete, progressive project list that turns the [[Physical AI Build Guide (Roadmap for Joe)|build guide]] into shipped artifacts. Same philosophy as the [[Python EE Project Ladder]]: each rung is small, finishable, and public. Sim-first — Projects 1–6 cost $0.

## Tier 0 — Foundations (sim, $0)

1. **PyTorch warm-up** — train a small MLP/CNN on a toy dataset; log it. Proves the ML floor.
2. **MuJoCo hello-robot** — load a built-in arm, command joint angles, render it. Proves the sim toolchain.
3. **Inverse kinematics reacher** — move the arm's end-effector to a clicked 3D target using IK. Proves [[Physical AI Build Guide (Roadmap for Joe)|Phase 1]] kinematics.

## Tier 1 — Learning-Based Control (sim, $0)

4. **PPO reacher** — train an RL policy (PPO) to reach random targets in MuJoCo/Gymnasium. First learned policy.
5. **Behavior cloning** — record a scripted expert, train a net to imitate it. The simplest imitation learning.
6. **ACT or Diffusion Policy pick-and-place** — train a modern imitation policy on a sim pick task. This is the *exact* algorithm class the real arms use — bridge to hardware.

## Tier 2 — Real Hardware (~$130–250) 🔧

7. **Build + teleoperate the SO-101** — assemble the arm, get teleoperation working in LeRobot. *Pure EE win:* wiring, servos, power, calibration.
8. **Record a real dataset** — teleoperate 30–50 demos of one task (e.g., cube into cup); publish it to the Hugging Face Hub.
9. **Train + deploy on the real arm** — train ACT/Diffusion Policy on your data, run it autonomously. **First real autonomous robot.** Document the sim-to-real gotchas (latency, calibration) — that writeup is gold.

## Tier 3 — Foundation Models (VLA) 🧠

10. **Fine-tune OpenVLA (LoRA)** — adapt a pretrained 7B VLA to your SO-101 task; compare vs your from-scratch ACT policy.
11. **Language-conditioned task** — get the VLA to follow a *spoken/typed* instruction ("pick up the red one"). The "wow" demo.
12. **Edge deployment** — quantize the policy and run inference on a Jetson Orin Nano *on the robot*. Reuses your [[Post-Training Quantization|quantization]] / edge-LLM skills; nobody else in a freshman cohort does this.

## Tier 4 — Capstone (pick ONE)

13a. **Niche manipulation system** — a polished, reliable multi-step task on sub-$300 hardware; full repo + video + writeup.
13b. **The EE-fusion project** — a robot that performs a physical EE/bench task, or a deep dive on the **power/actuator/embedded reliability** layer (your moat); ties Physical AI back to your [[Wide Bandgap Semiconductors|power]] identity.
13c. **FURI research** — formalize 13a/13b into an ASU Fulton Undergraduate Research proposal with a faculty mentor.

## Rules (same as the EE ladder)

- **Finish before perfect.** A janky working pick-and-place beats a beautiful unfinished one.
- **One public artifact per rung** — repo, dataset, or video.
- **Write the failure log.** The sim-to-real and calibration headaches you document *are* the differentiated content; everyone has the happy-path demo.
- **Don't skip Tier 2.** Real hardware is the whole point — it's where the EE edge and the 2026 reliability bottleneck live.

## See Also

- [[Physical AI Build Guide (Roadmap for Joe)]] — the phase-by-phase learning plan behind these projects
- [[Python EE Project Ladder]] — the sibling ladder for Python/EE
