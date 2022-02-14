import abc
import math
from typing import Tuple
# Python 3.8

from drawing import *


class FigureError(Exception):
    pass

class Figure(abc.ABC):

    # @abc.abstractmethod
    def calculate(self):
        return 'Метод calculate не задан'

    # временная заглушка
    def get_drawing(self):
        print('Метод get_drawing не задан')


# варианы построения
# название варианта / необходимые параметры / функция для создания
class CalcOption:
    def __init__(self, name, parameters: Tuple[str], function_for_create):
        self.name = name
        self.parameters = parameters
        self.create_obj = function_for_create

# круг
class Circle(DrawingCircle, Figure):
    # метод возвращает возможные варианты построения
    @classmethod
    def get_options(cls):
        return [
            CalcOption('По радиусу', ['Радиус'], Circle),
            CalcOption('По диаметру', ['Диаметр'], cls.circle_by_diameter),
            CalcOption('По площади', ['Площадь'], cls.circle_by_area),
            CalcOption('По периметру', ['Периметр'], cls.circle_by_perimeter),
        ]

    @staticmethod
    def circle_by_diameter(diameter):
        return Circle(diameter / 2)

    @staticmethod
    def circle_by_area(area):
        return Circle((area / math.pi)**(0.5))

    @staticmethod
    def circle_by_perimeter(perimeter):
        return Circle(perimeter / 2 / math.pi)

    def __init__(self, radius):
        self.radius = radius

    def get_diameter(self):
        return 2 * self.radius

    def get_area(self):
        return math.pi * self.radius**2

    def get_perimeter(self):
        return 2 * math.pi * self.radius

    def calculate(self):
        return (
            f'Радиус {round(self.radius, 2)} \n'
            f'Диаметр {round(self.get_diameter(), 2)} \n'
            f'Площадь {round(self.get_area(), 2)} \n'
            f'Периметр {round(self.get_perimeter(), 2)} \n'
        )

# треугольник
class Triangle(DrawingTriangle, Figure):

    @classmethod
    def get_options(cls):
        return [
            CalcOption('По трем сторонам', ['АВ', 'BC', 'AC'], cls.triangle_by_sides)
        ]

    @staticmethod
    def triangle_by_sides(side_ab, side_ac, side_bc):
        # проверяем на верность вводных
        if side_ab + side_ac < side_bc or side_ab + side_bc < side_ac or side_bc + side_ac < side_ab:
            raise FigureError('Нарушено правило длин сторон треугольника!')
        # вычисление углов
        angle_a = math.acos((side_ab**2 + side_ac**2 - side_bc**2) / (2 * side_ab * side_ac))
        angle_b = math.acos((side_ab**2 + side_bc**2 - side_ac**2) / (2 * side_ab * side_bc))
        angle_c = math.acos((side_ac**2 + side_bc**2 - side_ab**2) / (2 * side_ac * side_bc))
        return Triangle(side_ab, side_ac, side_bc, angle_a, angle_b, angle_c)

    def __init__(self, side_ab, side_ac, side_bc, angle_a, angle_b, angle_c):
        self.side_ab = side_ab
        self.side_ac = side_ac
        self.side_bc = side_bc
        self.angle_a = angle_a      # в радианах
        self.angle_b = angle_b
        self.angle_c = angle_c

    def get_area(self):
        p = self.get_perimeter() / 2    
        return (p * (p - self.side_ab) * (p - self.side_bc) * (p - self.side_ac))**(0.5)

    def get_perimeter(self):
        return self.side_ab + self.side_bc + self.side_ac

    def calculate(self):
        return (
            f'Сторона AB {self.side_ab} \n'
            f'Сторона AC {self.side_ac} \n'
            f'Сторона BC {self.side_bc} \n'
            f'Угол A {round(math.degrees(self.angle_a), 1)} \n'
            f'Угол B {round(math.degrees(self.angle_b), 1)} \n'
            f'Угол C {round(math.degrees(self.angle_c), 1)} \n'
            f'Площадь {round(self.get_area(), 2)} \n'
            f'Периметр {round(self.get_perimeter(), 2)} \n'
        )

# четырехугольник

class Quadrangle(Figure):
    def __init__(self, side_ab, side_bc, side_cd, side_ad, angle_a, angle_b, angle_c, angle_d):
        self.side_ab = side_ab
        self.side_bc = side_bc
        self.side_cd = side_cd
        self.side_ad = side_ad
        self.angle_a = angle_a
        self.angle_b = angle_b
        self.angle_c = angle_c
        self.angle_d = angle_d

    def get_perimeter(self):
        return self.side_ab + self.side_bc + self.side_cd + self.side_ad

    def get_area():
        return None

    def calculate(self):
        return (
            f'Сторона AB {self.side_ab} \n'
            f'Сторона BC {self.side_bc} \n'
            f'Сторона CD {self.side_cd} \n'
            f'Сторона AD {self.side_ad} \n'
            f'Угол A {round(self.angle_a, 1)} \n'
            f'Угол B {round(self.angle_b, 1)} \n'
            f'Угол C {round(self.angle_c, 1)} \n'
            f'Угол D {round(self.angle_d, 1)} \n'
            f'Площадь {round(self.get_area(), 2)} \n'
            f'Периметр {round(self.get_perimeter(), 2)} \n'
        )

# прямоугольник
class Rectangle(DrawingRectangle, Quadrangle):

    @classmethod
    def get_options(cls):
        return [
            CalcOption('Две стороны', ['АВ', 'BC'], Rectangle)
        ]
    
    def __init__(self, side_ab, side_bc):
        self.side_ab = self.side_cd = side_ab
        self.side_bc = self.side_ad = side_bc
        self.angle_a = self.angle_b = self.angle_c = self.angle_d = 90

    def get_area(self):
        return self.side_ab * self.side_bc

# квадрат
class Square(Rectangle):

    @classmethod
    def get_options(cls):
        return [
            CalcOption('По стороне', ['АВ'], Square)
        ]

    def __init__(self, side):
        self.side_ab = self.side_bc = self.side_cd = self.side_ad = side
        self.angle_a = self.angle_b = self.angle_c = self.angle_d = 90

# ромб
class Romb(DrawingRomb, Quadrangle):
    @classmethod
    def get_options(cls):
        return [
            CalcOption('Cторона и угол', ['АВ', 'A'], Romb)
        ]
    
    def __init__(self, side, angle_a):
        if angle_a >= 180 or angle_a <= 0:
            raise FigureError ('Угол должен быть больше 0 и меньше 180')
        self.side_ab = self.side_bc = self.side_cd = self.side_ad = side
        self.angle_a = self.angle_c = angle_a
        self.angle_b = self.angle_d = 180 - angle_a

    def get_area(self):
        return self.side_ab**2 * math.sin(math.radians(self.angle_a))

# трапеция
class Trapezoid(DrawingTrapezoid, Quadrangle):
    @classmethod
    def get_options(cls):
        return [
            CalcOption('Основание, два угла и высота', ['АВ', 'A', 'B', 'h'], cls.trapezoid_by_base_2angles_hight)
        ]

    @staticmethod
    def trapezoid_by_base_2angles_hight(side_ab, angle_a, angle_b, hight):
        angle_c = 180 - angle_b
        angle_d = 180 - angle_a
        side_bc = hight / math.sin(math.radians(angle_b))
        side_cd = side_ab - hight * (1/math.tan(math.radians(angle_a)) + 1/math.tan(math.radians(angle_b)))
        side_ad = hight / math.sin(math.radians(angle_a))

        return Trapezoid(side_ab, side_bc, side_cd, side_ad, angle_a, angle_b, angle_c, angle_d, hight)

    def __init__(self, side_ab, side_bc, side_cd, side_ad, angle_a, angle_b, angle_c, angle_d, hight):
        self.side_ab = side_ab
        self.side_bc = side_bc
        self.side_cd = side_cd
        self.side_ad = side_ad
        self.angle_a = angle_a
        self.angle_b = angle_b
        self.angle_c = angle_c
        self.angle_d = angle_d
        self.hight = hight

    def get_area(self):
        return (self.side_ab + self.side_bc) * self.hight / 2

    def calculate(self):
        return (
            f'Сторона AB {round(self.side_ab, 2)} \n'
            f'Сторона BC {round(self.side_bc, 2)} \n'
            f'Сторона CD {round(self.side_cd, 2)} \n'
            f'Сторона AD {round(self.side_ad, 2)} \n'
            f'Угол A {round(self.angle_a, 1)} \n'
            f'Угол B {round(self.angle_b, 1)} \n'
            f'Угол C {round(self.angle_c, 1)} \n'
            f'Угол D {round(self.angle_d, 1)} \n'
            f'Высота h {round(self.hight, 2)} \n'
            f'Площадь {round(self.get_area(), 2)} \n'
            f'Периметр {round(self.get_perimeter(), 2)} \n'
        )


# сфера, куб, параллелепипед, пирамида, цилиндр, конус.

# Circle(Parameter('diameter', 6400)).calculate()

if __name__ == '__main__':

    triangle = Triangle.get_options()[0].create_obj(4, 5, 6)
    print(triangle.calculate())
