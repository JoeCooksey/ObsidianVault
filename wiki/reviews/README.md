---
type: meta
title: "Book Review System — How It Works"
created: 2026-05-27
updated: 2026-05-27
tags: [meta, reviews, srs]
---
# 📚 Daily Book Review System

## How to Use Each Review File

1. **Open today's review file** (e.g. `2026-05-27.md`)
2. **Read the question** — try to recall the answer before expanding
3. **Click the answer callout** to reveal it
4. **Check exactly one box** to rate yourself:
   - `✅ Got it` — you recalled it fully
   - `🔄 Almost` — you had it mostly right
   - `❌ Missed it` — you blanked or got it wrong
5. **Tomorrow's agent reads your ratings** and adjusts each card's interval accordingly

## Spaced Repetition Schedule (Leitner System)

| Box | Interval | Meaning |
|-----|----------|---------|
| 1 | Every 1 day | New or failed cards |
| 2 | Every 3 days | Starting to stick |
| 3 | Every 7 days | Fairly solid |
| 4 | Every 14 days | Well learned |
| 5 | Every 30 days | Long-term memory |

- **Got it** → card moves up one box (longer interval)
- **Almost** → card stays in same box (same interval)
- **Missed it** → card resets to Box 1 (review tomorrow)

## Card Deck

52 cards across 9 books, introduced 8 at a time every 2 days.

| Book | Cards | Author |
|------|-------|--------|
| Atomic Habits | 7 | James Clear |
| The 7 Habits of Highly Effective People | 7 | Stephen Covey |
| The Psychology of Money | 6 | Morgan Housel |
| Steve Jobs | 6 | Walter Isaacson |
| Leonardo da Vinci | 6 | Walter Isaacson |
| Never Eat Alone | 5 | Keith Ferrazzi |
| How to Win Friends and Influence People | 5 | Dale Carnegie |
| The Subtle Art of Not Giving a F*ck | 5 | Mark Manson |
| The Laws of Human Nature | 5 | Robert Greene |

## Files

- `wiki/books/flashcards/*.json` — card content + SRS state (managed by agent)
- `wiki/reviews/YYYY-MM-DD.md` — daily review sessions (you interact here)
