---
type: concept
title: "Model Context Protocol"
status: developing
created: 2026-05-21
updated: 2026-05-21
tags:
  - concept
  - AI
  - agents
  - MCP
  - anthropic
---
# Model Context Protocol (MCP)

**Definition:** An open standard developed by Anthropic for connecting AI agents to external tools, data sources, and services. MCP defines a structured protocol for how an LLM can call external functions, read files, query databases, and interact with APIs in a reliable, composable way.

Described in the "Zero to AI Engineer" roadmap as the **2026 standard for agent tool-use**.

## Why MCP Matters

Before MCP, every AI agent implementation invented its own tool-calling scheme. MCP standardizes the interface so:
- Tools can be built once and reused across agents
- Agents know exactly how to discover and invoke external capabilities
- Safety constraints can be applied consistently at the protocol level

## Architecture Pattern (2026)

The recommended pattern combines two technologies:

| Layer | Technology | Role |
|---|---|---|
| **Orchestration** | LangGraph | Manages stateful, multi-step agent workflows; decides when to call which tools |
| **Tool connections** | MCP | Defines how the agent connects to file systems, APIs, databases; the actual connection protocol |

LangGraph handles *what the agent does*; MCP handles *how tools are exposed to the agent*.

## Anthropic Academy MCP Courses

Two free courses on Anthropic Academy (anthropic.skilljar.com):
1. "Introduction to Model Context Protocol" — build MCP servers and clients from scratch
2. "MCP: Advanced Topics" — production patterns, security, complex tool graphs

## Practical Example

An agent that reads an Obsidian vault, checks the web for updates, and sends a daily Telegram summary would use:
- **MCP server** for file system access (reads `.md` files in vault)
- **MCP server** for web search (fetches URLs, search results)
- **MCP server** for Telegram (sends messages)
- **LangGraph** to orchestrate the decision loop (when to read, when to search, when to send)

## Related
- [[Free AI Engineer Resources 2026]] — MCP courses are in the S-tier resource list
- [[AI-Assisted Programming Learning Roadmap]] — agent building is the advanced phase
- [[Andrej Karpathy]] — his tool-use philosophy: understand what's under the hood before adding frameworks
