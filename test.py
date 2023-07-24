from random import randint as rnd


def make_matrix(col, row):
    matrix = []
    for i in range(col):
        line = []
        for j in range(row):
            tmp = rnd(1, 10)
            line.append(tmp)
        matrix.append(line)
    return matrix


def check_matrix(a, b):
    line = []
    max_col = (max(len(a), len(b)))
    max_line = (max(len(a[0]), len(b[0])))
    print(max_col, max_line)
    for i in range(0, max_col):
        if len(a) <= i:
            a.append(line)
        if len(b) <= i:
            b.append(line)
        for j in range(0, max_line):
            if len(a[i]) <= j:
                a[i].append(0)
            if len(b[i]) <= j:
                b[i].append(0)
    # print(a)
    # print(b)
    return a, b


a = make_matrix(5, 2)
b = make_matrix(4, 3)

print(a)
print(b)

a, b = check_matrix(a, b)

print(a)
print(b)
