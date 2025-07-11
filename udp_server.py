#!/usr/bin/env python3
import socket

HOST, PORT = '0.0.0.0', 53444
with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as srv:
    srv.bind((HOST, PORT))
    print(f"[UDP] Listening on {HOST}:{PORT}")
    while True:
        data, addr = srv.recvfrom(1024)
        print(f"[UDP] Got {data!r} from {addr}")
        srv.sendto(b"back at you UDP", addr)
