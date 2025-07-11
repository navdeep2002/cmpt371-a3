#!/usr/bin/env python3
import socket, sys, time

if len(sys.argv)!=2:
    print("Usage: udp_client.py <server_ip>"); sys.exit(1)
srv_ip = sys.argv[1]

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    t1 = time.monotonic()
    s.sendto(b"Hello UDP",(srv_ip,53444))
    data, _ = s.recvfrom(1024)
    t2 = time.monotonic()

print(f"Received: {data.decode()}")
print(f"UDP RTT = {(t2-t1)*1000:.3f} ms")
