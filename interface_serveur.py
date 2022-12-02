import socket
from threading import Thread

import time


class server:
    def __init__(self):
        server = socket.socket()
        server.bind(('127.0.0.1', 9999))
        server.listen(5)
        self.server = server
        self.li = []
        self.di = {}
        self.get_con()

    def get_con(self):
        while 1:
            con, addr = self.server.accept()
            data = 'La connexion est réussie !, veuillez entrer un pseudo'
            con.send(data.encode())
            Thread(target=self.get_msg, args=(con, self.li, self.di, addr)).start()  # 启动子线程
            self.li.append(con)

    def get_msg(self, con, li, di, addr):
        name = con.recv(1024).decode()

        di[addr] = name
        while 1:
            try:
                redata = con.recv(1024).decode()
                # print("sdfsdffd" % redata)
            except Exception as e:
                # print("", e)
                self.close_client(con, addr)
                break
            if (redata.upper() == "QUIT"):
                self.close_client(con, addr)
                break

            print(di[addr] + ' ' + time.strftime('%x') + ':\n' + redata)
            for i in li:
                i.send((di[addr] + ' ' + time.strftime('%x') + ':\n' + redata).encode())

    def close_client(self, con, addr):
        self.li.remove(con)
        print("client:", self.li)
        con.close()
        print(self.di[addr] + "sqdsdqsqd")
        for k in self.li:
            k.send((self.di[addr] + "dsfdfsfd").encode())


if __name__ == "__main__":
    server()