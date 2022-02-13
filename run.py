import sys
import math
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QComboBox, QDoubleSpinBox, QVBoxLayout, QLabel
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from drawing import Drawing
from main_gui import Ui_MainWindow
from logic import Triangle


def main():

    # графическое окружение
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()


    def makeTriangle():
        options = Triangle.get_options()

        combo_box = QComboBox()
        combo_box.addItems([item.name for item in options])
        label = QLabel('Параметр')
        input_box = QDoubleSpinBox()
        
        vbox = QVBoxLayout()
        vbox.addWidget(combo_box)
        vbox.addWidget(label)
        vbox.addWidget(input_box)
        ui.inputBox.setLayout(vbox)


        drawing = Drawing()
        ui.drawingLayout.addWidget(drawing)


    # навешиваем методы на кнопки
    ui.triangleButton.clicked.connect(makeTriangle)



    sys.exit(app.exec())

if __name__ == '__main__':
    main()
