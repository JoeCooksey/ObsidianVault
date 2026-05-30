---
type: source
title: "KiCad — Official Linux / Linux Mint Install Pages"
source_type: documentation
author: KiCad project (kicad.org)
date_published: 2026
url: https://www.kicad.org/download/details/linux-mint/
confidence: high
status: complete
created: 2026-05-28
updated: 2026-05-28
tags:
  - source
  - kicad
  - linux-mint
  - eda
  - pcb
key_claims:
  - "Current stable KiCad PPA is ppa:kicad/kicad-10.0-releases"
  - "Ubuntu-based Linux Mint works with the PPA; LMDE (Debian) does NOT — use Flatpak there"
  - "KiCad is not officially supported on Mint but is reported working via the Ubuntu PPA"
  - "Flatpak is the official recommended method for non-Ubuntu/non-Fedora distros and bundles libraries, 3D models, and docs"
related:
  - "[[EE-Software-on-Linux-Mint]]"
---

# KiCad — Official Linux Install Pages

Primary-source documentation from the KiCad project itself (authoritative).

## What it contributes
- **Current stable PPA**: `ppa:kicad/kicad-10.0-releases` (the line advanced 9.0 → 10.0; KiCad 9.0 shipped Feb 2025).
- **Install commands** (Ubuntu-based Mint):
  ```bash
  sudo add-apt-repository --yes ppa:kicad/kicad-10.0-releases
  sudo apt update
  sudo apt install --install-recommends kicad
  ```
- **Caveat**: "Linux Mint is not officially supported by the KiCad project," but Ubuntu derivatives "have been reported to work with this PPA." **LMDE (Linux Mint Debian Edition) does not work with the PPA** — those users must use Flatpak.
- **Flatpak** is the official recommended method outside Ubuntu/Fedora and bundles app + libraries + 3D models + documentation (`flathub org.kicad.KiCad`).

## Credibility
First-party project documentation. **High confidence** for install commands and PPA names. Version numbers are time-sensitive — re-check kicad.org before installing.
