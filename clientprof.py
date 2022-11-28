import socket

host = "127.0.0.1"
port = 50000


def client():


    print(f"Ouverture de la socket sur le serveur {host} port {port}")

    client_socket = socket.socket()
    client_socket.connect((host, port))

    print("Serveur est connecté")


    message =""

    while True:


        message = input("Message au serveur : ")
        client_socket.send(message.encode())
        print(f"Message envoyé {message}")

        data = client_socket.recv(1024).decode()
        print(f"Message du serveur : {data}")
        if data == "kill" or data == "reset" or data == "disconect":
            break
    # Fermeture de la socket du client
    client_socket.close()
    print("Socket fermée")



if __name__ == '__main__':
    client()
