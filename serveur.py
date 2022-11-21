import socket

def server():

    host = ""
    port = 5100

    server_socket = socket.socket()

    server_socket.bind((host, port))

    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))


    while True:

        data = conn.recv(1024).decode()
        if data == 'bye':
            conn.close()
            server_socket.close()

            break
        print("from connected user: " + str(data))
        data = input(' -> ')
        conn.send(data.encode())
    conn.close()

    while True :
        data = conn.recv(1024).decode()
        if data == 'arret':
            server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server_socket.bind((host, port))
            print("serveur reset ")
            break


if __name__ == '__main__':
    server()
