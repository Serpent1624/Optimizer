#!/usr/bin/env python3
"""
Windows Security Scanner
A focused security scanning tool that integrates with your Windows Optimizer
"""

import subprocess
import sys
import platform
import os

def is_admin():
    """Check if the script is running with administrator privileges."""
    try:
        return subprocess.run(['net', 'session'], capture_output=True, text=True).returncode == 0
    except:
        return False

def check_malwarebytes():
    """Check if Malwarebytes is installed."""
    try:
        result = subprocess.run([
            'powershell', '-Command',
            'Get-ItemProperty HKLM:\\Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\* | Where-Object { $_.DisplayName -like "*Malwarebytes*" }'
        ], capture_output=True, text=True)

        if result.returncode == 0 and result.stdout.strip():
            print("✅ Malwarebytes is installed")
            return True
        else:
            print("❌ Malwarebytes is not installed")
            return False
    except Exception as e:
        print(f"Error checking Malwarebytes: {e}")
        return False

def run_windows_defender_scan():
    """Run Windows Defender full scan."""
    try:
        print("🛡️ Starting Windows Defender full scan...")
        result = subprocess.run([
            'powershell', '-Command',
            'Start-MpScan -ScanType FullScan'
        ], capture_output=True, text=True)

        if result.returncode == 0:
            print("✅ Windows Defender scan started successfully")
            print("📊 Check progress in Windows Security > Virus & threat protection")
        else:
            print("❌ Failed to start Windows Defender scan")
    except Exception as e:
        print(f"Error: {e}")

def get_security_recommendations():
    """Provide security recommendations."""
    print("\n🔒 SECURITY RECOMMENDATIONS:")
    print("=" * 40)
    print("1. 🛡️ Keep Windows Defender enabled and updated")
    print("2. 🦠 Install Malwarebytes for additional protection")
    print("3. 🔄 Run full scans weekly")
    print("4. 📅 Keep Windows updated")
    print("5. 🔑 Use strong, unique passwords")
    print("6. 📧 Be cautious with email attachments")
    print("7. 🌐 Avoid suspicious downloads")
    print("8. 🔒 Use firewall and antivirus software")
    print("9. 💾 Backup important data regularly")
    print("10. 🚫 Don't run unknown executables")

def main():
    """Main security scanner function."""
    print("🔍 WINDOWS SECURITY SCANNER")
    print("=" * 30)

    if platform.system() != 'Windows':
        print("❌ This tool is designed for Windows only.")
        sys.exit(1)

    if not is_admin():
        print("⚠️  Administrator privileges recommended for full functionality.")
        print("Some security checks may be limited.\n")

    print("1. Checking Malwarebytes installation...")
    malwarebytes_installed = check_malwarebytes()

    print("\n2. Checking Windows Defender status...")
    try:
        result = subprocess.run([
            'powershell', '-Command',
            'Get-MpComputerStatus | Select-Object AntivirusEnabled, RealTimeProtectionEnabled'
        ], capture_output=True, text=True)
        print(result.stdout)
    except Exception as e:
        print(f"Error checking Windows Defender: {e}")

    print("\n3. Security Options:")
    print("   A) Run Windows Defender Full Scan")
    print("   B) Get Malwarebytes Installation Guide")
    print("   C) View Security Recommendations")
    print("   D) Exit")

    while True:
        choice = input("\nChoose an option (A/B/C/D): ").upper()

        if choice == 'A':
            run_windows_defender_scan()
        elif choice == 'B':
            print("\n📥 MALWAREBYTES INSTALLATION GUIDE:")
            print("1. Visit: https://www.malwarebytes.com/download")
            print("2. Click 'Free Download'")
            print("3. Run installer as administrator")
            print("4. Follow installation wizard")
            print("5. Open Malwarebytes and run scan")
        elif choice == 'C':
            get_security_recommendations()
        elif choice == 'D':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please select A, B, C, or D.")

if __name__ == "__main__":
    main()
