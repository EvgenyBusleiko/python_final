from string import ascii_letters as as_lett
import unittest

class TestCheckEnglish(unittest.TestCase):
    def test_no_change(self):
        self.assertEqual('absdhisajfi',check_english ('absdhisajfi'))
    def test_no_case(self):
        self.assertEqual('absdhisajfi',check_english ('aBsdHisaJfi'))
    def test_no_punkt(self):
        self.assertEqual('absdhisajfi',check_english ('ab,sdh!isaj?fi'))
    def test_no_russian(self):
        self.assertEqual('absdhisajfi',check_english ('absЖdhшisajЩfi'))
    def test_no_all(self):
        self.assertEqual('absdhisajfi',check_english ('ab,Ж sdh!isaЫФАj? fi'))


def check_english(str1):
    # """
    # >>> check_english ('absdhisajfi')
    # 'absdhisajfi'
    # >>> check_english ('aBsdHisaJfi')
    # 'absdhisajfi'
    # >>> check_english ('ab,sdh!isaj?fi')
    # 'absdhisajfi'
    # >>> check_english ('absЖdhшisajЩfi')
    # 'absdhisajfi'
    # >>> check_english ('ab,Ж sdh!isaЫФАj? fi')
    # 'ab sdhisaj fi'
    #
    # """

    str2 = ''
    for i in str1:
        if i in as_lett or i == ' ':
            str2 += i
    return str2.lower()

if __name__ == '__main__':
    unittest.main(verbosity=2)