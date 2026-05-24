---
type: concept
title: "Trending GitHub Repositories May 2026"
status: complete
created: 2026-05-24
updated: 2026-05-24
tags:
  - github
  - tools
  - ai-engineering
  - electrical-engineering
  - quant-finance
  - python
  - resources
---

# Trending GitHub Repositories — May 2026 (Curated for Joe)

Sourced from GitHub Trending, Trendshift, and targeted searches across Joe's interest areas: EE/power electronics, AI/ML engineering, quant finance, and Python education. Filtered and ranked by relevance to Joe's current projects and goals.

---

## S-Tier — Star and Use This Week

### `codecrafters-io/build-your-own-x` ⭐ 504K
**Language:** Markdown
**Why:** "Master programming by recreating your favorite technologies from scratch." The most-starred repository on all of GitHub. Guides for building your own compiler, CPU, neural net, shell, git, database, web server — dozens of projects. Aligns 1:1 with Joe's build-first philosophy (buck converter, Python EE Ladder, Karpathy series). Pick any guide and start.
**Joe action:** Use as the source for Python EE Ladder Projects 7–12.

### `karpathy/microgpt` ⭐ ~3K (new, climbing fast)
**Language:** Python
**Why:** Andrej Karpathy's newest educational project — 200 lines of pure Python, zero dependencies, trains and inferences a full GPT including tokenizer, autograd engine, transformer architecture, Adam optimizer, and training loop. The most compressed, most educational ML implementation ever written. Karpathy is already in Joe's stack; this is the pinnacle of the series.
**Joe action:** Work through this immediately after finishing nn-zero-to-hero.

### `rohitg00/ai-engineering-from-scratch` ⭐ 15K
**Language:** Python
**Why:** Structured curriculum for learning, building, and shipping AI solutions. Covers LLMs, agents, RAG, tool use, deployment. Directly complements Joe's AI engineer roadmap from the "Zero to AI Engineer" ingest. Free.
**Joe action:** Cross-reference with [[Free AI Engineer Resources 2026]] and [[Zero to AI Engineer Roadmap - seelffff 2026]].

### `PyPedia/Electrical-Engineering-with-Python`
**Language:** Python
**Why:** Circuit analysis, mathematical modeling, and simulation using NumPy, SciPy, and SymPy — exactly the Python EE project ladder Joe is building. This repo is a living reference for turning EE math (Ohm's Law → Bode plots → FFT → PID → Buck simulator) into clean Python code.
**Joe action:** Use as reference library for all 12 projects in the Python EE Ladder.

---

## A-Tier — High Value, Add to Workflow

### `Lum1104/Understand-Anything` ⭐ 25K
**Language:** TypeScript/Python
**Why:** Turns any code or knowledge base into an interactive knowledge graph you can explore and query. Extremely useful for Joe when studying complex research papers, new codebases, or the ASU curriculum. Run it on Karpathy's nanoGPT, a WBG paper, or a new STM32 HAL codebase.
**Joe action:** Try on `karpathy/nn-zero-to-hero` or an EEE 202 textbook chapter.

### `ollama/ollama` ⭐ 165K
**Language:** Go
**Why:** Run large language models entirely on your own hardware with a single command. Free, fast, no API key or internet needed. Works with LLaMA 3, Mistral, Gemma, DeepSeek. Joe can run a local AI assistant for studying, code review, and EE homework at zero cost.
**Joe action:** `curl -fsSL https://ollama.ai/install.sh | sh` → `ollama pull llama3`.

### `open-webui/open-webui` ⭐ 124K
**Language:** Python/Svelte
**Why:** Self-hosted ChatGPT-style UI that connects to Ollama (and OpenAI-compatible APIs). Gives Joe a fully local AI assistant with chat history, custom system prompts, and document uploads — zero cost, 100% private. Pairs with Ollama above.
**Joe action:** Install after Ollama is running; upload EE lecture PDFs for Q&A.

### `karpathy/autoresearch` ⭐ ~2K (Karpathy's experimental repo)
**Language:** Python
**Why:** An AI agent given a small LLM training setup that experiments autonomously overnight — modifying code, training for 5 minutes, checking if results improved. Directly relevant to Joe's AI/ML research interest and FURI aspirations. Shows the frontier of AI-assisted research.

### `wilsonfreitas/awesome-quant` ⭐ ~16K
**Language:** Markdown
**Why:** The definitive curated list of quant finance libraries, packages, and resources — organized by category (data, pricing, portfolio, risk, backtesting, etc.). The master reference for Joe's quant finance self-study track in [[Quantitative Finance Career Guide]].
**Joe action:** Mine for Python libraries that match Quant Programming Stack.

### `polakowo/vectorbt` ⭐ ~4K
**Language:** Python
**Why:** Vectorized backtesting library — test thousands of strategy variations simultaneously instead of looping. Extremely fast. Named in Joe's [[Quant Programming Stack]] as a key backtesting tool. Running VectorBT on pairs trading or momentum strategies is a portfolio project.
**Joe action:** Use for portfolio projects 5–8 in [[Quant Programming Stack]].

---

## B-Tier — Bookmark for Later

### `n8n-io/n8n` ⭐ 180K
**Language:** TypeScript
**Why:** Workflow automation with native AI agent nodes, 400+ integrations, and a visual builder. Could automate Joe's study routines, research digests, or Obsidian vault updates. The self-hosted, open-source alternative to Zapier with LLM logic baked in.
**Use when:** Building AI-powered tools or automating repetitive research tasks.

### `infiniflow/ragflow` ⭐ 70K
**Language:** Python
**Why:** Open-source RAG (retrieval-augmented generation) engine. If Joe ever builds an AI app that queries his Obsidian vault or technical papers, RAGFlow provides document ingestion, vector indexing, and query planning out of the box.
**Use when:** Building a searchable AI interface over Joe's vault.

### `mem0ai/mem0` ⭐ 52K
**Language:** Python
**Why:** Persistent memory layer for AI agents — they remember across conversations. The missing piece in most chatbot workflows. Relevant when Joe builds AI-powered study tools or personal assistants.

### `666ghj/MiroFish` ⭐ 62K
**Language:** Python
**Why:** Universal swarm intelligence engine for predictions. Multi-agent prediction architecture that could be relevant to quant finance (ensemble forecasting) and ML research. Worth watching.

### `shiyu-coder/Kronos` ⭐ 25K
**Language:** Python
**Why:** Foundation model trained on financial market language — understands market microstructure, trading signals, and financial text natively. Relevant to Joe's quant finance track, especially [[Machine Learning in Quantitative Finance]].

### `nhivp/Awesome-Embedded` ⭐ ~6K
**Language:** Markdown
**Why:** Comprehensive curated list for embedded systems: STM32 HAL libraries, RTOS options, debugging tools, signal processing on MCUs. Complements Joe's STM32 buck converter build project.
**Use when:** Moving from breadboard to production STM32 firmware.

### `Artoriuz/OSEE` — Open-source EE Curriculum
**Language:** Markdown
**Why:** A structured, free EE curriculum covering the foundational knowledge every EE should have. Useful as a gap-filler alongside ASU coursework.
**Use when:** Self-studying between semesters.

---

## Meta — Tools for Tracking GitHub Trends

| Tool | URL | Use |
|------|-----|-----|
| GitHub Trending | github.com/trending | Daily snapshot of fastest-growing repos |
| Trendshift | trendshift.io | Live momentum ranking by stars/velocity |
| Star History | star-history.com | Compare star growth curves over time |
| OSSInsight | ossinsight.io | Deep analytics on any repo |

---

## Related Pages
- [[Andrej Karpathy]] — source of microgpt, autoresearch, nn-zero-to-hero
- [[Zero to AI Engineer Roadmap - seelffff 2026]] — AI engineer curriculum
- [[Quant Programming Stack]] — Python quant tools list
- [[Buck Converter Build Guide]] — STM32 embedded project context
- [[Free AI Engineer Resources 2026]] — AI learning resources

---

*Researched via GitHub Trending, Trendshift, web searches — 2026-05-24. 8 searches run.*
