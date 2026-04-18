# Monthly Review: {{date:MMMM YYYY}}

## 🎯 Goals for the Month
- [ ] 
- [ ] 
- [ ] 

## 📊 Habit Overview (Past 30 Days)

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
WHERE file.ctime >= this.file.ctime - dur(30 days)
SORT file.name ASC
```

## 🪞 Monthly Reflection
*What are my biggest takeaways from this month? Did my daily actions align with my bigger goals?*
- **Strongest habit this month:** - **Habit that needs the most work next month:** - **Overall thoughts:** ````

*(Note: Just remember to change `"Daily Notes"` in the `FROM` line of both Dataview queries to whatever folder name you actually use to store your daily notes!)*