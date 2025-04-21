import socket


def start_server():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)
    print("Сервер запущен. Ожидание подключения...")

    client_socket, addr = server_socket.accept()
    print(f"Подключено к {addr}")

    message = client_socket.recv(1024).decode('utf-8')
    print(f"Получено сообщение от клиента: {message}")

    response = "Hello, client!"
    client_socket.send(response.encode('utf-8'))

    client_socket.close()
    server_socket.close()


if __name__ == "__main__":
    start_server()
