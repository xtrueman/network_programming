#!/usr/bin/env python3
"""
Socket server using Selector and callbacks.
"""

import socket
import selectors

HOST, PORT = ('localhost', 12345)

def handle(sock, addr):
    try:
        data = sock.recv(1024)  # Should be ready
    except ConnectionError:
        print(f"Client suddenly closed while receiving")
        return False
    print(f"Received {data} from: {addr}")
    if not data:
        print("Disconnected by", addr)
        return False
    data = data.upper()
    print(f"Send: {data} to: {addr}")
    try:
        sock.send(data)  # Hope it won't block
    except ConnectionError:
        print(f"Client suddenly closed, cannot send")
        return False
    return True


def on_accept_ready(sel, serv_sock, mask):
    sock, addr = serv_sock.accept()  # Should be ready
    print("Connected by", addr)
    # sock.setblocking(False)
    sel.register(sock, selectors.EVENT_READ, on_read_ready)


def on_read_ready(sel, sock, mask):
    addr = sock.getpeername()
    if not handle(sock, addr):
        sel.unregister(sock)
        sock.close()


serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_sock.bind((HOST, PORT))
serv_sock.listen(1)
# serv_sock.setblocking(False)
print("Server started")

sel = selectors.DefaultSelector()
sel.register(serv_sock, selectors.EVENT_READ, on_accept_ready)
while True:
    print("Waiting for connections or data...")
    events = sel.select()
    for key, mask in events:
        callback = key.data
        callback(sel, key.fileobj, mask)

serv_sock.close()
