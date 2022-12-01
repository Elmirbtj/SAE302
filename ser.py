from threading import Thread
import socket
import sys , subprocess
import os,time

class ser():
    def Send(client):
        while True:
            client.send(input("Ecrit ton message :").encode('utf8'))
    def Reception(client):
        while True:
            req = client.recv(5000).decode('utf8')
            if not req:
                break
            print("client envoie :",req)

    def server():
        Host = ""
        Port = 10000
        message = ""
        while message != "kill":
            # A refaire si reset
            server_socket = socket.socket()
            server_socket.bind((Host, Port))
            server_socket.listen(1)

            while message != "kill" and message != "reset":
                # A refaire si disconnect
                print('En attente du client')
                conn, address = server_socket.accept()
                print(f'Client connecté {address}')

                while message != "kill" and message != "reset" and message != "disconect":
                    # Réception du message du client
                    msgb = conn.recv(1024)  # message en by
                    messagee = msgb.decode()
                    print(f"Message du client : {messagee}")

                    # J'envoie un message
                    # reply = input("Saisir un message : ")
                    message = input("Message au serveur : ")
                    conn.send(message.encode())
                    print(f"Message {message} envoyé")
        server_socket.close()
        print("Fermeture de la socket serveur")






    Host = ""
    Port = 10000

    server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    server_socket.bind((Host,Port))
    server_socket.listen(1)


    client, addrs = server_socket.accept()
    server = Thread(target=server)
    envoi = Thread(target=Send,args=[client])
    recep = Thread(target=Reception,args=[client])
    envoi.start()
    server.start()
    recep.start()

    recep.join()
    server.join()

    print('fin thread')
    client.close()
    server_socket.close()























if __name__ == '__main__':
    ser()