# Возьмите задачу из прошлых домашних заданий.
# Добавьте к ним логирование ошибок и полезной
# информации. Также реализуйте возможность запуска из
# командной строки с передачей параметров.
import argparse
import logging
from functools import wraps
from pathlib import Path


def get_logger():
    DIR_LOGS = Path.cwd() / 'logs'

    if not DIR_LOGS.is_dir():
        DIR_LOGS.mkdir()

    FORMAT_MSG = "{asctime} {levelname} {funcName}: {msg}"
    logging.basicConfig(filename='logs/h_tsk.log', filemode='a', encoding='utf-8', level=logging.INFO, style='{',
                        format=FORMAT_MSG)
    return logging.getLogger()


def log_decorator(func):
    @wraps(func)
    def wrapper(*args):
        logger = get_logger()

        try:
            result = func(*args)

        except:
            logger.error(f'ERORR! args={args}, {func.__name__}')
            return
        if result == None:
            logger.error(f'ERORR! args={args}, {func.__name__}, Сторона не может быть меньше или равна нулю')
            return
        dict1 = {'funcname': func.__name__, 'args': args, 'result': result}
        logger.info(dict1)
        return result

    return wrapper


@log_decorator
def get_length(a, b=None):
    b = a if not b else b
    if a <= 0 or b <= 0:
        return

    return 2 * (a + b)


def get_answer():
    parser = argparse.ArgumentParser(description='side_a side_b')
    parser.add_argument('-a', '--a', default=5)
    parser.add_argument('-b', '--b', default=0)
    arguments = parser.parse_args()

    return get_length(int(arguments.a), int(arguments.b))


if __name__ == '__main__':
    print(get_answer())
