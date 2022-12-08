from PyQt5 import QtGui
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
import sys
import socket
from threading import Thread


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()


        self.setGeometry(600, 300, 600, 500)
        self.setWindowTitle("interface")
        palette = QtGui.QPalette()
        #icon = QtGui.QPixmap(r'.https://www.shutterstock.com/image-illustration/abstract-wave-technology-background-blue-260nw-2152448863.jpg')
        #palette.setBrush(self.backgroundRole(), QtGui.QBrush(icon))
        self.setPalette(palette)

        self.addUI()
        client = socket.socket()

        self.client = client
        self.thread()
        widget = QWidget()
        self.setCentralWidget(widget)
        grid = QGridLayout()
        widget.setLayout(grid)
        self.__tabs = QTabWidget()
        self.__tab1 = QWidget()
        self.__tab2 = QWidget()
        self.__tabs.addTab(self.__tab2, "Connection")
        self.__tabs.addTab(self.__tab1, "Server_commande")

        self.__tab1.layout = QGridLayout()

        self.__tab1.layout.addWidget(self.text)
        self.__tab1.setLayout(self.__tab1.layout)

        self.__tab2.layout = QGridLayout()

        self.__tab2.layout.addWidget(self.text)
        self.__tab2.setLayout(self.__tab2.layout)

        grid.addWidget(self.__tabs, 0, 0, 1, 2)
        grid.addWidget(self.text, 3, 0)
        self.__tab1.layout.addWidget(self.text, 2, 0)
        self.__tab1.layout.addWidget(self.text2, 1, 0)
        self.__tab1.layout.addWidget(self.button, 1, 1)


        grid = QGridLayout()
        widget.setLayout(grid)
        self.__port = QLineEdit("")
        self.__ip = QLineEdit("")


        self.__port.setPlaceholderText("Port")
        self.__ip.setPlaceholderText("IP")


        self.__ok = QPushButton("Connection")

        grid.addWidget(self.__port, 1, 2)
        grid.addWidget(self.__ip, 1, 1)

        grid.addWidget(self.__ok, 1, 0, 1, 1)  # ligne,colonne,hauteur,largueur

        self.__tab2.layout.addWidget(self.__ip, 2, 0)
        self.__tab2.layout.addWidget(self.__port, 1, 0)
        self.__tab2.layout.addWidget(self.__ok, 1, 1)

        self.__ok.clicked.connect(self.__lancement)

        self.li = []


    def __lancement(self,li):
        HOST = self.__ip.text()
        PORT = int(self.__port.text())

        try:

            self.client.connect((HOST, PORT))
            Thread(target=self.recv_msg ,args=(self.li)).start()
            self.__ip.setText("")
            self.__port.setText("")
            self.li.append(self.client.connect((HOST, PORT)))


        except Exception as e:
            pass



    def on_click(self):
        print("message envoyer")
        self.send_msg()
        self.text2.clear()

    def addUI(self):


        self.text = QTextEdit(self)
        self.text.setReadOnly(True)
        self.text.setGeometry(10, 10, 359, 250)
        self.text.setStyleSheet('background-color:white;)')

        self.text2 = QLineEdit(self)

        self.text2.setPlaceholderText('Envoyer du contenu')
        self.text2.setGeometry(10,260, 300, 30)
        self.text2.setStyleSheet('background-color:white;)}')


        self.button = QPushButton('envoyer', self)
        self.button.setFont(QFont('', 8, QFont.Bold))
        self.button.setGeometry(310, 260, 60, 30)


    def send(self):
        self.button.clicked.connect(self.on_click)

    def thread(self):
        Thread(target=self.send).start()



    def send_msg(self):
        msg = self.text2.text()
        print(msg)
        if msg != "" :
            self.client.send(msg.encode())

        #if (msg.lower() == "reset"):

        #self.text2.clear()


    def recv_msg(self):
        while True:
            try:

                data = self.client.recv(1024).decode()
                self.text.append('-> ' + data + '\n')
            except:
                pass



    def closeEvent(self, QCloseEvent):
        self.client.close()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = MainWindow()
    dialog.show()
    sys.exit(app.exec())