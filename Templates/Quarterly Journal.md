# Quarterly Review: {{date:YYYY - [Q]Q}}

## 🎯 Goals for this Quarter
- [ ] 
- [ ] 
- [ ] *Example: Hit new PRs in hybrid lifting and running program*

## 📊 Habit Overview (Past 90 Days)

```dataview
TABLE WITHOUT ID
  file.link AS "Day",
  choice(eat_clean, "✅", "❌") AS "Clean",
  choice(stretch, "✅", "❌") AS "Stretch",
  choice(read_30, "✅", "❌") AS "Read",
  choice(less_scrolling, "✅", "❌") AS "Scroll",
  choice(more_sunlight, "✅", "❌") AS "Sun",
  choice(skincare, "✅", "❌") AS "Skin",
  choice(oral_care, "✅", "❌") AS "Teeth",
  choice(chinese_20, "✅", "❌") AS "Chinese",
  choice(sleep_90, "✅", "❌") AS "Sleep",
  choice(bible_study, "✅", "❌") AS "Bible",
  choice(no_weed, "✅", "❌") AS "Weed",
  choice(no_early_caffeine, "✅", "❌") AS "Caff",
  choice(no_porn, "✅", "❌") AS "Porn",
  choice(no_alcohol, "✅", "❌") AS "Alc"
FROM "Daily" 
WHERE file.ctime >= this.file.ctime - dur(90 days)
SORT file.name ASC
```

## 🪞 Quarterly Reflection
*What were the defining themes of this quarter? What is working well in my routine, and what needs a complete overhaul?*
-