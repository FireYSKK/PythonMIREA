# Создайте функцию list_range(low, high), возвращающую список чисел от low до high включительно.
from part2task3 import *


def list_range(low, high):
    if low > high:
        high = low
    return make_list(*range(low, high + 1))


if __name__ == "__main__":
    print(list_to_string(list_range(1, 7)))
