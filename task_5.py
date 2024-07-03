from scapy.all import sniff, IP, TCP, UDP, Raw

def packet_callback(packet):
    """
    packet (scapy.packet.Packet): The captured packet.
    """
    # Checking if the packet has an IP layer
    if IP in packet:
        ip_layer = packet[IP]
        print(f"\n[+] New Packet: {packet.summary()}")
        print(f"Source IP: {ip_layer.src}")
        print(f"Destination IP: {ip_layer.dst}")
        
        # Checking if the packet has a TCP layer
        if TCP in packet:
            tcp_layer = packet[TCP]
            print(f"Protocol: TCP")
            print(f"Source Port: {tcp_layer.sport}")
            print(f"Destination Port: {tcp_layer.dport}")
            # Check if the TCP packet has a payload
            if Raw in tcp_layer:
                print(f"Payload: {tcp_layer[Raw].load}")
        
        # Checking if the packet has a UDP layer
        elif UDP in packet:
            udp_layer = packet[UDP]
            print(f"Protocol: UDP")
            print(f"Source Port: {udp_layer.sport}")
            print(f"Destination Port: {udp_layer.dport}")
            # Check if the UDP packet has a payload
            if Raw in udp_layer:
                print(f"Payload: {udp_layer[Raw].load}")

def main():
    print("Starting packet sniffer...")
    # Start sniffing with the packet_callback function
    sniff(prn=packet_callback, store=False)

if __name__ == "__main__":
    main()
