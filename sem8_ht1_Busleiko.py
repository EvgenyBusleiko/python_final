#
# Напишите функцию, которая получает на вход директорию и рекурсивно
# обходит её и все вложенные директории. Результаты обхода сохраните в
# файлы json, csv и pickle.
# ○ Для дочерних объектов указывайте родительскую директорию.
# ○ Для каждого объекта укажите файл это или директория.
# ○ Для файлов сохраните его размер в байтах, а для директорий размер
# файлов в ней с учётом всех вложенных файлов и директорий.
# Соберите из созданных на уроке и в рамках домашнего задания функций
# пакет для работы с файлами разных форматов.

import os
import csv
import json
import pickle


def structure_of_directory(dir):
    dict = {}
    os.chdir(dir)
    for file in os.listdir(f'D:\Geek\Python_final\{dir}'):
        file_size = os.path.getsize(f'D:\Geek\Python_final\{dir}/' + file)
        dict[file] = [os.getcwd(), 'f', file_size]
    for _, dir_name, file_name in os.walk(os.getcwd()):
        # print(f'{dir_name = }\n{file_name = }\n')

        for directory in dir_name:
            # print(directory)
            size = 0
            for file in os.listdir(directory):
                file_size = os.path.getsize(directory + '/' + file)
                dict[file] = [directory, 'f', file_size]
                size += file_size
            dict[directory] = [os.getcwd(), 'd', size]
    with open('test.json', 'w', encoding='UTF-8') as f1:
        json.dump(dict, f1, ensure_ascii=False)


def json_to_csv(name):
    new_name = name.split('.')[0]
    csv_file_name = new_name + '.csv'
    with open(name, encoding='UTF-8') as f1, \
            open(csv_file_name, 'w', newline='', encoding='UTF-8') as f2:
        data = json.load(f1)
        rows = []
        for name, value in data.items():
            directory, type_f, size_f = value
            rows.append({'directory': directory, 'type': type_f, 'size_f': int(size_f), 'name': name})
        csv_write = csv.DictWriter(f2, fieldnames=['directory', 'type', 'size_f', 'name'], dialect='excel-tab')
        csv_write.writeheader()
        csv_write.writerows(rows)


def json_to_pickle(name):
    new_name = name.split('.')[0]
    pickle_file_name = new_name + '.pickle'
    # print(pickle_file_name)
    with open(name, 'r', encoding='UTF-8') as f1:
        with open(pickle_file_name, 'wb') as f2:
            data = json.load(f1)
            pickle.dump(data, f2)


structure_of_directory('Testdir')
json_to_csv('test.json')
json_to_pickle('test.json')
