from scanner import scan_target

def menu():
    print("=" * 60)
    print("       NMAP NETWORK DISCOVERY TOOL")
    print("=" * 60)

    target = input("Enter Target IP or Hostname: ")

    print("\nSelect Scan Type")
    print("1. Ping Scan")
    print("2. Fast Scan")
    print("3. Service Detection")
    print("4. OS Detection")
    print("5. Aggressive Scan")

    choice = input("\nEnter Choice: ")

    scan_target(target, choice)

menu()