---
type: concept
title: "Linux Mint Fresh-Install Essential Apps"
status: developing
created: 2026-05-28
updated: 2026-05-28
tags:
  - linux
  - linux-mint
  - software
  - open-source
  - apps
related:
  - "[[Linux-Mint-Cinnamon-Customization-Guide]]"
  - "[[Linux-Software-Alternatives]]"
  - "[[Linux-Mint-vs-Zorin-vs-PopOS-Guide]]"
---

# Linux Mint Fresh-Install Essential Apps

What to install on a fresh Linux Mint setup. All open source. For Windows→Linux replacement mapping, see [[Linux-Software-Alternatives]]; for making it look nice, see [[Linux-Mint-Cinnamon-Customization-Guide]]. (Source: [[Research - Linux Mint Customization and Software]])

> [!note] Mint already includes a lot
> A default Mint install ships LibreOffice, Firefox, Thunderbird, the Software Manager, **Timeshift**, **Warpinator**, and the Cinnamon spices system. Don't reinstall what's already there — this list is the *additions* most people want.

---

## System & maintenance (install day one)

| App | Why | Status |
|---|---|---|
| **Timeshift** | System snapshots / rollback before risky changes | Pre-installed — just configure it |
| **Synaptic** | Deep package manager with dependency control & search | `sudo apt install synaptic` |
| **GNOME Disks / GParted** | Disk health, partitioning | `sudo apt install gparted` |
| **Flatpak** (Flathub) | Access to newer app versions than the apt repos | Built into Software Manager; enable Flathub |

---

## Everyday / productivity

- **VLC** — plays virtually any media format. *(high)*
- **Obsidian / Joplin** — notes & second brain (Obsidian via Flatpak/AppImage; Joplin is fully FOSS).
- **Thunderbird** — email + calendar (pre-installed).
- **OnlyOffice** — better MS Office `.docx/.xlsx` fidelity than LibreOffice for complex files. (Source: [[Linux-Software-Alternatives]])
- **Bitwarden / KeePassXC** — password manager.

## Creative

- **GIMP** — Photoshop-class raster editor. *(high)*
- **Inkscape** — vector graphics (Illustrator alternative). *(high)*
- **Krita** — digital painting.
- **Darktable** — RAW photo / Lightroom alternative. (Source: [[Linux-Software-Alternatives]])
- **Kdenlive** or **Shotcut** — video editing.
- **Audacity** — audio editing.
- **OBS Studio** — screen recording / streaming.

## Internet & utilities

- **FileZilla** — FTP/SFTP client.
- **qBittorrent** — torrents, ad-free.
- **Flameshot** — best-in-class screenshot tool with annotation.
- **Wine / Bottles** — run Windows apps that have no Linux version. (Source: [[Linux-Software-Alternatives]])

---

## How to install (preference order)

1. **Software Manager** (GUI) — easiest; covers most of the above.
2. **Flatpak / Flathub** — when you need a newer version than apt ships.
3. **`apt` / PPA** — terminal; for tools or theme packs not in the GUI.
4. **AppImage / `.deb`** — last resort for apps not packaged elsewhere.

> [!tip] Stay system-package-first
> Prefer Software Manager / apt over random `.deb` files and curl-pipe-bash installers — they update automatically and don't fork your dependency tree.

> [!gap] Gaming not covered here
> Steam/Proton, Lutris, and GPU-driver setup are a separate topic — see [[Linux-Mint-vs-Zorin-vs-PopOS-Guide]] for the gaming/Nvidia angle.
