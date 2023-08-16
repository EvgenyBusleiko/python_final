list_1 = [1, 5, 88, 100, 2, -4]
min = int(input("введите минимальное число: "))
max = int(input("введите максимальное число: "))
def find_inx(array: list):
    for i in range(len(array)):
        if array[i] >= min and array[i] <= max:
            return i

list_2 = []
for i in range(len(list_1)):

    list_2.append(find_inx(list_1))
result = [i for i in list_2 if i]
print(result)
