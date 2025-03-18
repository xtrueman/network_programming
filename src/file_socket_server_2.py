#!/usr/bin/env python3

import socket

SOCKET_PATH = "/tmp/my_socket"
# (Удаляем старый сокет, если он остался)

# Создаем объект UNIX-сокета
server = socket.socket( socket.AF_UNIX, socket.SOCK_STREAM )
# Привязка (только для серверов) — указываем адрес (IP и порт) или путь к файлу (для UNIX-сокетов).
server.bind(SOCKET_PATH)
# Переводим сокет в режим ожидания подключений
server.listen()
print("Сервер ожидает соединения...")
# Ожидание подключения от клиента — принятие подключения
conn, addr = server.accept() # -> (socket object, address info)
print(f"Клиент подключился!")
# Получение данных (буфер 1024 байт)
data = conn.recv(1024)
print("Получено:", data.decode())
# Получение данных всем клиентам
conn.sendall(b"Hello from server!")
# закрываем соединение
conn.close()
server.close()
