import math

import unittest


class TestCheckEnglish(unittest.TestCase):
    def setUp(self):
        self.c1 = Circle(10)
        self.c2 = Circle(20)
        self.c3 = Circle(50)
        self.c4 = Circle(100)



    def test_length_10(self):
        self.assertEqual(2 * math.pi *10, self.c1.get_length())
    def test_length_20(self):
        self.assertEqual(2 * math.pi *20, self.c2.get_length())
    def test_area_50(self):
        self.assertEqual(math.pi *50**2, self.c3.get_area())
    def test_length_100(self):
        self.assertEqual(math.pi *100, self.c4.get_area())

    # def test_no_punkt(self):
    #     self.assertEqual('absdhisajfi', check_english('ab,sdh!isaj?fi'))
    #
    # def test_no_russian(self):
    #     self.assertEqual('absdhisajfi', check_english('absЖdhшisajЩfi'))
    #
    # def test_no_all(self):
    #     self.assertEqual('absdhisajfi', check_english('ab,Ж sdh!isaЫФАj? fi'))


class Circle():
    def __init__(self, radius):
        self.radius = radius

    def get_length(self):
        return 2 * math.pi * self.radius

    def get_area(self):
        return math.pi * self.radius ** 2

if __name__ == '__main__':
    unittest.main(verbosity=2)
