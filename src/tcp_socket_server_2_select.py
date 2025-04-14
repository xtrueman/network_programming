#!/usr/bin/env python3

"""Простой TCP-сервер: использование системного вызова select"""
import socket
import select

HOST = 'localhost'
PORT = 12345

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


serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

serv_sock.bind((HOST, PORT))
serv_sock.listen(1)
inputs = [serv_sock]
outputs = []

while True:
    print("Waiting for connections or data...")
    readable, writeable, _ = select.select(inputs, outputs, inputs)
    for sock in readable:
        if sock == serv_sock:
            sock, addr = serv_sock.accept() # Should be ready
            print("Connected by", addr)
            inputs.append(sock)
        else: # Client socket
            addr = sock.getpeername()
            if not handle(sock, addr): # Disconnected                
                inputs.remove(sock)
                if sock in outputs:
                    outputs.remove(sock)
                sock.close()

serv_sock.close(1)
