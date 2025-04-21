import socket


def start_client():

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_socket.connect(('localhost', 12345))

    request = client_socket.recv(1024).decode('utf-8')
    print(f"Получено сообщение от сервера: \033[30;44m{request}\033[0m")

    message = input("Введите сообщение для сервера: ")
    client_socket.send(message.encode('utf-8'))

    request = client_socket.recv(1024).decode('utf-8')
    print(f"Получено сообщение от сервера: \033[30;44m{request}\033[0m")

    message = input("Введите сообщение для сервера: ")
    client_socket.send(message.encode('utf-8'))

    response = client_socket.recv(1024).decode('utf-8')
    print(f"Получен ответ от сервера: \033[30;44m{response}\033[0m")

    client_socket.close()


if __name__ == "__main__":
    start_client()
