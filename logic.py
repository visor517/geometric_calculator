import abc
import math
from typing import Tuple
# Python 3.8

from drawing import *


class FigureError(Exception):
    pass

class Figure(abc.ABC):

    @abc.abstractclassmethod
    def get_options(cls):
        pass

    @abc.abstractmethod
    def get_stats(self):
        pass

    @abc.abstractmethod
    def get_drawing(self):
        pass


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
            CalcOption('По радиусу', ['Радиус'], cls),
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

    def get_stats(self):
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

    def get_stats(self):
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

    def get_stats(self):
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
            CalcOption('Две стороны', ['АВ', 'BC'], cls)
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
            CalcOption('По стороне', ['АВ'], cls)
        ]

    def __init__(self, side):
        self.side_ab = self.side_bc = self.side_cd = self.side_ad = side
        self.angle_a = self.angle_b = self.angle_c = self.angle_d = 90

# ромб
class Romb(DrawingRomb, Quadrangle):
    @classmethod
    def get_options(cls):
        return [
            CalcOption('Cторона и угол', ['АВ', 'A'], cls)
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
            CalcOption('Основание, два угла и высота', ['АВ', 'A', 'B', 'h'], cls.trapezoid_by_base_2angles_height)
        ]

    @staticmethod
    def trapezoid_by_base_2angles_height(side_ab, angle_a, angle_b, height):
        angle_c = 180 - angle_b
        angle_d = 180 - angle_a
        side_bc = height / math.sin(math.radians(angle_b))
        side_cd = side_ab - height * (1/math.tan(math.radians(angle_a)) + 1/math.tan(math.radians(angle_b)))
        side_ad = height / math.sin(math.radians(angle_a))

        if side_cd < 0:
            raise FigureError('Отрицательное основание. Поменяйте значения!')

        return Trapezoid(side_ab, side_bc, side_cd, side_ad, angle_a, angle_b, angle_c, angle_d, height)

    def __init__(self, side_ab, side_bc, side_cd, side_ad, angle_a, angle_b, angle_c, angle_d, height):
        self.side_ab = side_ab
        self.side_bc = side_bc
        self.side_cd = side_cd
        self.side_ad = side_ad
        self.angle_a = angle_a
        self.angle_b = angle_b
        self.angle_c = angle_c
        self.angle_d = angle_d
        self.height = height

    def get_area(self):
        return (self.side_ab + self.side_bc) * self.height / 2

    def get_stats(self):
        return (
            f'Сторона AB {round(self.side_ab, 2)} \n'
            f'Сторона BC {round(self.side_bc, 2)} \n'
            f'Сторона CD {round(self.side_cd, 2)} \n'
            f'Сторона AD {round(self.side_ad, 2)} \n'
            f'Угол A {round(self.angle_a, 1)} \n'
            f'Угол B {round(self.angle_b, 1)} \n'
            f'Угол C {round(self.angle_c, 1)} \n'
            f'Угол D {round(self.angle_d, 1)} \n'
            f'Высота h {round(self.height, 2)} \n'
            f'Площадь {round(self.get_area(), 2)} \n'
            f'Периметр {round(self.get_perimeter(), 2)} \n'
        )

# сфера
class Sphere(DrawingSpere, Figure):
    @classmethod
    def get_options(cls):
        return [
            CalcOption('По радиусу', ['Радиус'], cls),
            CalcOption('По диаметру', ['Диаметр'], cls.sphere_by_diameter),
            CalcOption('По площади', ['Площадь'], cls.sphere_by_area),
            CalcOption('По объему', ['Объем'], cls.sphere_by_volume),
        ]

    @staticmethod
    def sphere_by_diameter(diameter):
        return Sphere(diameter / 2)

    @staticmethod
    def sphere_by_area(area):
        return Sphere((area / (4 * math.pi))**(0.5))

    @staticmethod
    def sphere_by_volume(volume):
        return Sphere( ((3 * volume) / (4 * math.pi))**(1/3) )

    def __init__(self, radius):
        self.radius = radius

    def get_diameter(self):
        return 2 * self.radius

    def get_area(self):
        return 4 * math.pi * self.radius**2

    def get_volume(self):
        return 4 * math.pi * self.radius**3 / 3

    def get_stats(self):
        return (
            f'Радиус {round(self.radius, 2)} \n'
            f'Диаметр {round(self.get_diameter(), 2)} \n'
            f'Площадь {round(self.get_area(), 2)} \n'
            f'Объем {round(self.get_volume(), 2)} \n'
        )

# цилиндр
class Cylinder(DrawingCylinder, Figure):
    @classmethod
    def get_options(cls):
        return [
            CalcOption('По высоте и радиусу', ['Радиус r', 'Высота h'], cls),
        ]

    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def get_diameter(self):
        return 2 * self.radius

    def get_area(self):
        return 2 * math.pi * self.radius**2 + 2 * math.pi * self.radius * self.height

    def get_volume(self):
        return math.pi * self.radius**2 * self.height

    def get_stats(self):
        return (
            f'Радиус {round(self.radius, 2)} \n'
            f'Диаметр {round(self.get_diameter(), 2)} \n'
            f'Высота {round(self.height, 2)} \n'
            f'Площадь {round(self.get_area(), 2)} \n'
            f'Объем {round(self.get_volume(), 2)} \n'
        )

# куб
class Cube(DrawingCube, Figure):
    @classmethod
    def get_options(cls):
        return [
            CalcOption('Ребро', ['Ребро'], cls),
            CalcOption('Площадь', ['Площадь'], cls.cube_by_area),
            CalcOption('Объем', ['Объем V'], cls.cube_by_volume),
        ]

    @classmethod
    def cube_by_volume(cls, volume):
        return cls(volume**(1/3))

    @classmethod
    def cube_by_area(cls, area):
        return cls((area / 6)**(0.5))

    def __init__(self, side):
        self.side = side

    def get_area(self):
        return 6 * (self.side**2)

    def get_volume(self):
        return self.side**3

    def get_stats(self):
        return (
            f'Ребро {round(self.side, 2)} \n'
            f'Площадь {round(self.get_area(), 2)} \n'
            f'Объем {round(self.get_volume(), 2)} \n'
        )

# параллелепипед        
class Parallelepiped(DrawingParallelepiped, Figure):
    @classmethod
    def get_options(cls):
        return [
            CalcOption('Прямоугольный по трем сторонам', ['a', 'b', 'c'], cls),
        ]

    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def get_volume(self):
        return self.side_a * self.side_b * self.side_c

    def get_area(self):
        return 2 * (self.side_a * self.side_b + self.side_b * self.side_c + self.side_a * self.side_c)

    def get_stats(self):
        return (
            f'Ребро a {round(self.side_a, 2)} \n'
            f'Ребро b {round(self.side_b, 2)} \n'
            f'Ребро c {round(self.side_c, 2)} \n'
            f'Площадь {round(self.get_area(), 2)} \n'
            f'Объем {round(self.get_volume(), 2)} \n'
        )

# пирамида
class Pyramid(DrawingPyramid, Figure):
    @classmethod
    def get_options(cls):
        return [
            CalcOption('Сторона основания и высота', ['Сторна a', 'Высота h'], cls)
        ]

    def __init__(self, side, height):
        self.side = side
        self.height = height

    def get_edge_height(self):
        return (self.height**2 + (self.side / 2)**2)**(0.5)

    def get_area(self):
        return self.side**2 + self.get_edge_height() * self.height * 2

    def get_volume(self):
        return self.side**2 * self.height / 3

    def get_stats(self):
        return (
            f'Сторна основания {round(self.side, 2)} \n'
            f'Высота пирамиды {round(self.height, 2)} \n'
            f'Высота грани {round(self.get_edge_height(), 2)} \n'
            f'Площадь {round(self.get_area(), 2)} \n'
            f'Объем {round(self.get_volume(), 2)} \n'
        )

# конус
class Cone(DrawingCone, Figure):
    @classmethod
    def get_options(cls):
        return [
            CalcOption('Высота и радиус основания', ['Радиус r', 'Высота h'], cls)
        ]

    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def get_diameter(self):
        return 2 * self.radius

    def get_generatrix(self):
        return (self.height**2 + self.radius**2)**(0.5)

    def get_area(self):
        return math.pi * self.radius + self.get_generatrix() + math.pi * self.radius**2

    def get_volume(self):
        return math.pi * self.radius**2 * self.height / 3

    def get_stats(self):
        return (
            f'Радиус основания {round(self.radius, 2)} \n'
            f'Диаметр основания {round(self.get_diameter(), 2)} \n'
            f'Высота {round(self.height, 2)} \n'
            f'Образующая {round(self.get_generatrix(), 2)} \n' 
            f'Площадь {round(self.get_area(), 2)} \n'
            f'Объем {round(self.get_volume(), 2)} \n'
        )

if __name__ == '__main__':

    cube = Cube(100)
    print(cube.cube_by_area(6).get_volume())
