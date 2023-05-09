# Создайте функцию foldr(func, lst, acc), вычисляющую свертку справа для элементов списка.
from part2task9 import *


def make_list(*xs):
    if not xs:
        return None
    elif callable(xs[0]):
        return xs[0]
    else:
        return pair(xs[0], make_list(*xs[1:]))


def foldl(func, lst):
    if callable(tail(lst)):
        if lst(1)(0) is not None:
            return foldl(func, make_list(func(lst(0), lst(1)(0)), tail(tail(lst))))
    return lst(0)


def foldr(func, lst):
    return foldl(func, list_reverse(lst))


if __name__ == "__main__":
    print(foldr(lambda x, y: x + y, list_range(1, 10)))
    print(foldr(lambda x, y: x - y, list_range(1, 10)))
    print(foldr(lambda x, y: x * y, list_range(1, 7)))