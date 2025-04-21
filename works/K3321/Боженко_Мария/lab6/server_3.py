import socket


def start_http_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.bind(('localhost', 8080))

    server_socket.listen(1)
    print("HTTP сервер запущен. Ожидание подключения...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Подключено к {addr}")

        request = client_socket.recv(1024).decode('utf-8')
        print(f"Получени запрос:\n {request}")

        try:
            with open('index.html', 'r') as file:
                response_body = file.read()
            response_status = 'HTTP/1.1 200 OK\r\n'
        except FileNotFoundError:
            response_body = '<h1>404 Not Found :(</h1>'
            response_status = 'HTTP/1.1 404 Not Found\r\n'

        response_headers = 'Content-Type: text/html; charset=utf-8\r\n'
        response_headers += 'Content-Length: {}\r\n'.format(len(response_body))
        response_headers += '\r\n'

        client_socket.sendall(response_status.encode('utf-8'))
        client_socket.sendall(response_headers.encode('utf-8'))
        client_socket.sendall(response_body.encode('utf-8'))

        client_socket.close()


if __name__ == '__main__':
    start_http_server()
