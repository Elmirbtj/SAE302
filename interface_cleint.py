from PyQt5 import QtGui
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
import sys
import socket
from threading import Thread


class Login(QWidget):
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


class MyTableWidget(QWidget):

    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        widget = QWidget()


        self.__cb = QComboBox()
        grid = QGridLayout()
        widget.setLayout(grid)


        self.__text = QLineEdit("")
        self.__lab2 = QLabel("")
        quit = QPushButton("Quitter")
        ok = QPushButton("Ok")
        # Ajouter les composants au grid ayout

        grid.addWidget(self.__text, 1, 2)





        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()


        self.tabs.addTab(self.tab1, "Connection")
        self.tabs.addTab(self.tab2, "serveur")








        grid.addWidget(ok, 1, 2)



        self.tab1.layout = QVBoxLayout(self)
        self.pushButton1 = QPushButton("PyQt5 button")


        self.tab1.layout.addWidget(ok)

        self.tab1.layout.addWidget(self.__text)




        self.tab1.setLayout(self.tab1.layout)


        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = Login()
    dialog.show()
    sys.exit(app.exec())