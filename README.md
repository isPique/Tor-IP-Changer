# Auto Change Tor IP

* This tool automates the process of periodically changing the Tor IP address.
* Basically it enters a loop where it continuously fetches a new IP address through Tor proxies.
* Restart tor service, and you got a new IP :D

> [!IMPORTANT]
> This version of the tool is currently supported only on Unix-like operating systems.

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/isPique/Tor-IP-Changer.git
    ```

2. Navigate to the project directory:

    ```bash
    cd Tor-IP-Changer
    ```

3. Install required libraries:

   ```bash
   pip install -r requirements.txt
   ```

4. Run the script:

    ```bash
    sudo python3 IP-Changer.py
    ```
<br>

![Terminal](https://github.com/isPique/Tor-IP-Changer/blob/main/Terminal.jpg)
