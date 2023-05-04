# Создайте функцию make_list(*args), которая создает список на основе аргументов.
from part2task1 import *


def make_list(*xs):
    if not xs:
        return None
    else:
        return pair(xs[0], make_list(*xs[1:]))


def print_list(lst):
    if callable(lst):
        print(lst(0), end=' ')
        print_list(lst(1))
    else:
        print(lst)


if __name__ == "__main__":
    my_list = make_list(1, 2, 3, 4, 5)
    print_list(my_list)
    print_list(head(my_list))
    print_list(tail(my_list))
    print('fine')
