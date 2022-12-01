import socket

host = "127.0.0.1"
port = 5001



def client():


    print(f"Ouverture de la socket sur le serveur {host} port {port}")

    client_socket = socket.socket()
    client_socket.connect((host, port))

    print("Serveur est connecté")


    message =""

    while message != "reset" and message != "disconect":


        message = input("Message au serveur : ")
        client_socket.send(message.encode())
        print(f"Message envoyé {message}")


        data = client_socket.recv(1000).decode()
        print(f"Message du serveur : {data}")

    # Fermeture de la socket du client
    client_socket.close()
    print("Socket fermée")


"""message = input(" -> ")
client_socket.send(message.encode())
print("Message envoyé")
reponse = client_socket.recv(10000).decode()
print(f'{host} > {reponse}')"""


if __name__ == '__main__':
    client()
