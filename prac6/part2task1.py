# Создайте функцию pair(head, tail), которая порождает элемент списка. Не используйте ветвления.
# Создайте также функции head(lst) (возвращает значение головы списка) и tail(lst) (возвращает хвост списка).
def pair(head, tail=None):
    return lambda i: head if i == 0 else tail


def head(xs):
    return xs(0)


def tail(xs):
    return xs(1)
