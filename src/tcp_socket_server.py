#!/usr/bin/env python3

# Простой TCP-сервер
import socket

LISTEN_PORT = 12345
# Создаем сокет с использованием IPv4 (AF_INET) и TCP (SOCK_STREAM)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Разрешаем повторное использование порта
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# Привязываем сокет к адресу и порту
server_socket.bind(('localhost', LISTEN_PORT))

# Начинаем прослушивать входящие соединения (максимум 1 в очереди)
server_socket.listen(1)
print(f"Сервер ожидает подключение на порту {LISTEN_PORT}...")

# Принимаем соединение от клиента
conn, addr = server_socket.accept()
print(f"Подключение от {addr}")

# Получаем данные от клиента
data = conn.recv(1024)
print(f"Получено: {data.decode()}")

# Отправляем ответ клиенту
conn.sendall("Привет от сервера!".encode())

# Закрываем соединение
conn.close()  # Закрываем соединение с клиентом
server_socket.close()  # Закрываем серверный сокет

# Пояснение:
# - socket() создаёт новый TCP-сокет.
# - bind() привязывает сокет к локальному адресу и порту.
# - listen() переводит сокет в режим ожидания подключений.
# - accept() блокирует выполнение до тех пор, пока клиент не подключится.
# - recv() читает данные, отправленные клиентом.
# - sendall() отправляет данные клиенту.
# - close() закрывает соединение.