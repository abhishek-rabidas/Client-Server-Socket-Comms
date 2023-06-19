import socket


def send_string_over_socket(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the server
        client_socket.connect((host, port))
        response = client_socket.recv(1024)

        print("Received response:", response.decode())

    except ConnectionRefusedError:
        print("Connection refused. Make sure the server is running.")
    except Exception as e:
        print("An error occurred:", str(e))

    # Close the socket
    client_socket.close()


# Set the host and port of the server
server_host = 'localhost'
server_port = 1234

if __name__ == '__main__':
    send_string_over_socket(server_host, server_port)
