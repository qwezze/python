'''
Задача: Создать базовый класс Shape для геометрических фигур. Наследовать от него классы Rectangle и Circle, которые будут иметь методы для вычисления площади и периметра.
'''
import math
class Shape:
    def area(self):
        print("Данный метод обязательный")
    def perimetr(self):
        print("Данный метод обязательный")
class Rectangle(Shape):
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def area(self):
        return self.a * self.b
    def perimetr(self):
        return (self.a + self.b) * 2
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return math.pi * self.radius**2
    def perimetr(self):
        return 2 * math.pi * self.radius

a = Rectangle(2, 3)
print(a.area())
print(a.perimetr())
b = Circle(11)
print(b.area())
print(b.perimetr())


