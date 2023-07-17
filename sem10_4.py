# Создайте класс Сотрудник.
# Воспользуйтесь классом человека из прошлого задания.
# У сотрудника должен быть:
# шестизначный идентификационный номер
# уровень доступа вычисляемый как остаток от деления суммы цифр id на семь

class Person:
    def __init__(self, full_name, age, height):
        self.full_name = full_name
        self.__age = age
        self.__height = height

    def get_full_name(self):
        return self.full_name

    def get_age(self):
        return self.__age

    def get_height(self):
        return self.__height

    def birthday(self):
        self.__age += 1
        return self.get_age()


class Employee(Person):
    def __init__(self, full_name, age, height, id):
        super().__init__(full_name, age, height)
        self.id = id

    def get_id(self):
        return self.id

    def get_access_level(self):
        # tmp = 0
        # for i in str(self.id):
        #     tmp += int(i)
        tmp = sum([int(i) for i in str(self.id)])
        return tmp % 7


e1 = Employee('Иванов Иван Иванович', 44, 180, 49)

print(e1.get_age())
print(e1.get_full_name())
print(e1.birthday())

print(e1.get_access_level())
