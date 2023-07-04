# Улучшаем задачу 2.
# Добавьте возможность запуска функции “угадайки” из модуля в командной строке терминала.
# Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
# Для преобразования строковых аргументов командной строки в числовые параметры используйте генераторное выражение.

from random import randint as rd
import sys


def guess(down=10, up=100, tries=10):
    if down > up:
        up, down = down, up
    aim = rd(down, up)
    count = 0
    while count < tries:
        try:
            tmp = int(input('Введите целое число: '))
        except:
            print('Нужно ввести ЦЕЛОЕ число')
            count += 1
            continue
        if tmp < aim:
            print('Число больше')
        elif tmp > aim:
            print('Число меньше')
        else:
            return True
        count += 1
    return False



if __name__ == '__main__':
    print(sys.argv)
    if len(sys.argv) == 2:
        tries =int(sys.argv[1])
        print(guess(tries=tries))
    elif len(sys.argv) == 4:
        up, down, tries = (int(i) for i in sys.argv[1:])
        print(guess(up, down, tries))
    else:
        print('Неверное количество аргументов')
