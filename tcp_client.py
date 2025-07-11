#!/usr/bin/env python3
import socket, sys, time

if len(sys.argv)!=2:
    print("Usage: tcp_client.py <server_ip>"); sys.exit(1)
srv_ip = sys.argv[1]

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((srv_ip, 53333))
    t1 = time.monotonic()
    s.sendall(b"Hello TCP")
    reply = s.recv(1024)
    t2 = time.monotonic()

print(f"Received: {reply.decode()}")
print(f"TCP RTT = {(t2-t1)*1000:.3f} ms")
