# Доработайте прошлую задачу.
# Добавьте сравнение прямоугольников по площади
# Должны работать все шесть операций сравнения

class Rectangle:
    """
                    Данный класс хранит значения периметров,
                    умеет их сравнивать """
    def __init__(self, p):
        self.p = p

    def __add__(self, other):
        return Rectangle(self.p + other.p)

    def __sub__(self, other):
        return Rectangle(abs(self.p - other.p))

    def __eq__(self, other):
        return self.p == other.p

    def __ne__(self, other):
        return self.p != other.p

    def __lt__(self, other):
        return self.p < other.p

    def __le__(self, other):
        return self.p <= other.p

    def __gt__(self, other):
        return self.p > other.p

    def __ge__(self, other):
        return self.p >= other.p

    def __str__(self):
        return f'{self.p}'

r1 = Rectangle(5)
r2 = Rectangle(5)

print(r1.__eq__(r2)) #True
print(r1.__ne__(r2)) #False
print(r1.__lt__(r2)) #False
print(r1.__le__(r2))#True
print(r1.__gt__(r2))#False
print(r1.__ge__(r2))#True