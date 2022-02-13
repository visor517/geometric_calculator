import sys
import math
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QComboBox, QLineEdit, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from drawing import Drawing
from main_gui import Ui_MainWindow
from logic import Circle, Triangle
from tools import clear_layout


def main():

    # графическое окружение
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    options = []

    def inputOptions(FigureClass):
        global options
        options = FigureClass.get_options()

        ui.optionsBox.clear()
        # заполняем опции расчета
        ui.optionsBox.addItems([option.name for option in options])

        drawing = Drawing()
        # чистим холст
        clear_layout(ui.drawingLayout)
        ui.drawingLayout.addWidget(drawing)

    def draw_parameters(index):
        global options
        
        # чистим параметры
        clear_layout(ui.optionsFormLayout)

        if len(options) > 0:
            for parameter in options[index].parameters:
                ui.optionsFormLayout.addRow(QLabel(parameter), QLineEdit())

    # навешиваем методы на кнопки
    ui.circleButton.clicked.connect(lambda: inputOptions(Circle))
    ui.triangleButton.clicked.connect(lambda: inputOptions(Triangle))
    ui.optionsBox.currentIndexChanged.connect(draw_parameters)



    sys.exit(app.exec())

if __name__ == '__main__':
    main()
