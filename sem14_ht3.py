# Возьмите  задачу из тех, что были на прошлых
# семинарах или в домашних заданиях.
# Напишите к ним тесты.
# 2-5 тестов на задачу в трёх вариантах:
# ○ pytest.

import pytest


def test_get_length_double():
    c1 = Rectangle(4, 4)
    assert(16 == Rectangle.get_length(c1))


def test_get_length_one():
    c2 = Rectangle(5)
    assert(20 == Rectangle.get_length(c2))


def test_get_length_wrong():
    c3 = Rectangle(10, 4)
    assert(16 == Rectangle.get_length(c3))


def test_get_area_double():
    c1 = Rectangle(4, 4)
    assert(16 == Rectangle.get_area(c1))


def test_get_area_one():
    c2 = Rectangle(5)
    assert(25 == Rectangle.get_area(c2))


def test_get_area_wrong():
    c3 = Rectangle(10, 4)
    assert(16 == Rectangle.get_area(c3))


class Rectangle:
    def __init__(self, a, b=None):
        self.a = a
        self.b = a if not b else b

    def get_length(self):
        return 2 * (self.a + self.b)

    def get_area(self):
        return self.a * self.b


if __name__ == '__main__':
    pytest.main()
