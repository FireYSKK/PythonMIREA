# Создайте функцию list_to_string(lst), возвращающую строку, содержащую элементы списка.
from part2task2 import *


def list_to_string(lst) -> str:
    if callable(lst):
        return str(lst(0)) + " " + list_to_string(lst(1))
    else:
        return ""


if __name__ == "__main__":
    print(list_to_string(make_list(1, 2, 3, 4, 5)))
