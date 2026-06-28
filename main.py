from scanner import scan_target

print("=" * 50)
print("      NMAP NETWORK DISCOVERY TOOL")
print("=" * 50)

ip = input("Enter Target IP Address: ")

scan_target(ip)