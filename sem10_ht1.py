# Доработать задачи 5-6. Создайте класс-фабрику.
# ○ Класс принимает тип животного (название одного из созданных классов)
# и параметры для этого типа.
# ○ Внутри класса создайте экземпляр на основе переданного типа и
# верните его из класса-фабрики.
import sys


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age


class Horse(Animal):
    def __init__(self, name, age, power):
        super().__init__(name, age)
        self.power = power

    def get_name(self):
        return 'Secret!'

    def get_power(self):
        return self.power


class Fish(Animal):
    def __init__(self, name, age, tail_length):
        super().__init__(name, age)
        self.tail_length = tail_length


class Bird(Animal):
    def __init__(self, name, age, fly_speed):
        super().__init__(name, age)
        self.fly_speed = fly_speed

    def fly_speed(self):
        return self.fly_speed


class Animalmaker:

    def __init__(self, animal_type: Animal, name, age, extra):
        self.animal_type = animal_type
        self.name = name
        self.age = age
        self.extra = extra

    def make_class(self):
        type_list = ['Bird', 'Horse', 'Fish']

        tmp = self.animal_type(self.name, self.age, self.extra)

        if self.animal_type not in type_list:
            print('Такого класса нет')
            return
        else:
            class_name = (f'{self.animal_type}("{self.name}",{self.age},{self.extra})')
            tmp = eval(class_name)
        return tmp


a1 = Animalmaker(Bird, 'Po-po', 12, 46).make_class()
print(a1.get_name())
print(a1.get_age())
print(a1.fly_speed)
a2 = Animalmaker(Horse, 'Flower', 10, 'bite').make_class()
print(a2.get_name())
print(a2.get_age())
print(a2.power)
a3 = Animalmaker(Fish, 'Ponio', 1, 6).make_class()
print(a3.get_name())
print(a3.get_age())
print(a3.tail_length)

# print(a1.get_name())
