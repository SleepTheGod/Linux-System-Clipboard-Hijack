#!/usr/bin/python3
print("Clipboard Hijacking Made By Taylor Christian Newsome")
print("Taylor.ChristianNewsome@OWASP.org")
print("Twitter.com/ClumsyLulz")
try:
    import subprocess
except ImportError:
    print("Unable to import subprocess library! Please install it: `sudo apt install python3-subprocess`")
    exit(1)

def get_system_info():
    """Gets system uptime and package count (non-root version)."""
    commands = ["uptime -p", "dpkg-query -f 'c' | wc -l"]
    output = []
    for command in commands:
        # Execute and capture single line output
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output_line, errors = process.communicate()

        # Check for errors
        if process.returncode != 0:
            print(f"Error during {command}: {errors.decode('utf-8')}")
            return None

        output.append(output_line.decode("utf-8").strip())

    return "\n".join(output)

def write_to_clipboard(text):
    """Writes text to the clipboard (no xclip)."""
    # Fallback to `echo` and redirection if xclip is missing
    try:
        process = subprocess.Popen(["echo", text], stdout=subprocess.PIPE)
        process.communicate(input="/dev/clipboard")
        print("System info written to clipboard! Use Ctrl+V to paste.")
    except Exception as e:
        print(f"Couldn't write to clipboard: {e}")
        return False
    return True

def main():
    """Runs the script and handles results."""
    system_info = get_system_info()
    if system_info is None:
        return

    if write_to_clipboard(system_info):
        print("System info copied to clipboard! Check uptime and package count.")
    else:
        print("Couldn't copy info to clipboard. Please check your system setup.")

if __name__ == "__main__":
    main()
