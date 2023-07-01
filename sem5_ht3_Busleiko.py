def fibonacci(tmp):
    a = 0
    b = 1
    for i in range(tmp):
        yield b
        a, b = b, a + b


dig = int(input('Введите целое число для ряда Фибоначчи : '))

generator = fibonacci(dig)
for i in range(dig):
    print(next(generator))

