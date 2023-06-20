# Напишите программу, которая получает целое
# число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex
# используйте для проверки своего результата.

HEX = 16



def get_result(num: int, divider: int):
    digits = '0123456789abcdef'
    result = ""
    while num > 0:
        result = digits[num % divider]+result
        num //= divider
    return result


num=int (input('Введите число: '))


print(f"{hex(num)} == {get_result(num, HEX)}")
