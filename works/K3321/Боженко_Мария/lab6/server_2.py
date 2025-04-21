import socket


def start_server():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)
    print("Сервер запущен. Ожидание подключения...")

    client_socket, addr = server_socket.accept()
    print(f"Подключено к \033[30;45m{addr}\033[0m")

    request = "Уважаемый пользователь, выбери формулу: 1 - через высоту и основание; 2 - через синус"
    client_socket.send(request.encode('utf-8'))

    message = client_socket.recv(1024).decode('utf-8')
    print(f"Получено сообщение от клиента: \033[30;45m{message}\033[0m")

    if message == "1":
        request = "Уважаемый пользователь, введи основание и высоту ЧЕРЕЗ ПРОБЕЛ"
        client_socket.send(request.encode('utf-8'))

        message = client_socket.recv(1024).decode('utf-8')
        print(f"Получено сообщение от клиента: \033[30;45m{message}\033[0m")

        a, h = message.split()
        s = int(a) * int(h)

        response = f"Площадь данного параллелограмма равна {s}"
        client_socket.send(response.encode('utf-8'))
    else:
        request = "Уважаемый пользователь, введи синус и два основания ЧЕРЕЗ ПРОБЕЛ"
        client_socket.send(request.encode('utf-8'))

        message = client_socket.recv(1024).decode('utf-8')
        print(f"Получено сообщение от клиента: \033[30;45m{message}\033[0m")

        sin, a, b = message.split()
        s = float(sin) * int(a) * int(b)

        response = f"Площадь данного параллелограмма равна {s}"
        client_socket.send(response.encode('utf-8'))

    client_socket.close()
    server_socket.close()


if __name__ == "__main__":
    start_server()
