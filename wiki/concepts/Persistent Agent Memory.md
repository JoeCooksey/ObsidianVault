---
type: concept
title: "Persistent Agent Memory"
created: 2026-06-02
updated: 2026-06-02
tags:
  - concept
  - ai
  - agents
  - memory
status: developing
related:
  - "[[Hermes Agent]]"
  - "[[Self-Improving Agent Loop]]"
---

# Persistent Agent Memory

**Persistent agent memory** is the cross-session recall layer that lets an agent remember everything it has done for you. In [[Hermes Agent]] it is the second half of the compounding-value thesis (the first being the [[Self-Improving Agent Loop]]).

## How Hermes implements it

- **Session store** — a SQLite database indexed by **FTS5 full-text search** holds *every session ever run*. Start a new chat and say "fix the bug we were chasing Friday," and the agent greps Friday's transcript, pulls the relevant turns into context, and continues. (Source: [[Hermes Agent vs Claude Code vs OpenClaw]])
- **Durable facts** — `MEMORY.md` and `USER.md` hold long-lived facts about the project and the user.
- **Procedural memory** — saved **skills** (see [[Self-Improving Agent Loop]]).
- **LLM summarization** — sessions are summarized for efficient recall rather than re-ingesting raw transcripts.
- **User modeling** — integrates **Honcho** for "dialectic user modeling," building a deepening model of who you are across sessions. (Source: [[Hermes Agent — Official Site and GitHub]])

## Resilience

The scheduler and state persist across gateway restarts via the SQLite state DB. A pipeline interrupted mid-run **resumes from the last completed checkpoint** rather than restarting. (Source: [[Awesome Hermes Use Cases]])

## Community memory architectures

The ecosystem layers richer memory on top:
- **3-layer memory**: L1 Hindsight → L2 Graphiti → L3 MemPalace.
- **Custom 22k-line memory kernel** parsing everything into a *temporal context graph* in SQLite with decay, promotion, and supersession lifecycle.
- **Obsidian vault as memory backbone** — the agent writes structured markdown notes into a synced vault (directly analogous to this wiki).

(Source: [[Awesome Hermes Use Cases]])

> [!gap] Memory designs vary widely across deployments; the base product ships FTS5 + markdown files, and the graph/temporal systems above are user-built add-ons.
