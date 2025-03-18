#!/usr/bin/env python3

import socket

# Создаем UNIX-сокет
client = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
# Соединяемся с файл-сокетом
client.connect("/tmp/my_socket")
# Посылаем данные
client.sendall(b"Hello from client!")
# Получаем данные
data = client.recv(1024)
print("Ответ от сервера:", data.decode())
# Закрываем сокет
client.close()
