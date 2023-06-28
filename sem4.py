# my_dict = {'two': 2,
#            'one': 1,
#            'four': 4,
#            'three': 3,
#            'ten': 10, }
# print(sorted(my_dict.values()))

# def nunerated_word(tmp):
#     tmp = data.split()
#     tmp.sort()
#     longest = len(max(tmp, key=len))
#
#     for num, i in enumerate(tmp, 1):
#         print(f'{num} {i:>{longest}}')
#
#
# data = input('Введите строку: ')
# nunerated_word(data)

# def unicode_list(tmp):
#     chr_list = []
#     set_of_chr = set(tmp)
#     for i in set_of_chr:
#         chr_list.append(ord(i))
#     return sorted(chr_list, reverse=True)
#
#
# data = input('Введите строку: ')
#
# print(unicode_list(data))


# print(ord('Ϩ'))
# def two_numbers_unicode(data):
#     unicode_dict={}
#     num_1, num_2 = map(int, data.split())
#
#     if num_1 > num_2:
#         num_1, num_2 = num_2,num_1
#     for i in range (num_1,num_2+1,1):
#         unicode_dict[i]=chr(i)
#     return unicode_dict
#
#
# data = input('Введите строку: ')
#
# print(two_numbers_unicode(data))
# def list_sort(tmp_list):
#     for i in range(len(tmp_list)):
#         for j in range(len(tmp_list) - 1):
#             if tmp_list[j] > tmp_list[j + 1]:
#                 tmp_list[j], tmp_list[j + 1] = tmp_list[j + 1], tmp_list[j]
#     return tmp_list
#
#
# list_of_numbers = [4, 1, 5, 12, 2, 6, 7, 8]
#
# print(list_sort(list_of_numbers))
# from decimal import Decimal
#
#
# def extrasalary(names, salary, extrasalary):
#     final_dict = {}
#     for i in range(len(names)):
#         final_dict[names[i]] = Decimal(salary[i]) * Decimal(extrasalary[i].replace('%', ''))
#     return final_dict
#
#
# list_of_names = ['Иван', 'Дмитрий', 'Мария']
# list_of_salary = [100, 120, 140]
# list_of_extrasalary = ['10.2%', '14.3%', '15.6%']
#
# # print(extrasalary(list_of_names, list_of_salary, list_of_extrasalary))
# for name, award in extrasalary(list_of_names, list_of_salary, list_of_extrasalary).items():
#     print(f"{name} => {award}")

# def two_numbers(num_1, num_2, tmp):
#     s = 0
#     if num_1 > num_2:
#         num_1, num_2 = num_2, num_1
#
#     for i in tmp[num_1+1: num_2]:
#         s += i
#     return s
#
#
# list_of_numbers = [4, 1, 5, 12, 2, 6, 7, 8]
#
# index_1 = 0
# index_2 = 2
#
# print(two_numbers(index_1, index_2, list_of_numbers))

def balance(tmp_dict):
    final_balance = []
    for i in tmp_dict.values():
        final_balance.append(sum(i))
    return all([i if i > 0 else 0 for i in final_balance])


old_dict = {'Вода': [5000, 1000, -3000],
            'Нож': [2000, -1000, -7000],
            }
print(balance(old_dict))


