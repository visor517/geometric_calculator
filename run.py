from pyclbr import Class
import sys
import math
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QComboBox, QLineEdit, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from main_gui import Ui_MainWindow
from logic import Figure, Circle, Triangle
from tools import clear_layout


class Calculator:
    def __init__(self, ui: Ui_MainWindow):
        self.ui = ui
        self.options = []
        self.cur_option = None
        self.cur_figure_class = None
        self.cur_figure = None

        # навешиваем методы на кнопки
        self.ui.circleButton.clicked.connect(lambda: self.input_options(Circle))
        self.ui.triangleButton.clicked.connect(lambda: self.input_options(Triangle))
        self.ui.optionsBox.currentIndexChanged.connect(self.draw_parameters)
        self.ui.calculateButton.clicked.connect(self.calculate)

    # вывод вариантов ностроек для расчета фигуры
    def input_options(self, figure_class: Class):
        
        self.cur_figure_class = figure_class
        self.options = figure_class.get_options()
        self.ui.calculateButton.setEnabled(True)

        self.ui.optionsBox.clear()
        # заполняем вариантами расчета выподающее меню
        self.ui.optionsBox.addItems([option.name for option in self.options])


    def draw_parameters(self, index):
        self.cur_option = self.options[index]

        # чистим параметры
        clear_layout(self.ui.optionsFormLayout)

        if len(self.options) > 0:
            for parameter in self.options[index].parameters:
                self.ui.optionsFormLayout.addRow(QLabel(parameter), QLineEdit())

    # вычисления
    def calculate(self):
        # собираем введенные параметры 
        params = []
        for index in range(1, self.ui.optionsFormLayout.count(), 2):
            try:
                params.append(int(self.ui.optionsFormLayout.itemAt(index).widget().text()))
            except:
                self.show_message('Нужно вводить числа!')
                return
        
        # создвем фигуру
        self.cur_figure = self.cur_option.create_obj(*params)

        # вывод расчетов
        self.ui.outputTextBrowser.setText(self.cur_figure.calculate())

        # вызов черчения
        # чистим холст
        clear_layout(self.ui.drawingLayout)

        drawing = self.cur_figure.get_drawing()
        self.ui.drawingLayout.addWidget(drawing)


    # сообщения
    def show_message(self, message):
        msg = QMessageBox()
        msg.setText(message)
        msg.setWindowTitle("Сообщение")
        msg.exec_()


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
