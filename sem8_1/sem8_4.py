# Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# Дополните id до 10 цифр незначащими нулями.
# В именах первую букву сделайте прописной.
# Добавьте поле хеш на основе имени и идентификатора.
# Получившиеся записи сохраните в json файл, где каждая строка csv файла представлена как отдельный json словарь.
# Имя исходного и конечного файлов передавайте как аргументы функции.

import json
import csv


def csv_to_json(name):
    data = {}
    with open(name, encoding='UTF-8') as f1:

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



csv_to_json('res3.csv')
