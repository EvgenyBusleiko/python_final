# Напишите функцию в шахматный модуль.
# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте различный случайные  варианты и выведите 4 успешных расстановки.
from random import randint as rd


from sem6.sem6_ht2_Busleiko import check_chessboard


def get_chessboard():
    chessboard = []

    for x in range(1, 9):
        line = []
        y = rd(1, 8)
        for i in range(1, 9):
            if i != y:
                line.append(0)
            else:
                line.append(1)
        chessboard.append(line)
    return chessboard


def print_chessboard(chessboard):
    for i in chessboard:
        print(i)


count = 1
for i in range(4):
    check = False
    while check == False:
        chessboard = get_chessboard()
        check = check_chessboard(chessboard)
        count += 1
    print(f'Попытка №{count}')
    print_chessboard(chessboard)
