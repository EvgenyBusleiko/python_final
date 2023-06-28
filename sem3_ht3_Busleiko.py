# Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.
old_dict = {'Вода': 5000,
            'Нож': 1000,
            'Компас': 750,
            'Тушенка': 2000,




            }
print('Есть предметы')
print(old_dict)
not_full = True
max_weight = int(input('Введите вместимость рюкзака в граммах: '))
now_weight = 0
backpack = {}
min = max_weight
while not_full:
    for i in old_dict.keys():
        if now_weight + old_dict[i] <= max_weight:
            if i not in backpack.keys():
                backpack[i]=[i]
                backpack[i] [0]= 1
                backpack[i].append(old_dict[i])
            else:
                backpack[i][0] += 1
            now_weight += old_dict[i]
        if old_dict[i] < min:
            min = old_dict[i]

    if now_weight + min > max_weight:
        not_full = False
    if min>=max_weight:
        not_full = False

if min >= max_weight:
    print('В рюкзак ничего не влезет')
else:
    print("В рюкзак поместилось:")
    print(backpack)

    print(f'Общий вес {now_weight}')
