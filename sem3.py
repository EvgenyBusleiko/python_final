# my_list =[2,4,6,2,8,10,12]
#
# unique_list=[]
# for num in my_list:
#     if num not in unique_list:
#         unique_list.append(num)
# print(unique_list)
#
# new_list_2 = list(set(my_list))
#
# print(new_list_2)

# data = input('Введите число: ')
# if data.isdigit():
#     new_data=int(data)
#     print("Целое положительное")
# else:
#     try:
#         new_data=float(data)
#         print("Вещественное число")
#     except ValueError:
#         if data.islower():
#             new_data=data.upper()
#             print(new_data)
#         else:
#             new_data=data.lower()
#             print(new_data)
# my_data =(4,6,"2",8,10,12)
# new_dict={}
# for i in my_data:
#     if type(i).__name__ not in new_dict.keys():
#         new_dict[type(i).__name__]=[i]
#     else:
#         new_dict[type(i).__name__].append(i)
# print(new_dict)

# old_list=[1,2,2,2,4,7,3,7,8,9]
# new_list=[]
# new_dict={}
# check=0
# for i in old_list:
#     if i not in new_dict.keys():
#         new_dict[i]=[i]
#     else:
#         new_dict[i].append(i)
#
# for item in old_list:
#     if len(new_dict[item])!=2:
#         new_list.append(item)
#
# print(new_list)

# old_list=[1,2,2,2,4,7,3,7,8,9]
# new_list=[]
#
# for i in range (0,len(old_list)):
#     if old_list[i]%2==1:
#         new_list.append(i+1)
# print(new_list)

# data = input('Введите строку: ')
# tmp=data.split()
# tmp.sort()
# longest= len(max(tmp, key=len))
#
# for num, i in enumerate(tmp, 1):
#     print(f'{num} {i:>{longest}}')

# import pprint
#
# data = input('Введите строку: ')
# new_dict = {}
# new_dict2 = {}
# for i in data:
#     if i not in new_dict.keys():
#         new_dict[i] = 1
#     else:
#         new_dict[i] += 1
# print(new_dict)
#
# for i in data:
#     if i not in new_dict2.keys():
#         new_dict2[i]=data.count(i)
#     else:
#         continue
# print(new_dict2)
# pprint.pprint(new_dict2)

old_dict = {'Ваня': ('Нож', 'Рюкзак', 'Палатка'),
            'Игорь': ('Котелок', 'Рюкзак', 'Пенка'),
            'Андрей': ('Палатка', 'Спички', 'Рюкзак'),
            }
list_tuple = []
items = {}
items_2 = {}
uni_items = []
all_name = set(old_dict.keys())

for item in old_dict.values():
    list_tuple.append(set(item))

print(list_tuple)

inter_set = list_tuple[0]

for i in range(1, len(list_tuple)):
    inter_set = list_tuple[i] & inter_set

print(inter_set)

for i in list_tuple:
    for item in i:
        if item not in items:
            items[item] = 1
        else:
            items[item] += 1

for i in items:
    if items[i] == 1:
        uni_items.append(i)

print(uni_items)

for name in old_dict:
    for item in old_dict[name]:
        if item not in items_2:
            items_2[item] = [1, {name}]
        else:
            items_2[item][0] += 1
            items_2[item][1].add(name)

for item in items_2:
    if items_2[item][0] == len(old_dict) - 1:
        print(item)
        print(all_name - items_2[item][1])
print(inter_set)





