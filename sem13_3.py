# Создайте класс с базовым исключением и дочерние классы-исключения:
# ошибка уровня,
# ошибка доступа.

class UserException(Exception):
    pass


class LevelException(UserException):
    pass


class AccessException(UserException):
    pass
