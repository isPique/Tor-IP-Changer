
# Auto Change Tor IP

This tool automates the process of periodically changing the Tor IP address.  
Basically, it enters a loop where it continuously fetches a new IP address through Tor proxies.  
Restart the Tor service, and you got a new IP :D

> **IMPORTANT**  
> This version of the tool is supported on both Linux and Windows operating systems.

## Features
- Automatic Tor IP address change.
- Supports both Linux and Windows.
- Requires Tor service to be running.

## Installation

### Linux

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

4. Install Tor (if not already installed):

   For Ubuntu/Debian-based systems, run:

   ```bash
   sudo apt update
   sudo apt install tor
   ```

5. Run the script with root privileges:

    ```bash
    sudo python3 IP-Changer.py
    ```

### Windows

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

4. Install Tor:

   Download and install Tor from the official website: [Tor Browser Download](https://www.torproject.org/download/)

   After installing, you should be able to start the Tor service.

5. Run the script:

    Open Command Prompt (CMD) and navigate to the directory where the script is located, then run:

    ```bash
    python IP-Changer.py
    ```

## Usage

1. The script will automatically detect your operating system (Linux or Windows) and run the appropriate version.
2. Once the script is running, it will periodically change your Tor IP address.
3. The IP address will be changed at the interval you specify (in seconds).
4. To stop the script, press `Ctrl + C` in the terminal.

## Additional Information

- On Linux, you may need to run the script with `sudo` privileges to interact with the Tor service.
- On Windows, make sure that the Tor service is running and accessible. If you face issues, ensure that the Tor executable is correctly set up in your system's PATH.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Screenshot

![Terminal](https://github.com/isPique/Tor-IP-Changer/blob/main/Terminal.jpg)
