import subprocess
import requests
import time
import sys
import os

if os.name not in ['nt', 'posix']:
    sys.exit("This tool only supports Linux and Windows!")

def display_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    DEFAULT, GREEN, RED, YELLOW, YELLOW2, ITALIC = '\033[0m', '\033[1;92m', '\033[1;31m', '\033[1;33m', '\033[1;93m', '\033[3m'

    print('''
{4} █████ ███████████       █████████  █████   █████   █████████   ██████   █████   █████████  ██████████ ███████████{0}
{4}░░███ ░░███░░░░░███     ███░░░░░███░░███   ░░███   ███░░░░░███ ░░██████ ░░███   ███░░░░░███░░███░░░░░█░░███░░░░░███{0}
{4} ░███  ░███    ░███    ███     ░░░  ░███    ░███  ░███    ░███  ░███░███ ░███  ███     ░░░  ░███  █ ░  ░███    ░███{0}
{4} ░███  ░██████████    ░███          ░███████████  ░███████████  ░███░░███░███ ░███          ░██████    ░██████████{0}
{4} ░███  ░███░░░░░░     ░███          ░███░░░░░███  ░███░░░░░███  ░███ ░░██████ ░███    █████ ░███░░█    ░███░░░░░███{0}
{4} ░███  ░███           ░░███     ███ ░███    ░███  ░███    ░███  ░███  ░░█████ ░░███  ░░███  ░███ ░   █ ░███    ░███{0}
{4} █████ █████           ░░█████████  █████   █████ █████   █████ █████  ░░█████ ░░█████████  ██████████ █████   █████{0}
{4}░░░░░ ░░░░░             ░░░░░░░░░  ░░░░░   ░░░░░ ░░░░░   ░░░░░ ░░░░░    ░░░░░   ░░░░░░░░░  ░░░░░░░░░░ ░░░░░   ░░░░░{0}

                  {1}{5}================                                   {1}{5}======================
                    {3}{5}Version: {2}2.0{2}                                      {3}{5}Code Author: {2}isPique
                  {1}{5}================                                   {1}{5}======================

                                 {3}{5}GitHub Profile {2}:{0}{1} https://github.com/isPique{0}
          '''.format(DEFAULT, GREEN, RED, YELLOW, YELLOW2, ITALIC))

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    if os.name == 'posix' and os.geteuid() != 0:
        print("\033[1;91m[!]\033[1;93m This script must be run with root privileges.\033[0m")
        return
    else:
        tor_process = None
        tor_url = "https://archive.torproject.org/tor-package-archive/torbrowser/14.0.4/tor-expert-bundle-windows-x86_64-14.0.4.tar.gz"
        filename = "tor.tar.gz"
        default_extract_path = "tor_path.txt"

    url = "https://httpbin.org/ip"
    proxy = {
        'http': 'socks5://127.0.0.1:9050',
        'https': 'socks5://127.0.0.1:9050'
    }

    try:
        print("\033[1;34m[*] Checking if Tor is installed...\033[0m")
        time.sleep(1)
        if os.name == 'posix':
            if subprocess.run(['which', 'tor'], stdout = subprocess.PIPE, stderr = subprocess.PIPE).returncode != 0:
                print("\033[1;91m[!]\033[1;93m Tor is not installed. Installing it...\033[0m")
                if os.system("sudo apt install tor -y > /dev/null 2>&1"):
                    print("\033[1;91m[!]\033[1;93m Failed to install Tor!\n\033[1;91m[!]\033[1;93m Please check your network connection.\033[0m")
                    return False
                else:
                    print("\033[1;92m[+] Tor has been successfully installed.\033[0m")
                    time.sleep(1)
            else:
                print("\033[1;92m[+] Tor is already installed.\033[0m")
                time.sleep(1)
        elif os.name == 'nt':
            with open(default_extract_path, "r") as f:
                extract_path = f.read().strip()
            tor_path = f"{extract_path}\\Tor Expert Bundle\\tor\\tor.exe"

            if not os.path.exists(tor_path):
                print("\033[1;91m[!]\033[1;93m Tor is not installed.\033[0m")
                import urllib.request
                import tarfile

                try:
                    print(f"\033[1;34m[*] Downloading latest stable Tor version from '{tor_url}'")
                    urllib.request.urlretrieve(tor_url, filename)
                    print("\033[1;92m[+] Download complete.\033[0m")
                except urllib.error.HTTPError as err:
                    sys.exit(f"\033[1;91m[-] HTTP Error {err.code}: {err.reason}\033[0m")

                user_choice = input(f"\033[1;92m[>] The script will extract Tor to the '{extract_path}' by default. Do you want to change it? (y/N) \xBB\033[0m\033[1;77m ").strip().lower()
                if user_choice in ['n', 'no']:
                    print(f"\033[1;34m[*] Extracting Tor to the default directory '{extract_path}\\Tor Expert Bundle'...")
                elif user_choice in ['y', 'yes']:
                    extract_path = input("\033[1;92m[>] Enter the desired extraction directory:\033[0m\033[1;77m ").strip()
                    if not os.path.exists(extract_path):
                        sys.exit(f"\033[1;93m[!] The path '{extract_path}' does not exist.\033[0m")
                    elif not os.access(extract_path, os.W_OK):
                        sys.exit(f"\033[1;91m[-] The path '{extract_path}' is not writable. Please choose another location.\033[0m")
                else:
                    sys.exit("\033[1;91m[-] Invalid choice.\033[0m")
                try:
                    with tarfile.open(filename, "r:gz") as tar:
                        tar.extractall(f"{extract_path}\\Tor Expert Bundle", filter='fully_trusted')
                    os.remove(filename)
                    print(f"\033[1;92m[+] Tor has been successfully extracted to the '{extract_path}\\Tor Expert Bundle'\033[0m")
                    with open(default_extract_path, "w") as f:
                        f.write(extract_path)
                    time.sleep(3)
                except tarfile.ReadError:
                    sys.exit("\033[1;91m[-] The file is not a valid tar archive or is corrupted.\033[0m")
            else:
                print("\033[1;92m[+] Tor is already installed.\033[0m")
                time.sleep(1)
            tor_path = f'{extract_path}\\Tor Expert Bundle\\tor\\tor.exe'
        display_banner()

        try:
            if os.name == 'posix':
                version = os.popen("tor --version").read().strip().split('\n')[0].split(' ')[2]
                print(f"\033[1;34m[*] Your Tor version is: {version}\033[0m")
            elif os.name == 'nt':
                version = subprocess.run([tor_path, "--version"], capture_output=True, text=True, check=True).stdout.splitlines()[0].split(" ")[2]
                print(f"\033[1;34m[*] Your Tor version is: {version}\033[0m")
        except Exception:
            pass

        try:
            response = requests.get(url)
            current_ip = response.json()["origin"]
            print(f"\033[1;34m[*] Your current IP address is: {current_ip}\033[0m")
        except:
            pass

        try:
            time_interval = int(input("\033[1;92m[>] How often do you want to change your IP? (in seconds) \xBB\033[0m\033[1;77m "))
            if time_interval <= 0:
                raise Exception

        except Exception:
            print("\033[1;91m[!]\033[1;93m Time interval must be a positive integer.\033[0m")
            return

        print(f"\033[1;91m[!]\033[1;93m Your IP address will be changed every {time_interval} seconds until you stop the script!")
        print("\033[1;91m[!]\033[1;93m Press Ctrl + C to stop.")
        time.sleep(1)

        print("\033[1;34m[*] Checking for Tor connection...\033[0m")
        if os.name == 'posix':
            if "Active: active" in subprocess.run(["sudo", "service", "tor", "status"], capture_output=True, text=True).stdout:
                print("\033[1;92m[+] Tor is already running.\033[0m")
            else:
                print("\033[1;93m[-] Tor is not running. Starting Tor service...\033[0m")
                subprocess.run("sudo service tor start", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                time.sleep(3)
        elif os.name == 'nt':
            if "tor.exe" in subprocess.run(["tasklist"], capture_output=True, text=True).stdout:
                print("\033[1;92m[+] Tor is already running.\033[0m")
            else:
                print("\033[1;93m[-] Tor is not running. Starting Tor...\033[0m")
                tor_process = subprocess.Popen([tor_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                time.sleep(3)

        while True:
            try:
                response = requests.get(url, proxies=proxy)
                changed_ip = response.json().get('origin')
                print(f"\033[1;92m[+] Your IP has been changed to {changed_ip}\033[0m")
            except Exception:
                print(f"\033[1;91m[-] Error!\033[1;93m Failed to change IP. Retrying...\033[0m")

            time.sleep(time_interval)
            if os.name == 'posix':
                subprocess.run("sudo service tor reload", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            elif os.name == 'nt':
                subprocess.run(['taskkill', '/F', '/IM', 'tor.exe'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                subprocess.Popen([tor_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    except KeyboardInterrupt:
        print("\n\033[1;91m[!]\033[1;93m Exiting...\033[0m")
        if os.name == 'posix' and "Active: active" in subprocess.run(["sudo", "service", "tor", "status"], capture_output=True, text=True).stdout:
            print("\033[1;34m[*] Stopping Tor service...\033[0m")
            subprocess.run("sudo service tor stop", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        elif os.name == 'nt' and tor_process:
            print("\033[1;34m[*] Stopping Tor service...\033[0m")
            tor_process.kill()

if __name__ == '__main__':
    main()
