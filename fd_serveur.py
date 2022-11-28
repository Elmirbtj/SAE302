import socket

host = ""
port = 50001

message = ""
while message != "kill":
    # A refaire si reset
    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(1)

    while message != "kill" and message != "reset":
        # A refaire si disconnect
        print('En attente du client')
        conn, address = server_socket.accept()
        print(f'Client connecté {address}')

        while message != "kill" and message != "reset" and message !="disconect":
            # Réception du message du client
            msgb = conn.recv(1024)  # message en by
            message = msgb.decode()
            print(f"Message du client : {message}")

            # J'envoie un message
            #reply = input("Saisir un message : ")
            conn.send(message.encode())
            print(f"Message {message} envoyé")




server_socket.close()
print("Fermeture de la socket serveur")
