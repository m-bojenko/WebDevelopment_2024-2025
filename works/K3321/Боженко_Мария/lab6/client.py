import socket


def start_client():

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client_socket.connect(('localhost', 12345))

    message = "Hello, server! :)"
    # message = input("Введите сообщение для сервера: ")
    client_socket.send(message.encode('utf-8'))

    response = client_socket.recv(1024).decode('utf-8')
    print(f"Получен ответ от сервера: {response}")

    client_socket.close()


if __name__ == "__main__":
    start_client()
