# 2. Напишите однострочный генератор словаря, который принимает на вход три списка одинаковой длины:
# имена str, ставка int, премия str с указанием процентов вида «10.25%».
# В результате получаем словарь с именем в качестве ключа и суммой
# премии в качестве значения. Сумма рассчитывается
# как ставка умноженная на процент премии


from decimal import Decimal


list_of_names = ['Иван', 'Дмитрий', 'Мария']
list_of_salary = [100, 120, 140]
list_of_extrasalary = ['10.2%', '14.3%', '15.6%']
my_dictcomp = {list_of_names[i]: (Decimal(list_of_salary[i]) * Decimal(list_of_extrasalary[i].replace('%', '')))  for i in range(len(list_of_salary))}


for name, award in my_dictcomp.items():
    print(f"{name} => {award}")