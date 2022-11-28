import socket
import sys , subprocess
import os,time
host = ""
port = 50000


def ipconfig():
    print ("Your OS is ", sys.platform)
    if sys.platform == 'win32':
        print (os.system("ipconfig"))
    elif sys.platform == 'linux2':
        print (os.system("ifconfig"))
    time.sleep(5)


def ram():
    cmd = str(subprocess.check_output("wmic computersystem get totalphysicalmemory.", shell=True))
    return cmd

def Os():
    cmd=sys.platform
    if cmd == "win32":
        print("voici l'OS de votre pc")
        cmd= str(subprocess.check_output("ver", shell=True))
        return cmd

def server():
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




if __name__ == '__main__':
    server()


