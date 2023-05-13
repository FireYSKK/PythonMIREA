# Создайте функцию list_filter(pred, lst), аналог filter, с помощью foldr.
from part2task11 import *


def list_filter(func, lst):
    if lst is None:
        return lst
    elif not func(lst(0)):
        return list_filter(func, lst(1))
    return make_list(lst(0), list_filter(func, lst(1)))



if __name__ == "__main__":
    print([11, False, 18, 21, "", 12, 34, 0, [], {}])
    print_list(list_filter(lambda x: bool(x), make_list(11, False, 18, 21, "", 12, 34, 0, [], {})))
    print()
    print_list(list_filter(lambda x: x[0].lower() in 'aeiou', make_list("Petya", "Alesha", "Vasya", "Misha", "Olezha")))
