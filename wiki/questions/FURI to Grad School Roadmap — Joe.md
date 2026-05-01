---
type: question
title: "FURI to Grad School Roadmap — Joe"
created: 2026-05-01
updated: 2026-05-01
status: active
tags:
  - FURI
  - grad-school
  - WBG
  - power-electronics
  - ASU
  - roadmap
  - Joe
---

# FURI to Grad School Roadmap — Joe

## Goal
Get accepted into a top MS EE program (NC State MS-WBGS or VT CPES) via a strong WBG research track starting from Year 1 at ASU.

---

## The Three Faculty — Simplified for Joe's Interests

Joe's interests: WBG hardware (SiC/GaN), miniaturized converters, gate drivers, EV OBC, double pulse testing, Python/LTspice simulation.

### Mike Ranjram — **Most Relevant**
**Top research for Joe**: ML-CEMS fixed-frequency gain control (ECCE 2024)

The core idea in one sentence: instead of sweeping frequency to change the output voltage of an LLC converter (which bloats the magnetics), inject multi-level transformer voltages at fixed frequency to get the same gain range — keeping peak flux at 66 mT instead of 231 mT.

Why it matters for Joe's interests:
- It's a hardware paper with a clear physical result (flux density numbers, not just equations)
- It combines topology + magnetics + control — the exact overlap of WBG power electronics
- The open future-work (closed-loop control, variable passives) is FURI-scope
- The MAPEL GitHub repo (MHzCoreLossAggregateDataset) is a direct on-ramp: real data, real ferrites, real MHz operation

**What Joe should do with this now**: Read the ML-CEMS paper, compute the gain relation, and ask Ranjram about the closed-loop control problem at office hours.

### Raja Ayyanar — **Useful for Context, Not Joe's Primary Hardware Track**
**Top research for Joe**: "High Frequency Power Converters for Electric Vehicles" (EVSTS project)

The visible recent papers (feeder PV hosting capacity, volt-PF control) are grid/controls work, not hardware. Ayyanar's hardware thread — high-density EV dc/dc using WBG — exists but is less publicly documented. His value for Joe is:
- Industry connections (EVSTS has OEM + utility partners)
- EV application context for converter hardware
- Senior professor = more name recognition in SOP

**What Joe should do with this**: Keep Ayyanar as a second-priority mentor option. If Ranjram is full or unresponsive, pursue Ayyanar next. If you end up with Ayyanar, focus the FURI proposal on the EV converter hardware thread explicitly.

### Yuji Zhao — **Not an ASU Option; Know His Work for Grad School Context**
**Top research for Joe**: BN interlayer engineering for GaN/Ga₂O₃ reliability

Zhao is at Rice, so not a FURI mentor. But his research is directly relevant context:
- Process engineering can dramatically improve GaN reliability (trap density, TDDB lifetime)
- The BN interlayer trick (2.8 nm layer → +41% breakdown voltage on β-Ga₂O₃) is the kind of physical insight that shows up in WBG power electronics papers about device reliability
- If Joe pursues grad school at Rice or a program with UWBG device physics, Zhao's group is a target

**What Joe should do with this**: File for future reference. Not actionable for FURI. Read the two-step recess paper when studying GaN device physics (Year 2–3 context).

---

## Year-by-Year Roadmap

### Year 1 (Now → May 2027) — Build the Foundation
**Goal**: Arrive at FURI application time with skills and a faculty relationship.

**Semester 1–2 (now)**:
- [ ] Read the ML-CEMS paper (ECCE 2024) — understand the gain relation and the flux comparison table
- [ ] Read the HPPC paper (2025) — understand why single-stage ac/dc matters
- [ ] Clone MAPEL GitHub MHzCoreLossAggregateDataset — explore the schema
- [ ] Complete LTspice 10-circuit ladder (voltage divider → buck converter); simulate an LLC converter
- [ ] Python Phase 0–1: Ohm's Law CLI → NumPy → scipy.signal Bode plots → push to GitHub
- [ ] Join IEEE ASU + Solar Devils electrical sub-team Week 1
- [ ] Visit Ranjram office hours 2–3× (Month 2–3 of first semester); express specific interest in ML-CEMS or core-loss dataset
- [ ] Visit Ayyanar office hours once (Month 3–4) as fallback relationship

**October 2026 (critical)**:
- [ ] Apply for LLNL 2027 summer internship (apply Oct 2026, target Summer 2027)

### Year 2 (May 2027 → May 2028) — FURI + Lab Entry
**Goal**: Secure FURI mentorship under Ranjram; produce a research poster.

**Spring 2027 (FURI application window: ~October 2026)**:
- [ ] Submit FURI Spring 2027 application with Ranjram as mentor
  - Research proposal: pick one of (1) closed-loop HPPC, (2) core-loss dataset surrogate model, (3) self-resonance-aware planar magnetics
  - Personal statement: connect WBG interest → ML-CEMS paper → specific FURI problem
  - Write entirely yourself — FURI explicitly bans AI-generated application content

**During FURI semester**:
- [ ] Execute the FURI project (one semester, one clear result)
- [ ] Build the Fulton Forge poster (23" × 35"; Introduction | Methods | Results | Conclusions)
- [ ] Present at Fulton Forge Expo → this is a named research deliverable for your CV and SOP

**Summer 2027**:
- [ ] If LLNL internship secured: power electronics or semiconductor group; mention FURI project in interview
- [ ] If not: target Tri-Valley employers (Lam Research, local EE positions) + continue lab work

### Year 3 (May 2028 → May 2029) — Deepen Research + Grad School Prep
**Goal**: Second research semester (FURI again or MORE); build MS application profile.

- [ ] Apply for a second FURI semester OR MORE (graduate-equivalent research stipend)
- [ ] Target a conference submission (ECCE, APEC, or COMPEL) — even a poster or workshop abstract is a publication line
- [ ] Complete EE core coursework: EEE 202 Circuits, EEE 334 Electronic Circuits, EEE 350 Signals/Systems
- [ ] Start device physics (Neamen) alongside EEE 480 or equivalent WBG-adjacent courses
- [ ] Take Control Systems (EEE 482 or similar) — required for any converter control work
- [ ] Build the GRE-replacement profile: most MS programs (NC State, VT CPES) are GRE-optional — focus on GPA + research
- [ ] Target GPA ≥ 3.5 (minimum competitive target for VT CPES; NC State WBG needs ≥ 3.0 minimum, competitive ≥ 3.3+)
- [ ] Join IEEE PES chapter (power/energy networking, WBG career-aligned)
- [ ] Target HKN Eta Kappa Nu (top 1/4 sophomore GPA threshold — IEEE honor society, sends resume to industry)

### Year 4 (Senior Year) — Grad School Applications
**Goal**: Submit strong MS applications with named faculty, research abstract, and named letter.

**September–December (application season)**:
- [ ] Identify specific faculty at NC State MS-WBGS (PowerAmerica-affiliated professors) and VT CPES (name one specifically in SOP)
- [ ] Email target graduate faculty BEFORE submitting applications — same formula as Ranjram approach
- [ ] Request letter from Ranjram: should reference your specific project, named results, and your readiness for graduate research
- [ ] Write Statement of Purpose: research narrative (FURI project → specific result → open question you'd pursue in grad school); name faculty; name their specific work; keep it to 1–2 pages
- [ ] Apply: NC State MS-WBGS (priority #1) + VT CPES (priority #2) + Purdue MEng/online (safe option)

**Why this chain works**:
- FURI under Ranjram → named WBG research letter → research abstract in SOP
- Ranjram → PowerAmerica connections → NC State MS-WBGS (PowerAmerica has 49 WBG industry members)
- NC State MS-WBGS → LLNL/Sandia collaboration pipeline → Livermore career plan

---

## Key Numbers to Hit
| Metric | Minimum | Competitive |
|--------|---------|-------------|
| GPA | 3.0 | 3.5+ |
| Research semesters | 1 (FURI) | 2+ |
| Named letters | 1 (Ranjram) | 2 |
| Conference submissions | 0 | 1+ |
| GitHub repositories | 3 | 10+ |
| Industry internship | — | LLNL 2027 |

---

## Related Pages
- [[FURI Program Complete Guide]]
- [[Mike Ranjram]]
- [[Raja Ayyanar]]
- [[MS EE Programs Power Electronics Semiconductors]]
- [[Research - MS EE Programs Acceptance Rates]]
- [[EE High Income Action Plan]]
- [[Research - Power Electronics UWBG Faculty Scan 2026]]
