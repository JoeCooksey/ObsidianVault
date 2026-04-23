---
type: meta
title: "Hot Cache"
updated: 2026-04-22T12:00:00
tags:
  - meta
---
# Recent Context

## Last Updated
2026-04-23 — Autoresearch: How to Find an EE Mentor at ASU — tier list + faculty contacts + Year 1 action stack

## Key Recent Facts

### High Income Skills Tier List — newest autoresearch
- **#1 general skill (2026)**: AI/ML Engineering — $155k–$200k base; LLM specialists +25–40% premium → $200k–$350k; fastest legitimately learnable path to top-decile income
- **#1 EE specialization**: Analog/Mixed-Signal IC Design — median $222k, 90th percentile $349k; 5–10 year mastery curve; Apple/Qualcomm/NVIDIA/ADI/TI compete fiercely; most scarcity-protected EE career
- **Most underrated EE skill**: FPGA Engineering — avg $175k, top earners $251k+; Sandia National Lab (Livermore!) is a direct employer; 2–4 years to proficiency; Verilog/VHDL is the gateway
- **Joe's primary track**: Power Electronics WBG (SiC/GaN) — $112k–$230k; steepest demand growth of any EE field; every EV traction inverter is moving to SiC; 10–20 year demand runway
- **Best on-ramp to $150k+ for EE student**: Embedded Firmware + RTOS — $114k–$244k; C + RTOS + CAN/SPI/I2C; automotive/aerospace/defense; 12–18 months to job-ready
- **Salary multiplier**: EE + Python/AI stack → 20–30% salary premium; engineers who can simulate converters AND automate test data are commanding better offers at Tesla, Apple, Qualcomm
- **Freelance ceilings (for reference)**: ML engineers $120–250/hr; FPGA engineers $100–175/hr; power electronics consultants $75–150/hr
- **EE income ladder for Joe**: Student now → $25–35/hr internship (2027) → $90–120k entry (2029 BS) → $120–160k WBG specialist (2031 MS) → $150–230k senior (2034) → $200–300k principal (2039)

**Joe's 4-Phase Action Plan:**
- **Phase 1 (Apr–Oct 2026)**: Python + LTspice 10-circuit ladder + GitHub 3 repos + breadboard 5 circuits — exploit the zero-EE-courses Year 1 window
- **Phase 2 (Oct 2026 – Apr 2027)**: Erickson + Maksimovic (Fundamentals of Power Electronics Ch. 1–7) + Neamen device physics + STM32/FreeRTOS basics + APPLY to LLNL Oct 2026
- **Phase 3 (Apr 2027 – Oct 2027)**: WBG app notes (Wolfspeed/Infineon/GaN Systems) + double pulse test theory + KiCad 4-layer PCB + TI C2000 LaunchPad + FURI application
- **Phase 4 (Oct 2027 – Apr 2028)**: Choose Track A (FPGA + Verilog → Sandia/LLNL path) or Track B (Python/AI for EE → tech-sector EV path); both are secondary stacks on top of WBG primary

**General High-Income Skills Tier Summary:**
- **S-Tier ($150k–$400k+)**: AI/ML Eng, Analog/Mixed-Signal IC, Semiconductor Eng, FPGA Eng, Cloud Architecture
- **A-Tier ($120k–$180k)**: Embedded Firmware + RTOS, Power Electronics (WBG), Cybersecurity, Data Science, RF/Wireless Eng
- **B-Tier ($80k–$130k)**: Digital/RTL Design, Control Systems, Expert Copywriting, Technical Writing
- **C-Tier ($50k–$90k)**: General EE (non-specialized), Test Engineering, Social Media Marketing, Basic Web Dev

**EE Specialization Key Numbers (2026):**
- Analog/Mixed-Signal IC Design: $191k avg, $349k 90th percentile
- FPGA Engineering: $175k avg, $251k 90th percentile
- Semiconductor Engineering: $189k avg, $326k 90th percentile
- Embedded Firmware Engineering: $168k avg, $245k 90th percentile
- Power Electronics: $132k avg, $210k 90th percentile

### Bulking vs Cutting — previous autoresearch
- **Joe's stats**: 5'9" (1.7526 m), 156 lbs (70.76 kg), BMI 23.04 (healthy range — no urgency to change direction)
- **FFMI at current weight**: ~19.6 @ 15% BF / ~20.7 @ 10% BF / ~18.4 @ 20% BF — decent baseline, meaningful room to grow
- **Decision rule (by BF%)**: <15% → lean bulk | 15–20% → recomp (esp. if <2yr training) | >20% → cut to 12–15% first, then bulk
- **Visual test**: See abs clearly → bulk; faint ab outline → recomp; no abs, noticeable belly → cut first
- **Most likely call at 156 lbs**: BF probably 13–18% for an active person → lean bulk or recomp
- **Lean bulk protocol**: +200–300 cal/day over TDEE; gain 0.25–0.5 lb/week; protein 140–160 g/day; stop at ~18–20% BF
- **Cut protocol**: −300–500 cal/day; lose 0.5–1% bodyweight/week; protein stays HIGH at 128–156 g/day; maintain strength training; stop at 12–15% BF
- **Body recomp (best for beginners)**: Eat at TDEE ± 100–200; protein 140–160 g/day; progressive overload required; track waist + photos + strength, not scale
- **Joe's TDEE** (cycling 6×/week): ~2,800–3,000 cal/day; lean bulk = 3,000–3,300 cal; cut = 2,300–2,500 cal
- **Protein floor**: 140–160 g/day regardless of phase — this is the single most impactful nutritional variable
- **FFMI target milestones at 5'9"**:
  - FFMI 20–21: "Looks like you lift" = ~155–165 lbs @ 12% BF
  - FFMI 22: Great natural physique = **169 lbs @ 12% BF / 175 lbs @ 15% BF** ← realistic 2–4 yr goal
  - FFMI 25: Near natural ceiling = **192 lbs @ 12% BF / 199 lbs @ 15% BF** ← exceptional genetics + 8–10 yr
- **Muscle gain rate**: Beginner Year 1 = 1.5–2 lbs/month; Intermediate Year 2 = 1–1.5 lbs/month; Advanced = 0.25–0.5 lbs/month
- **Lean mass gap**: FFMI 19.6 → 22 requires ~+15 lbs lean mass = 1.5–3 year project at beginner-intermediate rates
- **Critical insight**: Bigger caloric surplus does NOT = more muscle. Intermediate on 1,000 cal surplus builds 5:1 fat-to-muscle ratio; +300 cal/day approaches 1:1–2:1 ratio
- **FFMI natural limit**: ~25 for elite genetic responders; most plateau at 22–23; FFMI >26 = statistical flag for PED use (Kouri et al. 1995)

### LTSpice Skills Guide — newest autoresearch
- **4 simulation types in order**: `.op` (DC bias check, always run first) → `.tran` (time-domain, most used) → `.ac` (Bode plot/frequency response) → `.dc` (sweep a source, I-V curves)
- **10-circuit ladder**: voltage divider → RC filter (Bode plot) → RL transient → RLC resonance → diode rectifier → op-amp inverting → Sallen-Key active filter → MOSFET I-V → buck converter → closed-loop buck
- **Power command**: `.step param R1 100 1k 100` is a for-loop that runs the whole sim for each R1 value — key to sweeping parameters
- **SPICE directive cheat**: S key → type `.tran 10m` or `.ac dec 100 1 1Meg` or `.step param...` — these go directly on the schematic
- **PWM source for power electronics**: `PULSE(0 15 0 10n 10n {D/fs} {1/fs})` — drives a MOSFET gate at duty cycle D and frequency fs
- **Import third-party models**: download `.lib` from TI/Wolfspeed/Infineon → add `.lib "path/to/model.lib"` as SPICE directive → part is now simulatable
- **Monte Carlo**: `R = {mc(1k, 0.05)}` + `.step param run 1 100 1` → 100 random runs showing tolerance spread
- **Most common beginner error**: no DC path to ground → "singular matrix" error; also: forgetting AC 1 attribute on AC source = all-zero Bode output
- **Joe's Phase 1 first session** (1h): install LTSpice → voltage divider → `.op` → verify 4.5V midpoint → RC filter → `.ac dec 100 1 1Meg` → Bode plot appears
- **Key shortcuts**: F2=component, F3=wire, F4=label, G=ground, S=SPICE directive, F7=move, Ctrl+R=rotate
- **Best free resources**: SparkFun Getting Started guide (best written beginner tutorial), Afrotechmods YouTube (best video), LTwiki.org (all SPICE directives), Simon Bramble tutorials (power electronics focus)
- **Month 3 milestone**: simulate a real buck converter with MOSFET model from Wolfspeed + measure efficiency with `.meas` → puts Joe ahead of most juniors at internship time



### Building Social Connections at ASU — newest autoresearch
- **S-Tier**: Technical project club sub-teams (IEEE ASU, Solar Devils) — same 5–10 people weekly, shared mission, career capital simultaneously + Study groups (lab/recitation) — seat proximity = 3–5× friendship odds (2022 Frontiers in Psychology, n=235) + First-year dorm floor (41% friendship rate with next-door neighbor)
- **A-Tier**: Rec sports / cycling club (shared physical effort = fast bonding) + Campus jobs especially undergrad research assistant + Welcome Week (first 2 weeks = unique open window that closes by week 6–8 — say yes to everything)
- **B-Tier**: Large club general meetings without sub-team commitment (upgrade: join a project team) + Greek life (high time/money cost, not ideal for Joe's EE track) + Campus events (one-off, weak ties)
- **C-Tier**: Large lectures without study group formation + ASU Discord / Bumble BFF (best for online students like Joe)
- **D-Tier**: Parties/bar scene (transient crowd, never accumulates 50+ hrs with same person) + cold social media DMs
- **The time math** (Jeffrey Hall, 2019): casual friend = 50 hrs; close friend = 200+ hrs; a study group 3×/week for 12 weeks = 36 hrs; a project team 6×/week for 16 weeks = 96 hrs; parties = <20 hrs total with any one person
- **First 2-week window**: social groups stabilize by week 6–8; Join everything in week 1–2, convert to regular context fast
- **Joe's online barrier**: proximity mechanisms (dorms, seats) are limited by hybrid setup; fix = IEEE sub-team (if on campus), ASU EE Discord (digital), Makerspace visits
- **Joe's action stack**: IEEE ASU sub-team (electrical/battery/power) + MAT 265 study group week 1 + Welcome Week yes-to-everything + ASU EE Discord
- **Key insight**: 2 deep contexts > 10 surface ones. Pick IEEE and one other, go deep in both. The people you meet in IEEE become your internship network, study partners, and lifelong connections.

### Free Time Tier List — newest autoresearch
- **S-Tier (maximum compounding)**: EE self-study (LTspice/Python/Git/breadboard — Year 1 leverage window, zero EE courses = exploit this gap NOW) + Deep reading (books from Phase 1–3 list = top 1% cognitive compounding) + Quality in-person social time (Harvard 80-year study: relationships > career/money for late-life happiness AND health)
- **A-Tier (compound slowly, do consistently)**: Side projects/GitHub (identity capital + internship portfolio) + Clubs — IEEE ASU, Solar Car (warm network via repeated contact) + Deliberate rest (walks, naps, journaling — not scrolling) + Weekly journaling/review (42% better goal follow-through)
- **B-Tier (supporting role, use during lower-intensity time)**: High-quality educational media (Huberman Lab, 3Blue1Brown, Lex Fridman — use for Zone 2 cardio sessions) + Cooking (life skill compounding daily for 60+ years) + Outdoor time (cortisol ↓, attention restoration theory)
- **C-Tier (fine in moderation)**: Gaming (capped 1–2 hrs/week) + Casual TV (intentional, one series at a time) + Passive socializing (fine, lower compounding than activity-based)
- **D-Tier (time sinks)**: Social media browsing (degrades attention — measured P300 reduction in TikTok heavy users; US adults average <16 min/day reading, down from 23 min; these cannibalize each other directly) + Regular heavy drinking (disrupts sleep architecture, money, cognition)
- **F-Tier (actively harmful)**: Doom-scrolling at night (blue light → delayed melatonin → less REM → worse cognition next day → craving more scrolling — measurable loop) + Comparison scrolling (upward social comparison = one of most reliable happiness reducers in social psychology)
- **The core insight**: The biggest lever is not adding more S-tier activities — it's **eliminating D/F defaults that fill idle gaps by inertia**. Phone out of bedroom, 20-min social media cap, default answer ready for "what do I do now?"
- **Optimal free time**: 2–5 hrs/day maximizes happiness (Rutgers/Holmes research); <2 hrs = stress; >5 hrs passive/solo = boredom/meaninglessness; 5+ hrs social/active = fine
- **Joe's top opportunity**: He already does S-tier exercise (6 days/week cycling). The gap is EE self-study + reading + eliminating passive phone time.

### Where to Get Cheap Books — newest autoresearch
- **S-tier free**: Libby app (library card = free ebooks + audiobooks; #1 most underused tool) + BookBub (free daily $0–$1 ebook deals, 40+ genres, no subscription) + Project Gutenberg (70k+ public domain classics free)
- **Book swapping**: BookMooch / PaperBackSwap — list books you own, earn credits, request others; completely free exchange
- **Little Free Library**: take a book, leave a book; neighborhood network
- **Best paid used-book sites**: ThriftBooks (#1 overall — 13M titles, free shipping >$10, rewards program) + Better World Books (cheap + funds literacy nonprofits; 6-for-$15 sales) + AbeBooks (books from $1; individual sellers) + Book Outlet (50–90% off new overstock)
- **Price comparison tools**: BookFinder.com (compares 100k+ sellers simultaneously) + BookScouter.com (best for textbooks) — run these before buying anything >$10
- **Kindle Unlimited**: $9.99/month; worth it if reading 3+ books/month; 4M+ titles including indie/self-published
- **Physical hunting**: thrift stores ($0.50–2), library book sales ($0.25–3, sometimes $1/bag day), Half Price Books stores, garage/estate sales
- **Joe's reading list cost**: 9-book Phase 1–2 list costs ~$0 via Libby, or ~$25–35 total buying all via ThriftBooks
- **Decision tree**: public domain? → Project Gutenberg free. Can wait 1–2 weeks? → Libby. Want ebook deal? → BookBub. Want physical now? → BookFinder then ThriftBooks.

### Top MS EE Programs — Physical Side — newest autoresearch
- **NC State MS-WBGS**: only dedicated MS in Wide Bandgap Semiconductors in the US; launches Fall 2026; covers SiC/GaN device physics, fabrication, characterization, EV power systems; plugged into PowerAmerica (49 WBG industry members) and FREEDM Center; hybrid online + on-campus summer practicum; **highest-leverage program for Joe's WBG career track**
- **Virginia Tech CPES**: Center for Power Electronics Systems; #1 power electronics research institution; $6–7M annual research, ~100 researchers; MS (research-based) or MEng (project-based); best for converter/inverter/magnetics focus
- **UT Austin SSE**: new Fall 2025 MS in Semiconductor Science and Engineering; 4 tracks (manufacturing, circuits & systems, heterogeneous integration, devices); industry-funded fellowships cover tuition + stipend + health insurance; GRE not required; Samsung/TI/NXP/Applied Materials all local
- **Purdue**: online-available MS in Microelectronics & Semiconductors within top-10 engineering school; best option if working full-time concurrent
- **MIT / Stanford / Berkeley**: tied #1 globally but not physical-side specialists; extremely competitive; best for academic/research track or broadest career optionality
- **Selection rule**: WBG semiconductors → NC State; power converters/inverters → VT CPES; semiconductor fabrication → UT Austin; online/concurrent → Purdue; maximum optionality → MIT/Stanford/Berkeley
- **Joe's recommended path**: FURI in Year 2 at ASU → apply NC State MS-WBGS or VT CPES during senior year → LLNL/Sandia have direct collaborations with NC State PowerAmerica → loops back to Livermore career plan
- **Admission signals**: GPA ≥ 3.0 minimum (competitive = 3.5+); GRE mostly optional; research/lab experience high weight at VT/MIT/Stanford; must name specific faculty in SOP

### College Dating Guide — previous autoresearch
- **S-Tier methods**: Clubs & organizations (repeated contact + shared interest = no cold approach needed) + Classes/study groups (weeks of exposure, free conversation starters)
- **A-Tier methods**: Campus social events/parties + Hinge (best app for relationships, prompts force better openers) + Tinder University (largest college user pool)
- **B-Tier**: Bumble (women message first = higher signal) + Campus jobs + Dorms
- **C-Tier**: Cold approach (open contexts only) + OkCupid/CMB
- **D-Tier**: Bars/clubs + cold DMs
- **App rankings**: Hinge = best for relationships; Tinder = most volume; Bumble = best signal quality; eHarmony = serious relationships only
- **The Ask Formula**: 3–5 interactions first → remember specific details from prior conversations → ask when conversation is flowing → "Would you want to get [dinner] at [specific place] on [specific day]?" → one re-offer max
- **93% of women prefer in-person ask** over text/app message
- **95% found it meaningful** when a guy remembered specific conversation details — biggest underused advantage
- **Specificity is the #1 differentiator**: "hang out sometime" = low intent; "dinner at [X] on Friday" = high intent, far more effective
- **Physical baseline** (prerequisite): daily hygiene, consistent exercise (Joe already trains 6 days/week = top 5%), 2–3 specific genuine interests to talk about
- **Mindset**: dating is not a transaction; rejection is data not verdict; consistency (showing up weekly) beats grand gestures; be the person worth dating first
- **50% of engaged couples** met through apps/websites (up from 39% eight years ago); 78% of app users feel emotionally drained — use apps as supplement, not replacement

### Book Recommendations — newest autoresearch
- **6 domains covered**: Finance & Investing, Self-Help & Discipline, Stoicism & Philosophy, Psychology & Persuasion, Business & Entrepreneurship, Fiction
- **Finance S-tier**: *The Intelligent Investor* (Graham) — value investing bible; *The Psychology of Money* (Housel) — best starting point for 20s; *The Essays of Warren Buffett*
- **Finance A-tier**: *Just Keep Buying* (Maggiulli, data-driven), *I Will Teach You to Be Rich* (Sethi, 20s practical), *The Little Book of Common Sense Investing* (Bogle, index fund case)
- **Self-Help S-tier**: *Atomic Habits* (already ingested ⭐⭐⭐⭐⭐); *Can't Hurt Me* (Goggins, 40% rule — you're only at 40% when you think you're done); *Deep Work* (Newport, focused work is the rarest valuable skill)
- **Discipline A-tier**: *Essentialism* (McKeown, less but better), *Man's Search for Meaning* (Frankl, meaning > pleasure), *Make Your Bed* (McRaven, small wins compound), *12 Rules for Life* (Peterson)
- **Stoicism S-tier**: *Meditations* (Marcus Aurelius, most re-readable philosophical text; Hays translation); *Ego Is the Enemy* (Holiday, MOST important for ambitious young men); *The Obstacle Is the Way* (Holiday)
- **Stoicism A-tier**: *Letters from a Stoic* (Seneca, Letter 1 = most important letter on time ever written), *The Daily Stoic* (Holiday, best on-ramp)
- **Psychology S-tier**: *Influence* (Cialdini, 6+1 principles: reciprocity, commitment, social proof, authority, liking, scarcity, unity); *Never Split the Difference* (Voss, tactical empathy + mirroring); *How to Win Friends* (Carnegie)
- **Psychology A-tier**: *Thinking, Fast and Slow* (Kahneman, System 1/2; loss aversion; cognitive biases); *Getting to Yes* (Fisher/Ury, BATNA + principled negotiation)
- **Business S-tier**: *Zero to One* (Thiel, monopoly thinking, the contrarian question); *Good to Great* (Collins, Level 5 leadership + hedgehog concept + flywheel); *Shoe Dog* (Knight, best business autobiography); *The Lean Startup* (Ries, build-measure-learn)
- **Fiction S-tier classics**: *The Count of Monte Cristo* (most gripping classic; patience theme); *East of Eden* (timshel — "thou mayest" — who you choose to become); *Crime and Punishment* (cautionary tale of intellectual arrogance); *1984* (most relevant every year); *The Road* (most emotionally powerful 200-page book)
- **Fiction S-tier modern**: *Dune* (leadership, ecology, messiah warning; read before films); *All Quiet on the Western Front* (19yo German soldier = your age)
- **Joe's Phase 1 reading order**: Psychology of Money → Ego Is the Enemy → Deep Work → Can't Hurt Me
- **Joe's Phase 2**: Intelligent Investor (ch. 1, 8, 20) → Never Split the Difference → Zero to One → Count of Monte Cristo
- **Joe's Phase 3**: Meditations → Thinking Fast and Slow → East of Eden → Man's Search for Meaning

### Food Health Tier Lists — newest autoresearch
- **Holy Trinity** (agreed upon by every dietary framework): Dark leafy greens + fatty fish + berries
- **S-tier overall foods**: Wild salmon, sardines, watercress (100/100 CDC score), spinach, blueberries, lentils, walnuts, chia seeds
- **F-tier overall foods**: Processed meats (WHO Group 1 carcinogen), sugary drinks (linked to 32 chronic conditions), ultra-processed snacks (60% of American diet), high-mercury fish
- **Vegetables**: Watercress = 100/100 CDC nutrient density; cruciferous (broccoli/kale/bok choy) → sulforaphane → cancer-cell inhibition; dark green > light green always
- **Fruits**: Berries dominate (blackberries GI ~25, raspberries 8g fiber/cup, blueberries highest antioxidants); avocado = S-tier fruit; never juice (strips fiber)
- **Meats/Seafood**: Omega-3 content is the primary differentiator; wild salmon 1.8g EPA+DHA, sardines 2g (highest + lowest mercury); processed meats = WHO carcinogen
- **Legumes**: Lentils = S-tier (highest fiber, lowest GI ~30, easiest to digest); ALL Blue Zone populations eat legumes daily; 28g/day nuts → 21% ↓ CVD
- **Nuts/Seeds**: Walnuts highest ALA omega-3; chia 10g fiber per 2 tbsp; Brazil nuts: 2/day max (selenium toxicity risk >2/day)
- **Grains**: Oats GI 9–11 (steel-cut) with beta-glucan → FDA heart-disease health claim; barley GI 25–35; white bread GI 70–95 (D-tier); whole > refined always
- **Dairy**: Fermentation hierarchy: kefir (61 probiotic strains) > plain yogurt > cheese > milk > processed cheese; always buy plain (add your own flavoring)
- **Universal rule**: Whole > processed at every level; color intensity = phytochemical content; omega-3 = health predictor in proteins; ultra-processing = harm

### Social Confidence & Social Ladder — previous autoresearch
- **Gold standard**: CBT + graded exposure therapy → 80% of people with social anxiety respond; gains maintained years later
- **The core tool — Fear Hierarchy (SUDS 0–100)**: Work bottom-up; don't advance until current step drops to ≤25. Start: eye contact+nod (SUDS 10) → smile at cashier (15) → ask stranger directions (35) → join group convo (55) → introduce yourself at party (65) → express opinion that might be disagreed with (75) → networking event alone (80)
- **Cognitive restructuring**: Social anxiety is maintained by automatic negative thoughts. Challenge each ANT: what's the evidence? Frame situations as experiments, not performances.
- **Three Staircase Levels**: Level 1 = micro-interactions with strangers → Level 2 = sustained conversations → Level 3 = high-stakes (groups, networking, status). Most anxious people skip to Level 3 and fail, confirming their fear.
- **Key conversation techniques (Leil Lowndes)**: Flooding Smile (pause then smile slowly) + Sticky Eyes (hold eye contact past natural break) + Big-Baby Pivot (full body turn) + Open questions ("what/how/tell me more") + Mirroring + Limit Fidget
- **Body language signals**: Slow movements = composure; 60–70% eye contact; downward inflection at end of sentences; stillness > fidgeting
- **Climbing the social ladder**: Value (develop interesting skills/opinions/stories) + Visibility (show up consistently to right contexts) + Consistency (follow up = where the relationship is built). High-status people reached through warm introductions, not cold approach.
- **Identity shift is the long game**: 90–180 days of consistent exposure → self-concept shifts from "I struggle socially" to "I connect easily." Each action is a vote for who you're becoming.
- **12-week plan**: Week 1-3 = fear map + cognitive restructuring + mindfulness; Week 4-6 = micro-interactions (strangers, cashiers, 2-min convos); Week 7-9 = group entry, deep listening, expressing opinions; Week 10-12 = initiate plans, networking events, lead social contexts

### First Job Roadmap — Livermore CA — previous autoresearch
- **Joe's geographic advantage**: LLNL and Sandia National Lab are literally in Livermore — 5–10 min drive; highest-leverage employers on the planet for an EE student
- **LLNL Engineering Summer Internship**: Applications open ~October each year; 2026 closed; **target 2027 — apply Oct 2026**; pay ~$25–35/hr undergrad
- **Sandia DOE CCI Program**: Applications due ~Jan 7 each year; GPA ≥ 3.0 required; 10-week full-time paid summer
- **Immediate actions (Phase 0)**: Get any local job this week (Tri-Valley Career Center) + LinkedIn (EE headline + Livermore location) + GitHub (3 repos, even tiny) + Forage simulation (free, goes on resume)
- **ASU resources**: Handshake (30k+ postings) + Global Virtual Internship (remote credit, 13k companies) + free career services
- **Other Tri-Valley targets**: Lam Research (Fremont, semiconductor equip), 10X Genomics (Pleasanton, biotech), Chevron (San Ramon), PG&E
- **LinkedIn headline formula**: "EE Student @ ASU | Python + LTspice + Embedded Systems | Seeking 2027 Summer Internship"
- **Roadmap phases**: Phase 0 (now) = local job + LinkedIn + GitHub + Forage → Phase 1 (summer 2026) = ASU virtual internship + personal project → Phase 2 (Oct 2026) = LLNL/Sandia apply → Phase 3 (2027) = first engineering internship

### Health Protocol Tier List — newest autoresearch
- **S-Tier non-negotiables**: Strength training 2–4×/week (−15–27% mortality), Zone 2 cardio 150+ min/week (VO2 max + mito), VO2 max intervals 4×4 min at 90–95% HR, Finnish sauna 80–100°C 20 min 4–7×/week (−40% CVD mortality), sleep 7–9h fixed wake, walking 7–10k steps/day (−50% mortality vs. <4k)
- **Finnish sauna is the most evidence-dense passive protocol**: Laukkanen et al. n=2,315, 20-yr follow-up; dose-response linear; 4–7×/week → 63% ↓ sudden cardiac death
- **Cold water immersion (A-tier)**: 10–15°C, 10–15 min; ↑ norepinephrine 200–300%; exercise recovery; DO NOT do within 4–6h of strength training (blunts mTOR)
- **TRE 16:8 (A-tier)**: significant improvement in fasting glucose, HOMA-IR, HDL-C (2025 meta-analysis); benefit mostly in sedentary people; active athletes see less metabolic benefit
- **Red light therapy (A-tier)**: 630–850 nm, 10–20 min/day; RCT-confirmed for hair loss, skin collagen, wound healing; 2025 consensus review by 20+ specialists
- **Breathwork (B-tier)**: Cyclic sighing (double inhale + long exhale) beat meditation for acute anxiety in 2023 Stanford RCT; box breathing = acute stress regulation; free
- **D-tier confirmed**: Detox cleanses, colonics, young plasma, GH anti-aging injections, ozone therapy — no mechanism or net harmful
- **Joe protocol stack**: Fixed wake + 7-9h sleep → morning sunlight → Zone 2 (cycling) → strength 2–3×/week → sauna 3–4×/week post-workout → CWI post-endurance (not post-lift) → TRE 16:8

### Biohacking Health Products Protocol — previous autoresearch
- **Skincare non-negotiable**: SPF 50 daily (EltaMD UV Clear) + retinoid at night (start Differin, graduate to tretinoin); UV = 80% of visible facial aging
- **AM routine**: Vitamin C serum (TruSkin or Timeless) → moisturizer (CeraVe) → SPF 50
- **PM routine**: cleanser → niacinamide or copper peptides → retinoid → moisturizer; retinol PM only; don't mix with vitamin C
- **Hair loss gold standard**: Finasteride 1 mg/day (oral) + Minoxidil 5% topical 2×/day + Nizoral 2% shampoo 3×/week; finasteride reduces scalp DHT by ~70%; stops loss in >80% of men
- **Hair alternatives (OTC)**: Pumpkin seed oil 400 mg (40% hair count increase in RCT) + Saw Palmetto 320 mg + LLLT cap 3×/week
- **Oral care hierarchy**: brush 2 min electric brush (Oral-B iO) + floss first + water flosser (Waterpik Aquarius) + tongue scraper; spit, do NOT rinse after brushing
- **nHA toothpaste**: Boka or RiseWell — nano-hydroxyapatite remineralizes enamel comparably to fluoride; SLS-free; no microbiome disruption
- **Avoid**: alcohol-based mouthwash daily (strips good bacteria); biotin mega-dosing (no benefit unless deficient); most DHT-blocking shampoos (Nizoral is the exception)
- **Health supplement S-tier**: Creatine 5 g + D3+K2 + Magnesium Glycinate 300–400 mg PM + Omega-3 2–3 g EPA/DHA + Zinc 15–25 mg
- **Collagen peptides A-tier**: 10–15 g/day; co-ingest vitamin C to double synthesis; proven skin elasticity, hair thickness improvement

### Atomic Habits (James Clear) — previous ingest
- **North Star quote**: "You do not rise to the level of your goals. You fall to the level of your systems."
- **1% compounding**: 1.01^365 ≈ 37.78×; 0.99^365 ≈ 0.03. Tiny habits compound dramatically in both directions.
- **Habit Loop**: Cue → Craving → Response → Reward. Craving is the key addition over Duhigg's 3-step model — dopamine fires on anticipation, not just reward.
- **Four Laws**: Make it Obvious (cue design) / Make it Attractive (craving design) / Make it Easy (response friction) / Make it Satisfying (reward design). Each law inverts for breaking bad habits.
- **Implementation Intention**: "I will [Behavior] at [Time] in [Location]." Closes the intent-action gap; 2–3× follow-through improvement in research.
- **Habit Stacking**: "After [Habit A] I will [Habit B]." Borrows the neural trigger of an existing habit for the new one.
- **Two-Minute Rule**: Any new habit must start as a <2 min action. Master showing up first; scale later. Targets [[Limbic Friction]] directly.
- **Temptation Bundling**: Pair WANT + NEED. Dopamine from anticipating the want bleeds into the need. Joe's action item: favorite playlist only during study sessions.
- **Goldilocks Rule**: Peak motivation at edge of ability. Boredom (not failure) is the long-run enemy of habit maintenance.
- **Never Miss Twice**: One miss = accident. Two misses = new (bad) habit starting. Highest-leverage resilience rule per Joe.
- **Identity as mechanism**: Every execution casts a vote for who you are becoming. Deepens [[Identity-Based vs Goal-Based Habits]] with evidence-accumulation framing.
- Joe rating: ⭐⭐⭐⭐⭐, finished ~March 1, 2026

### Math and Physics → EE (previous — autoresearch)
- **Calc 1 = Cap/inductor V-I**: $i = C\,dv/dt$ and $v = L\,di/dt$ are pure derivatives — you use Calc 1 every lecture in EEE 202
- **Calc 2 = RMS, energy, Fourier**: $V_\text{rms} = \sqrt{\frac{1}{T}\int v^2\,dt}$; energy = $\tfrac{1}{2}CV^2$; Fourier coefficients are integrals — all Calc 2
- **Calc 3 = Maxwell's equations**: gradient, divergence, curl appear in all 4 of Maxwell's equations; without Calc 3, EEE 340 Electromagnetics is inaccessible
- **DiffEQ → circuit transients**: RC circuit is a 1st-order ODE; RLC is 2nd-order with natural freq $\omega_n = 1/\sqrt{LC}$ and damping $\zeta = R/(2\sqrt{L/C})$
- **Laplace transform = the engineering shortcut**: converts ODE to algebra; transfer function $H(s)$ encodes poles, stability, Bode plot — foundation of EEE 202 + EEE 350
- **Mechanical-electrical analogy is exact**: mass↔inductance, spring↔capacitance, damper↔resistance; same ODE; solving one solves both; MEMS sensors are this analogy in silicon
- **Faraday's law = transformer operation**: $\mathcal{E} = -N\,d\Phi/dt$ is WHY transformers work; every switching power supply (buck, flyback) uses this
- **Lorentz force = motor torque + Hall sensor**: $\mathbf{F} = q\mathbf{v}\times\mathbf{B}$ gives motor torque ($\tau = BILN$) and Hall voltage ($V_H = IB/nqt$); PCB trace inductance is also this force
- **Joe's year-1 payoff**: MAT 265 → EEE 202 V-I relations; MAT 266 → EEE 202 energy/RMS; MAT 267 → EEE 340 fields; MAT 275 → EEE 202 transient analysis; PHY 121 → EEE 480 motor control; PHY 122 → EEE 340 all components

### First-Year ASU EE Skills (previous — autoresearch)
- **ASU Year 1 has zero EE courses** — it's all math (MAT 265/266/267) + physics (PHY 121/122); first EE course (EEE 120 Digital Design) doesn't hit until Term 3A (Year 2)
- **The leverage move**: self-teach LTspice + Python + Git + breadboarding in Year 1 before EEE 202 Circuits I (Term 4A) — this separates "thriving" from "surviving" students
- **LTspice is free and used in EEE 202** — 10 hours of self-study before Circuits I = massive advantage; build RC, RL, RLC circuits
- **Python before MATLAB**: Python is the practical scripting language; MATLAB is the academic/signals standard (also used in EEE 202); learn both, Python first
- **Breadboard + multimeter = $50** — buy now; build 5 circuits (LED → voltage divider → RC filter → transistor switch → op-amp buffer) before any EE coursework
- **Git/GitHub portfolio in Year 1** beats sophomore-level candidates for early internships; post even small Arduino/Python projects
- **Siemens hiring survey**: communication + collaboration ranked #1 and #2 skills for early-career EE hires — above all technical tools
- **ASU resources**: FURI (apply sophomore year), Solar Car Team (open to freshmen), IEEE ASU Branch, ASU Makerspace
- **7 hottest hiring skills (2026)**: electrical wiring, electrical design, control systems (+69% YoY), troubleshooting (+38%), systems design, CAD tools, communication
- **Joe context**: Year 1 = the math window; build LTspice + Python + breadboard now; GitHub portfolio before first internship app season (summer after freshman year)

### EE Physical Side — Hiring & Skills (previous — autoresearch)
- **Three hardest hiring filters**: (1) device physics fluency — can you derive switching loss? (2) double pulse test experience — can you set one up and interpret Eon/Eoff? (3) WBG PCB layout — power loop inductance, Kelvin gate, commutation loop minimization
- **18-month skill plan**: Foundations (Neamen + Erickson + LTspice) → Core power design (magnetics + gate drivers) → WBG specialization (SiC/GaN app notes + >1kW project) → Advanced (TI C2000 digital control + EMC + thermal sim)
- **Hottest EE specialties 2025–2026**: SiC traction inverter engineers (Wolfspeed, Onsemi, STMicro) and GaN OBC engineers (Navitas, EPC, GaN Systems) — $112k–$230k salary range
- **The DPT is the bench litmus test**: If you can't explain what Eon, Eoff, Qrr mean or how a double pulse test works, you won't pass a power lab interview
- **Textbook stack**: Erickson & Maksimovic *Fundamentals of Power Electronics* (the bible) + Neamen *Semiconductor Physics and Devices* — read both in parallel from month 1
- **Digital control matters now**: TI C2000 F28379D is the dominant automotive power DSP; PI current control in fixed-point arithmetic is expected at mid-level
- **70,000 new US semiconductor jobs by 2026** — employers increasingly value demonstrated skill over credentials due to talent shortage
- **Joe context**: 19-year-old EE student — this plan is executable now; Phase 1 starts with coursework overlap; Phase 2–3 = summer/capstone project territory

### Biohacking (previous — autoresearch)
- **Free hacks dominate**: Morning sunlight, 8h consistent sleep, Zone 2 cardio, and protein adequacy outperform every supplement and device
- **Foundation supplement stack**: D3+K2 | Magnesium Glycinate | Omega-3 (EPA+DHA) | Zinc | Creatine — fix deficiencies before adding nootropics
- **Most important blood tests**: ApoB (<70 mg/dL optimal) + Fasting Insulin (<5 μIU/mL) + HbA1c (4.8–5.2% optimal) — these three reveal most metabolic risk early
- **Sauna evidence**: 4×/week Finnish sauna = ~40% reduced cardiovascular mortality (Laukkanen et al., n=2,315, 20-year follow-up)
- **CGM is highest-information biohack**: 2-week continuous glucose monitor reveals personal food responses; keep glucose 70–90 mg/dL
- **S-tier supplements**: Creatine monohydrate, Caffeine+L-Theanine (cognitive); Magnesium Glycinate (sleep); Vitamin D3 (deficiency)
- **Biohacking tier list**: 10 categories (sleep, exercise, temperature, light, nutrition/fasting, stress, wearables, cognitive, longevity, gut)
- **ApoB > LDL-C**: ApoB directly counts atherogenic particles; LDL-C misleading in lean-mass hyper-responders
- **Supplement industry caution**: Only 16% of cognitive supplement labels had per-ingredient safety warnings; underdosing is endemic
- **For Joe specifically**: Start blood panel with D3, ferritin, testosterone (total+free), SHBG, HbA1c, fasting insulin, CBC, CMP, ApoB

### Nvidia Strategy (previous — Jensen Huang interview)
- **Electrons → Tokens**: Jensen's core mental model for Nvidia
- **Five-Layer Cake**: AI stack = energy → chips → compute platform → models → applications
- **CUDA Flywheel**: install base + programmability + ecosystem richness → self-reinforcing moat
- **Energy is the real bottleneck** (not chips); Hopper→Blackwell 50× mostly architecture/algorithms

### Cycling Periodization (previous)
- Annual arc (5 phases): Base+Strength (Oct–Dec) → Build+Power (Jan–Mar) → VO2 Max Blocks (Apr–May) → Competition (Jun–Aug) → Transition (Sep–Oct)
- Polarized model (Seiler): 80% Zone 1 / ~20% Zone 3; 6-day/week training plan

## Recent Changes
- Created: [[Research - Bulking vs Cutting Body Composition Guide]] + [[Bulk and Cut Decision Framework]] + [[FFMI Natural Muscle Potential]] — full body composition guide for 5'9" / 156 lb male; FFMI reference table; lean bulk/cut/recomp protocols; Joe-specific calorie math
- Created: [[Research - LTSpice Skills Guide]] + [[LTSpice Complete Skills Guide]] — complete LTSpice reference: 4 simulation types, 10-circuit build ladder, all SPICE directives, power electronics simulation, Monte Carlo, model import, common mistakes, Joe's 4-phase timeline
- Created: [[Research - Building Social Connections at ASU]] + [[ASU Social Connection Methods Ranked]] — S–D tier list for ASU friendship methods; proximity science; Jeffrey Hall 50–200 hr formula; Joe's action stack
- Created: [[Research - Where to Get Cheap Books]] + [[Book Sourcing Strategy]] — full S–D tier list for cheap/free books; Libby, BookBub, ThriftBooks, BookFinder; Joe-specific path
- Created: [[Research - Top MS EE Programs Physical Side]] + [[MS EE Programs Power Electronics Semiconductors]] — 10-school comparison, NC State WBG MS + VT CPES + UT Austin SSE deep dives, Joe-specific path recommendation
- Created: [[Research - College Dating Guide for Young Men]] + [[College Dating Methods Ranked]] — all methods ranked S–D, app comparison, ask formula, baseline stack
- Created: 8 food health tier list pages (Overall, Vegetables, Fruits, Meats & Seafood, Legumes, Nuts & Seeds, Grains, Dairy) + [[Research - Food Health Tier Lists]]
- Created: [[Research - Social Confidence and Climbing the Social Ladder]], [[Social Anxiety Exposure Hierarchy]], [[Social Confidence Building]], [[Social Ladder Climbing]]
- Created: [[Health Protocol Tier List]] — 28 protocols ranked S–D with specific prescriptions (dose, temp, frequency, timing)
- Created: [[Research - First-Year ASU EE Skills]], [[ASU EE Year 1-2 Curriculum Map]], [[EE Freshman Self-Study Stack]], [[EE Freshman Portfolio Strategy]]
- Created: [[Research - EE Physical Side Skills for Semiconductors and Power]], [[EE Physical Side — Actionable Skill Plan]]
- Created: [[Biohacking Health Products Protocol]] — skincare, haircare, oral care, supplements with full protocols
- Created: [[Biohacking Tier List]], [[Supplement Tier List Complete]], [[Health Biomarkers Complete Panel]], [[Biohacking Daily Health Hacks]]
- Created: [[Research - Complete Biohacking Guide]]
- Updated: [[Wiki Index]], [[Wiki Log]], [[Hot Cache]]

## Active Threads
- **EE Grad School**: NC State MS-WBGS (Fall 2026 launch) is the direct pipeline for Joe's WBG career track; VT CPES for pure power electronics; target FURI Year 2 to build research profile for grad applications
- **EE Freshman Year**: Joe is in Year 1 at ASU — no EE courses yet; self-study window for LTspice, Python, breadboarding, Git NOW before EEE 202 hits Term 4A
- **EE Career**: Joe is a 19yo EE student — physical side skill plan (WBG power electronics) is directly applicable to internship and capstone targeting
- **WBG × EV**: SiC traction inverter and GaN OBC are highest-demand 2025–2026; existing wiki content on WBG/800V/EV charging topology is directly relevant to career plan
- **Biohacking × Cycling**: VO2 max training is S-tier intervention; sauna post-workout relevant to Joe's 6-day/week schedule
- **Supplement × EE student**: Caffeine+L-theanine + creatine + bacopa stack is the core exam-period protocol
- **Biomarkers → action**: Joe should get baseline bloodwork (D3, ferritin, testosterone, HbA1c, fasting insulin, ApoB) as a young male
- Personal context: 19-year-old male EE student, trains 6 days/week, rest Sunday
