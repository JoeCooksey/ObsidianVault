---
type: concept
title: "Zero Cost Computer Skills — Tier List"
status: developing
created: 2026-04-27
updated: 2026-04-27
tags:
  - skills
  - career
  - free
  - programming
  - productivity
  - tier-list
---

# Zero Cost Computer Skills — Tier List

Skills you can start building TODAY, in front of a computer, with zero money required. Ranked by long-term compounding value for a 19-year-old EE student.

---

## S-Tier — Start This Week

### 1. Touch Typing
**What it is**: Typing without looking at the keyboard, all fingers used, 70–100+ WPM.
**Why it's S-tier**: The one meta-skill that multiplies every other skill on this list. 8 hrs/day × 30–50% throughput gain = 3–4 extra productive hours per day over a career. Most people plateau at 30–40 WPM hunt-and-peck and never fix it. Takes 4–6 weeks at 15 min/day.
**Start today**: keybr.com — no account required, adaptive per-key training, tracks WPM automatically.
**Backup**: typing.com (structured beginner → advanced curriculum, free)

---

### 2. Python
**What it is**: The dominant language of AI, data science, scientific computing, and EE simulation/automation.
**Why it's S-tier**: Already in the EE career roadmap as Phase 0–5. Python + NumPy + SciPy + Matplotlib + python-control = free MATLAB equivalent. Every tool is `pip install`. No purchase ever required. Also the language of AI/ML ($155k–$200k AI engineer base salary).
**Start today**: automatetheboringstuff.com — full textbook online free, no account. Chapter 1 runs in 30 minutes.
**Backup**: freeCodeCamp.org Scientific Computing with Python (completely free, no subscription)
**Joe's next step**: Project 1 from the Python EE Project Ladder (Ohm's Law Calculator, pure Python, 30 minutes)

---

### 3. Git / GitHub
**What it is**: Version control system + the platform where engineering work lives publicly.
**Why it's S-tier**: Non-negotiable for any engineering internship in 2026. A polished GitHub profile with 3 real repos is worth more than a GPA line on an early-career resume. Hiring managers look at GitHub before the resume for junior candidates. Takes 1–2 days to get functional; hours to create first repo.
**Start today**: git-scm.com/book — the "Pro Git" book, entirely free online. Or: skills.github.com — interactive Git learning, browser-based, free with GitHub account (free).
**Joe's immediate action**: Create `ee-projects` repo, push Project 1 from the Python EE Project Ladder as first commit.

---

### 4. LTSpice
**What it is**: Professional-grade SPICE circuit simulator from Analog Devices. Used by EE teams at Tesla, TI, Wolfspeed, Infineon.
**Why it's S-tier**: The free EE tool with the highest direct career ROI. Already mapped to a 10-circuit build ladder in this wiki. First session (voltage divider + `.op` → RC filter + Bode plot `.ac`) takes under 1 hour. Being able to say "I simulated a closed-loop buck converter in LTSpice" at age 19 separates Joe from 95% of EE sophomores.
**Start today**: Download from analog.com/LTspice — free, no account required. First circuit in under 1 hour.
**Best free tutorial**: SparkFun's "Getting Started with LTSpice" (written, best beginner doc) + Afrotechmods YouTube (best video series)

---

## A-Tier — High Value, Start Within a Month

### 5. SQL
**What it is**: Language for querying databases. Used everywhere data is stored — test labs, automation pipelines, telemetry.
**Why it's A-tier**: EE labs use SQL databases for automated test result storage. Data analysis and reporting require SQL. It is a universal language across EE, software, and data science. Takes 10–15 hours to reach "useful in real projects."
**Start today**: mode.com/sql-tutorial (free, structured) + SQLite inside Python (built-in, no install needed beyond Python).
**Backup**: Khan Academy's SQL course (free, browser-based, no install)

---

### 6. Linux / WSL Command Line
**What it is**: The shell environment used in every EE lab, EV company, and national lab (including LLNL and Sandia).
**Why it's A-tier**: WSL2 is already on Windows 11 (run `wsl --install` in PowerShell, free). Linux CLI proficiency is expected at any engineering internship. Python, Git, and simulation tools all run natively in Linux. The gap between a student who knows the shell and one who doesn't is visible in 10 minutes of pairing.
**Start today**: MIT "The Missing Semester of Your CS Education" — missing.csail.mit.edu — 11 free lectures covering shell, editors, Git, debugging. Lecture 1 runs in 1 hour.

---

### 7. Verilog / Digital Logic (In-Browser)
**What it is**: Hardware description language used for FPGA programming. FPGA engineers average $175k/year.
**Why it's A-tier**: EDA Playground (edaplayground.com) runs Verilog simulation in a browser tab — no installation, free account. HDLBits (hdlbits.01xz.net) is a free Verilog problem set in-browser. This is the zero-cost on-ramp to the FPGA track, which is already identified as a secondary high-income career path. Digital Logic is also EEE 120 (first actual EE course at ASU, Term 3A) — starting now means arriving fluent.
**Start today**: hdlbits.01xz.net — first problem set runs in browser, no install, no account needed.

---

### 8. Prompt Engineering
**What it is**: Systematic techniques for getting high-quality output from AI tools (Claude, ChatGPT, Copilot).
**Why it's A-tier**: A skilled prompter extracts 5–10× more useful output than an unskilled one from the same tool. The gap is not in the AI — it's in the human using it. Core techniques: chain-of-thought reasoning, few-shot examples, role assignment, output specification, iterative refinement. Takes 2–5 days to internalize; immediately amplifies Python, LTSpice, Git, and every other skill on this list.
**Start today**: docs.anthropic.com/prompt-engineering (free). Claude.ai has a free tier to practice.

---

## B-Tier — Supporting, Start When S and A Are Running

### 9. Markdown
**What it is**: Lightweight markup language used for GitHub READMEs, documentation, wikis, and Obsidian notes.
**Why it's B-tier**: Every GitHub repo needs a README. Obsidian runs on Markdown. Takes < 1 day to learn. Free reference: markdownguide.org.

### 10. GNU Octave (Free MATLAB)
**What it is**: Open-source MATLAB clone with 90%+ syntax compatibility. Free. ASU uses MATLAB in EEE courses.
**Why it's B-tier**: Lets you learn MATLAB syntax for free before needing the school license. Also useful for Bode plots, signal processing, and control design before switching to Python.
**Start today**: octave.org (free download) or run online at octave-online.net (browser-based, no install).

### 11. LaTeX
**What it is**: Document markup language used for engineering papers, technical reports, resumes.
**Why it's B-tier**: Standard for MS thesis, IEEE papers, and professional engineering documentation. Overleaf (overleaf.com) has a free tier that runs entirely in-browser — no installation needed.
**Start today**: overleaf.com → "New Project" → "Example Project" → immediate LaTeX document in browser.

### 12. HTML / CSS Basics
**What it is**: Web markup and styling. Used to build a personal portfolio site.
**Why it's B-tier**: A personal portfolio page on GitHub Pages is free to host and useful for internship applications. freeCodeCamp.org teaches responsive web design completely free.

### 13. Google Sheets / Spreadsheet Mastery
**What it is**: Advanced spreadsheet skills — formulas, pivot tables, data visualization, financial modeling.
**Why it's B-tier**: Free with a Google account. Used for budgeting, Roth IRA tracking, project cost analysis, and lab data summary. ExcelJet (exceljet.net) has free function-by-function tutorials.

---

## C-Tier — Useful But Lower Career Priority

### 14. Regular Expressions (Regex)
Pattern matching language used across programming, text search, and data parsing. regex101.com and regexr.com are free interactive playgrounds. Takes 3–5 days to get functional.

### 15. Chess
Cognitive training at chess.com (free tier). S-tier by cognitive benefit research (Carnegie Mellon studies), but the career ROI is lower than the skills above. Best as a 15-min daily warmup alongside touch typing.

### 16. Music Theory
musictheory.net and teoria.com teach music theory entirely free in-browser. Complements guitar learning (JustinGuitar.com) but not a career-ROI skill.

---

## Joe's Start-Today Action Stack

1. **Right now**: Go to keybr.com → start touch typing lesson 1 (15 minutes, no account)
2. **Today**: Download LTSpice → do voltage divider `.op` simulation (1 hour, from LTSpice Complete Skills Guide)
3. **This week**: automatetheboringstuff.com Chapter 1 → write first Python script → push to GitHub repo
4. **This month**: MIT Missing Semester Lecture 1 (shell) → hdlbits.01xz.net first 5 Verilog problems → SQL tutorial chapter 1

**The compound play**: Touch typing → Python → Git → push EE projects → GitHub portfolio → LLNL/Sandia internship application Oct 2026.

---

## Key Insight
The bottleneck is not access to resources — it's starting. Every S-tier skill on this list is free and can be started in under 10 minutes. The skills that cost money (BJJ, guitar, textbooks) have value too, but they require logistics. These cost nothing and start today.

**See also**: [[Free Time Tier List]], [[Python EE Project Ladder]], [[LTSpice Complete Skills Guide]], [[High Income Skills Tier List]], [[EE Freshman Self-Study Stack]]
