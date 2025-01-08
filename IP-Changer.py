import os
import sys
import main_win
import main_linux


def run_windows_script():
    print("Running Windows script...")
    main_win.main()

def run_linux_script():
    print("Running Linux script...")
    main_linux.main()

def main():
    if os.name == 'nt':
        # Якщо Windows
        run_windows_script()
    elif os.name == 'posix':
        # Якщо Linux
        run_linux_script()
    else:
        print("Unsupported operating system")
        sys.exit(1)

if __name__ == '__main__':
    main()