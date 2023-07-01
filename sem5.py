# a, b, c =('один','два','три')
# print(f'{a=} {b=} {c=}')
# data = [1,4,7,9]
# print(*data)

# data = [1,4,7,9]
# list_iter=iter(data)
# print(list_iter)
# print(next(iter(list_iter)))

# Пользователь вводит строку из четырёх
# или более целых чисел, разделённых символом “/”.
#
# Сформируйте словарь, где:
# второе и третье число являются ключами.
# первое число является значением для первого ключа.
# четвертое и все возможные последующие числа
#        хранятся в кортеже как значения второго ключа.

# a, b, c, *d = input('Введите строку: ').split('/')
# my_dict = {}
# my_dict[b] = a
# my_dict[c] = tuple(d)
#
# print(my_dict)
# Самостоятельно сохраните в переменной строку текста.
# Создайте из строки словарь, где ключ — буква, а значение — код буквы.
# Напишите преобразование в одну строку.

# string_tmp='Hello, world! Python is best'
# # my_dict = {key:ord(key) for key in string_tmp}
# my_dict = {}
# for ch in string_tmp:
#     my_dict[ch]=ord(ch)


# for expression, expr_hash in my_dict.items():
#     print(f"{expression} => {expr_hash}")

# Продолжаем развивать задачу 2.
# Возьмите словарь, который вы получили.
# Сохраните его итератор.
# Далее выведите первые 5 пар ключ-значение,
# обращаясь к итератору, а не к словарю.

# my_iter=iter(my_dict.items())
# for i in range (5):
#     key,value=next(my_iter)
#     print(f"{key} => {value}")
# Создайте генератор чётных чисел от нуля до 100.
# Из последовательности исключите
# числа, сумма цифр которых равна 8.
# Решение в одну строку.

# from random import random as rnd
#
# generator = (i for i in range(101) if (i % 2 == 0) and (sum(map(int, str(i))) != 8))
# for i in range (51):
#     print(next(generator))
# Напишите программу, которая выводит
# на экран числа от 1 до 100.
# При этом вместо чисел, кратных трем,
# программа должна выводить слово «Fizz»
# Вместо чисел, кратных пяти — слово «Buzz».
# Если число кратно и 3, и 5, то программа
# должна выводить слово «FizzBuzz».
# *Превратите решение в генераторное выражение

# some_generator2 = (
#     ("FizzBuzz" if x % 3 == 0 and x % 5 == 0 else "Fizz" if x % 3 == 0 else "Buzz" if x % 5 == 0 else x) for x in
#     range(1, 101))
# for i in range(1, 101):
#     print(next(some_generator2))

# for i in range(1,101):
#     if (i%3==0) and (i%5==0):
#         print(f'{i}=FizzBuzz')
#     elif (i%3==0):
#         print(f'{i}=Fizz')
#     elif (i%5==0):
#         print(f'{i}=Buzz')
#     else:
#         print(i)
# some_generator3 = (
#     ("FizzBuzz" for x in range (1,101)if x % 3 == 0 ) )
# for i in range(1, 101):
#     print(next(some_generator3))

# Выведите в консоль таблицу умножения
# от 2х2 до 9х10 как на школьной тетрадке.
# Таблицу создайте в виде однострочного генератора, где каждый элемент генератора — отдельный пример таблицы умножения.
# Для вывода результата используйте «принт»
# без перехода на новую строку.

# generator = (print(f'{i}x{j}={i * j}') for i in range(2, 10) for j in range(2, 11))
# for k in range(87):
#     next(generator)
# Создайте функцию-генератор.
# Функция генерирует N простых чисел,
# начиная с числа 2.
# Для проверки числа на простоту используйте правило: «число является простым, если делится нацело только на единицу и на себя».
def simple_dif(tmp):
    for i in range(2, tmp):
        check = False
 
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                check = True
                break
        if not check:
            yield i


dig = int(input('Введите целое число: '))
func = simple_dif(dig)
for k in range(2, 10):
    print(next(func))
