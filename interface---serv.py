import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QToolBar, QMainWindow, QGridLayout, QLabel, QLineEdit, \
    QPushButton, QComboBox, QVBoxLayout, QTabWidget
from PyQt5.QtCore import QCoreApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import os
import sys
class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        widget = QWidget()


        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)


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



        quit.clicked.connect(self.__actionQuitter)
        self.tab1.setLayout(self.tab1.layout)
        ok.clicked.connect(self.__actionOk)

        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

    @pyqtSlot()
    def on_click(self):
        print("rtyrtytryrty\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())

    def __actionQuitter(self):
        QCoreApplication.exit(0)
    def __actionOk(self):
        x = self.__text.text()
        self.__text.setText("Bonjour "+ x)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.resize(400, 300)
    window.show()
    app.exec()