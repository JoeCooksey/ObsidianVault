---
type: meta
title: "Wiki Index"
updated: 2026-05-03T00:00:00
tags:
  - meta
---
# Wiki Index

Master catalog of all wiki pages. Update on every ingest.

## Domains
- [[Engineering]] — software, systems, hardware, power electronics (6 sources, 2 syntheses)
- [[Mathematics]] — pure math, applied math, statistics (0 sources)
- [[Books]] — literature, non-fiction, key ideas from reading (2 sources, 13 book list pages)
- [[Research]] — deep-dive research topics and synthesis (2 syntheses)
- [[Theology]] — Bible study, theology, apologetics (0 sources)

## Entities
- [[Mike Ranjram]] — ASU MAPEL; converter architecture + MHz magnetics; ML-CEMS (flux 231→66 mT) + HPPC; Joe's #1 FURI target
- [[Raja Ayyanar]] — ASU EVSTS; EV/PV/WBG/grid control; senior faculty; Joe's #2 FURI target
- [[Yuji Zhao]] — Rice WIDE Lab (formerly ASU); GaN/β-Ga₂O₃ device physics; BN interface engineering; not FURI-eligible
- [[Stephen Covey]] — *The 7 Habits of Highly Effective People* (1989); Maturity Continuum; Character Ethic; 40M+ copies sold
- [[James Clear]] — *Atomic Habits* (2018); Four Laws of Behavior Change; 3M+ newsletter subscribers; ⭐⭐⭐⭐⭐ (Joe)
- [[Dale Carnegie]] — *How to Win Friends and Influence People* (1936); human relations training pioneer; 30M+ copies sold
- [[Keith Ferrazzi]] — *Never Eat Alone* (2014); generosity-first networking; RAP, pinging, follow-up formula; ⭐⭐⭐⭐⭐ (Joe)
- [[Andrew Huberman]] — Professor of Neurobiology, Stanford; Huberman Lab; coined Limbic Friction
- [[Wendy Wood]] — habit researcher; "Psychology of Habit" (*Annual Review of Psychology*)
- [[Susan David]] — Harvard psychologist; *Emotional Agility* (2016); Institute of Coaching co-founder
- [[Lawrence Livermore National Laboratory]] — DOE national security lab in Livermore, CA; undergrad summer internships; apply Oct–Jan; ~8,000 staff
- [[IEEE ASU Student Branch]] — 600+ member networking org; "Dinner With Engineers" with Boeing/TI/Honeywell/Intel; S-tier for EE networking
- [[Solar Devils ASU]] — solar-powered EV build club; electrical sub-team does battery pack + BMS + MPPT; S-tier project club for WBG track
- [[Sun Devil Satellite Laboratory]] — CubeSat + Altium PCB design; Northrop/Lockheed partnerships; S-tier project club
- [[HKN Eta Kappa Nu ASU]] — IEEE honor society for EE/CE; invitation-based; resume distribution to industry; A-tier
- [[Tau Beta Pi ASU]] — pan-engineering honor society; top 1/8 junior GPA; $10k fellowships; grad school recruiting; A-tier
- [[IEEE PES ASU Chapter]] — Power and Energy Society sub-chapter; WBG/power electronics networking; A-tier
- [[Sun Devil Semiconductor Club]] — semiconductor-focused student org (Sun Devil Central ID 36278); directly WBG/IC design-aligned; details pending; A-tier provisionally
- [[Intel]] — invented x86 ISA (1978); multi-core transition (2006)
- [[AMD]] — 64-bit x86 transition (2003); chiplet architecture (2019); Ryzen AI Max APU (2025)
- [[NVIDIA]] — coined "GPU" (1999); CUDA (2007); NVLink 5 at 1.8 TB/s (2024); electrons→tokens; 5-layer cake
- [[Jensen Huang]] — NVIDIA CEO/co-founder; "electrons→tokens"; five-layer cake; "do as much as needed, as little as possible"
- [[Dwarkesh Patel]] — podcaster; long-form interviews on AI, tech, science
- [[BitNet]] — Microsoft ternary LLM architecture and CPU inference framework
- [[llama.cpp]] — dominant C/C++ edge LLM inference engine (Georgi Gerganov)
- [[MLC-LLM]] — TVM-based universal LLM deployment engine
- [[Wolfspeed]] — largest SiC wafer manufacturer; 62% market share (2025)
- [[STMicroelectronics SiC]] — Tesla Model 3 SiC supplier; automotive SiC leader

## Concepts

### AI / Edge Computing
- [[Post-Training Quantization]] — INT4/INT8/FP8 weight and activation quantization (developing)
- [[GGUF Format]] — llama.cpp quantization file format; Q4_K_M recommended (developing)
- [[LLM Pruning]] — structured/unstructured sparsity; SparseGPT, Wanda (developing)
- [[Knowledge Distillation for Edge LLMs]] — small student models from large teachers (developing)
- [[Speculative Decoding]] — EAGLE, Medusa; 2–3.6× decoding speedup (developing)

### Self-Teaching / Lifelong Learning
- [[Self-Teaching Topics Tier List]] — S–C tier list of 18 subjects ranked by life ROI × self-teachability; S-tier: Math/Finance/Programming/Logic; full textbook recommendations per subject; Joe's 90-day priority stack (complete)
- [[Podcast Learning Tier List]] — S–C tier list of 20+ podcasts ranked by learning density × signal-to-noise; S-tier: Huberman Lab, Hardcore History, Lex Fridman, Dwarkesh; domain best-picks table; Joe's listening stack (complete)
- [[Research - Top Learning Podcasts]] — 8-finding synthesis: long-form beats short-form, Philosophize This! as best philosophy audio resource, Dwarkesh rise, Hardcore History as S-tier history, economics podcast taxonomy, AI podcast split; full tier table + sources (complete)

### EE Topic Depth Map
- [[EE Topic Depth Priority Map]] — 6-level leverage stack for first-year EE student targeting WBG power: Circuit Theory → Digital Logic → Semiconductor Devices → Signals/Laplace → Control → EM; year-by-year targets (developing)

### EE Core Curriculum Topics
- [[Circuit Theory Fundamentals]] — KVL/KCL, nodal/mesh analysis, Thevenin/Norton, AC phasors, impedance, RLC transients, op-amps, power — the bedrock of all EE (developing)
- [[Signals and Systems — Laplace and Fourier]] — Fourier Series/Transform, Laplace Transform, transfer functions, poles/zeros/stability, Bode plots, convolution, Z-transform — most powerful EE mathematical framework (developing)
- [[Semiconductor Device Fundamentals]] — p-n junction, diode I-V, BJT modes, MOSFET I-V, power MOSFET body diode, IGBT, SiC vs GaN physics — gateway to WBG power electronics (developing)
- [[Digital Logic and Boolean Algebra]] — Boolean algebra, De Morgan's laws, K-maps, combinational circuits, D flip-flops, FSMs, intro Verilog — prerequisite for EEE 120 and FPGA career track (developing)

### Laplace Transform Deep Dive (2026-05-03)
- [[Laplace Transform — Mathematical Foundations]] — definition, complex $s$-plane, ROC, all key properties, transform pairs table, inverse Laplace via partial fractions, connection to Fourier (developing)
- [[Laplace Transform in Circuit Analysis]] — s-domain impedances ($Z_R=R$, $Z_C=1/sC$, $Z_L=sL$), IC source terms, 3 worked examples (RC/RLC/RL), transfer function forms, buck converter small-signal application (developing)
- [[Transfer Functions and Poles Zeros]] — poles/zeros definition, s-plane stability map, $\zeta$/$\omega_n$, Bode plot construction rules, gain/phase margin, Python code (developing)
- [[Research - Laplace Transforms and Electrical Engineering]] — 8-finding synthesis: core insight, complex $s$, impedances, poles, Bode, control design, power electronics, partial fractions; ASU curriculum map; key formulas (complete)
- [[Research - Self-Teaching Topics Tier List]] — 8-finding synthesis: mathematics ROI, logic as meta-skill, personal finance compounding, writing as multiplier, economics worldview, Stoicism OS, statistics literacy, history as pattern recognition; complete tier list + 90-day stack (complete)

### Fall 2026 Upcoming Coursework
- [[EEE 202 Circuits I — Topics and Prep]] — 8-unit topic map (KVL/KCL → Laplace); Vasileska/Myhajlenko; Irwin textbook; best prep resources; overlap with PHY 131 (developing)
- [[MAT 343 Applied Linear Algebra — Topics and Prep]] — 10-unit topic map; MATLAB required; EE applications of eigenvalues/SVD; prep stack: 3B1B + MIT 18.06 (developing)
- [[PHY 131 University Physics II EM — Topics and Prep]] — 16-unit E&M topic map; Qing/Reaves; Young & Freedman 15th ed; 40% topic overlap with EEE 202 (developing)
- [[Fall 2026 Summer Study Plan — Joe]] — 3-phase 16-week schedule (May–Aug); weekly deliverables; resource quick-reference; synergy table (developing)
- [[Research - Fall 2026 Course Prep Plan]] — synthesis: full prep strategy, cross-course synergy table, open questions (complete)

### Math and Physics Foundations for EE
- [[Calculus in Electrical Engineering]] — Calc 1-3 mapped to EE: derivatives for V-I relations, integrals for energy/RMS/Fourier, vector calc for Maxwell (developing)
- [[Differential Equations in Electrical Engineering]] — RC/RL/RLC ODEs, Laplace/transfer functions, control systems, wave equation (developing)
- [[Classical Mechanics in Electrical Engineering]] — mechanical-electrical analogy, motor/generator dynamics, MEMS, vibration-to-resonance (developing)
- [[Electromagnetism Foundations for EE]] — Gauss/Faraday/Ampere/Lorentz mapped to components, transformers, motors, antennas (developing)

### Grad School / MS EE Programs
- [[MS EE Programs Power Electronics Semiconductors]] — quick-reference tier list: NC State WBG, VT CPES, UT Austin SSE, Purdue, MIT/Stanford/Berkeley (developing)

### Programming Languages for EE
- [[Python in Electrical Engineering]] — PyVISA (ATE control), python-control (Bode/rlocus/PI design), PyLTSpice, SciPy signal processing, cocotb FPGA verification (developing)
- [[C++ in Electrical Engineering]] — embedded firmware, TI C2000 PI control at 100 kHz, FreeRTOS, MISRA-C, ARM CMSIS-DSP, FOC motor control (developing)
- [[Python Self-Teaching Roadmap for EE]] — 4-phase roadmap: Python basics → NumPy/SciPy → control systems → PyVISA + PyLTSpice → advanced track (developing)
- [[C++ Self-Teaching Roadmap for EE]] — 5-phase roadmap: C fundamentals (K&R) → Arduino → STM32 HAL → FreeRTOS → TI C2000 digital power (developing)
- [[Python EE Project Ladder]] — **master 20-project roadmap**: pure Python → NumPy/Matplotlib → SciPy → python-control → PyLTSpice → PyVISA → cocotb/DPT (developing)
- [[Python EE Project Ladder - Phase 0-1]] — Projects 1–6: Ohm's Law Calculator through RLC transient simulator; full code for each (developing)
- [[Python EE Project Ladder - Phase 2-3]] — Projects 7–13: Bode plots, FFT analyzer, FIR/IIR filter designer, PID tuner, closed-loop buck simulator; full code (developing)
- [[Python EE Project Ladder - Phase 4-5]] — Projects 14–19: PyLTSpice parametric sweep + Monte Carlo + efficiency, PyVISA I-V + scope capture + auto Bode; full code (developing)
- [[Python EE Project Ladder - Advanced Tracks]] — Project 20+: Track A (cocotb Verilog testbench) or Track B (double pulse test DPT analyzer); full code (developing)

### Programming in the AI Era
- [[AI-Assisted Programming Learning Roadmap]] — 5-phase AI-native learning roadmap: fundamentals → Git/debugging → AI tool onboarding → real projects → systems thinking (developing)
- [[Programming Skills AI Cannot Replace]] — architecture, domain knowledge, debugging instinct, code review taste, security mindset, communication (developing)

### Power Electronics Faculty + Grad School Roadmap
- [[FURI to Grad School Roadmap — Joe]] — 4-year roadmap: Year 1 skills → Year 2 FURI under Ranjram → Year 3 second research term + grad prep → Year 4 NC State/VT CPES applications; key metrics table (developing)
- [[Research - Power Electronics UWBG Faculty Scan 2026]] — faculty scan of Ranjram/Ayyanar/Zhao; simplified for Joe's WBG interests; critical correction: Zhao is at Rice not ASU (complete)

### ASU Research Programs
- [[FURI Program Complete Guide]] — complete quick-reference: eligibility, deadlines, application checklist, poster specs, faculty mentor table, Joe's action timeline (developing)
- [[Research - FURI Program ASU Full Guide]] — full research synthesis: all application components, 7 research themes, faculty cold-email formula, semester timeline, grad-school connection (developing)
- [[ASU EE Mentorship Pathways]] — all mentorship channels ranked (peer mentor → FURI → IEEE → Barrett alumni) (developing)
- [[Research - EE Mentorship at ASU]] — full mentorship research: faculty contacts, cold email formula, Year 1 action stack (developing)

### Power Electronics / EV / Career
- [[EE Physical Side — Actionable Skill Plan]] — 18-month roadmap: device physics → converter design → WBG specialization → digital control (developing)
- [[ASU EE Year 1-2 Curriculum Map]] — term-by-term course sequence; no EE courses until Term 3A; Year 1 = math+physics gap to exploit (developing)
- [[EE Freshman Self-Study Stack]] — Tier 1–3 self-study tools: LTspice, Python, breadboard, Git, MATLAB, Arduino, KiCad (developing)
- [[EE Freshman Portfolio Strategy]] — GitHub portfolio approach, project tiers by year, ASU clubs (FURI, Solar Car, IEEE) (developing)
- [[EE Freshman Action Plans]] — 6 ordered action plans: math mastery, LTspice, Python, breadboard, Git, Arduino; 6-month timeline (developing)
- [[LTSpice Complete Skills Guide]] — Full reference: 4 simulation types, 10-circuit ladder, SPICE directives, op-amp, power electronics, Monte Carlo, model import (developing)
- [[Wide Bandgap Semiconductors]] — SiC vs GaN vs Ga₂O₃ material comparison (developing)
- [[Silicon Carbide Power Electronics]] — traction inverters, DCFC, OBC; 800V systems (developing)
- [[Gallium Nitride Power Electronics]] — OBC focus; 1200V roadmap; V2G enabler (developing)
- [[Gallium Oxide Power Electronics]] — ultra-wide bandgap; research stage; thermal barrier (seed)
- [[800V EV Architecture]] — forces SiC adoption; 350kW charging; market trajectory (developing)
- [[EV Fast Charging Topologies]] — totem pole PFC, CLLC, DAB; efficiency numbers (developing)
- [[V2G Bidirectional Charging]] — WBG enables bidirectional OBCs; grid integration (seed)
- [[WBG Thermal Management]] — junction temperature, failure modes, cooling strategies (developing)

### Computer Architecture / CPU+GPU
- [[CPU Architecture Evolution]] — scalar → superscalar → multi-core → heterogeneous SoC (developing)
- [[GPU Architecture Evolution]] — fixed-function → programmable shaders → GPGPU → AI accelerator (developing)
- [[Moore's Law and Dennard Scaling]] — transistor scaling laws + breakdown ~2005 + consequences (developing)
- [[Heterogeneous Computing]] — CPU/GPU division of labor; latency vs throughput optimization (developing)
- [[CUDA Programming Model]] — host/device/kernel model; NVIDIA's compute platform (2007) (developing)
- [[GPU Interconnects]] — PCIe vs NVLink vs CXL; bandwidth hierarchy table (developing)
- [[Unified Memory Architecture]] — Apple Silicon M-series, AMD Ryzen AI Max; shared memory pool (developing)
- [[Accelerated Computing]] — Nvidia's mission; domain-specific acceleration beyond AI (developing)
- [[CUDA Ecosystem Flywheel]] — install base + programmability + ecosystem richness → self-reinforcing moat (developing)
- [[GPU vs TPU Trade-offs]] — programmability vs specialization; ecosystem vs efficiency (developing)
- [[AI Five-Layer Cake]] — Jensen Huang's framework: energy → chips → platform → models → applications (developing)

### Intelligence Enhancement (EQ + IQ)
- [[EQ-IQ-Enhancement-Guide]] — master framework: definitions, trainability, evidence summary, combined tier list, Joe's priority stack (complete)
- [[IQ-Enhancement-Tier-List]] — S–D tier list: dual n-back, sleep, exercise, education, chess, nutrition, brain training apps; expected gains and evidence quality for each (complete)
- [[EQ-Enhancement-Tier-List]] — S–D tier list: therapy/CBT, journaling, mindfulness, empathy practice, affect labeling, fiction reading, volunteering; mechanisms for each (complete)
- [[Combined-EQ-IQ-Tier-List]] — high-ROI activities that develop both IQ and EQ simultaneously; S–D ranking; Joe's optimal daily stack (complete)

### Psychology / Emotional Intelligence
- [[Emotional Agility]] — compassionate, curious, courageous relationship with thoughts/emotions/stories (developing)
- [[Emotional Rigidity]] — fusion with thoughts/emotions/stories; drives action away from values (developing)
- [[Gentle Acceptance]] — end the struggle with whether you're "allowed" to feel; stop Type 2 emotion loops (developing)
- [[Emotion Granularity]] — precise labeling activates brain's readiness potential; "stressed" → "disappointed" (developing)
- [[Defusion Language]] — "I notice I feel X" vs "I AM X"; sky/cloud metaphor; restores space for choice (developing)
- [[Toxic Positivity]] — cultural suppression of difficult emotions causes burnout and lower resilience (developing)
- [[Emotions as Functional]] — Darwin: emotions are adaptive signals pointing to values and needs (developing)

### Neuroscience / Habits
- [[Limbic Friction]] — activation energy to override anxious/lethargic states (developing)
- [[Task Bracketing]] — dorsal lateral striatum; start+end neural fingerprint of habits (developing)
- [[Neuroplasticity and Habit Formation]] — habits as neural circuits; hippocampus → basal ganglia migration (developing)
- [[Habit Strength]] — context independence × limbic friction axes (developing)
- [[Linchpin Habits]] — force-multiplier habits; always enjoyable (developing)
- [[Identity-Based vs Goal-Based Habits]] — self-concept frame vs. per-execution checkbox; Clear adds evidence-accumulation mechanism (developing)
- [[Three-Phase Day Framework]] — circadian neurochemical windows for habit placement (developing)
- [[21-Day Habit Formation System]] — 6 habits/day, 4–5 expected, assess automaticity (developing)
- [[Habit Breaking via Replacement Behavior]] — immediate post-habit replacement remaps neural circuits (developing)
- [[Procedural Memory Visualization]] — mental step-through lowers execution threshold (developing)

### Pharmacology / Drug Harm
- [[Drug Harm vs Benefit Ranking]] — S–F harm-to-benefit tier list across 20 drugs; psilocybin S-tier (harm 5, strongest therapeutic pipeline); alcohol F-tier (harm 72, highest of all drugs); legal status inverts pharmacological evidence (complete)

### Hormones / Testosterone
- [[Testosterone Habits Tier List]] — S–F tier list of all habits ranked by effect × evidence: sleep/lean body fat/resistance training S-tier; cold exposure and NoFap D-tier; IF lowers T in lean men (complete)

### Sleep
- [[Sleep Habits Tier List]] — S–F tier list of all habits, products, and actions affecting sleep: circadian anchoring/morning sunlight/cool dark room S-tier; nicotine/alcohol/caffeine F-tier; supplements hierarchy; quick-reference protocol stack (complete)
- [[Research - Sleep Habits Tier List]] — full synthesis: 8 findings, CBT-I vs meds, supplement rankings, environment variables, diet-sleep connection, 20+ sources (complete)
- [[Research - Drug Harm vs Benefit Ranking]] — full synthesis: 8 findings, Nutt/ISCD 2010 harm scores for all 20 drugs, therapeutic evidence for psychedelics/buprenorphine/ketamine, cannabis evidence review, 14+ sources (complete)
- [[Sleep Optimization Supplements]] — melatonin (0.1–0.5 mg), magnesium glycinate (200–400 mg), L-theanine; what not to take (Benadryl, high-dose melatonin) (developing)

### Habits — Destructive (What to Avoid)
- [[Destructive Habits to Avoid at 19]] — S–C tier list of most damaging habits ranked by long-term harm × reversibility; doom scrolling/porn/alcohol S-tier; sleep deprivation/debt/procrastination A-tier; Joe-specific priority stack (complete)

### Habits / Behavior Design (Atomic Habits)
- [[Habit Loop]] — Clear's 4-step Cue→Craving→Response→Reward; extends Duhigg by adding Craving stage (developing)
- [[Four Laws of Behavior Change]] — Make it Obvious / Attractive / Easy / Satisfying; design framework mapped to Habit Loop (developing)
- [[Implementation Intention]] — "I will [Behavior] at [Time] in [Location]"; 2–3× follow-through improvement (developing)
- [[Habit Stacking]] — "After [Habit A] I will [Habit B]"; borrows existing neural trigger for new habit (developing)
- [[Two-Minute Rule]] — scale any new habit to <2 min entry point; master showing up first (developing)
- [[Temptation Bundling]] — pair WANT + NEED; anticipatory dopamine makes necessary habits attractive (developing)
- [[Goldilocks Rule]] — peak motivation at edge of current ability; boredom (not failure) is primary long-run enemy (developing)
- [[Commitment Device]] — present choice locks in future behavior; Ulysses contract; one-time actions; automation (developing)

### Health / Fitness / Cycling
- [[Cardio Training Zones]] — 5-zone system; Zone 1–5 definitions, benefits, BPM ranges for age 19 (max HR 201); Karvonen formula; zone system comparisons (evergreen)
- [[Training Periodization]] — macrocycle/mesocycle/microcycle; 5-phase annual cycling arc (developing)
- [[Polarized Training]] — Seiler 80/20: 80% Zone 1, ~20% Zone 3, avoid grey zone (developing)
- [[VO2 Max Interval Training]] — 2–4 min at 106–120% FTP; concentrated 2–3 week blocks (developing)
- [[Strength Training for Cyclists]] — 4-phase off-season gym arc: Adaptation → Hypertrophy → Strength → Power (developing)
- [[Daily Caloric Intake Calculator]] — TDEE calculation (Mifflin-St Jeor, Katch-McArdle, Harris-Benedict); activity multipliers; loss/gain/maintain targets; protein floors; macro splits (developing)
- [[Bulk and Cut Decision Framework]] — BF%-based decision rule; lean bulk/cut/recomp protocols; calorie math; cycle structure (developing)
- [[FFMI Natural Muscle Potential]] — FFMI formula, scale 16–25+, 5'9" reference table, natural ceiling ~25 (developing)

### GLP Medications (Weight Management)
- [[GLP-1 Medications Overview]] — generation comparison table: semaglutide vs. tirzepatide vs. retatrutide; receptor targets; decision framework (developing)
- [[Semaglutide]] — GLP-1 only; Ozempic/Wegovy/Rybelsus; 0.25→2.4 mg/week titration; ~14–20% wt loss; SELECT CV trial; oral form Dec 2025 (developing)
- [[Tirzepatide]] — GLP-1+GIP dual agonist; Mounjaro/Zepbound; 2.5→15 mg/week titration; ~20–22% wt loss; SURMOUNT-5 beats sema by 47%; OSA indication (developing)
- [[Retatrutide]] — GLP-1+GIP+glucagon triple agonist; 2→12 mg/week; 28.7% wt loss Phase 3; NOT FDA-approved (~2027); dysesthesia safety signal (developing)
- [[GLP Medication Exit Strategy]] — weight regain reality; maintenance dosing; 9-week taper protocol; pharmacological bridges; 5-lb trigger rule (developing)

### Health / Personal
- [[Foundational Health Supplements]] — vitamin D, magnesium, omega-3, zinc; deficiency rates (developing)
- [[Creatine for Cognitive Performance]] — memory SMD 0.31; moderate certainty; 3–5 g/day (developing)
- [[Caffeine and L-Theanine Stack]] — best acute study stack; 2:1 ratio; high evidence (developing)
- [[Caffeine Complete Guide]] — full mechanism, evidence-graded health effects, dosing table, tolerance, safety limits (stable)
- [[Caffeine Timing Protocol]] — 90-min morning delay, sleep cutoff by dose, cortisol interaction, pre-workout timing (stable)
- [[Caffeine Cycling Protocol]] — tolerance timeline, 4 cycling strategies, taper vs. cold turkey, withdrawal management (stable)
- [[Caffeinated Drinks Health Tier List]] — S–F tier ranking; matcha → green tea → filtered coffee → tea → energy drinks; caffeine content table (stable)
- [[Bacopa Monnieri]] — long-term memory; 4–12 weeks; medium evidence (developing)
- [[Lion's Mane Mushroom]] — NGF stimulation; thin human evidence; seed (seed)
- [[Rhodiola Rosea]] — stress/fatigue adaptogen; situational use; medium evidence (developing)
- [[Sleep Optimization Supplements]] — magnesium glycinate, melatonin dosing, sleep hygiene (developing)
- [[Supplement Priority Stack for Young Males]] — practical 4-tier implementation guide (developing)

### Personal Finance / Financial Literacy
- [[Financial Literacy Roadmap]] — phase-by-phase guide from zero to FI: foundation → wins → accumulation → tax optimization → independence; compound interest tables; 50/30/20 budget (developing)
- [[Financial Order of Operations]] — 9-step Money Guy FOO: deductible → employer match → high-interest debt → emergency fund → Roth IRA → 401k → hyper-accumulate → abundance → low-interest debt (developing)
- [[Index Fund Investing]] — why index funds beat 92% of active managers; fund guide (VTI/FXAIX/VTWAX); expense ratio math; DCA; Roth IRA setup steps; compound interest table by age (developing)
- [[Credit Score Building]] — FICO breakdown (35% payment history, 30% utilization); 4-step path from 0 to 750+; secured card strategy; authorized user hack; milestones by age (developing)

### Books / Reading Strategy
- [[Book Sourcing Strategy]] — decision tree + tier list for acquiring books free or cheap; Libby, BookBub, ThriftBooks, BookFinder; pricing norms (complete)

### Book Lists — Curated Reading by Category
- [[Book List — Finance and Investing]] — S/A/B tier; The Intelligent Investor, Psychology of Money, Just Keep Buying, index fund thesis, mental models (developing)
- [[Book List — Self-Help, Discipline, and Productivity]] — S/A/B tier; Atomic Habits, Can't Hurt Me, Deep Work, Essentialism, 7 Habits, Man's Search for Meaning (developing)
- [[Book List — Stoicism and Philosophy]] — S/A/B tier; Meditations, Ego Is the Enemy, Obstacle Is the Way, Letters from a Stoic; daily practice stack (developing)
- [[Book List — Psychology and Persuasion]] — S/A/B tier; Influence (Cialdini), Never Split the Difference (Voss), Thinking Fast and Slow, Getting to Yes; core persuasion models (developing)
- [[Book List — Business and Entrepreneurship]] — S/A/B tier; Zero to One, Good to Great, Shoe Dog, The Lean Startup, Hard Thing About Hard Things (developing)
- [[Book List — Fiction Must-Reads]] — S/A tier classics and modern; Count of Monte Cristo, East of Eden, 1984, Crime and Punishment, Dune, The Road; phased reading order (developing)
- [[Book List — Biographies]] — S/A/B tier; da Vinci, Jobs, Musk (Isaacson); Hamilton, Napoleon, Franklin, Rockefeller (Chernow/Roberts); Team of Rivals, Power Broker (developing)
- [[Book List — Science]] — S/A/B tier; Feynman Lectures, Selfish Gene, Short History of Nearly Everything, QED, The Gene, Emperor of All Maladies, GEB (developing)
- [[Book List — History]] — S/A/B tier; Sapiens, Guns of August, Rise and Fall of Third Reich; Genghis Khan, Silk Roads, SPQR, 1776; Durant's Story of Civilization (developing)
- [[Book List — Writing and Communication]] — S/A tier; On Writing Well (Zinsser), Elements of Style, Bird by Bird, Several Short Sentences (developing)
- [[Book List — Economics]] — S/A/B tier; Economics in One Lesson, Freakonomics, Worldly Philosophers, Basic Economics (Sowell), Poor Economics (developing)
- [[Book List — Health and Longevity]] — S/A/B tier; Outlive (Attia), Why We Sleep (Walker), Lifespan (Sinclair), Obesity Code (Fung) (developing)
- [[Book List — Mathematics]] — S/A/B tier; How to Prove It, GEB, Linear Algebra Done Right, Calculus (Spivak), AoPS series (developing)
- [[Research - Book Recommendations Master List]] — master synthesis with Joe's 12-book phased reading order across all categories (complete)

### Food / Nutrition Tier Lists
- [[Food Health Tier List — Overall]] — S–F ranking of all major foods by pure healthiness; scoring framework (developing)
- [[Food Health Tier List — Vegetables]] — CDC Powerhouse scores; cruciferous cancer-protection hierarchy; 100/100 watercress (developing)
- [[Food Health Tier List — Fruits]] — GI for every fruit; berry dominance; avoid dried/juice (developing)
- [[Food Health Tier List — Meats and Seafood]] — omega-3 content + mercury table; processed meat F-tier (WHO Group 1) (developing)
- [[Food Health Tier List — Legumes]] — fiber + protein per cup; lentils S-tier; Blue Zone legume data (developing)
- [[Food Health Tier List — Nuts and Seeds]] — omega-3 ratios; 28g/day = 21% CVD reduction; Brazil nut selenium caution (developing)
- [[Food Health Tier List — Grains]] — GI values; beta-glucan in oats/barley; whole vs. refined impact (developing)
- [[Food Health Tier List — Dairy]] — fermentation hierarchy; kefir 61 probiotic strains vs. yogurt 7; full-fat debate (developing)

### Biohacking / Optimization
- [[Biohacking Tier List]] — S–D ranking across 10 categories: sleep, exercise, temperature, light, fasting, stress, wearables, cognitive, longevity, gut (developing)
- [[Health Protocol Tier List]] — 28 protocols ranked S–D with specific prescriptions: dose, temp, frequency, timing; sauna, CWI, Zone 2, VO2 max, strength, sleep, TRE, red light, breathwork (developing)
- [[Supplement Tier List Complete]] — every supplement ranked across 15 categories with doses (developing)
- [[Peptide Tier List Complete]] — every major peptide ranked S–D by evidence × risk × Joe relevance; synergy map; WADA flags; priority action plan; GHK-Cu S-tier, BPC-157 A-tier, Semax A-tier (developing)
- [[Health Biomarkers Complete Panel]] — all blood test biomarkers with optimal longevity ranges and testing cadence (developing)
- [[Biohacking Daily Health Hacks]] — 36 simple, proven, free/cheap daily practices with mechanisms (developing)
- [[Biohacking Health Products Protocol]] — evidence-based products + step-by-step protocols for supplements, skincare, haircare, and oral care (developing)

### Online Income / Entrepreneurship
- [[Online Income Methods Tier List]] — S–C tier list of all online income methods ranked by speed-to-first-dollar and ceiling: tutoring S-tier, AI freelancing S-tier, UGC A-tier, dropshipping C-tier (developing)
- [[Freelancing Online]] — concept page: top categories, income ladder, AI freelancing breakout, platforms (Upwork/Fiverr/Toptal), starting with no experience (developing)
- [[UGC Content Creation]] — brand-paid content creation; no audience needed; $50–$150/video entry, $5,000–$15,000+/month ceiling; equipment, platforms, contract basics (developing)
- [[Research - Online Income Ways for 19 Year Old]] — full synthesis: 8 findings, S–C tier list, cross-links to finance and career tracks (complete)

### Income / Career Tier Lists
- [[High Income Skills Tier List]] — S–C ranking of all learnable skills by 2026 salary ceiling; AI/ML S-tier, power electronics A-tier, freelance ceilings (developing)
- [[EE Specialization Salary Tier List]] — EE-specific tier list: analog/mixed-signal S-tier ($222k median), FPGA S-tier ($175k avg), WBG power electronics A-tier ($112k–$230k); Joe income ladder (developing)
- [[EE High Income Action Plan]] — 4-phase Joe-specific roadmap: foundation → power electronics → WBG specialization → FPGA/AI second stack; LLNL/Sandia 2027 target (developing)

### Career / Job Search
- [[First Job Roadmap — Livermore Tri-Valley]] — Phase 0–3 roadmap for ASU EE freshman in Livermore: local jobs, LLNL/Sandia targeting, portfolio, LinkedIn (developing)
- [[ASU EE Mentorship Pathways]] — tier list of all mentorship channels at ASU: peer mentors, FURI, faculty (Ranjram/Ayyanar), IEEE ASU, IEEE Collabratec, Barrett Alumni; Year 1 action stack (developing)

### Chess Improvement
- [[Chess Improvement Complete Guide]] — master reference: four pillars (tactics, openings, endgames, game analysis), daily routines, common mistakes, cognitive benefits, Joe-specific integration (complete)
- [[Chess Rating Roadmap]] — phase-by-phase guide from unrated to 2000+; study distribution by rating, book ladder, platform comparison, endgame must-know list (complete)

### Free Time / Lifestyle
- [[Free Time Tier List]] — S–F ranking of free-time activities by long-term compounding ROI; EE self-study, deep reading, social time S-tier; doom-scrolling F-tier; Joe-specific (complete)
- [[Post-Study Energy Management]] — cognitive depletion model; recovery activity tier list; 10-min diagnostic; shutdown ritual; morning block schedule fix (developing)
- [[Video Games Cognitive Benefits]] — S–F tier list of 40+ PC+mobile games ranked by cognitive ROI; Chess/StarCraft II/Portal 2 S-tier; gacha games F-tier; Joe-specific recommendations (developing)
- [[Hobbies for Young Men — Life Domain Framework]] — tier list across 5 life domains (physical/creative/social/financial/intellectual); BJJ, guitar, rock climbing, investing S-tier; Joe domain audit (developing)
- [[Martial Arts for Young Men]] — BJJ vs boxing comparison; testosterone/GH benefits; gym culture; frequency with cycling; getting started in Livermore (developing)
- [[Music as a Life Skill]] — guitar vs piano; JustinGuitar curriculum; milestone timeline; integration with post-study recovery; social/identity/emotional ROI (developing)
- [[Zero Cost Computer Skills — Tier List]] — S–C tier list of 16 skills buildable today at a computer for free; touch typing/Python/Git/LTSpice S-tier; Verilog/SQL/Linux A-tier; Joe's start-today action stack (developing)

### Education / Learning Media
- [[YouTube Channels for STEM Learning]] — S–B tier list; 3Blue1Brown/Veritasium/PBS Space Time S-tier; Andrej Karpathy AI; Joe watch order mapped to EE coursework (developing)
- [[YouTube Channels for Humanities Learning]] — S–B tier list; Vsauce/Kurzgesagt S-tier; philosophy, history, economics channels; Ray Dalio economics video (developing)
- [[Educational Documentaries]] — S–B tier list; Cosmos (Sagan) S-tier; Particle Fever, Story of Math, Social Dilemma, Becoming Warren Buffett; Joe watch order (developing)
- [[Intellectual Films]] — S–B tier list; Oppenheimer/The Big Short S-tier; science, philosophy, business films; Joe watch order (developing)

### Dating / Relationships
- [[College Dating Methods Ranked]] — S–D tier list of all methods; clubs/classes S-tier; Hinge A-tier app; ask formula; physical baseline (developing)

### Social Connection / Friendships
- [[ASU Social Connection Methods Ranked]] — S–D tier list of all ASU friendship-building methods; IEEE/Solar Devils S-tier; study groups S-tier; proximity science; Joe's action stack (developing)
- [[ASU EE Clubs Tier List]] — S–C tier ranking of all ASU engineering clubs for EE students; IEEE+Solar Devils+SDSL S-tier; HKN/Tau Beta Pi/PES A-tier; Joe's recommended timeline (developing)

### Networking / Relationships
- [[Social Confidence Building]] — Three-staircase model (micro → sustained → high-stakes); conversation techniques (Flooding Smile, Sticky Eyes, mirroring); cognitive restructuring; identity shift (developing)
- [[Social Anxiety Exposure Hierarchy]] — SUDS 0–100 fear ladder; protocol for bottom-up graduated exposure; extinction curve (developing)
- [[Social Ladder Climbing]] — Value + visibility + consistency; super connectors; generosity-first; warm vs. cold approach (developing)
- [[Generosity-First Networking]] — give before you need; don't keep score; network as lifestyle, not transaction (developing)
- [[Relationship Action Plan]] — 3yr→1yr→90day goals mapped to people needed; build before you need it (developing)
- [[Pinging System]] — lightweight ongoing contact; frequency beats intensity; birthday effect (developing)
- [[Follow-Up Formula]] — follow up within 24h; reference specific detail; give something first (developing)
- [[Super Connectors]] — high-density network nodes; one super connector > 20 weak connections (developing)
- [[Health Wealth Family Framework]] — help someone with these three domains = deepest possible bond (developing)

## Sources

### Books
- [[The 7 Habits of Highly Effective People - Stephen Covey]] — Covey (1989); Maturity Continuum, P/PC Balance, Time Management Matrix, Empathic Listening, Synergy; ⭐⭐⭐⭐⭐
- [[Atomic Habits - James Clear]] — Clear (2018); 4-step Habit Loop, Four Laws of Behavior Change, 1% compounding; ⭐⭐⭐⭐⭐ (Joe)
- [[How To Win Friends and Influence People - Dale Carnegie]] — Carnegie (1936); 30 principles across 4 parts; human relations, influence, leadership
- [[Never Eat Alone - Keith Ferrazzi]] — Ferrazzi & Raz (2014); generosity-first networking; RAP, pinging, follow-up formula, super connectors; ⭐⭐⭐⭐⭐ (Joe)

### Course Syllabi / Prep Resources
- [[EEE 202 Course Page ASU Tsakalis]] — Tsakalis/Vasileska; canonical 8-unit sequence; PSpice + MATLAB; Irwin textbook
- [[MIT 18.06 Linear Algebra OCW Gilbert Strang]] — 34 lectures, free, CC BY-NC-SA; 18.06SC has problem sets; selective lecture guide for MAT 343 prep

### Computer Architecture
- [[SIGGRAPH - Eras of GPU Development 2025]] — ACM SIGGRAPH Blog, April 2025; authoritative GPU era framework
- [[Darkesh-Patel-Jensen-Huang-Nvidia-2025]] — Jensen Huang interview; CUDA moat, TPU vs GPU, supply chain, China export controls

### Psychology / Emotional Intelligence
- [[Impostors - Susan David on Emotional Agility]] — Impostors podcast, Susan David, 2023

### Neuroscience / Habits
- [[Huberman Lab Essentials - Habit Formation and Breaking]] — Huberman, 2025, podcast transcript

### AI / LLM
- [[Survey - Low-bit LLMs 2024]] — arXiv 2409.16694, comprehensive quantization survey
- [[Edge LLM Inference Benchmark 2026]] — arXiv 2603.23640, sustained hardware benchmarks
- [[Framework Comparison Apple Silicon 2025]] — arXiv 2511.05502, MLX/MLC-LLM/llama.cpp
- [[Bitnet.cpp Edge Inference 2025]] — arXiv 2502.11880, ternary LLM CPU inference

### Power Electronics / EV
- [[IEEE Spectrum SiC vs GaN 2024]] — authoritative SiC vs GaN competitive landscape
- [[MDPI WBG Comparative Review 2024]] — material properties, reliability, EV applications

## Areas (Personal)
- Health / Supplements — see [[Research - Supplements for Young Male Health and Learning]]

### Python EE Project Ladder (Sources)
- [[PyPedia EE with Python GitHub]] — PyPedia 2024; Jupyter notebooks covering digital circuits, circuit theory, microelectronics in Python
- [[Prasun Barua Python Circuit Analysis 2025]] — Barua April 2025; seven-project progression from Ohm's Law to automated n-node solver
- [[PySDR Python Filters Guide]] — PySDR.org 2025; definitive Python FIR/IIR filter design reference; firwin, freqz, lfilter
- [[Prasun Barua Python Power Electronics 2025]] — Barua April 2025; buck converter + SPWM inverter + FFT harmonic analysis in Python
- [[Heslip Labs Python LTSpice Tutorial]] — Heslip Labs 2024; eight PyLTSpice automation patterns with code; best PyLTSpice tutorial

### Math Foundations (Sources)
- [[Research - Math and Physics Foundations for EE]] — 8 key findings mapping Calc 1-3, DiffEQ, Mechanics, E&M to EE coursework and career (developing)

## Questions / Synthesis

### Travel
- [[Research - Rome Vatican Family Trip May 2026]] — complete 9-day family tourist guide (May 11–19); Joe + parents aged 60+52; Vatican Museums, Colosseum, Tivoli day trip, Ostia Antica, day-by-day itinerary, food guide, senior-friendly tips, booking checklist (complete)
- [[Research - Python EE Project Roadmap]] — 20-project ladder synthesis; library progression, cocotb FPGA track, double pulse test power track; full code for each project (developing)
- [[Research - Testosterone Habits Tier List]] — 8 key findings + 17 sources; sleep #1, body fat aromatase cycle, cold exposure myth debunked, NoFap myth debunked (complete)
- [[Research - Destructive Habits to Avoid at 19]] — 8 key findings + 5 open questions; doom scrolling brain rot, porn neuroplasticity damage, alcohol at 19 2× impairment, sleep deprivation Alzheimer's link, procrastination learned helplessness, debt compounding, social isolation = 15 cigarettes/day, fixed mindset ceiling (complete)
- [[Research - Free Time Tier List]] — 8 key findings; Harvard happiness study, flow research, attention degradation from social media; S–F tier ranking for 19yo EE student (complete)
- [[Research - Hobbies for Young Men]] — 8 key findings; 5 life domain framework; S–D tier list; BJJ + guitar + investing as Joe's priority stack; Roth IRA + martial arts + rock climbing action moves (developing)
- [[Research - Post-Study Motivation and Active Recovery]] — 8 key findings; cognitive depletion science; active recovery tier list; guilt reframe; schedule architecture fix; Joe-specific action plan (developing)
- [[Research - Where to Get Cheap Books]] — full tier list (S=free → D=avoid); Libby, BookBub, ThriftBooks, AbeBooks, BookFinder, Project Gutenberg; Joe-specific sourcing path for his 9-book reading list (complete)
- [[Research - Top MS EE Programs Physical Side]] — 10 schools ranked; NC State WBG MS, VT CPES, UT Austin SSE; Joe's recommended path to NC State + PowerAmerica pipeline (developing)
- [[Research - MS EE Programs Acceptance Rates]] — acceptance rate table for all 10 schools; Purdue ~37% most accessible; MIT PhD-only ~6–9%; NC State WBGS and UT Austin SSE too new for data; GPA + FURI + named-faculty SOP are key differentiators (developing)
- [[Research - College Dating Guide for Young Men]] — all methods ranked S–D; app rankings; the ask formula; baseline stack; mindset principles (complete)
- [[Research - Building Social Connections at ASU]] — 8 key findings; proximity science; Jeffrey Hall 50–200 hr formula; ASU-specific resources; online student strategy (developing)
- [[Research - Social Confidence and Climbing the Social Ladder]] — 8 key findings; 12-week week-by-week plan; CBT + exposure hierarchy; conversation techniques; social ladder strategy (developing)
- [[Research - First Job Roadmap Livermore CA]] — Local employer map, LLNL/Sandia internship timelines, ASU resources, phase-by-phase roadmap (developing)
- [[Research - EE Deep Learning Topics for First-Year Students]] — 8 key findings; 6-topic depth priority map with year-by-year targets; textbook + resource recommendations per topic; Joe-specific WBG-oriented action plan (developing)
- [[Research - First-Year ASU EE Skills]] — 8 key findings; ASU curriculum map, freshman self-study stack, portfolio strategy, hiring survey data (developing)
- [[Research - EE Physical Side Skills for Semiconductors and Power]] — 8 key findings; hiring signals, 18-month actionable plan, WBG career context (developing)
- [[Research - LTSpice Skills Guide]] — 8 key findings; 4 simulation types, 10-circuit ladder, SPICE directives, power electronics sim, common mistakes, Joe's 4-phase timeline (complete)
- [[Research - Complete Biohacking Guide]] — 8 key findings; tier lists, supplements, biomarkers, daily hacks (developing)
- [[Research - Peptide Tier List]] — 8 key findings; full peptide tier list personalized for Joe; WADA considerations; synergy stacks; regulatory shift Feb 2026; priority action plan (developing)
- [[Research - Cycling Training Periodization and Annual Plan]] — 8 key findings, 6-day/week training plan across 5 phases
- [[Research - GLP Medications Complete Guide]] — 8 key findings; semaglutide/tirzepatide/retatrutide mechanisms, full dosing tables, weight loss outcomes, exit strategies; retatrutide ~2027 FDA (developing)
- [[Research - High Income Skills Tier List]] — general + EE skill tier lists by 2026 salary; 4-phase Joe action plan; FPGA and WBG primary/secondary stack (developing)
- [[Research - EE Mentorship at ASU]] — 8 key findings; S–C tier list of all mentorship channels; faculty contact info; cold email formula; Year 1 action stack (developing)
- [[Research - Games Cognitive Tier List]] — 8 key findings; Portal 2 > Lumosity study; StarCraft II RCT; FPS attention research; gacha harm evidence; Joe game stack (developing)
- [[Research - Chess Improvement Guide]] — 8 key findings; tactics as fastest lever; rating-based study distribution; game analysis protocol; book ladder Seirawan → Silman → Yusupov → Dvoretsky; Joe-specific integration (complete)
- [[Research - Python and C++ in Electrical Engineering]] — 8 key findings; Python two-layer stack model, PyVISA ATE control, python-control design, TI C2000 DSP, MISRA-C, language handoff pattern; Joe's 9–24 month dual roadmap (developing)
- [[Research - YouTube Channels and Learning Media]] — 8 key findings; S-tier channel/documentary/film rankings; Joe-specific watch order for EE track; 5 open questions (developing)
- [[Research - Programming in the AI Era]] — 8 key findings; Python still the dominant AI-era language; 5-phase AI-native learning roadmap; skills AI can't replace; best 2026 tool combo (developing)
- [[Research - Daily Caloric Intake and Tracking Apps]] — 8 key findings; Mifflin-St Jeor formula; goal-based calorie targets; app tier list S–C (MacroFactor/Carbon/Cronometer/MFP/LoseIt/Noom); adaptive TDEE science (complete)
- [[Research - Bulking vs Cutting Body Composition Guide]] — bulk/cut/recomp decision tree; FFMI targets at 5'9"; Joe-specific calorie math; muscle gain timelines (developing)
- [[Research - Financial Literacy Roadmap]] — 8 key findings; 5-phase roadmap; FOO sequence; Roth IRA at 19 math; index fund fee table; credit score 4-step path; Joe-specific action plan; 40-year compound table (developing)
- [[Research - Zero Cost Computer Skills]] — 8 key findings; S–C tier list; touch typing, Python, Git, LTSpice S-tier; free resource links per skill; Joe start-today action stack (complete)
- [[Research - Evolution of CPUs and GPUs]] — 8 key findings, 5 open questions
- [[Research - LLM Quantization and Edge Hardware]] — 8 key findings, 5 open questions
- [[Research - WBG Semiconductors in EV Fast Charging]] — 8 key findings, 5 open questions
- [[Research - ASU EE Clubs]] — 8 key findings; S–C tier list; Solar Devils + SDSL + IEEE ASU S-tier project/networking clubs; honor society timeline; Joe's recommended club stack and timeline (developing)
- [[Research - Supplements for Young Male Health and Learning]] — 8 key findings, 5 open questions
- [[Research - Cardio Training Zones]] — 5-zone system deep dive; Zone 1–5 physiology; max HR 201 bpm at age 19; Karvonen formula; Garmin/Polar/Seiler/Coggan system comparisons; mitochondrial biogenesis mechanism; San Millán Zone 2 metabolic health evidence (evergreen)
