'''
Создайте класс `Shape` (Фигура) с методом `area` (площадь), который возвращает 0. Реализуйте два подкласса: `Rectangle` (Прямоугольник) и `Circle` (Круг), каждый из которых переопределяет метод `area` для вычисления площади соответствующей фигуры.
- Класс `Rectangle` должен принимать длину и ширину и вычислять площадь.
- Класс `Circle` должен принимать радиус и вычислять площадь круга.
'''
import math

class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def area(self, a, b):
        return a*b

class Circle(Shape):
    def area(self, r ):
        return math.pi*r**2

rec = Rectangle()
print(rec.area(10,20))

cir = Circle()
print(cir.area(15))
