# Ultimate Port Scanner 🚀

A high-speed, multithreaded TCP port scanner written purely in Python. This tool works like a custom Nmap engine, utilizing Python's native `socket` and `threading` libraries to scan all 65,535 ports in mere seconds.

## Features
- **Insanely Fast:** Uses 100 concurrent threads to scan all 65,535 ports in under 10 seconds.
- **CLI Integration:** Takes the target IP directly from the command line for a seamless hacker-like experience.
- **Precision:** Calculates and displays the exact total time taken for the scan.
- **Zero Dependencies:** Built entirely with Python's standard built-in libraries.

## How to Use
1. Clone this repository:
   `git clone https://github.com/pranjal211025/Ultimate-Port-Scanner.git`
2. Navigate to the directory:
   `cd Ultimate-Port-Scanner`
3. Run the scanner with a target IP:
   `python3 scanner.py <Target-IP>`
   *(Example: `python3 scanner.py 127.0.0.1`)*

*Disclaimer: Created for educational purposes and ethical hacking only.*
