from PyQt5 import QtGui
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
import sys
import socket
from threading import Thread

from PyQt5.QtCore import QCoreApplication, Qt




class connection(QWidget):
    def __init__(self, connection, parent):
        super().__init__()
        self.__grid = QGridLayout()
        self.setLayout(self.__grid)
        self.__connection = connection
        self.__parent = parent
        self.__stop = False
        self.connectionClosed = True
        self.addUI()
        #self.text.setStyleSheet("margin:0;padding:0")
        #self.__commandinput = QLineEdit()
        #self.__commandinput.setPlaceholderText('INSERER COMMANDE')
       # self.__commandinput.returnPressed.connect(self.__send_message)
        #self.__grid.addWidget(self.__terminous, 0, 0)
        #self.__grid.addWidget(self.__commandinput, 1, 0)
        self.__grid.setContentsMargins(0, 0, 0, 0)
        self.__grid.setSpacing(0)
        self.__threadecoute = Thread(target=self.recv_msg())
        self.__threadecoute.start()
        self.thread()
        self.__layout = QGridLayout()
        self.setLayout(self.__layout)
        self.__layout.addWidget(self.text, 0, 0)


    def addUI(self):



        self.text.setGeometry(10, 10, 359, 250)
        self.text.setStyleSheet('background-color:white;)')

        self.text2 = QLineEdit(self)

        self.text2.setPlaceholderText('Envoyer du contenu')
        self.text2.setGeometry(10, 260, 300, 30)
        self.text2.setStyleSheet('background-color:white;)}')
        self.text2.returnPressed.connect(self.send_msg)


        self.button = QPushButton('envoyer', self)
        self.button.setFont(QFont('', 8, QFont.Bold))
        self.button.setGeometry(310, 260, 60, 30)

    def send_msg(self):

        if len(self.text2.text()) > 0:
            command = self.text2.text()
            self.text2.setText(self.text2.text() + '\nMoi > ' + command)
            if not self.connectionClosed:
                try:

                    self.__connection.send(command.encode())
                except:
                    self.text.setText('Impossible de communiquer avec le server! \n')
            else:
                self.text.setText('Déconnecté. \n')
            self.text2.clear()

    def recv_msg(self):
        while not self.connectionClosed:
            try:
                data = self.__connection.recv(1024).decode()
                self.text.append(data + '\n')
                if data == 'DISCONNECT':
                    self.__connection.close()
                    self.connectionClosed = True
            except:
                pass

    def closeEvent(self, QCloseEvent):
        self.connectionClosed = True
        self.client.close()
        QCloseEvent.accept()
        self.__stop = True
        self.deleteLater()















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

        self.__tab1.setLayout(self.__tab1.layout)

        self.__tab2.layout = QGridLayout()


        self.__tab2.setLayout(self.__tab2.layout)

        grid.addWidget(self.__tabs, 8, 0, 1, 0)


        grid = QGridLayout()
        widget.setLayout(grid)
        self.__port = QLineEdit("")
        self.__ip = QLineEdit("")


        self.__port.setPlaceholderText("Port")
        self.__ip.setPlaceholderText("IP")


        self.__ok = QPushButton("Connection")
        self.__stop = False


        self.__tab2.layout.addWidget(self.__ip, 2, 0)
        self.__tab2.layout.addWidget(self.__port, 1, 0)
        self.__tab2.layout.addWidget(self.__ok, 1, 1)

        self.__ok.clicked.connect(self.__lancement)




    def __lancement(self):
        if len(self.__ip.text()) > 0 and self.__port.text().isdigit():
            HOST = self.__ip.text()
            PORT = int(self.__port.text())
            try:
                self.client = socket.socket()
                self.client.connect((HOST, PORT))
                self.connectionClosed = False
                tab = connection(self.client, self)

                self.__tabs.addTab(tab, str(HOST) + ':' + str(PORT))
                self.__ip.setText("")
                self.__port.setText("")
            except:
                print('ERREUR DE CONNECTION')
        else:
            print('ERREUR DE FORMULAIRE')

    def __actionQuitter(self):
        self.__stop = True
        self.client.close()


    def stopped(self) -> bool:
        return self.__stop

    def closeEvent(self, event):
        self.__actionQuitter()
        event.accept()





if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = MainWindow()
    dialog.show()
    sys.exit(app.exec())