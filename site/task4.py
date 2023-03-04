def main(n):
    if n == 0:
        return 0.46
    return main(n - 1) - (main(n - 1) ** 2) / 17
