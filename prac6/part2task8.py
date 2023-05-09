# Создайте функцию list_to_py(lst) для преобразования списка в обычный список Питона с помощью foldl.
from part2task7 import *


def list_to_py(lst) -> list:
    def sum_list(list1, list2):
        if not type(list1) is list:
            list1 = [list1]
        if not type(list2) is list:
            list2 = [list2]

        list1.extend(list2)
        return list1

    return foldl(sum_list, lst)


if __name__ == "__main__":
    print(list_to_py(make_list(1, 2, "3", -4, 5, dict(next=6), 7)))
