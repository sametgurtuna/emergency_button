# 🚨 Emergency Button

This project was originally created by **Mert** (mertpalaoglu1), who got bored during his internship and built this to have some fun without getting caught slacking.

I forked and improved it by adding configurable hotkey and file path settings, along with a modern UI and more flexible shortcut management.  
Now you can set your own hotkey and file to open instantly whenever you need to "pretend working."

---

## 📌 How to Use (Python Script)

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

## 🛠 Requirements (for Python Script)

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

## 🚀 How to Use the Executable (.exe) Version

If you don’t want to install Python or dependencies, you can use the standalone executable version:

1. Download the `emergency_button.exe` file from the [GitHub Releases](https://github.com/your-repo-link/releases).  
2. Run the `.exe` file (preferably **as Administrator** to enable hotkey support).  
3. Configure your file path and hotkey in the UI window.  
4. Hide the application window and press your configured hotkey anytime to instantly open your chosen file.  

### Notes for Executable

- The executable includes all required dependencies bundled inside.  
- Running as Administrator is recommended because the hotkey listener requires elevated permissions.  
- Some antivirus software (like Windows Defender) may flag the `.exe` as suspicious — this is a false positive.  
- If hotkeys don’t work, make sure you run the executable with admin rights.

---

Thanks for checking out **Emergency Button**! Feel free to open issues or contribute.
