import subprocess

print("test")
# Path to the AutoHotkey executable
ahk_exe = r'[PATH]'

# Path to the AutoHotkey script to execute
ahk_script = r'[PATH]'

# Execute the AutoHotkey script
subprocess.Popen([ahk_exe, ahk_script])
