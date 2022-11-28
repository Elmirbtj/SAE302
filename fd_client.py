import socket

host = "127.0.0.1"
port = 50001

reply = ""


print(f"Ouverture de la socket sur le serveur {host} port {port}")
client_socket = socket.socket()
client_socket.connect((host, port))
print("Serveur est connecté")


message = input("Message au serveur : ")
client_socket.send(message.encode())
print("Message envoyé")
data = client_socket.recv(1024).decode()
print(f"Message du serveur : {data}")



