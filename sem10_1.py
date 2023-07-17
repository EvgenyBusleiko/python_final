# Создайте класс окружность.
# Класс должен принимать радиус окружности при создании экземпляра.
# У класса должно быть два метода, возвращающие длину окружности и её площадь.
import math


class Circle():
    def __init__(self, radius):
        self.radius = radius

    def get_length(self):
        return 2 * math.pi * self.radius

    def get_area(self):
        return math.pi * self.radius ** 2


c1 = Circle(10)
print(c1.get_length())
print(c1.get_area())
