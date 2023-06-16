"""
Należy stworzyć przycisk, który po kliknięciu pozwoli na wybranie jakiegoś pliku.
"""

from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLabel, QFileDialog
from PyQt5 import uic
import sys


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Ładowanie UI stworzonego w QtDesigner
        uic.loadUi("dialog.ui", self)

        # Definiujemy widgety
        self.button = self.findChild(QPushButton, "pushButton")
        self.label = self.findChild(QLabel, "label")

        # Wybór pliku
        self.button.clicked.connect(self.clicker)

        self.show()

    def clicker(self):
        # Okno otwarcia pliku
        fname, _ = QFileDialog.getOpenFileName(self, "Open File", "", "All Files (*);;Text Files (*.txt)")

        # Nazwa pliku wyrzucona na ekran
        if fname:
            self.label.setText(str(fname[0]))

            x_value = []
            y_value = []
            file = open(fname, 'r')
            for line in file:
                x_value.append(float(line.split("\t")[0]))
                y_value.append(float(line.split("\t")[1]))
            file.close()
            print(f"Wartości X: {x_value}")
            print(f"Wartości Y: {y_value}")


app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
