@echo off
echo ========================================
echo    Windows Security Scanner
echo ========================================
echo.

REM Check if running as administrator
net session >nul 2>&1
if %errorLevel% == 0 (
    echo Administrator privileges confirmed.
) else (
    echo WARNING: Administrator privileges recommended.
    echo Some features may not work properly.
    echo.
)

echo Starting Security Scanner...
python security_scanner.py

echo.
echo Security scan completed.
pause
