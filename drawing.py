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
                painter.setPen(QPen(Qt.black, 2, Qt.SolidLine))
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
                painter.setPen(QPen(Qt.black, 2, Qt.SolidLine))
                painter.drawEllipse(center_point, self.radius, self.radius)
                painter.setPen(QPen(Qt.blue, 1, Qt.SolidLine))
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
                painter.setPen(QPen(Qt.black, 2, Qt.SolidLine))
                painter.drawRect(x1, y1, self.side_ab, self.side_bc)
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
                painter.setPen(QPen(Qt.black, 2, Qt.SolidLine))
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

class DrawingTrapezoid:

    def get_drawing(self):
        
        class Drawing(QFrame):
            def __init__(self, side_ab, side_bc, side_ad, angle_a, angle_b):
                super().__init__()
                self.side_ab = side_ab
                self.side_bc = side_bc
                self.side_ad = side_ad
                self.angle_a = angle_a
                self.angle_b = angle_b

            def paintEvent(self, e):

                center_point = get_center(self)

                # вершины
                point_A = QPoint(0, 0) + center_point
                point_B = point_A + QPoint(self.side_ab, 0)
                point_C = point_B + QPoint(-int(math.cos(math.radians(self.angle_b)) * self.side_bc), -int(math.sin(math.radians(self.angle_b)) * self.side_bc))
                point_D = point_A + QPoint(int(math.cos(math.radians(self.angle_a)) * self.side_ad), -int(math.sin(math.radians(self.angle_a)) * self.side_ad))
                
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
                painter.setPen(QPen(Qt.black, 2, Qt.SolidLine))
                painter.drawLine(point_A, point_B)
                painter.drawLine(point_B, point_C)
                painter.drawLine(point_C, point_D)
                painter.drawLine(point_A, point_D)
                painter.drawText(point_A + QPoint(-10, 10), 'А') # добавлено смещение подписи от точки
                painter.drawText(point_B + QPoint(5, 10), 'B') # позже можно сделать выбор сверяясь с центром фигуры
                painter.drawText(point_C + QPoint(5, -5), 'C')
                painter.drawText(point_D + QPoint(-10, -5), 'D')
                painter.end()

        return Drawing(self.side_ab, self.side_bc, self.side_ad, self.angle_a, self.angle_b)

class DrawingSpere:
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
                painter.setPen(QPen(Qt.black, 2, Qt.SolidLine))
                painter.drawEllipse(center_point, self.radius, self.radius)
                painter.drawEllipse(center_point, self.radius, self.radius / 2)
                painter.drawText(center_point + QPoint(-10, -5), 'O')
                painter.setPen(QPen(Qt.green, 1, Qt.SolidLine))
                painter.drawLine(center_point, center_point + QPoint(self.radius, 0))
                painter.end()

        return Drawing(self.radius)

class DrawingCylinder:
    def get_drawing(self):
        
        class Drawing(QFrame):
            def __init__(self, radius, height):
                super().__init__()
                self.radius = radius
                self.h = height

            def paintEvent(self, e):

                center_point = get_center(self)

                # построение
                painter = QPainter()
                painter.begin(self)
                painter.setPen(QPen(Qt.black, 2, Qt.SolidLine))
                painter.drawEllipse(center_point + QPoint(0, self.h / 2), self.radius, self.radius / 2)
                painter.drawEllipse(center_point - QPoint(0, self.h / 2), self.radius, self.radius / 2)
                painter.drawLine(center_point + QPoint(self.radius, self.h / 2), center_point + QPoint(self.radius, -self.h / 2))
                painter.drawLine(center_point - QPoint(self.radius, self.h / 2), center_point - QPoint(self.radius, -self.h / 2))
                painter.end()

        return Drawing(self.radius, self.height)

class DrawingCube:

    def get_drawing(self):
        
        class Drawing(QFrame):
            def __init__(self, side_ab):
                super().__init__()
                self.side = side_ab

            def paintEvent(self, e):

                center_point = get_center(self)

                # вершины
                point_A = QPoint(0, 0) + center_point
                point_B = point_A + QPoint(self.side, 0)
                point_C = point_B + QPoint(0, -self.side)
                point_D = point_A + QPoint(0, -self.side)

                point_A2 = point_A + QPoint(self.side / 2, -self.side / 3)
                point_B2 = point_B + QPoint(self.side / 2, -self.side / 3)
                point_C2 = point_C + QPoint(self.side / 2, -self.side / 3)
                point_D2 = point_D + QPoint(self.side / 2, -self.side / 3)

                # смещение от центра
                middle_point = (point_A + point_C2) / 2
                delta_point = center_point - middle_point
                point_A = point_A + delta_point
                point_B = point_B + delta_point
                point_C = point_C + delta_point
                point_D = point_D + delta_point
                point_A2 = point_A2 + delta_point
                point_B2 = point_B2 + delta_point
                point_C2 = point_C2 + delta_point
                point_D2 = point_D2 + delta_point

                # построение
                painter = QPainter()
                painter.begin(self)
                painter.setPen(QPen(Qt.black, 2, Qt.SolidLine))
                painter.drawLine(point_A, point_B)
                painter.drawLine(point_B, point_C)
                painter.drawLine(point_C, point_D)
                painter.drawLine(point_A, point_D)
                painter.drawLine(point_B2, point_C2)
                painter.drawLine(point_C2, point_D2)
                painter.drawLine(point_B, point_B2)
                painter.drawLine(point_C, point_C2)
                painter.drawLine(point_D, point_D2)
                painter.setPen(QPen(Qt.black, 2, Qt.DashLine))
                painter.drawLine(point_A, point_A2)
                painter.drawLine(point_A2, point_B2)
                painter.drawLine(point_A2, point_D2)
                painter.end()

        return Drawing(self.side)

class DrawingParallelepiped:

    def get_drawing(self):
        
        class Drawing(QFrame):
            def __init__(self, side_a, side_b, side_c):
                super().__init__()
                self.side_a = side_a
                self.side_b = side_b
                self.side_c = side_c

            def paintEvent(self, e):

                center_point = get_center(self)

                # вершины
                point_A = QPoint(0, 0) + center_point
                point_B = point_A + QPoint(self.side_a, 0)
                point_C = point_B + QPoint(0, -self.side_b)
                point_D = point_A + QPoint(0, -self.side_b)

                point_A2 = point_A + QPoint(self.side_c / 2, -self.side_c / 3)
                point_B2 = point_B + QPoint(self.side_c / 2, -self.side_c / 3)
                point_C2 = point_C + QPoint(self.side_c / 2, -self.side_c / 3)
                point_D2 = point_D + QPoint(self.side_c / 2, -self.side_c / 3)

                # смещение от центра
                middle_point = (point_A + point_C2) / 2
                delta_point = center_point - middle_point
                point_A = point_A + delta_point
                point_B = point_B + delta_point
                point_C = point_C + delta_point
                point_D = point_D + delta_point
                point_A2 = point_A2 + delta_point
                point_B2 = point_B2 + delta_point
                point_C2 = point_C2 + delta_point
                point_D2 = point_D2 + delta_point

                # построение
                painter = QPainter()
                painter.begin(self)
                painter.setPen(QPen(Qt.black, 2, Qt.SolidLine))
                painter.drawLine(point_A, point_B)
                painter.drawLine(point_B, point_C)
                painter.drawLine(point_C, point_D)
                painter.drawLine(point_A, point_D)
                painter.drawLine(point_B2, point_C2)
                painter.drawLine(point_C2, point_D2)
                painter.drawLine(point_B, point_B2)
                painter.drawLine(point_C, point_C2)
                painter.drawLine(point_D, point_D2)
                painter.setPen(QPen(Qt.black, 2, Qt.DashLine))
                painter.drawLine(point_A, point_A2)
                painter.drawLine(point_A2, point_B2)
                painter.drawLine(point_A2, point_D2)
                painter.end()

        return Drawing(self.side_a, self.side_b, self.side_c)

class DrawingCone:
    def get_drawing(self):
        
        class Drawing(QFrame):
            def __init__(self, height, radius):
                super().__init__()
                self.h = height
                self.radius = radius

            def paintEvent(self, e):

                center_point = get_center(self)

                # построение
                painter = QPainter()
                painter.begin(self)
                painter.setPen(QPen(Qt.black, 2, Qt.SolidLine))
                painter.drawEllipse(center_point + QPoint(0, self.h / 2), self.radius, self.radius / 2)
                painter.drawLine(center_point + QPoint(self.radius, self.h / 2), center_point + QPoint(0, -self.h / 2))
                painter.drawLine(center_point + QPoint(-self.radius, self.h / 2), center_point + QPoint(0, -self.h / 2))
                painter.end()

        return Drawing(self.height, self.radius)

class DrawingPyramid:
    def get_drawing(self):
        
        class Drawing(QFrame):
            def __init__(self, side, height):
                super().__init__()
                self.side = side
                self.h = height

            def paintEvent(self, e):

                center_point = get_center(self)

                # опять магические числа, но пока так
                # вершины
                point_A = center_point + QPoint(0, self.h / 2)
                point_B = point_A + QPoint(self.side, 0)
                point_C = point_B + QPoint(self.side / 2, -self.side / 3)
                point_D = point_A + QPoint(self.side / 2, -self.side / 3)
                middle_point = (point_A + point_B + point_C + point_D) / 4
                delta_point = point_A - middle_point

                point_A = point_A + delta_point
                point_B = point_B + delta_point
                point_C = point_C + delta_point
                point_D = point_D + delta_point
                point_T = center_point - QPoint(0, self.h / 2)

                # построение
                painter = QPainter()
                painter.begin(self)
                painter.setPen(QPen(Qt.black, 2, Qt.SolidLine))
                painter.drawLine(point_A, point_B)
                painter.drawLine(point_B, point_C)
                painter.drawLine(point_A, point_T)
                painter.drawLine(point_B, point_T)
                painter.drawLine(point_C, point_T)
                painter.setPen(QPen(Qt.black, 2, Qt.DashLine))
                painter.drawLine(point_C, point_D)
                painter.drawLine(point_A, point_D)
                painter.drawLine(point_D, point_T)

                painter.end()

        return Drawing(self.side, self.height)
