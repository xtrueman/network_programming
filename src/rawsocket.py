#!/usr/bin/env python3
import socket

# Создаём raw-сокет
s = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_TCP)

while True:
    packet = s.recvfrom(65565)[0]  # Получаем "сырой" пакет
    print(f"Received {len(packet)} bytes: {packet[:20].hex()}")