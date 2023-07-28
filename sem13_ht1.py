# Возьмите задачу из тех, что были на прошлых
# семинарах или в домашних заданиях. Напишите к ней
# классы исключения с выводом подробной информации.
# Поднимайте исключения внутри основного кода. Например
# нельзя создавать прямоугольник со сторонами
# отрицательной длины.
class UserException(Exception):
    pass


class NegativeSideException(UserException):
    def __str__(self):
        return (f'Размер стороны не может отрицательным ')


class TextInputException(UserException):
    def __str__(self):
        return (f'Сторона не может быть текстом ')


class Rectangle:
    def __init__(self, a, b=None):
        b = a if not b else b

        if not (self.isfloat(a)) or not(self.isfloat(b)):
            raise TextInputException
        elif a <= 0 or b <= 0:
            raise NegativeSideException
        else:
            self.a = a
            self.b = b

    def isfloat(self, value):
        try:
            float(value)

            return True
        except ValueError:
            return False


    def get_length(self):
        return 2 * (self.a + self.b)


    def get_area(self):
        return self.a * self.b


c1 = Rectangle(8,-10)
print(c1.get_length())
print(c1.get_area())

# print(int('десять'))
