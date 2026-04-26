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

## [2026-04-26] autoresearch | Python EE Project Roadmap
- Rounds: 3 | Searches: 9 | Sources fetched: 7 | Pages created: 11
- Created: [[Research - Python EE Project Roadmap]], [[Python EE Project Ladder]], [[Python EE Project Ladder - Phase 0-1]], [[Python EE Project Ladder - Phase 2-3]], [[Python EE Project Ladder - Phase 4-5]], [[Python EE Project Ladder - Advanced Tracks]]
- Sources: [[PyPedia EE with Python GitHub]], [[Prasun Barua Python Circuit Analysis 2025]], [[PySDR Python Filters Guide]], [[Prasun Barua Python Power Electronics 2025]], [[Heslip Labs Python LTSpice Tutorial]]
- Key finding: A 20-project ladder from Ohm's Law Calculator (pure Python) through nodal analysis (NumPy), DSP/FFT (SciPy), PID and buck simulation (python-control + solve_ivp), LTSpice automation (PyLTSpice), and real-instrument control (PyVISA) — ending in Track A (cocotb FPGA verification) or Track B (double pulse test analyzer for WBG power electronics). Each project teaches exactly one new Python concept while solving a real EE problem.

## [2026-04-24] autoresearch | Post-Study Motivation and Active Recovery
- Created: [[Research - Post-Study Motivation and Active Recovery]], [[Post-Study Energy Management]]
- Covers: What to do when class study drains motivation for outside technical work (LTSpice, programming); the science of cognitive fatigue and ego depletion; active recovery activity tier list; guilt reframe; schedule architecture fix
- Key findings: (1) Cognitive depletion after class study is neurologically real — EEG-confirmed; Cal Newport's deep work ceiling is ~4 hours/day, so class may consume the whole budget; (2) The biggest error is filling depleted time with F-tier activities (scrolling) instead of B-tier active recovery; (3) Passive learning (3Blue1Brown, reading Phase 1 books) is legitimate and compounds without requiring high cognitive load; (4) Best recovery activities: Zone 2 cardio, outdoor walks, real social time, reading enjoyable books, cooking — all restore directed attention better than passive phone use; (5) The 10-minute diagnostic rule: force-start for 10 min; still dragging = genuine fatigue, stop; absorbed = it was Limbic Friction, continue; (6) Schedule fix: put LTSpice/Python in morning block (post-ride) before class cognitive drain, not contingent on post-class energy; (7) Newport's shutdown ritual ("Shutdown Complete") eliminates low-grade work anxiety that blocks genuine restoration; (8) The guilt reframe: Energy × Focus × Time = Output; 30 focused minutes tomorrow >> 2 depleted hours tonight

## [2026-04-24] autoresearch | YouTube Channels and Learning Media
- Created: [[Research - YouTube Channels and Learning Media]], [[YouTube Channels for STEM Learning]], [[YouTube Channels for Humanities Learning]], [[Educational Documentaries]], [[Intellectual Films]]
- Covers: Comprehensive tier lists for YouTube channels (STEM + humanities), documentaries, and intellectual films for self-education
- Key findings: (1) 3Blue1Brown is uncontested #1 for mathematical intuition — Essence of Calculus/Linear Algebra/Neural Networks series directly supports EE math; (2) PBS Space Time is the highest-ceiling physics channel at near-graduate depth; Veritasium best for accessible physics; (3) Vsauce and Kurzgesagt offer widest interdisciplinary intellectual range on YouTube; (4) Andrej Karpathy "Neural Networks: Zero to Hero" is the elite AI/ML self-education resource — used in university courses; (5) Cosmos (Carl Sagan, 1980) is the greatest science documentary ever made — 9.3/10 IMDb, 13 episodes, still unmatched; (6) Oppenheimer (2023) and The Imitation Game (2014) are S-tier intellectual films — most ideas per hour in mainstream cinema; (7) The Social Dilemma (2020, Netflix) is the most immediately relevant documentary for young people building attention hygiene habits; (8) Best documentary arc (30h total): Cosmos → Particle Fever → Story of Math → Fermat's Last Theorem → Social Dilemma → Inside Bill's Brain → Becoming Warren Buffett

## [2026-04-24] autoresearch | Programming in the AI Era
- Created: [[Research - Programming in the AI Era]], [[AI-Assisted Programming Learning Roadmap]], [[Programming Skills AI Cannot Replace]]
- Covers: Whether Python is still worth learning in 2026; how old learning methods are outdated; a full 5-phase AI-native roadmap for learning to code using AI tools; skills AI cannot replace
- Key findings: (1) Python is more relevant than ever — it is the language of AI/ML itself, with 50% more jobs than Java; (2) AI tools don't replace learning, they amplify those who understand fundamentals and expose those who don't; (3) Old methods ARE partially outdated — rote syntax memorization, tutorial hell, solo grinding — but core fundamentals (debugging, data structures, systems thinking) remain essential; (4) New paradigm: AI-native project-based learning — build something real from week 1, use AI to explain on demand, question every generated line; (5) The 5-phase roadmap: Fundamentals (wk 1–8) → Git+debugging (wk 9–12) → AI tool onboarding (wk 13–16) → Build real projects (wk 17+) → Systems thinking + prompt engineering (month 6+); (6) Skills AI cannot replace: architectural judgment, domain/business context, debugging instinct, code review taste, security mindset, communication; (7) Premium has shifted to architecture and judgment, applied at a higher stack level; (8) Best 2026 AI tool combo: Claude Pro ($20/mo) + GitHub Copilot ($10/mo)

## [2026-04-24] autoresearch | Python and C++ in Electrical Engineering
- Created: [[Research - Python and C++ in Electrical Engineering]], [[Python in Electrical Engineering]], [[C++ in Electrical Engineering]], [[Python Self-Teaching Roadmap for EE]], [[C++ Self-Teaching Roadmap for EE]]
- Covers: Full breakdown of how Python and C++ serve complementary roles in physical EE (simulation/analysis vs. real-time firmware); complete month-by-month self-teaching roadmap for both languages from scratch to professional-grade skills
- Key findings: (1) Python and C++ are a two-layer stack — Python for design/simulation/analysis/automation, C/C++ for real-time embedded firmware; the canonical workflow is prototype in Python → validate in LTSpice → implement in C on DSP; (2) Python's physical EE superpower is PyVISA: programmatic control of every bench instrument over GPIB/USB/LAN via SCPI commands — core test automation skill; (3) python-control library directly replicates MATLAB Control Toolbox (Bode, rlocus, step response, margins) — free, runs on any PC; (4) C runs every power converter's brain: TI C2000 F28379D DSP runs PI control at 100 kHz inside EV traction inverters and DCFC chargers; (5) MISRA-C (automotive functional safety ISO 26262) mandates C not C++ for safety-critical embedded — knowing basics differentiates internship candidates; (6) ARM CMSIS-DSP is the C equivalent of SciPy — hardware-optimized FFT, FIR, PID functions for Cortex-M MCUs; (7) Language handoff pattern: design algorithm in Python → port to C → validate on hardware; MATLAB Coder / Cython can automate this; (8) Joe's roadmap: Python Phase 0 (K Automate Boring Stuff) → Phase 1 (NumPy/SciPy/Bode plots) → Phase 2 (python-control PI design) → Phase 3 (PyVISA + PyLTSpice) → C Phase 0 (K&R pointers) → Phase 1 (Arduino extended) → Phase 2 (STM32 HAL) → Phase 3 (FreeRTOS) → Phase 4 (TI C2000 digital power)

## [2026-04-24] autoresearch | PC & Mobile Games Cognitive Tier List
- Created: [[Research - Games Cognitive Tier List]], [[Video Games Cognitive Benefits]]
- Covers: 40+ PC and mobile games ranked S–F by cognitive benefit; based on peer-reviewed research, meta-analyses, and expert consensus; Joe-specific recommendations
- Key findings: (1) Portal 2 beat Lumosity in a Carnegie Mellon/FSU controlled study — entertainment games can outperform dedicated brain trainers; (2) StarCraft II has the strongest RCT evidence for cognitive flexibility (PLOS One — faster/more accurate tests vs. controls); (3) FPS games reliably improve perceptual speed and visual attention — 2023 APA meta-analysis confirmed, 2025 study shows greater gray matter in attention network; (4) BrainHQ is the most evidence-backed brain training app (100+ peer-reviewed studies, FDA-qualified cognitive device); (5) Gacha games actively impair inhibitory control — 2025 arXiv study confirmed; (6) S-tier games: Chess, StarCraft II, Portal 2, Factorio, The Talos Principle; (7) F-tier: gacha games, idle/clicker games (exploit cognitive biases or zero demand); (8) For Joe specifically: Chess.com + Portal 2 (one-time) + Into the Breach = best cognitive ROI within the 1–2 hrs/week gaming cap

## [2026-04-23] autoresearch | EE Mentorship at ASU
- Created: [[Research - EE Mentorship at ASU]], [[ASU EE Mentorship Pathways]]
- Covers: Complete guide to finding an electrical engineering mentor at ASU — formal programs, faculty approach, IEEE pathways, cold email formula, Year 1 action stack
- Key findings: (1) Every first-year ASU engineering student is auto-assigned a peer mentor — activate this immediately; (2) FURI is the highest-leverage formal faculty mentorship path ($1,500 stipend + research experience) — apply sophomore year; (3) Prof. Mike Ranjram (MAPEL, mike.ranjram@asu.edu) and Prof. Raja Ayyanar (rayyanar@asu.edu) are the top power electronics faculty to approach via office hours; (4) Cold email works — read 1–2 papers first, write 7–12 sentences, one email at a time, wait 7 days before follow-up; (5) IEEE ASU Branch (600+ members) is the S-tier social path to mentors — project sub-teams create organic relationships; (6) IEEE Collabratec Mentor Program gives access to global industry mentors for ~$32/year IEEE membership; (7) Barrett Honors Alumni Mentorship (Oct–March) matches undergrads with EE alumni in a structured program — contact barrettmentors@asu.edu; (8) Engineering Futures Scholarship bundles financial aid + structured mentoring for eligible first-year students

## [2026-04-22] autoresearch | High Income Skills Tier List
- Created: [[Research - High Income Skills Tier List]], [[High Income Skills Tier List]], [[EE Specialization Salary Tier List]], [[EE High Income Action Plan]]
- Covers: General high-income skills ranked S–C by 2026 salary data; EE-specific specializations ranked by salary ceiling + demand; 4-phase Joe-specific action plan from ASU Year 1 to LLNL/Sandia 2027 internship and WBG career
- Key findings: (1) AI/ML Engineering is the highest-paying learnable skill ($155k–$350k); (2) Analog/Mixed-Signal IC Design = highest-paid EE specialization (median $222k, top $349k); (3) FPGA Engineering = most underrated high-pay EE skill ($175k avg, $251k 90th percentile) and directly relevant for Sandia/LLNL Livermore; (4) Power Electronics (WBG SiC/GaN) = $112k–$230k with steepest demand growth; (5) Embedded Firmware + RTOS = widest on-ramp to $150k+ for EE students (12–18 months to job-ready); (6) Skill stacking (EE + Python/AI) creates 20–30% salary premium; (7) Freelance ceiling: ML engineers $120–250/hr, FPGA $100–175/hr, power electronics consultants $75–150/hr; (8) Joe's optimal path = power electronics WBG primary + FPGA or Python/AI secondary stack

## [2026-04-22] autoresearch | Bulking vs Cutting and Body Composition Guide
- Created: [[Research - Bulking vs Cutting Body Composition Guide]], [[Bulk and Cut Decision Framework]], [[FFMI Natural Muscle Potential]]
- Covers: Full guide for a 5'9" male at 156 lbs on whether to bulk, cut, or recomp; FFMI targets; ideal body weight milestones; calorie and protein protocols
- Key findings: (1) BMI 23.04 = healthy; body fat % is the real decision variable, not scale weight; (2) at 15% BF → FFMI ≈ 19.6 (decent, significant room to grow); (3) decision rule: <15% BF → lean bulk, 15–20% → recomp (if <2yr training), >20% → cut first; (4) lean bulk = +200–300 cal/day over TDEE with 0.25–0.5 lb/week gain target; (5) protein floor = 140–160 g/day regardless of phase; (6) target physique milestone = FFMI 22 = 169 lbs @ 12% BF or 175 lbs @ 15% BF; near natural ceiling = FFMI 25 = 192–199 lbs; (7) Joe's TDEE ≈ 2,800–3,000 cal/day (cycling 6×/week); lean bulk target = 3,000–3,300 cal/day; (8) for beginners/intermediates, body recomp at maintenance + high protein + progressive overload beats aggressive bulk/cut cycling

## [2026-04-22] autoresearch | LTSpice Complete Skills Guide
- Created: [[Research - LTSpice Skills Guide]], [[LTSpice Complete Skills Guide]]
- Covers: Full guide to building LTSpice skills from zero to power electronics simulation; calibrated for Joe (ASU EE freshman, Year 1, self-studying before EEE 202 Circuits I)
- Key findings: (1) 4 core simulation types to master in order: .op → .tran → .ac → .dc; (2) 10-circuit progressive build ladder from voltage divider to closed-loop buck converter; (3) .step parametric sweep is the key power command that separates basic from advanced users; (4) import third-party SPICE models from manufacturer websites (TI, Wolfspeed, Infineon) using .lib directive; (5) power electronics simulations use PULSE source for PWM + MOSFET + LC + .meas for efficiency; (6) Monte Carlo requires {mc(nominal,tol)} syntax + .step run iterations; (7) 8 common beginner mistakes documented with fixes (most common: no DC path to ground = singular matrix error); (8) Joe's 4-phase timeline: Month 1 RC/RLC basics → Month 2 op-amps/.step → Month 3 buck converter → Month 4+ advanced (Monte Carlo, FRA, noise)

## [2026-04-21] autoresearch | Building Social Connections at ASU
- Created: [[Research - Building Social Connections at ASU]], [[ASU Social Connection Methods Ranked]]
- Covers: S–D tier list of all ASU social connection methods ranked by friendship formation probability and depth; calibrated for Joe (EE student, Year 1, online/hybrid from Livermore)
- Key findings: proximity + repeated exposure are the two strongest friendship predictors (seat proximity = 3–5× friendship odds); Jeffrey Hall (2019) = 50 hrs for casual friend, 200+ hrs for close friend; technical project clubs (IEEE ASU, Solar Devils) are S-tier because they generate friendship + career capital simultaneously; first 2 weeks have a unique open social window that closes by week 6–8; study groups in shared classes (MAT 265, PHY 121) are naturally S-tier; parties/bar scene = D-tier because contact hours never accumulate; Joe's action stack = IEEE sub-team + MAT 265 study group + Welcome Week yes-to-everything + ASU EE Discord for online student gap

## [2026-04-21] autoresearch | Free Time Tier List
- Created: [[Research - Free Time Tier List]], [[Free Time Tier List]]
- Covers: S–F tier list of free-time activities ranked by long-term compounding ROI; calibrated for Joe (19yo EE student, ASU Year 1, Livermore CA, trains 6x/week)
- Key findings: S-tier = EE self-study (Year 1 leverage window), deep reading, quality in-person social time; A-tier = side projects/GitHub, clubs (IEEE/Solar Car), deliberate rest, journaling; D-tier = social media browsing (measurably degrades attention), regular heavy drinking; F-tier = doom-scrolling (directly breaks sleep architecture); biggest lever is eliminating D/F defaults that fill gaps by inertia, not adding more S-tier activities; Harvard 80-year study confirms relationships > career success for long-term happiness

## [2026-04-21] autoresearch | Where to Get Cheap Books
- Created: [[Research - Where to Get Cheap Books]], [[Book Sourcing Strategy]]
- Covers: complete tier list S–D for acquiring books (free → paid); Libby app, BookBub, Project Gutenberg (S-tier free); ThriftBooks, Better World Books, AbeBooks, Book Outlet (A-tier); Kindle Unlimited, thrift stores, library sales (B-tier); price comparison tools (BookFinder, BookScouter); Joe-specific path for his Phase 1–3 reading list
- Key findings: Libby (library app) is the highest-leverage free option — most people don't use it; BookBub = free daily ebook deals, no reason not to subscribe; ThriftBooks = best single used-book site; Project Gutenberg covers all the Stoicism/classics free; Joe's 9-book reading list costs ~$0 via library or ~$25–35 via ThriftBooks

## [2026-04-21] autoresearch | Top MS EE Programs Physical Side (Power Electronics & Semiconductors)
- Created: [[Research - Top MS EE Programs Physical Side]], [[MS EE Programs Power Electronics Semiconductors]]
- Covers: 10 schools ranked by specialty (WBG semiconductors, power electronics, semiconductor devices); NC State MS-WBGS detail; Virginia Tech CPES; UT Austin SSE; Purdue online; MIT/Stanford/Berkeley; admission signals; Joe-specific path recommendation
- Key findings: NC State has the only dedicated WBG MS program in the US (Fall 2026); VT CPES is #1 for power electronics; UT Austin SSE (Fall 2025) has industry-funded fellowships; Joe's recommended path = NC State MS-WBGS + FURI in Year 2 + LLNL/Sandia connection

## [2026-04-21] autoresearch | College Dating Guide for Young Men
- Created: [[Research - College Dating Guide for Young Men]], [[College Dating Methods Ranked]]
- Covers: all methods ranked S–D (clubs, classes, apps, cold approach, dorms, work); app comparison (Hinge vs Tinder vs Bumble); the ask formula; physical baseline; mindset principles
- Key findings: Clubs/classes are S-tier (repeated contact eliminates cold-approach problem); Hinge = best app for relationships; Tinder University = most volume; 93% prefer in-person ask; specificity ("Friday at [place]") is the #1 differentiator in asking someone out; remembering specific conversation details = biggest underused advantage

## [2026-04-21] autoresearch | Book Recommendations — Finance, Self-Help, Discipline, Fiction, Business, Stoicism
- Created: [[Research - Book Recommendations Master List]], [[Book List — Finance and Investing]], [[Book List — Self-Help, Discipline, and Productivity]], [[Book List — Stoicism and Philosophy]], [[Book List — Psychology and Persuasion]], [[Book List — Business and Entrepreneurship]], [[Book List — Fiction Must-Reads]]
- Covers: 7 pages, ~60 books tiered S–B across 6 domains; Joe's 12-book phased reading order; mental models per category; reading sequences and context notes for a 19yo EE student
- Key findings: Psychology of Money = best starting investment book; Ego Is the Enemy = most important for ambitious young men; The Count of Monte Cristo = highest ROI fiction; Never Split the Difference = most practical negotiation book; Zero to One = most contrarian business book; Meditations = most re-readable philosophical text

## [2026-04-21] autoresearch | Food Health Tier Lists — All Categories
- Created: [[Food Health Tier List — Overall]], [[Food Health Tier List — Vegetables]], [[Food Health Tier List — Fruits]], [[Food Health Tier List — Meats and Seafood]], [[Food Health Tier List — Legumes]], [[Food Health Tier List — Nuts and Seeds]], [[Food Health Tier List — Grains]], [[Food Health Tier List — Dairy]], [[Research - Food Health Tier Lists]]
- Covers: S–F tier rankings for all major food categories based purely on healthiness; CDC Powerhouse nutrient density scores; GI values for all grains/fruits; omega-3 + mercury table for fish; fiber/protein per cup for legumes; nuts meta-analysis (28g/day = 21% CVD reduction); fermentation hierarchy for dairy
- Key findings: Dark leafy greens + fatty fish + berries = "holy trinity" backed by every dietary framework. Processed meats (WHO Group 1 carcinogen) and sugary drinks are unambiguous F-tier. Watercress is 100/100 on CDC nutrient density. Lentils are the best legume. Walnuts have highest ALA omega-3 of any nut. Kefir has 61 probiotic strains vs. yogurt's ~7. Steel-cut oats beat all other grains for metabolic health.
- Added to index under Food / Nutrition Tier Lists (new section)

## [2026-04-20] autoresearch | Social Confidence & Climbing the Social Ladder
- Created: [[Research - Social Confidence and Climbing the Social Ladder]], [[Social Anxiety Exposure Hierarchy]], [[Social Confidence Building]], [[Social Ladder Climbing]]
- Covers: CBT + graded exposure (80% success rate), 12-week week-by-week plan (Phase 1: fear map + cognitive restructuring → Phase 2: micro-interactions → Phase 3: sustained social skills → Phase 4: advanced confidence), conversation techniques (Leil Lowndes, Dale Carnegie), body language signals, social ladder strategy (value + visibility + consistency + warm introductions)
- Key finding: Most anxious people try Level 3 (networking events/parties) first and fail, reinforcing fear. Building Level 1 (micro-interactions) first removes physiological alarm so Level 3 becomes a skill problem, not an anxiety problem. Identity shift takes 90–180 days of consistent exposure.
- Added to index under Networking / Relationships + Psychology

## [2026-04-20] autoresearch | First Job Roadmap — ASU Freshman in Livermore, CA
- Created: [[Research - First Job Roadmap Livermore CA]], [[First Job Roadmap — Livermore Tri-Valley]], [[Lawrence Livermore National Laboratory]]
- Covers: Tri-Valley employer map (LLNL, Sandia, Lam Research, 10X Genomics, Chevron), LLNL/Sandia internship application timelines (apply Oct–Jan for summer), ASU career resources (Handshake, Global Virtual Internship, Forage), Phase 0–3 roadmap, LinkedIn + GitHub strategy for no-experience freshman
- Key finding: LLNL and Sandia NL are literally in Livermore — highest-leverage employers; 2026 cycle closed, target 2027 by applying Oct 2026; immediate action = local part-time job + LinkedIn + GitHub + Forage simulation
- Added to index under Career / Job Search + Entities

## [2026-04-19] autoresearch | Health Protocol Tier List — Evidence-Based Prescriptions
- Created: [[Health Protocol Tier List]]
- Covers: S–D tier ranking of 28 health protocols with specific prescriptions (temperature, duration, frequency, timing); sauna, cold immersion, Zone 2, VO2 max intervals, strength training, sleep, TRE, red light, breathwork, meditation, and more
- Key finding: Finnish sauna 4×/week is the single most evidence-dense passive health protocol (40% CVD mortality ↓); strength training + walking have the strongest all-cause mortality signal
- Added to index under Biohacking / Optimization

## [2026-04-19] autoresearch | Biohacking Health Products Protocol — Skin, Hair, Oral, Body
- Created: [[Biohacking Health Products Protocol]]
- Covers: evidence-based supplements (S/A/B tiers), full skincare AM/PM protocol with specific brands, haircare with finasteride/minoxidil/ketoconazole protocol, oral care with nHA toothpaste and water flosser protocol
- Added to index under Biohacking / Optimization

## [2026-04-19] ingest | Atomic Habits — James Clear (Books)
- Source: `Books/Atomic Habits - James Clear.md`
- Hash: `a721f6fee0fe6e3cf80b6f6daeb71477`
- Summary: [[Atomic Habits - James Clear]]
- Pages created: [[Atomic Habits - James Clear]], [[James Clear]], [[Habit Loop]], [[Four Laws of Behavior Change]], [[Implementation Intention]], [[Habit Stacking]], [[Two-Minute Rule]], [[Temptation Bundling]], [[Goldilocks Rule]], [[Commitment Device]]
- Pages updated: [[Identity-Based vs Goal-Based Habits]], [[Books]], [[Wiki Index]], [[Wiki Log]], [[Hot Cache]], concepts/_index.md, entities/_index.md, .raw/.manifest.json
- Key insight: Clear's framework is a practical design system — the Four Laws (Obvious / Attractive / Easy / Satisfying) map directly onto the Habit Loop stages, allowing precise intervention at any point in the habit cycle. The 1% compounding principle (1.01^365 ≈ 37.78×) makes even tiny habits high-value. Never Miss Twice is the highest-leverage resilience rule.

## [2026-04-19] autoresearch | Math and Physics Foundations for EE — Calc 1-3, DiffEQ, Mechanics, E&M
- Source: synthesis of curriculum knowledge and E&M/mechanics fundamentals
- Summary: [[Research - Math and Physics Foundations for EE]]
- Pages created: [[Research - Math and Physics Foundations for EE]], [[Calculus in Electrical Engineering]], [[Differential Equations in Electrical Engineering]], [[Classical Mechanics in Electrical Engineering]], [[Electromagnetism Foundations for EE]]
- Pages updated: [[Wiki Index]], [[Hot Cache]], [[Wiki Log]]
- Key insight: Every course in Years 1-2 (MAT 265/266/267, MAT 275, PHY 121/122) has a direct 1-to-1 mapping to EE tools used weekly from EEE 202 onward. Calc 1 → cap/inductor V-I relations. Calc 2 → RMS, energy, Fourier. Calc 3 → Maxwell's equations. DiffEQ → circuit transients and control systems. Mechanics → motor equations and the mechanical-electrical analogy. E&M → capacitors, inductors, transformers, motors from first principles.

## [2026-04-19] action-plans | EE Freshman Action Plans — 6 Skill Plans + 6-Month Timeline
- Summary: [[EE Freshman Action Plans]]
- Pages created: [[EE Freshman Action Plans]]
- Pages updated: [[Wiki Index]], [[Wiki Log]]
- Key insight: 6 ordered action plans for math mastery, LTspice, Python, breadboard/multimeter, Git/GitHub, and Arduino. 6-month combined timeline with milestones and ~5–6h/week investment.

## [2026-04-19] autoresearch | First-Year ASU EE Skills — Freshman Skill-Building Plan
- Source: web research synthesis (ASU curriculum, hiring surveys, Siemens academic report, BLS data, Handshake internship data)
- Summary: [[Research - First-Year ASU EE Skills]]
- Pages created: [[Research - First-Year ASU EE Skills]], [[ASU EE Year 1-2 Curriculum Map]], [[EE Freshman Self-Study Stack]], [[EE Freshman Portfolio Strategy]]
- Pages updated: [[Wiki Index]], [[Hot Cache]], [[Wiki Log]]
- Key insight: ASU Year 1 has zero EE-specific courses — it's all math + physics. The leverage move is self-teaching LTspice + Python + Git + breadboarding before EEE 202 hits in Term 4A. Siemens hiring survey: communication + collaboration ranked #1 soft skill above all technical tools. Git/GitHub portfolio started in Year 1 beats most sophomores at early internship apps.

## [2026-04-19] autoresearch | EE Physical Side Skills — Semiconductors and Power Electronics
- Source: web research synthesis (semiconductor hiring trends, job postings, WBG device testing, learning paths)
- Summary: [[Research - EE Physical Side Skills for Semiconductors and Power]]
- Pages created: [[Research - EE Physical Side Skills for Semiconductors and Power]], [[EE Physical Side — Actionable Skill Plan]]
- Pages updated: [[Wiki Index]], [[Hot Cache]], [[Wiki Log]]
- Key insight: Device physics fluency + double pulse test bench experience + WBG PCB layout are the three hardest hiring filters. The 18-month plan moves through: foundations (Neamen + Erickson + LTspice) → core power design (magnetics + gate drivers + DPT) → WBG specialization (SiC/GaN app notes + >1kW project) → digital control (TI C2000 PI loop). SiC traction inverter and GaN OBC are the two highest-demand specialties in the 2025–2026 EV hiring market. 70,000 new semiconductor jobs projected by 2026.

## [2026-04-19] autoresearch | Complete Biohacking Guide — Tier Lists, Supplements, Biomarkers
- Source: web research synthesis (outliyr.com, onedaymd.com, functionhealth.com, medichecks.com, NIH ODS)
- Summary: [[Research - Complete Biohacking Guide]]
- Pages created: [[Biohacking Tier List]], [[Supplement Tier List Complete]], [[Health Biomarkers Complete Panel]], [[Biohacking Daily Health Hacks]]
- Pages updated: [[Wiki Index]], [[Hot Cache]], [[Wiki Log]]
- Key insight: The highest-ROI biohacks are free — sleep consistency, morning sunlight, Zone 2 cardio, and protein adequacy outperform every supplement. Foundation supplement stack (D3+K2, Magnesium Glycinate, Omega-3, Zinc, Creatine) addresses common deficiencies before any exotic nootropic. ApoB + fasting insulin are the two most actionable blood tests most people never order. Sauna 4×/week has 40% cardiovascular mortality reduction (Laukkanen et al.).

---

## [2026-04-19] ingest | How to Win Friends and Influence People — Dale Carnegie (1936)
- Source: book
- Summary: [[How To Win Friends and Influence People - Dale Carnegie]]
- Pages created: [[Dale Carnegie]]
- Pages updated: [[Books]] (domain), [[Wiki Index]]
- Key insight: Carnegie's 30 principles distill to one root insight — most influence failures come from ignoring the other person's need to feel important and understood. His empirical methods anticipate operant reinforcement (Skinner), identity-consistency (Festinger), and perspective-taking (social cognition research) by decades.

---

## [2026-04-18] ingest | Dwarkesh Patel × Jensen Huang — Nvidia Strategy Interview (2025)
- Source: `.raw/transcripts/Darkesh_Jensen.txt`
- Summary: [[Darkesh-Patel-Jensen-Huang-Nvidia-2025]]
- Pages created: [[Jensen Huang]], [[Dwarkesh Patel]], [[AI Five-Layer Cake]], [[CUDA Ecosystem Flywheel]], [[GPU vs TPU Trade-offs]], [[Accelerated Computing]]
- Pages updated: [[NVIDIA]], [[CUDA Programming Model]], [[Wiki Index]], [[Hot Cache]]
- Key insight: Jensen's framework — AI is a 5-layer cake (energy→chips→platform→models→apps); CUDA moat is a self-reinforcing flywheel of install base + programmability + ecosystem richness; Hopper→Blackwell 50× improvement came primarily from architecture/algorithms (not transistors), proving programmability > specialization. Energy (not chips) is the real multi-year bottleneck.

---

## [2026-04-18] research | Cycling Training Periodization and Annual Plan
- Query: Research on training cycling phases (strength winter / VO2 max summer) + 6-day/week training plan
- Pages created: [[Training Periodization]], [[Polarized Training]], [[VO2 Max Interval Training]], [[Strength Training for Cyclists]], [[Research - Cycling Training Periodization and Annual Plan]]
- Pages updated: [[Wiki Index]], [[Hot Cache]], concepts/_index.md
- Key insight: Strength in winter (4-phase gym arc: Adaptation→Hypertrophy→Strength→Power) followed by VO2 max blocks in spring (2×/week, 2–3 week concentrated blocks) is well-validated. Polarized intensity distribution (80/20) outperforms threshold-heavy training. Short intervals (2–4 min) maximize time above 90% VO2 max more effectively than long efforts.

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
