# Решить задания, которые не успели решить на семинаре.
# Добавьте ко всем задачам с семинара строки документации и методы вывода информации на печать.
# Создайте класс Матрица. Добавьте методы для: - вывода на печать,
# сравнения,
# сложения,
# *умножения матриц
from random import randint as rnd


class Matrix:
    """
            Данный класс  является классом для работы с матрицами,
             с несколько странной логикой:
             1. Складывать может любые матрицы (дописывает нули на недостающие места)
             2. Матрицы считаются равными, если имеют одинаковое количество строк и столбцов
             3. Перемножать умеет только квадратные матрицы
             4. Умеет генерировать матрицы заданного размера, заполненные случайными элементами от 1 до 10
             5. Умеет выводить матрицу на печать

             Надеюсь так можно было =)
            """

    def __init__(self, row, col):
        self.row = row
        self.col = col

    def make_matrix(self, row):
        matrix = []
        for i in range(self):
            line = []
            for j in range(row):
                tmp = rnd(1, 10)
                line.append(tmp)
            matrix.append(line)
        return matrix

    def check_matrix(self, b):
        line = []
        max_col = (max(len(self), len(b)))
        max_line = (max(len(self[0]), len(b[0])))
        # print(max_col, max_line)
        for i in range(0, max_col):
            if len(self) <= i:
                self.append(line)
            if len(b) <= i:
                b.append(line)
            for j in range(0, max_line):
                if len(self[i]) <= j:
                    self[i].append(0)
                if len(b[i]) <= j:
                    b[i].append(0)

        return self, b

    def print_matrix(self):
        for i in range(len(self)):
            print(self[i])
        print()

    def __add__(self, other):
        self, other = self.check_matrix(other)
        matrix = []
        for i in range(len(self)):
            line = []
            for j in range(len(self[i])):
                line.append(self[i][j] + other[i][j])

            matrix.append(line)
        print(self)
        print(other)
        return matrix

    def __eq__(self, other):
        # print(len(self),len(other),len(self[0]),len(other[0]))
        if (len(self) == len(other)) and (len(self[0]) == len(other[0])):
            return True
        else:
            return False

    def __mul__(self, other):
        if not Matrix.__eq__(self, other):
            print('Не могу перемножить матрицы, так как они не равны!')
            # Понимаю, что это можно не проверять, хотел функцию проверить

        elif len(self) != len(self[0]):
            print('Я умею  перемножать только квадратные матрицы!')
        else:
            result = []
            for i in range(len(self)):
                line = []
                for j in range(len(other[0])):
                    line.append(0)
                result.append(line)

            for i in range(len(self)):
                for j in range(len(other[0])):
                    for k in range(len(other)):
                        result[i][j] += self[i][k] * other[k][j]
            Matrix.print_matrix(result)


a = Matrix.make_matrix(2, 2)
b = Matrix.make_matrix(2, 3)

Matrix.print_matrix(a)

Matrix.print_matrix(b)

print(Matrix.__eq__(a, a))
Matrix.__mul__(a, a)
