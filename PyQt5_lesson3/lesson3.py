from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QLabel, QGridLayout
from PyQt5.QtWidgets import QLineEdit, QPushButton, QHBoxLayout

class Calculator(QWidget):
    def __init__(self):
        super().__init__()

        self.interface()

    def interface(self):

        # etykiety
        label1 = QLabel("Liczba 1:", self)
        label2 = QLabel("Liczba 2:", self)
        label3 = QLabel("Wynik:", self)

        # przypisanie widgetów do układu tabelarycznego
        ukladT = QGridLayout()
        ukladT.addWidget(label1, 0, 0)
        ukladT.addWidget(label2, 0, 1)
        ukladT.addWidget(label3, 0, 2)

        self.liczba1Edt = QLineEdit()
        self.liczba2Edt = QLineEdit()
        self.wynikEdt = QLineEdit()

        self.wynikEdt.readonly = True
        self.wynikEdt.setToolTip("wpisz <b>Liczby</b> i wybierz działanie...")

        ukladT.addWidget(self.liczba1Edt, 1, 0)
        ukladT.addWidget(self.liczba2Edt, 1, 1)
        ukladT.addWidget(self.wynikEdt, 1, 2)

        #przyciski
        dodajBtn = QPushButton("&Dodaj", self)
        odejmijBtn = QPushButton("&Odejmij", self)
        dzielBtn = QPushButton("&Dziel", self)
        mnozBtn = QPushButton("&Mnoz", self)
        koniecBtn = QPushButton("&Koniec", self)
        koniecBtn.resize(koniecBtn.sizeHint())

        ukladH = QHBoxLayout()
        ukladH.addWidget(dodajBtn)
        ukladH.addWidget(odejmijBtn)
        ukladH.addWidget(dzielBtn)
        ukladH.addWidget(mnozBtn)

        ukladT.addLayout(ukladH, 2, 0, 1, 3)
        ukladT.addWidget(koniecBtn, 3, 0, 1, 3)

        # przypisanie utworzonego układu do okna
        self.setLayout(ukladT)

        self.setGeometry(700, 400, 300, 100)
        self.setWindowIcon(QIcon("kalkulator.png"))
        self.setWindowTitle("Prosty kalkulator")
        self.show()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    window = Calculator()
    sys.exit(app.exec_())
