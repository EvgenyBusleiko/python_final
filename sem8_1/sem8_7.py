# Прочитайте созданный в прошлом задании csv файл без
# использования csv.DictReader.
# Распечатайте его как pickle строку.

import pickle

def csv_to_picklestring(file_name):
    data={}
    with open(file_name, encoding='UTF-8') as f1:
        for line in f1.readlines():
            access_id, level, name = line.strip().split()
            data[access_id] = [level, name]
        res = pickle.dumps(data, protocol=pickle.DEFAULT_PROTOCOL)
        print(f'{res = }')


csv_to_picklestring('../res3_1.csv')