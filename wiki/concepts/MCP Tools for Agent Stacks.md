---
type: concept
title: "MCP Tools for Agent Stacks"
status: developing
created: 2026-05-25
updated: 2026-05-25
tags:
  - MCP
  - tools
  - agents
  - AI
---

# MCP Tools for Agent Stacks

**MCP (Model Context Protocol)** is the standard tool layer for AI agents in 2026. Every major agent harness (Claude Code, Cursor, VS Code Agent Mode, LangGraph, CrewAI) ships with MCP support. Tools are composable, version-controllable, and shared across agent teams via a committed `.mcp.json` config file.

## Core Tool Stack for Software Development Agent Teams

| Tool | MCP Server | Purpose | Required By |
|---|---|---|---|
| **Filesystem** | `@anthropic/mcp-filesystem` | Read/write all project files | All agents |
| **GitHub** | `@modelcontextprotocol/mcp-github` | Commits, PRs, branches, repo search | Engineer, Reviewer |
| **Code Execution** | `e2b-mcp` or `@anthropic/code-execution` | Run code in sandbox, get stdout/stderr | Engineer, QA |
| **Browser / UI** | `@microsoft/playwright-mcp` | Navigate, click, screenshot, assert UI | QA (frontend) |
| **Live Docs** | `context7` | Fetch current library docs on demand | Architect, Engineer |
| **Web Search** | `brave-search-mcp` | Research during planning phase | PM, Architect |

## Committed Team Config (`.mcp.json`)

Committing this file to the repo ensures every agent and every developer gets identical tool access:

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["-y", "@anthropic/mcp-filesystem", "/workspace"],
      "permissions": ["read", "write"]
    },
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/mcp-github"],
      "env": { "GITHUB_TOKEN": "${GITHUB_TOKEN}" }
    },
    "e2b": {
      "command": "npx",
      "args": ["-y", "e2b-mcp"],
      "env": { "E2B_API_KEY": "${E2B_API_KEY}" }
    },
    "playwright": {
      "command": "npx",
      "args": ["-y", "@microsoft/playwright-mcp"]
    },
    "context7": {
      "command": "npx",
      "args": ["-y", "context7-mcp"]
    }
  }
}
```

Secret values (`GITHUB_TOKEN`, `E2B_API_KEY`) are injected via environment variables — never hardcoded in the config.

## Tool Security Principle

Assign each agent **only the tools it needs**:
- PM agent → web search only (research only, no file writes to `/src/`)
- Architect → filesystem read + web search + context7
- Engineer → filesystem read/write + code execution
- QA → filesystem read + code execution + playwright
- Reviewer → filesystem read/write + GitHub MCP (for PR creation)

This is the principle of least privilege applied to agent tool access. Claude Code subagent YAML files let you specify exactly which tools each subagent can use.

## 2026 MCP Protocol Updates

- **A2A (Agent-to-Agent) protocol**: owned by Google, standardizes how agents collaborate (MCP owns tools, A2A owns collaboration)
- **Parallel MCP init**: Claude Code subagents now initialize all MCP connections simultaneously on startup (April 2026), cutting multi-agent startup time significantly
- **VS Code 1.115–1.116 (April 2026)**: MCP server bridging to external agents, Companion App for parallel sessions

## E2B vs Local Code Execution

| | E2B (Cloud Sandbox) | Local Code Execution |
|---|---|---|
| Safety | Fully isolated container | Runs on host machine |
| Cost | ~$0.10–0.50/hour | Free |
| Language support | Python, JS, Bash, anything | Same as host |
| Best for | Untrusted code, CI/CD | Dev machine, trusted agent |

For production agent pipelines, use E2B to prevent agents from accidentally damaging the host system.

## Related

- [[Multi-Agent Development Team]] — which agents need which tools
- [[Agent Orchestration Frameworks]] — how MCP integrates with CrewAI, LangGraph, Claude Code
- [[Research - Full Agent Stack Team Guide]] — full `.mcp.json` examples
