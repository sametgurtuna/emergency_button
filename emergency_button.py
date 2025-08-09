import os
import json
import threading
import keyboard
import customtkinter as ctk
from tkinter import filedialog, messagebox

CONFIG_FILE = "panic_config.json"
current_hotkey = None

# ==========================
# Config Handling
# ==========================
def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    return {"file_path": "", "hotkey": "F9"}

def save_config(config):
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f)

# ==========================
# Panic Function
# ==========================
def open_file(path):
    if path and os.path.exists(path):
        print(f"[*] Panic mode activated — opening {path}")
        os.startfile(path)
    else:
        print(f"[!] Invalid file path: {path}")

# ==========================
# Hotkey Handling
# ==========================
def set_hotkey(hotkey, file_path):
    global current_hotkey
    if current_hotkey:
        try:
            keyboard.remove_hotkey(current_hotkey)
        except KeyError:
            pass
    current_hotkey = keyboard.add_hotkey(hotkey, lambda: open_file(file_path))
    print(f"[*] Listening for {hotkey}... (Press ESC to quit)")

def hotkey_listener_thread(config):
    set_hotkey(config["hotkey"], config["file_path"])
    keyboard.wait()

# ==========================
# UI
# ==========================
class PanicUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("🔥 Panic Button — Settings")
        self.geometry("450x250")
        
        ctk.set_appearance_mode("dark")  # "light" or "dark"
        ctk.set_default_color_theme("blue")
        
        self.config_data = load_config()
        
        # Title
        self.label_title = ctk.CTkLabel(self, text="⚡ Panic Button Settings", font=ctk.CTkFont(size=20, weight="bold"))
        self.label_title.pack(pady=(15, 5))
        
        self.label_desc = ctk.CTkLabel(self, text="Choose a file and hotkey to open it instantly in panic mode.")
        self.label_desc.pack(pady=(0, 15))
        
        # File selection row
        self.frame_file = ctk.CTkFrame(self)
        self.frame_file.pack(fill="x", padx=20, pady=(0, 10))
        
        self.label_file = ctk.CTkLabel(self.frame_file, text=self.config_data["file_path"] or "No file selected", wraplength=250)
        self.label_file.pack(side="left", padx=10, pady=10)
        
        self.btn_file = ctk.CTkButton(self.frame_file, text="📂 Select File", command=self.select_file)
        self.btn_file.pack(side="right", padx=10, pady=10)
        
        # Hotkey settings
        self.frame_hotkey = ctk.CTkFrame(self)
        self.frame_hotkey.pack(fill="x", padx=20, pady=(0, 10))
        
        self.entry_hotkey = ctk.CTkEntry(self.frame_hotkey, placeholder_text="Example: ctrl+alt+p")
        self.entry_hotkey.insert(0, self.config_data["hotkey"])
        self.entry_hotkey.pack(side="left", padx=10, pady=10, fill="x", expand=True)
        
        self.btn_apply = ctk.CTkButton(self.frame_hotkey, text="✅ Apply", command=self.apply_settings)
        self.btn_apply.pack(side="right", padx=10, pady=10)
    
    def select_file(self):
        file_path = filedialog.askopenfilename(title="Select File", filetypes=[("All Files", "*.*")])
        if file_path:
            self.config_data["file_path"] = file_path
            self.label_file.configure(text=file_path)
    
    def apply_settings(self):
        hotkey = self.entry_hotkey.get().strip()
        if not hotkey:
            messagebox.showwarning("Error", "Hotkey cannot be empty!")
            return
        if not self.config_data["file_path"]:
            messagebox.showwarning("Error", "Please select a file first!")
            return
        
        self.config_data["hotkey"] = hotkey
        save_config(self.config_data)
        set_hotkey(hotkey, self.config_data["file_path"])
        messagebox.showinfo("Success", "Settings applied successfully!")

# ==========================
# Main Program
# ==========================
if __name__ == "__main__":
    config = load_config()
    threading.Thread(target=hotkey_listener_thread, args=(config,), daemon=True).start()
    
    app = PanicUI()
    app.mainloop()
