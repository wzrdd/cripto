import sys
import time
import random
from scapy.all import *

def generate_icmp_request(seq, identifier, char):
    timestamp = int(time.time()).to_bytes(4, byteorder='big') + b'\x00\x00\x00\x00'
    random_bytes = bytes([random.randint(0, 255) for _ in range(2)])
    data_field = timestamp + random_bytes + char.encode() + b'\x00\x00\x00\x00\x00' + bytes([i for i in range(0x10, 0x38)])
    icmp_packet = IP(dst='8.8.8.8') / ICMP(id=identifier, seq=seq) / data_field
    return icmp_packet

def main():
    if len(sys.argv) != 2:
        print("Usage: python icmp_storm.py <string>")
        sys.exit(1)

    input_string = sys.argv[1]
    identifier = random.randint(1, 65535)

    for seq, char in enumerate(input_string, start=1):
        icmp_packet = generate_icmp_request(seq, identifier, char)
        send(icmp_packet, verbose=False)
        time.sleep(1)  # Delay between sending packets (you can adjust this)

if __name__ == "__main__":
    main()
