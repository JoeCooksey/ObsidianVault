---
type: source
title: "Udemy — Personal Plan Page and FAQ (July 2026)"
source_type: official-documentation
author: Udemy, Inc.
date_published: 2026-07-27
date_accessed: 2026-07-27
url: https://www.udemy.com/personal-plan/
confidence: high
status: complete
created: 2026-07-27
updated: 2026-07-27
tags:
  - source
  - domain/career
  - udemy
  - online-learning
key_claims:
  - "Personal Plan = 28,000+ curated courses out of Udemy's 250,000-course catalog"
  - "List price $35.00/month; promo $24.50/month (30% off first year, Jul 24–27 2026)"
  - "Subscription access ends when the subscription lapses; individual purchases are lifetime"
related:
  - "[[Udemy Personal Plan]]"
  - "[[Udemy]]"
---

# Udemy — Personal Plan Page and FAQ (July 2026)

Primary source. Udemy's own marketing page and FAQ accordion for the consumer subscription, read directly from the live page on 2026-07-27 (confidence: high — this is the vendor stating its own terms).

## Headline numbers

| Metric | Value |
|---|---|
| Courses in plan | **28,000+** |
| Practice exercises | 20,000+ |
| Average course rating | 4.5 |
| Instructors | 9,000+ |
| Full Udemy catalog (for contrast) | **250,000+** |
| List price | **$35.00/month** |
| Promo price (Jul 24–27, 2026) | $24.50/month — 30% off first year, annual billing |
| Individual course price | $19.99–$199.99, one-time |

So the plan is **~11% of Udemy's catalog**, curated.

## What Udemy says is included

- "Courses on in-demand professional topics — including web development, IT certification, data science, web design, digital marketing, and leadership — along with a selection of personal development topics, such as language learning, arts and creativity, and personal finance."
- **Udemy AI Assistant** for instant answers while learning
- **AI Role Play simulations**, **labs**, **coding exercises**, **certification exam practice tests**
- Certificates of completion from Udemy "or issuers like AWS, Microsoft, Google, CompTIA, and PMI"

> [!important] Engineering is not named anywhere in the marketing copy. The featured-collection carousel on the page shows only Web Development, Data Science, IT Certifications, Graphic Design & Illustration, Digital Marketing, Leadership, and Communication. The actual catalog is broader than the copy implies — see [[Udemy Personal Plan EE Coverage Map]].

## How courses are selected (verbatim)

> "The 28,000 courses included in Personal Plan are curated by Udemy's content experts from our catalog of 250,000 courses. We use insights from 75,000 global learners to identify top-rated, relevant courses on the most sought-after professional topics as well as a selection of personal development topics."

## Are all courses included? (verbatim)

> "**No.** The 28,000 courses in personal plan are our highest rated courses in tech, business, and personal development... You can access all of the in-demand courses within Personal Plan while you're subscribed, and still purchase courses outside of the subscription at any time."

## The access asymmetry

- **Subscription**: access lasts only while you pay. Stop paying, lose everything.
- **Individual purchase**: lifetime access to that course only.

This is the single most important structural fact for planning — see [[Udemy Personal Plan]].

## Method note

Udemy returns HTTP 403 to plain web-fetching tools. This page was read by driving a real browser session and extracting `main.innerText` plus the expanded FAQ accordion, logged out, US locale.
