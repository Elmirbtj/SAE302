from threading import Thread
import socket

def Send(client):
    while True:
        client.send(input("Ecrit ton message :").encode('utf8'))
def Reception(client):
    while True:
        req = client.recv(5000).decode('utf8')
        if not req:
            break
        print("client envoie :",req)


Host = ""
Port = 1000

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

server.bind((Host,Port))
server.listen(1)


client, addrs = server.accept()

envoi = Thread(target=Send,args=[client])
recep = Thread(target=Reception,args=[client])
envoi.start()
recep.start()

recep.join()

print('fin thread')
client.close()
server.close()