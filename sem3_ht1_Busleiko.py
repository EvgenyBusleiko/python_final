# Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов
old_list = [1, 2, 2, 2, 4, 7, 3, 7, 8, 9,1]
new_list = []
new_dict = {}
check = 0
for i in old_list:
    if i not in new_dict.keys():
        new_dict[i] = 1

    else:
        new_dict[i]+= 1

for item in new_dict.keys():
    if new_dict[item] != 1:
        new_list.append(item)

print(new_list)
