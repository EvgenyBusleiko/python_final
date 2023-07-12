# Напишите функцию, которая генерирует псевдоимена.
# Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# Полученные имена сохраните в файл.

import random


def fill_file(name,count_lines):
    with open(name,'a',encoding='UTF-8') as f:
        for j in range (count_lines):
            length=random.randint(4,7)
            check=True
            while check:
                password=''
                for i in range(length):
                    tmp=chr(random.randint(97,122))
                    password=password+tmp
                    if tmp in ['a','o','u','i','e']:
                        check=False

            print(password.capitalize(),file=f)

fill_file('2.txt',10)

