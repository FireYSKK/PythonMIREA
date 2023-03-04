def main(a, n, b, x):
    s = 0
    for j in range(1, b + 1):
        for i in range(1, n + 1):
            for c in range(1, a + 1):
                s += ((j ** 5) + ((15 * x + (i ** 2)) ** 7) + ((28 * c) ** 6))
    return s
