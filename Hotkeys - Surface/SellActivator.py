import subprocess

print("test")
# Path to the AutoHotkey executable
ahk_exe = r'C:/Users/ewokr/OneDrive/Desktop/Hotkeys/SellBTC.exe'

# Path to the AutoHotkey script to execute
ahk_script = r'C:/Users/ewokr/OneDrive/Desktop/Hotkeys/SellBTC.ahk'

# Execute the AutoHotkey script
subprocess.Popen([ahk_exe, ahk_script])