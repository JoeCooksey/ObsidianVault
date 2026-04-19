---
type: concept
title: "EE Freshman Action Plans"
status: developing
created: 2026-04-19
updated: 2026-04-19
tags:
  - electrical-engineering
  - ASU
  - action-plan
  - freshman
  - skills
---

# EE Freshman Action Plans

Concrete, ordered action plans for each top skill. Execute these alongside Year 1 coursework (MAT 265/266/267 + PHY 121/122). No EE courses until Term 3A — use this time.

---

## Action Plan 1 — Math Mastery (Calc I → Diff Eq)

**Why**: Fourier series, Laplace transforms, and complex phasors from MAT 267 + MAT 275 are the literal language of Circuits I and Signals & Systems. Students who "passed" but didn't internalize these hit a wall in Term 4A.

**Steps (in order)**:
1. In every calc lecture, ask "where does this show up in engineering?" — look up one application per topic
2. After each MAT 265/266 chapter, work 5 extra problems from a solutions manual (Schaum's Calculus is good)
3. When you reach integration techniques and series (MAT 266): **these are Fourier**. Treat them like EE, not pure math
4. During MAT 267 (multivariable): focus especially on partial derivatives and line integrals — they reappear in Electromagnetics (EEE 241)
5. Preview MAT 275 (Diff Eq) in summer after Year 1: 3Blue1Brown "Differential Equations" playlist (YouTube, free) — watch before the course starts
6. In MAT 275: when you learn Laplace transforms, immediately look up how they're used in circuit analysis (EEE 202 preview)

**Milestones**:
- [ ] Finish MAT 265 with genuine fluency in limits, derivatives, chain rule, optimization
- [ ] Finish MAT 266 with genuine fluency in integration by parts, series, Taylor series
- [ ] Finish MAT 267 with understanding of gradient, divergence, curl (these are Maxwell's equations)
- [ ] Watch 3B1B Diff Eq series before MAT 275 starts

**Time investment**: 5–8 extra hours/week on top of coursework.

---

## Action Plan 2 — LTspice (Circuit Simulator)

**Why**: LTspice is required in EEE 202 (Circuits I, Term 4A). Arriving knowing it transforms the course from stressful to confirmatory — you simulate what lecture explains.

**Steps (in order)**:
1. **Day 1**: Download LTspice free from Analog Devices (analog.com/en/design-center/design-tools-and-calculators/ltspice-simulator.html)
2. **Week 1** (4h): Watch "LTspice for Beginners" on YouTube (IEEA channel or Afrotechmods). Build a simple voltage divider. Run DC operating point simulation.
3. **Week 2** (3h): Build a RC low-pass filter. Run an AC frequency sweep (.ac dec 100 1 1Meg). Watch the Bode plot appear. This is literally EEE 202 content.
4. **Week 3** (3h): Build a RL circuit. Run a transient simulation (.tran). Watch the inductor current ramp. Add a diode — watch clamping behavior.
5. **Week 4** (3h): Build a RLC circuit. Observe resonance. Adjust R to see overdamped/underdamped/critically damped responses.
6. **Month 2**: Simulate an op-amp in inverting and non-inverting configuration. This previews EEE 334 (Circuits II).
7. **Screenshot every simulation** → save in a folder → this becomes portfolio evidence.

**Milestones**:
- [ ] Installed and ran first DC simulation
- [ ] Built and swept an RC filter (Bode plot)
- [ ] Built an RLC circuit and observed resonance
- [ ] Simulated a basic op-amp circuit
- [ ] Have 5 screenshots saved for portfolio

**Time investment**: ~3–4h/week for one month, then occasional use.

---

## Action Plan 3 — Python Basics

**Why**: Python is the EE scripting and data analysis language. Not formally taught in the ASU EE track until upper-division or electives. Employers expect it at internships.

**Steps (in order)**:
1. **Day 1**: Install Python 3.x from python.org (free). Install VS Code (free editor).
2. **Week 1** (5h): Work through "Automate the Boring Stuff with Python" Ch. 1–6 (free at automatetheboringstuff.com). Learn: variables, strings, lists, loops, functions, if/else.
3. **Week 2** (3h): Install numpy and matplotlib via pip. Plot a sine wave: `x = np.linspace(0, 2*np.pi, 1000); y = np.sin(x); plt.plot(x, y)`. This is signal processing.
4. **Week 3** (3h): Plot a square wave using Fourier series (add sin harmonics). This directly connects to EEE 203 (Signals & Systems) content.
5. **Week 4** (3h): Read a CSV file with pandas, plot the data. This is the bread-and-butter of EE lab data analysis.
6. **Project**: Write a Python script that generates RC filter frequency response and plots it — compare against your LTspice simulation. Push to GitHub.

**Milestones**:
- [ ] Python + VS Code installed; first "hello world" script runs
- [ ] Wrote a function, a loop, and a list comprehension
- [ ] Plotted a sine wave with matplotlib
- [ ] Plotted a Fourier series approximation of a square wave
- [ ] Read a CSV and plotted data
- [ ] Pushed a Python script to GitHub

**Time investment**: ~3–5h/week for 4–6 weeks to get foundational fluency.

---

## Action Plan 4 — Breadboard + Multimeter (Lab Hands)

**Why**: Physical circuit intuition separates lab-fluent engineers from textbook-only students. The multimeter is the most used instrument in every EE job.

**Shopping list** (~$50 total):
- Breadboard starter kit (~$20): AmazonBasics or Elegoo kit (includes breadboard, jumpers, resistors, LEDs, capacitors)
- Digital multimeter (~$15–20): AstroAI DM6000AR or Klein MM300 — reliable, accurate, cheap
- Optional: 9V battery + battery snap connectors

**Steps (in order)**:
1. **Circuit 1 — LED + Resistor** (30 min): Connect a 9V battery → 330Ω resistor → LED → ground. Measure voltage across each component with multimeter. Verify Kirchhoff's Voltage Law (voltages sum to 9V). **Take a photo.**
2. **Circuit 2 — Voltage Divider** (45 min): Use two resistors to divide 9V into ~4.5V. Measure output. Calculate expected vs. measured. Understand why load matters. **Photo + notes.**
3. **Circuit 3 — RC Charging Curve** (1h): Connect a resistor + capacitor in series from 9V. Use multimeter to measure voltage across capacitor at 5-second intervals. Sketch the charging curve. Compare to the math formula V(t) = V·(1 - e^(-t/RC)). **This is EEE 202.**
4. **Circuit 4 — Transistor Switch** (1h): Use a 2N2222 NPN transistor to switch an LED on/off with a low-current base signal. This is digital logic at the hardware level.
5. **Circuit 5 — Basic Amplifier** (1h): Use an LM741 op-amp (or LM358 in a non-inverting config) to amplify a signal. Verify gain with multimeter. **This previews EEE 334.**

**Multimeter skills checklist**:
- [ ] Measure DC voltage (V DC)
- [ ] Measure AC voltage (V AC)
- [ ] Measure resistance
- [ ] Measure current (use correct port — destroys meters if wrong)
- [ ] Continuity test (beep = connected)
- [ ] Diode test

**Milestones**:
- [ ] 5 circuits built, photographed, and logged
- [ ] Verified KVL and KCL experimentally
- [ ] Measured a charging capacitor and matched the math
- [ ] Comfortable switching between multimeter modes without looking at the manual

**Time investment**: ~2–3h/week for 4 weeks.

---

## Action Plan 5 — Git + GitHub Portfolio

**Why**: Version control is expected at every EE internship in 2025–2026. A public GitHub with even simple projects signals initiative and technical literacy far above the baseline freshman applicant.

**Steps (in order)**:
1. **Day 1** (30 min): Create a GitHub account at github.com. Apply for **GitHub Student Developer Pack** (free pro features — just need a .edu email from ASU).
2. **Day 2** (1h): Install Git from git-scm.com. Configure your name and email: `git config --global user.name "Joe"` and `git config --global user.email "your@asu.edu"`.
3. **Day 3** (1h): Watch "Git and GitHub for Beginners" by Traversy Media (YouTube, 1h). Understand: repository, commit, push, pull, branch, merge.
4. **Week 1**: Create your first repo: "ee-freshman-projects". Add a README.md describing what it will contain. Push it.
5. **Week 2+**: Every project (Python script, LTspice screenshots, breadboard build) gets a folder in this repo with a README.
6. **README template per project**:
   - What it is (1 sentence)
   - What tools/components used
   - What I learned
   - Photo (drag into GitHub)
   - Simulation screenshot if applicable
7. **Profile README**: Create a special repo named `[your-username]/[your-username]` — this shows on your GitHub profile. Write 3–4 sentences about who you are and what you're building.

**Milestones**:
- [ ] GitHub account created + Student Pack claimed
- [ ] Git installed and configured
- [ ] First repo pushed
- [ ] 3 project folders with READMEs and photos
- [ ] Profile README written and live

**Time investment**: ~2h upfront, then 30 min per project to document.

---

## Action Plan 6 — Arduino (Embedded Systems Bridge)

**Why**: Arduino bridges circuit theory and real embedded systems. It teaches GPIO, PWM, serial communication, and C/C++ syntax before CSE 100 formally introduces programming. Projects are portfolio-ready immediately.

**Shopping list** (~$30–40):
- Arduino Uno R3 starter kit (~$25–35 on Amazon — Elegoo kit includes sensors, LEDs, servo, LCD, breadboard)
- USB cable (usually included)

**Steps (in order)**:
1. **Setup** (30 min): Install Arduino IDE (free, arduino.cc). Plug in Arduino. Load "Blink" example sketch. Upload it. See LED blink. You've written and deployed embedded firmware.
2. **Project 1 — LED Blink + PWM** (1h): Blink an LED. Then use `analogWrite()` to fade it with PWM. Understand the difference between digital and analog output. **Photo + GitHub.**
3. **Project 2 — Pushbutton + Conditional Logic** (1h): Wire a pushbutton. Turn LED on when pressed, off when released. Add debounce delay. This is digital input handling.
4. **Project 3 — Potentiometer + Serial Monitor** (1h): Read a potentiometer (analog input, 0–1023). Print the value to Serial Monitor. Map it to an LED brightness. This is ADC — appears in EEE 202 and every real system.
5. **Project 4 — Temperature Sensor** (1.5h): Wire a DHT11 or TMP36. Read temperature. Display on Serial Monitor. Write a conditional: "if temp > 30°C, blink LED fast." This is a complete sensing system.
6. **Project 5 — Servo Motor** (1h): Control a servo with a potentiometer. Map 0–1023 ADC reading to 0–180° servo angle. This is motor control — the entry point to power electronics.
7. Push all 5 projects to GitHub with photos and README explanations.

**Milestones**:
- [ ] Arduino IDE installed; Blink example runs
- [ ] LED fading with PWM works
- [ ] Pushbutton input with debounce
- [ ] ADC value printed to Serial Monitor
- [ ] Temperature sensor reading live
- [ ] Servo controlled by potentiometer
- [ ] All 5 on GitHub with photos

**Time investment**: ~2–3h/week for 5–6 weeks.

---

## Combined Timeline (Year 1 — 6 Months)

| Month | Focus | Hours/week |
|-------|-------|-----------|
| Month 1 | LTspice basics + Python install + Git setup + Breadboard Kit arrival | 5h |
| Month 2 | LTspice RC/RL/RLC sweeps + Python plotting + First 3 breadboard circuits | 6h |
| Month 3 | Arduino Projects 1–3 + Python CSV/pandas + GitHub 3 repos live | 6h |
| Month 4 | Arduino Projects 4–5 + Python Fourier series project + Profile README polished | 5h |
| Month 5 | Preview MAT 275 (3B1B Diff Eq playlist) + LTspice op-amp circuits + MATLAB Onramp (2h free course) | 5h |
| Month 6 | Review and document everything; apply to summer research or freshman internship programs | 3h |

**By end of Year 1 you will have:**
- Functional LTspice simulation skills (ready for EEE 202)
- Python basics + signal plotting (ready for EEE 203 support)
- 5+ Arduino projects on GitHub
- 5 breadboard circuits photographed and documented
- A public GitHub portfolio with README-documented projects
- Git workflow fluency
- Calc I–III genuinely mastered (not just graded)

---

## Related
- [[Research - First-Year ASU EE Skills]]
- [[ASU EE Year 1-2 Curriculum Map]]
- [[EE Freshman Self-Study Stack]]
- [[EE Freshman Portfolio Strategy]]
- [[EE Physical Side — Actionable Skill Plan]]
