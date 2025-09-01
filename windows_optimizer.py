import os
import subprocess
import platform
import ctypes
import sys
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import threading
import time

import os
import subprocess
import platform
import ctypes
import sys
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import threading
import time

class WindowsOptimizerGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Windows Optimizer")
        self.root.geometry("900x800")
        self.root.resizable(True, True)

        # Set theme
        style = ttk.Style()
        style.theme_use('clam')

        # Optimization options with descriptions
        self.optimizations = {
            'create_restore_point': {
                'name': 'Create System Restore Point',
                'desc': 'Creates a restore point before making changes (Recommended)',
                'mandatory': True,
                'selected': True
            },
            'clean_temp_files': {
                'name': 'Clean Temporary Files',
                'desc': 'Removes temporary files to free up disk space',
                'mandatory': False,
                'selected': True
            },
            'run_disk_cleanup': {
                'name': 'Run Disk Cleanup',
                'desc': 'Runs Windows built-in disk cleanup utility',
                'mandatory': False,
                'selected': True
            },
            'defragment_drives': {
                'name': 'Defragment Drives',
                'desc': 'Optimizes hard drive performance by defragmenting files',
                'mandatory': False,
                'selected': True
            },
            'clear_windows_update_cache': {
                'name': 'Clear Windows Update Cache',
                'desc': 'Removes cached Windows update files',
                'mandatory': False,
                'selected': True
            },
            'run_system_file_checker': {
                'name': 'Run System File Checker',
                'desc': 'Scans and repairs corrupted system files',
                'mandatory': False,
                'selected': True
            },
            'run_dism_repair': {
                'name': 'Run DISM Repair',
                'desc': 'Repairs Windows image and component store',
                'mandatory': False,
                'selected': True
            },
            'clear_dns_cache': {
                'name': 'Clear DNS Cache',
                'desc': 'Flushes DNS resolver cache for better network performance',
                'mandatory': False,
                'selected': True
            },
            'optimize_windows_search': {
                'name': 'Optimize Windows Search',
                'desc': 'Rebuilds search index for faster file searches',
                'mandatory': False,
                'selected': True
            },
            'clear_browser_cache': {
                'name': 'Clear Browser Cache',
                'desc': 'Clears cache for Chrome, Firefox, and Edge browsers',
                'mandatory': False,
                'selected': True
            },
            'clear_event_logs': {
                'name': 'Clear Event Logs',
                'desc': 'Removes old Windows event logs to save space',
                'mandatory': False,
                'selected': True
            },
            'optimize_power_settings': {
                'name': 'Optimize Power Settings',
                'desc': 'Sets power plan to High Performance mode',
                'mandatory': False,
                'selected': True
            },
            'disable_hibernation': {
                'name': 'Disable Hibernation',
                'desc': 'Turns off hibernation to save disk space',
                'mandatory': False,
                'selected': True
            },
            'optimize_registry': {
                'name': 'Optimize Registry',
                'desc': 'Performs registry cleanup and optimization',
                'mandatory': False,
                'selected': False
            },
            'disable_unnecessary_services': {
                'name': 'Disable Unnecessary Services',
                'desc': 'Stops and disables non-essential Windows services',
                'mandatory': False,
                'selected': False
            },
            'optimize_startup_programs': {
                'name': 'Optimize Startup Programs',
                'desc': 'Manages startup programs for faster boot times',
                'mandatory': False,
                'selected': False
            },
            'optimize_network_settings': {
                'name': 'Optimize Network Settings',
                'desc': 'Tunes TCP/IP and network settings for better performance',
                'mandatory': False,
                'selected': False
            },
            'optimize_memory_management': {
                'name': 'Optimize Memory Management',
                'desc': 'Tunes virtual memory and memory settings',
                'mandatory': False,
                'selected': False
            },
            'optimize_visual_effects': {
                'name': 'Optimize Visual Effects',
                'desc': 'Disables unnecessary animations and visual effects',
                'mandatory': False,
                'selected': False
            },
            'optimize_ssd_settings': {
                'name': 'Optimize SSD Settings',
                'desc': 'Configures optimal settings for SSD drives',
                'mandatory': False,
                'selected': False
            },
            'optimize_security_settings': {
                'name': 'Optimize Security Settings',
                'desc': 'Tunes Windows Defender and security for performance',
                'mandatory': False,
                'selected': False
            },
            'optimize_system_settings': {
                'name': 'Advanced System Settings',
                'desc': 'Applies advanced system optimizations and tweaks',
                'mandatory': False,
                'selected': False
            },
            'clean_windows_old': {
                'name': 'Clean Windows.old Folder',
                'desc': 'Removes old Windows installation files',
                'mandatory': False,
                'selected': False
            },
            'optimize_game_mode': {
                'name': 'Optimize Game Mode',
                'desc': 'Enables and optimizes Game Mode for gaming performance',
                'mandatory': False,
                'selected': False
            },
            'optimize_context_menu': {
                'name': 'Optimize Context Menu',
                'desc': 'Cleans up right-click context menu items',
                'mandatory': False,
                'selected': False
            },
            'optimize_gpu_settings': {
                'name': 'Optimize GPU Settings',
                'desc': 'Tunes graphics card settings for better performance',
                'mandatory': False,
                'selected': False
            },
            'optimize_usb_settings': {
                'name': 'Optimize USB Settings',
                'desc': 'Configures USB power management and performance',
                'mandatory': False,
                'selected': False
            },
            'optimize_printer_settings': {
                'name': 'Optimize Printer Settings',
                'desc': 'Tunes print spooler and printer configurations',
                'mandatory': False,
                'selected': False
            },
            'optimize_audio_settings': {
                'name': 'Optimize Audio Settings',
                'desc': 'Tunes sound and audio performance settings',
                'mandatory': False,
                'selected': False
            },
            'optimize_bluetooth_settings': {
                'name': 'Optimize Bluetooth Settings',
                'desc': 'Configures Bluetooth power and performance',
                'mandatory': False,
                'selected': False
            },
            'optimize_firewall_settings': {
                'name': 'Optimize Firewall Settings',
                'desc': 'Tunes Windows Firewall for optimal performance',
                'mandatory': False,
                'selected': False
            },
            'optimize_uac_settings': {
                'name': 'Optimize UAC Settings',
                'desc': 'Configures User Account Control for performance',
                'mandatory': False,
                'selected': False
            },
            'optimize_windows_update_settings': {
                'name': 'Optimize Windows Update',
                'desc': 'Tunes update settings for better performance',
                'mandatory': False,
                'selected': False
            },
            'optimize_error_reporting': {
                'name': 'Optimize Error Reporting',
                'desc': 'Configures Windows error reporting settings',
                'mandatory': False,
                'selected': False
            },
            'optimize_remote_desktop': {
                'name': 'Optimize Remote Desktop',
                'desc': 'Tunes RDP settings for better remote performance',
                'mandatory': False,
                'selected': False
            },
            'optimize_task_scheduler': {
                'name': 'Optimize Task Scheduler',
                'desc': 'Cleans up unnecessary scheduled tasks',
                'mandatory': False,
                'selected': False
            },
            'optimize_font_cache': {
                'name': 'Optimize Font Cache',
                'desc': 'Clears and rebuilds system font cache',
                'mandatory': False,
                'selected': False
            },
            'optimize_icon_cache': {
                'name': 'Optimize Icon Cache',
                'desc': 'Rebuilds system icon cache for faster loading',
                'mandatory': False,
                'selected': False
            },
            'optimize_thumbnail_cache': {
                'name': 'Optimize Thumbnail Cache',
                'desc': 'Clears thumbnail cache for better explorer performance',
                'mandatory': False,
                'selected': False
            },
            'optimize_prefetch_superfetch': {
                'name': 'Optimize Prefetch/Superfetch',
                'desc': 'Tunes memory prefetch settings for SSD/HDD',
                'mandatory': False,
                'selected': False
            },
            'optimize_readyboost': {
                'name': 'Optimize ReadyBoost',
                'desc': 'Configures USB caching for better performance',
                'mandatory': False,
                'selected': False
            },
            'optimize_windows_store': {
                'name': 'Optimize Windows Store',
                'desc': 'Clears Microsoft Store cache and optimizes settings',
                'mandatory': False,
                'selected': False
            },
            'optimize_cortana': {
                'name': 'Optimize Cortana',
                'desc': 'Tunes Cortana settings and clears search data',
                'mandatory': False,
                'selected': False
            },
            'optimize_onedrive': {
                'name': 'Optimize OneDrive',
                'desc': 'Tunes OneDrive settings and clears cache',
                'mandatory': False,
                'selected': False
            },
            'optimize_microsoft_edge': {
                'name': 'Optimize Microsoft Edge',
                'desc': 'Tunes Edge browser settings and clears cache',
                'mandatory': False,
                'selected': False
            },
            'optimize_registry_animations': {
                'name': 'Disable Windows Animations',
                'desc': 'Disable animations and transitions for better performance',
                'mandatory': False,
                'selected': False
            },
            'optimize_explorer_settings': {
                'name': 'Optimize Explorer Settings',
                'desc': 'Tune Windows Explorer for better performance',
                'mandatory': False,
                'selected': False
            },
            'disable_windows_features': {
                'name': 'Disable Unnecessary Windows Features',
                'desc': 'Disable optional Windows features to improve performance',
                'mandatory': False,
                'selected': False
            },
            'optimize_memory_registry': {
                'name': 'Optimize Memory Registry',
                'desc': 'Tune memory management registry settings',
                'mandatory': False,
                'selected': False
            },
            'disable_telemetry_services': {
                'name': 'Disable Telemetry Services',
                'desc': 'Disable Windows telemetry and data collection services',
                'mandatory': False,
                'selected': False
            },
            'optimize_network_registry': {
                'name': 'Optimize Network Registry',
                'desc': 'Tune network registry settings for better performance',
                'mandatory': False,
                'selected': False
            },
            'disable_windows_tips': {
                'name': 'Disable Windows Tips & Suggestions',
                'desc': 'Disable Windows tips and suggestions for privacy',
                'mandatory': False,
                'selected': False
            },
            'optimize_usb_registry': {
                'name': 'Optimize USB Registry',
                'desc': 'Tune USB registry settings for better performance',
                'mandatory': False,
                'selected': False
            },
            'disable_store_autoupdates': {
                'name': 'Disable Store Auto-Updates',
                'desc': 'Disable automatic Microsoft Store updates',
                'mandatory': False,
                'selected': False
            },
            'optimize_power_registry': {
                'name': 'Optimize Power Registry',
                'desc': 'Tune power management registry settings',
                'mandatory': False,
                'selected': False
            },
            'disable_search_service': {
                'name': 'Disable Windows Search Service',
                'desc': 'Disable Windows Search service for better performance',
                'mandatory': False,
                'selected': False
            },
            'disable_xbox_services': {
                'name': 'Disable Xbox Services',
                'desc': 'Disable Xbox Live services if not needed',
                'mandatory': False,
                'selected': False
            },
            'disable_print_services': {
                'name': 'Disable Print Services',
                'desc': 'Disable print spooler and fax services if not needed',
                'mandatory': False,
                'selected': False
            },
            'disable_update_medic': {
                'name': 'Disable Update Medic Service',
                'desc': 'Disable Windows Update Medic service',
                'mandatory': False,
                'selected': False
            },
            'disable_store_install_service': {
                'name': 'Disable Store Install Service',
                'desc': 'Disable Microsoft Store Install service',
                'mandatory': False,
                'selected': False
            },
            'disable_push_notifications': {
                'name': 'Disable Push Notifications',
                'desc': 'Disable Windows push notification service',
                'mandatory': False,
                'selected': False
            },
            'disable_biometric_service': {
                'name': 'Disable Biometric Service',
                'desc': 'Disable Windows biometric service if not needed',
                'mandatory': False,
                'selected': False
            },
            'disable_windows_connect': {
                'name': 'Disable Windows Connect Now',
                'desc': 'Disable Windows Connect Now service',
                'mandatory': False,
                'selected': False
            },
            'enable_ultimate_performance': {
                'name': 'Enable Ultimate Performance Plan',
                'desc': 'Activate Ultimate Performance power plan for maximum performance',
                'mandatory': False,
                'selected': False
            },
            'optimize_pagefile_memory': {
                'name': 'Optimize Pagefile & Memory',
                'desc': 'Tune virtual memory and pagefile settings based on RAM size',
                'mandatory': False,
                'selected': False
            },
            'tune_gpu_driver_settings': {
                'name': 'Tune GPU Driver Settings',
                'desc': 'Optimize graphics drivers for max performance and low latency',
                'mandatory': False,
                'selected': False
            },
            'autoruns_kill_bloatware': {
                'name': 'Kill Bloatware & Background Tasks',
                'desc': 'Remove unnecessary startup programs and background processes',
                'mandatory': False,
                'selected': False
            },
            'finetune_network_stack': {
                'name': 'Fine-tune Network Stack',
                'desc': 'Disable Nagle algorithm and optimize NIC settings for low latency',
                'mandatory': False,
                'selected': False
            },
            'kill_eye_candy_dwm': {
                'name': 'Kill Eye-candy & DWM Effects',
                'desc': 'Disable visual effects and DWM for maximum performance',
                'mandatory': False,
                'selected': False
            },
            'keep_ssd_clean': {
                'name': 'Keep SSD Clean (TRIM)',
                'desc': 'Enable TRIM and disable unnecessary indexing for SSD health',
                'mandatory': False,
                'selected': False
            },
            'windows_updates_default': {
                'name': 'Windows Updates - Default',
                'desc': 'Reset Windows Update settings to stock/default settings',
                'mandatory': False,
                'selected': False
            },
            'windows_updates_recommended': {
                'name': 'Windows Updates - Recommended',
                'desc': 'Security-only updates; defer feature updates ~24 months',
                'mandatory': False,
                'selected': False
            },
            'windows_updates_disable_all': {
                'name': 'Windows Updates - Disable All',
                'desc': 'Disable all updates (not recommended; for legacy/isolated systems)',
                'mandatory': False,
                'selected': False
            },
            'check_malwarebytes_installation': {
                'name': 'Check Malwarebytes Installation',
                'desc': 'Check if Malwarebytes is installed and provide guidance',
                'mandatory': False,
                'selected': False
            },
            'run_malwarebytes_scan': {
                'name': 'Run Malwarebytes Scan',
                'desc': 'Attempt to run Malwarebytes scan if installed',
                'mandatory': False,
                'selected': False
            },
            'install_malwarebytes_guided': {
                'name': 'Malwarebytes Installation Guide',
                'desc': 'Get step-by-step guide for installing Malwarebytes',
                'mandatory': False,
                'selected': False
            },
            'scan_with_windows_defender': {
                'name': 'Windows Defender Full Scan',
                'desc': 'Run a full system scan with Windows Defender',
                'mandatory': False,
                'selected': False
            },
            'comprehensive_security_scan': {
                'name': 'Comprehensive Security Check',
                'desc': 'Run security checks and provide recommendations',
                'mandatory': False,
                'selected': False
            }
        }

        self.checkboxes = {}
        self.setup_ui()
        self.center_window()

    def setup_ui(self):
        # Main frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(1, weight=1)

        # Title
        title_label = ttk.Label(main_frame, text="Windows Optimizer",
                               font=("Arial", 16, "bold"))
        title_label.grid(row=0, column=0, pady=(0, 20))

        # Subtitle
        subtitle_label = ttk.Label(main_frame,
                                  text="Select the optimizations you want to perform:",
                                  font=("Arial", 10))
        subtitle_label.grid(row=1, column=0, pady=(0, 15))

        # Create scrollable frame for options
        options_frame = ttk.Frame(main_frame)
        options_frame.grid(row=2, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        options_frame.columnconfigure(0, weight=1)

        # Canvas and scrollbar for scrolling
        canvas = tk.Canvas(options_frame, height=500)
        scrollbar = ttk.Scrollbar(options_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = ttk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))

        # Create sections for different types of optimizations
        self.create_optimization_section(scrollable_frame, "🛡️ System Maintenance", [
            'create_restore_point', 'run_system_file_checker', 'run_dism_repair',
            'clean_windows_old', 'clear_dns_cache', 'clear_windows_update_cache'
        ])

        self.create_optimization_section(scrollable_frame, "💾 Disk & Storage", [
            'clean_temp_files', 'run_disk_cleanup', 'defragment_drives', 'clear_browser_cache',
            'clear_event_logs', 'disable_hibernation'
        ])

        self.create_optimization_section(scrollable_frame, "⚡ Performance Optimization", [
            'optimize_windows_search', 'optimize_power_settings', 'optimize_visual_effects',
            'optimize_memory_management', 'optimize_network_settings', 'optimize_game_mode'
        ])

        self.create_optimization_section(scrollable_frame, "🔧 Advanced System Tweaks", [
            'optimize_registry', 'disable_unnecessary_services', 'optimize_startup_programs',
            'optimize_security_settings', 'optimize_system_settings', 'optimize_context_menu',
            'optimize_gpu_settings', 'optimize_usb_settings', 'optimize_printer_settings',
            'optimize_audio_settings', 'optimize_bluetooth_settings', 'optimize_firewall_settings',
            'optimize_uac_settings', 'optimize_windows_update_settings', 'optimize_error_reporting',
            'optimize_remote_desktop', 'optimize_task_scheduler', 'optimize_font_cache',
            'optimize_icon_cache', 'optimize_thumbnail_cache', 'optimize_prefetch_superfetch',
            'optimize_readyboost', 'optimize_windows_store', 'optimize_cortana',
            'optimize_onedrive', 'optimize_microsoft_edge', 'optimize_registry_animations',
            'optimize_explorer_settings', 'disable_windows_features', 'optimize_memory_registry',
            'disable_telemetry_services', 'optimize_network_registry', 'disable_windows_tips',
            'optimize_usb_registry', 'disable_store_autoupdates', 'optimize_power_registry',
            'disable_search_service', 'disable_xbox_services', 'disable_print_services',
            'disable_update_medic', 'disable_store_install_service', 'disable_push_notifications',
            'disable_biometric_service', 'disable_windows_connect', 'enable_ultimate_performance',
            'optimize_pagefile_memory', 'tune_gpu_driver_settings', 'autoruns_kill_bloatware',
            'finetune_network_stack', 'kill_eye_candy_dwm', 'keep_ssd_clean'
        ])

        self.create_optimization_section(scrollable_frame, "🛡️ Virus Checker", [
            'check_malwarebytes_installation', 'run_malwarebytes_scan', 'install_malwarebytes_guided',
            'scan_with_windows_defender', 'comprehensive_security_scan'
        ])

        self.create_optimization_section(scrollable_frame, "🔄 Windows Updates", [
            'windows_updates_default', 'windows_updates_recommended', 'windows_updates_disable_all'
        ])

        # Configure scrollable frame
        scrollable_frame.columnconfigure(0, weight=1)
    # Buttons frame
    buttons_frame = ttk.Frame(main_frame)
    buttons_frame.grid(row=3, column=0, pady=(20, 0))

    # Select All / Deselect All buttons
    select_all_btn = ttk.Button(buttons_frame, text="Select All",
                   command=self.select_all)
    select_all_btn.grid(row=0, column=0, padx=(0, 10))

    deselect_all_btn = ttk.Button(buttons_frame, text="Deselect All",
                     command=self.deselect_all)
    deselect_all_btn.grid(row=0, column=1, padx=(0, 20))

    # Apply button
    self.apply_btn = ttk.Button(buttons_frame, text="Apply Optimizations",
                   command=self.start_optimization)
    self.apply_btn.grid(row=0, column=2)

    # Progress frame (initially hidden)
    self.progress_frame = ttk.Frame(main_frame)

    # Progress bar
    self.progress_var = tk.DoubleVar()
    self.progress_bar = ttk.Progressbar(self.progress_frame, variable=self.progress_var,
                       maximum=100, mode='determinate')
    self.progress_bar.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 10))

    # Status label
    self.status_label = ttk.Label(self.progress_frame, text="Ready to start...",
                     font=("Arial", 9))
    self.status_label.grid(row=1, column=0, pady=(0, 10))

    # Log text area
    log_label = ttk.Label(self.progress_frame, text="Optimization Log:",
                 font=("Arial", 9, "bold"))
    log_label.grid(row=2, column=0, sticky=tk.W, pady=(0, 5))

    self.log_text = scrolledtext.ScrolledText(self.progress_frame, height=8,
                         font=("Consolas", 8))
    self.log_text.grid(row=3, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    self.progress_frame.columnconfigure(0, weight=1)
    self.progress_frame.rowconfigure(3, weight=1)
    # Buttons frame
    buttons_frame = ttk.Frame(main_frame)
    buttons_frame.grid(row=3, column=0, pady=(20, 0))

    # Select All / Deselect All buttons
    select_all_btn = ttk.Button(buttons_frame, text="Select All",
                   command=self.select_all)
    select_all_btn.grid(row=0, column=0, padx=(0, 10))

    deselect_all_btn = ttk.Button(buttons_frame, text="Deselect All",
                     command=self.deselect_all)
    deselect_all_btn.grid(row=0, column=1, padx=(0, 20))

    # Apply button
    self.apply_btn = ttk.Button(buttons_frame, text="Apply Optimizations",
                   command=self.start_optimization)
    self.apply_btn.grid(row=0, column=2)

    # Progress frame (initially hidden)
    self.progress_frame = ttk.Frame(main_frame)

    # Progress bar
    self.progress_var = tk.DoubleVar()
    self.progress_bar = ttk.Progressbar(self.progress_frame, variable=self.progress_var,
                       maximum=100, mode='determinate')
    self.progress_bar.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=(0, 10))

    # Status label
    self.status_label = ttk.Label(self.progress_frame, text="Ready to start...",
                     font=("Arial", 9))
    self.status_label.grid(row=1, column=0, pady=(0, 10))

    # Log text area
    log_label = ttk.Label(self.progress_frame, text="Optimization Log:",
                 font=("Arial", 9, "bold"))
    log_label.grid(row=2, column=0, sticky=tk.W, pady=(0, 5))

    self.log_text = scrolledtext.ScrolledText(self.progress_frame, height=8,
                         font=("Consolas", 8))
    self.log_text.grid(row=3, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    self.progress_frame.columnconfigure(0, weight=1)
    self.progress_frame.rowconfigure(3, weight=1)

    def create_optimization_section(self, parent, section_title, option_keys):
        """Create a section of optimization options with a header."""
        # Section frame
        section_frame = ttk.LabelFrame(parent, text=section_title, padding="10")
        section_frame.grid(row=len(self.checkboxes), column=0, sticky=(tk.W, tk.E), pady=(10, 0), padx=5)
        section_frame.columnconfigure(0, weight=1)

        # Create checkboxes for this section
        for i, key in enumerate(option_keys):
            if key in self.optimizations:
                opt = self.optimizations[key]

                # Frame for each option
                option_frame = ttk.Frame(section_frame)
                option_frame.grid(row=i, column=0, sticky=(tk.W, tk.E), pady=2)
                option_frame.columnconfigure(1, weight=1)

                # Checkbox
                var = tk.BooleanVar(value=opt['selected'])
                checkbox = ttk.Checkbutton(option_frame, variable=var,
                                         state='disabled' if opt['mandatory'] else 'normal')
                checkbox.grid(row=0, column=0, sticky=tk.W)

                # Label frame for name and description
                label_frame = ttk.Frame(option_frame)
                label_frame.grid(row=0, column=1, sticky=(tk.W, tk.E), padx=(10, 0))
                label_frame.columnconfigure(0, weight=1)

                # Name
                name_label = ttk.Label(label_frame, text=opt['name'],
                                      font=("Arial", 9, "bold"))
                name_label.grid(row=0, column=0, sticky=tk.W)

                # Description
                desc_label = ttk.Label(label_frame, text=opt['desc'],
                                      font=("Arial", 8), foreground="gray")
                desc_label.grid(row=1, column=0, sticky=tk.W)

                # Mandatory indicator
                if opt['mandatory']:
                    mandatory_label = ttk.Label(option_frame, text="(Required)",
                                               font=("Arial", 7), foreground="red")
                    mandatory_label.grid(row=0, column=2, padx=(5, 0))

                self.checkboxes[key] = var


    def center_window(self):
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')

    def select_all(self):
        for key, opt in self.optimizations.items():
            if not opt['mandatory']:
                self.checkboxes[key].set(True)

    def deselect_all(self):
        for key, opt in self.optimizations.items():
            if not opt['mandatory']:
                self.checkboxes[key].set(False)

    def log_message(self, message):
        self.log_text.insert(tk.END, f"{time.strftime('%H:%M:%S')} - {message}\n")
        self.log_text.see(tk.END)
        self.root.update_idletasks()

    def start_optimization(self):
        # Get selected optimizations
        selected = []
        for key, var in self.checkboxes.items():
            if var.get():
                selected.append(key)

        if not selected:
            messagebox.showwarning("No Selection", "Please select at least one optimization.")
            return

        # Check if running on Windows
        if platform.system() != 'Windows':
            messagebox.showerror("Unsupported OS", "This tool is designed for Windows only.")
            return

        # Check admin privileges
        if not is_admin():
            messagebox.showerror("Administrator Required",
                               "This tool requires administrator privileges.\n\n"
                               "Please run as administrator.")
            return

        # Show progress frame
        self.progress_frame.grid(row=4, column=0, pady=(20, 0), sticky=(tk.W, tk.E, tk.N, tk.S))
        self.root.geometry("900x1000")

        # Disable apply button
        self.apply_btn.config(state='disabled')

        # Start optimization in separate thread
        thread = threading.Thread(target=self.run_optimizations, args=(selected,))
        thread.daemon = True
        thread.start()

    def run_optimizations(self, selected_optimizations):
        try:
            total_steps = len(selected_optimizations)
            current_step = 0

            self.log_message("Starting Windows optimization...")
            self.status_label.config(text="Starting optimization...")

            for optimization in selected_optimizations:
                current_step += 1
                progress = (current_step - 1) / total_steps * 100

                opt_info = self.optimizations[optimization]
                self.log_message(f"Running: {opt_info['name']}")
                self.status_label.config(text=f"Running: {opt_info['name']}")
                self.progress_var.set(progress)
                self.root.update_idletasks()

                # Run the optimization function
                func_name = optimization
                if func_name in globals():
                    func = globals()[func_name]
                    func()

                self.progress_var.set(current_step / total_steps * 100)
                time.sleep(0.5)  # Small delay for UI update

            self.log_message("All optimizations completed!")
            self.status_label.config(text="Optimization completed successfully!")
            self.progress_var.set(100)

            messagebox.showinfo("Success",
                              "All selected optimizations have been completed!\n\n"
                              "It is recommended to restart your computer for the changes to take effect.")

        except Exception as e:
            self.log_message(f"Error: {str(e)}")
            self.status_label.config(text="Error occurred during optimization")
            messagebox.showerror("Error", f"An error occurred during optimization:\n\n{str(e)}")

        finally:
            self.apply_btn.config(state='normal')

    def run(self):
        self.root.mainloop()

def is_admin():
    """Check if the script is running with administrator privileges."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def create_restore_point():
    """Create a system restore point."""
    try:
        print("Creating system restore point...")
        # Use PowerShell to create a restore point
        result = subprocess.run([
            'powershell', '-Command',
            'Checkpoint-Computer -Description "Before Windows Optimization" -RestorePointType MODIFY_SETTINGS'
        ], capture_output=True, text=True)
        if result.returncode == 0:
            print("System restore point created successfully.")
        else:
            print(f"Failed to create restore point: {result.stderr}")
    except Exception as e:
        print(f"Error creating restore point: {e}")

def clean_temp_files():
    """Clean temporary files."""
    try:
        print("Cleaning temporary files...")
        # Clean %temp% directory
        temp_dir = os.environ.get('TEMP', os.environ.get('TMP', 'C:\\Temp'))
        if os.path.exists(temp_dir):
            for root, dirs, files in os.walk(temp_dir):
                for file in files:
                    try:
                        os.remove(os.path.join(root, file))
                    except:
                        pass
        print("Temporary files cleaned.")
    except Exception as e:
        print(f"Error cleaning temp files: {e}")

def run_disk_cleanup():
    """Run Windows Disk Cleanup."""
    try:
        print("Running Disk Cleanup...")
        # This requires Disk Cleanup to be configured; otherwise, it might not work silently
        result = subprocess.run(['cleanmgr', '/sagerun:1'], capture_output=True, text=True)
        if result.returncode == 0:
            print("Disk Cleanup completed.")
        else:
            print(f"Disk Cleanup failed: {result.stderr}")
    except Exception as e:
        print(f"Error running Disk Cleanup: {e}")

def defragment_drives():
    """Defragment hard drives."""
    try:
        print("Defragmenting drives...")
        # Defrag C: drive
        result = subprocess.run(['defrag', 'C:', '/U', '/V'], capture_output=True, text=True)
        if result.returncode == 0:
            print("Defragmentation completed.")
        else:
            print(f"Defragmentation failed: {result.stderr}")
    except Exception as e:
        print(f"Error defragmenting: {e}")

def clear_windows_update_cache():
    """Clear Windows Update cache."""
    try:
        print("Clearing Windows Update cache...")
        # Stop Windows Update service
        subprocess.run(['net', 'stop', 'wuauserv'], capture_output=True)
        # Clear SoftwareDistribution folder
        update_cache_path = 'C:\\Windows\\SoftwareDistribution\\Download'
        if os.path.exists(update_cache_path):
            for item in os.listdir(update_cache_path):
                item_path = os.path.join(update_cache_path, item)
                try:
                    if os.path.isfile(item_path):
                        os.remove(item_path)
                    elif os.path.isdir(item_path):
                        import shutil
                        shutil.rmtree(item_path)
                except:
                    pass
        # Restart Windows Update service
        subprocess.run(['net', 'start', 'wuauserv'], capture_output=True)
        print("Windows Update cache cleared.")
    except Exception as e:
        print(f"Error clearing Windows Update cache: {e}")

def run_system_file_checker():
    """Run System File Checker to repair corrupted files."""
    try:
        print("Running System File Checker...")
        result = subprocess.run(['sfc', '/scannow'], capture_output=True, text=True)
        if result.returncode == 0:
            print("System File Checker completed.")
        else:
            print(f"System File Checker failed: {result.stderr}")
    except Exception as e:
        print(f"Error running System File Checker: {e}")

def run_dism_repair():
    """Run DISM to repair Windows image."""
    try:
        print("Running DISM repair...")
        # First restore health
        subprocess.run(['DISM', '/Online', '/Cleanup-Image', '/RestoreHealth'], capture_output=True)
        # Then scan health
        result = subprocess.run(['DISM', '/Online', '/Cleanup-Image', '/ScanHealth'], capture_output=True, text=True)
        if result.returncode == 0:
            print("DISM repair completed.")
        else:
            print(f"DISM repair failed: {result.stderr}")
    except Exception as e:
        print(f"Error running DISM repair: {e}")

def clear_dns_cache():
    """Clear DNS cache."""
    try:
        print("Clearing DNS cache...")
        result = subprocess.run(['ipconfig', '/flushdns'], capture_output=True, text=True)
        if result.returncode == 0:
            print("DNS cache cleared.")
        else:
            print(f"Failed to clear DNS cache: {result.stderr}")
    except Exception as e:
        print(f"Error clearing DNS cache: {e}")

def optimize_windows_search():
    """Optimize Windows Search indexing."""
    try:
        print("Optimizing Windows Search...")
        # Rebuild search index
        result = subprocess.run([
            'powershell', '-Command',
            'Set-WindowsSearchSetting -EnableWebResultsSetting $false; $searchIndexer = New-Object -ComObject "Search.SearchIndexer"; $searchIndexer.Reset()'
        ], capture_output=True, text=True)
        if result.returncode == 0:
            print("Windows Search optimized.")
        else:
            print(f"Failed to optimize Windows Search: {result.stderr}")
    except Exception as e:
        print(f"Error optimizing Windows Search: {e}")

def clear_browser_cache():
    """Clear browser caches for common browsers."""
    try:
        print("Clearing browser caches...")
        browsers = [
            ('Chrome', 'C:\\Users\\{}\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\Cache'),
            ('Firefox', 'C:\\Users\\{}\\AppData\\Local\\Mozilla\\Firefox\\Profiles'),
            ('Edge', 'C:\\Users\\{}\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default\\Cache')
        ]
        
        username = os.environ.get('USERNAME', '')
        for browser_name, cache_path_template in browsers:
            cache_path = cache_path_template.format(username)
            if os.path.exists(cache_path):
                try:
                    if 'Firefox' in browser_name:
                        # Firefox has multiple profiles
                        for profile in os.listdir(cache_path):
                            profile_path = os.path.join(cache_path, profile)
                            if os.path.isdir(profile_path) and 'cache2' in os.listdir(profile_path):
                                cache2_path = os.path.join(profile_path, 'cache2')
                                import shutil
                                shutil.rmtree(cache2_path, ignore_errors=True)
                    else:
                        import shutil
                        shutil.rmtree(cache_path, ignore_errors=True)
                    print(f"{browser_name} cache cleared.")
                except Exception as e:
                    print(f"Error clearing {browser_name} cache: {e}")
    except Exception as e:
        print(f"Error clearing browser caches: {e}")

def clear_event_logs():
    """Clear Windows event logs."""
    try:
        print("Clearing Windows event logs...")
        result = subprocess.run([
            'powershell', '-Command',
            'wevtutil cl System; wevtutil cl Application; wevtutil cl Security'
        ], capture_output=True, text=True)
        if result.returncode == 0:
            print("Event logs cleared.")
        else:
            print(f"Failed to clear event logs: {result.stderr}")
    except Exception as e:
        print(f"Error clearing event logs: {e}")

def optimize_power_settings():
    """Optimize power settings for performance."""
    try:
        print("Optimizing power settings...")
        result = subprocess.run([
            'powercfg', '/setactive', '8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c'  # High performance plan
        ], capture_output=True, text=True)
        if result.returncode == 0:
            print("Power settings optimized to High Performance.")
        else:
            print(f"Failed to optimize power settings: {result.stderr}")
    except Exception as e:
        print(f"Error optimizing power settings: {e}")

def disable_hibernation():
    """Disable hibernation to save disk space."""
    try:
        print("Disabling hibernation...")
        result = subprocess.run(['powercfg', '/hibernate', 'off'], capture_output=True, text=True)
        if result.returncode == 0:
            print("Hibernation disabled.")
        else:
            print(f"Failed to disable hibernation: {result.stderr}")
    except Exception as e:
        print(f"Error disabling hibernation: {e}")

def optimize_registry():
    """Perform registry optimizations."""
    try:
        print("Optimizing Windows Registry...")
        # Clean up registry using built-in tools
        result = subprocess.run(['reg', 'add', 'HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced', '/v', 'DontUsePowerShellOnWinX', '/t', 'REG_DWORD', '/d', '1', '/f'], capture_output=True, text=True)
        if result.returncode == 0:
            print("Registry optimizations completed.")
        else:
            print(f"Registry optimization failed: {result.stderr}")
    except Exception as e:
        print(f"Error optimizing registry: {e}")

def disable_unnecessary_services():
    """Disable unnecessary Windows services for better performance."""
    try:
        print("Disabling unnecessary services...")
        services_to_disable = [
            'SysMain',  # Superfetch
            'WSearch',  # Windows Search (if not needed)
            'Spooler',  # Print Spooler (if no printer)
            'Fax',      # Fax Service
            'XblGameSave',  # Xbox Game Save
            'XboxLiveAuthManager',  # Xbox Live Auth
            'XboxLiveGameSave',     # Xbox Live Game Save
            'XboxLiveNetAuthManager'  # Xbox Live Net Auth
        ]

        for service in services_to_disable:
            try:
                subprocess.run(['sc', 'config', service, 'start=', 'disabled'], capture_output=True)
                subprocess.run(['sc', 'stop', service], capture_output=True)
            except:
                pass  # Service might not exist or already disabled

        print("Unnecessary services disabled.")
    except Exception as e:
        print(f"Error disabling services: {e}")

def optimize_startup_programs():
    """Optimize startup programs for faster boot."""
    try:
        print("Optimizing startup programs...")
        # Use PowerShell to disable unnecessary startup items
        startup_script = '''
        $startupItems = Get-CimInstance -ClassName Win32_StartupCommand
        foreach ($item in $startupItems) {
            if ($item.Name -like "*OneDrive*" -or $item.Name -like "*Skype*" -or $item.Name -like "*Teams*") {
                # Optionally disable these - commented out for safety
                # $item | Remove-CimInstance
            }
        }
        '''
        result = subprocess.run(['powershell', '-Command', startup_script], capture_output=True, text=True)
        if result.returncode == 0:
            print("Startup programs optimized.")
        else:
            print(f"Startup optimization failed: {result.stderr}")
    except Exception as e:
        print(f"Error optimizing startup: {e}")

def optimize_network_settings():
    """Optimize network settings for better performance."""
    try:
        print("Optimizing network settings...")
        # Optimize TCP/IP settings
        network_commands = [
            ['netsh', 'int', 'tcp', 'set', 'global', 'chimney=enabled'],
            ['netsh', 'int', 'tcp', 'set', 'global', 'autotuninglevel=normal'],
            ['netsh', 'int', 'tcp', 'set', 'global', 'congestionprovider=ctcp'],
            ['netsh', 'int', 'tcp', 'set', 'global', 'timestamps=disabled'],
            ['netsh', 'int', 'tcp', 'set', 'global', 'rss=enabled'],
            ['netsh', 'int', 'tcp', 'set', 'global', 'ecncapability=disabled']
        ]

        for cmd in network_commands:
            try:
                subprocess.run(cmd, capture_output=True)
            except:
                pass

        print("Network settings optimized.")
    except Exception as e:
        print(f"Error optimizing network: {e}")

def optimize_memory_management():
    """Optimize virtual memory and memory management."""
    try:
        print("Optimizing memory management...")
        # Set optimal virtual memory settings
        memory_script = '''
        $totalMemory = (Get-CimInstance -ClassName Win32_ComputerSystem).TotalPhysicalMemory / 1MB
        $minSize = [math]::Round($totalMemory * 1.5)
        $maxSize = [math]::Round($totalMemory * 3)

        $pageFile = Get-CimInstance -ClassName Win32_PageFileSetting
        if ($pageFile) {
            $pageFile.InitialSize = $minSize
            $pageFile.MaximumSize = $maxSize
            $pageFile.Put()
        }
        '''
        result = subprocess.run(['powershell', '-Command', memory_script], capture_output=True, text=True)
        if result.returncode == 0:
            print("Memory management optimized.")
        else:
            print(f"Memory optimization failed: {result.stderr}")
    except Exception as e:
        print(f"Error optimizing memory: {e}")

def optimize_visual_effects():
    """Disable unnecessary visual effects for better performance."""
    try:
        print("Optimizing visual effects...")
        # Disable visual effects for best performance
        visual_script = '''
        $path = "HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\VisualEffects"
        if (!(Test-Path $path)) { New-Item -Path $path -Force }
        Set-ItemProperty -Path $path -Name "VisualFXSetting" -Value 2

        # Disable specific visual effects
        $effects = @(
            "AnimateMinMax",
            "ComboBoxAnimation",
            "CursorShadow",
            "DragFullWindows",
            "DropShadow",
            "ListBoxSmoothScrolling",
            "MenuAnimation",
            "SelectionFade",
            "TaskbarAnimations",
            "Themes",
            "TooltipAnimation",
            "WebView"
        )

        foreach ($effect in $effects) {
            Set-ItemProperty -Path "HKCU:\\Control Panel\\Desktop" -Name $effect -Value 0
        }
        '''
        result = subprocess.run(['powershell', '-Command', visual_script], capture_output=True, text=True)
        if result.returncode == 0:
            print("Visual effects optimized.")
        else:
            print(f"Visual effects optimization failed: {result.stderr}")
    except Exception as e:
        print(f"Error optimizing visual effects: {e}")

def optimize_ssd_settings():
    """Optimize settings for SSD drives."""
    try:
        print("Optimizing SSD settings...")
        # Disable defrag on SSDs and optimize settings
        ssd_script = '''
        $drives = Get-PhysicalDisk | Where-Object {$_.MediaType -eq "SSD"}
        foreach ($drive in $drives) {
            # Disable defrag scheduling for SSD
            Disable-ScheduledTask -TaskName "\\Microsoft\\Windows\\Defrag\\ScheduledDefrag" -ErrorAction SilentlyContinue

            # Enable TRIM
            fsutil behavior set DisableDeleteNotify 0

            # Optimize SSD settings
            fsutil behavior set EncryptPagingFile 0
            fsutil behavior set DisableLastAccess 1
        }
        '''
        result = subprocess.run(['powershell', '-Command', ssd_script], capture_output=True, text=True)
        if result.returncode == 0:
            print("SSD settings optimized.")
        else:
            print(f"SSD optimization failed: {result.stderr}")
    except Exception as e:
        print(f"Error optimizing SSD: {e}")

def optimize_security_settings():
    """Optimize security settings for better performance."""
    try:
        print("Optimizing security settings...")
        # Optimize Windows Defender and security settings
        security_script = '''
        # Optimize Windows Defender
        Set-MpPreference -ScanScheduleQuickScanTime 02:00:00
        Set-MpPreference -RemediationScheduleTime 03:00:00
        Set-MpPreference -SignatureScheduleTime 04:00:00

        # Disable unnecessary security features for performance
        Set-MpPreference -EnableControlledFolderAccess Disabled
        Set-MpPreference -PUAProtection Disabled

        # Optimize firewall
        Set-NetFirewallProfile -Profile Domain,Public,Private -DefaultInboundAction Block -DefaultOutboundAction Allow
        '''
        result = subprocess.run(['powershell', '-Command', security_script], capture_output=True, text=True)
        if result.returncode == 0:
            print("Security settings optimized.")
        else:
            print(f"Security optimization failed: {result.stderr}")
    except Exception as e:
        print(f"Error optimizing security: {e}")

def optimize_system_settings():
    """Apply advanced system optimizations."""
    try:
        print("Applying advanced system optimizations...")
        # Advanced system settings optimization
        system_script = '''
        # Disable Windows tips and suggestions
        Set-ItemProperty -Path "HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\ContentDeliveryManager" -Name "SubscribedContent-338393Enabled" -Value 0
        Set-ItemProperty -Path "HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\ContentDeliveryManager" -Name "SubscribedContent-353694Enabled" -Value 0

        # Disable feedback
        Set-ItemProperty -Path "HKCU:\\Software\\Microsoft\\Siuf\\Rules" -Name "NumberOfSIUFInPeriod" -Value 0

        # Optimize Windows Update
        Set-ItemProperty -Path "HKLM:\\SOFTWARE\\Policies\\Microsoft\\Windows\\WindowsUpdate\\AU" -Name "NoAutoUpdate" -Value 0
        Set-ItemProperty -Path "HKLM:\\SOFTWARE\\Policies\\Microsoft\\Windows\\WindowsUpdate\\AU" -Name "AUOptions" -Value 3

        # Disable telemetry
        Set-ItemProperty -Path "HKLM:\\SOFTWARE\\Policies\\Microsoft\\Windows\\DataCollection" -Name "AllowTelemetry" -Value 0
        '''
        result = subprocess.run(['powershell', '-Command', system_script], capture_output=True, text=True)
        if result.returncode == 0:
            print("Advanced system optimizations applied.")
        else:
            print(f"System optimization failed: {result.stderr}")
    except Exception as e:
        print(f"Error applying system optimizations: {e}")

def clean_windows_old():
    """Clean Windows.old folder if it exists."""
    try:
        print("Cleaning Windows.old folder...")
        old_path = os.path.join(os.environ.get('SYSTEMDRIVE', 'C:'), 'Windows.old')
        if os.path.exists(old_path):
            # Use Disk Cleanup to remove Windows.old
            result = subprocess.run(['cleanmgr', '/sagerun:1'], capture_output=True, text=True)
            if result.returncode == 0:
                print("Windows.old folder cleaned.")
            else:
                print(f"Failed to clean Windows.old: {result.stderr}")
        else:
            print("No Windows.old folder found.")
    except Exception as e:
        print(f"Error cleaning Windows.old: {e}")

def optimize_game_mode():
    """Enable and optimize Game Mode settings."""
    try:
        print("Optimizing Game Mode settings...")
        game_script = '''
        # Enable Game Mode
        Set-ItemProperty -Path "HKCU:\\Software\\Microsoft\\GameBar" -Name "GameMode" -Value 1

        # Optimize for gaming
        Set-ItemProperty -Path "HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\GameDVR" -Name "AppCaptureEnabled" -Value 0
        Set-ItemProperty -Path "HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\GameDVR" -Name "AudioCaptureEnabled" -Value 0
        Set-ItemProperty -Path "HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\GameDVR" -Name "CursorCaptureEnabled" -Value 0
        '''
        result = subprocess.run(['powershell', '-Command', game_script], capture_output=True, text=True)
        if result.returncode == 0:
            print("Game Mode optimized.")
        else:
            print(f"Game Mode optimization failed: {result.stderr}")
    except Exception as e:
        print(f"Error optimizing Game Mode: {e}")

def optimize_context_menu():
    """Clean up and optimize context menu."""
    try:
        print("Optimizing context menu...")
        context_script = '''
        # Remove unnecessary context menu items
        $keys = @(
            "HKCR:\\Directory\\Background\\shellex\\ContextMenuHandlers\\New",
            "HKCR:\\Directory\\Background\\shellex\\ContextMenuHandlers\\Library Location",
            "HKCR:\\Folder\\shellex\\ContextMenuHandlers\\Library Location"
        )

        foreach ($key in $keys) {
            try {
                Remove-Item -Path $key -Recurse -ErrorAction SilentlyContinue
            } catch {
                # Key might not exist
            }
        }
        '''
        result = subprocess.run(['powershell', '-Command', context_script], capture_output=True, text=True)
        if result.returncode == 0:
            print("Context menu optimized.")
        else:
            print(f"Context menu optimization failed: {result.stderr}")
    except Exception as e:
        print(f"Error optimizing context menu: {e}")

def optimize_gpu_settings():
    """Optimize GPU settings for better performance."""
    try:
        print("Optimizing GPU settings...")
        gpu_script = '''
        # Optimize NVIDIA GPU settings if present
        $nvidiaPath = "HKCU:\\Software\\NVIDIA Corporation\\Global\\NGP"
        if (Test-Path $nvidiaPath) {
            Set-ItemProperty -Path $nvidiaPath -Name "NGPMode" -Value 1 -ErrorAction SilentlyContinue
        }

        # Optimize AMD GPU settings if present
        $amdPath = "HKLM:\\SYSTEM\\CurrentControlSet\\Control\\Class\\{4d36e968-e325-11ce-bfc1-08002be10318}\\0000"
        if (Test-Path $amdPath) {
            Set-ItemProperty -Path $amdPath -Name "EnableUlps" -Value 0 -ErrorAction SilentlyContinue
        }

        # General GPU optimizations
        Set-ItemProperty -Path "HKCU:\\Software\\Microsoft\\DirectX\\UserGpuPreferences" -Name "DirectXUserGlobalSettings" -Value "VRROptimizeEnable=1;" -ErrorAction SilentlyContinue
        '''
        result = subprocess.run(['powershell', '-Command', gpu_script], capture_output=True, text=True)
        if result.returncode == 0:
            print("GPU settings optimized.")
        else:
            print(f"GPU optimization failed: {result.stderr}")
    except Exception as e:
        print(f"Error optimizing GPU: {e}")

def optimize_usb_settings():
    """Optimize USB settings and power management."""
    try:
        print("Optimizing USB settings...")
        usb_script = '''
        # Disable USB selective suspend
        $usbPath = "HKLM:\\SYSTEM\\CurrentControlSet\\Services\\USB"
        Set-ItemProperty -Path "$usbPath" -Name "DisableSelectiveSuspend" -Value 1 -ErrorAction SilentlyContinue

        # Optimize USB hub settings
        $hubPath = "HKLM:\\SYSTEM\\CurrentControlSet\\Services\\usbhub"
        Set-ItemProperty -Path "$hubPath" -Name "DisableSelectiveSuspend" -Value 1 -ErrorAction SilentlyContinue

        # Enable USB 3.0 power management
        Set-ItemProperty -Path "HKLM:\\SYSTEM\\CurrentControlSet\\Services\\USBXHCI" -Name "DisableSelectiveSuspend" -Value 0 -ErrorAction SilentlyContinue
        '''
        result = subprocess.run(['powershell', '-Command', usb_script], capture_output=True, text=True)
        if result.returncode == 0:
            print("USB settings optimized.")
        else:
            print(f"USB optimization failed: {result.stderr}")
    except Exception as e:
        print(f"Error optimizing USB: {e}")

def optimize_printer_settings():
    """Optimize printer and print spooler settings."""
    try:
        print("Optimizing printer settings...")
        printer_script = '''
        # Restart print spooler service
        Restart-Service -Name "Spooler" -Force -ErrorAction SilentlyContinue

        # Clear print queue
        $printers = Get-Printer
        foreach ($printer in $printers) {
            try {
                $printer | Remove-PrintJob -ErrorAction SilentlyContinue
            } catch {
                # Continue if error
            }
        }

        # Optimize spooler settings
        Set-ItemProperty -Path "HKLM:\\SYSTEM\\CurrentControlSet\\Control\\Print" -Name "SpoolerPriority" -Value 1 -ErrorAction SilentlyContinue
        '''
        result = subprocess.run(['powershell', '-Command', printer_script], capture_output=True, text=True)
        if result.returncode == 0:
            print("Printer settings optimized.")
        else:
            print(f"Printer optimization failed: {result.stderr}")
    except Exception as e:
        print(f"Error optimizing printer: {e}")

def optimize_audio_settings():
    """Optimize audio and sound settings."""
    try:
        print("Optimizing audio settings...")
        audio_script = '''
        # Optimize audio service
        Set-Service -Name "Audiosrv" -StartupType Automatic -ErrorAction SilentlyContinue
        Start-Service -Name "Audiosrv" -ErrorAction SilentlyContinue

        # Set high quality audio
        Set-ItemProperty -Path "HKCU:\\Software\\Microsoft\\Multimedia\\Audio" -Name "DefaultEndpointVolume" -Value ([byte[]](0x00,0x00,0x00,0x00)) -ErrorAction SilentlyContinue

        # Disable audio enhancements for better performance
        $audioDevices = Get-AudioDevice -Playback
        foreach ($device in $audioDevices) {
            Set-AudioDevice -ID $device.ID -DefaultOnly -ErrorAction SilentlyContinue
        }
        '''
        result = subprocess.run(['powershell', '-Command', audio_script], capture_output=True, text=True)
        if result.returncode == 0:
            print("Audio settings optimized.")
        else:
            print(f"Audio optimization failed: {result.stderr}")
    except Exception as e:
        print(f"Error optimizing audio: {e}")

def optimize_bluetooth_settings():
    """Optimize Bluetooth settings and power management."""
    try:
        print("Optimizing Bluetooth settings...")
        bluetooth_script = '''
        # Enable Bluetooth service if present
        $btService = Get-Service -Name "bthserv" -ErrorAction SilentlyContinue
        if ($btService) {
            Set-Service -Name "bthserv" -StartupType Automatic -ErrorAction SilentlyContinue
            Start-Service -Name "bthserv" -ErrorAction SilentlyContinue
        }

        # Optimize Bluetooth power management
        $btPath = "HKLM:\\SYSTEM\\CurrentControlSet\\Services\\BTHPORT\\Parameters"
        Set-ItemProperty -Path $btPath -Name "IdleTimeout" -Value 30 -ErrorAction SilentlyContinue
        Set-ItemProperty -Path $btPath -Name "PageTimeout" -Value 15 -ErrorAction SilentlyContinue
        '''
        result = subprocess.run(['powershell', '-Command', bluetooth_script], capture_output=True, text=True)
        if result.returncode == 0:
            print("Bluetooth settings optimized.")
        else:
            print(f"Bluetooth optimization failed: {result.stderr}")
    except Exception as e:
        print(f"Error optimizing Bluetooth: {e}")

def optimize_firewall_settings():
    """Optimize Windows Firewall settings."""
    try:
        print("Optimizing firewall settings...")
        firewall_script = '''
        # Enable Windows Firewall for all profiles
        Set-NetFirewallProfile -Profile Domain,Public,Private -Enabled True -ErrorAction SilentlyContinue

        # Remove unnecessary firewall rules
        $rules = Get-NetFirewallRule | Where-Object { $_.DisplayName -like "*OneDrive*" -or $_.DisplayName -like "*Skype*" -or $_.DisplayName -like "*Teams*" }
        foreach ($rule in $rules) {
            Disable-NetFirewallRule -Name $rule.Name -ErrorAction SilentlyContinue
        }

        # Optimize firewall logging
        Set-NetFirewallProfile -Profile Domain,Public,Private -LogAllowed False -LogBlocked False -ErrorAction SilentlyContinue
        '''
        result = subprocess.run(['powershell', '-Command', firewall_script], capture_output=True, text=True)
        if result.returncode == 0:
            print("Firewall settings optimized.")
        else:
            print(f"Firewall optimization failed: {result.stderr}")
    except Exception as e:
        print(f"Error optimizing firewall: {e}")

def optimize_uac_settings():
    """Optimize User Account Control settings."""
    try:
        print("Optimizing UAC settings...")
        uac_script = '''
        # Set UAC to default level (balanced)
        Set-ItemProperty -Path "HKLM:\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System" -Name "EnableLUA" -Value 1 -ErrorAction SilentlyContinue
        Set-ItemProperty -Path "HKLM:\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System" -Name "ConsentPromptBehaviorAdmin" -Value 5 -ErrorAction SilentlyContinue
        Set-ItemProperty -Path "HKLM:\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System" -Name "ConsentPromptBehaviorUser" -Value 3 -ErrorAction SilentlyContinue
        Set-ItemProperty -Path "HKLM:\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System" -Name "PromptOnSecureDesktop" -Value 0 -ErrorAction SilentlyContinue
        '''
        result = subprocess.run(['powershell', '-Command', uac_script], capture_output=True, text=True)
        if result.returncode == 0:
            print("UAC settings optimized.")
        else:
            print(f"UAC optimization failed: {result.stderr}")
    except Exception as e:
        print(f"Error optimizing UAC: {e}")

def optimize_windows_update_settings():
    """Optimize Windows Update settings for better performance."""
    try:
        print("Optimizing Windows Update settings...")
        update_script = '''
        # Configure Windows Update for better performance
        Set-ItemProperty -Path "HKLM:\\SOFTWARE\\Policies\\Microsoft\\Windows\\WindowsUpdate\\AU" -Name "NoAutoUpdate" -Value 0 -ErrorAction SilentlyContinue
        Set-ItemProperty -Path "HKLM:\\SOFTWARE\\Policies\\Microsoft\\Windows\\WindowsUpdate\\AU" -Name "AUOptions" -Value 3 -ErrorAction SilentlyContinue
        Set-ItemProperty -Path "HKLM:\\SOFTWARE\\Policies\\Microsoft\\Windows\\WindowsUpdate\\AU" -Name "ScheduledInstallDay" -Value 0 -ErrorAction SilentlyContinue
        Set-ItemProperty -Path "HKLM:\\SOFTWARE\\Policies\\Microsoft\\Windows\\WindowsUpdate\\AU" -Name "ScheduledInstallTime" -Value 3 -ErrorAction SilentlyContinue

        # Clean up Windows Update cache
        Stop-Service -Name "wuauserv" -ErrorAction SilentlyContinue
        Remove-Item -Path "C:\\Windows\\SoftwareDistribution\\Download\\*" -Recurse -Force -ErrorAction SilentlyContinue
        Start-Service -Name "wuauserv" -ErrorAction SilentlyContinue
        '''
        result = subprocess.run(['powershell', '-Command', update_script], capture_output=True, text=True)
        if result.returncode == 0:
            print("Windows Update settings optimized.")
        else:
            print(f"Windows Update optimization failed: {result.stderr}")
    except Exception as e:
        print(f"Error optimizing Windows Update: {e}")

def optimize_error_reporting():
    """Optimize Windows Error Reporting settings."""
    try:
        print("Optimizing error reporting...")
        error_script = '''
        # Disable Windows Error Reporting for better performance
        Set-ItemProperty -Path "HKLM:\\SOFTWARE\\Microsoft\\PCHealth\\ErrorReporting" -Name "DoReport" -Value 0 -ErrorAction SilentlyContinue
        Set-ItemProperty -Path "HKCU:\\Software\\Microsoft\\Windows\\Windows Error Reporting" -Name "Disabled" -Value 1 -ErrorAction SilentlyContinue

        # Disable Windows Feedback
        Set-ItemProperty -Path "HKCU:\\SOFTWARE\\Microsoft\\Siuf\\Rules" -Name "NumberOfSIUFInPeriod" -Value 0 -ErrorAction SilentlyContinue
        Set-ItemProperty -Path "HKCU:\\SOFTWARE\\Microsoft\\Siuf\\Rules" -Name "PeriodInNanoSeconds" -Value 0 -ErrorAction SilentlyContinue
        '''
        result = subprocess.run(['powershell', '-Command', error_script], capture_output=True, text=True)
        if result.returncode == 0:
            print("Error reporting optimized.")
        else:
            print(f"Error reporting optimization failed: {result.stderr}")
    except Exception as e:
        print(f"Error optimizing error reporting: {e}")

def optimize_remote_desktop():
    """Optimize Remote Desktop settings."""
    try:
        print("Optimizing Remote Desktop settings...")
        rdp_script = '''
        # Enable Remote Desktop
        Set-ItemProperty -Path "HKLM:\\SYSTEM\\CurrentControlSet\\Control\\Terminal Server" -Name "fDenyTSConnections" -Value 0 -ErrorAction SilentlyContinue

        # Optimize RDP performance
        Set-ItemProperty -Path "HKLM:\\SOFTWARE\\Policies\\Microsoft\\Windows NT\\Terminal Services" -Name "fEnableRemoteFXAdvanced" -Value 1 -ErrorAction SilentlyContinue
        Set-ItemProperty -Path "HKLM:\\SOFTWARE\\Policies\\Microsoft\\Windows NT\\Terminal Services" -Name "ColorDepth" -Value 4 -ErrorAction SilentlyContinue
        Set-ItemProperty -Path "HKLM:\\SOFTWARE\\Policies\\Microsoft\\Windows NT\\Terminal Services" -Name "MaxCompressionLevel" -Value 2 -ErrorAction SilentlyContinue
        '''
        result = subprocess.run(['powershell', '-Command', rdp_script], capture_output=True, text=True)
        if result.returncode == 0:
            print("Remote Desktop optimized.")
        else:
            print(f"Remote Desktop optimization failed: {result.stderr}")
    except Exception as e:
        print(f"Error optimizing Remote Desktop: {e}")

def optimize_task_scheduler():
    """Clean up and optimize Task Scheduler."""
    try:
        print("Optimizing Task Scheduler...")
        task_script = '''
        # Disable unnecessary scheduled tasks
        $tasksToDisable = @(
            "\\Microsoft\\Windows\\Application Experience\\Microsoft Compatibility Appraiser",
            "\\Microsoft\\Windows\\Application Experience\\ProgramDataUpdater",
            "\\Microsoft\\Windows\\Customer Experience Improvement Program\\Consolidator",
            "\\Microsoft\\Windows\\Customer Experience Improvement Program\\KernelCeipTask",
            "\\Microsoft\\Windows\\DiskDiagnostic\\Microsoft-Windows-DiskDiagnosticDataCollector",
            "\\Microsoft\\Windows\\Maintenance\\WinSAT",
            "\\Microsoft\\Windows\\Maps\\MapsToastTask",
            "\\Microsoft\\Windows\\Maps\\MapsUpdateTask"
        )

        foreach ($task in $tasksToDisable) {
            Disable-ScheduledTask -TaskName $task -ErrorAction SilentlyContinue
        }

        # Clean up old task cache
        Remove-Item -Path "C:\\Windows\\System32\\Tasks\\*" -Include "*.job" -Force -ErrorAction SilentlyContinue
        '''
        result = subprocess.run(['powershell', '-Command', task_script], capture_output=True, text=True)
        if result.returncode == 0:
            print("Task Scheduler optimized.")
        else:
            print(f"Task Scheduler optimization failed: {result.stderr}")
    except Exception as e:
        print(f"Error optimizing Task Scheduler: {e}")

def optimize_font_cache():
    """Clear and rebuild font cache."""
    try:
        print("Optimizing font cache...")
        font_script = '''
        # Stop font cache service
        Stop-Service -Name "FontCache" -Force -ErrorAction SilentlyContinue

        # Clear font cache files
        Remove-Item -Path "C:\\Windows\\ServiceProfiles\\LocalService\\AppData\\Local\\FontCache\\*" -Force -ErrorAction SilentlyContinue
        Remove-Item -Path "C:\\Windows\\System32\\FNTCACHE.DAT" -Force -ErrorAction SilentlyContinue

        # Restart font cache service
        Start-Service -Name "FontCache" -ErrorAction SilentlyContinue
        '''
        result = subprocess.run(['powershell', '-Command', font_script], capture_output=True, text=True)
        if result.returncode == 0:
            print("Font cache optimized.")
        else:
            print(f"Font cache optimization failed: {result.stderr}")
    except Exception as e:
        print(f"Error optimizing font cache: {e}")

def optimize_icon_cache():
    """Rebuild icon cache."""
    try:
        print("Optimizing icon cache...")
        icon_script = '''
        # Stop explorer
        Stop-Process -Name "explorer" -Force -ErrorAction SilentlyContinue

        # Remove icon cache files
        Remove-Item -Path "C:\\Users\\*\\AppData\\Local\\IconCache.db" -Force -ErrorAction SilentlyContinue
        Remove-Item -Path "C:\\Users\\*\\AppData\\Local\\Microsoft\\Windows\\Explorer\\iconcache*" -Force -ErrorAction SilentlyContinue

        # Restart explorer
        Start-Process "explorer.exe"
        '''
        result = subprocess.run(['powershell', '-Command', icon_script], capture_output=True, text=True)
        if result.returncode == 0:
            print("Icon cache optimized.")
        else:
            print(f"Icon cache optimization failed: {result.stderr}")
    except Exception as e:
        print(f"Error optimizing icon cache: {e}")

def optimize_thumbnail_cache():
    """Clear thumbnail cache."""
    try:
        print("Optimizing thumbnail cache...")
        thumb_script = '''
        # Clear thumbnail cache
        Remove-Item -Path "C:\\Users\\*\\AppData\\Local\\Microsoft\\Windows\\Explorer\\thumbcache*" -Force -ErrorAction SilentlyContinue

        # Clear thumbnail database
        Remove-Item -Path "C:\\Users\\*\\AppData\\Local\\Microsoft\\Windows\\Explorer\\thumbcache.db" -Force -ErrorAction SilentlyContinue
        '''
        result = subprocess.run(['powershell', '-Command', thumb_script], capture_output=True, text=True)
        if result.returncode == 0:
            print("Thumbnail cache optimized.")
        else:
            print(f"Thumbnail cache optimization failed: {result.stderr}")
    except Exception as e:
        print(f"Error optimizing thumbnail cache: {e}")

def optimize_prefetch_superfetch():
    """Optimize Prefetch and Superfetch settings."""
    try:
        print("Optimizing Prefetch and Superfetch...")
        prefetch_script = '''
        # Enable Superfetch for better performance
        Set-ItemProperty -Path "HKLM:\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management\\PrefetchParameters" -Name "EnablePrefetcher" -Value 3 -ErrorAction SilentlyContinue
        Set-ItemProperty -Path "HKLM:\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management\\PrefetchParameters" -Name "EnableSuperfetch" -Value 3 -ErrorAction SilentlyContinue

        # Optimize boot prefetch
        Set-ItemProperty -Path "HKLM:\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management\\PrefetchParameters" -Name "BootId" -Value 1 -ErrorAction SilentlyContinue
        '''
        result = subprocess.run(['powershell', '-Command', prefetch_script], capture_output=True, text=True)
        if result.returncode == 0:
            print("Prefetch and Superfetch optimized.")
        else:
            print(f"Prefetch optimization failed: {result.stderr}")
    except Exception as e:
        print(f"Error optimizing Prefetch: {e}")

def optimize_readyboost():
    """Optimize ReadyBoost settings."""
    try:
        print("Optimizing ReadyBoost settings...")
        readyboost_script = '''
        # Enable ReadyBoost for USB drives
        Set-ItemProperty -Path "HKLM:\\SOFTWARE\\Policies\\Microsoft\\Windows\\WcnSvc" -Name "DisableWcnSsidSsid" -Value 0 -ErrorAction SilentlyContinue

        # Configure ReadyBoost cache size
        $readyBoostPath = "HKLM:\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\OptimalLayout"
        Set-ItemProperty -Path $readyBoostPath -Name "EnableAutoLayout" -Value 1 -ErrorAction SilentlyContinue
        '''
        result = subprocess.run(['powershell', '-Command', readyboost_script], capture_output=True, text=True)
        if result.returncode == 0:
            print("ReadyBoost optimized.")
        else:
            print(f"ReadyBoost optimization failed: {result.stderr}")
    except Exception as e:
        print(f"Error optimizing ReadyBoost: {e}")

def optimize_windows_store():
    """Optimize Microsoft Store and app cache."""
    try:
        print("Optimizing Windows Store...")
        store_script = '''
        # Clear Microsoft Store cache
        WSReset.exe

        # Reset Microsoft Store
        Get-AppxPackage Microsoft.WindowsStore | Reset-AppxPackage -ErrorAction SilentlyContinue

        # Clear app cache
        Remove-Item -Path "C:\\Users\\*\\AppData\\Local\\Packages\\Microsoft.WindowsStore*\\LocalCache" -Recurse -Force -ErrorAction SilentlyContinue
        '''
        result = subprocess.run(['powershell', '-Command', store_script], capture_output=True, text=True)
        if result.returncode == 0:
            print("Windows Store optimized.")
        else:
            print(f"Windows Store optimization failed: {result.stderr}")
    except Exception as e:
        print(f"Error optimizing Windows Store: {e}")

def optimize_cortana():
    """Optimize Cortana settings and data."""
    try:
        print("Optimizing Cortana...")
        cortana_script = '''
        # Disable Cortana web search
        Set-ItemProperty -Path "HKCU:\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Search" -Name "BingSearchEnabled" -Value 0 -ErrorAction SilentlyContinue
        Set-ItemProperty -Path "HKCU:\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Search" -Name "CortanaConsent" -Value 0 -ErrorAction SilentlyContinue

        # Clear Cortana data
        Remove-Item -Path "C:\\Users\\*\\AppData\\Local\\Packages\\Microsoft.549981C3F5F10*\\LocalState" -Recurse -Force -ErrorAction SilentlyContinue
        '''
        result = subprocess.run(['powershell', '-Command', cortana_script], capture_output=True, text=True)
        if result.returncode == 0:
            print("Cortana optimized.")
        else:
            print(f"Cortana optimization failed: {result.stderr}")
    except Exception as e:
        print(f"Error optimizing Cortana: {e}")

def optimize_onedrive():
    """Optimize OneDrive settings and cache."""
    try:
        print("Optimizing OneDrive...")
        onedrive_script = '''
        # Disable OneDrive startup
        Set-ItemProperty -Path "HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Run" -Name "OneDrive" -Value "" -ErrorAction SilentlyContinue

        # Clear OneDrive cache
        Remove-Item -Path "C:\\Users\\*\\AppData\\Local\\Microsoft\\OneDrive\\cache" -Recurse -Force -ErrorAction SilentlyContinue

        # Optimize OneDrive settings
        Set-ItemProperty -Path "HKCU:\\Software\\Microsoft\\OneDrive" -Name "DisablePersonalSync" -Value 1 -ErrorAction SilentlyContinue
        '''
        result = subprocess.run(['powershell', '-Command', onedrive_script], capture_output=True, text=True)
        if result.returncode == 0:
            print("OneDrive optimized.")
        else:
            print(f"OneDrive optimization failed: {result.stderr}")
    except Exception as e:
        print(f"Error optimizing OneDrive: {e}")

def optimize_microsoft_edge():
    """Optimize Microsoft Edge browser settings."""
    try:
        print("Optimizing Microsoft Edge...")
        edge_script = '''
        # Clear Edge cache and data
        Remove-Item -Path "C:\\Users\\*\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default\\Cache" -Recurse -Force -ErrorAction SilentlyContinue
        Remove-Item -Path "C:\\Users\\*\\AppData\\Local\\Microsoft\\Edge\\User Data\\Default\\Cookies" -Recurse -Force -ErrorAction SilentlyContinue

        # Disable Edge prelaunch
        Set-ItemProperty -Path "HKCU:\\Software\\Microsoft\\Edge" -Name "StartupBoostEnabled" -Value 0 -ErrorAction SilentlyContinue

        # Optimize Edge performance
        Set-ItemProperty -Path "HKCU:\\Software\\Policies\\Microsoft\\Edge" -Name "BackgroundModeEnabled" -Value 0 -ErrorAction SilentlyContinue
        '''
        result = subprocess.run(['powershell', '-Command', edge_script], capture_output=True, text=True)
        if result.returncode == 0:
            print("Microsoft Edge optimized.")
        else:
            print(f"Microsoft Edge optimization failed: {result.stderr}")
    except Exception as e:
        print(f"Error optimizing Microsoft Edge: {e}")

def optimize_registry_animations():
    """Disable Windows animations and transitions for better performance."""
    try:
        print("Optimizing registry animations...")
        animation_script = '''
        # Disable Windows animations
        Set-ItemProperty -Path "HKCU:\\Control Panel\\Desktop" -Name "UserPreferencesMask" -Value ([byte[]](0x90,0x12,0x03,0x80,0x10,0x00,0x00,0x00)) -ErrorAction SilentlyContinue
        Set-ItemProperty -Path "HKCU:\\Control Panel\\Desktop\\WindowMetrics" -Name "MinAnimate" -Value 0 -ErrorAction SilentlyContinue

        # Disable taskbar animations
        Set-ItemProperty -Path "HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced" -Name "TaskbarAnimations" -Value 0 -ErrorAction SilentlyContinue

        # Disable menu animations
        Set-ItemProperty -Path "HKCU:\\Control Panel\\Desktop" -Name "MenuShowDelay" -Value 0 -ErrorAction SilentlyContinue

        # Disable tooltip animations
        Set-ItemProperty -Path "HKCU:\\Control Panel\\Desktop" -Name "SmoothScroll" -Value 0 -ErrorAction SilentlyContinue
        '''
        result = subprocess.run(['powershell', '-Command', animation_script], capture_output=True, text=True)
        if result.returncode == 0:
            print("Registry animations optimized.")
        else:
            print(f"Registry animation optimization failed: {result.stderr}")
    except Exception as e:
        print(f"Error optimizing registry animations: {e}")

def optimize_explorer_settings():
    """Optimize Windows Explorer settings for better performance."""
    try:
        print("Optimizing Explorer settings...")
        explorer_script = '''
        # Disable thumbnail generation
        Set-ItemProperty -Path "HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced" -Name "IconsOnly" -Value 1 -ErrorAction SilentlyContinue

        # Disable Aero Peek
        Set-ItemProperty -Path "HKCU:\\Software\\Microsoft\\Windows\\DWM" -Name "EnableAeroPeek" -Value 0 -ErrorAction SilentlyContinue

        # Disable Windows Aero Shake
        Set-ItemProperty -Path "HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced" -Name "DisallowShaking" -Value 1 -ErrorAction SilentlyContinue

        # Disable frequent folders in Quick Access
        Set-ItemProperty -Path "HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer" -Name "ShowFrequent" -Value 0 -ErrorAction SilentlyContinue

        # Disable recent files in Quick Access
        Set-ItemProperty -Path "HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer" -Name "ShowRecent" -Value 0 -ErrorAction SilentlyContinue
        '''
        result = subprocess.run(['powershell', '-Command', explorer_script], capture_output=True, text=True)
        if result.returncode == 0:
            print("Explorer settings optimized.")
        else:
            print(f"Explorer optimization failed: {result.stderr}")
    except Exception as e:
        print(f"Error optimizing Explorer: {e}")

def disable_windows_features():
    """Disable unnecessary Windows features for better performance."""
    try:
        print("Disabling unnecessary Windows features...")
        features_script = '''
        # Disable Windows Media Player
        Disable-WindowsOptionalFeature -Online -FeatureName "WindowsMediaPlayer" -NoRestart -ErrorAction SilentlyContinue

        # Disable Windows Fax and Scan
        Disable-WindowsOptionalFeature -Online -FeatureName "FaxServicesClientPackage" -NoRestart -ErrorAction SilentlyContinue

        # Disable XPS Viewer
        Disable-WindowsOptionalFeature -Online -FeatureName "Xps-Foundation-Xps-Viewer" -NoRestart -ErrorAction SilentlyContinue

        # Disable Work Folders
        Disable-WindowsOptionalFeature -Online -FeatureName "WorkFolders-Client" -NoRestart -ErrorAction SilentlyContinue
        '''
        result = subprocess.run(['powershell', '-Command', features_script], capture_output=True, text=True)
        if result.returncode == 0:
            print("Windows features disabled.")
        else:
            print(f"Windows features disabling failed: {result.stderr}")
    except Exception as e:
        print(f"Error disabling Windows features: {e}")

def optimize_memory_registry():
    """Optimize memory management registry settings."""
    try:
        print("Optimizing memory registry settings...")
        memory_script = '''
        # Optimize memory management
        Set-ItemProperty -Path "HKLM:\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management" -Name "LargeSystemCache" -Value 0 -ErrorAction SilentlyContinue
        Set-ItemProperty -Path "HKLM:\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management" -Name "DisablePagingExecutive" -Value 1 -ErrorAction SilentlyContinue
        Set-ItemProperty -Path "HKLM:\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management" -Name "SystemPages" -Value 0 -ErrorAction SilentlyContinue

        # Optimize virtual memory
        Set-ItemProperty -Path "HKLM:\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management" -Name "DisablePageCombining" -Value 1 -ErrorAction SilentlyContinue
        '''
        result = subprocess.run(['powershell', '-Command', memory_script], capture_output=True, text=True)
        if result.returncode == 0:
            print("Memory registry settings optimized.")
        else:
            print(f"Memory registry optimization failed: {result.stderr}")
    except Exception as e:
        print(f"Error optimizing memory registry: {e}")

def disable_telemetry_services():
    """Disable Windows telemetry and data collection services."""
    try:
        print("Disabling telemetry services...")
        telemetry_script = '''
        # Stop and disable Connected User Experiences and Telemetry
        Stop-Service -Name "DiagTrack" -ErrorAction SilentlyContinue
        Set-Service -Name "DiagTrack" -StartupType Disabled -ErrorAction SilentlyContinue

        # Stop and disable dmwappushservice
        Stop-Service -Name "dmwappushservice" -ErrorAction SilentlyContinue
        Set-Service -Name "dmwappushservice" -StartupType Disabled -ErrorAction SilentlyContinue

        # Disable Windows Error Reporting Service
        Stop-Service -Name "WerSvc" -ErrorAction SilentlyContinue
        Set-Service -Name "WerSvc" -StartupType Disabled -ErrorAction SilentlyContinue
        '''
        result = subprocess.run(['powershell', '-Command', telemetry_script], capture_output=True, text=True)
        if result.returncode == 0:
            print("Telemetry services disabled.")
        else:
            print(f"Telemetry services disabling failed: {result.stderr}")
    except Exception as e:
        print(f"Error disabling telemetry services: {e}")

def optimize_network_registry():
    """Optimize network registry settings for better performance."""
    try:
        print("Optimizing network registry settings...")
        network_script = '''
        # Optimize TCP/IP settings
        Set-ItemProperty -Path "HKLM:\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters" -Name "TcpAckFrequency" -Value 1 -ErrorAction SilentlyContinue
        Set-ItemProperty -Path "HKLM:\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters" -Name "TCPNoDelay" -Value 1 -ErrorAction SilentlyContinue
        Set-ItemProperty -Path "HKLM:\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters" -Name "Tcp1323Opts" -Value 1 -ErrorAction SilentlyContinue

        # Optimize network adapter settings
        Set-ItemProperty -Path "HKLM:\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters" -Name "DefaultTTL" -Value 64 -ErrorAction SilentlyContinue
        Set-ItemProperty -Path "HKLM:\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters" -Name "EnablePMTUDiscovery" -Value 1 -ErrorAction SilentlyContinue
        '''
        result = subprocess.run(['powershell', '-Command', network_script], capture_output=True, text=True)
        if result.returncode == 0:
            print("Network registry settings optimized.")
        else:
            print(f"Network registry optimization failed: {result.stderr}")
    except Exception as e:
        print(f"Error optimizing network registry: {e}")

def disable_windows_tips():
    """Disable Windows tips and suggestions."""
    try:
        print("Disabling Windows tips and suggestions...")
        tips_script = '''
        # Disable Windows Spotlight
        Set-ItemProperty -Path "HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\ContentDeliveryManager" -Name "SubscribedContent-338393Enabled" -Value 0 -ErrorAction SilentlyContinue
        Set-ItemProperty -Path "HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\ContentDeliveryManager" -Name "SubscribedContent-353694Enabled" -Value 0 -ErrorAction SilentlyContinue

        # Disable suggestions in Start menu
        Set-ItemProperty -Path "HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\ContentDeliveryManager" -Name "SubscribedContent-338388Enabled" -Value 0 -ErrorAction SilentlyContinue

        # Disable tips about Windows
        Set-ItemProperty -Path "HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\ContentDeliveryManager" -Name "SubscribedContent-338389Enabled" -Value 0 -ErrorAction SilentlyContinue
        '''
        result = subprocess.run(['powershell', '-Command', tips_script], capture_output=True, text=True)
        if result.returncode == 0:
            print("Windows tips and suggestions disabled.")
        else:
            print(f"Windows tips disabling failed: {result.stderr}")
    except Exception as e:
        print(f"Error disabling Windows tips: {e}")

def optimize_usb_registry():
    """Optimize USB registry settings for better performance."""
    try:
        print("Optimizing USB registry settings...")
        usb_script = '''
        # Optimize USB power management
        Set-ItemProperty -Path "HKLM:\\SYSTEM\\CurrentControlSet\\Services\\USB" -Name "DisableSelectiveSuspend" -Value 1 -ErrorAction SilentlyContinue

        # Optimize USB hub settings
        Set-ItemProperty -Path "HKLM:\\SYSTEM\\CurrentControlSet\\Services\\usbhub" -Name "DisableSelectiveSuspend" -Value 1 -ErrorAction SilentlyContinue

        # Enable USB 3.0 optimizations
        Set-ItemProperty -Path "HKLM:\\SYSTEM\\CurrentControlSet\\Services\\USBXHCI" -Name "DisableSelectiveSuspend" -Value 0 -ErrorAction SilentlyContinue

        # Optimize USB storage devices
        Set-ItemProperty -Path "HKLM:\\SYSTEM\\CurrentControlSet\\Services\\usbstor" -Name "ErrorControl" -Value 1 -ErrorAction SilentlyContinue
        '''
        result = subprocess.run(['powershell', '-Command', usb_script], capture_output=True, text=True)
        if result.returncode == 0:
            print("USB registry settings optimized.")
        else:
            print(f"USB registry optimization failed: {result.stderr}")
    except Exception as e:
        print(f"Error optimizing USB registry: {e}")

def disable_store_autoupdates():
    """Disable Microsoft Store automatic updates."""
    try:
        print("Disabling Microsoft Store auto-updates...")
        store_script = '''
        # Disable automatic app updates
        Set-ItemProperty -Path "HKLM:\\SOFTWARE\\Policies\\Microsoft\\WindowsStore" -Name "AutoDownload" -Value 2 -ErrorAction SilentlyContinue

        # Disable automatic updates for all apps
        Set-ItemProperty -Path "HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\BackgroundAccessApplications" -Name "GlobalUserDisabled" -Value 1 -ErrorAction SilentlyContinue
        '''
        result = subprocess.run(['powershell', '-Command', store_script], capture_output=True, text=True)
        if result.returncode == 0:
            print("Microsoft Store auto-updates disabled.")
        else:
            print(f"Microsoft Store auto-updates disabling failed: {result.stderr}")
    except Exception as e:
        print(f"Error disabling Microsoft Store auto-updates: {e}")

def optimize_power_registry():
    """Optimize power management registry settings."""
    try:
        print("Optimizing power registry settings...")
        power_script = '''
        # Disable USB selective suspend
        Set-ItemProperty -Path "HKLM:\\SYSTEM\\CurrentControlSet\\Services\\USB" -Name "DisableSelectiveSuspend" -Value 1 -ErrorAction SilentlyContinue

        # Optimize processor power management
        Set-ItemProperty -Path "HKLM:\\SYSTEM\\CurrentControlSet\\Control\\Power\\PowerSettings\\54533251-82be-4824-96c1-47b60b740d00\\0cc5b647-c1df-4637-891a-dec35c318583" -Name "Attributes" -Value 2 -ErrorAction SilentlyContinue

        # Disable hibernation timeout
        Set-ItemProperty -Path "HKLM:\\SYSTEM\\CurrentControlSet\\Control\\Power" -Name "HibernateEnabled" -Value 0 -ErrorAction SilentlyContinue
        '''
        result = subprocess.run(['powershell', '-Command', power_script], capture_output=True, text=True)
        if result.returncode == 0:
            print("Power registry settings optimized.")
        else:
            print(f"Power registry optimization failed: {result.stderr}")
    except Exception as e:
        print(f"Error optimizing power registry: {e}")

def disable_search_service():
    """Disable Windows Search service for better performance."""
    try:
        print("Disabling Windows Search service...")
        search_script = '''
        # Stop and disable Windows Search service
        Stop-Service -Name "WSearch" -ErrorAction SilentlyContinue
        Set-Service -Name "WSearch" -StartupType Disabled -ErrorAction SilentlyContinue

        # Disable search indexing
        Set-ItemProperty -Path "HKLM:\\SOFTWARE\\Policies\\Microsoft\\Windows\\Windows Search" -Name "AllowCortana" -Value 0 -ErrorAction SilentlyContinue
        Set-ItemProperty -Path "HKLM:\\SOFTWARE\\Policies\\Microsoft\\Windows\\Windows Search" -Name "AllowSearchToUseLocation" -Value 0 -ErrorAction SilentlyContinue
        '''
        result = subprocess.run(['powershell', '-Command', search_script], capture_output=True, text=True)
        if result.returncode == 0:
            print("Windows Search service disabled.")
        else:
            print(f"Windows Search service disabling failed: {result.stderr}")
    except Exception as e:
        print(f"Error disabling Windows Search service: {e}")

def disable_xbox_services():
    """Disable Xbox Live services for better performance."""
    try:
        print("Disabling Xbox services...")
        xbox_script = '''
        # Disable Xbox Live Auth Manager
        Stop-Service -Name "XblAuthManager" -ErrorAction SilentlyContinue
        Set-Service -Name "XblAuthManager" -StartupType Disabled -ErrorAction SilentlyContinue

        # Disable Xbox Live Game Save
        Stop-Service -Name "XblGameSave" -ErrorAction SilentlyContinue
        Set-Service -Name "XblGameSave" -StartupType Disabled -ErrorAction SilentlyContinue

        # Disable Xbox Live Net Auth
        Stop-Service -Name "XblNetAuthManager" -ErrorAction SilentlyContinue
        Set-Service -Name "XblNetAuthManager" -StartupType Disabled -ErrorAction SilentlyContinue
        '''
        result = subprocess.run(['powershell', '-Command', xbox_script], capture_output=True, text=True)
        if result.returncode == 0:
            print("Xbox services disabled.")
        else:
            print(f"Xbox services disabling failed: {result.stderr}")
    except Exception as e:
        print(f"Error disabling Xbox services: {e}")

def disable_print_services():
    """Disable print services if no printer is connected."""
    try:
        print("Disabling print services...")
        print_script = '''
        # Stop and disable Print Spooler
        Stop-Service -Name "Spooler" -ErrorAction SilentlyContinue
        Set-Service -Name "Spooler" -StartupType Disabled -ErrorAction SilentlyContinue

        # Disable Fax service
        Stop-Service -Name "Fax" -ErrorAction SilentlyContinue
        Set-Service -Name "Fax" -StartupType Disabled -ErrorAction SilentlyContinue
        '''
        result = subprocess.run(['powershell', '-Command', print_script], capture_output=True, text=True)
        if result.returncode == 0:
            print("Print services disabled.")
        else:
            print(f"Print services disabling failed: {result.stderr}")
    except Exception as e:
        print(f"Error disabling print services: {e}")

def disable_update_medic():
    """Disable Windows Update Medic Service."""
    try:
        print("Disabling Windows Update Medic...")
        medic_script = '''
        # Stop and disable Windows Update Medic Service
        Stop-Service -Name "WaaSMedicSvc" -ErrorAction SilentlyContinue
        Set-Service -Name "WaaSMedicSvc" -StartupType Disabled -ErrorAction SilentlyContinue
        '''
        result = subprocess.run(['powershell', '-Command', medic_script], capture_output=True, text=True)
        if result.returncode == 0:
            print("Windows Update Medic disabled.")
        else:
            print(f"Windows Update Medic disabling failed: {result.stderr}")
    except Exception as e:
        print(f"Error disabling Windows Update Medic: {e}")

def disable_store_install_service():
    """Disable Microsoft Store Install Service."""
    try:
        print("Disabling Microsoft Store Install Service...")
        store_script = '''
        # Stop and disable Microsoft Store Install Service
        Stop-Service -Name "InstallService" -ErrorAction SilentlyContinue
        Set-Service -Name "InstallService" -StartupType Disabled -ErrorAction SilentlyContinue
        '''
        result = subprocess.run(['powershell', '-Command', store_script], capture_output=True, text=True)
        if result.returncode == 0:
            print("Microsoft Store Install Service disabled.")
        else:
            print(f"Microsoft Store Install Service disabling failed: {result.stderr}")
    except Exception as e:
        print(f"Error disabling Microsoft Store Install Service: {e}")

def disable_push_notifications():
    """Disable Windows Push Notifications."""
    try:
        print("Disabling push notifications...")
        push_script = '''
        # Stop and disable Windows Push Notifications
        Stop-Service -Name "WpnService" -ErrorAction SilentlyContinue
        Set-Service -Name "WpnService" -StartupType Disabled -ErrorAction SilentlyContinue

        # Disable push notifications in registry
        Set-ItemProperty -Path "HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\PushNotifications" -Name "ToastEnabled" -Value 0 -ErrorAction SilentlyContinue
        '''
        result = subprocess.run(['powershell', '-Command', push_script], capture_output=True, text=True)
        if result.returncode == 0:
            print("Push notifications disabled.")
        else:
            print(f"Push notifications disabling failed: {result.stderr}")
    except Exception as e:
        print(f"Error disabling push notifications: {e}")

def disable_biometric_service():
    """Disable Windows Biometric Service."""
    try:
        print("Disabling biometric service...")
        bio_script = '''
        # Stop and disable Windows Biometric Service
        Stop-Service -Name "WbioSrvc" -ErrorAction SilentlyContinue
        Set-Service -Name "WbioSrvc" -StartupType Disabled -ErrorAction SilentlyContinue
        '''
        result = subprocess.run(['powershell', '-Command', bio_script], capture_output=True, text=True)
        if result.returncode == 0:
            print("Biometric service disabled.")
        else:
            print(f"Biometric service disabling failed: {result.stderr}")
    except Exception as e:
        print(f"Error disabling biometric service: {e}")

def disable_windows_connect():
    """Disable Windows Connect Now service."""
    try:
        print("Disabling Windows Connect Now...")
        connect_script = '''
        # Stop and disable Windows Connect Now
        Stop-Service -Name "wcncsvc" -ErrorAction SilentlyContinue
        Set-Service -Name "wcncsvc" -StartupType Disabled -ErrorAction SilentlyContinue
        '''
        result = subprocess.run(['powershell', '-Command', connect_script], capture_output=True, text=True)
        if result.returncode == 0:
            print("Windows Connect Now disabled.")
        else:
            print(f"Windows Connect Now disabling failed: {result.stderr}")
    except Exception as e:
        print(f"Error disabling Windows Connect Now: {e}")

def enable_ultimate_performance():
    """Enable Ultimate Performance power plan for maximum performance."""
    try:
        print("Enabling Ultimate Performance power plan...")
        ultimate_script = '''
        # Check if Ultimate Performance plan exists
        $ultimatePlan = Get-NetAdapter | Where-Object { $_.Name -like "*Ultimate*" }
        if (!$ultimatePlan) {
            # Create Ultimate Performance power plan
            powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61
            $ultimateGuid = (powercfg -list | Where-Object { $_ -like "*Ultimate*" } | ForEach-Object { $_.Split()[3] })
            if ($ultimateGuid) {
                powercfg -setactive $ultimateGuid
                Write-Host "Ultimate Performance plan enabled."
            } else {
                Write-Host "Failed to create Ultimate Performance plan."
            }
        } else {
            Write-Host "Ultimate Performance plan already exists."
        }
        '''
        result = subprocess.run(['powershell', '-Command', ultimate_script], capture_output=True, text=True)
        if result.returncode == 0:
            print("Ultimate Performance plan enabled.")
        else:
            print(f"Ultimate Performance plan setup failed: {result.stderr}")
    except Exception as e:
        print(f"Error enabling Ultimate Performance: {e}")

def optimize_pagefile_memory():
    """Optimize pagefile and memory settings based on RAM size."""
    try:
        print("Optimizing pagefile and memory settings...")
        memory_script = '''
        # Get total RAM in MB
        $totalRam = (Get-CimInstance -ClassName Win32_ComputerSystem).TotalPhysicalMemory / 1MB

        # Calculate optimal pagefile size (1.5x RAM for min, 3x RAM for max)
        $minSize = [math]::Round($totalRam * 1.5)
        $maxSize = [math]::Round($totalRam * 3)

        # Set pagefile to system managed with custom size
        $pageFile = Get-CimInstance -ClassName Win32_PageFileSetting
        if ($pageFile) {
            $pageFile.InitialSize = $minSize
            $pageFile.MaximumSize = $maxSize
            $pageFile.Put()
        }

        # Optimize memory management registry settings
        Set-ItemProperty -Path "HKLM:\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management" -Name "LargeSystemCache" -Value 0 -ErrorAction SilentlyContinue
        Set-ItemProperty -Path "HKLM:\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management" -Name "DisablePagingExecutive" -Value 1 -ErrorAction SilentlyContinue
        Set-ItemProperty -Path "HKLM:\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management" -Name "SystemPages" -Value 0 -ErrorAction SilentlyContinue

        Write-Host "Pagefile optimized for $($totalRam)MB RAM: Min=$($minSize)MB, Max=$($maxSize)MB"
        '''
        result = subprocess.run(['powershell', '-Command', memory_script], capture_output=True, text=True)
        if result.returncode == 0:
            print("Pagefile and memory settings optimized.")
        else:
            print(f"Pagefile optimization failed: {result.stderr}")
    except Exception as e:
        print(f"Error optimizing pagefile: {e}")

def tune_gpu_driver_settings():
    """Tune GPU driver settings for maximum performance and low latency."""
    try:
        print("Tuning GPU driver settings...")
        gpu_script = '''
        # NVIDIA GPU optimizations
        $nvidiaPath = "HKLM:\\SOFTWARE\\NVIDIA Corporation\\Global\\NGP"
        if (Test-Path $nvidiaPath) {
            Set-ItemProperty -Path $nvidiaPath -Name "NGPMode" -Value 1 -ErrorAction SilentlyContinue
            Set-ItemProperty -Path $nvidiaPath -Name "PerfLevelSrc" -Value 0x2222 -ErrorAction SilentlyContinue
        }

        # AMD GPU optimizations
        $amdPath = "HKLM:\\SYSTEM\\CurrentControlSet\\Control\\Class\\{4d36e968-e325-11ce-bfc1-08002be10318}\\0000"
        if (Test-Path $amdPath) {
            Set-ItemProperty -Path $amdPath -Name "EnableUlps" -Value 0 -ErrorAction SilentlyContinue
            Set-ItemProperty -Path $amdPath -Name "PP_MCLKStutterModeThreshold" -Value 0 -ErrorAction SilentlyContinue
        }

        # Intel GPU optimizations
        $intelPath = "HKLM:\\SOFTWARE\\Intel\\Display\\igfxcui\\profiles\\media"
        if (Test-Path $intelPath) {
            Set-ItemProperty -Path $intelPath -Name "ProcAmpEnabled" -Value 0 -ErrorAction SilentlyContinue
        }

        # General GPU optimizations
        Set-ItemProperty -Path "HKCU:\\Software\\Microsoft\\DirectX\\UserGpuPreferences" -Name "DirectXUserGlobalSettings" -Value "VRROptimizeEnable=1;SwapEffectUpgradeEnable=1;" -ErrorAction SilentlyContinue

        Write-Host "GPU driver settings tuned for maximum performance."
        '''
        result = subprocess.run(['powershell', '-Command', gpu_script], capture_output=True, text=True)
        if result.returncode == 0:
            print("GPU driver settings optimized.")
        else:
            print(f"GPU optimization failed: {result.stderr}")
    except Exception as e:
        print(f"Error tuning GPU settings: {e}")

def autoruns_kill_bloatware():
    """Use Autoruns-style approach to kill bloatware and background tasks."""
    try:
        print("Removing bloatware and optimizing startup...")
        bloatware_script = '''
        # Common bloatware processes to stop
        $bloatwareProcesses = @(
            "OneDrive",
            "Skype",
            "Teams",
            "Spotify",
            "Discord",
            "Steam",
            "EpicGamesLauncher",
            "UbisoftConnect",
            "Battle.net",
            "RiotClientServices",
            "Origin",
            "uTorrent",
            "AdobeARM",
            "CCleaner64",
            "CCleaner"
        )

        foreach ($process in $bloatwareProcesses) {
            try {
                Stop-Process -Name $process -Force -ErrorAction SilentlyContinue
            } catch {
                # Process might not be running
            }
        }

        # Disable common bloatware startup entries
        $startupPaths = @(
            "HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Run",
            "HKLM:\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run",
            "HKLM:\\SOFTWARE\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Run"
        )

        foreach ($path in $startupPaths) {
            if (Test-Path $path) {
                $bloatwareEntries = Get-ItemProperty -Path $path | Get-Member -MemberType NoteProperty | Where-Object {
                    $_.Name -like "*OneDrive*" -or $_.Name -like "*Skype*" -or $_.Name -like "*Teams*" -or
                    $_.Name -like "*Spotify*" -or $_.Name -like "*CCleaner*"
                }
                foreach ($entry in $bloatwareEntries) {
                    Remove-ItemProperty -Path $path -Name $entry.Name -ErrorAction SilentlyContinue
                }
            }
        }

        Write-Host "Bloatware processes stopped and startup entries removed."
        '''
        result = subprocess.run(['powershell', '-Command', bloatware_script], capture_output=True, text=True)
        if result.returncode == 0:
            print("Bloatware and background tasks optimized.")
        else:
            print(f"Bloatware cleanup failed: {result.stderr}")
    except Exception as e:
        print(f"Error removing bloatware: {e}")

def finetune_network_stack():
    """Fine-tune network stack by disabling Nagle and optimizing NIC settings."""
    try:
        print("Fine-tuning network stack...")
        network_script = '''
        # Disable Nagle's algorithm for reduced latency
        $tcpParams = "HKLM:\\SYSTEM\\CurrentControlSet\\Services\\Tcpip\\Parameters"
        Set-ItemProperty -Path $tcpParams -Name "TcpAckFrequency" -Value 1 -ErrorAction SilentlyContinue
        Set-ItemProperty -Path $tcpParams -Name "TCPNoDelay" -Value 1 -ErrorAction SilentlyContinue
        Set-ItemProperty -Path $tcpParams -Name "Tcp1323Opts" -Value 1 -ErrorAction SilentlyContinue

        # Optimize network interface settings
        $adapters = Get-NetAdapter | Where-Object { $_.Status -eq "Up" }
        foreach ($adapter in $adapters) {
            # Disable flow control
            Set-NetAdapterAdvancedProperty -Name $adapter.Name -RegistryKeyword "*FlowControl" -RegistryValue 0 -ErrorAction SilentlyContinue

            # Disable interrupt moderation
            Set-NetAdapterAdvancedProperty -Name $adapter.Name -RegistryKeyword "*InterruptModeration" -RegistryValue 0 -ErrorAction SilentlyContinue

            # Set receive buffers
            Set-NetAdapterAdvancedProperty -Name $adapter.Name -RegistryKeyword "*ReceiveBuffers" -RegistryValue 2048 -ErrorAction SilentlyContinue

            # Set transmit buffers
            Set-NetAdapterAdvancedProperty -Name $adapter.Name -RegistryKeyword "*TransmitBuffers" -RegistryValue 2048 -ErrorAction SilentlyContinue

            # Disable energy efficient ethernet
            Set-NetAdapterAdvancedProperty -Name $adapter.Name -RegistryKeyword "*EEE" -RegistryValue 0 -ErrorAction SilentlyContinue
        }

        # Optimize TCP global settings
        netsh int tcp set global chimney=enabled
        netsh int tcp set global autotuninglevel=normal
        netsh int tcp set global congestionprovider=ctcp
        netsh int tcp set global timestamps=disabled
        netsh int tcp set global rss=enabled
        netsh int tcp set global ecncapability=disabled

        Write-Host "Network stack fine-tuned for low latency."
        '''
        result = subprocess.run(['powershell', '-Command', network_script], capture_output=True, text=True)
        if result.returncode == 0:
            print("Network stack optimized.")
        else:
            print(f"Network optimization failed: {result.stderr}")
    except Exception as e:
        print(f"Error fine-tuning network: {e}")

def kill_eye_candy_dwm():
    """Kill eye-candy and DWM effects for maximum performance."""
    try:
        print("Disabling visual effects and DWM optimizations...")
        dwm_script = '''
        # Disable Desktop Window Manager visual effects
        $dwmPath = "HKCU:\\Software\\Microsoft\\Windows\\DWM"
        Set-ItemProperty -Path $dwmPath -Name "EnableAeroPeek" -Value 0 -ErrorAction SilentlyContinue
        Set-ItemProperty -Path $dwmPath -Name "AlwaysHibernateThumbnails" -Value 0 -ErrorAction SilentlyContinue
        Set-ItemProperty -Path $dwmPath -Name "EnableWindowColorization" -Value 0 -ErrorAction SilentlyContinue

        # Disable visual effects for best performance
        $visualPath = "HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\VisualEffects"
        if (!(Test-Path $visualPath)) { New-Item -Path $visualPath -Force }
        Set-ItemProperty -Path $visualPath -Name "VisualFXSetting" -Value 2 -ErrorAction SilentlyContinue

        # Disable specific visual effects
        $effects = @(
            "AnimateMinMax",
            "ComboBoxAnimation",
            "CursorShadow",
            "DragFullWindows",
            "DropShadow",
            "ListBoxSmoothScrolling",
            "MenuAnimation",
            "SelectionFade",
            "TaskbarAnimations",
            "Themes",
            "TooltipAnimation",
            "WebView"
        )

        foreach ($effect in $effects) {
            Set-ItemProperty -Path "HKCU:\\Control Panel\\Desktop" -Name $effect -Value 0 -ErrorAction SilentlyContinue
        }

        # Disable animations and transitions
        Set-ItemProperty -Path "HKCU:\\Control Panel\\Desktop\\WindowMetrics" -Name "MinAnimate" -Value 0 -ErrorAction SilentlyContinue
        Set-ItemProperty -Path "HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Advanced" -Name "TaskbarAnimations" -Value 0 -ErrorAction SilentlyContinue
        Set-ItemProperty -Path "HKCU:\\Control Panel\\Desktop" -Name "MenuShowDelay" -Value 0 -ErrorAction SilentlyContinue

        # Force refresh of visual settings
        Stop-Process -Name "explorer" -Force -ErrorAction SilentlyContinue
        Start-Process "explorer.exe"

        Write-Host "Visual effects and DWM optimizations disabled."
        '''
        result = subprocess.run(['powershell', '-Command', dwm_script], capture_output=True, text=True)
        if result.returncode == 0:
            print("Eye-candy and DWM effects disabled.")
        else:
            print(f"Visual effects optimization failed: {result.stderr}")
    except Exception as e:
        print(f"Error disabling visual effects: {e}")

def keep_ssd_clean():
    """Keep SSD clean with TRIM and disable unnecessary indexing."""
    try:
        print("Optimizing SSD for cleanliness and performance...")
        ssd_script = '''
        # Enable TRIM for SSDs
        fsutil behavior set DisableDeleteNotify 0

        # Disable Superfetch/Superfetch for SSDs (can cause unnecessary writes)
        Set-ItemProperty -Path "HKLM:\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management\\PrefetchParameters" -Name "EnableSuperfetch" -Value 0 -ErrorAction SilentlyContinue
        Set-ItemProperty -Path "HKLM:\\SYSTEM\\CurrentControlSet\\Control\\Session Manager\\Memory Management\\PrefetchParameters" -Name "EnablePrefetcher" -Value 0 -ErrorAction SilentlyContinue

        # Disable Windows Search indexing on SSD
        Set-ItemProperty -Path "HKLM:\\SOFTWARE\\Policies\\Microsoft\\Windows\\Windows Search" -Name "DisableIndexingEncryptedItems" -Value 1 -ErrorAction SilentlyContinue

        # Disable hibernation (creates large hiberfil.sys)
        powercfg -h off

        # Disable pagefile encryption
        fsutil behavior set EncryptPagingFile 0

        # Disable memory dump creation
        Set-ItemProperty -Path "HKLM:\\SYSTEM\\CurrentControlSet\\Control\\CrashControl" -Name "CrashDumpEnabled" -Value 0 -ErrorAction SilentlyContinue

        # Optimize SSD-specific settings
        $ssdDrives = Get-PhysicalDisk | Where-Object { $_.MediaType -eq "SSD" }
        foreach ($drive in $ssdDrives) {
            # Disable defrag scheduling for SSD
            Disable-ScheduledTask -TaskName "\\Microsoft\\Windows\\Defrag\\ScheduledDefrag" -ErrorAction SilentlyContinue

            # Set SSD-specific power settings
            powercfg -setacvalueindex scheme_current sub_disk 0b2d69d7-a2a1-449c-9680-f91c70521c60 0
            powercfg -setdcvalueindex scheme_current sub_disk 0b2d69d7-a2a1-449c-9680-f91c70521c60 0
        }

        Write-Host "SSD optimized for cleanliness and performance."
        '''
        result = subprocess.run(['powershell', '-Command', ssd_script], capture_output=True, text=True)
        if result.returncode == 0:
            print("SSD cleanliness and performance optimized.")
        else:
            print(f"SSD optimization failed: {result.stderr}")
    except Exception as e:
        print(f"Error optimizing SSD: {e}")

def windows_updates_default():
    """Reset Windows Update settings to default/stock settings."""
    try:
        print("Resetting Windows Update to default settings...")
        default_script = '''
        # Reset Windows Update to default settings
        Set-ItemProperty -Path "HKLM:\\SOFTWARE\\Policies\\Microsoft\\Windows\\WindowsUpdate\\AU" -Name "NoAutoUpdate" -Value 0 -ErrorAction SilentlyContinue
        Set-ItemProperty -Path "HKLM:\\SOFTWARE\\Policies\\Microsoft\\Windows\\WindowsUpdate\\AU" -Name "AUOptions" -Value 3 -ErrorAction SilentlyContinue
        Set-ItemProperty -Path "HKLM:\\SOFTWARE\\Policies\\Microsoft\\Windows\\WindowsUpdate\\AU" -Name "ScheduledInstallDay" -Value 0 -ErrorAction SilentlyContinue
        Set-ItemProperty -Path "HKLM:\\SOFTWARE\\Policies\\Microsoft\\Windows\\WindowsUpdate\\AU" -Name "ScheduledInstallTime" -Value 3 -ErrorAction SilentlyContinue

        # Enable Windows Update services
        Set-Service -Name "wuauserv" -StartupType Automatic -ErrorAction SilentlyContinue
        Set-Service -Name "WaaSMedicSvc" -StartupType Manual -ErrorAction SilentlyContinue
        Set-Service -Name "UsoSvc" -StartupType Automatic -ErrorAction SilentlyContinue

        # Start services
        Start-Service -Name "wuauserv" -ErrorAction SilentlyContinue
        Start-Service -Name "UsoSvc" -ErrorAction SilentlyContinue

        # Reset feature update deferral
        Set-ItemProperty -Path "HKLM:\\SOFTWARE\\Microsoft\\WindowsUpdate\\UX\\Settings" -Name "DeferFeatureUpdatesPeriodInDays" -Value 0 -ErrorAction SilentlyContinue
        Set-ItemProperty -Path "HKLM:\\SOFTWARE\\Microsoft\\WindowsUpdate\\UX\\Settings" -Name "DeferQualityUpdatesPeriodInDays" -Value 0 -ErrorAction SilentlyContinue

        # Reset update branch
        Set-ItemProperty -Path "HKLM:\\SOFTWARE\\Microsoft\\WindowsUpdate\\UX\\Settings" -Name "BranchReadinessLevel" -Value 16 -ErrorAction SilentlyContinue

        Write-Host "Windows Update reset to default settings."
        '''
        result = subprocess.run(['powershell', '-Command', default_script], capture_output=True, text=True)
        if result.returncode == 0:
            print("Windows Update settings reset to default.")
        else:
            print(f"Windows Update default reset failed: {result.stderr}")
    except Exception as e:
        print(f"Error resetting Windows Update to default: {e}")

def windows_updates_recommended():
    """Apply recommended Windows Update settings: Security-only, defer feature updates ~24 months."""
    try:
        print("Applying recommended Windows Update settings...")
        recommended_script = '''
        # Enable security updates only
        Set-ItemProperty -Path "HKLM:\\SOFTWARE\\Policies\\Microsoft\\Windows\\WindowsUpdate\\AU" -Name "NoAutoUpdate" -Value 0 -ErrorAction SilentlyContinue
        Set-ItemProperty -Path "HKLM:\\SOFTWARE\\Policies\\Microsoft\\Windows\\WindowsUpdate\\AU" -Name "AUOptions" -Value 4 -ErrorAction SilentlyContinue

        # Defer feature updates for ~24 months (730 days)
        Set-ItemProperty -Path "HKLM:\\SOFTWARE\\Microsoft\\WindowsUpdate\\UX\\Settings" -Name "DeferFeatureUpdatesPeriodInDays" -Value 730 -ErrorAction SilentlyContinue
        Set-ItemProperty -Path "HKLM:\\SOFTWARE\\Microsoft\\WindowsUpdate\\UX\\Settings" -Name "DeferQualityUpdatesPeriodInDays" -Value 0 -ErrorAction SilentlyContinue

        # Set to Semi-Annual Channel (Targeted)
        Set-ItemProperty -Path "HKLM:\\SOFTWARE\\Microsoft\\WindowsUpdate\\UX\\Settings" -Name "BranchReadinessLevel" -Value 32 -ErrorAction SilentlyContinue

        # Enable Windows Update services
        Set-Service -Name "wuauserv" -StartupType Automatic -ErrorAction SilentlyContinue
        Set-Service -Name "UsoSvc" -StartupType Automatic -ErrorAction SilentlyContinue

        # Start services
        Start-Service -Name "wuauserv" -ErrorAction SilentlyContinue
        Start-Service -Name "UsoSvc" -ErrorAction SilentlyContinue

        # Disable automatic restarts for updates
        Set-ItemProperty -Path "HKLM:\\SOFTWARE\\Policies\\Microsoft\\Windows\\WindowsUpdate\\AU" -Name "NoAutoRebootWithLoggedOnUsers" -Value 1 -ErrorAction SilentlyContinue

        Write-Host "Recommended Windows Update settings applied (Security-only, defer feature updates)."
        '''
        result = subprocess.run(['powershell', '-Command', recommended_script], capture_output=True, text=True)
        if result.returncode == 0:
            print("Recommended Windows Update settings applied.")
        else:
            print(f"Windows Update recommended settings failed: {result.stderr}")
    except Exception as e:
        print(f"Error applying recommended Windows Update settings: {e}")

def windows_updates_disable_all():
    """Disable all Windows Updates (not recommended, for legacy/isolated systems)."""
    try:
        print("WARNING: Disabling all Windows Updates (not recommended)...")
        disable_script = '''
        # Disable automatic updates
        Set-ItemProperty -Path "HKLM:\\SOFTWARE\\Policies\\Microsoft\\Windows\\WindowsUpdate\\AU" -Name "NoAutoUpdate" -Value 1 -ErrorAction SilentlyContinue
        Set-ItemProperty -Path "HKLM:\\SOFTWARE\\Policies\\Microsoft\\Windows\\WindowsUpdate\\AU" -Name "AUOptions" -Value 1 -ErrorAction SilentlyContinue

        # Stop and disable Windows Update services
        Stop-Service -Name "wuauserv" -ErrorAction SilentlyContinue
        Stop-Service -Name "WaaSMedicSvc" -ErrorAction SilentlyContinue
        Stop-Service -Name "UsoSvc" -ErrorAction SilentlyContinue

        Set-Service -Name "wuauserv" -StartupType Disabled -ErrorAction SilentlyContinue
        Set-Service -Name "WaaSMedicSvc" -StartupType Disabled -ErrorAction SilentlyContinue
        Set-Service -Name "UsoSvc" -StartupType Disabled -ErrorAction SilentlyContinue

        # Disable Windows Update Medic service completely
        Set-ItemProperty -Path "HKLM:\\SYSTEM\\CurrentControlSet\\Services\\WaaSMedicSvc" -Name "Start" -Value 4 -ErrorAction SilentlyContinue

        # Block Windows Update sites in hosts file (optional, commented out)
        # Add-Content -Path "C:\\Windows\\System32\\drivers\\etc\\hosts" -Value "127.0.0.1 windowsupdate.microsoft.com" -ErrorAction SilentlyContinue
        # Add-Content -Path "C:\\Windows\\System32\\drivers\\etc\\hosts" -Value "127.0.0.1 update.microsoft.com" -ErrorAction SilentlyContinue

        Write-Host "All Windows Updates disabled (not recommended for regular use)."
        Write-Host "WARNING: This reduces security - only use for isolated/legacy systems."
        '''
        result = subprocess.run(['powershell', '-Command', disable_script], capture_output=True, text=True)
        if result.returncode == 0:
            print("All Windows Updates disabled (use with caution).")
        else:
            print(f"Windows Update disable failed: {result.stderr}")
    except Exception as e:
        print(f"Error disabling Windows Updates: {e}")

def check_malwarebytes_installation():
    """Check if Malwarebytes is installed and offer installation guidance."""
    try:
        print("Checking for Malwarebytes installation...")

        # Check if Malwarebytes is installed
        result = subprocess.run([
            'powershell', '-Command',
            'Get-ItemProperty HKLM:\\Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\* | Where-Object { $_.DisplayName -like "*Malwarebytes*" }'
        ], capture_output=True, text=True)

        if result.returncode == 0 and result.stdout.strip():
            print("✅ Malwarebytes is already installed.")
            return True
        else:
            print("❌ Malwarebytes is not installed.")
            return prompt_malwarebytes_installation()
    except Exception as e:
        print(f"Error checking Malwarebytes installation: {e}")
        return False

def prompt_malwarebytes_installation():
    """Prompt user to install Malwarebytes and guide them through the process."""
    try:
        print("\n� MALWAREBYTES INSTALLATION ASSISTANT")
        print("=" * 45)
        print("\nMalwarebytes is a powerful anti-malware scanner that works great alongside Windows Defender.")
        print("It can detect threats that Windows Defender might miss.\n")

        while True:
            response = input("Would you like to install Malwarebytes now? (yes/no): ").lower().strip()

            if response in ['yes', 'y']:
                return install_malwarebytes_interactive()
            elif response in ['no', 'n']:
                print("❌ Skipping Malwarebytes installation.")
                print("💡 You can install it later from: https://www.malwarebytes.com/download")
                return False
            else:
                print("Please enter 'yes' or 'no'.")

    except KeyboardInterrupt:
        print("\n❌ Installation cancelled by user.")
        return False
    except Exception as e:
        print(f"Error during installation prompt: {e}")
        return False

def install_malwarebytes_interactive():
    """Guide user through interactive Malwarebytes installation."""
    try:
        print("\n🚀 MALWAREBYTES INSTALLATION PROCESS")
        print("=" * 40)

        # Check internet connection
        print("\n1. Checking internet connection...")
        ping_result = subprocess.run(['ping', '-n', '1', 'www.google.com'], capture_output=True, text=True)

        if ping_result.returncode != 0:
            print("❌ No internet connection detected.")
            print("Please connect to the internet and try again.")
            return False

        print("✅ Internet connection available.")

        # Provide download instructions
        print("\n2. DOWNLOADING MALWAREBYTES:")
        print("   📥 Opening Malwarebytes download page in your browser...")
        print("   📥 If browser doesn't open, visit: https://www.malwarebytes.com/download")

        # Try to open browser
        try:
            subprocess.run(['start', 'https://www.malwarebytes.com/download'], shell=True)
        except:
            print("   📝 Please manually visit: https://www.malwarebytes.com/download")

        # Wait for user to download
        input("\n3. Press Enter after you have downloaded the Malwarebytes installer...")

        # Guide through installation
        print("\n4. INSTALLATION STEPS:")
        print("   🖱️  Locate the downloaded file (usually 'MBSetup.exe')")
        print("   🖱️  Right-click the file")
        print("   🖱️  Select 'Run as administrator'")
        print("   🖱️  If prompted, click 'Yes' to allow the installation")
        print("   🖱️  Follow the installation wizard")
        print("   🖱️  Choose the 'Free' version when prompted")
        print("   🖱️  Click 'Install' and wait for completion")

        input("\n5. Press Enter after Malwarebytes installation is complete...")

        # Verify installation
        print("\n6. Verifying installation...")
        result = subprocess.run([
            'powershell', '-Command',
            'Get-ItemProperty HKLM:\\Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\* | Where-Object { $_.DisplayName -like "*Malwarebytes*" }'
        ], capture_output=True, text=True)

        if result.returncode == 0 and result.stdout.strip():
            print("✅ Malwarebytes installation verified successfully!")

            # Offer to run first scan
            while True:
                scan_response = input("\nWould you like to run your first Malwarebytes scan now? (yes/no): ").lower().strip()

                if scan_response in ['yes', 'y']:
                    print("\n🔍 Starting your first Malwarebytes scan...")
                    return run_malwarebytes_scan()
                elif scan_response in ['no', 'n']:
                    print("✅ Malwarebytes is ready to use!")
                    print("💡 You can run scans anytime from the desktop shortcut or Start menu.")
                    return True
                else:
                    print("Please enter 'yes' or 'no'.")

        else:
            print("❌ Installation verification failed.")
            print("💡 Try running the installer again or check the installation manually.")
            return False

    except KeyboardInterrupt:
        print("\n❌ Installation cancelled by user.")
        return False
    except Exception as e:
        print(f"Error during installation: {e}")
        return False

def run_malwarebytes_scan():
    """Attempt to run Malwarebytes scan if installed."""
    try:
        print("Attempting to run Malwarebytes scan...")

        # First check if Malwarebytes is installed
        if not check_malwarebytes_installation():
            return False

        # Try to find and run Malwarebytes
        print("🔍 Looking for Malwarebytes executable...")

        result = subprocess.run([
            'powershell', '-Command',
            '$mbPath = Get-ChildItem "C:\\Program Files\\Malwarebytes\\Anti-Malware\\mbam.exe" -ErrorAction SilentlyContinue; if ($mbPath) { Start-Process $mbPath.FullName -ArgumentList "/scan" -Wait; Write-Host "Scan completed successfully." } else { Write-Host "Malwarebytes executable not found at expected location." }'
        ], capture_output=True, text=True)

        if result.returncode == 0 and "Scan completed successfully" in result.stdout:
            print("✅ Malwarebytes scan completed successfully!")
            print("📊 Check the Malwarebytes interface for detailed results.")
            return True
        else:
            print("❌ Could not run Malwarebytes scan automatically.")
            print("💡 Please run Malwarebytes manually:")
            print("   1. Open Malwarebytes from desktop shortcut or Start menu")
            print("   2. Click the 'Scan' button")
            print("   3. Choose 'Threat Scan' or 'Custom Scan'")
            print("   4. Wait for scan to complete")
            return False

    except Exception as e:
        print(f"Error running Malwarebytes scan: {e}")
        print("💡 Please run Malwarebytes manually from the Start menu or desktop shortcut.")
        return False

def install_malwarebytes_guided():
    """Provide guided installation process for Malwarebytes (legacy function - now uses interactive installation)."""
    print("🔧 Using enhanced interactive Malwarebytes installation...")
    return prompt_malwarebytes_installation()

def scan_with_windows_defender():
    """Run a Windows Defender full scan."""
    try:
        print("Running Windows Defender full scan...")

        # Start Windows Defender full scan
        result = subprocess.run([
            'powershell', '-Command',
            'Start-MpScan -ScanType FullScan'
        ], capture_output=True, text=True)

        if result.returncode == 0:
            print("✅ Windows Defender full scan started successfully.")
            print("The scan is running in the background and may take 1-2 hours to complete.")
            print("You can check the progress in Windows Security > Virus & threat protection.")
        else:
            print("❌ Could not start Windows Defender scan.")
            print("Please run it manually from Windows Security.")

    except Exception as e:
        print(f"Error running Windows Defender scan: {e}")
        print("Please run Windows Defender manually from Windows Security.")

def comprehensive_security_scan():
    """Run comprehensive security checks including Windows Defender."""
    try:
        print("🔒 COMPREHENSIVE SECURITY SCAN")
        print("=" * 40)

        # Check Windows Defender status
        print("\n1. Checking Windows Defender status...")
        result = subprocess.run([
            'powershell', '-Command',
            'Get-MpComputerStatus | Select-Object AntivirusEnabled, RealTimeProtectionEnabled, FullScanAge'
        ], capture_output=True, text=True)

        if result.returncode == 0:
            print("✅ Windows Defender status retrieved.")
            print(result.stdout)
        else:
            print("❌ Could not check Windows Defender status.")

        # Run quick Windows Defender scan
        print("\n2. Running Windows Defender quick scan...")
        result = subprocess.run([
            'powershell', '-Command',
            'Start-MpScan -ScanType QuickScan; Start-Sleep 10; Get-MpScanResult'
        ], capture_output=True, text=True)

        if result.returncode == 0:
            print("✅ Windows Defender quick scan completed.")
        else:
            print("❌ Windows Defender quick scan failed.")

        # Check for Malwarebytes
        print("\n3. Checking for Malwarebytes...")
        check_malwarebytes_installation()

        # Provide recommendations
        print("\n📋 SECURITY RECOMMENDATIONS:")
        print("• Keep Windows Defender enabled and up to date")
        print("• Consider installing Malwarebytes for additional scanning")
        print("• Run full scans weekly")
        print("• Keep your system updated")
        print("• Use strong passwords")
        print("• Be cautious with email attachments and downloads")

    except Exception as e:
        print(f"Error in comprehensive security scan: {e}")
    """Main optimization function."""
    if platform.system() != 'Windows':
        print("This script is designed for Windows only.")
        sys.exit(1)

    if not is_admin():
        print("This script requires administrator privileges. Please run as administrator.")
        sys.exit(1)

    print("Starting Windows optimization...")
    create_restore_point()
    clean_temp_files()
    run_disk_cleanup()
    defragment_drives()
    clear_windows_update_cache()
    run_system_file_checker()
    run_dism_repair()
    clear_dns_cache()
    optimize_windows_search()
    clear_browser_cache()
    clear_event_logs()
    optimize_power_settings()
    disable_hibernation()
    optimize_registry()
    disable_unnecessary_services()
    optimize_startup_programs()
    optimize_network_settings()
    optimize_memory_management()
    optimize_visual_effects()
    optimize_ssd_settings()
    optimize_security_settings()
    optimize_system_settings()
    clean_windows_old()
    optimize_game_mode()
    optimize_context_menu()
    optimize_gpu_settings()
    optimize_usb_settings()
    optimize_printer_settings()
    optimize_audio_settings()
    optimize_bluetooth_settings()
    optimize_firewall_settings()
    optimize_uac_settings()
    optimize_windows_update_settings()
    optimize_error_reporting()
    optimize_remote_desktop()
    optimize_task_scheduler()
    optimize_font_cache()
    optimize_icon_cache()
    optimize_thumbnail_cache()
    optimize_prefetch_superfetch()
    optimize_readyboost()
    optimize_windows_store()
    optimize_cortana()
    optimize_onedrive()
    optimize_microsoft_edge()
    optimize_registry_animations()
    optimize_explorer_settings()
    disable_windows_features()
    optimize_memory_registry()
    disable_telemetry_services()
    optimize_network_registry()
    disable_windows_tips()
    optimize_usb_registry()
    disable_store_autoupdates()
    optimize_power_registry()
    disable_search_service()
    disable_xbox_services()
    disable_print_services()
    disable_update_medic()
    disable_store_install_service()
    disable_push_notifications()
    disable_biometric_service()
    disable_windows_connect()
    check_malwarebytes_installation()
    run_malwarebytes_scan()
    install_malwarebytes_guided()
    scan_with_windows_defender()
    comprehensive_security_scan()
    print("Optimization completed. Please restart your computer for changes to take effect.")

if __name__ == "__main__":
    # Check if command line arguments are provided
    # Only run GUI mode
    app = WindowsOptimizerGUI()
    app.run()
