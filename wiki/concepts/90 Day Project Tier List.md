---
type: concept
title: "90 Day Project Tier List"
status: complete
created: 2026-05-03
updated: 2026-05-03
tags:
  - projects
  - 90-day
  - planning
  - execution
  - tier-list
  - engineering
  - personal-development
---

# 90-Day Project Tier List

Projects and initiatives ranked by **ROI over a 90-day execution window** — measured by: career leverage, compounding potential, alignment with Joe's actual goals, and scope-fit for 90 days.

**Key insight**: Joe's vault shows extensive research and planning. The 90-day challenge is *execution*. The best projects are ones with a concrete deliverable at day 90 and daily accountability built in.

**Scope rule**: A 90-day project must have (1) a clear deliverable at day 90, (2) a daily or weekly action, and (3) no more than 2 hrs/day of work. Projects that fail this test aren't projects — they're vague goals.

---

## S-Tier — Highest Leverage, Build This First

| Project | Deliverable at Day 90 | Daily Load | Why It's S-Tier |
|---------|----------------------|------------|-----------------|
| **FURI Faculty Outreach + Research Proposal** | Draft FURI proposal, relationship with Ranjram or Ayyanar | 30 min/day avg | This is Joe's #1 career move. October FURI deadline = ~5 months. The groundwork must be done in summer. |
| **Buck Converter Build (STM32 + PCB)** | Working synchronous buck converter with PWM control | 60–90 min/day | FURI-ready portfolio artifact. Directly maps to [[Mike Ranjram]]'s MAPEL lab work. Only EE project that counts at a FURI interview. |
| **MIT 18.06 OCW Linear Algebra (Strang)** | 34 lectures + problem sets completed | 30–40 min/day | Direct Fall 2026 MAT 343 prep. Most EE-applicable math after calculus. Free. |

### S-Tier Project 1: FURI Faculty Outreach + Research Proposal

**Why it's S-tier**: Most undergrads who get FURI spend summer building the relationship. Joe's October deadline means August is the right time to finalize the proposal. Starting in May = 5 months of runway.

**Phase plan (90 days)**:
- Weeks 1–3: Read 3–5 recent papers by Ranjram (MAPEL, MHz magnetics, ML-CEMS) and 2–3 by Ayyanar (EV/PV grid control). Write 1-page summary of each.
- Week 4: Draft cold email — one specific question tied to one specific paper, plus 2-sentence background.
- Weeks 5–8: Follow up, attend any lab meetings or office hours. Build familiarity.
- Weeks 9–12: Draft FURI proposal using ASU template. Have mentor review.

**Key facts**:
- FURI applications close the 3rd Wednesday of October for Spring; the 3rd Wednesday of March for Summer/Fall
- Faculty look for: clear research question, authenticity, alignment, strong academic standing
- Cold emails that reference a specific paper result in 3–5× higher response rates than generic requests
- Reference: [[FURI Program Complete Guide]], [[Research - FURI Program ASU Full Guide]]

---

### S-Tier Project 2: Buck Converter Build

**Why it's S-tier**: A physical working hardware project is the *only* thing that separates two FURI applicants with the same GPA. It shows self-initiative, domain knowledge, and hands-on capability.

**Phase plan (90 days)**:
- Weeks 1–3: STM32 fundamentals — GPIO, PWM generation with Timer (TIM1/TIM8), ADC for feedback. Use STM32 Nucleo board. Complete 5 basic embedded exercises.
- Weeks 4–6: Design synchronous buck converter schematic in LTspice first (simulate → verify). Key specs: Vin = 12V, Vout = 5V, 1A, switching at 100 kHz. Gate driver selection (bootstrap or isolated).
- Weeks 7–9: Build on breadboard first, then transfer to KiCad-designed PCB (outsource fabrication to JLCPCB ~$10 for 5 boards). Measure efficiency, ripple, transient response.
- Weeks 10–12: Document with a short technical report (3–5 pages): schematic, Bode plot of control loop, measured waveforms, lessons learned. Post to GitHub.

**Resource stack**: LTspice (free) → STM32 Nucleo ($15) → Buck converter components (~$25) → KiCad (free) → JLCPCB ($10–$20) → oscilloscope (borrow from ASU lab if needed)

**See also**: [[Laplace Transform in Circuit Analysis]], [[Transfer Functions and Poles Zeros]], [[C++ Self-Teaching Roadmap for EE]], [[EE Freshman Action Plans]]

---

### S-Tier Project 3: MIT 18.06 Linear Algebra

**Why it's S-tier**: MAT 343 (Applied Linear Algebra) is Fall 2026. 90 days starting May = completed by early August, 2 months before class starts. Linear algebra is the math backbone of: signal processing, control systems, machine learning, power systems (Y-bus), and Fourier analysis.

**Phase plan (90 days)**: 34 lectures × ~1 hr each = 34 hrs. At 25 min/day video + 15 min problem sets = 40 min/day → done in 85 days.

**Resource**: MIT OCW 18.06 (Strang, free), *Introduction to Linear Algebra* 5th ed., 3Blue1Brown *Essence of Linear Algebra* (visual intuition, watch first)

**Milestone checkpoints**:
- Week 3: Gaussian elimination, row echelon form
- Week 6: Vector spaces, null space, column space
- Week 9: Orthogonality, Gram-Schmidt, least squares
- Week 12: Eigenvalues/eigenvectors, SVD

**See also**: [[MAT 343 Applied Linear Algebra — Topics and Prep]]

---

## A-Tier — High ROI, Strong Complement to S-Tier

| Project | Deliverable at Day 90 | Daily Load | Why A-Tier |
|---------|----------------------|------------|------------|
| **Python EE Project Ladder — Phase 0–3** | 12 working Python tools (Ohm's Law → PID buck simulator) | 45–60 min/day | Builds the software side of the FURI portfolio; bridges EE theory to code |
| **Progressive Overload Training Program** | Completed beginner strength program; measurable strength gains | 45–60 min, 3×/week | Meta-keystone habit; boosts testosterone, HGH, dopamine, focus. Everything else gets easier. |
| **Open Roth IRA + Automate Contributions** | Roth IRA open, $50–100/month automated | One-time 2 hr setup | His own research: Roth IRA at 19 = ~$500k at retirement. This is the highest-ROI single action that takes 2 hours, not 90 days. |
| **Cold Email 30 Engineers in Power Electronics** | 30 cold emails sent, 5+ replies, 2+ conversations | 3 emails/week | Professional network is the hidden multiplier. Gets internship/FURI leads. |

### A-Tier: Python EE Project Ladder Phase 0–3

Joe already has the roadmap mapped at [[Python EE Project Ladder]]. The 90-day execution:
- Projects 1–6 (Phase 0–1): Ohm's Law → RC transient → RLC → Bode plot
- Projects 7–13 (Phase 2–3): FFT analyzer → FIR filter → PID tuner → closed-loop buck simulator
- Pacing: ~1 project/week = 12 projects in 12 weeks

This directly produces GitHub-hostable code that complements the hardware Buck Converter project. Together they form a complete EE portfolio.

### A-Tier: Progressive Overload Training

**Evidence base**: From [[Human Hormones Complete Guide]] — resistance training 3–4×/week raises testosterone, HGH (pulse quality), insulin sensitivity, dopamine baseline, and focus. It is the most effective single lifestyle lever.

**Program options**:
- *Starting Strength* (Rippetoe) — 3×5, squat/press/deadlift, simplest, fastest strength gains
- *StrongLifts 5×5* — free app, same approach
- Pacing: 3 sessions/week, 45–60 min each = 12 weeks = one complete beginner block

**Measurable at day 90**: +30–50% on squat and deadlift 1RM from baseline (typical beginner gains).

### A-Tier: Open Roth IRA

This is a one-time action, not a daily project — but it belongs in the 90-day window because compound interest starts on day 1.

**Action checklist** (2 hrs):
1. Open Fidelity or Vanguard Roth IRA (free)
2. Fund with $100 initial deposit
3. Set up automatic monthly transfer ($50–100)
4. Invest in a single target-date index fund (e.g., FXIFX or VTTSX)
5. Done. Never touch it.

At $100/month starting at 19, invested at 8% avg annual return = **~$525,000 at age 65**. Every month delayed costs ~$5,000–$10,000 in final value due to compounding.

---

## B-Tier — Good ROI, Best Run in Parallel with S/A Projects

| Project | Deliverable at Day 90 | Daily Load | Notes |
|---------|----------------------|------------|-------|
| **KiCad PCB Design (learn + build 1–2 simple boards)** | 2 designed PCBs (fabricated or simulation-only) | 20 min/day | Required for Solar Devils BMS, SDS CubeSat, FURI-grade projects |
| **Catholic Daily Prayer Stack** | Established daily prayer + Lectio Divina habit | 20–35 min/day | From [[Catholic Spiritual Growth Steps]] — S-tier foundation: 15-min morning prayer + Sunday Mass + monthly Confession |
| **Read *Imitation of Christ* (Kempis)** | Book completed | 15 min/day | 90 days of slow prayerful reading. First book on the Catholic spiritual reading ladder. |
| **Technical Blog (GitHub Pages or Substack)** | 12 published posts | 20 min/day | Public portfolio artifact. Documents the EE + Python learning. Writing is the multiplier. |
| **Spanish via Language Transfer** | Language Transfer complete (40 lessons) | 25 min/day | Free audio. No textbook. ~20 hrs total. Latin-language base for international research opportunities. |

---

## C-Tier — Lower ROI or Too Broad for 90-Day Scope

| Project | Why C-Tier |
|---------|-----------|
| **Full Calculus III self-study** | PHY 131 E&M prep is better scoped per [[Fall 2026 Summer Study Plan — Joe]]; too broad as standalone project |
| **Learn Altium PCB Design** | Better after KiCad. SDS uses Altium but KiCad first builds the foundations. |
| **Learn MATLAB** | Required for MAT 343; but MIT 18.06 + Python covers the same ground more durably |
| **General "learn AI/ML"** | Too diffuse. No single deliverable. Better as reading + podcasts alongside structured projects. |
| **Write a technical paper** | Premature without a research project (i.e., FURI first). |

---

## F-Tier — Avoid as 90-Day Projects

| Project | Why It Fails |
|---------|-------------|
| **YouTube / social media channel** | Meta-work dominates; content doesn't compound like skills. Build the portfolio first. |
| **Cryptocurrency / trading** | High time-sink, speculative, not career-relevant for EE |
| **"Read 30 books"** | Reading without output (notes, summary, application) = low retention. Quality > quantity. |
| **Another research rabbit hole** | Joe's vault has extensive research. The constraint is now execution, not research. |

---

## Joe's Recommended 90-Day Execution Stack

**Primary projects** (run in parallel, complement each other):

| Priority | Project | Daily time | Deliverable |
|----------|---------|------------|-------------|
| #1 | MIT 18.06 Linear Algebra | 40 min/day | 34 lectures + problem sets done |
| #2 | Buck Converter Build | 60–90 min/day | Working hardware + GitHub documentation |
| #3 | FURI Faculty Outreach | 30 min/day avg | Draft proposal + faculty relationship |
| #4 | Python EE Project Ladder P0–3 | 45 min/day | 12 working EE Python tools |

**Habit systems** (not "projects" — run daily in background):

| Habit | Time |
|-------|------|
| Cold shower | 3 min |
| Progressive overload training | 45–60 min × 3/week |
| Catholic morning prayer | 15 min |
| "What did I avoid today?" journal | 5 min |

**One-time actions** (do in Week 1):

| Action | Time |
|--------|------|
| Open Roth IRA + automate | 2 hrs |
| Cold email Ranjram with paper-specific question | 30 min |

---

## Key Principles for 90-Day Success

1. **One primary project wins over five parallel projects** — cognitive load is real. If you must choose, Buck Converter + MIT 18.06 + FURI outreach is the stack. Python Ladder is the supplement.
2. **Measure weekly, not daily** — weekly check-ins: "Did I hit my project milestones this week?" beats tracking every day.
3. **The vault is the enemy** — more research without execution is comfort-seeking. Joe knows more than enough to start. The constraint is now doing.
4. **Compound the deliverable** — every project should produce something that persists: GitHub commit, a page in the wiki, a sent email, a built circuit. No output = no project.

---

*See also*: [[Research - 90 Day Project Ideas]], [[FURI to Grad School Roadmap — Joe]], [[EE Freshman Action Plans]], [[Python EE Project Ladder]], [[Fall 2026 Summer Study Plan — Joe]], [[Comfort Zone Habits Tier List]], [[Human Hormones Complete Guide]]
