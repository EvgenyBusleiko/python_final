# Создайте класс прямоугольник.
# Класс должен принимать длину и ширину при создании экземпляра.
# У класса должно быть два метода, возвращающие периметр и площадь.
# Если при создании экземпляра передаётся только одна сторона, считаем что у нас квадрат.

class Rectangle:
    def __init__(self, a, b=None):
        self.a = a
        self.b = a if not b else b

    def get_length(self):
        return 2 * (self.a + self.b)

    def get_area(self):
        return self.a * self.b


c1 = Rectangle(10, 5)
print(c1.get_length())
print(c1.get_area())
