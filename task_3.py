import types
from datetime import datetime
def decorator_view(old_func):
    def new_func(*args, **kwargs):
        print("это сейчас декоратор и время сейчас -", datetime.now())
        return old_func()
    return new_func




def flat_generator(list_of_lists):
    for i in list_of_lists:
        if isinstance(i, list):
            yield from flat_generator(i)
        else:
            yield i

@decorator_view
def test_task_3():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']

    assert isinstance(flat_generator(list_of_lists_2), types.GeneratorType)


test_task_3()