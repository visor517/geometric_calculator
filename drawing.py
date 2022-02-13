import sys
import math
from PyQt5.QtWidgets import QApplication, QFrame
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Drawing(QFrame):
    # def __init__(self):
    #     super().__init__()
 
    def paintEvent(self, e):

        # ищем центр
        x0 = self.width() / 2
        y0 = self.height() / 2
        center_point = QPoint(int(x0), int(y0))

        ab, ac, a = 150, 100, 1

        # вершины
        point_A = QPoint(0, 0) + center_point
        point_B = QPoint(ab, 0) + center_point
        point_C = QPoint(int(math.cos(a) * ac), -int(math.sin(a) * ac)) + center_point
        
        # смещение от центра
        middle_point = (point_A + point_B + point_C) / 3
        delta_point = center_point - middle_point
        point_A = point_A + delta_point
        point_B = point_B + delta_point
        point_C = point_C + delta_point

        # построение
        painter = QPainter()
        painter.begin(self)
        painter.drawLine(point_A, point_B)
        painter.drawLine(point_A, point_C)
        painter.drawLine(point_B, point_C)
        painter.drawText(point_A + QPoint(-10, 10), 'А') # добавлено смещение подписи от точки
        painter.drawText(point_B + QPoint(10, 10), 'B') # позже можно сделать выбор сверяясь с центром фигуры
        painter.drawText(point_C + QPoint(0, -10), 'C')
        painter.end()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Drawing()
    window.show()
    sys.exit(app.exec())

