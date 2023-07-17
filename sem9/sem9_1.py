# Создайте функцию-замыкание, которая запрашивает два целых числа:
# от 1 до 100 для загадывания,
# от 1 до 10 для количества попыток
# Функция возвращает функцию, которая через консоль просит угадать загаданное число за указанное число попыток.
import random


def create_guess_game(answer):
    def guess_game(attemps):
        for _ in range(attemps):
            guess = int(input('Введите число: '))
            if guess == answer:
                print('Угадали!')
                return
            elif guess < answer:
                print('Число больше')
            else:
                print('Число меньше')
        print('Не угадали!')


    return guess_game

num1 = random.randint(1, 10)
num2 = random.randint(1, 100)
create_guess_game(num1)(num2)

