# Решить задачи, которые не успели решить на семинаре.
# Напишите функцию группового переименования файлов. Она должна:
# принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# принимать параметр количество цифр в порядковом номере.
# принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# принимать параметр расширение конечного файла.
# принимать диапазон сохраняемого оригинального имени.
# Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
# К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
# 3.Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.

import os
from os import listdir
from os.path import isfile, join


def file_rename(name, num_dig, extension, final_extension, from_name=0, to_name=0):
    count = 1
    onlyfiles = [f for f in listdir(os.getcwd()) if isfile(join(os.getcwd(), f))]
    print(onlyfiles)

    for file in onlyfiles:
        if file.split('.')[-1] == extension:
            name_part = file.split('.')[0][from_name:to_name]
            if len(str(count)) != num_dig:
                tmp = (num_dig - len(str(count))) * '0'
                file_count = (f'{tmp}{count}')
                print(file_count)
            final_name = (f'{name_part}{name}{file_count}.{final_extension}')
            print(file)
            os.rename(file, final_name)
            print(final_name)
            count += 1


if __name__ == '__main__':
    file_rename('Polina', 5, 'jpg', 'txt', 0, 0)

