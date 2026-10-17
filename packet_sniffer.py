from scapy.all import sniff, IP, TCP, UDP, ICMP


def analyze_packet(packet):
    if IP not in packet:
        return

    ip = packet[IP]
    print("\n--- Packet Captured ---")
    print(f"Source IP: {ip.src}")
    print(f"Destination IP: {ip.dst}")

    if TCP in packet:
        print("Protocol: TCP")
        print(f"Source Port: {packet[TCP].sport}")
        print(f"Destination Port: {packet[TCP].dport}")
    elif UDP in packet:
        print("Protocol: UDP")
        print(f"Source Port: {packet[UDP].sport}")
        print(f"Destination Port: {packet[UDP].dport}")
    elif ICMP in packet:
        print("Protocol: ICMP")
    else:
        print(f"IP Protocol Number: {ip.proto}")


print("Starting localhost packet capture...")
print("Waiting for 10 IP packets. Press Ctrl+C to stop early.\n")

sniff(
    iface="Software Loopback Interface 1",
    filter="udp and host 127.0.0.1 and port 9999",
    prn=analyze_packet,
    count=1,
    store=False,
)

print("\nCapture complete!")