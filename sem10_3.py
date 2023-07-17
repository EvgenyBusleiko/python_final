# Напишите класс для хранения информации о человеке: ФИО, возраст и т.п. на ваш выбор.
# У класса должны быть методы birthday для увеличения возраста на год, full_name для вывода полного ФИО и т.п. на ваш выбор.
# Убедитесь, что свойство возраст недоступно для прямого изменения, но есть возможность получить текущий возраст.

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


p1 = Person('Иванов Иван Иванович', 44, 180)

print(p1.get_age())
print(p1.get_full_name())
print(p1.birthday())
print(p1._Person__height)
