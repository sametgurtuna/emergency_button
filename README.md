# 🚨 Emergency Button

This project was originally created by **Mert** (mertpalaoglu1), who got bored during his internship and built this to have some fun without getting caught slacking.

I forked and improved it by adding configurable hotkey and file path settings, along with a modern UI and more flexible shortcut management.  
Now you can set your own hotkey and file to open instantly whenever you need to "pretend working."

---

## 📌 How to Use

1. **Open your terminal**  
2. Navigate to the project folder:  
   ```bash
   cd "your-folder-path"
   ```  
3. Start the script:  
   ```bash
   python emergency_button.py
   ```  
4. Hide the terminal window.  
5. **Go wild.**

*(The terminal will keep running in the background while the hotkey listener stays active.)*

---

## 🛠 Requirements

- **Python 3.7+**  
- **keyboard** module:  
  ```bash
  pip install keyboard
  ```  
- **PyQt6** (if you use the PyQt6 UI version):  
  ```bash
  pip install PyQt6
  ```  
- **customtkinter** (if you use the customtkinter UI version):  
  ```bash
  pip install customtkinter
  ```

---
