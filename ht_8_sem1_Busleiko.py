from random import randint

num = randint (1,1000)
result="Ты использовал все попытки. Число не угадано!"
print('Привет! Я загадал число от 1 до 1000')
print('У тебя есть 10 попыток, чтобы угадать его')
print('Я буду подсказывать больше оно или меньше названного. Поехали!')
print(num)
count=1
while count<=10:
    number= int (input(f"Попытка №{count}. Введите число: "))
    if number>num:
        print ("Число меньше")
    elif number<num:
        print ("Число больше")
    else:
        result=f'Верно! Ты угадал с {count} попытки'
        break
    count+=1
print(result)