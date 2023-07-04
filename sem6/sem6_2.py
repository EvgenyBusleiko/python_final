# Создайте модуль с функцией внутри.
# Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество попыток.
# Внутри генерируется случайное число в указанных границах и пользователь должен угадать его за заданное число попыток.
# Функция выводит подсказки “больше” и “меньше”.
# Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.

from random import randint as rd


def guess(down, up, tries):
    if down > up:
        up, down = down, up
    aim = rd(down, up)
    count = 0
    while count < tries:
        try:
            tmp = int(input('Введите целое число: '))
        except:
            print('Нужно ввести ЦЕЛОЕ число')
            count+=1
            continue
        if tmp < aim:
            print('Число больше')
        elif tmp > aim:
            print('Число меньше')
        else:
            return True
        count += 1
    return False


if __name__=='__main__':
    print(guess(10,100,9))
