# Создайте функцию, которая удаляет из текста все символы кроме букв латинского алфавита и пробелов.
# Возвращается строка в нижнем регистре.
from string import ascii_letters as as_lett


def check_english(str1):
    str2 = ''
    for i in str1:
        if i in as_lett or i == ' ':
            str2 += i
    return str2.lower()

print(check_english('aofhqfhioqJJJJ99989:*:?:;№:ПППП   ывфыв   шФГВШВГ'))
