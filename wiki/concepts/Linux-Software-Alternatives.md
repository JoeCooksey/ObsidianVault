---
type: concept
title: "Linux Software Alternatives"
status: developing
created: 2026-05-26
updated: 2026-05-26
tags:
  - linux
  - software
  - open-source
  - productivity
---

# Linux Software Alternatives

Reference table for Windows software with no native Linux version and their best open-source or native Linux replacements. See [[Windows-to-Linux-Complete-Guide]] for full context.

---

## Productivity / Office

| Windows App | Linux Status | Best Linux Alternative |
|---|---|---|
| Microsoft Word | No native | LibreOffice Writer, OnlyOffice, Google Docs |
| Microsoft Excel | No native | LibreOffice Calc, Google Sheets |
| Microsoft PowerPoint | No native | LibreOffice Impress, Google Slides |
| Microsoft Outlook | No native | Thunderbird (email), Evolution (full PIM) |
| Microsoft OneNote | No native | Obsidian, Joplin, Standard Notes |
| Notion | Web app ✅ | Same web app |

**Compatibility caveat**: LibreOffice handles basic .docx/.xlsx well. Complex macros, advanced Excel formulas, and heavily formatted PowerPoint files may render incorrectly. OnlyOffice has better compatibility for complex Office files.

---

## Creative / Adobe

| Windows App | Linux Status | Best Linux Alternative |
|---|---|---|
| Adobe Photoshop | No native | GIMP (free; layer-based; most feature-complete) |
| Adobe Lightroom | No native | Darktable (free; non-destructive; RAW support) |
| Adobe Illustrator | No native | Inkscape (free; SVG-native; vector graphics) |
| Adobe Premiere | No native | Kdenlive (free), DaVinci Resolve (free tier) |
| Adobe After Effects | No native | Natron, Blender (compositor) |
| Adobe Audition | No native | Audacity (simple), Ardour (professional DAW) |
| Adobe InDesign | No native | Scribus (free; desktop publishing) |
| Figma | Web app ✅ | Same web app (browser); also Penpot (open-source) |

**Note**: DaVinci Resolve has a native Linux version — the free tier covers most needs. It is the strongest cross-platform video editor.

---

## Developer Tools (mostly available natively ✅)

| Tool | Linux Status |
|---|---|
| VS Code | Native ✅ |
| JetBrains IDEs | Native ✅ |
| Git | Native ✅ (superior to Windows Git) |
| Python | Native ✅ |
| Node.js / npm | Native ✅ |
| Docker | Native ✅ (no Docker Desktop overhead) |
| WSL2 | N/A — you *are* Linux |
| Postman | Native ✅ |

---

## Communication / Productivity Apps (mostly available ✅)

| App | Linux Status |
|---|---|
| Discord | Native ✅ |
| Slack | Native ✅ |
| Microsoft Teams | Native ✅ (Electron) |
| Zoom | Native ✅ |
| Spotify | Native ✅ |
| Telegram | Native ✅ |
| Signal | Native ✅ |
| WhatsApp | Web app only |

---

## EE-Specific Tools (Joe-relevant)

| Tool | Linux Status |
|---|---|
| LTSpice | Via Wine (functional, some quirks) or use on Windows in dual-boot |
| KiCad | Native ✅ (Linux is primary development platform) |
| GNU Octave (MATLAB alternative) | Native ✅ |
| Python + SciPy + Matplotlib | Native ✅ |
| Icarus Verilog + GTKWave | Native ✅ |
| STM32CubeIDE | Native ✅ |
| Wireshark | Native ✅ |
| Arduino IDE | Native ✅ |

**Key insight for Joe**: Linux is actually *better* for EE development. KiCad, GTKWave, Icarus Verilog, Python simulation stack all work better or equally well. The only EE tool that needs workaround is LTSpice (Wine-based or dual-boot into Windows for simulation-critical work).

---

## Gaming

| Situation | Linux Solution |
|---|---|
| Steam library | Proton — 80%+ of catalog |
| GOG / Epic games | Lutris (install scripts + Wine/Proton) |
| Emulators | RetroArch, Dolphin, RPCS3 — native and often better |
| Anti-cheat games (Valorant) | **Not supported** — kernel-level anti-cheat blocks Linux |
| Check compatibility | [ProtonDB.com](https://www.protondb.com) |

---

## Related Pages
- [[Windows-to-Linux-Complete-Guide]] — full migration guide
- [[Linux-Distros-for-Windows-Switchers]] — which distro to choose
