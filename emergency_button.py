import keyboard
import os
import time
# açmak istediğimiz dosyanın yolu 
file_path = r"projectpath"

def open_file():
    print("[*] Panic mode activated — opening cover file...")
    os.startfile(file_path)

print("Listening for F9... (press ESC to quit)")

# arkaplanda F9 tuşuna basıldığında open_file fonksiyonunu çağır
keyboard.add_hotkey('F9', open_file)

# keyboard interrupt gelene kadar dinlemeye devam et
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Exiting...")
