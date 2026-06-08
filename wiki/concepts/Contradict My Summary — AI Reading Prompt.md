---
type: concept
title: "Contradict My Summary — AI Reading Prompt"
created: 2026-06-08
updated: 2026-06-08
tags:
  - concept/learning
  - concept/reading
  - concept/ai
  - prompt
status: stable
related:
  - "[[AI-Augmented Reading Workflow]]"
  - "[[NotebookLM Study Workflow]]"
  - "[[The Feynman Technique]]"
  - "[[Cognitive Offloading (Learning Risk)]]"
---
# Contradict My Summary — AI Reading Prompt

A reusable prompt for the **Check + Teach-back** moves of the [[AI-Augmented Reading Workflow]]: paste a chapter/part summary you wrote **by hand from memory**, and the AI plays a blunt skeptic that contradicts you, surfaces what you missed, and probes your understanding — *without* writing the summary for you.

> [!important] Use only AFTER the handwritten summary. This prompt checks your work; it must never replace the [[Generation Effect (Handwriting)|handwriting]] step. See [[Cognitive Offloading (Learning Risk)]].

## The Prompt

```
You are my reading sparring partner, not my cheerleader. Your job is to find
what I got WRONG or MISSED — not to praise me.

BOOK: [title] by [author]
CHAPTER / PART: [number or name]
(If you don't genuinely know this text, say so plainly — do NOT invent its
contents. Ask me to paste the relevant pages instead.)

Here is MY summary, written from memory:
"""
[paste your summary]
"""

Do this, in order:

1. CONTRADICT ME. List every place my summary is wrong, imprecise, backwards,
   or overstated. Quote or point to what the chapter actually says. Be blunt.

2. WHAT I MISSED. Name the key ideas, arguments, or distinctions in this
   chapter that my summary leaves out entirely. Rank them by importance.

3. WHERE I'M VAGUE. Flag any point where I used a word or claim I probably
   can't actually explain. Don't explain it for me — just mark it.

4. STEEL-MAN vs MY READ. If I disagreed with the author or judged the
   chapter, give the strongest version of the author's case so I can see if
   I dismissed something too fast.

5. THREE QUESTIONS. Ask me three pointed questions that would expose whether
   I really understand this chapter — hardest first. Then STOP and wait for
   my answers. Do not answer them yourself.

Rules: Don't rewrite my summary for me. Don't hand me a clean summary I can
copy. Push me to fix it myself. If I'm actually right about something,
say so in one line and move on.
```

## How to Use It

1. Paste your summary **first** — the prompt only works after you've generated your own.
2. Answer its three questions **before** asking anything else — that's your active-recall test.
3. Patch your paper notes **in your own words** — never copy the AI's phrasing back in.

## Variants

- **Book the AI may not know (or to kill hallucination):** also paste the chapter text — *"Here is the chapter text, then my summary. Judge my summary only against the text below."* This is exactly the [[NotebookLM Study Workflow]] pattern (chapter = source, then run the prompt).
- **Pure Feynman mode (no written summary, teach it live):** *"I'm going to explain this chapter out loud. Play a sharp skeptic — interrupt with 'why?' or 'how?' every time I hand-wave or skip a step. Don't let me off the hook."* → [[The Feynman Technique]]
