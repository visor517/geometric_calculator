from pyclbr import Class
import sys
import math
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QComboBox, QLineEdit, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from drawing import Drawing
from main_gui import Ui_MainWindow
from logic import Circle, Triangle
from tools import clear_layout


class Calculator:
    def __init__(self, ui: Ui_MainWindow):
        self.ui = ui
        options = []
        cur_figure_class = None
        cur_figure = None       # может не пригодится

        # навешиваем методы на кнопки
        self.ui.circleButton.clicked.connect(lambda: self.inputOptions(Circle))
        self.ui.triangleButton.clicked.connect(lambda: self.inputOptions(Triangle))
        self.ui.optionsBox.currentIndexChanged.connect(self.draw_parameters)
        self.ui.calculateButton.clicked.connect(self.calculate)

    def inputOptions(self, figure_class: Class):
        
        self.cur_figure_class = figure_class
        self.options = figure_class.get_options()

        self.ui.optionsBox.clear()
        # заполняем опции расчета
        self.ui.optionsBox.addItems([option.name for option in self.options])

        drawing = Drawing()
        # чистим холст
        clear_layout(self.ui.drawingLayout)
        self.ui.drawingLayout.addWidget(drawing)

    def draw_parameters(self, index):
        global options

        # чистим параметры
        clear_layout(self.ui.optionsFormLayout)

        if len(self.options) > 0:
            for parameter in self.options[index].parameters:
                self.ui.optionsFormLayout.addRow(QLabel(parameter), QLineEdit())

    def calculate():
        pass


def main():

    # графическое окружение
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    # калькулятор
    Calculator(ui)
   
    sys.exit(app.exec())

if __name__ == '__main__':
    main()
