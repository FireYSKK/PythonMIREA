# Создайте функцию list_sum(lst) для вычисления суммы элементов списка с помощью foldl.
from part2task5 import *


def list_sum(lst):
    return foldl(lambda x, y: x + y, lst)



if __name__ == "__main__":
    print(list_sum(list_range(1, 100)))
