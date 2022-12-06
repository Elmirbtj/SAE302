from PyQt5 import QtGui
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
import sys
import socket
from threading import Thread


class MainWindow(QMainWindow):
    def __init__(self):
        QWidget.__init__(self)

        self.setGeometry(600, 300, 400, 300)
        self.setWindowTitle("interface")
        palette = QtGui.QPalette()
        #icon = QtGui.QPixmap(r'.https://www.shutterstock.com/image-illustration/abstract-wave-technology-background-blue-260nw-2152448863.jpg')
        #palette.setBrush(self.backgroundRole(), QtGui.QBrush(icon))
        self.setPalette(palette)

        self.addUI()
        client = socket.socket()
        client.connect(('127.0.0.1', 5006))
        self.client = client
        self.thread()
        widget = QWidget()
        self.setCentralWidget(widget)
        grid = QGridLayout()
        widget.setLayout(grid)
        self.__tabs = QTabWidget()
        self.__tab1 = QWidget()
        self.__tab2 = QWidget()
        self.__tabs.addTab(self.__tab1, "Server_commande")
        self.__tabs.addTab(self.__tab2, "hjhgjghjh")

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
        self.__repons = QLineEdit("")

        self.__port.setPlaceholderText("Done port.")
        self.__ip.setPlaceholderText("done IP")
        self.__repons.setPlaceholderText("ecris ton text")

        self.__ok = QPushButton("Ok")

        grid.addWidget(self.__port, 1, 2)
        grid.addWidget(self.__ip, 1, 1)
        grid.addWidget(self.__repons, 2, 2)
        grid.addWidget(self.__ok, 1, 0, 1, 1)  # ligne,colonne,hauteur,largueur

        self.__ok.clicked.connect(self.__lancement)





    def __lancement(self):
        HOST = self.__ip.text()
        PORT = int(self.__port.text())
        try:
            self.client.connect((HOST, PORT))
            self.ecoute.start()

            self.__port.setHidden(True)
            self.__ip.setHidden(True)
            self.__ok.setHidden(True)

        except Exception as e:
            error = "Unable to connect to server \n'{}'".format(str(e))
            print("[INFO]", error)
            self.show_error("Connection Error", error)
            self.text2.text.clear()



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
        Thread(target=self.recv_msg).start()



    def send_msg(self):
        msg = self.text2.text()
        print(msg)
        if msg != "" :
            self.client.send(msg.encode())

        if (msg.lower() == "qrereuit"):
            self.client.close()
        self.text2.clear()


    def recv_msg(self):

        while True:
            data = self.client.recv(1024).decode()
            self.text.append('-> ' + data + '\n')



    def closeEvent(self, QCloseEvent):
        self.client.close()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = MainWindow()
    dialog.show()
    sys.exit(app.exec())