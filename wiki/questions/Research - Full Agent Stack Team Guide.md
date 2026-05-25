---
type: research
title: "Research — Full Agent Stack Team: Prompt to Project"
status: complete
created: 2026-05-25
updated: 2026-05-25
tags:
  - AI
  - agents
  - multi-agent
  - software-development
  - orchestration
  - CrewAI
  - LangGraph
  - MetaGPT
---

# Research — Full Agent Stack Team: Prompt to Project

> **Goal:** Build a team of AI agents that accepts any prompt and delivers a full project — requirements, architecture, code, tests, and review — with minimal human intervention.

## 8 Key Findings

1. **Five core agent roles mirror a real software company.** MetaGPT proved in research that assigning Product Manager → Architect → Project Manager → Engineer → QA Engineer to separate LLM agents, each with an isolated context, produces dramatically more reliable output than a single agent trying to do everything. The assembly-line pattern reduces error compounding.

2. **Three orchestration patterns fit different complexity levels.** Sequential pipeline (fixed handoffs) works for well-scoped projects. Supervisor pattern (one orchestrator agent delegates to workers) works for dynamic task allocation. Role-based crew (agents self-organize with roles + goals) works for open-ended creative work. Choose based on how deterministic your workflow needs to be.

3. **CrewAI, LangGraph, and Claude Code Agent Teams are the three production-ready choices in 2026.** AutoGen reached GA then pivoted to maintenance mode (new projects should use Microsoft Agent Framework). MetaGPT is the reference architecture but less suitable for custom pipelines.

4. **MCP (Model Context Protocol) is the standard tool layer.** Every major agent harness ships with MCP in 2026. Core tools the stack needs: Filesystem MCP (read/write), GitHub MCP (commits, PRs), Playwright MCP (browser/UI testing), E2B MCP (sandboxed code execution), Context7 (live documentation). These are composable and version-controllable per project.

5. **Shared state and explicit handoffs prevent agent coordination failure.** Multi-agent systems don't break at logic — they break at integration. Each agent should write its output to an external artifact (file or structured object), not just pass text in a conversation. This creates audit trails and enables resumable workflows.

6. **Human-in-the-loop at three checkpoints is the production pattern.** Gate 1: PRD approval before architecture begins. Gate 2: architecture approval before coding begins. Gate 3: final code review before merge/deploy. Everything between gates runs autonomously. This balance prevents hallucinated scope and irreversible mistakes.

7. **Claude Code Agent Teams is the highest-leverage option if already in the Claude ecosystem.** As of February 2026 (Opus 4.6), Claude Code supports 2–16 agents on a shared codebase. Subagents have isolated context windows, model-pinned configurations, and initialize in parallel (April 2026 update). The orchestrator sequences dependent work and passes context between workers natively.

8. **The stack is fully buildable with free/low-cost tools.** CrewAI is open source. LangGraph is open source. Claude API is pay-per-token with the free tier. E2B has a free tier. GitHub MCP is free. A complete "prompt-to-project" pipeline can run for under $5 per mid-sized project with Claude Haiku or Sonnet 4.6 for worker agents and Opus 4.7 only for the orchestrator.

---

## The Standard 5-Role Agent Team

```
[User Prompt]
     │
     ▼
┌─────────────────┐
│  Product Manager │  → Generates PRD (user stories, acceptance criteria, scope)
│  (Requirements)  │
└────────┬────────┘
         │ ← [Human Gate 1: PRD approval]
         ▼
┌─────────────────┐
│   Architect     │  → Tech spec, system design, API contracts, file structure
└────────┬────────┘
         │ ← [Human Gate 2: Architecture approval]
         ▼
┌─────────────────┐
│ Project Manager │  → Task breakdown, sequencing, agent assignments
│   (optional)    │
└────────┬────────┘
         ▼
┌─────────────────┐
│  Engineer(s)    │  → Implements code, one agent per module/service
└────────┬────────┘
         ▼
┌─────────────────┐
│   QA / Tester   │  → Writes + runs tests, debugs, verifies acceptance criteria
└────────┬────────┘
         ▼
┌─────────────────┐
│    Reviewer     │  → Final code review, refactor, docstrings, PR creation
└────────┬────────┘
         │ ← [Human Gate 3: Final review]
         ▼
  [Merged / Deployed Project]
```

---

## Framework Selection Guide

| Framework | Best For | Orchestration Model | State Management | Learning Curve |
|---|---|---|---|---|
| **CrewAI** | Fast prototyping, role-based teams | Role + Task (hierarchical or sequential) | Shared crew context | Low |
| **LangGraph** | Production, complex dependencies | Directed graph (state machine) | Checkpointed graph state | Medium-High |
| **Claude Code Agent Teams** | Claude-native development | Orchestrator + subagents | Shared codebase + handoffs | Low (if using Claude) |
| **MetaGPT** | Software company simulation | Sequential assembly line | Structured artifacts (PRD, spec, code) | Medium |
| **AutoGen** (legacy) | Iterative code generation | Conversation / group chat | Docker sandbox | Medium (maintenance mode) |

---

## CrewAI Implementation Pattern

```python
from crewai import Agent, Task, Crew, Process

# Define agents with roles, goals, backstories
product_manager = Agent(
    role="Product Manager",
    goal="Translate user prompt into a precise PRD with user stories and acceptance criteria",
    backstory="10-year PM who writes crisp requirements, never over-scopes",
    tools=[FileWriteTool()],
    llm="claude-opus-4-7"  # Use powerful model for requirements
)

architect = Agent(
    role="Software Architect",
    goal="Design system architecture from the PRD: components, APIs, data models",
    backstory="Principal engineer who prioritizes simplicity and maintainability",
    tools=[FileReadTool(), FileWriteTool()],
    llm="claude-opus-4-7"
)

engineer = Agent(
    role="Senior Software Engineer",
    goal="Implement clean, tested code following the architecture spec",
    backstory="Full-stack engineer who writes production-quality code with no TODOs",
    tools=[FileReadTool(), FileWriteTool(), CodeInterpreterTool()],
    llm="claude-sonnet-4-6"  # Cheaper model for implementation
)

qa_engineer = Agent(
    role="QA Engineer",
    goal="Write and execute tests, verify all acceptance criteria are met",
    backstory="Test engineer obsessed with edge cases and coverage",
    tools=[FileReadTool(), FileWriteTool(), CodeInterpreterTool()],
    llm="claude-sonnet-4-6"
)

reviewer = Agent(
    role="Code Reviewer",
    goal="Review all code for quality, security, performance, and correctness",
    backstory="Staff engineer who focuses on maintainability and catches subtle bugs",
    tools=[FileReadTool(), FileWriteTool()],
    llm="claude-opus-4-7"
)

# Define tasks with sequential dependency
prd_task = Task(
    description="Read the user prompt and produce a PRD with user stories, acceptance criteria, and scope",
    expected_output="A structured PRD document saved to /artifacts/prd.md",
    agent=product_manager
)

architecture_task = Task(
    description="Read the PRD and design the system architecture",
    expected_output="An architecture spec saved to /artifacts/architecture.md including component diagram, API contracts, data models",
    agent=architect,
    context=[prd_task]
)

implementation_task = Task(
    description="Implement all components per the architecture spec",
    expected_output="Complete working code in /src/ with no placeholders",
    agent=engineer,
    context=[prd_task, architecture_task]
)

testing_task = Task(
    description="Write and run tests for all components, verify acceptance criteria",
    expected_output="Test files in /tests/, all passing, coverage report",
    agent=qa_engineer,
    context=[prd_task, implementation_task]
)

review_task = Task(
    description="Review all code for quality, correctness, security, and readability",
    expected_output="Review report in /artifacts/review.md and any inline fixes applied",
    agent=reviewer,
    context=[implementation_task, testing_task]
)

# Assemble crew
crew = Crew(
    agents=[product_manager, architect, engineer, qa_engineer, reviewer],
    tasks=[prd_task, architecture_task, implementation_task, testing_task, review_task],
    process=Process.sequential,
    verbose=True
)

result = crew.kickoff(inputs={"prompt": "Build a CLI tool that monitors CPU and memory usage and alerts when thresholds are exceeded"})
```

---

## LangGraph Implementation Pattern

LangGraph models the team as a directed graph where the supervisor node routes work between specialist agents.

```python
from langgraph.graph import StateGraph, END
from typing import TypedDict, Annotated

# Shared state flows through every node
class ProjectState(TypedDict):
    user_prompt: str
    prd: str
    architecture: str
    code: dict[str, str]      # filename → content
    test_results: str
    review_notes: str
    status: str

# Each node is an agent function
def product_manager_node(state: ProjectState) -> ProjectState:
    # Call LLM with role prompt, update state["prd"]
    ...

def architect_node(state: ProjectState) -> ProjectState:
    # Read state["prd"], update state["architecture"]
    ...

def engineer_node(state: ProjectState) -> ProjectState:
    # Read state["architecture"], update state["code"]
    ...

def qa_node(state: ProjectState) -> ProjectState:
    # Execute tests against state["code"], update state["test_results"]
    ...

def reviewer_node(state: ProjectState) -> ProjectState:
    # Review state["code"], update state["review_notes"]
    ...

# Human-in-the-loop gates use interrupt_before
def route_after_prd(state: ProjectState) -> str:
    return "architect"  # or "END" if human rejects

# Build graph
builder = StateGraph(ProjectState)
builder.add_node("pm", product_manager_node)
builder.add_node("architect", architect_node)
builder.add_node("engineer", engineer_node)
builder.add_node("qa", qa_node)
builder.add_node("reviewer", reviewer_node)

builder.set_entry_point("pm")
builder.add_edge("pm", "architect")          # after PRD
builder.add_edge("architect", "engineer")    # after arch spec
builder.add_edge("engineer", "qa")           # after code
builder.add_edge("qa", "reviewer")           # after tests
builder.add_edge("reviewer", END)

graph = builder.compile(interrupt_before=["architect", "engineer"])  # human gates
```

---

## Claude Code Agent Teams Pattern

The most frictionless option if you are already using Claude Code:

```yaml
# .claude/agents/product-manager.yml
name: product-manager
model: claude-opus-4-7
system: |
  You are a senior Product Manager. Given a user prompt, produce a complete PRD in /artifacts/prd.md.
  Include: problem statement, user stories, acceptance criteria, out-of-scope items.
  Do not begin coding. Your output is documentation only.
tools:
  - read
  - write
  - edit

# .claude/agents/engineer.yml
name: engineer
model: claude-sonnet-4-6
system: |
  You are a senior software engineer. Read /artifacts/architecture.md and implement all components.
  Write production-quality code. No TODOs. No placeholder comments. All files go in /src/.
tools:
  - read
  - write
  - edit
  - bash
```

Then orchestrate from the main Claude Code session:
```
"Run the product-manager agent on this prompt: [your prompt]. After I approve the PRD, run the architect agent, then the engineer, then qa, then reviewer."
```

---

## MCP Tool Stack for the Agent Team

| Tool | MCP Server | Purpose |
|---|---|---|
| File I/O | `@anthropic/filesystem-mcp` | Read/write all project files |
| Git | `@modelcontextprotocol/github-mcp` | Commits, PRs, branch management |
| Code Execution | `e2b-mcp` or `@anthropic/code-execution` | Run code in sandbox, get output |
| Browser / UI Testing | `@microsoft/playwright-mcp` | Navigate, click, screenshot, assert |
| Live Docs | `context7` | Fetch current library documentation |
| Search | `brave-search-mcp` | Research during architecture phase |

Config example (`.mcp.json` in repo root — committed so all agents share it):
```json
{
  "mcpServers": {
    "filesystem": { "command": "npx", "args": ["-y", "@anthropic/mcp-filesystem", "/workspace"] },
    "github": { "command": "npx", "args": ["-y", "@modelcontextprotocol/mcp-github"], "env": { "GITHUB_TOKEN": "${GITHUB_TOKEN}" } },
    "e2b": { "command": "npx", "args": ["-y", "e2b-mcp"], "env": { "E2B_API_KEY": "${E2B_API_KEY}" } },
    "playwright": { "command": "npx", "args": ["-y", "@microsoft/playwright-mcp"] },
    "context7": { "command": "npx", "args": ["-y", "context7-mcp"] }
  }
}
```

---

## Agent Memory & State Handoff Best Practices

**Multi-scope memory model**: tag every memory write with `user_id`, `agent_id`, `session_id`, and `org_id`. At retrieval, the pipeline merges and ranks results across all applicable scopes.

**Explicit artifacts over conversational handoffs**: each agent writes its output to a named file (`/artifacts/prd.md`, `/artifacts/architecture.md`, etc.) rather than passing text in a chat thread. This creates audit trails and prevents "telephone game" information loss.

**Atomic state operations**: critical state updates (PRD approval, arch sign-off) should be atomic — either fully written or not at all — to prevent partial-state corruption in long-running workflows.

**LangGraph checkpoints**: use `interrupt_before` on critical nodes to pause and resume across sessions without losing progress. State is persisted to a SQLite or Redis checkpoint.

**Isolate agent contexts**: each agent should only see what it needs (its system prompt + its input artifact). Cross-pollinating all prior messages degrades performance and increases cost. Agents in Claude Code subagents get their own isolated context window by default.

---

## Cost Optimization Strategy

| Agent | Recommended Model | Rationale |
|---|---|---|
| Product Manager | Opus 4.7 | Ambiguity resolution requires best judgment |
| Architect | Opus 4.7 | System design mistakes compound downstream |
| Project Manager | Sonnet 4.6 | Task decomposition is structured |
| Engineer | Sonnet 4.6 | Implementation is iterative with tool calls |
| QA | Sonnet 4.6 | Test generation is formulaic |
| Reviewer | Opus 4.7 | Final quality gate needs highest accuracy |

Use `claude-haiku-4-5` for repetitive subtasks (e.g., generating boilerplate, reformatting files) to minimize cost. A typical mid-sized project (10–20 files, 1,000–5,000 lines) costs $2–10 total with this split.

---

## Quick-Start Checklist

- [ ] Choose framework: CrewAI (fast), LangGraph (complex), Claude Code Agent Teams (native)
- [ ] Define 5 agents: PM, Architect, [PM/PM optional], Engineer, QA, Reviewer
- [ ] Write YAML/Python agent definitions with: role, goal, backstory, tools, model
- [ ] Set up MCP tool stack: filesystem + github + code execution + playwright
- [ ] Add 3 human-in-the-loop gates: PRD approval, arch approval, final review
- [ ] Test on a small project first (CLI tool, single-module API)
- [ ] Add shared `/artifacts/` directory for inter-agent handoffs
- [ ] Commit `.mcp.json` to repo so all agents share tool config

---

## Open Questions

1. How do agent teams handle ambiguous or contradictory requirements in the PRD?
2. What's the best strategy for multi-service projects where engineer agents need to coordinate APIs?
3. How do LangGraph's new cloud-hosted checkpoints (LangGraph Cloud, 2026) compare to self-managed persistence?
4. Can MetaGPT-style structured artifact passing be used inside Claude Code Agent Teams?
5. What's the right token budget strategy when the codebase grows beyond 100 files and context limits become a factor?

---

## Sources

- [AI Agent Frameworks Compared (2026)](https://pecollective.com/blog/ai-agent-frameworks-compared/)
- [Multi-Agent AI in 2026: CrewAI, LangGraph & AutoGen](https://dev.to/ottoaria/multi-agent-ai-in-2026-build-production-systems-with-crewai-langgraph-autogen-5e40)
- [LangGraph vs CrewAI vs AutoGen: The Complete Guide](https://pockit.tools/blog/langgraph-crewai-autogen-multi-agent-orchestration-guide/)
- [The AI Agent Stack in 2026](https://thenuancedperspective.substack.com/p/the-ai-agent-stack-in-2026)
- [The State of AI Coding Agents (2026)](https://medium.com/@dave-patten/the-state-of-ai-coding-agents-2026-from-pair-programming-to-autonomous-ai-teams-b11f2b39232a)
- [Agentic Coding 2026: Multi-Agent AI Teams](https://aiautomationglobal.com/blog/agentic-coding-revolution-multi-agent-teams-2026)
- [AgentMesh: Cooperative Multi-Agent Framework](https://arxiv.org/html/2507.19902v1)
- [MetaGPT: Multi-Agent Framework](https://github.com/FoundationAgents/MetaGPT)
- [Claude Code Agent Teams Guide 2026](https://claudefa.st/blog/guide/agents/agent-teams)
- [Claude Code Subagents: Complete Guide](https://skillsplayground.com/guides/claude-code-agents/)
- [Best Practices for Multi-Agent Systems 2026](https://medium.com/online-inference/best-practices-for-building-effective-ai-agents-and-multi-agent-systems-2c7fe11c9605)
- [State of AI Agent Memory 2026](https://mem0.ai/blog/state-of-ai-agent-memory-2026)
- [Best MCP Servers for Developers 2026](https://www.builder.io/blog/best-mcp-servers-2026)
- [LangGraph + MCP Multi-Agent Workflow Guide 2026](https://techbytes.app/posts/langgraph-mcp-multi-agent-workflow-guide-2026/)
- [CrewAI: Role-Based Agent Orchestration](https://www.digitalocean.com/community/tutorials/crewai-crash-course-role-based-agent-orchestration)
