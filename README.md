# Nmap Network Discovery Tool

## Overview

This project is a Python-based Network Discovery Tool that uses Nmap to scan a target IP address or hostname. The application is developed in Visual Studio Code and managed with Git and GitHub.

## Features

- Scan an IP address or hostname
- Display host status
- Detect open ports
- Identify running services
- Command-line interface
- Git version control

## Technologies Used

- Python 3
- Nmap
- python-nmap
- Visual Studio Code
- Git
- GitHub

## Project Structure

```
nmap-network-discovery-project/
│
├── main.py
├── scanner.py
├── README.md
├── report.md
├── commands.md
├── findings.md
├── LICENSE
├── scans/
├── screenshots/
└── results/
```

## Installation

```bash
pip install python-nmap
```

Install Nmap on your system and ensure it is added to your system PATH.

## Run

```bash
python main.py
```

## Example

```
Enter Target IP Address:
192.168.1.1
```

The application scans the target and displays the detected host status, ports, and services.

## Author

Faisal Boota