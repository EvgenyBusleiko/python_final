# Возьмите  задачу из тех, что были на прошлых
# семинарах или в домашних заданиях.
# Напишите к ним тесты.
# 2-5 тестов на задачу в трёх вариантах:
# ○ doctest

import doctest


class Rectangle:
    def __init__(self, a, b=None):
        self.a = a
        self.b = a if not b else b

    def get_length(self):
        """

        >>> c1 = Rectangle(4, 4)
        >>> Rectangle.get_length (c1)
        16
        >>> c2 = Rectangle(5)
        >>> Rectangle.get_length (c2)
        20
        >>> c3 = Rectangle(10, 4)
        >>> Rectangle.get_length (c3)
        22
        """
        return 2 * (self.a + self.b)

    def get_area(self):
        """
        >>> c1 = Rectangle(4, 4)
        >>> Rectangle.get_area(c1)
        16
        >>> c2 = Rectangle(5)
        >>> Rectangle.get_area(c2)
        25
        >>> c3 = Rectangle(10, 4)
        >>> Rectangle.get_area(c3)
        22
        """
        return self.a * self.b


if __name__ == '__main__':
    doctest.testmod(verbose=True)
# c1 = Rectangle(10, 5)
# print(c1.get_length())
# print(c1.get_area())
