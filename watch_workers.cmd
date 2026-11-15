@echo off
cd /d "%~dp0"
set "KRUGRADE_PYTHON=%USERPROFILE%\.cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
if exist "%KRUGRADE_PYTHON%" (
  "%KRUGRADE_PYTHON%" -B -X utf8 watch_workers.py
) else (
  python -B -X utf8 watch_workers.py
)
pause
