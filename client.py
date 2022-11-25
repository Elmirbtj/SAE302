import socket


class client():
    host = socket.gethostname()
    port = 5100

    client_socket = socket.socket()
    client_socket.connect((host, port))

    message = input(" -> ")


    while message != 'byye':
        client_socket.send(message.encode())
        data = client_socket.recv(1024).decode()

        print('Received from server:  ' + data)
        if data == 'bye':
            client_socket.close()
            break

        message = input(" -> ")

    client_socket.close()



if __name__ == '__main__':
    client()