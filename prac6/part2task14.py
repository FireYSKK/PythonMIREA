#
from part2task8 import *


def concat(xs, ys):
    if xs is None:
        return ys
    else:
        return pair(head(xs), concat(tail(xs), ys))


if __name__ == "__main__":
    print_list(concat(make_list(1, 2, 3), make_list(9, 8, 7)))