"""Paths and constants for the life dashboard. Paths resolve relative to this
file so the app works regardless of where the repo is checked out."""
from pathlib import Path

APP_DIR = Path(__file__).resolve().parent          # apps/life-dashboard
VAULT_ROOT = APP_DIR.parent.parent                 # Joe_Vault

ACCOUNTS_DIR = VAULT_ROOT / "Finance" / "Accounts"
SNAPSHOT_NOTE = VAULT_ROOT / "Finance" / "Portfolio Dashboard.md"
CACHE_DIR = APP_DIR / ".cache"

PRICE_TTL_SECONDS = 600
PORT = 5058
