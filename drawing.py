import math
from PyQt5.QtWidgets import QFrame
from PyQt5.QtGui import *
from PyQt5.QtCore import *


# ищем центр
def get_center(obj):
    x0 = obj.width() / 2
    y0 = obj.height() / 2
    return QPoint(int(x0), int(y0))

# классы для черчения
class DrawingTriangle:

    def get_drawing(self):
        
        class Drawing(QFrame):
            def __init__(self, side_ab, side_ac, angle_a):
                super().__init__()
                self.side_ab = side_ab
                self.side_ac = side_ac
                self.angle_a = angle_a

            def paintEvent(self, e):

                center_point = get_center(self)

                # вершины
                point_A = QPoint(0, 0) + center_point
                point_B = QPoint(self.side_ab, 0) + center_point
                point_C = QPoint(int(math.cos(self.angle_a) * self.side_ac), -int(math.sin(self.angle_a) * self.side_ac)) + center_point
                
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

        return Drawing(self.side_ab, self.side_ac, self.angle_a)

class DrawingCircle:

    def get_drawing(self):
        
        class Drawing(QFrame):
            def __init__(self, radius):
                super().__init__()
                self.radius = radius

            def paintEvent(self, e):

                center_point = get_center(self)

                # построение
                painter = QPainter()
                painter.begin(self)
                painter.drawEllipse(center_point, self.radius, self.radius)
                pen = QPen()
                pen.setBrush(Qt.blue)
                painter.setPen(pen)
                painter.drawLine(center_point, center_point + QPoint(self.radius, 0))
                painter.end()

        return Drawing(self.radius)

class DrawingRectangle:

    def get_drawing(self):
        
        class Drawing(QFrame):
            def __init__(self, side_ab, side_bc):
                super().__init__()
                self.side_ab = side_ab
                self.side_bc = side_bc

            def paintEvent(self, e):

                x0 = self.width() / 2
                y0 = self.height() / 2
                x1 = x0 - self.side_ab / 2
                y1 = y0 - self.side_bc / 2

                # построение
                painter = QPainter()
                painter.begin(self)
                painter.drawRect(x1, y1, self.side_ab, self.side_bc)
                pen = QPen()
                pen.setBrush(Qt.blue)
                painter.setPen(pen)
                painter.end()

        return Drawing(self.side_ab, self.side_bc)

class DrawingRomb:

    def get_drawing(self):
        
        class Drawing(QFrame):
            def __init__(self, side_ab, angle_a):
                super().__init__()
                self.side = side_ab
                self.angle_a = angle_a

            def paintEvent(self, e):

                center_point = get_center(self)

                # вершины
                point_A = QPoint(0, 0) + center_point
                point_B = point_A + QPoint(self.side, 0)
                point_C = point_B + QPoint(int(math.cos(math.radians(self.angle_a)) * self.side), -int(math.sin(math.radians(self.angle_a)) * self.side))
                point_D = point_C - QPoint(self.side, 0)
                
                # смещение от центра
                middle_point = (point_A + point_B + point_C + point_D) / 4
                delta_point = center_point - middle_point
                point_A = point_A + delta_point
                point_B = point_B + delta_point
                point_C = point_C + delta_point
                point_D = point_D + delta_point

                # построение
                painter = QPainter()
                painter.begin(self)
                painter.drawLine(point_A, point_B)
                painter.drawLine(point_B, point_C)
                painter.drawLine(point_C, point_D)
                painter.drawLine(point_A, point_D)
                painter.drawText(point_A + QPoint(-10, 10), 'А') # добавлено смещение подписи от точки
                painter.drawText(point_B + QPoint(5, 10), 'B') # позже можно сделать выбор сверяясь с центром фигуры
                painter.drawText(point_C + QPoint(5, -5), 'C')
                painter.drawText(point_D + QPoint(-10, -5), 'D')
                painter.end()

        return Drawing(self.side_ab, self.angle_a)
