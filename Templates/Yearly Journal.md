# Yearly Review: {{date:YYYY}}

## 🎯 Goals for the Year
- [ ] 
- [ ] 
- [ ] 

## 📊 Habit Overview (Past 365 Days)

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
WHERE file.ctime >= this.file.ctime - dur(365 days)
SORT file.name ASC
```

## 🪞 Yearly Reflection
**The Highlights:**
*What were my biggest accomplishments and best memories this year?*
- 

**The Hard Lessons:**
*What challenged me the most, and how did I grow from it?*
- 

**Looking Forward:**
*Who do I want to become by the end of next year? What systems do I need to build to get there?*
-