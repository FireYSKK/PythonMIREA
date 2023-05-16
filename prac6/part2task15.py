# Создайте функцию list_replace(lst, index, value) для изменения элемента списка по индексу.
from part2task13 import *


def list_replace(lst, index, value):
    if index == 0:
        return make_list(value, lst(1))
    return make_list(lst(0), list_replace(lst(1), index - 1, value))


if __name__ == "__main__":
    a = list_range(1, 10)
    print_list(a)
    print()
    print_list(list_replace(a, 4, "LET'S GO!!!"))
