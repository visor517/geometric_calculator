import abc
import math
from typing import Tuple
# Python 3.8

from drawing import *


class FigureError(Exception):
    pass

class Figure(abc.ABC):

    @abc.abstractmethod
    def calculate(self):
        '''calculates a figure'''

class Parameter:
    def __init__(self, name, value):
        self.name = name
        self.value = value

# варианы построения
# название варианта / необходимые параметры / функция для создания
class CalcOption:
    def __init__(self, name, parameters: Tuple[str], function_for_create):
        self.name = name
        self.parameters = parameters
        self.create_obj = function_for_create

# круг
class Circle(Figure):
    # метод возвращает возможные варианты построения
    @classmethod
    def get_options(cls):
        return [
            CalcOption('По радиусу', ['Радиус'], cls.__init__),
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
        print(f'Радиус {self.radius}')
        print(f'Диаметр {self.get_diameter()}')
        print(f'Площадь {self.get_area()}')
        print(f'Периметр {self.get_perimeter()}')

# треугольник
class Triangle(Figure, DrawingTriangle):

    @classmethod
    def get_options(cls):
        return [
            CalcOption('По трем сторонам', ['АВ', 'BC', 'AC'], cls.triangle_by_sides)
        ]

    @staticmethod
    def triangle_by_sides(side_ab, side_ac, side_bc):
        # проверяем на верность вводных
        if side_ab + side_ac < side_bc or side_ab + side_bc < side_ac or side_bc + side_ac < side_ab:
            raise FigureError('Нарушено правило длин сторон треугольника')
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

# прямоугольник
class Rectangle(Figure):
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    def get_area(self):
        return self.side_a * self.side_b

    def get_perimeter(self):
        return 2 * (self.side_a + self.side_b)

# квадрат
class Square(Figure):
    def __init__(self, side):
        self.side = side

    def get_area(self):
        return self.side**2

    def get_perimeter(self):
        return 4 * self.side

# ромб
class Romb(Figure):
    def __init__(self, side, angle_a, angle_b):
        self.side = side
        self.angle_a = angle_a
        self.angle_b = angle_b

    def get_area(self):
        return self.side**2 * math.sin(self.angle_a)

    def get_perimeter(self):
        return 4 * self.side

# трапеция
class Trapezoid(Figure):
    def __init__(self, side_a, side_b, hight):
        self.side_a = side_a
        self.side_b = side_b
        self.hight = hight

    def get_area(self):
        return (self.side_a + self.side_b) * self.hight / 2

    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c + self.side_d


# сфера, куб, параллелепипед, пирамида, цилиндр, конус.

# Circle(Parameter('diameter', 6400)).calculate()

if __name__ == '__main__':

    triangle = Triangle.get_options()[0].create_obj(4, 5, 6)
    print(triangle.calculate())
