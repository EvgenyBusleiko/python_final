# Добавьте в модуль с загадками функцию, которая принимает на вход строку (текст загадки) и число (номер попытки, с которой она угадана).
# Функция формирует словарь с информацией о результатах отгадывания.
# Для хранения используйте защищённый словарь уровня модуля.
# Отдельно напишите функцию, которая выводит результаты угадывания из защищённого словаря в удобном для чтения виде.
# Для формирования результатов используйте генераторное выражение.

from sem6_4 import riddle_game

_results = dict()


def get_circle_riddles(riddles: dict):
    global _results
    for question, answers in riddles.items():
        _results[question] = riddle_game(question, answers, 3)
        print()
    return _results


def show_results():
    global _results
    for question, result in _results.items():
        print(f"С загадкой: {question}")
        print("Ваш результат: ", end="")
        print(f"Вы угадали с {result} попытки\n" if result != 0 else "Вы не угадали\n")


if __name__ == '__main__':
    riddles_ = {
        "Сидит дед в сто шуб одет, кто его раздевает, тот слёзы проливает": ['лук', 'onion'],
        "Висит груша нельзя скушать": ["лампочка", "лампа", "light bulb"]
    }
    get_circle_riddles(riddles_)
    show_results()
