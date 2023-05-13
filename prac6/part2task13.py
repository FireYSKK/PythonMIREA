# Создайте функцию sum_odd_squares для вычисления суммы квадратов нечетных чисел списка с помощью list_sum, list_map и list_filter.
from part2task12 import *


def sum_odd_squares(lst):
    return list_sum(list_map(lambda x: x ** 2, list_filter(lambda y: y % 2 == 1, lst)))


if __name__ == "__main__":
    print(sum_odd_squares(list_range(1, 10)))
    
    a = []
    for i in range(11):
        if i % 2 == 1:
            a.append(i ** 2)
    print(sum(a))
