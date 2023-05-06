# Создайте функцию foldl(func, lst, acc), вычисляющую свертку элементов списка, аналогично reduce.
from part2task4 import *


# def foldl(func, lst):
#     if callable(tail(lst)):
#         return func(lst(0), foldl(func, lst(1)))
#     return lst(0)


def foldl(func, lst):
    if callable(tail(lst)):
        if lst(1)(0) is not None:
            return foldl(func, make_list(func(lst(0), lst(1)(0)), tail(tail(lst))))
    return lst(0)


if __name__ == "__main__":
    print(foldl(lambda x, y: x + y, list_range(1, 10)))
