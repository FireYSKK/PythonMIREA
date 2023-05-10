# Создайте функцию list_map(func, lst), аналог map, с помощью foldr.
from part2task10 import *


def list_map(func, lst):
    if not lst:
        return lst
    if not lst(0):
        return list_map(func, lst(1))
    return make_list(func(lst(0)), list_map(func, lst(1)))


if __name__ == "__main__":
    print_list(list_map(lambda x: x * 2 + 3, make_list(10, 15, 21, 33, 42, 55)))
