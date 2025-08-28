@echo off
echo ========================================
echo Windows Optimizer EXE Builder
echo ========================================
echo.

REM Check if Python is installed
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python is not installed or not in PATH.
    echo Please install Python 3.x from https://python.org
    pause
    exit /b 1
)

echo Python found. Installing PyInstaller...
pip install pyinstaller --quiet

if errorlevel 1 (
    echo ERROR: Failed to install PyInstaller.
    echo Try running: pip install pyinstaller
    pause
    exit /b 1
)

echo.
echo Building executable with GUI support...
echo This may take a few minutes...
echo.

REM Clean previous builds
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
if exist *.spec del *.spec

REM Build the executable with GUI support
pyinstaller --onefile --noconsole --windowed --name windows_optimizer --icon=icon.ico windows_optimizer.py

if errorlevel 1 (
    echo ERROR: Failed to build executable.
    echo Trying without icon...
    pyinstaller --onefile --noconsole --windowed --name windows_optimizer windows_optimizer.py
)

if errorlevel 1 (
    echo ERROR: Build failed completely.
    pause
    exit /b 1
)

echo.
echo ========================================
echo Build completed successfully!
echo ========================================
echo.
echo Your executable is located at:
echo %CD%\dist\windows_optimizer.exe
echo.
echo To run the optimizer:
echo 1. Double-click on windows_optimizer.exe
echo 2. Select your desired optimizations
echo 3. Click "Apply Optimizations"
echo.
echo For command-line mode, run:
echo windows_optimizer.exe --cli
echo.
echo Press any key to exit...
pause >nul
