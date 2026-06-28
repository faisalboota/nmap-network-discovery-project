from scanner import scan_target

def main():
    print("=" * 60)
    print("      NMAP NETWORK DISCOVERY TOOL")
    print("=" * 60)

    while True:
        print("\nMenu")
        print("1. Scan Target")
        print("2. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            target = input("Enter Target IP or Hostname: ")
            scan_target(target)

        elif choice == "2":
            print("\nThank you for using Nmap Network Discovery Tool.")
            break

        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()