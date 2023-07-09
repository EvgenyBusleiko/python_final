# Дорабатываем функции из предыдущих задач.
# Генерируйте файлы в указанную директорию — отдельный параметр функции.
# Отсутствие/наличие директории не должно вызывать ошибок в работе функции (добавьте проверки).
# Существующие файлы не должны удаляться/изменяться в случае совпадения имён.

import os
import random


def file_extensions_folder(folder, extensions, min_length=6, max_length=30, min_bytes=256, max_bytes=4096):
    if not os.path.isdir(folder):
        os.mkdir(folder)
    os.chdir(folder)
    for extension in extensions:
        for i in range(extensions[extension]):
            check = True
            while check:
                name = ''
                for j in range(random.randint(min_length, max_length)):
                    tmp = chr(random.randint(97, 122))
                    name = name + tmp
                if not os.path.isfile(f'{name}.{extension}'):
                    check = False

            with open(f'{name}.{extension}', 'w', encoding='UTF-8') as f:
                for k in range(random.randint(min_bytes, max_bytes)):
                    print(chr(random.randint(97, 122)), file=f, end='')


file_extensions_folder('tmp1',{'jpg': 2, 'pdf': 1})
