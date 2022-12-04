
from PyQt5 import QtGui
from PyQt5.QtGui import QFont  
。
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot
import sys
import socket
from threading import Thread


class Login(QWidget):  
    def __init__(self):
        QWidget.__init__(self)
    
        self.setGeometry(600, 300, 400, 300)
  
        self.setWindowTitle("interface")
  
        palette = QtGui.QPalette()
        icon = QtGui.QPixmap(r'.https://www.shutterstock.com/image-illustration/abstract-wave-technology-background-blue-260nw-2152448863.jpg')
        palette.setBrush(self.backgroundRole(), QtGui.QBrush(icon))
        self.setPalette(palette)

        self.addUI()
        client = socket.socket()
        client.connect(('127.0.0.1', 9998))
        self.client = client
        self.begin_thread()




    def on_click(self):
        print("message envoyer")
        self.send_msg()
        self.text2.clear()

    def addUI(self):  

       
        self.text = QTextBrowser(self)  
        self.text.setGeometry(10, 10, 359, 250)
        self.text.setStyleSheet('background-color:white;)')  

        self.text2 = QLineEdit(self)

        self.text2.setPlaceholderText('Envoyer du contenu')
        self.text2.setGeometry(10,260, 300, 30)
        self.text2.setStyleSheet('background-color:white;)}') 

  
        self.button = QPushButton('envoyer', self)
        self.button.setFont(QFont('truyu', 10, QFont.Bold))
        self.button.setGeometry(310, 260, 60, 30)
        # self.button = button


    def send(self):
        self.button.clicked.connect(self.on_click)

    def begin_thread(self):
        Thread(target=self.send).start()
        Thread(target=self.recv_msg).start()

    def send_msg(self):
        msg = self.text2.text()
        print(msg)
        self.client.send(msg.encode())
        if (msg.upper() == "QUIT"):
            self.client.close()
        self.text2.clear()

    def recv_msg(self):
        while 1:
            try:
                data = self.client.recv(1024).decode()
                data = data + "\n"
                self.text.append(data)
            except:
                exit()

    def closeEvent(self, QCloseEvent):
        self.client.close()

if __name__ == "__main__":

    app = QApplication(sys.argv)
    dialog = Login()

    dialog.show()
 
    sys.exit(app.exec())
