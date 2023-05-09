# Создайте функцию list_reverse(lst) для разворота списка в обратном направлении с помощью foldl.
from part2task14 import *


def list_reverse(lst):
    if lst is None:
        return lst
    else:
        return concat(list_reverse(tail(lst)), pair(head(lst), None))

    # def reverse(arg1, arg2):
    #     return make_list(arg2, arg1)
    #
    # return foldl(reverse, lst)


def print_list(lst):
    if callable(lst):
        print_list(lst(0))
        print_list(lst(1))
    elif lst is not None:
        print(lst, end=' ')


if __name__ == "__main__":
    print_list(list_reverse(make_list(1, 2, 3, 4, 5, 6)))
