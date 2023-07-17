# Создайте три (или более) отдельных классов животных. Например рыбы, птицы и т.п.
# У каждого класса должны быть как общие свойства, например имя, так и специфичные для класса.
# Для каждого класса создайте метод, выводящий информацию специфичную для данного класса.

class Horse:
    def __init__(self, name, age, power):
        self.name = name
        self.age = age
        self.power = power

class Fish:
    def __init__(self, name, age, tail_length):
        self.name = name
        self.age = age
        self.tail_length = tail_length

class Bird:
    def __init__(self, name, age, fly_speed):
        self.name = name
        self.age = age
        self.fly_speed = fly_speed

