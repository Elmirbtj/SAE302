from PyQt5 import QtGui
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
import sys
import socket
from threading import Thread
from PyQt5.QtCore import QCoreApplication

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()


        self.setGeometry(600, 300, 600, 500)
        self.setWindowTitle("interface")
        palette = QtGui.QPalette()
        #icon = QtGui.QPixmap(r'.https://www.shutterstock.com/image-illustration/abstract-wave-technology-background-blue-260nw-2152448863.jpg')
        #palette.setBrush(self.backgroundRole(), QtGui.QBrush(icon))
        self.setPalette(palette)

        self.setStyleSheet("""
        QMainWindow{background:black}
        """)

        self.addUI()

        self.client = socket.socket()
        self.thread()
        widget = QWidget()
        self.setCentralWidget(widget)
        self.connectionClosed = True
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
        self.__port = QLineEdit("5")
        self.__ip = QLineEdit("localhost")


        self.__port.setPlaceholderText("Port")
        self.__ip.setPlaceholderText("IP")


        self.__ok = QPushButton("Connection")

        self.__tab2.layout.addWidget(self.__ip, 2, 0)
        self.__tab2.layout.addWidget(self.__port, 1, 0)
        self.__tab2.layout.addWidget(self.__ok, 1, 1)

        self.__ok.clicked.connect(self.__lancement)

        self.li = []

        self.button.clicked.connect(self.send_msg)
        self.text2.returnPressed.connect(self.send_msg)
        self.__threadecoute = Thread(target=self.send_msg())
        self.__threadecoute.start()

    def __lancement(self):
        if len(self.__ip.text()) > 0 and self.__port.text().isdigit():
            HOST = self.__ip.text()
            PORT = int(self.__port.text())
            try:
                self.client = socket.socket()
                self.client.connect((HOST, PORT))
                self.connectionClosed = False
                Thread(target=self.recv_msg).start()
                self.__ip.setText("")
                self.__port.setText("")
            except:

                print('ERREUR DE CONNECTION')
        else:
            print('ERREUR DE FORMULAIRE')


    def addUI(self):


        self.text = QTextEdit(self)
        self.text.verticalScrollBar().rangeChanged.connect(lambda: self.text.verticalScrollBar().setValue(self.text.verticalScrollBar().maximum()))
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



    def send_msg(self):
        if len(self.text2.text()) > 0:
            msg = self.text2.text()
            self.text.append('MOI : ' + msg + '\n')
            if not self.connectionClosed:
                try:
                    print(msg)
                    if msg != "":
                        self.client.send(msg.encode())
                except:
                    self.text.append('Impossible de communiquer avec le server! \n')
            else:
                self.text.append('Déconnecté. \n')
            self.text2.clear()


    def recv_msg(self):
        while not self.connectionClosed:
            try:
                data = self.client.recv(1024).decode()
                self.text.append(data + '\n')
                if data == 'DISCONNECT':
                    self.client.close()
                    self.connectionClosed = True
            except:
                pass



    def closeEvent(self, QCloseEvent):
        self.connectionClosed = True
        self.client.close()
        QCloseEvent.accept()
        QCoreApplication.exit(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = MainWindow()
    dialog.show()
    sys.exit(app.exec())