server_socket.bind("/tmp/my_socket")     # UNIX-сокет
server_socket.bind(("localhost", 12345)) # адрес хоста в виде домена
server_socket.bind(("my-org.ru", 12345)) # адрес хоста в виде домена
server_socket.bind(("127.0.0.1", 12345)) # адрес хоста в виде IP
server_socket.bind(("0.0.0.0", 12345))   # на всех доступных интерфейсах!
