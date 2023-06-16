hight = int(input('Введите высоту елочки : '))
for i in range(1, hight + 1):
    print(f"{' ' * (hight - i)}{'*' * (i + (i - 1))}")