---
type: source
title: "Pop!_OS Dual Boot Setup Guide"
status: complete
created: 2026-05-26
updated: 2026-05-26
tags:
  - linux
  - pop-os
  - dual-boot
  - windows
  - gaming
  - nvidia
  - how-to
---

# Pop!_OS Dual Boot Setup Guide

Full step-by-step guide for running Pop!_OS alongside Windows on a gaming PC with an Nvidia GPU. See [[Windows-to-Linux-Complete-Guide]] for context on why to switch, and [[Linux-Distros-for-Windows-Switchers]] for distro comparison.

**Time required:** 1.5–2 hours
**Target setup:** Windows already installed, Nvidia GPU, gaming PC

---

## Before You Start — Two Common Failure Points

1. **Fast Startup** — Windows locks the drive on shutdown. Linux installer can't work alongside it. Must be disabled first.
2. **Secure Boot** — blocks unsigned bootloaders. Pop!_OS needs it off in BIOS.

Both are fixed in Phase 1 and Phase 3 below. Don't skip them.

---

## What You Need

- USB drive, 8 GB minimum (gets wiped)
- External drive or cloud backup destination
- Gaming PC running Windows
- Internet connection

---

## Phase 1 — Windows Prep

### 1.1 Back Up Important Files

```
□ Documents, Desktop, Downloads
□ Game saves (check %APPDATA%\Roaming for some games)
□ Browser bookmarks (Chrome: Settings → Bookmarks → Export)
□ Software license keys
□ Photos/videos not already backed up
```

CS2 saves are Steam Cloud synced. OSRS progress is server-side. Nothing to back up for either.

---

### 1.2 Disable Fast Startup

`Win` → search **"Power & sleep settings"** → open it
→ **Additional power settings**
→ **Choose what the power buttons do** (left panel)
→ **Change settings that are currently unavailable**
→ Uncheck **"Turn on fast startup (recommended)"**
→ **Save changes**

---

### 1.3 Confirm UEFI Mode

`Win + R` → type `msinfo32` → Enter
Look for **BIOS Mode** in the list.
- **UEFI** → modern setup, you're good
- **Legacy** → note this; changes one step in Phase 4

Almost every gaming PC from 2015+ is UEFI.

---

### 1.4 Shrink Your Windows Partition

**If you have a second SSD/HDD:** skip this — install Pop!_OS on that drive entirely.

**Single drive only:**

`Win + X` → **Disk Management**
→ Right-click **C:** → **Shrink Volume**
→ In the shrink box, enter MB:
- `61440` = 60 GB (minimum)
- `102400` = 100 GB (recommended if using Linux daily)

→ Click **Shrink**

A grey **Unallocated Space** block appears. Leave it — don't format it. The Linux installer claims it.

**If Disk Management won't shrink enough** (blocked by system files):
```powershell
# Run PowerShell as Administrator
powercfg /h off    # disables hibernation file
# Then retry shrink in Disk Management
```

---

## Phase 2 — Download & Create Bootable USB

### 2.1 Download the Pop!_OS Nvidia ISO

`system76.com/pop` → **Download** → choose **NVIDIA**

The Nvidia ISO (~1.3 GB) bundles the proprietary driver. This is the one you want — no driver hunting after install.

---

### 2.2 Write ISO to USB with Rufus

Download Rufus from `rufus.ie` (free, no install, just run the .exe).

| Field | Value |
|---|---|
| Device | Your USB drive |
| Boot selection | SELECT → pick the Pop!_OS .iso |
| Partition scheme | **GPT** (for UEFI systems) |
| Target system | UEFI (non-CSM) |
| File system | FAT32 (auto) |

**START** → if prompted, choose **Write in DD Image mode** → accept USB wipe warning.

Takes ~5–10 minutes.

---

## Phase 3 — BIOS Setup

### 3.1 Enter BIOS

Fully shut down → power on → spam your BIOS key:

| Motherboard | Key |
|---|---|
| ASUS | **Delete** or F2 |
| MSI | **Delete** |
| Gigabyte | **Delete** or F2 |
| ASRock | **F2** |
| Unknown | Try **Delete** first |

---

### 3.2 Disable Secure Boot

Find **Security** or **Boot** tab → **Secure Boot** → **Disabled**

Some boards require a supervisor password before this option unlocks — set one if prompted.

---

### 3.3 Set Boot Order

Find **Boot Priority** → move **USB drive** to position #1 (above Windows Boot Manager).

---

### 3.4 Save and Exit

**Save & Exit** → **Save Changes and Reset** (or F10 on most boards).

PC restarts and boots from USB.

---

## Phase 4 — Installation

### 4.1 Live Environment

Pop!_OS boots to a live desktop. Select your language.

Choose **Try Demo Mode** first — don't install immediately.

---

### 4.2 Test Hardware (5 minutes — don't skip)

In the live demo, verify:
- Monitor shows correct resolution
- Wi-Fi appears in top-right network menu
- Browser loads a page
- Audio works in sound settings

If something doesn't work in live mode, research the fix before installing — it won't fix itself post-install.

Everything working → double-click **Install Pop!_OS**.

---

### 4.3 The Installer

Walk through: Language → Keyboard → Drive selection (critical screen below).

---

#### Two-Drive Setup (install Linux on second drive)

Select **Custom (Advanced)**
→ Find your second drive in the list (not the one with Windows)
→ Click it → **Erase and Install**

Windows drive is untouched.

---

#### Single-Drive Setup (using unallocated space)

Select **Custom (Advanced)**

You'll see something like:
```
/dev/sda1  100 MB    EFI System Partition
/dev/sda2  16 MB     Microsoft reserved
/dev/sda3  850 GB    Windows (NTFS)       ← C: drive — do not touch
/dev/sda4  700 MB    Windows Recovery
            100 GB   Free Space            ← your unallocated space
```

Click **Free Space** → click **+**

| Setting | Value |
|---|---|
| Size | Full remaining space |
| Type | ext4 |
| Mount point | `/` |

→ **Create**

Leave the EFI partition alone — Pop!_OS detects it automatically and adds itself.

→ **Erase and Install** (only erases what you assigned — not Windows)

---

### 4.4 User Setup

| Field | Value |
|---|---|
| Full name | Your name |
| Username | Lowercase, no spaces (used for login + `sudo`) |
| Password | Strong — you'll type this for system commands |
| Encrypt drive | Skip for a home gaming PC |

→ **Set Up User** → installation runs (~10–20 min)

---

### 4.5 Reboot

**Restart** → pull USB out when screen goes black.

---

## Phase 5 — First Boot

### 5.1 The Boot Menu

Pop!_OS uses **systemd-boot** (not GRUB — looks different from most distros):

```
Pop!_OS
Windows Boot Manager
```

Arrow keys + Enter to select. Default is Pop!_OS.

> **Note:** Windows updates sometimes reset boot priority back to Windows, making the Pop!_OS menu disappear. Fix: go back into BIOS → restore boot order. This is the one recurring dual-boot annoyance.

---

### 5.2 Verify Nvidia Driver

Open terminal (`Ctrl+Alt+T` or Super → type "terminal"):

```bash
nvidia-smi
```

Should show your GPU model and driver version. If it does — the Nvidia ISO worked perfectly.

If it fails:
```bash
sudo apt install nvidia-driver-550
sudo reboot
```

---

### 5.3 Update Everything

```bash
sudo apt update && sudo apt upgrade -y
sudo reboot   # if kernel or driver updates installed
```

---

### 5.4 Enable Firewall

```bash
sudo ufw enable
```

---

## Phase 6 — Gaming Setup

### CS2

```bash
sudo apt install steam -y
```

Steam → **Settings** → **Compatibility** tab:
- Enable **"Steam Play for all titles"**
- Set to **Proton Experimental**

Install CS2 from library normally. Runs through Proton automatically.

VAC (Valve Anti-Cheat) works fine on Linux — CS2 is a Valve game and one of the best-supported titles on Proton. Expected FPS: within 5–10% of Windows.

---

### Old School RuneScape (RuneLite)

Go to `runelite.net` → download **Linux** AppImage:

```bash
chmod +x RuneLite-*.AppImage    # make executable
./RuneLite-*.AppImage           # run
```

Or right-click the file → Properties → **Allow executing as program** → double-click.

RuneLite is Java — runs identically on any OS. Zero compatibility concerns.

---

## Phase 7 — Quality of Life

### Useful Terminal Tools

```bash
sudo apt install htop neofetch git curl wget -y
```

- `htop` — better Task Manager in terminal
- `neofetch` — shows system info; run once to confirm everything's detected

---

### Pop!_Shop (App Store)

Click **Pop!_Shop** in the taskbar. Install Discord, Spotify, VLC, GIMP, etc. with one click.

Or terminal:
```bash
sudo apt install vlc gimp discord -y
```

---

### Adjust Boot Menu Timeout (optional)

Default boot menu waits 5 seconds. To change:

```bash
sudo nano /boot/efi/loader/loader.conf
```

Change `timeout 5` to however many seconds you want. `Ctrl+X` → Y → Enter to save.

---

## Troubleshooting

| Problem | Fix |
|---|---|
| Boot menu gone — boots straight to Windows | BIOS → boot order → move Pop!_OS back to #1 |
| No Wi-Fi after install | `sudo apt install linux-firmware` then reboot |
| Wrong screen resolution | System Settings → Displays → set manually |
| CS2 won't launch | Steam → CS2 → Properties → Compatibility → force Proton 9.0 |
| `nvidia-smi` fails after kernel update | `sudo apt install --reinstall nvidia-driver-550` |
| Windows partition shows as read-only | Fast Startup wasn't disabled — boot Windows, disable it, shut down properly, retry |
| Pop!_OS boot menu disappeared after Windows update | BIOS → restore boot order (happens occasionally after major Windows updates) |

---

## Full Checklist

```
□ Files backed up
□ Fast Startup disabled in Windows
□ Confirmed UEFI mode (msinfo32)
□ Windows partition shrunk OR second drive identified
□ Pop!_OS NVIDIA ISO downloaded
□ ISO written to USB with Rufus (GPT mode)
□ Secure Boot disabled in BIOS
□ USB set as first boot device
□ Live environment tested — all hardware works
□ Installed to correct partition/drive
□ nvidia-smi shows GPU on first boot
□ sudo apt update && sudo apt upgrade run
□ ufw firewall enabled
□ Steam installed → Proton enabled
□ CS2 installed and launched
□ RuneLite installed and logged in
```

---

## Related Pages
- [[Windows-to-Linux-Complete-Guide]] — full pros/cons, software alternatives, distro overview
- [[Linux-Distros-for-Windows-Switchers]] — distro comparison and decision matrix
- [[Linux-Software-Alternatives]] — what replaces Windows apps on Linux
