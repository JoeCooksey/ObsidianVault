---
type: meta
title: "Hot Cache"
updated: 2026-04-18T00:00:00
tags:
  - meta
---
# Recent Context

## Last Updated
2026-04-18 — Autoresearch: Wide Bandgap Semiconductors in EV Fast Charging

## Key Recent Facts

### WBG / EV Power Electronics (newest)
- **SiC is mandatory for 800V EVs**: 1200V blocking requirement makes silicon IGBTs nonviable; SiC MOSFETs are the only solution — used in all Porsche/Hyundai/Audi/Kia 800V platforms
- **SiC vs Si IGBT**: ~5% vehicle range improvement; ~2× higher slew rate; OBC efficiency 97%+ vs 93–95% for Si
- **GaN is the OBC winner**: hundreds of kHz switching vs SiC's ~100 kHz; 30–60% smaller passives; first production GaN OBCs in EVs by Q4 2025
- **1200V GaN battleground**: first commercial 1200V GaN transistors expected 2025, priced below SiC — could challenge SiC in 800V inverters if automotive-qualified
- **Wolfspeed**: 62% SiC wafer market share; Gen 4 platform January 2025; supply chain risk for EV OEMs
- **Ga₂O₃**: 4.8 eV bandgap, 8 MV/cm breakdown — theoretically superior to all; blocked by 0.1 W/mK thermal conductivity; 5–15 year horizon
- **V2G**: WBG eliminates reverse-recovery losses enabling bidirectional OBCs; grid integration (ISO 15118) is the deployment bottleneck, not power electronics

### AI / LLM Edge Computing (previous session)
- **INT4 AWQ/GGUF Q4_K_M**: practical sweet spot for edge LLM deployment
- **Thermal throttling**: primary mobile edge bottleneck — RPi+Hailo-10H is only <2W stable platform
- **BitNet b1.58**: 2.4–6× CPU speedup, 55–82% energy reduction; requires training from scratch

## Recent Changes
- Created 13 pages (WBG EV research): concepts, entities, sources, synthesis
- Updated [[Wiki Index]], [[Wiki Log]]

## Active Threads
- Two research areas now in wiki: LLM edge inference + WBG power electronics for EV
- Cross-domain connection: both fields optimize the same thing — more performance per watt in constrained hardware environments
- Open: 1200V GaN automotive qualification timeline; Ga₂O₃ thermal barrier solutions
