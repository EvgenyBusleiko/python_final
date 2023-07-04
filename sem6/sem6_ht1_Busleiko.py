# В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку
import sys
from calendar import isleap


def check_year(year):
    return isleap(year)


def check_date(day, month, year):
    try:
        dt(year=year, month=month, day=day)
    except:
        return False
    return True


if __name__ == '__main__':
    print(sys.argv)
    try:
        day, month, year = map(int, sys.argv[1].split('.'))
        print(day, month, year)

    except:
        print("Неверный формат даты")

    print(check_year(year=year))
    print(check_date(day=day, month=month, year=year))
