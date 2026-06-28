import nmap


def scan_target(target):
    scanner = nmap.PortScanner()

    print("\nScanning... Please wait.\n")

    try:
        scanner.scan(hosts=target, arguments="-A")

        for host in scanner.all_hosts():
            print("=" * 50)
            print(f"Host: {host}")
            print(f"State: {scanner[host].state()}")

            for protocol in scanner[host].all_protocols():
                print(f"\nProtocol: {protocol}")

                ports = scanner[host][protocol].keys()

                for port in sorted(ports):
                    state = scanner[host][protocol][port]['state']
                    service = scanner[host][protocol][port]['name']

                    print(f"Port {port:<5} {state:<8} Service: {service}")

            print("=" * 50)

    except Exception as e:
        print("Error:", e)