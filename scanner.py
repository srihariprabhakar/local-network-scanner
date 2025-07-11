from scapy.all import ARP, Ether, srp

def scan_network(target_ip):
    arp = ARP(pdst=target_ip)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    result = srp(packet, timeout=3, verbose=0)[0]

    print("IP\t\tMAC Address")
    print("-" * 40)
    for sent, received in result:
        print(f"{received.psrc}\t{received.hwsrc}")

if __name__ == "__main__":
    subnet = "192.168.1.0/24"
    scan_network(subnet)
