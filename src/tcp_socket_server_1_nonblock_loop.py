#!/usr/bin/env python3

"""TCP-сервер: Неблокирующие сокеты + бесконечный цикл проверки"""
import socket

HOST = 'localhost'
PORT = 12345

serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_sock.bind((HOST, PORT))
serv_sock.listen(1)
serv_sock.setblocking(False)  # Important!

connections = []

while True:
    try:
        # print("Try to accept a new connection...")
        sock, addr = serv_sock.accept()
        sock.setblocking(False)
        print("Connected by", addr)
        connections.append((sock, addr))
    except BlockingIOError:
        # print("No connections are waiting to be accepted")
        pass

    for sock, addr in connections.copy():
        print("Try to receive data from:", sock, addr)
        try:
            data = sock.recv(1024)
        except ConnectionError:
            print(f"Client suddenly closed while receiving from {addr}")
            connections.remove((sock, addr))
            sock.close()
            continue
        except BlockingIOError:
            # No data received
            continue
        print(f"Received: {data} from: {addr}")
        if not data:
            connections.remove((sock, addr))
            sock.close()
            print("Disconnected by", addr)
            continue
        data = data.upper()
        print(f"Send: {data} to: {addr}")
        try:
            sock.sendall(data)
        except ConnectionError:
            print(f"Client suddenly closed, cannot send to {addr}")
            connections.remove((sock, addr))
            sock.close()
            continue
