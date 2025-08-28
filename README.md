# Windows Optimizer

A comprehensive Windows optimization tool that creates a system restore point and performs various cleanup and optimization tasks to improve system performance.

## 🆕 New Security Features

### 🔒 Antivirus Integration
- **Malwarebytes Support**: Check installation, run scans, guided installation
- **Windows Defender Integration**: Full system scans with progress tracking
- **Security Assessment**: Comprehensive security checks and recommendations
- **Standalone Security Scanner**: Dedicated `security_scanner.py` for focused security tasks

### 🛡️ Security Scanning Options
- **Malwarebytes Installation Check**: Verifies if Malwarebytes is installed and **prompts for installation** if not found
- **Interactive Installation Guide**: Step-by-step guided installation with user prompts and verification
- **Automated Malwarebytes Scan**: Attempts to run scan if software is installed
- **Windows Defender Full Scan**: Complete system scan using built-in Windows Defender
- **Security Recommendations**: Best practices and security tips

## Features

### System Maintenance
- ✅ Creates system restore point before any changes
- ✅ Runs System File Checker (SFC) to repair corrupted files
- ✅ Runs DISM to repair Windows image
- ✅ Clears Windows Update cache
- ✅ Clears DNS cache
- ✅ Cleans Windows.old folder

### Disk & Storage Optimization
- ✅ Cleans temporary files
- ✅ Runs Windows Disk Cleanup
- ✅ Defragments hard drives
- ✅ Clears browser caches (Chrome, Firefox, Edge)
- ✅ Clears Windows event logs
- ✅ Disables hibernation to save disk space
- ✅ Optimizes SSD settings (TRIM, defrag scheduling)

### Performance Optimization
- ✅ Optimizes Windows Search indexing
- ✅ Sets power plan to High Performance mode
- ✅ Optimizes visual effects (disables animations)
- ✅ Optimizes memory management (virtual memory)
- ✅ Optimizes network settings (TCP/IP tuning)
- ✅ Optimizes Game Mode for gaming performance

### Advanced System Tweaks
- ✅ Registry cleanup and optimization
- ✅ Disables unnecessary Windows services
- ✅ Manages startup programs for faster boot
- ✅ Optimizes security settings
- ✅ Applies advanced system optimizations
- ✅ Cleans up context menu items
- ✅ Optimizes GPU, USB, printer, audio, and Bluetooth settings
- ✅ Optimizes firewall and UAC settings
- ✅ Optimizes Windows Update and error reporting
- ✅ Optimizes remote desktop and task scheduler
- ✅ Optimizes font, icon, and thumbnail caches
- ✅ Optimizes prefetch/superfetch and ReadyBoost
- ✅ Optimizes Windows Store, Cortana, OneDrive, and Edge
- ✅ Disables telemetry services and Windows tips
- ✅ Optimizes memory, network, and power registry settings
- ✅ **Enable Ultimate Performance Plan** (maximum performance power scheme)
- ✅ **Optimize Pagefile & Memory** (RAM-based virtual memory tuning)
- ✅ **Tune GPU Driver Settings** (max performance, low latency graphics)
- ✅ **Kill Bloatware & Background Tasks** (Autoruns-style cleanup)
- ✅ **Fine-tune Network Stack** (disable Nagle, optimize NIC)
- ✅ **Kill Eye-candy & DWM Effects** (maximum performance visuals)
- ✅ **Keep SSD Clean (TRIM)** (SSD health and performance)

### Virus Checker & Security
- ✅ **Interactive Malwarebytes Installation** (prompts user if not installed)
- ✅ **Malwarebytes Scan** (automatic if installed)
- ✅ **Windows Defender Full Scan** (comprehensive system scan)
- ✅ **Security Recommendations** (best practices and tips)
- ✅ **Comprehensive Security Check** (full security assessment)

### Windows Updates
- ✅ **Default Settings** (reset Windows Update to stock settings)
- ✅ **Recommended Settings** (security-only; defer feature updates ~24 months)
- ✅ **Disable All Updates** (not recommended; for legacy/isolated systems)

## GUI Usage

### Running the Application
1. **Launch the executable** by double-clicking `windows_optimizer.exe`
2. **Select optimizations** by checking/unchecking the boxes
3. **Review selections** - some optimizations are mandatory for safety
4. **Click "Apply Optimizations"** to start the process
5. **Monitor progress** through the progress bar and log window

### GUI Features
- **Select All / Deselect All** buttons for quick selection
- **Scrollable optimization list** for easy navigation
- **Real-time status updates** during optimization
- **Detailed activity log** for troubleshooting
- **Success/failure notifications** with recommendations

### Command Line Mode
For advanced users or automation, you can still use the command line:

```bash
# Run with GUI (default)
windows_optimizer.exe

# Run in command-line mode (runs all optimizations)
windows_optimizer.exe --cli
```

## Requirements
- **Windows 10/11** operating system
- **Administrator privileges** (required for most optimizations)
- **No additional dependencies** - everything is bundled in the exe

### For Building from Source:
- **Python 3.8+** (only needed for building the exe)
- **PyInstaller** (automatically installed by build scripts)

## Building the Executable

### Method 1: Using Batch File (Recommended)
1. Transfer all files to your Windows machine
2. Right-click on `build_exe.bat`
3. Select "Run as administrator"
4. Wait for the build process to complete
5. Find your executable at `dist\windows_optimizer.exe`

### Method 2: Using PowerShell Script
1. Transfer all files to your Windows machine
2. Right-click on `build_exe.ps1`
3. Select "Run with PowerShell" (as administrator)
4. Wait for the build process to complete
5. Find your executable at `dist\windows_optimizer.exe`

### Method 4: Run Security Scanner Only
For security-focused scanning without full optimization:

```bash
# Run the standalone security scanner
python security_scanner.py

# Or use the batch file
run_security_scan.bat
```

The security scanner provides:
- Malwarebytes installation checking
- Windows Defender status and scanning
- Security recommendations
- Guided setup instructions

## How to Use the Optimizer

### Running the Executable
1. Locate `windows_optimizer.exe` in the `dist` folder
2. **Right-click** on the file
3. Select **"Run as administrator"**
4. The program will run automatically and show progress

### What Happens During Optimization
The tool will perform these operations in sequence:
1. **Safety Check** - Verifies Windows OS and admin privileges
2. **Restore Point** - Creates a system restore point
3. **Cache Cleaning** - Clears various system and browser caches
4. **System Repair** - Runs SFC and DISM scans
5. **Disk Optimization** - Cleans temp files and defragments drives
6. **Performance Tuning** - Optimizes search, power settings, and more

## Important Notes
- ⚠️ **Administrator privileges are required** for most optimizations
- 🔄 **System restore point is created automatically** before changes
- ⏱️ **Some operations may take several minutes** to complete
- 🔄 **Restart recommended** after optimization for best results
- 💾 **~500MB free space** recommended for the build process

## Troubleshooting

### Build Issues
- **"Python not found"**: Install Python from [python.org](https://python.org)
- **Permission denied**: Run build scripts as administrator
- **PyInstaller fails**: Try `pip install --upgrade pyinstaller`

### Runtime Issues
- **"Access denied"**: Run the exe as administrator
- **Operations fail**: Some optimizations may require specific Windows versions
- **Antivirus blocks**: Add exception for the exe file

```
windows_optimizer/
├── windows_optimizer.py    # Main Python script
├── security_scanner.py     # Standalone security scanner
├── build_exe.bat          # Batch build script
├── run_security_scan.bat  # Security scanner batch file
├── build_exe.ps1          # PowerShell build script
├── requirements.txt       # Python dependencies
├── README.md             # This file
└── dist/                 # Generated executable (after build)
    └── windows_optimizer.exe
```

## Disclaimer
⚠️ **Use at your own risk.** While a restore point is created automatically, it's always recommended to:
- Backup important data before running optimization tools
- Test on a non-critical system first
- Review the source code to understand what changes are made

## License
This tool is provided as-is for educational and personal use.
