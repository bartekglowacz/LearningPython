import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget, QFileDialog, QGridLayout
from PyQt5.QtGui import QPixmap
from PyQt5 import QtGui, QtCore, Qt
from PyQt5.QtGui import QCursor

app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Who wants to be a programmer?")
window.setFixedWidth(1000)
window.setStyleSheet("background: #161219;")

grid = QGridLayout()

#display logo
image = QPixmap("logo.png")
logo = QLabel()
logo.setPixmap(image)
logo.setStyleSheet("margin-top: 100px;")

#button widget
button = QPushButton("PLAY")
button.setStyleSheet(
    "border: 4px solid '#BC006C';" +
    "border-radius: 15px;" +
    "font-size: 35px;"
    "color: 'white'"
)

grid.addWidget(logo, 0, 0)
grid.addWidget(button, 1, 0)

window.setLayout(grid)

window.show()
sys.exit(app.exec())