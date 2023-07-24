# Напишите функцию для транспонирования матрицы


def matrix_transpon(tmp):
    new_matrix = []
    for i in range(len(tmp[0])):
        tmp_list = []

        for j in range(len(tmp)):
            tmp_list.append(tmp[j][i])
        new_matrix.append(tmp_list)
    return (new_matrix)


def print_matrix(matrix):
    for i in range(len(matrix)):
        print(matrix[i])


my_matrix = [[1, 2, 3], [2, 4, 6], [3, 6, 9], [4, 8, 12], [5, 10, 15]]
print('Старая матрица')
print_matrix(my_matrix)
print('Новая матрица')
print_matrix(matrix_transpon(my_matrix))
