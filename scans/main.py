from scanner import scan_target

print("=" * 40)
print(" Nmap Network Discovery Tool ")
print("=" * 40)

target = input("Enter Target IP Address: ")

scan_target(target)