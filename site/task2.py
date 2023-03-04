import math


def main(y):
    if y < 147:
        return 4 * y - y ** 4 - y ** 5
    elif y < 189:
        return 92 * (y ** 3) - 44 * (math.tan(68 * (y ** 3)
                                              + y + (y ** 2)) ** 4) - (y ** 2)
    elif y < 283:
        return 85 * (y ** 6)
    return 85 * y
