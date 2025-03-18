#!/usr/bin/env python3

import os
import socket

SOCKET_PATH = "/tmp/my_socket"

# Удаляем старый сокет, если он остался
if os.path.exists(SOCKET_PATH):
    os.remove(SOCKET_PATH)

# Создаем UNIX-сокет
server = socket.socket( socket.AF_UNIX, socket.SOCK_STREAM )
# Привязка (только для серверов) — указываем адрес (IP и порт) или путь к файлу (для UNIX-сокетов).
server.bind(SOCKET_PATH)
# Переводим сокет в режим ожидания подключений
server.listen()
print("Сервер ожидает соединения...")
# Ожидание подключения от клиента — принятие подключения
conn, _ = server.accept() # -> (socket object, address info)
print("Клиент подключился!")
# Получение данных (буфер 1024 байт)
data = conn.recv(1024)
print("Получено:", data.decode())
# Получение данных всем клиентам
conn.sendall(b"Hello from server!")
# закрываем соединение
conn.close()
server.close()

