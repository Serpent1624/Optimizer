# Windows Optimizer GUI Test
# Run this to test the GUI without running actual optimizations

import tkinter as tk
from tkinter import ttk, messagebox
import sys
import platform

class TestGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Windows Optimizer - GUI Test")
        self.root.geometry("600x400")

        # Create test interface
        frame = ttk.Frame(self.root, padding="20")
        frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        title = ttk.Label(frame, text="GUI Test Mode", font=("Arial", 16, "bold"))
        title.grid(row=0, column=0, pady=(0, 20))

        info = ttk.Label(frame, text="This is a test of the GUI interface.\n"
                      "No optimizations will be performed.", font=("Arial", 10))
        info.grid(row=1, column=0, pady=(0, 20))

        # Test buttons
        test_btn = ttk.Button(frame, text="Test Message Box",
                             command=self.test_message)
        test_btn.grid(row=2, column=0, pady=(0, 10))

        progress_btn = ttk.Button(frame, text="Test Progress Bar",
                                 command=self.test_progress)
        progress_btn.grid(row=3, column=0, pady=(0, 10))

        # System info
        sys_info = f"Platform: {platform.system()}\n"
        sys_info += f"Python: {sys.version.split()[0]}\n"
        sys_info += "GUI: tkinter loaded successfully"

        info_label = ttk.Label(frame, text=sys_info, font=("Consolas", 9),
                              background="lightgray", padding=10)
        info_label.grid(row=4, column=0, pady=(20, 0))

        # Center window
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')

    def test_message(self):
        messagebox.showinfo("Test", "GUI is working correctly!\n\n"
                          "The interface loaded successfully and\n"
                          "message boxes are functional.")

    def test_progress(self):
        # Create progress window
        progress_window = tk.Toplevel(self.root)
        progress_window.title("Progress Test")
        progress_window.geometry("300x150")

        ttk.Label(progress_window, text="Testing Progress Bar...",
                 font=("Arial", 10)).pack(pady=10)

        progress = ttk.Progressbar(progress_window, mode='determinate',
                                  maximum=100, length=200)
        progress.pack(pady=10)

        # Simulate progress
        for i in range(101):
            progress['value'] = i
            progress_window.update_idletasks()
            self.root.after(20)

        ttk.Label(progress_window, text="Progress test completed!",
                 font=("Arial", 9, "bold")).pack(pady=5)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = TestGUI()
    app.run()
