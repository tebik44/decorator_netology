import os
import logging


# Доработать декоратор logger в коде ниже. Должен получиться декоратор, который записывает в файл 'main.log'
# дату и время вызова функции, имя функции, аргументы,
# с которыми вызвалась, и возвращаемое значение. Функция test_1 в коде ниже также должна отработать без ошибок.

def logger_for_test_1(old_function):
    logging.basicConfig(level=logging.DEBUG, filename="main.log", datefmt='%Y-%m-%d %H:%M:%S', filemode="w",
                        format="%(asctime)s %(levelname)s %(message)s")
    def new_function(*args, **kwargs):
        result = old_function(*args, **kwargs)
        logging.info(f"Name function: {old_function.__name__} "
                     f"Arguments: {args, kwargs} "
                     f"return object: {result}")
        return result
    return new_function


def test_1():
    path = 'main.log'
    # if os.path.exists(path):
    #     os.remove(path)

    @logger_for_test_2()
    def hello_world():
        return 'Hello World'

    @logger_for_test_2()
    def summator(a, b=0):
        return a + b

    @logger_for_test_2()
    def div(a, b):
        return a / b


    assert 'Hello World' == hello_world(), "Функция не возвращает 'Hello World'"
    result = summator(2, 2)
    assert isinstance(result, int), 'Должно вернуться целое число'
    assert result == 4, '2 + 2 = 4'
    result = div(6, 2)
    assert result == 3, '6 / 2 = 3'

    assert os.path.exists(path), 'файл main.log должен существовать'

    summator(4.3, b=2.2)
    summator(a=0, b=0)

    with open(path) as log_file:
        log_file_content = log_file.read()

    assert 'summator' in log_file_content, 'должно записаться имя функции'
    for item in (4.3, 2.2, 6.5):
        assert str(item) in log_file_content, f'{item} должен быть записан в файл'


# Доработать параметризованный декоратор logger в коде ниже. Должен получиться декоратор, который записывает в файл дату
# и время вызова функции, имя функции, аргументы, с которыми вызвалась, и возвращаемое значение. Путь к файлу должен
# передаваться в аргументах декоратора. Функция test_2 в коде ниже также должна отработать без ошибок.
count = 0
def logger_for_test_2(path = "main.log"):
    def _logger_for_test_2(old_function):
        def new_function(*args, **kwargs):
            global count
            result = old_function(*args, **kwargs)
            logging.basicConfig(level=logging.INFO, filename=path, datefmt='%Y-%m-%d %H:%M:%S', filemode="w",
                                format="%(asctime)s %(levelname)s %(message)s")
            count += 1
            logging.info(f"Name function: {old_function.__name__} "
                         f"Arguments: {args, kwargs} "
                         f"return object: {result}")
            logging.getLogger()
            return result
        return new_function
    return _logger_for_test_2

def test_2():
    paths = ('log_1.log', 'log_2.log', 'log_3.log')

    for path in paths:
        if os.path.exists(path):
            os.remove(path)

        @logger_for_test_2(path)
        def hello_world():
            return 'Hello World'

        @logger_for_test_2(path)
        def summator(a, b=.0):
            return a + b

        @logger_for_test_2(path)
        def div(a, b):
            return a / b

        assert 'Hello World' == hello_world(), "Функция возвращает 'Hello World'"
        result = summator(2, 2)
        assert isinstance(result, int), 'Должно вернуться целое число'
        assert result == 4, '2 + 2 = 4'
        result = div(6, 2)
        assert result == 3, '6 / 2 = 3'
        summator(4.3, b=2.2)

    for path in paths:

        assert os.path.exists(path), f'файл {path} должен существовать'

        with open(path) as log_file:
            log_file_content = log_file.read()

        assert 'summator' in log_file_content, 'должно записаться имя функции'

        for item in (4.3, 2.2, 6.5):
            assert str(item) in log_file_content, f'{item} должен быть записан в файл'


if __name__ == '__main__':
    test_1()
    test_2()