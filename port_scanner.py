import socket
import sys

COMMON_PORTS = [22, 80, 443, 8080, 3306, 5432]

def scan_ports(target_ip):
    print(f"Scanning {target_ip} for common open ports...")
    for port in COMMON_PORTS:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.settimeout(1)
            result = sock.connect_ex((target_ip, port))
            if result == 0:
                print(f"Port {port} is OPEN")
            else:
                print(f"Port {port} is closed")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python port_scanner.py <target_ip>")
        sys.exit(1)

    scan_ports(sys.argv[1])
