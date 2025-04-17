# The basic OS info script in python works on both Windows and Linux OS

import os
import platform
import subprocess
from pathlib import Path

def main():
    # 1. Current working directory
    print(f"\nCurrent directory: {os.getcwd()}")

    # 2. Current user
    print(f"\nCurrent user: {os.getlogin()}")

    # 3. OS and version
    print(f"\nOS: {platform.system()} {platform.release()}")

    # 4. Check firewall status (Windows/Linux)
    print("\nFirewall status:")
    try:
        if platform.system() == "Windows":
            subprocess.run(["netsh", "advfirewall", "show", "allprofiles"], check=True)
        else:
            subprocess.run(["sudo", "ufw", "status"], check=True)
    except Exception as e:
        print(f"Could not check firewall: {e}")

    # 5. List items in current directory
    print("\nCurrent directory items:")
    for item in os.listdir():
        print(f" - {item}")

    # 6. List txt files in specific directory (example: Documents)
    target_dir = os.path.expanduser("~/Documents")
    print(f"\nTXT files in {target_dir}:")
    try:
        for file in Path(target_dir).glob("*.txt"):
            print(f" - {file.name}")
    except Exception as e:
        print(f"Error accessing directory: {e}")

    # 7. Create and remove directory
    test_dir = "test_directory"
    print(f"\nCreating directory: {test_dir}")
    os.makedirs(test_dir, exist_ok=True)
    
    print(f"Removing directory: {test_dir}")
    try:
        os.rmdir(test_dir)
    except OSError as e:
        print(f"Error removing directory: {e}")

    # 8. Basic security check
    print("\nBasic security checks:")
    print(f"Running as admin: {os.geteuid() == 0 if platform.system() != 'Windows' else 'N/A'}")
    print(f"Environment variables: {', '.join(os.environ.keys())}")

if __name__ == "__main__":
    main()
