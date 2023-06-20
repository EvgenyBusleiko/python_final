# Напишите программу, которая принимает две строки
# вида “a/b” — дробь с числителем и знаменателем.
# Программа должна возвращать сумму
# и *произведение дробей. Для проверки своего
# кода используйте модуль fractions.

from fractions import Fraction
from re import split


def check_fraction(first, second):
    first = int(first)
    second = int(second)
    if first <= second:
        minimum = first
    else:
        minimum = second
    for i in range(minimum, 1, -1):

        if (second % i == 0) and (first % i == 0):
            second /= i
            first /= i
            break

    return int(first), int(second)


str_1 = input('Введите первую дробь вида x/y: ')
str_2 = input('Введите первую дробь вида x/y: ')

result_sum = Fraction(str_1) + Fraction(str_2)
result_mult = Fraction(str_1) * Fraction(str_2)

fraction_1 = split('/', str_1)
fraction_2 = split('/', str_2)

down = int(fraction_1[1]) * int(fraction_2[1])

up = int(fraction_1[0]) * down / int(fraction_1[1]) + int(fraction_2[0]) * down / int(fraction_2[1])
result = check_fraction(up, down)
print(f"Результат сложения дробей {result[0]}/{result[1]}")
print("Проверка - ", result_sum)
up = int(fraction_1[0]) * int(fraction_2[0])
result = check_fraction(up, down)
print(f"Результат умножения дробей {result[0]}/{result[1]}")
print("Проверка - ", result_mult)
