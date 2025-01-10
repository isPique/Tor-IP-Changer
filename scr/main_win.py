import subprocess
import requests
import time
import sys
import os

if os.name != 'nt':
    sys.exit("This tool can only run on Windows!")

def display_banner():
    os.system('cls')  # Clears screen on Windows
    DEFAULT, GREEN, RED, YELLOW, YELLOW2, ITALIC, BLINK = '\033[0m', '\033[1;92m', '\033[1;31m', '\033[1;33m', '\033[1;93m', '\033[3m', '\033[5m'

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
                    {3}{5}Version: {2}1.0{2}                                      {3}{5}Code Author: {2}isPique
                  {1}{5}================                                   {1}{5}======================
  
                                 {3}{5}GitHub Profile {2}{6}:{0}{1} https://github.com/isPique{0}
          '''.format(DEFAULT, GREEN, RED, YELLOW, YELLOW2, ITALIC, BLINK))

def install_tor():
    tor_installed = subprocess.run(["where", "tor"], stdout=subprocess.PIPE, stderr=subprocess.PIPE).returncode == 0
    if not tor_installed:
        print("\033[1;91m[!]\033[1;93m Tor is not installed. Please install Tor from https://www.torproject.org/ and ensure it's added to your PATH.\033[0m")
        return False
    return True

def main():
    url = "https://httpbin.org/ip"
    proxy = {
        'http': 'socks5://127.0.0.1:9050',
        'https': 'socks5://127.0.0.1:9050'
    }

    try:
        print("\033[1;34m[*] Checking if Tor is installed...\033[0m")
        time.sleep(1)
        if not install_tor():
            return
        else:
            print("\033[1;92m[+] Tor is already installed.\033[0m")
            time.sleep(1)

        display_banner()

        try:
            version_info = subprocess.run("tor --version", capture_output=True, text=True, shell=True)
            version = version_info.stdout.split('\n')[0].split(' ')[2]
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
        tor_status = subprocess.run(["tasklist", "/FI", "imagename eq tor.exe"], capture_output=True, text=True, shell=True)
        if "tor.exe" in tor_status.stdout:
            print("\033[1;92m[+] Tor is already running.\033[0m")
        else:
            print("\033[1;93m[-] Tor is not running.\033[0m")
            print("\033[1;34m[*] Starting Tor service...\033[0m")
            subprocess.run("start tor", shell=True)
            time.sleep(3)

        while True:
            try:
                response = requests.get(url, proxies=proxy)
                changed_ip = response.json().get('origin')
                print(f"\033[1;92m[+] Your IP has been changed to {changed_ip}\033[0m")
            except Exception:
                print(f"\033[1;91m[-] Error!\033[1;93m Failed to change IP. Retrying...\033[0m")

            time.sleep(time_interval)
            subprocess.run("start tor", shell=True)

    except KeyboardInterrupt:
        print("\n\033[1;91m[!]\033[1;93m Exiting...\033[0m")
        print("\033[1;34m[*] Stopping Tor service...\033[0m")
        subprocess.run("taskkill /IM tor.exe /F", shell=True)

if __name__ == '__main__':
    main()
