import socket


def run_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server_socket.bind((host, port))

    # Listen for incoming connections
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}...")

    while True:
        # Accept a client connection
        client_socket, client_address = server_socket.accept()
        print(f"Accepted connection from {client_address[0]}:{client_address[1]}")

        message = 0xcacbcccd02ff080000022daa370250050008021295aa000000000501080000139e553a02000782080002dee2000100000783060000000000000783020001078507018a6468955400078305ffff00000e20eaebeced
        client_socket.send(message.encode())
        client_socket.close()


if __name__ == '__main__':
    run_server('127.0.0.1', 1234)
