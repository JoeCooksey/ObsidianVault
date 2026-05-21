---
type: concept
title: "Free AI Engineer Resources 2026"
status: complete
created: 2026-05-21
updated: 2026-05-21
tags:
  - concept
  - AI
  - machine-learning
  - resources
  - free
  - career
---
# Free AI Engineer Resources 2026

The major AI companies (Anthropic, OpenAI, Google) are giving away structured training with certificates in 2026. Combined with high-starred GitHub repositories, the total cost of a quality AI engineering education is $0. This page is the actionable resource reference from the "Zero to AI Engineer" roadmap.

The key insight: certificate platforms (Coursera Plus, DataCamp, Udemy) charge for packaging. The actual intellectual content comes from the companies themselves — for free.

## Platform Priority Ranking

### S-Tier (Start Here)

**Anthropic Academy** — `anthropic.skilljar.com`
- 16 courses, all free with certificates
- Author calls it "the most underrated AI learning platform in 2026"
- Key courses: "AI Fluency: Framework & Foundations" (4D Framework, 2–3 hrs) → "Building with the Claude API" (auth, system prompts, tool use, streaming) → "Introduction to MCP" + "MCP: Advanced Topics"
- Certificates are from Anthropic — carries real weight in 2026

**karpathy/nn-zero-to-hero**
- Andrej Karpathy (former Tesla AI Director, OpenAI co-founder) teaching neural networks from zero, pure Python, no frameworks
- Build micrograd → makemore → nanoGPT in sequence
- The most respected free deep learning curriculum in existence
- Complements theory with hands-on code every step

**mlabonne/llm-course** (40K★)
- The most comprehensive free LLM curriculum
- Three sections: (1) Math foundations — linear algebra, calculus, probability relevant to ML only; (2) LLM Scientist Track — architecture, fine-tuning (LoRA/QLoRA), quantization, evaluation; (3) LLM Engineer Track — RAG, deployment, agents
- Colab notebooks for every topic

### A-Tier

**microsoft/generative-ai-for-beginners** (95K★)
- 21 lessons; fork and work through
- Weeks 1–2: Lessons 1–6 (GenAI intro, LLM mechanics, first chat app)
- Weeks 9–10: Lessons 7–21 (RAG, function calling, fine-tuning, design patterns) — click better after building understanding in Karpathy

**microsoft/ML-For-Beginners** (44.9K★)
- 12-week classical ML curriculum; compress to 3 weeks (2 lessons/day)
- Regression, classification, clustering, NLP basics
- Quizzes, notebooks, challenges — the complete package for classical ML

**microsoft/ai-agents-for-beginners**
- 12 lessons: tool use, memory, multi-agent systems, orchestration
- The structured on-ramp to agent architecture before going deep on MCP

**OpenAI Academy** — `academy.openai.com`
- Free workshops, tutorials, AI Foundations course
- "Intro to Prompt Engineering" from the ChatGPT team
- Free certificates from OpenAI

**Google AI Professional Certificate** — `grow.google/ai`
- 7 modules; free via Coursera audit
- Gentlest on-ramp — no code in first 3 modules; vocabulary-building before diving into code

### B-Tier

**IBM Machine Learning Certificate** (Coursera, audit free)
- Traditional video format; use alongside microsoft/ML-For-Beginners for two angles on same topics
- Audit mode = full video access, no Coursera cert (you'll have IBM or directly Google/Anthropic/OpenAI certs instead)

**microsoft/AI-For-Beginners** (35K★)
- Weeks 7–12 deep learning section: CNNs, RNNs; expands beyond Karpathy into computer vision

**DeepLearning.AI** — `deeplearning.ai`
- Andrew Ng short courses; "Agentic AI" and "LangChain for LLM Apps" are the most relevant

**NVIDIA DLI** — `developer.nvidia.com/training`
- GPU + deep learning; free tier

---

## Coursera Audit Mode (Key Hack)

When Coursera asks you to pay, look for the small "Audit this course" link at the bottom of the enrollment dialog. Full access to all videos and materials; no Coursera-branded certificate. Since you'll get certificates directly from Anthropic, OpenAI, and Google instead, the audit mode is strictly better for cost.

---

## Key GitHub Repositories (by Use Case)

| Use Case | Repository | Stars |
|---|---|---|
| GenAI intro + first projects | microsoft/generative-ai-for-beginners | 95K★ |
| Classical ML curriculum | microsoft/ML-For-Beginners | 44.9K★ |
| Deep learning + CV | microsoft/AI-For-Beginners | 35K★ |
| Neural nets from scratch | karpathy/nn-zero-to-hero | — |
| Complete LLM roadmap | mlabonne/llm-course | 40K★ |
| Agent architecture | microsoft/ai-agents-for-beginners | — |
| 500+ project ideas | ashishpatel26/500-AI-ML-DL-Projects | — |

---

## Free Tools Stack

| Tool | Category | Use |
|---|---|---|
| **Ollama** | Local inference | Run LLMs locally (llama3.2:3b is the comparison baseline) |
| **Open WebUI** | Local interface | Self-hosted ChatGPT alternative on top of Ollama |
| **ChromaDB** | Vector database | Free, local RAG storage |
| **LanceDB** | Vector database | Free, local alternative to ChromaDB |
| **DeepEval** | Evaluation | Open-source LLM evaluation framework |
| **RAGAS** | Evaluation | Specifically for RAG pipeline quality |
| **Gradio + HF Spaces** | Deployment | Fastest ML demo hosting (free) |
| **Streamlit Community** | Deployment | Data-focused apps (free tier) |
| **Vercel** | Deployment | Web-based AI tools (free tier) |

---

## Free Reference Documentation

- **Anthropic Prompt Engineering Guide** — `docs.anthropic.com` — author calls it "arguably the best-written prompt engineering guide on the internet"; not a course, a deeply detailed reference
- **Anthropic Cookbook** — `docs.anthropic.com/en/docs/about-claude/use-case-guides` — best real-world tool use + MCP pattern examples; study like case studies

---

## Model Context Protocol (MCP) — Why It Matters in 2026

MCP is Anthropic's open standard for connecting AI agents to external tools. The article describes it as the **2026 standard for agent tool-use**. Anthropic Academy's two MCP courses teach building MCP servers and clients from scratch.

Architecture pattern: **LangGraph for orchestration + MCP for tool connections** — LangGraph manages stateful multi-step workflows; MCP defines how the agent connects to file systems, APIs, databases.

See [[Model Context Protocol]] for the full concept.

---

## Career Salary Benchmarks (2026)

| Level | Salary Range | Key Skills |
|---|---|---|
| Junior AI Engineer | $80–120K | API integration, prompt engineering, basic fine-tuning |
| Prompt/Agent Engineer | $120–180K | Agent architecture, MCP, RAG, evaluation |
| AI Product Engineer | $150–250K | Production deployment, evaluation systems, safety |

WEF 2025 data: AI-literate workers command 15–22% salary premiums over equivalent non-AI-literate workers.

---

## Maintenance Mode (Post-Roadmap, 1 hr/week)

| Day | Activity | Time |
|---|---|---|
| Monday | Anthropic/OpenAI/Google release notes | 10 min |
| Wednesday | arxiv-sanity-lite — 1 abstract | 15 min |
| Friday | Yannic Kilcher or 1littlecoder video | 20 min |
| Monthly | Build one small project with a new tool; push to GitHub | — |

---

## Joe-Specific Integration

How this roadmap maps to existing Joe vault resources:

| Roadmap Step | Existing Joe Resource | Integration |
|---|---|---|
| Step 3 ML Foundations | [[AI ML for Engineers Roadmap]] Phase 1 | mlabonne/llm-course math section replaces "find your own math reference" |
| Step 4 Deep Learning | [[AI ML for Engineers Roadmap]] Phase 2 | Karpathy is already there; MCP Anthropic courses are new additions |
| Step 5 LLMs | [[AI-Assisted Programming Learning Roadmap]] | Prompt engineering layer adds to existing programming roadmap |
| Step 6 Agents | No existing page | New territory — MCP + LangGraph |
| Step 7 Portfolio | [[EE Freshman Portfolio Strategy]] | Extends GitHub portfolio strategy to AI projects |

**Recommended Joe action (tonight):**
1. Sign up for Anthropic Academy (free)
2. Complete "AI Fluency: Framework & Foundations" (2–3 hrs, certificate) — aligns directly with MAT 343 eigenvalue / EEE 202 poles connection
3. Fork microsoft/generative-ai-for-beginners and open Lesson 1 alongside the [[Python EE Project Ladder]]

## Related
- [[AI ML for Engineers Roadmap]] — EE-specialized roadmap (theory-deep, power electronics integration)
- [[Zero to AI Engineer Roadmap - seelffff 2026]] — source article
- [[AI-Assisted Programming Learning Roadmap]] — programming-angle complement
- [[Andrej Karpathy]] — the central resource in Steps 4–5
- [[Model Context Protocol]] — the 2026 agent standard
- [[Programming Skills AI Cannot Replace]] — what to build on top of these free resources
