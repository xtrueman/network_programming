#!/usr/bin/env python3

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("Send Buffer:", s.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF))
print("Receive Buffer:", s.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF))