# Создайте класс студента.
# ○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и
# наличие только букв.
# ○ Названия предметов должны загружаться из файла CSV при создании
# экземпляра. Другие предметы в экземпляре недопустимы.
# ○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты
# тестов (от 0 до 100).
# ○ Также экземпляр должен сообщать средний балл по тестам для каждого
# предмета и по оценкам всех предметов вместе взятых.

import csv
from random import randint as rnd


class Range:

    def __set_name__(self, owner, name):
        self.param_name = '_' + name

    def validate(self, value):

        if all(x.isalpha() or x.isspace() for x in value):
            tmp = value.title()
            return tmp
        else:
            raise TypeError(f'Значение {value} должно содержать только буквы или пробел')

    def __set__(self, instance, value):
        value = self.validate(value)
        print(value)
        setattr(instance, self.param_name, value)

    def __get__(self, instance, owner):
        return getattr(instance, self.param_name)


class Student:
    full_name = Range()

    def reading_from_csv(self):
        subjects = []
        with open('res12.csv', encoding='UTF-8') as f1:
            for line in f1.readlines()[1:]:
                subjects.append(line.rstrip())

            return subjects

    def __init__(self, full_name):
        total_point = 0
        average_test = 0
        self.full_name = full_name
        self.subjects_dict = {}
        self.subjects = self.reading_from_csv()
        for i in self.subjects:
            point = rnd(2, 5)
            test = rnd(0, 100)
            self.subjects_dict[i] = [point, test]
            average_test += test
            total_point += point
        self.average_test = average_test / len(self.subjects)
        self.total_point = total_point

    def __repr__(self):
        return f'Студент {self.full_name},\nимеет следующие оценки и результаты тестов {self.subjects_dict}\n\
Средний балл по тестам {self.average_test} и суммарную оценку {self.total_point}'


s = Student('john ivanovich lenon')

print(s.__repr__())
