# Создайте функцию fact(n) для вычисления факториала с помощью foldl и list_range.
from part2task6 import *


def fact(n):
    return foldl(lambda x, y: x * y, list_range(1, n))



if __name__ == "__main__":
    print(fact(6))
