# Напишите функцию принимающую на вход только ключевые
# параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента. Если
# ключ не хешируем, используйте его строковое представление.

def hash_dict(tmp):
    my_dict = {}
    for key in tmp:
        if key not in my_dict.keys():
            my_dict[key] = hash(key)
            print()
    return my_dict


my_list = ['sa', 'rt', 'er']

hash_dict(my_list)
for expression, expr_hash in hash_dict(my_list).items():
    print(f"{expression} => {expr_hash}")

# def school_print(**kwargs):
#     for key, value in kwargs.items():
#         print(f'По предмету "{key}" получена оценка {value}')
# school_print(химия=5, физика=4, математика=5, физра=5)
