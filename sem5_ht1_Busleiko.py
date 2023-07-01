# 1. Напишите функцию, которая принимает на вход строку
# — абсолютный путь до файла. Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
def way(tmp):
    extention = tmp.rfind('.')
    file_name = tmp.rfind('/')
    size = len(tmp)
    final = (tmp[:file_name + 1], tmp[file_name + 1:extention], tmp[extention + 1:size])
    return final


# tmp_str = input('Введите строку : ')
tmp_str = "C:/win/user/doc.txt"

print(way(tmp_str))
