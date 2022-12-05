import socket
from threading import Thread

import time


m_kill = "kill"
m_disconnect = "disconnect"
m_reset = "reset"

host = "localhost"
port = 5006

message_client = ""
class server:
    def __init__(self):

        self.server = socket.socket()
        self.server.bind((host, port))
        self.server.listen(5)

        self.li = []
        self.di = {}
        self.get_con()

    def get_con(self):
        while True:
            try:
                con, addr = self.server.accept()
                data = 'La connexion est réussie !'
                con.send(data.encode())
                Thread(target=self.get_msg, args=(con, self.li, self.di, addr)).start()
                self.li.append(con)
            except:
                pass

    def get_msg(self, con, li, di, addr):
        name="dfdf"
        di[addr] = name
        while True:
            try:
                redata = con.recv(1024).decode()
                #print("Connection de",redata)
            except Exception as e:
                print("", e)
                self.close_client(con, addr)
                break
            if (redata.lower() == "quit"):
                self.close_client(con, addr)
                break
            if (redata.lower() == "reset"):
                self.reset(con ,addr,redata,server)
                break
            if (redata.lower() == "kill"):
                self.kill(con)
                break

            print(di[addr] + ' '  + ':\n' + redata)
            for i in li:
                i.send((di[addr] + ' ' + ':\n' + redata).encode())

    def close_client(self, con, addr):
        self.li.remove(con)
        print("client:", self.li)
        con.close()
        print(self.di[addr] + " A QUITER")
        for k in self.li:
            k.send((self.di[addr] + "uuuuuuuuuu").encode())

    def execute(self,cmd):
        return str(cmd)

    def kill(self, con):

        con.send("kill".encode())
        self.li.remove(con)
        print("client:", self.li)
        con.close()
        print(self.di[addr] + " A QUITER")
        self.server.close()
        print( "Serveur deconecter")

    def reset (self,con ,addr,redata,server):
        con.send("reset".encode())
        con.close()
        self.server.close()
        print("relance du server")
        self.server =socket.socket() # Création d’un canal de communication permet de creer un socket avec une ip soit un socket tcp
        self.server.bind((host, port))
        self.server.listen(5)
        print(redata +"En attente d'un client")
        print(self.di[addr] + " A QUITER")
        for k in self.li:
            k.send((self.di[addr] + "uuuuuuuuuu").encode())




    def serveur(self):
        redata = ""
        while redata != "kill":

            redata = ""
            while redata != "kill":
                self.server = socket.socket()
                self.server.bind((host, port))
                self.server.listen(1)
                print(f"Socket ouverte sur {host} - {port}")

                redata = ""
                while redata != "kill" and redata != "reset":
                    print('FD> En attente du client')
                    con, addr = self.server.accept()
                    print(f'Client connecté {addr}')

                    redata = ""
                    while redata.lower() != m_kill and redata.lower() != m_reset and redata.lower() != m_disconnect:
                        redata = con.recv(1024).decode()
                        print(f"Message reçu {redata}")
                        execution = self.execute(redata)
                        con.send(execution.encode())

                    con.close()
                    print("Fermeture de la socket client")

                self.server.close()
                print("Fermeture du serveur")


if __name__ == "__main__":
    server()
