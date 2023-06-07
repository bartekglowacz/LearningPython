"""
Program dostaje jako dane wejściowe plik txt z dwiema kolumnami. Pierwsza zawiera częstotliwości w MHz, a druga poziom w dBuV.
Użytkownik powinien mieć możliwość wyklikania pliku, który chce wczytać.
GUI musi wyświetlić tabelę z wczytanymi wartościami, z rozdzieleniem na odpowiednie kolumny.
W GUI musi finalnie znaleźć się wykres na podstawie wczytanych danych, odpowiednio przeskalowany.
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QTableWidget, QTableWidgetItem
import matplotlib.pyplot as plt


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.BrowseButton = QtWidgets.QToolButton(self.centralwidget)
        self.BrowseButton.setGeometry(QtCore.QRect(0, 0, 120, 40))
        self.BrowseButton.setMouseTracking(False)
        self.BrowseButton.setObjectName("BrowseButton")
        self.BrowseButton.clicked.connect(self.openFile)

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 40, 181, 401))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")

        self.tableWidget = QTableWidget(self.scrollArea)  # Dodajemy tabelę
        self.tableWidget.setColumnCount(2)  # Ustalamy liczbę kolumn
        self.tableWidget.setHorizontalHeaderLabels(["f [MHz]", "U [dBuV]"])  # Etykiety kolumn

        self.scrollArea.setWidget(self.tableWidget)  # Ustawiamy tabelę jako widżet w scrollArea

        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setGeometry(QtCore.QRect(190, 40, 591, 401))
        self.graphicsView.setObjectName("graphicsView")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(280, 460, 181, 71))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionClose = QtWidgets.QAction(MainWindow)
        self.actionClose.setObjectName("actionClose")
        self.menuFile.addAction(self.actionClose)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.BrowseButton.setText(_translate("MainWindow", "Browse"))
        self.label.setText(_translate("MainWindow", "EndStatus"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionClose.setText(_translate("MainWindow", "Close"))

    def openFile(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setNameFilter("Pliki tekstowe (*.txt)")

        if file_dialog.exec_():
            file_path = file_dialog.selectedFiles()[0]
            self.processFile(file_path)

    def processFile(self, file_path):
        with open(file_path, "r") as file:
            lines = file.readlines()

        self.tableWidget.setRowCount(len(lines))  # Ustawiamy liczbę wierszy tabeli

        x_data = []
        y_data = []

        for i, line in enumerate(lines):
            line = line.strip()
            if line:
                freq, level = line.split()
                freq_item = QTableWidgetItem(freq)
                level_item = QTableWidgetItem(level)
                self.tableWidget.setItem(i, 0, freq_item)  # Wstawiamy wartość częstotliwości
                self.tableWidget.setItem(i, 1, level_item)  # Wstawiamy wartość poziomu

                x_data.append(float(freq))
                y_data.append(float(level))

        self.tableWidget.resizeColumnsToContents()  # Dopasowanie szerokości kolumn

        # Tworzenie wykresu
        plt.figure()
        plt.plot(x_data, y_data)
        plt.xlabel('Częstotliwość (MHz)')
        plt.ylabel('Poziom (dBuV)')
        plt.title('Wykres')
        plt.tight_layout()  # Dopasowanie układu wykresu
        plt.xlim(min(x_data), max(x_data))  # Przeskalowanie osi X
        plt.ylim(min(y_data), max(y_data))  # Przeskalowanie osi Y
        plt.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

