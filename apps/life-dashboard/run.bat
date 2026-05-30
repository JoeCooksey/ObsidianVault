@echo off
REM Life Dashboard launcher
cd /d "%~dp0"
if not exist ".venv" (
  echo Creating virtual environment...
  python -m venv .venv
  call .venv\Scripts\activate.bat
  echo Installing dependencies...
  pip install -r requirements.txt
) else (
  call .venv\Scripts\activate.bat
)
echo.
echo Starting Life Dashboard at http://127.0.0.1:5058
start "" http://127.0.0.1:5058
python app.py
