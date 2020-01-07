#!/usr/bin/env python

import socket
import threading

TCP_PORT = 7884
BUFFER_SIZE = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', TCP_PORT))
print("listening...")
s.listen(5)

def handle_inputs(conn, connections):
    data = conn.recv(BUFFER_SIZE)
    print("received:", data)
    namelist.append(data)
    for c in connections:
        c.sendall(",".join(namelist))
        print("sending", namelist, c)


connections = []
namelist = []

while True:
    conn, addr = s.accept()
    connections.append(conn)
    client_handler = threading.Thread(target=handle_inputs, args=(conn, connections,))
    client_handler.start()
