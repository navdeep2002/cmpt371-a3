#!/usr/bin/env python3
import socket

HOST, PORT = '0.0.0.0', 53333
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as srv:
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind((HOST, PORT))
    srv.listen(1)
    print(f"[TCP] Listening on {HOST}:{PORT}")
    conn, addr = srv.accept()
    with conn:
        print(f"[TCP] Connection from {addr}")
        while True:
            data = conn.recv(1024)
            if not data: break
            conn.sendall(b"back at you TCP")
