'''
При помощи ООП спроектировать и реализовать геометрический калькулятор
для вычислений, производимых над фигурами. Калькулятор должен поддерживать вычисления для плоских и объемных фигур.
Плоские фигуры: круг, квадрат, прямоугольник, треугольник, трапеция, ромб.
Объемные фигуры: сфера, куб, параллелепипед, пирамида, цилиндр, конус.
Реализовать как минимум один общий метод вычисления для всех фигур и как минимум один специфичный для определенных фигур. 
Например, площадь – общий метод для всех фигур, медиана – специфичный метод для ряда фигур.
Необходимо: реализовать графический интерфейс для возможностей взаимодействия пользователя с программой и визуализации 
фигур (с учетом введенных параметров фигуры).
При реализации использовать все виды методов: статический, метод класса и экземпляра.
'''

import abc
import math
from typing import Tuple
# Python 3.8


class FigureError(Exception):
    pass

class Figure(abc.ABC):

    @abc.abstractmethod
    def plot(self):
        '''plots a figure'''

class Parameter:
    def __init__(self, name, value):
        self.name = name
        self.value = value

# варианы построения
# название варианта / необходимые параметры / функция для создания
class CulcOption:
    def __init__(self, name, parameters: Tuple[str], function_for_init):
        self.name = name
        self.parameters = parameters
        self.init = function_for_init

# круг
class Circle(Figure):
    # метод возвращает возможные варианты построения
    @classmethod
    def get_options(cls):
        return [
            CulcOption('По радиусу', ['Радиус'], cls.__init__),
            CulcOption('По диаметру', ['Диаметр'], cls.circle_by_diameter),
            CulcOption('По площади', ['Площадь'], cls.circle_by_area),
            CulcOption('По периметру', ['Периметр'], cls.circle_by_perimeter),
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

    def plot(self):
        print(f'Радиус {self.radius}')
        print(f'Диаметр {self.get_diameter()}')
        print(f'Площадь {self.get_area()}')
        print(f'Периметр {self.get_perimeter()}')

# треугольник
class Triangle(Figure):

    @classmethod
    def get_options(cls):
        return [
            CulcOption('По трем сторонам', ['АВ', 'BC', 'AC'], cls.triangle_by_sides) 
        ]

    @staticmethod
    def triangle_by_sides(side_ab, side_ac, side_bc):
        # проверяем на верность вводных
        if side_ab + side_ac < side_bc or side_ab + side_bc < side_ac or side_bc + side_ac < side_ab:
            raise FigureError('Нарушено правило длин сторон треугольника')
        # вычисление углов
        angle_a = round(math.degrees(math.acos((side_ab**2 + side_ac**2 - side_bc**2) / (2 * side_ab * side_ac))), 0)
        angle_b = round(math.degrees(math.acos((side_ab**2 + side_bc**2 - side_ac**2) / (2 * side_ab * side_bc))), 0)
        angle_c = round(math.degrees(math.acos((side_ac**2 + side_bc**2 - side_ab**2) / (2 * side_ac * side_bc))), 0)
        return Triangle(side_ab, side_ac, side_bc, angle_a, angle_b, angle_c)
        


    def __init__(self, side_ab, side_ac, side_bc, angle_a, angle_b, angle_c):
        self.side_ab = side_ab
        self.side_ac = side_ac
        self.side_bc = side_bc
        self.angle_a = angle_a
        self.angle_b = angle_b
        self.angle_c = angle_c

    def get_area(self):
        p = self.get_perimeter() / 2    
        return (p * (p - self.side_ab) * (p - self.side_bc) * (p - self.side_ac))**(0.5)

    def get_perimeter(self):
        return self.side_ab + self.side_bc + self.side_ac

    def plot(self):
        print(f'Сторона AB {self.side_ab}')
        print(f'Сторона AC {self.side_ac}')
        print(f'Сторона BC {self.side_bc}')
        print(f'Угол A {self.angle_a}')
        print(f'Угол B {self.angle_b}')
        print(f'Угол C {self.angle_c}')
        print(f'Площадь {self.get_area()}')
        print(f'Периметр {self.get_perimeter()}')

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

# Circle(Parameter('diameter', 6400)).plot()

if __name__ == '__main__':

    triangle = Triangle.get_options()[0].init(4, 5, 6)
    triangle.plot()
