# Windows Optimizer EXE Builder (PowerShell)
# Run this script on Windows to build the executable

param(
    [switch]$Clean,
    [switch]$Verbose
)

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Windows Optimizer EXE Builder" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check if Python is installed
try {
    $pythonVersion = python --version 2>$null
    if ($LASTEXITCODE -ne 0) {
        throw "Python not found"
    }
    Write-Host "✓ Python found: $pythonVersion" -ForegroundColor Green
} catch {
    Write-Host "❌ ERROR: Python is not installed or not in PATH." -ForegroundColor Red
    Write-Host "Please install Python 3.x from https://python.org" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

# Install PyInstaller
Write-Host "Installing PyInstaller..." -ForegroundColor Yellow
try {
    pip install pyinstaller --quiet
    if ($LASTEXITCODE -ne 0) {
        throw "Failed to install PyInstaller"
    }
    Write-Host "✓ PyInstaller installed successfully" -ForegroundColor Green
} catch {
    Write-Host "❌ ERROR: Failed to install PyInstaller." -ForegroundColor Red
    Write-Host "Try running: pip install pyinstaller" -ForegroundColor Yellow
    Read-Host "Press Enter to exit"
    exit 1
}

Write-Host ""
Write-Host "Building executable with GUI support..." -ForegroundColor Yellow
Write-Host "This may take a few minutes..." -ForegroundColor Yellow
Write-Host ""

# Clean previous builds if requested
if ($Clean) {
    Write-Host "Cleaning previous builds..." -ForegroundColor Yellow
    if (Test-Path "build") { Remove-Item "build" -Recurse -Force }
    if (Test-Path "dist") { Remove-Item "dist" -Recurse -Force }
    Get-ChildItem "*.spec" | Remove-Item -Force
}

# Build arguments
$pyInstallerArgs = @(
    "--onefile",
    "--noconsole",
    "--windowed",
    "--name", "windows_optimizer"
)

if (Test-Path "icon.ico") {
    $pyInstallerArgs += "--icon=icon.ico"
}

$pyInstallerArgs += "windows_optimizer.py"

# Build the executable
try {
    if ($Verbose) {
        & pyinstaller $pyInstallerArgs
    } else {
        & pyinstaller $pyInstallerArgs 2>$null
    }

    if ($LASTEXITCODE -ne 0) {
        throw "PyInstaller failed"
    }
} catch {
    Write-Host "❌ ERROR: Failed to build executable." -ForegroundColor Red
    Write-Host "Trying without icon..." -ForegroundColor Yellow
    
    # Try without icon
    $pyInstallerArgsNoIcon = $pyInstallerArgs | Where-Object { $_ -ne "--icon=icon.ico" -and $_ -ne "icon.ico" }
    & pyinstaller $pyInstallerArgsNoIcon 2>$null
    
    if ($LASTEXITCODE -ne 0) {
        Write-Host "❌ ERROR: Build failed completely." -ForegroundColor Red
        Read-Host "Press Enter to exit"
        exit 1
    }
}

Write-Host ""
Write-Host "========================================" -ForegroundColor Green
Write-Host "Build completed successfully!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Green
Write-Host ""
Write-Host "Your executable is located at:" -ForegroundColor Cyan
Write-Host "$PWD\dist\windows_optimizer.exe" -ForegroundColor White
Write-Host ""
Write-Host "To run the optimizer:" -ForegroundColor Cyan
Write-Host "1. Right-click on windows_optimizer.exe" -ForegroundColor White
Write-Host "2. Select 'Run as administrator'" -ForegroundColor White
Write-Host ""
Write-Host "Press Enter to exit..." -ForegroundColor Yellow
Read-Host
