#!/usr/bin/env python3
import socket, sys, time

# Usage: python udp_client.py <server_ip>
if len(sys.argv) != 2:
    print("Usage: udp_client.py <server_ip>")
    sys.exit(1)
srv_ip = sys.argv[1]

msg = b"hello UDP"
addr = (srv_ip, 53344)
N = 1000

# Create UDP socket and warm ARP cache once
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    # Start timing just before the first send
    t1 = time.monotonic()
    for _ in range(N):
        sock.sendto(msg, addr)
        _ = sock.recvfrom(1024)
    # Stop timing immediately after the last recv
    t2 = time.monotonic()

# Compute and print total RTT in milliseconds
total_ms = (t2 - t1) * 1000
print(f"UDP: sent/recv {N} msgs in {total_ms:.3f} ms")
