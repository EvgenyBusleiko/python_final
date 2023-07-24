# Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# Дополните id до 10 цифр незначащими нулями.
# В именах первую букву сделайте прописной.
# Добавьте поле хеш на основе имени и идентификатора.
# Получившиеся записи сохраните в json файл, где каждая строка csv файла представлена как отдельный json словарь.
# Имя исходного и конечного файлов передавайте как аргументы функции.
# Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация
# данных), которые вы уже решали. Превратите функции в методы класса, а
# параметры в свойства. Задачи должны решаться через вызов методов
# экземпляра.

import json
import csv


class CsvFile:
    def __init__(self, name):
        self.name = name

    def convert(self):
        data = {}
        with open(self.name, encoding='UTF-8') as f1:
            for line in f1.readlines()[1:]:
                level, access_id, name = line.strip().split()
                # print(level, access_id, name)
                # access_id = f'{int(access_id):010}'
                # print(access_id)
                name = name.capitalize()
                # h_name = hash(name + access_id)
                # print(h_name)
                data[access_id] = [level, name]
            # print(data)
        with open('res3.json', 'w', encoding='UTF-8') as f2:
            json.dump(data, f2, ensure_ascii=False)


CsvFile('res3.csv').convert()
