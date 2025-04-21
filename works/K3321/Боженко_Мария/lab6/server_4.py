import socket
import threading

HOST = '127.0.0.1'
PORT = 12345

clients = []


def handle_client(client_socket, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                print(f"[{addr}] {message}")
                broadcast(message, client_socket)
            else:
                remove(client_socket)
                break
        except:
            continue


def broadcast(message, client_socket):
    for client in clients:
        if client != client_socket:
            try:
                client.send(message.encode('utf-8'))
            except:
                remove(client)


def remove(client_socket):
    if client_socket in clients:
        clients.remove(client_socket)


def start():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((HOST, PORT))
    server_socket.listen(5)
    print("[SERVER STARTED] Waiting for connections...")

    while True:
        client_socket, addr = server_socket.accept()
        clients.append(client_socket)
        thread = threading.Thread(target=handle_client, args=(client_socket, addr))
        thread.start()


if __name__ == "__main__":
    start()
