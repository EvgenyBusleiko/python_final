# Добавьте возможность изменять длину и ширину прямоугольника и встройте контроль недопустимых значений (отрицательных).
# Используйте декораторы свойств.

class Rectangle:
    def __init__(self, a, b=None):
        self.a = a
        self.b = a if not b else b

    def get_length(self):
        return 2 * (self.a + self.b)

    def get_area(self):
        return self.a * self.b

    @property
    def a(self):
        return self._a

    @property
    def b(self):
        return self._b

    @a.setter
    def a(self, value):
        if value > 0:
            self._a = value
        else:
            raise ValueError('Значение должно быть больше нуля')

    @b.setter
    def b(self, value):
        if value > 0:
            self._b = value
        else:
            raise ValueError('Значение должно быть больше нуля')


r = Rectangle(10, 6)
r.b = 15

print(r.b)
