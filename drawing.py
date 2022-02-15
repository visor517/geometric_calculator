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
        side_ab = self.side_ab
        side_ac = self.side_ac
        angle_a = self.angle_a
        
        class Drawing(QFrame):
            def paintEvent(self, e):

                center_point = get_center(self)

                # вершины
                point_A = QPoint(0, 0) + center_point
                point_B = QPoint(side_ab, 0) + center_point
                point_C = QPoint(int(math.cos(angle_a) * side_ac), -int(math.sin(angle_a) * side_ac)) + center_point
                
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

        return Drawing()

class DrawingCircle:

    def get_drawing(self):
        radius = self.radius
        
        class Drawing(QFrame):
            def paintEvent(self, e):

                center_point = get_center(self)

                # построение
                painter = QPainter()
                painter.begin(self)
                painter.setPen(QPen(Qt.black, 2, Qt.SolidLine))
                painter.drawEllipse(center_point, radius, radius)
                painter.setPen(QPen(Qt.blue, 1, Qt.SolidLine))
                painter.drawLine(center_point, center_point + QPoint(radius, 0))
                painter.end()

        return Drawing()

class DrawingRectangle:

    def get_drawing(self):
        side_ab = self.side_ab
        side_bc = self.side_bc
        
        class Drawing(QFrame):

            def paintEvent(self, e):

                x0 = self.width() / 2
                y0 = self.height() / 2
                x1 = x0 - side_ab / 2
                y1 = y0 - side_bc / 2

                # построение
                painter = QPainter()
                painter.begin(self)
                painter.setPen(QPen(Qt.black, 2, Qt.SolidLine))
                painter.drawRect(x1, y1, side_ab, side_bc)
                painter.end()

        return Drawing()

class DrawingRomb:

    def get_drawing(self):
        side = self.side_ab
        angle_a = self.angle_a

        class Drawing(QFrame):

            def paintEvent(self, e):

                center_point = get_center(self)

                # вершины
                point_A = QPoint(0, 0) + center_point
                point_B = point_A + QPoint(side, 0)
                point_C = point_B + QPoint(int(math.cos(math.radians(angle_a)) * side), -int(math.sin(math.radians(angle_a)) * side))
                point_D = point_C - QPoint(side, 0)
                
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

        return Drawing()

class DrawingTrapezoid:

    def get_drawing(self):
        side_ab = self.side_ab
        side_bc = self.side_bc 
        side_ad = self.side_ad
        angle_a = self.angle_a 
        angle_b = self.angle_b        
        class Drawing(QFrame):

            def paintEvent(self, e):

                center_point = get_center(self)

                # вершины
                point_A = QPoint(0, 0) + center_point
                point_B = point_A + QPoint(side_ab, 0)
                point_C = point_B + QPoint(-int(math.cos(math.radians(angle_b)) * side_bc), -int(math.sin(math.radians(angle_b)) * side_bc))
                point_D = point_A + QPoint(int(math.cos(math.radians(angle_a)) * side_ad), -int(math.sin(math.radians(angle_a)) * side_ad))
                
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

        return Drawing()

class DrawingSpere:
    def get_drawing(self):
        radius = self.radius
        
        class Drawing(QFrame):              

            def paintEvent(self, e):

                center_point = get_center(self)

                # построение
                painter = QPainter()
                painter.begin(self)
                painter.setPen(QPen(Qt.black, 2, Qt.SolidLine))
                painter.drawEllipse(center_point, radius, radius)
                painter.drawEllipse(center_point, radius, radius / 2)
                painter.drawText(center_point + QPoint(-10, -5), 'O')
                painter.setPen(QPen(Qt.green, 1, Qt.SolidLine))
                painter.drawLine(center_point, center_point + QPoint(radius, 0))
                painter.end()

        return Drawing()

class DrawingCylinder:
    def get_drawing(self):
        radius = self.radius
        height = self.height
        
        class Drawing(QFrame):
            def paintEvent(self, e):

                center_point = get_center(self)

                # построение
                painter = QPainter()
                painter.begin(self)
                painter.setPen(QPen(Qt.black, 2, Qt.SolidLine))
                painter.drawEllipse(center_point + QPoint(0, height / 2), radius, radius / 2)
                painter.drawEllipse(center_point - QPoint(0, height / 2), radius, radius / 2)
                painter.drawLine(center_point + QPoint(radius, height / 2), center_point + QPoint(radius, -height / 2))
                painter.drawLine(center_point - QPoint(radius, height / 2), center_point - QPoint(radius, -height / 2))
                painter.end()

        return Drawing()

class DrawingCube:

    def get_drawing(self):
        side = self.side

        class Drawing(QFrame):

            def paintEvent(self, e):

                center_point = get_center(self)

                # вершины
                point_A = QPoint(0, 0) + center_point
                point_B = point_A + QPoint(side, 0)
                point_C = point_B + QPoint(0, -side)
                point_D = point_A + QPoint(0, -side)

                point_A2 = point_A + QPoint(side / 2, -side / 3)
                point_B2 = point_B + QPoint(side / 2, -side / 3)
                point_C2 = point_C + QPoint(side / 2, -side / 3)
                point_D2 = point_D + QPoint(side / 2, -side / 3)

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

        return Drawing()

class DrawingParallelepiped:

    def get_drawing(self):
        side_a = self.side_a
        side_b = self.side_b
        side_c = self.side_c
        
        class Drawing(QFrame):

            def paintEvent(self, e):

                center_point = get_center(self)

                # вершины
                point_A = QPoint(0, 0) + center_point
                point_B = point_A + QPoint(side_a, 0)
                point_C = point_B + QPoint(0, -side_b)
                point_D = point_A + QPoint(0, -side_b)

                point_A2 = point_A + QPoint(side_c / 2, -side_c / 3)
                point_B2 = point_B + QPoint(side_c / 2, -side_c / 3)
                point_C2 = point_C + QPoint(side_c / 2, -side_c / 3)
                point_D2 = point_D + QPoint(side_c / 2, -side_c / 3)

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

        return Drawing()

class DrawingCone:
    def get_drawing(self):
        height = self.height
        radius = self.radius
        
        class Drawing(QFrame):

            def paintEvent(self, e):

                center_point = get_center(self)

                # построение
                painter = QPainter()
                painter.begin(self)
                painter.setPen(QPen(Qt.black, 2, Qt.SolidLine))
                painter.drawEllipse(center_point + QPoint(0, height / 2), radius, radius / 2)
                painter.drawLine(center_point + QPoint(radius, height / 2), center_point + QPoint(0, -height / 2))
                painter.drawLine(center_point + QPoint(-radius, height / 2), center_point + QPoint(0, -height / 2))
                painter.end()

        return Drawing()

class DrawingPyramid:
    def get_drawing(self):
        side = self.side
        height = self.height
        
        class Drawing(QFrame):

            def paintEvent(self, e):

                center_point = get_center(self)

                # опять магические числа, но пока так
                # вершины
                point_A = center_point + QPoint(0, height / 2)
                point_B = point_A + QPoint(side, 0)
                point_C = point_B + QPoint(side / 2, -side / 3)
                point_D = point_A + QPoint(side / 2, -side / 3)
                middle_point = (point_A + point_B + point_C + point_D) / 4
                delta_point = point_A - middle_point

                point_A = point_A + delta_point
                point_B = point_B + delta_point
                point_C = point_C + delta_point
                point_D = point_D + delta_point
                point_T = center_point - QPoint(0, height / 2)

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

        return Drawing()
