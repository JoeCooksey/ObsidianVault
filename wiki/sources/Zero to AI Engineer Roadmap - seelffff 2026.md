---
type: source
title: "Zero to AI Engineer Roadmap — seelffff (2026)"
status: complete
created: 2026-05-21
updated: 2026-05-21
tags:
  - source
  - article
  - AI
  - machine-learning
  - roadmap
  - career
---
# Zero to AI Engineer — The Roadmap

**Source:** Article by @seelffff (social media, 2026)
**Format:** Step-by-step 14-week free roadmap
**Thesis:** The companies that build AI (Anthropic, OpenAI, Google) are giving their training away for free. Combined with high-star GitHub repos, you can go from zero to deployable AI systems at $0.

---

## Core Argument

The author cancelled $300/month in Coursera/DataCamp/Udemy subscriptions after discovering that:
1. Anthropic Academy, OpenAI Academy, and Google AI offer free courses with real certificates
2. GitHub repos like microsoft/generative-ai-for-beginners (95K★) teach better than paid courses
3. Certificate collecting ≠ building ability — the only measure that matters

---

## 7-Step, 14-Week Structure

### Step 1 — Environment Setup (Day 1)
**Install:** Python 3.11+, VS Code, Git/GitHub, Obsidian (AI-Learning vault), Ollama
**Create accounts:** Anthropic Academy, OpenAI Academy, Google AI / Coursera (audit mode)
**Checkpoint:** Tools installed, accounts live, vault structured

### Step 2 — AI Fundamentals (Weeks 1–2)
- **Week 1:** Google AI Professional Certificate (Modules 1–3) → then Anthropic Academy: "AI Fluency: Framework & Foundations" (4D Framework, 2–3 hrs, certificate looks good on LinkedIn)
- **Week 2:** microsoft/generative-ai-for-beginners, Lessons 1–6 (95K★)
- **Note-taking template:** What I learned / What surprised me / Still unclear / Key terms
- **Checkpoint:** Can explain LLMs, tokens, transformers in own words; 4–6 Obsidian notes

### Step 3 — ML Foundations (Weeks 3–5)
- **Primary:** microsoft/ML-For-Beginners (44.9K★) — 12 weeks compressed to 3; 2 lessons/day
- **Parallel:** IBM Machine Learning on Coursera (audit free) — two angles = better retention
- **Math reference:** mlabonne/llm-course Foundations section (linear algebra, calculus, probability — ML-relevant only)
- **Project:** Train a classification model from scratch on a real dataset; push to GitHub
- **Checkpoint:** Understands regression, classification, clustering, gradient descent, loss functions, overfitting

### Step 4 — Deep Learning (Weeks 6–8)
- **Primary:** karpathy/nn-zero-to-hero — build micrograd → makemore → nanoGPT from scratch (pure Python, no frameworks)
  - Week 6: Lectures 1–3 (micrograd + makemore); code every line
  - Week 7: Lectures 4–5 (activations, BatchNorm, backprop)
  - Week 8: Lectures 6–7 (GPT from scratch + tokenization)
- **Experiment:** Run `ollama run llama3.2:3b` alongside nanoGPT — compare 3B vs. 10M params live
- **Supplement:** microsoft/AI-For-Beginners Weeks 7–12 (CNNs, RNNs)
- **Bridge:** Anthropic Academy — "Building with the Claude API" (auth, system prompts, tool use, streaming)
- **Checkpoint:** Built neural net from scratch; understand backprop/attention/transformers; can run local models; knows Claude API

### Step 5 — LLMs & Prompt Engineering (Weeks 9–10)
- **Deep dive:** mlabonne/llm-course LLM Scientist Track (40K★) — architecture → fine-tuning (LoRA, QLoRA) → quantization → evaluation
- **Prompt engineering:** OpenAI Academy ("Intro to Prompt Engineering") + Anthropic docs.anthropic.com (author calls it "arguably the best-written prompt engineering guide on the internet")
- **Continuation:** Finish microsoft/generative-ai-for-beginners Lessons 7–21 (RAG, function calling, design patterns, fine-tuning)
- **Project:** Build a RAG over your own Obsidian notes using ChromaDB or LanceDB (both free, local) — "a second brain over your second brain"

### Step 6 — AI Agents (Weeks 11–12)
- **Primary:** microsoft/ai-agents-for-beginners — 12 lessons: tool use, memory, multi-agent systems, orchestration
- **Deep dive:** Anthropic Academy — "Introduction to MCP" + "MCP: Advanced Topics" — MCP (Model Context Protocol) is described as the **2026 standard** for agent tool-use; teaches building MCP servers and clients from scratch
- **Framework:** LangGraph (by LangChain) — most popular framework for stateful, multi-step agent workflows; complements MCP (LangGraph for orchestration, MCP for tool connections)
- **Reference:** Anthropic Cookbook (docs.anthropic.com) — best real-world tool use + MCP patterns
- **Project:** Build an MCP + Claude agent that reads Obsidian vault, checks web updates on study topics, generates daily Telegram summary
- **Checkpoint:** Working AI agent with MCP; understands tool use, memory, multi-step workflows

### Step 7 — Production, Portfolio & Responsible AI (Weeks 13–14)
**Deploy (all free):**
- Gradio + Hugging Face Spaces — fastest ML demo hosting
- Streamlit Community Cloud — data-focused apps
- Vercel — web-based AI tools

**Evaluate:**
- DeepEval — open-source LLM evaluation
- RAGAS — RAG pipeline evaluation
- LLM-as-Judge — Claude evaluating Claude outputs

**Responsible AI:**
- Constitutional AI (Anthropic's alignment approach)
- Prompt injection defense
- Red-teaming your own systems

**Portfolio:**
- GitHub profile README + project READMEs with architecture diagrams + live demo links
- 2–3 LinkedIn case studies (problem → what you built → what you learned)
- Career tracks: Junior AI Engineer ($80–120K) → Prompt/Agent Engineer ($120–180K) → AI Product Engineer ($150–250K)

**Capstone:** Production-grade AI agent solving a real problem — deployed, evaluated, safety-checked

---

## Maintenance Mode (1 hr/week post-roadmap)
- Monday: Anthropic/OpenAI/Google release notes (10 min)
- Wednesday: arxiv-sanity-lite — 1 abstract (15 min)
- Friday: Yannic Kilcher or 1littlecoder video on a new paper/tool (20 min)
- Monthly: Build one small project with a new tool; push to GitHub

---

## Complete Free Resource List

### Free Courses (with certificates)
| Platform | Resource | Notes |
|---|---|---|
| Anthropic Academy | anthropic.skilljar.com | 16 courses, free certs — author calls it "most underrated AI learning platform in 2026" |
| OpenAI Academy | academy.openai.com | Workshops, tutorials, AI Foundations |
| Google AI | grow.google/ai | AI Professional Certificate — 7 modules |
| Coursera (audit) | coursera.org | IBM ML Certificate; Google courses; audit = free access, no cert |
| NVIDIA DLI | developer.nvidia.com/training | GPU + deep learning |
| DeepLearning.AI | deeplearning.ai | Andrew Ng short courses; "Agentic AI" and "LangChain for LLM Apps" recommended |

### GitHub Repositories (Stars as of 2026)
| Repo | Stars | Content |
|---|---|---|
| microsoft/generative-ai-for-beginners | 95K★ | 21 lessons GenAI |
| microsoft/ML-For-Beginners | 44.9K★ | 12 weeks classic ML |
| microsoft/AI-For-Beginners | 35K★ | 24 lessons deep learning + CV |
| karpathy/nn-zero-to-hero | — | Neural nets from scratch |
| mlabonne/llm-course | 40K★ | Complete LLM roadmap + Colab |
| microsoft/ai-agents-for-beginners | — | 12 lessons AI agents |
| ashishpatel26/500-AI-ML-DL-Projects | — | 500+ project ideas |

### Free Tools
| Tool | Use |
|---|---|
| Ollama + Open WebUI | Run models locally; self-hosted ChatGPT alternative |
| ChromaDB / LanceDB | Free local vector databases for RAG |
| DeepEval | Open-source LLM evaluation framework |
| RAGAS | RAG pipeline evaluation |
| Gradio + HF Spaces | Fastest ML demo deployment |

### YouTube Channels
- Andrej Karpathy — Neural Networks: Zero to Hero
- 3Blue1Brown — neural networks + linear algebra visualized
- Yannic Kilcher — AI paper breakdowns
- 1littlecoder — latest AI tools and implementations (2026 focus)
- Matt Wolfe — AI news and tool reviews

---

## Author's 3-Step "Start Tonight" Action Plan
1. Install Obsidian, create AI-Learning vault (5 min)
2. Sign up for Anthropic Academy, start "AI Fluency," write first note (30 min)
3. Fork microsoft/generative-ai-for-beginners, open Lesson 1 (20 min)

---

## Key Insight
> "The people who will actually learn AI in 2026 aren't the ones who bookmark 50 articles. They're the ones who open a terminal and start."

Certificate collecting ≠ building ability. Companies pay for engineers who can debug models and ship systems — not for people with certificates from courses they don't remember.

## Related
- [[AI ML for Engineers Roadmap]] — existing roadmap (EE-specialized; theory-deep)
- [[Free AI Engineer Resources 2026]] — condensed resource reference from this article
- [[AI-Assisted Programming Learning Roadmap]] — programming-angle complement
- [[Programming Skills AI Cannot Replace]] — what still matters
- [[Andrej Karpathy]] — central resource in Steps 4 + 5
- [[Model Context Protocol]] — the 2026 agent standard highlighted
