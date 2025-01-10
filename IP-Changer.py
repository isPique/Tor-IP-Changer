import os
import sys
from scr import main_win
from scr import main_linux


def run_windows_script():
    print("Running Windows script...")
    main_win.main()

def run_linux_script():
    print("Running Linux script...")
    main_linux.main()

def main():
    if os.name == 'nt':
        run_windows_script()
    elif os.name == 'posix':
        run_linux_script()
    else:
        print("Unsupported operating system")
        sys.exit(1)

if __name__ == '__main__':
    main()
