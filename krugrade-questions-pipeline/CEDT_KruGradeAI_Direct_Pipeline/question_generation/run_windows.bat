@echo off
cd /d "%~dp0"
python run_pipeline.py run
if errorlevel 1 (
    echo Pipeline failed. Check output\validation_report.json
    pause
    exit /b 1
)
echo Output is ready in the output folder.
pause
