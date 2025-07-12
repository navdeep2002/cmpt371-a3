#!/usr/bin/env python3
import socket, sys, time

# Usage: python tcp_client.py <server_ip>
if len(sys.argv) != 2:
    print("Usage: tcp_client.py <server_ip>")
    sys.exit(1)
srv_ip = sys.argv[1]

# Establish TCP connection once (not timed)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((srv_ip, 53333))

    msg = b"hello TCP"
    N = 1000

    # Start timing just before the first send
    t1 = time.monotonic()
    for _ in range(N):
        s.sendall(msg)
        _ = s.recv(1024)
    # Stop timing immediately after the last recv
    t2 = time.monotonic()

# Compute and print total RTT in milliseconds
total_ms = (t2 - t1) * 1000
print(f"TCP: sent/recv {N} msgs in {total_ms:.3f} ms")