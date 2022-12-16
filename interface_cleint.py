from PyQt5 import QtGui
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import *
import sys
import socket
from threading import Thread
from PyQt5.QtCore import QCoreApplication
from PyQt5 import QtCore




class shell(QWidget):
    def __init__(self,connection):
        super(shell, self).__init__()
        grid = QGridLayout()
        self.setLayout(grid)
        self.connnection =connection

        self.addUI()
        self.text2.returnPressed.connect(self.send_msg)


        self.connectionClosed =False

        self.__threadecoute = Thread(target=self.recv_msg)
        self.__threadecoute.start()



    def addUI(self):

        self.text = QTextEdit(self)
        self.text.verticalScrollBar().rangeChanged.connect(lambda: self.text.verticalScrollBar().setValue(self.text.verticalScrollBar().maximum()))
        self.text.setReadOnly(True)
        self.text.setGeometry(10, 10, 570, 430)
        self.text.setStyleSheet('background-color:white;)')

        self.text2 = QLineEdit(self)

        self.text2.setPlaceholderText('Envoyer du contenu')
        self.text2.setGeometry(10, 440, 570, 30)
        self.text2.setStyleSheet('background-color:white;)}')

    def send_msg(self):
        if len(self.text2.text()) > 0:
            msg = self.text2.text()
            self.text.append('MOI : ' + msg + '\n')
            if not self.connectionClosed:
                try:
                    print(msg)
                    if msg != "":
                        self.connnection.send(msg.encode())
                except:
                    self.text.append('Impossible de communiquer avec le server! \n')
            else:
                self.text.append('Déconnecté. \n')
            self.text2.clear()

    def recv_msg(self):
        while not self.connectionClosed:
            try:
                data = self.connnection.recv(1024).decode()
                self.text.append(data + '\n')
                if data == 'DISCONNECT':

                    self.close()
            except:
                pass


    def close(self):
        self.connectionClosed=True
        self.connnection.close()
        self.deleteLater()



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(600, 300, 600, 500)
        self.setWindowTitle("interface")
        palette = QtGui.QPalette()
        self.setPalette(palette)

        self.setStyleSheet("""
        QMainWindow{background:white}
        """)

        widget = QWidget()
        self.setCentralWidget(widget)
        grid = QGridLayout()
        widget.setLayout(grid)

        self.__tabs = QTabWidget()
        self.__tab1 = QWidget()
        self.__tabs.addTab(self.__tab1,"Connection")
        self.create_table()
        self.__tabs.addTab(self.table,"CSV")
        grid.setContentsMargins(0,0,0,0)
        grid.setSpacing(0)

        self.__tab1.layout = QGridLayout()
        self.__tab1.setLayout(self.__tab1.layout)
        grid.addWidget(self.__tabs, 0, 0, 0, 0)

        grid = QGridLayout()
        widget.setLayout(grid)
        self.__port = QLineEdit("5")
        self.__ip = QLineEdit("localhost")

        self.__port.setPlaceholderText("Port")
        self.__ip.setPlaceholderText("IP")
        self.__ok = QPushButton("Connection")

        self.__tab1.layout.addWidget(self.__ip, 1, 0)
        self.__tab1.layout.addWidget(self.__port, 1, 1)
        self.__tab1.layout.addWidget(self.__ok, 1, 2)
        self.__ok.clicked.connect(self.__start)
        self.connections = []


    def create_table(self):
        self.table = QTableWidget()
        self.table.setRowCount(0)
        self.table.setColumnCount(1)

        try:
            with open('test.csv','r') as file:
                lines = file.readlines()
                for line in lines:
                    line =line.replace('\n', '')
                    if len(line.split(',')) == 2 and line.split(',')[1].isdigit() and len(line.split(',')[0]) > 0:
                        HOST = line.split(',')[0]
                        PORT = line.split(',')[1]

                        row = self.table.rowCount()
                        self.table.setRowCount(row + 1)
                        self.table.setItem(row, 0, QTableWidgetItem(HOST + ':' + PORT))
        except:
            with open('test.csv','w') as file :
                file.write('')

        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.verticalHeader().setVisible(False)
        self.table.horizontalHeader().setVisible(False)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.table.setFocusPolicy(QtCore.Qt.NoFocus)
        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.resizeRowsToContents()


    def __start(self):
        if len(self.__ip.text()) > 0 and self.__port.text().isdigit():
            HOST = self.__ip.text()
            PORT = int(self.__port.text())
            try:
                client = socket.socket()
                client.connect((HOST,PORT))
                tab = shell(connection=client)
                self.__tabs.addTab(tab, f'{HOST}:{PORT}')
                self.connections.append(tab)

            except:

                print('ERREUR DE CONNECTION')
        else:
            print('ERREUR DE FORMULAIRE')






    def closeEvent(self, QCloseEvent):
        for i in self.connections :
            try :
                i.close()
            except:
                pass
        QCloseEvent.accept()
        QCoreApplication.exit(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dialog = MainWindow()
    dialog.show()
    sys.exit(app.exec())